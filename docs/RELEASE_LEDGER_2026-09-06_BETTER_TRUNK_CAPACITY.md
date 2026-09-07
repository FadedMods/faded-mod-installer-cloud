# Better Trunk Capacity 1.0.0 release ledger

- Published: 2026-09-06 (America/New_York)
- Release tag: `mod-assets-2026-09-06-better-trunk-capacity-1.0.0`
- Asset: `BetterTrunkCapacity-v1.0.0.zip`
- Size: `4927803` bytes
- SHA-256: `c79ab9c787697c2c3b157202c6156a4f303b5e16804bf68624d4f618bd81d4de`
- Prepared payload: 8 files / 4,926,344 bytes
- Java plugin: `faded.bettertrunkcapacity` 1.0.0 (`BOTH`, `HYBRID`)
- Runtime JAR SHA-256: `ca69aff7dda15d62d102598da84842bf45effa51b14e98fb9ea6207aa564f105`

## Validation

- All staged SHA-256 checks passed and a fresh Gradle package/check rebuild produced the identical runtime JAR.
- Capacity policy reported 120 checks and the ClearView restoration guard reported 16 checks.
- Supplied FJL CLIENT/SERVER cargo suites reported 203 checks each; CLIENT/SERVER native sandbox suites reported 3,944 checks each.
- ZIP CRC, forward-slash paths, traversal checks, one-root layout, one authoritative `42/mod.info`, and production-installer preparation passed.
- No executable Lua is shipped; the only Lua-tree payload is the translation dictionary.

The supplied outer `BetterTrunkCapacity-1.0.0.zip` is a developer handoff bundle containing source, documentation, and four metadata files. It was preserved but was not published. The hosted artifact was rebuilt from `Contents/mods` through the production packager.

The release is added to the main installer catalog only. It is not added to the Faded Realms manifest or Federated Server's authoritative 79-mod pack without a separate owner instruction.

Remaining manual scope: a played single-player session, a connected multiplayer session, rendered Sandbox-menu inspection, and full-modpack occupied-seat/inventory-grid checks.
