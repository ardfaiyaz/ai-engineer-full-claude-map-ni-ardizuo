[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$config = if ([string]::IsNullOrWhiteSpace($env:CLAUDE_CONFIG_DIR)) { Join-Path $HOME '.claude' } else { $env:CLAUDE_CONFIG_DIR }
$manifest = Get-Content -LiteralPath (Join-Path $repo 'setup\development-assets.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$missing = 0; $matching = 0; $different = 0
foreach ($rel in $manifest.filePaths) {
    $relative = ([string]$rel).Replace('/', [IO.Path]::DirectorySeparatorChar)
    $src = Join-Path $repo (Join-Path 'ardizuo-plugin' $relative)
    $dst = Join-Path $config $relative
    $status = 'missing'
    if (Test-Path -LiteralPath $dst -PathType Leaf) {
        if ((Get-FileHash -LiteralPath $src -Algorithm SHA256).Hash -eq (Get-FileHash -LiteralPath $dst -Algorithm SHA256).Hash) {
            $status = 'identical'; $matching++
        } else { $status = 'different'; $different++ }
    } else { $missing++ }
    Write-Host ('{0,-11} {1}' -f $status, $rel)
}
Write-Host ('Development pack status: {0} identical; {1} missing; {2} different (out of {3})' -f $matching, $missing, $different, @($manifest.filePaths).Count)
Write-Host 'Hook activation: not checked (inspect Claude Code /hooks). MCP and plugin authentication: not checked.'
