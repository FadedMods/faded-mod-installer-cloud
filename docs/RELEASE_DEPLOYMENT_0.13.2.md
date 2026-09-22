# Echoes of Humanity 0.13.2 deployment

Completed 2026-09-22T10:07:16.792342+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-22-echoes-0132). Catalog commit `84297f90bf39a156f0514dcf731b1cad3b343078` updates Echoes only in Main and Faded Realms. The 121/79 ID sets remain unchanged; manifest validation and CodeQL passed.

## Repairs

Multiplayer weapon changes previously rebuilt worn clothing, rerolling native colour and texture choices. Clothing now has separate change tracking from attached weapons. Bounded native visual records reproduce the server's clothing tint, variants, decals and wear, including reconnects. Existing clothing objects survive weapon changes.

The director previously offered nearby encounters through a 35% roll followed by one-in-four priority, allowing distant sites to take most opportunities. Nearby areas now receive alternating priority. An existing abstract four-person patrol may travel toward an underserved area; routing is bounded, respects local quotas, protects owned/event actors, and never teleports native bodies or creates identities above caps. Explicit world limits above 82 are respected, and micro/civilian people count when filling partial squads. Default materialized-body and CPU budgets are unchanged.

The supplied log also reports `invalid lua table type 69` during native GlobalModData loading. The regression reproduces this exact error with an oversized NPC-like string. PZ's signed-short string length cannot hold large Base64 actor states. Echoes now splits oversized saved strings into safe chunks and reassembles them through the production load boundary. Small legacy snapshots remain supported; chunked saves require 0.13.2 or newer.

**Already-damaged saves:** the update prevents this overflow. It cannot repair a file that fails before Echoes starts. Preserve the user's save and backups; use a verified working backup or diagnose the actual damaged global_mod_data.bin separately. Only the report/log was available, so that remote world's recovery is not claimed.

## Validation and delivery

- 57 focused native regression checks cover the exact save failure, signed-short boundaries, a 700 KB snapshot, Unicode, following table fields, actual manager save/load, native clothing visual records, repeated weapon changes, visual slot alignment, and capped existing-squad travel.
- Full native/offline release gate passed, including damage/corpses, persistence, authority, Lua/UI, package/assets/voices and public/protected ABI preservation across 36 overlays. Runtime contains 538 classes.
- Isolated dedicated-server bootstrap and native bridge/schema probes passed. No connected visual multiplayer playthrough or FPS measurement is claimed.
- Public packaged Installer 0.3.3 clean/existing installation checks passed with FJL 0.4.1 ready. All 990 public, local and OVH payload files match their staged archive. Remote ownership is correct.
- ZIP SHA-256: `948486c993c79621700560dd2a82b539f38300de17c6c3bc80655a61af1a6e9a`. Existing Installer 0.3.3 Windows, multilingual, Linux and macOS update entries remain verified; no installer rebuild was needed.

Canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`. Immutable archive: `E:/Faded Mod Staging/EchoesOfHumanity-0.13.2-release`.

Local playable: `C:\Users\Luis\Zomboid\mods\EchoesOfHumanity`. Previous copy preserved at `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260922_055952` after exclusive JAR-access validation. The enabled profile is unchanged; FJL READY passed.

The Downloads PDF has 41 pages, 71 bookmarks and 180 verified internal links. Public PDF/Discord assets match the local files byte-for-byte.

## OVH

A fresh zero-player heartbeat, active service, free lock and sufficient disk preceded the protected backup/update/restart. Verified backup `project-zomboid-20260922T100045Z.tar.zst`: 13,202,350,992 bytes, SHA-256 `dc4a000ebe1b63a743e6c8749826434216cb84a0be16c79dca866ad25bee60b0`.

ServerSync installed 0.13.2. GAME_READY, completed WorldDictionary, SERVER STARTED, both UDP game listeners, zero crash restarts, unchanged enabled mod IDs, fresh online heartbeat and the Nexus artifact hash all passed. No world or NPC data was deleted.

## Interfaces and evidence

Campaign API 3 and community extension 1 remain unchanged. [Native contract](WARDROBE_SAVE_NATIVE_CONTRACT.md) documents the additive wornVisuals snapshot field, safe-string persistence representation and encounter routing limits. Clients and server should update together and restart fully.

Evidence: source `build/wardrobe-0132/`, `.test-work/wardrobe-0132/`, staged `SERVER-SMOKE.json`, and installer `.test-work/echoes-0132/`. Raw user logs and server access details are not published.
