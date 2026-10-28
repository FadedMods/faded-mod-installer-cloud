import base64
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

import validate_schedule_i_catalog as catalog


ROOT = Path(__file__).resolve().parents[1]


class ScheduleICatalogValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.key = rsa.generate_private_key(public_exponent=65537, key_size=3072)
        cls.key_id = hashlib.sha256(cls.key.public_key().public_bytes(
            serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)).hexdigest()
        cls.trust = json.dumps({
            'schema': 1, 'channel': 'production', 'keyId': cls.key_id,
            'publicKeyPem': cls.key.public_key().public_bytes(
                serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo).decode('ascii'),
        }).encode('utf-8')

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        trust = self.root / 'trust.json'
        trust.write_bytes(self.trust)
        self.addCleanup(patch.stopall)
        patch.object(catalog, 'TRUST_PATH', trust).start()
        patch.object(catalog, 'TRUST_SHA256', hashlib.sha256(self.trust).hexdigest()).start()
        self.descriptor = {
            'schema': 1, 'product': 'schedule-i', 'component': 'package-helper',
            'channel': 'production', 'keyId': self.key_id, 'version': '0.5.0',
            'contractSchema': 1, 'minimumInstallerVersion': '0.3.21', 'platform': 'windows-x64',
            'prerequisites': dict(framework='Microsoft.NETCore.App', version='11.0.2', architecture='x64', rollForward='Disable'),
            'archive': dict(url='https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/helper-0.5/helper.zip',
                            size=1000, sha256='a' * 64),
            'files': [dict(path=name, size=1, sha256='b' * 64) for name in sorted(catalog.HELPER_FILES)],
        }

    def envelope(self, descriptor=None, *, domain=catalog.SIGNATURE_DOMAIN, raw=None):
        raw = raw or json.dumps(descriptor or self.descriptor).encode('utf-8')
        signature = self.key.sign(domain + raw,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32), hashes.SHA256())
        return dict(payload=base64.b64encode(raw).decode('ascii'), signature=base64.b64encode(signature).decode('ascii'))

    def full_catalog(self, descriptor=None):
        descriptor = descriptor or self.descriptor
        value = json.loads((ROOT / 'schedule-i/0.4-manifest.json').read_bytes())
        # Helper contract fixtures must not inherit the changing public mod list.
        # Independent mod membership/counting is exercised explicitly below.
        value['mods'] = []
        value.update(minimumInstallerVersion='0.3.21', version='0.5.0', prerequisites=descriptor['prerequisites'])
        value['runtime']['version'] = '0.5.0'
        value['helper'].update(version=descriptor['version'], contractSchema=1,
                               **descriptor['archive'], signedRelease=self.envelope(descriptor))
        return value

    def test_legacy_unsigned_helper_remains_supported_but_future_unsigned_is_rejected(self):
        value = self.full_catalog()
        value['helper'].pop('signedRelease')
        with self.assertRaises(ValueError):
            catalog.validate_object(value)
        value['helper']['version'] = '0.4.0'
        value['prerequisites'] = dict(framework='Microsoft.NETCore.App', version='10.0.12', architecture='x64', rollForward='Disable')
        self.assertEqual(catalog.validate_object(value), 2)

    def test_future_helper_and_exact_dotnet_prerequisite_need_no_validator_code_change(self):
        value = self.full_catalog()
        self.assertEqual(catalog.validate_object(value), 2)
        self.assertEqual(catalog.validate_helper_release(value['helper']['signedRelease']), self.descriptor)

    def test_independent_mod_is_counted_and_its_identity_must_be_unique(self):
        value = self.full_catalog()
        value['mods'] = [{
            'id': 'faded.fixture', 'packageId': 'faded.fixture', 'kind': 'mod',
            'version': '1.0.0', 'size': 100, 'sha256': 'c' * 64,
            'url': 'https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/fixture/TestMod.fmod',
        }]
        self.assertEqual(catalog.validate_object(value), 3)
        self.assertEqual(catalog.validate(self.write_stable(value)), 5)
        value['mods'].append(copy.deepcopy(value['mods'][0]))
        with self.assertRaisesRegex(ValueError, 'Unique component'):
            catalog.validate_object(value)

    def test_descriptor_signature_key_domain_and_raw_json_are_authoritative(self):
        tampered = self.envelope()
        tampered['payload'] = base64.b64encode(base64.b64decode(tampered['payload']).replace(b'0.5.0', b'0.6.0')).decode('ascii')
        for envelope in [tampered, self.envelope(domain=b'another protocol\n'),
                         dict(self.envelope(), publicKeyPem='catalog cannot replace trust')]:
            with self.subTest(envelope=str(envelope)[:40]), self.assertRaises(ValueError):
                catalog.validate_helper_release(envelope)
        catalog.TRUST_PATH.write_bytes(self.trust + b'\n')
        with self.assertRaisesRegex(ValueError, 'pinned'):
            catalog.validate_helper_release(self.envelope())

    def test_signed_archive_and_outer_catalog_cannot_diverge(self):
        for change in [dict(version='0.6.0'), dict(sha256='0' * 64), dict(size=999),
                       dict(url='https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/other/helper.zip')]:
            value = self.full_catalog()
            value['helper'].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                catalog.validate_object(value)
        value = self.full_catalog()
        value['prerequisites']['version'] = '11.0.3'
        with self.assertRaises(ValueError):
            catalog.validate_object(value)

    def test_signed_helper_enforces_closed_files_protocol_and_immutable_origin(self):
        variants = []
        for change in [dict(contractSchema=2), dict(schema=True), dict(channel='development'),
                       dict(platform='windows-x86'), dict(minimumInstallerVersion='0.3.20')]:
            variants.append(dict(self.descriptor, **change))
        for field, value in [('url', self.descriptor['archive']['url'] + '?mutable=yes'), ('size', True), ('sha256', 'x' * 64)]:
            descriptor = copy.deepcopy(self.descriptor)
            descriptor['archive'][field] = value
            variants.append(descriptor)
        descriptor = copy.deepcopy(self.descriptor)
        descriptor['files'][0]['path'] = '../outside.dll'
        variants.append(descriptor)
        descriptor = copy.deepcopy(self.descriptor)
        descriptor['files'][1] = descriptor['files'][0]
        variants.append(descriptor)
        for descriptor in variants:
            with self.subTest(descriptor=str(descriptor)[:100]), self.assertRaises(ValueError):
                catalog.validate_helper_release(self.envelope(descriptor))

    def test_duplicate_signed_json_fields_are_rejected_after_authentication(self):
        raw = json.dumps(self.descriptor).encode('utf-8')
        raw = raw.replace(b'"schema": 1', b'"schema": 1, "schema": 1')
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON'):
            catalog.validate_helper_release(self.envelope(raw=raw))

    def write_stable(self, nested, *, mirror='schedule-i/future-helper-manifest.json'):
        root = json.loads((ROOT / 'schedule-i-manifest.json').read_bytes())
        root['compatibleCatalogs'] = [dict(minimumInstallerVersion=nested['minimumInstallerVersion'], manifestPath=mirror, catalog=nested)]
        root.update(latestRuntimeVersion=nested['runtime']['version'], minimumInstallerVersionForLatest=nested['minimumInstallerVersion'])
        path = self.root / 'schedule-i-manifest.json'
        path.write_text(json.dumps(root), encoding='utf-8')
        mirror_path = self.root / mirror
        mirror_path.parent.mkdir(parents=True, exist_ok=True)
        mirror_path.write_text(json.dumps(nested), encoding='utf-8')
        return path

    def test_future_helper_wrapper_and_explicit_full_mirror_validate(self):
        self.assertEqual(catalog.validate(self.write_stable(self.full_catalog())), 4)
        nested = self.full_catalog()
        nested['minimumInstallerVersion'] = '0.3.20'
        with self.assertRaises(ValueError):
            catalog.validate(self.write_stable(nested))

    def test_full_mirror_cannot_escape_or_differ_and_legacy_rows_remain_required(self):
        nested = self.full_catalog()
        for mirror in ['../outside-manifest.json', 'schedule-i/../outside-manifest.json']:
            path = self.write_stable(nested, mirror=mirror)
            with self.subTest(mirror=mirror), self.assertRaises(ValueError):
                catalog.validate(path)
        path = self.write_stable(nested)
        (self.root / 'schedule-i/future-helper-manifest.json').write_text('{}')
        with self.assertRaises(ValueError):
            catalog.validate(path)
        path = self.write_stable(nested)
        value = json.loads(path.read_bytes())
        value['runtime']['version'] = '0.3.1'
        path.write_text(json.dumps(value), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'legacy'):
            catalog.validate(path)


if __name__ == '__main__':
    unittest.main()
