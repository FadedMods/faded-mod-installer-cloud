# Common Sense Reborn 1.9.69 release ledger

Published 2026-09-09 from the verified Faded staging trees. Main catalog
updates both CSR identities; Faded Realms updates only its existing Test
identity. Faded Java Loader remains optional.

## Immutable 1.9.68 preserve-at-all-cost backup

Taken before this catalog push. Do not delete, overwrite, or replace with a
newer CSR version.

Desktop folder:

```text
C:\Users\Luis\Desktop\PRESERVE THIS BACKUP AT ALL COST - CSR 1.9.68
```

Mirrored to OneDrive Desktop under the same folder name. Files:

- `CommonSenseReborn-v1.9.68.zip`: 43,430,573 bytes, SHA-256
  `bea9268f1c1a48c63b27ab86783ce1f7bdb11f06571fd3d25b011a9f15db3594`
- `CommonSenseRebornTest-v1.9.68.zip`: 44,918,829 bytes, SHA-256
  `7c1e54bda1290c789edb3fde4f3b0ceaa08bab05ef384f11fcf347803b6042d8`

Those hashes match the previously published 1.9.68 catalog assets and the
local copy at `E:\FadedModsStaging\release-assets-20260906-csr-1.9.68`.
GitHub recovery tag: `mod-assets-2026-09-06-csr-1.9.68-literature-integrations`.

## Immutable 1.9.69 release

- Tag: `mod-assets-2026-09-09-csr-1.9.69-donor-refresh`
- `CommonSenseReborn-v1.9.69.zip`: 64,367,034 bytes, SHA-256
  `259f2b55fa4697889777b0503387b4448f7143d7978dbcb106ca6e16aaffde7d`
- `CommonSenseRebornTest-v1.9.69.zip`: 65,852,267 bytes, SHA-256
  `3ecf00076dd3e09316a768db52d08c03e2a210c31b62badebebe21b7bb48e37d`

Both ZIPs use portable forward-slash paths, contain exactly one Build 42
`mod.info`, reconstruct through `app.installer.prepare_mod_zip` as the
expected IDs, and include `42/java/CommonSenseReborn-Hybrid-1.9.69.jar`.

## Package content

Version 1.9.69 refreshes authorized 42-donor integrations and the sandbox
preset reader. Production has 725 sandbox options; Test has 752. Stove
shutoff and vehicle devices stay off by default.
