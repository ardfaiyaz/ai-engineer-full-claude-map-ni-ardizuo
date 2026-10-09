#!/usr/bin/env python3
"""Read-only local provenance/sidecar inventory for EXACT reference-machine skills.

Default: no network and no writes. --compare-public fetches only publisher-pinned
public SKILL.md files (it never uploads local bytes). --output saves metadata-only
JSON outside both the GitHub checkout and user's Claude config, create-only.
This is NOT a permission-to-redistribute assessment or skill execution test.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
COVERAGE_FILE = ROOT / 'setup/release-coverage.json'
REFERENCE_FILE = ROOT / 'setup/reference-inventory.json'
CANDIDATES_FILE = ROOT / 'setup/direct-skill-origin-candidates.json'

# Fixed, previously observed local differences. Never export the private content.
CUSTOMIZED_FILES = (
    'commands/log-to-vault.md',
    'hooks/lib/common.mjs',
    'hooks/vault-session-init.mjs',
    'rules/developer-orchestration.md',
    'skills/vault-learning/SKILL.md',
    'workflows/completion-mandate.md',
    'workflows/wave-protocol.md',
)
MAX_SKILL_BYTES = 4 * 1024 * 1024
MAX_SIDECARS = 2000
# Merely *hints* of paths mentioned in the Markdown; not proof they are required.
PATH_HINT = re.compile(r'(?<![A-Za-z0-9_])(?:\./)?((?:scripts|references|assets|templates|data|examples)/[A-Za-z0-9_.\-/]{1,180})')
SAFE_NAME = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]*$')
SAFE_REPO = re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')
SAFE_REV = re.compile(r'^[a-f0-9]{40}$')


def load_manifest():
    cv = json.loads(COVERAGE_FILE.read_text(encoding='utf-8'))
    ref = json.loads(REFERENCE_FILE.read_text(encoding='utf-8'))
    cm = json.loads(CANDIDATES_FILE.read_text(encoding='utf-8'))
    expected = set(cv['notAutomaticallyReproduced']['directSkillsRequiringVerifiedOriginOrExternalSource'])
    items = cm['entries']
    if len(items) != len(expected) or {x['name'] for x in items} != expected:
        raise ValueError('Source leads must match the 17 reference-machine external/unverified direct skills')
    if any(not SAFE_NAME.fullmatch(x['name']) for x in items):
        raise ValueError('Invalid skill name in manifest')
    for x in items:
        if 'repository' in x:
            if not SAFE_REPO.fullmatch(x['repository']) or not SAFE_REV.fullmatch(x['revision']):
                raise ValueError('Invalid pinned source identifier')
            path = x['sourcePath']
            if any(p in ('', '..', '.') for p in path.split('/')) or not path.endswith('/SKILL.md'):
                raise ValueError('Invalid relative pinned source path')
            if not SAFE_REV.fullmatch(x['gitBlobSHA1']):
                raise ValueError('Invalid pinned blob checksum')
    if len(ref['globalSkills']) != 62 or len(set(ref['globalSkills'])) != 62:
        raise ValueError('Unexpected 62-skill reference inventory')
    return cv, ref, {x['name']:x for x in items}


def remote_bytes(candidate, fetcher=None):
    repo, rev, path = candidate['repository'], candidate['revision'], candidate['sourcePath']
    url = f'https://raw.githubusercontent.com/{repo}/{rev}/{path}'
    if fetcher is not None:
        body = fetcher(url)
    else:
        request = Request(url, headers={'User-Agent':'Ardizuo-Safe-Origin-Comparison/1.0'})
        with urlopen(request, timeout=20) as response:
            body = response.read(MAX_SKILL_BYTES + 1)
    if len(body) > MAX_SKILL_BYTES:
        raise ValueError('Public candidate exceeds 4MB safety limit')
    git_sha1 = hashlib.sha1(b'blob '+str(len(body)).encode('ascii')+b'\0'+body).hexdigest()
    if git_sha1 != candidate['gitBlobSHA1']:
        raise ValueError('Publisher candidate did not match pinned Git blob SHA-1')
    return body


def matching_status(a: bytes, b: bytes):
    if a == b: return 'EXACT_BYTE_MATCH'
    if a.replace(b'\r\n',b'\n') == b.replace(b'\r\n',b'\n'):
        return 'TEXT_MATCH_LINE_ENDINGS_ONLY'
    return 'DIFFERENT_CONTENT'


def is_link_or_junction(path: Path):
    return path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction())


def safe_skill_file(config: Path, name: str):
    skill = config/'skills'/name
    if is_link_or_junction(skill) or not skill.is_dir():
        return None
    prompt = skill/'SKILL.md'
    if is_link_or_junction(prompt) or not prompt.is_file():
        return None
    return prompt


def count_sidecars(skill_folder: Path):
    count = 0
    kinds = Counter()
    symlinks_skipped = 0
    capped = False
    for base, dirs, names in os.walk(skill_folder, topdown=True, followlinks=False):
        checked=[]
        for d in dirs:
            p=Path(base)/d
            if is_link_or_junction(p): symlinks_skipped+=1
            elif d not in ('.git', 'node_modules', '.venv', '__pycache__'):
                checked.append(d)
        dirs[:]=checked
        for n in names:
            p=Path(base)/n
            if is_link_or_junction(p):
                symlinks_skipped+=1
                continue
            if p.name == 'SKILL.md' and p.parent == skill_folder:
                continue
            if count >= MAX_SIDECARS:
                capped = True
                dirs[:]=[]
                break
            if p.is_file():
                count += 1
                ext = p.suffix.lower()
                kinds[ext if ext and len(ext)<=12 else '[other]'] += 1
        if capped: break
    return {'supportingFileCount':count,'supportingFileExtensionCounts':dict(sorted(kinds.items())),
            'symlinksSkipped':symlinks_skipped,'scanCapped':capped}


def relative_hints(prompt_bytes: bytes, skill_folder:Path):
    text = prompt_bytes.decode('utf-8',errors='replace')
    potential=set()
    for match in PATH_HINT.finditer(text):
        hint=match.group(1).rstrip('.,;:\\')
        parts=hint.split('/')
        if '..' in parts or '' in parts:continue
        potential.add('/'.join(parts))
    found=0
    for hint in potential:
        p=skill_folder/Path(hint)
        if not is_link_or_junction(p) and p.is_file(): found += 1
    return {'relativeReferenceHints':len(potential),'referenceHintsWithFiles':found,
            'unresolvedReferenceHints':len(potential)-found}


def main_audit(config:Path, compare_public=False, fetcher=None):
    cv, ref, candidates = load_manifest()
    normal=cv['defaultInstall']['directSkills']
    bundled=set(normal['reviewedBundled']); pinned=set(normal['verifiedPinned'])
    variants=set(cv['optInUpstreamVersions']['skills'])
    external=set(cv['notAutomaticallyReproduced']['directSkillsRequiringVerifiedOriginOrExternalSource'])
    unknown=set(cv['notAutomaticallyReproduced']['directSkillsWithUnknownSafeSource'])
    assert bundled.isdisjoint(pinned) and len(bundled|pinned)==36
    rows=[]
    for name in ref['globalSkills']:
        tier=('bundled' if name in bundled else 'pinned' if name in pinned else
              'optional-upstream-version' if name in variants else
              'unverified-direct-skill' if name in external else
              'unknown-source' if name in unknown else 'UNEXPECTED')
        row={'name':name,'releaseCategory':tier}
        prompt=safe_skill_file(config,name)
        row['localSKILLmdPresent']=prompt is not None
        if prompt is not None:
            blob=prompt.read_bytes()
            if len(blob)>MAX_SKILL_BYTES:raise ValueError('Local SKILL.md exceeds 4MB: '+name)
            row['sourceSizeBytes']=len(blob)
            row.update(count_sidecars(prompt.parent))
            row.update(relative_hints(blob,prompt.parent))
        if name in candidates:
            lead=candidates[name]
            row['publicCandidateAvailable']='repository' in lead
            if 'repository' in lead:
                row['publicCandidateRepository']=lead['repository']
                row['pinnedRevision']=lead['revision']
                row['publicCandidateFile']=lead['sourcePath']
                row['upstreamComparison']='NOT_RUN' if not compare_public else 'MISSING_LOCAL' if prompt is None else None
                if compare_public and prompt is not None:
                    try: row['upstreamComparison']=matching_status(blob,remote_bytes(lead,fetcher))
                    except Exception: row['upstreamComparison']='DOWNLOAD_OR_CHECKSUM_FAILURE'
            else: row['upstreamComparison']='NO_APPROVED_SOURCE_CANDIDATE'
        rows.append(row)
    diffs=[]
    for rel in CUSTOMIZED_FILES:
        repo=ROOT/'ardizuo-plugin'/rel
        local=config/rel
        if not repo.is_file():raise ValueError('Packaged Ardizuo file missing: '+rel)
        state=('NOT_PRESENT' if not local.is_file() or is_link_or_junction(local) else
               'IDENTICAL_TO_PACKAGE' if repo.read_bytes()==local.read_bytes() else 'DIFFERENT_FROM_PACKAGE')
        diffs.append({'relativePath':rel,'status':state})
    expected={x['name'] for x in rows}
    if expected!=set(ref['globalSkills']):raise ValueError('Missing declared reference skills')
    return {'schemaVersion':1,'scope':'Read-only local evidence; not an installability or execution claim',
            'localContentsExported':False,'localAbsolutePathsExported':False,
            'note':'Public source candidates do not imply redistribution rights. Supporting-file path hints are heuristic.',
            'summary':{
                'skillsExpected':len(rows),
                'localSKILLmdPresent':sum(x['localSKILLmdPresent'] for x in rows),
                'candidatePinsAvailable':sum('publicCandidateRepository' in x for x in rows),
                'unresolvedLocalDifferences':sum(x['status']=='DIFFERENT_FROM_PACKAGE' for x in diffs),
                'supportingFilesFound':sum(x.get('supportingFileCount',0) for x in rows)},
            'skills':rows,'customizedArdizuoFiles':diffs}


def safe_output_path(value:str, config:Path):
    path=Path(value).expanduser().resolve()
    for forbidden in (ROOT.resolve(),config.resolve()):
        if path == forbidden or forbidden in path.parents:
            raise ValueError('Report must be outside repository and Claude global configuration')
    if path.suffix.lower()!='.json':raise ValueError('Use a .json report filename')
    if not path.parent.is_dir():raise ValueError('Create a private output folder first')
    return path


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config-dir',default=str(Path.home()/'.claude'),help='User Claude config, read-only')
    ap.add_argument('--compare-public',action='store_true',help='Download pinned public SKILL.md candidates; no local upload')
    ap.add_argument('--output',help='Explicit private .json report path, created once; no overwrite')
    args=ap.parse_args(argv)
    config=Path(args.config_dir).expanduser().resolve()
    result=main_audit(config,args.compare_public)
    s=result['summary']
    print('ARDIZUO EXACT LOCAL COMPONENT REVIEW — READ ONLY')
    print('  62 direct skills:',s['localSKILLmdPresent'],'found; support files:',s['supportingFilesFound'])
    print('  Existing public source candidates:',s['candidatePinsAvailable'],'out of 17 previously unresolved skill origins')
    print('  Seven Ardizuo source comparisons:',s['unresolvedLocalDifferences'],'different from public package')
    for x in result['skills']:
        if x['releaseCategory'] in ('unverified-direct-skill','unknown-source','optional-upstream-version'):
            verdict=x.get('upstreamComparison','NOT_CANDIDATE')
            print('  ',x['name']+':',x['releaseCategory'], '|','present' if x['localSKILLmdPresent'] else 'missing','|',verdict,
                  '| sidecars:',x.get('supportingFileCount',0))
    if args.output:
        p=safe_output_path(args.output,config)
        with p.open('x',encoding='utf-8') as f:
            json.dump(result,f,indent=2,ensure_ascii=False)
            f.write('\n')
        print('  Private metadata-only report:',str(p))
    else:
        print('  No report saved (provide --output to save outside the public repo).')
    print('  Local content not printed, copied or uploaded. Script makes no Claude settings changes.')
    return 0

if __name__=='__main__':
    try:sys.exit(main())
    except Exception as exc:
        print('AUDIT FAILED:',str(exc),file=sys.stderr)
        sys.exit(1)
