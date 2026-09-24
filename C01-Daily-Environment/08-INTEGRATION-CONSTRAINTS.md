# Future integration constraints

This document is a boundary for any separately authorized future work. C01 itself changes no runtime asset or code.

## Immutable game contract

Future integration must preserve all of the following:

- 414×736 logical game canvas and the current horizon/projection.
- Three lanes, current procedural track, current rails and chevrons.
- Current input and 110ms lane transition.
- Current player radius and collision behavior.
- Current RNG, spawns and object semantics.
- Current DOM HUD and feedback bands.
- Daily `rulesVersion`, Daily scoring, ranked logic and token IDs.
- Existing logo system and Prismatic Core fallback.

The environment is always **DECORATIVE BACKGROUND ONLY**. It must not create gameplay RNG draws; move lane/collision geometry; alter scoring, tokens or ranked eligibility; use runtime image generation; or perform a mid-run network fetch.

## Future technical envelope

- The plate remains behind game layers (current Daily environment target depth −20; road is 0, chevrons 1, player 10).
- It may not paint FINISH or replace the existing portal timing/pivot/transparent center.
- No architecture may render above hazards, actionable objects or HUD.
- One opaque plate is expected, with a 828×1472 master and later 414×736/828×1472 runtime tiers only after review and performance validation.
- Existing procedural fallback must remain available.
- Any production output must be local, versioned, hashed, normalized, reviewed at actual size and tested across required devices. A generated source image is not an automatic runtime asset.

No C01 work may modify `src/`, `public/`, `api/`, `supabase/`, `registry/`, `package.json`, or `package-lock.json` unless a separate, explicit integration authorization is granted.
