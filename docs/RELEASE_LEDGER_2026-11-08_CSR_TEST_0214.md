# Common Sense Reborn Test 2.1.4 — pre-release revision 3d39148846

Catalogs stay on Common Sense Reborn Test 2.1.3 until the uploaded zip measurements are confirmed. Production Common Sense Reborn 2.1.1 is not part of this release. Deadflow 0.2.14, PZ Optimized 0.4.3, and FJL 0.6.10 are unchanged.

The source patch is applied in `E:\Mod Projects\PZ-Common-Sense-Reborn` on the dirty working tree, not by resetting to git `b39bce6`. It does not restore deleted HEAD files and does not replace the omitted claim Lua files.

## Versions

Test Lua package `2.1.4`, stamped by `sync-test.ps1`. Production `mod.info` stays `2.1.1`. Hybrid `2.0.14` and Nearby `2.0.14` are the next independent plugin versions. Apartments stays `2.1.1` because it already accepts game version `42.22.0` and its source was not changed. Installed Test Lua `2.1.3` matches the working tree plus `TestOnlyAssets` except `mod.info`; this release does not replace that Lua with the older production tree.

## Admission

Hybrid and Nearby still refuse an unknown revision. They additionally accept `42.22.0` / `3d39148846` only with jar SHA-256 `3c4a7c5f149d784758c6fb5f8fa85f3a21d572e38bc081400e89035f8120d287`. The existing `e013dbb529` pin stays. `SelectorContractTest` checked that jar, including the `canRagdoll` guard order. The same guard order is present in the PZ Optimized 0.4.3 `IsoGameCharacter` override. FullHD behavior was not changed.

## After the parent uploads the Test zip

Fill `docs/csr-test-2.1.4-publication.pending.json` `required_from_uploaded_package` with the confirmed URL, SHA-256, size, uncompressed size, and required free bytes. The URL must be the expected 2.1.4 URL above. Then:

```text
python3 scripts/stage_csr_test_2_1_4.py --publication docs/csr-test-2.1.4-publication.pending.json --apply
```

Do not run `--apply` before those five values exist.
