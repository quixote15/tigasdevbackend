# Ciro Gomes - Prompts para Geracao de Arte

## PROMPT BASE DO PERSONAGEM

### Stable Diffusion / SDXL

```
grotesque caricature of a Brazilian politician, gray-haired older man with perfectly styled silver hair, dark navy suit too expensive for the apocalypse, red tie, bulging purple neck veins like angry snakes, red flushed face, clenched jaw, holding a small medicine bottle (Rivotril), carrying an economics book nobody reads, underground comix style, Robert Crumb inspired, thick outlines, heavy shadows, dirty saturated colors, orange-blood sky background, top-down isometric pixel art, 64x64 pixel sprite, game asset, transparent background
```

### DALL-E 3

```
A grotesque underground comic-style caricature of an arrogant Brazilian male politician as a 64x64 pixel game sprite, top-down isometric perspective. He has perfectly styled silver-gray hair (the ONLY neat thing about him), a dark navy expensive suit, red tie, and a face flushed red with rage. His neck has grotesquely bulging purple veins that look like writhing snakes. He's clutching a small orange medicine bottle in one hand and an economics book under his other arm. Style: Robert Crumb meets Brazilian political satire meets B-movie horror. Thick black outlines, heavy shadows, exaggerated proportions with oversized head. Transparent PNG background.
```

### Midjourney

```
/imagine grotesque political caricature, Brazilian politician, silver perfectly styled hair, navy suit, red tie, purple bulging veins on thick neck, red flushed angry face, holding medicine bottle and economics book, underground comix style, Robert Crumb influence, B-movie horror comedy, thick outlines, heavy shadows, dirty saturated palette, pixel art sprite 64x64, top-down isometric, transparent background --ar 1:1 --style raw --no smooth, clean, cute, anime
```

---

## PROMPTS POR ANIMACAO

### Idle (4 frames)

```
[BASE PROMPT] + standing arrogantly with chin raised, one hand holding small orange bottle, book tucked under arm, confident smirk, veins visible on neck, pixel art sprite sheet, 4 frames horizontal strip, 256x64 pixels total, slight variations between frames showing breathing and impatience, twitchy jerky animation style
```

### Walk (6 frames)

```
[BASE PROMPT] + walking briskly with irritated stride, hurried pace, arms swinging aggressively, tie flapping, suit stretching at shoulders, medicine bottle in jacket pocket, book nearly falling from under arm, pixel art walk cycle sprite sheet, 6 frames horizontal strip, 384x64 pixels total, jerky choppy animation, NOT smooth
```

### Attack (Rivotril Turbo - 3 frames)

```
[BASE PROMPT] + swinging an oversized medicine bottle like a war club, overhead swing attack, face bright red with rage, veins maximally bulging, mouth open screaming, liquid splashing from bottle on impact, blue cyan liquid drops flying, pixel art attack animation sprite sheet, 3 frames horizontal strip, 192x64 pixels total, violent twitchy motion
```

### Death / Pacoca Mental (4 frames)

```
[BASE PROMPT] + falling backwards dramatically, medicine bottle flying from hand, book falling, suit crumpling, eyes going blank, speech bubble with "pacoca..." text, lying on ground with vacant expression, mouth moving robotically, colors desaturating, pixel art death animation sprite sheet, 4 frames horizontal strip, 256x64 pixels total
```

### Hit (2 frames)

```
[BASE PROMPT] + recoiling from impact, white flash overlay, face turning redder, mouth open yelling insult, fist clenching, medicine bottle almost dropping, pixel art hit reaction sprite sheet, 2 frames horizontal strip, 128x64 pixels total, exaggerated knockback
```

### Cirocracia (Energy Dome - 8 frames)

```
[BASE PROMPT] + summoning a translucent blue energy dome/force field around himself, arms raised, blue royal particles spiraling upward, dome forming then cracking then shattering into fragments, trapped inside his own creation, pixel art special ability animation sprite sheet, 8 frames horizontal strip, 512x64 pixels total, magical energy effect, blue glow
```

### Rage do Rivotril (6 frames)

```
[BASE PROMPT] + looking at EMPTY medicine bottle in horror, face going from normal to maximum red, veins EXPLODING from neck like tentacles, eyes turning red, spinning wildly with bottle as weapon, shockwave circle around him, dizzy with stars after, pixel art rage mode animation sprite sheet, 6 frames horizontal strip, 384x64 pixels total, berserker frenzy
```

### Candidatura Eterna - Ressurreicao (4 frames)

```
[BASE PROMPT] + lying dead then golden glow appears at edges, body levitates, suit magically repairs itself, tie straightens, standing again but SMALLER and more faded than before, pointing finger upward triumphantly but clearly weaker, pixel art resurrection animation sprite sheet, 4 frames horizontal strip, 256x64 pixels total, golden light effect
```

### Debate Unilateral (4 frames)

```
[BASE PROMPT] + standing with coffee cup in hand, arms spread wide in orator pose, huge speech bubble appearing with random symbols, nearby characters showing confusion question marks and irritation, nobody listening, pixel art speech animation sprite sheet, 4 frames horizontal strip, 256x64 pixels total, comedic effect
```

### Xingamento Erudito (4 frames)

```
[BASE PROMPT] + inhaling deeply chest expanding, mouth opening grotesquely wide to 60% of face, visible sound waves emanating, bold red text "BOSSALOIDE!" flying as projectile toward enemy, enemy stunned with stars, straightening tie smugly after, pixel art shout attack animation sprite sheet, 4 frames horizontal strip, 256x64 pixels total
```

### Terceira Via - Dash (4 frames)

```
[BASE PROMPT] + crouching to dodge, then dashing with triple ghost trail afterimages, body stretched in direction of movement, phasing through enemies without hitting anything, stopping confused on other side looking back, pixel art dash animation sprite sheet, 4 frames horizontal strip, 256x64 pixels total, speed motion blur
```

---

## PROMPTS PARA EFEITOS ESPECIAIS

### Barra de Rivotril (UI)
```
pixel art UI health bar element, 32x4 pixels, gradient from cyan (#00BFFF) to red (#FF0000), small orange medicine bottle icon 8x8 on left side, pulsing red border when empty, game HUD element, transparent background, clean pixel art
```

### Projetil - Frasco Voando
```
pixel art projectile, small orange glass bottle spinning in air, 4 rotation frames, blue liquid trail behind it, 32x32 pixels per frame, 128x32 sprite sheet, impact frame with liquid splash, transparent background
```

### Projetil - Texto "BOSSALOIDE!"
```
pixel art text projectile, bold red pixelated text "BOSSALOIDE!" with yellow concentric sound wave circles around it, 32x16 pixels, 2 frame animation, shaking trembling text effect, transparent background
```

### Cupula da Cirocracia
```
pixel art translucent blue energy dome, royal blue (#4169E1) semi-sphere, 56x56 pixels, glowing edges, small particles orbiting, cracks forming, shattering into fragments, transparent background, magical force field effect
```

---

## NEGATIVE PROMPTS

### Para TODOS os prompts de Ciro, adicionar:

**Stable Diffusion:**
```
--negative_prompt smooth, clean lines, anime style, cute, kawaii, realistic photo, 3D render, soft shading, gradient shading, cel shading, vector art, flat design, minimalist, pastel colors, watercolor, oil painting, modern, sleek, polished, symmetrical face, handsome, young, thin, blurry, low contrast, muted colors, gentle expression, calm face
```

**Midjourney:**
```
--no smooth, clean, cute, anime, realistic, 3D, soft, gradient, cel-shaded, vector, flat, pastel, watercolor, modern, sleek, polished, symmetrical, handsome, young, blurry, muted, gentle, calm
```

**DALL-E 3:**
Incluir no prompt: "Do NOT make the character look handsome, calm, young, or clean. The style must be GROTESQUE, dirty, exaggerated, underground comix. NOT anime, NOT cute, NOT smooth."

---

## STYLE TAGS

### Tags obrigatorias em TODOS os prompts:

```
underground comix, Robert Crumb style, grotesque caricature, thick outlines, heavy shadows, dirty saturated colors, B-movie horror, Brazilian political satire, pixel art, game sprite, top-down isometric, twitchy animation, jerky movement, exaggerated proportions, oversized head, deformed anatomy
```

### Tags especificas de Ciro:

```
arrogant politician, silver hair perfectly styled, navy suit, red tie, bulging neck veins, flushed red face, medicine bottle, economics book, nobody listening, comic relief, eternal candidate
```

---

## DICAS PARA GERACAO

1. **Cabeca grande, corpo pequeno**: Proporcao ~40/60. A cabeca de Ciro deve dominar o sprite.
2. **Veias sao ESSENCIAIS**: Se o prompt nao gerar veias visiveis no pescoco, regenerar. E a marca registrada.
3. **Contraste terno/caos**: O terno DEVE parecer caro e arrumado. O rosto DEVE parecer furioso e deformado. O contraste e a piada.
4. **Rivotril sempre visivel**: O frasco laranja deve ser reconhecivel mesmo em 64x64.
5. **Vermelho progressivo**: Cada frame de raiva deve ser MAIS vermelho que o anterior.
6. **NAO suavizar**: Se a IA tender a "limpar" o estilo, reforcar "underground comix, grotesque, Robert Crumb, dirty lines, NOT clean, NOT smooth".
7. **Sprite sheet alignment**: Garantir que todos os frames tenham o personagem na mesma posicao Y (pes alinhados) para evitar "pulo" na animacao.
