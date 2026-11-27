#requires -Version 5.1
[CmdletBinding()]
param(
    [string]$Distribution = 'Ubuntu-24.04',
    [string]$LinuxUser = $env:USERNAME.ToLowerInvariant(),
    [string]$LinuxHome,
    [string]$Workspace,
    [string]$CredentialPath = (Join-Path $env:LOCALAPPDATA 'NFAI\Secrets\kimi-nvidia.dpapi')
)

$ErrorActionPreference = 'Stop'

$wsl = Join-Path $env:SystemRoot 'System32\wsl.exe'
if (-not $LinuxHome) { $LinuxHome = "/home/$LinuxUser" }
if (-not $Workspace) { $Workspace = "$LinuxHome/code/NFAI" }
$session = [Guid]::NewGuid().ToString('N')
$helper = "/tmp/nfai-kimi-$session/run.py"

$bootstrap = @'
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

runner = r'''
import os
import subprocess
import sys
from pathlib import Path

if len(sys.argv) != 2 or not sys.argv[1].strip():
    raise SystemExit('Supply one prompt, or --smoke for the connection test.')

directory = Path(__file__).resolve().parent
credential = Path((directory / 'credential-path').read_text('utf-8'))
try:
    key = credential.read_bytes().strip()
except OSError as error:
    raise SystemExit(f'KIMI_CREDENTIAL_UNAVAILABLE: {error.strerror}.')
environment = dict(os.environ)
environment.update(
    KIMI_CODE_HOME=str(directory / 'state'),
    KIMI_MODEL_PROVIDER_TYPE='openai',
    KIMI_MODEL_NAME='moonshotai/kimi-k3.1-pro',
    KIMI_MODEL_BASE_URL='https://integrate.api.nvidia.com/v1',
    KIMI_MODEL_MAX_CONTEXT_SIZE='1048576',
    KIMI_MODEL_API_KEY=key.decode('ascii'),
)
args = [str(Path.home() / '.kimi-code/bin/kimi')]
smoke = sys.argv[1] == '--smoke'
if smoke:
    args.extend(('--agent-file', str(directory / 'smoke.md')))
    prompt = 'Reply with exactly KIMI_OK. Do not use tools.'
else:
    prompt = sys.argv[1]
args.append('--prompt=' + prompt)

try:
    result = subprocess.run(args, env=environment, capture_output=True,
                            timeout=180 if smoke else None)
except subprocess.TimeoutExpired:
    raise SystemExit('KIMI_TIMEOUT after 180 seconds.')
for stream, output in ((sys.stdout.buffer, result.stdout),
                       (sys.stderr.buffer, result.stderr)):
    stream.write(output.replace(key, b'[REDACTED]'))
    stream.flush()
print(f'KIMI_EXIT={result.returncode}')
raise SystemExit(result.returncode)
'''

mode, token = sys.argv[1:]
if not re.fullmatch('[0-9a-f]{32}', token):
    raise SystemExit('Invalid session identifier.')
session_name = f'nfai-kimi-{token}'
directory = Path('/tmp') / session_name
runtime_roots = (Path('/run/user') / str(os.getuid()), Path('/run/lock'))
if mode == 'cleanup':
    for path in (directory, *(root / session_name for root in runtime_roots)):
        if path.is_dir() and not path.is_symlink() and path.stat().st_uid == os.getuid():
            shutil.rmtree(path)
    raise SystemExit(0)
def find_runtime_root():
    for root in runtime_roots:
        if not root.is_dir() or not os.access(root, os.W_OK | os.X_OK):
            continue
        info = root.stat()
        private = info.st_uid == os.getuid() and not info.st_mode & 0o022
        sticky = info.st_uid == 0 and bool(info.st_mode & stat.S_ISVTX)
        if not (private or sticky):
            continue
        filesystem = subprocess.run(
            ['/usr/bin/stat', '-f', '-c', '%T', '--', str(root)],
            capture_output=True, text=True)
        if filesystem.returncode == 0 and filesystem.stdout.strip() == 'tmpfs':
            return root
    raise SystemExit('No writable protected tmpfs directory under /run in this Ubuntu session.')

runtime_root = find_runtime_root()
if mode == 'probe':
    if sys.stdin.buffer.read(64).strip() != b'nfai-wsl-pipe-probe':
        raise SystemExit('WSL did not deliver the test line on stdin.')
    print('KIMI_WSL_PIPE_OK')
    raise SystemExit(0)
if mode != 'setup':
    raise SystemExit('Unknown launcher operation.')
secret = sys.stdin.buffer.read(4097).strip()
if not 12 <= len(secret) <= 4096 or not re.fullmatch(rb'nvapi-[A-Za-z0-9._-]+', secret):
    raise SystemExit('The stored credential is not in the expected NVIDIA API key format.')

os.umask(0o077)
directory.mkdir(mode=0o700)
(directory / 'state').mkdir(mode=0o700)
credential_directory = runtime_root / session_name
credential_directory.mkdir(mode=0o700)
credential = credential_directory / 'credential'
credential.write_bytes(secret)
(directory / 'credential-path').write_text(str(credential), encoding='utf-8')
(directory / 'run.py').write_text(runner, encoding='utf-8')
(directory / 'smoke.md').write_text(
    '---\nname: nfai-smoke\ndescription: Kimi connectivity test\ntools: []\nsubagents: []\n---\n'
    'Return the requested marker. Use only the supplied prompt.\n', encoding='utf-8')
print('KIMI_CREDENTIAL_READY')
'@
$encodedBootstrap = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($bootstrap))
$pythonLoader = "exec(__import__('base64').b64decode(__import__('sys').argv.pop(1)))"
$linux = @('-d', $Distribution, '-u', $LinuxUser, '--cd', $Workspace, '--exec')
$secure = $null
$pointer = [IntPtr]::Zero
$key = $null
$setupAttempted = $false

function Invoke-WslBootstrap([string]$Phase, [string]$InputLine, [string]$Expected) {
    $nativeArguments = $linux + @('/usr/bin/python3', '-c', $pythonLoader, $encodedBootstrap, $Phase, $session)
    # Capture native diagnostics on both Windows PowerShell 5.1 and PowerShell 7.
    $ErrorActionPreference = 'Continue'
    if ($InputLine) {
        $output = @($InputLine | & $wsl @nativeArguments 2>&1)
    } else {
        $output = @(& $wsl @nativeArguments 2>&1)
    }
    $exitCode = $LASTEXITCODE
    $lines = @($output | ForEach-Object {
        $line = $_.ToString().Replace([string][char]0, '')
        if ($InputLine) { $line = $line.Replace($InputLine, '[REDACTED]') }
        $line -creplace 'nvapi-[A-Za-z0-9._-]+', '[REDACTED]'
    })
    if ($exitCode -ne 0 -or ($Expected -and $Expected -cnotin $lines)) {
        $details = $lines -join [Environment]::NewLine
        if ([string]::IsNullOrWhiteSpace($details)) { $details = 'No output was returned.' }
        throw "WSL $Phase failed (exit $exitCode). $details"
    }
    if ($Expected) { Write-Host $Expected }
}

try {
    Invoke-WslBootstrap probe 'nfai-wsl-pipe-probe' 'KIMI_WSL_PIPE_OK'
    try {
        $secure = ConvertTo-SecureString -String ([IO.File]::ReadAllText($CredentialPath).Trim())
        $pointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
        $key = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($pointer)
        $setupAttempted = $true
        Invoke-WslBootstrap setup $key 'KIMI_CREDENTIAL_READY'
    } finally {
        if ($pointer -ne [IntPtr]::Zero) {
            [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($pointer)
        }
        if ($secure) { $secure.Dispose() }
        $key = $null
    }

    $linuxPath = "PATH=${LinuxHome}/.local/bin:${LinuxHome}/.kimi-code/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    $prompt = "Run /usr/bin/python3 $helper --smoke exactly once in the current sandbox. This launches Kimi Code directly against NVIDIA on the existing free route. Report the actual assistant reply and KIMI_EXIT, or the exact failure. Do not open or print credential files, call PowerShell, use OmniRoute for Kimi, or test Claude again. For later Kimi tasks in this session, pass the complete prompt as the only argument to the same Python launcher."
    & $wsl @linux /usr/bin/env $linuxPath "$LinuxHome/.local/bin/codex" --sandbox workspace-write -c 'sandbox_workspace_write.network_access=true' resume --last $prompt
    if ($LASTEXITCODE -ne 0) { throw "Codex exited with code $LASTEXITCODE." }
} finally {
    if ($setupAttempted) {
        try {
            Invoke-WslBootstrap cleanup
        } catch {
            Write-Warning ("Could not remove temporary Kimi session data. " + $_.Exception.Message)
        }
    }
}