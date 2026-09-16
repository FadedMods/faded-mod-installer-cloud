# CSR Clearview GPS 1.3.0 release ledger

- Published: 2026-09-16
- Release: `mod-assets-2026-09-16-csr-clearviewgps-1.3.0`
- Main manifest entry: `CSR_ClearviewGPS` (version update)
- Faded Realms manifest: `CSR_ClearviewGPS` (already in the live `Mods=` pack)

## Content change

1.3.0 adds the live Knox Country web map to the tablet:

- The tablet **Web** button opens `https://network.fadedmods.com/map`.
- While the tablet is in inventory the GPS writes `Zomboid/Lua/CSR_ClearviewGPS/live.txt` so the site can follow the player.
- Multiplayer sandbox option controls whether other tablet users appear on the web map (off / faction / everyone).
- Does not require the in-game FadedNexus mod.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `CSR_ClearviewGPS-v1.3.0.zip` | 1,482,097 | `dc565715c132a4fbf525e98a97264493ab0af570f1031bf415067da348bb609f` |

Single-part ZIP, well under the 1800 MB split limit.

## Package validation

- Staged source: `E:\Faded Mod Staging\CSR_ClearviewGPS`
- Previous staging folder moved to `E:\Faded Mod Staging\backups\CSR_ClearviewGPS-before-1.3.0-20260916-084453`
- Packaged with `scripts/package_local_mods.py`; archive reconstructs as `CSR_ClearviewGPS` with exactly one Build 42 `mod.info` (`CSR_ClearviewGPS/42/mod.info`) and no root duplicate `mod.info`
- `modversion=1.3.0` verified
- Forward-slash entry names; 94 archive entries; `ClearviewGPS_Live.lua` and `ClearviewGPS_LiveServer.lua` present
- Repo validator `tools/validate.ps1` passed before packaging

## Catalog shape

Main and Faded Realms keep the existing `CSR_ClearviewGPS` id. No new id was added. `scripts/validate_manifests.py` passed.

## Local deployment

Staging plus the exact public tree on the client play folders. No Workshop upload.

## Dedicated server deployment

Deployed the exact published tree to `faded-pz-vps` (`The Faded Realms`, B42.20.4):

- Target: `/home/pzserver/Zomboid/mods/CSR_ClearviewGPS`
- Backup: `/home/ubuntu/CSR_ClearviewGPS-before-1.3.0-20260916-124810`
- 60 files, `modversion=1.3.0`; `project-zomboid.service` restarted and reached `*** SERVER STARTED ****`
- FJL server sync reported `Up to date: CSR_ClearviewGPS v1.3.0`; no `CSR_ClearviewGPS` errors in the startup log
