# FJL 0.5.7 publication

Authorized by the owner on 2026-09-30. Release tag:
`mod-assets-2026-09-30-faded-java-loader-0.5.7`.

This release fixes the restart-notice empty-match loop in the game's Kahlua Lua
runtime and checks changed Java selections before vanilla resets Lua. It keeps
the selected mods for a full restart. The loader's 23 transformation/Mixin classes
remain byte-identical to 0.5.6, preserving the EoH/PZ Optimized override fix.

The bridge moves from the live catalog's 0.4.3 to 0.5.7. Its published FadedStack-Coop
1.0.2 JAR is retained byte for byte (SHA-256
`6ab5752de6426dcfb243078c1506eacdc7d83de7b27f70d9833eba56d564a9de`), preserving
PZ 42.21 admission and both ArrayList/List CSR Test alias handling. The CLI backs up
and retires only the exact superseded official 1.0.1 JAR when installing its exact
1.0.2 replacement. Custom files remain intact.

Four client packages cover Windows, Linux, native Steam Deck, and macOS. Two server
packages cover Windows/Linux. Steam Deck uses client-linux in the existing v3
installer schema; its dedicated ZIP is also a signed direct download. The SDK,
example plugins, and standalone bridge are included.

## Signing and validation

- [Signing run](https://github.com/FadedMods/faded-mod-installer-cloud/actions/runs/36762317789)
  succeeded using `faded-fjl-release-2026-08-r4`.
- Public DER SHA-256:
  `b04d626a7908926c3f51bdd9685a5ff0fceacf8b4c474bcbd2175306e06d1166`.
- All nine Ed25519 signatures and 16 checksum entries were verified after download;
  every package matched the local release bytes. Package CRCs, Unix executable
  modes, LF scripts, embedded agent/CLI/bridge resources, and current Lua passed.
- 202 Java tests passed with zero failures/errors/skips. Real-game Kahlua selection
  and notice harnesses, the remaining Lua harnesses, 24 POSIX launcher checks,
  four metadata tests, and manifest validation passed.
- Final Windows packaged install/verify checked bridge upgrade, backup, retirement
  of the superseded JAR, and custom-file preservation. Linux/Deck packaged
  install/verify/uninstall passed under WSL with paths containing spaces.
- FadedStack-Coop 1.0.2 passed client/server bytecode preflight on PZ 42.21.0.
- Native macOS/Steam Deck hardware tests and the original affected user's live
  session retest remain outstanding.

The first signing run signed successfully but its upload lookup returned 404 for
the draft release. The workflow now resolves its numeric release ID through
`gh release view`, allowing signing and verification before public publication.
No private key was retrieved locally, and the pinned key is unchanged.

## Catalog scope and activation

Only Main and Faded Realms `java_loader_v2`, `java_loader_v3`, and their existing
FadedJavaLoaderBridge entries are updated. Legacy loader channels, unrelated mods,
minimum loader requirements, catalog membership, and the retired Outback catalog
are preserved. The desktop installer app does not require a rebuild.

This publication does not deploy or restart game servers. Owners must update both
the server agent and bridge and restart; multiplayer loader versions must match.
Nexus world packs pinning the previous bridge need regeneration after that update.
Clients refresh their installer catalog, update FJL and the bridge, and fully restart.
