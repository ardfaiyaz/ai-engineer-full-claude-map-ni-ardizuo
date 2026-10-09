# Requirements — Windows-first

| Requirement | Role | Core bootstrap | Full setup plan |
| --- | --- | --- | --- |
| Windows 10/11 + PowerShell 5.1+ | Local installer and scripts | Required | Required |
| Claude Code CLI | Agent runtime | Recommended | Required |
| Git | Clone and repository workflows | Recommended | Required |
| Node.js + npm | JS runtime, Claude Map and JS MCPs | Recommended | Required for relevant modules |
| Python 3 | Selected developer tools | Optional | Some modules |
| `uv` / `uvx` | Python-based MCP launchers such as Serena | Optional | If selected |
| GitHub CLI (`gh`) | GitHub login and review | Optional | If selected |
| Docker Desktop | Docker-backed MCPs / optional AIRIS | Optional | If selected |
| Obsidian | Browse local development notes | Optional | If memory selected |
| WSL | Linux-only tools | Not required | Optional |

Use `scripts/doctor.ps1` for a local check. The checker does not install system packages or verify account authentication.

## Paths

The installer uses `$env:CLAUDE_CONFIG_DIR` if set; otherwise `Join-Path $HOME '.claude'`. This is deliberately independent of the author's username. Vaults and backups are separate from your Git clone and always opt-in.

## Provider authentication

Figma, Vercel, Supabase, GitHub, Expo, Stripe, Sentry, Atlassian and Notion may prompt for OAuth or API access. A provider installed or configured in Claude Code may still be unauthenticated. Test with `/mcp`, `claude mcp list`, and the provider's documented verification flow. Use least-privileged / test environments for financial and deployment tools.
