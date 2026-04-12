# Martelao da Censura -- Sprite Specification

**Weapon ID:** 11
**Boss:** Xandao (Alexandre de Moraes)
**Type:** Melee / Shockwave (Giant Gavel)
**Category:** Boss Exclusive

---

## 1. Weapon Sprite (Held)

**Dimensions:** 48x48 px
**Anchor point:** Bottom-center (24, 44)

### Color Palette

| Name                | Hex       | Usage                                  |
|---------------------|-----------|----------------------------------------|
| Wood Dark           | `#4A2F1A` | Gavel handle deep shadow               |
| Wood Main           | `#7B5B3A` | Gavel handle primary                   |
| Wood Light          | `#A67C52` | Gavel handle highlight                 |
| Wood Grain          | `#5C3D22` | Handle grain texture lines             |
| Head Dark           | `#2C1A0E` | Gavel head deep shadow                 |
| Head Main           | `#5C3A1E` | Gavel head primary (darker wood)       |
| Head Light          | `#8B6340` | Gavel head highlight                   |
| Metal Band          | `#C0C0C0` | Iron bands on gavel head               |
| Metal Band Dark     | `#808080` | Iron band shadow                       |
| Censura Red         | `#CC0000` | "CENSURADO" text inscription           |
| Censura Red Dark    | `#8B0000` | "CENSURADO" shadow                     |
| Shockwave Blue      | `#3366CC` | Judicial shockwave energy              |
| Shockwave Light     | `#6699FF` | Shockwave highlight                    |
| Shockwave White     | `#CCDDFF` | Shockwave core flash                   |
| STF Gold            | `#B8860B` | STF (Supreme Court) emblem on head     |
| Black Outline       | `#1A1A1A` | Thick outlines                         |
| Stamp Red           | `#CC0000` | "INQUERITO INSTAURADO" stamp           |
| Paper White         | `#FFFFFF` | Stamp background                       |

### Frame Descriptions

#### Frame 1 -- Static / Inventory
- ABSURDLY MASSIVE judge's gavel, the size of a light pole
- Viewed top-down: long wooden handle running vertically (takes ~70% of sprite height)
- Gavel head at top: rectangular block of dark heavy wood
- Iron bands wrapping gavel head (2 bands, top and bottom edges)
- "CENSURADO" inscribed in RED capital letters across the gavel head face
  - Letters are rough-carved, not elegant -- like branded/burnt into wood
- Small gold STF emblem on the handle near the head (scales of justice icon, tiny)
- Handle has visible wood grain texture (dark lines running along length)
- Bottom of handle has a rubber grip (dark grey, textured dots)
- The gavel RADIATES authority -- disproportionately large, intimidating
- Thick black outlines (3px), heavy shadows on right side
- Faint blue judicial aura around the head (1-2px glow)

#### Frame 2 -- Idle Glow A
- Same as Frame 1
- Blue judicial aura PULSES brighter on LEFT side of head (3px glow)
- "CENSURADO" text glows slightly (redder, more vivid)
- Small blue energy crackle on one iron band (2px spark)

#### Frame 3 -- Idle Glow B
- Same as Frame 1
- Blue judicial aura PULSES brighter on RIGHT side of head
- "CENSURADO" text dims slightly
- Blue energy crackle on other iron band
- Handle grain shimmers (subtle light wave along wood)

---

## 2. Swing / Strike Animation

**Dimensions:** 48x48 px per frame
**Frames:** 4
**Sprite sheet:** 192x48 px

#### Frame 1 -- Raise
- Gavel raised HIGH (shifted 8px up, rotated 30 degrees back)
- Blue energy gathering at head (4-6 small blue particles swirling toward head)
- "CENSURADO" text glowing BRIGHT red (anticipation)
- Shadow on ground grows larger (gavel is UP, shadow extends)
- Motion lines suggest upward force (2 black lines below)

#### Frame 2 -- Apex Hold
- Gavel at highest point (top of frame, nearly leaving bounds)
- Head surrounded by concentrated blue energy cloud (10px aura)
- Iron bands crackling with blue-white electricity
- "CENSURADO" text now BLAZING (white-hot red center)
- Brief pause frame (slightly longer duration for dramatic tension)
- Xandao's silhouetted hand visible at grip (grotesque, authoritarian grip)

#### Frame 3 -- Downswing
- Gavel SLAMMING down with tremendous force
- Extreme motion blur on head (stretched vertically, 6px blur)
- Blue energy trailing behind like comet tail
- Speed lines: 5-6 bold black diagonal lines
- "CENSURADO" text now a red streak
- Air displacement visual: compressed air ring ahead of gavel (white semi-circle)

#### Frame 4 -- Impact
- Gavel head SMASHED into ground (at bottom of frame)
- Head partially sunk into surface (2px below ground line)
- MASSIVE impact: radial crack pattern on ground from impact point
  - 6-8 cracks radiating outward (dark lines)
- Blue shockwave ERUPTS from impact (see shockwave section)
- Debris flying: wood splinters, ground chunks, dust
- "CENSURADO" text visible on embedded gavel head
- Flash: bright white at impact center

---

## 3. Shockwave (Area Effect)

**Dimensions:** 96x96 px per frame (EXTRA LARGE for shockwave coverage)
**Frames:** 4
**Sprite sheet:** 384x96 px

#### Frame 1 -- Shockwave Birth
- Central impact point: white-blue flash (8px radius)
- First ring of blue judicial energy expanding (16px radius)
  - Ring: 2px thick, blue `#3366CC` with white `#CCDDFF` inner edge
- Ground cracks visible at center (dark lines)
- Small debris particles launched upward (4-5 grey/brown specs)
- Compressed air distortion (slight pixel displacement at ring edge)

#### Frame 2 -- Shockwave Expansion
- Ring now at 32px radius and expanding
- Ring color shifting: blue outer edge, white-blue inner
- Second inner ring forming (16px radius, thinner)
- Text fragments appearing in the shockwave: tiny "CENSURADO" echoes
- Blue energy wisps trailing the expanding ring (8-10 particles following ring edge)
- Ground dust cloud rising at center (grey-brown, 12px)

#### Frame 3 -- Maximum Range
- Primary ring at 44px radius (nearly filling 96px frame)
- Ring now more transparent (alpha 0.6, fading)
- Second ring at 32px radius
- Third faint ring at 20px radius
- All rings have "judicial electricity" crackling along them (small white zigzag lines)
- Central area: dust settling, crack pattern fully formed
- "CENSURADO" echo texts now at various distances, fading

#### Frame 4 -- Dissipation
- All rings fading to very faint (alpha 0.2)
- Expanding beyond frame edges
- Residual blue motes floating (5-6 tiny blue dots drifting)
- Ground cracks remain visible
- Dust cloud nearly settled
- Final "authority echo" -- faintest ring barely visible

---

## 4. "INQUERITO INSTAURADO" Stamp (On-Hit Effect)

**Dimensions:** 48x32 px
**Frames:** 3
**Sprite sheet:** 144x32 px

#### Frame 1 -- Stamp Appear
- Giant red official stamp SLAMS onto enemy position
- White rectangular border (44x28px)
- Red text inside: "INQUERITO" top line, "INSTAURADO" bottom line
- Text style: official bureaucratic capitals, bold serif
- Angle: -8 degrees (classic stamp tilt)
- Impact: slight downward overshoot (appears 2px below final position)
- Red ink splatter at corners from stamp force (4 small red dots)

#### Frame 2 -- Stamp Hold
- Stamp settled at final position (overlaying enemy sprite)
- Text BOLD and clear: "INQUERITO INSTAURADO"
- Red ink is vivid
- Small shock stars around stamp (3-4 tiny 2px stars, yellow)
- Enemy beneath is implied to be "officially silenced"

#### Frame 3 -- Stamp Fade
- Stamp begins dissolving
- Text fragmenting (letters separating slightly)
- Red ink fading
- Border becoming dashed/broken
- Alpha reducing from 1.0 to 0.3
- Final bureaucratic dust particles rising

---

## 5. Silence Effect (On Enemies Hit by Shockwave)

**Dimensions:** 24x24 px per frame
**Frames:** 2 (loop for silence duration)
**Sprite sheet:** 48x24 px

#### Frame 1 -- Mute Icon A
- Classic "muted speaker" icon over enemy head
- Blue circle with diagonal line through it (prohibition symbol)
- Inside: small speaker/megaphone silhouette
- Color: `#3366CC` (blue, judicial)
- Small blue particles drifting from icon (silenced energy)

#### Frame 2 -- Mute Icon B
- Same icon, but PULSING larger (scale 1.1x)
- Line through speaker is BOLDER
- Blue particles at different positions
- Faint "X" marks around icon (emphasis)

---

## Notes

- Xandao (Alexandre de Moraes) is the STF minister known for judicial activism and censorship orders
- The gavel being "the size of a light pole" must be taken literally in boss scale -- it should dwarf Xandao's own sprite
- "CENSURADO" (censored) and "INQUERITO INSTAURADO" (investigation opened) are his signature judicial moves
- The shockwave "silences" enemies -- gameplay mechanic disables enemy attacks for X seconds
- The blue color scheme represents judicial/legal authority (not political red or green)
- The stamp appearing on enemies is both a visual effect and a comedic political commentary
- Shockwave at 96x96 is intentionally larger than standard weapon effects -- this is a BOSS weapon
- Iron bands on the gavel add a medieval/authoritarian feel
- The STF gold emblem is small but important for identifying the weapon's origin
- Wood grain texture should look heavy and dense -- this is old-growth judicial timber
- The "silence" mechanic mute icon uses a modern/digital "muted" aesthetic contrasted against the medieval gavel -- intentional anachronism matching Moraes' use of tech-era censorship
