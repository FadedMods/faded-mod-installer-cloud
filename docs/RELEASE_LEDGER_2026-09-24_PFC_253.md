# Project Faded Car 2.5.3

The September 24 join failure named `ProjectFadedCar.WorkshopCarLift` as a
missing client dictionary script. A leading UTF-8 BOM made B42.20.4 parse the
module keyword incorrectly. Removing exactly three bytes restores the entity;
its ID, recipe, dedicated sprites, callbacks and lift behavior are preserved.
The optional Carrier Core JAR stays byte-identical at 2.5.0. No save reset.

- Release: https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-24-project-faded-car-2.5.3
- Manifest commit: `15e30a6`.
- ID: `ProjectFadedCar`; version: `2.5.3`.
- ZIP: `ProjectFadedCar-v2.5.3.zip`; 225,180,620 bytes; 4,636 files.
- SHA-256: `371ba2fc26eb136621029f914d440ae424d9d1cbacbbd1a2a7c04c0bc76fc53d`.
- Main remains 123 entries; Season 3 Faded Realms remains 70, matching Mods=.
- Both canonical raw manifests verified at 2.5.3. The public download passes
  installer preparation and exact source/public/local file-hash comparison.
- Local backup: `ProjectFadedCar_20260924_125228` under installer app-data backups.
- Hosted lift script and mod.info backed up under
  `/server/Zomboid/mod-backups/ProjectFadedCar-2.5.2-before-join-fix-20260924`,
  replaced and read back successfully. No Java files or saved-world files changed.

Validation: 35 repository checks pass, including 89 Python tests, 30 Lua
suites and 290 Lua parses. Installed B42.20.4 parser reproduces the original
failure; the fixed mod starts a native dedicated server alongside ModernEVs
with both lift and charging-station definitions loaded. Native visual lift
test and six Bullet raise/hold/lower cycles pass. All 1,283 SpriteConfigs
marked loaded in the hosted dictionary have matching entity declarations
across vanilla and the enabled 70-mod client pack after the fix.

At publication, hosted restart and successful player join remain pending.
Echoes must update from hosted 0.14.0 to published/local 0.15.0 at restart.
The server's enabled pre-boot updater uses the unchanged Main manifest URL.
Players use Refresh Mod List; an installer executable update is unnecessary.
