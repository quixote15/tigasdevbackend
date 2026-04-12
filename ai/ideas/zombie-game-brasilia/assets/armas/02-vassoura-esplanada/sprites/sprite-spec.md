# Vassoura da Esplanada - Sprite Specification

## Overview
- **Weapon Type:** Melee (extended range)
- **Sprite Dimensions:** 48x48px (larger to accommodate broom length)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 12 (1 static + 4 sweep + 3 impact + 2 dust burst + 2 idle)
- **Sprite Sheet Size:** 576x48px
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (24, 44) -- handle grip point

## Color Palette

| Element              | Hex Code  | Usage                          |
|----------------------|-----------|--------------------------------|
| Wood Handle (main)   | `#8B6914` | Broom handle body              |
| Wood Handle (light)  | `#B8860B` | Handle highlights / worn edges |
| Wood Handle (dark)   | `#5C4409` | Handle shadow / grain lines    |
| Straw (main)         | `#D4A017` | Broom bristles base color      |
| Straw (light)        | `#E8C547` | Bristle highlights             |
| Straw (dark)         | `#8B7510` | Bristle shadows / dirt         |
| Straw (dirty)        | `#6B5B0A` | Dirty/wet bristle tips         |
| Binding Wire         | `#808080` | Wire holding bristles to handle|
| Binding Rust         | `#A0522D` | Rusted wire accent             |
| Outline Black        | `#1A1A1A` | Thick 2px outlines (Crumb)     |
| Shadow Dark          | `#0D0D0D` | Drop shadow, 50% opacity       |
| Dust Cloud (main)    | `#C4A35A` | Sweep dust particles           |
| Dust Cloud (light)   | `#E8D5A0` | Dust highlights                |
| Dust Cloud (dark)    | `#8B7D3F` | Thick dust patches             |
| Impact Beige         | `#DEB887` | "SWOOOSH" onomatopeia          |
| Impact Brown         | `#8B4513` | Onomatopeia shadow             |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 47,47
- **Description:** Old straw broom seen from top-down isometric view. Handle runs diagonally from bottom-left to top-right (~45deg). DISPROPORTIONALLY LARGE -- the broom head fills nearly half the frame. Thick wooden handle with visible grain lines (1px dark streaks). The bristle head is splayed outward, ragged and uneven -- this broom has swept the Esplanada dos Ministerios for decades. Rusty wire binding wraps where bristles meet handle (2-3 pixel lines of gray/brown). Individual straw bristles visible at the edges (jutting out 2-3px). Heavy drop shadow. Thick black outlines throughout.
- **Style Notes:** The broom should look ANCIENT and overworked. Bristles are bent, frayed, some broken off. The handle has dents and scratches. This is a weapon born from manual labor and indignity. A relic of the invisible workers who keep Brasilia "clean."

### Frame 1: Sweep Animation - Wind-up
- **Position in sheet:** 48,0 to 95,47
- **Description:** Broom pulled to the player's right side, bristle head sweeping back. Handle tilted ~60deg from original position. The bristles trail behind in the pull direction, bending from air resistance. Small anticipation squash on the bristle head (compressed 3px). The handle shows a slight flex curve (1px bend at midpoint). 1 faint motion trail line from the bristle tips.

### Frame 2: Sweep Animation - Full Sweep Left
- **Position in sheet:** 96,0 to 143,47
- **Description:** Broom in maximum sweep motion, bristle head sweeping left across the ground plane. The entire broom is nearly horizontal. Bristles are SPREAD WIDE from centrifugal force, creating a fan shape. Maximum stretch on bristles (5-6px spread beyond normal). 3 motion blur trails from the bristle tips at different opacities (80%, 50%, 20%). 2-3 dust particles (4x4px dust clouds) begin to appear near the bristle tips. The handle shows speed flex (subtle S-curve).

### Frame 3: Sweep Animation - Sweep Contact
- **Position in sheet:** 144,0 to 191,47
- **Description:** Broom at moment of contact with targets. Bristles COMPRESSED against the hit zone, flattened on one side. The impact causes bristles to splay violently outward on the non-contact side. A wide arc of dust particles erupts (6-8 small particles, 2x2 to 4x4px, in dust colors). Broken straw bits (1x3px, straw-colored) fly off at angles. Impact starburst visible at the contact edge of the bristles. Ground shows a sweep mark (1px line of dust color).

### Frame 4: Sweep Animation - Follow-through
- **Position in sheet:** 192,0 to 239,47
- **Description:** Broom continuing past the sweep, now on the player's left side. Bristles slowly returning to shape, still somewhat spread. A residual dust cloud (8x8px, semi-transparent) lingers at the sweep path center. Single motion trail fading. The broom is decelerating -- less motion blur. A few straw bristles are permanently bent from the impact (1-2 pixels displaced from the original pattern).

### Frame 5: Impact - Dust Explosion Frame 1
- **Position in sheet:** 240,0 to 287,47
- **Description:** Large dust cloud eruption effect. A billowing cloud of Esplanada dust fills ~60% of the frame. Multiple concentric dust puffs in varying sizes (4x4, 6x6, 8x8px) in dust palette colors. Small debris mixed in -- tiny paper scraps (2x2px white), cigarette butts (1x3px gray), a crushed beer can lid (3x3px silver). The dust cloud has darker center and lighter edges. "SWOOOSH" text begins to appear through the dust in beige/brown colors, hand-lettered style.

### Frame 6: Impact - Dust Explosion Frame 2
- **Position in sheet:** 288,0 to 335,47
- **Description:** Peak dust explosion. Cloud at maximum spread (~80% of frame). "SWOOOSH" text fully visible, large and bold, cutting through the dust. Letters are wavy/distorted as if seen through heat haze. The dust layers create depth -- foreground particles larger and more opaque, background particles smaller and faded. More debris visible at the cloud edges flying outward. A subtle circular shockwave ring (1px, 40% opacity) marks the blast radius.

### Frame 7: Impact - Dust Explosion Frame 3
- **Position in sheet:** 336,0 to 383,47
- **Description:** Dust cloud dissipating. Cloud reduced to ~40% of frame, breaking into separate smaller puffs. "SWOOOSH" text fading (60% opacity), letters starting to drift apart. Debris settling downward with slight gravity. Individual dust particles visible at edges as they float away. The air is "clearing" -- more transparent background visible through the cloud.

### Frame 8: Dust Burst Effect 1
- **Position in sheet:** 384,0 to 431,47
- **Description:** Small ground-level dust puff for continuous sweep effect. 3-4 small dust clouds (3x3px each) arranged in a line following the sweep direction. Each cloud slightly different shape. Colors are muted dust tones. This plays during the sweep animation to add ground interaction. Light and subtle -- not as dramatic as the impact dust explosion.

### Frame 9: Dust Burst Effect 2
- **Position in sheet:** 432,0 to 479,47
- **Description:** Second small ground-level dust puff, offset from Frame 8. Clouds have moved/expanded slightly from Frame 8 positions. Some are fading (lower opacity). New tiny particles appear at different positions. Creates continuous dust trail when alternated with Frame 8.

### Frame 10: Idle Effect - Bristle Sway 1
- **Position in sheet:** 480,0 to 527,47
- **Description:** Broom in resting position. Bristles lean slightly to the left (2px displacement at tips). A tiny dust mote (1x1px, dust color) floats near the bristle tips -- this broom never stops shedding dust. The handle is perfectly still but the bristles suggest latent energy. A single straw bristle at the edge twitches outward (1px).

### Frame 11: Idle Effect - Bristle Sway 2
- **Position in sheet:** 528,0 to 575,47
- **Description:** Bristles lean slightly to the right (2px displacement, mirroring Frame 10). The floating dust mote has moved to a new position. The twitchy bristle returns to its normal position. Together with Frame 10, creates a subtle "alive" broom effect -- the straw breathes.

## Sprite Sheet Summary

| Frame | Name                 | Position    | Purpose              |
|-------|----------------------|-------------|----------------------|
| 0     | static               | 0-47        | Inventory / UI icon  |
| 1     | sweep_windup         | 48-95       | Attack start         |
| 2     | sweep_full           | 96-143      | Attack peak sweep    |
| 3     | sweep_contact        | 144-191     | Hit moment           |
| 4     | sweep_followthrough  | 192-239     | Attack end           |
| 5     | impact_dust_1        | 240-287     | Dust explosion start |
| 6     | impact_dust_2        | 288-335     | Dust explosion peak  |
| 7     | impact_dust_3        | 336-383     | Dust explosion fade  |
| 8     | dust_trail_1         | 384-431     | Ground dust effect A |
| 9     | dust_trail_2         | 432-479     | Ground dust effect B |
| 10    | idle_sway_1          | 480-527     | Idle animation A     |
| 11    | idle_sway_2          | 528-575     | Idle animation B     |

## Phaser 3 Atlas Key
```
key: 'weapon_vassoura'
frameWidth: 48
frameHeight: 48
```

## Notes for Artist
- The broom must feel MASSIVE -- it is a weapon of the working class
- Straw bristles should look individually rendered at the edges, chaotic and wild
- The wooden handle should show years of abuse -- dents, grain, dark spots
- Dust clouds are a MAJOR visual feature -- they should feel thick and choking
- The Esplanada context means the dust is Brasilia's red earth mixed with concrete dust
- "SWOOOSH" text should feel like wind -- wavy, elongated letters
- The rusty wire binding is a detail that sells the broom's age and authenticity
- Think of a street sweeper who has been sweeping since the city was built in 1960
- Thick Crumb-style outlines on everything, especially the bristle silhouette
