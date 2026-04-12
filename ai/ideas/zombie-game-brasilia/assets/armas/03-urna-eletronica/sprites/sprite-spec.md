# Urna Eletronica - Sprite Specification

## Overview
- **Weapon Type:** Ranged (shoots vote projectiles)
- **Sprite Dimensions:** 48x48px (weapon body), 32x32px (vote projectiles)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 15 (1 static + 4 fire + 4 projectile flight + 3 impact + 1 muzzle flash + 2 idle)
- **Sprite Sheet Size:** 720x48px (weapon), 128x32px (projectile sheet)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (24, 40) -- grip point

## Color Palette

| Element                 | Hex Code  | Usage                            |
|-------------------------|-----------|----------------------------------|
| Urna Body (dark gray)   | `#2C2C2C` | Main casing body                 |
| Urna Body (mid gray)    | `#4A4A4A` | Casing panel lines               |
| Urna Body (light gray)  | `#6B6B6B` | Casing highlights / edges        |
| Screen (base)           | `#0A3D0A` | Old CRT screen background        |
| Screen (glow)           | `#00FF41` | Screen text / glitch glow        |
| Screen (crack)          | `#1A1A1A` | Cracked screen lines             |
| Wire Red               | `#CC0000` | Exposed wire A                   |
| Wire Yellow             | `#CCCC00` | Exposed wire B                   |
| Wire Blue               | `#0044CC` | Exposed wire C                   |
| Spark Yellow            | `#FFD700` | Electrical spark effects         |
| Spark White             | `#FFFFFF` | Peak spark brightness            |
| Keypad Beige            | `#D2B48C` | Number pad buttons               |
| Keypad Numbers          | `#1A1A1A` | Button text                      |
| Outline Black           | `#1A1A1A` | Thick 2px outlines               |
| Shadow Dark             | `#0D0D0D` | Drop shadow                      |
| Vote Paper (white)      | `#F5F5DC` | Ballot paper projectile          |
| Vote Paper (print)      | `#1A1A1A` | Printed marks on ballot          |
| Vote Paper (stamp)      | `#CC0000` | "CONFIRMADO" stamp               |
| Green Flag              | `#009B3A` | Brazil flag green element        |
| Yellow Flag             | `#FEDF00` | Brazil flag yellow element       |
| Impact Flash Blue       | `#0066FF` | "VOTO!" onomatopeia              |
| Impact Flash White      | `#FFFFFF` | Impact flash                     |

## Frame-by-Frame Descriptions (Weapon Body - 48x48)

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 47,47
- **Description:** Old Brazilian voting machine seen from top-down isometric view. DISPROPORTIONALLY LARGE -- a hulking piece of electoral technology. Dark gray rectangular body with a small cracked green CRT screen on the upper portion. A numeric keypad (3x4 grid of beige buttons) on the lower portion. 2-3 exposed wires (red, yellow, blue) dangling from the right side where the casing is cracked/broken open. A thick power cable trails from the bottom. Small "TSE" text scratched onto the casing. The screen shows garbled green text/static (2-3 pixels of green glow). Thick black outlines, heavy shadows. This machine has seen MANY elections and none of them clean.
- **Style Notes:** The urna should look like a Frankenstein of Brazilian democracy. Battered, held together with tape and prayers. The cracked screen flickers. Exposed wires spark occasionally. The numeric keypad buttons are worn smooth from millions of votes. A small Brazilian flag sticker peels off one corner.

### Frame 1: Fire Animation - Charge Up
- **Position in sheet:** 48,0 to 95,47
- **Description:** The urna begins charging. The cracked screen brightens intensely (screen glow color expands 2px beyond screen bounds). The exposed wires begin to glow at their tips -- small spark dots (1x1px yellow). The keypad buttons depress slightly (1px downward shift). A faint hum ring appears around the machine (1px circle, 20% opacity green). The casing vibrates (entire sprite offset 1px randomly from center -- jitter effect described, drawn as slight positional shift).

### Frame 2: Fire Animation - Power Surge
- **Position in sheet:** 96,0 to 143,47
- **Description:** Full power surge. The screen is now BLAZING green, with scan lines visible (alternating 1px bright and dark green horizontal lines). Electrical arcs jump between the exposed wires (jagged 1px yellow/white lines connecting wire tips). The keypad shows "00" displayed on the buttons (referencing null votes). The machine's casing shows stress cracks glowing with green light from inside. A ballot paper begins to emerge from a slot on the left side of the machine.

### Frame 3: Fire Animation - Vote Launch
- **Position in sheet:** 144,0 to 191,47
- **Description:** The ballot paper SHOOTS out of the urna at high velocity. The slot on the left side glows white from the ejection energy. A muzzle-flash style burst (6x6px starburst, white center fading to blue) appears at the ejection slot. The screen displays "CONFIRMADO" in large green pixels. Small electrical sparks (3-4, 1x1px yellow) scatter from the ejection point. The machine recoils slightly to the right (2px offset from rest position). The ballot paper (partially visible at frame edge) has begun its flight trajectory.

### Frame 4: Fire Animation - Recoil Recovery
- **Position in sheet:** 192,0 to 239,47
- **Description:** The urna recovering from recoil. Shifting back 1px toward center (still 1px offset). Screen dimming back toward normal (but still shows "CONFIRMADO" in fading green). Sparks dissipating. Exposed wires still glowing but fading. A small wisp of smoke (2x3px gray, 50% opacity) rises from the ejection slot. The keypad returns to normal height.

### Frame 5: Muzzle Flash
- **Position in sheet:** 240,0 to 287,47
- **Description:** Standalone muzzle flash effect for layering. Large starburst at the ejection slot position (12x12px). White center (#FFFFFF) transitioning through bright blue (#0066FF) to green (#00FF41) at edges. 4-6 radial spike lines. Small ballot paper confetti (2x2px) in the burst. An electrical arc effect (jagged line) extends from the starburst. This frame overlays on the weapon during Frame 3 for extra punch.

### Frame 6: Impact - "VOTO!" Frame 1
- **Position in sheet:** 288,0 to 335,47
- **Description:** Impact effect when vote projectile hits target. "VOTO!" text appears in bold, chunky, hand-lettered style. Blue (#0066FF) letters with white (#FFFFFF) outline. A circular burst of tiny ballot papers (4-6, 2x2px each) radiates outward. Small Brazil flag colors (green and yellow dots, 1x1px) scatter in the burst. A confirmation "beep" visual -- concentric circles (2 rings, 1px, green) emanating from center.

### Frame 7: Impact - "VOTO!" Frame 2
- **Position in sheet:** 336,0 to 383,47
- **Description:** "VOTO!" at peak intensity and maximum size. Letters are 120% scale of Frame 6. The ballot paper confetti has spread further. The concentric "beep" rings are larger and more visible. A small "CONFIRMADO" stamp mark (red, like a rubber stamp impression) appears below the main text. Maximum blue flash intensity. Impact starburst lines extend to frame edges.

### Frame 8: Impact - "VOTO!" Frame 3
- **Position in sheet:** 384,0 to 431,47
- **Description:** "VOTO!" fading. Text at 60% opacity, shrinking to 80% scale. Ballot confetti at frame edges, nearly gone. Concentric rings fading and expanding past frame bounds. "CONFIRMADO" stamp fading. Colors desaturating toward gray. The democratic process is complete.

### Frame 9-12: RESERVED for projectile (see Projectile Sheet below)

### Frame 13: Idle Effect - Screen Flicker 1
- **Position in sheet:** 624,0 to 671,47 (adjusted position accounting for all frames)
- **Description:** The urna at rest with screen showing static/glitch pattern A. Screen displays garbled green characters (random pixels in screen glow color). One exposed wire sparks intermittently (1px yellow dot at wire tip). The small peeling flag sticker is visible. A very faint hum glow (1px green outline around screen at 10% opacity). The machine looks dormant but not dead.

### Frame 14: Idle Effect - Screen Flicker 2
- **Description:** Screen shows different static pattern B (different random pixel arrangement). The sparking wire tip is dark (spark has moved to a different wire). Hum glow slightly brighter (15% opacity). Screen briefly shows a ghost image of a number (like "13" or "45" -- any party number, flickering in and out). The machine remembers every vote.

## Projectile Sprite Sheet (Separate - 32x32px)

### Projectile Frame 0: Vote - Flat
- **Sheet:** projectile_vote.png, position 0,0 to 31,31
- **Description:** A ballot paper (cedula de voto) seen from above, flat. Rectangular white/cream paper (#F5F5DC) with printed black lines (candidate number boxes). A large red "CONFIRMADO" stamp diagonally across the paper. Small official-looking printed text (illegible at this scale -- just 1px dark marks). The paper is crisp and freshly ejected. Thin black outline. Paper fills ~70% of the 32x32 frame. Small corner fold on one edge.

### Projectile Frame 1: Vote - Spinning A
- **Sheet:** position 32,0 to 63,31
- **Description:** The ballot paper in flight, rotated 90deg from Frame 0. Shows the paper from a perspective angle -- appears narrower (foreshortening). The "CONFIRMADO" stamp is partially visible. Motion blur trail (2 faint copies behind at 40% and 20% opacity). A small green glow trail (1px, screen glow color) follows the paper like a tracer.

### Projectile Frame 2: Vote - Spinning B
- **Sheet:** position 64,0 to 95,31
- **Description:** Paper at 180deg rotation -- showing the back side. Back of ballot is mostly blank cream with a small official watermark (simplified to a few gray pixels suggesting the TSE seal). Motion blur more pronounced (paper is at peak flight speed). Green tracer glow brighter. The paper flutters slightly (edges are wavy, not straight).

### Projectile Frame 3: Vote - Spinning C
- **Sheet:** position 96,0 to 127,31
- **Description:** Paper at 270deg rotation -- another foreshortened perspective view, mirroring Frame 1. "CONFIRMADO" stamp visible from the other angle. Motion blur continues. Green tracer. Small electrical spark (1x1px) at the paper's leading edge -- the paper is charged with electoral energy. The paper crackles with democracy.

## Sprite Sheet Summary (Weapon)

| Frame | Name                | Position       | Purpose                |
|-------|---------------------|----------------|------------------------|
| 0     | static              | 0-47           | Inventory / UI icon    |
| 1     | fire_charge         | 48-95          | Charge-up              |
| 2     | fire_surge          | 96-143         | Power surge            |
| 3     | fire_launch         | 144-191        | Vote ejection          |
| 4     | fire_recoil         | 192-239        | Recoil recovery        |
| 5     | muzzle_flash        | 240-287        | Overlay flash effect   |
| 6     | impact_voto_1       | 288-335        | "VOTO!" appear         |
| 7     | impact_voto_2       | 336-383        | "VOTO!" peak           |
| 8     | impact_voto_3       | 384-431        | "VOTO!" fade           |
| 9     | idle_flicker_1      | 432-479        | Idle screen A          |
| 10    | idle_flicker_2      | 480-527        | Idle screen B          |

## Projectile Sheet Summary

| Frame | Name            | Position  | Purpose              |
|-------|-----------------|-----------|----------------------|
| 0     | vote_flat       | 0-31      | Initial / static     |
| 1     | vote_spin_a     | 32-63     | Flight spin phase 1  |
| 2     | vote_spin_b     | 64-95     | Flight spin phase 2  |
| 3     | vote_spin_c     | 96-127    | Flight spin phase 3  |

## Phaser 3 Atlas Keys
```
// Weapon body
key: 'weapon_urna'
frameWidth: 48
frameHeight: 48

// Vote projectile
key: 'projectile_vote'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- The urna must look like a piece of technology that should have been retired 20 years ago
- The cracked screen is ESSENTIAL -- green CRT glow leaking through cracks
- Exposed wires give it a "jury-rigged weapon" feel, not a clean device
- The numeric keypad buttons should be visibly worn (lighter color at center from use)
- "CONFIRMADO" on the screen is the visual equivalent of a gunshot -- make it bold
- The ballot paper projectiles should look bureaucratic and official, yet absurd as ammunition
- Brazil flag elements (green/yellow accents) add national identity without being heavy-handed
- The muzzle flash should combine electrical (sparks, arcs) with bureaucratic (paper confetti)
- Robert Crumb thick lines on everything -- this is ugly technology
- The machine should feel like it has a malevolent consciousness -- it watches, it remembers
