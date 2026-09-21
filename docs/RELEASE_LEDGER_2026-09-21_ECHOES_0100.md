# Echoes 0.10.0 deployment - September 21, 2026

Completed and verified at 2026-09-21T17:38:57.700010+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-0100). Catalog commit `2d04d0253f77d4152213f6f8ff6f9f4f7dcea4d6` updates Echoes in Main and Faded Realms. Both catalog workflows passed; other entries and enabled mod IDs are preserved.

## Release and installation

- ZIP: 55,899,007 bytes; SHA-256 `9f51664e2a76692711282be6cfd76b9ccfcc44def316aea4d24bc8f8ace7ba52`.
- Native JAR: 481 classes; SHA-256 `793b99623e287be8c5d60989c7412ab43f3f4703b6624ed1432b47ea9e338e7b`.
- All 941 local and OVH installed files match the public ZIP. Remote ownership is correct.
- Immutable stage: `E:/Faded Mod Staging/EchoesOfHumanity-0.10.0-release`; canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`.
- Local replacement used a verified backup and JAR-lock preflight. FJL 0.4.1 is READY with its existing schema-2 modList profile preserved.

The actual packaged Installer 0.3.3 passed public clean-install and existing-install tests, including signed loader installation, Build 42 bridge metadata, activation, backup and all payload hashes. The original game shell was unchanged. Windows standard/multilingual, Linux/Steam Deck and macOS update feed entries match the previously verified 0.3.3 release; this mod-only update required no installer application rebuild. A legacy profile-only badge can misreport a schema-2 plugin; the native verifier passed.

## Protected OVH deployment

A fresh zero-player heartbeat, active service, free backup lock and available disk space preceded the protected save/backup/restart. Verified archive `project-zomboid-20260921T173131Z.tar.zst`: 13,167,987,474 bytes; SHA-256 `1572fe5115ec87dd9a4620297f02adb7014a03880bc5819b84bc54d83e4046e8`.

ServerSync updated only Echoes, to 0.10.0. FJL GAME_READY, completed WorldDictionary, SERVER STARTED, UDP 16261/16262, fresh online Nexus heartbeat and zero crash restarts passed. Nexus pack `sync-20260921T173534Z-b65df498` advertises the exact release artifact hash. The enabled mod list and loader are preserved.

## Implemented behavior

- Native loud-sound investigation: nearest available units send one scout each, cover the approach, observe real contacts and share a completed radio report or return physically. Radio battery, deadlines, injury/death cancellation, own-unit noise exclusion and squad reinforcement limits apply. A gunshot alone never assigns blame to a player.
- Angela receives a persistent first-encounter journey and a Linux asset-path correction. Existing identity, mortality and campaign ownership remain; unsafe admission or travel waits rather than fabricating an encounter.
- Four finite Rosewood civilian residents work and scavenge, gradually consume actual materials to board windows, preserve exits and defend themselves after confirmed aggression. Claimed sites fall back from firehouse to police station to church. Dead or issued-but-unavailable residents are never replaced.
- Household assaults affect Unaligned standing and ordinary Knox assistance. Household backup uses the existing interruptible one-caller radio/flare lifecycle; lone survivors defend themselves. Campaign conversations remain available.
- Five host controls; campaign API 3 preserved. The 254 bundled voice clips are retained; new callouts have text fallback.

Project A-Life's expiring evidence, single radioman, defensive civilian policy and incremental fortification informed native implementations. Twelve source subsystems were reviewed and fingerprinted in `ALIFE_RESEARCH_0.10.0.md/json`. No second NPC runtime was imported. Entrance reservations, complete room-search behavior and new radio recordings remain outside this release.

## Verification and documents

Final full release gate passed at `2026-09-21T17:26:27.9776552Z`: 51 Gradle tasks, 49 living-response checks, 213 native sandbox checks, all existing Java/Lua regressions, transformed player-damage/XP checks, model/voice/package audits and all original descriptors across 33 overlays. Exact-runtime dedicated-server bootstrap passed at `build/smoke/20260921-132547-384`. These checks do not claim a connected-client visual playthrough or long-play balance acceptance.

Downloads contains the complete 0.10.0 guide (32 pages, 47 bookmarks, 123 validated internal links) and a Discord-ready post. The PDF SHA-256 is `96c37f08c28219386ee0220b390d56a94f8127cafd4b1f120bb4b9d3d1a160cb`. Both documents are attached to the public release; prior versions are retained.

Native contracts and ownership are documented in `campaign/FFO_NATIVE_HANDOFF_RESULT.md`. Detailed receipts remain in installer `.test-work/echoes-0100/`; source gate `.test-work/echoes-0100/validation-release.log`. Existing unrelated modified/untracked work was preserved.
