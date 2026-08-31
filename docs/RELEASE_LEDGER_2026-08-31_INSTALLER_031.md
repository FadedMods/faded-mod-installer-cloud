# Faded Local Mod Installer 0.3.1 Release Ledger

Published August 31, 2026.

- Source repository: `FadedMods/faded-local-mod-installer`
- Source commit: `4d6460b4e2b2afd7b301734ade371a93466a285f`
- Source tag: `faded-local-mod-installer-0.3.1`
- Public release:
  <https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.3.1>
- Linux workflow: `33437844758` — successful for standard and Steam Deck.
- macOS workflow: `33437844778` — successful for arm64 and x86_64.
- Local/source test suite: 144 tests passed.

The release fixes Windows extraction failures for Buildcraft Reborn by
migrating the generated deep AppData staging default to `%TEMP%\FMI`. Explicit
custom staging directories remain unchanged. Buildcraft itself was not
republished because its public asset passed URL, size, SHA-256, CRC, portable
path, preparation, installation, and backup/replace verification.

The Player Install layout now provides two complete catalog card rows at the
1320x900 reference size after a live 103-mod refresh. The Faded dark/purple
palette and character artwork were not changed. Top 5 and activity panels are
available through compact toggles, and failures reveal activity automatically.

`SHA256SUMS.txt` in the release is the authoritative checksum list for all
eight platform packages. The stable automatic-update catalog remains:

```text
https://raw.githubusercontent.com/FadedMods/faded-mod-installer-cloud/main/app-updates.json
```
