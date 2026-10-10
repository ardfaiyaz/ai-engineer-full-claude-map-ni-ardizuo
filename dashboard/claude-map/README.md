# 📥 Claude Map — AI / Software Engineer Claude Setup


**Local-only visualization with the five-stage workflow surface and capability layers.** Ardizuo's dashboard extends [upstream Claude Map](https://github.com/shamim0902/claude-map); it is not a hosted site or a replacement for Claude Code.


<br />
<br />


## 📥 Check the installed package on Windows


```powershell
npm ls -g claude-map --depth=0
$mapRoot = Join-Path ((npm root -g).Trim()) 'claude-map'
Test-Path (Join-Path $mapRoot 'server.js')
Test-Path (Join-Path $mapRoot 'public/app.js')
python .\scripts\install-dashboard.py --map-root "$mapRoot"
```

The dashboard installer now resolves `npm.cmd` automatically on Windows. The explicit `--map-root` override is useful for diagnostics and for portable/test installations.

The **default mode is read-only**. It checks that the package exists and that the initial Development Hub scaffold can be applied (or is already present). **This does not prove compatibility of the remaining four overlay stages.** A mismatch stops with an explanatory error instead of silently modifying files.

Do not use `--apply` until the installed upstream version and all five patches have been reviewed in a disposable installation. Some overlays are version-sensitive; a successful initial preflight alone is insufficient. The current user's installed version is `claude-map@1.2.3`, but the exact custom modifications on that installation are not yet known.


<br />
<br />


## 📄 Rehearse all five stages in a disposable copy


The initial preview checks only the scaffold. The new `--rehearse` mode runs
**all five** overlay scripts against temporary copies of `server.js` and
`public/app.js`. It redirects `HOME`, `USERPROFILE` and `CLAUDE_CONFIG_DIR`
to an isolated temporary folder, so patch-created backups and the optional
agent file cannot change your existing setup.

```powershell
python .\scripts\install-dashboard.py --rehearse
```

For a reliable *fresh-install* compatibility test, use an **unmodified official
Claude Map 1.2.3 archive**, not your already-customized global installation:

```powershell
$testRoot = Join-Path $HOME 'Documents/Ardizuo-Map-Upstream-Test'
if (Test-Path $testRoot) { throw 'Test folder exists. Choose a fresh path.' }
New-Item -ItemType Directory -Path $testRoot | Out-Null
npm pack claude-map@1.2.3 --pack-destination $testRoot
if ($LASTEXITCODE -ne 0) { throw 'npm pack failed' }
tar -xzf (Join-Path $testRoot 'claude-map-1.2.3.tgz') -C $testRoot
if ($LASTEXITCODE -ne 0) { throw 'tar extraction failed' }
python .\scripts\install-dashboard.py --map-root (Join-Path $testRoot 'package') --rehearse
```

`npm pack` downloads the published tarball into that folder and does **not**
reinstall or overwrite your live dashboard. When the current dashboard has
already been modified, the rehearsal may stop at an already-applied stage;
rehearse the clean archive to test reproducibility.

A successful rehearsal verifies source compatibility and JavaScript syntax,
**not** browser rendering, runtime behavior or external connections. If any
stage fails, **do not run `--apply`**; collect its error output first.


<br />
<br />


## 🔄 Apply only after full compatibility review


Stop the dashboard server. Back up your complete global `claude-map` package, not just `server.js` and `public/app.js`, in case an overlay stage also writes auxiliary files. Then, and only then:

```powershell
python .\scripts\install-dashboard.py --map-root "$mapRoot" --apply
claude-map -p 8888
```

Open <http://localhost:8888/?tab=devhub> and refresh. Keep this dashboard local and on a trusted machine. Some upstream patches can create a missing diagram agent under the active Claude config; install and inspect the Ardizuo local assets first. Never put tokens, private `.claude.json`, settings backups or vault notes into the repository.

The intended UI has the title **AI / Software Engineer Claude Setup**, the five-stage workflow, and status views for agents, skills, commands, hooks, config, vault, plugins and MCPs. Detected/configured does not mean authenticated or successfully executed.

[Full setup](../../docs/installation/full-setup.md) · [Architecture](../../docs/architecture.md) · [Security](../../SECURITY.md)
