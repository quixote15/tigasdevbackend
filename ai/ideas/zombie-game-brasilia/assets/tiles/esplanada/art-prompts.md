# Art Prompts — Tiles & Cenario Esplanada dos Ministerios

> Prompts otimizados para geracao de imagem (Stable Diffusion XL / DALL-E 3 / Midjourney v6)
> Cada prompt gera UM tile ou grupo de variantes
> Pos-processamento: reduzir para 16x16px, aplicar paleta (color-palette.md), adicionar textura de papel

---

## Estilo Base (Prefixo para TODOS os prompts)

```
STYLE PREFIX (adicionar antes de cada prompt):
"pixel art, 16x16 tile, top-down perspective, hand-drawn style, 
thick irregular outlines, cross-hatching shadows, dirty muted colors, 
underground comix aesthetic, paper texture overlay, Robert Crumb inspired, 
NOT clean vector art, NOT smooth gradients, rough imperfect lines"
```

**Negative prompt global:**
```
"clean lines, vector art, smooth gradients, cel-shading, anime style, 
3D render, photorealistic, bright pure colors, symmetric, perfect geometry,
AI-generated look, stock photo"
```

---

## 1. Tiles Base (T01–T10)

### T01 — Concreto Rachado (4 variantes)

**Prompt:**
```
[STYLE PREFIX]
concrete floor tile, top-down view, cracked gray pavement, 
dirty concrete with hairline cracks in irregular pattern, 
dark stains and weathering marks, brutalist architecture floor,
colors: gray #8A8580 base with #5C5C55 cracks and #3A3530 dark stains,
seamless tileable pattern, urban decay wasteland floor
```

**Variantes:**
- T01a: Rachaduras diagonais NE-SW
- T01b: Rachaduras diagonais NW-SE
- T01c: Rachaduras em X (cruzadas)
- T01d: Rachaduras com mancha grande no centro

**Pos-processamento:**
1. Reduzir para 16x16
2. Aplicar paleta restrita (max 6 cores)
3. Adicionar cross-hatching nas rachaduras (1px linhas diagonais)
4. Overlay textura de papel (3% opacity)
5. Testar seamless: colocar 4 tiles lado a lado

---

### T02 — Concreto Limpo (2 variantes)

**Prompt:**
```
[STYLE PREFIX]
clean indoor concrete floor tile, top-down view, 
institutional building interior floor, slightly worn but maintained,
lighter gray than outdoor concrete, subtle scuff marks,
government office building floor, brutalist architecture interior,
colors: #8A8580 base with #A09888 lighter areas,
seamless tileable pattern
```

**Variantes:**
- T02a: Liso com desgaste sutil
- T02b: Com linha de rodape (borda inferior mais escura)

---

### T03 — Grama Seca (4 variantes)

**Prompt:**
```
[STYLE PREFIX]
dead dry grass tile, top-down view, yellow-straw colored lawn,
Brazilian cerrado dry season grass, tufts of dead vegetation,
patches of bare dirt, neglected public park lawn,
colors: #C4A265 straw-yellow base, #7A8830 darker tufts, 
#5C5C55 bare ground patches,
seamless tileable pattern, wasteland dried grass
```

**Variantes:**
- T03a: Grama densa (mais tufos, menos terra)
- T03b: Grama rala (mais terra exposta)
- T03c: Grama com buraco de obra (centro escuro)
- T03d: Grama com irrigador quebrado (sprite 3x3px metalico)

---

### T04 — Grama com Sangue (3 variantes)

**Prompt:**
```
[STYLE PREFIX]
dead grass with blood-ink stains, top-down view,
stylized blood splatter like red ink NOT realistic gore,
cartoon blood drops on dry yellow grass,
Robert Crumb style blood as paint/ink,
colors: #C4A265 grass + #8B0000 dark red ink splatter,
seamless tileable pattern
```

**Variantes:**
- T04a: Manchas pequenas espalhadas
- T04b: Uma mancha grande central
- T04c: Trilha de gotas (direcional)

**IMPORTANTE:** Sangue estilizado como TINTA, nao sangue real. Gotas amorfas, exageradas, estilo underground comix.

---

### T05 — Agua Turva (9 variantes — bordas + centro)

**Prompt (centro):**
```
[STYLE PREFIX]
murky dark water tile, top-down view, polluted pond surface,
dark green-black stagnant water, slight oily sheen,
no reflections just opaque dirty water, government reflecting pool,
colors: #2A3D2E dark water, #3D6B3A greenish tint,
seamless tileable pattern
```

**Prompt (bordas):**
```
[STYLE PREFIX]
water edge tile where concrete meets murky water, top-down view,
half concrete half dark water, rough stone border,
dirty water lapping at cracked concrete edge,
colors: #8A8580 concrete side, #2A3D2E water side
```

**Variantes:**
- T05a: Centro (agua pura)
- T05b: Borda norte (concreto acima, agua abaixo)
- T05c: Borda sul
- T05d: Borda leste
- T05e: Borda oeste
- T05f: Canto NE
- T05g: Canto NW
- T05h: Canto SE
- T05i: Canto SW

**Animacao (4 frames, 4fps):**
Deslocamento sutil da textura de agua (1px shift circular)

---

### T06 — Asfalto (4 variantes)

**Prompt:**
```
[STYLE PREFIX]
asphalt road tile, top-down view, cracked dark pavement,
old highway road surface with faded yellow center line,
potholed damaged road, urban decay,
colors: #3A3530 dark asphalt, #B8A030 faded yellow stripe,
seamless tileable pattern
```

**Variantes:**
- T06a: Asfalto liso (sem faixa)
- T06b: Asfalto com faixa amarela horizontal
- T06c: Asfalto com faixa amarela vertical
- T06d: Asfalto muito rachado (quase destruido)

---

### T07 — Piso Interno (2 variantes)

**Prompt:**
```
[STYLE PREFIX]
old linoleum office floor tile, top-down view,
faded institutional floor, 1970s government building interior,
subtle grid pattern barely visible, scuff marks from office chairs,
worn out beige-gray floor,
colors: #A09888 base, #8A8580 darker wear marks,
seamless tileable pattern
```

---

### T08 — Carpete Vermelho (2 variantes)

**Prompt:**
```
[STYLE PREFIX]
red carpet floor tile, top-down view, VIP area carpet,
dark maroon government building formal carpet,
woven fabric texture with cross-hatching pattern,
slightly worn luxury carpet, parliament hall floor,
colors: #8B2020 base, #6B1515 shadow, #A03030 highlight,
seamless tileable pattern
```

---

### T09 — Santinhos no Chao (3 variantes)

**Prompt:**
```
[STYLE PREFIX]
scattered political campaign flyers on floor, top-down view,
small paper rectangles littered on ground, Brazilian election debris,
campaign pamphlets scattered randomly, "VOTE" text barely visible,
cream-colored papers with faded text on gray concrete,
colors: #F0E8D0 papers on #8A8580 concrete background,
seamless tileable pattern
```

**Variantes:**
- T09a: 3-5 papeis espalhados (pouco)
- T09b: 8-12 papeis (muito)
- T09c: Amontoado denso (quase cobrindo o chao)

---

### T10 — Grama com Emenda (2 variantes)

**Prompt:**
```
[STYLE PREFIX]
official government papers scattered on dead grass, top-down view,
legal documents with gold seals on dry yellow lawn,
parliamentary amendment papers littered on ground,
larger papers than campaign flyers with official stamps,
colors: #E8D8B0 papers with #C8A832 gold seals on #C4A265 grass,
seamless tileable pattern
```

---

## 2. Landmarks

### Blocos Ministeriais (M1-M5)

**Prompt:**
```
[STYLE PREFIX]
brutalist government building, top-down view,
Oscar Niemeyer inspired concrete ministry block,
rectangular building with columns and dark empty windows,
windows look like dead eyes, concrete pillars at ground level,
satirical sign on front, imposing modernist architecture,
colors: #8A8580 concrete, #1A1A18 dark windows,
pixel art building sprite, 48x64 pixels, 3 tiles wide by 4 tiles tall
```

**Placa satirica (sprite separado 32x8px por ministerio):**
- M1: "MIN. DA ENROLACAO"
- M2: "MIN. DO PUXADINHO"
- M3: "MIN. DA PROMESSA NAO CUMPRIDA"
- M4: "MIN. DO JEITINHO"
- M5: "MIN. DA PLANILHA INFINITA"

Placa: fundo `#2A5A3A`, texto `#F0E8D0`, borda `#1A1A18`

---

### Eixo Monumental

**Prompt:**
```
[STYLE PREFIX]
wide cracked highway corridor, top-down view,
central ceremonial avenue with faded yellow center line,
cracked asphalt flanked by dead grass,
toppled light posts on sides, papers blowing across,
monumental scale urban decay, government district main road,
colors: #3A3530 asphalt, #B8A030 faded stripe, #C4A265 grass sides,
32 pixels wide corridor (2 tile widths), seamless vertical scroll
```

---

### Espelho D'Agua

**Prompt:**
```
[STYLE PREFIX]
polluted reflecting pool, top-down view,
murky dark green-black water, stagnant government reflecting pool,
dead fish floating on surface (small white shapes),
distorted greenish reflection of distant building,
concrete border around pool, oppressive atmosphere,
colors: #2A3D2E water, #3D6B3A green tint, #8A8580 concrete border,
rectangular pool sprite, 6 tiles wide by 3 tiles tall
```

---

### Congresso Nacional (Background)

**Prompt:**
```
[STYLE PREFIX]
Brazilian National Congress building silhouette, front view,
two distinctive domes (one concave bowl, one convex dome),
twin towers between the domes, iconic Niemeyer architecture,
dark silhouette against orange-red sky, sinister green glow between towers,
pixel art building, 128x48 pixels,
colors: #1A1A18 building silhouette, #3D6B3A green glow,
#FF6B35 to #8B0000 gradient sky behind
```

---

### Cabine de Votacao

**Prompt:**
```
[STYLE PREFIX]
toppled electronic voting booth, top-down view,
Brazilian voting machine fallen on side, exposed wires,
cracked plastic shell, small screen showing static,
democracy abandoned aesthetic,
colors: #4A4A4A gray machine, #CC6600 copper wires, #1A1A18 screen,
pixel art sprite, 16x16 pixels
```

---

### Helicoptero IBAMA

**Prompt:**
```
[STYLE PREFIX]
crashed helicopter on its side, top-down view,
green-brown military/environmental helicopter wreck,
twisted rotor blades, cracked windshield,
"IBAMA" barely visible on fuselage, rust and decay,
colors: #4A6B3A green-brown body, #8B4513 rust, #5C5C55 metal,
pixel art sprite, 48x32 pixels (3 tiles wide by 2 tiles tall)
```

---

### Ambulancia SUS

**Prompt:**
```
[STYLE PREFIX]
crashed ambulance van, top-down view,
white ambulance with red cross dented and battered,
weak flashing red light on top, row of plastic chairs next to it,
satirical waiting line setup even in apocalypse,
colors: #E8E0D0 dirty white body, #CC3030 cross and siren,
pixel art sprite, 32x16 pixels (2 tiles wide)
```

---

### Buffet de Gala

**Prompt:**
```
[STYLE PREFIX]
fancy banquet table aftermath, top-down view,
long table with stained white tablecloth,
half-eaten lobster, spilled champagne glasses,
politician party leftovers, decadent feast remains,
colors: #E8E0D0 tablecloth with #8B0000 stains, #C8A832 champagne,
pixel art sprite, 32x16 pixels
```

---

### Palanque Eleitoral

**Prompt:**
```
[STYLE PREFIX]
campaign rally stage, top-down view,
small wooden stage with microphone stand,
torn political banners and flags from all parties,
red blue green yellow flags all mixed and tattered,
cheap wood construction, speaker equipment,
colors: #6B4423 wood, mixed flag colors all faded,
pixel art sprite, 32x32 pixels (2x2 tiles)
```

---

## 3. Cenario do Limbo (Game Over)

### Void Escuro

**Prompt:**
```
[STYLE PREFIX]
infinite dark void background, subtle floating particles,
pure black emptiness with faint gray dust motes,
existential void, limbo space,
colors: #0A0A0A background, #2A2A2A particles at 40% opacity,
tileable dark background
```

### Podcast Flutuante

**Prompt:**
```
[STYLE PREFIX]
floating podcast recording desk in dark void, 
desk with two microphones and headphones,
green-tinted spotlight illuminating from above,
surreal floating furniture in emptiness,
colors: #3D6B3A green light, #0A0A0A void,
pixel art sprite, 48x32 pixels
```

### Cadeira Monark

**Prompt:**
```
[STYLE PREFIX]
single gaming chair floating in dark void,
orange-tinted spotlight from below,
comfortable chair spinning slowly in emptiness,
surreal limbo furniture,
colors: #D47820 orange glow, #0A0A0A void, #4A4A4A chair,
pixel art sprite, 16x32 pixels
```

---

## 4. Particulas e Efeitos

### Gas Verde (8x8px)

**Prompt:**
```
[STYLE PREFIX]
small green gas particle, soft diffuse circle,
toxic green mist particle, no hard edges,
glowing faintly, translucent,
colors: #4A7C59 center fading to transparent,
8x8 pixels, alpha gradient from center
```

### Santinho Voando (16x16, sprite sheet 4 frames)

**Prompt:**
```
[STYLE PREFIX]
political campaign flyer rotating in wind, 4 animation frames,
small cream paper rectangle tumbling through air,
frame 1: front view (flat), frame 2: 45-degree tilt,
frame 3: edge-on (thin line), frame 4: opposite 45-degree tilt,
colors: #F0E8D0 paper with faint text lines,
16x16 pixel sprite sheet, 4 frames horizontal strip = 64x16 total
```

### Tinta-Sangue Splat (16x16, 3 variantes)

**Prompt:**
```
[STYLE PREFIX]
cartoon ink blood splatter on ground, top-down view,
stylized blood like spilled red ink NOT realistic,
Robert Crumb comic style blood splash,
amorphous blob shape with irregular edges,
colors: #8B1A1A red-ink on transparent background,
16x16 pixel sprite, 3 shape variations
```

### Explosao de Morte (32x32, 6 frames)

**Prompt:**
```
[STYLE PREFIX]
zombie death explosion animation, 6 frames,
papers and bureaucratic debris flying outward,
stamps badges ID cards exploding from center,
comic book style explosion with paper confetti,
NOT fire explosion - PAPER explosion,
colors: #F0E8D0 papers, #C8A832 badges, #8A8580 debris,
32x32 pixel sprite sheet, 6 frames = 192x32 total
```

---

## 5. Workflow de Geracao

### Passo a Passo
1. **Gerar em alta resolucao** (256x256 ou 512x512) usando o prompt
2. **Downscale para 16x16** usando nearest-neighbor (NAO bilinear)
3. **Aplicar paleta restrita** — max 8 cores por tile (ver color-palette.md)
4. **Adicionar outlines** — 1px contorno `#1A1A18` onde necessario
5. **Cross-hatching manual** — sombras com linhas diagonais, NAO gradiente
6. **Textura de papel** — overlay noise monocromatico 3-5%
7. **Teste de seamless** — colocar 4x4 tiles juntos, verificar repeticao
8. **Teste de legibilidade** — deve funcionar a 2x e 3x scale
9. **Export** — PNG-8 com transparencia, sem anti-aliasing

### Ferramentas Recomendadas
| Etapa | Ferramenta |
|---|---|
| Geracao base | Stable Diffusion XL (local) ou DALL-E 3 |
| Pixel editing | Aseprite (principal) ou Photoshop |
| Paleta | Aseprite palette editor |
| Tilemap | Tiled Map Editor |
| Teste in-game | Phaser 3 dev server (Vite) |
| Sprite sheet packing | TexturePacker ou Aseprite batch export |
