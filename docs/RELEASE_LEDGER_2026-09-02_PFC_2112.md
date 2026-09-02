# Project Faded Car 2.1.12 Release Ledger

Published 2026-09-02 for Project Zomboid 42.20.4.

## Artifact

- Release: `mod-assets-2026-09-02-pfc-2.1.12-fleet-sandbox-startup`
- Asset: `ProjectFadedCar-v2.1.12.zip`
- Compressed size: `75,444,368` bytes
- Uncompressed size: `92,425,355` bytes
- Required free space: `704,740,635` bytes
- SHA-256: `09a5c9528e7359c41f48663c331050d4b78491d72f125756953a0e028e07210c`
- ZIP entries: `610`, all forward-slash paths
- Build manifests: exactly one, `ProjectFadedCar/42/mod.info`

## Repair

FED reported four PFC 2.1.10 multiplayer initialization errors caused by the
old imported spawn callbacks indexing `SandboxVars.PFC` before that legacy
table existed. Version 2.1.11 removed those legacy files. Version 2.1.12 also
hardens their PFC-namespaced replacements with a guarded accessor, preserves
the declared spawn defaults during initialization, and adds regression coverage
for missing and malformed sandbox values.

## Verification

- 44 Python contracts and 12 Lua gameplay smokes passed.
- All 162 shipped Lua files parsed.
- Script registry and translation gates passed.
- Exact B42.20.4 dedicated boots passed standalone, with FJL, and with an
  independently installed TsarLib; all had zero PFC diagnostics.
- A two-stage same-save 2.0.9 to 2.1.12 test with Into the River preserved
  `IntoTheRiver.TransportFreezer` registry ID `2114` and created no
  `WD_ERROR` folder.
- Source, staged tree, and playable local tree are exact 610-file mirrors.
- The public asset was downloaded through the live main manifest, hash checked,
  and prepared as `ProjectFadedCar` by installer 0.3.1.

## Commits

- PFC gameplay: `dbe466a`
- Main and Faded Realms manifests: `e7d678f`
