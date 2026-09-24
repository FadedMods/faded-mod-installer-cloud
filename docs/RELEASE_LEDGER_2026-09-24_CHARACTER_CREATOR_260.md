# Character Creator 2.6.0

Release: `mod-assets-2026-09-24-character-creator-2.6.0`.

Rebuilds the default female ("Realistic") and Curvy athletic bodies as
MakeHuman (CC0) bodies and rebuilds Curvy and Plus size with rounder buttocks.
Fuller, shorter necks that no longer stretch in the idle pose; a lower
trapezius matching the game body's neck/shoulder line; new face shaping with
all 57 face-shape heads rebuilt; tone 4 without heavy makeup and tone 2
without painted pubic hair; new garment cages, head fit and recalibrated
Sculpt controls. Saved body choices, item names and GUIDs are unchanged.
Requires Faded Java Loader 0.3.4+; client plugin `charactercreator.morph`
remains version 1.0.0, mode HYBRID.

## Immutable package

- `CharacterCreator-v2.6.0.zip`: 1,280,782,184 bytes.
- SHA-256: `ffa813e2fd98e8e8e59f9c751c09606811fa551453dbc05328180eb212ce8a1a`
  (GitHub's server-computed digest matches).
- Expanded: 1,647,649,013 bytes; required free space: 3,465,302,109 bytes.
- 13,648 files under `CharacterCreator/`, canonical `42/mod.info` only; ZIP CRC
  and installer extraction pass and the extracted payload equals the source.

## Validation and limits

The complete source gate passes. The rebuilt renderer passes 95,055
installed-engine/FJL/shader/GPU checks; all four female bodies pass the
installed importer rig/weight audit and all 96 controls. An isolated
B42.20.4 client with the renderer loaded showed every body, neck close-ups,
tone-matched faces, all five tones and four outfits in the creator preview
(idle animation). World gameplay, zombies in the world and multiplayer are
unverified.

## Catalogs

Only the CharacterCreator entry in Main changed (123 entries); every other
entry, ID order and Java-loader metadata is preserved and the manifest
validator passes. Faded Realms deliberately stays on 2.4.0: the OVH server was
not updated in this release.

## Local deployment

`E:\PZ User Data\Zomboid\mods\CharacterCreator` (also reached through the
`C:\Users\Luis\Zomboid` junction) matches all 13,648 payload files; installer
backup `%APPDATA%\FadedLocalModInstaller\backups\CharacterCreator_20260924_041622`.
Staging `E:\Faded Mod Staging\CharacterCreator` matches the same payload; the
previous staged tree is in
`E:\Faded Mod Staging\backups\CharacterCreator-staging-pre-2.6.0-20260924-040602`.
