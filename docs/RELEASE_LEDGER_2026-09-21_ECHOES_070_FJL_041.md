# Echoes 0.7.0 / FJL 0.4.1 deployment — September 21, 2026

Completed and verified at 2026-09-21T08:30:15.709499+00:00. Catalog commit `d1fb883` updates only Echoes,
the existing FJL bridge, and the signed v2/v3 loader channels. Main retains all
121 IDs; Faded Realms retains its existing 79. The OVH enabled list is unchanged.

## Published artifacts and installation

- [Echoes 0.7.0 release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-070)
- [FJL 0.4.1 release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-faded-java-loader-0.4.1)
- Echoes ZIP: 52,789,835 bytes; SHA-256 `ca52ab9e1799637576dc83445c602eea4c331fd747e959fe3ed4328a2eb65fb0`.
- Echoes native JAR: 1,508,191 bytes, 427 classes; SHA-256 `e3cfba0a6200e493bda01da4caf1a71ee27cf71314bcf81bf470412c34a70a3d`.
- 840 installed files match the public ZIP on both local and OVH installations.
- FJL agent SHA-256 `f6cb71211f13f9328e6d86e703f69b4e2318e6ff0074fa9c152f3178f8e1df2c` verified on both targets; bridge 0.4.1 deployed.
- Canonical staging: `E:/Faded Mod Staging/EchoesOfHumanity`; versioned release folder `EchoesOfHumanity-0.7.0-release`.
- Local Echoes backup: `local backup recorded in the private deployment receipt`. Local bridge backup: `local bridge backup recorded in the private deployment receipt`.

Installer 0.3.3 passed actual packaged clean and existing installation paths
against the public assets, with a signed FJL 0.4.1 loader, valid Build 42 bridge,
enabled plugin, verified payload and rollback backup. The fixture did not change
the original game shell. Windows standard/multilingual, Linux, Steam Deck and
macOS updater entries still match the verified 0.3.3 release; no installer source
change or app rebuild was needed. FJL has all eight platform/SDK/bridge ZIPs and
17 published assets verified by hash and signed-catalog checks.

The actual local native schema-2 `modList` profile was preserved and its owning
mod/explicit disables checked. The old installer profile-only repair badge can
still falsely say a plugin is not enabled because it reads legacy
`enabledPlugins`; native FJL verification reports READY. This is a remaining
cosmetic checker issue, not a missing bridge or a reason to rewrite the profile.

## OVH protected restart

Fresh zero-player heartbeat and service/lock/disk checks preceded the normal
`sudo faded-pz-backup`. Verified archive: `/srv/backups/project-zomboid/daily/project-zomboid-20260921T082404Z.tar.zst`. The old 0.3.4 loader was
separately backed up under the game loader directory, then replaced atomically
with the verified 0.4.1 JAR by a temporary stopped-service pre-start hook. The
hook was removed afterward; launch arguments and enabled mod IDs were preserved.
Native profile migration retains explicit disables and its own legacy backup.

Verified GAME_READY, completed WorldDictionary, SERVER STARTED, UDP 16261/16262,
fresh online Nexus heartbeat, updated pack and zero crash restarts. Every Echoes
file matches the immutable public ZIP and is owned by pzserver. Detailed receipts
are in the installer's `.test-work/echoes-070/`.

## Validation and limits

Final full release gate passed after the final mission-scavenging guard change.
It includes Java and Lua regressions, transformed survivor XP/hit checks,
31 baseline ABI overlays, assets/licenses/voice audits and exact-runtime isolated
Build 42.20.4 server startup. New focused checks include 73 presentation,
25 confinement, 30 daily-life, 28 conflict, 34 equipment and 123 native sandbox
assertions, plus 10,000 stable suppressor selection samples.

The supplied client hit-reaction error and server PZArrayList iterator error
are repaired. FJL validates both supplied CSI copies against the actual game,
preserves explicit Staircast advice bindings and isolates compatibility-plugin
namespace collisions; 148 FJL Java tests passed. Unsupported `javaPreload` and
`Exposer.exposeMethod(String,String)` remain refused and are not claimed fixed.

Gameplay changes and contracts are in `RELEASE_NOTES_0.7.0.md`,
`DAILY_LIFE_SETTLEMENT_CONTRACT.md`, `FACTION_CONFLICT_CONTRACT.md`,
`campaign/EQUIPMENT_WEAR_API.md` and `campaign/FFO_NATIVE_HANDOFF_RESULT.md`.
Campaign API 3 and the loader minimum 0.2.0 are preserved.

No connected-player visual, pathfinding, faction fight, long-run equipment or
48-hour campaign acceptance is claimed. Early secured houses need suitable
loaded/safe buildings, workers and real materials; conflict attempts still need
valid hostile squads and capacity. New social lines are captions; the existing
158 OGG clips remain unchanged. Chasm is assessed in `CHASM_EVALUATION.md`, not
integrated or bundled. Corrupt actor snapshots retain the pre-existing explicit
canonical recovery fallback; normal snapshots preserve exact item condition.

## Player documents

Downloads contains `Echoes of Humanity - Complete Player Guide v0.7.0.pdf`
(40 pages, 35 bookmarks, 107 valid internal links) and
`Echoes of Humanity - Discord Release v0.7.0.txt` (1,734 characters).
Source-mod concepts are implemented through native identity, work, resource,
navigation and companion services; donor population runtimes are not stacked
onto Echoes. NSA retains ownership of shared-rest intimacy.
