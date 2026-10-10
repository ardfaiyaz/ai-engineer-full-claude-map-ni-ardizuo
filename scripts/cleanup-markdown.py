#!/usr/bin/env python3
"""Audit, then optionally replace legacy Markdown SVG icons with emoji.

Repository source only. Deliberately never touches ~/.claude, vault notes outside
this checkout, provider credentials, or the external dashboard package.

Preview is read-only. --apply changes only tracked/documentation markdown,
retired release handoff notes, and known presentation-only SVG directories.
"""
import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEGACY_HANDOFFS = (
    'DASHBOARD-REHEARSAL-READ-ME.md',
    'DASHBOARD-WINDOWS-FIX-README.md',
    'HOTFIX-README.md',
    'SPRINT-2-READ-ME.md',
    'SPRINT-3-READ-ME.md',
    'SPRINT-4-READ-ME.md',
    'SPRINT-5-READ-ME.md',
    'SPRINT-6-READ-ME.md',  # May exist in uncommitted Sprint 6 work.
)
PRESENTATION_FOLDERS = (
    'ardizuo-plugin/assets/lucide',
    'docs/assets/lucide',
    'docs/assets/icons',
    'global-config/assets/lucide',
    'vault/.ardizuo-icons',
)
EMOJI = {
    'alert-triangle': '⚠️', 'blocks': '🧩', 'book-open': '📖',
    'bot': '🤖', 'check-circle-2': '✅', 'circle-help': '❓',
    'clipboard-list': '📋', 'command': '⌨️', 'database': '🗄️',
    'download': '📥', 'file-text': '📄', 'folder-open': '📁',
    'git-branch': '🌿', 'key-round': '🔑', 'layers': '🗂️',
    'list-checks': '☑️', 'monitor': '🖥️', 'notebook-pen': '📝',
    'package': '📦', 'plug': '🔌', 'puzzle': '🧩',
    'rocket': '🚀', 'search-check': '🔎', 'settings-2': '⚙️',
    'shield-check': '🛡️', 'terminal': '💻', 'workflow': '🔄',
    'wrench': '🛠️', 'broom': '🧹',
    # Original README-only Lucide set, also presentation-only.
    'book': '📖', 'network': '🌐', 'shield': '🛡️',
    'compass':'🧭', 'node':'🟩', 'snake':'🐍', 'whale':'🐳', 'penguin':'🐧', 'hook':'🪝', 'flask':'🧪',
}
TAG = re.compile(r'<img\s+[^>]*?\bsrc=["\'](?P<src>[^"\']+)["\'][^>]*>', re.I)
MD_IMAGE = re.compile(r'!\[[^\]\n]*\]\((?P<src>[^)]+\.svg)\)')
ICON_PATH = re.compile(r'(?:^|/)(?:assets/(?:lucide|icons)|\.ardizuo-icons)/([\w-]+)\.svg$', re.I)
FENCE = re.compile(r'^\s*(`{3,}|~{3,})')
# Legacy help paragraphs were written for SVGs installed into ~/.claude/vault.
TEXT_REPLACEMENTS = (
    ('plus local Lucide icon assets', 'with emoji headings'),
    ('and local Lucide icon assets', 'and emoji headings'),
    ('and local icons', 'and emoji headings'),
    ('plus local icons', 'plus emoji headings'),
    ('Lucide-style SVG icon assets', 'emoji headings'),
    ('Lucide-style SVGs', 'emojis'),
    ('local Lucide SVGs', 'emojis'),
    ('Lucide presentation assets', 'emoji headings'),
    ('Lucide icon assets', 'emoji headings'),
    ('local Lucide assets', 'emoji headings'),
    ('local Lucide icons', 'emojis'),
    ('Lucide-style icons', 'emojis'),
    ('Lucide icons', 'emojis'),
    ('Lucide SVGs', 'emojis'),
    ('Lucide SVG', 'emoji'),
    ('local icon assets', 'emoji headings'),
    ('and local icon assets', 'and emoji headings'),
    ('plus local icon assets', 'plus emoji headings'),
    ('icon-styled headings', 'emoji headings'),
)

def emoji_for(src: str):
    match = ICON_PATH.search(src.replace('\\', '/'))
    if not match:
        return None
    if match.group(1) not in EMOJI:
        raise ValueError('Unknown presentation icon: ' + src)
    return EMOJI[match.group(1)]

def transform(text: str):
    """Replace presentation SVG tags outside fenced blocks; keep real images."""
    lines = text.splitlines(keepends=True)
    in_fence = False
    fence_char = None
    for i, line in enumerate(lines):
        m = FENCE.match(line)
        if m:
            marker = m.group(1)
            if not in_fence:
                in_fence, fence_char = True, marker[0]
            elif marker[0] == fence_char:
                in_fence, fence_char = False, None
            continue
        if in_fence:
            continue
        def replace_tag(m):
            emoji = emoji_for(m.group('src'))
            return emoji if emoji else m.group(0)
        def replace_md(m):
            emoji = emoji_for(m.group('src'))
            return emoji if emoji else m.group(0)
        new = TAG.sub(replace_tag, line)
        new = MD_IMAGE.sub(replace_md, new)
        for old, replacement in TEXT_REPLACEMENTS:
            new = new.replace(old, replacement)
        lines[i] = new
    return ''.join(lines)

def transform_document(path: Path, text: str):
    text = transform(text)
    if path.as_posix() == 'THIRD_PARTY_NOTICES.md':
        # The ISC attribution block is removed only because the project stops
        # distributing these presentation SVGs. Do not change other notices.
        text = re.sub(r'(?ms)^\n*## 📄 Lucide icon attribution\s*\n.*?(?=^## |\Z)', '\n', text)
    return text

def plan(root: Path):
    changes = {}
    for file in sorted(root.rglob('*.md')):
        if '.git' in file.parts or file.is_symlink():
            continue
        if file.name in LEGACY_HANDOFFS and file.parent == root:
            continue
        original = file.read_bytes()
        text = original.decode('utf-8-sig')
        changed = transform_document(file.relative_to(root), text)
        if changed != text:
            bom = original[:3] if original.startswith(b'\xef\xbb\xbf') else b''
            changes[file] = bom + changed.encode('utf-8')
    retired = [root/n for n in LEGACY_HANDOFFS if (root/n).is_file() and not (root/n).is_symlink()]
    images = []
    for folder in PRESENTATION_FOLDERS:
        base = root/folder
        if base.is_dir() and not base.is_symlink():
            images.extend(p for p in sorted(base.glob('*.svg')) if p.is_file() and not p.is_symlink() and p.stem in EMOJI)
            unrecognized = [p.name for p in base.iterdir() if p.is_file() and p.suffix == '.svg' and p.stem not in EMOJI]
            if unrecognized:
                raise ValueError(f'Unknown SVG in {folder}; no deletions allowed: {unrecognized}')
    return changes, retired, images

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--apply',action='store_true',help='Replace Markdown presentation SVGs with emojis and retire known handoff/icon files')
    p.add_argument('--check',action='store_true',help='Return nonzero if cleanup is still required (CI verification)')
    args=p.parse_args(argv)
    if args.apply and args.check:
        p.error('--apply and --check cannot be combined')
    modified, retired, images = plan(ROOT)
    print(f'Markdown to update: {len(modified)}; obsolete handoff notes: {len(retired)}; presentation SVGs: {len(images)}')
    for file in retired:print('  RETIRE note:',file.name)
    if args.check:
        return 2 if modified or retired or images else 0
    if not args.apply:
        print('PREVIEW ONLY: no files modified. Run with --apply after reviewing the plan.')
        return 0
    # Validate the transformed docs before touching disk: no icon reference should survive.
    for file, content in modified.items():
        text = content.decode('utf-8-sig')
        for tag in TAG.finditer(text):
            if emoji_for(tag.group('src')) is not None:
                raise ValueError('An icon would remain: '+str(file))
    for file, content in modified.items():file.write_bytes(content)
    for file in retired + images:file.unlink()
    # Remove presentation-only directories if empty, bottom-up; leave unrelated files alone.
    for folder in PRESENTATION_FOLDERS:
        current=ROOT/folder
        while current != ROOT and current.is_dir():
            try:current.rmdir()
            except OSError:break
            current=current.parent
    print('Applied. Existing skills, agents, commands, rules, hooks and settings are not removed.')
    return 0

if __name__=='__main__':sys.exit(main())
