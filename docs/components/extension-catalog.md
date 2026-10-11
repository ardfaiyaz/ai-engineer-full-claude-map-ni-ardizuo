# 🗂️ Master extension catalog


This catalog lists everything in the Ardizuo reference setup plus **74 researched rows**: 20 skills, 6 MCP integrations, 2 guardrail systems, 4 agent collections, 8 extension systems, 14 extension commands and 20 tools or references. The machine-readable source is [`setup/extension-catalog.json`](../../setup/extension-catalog.json).

All of it is part of the **one-command full installation**. `.\scripts\install-all.ps1 -Apply -All` installs the extended stack together with the agents, skills, commands, plugins, MCPs, hooks and vault. See the [extended stack guide](../installation/extensions.md) for commands and first-run steps.

Counts are catalog rows, not unique packages. One suite can supply skills, commands and agents, so it can appear in several sections. Last upstream check: **2026-10-11** (GitHub API, npm, PyPI and winget). That check proves names, IDs and licenses, not that each tool runs or signs in on Windows.


<br />
<br />


## 📋 How each row is delivered


| Delivery | Meaning |
| --- | --- |
| **Plugin** | Installed with `claude plugin install <id>@<marketplace>` after the marketplace is registered |
| **MCP** | Registered with `claude mcp add --scope user` |
| **CLI** | Global tool via `npm install -g`, `uv tool install` or `winget install` |
| **Pinned files** | Skill files downloaded at a fixed commit and hash-verified |
| **Git suite** | Cloned into the Claude config and set up with its own script |
| **Credential** | Needs your own API key, so the installer prints the command instead of running it |
| **Per project** | Only meaningful inside one project, so it is printed with instructions |
| **Reference** | A reading list or library; nothing to install |

Treat **discovered, documented, installed, enabled, authenticated and tested** as six different states. The installer reaches "installed" and "enabled"; sign-in and real use are up to you.


<br />
<br />


## 📦 Summary


| Category | Existing reference | Added in this catalog | Combined |
| --- | --- | --- | --- |
| Skills | 62 (+ the new Ardizuo `version-log`) | 20 | 82 named skills |
| MCP servers / integrations | 9 | 6 | 15 named integrations |
| Hooks and guardrails | 5 handler scripts | 2 external systems | 5 hooks + 2 systems, **not** 7 Ardizuo hooks |
| Agents / collections | 21 agents | 4 collections | 21 agents + 4 collection rows |
| Plugins / marketplaces / suites | 12 plugin IDs | 8 extension systems | 20 entries |
| Commands | 31 executable names | 14 extension commands | 45 command names |
| Other tools and references | — | 20 | 20 rows, with cross-category duplicates |

Behind those rows, the installer handles **40 packages**: 24 plugin packages (115 plugin IDs from 18 marketplaces), 3 MCP registrations, 7 global CLI tools, 1 pinned skill set, 1 git suite, 1 credential-gated MCP and 3 per-project setups.

The existing rows are documented in the [full reference inventory](./coverage.md), the [plugin catalog](../../integrations/plugins/README.md), the [MCP catalog](../../integrations/mcp/README.md), the [hook catalog](./hooks/README.md) and the [agent layer](./agents/README.md). This page doesn't repeat those lists, so they can't drift apart.


<br />
<br />


## ⚠️ Corrections found during verification


| Draft inventory assumption | Verified upstream fact (2026-10-11) |
| --- | --- |
| `steveyegge/beads` | Moved to [`gastownhall/beads`](https://github.com/gastownhall/beads); marketplace `beads-marketplace`; CLI `@beads/bd` |
| `ryoppippi/ccusage` | Moved to [`ccusage/ccusage`](https://github.com/ccusage/ccusage) |
| `affaan-m/everything-claude-code` | Renamed [`affaan-m/ECC`](https://github.com/affaan-m/ECC); plugin `ecc@ecc` (71 agents, 311 skills, hooks) |
| Firecrawl and Exa as standalone MCP servers | Both ship as official plugins: `firecrawl@claude-plugins-official`, `exa@claude-plugins-official` |
| Agentation is open source | License is **PolyForm Shield 1.0.0** (not OSI open source) |
| Probity is npm-only | It also ships a Claude plugin, `probity@probity`; the npm package is the per-project config |
| TDD Guard and Probity are unrelated | TDD Guard's README says it **grew into Probity** |
| `handoff`, `tdd`, `code-review`, `grill-me` names unverified | All exist in `mattpocock-skills@mattpocock` 1.3.1 |
| `karpathy-*` names unverified | Four skills exist (`coding-loop`, `verification`, `context-engineering`, `task-routing`); MIT license file; no marketplace |
| `/claude-hud:configure`, `/ce-*` unverified | All exist upstream (`commands/configure.md`, `skills/ce-*/SKILL.md`) |
| wshobson Agents is one install | It is a 94-plugin marketplace (`claude-code-workflows`); 92 are installed, 2 social-media plugins excluded |


<br />
<br />


## 🧩 1. Skills 63–82


| # | Skill | Delivered by | Verified upstream path | Note |
| --- | --- | --- | --- | --- |
| 63 | `ponytail` | `ponytail@ponytail` | `skills/ponytail/SKILL.md` | Overlaps `pragmatic-code-guidelines`; ships hooks |
| 64 | `domain-modeling` | `mattpocock-skills@mattpocock` | `skills/engineering/domain-modeling` | Triage |
| 65 | `codebase-design` | `mattpocock-skills@mattpocock` | `skills/engineering/codebase-design` | Contract |
| 66 | `grill-with-docs` | `mattpocock-skills@mattpocock` | `skills/engineering/grill-with-docs` | Triage |
| 67 | `to-tickets` | `mattpocock-skills@mattpocock` | `skills/engineering/to-tickets` | Contract |
| 68 | `handoff` | `mattpocock-skills@mattpocock` | `skills/productivity/handoff` | Ship |
| 69 | `differential-review` | `differential-review@trailofbits` | plugin | Review, security |
| 70 | `supply-chain-risk-auditor` | `supply-chain-risk-auditor@trailofbits` | plugin | Review, security |
| 71 | `property-based-testing` | `property-based-testing@trailofbits` | plugin | Review, testing |
| 72 | `mutation-testing` | `mutation-testing@trailofbits` | plugin | Review, testing |
| 73 | `spec-to-code-compliance` | `spec-to-code-compliance@trailofbits` | plugin | Review, correctness |
| 74 | `frontend-visual-qa` | `frontend-visual-qa@daymade-skills` | `frontend-visual-qa/SKILL.md` | Only this plugin from Daymade |
| 75 | `karpathy-coding-loop` | Pinned files | `skills/karpathy-coding-loop` (+ `references/examples.md`) | Hash-verified download |
| 76 | `karpathy-verification` | Pinned files | `skills/karpathy-verification` | Hash-verified download |
| 77 | `diagnosing-bugs` | `mattpocock-skills@mattpocock` | `skills/engineering/diagnosing-bugs` | Overlaps `root-cause-analysis` |
| 78 | `tdd` | `mattpocock-skills@mattpocock` | `skills/engineering/tdd` | Overlaps Superpowers TDD |
| 79 | `code-review` | `mattpocock-skills@mattpocock` | `skills/engineering/code-review` | Built-in `/code-review` also exists; use the namespace |
| 80 | `to-spec` | `mattpocock-skills@mattpocock` | `skills/engineering/to-spec` | Contract |
| 81 | `improve-codebase-architecture` | `mattpocock-skills@mattpocock` | `skills/engineering/improve-codebase-architecture` | Review |
| 82 | `grill-me` | `mattpocock-skills@mattpocock` | `skills/productivity/grill-me` | Triage |

Plugin skills are namespaced (for example `mattpocock-skills:prototype`), so they don't replace the existing pinned `prototype` skill. The Karpathy set also installs `karpathy-context-engineering` and `karpathy-task-routing` from the same commit.


<br />
<br />


## 🔌 2. MCP integrations 10–15


| # | Integration | Delivered by | Credentials | Note |
| --- | --- | --- | --- | --- |
| 10 | [Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server) | Plugin `firecrawl@claude-plugins-official` | Firecrawl API key | Extraction and crawling |
| 11 | [Exa](https://github.com/exa-labs/exa-mcp-server) | Plugin `exa@claude-plugins-official` | Exa account | Overlaps Tavily |
| 12 | [n8n MCP](https://github.com/czlonkowski/n8n-mcp) | MCP `n8n-mcp` (user scope) | None for docs tools | Management tools need an n8n API key |
| 13 | [21st Magic MCP](https://github.com/21st-dev/magic-mcp) | Plugin `21st@21st-dev` | `API_KEY_21ST` | React/Tailwind components |
| 14 | [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP `playwright-mcp` (user scope) | None | Runs next to the Playwright plugin |
| 15 | [Agentation MCP](https://github.com/benjitaylor/agentation) | MCP `agentation` (user scope) + `npm install -D agentation` per project | None | PolyForm Shield license |

MCP Inspector, ToolHive, Stagehand and mcp-use are tools, listed in section 7.


<br />
<br />


## 🪝 3. External guardrail systems 6–7


| # | System | Delivered by | Note |
| --- | --- | --- | --- |
| 6 | [Probity](https://github.com/nizos/probity) | Plugin `probity@probity` + per-project `@nizos/probity` and `probity.config.ts` | Rules activate only in projects with a config |
| 7 | [TDD Guard](https://github.com/nizos/tdd-guard) | Plugin `tdd-guard@tdd-guard` | Predecessor of Probity; type `tdd-guard off` if it blocks work |

These are **not** extra Ardizuo hook scripts; the five handlers stay as documented in the [hook catalog](./hooks/README.md). Both systems are installed, and the installer prints an overlap note because they enforce the same thing.


<br />
<br />


## 🤖 4. Agent collections 22–25


| # | Collection | Source | Delivered by |
| --- | --- | --- | --- |
| 22 | wshobson Agents | [wshobson/agents](https://github.com/wshobson/agents) | 92 plugins from marketplace `claude-code-workflows` (social-media plugins excluded) |
| 23 | Everything Claude Code | [affaan-m/ECC](https://github.com/affaan-m/ECC) | Plugin `ecc@ecc` |
| 24 | gstack | [garrytan/gstack](https://github.com/garrytan/gstack) | Git suite in `<ClaudeConfig>/skills/gstack` (needs Bash and Bun) |
| 25 | Compound Engineering | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | Plugin `compound-engineering@compound-engineering-plugin` |

Rows 22–25 are collections. They add their own agents inside plugins; the 21 global agent definitions stay as they are.


<br />
<br />


## 📦 5. Extension systems 13–20


| # | Extension | Exact install ID | Type | License |
| --- | --- | --- | --- | --- |
| 13 | [OpenAI Codex Plugin](https://github.com/openai/codex-plugin-cc) | `codex@openai-codex` + `@openai/codex` CLI | Plugin + CLI | Apache-2.0 |
| 14 | [Claude HUD](https://github.com/jarrodwatts/claude-hud) | `claude-hud@claude-hud` | Plugin | MIT |
| 15 | [Trail of Bits](https://github.com/trailofbits/skills) | Six `<plugin>@trailofbits` IDs | Marketplace of 44 plugins; the six catalogued ones are installed | CC-BY-SA-4.0 |
| 16 | [Matt Pocock Skills](https://github.com/mattpocock/skills) | `mattpocock-skills@mattpocock` | Plugin with 27 skills | MIT |
| 17 | [Daymade Skills](https://github.com/daymade/claude-code-skills) | `frontend-visual-qa@daymade-skills` | Marketplace of 61 plugins; the catalogued one is installed | MIT |
| 18 | [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | `compound-engineering@compound-engineering-plugin` | Plugin | MIT |
| 19 | [Claude-Mem](https://github.com/thedotmack/claude-mem) | `claude-mem@thedotmack` | Plugin | Apache-2.0 |
| 20 | [gstack](https://github.com/garrytan/gstack) | Git clone + `./setup` | Workflow suite | MIT |


<br />
<br />


## ⌨️ 6. Extension commands 32–45


| # | Command | Provider | Verification |
| --- | --- | --- | --- |
| 32 | `/codex:setup` | Codex plugin | `plugins/codex/commands/setup.md` |
| 33 | `/codex:review` | Codex plugin | `plugins/codex/commands/review.md` |
| 34 | `/claude-hud:setup` | Claude HUD | `commands/setup.md` |
| 35 | `/claude-hud:configure` | Claude HUD | `commands/configure.md` |
| 36 | `/reload-plugins` | Claude Code | Built-in; depends on Claude Code version |
| 37 | `/setup-matt-pocock-skills` | Matt Pocock Skills | Skill file; may appear namespaced |
| 38 | `/grill-with-docs` | Matt Pocock Skills | Skill file; may appear namespaced |
| 39 | `/ce-brainstorm` | Compound Engineering | Skill file; may appear namespaced |
| 40 | `/ce-plan` | Compound Engineering | Skill file; may appear namespaced |
| 41 | `/ce-work` | Compound Engineering | Skill file; may appear namespaced |
| 42 | `/ce-code-review` | Compound Engineering | Skill file; may appear namespaced |
| 43 | `/ce-compound` | Compound Engineering | Skill file; may appear namespaced |
| 44 | `/ce-debug` | Compound Engineering | Skill file; may appear namespaced |
| 45 | `/ce-handoff` | Compound Engineering | Skill file; may appear namespaced |

They appear after the full installation. Check the slash menu once before relying on an exact name.


<br />
<br />


## 🛠️ 7. Developer tools and references


| # | Project | Delivered by | Note |
| --- | --- | --- | --- |
| 1 | [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | CLI `npm install -g @modelcontextprotocol/inspector` | Run `mcp-inspector` when debugging; opens a localhost port |
| 2 | [Beads](https://github.com/gastownhall/beads) | CLI `@beads/bd` + plugin `beads@beads-marketplace` | `bd init` per project |
| 3 | [mcp-use](https://github.com/mcp-use/mcp-use) | Plugin `all-skills@mcp-use` + per-project starter | SDK goes into each project |
| 4 | [Snyk Agent Scan](https://github.com/snyk/agent-scan) | CLI `uv tool install snyk-agent-scan` | A scan can send tool descriptions to Snyk |
| 5 | [AutoHarness](https://github.com/tigerless-labs/autoharness) | Plugin `autoharness@autoharness` | Experimental; Windows unverified |
| 6 | [i-have-adhd](https://github.com/leondebeer/i-have-adhd) | Plugin `i-have-adhd@i-have-adhd` | Changes response style |
| 7 | [Karpathy-inspired Skills](https://github.com/benfngu/karpathy-claude-skills) | Pinned files (4 skills) | Hash-verified |
| 8 | [Everything Claude Code](https://github.com/affaan-m/ECC) | Plugin `ecc@ecc` | Very large; hooks on by default |
| 9 | [wshobson Agents](https://github.com/wshobson/agents) | 92 plugins | Very large |
| 10 | [GitHub Spec Kit](https://github.com/github/spec-kit) | CLI `uv tool install specify-cli` + per-project `specify init` | Needs Python 3.11+ |
| 11 | [Daymade Skills](https://github.com/daymade/claude-code-skills) | Plugin `frontend-visual-qa@daymade-skills` | Catalogued plugin only |
| 12 | [ccusage](https://github.com/ccusage/ccusage) | CLI `npm install -g ccusage` | Overlaps Claude Map usage views |
| 13 | [Browserbase Stagehand](https://github.com/browserbase/stagehand) | Credential: Browserbase MCP; SDK per project | Needs a Browserbase key |
| 14 | [ToolHive](https://github.com/stacklok/toolhive) | CLI `winget install stacklok.thv` | Needs Docker or Podman |
| 15 | [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) | Reference | Examples to read, not a single install |
| 16 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | Reference | Library for your own MCP projects |
| 17 | mcp-use Inspector | Part of mcp-use | Not a separate package |
| 18 | [Trail of Bits static analysis](https://github.com/trailofbits/skills) | Plugin `static-analysis@trailofbits` | Needs CodeQL/Semgrep |
| 19 | [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) | Reference | Discovery list |
| 20 | [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code) | Reference | Discovery list |


<br />
<br />


## 🧭 8. Overlaps inside the single installation


Everything is installed. These groups do similar jobs, so the installer prints a note, and you can disable one member if they get in each other's way.

| Capability | Already in the baseline | Also installed | What to watch |
| --- | --- | --- | --- |
| Orchestration | SuperClaude + Superpowers + five-stage workflow | Compound Engineering, gstack, ECC | Pick one workflow per task |
| Code simplicity | `pragmatic-code-guidelines`, `clean-code-typescript` | Ponytail, Karpathy skills | Similar rules; fine together |
| Browser automation | Playwright plugin, Chrome DevTools MCP | Playwright MCP, Browserbase (with a key) | Don't drive one browser from two servers |
| Web search and extraction | Tavily MCP | Firecrawl, Exa | Firecrawl for extraction, Tavily for search |
| Memory and tasks | Obsidian vault-learning | Claude-Mem, Beads | Review what Claude-Mem records |
| TDD enforcement | Test/quality skills and hooks | Probity, TDD Guard | Two enforcers can block the same edit |
| Usage reporting | Claude Map | Claude HUD, ccusage | Different views of the same data |

[Extended stack guide](../installation/extensions.md) · [Component catalog](./README.md) · [Third-party notices](../../THIRD_PARTY_NOTICES.md)
