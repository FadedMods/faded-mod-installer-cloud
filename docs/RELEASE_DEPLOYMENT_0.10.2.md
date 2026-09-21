# Echoes 0.10.2 deployment — September 21, 2026

Completed and verified at 2026-09-21T21:17:55.601060+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-0102). Catalog commit `a81500731d1e52c823deb8824a65eebcc3a14b09` updates only Echoes in Main (121 IDs) and Faded Realms (79 IDs).

## Package and installation

- ZIP: 55,923,875 bytes; SHA-256 `89bcc2eabcc68fce6f871489424bb226ff37a73454c477b98aaa15975bcce957`.
- Native JAR: 492 runtime classes; SHA-256 `47b7917196bb56fe8e3127adc12c5d63093046409b86357a5b393b076859afce`.
- All 941 public/local/OVH payload files match byte-for-byte; remote ownership is correct.
- Immutable release stage: `E:/Faded Mod Staging/EchoesOfHumanity-0.10.2-release`; canonical payload-only stage: `E:/Faded Mod Staging/EchoesOfHumanity`.
- Local update used a JAR-lock preflight and recoverable backup: `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260921_171015`. Existing FJL 0.4.1 schema-2 modList profile is preserved and its native verifier reports READY.

The actual packaged Installer 0.3.3 passed public clean-install and existing-install tests, signed loader installation, Build 42 bridge activation and every payload hash. Existing Windows standard/multilingual, Linux/Steam Deck and macOS updater entries match the verified 0.3.3 release. This mod-only update does not require rebuilding the installer application. The legacy profile-only diagnostic can still mislabel schema-2 modList activation; the native verification passed.

## OVH

A fresh zero-player heartbeat, active service, free backup lock and available disk space preceded `sudo faded-pz-backup`. Verified backup `project-zomboid-20260921T211105Z.tar.zst`: 13,170,866,871 bytes; SHA-256 `edbca958f8e4477aa6b1a57f2136ebf5968a5040e8ce23a327418782bfeb246d`. The protected command saved/stopped/backed up/restarted the game service; the VPS was not rebooted.

FJL ServerSync installed Echoes 0.10.2. GAME_READY, completed WorldDictionary, SERVER STARTED, UDP 16261/16262, zero crash restarts, unchanged enabled mod IDs and a fresh online Nexus heartbeat were verified. The Nexus pack advertises the exact public ZIP hash.

## Behavior and verification

Player damage retains native skill/armor effects while avoiding the generic weapon reduction that made human targets too durable. Delayed/reordered native attack and finite-ammo receipts are retained in bounded histories; player reports cannot author damage. Mixed wounds subtract new body damage instead of hiding it behind weapon health. Client proxies cannot author health, and revision/death ordering prevents old snapshots recreating dead bodies.

Managed deaths prepare loot before the native corpse constructor takes inventory ownership. Explicit native corpse packets synchronize appearance, inventory and persistent identity. Failed finalization retains the actor for retry; private-uniform and existing issued-weapon drop policies are preserved. Ordinary loot remains unfavorited.

New sandbox defaults: player-to-NPC damage 1.0; NPC-to-NPC and zombie-to-NPC damage .25 each; mercy threshold 80%. All use one shared health pool. Advanced confirmed infection produces nearby squadmate diagnosis, plea/reply, an eight-second farewell, visible melee action and remembrance. A completed mercy kill prevents reanimation. New dialogue is halo text without newly recorded voice clips. Accessories with no body regions skip random dirt placement.

Full release gate completed at `2026-09-21T21:07:44.8224782Z`: 52 Gradle tasks, native transformed health/death and finite-ammo checks, actual corpse construction/save/load/packet serialization, 93 clinical/infection checks, 263 native sandbox checks, existing Java/Lua/model/voice/package regressions and API compatibility across 33 overlays. Exact-runtime dedicated bootstrap passed at `build/smoke/20260921-170633-907`. No connected multiplayer combat/visual playthrough or long-play balance acceptance is claimed. Both server and clients must update/restart; no save reset is needed.

## Documentation

Downloads contains the complete 0.10.2 PDF guide (34 pages, 56 bookmarks, 143 validated internal links) and Discord-ready post. Both are public release assets. PDF SHA-256 `c8b555e3d09600cfc29657a858410e0f402025a9485208dff74fd5e434e569ea`. Native interface contracts are in `campaign/FFO_NATIVE_HANDOFF_RESULT.md`.

Detailed receipts remain in installer `.test-work/echoes-0102/`; source validation log `.test-work/damage-0102/validation.log`. All unrelated modified/untracked work was preserved.
