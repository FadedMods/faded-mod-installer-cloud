# The Last of Us Complete Edition 1.1.0 release ledger

- Published: 2026-09-12
- Release: `mod-assets-2026-09-12-tlou-complete-edition-1.1.0`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: intentionally unchanged; this is not in the Federated Server pack.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.1.0-part1.zip` | 1,826,092,688 | `7bfdf9350c3c9e5a8c0da6da9024df084691046ecc79f8c197dda3cb19b62293` |
| `TLOU_CompleteEdition-v1.1.0-part2.zip` | 83,294,913 | `4c826820c88acb4161e55d21f6fb8957e26a9c39ab3b17b8385ee9c348e3f952` |
| `TLOU_CompleteEdition_UI-v1.1.0.zip` | 538,559,264 | `f8c54058f10470dc675ab7094877a1a550493292c0d38de9f88c67c4ac6a7c96` |

## Package validation

- All three ZIP central directories and payload CRCs passed.
- All archive paths use portable forward slashes and have one intended top-level mod root.
- The two base-mod parts have zero duplicate files (3,313 unique files).
- UI zip has 7,601 files and one `TLOU_CompleteEdition_UI/42/mod.info`.
- `STAGING.txt` is excluded from both packages.
- `mod.info` IDs are `TLOU_CompleteEdition` / `TLOU_CompleteEdition_UI` and `modversion=1.1.0`.
- Installer `prepare_mod_zip_parts` and `prepare_mod_zip` both succeeded.

## Catalog shape

FJL is optional in 1.1.0 (`required: false` in both plugin descriptors, Lua fallback when FJL is absent). Main catalog entries therefore keep `requiresJavaLoader: false` and omit `javaPluginId` / related Java fields. Adding those fields without `requiresJavaLoader: true` would make legacy installer clients reject the entire catalog.
