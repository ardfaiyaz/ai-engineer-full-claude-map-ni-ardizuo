# Full release checklist

The **assisted Full preview** includes original assets and external installation orchestration. It is not yet a verified stable release; these gates must pass first.

<br />

## Source and licensing

- [x] Add MIT license for original Ardizuo-owned files (external packages retain upstream licensing).
- [ ] Attribute upstream Claude Map, plugins and other authors appropriately.
- [ ] Review and license-check 21 agent definitions.
- [ ] Review all original skills, five hooks and global rules for secrets, paths and side effects.

<br />

## Installer and guides

- [x] Package the 28 reviewed original assets with hash checks and collision-safe installation.
- [ ] Make Full, Frontend, Backend, Mobile and Custom profiles genuinely installable or explicitly mark incomplete.
- [x] Provide individual official-linked dependency and [installation guides](./installation/README.md).
- [ ] Verify all [plugin](../integrations/plugins/README.md) and [MCP](../integrations/mcp/README.md) registrations and auth flows.
- [ ] Verify an attributed, version-pinned Claude Map overlay against a clean upstream Windows install (patch sources are included but version-sensitive).
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
