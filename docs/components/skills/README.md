# 🧩 Built-in Ardizuo skill catalog


This repository includes **16 Ardizuo-authored skills**. Their real Claude Code instructions live in `ardizuo-plugin/skills/<name>/SKILL.md`; this catalog replaces 16 repetitive installation pages.


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


## 📥 Install the complete set


From the cloned repository in **Windows PowerShell**:

```powershell
# Preview the local pack without installing any plugins or MCPs.
.\scripts\install-all.ps1

# Apply only when the preview shows no conflicts.
.\scripts\install-all.ps1 -Apply
```

These skills are also included when you choose the guided `-Apply -All` install. Existing different files are **never overwritten**.


## ✅ Verify and use


```powershell
python .\scripts\verify-installed-layers.py --strict-local
```

In Claude Code, use `/skills`. This verifies file installation, **not** whether an individual skill executed. To see all third-party source-matched skills, read [pinned skills](../../installation/pinned-skills.md).

[Component catalog](../README.md) · [Quick start](../../../START-HERE.md)
