[CmdletBinding()]
param(
    [ValidateSet('core','full','frontend','backend','mobile','custom')]
    [string]$Profile = 'core',
    [switch]$Apply
)
$ErrorActionPreference = 'Stop'

$repo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$source = Join-Path $repo 'global-config\rules\ardizuo-development.md'
$config = if ([string]::IsNullOrWhiteSpace($env:CLAUDE_CONFIG_DIR)) { Join-Path $HOME '.claude' } else { $env:CLAUDE_CONFIG_DIR }
$destination = Join-Path $config 'rules\ardizuo-development.md'

if ($Profile -ne 'core') {
    throw "Profile '$Profile' is NOT installable in this bootstrap preview. Read setup/profiles/$Profile.json. Only -Profile core is supported."
}
if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw "Missing packaged rule: $source" }

Write-Host 'Ardizuo Windows installer — BOOTSTRAP ONLY'
Write-Host "Profile: $Profile"
Write-Host "Source: $source"
Write-Host "Destination: $destination"
Write-Host 'Actions: one namespaced development rule; NO plugins, MCPs, agents, dashboard, or external packages.'

if (Test-Path -LiteralPath $destination -PathType Leaf) {
    $sourceHash = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash
    $targetHash = (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash
    if ($sourceHash -eq $targetHash) {
        Write-Host 'Already installed, identical. No changes.'
        exit 0
    }
    throw 'Existing namespaced rule differs. Refusing to overwrite. Back it up and resolve the conflict manually.'
}

if (-not $Apply) {
    Write-Host 'DRY RUN. Nothing changed. Add -Apply to copy the rule.'
    exit 0
}

$targetDir = Split-Path -Parent $destination
if (-not (Test-Path -LiteralPath $targetDir)) { New-Item -ItemType Directory -Path $targetDir -Force | Out-Null }
Copy-Item -LiteralPath $source -Destination $destination -ErrorAction Stop
if ((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash) {
    throw 'Post-install verification failed. Inspect the target rule.'
}
Write-Host 'Installed and checksum verified. Restart Claude Code to load new global rules.'
