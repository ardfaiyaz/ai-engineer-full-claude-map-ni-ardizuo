#!/usr/bin/env python3
"""Add a conservative empty Development Hub tab to an upstream Claude Map app.js.
Follow with the reviewed video/minimal/semantic patches. Never touch user config.
"""
import argparse, pathlib, subprocess, datetime, shutil,sys

def patch(src):
    if 'function renderDevelopmentHub() {' in src and "devhub: renderDevelopmentHub" in src:
        return src,False
    anchors={
      'const TAB_GROUPS_GLOBAL = [':"const TAB_GROUPS_GLOBAL = [\n  { id: 'devsys', label: 'Developer Hub', icon: '◈', tabs: ['devhub'] },",
      'const TAB_GROUPS_PROJECT = [':"const TAB_GROUPS_PROJECT = [\n  { id: 'devsys', label: 'Developer Hub', icon: '◈', tabs: ['devhub'] },",
      'const TAB_META = {':"const TAB_META = {\n  devhub: { label: 'Development Hub', icon: '◈' },",
      '    mcp:      renderMCP,':"    mcp:      renderMCP,\n    devhub:   renderDevelopmentHub,",
      'function renderMCP() {':"function renderDevelopmentHub() {\n  return '<section style=\\\"padding:16px\\\"><h2>Development Hub</h2><p>Apply the architecture patch to activate the inventory.</p></section>';\n}\n\nfunction renderMCP() {",
    }
    changed=src
    for k,v in anchors.items():
        if changed.count(k)!=1:raise ValueError('Incompatible upstream Claude Map app.js anchor: '+k)
        changed=changed.replace(k,v,1)
    return changed,True

def main():
 p=argparse.ArgumentParser();p.add_argument('--map-root',required=True);p.add_argument('--apply',action='store_true');a=p.parse_args()
 app=pathlib.Path(a.map_root)/'public/app.js'
 if not app.is_file():raise RuntimeError('Claude Map public/app.js not found')
 original=app.read_text(encoding='utf8'); new,changed=patch(original)
 if not changed:print('Development Hub scaffold already exists.');return
 print('Development Hub scaffold: compatible, edits needed')
 if not a.apply: print('DRY RUN. Nothing changed.');return
 backup=pathlib.Path.home()/('claude-map-scaffold-backup-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S%f'))
 backup.mkdir(exist_ok=False,parents=True);shutil.copy2(app,backup/'app.js')
 try:
  app.write_text(new,encoding='utf8');r=subprocess.run(['node','--check',str(app)],capture_output=True,text=True)
  if r.returncode:raise RuntimeError(r.stderr)
 except Exception:
  app.write_text(original,encoding='utf8');raise
 print('Scaffold installed; backup:',backup)
if __name__=='__main__':
 try:main()
 except Exception as e:print('ERROR:',e,file=sys.stderr);sys.exit(1)
