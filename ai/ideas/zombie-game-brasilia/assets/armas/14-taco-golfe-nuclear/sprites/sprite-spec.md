# Taco de Golfe Nuclear - Sprite Specification

## Overview
- **Weapon Type:** Ranged/Melee Hybrid (Boss Weapon - Trump)
- **Sprite Dimensions:** 48x48px (BOSS SCALE -- grotesquely golden and oversized)
- **Projectile Dimensions:** 32x32px (explosive golf balls with Trump's face)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 16 (1 static + 4 swing + 4 projectile + 3 impact-hit + 3 impact-miss + 1 idle)
- **Sprite Sheet Size:** 768x48px (weapon) / 128x32px (projectiles)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (24, 44) -- shaft grip point

## Color Palette

| Element                | Hex Code  | Usage                                  |
|------------------------|-----------|----------------------------------------|
| Gold Main              | `#D4A017` | Club body, primary surface             |
| Gold Bright            | `#FFD700` | Highlights, sparkle points             |
| Gold Dark              | `#A07D14` | Shadows, depth on club                 |
| Gold Tacky             | `#F5C518` | Extra gaudy highlights                 |
| Trump Orange           | `#E8820C` | Trump face on golf balls               |
| Trump Hair Yellow      | `#F0C040` | Hair on golf ball face                 |
| Trump Skin Light       | `#F5B87A` | Face highlight on balls                |
| White Ball             | `#F8F8F0` | Golf ball base color                   |
| Ball Dimple Shadow     | `#D8D8D0` | Golf ball texture dimples              |
| Nuclear Green          | `#39FF14` | Radioactive glow on club head          |
| Nuclear Green Dark     | `#228B22` | Nuclear trail darker shade             |
| Explosion Orange       | `#FF6B00` | Explosion fireball core                |
| Explosion Yellow       | `#FFE000` | Explosion flash outer                  |
| Explosion Red          | `#CC0000` | Explosion inner fire                   |
| Text Red (TREMENDOUS)  | `#FF0000` | "TREMENDOUS!" onomatopeia             |
| Text Blue (FAKE NEWS)  | `#0040FF` | "FAKE NEWS!" text                      |
| Diamond Sparkle        | `#FFFFFF` | Tacky diamond encrust highlights       |
| Shaft Chrome           | `#C0C0C0` | Club shaft (also gold-plated)          |
| Outline Black          | `#1A1A1A` | Thick 2px outlines (Crumb style)       |
| Shadow Dark            | `#0D0D0D` | Drop shadow, 50% opacity              |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 47,47
- **Description:** ABSURDLY gaudy golden golf club seen from top-down isometric. The club head is a MASSIVE driver, disproportionally large (fills upper 60% of frame). Entirely gold-plated with visible fake diamond studs (2-3 white sparkle pixels on the club head). The shaft is also gold, running diagonally from club head to lower-right corner. A faint nuclear green glow emanates from the club head (2px green aura, 30% opacity). The club face has a tiny "T" monogram engraved in darker gold. Tacky grip wrapped in what appears to be gold leather at the handle end. Thick 2px black outlines. Drop shadow (3px, 50% opacity). Everything about this club screams NEW MONEY EXCESS.
- **Style Notes:** This is the UGLIEST, most garish golf club imaginable. Gold on gold on gold. The diamonds are clearly fake (oversized sparkle points). The nuclear glow suggests this isn't just tacky -- it's DANGEROUS. Think Trump Tower aesthetics compressed into 48 pixels.

### Frame 1: Swing Animation - Backswing (The Best Backswing)
- **Position in sheet:** 48,0 to 95,47
- **Description:** Club pulled back to upper-right corner of frame, rotated ~60deg clockwise. The gold surfaces catch maximum light -- 4-5 sparkle pixels (white, 1x1px) appear on the club head. The nuclear green aura intensifies (40% opacity, 3px wide). A golf ball appears at the bottom-left of the frame, sitting on a tiny tee -- white with visible dimple texture and a tiny caricature of Trump's face (orange circle with yellow hair swoosh, 4x4px). The shaft bends slightly (exaggerated flex). Motion anticipation line (1px gold, trailing from club head).

### Frame 2: Swing Animation - Downswing (Tremendous Power)
- **Position in sheet:** 96,0 to 143,47
- **Description:** Club at peak velocity, sweeping left-to-right at maximum speed. The club head stretches 4px in swing direction (speed distortion). Nuclear green trail streaks behind the club head (5px trail, fading from 60% to 10% opacity). Three gold motion lines follow the swing path. The gold surface blurs -- sparkle pixels stretch into 2px streaks. The golf ball is about to be struck -- compressed slightly from the incoming force shockwave. Dollar sign particles ($, 1px, gold) scatter in the wake.

### Frame 3: Swing Animation - Contact (FORE!)
- **Position in sheet:** 144,0 to 191,47
- **Description:** EXPLOSIVE contact. The club head DEFORMS the golf ball which squashes flat (8x4px, compressed). A BURST of nuclear green and gold energy at the contact point -- starburst (20px diameter) of alternating green and gold rays. The Trump face on the ball distorts comically (stretched by impact). 4-5 gold sparkle fragments fly off the club head from the force. Small dollar bill particles ($$$) erupt from impact. The club head has a tiny crack (1px dark line) from the nuclear force. A ring of green energy (24px diameter, 1px) expands from contact.

### Frame 4: Swing Animation - Follow-through (Perfect Swing)
- **Position in sheet:** 192,0 to 239,47
- **Description:** Club continues past impact, now pointing upper-left. The gold surface gleams with afterglow. Nuclear green residue trails from club head (3 green dots, fading). The golf ball is GONE (launched as projectile). A faint afterimage (20% opacity gold silhouette) of the club lingers at the contact point. Single gold motion line. The shaft returns to straight. A tiny puff of green smoke (4x4px, nuclear green, 40% opacity) at the tee position where the ball was.

### Frame 5: Projectile - Trump Ball Launch (32x32px)
- **Position in sheet:** 0,0 to 31,31 (projectile sheet)
- **Description:** Golf ball in flight, seen top-down. White ball (12px diameter) centered in frame, with visible dimple pattern (tiny shadow dots). Trump's face caricature on the ball -- orange-skinned, yellow hair swept back, tiny eyes, pouting lips (all within ~8x8px on the ball surface). The face is GROTESQUE and exaggerated. Nuclear green trail (4px wide, 10px long) streams behind the ball. Small gold sparkle (1x1px) at the ball's leading edge. The ball has a faint gold tint from the club's plating.

### Frame 6: Projectile - Trump Ball Mid-flight (32x32px)
- **Position in sheet:** 32,0 to 63,31 (projectile sheet)
- **Description:** Golf ball spinning -- Trump's face has rotated 90deg (now sideways, even more grotesque). The dimple pattern shifts to show rotation. Nuclear green trail widens (6px) and lengthens (14px). The ball pulses slightly larger (13px diameter -- nuclear energy building). Two sparkle points trail behind. Dollar sign ($) particle (2px, gold) floats in the wake. The ball vibrates with barely-contained explosive energy.

### Frame 7: Projectile - Trump Ball Wobble (32x32px)
- **Position in sheet:** 64,0 to 95,31 (projectile sheet)
- **Description:** Ball wobbling erratically in flight -- shifted 1px off-center (jerky Andre Guedes style). Trump's face rotated 180deg (upside down, comically warped). Nuclear green trail flickers (broken into segments). The ball surface shows cracks (2-3 dark lines, 1px) as nuclear energy destabilizes. Hair on the face flies wildly. Small green sparks (2, 1x1px) fly off the ball. This frame sells the unstable, dangerous nature of the projectile.

### Frame 8: Projectile - Trump Ball Pre-impact (32x32px)
- **Position in sheet:** 96,0 to 127,31 (projectile sheet)
- **Description:** Ball glowing intensely -- nuclear green aura expands to 4px around the ball. Trump's face is SCREAMING (mouth wide open on the caricature). Cracks widen with green light leaking through. The ball is about to EXPLODE. No trail -- all energy concentrated forward. A warning ring (16px diameter, 1px, red) appears around the ball. The entire projectile pulses between 14px and 12px diameter (throbbing).

### Frame 9: Impact (Hit) - "TREMENDOUS!" Frame 1
- **Position in sheet:** 240,0 to 287,47
- **Description:** MASSIVE EXPLOSION. Orange-red fireball fills 70% of frame. At the center, the golf ball disintegrates -- white fragments fly outward mixed with fire. "TREMENDOUS!" text begins appearing in BOLD red (#FF0000) letters with gold (#FFD700) outline, comic-book style, hand-lettered with uneven baseline. The text is HUGE, arcing across the upper portion. Fireball has concentric rings: red core, orange middle, yellow outer. Small mushroom cloud shape beginning to form (nuclear golf ball!). Green radiation particles (4, 1x1px) in the explosion mix.

### Frame 10: Impact (Hit) - "TREMENDOUS!" Frame 2
- **Position in sheet:** 288,0 to 335,47
- **Description:** "TREMENDOUS!" at MAXIMUM SIZE (fills 80% of frame width). Letters vibrate (each shifted 1px randomly). Fireball at peak -- tiny mushroom cloud fully formed (stem 4px wide, cap 16px wide, all in orange/red gradient). Dollar signs ($$$) rain down from the explosion (3-4, gold, 2px each). Green radiation symbol (3-wedge, 6x6px) briefly visible in the cloud center. Screen flash: 2px red border at 40% opacity. The explosion is GLORIOUSLY over-the-top, like a Michael Bay film compressed into 48 pixels.

### Frame 11: Impact (Hit) - "TREMENDOUS!" Frame 3
- **Position in sheet:** 336,0 to 383,47
- **Description:** "TREMENDOUS!" fading (70% scale, 50% opacity), red shifting to dark red. Mushroom cloud dissipating into wisps (orange to dark grey at edges). Green radiation residue circle on the ground (16px diameter, nuclear green, 30% opacity). Dollar sign particles settling. Smoke wisps (3-4, grey, 2x2px) drift upward. Scorched ground mark (8px dark circle) remains at impact center. Transition frame.

### Frame 12: Impact (Miss) - "FAKE NEWS!" Frame 1
- **Position in sheet:** 384,0 to 431,47
- **Description:** The golf ball hits the GROUND (no target). Small pathetic poof of dirt/dust (brown particles, 4-5, 2x2px). "FAKE NEWS!" text appears in BLUE (#0040FF) bold letters with white outline, comic-book rage font. The text is angry -- letters are JAGGED, angular, accusatory. Trump's face fragment (from the shattered ball) lies on the ground looking displeased (3x3px orange scowl). A tiny American flag (4x3px) plants itself at the miss point (comedy). The explosion is MUCH smaller than the hit version -- deliberately underwhelming.

### Frame 13: Impact (Miss) - "FAKE NEWS!" Frame 2
- **Position in sheet:** 432,0 to 479,47
- **Description:** "FAKE NEWS!" at peak size, letters vibrating with indignation. The text shakes more aggressively than the hit version -- this is ANGRY text. An additional "SAD!" appears below in smaller gold text (8px wide). The dirt poof is at maximum spread. The tiny American flag waves. A single tumbleweed pixel (2x2px, brown) rolls across the bottom of the frame. The mood is pathetic disappointment vs the hit's triumphant explosion.

### Frame 14: Impact (Miss) - "FAKE NEWS!" Frame 3
- **Position in sheet:** 480,0 to 527,47
- **Description:** "FAKE NEWS!" fading rapidly (60% scale, 40% opacity). "SAD!" also fading. Dust settles. The American flag falls over (tilted 45deg). Trump face fragment remains on ground, scowling. Tumbleweed exits frame. A small crack in the ground (4px line, dark grey) remains at impact. The pathos is thick. Transition frame back to gameplay.

### Frame 15: Idle Effect - Gold Gleam
- **Position in sheet:** 528,0 to 575,47
- **Description:** Club at rest with cycling gold highlights. A sparkle (2x2px, white > gold) travels along the club head surface in a predictable arc (upper-left to lower-right of club face). Nuclear green glow pulses between 20% and 40% opacity. The tacky diamond studs twinkle (alternating which ones are white vs slightly dimmer). The shaft has a single traveling gleam line (1px white, moves from grip to head). Everything shimmers. This single idle frame is tweened in Phaser for continuous sparkle motion.

## Sprite Sheet Summary

| Frame | Name                | Position      | Purpose                    |
|-------|---------------------|---------------|----------------------------|
| 0     | static              | 0-47          | Inventory / UI icon        |
| 1     | swing_backswing     | 48-95         | Attack wind-up             |
| 2     | swing_downswing     | 96-143        | Attack peak velocity       |
| 3     | swing_contact       | 144-191       | Hit moment                 |
| 4     | swing_followthrough | 192-239       | Attack recovery            |
| 5     | trumpball_1         | proj 0-31     | Projectile launch          |
| 6     | trumpball_2         | proj 32-63    | Projectile mid-flight      |
| 7     | trumpball_3         | proj 64-95    | Projectile wobble          |
| 8     | trumpball_4         | proj 96-127   | Projectile pre-impact      |
| 9     | hit_tremendous_1    | 240-287       | Hit onomatopeia appear     |
| 10    | hit_tremendous_2    | 288-335       | Hit onomatopeia peak       |
| 11    | hit_tremendous_3    | 336-383       | Hit onomatopeia fade       |
| 12    | miss_fakenews_1     | 384-431       | Miss onomatopeia appear    |
| 13    | miss_fakenews_2     | 432-479       | Miss onomatopeia peak      |
| 14    | miss_fakenews_3     | 480-527       | Miss onomatopeia fade      |
| 15    | idle_gleam          | 528-575       | Idle gold sparkle          |

## Phaser 3 Atlas Key
```
key: 'weapon_taco_golfe_nuclear'
frameWidth: 48
frameHeight: 48
```
```
key: 'projectile_trump_ball'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- EVERYTHING is gold. The shaft, the head, the grip. It's offensively, tastelessly gold.
- The Trump face on the golf balls must be a GROTESQUE caricature -- orange skin, yellow combover, tiny pursed lips, beady eyes
- The nuclear green glow makes this weapon feel genuinely DANGEROUS despite its absurdity
- The contrast between HIT ("TREMENDOUS!") and MISS ("FAKE NEWS!") reactions is the comedic core
- The mushroom cloud on hit is ESSENTIAL -- a tiny nuclear explosion from a golf ball
- Dollar signs ($$$) should be a recurring particle motif -- money rains from this weapon
- "FAKE NEWS!" on miss should feel ANGRIER and more PATHETIC than the triumphant hit explosion
- The fake diamonds are a key detail -- they sparkle TOO much, obviously costume jewelry
- Robert Crumb style: this weapon is a monument to grotesque excess
- The American flag on miss is a small comedy detail -- it plants triumphantly then falls over
- The "SAD!" text on miss is smaller and more pitiful than "FAKE NEWS!"
