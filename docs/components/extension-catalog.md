# 🗂️ Master extension catalog


This catalog lists everything in the Ardizuo reference setup plus **74 researched extension rows**: 20 skills, 6 MCP integrations, 2 guardrail systems, 4 agent collections, 8 extension systems, 14 extension commands and 20 tools or references. The machine-readable source is [`setup/extension-catalog.json`](../../setup/extension-catalog.json).

**This is an inventory and integration plan, not a claim of 214 working installations.** Counts are catalog rows, not unique packages. One suite can supply skills, commands and agents, so it can appear in several sections.

Last upstream check: **2026-10-11**, via the GitHub API (repository, license, default-branch commit, `.claude-plugin` manifests and the `SKILL.md` or command path). That check does not prove that a tool runs, signs in, or works on Windows.


<br />
<br />


## 📋 How to read the status labels


| Label | Meaning |
| --- | --- |
| **Existing** | Named in the reference inventory. Being in the repository does not prove it runs on a new machine. |
| **Verified upstream** | The exact plugin ID, skill or command file was found in the publisher's repository at the commit recorded in the JSON file. |
| **Optional** | Install per project or by explicit opt-in. Never part of `-All`. |
| **Alternative** | Overlaps something you already use. Pick one; the installer refuses two from the same group. |
| **Guided** | Project-scoped, on-demand or manual. The installer prints its commands and never runs them. |
| **Reference** | A library, SDK or directory, not a single Claude Code component. |

Treat **discovered, documented, installed, enabled, authenticated and tested** as six different states.


<br />
<br />


## 📦 Summary


| Category | Existing reference | Added in this catalog | Combined |
| --- | --- | --- | --- |
| Skills | 62 | 20 | 82 named skills |
| MCP servers / integrations | 9 | 6 | 15 named integrations |
| Hooks and guardrails | 5 handler scripts | 2 external systems | 5 hooks + 2 systems, **not** 7 hooks |
| Agents / collections | 21 agents | 4 collections | 21 agents + 4 collection rows |
| Plugins / marketplaces / suites | 12 plugin IDs | 8 extension systems | 20 entries |
| Commands | 31 executable names | 14 extension commands | 45 command names |
| Other tools and references | — | 20 | 20 rows, with cross-category duplicates |

The existing rows are already documented in the [full reference inventory](./coverage.md), the [12-plugin catalog](../../integrations/plugins/README.md), the [nine-MCP catalog](../../integrations/mcp/README.md), the [hook catalog](./hooks/README.md) and the [agent layer](./agents/README.md). This page does not repeat those lists, so the two can't drift apart.


<br />
<br />


## ⚠️ Corrections found during verification


| Catalog assumption | Verified upstream fact (2026-10-11) |
| --- | --- |
| `steveyegge/beads` | Moved to [`gastownhall/beads`](https://github.com/gastownhall/beads); marketplace `beads-marketplace` |
| `ryoppippi/ccusage` | Moved to [`ccusage/ccusage`](https://github.com/ccusage/ccusage) |
| `affaan-m/everything-claude-code` | Renamed [`affaan-m/ECC`](https://github.com/affaan-m/ECC); marketplace `ecc` |
| Firecrawl and Exa as standalone MCP servers | Both ship as official plugins: `firecrawl@claude-plugins-official`, `exa@claude-plugins-official` |
| Agentation is open source | License is **PolyForm Shield 1.0.0** (not OSI open source); project use only after review |
| TDD Guard and Probity are separate options | TDD Guard's README says it **grew into Probity**; treat them as one exclusive group |
| `handoff`, `tdd`, `code-review`, `grill-me` names unverified | All exist in `mattpocock-skills@mattpocock` 1.3.1 |
| `karpathy-*` names unverified | `karpathy-coding-loop` and `karpathy-verification` exist; MIT license file; no marketplace |
| `/claude-hud:configure`, `/ce-*` unverified | All exist upstream (`commands/configure.md`, `skills/ce-*/SKILL.md`) |


<br />
<br />


## 🧩 1. Skills 63–82


| # | Skill | Delivered by | Verified upstream path | Note |
| --- | --- | --- | --- | --- |
| 63 | `ponytail` | `ponytail@ponytail` | `skills/ponytail/SKILL.md` | Overlaps `pragmatic-code-guidelines`; ships hooks |
| 64 | `domain-modeling` | `mattpocock-skills@mattpocock` | `skills/engineering/domain-modeling` | Optional |
| 65 | `codebase-design` | `mattpocock-skills@mattpocock` | `skills/engineering/codebase-design` | Optional |
| 66 | `grill-with-docs` | `mattpocock-skills@mattpocock` | `skills/engineering/grill-with-docs` | Optional |
| 67 | `to-tickets` | `mattpocock-skills@mattpocock` | `skills/engineering/to-tickets` | Optional |
| 68 | `handoff` | `mattpocock-skills@mattpocock` | `skills/productivity/handoff` | Optional |
| 69 | `differential-review` | `differential-review@trailofbits` | plugin | Recommended security skill |
| 70 | `supply-chain-risk-auditor` | `supply-chain-risk-auditor@trailofbits` | plugin | Optional security |
| 71 | `property-based-testing` | `property-based-testing@trailofbits` | plugin | Optional testing |
| 72 | `mutation-testing` | `mutation-testing@trailofbits` | plugin | Optional testing |
| 73 | `spec-to-code-compliance` | `spec-to-code-compliance@trailofbits` | plugin | Optional correctness |
| 74 | `frontend-visual-qa` | `frontend-visual-qa@daymade-skills` | `frontend-visual-qa/SKILL.md` | Install only this plugin from Daymade |
| 75 | `karpathy-coding-loop` | Guided manual copy | `skills/karpathy-coding-loop` | No marketplace; Bash installer |
| 76 | `karpathy-verification` | Guided manual copy | `skills/karpathy-verification` | No marketplace; Bash installer |
| 77 | `diagnosing-bugs` | `mattpocock-skills@mattpocock` | `skills/engineering/diagnosing-bugs` | Overlaps `root-cause-analysis` |
| 78 | `tdd` | `mattpocock-skills@mattpocock` | `skills/engineering/tdd` | Overlaps Superpowers TDD |
| 79 | `code-review` | `mattpocock-skills@mattpocock` | `skills/engineering/code-review` | Built-in `/code-review` also exists; use the namespace |
| 80 | `to-spec` | `mattpocock-skills@mattpocock` | `skills/engineering/to-spec` | Optional |
| 81 | `improve-codebase-architecture` | `mattpocock-skills@mattpocock` | `skills/engineering/improve-codebase-architecture` | Optional |
| 82 | `grill-me` | `mattpocock-skills@mattpocock` | `skills/productivity/grill-me` | Optional |

Plugin skills are namespaced (for example `mattpocock-skills:prototype`), so they don't replace the existing pinned `prototype` skill.


<br />
<br />


## 🔌 2. MCP integrations 10–15


| # | Integration | Install route | Credentials | Status |
| --- | --- | --- | --- | --- |
| 10 | [Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server) | `firecrawl@claude-plugins-official` | Firecrawl API key | Optional; extraction, not a Tavily replacement |
| 11 | [Exa](https://github.com/exa-labs/exa-mcp-server) | `exa@claude-plugins-official` | Exa account | Optional; overlaps Tavily |
| 12 | [n8n MCP](https://github.com/czlonkowski/n8n-mcp) | User stdio registration `n8n-mcp` | None for docs tools | Optional if you use n8n |
| 13 | [21st Magic MCP](https://github.com/21st-dev/magic-mcp) | `21st@21st-dev` | `API_KEY_21ST` | Optional frontend |
| 14 | [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp) | User stdio registration `playwright-mcp` | None | **Alternative** to the Playwright plugin |
| 15 | [Agentation MCP](https://github.com/benjitaylor/agentation) | Guided, inside one React/Next.js project | None | Project-only; PolyForm Shield license |

Don't register all 15 as permanent global servers. MCP Inspector, ToolHive, Stagehand and mcp-use are tools, listed in section 7.


<br />
<br />


## 🪝 3. External guardrail systems 6–7


| # | System | Route | Note |
| --- | --- | --- | --- |
| 6 | [Probity](https://github.com/nizos/probity) | Guided: `npm install -D @nizos/probity` in one test project | Compare with the five Ardizuo hooks before enabling |
| 7 | [TDD Guard](https://github.com/nizos/tdd-guard) | `tdd-guard@tdd-guard` (alternative) | Predecessor of Probity; choose one |

These are **not** extra Ardizuo hook scripts. The five handlers stay as documented in the [hook catalog](./hooks/README.md).


<br />
<br />


## 🤖 4. Agent collections 22–25


| # | Collection | Source | Route |
| --- | --- | --- | --- |
| 22 | wshobson Agents | [wshobson/agents](https://github.com/wshobson/agents) | Reference; marketplace `claude-code-workflows` (94 plugins), install selectively |
| 23 | Everything Claude Code | [affaan-m/ECC](https://github.com/affaan-m/ECC) | Reference; selective manual import |
| 24 | gstack | [garrytan/gstack](https://github.com/garrytan/gstack) | Alternative orchestration; its setup edits `CLAUDE.md` |
| 25 | Compound Engineering | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | Alternative orchestration plugin |

Rows 22–25 are collections, not four agent definitions. The real agent count stays at 21.


<br />
<br />


## 📦 5. Extension systems 13–20


| # | Extension | Exact install ID | Type | License |
| --- | --- | --- | --- | --- |
| 13 | [OpenAI Codex Plugin](https://github.com/openai/codex-plugin-cc) | `codex@openai-codex` | Plugin, priority | Apache-2.0 |
| 14 | [Claude HUD](https://github.com/jarrodwatts/claude-hud) | `claude-hud@claude-hud` | Plugin, priority | MIT |
| 15 | [Trail of Bits](https://github.com/trailofbits/skills) | `<plugin>@trailofbits` | Marketplace of 44 plugins, install selected ones | CC-BY-SA-4.0 |
| 16 | [Matt Pocock Skills](https://github.com/mattpocock/skills) | `mattpocock-skills@mattpocock` | Plugin with 27 skills | MIT |
| 17 | [Daymade Skills](https://github.com/daymade/claude-code-skills) | `frontend-visual-qa@daymade-skills` | Marketplace of 61 plugins, install one | MIT |
| 18 | [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | `compound-engineering@compound-engineering-plugin` | Plugin, alternative | MIT |
| 19 | [Claude-Mem](https://github.com/thedotmack/claude-mem) | `claude-mem@thedotmack` | Plugin, alternative memory | Apache-2.0 |
| 20 | [gstack](https://github.com/garrytan/gstack) | Guided Git clone | Workflow suite, alternative | MIT |


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

Check the real slash menu after installing before you mark any of these active.


<br />
<br />


## 🛠️ 7. Developer tools and references


| # | Project | Route | Recommendation |
| --- | --- | --- | --- |
| 1 | [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | `npx @modelcontextprotocol/inspector` | Priority for MCP development; opens a localhost port |
| 2 | [Beads](https://github.com/gastownhall/beads) | `npm install -g @beads/bd` + `beads@beads-marketplace` | Project-only |
| 3 | [mcp-use](https://github.com/mcp-use/mcp-use) | `npx -y create-mcp-use-app@latest` | Project-only SDK |
| 4 | [Snyk Agent Scan](https://github.com/snyk/agent-scan) | `uvx snyk-agent-scan@latest` | Review privacy: it can send tool descriptions to Snyk |
| 5 | [AutoHarness](https://github.com/tigerless-labs/autoharness) | `autoharness@autoharness` (alternative) | Experimental; Windows unverified |
| 6 | [i-have-adhd](https://github.com/leondebeer/i-have-adhd) | `i-have-adhd@i-have-adhd` (alternative) | Optional response style |
| 7 | [Karpathy-inspired Skills](https://github.com/benfngu/karpathy-claude-skills) | Manual copy | Reference / overlap |
| 8 | [Everything Claude Code](https://github.com/affaan-m/ECC) | Reference | Reference / overlap |
| 9 | [wshobson Agents](https://github.com/wshobson/agents) | Reference | Reference / overlap |
| 10 | [GitHub Spec Kit](https://github.com/github/spec-kit) | `uv tool install specify-cli` | Alternative to the Contract stage |
| 11 | [Daymade Skills](https://github.com/daymade/claude-code-skills) | `frontend-visual-qa@daymade-skills` | Selected plugin only |
| 12 | [ccusage](https://github.com/ccusage/ccusage) | `npx ccusage@latest` | Optional; overlaps Claude Map |
| 13 | [Browserbase Stagehand](https://github.com/browserbase/stagehand) | `npm install @browserbasehq/stagehand` | Optional, per project |
| 14 | [ToolHive](https://github.com/stacklok/toolhive) | Publisher download | Only for many containerized MCPs |
| 15 | [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) | Reference | Reference |
| 16 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | Reference | Reference / SDK |
| 17 | mcp-use Inspector | Part of mcp-use | Not a separate package |
| 18 | [Trail of Bits static analysis](https://github.com/trailofbits/skills) | `static-analysis@trailofbits` | Needs CodeQL/Semgrep locally |
| 19 | [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) | Directory | Discovery only |
| 20 | [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code) | Directory | Discovery only |


<br />
<br />


## 🧭 8. Overlap groups: select, don't stack


| Capability | Existing option | Alternatives | Installer rule |
| --- | --- | --- | --- |
| Orchestration | SuperClaude + Superpowers + five-stage workflow | gstack, Compound Engineering, ECC | `orchestration` group: alternatives only |
| Code simplicity | `pragmatic-code-guidelines`, `clean-code-typescript` | Ponytail, Karpathy skills | Trial one at a time |
| Browser automation | Playwright plugin, Chrome DevTools MCP | Playwright MCP, Stagehand | `browser-automation` group: alternative |
| Web search and extraction | Tavily MCP | Exa, Firecrawl | Firecrawl for extraction only |
| Memory | Obsidian vault-learning | Claude-Mem, Beads | `memory` group: alternative |
| TDD enforcement | Test/quality skills and hooks | Probity, TDD Guard | `tdd-enforcement` group: one only |
| Usage reporting | Claude Map | Claude HUD, ccusage | Add only if needed |

Install it with the [optional extensions guide](../installation/extensions.md). [Component catalog](./README.md) · [Third-party notices](../../THIRD_PARTY_NOTICES.md)
