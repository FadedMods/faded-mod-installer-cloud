# Project Faded Car 2.3.8 release ledger

- Published: 2026-09-08
- Release tag: `mod-assets-2026-09-08-project-faded-car-2.3.8`
- Asset: `ProjectFadedCar-v2.3.8.zip`
- Size: `94382357` bytes
- SHA-256: `8360818bb2cc4f8dd77cc4e0e0387115b29070b2a3480d8e6e50cc21e5cda62e`
- Prepared payload: 1079 files / 131,295,764 bytes
- Required free bytes: `762549033`
- Optional Java plugin: `ProjectFadedCar-CarrierCore-2.3.8.jar` (bundled; FJL not required)

## Source

Canonical staged payload: `E:\Faded Mod Staging\ProjectFadedCar`.
Portable ZIP: `E:\Faded Mod Staging\ProjectFadedCar-v2.3.8.zip`.
Source mirror: `E:\Mod Projects\Project Faded Car\dist\ProjectFadedCar-v2.3.8.zip`.

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

Runtime `id` remains `ProjectFadedCar`. Version `2.3.8` is taken from
`modversion=` in `42/mod.info`.

## Catalog

Both `manifest.json` and `manifests/faded-realms.json` were updated
surgically: version, description, `updated_at`, download URL, zip name, size,
SHA-256, uncompressed size, and required free bytes. No other catalog entries
changed. Java catalog fields were left unset; Carrier Core stays optional.
Main catalog remains 113 entries. Faded Realms remains the live 79-mod pack.

## Notes

2.3.8 repairs the hauler/forklift `IsoCell.getVehicles()` Set indexing crash,
restores namespaced forklift/wrecker/plow/fleet model references, keeps native
fleet script identities, and reduces ordinary mechanical part wear to 25 percent
of the previous loss with fractional carry. Physical engine-bay simulation and
fluids are unchanged.
