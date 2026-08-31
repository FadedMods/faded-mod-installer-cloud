# Never Survive Alone 0.5.2-alpha

Published 2026-08-31 as a focused Build 42.20 compatibility hotfix.

- Release tag: `mod-assets-2026-08-31-nsa-0.5.2-tag-api-fix`
- Asset: `NeverSurviveAlone-v0.5.2-alpha.zip`
- Size: `32322988` bytes
- SHA-256: `65b8fd697f278d5c768ef4acaedd540d2ece1d9c7759f94280531b2285f781f7`
- Uncompressed size: `36551910` bytes
- Required free space: `605745810` bytes

The hotfix replaces invalid `InventoryItem:hasTag(String)` calls in the NSA
Lifestyle layer. Project Zomboid 42.20 exposes that method with an `ItemTag`
argument, so unrelated worn clothing could throw while calculating scene
bonuses. NSA now reads custom string tags from the inventory item's tag
collection and its script item's tag collection. Regression coverage includes
the reported `Detail_Scar_Face` cosmetic and namespaced third-party tags.

Both `manifest.json` and `manifests/faded-realms.json` carry identical release
metadata. The ZIP was verified to use portable forward-slash entry names and
passed the installer's Build 42 preparation check.
