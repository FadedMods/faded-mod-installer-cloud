# Echoes 0.12.1 hotfix deployment

Completed at 2026-09-22T03:10:17.338633+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-0121). Catalog commit `617bf5070762af6d9d4a1f9212d2790b0460d50f` updates Echoes only in Main (121 IDs) and Faded Realms (79 IDs).

## Cause and repair

The supplied server-console (6).zip contains 6,949 instances of `Squad faction mismatch: rosewood.residents`. The old civilian squad metadata conflicted with resident definitions now belonging to the Rosewood micro-faction, preventing world initialization from completing on every tick.

The hotfix migrates only the known legacy squad's faction before native persistence reads it. It restores recruited civilian community ownership before agent registration, and creates native community squads before adoption or restored membership joins. Dead residents stay in the historical ledger without joining the newly adopted active squad. Campaign API 3 and community extension 1 remain unchanged.

Regression tests reproduce the exact exception using real serialized legacy records and execute the actual manager initializer. Upgrade, repeat load, adoption/reload, migrant ledger and per-person receipt recovery pass; identity, names, casualties, health, ammunition, memories, squad objective/destination/timestamp/morale remain intact. Future schemas and unrelated civilian squads are untouched. All 66 migration checks and the existing 2,310 community/road checks passed, followed by the complete offline/native release gate and exact-runtime dedicated bootstrap.

## Published package and installs

- ZIP bytes: 90,096,048; SHA-256 `0fed283e2b5ce22c644599e93c9bc5f16b2e9d14d1606e35bd4c2f9f8c4aacf6`.
- Native runtime: 530 classes; SHA-256 `b5c5692eeee51152cdd0da8a54058145d34cc8ba5dee45b2b53a8d24d926154f`.
- All 990 public, local and OVH files match byte-for-byte. Remote files belong to the server owner.
- Canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`; immutable release: `E:/Faded Mod Staging/EchoesOfHumanity-0.12.1-release`.
- Local replacement passed the JAR-lock check and preserved backup `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260921_230246`. Existing FJL profile preserved; native verifier READY.
- Packaged standard Installer 0.3.3 passed fresh public clean and existing installs, bridge activation and all payload hashes. Published platform updater entries remain verified at 0.3.3; this mod hotfix does not rebuild installer binaries.

## OVH

Fresh zero-player/heartbeat, active service, free lock and disk checks preceded the protected save/stop/backup/restart. Backup `project-zomboid-20260922T030353Z.tar.zst`: 13,202,323,235 bytes, SHA-256 `561ece2f56c81dc132bce99987c81c33f247c3ae64af3a4a477244e4c5da82f3`.

ServerSync installed 0.12.1. GAME_READY, completed WorldDictionary, SERVER STARTED, UDP 16261/16262, zero crash restarts, unchanged enabled mod IDs and fresh online Nexus heartbeat passed. Nexus advertises the public package hash. No save or NPC-data deletion was performed.

## Documentation and limits

The updated complete PDF is in Downloads: 38 pages, 66 bookmarks, 167 checked internal links; SHA-256 `68124972c02e41dacad68ef49042d6db453487c315893c8c8fc61fa9f7f259ed`. The Discord hotfix post and PDF are public release assets. Native contract handoff is updated.

Validation completed at `2026-09-22T02:59:31.7050136Z`; evidence in `build/log-review-0121/` and installer `.test-work/echoes-0121/`. A connected reproduction on the reporting user's world is not claimed. Their separate missing animation-folder messages across installed mods and native missing-square ReceiveModData errors are not established as Echoes failures or claimed fixed here. Update both clients and server and fully restart; no world reset is needed.
