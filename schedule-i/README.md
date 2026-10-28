# Schedule I / FadedCore catalog

The stable URL remains `schedule-i-manifest.json`. FadedCore 0.4.1 MP-actions RC uses
production signatures and the existing publisher key. Its SDK remains a separate
developer preview; players do not need that ZIP.

Installer 0.3.20 or later is required for helper 0.4.0, signed minimum-runtime
fields and PNG/PCM WAV/textured mesh admission. API 1/2 and SDK assembly identity
remain compatible. Mods using the new replicated NPC/request/action services
declare minimumRuntime 0.4.1 on every peer. The compiled runtime and frozen SDK
retain internal 0.4.0 identities; distribution suite 0.4.1 distinguishes the update.

Installer 0.3.21 adds independently publisher-signed helper updates. Routine
framework, SDK, mod and compatible helper releases use this catalog without
another installer build. The signed helper descriptor binds contract 1, exact
.NET prerequisite, ZIP integrity and all three helper files. A catalog URL/hash
alone never authorizes executable code. Publisher trust stays pinned locally.

## Compatible catalog selection

The schema-1 root retains helper 0.3.1 and the existing 0.3 runtime/SDK entries so
published older clients keep working. Informational latestRuntimeVersion and
minimumInstallerVersionForLatest point to the latest supported selection.
compatibleCatalogs contains wrappers with minimumInstallerVersion and a complete
catalog object. New clients select the highest runtime compatible with their
installer and helper contract. Installer 0.3.20 uses its exact pinned helper;
0.3.21 can use a newer helper only after validating helper.signedRelease against
the installer's pinned publisher. Downloaded catalogs cannot replace that trust.

The modern full catalog is also at `schedule-i/0.4-manifest.json`. Its object must
match the corresponding compatibleCatalogs selection in the stable root. The
validator checks both and prevents accidental legacy-entry replacement.

When future helper variants share the same runtime major/minor, give each wrapper
an explicit `manifestPath` under `schedule-i/` to avoid mirror collisions. Keep a
complete older variant for existing clients and set the new minimum installer to
0.3.21. Helpers must retain command/response contract 1 and backward compatibility
with admitted generations. App UI, trust-root, platform or protocol changes may
still require an installer release.

```text
python scripts/validate_schedule_i_catalog.py schedule-i-manifest.json
python scripts/validate_schedule_i_catalog.py schedule-i/0.4-manifest.json
```

Each runtime/mod row has identity, version, immutable .fmod URL, byte length,
SHA-256 and declared compatibility/requirements. The signed .fmod remains
installation authority. The SDK ZIP has independently checked catalog integrity;
it is not an .fmod publisher signature. SDK owner license selection remains
required before a production SDK release; no first-party license grant is added.

## Publishing a mod

Create C# code against FadedCore.SDK.dll, compile using its build script, then
separately package/sign the clean output with the authorized publisher key.
Upload a new immutable .fmod and update the modern variant and mirrored full
catalog. Include minimum runtime/API/game/dependency requirements, version, size
and SHA-256. Compatible mods do not require rebuilding the installer/framework.
Missing dependencies are checked but not fetched automatically. The current
independent gameplay-mod list remains empty; unrelated Gang Life work is separate.
Never publish private signing keys, game binaries or private diagnostics.

Runtime upgrades retain existing admitted mod selections/startup settings; new
bundled branding/examples are not automatically added. Fresh 0.4 installs enable
local branding and keep gameplay/SDK acceptance disabled. The Online badge means
local readiness, not a multiplayer connection.

## Limits and preservation

Compatibility remains Windows x64, Steam app 3164500/build 25796331, all four
signed game hashes and registered Microsoft.NETCore.App 10.0.12, roll-forward
Disabled. Owned NPC network initialization/presentation and late-join/reconnect
paths are implemented in these new binaries. Connected multiplayer sessions,
full live-actor teardown and other documented gameplay boundaries remain
unqualified. Comparative performance remains partial. SDK RC3 remains an
unchanged developer preview; templates still mentioning 0.4.0 must be raised to
minimumRuntime 0.4.1 for mods using the new request/action services.

Install/update/remove uses per-user immutable generations; external data and
changed/unowned residues are preserved. Startup changes require restart; live
session controls are separate. No game files, saves or servers are publication
destinations. PZ catalogs/settings/FJL are separate.

For old development-preview migration, use original 0.3.18 to Remove successfully,
close both installers/game, preserve the ENTIRE remaining preview runtime folder
in a new separate backup, then let the new installer create a fresh default root.
Do not merge old component/history/state/journal metadata into production. Keep
all data; if old removal cannot finish, leave it intact and use support. Ordinary
production 0.3 to 0.4 upgrades use Update and preserve the installed mod selection.
