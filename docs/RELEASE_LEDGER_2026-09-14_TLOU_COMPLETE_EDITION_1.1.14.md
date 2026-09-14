# The Last of Us Complete Edition 1.1.14 release ledger

- Published: 2026-09-14
- Release: `mod-assets-2026-09-14-tlou-complete-edition-1.1.14`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: unchanged; these IDs are not in its live server pack.

## Content change

1.1.13 died on New Game before the occupation screen. Clicking Play loaded
`worldmap-annotations.lua` onto the spawn picker. That file talks to
`WorldMapSymbolsV2`, which the picker never constructs (`uiSymbols` is null),
then `addUntranslatedText` of null, then the game thread exited.

The spawn picker no longer loads annotations. Town names still come from
`worldmap.xml` / `MapLabel.json`; the in-game map still loads annotations
itself. The Listener trait description now uses `%%` so the translator stops
throwing `UnknownFormatConversionException`.

Both mod versions advance to 1.1.14; the Java plugin remains 1.0.0.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.14-part1.zip` | 1,819,398,802 | `24a0e94f04f95ebf976efff01b70182cfe8218506b4c8a3adcfff26f32379c5e` |
| `TLOU_CompleteEdition-v1.1.14-part2.zip` | 91,692,596 | `d296cf87490bdc923e7a294b82fa0279a1582264320df79bffa52b332f779cd4` |
| `TLOU_CompleteEdition_UI-v1.1.14.zip` | 544,862,517 | `9b9a7d3655f610fc7485a19ceb268f932a8070529e8ab1bbe50ca3fa961cf6ba` |

## Package validation

- All three ZIP central directories, portable local headers, and payload CRCs passed.
- Archive paths use forward slashes and the intended top-level mod roots.
- Base multipart archive: 3,547 unique files, zero duplicates (3,221 in part1, 326 in part2).
- UI archive: 7,619 files and one `TLOU_CompleteEdition_UI/42/mod.info`.
- Staging notes are excluded; mod IDs and `modversion=1.1.14` are verified.
- Packaged spawn select does not call `initDirectoryAnnotations`.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.

## Catalog shape

Main keeps its existing entry count. Existing curated descriptions, names, IDs,
and optional Java-loader behavior are preserved. Only version, download
metadata, update date, and storage requirements change for these two entries.
Both retain `requiresJavaLoader: false` and omit catalog Java plugin fields for
legacy client compatibility. `scripts/validate_manifests.py` passes.

## Local deployment

Both installed mods were updated and verified against source: 3,547 base files
and 7,619 UI files, with exact relative paths and SHA-256 parity, zero missing,
zero extra and zero content mismatches. Staging notes were excluded. The
previous local installs were recoverably moved to:

- `E:\Faded Mod Staging\backups\TLOU_CompleteEdition-before-1.1.14-20260914-073014`
- `E:\Faded Mod Staging\backups\TLOU_CompleteEdition_UI-before-1.1.14-20260914-073014`

The local mods directory is reached through the existing Zomboid user-data
junction (`C:\Users\Luis\Zomboid` -> `E:\PZ User Data\Zomboid`). No installer
application rebuild or server deployment was part of this mod release.
