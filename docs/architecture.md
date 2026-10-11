# 🔄 Developer orchestration architecture


The system has **five development stages**. The dashboard is a map of *capabilities*; a passing end-to-end run needs separate evidence.


<br />
<br />


## 🔄 Workflow Surface


```text
Triage  ->  Contract  ->  Dispatch  ->  Review  ->  Ship
```

| Stage | Responsibility | Example evidence |
| :--- | :--- | :--- |
| **Triage** | Understand requests and existing code | Requirements and reuse notes |
| **Contract** | Define scope, acceptance criteria and file ownership | Task plan and boundaries |
| **Dispatch** | Delegate where it improves the outcome | Actual agent invocation log |
| **Review** | Review tests, quality and security | Test outputs and review findings |
| **Ship** | Verify readiness and document handoff | Builds, Git review, rollback plan and notes |


<br />
<br />


## 📄 Completion mandate


`simplify` · `code-review` · `reuse-audit` · `dead-code-scan` · `vault-learning` · `version-log`

A checkbox must reflect **what actually ran**, not simply whether a name is installed or built in. Delegation is optional on very small tasks; **do not fabricate agent calls**.


<br />
<br />


## 🗂️ System layers


| Layer | Responsibilities | Current public status |
| :--- | :--- | :--- |
| Agents | Specialist definitions and scope controls | 21/21: `diagram-architect` bundled + 20 pinned SuperClaude agents |
| Skills | Ardizuo, publisher-pinned and plugin-provided skills | 36/62 reference skills by default (41/62 with opt-in variants), plus `version-log` and the extended-stack plugins |
| Commands | Slash commands | 20/31 by default, 31/31 with opt-in SuperClaude variants |
| Hooks | Session lifecycle, skill gates, vault logging, dead-code checks | Five handlers bundled; registered with `-Hooks` |
| Config | Portable `CLAUDE.md`, rules, `skill-gates.json`, workflow Markdown | Bundled and installed create-only |
| Memory | Optional Obsidian vault folders and templates | Eight folders + four templates with `-Vault`; private notes excluded |
| MCP & plugins | Provider-backed tools and services | 12 plugins and nine MCPs with supported install commands; sign-in is per user |
| Extended stack | Researched tools from other publishers | 74 catalog rows / 40 packages, installed by `-All` |
| Dashboard | Local Claude Map architecture view | Five-stage overlay for `claude-map@1.2.3`; separate rehearsal before applying |


<br />
<br />


## 🧩 Where the extended stack fits


All of these are installed. Each row shows which tools strengthen a stage and what they overlap with, so you know which one to reach for.

| Stage | Baseline already provides | Extended stack | Overlap to watch |
| :--- | :--- | :--- | :--- |
| **Triage** | Superpowers brainstorming, `sc:research`, Tavily | Matt Pocock `grill-me`, `grill-with-docs`, `domain-modeling`; Firecrawl or Exa for research | Exa overlaps Tavily |
| **Contract** | Ralph PRD, `sc:workflow` | Matt Pocock `to-spec`, `to-tickets`; GitHub Spec Kit; Beads for task dependencies | Spec Kit is a full alternative Contract flow |
| **Dispatch** | 21 agents, `team-driven-development` | Codex `/codex:rescue`; Compound Engineering, gstack, ECC, wshobson agents | Each suite has its own end-to-end workflow |
| **Review** | `code-review`, `simplify`, `reuse-audit`, `dead-code-scan` | Codex `/codex:review`, Trail of Bits `differential-review`, `mutation-testing`, `property-based-testing`, `frontend-visual-qa`, Ponytail | Ponytail overlaps `pragmatic-code-guidelines` |
| **Ship** | `ship-learn-next`, `vault-learning`, `version-log`, Claude Map | Claude HUD, ccusage, Snyk Agent Scan, Matt Pocock `handoff` | Claude-Mem overlaps the vault |

Test-first enforcement (Probity and TDD Guard, both installed) cuts across Contract and Review. If they block the same edit, disable one, and compare their hooks with the five Ardizuo hooks. Details: [master extension catalog](./components/extension-catalog.md).


<br />
<br />


## 📄 Verification plan


- Agent delegation: inspect actual delegated-task invocation and outcome.
- Skills: check the tool invoked, not just folder names or plugin enablement.
- Hooks: test event behavior with reviewed sample payloads.
- MCPs: distinguish configured, connected, authorized and executed.
- Extensions: `python scripts/install-extensions.py --status` shows enabled or registered names only; run one real command per extension before calling it working.
- Memory: approve a note, save it, then verify reload in a fresh session.
- Ship: provide genuine lint, test, build, Git, documentation and rollback evidence.


[Component catalog](./components/README.md) · [Release gates](./release-checklist.md) · [Back to README](../README.md)
