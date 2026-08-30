# 2026-08-30 PFC and ClearView release ledger

Manifest commit: `1e0a160c9be9395d026077e4518fcb4618f831a8`

| Manifest ID | Version | Release | Asset | SHA-256 |
|---|---:|---|---|---|
| `ProjectFadedCar` | 2.1.5 | `mod-assets-2026-08-30-pfc-2.1.5` | `ProjectFadedCar-v2.1.5.zip` | `616313bb6d3176f68199e91df2e256bb0d7ea06c91cb3eef53dc634dd273fdd6` |
| `FadedsClearViewUI` | 0.6.14 | `mod-assets-2026-08-30-clearview-0.6.14` | `FadedsClearViewUI-v0.6.14.zip` | `c81a71191548959afd22dfe15aa0bef22173db821d931095a1ba6c0d9a85fe76` |

Main and Faded Realms carry identical metadata for both entries. The public raw
Main manifest was parsed after the push, and both assets were downloaded and
prepared through the installer. Both archives use portable forward-slash names
in the central directory and local headers.

PFC 2.1.5 repairs B42.20.x Java `Set` traversal in fleet tire authority and
prevents the server authority from registering on MP clients. ClearView 0.6.14
publishes the validated UI ownership candidate and adds automatic single-owner
nametag fallback whenever vanilla multiplayer names are enabled.
