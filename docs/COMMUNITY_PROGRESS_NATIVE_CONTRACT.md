# Community activity and capacity — 0.13.3

Campaign API 3 and community extension API 1 are unchanged. No FFO changes are required.

## Routine ownership

Authority schedules one loaded community per real-time second in round-robin order. Each group rotates its first worker, scheduling at most one job (or one two-person conversation) per visit. Dormant/extinct groups do not occupy work slices. Demographic updates retain their three-second cadence. Runtime cursors reset safely on world changes.

Community availability permits native unique residents and reduced simulation, while refusing forced goals, custody, combat, radio calls, conversation/trade ownership, companions, missions, campaign jobs, self-preservation, traversal, journeys, vehicles and critical hunger/thirst. Ordinary faction routines exclude micro-factions. A queued runner is not idle and retains its lease. Existing finite movement/action deadlines remain enforced.

Failed community movement clears the failed destination and selects a nearby safe point for a bounded native-path recovery attempt. Success clears recovery. This cannot pass an impassable wall, teleport a body or create missing resources; blocked buildings may require environmental interaction or a usable exit.

## Capacity

`EchoesOfHumanity.MicroActivePercent`: server sandbox integer, 10–50, default 33. Admission ceiling is floor(maximum materialized agents × percentage / 100). Living valid community bodies count, including legacy unique Rosewood residents. Checked on simulation promotion and actual native spawn/restore. Main factions are not subject to the community sublimit; their existing total body and cohort checks remain. Visible community bodies are never evicted by the new gate. Recruited companions retain priority. Extremely small total limits can round community seats to zero.

New founding/recruitment uses min(MicroPopulationCap, floor(maximum population / 3)), also constrained by remaining global population. Existing over-cap identities are retained; admissions wait for capacity. This is an admission reservation, not retroactive deletion or a promise to fill all reserved seats immediately.

## Interaction result

Rosewood consequence rejection uses stable `reason=rosewood_distrust`, `lineKey=UI_EchoesOfHumanityNpc_Reject_rosewood_distrust`, `speakerName`, `npcId` and `accepted=false`. It closes any existing interaction session. The client presents readable localized text plus a direct Close control; unknown/missing reason translations use a generic unavailable-conversation fallback. Request correlation/MP authority remain unchanged.

## Execution model

No GPU/native-actor threading changes. Existing detached road planning workers and bounded simulation scheduling remain. Native world, inventory, bodies and network decisions continue on the authoritative game thread.

Offline coverage executes real community plans, unique/reduced work completion, pending lease retention, failed-route recovery, preserved mission ownership and budget admission with native survivor fixtures. Lua coverage exercises actual rejection UI methods and close callbacks. Dedicated startup smoke is separate from visual multiplayer gameplay validation.
