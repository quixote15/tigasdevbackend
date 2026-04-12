# Santinho Explosivo - Sprite Specification

## Overview
- **Weapon Type:** Projectile (thrown explosive)
- **Sprite Dimensions:** 32x32px (pamphlet held + projectile), 48x48px (explosion effect)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 16
  - Held weapon sheet (32x32): 1 static + 3 throw + 4 flight + 2 idle = 10 frames
  - Explosion sheet (48x48): 4 explosion + 2 aftermath = 6 frames
- **Sprite Sheet Sizes:**
  - santinho_weapon.png: 320x32px (10 frames x 32px)
  - santinho_explosion.png: 288x48px (6 frames x 48px)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Center (16,16 for held / 24,24 for explosion)

## Color Palette

| Element                    | Hex Code  | Usage                                  |
|----------------------------|-----------|----------------------------------------|
| Paper White                | `#F0EDE4` | Pamphlet base color                    |
| Paper Aged                 | `#E8DCC8` | Aged/dirty paper tone                  |
| Paper Crease               | `#C4B89C` | Fold lines and creases                 |
| Candidate Face (skin)      | `#DEB887` | Caricature face skin                   |
| Candidate Face (shadow)    | `#A0785A` | Face shadow tone                       |
| Candidate Suit             | `#1A3C5E` | Generic politician suit blue           |
| Candidate Tie              | `#CC0000` | Power tie red                          |
| Candidate Smile            | `#FFFFFF` | Exaggerated fake white teeth           |
| Text Print (black)         | `#1A1A1A` | Printed slogans and number             |
| Text Print (red)           | `#CC2200` | "VOTE" text accent                     |
| Number Blue                | `#0044CC` | Candidate number (large)               |
| Fuse Glow                  | `#FF6600` | Lit fuse / burning edge                |
| Fuse Spark                 | `#FFD700` | Fuse sparks                            |
| Fuse Smoke                 | `#666666` | Fuse smoke trail                       |
| Explosion Orange           | `#FF6B00` | Main explosion fireball                |
| Explosion Yellow           | `#FFD700` | Explosion center/hot core              |
| Explosion Red              | `#CC0000` | Explosion outer ring                   |
| Explosion White            | `#FFFFFF` | Flash center                           |
| Confetti Green             | `#009B3A` | Brazil green confetti                  |
| Confetti Yellow            | `#FEDF00` | Brazil yellow confetti                 |
| Confetti Blue              | `#0044CC` | Party confetti                         |
| Confetti Pink              | `#FF69B4` | Campaign confetti                      |
| Outline Black              | `#1A1A1A` | Thick outlines                         |
| Shadow Dark                | `#0D0D0D` | Drop shadow                            |

## Frame-by-Frame Descriptions (Weapon - 32x32px)

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 31,31
- **Description:** An electoral pamphlet ("santinho") seen from above. Rectangular paper roughly 20x24px within the 32x32 frame. The front shows a GROTESQUE caricature of a generic politician's face -- huge fake smile with oversized white teeth, beady eyes, receding hairline, blue suit and red tie. Below the face, a large candidate number in blue (like "00" or "13" -- keep it generic). Above the face, text reading "VOTE" in red. The paper edges are slightly crinkled and uneven (not perfectly straight). A small burning fuse sticks out of the top-right corner -- this is no ordinary pamphlet. The fuse tip glows orange with a tiny yellow spark. Light drop shadow underneath. Thick Crumb-style outlines on everything.
- **Style Notes:** The politician caricature must be GROTESQUE -- Robert Crumb meets Brazilian political cartoons. Exaggerated features, sinister smile that pretends to be friendly. The pamphlet looks cheap and mass-produced. The fuse makes it clear this is an improvised explosive device disguised as electoral propaganda.

### Frame 1: Throw Animation - Wind-up
- **Position in sheet:** 32,0 to 63,31
- **Description:** The santinho pulled back, preparing to throw like a frisbee. The pamphlet is tilted ~30deg, slightly squashed horizontally (anticipation compression). The fuse is now clearly burning -- the orange glow is larger (3px instead of 1px), with a smoke trail (2-3px gray puff) rising from it. A 1px motion line suggests the pull-back direction. The politician's face on the pamphlet seems to grimace from the motion (a subtle 1px shift in the mouth -- creative license).

### Frame 2: Throw Animation - Release
- **Position in sheet:** 64,0 to 95,31
- **Description:** The santinho at the moment of release, spinning. The pamphlet rotated ~45deg from rest position, in the transition from hand to air. Motion blur trails (2 copies at 40% and 20% opacity) show the spin. The fuse is burning brighter -- 4px glow with sparks shooting off (2-3 yellow 1x1px sparks). The paper shows slight flutter distortion (edges wavy). Speed lines emanate from the release point.

### Frame 3: Throw Animation - In Air (initial)
- **Position in sheet:** 96,0 to 127,31
- **Description:** The santinho now fully airborne and beginning its frisbee flight. Rotated 90deg from rest. Strong motion blur. The fuse is actively burning down (shorter than in static frame -- the clock is ticking). Spark trail behind. The politician's face appears and disappears as the pamphlet spins -- in this frame it is mostly edge-on (thin sliver showing paper thickness). A faint smoke trail follows the flight path.

### Frame 4: Projectile Flight - Face Up
- **Position in sheet:** 128,0 to 159,31
- **Description:** Santinho mid-flight, politician's face fully visible from above (full front of pamphlet). The paper is flat-on in its spin cycle. Face visible with all its grotesque detail. Number visible. Fuse is almost burned to the paper edge -- DANGER. Spark trail intense. Smoke trail behind. Subtle green glow around the pamphlet edges (explosive charge warming up).

### Frame 5: Projectile Flight - Edge
- **Position in sheet:** 160,0 to 191,31
- **Description:** Santinho mid-flight, seen edge-on (just a thin line of paper, ~4px wide, full 24px tall). This is the frisbee spin showing the paper's profile. The fuse spark is visible at the edge. Motion blur trails. Smoke trail. The thin profile makes it look fast and dangerous.

### Frame 6: Projectile Flight - Back
- **Position in sheet:** 192,0 to 223,31
- **Description:** Santinho mid-flight, showing the back of the pamphlet. The back is mostly blank paper (aged white) with a small "MATERIAL ELEITORAL" legal disclaimer text (illegible at this scale -- just small 1px marks). Maybe a small fingerprint smudge (3x3px slightly darker area). Fuse almost gone. Green glow from edges increasing. This pamphlet is about to blow.

### Frame 7: Projectile Flight - Other Edge
- **Position in sheet:** 224,0 to 255,31
- **Description:** Santinho mid-flight, other edge-on view (mirror of Frame 5 but with fuse on the opposite visual side). Completes the 360-degree spin cycle when combined with frames 4-5-6-7. Spark and smoke trails continue. The paper edge glows slightly orange now -- the explosive compound is activating.

### Frame 8: Idle Effect - Fuse Flicker 1
- **Position in sheet:** 256,0 to 287,31
- **Description:** Santinho in hand, at rest. The fuse spark is large and bright (3px glow), actively sputtering. A tiny smoke puff (2x2px gray) rises from the fuse. The politician on the pamphlet has a nervous expression (a creative 1px eyebrow shift -- the face knows what is coming). Paper is still with slight glow at the fuse corner. Idle state A.

### Frame 9: Idle Effect - Fuse Flicker 2
- **Position in sheet:** 288,0 to 319,31
- **Description:** Santinho in hand. Fuse spark is smaller/dimmer (1px glow -- the flicker effect). Smoke puff has drifted to a new position. The politician's expression returns to the standard fake smile. No edge glow. Idle state B. Alternating with Frame 8 creates a flickering fuse idle animation.

## Frame-by-Frame Descriptions (Explosion - 48x48px)

### Explosion Frame 0: Detonation
- **Position in sheet:** 0,0 to 47,47
- **Description:** The moment of explosion. A bright white-yellow core (8x8px, #FFFFFF center, #FFD700 edge) at the impact center. Orange fireball (20x20px) expanding from the core. The pamphlet is disintegrating -- paper shreds (3-4 fragments, 2x3px each, paper-colored) flying outward from the core. The politician's face is splitting apart in the explosion -- one eye goes one way, the smile another (2-3 face-colored fragments). First confetti pieces appear (4-6, 2x2px, in campaign colors: green, yellow, blue, pink). Initial shockwave ring (1px white circle, ~24px diameter).

### Explosion Frame 1: Fireball Peak
- **Position in sheet:** 48,0 to 95,47
- **Description:** Maximum fireball expansion. The fireball fills ~70% of the 48x48 frame. Yellow-white core (#FFD700 to #FFFFFF), orange mid-ring (#FF6B00), red outer ring (#CC0000). Heavy black smoke wisps (4-5, 3x3px, dark gray) at the fireball edges. MASSIVE confetti burst -- 10-15 pieces of colored confetti (2x2px each) in campaign colors, filling the space between fireball edge and frame edge. Paper fragments further out, some on fire (orange-tipped). "BOOM!" onomatopeia text beginning to appear through the fireball in bright yellow, jagged hand-lettered style. Face fragments scattered at maximum distance. The shockwave ring is now at ~40px diameter.

### Explosion Frame 2: Confetti Rain
- **Position in sheet:** 96,0 to 143,47
- **Description:** Fireball subsiding to ~50% of frame. Colors shifting -- more red and dark orange, less yellow/white (cooling). "BOOM!" text fully visible, large and bold, yellow (#FFD700) with orange (#FF6B00) shadow. The real star of this frame: CONFETTI EVERYWHERE. 15-20 confetti pieces of varying sizes (1x1px to 3x3px) scattered across the entire frame, in all campaign colors. Some confetti pieces are tiny politician faces (2x2px caricatures). Paper shreds still floating. Smoke thickening at top (rising). Multiple scattered fragments of the original pamphlet identifiable -- a torn "VOTE" text, half a candidate number.

### Explosion Frame 3: Aftermath Cloud
- **Position in sheet:** 144,0 to 191,47
- **Description:** Fireball reduced to embers (15x15px area, dark red/orange glow). Thick smoke cloud dominates upper portion (dark gray, ~60% opacity). Confetti settling -- pieces at lower positions now, some fading. "BOOM!" text fading (40% opacity), letters drifting apart. Ground area shows blast mark -- a dark circular scorch (8x8px, dark brown/black). Scattered confetti on the ground (flattened pieces, no longer floating). Last fragments of the politician's face settling -- the caricature is destroyed but recognizable debris remains.

### Explosion Frame 4: Smoke Dissipate 1
- **Position in sheet:** 192,0 to 239,47
- **Description:** Smoke cloud thinning and rising (shifted upward 4px from Frame 3). Embers fading (5x5px area, barely glowing). Confetti mostly settled on ground. A few last pieces flutter down. Scorch mark clearly visible. Faint campaign color tint in the smoke (the confetti has colored the air). Very faint "BOOM!" ghost text (10% opacity). The air is clearing.

### Explosion Frame 5: Smoke Dissipate 2
- **Position in sheet:** 240,0 to 287,47
- **Description:** Final dissipation frame. Smoke nearly gone (2-3 thin wisps at 20% opacity). No embers. Ground scorch mark remains (this persists as a ground decal in gameplay). A few confetti pieces on the ground. One last tiny politician face fragment (1x1px) settles. Clean air returning. This frame transitions back to normal gameplay. The political pamphlet has fulfilled its true purpose -- destruction.

## Sprite Sheet Summary (Weapon - 32x32)

| Frame | Name                | Position    | Purpose                  |
|-------|---------------------|-------------|--------------------------|
| 0     | static              | 0-31        | Inventory / UI icon      |
| 1     | throw_windup        | 32-63       | Throw preparation        |
| 2     | throw_release       | 64-95       | Release moment           |
| 3     | throw_initial       | 96-127      | Initial flight           |
| 4     | flight_face_up      | 128-159     | Flight spin - front      |
| 5     | flight_edge_a       | 160-191     | Flight spin - edge       |
| 6     | flight_back         | 192-223     | Flight spin - back       |
| 7     | flight_edge_b       | 224-255     | Flight spin - other edge |
| 8     | idle_fuse_bright    | 256-287     | Idle fuse flicker A      |
| 9     | idle_fuse_dim       | 288-319     | Idle fuse flicker B      |

## Sprite Sheet Summary (Explosion - 48x48)

| Frame | Name                | Position    | Purpose                  |
|-------|---------------------|-------------|--------------------------|
| 0     | explode_detonate    | 0-47        | Initial detonation       |
| 1     | explode_fireball    | 48-95       | Peak fireball + "BOOM!"  |
| 2     | explode_confetti    | 96-143      | Confetti rain peak       |
| 3     | explode_aftermath   | 144-191     | Aftermath cloud          |
| 4     | smoke_dissipate_1   | 192-239     | Smoke clearing A         |
| 5     | smoke_dissipate_2   | 240-287     | Smoke clearing B (final) |

## Phaser 3 Atlas Keys
```
// Held weapon + projectile
key: 'weapon_santinho'
frameWidth: 32
frameHeight: 32

// Explosion effect (larger)
key: 'santinho_explosion'
frameWidth: 48
frameHeight: 48
```

## Notes for Artist
- The politician caricature on the santinho is ESSENTIAL -- it must be grotesque, satirical
- Keep the politician generic (no specific real person) but recognizable as "Brazilian politician"
- The fake smile with oversized white teeth is the signature detail
- The burning fuse turns a piece of electoral trash into an improvised weapon -- guerrilla comedy
- Confetti in the explosion references the real confetti used in Brazilian campaigns
- Politician face fragments in the explosion add dark satirical humor
- "BOOM!" text should feel different from other weapons' onomatopeias -- more explosive, blockier
- The frisbee spin cycle (frames 4-5-6-7) must read clearly even at 32x32
- The explosion must feel SATISFYING -- this is the most visually spectacular weapon
- Scorch marks from the explosion should suggest a ground decal system
- Robert Crumb thick lines, underground comix ugliness on everything
- The whole concept: Brazilian electoral spam mail, weaponized. Maximum satire.
