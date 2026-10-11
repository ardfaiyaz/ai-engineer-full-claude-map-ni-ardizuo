# 📥 Complete Windows installation


This is the canonical install sequence for the **Ardizuo development setup**: the reference layers plus the researched extended stack, in one run. It never invents private assets.


<br />
<br />


## ✅ Requirements


Open PowerShell and verify Git, Python, Node.js/npm, and Claude Code are installed:

```powershell
git --version
python --version
node --version
npm --version
claude --version
```

See the [prerequisites guide](../prerequisites.md) for installation help. Some optional MCPs also need `uvx`, Docker or a provider account.


<br />
<br />


## 🚀 Install from GitHub


```powershell
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo

# Safe preview: no files installed or providers contacted.
.\scripts\install-all.ps1 -All

# Apply the reviewed changes. Provider downloads, hooks and vault creation can occur.
.\scripts\install-all.ps1 -Apply -All
```

If a conflicting file already exists, the non-overwriting installer stops rather than replacing your own config. Keep a backup, compare the files, and select only the parts you want. `-All` is best suited to a **fresh** Windows user configuration.


<br />
<br />


## ⚙️ Installer switch reference


`scripts/install-all.ps1` is a thin wrapper around `scripts/install-all.py`. Every switch below has a matching `--lower-case` Python flag. Without `-Apply`, every switch only previews.

| Switch | What it does | In `-All`? |
| --- | --- | --- |
| `-Apply` | Actually writes files and runs the selected external commands | — |
| `-External` | Allows any third-party download or CLI install; required by the switches marked † | Yes |
| `-PinnedSuperClaude` | 20 SuperClaude agents + 19 commands from a pinned commit, checksum-verified | Yes (unless `-SuperClaude`) |
| `-UpstreamVariants` | Adds 11 publisher-original SuperClaude commands; needs `-PinnedSuperClaude` | No |
| `-SuperClaude` † | Runs the upstream `pipx install superclaude` + `superclaude install` instead of pinned files | No |
| `-PinnedSkills` | 20 publisher-pinned `SKILL.md` files, checksum-verified | Yes |
| `-SkillUpstreamVariants` | Adds 5 publisher-original skill variants; needs `-PinnedSkills` | No |
| `-Plugins` † | Registers the four marketplaces and installs the 12 baseline plugins | Yes |
| `-Mcps` † | Registers the supported baseline MCPs (Tavily and Morph stay manual) | Yes |
| `-Hooks` | Registers the five Ardizuo hooks in `settings.json`, with a backup | Yes |
| `-Vault` / `-VaultPath` | Creates the eight Obsidian folders and four templates | Yes (default path) |
| `-Dashboard` | Prints the Claude Map rehearsal steps; never patches automatically | Yes (guidance only) |
| `-Extensions <selection>` † | Extended stack from `setup/extension-catalog.json`: `all`, groups or IDs | Yes (`all`) |
| `-ConfigDir <path>` | Uses an isolated Claude config for local files; cannot be combined with external installs plus `-Apply` | — |

The 29 reviewed local files, the portable `CLAUDE.md` and the base rule are always part of the plan, with or without switches.

```powershell
# Everything, but only the priority group of the extended stack:
.\scripts\install-all.ps1 -All -Extensions priority            # preview
.\scripts\install-all.ps1 -Apply -All -Extensions priority     # install
```


<br />
<br />


## 🔑 Finish accounts and connection checks


```powershell
claude plugin list
claude mcp list
python .\scripts\verify-installed-layers.py --strict-local --require-hooks
```

Inside Claude Code, inspect `/skills`, `/mcp`, and `/hooks`. A plugin can be installed but need OAuth; an MCP can be registered but disconnected. Each friend uses their **own** accounts and secrets. You may skip Atlassian authentication unless you use it.


<br />
<br />


## 🛠️ Existing setup or cautious trial


Test only locally installed definitions in a separate configuration. Do **not** combine `-ConfigDir` with `-Apply -All`, because external plugin/MCP CLI operations are user-scoped:

```powershell
$trial = Join-Path $HOME 'Documents/Ardizuo-Trial-Config'
.\scripts\install-all.ps1 -ConfigDir $trial -PinnedSuperClaude -PinnedSkills
.\scripts\install-all.ps1 -Apply -ConfigDir $trial -PinnedSuperClaude -PinnedSkills -Hooks
python .\scripts\verify-installed-layers.py --config-dir $trial --strict-local --require-hooks
```

For original upstream versions **different from** the maintainer's files, the explicit switches are `-SkillUpstreamVariants` (five more skill prompts) and `-UpstreamVariants` (11 more SuperClaude commands). Those are not exact personal copies, so leave them off unless needed. The researched extended stack is part of `-All` (`-Extensions all`); see [extended stack](./extensions.md). Some pinned skills require publisher-side support files that are not part of the current installer.


<br />
<br />


## 🖥️ Optional Claude Map dashboard


The five-stage Development Hub overlay **is not silently patched by `-All`**. See the [dashboard setup](../../dashboard/claude-map/README.md), rehearse against a compatible Claude Map version, review backups, then separately approve any live changes. Opening the dashboard is not proof of agent execution.


<br />
<br />


## 📋 Exact scope and limitations


| Reference component | Default package | Optional publisher versions |
| --- | --- | --- |
| Agent definitions | 21 / 21 | — |
| Direct skill definitions | 36 / 62 | 41 / 62 |
| Executable commands | 20 / 31 | 31 / 31 |
| Plugin IDs | 12 documented/CLI-supported | Provider sign-in separately |
| Target MCP servers | 9 documented/supported | Provider sign-in separately |
| Hooks | Five handlers (when selected) | Runtime actions require an actual Claude session |
| Extended stack | 115 plugin IDs, 3 MCPs, 7 CLI tools, 4 pinned skills, gstack | Provider sign-in separately; credential and per-project steps printed ([guide](./extensions.md)) |

The maintainer's machine also has other direct-skill folders and associated files whose origin or redistribution status isn't resolved. **The installer will not fabricate them.** Provider caches, native commands and plugin skills are not independently counted as bundled global `SKILL.md` files. See the [by-name matrix](./reproducibility-matrix.md), [origin review](./exact-local-origin-review.md), and [security policy](../../SECURITY.md).


<br />
<br />


## 🛠️ Troubleshooting and undo


Use [troubleshooting](../troubleshooting.md) for missing tools and login prompts; use the [plugin](../../integrations/plugins/README.md) and [MCP](../../integrations/mcp/README.md) guides for provider-specific setup. The installer does not overwrite different files, but external package installations and account authorizations may need manual cleanup. `scripts/backup.ps1` and `scripts/restore.ps1` cover only their documented backup scope—**not** every provider or a universal uninstall.

[One-page starting guide](../../START-HERE.md) · [Release checklist](../release-checklist.md)
