# Faded Realms catalog restored to the live 79-mod pack

Published 2026-09-07. No release assets changed.

## Defect

`manifests/faded-realms.json` had grown to 82 entries. The live Faded Realms
dedicated server `Mods=` line is 79 ids. A read-only SFTP check of
`/server/Zomboid/Server/servertest.ini` confirmed every enabled id was already
in the catalog, plus three extras that were never enabled:

- `tsarslib` 3.30, leftover from the reversed PFC 2.1.10 TsarLib dependency
- `KnoxPhasmophobia` 0.1.0, published to both catalogs on 2026-09-03
- `CATConstruction` 0.2.0, published to both catalogs on 2026-09-05

Those three remain on Main. They are not on the live Faded Realms pack.

## Repair

Removed the three extras from `manifests/faded-realms.json` only. The catalog
id set now matches the live `Mods=` pack exactly (79).

`scripts/validate_manifests.py` now enforces `FADED_REALMS_LIVE_MOD_IDS`.
Future catalog-only extras fail CI. If Luis adds a mod to the live server pack,
update that allowlist in the same commit as the catalog entry.
