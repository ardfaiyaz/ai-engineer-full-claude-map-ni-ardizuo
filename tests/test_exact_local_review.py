"""Sprint 6: exact existing skills are inventoried locally, not guessed or published."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'scripts/review-exact-local-components.py'

def load():
    spec=importlib.util.spec_from_file_location('exact_local_review',SOURCE)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class ExactLocalReviewTests(unittest.TestCase):
    def test_six_public_source_leads_but_no_install_approval(self):
        m=load(); _,ref,c=m.load_manifest()
        self.assertEqual(len(ref['globalSkills']),62)
        self.assertEqual(len(c),17)
        found=[v for v in c.values() if 'repository' in v]
        self.assertEqual(len(found),6)
        self.assertTrue(all('approvedForInstall' not in x for x in c.values()))
        self.assertIn('skill-creator',c)
        self.assertNotIn('owasp-security',c)
    def test_default_preview_no_network_no_writes(self):
        with tempfile.TemporaryDirectory() as t:
            folder=Path(t)/'missing'
            with patch('urllib.request.urlopen',side_effect=AssertionError('network forbidden')):
                p=subprocess.run([sys.executable,str(SOURCE),'--config-dir',str(folder)],text=True,capture_output=True)
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertIn('6 out of 17',p.stdout)
            self.assertFalse(folder.exists())
    def test_script_never_exports_private_bytes_or_absolute_paths(self):
        m=load()
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'config'; skill=root/'skills'/'docx'; (skill/'scripts').mkdir(parents=True)
            message=b'PRIVATE_ACCESS_TOKEN_DO_NOT_EXPORT\nRun scripts/do.py\n'
            (skill/'SKILL.md').write_bytes(message)
            (skill/'scripts'/'do.py').write_text('# private script',encoding='utf8')
            result=m.main_audit(root)
            self.assertEqual(result['summary']['localSKILLmdPresent'],1)
            skillrow=next(x for x in result['skills'] if x['name']=='docx')
            self.assertEqual(skillrow['supportingFileCount'],1)
            self.assertGreaterEqual(skillrow['relativeReferenceHints'],1)
            self.assertEqual(skillrow['unresolvedReferenceHints'],0)
            dump=json.dumps(result)
            self.assertNotIn('PRIVATE_ACCESS_TOKEN',dump)
            self.assertNotIn(str(root),dump)
            self.assertNotIn('do.py',dump)
    def test_pinned_public_hash_check_and_equivalence(self):
        m=load()
        data=b'# SKILL\n'
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\x00'+data).hexdigest()
        good={'repository':'anthropics/skills','revision':'0'*40,'sourcePath':'skills/pdf/SKILL.md','gitBlobSHA1':blob}
        self.assertEqual(m.remote_bytes(good,fetcher=lambda url:data),data)
        self.assertEqual(m.matching_status(data,b'# SKILL\r\n'),'TEXT_MATCH_LINE_ENDINGS_ONLY')
        self.assertEqual(m.matching_status(data,b'# CHANGE\n'),'DIFFERENT_CONTENT')
        bad=dict(good,gitBlobSHA1='0'*40)
        with self.assertRaisesRegex(ValueError,'Git blob'):
            m.remote_bytes(bad,fetcher=lambda url:data)
    def test_origin_comparison_never_bundles_unverified_skills(self):
        m=load()
        with tempfile.TemporaryDirectory() as t:
            skill=Path(t)/'skills'/'docx'; skill.mkdir(parents=True)
            (skill/'SKILL.md').write_text('local version',encoding='utf8')
            with patch.object(m,'remote_bytes',return_value=b'public version') as mock_fetch:
                res=m.main_audit(Path(t),compare_public=True)
            row=next(x for x in res['skills'] if x['name']=='docx')
            self.assertEqual(row['upstreamComparison'],'DIFFERENT_CONTENT')
            self.assertEqual(mock_fetch.call_count,1)
            self.assertEqual(row['releaseCategory'],'unverified-direct-skill')
    def test_metadata_report_creation_is_explicit_and_create_only(self):
        m=load()
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'user-config'; destination=Path(t)/'private-report.json'
            code=m.main(['--config-dir',str(root),'--output',str(destination)])
            self.assertEqual(code,0)
            self.assertTrue(destination.is_file())
            with self.assertRaises(FileExistsError):
                m.main(['--config-dir',str(root),'--output',str(destination)])
            with self.assertRaisesRegex(ValueError,'outside'):
                m.safe_output_path(str(ROOT/'inside.json'),root)
            with self.assertRaisesRegex(ValueError,'outside'):
                m.safe_output_path(str(root/'inside.json'),root)
    def test_symlinks_are_not_followed(self):
        m=load()
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'config'; d=p/'skills'/'pdf';d.mkdir(parents=True)
            (d/'SKILL.md').write_text('# PDF',encoding='utf8')
            (d/'subfile').write_text('safe',encoding='utf8')
            self.assertTrue(m.safe_skill_file(p,'pdf'))
            self.assertEqual(m.count_sidecars(d)['supportingFileCount'],1)
            link=d/'external'
            try:link.symlink_to(Path(t),target_is_directory=True)
            except (OSError,NotImplementedError):return
            self.assertEqual(m.count_sidecars(d)['supportingFileCount'],1)
            self.assertGreaterEqual(m.count_sidecars(d)['symlinksSkipped'],1)
    def test_only_existing_reference_components(self):
        m=load();_,ref,c=m.load_manifest()
        j=json.loads((ROOT/'setup/release-coverage.json').read_text())
        sources=set(j['notAutomaticallyReproduced']['directSkillsRequiringVerifiedOriginOrExternalSource'])
        self.assertEqual(sources,set(c))
        self.assertTrue(sources.issubset(set(ref['globalSkills'])))
        self.assertEqual(len(m.CUSTOMIZED_FILES),7)

if __name__=='__main__':unittest.main()
