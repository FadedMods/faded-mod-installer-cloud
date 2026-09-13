# The Last of Us Complete Edition 1.1.10 release ledger

- Release date: 2026-09-13
- Release: `mod-assets-2026-09-13-tlou-complete-edition-1.1.10`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: unchanged; these IDs are not in its live server pack.

## Content change

Combat Text and its health-bar manager replace unsupported Kahlua `next()` empty-table calls with `pairs()`-based checks. Both mod versions advance to 1.1.10; the Java plugin version remains 1.0.0.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.10-part1.zip` | 1,825,591,941 | `d51ca9069c3b2052334e1f1ca6d5a5f4c4e8b95a36df73b4a4bef0fbd189c482` |
| `TLOU_CompleteEdition-v1.1.10-part2.zip` | 84,717,428 | `1fe80f6d4bb5d48bec23ac30bd81d96ce3837aa9ad3e283b7c28ea5701db833e` |
| `TLOU_CompleteEdition_UI-v1.1.10.zip` | 538,155,011 | `cf1059c4d7acd50d380cb78ebe227ffc2ecc7c563e35b17132abcc7ebbfbee53` |

## Package validation

- All three ZIP central directories, portable local headers, and payload CRCs passed.
- Archive paths use forward slashes and the intended top-level mod roots.
- Base multipart archive: 3,441 unique files, zero duplicates.
- UI archive: 7,601 files.
- Staging notes are excluded; mod IDs and `modversion=1.1.10` are verified.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.
- Source B42 global-call audit passed across 182 Lua files.
- Local manifest safety validation passed.

## Catalog shape

Main retains 115 entries. Existing curated descriptions, names, IDs, update date, and optional Java-loader behavior are preserved. Only version, download metadata, and storage requirements change for these two entries. Both retain `requiresJavaLoader: false` and omit catalog Java plugin fields for legacy client compatibility.

## Local deployment

Both installed mods were updated and verified against source and staging: 3,441 base files and 7,601 UI files, with exact relative paths and SHA-256 parity. Eleven pre-existing filename capitalization differences were corrected to source casing; no extra files remained. Staging notes were excluded.

The local mods directory is reached through the existing Zomboid user-data junction. No installer application rebuild or server deployment was part of this mod release. In-game runtime acceptance was not performed during this release operation.
