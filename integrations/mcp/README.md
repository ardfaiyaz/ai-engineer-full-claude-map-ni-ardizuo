# <img src="../../docs/assets/lucide/plug.svg" width="18" height="18" alt="" /> MCP integration catalog

**These are the nine user-scoped server names from the author's reference environment.** The current Core bootstrap does not install or authenticate any of them.

<br />

## <img src="../../docs/assets/lucide/file-text.svg" width="18" height="18" alt="" /> Pick a provider

| Individual guide | Reference transport | Core install status |
| :--- | :--- | :--- |
| [Serena](./serena.md) | `stdio` | Reference only |
| [Sequential Thinking](./sequential-thinking.md) | `stdio` | Reference only |
| [Chrome DevTools MCP](./chrome-devtools.md) | `stdio` | Reference only |
| [Tavily](./tavily.md) | `stdio` | Reference only |
| [Morph MCP](./morph-mcp.md) | `stdio` | Reference only |
| [Supabase](./supabase.md) | `http` | Reference only |
| [Figma](./figma.md) | `http` | Reference only |
| [Vercel](./vercel.md) | `http` | Reference only |
| [GitHub MCP](./github.md) | `stdio` | Reference only |

<br />

## <img src="../../docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Recommended setup flow

1. Read [Claude Code's official MCP guide](https://code.claude.com/docs/en/mcp).
2. Choose a provider and follow its dedicated page.
3. Register at **user scope** only if you want it across all projects.
4. Prefer provider OAuth/browser sign-in over static keys; follow [API key safety](../../docs/security/api-keys-and-powershell.md).
5. Check `claude mcp list` and Claude Code `/mcp`. A configured item is **not proof of connectivity**.

**Do not copy anyone else's `.claude.json`, MCP bearer tokens, environment blocks, personal Docker wrappers or credentials.**

<br />

[Plugin catalog](../plugins/README.md) · [Requirements](../../docs/prerequisites.md) · [Docs hub](../../docs/README.md)


## <img src="../../docs/assets/lucide/command.svg" width="18" height="18" alt="" /> Seven supported registration commands, two account-specific steps

The All Layers installer can now **attempt** public registrations for Serena, Sequential Thinking, Chrome DevTools, Supabase (read-only), Figma, Vercel, and the [official GitHub MCP Docker OAuth flow](./github.md). Tavily and Morph remain manual credential-dependent setups.

No MCP connector is considered authenticated by merely returning exit code zero. GitHub Docker OAuth will prompt for browser login on first use. Supabase, Figma and Vercel may also need account consent in Claude Code.

```powershell
.\scripts\install-all.ps1 -External -Mcps          # dry run
.\scripts\install-all.ps1 -Apply -External -Mcps   # user-approved registration
claude mcp list
```

Use [exact reference coverage](../../docs/components/exact-coverage.md) to audit the configured names and then verify live status in `/mcp`.
