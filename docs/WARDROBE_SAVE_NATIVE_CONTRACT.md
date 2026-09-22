# Echoes 0.13.2 wardrobe, persistence and encounter corrections

Campaign API 3 and community extension 1 remain unchanged. No FFO action is required.

## Multiplayer appearance

`EchoesOfHumanityNpc/Snapshot` adds `wornVisuals`, an ordered table aligned one-to-one with `wornItems`. Each element is an empty string or a bounded Base64 native `ItemVisual.save` record using the running PZ world version. Empty records preserve their slot. The server initializes lazy clothing choices and caches each item's record for two seconds. These records carry tint, texture choices, decals, blood/dirt/holes/patches. Clients validate the item type before applying a record and leave the prior visual intact on malformed input.

Worn clothes and attached weapons have separate change tracking. Holstering, drawing, switching sidearms and changing weapon attachments no longer rebuild clothing. Worn records overwrite the random starter outfit. Clothing visual changes update the existing item rather than creating a replacement. Reconnects receive the server's actual chosen appearance.

## NPC saved strings

PZ 42.20.4's `GameWindow.StringUTF` saves a signed-short UTF-8 length. Its writer allows a longer value, but its reader cannot consume that value correctly. A native table containing an NPC-like 50,005-character string reproduces the reported `invalid lua table type 69` exactly.

The manager now packs oversized string values in `NpcPersistenceService.TABLE_NAME` immediately after every save, including the save exception cleanup path. Values over 30,000 UTF-8 bytes become a table with boolean `EOH.StringChunks.v1` and contiguous numeric string entries. Chunks contain at most 7,000 UTF-16 units and do not split a surrogate pair. Every native string remains below the signed-short limit.

Before the existing persistence reader runs, the manager restores those strings in memory. A `finally` block repacks the stored table. The native actor state, identities, inventory, health and other persistence fields are retained byte-for-byte. Existing small-string saves still load. New chunked saves require Echoes 0.13.2 or newer; preserve the pre-update backup if rolling back.

This is prevention for healthy saves, not an automatic rewrite of a damaged `global_mod_data.bin`. The supplied log fails in native loading before Echoes can initialize. Keep that server's original save and backups. Recovery needs a verified working backup or inspection of the actual damaged file. The log alone cannot establish ownership of every corrupt field.

## Encounter coverage and budgets

The population director checks underserved player areas each cycle and alternates nearby/distant opportunity priority. Existing global, faction, per-player, safe-position and whole-cohort checks remain. Explicit world limits above 82 are no longer silently clamped to the sum of authored faction caps; each faction still retains its own cap. Filling partial cohorts counts other living identities in the global total.

Every 120,000 milliseconds of director time, one player center is considered in rotation. With fewer than four nearby procedural survivors and no incoming coverage patrol, one complete abstract ordinary squad within 1,200 tiles can receive a fixed patrol destination 48–76 tiles from that center. All members must be outside every player's demotion radius. Unique actors, event squads, forced/companion/campaign ownership, native vehicle attachment and active field work are excluded.

This generates no people and does not increase body or CPU budgets. The existing road service and offline speed move the squad. Routing ends on native materialization, arrival, protected ownership or a one-hour director-time expiry. No moving player tracking is applied after dispatch. No eligible squad, safe loaded square or available native capacity means arrival waits; this is not a forced encounter guarantee.

## Validation

The focused native harness reproduces the original error and verifies signed-short boundary sizes, a 700 KB snapshot, Unicode/surrogate boundaries, trailing table alignment, and a production manager save/load cycle. It also verifies native clothing visual serialization, repeated weapon-state changes retaining clothing objects, empty visual slot alignment, and bounded existing-squad travel without moving a materialized actor. The full release gate adds the existing combat, death/corpse, persistence, Lua/UI, authority and isolated dedicated startup checks. No connected visual multiplayer playthrough is claimed.
