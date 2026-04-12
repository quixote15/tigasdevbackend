# Chinelo Havaianas - Sprite Specification

## Overview
- **Weapon Type:** Melee (initial weapon)
- **Sprite Dimensions:** 32x32px
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 10 (1 static + 4 swing + 3 impact + 2 idle)
- **Sprite Sheet Size:** 320x32px
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (16, 28) -- handle grip point

## Color Palette

| Element              | Hex Code  | Usage                          |
|----------------------|-----------|--------------------------------|
| Rubber Blue (main)   | `#1A5276` | Flip-flop sole body            |
| Rubber Blue (light)  | `#2E86C1` | Top surface highlights         |
| Rubber Blue (dark)   | `#0E3651` | Sole underside / shadows       |
| Strap Color          | `#154360` | Toe strap (Y-shape)            |
| Strap Highlight      | `#2874A6` | Strap light edge               |
| Logo White           | `#F0F0E8` | Havaianas-style logo mark      |
| Logo Off-White       | `#D5D5C8` | Logo shadow/depth              |
| Outline Black        | `#1A1A1A` | Thick 2px outlines (Crumb)     |
| Shadow Dark          | `#0D0D0D` | Drop shadow, 50% opacity       |
| Impact Yellow        | `#F4D03F` | "THWACK" onomatopeia text      |
| Impact Red           | `#E74C3C` | Impact flash / onomatopeia BG  |
| Skin Debris          | `#A0785A` | Zombie skin particles on hit   |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 31,31
- **Description:** Chinelo seen from slightly above (top-down isometric). Sole faces mostly upward, angled ~30deg to suggest readiness. Classic Havaianas shape -- oval sole tapered at toe, Y-strap visible. DISPROPORTIONALLY LARGE -- fills ~80% of the 32x32 frame. Thick black outlines (2px minimum). Small faux-logo mark on the insole in off-white. Subtle drop shadow underneath (2px offset, 50% opacity black).
- **Style Notes:** Exaggerated proportions -- sole is chunky and rubbery-looking. The blue is saturated but slightly dirty/worn. Small scuff marks on sole (1-2 dark pixels). The strap has visible wear.

### Frame 1: Swing Animation - Wind-up
- **Position in sheet:** 32,0 to 63,31
- **Description:** Chinelo pulled back behind the player's implied position. Rotated ~45deg clockwise from resting. Slight squash effect (compressed 2px horizontally, stretched 2px vertically) to suggest elastic rubber tension. Motion blur line (1px white, 40% opacity) trailing from toe end. The strap flexes slightly outward.

### Frame 2: Swing Animation - Mid-swing
- **Position in sheet:** 64,0 to 95,31
- **Description:** Chinelo at peak velocity, nearly horizontal. Maximum stretch effect (stretched 3px in swing direction). Two motion blur lines trailing behind (1px each, 60% and 30% opacity). The sole shows its underside partially -- revealing tread pattern (crosshatch, 1px dark blue lines). Slight rotation blur on edges.

### Frame 3: Swing Animation - Contact
- **Position in sheet:** 96,0 to 127,31
- **Description:** Chinelo at moment of impact. SQUASHED flat against the hit point -- compressed significantly (roughly 28x20px shape, wider than tall). The rubber deforms visibly. 2-3 small debris particles (skin-colored, 2x2px) fly off at 45deg angles. A small white starburst (6x6px) appears at the contact point. The strap wobbles outward from deformation.

### Frame 4: Swing Animation - Follow-through
- **Position in sheet:** 128,0 to 159,31
- **Description:** Chinelo continuing past impact, now angled ~30deg past horizontal in opposite direction from wind-up. Returning to normal proportions (rubber bounce-back). Single motion blur line. The sole shows a faint imprint mark (1px lighter blue outline) suggesting the slap residue. Small rubber vibration lines (1px, 2 wavy lines near edges).

### Frame 5: Impact - "THWACK" Frame 1
- **Position in sheet:** 160,0 to 191,31
- **Description:** Bold "THWACK" text appears, comic-book style. Letters are LARGE (fill ~70% of frame), bright yellow (#F4D03F) with red (#E74C3C) drop shadow (1px offset). Jagged starburst outline behind text in white. Letters are chunky, hand-drawn style with uneven baselines. 3-4 small debris particles (mixed skin-colored and blue rubber flecks) radiate outward from center.

### Frame 6: Impact - "THWACK" Frame 2
- **Position in sheet:** 192,0 to 223,31
- **Description:** "THWACK" text at maximum size, slightly larger than Frame 5 (scale ~110%). Colors intensify -- yellow becomes brighter, red shadow deepens. Starburst lines extend to frame edges. Additional impact lines (4 radial lines from center, 1px white). Debris particles have moved further outward. Slight screen-flash effect -- 1px white border around entire frame at 30% opacity.

### Frame 7: Impact - "THWACK" Frame 3
- **Position in sheet:** 224,0 to 255,31
- **Description:** "THWACK" text fading -- scale back to 90%, opacity reduced to ~60%. Starburst lines thinner and fading. Debris particles at frame edges, nearly gone. Yellow text becomes slightly more orange as it dissipates. This frame bridges back to normal gameplay. The fading creates a ghosting effect.

### Frame 8: Idle Effect - Rubber Wobble 1
- **Position in sheet:** 256,0 to 287,31
- **Description:** Chinelo in resting position with subtle idle animation. Slight leftward lean (2px tilt). The rubber has a very subtle "breathing" squash -- 1px wider than static frame. A tiny highlight glint (1px white pixel) appears on the upper-left of the sole surface, suggesting rubber sheen. Strap is relaxed.

### Frame 9: Idle Effect - Rubber Wobble 2
- **Position in sheet:** 288,0 to 319,31
- **Description:** Chinelo mirrors Frame 8 with slight rightward lean (2px tilt opposite direction). 1px taller than static frame (stretch counterpart to Frame 8's squash). Highlight glint moves to upper-right. Together Frames 8-9 create a gentle rubbery idle sway when looped. Strap mirrors the lean direction.

## Sprite Sheet Summary

| Frame | Name                | Position    | Purpose              |
|-------|---------------------|-------------|----------------------|
| 0     | static              | 0-31        | Inventory / UI icon  |
| 1     | swing_windup        | 32-63       | Attack start         |
| 2     | swing_mid           | 64-95       | Attack peak          |
| 3     | swing_contact       | 96-127      | Hit moment           |
| 4     | swing_followthrough  | 128-159     | Attack end           |
| 5     | impact_thwack_1     | 160-191     | Onomatopeia appear   |
| 6     | impact_thwack_2     | 192-223     | Onomatopeia peak     |
| 7     | impact_thwack_3     | 224-255     | Onomatopeia fade     |
| 8     | idle_wobble_1       | 256-287     | Idle animation A     |
| 9     | idle_wobble_2       | 288-319     | Idle animation B     |

## Phaser 3 Atlas Key
```
key: 'weapon_chinelo'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- The chinelo must look GROTESQUELY oversized -- like a weapon, not a shoe
- Outlines must be thick and uneven (Robert Crumb style)
- The blue should look worn and dirty, not pristine
- Rubber deformation on impact should be exaggerated and cartoony
- "THWACK" text must look hand-lettered, not typeset
- Every frame should feel slightly "wrong" -- asymmetric, wobbly, alive
- The Havaianas logo is a PARODY -- do not use the actual logo, just suggest it
