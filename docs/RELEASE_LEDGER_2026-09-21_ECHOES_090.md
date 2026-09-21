# Echoes 0.9.0 deployment â€” September 21, 2026

Completed and verified at 2026-09-21T13:56:24.576130+00:00. [Immutable release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-090); catalog commit `72d53726560626448e3eec556b7af4dd871e3d71` updates Echoes in Main and Faded Realms. Their existing mod IDs and other catalog entries remain unchanged; the OVH enabled list is preserved. Both catalog publication workflows passed.

## Published and installed

- ZIP: 55,863,221 bytes; SHA-256 `4495521a42c3655f16e06cf1821fa6646e9da87e90b2c5f1b54a6f1e8d6cd350`.
- Native JAR: 1,651,269 bytes / 473 classes; SHA-256 `f5dbf97caad96508d179707e93ff385b551bb9b658d25528fb263c844739444b`.
- All 941 installed files match the public ZIP locally and on OVH. Remote files are owned by pzserver.
- Immutable stage: `E:/Faded Mod Staging/EchoesOfHumanity-0.9.0-release`; canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`.
- Local rollback backup: `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260921_094908`. JAR-lock preflight passed before replacement.
- Local FJL verification: READY; existing schema-2 modList profile preserved. FJL remains 0.4.1.

The actual packaged Installer 0.3.3 passed public clean-install and existing-install tests, including signed loader, Build 42 bridge, plugin activation, backup and payload hashes. The original game shell was unchanged. The Windows standard/multilingual, Linux/Steam Deck and macOS update entries match the previously verified 0.3.3 artifacts. This mod-only release required no installer application rebuild. Its legacy profile-only badge can still misreport a schema-2 plugin; native verification passed.

## Protected OVH backup and restart

A fresh zero-player heartbeat, active service, free backup lock and available disk space preceded `sudo faded-pz-backup`. Verified archive: `/srv/backups/project-zomboid/daily/project-zomboid-20260921T135006Z.tar.zst`; 13,169,212,923 bytes; SHA-256 `6e9c6e94bee5585499b764f2c3a34a98fb2c39ecdcc251bcfa9afcf920a856e2`.

ServerSync installed Echoes 0.9.0 before discovery. FJL GAME_READY, WorldDictionary completion, SERVER STARTED, UDP 16261/16262, fresh online Nexus heartbeat and zero crash restarts passed. Nexus pack `sync-20260921T135411Z-f5941e69` advertises 0.9.0 and its exact artifact hash. No enabled mod was added or removed, and the loader was not replaced.

## Implemented behavior and verification

- Physical idle recovery, including ordinary followers and squads sharing a room with a working medic; real bounded door/exit/patrol routes and protected meaningful work.
- Local faction standoff warning/escalation, friendly/allied and horde-truce protection, and single-visible-human squad maneuvers. No global diplomacy rewrite or unseen firing target.
- One persistent four-person ambush including the disguised bait, real friendly-faction clothes and native conversation reveal; no additional backup waves or casualty refills.
- One additional squad requested per completed paid report, safe deferred admission, native whole-party vehicle attempts and walking fallback. Existing cars/keys are required. Loaded travel expires after 180 seconds on foot or 360 seconds total; saved elapsed time excludes unloaded intervals. Expiry releases ordinary AI and cannot create replacement waves.
- Seven additional native sandbox controls; prior actual health damage, finite ammunition, UI fixes, loot provenance, companions, clinical integration and 254 bundled voice clips retained. New encounter captions may be text-only.

The final full release gate passed at 2026-09-21T13:46:29.3752699Z. Focused checks include idle progression 75; territorial pressure 27; event admission 18; ambush 53; additional backup/transit 96; assault tactics 40; native sandbox 179. Existing Java/Lua regressions, transformed player health/death and ammunition transactions, provenance, presentation, asset/voice/package audits and original ABI in 31 overlays passed. Exact-runtime isolated startup passed at `build/smoke/20260921-094553-088`.

The deterministic movement/encounter fixtures and headless bootstrap do not establish connected multiplayer rendering, live driving or long-play balance. No such acceptance session is claimed. API 3, persistent identities and campaign ownership remain unchanged. Contracts: `LOCAL_ENCOUNTER_CONTRACT.md`, `IDLE_PROGRESSION_CONTRACT.md`, `AMBUSH_CONTRACT.md`, `RETALIATION_BACKUP_CONTRACT.md` and `campaign/FFO_NATIVE_HANDOFF_RESULT.md`.

## Player documents and evidence

Downloads contains `Echoes of Humanity - Complete Player Guide v0.9.0.pdf`: 49 pages, 42 bookmarks and 130 validated internal links; SHA-256 `b34ca1e59d21c952567b76a33f6061d98ee9ed5011a9407b79b9a60ab33e923c`. The Discord post is 1,775 characters. Prior 0.8 artifacts are preserved.

Detailed receipts: installer `.test-work/echoes-090/`; final source gate: EOH `.test-work/activity-090/full-release-gate.log`. Existing unrelated modified/untracked work was preserved.
