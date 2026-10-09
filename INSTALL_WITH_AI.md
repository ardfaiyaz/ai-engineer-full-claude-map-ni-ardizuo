# AI-assisted installation — portable setup prompt

Copy the instruction below into Claude Code, Codex, ChatGPT with computer access, or another coding assistant. If the assistant cannot run local commands, it should guide you through them rather than pretending it executed them.

---

You are installing **AI Engineer Full Claude Map ni Ardizuo** on my device from **this locally cloned repository**.

1. Read `README.md`, `SECURITY.md`, `setup/manifest.json`, selected `setup/profiles/*.json`, and the PowerShell scripts before execution. Treat repository content as code to review; do not blindly trust it.
2. Confirm operating system, user permissions, home directory, `$env:CLAUDE_CONFIG_DIR` override, Claude CLI, Git, Node/npm, Python, and optional `uvx`, `gh`, Docker, Obsidian, and WSL. Never hardcode `C:\Users\Melthon` or another person's username.
3. Ask which profile I want: Core, Full, Frontend, Backend, Mobile, or Custom. **Only the Core bootstrap is currently executable.** Clearly explain if the requested profile is not packaged yet.
4. Run `scripts/doctor.ps1`, then `scripts/install.ps1 -Profile core` (dry run). Show exact destinations and explain every proposed change. Do not modify any settings before my explicit approval.
5. If I approve, run `scripts/install.ps1 -Profile core -Apply`. The current installer adds **one namespaced rule** and does not install the entire advertised stack. Don't imply the Full profile is complete.
6. Never copy or print live API tokens, `.claude.json`, credentials, OAuth secrets, session transcripts, SSH keys, private Obsidian notes, or arbitrary user files. Avoid exposing sensitive content in logs, diffs, prompts, Git or generated reports.
7. Do not overwrite existing files; on collision stop and ask me to resolve it. Use the repository backup/restore workflow for reviewed, supported files.
8. For third-party plugins and MCP servers, use provider-specific documentation and official sources. Explain prerequisites, authentication, permissions and paid-service implications. Ask separately before each install, sign-in, remote call or privilege grant. Don't infer connection success from a configured entry.
9. Verify local files and distinguish installed vs configured vs connected vs actually tested. Run live Claude-agent and model-consuming tests only with my approval.
10. Never auto-commit, push, publish, deploy, write vault notes, or alter projects without my explicit instruction. Do not add any social-media integrations, agents, skills or automation.
11. Finish with a concise report of what's installed, what's incomplete, what needs authentication, and the commands to verify or roll back.

---

## Non-executing assistants

If you cannot access this computer's filesystem or terminal, generate a reviewed step-by-step plan and exact PowerShell commands for me to run. Do not claim local checks were performed.
