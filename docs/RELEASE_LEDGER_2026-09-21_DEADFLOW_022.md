# Deadflow 0.2.2 deployment — September 21, 2026

Completed and verified 2026-09-21T14:42:07.866504+00:00. [Immutable public release](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-21-deadflow-022). Catalog commit `aae97be8f9cca6027b013f2f6e366a2880e01098`. The normal Main URL serves 0.2.2; both catalog workflows passed. Deadflow was already present in Main and enabled on OVH. It is absent from the separate Faded Realms installer catalog, which remains unchanged. Other catalog entries, loader channels and the OVH enabled-mod list are preserved.

## Repair

Reproduced the exact missing-DeathMixin refusal with PZOpt. Its collision override failed Deadflow's original-class hash check; Mixin swallowed the config-selection exception, obscuring the original cause. The fix accepts only the reviewed collision class and four matching companions, retaining stock checks and native-library fingerprints. Unsupported overrides remain refused with the original class-specific reason. No third-party engine classes are bundled or installed. Population API 2 and existing Deadflow save format are unchanged. FJL stays 0.4.1.

## Validation and delivery

- Core ledger 19 cases; production population conservation/restart/corruption regressions; exact hook/native audit; compatibility rejection/cause tests passed.
- Collision ABI/field/ordered-effect audit passed. PZOpt releases 1cf5080 and c69c085 have identical reviewed collision and worker binaries. Bytecode branches differ from stock because of recompilation; no blanket compatibility with future releases is claimed.
- Four real FJL client/server bootstrap combinations (stock/PZOpt), with Echoes 0.9.0 and FadedStack, passed with all 42 native population boundaries replaced. Two deliberately modified class fixtures remained refused with accurate diagnostics.
- A disposable three-start native dedicated-world test retained population identity, health, inventory and adapter state; counted a zombie death exactly once; and prevented dead-member replay after restart.
- Packaged Installer 0.3.3 passed clean installation and backup/replacement against the public asset, with FJL READY, correct B42 bridge metadata and identical payloads.
- Public ZIP: 2,558,691 bytes; SHA-256 `3acc9013198994abb9258f619d4df60c0a3ef5fe5df8ec902179f7862e00376c`.
- Java JAR SHA-256 `3f05a05840ce6b35a4102aec84b7f89bc39225775ef3148ff7d26e7617f9f394`. All 19 installed files match the ZIP locally, in both staging locations and on OVH; remote ownership verified.
- Local update created a rollback backup at `C:\Users\Luis\AppData\Roaming\FadedLocalModInstaller\backups\Deadflow_20260921_103518`. Canonical staging is `E:/Faded Mod Staging/Deadflow`; immutable release staging is `E:/Faded Mod Staging/Deadflow-0.2.2-release`. Previous canonical staging was preserved separately.
- OVH restarted through the protected zero-player backup procedure. Verified backup `project-zomboid-20260921T143615Z.tar.zst`, 13,168,021,717 bytes, SHA-256 `1fc0943eb5164e58124ddee276efdc90039d3f9d3316147f91d62368d7c6831a`.
- Service active since Mon 2026-09-21 14:39:15 UTC; fresh online heartbeat, FJL GAME_READY, completed WorldDictionary, SERVER STARTED and both UDP listeners verified. No crash restart or checked fatal signature. ServerSync changed only Deadflow; Nexus advertises the exact 0.2.2 artifact.

Receipts are retained locally under installer `.test-work/deadflow-022/` and Deadflow `build/compatibility-3dhs9rqn/`, `build/engine-lab/20260921-102937/`. Existing modified and untracked source work was preserved. The reporting user's complete mod set and live playthrough were not available; no such acceptance test is claimed.
