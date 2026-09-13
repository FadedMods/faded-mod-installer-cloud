# The Last of Us Complete Edition 1.1.8 release ledger

- Published: 2026-09-13
- Release: `mod-assets-2026-09-13-tlou-complete-edition-1.1.8`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: intentionally unchanged; this is not in the Federated Server pack.
- 1.1.1 through 1.1.7 were superseded. 1.1.6 was the previous public catalog build.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.8-part1.zip` | 1,826,238,043 | `3322d51c05f49633d13f9396c5da9d5b071697003b1f65a6bc06630f2319148f` |
| `TLOU_CompleteEdition-v1.1.8-part2.zip` | 83,787,140 | `88f22d8a76ca69288f0e7481d59d5d22b0212bc984fbd135d16bdaa43a70976d` |
| `TLOU_CompleteEdition_UI-v1.1.8.zip` | 538,147,885 | `4263050bbbbf0249f265a46a18544591eefac9d3dcf5e09b2667b20974355e00` |

## Package validation

- All three ZIP central directories and payload CRCs passed.
- All archive paths use portable forward slashes and have one intended top-level mod root.
- The two base-mod parts have zero duplicate files (3,364 unique files).
- UI zip has 7,600 files and one `TLOU_CompleteEdition_UI/42/mod.info`.
- `STAGING.txt` is excluded from both packages.
- `mod.info` IDs are `TLOU_CompleteEdition` / `TLOU_CompleteEdition_UI` and `modversion=1.1.8`.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.

## Catalog shape

FJL remains optional. Main catalog entries keep `requiresJavaLoader: false` and omit `javaPluginId` / related Java fields so legacy installer clients do not reject the entire catalog.
