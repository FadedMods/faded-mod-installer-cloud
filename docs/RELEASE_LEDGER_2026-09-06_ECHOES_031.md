# Echoes of Humanity 0.3.1 release ledger

- Published: 2026-09-06
- Release tag: `mod-assets-2026-09-06-echoes-of-humanity-0.3.1-factions-ai`
- Asset: `EchoesOfHumanity-v0.3.1.zip`
- Size: `41185510` bytes
- SHA-256: `12c134589f853dbaace3fdccf8bf5f31643a3dab0e202dbd3f03bb9605d601f3`
- Prepared payload: 668 files / 47,917,136 bytes
- Java plugin: `faded.echoesofhumanity` 0.3.1 (`BOTH`, `HYBRID`)
- Runtime JAR SHA-256: `40B32DEE60541AFD7DA5849ECFF6ABF124C08B22C5735403004640D490A929F2`

## Release validation

- Full native Java, Lua, item, faction, authority, integration, provenance, ABI, and package regression suite passed.
- Isolated Project Zomboid Build 42.20.4 dedicated-server smoke passed server start, native bridge/schema probes, 112-item registry, and all 10 starting-faction registrations with no fatal matches.
- ZIP CRC, forward-slash paths, traversal checks, manifest cardinality, and production-installer preparation passed.
- The archive intentionally contains only the authoritative `42/mod.info`; the duplicate legacy root metadata remains in source/staging but is excluded from hosted installer archives.

The headless smoke does not replace a connected-player, rendered character-creation, or physical-driving playtest.
