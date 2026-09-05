# PFC 2.3.2 and What A World 1.2.1

Published on 2026-09-05 to both `manifest.json` and
`manifests/faded-realms.json`.

## Project Faded Car 2.3.2

- Release: `mod-assets-2026-09-05-pfc-2.3.2-anim-parent-repair`
- Asset: `ProjectFadedCar-v2.3.2.zip`
- Size: 93,289,921 bytes
- SHA-256: `fab7bcd98bf6d943a4cf7fe51c5618c051c6ee90b2837fef9a3d49d47348462d`
- Payload: 1,069 files
- Repair: all local vehicle-aim animation children reference the PFC-prefixed
  parent XML files that ship in the same directory.

## What A World 1.2.1

- Release: `mod-assets-2026-09-05-what-a-world-1.2.1-portable`
- Asset: `WhatAWorld-v1.2.1.zip`
- Size: 33,523,579 bytes
- SHA-256: `b8cb90de9c4113ce4a077636838ffd553048c150554d832c3f8c890ba382ab74`
- Payload: 250 files
- Repair: `AcidIrritationShiver.xml` is a complete self-contained node and no
  longer inherits a vanilla XML file across the mod filesystem boundary.
- Portable package: exactly one `WhatAWorld/42/mod.info`.

The earlier same-day release tag
`mod-assets-2026-09-05-what-a-world-1.2.1-anim-self-contained` contained both
the authoring-root and Build 42 `mod.info` files. The real installer rejected
that archive before changing the installed mod. It is superseded and is not
referenced by either manifest.

Manifest commit `1ad3405e876edb2c2ae549c274a860daaaec0a74` is the first
commit that points both catalogs at the final portable assets. Manifest safety
validation and installer parsing passed. The exact public payloads were then
installed into the local playable tree, with zero missing, extra, or changed
files across all 1,319 files.
