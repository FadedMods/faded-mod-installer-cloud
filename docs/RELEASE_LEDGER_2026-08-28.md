# August 28, 2026 publication ledger

This ledger records the immutable release sequence published through the Faded
Local Mod Installer manifests on August 28, 2026.

## Catalog state

- Main: 99 entries in `manifest.json`.
- Faded Realms: 75 entries in `manifests/faded-realms.json`.
- Manifest head before this documentation-only follow-up: `204cf88`.
- Every August 28 `Validate manifests` workflow completed successfully.

## Installer

Faded Local Mod Installer `0.2.16` repaired optional hybrid-Java declarations,
failed-refresh catalog retention, and uninstall-to-reinstall navigation. The
release contains Windows, Linux x86_64, macOS arm64, and macOS x86_64 packages:

<https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.2.16>

## Current highlighted entries

| Mod ID | Version | Release tag |
|---|---:|---|
| `BuildcraftReborn` | 0.5.16 | `mod-assets-2026-08-28-buildcraft-0.5.16-standalone` |
| `CharacterCreator` | 2.1.4 | `mod-assets-2026-08-28-character-creator-2.1.4` |
| `CommonSenseReborn` | 1.9.57 | `mod-assets-2026-08-28-csr-1.9.57-animnode-flatten-repair` |
| `CommonSenseRebornTest` | 1.9.57 | `mod-assets-2026-08-28-csr-1.9.57-animnode-flatten-repair` |
| `FadedJavaLoaderBridge` | 0.3.8 | `mod-assets-2026-08-28-stack-command-bridge` |
| `FadedsClearViewUI` | 0.6.10 | `mod-assets-2026-08-28-clearview-0.6.10` |
| `FaithsTraditions` | 1.1.2 | `mod-assets-2026-08-28-stack-command-bridge` |
| `ItsATrap` | 2.0.1 | `mod-assets-2026-08-28-stack-command-bridge` |
| `KnoxReborn` | 0.3.15 | `mod-assets-2026-08-28-knox-reborn-0.3.15` |
| `MassiveKI5Pack` | 1.2.10 | `mod-assets-2026-08-28-mkp-trunk-ui` |
| `ProjectFadedCar` | 2.1.3 | `mod-assets-2026-08-28-pfc-2.1.3-portable` |
| `WaterExpanded` | 2.4.7 | `mod-assets-2026-08-28-stack-command-bridge` |

## Publication commits

| Commit | Publication |
|---|---|
| `b615ff2` | CSR 1.9.54 and Knox Reborn 0.3.14 |
| `f01dfc1` | ClearView UI 0.6.10 portable package |
| `c38ae88` | CSR 1.9.55, Knox Reborn 0.3.15, FJL Bridge 0.3.7 |
| `63e63a3` | Project Faded Car 2.1.3 portable archive |
| `0ebaa61` | CSR 1.9.56 AnimNode repair |
| `df0f107` | CSR 1.9.57 flattened AnimNode repair |
| `711d41e` | Optional FadedStack command bridge migration |
| `c6870a7` | Faded Java Loader Bridge 0.3.8 metadata correction |
| `fc18ff9` | Faiths 1.1.2 animator guard correction |
| `5546213` | Standalone optional-Java manifest compatibility |
| `f66b912` | Legacy-incompatible optional-Java metadata rejection |
| `ed2b497` | Installer 0.2.16 update catalog |
| `9d24c3f` | Buildcraft Reborn 0.5.16 |
| `b97d4da` | Massive KI5 Pack 1.2.9 |
| `bd6c060` | Massive KI5 Pack 1.2.10 asset |
| `204cf88` | Character Creator 2.1.4 |

The final two gameplay updates are intentionally linear: `bd6c060` is the
direct parent of `204cf88`. The Character Creator publication did not overwrite
or interrupt MKP. Both manifests still point to `MassiveKI5Pack-v1.2.10.zip`
(326,277,603 bytes, SHA-256
`7742bef3aae01f7ae7986091523727b10a79b0d4fb69e98d8722c6cad1fd7157`).

## Release outcomes

- CSR `1.9.57` contains the `1.9.54` licensed integrations, `1.9.55` runtime
  repairs, and inheritance-free roleplay AnimNodes for Linux dedicated-server
  safety.
- ClearView `0.6.10` preserves validated `0.6.9` behavior and repairs portable
  ZIP entry separators.
- Knox Reborn `0.3.15` completes 53 map-label keys and repairs population grids
  for all 18 authored Grapeseed areas without changing geometry or loot.
- PFC `2.1.3` preserves `2.1.2` gameplay in a portable archive; the known-bad
  `2.1.0` WorldDictionary payload remains quarantined.
- Buildcraft `0.5.16` restores native module-qualified entity loading without
  requiring FJL while retaining its optional hybrid accelerator.
- MKP `1.2.10` replaces the placeholder `TruckBed` loot presentation with the
  authored container, capacity, and icon.
- Character Creator `2.1.4` saves and restores occupation, traits, identity,
  appearance, and wardrobe as one complete preset while preserving one-sided
  legacy records.
- The FadedStack migration is optional. Participating mods retain their direct
  Project Zomboid event fallbacks when FJL/bridge capabilities are absent.
