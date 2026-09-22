# Echoes of Humanity 0.12.2 hotfix deployment

Completed at 2026-09-22T03:39:32.101270+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-echoes-0122). Catalog commit `6636d894e43080fe0b42139692b303e52fc417f9` changes only Echoes in the existing Main and Faded Realms entries. Catalog ID sets and other mods are preserved; manifest validation and CodeQL passed.

## Diagnosis and repair

The reported `console - Copy.txt` contains 1,447 render exceptions; the local console contains 1,878. Both identify `EchoesOfHumanityHunterDrop.lua:45`, where `next(Drop.events)` runs on every OnPreUIDraw. PZ's shipped Kahlua libraries do not expose global `next`, so the overlay failed even without any hunter arrival.

The overlay now checks for active events through the supported `pairs` iterator. Idle frames create no drawing resources. Expired replay receipts are also pruned while idle. Existing parachutes, aircraft, one-time audio, duplicate suppression, touchdown cleanup, zero mouse area and under-menu draw ordering remain in place. No gameplay authority, API, save schema or saved character data changed.

## Verification

- A regression executes the actual production Lua overlay with the installed game's Kahlua libraries and actual `stdlib.lua`. The pre-fix code reproduces `Object tried to call nil in render`; the repaired code passes initial idle frames, active rendering, duplicate delivery, touchdown, replay expiry and reset.
- The stock Lua fixture additionally disables `next` to prevent an accidental compatibility assumption.
- Full native/offline release gate and isolated dedicated bootstrap passed at `2026-09-22T03:30:12.7776213Z`. This local isolated server check did not contact or restart OVH. Connected multiplayer gameplay is not claimed as tested.
- ZIP SHA-256: `9a61d0d2e794c32a0f6c233bd56e77a794a02f2f0d0bf92411f08ed7d59bdb72`. All 990 public-download and local playable payload files match the staged archive byte-for-byte.
- Packaged standard Installer 0.3.3 passed both clean and existing public installs, including FJL bridge activation. The local native loader verifier reports READY; the existing local profile remains intact.
- The installer updater's existing Windows standard/multilingual, Linux/Steam Deck and macOS catalog remains unchanged and verified. This mod-only hotfix does not require new installer executables.

## Release and local installation

Canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`. Immutable release: `E:/Faded Mod Staging/EchoesOfHumanity-0.12.2-release`.

Local playable: `C:\Users\Luis\Zomboid\mods\EchoesOfHumanity`. The JAR lock check passed before replacement; previous installation preserved at `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260921_233841`.

The updated PDF in Downloads has 39 pages, 67 bookmarks and 170 checked internal links. PDF and Discord post were uploaded and verified against their public release bytes.

## OVH scope

**OVH deployment and restart were deliberately skipped at the user's request.** No OVH payload or live-server version verification is claimed. A later normal server update can consume the published catalog.

Users should update through Installer 0.3.3, refresh the mod list and fully exit/reopen the game. Administrators should align server and client versions. No world reset or NPC data deletion is needed.

Evidence: source `build/log-review-0122/`, `.test-work/hunters-0122/`, and installer `.test-work/echoes-0122/`. Full user logs remain local and are not published.
