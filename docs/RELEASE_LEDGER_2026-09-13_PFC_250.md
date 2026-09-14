# Project Faded Car 2.5.0 release ledger

- Published: 2026-09-13
- Release tag: `mod-assets-2026-09-13-project-faded-car-2.5.0`
- Asset: `ProjectFadedCar-v2.5.0.zip`
- Size: `223799665` bytes
- SHA-256: `6b249fe607d4e9fc7819362e99ed3a94366eeb2846b143507548aa465c392bca`
- Prepared payload: 4,636 files / 283,812,533 bytes
- Required free bytes: `1044483110`
- Optional Java plugin: `ProjectFadedCar-CarrierCore-2.5.0.jar` (bundled; FJL not required)

## Source

Canonical staged payload: `E:\Faded Mod Staging\ProjectFadedCar`.
Portable ZIP: `E:\Faded Mod Staging\ProjectFadedCar-v2.5.0.zip`.
Versioned release folder: `E:\Faded Mod Staging\ProjectFadedCar-2.5.0-release`.

The published asset is that portable ZIP. It was not rebuilt, because the staged
archive already had installer layout and matched the documented SHA-256.

## Payload

- One top-level directory: `ProjectFadedCar/`
- One `mod.info`: `ProjectFadedCar/42/mod.info`
- One JAR: `ProjectFadedCar/42/java/ProjectFadedCar-CarrierCore-2.5.0.jar`
- No root `mod.info`; no root-level files other than `ProjectFadedCar/`
- 4,636 file entries, no directory entries, forward-slash ZIP paths
- `testzip()` clean; `app.installer.prepare_mod_zip` reconstructs `ProjectFadedCar`

Runtime `id` remains `ProjectFadedCar`. Version `2.5.0` is taken from
`modversion=` in `42/mod.info`.

## Content change

Licensed Steam Workshop vehicle systems are native to Project Faded Car for
Project Zomboid 42.20.4; the playable mod has no donor-folder dependency.
MP-synced high beams with the Skeeve speed-offset flicker fix and reverse fill
lights; idle settle after the driver leaves and instant engine-bay door;
workshop quality/battery/heater/glove-box with rebuild-part and upgrade kits; an
extra tank that feeds the real GasTank; threshold-gated engine/battery stall with
no displayed-condition jump; battery drain tuners; Realistic Mechanics and shop
crane; combined chassis builder; Real Vehicle VFX; safer heavy-part drops;
stable corpse driving; tarp carrier; namespaced Rhino wrecker on the FJL hook
hoist; PFC_RLib rotator UI; FJL hitch-impulse persist and all-tow yaw damping.

## Catalog

Both `manifest.json` and `manifests/faded-realms.json` were updated surgically;
the `ProjectFadedCar` entry is byte-identical in both. No other entries were
added or removed in this release commit. Faded Realms remains the live 79-mod
pack. `scripts/validate_manifests.py` passed.

## Local deployment

The local playable tree was replaced from the staged 2.5.0 payload:

- `E:\PZ User Data\Zomboid\mods\ProjectFadedCar` (reached through the existing
  `C:\Users\Luis\Zomboid` -> `E:\PZ User Data\Zomboid` junction)
- 4,636 files copied; missing/extra/mismatched = 0/0/0; `modversion=2.5.0`
  confirmed.
- Previous 2.4.0 install (1,080 files) recoverably moved to
  `E:\Faded Mod Staging\backups\ProjectFadedCar-before-2.5.0-local-20260913-213203`.

No installer application rebuild, Workshop republish, or production/dedicated
server deployment was part of this release. In-game runtime acceptance was not
performed during this operation.
