# Echoes of Humanity 0.4.0 release ledger

- Published: September 19, 2026.
- Tag: `mod-assets-2026-09-19-echoes-of-humanity-0.4.0`.
- Asset: `EchoesOfHumanity-v0.4.0.zip` (48,793,729 bytes).
- SHA-256: `1c7687179e5c3fa988065f7a8c25e84cdcebd3d1ddb859e85232ccf79a5bfafa`.
- Portable payload: 677 files / 59,946,667 bytes; one authoritative `42/mod.info`.
- Native runtime: 351 classes / 1,289,111 bytes.
- Runtime SHA-256: `c2130fc293d5a0bf830a636f56e162f74e571a9dae044aa7dc3ce159db771941`.
- Plugin: `faded.echoesofhumanity`, 0.4.0, BOTH/HYBRID; FJL 0.2.0+.
- Target: Project Zomboid 42.20.4.
- Main retains 119 IDs; Faded Realms retains its 79 IDs. Only existing Echoes
  release metadata is updated in both catalogs.

## Delivery

The release includes the runtime ZIP, a 24-page PDF player manual with clickable
contents and 23 bookmarks, and a Discord post under the standard 2,000-character
message limit. The manual documents existing gameplay, all new features, donor
adaptations, permissions, configuration, campaign boundaries and known gaps.

This release adds native idle/gesture recovery, physical settlement construction,
persistent friend/partner companions, finite care/passenger following, durable
identity reservations, protected admin outfit presets, health/ammo presentation,
optional API-key chat and bounded companion tools. FFO campaign API 3 is preserved
and extended with stewardship, service/depot/freight and combat-evidence behavior.

## Checks and local installation

- Full standalone Java, regression, Lua UI/transport, compatibility, asset,
  provenance, ABI and package validation passed.
- 53 companion checks, 47 chat checks, living-activity scenarios, 16 Lua chat
  lifecycle checks; 32 Echoes and 86 FFO files parsed by real-game Kahlua.
- Original public/protected interfaces retained across 28 native overlays.
- Isolated B42.20.4 dedicated startup reached SERVER STARTED and verified native
  NPC/Living World/companion/chat bridges, world schema, 113 registered items,
  Angela protections and all ten faction origins, without fatal audit matches.
- ZIP CRC, portable paths, source/stage/ZIP SHA parity and production installer
  preparation passed. The user's local playable was updated with the installer's
  backup-and-replace operation; all 677 installed files match the ZIP.
- The prior 0.3.3 local installation and previous canonical staging tree were
  preserved as backups. Source work, including preexisting dirty/untracked work,
  was not reset or blanket-staged.

## Remaining acceptance and scope

No paid provider request or connected-player visual/MP acceptance is claimed.
Extended construction/driving, crowd pathing, HUD/wardrobe/care/passenger
replication and measured gameplay performance remain live checks. Full donor
surgery/intimacy, workstations/decor, arbitrary founding, advanced defenses and
generator installation/refueling are not included. FFO must consume its native
contracts; this release does not complete its full campaign. Embedded MCP uses
authenticated game transport, not an external HTTP/stdio listener.
