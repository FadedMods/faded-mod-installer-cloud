# Echoes 0.8.0 deployment — September 21, 2026

Completed and verified at 2026-09-21T10:54:19.863931+00:00. [Immutable release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-080); catalog commit `1806b12866f3b767ea87c311d87137aa6298bffa` updates only Echoes in Main and Faded Realms. Their 121/79 IDs remain unchanged; the OVH enabled list is preserved. Both catalog-validation and CodeQL workflows passed.

## Published and installed

- ZIP: 55,793,789 bytes; SHA-256 `d24be170a45987d2bb7bc9d7ce9565d699b407c78a0e82131e1b1f11aed18902`.
- Native JAR: 1,579,547 bytes / 454 classes; SHA-256 `e136b7069bdfb2292066729b1cf2407ebc855583e75c0a6aca9bfdbffa1be306`.
- All 941 installed files match the public ZIP on local and OVH installations. Remote files are owned by pzserver.
- Stage: `E:/Faded Mod Staging/EchoesOfHumanity-0.8.0-release`; canonical stage `E:/Faded Mod Staging/EchoesOfHumanity`.
- Local rollback backup: `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260921_064803`.
- Local native FJL verification: READY; schema-2 modList selection preserved without profile edits. FJL remains 0.4.1.

Installer 0.3.3 passed actual packaged clean-install and existing-install tests using the public catalogs, signed loader, Build 42 bridge, plugin activation, backup and all payload hashes. Its original game shell remained unchanged. Windows standard/multilingual, Linux/Steam Deck and macOS update entries still match the previously verified 0.3.3 artifacts; no installer application change or rebuild was required.

The first local replacement encountered the running game's locked 0.7.0 JAR. The complete prior 840-file payload was immediately restored and checked against its immutable ZIP. After the user saved and exited, installation completed with all 941 new files verified. A JAR-lock preflight now protects this release helper. The installer's existing legacy profile-only checker can still display a false disabled-plugin message for schema-2 modList profiles; native FJL reports READY.

## Protected OVH backup and restart

A fresh zero-player heartbeat, active service, free backup lock and adequate disk space preceded `sudo faded-pz-backup`. Verified archive: `/srv/backups/project-zomboid/daily/project-zomboid-20260921T104825Z.tar.zst`; 13,164,145,120 bytes; SHA-256 `9ed30f18249838a5d356bfdb4cbaf0573022e9d6fea538e2639e6d7be34213d5`.

ServerSync installed Echoes 0.8.0 before discovery. Verified FJL GAME_READY, WorldDictionary completion, SERVER STARTED, UDP 16261/16262, fresh online Nexus heartbeat and zero crash restarts. Nexus pack `sync-20260921T105229Z-4e4a329c` advertises 0.8.0 and the exact release hash. No enabled mod was added or removed, and the loader was not replaced.

## What changed and evidence

- Actual server health damage for multiplayer player collisions, stock finite ammunition transactions, bounded repeated-hit admission and preserved melee handling.
- Immediate assault self-defense; lone survivors fight immediately. One coordinated squad caller uses an interruptible native radio/flare action. Only original members still in the same squad respond; a completed report retains faction consequences.
- Tactical movement against one confirmed attacker, caller action protection and native terrain-aware firing/retreat position selection.
- Independent equipment protection replaces NPC favorite flags. Named gift/trade/recovery/verified-kill tooltips and bounded durable reputation effects; real spare companion gifts.
- 96 new English voice clips: 127 lines / 254 OGGs in total. No API is required for bundled playback.

Full release validation and exact-runtime isolated server bootstrap passed. Focused checks: transformed health/death/transport 25; transformed stock/NPC ammunition 27; retaliation 63; provenance 38 plus 15 Lua tooltip checks; actual tactical controller/combat navigation requests 31; cover scoring 5; native presentation 104; native sandbox 129. Original public/protected ABI remains intact in 31 overlays. Asset, voice, package and existing Java/Lua regressions passed.

The tactical navigation fixture uses a fake-world adapter, while the server bootstrap verifies native loading/registries. No connected multiplayer combat, rendered cover/animation or extended-play acceptance session is claimed. Campaign API 3 and explicit immortal/custody guards remain unchanged. Contracts: `campaign/PLAYER_DAMAGE_TRANSPORT.md`, `RETALIATION_BACKUP_CONTRACT.md`, `campaign/ITEM_PROVENANCE_API.md` and `campaign/FFO_NATIVE_HANDOFF_RESULT.md`.

## Player documents

Downloads contains `Echoes of Humanity - Complete Player Guide v0.8.0.pdf`: 45 pages, 38 bookmarks, 118 valid internal links; SHA-256 `6facfdd617745566dad2bbe1684bfc5f2602c817dfe1c8335fad0af74f0257ab`. The matching Discord post is 1,875 characters. Full release notes and editable guide remain in this repository.

Detailed local receipts: installer `.test-work/echoes-080/`; exact native smoke: EOH `build/smoke/20260921-064153-751/`. Existing unrelated source modifications and untracked work were preserved.
