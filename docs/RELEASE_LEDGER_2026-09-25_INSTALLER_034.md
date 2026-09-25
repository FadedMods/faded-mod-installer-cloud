# Installer 0.3.4 / Outback Steakhouse release

Published September 25, 2026. [Download all platforms](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.3.4).

Outback Steakhouse now has a visible manifest-channel button and built-in
modder-list entry. Existing settings receive the source once while preserving
the active catalog and install folder. Select Outback Steakhouse, All Mods,
clear the search, Select Visible, then Install Queue.

Its public catalog has all 59 entries from Nexus pack `2026.09.25.1-outback-full`.
IDs, server IDs, order, versions, artifact hashes and sizes match; the loader
catalog is FJL 0.4.4. Four older mod versions are deliberately retained to
match this published server pack. Catalog commit: `afa0a41`.

The cloud Actions workflow synchronizes from Nexus after Main catalog changes,
on manual dispatch, and on a ten-minute schedule, subject to GitHub scheduling
delays. Exact historical artifacts are resolved from Git history. Failure or
an unavailable/mismatched artifact preserves the last valid catalog.
Future pack changes need a list refresh, not another app update.

## Source and builds

- Source commit/tag: `de2931de256fb70ea12c4adf4fc24463aaef5154` / `faded-local-mod-installer-0.3.4`.
- [Source](https://github.com/FadedMods/faded-local-mod-installer/commit/de2931de256fb70ea12c4adf4fc24463aaef5154)
- [Linux and Steam Deck CI](https://github.com/FadedMods/faded-local-mod-installer/actions/runs/36096301980)
- [Apple Silicon and Intel Mac CI](https://github.com/FadedMods/faded-local-mod-installer/actions/runs/36096301970)
- [Nexus catalog sync CI](https://github.com/FadedMods/faded-mod-installer-cloud/actions/runs/36096168891)
- Clean source worktree: `E:/tmp/installer-0.3.4-outback`.
- Versioned local packages and Windows executables: `E:/Mod Projects/Faded Local Mod Installer/release`.
- The older dirty checkout at `E:/Faded Local Mod Installer` was preserved;
  do not rebuild 0.3.4 from its old branch without updating the source first.

## Verification

- 154 app tests pass on Windows and both Linux and Mac build variants.
- Six catalog sync tests cover exact historical artifacts, missing/mismatched
  data, ordered multipart downloads, duplicate/empty/foreign/quarantined packs,
  atomic failure preservation, a changing pack and repeat syncs.
- All eight platform packages downloaded publicly without authentication and
  matched their size and SHA-256. All ten GitHub assets (packages, notes and
  checksums) match local digests. ZIP CRC/path and Linux archive checks pass.
- Native Mac jobs verify app architecture, ad-hoc signature, packaged CLI,
  ZIP signature and DMG checksums. Linux jobs verify packaged dependencies and
  installed-style launcher execution.
- Both Windows EXEs contain version 0.3.4, the Outback source, and the Mac
  architecture update selector; packaged EXEs match their ZIP contents.
- Built standard Windows CLI installed public Outback ClearView 0.6.18 into
  isolated directories twice (clean, then backup-and-replace), both exit 0,
  all 1,078 files identical and the previous copy backed up.
- Standard and multilingual UI layouts queue all 59 mods at desktop and
  minimum window sizes. The multilingual build shares the tested install
  path but still does not expose the standard executable's CLI entry point.
- All 67 pinned mod/loader asset URLs respond with their expected byte sizes.
- Main and Faded Realms mod catalogs, server configuration and local playable
  mods are unchanged by this installer task. No connected-game test is claimed.

Mac update selection now distinguishes Intel and Apple Silicon. Intel Mac
users upgrading from 0.3.3 or earlier must choose the `macos-x86_64` download
on the release page; old versions use the generic Apple Silicon feed entry.

## Artifacts

| Package | Bytes | SHA-256 |
| --- | ---: | --- |
| FadedLocalModInstaller-0.3.4-windows.zip | 55830661 | `3cd9a63a4104e46baab9b56b33df2e8c7566958536ad89db986af86590f7e6ba` |
| FadedLocalModInstaller-0.3.4-windows-multilingual.zip | 55818148 | `b83d941d3102189e0708d950b4e85a9575ed70689ecfbfb9219ee389a808263d` |
| FadedLocalModInstaller-0.3.4-linux-standard-x86_64.tar.gz | 390020987 | `e0f0fdb4751f819ce43e2dacae99a470c232d0b95bca3eb74b5467b71eef9262` |
| FadedLocalModInstaller-0.3.4-linux-x86_64.tar.gz | 301302426 | `4d1e7c19acb3e72de79d177206eb81846bea7c61c1c7dee21eb5a3758646b69f` |
| FadedLocalModInstaller-0.3.4-macos-arm64.zip | 47167956 | `511ae5e0566c32769e40b84455fd7942ac3ecb4f6b43e657b4f8c48c1ed8ec2d` |
| FadedLocalModInstaller-0.3.4-macos-x86_64.zip | 50621018 | `d3bbb106792db13a207b07965a54df932aa4e11978d409365a5ace1dc6b15e28` |
| FadedLocalModInstaller-0.3.4-macos-arm64.dmg | 53971480 | `8b6baa3a5f836bf29b5af020c54c119d0640aada40dc63a5f78cc6bae3fae39d` |
| FadedLocalModInstaller-0.3.4-macos-x86_64.dmg | 57764510 | `f1c4637c4450e1337cf122cdf3398c49272ecc92be924809d3a7e93ec22e51c6` |

All seven existing app-update platform keys point to verified 0.3.4 assets;
the generic `macos` alias remains Apple Silicon for compatibility. Release
notes and `SHA256SUMS-0.3.4.txt` are published alongside the packages.

Evidence is retained in the clean worktree's `.test-work`: `release-artifacts.json`,
`public-release-receipts.json`, `github-release.json`, `packaged-install/receipt.json`,
and `outback-verification/receipt.json` plus `public-link-receipts.json`.
