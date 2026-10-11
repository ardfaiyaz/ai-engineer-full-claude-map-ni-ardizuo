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
| Direct skills | 36/62 reference skills by default (41/62 with opt-in, **different** upstream variants), plus the new Ardizuo `version-log` skill |
| Executable commands | 20/31 by default; 31/31 with optional upstream variants |
| Plugins | Installation attempts for all 12 listed plugins; authentication is individual |
| MCP servers | Nine listed servers; supported registrations plus guided manual authentication |
| Hooks | Five handlers and optional registration |
| Workflow | Five stages, rules, gates and portable context |
| Memory | Optional empty Obsidian folder structure and four templates |
| Dashboard | Optional Claude Map; live Development Hub overlay requires separate rehearsal |
| Extended stack | 74 researched catalog rows delivered by 40 packages: 115 plugin IDs, 3 MCPs, 7 CLI tools, pinned Karpathy skills and gstack |

The public package intentionally **does not** bundle unsourced third-party skill files, private notes, credentials or provider sessions. File presence is not runtime execution proof.

`-All` installs **every layer above, including the extended stack**, in one run. Each layer also has its own switch (`-Plugins`, `-Mcps`, `-Hooks`, `-Vault`, …); see the [switch reference](./docs/installation/full-setup.md).


<br />
<br />


## 🧩 Extended stack (part of the one installation)


A researched [master extension catalog](./docs/components/extension-catalog.md) adds **74 rows** to the reference setup: 20 skills, 6 MCP integrations, 2 guardrail systems, 4 agent collections, 8 extension systems, 14 commands and 20 developer tools. Every repository, license, plugin ID, package name and skill or command path was checked upstream on 2026-10-11.

They are installed by the same `-All` run as everything else; nothing is left as a separate optional step.

| Highlights | What it adds | Delivered as |
| --- | --- | --- |
| OpenAI Codex | A second model reviews your changes (`/codex:review`) | Plugin `codex@openai-codex` + `codex` CLI |
| Claude HUD | Status line with context use, tools, agents and todos | Plugin `claude-hud@claude-hud` |
| Trail of Bits | Differential review, supply-chain audit, mutation and property-based testing, static analysis | Six plugins `…@trailofbits` |
| Matt Pocock skills | `grill-me`, `to-spec`, `to-tickets`, `tdd`, `domain-modeling` and 22 more | Plugin `mattpocock-skills@mattpocock` |
| Firecrawl, Exa, 21st Magic, n8n | Web extraction, search, UI components, n8n workflows | Plugins and MCP registrations |
| Probity, TDD Guard, Ponytail, Compound Engineering, Claude-Mem, Beads | Guardrails, simplicity mode, workflows, memory, task tracking | Plugins (+ `bd` CLI) |
| ECC and wshobson Agents | Large agent and skill collections | `ecc@ecc` + 92 `claude-code-workflows` plugins |
| MCP Inspector, Snyk Agent Scan, ccusage, Spec Kit, ToolHive | Developer CLIs | `npm`, `uv` and `winget` global installs |
| Karpathy skills, gstack | Skill files and a role-based skill suite | Hash-pinned download; Git clone + setup |

```powershell
.\scripts\install-all.ps1 -All                       # preview everything, including the extended stack
.\scripts\install-all.ps1 -Apply -All                # install everything
python .\scripts\install-extensions.py --status       # what is enabled, registered or on PATH now
python .\scripts\install-extensions.py --list         # every package, type and group
```

A few rows can't be installed for you: Browserbase/Stagehand needs your own API key, Probity/Spec Kit/mcp-use have per-project setup steps, and four rows are reading lists or libraries. The installer prints those steps. Overlapping tools (for example Probity and TDD Guard) are installed together with a warning; see the [extended stack guide](./docs/installation/extensions.md).


<br />
<br />


## 🧭 Choose the next step


| You want to… | Follow |
| --- | --- |
| Install from scratch | [Start here](./START-HERE.md) |
| Get individual **copyable installation commands** | [Prerequisites](./docs/prerequisites.md) |
| Install or troubleshoot the 12 plugins | [Plugin catalog](./integrations/plugins/README.md) |
| Register the nine MCPs | [MCP catalog](./integrations/mcp/README.md) |
| Understand or repair the extended stack (Codex, Claude HUD, Trail of Bits, …) | [Extended stack](./docs/installation/extensions.md) · [Master catalog](./docs/components/extension-catalog.md) |
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

The dashboard is a local visualization of this architecture. **Detected** does not mean used, connected or authenticated. See [architecture](./docs/architecture.md) for what each stage does and which extended-stack tools fit where.


<br />
<br />


## 📁 Repository layout


| Path | Contents |
| --- | --- |
| `ardizuo-plugin/` | The 29 reviewed original files: 17 skills (including `version-log`), `diagram-architect`, `log-to-vault`, five hooks + helper, rules and workflows |
| `global-config/` | Portable `CLAUDE.md` and the base development rule |
| `setup/` | Manifests: baseline stack, pinned sources, release coverage, reference inventory and the **extension catalog** |
| `scripts/` | Installers (`install-all`, `install-extensions`, pinned installers, dashboard), verifiers and audits |
| `integrations/` | Plugin and MCP catalogs with copyable commands |
| `dashboard/claude-map/` | Development Hub overlay patches and rehearsal guide |
| `vault/` | Obsidian folder guide and four note templates |
| `docs/` | Installation guides, component catalogs, security and release material |
| `tests/` | Offline checks run by CI on every push |


<br />
<br />


## 🛡️ Security and support


Review commands before running them. Never commit `.claude.json`, `settings.json` containing tokens, private Obsidian notes or credentials. The installer refuses to overwrite different local files. Third-party extensions are installed from their publishers after approval.

[Security](./SECURITY.md) · [Third-party notices](./THIRD_PARTY_NOTICES.md) · [License](./LICENSE) · [Development documentation](./docs/README.md)
