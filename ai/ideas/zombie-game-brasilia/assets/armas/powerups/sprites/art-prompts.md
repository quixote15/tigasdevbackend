# Power-Ups — Art Generation Prompts

> Prompts for Stable Diffusion / DALL-E / Midjourney to generate base art for each power-up.
> After generation, the output must be:
> 1. Downscaled to target pixel dimensions (16x16 or 24x24)
> 2. Manually pixel-edited to add thick outlines, fix silhouette clarity
> 3. Paper texture overlay applied (Gaussian noise 3-5%)
> 4. Split into individual frames per the sprite-spec.md

---

## Global Style Suffix (append to ALL prompts)

```
underground comix art style, Robert Crumb inspired, thick uneven ink outlines,
grotesque caricature, dirty saturated colors mixed with gray-brown, low-fi
pixel art, top-down isometric view from slightly above, horror B-movie aesthetic,
Brazilian political satire, hand-drawn imperfect lines, cross-hatching shadows,
cheap offset print texture, 1970s underground magazine, dark humor,
transparent PNG background, single isolated object, no text unless specified
```

---

## 1. Cafe (Copinho de Cafe)

### Stable Diffusion / SDXL

```
a tiny disposable white plastic coffee cup from a vending machine, seen from
above at a slight angle, top-down perspective, the cup is a small truncated cone
shape with dark brown coffee visible inside, thin wisps of steam rising from the
hot coffee, the plastic cup looks cheap and slightly crumpled with scuff marks,
congressional cafeteria vending machine quality, warm brown and dirty white color
palette, coffee is very dark almost black-brown, steam is translucent white wisps,
subtle warm orange glow emanating from beneath the cup, isolated object on
transparent background, (underground comix art style:1.3), (Robert Crumb
inspired:1.2), thick uneven ink outlines, grotesque detailed, dirty saturated
colors, pixel art, Brazilian political humor, hand-drawn imperfect lines,
cross-hatching shadows
```

**Negative prompt:**
```
clean digital art, smooth gradients, 3D render, photorealistic, anime,
cartoon cute style, bright pure colors, thin lines, symmetric, perfect,
polished, text, watermark, signature
```

### DALL-E 3

```
Top-down view of a tiny disposable white plastic coffee cup from a cheap vending
machine, in the art style of Robert Crumb's underground comix. The cup is
slightly crumpled and dirty, with dark brown coffee inside and thin steam wisps
rising. Thick uneven black ink outlines, cross-hatching shadows, dirty muted
color palette (browns, dirty whites). The style should look like a hand-drawn
illustration from a 1970s underground Brazilian political comic magazine.
Isolated on transparent background, slight isometric angle from above.
```

### Midjourney v6

```
/imagine tiny disposable plastic coffee cup from a vending machine, dark coffee
inside with steam rising, seen from above top-down isometric, Robert Crumb
underground comix art style, thick uneven ink outlines, dirty muted browns and
whites, cross-hatching shadows, cheap offset print texture, Brazilian political
satire aesthetic, hand-drawn imperfect, isolated object --no background text
watermark --ar 1:1 --style raw --s 200
```

---

## 2. Coxinha

### Stable Diffusion / SDXL

```
a Brazilian coxinha fried snack seen from above at a slight angle, top-down
perspective, classic teardrop cone shape, golden-brown crispy breaded exterior
with oil glistening on the surface, visible seam where the dough was pinched
shut, the coxinha looks greasy and overstuffed and irresistibly delicious,
cafeteria food from the Brazilian Congress, golden brown color palette with oil
sheen highlights, isolated object on transparent background, (underground comix
art style:1.3), (Robert Crumb inspired:1.2), thick uneven ink outlines,
grotesque detailed, dirty saturated golden colors, pixel art, Brazilian
political humor, hand-drawn imperfect lines, cross-hatching shadows, warm
golden glow beneath
```

**Negative prompt:**
```
clean digital art, smooth gradients, 3D render, photorealistic, anime,
cartoon cute style, bright pure colors, thin lines, symmetric, perfect,
polished, text, watermark, signature, healthy food, salad
```

### DALL-E 3

```
Top-down view of a Brazilian coxinha (teardrop-shaped fried chicken snack) in
the art style of Robert Crumb's underground comix. Golden-brown crispy breading
with visible oil glistening, a pinched seam running down one side, looking
greasy and overstuffed like cafeteria food from the Brazilian Congress. Thick
uneven black ink outlines, cross-hatching shadows, dirty saturated golden-brown
colors. Hand-drawn 1970s underground comic magazine style. Isolated on
transparent background, slight isometric angle from above.
```

### Midjourney v6

```
/imagine Brazilian coxinha fried snack, teardrop shape, golden-brown crispy
breading, oil glistening, seen from above top-down isometric, Robert Crumb
underground comix art style, thick uneven ink outlines, dirty saturated golden
browns, cross-hatching shadows, cheap offset print texture, greasy cafeteria
food, hand-drawn imperfect, isolated object --no background text watermark
--ar 1:1 --style raw --s 200
```

---

## 3. Picanha

### Stable Diffusion / SDXL

```
a thick juicy slab of Brazilian picanha steak on a small wooden cutting board,
seen from above at a slight angle, top-down perspective, the steak has a
distinctive white fat cap along one edge, dark grill marks crossing the red
meat surface, rare in the center with seared dark edges, meat juices pooling
on the wooden board, thin wisps of steam and sizzle rising, the steak is
absurdly thick and juicy, political satire reference to Brazilian politics and
churrasco culture, red and brown color palette with white fat strip, isolated
object on transparent background, (underground comix art style:1.3), (Robert
Crumb inspired:1.2), thick uneven ink outlines, grotesque detailed, dirty
saturated colors, pixel art, Brazilian political humor, hand-drawn imperfect
lines, cross-hatching shadows, warm red glow beneath
```

**Negative prompt:**
```
clean digital art, smooth gradients, 3D render, photorealistic, anime,
cartoon cute style, bright pure colors, thin lines, symmetric, perfect,
polished, text, watermark, signature, vegetarian, salad, plate
```

### DALL-E 3

```
Top-down view of a thick slab of Brazilian picanha steak on a small rustic
wooden board, in the art style of Robert Crumb's underground comix. The steak
has a prominent white fat cap along one edge (signature of picanha), dark
charred grill marks, rare red center with seared dark edges, juices pooling on
the board, steam rising. Absurdly thick and juicy, grotesquely appetizing.
Thick uneven black ink outlines, cross-hatching shadows, dirty saturated reds
and browns. Hand-drawn 1970s underground Brazilian political comic style.
Isolated on transparent background, slight isometric angle from above.
```

### Midjourney v6

```
/imagine thick Brazilian picanha steak on wooden cutting board, white fat cap
strip, grill marks, rare red center, seared edges, juices pooling, steam
rising, seen from above top-down isometric, Robert Crumb underground comix art
style, thick uneven ink outlines, dirty saturated reds browns, cross-hatching
shadows, absurdly juicy, Brazilian political satire, hand-drawn imperfect,
isolated object --no background text watermark --ar 1:1 --style raw --s 200
```

---

## 4. Santinho (Electoral Pamphlet)

### Stable Diffusion / SDXL

```
a crumpled Brazilian electoral campaign pamphlet (santinho) seen from above at
a slight angle, top-down perspective, small rectangular paper flyer slightly
tilted and crumpled, the pamphlet has a generic caricature politician face
printed on it with a bold candidate number below, cheap print quality on
cream-colored paper, one corner is folded, the pamphlet glows with a faint
golden sparkle as if magically charged, electoral propaganda litter from
Brazilian streets, cream and off-white with red and blue print marks, isolated
object on transparent background, (underground comix art style:1.3), (Robert
Crumb inspired:1.2), thick uneven ink outlines, grotesque political caricature,
dirty saturated colors, pixel art, Brazilian political humor, hand-drawn
imperfect lines, golden magical sparkles floating above it
```

**Negative prompt:**
```
clean digital art, smooth gradients, 3D render, photorealistic, anime,
cartoon cute style, bright pure colors, thin lines, symmetric, perfect,
polished, watermark, signature, real politician face, specific party logo,
identifiable candidate
```

### DALL-E 3

```
Top-down view of a crumpled Brazilian electoral campaign pamphlet (santinho)
in the art style of Robert Crumb's underground comix. Small rectangular
cream-colored paper flyer, slightly tilted and crumpled, with a grotesque
generic caricature politician face (not any real person) and a bold candidate
number printed in cheap ink. One corner is folded. Golden magical sparkles
float above it, suggesting it has mystical power. Thick uneven black ink
outlines, cross-hatching shadows, dirty muted cream colors with cheap red and
blue print. Hand-drawn 1970s underground Brazilian political comic style.
Isolated on transparent background, slight isometric angle.
```

### Midjourney v6

```
/imagine crumpled Brazilian electoral pamphlet santinho, cream paper, generic
grotesque politician caricature face, bold candidate number, cheap print quality,
folded corner, golden sparkles floating above, seen from above top-down
isometric, Robert Crumb underground comix art style, thick uneven ink outlines,
dirty muted colors, cross-hatching shadows, Brazilian political satire, magical
glowing item, hand-drawn imperfect, isolated object --no background text
watermark --ar 1:1 --style raw --s 200
```

---

## 5. Cracha VIP (Government VIP Badge)

### Stable Diffusion / SDXL

```
a golden VIP government identification badge with a red neck lanyard, seen from
above at a slight angle, top-down perspective, rectangular metallic golden badge
with a small ID photo area and bold "VIP" text engraved on it, a red fabric
lanyard strap attached at the top with a metal clip, the badge has a prestigious
metallic sheen with specular highlights, it radiates golden authority and corrupt
privilege, Brazilian government bureaucracy aesthetic, gold and red color palette
with metallic highlights, isolated object on transparent background, (underground
comix art style:1.3), (Robert Crumb inspired:1.2), thick uneven ink outlines,
grotesque detailed, dirty saturated golden colors, pixel art, Brazilian political
humor, hand-drawn imperfect lines, cross-hatching shadows, golden aura glow,
star sparkles around it
```

**Negative prompt:**
```
clean digital art, smooth gradients, 3D render, photorealistic, anime,
cartoon cute style, bright pure colors, thin lines, symmetric, perfect,
polished, text, watermark, signature, modern corporate badge, lanyard only
```

### DALL-E 3

```
Top-down view of a golden VIP government identification badge with a red neck
lanyard, in the art style of Robert Crumb's underground comix. Rectangular
metallic golden badge with a tiny ID photo, bold hand-lettered "VIP" text, and
fake credential lines. Red fabric lanyard with metal clip. The badge has corrupt
golden prestige, metallic sheen, star sparkles around it suggesting power and
privilege. Thick uneven black ink outlines, cross-hatching shadows, dirty
saturated golds and reds. Hand-drawn 1970s underground Brazilian political
comic style. Isolated on transparent background, slight isometric angle.
```

### Midjourney v6

```
/imagine golden VIP government ID badge with red neck lanyard, metallic sheen,
tiny ID photo, bold VIP text, metal clip, star sparkles, corrupt golden prestige,
seen from above top-down isometric, Robert Crumb underground comix art style,
thick uneven ink outlines, dirty saturated gold and red, cross-hatching shadows,
Brazilian political satire, authoritative aura, hand-drawn imperfect, isolated
object --no background text watermark --ar 1:1 --style raw --s 200
```

### Additional: Shield Active Effect

```
/imagine translucent golden-blue hexagonal shield aura effect, concentric rings
of gold and blue energy, small star sparkles at edges, seen from above top-down,
game power-up shield effect, pixel art style, transparent center, glowing energy
barrier, isolated on transparent background --ar 1:1 --style raw --s 150
```

---

## 6. Emenda Pix (Pix Transfer Icon)

### Stable Diffusion / SDXL

```
a corrupted glowing green Pix payment icon, the Brazilian instant payment system
logo which is a diamond shape (square rotated 45 degrees) with transfer arrows
inside, seen from above at a slight angle, top-down perspective, the diamond
glows with sickly green energy like corrupted money, small green particles orbit
around it, a bold yellow "2x" multiplier text floats nearby, the icon represents
corrupt parliamentary amendment transfers (emendas Pix), green color palette
matching toxic gas aesthetic, isolated object on transparent background,
(underground comix art style:1.3), (Robert Crumb inspired:1.2), thick uneven
ink outlines, grotesque detailed, dirty saturated green colors mixed with gold
corruption accents, pixel art, Brazilian political humor, hand-drawn imperfect
lines, cross-hatching shadows, sickly green glow, floating particles
```

**Negative prompt:**
```
clean digital art, smooth gradients, 3D render, photorealistic, anime,
cartoon cute style, bright pure colors, thin lines, symmetric, perfect,
polished, watermark, signature, modern app icon, flat design, corporate logo
```

### DALL-E 3

```
Top-down view of a corrupted glowing Pix payment icon (Brazilian instant
payment logo - diamond/rotated square shape with transfer arrows inside) in the
art style of Robert Crumb's underground comix. The diamond glows with sickly
toxic green energy, small green particles orbiting around it, a bold yellow "2x"
multiplier text floating nearby. Represents corrupt parliamentary amendment money
transfers. Thick uneven black ink outlines, cross-hatching shadows, dirty
saturated greens with gold corruption accents. Hand-drawn 1970s underground
Brazilian political comic style. Isolated on transparent background, slight
isometric angle.
```

### Midjourney v6

```
/imagine corrupted glowing green Pix payment diamond icon, rotated square with
transfer arrows, sickly toxic green glow, orbiting green particles, yellow 2x
multiplier text, corrupt money energy, seen from above top-down isometric,
Robert Crumb underground comix art style, thick uneven ink outlines, dirty
saturated greens with gold accents, cross-hatching shadows, Brazilian political
satire, hand-drawn imperfect, isolated object --no background text watermark
--ar 1:1 --style raw --s 200
```

### Additional: Active Trail Effect

```
/imagine green particle trail energy effect, small glowing green orbs in a
circular orbit pattern, sickly toxic green wisps trailing downward, yellow 2x
text floating, corrupted data particles, seen from above top-down, game power-up
aura effect, pixel art style, transparent center, isolated on transparent
background --ar 1:1 --style raw --s 150
```

---

## Post-Generation Pipeline

For each generated image, follow this process:

### Step 1: Scale Down
- Resize to 4x target (64x64 for 16px items, 96x96 for 24px items) using nearest-neighbor
- Manually clean up at this intermediate size
- Final downscale to target (16x16 or 24x24) using nearest-neighbor (NO anti-aliasing)

### Step 2: Outline Pass
- Add/reinforce 1-2px black (`#1A1A18`) outlines on all edges
- Make outlines UNEVEN -- vary thickness by 1px randomly
- Break perfect straight lines -- add micro-wobbles

### Step 3: Color Correction
- Match all colors to the hex values in sprite-spec.md
- Ensure NO pure colors exist -- everything is dirty/mixed
- Add 10% `#5C5C55` to any color that looks too clean

### Step 4: Texture Overlay
- Apply Gaussian noise (monochromatic, 3-5% opacity) to simulate offset print
- This must be applied per-frame, not as a sheet overlay

### Step 5: Frame Assembly
- Cut/arrange into horizontal sprite sheet
- Verify each frame boundary is clean (no pixel bleed between frames)
- Export as PNG with full alpha transparency

### Step 6: Validation
- View at 1x zoom (actual game size) -- silhouette must be INSTANTLY recognizable
- View against dark background (concrete, asphalt tiles)
- View against light background (dry grass tiles)
- Glow must be visible in both contexts
- Each item must be distinguishable from ALL other items at a glance
