# Portable ZIP repair — 2026-08-30

Four release archives were created by a Windows ZIP writer that stored `\` in
both the local file headers and central-directory entry names. Windows tools
silently normalized those names, but Java/Linux streaming extraction treated
them as literal characters and could not create the expected mod directory
tree.

The payloads were repacked without changing any file content, mod ID, or mod
version. Per-entry names, sizes, and CRCs were compared before publication.
The replacement archives use `/` in both ZIP indexes and Unix-compatible ZIP
metadata.

Release: `mod-assets-2026-08-30-portable-linux-repair`

| Mod | Version | Rejected SHA-256 | Portable SHA-256 |
|---|---|---|---|
| Faded Java Loader Bridge | 0.3.8 | `626333c10c4f4e0ae5b85805f610e746394bee213472adb33bced23bb5234361` | `640b9a912bc38def57e3f1359d3376a406a665143f35cfb27aec88bac741a8bc` |
| I Sync, You Sync, We All Sync For DeSync | 1.1.9-b42.20.4-fpse | `db1fe13f17d8ec2cc445b0976b90198235287f98e6d15b733dc504900170a3a8` | `16f2f0bac9f6773ac44fd2ae89e500af20b89e5b5e78e1c7620a807e175cee2a` |
| F.A.D.E.D Nexus | 0.4.0 | `1cc23f0558909f31d6cd68bf4eef167defc35661568205daacf2daea0a07e922` | `2acbd4c8c5e52a5d8f5729cb3c4863b3014dc73bcf867a73a11b22814d60caea` |
| F.A.D.E.D Nexus // Survivor Pulse | 1.1.2-nexus.2 | `060acbccc8f57dcd19a22bb57ff997930cf3fcd76c919d4f8f1b000a71a52729` | `0b25e7dd0e1fd453019925ed026e5696cb42d50756b225ab72b83870e4058d43` |

Both public manifests were updated where they referenced an affected asset.
The four rejected hashes are quarantined by `scripts/validate_manifests.py` so
they cannot be reintroduced accidentally.
