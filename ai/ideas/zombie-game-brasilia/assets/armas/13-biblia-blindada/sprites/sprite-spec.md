# Biblia Sagrada Blindada - Sprite Specification

## Overview
- **Weapon Type:** Melee (Boss Weapon - Daciolo)
- **Sprite Dimensions:** 48x48px (BOSS SCALE -- absurdly oversized)
- **Projectile Dimensions:** 32x32px (holy light ray projectiles)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 17 (1 static + 4 swing + 4 projectile + 3 impact + 2 idle + 3 conversion special)
- **Sprite Sheet Size:** 816x48px (weapon) / 256x32px (projectiles)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (24, 44) -- spine grip point

## Color Palette

| Element                | Hex Code  | Usage                                |
|------------------------|-----------|--------------------------------------|
| Leather Brown (main)   | `#5B3A1A` | Bible cover, worn leather            |
| Leather Brown (dark)   | `#3B2410` | Cover creases, shadows               |
| Leather Brown (light)  | `#7A5230` | Cover highlights, worn edges         |
| Titanium Plate         | `#8C9EAE` | Armor plating on cover               |
| Titanium Highlight     | `#B8CCDB` | Metal sheen, rivet highlights        |
| Titanium Shadow        | `#5A6B78` | Metal depth, plate joins             |
| Gold Trim              | `#D4A017` | Cross on cover, page edge gilt       |
| Gold Bright            | `#F5D442` | Cross glow, gilt highlights          |
| Page Cream             | `#F0E6C8` | Exposed page edges                   |
| Page Shadow            | `#C9B894` | Page depth                           |
| Holy Light Yellow      | `#FFF8B0` | Divine ray core                      |
| Holy Light White       | `#FFFEF0` | Divine ray peak glow                 |
| Holy Light Gold        | `#FFD700` | Divine ray outer                     |
| Halo Gold              | `#FFE066` | Converted zombie halo                |
| Halo Crack Red         | `#CC3333` | Crooked halo cracks                  |
| Outline Black          | `#1A1A1A` | Thick 2px outlines (Crumb style)     |
| Shadow Dark            | `#0D0D0D` | Drop shadow, 50% opacity            |
| Rivet Steel            | `#6B7B8A` | Armor rivets on plating              |
| Blood Red              | `#8B0000` | Ribbon bookmark                      |
| "GLORIA" Yellow        | `#FFD700` | Text onomatopeia                     |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 47,47
- **Description:** MASSIVE Bible seen from top-down isometric angle. The book is comically huge -- fills 90% of the 48x48 frame. Thick leather cover with visible stitching. Titanium armor plates bolted onto front and back covers with visible hex rivets (4 per plate, 2x2px each). A large gold cross dominates the front cover, slightly off-center (hand-drawn imperfect). Page edges visible on right side, cream-colored with gold gilt. A blood-red ribbon bookmark dangles from the bottom. The armor plates have dents and scratches -- this Bible has seen COMBAT. Thick 2px black outlines on everything. Drop shadow (3px, 50% opacity).
- **Style Notes:** The titanium plating should look bolted on aftermarket -- not elegant, BRUTAL. Think tank armor welded onto a holy book. Rivets are oversized. The leather is cracked and battle-worn. The gold cross GLOWS faintly (1px yellow pixel halo around cross edges).

### Frame 1: Swing Animation - Wind-up (Heaven's Judgment Rising)
- **Position in sheet:** 48,0 to 95,47
- **Description:** Bible raised high above Daciolo's implied position, tilted back ~50deg. The book appears to GLOW from within -- 1px holy light yellow outline appears around the entire book over the black outline. Pages splay open slightly at the bottom edge (2-3px fan of cream pages). Small upward motion lines (2 white lines, 1px, 40% opacity) trail below. The gold cross on the cover brightens. The titanium plates catch light -- highlight pixels intensify on upper edges. A single tiny sparkle (2x2px white) appears above the book.

### Frame 2: Swing Animation - Mid-swing (Divine Smite Descending)
- **Position in sheet:** 96,0 to 143,47
- **Description:** Bible at peak velocity, crashing downward at ~30deg angle. Maximum stretch effect (3px elongated in swing direction). BRIGHT holy rays (3 rays, 1px wide, holy light yellow) shoot outward from the cross during the swing -- 8px long, at 45deg angles. Pages are fluttering violently -- cream pixels scatter at the trailing edge (3-4 particles, 2x1px). Titanium plates blur with speed. Two thick motion lines (2px, 60% opacity white) trail behind. The book seems to VIBRATE with righteous fury.

### Frame 3: Swing Animation - Contact (JUDGMENT DAY)
- **Position in sheet:** 144,0 to 191,47
- **Description:** Bible SLAMS flat at impact point. Massive squash deformation (42x28px compressed shape). The titanium plates CRACK outward on impact -- small fracture lines visible (1px dark lines on plates). EXPLOSION of holy light -- 6 rays burst outward from the center (holy light yellow core, gold outer, each 10px long, 2px wide). Pages ERUPT upward (6-8 cream page particles, 2x3px, flying in all directions). The gold cross is BLAZING white at center. A shockwave ring (1px gold circle, 40px diameter) expands from the hit point. Small sparks (3-4 white 1x1px) scattered around impact.

### Frame 4: Swing Animation - Follow-through (Amen)
- **Position in sheet:** 192,0 to 239,47
- **Description:** Bible bouncing back up from impact, returning to shape. Slight upward tilt (~20deg past rest). Residual glow fading on cross. 2-3 holy light particles (2x2px, gold, 60% opacity) drift upward like embers. Pages settling back into alignment -- 1-2 stray page corners still sticking out. Titanium plates show new dents from the impact. A faint golden afterimage (30% opacity silhouette of the Bible) lingers at the impact point below. Single motion line trailing.

### Frame 5: Projectile - Holy Ray 1 (Beam Launch)
- **Position in sheet:** 0,0 to 31,31 (projectile sheet)
- **Description:** A concentrated beam of holy light, seen top-down. Central core is blazing white (#FFFEF0, 2px wide), surrounded by holy light yellow (#FFF8B0, 4px wide halo), then gold (#FFD700, 2px outer glow, 40% opacity). The beam has a pointed tip like a spear. Small cross shape (4x4px, white) embedded in the beam's head. Tiny sparkle particles (1x1px, white) trail along the sides. The beam is ~24px long, 8px wide, centered in the 32x32 frame. Thick 1px dark gold outline separates layers.

### Frame 6: Projectile - Holy Ray 2 (Mid-flight)
- **Position in sheet:** 32,0 to 63,31 (projectile sheet)
- **Description:** Beam at maximum intensity. Core brightens -- white pixels expand to 3px wide. The cross shape at the tip rotates 45deg (now X-shaped). Halo pulses wider (6px). Small scripture letters (illegible, 1px dark gold marks) appear to swirl within the beam body like fragments of text caught in divine wind. Trail of 4 sparkle particles behind (diminishing size: 2x2, 2x1, 1x1, 1x1).

### Frame 7: Projectile - Holy Ray 3 (Flickering)
- **Position in sheet:** 64,0 to 95,31 (projectile sheet)
- **Description:** Beam flickers -- core narrows to 1px momentarily. The halo stutters (broken into 3 segments with 1px gaps). Cross at tip intact but dimmer. Scripture fragments more dispersed. This creates the jerky, twitchy feel of the Andre Guedes animation style. Trail particles spread wider apart.

### Frame 8: Projectile - Holy Ray 4 (Arriving)
- **Position in sheet:** 96,0 to 127,31 (projectile sheet)
- **Description:** Beam concentrated for impact -- tip widens into a blunt cross shape (8x8px). Core blazes back to maximum brightness. Halo contracts tight around the beam (compressed energy before detonation). No trail particles -- all energy focused forward. A tiny ring of gold (12px diameter, 1px) appears around the tip, foreshadowing the impact explosion.

### Frame 9: Impact - "GLORIA!" Frame 1
- **Position in sheet:** 240,0 to 287,47
- **Description:** Massive starburst of holy light fills ~80% of frame. At the center, bold text "GLORIA!" in chunky hand-lettered style -- letters are gold (#FFD700) with white (#FFFEF0) inner highlight and dark brown (#3B2410) drop shadow. Letters are LARGE, uneven, shaky -- like someone screaming. Radial light rays (8 rays, alternating holy light yellow and gold, from center to frame edges). Small floating pages (3-4, cream colored, 3x2px) swirl around the text. A miniature cross (4x4px, bright white) hovers above the "I" in GLORIA.

### Frame 10: Impact - "GLORIA!" Frame 2
- **Position in sheet:** 288,0 to 335,47
- **Description:** "GLORIA!" text at MAXIMUM size (110% scale). Letters vibrate -- each shifted 1px in random directions from Frame 9 positions. Light rays extend beyond frame edges. Color intensifies -- gold becomes near-white at centers. Additional exclamation marks appear ("GLORIA!!!") in smaller size orbiting the main text. Page particles at frame edges, almost gone. The entire frame has a 2px white border flash at 40% opacity (screen flash effect). Tiny angel wing shapes (3x2px, white) flank the text.

### Frame 11: Impact - "GLORIA!" Frame 3
- **Position in sheet:** 336,0 to 383,47
- **Description:** "GLORIA!" fading -- text at 80% scale, 50% opacity. Colors shift from gold to warm cream as light dissipates. Rays thin to 1px and retract toward center. Page particles gone. A faint golden residue circle (20px diameter, 20% opacity) lingers at impact center -- the "blessing mark." The miniature cross drifts upward and fades. Transition frame back to gameplay.

### Frame 12: Idle Effect - Holy Pulse 1
- **Position in sheet:** 384,0 to 431,47
- **Description:** Bible at rest with subtle divine idle animation. The gold cross on the cover pulses brighter -- highlight pixels expand by 1px outward. A faint halo of holy light (1px, holy light yellow, 30% opacity) surrounds the entire book. The ribbon bookmark sways slightly left. One tiny sparkle (1x1px, white) appears near the upper-right corner of the book, suggesting divine favor. Titanium plates reflect a subtle gleam (1px highlight shifts position from Frame 0).

### Frame 13: Idle Effect - Holy Pulse 2
- **Position in sheet:** 432,0 to 479,47
- **Description:** Cross dims back to normal brightness, halo contracts and disappears. The sparkle moves to the opposite corner (upper-left). Ribbon bookmark sways right. A barely-visible page corner lifts (1px cream pixel) as if an unseen wind (the Holy Spirit?) ruffles the pages. Titanium gleam shifts to opposite edge. Together Frames 12-13 create a gentle, reverent breathing glow when looped.

### Frame 14: Special - Conversion Blast 1 (Soul Capture)
- **Position in sheet:** 480,0 to 527,47
- **Description:** Bible OPENS explosively -- covers fly apart to 45deg angle, revealing blazing white pages within. A massive cross-shaped light beam (fills 40x40px of frame) erupts from the open book. The cross beam has concentric rings of gold, yellow, and white. Titanium plates on the covers reflect the blast. This is the "conversion" attack activation frame. Small spiraling scripture fragments (1px dark marks in circular paths) orbit the cross beam.

### Frame 15: Special - Conversion Blast 2 (Halo Formation)
- **Position in sheet:** 528,0 to 575,47
- **Description:** The cross beam contracts into a tight ring shape -- this is the halo forming. The ring is gold (#FFE066) with cracks of red (#CC3333) running through it (the halo is CROOKED and imperfect). The ring hovers above the target area (~30px diameter). Inside the ring, a faint downward arrow motif (suggesting the halo descending onto a zombie). The Bible is closing back, still glowing. Sparkle particles (4-5, white, 1x1px) orbit the forming halo.

### Frame 16: Special - Conversion Blast 3 (Hallelujah)
- **Position in sheet:** 576,0 to 623,47
- **Description:** The crooked halo is now complete -- a wobbly golden ring with visible cracks and imperfections (deliberately ugly, comic style). Below the halo, text "GLORIA!" in smaller size (fits 20x8px) in gold with red shadow. Small musical note symbols (2x3px, gold) float around the halo (2-3 notes), suggesting the converted zombie is now singing/screaming praise. The Bible is closed, returned to rest, with residual glow fading. This frame represents the converted zombie's status marker.

## Sprite Sheet Summary

| Frame | Name                 | Position     | Purpose                    |
|-------|----------------------|--------------|----------------------------|
| 0     | static               | 0-47         | Inventory / UI icon        |
| 1     | swing_windup         | 48-95        | Attack wind-up             |
| 2     | swing_mid            | 96-143       | Attack peak velocity       |
| 3     | swing_contact        | 144-191      | Hit moment                 |
| 4     | swing_followthrough  | 192-239      | Attack recovery            |
| 5     | holy_ray_1           | proj 0-31    | Projectile launch          |
| 6     | holy_ray_2           | proj 32-63   | Projectile mid-flight      |
| 7     | holy_ray_3           | proj 64-95   | Projectile flicker         |
| 8     | holy_ray_4           | proj 96-127  | Projectile pre-impact      |
| 9     | impact_gloria_1      | 240-287      | Onomatopeia appear         |
| 10    | impact_gloria_2      | 288-335      | Onomatopeia peak           |
| 11    | impact_gloria_3      | 336-383      | Onomatopeia fade           |
| 12    | idle_pulse_1         | 384-431      | Idle holy glow A           |
| 13    | idle_pulse_2         | 432-479      | Idle holy glow B           |
| 14    | convert_blast_1      | 480-527      | Conversion activation      |
| 15    | convert_halo_form    | 528-575      | Halo materializing         |
| 16    | convert_hallelujah   | 576-623      | Conversion complete marker |

## Phaser 3 Atlas Key
```
key: 'weapon_biblia_blindada'
frameWidth: 48
frameHeight: 48
```
```
key: 'projectile_holy_ray'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- This Bible must look INDESTRUCTIBLE -- the titanium plating should be absurdly thick and industrial
- The contrast between sacred (gold cross, holy light) and military (bolted armor, rivets, dents) is the visual joke
- Daciolo's Bible is a WEAPON OF MASS CONVERSION -- the holy light should feel dangerous, not peaceful
- The "GLORIA!" text must be SCREAMED -- shaky, uneven, with visible vibration marks
- The crooked halo on converted zombies is ESSENTIAL -- it must look wrong, broken, hastily blessed
- Every rivet, dent, and scratch tells a story of spiritual warfare
- The leather should look ancient and THICK -- like it could stop bullets (and it can)
- Pages that fly out during impact should have tiny illegible text scrawled on them
- The red ribbon bookmark is a subtle detail but grounds the Bible as a real book
- Robert Crumb style: nothing is straight, nothing is clean, everything has texture and weight
