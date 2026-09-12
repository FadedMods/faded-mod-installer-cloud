# The Last of Us Complete Edition 1.1.6 release ledger

- Published: 2026-09-12
- Release: `mod-assets-2026-09-12-tlou-complete-edition-1.1.6`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: intentionally unchanged; this is not in the Federated Server pack.
- 1.1.1 through 1.1.5 were staged and withdrawn before public release. Do not publish those versions.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.6-part1.zip` | 1,826,094,152 | `157ebe77506b10425bcdf884176c957e1702a115e9247a862b844ef0445582a4` |
| `TLOU_CompleteEdition-v1.1.6-part2.zip` | 83,294,913 | `4c826820c88acb4161e55d21f6fb8957e26a9c39ab3b17b8385ee9c348e3f952` |
| `TLOU_CompleteEdition_UI-v1.1.6.zip` | 538,147,787 | `68f31972361a734a1ed147d6350a5659e087c80a531840c5b969c3345edcd83c` |

## Package validation

- All three ZIP central directories and payload CRCs passed.
- All archive paths use portable forward slashes and have one intended top-level mod root.
- The two base-mod parts have zero duplicate files (3,304 unique files).
- UI zip has 7,600 files and one `TLOU_CompleteEdition_UI/42/mod.info`.
- `STAGING.txt` is excluded from both packages.
- `mod.info` IDs are `TLOU_CompleteEdition` / `TLOU_CompleteEdition_UI` and `modversion=1.1.6`.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.

## Catalog shape

FJL remains optional. Main catalog entries keep `requiresJavaLoader: false` and omit `javaPluginId` / related Java fields so legacy installer clients do not reject the entire catalog.
