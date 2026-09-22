# Echoes 0.12.0 deployment - September 21, 2026

Completed and verified at 2026-09-22T01:45:38.725655+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-0120). Catalog commit `4155118b9e9f52da13068f554d23fd99d3887c90` updates only Echoes in Main (121 IDs) and Faded Realms (79 IDs). Both publication workflows passed.

## Package and installations

- ZIP: 90,093,377 bytes; SHA-256 `368245fe67a21ed722766673e2552d3e7202945b95738fdcf6401bf29b279852`.
- Native JAR: 529 runtime classes; SHA-256 `4f74814fc8b84f4ab880852740e029a9bb5d0e62ed6059b3ee0acd0eee0b3940`.
- All 990 public/local/OVH payload files match byte-for-byte; remote ownership is correct.
- Immutable release stage: `E:/Faded Mod Staging/EchoesOfHumanity-0.12.0-release`; canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`.
- Local update passed an exclusive JAR-lock preflight and kept a recoverable backup: `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260921_213831`.
- Existing FJL 0.4.1 schema-2 modList profile is preserved; native verification reports READY. A running game process must be restarted to load the new Java code.

Packaged Installer 0.3.3 passed public clean-install and existing-install tests, signed loader installation, Build 42 bridge activation and every payload hash. Existing Windows standard/multilingual, Linux/Steam Deck and macOS updater entries match the verified 0.3.3 release. This mod-only update did not rebuild installer binaries. The legacy profile-only diagnostic can mislabel schema-2 activation; the native verifier passed.

## OVH

A fresh zero-player heartbeat, active service, free backup lock and available disk space preceded `sudo faded-pz-backup`. Verified backup `project-zomboid-20260922T013940Z.tar.zst`: 13,168,000,345 bytes; SHA-256 `b0e5d4d210c0c00e672a5224a4e58e73c2f14316c6d2acaf66e547532c897ea8`. The protected command saved/stopped/backed up/restarted the game service.

FJL ServerSync installed Echoes 0.12.0. GAME_READY, completed WorldDictionary, SERVER STARTED, UDP 16261/16262, zero crash restarts, unchanged enabled mod IDs and a fresh online Nexus heartbeat were verified. The Nexus pack advertises the exact public ZIP hash.

## Included behavior

This release includes the previously undeployed 0.11.0 expansion: 150 available micro-faction definitions, bounded active communities, finite vanilla supplies, migrant recruitment, shared homes, major-faction allies, contextual interaction, native road planning and finite authority-owned vehicles. Road compilation and queries use bounded CPU workers; live physics and inventories stay on the authority thread.

Ordinary corpse defaults limit drops to one firearm at 25%, one armor piece at 35%, twelve rounds including loaded ammunition, six supplies and one bag. Surviving armaments have at most half condition. NPC-versus-NPC and hunter deaths keep persistent visible bodies with no inventory loot. Genuine trades and gifts are exempt from resupply warrants.

Persistent source-faction warrants respond to verified kills, recovered armaments and continued equipment use. An excessive score hires three independent contract hunters with a world announcement, aircraft/chopper sound and a parachute insertion. Their native bodies appear at validated touchdown locations; the airborne presentation is a bounded rendered sequence, not helicopter vehicle physics. Hunters have private tactical armor and suppressed AWP/SCAR/M4 variants, expert aiming, finite ammunition and double effective health. Their equipment is neither distributed nor transferable; their corpses are empty. Three successful attempts clear that employer's recorded resupply penalties. Disconnection, missing/unloaded actors and restart gaps do not earn survival time. Ten new sandbox options control pressure and ordinary drops.

The four authorized donors provide parachute/aircraft presentation, harness, armor and weapon assets under private Echoes IDs. Their scripts and dependencies are not imported. Source folders remain unchanged; donor hashes are in HUNTER_ASSET_PROVENANCE.json.

## Validation and limits

Full release gate passed at `2026-09-22T01:28:58.1997734Z`. Native damage, actual corpse inventory/save-load, warrant persistence and deduplication, global population limits, all 57 sandbox options, private asset closure, Lua insertion cleanup, Java/Lua/voice regressions and ABI preservation across 36 overlays passed. The exact runtime passed a dedicated 42.20.4/FJL 0.4.1 bootstrap at `build/smoke/20260921-212731-354`.

No connected multiplayer visual or tactical playthrough, long-term hunter balance test, physical road-driving acceptance or FPS measurement is claimed. Both server and clients must update and restart; no save reset is needed.

## Documentation

Downloads contains the complete 0.12.0 PDF guide (38 pages, 65 bookmarks, 165 validated internal links) and Discord-ready post. Both public release assets were downloaded and matched. PDF SHA-256 `df2785e6698170bc31b95761d6e45fb4d5daee71afc4af8148b8ce5b19101ead`.

Contracts: HUNTER_NATIVE_CONTRACT.md, MICROFACTION_NATIVE_CONTRACT.md, campaign/FFO_NATIVE_HANDOFF_RESULT.md. Campaign API remains 3; community extension remains 1. Detailed deployment receipts: installer `.test-work/echoes-0120/`; native validation: `build/hunters/release-validation.log`. Unrelated modified/untracked work was preserved.
