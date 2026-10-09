"""One-time maintainer migration for adding the development pack to bootstrap docs and manifest.
Review the diff afterward. Intentionally does not install Claude assets or call Git.
"""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]

readme=ROOT/'README.md'
manifest=ROOT/'setup/manifest.json'
installer=ROOT/'scripts/install.ps1'
install_ai=ROOT/'INSTALL_WITH_AI.md'
index=ROOT/'docs/installation/README.md'
for file in (readme,manifest,installer,install_ai,index):
    if not file.is_file(): raise SystemExit(f'Missing expected repository file: {file}')

# Validate all markers and JSON BEFORE writing anything.
r=readme.read_text(encoding='utf-8-sig')
m=json.loads(manifest.read_text(encoding='utf-8-sig'))
i=installer.read_text(encoding='utf-8-sig')
a=install_ai.read_text(encoding='utf-8-sig')
d=index.read_text(encoding='utf-8-sig')
source_manifest=json.loads((ROOT/'setup/development-assets.json').read_text(encoding='utf-8'))
if 'development' not in i and "[ValidateSet('core','full'" not in i:
    raise SystemExit('Unexpected install.ps1 profile marker. No files changed.')
if m.get('schemaVersion') != 1 or 'packagedAssets' not in m:
    raise SystemExit('Unexpected root manifest. No files changed.')
if '## Ardizuo development pack · Phase 1' not in r and '# ' not in r:
    raise SystemExit('Unexpected README format. No files changed.')

if '## Ardizuo development pack · Phase 1' not in r:
    snippet='''\n<br />\n\n## Ardizuo development pack · Phase 1\n\nAn installable pack of **28 reviewed local development files** (16 skills, one agent, five hooks, shared helper, workflows, rule and command) is now included. The **Full profile is still incomplete**: it does not automate third-party plugins, MCPs or the dashboard.\n\n```powershell\n.\\scripts\\install.ps1 -Profile development          # Dry run\n.\\scripts\\install.ps1 -Profile development -Apply   # Install after review\n.\\scripts\\doctor-development.ps1                  # Verify file hashes\n```\n\nHook registration and vault usage remain opt-in. See the [Phase 1 installation guide](./docs/installation/ardizuo-development-pack.md).\n'''
    # Insert before first level-2 section, after intro and banner.
    mt=re.search(r'^##\s+',r,re.M)
    if not mt: raise SystemExit('README lacks level-2 heading. No files changed.')
    r=r[:mt.start()]+snippet+'\n'+r[mt.start():]
    r=re.sub(r'(>\s*\*\*[^\n]*)(bootstrap preview)([^\n]*)',lambda x:x.group(1)+'Phase 1 source pack preview'+x.group(3),r,flags=re.I)
    r=r.replace('The only executable profile currently installs one namespaced global rule.',
                'Core installs one global rule; the development profile installs reviewed original files. Full remains unavailable.')
    r=r.replace('The only executable profile is Core.', 'Core and Development are executable; Full is not.')

if 'development' not in i.split('ValidateSet')[1].split(')')[0]:
    i=i.replace("[ValidateSet('core','full','frontend','backend','mobile','custom')]", "[ValidateSet('core','development','full','frontend','backend','mobile','custom')]")
    anchor="$ErrorActionPreference = 'Stop'"
    inject='''$ErrorActionPreference = 'Stop'\nif ($Profile -eq 'development') {\n    & (Join-Path $PSScriptRoot 'install-development.ps1') -Apply:$Apply\n    return\n}'''
    if i.count(anchor)!=1:raise SystemExit('Unexpected install script body. No files changed.')
    i=i.replace(anchor,inject,1)

if 'developmentPack' not in m:
    m['developmentPack']={'manifest':'setup/development-assets.json',
                         'profile':'setup/profiles/development.json',
                         'installer':'scripts/install-development.ps1',
                         'installable':True, 'fileCount':len(source_manifest['filePaths']),
                         'hookRegistration':'opt-in',
                         'noExternalPluginsMcpDashboard':True}
    for p in source_manifest['filePaths']:
        m['packagedAssets'].append({'id':'development:'+p,'kind':'original-development-asset',
                                    'source':'ardizuo-plugin/'+p,
                                    'destination':p,'installable':True})
    m['notes']='Core and the original Development pack are locally installable. Full and third-party integration automation are not yet available. Never treat configured plugins or MCP names as live connections.'

if 'ardizuo-development-pack.md' not in d:
    d+='\n<br />\n\n## Original Ardizuo development pack\n\n[Install 28 reviewed global Claude Code assets](./ardizuo-development-pack.md). This is optional and separate from external plugin/MCP installation.\n'

# Keep the existing AI prompt instructions, adding an accurate notice rather than rewriting unrelated instructions.
if 'Development pack Phase 1' not in a:
    a+='''\n<br />\n\n## Development pack Phase 1\n\nFor original Ardizuo assets (without external plugins or MCPs), review [the development pack guide](./docs/installation/ardizuo-development-pack.md) and use `scripts/install.ps1 -Profile development` for a dry run. After explicit approval, use `-Apply`. Hooks require separate approval using `node scripts/register-hooks.mjs --apply`. The Full profile is still unavailable.\n'''
    a=a.replace('only the Core bootstrap is executable','the Core bootstrap and reviewed Development pack are executable')
    a=a.replace('only the Core bootstrap is executable today','Core and Development are available; Full is not available')

# Write only after prevalidation; no external effects.
for p,content in ((readme,r),(manifest,json.dumps(m,indent=2,ensure_ascii=False)+'\n'),(installer,i),(install_ai,a),(index,d)):
    p.write_text(content,encoding='utf-8')
print('Phase 1 README, AI guide, install.ps1, installation index and manifest updated.')
print('Review git diff; no Claude config, vault, tokens or remote repositories were touched.')
