# 🔌 Tavily MCP

**Purpose:** Web research and search responses. **Transport on reference machine:** `stdio`.

**Status:** Reference-only; not installed, registered or authenticated by the Core bootstrap.

<br />

## 📥 1. Requirements

[Tavily — official source](https://docs.tavily.com/) · [API keys](../../docs/security/api-keys-and-powershell.md)

A Tavily account and API key may be required.

<br />

## 🔌 2. Register the server (after review)

**Installation:** This is a local `stdio` server. Its package name, launcher arguments, version and required environment vary by upstream implementation. Use [Tavily official documentation](https://docs.tavily.com/) for the exact command and review it before running. Avoid copying credentials or private launcher scripts from another computer.


**Safety:** Avoid logging searches that contain confidential source code or personal information.

<br />

## ☑️ 3. Authenticate and verify

```powershell
claude mcp list
```

Open Claude Code and use `/mcp` to complete provider sign-in and inspect status. A config entry is only **configured** until the server is actually connected. Grant only the needed access, ideally in a test environment.

<br />

## 🛠️ 4. Troubleshoot and remove

If startup fails, confirm the runtime, endpoint or launcher command, connectivity and permissions using the official source above. Don't paste tokens, full auth headers, raw `.claude.json`, or secret-containing MCP logs into a public issue.

If you no longer need this server, review the configuration first and use `claude mcp get tavily` to confirm the scope, then use `claude mcp remove tavily` only for the matching registration; verify with `claude mcp list`. Check your installed Claude CLI's help if the flags differ.

<br />

[All MCP servers](./README.md) · [API keys](../../docs/security/api-keys-and-powershell.md) · [Documentation hub](../../docs/README.md)

<br />

## 📥 Ardizuo one-package setup

**Installer:** Requires manual review and authentication; not automatically registered.

**Official source:** https://docs.tavily.com/documentation/mcp

**Notes:** Requires Tavily key; follow provider guide and avoid storing a literal token in CLI history.

Never paste real keys into your issue, commit, README, or chat. Run `claude mcp list` and `/mcp` after registration; presence is not authentication.


---

## 📥 Current all-layer installer behavior

- **Manifest name:** `tavily`
- **Transport:** `stdio`
- **CLI registration:** Requires manual provider credential setup; this package does not guess keys
- **Prerequisites:** `npx`
- **Official documentation:** https://docs.tavily.com/documentation/mcp

This server's settings are scoped to the **installer user's account**. Existing registrations are not overwritten. The installer tracks the result of a public registration command, but cannot complete an OAuth browser flow or guarantee the server is connected.

```powershell
# Preview just the third-party MCP registration portion.
.\scripts\install-all.ps1 -Mcps -External

# Review and explicitly approve only when ready.
.\scripts\install-all.ps1 -Apply -Mcps -External

# Inspect locally after registration; avoid pasting credentials in issues.
claude mcp list
```

For verification, enter Claude Code and open `/mcp`. The desired lifecycle is **registered → connected/authenticated → successful permitted tool call**. The final two states require a real provider session. Do not treat `claude mcp list` or the Ardizuo dashboard as proof of a live successful call.
