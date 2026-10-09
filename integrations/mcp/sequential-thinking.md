# <img src="../../docs/assets/lucide/plug.svg" width="18" height="18" alt="" /> Sequential Thinking MCP

**Purpose:** Structured sequential reasoning tooling. **Transport on reference machine:** `stdio`.

**Status:** Reference-only; not installed, registered or authenticated by the Core bootstrap.

<br />

## <img src="../../docs/assets/lucide/download.svg" width="18" height="18" alt="" /> 1. Requirements

[Sequential Thinking — official source](https://github.com/modelcontextprotocol/servers) · [Node/npm](../../docs/installation/nodejs-npm.md)

Node/npm may be needed for the maintained server package.

<br />

## <img src="../../docs/assets/lucide/plug.svg" width="18" height="18" alt="" /> 2. Register the server (after review)

**Installation:** This is a local `stdio` server. Its package name, launcher arguments, version and required environment vary by upstream implementation. Use [Sequential Thinking official documentation](https://github.com/modelcontextprotocol/servers) for the exact command and review it before running. Avoid copying credentials or private launcher scripts from another computer.


**Safety:** Check official registry/publisher and executable arguments before registering.

<br />

## <img src="../../docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 3. Authenticate and verify

```powershell
claude mcp list
```

Open Claude Code and use `/mcp` to complete provider sign-in and inspect status. A config entry is only **configured** until the server is actually connected. Grant only the needed access, ideally in a test environment.

<br />

## <img src="../../docs/assets/lucide/wrench.svg" width="18" height="18" alt="" /> 4. Troubleshoot and remove

If startup fails, confirm the runtime, endpoint or launcher command, connectivity and permissions using the official source above. Don't paste tokens, full auth headers, raw `.claude.json`, or secret-containing MCP logs into a public issue.

If you no longer need this server, review the configuration first and use `claude mcp get sequential-thinking` to confirm the scope, then use `claude mcp remove sequential-thinking` only for the matching registration; verify with `claude mcp list`. Check your installed Claude CLI's help if the flags differ.

<br />

[All MCP servers](./README.md) · [API keys](../../docs/security/api-keys-and-powershell.md) · [Documentation hub](../../docs/README.md)

<br />

## <img src="../../docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Ardizuo one-package setup

**Installer:** Supported automatic registration after explicit `-Apply -External -Mcps`.

Run the orchestrator to register it. The underlying command is shown below for reference:

```powershell
claude mcp add --scope user sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking
```

**Official source:** https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking

**Notes:** Node/npm required; inspect package before accepting execution.

Never paste real keys into your issue, commit, README, or chat. Run `claude mcp list` and `/mcp` after registration; presence is not authentication.


---

## <img src="../../docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Current all-layer installer behavior

- **Manifest name:** `sequential-thinking`
- **Transport:** `stdio`
- **CLI registration:** Included as a supported, opt-in command
- **Prerequisites:** `npx`
- **Official documentation:** https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking

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
