$ErrorActionPreference='Stop'
$PSNativeCommandArgumentPassing='Legacy'
$ProgressPreference='SilentlyContinue'
$bin = Split-Path -Parent $PSCommandPath
$root=Join-Path ([IO.Path]::GetTempPath()) ('nfai-kimi-regression-'+[Guid]::NewGuid().ToString('N'))
[void][IO.Directory]::CreateDirectory($root)
[void][IO.Directory]::CreateDirectory((Join-Path $root 'ram'))
[void][IO.Directory]::CreateDirectory((Join-Path $root 'state'))
$stub=Join-Path $root 'wsl.py'
$mockdpapi=Join-Path $root 'test.dpapi'
ConvertFrom-SecureString (ConvertTo-SecureString 'nvapi-testonly' -AsPlainText -Force) | Set-Content -LiteralPath $mockdpapi -Encoding ASCII
$python=@'
from pathlib import Path
import base64
import os
import re
import subprocess
import sys

prefix = ['-d', 'Ubuntu-24.04', '-u', 'nfai-test',
          '--cd', '/home/nfai-test/code/NFAI', '--exec']
assert sys.argv[1:8] == prefix, sys.argv[1:8]
args = sys.argv[8:]
root = Path(__file__).parent
ram = root / 'ram'
temp = root / 'state'
if args[0] == '/usr/bin/python3':
    binary, flag, loader, encoded, phase, token = args
    assert flag == '-c'
    assert loader == "exec(__import__('base64').b64decode(__import__('sys').argv.pop(1)))"
    if phase == 'probe' and os.environ.get('NFAI_TEST_FAIL_PROBE'):
        print('Simulated WSL stderr', file=sys.stderr)
        sys.exit(2)
    source = base64.b64decode(encoded).decode()
    source = source.replace("Path('/tmp')", f'Path({str(temp)!r})')
    source = source.replace("(Path('/run/user') / str(os.getuid()), Path('/run/lock'))", f"(Path({str(ram)!r}),)")
    source = source.replace('path.stat().st_uid == os.getuid()', 'path.parent in (directory.parent, runtime_roots[0])')
    source = source.replace('private = info.st_uid == os.getuid() and not info.st_mode & 0o022', 'private = True')
    source = re.sub(r'        filesystem = subprocess\.run\(.*?\n        if filesystem\.returncode == 0 and filesystem\.stdout\.strip\(\) == .tmpfs.:', '        if True:', source, count=1, flags=re.S)
    cmd = [sys.executable, flag, loader, base64.b64encode(source.encode()).decode(), phase, token]
    data = sys.stdin.buffer.read() if phase != 'cleanup' else b''
    r = subprocess.run(cmd, input=data)
    sys.exit(r.returncode)
assert args[0] == '/usr/bin/env'
assert args[-3:-1] == ['resume', '--last']
prompt = args[-1]
token = re.search(r'/tmp/nfai-kimi-([a-f0-9]{32})/run.py --smoke', prompt).group(1)
directory = temp / f'nfai-kimi-{token}'
credential = ram / f'nfai-kimi-{token}' / 'credential'
assert Path((directory / 'credential-path').read_text('utf-8')) == credential
assert not (directory / 'credential').exists()
assert credential.read_bytes() == b'nvapi-testonly'
assert 'KIMI_MODEL_API_KEY' not in os.environ
kimi_stub = root / 'kimi.py'
kimi_stub.write_text(
    "import os,sys\n"
    "assert os.environ['KIMI_MODEL_PROVIDER_TYPE'] == 'openai'\n"
    "assert os.environ['KIMI_MODEL_BASE_URL'] == 'https://integrate.api.nvidia.com/v1'\n"
    "assert os.environ['KIMI_MODEL_NAME'] == 'moonshotai/kimi-k3.1-pro'\n"
    "assert os.path.basename(os.environ['KIMI_CODE_HOME']) == 'state'\n"
    "assert os.environ['KIMI_MODEL_API_KEY'] == 'nvapi-testonly'\n"
    "assert sys.argv[1] == '--agent-file'\n"
    "print('KIMI_OK')\n"
    "print(os.environ['KIMI_MODEL_API_KEY'], file=sys.stderr)\n",
    encoding='utf-8')
runner = directory / 'run.py'
source = runner.read_text('utf-8')
source = source.replace("[str(Path.home() / '.kimi-code/bin/kimi')]", repr([sys.executable, str(kimi_stub)]))
runner.write_text(source, encoding='utf-8')
r = subprocess.run([sys.executable, str(runner), '--smoke'], capture_output=True)
assert r.returncode == 0, r.stderr
assert r.stdout.splitlines() == [b'KIMI_OK', b'KIMI_EXIT=0']
assert r.stderr.strip() == b'[REDACTED]'
print('MOCK_KIMI_RESPONSE_VALIDATED')

'@
[IO.File]::WriteAllText($stub,$python,[Text.UTF8Encoding]::new($false))
$target=Join-Path $bin 'Start-NFAI-Kimi-WSL.ps1'
$source=[IO.File]::ReadAllText($target)
$source=$source.Replace('$wsl = Join-Path $env:SystemRoot ''System32\wsl.exe''','$wsl = (Get-Command python.exe).Source')
$source=$source.Replace('$linux = @(',('$linux = @('+"'"+$stub+"', "))
try {
    & ([ScriptBlock]::Create($source)) -LinuxUser nfai-test -CredentialPath $mockdpapi
    if (Get-ChildItem -LiteralPath (Join-Path $root 'ram'),(Join-Path $root 'state') -Force) { throw 'Mock cleanup left a session' }
    $env:NFAI_TEST_FAIL_PROBE='1'
    try {
        & ([ScriptBlock]::Create($source)) -LinuxUser nfai-test -CredentialPath (Join-Path $root 'missing.dpapi')
        throw 'Native probe unexpectedly continued'
    } catch {
        if ($_.Exception.Message -notlike '*WSL probe failed (exit 2). Simulated WSL stderr*') { throw }
        'MOCK_WSL_EXIT_AND_STDERR_VALIDATED'
    }
} finally {
    Remove-Item Env:NFAI_TEST_FAIL_PROBE -ErrorAction SilentlyContinue
    $resolved=(Resolve-Path -LiteralPath $root).Path
    $parent=(Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path.TrimEnd('\')+'\'
    if ($resolved.StartsWith($parent,[StringComparison]::OrdinalIgnoreCase) -and (Split-Path -Leaf $resolved) -like 'nfai-kimi-regression-*') {
        Remove-Item -LiteralPath $resolved -Recurse -Force
    }
}
