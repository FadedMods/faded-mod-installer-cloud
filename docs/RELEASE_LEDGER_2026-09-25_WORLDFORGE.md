# World Forge public preview and Installer 0.3.6

Published releases:

- [World Forge 0.1.0-preview.1](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/worldforge-0.1.0-preview.1)
- [Faded Local Mod Installer 0.3.6](https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/faded-local-mod-installer-0.3.6)
- [World Forge product page](../products/worldforge/README.md)

## World Forge

The Windows x64 portable ZIP includes the native desktop editor, bundled .NET
runtime, command-line executable, stdio MCP server, 82 prefabs, 28-page PDF guide,
Markdown documentation and third-party notices. Game texture packs, original map
files, API keys and local user settings are not included.

The ZIP is 67,122,704 bytes, SHA-256
`9495e1bdb353877a44c4b45c86e2dfdc24823b4147fdac5ae27e3c8cf051821f`.
The PDF is 8,801,773 bytes, SHA-256
`e712993223807793a434ad3498d588084ac7b1f8f957b078a254135a13935071`.
Both public downloads were retrieved without authentication and matched their
local release files exactly.

The guide has 26 chapters, 27 bookmarks and 87 links, with no layout overflow,
blank pages or invalid internal destinations. It covers manual editing, vanilla
and mod-map workflows, B41 conversion, optional AI viewport sight, sprites, model
adapters, import/export, troubleshooting and attribution.

Verification includes the previously passing 517 editor tests and native desktop
smoke coverage, plus the actual portable runtime: AMD64 executables and native
dependencies, exact custom pixels through Skia, SQLite create/validate, MCP
initialization and 99 tools. Every one of 451 staged-file hashes and 452 ZIP
entries matches. This does not certify in-game load or multiplayer export behavior.

## Installer

Source commit: `f67b0d054386bbf438c0f400e5392ede972dce68`.
All six installer variants come from that source, with 160 tests passing.
Native Linux CI run `36184025918` and native macOS CI run `36184025894` pass.

World Forge's new tab sits immediately beside Nexus and includes real editor
captures, direct ZIP/PDF links, capabilities, quick start, copyable AI prompts and
preview scope. The existing Nexus shortcut still selects Nexus.

Archive verification caught a missing-image Linux packaging defect before
publication. The Linux spec now includes the complete application asset folder,
and both build scripts compare every frozen PNG/ICO with source before packaging.
The repaired tarballs contain the exact editor screenshots and Workshop artwork.

All eight archives pass size/hash checks, safe member/link paths and ZIP CRC or
gzip integrity checks where applicable. Windows, ELF and Mach-O architecture
headers are correct. Frozen modules contain version 0.3.6 and the expected World
Forge URLs/actions. Mac ZIPs and DMGs match native CI checksums; native jobs check
ad-hoc signatures and DMG integrity. Windows packaged CLI startup passes.
All eight published archives were then downloaded without authentication and
matched their final local size and SHA-256 before the app update feed was advanced.

The app update feed preserves its seven platform keys: Windows, multilingual
Windows, standard Linux, Steam Deck, Apple Silicon, Intel Mac and the existing
Apple Silicon `macos` compatibility alias. No mod catalog or server pack was changed.

World Forge itself remains a **Windows x64 public preview**. The guide documents
remaining saved-world reconstruction, complete real-world generation and game
acceptance limits. KnoxMap and ZomboSlicer attribution ships in both program and PDF.
