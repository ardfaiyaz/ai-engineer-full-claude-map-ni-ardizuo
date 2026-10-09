# 🖥️ Development Hub surface — exactly the observed capabilities

The local Claude Map page `http://localhost:8888/?tab=devhub` is a **read-only capability inventory**. Its five-stage workflow and component badges classify existing, built-in, and equivalent capabilities differently. This guide documents only elements observed on the owner's working Claude Map—**it does not create or install new Claude skills**.

## 🔄 Five-stage workflow surface

| Stage | Existing workflow purpose | What the operator should verify |
|---|---|---|
| **01 Triage** | Understand task, examine context, find reusable solutions | Real repository inspection; Superpowers brainstorming, `sc:research`, and Ralph PRD availability where needed |
| **02 Contract** | Agree on permitted scope, expected results and task constraints | Written acceptance criteria and approval before writes |
| **03 Dispatch** | Use the agent/skill most suited to the agreed change | Actual delegated task evidence; never infer delegation from `agents/*.md` |
| **04 Review** | Validate implementation with tests, code review, simplify/reuse/dead-code checks | Real test outputs, file diffs, and review comments |
| **05 Ship** | Summarize changed files, remaining limitations and approved learnings | Explicit acceptance, Git review, and vault note only after permission |

The **Completion Mandate** includes native `simplify` and `code-review`, together with local `reuse-audit`, `dead-code-scan`, and `vault-learning`. Native Claude Code commands are **not** redistributed as `SKILL.md` files.

## 🗂️ What the eight skill groups actually mean

These dashboard names reflect the original interface's display, not additional install requirements.

| Dashboard group | Existing capabilities shown | Correct source or verification |
|---|---|---|
| **Orchestration (5)** | team-driven-development, dispatching-parallel-agents, writing-plans, executing-plans, sc:workflow | Local source, Superpowers plugin, or an existing SuperClaude command as individually indicated |
| **Quality (8)** | simplify, code-review, clean-code-typescript, karpathy-guidelines, code-splitting, gauge-improvements, security-review, verification-before-completion | Some are built-ins or already present via plugins; `karpathy-guidelines` is a related existing local capability, **not** a new component to install |
| **Development (5)** | test-driven-development, using-git-worktrees, finishing-a-development-branch, receiving-code-review, fix-build | Existing Superpowers/plugin skills and local fix-build |
| **Debugging (3)** | systematic-debugging, test-fixing, root-cause-analysis | Plugin or bundled Ardizuo skills |
| **Discovery (4)** | superpowers:brainstorming, sc:brainstorm, ralph-skills:prd, sc:research | Existing installed plugin and SuperClaude commands |
| **Design (4)** | frontend-design, ui-ux-pro-max, web-design-guidelines, figma:figma-use | Existing skills and Figma MCP functionality; a related MCP is not the same thing as a local SKILL.md |
| **Writing (4)** | humanizer, elements-of-style, sc:document, claude-md-management | Local skills, plugin content, and upstream command as discovered |
| **Integrations (9)** | vercel:nextjs, vercel:ai-sdk, vercel:deploy, react-native-best-practices, expo:deployment, stripe:best-practices, sentry:sentry-workflow, atlassian:triage-issue, Notion:search | Existing MCP or provider plugin capabilities; **not** nine additional direct skill files |
| **Operations (3)** | sc:pm, ship-learn-next, claude-api | Upstream SuperClaude, local skill, and an existing capability label |

The hub may display **178 discovered skill entries** while the direct user directory contains **62 `SKILL.md` files**. Cache duplicates, plugin versions and built-in or equivalent capabilities explain why these are different measures. Never promise to create 178 independent packages.

## 🤖 Agent and command layers

The observed 21 agent definitions are **one Ardizuo-authored diagram agent plus 20 publisher-pinned SuperClaude definitions**. The public installer covers all 21 names. The reference machine has **31 executable command definitions**—one Ardizuo command plus 30 SuperClaude commands—and one SuperClaude `README.md` among its 32 Markdown files. Eleven SuperClaude source files differ from the working machine's local copies; upstream alternatives are available only with explicit opt-in.

Use [the by-name matrix](../installation/reproducibility-matrix.md) for the complete agent, skill and command inventory.

## 🔌 MCP and plugin layers

The public installer records **exactly nine target user-scope MCP server names** and **exactly 12 plugin IDs**. The reference machine reports all nine user MCPs connected and twelve plugins enabled. Additional provider MCP entries may be installed by plugins or attached to the account, and should not be counted as new Ardizuo-provided global servers. Atlassian plugin MCP sign-in may remain an explicitly deferred optional connection.

**The GitHub MCP difference matters:** the reference machine uses an existing personal PowerShell launcher. The public setup deliberately documents an official Docker/OAuth-based alternative rather than copying a possibly personal launcher file. This preserves functionality but does **not** prove an identical launcher or OAuth state on another machine.

## ⚙️ Hooks, global configuration and rules

The dashboard sees five hook script filenames mapped to four lifecycle event types: `UserPromptSubmit`, `SessionStart`, two `PostToolUse` handlers, and `Stop`. The package contains all five scripts plus their shared helper; **`-Hooks` is required to register them**, and registration alone is not execution evidence.

The global config layer detects `CLAUDE.md`, `skill-gates.json`, personas, commands, `wave-protocol.md`, `completion-mandate.md`, and `developer-orchestration.md`. The repository has reviewed bundled rules, gates, commands, workflow Markdown, and a **portable** global `CLAUDE.md` template. The owner's exact global `CLAUDE.md`, persona contents, and seven locally different customized files have **not been approved or included as byte-identical public copies**. Do not fabricate a persona file just to turn a badge green.

## 📝 Obsidian memory and dashboard

The original vault surface includes Sessions, Learnings, ADRs, Dispatch-Logs, PRDs, Diagrams, Projects and Templates. Optional setup creates these eight folders, four template files, and icon assets. It does not export personal notes. The dashboard's five-stage overlay passed a sandbox rehearsal against Claude Map 1.2.3, and the owner confirmed that the live browser view loads; a clean-device browser walkthrough is still a release gate.

## 🛡️ Why the public package stops at confirmed sources

The remaining **17 externally sourced direct skill files, four unknown-source direct skills, five different skill variants, and eleven different command variants** cannot be represented as exact copies without owner-provided review and redistribution authority. The correct follow-up is to inspect their sources and supporting files, not create replacement skills absent from the original Claude setup. See [source review](../installation/private-source-migration.md), [release coverage](../installation/reproducibility-matrix.md), and [installed-layer verification](../installation/installed-layer-audit.md).
