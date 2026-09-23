# Visual Phase A — UI coherence / vector language / material system

**Branch:** `visual/phase-a-ui-coherence` · **Baseline:** `1646d0f366b3cb609531afcb36f54b0e5a0078a4`
**Status:** implemented + product-review corrections applied, uncommitted. Nothing committed, pushed, merged or deployed.

> **Product review round 1 — two approved corrections, applied.**
> 1. **Stat-value alignment regression.** Making `.stat__value` a flex row (to seat the authored icon beside
>    the number) silently dropped the `text-align: center` inherited from `.screen`, leaving values
>    left-aligned under centred labels on Profile, Daily/Training/Survival Result and Campaign Result.
>    Fixed with `justify-content: center`.
> 2. **Unselected Leaderboard tabs too weak.** The sunken-surface concept is kept; only the edge is promoted
>    from `--border-divider` (.12) to `--border-structural` (.26). No glow added, selected tab untouched.
>    See `comparison/tab-border-fix.png` for the zoomed before/after.
>
> Affected AFTER frames were recaptured (Profile, Profile-lower, Daily Result, Campaign Result, all three
> Leaderboard states, at all three viewports — 21 frames). The other 45 AFTER frames are the originals from
> review round 1, because neither fix can reach them. The Lives green, `.pi-panel__done` green and the
> 15-icon family were reviewed and approved as-is.

Start here: **[comparison/index.html](comparison/index.html)** — filterable before/after contact sheet.
Also: **[comparison/icon-family.html](comparison/icon-family.html)** (every icon at every shipping size) and
**[comparison/status-channel.html](comparison/status-channel.html)** (the five gameplay status chips).

---

## What this phase did

The audit's verdict was that Rush Pi's palette and semantics are sound, and that the ceiling is set by
*inconsistency* rather than by missing art. Phase A therefore spends no raster art at all. It gives the
values the product was already using a **role**, and replaces the glyphs the product does not own.

Three things changed, in order of how much they matter:

1. **An authored vector icon family** replaces every platform-rendered emoji in the UI, plus the unicode
   symbols that shared a slot with one. The Daily HUD's coin glyph — which renders as an empty box (▯) in
   the audit browser — is gone.
2. **A material system**: surface, border, radius, glow and type roles as CSS variables, applied to the
   families that already existed. No class was renamed; no component was abstracted into a design system.
3. **Hierarchy repairs** on the two screens the audit called out for flat weighting (Profile, Campaign list)
   and one for uncontrolled glow (Home).

---

## Files changed

| File | What changed |
|---|---|
| `src/components/RushIcon.tsx` | **New.** The 15-mark authored icon family + the shared `StarRow`. |
| `src/styles/global.css` | Material-system tokens; role application across ~30 rules. |
| `src/components/GameScreen.tsx` | Token chip, Lives, status channel, tabular numerals. |
| `src/components/HomeScreen.tsx` | Mode emblems, profile-strip marks, streak copy. |
| `src/components/ProfileScreen.tsx` | Stat tone/icon, locked badges, star rows, section separation. |
| `src/components/CampaignScreen.tsx` | Star rows, lock mark, objective alignment. |
| `src/components/LeaderboardScreen.tsx` | Energy/hit marks, tabular numerals. |
| `src/components/ResultScreen.tsx` | Star rows, trophy, streak, token ✓/✕ marks. |
| `src/components/ModeIntroModal.tsx` | Close mark; the legend star now matches the product star. |
| `src/components/MarketDataPreview.tsx` | Logo placeholder glyph. |
| `src/components/PiPanel.tsx` | Payment-confirmed mark. |

No change under `src/game/`, `api/`, `supabase/`, `registry/`, `public/assets/rushpi/production/` or `public/data/`.

---

## The icon family

15 marks, one technical language: 24×24 viewBox, nominal 2px stroke with optical correction below 24px,
round caps and joins, `currentColor` throughout, `aria-hidden` by default. Every icon sits beside text that
already carries the meaning, so no text control became an icon-only control.

**12 replace an emoji or an unstable glyph:**

| Mark | Replaced | Seen on |
|---|---|---|
| `token` | `🪙` — **renders as an empty box in the audit browser** | Daily HUD (every second of every Daily run) |
| `streak` | `🔥` | Home strip, Profile ×2, Daily/Training result |
| `trophy` | `🏆` | Home strip, Profile season, Campaign result |
| `badge` | `🏅` | Home strip |
| `lock` | `🔒` | Profile badge grid (41 of 43 cards), Profile progress, Campaign list |
| `star` | `★` / `☆` | Campaign list, Profile progress, Result objectives, intro-modal legend |
| `life` | `❤️` | Survival / Campaign HUD |
| `energy` | `💠` / `✦` | Leaderboard rows, Energy Zone status |
| `check` | `✓` | Daily token list, Pi payment confirmation |
| `cross` | `✕` | Daily token list, obstacles-hit count, modal close |
| `shield` | `🛡` | Gameplay status channel |
| `magnet` | `🧲` | Gameplay status channel |

**3 complete a channel rather than replace an emoji** — `speed` (`»`), `danger` (`▲`), `tunnel` (`◎`).
These three share the *single* gameplay status slot with Shield and Magnet. Converting only the two emoji
would have left one slot rendering two authored marks beside three unicode ones at different optical
weights, which is precisely the incoherence this phase exists to fix.

This is 15 designs against the brief's "approximately 8–12". The overage is those three channel symbols
and is called out here deliberately rather than buried.

### Glyphs intentionally RETAINED

- **The 43 badge icons in `src/utils/badges.ts`** keep their emoji. The brief forbids redrawing the set,
  and a half-converted set reads worse than a consistent one. Only the *locked* state is authored — that is
  the state 41 of 43 cards are in for a new player, and the padlock emoji's brown was the loudest foreign
  colour on the screen. **Known seam:** unlocked emoji badges now sit beside authored padlocks. This reads
  as intentional (rewards are colourful; locks are quiet) but it is a real inconsistency, and converting the
  badge set is a candidate for a later phase.
- **The `.legend-mark` CSS miniatures** in the intro modal. They are a deliberate system mirroring real
  in-game geometry, and the audit grades them as working. Only the legend's `★` was converted, so the legend
  shows the player the same star Campaign actually draws.
- **The back chevron.** The audit grades it effective; it keeps its heavier 2.6px navigation stroke.
- **`·` separators, `?` info marks, `π`, currency and arrow glyphs** — stable, and replacing them would be
  change for its own sake.

---

## Material system

Added to `:root`, applied by role. Existing names (`--radius`, `--shadow-glow`) were kept so no rule had to
change merely to mean the same thing.

**Surfaces** — `--surface-card` / `--surface-compact` / `--surface-hud` / `--surface-chip` / `--surface-sunken`.
These name the translucent values the stylesheet had been re-typing by hand, so a compact card and a HUD pod
are now the same decision.

**Borders** — `--border-structural` (1px) / `--border-emphasis` (2px where justified) / `--border-divider`
(subdued) / `--border-reward` (gold).

**Radii, by role** — 16px main cards and primary buttons · 12px compact cards and HUD · 8px small controls ·
999px genuine pills only. Two moves are visible: `.btn--small` (Home's Training/Leaderboard/Profile row) drops
from 16px to 8px, because at 40px tall a 16px radius is almost a pill and gave a utility button the same corner
language as the dominant Daily card; and list rows (`.cp-row`, `.history-row`) settle at 8px.

**Glow, four tiers** — tier 0 has no token on purpose: most surfaces should reach for nothing.
Tier 1 `0 4px 12px /.42` ambient · tier 2 `0 0 18px /.26` selected or primary · tier 3 `0 0 20px /.30` accent.

Two specific reductions, both named in the audit as the cohesion problem:

- `.btn--primary` was `0 0 24px rgba(139,92,246,.45)` — a persistent broad bloom on every primary button.
  Now tier 2 plus a grounding ambient.
- `.home__logo` was `0 0 36px rgba(255,209,102,.5)` — a permanent gold bloom wider than the mark itself,
  and the audit's example of two unrelated glow languages in one screen. Now tier 3.

**Type roles** — `--fs-score` / `--fs-title` / `--fs-stat` / `--fs-body` / `--fs-secondary` / `--fs-label` /
`--fs-chip`, at sizes the product already used. Nothing was mechanically enlarged. `font-variant-numeric:
tabular-nums` was applied to Score, Time, Combo, token counts, XP, charge, progress, leaderboard scores and
ranks, stat values, best scores and the result score — every number that changes while the player watches.

---

## Screen by screen

**Home.** Daily still wins: it keeps the identity gradient and is the only card carrying a tier-2 glow, and
the secondary pair moved to the quieter compact-card role so they no longer compete on border brightness.
Each mode gained a small authored emblem — deliberately *not* new icons, but a symbol the mode already owns:
Daily → the token it is a rush for, Survival → the life it gives you three of, Campaign → the star it is
scored in. No card painting, no second hero, nothing behind text. Background, layout, copy and routing
unchanged.

**HUD — polish, not redesign.** Position, the three groups, sizes and the status priority are untouched.
The pods gained a 1px structural edge so they read as surfaces over the illustrated Daily tunnel instead of
smudges. Lives became authored hearts in `--life-green`: the ❤️ emoji arrived in the platform's red, the
colour this product reserves for danger, on a screen full of red hazard diamonds. **This is a colour change
and is flagged for review** — it aligns the HUD with the green Life Orb that grants lives, but it is the one
place Phase A moved a colour rather than a material.

**Token chip (acceptance item).** `🪙 Tokens N/15` → authored token mark + `Tokens N/15`. Count, total,
wording, position and HUD priority byte-identical. See `before/daily-gameplay-375x667.png` for the ▯.

**Results.** Information architecture untouched — no reorder, no added reward mechanic, no generated art,
CTA order preserved, the first-Daily "Leaderboard leads" rule intact. Score stays dominant and is now tabular.
Star rows, trophy, streak flame and the token list's ✓/✕ are authored. A missed token row moved from 0.5 to
0.66 opacity, because at 0.5 the symbol and price a player scans to see *what they missed* were below
comfortable reading. **First Result is visually unchanged** and remains deliberately quiet.

**Profile.** Nine identically weighted stat cards gave no number the lead. No data removed, nothing reordered,
no card collapsed: hierarchy comes from tone instead. Best Daily — the headline number — reads in reward gold
with a structural border; the streak pair is marked by its icon; everything else stays neutral, so exactly one
value is coloured for emphasis. Section titles gained a hairline divider, turning each into a real boundary at
1px of added ink. The locked badge grid is the biggest single win: 41 brown padlock emoji at 0.45 opacity with
barely-legible names became authored padlocks at 0.72 on a sunken surface (`before/profile-lower-375x667.png`
against `after/`).

**Leaderboard.** Daily default, tabs, ranking data, empty states and actions unchanged. An unselected tab
gained a surface so the row reads as one control rather than three outlines; the selected tab is the only glow.
Rank 1 takes the 2px emphasis border and ranks 2–3 gained matching numeral colours, so first place is
distinguishable from second without relying on gold-vs-silver hue alone. `💠` — a **blue** platform diamond used
for *energy*, while blue means protection in this product — became the authored gold spark.

**Campaign list only.** No map, no chapter art, no boss. Cards joined the main-card material family. The
objective tiers were `★`, `★★`, `★★★` — three different widths, so the labels beside them never lined up;
they are now three fixed slots with 1/2/3 filled, same information, aligned column. A locked card moved from
0.5 to 0.68 opacity: the lock mark, the "Finish Level N" line and the disabled state already say it is locked,
and 0.5 made the objectives unreadable. 8 levels, names, objectives, stars, locks, scores and unlock behaviour
unchanged.

**Modals / Daily preparation.** Scroll behaviour, fixed footer, 13G entry logic, auth logic, last-attempt logic
and button actions untouched. They took the common material and icon language only. The last-attempt panel
remains warm gold, not destructive red.

---

## Accessibility and readability

Reviewed at 375×667, 414×736 and 1440×900.

- **Nothing was dimmed for style.** Three opacities moved *up* (locked badge 0.45→0.72, locked level 0.5→0.68,
  missed token 0.5→0.66, locked progress row 0.55→0.7) because each was suppressing text the player is asked to read.
- **Icon meaning never depends on colour.** Earned vs unearned stars differ by *fill*; met vs unmet objectives
  differ by fill; collected vs missed tokens are check vs cross. Every icon sits beside its own text.
- **Touch targets unchanged.** The 44×44 areas on the mode `?` button, the modal close and the back button are
  untouched; only the visible marks inside them changed.
- **Semantic colours preserved** — red danger, cyan protection, green life, gold/orange reward, violet product.
  Two corrections *toward* the scheme: energy left blue for gold, HUD lives left red for green.
  One deliberate move: `.pi-panel__done` (payment confirmed) went gold → green, as a confirmed positive state
  rather than a reward. Flagged for review.
- **No new motion.** No looping decoration added. The two new transitions (`.mode-card` press, `.tab` colour)
  are colour/transform only and are not required for comprehension.
- **Not certified.** These are desktop-Chromium viewport emulations at DPR 1. Native Pi Browser, real devices,
  high-DPR text rendering and full WCAG measurement remain open QA, exactly as in the audit.

---

## Evidence

`before/` holds 63 baseline frames copied unchanged from the audit. `after/` holds the same 63 recaptured with
the same harness, fixture and viewports, plus 3 populated-leaderboard frames.

**Runs are live gameplay**, so scores and object poses differ between columns — compare UI treatment, not
identical frames.

Capture conditions match the audit's, because the capture is the audit's own script (`after/capture.mjs`,
`after/cdp.mjs`, copied unchanged): isolated headless Chromium at DPR 1, all HTTPS blocked, `/api/*`
intercepted, the same deterministic 15-token fixture rebuilt from the same registry inputs, empty leaderboard
responses. No Pi authentication, claim, submission, payment or ranked attempt occurred.

Three gaps, stated plainly:

- **The harness's per-task JSON logs were not retained.** They were written during capture and removed in
  cleanup, so the "zero runtime exceptions / zero non-GET requests" record the audit published has no
  equivalent here. Re-running any task in `after/capture.mjs` regenerates them.

- **The leaderboard row changes have no matched runtime pair.** Both the audit baseline and this capture show an
  empty local list and an empty server fixture. `after/leaderboard-local-populated-*.png` was produced by seeding
  the *local* save through the product's own shape (no server, no ranked attempt, no claim) and has no baseline
  counterpart.
- **The Shield/Magnet status chips never appear in either capture set**, because forcing an active power-up would
  mean editing gameplay. `comparison/status-channel.html` renders the real markup against the real production
  stylesheet instead. It is presentation evidence, not a screenshot of a running game.

---

## Verification

| Check | Result |
|---|---|
| `npm test` | **422 / 422**, 0 failures (baseline 422) |
| `npx tsc --noEmit` | clean |
| `npx tsc -p api/tsconfig.json` | clean |
| `npm run build` | clean |
| `npx vercel build` | Build completed successfully |
| `git diff --check` | clean |

No test was added or modified. One existing Phase-13F guard (`firstDailyMeta.test.ts` #14, which pins the
streak line as state living outside the one-time lesson gate) initially failed on JSX line-wrapping alone.
The contract was intact, so the **source** was reshaped back to what the guard expects rather than loosening
the test.

---

## Stop conditions — what was reverted or not attempted

- No change kept that only reads better zoomed in; the icon family was proofed at 13px and 16px and four marks
  were redrawn after failing there (`token` collapsed into `tunnel`; `badge` read as a keyhole; `energy` filled
  into a blot; `magnet` read as an arch with a line through it).
- No layout at 375×667 became tighter, except Profile's section dividers, which add ~10px per section on an
  already-scrolling screen.
- **Unselected-tab surface** was flagged in review round 1 as earning nearly nothing against the app frame's
  own dark gradient. Resolved by keeping the surface and promoting the border to the structural tier, rather
  than reverting — see the correction note at the top.
- Not attempted, per brief: the Phaser hard-disc halo (Phase B), any background or card painting (Phase C),
  any new font family, any Campaign worldbuilding, any badge-set redraw.
