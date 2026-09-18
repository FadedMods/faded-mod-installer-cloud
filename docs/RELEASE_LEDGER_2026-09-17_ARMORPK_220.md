# Faded's Armor Pack 2.2.0 release ledger

- Published: 2026-09-17
- Release: `mod-assets-2026-09-17-armorpk-2.2.0`
- Main manifest: `ArmorPK` (multipart, 2 parts) `2.1.0` -> `2.2.0`
- Faded Realms manifest: `ArmorPK` (same two parts)
- Supersedes the 2.1.0 package published on
  `mod-assets-2026-08-17-four-mod-update`.

## Content change

- Imported the source webbing rework. The 22 ArmorPK magazine and shotgun chest
  rigs (`Bag_X_Vest`, `Bag_SKS_Vest`, `Bag_AK_Vest`, `Bag_D3M`, `Bag_Blackhawk`,
  `Rig_Smersh`, `Rig_Smersh_A/B/C`, `D3CR`, `Shotgun_Rig` and their `_Loose`
  states) provide `WebbingLeft`/`WebbingRight` attachment slots for a knife or
  walkie-talkie, with vanilla `Tooltip_Webbing` / `Tooltip_AmmoStrap_Shotgun`
  text.
- Added `42/media/lua/shared/ArmorPK_Reload.lua`: a namespaced, idempotent,
  chain-preserving wrapper of `ISReloadWeaponAction.setReloadSpeed` that grants
  the vanilla 15% magazine/shell bonus only while a worn allow-listed ArmorPK rig
  actually contains a compatible magazine or shells. Racking speed is never
  altered and the bonus never stacks on vanilla ammo straps or webbing.
- The six `Glove_*` items now carry static hand protection
  (Scratch/Bite): `Glove_3M` 10/5, `Glove_Fisher` 15/5, `Glove_Mechanix` 20/10,
  `Glove_Mechanix_Pact` 25/10, `Glove_Leather` 30/15, `Glove_Mustang` 30/15.
  `hands` was added to the generated defensive outfit pools, so coverage is now
  447/447 defensive items.
- Removed 36 shadowed duplicate item parameters (repeated
  `WaterResistance`/`Weight`/`RunSpeedModifier`/`BloodLocation`/`ScratchDefense`
  lines) across six clothing scripts. The retained value is the one the engine
  already used, so there is no gameplay change.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `ArmorPK-v2.2.0-part1.zip` | 1,764,957,016 | `ff457b85c899b90020b870c659174d49094da7d7713868ac59c0c3b8c9c0587d` |
| `ArmorPK-v2.2.0-part2.zip` | 1,485,343,707 | `9ed643aa5f41054888ae938348cb0c1927777ecc0250e30b027fbb572243dffa` |

Uncompressed package: 3,373,198,050 bytes; `required_free_bytes` 7,160,369,685.
Each part is below GitHub's per-asset limit.

## Package validation

- Staged source: `E:\FadedModsStaging\ArmorPK`; release working root
  `E:\FadedModsStaging\release-20260917-armorpk-2.2.0`.
- Packaged with `scripts/package_local_mods.py` (installer `.venv` Python).
- Exactly one `ArmorPK/42/mod.info` (`version=2.2.0`), no root duplicate;
  `mod.info` is entry 0 of part1; 5,637 archive entries (5,570 files + dirs).
- ArmorPK release gate `reports/ArmorPK_RELEASE_GATE.json`: **PASS**, 0
  problems, 5,569-file `42` tree SHA-256
  `5f4302447d24f7f474ec9283f9457cf302480585f455452bc83a8e5d68f75b21`, and the
  synced physical package matched the source with no missing/extra/mismatched
  files.
- Public live verification: downloaded both public assets, SHA-256 matched, and
  `prepare_mod_zip_parts` produced `ArmorPK` with `42/mod.info` at 2.2.0. The
  public payload is byte-identical to staging (5,570/5,570 files, 0 mismatches).
  GitHub release asset digests match the local SHA-256 values exactly.

## Catalog shape

Main manifest 119 entries and Faded Realms 79 entries; only the `ArmorPK` entry
changed in each, order preserved. `scripts/validate_manifests.py` passed.
Manifest commit `ea518b6 Update Faded's Armor Pack to 2.2.0`.

## Local deployment

Exact public payload installed with `install_prepared_mod` (`BACKUP_REPLACE`) to
`E:\PZ User Data\Zomboid\mods\ArmorPK`: 5,570/5,570 files byte-identical to the
public ZIP, `version=2.2.0`. Previous 2.1.0 backup:
`%APPDATA%\FadedLocalModInstaller\backups\ArmorPK_20260917_213615`.

## Dedicated server deployment

`faded-pz-vps` (`The Faded Realms`, B42.20.4):

- Public assets downloaded on the host; SHA-256 matched both parts.
- Target: `/home/pzserver/Zomboid/mods/ArmorPK`, 5,570 files, `version=2.2.0`,
  `pzserver:pzserver`.
- Backup: `/home/ubuntu/ArmorPK-before-2.2.0-20260918T013700` (2.1.0).
- `project-zomboid.service` stopped, tree swapped, started; reached
  `*** SERVER STARTED ****` at 01:40:36 UTC. ArmorPK is present in the activated
  mod list (`count=80`), with no ArmorPK Lua or script errors.
- Pre-existing and unchanged by this release: the four
  `media/AnimSets` / `media/actiongroups` `NoSuchFileException` traces and the
  FJL `WORLD_PACK_SYNC_UNVERSIONED_MOD_CHANGED` retry warning are identical on
  the prior 2.1.0 boot. Neither is a regression from 2.2.0.
