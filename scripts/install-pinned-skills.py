#!/usr/bin/env python3
"""Install only publisher-pinned, hash-verified SKILL.md definitions.

Dry-run is offline. --apply explicitly fetches public sources, verifies Git blob
checksums, and creates ONLY absent files. No global config is read for secrets.
A single SKILL.md is NOT proof that its optional sidecars/dependencies work.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / 'setup/source-provenance-lock.json'
CANDIDATES = ROOT / 'setup/skill-source-candidates.json'
SOURCE_LIMIT = 1024 * 1024
TOTAL_LIMIT = 8 * 1024 * 1024
# Explicit publisher allowlist; changes to this require repository code review.
PUBLISHERS = {
    'bencium/bencium-marketplace': '5de46a39b4640fa419560cd0b67e4c4b50dac802',
    'nextlevelbuilder/ui-ux-pro-max-skill': '50d8a7de0900119855614541f15a1a616691eb33',
    'vercel-labs/skills': '13e4063a1cf913f5606d57d42ab83a86f5001e04',
    'pbakaus/impeccable': 'd631a8827f99414d2b6daba4ef08b7f8701751d7',
    'supabase/agent-skills': 'c9be0e931b7930f7d02126d04774d904c381e7d7',
    'vercel-labs/agent-skills': '063bee94c3f4df8453406c830b0a7df0f2860278',
    'emilkowalski/skills': 'e8a175de22ae1e49370fc144c1f3bb9aeedf988d',
    'addyosmani/agent-skills': '1401c8b8030e023baeebb31781a6653fe8e93026',
    'vitalics/playwright-labs': 'be116c4523b1adf403cef3b7dc71f5e01d842d3a',
    'dominika-zajac/better-frontend-skills': '92cdb7e73323f6d627dbab0462e94ba8786f3264',
}


def blob_sha(body):
    return hashlib.sha1(b'blob ' + str(len(body)).encode('ascii') + b'\0' + body).hexdigest()


def normalize_eol(body):
    # Normalizes CRLF only; do not silently change any other content.
    return body.replace(b'\r\n', b'\n')


def safe_name(target):
    if not isinstance(target, str) or '\\' in target or ':' in target or target.startswith('/'):
        raise ValueError('Invalid skill target')
    pieces=target.split('/')
    if len(pieces)!=3 or pieces[0]!='skills' or pieces[2]!='SKILL.md' or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,90}', pieces[1]):
        raise ValueError('Unsafe skill target')
    return Path(*pieces)


def selected_rows(lock, include_variants=False):
    all_skills=[r for r in lock['entries'] if r['target'].startswith('skills/')]
    if len(all_skills)!=29 or len({r['target'].casefold() for r in all_skills})!=29:
        raise ValueError('Unexpected reference skill count or duplicate targets')
    chosen=[]
    for row in all_skills:
        policy=row['installPolicy']
        if policy not in ('automatic-reviewed-upstream', 'opt-in-upstream-variant'):
            if policy!='manual-source-review':raise ValueError('Unexpected skill policy')
            continue
        if policy=='opt-in-upstream-variant' and not include_variants: continue
        rel=safe_name(row['target'])
        repository=row.get('upstreamRepository')
        revision=row.get('revision')
        source=row.get('sourceFilePath')
        if repository not in PUBLISHERS or revision!=PUBLISHERS[repository]:
            raise ValueError('Unreviewed publisher or revision: '+str(repository))
        parts=PurePosixPath(source).parts if isinstance(source,str) else ()
        if not parts or any(x in ('..','.','') for x in parts) or '\\' in source or ':' in source or source.startswith('/'):
            raise ValueError('Invalid upstream skill path')
        # Sources may have a publisher-dependent directory, but must be a SKILL.md
        # under a folder with the same basename (or an explicitly reviewed alias).
        reviewed_aliases={'vercel-composition-patterns':'composition-patterns','vercel-react-best-practices':'react-best-practices'}
        if len(parts)<2 or parts[-1]!='SKILL.md' or parts[-2]!=reviewed_aliases.get(rel.parts[1],rel.parts[1]):
            raise ValueError('Unreviewed source-to-target mapping')
        if not re.fullmatch(r'[a-f0-9]{40}',row.get('gitBlobSHA1','')):
            raise ValueError('Missing immutable Git blob hash')
        expected_comparison = ('DIFFERENT_CONTENT' if policy=='opt-in-upstream-variant' else row['comparison'])
        if policy=='automatic-reviewed-upstream' and expected_comparison not in ('EXACT_BYTE_MATCH','TEXT_MATCH_LINE_ENDINGS_ONLY'):
            raise ValueError('Only locally compared skill definitions may be automatic')
        if policy=='opt-in-upstream-variant' and row['comparison']!='DIFFERENT_CONTENT':
            raise ValueError('Variants only for known differing sources')
        chosen.append((row, rel))
    if len(chosen)!=(25 if include_variants else 20):
        raise ValueError('Review required: skill policy counts unexpectedly changed')
    return chosen


def safe_target(config,relative):
    current=config
    if current.is_symlink():raise ValueError('Config is a symlink')
    for part in relative.parts:
        current=current/part
        if current.is_symlink():raise ValueError('Target path contains symlink')
    return current


def matching_local(body,row):
    if blob_sha(body)==row['gitBlobSHA1']:return True
    # We cannot normalize to a hash, so only use this form to compare a newly
    # downloaded upstream file against the existing file in execute().
    return False


def make_plan(config,chosen,reference_bytes=None):
    result=[]
    for row,rel in chosen:
        dest=safe_target(config,rel)
        if not dest.exists():state='new'
        elif not dest.is_file():state='CONFLICT'
        elif matching_local(dest.read_bytes(),row):state='identical'
        elif row['comparison']=='TEXT_MATCH_LINE_ENDINGS_ONLY' and reference_bytes is not None and row['target'] in reference_bytes and normalize_eol(dest.read_bytes())==normalize_eol(reference_bytes[row['target']]):state='identical-line-endings'
        else:state='CONFLICT'
        result.append((row,rel,dest,state))
    return result


def fetch_source(row,timeout=25):
    segments=[urllib.parse.quote(p,safe='') for p in PurePosixPath(row['sourceFilePath']).parts]
    url='https://raw.githubusercontent.com/{}/{}/{}'.format(row['upstreamRepository'],row['revision'],'/'.join(segments))
    request=urllib.request.Request(url,headers={'User-Agent':'Ardizuo-Skill-Pins/1.0','Accept':'text/plain'})
    with urllib.request.urlopen(request,timeout=timeout) as resp:
        body=resp.read(SOURCE_LIMIT+1)
    if len(body)>SOURCE_LIMIT:raise ValueError('Skill exceeds source size limit: '+row['target'])
    if blob_sha(body)!=row['gitBlobSHA1']:raise ValueError('Publisher checksum mismatch: '+row['target'])
    return body


def install(config,chosen,apply=False,fetch=fetch_source):
    # Preflight conflicts before any downloads, including mismatching personal skills.
    initial=make_plan(config,chosen)
    for row,rel,_,state in initial:
        detail=" (PUBLISHER VARIANT, differs from author reference)" if row['installPolicy']=='opt-in-upstream-variant' else ''
        print(f'  {state:10} {rel.as_posix()}{detail}')
    if any(s=='CONFLICT' for *_,s in initial):
        raise RuntimeError('Existing skill conflicts. No files downloaded or modified.')
    missing=[(r,p,d) for r,p,d,s in initial if s=='new']
    if not apply:
        print(f'DRY RUN: {len(missing)} pinned skill prompts planned; no downloads or writes.')
        return {'new':len(missing),'identical':len(initial)-len(missing)}
    payloads={};size=0
    for row,rel,dest in missing:
        body=fetch(row)
        if blob_sha(body)!=row['gitBlobSHA1']:raise ValueError('Checksum mismatch: '+row['target'])
        size+=len(body)
        if size>TOTAL_LIMIT:raise ValueError('Total download limit exceeded')
        payloads[row['target']]=body
    # Also support idempotence for CRLF files with known identical text. We
    # compare them only if the remote bytes were fetched previously; without
    # downloaded bytes, refuse ambiguity instead of accepting unknown edits.
    if any(s=='CONFLICT' for *_,s in make_plan(config,chosen)):
        raise RuntimeError('Skill contents changed during downloading. No files written.')
    created=[]
    try:
        for row,rel,dest in missing:
            safe_target(config,rel)
            dest.parent.mkdir(parents=True,exist_ok=True)
            with dest.open('xb') as out:out.write(payloads[row['target']])
            created.append(dest)
            if blob_sha(dest.read_bytes())!=row['gitBlobSHA1']:
                raise RuntimeError('Post-write verification failed: '+row['target'])
    except BaseException:
        for f in reversed(created):f.unlink(missing_ok=True)
        raise
    print(f'INSTALLED: {len(created)} new SKILL.md files; {len(initial)-len(created)} already identical. No overwrites.')
    print('Sidecars not included: Some publishers require scripts, data or CLI setup. Read docs/installation/pinned-skills.md.')
    return {'new':len(created),'identical':len(initial)-len(created)}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config-dir',type=Path,help='Use a new disposable directory first')
    parser.add_argument('--apply',action='store_true',help='Download public files after checksum validation; create files only')
    parser.add_argument('--upstream-variants',action='store_true',help='Explicitly add publisher versions of 5 locally modified skills')
    parser.add_argument('--pending',action='store_true',help='Show the 19 reviewed leads, including 4 unknown sources')
    a=parser.parse_args(argv)
    config=a.config_dir or Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude')
    if config.is_symlink():parser.error('Config must not be a symlink')
    config=config.expanduser().resolve()
    if config==ROOT or config.is_relative_to(ROOT):parser.error('Config may not be inside the public repository')
    lock=json.loads(LOCK.read_text('utf-8'))
    chosen=selected_rows(lock,a.upstream_variants)
    print('Publisher-pinned skills:',len(chosen),'selected; 4 unknown sources excluded; sidecar files not included')
    if a.pending:
        pending=json.loads(CANDIDATES.read_text('utf-8'))['entries']
        for row in pending:print('  '+row['target']+': '+row['status']+((' ('+row['candidateRepository']+')') if row.get('candidateRepository') else ''))
        if not a.apply:return
    install(config,chosen,a.apply)

if __name__=='__main__':
    try:main()
    except Exception as e:
        print('ERROR:',e,file=sys.stderr);sys.exit(1)
