# Common Sense Reborn 2.0.2 release ledger

- Published: 2026-09-13
- Release: `mod-assets-2026-09-13-csr-2.0.2-medical-names-sandbox`
- Main manifest entries: `CommonSenseReborn`, `CommonSenseRebornTest`
- Faded Realms manifest: `CommonSenseRebornTest` only (the production identity is
  not in its live server pack). No IDs were added or removed in either catalog.

## Content change

Version 2.0.2 medical, item-name, sandbox, and circle-bar repairs for Build
42.20.4:

- Health-panel medical actions (replace bandage, staple, massage, soak rag,
  antibodies, make bandage) now sit on the native context root. A single
  applicable item runs on the first click; a type picker appears only when more
  than one bandage or disinfectant is available.
- Carry Visible Items no longer redefines vanilla item scripts, so named
  magazines, unique titles and third-party prefixes stay intact. Held models are
  applied in Lua. New sandbox `EnableCarryVisibleItems` (default ON, restart to
  apply).
- Expanded moodle titles and descriptions use CSR-prefixed translation keys and
  can be turned off with `EnableExpandedMoodleDescriptions` (default ON, live).
- Circle status bars draw a dim full track, a distinct filling arc, and
  25/50/75/100 ticks.
- Main is 727 sandbox options; Test is 754.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `CommonSenseReborn-v2.0.2.zip` | 64,373,958 | `1496bbaf7ec001cab85caa5c0af4d7c932b52661af6389d595e924a71c37413e` |
| `CommonSenseRebornTest-v2.0.2.zip` | 65,859,200 | `065745ea7792bedc63d413be1416740710fd0997b468a233627aefe170fc9883` |

Both are single-part ZIPs (well under the 1800 MB split limit). GitHub's own
upload digests match the local SHA-256 values above.

## Package validation

- ZIP central directories, portable local headers, and payload CRCs passed
  `scripts/package_local_mods.validate_portable_zip_headers`.
- Archive paths use forward slashes and the intended top-level mod roots
  (`CommonSenseReborn`, `CommonSenseRebornTest`); the root-level duplicate
  `mod.info` is excluded, leaving exactly one Build 42 `mod.info` per archive.
- Main archive: 2,977 files and `CommonSenseReborn/42/mod.info`.
- Test archive: 3,029 files and `CommonSenseRebornTest/42/mod.info`.
- Both `modversion=2.0.2` and `versionMin=42.20.4` are verified.
- `app.installer.prepare_mod_zip` reconstructs each archive as the expected mod
  folder name.

## Catalog shape

Main keeps both CSR identities; Faded Realms keeps only its existing Test
identity. Existing names, IDs, `server_mod_id`, optional-Faded-Java-Loader
behavior (`requiresJavaLoader: false`), and descriptions are preserved apart
from the version-specific notes, download metadata, storage requirements, and
`updated_at: 2026-09-13`. `scripts/validate_manifests.py` passes.

## Local deployment

The approved local Test install was replaced from the staged 2.0.2 tree:

- `E:\PZ User Data\Zomboid\mods\CommonSenseRebornTest` (reached through the
  existing `C:\Users\Luis\Zomboid` -> `E:\PZ User Data\Zomboid` junction)
- 3,029 files copied; missing/extra/mismatched = 0/0/0; `modversion=2.0.2`
  confirmed.
- Previous install recoverably moved to
  `E:\Faded Mod Staging\backups\CommonSenseRebornTest-before-2.0.2-20260913-164338`.

The Test-only root-level duplicate `mod.info` was excluded to mirror the
published package. No installer application rebuild or server deployment was
part of this mod release. In-game runtime acceptance was not performed during
this release operation.
