# Character Creator 2.4.0

Release: `mod-assets-2026-09-19-character-creator-2.4.0`.

Updates the five selectable body shapes, source-rest animation, body and face
sculpting, clothing/accessory fitting, heads, skin tones, eye colors and male
anatomy coverage. Traits have separate positive/negative lists with native icons;
prebuilt characters have live 3D portraits and fixed starting traits. The accepted
Faded model, arm and glove repair is retained. Requires Faded Java Loader 0.3.4+;
client plugin `charactercreator.morph` remains version 1.0.0, mode HYBRID.

## Immutable package

- `CharacterCreator-v2.4.0.zip`: 1,274,072,364 bytes.
- SHA-256: `b6d9fdbe1e63ca724961bad29ef75842d69e06c699881fa547102cbed391169b`.
- Expanded: 1,648,757,502 bytes; required free space: 3,459,700,778 bytes.
- 13,648 files under `CharacterCreator/`, with the canonical `42/mod.info` entry.
  The portable packager deliberately omits the redundant root mod.info.
- ZIP CRC, installer extraction and all extracted source hashes pass.
- Production renderer SHA-256:
  `fdb01fba79c1f1e543e47cd297d1cfc763d1086ddb613ede31de2acf2cdec597`.
- Body inventory SHA-256:
  `ff363efe95fa68e777369561b3c1a345dc1fc82514d761edc5b80d674f64ce1d`.

## Validation and limits

The complete source gate passes. The exact packaged renderer passes 95,052
installed-engine/FJL/shader/GPU checks. Final body importer audits pass all 96
controls; the male anatomy alias is bound to the clothed male normalization
frame. Saved-mesh cargo and vest clearance checks pass all three curvy profiles.

The owner explicitly requested skipping the final combined in-game test. Final
combined appearance and gameplay are **unverified in game**; automated checks and
earlier runtime observations are not represented as final in-game acceptance.

Only the existing CharacterCreator entry changes in Main (119 entries) and
Faded Realms (79 entries). All other entries, ID order and Java-loader metadata
are preserved; the manifest validator passes.

Catalog release commit: `f9a93d1a9b9a3cd2e531d148dabe018af8cf4241`.
GitHub's server-computed SHA-256 and asset size match the local ZIP, and both
public catalogs were read back and matched the committed content.

## Local deployment

All 13,648 files match the verified ZIP at both destinations:

- `E:\Faded Mod Staging\CharacterCreator`; adjacent backup
  `CharacterCreator-before-2.4.0-20260919T152634Z`.
- `E:\PZ User Data\Zomboid\mods\CharacterCreator`; installer backup
  `%APPDATA%\FadedLocalModInstaller\backups\CharacterCreator_20260919_112754`.

The installer profile helper verified/enabled `charactercreator.morph` in the
user's FadedJavaLoader default profile, preserving unrelated plugin settings.
The game installation was not modified.

## OVH deployment

The immediate pre-restart check observed zero players, a heartbeat 5.27 seconds
old, active service, available backup lock and 95.88 GiB free. The authorized
`sudo faded-pz-backup` operation returned zero and retained the default restart.

- Verified backup:
  `/srv/backups/project-zomboid/daily/project-zomboid-20260919T153731Z.tar.zst`,
  12,833,187,383 bytes, with checksum sidecar.
- FJL independently downloaded and verified the published ZIP SHA-256 at
  15:40:47 UTC; installed CharacterCreator 2.4.0 at 15:41:00 UTC.
- Installed renderer matches `fdb01fba...cdec597` exactly.
- FJL reached GAME_READY, WorldDictionary initialization completed, and
  `SERVER STARTED` was observed. UDP 16261/16262 listen; the public heartbeat
  was online at 15:43:24 UTC.
- The enabled 80-mod ID list remains unchanged. No actionable CharacterCreator
  startup errors were found; FJL emitted its generic trusted-executable-code
  notice for the plugin.

This verifies installation and server startup, not the waived final in-game
appearance review.
