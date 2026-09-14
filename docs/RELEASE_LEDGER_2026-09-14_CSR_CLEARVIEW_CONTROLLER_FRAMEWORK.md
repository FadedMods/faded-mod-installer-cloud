# CSR/ClearView Controller Framework 1.2.0 release ledger

- Published: 2026-09-14
- Release: `mod-assets-2026-09-14-csr-clearview-controller-framework`
- Main manifest entry: `CSRClearViewController` (new)
- Faded Realms manifest: unchanged. The new id is not in the live server
  `Mods=` pack, so it stays out of `manifests/faded-realms.json`.

## Content change

Faded controller framework for Project Zomboid Build 42.20:

- Injects button prompts, Faded glyphs, focus rings, and pad navigation onto CSR
  object panels, ClearView UI, and other windows.
- Semantic bindings follow the player's own remap.
- Client UI only and add/remove safe; intended to load first.

## Immutable assets

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `CSRClearViewController-v1.2.0.zip` | 5,144,308 | `15bc03e593a20b512eb1322d263ab68704eab6dc9353f9e7af07769c85b87fe2` |

Single-part ZIP, well under the 1800 MB split limit. GitHub's own upload digest
matches the local SHA-256 value above.

## Package validation

- Staged source: `E:\fadedmodsstaging\CSRClearViewController`.
- Packaged with `scripts/package_local_mods.py`; the root-level duplicate
  `mod.info` is excluded, leaving exactly one Build 42 `mod.info`.
- Archive: 82 entries, single top-level root `CSRClearViewController`, and
  `CSRClearViewController/42/mod.info`.
- `modversion=1.2.0` and `versionMin=42.20.0` verified from the staged
  `mod.info`.
- Forward-slash entry names only; `validate_portable_zip_headers` passed and
  every payload CRC verified.
- `app.installer.prepare_mod_zip` reconstructs the archive as the expected mod
  folder name `CSRClearViewController`.

## Catalog shape

Main gains one entry while `id` and `server_mod_id` stay `CSRClearViewController`.
`scripts/validate_manifests.py` passes. No Faded Realms catalog change was made.

## Local deployment

No local mod install, installer rebuild, or server deployment was part of this
release. In-game runtime acceptance was not performed during this release
operation.
