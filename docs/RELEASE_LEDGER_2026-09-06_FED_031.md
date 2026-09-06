# Faded's Error Detected 0.3.1 release ledger

- Release: `mod-assets-2026-09-06-fadeds-error-detected-0.3.1-portable-root`
- Asset: `FadedsErrorDetected-v0.3.1.zip`
- Size: `591906` bytes
- SHA-256: `327e34a22ed1f943d0a294015097c9ccb3ffe5ccaee4330816e9237efc603ac4`
- Installed payload: `698857` bytes across 19 files
- Project Zomboid target: `42.20.4`
- Optional Java plugin retained: `faded.fed.performance` `1.0.2`, server-only

This release corrects the 0.3.0 archive-layout defect that caused FJL on Linux
servers to install the Workshop-only `Contents/` hierarchy as `/mods/Contents`.
The 0.3.1 archive has exactly one `FadedsErrorDetected/` top-level directory,
exactly one `FadedsErrorDetected/42/mod.info`, forward-slash entry names, and no
`Contents/`, traversal, source, Gradle, build, or distribution paths.

The source-owned release packager enforces these invariants. Lua diagnostic,
Escape-menu, and alert-button regression suites passed. Gradle 9.6.1 clean
build, tests, performance self-test, protected-class audit, and plugin install
passed against Project Zomboid 42.20.4. The desktop installer independently
prepared the archive as `FadedsErrorDetected` before publication.

Both the main and Faded Realms manifests were changed surgically from 0.3.0 to
0.3.1. No mod IDs, ordering, or unrelated catalog entries changed.
