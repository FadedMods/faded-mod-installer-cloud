# F.A.D.E.D Nexus 0.4.4

Published 2026-08-31 as the verified-pack restart hotfix.

- Release tag: `mod-assets-2026-08-31-faded-nexus-0.4.4`
- Main installer asset: `FadedNexusMain-v0.4.4.zip`
  - Size: `3176121` bytes
  - SHA-256: `51e56e2b4fd6ed379279c8f399b64f9b3b9b99c2d79ee07672e73b1d13594d01`
  - Uncompressed size: `3292917` bytes
  - Required free space: `543339950` bytes
- Full suite asset: `FadedNexus-v0.4.4.zip`
  - Size: `14655629` bytes
  - SHA-256: `03138fe34378c94c64db48bd8cc24f87b641dc70ee899217de35845c6ac9da95`
- Bridge JAR SHA-256: `4593c8a18b057f491fa0b47f3438a2c3b3029851ce3b56fc5d7a07a5b454aa1c`

The main and Faded Realms manifests now expose identical `FadedNexus` 0.4.4
metadata. `FadedNexus` was also added to the shared-release parity validator so
future updates cannot advance only one public manifest.

The staged handoff listed `543333310` required bytes. The published manifests
use the package tooling formula instead: compressed size + uncompressed size +
512 MiB, which is `543339950` bytes for this asset.

Both ZIPs passed CRC and portable-path checks. The main asset passed the local
installer's Build 42 preparation flow, and its embedded bridge JAR matched the
staged handoff hash. No production server was restarted as part of this client
catalog and local-play release.
