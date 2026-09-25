# Outback Steakhouse catalog

Retired by the owner on September 25, 2026. Installer 0.3.5 removes its
button, tab and built-in source and migrates existing selections to FadedMods.
Automatic catalog synchronization is disabled; the last published catalog
remains available for historical clients. Do not update or restart the server.
The workflow can only run on explicit manual dispatch.

## Historical setup (0.3.4)

Installer 0.3.4 adds a built-in Outback Steakhouse channel at:

https://raw.githubusercontent.com/FadedMods/faded-mod-installer-cloud/main/manifests/outback-steakhouse.json

Authority: the public Nexus pack for world `78c689b5-d7a0-49e7-9c2f-b50753098c48`:

https://network.fadedmods.com/api/v1/worlds/78c689b5-d7a0-49e7-9c2f-b50753098c48/pack

The initial catalog contains 59 required entries from pack
`2026.09.25.1-outback-full`, ID `ee93ebe2-d258-480d-8f56-7ba2e4adcc17`, hash
`6058873f50d341d3d30bba1547702130c19f2db912599b1e25d9f0261530ba64`, with FJL 0.4.4.
It includes the exact versions, server IDs, artifact hashes and load order.
Do not copy Main's latest versions over this catalog while Nexus pins an older pack.

The `Sync Outback Steakhouse Nexus catalog` Actions workflow runs after Main
catalog changes, on manual dispatch, and on a ten-minute schedule (GitHub may
delay scheduled jobs). It resolves current entries first, then historical
immutable release entries from the cloud repository's full Git history.
No login or server credentials are used. Unknown, quarantined or mismatched
artifacts fail the job before writing. A failed request preserves the last
published catalog. If Nexus changes during resolution, the job fails and a
later run retries. Concurrent catalog commits cannot be force-overwritten.

Manual sync from a full checkout:

```text
python -m unittest discover -s scripts -p test_sync_outback_catalog.py
python scripts/sync_outback_catalog.py
python scripts/validate_manifests.py
```

Review and commit only the generated Outback catalog. Changing this catalog
does not enable mods on a server or alter the Faded Realms player list.
The installed app keeps its normal signed loader and hash-verified download
workflow. Players click Outback Steakhouse, All Mods, clear the search,
Select Visible, then Install Queue. Future pack updates need a list refresh,
not a new installer release.
