# What A World 1.4.2 release ledger

Published 2026-09-25 by request. Catalog commit:
`f4b10f273db859fa417c85a29d97aee9faa151ae`.

- Release: [What A World 1.4.2](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-25-what-a-world-1.4.2)
- Asset: `WhatAWorld-v1.4.2.zip`, 146,263,077 bytes.
- SHA-256: `38623fbcd82f4ffedfb42c18faf50134a3e793a78294aedef83c14a1509cf5e9`.
- Optional client plugin: `faded.whataworld.textures` 1.3.2. FJL remains optional.

## Changes and verification

Bird artwork is shipped at a 256-pixel maximum edge instead of roughly 1,600
pixels for 40-82-pixel draws: 96.54 -> 3.18 MiB of raw RGBA pixels. The runtime
loads individual sprites, skips off-screen submissions, removes idle draw
callbacks, and handles disable/slow-frame/timer lifecycle correctly. Java pack
replacement now honors the texture governor's protected-asset exclusions.

The downloaded 1.4.1 package differs in exactly 20 files: the bird Lua module,
16 bird PNGs, Lua version, mod.info version, and the optional plugin JAR. No
files were added or removed. Inside the JAR only TexturePack.class and the two
version metadata files changed.

Release gates passed: consent (including final pre-stage check), 1,399 Lua
behavior checks, shipping smoke, installed-game API surface, name scan against
250 other mod directories, both Java builds, 189 Java checks, sprite budget,
and package check. Installer prepare and ZIP CRC checks passed. Actual in-game
FPS and reported lockup resolution remain unmeasured on affected hardware.

## Catalog and deployment

Main retains 123 entries; Faded Realms retains 69. Only WhatAWorld changed in
each, with ordering, IDs, descriptions, optional-loader semantics and all
unrelated fields preserved. Both canonical public raw URLs served 1.4.2 before
installation. Manifest safety validation and the commit-specific Validate
manifests / Outback synchronization Actions passed. Outback's pinned server
catalog was not manually edited.

The public ZIP was downloaded through the installer, SHA-256 verified, prepared,
and installed with BACKUP_REPLACE. All 1,116 files match the public ZIP at:

- Local play: `E:/PZ User Data/Zomboid/mods/WhatAWorld` (also reached through
  the `C:/Users/Luis/Zomboid` junction).
- Staging mirror: `E:/Faded Mod Staging/WhatAWorld`.

Previous local installation:
`C:/Users/Luis/AppData/Roaming/FadedLocalModInstaller/backups/WhatAWorld_20260925_011608`.
Previous staging:
`E:/Faded Local Mod Installer/.test-work/waw-142/stage-backup/WhatAWorld`.

Local FJL verifies ready, WhatAWorld remains in the active preset, and the
profile hash was unchanged by installation. No hosted game server was restarted
or deployed during this request. Detailed evidence and helper script are under
the installer's `.test-work/waw-142/`; those files are not committed.
