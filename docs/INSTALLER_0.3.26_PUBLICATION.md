# Installer 0.3.26: normal Settings update

The stable `app-updates.json` advances all six installer editions together to
0.3.26. Existing users choose **Settings → Check for App Update**. The stable
feed URL and all seven existing selectors, including the legacy macOS arm64
alias, remain the same.

Release: https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.3.26

Source: `FadedMods/faded-local-mod-installer`, immutable commit
`6aa3c35e81ed44faaaf9ec5167dfb67ce0f06447`, tag
`faded-local-mod-installer-0.3.26`. Source PR9 merged into the maintained release
branch; no tag was changed during this feed promotion.

## Behavior

The frozen Linux installer removes its private Qt library paths from the FJL
child process while preserving external library paths and Java options. The
running installer keeps its own environment. Missing or malformed FJL JSON now
includes bounded, redacted process diagnostics. Windows, macOS and source-mode
environment inheritance retain their existing behavior.

The exact failure on the remote Ubuntu machine could not be reproduced from its
original logs. The unsafe inherited environment was independently reproduced
and fixed. An actual frozen Linux launcher, signed public FJL0.6.10 archive and
native Java25 returned the expected status JSON with the isolated child
environment; no game or user installation was changed by that proof.

## Qualification and publication

- Windows standard and multilingual were built natively with the maintained
  `scripts/build_candidate.ps1` from the exact clean source. These are local
  native builds; no Windows CI run is claimed. The 471-test suite completed
  successfully with six platform skips. The packaged README version header was
  normalized from 0.3.25 to 0.3.26; its remaining source text was preserved.
- Linux standard and Steam Deck came from successful native CI run
  `42848970580`; macOS arm64 and Intel came from successful native CI run
  `42848970615`. Their artifact archive hashes and exact source identities were
  checked before extraction.
- Each of the six final packages has a passing native frozen proof binding
  23 application modules and 30 actual embedded resources to that source's Git
  blobs. Final executable hashes, PE/ELF/Mach-O architecture and archive
  integrity were independently checked. macOS DMG/checksum files were retained.
- The public release contains 18 assets: six primary packages, two DMGs, two
  macOS checksum files, six normalized native proofs, release notes and a
  complete SHA256 manifest. Existing published Ubuntu bytes are reused without
  replacement: 428,401,534 bytes, SHA256
  `dc2af538d60805fadc067881dc259e4e33c971af133cea907c3c92f4bfc8880e`.
- The unmodified published 0.3.25 Settings updater accepts all six selections,
  offers 0.3.26, preserves the legacy Mac alias and neither repeats the update
  after 0.3.26 nor downgrades a newer version.
- The actual 0.3.25 Linux installation helper upgraded an isolated XDG user
  installation using the qualified 0.3.26 archive, preserved a settings
  sentinel, refreshed its executable symlink and desktop entry, and selected
  the updated wrapper for relaunch. The resulting frozen application ran CLI
  help successfully. This was an isolated helper proof, not a graphical click
  or a change to an existing user installation.

The macOS Finder bundle metadata retains the build scripts' existing generic
`0.0.0`. The actual application, Settings updater and all archive names use the
verified runtime version 0.3.26; this preexisting packaging detail was not
changed in the Linux fix.

`INSTALLER_0.3.26_PUBLICATION.json` records the exact source, package identities,
native proofs and server asset identities. Per-edition public proofs distinguish
local Windows qualification from GitHub Actions provenance. No gameplay catalog,
game binary, FJL package, user preference or local playable mod is changed by
this installer feed promotion.
