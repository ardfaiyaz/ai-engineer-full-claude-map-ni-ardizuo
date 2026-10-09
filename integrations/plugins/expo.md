# Expo plugin

**Purpose:** React Native / Expo development, builds and releases.

**Status:** Enabled in the author's reference environment; **not automatically installed by the public Core bootstrap**.

<br />

## 1. Requirements and official source

[Expo — official reference](https://docs.expo.dev/) · [Node and npm](../../docs/installation/nodejs-npm.md)

An Expo account and project access may be needed for cloud build/deployment; start with nonproduction projects.

<br />

## 2. Install (optional)

Review the [official Claude Code plugin documentation](https://code.claude.com/docs/en/discover-plugins) and the marketplace catalog first. In a terminal with Claude Code available, you can use:

```powershell
claude plugin install expo@claude-plugins-official
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
