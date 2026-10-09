#!/usr/bin/env python3
"""Safely add a diagrams specialist and honest video-plugin labels to Claude Map.

Windows / Python 3.8+. Only writes a single agent markdown file and Claude Map
public/app.js. Doesn't install or authenticate any external provider plugins.
"""
import argparse
import datetime as dt
import os
from pathlib import Path
import shutil
import subprocess
import sys

AGENT = '''---
name: diagram-architect
description: Read-only specialist for Mermaid diagrams, architecture maps, sequence flows, data models, and system component relationships grounded in repository evidence. Use when diagrams improve development planning or documentation.
tools: Read, Glob, Grep
model: inherit
---

# Diagram Architect

You create **accurate technical diagrams** of software projects. Prefer Mermaid
flowcharts, sequence diagrams, state diagrams, ERDs and C4-style component
maps where the format is supported. Do not invent architecture or imply a
connection exists without repository evidence.

## Process

1. Inspect the relevant files and existing project docs using Read/Glob/Grep.
2. List components and interactions, separating confirmed from assumed edges.
3. Produce Mermaid source that is short, syntactically plausible and readable.
4. Give a legend and source-file references for nontrivial architecture claims.
5. Flag unknown interactions and questions rather than fabricating them.
6. Do not edit source files, configure services, commit, push or deploy.
7. To save a diagram to an Obsidian vault, first show the complete proposed
   Markdown and destination, then request explicit user approval. You have no
   writing tools and must leave saving to an approved follow-up workflow.

Use this agent for software-development diagrams only. No social media
workflows, promotion, or publishing automations.
'''

ROLE_OLD = "['product','requirements-analyst'],['diagrams','']"
ROLE_NEW = "['product','requirements-analyst'],['diagrams','diagram-architect']"
PLUGIN_ANCHOR = "// Honest equivalent labels; do not claim these video skill names are installed."
PLUGIN_MAPPING = """// Video-reference labels for related, official enabled plugins.
// A related plugin is not proof that the original skill name exists.
const DEV_RELATED_PLUGIN = {
 'expo:deployment':'expo',
 'stripe:best-practices':'stripe',
 'sentry:sentry-workflow':'sentry',
 'atlassian:triage-issue':'atlassian',
 'Notion:search':'notion'
};
"""
SET_ANCHOR = " const mcps=new Set((inv.mcp||[]).map(x=>x.name.toLowerCase()));"
SET_REPLACE = SET_ANCHOR + "\n const enabledPlugins=new Set((inv.enabledPlugins||[]).map(x=>x.toLowerCase().split('@')[0]));"
STATUS_ANCHOR = "   if (provider && mcps.has(provider.toLowerCase())) return ['alternative','Via '+provider+' MCP'];"
STATUS_REPLACE = STATUS_ANCHOR + "\n   const plugin=DEV_RELATED_PLUGIN[n];\n   if (plugin && enabledPlugins.has(plugin)) return ['alternative','Via '+plugin+' plugin'];"
BUILTIN_OLD = "if (builtin.has(name)) return ['builtin','Built-in*'];"
BUILTIN_NEW = "if (builtin.has(name)) return ['builtin','Claude built-in'];"
LEGEND_OLD = 'Built-in* = previously seen in Claude CLI; verify in /skills.'
LEGEND_NEW = 'Claude built-in = native Claude Code command (not a SKILL.md); verify in the slash-command menu.'


def locate_map():
    env = os.environ.get('CLAUDE_MAP_ROOT')
    if env:
        return Path(env)
    try:
        r = subprocess.run(['npm.cmd' if os.name == 'nt' else 'npm', 'root', '-g'],
                           capture_output=True, text=True, check=True, timeout=12)
        return Path(r.stdout.strip()) / 'claude-map'
    except (OSError, subprocess.SubprocessError):
        return Path.home() / 'AppData' / 'Roaming' / 'npm' / 'node_modules' / 'claude-map'


def replace_one(src, old, new, what):
    # A completed insertion still contains its anchor. Check the expanded
    # replacement first so repeated runs are truly idempotent.
    if new in src:
        return src
    count = src.count(old)
    if count == 1:
        return src.replace(old, new, 1)
    raise RuntimeError(f'{what}: expected one known marker, found {count}. No files changed.')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--apply', action='store_true')
    p.add_argument('--map-root', type=Path, help='optional, for local tests')
    p.add_argument('--claude-dir', type=Path, help='optional, for local tests')
    args = p.parse_args()
    if args.dry_run and args.apply:
        p.error('Use either --dry-run or --apply')
    map_root = args.map_root or locate_map()
    claude_dir = args.claude_dir or Path.home() / '.claude'
    app_path = map_root / 'public' / 'app.js'
    agent_path = claude_dir / 'agents' / 'diagram-architect.md'
    if not app_path.is_file():
        raise RuntimeError('Claude Map not found at: ' + str(app_path))
    src = app_path.read_text(encoding='utf-8')
    # Ensure this is the minimal Development Hub already installed.
    if 'function renderDevelopmentHub()' not in src or 'const VIDEO_ROLES' not in src:
        raise RuntimeError('Expected minimal Development Hub missing. Do not patch this version.')
    changed = src
    changed = replace_one(changed, ROLE_OLD, ROLE_NEW, 'diagrams role mapping')
    changed = replace_one(changed, PLUGIN_ANCHOR, PLUGIN_MAPPING + PLUGIN_ANCHOR, 'plugin mapping')
    changed = replace_one(changed, SET_ANCHOR, SET_REPLACE, 'enabled plugin set')
    changed = replace_one(changed, STATUS_ANCHOR, STATUS_REPLACE, 'plugin status check')
    changed = replace_one(changed, BUILTIN_OLD, BUILTIN_NEW, 'native built-in label')
    changed = replace_one(changed, LEGEND_OLD, LEGEND_NEW, 'built-in legend')
    if agent_path.exists():
        print('Existing agent preserved:', agent_path)
    else:
        print('New read-only diagram agent:', agent_path)
    if args.dry_run or not args.apply:
        print('PREVIEW: Claude Map frontend:', app_path)
        print('Frontend patch needed:', changed != src)
        print('No changes made. Use --apply to install.')
        return 0
    if changed == src and agent_path.exists():
        print('Already installed; no changes made.')
        return 0
    backup = Path.home() / ('claude-map-integrations-backup-' + dt.datetime.now().strftime('%Y%m%d-%H%M%S'))
    backup.mkdir(parents=True, exist_ok=False)
    shutil.copy2(app_path, backup / 'app.js')
    original_agent = agent_path.read_bytes() if agent_path.exists() else None
    if original_agent is not None:
        (backup / 'diagram-architect.md').write_bytes(original_agent)
    try:
        if changed != src:
            # Preserve UTF-8 content and replace file atomically.
            tmp = app_path.with_name('app.js.pending-' + str(os.getpid()))
            try:
                tmp.write_text(changed, encoding='utf-8')
                os.replace(tmp, app_path)
            finally:
                if tmp.exists():
                    tmp.unlink()
        if not agent_path.exists():
            agent_path.parent.mkdir(parents=True, exist_ok=True)
            agent_path.write_text(AGENT, encoding='utf-8')
        result = subprocess.run(['node', '--check', str(app_path)], capture_output=True, text=True, timeout=20)
        if result.returncode != 0:
            raise RuntimeError('node --check failed: ' + result.stderr)
    except Exception:
        shutil.copy2(backup / 'app.js', app_path)
        if original_agent is None and agent_path.exists():
            agent_path.unlink()
        elif original_agent is not None:
            agent_path.write_bytes(original_agent)
        print('Validation failed: original files restored.')
        raise
    print('SUCCESS: Diagram specialist installed/mapped; plugin-equivalence checks added.')
    print('Backup:', backup)
    print('Frontend JS syntax: PASS')
    print('Install provider plugins separately; not installed by this script.')
    print('Restart Claude Code and Claude Map, then hard refresh your browser.')
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print('ERROR:', e, file=sys.stderr)
        sys.exit(1)
