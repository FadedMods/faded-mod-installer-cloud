# Military Vehicles Reborn 2.1.1 release ledger

- Published: 2026-09-07
- Release tag: `mod-assets-2026-09-07-military-vehicles-reborn-2.1.1`
- Asset: `MilitaryVehiclesReborn-v2.1.1.zip`
- Size: `274268405` bytes
- SHA-256: `2289fcfcf26faf03dfce69cfe6c3e26fb2a551d790df68a135a1c259fbfe9d9f`
- Prepared payload: 378 files / 524,560,407 bytes
- Required free bytes: `1335699724`

## Source

Staged at `E:\Faded Mod Staging\MilitaryVehiclesReborn-v2.1.1`. The outer folder
and `MilitaryVehiclesReborn-v2.1.1.zip` are a Workshop/handoff bundle
(`Contents/mods`, PDF, preview, `workshop.txt`, validation records). That
bundle was preserved locally and was not published.

The hosted artifact was rebuilt from
`Contents/mods/MilitaryVehiclesReborn` through `scripts/package_local_mods.py`.

## Payload

- One top-level directory: `MilitaryVehiclesReborn/`
- One `mod.info`: `MilitaryVehiclesReborn/42/mod.info`
- No root `mod.info`, no `workshop.txt`, no PDF, no staging metadata
- Forward-slash ZIP paths in both local and central headers
- `testzip()` clean

Runtime `id` remains `MilitaryVehiclesReborn`. Version `2.1.1` is taken from
`version=` / `modversion=` in `42/mod.info`.

## Catalog

Both `manifest.json` and `manifests/faded-realms.json` were updated
surgically: version, description, `updated_at`, download URL, zip name, size,
SHA-256, uncompressed size, and required free bytes. No other catalog entries
changed.

## Not included

The vehicle/weapons PDF and original screenshots remain in Downloads / the
staging folder. They are not part of the installer mod archive.
