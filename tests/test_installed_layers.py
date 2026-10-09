"""Offline tests for a truthful and non-mutating config deployment report."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'scripts/verify-installed-layers.py'

def load():
    spec=importlib.util.spec_from_file_location('installed_layers',SRC)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m

class InstalledLayersTests(unittest.TestCase):
    def test_all_default_names_are_from_existing_source_lock_and_owned_assets(self):
        m=load(); f=m.expected()
        self.assertEqual(len(f),len(set(f)))
        self.assertEqual(len([p for p in f if p.startswith('agents/')]),21)
        self.assertEqual(len([p for p in f if p.startswith('skills/')]),36)
        self.assertEqual(len([p for p in f if p.startswith('commands/')]),20)
        self.assertEqual(len([p for p in m.expected(True) if p.startswith('skills/')]),41)
        self.assertEqual(len([p for p in m.expected(True) if p.startswith('commands/')]),31)
        self.assertFalse(any('social' in p.casefold() for p in f))
    def test_fresh_config_reports_missing_not_fake_success(self):
        with tempfile.TemporaryDirectory() as t:
            result=load().audit(Path(t))
            self.assertEqual(result['presentLocalFiles'],0)
            self.assertEqual(len(result['missing']),result['expectedLocalFiles'])
            self.assertFalse(any(result['hooksRegistered'].values()))
            self.assertIn('NOT TESTED',result['providers'])
    def test_real_local_installer_and_hook_registration_in_sandbox(self):
        with tempfile.TemporaryDirectory() as t:
            conf=Path(t)/'config';vault=Path(t)/'vault'
            c=subprocess.run([sys.executable,str(ROOT/'scripts/install-all.py'),'--apply','--config-dir',str(conf),'--vault','--vault-path',str(vault)],capture_output=True,text=True)
            self.assertEqual(c.returncode,0,c.stderr)
            m=load();a=m.audit(conf, vault=vault)
            self.assertEqual(a['byLayer']['agents']['present'],1)
            self.assertEqual(a['byLayer']['skills']['present'],16)
            self.assertEqual(a['byLayer']['global-context']['present'],1)
            self.assertEqual(a['vault']['templatesFound'],4)
            self.assertEqual(a['vault']['foldersFound'],8)
            self.assertEqual(len(a['missing']),a['expectedLocalFiles']-a['presentLocalFiles'])
            if subprocess.run(['node','--version'],capture_output=True).returncode==0:
                reg=subprocess.run(['node',str(ROOT/'scripts/register-hooks.mjs'),'--config-dir',str(conf),'--apply'],capture_output=True,text=True)
                self.assertEqual(reg.returncode,0,reg.stderr)
                b=m.audit(conf)
                self.assertTrue(all(b['hooksRegistered'].values()))
    def test_strict_local_fails_missing_without_touching_config(self):
        with tempfile.TemporaryDirectory() as t:
            target=Path(t)/'fresh'
            cmd=[sys.executable,str(SRC),'--config-dir',str(target),'--strict-local','--json']
            r=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(r.returncode,2,r.stderr)
            self.assertFalse(target.exists())
            self.assertGreater(len(json.loads(r.stdout)['missing']),50)

if __name__=='__main__':unittest.main()
