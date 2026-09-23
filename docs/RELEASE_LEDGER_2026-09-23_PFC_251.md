# Project Faded Car 2.5.1 release ledger

- Published: 2026-09-23
- Release tag: `mod-assets-2026-09-23-project-faded-car-2.5.1`
- Asset: `ProjectFadedCar-v2.5.1.zip`
- Size: `223799664` bytes
- SHA-256: `76f09be6b47aad1c10d6e5e42917b0fb61c84dc5b88b2279aa747495a06bd355`
- Prepared payload: 4,636 files / 283,812,529 bytes
- Required free bytes: `1044483110`
- Optional Java plugin: `ProjectFadedCar-CarrierCore-2.5.0.jar` (bundled; FJL not required; version stamp unchanged from 2.5.0)

## Source

Canonical staged payload: `E:\Faded Mod Staging\ProjectFadedCar`.
Portable ZIP: `E:\Faded Mod Staging\ProjectFadedCar-v2.5.1.zip`.
Versioned release folder: `E:\Faded Mod Staging\ProjectFadedCar-2.5.1-release`.

The published asset is that portable ZIP. It was not rebuilt for GitHub upload;
the staged archive already had installer layout and matched the documented SHA-256.

## Payload

- One top-level directory: `ProjectFadedCar/`
- One `mod.info`: `ProjectFadedCar/42/mod.info` (`modversion=2.5.1`)
- One JAR: Carrier Core (bundled)
- 4,636 file entries, forward-slash ZIP paths
- Propane craft-flag count: 0 (`flags[Prop1]` on weld/frame recipes)

## Content change

BlowTorch craft inputs that used invalid `flags[Propane]` (no such InputFlag)
in recipes `PFC_WeldEngineParts` and `PFC_BuildVehicleFrame` now use
`flags[Prop1]`, matching the rest of PFC and unblocking server WorldDictionary
load. All 2.5.0 native workshop vehicle systems are unchanged.

## Catalog

Both `manifest.json` and `manifests/faded-realms.json` were updated surgically;
the `ProjectFadedCar` entry is byte-identical in both. No other entries were
added or removed in this release commit.

## Local deployment

The local playable tree is replaced from the staged 2.5.1 payload:

- `E:\PZ User Data\Zomboid\mods\ProjectFadedCar`
- Prior install recoverably moved under `E:\Faded Mod Staging\backups\`.

No installer application rebuild or Workshop republish. PingPlayers 54191
ServerSync uses Main `manifest.json` with `forceServerSync=true` (no PFC
version pin), so Stop→Start pulls 2.5.1 after this catalog commit lands on main.
