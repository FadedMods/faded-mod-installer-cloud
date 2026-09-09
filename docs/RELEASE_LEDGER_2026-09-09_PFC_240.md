# Project Faded Car 2.4.0 release ledger

- Published: 2026-09-09
- Release tag: `mod-assets-2026-09-09-project-faded-car-2.4.0`
- Asset: `ProjectFadedCar-v2.4.0.zip`
- Size: `92989764` bytes
- SHA-256: `97da642d0a31e7263d8810b405f1ea0275af901dcd3582fe7fbb117a3b181ead`
- Prepared payload: 1080 files / 130,026,839 bytes
- Required free bytes: `759887515`
- Optional Java plugin: `ProjectFadedCar-CarrierCore-2.4.0.jar` (bundled; FJL not required)

## Source

Canonical staged payload: `E:\Faded Mod Staging\ProjectFadedCar`.
Portable ZIP: `E:\Faded Mod Staging\ProjectFadedCar-v2.4.0.zip`.

The published asset is that portable ZIP. It was not rebuilt, because the staged
archive already had installer layout and matched the documented SHA-256.

## Payload

- One top-level directory: `ProjectFadedCar/`
- One `mod.info`: `ProjectFadedCar/42/mod.info`
- No root `mod.info`
- Forward-slash ZIP paths
- `testzip()` clean
- Transport items remain under `ProjectFadedCar/Fleet/commonlibrary/`

Runtime `id` remains `ProjectFadedCar`. Version `2.4.0` is taken from
`modversion=` in `42/mod.info`.

## Catalog

Both `manifest.json` and `manifests/faded-realms.json` were updated
surgically. Main remains 113 entries. Faded Realms remains the live 79-mod pack.
