[CmdletBinding()]
param([switch]$Apply)
$ErrorActionPreference = 'Stop'

# Windows PowerShell 5.1+; deliberately no plugin/MCP downloads or settings.json writes.
$repo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$config = if ([string]::IsNullOrWhiteSpace($env:CLAUDE_CONFIG_DIR)) {
    Join-Path $HOME '.claude'
} else { $env:CLAUDE_CONFIG_DIR }
$manifestFile = Join-Path $repo 'setup\development-assets.json'
if (-not (Test-Path -LiteralPath $manifestFile -PathType Leaf)) { throw 'Missing development asset manifest.' }
$data = Get-Content -LiteralPath $manifestFile -Raw -Encoding UTF8 | ConvertFrom-Json
if ($data.schemaVersion -ne 1) { throw 'Unsupported development asset manifest.' }
$files = @($data.filePaths)
if ($files.Count -ne 28) { throw 'Expected 28 reviewed source files; manifest must be reviewed before use.' }

$plan = @()
$conflicts = @()
foreach ($rel in $files) {
    $name = [string]$rel
    if ($name -notmatch '^(agents|skills|hooks|rules|workflows|commands)/' -or
        $name -match '(^|/)(\.|\.\.)(/|$)' -or $name -match '[\\:]' -or $name -match '//') {
        throw "Unsafe manifest path: $name"
    }
    $localRel = $name.Replace('/', [IO.Path]::DirectorySeparatorChar)
    $src = Join-Path $repo (Join-Path 'ardizuo-plugin' $localRel)
    $dst = Join-Path $config $localRel
    if (-not (Test-Path -LiteralPath $src -PathType Leaf)) { throw "Package file missing: $name" }
    $state = 'create'
    if (Test-Path -LiteralPath $dst) {
        if (-not (Test-Path -LiteralPath $dst -PathType Leaf)) { $state = 'conflict' }
        elseif ((Get-FileHash -LiteralPath $src -Algorithm SHA256).Hash -eq
                (Get-FileHash -LiteralPath $dst -Algorithm SHA256).Hash) { $state = 'identical' }
        else { $state = 'conflict' }
    }
    $plan += [PSCustomObject]@{ Relative=$name; Source=$src; Destination=$dst; Status=$state }
    if ($state -eq 'conflict') { $conflicts += $name }
}

Write-Host 'Ardizuo development pack — Phase 1 (no external plugins, MCPs or dashboard)'
Write-Host "Global Claude directory: $config"
Write-Host ('Plan: {0} new, {1} identical, {2} conflicts' -f
    @($plan | Where-Object Status -eq 'create').Count,
    @($plan | Where-Object Status -eq 'identical').Count,
    $conflicts.Count)
$plan | Select-Object Relative, Status | Format-Table -AutoSize
if ($conflicts.Count -gt 0) {
    throw ('Conflicting user files found: ' + ($conflicts -join ', ') + '. NOTHING changed. Use an isolated test config or resolve conflicts manually; existing files are never overwritten.')
}
if (-not $Apply) {
    Write-Host 'DRY RUN ONLY. Add -Apply to copy missing files after reviewing this plan.'
    Write-Host 'Hooks will NOT be activated automatically. To preview registration after install: node .\scripts\register-hooks.mjs'
    exit 0
}

$created = New-Object 'System.Collections.Generic.List[string]'
try {
    foreach ($item in $plan) {
        if ($item.Status -ne 'create') { continue }
        $folder = Split-Path -Parent $item.Destination
        if (-not (Test-Path -LiteralPath $folder)) {
            New-Item -ItemType Directory -Path $folder -Force | Out-Null
        }
        # No -Force: a racing new file must never be overwritten.
        [System.IO.File]::Copy($item.Source, $item.Destination, $false)
        $created.Add($item.Destination)
        if ((Get-FileHash -LiteralPath $item.Source -Algorithm SHA256).Hash -ne
            (Get-FileHash -LiteralPath $item.Destination -Algorithm SHA256).Hash) {
            throw "Post-copy checksum mismatch: $($item.Relative)"
        }
    }
} catch {
    foreach ($createdFile in $created) {
        # Only files this invocation created; no preexisting content is touched.
        Remove-Item -LiteralPath $createdFile -Force -ErrorAction SilentlyContinue
    }
    throw
}
Write-Host ('Installed and checksum verified: {0} new files; {1} identical files left unchanged.' -f $created.Count, ($plan.Count - $created.Count))
Write-Host 'No existing file overwritten. Hook activation requires separate review/approval.'
Write-Host 'Restart Claude Code after installing. To review hook activation, run: node .\scripts\register-hooks.mjs'
