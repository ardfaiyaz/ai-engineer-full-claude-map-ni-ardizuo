# Maintainer roadmap

**Goal:** Package a safe, reproducible Windows-first global Claude Code development configuration. No hosted site and no social-media features.

<br />

## Next three development milestones

### 1. Audit original source assets

- Collect **only the files Ardizuo authored or has redistribution rights to**.
- Review the 21 agents, five hooks, custom skills and workflow rules for secrets, personal paths and side effects.
- Do not export the whole `.claude` folder or plugin cache.

### 2. Implement the Full profile

- Add idempotent installation for audited assets with a dry run, collision handling and rollback.
- Register third-party components from official sources **with explicit user consent**.
- Support Core, Full and specialized profiles only when tested, not just defined in JSON.

### 3. Verify and release

- Test on a clean Windows user profile.
- Confirm plugin discovery, MCP sign-in, delegation, vault save/reload and Ship evidence.
- Audit Git history and CI output for private values; add LICENSE and notices.

<br />

[Release checklist](./release-checklist.md) · [Security](../SECURITY.md) · [Architecture](./architecture.md)
