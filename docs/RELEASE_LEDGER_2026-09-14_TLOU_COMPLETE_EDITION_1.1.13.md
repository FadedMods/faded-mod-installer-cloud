# The Last of Us Complete Edition 1.1.13 release ledger

- Published: 2026-09-14
- Release: `mod-assets-2026-09-14-tlou-complete-edition-1.1.13`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: unchanged; these IDs are not in its live server pack.

## Content change

Spawn-screen and occupation roster work for the total conversion:

- Every vanilla town is offered on the spawn picker, including regions vanilla
  locks behind Sandbox-only, plus a Seattle row that zooms to the Louisville
  cells already in the Muldraugh map.
- Custom occupation keys get spawn coordinates so TLOU jobs still receive a
  house list.
- The panning map loads worldmap-annotations so town names come from MapLabel
  translations instead of the four baked Kentucky labels.
- Occupation filter keeps the ten authored TLOU jobs plus Unemployed, matching
  registered profession ids instead of display names.
- Trait/profession art and world-map badges were refreshed.

Both mod versions advance to 1.1.13; the Java plugin remains 1.0.0.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.13-part1.zip` | 1,819,398,789 | `b466c115d08d9a4278e891d1b6e2c861c3ca606213e42de275b823cca169fac1` |
| `TLOU_CompleteEdition-v1.1.13-part2.zip` | 91,692,596 | `d296cf87490bdc923e7a294b82fa0279a1582264320df79bffa52b332f779cd4` |
| `TLOU_CompleteEdition_UI-v1.1.13.zip` | 544,862,517 | `54d796c0a6dafa43ddeceb3716c476d0a3f7b87e39c990799c57ad042b0ea0ee` |

## Package validation

- All three ZIP central directories, portable local headers, and payload CRCs passed.
- Archive paths use forward slashes and the intended top-level mod roots.
- Base multipart archive: 3,547 unique files, zero duplicates (3,221 in part1, 326 in part2).
- UI archive: 7,619 files and one `TLOU_CompleteEdition_UI/42/mod.info`.
- Staging notes are excluded; mod IDs and `modversion=1.1.13` are verified.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.

## Catalog shape

Main keeps its existing entry count. Existing curated descriptions, names, IDs,
and optional Java-loader behavior are preserved. Only version, download
metadata, update date, and storage requirements change for these two entries.
Both retain `requiresJavaLoader: false` and omit catalog Java plugin fields for
legacy client compatibility. `scripts/validate_manifests.py` passes.

## Local deployment

Both installed mods were updated from source after a recoverable backup of the
previous playable copies. Staging notes were excluded. The local mods directory
is reached through the existing Zomboid user-data junction
(`C:\Users\Luis\Zomboid` -> `E:\PZ User Data\Zomboid`). No installer application
rebuild or server deployment was part of this mod release. In-game runtime
acceptance was not performed during this release operation.
