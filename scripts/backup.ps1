[CmdletBinding()]
param(
    [string]$BackupRoot = (Join-Path (Join-Path $HOME 'Documents') 'Ardizuo-Backups'),
    [switch]$Apply
)
$ErrorActionPreference = 'Stop'
$config = if ([string]::IsNullOrWhiteSpace($env:CLAUDE_CONFIG_DIR)) { Join-Path $HOME '.claude' } else { $env:CLAUDE_CONFIG_DIR }

$relativeFiles = @(
    'CLAUDE.md',
    'rules\ardizuo-development.md',
    'rules\development-workflow.md',
    'rules\developer-orchestration.md',
    'workflows\skill-gates.json',
    'workflows\wave-protocol.md',
    'workflows\completion-mandate.md',
    'hooks\skill-gate-check.mjs',
    'hooks\vault-session-init.mjs',
    'hooks\log-to-vault.mjs',
    'hooks\stop-vault-log.mjs',
    'hooks\dead-code-check.mjs'
)
$available = @($relativeFiles | Where-Object { Test-Path -LiteralPath (Join-Path $config $_) -PathType Leaf })
Write-Host ('Reviewed backup file candidates found: {0}' -f $available.Count)
foreach ($file in $available) { Write-Host "  $file" }
Write-Host "Backup root: $BackupRoot"
Write-Host 'Backups may contain PERSONAL INFORMATION. Store them privately, outside this Git repository.'
if (-not $Apply) { Write-Host 'DRY RUN. Use -Apply to save a timestamped snapshot.'; exit 0 }
if ($available.Count -eq 0) { Write-Host 'Nothing to back up.'; exit 0 }

$stamp = Get-Date -Format 'yyyyMMdd-HHmmss-ffff'
$dest = Join-Path $BackupRoot $stamp
New-Item -ItemType Directory -Path $dest -Force | Out-Null
foreach ($file in $available) {
    $source = Join-Path $config $file
    $target = Join-Path $dest $file
    $parent = Split-Path -Parent $target
    if (-not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    Copy-Item -LiteralPath $source -Destination $target -ErrorAction Stop
}
$index = [ordered]@{ schemaVersion = 1; createdUtc = (Get-Date).ToUniversalTime().ToString('o'); files = @($available) }
$index | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $dest 'backup-manifest.json') -Encoding UTF8
Write-Host "Private backup created: $dest"
