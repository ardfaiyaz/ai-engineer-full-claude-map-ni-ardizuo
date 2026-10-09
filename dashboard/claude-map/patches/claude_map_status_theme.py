#!/usr/bin/env python3
"""Windows-safe, idempotent theme update for the existing Claude Map Development Hub.

Scope: Claude Map public/app.js ONLY. No Claude Code config, vault, MCP settings,
credentials, skills, hooks, agents or projects are written.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import os
from pathlib import Path
import shutil
import subprocess
import sys

TITLE = 'AI / Software Engineer Claude Setup'
MARKER = '/* BEGIN DEVELOPMENT HUB STATUS PALETTE V1 */'
OLD_TITLE = '<h1>Developer Orchestration</h1>'
NEW_TITLE = f'<h1>{TITLE}</h1>'
LOADING_TITLE_OLD = '<h1>Development System</h1>'
LOADING_TITLE_NEW = f'<h1>{TITLE}</h1>'
STYLE_ANCHOR = ' </style><div class="mh-shell">'

STATUS_CSS = r''' /* BEGIN DEVELOPMENT HUB STATUS PALETTE V1 */
 /* Base: monochrome panels; semantic colors are reserved for real status. */
 .mh-shell {
   --mh-bg: #0c0d10;
   --mh-panel: #15171b;
   --mh-panel2: #202329;
   --mh-border: #32353c;
   --mh-fg: #f4f5f7;
   --mh-muted: #aeb4bd;
   --mh-dim: #929aa6;
   --mh-success: #67dca3;
   --mh-danger: #ff858b;
   --mh-info: #a4b9ff;
   --mh-related: #80d0e1;
   --mh-amber: #e9c37d;
 }
 .mh-shell .mh-layer,
 .mh-shell .mh-card {
   background: var(--mh-panel);
   border-color: var(--mh-border);
   box-shadow: 0 1px 0 rgba(255,255,255,.018);
 }
 .mh-shell .mh-stage {
   background: #0f1013;
   border-color: #373b43;
   transition: border-color .16s ease, background .16s ease;
 }
 .mh-shell .mh-stage:hover {
   border-color: #9da4af;
   background: #1b1e23;
 }
 .mh-shell .mh-stage.active {
   border-color: #e7eaf0;
   background: #292c32;
   box-shadow: inset 0 2px 0 #e7eaf0;
 }
 .mh-shell .mh-stage:focus-visible {
   outline: 2px solid var(--mh-info);
   outline-offset: 2px;
 }
 .mh-shell .mh-chip {
   background: #111317;
   color: #ecedf0;
   border: 1px solid #42464e;
   opacity: 1;
   border-radius: 5px;
   transition: background .16s ease, border-color .16s ease;
 }
 .mh-shell .mh-chip span { color: #aeb4bd; }
 /* Detected / existing file / enabled plugin: verified local inventory. */
 .mh-shell .mh-chip.mh-installed,
 .mh-shell .mh-chip.mh-file {
   color: #d6f6e4;
   background: rgba(54,172,112,.105);
   border-color: #397e58;
   border-style: solid;
 }
 .mh-shell .mh-chip.mh-installed span,
 .mh-shell .mh-chip.mh-file span { color: var(--mh-success); }
 /* Missing is visually obvious, never faded or hidden. */
 .mh-shell .mh-chip.mh-missing {
   color: #ffdadd;
   background: rgba(208,61,77,.115);
   border: 1px dashed #98505a;
   opacity: 1;
 }
 .mh-shell .mh-chip.mh-missing span { color: var(--mh-danger); }
 /* Native Claude Code command: available but not a local skill file. */
 .mh-shell .mh-chip.mh-builtin {
   color: #e4e8ff;
   background: rgba(104,119,212,.10);
   border: 1px dashed #6c78ad;
 }
 .mh-shell .mh-chip.mh-builtin span { color: var(--mh-info); }
 /* A related service/skill is not the exact named skill. */
 .mh-shell .mh-chip.mh-alternative,
 .mh-shell .mh-chip.mh-service {
   color: #d5f4f7;
   background: rgba(59,160,182,.095);
   border: 1px dotted #468596;
 }
 .mh-shell .mh-chip.mh-alternative span,
 .mh-shell .mh-chip.mh-service span { color: var(--mh-related); }
 /* An alternative local skill deserves its own warning/alternative color. */
 .mh-shell .mh-chip.mh-local,
 .mh-shell .mh-chip.mh-unknown {
   color: #fff0d4;
   background: rgba(192,138,51,.10);
   border: 1px dotted #92713d;
 }
 .mh-shell .mh-chip.mh-local span,
 .mh-shell .mh-chip.mh-unknown span { color: var(--mh-amber); }
 /* Registered MCP is not necessarily connected: stay neutral until checked. */
 .mh-shell .mh-chip.mh-configured {
   color: #e2e7ed;
   background: rgba(139,151,169,.085);
   border-color: #58616e;
 }
 .mh-shell .mh-chip.mh-configured span { color: #bac6d4; }
 .mh-shell .mh-evidence .mh-evidence-pass strong,
 .mh-shell .mh-evidence .mh-evidence-pass span { color: var(--mh-success); }
 .mh-shell .mh-evidence .mh-evidence-fail strong,
 .mh-shell .mh-evidence .mh-evidence-fail span { color: var(--mh-danger); }
 .mh-shell .mh-ship { border-color: #49505b; background: #191d22; }
 .mh-shell h1 { font-size: 25px; letter-spacing: -.7px; }
 .mh-shell .mh-eyebrow { color: #c3c9d2; }
 /* END DEVELOPMENT HUB STATUS PALETTE V1 */
'''


def replace_exact_once(s: str, old: str, new: str, label: str) -> str:
    count = s.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected one insertion point; found {count}. No changes made.')
    return s.replace(old, new, 1)


def find_map(explicit: Path | None) -> Path:
    if explicit:
        return explicit
    if os.environ.get('CLAUDE_MAP_ROOT'):
        return Path(os.environ['CLAUDE_MAP_ROOT'])
    try:
        result = subprocess.run(['npm.cmd' if os.name == 'nt' else 'npm', 'root', '-g'],
                                capture_output=True, text=True, check=True, timeout=15)
        return Path(result.stdout.strip()) / 'claude-map'
    except (OSError, subprocess.SubprocessError):
        return Path.home() / 'AppData' / 'Roaming' / 'npm' / 'node_modules' / 'claude-map'


def main() -> int:
    parser = argparse.ArgumentParser(description='Rename and color the Claude Map Development Hub.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--dry-run', action='store_true', help='Check compatibility, no changes')
    group.add_argument('--apply', action='store_true', help='Back up then apply patch')
    parser.add_argument('--map-root', type=Path, help='Optional explicit Claude Map root (for testing)')
    args = parser.parse_args()

    map_root = find_map(args.map_root)
    target = map_root / 'public' / 'app.js'
    if not target.is_file():
        raise RuntimeError(f'Claude Map frontend was not found: {target}')
    source = target.read_text(encoding='utf-8')
    if 'function renderDevelopmentHub()' not in source or 'BEGIN MINIMAL DEV SYSTEM HUB V2' not in source:
        raise RuntimeError('Expected existing Development Hub was not detected; nothing modified.')
    if MARKER in source:
        print('Already applied. No changes made.')
        return 0

    changed = replace_exact_once(source, OLD_TITLE, NEW_TITLE, 'Hub title')
    if LOADING_TITLE_OLD in changed:
        changed = replace_exact_once(changed, LOADING_TITLE_OLD, LOADING_TITLE_NEW, 'Loading title')

    # Keep related capabilities distinguishable (local alternative != external service).
    chip_anchor = " const chip=n=>{const [state,desc]=status(n);\n"
    chip_new = (chip_anchor +
        "   const shade=state==='alternative'\n"
        "     ? (desc==='Via local skill' ? ' mh-local' : ' mh-service') : '';\n")
    changed = replace_exact_once(changed, chip_anchor, chip_new, 'Skill status color')
    changed = replace_exact_once(changed,
        'class="mh-chip mh-${state}" title="${safe(desc)}"',
        'class="mh-chip mh-${state}${shade}" title="${safe(desc)}"',
        'Skill chip renderer')

    # Configured user MCPs are not marked green until actual connection verification.
    changed = replace_exact_once(changed,
        'const allMcps=(inv.mcp||[]).map(x=>`<span class="mh-chip mh-installed">',
        'const allMcps=(inv.mcp||[]).map(x=>`<span class="mh-chip mh-configured">',
        'Configured MCP visual state')
    # Unknown is amber, rather than implying an actual failed connection.
    changed = replace_exact_once(changed,
        "x.status==='Connected'?'mh-installed':'mh-missing'",
        "x.status==='Connected'?'mh-installed':x.status==='Unavailable'?'mh-missing':'mh-unknown'",
        'Live MCP status')
    # Recorded checks are colored only according to the actual recorded exit code.
    changed = replace_exact_once(changed,
        'evidence.map(x=>`<div><strong>${safe(x.check)}</strong>',
        'evidence.map(x=>`<div class="${x.exitCode===0?\'mh-evidence-pass\':\'mh-evidence-fail\'}"><strong>${safe(x.check)}</strong>',
        'Ship evidence color')
    changed = replace_exact_once(changed, STYLE_ANCHOR,
                                 STATUS_CSS + STYLE_ANCHOR, 'Scoped palette CSS')

    if args.dry_run:
        print('DRY RUN PASSED (no changes).')
        print('Target:', target)
        print('Will set heading to:', TITLE)
        print('Will color detected=green, missing=red, built-in=lavender, related=cyan, local alternative=amber.')
        print('Registered MCPs stay neutral until live connection status is checked.')
        return 0

    backup = Path.home() / ('claude-map-status-theme-backup-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
    backup.mkdir(parents=True, exist_ok=False)
    shutil.copy2(target, backup / 'app.js')
    temp = target.with_name(f'app.js.theme-pending-{os.getpid()}')
    try:
        temp.write_text(changed, encoding='utf-8')
        os.replace(temp, target)
        check = subprocess.run(['node', '--check', str(target)], capture_output=True,
                               text=True, timeout=30)
        if check.returncode:
            raise RuntimeError('JavaScript syntax check failed:\n' + check.stderr)
    except Exception:
        if temp.exists():
            temp.unlink()
        shutil.copy2(backup / 'app.js', target)
        print('Patch failed. Previous app.js restored from backup.')
        raise
    print('SUCCESS: Development Hub title and semantic color theme applied.')
    print('JavaScript syntax: PASS')
    print('Backup:', backup)
    print('File changed:', target)
    print('Restart Claude Map and hard-refresh the browser.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print('ERROR:', exc, file=sys.stderr)
        sys.exit(1)
