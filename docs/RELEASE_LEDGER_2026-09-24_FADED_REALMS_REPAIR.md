# Faded Realms repair release — 2026-09-24

Release: https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-24-faded-realms-world-ui-vehicle-repair

| Mod | Version | ZIP bytes | SHA-256 |
| --- | --- | ---: | --- |
| CommonSenseReborn | 2.0.5 | 64537082 | 830adb14657759cb70c9a85d8b3e4bb3f896e1f2d39a2a39727a8f07a07f79be |
| CommonSenseRebornTest | 2.0.5 | 66021737 | ae8d64388cf4739ace6c55a54d51e48decafced64a60f8cc673f7f0a633a98a3 |
| EchoesOfHumanity | 0.15.1 | 90300332 | cd4546d4fa0a94bcc43eadb6b6f1d387b59912cc81ae965cd688e8600fa1212e |
| FadedsClearViewUI | 0.6.18 | 4782166 | 14930c14c51707064bb67043f9f6be3fc6c198fc5e49d5ec214bba1c9b282d13 |
| FadedTacticalOperationsCenter | 1.1.15 | 2707165 | 0193a81ea17f535ecb9cc7a64b7f5fc87e0b0f1c3811cd84c84245e9c0e184bc |
| ModernEVs | 1.0.2 | 31775883 | e356b6aa237d09976024e15a9673c33ad9d134230bcead12263ff791038be439 |
| VehiclesByFaded | 1.0.2 | 64056288 | 004c5a688105730c35d492ac15b08ec8940aa93c8771ffba635d4ae62cb84c2b |

Repairs for the Faded Realms Build 42.20.4 pack:

- CSR Main/Test 2.0.5 yields target outlines to the active Back to Atlanta renderer and accepts ClearView 0.6.18 inventory markers.
- ClearView 0.6.18 supplies a compact character/health workspace, vanilla anatomy art, TPLT levels 11–15 and confirmed mastery choices, and native map/admin input cooperation.
- TOC 1.1.15 repairs transparent-area mouse routing, native dialog focus, tool teardown, and provider status formatting. The optional companion remains 1.1.5.
- Echoes 0.15.1 gates Tikitown faction/civilian locations by selected map and defers client NPC presentation while its square is unloaded.
- Modern EVs 1.0.2 fixes B42's Set-based vehicle traversal and avoids repeated scans for multiple players.
- Vehicles by Faded 1.0.2 restores authored vertex colors and embedded textures in affected skins; geometry, bones and animation clips match the prior assets within export floating-point precision.

Automated checks: ClearView 1,719 release checks and isolated B42 server smoke; CSR 83 outline and 24 inventory assertions plus B42 package validation; Echoes complete release validation (565 runtime classes, native regressions, ABI and asset audits); TOC Lua/static/mock suites; Modern EVs Set/cadence/proximity regression; VBF full pack checks and 24 geometry/rig/clip comparisons. The historical TOC Java rebuild test needs an unavailable pinned FJL 0.3.4 API artifact; the packaged companion is byte-identical to the prior installed release.

Interactive visual results, map teleport, and measured multiplayer FPS remain unverified. The unexplained empty UI rectangle still needs a fresh-client observation to identify its owner. A full client and server restart is required.


Main remains 123 entries. The Faded Realms preset is 69 entries after the owner-requested Solar Shadows removal. General Main catalog availability is retained. Stable manifest URLs and installer application version are unchanged.
Every package passed installer prepare, CRC, path/case safety, exact staged file and directory verification. GitHub asset digests match all seven local ZIPs. CSR retains optional FJL metadata; Echoes plugin version is 0.15.1.
