# 🔌 Existing Claude Code MCP servers


This project targets **nine user-scoped MCP registrations**. **Registered**, **connected** and **authenticated** are different states. Never copy another person's `.claude.json` or credentials.


<br />
<br />


## 🚀 Recommended: register supported MCPs


From **Windows PowerShell** in the cloned repository:

```powershell
# Preview; no MCP settings are changed.
.\scripts\install-all.ps1 -External -Mcps

# Register missing servers with supported public commands.
.\scripts\install-all.ps1 -Apply -External -Mcps

# Inspect registrations and live connection indications.
claude mcp list
```

Tavily and Morph are deliberately **manual** because they need private credentials. The installer does not guess or embed API keys. GitHub's Docker option requires a running Docker Desktop instance and an unused port 8085.


<br />
<br />


## 📋 Included MCP names


| MCP | Transport | Installation | What it provides |
| --- | --- | --- | --- |
| `serena` | `stdio` | Supported registration | Code navigation and semantic editing (uvx) |
| `sequential-thinking` | `stdio` | Supported registration | Structured sequential reasoning (npx) |
| `chrome-devtools` | `stdio` | Supported registration | Browser inspection and debugging (npx) |
| `tavily` | `stdio` | Guided/manual | Search MCP; requires a provider API key |
| `morph-mcp` | `stdio` | Guided/manual | Morph MCP; requires provider credentials |
| `supabase` | `http` | Supported registration | Read-only Supabase project access (OAuth) |
| `figma` | `http` | Supported registration | Figma integration (OAuth) |
| `vercel` | `http` | Supported registration | Vercel account and project tools (OAuth) |
| `github` | `stdio` | Supported registration | GitHub tools through Docker OAuth and free loopback port 8085 |


<br />
<br />


## ⌨️ Individual registration commands


These are the exact supported public commands from `setup/full-stack.json`. Run **only for servers that aren't already registered**. Confirm installed package publishers before launching them.

```powershell
# serena — register only when missing
claude mcp add --scope user serena -- uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant

# sequential-thinking — register only when missing
claude mcp add --scope user sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# chrome-devtools — register only when missing
claude mcp add --scope user chrome-devtools -- npx -y chrome-devtools-mcp@latest

# supabase — register only when missing
claude mcp add --transport http --scope user supabase "https://mcp.supabase.com/mcp?read_only=true"

# figma — register only when missing
claude mcp add --transport http --scope user figma https://mcp.figma.com/mcp

# vercel — register only when missing
claude mcp add --transport http --scope user vercel https://mcp.vercel.com

# github — register only when missing
claude mcp add --scope user github -e GITHUB_OAUTH_CALLBACK_PORT=8085 -- docker run -i --rm -p 127.0.0.1:8085:8085 -e GITHUB_OAUTH_CALLBACK_PORT ghcr.io/github/github-mcp-server
```

For **Tavily** or **Morph**, use your own account's official MCP configuration flow, then check:

```powershell
claude mcp list
claude mcp get tavily
claude mcp get morph-mcp
```

**Do not paste API keys into shell commands, issue reports or GitHub commits.** Use your provider's supported authentication and secure environment configuration. Provider instructions: [Tavily](https://docs.tavily.com/documentation/mcp) · [Morph](https://docs.morphllm.com).


<br />
<br />


## 🧩 Optional extension MCPs (not part of the nine)


Six researched MCP integrations are available as an opt-in layer. Prefer project scope, and don't stack overlapping browser or search servers.

| Integration | Route | Credentials | Note |
| --- | --- | --- | --- |
| Firecrawl | `firecrawl@claude-plugins-official` plugin | Firecrawl API key | Extraction and crawling |
| Exa | `exa@claude-plugins-official` plugin | Exa account | Overlaps Tavily |
| n8n MCP | `n8n-mcp` user stdio registration | None for docs tools | Only if you use n8n |
| 21st Magic | `21st@21st-dev` plugin | `API_KEY_21ST` | React/Tailwind components |
| Playwright MCP | `playwright-mcp` user stdio registration | None | **Alternative** to the Playwright plugin |
| Agentation | Guided, inside one React/Next.js project | None | PolyForm Shield license |

```powershell
.\scripts\install-all.ps1 -External -Extensions research,automation          # Preview
.\scripts\install-all.ps1 -Apply -External -Extensions research,automation   # Install
```

The n8n registration the installer uses (documentation tools only):

```powershell
claude mcp add --scope user n8n-mcp -e MCP_MODE=stdio -e LOG_LEVEL=error -e DISABLE_CONSOLE_OUTPUT=true -- npx -y n8n-mcp
```

[Optional extensions guide](../../docs/installation/extensions.md) · [Master extension catalog](../../docs/components/extension-catalog.md)


<br />
<br />


## ✅ After registration


Open Claude Code and use `/mcp` to complete sign-in and inspect server status. Test a permitted read-only call before claiming an integration works. A dashboard badge is not connection proof.

To remove an unwanted server, first inspect `claude mcp get <name>` and then use `claude mcp remove <name>` only for that server.

[Plugin catalog](../plugins/README.md) · [Full setup](../../docs/installation/full-setup.md) · [Credential safety](../../docs/security/api-keys-and-powershell.md)
