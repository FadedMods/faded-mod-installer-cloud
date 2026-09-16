# CSR Clearview GPS 1.2.0 release ledger

- Published: 2026-09-15
- Release: `mod-assets-2026-09-15-csr-clearviewgps-1.2.0`
- Main manifest entry: `CSR_ClearviewGPS` (version update)
- Faded Realms manifest: `CSR_ClearviewGPS` (already in the live `Mods=` pack)

## Content change

1.2.0 upgrades the working Navigator GPS with a rare 3D tablet item, gunmetal/carbon tablet UI, and autodrive:

- `CSR_ClearviewGPS.ClearviewGPSTablet` is a placeable electronics item. GPS window and autodrive require it in inventory (sandbox `CSR_ClearviewGPSNeedTablet`, default on).
- Rare loot in military electronics, electronics stores/crates, police/control rooms, and glove boxes. Sandbox spawn toggle.
- GPS window is lockable and resizable, painted as a gunmetal carbon tablet. Purple route line unchanged. Vanilla minimap is hidden while the GPS is open without writing `MiniMap.StartVisible`.
- Autodrive follows the existing Navigator route on a running vehicle. MP module `CSR_ClearviewGPSAuth` re-checks the tablet. Route cache module stays `CSR_ClearviewGPSRouteData`.
- B42.20.4 cache files parse as data (`LuaTableParser`); `loadstring` is gone.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `CSR_ClearviewGPS-v1.2.0.zip` | 1,468,731 | `e1447cd82b5ef5819de37e37f96b48fdad57694ab203a6836b9e7e68fd378977` |

Single-part ZIP, well under the 1800 MB split limit.

## Package validation

- Staged source: `E:\Faded Mod Staging\CSR_ClearviewGPS`
- Previous staging folder moved to `E:\Faded Mod Staging\backups\CSR_ClearviewGPS-before-1.2.0-20260915-223453`
- Packaged with `scripts/package_local_mods.py`; archive reconstructs as `CSR_ClearviewGPS` with exactly one Build 42 `mod.info` (`CSR_ClearviewGPS/42/mod.info`)
- `modversion=1.2.0` verified
- Forward-slash entry names; 58 archive entries including `models_X/WorldItems/ClearviewGPSTablet.fbx` and `Item_ClearviewGPSTablet.png`
- Repo validator `tools/validate.ps1` passed before packaging

## Catalog shape

Main and Faded Realms keep the existing `CSR_ClearviewGPS` id. No new id was added. `scripts/validate_manifests.py` passed.

## Local deployment

Staging only to `E:\Faded Mod Staging`. No Workshop upload.
