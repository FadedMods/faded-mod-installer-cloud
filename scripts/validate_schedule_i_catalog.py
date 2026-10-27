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


def validate(path):
    raw = path.read_bytes()
    check(0 < len(raw) <= 256 * 1024, 'Catalog size bound')
    data = json.loads(raw, object_pairs_hook=unique_pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Nonfinite JSON')))
    check(type(data) is dict and data.get('schema') == 1 and data.get('product') == 'schedule-i', 'Product/schema')
    check(data.get('channel') == 'production', 'Production catalog required')
    check(type(data.get('helper')) is dict and data['helper'].get('version') == '0.3.1', 'Helper contract')
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
        check(type(entry.get('size')) is int and 0 < entry['size'] <= 192 * 1024 * 1024, 'Component size')
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


if __name__ == '__main__':
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('schedule-i-manifest.json')
    print(f'Schedule I catalog valid: {validate(source)} separate components; signed package verification remains required.')
