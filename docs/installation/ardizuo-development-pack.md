# 📄 Ardizuo development pack · Phase 1


**Portable source assets for global Claude Code** — no separate website or account required. This phase installs **28 locally authored files**, not the third-party plugins, MCP servers, dashboard, or complete Full profile.


## 📥 1. Before installing


- [Claude Code CLI](./claude-code.md), [Git](./git.md), [Node.js](./nodejs-npm.md), and Windows PowerShell 5.1 or newer.
- Clone the [repository](https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo) and open a PowerShell terminal in the root directory.
- Close active Claude Code sessions while changing the global configuration.

The package resolves the user's configuration from `CLAUDE_CONFIG_DIR` if set; otherwise from `$HOME\.claude`. It never uses the author's original Windows username.


## 🔄 2. Preview changes — recommended first


```powershell
.\scripts\install-development.ps1
```

Or from the main installer once this phase is merged:

```powershell
.\scripts\install.ps1 -Profile development
```

The **dry run** lists which files would be created, which already match, and which conflict. A conflict **blocks the entire installation**; existing files are never overwritten. If your machine already has a development setup, use a disposable Windows user profile or a temporary `CLAUDE_CONFIG_DIR` for first testing.


## 📥 3. Install only after you approve the plan


```powershell
.\scripts\install-development.ps1 -Apply
.\scripts\doctor-development.ps1
```

The installer checks file hashes. It includes 16 original local skills, the diagram agent, a manual vault command, five hook scripts plus shared helper, three workflows, and a developer rule.

**Installing files does not enable hooks, authenticate third-party services, run agents, or write to Obsidian.**


## 🔄 4. Optionally activate hooks


Five scripts support `UserPromptSubmit`, `SessionStart`, `PostToolUse` (two scripts) and `Stop`.

```powershell
node .\scripts\register-hooks.mjs                # DRY RUN
node .\scripts\register-hooks.mjs --apply        # only after review
```

Registration merges entries into the existing global `settings.json` and creates a **private backup** of the previous settings in the Claude configuration folder. Existing entries are preserved, and matching hook commands are not duplicated.

**Review changes and close Claude Code first.** `settings.json` may contain sensitive configuration; never commit your backup. If Claude Code uses a custom shell or config path, inspect `/hooks` after restarting to verify activation. Successful registration is not proof a lifecycle event actually ran.


## 📝 5. Configure optional Obsidian memory


No vault is created by default. The hooks use this default folder:

```text
%USERPROFILE%\Documents\Claude-Dev-Vault
```

To choose a different vault **for the current PowerShell session only**:

```powershell
$env:CLAUDE_DEV_VAULT = Join-Path $HOME 'Documents\Your-Vault-Name'
claude
```

The environment variable must be visible to the Claude Code process. Do not copy anyone else's vault notes. `/log-to-vault` previews the complete note and requires your explicit affirmative approval before saving it. The `SessionStart` hook only reads previously approved notes.


## 🛠️ 6. Verify and troubleshoot


```powershell
.\scripts\doctor-development.ps1
claude plugin list
claude mcp list
```

Inside Claude Code, open `/skills` and `/hooks`. Invoke `reuse-audit` on a small disposable project; approve a harmless `/log-to-vault` note and test reload **only when you're comfortable doing a model-consuming live test**.

If installation reports a conflict, **do not delete your original file to make the status green**. Compare the file versions, choose the desired behavior, and back up your existing configuration. The installer does not contain a sweeping uninstall; use the private backup and record the paths it created before removing anything.


[Back to installation guides](./README.md) · [Security](../../SECURITY.md) · [MCP guides](../../integrations/mcp/README.md)
