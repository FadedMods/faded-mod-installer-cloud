# Common Sense Reborn Test 2.1.4 — pre-release revision 3d39148846

This pull request switches Common Sense Reborn Test to 2.1.4 in Main and Faded Realms. The catalogs become live when the pull request merges. Production Common Sense Reborn 2.1.1 is unchanged. Deadflow 0.2.14, PZ Optimized 0.4.3, and FJL 0.6.10 are unchanged. `requiresJavaLoader` stays false, and no Java plugin fields were added.

The source patch is applied in `E:\Mod Projects\PZ-Common-Sense-Reborn` on the dirty working tree, not by resetting to git `b39bce6`. It does not restore deleted HEAD files and does not replace the omitted claim Lua files.

## Versions

Test Lua package `2.1.4`, stamped by `sync-test.ps1`. Production `mod.info` stays `2.1.1`. Hybrid `2.0.14` and Nearby `2.0.14` are the next independent plugin versions. Apartments stays `2.1.1` because it already accepts game version `42.22.0` and its source was not changed. Installed Test Lua `2.1.3` matches the working tree plus `TestOnlyAssets` except `mod.info`; this release does not replace that Lua with the older production tree.

## Admission

Hybrid and Nearby still refuse an unknown revision. They additionally accept `42.22.0` / `3d39148846` only with jar SHA-256 `3c4a7c5f149d784758c6fb5f8fa85f3a21d572e38bc081400e89035f8120d287`. The existing `e013dbb529` pin stays. `SelectorContractTest` checked that jar, including the `canRagdoll` guard order. The same guard order is present in the PZ Optimized 0.4.3 `IsoGameCharacter` override. FullHD behavior was not changed.

## Published Test package

- URL `https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/mod-assets-2026-11-08-csr-test-2.1.4-b42.22/CommonSenseRebornTest-v2.1.4.zip`
- SHA-256 `10ef8f347b716e4c9fa660d3dad2ee6d09527daa120262b350028ab5db5b4eb2`
- size `95362016`, uncompressed `253919656`, required free `886152584`
- source `791f91f3f527e1fcf5239a1a4fe3f5d6ba6dd4fc`, tag `v2.1.4-test`
- Hybrid and Nearby `2.0.14`; Apartments `2.1.1`

Running the stage script again with this publication record is refused because that package hash is already published.
