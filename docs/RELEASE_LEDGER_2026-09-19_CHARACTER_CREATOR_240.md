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

Local staging/install and OVH backup/restart evidence will be recorded after
the corresponding operations complete. The OVH enabled-mod list is independent
of either catalog and must remain unchanged.
