"""Validate the separate Schedule I catalog without executing downloaded code."""
import base64
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


TRUST_PATH = Path(__file__).resolve().parents[1] / 'schedule-i/fadedcore-release.json'
TRUST_SHA256 = 'a7c12a1d68502061cd2597d20425049d49264eb47fd4cd0734c843028cdafd33'
SIGNATURE_DOMAIN = b'FadedCore.HelperRelease.v1\n'
HELPER_FILES = {'FadedCore.Packages.dll', 'FadedCore.Packages.deps.json', 'FadedCore.Packages.runtimeconfig.json'}
MAX_HELPER_ARCHIVE = 16 * 1024 * 1024


def check(value, message):
    if not value:
        raise ValueError(message)


def unique_pairs(rows):
    result = {}
    for key, value in rows:
        check(key not in result, 'Duplicate JSON property: ' + key)
        result[key] = value
    return result


def json_document(raw, maximum):
    check(0 < len(raw) <= maximum, 'JSON byte bound')
    value = json.loads(raw, object_pairs_hook=unique_pairs,
                       parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Nonfinite JSON')))
    check(type(value) is dict, 'JSON object required')
    return value


def digest(value):
    return type(value) is str and re.fullmatch(r'[a-f0-9]{64}', value)


def component_version(value):
    check(type(value) is str and re.fullmatch(r'\d{1,6}\.\d{1,6}\.\d{1,6}(?:-[A-Za-z0-9.-]{1,64})?', value), 'Component version')
    numeric, separator, preview = value.partition('-')
    return tuple(map(int, numeric.split('.'))) + (0 if separator else 1, preview)


def decode64(value, maximum):
    check(type(value) is str and 0 < len(value) <= ((maximum + 2) // 3) * 4, 'Signature envelope bound')
    raw = base64.b64decode(value, validate=True)
    check(0 < len(raw) <= maximum and base64.b64encode(raw).decode('ascii') == value, 'Canonical base64 envelope')
    return raw


def validate_helper_release(envelope):
    """Authenticate helper metadata using repository-pinned public trust only.

    This independently implements the installer bootstrap's schema-1 protocol;
    downloaded catalog keys, helpers and executables are never used by CI.
    """
    check(type(envelope) is dict and set(envelope) == {'payload', 'signature'}, 'Signed helper envelope')
    raw, signature = decode64(envelope['payload'], 32768), decode64(envelope['signature'], 1024)
    trust_raw = TRUST_PATH.read_bytes()
    check(hashlib.sha256(trust_raw).hexdigest() == TRUST_SHA256, 'Independently pinned helper publisher trust')
    trust = json_document(trust_raw, 32768)
    key = serialization.load_pem_public_key(trust['publicKeyPem'].encode('ascii'))
    check(isinstance(key, rsa.RSAPublicKey) and 3072 <= key.key_size <= 8192, 'Helper publisher key strength')
    key_id = hashlib.sha256(key.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)).hexdigest()
    check(trust.get('schema') == 1 and trust.get('channel') == 'production' and trust.get('keyId') == key_id, 'Pinned publisher identity')
    try:
        key.verify(signature, SIGNATURE_DOMAIN + raw,
                   padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32), hashes.SHA256())
    except InvalidSignature as exc:
        raise ValueError('Helper publisher signature mismatch') from exc
    value = json_document(raw, 32768)
    check(set(value) == {'schema', 'product', 'component', 'channel', 'keyId', 'version', 'contractSchema',
                         'minimumInstallerVersion', 'platform', 'prerequisites', 'archive', 'files'}, 'Helper descriptor fields')
    check(type(value['schema']) is int and value['schema'] == 1 and value['product'] == 'schedule-i' and
          value['component'] == 'package-helper' and value['channel'] == 'production' and value['keyId'] == key_id and
          type(value['contractSchema']) is int and value['contractSchema'] == 1 and value['platform'] == 'windows-x64', 'Signed helper protocol')
    check(component_version(value['version']) >= component_version('0.4.0'), 'Helper bootstrap version floor')
    check(component_version(value['minimumInstallerVersion']) >= component_version('0.3.21'), 'Signed helper installer floor')
    required = value['prerequisites']
    check(type(required) is dict and set(required) == {'framework', 'version', 'architecture', 'rollForward'} and
          required['framework'] == 'Microsoft.NETCore.App' and required['architecture'] == 'x64' and
          required['rollForward'] == 'Disable', 'Authenticated exact x64 runtime policy')
    version(required['version'])
    archive = value['archive']
    check(type(archive) is dict and set(archive) == {'url', 'size', 'sha256'} and
          type(archive['size']) is int and 0 < archive['size'] <= MAX_HELPER_ARCHIVE and digest(archive['sha256']), 'Signed helper archive')
    check(type(archive['url']) is str and len(archive['url']) <= 2048, 'Signed helper URL bound')
    url = urlsplit(archive['url'])
    check(url.scheme == 'https' and url.hostname == 'github.com' and url.port in (None, 443) and
          not any((url.username, url.password, url.query, url.fragment)) and
          re.fullmatch(r'/FadedMods/faded-mod-installer-cloud/releases/download/[A-Za-z0-9._-]+/[A-Za-z0-9._-]+\.zip', url.path), 'Signed immutable helper release URL')
    rows = value['files']
    check(type(rows) is list and len(rows) == 3, 'Closed helper file count')
    names = set()
    for row in rows:
        check(type(row) is dict and set(row) == {'path', 'size', 'sha256'} and row['path'] in HELPER_FILES and
              row['path'] not in names and type(row['size']) is int and 0 < row['size'] <= MAX_HELPER_ARCHIVE and digest(row['sha256']), 'Signed helper file inventory')
        names.add(row['path'])
    check(names == HELPER_FILES and sum(row['size'] for row in rows) <= 2 * MAX_HELPER_ARCHIVE, 'Closed bounded helper layout')
    return value


def validate_object(data):
    check(type(data) is dict and type(data.get('schema')) is int and data.get('schema') == 1 and data.get('product') == 'schedule-i', 'Product/schema')
    check(data.get('channel') == 'production', 'Production catalog required')
    helper = data.get('helper')
    check(type(helper) is dict, 'Helper object')
    helper_version = helper.get('version')
    signed = validate_helper_release(helper['signedRelease']) if 'signedRelease' in helper else None
    if signed is None:
        check(helper_version in {'0.3.1', '0.4.0'}, 'Unknown helpers require a publisher-signed release')
    else:
        check(helper_version == signed['version'] and type(helper.get('contractSchema')) is int and
              helper.get('contractSchema') == signed['contractSchema'], 'Signed helper version/protocol agreement')
        check(all(helper.get(key) == signed['archive'][key] for key in ('url', 'size', 'sha256')), 'Signed helper archive agreement')
        if helper_version != '0.4.0':
            check(component_version(data.get('minimumInstallerVersion')) >= component_version(signed['minimumInstallerVersion']), 'Future helper bootstrap gate')
    maximum_size = (192 if helper_version == '0.3.1' else 384) * 1024 * 1024
    check(type(data.get('runtime')) is dict and type(data.get('sdk')) is dict and type(data.get('mods')) is list, 'Component groups')
    check(len(data['mods']) <= 128, 'Mod count bound')
    check(data['runtime'].get('id') == 'fadedcore.suite' and data['sdk'].get('id') == 'fadedcore.sdk', 'Runtime/SDK identities')
    ids = set()
    for entry, kind in [(data['runtime'], 'runtime-suite'), (data['sdk'], 'sdk')] + [(row, 'mod') for row in data['mods']]:
        check(type(entry) is dict, 'Component object')
        identity = entry.get('id')
        check(type(identity) is str and re.fullmatch(r'[a-z0-9][a-z0-9._-]{0,127}', identity), 'Component identity')
        check(identity not in ids and entry.get('kind') == kind, 'Unique component identity/kind')
        ids.add(identity)
        check(type(entry.get('version')) is str and re.fullmatch(r'\d{1,6}\.\d{1,6}\.\d{1,6}(?:-[A-Za-z0-9.-]{1,64})?', entry['version']), 'Component version')
        check(type(entry.get('size')) is int and 0 < entry['size'] <= maximum_size, 'Component size')
        check(type(entry.get('sha256')) is str and re.fullmatch(r'[a-f0-9]{64}', entry['sha256']), 'Component SHA256')
        check(type(entry.get('url')) is str, 'Component URL string')
        url = urlsplit(entry['url'])
        check(url.scheme == 'https' and url.hostname == 'github.com' and url.port in (None, 443) and
              not any((url.username, url.password, url.query, url.fragment)), 'HTTPS release origin')
        check(re.fullmatch(r'/FadedMods/faded-mod-installer-cloud/releases/download/[^/]+/[^/]+', url.path), 'Versioned release path')
        check(url.path.endswith('.zip' if kind == 'sdk' else '.fmod'), 'Component file type')
    required = data.get('prerequisites', {})
    expected = signed['prerequisites'] if signed else dict(framework='Microsoft.NETCore.App', version='10.0.12', architecture='x64', rollForward='Disable')
    check(required == expected, 'Authenticated exact runtime prerequisite')
    check(data['runtime'].get('compatibility', {}).get('steamAppId') == 3164500, 'Steam product identity')
    return len(ids)


def version(value):
    check(type(value) is str and re.fullmatch(r'\d{1,6}\.\d{1,6}\.\d{1,6}', value), 'Release version')
    return tuple(map(int, value.split('.')))


def validate(path):
    raw = path.read_bytes()
    data = json_document(raw, 256 * 1024)
    count = validate_object(data)
    variants = data.get('compatibleCatalogs', [])
    check(type(variants) is list and len(variants) <= 8, 'Compatible catalog bound')
    selections = set()
    runtime_versions = []
    for wrapper in variants:
        check(type(wrapper) is dict and type(wrapper.get('catalog')) is dict, 'Compatible catalog wrapper')
        minimum = version(wrapper.get('minimumInstallerVersion'))
        nested = wrapper['catalog']
        check('compatibleCatalogs' not in nested, 'Nested compatibility wrappers are refused')
        check(nested.get('minimumInstallerVersion') == wrapper['minimumInstallerVersion'], 'Minimum installer agreement')
        helper_version = nested.get('helper', {}).get('version')
        check((helper_version == '0.4.0' and minimum >= (0, 3, 20)) or
              (helper_version != '0.4.0' and minimum >= (0, 3, 21) and 'signedRelease' in nested.get('helper', {})), 'Compatible helper bootstrap gate')
        count += validate_object(nested)
        runtime_version = version(nested['runtime']['version'])
        selection = (nested['helper']['version'], minimum, runtime_version)
        check(selection not in selections, 'Duplicate compatible selection')
        selections.add(selection)
        runtime_versions.append((runtime_version, wrapper['minimumInstallerVersion']))
        if path.name == 'schedule-i-manifest.json':
            mirror_name = wrapper.get('manifestPath', f'schedule-i/{runtime_version[0]}.{runtime_version[1]}-manifest.json')
            check(type(mirror_name) is str and re.fullmatch(r'schedule-i/[A-Za-z0-9][A-Za-z0-9._-]{0,95}-manifest\.json', mirror_name), 'Full catalog mirror path')
            mirror_path = path.parent / mirror_name
            check(mirror_path.is_file(), 'Missing full compatible catalog')
            mirror = json_document(mirror_path.read_bytes(), 256 * 1024)
            check(mirror == nested, 'Compatible catalog and full catalog differ')
    if path.name == 'schedule-i-manifest.json':
        check(data['helper']['version'] == '0.3.1' and data['runtime']['version'] == '0.3.0', 'Retain legacy client entries')
    if variants:
        latest = max(runtime_versions)
        check(version(data.get('latestRuntimeVersion')) == latest[0], 'Latest runtime pointer')
        check(data.get('minimumInstallerVersionForLatest') == latest[1], 'Latest installer pointer')
    return count


if __name__ == '__main__':
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('schedule-i-manifest.json')
    print(f'Schedule I catalog valid: {validate(source)} separate components; signed package verification remains required.')
