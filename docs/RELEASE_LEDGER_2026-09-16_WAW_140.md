# What A World 1.4.0 and Solar Shadows 1.0.0 release ledger

- Published: 2026-09-16
- Release: `mod-assets-2026-09-16-what-a-world-1.4.0`
- Main manifest: `WhatAWorld` (version update); `WhatAWorldSolarShadows` (new entry, appended)
- Faded Realms manifest: `WhatAWorld` only (already in the live `Mods=` pack).
  `WhatAWorldSolarShadows` is **not** on the server and is deliberately Main-only.

## Content change

What A World 1.4.0:

- Imports eleven donor systems into the per-player budget table: ground cover
  (Grass Lands + its B42 band patch), road erosion thinning, visible door
  damage, torchlight through floor openings, animals that eat corpses, worn-load
  movement sounds, photometric flashlights, body bags, working popcorn machines
  and a hospital gurney.
- Fixes the three 1.3.3 errors seen in both the OVH server log and a client log:
  unbound `WAW` in `WAW_SeasonData.lua` and `WAW_WeatherLoot.lua` (the weather
  receiver and magazine never reached loot tables in 1.3.3), and the missing
  `AnimSets`/`actiongroups` scan directories.
- Donor defects fixed on the way in, including Visible Door Damage's per-tick
  refresh (90 ms+ frames, reported), the gurney's undeletable half in
  multiplayer (reported), and Animals Eat Corpses shipping at 20x debug speed.

What A World - Solar Shadows 1.0.0 (new, optional companion, derived from ShadowZ):

- Replaces `screen.frag`, so it is a separate opt-in mod, like Tree Visibility.
- Runs on **Faded's Java Loader**. ShadowZ's ZombieBuddy patches were rebuilt as
  14 FJL Mixins; the donor lighting engine ships as its original bytecode. No
  ZombieBuddy declaration or class anywhere.
- Single-player is the tested target.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `WhatAWorld-v1.4.0.zip` | 161,505,772 | `6e501c74fc4190c33ff0be22a7657aeee7639aaf0329d1794969f19b0945d919` |
| `WhatAWorldSolarShadows-v1.0.0.zip` | 1,222,305 | `a5bc40cde5a024fe8a8590bd6e462dee571b0a42a428130190764c3847844ac5` |

Both single-part, under the 1800 MB split limit. GitHub asset size and digest
match the local SHA-256 for both.

## Package validation

- Staged source: `E:\Faded Mod Staging\WhatAWorld` and `E:\Faded Mod Staging\WhatAWorldSolarShadows`
- Previous WAW staging preserved at `E:\Faded Mod Staging\WhatAWorld-1.3.3-superseded`
- Packaged with `scripts/package_local_mods.py`; each archive reconstructs as a
  single top-level folder with exactly one `42/mod.info`, no root duplicate and
  no double nesting; forward-slash entry names; CRC test passed
- `prepare_mod_zip` passed for both; byte parity against staging 1116/1116 and
  22/22 files, zero mismatches
- `modversion=1.4.0` and `modversion=1.0.0` verified
- WAW repo gates passed: consent contract, 1,383 behaviour checks, smoke run,
  engine API, name collisions, `build-java.ps1` (both plugins), package check

## Java metadata

`WhatAWorld` keeps **no** Java fields. Its bundled `faded.whataworld.textures`
plugin is optional by that mod's own contract, which forbids making FJL a
required dependency.

`WhatAWorldSolarShadows` declares its plugin, because FJL's profile uses an
`enabledPlugins` allowlist and an undeclared plugin installs and is silently
skipped:

| Field | Value |
| --- | --- |
| `requiresJavaLoader` | `true` |
| `minimumJavaLoaderVersion` | `0.3.4` (JAR declares 0.3.0; verified against 0.3.4) |
| `javaEnvironment` | `CLIENT` |
| `javaPluginId` | `faded.whataworld.solarshadows` |
| `javaPluginVersion` | `1.0.0` |
| `javaPluginMode` | `HYBRID` |

`validate_java_plugin` passed against the prepared archive. Offline FJL proof:
the installed FJL agent 0.3.4 was run against the real 42.20.4
`projectzomboid.jar` with both WAW plugins installed and all 27 Solar Shadows
injections applied with no warnings; with the mod installed but not enabled,
FJL refused the plugin and 0/27 applied.

## Catalog shape

Main: 118 -> 119 (1 changed, 1 appended, 117 untouched, order and top-level
blocks preserved). Faded Realms: 79 -> 79 (1 changed, 78 untouched). Both files
round-trip byte-exactly through `json.dumps(indent=2, ensure_ascii=False)`.
`scripts/validate_manifests.py` passed.

## Local deployment

Exact public payloads installed with the installer's `install_prepared_mod`
(`BACKUP_REPLACE`) to `E:\PZ User Data\Zomboid\mods`:

- `WhatAWorld` 1.4.0: 1116/1116 files byte-identical to the public ZIP.
  Previous 1.3.3 backup: `%APPDATA%\FadedLocalModInstaller\backups\WhatAWorld_20260916_195903`.
- `WhatAWorldSolarShadows` 1.0.0: 22/22 files byte-identical; installed plugin
  verified with `verify_installed_java_plugin`.
- `sync_manifest_java_plugin_profile` enabled `faded.whataworld.solarshadows`
  (and kept `faded.whataworld.textures`) in the local FJL profile.

No Workshop upload.

## Dedicated server deployment

Deployed the exact published tree to `faded-pz-vps` (`The Faded Realms`, B42.20.4):

- Asset downloaded on the host from the public release URL; size and SHA-256
  matched; per-file tree hash identical to the local installed tree.
- Target: `/home/pzserver/Zomboid/mods/WhatAWorld`, 1116 files,
  `modversion=1.4.0`, owner `pzserver:pzserver`
- Backup: `/home/ubuntu/WhatAWorld-before-1.4.0-20260917-000313` (882 files, 1.3.3)
- `project-zomboid.service` stopped, swapped, started; reached
  `*** SERVER STARTED ****` at 00:05:32 UTC. No players were connected.
- FJL server sync: `Up to date: WhatAWorld v1.4.0`, `changed=0`.
- The three 1.3.3 errors are gone: zero `WAW_SeasonData.lua` and
  `WAW_WeatherLoot.lua` traces, zero `weather loot registration failed`, zero
  `NoSuchFileException` for `mods/WhatAWorld/`. Zero What A World stack frames.
- `WhatAWorldSolarShadows` was not deployed; it is not in the server `Mods=` pack.

Known follow-up found in this boot log: `ground cover: the engine refused the
overlay table` is a false report. `TileOverlays.addOverlays` returns `void`, so
the guarded call returns nil on success and 1.4.0 misreads it as a refusal. The
overlays do register; the F7 restart-needed notice for ground cover cannot fire
until that check is fixed. `WhatAWorldTreeVisibility` 1.0.0's hosted ZIP still
lacks its `AnimSets`/`actiongroups` placeholder directories, so its four
`NoSuchFileException` lines remain.
