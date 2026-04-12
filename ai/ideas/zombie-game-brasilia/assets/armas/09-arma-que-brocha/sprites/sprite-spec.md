# Arma que Brocha (as Vezes) -- Sprite Specification

**Weapon ID:** 09
**Boss:** Bolsonaro
**Type:** Ranged (Revolver) / 70% success, 30% backfire
**Category:** Boss Exclusive

---

## 1. Weapon Sprite (Held)

**Dimensions:** 48x48 px
**Anchor point:** Bottom-center (24, 44)

### Color Palette

| Name                | Hex       | Usage                                |
|---------------------|-----------|--------------------------------------|
| Gold Dark           | `#8B7500` | Gun body deep shadows                |
| Gold Main           | `#DAA520` | Primary gun body                     |
| Gold Bright         | `#FFD700` | Gun body highlights/reflections      |
| Gold Pale           | `#FFEAA7` | Extreme highlights/gleam             |
| Grip Brown Dark     | `#3E2723` | Gun grip shadows                     |
| Grip Brown          | `#5D4037` | Gun grip wood/leather texture        |
| Flag Green          | `#009739` | Brazil flag sticker (green)          |
| Flag Yellow         | `#FEDD00` | Brazil flag sticker (yellow diamond) |
| Flag Blue           | `#012169` | Brazil flag sticker (blue circle)    |
| Flag White          | `#FFFFFF` | Flag sticker "Ordem e Progresso"     |
| Muzzle Black        | `#0A0A0A` | Barrel opening                       |
| Steel Grey          | `#4A4A4A` | Trigger, cylinder details            |
| Red Accent          | `#CC0000` | Decorative grip inlays               |
| Chrome Silver       | `#C0C0C0` | Cylinder, hammer                     |
| Black Outline       | `#1A1A1A` | Thick outlines (Crumb style)         |

### Frame Descriptions

#### Frame 1 -- Static / Inventory
- ABSURDLY oversized golden cowboy revolver (Colt SAA style)
- Viewed top-down, barrel pointing up (north)
- Entire body is gaudy gold plating -- overly shiny, tacky
- Grip: dark brown faux-leather wrap with red "patriotic" inlays
- Brazil flag sticker on the barrel side (green rectangle, yellow diamond, blue circle)
  - Sticker looks cheaply applied, slightly peeling at one corner
- Cylinder: chrome silver with 6 visible chambers
- Hammer: pulled back, ready position
- Barrel is COMICALLY long (takes up 60% of sprite height)
- Overall design screams "overcompensating macho" -- every detail is too much
- Thick black outlines (3px), heavy shadows
- Small engraved text on barrel (too small to read but implying "MITO")

#### Frame 2 -- Idle Gleam A
- Same as Frame 1
- Gold gleam/shine effect on barrel (bright white sparkle at barrel tip, 3px star shape)
- Slight metallic shimmer on body (shifted highlight position)

#### Frame 3 -- Idle Gleam B
- Same as Frame 1
- Gold gleam on grip area (sparkle migrated)
- Different highlight position on cylinder
- Flag sticker corner lifts slightly more

---

## 2. Successful Shot Animation (70% chance)

**Dimensions:** 48x48 px per frame
**Frames:** 4
**Sprite sheet:** 192x48 px

#### Frame 1 -- Aim
- Revolver tilted slightly forward (5 degrees toward target)
- Hammer fully cocked
- Slight gold gleam on barrel tip
- "Tension" lines around trigger area (2 small black lines)

#### Frame 2 -- Fire
- MASSIVE muzzle flash emanating from barrel (fills top 40% of frame)
  - White core, yellow mid, orange edges
  - Flash is star-shaped, 5 points, irregular (not symmetric)
- Revolver kicked back slightly (recoil, shifted 3px down)
- Cylinder has rotated (one chamber advanced)
- Smoke beginning from barrel

#### Frame 3 -- Recoil Peak
- Revolver at maximum recoil position (shifted 5px down, 2px rotated back)
- Muzzle flash dissipating (smaller, more orange/red)
- Heavy smoke cloud from barrel (grey, 8px wide)
- Spent brass casing ejecting from side (small gold rectangle, 3px)
- "POW!" implied by visual energy

#### Frame 4 -- Recovery
- Revolver returning to normal position
- Residual smoke wisps
- Barrel still hot (tiny red-orange glow at tip, 2px)
- Spent casing now at 10px distance, falling

---

## 3. BACKFIRE Animation (30% chance)

**Dimensions:** 48x48 px per frame
**Frames:** 4
**Sprite sheet:** 192x48 px

#### Frame 1 -- Attempt
- Same as Successful Shot Frame 1 (aim position)
- Identical to build expectation

#### Frame 2 -- Misfire
- Instead of muzzle flash FORWARD, a pathetic PUFF exits barrel
  - Tiny grey-brown smoke cloud (10px, sad and wimpy)
  - No flash, no fire -- just a deflating "pfft"
- A small "click" visual: tiny impact star at hammer (3px, grey)
- Gun vibrates/shakes (offset 1px in random direction)
- Flag sticker peels off slightly more

#### Frame 3 -- Backfire Damage
- Small explosion at the GRIP end (behind the gun)
  - Orange-red puff (12px)
  - Directed BACK toward Bolsonaro
- Revolver cracked slightly (thin dark line on barrel)
- Comedic black soot marks on gun body
- The gold plating is chipped, revealing grey steel underneath in 2-3 spots
- Sad little smoke ring drifts from barrel

#### Frame 4 -- Embarrassment
- Gun drooping downward (barrel points down, "limp" angle ~30 degrees)
- Heavy soot/smoke residue on entire gun
- Flag sticker half peeled off
- A single comedic teardrop shape near the barrel (sweat drop, blue, 3px)
- General aura of pathetic failure
- Gold is dulled/tarnished

---

## 4. Projectile -- Bullet (Successful Shot)

**Dimensions:** 32x32 px per frame
**Frames:** 4
**Sprite sheet:** 128x32 px

#### Frame 1 -- Bullet Flight A
- Oversized golden bullet (rifle-caliber size, comically big)
- Gold casing with darker gold shadow on bottom
- Bright tip (pale gold highlight)
- Motion lines behind (3 horizontal lines, fading)
- Small flame trail at base (orange, 4px)

#### Frame 2 -- Bullet Flight B
- Same bullet, slight rotation
- Motion lines shifted
- Flame trail larger (6px)
- 1-2 gold sparkle particles trailing

#### Frame 3 -- Bullet Flight C
- Bullet with spin-blur effect (slight horizontal stretch)
- Flame trail at peak (8px)
- Air distortion ring around bullet (1px transparent ring)
- More sparkle trail

#### Frame 4 -- Bullet Flight D
- Bullet at different spin angle
- Flame trail cycling back (5px)
- Trail of gold dust particles (3-4 tiny 1px dots)

---

## 5. Bullet Impact (Successful Hit)

**Dimensions:** 48x48 px per frame
**Frames:** 3
**Sprite sheet:** 144x48 px

#### Frame 1 -- Impact Flash
- Bright gold-white impact star (20px, 6-pointed)
- Bullet fragments spraying outward (4-5 gold shards)
- Red damage splatter mixed in (4-5 red pixels)
- Central white core

#### Frame 2 -- Expansion
- Star expands (28px)
- Gold particle ring expanding outward
- Small "MITO!" text fragment in gold (satirical)
- Fragments at greater distance

#### Frame 3 -- Fade
- Star shape dissolving
- Residual gold sparkles (5-6 fading)
- Smoke wisps
- "MITO!" text fading out

---

## 6. Backfire -- Pathetic Smoke Puff

**Dimensions:** 32x32 px per frame
**Frames:** 3
**Sprite sheet:** 96x32 px

#### Frame 1 -- Initial Puff
- Small grey-brown cloud (8px radius)
- Off-center, drooping downward
- A few pitiful sparks (orange, 1px, only 2-3)
- Shape: lumpy, asymmetric (not a proud explosion)

#### Frame 2 -- Expanding Sadness
- Cloud grows slightly (12px) but stays pathetic
- Color shifts to more grey (losing brown warmth)
- Sparks dying out
- A tiny broken bullet falls out of the cloud (3px gold, cracked)

#### Frame 3 -- Dissipating Shame
- Cloud wispy and barely there (15px but very transparent)
- Almost entirely grey
- Single gold flake drifting down
- Feels empty and disappointing

---

## 7. "TALKEI?" Text Popup (Backfire)

**Dimensions:** 48x24 px
**Frames:** 1 (static, animated via code)

- White speech bubble with black outline
- Text: "TALKEI?" in bold red comic font
- Bubble has classic comic tail pointing down
- Slight tremor in letter positioning (letters not perfectly aligned -- nervous/embarrassed)
- Question mark is larger than other letters

---

## Notes

- The gun's design must be ABSURDLY macho/overcompensating -- it should look like a parody of masculinity
- The gold plating should look CHEAP, not elegant -- gaudy like a costume prop, not a real gold gun
- The Brazil flag sticker is the cheapest possible -- like a bumper sticker, not an engraving
- Backfire animation must feel PATHETICALLY funny, not just "gun jam" -- it should be humiliating
- The "TALKEI?" is Bolsonaro's verbal tic, used here as the sad punchline
- 70/30 split should be handled in game logic, but both animation sets must be loaded
- Boss scale: revolver should be nearly as long as Bolsonaro's full sprite height
- The barrel should remind viewers of phallic overcompensation -- this is the entire joke
