# The Young Died Too 1.1.0 release ledger

- Published: 2026-09-07
- Release tag: `mod-assets-2026-09-07-the-young-died-too-1.1.0`
- Asset: `TheYoungDiedToo-v1.1.0.zip`
- Size: `24874714` bytes
- SHA-256: `f18f14b65ef23aa5f03acd40d1f0c2e34cfef14efa9760073964f79cac65072d`
- Prepared payload: 438 files / 28,472,302 bytes
- Required free bytes: `590217928`

## Source

Staged at `E:\Faded Mod Staging\TheYoungDiedToo` with runtime ZIP
`TheYoungDiedToo-v1.1.0.zip`. That staged archive contained three `mod.info`
files (`TheYoungDiedToo/mod.info`, `common/mod.info`, and `42/mod.info`).
`find_single_mod_folder` would reject it.

The hosted artifact was rebuilt through `scripts/package_local_mods.py` so the
published ZIP has one top-level `TheYoungDiedToo/` folder and one
`42/mod.info`. The art-source ZIP was preserved locally and not published.

## Catalog

Both `manifest.json` and `manifests/faded-realms.json` were updated. The Young
Died Too is in the live Faded Realms 79-mod pack, so both catalogs stay in
sync. No other catalog ids changed.
