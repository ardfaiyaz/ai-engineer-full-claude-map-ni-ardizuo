# <img src="assets/lucide/workflow.svg" width="18" height="18" alt="" /> Developer orchestration architecture

The system has **five development stages**. The dashboard is a map of *capabilities*; a passing end-to-end run needs separate evidence.

<br />

## <img src="assets/lucide/workflow.svg" width="18" height="18" alt="" /> Workflow Surface

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

## <img src="assets/lucide/file-text.svg" width="18" height="18" alt="" /> Completion mandate

`simplify` · `code-review` · `reuse-audit` · `dead-code-scan` · `vault-learning`

A checkbox must reflect **what actually ran**, not simply whether a name is installed or built in. Delegation is optional on very small tasks; **do not fabricate agent calls**.

<br />

## <img src="assets/lucide/layers.svg" width="18" height="18" alt="" /> System layers

| Layer | Responsibilities | Current public status |
| :--- | :--- | :--- |
| Agents | Specialist definitions and scope controls | Original files still awaiting review |
| Skills | Superpowers, SuperClaude, custom skills and PRD | Official plugins + authored assets pending |
| Hooks | Session lifecycle and skill checks | Five source files pending audit |
| Config | Rules, workflow JSON/Markdown | One namespaced rule installed by bootstrap |
| Memory | Optional Obsidian vault templates | Safe templates bundled; private notes excluded |
| MCP & plugins | Provider-backed tools and services | Reference guides; auth performed by user |
| Dashboard | Local Claude Map architecture view | Version-pinned, attributed package pending |

<br />

## <img src="assets/lucide/file-text.svg" width="18" height="18" alt="" /> Verification plan

- Agent delegation: inspect actual delegated-task invocation and outcome.
- Skills: check the tool invoked, not just folder names or plugin enablement.
- Hooks: test event behavior with reviewed sample payloads.
- MCPs: distinguish configured, connected, authorized and executed.
- Memory: approve a note, save it, then verify reload in a fresh session.
- Ship: provide genuine lint, test, build, Git, documentation and rollback evidence.

<br />

[Component catalog](./components/README.md) · [Release gates](./release-checklist.md) · [Back to README](../README.md)
