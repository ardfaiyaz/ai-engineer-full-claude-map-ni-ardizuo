# <img src="docs/assets/lucide/monitor.svg" width="18" height="18" alt="" /> Start here — AI Engineer Full Claude Map ni Ardizuo

**Single ZIP package. Windows-first. No hosted website.**

<br />

## <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> For someone installing it

Read the main [README](./README.md). Install the required [prerequisites](./docs/prerequisites.md), then open PowerShell inside the repository:

```powershell
# Preview everything without changes
.\scripts\install-all.ps1 -All

# After reading the plan and giving explicit approval
.\scripts\install-all.ps1 -Apply -All
```

Plugin marketplace availability, provider authentication, dashboard compatibility and MCP credentials require attention. Open the [Full setup walkthrough](./docs/installation/full-setup.md), then the [30-step verification checklist](./docs/installation/verification-checklist.md).

<br />

## <img src="docs/assets/lucide/file-text.svg" width="18" height="18" alt="" /> For the repository maintainer

1. Commit any existing local changes before applying this ZIP. Do not extract over unexpected uncommitted edits.
2. Extract all contents to the root of `ai-engineer-full-claude-map-ni-ardizuo` (it overwrites earlier documentation and installation scripts). This is a **repository source update**, not an executable installer by itself.
3. Run `python -m unittest discover -s tests -v` and `git diff --check`.
4. Run an isolated test: `scripts/install-all.ps1 -ConfigDir "$HOME\Documents\Ardizuo-Test-Config"` (dry run), then add `-Apply` if safe. Do **not** use `-All` with isolated config for external CLI installers.
5. Review all source/credential/third-party licensing changes and commit/push only your approved files. No secrets or private vault notes are included.

<br />

## <img src="docs/assets/lucide/book-open.svg" width="18" height="18" alt="" /> What is included and not guaranteed

This archive contains original reviewed skills, hooks, a custom agent, rules, manifests, source dashboard patches, separate plugin/MCP installation guides and all generated documentation. Official third-party binaries and private credentials are **not** embedded. The end-to-end Full workflow still needs a clean Windows installation and provider-specific login tests before claiming a stable release.

[Project README](./README.md) · [Security](./SECURITY.md) · [Release checklist](./docs/release-checklist.md)


## <img src="docs/assets/lucide/package.svg" width="18" height="18" alt="" /> Maintainer: complete the exact Development Hub inventory

```powershell
python .\scripts\coverage-doctor.py
python .\scripts\coverage-doctor.py --json

# Preview which additional direct-scope files exist on your OWN machine.
# Review ownership and secrets before sharing any contents.
python .\scripts\prepare-private-review.py
```

See [exact coverage](./docs/components/exact-coverage.md) and [private source migration](./docs/installation/private-source-migration.md). The package does not invent files for skills that exist only as a reference name, nor can it migrate another user's provider credentials.


## <img src="docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> What the public installer really reproduces

The reference machine has **21 agent files, 62 direct skill definitions, 31 executable command files plus one `README.md`, 12 enabled plugins and nine target user MCP servers**. The public installer does **not yet** exactly reproduce all of those on a fresh account. See the [release coverage matrix](docs/installation/reproducibility-matrix.md) for default, optional, provider-authenticated, and blocked items. Never publish personal provider configuration or private vault content.


## <img src="docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Inspect a real install without touching it

Use the [read-only installed-layer verification](./docs/installation/installed-layer-audit.md) to check which expected files, hook registrations, and vault templates actually landed in your chosen Claude configuration. It does not claim that provider authentication or skill execution succeeded.
