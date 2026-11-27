#requires -Version 5.1
# Archived Windows prototype. Task Scheduler activation and live dispatch were not verified.
# The NFAI direct integration pilot uses the WSL launcher in the parent directory.
[CmdletBinding()]
param(
    [Parameter(Mandatory)][ValidateSet('Install','Worker','Submit','Status','Result')]
    [string]$Action,
    [ValidateSet('claude','kimi')][string]$Agent,
    [string]$PromptFile,
    [ValidatePattern('^[0-9a-f]{32}$')][string]$JobId,
    [switch]$NonConfidential
)

$ErrorActionPreference = 'Stop'
$taskName = 'NFAI Direct Agents'
$engine = Join-Path $env:USERPROFILE 'NFAI-Free-Engine'
$runnerRoot = Join-Path $engine 'tests\headless-20261125-a40ac270'
$runner = Join-Path $runnerRoot 'start-bounded.ps1'
$router = Join-Path $engine 'Start_NFAI_Router.ps1'
$queue = Join-Path $PSScriptRoot 'NFAI-Direct-Agent-Jobs'
$heartbeat = Join-Path $queue 'worker.json'
$powerShell = Join-Path $env:WINDIR 'System32\WindowsPowerShell\v1.0\powershell.exe'
$chat = @{ claude = '10'; kimi = '11' }
$utf8 = [System.Text.UTF8Encoding]::new($false, $true)

function Write-Json($Path, $Data) {
    $pending = "$Path.$PID.pending"
    [IO.File]::WriteAllText($pending, ($Data | ConvertTo-Json -Depth 5 -Compress), $utf8)
    if ([IO.File]::Exists($Path)) {
        [IO.File]::Replace($pending, $Path, $null)
    } else {
        [IO.File]::Move($pending, $Path)
    }
}

function Read-Json($Path) {
    [IO.File]::ReadAllText($Path, $utf8) | ConvertFrom-Json
}

function Get-Time {
    [DateTime]::UtcNow.ToString('o')
}

function Get-PromptHash($Path) {
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Add-Job($Executor, [byte[]]$Bytes, $Expected) {
    if ($Bytes.Length -lt 1 -or $Bytes.Length -gt 24000) {
        throw 'Use a UTF-8 task brief between 1 and 24000 bytes.'
    }
    $brief = $utf8.GetString($Bytes)
    if ([string]::IsNullOrWhiteSpace($brief) -or $brief.Contains([char]0)) {
        throw 'Use a non-empty UTF-8 task brief.'
    }
    $id = [guid]::NewGuid().ToString('N')
    $pending = Join-Path $queue "pending-$id"
    [IO.Directory]::CreateDirectory($pending) | Out-Null
    $prompt = Join-Path $pending 'prompt.txt'
    [IO.File]::WriteAllBytes($prompt, $Bytes)
    Write-Json (Join-Path $pending 'request.json') @{
        agent = $Executor; submitted = Get-Time; prompt_sha256 = Get-PromptHash $prompt
        expected = $Expected
    }
    [IO.Directory]::Move($pending, (Join-Path $queue $id))
    [pscustomobject]@{ job_id = $id; agent = $Executor; state = 'queued' }
}

function Confirm-Runner {
    $files = @{
        'start-bounded.ps1' = 'B9C7EC9B916897C49EF27487818E5327246B94D3CEBC7AB00306521C6D225D0B'
        'run-bounded.py' = '26693C1DEA92E6E18C261E19170BE071F1EB35BBC3CF8B73184D1180D4BA9E73'
    }
    foreach ($name in $files.Keys) {
        if ((Get-PromptHash (Join-Path $runnerRoot $name)) -ne $files[$name]) {
            throw "The reviewed agent runner changed: $name."
        }
    }
}

function Test-Router {
    try {
        $health = Invoke-WebRequest -UseBasicParsing -Uri 'http://127.0.0.1:20128/api/health' -TimeoutSec 2
        return $health.StatusCode -eq 200
    } catch {
        return $false
    }
}

function Start-ExistingRouter {
    if (Test-Router) { return }
    $process = Start-Process -FilePath $powerShell -ArgumentList @(
        '-NoProfile', '-NonInteractive', '-File', ('"{0}"' -f $router)
    ) -WindowStyle Hidden -PassThru
    for ($attempt = 0; $attempt -lt 25; $attempt++) {
        Start-Sleep -Seconds 1
        if (Test-Router) { return }
        if ($process.HasExited) { break }
    }
    throw 'The existing OmniRoute did not respond on 127.0.0.1:20128.'
}

function Read-AgentReply($Executor, $RunDirectory) {
    $output = Join-Path $RunDirectory 'stdout.log'
    if ($Executor -eq 'claude') {
        $response = Read-Json $output
        if ($response.type -eq 'result' -and $response.subtype -eq 'success' -and $response.is_error -eq $false) {
            return [string]$response.result
        }
        return
    }
    $messages = foreach ($line in [IO.File]::ReadLines($output, $utf8)) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $event = $line | ConvertFrom-Json
        if ($event.role -eq 'assistant' -and $event.content -is [string] -and -not $event.tool_calls) {
            $event.content
        }
    }
    return $messages -join ''
}

function Finish-Job($Directory, $Request, $RunDirectory) {
    $path = Join-Path $RunDirectory 'exit.json'
    $state = 'failed'
    $code = $null
    $reason = 'runner_exited_without_receipt'
    if (Test-Path -LiteralPath $path -PathType Leaf) {
        $receipt = Read-Json $path
        if ($receipt.job_id -cne $Directory.Name -or $receipt.executor -cne $Request.agent -or
            $receipt.prompt_sha256 -ne $Request.prompt_sha256) {
            $reason = 'runner_receipt_mismatch'
        } else {
            $code = $receipt.exit_code
            $reason = $receipt.state
            if ($receipt.state -eq 'exited' -and $null -ne $code -and $code -eq 0) {
                $reply = Read-AgentReply $Request.agent $RunDirectory
                $reason = 'runner_returned_no_reply'
                if (-not [string]::IsNullOrWhiteSpace($reply)) {
                    if ($Request.expected -and $reply.Trim() -cne $Request.expected) {
                        $reason = 'acceptance_reply_mismatch'
                    } else {
                        $state = 'completed'
                        $reason = 'agent_reply_received'
                        [IO.File]::WriteAllText((Join-Path $Directory.FullName 'reply.txt'), $reply, $utf8)
                    }
                }
            } elseif ($receipt.state -eq 'timed_out') {
                $state = 'timed_out'
            }
        }
    }
    Write-Json (Join-Path $Directory.FullName 'result.json') @{
        job_id = $Directory.Name; agent = $Request.agent; state = $state
        exit_code = $code; reason = $reason; finished = Get-Time
    }
}

function Find-JobProcess($Run) {
    if (-not $Run.pid -or -not $Run.process_started) { return }
    try {
        $process = Get-Process -Id $Run.pid
        if ($process.StartTime.ToUniversalTime().ToString('o') -ceq $Run.process_started) {
            return $process
        }
    } catch {}
}

function Get-Jobs {
    Get-ChildItem -LiteralPath $queue -Directory |
        Where-Object { $_.Name -cmatch '^[0-9a-f]{32}$' -and
            -not ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) } |
        Sort-Object CreationTimeUtc, Name
}

function Invoke-Worker {
    $mutex = [Threading.Mutex]::new($false, 'Local\NFAI-Direct-Agent-Worker')
    $ownsMutex = $false
    try {
        try { $ownsMutex = $mutex.WaitOne(0) } catch [Threading.AbandonedMutexException] {
            $ownsMutex = $true
        }
        if (-not $ownsMutex) { return }
        while ($true) {
            Write-Json $heartbeat @{ pid = $PID; updated = Get-Time }
            $active = @{}
            $queued = @()
            foreach ($dir in @(Get-Jobs)) {
                $result = Join-Path $dir.FullName 'result.json'
                if (Test-Path -LiteralPath $result) { continue }
                try {
                    $request = Read-Json (Join-Path $dir.FullName 'request.json')
                    if ($request.agent -cnotin @('claude', 'kimi')) { throw 'Unknown agent.' }
                    $runDirectory = Join-Path $runnerRoot ("chat-{0}-{1}" -f $chat[$request.agent], $dir.Name)
                    $runPath = Join-Path $dir.FullName 'run.json'
                    if (Test-Path -LiteralPath $runPath) {
                        $process = Find-JobProcess (Read-Json $runPath)
                        if ($process -and -not $process.HasExited) {
                            $active[$request.agent] = $true
                        } else {
                            Finish-Job $dir $request $runDirectory
                        }
                    } else {
                        $queued += [pscustomobject]@{ dir = $dir; request = $request; runPath = $runPath }
                    }
                } catch {
                    Write-Json $result @{
                        job_id = $dir.Name; state = 'failed'; reason = 'invalid_job_or_receipt'; finished = Get-Time
                    }
                }
            }
            foreach ($job in $queued) {
                $executor = $job.request.agent
                if ($active[$executor]) { continue }
                $dir = $job.dir
                $prompt = Join-Path $dir.FullName 'prompt.txt'
                $stage = 'validate_runner_and_prompt'
                try {
                    Confirm-Runner
                    $info = Get-Item -LiteralPath $prompt
                    if (($info.Attributes -band [IO.FileAttributes]::ReparsePoint) -or
                        $info.Length -gt 24000 -or (Get-PromptHash $prompt) -ne $job.request.prompt_sha256) {
                        throw 'The task brief changed.'
                    }
                    if ($executor -eq 'claude') {
                        $stage = 'omniroute_unavailable'
                        Start-ExistingRouter
                    }
                    $stage = 'runner_launch_failed'
                    Write-Json $job.runPath @{ started = Get-Time }
                    $process = Start-Process -FilePath $powerShell -ArgumentList @(
                        '-NoProfile', '-NonInteractive', '-File', ('"{0}"' -f $runner),
                        '-Chat', $chat[$executor], '-JobId', $dir.Name,
                        '-PromptFile', ('"{0}"' -f $prompt)
                    ) -WorkingDirectory $runnerRoot -WindowStyle Hidden -PassThru
                    try { $processStart = $process.StartTime.ToUniversalTime().ToString('o') }
                    catch { $processStart = $null }
                    Write-Json $job.runPath @{
                        started = Get-Time; pid = $process.Id; process_started = $processStart
                    }
                    $active[$executor] = $true
                } catch {
                    Write-Json (Join-Path $dir.FullName 'result.json') @{
                        job_id = $dir.Name; agent = $executor; state = 'failed'
                        reason = $stage; finished = Get-Time
                    }
                }
            }
            Start-Sleep -Seconds 3
        }
    } finally {
        if ($ownsMutex) { $mutex.ReleaseMutex() }
        $mutex.Dispose()
    }
}

function Get-State($Directory) {
    $result = Join-Path $Directory.FullName 'result.json'
    if (Test-Path -LiteralPath $result) { return Read-Json $result }
    $request = Read-Json (Join-Path $Directory.FullName 'request.json')
    $state = 'queued'
    if (Test-Path -LiteralPath (Join-Path $Directory.FullName 'run.json')) { $state = 'running' }
    [pscustomobject]@{ job_id = $Directory.Name; agent = $request.agent; state = $state; submitted = $request.submitted }
}

[IO.Directory]::CreateDirectory($queue) | Out-Null
switch ($Action) {
    'Install' {
        if (-not $NonConfidential) {
            throw 'Use -NonConfidential for the two synthetic tests with your existing NVIDIA Developer Program access.'
        }
        Confirm-Runner
        $user = [Security.Principal.WindowsIdentity]::GetCurrent().Name
        $taskAction = New-ScheduledTaskAction -Execute $powerShell -Argument (
            '-NoProfile -NonInteractive -WindowStyle Hidden -File "{0}" -Action Worker' -f $PSCommandPath
        ) -WorkingDirectory $PSScriptRoot
        $trigger = New-ScheduledTaskTrigger -AtLogOn -User $user
        $principal = New-ScheduledTaskPrincipal -UserId $user -LogonType Interactive -RunLevel Limited
        $taskOptions = @{
            AllowStartIfOnBatteries = $true; DontStopIfGoingOnBatteries = $true; StartWhenAvailable = $true
            ExecutionTimeLimit = [TimeSpan]::Zero; MultipleInstances = 'IgnoreNew'
            RestartCount = 3; RestartInterval = New-TimeSpan -Minutes 1
        }
        $settings = New-ScheduledTaskSettingsSet @taskOptions
        $registration = @{
            TaskName = $taskName; Action = $taskAction; Trigger = $trigger; Principal = $principal
            Settings = $settings; Force = $true
        }
        Register-ScheduledTask @registration | Out-Null
        Start-ScheduledTask -TaskName $taskName
        foreach ($executor in 'kimi', 'claude') {
            $marker = 'NFAI_DIRECT_' + $executor.ToUpperInvariant() + '_OK'
            Add-Job $executor ($utf8.GetBytes("Reply with exactly $marker. Do not use tools.")) $marker
        }
    }
    'Worker' { Invoke-Worker }
    'Submit' {
        if (-not $NonConfidential -or -not $Agent -or -not $PromptFile) {
            throw 'Supply -Agent, -PromptFile, and -NonConfidential.'
        }
        $source = Get-Item -LiteralPath $PromptFile
        if ($source.Length -gt 24000) { throw 'Use a UTF-8 task brief of up to 24000 bytes.' }
        Add-Job $Agent ([IO.File]::ReadAllBytes($source.FullName)) $null
    }
    'Status' {
        $worker = $null
        if (Test-Path -LiteralPath $heartbeat) { $worker = Read-Json $heartbeat }
        $jobs = @(Get-Jobs)
        if ($JobId) { $jobs = @($jobs | Where-Object Name -ceq $JobId) }
        [pscustomobject]@{
            worker = $worker; jobs = @($jobs | Select-Object -Last 20 | ForEach-Object { Get-State $_ })
        } | ConvertTo-Json -Depth 5
    }
    'Result' {
        if (-not $JobId) { throw 'Supply -JobId.' }
        $dir = Get-Item -LiteralPath (Join-Path $queue $JobId)
        $state = Get-State $dir
        if ($state.state -ne 'completed') { throw "Job state: $($state.state)." }
        [IO.File]::ReadAllText((Join-Path $dir.FullName 'reply.txt'), $utf8)
    }
}
