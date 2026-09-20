# Echoes of Humanity 0.6.1

Owner-authorized update for invisible NPCs, stuttering movement and excessive firearm accuracy/damage. Main and Faded Realms retain their existing IDs and unrelated releases. NSA remains 0.7.0-alpha; FJL remains 0.4.0.

The complete offline release gate passed, including 60 ranged checks, ten movement/replication scenarios, relationship visibility and hostile HUD checks, and actual FJL-transformed native XP serialization. Final isolated dedicated smoke `20260920-174247-766` reached SERVER STARTED with native probes and no checked fatal signatures. Connected-player visual and combat-feel acceptance remains outstanding.

- Release: https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-20-echoes-061
- ZIP: `EchoesOfHumanity-v0.6.1.zip`, 52,678,204 bytes, 838 payload files.
- ZIP SHA-256: `56f88733fe7f75d7559be47d0105b64660d8333b5b3ed0a51a38112c155679a9`.
- Native JAR SHA-256: `e3640a4b3da1536c223b5923a214607f545ef3792c23d359cfb3e1720f4a53f8`, 383 classes.
- Stage: `E:\Faded Mod Staging\EchoesOfHumanity-0.6.1-release`; prior canonical stage backed up.
- Production installer prepared the staged ZIP and verified every payload hash.
- Player PDF: 32 pages, 29 bookmarks, 87 valid clickable links. PDF and Discord copy-paste text are release assets and saved in Downloads.

Public installation and protected OVH restart receipts follow after verification.


## Completed publication and deployment

- Public release: https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-20-echoes-061
- Main/Faded Realms catalog commit: `2548797`. All three GitHub checks passed; 119 Main and 79 Faded Realms IDs preserved.
- ZIP: 52,678,204 bytes, 838 files, SHA-256 `56f88733fe7f75d7559be47d0105b64660d8333b5b3ed0a51a38112c155679a9`. Public GitHub asset digest and production installer download match.
- Native JAR: 383 classes, SHA-256 `e3640a4b3da1536c223b5923a214607f545ef3792c23d359cfb3e1720f4a53f8`.
- Local playable installed with BACKUP_REPLACE; all 838 files match. Previous copy: `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260920_174511`.
- Protected OVH backup/restart ran after verifying a fresh zero-player heartbeat, free backup lock and disk space. The helper verified `project-zomboid-20260920T214529Z.tar.zst` (13,162,522,617 bytes); its checksum file exists and the helper exited successfully.
- Service active since **Sun 2026-09-20 21:49:33 UTC**. Full readiness verified **2026-09-20T21:51:47.620467+00:00**: GAME_READY, WorldDictionary completion, SERVER STARTED, UDP 16261/16262, fresh online heartbeat and zero crash restarts.
- All 838 OVH files match the public ZIP and belong to pzserver. All 80 enabled server IDs remain unchanged.
- NPC guide in Downloads: 32 pages, 29 bookmarks, 87 valid links; SHA-256 `86d3f5ac6dfce001a5e76f07054c5e0a52dd2dffe2914a1d2297350d2b667a54`. Matching Discord copy-paste text is also saved and published as an asset.

Existing unrelated mod-pack warnings are outside this patch. No connected-player rendering/FPS or live combat-feel acceptance test was performed. Full local receipts are retained in installer `.test-work/echoes-061`; source evidence is `docs/campaign/RELEASE_0.6.1_VERIFICATION.json`.
