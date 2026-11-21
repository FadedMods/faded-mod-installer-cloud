# Release ledger: Knox Reborn Lite 0.5.2

Date: 2026-11-21. Owner-authorized hotfix.

## Problem

Multiplayer clients on 42.22.2 hung on the load screen right after connecting to Faded Realms. `MapSpawnSelect.lua:362` (`fillList`) called `GameMode.get(ResourceLocation.of(getCore():getGameMode()))`. On 42.22.2 `getCore():getGameMode()` returns a `GameMode` object, so `ResourceLocation.of` threw `java.lang.RuntimeException: expected argument of type String, got GameMode` from `OnConnected` and the spawn list never populated.

## Fix

- `fillList` now compares `getCore():getGameMode()` directly with `info.only_for_game_mode` (as vanilla 42.22.2 `MapSpawnSelect.lua:479` does), with a `tostring` fallback in case either side is a string.
- No other `ResourceLocation.of(getCore():getGameMode())` uses exist in the mod.
- `42/mod.info` `modversion` 0.5.2. Java plugin `knoxreborn.hybrid` unchanged at 0.5.0.

Only `42/media/lua/client/OptionScreens/MapSpawnSelect.lua` and `42/mod.info` differ from 0.5.1 (24155 payload files, all others hash-identical).

## Validation

`luac -p` (Lua 5.4) parses the changed file. Packaged with the installer's `package_local_mods.py` helper (ZIP CRC test passed). Not yet tested in game.

## Assets

Release tag: `mod-assets-2026-11-21-knox-reborn-lite-0.5.2`.

| ZIP | Bytes | SHA-256 |
| --- | ---: | --- |
| KnoxReborn-v0.5.2.zip | 1790932719 | `3e2af2062b7a2d17b1c2558c3fb7b99cb82f2bc293e1037d9dff6a0e081a87f8` |

Uncompressed bytes: 6648294789. Required free bytes: 9104056986.

Main and Faded Realms rows updated.
