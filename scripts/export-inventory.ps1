[CmdletBinding()]
param(
    [string]$OutputPath = (Join-Path (Join-Path $HOME 'Documents') 'Ardizuo-Inventory.local.json')
)
$ErrorActionPreference = 'Stop'
$config = if ([string]::IsNullOrWhiteSpace($env:CLAUDE_CONFIG_DIR)) { Join-Path $HOME '.claude' } else { $env:CLAUDE_CONFIG_DIR }

function Get-Names([string]$folder, [string]$filter, [switch]$Recursive, [switch]$ParentNames) {
    if (-not (Test-Path -LiteralPath $folder -PathType Container)) { return @() }
    $items = @(Get-ChildItem -LiteralPath $folder -Filter $filter -File -Recurse:$Recursive -ErrorAction SilentlyContinue)
    if ($ParentNames) { return @($items | ForEach-Object { $_.Directory.Name } | Sort-Object -Unique) }
    return @($items | ForEach-Object { $_.BaseName } | Sort-Object -Unique)
}

# Only filenames are collected. Never read ~/.claude.json, hooks' contents, MCP args/env or credentials.
$globalAgents = @(Get-Names (Join-Path $config 'agents') '*.md')
$globalSkills = @(Get-Names (Join-Path $config 'skills') 'SKILL.md' -Recursive -ParentNames)
$pluginSkills = @(Get-Names (Join-Path $config 'plugins\cache') 'SKILL.md' -Recursive -ParentNames)
$hookFiles = @(Get-Names (Join-Path $config 'hooks') '*.mjs')
$commands = @(Get-Names (Join-Path $config 'commands') '*.md' -Recursive)

$pluginNames = @()
$settingsPath = Join-Path $config 'settings.json'
if (Test-Path -LiteralPath $settingsPath -PathType Leaf) {
    try {
        $settings = Get-Content -LiteralPath $settingsPath -Raw | ConvertFrom-Json
        if ($settings.enabledPlugins) {
            $pluginNames = @($settings.enabledPlugins.PSObject.Properties | Where-Object { $_.Value -eq $true } | ForEach-Object { $_.Name } | Sort-Object -Unique)
        }
    } catch {
        Write-Warning 'Could not read enabled plugin names from settings.json; skipping that category.'
    }
}

$report = [ordered]@{
    schemaVersion = 1
    generatedUtc = (Get-Date).ToUniversalTime().ToString('o')
    warning = 'Names-only local inventory. It does not contain file contents, tokens or live connection results. Review before sharing.'
    globalAgents = $globalAgents
    globalSkills = $globalSkills
    cachedPluginSkillNames = $pluginSkills
    hookScriptNames = $hookFiles
    globalCommandNames = $commands
    enabledPluginNames = $pluginNames
    mcpConnectivity = 'not tested'
    agentDelegation = 'not tested'
    vaultWriteAndReload = 'not tested'
}

$parent = Split-Path -Parent $OutputPath
if ($parent -and (-not (Test-Path -LiteralPath $parent))) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
$report | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $OutputPath -Encoding UTF8
Write-Host "Names-only report created at: $OutputPath"
Write-Host 'Review the JSON manually before sharing it or copying anything into a public repository.'
