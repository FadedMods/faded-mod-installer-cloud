# Echoes of Humanity 0.13.1 deployment

Completed at 2026-09-22T05:45:50.614994+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-22-echoes-0131). Catalog commit `398f0e7f5e6e5b94814db15e8d16c970e2b9f3e1` updates Echoes only in Main and Faded Realms. Other entries and the 121/79 ID sets remain intact. Manifest validation and CodeQL passed.

## What changed

Players could receive a request for clean water without a clear way to hand it over. The native needs choice now opens a validated route to Trade / Give supplies and reports the same inventory-backed shortages used in trade. Main factions and micro-factions share this behavior, including Rosewood residents.

Trade displays remaining clean water, safe food, dressings and compatible ammunition needs. Matching items sort first and receive a bounded scarcity premium in both directions. Giving useful supplies with nothing requested awards capped personal/faction standing; real deliveries remove needs immediately, and use or sale recreates shortages. Persisted per-faction daily cooldowns and original-item gift markers prevent repeat-aid farming. Unfair offers refresh stock/prices without closing the window. The needs/feedback panel stays in a fixed, clipped scroll area at larger font sizes. Capacity checks permit an overburdened player to donate.

B42 fluid contents determine clean-water eligibility, including clean carbonated water. Empty bottles, taint, fuel, poison and unsafe food do not satisfy needs. The same water/food classifier also serves ordinary NPC consumption. There is no new per-frame inventory scan or network poll loop.

## Validation

- 132 native trade-needs regression checks, including the actual resident conversation and native trade session, real original item movement, authority rejection, duplicate/stale IDs, partial/fulfilled supplies, micro-faction standing, gift replay, price reversal protection and saved cooldowns.
- 39 client-flow/layout checks, including nine screen/font combinations, under both stock Lua and Project Zomboid Kahlua; 36 existing price-column, scrollbar, UTF-8 and cache checks retained.
- Full native/offline release suite, original 36-overlay public/protected ABI preservation, 534 runtime classes, package/assets/voices and damage/corpse/save regressions passed.
- Isolated dedicated startup passed with real vanilla empty, clean, tainted, contaminated, fuel and carbonated fluid containers, safe/poisoned food, native bridges, item/trait registries and unchanged API versions. Connected-player visual gameplay is not claimed as tested.
- Public packaged Installer 0.3.3 passed clean and existing-install paths with FJL 0.4.1 ready. All 990 public, local and OVH payload files match the staged archive; remote ownership is correct.
- ZIP SHA-256: `9fc3dc19c1c4d1da9937975c4446fc6b019b4297421ea614f2dd9b1c1949558d`. Installer 0.3.3's existing Windows, multilingual, Linux and macOS update entries remain verified. This mod release requires no installer rebuild.

## Publication and local copy

Canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`. Immutable release: `E:/Faded Mod Staging/EchoesOfHumanity-0.13.1-release`.

Local playable: `C:\Users\Luis\Zomboid\mods\EchoesOfHumanity`. Exclusive JAR access was checked; previous installation preserved at `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260922_013730`. The existing enabled-mod profile is unchanged; FJL reports READY.

Downloads guide: 41 pages, 70 bookmarks, 178 verified internal links. The public PDF and Discord post match their local files byte-for-byte.

## OVH

Fresh zero-player heartbeat, active service, free backup lock and sufficient disk preceded the protected backup/update/restart. Verified backup `project-zomboid-20260922T053858Z.tar.zst`: 13,201,991,820 bytes, SHA-256 `c66c1a7e7adee8a552706e6b9eaebb5764ad0a864d5cfa8fecfef83cf4df8319`.

ServerSync installed 0.13.1. GAME_READY, completed WorldDictionary, SERVER STARTED, both game UDP listeners, zero crash restarts, unchanged enabled mod IDs, a fresh online heartbeat and the expected Nexus package hash all passed. No save or NPC data was deleted.

## Interfaces and evidence

Campaign API 3 and community extension 1 are unchanged. [Trade needs native contract](TRADE_NEEDS_NATIVE_CONTRACT.md) describes additive payload fields, read-only physical supply classification, authority and new aid receipts. Existing NPC save schemas remain compatible.

Clients should refresh Installer 0.3.3, update and fully restart. To help a resident: Talk, Trade / Give supplies, add items to Your offer, request nothing, Give supplies. Items must be in main inventory and not equipped/favorited/protected.

Local evidence: source `build/trade-0131/`, `.test-work/trade-0131/`, final smoke recorded in staged SERVER-SMOKE.json, and installer `.test-work/echoes-0131/`. Raw user logs and server access details are not published.
