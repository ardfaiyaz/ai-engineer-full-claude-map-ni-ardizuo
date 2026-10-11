# 🧩 Extended stack


The extended stack is every researched tool from the [master extension catalog](../components/extension-catalog.md), installed by the **same one-command installation** as the rest of the setup. `.\scripts\install-all.ps1 -Apply -All` installs it automatically. There is no separate optional step.

It covers 40 packages from `setup/extension-catalog.json`:

| Install type | Packages | What the installer does |
| --- | --- | --- |
| Plugins | 24 packages, **115 plugin IDs** from 18 marketplaces | Registers each marketplace, then `claude plugin install` for every ID not already enabled |
| MCP registrations | 3 (`n8n-mcp`, `playwright-mcp`, `agentation`) | `claude mcp add --scope user …` unless the name already exists |
| Global CLI tools | 7 (`codex`, `bd`, `mcp-inspector`, `snyk-agent-scan`, `ccusage`, `specify`, `thv`) | `npm install -g`, `uv tool install` or `winget install` unless the command is already on `PATH` |
| Pinned skill files | 1 (4 Karpathy skills, 6 files) | Downloads at a fixed commit, verifies every Git blob hash, writes only absent files |
| Git skill suite | 1 (gstack) | Clones into `<ClaudeConfig>/skills/gstack` and runs its `./setup` |
| Credential-gated | 1 (Browserbase MCP for Stagehand) | Printed: needs your own API key, like Tavily and Morph |
| Per-project | 3 (Probity config, Spec Kit init, mcp-use app) | Printed: these only make sense inside a specific project |

Four catalog rows aren't installable at all, because they are reading lists or libraries: Awesome Claude Code, Awesome MCP Servers, MCP Reference Servers and the MCP TypeScript SDK.


<br />
<br />


## 🚀 Install everything


From **Windows PowerShell** in the repository root:

```powershell
# Preview the full setup, including the extended stack (nothing changes).
.\scripts\install-all.ps1 -All

# Install everything after reviewing the preview.
.\scripts\install-all.ps1 -Apply -All

# Check what is enabled, registered or on PATH (names only).
python .\scripts\install-extensions.py --status
```

To install **only** the extended stack, or part of it, without the rest of `-All`:

```powershell
.\scripts\install-all.ps1 -Apply -External -Extensions all          # the whole extended stack
.\scripts\install-all.ps1 -Apply -External -Extensions security     # one group
.\scripts\install-all.ps1 -Apply -External -Extensions codex,ponytail   # specific packages
```

`-All` passes `-Extensions all` unless you give your own `-Extensions` value, so `-All -Extensions priority` narrows the extended part to the priority group.


<br />
<br />


## 📋 Groups


Groups let you install or re-run part of the stack. `all` is every package.

| Group | Packages |
| --- | --- |
| `priority` | Codex plugin + CLI, Claude HUD, Trail of Bits `differential-review`, Ponytail, Firecrawl, Agentation, Probity, Beads plugin + CLI, mcp-use skills, MCP Inspector |
| `security` | Six Trail of Bits plugins, Snyk Agent Scan |
| `testing` | Property-based testing, mutation testing, Probity, TDD Guard, Probity project setup |
| `engineering` | Matt Pocock skills, Ponytail, AutoHarness, Karpathy skills |
| `frontend` | Daymade `frontend-visual-qa`, 21st Magic, Agentation |
| `research` | Firecrawl, Exa |
| `review` | Codex plugin + CLI |
| `workflow` | Compound Engineering, Beads, Spec Kit, gstack |
| `collections` | Everything Claude Code (ECC), wshobson Agents (92 plugins) |
| `mcp-dev` | mcp-use, MCP Inspector, ToolHive, mcp-use project starter |
| `browser` | Playwright MCP, Stagehand / Browserbase |
| `automation` | n8n MCP |
| `memory` | Claude-Mem |
| `usage` | ccusage |
| `style` | i-have-adhd |


<br />
<br />


## ⚠️ Overlaps are installed together


Some packages do the same job. Because you asked for everything in one installation, the installer installs **all** of them and prints a note for each overlap. If two of them get in each other's way, disable one with `claude plugin disable <id>`.

| Overlap | Installed together | What to watch |
| --- | --- | --- |
| TDD enforcement | Probity, TDD Guard | Both can block edits until a failing test exists. If work is blocked, type `tdd-guard off` in a prompt or disable one plugin |
| Orchestration | Compound Engineering, gstack, Everything Claude Code, next to Superpowers + SuperClaude | Several workflows offer their own plan/review/ship commands; pick one per task |
| Web research | Firecrawl, Exa, plus the existing Tavily | Firecrawl is best for extraction, Tavily for search |
| Code simplicity | Ponytail, Karpathy skills, plus `pragmatic-code-guidelines` | Similar rules; harmless together |
| Browser automation | Playwright MCP, plus the existing Playwright plugin and Chrome DevTools MCP | Don't drive one browser from two servers at once |
| Memory | Claude-Mem, plus Obsidian `vault-learning` | Claude-Mem records sessions automatically; review its privacy settings |

**Size warning:** ECC adds 71 agents and 311 skills, and wshobson Agents adds 92 plugins. Every session lists their skills and agents, which uses more context and makes skill selection noisier. If that becomes a problem, disable the collections you don't use; they stay installed.


<br />
<br />


## 📦 Every package


| ID | Type | What you get | Needs |
| --- | --- | --- | --- |
| `codex` | plugin | `/codex:review`, `/codex:adversarial-review`, `/codex:rescue` and a `codex-rescue` agent: a second model reviews your diff | `codex-cli` + OpenAI/ChatGPT sign-in |
| `codex-cli` | CLI | `codex` command (`@openai/codex`) | npm |
| `claude-hud` | plugin | Status line with context use, rate limits, active tools, running agents and todo progress | — |
| `tob-differential-review` | plugin | Security-focused review of changed code | — |
| `tob-supply-chain-risk-auditor` | plugin | Dependency and supply-chain risk review | — |
| `tob-property-based-testing` | plugin | Property-based tests and invariants | A property-testing library in the project |
| `tob-mutation-testing` | plugin | Checks whether tests catch deliberate mutations | A mutation tool for the language |
| `tob-spec-to-code-compliance` | plugin | Compares an implementation with its specification | A written spec |
| `tob-static-analysis` | plugin | Guided CodeQL and Semgrep analysis | CodeQL and/or Semgrep |
| `mattpocock-skills` | plugin | 27 skills: `grill-me`, `grill-with-docs`, `to-spec`, `to-tickets`, `tdd`, `diagnosing-bugs`, `domain-modeling`, `codebase-design`, `handoff` and more | `/setup-matt-pocock-skills` once per repo |
| `frontend-visual-qa` | plugin | Audits rendered UI for visual defects | A running frontend |
| `ponytail` | plugin | Simplest-working-solution mode plus `ponytail-audit`, `ponytail-review`, `ponytail-debt`; adds hooks | — |
| `firecrawl` | plugin | Scrape, crawl, search and extract websites | Firecrawl API key |
| `exa` | plugin | Exa web, company, people and paper search | Exa account |
| `21st-magic` | plugin | 21st.dev React/Tailwind component generation | `API_KEY_21ST` |
| `n8n-mcp` | MCP | n8n node documentation and workflow validation | — (management tools need `N8N_API_URL`/`N8N_API_KEY`) |
| `playwright-mcp` | MCP | Microsoft Playwright browser automation server | — |
| `agentation` | MCP | Receives structured UI feedback from the Agentation component | `npm install -D agentation` per React/Next.js project |
| `compound-engineering` | plugin | `/ce-brainstorm`, `/ce-plan`, `/ce-work`, `/ce-code-review`, `/ce-compound`, `/ce-debug`, `/ce-handoff` and more | — |
| `claude-mem` | plugin | Automatic memory across sessions | Privacy review |
| `probity` | plugin | TDD and rule enforcement hooks | `probity.config.ts` per project |
| `tdd-guard` | plugin | Blocks implementation before a failing test | A test reporter per project |
| `autoharness` | plugin | Derives and refines skills from your sessions | Experimental |
| `i-have-adhd` | plugin | Short, action-first answers | — |
| `beads` | plugin | Beads skills and commands | `beads-cli` |
| `beads-cli` | CLI | `bd` issue and dependency tracker | npm; `bd init` per project |
| `mcp-use` | plugin | `all-skills@mcp-use`: build, debug and deploy MCP servers and apps | — |
| `mcp-inspector` | CLI | `mcp-inspector` web/CLI/TUI debugger | npm |
| `karpathy-skills` | pinned files | `karpathy-coding-loop`, `karpathy-verification`, `karpathy-context-engineering`, `karpathy-task-routing` | — |
| `snyk-agent-scan` | CLI | Scans MCP configs and skills for prompt injection and risky tools | uv |
| `ccusage` | CLI | Token and cost report from local Claude Code logs | npm |
| `spec-kit` | CLI | `specify` CLI for spec-driven development | uv, Python 3.11+ |
| `toolhive` | CLI | `thv` runs MCP servers in isolated containers | winget; Docker or Podman |
| `gstack` | git suite | Role-based skills such as `/office-hours`, `/review`, `/qa`, `/ship` | Git, Bash (Git Bash), Bun 1.4.2+ |
| `stagehand` | credential | Browserbase hosted browser MCP; Stagehand SDK per project | Browserbase API key |
| `everything-claude-code` | plugin | `ecc@ecc`: 71 agents, 311 skills, hooks, rules | — |
| `wshobson-agents` | plugin | 92 plugins from `claude-code-workflows` (social-media plugins excluded) | — |
| `probity-project` | per project | `npm install -D @nizos/probity` and `probity.config.ts` | Node project |
| `spec-kit-project` | per project | `specify init <project> --integration claude` | `spec-kit` |
| `mcp-use-project` | per project | `npx -y create-mcp-use-app@latest` | Node.js |

The two wshobson plugins named `social-publishing` and `hermes-tweet` are left out on purpose: this setup's rules forbid social-media automation.


<br />
<br />


## 🔑 First run after installing


Installing puts each tool in place. These one-time steps make them usable:

| Extension | One-time step |
| --- | --- |
| Codex | `codex login` (ChatGPT or API key), then `/codex:setup` in Claude Code. Use `/codex:review` on a diff. |
| Claude HUD | `/claude-hud:setup`, then `/claude-hud:configure`; restart Claude Code. |
| Matt Pocock skills | `/setup-matt-pocock-skills` in each repository where you want them. |
| Firecrawl, Exa, 21st Magic | Provider sign-in or key flow (see [API key safety](../security/api-keys-and-powershell.md)); then check `/mcp`. |
| Trail of Bits `static-analysis` | `uv tool install semgrep` and/or install CodeQL. |
| Ponytail, Probity, TDD Guard, ECC, Claude-Mem | Open `/hooks` and review the hooks they added next to the five Ardizuo hooks. |
| Beads | `bd init` inside a project. |
| n8n MCP | Works for documentation tools at once; add `N8N_API_URL`/`N8N_API_KEY` securely for management tools. |
| gstack | If Bun was missing, install it from [bun.sh](https://bun.sh/) and re-run `.\scripts\install-all.ps1 -Apply -External -Extensions gstack`. |
| Stagehand / Browserbase | Register the Browserbase MCP with your own key through a secure flow. |

Inside Claude Code, run `/reload-plugins` (if your version has it) or restart, then check `/plugin`, `/skills`, `/mcp` and `/hooks`.


<br />
<br />


## ⌨️ Manual commands


The installer runs these for you. They are listed so you can repair one item by hand.

```powershell
# Marketplaces (add only the missing ones)
claude plugin marketplace add openai/codex-plugin-cc
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin marketplace add trailofbits/skills
claude plugin marketplace add mattpocock/skills
claude plugin marketplace add daymade/claude-code-skills
claude plugin marketplace add DietrichGebert/ponytail
claude plugin marketplace add 21st-dev/magic-mcp
claude plugin marketplace add EveryInc/compound-engineering-plugin
claude plugin marketplace add thedotmack/claude-mem
claude plugin marketplace add nizos/tdd-guard
claude plugin marketplace add nizos/probity
claude plugin marketplace add tigerless-labs/autoharness
claude plugin marketplace add leondebeer/i-have-adhd
claude plugin marketplace add gastownhall/beads
claude plugin marketplace add mcp-use/mcp-use
claude plugin marketplace add affaan-m/ECC
claude plugin marketplace add wshobson/agents

# Plugins
claude plugin install codex@openai-codex
claude plugin install claude-hud@claude-hud
claude plugin install differential-review@trailofbits
claude plugin install supply-chain-risk-auditor@trailofbits
claude plugin install property-based-testing@trailofbits
claude plugin install mutation-testing@trailofbits
claude plugin install spec-to-code-compliance@trailofbits
claude plugin install static-analysis@trailofbits
claude plugin install mattpocock-skills@mattpocock
claude plugin install frontend-visual-qa@daymade-skills
claude plugin install ponytail@ponytail
claude plugin install firecrawl@claude-plugins-official
claude plugin install exa@claude-plugins-official
claude plugin install 21st@21st-dev
claude plugin install compound-engineering@compound-engineering-plugin
claude plugin install claude-mem@thedotmack
claude plugin install probity@probity
claude plugin install tdd-guard@tdd-guard
claude plugin install autoharness@autoharness
claude plugin install i-have-adhd@i-have-adhd
claude plugin install beads@beads-marketplace
claude plugin install all-skills@mcp-use
claude plugin install ecc@ecc
# wshobson: 92 IDs ending in @claude-code-workflows; list them with
python .\scripts\install-extensions.py --list

# MCP registrations
claude mcp add --scope user n8n-mcp -e MCP_MODE=stdio -e LOG_LEVEL=error -e DISABLE_CONSOLE_OUTPUT=true -- npx -y n8n-mcp
claude mcp add --scope user playwright-mcp -- npx -y @playwright/mcp@latest
claude mcp add --scope user agentation -- npx -y agentation-mcp server

# Global CLI tools
npm.cmd install -g @openai/codex
npm.cmd install -g @beads/bd
npm.cmd install -g @modelcontextprotocol/inspector
npm.cmd install -g ccusage
uv tool install snyk-agent-scan
uv tool install specify-cli
winget install --id stacklok.thv --exact --source winget
```

The exact list, including all 92 wshobson plugin IDs, lives in `setup/extension-catalog.json`.


<br />
<br />


## 🛡️ Safety


- Provider sign-in (Codex, Firecrawl, Exa, 21st, Browserbase) happens in each publisher's own flow. Never paste API keys into commands, issues or commits.
- Several packages add hooks. Review `/hooks` after installing and disable any you don't want.
- Agentation uses the PolyForm Shield license (not open source); Trail of Bits content is CC-BY-SA-4.0. Both are installed from their publishers and never copied into this repository.
- Snyk Agent Scan can send tool descriptions to Snyk when you run a scan. Installing it sends nothing.
- An exit code of 0 means only that the CLI accepted the command. It doesn't prove a plugin is enabled, signed in or working.


<br />
<br />


## 🧹 Remove or disable one item


```powershell
claude plugin disable ponytail@ponytail          # keep it installed but off
claude plugin uninstall ponytail@ponytail        # remove it
claude plugin marketplace remove ponytail        # only if no other plugin uses that marketplace
claude mcp remove n8n-mcp                        # remove an MCP registration
npm.cmd uninstall -g ccusage                     # remove a global npm tool
uv tool uninstall specify-cli                    # remove a uv tool
```

The Karpathy skill folders and `skills/gstack` can be deleted from your Claude config folder like any other skill.


<br />
<br />


## 🔎 How the catalog was verified


Every entry was checked on **2026-10-11** through the GitHub API and npm/PyPI/winget: repository, license, default-branch commit, `.claude-plugin/marketplace.json` plugin names, the `SKILL.md` or command file behind each named skill or command, and each package name. The installer was dry-run against all 40 packages, and the pinned Karpathy download was run for real into a throwaway folder (6 files, hashes verified). Plugins, MCPs and CLI tools have **not** been installed or signed in on a clean Windows machine yet.

[Master catalog](../components/extension-catalog.md) · [Plugins](../../integrations/plugins/README.md) · [MCPs](../../integrations/mcp/README.md) · [Installation index](./README.md)
