# Project Faded Car 2.5.2 + It's A Trap! 2.1.1 release ledger

- Published: 2026-09-23
- Coexistence / WorldDictionary fix for Ping Players server 54191 boot crash

## Project Faded Car 2.5.2

- Release tag: `mod-assets-2026-09-23-project-faded-car-2.5.2`
- Asset: `ProjectFadedCar-v2.5.2.zip`
- Size: `223800552` bytes
- SHA-256: `39067f0d75f158c74dee814800307b0b3b8f69a49d403d55985cf8338c918602`
- Uncompressed: `283814215` bytes / 4,637 files
- Required free bytes: `1044485679`

### Content change

WorkshopCarLift SpriteConfig remapped from `location_business_machinery_01_*` to
`pfc_car_lift_01_*` (face S: 8/12/9; face E: 11/13/10). EngineLift Lua accepts
`pfc_car_lift` sprites. Retains 2.5.1 BlowTorch `flags[Prop1]` fix.

## It's A Trap! 2.1.1

- Release tag: `mod-assets-2026-09-23-its-a-trap-2.1.1`
- Asset: `ItsATrap-v2.1.1.zip`
- Size: `45883958` bytes
- SHA-256: `e13180583ba5f4bd39087ba1077b73388308de7f678d35adcfe326fcd251c386`
- Uncompressed: `49559479` bytes / 1,098 files
- Required free bytes: `632314349`

### Content change

tiledefs `IAT_floor_spikes` / `cheval_wood` / `cheval_metal` moved
8187/8188/8189 → 8190/8191/8192.

## Catalog

Both `manifest.json` and `manifests/faded-realms.json` updated surgically for
`ProjectFadedCar` 2.5.2 and `ItsATrap` 2.1.1. Entries are byte-identical across
Main and Faded Realms for those two ids.

## Local deployment

Local playable trees replaced from staged payloads under
`E:\PZ User Data\Zomboid\mods\` with prior installs moved to
`E:\Faded Mod Staging\backups\`.
