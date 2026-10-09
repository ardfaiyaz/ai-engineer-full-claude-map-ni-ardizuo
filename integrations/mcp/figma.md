# 🔌 Figma MCP

**Purpose:** Design files, components and handoff context. **Transport on reference machine:** `http`.

**Status:** Reference-only; not installed, registered or authenticated by the Core bootstrap.

<br />

## 📥 1. Requirements

[Figma — official source](https://developers.figma.com/) · [API keys](../../docs/security/api-keys-and-powershell.md)

Connect only the design workspace/files you need, normally via provider sign-in.

<br />

## 🔌 2. Register the server (after review)

**Reference endpoint used by the author:** `https://mcp.figma.com/mcp`. Check the provider documentation for the current endpoint, then, if approved, register it as a **user-scoped HTTP MCP**:

```powershell
claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp
```


**Safety:** Use read-only design permissions where practical.

<br />

## ☑️ 3. Authenticate and verify

```powershell
claude mcp list
```

Open Claude Code and use `/mcp` to complete provider sign-in and inspect status. A config entry is only **configured** until the server is actually connected. Grant only the needed access, ideally in a test environment.

<br />

## 🛠️ 4. Troubleshoot and remove

If startup fails, confirm the runtime, endpoint or launcher command, connectivity and permissions using the official source above. Don't paste tokens, full auth headers, raw `.claude.json`, or secret-containing MCP logs into a public issue.

If you no longer need this server, review the configuration first and use `claude mcp get figma` to confirm the scope, then use `claude mcp remove figma` only for the matching registration; verify with `claude mcp list`. Check your installed Claude CLI's help if the flags differ.

<br />

[All MCP servers](./README.md) · [API keys](../../docs/security/api-keys-and-powershell.md) · [Documentation hub](../../docs/README.md)

<br />

## 📥 Ardizuo one-package setup

**Installer:** Supported automatic registration after explicit `-Apply -External -Mcps`.

Run the orchestrator to register it. The underlying command is shown below for reference:

```powershell
claude mcp add --transport http --scope user figma https://mcp.figma.com/mcp
```

**Official source:** https://developers.figma.com/docs/figma-mcp-server/

**Notes:** OAuth/account access required.

Never paste real keys into your issue, commit, README, or chat. Run `claude mcp list` and `/mcp` after registration; presence is not authentication.


---

## 📥 Current all-layer installer behavior

- **Manifest name:** `figma`
- **Transport:** `http`
- **CLI registration:** Included as a supported, opt-in command
- **Prerequisites:** Claude Code; provider access for OAuth
- **Official documentation:** https://developers.figma.com/docs/figma-mcp-server/

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
