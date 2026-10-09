# Ardizuo developer plugin

**Planned plugin — not ready to install as a complete agent/skill distribution.** The existing `.claude-plugin/plugin.json` is metadata scaffolding only.

<br />

## What will be included

Reviewed original specialist agents, manual skills, commands and Node lifecycle hooks. Original files must be stripped of local usernames, secrets and implicit write operations before reuse.

<br />

## How users will install it (after release)

The [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins) describes how to package plugins. Exact marketplace registration and installation commands will be published after the plugin files and version are validated; no working marketplace distribution is claimed today.

<br />

## Maintainer checks

- Keep plugin-owned assets separate from Claude Code's global cache.
- Test discoverability with `/skills` and reviewed hook lifecycle tests.
- Confirm user-level installations do not overwrite personal settings.
- Provide release versions, changelog, rollback and user approval for write operations.

<br />

[Component catalog](../docs/components/README.md) · [Developer architecture](../docs/architecture.md) · [Docs hub](../docs/README.md)
