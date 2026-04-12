# Frasco de Rivotril Turbo - Sprite Specification

## Overview
- **Weapon Type:** Melee Club + AoE Effect (Boss Weapon - Ciro)
- **Sprite Dimensions:** 48x48px (BOSS SCALE -- comically oversized pill bottle)
- **Projectile Dimensions:** 32x32px (sedation cloud / flying pills)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 17 (1 static + 4 swing + 4 projectile + 3 impact + 2 idle + 3 panic special)
- **Sprite Sheet Size:** 816x48px (weapon) / 128x32px (projectile cloud)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (24, 42) -- bottle bottom grip

## Color Palette

| Element                  | Hex Code  | Usage                                   |
|--------------------------|-----------|----------------------------------------|
| Bottle Orange (main)     | `#E87830` | Prescription bottle body               |
| Bottle Orange (light)    | `#F09848` | Bottle highlights, curvature           |
| Bottle Orange (dark)     | `#C05818` | Bottle shadows, depth                  |
| Cap White                | `#F0F0F0` | Child-proof cap                        |
| Cap Shadow               | `#C8C8C8` | Cap depth, threading                   |
| Label White              | `#FFFFFF` | Prescription label background          |
| Label Text Blue          | `#2040A0` | "RIVOTRIL" text on label               |
| Label Text Red           | `#CC2020` | "TURBO" text, warning symbols          |
| Pill Blue (clonazepam)   | `#4488CC` | Individual pills visible through bottle |
| Pill Blue Light          | `#66AAEE` | Pill highlights                        |
| Sedation Purple          | `#8844AA` | Sedation cloud/gas effect              |
| Sedation Purple Light    | `#AA66CC` | Cloud highlights, inner glow           |
| Sedation Purple Dark     | `#662288` | Cloud depth, darker wisps              |
| Sleep Z's Yellow         | `#FFE040` | Floating "Z z z" sleep symbols         |
| Panic Red                | `#FF2020` | Ciro panic state, veins, stress        |
| Panic Red Dark           | `#CC0000` | Panic shadow, stress lines             |
| Sweat Drop Blue          | `#88CCFF` | Panic sweat drops                      |
| Star Yellow              | `#FFD700` | Impact stars (seeing stars effect)     |
| Outline Black            | `#1A1A1A` | Thick 2px outlines (Crumb style)       |
| Shadow Dark              | `#0D0D0D` | Drop shadow, 50% opacity              |
| Liquid Amber             | `#FFAA30` | Liquid sloshing inside bottle          |
| Cross Red                | `#FF0000` | Medical cross symbol on label          |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 47,47
- **Description:** GIANT prescription medication bottle, seen top-down isometric. Classic orange-brown translucent pharmacy bottle shape, cylindrical, fills 85% of the 48x48 frame. ABSURDLY oversized -- this is a bottle big enough to bludgeon someone with. White child-proof cap on top (8px diameter circle). A white prescription label wraps around the front with "RIVOTRIL" in blue pharmacy text and "TURBO" stamped below in aggressive red. A red medical cross symbol on the label. Through the translucent orange plastic, you can see dozens of small blue pills rattling inside (5-6 visible as blue dots behind the orange). The bottle is slightly dented on one side (it's been used as a weapon before). Thick 2px black outlines. Drop shadow (3px, 50% opacity). A single pill has escaped and sits next to the bottle base (2x1px blue pill).
- **Style Notes:** The bottle must look like actual medication but WEAPONIZED. The dents show combat use. The pills inside should rattle visually -- some near the top, some settled at bottom. The "TURBO" addition to the label is hand-scrawled, not printed. There's a desperate, anxious energy to this weapon -- it IS the medication Ciro needs but he's swinging it instead.

### Frame 1: Swing Animation - Wind-up (Desperate Grip)
- **Position in sheet:** 48,0 to 95,47
- **Description:** Bottle raised overhead, tilted back ~45deg. The liquid inside sloshes -- amber fluid shifts to the back of the bottle (3-4 amber pixels near the cap end). Pills scatter inside (blue dots rearrange from Frame 0 positions). The cap shakes loose slightly (1px gap between cap and bottle body). Two small sweat drops (2x3px, light blue) appear near the grip point -- Ciro is STRESSED holding his medication as a weapon. A single pill flies out from the loose cap (1x1px blue, trailing upward). Motion anticipation line (1px, orange).

### Frame 2: Swing Animation - Mid-swing (Medicated Fury)
- **Position in sheet:** 96,0 to 143,47
- **Description:** Bottle at peak horizontal velocity, sweeping in an arc. The liquid inside sloshes VIOLENTLY to one side (amber pixels compressed against the leading wall). Pills fly around chaotically inside (blue dots scattered wildly). 3-4 pills escape through the loose cap, trailing behind the swing (blue 1x1px particles). Two thick motion lines (orange, 2px). The label text "RIVOTRIL" blurs with speed. A faint purple sedation wisp (2px, 30% opacity) leaks from the escaping pills. The bottle stretches slightly in swing direction (speed distortion, 2px).

### Frame 3: Swing Animation - Contact (DOSE LETAL)
- **Position in sheet:** 144,0 to 191,47
- **Description:** Bottle SMASHES into target. The bottle deforms on impact -- squashed at the contact end (bulging slightly at the sides, 40x36px distorted shape). PILLS EXPLODE outward from the cap which pops completely off -- 8-10 blue pills burst in all directions (1-2px each, radially distributed). A CLOUD of purple sedation gas erupts at the impact point (15px diameter, sedation purple, 50% opacity). The amber liquid splashes (4-5 amber droplets, 1x1px, flying from impact). The label cracks (1px dark line across the text). Stars (3, yellow, 3x3px, classic cartoon stars) orbit the impact point. A white starburst (8x8px) at the contact center.

### Frame 4: Swing Animation - Follow-through (Pill Scatter)
- **Position in sheet:** 192,0 to 239,47
- **Description:** Bottle continuing past impact, rebounding. The cap is gone (lost in the explosion). Bottle mouth is open -- more pills tumble out (3-4 blue pills falling from the opening). The bottle is less full now (fewer blue dots visible inside). Liquid drips from the opening (2 amber drops, 1x1px). The purple sedation cloud at the hit point lingers and expands (20px diameter). A single motion line trails. The "TURBO" text on the label is partially obscured by a crack. Sweat drops near the grip intensify (Ciro is anxious about wasting his meds).

### Frame 5: Projectile - Sedation Cloud Launch (32x32px)
- **Position in sheet:** 0,0 to 31,31 (projectile sheet)
- **Description:** A puff of purple sedation gas, seen top-down. Central dense cloud (10px diameter, sedation purple, 70% opacity) surrounded by wispy tendrils (2-3 extensions, 4px each, lighter purple, 40% opacity). 3 blue pills visible tumbling within the cloud (2x1px each, scattered at different angles). A tiny "Zz" (sleep symbol, yellow, 3x4px) floats at the top-right of the cloud. The cloud has an organic, billowing, slightly toxic look. Green-purple tint variations within (not uniform -- patchy, chemical).

### Frame 6: Projectile - Sedation Cloud Expanding (32x32px)
- **Position in sheet:** 32,0 to 63,31 (projectile sheet)
- **Description:** Cloud expanding -- central mass now 14px diameter, tendrils reaching 6px outward. The cloud is more diffuse, lighter at edges. Pills within have dissolved partially (smaller, 1x1px, fading). "Zzz" sleep symbols larger (5x5px) and drifting upward. Tiny spiral (hypnotic swirl, 2px, darker purple) appears at cloud center suggesting sedative effect. The whole cloud drifts slowly, ominously.

### Frame 7: Projectile - Sedation Cloud Pulsing (32x32px)
- **Position in sheet:** 64,0 to 95,31 (projectile sheet)
- **Description:** Cloud pulses -- contracts momentarily (10px diameter) then bloats (16px). Jerky animation style -- the cloud shape shifts dramatically between frames. Color shifts to darker purple at center (concentration pulse). "Zzz" symbols jitter (shifted 1px from Frame 6 positions). Pills fully dissolved -- just faint blue tint remains in the cloud. A small skull-and-crossbones motif (3x3px, very faint, 20% opacity) appears briefly in the cloud center (it's THAT strong).

### Frame 8: Projectile - Sedation Cloud Arriving (32x32px)
- **Position in sheet:** 96,0 to 127,31 (projectile sheet)
- **Description:** Cloud concentrating for impact -- edges sharpen, density increases. Central mass 12px, darker purple, nearly opaque (80%). Tendrils retract inward, pulling energy to center. "Zzz" symbols are huge (7x6px) and bold -- maximum sleepiness incoming. No dissolved pills visible -- the sedation is pure chemical now. A faint purple ring (18px diameter, 1px, 30% opacity) appears around the cloud, foreshadowing the sedation AoE.

### Frame 9: Impact - "NOCAUTE!" Frame 1
- **Position in sheet:** 240,0 to 287,47
- **Description:** Sedation cloud DETONATES into a wide area effect. Purple gas expands to fill 80% of frame. "NOCAUTE!" (knockout) text appears in purple (#8844AA) with yellow (#FFE040) outline, hand-lettered, wobbly, like the letters themselves are sedated. Floating "Z z Z z Z" symbols (yellow) scatter across the frame in various sizes (2px to 6px). Cartoon stars (3-4, yellow, 3x3px) orbit the impact center. Blue pill fragments (4-5, 1px) rain down. The purple gas has a hypnotic swirl pattern (concentric circles at 20% opacity visible in the cloud).

### Frame 10: Impact - "NOCAUTE!" Frame 2
- **Position in sheet:** 288,0 to 335,47
- **Description:** "NOCAUTE!" text at maximum size, letters DROOPING (the word itself is falling asleep -- letters tilt, sag, droop at varying angles). The "Z" symbols grow even larger (8px) and multiply (6-7 floating). Purple gas at maximum spread, nearly filling the entire frame. The swirl pattern intensifies -- the viewer should feel dizzy. A tiny cartoon clock (4x4px) appears, suggesting the sedation timer. Stars orbit slower (they're getting sedated too). Screen tint: purple overlay at 15% opacity.

### Frame 11: Impact - "NOCAUTE!" Frame 3
- **Position in sheet:** 336,0 to 383,47
- **Description:** "NOCAUTE!" fading -- text at 70% scale, 40% opacity, letters now nearly horizontal (fallen asleep). Purple gas begins dissipating from edges inward. "Z" symbols float upward and fade. The swirl collapses. A purple residue circle remains (18px diameter, 20% opacity) -- the sedation zone marker. Stars gone. A few last blue pill fragments on the ground (static, tiny). Transition frame. The clock ticks (hand moved slightly from Frame 10).

### Frame 12: Idle Effect - Liquid Slosh 1
- **Position in sheet:** 384,0 to 431,47
- **Description:** Bottle at rest with subtle idle animation. The amber liquid inside sloshes gently left (2px shift of amber pixel cluster). Pills drift to the left inside (blue dots shift 1px). The loose cap wobbles slightly (1px leftward tilt). A single tiny "z" (2px, yellow, 30% opacity) drifts upward from the cap -- the medication is so strong it radiates sleepiness even sealed. The label is intact but worn. One stray pill sits on the ground beside the bottle (callbacks to Frame 0).

### Frame 13: Idle Effect - Liquid Slosh 2
- **Position in sheet:** 432,0 to 479,47
- **Description:** Liquid sloshes right (mirror of Frame 12). Pills drift right. Cap wobbles right. The "z" symbol is on the opposite side, slightly higher (drifting upward and fading). The stray pill on the ground has shifted 1px (it rolled). Together Frames 12-13 create a gentle liquid sloshing idle loop. The bottle feels alive with contained chemical energy -- anxious, vibrating with pharmaceutical potential.

### Frame 14: Special - Panic State 1 (Ciro Needs His Meds)
- **Position in sheet:** 480,0 to 527,47
- **Description:** The bottle starts SHAKING VIOLENTLY -- rattling animation. The entire bottle vibrates 2px left of center. The liquid inside is agitated -- amber pixels swirl chaotically. Pills bounce off the walls inside (blue dots at extreme positions, hitting edges). RED stress lines (panic red, 3 lines, 1px each) radiate from the bottle. The cap rattles -- 2px gap now, about to fly off. Sweat drops (3, light blue, 2x3px) appear around the bottle. The label text turns RED ("RIVOTRIL" shifts from blue to red, warning of depleted patience). A small exclamation mark "!" (red, 4x6px) appears above the bottle. This triggers when Ciro hasn't attacked for 10 seconds.

### Frame 15: Special - Panic State 2 (WITHDRAWAL!)
- **Position in sheet:** 528,0 to 575,47
- **Description:** Bottle EXPLODING with panic energy -- shifted 2px RIGHT of center (violent alternation with Frame 14). Liquid BOILS inside (amber pixels now have red tint, bubbling at the top). Pills are in complete chaos (blue dots at random extreme positions). The cap has POPPED OFF -- floating 4px above the bottle, tilted. Purple sedation gas LEAKS from the open top (wisps rising, 3 purple tendrils). Sweat drops are HUGE (4x5px) and multiplied (5 drops). Red stress lines doubled (6 lines). "!!" double exclamation above. The label is cracking further. Small pieces of orange plastic chip off the bottle (2-3 orange fragments, 1x1px, near the dented area).

### Frame 16: Special - Panic State 3 (Self-Dose)
- **Position in sheet:** 576,0 to 623,47
- **Description:** The bottle TIPS toward Ciro (angled 60deg toward the player). Pills pour out of the open top toward the player character (stream of 5-6 blue pills arcing downward). Purple sedation gas billows in the pour direction. The liquid sloshes out (amber drops cascade). A halo of yellow stars (4, 3x3px) circles above the bottle -- Ciro is self-medicating via weapon. Text "-HP" appears in red (damage to self). The label reads "DOSE EMERGENCIAL" (barely legible, red text). The sweat drops are replaced by relief sweat (different positions, smaller, calmer). The bottle is now half-empty (fewer pills and less liquid visible inside).

## Sprite Sheet Summary

| Frame | Name                | Position      | Purpose                    |
|-------|---------------------|---------------|----------------------------|
| 0     | static              | 0-47          | Inventory / UI icon        |
| 1     | swing_windup        | 48-95         | Attack wind-up             |
| 2     | swing_mid           | 96-143        | Attack peak velocity       |
| 3     | swing_contact       | 144-191       | Hit moment                 |
| 4     | swing_followthrough | 192-239       | Attack recovery            |
| 5     | sedate_cloud_1      | proj 0-31     | Sedation cloud launch      |
| 6     | sedate_cloud_2      | proj 32-63    | Cloud expanding            |
| 7     | sedate_cloud_3      | proj 64-95    | Cloud pulsing              |
| 8     | sedate_cloud_4      | proj 96-127   | Cloud arriving             |
| 9     | impact_nocaute_1    | 240-287       | Onomatopeia appear         |
| 10    | impact_nocaute_2    | 288-335       | Onomatopeia peak           |
| 11    | impact_nocaute_3    | 336-383       | Onomatopeia fade           |
| 12    | idle_slosh_1        | 384-431       | Idle liquid left           |
| 13    | idle_slosh_2        | 432-479       | Idle liquid right          |
| 14    | panic_1             | 480-527       | Panic shaking              |
| 15    | panic_2             | 528-575       | Panic exploding            |
| 16    | panic_selfdose      | 576-623       | Self-damage medication     |

## Phaser 3 Atlas Key
```
key: 'weapon_frasco_rivotril'
frameWidth: 48
frameHeight: 48
```
```
key: 'projectile_sedate_cloud'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- The bottle must look like REAL pharmacy medication -- orange translucent plastic, white cap, prescription label
- But it's ABSURDLY large, dented from combat use, and clearly being misused as a weapon
- The liquid sloshing inside is ESSENTIAL -- it sells the weight and chaos of swinging a bottle
- Pills flying everywhere on impact should feel wasteful and desperate
- The purple sedation cloud is the signature visual -- toxic, hypnotic, dangerous
- "Z z Z" sleep symbols are the recurring particle motif -- everything gets SLEEPY
- The PANIC mechanic is the dark comedy core: Ciro NEEDS this medication but he's using it to fight
- Panic frames should feel genuinely ANXIOUS -- shaking, sweating, vibrating
- The self-dose frame (Frame 16) is both sad and funny -- he's literally drinking from his weapon
- Robert Crumb style: the pharmaceutical anxiety should be PALPABLE in every pixel
- The "TURBO" on the label is scrawled in marker, not printed -- suggesting Ciro modified his own prescription
- Every dent in the bottle is a zombie he already hit with his anxiety medication
