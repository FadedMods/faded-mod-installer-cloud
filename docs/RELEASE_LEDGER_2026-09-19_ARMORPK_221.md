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

Publication and protected OVH restart verification are in progress; final
evidence will be appended after verification.
