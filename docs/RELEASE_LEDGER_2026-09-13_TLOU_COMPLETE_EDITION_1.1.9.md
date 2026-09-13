# The Last of Us Complete Edition 1.1.9 release ledger

- Published: 2026-09-13
- Release: `mod-assets-2026-09-13-tlou-complete-edition-1.1.9`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: intentionally unchanged; this is not in the Federated Server pack.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.9-part1.zip` | 1,825,591,711 | `503040e5f1dfe5e2be8d52625d3205ff044d609c9802ae29ed99738b42f538ed` |
| `TLOU_CompleteEdition-v1.1.9-part2.zip` | 84,717,428 | `1fe80f6d4bb5d48bec23ac30bd81d96ce3837aa9ad3e283b7c28ea5701db833e` |
| `TLOU_CompleteEdition_UI-v1.1.9.zip` | 538,155,015 | `57ec61a8377ee5a190b6b3a6f69b50c3f9d55c5b7ab7b7f6bdd4f4e3e6c4b491` |

## Package validation

- All three ZIP central directories and payload CRCs passed.
- All archive paths use portable forward slashes and have one intended top-level mod root.
- The two base-mod parts have zero duplicate files (3,441 unique files).
- UI zip has 7,601 files and one `TLOU_CompleteEdition_UI/42/mod.info`.
- `STAGING.txt` is excluded from both packages.
- `mod.info` IDs are `TLOU_CompleteEdition` / `TLOU_CompleteEdition_UI` and `modversion=1.1.9`.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.

## Catalog shape

FJL remains optional. Main catalog entries keep `requiresJavaLoader: false` and omit `javaPluginId` / related Java fields so legacy installer clients do not reject the entire catalog.
