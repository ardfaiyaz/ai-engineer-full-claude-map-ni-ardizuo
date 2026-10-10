# ☑️ Release and installation checklist


**Two different questions:** Does the **public package** install its supported components? Does it **exactly clone** the maintainer's private device? The first has passed an isolated Windows installation. The second has unresolved sources and cannot honestly be called complete.


<br />
<br />


## 📦 Public package — verified scope


- [x] **21 agent definitions:** one Ardizuo-owned and 20 pinned upstream.
- [x] **36 default direct skill definitions:** 16 Ardizuo-owned and 20 pinned publisher prompts; five different upstream versions require opt-in.
- [x] **20 default executable commands:** one Ardizuo command and 19 pinned SuperClaude commands; 11 different upstream variants require opt-in.
- [x] **12 plugin IDs and nine target MCPs** have installation guides or supported registration attempts.
- [x] **Five hooks, rules, workflow definitions, portable `CLAUDE.md`** and safe hook registration are packaged.
- [x] **Optional memory templates** and a five-stage Claude Map rehearsal are available, without bundling personal notes.
- [x] Installer previews first, avoids overwriting different files, and leaves credentials out of the package.
- [x] Markdown uses emoji headings and obsolete sprint handoff notes were removed.


<br />
<br />


## 🖥️ New Windows device — short acceptance check


- [ ] Git, Python, Node/npm and Claude Code resolve in a fresh PowerShell session.
- [ ] `scripts/install-all.ps1 -All` previews expected changes and identifies any conflicts.
- [ ] `scripts/install-all.ps1 -Apply -All` completes the selected install or explains any optional unavailable providers.
- [ ] `python scripts/verify-installed-layers.py --strict-local --require-hooks` reports no expected package file or registration missing.
- [ ] `claude plugin list` shows the plugins actually enabled; `claude mcp list` shows connected/unauthenticated servers accurately.
- [ ] In Claude Code, inspect `/skills`, `/hooks`, and `/mcp`; run **one** low-risk agent or skill action if desired.
- [ ] If using Claude Map, run the *separate* dashboard rehearsal and verify the five stages in the local browser.


<br />
<br />


## ⚠️ Known limits — not hidden blockers


- **Not a byte-for-byte clone:** 17 separately sourced direct skills and four unknown-origin skill files lack approved full-source reproduction.
- **Different upstream content:** five skill and 11 SuperClaude command variants differ from the source machine, so opt-in versions are not called exact copies.
- **Support files:** some skills reference scripts, data or other sidecars; an installed `SKILL.md` alone does not prove full functionality.
- **Accounts:** user logins, provider OAuth, API keys, account-scoped MCP connections and private vault contents are not redistributable.
- **Runtime:** source presence, CLI exit code and configured status do not demonstrate executed agent delegation, hook side effects or completed tasks.
- **Removal:** there is no universally safe automatic uninstall for all third-party packages. Keep personal backups and use the provider's instructions.


<br />
<br />


## 🛡️ Maintainer's final publication gate


- [ ] Keep `main` clean: `git status` and `git diff --check`.
- [ ] Run **one concise check** before a release: `python -m unittest discover -s tests -q`.
- [ ] Confirm the public-facing numbers with `python scripts/release-audit.py`; don't claim 62/62 direct-skill installation until the sources are verified.
- [ ] Check tracked files and Git history for credentials, personal paths, private vault notes and unlicensed content before publishing a release tag.
- [ ] Publish the scope as **public assisted setup**, not a guaranteed exact device clone or credential migration.

[Quick install](../START-HERE.md) · [Package matrix](./installation/reproducibility-matrix.md) · [Security](../SECURITY.md)
