# The Last of Us Complete Edition 1.0.0 release ledger

- Published: 2026-09-06
- Release: `mod-assets-2026-09-06-tlou-complete-edition-1.0.0`
- Main manifest entries: `TLOU_CompleteEdition`, `TLOU_CompleteEdition_UI`
- Faded Realms manifest: intentionally unchanged; this is a separate total conversion and was not authorized for Federated Server.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `TLOU_CompleteEdition-v1.0.0-part1.zip` | 1,826,111,058 | `473531a79a3034546f419c6c3e1b0119c6a14669407882c304083a1cb3186f32` |
| `TLOU_CompleteEdition-v1.0.0-part2.zip` | 83,295,225 | `302742f01e29c45f8753ecc899cfb3f4cbf76797f1769d2da3e444938d040ae3` |
| `TLOU_CompleteEdition_UI-v1.0.0.zip` | 538,590,791 | `769d78d7456382e9f4eb59729b51c2fd58b7d0442d832aa61ee74816445e0de4` |

## Package validation

- All three ZIP central directories and payload CRCs passed.
- All archive paths use portable forward slashes and have one intended top-level mod root.
- The two base-mod parts have zero duplicate files.
- `mod.info` IDs and versions match the manifest.
- Embedded FJL descriptors match the published Java metadata: `tlou.completeedition` 1.0.0 (`BOTH`) and `tlou.completeedition.ui` 1.0.0 (`CLIENT`), minimum loader 0.3.0.
- The staged handoff omitted Java-loader fields; the public entries restore them from the matching `mod.info` and embedded plugin descriptors so installation fails closed when FJL is unavailable.
