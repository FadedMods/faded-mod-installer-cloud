# CSR Optional FJL Manifest Repair

Date: 2026-09-05

Common Sense Reborn 1.9.67 and Common Sense Reborn Test 1.9.67 were incorrectly
published with `requiresJavaLoader: true` in the installer catalogs. That made
the installer label Faded Java Loader as a hard dependency, attempt loader
setup during a normal CSR install, and block CSR from the ordinary remote
server-upload path.

CSR itself was not broken. Both shipped `mod.info` files describe a standalone
Lua-capable mod with no dependencies, and the bundled hybrid JAR descriptor has
`required: false`. The Java layer supplies optional exact-build features such
as Staircast and multiplayer ragdolls and is auto-discovered when FJL is
already installed.

The main Production/Test entries and the Faded Realms Test entry now use the
legacy-safe optional declaration:

```json
"requiresJavaLoader": false
```

Installer-only Java fields were removed from these entries because legacy
installer clients reject the entire catalog when Java plugin fields accompany
`requiresJavaLoader: false`. No ZIP, JAR, version, digest, or playable mod file
changed. Current installers treat CSR as an ordinary mod, while the bundled
optional JAR remains available to FJL at runtime.

The manifest validator now rejects any future CSR Production/Test entry that
does not keep `requiresJavaLoader` explicitly false. Manifest validation and
the installer's manifest/Java-mod test suites passed before publication.
