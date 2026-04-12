# Cracha Afiado — Sprite Specification

## Overview
Government employee badge sharpened into a lethal throwing star. The badge features a comically bad ID photo, the name "SILVA, J.C." in block letters, and "SERVIDOR PUBLICO FEDERAL" stamped across the bottom. The edges are visibly sharpened to razor points with metallic glint highlights. The lanyard remnant trails behind when thrown. Boomerang return mechanic.

## Dimensions
- **Weapon sprite (held/inventory):** 32x32px
- **Projectile (in-flight):** 32x32px
- **Impact frames:** 32x32px
- **Paper trail particles:** 16x16px each

## Color Palette

| Element                | Hex Code  | Description                         |
|------------------------|-----------|-------------------------------------|
| Badge base             | #C4A35A   | Dirty brass/gold laminated plastic  |
| Badge border           | #8B6914   | Dark gold metallic edge             |
| Sharpened edges        | #E8E8E8   | Bright steel silver (razor glint)   |
| Edge glint highlight   | #FFFFFF   | Pure white flash on blade tips      |
| Photo area             | #7A9EBF   | Washed-out blue passport photo bg   |
| Photo face             | #D4A574   | Skin tone (tiny caricature face)    |
| Text "SERVIDOR"        | #1A1A1A   | Black stencil text                  |
| Badge clip remnant     | #A0A0A0   | Gray metal clip stub                |
| Lanyard trail          | #2E4A7A   | Dark government-blue ribbon         |
| Paper particles        | #F5F0E0   | Yellowed bureaucratic paper         |
| Paper text scribbles   | #3A3A3A   | Dark gray fake handwriting          |
| Blood on return        | #8B0000   | Dark crimson                        |
| Spin blur              | #C4A35A50 | Semi-transparent gold motion blur   |

## Frame-by-Frame Descriptions

### Static / Inventory (1 frame)
**Frame 0 — `cracha_static.png`**
The badge sits at a slight diagonal (15-degree tilt). The rectangular badge with rounded corners fills roughly 24x28px within the 32x32 canvas. The top has a small metal clip stub (2px). The photo area is a 8x10px rectangle in the upper-left quadrant showing a tiny grotesque caricature face (2 dark dots for eyes, a squiggle mouth). Below the photo: two lines of illegible text scribbles representing name/title. Across the bottom in readable block letters: "SERVIDOR" (1px tall font approximation). All four corners have visible metallic sharpened points that extend 2px beyond the badge body, catching white glint highlights. The lanyard stub hangs from the clip, a 3px dangling blue ribbon. Overall dirty, worn look with slight yellowing.

### Throw / Use Animation (4 frames)
**Frame 1 — `cracha_throw_01.png`**
Wind-up: The badge is held at the character's side, tilted back 45 degrees. The arm (implied by position offset) pulls the badge behind. A small "whoosh" line (2px white arc) begins forming. The badge details are fully visible and sharp.

**Frame 2 — `cracha_throw_02.png`**
Release: The badge leaves the hand position, now centered in frame. Slight forward lean (30-degree rotation from vertical). Two motion lines trail behind it (white, 1px). The sharpened corners have small white glint sparks (1px dots). The lanyard whips upward.

**Frame 3 — `cracha_throw_03.png`**
Full spin: The badge is now a 45-degree rotated blur. The details are partially obscured by rotational motion — the photo and text are smeared. A circular motion arc surrounds it (1px gold semi-circle). Three speed lines trail behind. First paper particle spawns behind.

**Frame 4 — `cracha_throw_04.png`**
Extended flight: The badge is rotated 90 degrees from Frame 1 (horizontal). Maximum spin blur effect — the badge appears as an angular star shape with the sharpened corners creating a throwing-star silhouette. Strong speed lines (3 trailing). The lanyard is a blue spiral. Two paper particles trail behind at different distances.

### Projectile Flight (4 frames — looping)
**Frame 0 — `cracha_flight_01.png`**
The badge at 0-degree rotation (upright). Sharpened corners gleam. Slight spin blur on edges. One paper particle spawning at origin point behind badge.

**Frame 1 — `cracha_flight_02.png`**
Rotated 90 degrees clockwise. The photo/text now sideways. Glint shifts to upper-right corner. Paper trail: two papers at varying distances behind, gently tumbling.

**Frame 2 — `cracha_flight_03.png`**
Rotated 180 degrees — badge upside-down. Text and photo inverted. Glint on lower-left corner. Three paper particles trailing, the furthest one almost faded.

**Frame 3 — `cracha_flight_04.png`**
Rotated 270 degrees. Near-completion of full spin cycle. All four corners have had their glint moment. Paper trail at maximum — four small papers of varying opacity trailing in a gentle arc, suggesting the boomerang curve path.

### Impact (3 frames)
**Frame 0 — `cracha_impact_01.png`**
The badge embeds into target at a dramatic angle (stuck at 30 degrees). A burst of 6-8 paper fragments explodes outward in a radial pattern from the impact point. White flash circle (4px radius) at the point of contact. The text "PLONK!" begins appearing in red blocky letters above (2px tall, partially formed).

**Frame 1 — `cracha_impact_02.png`**
The badge vibrates in place (1px offset shake). Paper fragments have spread further outward (8px radius). The flash has expanded and is fading (6px radius, lower opacity). "PLONK!" text is fully formed and bold. Small blood/ink drops (dark red, 1px) spray from impact. The badge photo is cracked.

**Frame 2 — `cracha_impact_03.png`**
The badge begins returning — pulling free with a small motion arc showing return trajectory. Paper fragments are settling/fading. Flash fully gone. "PLONK!" text starting to fade. A thin curved line shows the boomerang return path. Tiny debris particles (1px, mixed gold and white) scatter.

### Idle Glow / Effect (2 frames — looping)
**Frame 0 — `cracha_idle_01.png`**
The badge in static position with a subtle metallic shimmer. The sharpened corners have small 1px white glint dots on the upper-right and lower-left corners. The "SERVIDOR" text has a faint pulse glow (slightly brighter than base). A single paper particle floats lazily nearby, half-transparent.

**Frame 1 — `cracha_idle_02.png`**
The glint dots shift to upper-left and lower-right corners (alternating flash pattern suggesting sharpness). The text glow has subsided. The floating paper particle has drifted slightly and is more faded. The badge has a 1px sub-pixel shift downward (breathing idle).

## Sprite Sheet Layout
Horizontal strip: 32px height, frames laid out left-to-right.

| Sheet             | Frames | Total Width |
|-------------------|--------|-------------|
| `cracha_static`   | 1      | 32px        |
| `cracha_throw`    | 4      | 128px       |
| `cracha_flight`   | 4      | 128px       |
| `cracha_impact`   | 3      | 96px        |
| `cracha_idle`     | 2      | 64px        |

## Paper Trail Particle Sprites (16x16px)
**`paper_particle_01.png`** — Small rectangular piece of paper, slightly crumpled, with faint text lines. Yellowed.
**`paper_particle_02.png`** — Same paper but rotated 45 degrees and more crumpled. Slightly more transparent.
**`paper_particle_03.png`** — Smallest fragment, mostly curled, very faded. Near end of trail lifetime.

## Notes
- The boomerang return animation reuses the flight frames in reverse order (3, 2, 1, 0).
- Paper trail particles are independent emitter objects in Phaser, not baked into the weapon sprite sheet.
- On critical hit, the impact "PLONK!" changes to "DEFERIDO!" (APPROVED) in green — a rare ironic joke.
- The badge photo should be just recognizable enough as a terrible ID photo but not depict any real person.
