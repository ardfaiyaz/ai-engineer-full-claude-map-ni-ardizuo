# GitHub MCP MCP

**Purpose:** Repository, pull-request and issue workflows. **Transport on reference machine:** `stdio`.

**Status:** Reference-only; not installed, registered or authenticated by the Core bootstrap.

<br />

## 1. Requirements

[GitHub MCP — official source](https://github.com/github/github-mcp-server) · [GitHub CLI](../../docs/installation/github-cli.md) · [Docker](../../docs/installation/docker.md)

GitHub CLI OAuth and (for some setups) Docker are used.

<br />

## 2. Register the server (after review)

**Installation:** This is a local `stdio` server. Its package name, launcher arguments, version and required environment vary by upstream implementation. Use [GitHub MCP official documentation](https://github.com/github/github-mcp-server) for the exact command and review it before running. Avoid copying credentials or private launcher scripts from another computer.


**Safety:** Prefer read-only mode for exploration. Avoid printing `gh auth token` or putting PATs in command history.

<br />

## 3. Authenticate and verify

```powershell
claude mcp list
```

Open Claude Code and use `/mcp` to complete provider sign-in and inspect status. A config entry is only **configured** until the server is actually connected. Grant only the needed access, ideally in a test environment.

<br />

## 4. Troubleshoot and remove

If startup fails, confirm the runtime, endpoint or launcher command, connectivity and permissions using the official source above. Don't paste tokens, full auth headers, raw `.claude.json`, or secret-containing MCP logs into a public issue.

If you no longer need this server, review the configuration first and use `claude mcp get github` to confirm the scope, then use `claude mcp remove github` only for the matching registration; verify with `claude mcp list`. Check your installed Claude CLI's help if the flags differ.

<br />

[All MCP servers](./README.md) · [API keys](../../docs/security/api-keys-and-powershell.md) · [Documentation hub](../../docs/README.md)

<br />

## Ardizuo one-package setup

**Installer:** Requires manual review and authentication; not automatically registered.

**Official source:** https://github.com/github/github-mcp-server

**Notes:** Original setup used gh+Docker wrapper. Obtain official read-only setup; never embed gh token in public configuration.

Never paste real keys into your issue, commit, README, or chat. Run `claude mcp list` and `/mcp` after registration; presence is not authentication.
