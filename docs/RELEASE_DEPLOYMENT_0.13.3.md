# Echoes of Humanity 0.13.3 deployment

Completed 2026-09-22T10:47:12.648149+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-22-echoes-0133). Catalog commit `bd0bb4e3a090b852a7d059b04c0017584579e63c` updates Echoes only in Main and Faded Realms. The 121/79 ID sets remain unchanged; manifest validation and CodeQL passed.

## Repairs

Community planning always began at the first resident, allowing that person to receive repeated jobs while others waited. Loaded groups now receive one planning slice per second in rotation, and each group rotates its first worker. Queued actions retain their lease. The social/work admission path now accepts unique Rosewood residents and reduced-simulation micro-factions while respecting combat, missions, conversations, companions and urgent survival needs.

Failed community movement clears the failed destination and requests a bounded short native route before resuming work. Existing action timeouts remain. Residents remain based at their settlements and perform local work, patrol and supply trips; they do not abandon their home merely to create movement. Impassable geometry still requires a usable route or environmental interaction.

New server sandbox setting MicroActivePercent defaults to 33%, range 10–50. New community bodies, including legacy Rosewood residents, respect that share of the materialized NPC budget. The gate runs at promotion and native spawn/restore. Existing visible residents and recruited companions retain priority. New founding/recruitment is also limited to one third of the world identity cap or the lower configured community cap. Existing people are preserved; this reserves admissions rather than forcibly despawning anyone. Main factions retain their existing global limits.

Rosewood consequence refusals now use a stable reason code and localized message with the speaker name. The UI provides a direct Close response and a safe fallback for unknown/missing reasons. Existing interaction ownership is released on this refusal. The previous clothing, trade, damage, corpse and save repairs remain included. Native actors/world mutations stay on the authoritative game thread; existing bounded background road workers remain, with no GPU change.

## Validation and delivery

- 27 new native checks execute community rotation despite a repeatedly ready first worker, queued leases, unique/reduced work completion, ownership exclusions, authority, failed/successful movement and admission reservations. All 30 existing daily-life checks pass.
- 51 actual Lua UI checks pass, including 12 new rejection/dismissal checks, in stock Lua and native Kahlua. Native parsing verifies all 58 sandbox settings and the new setting's type, range, default and changed server value.
- Full native/offline release gate passed, including damage/corpses, persistence, authority, Lua/UI, package/assets/voices and public/protected ABI preservation.
- Isolated dedicated-server bootstrap and native bridge/schema probes passed. No connected visual multiplayer playthrough or FPS measurement is claimed.
- Public packaged Installer 0.3.3 clean/existing installation checks passed with FJL 0.4.1 ready. All 990 public, local and OVH payload files match their staged archive. Remote ownership is correct.
- ZIP SHA-256: `414f5920d060b0993b6a9e2e8c3cc0d409d595671aaf8b258f6a908de1b1ea67`. Existing Installer 0.3.3 Windows, multilingual, Linux and macOS update entries remain verified; no installer rebuild was needed.

Canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`. Immutable archive: `E:/Faded Mod Staging/EchoesOfHumanity-0.13.3-release`.

Local playable: `C:\Users\Luis\Zomboid\mods\EchoesOfHumanity`. Previous copy preserved at `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260922_063938` after exclusive JAR-access validation. The enabled profile is unchanged; FJL READY passed.

The Downloads PDF has 42 pages, 72 bookmarks and 183 verified internal links. Public PDF/Discord assets match the local files byte-for-byte.

## OVH

A fresh zero-player heartbeat, active service, free lock and sufficient disk preceded the protected backup/update/restart. Verified backup `project-zomboid-20260922T104041Z.tar.zst`: 13,203,589,193 bytes, SHA-256 `64f2a62dd170a68533c9f42c1590ffbe3030ae032f596964f3eaa30a5bd25d86`.

ServerSync installed 0.13.3. GAME_READY, completed WorldDictionary, SERVER STARTED, both UDP game listeners, zero crash restarts, unchanged enabled mod IDs, fresh online heartbeat and the Nexus artifact hash all passed. No world or NPC data was deleted.

## Interfaces and evidence

Campaign API 3 and community extension 1 remain unchanged. [Native contract](COMMUNITY_PROGRESS_NATIVE_CONTRACT.md) documents work ownership, bounded cadence, capacity semantics and the rejection response. Clients and server should update together and restart fully.

Evidence: source `build/community-0133/`, `.test-work/community-0133/`, staged `SERVER-SMOKE.json`, and installer `.test-work/echoes-0133/`. Raw user logs and server access details are not published.
