# Character Creator 2.6.1

Release: `mod-assets-2026-09-24-character-creator-2.6.1`.

Owner-authorized completion of the Character Creator update process: version
bump, staging and local install, old mod-backup cleanup, fresh archive upload,
all existing catalog entries, and OVH protected backup/restart.

## Package and scope

- `CharacterCreator-v2.6.1.zip`: 1,280,782,185 bytes.
- SHA-256: `f69257c3b097b9982bb5004345c63efb0e13108004b147df2b4d5b2e590c172a`.
- Expanded: 1,647,649,013 bytes; required free space: 3,465,302,110 bytes.
- 13,648 files under `CharacterCreator/`; exactly one `42/mod.info`.
- Compared with 2.6.0, only `42/mod.info` and `CC_Core.lua` version strings change.
  The source-root duplicate manifest is bumped but excluded from the archive.
- Body assets and the `charactercreator.morph` 1.0.0 CLIENT/HYBRID renderer are
  unchanged; minimum FJL remains 0.3.4.

## Catalogs

Main and Faded Realms both advance their existing CharacterCreator entries to
2.6.1. Their 123/79 IDs and ordering, other mods and top-level loader channels
are preserved. All other catalog files were inspected and contain no matching
entry. CharacterCreator is now included in the catalog validator's synchronized
release IDs; a focused regression check confirms that the old 2.6.0/2.4.0
mismatch is rejected. The old ledger's OVH-based Faded Realms holdback is ended
by this owner's explicit instruction to update every manifest and restart OVH.
OVH and the PingPlayers Faded Realms host remain distinct servers.

## Verification and local deployment

Source gates pass before and after the version bump. ZIP SHA-256, CRC, portable
headers, installer preparation, Java declaration and exact source parity pass.
Canonical staging (`E:/Faded Mod Staging/CharacterCreator`) and the local install
(`E:/PZ User Data/Zomboid/mods/CharacterCreator`) each match all 13,648 files.
The local schema-2 FJL profile keeps `pluginSource: modList`; CharacterCreator
remains selected in the game mod list with no explicit Java disable.

Fresh pre-2.6.1 staging and local rollback backups are retained. The older
CharacterCreator mod backups are removed after successful replacement. The
server backup command applies its existing two-daily/one-weekly retention.
Detailed receipts are local under `Character Creator/build/release-2.6.1/`.

## Publication and OVH completion

- Catalog publication commit: `268328dad461d932a2a62df6ec59cb0e1d69004f`.
- Both raw public catalogs match the exact 2.6.1 metadata. GitHub's archive
  digest matches the local package; a fresh public download through the
  installer passes size/hash checks, extraction, Java validation and all
  13,648 file hashes. GitHub's manifest validation workflow passed.
- Five older CharacterCreator backups were removed (one by the installer's
  retention helper, four explicitly). Fresh staging/local rollback copies
  remain; the local copy was separately verified against every 2.6.0 hash.
- OVH had zero players, a fresh heartbeat, an active service and a free backup
  lock before `sudo faded-pz-backup`. The verified archive is
  `project-zomboid-20260924T143858Z.tar.zst`, SHA-256
  `47a6e1c559baea315ebe69db3ed80676ef93b548d5b8f3a47defe82568bb8095`.
  Existing retention pruned the oldest daily backup, retaining two daily
  archives. The backup command completed successfully and restarted PZ.
- FJL ServerSync verified the published ZIP hash and installed 2.6.1. Every
  one of the 13,648 server files matches the release, with no extras or missing
  files. OVH's 80 enabled mod IDs and their order are unchanged.
- By 14:44 UTC, GAME_READY, WorldDictionary completion, SERVER STARTED,
  UDP 16261/16262, and a fresh online Nexus heartbeat were confirmed.
  Nexus pack version: `sync-20260924T144329Z-f8df50e8`.
- Local, staging and OVH now agree on the exact 2.6.1 payload. The client FJL
  profile's mod-list selection mode is preserved. No PingPlayers restart or
  unrelated server configuration change was made.

Packaging and startup checks do not establish in-game appearance, animation,
loot balance or multiplayer behavior; 2.6.0 limits remain. The manifest URLs
are unchanged; players use Refresh Mod List to obtain the update.
