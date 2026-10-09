#!/usr/bin/env python3
"""Install hash-verified, commit-pinned SuperClaude definitions without clobbering user files.

Default is local-only DRY RUN (zero network). --apply is a network opt-in that
fetches approved public sources, validates Git blob SHA-1 and only creates files
when all downloads and conflict checks succeed. No secrets or user notes read.
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
MAX_SOURCE_BYTES = 1024 * 1024
MAX_TOTAL_BYTES = 8 * 1024 * 1024
ALLOWED_REPOSITORY = 'SuperClaude-Org/SuperClaude_Framework'


def git_blob_sha1(content):
    return hashlib.sha1(b'blob ' + str(len(content)).encode('ascii') + b'\0' + content).hexdigest()


def safe_relative(s):
    if not isinstance(s, str) or '\\' in s or s.startswith('/') or ':' in s:
        raise ValueError('Invalid manifest path')
    pure = PurePosixPath(s)
    if not pure.parts or any(p in ('', '.', '..') for p in pure.parts):
        raise ValueError('Unsafe manifest path')
    if pure.parts[0] not in ('agents', 'commands'):
        raise ValueError('Only agents and commands are allowed')
    return Path(*pure.parts)


def allowed_rows(lock, upstream_variants=False, category='all'):
    upstream = lock['upstream']
    if upstream['repository'] != ALLOWED_REPOSITORY or not re.fullmatch(r'[a-f0-9]{40}', upstream['revision']):
        raise ValueError('Unexpected upstream pin; review before use')
    selected=[]
    for row in lock['entries']:
        # Sprint 3 introduces separately reviewed pinned skill entries in the same lock.
        # SuperClaude installer must ignore them rather than treating them as agent paths.
        if not row['target'].startswith(('agents/', 'commands/')):
            continue
        policy=row['installPolicy']
        if policy != 'automatic-reviewed-upstream' and not (upstream_variants and policy=='opt-in-upstream-variant'):
            continue
        relative=safe_relative(row['target'])
        if category != 'all' and relative.parts[0] != category:
            continue
        if row.get('upstreamRepository') != ALLOWED_REPOSITORY or row.get('revision') != upstream['revision']:
            raise ValueError('Unrecognized source in lock file')
        source=row['sourceFilePath']
        expected=('src/superclaude/agents/' if relative.parts[0]=='agents' else 'src/superclaude/commands/') + relative.name
        if source != expected or not re.fullmatch(r'[a-f0-9]{40}', row.get('gitBlobSHA1','')):
            raise ValueError('Unsafe or unverified source definition')
        selected.append((row,relative))
    if len({str(p).casefold() for _,p in selected}) != len(selected):
        raise ValueError('Duplicate output paths in lock')
    return selected


def require_safe_target(config, rel):
    dest = config / rel
    # Don't follow existing symlink directories or files into arbitrary locations.
    current = config
    if current.is_symlink():
        raise ValueError('Claude config is a symlink; refusing')
    for part in rel.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError('Target path contains symlink; refusing')
    return dest


def build_plan(config, entries):
    plan=[]
    for row,rel in entries:
        dest=require_safe_target(config,rel)
        if not dest.exists():status='new'
        elif not dest.is_file():status='CONFLICT'
        elif git_blob_sha1(dest.read_bytes())==row['gitBlobSHA1']:status='identical'
        else:status='CONFLICT'
        plan.append((row,rel,dest,status))
    return plan


def fetch_pinned(row, timeout=20):
    commit=row['revision']
    source='/'.join(urllib.parse.quote(p,safe='') for p in PurePosixPath(row['sourceFilePath']).parts)
    url=f'https://raw.githubusercontent.com/{ALLOWED_REPOSITORY}/{commit}/{source}'
    request=urllib.request.Request(url,headers={'User-Agent':'Ardizuo-Pinned-Installer/1.0','Accept':'text/plain'})
    with urllib.request.urlopen(request,timeout=timeout) as response:
        content=response.read(MAX_SOURCE_BYTES+1)
    if len(content)>MAX_SOURCE_BYTES:
        raise ValueError('Upstream file too large: '+row['target'])
    if git_blob_sha1(content)!=row['gitBlobSHA1']:
        raise ValueError('Upstream checksum mismatch: '+row['target'])
    return content


def execute(config, selected, apply=False, fetch=fetch_pinned):
    plan=build_plan(config,selected)
    for row,rel,dest,state in plan:
        suffix=' (UPSTREAM VERSION, differs from reference machine)' if row['installPolicy']=='opt-in-upstream-variant' else ''
        print(f'  {state:10} {rel.as_posix()}{suffix}')
    if any(state=='CONFLICT' for _,_,_,state in plan):
        raise RuntimeError('Existing files differ. No writes or downloads. Run in a fresh isolated --config-dir.')
    missing=[(row,rel,dest) for row,rel,dest,state in plan if state=='new']
    if not apply:
        print(f'DRY RUN: {len(missing)} files would be fetched and installed, {len(plan)-len(missing)} identical. NO network or writes.')
        return {'new':len(missing),'identical':len(plan)-len(missing)}
    # Download all files first: an upstream outage/checksum failure cannot cause a partial install.
    downloaded=[];total=0
    for row,rel,dest in missing:
        body=fetch(row)
        if git_blob_sha1(body)!=row['gitBlobSHA1']:
            raise ValueError('Hash mismatch for '+rel.as_posix())
        total+=len(body)
        if total>MAX_TOTAL_BYTES:raise ValueError('Combined downloads exceed size limit')
        downloaded.append((row,rel,dest,body))
    # Check again after potentially slow downloads. No existing file is overwritten.
    if any(state=='CONFLICT' for _,_,_,state in build_plan(config,selected)):
        raise RuntimeError('Targets changed while downloading; no writes made')
    created=[]
    try:
        for row,rel,dest,body in downloaded:
            require_safe_target(config,rel)
            dest.parent.mkdir(parents=True,exist_ok=True)
            with dest.open('xb') as f:
                f.write(body)
            created.append(dest)
            if git_blob_sha1(dest.read_bytes())!=row['gitBlobSHA1']:
                raise RuntimeError('File failed post-write verification: '+rel.as_posix())
    except BaseException:
        for target in reversed(created):target.unlink(missing_ok=True)
        raise
    print(f'INSTALLED: {len(created)} verified upstream files; {len(plan)-len(created)} already identical. No overwrite.')
    print('These are static definitions; Claude runtime behavior and SuperClaude CLI features are not verified here.')
    return {'new':len(created),'identical':len(plan)-len(created)}


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config-dir',type=Path,help='Claude target; use a disposable directory first')
    ap.add_argument('--apply',action='store_true',help='Opt-in to network downloads and creating missing files')
    ap.add_argument('--upstream-variants',action='store_true',help='Include 11 upstream commands that differ from author local copies. Never overwrite.')
    ap.add_argument('--category',choices=['all','agents','commands'],default='all')
    args=ap.parse_args(argv)
    config=args.config_dir or Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude')
    if config.is_symlink():ap.error('Claude config path is a symlink')
    config=config.expanduser().resolve()
    if config==ROOT or config.is_relative_to(ROOT):ap.error('Claude config must be outside the public repository')
    lock=json.loads(LOCK.read_text(encoding='utf-8'))
    selected=allowed_rows(lock,args.upstream_variants,args.category)
    print(f'Pinned SuperClaude {lock["upstream"]["revision"]}; {len(selected)} files; {"APPLY" if args.apply else "PREVIEW"}')
    print('Publisher: https://github.com/SuperClaude-Org/SuperClaude_Framework (MIT, attribution in THIRD_PARTY_NOTICES.md)')
    execute(config,selected,args.apply)

if __name__=='__main__':
    try:main()
    except Exception as e:
        print('ERROR:',e,file=sys.stderr);sys.exit(1)
