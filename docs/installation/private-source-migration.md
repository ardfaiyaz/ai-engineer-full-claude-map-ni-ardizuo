# Privately reviewing missing global agents, skills and commands

<img src="../assets/icons/shield.svg" width="18" height="18" alt="" /> **Owner review required before redistribution.**

The main installer includes 28 reviewed development assets and obtains other items from their upstream publishers. The author's reference machine has additional agent, skill and command files, but a **filename is not evidence of authorship or an open-source license**. This is a controlled process for inspecting direct-scope definitions without exporting private session data or copying plugin caches.

<br />

## 1. Prepare a private, outside-the-repo folder

```powershell
cd "$HOME\Documents\ai-engineer-full-claude-map-ni-ardizuo"

# Preview file names ONLY — no copying or secret output.
python .\scripts\prepare-private-review.py
```

The script looks at the names-only inventory of **21 agents, 62 skills and 32 commands**. It finds matching direct-scope source Markdown but skips all files already included in Ardizuo's 28 reviewed assets. It will **not** scan caches, personal chats, `.claude.json`, `settings.json`, tokens, or Obsidian notes.

<br />

## 2. Export candidates locally, with explicit approval

```powershell
python .\scripts\prepare-private-review.py --apply
```

Default destination: `$HOME\Documents\Ardizuo-Additional-Assets-PRIVATE`. The script refuses an existing target so it cannot overwrite a previous review. **Do not put this folder inside the public repository or immediately compress/share it.** You can specify another empty location with `--output`.

<br />

## 3. Review content, origin and licenses

For every file, check:

- **Provenance:** Was this authored by you, a published third-party project, an AI coding plugin, or a copy of someone else's skill? Identify repository URL and license when applicable.
- **Secrets:** Remove credentials, personal API endpoints, account IDs, auth headers, passwords and access tokens. Review all textual values, not only standard token prefixes.
- **Paths:** Remove `C:\Users\<username>` paths, private local file names, vault paths, external hardcoded working directories and home-machine assumptions.
- **Behavior:** Identify downloads, shell scripts, file modification, network calls, local privilege changes or automatic note saving. They must require suitable user approval.
- **Redistribution:** Reference an official upstream installer when rights to republish source are unclear. Attribute original authors and observe license obligations.

Use a text editor to review each file. An automated pattern scan is an **aid**, never a proof of safety.

<br />

## 4. Integrate only approved sources

Only original or redistribution-approved assets should be added to `ardizuo-plugin/` and to an explicit, tested source manifest. Third-party packages should normally be installed from the publisher's marketplace, not vendored into this repository. Update [exact coverage](../components/exact-coverage.md), the license notice, the installation scripts and regression tests together.

Never commit credential-bearing configuration, any `*.local.json` inventory with secret values, `.claude.json`, `settings.json` backups, vault notes, plugin caches, or session logs.

<br />

## 5. Check live integration separately

```powershell
python .\scripts\coverage-doctor.py
python -m unittest discover -s tests -v
```

Then run the steps in [verification checklist](./verification-checklist.md) on a disposable Claude configuration and a real fresh Windows installation. File presence alone is not runtime proof.

[Security](../../SECURITY.md) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Docs hub](../README.md)
