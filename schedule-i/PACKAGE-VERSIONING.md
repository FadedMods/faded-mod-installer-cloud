# Schedule I package versions and SDK compatibility

This guide describes the first public Gang Life release and its matching framework.
The stable Schedule I catalog URL remains unchanged:

`https://raw.githubusercontent.com/FadedMods/faded-mod-installer-cloud/main/schedule-i-manifest.json`

## One framework, independently updated components

FadedCore suite 0.4.2 updates the existing framework installation in place. Gang
Life 0.2.0 is a separate signed mod for that framework. Players do not install a
second loader, and this component release does not require another installer
update. The existing helper 0.4.0, publisher key and trust descriptor are unchanged.

| Component | Release identity | Purpose |
| --- | --- | --- |
| Framework suite | 0.4.2 | Signed distribution version for the frozen RC6 runtime payload |
| Compiled runtime/SDK | Internal 0.4.0 identities retained | These labels alone do not distinguish RC3 from RC6 capabilities |
| Developer kit | `0.4.0-ganglife-mp-actions-rc6` | Matching SDK DLL, source, examples and authoring tools; developer preview |
| Package helper | 0.4.0 / contract 1 | Verifies packages and composes immutable generations |
| Gang Life | 0.2.0 | First independently published gameplay mod; requires suite 0.4.2 |

Public downloads:

- [FadedCore 0.4.2 and matching RC6 SDK](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/schedule-i-fadedcore-0.4.2-ganglife-rc6)
- [Gang Life 0.2.0](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/schedule-i-ganglife-0.2.0)

Every host and joining player needs the matching runtime and Gang Life packages.
Update the runtime first, then install the mod with the game closed. Refresh the
existing Schedule I catalog after publication. Missing package dependencies are
refused rather than downloaded automatically. Players do not need the SDK ZIP.

## Feature floor and required distribution are different fields

The frozen RC6 managed loader accepts an inner mod manifest `minimumRuntime` no
higher than 0.4.0. Raising that field to 0.4.1 or 0.4.2 would make mod discovery
refuse the mod even if the package helper had installed it successfully.

Preserve the reviewed Gang Life DLL, assets and inner manifest. Its inner
`minimumRuntime` and the signed outer `mods[].minimumRuntime` remain 0.4.0. The
required distribution is enforced separately in the signed package envelope:

```json
{
  "packageDependencies": {
    "fadedcore.suite": "0.4.2"
  },
  "mods": [
    {
      "id": "faded.ganglife",
      "version": "0.2.0",
      "minimumRuntime": "0.4.0"
    }
  ]
}
```

This is an excerpt, not a complete package manifest. The helper compares the
installed suite's signed outer version with `packageDependencies` before it
activates the composed runtime/mod generation. Suite 0.4.1 and earlier must
refuse a mod requiring 0.4.2. The catalog must describe the same package
requirement; catalog text alone does not replace the signed dependency.

For the approved mod output, pass `--runtime-min 0.4.2` to the existing package
helper's `pack --kind mod` command. This sets the signed suite dependency while
retaining the input inner mod manifest's 0.4.0 feature floor. Use the authorized
protected signing key and independently trusted production descriptor, then
verify the new package's metadata and signature. Never overwrite an existing
frozen artifact or publish private signing material.

The suite's 0.4.2 envelope identifies the new runtime distribution; its frozen
compiled payload remains the reviewed RC6 bytes. Runtime upgrades preserve
existing selected mods, startup settings and mutable data. They do not
automatically install Gang Life or add previously unselected bundled examples.

## Compile against the matching SDK

The SDK assembly identity and API 1/2 numbers are retained, but RC6 has a concrete
method-signature change: `OpenPhoneMap()` now returns `bool` instead of `void`.
The result reports native map readiness so callers can retry cooperatively.
An older compiled caller is not guaranteed to bind to the new method merely
because the assembly version is unchanged.

Authors using an older SDK should refresh the project reference from the RC6
kit, adapt their map-opening calls, recompile and qualify the resulting package
against suite 0.4.2. Gang Life's approved build already uses the matching SDK.
There were no independently published gameplay mods before this first Gang
Life release; do not imply a wider existing-mod compatibility guarantee.

The SDK ZIP retains internal version `0.4.0-ganglife-mp-actions-rc6` and remains
a developer preview (`productionEligible: false`). Its inventory and download
hash identify its exact bytes. They are separate from the `.fmod` publisher
signature and do not add a first-party license grant.

## Publish through the existing catalog

Freeze and verify the runtime, mod and optional SDK artifacts; upload their exact
bytes to immutable releases in `FadedMods/faded-mod-installer-cloud`. Verify
actual public transfers, lengths, SHA-256 values, package signatures and complete
payload inventories. Add or update their rows in the modern full catalog and
its compatible selection/mirror, including the signed suite dependency.

Preserve the legacy root catalog and older compatible variants. Older installers
continue selecting their supported helper/runtime entries; modern installers
select the updated complete Schedule I catalog. Unrelated PZ catalogs, loader
flows, servers and Workshop content are outside this release.

Installer 0.3.20 supports the unchanged helper 0.4.0. Installer 0.3.21 also
authenticates compatible future helper releases against its pinned publisher
key. A compatible signed helper may declare a reviewed exact .NET prerequisite
without another installer build. A different command protocol, trust root,
platform, dependency layout or installer UI can still require an app update.

Publication and artifact checks do not establish connected multiplayer gameplay
or measured performance. Record exact-binary test scope separately; the user's
accepted assumed-working/reactive-fix policy does not turn unobserved behavior
into a measured result.
