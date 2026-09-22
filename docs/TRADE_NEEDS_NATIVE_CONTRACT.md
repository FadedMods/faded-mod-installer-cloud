# Native trade needs - Echoes 0.13.0

Introduced in 0.13.0 and unchanged in 0.13.1. The 0.13.1 client keeps needs/feedback in a fixed, clipped scroll viewport; no interface or authority change is required for that layout fix.

Campaign API 3 and community extension 1 are unchanged. These additions use the existing authenticated `EchoesOfHumanityNpc` interaction/trade transport; existing fields and original Java public/protected members remain available.

## Conversation and transactions

`Choice {npcId, choice="needs", requestId}` first validates the ordinary conversation, then establishes a trade session through the native `trade` choice. An accepted result adds `needsGuidance=true` and `needs`, with an `open_trade` follow-up. `TradeOpen` still requires that session. `TradeCommit` accepts only original player/NPC inventory item IDs; no client-supplied quantities, needs, prices or standing are trusted.

`TradeOpen` and `TradeCommit` results add:

| Field | Meaning |
| --- | --- |
| `needs` | Array of current shortages, each `{key, missing, target, unit}`. |
| `playerItems[].needed`, `npcItems[].needed` | Whether that actual object satisfies a current shortage. |
| `playerItems[].needKey`, `npcItems[].needKey` | Supply category, or empty string for unclassified items. |
| `feedback` | Empty on open; `trade_complete`, `aid_received`, `aid_cooldown` or `gift_received` after success. |
| `reputationDelta` | Actual personal standing change in this transaction. |
| `factionReputationDelta` | Actual standing change with the NPC's current faction, including a micro-faction. |

Need keys are `water`, `food`, `medical`, `ammo`. Units are `litres`, `meals`, `dressings`, `rounds`; a meal-equivalent is 0.1 native hunger reduction. Targets are 1 L, 3 meal-equivalents, 2 dressings, and 6-30 compatible rounds when a usable carried ranged weapon is available. The equipped weapon is preferred and rounds already loaded are counted. This is carried personal inventory, not communal storage or fabricated settlement reserves. Ammo boxes must be unpacked; empty magazines do not qualify. Matching rows sort before ordinary merchandise.

An unfair offer includes refreshed inventories and needs with `accepted=false`, `reason="unfair_offer"`; nothing moves. Existing session, connection, range, hostility, danger, custody, protected/private gear and local arms-law gates remain. Personal necessities may be offered to specialty merchants alongside their usual accepted goods, subject to the same law and item gates. Existing ordinary fair-trade rewards and colony contribution accounting remain separate.

## Authority and persistence

Prices use actual condition and existing commerce rules plus a 0-50% shortage bonus on both sides. NPC sales of usable supplies include a 1.75 vendor multiplier before the existing reputation/law exchange ratio. This spread exceeds maximum stock-price fluctuation even with the ordinary trusted-customer discount. Non-supply equipment pricing is unchanged. Every open/commit computes demand from inventory; there is no new per-frame scan, worker job or request/poll loop. While an idle window is open, reopen/refresh to observe outside changes; a commit always revalidates.

Only a player-only transfer can claim aid reputation. Native original-object transfer/rollback completes first. Credit is capped by pre-transfer shortage and requires at least 10% of a normal reserve; useful aid earns 2-6 points. `EchoesOfHumanity.TradeAid.v1` global mod data stores the latest reward time for each length-prefixed player/faction key. It enforces a rolling 86,400,000 world-millisecond cooldown and rejects clock rollback. Native global mod-data saving preserves this ledger. Useful donated objects carry `EOH_UsefulAidDonated=true` in their persisted item mod data; buying back or returning them cannot earn aid twice. No new NPC save schema or reset is required.

Requests transfer whole original objects. Player items must be in main inventory; favorited/equipped items and private/protected equipment stay excluded. Capacity checks use net transferred weight, so an already overburdened player can still donate. Stock disappears only through existing physical transfer/consumption. Receipt feedback never substitutes for an actual inventory change.

## Read-only supply integration

`EchoesOfHumanityNpcLuaBridge.tradeSupplyInfo(InventoryItem)` returns `{cleanWaterLitres, safeFoodMeals}` using the native classifier. It accepts a null item and returns zero values. It changes no inventory, character stats, reputation or world state. This is useful for campaign/companion supply UI; it is not authorization for a trade or donation.

Clean water requires positive finite contents consisting solely of clean Water and/or CarbonatedWater, without taint/poison. Food requires edible hunger reduction, without spoilage, poison, freezing, burning or dangerous uncooked status. These checks also gate ordinary NPC inventory water/food selection, so unusable supplies cannot satisfy a request on paper then stall consumption.

## Verification

`tradeNeedsRegressionTest` executes real dialogue/session and native trade commits with real inventory objects, plus shortage, price, authority, replay, cooldown and micro-faction standing checks. `test-trade-needs.lua` executes actual client methods in stock Lua and PZ Kahlua. The isolated dedicated smoke checks real vanilla B42 water containers, clean/tainted/contaminated contents and poisoned food. Full release validation includes existing transfer, damage, corpse, save, ABI and package checks. No connected-player visual playthrough is claimed.
