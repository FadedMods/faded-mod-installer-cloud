# Release ledger: ArmorPK 3.0.2

Date: 2026-11-21. Owner-authorized hotfix ("fix it dont test it just fix and push").

## Problem

ArmorPK 3.0.1's client fit plugin (`faded.armorpk.fit`) used a `@Redirect` on the
`ModelMesh.Draw(Shader)` call inside `Model.DrawSolid`. Character Creator's morph
plugin (`charactercreator-morph.mixins.json:WorldModelMixin`) already redirects that
same call. Mixin skipped ArmorPK's redirect, its `require = 1` turned that into a
critical injection failure, and FJL refused to define `Model`, so the client aborted
at startup. Dedicated servers were unaffected (the plugin is client-only).

## Fix

- `ArmorPKSolidModel` now uses two `@Inject` callbacks (BEFORE/AFTER the same call)
  that temporarily point the armor mesh at its fitted buffer. Whatever draws next
  (stock code or Character Creator's redirect) renders the fitted buffer.
- `armorpk.fit.mixins.json`: `required: false`, `defaultRequire: 0`; the RenderList
  hook is `require = 0`. A missed hook disables fitting instead of aborting startup.
- Plugin version 3.0.2; `mod.info` `version`/`modversion` 3.0.2.
- Character Creator is unchanged.

## Validation

Compiled with javac 25 against PZ 42.22.2 and FJL agent classpath; jar listing verified.
Per owner request, no in-game or launch test was run.

## Assets

Release tag: `mod-assets-2026-11-21-armorpk-3.0.2`.

| ZIP | Bytes | SHA-256 |
| --- | ---: | --- |
| ArmorPK-v3.0.2-part1.zip | 1769466292 | `27e61c2955b6bf59343aa92a643f577c6fcd627609afc24d3ca80d042ee7e836` |
| ArmorPK-v3.0.2-part2.zip | 1887408495 | `6600a5777aa57bfbb40542683bb1e60e4c2794007ca6a8d822022399d3f304b4` |
| ArmorPK-v3.0.2-part3.zip | 22074497 | `509bfe054e731443ac701e150b238fa8bab014be6d482abdba4b27ab926f0577` |

Part1 is the 3.0.1 part1 with only `42/mod.info` and `42/java/ArmorPK.Fit.jar` replaced
(all other entries CRC-identical). Parts 2 and 3 are byte-identical to 3.0.1.
Uncompressed bytes: 3795573221. Required free bytes: 8011393417.

Main and Faded Realms rows updated. Outback Steakhouse stays on 2.2.1 (it was not
moved to 3.0.x and 3.0.x requires Build 42.22.2).