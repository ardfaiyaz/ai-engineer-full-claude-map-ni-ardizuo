# Supabase MCP

**Purpose:** Database/project integration. **Transport on reference machine:** `http`.

**Status:** Reference-only; not installed, registered or authenticated by the Core bootstrap.

<br />

## 1. Requirements

[Supabase — official source](https://supabase.com/docs) · [API keys](../../docs/security/api-keys-and-powershell.md)

Project access and provider authentication may be required.

<br />

## 2. Register the server (after review)

**Reference endpoint used by the author:** `https://mcp.supabase.com/mcp?read_only=true`. Check the provider documentation for the current endpoint, then, if approved, register it as a **user-scoped HTTP MCP**:

```powershell
claude mcp add --scope user --transport http supabase https://mcp.supabase.com/mcp?read_only=true
```


**Safety:** Prefer read-only settings when inspecting production data. The original author used a read-only connection.

<br />

## 3. Authenticate and verify

```powershell
claude mcp list
```

Open Claude Code and use `/mcp` to complete provider sign-in and inspect status. A config entry is only **configured** until the server is actually connected. Grant only the needed access, ideally in a test environment.

<br />

## 4. Troubleshoot and remove

If startup fails, confirm the runtime, endpoint or launcher command, connectivity and permissions using the official source above. Don't paste tokens, full auth headers, raw `.claude.json`, or secret-containing MCP logs into a public issue.

If you no longer need this server, review the configuration first and use `claude mcp get supabase` to confirm the scope, then use `claude mcp remove supabase` only for the matching registration; verify with `claude mcp list`. Check your installed Claude CLI's help if the flags differ.

<br />

[All MCP servers](./README.md) · [API keys](../../docs/security/api-keys-and-powershell.md) · [Documentation hub](../../docs/README.md)

<br />

## Ardizuo one-package setup

**Installer:** Supported automatic registration after explicit `-Apply -External -Mcps`.

Run the orchestrator to register it. The underlying command is shown below for reference:

```powershell
claude mcp add --transport http --scope user supabase https://mcp.supabase.com/mcp?read_only=true
```

**Official source:** https://supabase.com/docs/guides/getting-started/mcp

**Notes:** OAuth needed; read-only flag is default in this pack.

Never paste real keys into your issue, commit, README, or chat. Run `claude mcp list` and `/mcp` after registration; presence is not authentication.
