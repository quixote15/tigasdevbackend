# Carimbo de Protocolo — Sprite Specification

## Overview
A comically oversized rubber stamp that says "INDEFERIDO" (DENIED) on its stamping face. This is a melee special weapon — a bureaucratic bludgeon that stuns enemies by literally denying their existence. The stamp handle is a thick wooden cylinder grip, and the rubber base is massive, dripping with red ink. When slammed down, it leaves a visible "INDEFERIDO" imprint on the ground and on enemies. The weapon is deliberately larger than the player character — a grotesque monument to Brazilian bureaucratic power.

## Dimensions
- **Weapon sprite (held/swing):** 48x48px (oversized — weapon bigger than character)
- **Impact stamp mark:** 32x32px
- **Ink splatter particles:** 16x16px each
- **"INDEFERIDO" ground decal:** 48x16px

## Color Palette

| Element                 | Hex Code  | Description                              |
|-------------------------|-----------|------------------------------------------|
| Stamp handle (wood)     | #8B5E3C   | Dark worn wood grain                     |
| Handle highlight        | #A67C52   | Lighter wood on top edge                 |
| Handle grip rings       | #6B3A1F   | Darker carved grip grooves               |
| Rubber base             | #2B2B2B   | Near-black vulcanized rubber             |
| Rubber base edge        | #1A1A1A   | Pure dark rubber outline                 |
| "INDEFERIDO" text       | #CC1111   | Bold red stamp ink                       |
| Red ink (fresh)         | #DD2222   | Bright fresh ink splatter                |
| Red ink (dried/dark)    | #8B1111   | Darker dried ink stains on stamp         |
| Ink drips               | #CC1111AA | Semi-transparent dripping ink            |
| Wood screws/metal       | #A0A0A0   | Gray metal fittings on handle            |
| Stun stars              | #FFD700   | Gold cartoon stun stars                  |
| White flash             | #FFFFFF   | Impact flash                             |
| Ground stamp mark       | #CC111166 | Semi-transparent red imprint on ground   |
| Dust cloud              | #C4B99F   | Brown-gray impact dust                   |

## Frame-by-Frame Descriptions

### Static / Inventory (1 frame)
**Frame 0 — `carimbo_static.png`**
The stamp is shown from a top-down isometric view: the massive rubber base facing down-right, the wooden handle extending up-left. The stamp fills nearly the entire 48x48 canvas — it is ABSURDLY large. The wooden handle is a thick cylinder (~12px wide, ~20px tall) with carved grip rings (3 dark grooves). At the top of the handle, two small gray metal screws are visible. The rubber base is a thick rectangular block (~30x18px) extending from the handle. On the visible side of the rubber base, "INDEFERIDO" is embossed in reversed mirror-text (as real stamps show). The base has dried red ink caked on it — splotchy, uneven, with small drip trails running down the sides (2-3px red drip lines). The overall look is battered, well-used, slightly menacing. A small red ink puddle (3px) sits beneath the stamp base, suggesting it's always dripping.

### Swing / Use Animation (4 frames)
**Frame 1 — `carimbo_swing_01.png`**
Raise: The stamp is lifted high. The handle points upward at 70 degrees from horizontal. The rubber base is visible and cocked back, loaded for a devastating slam. The entire weapon is shifted upward in the frame by 8px. Small red ink drops detach from the base (2 droplets, 1px each, falling). Two thin white motion lines suggest upward movement. The stamp casts a larger shadow below (4px dark oval) indicating height.

**Frame 2 — `carimbo_swing_02.png`**
Apex: The stamp reaches maximum height, momentarily paused. The handle is nearly vertical (85 degrees). The rubber base is at the top of the frame. Three ink drops are now mid-fall below the stamp. The shadow below is at maximum size (8px dark oval). A small "glint" star appears on the metal screws (2px white cross). This is the dramatic pause before the slam — the frame where the player commits.

**Frame 3 — `carimbo_swing_03.png`**
Downswing: The stamp rockets downward. Extreme motion blur — the handle is a streak of brown, the rubber base a dark mass with red trailing smear. 4 thick white speed lines frame the downward motion. The shadow below is shrinking rapidly as stamp approaches ground. The entire frame conveys MAXIMUM VIOLENCE. The ink drops from earlier have been overtaken by the stamp's speed. Comic-style "action zoom" lines radiate from the impact point.

**Frame 4 — `carimbo_swing_04.png`**
SLAM: The stamp has hit the ground. The rubber base is flat on the surface. The handle bounces slightly (2px upward recoil, tilted 10 degrees from the rebound). A massive dust cloud erupts around the base (12px radius, brown-gray). Red ink splatters explode radially from under the stamp in 8 directions (each splatter 3-4px long). The ground beneath shows a fresh "INDEFERIDO" stamp mark in red. The onomatopoeia "PLAFT!" appears in large red block letters above (full width of frame, 6px tall). Screen shake implied by slight offset of all elements by 2px.

### Impact / Stun Effect (3 frames)
**Frame 0 — `carimbo_impact_01.png`**
The stamp connects with an enemy. Massive white circular flash (16px radius) at contact point. Red ink explosion — 12+ ink droplets spraying in all directions. The "INDEFERIDO" text begins stamping itself onto the center of the frame in large red letters. Three gold cartoon stun stars begin appearing around the impact area. A shockwave ring (1px white circle) expands outward from impact.

**Frame 1 — `carimbo_impact_02.png`**
Peak impact: The flash fades but the red ink splatter is at maximum spread (20px radius). "INDEFERIDO" text is fully visible, stamped in bold red at a slightly crooked angle (as a real stamp would leave). The three stun stars are fully formed and orbiting the impact point. The shockwave ring has expanded to 24px and is fading. Additional detail: small cracks appear on the ground beneath the stamp (2-3 dark lines radiating from center). Red ink is pooling at the impact center.

**Frame 2 — `carimbo_impact_03.png`**
Recovery: The stamp lifts from the target with a "sucking" motion — a thin red ink strand stretches from the stamp base to the impact point (2px red line). The stun stars are still orbiting but shrinking. The "INDEFERIDO" text remains on the ground/enemy as a persistent decal, slowly fading. Ink splatters have settled. The stamp returns to ready position. Small red droplets drip from the base.

### Idle Glow / Effect (2 frames — looping)
**Frame 0 — `carimbo_idle_01.png`**
The stamp in rest position, leaning slightly left. A slow red ink drip forms on the bottom of the rubber base — a small bulging droplet (2px) about to fall. The "INDEFERIDO" text on the rubber base has a faint ominous red glow (1px red aura). The wooden handle has a subtle warm highlight on its upper edge. A tiny fly (2px, black dot with 1px wings) buzzes near the ink.

**Frame 1 — `carimbo_idle_02.png`**
The ink drip has fallen — now a 1px red dot on the ground below the stamp. A new drip is not yet formed (base is flat, no bulge). The red glow on the text has shifted slightly (pulsing effect). The fly has moved to the opposite side of the stamp. The handle highlight has shifted downward by 1px (subtle breathing). The overall feeling is of a weapon that is alive with bureaucratic malice, always dripping, always ready to deny.

## Sprite Sheet Layout
Horizontal strip: 48px height, frames laid out left-to-right.

| Sheet              | Frames | Total Width |
|--------------------|--------|-------------|
| `carimbo_static`   | 1      | 48px        |
| `carimbo_swing`    | 4      | 192px       |
| `carimbo_impact`   | 3      | 144px       |
| `carimbo_idle`     | 2      | 96px        |

## Additional Decal Sprites

### `stamp_mark_ground.png` (48x16px)
The word "INDEFERIDO" in red (#CC1111) blocky letters at alpha 0.5, slightly crooked (2-degree rotation). Rough edges like a real rubber stamp impression — uneven ink density, some letters slightly smudged. This decal persists on the ground for 3 seconds after a slam, fading from alpha 0.5 to 0.0.

### `stamp_mark_enemy.png` (32x32px)
Same "INDEFERIDO" text but formatted to overlay an enemy sprite. Red text at alpha 0.7, positioned to cover the enemy's center mass. This visual stays on the stunned enemy for the duration of the stun effect.

## Ink Splatter Particles (16x16px)
**`ink_splat_01.png`** — Irregular red blob, thick, freshly splattered. Asymmetric shape with 2-3 small satellite drops.
**`ink_splat_02.png`** — Thin elongated red streak, like ink flung from rapid motion. Tapered ends.
**`ink_splat_03.png`** — Small round red drop, simple, with a highlight dot suggesting wet ink. Used for drips.

## Notes
- The stamp is intentionally LARGER than the player character sprite (48x48 vs 64x64 character). When held, it should look absurdly oversized, dragging on the ground.
- "INDEFERIDO" decals on the ground stack — multiple slams create a satisfying carpet of denial.
- The stun effect (gold stars) is a separate overlay that follows the stunned enemy sprite.
- The tiny buzzing fly in idle frames is a detail homage to Andre Guedes' animation style of adding small grotesque ambient life.
- On critical hit, the stamp text changes to "ARQUIVADO" (FILED AWAY) and the enemy takes extra damage.
