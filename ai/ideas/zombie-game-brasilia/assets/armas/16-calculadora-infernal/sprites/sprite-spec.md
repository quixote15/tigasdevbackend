# Calculadora Infernal - Sprite Specification

## Overview
- **Weapon Type:** Ranged (Boss Weapon - Taxadd)
- **Sprite Dimensions:** 48x48px (BOSS SCALE -- monstrously oversized calculator)
- **Projectile Dimensions:** 32x32px (flying tax numbers/percentages)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 16 (1 static + 3 firing + 4 projectile + 3 impact + 2 idle + 3 special receipt trail)
- **Sprite Sheet Size:** 768x48px (weapon) / 128x32px (projectile numbers)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (24, 44) -- base grip point

## Color Palette

| Element                  | Hex Code  | Usage                                   |
|--------------------------|-----------|----------------------------------------|
| Calculator Grey (main)   | `#3A3A3A` | Calculator body, dark plastic           |
| Calculator Grey (light)  | `#505050` | Body highlights, edge bevels            |
| Calculator Grey (dark)   | `#222222` | Body shadows, underside                 |
| Display Green            | `#00FF66` | LCD display text (classic calculator)   |
| Display Green Dark       | `#00AA44` | Display text shadow/ghost digits        |
| Display Background       | `#1A2820` | LCD display background (dark green-grey)|
| Button Red               | `#CC2020` | Number buttons when firing (hot)        |
| Button Red Glow          | `#FF4040` | Button glow halos when active           |
| Button Grey Normal       | `#606060` | Number buttons resting state            |
| Button Grey Light        | `#808080` | Button highlights                       |
| Number White             | `#FFFFFF` | Projectile numbers, bright              |
| Number Red               | `#FF0000` | High-damage tax numbers (50%+)          |
| Number Orange            | `#FF8800` | Medium-damage numbers (25-49%)          |
| Number Yellow            | `#FFCC00` | Low-damage numbers (1-24%)              |
| Receipt Cream            | `#FFF8E0` | Receipt paper trail color               |
| Receipt Text Black       | `#1A1A1A` | Receipt printed text                    |
| Receipt Text Red         | `#CC0000` | Receipt TOTAL line / warning text       |
| Infernal Red             | `#880000` | Hellish glow from within calculator     |
| Infernal Orange          | `#FF4400` | Hellfire embers, infernal aura          |
| Fire Yellow              | `#FFD700` | Fire highlight tips                     |
| Smoke Grey               | `#444444` | Smoke wisps from overheated calculator  |
| Outline Black            | `#1A1A1A` | Thick 2px outlines (Crumb style)        |
| Shadow Dark              | `#0D0D0D` | Drop shadow, 50% opacity               |
| "%" Symbol Red           | `#FF0000` | Percentage signs on projectiles         |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 47,47
- **Description:** MONSTROUS oversized calculator, seen top-down isometric. Classic desk calculator shape but GROTESQUE -- fills 90% of the 48x48 frame. Dark grey plastic body with visible screw holes (2x2px dark circles at corners). A large LCD display at the top permanently shows "99,99%" in eerie green calculator digits (display green on dark green-grey background). Below the display, a grid of number buttons (4 rows x 4 columns, each button 4x4px with 1px gaps). Buttons are grey in resting state. An oversized red "=" button at the bottom-right (6x4px, button red). A faint infernal red glow seeps from between the button gaps and around the display edges (infernal red, 20% opacity). Cracks in the plastic body (2-3 hairline dark lines) reveal more red glow beneath -- something HELLISH lives inside this calculator. A small receipt paper strip curls from the top-left (receipt cream, 3px wide, 8px long, with tiny text marks). Thick 2px black outlines. Drop shadow (3px, 50% opacity).
- **Style Notes:** This calculator should look CURSED. The normal grey plastic exterior contrasts with the hellfire glow leaking through cracks. The "99,99%" display is permanent -- this is the maximum tax rate, always. The receipt paper suggests constant, relentless taxation. The buttons should look like they've been pressed a MILLION times -- worn smooth, slightly sunken.

### Frame 1: Firing Animation - Charge (Tax Calculation)
- **Position in sheet:** 48,0 to 95,47
- **Description:** Calculator buttons begin lighting up RED in sequence -- bottom row first, then second, third, top. Each lit button glows (button red with 2px button red glow halo). The display flickers -- "99,99%" changes digit by digit (the last digit cycles rapidly through 0-9, creating a slot-machine effect in 1 frame). The infernal glow between cracks intensifies (40% opacity). Small sparks (2, infernal orange, 1x1px) fly from the cracks. Smoke wisps (2, grey, 1x1px) rise from the top edge. The receipt paper begins feeding out (now 12px long, curling). The "=" button pulses larger (7x5px, anticipation).

### Frame 2: Firing Animation - Calculate! (Button Slam)
- **Position in sheet:** 96,0 to 143,47
- **Description:** ALL buttons simultaneously glow MAXIMUM RED -- the entire button grid is a sea of angry red light with halos merging. The display BLAZES -- "99,99%" is now BRIGHT green, oversized, nearly overflowing the display area. The "=" button is PRESSED (depressed 1px, darker at center). A shockwave of red light pulses outward from the display (ring, 30px diameter, infernal red, 40% opacity). The number projectile is being BORN -- a ghostly white number ("%" symbol) begins materializing above the display, half-formed. Fire particles (3, orange/yellow, 1x1px) erupt from the cracks. Receipt paper feeds faster (now 16px, the fresh portion shows "IMPOSTO:" text). The entire calculator VIBRATES (1px shift from center).

### Frame 3: Firing Animation - Launch! (Number Flies)
- **Position in sheet:** 144,0 to 191,47
- **Description:** The number projectile LAUNCHES from the display -- a large "%" symbol exits upward with a trail of smaller numbers (cascading "27,5%", "45%", "99,99%" fragments). The display briefly shows "ENVIADO" (sent) in green, then returns to "99,99%". Buttons still red but dimming (returning to grey from bottom up). A burst of infernal fire (8px starburst, orange/red) erupts from the display as the number exits. The receipt paper is at maximum extension (20px, curling at the end, the fresh text reads "TOTAL: R$ !!!"). Recoil: the calculator shifts 2px backward from the launch direction. Small ember particles (3, orange, 1x1px) trail the launched number. Smoke puff (4x4px, grey, 30% opacity) at the display.

### Frame 4: Projectile - Tax Number Launch (32x32px)
- **Position in sheet:** 0,0 to 31,31 (projectile sheet)
- **Description:** A flying tax number seen top-down. Central element: a BOLD percentage number, randomly selected from the damage tiers (e.g., "45%"). The number is rendered in sharp calculator-font style (segmented digits like an LCD). Color based on damage: yellow for low (1-24%), orange for medium (25-49%), RED for high (50%+). The "%" symbol is always RED regardless. Size: the number fills ~16x10px centered in frame. Behind the number: a trail of smaller receipt paper fragments (3-4 cream rectangles, 2x3px, scattered behind). A faint red glow (infernal red, 2px halo, 20% opacity) surrounds the number. Leading edge has a small white flash (2x2px, 40% opacity).

### Frame 5: Projectile - Tax Number Mid-flight (32x32px)
- **Position in sheet:** 32,0 to 63,31 (projectile sheet)
- **Description:** The number is at maximum intensity -- color brightens by 20%. The percentage symbol "%" rotates slightly (15deg tilt). Receipt paper fragments trail longer (now 5-6 pieces, spread over 18px behind). Tiny secondary numbers (1px marks, illegible) orbit the main number like tax code clauses. The red glow halo expands (3px). A faint smoke trail (1px grey, 10px long, 20% opacity) follows behind. The number appears to be ON FIRE (1-2 orange flame pixels at the trailing edge).

### Frame 6: Projectile - Tax Number Flickering (32x32px)
- **Position in sheet:** 64,0 to 95,31 (projectile sheet)
- **Description:** The number FLICKERS -- shifts 1px off-center (jerky Andre Guedes style). The LCD digits partially disappear (2-3 segments of the number missing, like a glitchy display). The percentage sign is intact but rotated further (30deg). Receipt fragments spread wider. Flame at trailing edge intensifies (2-3 orange pixels). The glow halo stutters (breaks into segments). Secondary orbiting numbers scatter. This frame creates visual instability suggesting the tax number is volatile.

### Frame 7: Projectile - Tax Number Arriving (32x32px)
- **Position in sheet:** 96,0 to 127,31 (projectile sheet)
- **Description:** Number CONCENTRATES for impact -- all segments restored, brighter than ever. The "%" symbol is HUGE (dominates 8x8px at center, deep red). The main number wraps around the percentage sign. No trail -- all fragments pulled forward. Flame engulfs the entire number (orange/yellow border around the digit). A red impact ring (20px diameter, 1px, infernal red) forms around the projectile. The number THROBS (scale oscillates 110% to 90%). This is a tax bill arriving at terminal velocity.

### Frame 8: Impact - "TAXADO!" Frame 1
- **Position in sheet:** 192,0 to 239,47
- **Description:** The tax number DETONATES on impact. An explosion of PAPERWORK -- dozens of receipt strips, tax forms, invoices burst outward (8-10 cream paper rectangles of varying sizes, 2x3px to 4x6px, with tiny illegible text marks). "TAXADO!" (taxed!) text appears in RED (#FF0000) bold letters with black (#1A1A1A) outline, hand-lettered comic book style. The percentage number persists briefly at the center, blazing (white hot, 100ms). Fire particles (6, orange/red) burst radially. A "R$" (Real symbol) currency sign (4x4px, green) appears next to the text. Red flash starburst (24px diameter) behind everything.

### Frame 9: Impact - "TAXADO!" Frame 2
- **Position in sheet:** 240,0 to 287,47
- **Description:** "TAXADO!" at MAXIMUM SIZE, letters in flames (small orange flame pixels on top of each letter). Paper fragments at maximum spread -- some are burning at edges (orange pixel on cream paper corners). The "R$" symbol multiplies (3 instances, orbiting the text). Additional text appears: the specific percentage that hit (e.g., "99,99%!") in smaller green calculator-font below the main text. Fire particles peak. A shower of tiny coins (3-4, gold circles, 2x2px) rains down. Red screen flash: 2px border at 30% opacity.

### Frame 10: Impact - "TAXADO!" Frame 3
- **Position in sheet:** 288,0 to 335,47
- **Description:** "TAXADO!" fading (70% scale, 50% opacity, red shifting darker). Paper fragments flutter to ground (now with visible "burn" damage -- dark edges on cream paper). Fire dissipates to embers (2-3 orange sparks). Coins hit the ground (no longer falling). "R$" symbols fade. A scorched receipt (8x4px, cream with dark burn marks) remains on the ground at impact center -- the "tax bill." The percentage text is gone. Smoke wisps (3, grey) drift upward. Transition frame.

### Frame 11: Idle Effect - Display Pulse 1
- **Position in sheet:** 336,0 to 383,47
- **Description:** Calculator at rest with ominous idle animation. The display "99,99%" pulses brighter (display green intensifies, digits slightly larger). The infernal glow between cracks brightens (30% opacity pulse). A single button (random position on grid) flickers red momentarily (200ms highlight). The receipt paper curls gently (paper tip moves 1px left). A tiny ember (1x1px, orange) drifts from a crack. Smoke wisp (single, grey, 1px) rises from the right side. The "=" button has a faint red pulse.

### Frame 12: Idle Effect - Display Pulse 2
- **Position in sheet:** 384,0 to 431,47
- **Description:** Display "99,99%" dims slightly (standard green, normal digit size). Infernal glow retreats (20% opacity). A different button flickers red. Receipt paper tip moves 1px right. The ember is on the opposite side. Smoke wisp from the left. Together Frames 11-12 create a menacing idle pulse -- the calculator is always CALCULATING, always hungry for taxes. The display never goes blank. The fire never goes out.

### Frame 13: Special - Receipt Trail 1 (Paper Storm Building)
- **Position in sheet:** 432,0 to 479,47
- **Description:** The calculator's receipt printer goes HAYWIRE. Receipt paper FLOODS from the top-left, now multiple strips (3 parallel streams, cream colored, each 3px wide). The paper curls and spirals. Visible text on the paper: "ICMS", "ISS", "IRPF", "PIS", "COFINS" (Brazilian tax acronyms, in tiny 1px marks). The display rapidly cycles numbers (digits blur). Buttons light up in random patterns (3-4 red at any time). Infernal glow peaks at 50% opacity. This triggers as a special area attack -- Taxadd drowns enemies in tax paperwork.

### Frame 14: Special - Receipt Trail 2 (Paper Vortex)
- **Position in sheet:** 480,0 to 527,47
- **Description:** Receipt paper now forms a VORTEX around the calculator -- strips spiral outward in a clockwise pattern, filling 70% of the frame. The paper strips have red "TOTAL" stamps visible on them. Some strips are ON FIRE (orange edge pixels). The display shows "CALCULANDO..." (calculating) in green, scrolling. All buttons are RED simultaneously, blazing. The infernal fire is now VISIBLE through the cracks (not just a glow -- actual tiny flame shapes, orange/yellow, licking upward from gaps). Numbers ("%" symbols in white) ride the paper vortex like debris in a tornado.

### Frame 15: Special - Receipt Trail 3 (Tax Tsunami)
- **Position in sheet:** 528,0 to 575,47
- **Description:** The paper vortex EXPLODES outward -- receipt strips fly to all frame edges. A WAVE of paper (cream, multi-layered, fills 90% of frame) pushes outward from center. The calculator sits at the center, all buttons ablaze, display overloaded (every segment lit, green blur). Fire erupts from the display ("99,99%" in FLAMES). Large "%" symbols (3, red, various sizes 6-10px) ride the paper wave. Tax form fragments (larger pieces, 4x6px, with visible grid lines like a spreadsheet) mix with the receipts. A "R$" symbol in flames at the wave crest. This is the ULTIMATE tax attack -- death by bureaucracy.

## Sprite Sheet Summary

| Frame | Name                | Position      | Purpose                    |
|-------|---------------------|---------------|----------------------------|
| 0     | static              | 0-47          | Inventory / UI icon        |
| 1     | fire_charge         | 48-95         | Buttons lighting up        |
| 2     | fire_calculate      | 96-143        | Button slam, number forms  |
| 3     | fire_launch         | 144-191       | Number projectile launches |
| 4     | taxnum_1            | proj 0-31     | Projectile launch          |
| 5     | taxnum_2            | proj 32-63    | Projectile mid-flight      |
| 6     | taxnum_3            | proj 64-95    | Projectile flicker         |
| 7     | taxnum_4            | proj 96-127   | Projectile arriving        |
| 8     | impact_taxado_1     | 192-239       | Onomatopeia appear         |
| 9     | impact_taxado_2     | 240-287       | Onomatopeia peak           |
| 10    | impact_taxado_3     | 288-335       | Onomatopeia fade           |
| 11    | idle_pulse_1        | 336-383       | Idle display bright        |
| 12    | idle_pulse_2        | 384-431       | Idle display dim           |
| 13    | special_receipt_1   | 432-479       | Receipt storm building     |
| 14    | special_receipt_2   | 480-527       | Paper vortex               |
| 15    | special_receipt_3   | 528-575       | Tax tsunami                |

## Phaser 3 Atlas Key
```
key: 'weapon_calculadora_infernal'
frameWidth: 48
frameHeight: 48
```
```
key: 'projectile_tax_number'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- The calculator must look like a CURSED office supply -- mundane design hiding infernal power
- The "99,99%" display is the visual anchor -- always present, always menacing, ALWAYS at maximum tax
- The infernal glow through the cracks is ESSENTIAL -- hell itself powers this calculator
- Receipt paper is the recurring motif -- it NEVER stops printing, endlessly generating tax obligations
- Number projectiles use LCD/calculator font (segmented display style) -- sharp, digital, mechanical
- Color-coded damage (yellow/orange/red) gives visual feedback on projectile power
- The Brazilian tax acronyms on receipts (ICMS, ISS, IRPF, PIS, COFINS) are crucial comedy details
- "R$" (Brazilian Real) currency symbols should appear frequently in effects
- Robert Crumb style: the bureaucratic horror should feel OPPRESSIVE and inescapable
- The buttons lighting up red is like the calculator WARMING UP -- building infernal tax energy
- Every impact should feel like receiving a tax bill from hell
- The special attack (receipt tsunami) is death by paperwork -- grotesquely mundane apocalypse
