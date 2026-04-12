# Caneta Bicolor -- Sprite Specification

**Weapon ID:** 10
**Boss:** BolsoLula (Fusion Boss)
**Type:** Ranged / Explosive (Ink Projectiles)
**Category:** Boss Exclusive

---

## 1. Weapon Sprite (Held)

**Dimensions:** 48x48 px
**Anchor point:** Bottom-center (24, 44)

### Color Palette

| Name                | Hex       | Usage                                  |
|---------------------|-----------|----------------------------------------|
| Pen Body White      | `#F0F0F0` | BIC pen main body (classic white)      |
| Pen Body Grey       | `#D0D0D0` | Pen body shadow/contour                |
| Red Cap             | `#CC0000` | Red end cap (PT/Lula side)             |
| Red Dark            | `#8B0000` | Red cap shadow                         |
| Red Bright          | `#FF1A1A` | Red cap highlight                      |
| Green-Yellow Cap    | `#009739` | Green end cap (Bolsonaro side)         |
| Yellow Accent       | `#FEDD00` | Yellow stripe on green cap             |
| Green Dark          | `#005C24` | Green cap shadow                       |
| Ink Red             | `#E60000` | Red ink drops/trail                    |
| Ink Green           | `#00AA44` | Green ink drops/trail                  |
| Ink Yellow          | `#FFD700` | Yellow ink accent drops                |
| Chrome Clip         | `#C0C0C0` | Pen clip (chrome metal)                |
| Chrome Highlight    | `#E8E8E8` | Clip highlight                         |
| BIC Blue            | `#0033A0` | "BIC" logo text on body                |
| Black Outline       | `#1A1A1A` | Thick outlines                         |
| Paper Cream         | `#FFF8DC` | "Emenda parlamentar" paper scraps      |
| Stamp Red           | `#CC0000` | "APROVADO" stamp on amendments         |

### Frame Descriptions

#### Frame 1 -- Static / Inventory
- GIANT BIC Cristal pen viewed top-down (comically oversized, nearly full sprite height)
- Classic BIC shape: hexagonal barrel, translucent-ish white body
- LEFT half has RED cap/end with PT star subtly embossed
- RIGHT half has GREEN-YELLOW cap/end with Brazil flag colors
- "BIC" logo in blue on center of barrel (distorted, reading "BIC*OLOR" -- pun on "bicolor")
- Chrome clip on top, absurdly large and bent (suggesting it clips onto giant pockets)
- The pen GLOWS faintly: red aura on red end, green aura on green end
- Visible through translucent body: ink cartridge split RED on left, GREEN on right
- Thick black outlines (3px), dirty shading
- Tip of pen (bottom): dual-point, one red nib, one green nib side by side

#### Frame 2 -- Idle Pulse A
- Same as Frame 1
- Red end PULSES brighter (aura expands 2px)
- Green end dims slightly
- Small red ink drop forming at red nib tip (2px)
- Suggests the "Lula side" is momentarily dominant

#### Frame 3 -- Idle Pulse B
- Same as Frame 1
- Green-yellow end PULSES brighter (aura expands 2px)
- Red end dims slightly
- Small green ink drop forming at green nib tip (2px)
- Suggests the "Bolsonaro side" is momentarily dominant

---

## 2. Signature / Attack Animation

**Dimensions:** 48x48 px per frame
**Frames:** 4
**Sprite sheet:** 192x48 px

#### Frame 1 -- Lift
- Pen rises slightly (shifted 3px up)
- Both ends glow equally (balanced power)
- Small anticipation lines at nib (2 tiny black marks)
- Ink drip hangs from tip

#### Frame 2 -- Downstroke Start
- Pen slams down and LEFT (signing motion, 5px shift)
- Red ink trail begins spraying from red nib
- Green ink trail begins spraying from green nib
- The two ink colors create parallel streaks
- "Paper" texture appears beneath pen (cream-colored rectangle, 16x10px)

#### Frame 3 -- Signature Flourish
- Pen sweeps RIGHT with dramatic flourish
- Both ink streams now forming an elaborate, illegible signature
- Red ink arcs left, green ink arcs right -- creating an X shape
- The paper/document beneath now has text: "EMENDA" partially visible
- Ink splatter droplets fly off in both directions (3-4 each color)

#### Frame 4 -- Stamp/Release
- Pen lifted back to original position
- The signed "emenda parlamentar" (amendment) document is now complete
- Visible "APROVADO" stamp appears on the paper in red
- The document begins GLOWING (it is now a projectile/bomb)
- Final ink droplets fall from nibs
- Small "R$" (money symbol) floats off the document

---

## 3. Projectile -- Explosive Parliamentary Amendment

**Dimensions:** 32x32 px per frame
**Frames:** 4 (flutter/rotation)
**Sprite sheet:** 128x32 px

#### Frame 1 -- Amendment Flight A
- Cream-colored official document, slightly crumpled
- Red and green ink signature visible on face
- "EMENDA PARLAMENTAR" text at top (tiny but present)
- "APROVADO" red stamp in corner
- Document flat, facing up
- Faint red-green glow aura
- Flutter: left edge slightly lifted

#### Frame 2 -- Amendment Flight B
- Document tilted 15 degrees
- Fluttering in wind (right edge now lifted)
- "R$ 999.999.999" visible (absurd money value)
- Red-green ink particles trailing behind (2-3 of each)
- Glow intensifies (about to explode)

#### Frame 3 -- Amendment Flight C
- Document tilted -15 degrees (opposite flutter)
- More crumpled/agitated looking
- Ink is BLEEDING off the document -- red drips left, green drips right
- Glow at maximum (pulsing bright)
- Small smoke wisps from edges (paper smoldering)

#### Frame 4 -- Amendment Flight D
- Document back to nearly flat
- Edges singed and darkening
- Red-green glow PULSING
- "APROVADO" stamp pulsing
- Ready to detonate

---

## 4. Impact / Explosion -- Bureaucratic Detonation

**Dimensions:** 64x64 px per frame
**Frames:** 4
**Sprite sheet:** 256x64 px

#### Frame 1 -- Paper Burst
- Document tears apart from center
- Paper confetti exploding outward (8-10 cream scraps)
- Central flash: split RED on left, GREEN on right (dual-color explosion)
- Ink splashes radiate: red ink west, green ink east
- Small "R$" money symbols fly out (3-4 golden characters)

#### Frame 2 -- Ink Explosion
- Massive dual-color ink explosion expanding
- Left hemisphere: RED ink splatter cloud (24px radius)
- Right hemisphere: GREEN ink splatter cloud (24px radius)
- Center: where they meet creates BROWN/DARK (ink mixing)
- Paper confetti now at far edges, some on fire
- Bureaucratic stamps flying: "URGENTE", "SIGILO", "CONFIDENCIAL" (tiny text fragments)

#### Frame 3 -- Maximum Expansion
- Full explosion: 50px diameter ink explosion
- Red and green inks swirling chaotically, mixing into muddy colors at center
- "R$" symbols now larger, spinning at edges
- Black smoke ring expanding outward
- Ground stained with bicolor ink puddles

#### Frame 4 -- Aftermath
- Explosion contracting
- Ink raining down (heavy red-green droplets falling)
- Permanent ink stains on ground (red and green splotches)
- Floating paper ash/embers (grey, tiny)
- Fading "APROVADO" ghost text in smoke

---

## 5. Ink Trail Effects (Persistent Ground Decoration)

**Dimensions:** 32x32 px per frame
**Frames:** 2 (alternating for variety)
**Sprite sheet:** 64x32 px

#### Frame 1 -- Red-Green Ink Trail A
- Ground-level ink stains
- Red ink splotch (irregular, 8-12px) on left
- Green ink splotch (irregular, 8-12px) on right
- Some mixing where they overlap (muddy brown-green)
- Semi-transparent (alpha 0.6) -- ground shows through

#### Frame 2 -- Red-Green Ink Trail B
- Different arrangement of ink splotches
- More splatter pattern (like drops from height)
- Slight variation in red and green positions
- Semi-transparent

---

## 6. Pen Never Runs Out -- Visual Feedback

**Dimensions:** 16x16 px
**Frames:** 2 (loop)
**Sprite sheet:** 32x16 px

#### Frame 1 -- Infinity Ink A
- Small infinity symbol (lemniscate) hovering near pen
- Left loop: RED
- Right loop: GREEN
- Subtle glow

#### Frame 2 -- Infinity Ink B
- Same infinity symbol, colors SWAPPED
- Left loop: GREEN
- Right loop: RED
- Pulsing glow (brighter)

---

## Notes

- BolsoLula is the FUSION BOSS -- a grotesque merge of Bolsonaro and Lula
- The bicolor pen represents the absurd political duality: both sides sign spending amendments
- "Emenda parlamentar" (parliamentary amendment) is a real Brazilian political mechanism for budget allocation -- the joke is that both sides abuse it equally
- The pen NEVER runs out because politicians never stop signing spending bills
- The infinity symbol is a small UI indicator reinforcing the "infinite ink" mechanic
- Dual-color effects should always split cleanly: RED = left/Lula, GREEN-YELLOW = right/Bolsonaro
- Boss scale: the pen should be as tall as BolsoLula's grotesque merged sprite
- The attack creates "explosive amendments" -- literal weaponized bureaucracy
- Ink mixing in the center of explosions (creating muddy brown) symbolizes how both sides blend together
