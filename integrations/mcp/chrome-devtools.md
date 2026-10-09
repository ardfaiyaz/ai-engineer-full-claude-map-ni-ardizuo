# Chrome DevTools MCP MCP

**Purpose:** Chrome browser debugging and inspection. **Transport on reference machine:** `stdio`.

**Status:** Reference-only; not installed, registered or authenticated by the Core bootstrap.

<br />

## 1. Requirements

[Chrome DevTools MCP — official source](https://github.com/ChromeDevTools/chrome-devtools-mcp) · [Node/npm](../../docs/installation/nodejs-npm.md)

Chrome and Node/npm are typically required.

<br />

## 2. Register the server (after review)

**Installation:** This is a local `stdio` server. Its package name, launcher arguments, version and required environment vary by upstream implementation. Use [Chrome DevTools MCP official documentation](https://github.com/ChromeDevTools/chrome-devtools-mcp) for the exact command and review it before running. Avoid copying credentials or private launcher scripts from another computer.


**Safety:** Only attach to browser sessions you are authorized to inspect; browser state may contain private data.

<br />

## 3. Authenticate and verify

```powershell
claude mcp list
```

Open Claude Code and use `/mcp` to complete provider sign-in and inspect status. A config entry is only **configured** until the server is actually connected. Grant only the needed access, ideally in a test environment.

<br />

## 4. Troubleshoot and remove

If startup fails, confirm the runtime, endpoint or launcher command, connectivity and permissions using the official source above. Don't paste tokens, full auth headers, raw `.claude.json`, or secret-containing MCP logs into a public issue.

If you no longer need this server, review the configuration first and use `claude mcp get chrome-devtools` to confirm the scope, then use `claude mcp remove chrome-devtools` only for the matching registration; verify with `claude mcp list`. Check your installed Claude CLI's help if the flags differ.

<br />

[All MCP servers](./README.md) · [API keys](../../docs/security/api-keys-and-powershell.md) · [Documentation hub](../../docs/README.md)
