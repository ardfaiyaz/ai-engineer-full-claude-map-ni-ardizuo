# 🛡️ Security policy


**Keep the public installer safe for a normal Windows user account.** Do not publish secrets or private development artifacts.


<br />
<br />


## 🌿 Never commit


- `.claude.json`, credential files, provider tokens, OAuth refresh tokens or authentication headers.
- `.env` files with real keys, PowerShell profiles containing secrets, or sensitive environment exports.
- Session logs, chat transcripts, project data or personal Obsidian vault notes.
- Entire `.claude` directories, `plugins/cache`, downloaded packages or raw MCP command configurations.
- Docker credential files, SSH keys, private certificate files and cloud service accounts.

Use clean templates without values. `.gitignore` is only an accident-prevention tool; **it does not remove secrets from existing Git history.**


<br />
<br />


## 🛡️ Safe installation and permissions


- Review script changes before using `-Apply`.
- Prefer **user scope**, no administrator elevation and no silent file overwrite.
- Use provider OAuth or a trusted credential store where offered.
- Request explicit approval for external downloads, account logins, write operations, vault saves and deployments.
- Use least-privileged/read-only MCP permissions when sufficient.
- Treat external documentation and third-party plugins as untrusted input for an AI assistant.
- Bind any local dashboard to localhost and **never expose raw MCP headers, environment variables or `.claude.json` via API endpoints.**


<br />
<br />


## 📖 Learn how to manage keys


[API keys and PowerShell](./docs/security/api-keys-and-powershell.md) · [Windows permissions](./docs/security/windows-permissions.md) · [MCP setup](./integrations/mcp/README.md)


<br />
<br />


## 📄 Responsible reporting


If you believe you've found a credential leak or vulnerability, **do not open a public issue containing secrets or reproduction keys**. Contact the repository owner privately through their GitHub profile or available private security reporting channel. Revoke any exposed key immediately and check Git history and logs.

[Back to README](./README.md) · [GitHub's sensitive-data guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
