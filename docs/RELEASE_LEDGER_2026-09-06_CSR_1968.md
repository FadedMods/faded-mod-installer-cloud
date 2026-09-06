# Common Sense Reborn 1.9.68 release ledger

Published 2026-09-06 from the verified CSR staging trees. The release keeps
Faded Java Loader optional and updates both CSR identities in the main catalog;
the Faded Realms catalog updates only its existing Test identity.

## Immutable release

- Tag: `mod-assets-2026-09-06-csr-1.9.68-literature-integrations`
- `CommonSenseReborn-v1.9.68.zip`: 43,430,573 bytes, SHA-256
  `bea9268f1c1a48c63b27ab86783ce1f7bdb11f06571fd3d25b011a9f15db3594`
- `CommonSenseRebornTest-v1.9.68.zip`: 44,918,829 bytes, SHA-256
  `7c1e54bda1290c789edb3fde4f3b0ceaa08bab05ef384f11fcf347803b6042d8`

Both ZIPs use portable forward-slash paths, contain exactly one Build 42
`mod.info`, and reconstruct through `app.installer.prepare_mod_zip` as the
expected IDs. Fresh public catalog downloads passed size/hash verification and
portable preparation for both packages. `scripts/validate_manifests.py`, JSON
parsing, and `git diff --check` passed before publication.

## Package content

Version 1.9.68 repairs the Build 42.20.4 literature UI and integrates the
authorized anchored-pose, safe-spawn, injury-feedback, and fire-extinguisher
work. Production contains 665 sandbox options; Test contains 692. The CSR
source repository's B42 package gates passed for both staged identities, and
all 140 Production translation JSON files passed strict UTF-8/no-BOM parsing
with zero placeholder, malformed-percent, or missing-file findings.

## Deployment confirmation

The approved playable Test folder was replaced from the freshly downloaded
public package at `E:\PZ User Data\Zomboid\mods\CommonSenseRebornTest`; its
previous 1.9.67 tree remains recoverable under `E:\FadedModsStaging\playable-backups`.
The Federated Server's normal FJL sync then hash-verified and installed Test
1.9.68 with `changed=1`. The game reached FJL `GAME_READY`, connected its
existing Nexus identity, completed `WorldDictionary.init()`, emitted
`*** SERVER STARTED ****`, and opened UDP 16261/16262 with zero service crash
restarts. Nexus accepted automatic pack
`sync-20260906T152146Z-c75afa3c`.
