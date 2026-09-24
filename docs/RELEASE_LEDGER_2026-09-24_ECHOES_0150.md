# Echoes of Humanity 0.15.0 deployment

Published 2026-09-24: https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-24-echoes-0150

Manifest commit: 441813159a77e44af44da33ed5b104e926a90b55. Only Echoes changed in Main (123 entries) and Faded Realms Season 3 (70 entries). Existing catalog URLs, selection sets and installer binaries are unchanged. Both canonical raw URLs were verified serving version and javaPluginVersion 0.15.0.

## Preparation and validation

The handed-off source was labeled planned 0.15.0 but its freshly built hotfix JAR still declared 0.14.0. Its 16:02 UTC validation and dedicated smoke records matched every current build input and payload hash. Release preparation assigned 0.15.0 to build.gradle, both mod.info files and META-INF/faded-java-mod.json, then rebuilt and reran tools/validate-release.ps1 -ServerSmoke.

The rebuilt JAR differs from the handed-off validated hotfix in only META-INF/MANIFEST.MF and META-INF/faded-java-mod.json. Every bytecode/resource entry is otherwise identical. The source repository was already extensively dirty; unrelated work was preserved and no broad source commit was made.

Final validation-status.json passed at 2026-09-24T16:14:12Z. Native regression, Lua, package, asset, voice and ABI checks passed. The shell wrapper surfaced a native Java warning on stderr; the completed validation record and staging's exact source/audit checks passed. Smoke build/smoke/20260924-121335-847 reached SERVER STARTED and passed native NPC, item/trait, trade and companion probes without fatal matches. These are headless checks, not a connected-player gameplay or rendered-UI verification.

## Artifact

- ID: EchoesOfHumanity
- Version and Java plugin version: 0.15.0
- ZIP: EchoesOfHumanity-v0.15.0.zip
- Size: 90,209,806 bytes
- SHA-256: e56d8b194cf3abce42ecff413ab2aa9f7c8d5052ddb63fcb513dc1d2654e5a68
- Runtime JAR SHA-256: a219f7f2c2c1e51cd81b7b7ff9a291df5630ac2ee72df0a03a73142abebaa79f
- Payload: 990 files, one version-folder mod.info and one runtime JAR. GitHub asset digest matches.

## Installation

The public ZIP was downloaded again through the installer, hash/size verified, prepared, and installed to C:/Users/Luis/Zomboid/mods/EchoesOfHumanity (the E:/PZ User Data junction). All 990 hashes match. Prior playable backup: C:/Users/Luis/AppData/Roaming/FadedLocalModInstaller/backups/EchoesOfHumanity_20260924_121636.

Canonical source stage: E:/Faded Mod Staging/EchoesOfHumanity. Immutable release: E:/Faded Mod Staging/EchoesOfHumanity-0.15.0-release. The canonical source stage retains the extra root mod.info, which is intentionally omitted from the public ZIP. Its 990 public payload files match exactly. The E:/FadedModsStaging/EchoesOfHumanity mirror matches the public package exactly.

FJL verification reports ready. The plugin declaration and schema-2 modList activation were verified without changing the profile. The legacy checker expects enabledPlugins, but the installed FJL profile uses owning-mod selection; the mod is enabled in default.txt and is not disabled in the profile.

Evidence: source build/reports-0150-release and build/smoke/20260924-121335-847; installer E:/Faded Local Mod Installer/.test-work/echoes-0150.

## Remaining runtime verification

The hosted server was not updated or restarted during this Echoes publication. It must consume 0.15.0 and restart before an updated client joins. Both sides require the same BOTH/transforming plugin. No successful live player join or rendered gameplay is claimed. Players use Refresh Mod List and update Echoes at the existing URL; no installer update is needed.
