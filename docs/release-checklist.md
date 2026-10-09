# Full release checklist

A **public bootstrap preview** is already available. It becomes a full installable release only after every required check passes.

<br />

## Source and licensing

- [ ] Choose a LICENSE covering original content only.
- [ ] Attribute upstream Claude Map, plugins and other authors appropriately.
- [ ] Review and license-check 21 agent definitions.
- [ ] Review all original skills, five hooks and global rules for secrets, paths and side effects.

<br />

## Installer and guides

- [ ] Package approved assets with idempotent installation and collision handling.
- [ ] Make Full, Frontend, Backend, Mobile and Custom profiles genuinely installable or explicitly mark incomplete.
- [ ] Provide verified dependency and [installation guides](./installation/README.md).
- [ ] Verify all [plugin](../integrations/plugins/README.md) and [MCP](../integrations/mcp/README.md) registrations and auth flows.
- [ ] Bundle an attributed, version-pinned local dashboard patch with tests.
- [ ] Make rollback and uninstall work without modifying unrelated user settings.

<br />

## Runtime and security

- [ ] Test explicit agent delegation and truthful reporting of no delegation.
- [ ] Verify real completion mandate, tests, builds, Git review and Ship evidence.
- [ ] Test approved Obsidian note write and retrieval in a new session.
- [ ] Run a clean Windows install, repeat installation and rollback.
- [ ] Scan tracked files, Git history, sample environment files and CI logs for private data.
- [ ] Tag a stable release only after the package meets its stated scope.

<br />

[Maintainer notes](./maintainer-next-steps.md) · [Security](../SECURITY.md) · [README](../README.md)
