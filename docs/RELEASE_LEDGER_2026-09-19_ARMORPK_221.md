# Release ledger: ArmorPK 2.2.1

Date: 2026-09-19. Owner-authorized metadata repair and full deployment.

## Repair

ArmorPK 2.2.0 supplied `version` but omitted native lowercase `modversion`.
Nexus could not prove the installed version after FJL replaced its changed-entry
receipt on a later startup. The published World pack remained on ArmorPK 2.1.0.
This release supplies both fields as 2.2.1 and makes the source release gate
require them to match the configured version. Nexus verification stays intact.

All 5,569 canonical Build 42 files were compared with the published 2.2.0
source tree: only mod.info changed. No gameplay files were added or removed.
Existing source work was preserved. The source metadata writer was corrected.

## Validation

- Source/staging release gate: PASS, zero problems.
- Port and clothing checks: zero problems/warnings. Asset check: PASS with
  three existing manual visual-review warnings. All 50 Lua files compiled.
- The actual Nexus Java receipt scanner reproduced the missing version in
  2.2.0 and proved 2.2.1 with an empty FJL changed-entry array.
- Historical client/dedicated smoke records were not represented as new tests.

## Assets

Release tag: `mod-assets-2026-09-19-armorpk-2.2.1`.

| ZIP | Bytes | SHA-256 |
| --- | ---: | --- |
| ArmorPK-v2.2.1-part1.zip | 1762856638 | `1a0d2a8373f9a5c763daec6f0e31c863a9724e3fbee21295a3372106372e1d61` |
| ArmorPK-v2.2.1-part2.zip | 1485225721 | `f21279b1d9a1bf66ac11c048c86f34105c0fb9778ddf197fab5d63ba7b41fa2c` |

Uncompressed bytes: 3373198067. Required free bytes: 7158151338.

Staging: `E:\Faded Mod Staging\ArmorPK`; release assets in
`E:\Faded Mod Staging\ArmorPK-2.2.1-release`. Both parts must be installed together.

## Deployment verification

The production installer prepared both ZIP parts together. All 5,570 files
match staging by SHA-256, with exactly one authoritative 42/mod.info.

The local playable copy was updated through the installer backup/replace path
and all 5,570 installed files match. Its previous copy is preserved on E: under
ArmorPK-2.2.1-release/local-backups/ArmorPK_20260919_150921. The backup destination
was overridden for this invocation because the system drive had less than 4 GiB
free; the installer source and replacement/rollback implementation were unchanged.

Main retains 119 entries and Faded Realms retains 79, in their existing order.
Only the ArmorPK catalog entries change.

Publication and deployment completed successfully. Catalog commit `d168ddc`
updated both stable manifests; all three GitHub checks passed. The production
installer downloaded both public archives, verified their SHA-256 values, and
prepared all 5,570 files with exact staging parity.

A fresh zero-player heartbeat preceded the protected backup/restart. Verified
backup: `project-zomboid-20260919T192607Z.tar.zst` (13,162,962,865 bytes).
The service restarted at 19:29:07 UTC. FJL installed ArmorPK 2.2.1 from the two
public assets and changed exactly one mod. All 80 enabled OVH IDs were preserved.
All 5,570 remote files match the release by SHA-256, with no extras and correct
pzserver ownership.

Final readiness at 2026-09-19T19:32:18.610666+00:00: GAME_READY, WorldDictionary completion,
SERVER STARTED, UDP 16261/16262, fresh online heartbeat, and zero crash restarts.
Checked native/registry fatal signatures were absent. This does not claim that
all unrelated historical game/mod warnings have been eliminated.

Nexus accepted the automatic receipt at 19:30:47 UTC and published pack
`sync-20260919T193047Z-f72c2fe3`. Its ArmorPK entry is 2.2.1 and both artifact hashes match
this release. The old WORLD_PACK_SYNC_UNVERSIONED_MOD_CHANGED warning is absent.
The refreshed pack also contains the already-installed EOH 0.5.0 and NSA
0.7.0-alpha. No manual pack publication or relaxed verification was needed.
