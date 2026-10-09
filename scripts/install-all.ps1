[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$All,
    [switch]$External,
    [switch]$Plugins,
    [switch]$Mcps,
    [switch]$SuperClaude,
    [switch]$PinnedSuperClaude,
    [switch]$UpstreamVariants,
    [switch]$Hooks,
    [switch]$Vault,
    [switch]$Dashboard,
    [string]$VaultPath,
    [string]$ConfigDir
)
$ErrorActionPreference = 'Stop'
$script = Join-Path $PSScriptRoot 'install-all.py'
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw 'Python 3 required. See docs/installation/python.md.' }
$arguments = @($script)
if ($All) { $External = $true; $SuperClaude = $true; $Plugins = $true; $Mcps = $true; $Hooks = $true; $Vault = $true; $Dashboard = $true }
if ($Apply) { $arguments += '--apply' }
if ($External) { $arguments += '--external' }
if ($Plugins) { $arguments += '--plugins' }
if ($Mcps) { $arguments += '--mcps' }
if ($SuperClaude) { $arguments += '--superclaude' }
if ($PinnedSuperClaude) { $arguments += '--pinned-superclaude' }
if ($UpstreamVariants) { $arguments += '--upstream-variants' }
if ($Hooks) { $arguments += '--hooks' }
if ($Vault) { $arguments += '--vault' }
if ($Dashboard) { $arguments += '--dashboard' }
if ($VaultPath) { $arguments += @('--vault-path', $VaultPath) }
if ($ConfigDir) { $arguments += @('--config-dir', $ConfigDir) }
& python @arguments
if ($LASTEXITCODE -ne 0) { throw "Installer stopped with exit code $LASTEXITCODE. No credentials are included." }
