# Deadflow 0.2.0 release ledger

- Published: 2026-09-06
- Release: `mod-assets-2026-09-06-deadflow-0.2.0`
- Main manifest ID: `Deadflow`
- Faded Realms manifest: intentionally unchanged. Deadflow 0.2.0 is restricted to new Deadflow worlds and must not be injected into the existing Federated Server save.

## Immutable asset

| Asset | Bytes | Uncompressed bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `Deadflow-v0.2.0.zip` | 2,560,615 | 2,564,964 | `ed3c8a55abeb58a0803a3d9bd04f0289a13ac35bde037289f4823f31252e7e7e` |

## Package validation

- All 20 files listed in the supplied staging ledger existed and matched their recorded SHA-256 hashes.
- The release contains 19 runtime files beneath one `Deadflow/` root; staging-control JSON, Workshop description, and the duplicate root `mod.info` are excluded.
- The original staging layout was rejected by the installer because both `Deadflow/mod.info` and `Deadflow/42/mod.info` described the same mod. The release retains only authoritative `Deadflow/42/mod.info`, preserving Build 42 functionality and producing one unambiguous install root.
- ZIP CRC and path-safety checks pass; all entries use portable forward slashes.
- Local installer extraction/preparation passes as `Deadflow` with `42/mod.info`.
- Embedded FJL descriptor matches the manifest: plugin `deadflow.population`, version `0.2.0`, environment `BOTH`, minimum FJL `0.3.4`, exact supported PZ build `42.20.4`.
