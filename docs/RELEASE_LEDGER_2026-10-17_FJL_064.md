# FJL 0.6.4

- [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-10-17-faded-java-loader-0.6.4).
- [Pinned r4 signing workflow](https://github.com/FadedMods/faded-mod-installer-cloud/actions/runs/39064558051), successful.
- Main and Faded Realms loader v2/v3 channels advance to 0.6.4. All 124 Main
  and 67 Faded Realms mod entries, bridge 0.5.7 bytes/metadata, minimum loader
  requirements, legacy loader channels and other catalogs are preserved.

The loader embeds the approved graffiti FJL - Online badge, green Online accents
and a real clock-driven purple monitor pulse. It anchors above the lower-right
legal/report/mod/reset controls and hides only the main-menu game-version button.
Older optional bridge skull panels are replaced without requiring a bridge update.
Game-version APIs, save compatibility and legal controls remain available.

Supported discovered ZombieBuddy Java candidates can be selected before startup
activation through isolated bytecode previews. Only selected Java is published or
initialized. Policy and runtime refusals persist; inactive alternatives are inspected
independently and unknown Lua companions are not automatically approved.

Client initialization failures can reach the menu only before world loading; partial
initialization permanently requires a fresh JVM before gameplay. Servers and clients
after world entry retain startup failure. Unexpected patch errors still block class
definition. Exact inserted frames follow original method locals/stack without loading
class hierarchies or guessing Object types.

Validation: Java 25 / installed PZ 42.21.0 build succeeds with 278 tests, 272 passes,
zero failures/errors and six unavailable audited-Workshop-fixture skips. Real Kahlua
and stock Lua menu regressions cover old/new bridge ordering, resets, one panel,
720p/1080p placement, animation, version hiding and cosmetic failure isolation.
Package audits and pinned r4 verification cover nine ZIP signatures and sixteen
checksum entries. Existing public mod APIs and multiplayer protocol are unchanged;
clients and servers still need matching loader versions.

No live game, save, Workshop files or remote server was modified or restarted.
Full gameplay and live graphics rendering were not exercised by these offline tests.
