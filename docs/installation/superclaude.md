# 🤖 SuperClaude Framework — agents and sc commands


**Publisher:** [SuperClaude-Org](https://github.com/SuperClaude-Org/SuperClaude_Framework) · **Role:** upstream specialist agents, `sc` commands and development workflow extensions. **Important:** exact filenames and agent installation behavior have differed across upstream versions; verify individually rather than assuming 20/20 files.


<br />
<br />


## 📥 Requirements


Install [Python](./python.md), [Claude Code](./claude-code.md) and [pipx](https://pipx.pypa.io/stable/installation/). For optional SuperClaude MCP features, follow the framework's official documentation.


<br />
<br />


## 📥 Install (official method)


```powershell
pipx install superclaude
superclaude install
```

The `superclaude install` command modifies global Claude Code assets. Preview changes and back up existing configuration before accepting upstream prompts. The Ardizuo Full installer invokes this only when you explicitly select `-SuperClaude` (or `-All`).


<br />
<br />


## ☑️ Verify


```powershell
superclaude doctor
superclaude install --list
```

Within Claude Code, look for `/sc:research`, `/sc:brainstorm`, and installed specialist agent definitions. Filename discovery is not proof that the agent executed.

```powershell
python .\scripts\coverage-doctor.py
```

**If the doctor still shows missing agents**, check the current upstream package and release documentation. An upstream [2026 issue about missing agent files](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues/531) demonstrates why the command succeeding cannot be treated as exact agent-file proof. Do not silently download cached agent files from unrelated plugins or overwrite custom agents.


<br />
<br />


## 🛠️ Troubleshooting and removal


If the CLI isn't found after installing with pipx, reopen PowerShell and check `pipx list` and your PATH. If it reports conflicts, stop and use the official [installation guide](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/docs/getting-started/installation.md), rather than deleting existing users' files.

For removal, use the upstream framework's uninstall instructions, review generated changes, and retain user-authored files.

[Installation guides](./README.md) · [Reference agent list](../components/coverage.md)


<br />
<br />


## 📁 Exact source pin for repeatable definitions


The [pinned SuperClaude installer](./pinned-superclaude.md) can reproduce 20 upstream agent definitions and 19 identical command definitions without installing SuperClaude's Python CLI. Another 11 command definitions are available as explicitly opted-in publisher originals, not exact matches for the author's locally changed files. Use this mode in a disposable config and test runtime behavior separately.
