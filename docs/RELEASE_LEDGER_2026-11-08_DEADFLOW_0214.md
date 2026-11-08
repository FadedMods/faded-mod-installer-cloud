# Deadflow 0.2.14 — revised 42.22.0 revision 3d39148846

Main and Faded Realms now publish Deadflow 0.2.14 and PZ Optimized 0.4.3. The two Deadflow objects are identical, and the two PZ Optimized objects are identical. Outback, FJL, and Realm001 were not edited. GitHub release `mod-assets-2026-11-08-deadflow-0.2.14-b42.22` has both assets, and the catalog hashes and sizes are the release digests.

## Game bytes

Anonymous SteamCMD app 380870, branch `pre-release`, build 26486687. Linux and Windows depots both contain `java/projectzomboid.jar` SHA-256 `3c4a7c5f149d784758c6fb5f8fa85f3a21d572e38bc081400e89035f8120d287`. `GitVersion` and `Core` embed revision `3d39148846`. `Core` constructs `GameVersion(42, 22, "")`. `IsoWorld.getWorldVersion()` is still the constant 251.

The eight Deadflow engine targets and four collision workers are byte-identical to reviewed revision `e013dbb529`. `linux64/libPZPopMan64.so` and Windows `natives/PZPopMan64.dll` are the same bytes already pinned for that revision (`70fc9f4e…` and `60a102b3…`). No new native hash is allowlisted. PZ Optimized 0.4.0 and 0.4.1 stay bound to `e013dbb529` and are refused on this jar.

0.2.14 adds stock profile `STOCK_42_22_3D39148846` and looks for `PZPopMan64.dll` under `natives/`, which is where the Windows dedicated depot stores it. Unknown jars, edited classes, wrong natives and missing natives still fail closed.

## What was tested here

- `HookAudit` passed on copied Windows-client, Linux-dedicated (`java/` + `linux64/`) and Windows-dedicated (`java/` + `natives/`) layouts. Each selected `STOCK_42_22_3D39148846`.
- `NativeBoundaryTests`, `CompatibilityTests` (349), `CoreTests` (19) and `PopulationTests` passed.
- `tools/test-422-revised-layouts.py` passed the three admit layouts and four fail-closed cases.
- Linux `tools/native-collision-probe.py` passed (72 routes) on JRE 25.0.5. The Windows DLL was not executed; its hash matches the previously reviewed file.
- `src/main/java` compiled with JDK 25 against this jar and published FJL 0.6.10. Workspace jar SHA-256 `901d6ffd3670a9e75ebcc40e10a6f37654a45ffcf3f1663db78d835f699a28b6`. That jar is a compile check. `tools/build.ps1` on the parent tree is the publication build.

The catalog switch below records the parent gates that followed this review: Windows and Linux offline repair, Linux HookAudit and NativeBoundary, the Windows Deadflow suite, and isolated FJL 0.6.10 premain probes. FJL source was not modified. No server was restarted by this repository change.

## Parent steps

The uploaded assets are already on tag `mod-assets-2026-11-08-deadflow-0.2.14-b42.22`. Both catalog appliers have run. Running either one again with the confirmed publication record is refused because that package hash is already published. `minimumJavaLoaderVersion` stays `0.6.7` for Deadflow and `0.6.10` for PZ Optimized.

## Published catalogs

Deadflow 0.2.14, both catalogs:

- URL `https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/mod-assets-2026-11-08-deadflow-0.2.14-b42.22/Deadflow-v0.2.14.zip`
- SHA-256 `4ec8a0c18a2a0f7d779301dcc69fb027ea4d116bf5190d18140cd555c2e97d34`
- size `2587845`, uncompressed `2596591`, required free `542055348`
- `javaPluginVersion` `0.2.14`, `minimumJavaLoaderVersion` `0.6.7`
- plugin jar SHA-256 `092a61f0a2cf644ebc2ae235ad59df16e7d544214a331d2237bea8ee2084fcec`
- source `5455b1720fddc962c971fa55ba78ca81a460486c`, tag `v0.2.14`

PZ Optimized 0.4.3, both catalogs:

- URL `https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/mod-assets-2026-11-08-deadflow-0.2.14-b42.22/PZOptimized-v0.4.3.zip`
- SHA-256 `4460ce81890358c6a3a36e053757bc56b6a0035a6c240e1d870d24da04a9e166`
- size `251863885`, uncompressed `266476534`, required free `1055211331`
- `javaPluginVersion` `0.4.3`, `minimumJavaLoaderVersion` `0.6.10`
- plugin jar SHA-256 `043faa6528b228b8d71efc31528908a7068e693fc78a17f098b1ad6b00b694b5`
- source `5ae12f7a539b50d7e81f2b5028420ed6b94f518f`, tag `v0.4.3`, snapshot baseline `49e598587b52c2eaecae89f4bcab64cd4b1d0c25`

Parent gates that authorized this switch: 135 retained targets unchanged, PZO 90 tests with 0 failures and 1 platform skip, Windows offline repair passed, live Linux repair and its idempotent rerun passed with launcher SHA-256 `7014cadaeb072e21dac66e951769c41399af8fd4c555d9053aa4bb0736439f7a`, Linux HookAudit and NativeBoundary passed, and the Windows Deadflow suite passed. FJL 0.6.10 was not modified.
