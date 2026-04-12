# Power-Ups — Sprite Specification

> "Zumbis de Brasilia" | 6 Power-Up Items
> Estilo: Robert Crumb + Andre Guedes + horror B-movie brasileiro
> Perspectiva: top-down levemente isometrica (Y-sorting)
> REGRA: Todas as cores sao "sujas" — NUNCA use cores puras

---

## General Rules

- **Item Sprite Dimensions:** 16x16px (healing items, santinho) or 24x24px (timed power-ups)
- **Sprite Sheet Layout:** Horizontal strip, 1 row per item
- **Format:** PNG with alpha transparency
- **Outline Style:** Thick uneven outlines (1-2px at 16x16, 2px at 24x24), `#1A1A18`
- **Glow:** All items on the ground have a subtle radial glow behind them (item-specific color, 30-40% opacity, 2px larger than sprite)
- **Pulse:** Idle frames alternate scale 100% <-> 105% to create a "breathing" pulse
- **Paper Texture Overlay:** Gaussian noise, monochromatic, 3-5% opacity on every frame
- **Anchor Point:** Bottom-center of each frame

### Frame Layout per Item

Each power-up sprite sheet contains **7 frames**:

| Frame | Name           | Purpose                                       |
|-------|----------------|-----------------------------------------------|
| 0     | idle_pulse_1   | Ground state A (normal size)                  |
| 1     | idle_pulse_2   | Ground state B (slightly larger, brighter)    |
| 2     | pickup_flash_1 | White flash engulfs item                      |
| 3     | pickup_flash_2 | Item dissolves into particles                 |
| 4     | pickup_flash_3 | Particles scatter, frame nearly empty         |
| 5     | active_effect_1| Active aura/overlay frame A (timed items)     |
| 6     | active_effect_2| Active aura/overlay frame B (timed items)     |

> Frames 5-6 are only used by **Cracha VIP** and **Emenda Pix**. For healing items and santinho, frames 5-6 are blank (fully transparent).

---

## 1. Cafe (Copinho de Cafe) — Small Heal

- **Sprite Dimensions:** 16x16px
- **Sprite Sheet Size:** 112x16px (7 frames)
- **Phaser Key:** `powerup_cafe`
- **Gameplay:** Heals 15% HP | Very Common spawn

### Color Palette

| Element              | Hex Code  | Usage                              |
|----------------------|-----------|------------------------------------|
| Cup White            | `#E8E0D0` | Plastic cup body (dirty white)     |
| Cup Shadow           | `#B8B0A0` | Cup underside / fold shadow        |
| Cup Rim              | `#D0C8B8` | Lip of the cup, slightly darker    |
| Coffee Brown         | `#4A2810` | Dark coffee liquid surface         |
| Coffee Highlight     | `#6B3A1A` | Coffee meniscus / light reflection |
| Steam White          | `#F0E8D8` | Rising steam wisps, 50% opacity    |
| Steam Fade           | `#F0E8D8` | Steam upper portion, 20% opacity   |
| Glow Warm            | `#D47820` | Ground glow behind item, 35% alpha |
| Outline Black        | `#1A1A18` | Thick irregular outlines           |
| Flash White          | `#FFFFF0` | Pickup flash, 90% opacity          |
| Particle Brown       | `#6B3A1A` | Pickup dissolve particles          |

### Frame Descriptions

#### Frame 0: idle_pulse_1 (0,0 to 15,15)
Tiny disposable plastic coffee cup seen from slightly above. Cup is a truncated cone shape, wider at top (~8px) than bottom (~5px). Dark coffee visible inside with a single-pixel highlight dot on the liquid surface. Faint scuff marks on the cup (1px darker pixels). A single wisp of steam (2-3px tall, 1px wide, wavy) rises from the coffee, rendered at 50% opacity. Subtle warm glow (`#D47820` at 35% alpha) radiates 2px outward from the base. Thick uneven black outline. The cup looks cheap, disposable, slightly crumpled -- congressional vending machine quality.

#### Frame 1: idle_pulse_2 (16,0 to 31,15)
Same cup but scaled to ~105% (1px larger footprint in each dimension effectively). Coffee highlight pixel shifts 1px. Steam wisp is in a different position (shifted or second wisp shape). Glow radius increases by 1px and brightens to 45% alpha. This frame alternates with Frame 0 to create the pulsing "pick me up" effect.

#### Frame 2: pickup_flash_1 (32,0 to 47,15)
Cup still visible but engulfed in a bright warm-white flash (`#FFFFF0` at 90% opacity). The flash is a 12x12px soft circle centered on the cup. Cup outlines barely visible through the flash. Steam disappears. A thin warm ring (`#D47820`) appears at the flash edge.

#### Frame 3: pickup_flash_2 (48,0 to 63,15)
Cup silhouette breaking apart into 4-5 small brown particles (2x2px and 1x1px). Flash circle shrinks to 8x8px but intensifies. Particles begin moving outward (1-2px from center). A "+" shape (3x3px, `#C83030` HP red) flickers in the center, hinting at the heal.

#### Frame 4: pickup_flash_3 (64,0 to 79,15)
Particles scattered to edges of the frame (6-7px from center), fading to 40% opacity. Flash reduced to a 4x4px warm dot, nearly gone. One or two particles have left the frame. Frame is mostly transparent -- item is consumed.

#### Frames 5-6: (blank / transparent)
Not applicable -- Cafe is a heal item with no active duration effect.

---

## 2. Coxinha — Medium Heal

- **Sprite Dimensions:** 16x16px
- **Sprite Sheet Size:** 112x16px (7 frames)
- **Phaser Key:** `powerup_coxinha`
- **Gameplay:** Heals 35% HP | Moderate spawn

### Color Palette

| Element              | Hex Code  | Usage                              |
|----------------------|-----------|------------------------------------|
| Crust Golden         | `#C8952A` | Main breaded exterior              |
| Crust Highlight      | `#D4A840` | Top highlights, crispy ridges      |
| Crust Dark           | `#8B6518` | Bottom shadow, crease              |
| Oil Sheen            | `#E0C060` | Oil glistening dots, 60% opacity   |
| Interior Cream       | `#E8D8A0` | Exposed filling at the seam        |
| Tip Dark             | `#6B4A10` | Pointed tip shadow                 |
| Glow Gold            | `#D4A840` | Ground glow, 35% alpha             |
| Outline Black        | `#1A1A18` | Thick irregular outlines           |
| Flash White          | `#FFFFF0` | Pickup flash                       |
| Particle Gold        | `#C8952A` | Breadcrumb dissolve particles      |

### Frame Descriptions

#### Frame 0: idle_pulse_1 (0,0 to 15,15)
Classic coxinha shape from above: a fat teardrop/cone, pointed end angled slightly toward camera. The breaded shell is golden-brown with 2-3 lighter pixels suggesting crispy ridges. A visible seam runs down one side where the dough was pinched (1px darker line). 1-2 oil sheen pixels (bright golden, 60% opacity) glint on the top surface. The pointed tip is slightly darker. Drop shadow (2px, 40% opacity black) beneath. Thick black outlines, deliberately lumpy. The coxinha should look greasy, overstuffed, irresistible. Warm golden glow behind (`#D4A840` at 35%).

#### Frame 1: idle_pulse_2 (16,0 to 31,15)
Coxinha at 105% scale. Oil sheen pixels shift position (simulates glistening under light). Glow brightens to 45%. One additional oil pixel appears. The crust highlight area is 1px larger. Creates an appetizing pulse effect.

#### Frame 2: pickup_flash_1 (32,0 to 47,15)
Coxinha engulfed in warm golden-white flash. Flash circle 12x12px centered. Coxinha outline barely visible. A tiny oil droplet (1px) flings outward from the flash.

#### Frame 3: pickup_flash_2 (48,0 to 63,15)
Coxinha shatters into 5-6 breadcrumb particles (2x2px golden, 1x1px dark golden). Flash shrinks to 8x8px. A "+" shape (`#C83030`, 3x3px) appears at center. Crumbs scatter outward 2-3px from center.

#### Frame 4: pickup_flash_3 (64,0 to 79,15)
Breadcrumb particles at frame edges, fading. Flash down to a 3x3px warm glow. Most of the frame is transparent. One large crumb (2x2px) lingers near center at 50% opacity.

#### Frames 5-6: (blank / transparent)
Not applicable -- Coxinha is a heal item.

---

## 3. Picanha — Large Heal

- **Sprite Dimensions:** 16x16px
- **Sprite Sheet Size:** 112x16px (7 frames)
- **Phaser Key:** `powerup_picanha`
- **Gameplay:** Heals 60% HP | Rare spawn

### Color Palette

| Element              | Hex Code  | Usage                              |
|----------------------|-----------|------------------------------------|
| Meat Red             | `#8B2020` | Main steak body, raw-red center    |
| Meat Seared          | `#5A1A0A` | Seared crust edges                 |
| Fat Cap White        | `#E0D0B0` | Picanha fat strip on one side      |
| Fat Highlight        | `#F0E0C0` | Fat cap light reflection           |
| Grill Marks          | `#2D0A0A` | Dark charred lines across meat     |
| Juice Pink           | `#CC4040` | Juice pooling beneath, 40% alpha   |
| Board Wood           | `#6B4423` | Wooden serving board beneath       |
| Board Dark           | `#4A2E15` | Board shadow / grain lines         |
| Steam White          | `#F0E8D8` | Sizzle steam, 40-50% opacity       |
| Glow Red             | `#CC4040` | Ground glow, 40% alpha             |
| Outline Black        | `#1A1A18` | Thick outlines                     |
| Flash White          | `#FFFFF0` | Pickup flash                       |
| Particle Meat        | `#8B2020` | Dissolve particles                 |

### Frame Descriptions

#### Frame 0: idle_pulse_1 (0,0 to 15,15)
A thick slab of picanha steak sitting on a small wooden board (board is ~12x8px, forming the base). The steak is roughly 8x6px, irregular edges. A distinctive fat cap (2px wide white strip) runs along one edge -- the signature of picanha. Two thin grill marks (1px dark lines, diagonal) cross the meat surface. The center of the meat is redder (rare), the edges darker (seared). 1-2 juice pixels (pink, 40% opacity) pool at the board edges. A single steam wisp (2px tall) rises from the steak. Red glow beneath (`#CC4040` at 40%). Thick black outlines on everything. The board has 1-2 wood grain lines (1px). This steak looks ABSURDLY juicy and thick for its size -- political satire excess.

#### Frame 1: idle_pulse_2 (16,0 to 31,15)
Steak at 105% apparent size. Steam wisp shifts position or a second shorter wisp appears. Juice pool pixels shift slightly (sizzling effect). Fat cap gets an additional highlight pixel. Glow radius increases 1px, brightens to 50% alpha. The meat seems to THROB with juiciness.

#### Frame 2: pickup_flash_1 (32,0 to 47,15)
Steak and board engulfed in reddish-white flash (mix of `#FFFFF0` and `#CC4040`, warm). Flash 14x14px -- larger than other items because this is a RARE, POWERFUL pickup. Steam explodes outward. Board outline barely visible.

#### Frame 3: pickup_flash_2 (48,0 to 63,15)
Steak fragments into 6-7 particles (mix of meat-red 2x2px, fat-white 1x1px, and wood-brown 1x1px). Large "+" symbol (`#C83030`, 5x5px) in center -- bigger than other heals to signal major recovery. Flash shrinks to 10x10px.

#### Frame 4: pickup_flash_3 (64,0 to 79,15)
Particles scattered wide. The "+" fades to 30% opacity. A single juice pixel remains at center, then fades. Frame mostly transparent.

#### Frames 5-6: (blank / transparent)
Not applicable -- Picanha is a heal item.

---

## 4. Santinho (Electoral Pamphlet) — Score Boost

- **Sprite Dimensions:** 16x16px
- **Sprite Sheet Size:** 112x16px (7 frames)
- **Phaser Key:** `powerup_santinho`
- **Gameplay:** +500 Score on pickup | Common spawn

### Color Palette

| Element              | Hex Code  | Usage                              |
|----------------------|-----------|------------------------------------|
| Paper Base           | `#F0E8D0` | Pamphlet body (matches tile palette)|
| Paper Shadow         | `#D0C8A8` | Folded edge shadow                 |
| Paper Crease         | `#C0B898` | Fold line / crumple mark           |
| Print Red            | `#CC3030` | Generic politician photo tint      |
| Print Blue           | `#2A3A5A` | Generic text lines                 |
| Print Number         | `#1A1A18` | Bold candidate number              |
| Glow Yellow          | `#F0C830` | Score-associated glow, 40% alpha   |
| Sparkle White        | `#FFFFF0` | Floating sparkle particles         |
| Outline Black        | `#1A1A18` | Outlines                           |
| Flash Yellow         | `#F0C830` | Pickup flash (score = gold/yellow) |
| Particle Paper       | `#F0E8D0` | Confetti dissolve particles        |

### Frame Descriptions

#### Frame 0: idle_pulse_1 (0,0 to 15,15)
A small rectangular electoral pamphlet (santinho), roughly 10x12px, slightly crumpled and angled ~15deg on the ground. The pamphlet has a generic caricature face (3x3px, pink/red blob with two dot eyes -- deliberately unrecognizable, NO real politician). Below the face, 1-2 lines of "text" (1px blue horizontal dashes). A bold 2-digit number at the bottom (2x3px, black, illegible at this size but suggesting a candidate number). One corner is folded. Paper is cream/off-white, dirty. A sparkle particle (1px white, diamond shape) floats 2px above the pamphlet, rotating. Yellow score-glow behind (`#F0C830` at 40%). The pamphlet gently hovers 1px above the ground (tiny shadow beneath).

#### Frame 1: idle_pulse_2 (16,0 to 31,15)
Pamphlet at 105% with sparkle particle in a different position (shifted 2px, or second sparkle appears). Glow intensifies to 50%. The pamphlet tilts 1px in the opposite direction (subtle floating wobble). The folded corner unfolds 1px -- like it is breathing.

#### Frame 2: pickup_flash_1 (32,0 to 47,15)
Pamphlet engulfed in bright golden-yellow flash (`#F0C830`). Flash 12x12px. The text "+500" begins to form in the flash center (bold, 1px outline, yellow on white).

#### Frame 3: pickup_flash_2 (48,0 to 63,15)
Pamphlet tears into 6-8 confetti particles (small paper-colored rectangles, 1x2px and 2x1px, mixed cream and colored). "+500" text fully visible and bold in the center (this gets read by the score HUD system). Flash shrinks to 8x8px. Confetti scatters outward with rotation.

#### Frame 4: pickup_flash_3 (64,0 to 79,15)
Confetti at frame edges, some leaving. "+500" fades to 40% opacity. Flash down to 3x3px warm dot. Frame nearly clear. A final sparkle pixel winks out.

#### Frames 5-6: (blank / transparent)
Not applicable -- Santinho is an instant effect, no active duration.

---

## 5. Cracha VIP (Government VIP Badge) — Temporary Invulnerability

- **Sprite Dimensions:** 24x24px (larger: timed power-up with active effect)
- **Sprite Sheet Size:** 168x24px (7 frames)
- **Phaser Key:** `powerup_cracha_vip`
- **Gameplay:** 5 seconds invulnerability | Rare spawn

### Color Palette

| Element              | Hex Code  | Usage                              |
|----------------------|-----------|------------------------------------|
| Badge Gold           | `#C8A832` | Badge body, metallic               |
| Badge Dark Gold      | `#8B7520` | Badge shadow, engraved lines       |
| Badge Highlight      | `#E0C850` | Bright specular highlight          |
| Lanyard Red          | `#CC3030` | Neck lanyard strap                 |
| Lanyard Dark         | `#8B1A1A` | Lanyard shadow                     |
| Photo Gray           | `#8A8580` | Generic ID photo area              |
| Photo Face           | `#A0785A` | Tiny face blob in photo            |
| Text Line            | `#1A1A18` | "VIP" text and fake name lines     |
| Shield Blue          | `#2E86C1` | Invulnerability shield aura        |
| Shield Light         | `#5DADE2` | Shield highlight / pulse           |
| Glow Gold            | `#E0C850` | Ground glow, 45% alpha             |
| Outline Black        | `#1A1A18` | Thick outlines                     |
| Flash Gold           | `#E0C850` | Pickup flash                       |
| Star Sparkle         | `#FFFFF0` | Prestige sparkle particles         |

### Frame Descriptions

#### Frame 0: idle_pulse_1 (0,0 to 23,23)
A government VIP badge/credential seen from above. Rectangular golden badge (~14x18px) with a red lanyard strap extending from the top (folded, suggesting it hangs from a neck). The badge face has: a tiny photo area (4x4px gray with a 2x2px face blob), the letters "VIP" in bold black (hand-lettered, uneven), and 2 lines of fake text beneath (1px dashes). The badge has a metallic sheen -- 2-3 bright gold highlight pixels on the upper edge. A clip or pin at the top (2px metallic). The whole badge is encircled by a faint golden glow (`#E0C850` at 45% alpha, 3px radius beyond badge). A single star sparkle (cross shape, 3x3px white) floats near the top-right corner. Thick outlines, slightly wobbly. The badge radiates PRIVILEGE and POWER.

#### Frame 1: idle_pulse_2 (24,0 to 47,23)
Badge at 105%. Highlight pixels shift (metallic shimmer). Sparkle moves to top-left (rotating around the badge). Glow intensifies to 55%. The lanyard sways 1px to the side. A second smaller sparkle appears opposite the first. The badge DEMANDS to be picked up.

#### Frame 2: pickup_flash_1 (48,0 to 71,23)
Badge engulfed in golden flash (`#E0C850` at 90%). Flash circle 20x20px. A shield outline (blue, `#2E86C1`) begins to form around the flash -- hexagonal or circular, 1px thick. Lanyard disappears into the flash.

#### Frame 3: pickup_flash_2 (72,0 to 95,23)
Badge shatters into 5-6 golden particles and 2 red lanyard fragments. The shield outline solidifies and pulses outward (expanding ring, 2px thick blue). A bold shield icon (8x8px, blue with gold trim) appears at center. Star sparkles (3-4) radiate outward.

#### Frame 4: pickup_flash_3 (96,0 to 119,23)
Particles scattered. Shield ring has expanded to frame edges and fades. The shield icon shrinks and fades. Frame mostly transparent. This transitions to the active effect being applied to the PLAYER sprite.

#### Frame 5: active_effect_1 (120,0 to 143,23)
**Player overlay frame.** A golden-blue shield aura to be composited over the player sprite. Concentric shield ring (outer: `#C8A832` gold 2px, inner: `#2E86C1` blue 1px). The ring is roughly 20x20px, centered. Small star sparkles (2-3, 1px white) at cardinal points on the ring. Inside the ring is transparent (player shows through). Faint blue tint wash over the entire frame at 10% opacity (gives player a "shielded" look).

#### Frame 6: active_effect_2 (144,0 to 167,23)
Same shield aura but ring has expanded 1px outward and the gold/blue colors swap intensity (blue becomes brighter, gold dims slightly). Sparkles rotate to intercardinal points. The 10% tint shifts to gold. Alternating frames 5-6 creates a shimmering invulnerability aura around the player. When the 5-second duration nears end (last 1.5s), these frames should play at DOUBLE speed (flicker warning).

---

## 6. Emenda Pix (Pix Transfer Icon) — Score Multiplier

- **Sprite Dimensions:** 24x24px (larger: timed power-up with active effect)
- **Sprite Sheet Size:** 168x24px (7 frames)
- **Phaser Key:** `powerup_emenda_pix`
- **Gameplay:** 2x Score Multiplier for 10 seconds | Moderate spawn

### Color Palette

| Element              | Hex Code  | Usage                              |
|----------------------|-----------|------------------------------------|
| Pix Green            | `#4A7C59` | Main icon body (matches gas palette)|
| Pix Light Green      | `#5A9A6A` | Highlights, inner glow             |
| Pix Dark Green       | `#3D6B3A` | Shadow side, depth                 |
| Diamond Shape        | `#5A9A6A` | Pix logo diamond rotated 45deg    |
| Arrow White          | `#E8E0D0` | Transfer arrows inside diamond     |
| Multiplier Yellow    | `#F0C830` | "2x" text overlay                  |
| Multiplier Outline   | `#8B6518` | "2x" text dark outline             |
| Trail Green          | `#4A7C59` | Particle trail, 40-60% opacity     |
| Trail Bright         | `#5A9A6A` | Trail highlight particles          |
| Glow Green           | `#4A7C59` | Ground glow, 40% alpha             |
| Outline Black        | `#1A1A18` | Thick outlines                     |
| Flash Green          | `#5A9A6A` | Pickup flash                       |
| Corrupt Gold         | `#C8A832` | Corruption sparkle accents         |

### Frame Descriptions

#### Frame 0: idle_pulse_1 (0,0 to 23,23)
The Pix logo -- a diamond (square rotated 45deg, ~12x12px) in sickly green, with two small arrows inside (one pointing up-right, one pointing down-left, each 3px, dirty white). The diamond floats above a faint shadow. Around the diamond, a green glow (`#4A7C59` at 40% alpha) pulses outward 3px. Bold "2x" text in yellow (`#F0C830`) with dark outline sits at the bottom-right corner of the frame, partially overlapping the glow (text is ~6x5px). 1-2 small green particles (1px, `#5A9A6A`, 60% opacity) drift lazily around the diamond like corrupted data. A single gold sparkle (`#C8A832`, 1px) at the top suggests dirty money. Thick wobbly black outlines on the diamond. The whole thing looks like a CORRUPTED financial transaction given form.

#### Frame 1: idle_pulse_2 (24,0 to 47,23)
Diamond at 105%, arrows inside have swapped direction (or rotated 90deg -- simulates a looping transfer). Green glow expands 1px and brightens to 50%. "2x" text pulses brighter (highlight yellow). Green particles shift position. Gold sparkle moves. The diamond subtly rotates 2-3deg. Creates a hypnotic, greedy pulse.

#### Frame 2: pickup_flash_1 (48,0 to 71,23)
Diamond engulfed in bright green flash (`#5A9A6A` at 85%). Flash 18x18px. The "2x" text scales up and becomes the dominant element in the flash, now centered and 8x7px. Green particle ring forms at flash edge.

#### Frame 3: pickup_flash_2 (72,0 to 95,23)
Diamond explodes into 6-8 green particles (mixed sizes: 2x2 and 1x1, various green shades). "2x" text at maximum size (10x8px), bold, yellow with green outline -- this is the moment the player KNOWS what they got. The arrows from inside the diamond become standalone particles flying outward. Green flash shrinks to 12x12px.

#### Frame 4: pickup_flash_3 (96,0 to 119,23)
Green particles scattered to edges, trailing green wisps (1px lines, 30% opacity). "2x" fades to 50% opacity and shrinks. Flash down to 6x6px. A green particle trail begins to form downward (previewing the active trail effect).

#### Frame 5: active_effect_1 (120,0 to 143,23)
**Player overlay frame.** A green particle trail/aura to composite behind/around the player. Frame shows: a ring of 6-8 green particles (mixed `#4A7C59` and `#5A9A6A`, 60-80% opacity) orbiting at ~10px radius from center. "2x" text floating above center (6x5px, yellow, 70% opacity) -- this text follows the player during the active period. 2-3 green trail wisps (2-3px lines) extend downward from center, suggesting a particle trail behind movement. A faint green tint (8% opacity) washes the frame.

#### Frame 6: active_effect_2 (144,0 to 167,23)
Orbiting particles have rotated ~30deg from Frame 5 positions. "2x" text bobs 1px upward. Trail wisps shift to slightly different angles. Green tint alternates to 12% opacity. The trail particles are in new positions, creating the sense of continuous motion when frames alternate. During the last 2 seconds of the 10-second duration, these frames play at TRIPLE speed (frantic flicker warning -- money is running out).

---

## Sprite Sheet Summary — All Items

| Item          | Key                    | Frame Size | Sheet Size | Frames | Rarity    |
|---------------|------------------------|------------|------------|--------|-----------|
| Cafe          | `powerup_cafe`         | 16x16      | 112x16     | 7      | Very Common |
| Coxinha       | `powerup_coxinha`      | 16x16      | 112x16     | 7      | Moderate  |
| Picanha       | `powerup_picanha`      | 16x16      | 112x16     | 7      | Rare      |
| Santinho      | `powerup_santinho`     | 16x16      | 112x16     | 7      | Common    |
| Cracha VIP    | `powerup_cracha_vip`   | 24x24      | 168x24     | 7      | Rare      |
| Emenda Pix    | `powerup_emenda_pix`   | 24x24      | 168x24     | 7      | Moderate  |

## Phaser 3 Atlas Config

```javascript
// 16x16 items
['powerup_cafe', 'powerup_coxinha', 'powerup_picanha', 'powerup_santinho'].forEach(key => {
  this.load.spritesheet(key, `assets/armas/powerups/sprites/${key}.png`, {
    frameWidth: 16,
    frameHeight: 16
  });
});

// 24x24 items
['powerup_cracha_vip', 'powerup_emenda_pix'].forEach(key => {
  this.load.spritesheet(key, `assets/armas/powerups/sprites/${key}.png`, {
    frameWidth: 24,
    frameHeight: 24
  });
});
```

## Notes for Artist

- Every item must have a DISTINCT SILHOUETTE recognizable at 16x16. Cup = tall, Coxinha = teardrop, Picanha = wide rectangle, Santinho = tilted paper, Badge = rectangle+lanyard, Diamond = rotated square.
- Colors are DIRTY -- never pure green, never pure gold. Mix in gray/brown per the global color palette rules.
- Outlines are THICK and UNEVEN. Hand-drawn feel. Micro-variations simulating human hand.
- Glow/pulse must be VISIBLE against all ground tile types (concrete, grass, asphalt). Test on dark AND light backgrounds.
- Healing items have WARM glows (orange, gold, red). Score items have YELLOW glows. Timed power-ups have their THEMATIC color glow.
- The pickup flash must feel like a REWARD -- brief but intense, satisfying.
- Paper texture overlay (Gaussian noise, 3-5%) on every single frame. Remove any digital cleanliness.
- These items exist in a world of rotting congressional cafeteria food, corrupt government badges, and worthless electoral promises. They should look APPETIZING but also slightly GROTESQUE.
