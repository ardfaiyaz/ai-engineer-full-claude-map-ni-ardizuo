"""Dependency-free bootstrap manifest and release-boundary checks."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class BootstrapTests(unittest.TestCase):
    def test_manifest_and_packaged_asset_exist(self):
        data = json.loads((ROOT / 'setup' / 'manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(data['schemaVersion'], 1)
        self.assertEqual(data['stage'], 'bootstrap-preview')
        for asset in data['packagedAssets']:
            self.assertTrue((ROOT / asset['source']).is_file(), asset['source'])
            self.assertFalse('..' in pathlib.PurePosixPath(asset['source']).parts)

    def test_only_core_profile_is_installable(self):
        for path in (ROOT / 'setup' / 'profiles').glob('*.json'):
            data = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(data['installableInBootstrap'], path.stem == 'core')

    def test_no_home_directory_is_hardcoded_in_install_scripts(self):
        for path in (ROOT / 'scripts').glob('*.ps1'):
            content = path.read_text(encoding='utf-8')
            self.assertNotIn('C:\\Users\\Melthon', content)
            self.assertNotIn('Authorization: Bearer ', content)

    def test_no_social_media_component_ids(self):
        data = json.loads((ROOT / 'setup' / 'manifest.json').read_text(encoding='utf-8'))
        names = str(data['plannedAssets']['externalPluginsForUserInstallation'] + data['plannedAssets']['externalUserMcpReferencesNoSecrets']).lower()
        for forbidden in ('vidiq', 'instagram', 'tiktok', 'facebook', 'twitter', 'x-twitter'):
            self.assertNotIn(forbidden, names)

if __name__ == '__main__':
    unittest.main()
