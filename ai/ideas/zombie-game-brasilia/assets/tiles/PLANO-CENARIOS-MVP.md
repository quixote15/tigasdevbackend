# Plano de Cenarios e Tiles — MVP 2 Semanas

**Jogo:** Zumbis de Brasilia
**Cenario MVP:** Esplanada dos Ministerios (unico mapa)
**Mapa:** 960x640px (60x40 tiles de 16x16)
**Engine:** Phaser 3 (WebGL), top-down com Y-sorting
**Tileset max:** 512x512px
**Ferramenta:** PixelLab MCP (create_topdown_tileset, create_tiles_pro, create_map_object)
**Estilo:** Andre Guedes grotesco — cores sujas, outlines irregulares, textura de papel, cross-hatching

---

## Resumo do Mapa MVP

```
NORTE ────────────────────────────────────────── CONGRESSO (background)
  |  [M1] [M2] [M3] [M4] [M5]  ← Ministerios (chokepoints)
  |  ═══ CONCRETO RACHADO ═══
  |  ═══ EIXO MONUMENTAL (asfalto) ═══
  |  ═══ CONCRETO ═══
  |  ~~~~~ ESPELHO D'AGUA (kill zone) ~~~~~
  |  ═══ CONCRETO ═══
  |  [H] [V] [U] [B] [P]  ← Landmarks interativos
SUL ─────────────────────────────────────── SPAWN DO JOGADOR (grama)
```

---

## FASE 1: Base Tiles (Semana 1, Dias 1-3)

### Prioridade CRITICA — Sem estes, nao ha jogo

#### 1.1 Tileset: Concreto Rachado ↔ Grama Seca
**Ferramenta:** `create_topdown_tileset` (Wang autotile — 16 tiles de transicao)
**Prioridade:** P0 — PRIMEIRO a gerar

| Parametro | Valor |
|-----------|-------|
| lower_description | "cracked dirty gray concrete sidewalk with dark stains and fine irregular cracks, brutalist architecture floor, Brasilia esplanade, apocalyptic decay" |
| upper_description | "dry dead yellow-brown grass lawn with sparse tufts and bare earth patches, drought-stricken Brazilian cerrado, desiccated" |
| transition_description | "broken concrete edge crumbling into dry dirt and dead grass, debris and rubble at the border" |
| transition_size | 0.5 |
| tile_size | {"width": 16, "height": 16} |
| view | "high top-down" |
| shading | "medium shading" |
| outline | "selective outline" |
| detail | "medium detail" |

**Resultado:** 16 tiles (concreto puro, grama pura, + 14 transicoes)
**Uso no mapa:** 70% da area jogavel

#### 1.2 Tileset: Concreto ↔ Asfalto (Eixo Monumental)
**Ferramenta:** `create_topdown_tileset`
**Prioridade:** P0

| Parametro | Valor |
|-----------|-------|
| lower_description | "dark cracked asphalt road with faded yellow center line marking, abandoned highway, Brasilia monumental axis" |
| upper_description | "cracked dirty gray concrete sidewalk, brutalist Brasilia esplanade floor" |
| transition_description | "concrete curb edge transitioning to damaged asphalt road with debris" |
| transition_size | 0.25 |
| tile_size | {"width": 16, "height": 16} |
| view | "high top-down" |
| shading | "medium shading" |
| outline | "selective outline" |

**Resultado:** 16 tiles
**Uso:** Eixo Monumental (faixa central do mapa, rows 14-18)
**Conectar:** usar `lower_base_tile_id` do concreto do tileset 1.1

#### 1.3 Tileset: Concreto/Grama ↔ Agua Turva (Espelho D'Agua)
**Ferramenta:** `create_topdown_tileset`
**Prioridade:** P0

| Parametro | Valor |
|-----------|-------|
| lower_description | "dark murky stagnant green-black water, opaque polluted reflecting pool, dead fish floating, sickly toxic appearance" |
| upper_description | "cracked gray concrete edge with drainage, Brasilia reflecting pool border" |
| transition_description | "concrete edge crumbling into murky dark water, algae growth, slime on stone" |
| transition_size | 0.5 |
| tile_size | {"width": 16, "height": 16} |
| view | "high top-down" |
| shading | "medium shading" |
| outline | "selective outline" |

**Resultado:** 16 tiles
**Uso:** Espelho D'Agua (barreira central, rows 22-26)
**Propriedades:** agua = NOT walkable, collision: true, damage_zone: true

#### 1.4 Tileset: Grama ↔ Asfalto
**Ferramenta:** `create_topdown_tileset`
**Prioridade:** P1

| Parametro | Valor |
|-----------|-------|
| lower_description | "dark cracked asphalt road, abandoned Brazilian highway" |
| upper_description | "dry dead yellow grass lawn, drought cerrado" |
| transition_description | "asphalt road edge decaying into dry grass and weeds growing through cracks" |
| transition_size | 0.25 |
| tile_size | {"width": 16, "height": 16} |

**Resultado:** 16 tiles
**Uso:** Bordas laterais do Eixo Monumental

---

## FASE 2: Tiles Extras e Variantes (Semana 1, Dias 3-5)

#### 2.1 Tiles Pro: Variantes de piso
**Ferramenta:** `create_tiles_pro` (square_topdown)
**Prioridade:** P1

```
Descricao: "1). cracked concrete with blood-ink red stains 2). concrete with scattered election 
leaflets cream-colored papers 3). dry grass with blood-ink stains 4). grass with scattered 
parliamentary amendment papers with gold seals 5). asphalt with faded yellow lane marking 
6). cracked asphalt with pothole"
```

| Parametro | Valor |
|-----------|-------|
| tile_type | "square_topdown" |
| tile_size | 16 |
| tile_view | "high top-down" |
| outline_mode | "segmentation" |

**Resultado:** 6 tiles decorativos para variar o visual
**Uso:** Espalhados pelo mapa para quebrar repeticao

#### 2.2 Tiles Pro: Pisos internos (Ministerios)
**Ferramenta:** `create_tiles_pro`
**Prioridade:** P2

```
Descricao: "1). old worn institutional linoleum floor faded gray with grid pattern 
2). stained dark red carpet with fabric texture cross-hatching 
3). linoleum with overturned chair shadow 
4). red carpet with indeterminate dark stains"
```

| Parametro | Valor |
|-----------|-------|
| tile_type | "square_topdown" |
| tile_size | 16 |
| tile_view | "high top-down" |

**Resultado:** 4 tiles
**Uso:** Interior dos ministerios (se MVP incluir entrada)
**Nota:** Pode ser cortado do MVP se tempo apertar

---

## FASE 3: Background e Landmarks (Semana 1, Dias 4-7)

### 3.1 Background: Ceu Apocaliptico
**Ferramenta:** Gerado via CSS/Phaser (NAO precisa de PixelLab)
**Prioridade:** P0

```css
/* Ceu permanente 15h de abril — o apocalipse congelou Brasilia */
background: linear-gradient(to top, #FF6B35 0%, #8B0000 45%, #2D0A0A 100%);
```

- Layer 0 (background fixo)
- scrollFactor: 0 (nao se move com camera)

### 3.2 Background: Silhueta do Congresso Nacional
**Ferramenta:** `create_map_object`
**Prioridade:** P0

| Parametro | Valor |
|-----------|-------|
| description | "Silhouette of Brazilian National Congress building in Brasilia, Oscar Niemeyer brutalist architecture. Two tall rectangular twin towers in center, concave dome on left (Chamber of Deputies like inverted bowl), convex dome on right (Senate like half sphere). Dark almost-black silhouette against orange-red apocalyptic sky. Sinister green glow emanating between the towers. Pixel art game background sprite. Simplified iconic shape." |
| width | 256 |
| height | 96 |
| view | "side" |
| outline | "single color outline" |
| shading | "basic shading" |
| detail | "medium detail" |

- scrollFactor: 0.3 (parallax lento)
- Depth: -999
- PointLight verde (#3D6B3A) entre as torres, pulsa 0.2-0.9 conforme wave

### 3.3 Blocos dos Ministerios (M1-M5)
**Ferramenta:** `create_map_object` (1 bloco generico + 5 placas)
**Prioridade:** P0

**Bloco base (48x64px):**

| Parametro | Valor |
|-----------|-------|
| description | "Brazilian ministry building block top-down view, Oscar Niemeyer brutalist concrete architecture. Rectangular gray concrete block with dark black window rows (dead eyes), ground level has pilotis columns with center door opening. Flat roof. Institutional gray concrete with dark stains. Pixel art game building, grotesque underground comix style. Top-down perspective." |
| width | 48 |
| height | 64 |
| view | "high top-down" |
| outline | "single color outline" |
| shading | "medium shading" |
| detail | "high detail" |

**Variante danificada (wave 10+):**
- Mesmo bloco + rachaduras, janelas quebradas, gas verde, panfletos grudados

**Placas satiricas (5x, como map_objects 32x8px cada):**

| Ministerio | Texto da Placa |
|------------|---------------|
| M1 | "MIN. DA ENROLACAO" |
| M2 | "MIN. DO PUXADINHO" |
| M3 | "MIN. DA PROMESSA NAO CUMPRIDA" |
| M4 | "MIN. DO JEITINHO" |
| M5 | "MIN. DA PLANILHA INFINITA" |

### 3.4 Landmarks Interativos
**Ferramenta:** `create_map_object`
**Prioridade:** P1

| # | Landmark | Size | Descricao PixelLab | Funcao no Jogo |
|---|----------|------|--------------------|----------------|
| L1 | Ambulancia SUS | 48x32 | "Abandoned white ambulance van with red cross and SUS (Brazilian health system) logo, rusted, one door open, weak pulsing red siren on top, pixel art grotesque style, top-down view" | Cura 10 HP/s apos 3s |
| L2 | Cabine de Votacao | 32x32 | "Toppled electronic Brazilian voting booth (urna eletronica), gray institutional box tipped on its side, exposed wires orange, cracked screen, pixel art grotesque style, top-down" | Spawn de power-up 1x/wave |
| L3 | Buffet Abandonado | 48x32 | "Abandoned gala dinner buffet table with dirty white tablecloth with blood-ink stains, toppled champagne glasses, scattered gold cutlery, half-eaten food, pixel art grotesque top-down" | 2x score por 5s |
| L4 | Helicoptero IBAMA | 48x32 | "Crashed green IBAMA helicopter (Brazilian environmental agency), rotor broken, rusted, tilted on side, overgrown with dry grass, pixel art grotesque style, top-down view" | Cobertura contra projeteis |
| L5 | Palanque Eleitoral | 32x32 | "Cheap wooden electoral rally platform/stage with broken microphone, torn mixed-color political flags (red green yellow blue all together), scattered campaign signs, pixel art grotesque top-down" | Arena do Boss (wave 5+) |
| L6 | Barraca de Hot Dog | 32x32 | "Brazilian hot dog street vendor cart abandoned, colorful umbrella torn, condiment bottles scattered, steam still rising, warm inviting glow, pixel art grotesque style, top-down" | Zona de cura alternativa |

---

## FASE 4: Decoracoes e Particulas (Semana 2, Dias 8-10)

### 4.1 Objetos Decorativos
**Ferramenta:** `create_map_object` (16x16 ou 32x16)
**Prioridade:** P2

| # | Objeto | Size | Descricao |
|---|--------|------|-----------|
| D01 | Poste de luz caido | 16x32 | "Fallen metal street light pole lying on ground, bent, wires exposed, pixel art top-down" |
| D02 | Placa de campanha | 16x16 | "Political campaign sign stuck in ground like cemetery marker, torn poster, pixel art top-down" |
| D03 | Banco quebrado | 32x16 | "Destroyed concrete park bench, broken in half, graffiti, pixel art top-down" |
| D04 | Lixeira transbordando | 16x16 | "Overflowing public trash can with papers and bureaucratic waste spilling out, pixel art top-down" |
| D05 | Cone de transito | 16x16 | "Orange traffic cone on cracked asphalt, tilted, pixel art top-down" |
| D06 | Cratera pequena | 16x16 | "Small ground crater/pothole with dark center, cracked edges, pixel art top-down" |
| D07 | Pegadas verdes | 16x16 | "Glowing sickly green zombie footprints on ground, 3-4 footsteps, translucent, pixel art top-down" |
| D08 | Mancha de gas | 16x16 | "Toxic green gas stain on concrete floor, translucent sickly green, pixel art top-down" |
| D09 | Aspersores quebrados | 16x16 | "Broken irrigation sprinkler head on dry grass, symbol of abandonment, pixel art top-down" |
| D10 | Barricada improvisada | 32x16 | "Improvised barricade made of overturned desks and filing cabinets, bureaucratic debris, pixel art top-down" |

### 4.2 Sprites de Particulas (Sprite Sheets)
**Ferramenta:** `create_tiles_pro` ou manual
**Prioridade:** P2

| Particula | Frames | Size | Cor Base |
|-----------|--------|------|----------|
| Gas Emenda 666 | 1 (diffuse) | 8x8 | #4A7C59 alpha 40% |
| Panfleto voando | 4 (rotacao) | 16x16 | #F0E8D0 |
| Fragmento de papel | 1 | 2x3 | #E8E0D0 |
| Poeira | 1 | 4x4 | #C4A265 alpha 30% |
| Folha seca | 2 | 8x8 | #8B6914 |

---

## FASE 5: Montagem do Mapa (Semana 2, Dias 10-12)

### 5.1 Tiled Map Editor — Assembly

**Layers (ordem de renderizacao):**

| Layer | Tipo | Conteudo |
|-------|------|----------|
| 0 - sky | Image | Gradiente CSS (nao tilemap) |
| 1 - congress | Image | Sprite do Congresso (parallax 0.3) |
| 2 - ground_base | Tile | Concreto, grama, asfalto, agua |
| 3 - ground_detail | Tile | Variantes com sangue, panfletos, marcas |
| 4 - shadows | Tile | Sombras dos ministerios (alpha 25%) |
| 5 - buildings | Object | Ministerios M1-M5 + placas |
| 6 - landmarks | Object | Ambulancia, helicoptero, cabine, buffet, palanque, hot dog |
| 7 - decorations | Object | Postes, bancos, lixeiras, cones, crateras |
| 8 - entities | (runtime) | Jogador + zumbis (Y-sorted) |
| 9 - particles | (runtime) | Gas, panfletos, poeira |
| 10 - vfx | (runtime) | Onomatopeias, dano, efeitos |
| 11 - hud | (runtime) | UI fixa (camera separada) |

### 5.2 Collision Map

| Tile/Objeto | Walkable | Speed Mod | Collision | Kill Zone |
|-------------|----------|-----------|-----------|-----------|
| Concreto | sim | 1.0 | nao | nao |
| Grama | sim | 0.85 | nao | nao |
| Asfalto | sim | 1.0 | nao | nao |
| Agua | NAO | 0 | SIM | SIM |
| Ministerio (paredes) | NAO | 0 | SIM | nao |
| Ministerio (porta) | sim | 1.0 | nao | nao |
| Landmarks | parcial | 1.0 | parcial | nao |
| Decoracoes grandes | NAO | 0 | SIM | nao |
| Decoracoes pequenas | sim | 1.0 | nao | nao |

### 5.3 Spawn Zones (Object Layer no Tiled)

| Zona | Ativacao | Tiles (X,Y) | Max Simultaneo |
|------|----------|-------------|----------------|
| Bordas laterais | Wave 1+ | X:0 e X:59, Y:0-40 | 5/lado |
| Norte | Wave 1+ | Y:0, X:5-55 | 8 |
| Portas ministerios | Wave 3+ | Frente de cada M | 2/ministerio |
| Sul | Wave 5+ | Y:39, X:10-50 | 6 |
| Centro (pos-agua) | Wave 8+ | Y:28-30, X:20-40 | 4 |

---

## FASE 6: Polish e Atmosfera (Semana 2, Dias 12-14)

### 6.1 Efeitos Dinamicos (Phaser 3)

| Efeito | Implementacao | Prioridade |
|--------|--------------|------------|
| Pulso verde do Congresso | PointLight #3D6B3A, 3s cycle, intensifica por wave | P0 |
| Sombras dos ministerios | Tiles alpha 25%, direcao NE→SW | P1 |
| Particulas de gas | 3-5/s, 8x8px, blend ADD, drift horizontal | P1 |
| Panfletos voando | 1-2/s, 16x16px 4-frame, vento horizontal | P1 |
| Reflexo distorcido na agua | Overlay sprite do Congresso invertido, wobble shader | P2 |
| Paper texture overlay | Noise 3-5% opacity sobre tudo | P2 |
| Rachadura progressiva | Tiles de concreto trocam para variante danificada em waves altas | P3 |

### 6.2 Audio Zones (referencia)

| Zona | Wind | Sirens | AC | Speeches |
|------|------|--------|----|----------|
| Gramados | 100% | 50% | 0% | 30% |
| Eixo Monumental | 80% | 80% | 0% | 50% |
| Perto Ministerios | 40% | 30% | 100% | 80% |
| Perto Agua | 60% | 20% | 0% | 20% |
| Perto Congresso | 30% | 100% | 50% | 100% |

---

## CRONOGRAMA DE GERACAO (PixelLab)

### Semana 1

| Dia | Task | Ferramenta | Tiles |
|-----|------|------------|-------|
| D1 | Tileset Concreto↔Grama | create_topdown_tileset | 16 |
| D1 | Tileset Concreto↔Asfalto | create_topdown_tileset | 16 |
| D2 | Tileset Concreto↔Agua | create_topdown_tileset | 16 |
| D2 | Tileset Grama↔Asfalto | create_topdown_tileset | 16 |
| D3 | Tiles Pro variantes (sangue, panfletos) | create_tiles_pro | 6 |
| D3 | Tiles Pro pisos internos | create_tiles_pro | 4 |
| D4 | Silhueta Congresso | create_map_object | 1 sprite |
| D4 | Bloco Ministerio (base + danificado) | create_map_object | 2 sprites |
| D5 | 6 Landmarks interativos | create_map_object | 6 sprites |
| D6-7 | Montagem tileset 512x512 + testes | Manual/Tiled | — |

### Semana 2

| Dia | Task | Ferramenta | Output |
|-----|------|------------|--------|
| D8 | 10 objetos decorativos | create_map_object | 10 sprites |
| D9 | Sprites de particulas | create_tiles_pro | 5 sprite sheets |
| D10-11 | Montagem mapa no Tiled | Tiled Editor | esplanada.json |
| D12 | Collision map + spawn zones | Tiled Editor | collision layer |
| D13 | Efeitos dinamicos (Phaser) | Codigo | shaders + particulas |
| D14 | Polish, teste, ajustes | QA | — |

---

## INVENTARIO TOTAL DE ASSETS

| Categoria | Quantidade | Ferramenta |
|-----------|-----------|------------|
| Wang tilesets (16 tiles cada) | 4 sets = 64 tiles | create_topdown_tileset |
| Tiles variantes | 10 tiles | create_tiles_pro |
| Background (Congresso) | 1 sprite 256x96 | create_map_object |
| Ministerios | 2 sprites 48x64 (base + dano) | create_map_object |
| Landmarks interativos | 6 sprites | create_map_object |
| Objetos decorativos | 10 sprites | create_map_object |
| Sprites de particulas | 5 sprites/sheets | create_tiles_pro |
| **TOTAL** | **~74 tiles + 19 sprites** | |

### Tileset Final (512x512px, 16x16 grid = 1024 slots)

```
Slots usados: ~74 tiles
Slots livres: ~950 (expansao futura — novos cenarios, waves, etc.)
```

---

## REGRAS DE ESTILO (Checklist de Qualidade)

- [ ] NENHUMA cor pura (#FF0000, #00FF00, #0000FF) — tudo "sujo"
- [ ] Outlines irregulares 2-3px (nunca uniformes)
- [ ] Sombras com cross-hatching diagonal (NUNCA gradiente)
- [ ] Textura de papel sutil (noise 3-5% opacity)
- [ ] Sangue como TINTA VERMELHA (Robert Crumb), nao realista
- [ ] Tiles fazem tiling seamless em 8x8 minimo
- [ ] Cores politicas NUNCA isoladas (vermelho, verde, amarelo sempre JUNTAS)
- [ ] Brasilia = opressiva, decadente, mas COMICA (horror-comedy)
- [ ] "Se parece que saiu de AI generica ou asset store, voce falhou"
- [ ] O imperfeito e o estilo. A sujeira e a identidade.

---

## PROXIMOS PASSOS

1. **Executar Fase 1** — Gerar os 4 Wang tilesets base com PixelLab
2. Montar tileset PNG 512x512 combinando todos os tiles
3. Gerar landmarks e Congresso
4. Montar mapa no Tiled Map Editor
5. Integrar com Phaser 3
6. Adicionar particulas e efeitos
7. Testar no Samsung Galaxy A06 (target device)
