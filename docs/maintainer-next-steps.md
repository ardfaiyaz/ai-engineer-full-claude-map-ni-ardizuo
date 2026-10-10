# 📄 Maintainer roadmap


**Goal:** Package a safe, reproducible Windows-first global Claude Code development configuration. No hosted site and no social-media features.


<br />
<br />


## 📄 Next three development milestones


<br />


### 🔄 1. Complete ownership and portability review


- Collect **only the files Ardizuo authored or has redistribution rights to**.
- Review the 21 agents, five hooks, custom skills and workflow rules for secrets, personal paths and side effects.
- Do not export the whole `.claude` folder or plugin cache.


<br />


### ⚙️ 2. Complete the assisted Full profile and optional presets


- The 28 original assets already support dry-run, idempotence and collision checks; now finish lifecycle rollback, verified Windows tests and optional uninstall.
- The Full orchestrator can attempt upstream installs with explicit user consent; verify actual provider login, marketplace availability, and pin tested versions.
- Support Core, Full and specialized profiles only when tested, not just defined in JSON.


<br />


### ☑️ 3. Verify and release


- Test on a clean Windows user profile.
- Confirm plugin discovery, MCP sign-in, delegation, vault save/reload and Ship evidence.
- Audit Git history and CI output for private values; add LICENSE and notices.


[Release checklist](./release-checklist.md) · [Security](../SECURITY.md) · [Architecture](./architecture.md)
