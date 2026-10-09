[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'

$config = if ([string]::IsNullOrWhiteSpace($env:CLAUDE_CONFIG_DIR)) { Join-Path $HOME '.claude' } else { $env:CLAUDE_CONFIG_DIR }
Write-Host 'Ardizuo Setup Doctor — local inventory only'
Write-Host 'Installed != configured != authenticated != executed.'
Write-Host ''

$commands = @('claude','git','node','npm','python','uvx','gh','docker','winget')
foreach ($command in $commands) {
    $present = [bool](Get-Command $command -ErrorAction SilentlyContinue)
    $status = if ($present) { 'available' } else { 'not found (may be optional)' }
    Write-Host ('{0,-11} {1}' -f $command, $status)
}

Write-Host ''
if (-not (Test-Path -LiteralPath $config -PathType Container)) {
    Write-Host 'Claude global configuration folder: not found'
    Write-Host 'Runtime check: not run. MCP authentication: not tested.'
    exit 0
}
Write-Host 'Claude global configuration folder: exists'

$agentsDir = Join-Path $config 'agents'
$skillsDir = Join-Path $config 'skills'
$hooksDir = Join-Path $config 'hooks'
$commandsDir = Join-Path $config 'commands'
$pluginCache = Join-Path $config 'plugins\cache'

$agentCount = if (Test-Path -LiteralPath $agentsDir) { @(Get-ChildItem -LiteralPath $agentsDir -File -Filter '*.md' -ErrorAction SilentlyContinue).Count } else { 0 }
$skillCount = if (Test-Path -LiteralPath $skillsDir) { @(Get-ChildItem -LiteralPath $skillsDir -Recurse -File -Filter 'SKILL.md' -ErrorAction SilentlyContinue).Count } else { 0 }
$pluginSkillCount = if (Test-Path -LiteralPath $pluginCache) { @(Get-ChildItem -LiteralPath $pluginCache -Recurse -File -Filter 'SKILL.md' -ErrorAction SilentlyContinue).Count } else { 0 }
$hookCount = if (Test-Path -LiteralPath $hooksDir) { @(Get-ChildItem -LiteralPath $hooksDir -File -Filter '*.mjs' -ErrorAction SilentlyContinue).Count } else { 0 }
$commandCount = if (Test-Path -LiteralPath $commandsDir) { @(Get-ChildItem -LiteralPath $commandsDir -Recurse -File -Filter '*.md' -ErrorAction SilentlyContinue).Count } else { 0 }

Write-Host ('Global agent .md files:        {0} (does not include plugin agents)' -f $agentCount)
Write-Host ('Global SKILL.md files:         {0}' -f $skillCount)
Write-Host ('Cached plugin SKILL.md files: {0} (may include duplicate versions)' -f $pluginSkillCount)
Write-Host ('Top-level .mjs hook files:    {0} (not activation proof)' -f $hookCount)
Write-Host ('Global command .md files:     {0}' -f $commandCount)
Write-Host ('Core Ardizuo rule:            {0}' -f (Test-Path -LiteralPath (Join-Path $config 'rules\ardizuo-development.md') -PathType Leaf))
Write-Host ''
Write-Host 'Manual live verification: claude plugin list ; claude mcp list ; Claude Code /mcp and /skills.'
Write-Host 'This doctor makes NO connections, API calls, vault writes or Claude model calls.'
