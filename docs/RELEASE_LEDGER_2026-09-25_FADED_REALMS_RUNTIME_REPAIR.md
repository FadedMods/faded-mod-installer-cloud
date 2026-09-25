# Faded Realms runtime repair - 2026-09-25

Release: https://github.com/FadedMods/faded-mod-installer-cloud/releases/tag/mod-assets-2026-09-25-faded-realms-runtime-repair

The existing Main and Faded Realms catalog URLs are unchanged. Membership/order
remain 123 and 69. Main CSR stays out of the owner's personal playable folder.
No installer binary, Java companion, sandbox rebalance or world reset is part
of this release. Existing FJL 0.4.4 performs the authorized server update on boot.

| ID | Version | ZIP | Bytes | SHA-256 |
|---|---|---|---:|---|
| BackToAtlanta_UI | 1.0.1 | BackToAtlanta_UI-v1.0.1.zip | 70853628 | b8df9fda4cf786484a24e6dc7884ff3299a788ce7a85a0415797bd0eb4079a55 |
| CommonSenseReborn | 2.0.6 | CommonSenseReborn-v2.0.6.zip | 64537105 | aa110c1bbfe721aaa2d638ca565f2e1498f86b4c3dd7aaacb2ec2b6ea3a25fef |
| CommonSenseRebornTest | 2.0.6 | CommonSenseRebornTest-v2.0.6.zip | 67676087 | 0ba72895b4f8b0dbd4cd03cea25de04dfe1d0fa41f5264c1aa518d33832bfbd0 |
| FadedFarmingFishingReborn | 0.4.1-b42.20.4 | FadedFarmingFishingReborn-v0.4.1-b42.20.4.zip | 211239410 | 5d62c59f8853e613fc5eb42ba0794232dfcebe4160b222b5341760e07794a840 |
| FadedsClearViewUI | 0.6.19 | FadedsClearViewUI-v0.6.19.zip | 4785850 | f52466a810c79d5864ef444aeae8b2a661bbf8eea9d684c60eb77bb07496f7e0 |
| ProjectFadedCar | 2.5.5 | ProjectFadedCar-v2.5.5.zip | 225180793 | 5daf60c28a14377d6ace508939672a9b9e350242c79a96112ffe2bf05f4601eb |
| SentryNet | 0.1.0-alpha.4 | SentryNet-v0.1.0-alpha.4.zip | 41598573 | c4a72fd96525152320cb9bccb1b5de933ef681d66bb55be0acacafc38bf4263f |

## Repairs and evidence

- PFC plow generation no longer creates partial vehicle types in the wrong
  module. Native B42.20.4 registry audit with all 69 script packs: 776 entries /
  387 model-less before; 389 entries / zero model-less after. All 12 ModernEVs
  scripts already have bodies. New compatibility applies only to real loaded
  models, is idempotent, and never calls Loaded twice.
- PFC 89 Python tests, 30 Lua smoke suites, syntax, registry, tiledefs and sync
  dry run pass. All 84 lift-related files/Java binaries match the old installation.
- CSR density removes unavailable Kahlua `next` calls (316 regression assertions).
  NPC head-hit feedback now targets network players only; NPC damage is preserved.
  Outline ownership (83), branding (21) and inventory compatibility (24) pass.
- CSR Test's alpha-preserved map mark is text only, displayed 252x84:
  Faded Realms: / Season 3 / The Walking Dead. No illustrated banner.
- ClearView restores FAM Heart/native Skills routing (261 assertions), adapts
  the authorized PZ Modern UI 0.13.2 map geometry by Codex and Baxter (Workshop
  3787349247), and retains native map input/data plus Faded overlay callbacks.
  Full gate: 1723 checks, 206 Lua files, 244 requires; isolated native startup
  and clean shutdown pass. Canonical staging now retains THIRD_PARTY_NOTICES.md.
- Farming corrects InventoryContainer:setWeightReduction. High configured
  reductions and saved-cart restamping remain; full gate plus native standalone,
  CSR Main and CSR Test smoke modes pass on 42.20.4 revision b0bbce05d5.
- SentryNet uses getPartCount/getPartByIndex and guards unloaded actor state;
  full verify, 55 native model imports and camera checks pass.
- TWD reasserts at most eight selected highlights between existing six-tick
  discovery scans; cleanup preserves foreign ownership. Outline regression and
  validator pass (eight pre-existing unrelated protected-call warnings).

All seven archive CRC, safe paths, metadata, SHA-256 and installer preparation
checks passed before publication; GitHub's public asset digests match. Fresh
public-download/local-install receipts are retained by the release operator.

## Acceptance limits

These gates do not prove graphical appearance, stable FPS, native loot transfer,
TOC item grants, teleport or Echoes intelligence delivery in a joined client.
The incident server stopped advancing its world frame for roughly 15 minutes;
the log does not prove which component stalled it. Restart and gameplay checks
are required. One saved invalid PFC vehicle type has a separately reviewed,
backed-up single-record migration; no blanket vehicle deletion or world wipe.
