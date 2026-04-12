# Microfone do Plenario — Sprite Specification

## Overview
A Congress podium microphone ripped from its stand, used as a ranged sonic weapon. The microphone is an old-school dynamic mic on a bent chrome gooseneck with a chunk of the wooden podium still attached at the base. The attack is a sonic feedback screech that emits visible sound wave rings as projectiles. The mic crackles with electricity and feedback static when idle. The visual personality is "unhinged politician screaming into a broken mic" — pure auditory violence turned visible.

## Dimensions
- **Weapon sprite (held):** 48x48px (oversized gooseneck mic with podium chunk)
- **Sound wave projectile rings:** 32x32px
- **Feedback screech effect:** 48x48px
- **Static/electricity particles:** 16x16px each

## Color Palette

| Element                  | Hex Code  | Description                               |
|--------------------------|-----------|-------------------------------------------|
| Mic head (grille)        | #A8A8A8   | Silver-gray metal mesh grille              |
| Mic head dark spots      | #707070   | Darker mesh pattern holes                  |
| Mic head highlight       | #D4D4D4   | Bright metallic sheen on top               |
| Gooseneck chrome         | #B0B0B0   | Brushed chrome flexible neck               |
| Gooseneck joint rings    | #888888   | Darker articulation segments               |
| Podium chunk (wood)      | #6B4226   | Dark mahogany congress podium wood         |
| Podium wood highlight    | #8B5A2B   | Lighter wood grain streaks                 |
| Exposed wires            | #CC4400   | Orange-copper exposed wiring at break      |
| Wire insulation          | #222222   | Black rubber wire insulation scraps        |
| Sound wave rings         | #44BBFF   | Electric blue sonic wave (primary)         |
| Sound wave inner         | #88DDFF   | Lighter blue inner ring glow               |
| Sound wave outer         | #2288CC   | Darker blue outer ring edge                |
| Feedback screech         | #FFDD00   | Harsh yellow feedback distortion           |
| Feedback hot center      | #FFFFFF   | White-hot center of screech blast          |
| Electricity arcs         | #FFFF44   | Bright yellow electric sparks              |
| Electricity secondary    | #88CCFF   | Blue-white secondary arc color             |
| Static particles         | #AADDFF   | Pale blue static discharge                 |
| Red "ON AIR" light       | #FF0000   | Red indicator LED on mic base              |
| Red light glow           | #FF000066 | Semi-transparent red glow halo             |

## Frame-by-Frame Descriptions

### Static / Inventory (1 frame)
**Frame 0 — `mic_static.png`**
Top-down isometric view of the weapon. The mic head is at the upper-right — a rounded cylinder shape (~10x12px) with a visible mesh grille pattern (tiny alternating light/dark pixels creating a dot-screen effect). The gooseneck extends from the mic head downward-left in a gentle S-curve (~24px long), composed of visible chrome articulation segments (6-8 rings, alternating #B0B0B0 and #888888). At the base, the gooseneck is embedded in a jagged chunk of dark mahogany podium wood (~16x12px) — the wood has a splintered, torn edge where it was ripped from the Congress podium. Exposed orange-copper wires dangle from the broken base (3-4 thin lines, 4-6px long). A small red LED dot (2px, #FF0000) glows on the mic base near where it meets the gooseneck, with a tiny red glow halo (4px, low alpha). The overall impression: this mic was violently torn from its podium and is still crackling with power.

### Use / Fire Animation (4 frames)
**Frame 1 — `mic_fire_01.png`**
Charge-up: The mic is angled forward (pointed at attack direction). The red LED brightens (2px -> 3px glow radius). Tiny yellow electricity arcs (2-3 arcs, each 3-4px) crackle around the mic head grille. The gooseneck straightens slightly as if tensing. The exposed wires at the base spark (1px yellow flashes at wire tips). A faint concentric ring (1px, very low alpha blue) begins forming around the mic head — the sound wave is building.

**Frame 2 — `mic_fire_02.png`**
Feedback build: The mic head is now visibly vibrating (1px blur/double-image on the grille). Electricity arcs intensify — 4-5 arcs radiating from the mic head, longer (5-6px each), bright yellow with blue-white secondary arcs. The forming sound wave ring is more visible (2px, medium alpha blue circle, 8px radius around mic head). The red LED is now flashing (alternating frames between bright red and dim). The mesh grille appears to be distorting/bulging from the sound pressure building inside. The wood chunk at the base vibrates (1px offset). Text fragments of "EEEEEE" begin appearing in tiny yellow letters near the mic (feedback screech text).

**Frame 3 — `mic_fire_03.png`**
SCREECH RELEASE: The mic fires. The grille mesh is blown open slightly (distorted outward shape). A massive blast of yellow-white light erupts from the mic head (12px conical burst in the attack direction). The first sound wave ring launches — a bold blue (#44BBFF) ring, 3px thick, at 12px distance from mic head. Electricity arcs are at maximum — 6-8 arcs flailing wildly around the mic and blast zone. "EEEEEE" text is fully formed and bold in yellow, vibrating. The gooseneck recoils backward (bent 10 degrees away from blast direction, like a gun recoil). Speed lines radiate from the mic head outward.

**Frame 4 — `mic_fire_04.png`**
Post-fire: The blast cone has dissipated. The sound wave ring has launched and is now at 24px distance (and has become a separate projectile entity). A second, smaller wave ring is forming at the mic head (8px distance). The mic head is smoking — 2-3 small gray smoke wisps rise from the grille. The electricity has calmed to 1-2 residual arcs. The gooseneck is returning to resting position (5 degree recoil, recovering). "EEEEEE" text is fading. A brief calm before the next possible shot.

### Sound Wave Projectile (4 frames — looping)
**Frame 0 — `wave_projectile_01.png`**
A concentric ring of sound energy. The ring is 16px diameter, centered in the 32x32 frame. It consists of a bright inner ring (#88DDFF, 1px) and a bolder outer ring (#44BBFF, 2px) with a darker edge (#2288CC, 1px). Inside the ring, there are 3-4 tiny radiating lines suggesting vibration energy. The ring is perfectly circular and bold.

**Frame 1 — `wave_projectile_02.png`**
The ring has expanded to 20px diameter. The outer ring has become slightly thinner (1.5px) and the inner ring brighter. Small distortion marks appear at the ring's leading edge (compression lines). The radiating lines inside have shifted position (rotating effect). A faint secondary ring (1px, very low alpha) trails 4px behind the main ring.

**Frame 2 — `wave_projectile_03.png`**
The ring is at 24px diameter. The ring lines are thinner still (1px each) and slightly more transparent — the wave is expanding and weakening. More distortion marks at the edges. The secondary trailing ring is now visible (8px behind, fading). Small white dots at cardinal points of the ring suggest peak amplitude nodes.

**Frame 3 — `wave_projectile_04.png`**
The ring is at 28px diameter, nearly filling the 32x32 frame. Thinnest lines (1px, medium alpha). Maximum expansion before the projectile either hits or expires. Both rings visible — primary and secondary — creating a double-ring pattern. The amplitude node dots are brighter, suggesting the wave is at its final peak before dissipation.

### Impact (3 frames)
**Frame 0 — `mic_impact_01.png`**
The sound wave ring hits an enemy and SHATTERS. The ring breaks into 8-10 curved arc fragments that scatter outward. A central burst of white-blue light (8px radius). Distortion lines radiate from the impact point — the air itself is visibly warped (wavy pixel displacement effect). The onomatopoeia "SCREEEECH!" begins forming in jagged yellow-blue letters above.

**Frame 1 — `mic_impact_02.png`**
The arc fragments have spread further (16px radius). The central light burst is expanding and fading. The air distortion effect is at maximum — concentric wavy lines surround the impact (like heat shimmer). "SCREEEECH!" text is fully formed, large, jagged, electric font. Yellow (#FFDD00) with blue (#44BBFF) outline. The impacted area has visible "noise static" — random colored pixels suggesting audio distortion made visible. Small blue lightning bolts (4-5, each 3-4px) arc outward from impact.

**Frame 2 — `mic_impact_03.png`**
The arc fragments are dissolving into tiny sparkle particles. The light burst is gone. Air distortion ripples are fading. "SCREEEECH!" text is dissolving, breaking into individual letters that scatter. The static noise pixels are settling. A final faint ring ripple (1px, very low alpha) expands outward as the last echo of the wave. Everything calming, returning to normal.

### Idle Glow / Effect (2 frames — looping)
**Frame 0 — `mic_idle_01.png`**
The mic in resting position. The red LED glows steadily (2px dot with 4px halo). One small electricity arc jumps between two points on the gooseneck (3px yellow arc). The mesh grille has a subtle highlight shimmer on its upper-right quadrant. The exposed wires at the base hang still. A tiny "hummm" text (barely visible, 1px tall, pale blue) appears near the mic head — ambient hum visualization.

**Frame 1 — `mic_idle_02.png`**
The red LED dims slightly (2px dot, 3px halo — smaller glow). The electricity arc has jumped to a different position on the gooseneck (between two other segments). The grille shimmer has moved to upper-left quadrant. One exposed wire twitches (1px shift). The "hummm" text has shifted position slightly and one "m" has faded. A very faint static crackle particle (1px blue-white dot) appears and disappears near the mic head.

## Sprite Sheet Layout
Horizontal strip, frames laid out left-to-right.

| Sheet              | Frame Size | Frames | Total Width |
|--------------------|------------|--------|-------------|
| `mic_static`       | 48x48      | 1      | 48px        |
| `mic_fire`         | 48x48      | 4      | 192px       |
| `wave_projectile`  | 32x32      | 4      | 128px       |
| `mic_impact`       | 48x48      | 3      | 144px       |
| `mic_idle`         | 48x48      | 2      | 96px        |

## Electricity / Static Particles (16x16px)
**`electric_arc_01.png`** — A jagged yellow lightning bolt (3-4 segments, zigzag pattern). Bright yellow (#FFFF44) with blue-white core (#88CCFF). 2-3px tall, thin.
**`electric_arc_02.png`** — A smaller spark burst: 3-4 lines radiating from a central point, like a static discharge. Yellow with blue tips.
**`static_crackle.png`** — A small cluster of 3-4 randomly colored pixels (blue, white, yellow) suggesting TV static / audio noise made visible. 4x4px active area within 16x16.

## Notes
- Sound wave projectile rings GROW as they travel. In-game, the sprite scales from 0.5x to 1.5x over the projectile's flight distance, simulating an expanding sound wave.
- Multiple projectiles can be on screen simultaneously (rapid fire weapon).
- The "SCREEEECH!" onomatopoeia uses a unique jagged/distorted font compared to other weapons' text effects — it should look like the letters themselves are vibrating and unstable.
- The exposed wires are a key visual detail — they sell the "ripped from Congress" improvised weapon story.
- The red "ON AIR" LED is a persistent detail that reminds the player this mic is still broadcasting its destruction live.
