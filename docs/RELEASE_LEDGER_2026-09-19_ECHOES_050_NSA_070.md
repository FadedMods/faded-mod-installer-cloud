# Echoes 0.5.0 / Never Survive Alone 0.7.0-alpha

Published September 19, 2026 under tag
`mod-assets-2026-09-19-echoes-050-nsa-070`.
Both existing entries are updated in Main (119 unchanged IDs) and Faded Realms
(79 unchanged IDs). FFO API 3 remains compatible. No new pack IDs were added.

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| EchoesOfHumanity-v0.5.0.zip | 52,620,244 | b066a90fddb50c287c367fbb11e942e79466136ac35e543812cda4d25ef69d7f |
| NeverSurviveAlone-v0.7.0-alpha.zip | 233,829,580 | 84db53897b84c318ca6ffc22deda0a7be40b53ae03518ed357ad4e3383a94251 |

EOH has 838 portable payload files / 63,925,754 uncompressed bytes; NSA has 692 /
239,242,647. ZIPs contain a single authoritative 42/mod.info, forward-slash paths
and their existing mod directory names. Native EOH JAR SHA-256:
`bf4e540bd989502e238cfb3fd5341b88429df306bafd785cdfa720b17ed5499f`.

EOH adds faction hails/radial replies, 158 bundled AI-generated OGG voice clips
covering 79 preset lines, separate optional client speech for AI chat, an actual
NPC participant bridge for NSA, advanced finite medicine, washing, founded camps
and physical generator upkeep. NSA owns opt-in, scenes, cooldowns and benefits;
EOH owns persistent NPC identity, relationship, action and emergency interruption.
NSA has a new compact shelter/pair radial icon. Both mods remain independently usable.

All native and Lua regressions passed, including 24 expansion boundary/wound-model
checks, 10 hail and 16 chat client lifecycle checks, NSA lifecycle/wardrobe/item
checks and all 158 audio hashes/registrations. Combined isolated B42.20.4 dedicated
startup verified both mods, the native NSA bridge, unauthorized-call denial and
the voice registry. A local memory allocation failure on an intermediate smoke
run was followed by a successful final rerun of the exact staged JAR.

Local installation used the production installer's backup-and-replace path.
All 838 EOH and 692 NSA local files match their respective archives. Previous
versions were backed up. Staging lives under the owner's E:\Faded Mod Staging.

The release also includes a 30-page PDF with clickable contents, 27 bookmarks
and 81 checked links, plus a 1,900-character Discord post. Both were saved to the
owner's Downloads folder. PDF SHA-256:
`a133e6d2484c6b6d6dac3f65b9685970980cb86ed0f0c5a29471efa27a13cccf`.

No connected-player visual acceptance or paid live-chat speech test is claimed.
The bundled voice pack was actually generated and decoded; optional live speech
has schema/boundary checks and text fallback. Full donor parity is not claimed.

Public installer and OVH backup/restart verification follow this catalog commit;
the final result will be appended after the running server is checked.
