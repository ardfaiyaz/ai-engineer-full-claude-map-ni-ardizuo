# 🚀 AI Engineer Full Claude Map ni Ardizuo

![Ardizuo Claude Code setup banner](./banner.png)


A **Windows-first Claude Code development setup** with agents, skills, commands, hooks, MCPs, plugins, optional Obsidian memory and an optional five-stage Claude Map dashboard.

This is an **assisted open-source setup**, not a copy of anyone's private tokens, accounts or unreleased skill files.


<br />
<br />


## 📥 Copy, paste, install (Windows PowerShell)


Already have Git, Python 3, Node.js and Claude Code? Use the first block. Otherwise, install prerequisites below.

```powershell
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo

# Preview: see what will be installed without making changes.
.\scripts\install-all.ps1 -All

# Apply only after reviewing the preview.
.\scripts\install-all.ps1 -Apply -All

# Verify the local files, hooks and external CLI integrations.
python .\scripts\verify-installed-layers.py --strict-local --require-hooks
claude plugin list
claude mcp list
```

**New Windows machine — install basic prerequisites** (PowerShell; skip tools you already have):

```powershell
winget install --id Git.Git --exact --source winget
winget install --id OpenJS.NodeJS.LTS --exact --source winget
winget install --id Python.Python.3.13 --exact --source winget
winget install --id Anthropic.ClaudeCode --exact --source winget
```

**Reopen PowerShell** after installation. Python 3.13 is a known supported option; a newer compatible Python 3 release is also suitable.

[Short setup checklist](./START-HERE.md) · [Troubleshooting](./docs/troubleshooting.md)


<br />
<br />


## 📦 What the public installer provides


| Layer | Coverage on a fresh computer |
| --- | --- |
| Agents | 21/21 file definitions |
| Direct skills | 36/62 by default; 41/62 with opt-in, **different** upstream variants |
| Executable commands | 20/31 by default; 31/31 with optional upstream variants |
| Plugins | Installation attempts for all 12 listed plugins; authentication is individual |
| MCP servers | Nine listed servers; supported registrations plus guided manual authentication |
| Hooks | Five handlers and optional registration |
| Workflow | Five stages, rules, gates and portable context |
| Memory | Optional empty Obsidian folder structure and four templates |
| Dashboard | Optional Claude Map; live Development Hub overlay requires separate rehearsal |

The public package intentionally **does not** bundle unsourced third-party skill files, private notes, credentials or provider sessions. File presence is not runtime execution proof.


<br />
<br />


## 🧭 Choose the next step


| You want to… | Follow |
| --- | --- |
| Install from scratch | [Start here](./START-HERE.md) |
| Get individual **copyable installation commands** | [Prerequisites](./docs/prerequisites.md) |
| Install or troubleshoot the 12 plugins | [Plugin catalog](./integrations/plugins/README.md) |
| Register the nine MCPs | [MCP catalog](./integrations/mcp/README.md) |
| Set up Claude Map and the existing overlay | [Claude Map](./docs/installation/claude-map.md) |
| Compare against the original Claude setup | [Coverage matrix](./docs/installation/reproducibility-matrix.md) |
| Understand file conflicts and restore options | [Full setup](./docs/installation/full-setup.md) |


<br />
<br />


## 🔄 Development workflow


```text
Triage  →  Contract  →  Dispatch  →  Review  →  Ship
             Agents • Skills • Rules
              Hooks • MCP • Memory
```

The dashboard is a local visualization of this architecture. **Detected** does not mean used, connected or authenticated.


<br />
<br />


## 🛡️ Security and support


Review commands before running them. Never commit `.claude.json`, `settings.json` containing tokens, private Obsidian notes or credentials. The installer refuses to overwrite different local files. Third-party extensions are installed from their publishers after approval.

[Security](./SECURITY.md) · [Third-party notices](./THIRD_PARTY_NOTICES.md) · [License](./LICENSE) · [Development documentation](./docs/README.md)
