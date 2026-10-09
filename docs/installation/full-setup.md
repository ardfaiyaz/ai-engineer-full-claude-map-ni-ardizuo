# Full setup — one installer, guided steps

**Windows-first.** This setup aims to reproduce the author's Claude development environment without republishing third-party packages or copying secrets.

<br />

## 1. Prerequisites

Install [Claude Code](./claude-code.md), [Git](./git.md), [Python](./python.md), and [Node/npm](./nodejs-npm.md). Optional tools include [uvx](./uv.md), [GitHub CLI](./github-cli.md), [Docker](./docker.md) and [Obsidian](./obsidian.md).

```powershell
claude --version
git --version
python --version
node --version
npm --version
```

<br />

## 2. Preview everything (no writes)

From your cloned project directory:

```powershell
.\scripts\doctor.ps1
python .\scripts\verify-all.py
.\scripts\install-all.ps1 -All
```

The preview lists 28 custom assets plus the Ardizuo base rule and optional external actions. No install, vault write or API connection occurs.

<br />

## 3. Test local files in isolation (recommended)

```powershell
$testConfig = Join-Path $HOME 'Documents/Ardizuo-Sandbox-Claude-Config'
.\scripts\install-all.ps1 -ConfigDir $testConfig
.\scripts\install-all.ps1 -Apply -ConfigDir $testConfig
$old = $env:CLAUDE_CONFIG_DIR
$env:CLAUDE_CONFIG_DIR = $testConfig
python .\scripts\verify-all.py
$env:CLAUDE_CONFIG_DIR = $old
```

**External CLI installation is intentionally blocked when `-ConfigDir` is used.** Most third-party CLIs use real user scope and cannot safely be isolated using only this environment variable.

<br />

## 4. Apply the complete guided setup

```powershell
.\scripts\install-all.ps1 -Apply -All
```

This command can make external network requests and ask you for input. Read the plan before using it. It does **not** enter credentials, grant OAuth access, or guarantee the dashboard patch works with every upstream Claude Map release.

**What it attempts:**

1. Copy your original 28 files and core rule, without overwriting conflicting files.
2. Install SuperClaude via pipx and then run the upstream setup when absent.
3. Invoke CLI installation for 12 plugins. Marketplace prerequisites and provider sign-in may still require manual work.
4. Register six MCPs from public/verified launch commands when not already present.
5. Explain three remaining credential-dependent MCPs: Tavily, Morph and GitHub.
6. Register the five hooks after a private settings backup.
7. Create the eight empty Obsidian vault folders, without creating session notes.
8. Install the upstream Claude Map npm package; patch compatibility is checked separately.

For a **dashboard-only** install, use [Claude Map setup](../../dashboard/claude-map/README.md).

<br />

## 5. Verify honestly

```powershell
python .\scripts\verify-all.py
claude plugin list
claude mcp list
```

In Claude Code, open `/skills`, `/mcp`, and `/hooks`. Sign in only to services you intend to use. Run a small delegated code-review, local test build and explicitly approved vault-note test to verify runtime behavior.

**Status meanings:**

- **Installed:** file/package found
- **Configured:** CLI registration found
- **Authenticated/connected:** provider handshakes verified in Claude Code
- **Executed:** observed agent/tool/hook output exists; not inferred from configuration

<br />

## 6. Rollback and removal

The installer skips identical assets and fails on conflicting files; it never force-overwrites your unrelated configuration. Use `scripts/backup.ps1` before changing personal rules and refer to its matching `restore.ps1` for supported backups. Claude Map overlay scripts back up their patched source files. There is not yet a fully tested automatic uninstall of every third-party service; use each [plugin](../../integrations/plugins/README.md) or [MCP](../../integrations/mcp/README.md) guide for removal.

<br />

## 7. Known limitations

- The Full mode is an **assisted preview**, not a verified one-click offline replica.
- Some plugin marketplace IDs and CLI options can change; errors require guide-based resolution.
- 178 discovered skill entries do **not** mean 178 independent skills or redistributable files.
- Native Claude built-ins, OAuth credentials and personal Obsidian notes are not bundled.
- Dashboard overlays are version-sensitive; see [the dashboard guide](../../dashboard/claude-map/README.md).

[Read the repository overview →](../../README.md) · [Troubleshooting](../troubleshooting.md)

<br />

## Visual 30-step walkthrough

[Follow the full verification checklist](./verification-checklist.md) after installation.
