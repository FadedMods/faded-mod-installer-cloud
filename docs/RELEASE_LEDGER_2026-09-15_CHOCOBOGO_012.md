# Chocobo Go 0.1.2 release ledger

- Published: 2026-09-15
- Release: `mod-assets-2026-09-15-chocobogo-0.1.2`
- Main manifest entry: `ChocoboGo` (version update)
- Faded Realms manifest: unchanged. This id is not in the live server `Mods=` pack.

## Content change

0.1.1 shipped the `ChocoboGo.Feather` item with the companion portrait icon and no world/inventory mesh. 0.1.2 adds the missing 3D ground feather:

- Shared `models_X/ChocoboGo/Feather.x` mesh, plumage atlases, and inventory icons for yellow, green, blue, black, and gold.
- Color-matched `featherItem` / butchering drops from each breed.
- Native `Tags = base:feather` and `DisplayCategory = AnimalPart`.
- Java plugin remains 0.1.1. Full features still require Faded's Java Loader 0.3.4 and FadedJavaLoaderBridge.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `ChocoboGo-v0.1.2.zip` | 37,890,547 | `1d34698d7e88d481bab24888e0b28a986652506fbe518027559284502bcfac2b` |

Single-part ZIP, well under the 1800 MB split limit. GitHub's own upload digest matches the local SHA-256 value above.

## Package validation

- Staged source: `E:\Faded Mod Staging\ChocoboGo` (full dist) and installer pack-src `E:\Faded Mod Staging\ChocoboGo-0.1.2-pack-src\ChocoboGo`.
- Previous staging folder moved to `E:\Faded Mod Staging\backups\ChocoboGo-before-0.1.2-20260915-212139`.
- Packaged with `scripts/package_local_mods.py`; archive reconstructs as `ChocoboGo` with exactly one Build 42 `mod.info`.
- `modversion=0.1.2` verified from the packaged `mod.info`.
- Forward-slash entry names only; `validate_portable_zip_headers` passed.
- `app.installer.prepare_mod_zip` reconstructs the archive as `ChocoboGo` and includes `42/media/models_X/ChocoboGo/Feather.x`.
- 322 archive entries; 12 feather mesh/texture/icon files.

## Catalog shape

Main keeps the existing `ChocoboGo` id. Java-loader fields are preserved; `javaPluginVersion` stays `0.1.1` because the native JAR is unchanged. `scripts/validate_manifests.py` passes. No Faded Realms catalog change was made.

## Local deployment

No Zomboid `mods` install, installer rebuild, Workshop upload, or server deployment was part of this release. In-game runtime acceptance was not performed during this release operation.
