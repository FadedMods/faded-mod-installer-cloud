# Echoes of Humanity 0.12.3 crash hotfix deployment

Completed at 2026-09-22T04:48:17.639086+00:00. [Published release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-22-echoes-0123). Catalog commit `3fec8dbbe56ba7eeb635833be31062d3803a9ce6` changes Echoes only in Main and Faded Realms. ID sets and other entries remain intact. Manifest validation and CodeQL passed.

## Crash diagnosis and repair

The local 0.12.2 session first exits gameplay at frame 141812 with `UnsupportedOperationException` in `PZArrayList.iterator`, called by `NpcRosewoodCommunity.claimed` during native micro-faction home selection. B42's square-object list permits indexed access but intentionally rejects ordinary Java iterators. The claimed-home scan and both community fortification scans now use the existing indexed adapter. Player-built objects, generators and barricades retain their occupation protection.

During the resulting shutdown, the KillCell callback attempted a second NPC save after B42 had reset GameEntityManager. Restoring a transient held weapon then threw through the serializer's cleanup and interrupted world exit, leading to repeated UI, weather, lighting and save errors against torn-down systems. The late callback now discards runtime ownership without saving again. Normal OnSave runs earlier; its valid snapshot is preserved.

The log's earlier clothing extra-action errors (`IsClothing`/`getVisual` on null) are not established as the cause of this exit and are not claimed fixed. The previous hunter-render repair remains included.

## Verification

- Reproduced the unsupported iterator using the installed game's actual PZArrayList and square object scan. Empty/ordinary squares and protected construction/generators now pass.
- Checked 4,195 compiled native methods for unsupported direct PZArrayList iterator calls and reviewed the square-object lists stored through the List interface.
- Verified actual B42 shutdown bytecode orders GameEntityManager.Reset before KillCell. The native persistence regression saves a survivor, then checks teardown when serialization is unavailable, unrelated-world callbacks, repeat cleanup and late save callbacks. Saved NPC table bytes remain identical. All 12 new checks passed.
- Full offline/native gate and isolated dedicated startup passed at `2026-09-22T04:37:52.9784009Z`. Connected multiplayer gameplay is not claimed as tested.
- Public installer clean and existing installs passed with FJL ready. All 990 public, local and OVH files match the staged archive byte-for-byte; remote files have the correct server ownership.
- ZIP SHA-256: `67915eaaccbc09d58bda38ff02d2891e9a64c8a7244c3e0e77447621902b3929`. Existing installer 0.3.3 platform update entries remain verified; no installer rebuild is required for this mod hotfix.

## Publication and local copy

Canonical stage: `E:/Faded Mod Staging/EchoesOfHumanity`. Immutable release: `E:/Faded Mod Staging/EchoesOfHumanity-0.12.3-release`.

Local playable: `C:\Users\Luis\Zomboid\mods\EchoesOfHumanity`. Exclusive JAR access was checked; previous installation preserved at `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\EchoesOfHumanity_20260922_004038`. Existing profile unchanged; FJL reports READY.

Updated Downloads PDF: 40 pages, 68 bookmarks, 173 verified internal links. PDF and Discord post public bytes match their local originals.

## OVH

Fresh zero-player heartbeat, active service, free backup lock and sufficient disk checks preceded the authorized protected backup/update/restart. Verified backup `project-zomboid-20260922T044203Z.tar.zst`: 13,201,861,225 bytes, SHA-256 `cc2688d05cee582307a5e69187460142749ebd58cc6b779641fbbd45c1daa16f`.

ServerSync installed 0.12.3. GAME_READY, completed WorldDictionary, SERVER STARTED, both game UDP listeners, zero crash restarts, unchanged enabled mod IDs, fresh online heartbeat and the expected Nexus package hash all passed. No world save or NPC-data deletion was performed.

## Interfaces and evidence

Campaign API 3, community extension 1, multiplayer authority, network contracts and save schemas are unchanged. Clients should refresh Installer 0.3.3, update and fully restart the game; no save reset is required.

Evidence remains local in `build/log-review-0123/`, `.test-work/hunters-0123/` and installer `.test-work/echoes-0123/`. Raw user logs and server access details are not published.
