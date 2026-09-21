# Echoes 0.10.1 deployment - September 21, 2026

Completed and verified at 2026-09-21T18:10:30.923467+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-0101). Catalog commit `ad36d23a6b8b92a0e95ed8312cc7fa3fdba6f3ad` updates Echoes in Main and Faded Realms. Both catalog workflows passed; other entries and enabled mod IDs are preserved.

## Release and installation

- ZIP: 55,904,777 bytes; SHA-256 `d48ad2953ab05e54c126b89e16807a2e1f721114345d544ca78958c5e849d150`.
- Native JAR: 482 classes; SHA-256 `3ad12c1f566019658ebb0a72de3131f37afe68244a8cc47519100af4ff648f5a`.
- All 941 local and OVH installed files match the public ZIP. Remote ownership is correct.
- Immutable stage: `E:/Faded Mod Staging/EchoesOfHumanity-0.10.1-release`; canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`.
- Local replacement used a verified backup and JAR-lock preflight. FJL 0.4.1 is READY with its existing schema-2 modList profile preserved.

The actual packaged Installer 0.3.3 passed public clean-install and existing-install tests, including signed loader installation, Build 42 bridge metadata, activation, backup and all payload hashes. The original game shell was unchanged. Windows standard/multilingual, Linux/Steam Deck and macOS update feed entries match the previously verified 0.3.3 release; this mod-only update required no installer application rebuild. A legacy profile-only badge can misreport a schema-2 plugin; the native verifier passed.

## Protected OVH deployment

A fresh zero-player heartbeat, active service, free backup lock and available disk space preceded the protected save/backup/restart. Verified archive `project-zomboid-20260921T180427Z.tar.zst`: 13,168,580,846 bytes; SHA-256 `7111f1687cd4d5881a6dd1c522cc751fa0177a07fdc4d98db739510e3ec08f1a`.

ServerSync updated only Echoes, to 0.10.1. FJL GAME_READY, completed WorldDictionary, SERVER STARTED, UDP 16261/16262, fresh online Nexus heartbeat and zero crash restarts passed. Nexus pack `sync-20260921T180829Z-8b075e95` advertises the exact release artifact hash. The enabled mod list and loader are preserved.

## Implemented behavior

- Native draw/update registration repairs after dedicated-client streaming and single-player restoration. Cached shells keep their identities and equipment; the recovery does not respawn NPCs.
- Unloaded client shells leave the native scene until safe re-entry. A bounded authority-owned pass can repair missing SP scheduling. Missing/inactive model registrations retry without rebuilding healthy models every tick.
- Recipient relationship state and body retention share a ten-second lifetime, avoiding a shorter visibility timeout after missed stationary heartbeats. Explicit Hide remains immediate and hostile sight restrictions remain intact.
- Health/ammunition follows the actual local body and requires a visible active model, eliminating orphan bars from stale network coordinates.
- Three host controls: ShowHealthBars, ShowIdentifyingInfo and OverheadHoverOnly. All default true, so names/faction labels and health/ammo appear only while hovering by default. Health/ammo and identity labels can be disabled separately, or always-visible display restored. Callouts and conversations continue.
- Camera zoom, split-screen, overlapping NPCs and menu input ownership are respected. The HUD remains zero-area and click-through. API 3 and existing campaign/AI behavior remain unchanged.

The confirmed code defects are consistent with the reported pattern of bars/names with missing bodies. No complete affected-user log or connected visual reproduction was supplied; this release repairs the verified lifecycle and timing gaps. Clients and server must both update and restart.

## Verification and documents

Final full release gate passed at `2026-09-21T18:00:52.5210458Z`: 52 Gradle tasks, 20 native scene/hover checks, 231 native sandbox checks, all existing Java/Lua regressions, transformed player-damage/XP checks, model/voice/package audits and all original descriptors across 33 overlays. Exact-runtime dedicated-server bootstrap passed at `build/smoke/20260921-140004-038`. These checks do not claim a connected-client visual playthrough or long-play balance acceptance.

Downloads contains the complete 0.10.1 guide (32 pages, 50 bookmarks, 129 validated internal links) and a Discord-ready post. The PDF SHA-256 is `bf05f014f5834bb3fe58231e6d9ba157d052632df2f49af68815acfa64c204d9`. Both documents are attached to the public release; prior versions are retained.

Native contracts and ownership are documented in `campaign/FFO_NATIVE_HANDOFF_RESULT.md`. Detailed receipts remain in installer `.test-work/echoes-0101/`; source gate `.test-work/visibility-0101/validation-final.log`. Existing unrelated modified/untracked work was preserved.
