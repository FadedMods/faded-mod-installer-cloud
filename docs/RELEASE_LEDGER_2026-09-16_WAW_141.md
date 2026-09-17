# What A World 1.4.1 release ledger

- Published: 2026-09-16
- Release: `mod-assets-2026-09-16-what-a-world-1.4.1`
- Main manifest: `WhatAWorld` (version update)
- Faded Realms manifest: `WhatAWorld` (already in the live `Mods=` pack)
- Supersedes 1.4.0 (`RELEASE_LEDGER_2026-09-16_WAW_140.md`). Solar Shadows 1.0.0
  is unchanged; its rebuilt JAR is byte-identical to the published one.

## Content change

Two defects introduced in 1.4.0, found in its first dedicated-server boot log:

- Closed garage doors never showed damage stages. `IsoSprite:LoadSingleTexture`
  returns a Texture; 1.4.0 compared it against `true`. Fixed to a truthiness
  check, with a behavioural test that fails on 1.4.0.
- Ground cover logged "the engine refused the overlay table" on every boot
  although the overlays registered. `TileOverlays.addOverlays` is `void`; the
  result of a guarded call cannot signal success. Now taken from `pcall`'s
  status, which also restores the F7 restart-needed notice.

Files changed versus 1.4.0: `WAW_FX_DoorDamage.lua`, `WAW_GroundCover.lua`,
`WAW_Core.lua` (version), `42/mod.info` (version). Nothing else.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `WhatAWorld-v1.4.1.zip` | 161,982,913 | `b6835246fadab68742d84d12ac44645c5a0af06fc8d0c7943951eb4408d57f5c` |

The ZIP is 477 KB larger than 1.4.0 with identical entries and uncompressed
sizes: it was packaged with the installer `.venv` Python, whose zlib deflates
the console `.dat` binaries slightly differently. Content parity is exact.
GitHub asset digest matches.

## Package validation

- Staged source: `E:\Faded Mod Staging\WhatAWorld`; 1.4.0 staging preserved at
  `E:\Faded Mod Staging\WhatAWorld-1.4.0-superseded`
- `scripts/package_local_mods.py`; exactly one `WhatAWorld/42/mod.info`, no
  double nesting; `prepare_mod_zip` passed; 1116/1116 files byte-identical to
  staging; `modversion=1.4.1`
- WAW gates: consent contract, 1,389 behaviour checks, smoke, engine API, name
  collisions, `build-java.ps1` (both plugins, WAW JAR unchanged), package check

## Catalog shape

Main 119 and Faded Realms 79, one entry changed in each, order and top-level
blocks preserved. `scripts/validate_manifests.py` passed.
