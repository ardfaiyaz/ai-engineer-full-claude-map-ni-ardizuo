#!/usr/bin/env python3
"""Version-sensitive upstream Claude Map layering. Dry-run by default.
Never executes model calls or accesses vault notes.
"""
import argparse,subprocess,pathlib,sys,shutil,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
PATCH=ROOT/'dashboard/claude-map/patches'

def main():
 p=argparse.ArgumentParser();p.add_argument('--apply',action='store_true');p.add_argument('--map-root',type=pathlib.Path);a=p.parse_args()
 if a.map_root: directory=a.map_root
 else:
  r=subprocess.run(['npm','root','-g'],capture_output=True,text=True)
  if r.returncode:raise RuntimeError('npm root -g unavailable')
  directory=pathlib.Path(r.stdout.strip())/'claude-map'
 if not (directory/'public/app.js').is_file() or not (directory/'server.js').is_file():raise RuntimeError('Claude Map source not found; install npm package first')
 print('Target:',directory)
 patches=[
  ('bootstrap_devhub.py',['--map-root',str(directory),'--apply']),
  ('claude_map_video_dashboard_patch.py',['--map-dir',str(directory)]),
  ('claude_map_minimal_complete.py',['--map-dir',str(directory)]),
  ('claude_map_finalize_integrations.py',['--map-root',str(directory),'--dry-run' if not a.apply else '--apply']),
  ('claude_map_status_theme.py',['--map-root',str(directory),'--dry-run' if not a.apply else '--apply'])
 ]
 # Dry-run requires a disposable copy because the later patch requires previous mutations.
 if not a.apply:
  print('DRY RUN — review overlay stages before using --apply:')
  for name,_ in patches:print('  ',name)
  print('Compatibility not guaranteed. No changes made.');return
 backups=pathlib.Path.home()/('claude-map-complete-backup-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S%f'))
 backups.mkdir(parents=True,exist_ok=False)
 for pth in [directory/'server.js',directory/'public/app.js']:shutil.copy2(pth,backups/pth.name)
 try:
  for name,args in patches:
   print('Installing overlay:',name)
   cmd=[sys.executable,str(PATCH/name)]+args
   r=subprocess.run(cmd)
   if r.returncode:raise RuntimeError(f'Overlay {name} failed with exit {r.returncode}')
  for pth in [directory/'server.js',directory/'public/app.js']:
   r=subprocess.run(['node','--check',str(pth)],capture_output=True,text=True)
   if r.returncode:raise RuntimeError(r.stderr)
 except Exception:
  print('Overlay not compatible. Restoring backup files.')
  for pth in [directory/'server.js',directory/'public/app.js']:shutil.copy2(backups/pth.name,pth)
  raise
 print('Installed Development Hub overlay. Backup:',backups)
 print('Restart claude-map -p 8888 and hard refresh. Existing plugin/MCP connection not implied.')
if __name__=='__main__':
 try:main()
 except Exception as e:print('ERROR:',e,file=sys.stderr);sys.exit(1)
