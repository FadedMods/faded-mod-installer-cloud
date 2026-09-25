# Faded Mod Installer Cloud

Public manifest and release-asset host for Faded Local Mod Installer.

## World Forge

[World Forge](products/worldforge/README.md) is the new standalone Windows map
editor preview for Project Zomboid B42.20.4. Download the portable app, illustrated
PDF guide and view real editor screenshots on its product page. Installer **0.3.6**
adds a World Forge tab beside Nexus on every installer platform.

## Manifest URL

Use this URL in the installer's **Manifest URL** setting:

```text
https://raw.githubusercontent.com/FadedMods/faded-mod-installer-cloud/main/manifest.json
```

Faded Realms uses:

```text
https://raw.githubusercontent.com/FadedMods/faded-mod-installer-cloud/main/manifests/faded-realms.json
```

That catalog must match the live Faded Realms dedicated-server `Mods=` pack
exactly. New mods stay on Main unless Luis enables them on that server. As of
2026-09-24 the Season 3 pack is 69 mods after Solar Shadows removal. `scripts/validate_manifests.py` rejects extras
or missing ids.

B47ANCE uses:

```text
https://raw.githubusercontent.com/FadedMods/faded-mod-installer-cloud/main/manifests/b47ance.json
```

The URL remains stable when mods are updated. Players click **Refresh Mod
List** in the installer after a publication. Installer `0.3.2` shows B47ANCE
as a built-in modder list.

## Current release state

The current installer is **0.3.6** (September 25, 2026), with the new World Forge
page and verified Windows, Linux, Steam Deck and macOS packages:

<https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.3.6>

[World Forge and installer release verification](docs/RELEASE_LEDGER_2026-09-25_WORLDFORGE.md).

The complete August 28 manifest commit and mod-release sequence is recorded in
[`docs/RELEASE_LEDGER_2026-08-28.md`](docs/RELEASE_LEDGER_2026-08-28.md).

## Legal Notice

Access to this repository, release assets, manifests, and related FadedMods materials is subject to the repository legal notice:

[DISCLAIMER.md](DISCLAIMER.md)
