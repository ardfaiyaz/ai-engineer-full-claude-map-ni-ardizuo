# 🧩 Built-in Ardizuo skill catalog


This repository includes **17 Ardizuo-authored skills**. Their real Claude Code instructions live in `ardizuo-plugin/skills/<name>/SKILL.md`; this catalog replaces 16 repetitive installation pages.


<br />
<br />


## 📋 What each skill is for


| Skill | Purpose |
| --- | --- |
| `claude-md-management` | Review project and global instruction files safely. |
| `clean-code-typescript` | Keep TypeScript code readable and well typed. |
| `code-splitting` | Identify sensible lazy-loading and bundle boundaries. |
| `dead-code-scan` | Review likely unused code and request approval before removal. |
| `fix-build` | Diagnose a failing build and verify the smallest fix. |
| `gauge-improvements` | Compare improvements against measured baselines. |
| `humanizer` | Improve writing clarity while retaining technical meaning. |
| `pragmatic-code-guidelines` | Prefer a small, maintainable implementation. |
| `react-native-best-practices` | Review React Native structure, performance and state. |
| `reuse-audit` | Check for existing reusable code before implementing another version. |
| `root-cause-analysis` | Find the cause of a problem before changing code. |
| `ship-learn-next` | Summarize verified delivery and follow-up tasks. |
| `team-driven-development` | Define explicit owners and boundaries for parallel work. |
| `technical-style-guide` | Keep technical documentation consistent and concise. |
| `test-fixing` | Investigate tests and repair genuine failures. |
| `vault-learning` | Capture approved, reusable lessons in the local vault. |
| `version-log` | Keep a `VERSIONLOG.md` at the root of every repository you change: one dated entry per change set, newest first. |


<br />
<br />


## 📥 Install the complete set


From the cloned repository in **Windows PowerShell**:

```powershell
# Preview the local pack without installing any plugins or MCPs.
.\scripts\install-all.ps1

# Apply only when the preview shows no conflicts.
.\scripts\install-all.ps1 -Apply
```

These skills are also included when you choose the guided `-Apply -All` install. Existing different files are **never overwritten**.


<br />
<br />


## 🔎 Researched extension skills (installed by -All)


Twenty more skills (catalog rows 63–82) come from publisher plugins rather than this repository. They include Ponytail, Matt Pocock's `domain-modeling`, `to-tickets`, `tdd` and `grill-me`, Trail of Bits' `differential-review` and `mutation-testing`, and Daymade's `frontend-visual-qa`. Every name was verified upstream on 2026-10-11. They are **not** counted in the 62 reference skills; `-All` installs them through the extended stack, together with four hash-pinned Karpathy skills.

[Master extension catalog](../extension-catalog.md) · [Extended stack guide](../../installation/extensions.md)


<br />
<br />


## 📄 The version-log skill


`version-log` gives every installation the habit of keeping a version history. At the end of a change (the Ship stage), Claude finds the repository root, reads the real diff, and adds a dated entry at the top of `VERSIONLOG.md` (or the project's existing `CHANGELOG.md`) under Added, Changed, Fixed, Removed, Security or Docs, with the checks that actually ran. It never rewrites old entries, invents version numbers or records secrets, and it never bumps a version file without asking. You can also ask for it directly: "update the version log".

It is a **skill** rather than a hook or agent on purpose. A hook only runs a script on an event and can't judge what changed. An agent only runs when something delegates to it. A skill is instructions Claude follows at the right moment. This repository keeps its own [VERSIONLOG.md](../../../VERSIONLOG.md) the same way.


<br />
<br />


## ✅ Verify and use


```powershell
python .\scripts\verify-installed-layers.py --strict-local
```

In Claude Code, use `/skills`. This verifies file installation, **not** whether an individual skill executed. To see all third-party source-matched skills, read [pinned skills](../../installation/pinned-skills.md).

[Component catalog](../README.md) · [Quick start](../../../START-HERE.md)
