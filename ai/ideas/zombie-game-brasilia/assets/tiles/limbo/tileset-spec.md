# Tileset Spec — LIMBO DOS CANCELADOS

> Mapa especial: Game Over / Loja do Limbo. Cenario do podcast Monark + Arthur do Val.
> O OPOSTO da Esplanada — sem concreto, sem arquitetura. Apenas VOID com podcast flutuante.
> Todos os tiles: 16x16px, PNG com transparencia, seamless.
> Tileset unico para Phaser 3: max 256x256px (16x16 tiles = 256 tiles possiveis).
> Mapa menor que Esplanada (tela unica, sem scrolling — e um cenario de Game Over, nao arena).

---

## 1. Dimensoes e Grid

| Parametro | Valor |
|---|---|
| **Tile size** | 16x16 pixels |
| **Tileset image** | 256x256px (max) |
| **Tiles por linha** | 16 |
| **Total de tiles possiveis** | 256 (16x16) |
| **Tiles planejados** | ~80 tiles (base + variantes + props + efeitos) |
| **Formato** | PNG-8 com transparencia |
| **Ferramenta de edicao** | Tiled Map Editor (export JSON para Phaser 3) |
| **Perspectiva** | Top-down (mesmo do jogo, mas cenario e mais "flat" — void infinito) |
| **Tamanho do mapa** | 20x15 tiles (320x240px real, escalado para tela) — tela unica |

---

## 2. Conceito Visual do Limbo

### Filosofia
O Limbo e o ANTI-CENARIO. Enquanto a Esplanada e cheia de concreto, grama, agua, landmarks e detalhes, o Limbo e o VAZIO. A tensao visual vem do NADA interrompido por poucos objetos significativos flutuando.

### Regras Visuais
1. **90% do mapa e void** — escuridao com variacao sutil
2. **Props flutuam** — nada toca "chao" (nao ha chao)
3. **Iluminacao e pontual** — apenas os objetos emitem luz/glow
4. **Cores: paleta do Limbo** (ver color-palette.md secao 7)
5. **SEM paredes** — o void e infinito em todas as direcoes
6. **SEM horizonte** — nao ha ceu vs chao, tudo e o MESMO nada
7. **Atmosfera de podcast underground** — equipamento de audio e a unica referencia "real"

### Contraste com Esplanada
| Aspecto | Esplanada | Limbo |
|---|---|---|
| Chao | Concreto, grama, asfalto | Void (nada) |
| Paredes | Ministerios, muros | Nenhuma (infinito) |
| Luz | Ceu laranja-sangue | Sem ceu (escuridao total) |
| Cor dominante | Laranja/verde/cinza | Preto/cinza muito escuro |
| Elementos | Centenas de tiles, landmarks, decoracoes | Poucos objetos isolados no nada |
| Atmosfera | Apocalipse urbano caotico | Solidao cosmica humoristica |
| Vida | Zumbis, particulas, vento | Estatico com particulas sutis |

---

## 3. Tiles Base — VOID (O "Chao" do Limbo)

O void nao e preto uniforme. Tem variacao SUTIL para evitar flat digital e criar profundidade.

### L01 — Void Puro
- **Funcao**: Tile base principal — a "escuridao" do Limbo
- **Cores**: `#0A0A0A` base com noise sutil
- **Variantes**: 4 (patterns de noise diferentes para evitar repeticao)
- **Propriedades Phaser**: walkable, no collision
- **Detalhes**: NAO e preto puro (#000000). E preto sujo (#0A0A0A) com noise gaussiano monocromatico de 2-3% opacity. Cada variante tem distribuicao de noise diferente.
- **IDs**: L01a, L01b, L01c, L01d

### L02 — Void com Particulas
- **Funcao**: Areas do void com particulas flutuantes pintadas (nao emitter)
- **Cores**: `#0A0A0A` base + `#2A2A2A` alpha 40% particulas
- **Variantes**: 4 (particulas em posicoes diferentes)
- **Propriedades Phaser**: walkable, no collision
- **Detalhes**: 2-3 pontos de `#2A2A2A` por tile (1x1px ou 2x1px) simulando poeira do void. Distribuicao aleatoria por variante.
- **IDs**: L02a, L02b, L02c, L02d

### L03 — Void com Veias de Energia
- **Funcao**: Linhas tenues de energia cruzando o void (como circuitos do alem)
- **Cores**: `#0A0A0A` base + `#3D6B3A` alpha 15% linhas
- **Variantes**: 4 (linhas em direcoes: horizontal, vertical, diagonal esquerda, diagonal direita)
- **Propriedades Phaser**: walkable, no collision
- **Detalhes**: Linha de 1px em verde MUITO escuro atravessando o tile. Quase invisivel — perceptivel apenas quando varios tiles se alinham formando "circuitos". As linhas se conectam entre tiles adjacentes (seamless obrigatorio).
- **IDs**: L03a (H), L03b (V), L03c (DE), L03d (DD)

### L04 — Void Gradiente (Bordas do Podcast Light)
- **Funcao**: Transicao entre void puro e area iluminada pelo podcast
- **Cores**: `#0A0A0A` para `#1A1A18` gradiente sutil
- **Variantes**: 4 (gradiente vindo do norte, sul, leste, oeste)
- **Propriedades Phaser**: walkable, no collision
- **Detalhes**: Gradiente MUITO sutil — apenas 10% de diferenca de luminosidade. Dithering em vez de gradiente suave (consistente com estetica do jogo).
- **IDs**: L04a (grad-N), L04b (grad-S), L04c (grad-E), L04d (grad-W)

### L05 — Void Iluminado (Podcast Zone)
- **Funcao**: Area mais clara onde a luz do podcast alcanca (zona central do mapa)
- **Cores**: `#1A1A18` base com dithering para `#0A0A0A`
- **Variantes**: 2 (centro mais claro, borda mais escura)
- **Propriedades Phaser**: walkable, no collision
- **Detalhes**: A area MAIS CLARA do mapa inteiro e `#1A1A18` — que ainda e MUITO escuro. A "iluminacao" e relativa. O podcast emite uma luz fraquissima que mal ilumina nada.
- **IDs**: L05a (centro), L05b (borda)

---

## 4. Tiles de Props — Equipamento de Podcast Flutuante

Props que NAO sao tiles de chao — sao objetos SOBRE o void. Desenhados como sprites que ocupam multiplos tiles. Renderizados em layer separada.

### P01 — Mesa de Podcast (Destruida)
- **Funcao**: Mesa onde ficaria equipamento — tombada, flutuando, partida ao meio
- **Tamanho**: 48x32px (3x2 tiles)
- **Cores**: `#6B4423` madeira + `#1A1A18` pernas + `#5C5C5C` metal
- **Detalhes**: Mesa retangular partida em diagonal. Metade inclinada pra um lado, metade pro outro. Parafusos visiveis. Marcas de arranhao. Papeis colados na superficie (stickers de podcast).
- **Propriedades**: collision: false (decoracao flutuante, jogador "passa por baixo" visualmente)
- **Animacao**: Leve rotacao (tween de 0.5 grau, bob vertical de 1px, periodo 4s)

### P02 — Microfone Quebrado (Flutuante)
- **Funcao**: Microfones de condensador destruidos flutuando pelo void
- **Tamanho**: 16x32px (1x2 tiles)
- **Cores**: `#5C5C5C` corpo + `#8A8A8A` grade + `#3A3A3A` cabo cortado
- **Variantes**: 3 (inteiro mas sem cabo, partido ao meio, so a grade)
- **Detalhes**: Cabo de audio cortado pendendo (fios de 1px em `#CC6600`). Grade amassada. Espuma interna visivel (`#3A3A3A`). Um tem mancha de sangue (`#8B0000`).
- **Propriedades**: collision: false (decoracao)
- **IDs**: P02a (inteiro sem cabo), P02b (partido), P02c (so grade)

### P03 — Cadeira de Podcast (Abandonada)
- **Funcao**: Cadeiras de convidados do podcast — vazias, flutuando, tombadas
- **Tamanho**: 16x32px (1x2 tiles)
- **Cores**: `#1A1A18` corpo + `#3A3A3A` estofado + `#5C5C5C` rodinhas
- **Variantes**: 2 (tombada lateral, tombada pra tras)
- **Detalhes**: Cadeira gamer barata (nao a do Monark — essa e de convidados). Rasgos no estofado. Uma rodinha faltando. Etiqueta de preco ainda pendurada (preco: "SUA ALMA").
- **Propriedades**: collision: true (obstaculo)
- **IDs**: P03a (lateral), P03b (tras)

### P04 — Fones de Ouvido (Flutuando)
- **Funcao**: Headphones de estudio flutuando abertos no void
- **Tamanho**: 16x16px (1 tile)
- **Cores**: `#1A1A18` arco + `#3A3A3A` ear pads + `#CC6600` fio
- **Variantes**: 2 (abertos, um pad faltando)
- **Detalhes**: Fio enrolando no void (espiral de 1px). Arco deformado. Ear pad com suor (mancha amarelada).
- **Propriedades**: collision: false
- **IDs**: P04a, P04b

### P05 — Cabos de Audio (Emaranhados)
- **Funcao**: Cachos de cabos XLR/P10 emaranhados flutuando como tentaculos
- **Tamanho**: 32x32px (2x2 tiles)
- **Cores**: `#1A1A18` isolamento + `#CC6600` cobre exposto + `#5C5C5C` conectores
- **Variantes**: 2 (emaranhado solto, emaranhado apertado tipo no)
- **Detalhes**: Cabos se enrolando no void como TENTACULOS. Pontas de conectores XLR visiveis. Fios de cobre expostos. Alguns cabos tem fita adesiva (`#B8A030` prata desbotada).
- **Animacao**: Ondulacao lenta (2 frames alternantes, 2fps)
- **IDs**: P05a (solto), P05b (no)

### P06 — Letreiro "LIMBO" (Neon Flutuante)
- **Funcao**: Placa neon com "LIMBO" — unico texto legivel no cenario. Marca o lugar.
- **Tamanho**: 64x16px (4x1 tiles)
- **Cores**: `#3D6B3A` neon ON + `#1A2A1A` neon OFF + `#5C5C5C` estrutura
- **Detalhes**: Letras em neon verde estilo bar/motel barato. Tubos de neon visiveis (linhas de 2px). Estrutura metalica por tras. O "B" pisca (mau contato — 1 frame ON, 3 frames OFF, ciclo de 2s). Glow difuso ao redor (overlay `#3D6B3A` alpha 20%, raio 8px).
- **Animacao**: 4 frames (tudo ON, "B" OFF, tudo ON, "I" e "B" OFF) a 2fps
- **Propriedades**: collision: false (pendurado/flutuando acima)
- **ID**: P06

### P07 — Selo de "CANCELADO" (Flutuante)
- **Funcao**: Selos vermelhos gigantes de "CANCELADO" flutuando como folhas no void
- **Tamanho**: 16x16px (1 tile)
- **Cores**: `#8B0000` selo + `#E8D8C8` papel + `#1A1A18` texto
- **Variantes**: 3 (reto, inclinado 15deg, inclinado -15deg)
- **Detalhes**: Retangulo de papel creme com selo circular vermelho "CANCELADO" (texto de 1px, quase ilegivel mas reconhecivel). Bordas do papel amassadas. Textura de carimbo (nao clean — borrado).
- **Animacao**: Bob vertical lento (tween, 1px, 3s ciclo)
- **Propriedades**: collision: false
- **IDs**: P07a, P07b, P07c

### P08 — Jornal/Manchete Flutuante
- **Funcao**: Recortes de jornal com manchetes sobre cancelamentos flutuando
- **Tamanho**: 16x16px (1 tile)
- **Cores**: `#E8D8C8` papel amarelado + `#1A1A18` texto (ilegivel) + `#8B0000` manchas
- **Variantes**: 3 (inteiro, rasgado metade, pedaco pequeno)
- **Detalhes**: Papel de jornal com grid de colunas (linhas de 1px), titulo em bold (barra de 2x6px escura), "texto" como linhas horizontais de 1px. Manchas de tinta/sangue. Amassado.
- **Propriedades**: collision: false
- **IDs**: P08a (inteiro), P08b (rasgado), P08c (pedaco)

### P09 — Smartphone Destruido
- **Funcao**: Celulares destruidos (dos cancelados) flutuando no void
- **Tamanho**: 16x16px (1 tile)
- **Cores**: `#1A1A18` corpo + `#4A9ACA` tela rachada + linhas de rachadura `#E8E0D0`
- **Variantes**: 2 (tela rachada, partido ao meio)
- **Detalhes**: Smartphone moderno com tela rachada em teia de aranha. Tela ainda mostrando um brilho azul (ultima mensagem?). Fios internos expostos. Vidro estilhacando (1px branco ao redor).
- **Propriedades**: collision: false
- **IDs**: P09a (rachado), P09b (partido)

### P10 — Cadeira do Monark (Referencia Central)
- **Funcao**: A cadeira de podcast principal do Monark — MARCO CENTRAL do mapa
- **Tamanho**: 32x48px (2x3 tiles)
- **Cores**: `#1A1A18` base + `#D47820` glow + `#3D6B3A` luz podcast
- **Detalhes**: Cadeira gamer premium com encosto alto. Glow laranja emanando de baixo. E o UNICO objeto com glow quente no cenario inteiro. O Monark senta AQUI (sprite do personagem sobrepoe este prop). Bracos da cadeira largos. Rodas flutuando no nada.
- **Propriedades**: collision: false (o Monark senta nela, overlay)
- **ID**: P10

### P11 — Cadeira do Arthur (Referencia Secundaria)
- **Funcao**: A cadeira do co-apresentador — menor, mais simples, sem glow
- **Tamanho**: 16x32px (1x2 tiles)
- **Cores**: `#3A3A3A` base + `#5C5C5C` detalhes (SEM glow)
- **Detalhes**: Cadeira de escritorio basica. Encosto medio. SEM glow. Uma rodinha solta. Arthur senta AQUI. Visualmente INFERIOR a cadeira do Monark.
- **Propriedades**: collision: false (overlay)
- **ID**: P11

---

## 5. Tiles de Atmosfera (Efeitos Pintados)

Efeitos visuais pintados diretamente nos tiles (nao particle emitters — performance em tela de Game Over).

### A01 — Fumaca Eterea (Pintada)
- **Funcao**: Wisps de fumaca verde-cinza pintados em tiles (nao emitter)
- **Tamanho**: 16x16px
- **Cores**: `#6A8A6A` alpha 20-30%
- **Variantes**: 4 (formatos diferentes de wisps)
- **Detalhes**: Formas organicas, NUNCA geometricas. Semi-transparentes. Overlay sobre void.
- **IDs**: A01a, A01b, A01c, A01d

### A02 — Poeira do Void (Pintada)
- **Funcao**: Particulas estaticas pintadas no tile
- **Tamanho**: 16x16px
- **Cores**: `#2A2A2A` alpha 40% pontos
- **Variantes**: 3 (1-2-3 pontos por tile, posicoes diferentes)
- **IDs**: A02a, A02b, A02c

### A03 — Rastro de Luz (Podcast Light Cone)
- **Funcao**: Tiles que formam o cone de luz do podcast quando adjacentes
- **Tamanho**: 16x16px
- **Cores**: `#3D6B3A` alpha 5-15% (MUITO sutil)
- **Variantes**: 6 (borda norte, sul, leste, oeste do cone + centro + corner)
- **Detalhes**: Quando combinados, formam um cone de luz vindo de cima-esquerda. O efeito e QUASE invisivel — apenas 5-15% alpha. O jogador percebe mais pela AUSENCIA de void total do que pela presenca de luz.
- **IDs**: A03a-A03f

### A04 — Glow Laranja (Cadeira do Monark)
- **Funcao**: Tiles com glow laranja que ficam ABAIXO da cadeira do Monark
- **Tamanho**: 16x16px
- **Cores**: `#D47820` alpha 10-25%
- **Variantes**: 4 (centro intenso, borda norte, leste, oeste + cantos)
- **Detalhes**: Radial gradient pintado. Centro sob a cadeira mais intenso (25%), bordas diminuindo (10%). Dithering em vez de gradiente suave.
- **IDs**: A04a (centro), A04b (borda), A04c (canto), A04d (fraco)

### A05 — Papeis de Cancelamento Voando (Animado)
- **Funcao**: Papeis com "CANCELADO" voando lentamente pelo void (spritesheet animado)
- **Tamanho**: 16x16px
- **Frames**: 4 (papel girando lentamente)
- **Cores**: `#E8D8C8` papel + `#8B0000` selo
- **FPS**: 2 (rotacao MUITO lenta no void — nao ha vento, so deriva)
- **Detalhes**: Similar aos santinhos da Esplanada mas MAIS LENTOS e com selo de CANCELADO em vez de propaganda eleitoral. Derivam no void como detritos no espaco.
- **ID**: A05 (spritesheet 64x16, 4 frames)

---

## 6. Composicao do Mapa (20x15 tiles)

### Layout Conceitual
```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ L01 L01 L02 L01 L01 L01 L02 L01 L01 L02 L01 L01 L01 L02 L01 L01 L01 L02 L01 L01  │  Row 0
│ L01 L02 L01 L01 P08 L01 L01 L01 L02 L01 L01 L01 L02 L01 L01 L01 P07 L01 L02 L01  │  Row 1
│ L01 L01 L01 L02 L01 L01 L03 L03 L01 L01 P06 P06 P06 P06 L01 L01 L01 L01 L01 L02  │  Row 2: "LIMBO"
│ L02 L01 L01 L01 L01 L03 L01 L01 L03 L01 L01 L01 L01 L01 L01 P07 L01 L01 L01 L01  │  Row 3
│ L01 L01 P07 L01 L04 L04 L04 L04 L04 L04 L04 L04 L04 L04 L04 L01 L01 P09 L01 L01  │  Row 4
│ L01 L01 L01 L04 L04 A03 A03 A03 A03 A03 A03 A03 A03 A03 L04 L04 L01 L01 L01 P08  │  Row 5
│ L01 P02 L01 L04 A03 A03 L05 L05 L05 L05 L05 L05 L05 A03 A03 L04 L01 L01 L01 L01  │  Row 6
│ L01 L01 L01 L04 A03 L05 L05 A04 P10 P10 A04 P11 L05 L05 A03 L04 L01 P04 L01 L01  │  Row 7: CENTRO
│ L01 L01 L01 L04 A03 L05 L05 A04 P10 P10 A04 P11 L05 L05 A03 L04 L01 L01 L01 L01  │  Row 8: CENTRO
│ L01 L01 L01 L04 A03 A03 L05 L05 P01 P01 P01 L05 L05 A03 A03 L04 L01 L01 P09 L01  │  Row 9: Mesa
│ L01 P05 L01 L04 L04 A03 A03 A03 A03 A03 A03 A03 A03 A03 L04 L04 L01 L01 L01 L01  │  Row 10
│ L01 L01 L01 L01 L04 L04 L04 L04 L04 L04 L04 L04 L04 L04 L04 L01 L01 L01 P07 L01  │  Row 11
│ L02 L01 L01 L01 L01 L01 L03 L01 L01 L03 L01 L01 L01 L01 P08 L01 L01 L01 L01 L02  │  Row 12
│ L01 L01 P08 L01 L02 L01 L01 L01 L01 L01 P05 L01 L01 L02 L01 L01 L01 P02 L01 L01  │  Row 13
│ L01 L02 L01 L01 L01 L02 L01 L01 L02 L01 L01 L01 L01 L01 L02 L01 L01 L01 L02 L01  │  Row 14
└──────────────────────────────────────────────────────────────────────────────────────┘

Legenda:
L01-L05 = Tiles de void (base)
P01-P11 = Props flutuantes
A01-A05 = Tiles de atmosfera
P10     = Cadeira Monark (centro, 2x3)
P11     = Cadeira Arthur (direita do Monark, 1x2)
P06     = Letreiro "LIMBO" (topo, 4x1)
P01     = Mesa de podcast (abaixo das cadeiras, 3x2)
```

### Layers do Tilemap (Tiled Map Editor)
```
Layer 4 (topo):    NPCs (Monark + Arthur — sprites, nao tiles)
Layer 3:           Atmosfera (A01-A05 — fumaca, cone de luz, glow)
Layer 2:           Props superiores (P06 letreiro, P02 mics, P07 selos)
Layer 1:           Props inferiores (P01 mesa, P03 cadeiras, P10-P11 cadeiras NPC)
Layer 0 (base):    Void (L01-L05 — "chao" do Limbo)
```

---

## 7. Propriedades de Collision

Mapa de Game Over — collision e minima (e basicamente uma tela de dialogo/loja, nao uma arena).

| Tile | walkable | collision | Notas |
|---|---|---|---|
| L01-L05 (void) | true | false | Jogador "anda" no void |
| P01 (mesa) | false | true | Obstaculo decorativo |
| P02 (mic quebrado) | true | false | Decoracao flutuante, jogador passa por baixo |
| P03 (cadeira vazia) | false | true | Obstaculo |
| P04-P05 | true | false | Decoracao flutuante |
| P06 (letreiro) | true | false | Flutuando acima, nao bloqueia |
| P07-P09 | true | false | Detritos flutuantes, overlay |
| P10-P11 | true | false | Cadeiras dos NPCs, overlay (jogador interage, nao colide) |
| A01-A05 | true | false | Overlays de atmosfera |

---

## 8. Paleta de Cores do Limbo (Referencia Cruzada)

Extraida da `color-palette.md` secao 7, expandida para o tileset:

| Nome | Hex | Uso | Alpha |
|---|---|---|---|
| **Void Base** | `#0A0A0A` | Fundo infinito — tile L01 | 100% |
| **Void Noise** | `#141414` | Variacao sutil do void — noise nos tiles L01 | 100% |
| **Void Particula** | `#2A2A2A` | Poeira flutuante, pontos nos tiles L02 | 40% |
| **Void Iluminado** | `#1A1A18` | Area mais "clara" sob luz do podcast — L05 | 100% |
| **Podcast Light** | `#3D6B3A` | Luz verde do podcast — A03, P06, glow | 5-30% |
| **Cadeira Glow** | `#D47820` | Glow laranja sob cadeira Monark — A04 | 10-25% |
| **Neon Limbo** | `#3D6B3A` | Letreiro "LIMBO" — P06 aceso | 100% |
| **Neon Off** | `#1A2A1A` | Letreiro "LIMBO" — segmentos apagados | 100% |
| **Metal Podcast** | `#5C5C5C` | Microfones, estruturas metalicas — P02, P04 | 100% |
| **Metal Escuro** | `#3A3A3A` | Cabos, detalhes metalicos escuros — P05 | 100% |
| **Madeira Mesa** | `#6B4423` | Mesa de podcast — P01 | 100% |
| **Papel Jornal** | `#E8D8C8` | Manchetes, papeis flutuantes — P08 | 100% |
| **Selo Cancelado** | `#8B0000` | Selos de cancelamento — P07 | 100% |
| **Cobre Fio** | `#CC6600` | Fios de audio expostos — P02, P05 | 100% |
| **Tela Celular** | `#4A9ACA` | Smartphones destruidos — P09 | 100% |
| **Fumaca Limbo** | `#6A8A6A` | Wisps de fumaca — A01 | 20-30% |
| **ON AIR** | `#CC3030` | LED do microfone do Monark | 100% |
| **Sangue** | `#8B0000` | Manchas em detritos | 100% |
| **Fita Adesiva** | `#B8A030` | Fita em equipamento improvisado | 100% |
| **Contorno** | `#1A1A18` | Linhas de contorno em TODOS os props | 100% |

### Regras de Cor
- **NUNCA usar branco puro** (`#FFFFFF`) — o maximo e `#E8E0D0` (branco sujo)
- **NUNCA usar preto puro** (`#000000`) — o maximo e `#0A0A0A` (preto com noise)
- **COR QUENTE UNICA**: O glow `#D47820` da cadeira do Monark. E a UNICA fonte de calor visual em todo o Limbo. Isola o Monark como centro.
- **Verde e a cor dominante** do neon/luz: `#3D6B3A` em todas as fontes de luz
- **Cross-hatching nas sombras** de todos os props (consistente com o estilo)

---

## 9. Animacoes de Tiles

Tiles animados no Limbo sao POUCOS e LENTOS (contraste com a Esplanada caotica):

| Tile | Frames | FPS | Tipo | Descricao |
|---|---|---|---|---|
| P05 (cabos) | 2 | 2 | Loop | Ondulacao lenta dos cabos no void |
| P06 (letreiro) | 4 | 2 | Loop | "B" e "I" piscando por mau contato |
| A05 (papeis) | 4 | 2 | Loop | Papeis de cancelamento girando lentamente |
| P09 (celular) | 2 | 1 | Loop | Tela piscando (ultimo sinal de vida) |

**Total de tiles animados**: 4 (contra dezenas na Esplanada). O Limbo e ESTATICO com micro-movimentos sutis.

---

## 10. Exportacao para Phaser 3

### Arquivos
```
limbo.json              — Mapa completo (JSON export do Tiled)
limbo-tileset.png       — Tileset image (256x256)
limbo-tileset.json      — Tileset data (embedded no mapa)
```

### Carregamento no Phaser (GameOverScene.ts)
```javascript
// Preload
this.load.image('limbo-tiles', 'assets/tiles/limbo/limbo-tileset.png');
this.load.tilemapTiledJSON('limbo-map', 'assets/maps/limbo.json');

// Create
const map = this.make.tilemap({ key: 'limbo-map' });
const tileset = map.addTilesetImage('limbo-tileset', 'limbo-tiles');

// Layers em ordem
const voidLayer = map.createLayer('Void', tileset, 0, 0);
const propsLowerLayer = map.createLayer('PropsLower', tileset, 0, 0);
const propsUpperLayer = map.createLayer('PropsUpper', tileset, 0, 0);
const atmosphereLayer = map.createLayer('Atmosphere', tileset, 0, 0);

// Collision minima
propsLowerLayer.setCollisionByProperty({ collision: true });

// SEM background gradient (o void E o background)
this.cameras.main.setBackgroundColor('#0A0A0A');
```

### Efeitos Pos-Mapa (Em Codigo)
```javascript
// Letreiro "LIMBO" piscando
this.time.addEvent({
    delay: 2000,
    callback: () => {
        // Toggle visibilidade do "B" no letreiro
        limboB.setVisible(!limboB.visible);
    },
    loop: true
});

// Glow pulsante da cadeira do Monark
const chairGlow = this.add.pointlight(
    MONARK_X, MONARK_Y + 24,
    0xD47820, 40, 0.15
);
this.tweens.add({
    targets: chairGlow,
    intensity: { from: 0.1, to: 0.2 },
    duration: 2000,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});

// Particulas do void (emitter lento)
const voidParticles = this.add.particles(0, 0, 'void-particle', {
    x: { min: 0, max: MAP_WIDTH },
    y: { min: 0, max: MAP_HEIGHT },
    scale: { min: 0.3, max: 0.8 },
    alpha: { start: 0.15, end: 0 },
    speed: { min: 1, max: 3 },
    lifespan: { min: 5000, max: 10000 },
    frequency: 1000,
    maxParticles: 10,
    tint: 0x2A2A2A
});
```

---

## 11. Organizacao do Tileset PNG (256x256)

```
Row 0:   L01a L01b L01c L01d L02a L02b L02c L02d L03a L03b L03c L03d L04a L04b L04c L04d
Row 1:   L05a L05b [vazio x14]
Row 2:   P02a P02b P02c P04a P04b P07a P07b P07c P08a P08b P08c P09a P09b [vazio x3]
Row 3:   A01a A01b A01c A01d A02a A02b A02c A03a A03b A03c A03d A03e A03f A04a A04b A04c
Row 4:   A04d A05(f0) A05(f1) A05(f2) A05(f3) [vazio x11]
Row 5-6: P01 (mesa, 3x2 tiles — disposto em 6 tiles sequenciais)
Row 7:   P03a(2 tiles) P03b(2 tiles) P05a(4 tiles) P05b(4 tiles) [vazio]
Row 8:   P06 (letreiro 4x1 tiles — 4 estados x 4 tiles = 16 tiles)
Row 9:   P10 (cadeira Monark 2x3 = 6 tiles) P11 (cadeira Arthur 1x2 = 2 tiles) [vazio]
Row 10-15: Reservado para expansao
```

---

## 12. UI do Game Over (Sobre o Tilemap)

A UI do Game Over e renderizada SOBRE o tilemap do Limbo, como overlay do Phaser.

### Layout
```
┌─────────────────────────────────────────────────┐
│                                                  │
│          [LETREIRO "LIMBO" — P06]                │
│                                                  │
│      [MONARK na cadeira]  [ARTHUR na cadeira]    │
│           [Mesa de podcast abaixo]               │
│                                                  │
│        ╔══════════════════════════╗              │
│        ║  SEU MANDATO ACABOU     ║              │  Fonte irregular, grande
│        ╚══════════════════════════╝              │
│                                                  │
│          SCORE: 12,450                           │  #F0C830
│          WAVE: 7                                 │  #D47820
│          TITULO: "Cabo Eleitoral"                │  Titulo satirico
│                                                  │
│        ┌──────────────┐  ┌──────────────┐       │
│        │   SEGUNDA    │  │   DESISTIR   │       │
│        │   CHANCE     │  │              │       │
│        └──────────────┘  └──────────────┘       │
│        (Monark oferece)  (Menu Principal)        │
└─────────────────────────────────────────────────┘
```

### Titulos Satiricos (baseados no score)
| Score | Titulo | Referencia |
|---|---|---|
| 0 - 999 | "Eleitor Arrependido" | Baixo envolvimento |
| 1000 - 4999 | "Cabo Eleitoral" | Nivel basico |
| 5000 - 9999 | "Vereador Suplente" | Quase alguem |
| 10000 - 19999 | "Deputado de Primeiro Mandato" | Competente |
| 20000 - 49999 | "Senador em Ascensao" | Bom |
| 50000 - 99999 | "Ministro Interino" | Muito bom |
| 100000+ | "Presidente da Republica (por 5 min)" | Lendario |

---

## 13. Transicao de Entrada (Death → Limbo)

### Timeline (total ~3.5 segundos)
```
0ms     — Gameplay congela, fade out soundtrack
200ms   — Player death animation completa
500ms   — Fade to black (300ms)
800ms   — Void background aparece (#0A0A0A)
1200ms  — Particulas do void comecam
1500ms  — Props fade in (mesa, cadeiras abandonadas, detritos)
2000ms  — Letreiro "LIMBO" acende (flash verde)
2200ms  — Cadeira do Monark materializa com glow laranja
2400ms  — Cadeira do Arthur materializa (sem glow)
2600ms  — Monark entrance animation (A09) — se primeira morte
         OU Monark ja presente (idle) — se morte subsequente
3000ms  — "SEU MANDATO ACABOU" aparece (typewriter)
3500ms  — Score, opcoes, dialogo do Monark comecam
```

---

## 14. Checklist de Producao

### Tiles Base
- [ ] Criar paleta de cores no editor (Aseprite/Photoshop)
- [ ] Desenhar 4 variantes de L01 (void puro com noise diferente)
- [ ] Desenhar 4 variantes de L02 (void com particulas)
- [ ] Desenhar 4 variantes de L03 (void com veias de energia)
- [ ] Desenhar 4 variantes de L04 (void gradiente — bordas podcast light)
- [ ] Desenhar 2 variantes de L05 (void iluminado)
- [ ] Testar seamless: tiles de void devem ser IMPERCEPTIVELMENTE diferentes entre si

### Props
- [ ] Desenhar P01 (mesa de podcast destruida, 3x2 tiles)
- [ ] Desenhar P02 a-c (microfones quebrados)
- [ ] Desenhar P03 a-b (cadeiras abandonadas)
- [ ] Desenhar P04 a-b (fones de ouvido)
- [ ] Desenhar P05 a-b (cabos emaranhados, 2x2 tiles)
- [ ] Desenhar P06 (letreiro "LIMBO", 4x1 tiles, 4 estados de animacao)
- [ ] Desenhar P07 a-c (selos de cancelado)
- [ ] Desenhar P08 a-c (manchetes flutuantes)
- [ ] Desenhar P09 a-b (smartphones destruidos)
- [ ] Desenhar P10 (cadeira Monark, 2x3 tiles)
- [ ] Desenhar P11 (cadeira Arthur, 1x2 tiles)

### Atmosfera
- [ ] Desenhar A01 a-d (fumaca eterea)
- [ ] Desenhar A02 a-c (poeira do void)
- [ ] Desenhar A03 a-f (rastro de luz / cone podcast)
- [ ] Desenhar A04 a-d (glow laranja cadeira)
- [ ] Desenhar A05 (papeis cancelamento, 4 frames animados)

### Montagem
- [ ] Montar tileset PNG 256x256
- [ ] Configurar no Tiled Map Editor
- [ ] Definir propriedades de collision
- [ ] Montar mapa 20x15 tiles
- [ ] Configurar layers (Void, PropsLower, PropsUpper, Atmosphere)
- [ ] Exportar JSON para Phaser 3
- [ ] Testar carregamento na GameOverScene

### Validacao
- [ ] Verificar que void nao e "flat" (variacao sutil visivel)
- [ ] Verificar que props parecem FLUTUAR (sem referencia de chao)
- [ ] Verificar glow laranja da cadeira do Monark como UNICO ponto quente
- [ ] Verificar letreiro "LIMBO" legivel e piscando
- [ ] Verificar que o cenario e o OPOSTO da Esplanada (vazio vs cheio)
- [ ] Testar com sprites do Monark e Arthur posicionados
- [ ] Verificar performance (deve ser MAIS leve que Esplanada — menos tiles, menos particulas)
- [ ] Aplicar overlay de textura de papel em todos os tiles (consistencia com resto do jogo)
- [ ] Verificar que nenhuma cor e "pura" (ver color-palette.md)
