# FED outline and companion repair - 2026-09-25

Release: https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-25-fed-outline-companion-repair

| ID | Version | ZIP bytes | SHA-256 |
|---|---|---:|---|
| BackToAtlanta_UI | 1.0.2 | 70853751 | d02d3cb16f1093e6c4d567cee54b6e440b51febe52569995880dedbc6bda0edd |
| MyOnlyFriend | 2.3.7 | 160051225 | 93a64eda78391db0fd8e3cff2c701fe4d17d4ab76a68ae31020e1e593e22c631 |

The FED 0.3.1 report captured 9,578 occurrences in seven groups on a
B42.20.4 multiplayer client. Back to Atlanta passed a packed ABGR integer to
the ColorInfo-only two-argument outline setter. The installed engine/Kahlua
reproducer rejected that overload, then failed a subsequent nested Java/Lua
call with the report's exact ReturnValues.put / callFrame NullPointerException.
This explains the companion Kill and later hotbar/timed-action stack patterns;
the names in those later stacks do not independently establish defects in CSR
or Arsenal. The report's embedded catalog versions were stale: both live
catalogs already had CSR Test 2.0.6, Arsenal 1.6.2 and Character Creator 2.6.2.

UI 1.0.2 restores owned colors using ColorInfo:setABGR and releases an outline
on death even when combat text is disabled. Its independent Java plugin remains
1.0.0. The main Back to Atlanta content/map package is unchanged.

My Only Friend's server brain was executing on the multiplayer client and
calling Kill directly. Installed IsoZombie.onKilled bytecode skips normal
DoZombieInventory when GameClient.client is true. All fifteen server modules
now return before registration on clients, preserving dedicated/SP authority
and existing client command/visual transport. Lethal protection and high-damage
special bites use native Kill, and dead targets are ignored. Its independent
Java plugin remains the byte-identical 2.3.2 binary.

Validation before publication:

- Native engine/Kahlua: 1,000 outline acquire/release cycles, engine resets,
  foreign ownership, unload, death with text disabled, signed ABGR round trips,
  and 1,000 subsequent nested callbacks pass; no duplicate argument-pool entries.
- Companion authority fixture: 19 checks in Lua and installed Kahlua. All seven
  existing movement, ecology, spawning, definitions, roster/training and map
  retirement suites pass.
- Character Creator's complete validator and bounded loot/population test pass.
  Its corpse/render hooks inspected here do not remove inventory. No creator
  change or version bump is justified by this report.
- CSR hotbar recovery, backpack slots, equipment refresh/combat and outline
  suites pass: 18 + 7 + 5 + 31 + 83 assertions. CSR source is unchanged.
- TWD validator: zero errors, eight pre-existing unrelated pcall warnings.
- Exact staging hashes, portable ZIP layout/CRC, one mod.info per archive,
  installer preparation, and Java declaration validation pass. GitHub asset
  sizes/digests match. Compared with the previous local installs, UI changes
  two files and MOF changes eighteen; no additions or removals.
- Main remains 123 entries and Faded Realms 69, in the same order. Only these
  two existing entries change in both catalogs; loader metadata is preserved.

The game must restart fully to clear an already-corrupted Kahlua session.
Existing stripped corpses are not reconstructed. Joined multiplayer corpse,
loot and visual acceptance remains pending; automated checks are not gameplay
confirmation. No remote server deployment/restart is part of this release;
OVH and Outback remain untouched. CSR Main stays out of the personal install.

## Public download and local installation

Completed at 2026-09-25 11:19:08 UTC. Both assets were freshly downloaded via
the installer using catalog commit `6c20632b62e53995dd395bb0278c4fe4df243172`
while the stable raw URL cache refreshed. SHA-256, preparation and every
installed file/directory match the public packages. The previous installs were
hash-verified and retained outside the game's scan root. All 69 playable mod
folders remain; CSR Main is absent. Both publication workflows succeeded.

Local receipts: `E:/tmp/faded-fed-repair-20260925/completed.json`,
`public-local-receipts.json`, `packages.json`, and `REPAIR_REPORT.md`.
