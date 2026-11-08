# Deadflow 0.2.14 — revised 42.22.0 revision 3d39148846

Catalogs are intentionally still on 0.2.13. Live `main` matches this branch for both `manifest.json` and `manifests/faded-realms.json`, and their Deadflow objects are identical. `scripts/stage_deadflow_0_2_14.py` is the catalog switch. It does not write unless `--apply` is given a complete publication record, and this commit does not run it. Pointing either catalog at the 0.2.14 URL before the asset exists would 404 the installed mod.

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

Not claimed: live FJL premain, a played world, RCON, an existing Deadflow save, or a PZO repair for `3d39148846`. `tools/test-42.22-joint.py` still needs the parent's FJL, PZO and retained 42.21 fixtures. Its PZO cases remain valid only for `e013dbb529`.

## Parent steps

Source base is Deadflow git `d7198e8d22dbafe0cbfd6e6671c19b8aa9cba451`, branch `release-0.2.13`. From that repository root:

```text
patch -p1 < deadflow-0.2.14-against-d7198e8.patch
```

The Deadflow source patch dry run was clean. Build and package with `tools/build.ps1` and the existing packager. Upload `Deadflow-v0.2.14.zip` to tag `mod-assets-2026-11-08-deadflow-0.2.14-b42.22`. Then fill `docs/deadflow-0.2.14-publication.pending.json` `required_from_uploaded_package` with the confirmed `download_url`, `sha256`, `size_bytes`, `uncompressed_size_bytes`, and `required_free_bytes`, and run:

```text
python3 scripts/stage_deadflow_0_2_14.py --publication docs/deadflow-0.2.14-publication.pending.json --apply
```

The applier updates only the Deadflow objects in `manifest.json` and `manifests/faded-realms.json`. It refuses to run unless both catalogs are still the published 0.2.13 package, and it leaves PZ Optimized, FJL, and every other entry untouched. `minimumJavaLoaderVersion` stays `0.6.7`. The expected URL is `https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/mod-assets-2026-11-08-deadflow-0.2.14-b42.22/Deadflow-v0.2.14.zip`.

Suggested description, already in both `mod.info` files:

```text
Population authority for new Deadflow worlds on 42.20.4, 42.21 and 42.22 (Windows and Linux dedicated). Stock 42.22 includes reviewed revisions e013dbb529 and 3d39148846. PZ Optimized 0.4.0 and 0.4.1 remain limited to revision e013dbb529. Older saved zombie snapshot formats are not migrated. Requires FJL 0.6.7+ and its fixed Bridge.
```

FJL was not modified. No server was restarted and no save backup was taken.
