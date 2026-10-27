# Schedule I / FadedCore catalog

The separate `schedule-i-manifest.json` describes immutable player runtime,
independent C# mods and developer SDK downloads. It never changes PZ catalog
membership or settings. Initial release: [FadedCore 0.3.0 RC2](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/schedule-i-fadedcore-0.3.0-rc2).

The runtime has a production-channel signature; the release is a prerelease RC.
The unchanged SDK kit remains a developer preview. Its internal inventory is
local-development/non-production-eligible, and no first-party license grant is
added. Players need the runtime, not the developer ZIP.

Create C# mods against FadedCore.SDK.dll, compile using the generated build.ps1,
then separately package/sign their clean output with the existing protected
publisher key. New independent mods need only immutable `.fmod` uploads and new
rows in `mods`, with runtime/API/game/dependency requirements. Framework rebuilds
and installer changes are unnecessary for each supported mod.

Schema 1 has `product: schedule-i`, `channel: production`, `helper`, `runtime`,
`sdk`, and `mods`. Each download row has `id`, `kind`, `version`, `url`, `size`
and `sha256`. Runtime/mod signed metadata remains activation authority. The
installer pins helper/public-trust bytes independently; catalogs cannot replace
them. Private signing keys are never distributed. Run:

```text
python scripts/validate_schedule_i_catalog.py schedule-i-manifest.json
```

Upload new versioned assets, verify actual public downloads and package
signatures, then update this catalog in a clean current-main checkout. Do not
overwrite released assets or unrelated catalogs. SDK integrity is independently
checked by catalog size/hash; it is not an `.fmod` publisher signature.

Compatibility requires exact signed game fingerprints for Steam app 3164500,
build 25796331, Windows x64 and registered Microsoft.NETCore.App 10.0.12 with
roll-forward disabled. Installation composes per-user immutable generations,
preserving mutable data and changed/unowned residues. Dependencies are checked
but not acquired automatically. Startup configuration needs restart; live session
enable/disable and menu controls are separate.

The initial catalog has runtime and SDK entries, with no separately published
gameplay mods. The suite includes example/probe mods; gameplay acceptance probe
is startup-disabled. Multiplayer remains assumed/unverified, comparative
performance partial, host geometry/navigation local, and AssetBundles stripped.
No blanket AI arbitration, multiplayer negotiation or hot assembly replacement
claim is made. [Installer 0.3.19](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.3.19)
exposes this public catalog through the Schedule I tab. Existing users use
Settings -> Check for App Update. The in-app guide includes migration from the
older development-signed preview. Future compatible gameplay mods need only an
independently signed package upload and a new row in this catalog.
