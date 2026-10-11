---
name: version-log
description: Keep a VERSIONLOG.md at the repository root up to date. Use at the Ship stage after any completed change to a repository (feature, fix, refactor, docs, dependency or config change), before committing, and whenever the user asks for a changelog, release notes or version history.
---


# 📄 Version Log


This is an original Ardizuo development skill. It keeps one human-readable history file, `VERSIONLOG.md`, at the **root of the repository being changed**, so every change set has a dated record.


<br />
<br />


## 🔄 When to run


- At the end of the Ship stage, after the change is verified and **before** the commit, so the entry and the code ship together.
- When the user asks for a changelog, release notes or "what changed".
- Skip it for a change that touches nothing in the repository (pure questions, read-only reviews).


<br />
<br />


## 📋 Steps


1. Find the repository root (`git rev-parse --show-toplevel`). Use its `VERSIONLOG.md`; if the project already keeps `CHANGELOG.md` instead, update that file and don't create a second log.
2. If no log exists, create `VERSIONLOG.md` with the header from the template below.
3. Work out what changed from evidence: `git status`, `git diff --stat` and `git diff` for uncommitted work, or `git log` since the last logged entry. Never list a change you did not see.
4. Pick the version label:
   - If the project declares a version (`package.json`, `pyproject.toml`, `Cargo.toml`, `*.csproj`, a Git tag), use it and say whether this change bumps it. Suggest a semantic version bump (major for breaking changes, minor for features, patch for fixes), but never edit the version file without the user's approval.
   - Otherwise use the date as the label, for example `2026-10-11`. Add `.2`, `.3` for further entries on the same day.
5. Add one new entry **at the top**, newest first, grouped under only the headings that apply: Added, Changed, Fixed, Removed, Security, Docs.
6. Write each bullet as a user-visible outcome in plain language, and name the main files or commands touched. Add a **Verification** line with the checks that actually ran (tests, build, lint), or say that none ran.
7. Show the entry to the user together with the rest of the Ship summary. It is part of the change, so it is committed with it, but commit only when the user has asked for a commit.


<br />
<br />


## 📄 Template


```markdown
# Version log

All notable changes to this project. Newest first.

## 2026-10-11 — Short title of the change

### Added
- What is new, from the user's point of view (`path/or/command`).

### Changed
- What behaves differently now.

### Fixed
- What was broken and is now correct.

**Verification:** `npm test` passed (42 tests); build not run.
```

If the repository has its own Markdown heading conventions (for example required emoji in headings), follow them inside the log.


<br />
<br />


## 🛡️ Rules


- Never rewrite or delete earlier entries. Correct a mistake with a new bullet in the newest entry.
- Never record secrets, tokens, internal URLs, personal paths, customer data or raw conversation text.
- Don't invent version numbers, release dates, ticket IDs or commit hashes. A commit hash can be added only after the commit exists.
- Keep entries short: a few bullets per heading. Link to detailed docs instead of copying them.
- One entry per change set. If several commits ship together, summarize them in one entry.
