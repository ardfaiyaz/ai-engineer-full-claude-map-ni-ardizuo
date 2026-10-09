[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$BackupDirectory,
    [switch]$Apply,
    [switch]$OverwriteExisting
)
$ErrorActionPreference = 'Stop'
$config = if ([string]::IsNullOrWhiteSpace($env:CLAUDE_CONFIG_DIR)) { Join-Path $HOME '.claude' } else { $env:CLAUDE_CONFIG_DIR }
$indexPath = Join-Path $BackupDirectory 'backup-manifest.json'
if (-not (Test-Path -LiteralPath $indexPath -PathType Leaf)) { throw 'Missing trusted backup-manifest.json. Refusing restore.' }
$index = Get-Content -LiteralPath $indexPath -Raw | ConvertFrom-Json
if ($index.schemaVersion -ne 1) { throw 'Unsupported backup manifest version.' }

$allowed = @(
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
Write-Host 'Private backup restore — dry run unless -Apply is specified.'
foreach ($relative in @($index.files)) {
    $rel = [string]$relative
    if ($allowed -notcontains $rel) { throw "Unsafe/unexpected backup path: $rel" }
    $source = Join-Path $BackupDirectory $rel
    $dest = Join-Path $config $rel
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw "Backup file missing: $rel" }
    if (Test-Path -LiteralPath $dest -PathType Leaf) {
        if (-not $OverwriteExisting) { Write-Host "SKIP existing: $rel (requires -OverwriteExisting)"; continue }
        Write-Host "Overwrite destination: $rel"
    } else { Write-Host "Create destination: $rel" }
    if (-not $Apply) { continue }
    $parent = Split-Path -Parent $dest
    if (-not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    Copy-Item -LiteralPath $source -Destination $dest -Force:$OverwriteExisting -ErrorAction Stop
}
if (-not $Apply) { Write-Host 'No files restored. Add -Apply; add -OverwriteExisting ONLY if you intend to replace current files.' }
