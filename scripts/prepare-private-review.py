#!/usr/bin/env python3
"""Prepare a PRIVATE candidate export of missing direct-scope definitions.

Do not publish this directory. A local definition may have been downloaded from
someone else, have incompatible licenses, include private paths, or embed secrets.
No plugin caches, auth, sessions, settings, vault notes, or transcripts are read.
"""
import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = json.loads((ROOT/'setup/reference-inventory.json').read_text(encoding='utf-8'))
OWN = set(json.loads((ROOT/'setup/development-assets.json').read_text(encoding='utf-8'))['filePaths'])


def candidates(config):
    for folder, entries in (('agents', REF['agents']), ('skills', REF['globalSkills']), ('commands', REF['commands'])):
        for name in entries:
            if '/' in name or '\\' in name or name in ('.', '..'):
                raise ValueError('Untrusted inventory name')
            if folder == 'skills':
                rel = Path(folder)/name/'SKILL.md'
                origins = [config/rel]
            elif folder == 'commands':
                # Include namespaced SuperClaude commands only when their name matches.
                origins = sorted((config/folder).rglob(name+'.md')) if (config/folder).is_dir() else []
                origins = [p for p in origins if len(p.relative_to(config/folder).parts) <= 3]
            else:
                rel = Path(folder)/(name+'.md')
                origins = [config/rel]
            for source in origins:
                if not source.is_file() or source.is_symlink(): continue
                rel = source.relative_to(config)
                if rel.as_posix() in OWN: continue
                yield rel, source


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config-dir',type=Path,default=Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude'))
    p.add_argument('--output',type=Path,default=Path.home()/'Documents/Ardizuo-Additional-Assets-PRIVATE')
    p.add_argument('--apply',action='store_true',help='Copy selected source into private review location; default only lists names')
    args=p.parse_args()
    config=args.config_dir.expanduser().resolve()
    target=args.output.expanduser().resolve()
    if target == config or target.is_relative_to(config) or target == ROOT or target.is_relative_to(ROOT) or config.is_relative_to(target):
        raise ValueError('Private export must be outside Claude config and public project.')
    if target.exists():
        raise ValueError('Private review output already exists; choose a new empty path. No overwrites permitted.')
    originals=list(candidates(config))
    print('PRIVATE SOURCE REVIEW. Never push this staging folder to GitHub.')
    print('Candidate files:',len(originals))
    for rel,_ in originals: print('  ',rel.as_posix())
    print('Origin and license NOT verified. Review each file; redact paths and secrets; do not redistribute third-party code without permission.')
    if not args.apply:
        print('DRY RUN. Add --apply to copy candidates into the private review location.')
        return
    # Files may be extremely sensitive. Do not make a ZIP, do not upload, do not commit.
    for rel, src in originals:
        dst=target/rel
        dst.parent.mkdir(parents=True,exist_ok=True)
        with dst.open('xb') as out: out.write(src.read_bytes())
    print('Copied candidates into a PRIVATE local folder; inspect/redact manually before sharing anything.')

if __name__=='__main__':main()
