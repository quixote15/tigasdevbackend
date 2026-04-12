# Toga de Teflon -- Sprite Specification

**Weapon ID:** 12
**Boss:** Gilmar (Gilmar Mendes)
**Type:** Defensive / Reflective (Teflon-coated judicial robe)
**Category:** Boss Exclusive

---

## 1. Weapon Sprite (Worn -- Replaces Held Weapon)

**Dimensions:** 48x48 px
**Anchor point:** Center (24, 24) -- worn on body, not held

### Color Palette

| Name                  | Hex       | Usage                                    |
|-----------------------|-----------|------------------------------------------|
| Toga Black            | `#1A1A1A` | Primary robe color (deep black)          |
| Toga Black Highlight  | `#2D2D2D` | Robe fold highlights                     |
| Toga Black Shadow     | `#0A0A0A` | Robe deepest shadows/creases             |
| Teflon Sheen          | `#4A5568` | Teflon reflective surface sheen          |
| Teflon Highlight      | `#718096` | Teflon bright spots (non-stick gleam)    |
| Teflon Flash          | `#A0AEC0` | Maximum Teflon reflection               |
| Pastel Grease Stain   | `#E8C547` | Pastel (food) grease stains              |
| Pastel Grease Dark    | `#C4A030` | Grease stain shadows/depth              |
| Pastel Cream          | `#FFF3C4` | Lighter pastel crumb stains              |
| Money Green           | `#2D8B4E` | Bills sticking out of pocket             |
| Money Green Dark      | `#1A6B35` | Money shadow                             |
| Money Green Light     | `#45B868` | Money highlight                          |
| Pocket Lining Red     | `#8B2252` | Inner pocket lining visible              |
| Gold Trim             | `#B8860B` | Robe ceremonial trim                     |
| Gold Trim Light       | `#DAA520` | Trim highlights                          |
| Deflection Silver     | `#E2E8F0` | Projectile deflection flash              |
| Deflection Blue       | `#63B3ED` | Teflon energy field                      |
| Reflection Red        | `#FF4444` | Reflected projectile tint                |
| Black Outline         | `#1A1A1A` | Thick outlines                           |

### Frame Descriptions

#### Frame 1 -- Static / Inventory
- Judicial robe (toga) viewed top-down, draped over invisible mannequin shape
- Predominantly BLACK fabric with visible fold lines and creases
- TEFLON SHEEN: unnatural metallic-grey reflective patches on surface (3-4 highlights)
  - These are NOT fabric reflections -- they look like an oil-slick/teflon coating
  - Slightly iridescent quality (blue-grey shifts)
- PASTEL GREASE STAINS: 3-4 yellowish grease spots on front of robe
  - Irregular shapes (5-8px each), clearly food grease
  - One stain has a visible pastel CRUMB (2px cream dot with flaky texture)
  - Positioned on chest area and one near pocket
- POCKET WITH MONEY: right side pocket bulging outward
  - Dark robe pocket opening visible
  - Red silk lining peeking out
  - 2-3 green bills (R$100 notes) sticking out sloppily
  - One bill halfway falling out (diagonal, lower half exposed)
  - Bills have visible "100" text (tiny)
- Gold ceremonial trim along collar and front edges (thin gold lines, 1px)
- Overall impression: once-dignified judicial robe, now corrupted and stained
- Thick black outlines (3px), heavy shadows in folds

#### Frame 2 -- Idle Shimmer A
- Same as Frame 1
- Teflon sheen SHIFTS: highlights migrate 2-3px clockwise around robe
- Creates "oil slick" visual movement
- One money bill shifts slightly (wind or movement)
- Faint silver-blue aura around robe edges (1px, alpha 0.15)

#### Frame 3 -- Idle Shimmer B
- Same as Frame 1
- Teflon sheen shifts in opposite direction from Frame 2
- Different highlight positions
- Money bill shifts back
- Pastel grease stain on chest appears slightly MORE visible (grease spreading?)
- Silver-blue aura on different section of robe edge

---

## 2. Deflection Animation (When Projectile is Absorbed / Deflected)

**Dimensions:** 48x48 px per frame
**Frames:** 4
**Sprite sheet:** 192x48 px

#### Frame 1 -- Projectile Contact
- Projectile hitting the toga surface (incoming from any direction)
- Contact point: bright silver-white flash (6px star)
- Teflon surface at contact point goes BRIGHT (full Teflon Flash color)
- Ripple starting on robe fabric from contact point
- Robe folds distort slightly from impact force
- Money in pocket jolts (bills shift from impact)

#### Frame 2 -- Teflon Activation
- Entire teflon coating LIGHTS UP -- all sheen patches glow simultaneously
- Silver-blue energy field visible around entire robe (3px aura, alpha 0.3)
- The projectile is visibly SLIDING off the surface
  - Projectile sprite compressed/flattened against teflon
  - Directional streak marks where projectile slides
- "Non-stick" visual: small droplets of projectile energy beading and rolling off
- Pastel grease stains glow slightly (even the grease is teflon-coated)
- Text flickers: "NADA PEGA" (nothing sticks) in tiny silver letters (6px)

#### Frame 3 -- Reflection Burst (33% chance branch)
- If reflecting: projectile LAUNCHES back from toga surface
  - Red-tinted version of original projectile appears leaving the robe
  - Bright flash at launch point (8px, silver-red star)
  - Speed lines radiating OUTWARD from robe
  - Robe ripples outward from reflection point
- If absorbing (67%): projectile simply dissolves
  - Silver sparkles where projectile was (5-6 particles)
  - Quieter effect, projectile energy absorbed into toga
  - Toga briefly glows warmer (grease stains shimmer)

#### Frame 4 -- Recovery
- Toga settling back to normal
- Teflon sheen slowly dims back to idle levels
- Residual silver sparkles fading (3-4 remaining)
- Money in pocket resettles
- One additional bill may have slipped further out (corruption continues)
- Faint residual aura fading

---

## 3. Reflected Projectile (When 33% Reflection Triggers)

**Dimensions:** 32x32 px per frame
**Frames:** 3
**Sprite sheet:** 96x32 px

#### Frame 1 -- Reflected Shot A
- Original projectile sprite but RE-COLORED:
  - Base: silver-grey tint replacing original colors
  - Overlay: red angry tint (`#FF4444` at alpha 0.3)
  - Edge: silver-blue trailing energy
- Motion lines behind (reversed from original direction)
- Teflon energy wisps trailing (blue-silver, 3-4 small particles)
- Looks "corrupted" -- the projectile has been tainted by Gilmar's toga

#### Frame 2 -- Reflected Shot B
- Same reflected projectile, slight rotation
- Energy wisps at different positions
- Red tint pulses brighter
- Silver streaks extend from edges

#### Frame 3 -- Reflected Shot C
- Reflected projectile, another rotation
- Energy fading slightly (less silver trail)
- Red tint stable
- Approaching original attacker

---

## 4. Money Falling Effect (Passive / Continuous)

**Dimensions:** 16x16 px per frame
**Frames:** 4 (falling bill cycle)
**Sprite sheet:** 64x16 px

#### Frame 1 -- Bill Flutter A
- Single R$100 bill (green) fluttering down
- Bill at 0 degree angle, face visible
- "100" text visible
- Left edge slightly raised (wind)

#### Frame 2 -- Bill Flutter B
- Bill tilted 20 degrees right
- Flipping, back side partially visible (lighter green)
- Tumbling motion

#### Frame 3 -- Bill Flutter C
- Bill tilted -20 degrees left
- Full face visible again
- Lower in descent

#### Frame 4 -- Bill Flutter D
- Bill nearly flat, settling on ground
- Slightly crumpled from falling
- Semi-transparent (alpha 0.7 -- becoming ground litter)

---

## 5. "NADA PEGA" Text Effect (On Successful Deflection)

**Dimensions:** 48x16 px
**Frames:** 1 (code-animated)

- Silver text: "NADA PEGA" (Nothing Sticks)
- Font: elegant judicial serif, italic
- Color: `#A0AEC0` (silver-grey) with `#1A1A1A` 1px stroke
- Subtle teflon sheen on letters (highlight shifting across text)
- Small sparkle on the "N" or "P" (rotating which letter)

---

## 6. Absorption Effect (67% Non-Reflection)

**Dimensions:** 32x32 px per frame
**Frames:** 3
**Sprite sheet:** 96x32 px

#### Frame 1 -- Dissolve Start
- Incoming projectile at toga surface, losing shape
- Projectile sprite pixelating/dissolving from edges inward
- Silver teflon particles replacing projectile pixels
- Small flash at center of dissolution (white, 3px)

#### Frame 2 -- Dissolve Mid
- Projectile 60% dissolved
- More silver-blue particles where projectile was
- Energy being "absorbed" into toga -- subtle dark pulse inward
- Remaining projectile pixels scattered and fading

#### Frame 3 -- Dissolve Complete
- Projectile fully gone
- Cloud of silver sparkles (6-8 particles) at dissolution point
- Sparkles drifting inward toward toga center (absorbed)
- Residual shimmer (2-3 fading motes)
- A tiny "R$" symbol floats up from absorption point (corruption converts everything to money)

---

## Notes

- Gilmar Mendes is the STF minister known for "teflon" -- no accusations stick to him
- The toga is NOT a traditional weapon -- it is a DEFENSIVE/REFLECTIVE equip
- "Teflon" coating should look VISIBLY UNNATURAL on fabric -- it is a metaphor made literal
- Pastel (Brazilian savory pastry) grease stains are a reference to Gilmar's alleged corruption meetings at bakeries/restaurants
- Money falling from pockets is a CONTINUOUS passive effect -- bills slowly fall as Gilmar moves
- The 33% reflection mechanic: when a projectile hits the toga, there is a 33% chance it RETURNS to the attacker
- The remaining 67%: projectile is simply absorbed/nullified (still a strong defensive mechanic)
- Boss scale: the toga should billow and be oversized even on Gilmar's sprite, suggesting it is a living shield
- "NADA PEGA" (nothing sticks) is the key catchphrase -- the teflon metaphor
- The money constantly falling creates a trail behind Gilmar as he walks -- visual storytelling of corruption
- Pastel grease on the toga should look increasingly disgusting across the fight (could add more stains in later phases)
- The reflected projectile being RED-tinted suggests the toga "corrupts" whatever it reflects
- This weapon has NO offensive attack animation -- all specs are reactive/defensive
