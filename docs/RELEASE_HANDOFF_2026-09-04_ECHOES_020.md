# Echoes of Humanity 0.2.0 Release Handoff

Release date: 2026-09-04

## Published Release

- Mod ID: `EchoesOfHumanity`
- Version: `0.2.0`
- Release tag: `mod-assets-2026-09-04-echoes-of-humanity-0.2.0-living-world`
- Asset: `EchoesOfHumanity-v0.2.0.zip`
- Asset size: `23,571,192` bytes
- Uncompressed payload size: `28,155,175` bytes
- SHA-256: `36287fe1a96ffe6072612ab7c0637b19c4665e78f88374fe135b7b74e6018bc6`

The main and Faded Realms manifests expose identical release, Java-loader,
size, and digest metadata. The manifest publication commit is `8d3d495`.

## Packaging Repair

The incoming staged archive contained both `EchoesOfHumanity/mod.info` and
`EchoesOfHumanity/42/mod.info`. The installer correctly rejected that archive
because it represented two possible mod roots. The release was repackaged from
the canonical staged/source payload with the repository's portable mod packager.
The redundant root metadata was omitted; `EchoesOfHumanity/42/mod.info` is the
single authoritative Build 42 descriptor. No runtime payload file was changed.

The published ZIP has 589 files, uses portable forward-slash archive paths, and
matches the staged/source tree byte-for-byte after excluding only the redundant
root `mod.info`.

## Verification

- Manifest safety validation passed.
- Main and Faded Realms raw manifests were fetched after publication and both
  resolved Echoes of Humanity 0.2.0 with the expected SHA-256.
- The public asset was downloaded through the installer's manifest client and
  passed archive preparation.
- All 113 translation JSON files parsed successfully.
- All 19 Lua files passed syntax loading.
- The supplied dedicated-server smoke receipt passed, including server startup
  and the native probe.
- GitHub `Validate manifests` and `Push on main` workflows passed for `8d3d495`.

The supplied smoke evidence does not represent a connected-player or physical
vehicle-driving playtest.

## Local Playable Deployment

The public artifact was installed with backup-and-replace into:

`E:\PZ User Data\Zomboid\mods\EchoesOfHumanity`

The prior playable copy was backed up at:

`C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260904_211213`

Post-install comparison found 589 public files and 589 local files with no
missing, extra, or mismatched files. The installed `mod.info` and native plugin
descriptor both report version `0.2.0`; the plugin ID remains
`faded.echoesofhumanity` and requires Faded Java Loader `0.2.0` or newer.

## Source Preservation

The Echoes of Humanity source worktree contained the update author's uncommitted
0.2.0 changes. It was inspected but not reset, cleaned, staged, or otherwise
modified during publication.
