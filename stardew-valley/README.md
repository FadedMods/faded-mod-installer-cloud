# Stardew Valley distribution

Installer 0.3.24 adds a separate Stardew Valley tab and production catalog:

```text
https://raw.githubusercontent.com/FadedMods/faded-mod-installer-cloud/main/stardew-valley-manifest.json
```

The URL stays stable across package releases. This catalog is independent of the
Project Zomboid and Schedule I catalogs and their settings. Players refresh the
Stardew catalog to receive new package versions.

The initial packages target Stardew Valley 1.6.15 and SMAPI API 4.5.2. Install
[SMAPI using its official installer](https://smapi.io/), select the game folder,
and install Darkdew Valley. The installer installs its separate Stardew Mod
Framework dependency into the same game's `Mods` directory. Launch through SMAPI.
Players do not need the .NET 10 SDK used by the authors to build these mods.

`runtime` identifies the framework; `mods` contains independently updated gameplay
mods. Each row has its SMAPI UniqueID, version, folder, entry DLL, minimum game/API
versions, dependencies, immutable GitHub release ZIP URL, exact byte length and
SHA-256. Archives have exactly one mod folder. Framework and gameplay packages
remain separate; game and SMAPI assemblies are never bundled.

The initial framework 0.2.0 ZIP contains the rebuilt HD texture API needed by
Darkdew Valley 0.1.1. An older local development framework also labeled 0.2.0 is
not sufficient. Package identity includes the archive hash, and installation
receipts track payload files so older same-version binaries can be repaired.

The packages contain portable managed assemblies. Author native runtime evidence
was recorded on Windows; connected multiplayer, full-year gameplay, all clothing
and special-animation combinations, and presentation-mod combinations remain
unqualified. The installer changes only the selected owned mod folders and
preserves user configuration and unrelated files; neither archive contains saves.

Before publishing, run the catalog tests and validate exact local archives:

```text
python -m unittest discover -s scripts -p test_validate_stardew_catalog.py
python scripts/validate_stardew_catalog.py stardew-valley-manifest.json --archive-dir PATH_TO_RELEASE_ZIPS
```

CI validates metadata, dependency closure and cycles, component identity, safe
folders and immutable download origins without downloading or executing mod code.
The optional local archive check verifies size, hash, CRC/readability, single-folder
layout, duplicate/case collisions, entry DLL, SMAPI manifest identity/version and
required dependencies. Release assets must be uploaded before the catalog is
published, and actual public installer downloads must be verified afterward.
