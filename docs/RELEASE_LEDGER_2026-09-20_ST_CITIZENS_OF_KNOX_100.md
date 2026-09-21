# Starship Troopers: Citizens of Knox 1.0.0 release ledger

- Published: 2026-09-20
- Release: `mod-assets-2026-09-20-st-citizens-of-knox-1.0.0`
- Main manifest entries: `ST_Citizens_of_Knox`, `ST_Citizens_of_Knox_UI` (new)
- Faded Realms manifest: unchanged; these IDs are not in the live Federated Server pack.

## Content

First public installer catalog release. Project Zomboid 42.20.4 total conversion:

- Arachnid bodies (warrior, hopper, flyer, tank, brain bug) on their own skeletons, AnimSets and voices.
- Twelve Federation / Mobile Infantry occupations and twelve renamed spawn towns.
- Morita family, Federation ammo, MI field gear, belt-clipped lights, lower-back duffels.
- UI companion: Federation front end, Stomper's branding, suit HUD.
- Hybrid FJL plugins `st.citizensofknox` 1.0.0 (`BOTH`) and `st.citizensofknox.ui` 1.0.0 (`CLIENT`).
- Content `require=` remains `ZW_TelekinesisMindOverDead` for PsyOps. That mod is not hosted in this catalog.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `ST_Citizens_of_Knox-v1.0.0.zip` | 22,735,668 | `5984e4cac4564e670997d4f5e24987c293a6caa90cb013c4a8515811b683b6c7` |
| `ST_Citizens_of_Knox_UI-v1.0.0.zip` | 78,163,293 | `d05f468775747248861490f1b374c6000ee93d4bcf1bc8fdd66b89d3ac48064d` |

Both are single-part ZIPs (under the 1800 MB split limit).

## Package validation

- ZIP central directories, portable local headers, and payload CRCs passed `validate_portable_zip_headers`.
- Archive paths use forward slashes and one intended top-level mod root each.
- Content archive: 2,354 files and one `ST_Citizens_of_Knox/42/mod.info`.
- UI archive: 1,581 files and one `ST_Citizens_of_Knox_UI/42/mod.info`.
- No duplicate `mod.info`. `modversion=1.0.0` and matching `javaPluginVersion=1.0.0`.
- Staged from `E:\FadedModsStaging\STCitizensOfKnox-1.0.0-pack-src` through `scripts/package_local_mods.py`.

## Catalog shape

Main gains two new IDs. Faded Realms is not changed. `requiresJavaLoader: true` with plugin fields, matching the hybrid jars. `scripts/validate_manifests.py` passes.
