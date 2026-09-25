# Installer 0.3.5: retire Outback Steakhouse

Published September 25, 2026 at the owner's request.
[Download](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.3.5)

The Outback Steakhouse button, catalog tab and built-in source are removed in
both standard and multilingual builds. Existing saved Outback selections move
to FadedMods on startup. Other selected sources, custom catalogs, installed
mods and install paths are preserved. Outback's historical catalog remains
available for old clients, but its scheduled/push-triggered synchronization
was retired in cloud commit `1a85e55`; only manual dispatch remains.

## Source and verification

- Source commit: `1b5241c844bd8f97ff83f59ad0378ca19e658143`.
- Source tag: `faded-local-mod-installer-0.3.5`.
- 155 app tests pass, including saved-settings migration, custom-source
  preservation and absence of Outback in both Qt UI variants.
- Both packaged Windows EXEs contain 0.3.5, omit the Outback button and pass
  migration checks against their embedded config code. ZIP contents match
  the executables and pass CRC checks.
- [Linux/Steam Deck CI](https://github.com/FadedMods/faded-local-mod-installer/actions/runs/36122338809)
  and [Apple Silicon/Intel Mac CI](https://github.com/FadedMods/faded-local-mod-installer/actions/runs/36122338842)
  passed tests, builds and their native package checks.
- All eight public package downloads matched size and SHA-256 without auth.
  All ten GitHub release assets match their local digests. Portable archive
  path checks, Windows/Mac ZIP CRCs and Mac build-produced checksums pass.
- All seven existing app-update platform keys advance to verified 0.3.5
  packages. The generic macOS alias remains Apple Silicon for compatibility.
- No hosted game server was updated or restarted. OVH and Outback were
  expressly excluded by the owner.

## Artifacts

| Package | Bytes | SHA-256 |
| --- | ---: | --- |
| FadedLocalModInstaller-0.3.5-windows.zip | 55829478 | `117acc355d070a81c992fd206a011dd0eaa99c34d7ad4354b8227760887d1d2f` |
| FadedLocalModInstaller-0.3.5-windows-multilingual.zip | 55820357 | `9efc6b207b0fe8df63aca0e6962e5bde277db38c5c96bda5b827cae02c93f2ba` |
| FadedLocalModInstaller-0.3.5-linux-standard-x86_64.tar.gz | 390025045 | `825c7c0dc31ca34922014bde8545db2557463c741c1fdbe072c46569ee27d3f8` |
| FadedLocalModInstaller-0.3.5-linux-x86_64.tar.gz | 301319570 | `cae1451c07e5d8c1ae9a53c6584849a3d7715e3d55b23871f4f48f38d2c3f31b` |
| FadedLocalModInstaller-0.3.5-macos-arm64.zip | 47168021 | `4121b085aaaf76fd6bcc0cfd8a942fc89645258cdf3e6246f00c32f0af464660` |
| FadedLocalModInstaller-0.3.5-macos-x86_64.zip | 50619953 | `569792465fee93ec71f4dd69788ef3106f96524037f016c72852322da6f7bf5d` |
| FadedLocalModInstaller-0.3.5-macos-arm64.dmg | 53971886 | `5d52dec1b71525aa2830dc19eca1bd302379da539dd4c811fdc73ed71c3b24eb` |
| FadedLocalModInstaller-0.3.5-macos-x86_64.dmg | 57764026 | `c3295abc4f2b6d728da4cd74eac39f0140dda594156c7c5a39960052b1c84983` |

Local packages and versioned Windows executables are in
`E:/Mod Projects/Faded Local Mod Installer/release/`. Release source is the
clean worktree `E:/tmp/installer-0.3.4-outback` on the 0.3.5 release commit;
receipts and verification helpers are in its `.release-035/` directory.
The older source checkouts were preserved. Do not build a new package from an
older checkout without first updating it to the published source.
