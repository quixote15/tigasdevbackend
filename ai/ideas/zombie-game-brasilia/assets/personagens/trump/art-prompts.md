# TRAMPI (Trump) - Prompts de Geracao de Arte por IA

## Boss Internacional - "Zumbis de Brasilia"

---

## Notas de Uso

- Cada prompt inclui versoes para **Stable Diffusion XL**, **DALL-E 3** e **Midjourney v6**
- Os prompts negativos sao CRITICOS para manter o estilo grotesco e evitar "limpeza" da IA
- Apos gerar, SEMPRE aplicar pos-processamento: adicionar linhas irregulares, cross-hatching, textura papel sujo
- Resolucao de geracao: 1024x1024 minimo, depois recortar/redimensionar para 64x64px com nearest-neighbor (NUNCA bilinear -- mantém pixels duros)
- O estilo Andre Guedes e a REFERENCIA PRIMARIA. Se a IA gerar algo "bonito demais", esta ERRADO

---

## Prompt Base de Estilo (Prefixo para TODOS os prompts)

### Stable Diffusion XL -- Prefixo
```
underground comix style, grotesque political caricature, Robert Crumb inspired, 
thick irregular ink outlines 2-4px, cross-hatching shadows, dirty paper texture, 
saturated muddy colors, Brazilian political humor, B-movie horror aesthetic, 
deformed proportions, exaggerated anatomy, pixel art sprite, 64x64 pixels, 
low resolution retro game sprite, hand-drawn feel, jerky animation frame,
Andre Guedes cartoon style, ((extremely ugly)), ((grotesque)), ((caricature)),
```

### Negative Prompt Global
```
beautiful, clean, smooth, realistic, photographic, 3D render, CGI, anime, manga, 
cute, kawaii, chibi proportional, symmetric, perfect anatomy, digital painting, 
airbrushed, gradient smooth, vector art, flat design, minimalist, modern, 
professional illustration, Disney style, Pixar style, soft shadows, gentle,
pretty, attractive, handsome, refined, elegant, sophisticated, high fashion,
normal proportions, correct anatomy, realistic hands, large hands
```

---

## 1. PORTRAIT / RETRATO COMPLETO

### Para: Tela de selecao de personagem, UI, cards

#### Stable Diffusion XL
```
Prompt:
underground comix style, grotesque political caricature, Robert Crumb inspired,
thick irregular ink outlines 2-4px, cross-hatching shadows, dirty paper texture,
portrait of Donald Trump caricature called "Trampi", Brazilian political satire,
((NEON FLUORESCENT ORANGE SKIN)) like industrial fake tan disaster, 
((COMICALLY TINY MICROSCOPIC HANDS)) absurdly small baby hands that cant grab anything,
((ENORMOUS bird nest orange hair)) messy cotton candy mutant hair with loose strands,
((OVERSIZED golden suit)) cheap gaudy gold fabric too big for body,
((EXTREMELY LONG red necktie)) reaching down to knees,
((double chin)) pronounced jowls, bully expression, squinting small eyes,
smug arrogant smirk showing irregular teeth, bulbous nose,
orange glow emanating from skin, neon effect,
confrontational power stance, dictator pose,
blood orange sky background, toxic green gas,
Brazilian Esplanada dos Ministerios silhouette behind,
squat proportions 5 heads tall, oversized torso,
dirty saturated color palette, horror B-movie lighting

Negative:
beautiful, clean, smooth, realistic, photographic, 3D render, anime, cute, 
symmetric, perfect anatomy, normal sized hands, proportional hands,
airbrushed, gradient smooth, pretty, attractive, elegant, sophisticated,
normal proportions, realistic skin tone, natural orange, subtle
```

#### DALL-E 3
```
A grotesque underground comix style caricature portrait of a fictional political 
boss character called "Trampi" for a Brazilian satirical zombie video game. 
The character has EXTREMELY fluorescent neon orange skin (like he fell into 
industrial fake tan), a massive bird-nest shaped orange hair that looks like 
mutant cotton candy with strands flying everywhere, and ABSURDLY MICROSCOPIC 
tiny hands -- so small they look like baby doll hands on a huge body. He wears 
a gaudy oversized golden suit thats way too big, with a blood-red necktie that 
hangs all the way down to his knees. His expression is a smug bully smirk with 
squinting eyes and a prominent double chin. The art style is Robert Crumb 
underground comics meets Brazilian political humor -- thick uneven ink outlines, 
cross-hatching for shadows, dirty paper texture, saturated muddy colors. 
Background: blood-orange sky with toxic green haze. Proportions: squat and 
stocky, head 1.5x too large, torso 2x too wide. The character should look 
UGLY, GROTESQUE, and FUNNY -- never attractive or dignified.
```

#### Midjourney v6
```
/imagine prompt: grotesque underground comix political caricature, "Trampi" 
boss character, NEON FLUORESCENT ORANGE skin glowing, MICROSCOPIC tiny baby 
hands, enormous bird-nest orange hair with flyaway strands, oversized cheap 
golden suit, extra-long red necktie to knees, double chin, bully smirk, 
squinting eyes, Robert Crumb ink style, thick irregular outlines, 
cross-hatching shadows, dirty paper texture, Brazilian political satire, 
B-movie horror, blood orange sky, toxic green fog, squat 5-head proportions 
--ar 1:1 --style raw --no beautiful clean smooth realistic anime cute 
symmetric pretty elegant --v 6
```

---

## 2. SPRITE IDLE (4 frames)

### Para: Sprite sheet 256x64px de idle

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 4 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss, ((neon fluorescent orange skin with glow)),
((microscopic tiny hands 3 pixels)), ((bird nest orange hair)),
((oversized golden suit)), ((long red tie to knees)),
idle animation cycle, power stance, slight breathing motion,
frame 1: standing power pose bully expression,
frame 2: chest puffs up ego inflating,
frame 3: tiny hand tries to adjust tie but drops it,
frame 4: attempts OK hand gesture but hands too small to form it,
pixel art retro game style, transparent background, sprite sheet format,
dirty saturated colors, cross-hatching shadows

Negative:
beautiful, smooth, realistic, 3D, anime, cute, large hands, normal hands,
proportional hands, high resolution detail, anti-aliased, soft edges,
gradient smooth, clean lines, perfect geometry, symmetric
```

---

## 3. SPRITE WALK (6 frames)

### Para: Sprite sheet 384x64px de caminhada

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 6 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss walking cycle,
((neon fluorescent orange skin)), ((microscopic tiny hands)),
((bird nest orange hair bouncing with steps)),
((oversized golden suit swaying)), ((long red tie swinging)),
heavy authoritative walk, body leans with each step,
frame 1: right foot contact weight shifting,
frame 2: mid stride passing,
frame 3: right foot lifting,
frame 4: left foot contact mirror,
frame 5: mid stride passing mirror,
frame 6: left foot lifting,
suit jacket flaps open with movement, tie swings opposite to walk,
hair deforms with each step jerky motion,
pixel art retro game style, transparent background,
dirty saturated colors, side view 3/4 angle

Negative:
beautiful, smooth, realistic, 3D, anime, cute, large hands, normal hands,
graceful walk, elegant stride, smooth animation, fluid motion,
clean lines, perfect geometry, anti-aliased
```

---

## 4. SPRITE ATTACK (3 frames)

### Para: Sprite sheet 192x64px de ataque

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 3 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss attack animation,
((neon fluorescent orange skin)), ((microscopic tiny hands trying to grip weapon)),
((bird nest orange hair deforming with swing)),
((oversized golden suit stretching at seams)),
golf club swing attack motion,
frame 1: wind up pulling back tiny hand barely gripping golden club,
frame 2: full swing peak velocity hair flying suit buttons popping motion blur,
frame 3: follow through smug expression "TREMENDOUS" text floating above,
impact sparkles golden particles, 
tiny hands struggling to hold the weapon slipping,
pixel art retro game style, transparent background,
explosive action, exaggerated motion lines

Negative:
beautiful, smooth, realistic, 3D, anime, cute, large hands, normal hands,
correct grip, proper form, elegant swing, graceful motion,
clean lines, anti-aliased, soft
```

---

## 5. SPRITE DEATH (4 frames)

### Para: Sprite sheet 256x64px de morte

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 4 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss death animation sequence,
((neon orange skin glow fading)), ((microscopic tiny hands flailing)),
((bird nest hair flying off revealing bald patch underneath)),
((golden suit falling apart buttons popping)),
frame 1: hit recoil shock expression mouth agape eyes wide,
frame 2: falling backward hair detaching showing pink bald head ketchup stains on shirt,
frame 3: on the ground suit spread like golden puddle tie over face X eyes tooth flying,
frame 4: fading transparency orange glow dies skin turns pale hair shrinks suit loses shine,
"FAKE NEWS" text floating and fading, defeated humiliated,
pixel art retro game style, transparent background,
dramatic death comedy, pathetic defeat

Negative:
beautiful, smooth, realistic, 3D, anime, cute, dignified death, heroic,
noble defeat, graceful fall, clean, elegant, respectful,
anti-aliased, soft edges
```

---

## 6. SPRITE HIT (2 frames)

### Para: Sprite sheet 128x64px de hit reaction

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 2 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss getting hit damage reaction,
((neon orange skin flashing white)), ((microscopic tiny hands raised defensively but useless)),
((bird nest hair deforming on impact stretching)),
((golden suit vibrating outline doubling)),
frame 1: recoil from hit white flash pain expression mouth O eyes squeezed shut star particles,
frame 2: recovery anger expression instant transition from pain to fury squinting rage,
damage indicators, knockback motion,
pixel art retro game style, transparent background,
jerky twitchy no smooth transition abrupt

Negative:
beautiful, smooth, realistic, 3D, anime, cute, graceful, stoic,
smooth transition, gentle reaction, fluid motion,
anti-aliased, soft, clean
```

---

## 7. SPECIAL - BUILD THE WALL (4 frames)

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 4 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss casting wall spell,
((neon fluorescent orange skin glowing intensely)),
((microscopic tiny hands extended trying to summon)),
((bird nest hair standing up with power)),
frame 1: plants feet extends tiny hands forward power stance,
frame 2: golden bricks rising from ground 4x4 pixel blocks,
frame 3: golden wall forming with "TRUMP" text in gaudy letters,
frame 4: pointing at wall proudly tiny hand barely visible,
fake gold wall tacky cheap looking, 
golden sparkle particles, construction debris,
pixel art retro game style, transparent background

Negative:
beautiful, smooth, realistic, 3D, anime, cute, impressive wall,
well-built, solid construction, elegant, refined gold,
anti-aliased, clean, sophisticated
```

---

## 8. SPECIAL - FAKE NEWS (4 frames)

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 4 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss casting fake news spell,
((neon orange skin)), ((microscopic tiny hands fumbling with phone dropping it once)),
frame 1: tiny hand reaches for phone drops it fumble animation,
frame 2: picks up phone screen glows red FAKE NEWS text,
frame 3: distortion waves emanating from phone concentric circles spreading,
frame 4: smug satisfied grin reality warping around him,
information warfare visual, red text particles,
digital glitch effects, propaganda waves,
pixel art retro game style, transparent background

Negative:
beautiful, smooth, realistic, 3D, anime, cute, truthful, honest,
clean technology, sleek phone, elegant, sophisticated,
anti-aliased, clean lines
```

---

## 9. SPECIAL - AMERICA FIRST ULTIMATE (8 frames)

#### Stable Diffusion XL (gerar em partes de 4 frames)

##### Parte 1 (frames 0-3):
```
Prompt:
pixel art sprite sheet, 4 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss ultimate attack first half,
((neon orange skin at maximum glow)), ((microscopic tiny hands raised to sky)),
((bird nest hair blowing dramatically)),
frame 1: raises both tiny hands skyward summoning pose screaming,
frame 2: sky darkens blue-red filter begins golden eagles descend,
frame 3: steel golden eagles attacking 32x32 sprites explosions,
frame 4: patriotic starbursts red white blue American flags sprouting from ground,
military industrial spectacle, over the top patriotism,
distorted national anthem energy, golden eagle bombers,
pixel art retro game style, transparent background

Negative:
beautiful, smooth, realistic, 3D, anime, cute, respectful patriotism,
genuine reverence, tasteful, subtle, understated, dignified,
anti-aliased, clean, sophisticated
```

##### Parte 2 (frames 4-7):
```
Prompt:
pixel art sprite sheet, 4 frames horizontal strip, 64x64 pixels each frame,
underground comix style, grotesque caricature, thick ink outlines,
character "Trampi" political boss ultimate attack second half,
((neon orange skin pulsing with power)), ((hair blown by explosions)),
frame 5: wind blowing hair and tie dramatically power pose amidst destruction,
frame 6: maximum white flash screen 80 percent white overwhelming,
frame 7: aftermath smoke clearing Trampi in victory pose surrounded by destruction flags,
frame 8: return to normal power stance smug everything destroyed around him,
aftermath devastation, gaudy golden destruction,
American flag debris, eagle feathers falling,
pixel art retro game style, transparent background

Negative:
beautiful, smooth, realistic, 3D, anime, cute, subtle, tasteful,
clean destruction, elegant, anti-aliased, sophisticated
```

---

## 10. MICRO-HANDS DETAIL SHEET

### Para: Overlay sprite sheet 192x16px (12 frames de 16x16px)

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 12 frames horizontal strip, 16x16 pixels each frame,
extreme close up of comically tiny microscopic hands, 
((only 3x3 pixels per hand)), neon fluorescent orange skin,
underground comix style, grotesque humor,
frame sequence: idle hanging, trying to grab, failing to grab, dropping object,
pointing with stub finger, attempting OK sign failing, tiny fist,
waving, thumbs up barely visible, rare successful grab, trembling, 
dead rigid insect legs pointing up,
each hand is ABSURDLY SMALL like baby doll hand on adult body,
comedy of inadequacy, pathetic tiny appendages,
pixel art retro game style, transparent background

Negative:
normal hands, large hands, proportional hands, realistic hands,
detailed fingers, elegant hands, beautiful hands, capable hands,
3D, smooth, anti-aliased, high detail
```

---

## 11. CABELO-NINHO DETAIL SHEET

### Para: Overlay sprite sheet 128x16px (8 frames de 16x16px)

#### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 8 frames horizontal strip, 16x16 pixels each frame,
extreme close up of enormous bird nest shaped orange hair,
mutant cotton candy hair, flyaway strands in all directions,
underground comix style, grotesque texture,
frame sequence: normal volume with 2 loose strands, 
wind right deforming 3 pixels with 4 flying strands,
wind left mirror, impact flattened widened, 
ego puff inflated larger, messy disheveled all directions,
partially detached revealing pink bald underneath,
completely gone just pink bald scalp hair falling as separate object,
exaggerated impossible hair physics, 
pixel art retro game style, transparent background

Negative:
realistic hair, beautiful hair, styled hair, neat groomed,
natural flow, elegant, sophisticated, clean,
3D, smooth, anti-aliased
```

---

## 12. EFEITO GLOW LARANJA (Reference Tecnica)

### Para: Guia de pos-processamento do glow da pele

```
Nao gerar por IA -- implementar tecnicamente no Phaser 3:

1. Duplicar sprite do personagem
2. Aplicar filtro de cor solida #FFAA33
3. Expandir 1px em todas direcoes (dilate)
4. Aplicar blur de 1px
5. Colocar ATRAS do sprite original
6. Animar opacity: 
   - Idle: sine wave 30%-50% (periodo 2s)
   - Hit: flash 100% branco por 100ms, depois volta
   - Death: linear fade 50% -> 0% (1.5s)
   - Attack: constante 60%
   - Ultimate: constante 100%, cor alterna azul-branco-vermelho (200ms cada)
```

---

## Guia de Pos-Processamento

### Passo a Passo Apos Geracao por IA

1. **Redimensionar**: De 1024x1024 para 64x64 usando NEAREST NEIGHBOR (sem anti-alias)
2. **Adicionar outlines**: Linhas pretas irregulares 2-4px ao redor de cada elemento, NUNCA retas
3. **Cross-hatching manual**: Adicionar hachura diagonal nas areas de sombra (sob queixo, flancos do terno, entre pernas)
4. **Textura papel sujo**: Overlay de textura de papel amarelado a 10-15% opacity
5. **Saturar + Sujar**: Aumentar saturacao 20%, depois adicionar ruido gaussiano 5%
6. **Corrigir maos**: As IAs SEMPRE vao fazer as maos grandes demais. REDUZIR manualmente para 3x3px maximo
7. **Verificar glow**: A pele laranja deve parecer NEON/FLUORESCENTE, nao apenas laranja normal
8. **Verificar proporcoes**: Cabeca 1.5x, torso 2x, pernas 1.5x, maos 0.1x (microscopicas)
9. **Irregular tudo**: Se algo ficou geometricamente perfeito, DISTORCER levemente
10. **Remover fundo**: Garantir alpha transparency perfeita

### Checklist Final por Frame
- [ ] Maos microscopicas visiveis (por serem absurdamente pequenas)?
- [ ] Pele genuinamente NEON laranja fluorescente com glow?
- [ ] Cabelo com formato de ninho de passarinho?
- [ ] Terno visivelmente OVERSIZED e dourado cafona?
- [ ] Gravata descendo ate o joelho?
- [ ] Outlines irregulares estilo Crumb?
- [ ] Cross-hatching nas sombras?
- [ ] Expressao de bully/arrogante?
- [ ] Proporcoes atarracadas (5 cabecas de altura)?
- [ ] Nenhuma parte "bonita" ou "limpa" demais?
