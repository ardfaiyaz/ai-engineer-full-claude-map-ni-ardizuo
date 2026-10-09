#!/usr/bin/env python3
"""Read-only re-comparison of 19 previously unresolved SKILL.md definitions.

With --compare, downloads public publisher files into memory, verifies their Git
blob hashes, and reads the matching private SKILL.md locally for comparison.
Never uploads, prints, writes, or packages private source contents. Output CSV
contains statuses and public source metadata ONLY. No install approval given.
"""
import argparse
import csv
import json
import os
from pathlib import Path
import re
import sys
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
CANDIDATES=ROOT/'setup/skill-source-candidates.json'
MAX_BYTES=1024*1024
ALLOWED={
    'emilkowalski/skills':'e8a175de22ae1e49370fc144c1f3bb9aeedf988d',
    'addyosmani/agent-skills':'1401c8b8030e023baeebb31781a6653fe8e93026',
    'vitalics/playwright-labs':'be116c4523b1adf403cef3b7dc71f5e01d842d3a',
    'vercel-labs/agent-skills':'063bee94c3f4df8453406c830b0a7df0f2860278',
    'dominika-zajac/better-frontend-skills':'92cdb7e73323f6d627dbab0462e94ba8786f3264',
}


def validate_candidates(rows):
    if len(rows)!=19 or len({row['target'].casefold() for row in rows})!=19:
        raise ValueError('Skill candidates changed; review the manifest')
    for row in rows:
        parts=row['target'].split('/')
        if len(parts)!=3 or parts[0]!='skills' or parts[-1]!='SKILL.md' or not re.fullmatch(r'[a-z0-9-]+',parts[1]):
            raise ValueError('Unsafe candidate target')
        if row.get('approvedForInstall') is not False:raise ValueError('Candidates must not be approved automatically')
        if not row.get('candidateRepository'):continue
        repository=row['candidateRepository']
        if repository not in ALLOWED or row['revision']!=ALLOWED[repository]:raise ValueError('Unreviewed source repository')
        path=row['sourceFilePath']
        if not isinstance(path,str) or '\\' in path or path.startswith('/') or ':' in path or '..' in path.split('/') or not path.endswith('/SKILL.md'):
            raise ValueError('Invalid upstream source path')
        if not re.fullmatch(r'[a-f0-9]{40}',row.get('gitBlobSHA1','')):
            raise ValueError('Invalid public blob checksum')


def public_source(row,timeout=25):
    # Public source is always an immutable commit on a recognized GitHub repo.
    parts=[urllib.parse.quote(p,safe='') for p in row['sourceFilePath'].split('/')]
    url=f'https://raw.githubusercontent.com/{row["candidateRepository"]}/{row["revision"]}/{"/".join(parts)}'
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Ardizuo-Private-Source-Comparator/1.0'}),timeout=timeout) as r:
        data=r.read(MAX_BYTES+1)
    if len(data)>MAX_BYTES:raise ValueError('Public skill too large')
    # Import the local checksum algorithm without executing any installer.
    import hashlib
    sha=hashlib.sha1(b'blob '+str(len(data)).encode('ascii')+b'\0'+data).hexdigest()
    if sha!=row['gitBlobSHA1']:raise ValueError('Pinned publisher hash mismatch')
    return data


def compare_rows(rows,private_root,fetch=public_source):
    from pathlib import PurePosixPath
    results=[]
    for row in rows:
        label=row['target'];repo=row.get('candidateRepository')
        out={'target':label,'candidateRepository':repo or '', 'revision':row.get('revision') or '', 'sourceFilePath':row.get('sourceFilePath') or ''}
        if not repo:
            out['comparison']='SOURCE_UNKNOWN';results.append(out);continue
        src=private_root/Path(*PurePosixPath(label).parts)
        if src.is_symlink() or any(p.is_symlink() for p in src.parents if p==private_root or private_root in p.parents):
            out['comparison']='PRIVATE_SYMLINK_REFUSED';results.append(out);continue
        if not src.is_file():out['comparison']='LOCAL_FILE_MISSING';results.append(out);continue
        if src.stat().st_size>MAX_BYTES:out['comparison']='PRIVATE_FILE_TOO_LARGE';results.append(out);continue
        try:
            # Private bytes remain on the machine; they are never sent in a request.
            local=src.read_bytes()
            remote=fetch(row)
            if local==remote:out['comparison']='EXACT_BYTE_MATCH'
            elif local.replace(b'\r\n',b'\n')==remote.replace(b'\r\n',b'\n'):out['comparison']='TEXT_MATCH_LINE_ENDINGS_ONLY'
            else:out['comparison']='DIFFERENT_CONTENT'
        except Exception:
            out['comparison']='DOWNLOAD_OR_VERIFICATION_FAILED'
        results.append(out)
    return results


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--private-root',type=Path,default=Path.home()/'Documents/Ardizuo-Additional-Assets-PRIVATE')
    ap.add_argument('--output',type=Path,default=Path.home()/'Documents/Ardizuo-Remaining-Skill-Comparison.csv')
    ap.add_argument('--compare',action='store_true',help='Opt in to fetching public sources and creating results CSV')
    a=ap.parse_args(argv)
    root=a.private_root.expanduser().resolve();out=a.output.expanduser().resolve()
    rows=json.loads(CANDIDATES.read_text('utf-8'))['entries'];validate_candidates(rows)
    print('Historical source-review entries:',len(rows),'; public publisher candidates:',sum(bool(x.get('candidateRepository')) for x in rows))
    if not a.compare:
        for row in rows:print('  '+row['target']+': '+row['status'])
        print('DRY RUN. No network, no source reads, no output file writes. Add --compare to proceed.')
        return
    if not root.is_dir() or root.is_symlink():raise ValueError('Private root not found or a symlink')
    if out.exists() or out==ROOT or out.is_relative_to(ROOT) or out==root or out.is_relative_to(root):
        raise ValueError('Choose a new output path OUTSIDE the public project and private source folder. No overwrites.')
    results=compare_rows(rows,root)
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x',newline='',encoding='utf-8-sig') as fh:
        writer=csv.DictWriter(fh,fieldnames=['target','candidateRepository','revision','sourceFilePath','comparison']);writer.writeheader();writer.writerows(results)
    counts={k:sum(r['comparison']==k for r in results) for k in sorted({r['comparison'] for r in results})}
    print('Comparison statuses:',counts)
    print('Private source contents never left the machine. Report:',out)
    print('Results are source evidence only; no bundle/install approval is inferred.')

if __name__=='__main__':
    try:main()
    except Exception as e:print('ERROR:',e,file=sys.stderr);sys.exit(1)
