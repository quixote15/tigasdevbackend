# Taco de Golfe Nuclear - Prompts de Geracao de Arte por IA

## Arma Exclusiva do Trampi - "Zumbis de Brasilia"

---

## Notas de Uso

- Prompts focados em **Stable Diffusion XL** (melhor para pixel art de objetos)
- Incluir variantes DALL-E 3 e Midjourney para prompts criticos
- Resolucao de geracao: 1024x1024, depois downscale com nearest-neighbor para 32x32px
- NUNCA usar bilinear/bicubic para downscale -- pixels DUROS sempre
- Pos-processamento OBRIGATORIO: linhas irregulares, cross-hatching, textura papel sujo

---

## Prompt Base de Estilo (Prefixo para TODOS os prompts)

### Stable Diffusion XL -- Prefixo
```
pixel art weapon sprite, underground comix style, Robert Crumb thick irregular ink outlines,
cross-hatching shadows, dirty paper texture, saturated muddy colors, 
grotesque exaggerated proportions, retro game sprite 32x32 pixels,
hand-drawn feel, Brazilian political satire game asset,
```

### Negative Prompt Global
```
beautiful, clean, smooth, realistic, photographic, 3D render, CGI, anime, manga,
cute, kawaii, elegant, sophisticated, refined, professional, modern, minimalist,
vector art, flat design, gradient smooth, airbrushed, symmetric, perfect geometry,
high detail, anti-aliased, soft edges, gentle, subtle, understated
```

---

## 1. TACO DE GOLFE -- SPRITE COMPLETO

### Stable Diffusion XL
```
Prompt:
pixel art weapon sprite, underground comix style, Robert Crumb thick irregular ink outlines,
cross-hatching shadows, dirty paper texture, 32x32 pixel sprite,
((golden golf club weapon)), gaudy cheap fake gold color, 
oversized club head with ((nuclear radiation symbol)) trefoil sticker,
red leather grip with cross-hatch texture,
golden shaft slightly bent irregular not straight,
((nuclear green glow)) around club head radioactive,
metallic highlights scattered along shaft,
tacky gaudy ostentatious not elegant,
like a cheap casino prop weapon,
transparent background, game sprite,
thick black outlines 2-3 pixels uneven

Negative:
beautiful, elegant, refined golf club, professional sports equipment,
realistic metal, clean lines, smooth, symmetric, modern design,
3D render, photographic, subtle, tasteful, expensive looking,
anti-aliased, gradient, soft
```

### DALL-E 3
```
A pixel art sprite of a gaudy golden golf club weapon for a satirical 
Brazilian political zombie game. The club is 32x32 pixels, drawn in 
underground comix style with thick uneven black ink outlines. The shaft 
is cheap-looking gold (like costume jewelry, not real gold) and slightly 
bent/irregular. The club head is oversized and has a radiation/nuclear 
trefoil symbol stuck on it like a crooked sticker. The grip is red 
leather with visible cross-hatching texture. There's a sickly 
yellow-green radioactive glow around the club head. The entire weapon 
looks TACKY, GAUDY, and FAKE -- like a prop from a cheap casino. 
Robert Crumb art style: thick irregular lines, cross-hatching for 
shadows, dirty paper texture feel. Transparent background.
```

### Midjourney v6
```
/imagine prompt: pixel art 32x32 sprite, golden golf club weapon, 
gaudy cheap fake gold, oversized clubhead with nuclear symbol sticker, 
red leather grip, radioactive green glow, underground comix Robert Crumb 
style, thick irregular ink outlines, cross-hatching, tacky casino prop, 
game weapon sprite, transparent background --ar 1:1 --style raw 
--no beautiful elegant refined smooth realistic 3D --v 6
```

---

## 2. TACO -- SWING ANIMATION (4 frames)

### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 4 frames horizontal strip, 32x32 pixels each frame,
underground comix style, thick ink outlines,
golden golf club weapon swing animation sequence,
gaudy cheap gold, nuclear glow on clubhead,
frame 1: club pulled back behind 140 degrees wind up tension bent shaft,
frame 2: club mid-swing horizontal maximum speed motion blur lines trailing,
frame 3: club at impact point squashed clubhead starburst contact sparks,
frame 4: club follow through ascending after hit residual motion lines,
each frame shows increasing then decreasing energy,
golden particles and nuclear glow intensifying at impact,
pixel art retro game style, transparent background

Negative:
beautiful, smooth, realistic, 3D, anime, elegant, refined,
proper golf form, professional swing, clean lines,
anti-aliased, gradient, soft
```

---

## 3. BOLA DE GOLFE COM CARA DO TRUMP

### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 8 frames horizontal strip, 32x32 pixels each frame,
underground comix style, thick ink outlines,
golf ball projectile with ((Trump caricature face painted on it)),
((neon fluorescent orange face)) on white golf ball,
((bird nest orange hair as tiny tuft on top)) of the ball,
angry screaming expression squinting eyes open mouth,
dimpled golf ball texture white surface,

frame 1: ball static showing angry Trump face front view,
frame 2: ball flying rotation 0 degrees face forward fire trail behind,
frame 3: ball rotation 90 degrees face in profile fire trail,
frame 4: ball rotation 180 degrees showing back of hair tuft fire trail,
frame 5: ball rotation 270 degrees opposite profile fire trail fading,
frame 6: ball about to explode panicked expression cracking surface flashing,
frame 7: ball EXPLODING golden burst fragments face flying off "TREMENDOUS" text,
frame 8: explosion dissipating golden smoke debris fading,

fire trail behind ball in flight frames,
((face changes from angry to panicked before explosion)),
golden explosion not regular fire,
pixel art retro game style, transparent background

Negative:
beautiful, clean, smooth, realistic, 3D render, anime, cute,
normal golf ball, elegant, refined, professional,
anti-aliased, gradient, soft, subtle
```

### DALL-E 3
```
A pixel art sprite sheet showing 8 frames (32x32 pixels each) of a 
golf ball projectile for a satirical Brazilian political zombie game. 
The golf ball has a caricature of Trump's face painted on it -- neon 
fluorescent orange skin, tiny bird-nest orange hair tuft on top, 
squinting angry eyes, and screaming open mouth. Underground comix 
Robert Crumb art style with thick irregular outlines.

The 8 frames show: (1) Ball static with angry face, (2-5) Ball flying 
and rotating through 4 positions with fire trail behind it, the face 
rotating around the ball, (6) Ball about to explode -- face changes 
to PANICKED expression, surface cracking, flashing, (7) Ball EXPLODING 
in a golden burst with "TREMENDOUS!" text appearing and the face flying 
off as debris, (8) Explosion dissipating into golden smoke.

The explosion is GOLDEN (fake gold particles, not regular fire). 
Everything is grotesque, exaggerated, and funny. Thick uneven ink 
outlines. Cross-hatching shadows. Dirty paper texture feel.
```

### Midjourney v6
```
/imagine prompt: pixel art sprite sheet 8 frames, 32x32 each, 
golf ball with Trump caricature face painted on it, neon orange skin 
tiny hair tuft, angry screaming expression, rotation animation with 
fire trail, explosion into golden debris "TREMENDOUS" text, 
underground comix Robert Crumb style, thick irregular outlines, 
grotesque satirical game projectile --ar 4:1 --style raw 
--no beautiful clean smooth realistic 3D anime elegant --v 6
```

---

## 4. EXPLOSAO DOURADA (Efeito de Impacto)

### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 4 frames horizontal strip, 48x48 pixels each frame,
underground comix style, thick ink outlines,
((golden explosion effect)) not regular fire,
fake gold particles and debris flying,
cheap gaudy golden smoke and sparks,

frame 1: initial flash white center 12px golden starburst 8 rays golden debris launching,
frame 2: expanding golden fireball golden shockwave ring debris spreading golden smoke starting,
frame 3: peak explosion maximum size bold text "TREMENDOUS" golden core golden smoke dominant,
frame 4: dissipating golden smoke debris at edges crater mark on ground fading,

all particles and effects are GOLD colored not orange not red,
((gaudy tacky cheap gold aesthetic)),
nuclear undertone sickly yellow-green mixed with gold,
pixel art retro game style, transparent background,
explosion should look EXPENSIVE but FAKE like costume jewelry exploding

Negative:
beautiful, realistic explosion, cinematic, elegant, refined fire,
normal colored explosion, red orange flame, 
clean, smooth, 3D render, photographic, subtle,
anti-aliased, gradient
```

### DALL-E 3
```
A pixel art sprite sheet of 4 frames (48x48 pixels each) showing a 
GOLDEN EXPLOSION effect for a satirical Brazilian zombie game weapon. 
This is NOT a normal fire explosion -- everything is GOLD colored, like 
cheap fake gold jewelry exploding. Underground comix Robert Crumb art 
style with thick uneven ink outlines.

Frame 1: White flash at center with golden starburst rays and golden 
debris launching outward. Frame 2: Expanding golden fireball with 
shockwave ring, debris spreading, golden smoke beginning. Frame 3: 
Peak explosion at maximum size, bold "TREMENDOUS!" text in gold, 
thick golden smoke. Frame 4: Dissipating golden smoke, debris at 
edges almost gone, dark crater mark on ground.

The aesthetic is GAUDY and TACKY -- like a cheap casino sign exploding. 
Mix of gold (#DAA520, #FFD700) with sickly nuclear yellow-green hints. 
Thick irregular outlines, cross-hatching in smoke, dirty paper texture.
```

---

## 5. TACO SEGURADO POR MAOS MICROSCOPICAS (Detail)

### Stable Diffusion XL
```
Prompt:
pixel art detail sprite, 32x32 pixels,
underground comix style, thick ink outlines, cross-hatching,
close up of ((comically tiny microscopic orange hand)) 
trying to hold a ((golden golf club)) that is too large for it,
((hand is only 3x3 pixels)), neon fluorescent orange skin on hand,
club grip is 6 pixels wide hand cannot wrap around it,
the grip is slipping the hand is too small,
comedy of inadequacy pathetic tiny appendage holding large weapon,
visible gap between tiny fingers and club handle,
precarious unstable grip about to drop,
pixel art retro game style, transparent background

Negative:
normal hands, large hands, proportional grip, secure grip,
realistic, beautiful, elegant, 3D render, smooth,
capable hands, strong grip, anti-aliased
```

---

## 6. TACO DANIFICADO / QUEBRADO

### Stable Diffusion XL
```
Prompt:
pixel art sprite sheet, 2 frames horizontal strip, 32x32 pixels each,
underground comix style, thick ink outlines, cross-hatching,

frame 1: damaged golden golf club weapon, shaft cracked diagonal line,
clubhead slightly bent misaligned, dulled gold less shiny,
nuclear glow flickering irregular, grip worn out sparse texture,
weapon looks about to break any moment,

frame 2: BROKEN golden golf club split in two pieces,
shaft snapped in half 3 pixel gap between halves,
clubhead detached tilted falling, golden fragments floating,
nuclear glow completely dead no more radiation,
nuclear symbol cracked, grip loose detaching,
metallic decomposition tarnished gold,

pixel art retro game style, transparent background,
sad pathetic broken weapon aesthetic

Negative:
beautiful, intact, new, shiny, elegant, refined, whole,
realistic, 3D render, smooth, clean, anti-aliased,
well-maintained, professional equipment
```

---

## 7. TEXTO "TREMENDOUS!" e "FAKE NEWS!" (Efeito de Impacto)

### Stable Diffusion XL
```
Prompt:
pixel art text effects sprite sheet, 4 frames horizontal strip, 32x16 pixels each,
underground comix style, hand-lettered comic book text,
((NOT typeset NOT font)) hand drawn irregular letters,

frame 1: "TREMENDOUS!" text appearing letter by letter golden yellow color 
with dark red outline, comic book impact style, jagged edges,
frame 2: "TREMENDOUS!" at full size bold thick golden letters maximum impact 
starburst behind, shaking vibrating with energy,
frame 3: "TREMENDOUS!" starting to fade 60 percent opacity letters shrinking,
frame 4: "FAKE NEWS!" text in angry red color with black outline,
bold accusatory style, different energy from tremendous,
both texts should look hand-scrawled not perfectly typed,
uneven baselines wobbly letters Robert Crumb lettering style,
pixel art game text effect, transparent background

Negative:
clean typography, computer font, serif, sans-serif, perfect letters,
symmetric text, professional typesetting, elegant, refined,
smooth, anti-aliased, modern font, minimal
```

---

## 8. LOOT DROP DO TACO (Flutuando no Chao)

### Stable Diffusion XL
```
Prompt:
pixel art game item sprite, 32x32 pixels,
underground comix style, thick ink outlines,
golden golf club floating in air as loot drop collectible item,
maximum shine and sparkle golden highlights everywhere,
3 small golden sparkle particles orbiting around it,
nuclear green glow at maximum around clubhead,
shadow on ground below ellipse shape,
the club rotates slowly slightly angled,
inviting the player to pick it up,
gaudy tacky cheap gold but EXTRA shiny as loot,
pixel art retro game style, transparent background

Negative:
realistic, elegant, refined, subtle, muted,
3D render, photographic, clean, smooth,
anti-aliased, modern, professional
```

---

## Guia de Pos-Processamento

### Pipeline para Sprites do Taco

1. **Gerar em 1024x1024** usando os prompts acima
2. **Selecionar melhor regiao**: Recortar a area mais relevante do output da IA
3. **Downscale**: Nearest-neighbor para 32x32px (ou 48x48 para explosoes)
4. **Limpeza manual**:
   - Remover pixels soltos/ruido
   - Garantir alpha transparency limpa
   - Corrigir outline para 2px irregulares consistentes
5. **Adicionar cross-hatching**: Manualmente nas areas de sombra (diagonal, 1px)
6. **Verificar paleta**: Comparar com tabela de cores da spec. Corrigir desvios.
7. **Dourado correto**: O dourado deve ser #DAA520 (goldenrod), NAO #FFD700 puro. #FFD700 so para highlights.
8. **Glow nuclear**: Adicionar manualmente 1px de #CCFF00 ao redor do clubhead, 30% opacity
9. **Textura de papel**: Overlay de textura papel amarelado a 8-10% opacity
10. **Irregularizar**: Se algo ficou reto/perfeito, DISTORCER com ferramenta warp/liquify em 1-2px

### Checklist Final para Cada Frame

#### Taco
- [ ] Dourado parece CAFONA (nao elegante)?
- [ ] Simbolo nuclear no clubhead (torto, como adesivo)?
- [ ] Glow esverdeado ao redor do clubhead?
- [ ] Outline irregular 2px?
- [ ] Cross-hatching na empunhadura?
- [ ] Pontos de brilho (1px brancos) na haste?
- [ ] Parece uma arma RIDICULA (nao uma arma seria)?

#### Bola de Golfe
- [ ] Rosto do Trump na bola (laranja neon, topete, expressao)?
- [ ] Expressao muda de raiva para panico antes de explodir?
- [ ] Trail de fogo atras durante voo?
- [ ] Rotacao visivel nos frames de voo?
- [ ] Explosao e DOURADA (nao laranja/vermelha normal)?
- [ ] Texto "TREMENDOUS!" ou "FAKE NEWS!" aparece?
- [ ] Fragmentos do rosto voam como particula na explosao?

#### Explosao
- [ ] Predominantemente DOURADA (ouro falso)?
- [ ] Estetica de "joia barata explodindo"?
- [ ] Fumaca dourada (nao cinza)?
- [ ] Detritos dourados?
- [ ] Marca de cratera no chao no frame final?
- [ ] Tamanho correto (48x48px)?

---

## Notas Adicionais

### Consistencia Visual com o Trampi
- O taco PERTENCE ao Trampi. O dourado do taco deve ser o MESMO dourado do terno (#DAA520).
- O glow nuclear do taco complementa o glow laranja da pele do Trampi -- ambos "brilham" mas com cores diferentes.
- Quando o taco esta na mao microscopica, deve haver 1px de gap ou overlap impreciso -- NUNCA um encaixe perfeito.

### Escala Relativa
- Taco: 32x32px sprite, mas quando no jogo ao lado do Trampi (64x64px), o taco ocupa ~24px de altura
- Bola: 32x32px sprite, mas a bola em si tem ~12px de diametro dentro do frame (resto e efeitos)
- Explosao: 48x48px -- MAIOR que o taco e menor que o personagem. O alcance visual da explosao deve ser impactante.

### Referencia de Estilo Final
O taco de golfe nuclear e a ARMA MAIS RIDICULA do jogo. Nao e a mais forte. Nao e a mais pratica. E a mais ABSURDA. Um taco de golfe de ouro falso com simbolo nuclear que dispara bolas com a cara do dono e grita "TREMENDOUS!" quando explode. Se o artista nao esta rindo enquanto desenha, algo esta ERRADO.
