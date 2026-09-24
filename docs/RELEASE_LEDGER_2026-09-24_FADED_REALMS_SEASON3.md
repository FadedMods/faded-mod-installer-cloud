# Faded Realms Season 3 catalog - 2026-09-24

The existing Faded Realms URL now serves the active Season 3 server pack. No installer rebuild, version bump, app-update catalog change, or new player URL is required. Existing installer code fetches this hosted catalog each refresh with no-cache request headers; temporary GitHub CDN propagation is external to the installer.

The server Mods= line was read again after the owner's restart. The catalog contains exactly its 70 IDs, in server load order, using the already-published Main release entries. Main remains unchanged. The manifest app_name is Faded Realms - Season 3; the installer's built-in selector remains Faded Realms.

The previous catalog had 79 entries. Added 11 active server entries and removed 20 inactive entries from this catalog only. Refreshing the list does not uninstall old mods from players' disks; the server selects the enabled mods when joining.

## Added

- BackToAtlanta
- BackToAtlanta_UI
- CATConstruction
- ChocoboGo
- Deadflow
- FadedDepths
- ModernEVs
- SentryNet
- VehiclesByFaded
- WhatAWorldSolarShadows
- groundWorks

## Removed from this catalog

- ChadedMilitaryConvoy
- FadedAfflictions
- FadedCombatText
- FadedFromTheWindow_ZCTW
- FadedNinja
- FadedTrenchCoats
- FadedsLastChance
- FadedsLegacyCodex
- FaithsTraditions
- IntoTheRiver
- JustFaded
- KnoxReborn
- KnoxTransit
- MassiveKI5Pack
- MassiveVehiclePack
- Military_Tool_Kit
- SaveTheBabies
- SimpleOverhaulTraitsAndOccupations
- TheLastTestament
- WhimsyWeapons

## Checks

- Catalog ID order and set equal the live server Mods= line.
- Every entry exactly equals its published Main entry.
- Existing installer parse_manifest_catalog accepts all 70 entries without code changes.
- Updated the server-pack allowlist; replaced the obsolete shared MassiveKI5Pack requirement with ItsATrap (MassiveKI5Pack is no longer enabled on the server).
- Manifest safety checks passed; public raw propagation verification is recorded after push.

## Related crash repair

ItsATrap 2.1.1 used invalid tiledef IDs 8190-8192, above the engine maximum 8189. The server rejected the mod, and the client failed with missing SpriteConfig ItsATrap.MetalChevalDeFrise. Source and installed metadata were repaired as 2.1.2 using free IDs 8111-8113, published in manifest commit 5e3f4f9. Asset: ItsATrap-v2.1.2.zip, 45,939,592 bytes, SHA-256 856866b0549fb948a505fef8e1a0aa432214f7e7f33b87b5665a9142cd34a3a4.

Both source release gates and a real isolated B42.20.4 server startup passed. Public/local/staging hashes matched all 1096 files. After the owner's restart, the actual hosted server's 2026-09-24_16-00 boot loads ItsATrap, finishes WorldDictionary.init, and reaches SERVER STARTED. It no longer reports invalid IAT tiledef IDs or missing ItsATrap. Successful player rejoin has not yet been observed. Other pre-existing animation warnings remain outside this join repair.

Players select Faded Realms and click Refresh Mod List, install/update the selected pack, then fully restart Project Zomboid before joining.
