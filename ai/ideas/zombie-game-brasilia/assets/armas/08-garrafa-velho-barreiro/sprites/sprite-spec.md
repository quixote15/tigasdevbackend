# Garrafa de Velho Barreiro Incendiaria -- Sprite Specification

**Weapon ID:** 08
**Boss:** Lula
**Type:** Ranged / Area-of-Effect (Molotov)
**Category:** Boss Exclusive

---

## 1. Weapon Sprite (Held)

**Dimensions:** 48x48 px
**Anchor point:** Bottom-center (24, 44)

### Color Palette

| Name               | Hex       | Usage                              |
|--------------------|-----------|-------------------------------------|
| Bottle Green Dark  | `#2E5A1C` | Main glass body shadow              |
| Bottle Green       | `#4A8B2F` | Main glass body                     |
| Bottle Green Light | `#6BBF47` | Glass highlight/reflection          |
| Label Cream        | `#F5E6C8` | Velho Barreiro label background     |
| Label Red          | `#C41E3A` | "Edicao Companheira" text           |
| Label Gold         | `#D4A017` | Label border/star details           |
| Cachaça Amber      | `#C68E17` | Liquid inside bottle                |
| Rag Orange         | `#E85D04` | Cloth fuse (top)                    |
| Rag Orange Dark    | `#9D4300` | Cloth fuse shadow                   |
| Flame Yellow       | `#FFD700` | Flame core                          |
| Flame Orange       | `#FF6B00` | Flame mid                           |
| Alcohol Blue       | `#4488FF` | Alcohol-tinted flame tips           |
| Black Outline      | `#1A1A1A` | Thick outlines (Crumb style)        |

### Frame Descriptions

#### Frame 1 -- Static / Inventory
- Bottle viewed from slightly above (top-down perspective)
- Green glass bottle, rectangular-ish with rounded shoulders
- Prominent label reading "VELHO BARREIRO" in bold serif, subtitle "Edicao Companheira" in red cursive
- Small red star (PT symbol) on label corner
- Amber liquid visible through glass (3/4 full)
- Orange rag stuffed in bottleneck, tip on fire
- Thick black outlines (3px), heavy shadows on left side
- Flame at top rendered with 2-3 licks of fire (yellow core, orange mid, blue alcohol tips)

#### Frame 2 -- Idle Glow A
- Same as Frame 1 but flame leans slightly LEFT
- Subtle amber glow around bottle neck (2px)
- Liquid inside has a slight wave pattern shifted right
- Blue alcohol flame tips more visible

#### Frame 3 -- Idle Glow B
- Same as Frame 1 but flame leans slightly RIGHT
- Amber glow shifted
- Liquid wave pattern shifted left
- Orange flame more dominant

---

## 2. Swing / Throw Animation (Weapon Use)

**Dimensions:** 48x48 px per frame
**Frames:** 4
**Sprite sheet:** 192x48 px (4 frames horizontal)

#### Frame 1 -- Wind-Up
- Bottle pulled back (shifted 6px right, 4px up from center)
- Bottle rotated ~20 degrees clockwise
- Flame trails slightly behind (motion blur suggestion with 2 smaller flame copies)
- Lula's hand implied at bottom (grotesque thick fingers, pinky ring)

#### Frame 2 -- Mid-Swing
- Bottle at apex, centered, tilted 45 degrees
- Flame stretched vertically (excitement)
- Motion lines (3 curved black lines trailing)
- Label partially visible, distorted by angle

#### Frame 3 -- Release
- Bottle leaving hand, tilted ~70 degrees forward
- Flame now a bright streak
- 2-pixel motion blur trail behind bottle
- Visible arc trajectory start (small dotted line, 3 dots)

#### Frame 4 -- Follow-Through
- Hand open (empty), fingers splayed grotesquely
- Small amber droplets (3-4 pixels each) where bottle was
- Residual flame spark (2px yellow dot)

---

## 3. Projectile -- Bottle in Flight

**Dimensions:** 32x32 px per frame
**Frames:** 4 (rotation cycle)
**Sprite sheet:** 128x32 px

#### Frame 1 -- Rotation 0 degrees
- Bottle viewed top-down, label facing up
- Flame trail streaming behind (8-10px)
- Bottle slightly smaller than held version (fits 32x32)
- Amber liquid sloshing visibly
- Blue-tinged flame at fuse

#### Frame 2 -- Rotation 90 degrees
- Bottle rotated, side view of glass body
- Flame trails in spiral pattern
- Label text sideways
- Liquid shifted to one side of bottle

#### Frame 3 -- Rotation 180 degrees
- Bottle upside-down, bottom of glass visible
- Flame now at bottom visually
- Drips of cachaça (2-3 amber pixels) falling from neck
- Maximum flame intensity (largest flame)

#### Frame 4 -- Rotation 270 degrees
- Mirror of Frame 2 (other side)
- Flame wrapping around bottle body
- Glass reflection highlight on opposite side
- Trail of small ember particles (1px orange/yellow dots, 4-5 of them)

---

## 4. Impact / Explosion

**Dimensions:** 64x64 px per frame (OVERSIZED for boss weapon emphasis)
**Frames:** 4
**Sprite sheet:** 256x64 px

#### Frame 1 -- Initial Shatter
- Glass fragments exploding outward (8-10 green shards, irregular shapes)
- Central flash: bright white/yellow core (8px radius)
- Amber liquid splash radiating (thick droplets)
- Label fragment visible in debris (torn "VELH-" readable)
- Black outline fragments

#### Frame 2 -- Fireball Expansion
- Orange-yellow fireball (28px radius)
- Blue alcohol flames at edges (distinctive blue-tipped tongues)
- Glass shards now at periphery, some on fire
- Thick black smoke starting at top
- Cachaça puddle forming at base

#### Frame 3 -- Maximum Explosion
- Full fireball (40px radius fills most of frame)
- Mixed orange/yellow/blue flames in chaotic pattern
- Dark smoke ring at edges
- Ground scorching visible (dark brown/black circle underneath)
- Small "stars" and "embers" at extreme edges

#### Frame 4 -- Dissipating
- Fireball shrinking (20px radius)
- Heavy black-grey smoke billowing upward
- Remaining blue alcohol flames flickering at base
- Transition to fire pool state

---

## 5. Fire Pool (Area Denial)

**Dimensions:** 64x64 px per frame
**Frames:** 4 (looping)
**Sprite sheet:** 256x64 px

#### Frame 1 -- Active Pool A
- Circular pool of burning cachaça on ground (~48px diameter)
- Amber-orange liquid base with flame tongues rising (6-8 small flames)
- Blue alcohol flame tips on 30% of flames
- Dark scorch marks at edges
- Wavering heat distortion lines above (2px wavy lines, semi-transparent)

#### Frame 2 -- Active Pool B
- Same pool, flames shifted position (randomized look)
- Some flames taller, others shorter vs Frame 1
- Blue tips now on different flames
- Subtle cachaça puddle shimmer effect

#### Frame 3 -- Active Pool C
- Flames slightly diminished overall
- More smoke (grey wisps rising)
- Pool edges starting to darken
- A few embers popping off (1px yellow dots above flames)

#### Frame 4 -- Active Pool D
- Different flame arrangement than A/B/C
- Peak of blue alcohol flames (most blue this frame)
- Crackling effect: tiny bright-white pixel flashes (2-3)

---

## 6. "Drunk" Effect on Enemies

**Dimensions:** 32x32 px per frame (overlay on enemy sprite)
**Frames:** 3 (looping for 3-second duration)
**Sprite sheet:** 96x32 px

#### Frame 1 -- Drunk Overlay A
- Spiral "dizzy" symbols over enemy head (classic cartoon drunk)
- Small green cachaça bottle icons orbiting (2 tiny 4px bottles)
- Wavy distortion lines around enemy edges
- Greenish-amber tint overlay on enemy

#### Frame 2 -- Drunk Overlay B
- Spirals rotated 120 degrees from Frame 1
- Bottles at different orbital positions
- Pink "blush" marks on enemy (2 small pink circles on face area)
- Musical note icon (suggesting singing/stumbling)

#### Frame 3 -- Drunk Overlay C
- Spirals rotated 240 degrees
- Bottles at yet another position
- Stars mixed with spirals
- Slight green tint pulsing brighter

---

## Notes

- The label "Edicao Companheira" is a satirical play on "companheiro" (Lula's trademark greeting)
- Boss weapon scale: the bottle should appear COMICALLY LARGE when held -- nearly as tall as Lula's sprite
- Fire pool persists 5 seconds in-game, the 4-frame loop cycles continuously
- "Drunk" effect inverts enemy controls for 3 seconds and applies the dizzy overlay
- All outlines must be THICK (2-3px minimum) per the Crumb/Andre Guedes underground comix style
- Glass reflections should feel grimy, not clean -- this is cheap cachaça, not fine wine
