"""Validate the separate Schedule I catalog without executing downloaded code."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit


def check(value, message):
    if not value:
        raise ValueError(message)


def unique_pairs(rows):
    result = {}
    for key, value in rows:
        check(key not in result, 'Duplicate JSON property: ' + key)
        result[key] = value
    return result


def validate_object(data):
    check(type(data) is dict and data.get('schema') == 1 and data.get('product') == 'schedule-i', 'Product/schema')
    check(data.get('channel') == 'production', 'Production catalog required')
    check(type(data.get('helper')) is dict and data['helper'].get('version') in {'0.3.1', '0.4.0'}, 'Helper contract')
    maximum_size = (384 if data['helper']['version'] == '0.4.0' else 192) * 1024 * 1024
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
    check(required == dict(framework='Microsoft.NETCore.App', version='10.0.12', architecture='x64', rollForward='Disable'), 'Exact runtime prerequisite')
    check(data['runtime'].get('compatibility', {}).get('steamAppId') == 3164500, 'Steam product identity')
    return len(ids)


def version(value):
    check(type(value) is str and re.fullmatch(r'\d{1,6}\.\d{1,6}\.\d{1,6}', value), 'Release version')
    return tuple(map(int, value.split('.')))


def validate(path):
    raw = path.read_bytes()
    check(0 < len(raw) <= 256 * 1024, 'Catalog size bound')
    data = json.loads(raw, object_pairs_hook=unique_pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Nonfinite JSON')))
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
        check(nested.get('helper', {}).get('version') == '0.4.0' and minimum >= (0, 3, 20), 'Authenticated helper 0.4 installer gate')
        count += validate_object(nested)
        runtime_version = version(nested['runtime']['version'])
        selection = (nested['helper']['version'], minimum, runtime_version)
        check(selection not in selections, 'Duplicate compatible selection')
        selections.add(selection)
        runtime_versions.append((runtime_version, wrapper['minimumInstallerVersion']))
        if path.name == 'schedule-i-manifest.json':
            mirror_path = path.parent / 'schedule-i' / f'{runtime_version[0]}.{runtime_version[1]}-manifest.json'
            check(mirror_path.is_file(), 'Missing full compatible catalog')
            mirror = json.loads(mirror_path.read_bytes(), object_pairs_hook=unique_pairs)
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
