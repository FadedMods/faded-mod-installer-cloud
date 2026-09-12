# The Last of Us Complete Edition 1.1.2 release ledger

- Published: 2026-09-12
- Release: `mod-assets-2026-09-12-tlou-complete-edition-1.1.2`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: intentionally unchanged; this is not in the Federated Server pack.
- 1.1.1 was staged and withdrawn before any public release. Do not publish 1.1.1.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.2-part1.zip` | 1,826,093,431 | `9153073bd7225ded23827a3d5e2946b5b23ca7981afa918234210b34d65dbf44` |
| `TLOU_CompleteEdition-v1.1.2-part2.zip` | 83,294,913 | `4c826820c88acb4161e55d21f6fb8957e26a9c39ab3b17b8385ee9c348e3f952` |
| `TLOU_CompleteEdition_UI-v1.1.2.zip` | 538,559,264 | `aa9a3645747ef8c9e38577fb5b01fdfc3877d282ff931107ff7a10d0c76ec347` |

## Package validation

- All three ZIP central directories and payload CRCs passed.
- All archive paths use portable forward slashes and have one intended top-level mod root.
- The two base-mod parts have zero duplicate files (3,313 unique files).
- UI zip has 7,601 files and one `TLOU_CompleteEdition_UI/42/mod.info`.
- `STAGING.txt` is excluded from both packages.
- `mod.info` IDs are `TLOU_CompleteEdition` / `TLOU_CompleteEdition_UI` and `modversion=1.1.2`.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.

## Catalog shape

FJL remains optional (`required: false` in both plugin descriptors). Main catalog entries keep `requiresJavaLoader: false` and omit `javaPluginId` / related Java fields so legacy installer clients do not reject the entire catalog.
