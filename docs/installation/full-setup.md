# <img src="../assets/lucide/download.svg" width="18" height="18" alt="" /> Full setup — one installer, guided steps

**Windows-first.** This setup aims to reproduce the author's Claude development environment without republishing third-party packages or copying secrets.

<br />

## <img src="../assets/lucide/download.svg" width="18" height="18" alt="" /> 1. Prerequisites

Install [Claude Code](./claude-code.md), [Git](./git.md), [Python](./python.md), and [Node/npm](./nodejs-npm.md). Optional tools include [uvx](./uv.md), [GitHub CLI](./github-cli.md), [Docker](./docker.md) and [Obsidian](./obsidian.md).

```powershell
claude --version
git --version
python --version
node --version
npm --version
```

<br />

## <img src="../assets/lucide/workflow.svg" width="18" height="18" alt="" /> 2. Preview everything (no writes)

From your cloned project directory:

```powershell
.\scripts\doctor.ps1
python .\scripts\verify-all.py
.\scripts\install-all.ps1 -All
```

The preview lists 28 reviewed custom assets, the base rule, a portable global `CLAUDE.md`, the local Lucide icon assets, publisher-pinned agent/command/skill source steps, and optional external actions. No install, vault write or API connection occurs.

<br />

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 3. Test local files in isolation (recommended)

```powershell
$testConfig = Join-Path $HOME 'Documents/Ardizuo-Sandbox-Claude-Config'
.\scripts\install-all.ps1 -ConfigDir $testConfig
.\scripts\install-all.ps1 -Apply -ConfigDir $testConfig
$old = $env:CLAUDE_CONFIG_DIR
$env:CLAUDE_CONFIG_DIR = $testConfig
python .\scripts\verify-all.py
$env:CLAUDE_CONFIG_DIR = $old
```

**External CLI installation is intentionally blocked when `-ConfigDir` is used.** The pinned SuperClaude and pinned skill download installers can be isolated safely with `-ConfigDir -PinnedSuperClaude -PinnedSkills` because they explicitly write only under that folder. Most plugin/MCP CLI installs cannot be isolated this way.

<br />

## <img src="../assets/lucide/download.svg" width="18" height="18" alt="" /> 4. Apply the complete guided setup

```powershell
.\scripts\install-all.ps1 -Apply -All
```

This command can make external network requests and ask you for input. Read the plan before using it. It does **not** enter credentials, grant OAuth access, or guarantee the dashboard patch works with every upstream Claude Map release.

**What it attempts:**

1. Copy your original 28 files, core rule, portable global CLAUDE.md and Lucide icon assets, without overwriting conflicting files.
2. Fetch publisher-pinned SuperClaude agent/command definitions (up to 20 agents and 19 byte-exact commands; 11 upstream variants opt-in) and 20 source-compared skill prompts. The upstream SuperClaude CLI is an alternative.
3. Check and register four official/upstream plugin marketplaces before attempting all 12 plugins. Account sign-in still requires user approval.
4. Register seven MCP servers, including the official GitHub Docker OAuth launcher, when not already present.
5. Explain the two remaining credential-dependent MCPs: Tavily and Morph. GitHub still requires interactive OAuth and a running Docker engine.
6. Register the five hooks after a private settings backup.
7. Create eight Obsidian vault folders and install four supplied templates without overwriting customized ones or creating session notes.
8. **Guide** the Claude Map installation: do not silently upgrade or repatch an existing global dashboard. Rehearse the five-stage overlay and approve live modification separately.

For a **dashboard-only** install, use [Claude Map setup](../../dashboard/claude-map/README.md). For tested static source setup, read [pinned SuperClaude](./pinned-superclaude.md) and [pinned skills](./pinned-skills.md).

**Not a perfect clone:** A complete 30-command upstream set needs `-UpstreamVariants`, five modified publisher skill versions need `-SkillUpstreamVariants`, four skills still lack verified sources and 17 additional direct-skill origins require separate installation, and sidecars/runtime behavior are not automatically covered.

<br />

## <img src="../assets/lucide/blocks.svg" width="18" height="18" alt="" /> 5. Audit every named reference capability

```powershell
python .\scripts\coverage-doctor.py
python .\scripts\coverage-doctor.py --json
```

The audit reports all 21 reference agent names, 62 skill names, 32 command names, 12 plugins, and nine MCP servers individually. It is offline; it will NOT test provider authentication. `cached-unconfirmed` means a plugin file was found on disk but the corresponding plugin was not confirmed enabled.

The reference count is not the install promise. See [exact coverage](../components/exact-coverage.md) and [privately reviewing missing files](./private-source-migration.md).

<br />

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 6. Verify honestly

```powershell
python .\scripts\verify-all.py
claude plugin list
claude mcp list
```

In Claude Code, open `/skills`, `/mcp`, and `/hooks`. Sign in only to services you intend to use. Run a small delegated code-review, local test build and explicitly approved vault-note test to verify runtime behavior. For **file-by-file deployment evidence**, run `python .\scripts\verify-installed-layers.py --config-dir $testConfig` on an isolated configuration and read [the installed-layers guide](./installed-layer-audit.md).

**Status meanings:**

- **Installed:** file/package found
- **Configured:** CLI registration found
- **Authenticated/connected:** provider handshakes verified in Claude Code
- **Executed:** observed agent/tool/hook output exists; not inferred from configuration

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 7. Rollback and removal

The installer skips identical assets and fails on conflicting files; it never force-overwrites your unrelated configuration. Use `scripts/backup.ps1` before changing personal rules and refer to its matching `restore.ps1` for supported backups. Claude Map overlay scripts back up their patched source files. There is not yet a fully tested automatic uninstall of every third-party service; use each [plugin](../../integrations/plugins/README.md) or [MCP](../../integrations/mcp/README.md) guide for removal.

<br />

## <img src="../assets/lucide/alert-triangle.svg" width="18" height="18" alt="" /> 8. Known limitations

- The Full mode is an **assisted preview**, not a verified one-click offline replica.
- Some plugin marketplace IDs and CLI options can change; errors require guide-based resolution.
- 178 discovered skill entries do **not** mean 178 independent skills or redistributable files.
- Native Claude built-ins, OAuth credentials and personal Obsidian notes are not bundled.
- Dashboard overlays are version-sensitive; see [the dashboard guide](../../dashboard/claude-map/README.md).

[Read the repository overview →](../../README.md) · [Troubleshooting](../troubleshooting.md)

<br />

## <img src="../assets/lucide/monitor.svg" width="18" height="18" alt="" /> Visual 30-step walkthrough

[Follow the full verification checklist](./verification-checklist.md) after installation.

## <img src="../assets/lucide/folder-open.svg" width="18" height="18" alt="" /> Optional reproducibility: pinned SuperClaude file definitions

If you need exactly audited upstream agent/command definitions without running the SuperClaude CLI, use the separate [hash-verified, pinned SuperClaude installer](./pinned-superclaude.md). It installs into an isolated `-ConfigDir` first and refuses conflicts. This is an alternative to the `-All` mode's upstream CLI, **not** an additional automatic overwrite step.


## <img src="../assets/lucide/blocks.svg" width="18" height="18" alt="" /> Sprint 4 — 20 publisher-pinned skill definitions

The unified installer now selects **20** content-matched third-party skill prompts by default and requires **`-SkillUpstreamVariants`** to add the five upstream skills whose text differs from the author’s local files. Four skills have no verified source and cannot be reproduced yet. See [pinned skills](./pinned-skills.md). Downloads and runtime behavior still require an isolated Windows verification.


## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Release completeness is an explicit separate check

`python .\scripts\release-audit.py` compares **the package manifest against the reference inventory**; `python .\scripts\verify-installed-layers.py --config-dir $testConfig` checks whether selected package files actually exist under a target config. They do **not** test OAuth, remote MCP connectivity, child skill scripts, agent delegation or the dashboard browser. [See the read-only audit walkthrough](./installed-layer-audit.md).
