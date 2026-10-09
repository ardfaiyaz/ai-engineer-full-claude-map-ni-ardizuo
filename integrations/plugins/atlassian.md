# Atlassian plugin

**Purpose:** Jira issue triage and developer project management.

**Status:** Enabled in the author's reference environment; **not automatically installed by the public Core bootstrap**.

<br />

## 1. Requirements and official source

[Atlassian — official reference](https://support.atlassian.com/) · [API key guide](../../docs/security/api-keys-and-powershell.md)

Sign in to the intended Jira/Atlassian workspace; prefer least-privileged issue permissions.

<br />

## 2. Install (optional)

Review the [official Claude Code plugin documentation](https://code.claude.com/docs/en/discover-plugins) and the marketplace catalog first. In a terminal with Claude Code available, you can use:

```powershell
claude plugin install atlassian@claude-plugins-official
```

If the marketplace isn't registered, use Claude Code's `/plugin` marketplace UI to find the **official maintained source** and add it after review. A missing or renamed listing is not permission to download an unrelated plugin of the same name.

<br />

## 3. Sign in and verify

```powershell
claude plugin list
claude mcp list
```

In Claude Code, open `/skills` to inspect the actual available skills and `/mcp` for plugin-provided connections that need authentication.

**Important:** The video label for a skill may differ from the name that this provider actually installs. An installed plugin does not prove any specific task ran.

<br />

## 4. Troubleshooting and removal

If the plugin doesn't appear, reload plugins inside Claude Code with `/reload-plugins`, reopen the session, and confirm you used the right marketplace. Review provider account scopes and permissions before connecting.

Use Claude Code's `/plugin` manager or the supported plugin uninstall command to remove it; do not manually delete other plugins' caches.

<br />

[All plugins](./README.md) · [Secrets and authentication](../../docs/security/api-keys-and-powershell.md) · [Documentation hub](../../docs/README.md)

<br />

## One-package option

From the repository root, use `scripts/install-all.ps1 -Apply -External -Plugins` after reviewing the dry run. This invokes the CLI install for this plugin; it registers upstream marketplaces first where possible, but does not grant account permissions or guarantee successful provider authentication. For failures, use the manual installer and official source above.


---

## Marketplace source and repeatable installation

**Capability:** Jira/Confluence issue workflows.

**Upstream marketplace:** [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) — expected catalog ID `claude-plugins-official`. Source code and provider agreements remain third-party. Review the marketplace before proceeding.

```powershell
# Preview every optional external action without downloading anything.
.\scripts\install-all.ps1 -All

# To install only supported plugins from their declared marketplaces:
.\scripts\install-all.ps1 -Apply -External -Plugins

# This plugin's manual equivalent (run from any directory after marketplace setup):
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install atlassian@claude-plugins-official
```

If the marketplace already exists, do not remove it; the script attempts to detect registrations before adding them. CLI return code zero does **not** verify plugin runtime state. In Claude Code open `/plugin` and `/skills`, and use `claude plugin list` to distinguish installed versus enabled. Provider-specific OAuth/API key steps are performed by each installer user and must be checked in `/mcp` when applicable.

**Practical safety check:** Scopes may include confidential tickets. Confirm the exact Atlassian workspace before enabling write actions.

**Rollback:** Use Claude Code's plugin manager for this exact `plugin@marketplace` identity. Removing a marketplace may affect other plugins; never delete unrelated caches or sessions.
