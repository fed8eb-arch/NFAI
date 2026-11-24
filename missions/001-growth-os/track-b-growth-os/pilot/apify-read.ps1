# NFAI Growth OS / Apify: Windows current-user DPAPI, named dataset, read-only QC.
# No Actor launches, no subscription changes, no secrets in arguments or output.
[CmdletBinding()]
param(
    [switch]$Initialize,
    [string]$DatasetId,
    [ValidateRange(1,1000)][int]$Limit = 100
)
$ErrorActionPreference = 'Stop'
$secretFile = Join-Path $env:LOCALAPPDATA 'NFAI-Free-Engine\secrets\apify.dpapi'
$adapter = Join-Path $PSScriptRoot 'creative-qc.cjs'
$datasetName = 'nfai-growth-os-observations'
$secure = $null
$ptr = [IntPtr]::Zero
$phase = 'preflight'
try {
    if ($Initialize -and $DatasetId) { throw 'Choose Initialize or DatasetId, not both.' }
    if (-not $Initialize -and $DatasetId -notmatch '^[A-Za-z0-9]{10,40}$') { throw 'DatasetId required.' }
    if (-not (Test-Path -LiteralPath $secretFile -PathType Leaf)) { throw 'DPAPI file missing.' }
    if (-not (Test-Path -LiteralPath $adapter -PathType Leaf)) { throw 'QC adapter missing.' }
    $node = Get-Command node.exe -CommandType Application -ErrorAction Stop | Select-Object -First 1
    $version = & $node.Source --version
    if ($LASTEXITCODE -ne 0 -or "$version" -notmatch '^v(\d+)\.') { throw 'Node version unavailable.' }
    if ([int]$Matches[1] -lt 18) { throw 'Node 18+ required.' }
    $phase = 'credential'
    $secure = Get-Content -LiteralPath $secretFile -Raw | ForEach-Object { $_.Trim() } | ConvertTo-SecureString
    $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
    $env:APIFY_TOKEN = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
    $ptr = [IntPtr]::Zero
    $secure.Dispose()
    $secure = $null
    if ($env:APIFY_TOKEN -notmatch '^[-_A-Za-z0-9]{10,256}$') { throw 'Invalid token shape.' }
    if ($Initialize) {
        $phase = 'dataset-initialize'
        $response = Invoke-RestMethod -Method Post -Uri ('https://api.apify.com/v2/datasets?name=' + $datasetName) -Headers @{Authorization = ('Bearer ' + $env:APIFY_TOKEN)} -MaximumRedirection 0 -TimeoutSec 20 -ErrorAction Stop
        if ($response.data.name -ne $datasetName -or $response.data.id -notmatch '^[A-Za-z0-9]{10,40}$') { throw 'Unexpected dataset response.' }
        $DatasetId = [string]$response.data.id
        $response = $null
    }
    $phase = 'creative-qc-read'
    $raw = & $node.Source $adapter --apify-dataset $DatasetId $Limit --approved-free-read
    if ($LASTEXITCODE -ne 0) { throw 'QC read failed.' }
    $report = ($raw -join [Environment]::NewLine) | ConvertFrom-Json
    if ($report.schema -ne 'nfai-creative-qc-report-v1' -or $report.import.provider -ne 'apify' -or $report.import.dataset_id -ne $DatasetId) { throw 'Unexpected report.' }
    $phase = 'report'
    $dir = Join-Path $env:LOCALAPPDATA 'NFAI-Free-Engine\reports'
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
    $output = Join-Path $dir ('apify-qc-' + [Guid]::NewGuid().ToString('N') + '.json')
    [System.IO.File]::WriteAllText($output, ($raw -join [Environment]::NewLine), (New-Object System.Text.UTF8Encoding($false)))
    $check = Get-Content -LiteralPath $output -Raw | ConvertFrom-Json
    if ($check.import.dataset_id -ne $DatasetId -or $check.import.returned -ne $report.import.returned) { throw 'Report readback failed.' }
    Write-Output 'APIFY QC: PASS'
    Write-Output ('DATASET ID: ' + $DatasetId)
    Write-Output ('RETURNED: ' + $report.import.returned)
    Write-Output ('TOTAL: ' + $report.import.total)
    Write-Output ('COMPLETE: ' + $report.import.complete)
    Write-Output ('REPORT: ' + $output)
} catch {
    throw ('APIFY QC: FAILED at ' + $phase + '. No automatic retry. Inspect locally without printing credentials.')
} finally {
    Remove-Item Env:APIFY_TOKEN -ErrorAction SilentlyContinue
    if ($ptr -ne [IntPtr]::Zero) { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr) }
    if ($null -ne $secure) { $secure.Dispose() }
}
