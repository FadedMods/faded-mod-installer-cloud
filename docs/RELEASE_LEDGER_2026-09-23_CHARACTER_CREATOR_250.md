# Character Creator 2.5.0

Release: `mod-assets-2026-09-23-character-creator-2.5.0`.

Replaces the Curvy full and Curvy soft bodies with MakeHuman (CC0) "Plus size"
and "Curvy" bodies: detailed faces with eyeballs that keep all seven eye colours,
five new skin tones each, rebuilt face-shape heads, new garment cages, head fit
and recalibrated Sculpt controls. Saved body choices, item names and GUIDs are
unchanged. Also ships the September 22 shoulder/neck weight smoothing for the
default, athletic and nude bodies. Requires Faded Java Loader 0.3.4+; client
plugin `charactercreator.morph` remains version 1.0.0, mode HYBRID.

## Immutable package

- `CharacterCreator-v2.5.0.zip`: 1,258,190,415 bytes.
- SHA-256: `2433d464caac4b0283abbee27d968e8f18917c5b7c1a61ba10be8f939457f277`
  (GitHub's server-computed digest matches).
- Expanded: 1,628,097,479 bytes; required free space: 3,423,158,806 bytes.
- 13,648 files under `CharacterCreator/`, canonical `42/mod.info` only; ZIP CRC
  and installer extraction pass and the extracted payload equals the source.

## Validation and limits

The complete source gate passes. The rebuilt renderer passes 95,055
installed-engine/FJL/shader/GPU checks; both new bodies pass the installed
importer rig/weight audit and all 96 controls. Offline GarmentFit replays,
clothing-mask renders and posed renders were checked. The new bodies are
**unverified in game**.

## Catalogs

Only the CharacterCreator entry in Main changed (123 entries); every other
entry, ID order and Java-loader metadata is preserved and the manifest
validator passes. Faded Realms deliberately stays on 2.4.0: the OVH server was
not updated in this release.

## Local deployment

`E:\PZ User Data\Zomboid\mods\CharacterCreator` (also reached through the
`C:\Users\Luis\Zomboid` junction) matches all 13,648 payload files; installer
backup `%APPDATA%\FadedLocalModInstaller\backups\CharacterCreator_20260923_173418`.
Staging `E:\Faded Mod Staging\CharacterCreator` matches the same payload; the
previous staged tree is in `E:\Faded Mod Staging\backups`.
