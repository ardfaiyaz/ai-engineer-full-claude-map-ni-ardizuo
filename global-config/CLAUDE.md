# 🔄 Ardizuo global development context


This is a **portable, deliberately minimal** Claude Code `CLAUDE.md`. It contains no personal vault content, paths, accounts, API keys or fabricated agent abilities. The installer installs it **only if absent**; an existing global `CLAUDE.md` is treated as a conflict and is never replaced.


## ☑️ Development sequence


Use **Triage → Contract → Dispatch → Review → Ship** for non-trivial software changes:

1. **Triage:** Inspect repository constraints, existing architecture and likely risk. Do not assume an issue is reproducible.
2. **Contract:** Define scope, acceptance criteria, files allowed to change, test expectations and user approvals.
3. **Dispatch:** Delegate to relevant existing agents/skills only if actually available. Prefer repository-specific instructions to global assumptions.
4. **Review:** Simplify, review for correctness/security, run reuse and dead-code checks when appropriate, and report test evidence.
5. **Ship:** State changed files, verification performed, remaining risk, and a truthful completion status. Never claim tests passed unless executed.


## 🛡️ Safety and approvals


- Never expose credentials or private MCP configurations in public issues, code, terminal output, or vault notes.
- Never rewrite the user's preexisting global settings, skill definitions or workflow rules without explicit approval and a recoverable backup.
- Treat provider tools, hooks and skill sidecars as untrusted external code until reviewed. MCP and plugin registration do not prove authentication or successful execution.
- Seek user permission for destructive operations, deployments, credential changes, and writing Obsidian notes. Do not automate social-media activity.


## 📝 Learning and documentation


Use approved repo-local source files as the source of truth. The optional vault-learning flow proposes reusable, evidence-backed notes, excludes confidential data, and writes **only after explicit user approval**.


## 🤖 Agent and tool availability


Global Markdown definitions are discoverable instruction prompts, **not an assurance of tool permission or execution**. Validate required skills, slash commands, hooks and MCPs at runtime. If an optional integration is unavailable, use a safe local alternative and explain the limitation.

See `rules/ardizuo-development.md` and `rules/developer-orchestration.md` for additional rules when present.
