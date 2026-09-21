# Echoes of Humanity 0.6.2 — release evidence

Working repository: `E:\Mod Projects\Echoes of Humanity`. Existing modified/untracked work was preserved. FFO source was read only. The user authorized implementation, publication, local playable update and the usual protected OVH restart.

## Native delivery and checks

Implemented the finalized `TRIAL_DOSE_HANDOFF.md`: actual consent-bound NPC Strength/Fitness, fever relief and infection-suppression actions, exact original dose and clinician syringe consumption, patient lifetime/cooldown reservations, saved physical evidence and fail-closed uncertain-commit recovery. Campaign API remains 3. See [the exact API contract](campaign/CLINICAL_DOSE_API.md) and [handoff](campaign/FFO_NATIVE_HANDOFF_RESULT.md).

Runtime: `Contents/mods/EchoesOfHumanity/42/java/EchoesOfHumanity-0.6.2.jar`, 391 classes, 1,417,155 bytes, SHA-256 `98d17864e7c5251651e13c298815e4eb8263ff44ee9db8e65890568fb45f6301`. Previous 0.6.1 runtime was preserved in `.test-work/release-062` before the bump. One runtime JAR is packaged.

Full `tools/validate-release.ps1 -ServerSmoke` passed. New checks: 87 real game-body effects, 35 authority/lifetime policy checks, 37 original-item transaction checks, 18 transformed native survivor XP save/load checks. Existing 149 Storylines/clinical checks, movement/visibility/ranged checks, Lua/asset/voice/UI/authority gates and all original public/protected descriptors in 31 maintained overlays pass. Actual FFO campaign syntax: 147 Lua files passed.

Exact-runtime isolated B42.20.4 startup: `build/smoke/20260920-200453-107`, passed at 2026-09-21 00:05:33 UTC. Native API/schema probes, 113 item registrations, ten faction traits and SERVER STARTED passed without checked fatal signatures. This is headless startup and offline native verification, not connected-player clinical or visual acceptance.

## Installer correction

Faded Local Mod Installer 0.3.2 looked only for root-level bridge metadata, while the signed FJL 0.4.0 archive correctly places it in `FadedJavaLoaderBridge/42/mod.info`. This produced a false missing-bridge failure even with an active installed bridge. Installer 0.3.3 accepts and validates the actual B42 layout while retaining legacy support. No dependency was bypassed or removed.

Installer source commit `236f20529874864e15aa4ba190ef309e10f4dcf7`; 151 tests passed. Linux and macOS CI builds passed. Eight platform archives were verified; standard packaged Windows executable passed real clean and replacement installs using an isolated game shell, including bridge, preset and Java plugin profile setup. Multilingual uses the same corrected installer code but its existing entrypoint has no CLI; no multilingual CLI pass is claimed.

Deployment receipts and final publication details follow after the public download/local/server verification.


## Completed publication and deployment

- [Echoes 0.6.2 release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-20-echoes-062) and [Installer 0.3.3 release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.3.3) are public. The installer includes Windows standard/multilingual, Linux standard/Steam Deck and macOS arm64/Intel ZIPs and DMGs: eight packages, all checksummed.
- Main/Faded Realms catalogs and app updater: commit `0ca0488`; all three GitHub checks passed. Preserved all 119 Main and 79 Realms IDs. Every updater URL, byte count and SHA-256 matches the published artifact. The production updater advertises 0.3.3 to both Windows variants.
- Echoes ZIP: 52,700,993 bytes, 838 files, SHA-256 `fcdbbd12d39dd766aac05b0d31e6d610603ccd4a505abf36519f6a1657b36b98`. Public download and both production catalog readers verified.
- Packaged standard installer 0.3.3 installed public Echoes 0.6.2 successfully in both clean and existing-bridge fixtures: exit 0, all 838 hashes match, FJL 0.4.0 READY, B42 bridge and plugin profile enabled. Real game shell remained unchanged by the fixtures.
- Local playable updated using BACKUP_REPLACE; all 838 files match. Prior copy: `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260920_200854`.
- Protected zero-player OVH backup/restart completed. Verified archive `project-zomboid-20260921T000923Z.tar.zst`: 13,162,372,232 bytes with checksum file; native helper completed successfully.
- Service active since **Mon 2026-09-21 00:12:32 UTC**. Full startup verified **2026-09-21T00:15:23.597472+00:00**: GAME_READY, WorldDictionary completion, SERVER STARTED, UDP 16261/16262, fresh online heartbeat and zero crash restarts. All 80 enabled server IDs remain unchanged.
- All 838 OVH files match the public ZIP and belong to pzserver. Nexus advertises Echoes 0.6.2 with the correct artifact hash.
- Updated Downloads PDF: 34 pages, 31 bookmarks and 93 links. SHA-256 `68e099e1056609efd93cb51cd7a3144d94b6f8c22992638e1d3b5c0e2e0f31e0`. The date-corrected public guide is `EchoesOfHumanity-0.6.2-Player-Guide-2026-09-20.pdf`; the first immutable guide asset remains available. Matching Discord copy-paste text is in Downloads and the release.

Exact clinical API and completed work are in `docs/campaign/CLINICAL_DOSE_API.md` and `docs/campaign/FFO_NATIVE_HANDOFF_RESULT.md`. Latest FFO handoff hashes were rechecked unchanged. Remaining acceptance: FFO-owned UI/production flow and connected-player clinical behavior. No connected-player game test is claimed. Existing unrelated pack warnings remain outside this patch.

Machine-readable evidence: `docs/campaign/RELEASE_0.6.2_VERIFICATION.json`. Local deployment/install receipts: installer `.test-work/echoes-062` and `.test-work/echoes-next-install/full-install/20260921T000842240178Z`.


Local loader follow-up: signed FJL 0.4.0 is READY; Echoes 0.6.2 plugin metadata, active default mod preset, bridge and explicit-disable checks pass. The local schema-2 profile uses `pluginSource=modList`, so native activation follows the selected owning mod. Its profile was preserved. Installer 0.3.3's older installed-status repair checker can still show a false legacy-profile warning on migrated schema-2 profiles; normal installation succeeds and this is separate from the corrected missing-bridge failure. This remaining installer status-display issue is recorded for follow-up; no native activation bypass was introduced.
