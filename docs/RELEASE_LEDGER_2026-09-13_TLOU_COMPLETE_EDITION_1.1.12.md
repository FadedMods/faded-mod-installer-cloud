# The Last of Us Complete Edition 1.1.12 release ledger

- Published: 2026-09-13
- Release: `mod-assets-2026-09-13-tlou-complete-edition-1.1.12`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: unchanged; these IDs are not in its live server pack.

## Content change

Repair-menu context actions. In 1.1.11 the port renamed `CSR_ContextMenu`
before converting the `CSR_ContextMenuRouter` calls, so all eight repair-menu
router calls targeted a nonexistent global and right-clicking an item threw
`attempted index: addOption of non-table: null` (`TLOU_CE_RepairMenu.lua`
lines 48, 101 and 143). The rename now happens after the router calls are
converted, and the port stops if any ported file still reaches for a router.
`verify_b42_globals.py` now checks calls on global tables; `test_repair_menu.lua`
is new. Both mod versions advance to 1.1.12; the Java plugin remains 1.0.0.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.12-part1.zip` | 1,825,080,487 | `bf5c03d3c1f77b274c56771c46e672bbd2c13a88ae2553b358524958b656046e` |
| `TLOU_CompleteEdition-v1.1.12-part2.zip` | 85,519,702 | `4bd0fec363a16cc9793e9e466f138062c0d374fcd7c1cbbb3b0dee8420f21cff` |
| `TLOU_CompleteEdition_UI-v1.1.12.zip` | 538,902,113 | `f92835f50bf06d84caaa8a4517952448d9d9f65c841f8917c8822cbc475d571f` |

## Package validation

- All three ZIP central directories, portable local headers, and payload CRCs passed.
- Archive paths use forward slashes and the intended top-level mod roots.
- Base multipart archive: 3,484 unique files, zero duplicates (3,188 in part1, 296 in part2).
- UI archive: 7,601 files and one `TLOU_CompleteEdition_UI/42/mod.info`.
- Staging notes are excluded; mod IDs and `modversion=1.1.12` are verified.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.

## Catalog shape

Main retains 115 entries. Existing curated descriptions, names, IDs, update
date, and optional Java-loader behavior are preserved. Only version, download
metadata, and storage requirements change for these two entries. Both retain
`requiresJavaLoader: false` and omit catalog Java plugin fields for legacy
client compatibility. `scripts/validate_manifests.py` passes.

## Local deployment

Both installed mods were updated and verified against source and staging:
3,484 base files and 7,601 UI files, with exact relative paths and SHA-256
parity, zero missing, zero extra and zero content mismatches. Staging notes
were excluded. The previous local installs were recoverably moved to:

- `E:\Faded Mod Staging\backups\TLOU_CompleteEdition-before-1.1.12-20260913-151521`
- `E:\Faded Mod Staging\backups\TLOU_CompleteEdition_UI-before-1.1.12-20260913-151521`

The local mods directory is reached through the existing Zomboid user-data
junction (`C:\Users\Luis\Zomboid` -> `E:\PZ User Data\Zomboid`). No installer
application rebuild or server deployment was part of this mod release.
In-game runtime acceptance was not performed during this release operation.
