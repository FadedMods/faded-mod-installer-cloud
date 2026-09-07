# CAT Construction 0.2.0 duplicate `mod.info` repack

Packaging repair published 2026-09-07. No mod ID, mod version, or file content
changed.

## Defect

The 2026-09-05 asset shipped two byte-identical `mod.info` files:

```text
CATConstruction/mod.info
CATConstruction/42/mod.info
```

`app.installer.find_single_mod_folder` rejects any archive containing more than
one `mod.info`, so every install attempt failed for every user on every
platform, on both the local-install and the server-upload path:

```text
ModValidationError: Multiple mod.info files were found: CATConstruction, CATConstruction\42
```

A scan of all 112 catalog entries confirmed CAT Construction was the only mod
carrying this defect. No other archive has duplicate or missing `mod.info`, and
none has multiple top-level directories.

## Repair

Only `CATConstruction/mod.info` was removed. The root `icon.png` and
`poster.png` were left in place; they are exact duplicates of the copies under
`42/`, and the `42/` tree is self-contained because `42/mod.info` resolves
`poster=poster.png` and `icon=icon.png` next to itself.

All 110 retained entries were compared against the superseded archive
entry-by-entry: every CRC-32 and uncompressed size matches. Entry names use
forward slashes, there are no absolute or traversal paths, `testzip()` passes,
and the archive has exactly one top-level `CATConstruction/` directory and
exactly one `CATConstruction/42/mod.info`.

## Release

- Tag: `mod-assets-2026-09-07-cat-construction-0.2.0-single-modinfo`
- Asset: `CATConstruction-v0.2.0.zip`
- Version: `0.2.0` (unchanged)
- Target: Project Zomboid `42.20.4`
- Compressed bytes: `129501290`
- Installed bytes: `215514173` across 90 files
- Required free bytes: `881886375`
- SHA-256: `ed8e2ffb0d0b5f20dba7bdb603bba4599f129408b424b0d1431987d34ac37de2`
- Superseded SHA-256: `19cccaa4814bd648d735844d93f85b9194b5d3f059527e3f01830a6dc898adfd`

The version stays `0.2.0` because the payload is unchanged and installation was
impossible before this release, so no user can hold an older `0.2.0` tree. This
follows the 2026-08-30 portable-ZIP repair precedent, which likewise repacked
without touching mod versions.

## Verification

The public asset was downloaded after publication and is byte-identical to the
verified local repack. It then prepared through `app.installer.prepare_mod_zip`
as `CATConstruction`, passed `validate_prepared_mod`, and installed to a scratch
mods root as `CATConstruction/42/mod.info` with 90 files.

The superseded SHA-256 is quarantined in `scripts/validate_manifests.py` under
`DUPLICATE_MOD_INFO_SHA256S` so it cannot be reintroduced.

Both `manifest.json` and `manifests/faded-realms.json` were changed surgically:
`updated_at`, `uncompressed_size_bytes`, `required_free_bytes`, `download_url`,
`size_bytes`, and `sha256`. No mod IDs, ordering, or unrelated catalog entries
changed.

## Not addressed here

Two installer-side issues found during the investigation remain open and are
deliberately out of scope for this hotfix:

1. `find_single_mod_folder` hard-fails on a legal Build 42 layout that carries
   both a root and a versioned `mod.info`. The scoring in
   `scripts/generate_b42_tracker.py` (`mod_info_score` / `choose_mod_info`)
   already resolves this correctly and should be reused.
2. `prepare_mod_zip` leaks its extraction directory when validation fails after
   extraction, and the UI holds every downloaded ZIP and extracted tree for the
   whole install queue. A failed CAT install leaked 215 MB of staging.
