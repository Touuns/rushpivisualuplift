# Composition and safe zones

Use this document with the PNG guides. They are at both 414×736 and 828×1472; the latter is the requested environment-master target.

| File | Meaning |
|---|---|
| `masks/c01-road-exclusion-414x736.png` / `-828x1472.png` | Semi-transparent **red protected road polygon**. Do not put generated high-contrast architecture, rails, collectible-like details, or strong landmarks there. |
| `masks/c01-hud-safe-zone-414x736.png` / `-828x1472.png` | Semi-transparent **red protected top HUD region**: logical y 0–150 (2× y 0–300). It is not an instruction to leave the whole top empty; it is an instruction to avoid high-frequency/high-contrast conflicts behind HUD. |
| `overlays/c01-generation-guide-414x736.png` / `-828x1472.png` | Combined view: cool green-blue lateral **detail allowed** regions, graphite **center quiet** road corridor, red protected road boundary/top HUD band, plus the horizon marker. |

## Composition contract

The central road/player corridor must have low local contrast, low detail frequency, no strong focal landmark, and no bright collectible-sized objects. Its screen-space road polygon remains procedural-game territory. Keep the lower player region especially calm.

Architectural detail belongs principally in the left and right side structures, far background, and depth layers. Use receding surfaces, seams, conduits, and silhouettes to point the eye gently toward the horizon. Do not place a giant portal, target, fake road, or focal landmark at the horizon.

### Lighting hierarchy

- Dark indigo/violet: structural base and ambient world identity.
- Warm gold/orange: selective, directional architectural energy and small emphasis only.
- Cyan/electric blue: secondary atmospheric depth, never dominant in the gameplay corridor.
- Glow must visibly emanate from seams, materials, and light sources—not arbitrary blurred circles.

The overlay colors are a technical review convention; they are not palette instructions for the final art.
