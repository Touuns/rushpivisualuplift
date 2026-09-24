# Context and goal

## What C01 tests

The visual audit identified a particular Daily-mode mismatch: the production Daily background contains depth and architecture, while the playable track is a comparatively flat procedural trapezoid. C01 tests one safer future composition:

```text
generated/authored environment plate
        + procedural Phaser track
        + procedural gameplay objects
        + DOM HUD
```

The plate owns world, depth, architecture, atmosphere, and lighting context. The game owns lanes, rails, track geometry, objects, hazards, tokens, collision, movement, and HUD. A C01 image is never gameplay authority.

## Canonical direction

**Refined Prismatic Arcade**: deep indigo/dark-violet world; violet structural identity; selective warm orange/gold reward and accent light; secondary electric-blue/cyan atmospheric light; clean futuristic architecture; controlled emissive materials; restrained glow; clear silhouettes; strong mobile readability.

It should feel more premium, architectural, cohesive, spatial, deliberate, and like a finished game world. It must not become busier, noisier, generic AI concept art, or cyberpunk for its own sake.

Material target: dark violet ceramic/glass, smoked futuristic surfaces, subtle prismatic facets, satin metallic gold details, and integrated emissive seams. Avoid toy plastic, random chrome, wet cyberpunk pavement, fantasy crystal caves, and excessive transparent glass.

## Fixed geometry

| Contract | Logical | 2× master |
|---|---:|---:|
| Game canvas | 414 × 736 | 828 × 1472 |
| Horizon | (207, 117.76) | (414, 235.52) |
| HUD safe top | approximately y 0–150 | approximately y 0–300 |

Authoritative road polygon at logical resolution:

```text
(140.76, 117.76) → (273.24, 117.76) → (414, 736) → (0, 736)
```

This is an exclusion and quiet zone for generated art, not a shape to paint. Current rails and three lanes remain procedural.

## Success criterion

A candidate only progresses if it beats the existing Daily production control at actual gameplay size while preserving readability, object separation, perspective compatibility, material coherence, and technical plausibility. A more detailed or more spectacular candidate does not win by default. No selection, cleanup, integration, or deployment is authorized by C01 preparation.
