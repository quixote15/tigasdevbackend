# Bigode da Justica - Sprite Specification

## Overview
- **Weapon Type:** Thrown Boomerang (Boss Weapon - Eneas)
- **Sprite Dimensions:** 48x48px (BOSS SCALE -- absurdly huge detachable mustache)
- **Projectile Dimensions:** 32x32px (spinning mustache boomerang)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 16 (1 static + 3 throw + 4 projectile flight + 3 impact + 2 idle + 3 special return)
- **Sprite Sheet Size:** 768x48px (weapon) / 128x32px (projectile)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Center (24, 24) -- mustache center point (attaches to face)

## Color Palette

| Element                  | Hex Code  | Usage                                   |
|--------------------------|-----------|----------------------------------------|
| Mustache Black (main)    | `#1A1A1A` | Primary mustache hair color             |
| Mustache Black (light)   | `#2D2D2D` | Hair highlight strands, texture         |
| Mustache Black (dark)    | `#0A0A0A` | Deepest shadow within hair mass         |
| Mustache Grey            | `#404040` | Distinguished grey streaks              |
| Skin Tone (Eneas)        | `#C48A5A` | Skin visible at attachment base         |
| Skin Tone Dark           | `#A06830` | Skin shadow at detachment point         |
| Upper Lip Pink           | `#B06060` | Upper lip visible when mustache detaches|
| Justice Gold             | `#FFD700` | Justice aura, impact sparkle            |
| Justice Gold Dark        | `#B8960F` | Justice aura shadow/depth               |
| Patriotic Green          | `#009B3A` | Brazilian flag green accents            |
| Patriotic Yellow         | `#FEDF00` | Brazilian flag yellow accents           |
| Patriotic Blue           | `#002776` | Brazilian flag blue accents             |
| Blood Red                | `#8B0000` | Blood on mustache edges (from cutting)  |
| Blood Red Bright         | `#CC0000` | Fresh blood splatter                    |
| Wind White               | `#FFFFFF` | Motion trails, wind effects             |
| Wind Light Blue          | `#C0E0FF` | Secondary wind/air current trails       |
| Starburst Yellow         | `#FFE040` | Impact starburst                        |
| Rage Vein Red            | `#FF3030` | Rage veins on mustache in combat        |
| Outline Black            | `#0D0D0D` | Thick 2px outlines (Crumb style)        |
| Shadow Dark              | `#0D0D0D` | Drop shadow, 50% opacity               |
| Hair Sheen               | `#505060` | Subtle blue-grey sheen on groomed hair  |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon (Mustache Attached to Face)
- **Position in sheet:** 0,0 to 47,47
- **Description:** Eneas' ICONIC mustache, seen from top-down isometric, still attached to a sliver of his face. The mustache is ENORMOUS -- a thick, luxurious, perfectly maintained handlebar/walrus style mustache that fills 85% of the 48x48 frame. The hair is jet black with subtle grey dignified streaks (2-3 grey pixel lines). The mustache is THICK -- at its densest point, the hair mass is 12px tall. Each side sweeps outward and slightly upward in a distinguished curl at the tips. Individual hair strands are suggested by 1px lines in slightly lighter black at the edges. At the center base, a strip of skin tone (8px wide) represents the upper lip area where it attaches to Eneas' face. The mustache has visible WEIGHT and DENSITY -- it's a weapon even before it detaches. A faint golden justice aura (1px, justice gold, 20% opacity) outlines the entire mustache. Thick 2px outlines. Drop shadow (3px, 50% opacity).
- **Style Notes:** This mustache must be IMMEDIATELY recognizable as Eneas' iconic facial hair. It's thick, black, distinguished, and ABSURDLY large. The hair texture should be lovingly detailed -- individual strands, careful grooming lines, the curl at the tips. It must look both dignified and DANGEROUS. Think of it as a hairy boomerang waiting to happen. The golden justice aura hints at its supernatural nature.

### Frame 1: Throw Animation - Detachment (Rip!)
- **Position in sheet:** 48,0 to 95,47
- **Description:** The mustache DETACHES from Eneas' face in a grotesque, violent motion. The center base area shows TEARING -- the skin tone strip at the center splits, revealing pink upper lip beneath (#B06060). Small skin-colored particles (2-3, 1x1px) fly from the tear point. The mustache is tilted 20deg from horizontal, being grabbed/ripped. A brief flash of pain (2 red veins appear on the mustache, rage vein red, 1px lines pulsing outward from center). Motion anticipation line (1px, white) arcing from the face position upward. The hair bristles outward (individual strand lines separate slightly at edges -- the mustache is ANGRY about being detached). A small golden flash (4x4px, justice gold, 40% opacity) at the detachment point.

### Frame 2: Throw Animation - Wind-up (Justice Charging)
- **Position in sheet:** 96,0 to 143,47
- **Description:** The mustache, now fully detached, is drawn back behind the thrower. It begins to GLOW -- the golden justice aura intensifies (3px wide, justice gold, 40% opacity). The hair bristles even more aggressively (edge strands fan outward, the mustache looks ENRAGED). The tips of the mustache curve inward slightly, forming an aerodynamic boomerang shape. Small golden sparkles (3, 1x1px, justice gold) appear at the tips. The detachment wound at center is now a red line (healed/cauterized by JUSTICE). A wind current line (1px, wind white) spirals around the mustache, showing the throw building momentum. The mustache VIBRATES with righteous energy (1px shift from center).

### Frame 3: Throw Animation - Release (JUSTICE IS SERVED!)
- **Position in sheet:** 144,0 to 191,47
- **Description:** The mustache LAUNCHES forward, spinning. In this single frame, the mustache is at 45deg rotation (caught mid-spin). The justice aura BLAZES (5px wide, justice gold, 60% opacity). The tips leave golden arc trails (1px gold lines curving from each tip position, 8px long). Hair strands stream backward from the spin velocity (edge hairs stretch 2-3px behind rotation direction). A burst of patriotic particles (2 green, 2 yellow, 1 blue, each 1x1px, Brazilian flag colors) erupt from the center. The wind becomes visible -- 3 white circular motion lines around the mustache showing spin. A small shockwave ring (24px diameter, 1px, gold) expands from the launch point. The mustache casts a blur shadow below it (motion shadow, 3px offset, 40% opacity, slightly behind).

### Frame 4: Projectile - Spinning Mustache 1 (0 degrees) (32x32px)
- **Position in sheet:** 0,0 to 31,31 (projectile sheet)
- **Description:** The mustache in flight, horizontal orientation (0 degrees). The boomerang shape is clear -- thick center, sweeping curved arms on each side. In the 32x32 projectile frame, the mustache spans ~28px wide, 10px tall at center. The hair is a dense black mass with visible strand texture. The tips are SHARP (pointed, slightly red from blood of previous cuts). Golden justice aura (2px, gold, 40% opacity) surrounds the entire shape. A circular wind trail (1px, white, 30% opacity) follows the spinning path -- a circle around the mustache. Small golden sparkles (2, 1x1px) at the tips. Blood droplets (1-2, red, 1x1px) trail behind the sharp tips. The mustache is CLEARLY spinning (rotation motion suggested by slight blur on edges).

### Frame 5: Projectile - Spinning Mustache 2 (90 degrees) (32x32px)
- **Position in sheet:** 32,0 to 63,31 (projectile sheet)
- **Description:** Mustache rotated 90 degrees -- now VERTICAL. The thick center is at the midpoint, arms sweep upward and downward. From this angle, the THICKNESS of the mustache is apparent (8px wide at center). The hair detail shows cross-section -- dense, layered, with grey streaks visible. Golden aura rotates with the mustache. Wind circle trail continues (new 90deg position). Blood on tips now pointing up and down. The hair strands fan outward from centrifugal force (1-2px extension at edges). This frame shows the mustache is a SERIOUS cutting implement -- thick enough to decapitate.

### Frame 6: Projectile - Spinning Mustache 3 (180 degrees) (32x32px)
- **Position in sheet:** 64,0 to 95,31 (projectile sheet)
- **Description:** Mustache at 180 degrees -- horizontal but FLIPPED from Frame 4 (tips point opposite direction). The spin speed is apparent from the frame-to-frame 90deg rotation. The hair texture shifts (different strands catch the light). Blood drops trail in new positions (shifted 90deg from Frame 5). The golden aura PULSES (brighter than Frame 4/5, 50% opacity -- the justice is building mid-flight). Small patriotic particle (1, random flag color, 1x1px) sheds from the spin. The jerky 90deg rotation per frame creates the signature twitchy Andre Guedes animation feel.

### Frame 7: Projectile - Spinning Mustache 4 (270 degrees) (32x32px)
- **Position in sheet:** 96,0 to 127,31 (projectile sheet)
- **Description:** Mustache at 270 degrees -- vertical again but FLIPPED from Frame 5. Completes the full rotation cycle (Frames 4-7 = 0, 90, 180, 270 = full 360deg spin). Golden aura at maximum intensity (60% opacity). Blood drops trail at maximum spread (the cutting edges are fully active). A brief FLASH at the tips (1px white, sharp, suggesting razor contact). The wind circle is complete. At this rotation, the returning boomerang trajectory begins curving back. If near an enemy, this is the pre-impact frame.

### Frame 8: Impact - "JUSTICA!" Frame 1
- **Position in sheet:** 192,0 to 239,47
- **Description:** The mustache SLICES through the target. A massive horizontal CUT LINE appears across the frame (2px wide, blood red bright, 40px long, centered). Hair strands FLY in all directions (6-8 small black 1x2px pieces, radially distributed -- both the target's hair and loose mustache strands). "JUSTICA!" (Justice!) text ERUPTS in BOLD gold (#FFD700) letters with blue (#002776) outline, hand-lettered, powerful, AUTHORITATIVE. The text is thick and commanding, not shaky -- Eneas delivers justice with CONVICTION. A golden starburst (24px diameter) behind the text. Blood splatter (4-5 red dots, 1-2px, scattered near the cut line). The mustache itself is at the far side of the frame, passing through the target. Brazilian flag color sparkles (2 green, 2 yellow, 1 blue, 1x1px) burst from the impact.

### Frame 9: Impact - "JUSTICA!" Frame 2
- **Position in sheet:** 240,0 to 287,47
- **Description:** "JUSTICA!" at MAXIMUM SIZE (fills 85% of frame width). Letters are SOLID and BOLD -- unlike other weapons' shaky text, this text is STABLE and AUTHORITATIVE (Eneas is decisive, not panicked). Gold letters glow with white inner highlight. The cut line remains, now with additional slash marks (2 more, crossing the first at angles -- a triple cut). Hair debris at maximum spread. Blood splatter spreads. The golden starburst intensifies -- now with patriotic green and yellow rays alternating with gold. A small silhouette of a raised fist (justice symbol, 4x6px, dark, 30% opacity) appears behind the text. Screen flash: 2px gold border at 35% opacity.

### Frame 10: Impact - "JUSTICA!" Frame 3
- **Position in sheet:** 288,0 to 335,47
- **Description:** "JUSTICA!" fading with DIGNITY (80% scale, 60% opacity -- fades slower than other weapons because justice LINGERS). Gold shifts to warm bronze. Cut lines fade (from bright red to dark red). Hair debris settles to ground. Blood splatter persists (darker, drying). The golden starburst contracts to a small golden star (8x8px, persists at center for 500ms -- a "mark of justice" decal). Patriotic particles gone. The mood is not comedic dissipation -- it's RESPECTFUL fading, like a salute ending. Transition frame.

### Frame 11: Idle Effect - Bristle Flex 1
- **Position in sheet:** 336,0 to 383,47
- **Description:** Mustache at rest on Eneas' face with subtle idle animation. The hair BRISTLES leftward -- individual strand lines at the edges lean 1-2px left, as if blown by wind (or by Eneas breathing heavily). The tips curl slightly tighter (distinguished grooming reflex). Golden justice aura at minimum (1px, 15% opacity), gently present. A single grey streak catches light (1px lighter grey pixel appears in a strand). The center attachment point is secure (skin tone visible, no tearing). The mustache exudes quiet AUTHORITY even at rest.

### Frame 12: Idle Effect - Bristle Flex 2
- **Position in sheet:** 384,0 to 431,47
- **Description:** Hair bristles rightward (mirror of Frame 11). Tips curl in opposite direction. The golden justice aura shifts to the other side (asymmetric highlight). A different grey streak catches light. Together Frames 11-12 create a gentle breathing/bristling idle -- the mustache is ALIVE, gently flexing, always ready to detach and deliver justice. The movement is subtle and dignified, befitting Eneas' gravitas.

### Frame 13: Special - Boomerang Return 1 (Incoming)
- **Position in sheet:** 432,0 to 479,47
- **Description:** The mustache is RETURNING to Eneas' face from the throw. Seen from the target's perspective: the mustache approaches, spinning (at 45deg angle, mid-rotation). It's trailing a golden comet tail (justice gold, 3px wide, 12px long, fading from 60% to 10% opacity). Blood is visible on the tips (bright red, it has cut something). Loose enemy hair strands and debris trail behind in its wake (3-4 dark particles, 1x1px). The boomerang curve is visible in the trajectory -- a slight arc in the wind trail. The mustache is APPROACHING with PURPOSE -- it always returns. A patriotic sparkle (1, yellow, 1x1px) trails.

### Frame 14: Special - Boomerang Return 2 (Reattachment Approaching)
- **Position in sheet:** 480,0 to 527,47
- **Description:** Mustache very close to Eneas' face, decelerating. The spin slows (mustache at 15deg tilt -- nearly horizontal, settling into natural position). The golden comet tail shortens (6px, fading). Eneas' upper lip area (pink, 8px wide) is visible at the bottom of frame, WAITING for reattachment. The mustache's center base shows small golden threads (1px, justice gold) reaching TOWARD the lip -- magnetic reattachment beginning. Blood on tips drying (bright red to dark red). Wind trail dissipating. The hair strands settle back into groomed position (edge strands retract from combat fan to neat alignment).

### Frame 15: Special - Boomerang Return 3 (Reattachment!)
- **Position in sheet:** 528,0 to 575,47
- **Description:** SNAP! The mustache REATTACHES to Eneas' face. The center base connects to the upper lip area with a golden FLASH (6x4px, bright justice gold, 100% opacity for 1 frame). The hair instantly settles into its resting position -- dignified, groomed, authoritative. A small golden shockwave ring (16px diameter) expands from the reattachment point. Tiny sparkles (3, gold, 1x1px) pop at the connection. Any remaining blood on the tips is ABSORBED (the mustache cleans itself through justice). The tips spring slightly outward and settle (recoil from snap-on). A final patriotic flash: momentary green-yellow-blue sparkle trio at the base. The mustache looks EXACTLY as it did in Frame 0 -- as if it never left. Justice has been served and order is restored.

## Sprite Sheet Summary

| Frame | Name                | Position      | Purpose                    |
|-------|---------------------|---------------|----------------------------|
| 0     | static              | 0-47          | Inventory / on-face icon   |
| 1     | throw_detach        | 48-95         | Rip from face              |
| 2     | throw_windup        | 96-143        | Wind-up with justice aura  |
| 3     | throw_release       | 144-191       | Launch spinning             |
| 4     | spin_0deg           | proj 0-31     | Projectile 0deg rotation   |
| 5     | spin_90deg          | proj 32-63    | Projectile 90deg rotation  |
| 6     | spin_180deg         | proj 64-95    | Projectile 180deg rotation |
| 7     | spin_270deg         | proj 96-127   | Projectile 270deg rotation |
| 8     | impact_justica_1    | 192-239       | Onomatopeia appear         |
| 9     | impact_justica_2    | 240-287       | Onomatopeia peak           |
| 10    | impact_justica_3    | 288-335       | Onomatopeia fade           |
| 11    | idle_bristle_1      | 336-383       | Idle bristle left          |
| 12    | idle_bristle_2      | 384-431       | Idle bristle right         |
| 13    | return_incoming     | 432-479       | Boomerang returning        |
| 14    | return_approach     | 480-527       | Decelerating near face     |
| 15    | return_reattach     | 528-575       | Snap back onto face        |

## Phaser 3 Atlas Key
```
key: 'weapon_bigode_justica'
frameWidth: 48
frameHeight: 48
```
```
key: 'projectile_bigode_spin'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- This mustache must be INSTANTLY recognizable as Eneas' iconic facial hair -- thick, black, authoritative
- The DETACHMENT from the face is the grotesque comedy moment -- it should look painful and absurd
- In flight, the mustache is a DEADLY spinning blade -- the thick hair acts as cutting edges
- The boomerang return mechanic means EVERY throw ends with the glorious reattachment snap
- Unlike other weapons, the "JUSTICA!" text is NOT shaky -- it is BOLD, STABLE, AUTHORITATIVE
- Eneas believes in justice with absolute conviction and his weapon reflects that
- The golden justice aura is subtle at rest but BLAZES in combat -- proportional to conviction
- Blood on the cutting tips should be present but not excessive -- justice is clean, not gratuitous
- Brazilian patriotic colors (green, yellow, blue) appear as accent particles -- Eneas is a nationalist
- The hair texture must be LOVINGLY detailed -- individual strands, grooming lines, grey wisdom streaks
- Robert Crumb style applied to the grotesque concept, but the mustache itself is BEAUTIFUL within that style
- The reattachment frame is the payoff -- the mustache returns and it's like it never left
- The bare upper lip (visible during throw) should look WRONG and VULNERABLE -- Eneas without his mustache is incomplete
