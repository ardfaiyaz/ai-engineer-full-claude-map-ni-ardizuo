# <img src="../../docs/assets/lucide/plug.svg" width="18" height="18" alt="" /> GitHub MCP MCP

**Purpose:** Repository, pull-request and issue workflows. **Transport on reference machine:** `stdio`.

**Status:** Reference-only; not installed, registered or authenticated by the Core bootstrap.

<br />

## <img src="../../docs/assets/lucide/download.svg" width="18" height="18" alt="" /> 1. Requirements

[GitHub MCP — official source](https://github.com/github/github-mcp-server) · [GitHub CLI](../../docs/installation/github-cli.md) · [Docker](../../docs/installation/docker.md)

GitHub CLI OAuth and (for some setups) Docker are used.

<br />

## <img src="../../docs/assets/lucide/plug.svg" width="18" height="18" alt="" /> 2. Register the server (after review)

**Recommended setup:** official Docker OAuth launcher, per [GitHub MCP for Claude Code](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md). Install and start Docker Desktop first. Port 8085 on the loopback interface must be free.

```powershell
claude mcp add --scope user github -e GITHUB_OAUTH_CALLBACK_PORT=8085 -- docker run -i --rm -p 127.0.0.1:8085:8085 -e GITHUB_OAUTH_CALLBACK_PORT ghcr.io/github/github-mcp-server
```

The server prompts for GitHub browser OAuth when used. No PAT or raw bearer authorization header is embedded. The Ardizuo Full installer now has this **opt-in registration command** when Docker is available. This does not prove the container started or OAuth succeeded.


**Safety:** Prefer read-only mode for exploration. Avoid printing `gh auth token` or putting PATs in command history.

<br />

## <img src="../../docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 3. Authenticate and verify

```powershell
claude mcp list
```

Open Claude Code and use `/mcp` to complete provider sign-in and inspect status. A config entry is only **configured** until the server is actually connected. Grant only the needed access, ideally in a test environment.

<br />

## <img src="../../docs/assets/lucide/wrench.svg" width="18" height="18" alt="" /> 4. Troubleshoot and remove

If startup fails, confirm the runtime, endpoint or launcher command, connectivity and permissions using the official source above. Don't paste tokens, full auth headers, raw `.claude.json`, or secret-containing MCP logs into a public issue.

If you no longer need this server, review the configuration first and use `claude mcp get github` to confirm the scope, then use `claude mcp remove github` only for the matching registration; verify with `claude mcp list`. Check your installed Claude CLI's help if the flags differ.

<br />

[All MCP servers](./README.md) · [API keys](../../docs/security/api-keys-and-powershell.md) · [Documentation hub](../../docs/README.md)

<br />

## <img src="../../docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Ardizuo one-package setup

**Installer:** Supported public registration command (Docker OAuth); interactive GitHub login and runtime verification remain required.

**Official source:** https://github.com/github/github-mcp-server

**Notes:** Recommended official Docker OAuth flow on localhost port 8085. Do not publish OAuth credentials or private settings. Review GitHub tool access before granting write permissions.

Never paste real keys into your issue, commit, README, or chat. Run `claude mcp list` and `/mcp` after registration; presence is not authentication.


---

## <img src="../../docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Current all-layer installer behavior

- **Manifest name:** `github`
- **Transport:** `stdio`
- **CLI registration:** Included as a supported, opt-in command
- **Prerequisites:** `docker`
- **Official documentation:** https://github.com/github/github-mcp-server

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
