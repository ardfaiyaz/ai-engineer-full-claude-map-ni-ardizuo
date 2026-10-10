# 🛡️ API keys, OAuth, and PowerShell privacy


**Read this before connecting MCP servers or provider plugins.** You usually do not need an API key to use the Claude Code subscription sign-in flow. Other providers may require OAuth, API keys or organization permissions.


## 🛡️ 1. Choose the safer authentication method


| Preferred approach | Best for | Why |
| :--- | :--- | :--- |
| **Provider OAuth / browser login** | Claude Code, GitHub, many cloud MCPs | Provider handles token storage and refresh |
| **Approved credential manager** | Long-lived local application secrets | Avoids keeping keys in your PowerShell profile or Git files |
| **Temporary process environment variable** | CLI that *only* supports a key in an environment variable | Works for the current terminal and its children; clear it afterward |
| `.env` file in a Git repository | **Avoid for sensitive keys** | Easy to leak through logs, commits or backups |

**Never** commit credentials, paste live keys into an AI prompt, or add them to command-line flags where command history can record them.


## 📄 2. Getting a provider key (only if needed)


Open the provider's **official console** and use its API or developer section. Choose minimal scopes, development/test environment, and an expiry if available. Some tools may offer OAuth instead and should use that first.

| Provider | Official entry point | Guidance |
| :--- | :--- | :--- |
| Anthropic | [Console](https://console.anthropic.com/) · [API keys](https://docs.anthropic.com/en/docs/initial-setup) | Subscription sign-in and API billing are different |
| GitHub | [GitHub CLI](https://cli.github.com/manual/gh_auth_login) | Prefer `gh auth login`; tokens only if required |
| Tavily | [Developer portal](https://app.tavily.com/) | Keep the key only in the intended integration |
| Supabase | [Dashboard](https://supabase.com/dashboard) · [access tokens](https://supabase.com/docs/guides/platform/access-tokens) | Prefer read-only/database-limited access where supported |
| Figma | [Developer documentation](https://www.figma.com/developers) | Prefer OAuth or official MCP login |
| Vercel | [Tokens](https://vercel.com/docs/rest-api#authentication) | Scope to the intended team/project |
| Stripe | [API keys](https://docs.stripe.com/keys) | **Use test keys**; never publish or use live secret keys in examples |
| Sentry | [Developer docs](https://docs.sentry.io/api/auth/) | Use only the scopes needed by your workflows |
| Atlassian | [API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) | Use provider authentication supported by its plugin |
| Notion | [Integrations](https://developers.notion.com/docs/create-a-notion-integration) | Limit pages and permissions explicitly |

MCPs that support browser sign-in often **do not need any manual API token**.


## 💻 3. Mask a key while typing (PowerShell 5.1 compatible)


`Read-Host -AsSecureString` hides the *input*. But environment variables are **ordinary strings**, not a secure vault. The value can exist in process memory and be read by sufficiently privileged software.

If a trusted CLI requires an environment variable, this is an example of creating a **temporary process-scoped** value without placing the secret itself in shell history:

```powershell
# Example only: use the variable name documented by your chosen provider.
$secret = Read-Host 'Enter MY_SERVICE_API_KEY' -AsSecureString
$ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
try {
    $env:MY_SERVICE_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
} finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
    Remove-Variable secret -ErrorAction SilentlyContinue
}

# Run the trusted CLI that reads this variable here.
# Example: & .\trusted-tool.exe

# Remove it as soon as the command has finished:
Remove-Item Env:MY_SERVICE_API_KEY -ErrorAction SilentlyContinue
```

**Limitations:** The string exists unencrypted in the current PowerShell process and is inherited by child processes while set. It is **not invisible** to the operating system, debuggers, administrators or processes with appropriate access. For stronger protection use provider OAuth or an application credential store, not environment variables.


## 📄 4. What NOT to do


```powershell
# DO NOT put a real key in these examples:
# $env:MY_SERVICE_API_KEY = 'real-secret-here'        # shell history
# setx MY_SERVICE_API_KEY 'real-secret-here'          # persistent user storage
# claude mcp add --env MY_SERVICE_API_KEY=real-key ... # command history/config risk
```

Do not put long-lived secrets in `$PROFILE`, `settings.json`, public `.mcp.json`, repository `.env` files, screenshots, CI logs, or prompt text. **Ignoring `.env` via `.gitignore` reduces accidents but does not encrypt a file.**

For persistent credentials, follow the provider's OAuth/credential-store instructions. If a service only supports static keys, document exactly where it stores them and assess whether you trust that storage before continuing.


## 🛡️ 5. Verify safely without revealing the value


```powershell
# Only checks if the variable is populated. It does not print its content.
[bool]$env:MY_SERVICE_API_KEY

# Verify MCP connection status separately:
claude mcp list
```

Inside Claude Code, open `/mcp` to inspect sign-in requirements. A configured entry is **not** the same as an authenticated, working server.


## 📄 6. If a key was exposed


1. **Revoke or rotate it immediately** in the provider console.
2. Check Git history, CI logs, shell history, screenshots, pasted prompts and exposed files.
3. Replace the credential in trusted storage and reduce its permissions.
4. If it was committed, follow your organization's incident process; deleting a file in a later commit does **not** remove the original secret from Git history.


### 📖 Official references


- [PowerShell: environment variable scopes](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables)
- [Microsoft: Read-Host and secure input](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/read-host)
- [Claude Code: MCP authentication](https://code.claude.com/docs/en/mcp)
- [GitHub: remove sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

[Security policy](../../SECURITY.md) · [MCP catalog](../../integrations/mcp/README.md) · [Docs hub](../README.md)
