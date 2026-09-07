# Project Faded Car 2.3.7 release ledger

- Published: 2026-09-07
- Release tag: `mod-assets-2026-09-07-project-faded-car-2.3.7`
- Asset: `ProjectFadedCar-v2.3.7.zip`
- Size: `94374433` bytes
- SHA-256: `7309fbba05141ca7a3a7fda624be699c540d1dc0adae968ff12fdd24c6a73108`
- Prepared payload: 1076 files / 131,290,191 bytes
- Required free bytes: `762535536`
- Optional Java plugin: `ProjectFadedCar-CarrierCore-2.3.7.jar` (bundled; FJL not required)

## Source

Canonical staged payload: `E:\Faded Mod Staging\ProjectFadedCar`.
Portable ZIP: `E:\Faded Mod Staging\ProjectFadedCar-2.3.7-release\ProjectFadedCar-v2.3.7.zip`.

The published asset is that portable ZIP. It was not rebuilt, because the staged
archive already had installer layout and matched the documented SHA-256.

## Payload

- One top-level directory: `ProjectFadedCar/`
- One `mod.info`: `ProjectFadedCar/42/mod.info`
- No root `mod.info`
- Forward-slash ZIP paths in both local and central headers
- `testzip()` clean
- Transport items remain `module ProjectFadedCar` under
  `42/media/scripts/ProjectFadedCar/Fleet/commonlibrary/transport_item.txt`
  (not the quarantined generic `42/media/scripts/commonlibrary/transport_item.txt`
  path and not `Base.Transport*` IDs)

Runtime `id` remains `ProjectFadedCar`. Version `2.3.7` is taken from
`modversion=` in `42/mod.info`.

## Catalog

Both `manifest.json` and `manifests/faded-realms.json` were updated
surgically: version, description, `updated_at`, download URL, zip name, size,
SHA-256, uncompressed size, and required free bytes. No other catalog entries
changed. Java catalog fields were left unset; Carrier Core stays optional.
