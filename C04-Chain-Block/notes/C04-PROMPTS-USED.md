# C04 — Prompts et provenance

25 septembre2026. Outil intégré image_gen. Trois appels initiaux séparés, un par direction ; aucune fabrication artistique par script.

Références de chaque appel initial, dans cet ordre :

1. `I:/ProjetDEv/rushpivisualuplift/C01-Daily-Environment/references/03-current-chain-block-128w.png`
2. `I:/ProjetDEv/rushpivisualuplift/C01-Daily-Environment/round-2-B2/generated/C01-B2-v1.png`
3. `I:/ProjetDEv/rushpivisualuplift/C01-Daily-Environment/references/01-daily-gameplay-414x736.png`
4. `I:/ProjetDEv/rushpivisualuplift/C01-Daily-Environment/round-2-B2/preview/C01-B2-gameplay-preview.png`

## C04-A — prompt exact initial

```text
Use case: stylized-concept, reference-guided new sprite. Create ONE isolated Rush Pi Chain Block game object on a truly transparent alpha background. Square master at least 512x512, preferably 1024x1024. Centered pivot, full object uncropped with generous transparent padding, opaque solid body and clean antialiased edge. No background color, no fake checkerboard, no ground plane, no cast shadow or external bloom. Output one sprite, not a sheet.
References in order: 1 current Chain Block = recognition, compact angular silhouette, violet housing and single gold energy core. 2 B2 architectural environment = material/lighting only, never copy canyon shape or backdrop. 3 Daily gameplay screenshot = small-scale legibility and semantic separation only. 4 B2 gameplay preview = restrained lighting context only. Do not reproduce screenshot UI, text, objects or background.
Material direction: Refined Prismatic Arcade, dominant violet/dark indigo ceramic and smoked glass, broad readable beveled planes, small satin-gold structural inlays, ONE clear warm gold luminous energy core set into front housing; controlled violet edge light tied to material. Body must read as a compact angular engineered BLOCK, three-quarter shallow view, asymmetrically faceted outer housing, NOT round, not a disc, not a coin, not a badge, not a powerup. Violet body visually dominates, core at most about 15% of visible area. Internal light, no huge glow, no cyan energy core. At final gameplay size 32 and 45 pixels the silhouette and single core must still read instantly: very few large facets, no filigree, no tiny noisy seams.
Current gameplay box is 45x45 before perspective, logical radius is 18. Keep a compact near-square silhouette with no spikes or outward decorative arms. The object must not suggest a larger collision envelope. Small structural gold lugs may be integrated flush with housing but never extend the silhouette dramatically.
ABSOLUTE: no text, letters, pi, logos, currency symbols, token ring, coin-like circular frame, detached particles, satellites, halo defining silhouette, gems, jewelry, fantasy crystal, excessive gold, toy plastic, spikes, needles, tiny facet noise, red hazard forms, cyan shield forms. Not an orb. Transparent background must be real alpha.

C04-A — Refined Current. Stay closest to reference 1's violet angular multi-lobed block and recognizable single warm energy core. Clean up toy-like edges into broad ceramic bevels, retain the characteristic asymmetry and integrated small gold connections. Preserve recognition before novelty.
```

## C04-B — prompt exact initial

```text
Use case: stylized-concept, reference-guided new sprite. Create ONE isolated Rush Pi Chain Block game object on a truly transparent alpha background. Square master at least 512x512, preferably 1024x1024. Centered pivot, full object uncropped with generous transparent padding, opaque solid body and clean antialiased edge. No background color, no fake checkerboard, no ground plane, no cast shadow or external bloom. Output one sprite, not a sheet.
References in order: 1 current Chain Block = recognition, compact angular silhouette, violet housing and single gold energy core. 2 B2 architectural environment = material/lighting only, never copy canyon shape or backdrop. 3 Daily gameplay screenshot = small-scale legibility and semantic separation only. 4 B2 gameplay preview = restrained lighting context only. Do not reproduce screenshot UI, text, objects or background.
Material direction: Refined Prismatic Arcade, dominant violet/dark indigo ceramic and smoked glass, broad readable beveled planes, small satin-gold structural inlays, ONE clear warm gold luminous energy core set into front housing; controlled violet edge light tied to material. Body must read as a compact angular engineered BLOCK, three-quarter shallow view, asymmetrically faceted outer housing, NOT round, not a disc, not a coin, not a badge, not a powerup. Violet body visually dominates, core at most about 15% of visible area. Internal light, no huge glow, no cyan energy core. At final gameplay size 32 and 45 pixels the silhouette and single core must still read instantly: very few large facets, no filigree, no tiny noisy seams.
Current gameplay box is 45x45 before perspective, logical radius is 18. Keep a compact near-square silhouette with no spikes or outward decorative arms. The object must not suggest a larger collision envelope. Small structural gold lugs may be integrated flush with housing but never extend the silhouette dramatically.
ABSOLUTE: no text, letters, pi, logos, currency symbols, token ring, coin-like circular frame, detached particles, satellites, halo defining silhouette, gems, jewelry, fantasy crystal, excessive gold, toy plastic, spikes, needles, tiny facet noise, red hazard forms, cyan shield forms. Not an orb. Transparent background must be real alpha.

C04-B — Architectural Facet. Translate B2's broad architectural bevels into a compact engineered block: a few large stepped violet planes, substantial geometric housing, recessed rectangular/chamfered warm core, very restrained flush gold inlays. More architectural than A, but still unmistakably the same Chain Block object family. No long tower forms.
```

## C04-C — prompt exact initial

```text
Use case: stylized-concept, reference-guided new sprite. Create ONE isolated Rush Pi Chain Block game object on a truly transparent alpha background. Square master at least 512x512, preferably 1024x1024. Centered pivot, full object uncropped with generous transparent padding, opaque solid body and clean antialiased edge. No background color, no fake checkerboard, no ground plane, no cast shadow or external bloom. Output one sprite, not a sheet.
References in order: 1 current Chain Block = recognition, compact angular silhouette, violet housing and single gold energy core. 2 B2 architectural environment = material/lighting only, never copy canyon shape or backdrop. 3 Daily gameplay screenshot = small-scale legibility and semantic separation only. 4 B2 gameplay preview = restrained lighting context only. Do not reproduce screenshot UI, text, objects or background.
Material direction: Refined Prismatic Arcade, dominant violet/dark indigo ceramic and smoked glass, broad readable beveled planes, small satin-gold structural inlays, ONE clear warm gold luminous energy core set into front housing; controlled violet edge light tied to material. Body must read as a compact angular engineered BLOCK, three-quarter shallow view, asymmetrically faceted outer housing, NOT round, not a disc, not a coin, not a badge, not a powerup. Violet body visually dominates, core at most about 15% of visible area. Internal light, no huge glow, no cyan energy core. At final gameplay size 32 and 45 pixels the silhouette and single core must still read instantly: very few large facets, no filigree, no tiny noisy seams.
Current gameplay box is 45x45 before perspective, logical radius is 18. Keep a compact near-square silhouette with no spikes or outward decorative arms. The object must not suggest a larger collision envelope. Small structural gold lugs may be integrated flush with housing but never extend the silhouette dramatically.
ABSOLUTE: no text, letters, pi, logos, currency symbols, token ring, coin-like circular frame, detached particles, satellites, halo defining silhouette, gems, jewelry, fantasy crystal, excessive gold, toy plastic, spikes, needles, tiny facet noise, red hazard forms, cyan shield forms. Not an orb. Transparent background must be real alpha.

C04-C — Premium Hybrid. Balance the recognizable current angular Chain Block with B2's restrained premium material. Use a small number of substantial violet bevels, a clearly recessed warm core, one or two quiet gold links integrated into the block. Prioritize the most legible compact silhouette at 32px, not ornament. Keep recognition and depth in equal balance.
```

## C04-C — unique correction

Entrées : `C:/Users/Touunss/.codex/generated_images/01a0ceec-1879-7b03-92ff-781b0f645939/exec-a2d6f601-38b9-4659-8104-5dab5760cfb9.png` (C initial, non retenu) puis B2 brut. Sortie corrigée retenue comme C04-C-v1-master.

```text
Edit the FIRST image (C04-C Chain Block) into the final C04-C-v1 sprite. The SECOND image is B2, material/light restraint reference only. Keep the compact angular block silhouette, front three-quarter orientation and broad violet planes. Make these specific corrections: remove ALL THREE small glowing gold satellite nodes and their gold connecting arms, replacing them with flush dark violet ceramic housing bevels. Leave ONE central recessed warm amber energy core only. Reduce that core's visible size by about one third, remove the miniature glowing cube drawn inside it, use a simple softly luminous chamfered energy window. Replace bright purple neon edges with restrained lighter-violet ceramic bevel highlights. The object must be mostly dark violet/indigo, with tiny satin gold inlay just around its ONE core. Render clean premium B2-like smoked ceramic planes without toy gloss. Keep body visible at 32px through broad facet value separation, not excessive glow. No additional geometry, no spikes, no round coin border. Square master >=512px, centered with transparent margins; TRUE transparent alpha background, clean antialiased edge, NO background, NO shadow, NO external halo, NO checkerboard baked in, NO text, NO logos, NO pi, NO letters, NO particles. One final isolated sprite only.
```

Quatre images générées au total ; trois masters finaux conservés. La version C initiale n'est pas un quatrième finaliste et n'est pas copiée dans candidates.

## Fichiers natifs retenus

- C04-A : `C:/Users/Touunss/.codex/generated_images/01a0ceec-1879-7b03-92ff-781b0f645939/exec-2bd68c36-80c2-4da2-a68e-495b0c60b0c3.png` → [master conservé](../candidates/A/C04-A-v1-master.png)
- C04-B : `C:/Users/Touunss/.codex/generated_images/01a0ceec-1879-7b03-92ff-781b0f645939/exec-93c2c437-2b0d-4efc-9b46-8f5d49cba8c5.png` → [master conservé](../candidates/B/C04-B-v1-master.png)
- C04-C : `C:/Users/Touunss/.codex/generated_images/01a0ceec-1879-7b03-92ff-781b0f645939/exec-92f47c21-56f7-49c4-8176-5a069ad0b110.png` → [master conservé](../candidates/C/C04-C-v1-master.png)

