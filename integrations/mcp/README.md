# MCP reference catalog

No tokens, auth headers or API keys are stored here. **Configured** does not mean **connected**. Each provider must be installed and authenticated by the user.

| Name | Transport reported by original environment | Status in this repository |
| --- | --- | --- |
| `serena` | `stdio` | Reference only |
| `sequential-thinking` | `stdio` | Reference only |
| `chrome-devtools` | `stdio` | Reference only |
| `tavily` | `stdio` | Reference only |
| `morph-mcp` | `stdio` | Reference only |
| `supabase` | `http` | Reference only |
| `figma` | `http` | Reference only |
| `vercel` | `http` | Reference only |
| `github` | `stdio` | Reference only |

Check connectivity using `claude mcp list` and Claude Code `/mcp` before assuming a server is available. Some providers require additional consent or paid accounts.
