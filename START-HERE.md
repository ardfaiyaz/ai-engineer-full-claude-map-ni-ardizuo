# Start here — AI Engineer Full Claude Map ni Ardizuo

**Single ZIP package. Windows-first. No hosted website.**

<br />

## For someone installing it

Read the main [README](./README.md). Install the required [prerequisites](./docs/prerequisites.md), then open PowerShell inside the repository:

```powershell
# Preview everything without changes
.\scripts\install-all.ps1 -All

# After reading the plan and giving explicit approval
.\scripts\install-all.ps1 -Apply -All
```

Plugin marketplace availability, provider authentication, dashboard compatibility and MCP credentials require attention. Open the [Full setup walkthrough](./docs/installation/full-setup.md), then the [30-step verification checklist](./docs/installation/verification-checklist.md).

<br />

## For the repository maintainer

1. Commit any existing local changes before applying this ZIP. Do not extract over unexpected uncommitted edits.
2. Extract all contents to the root of `ai-engineer-full-claude-map-ni-ardizuo` (it overwrites earlier documentation and installation scripts). This is a **repository source update**, not an executable installer by itself.
3. Run `python -m unittest discover -s tests -v` and `git diff --check`.
4. Run an isolated test: `scripts/install-all.ps1 -ConfigDir "$HOME\Documents\Ardizuo-Test-Config"` (dry run), then add `-Apply` if safe. Do **not** use `-All` with isolated config for external CLI installers.
5. Review all source/credential/third-party licensing changes and commit/push only your approved files. No secrets or private vault notes are included.

<br />

## What is included and not guaranteed

This archive contains original reviewed skills, hooks, a custom agent, rules, manifests, source dashboard patches, separate plugin/MCP installation guides and all generated documentation. Official third-party binaries and private credentials are **not** embedded. The end-to-end Full workflow still needs a clean Windows installation and provider-specific login tests before claiming a stable release.

[Project README](./README.md) · [Security](./SECURITY.md) · [Release checklist](./docs/release-checklist.md)
