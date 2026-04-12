# Martelao da Censura -- Especificacao de Sprites

**Weapon ID:** 11
**Boss:** Xandao (Alexandre de Moraes)
**Tipo:** Melee / Area-of-Effect (Shockwave)
**Categoria:** Arma Exclusiva de Boss do STF
**Nivel de Perigo:** EXTREMO -- arma de boss final do arco STF

---

## Descricao Geral

Martelo de juiz ABSURDAMENTE desproporcional -- do tamanho de um poste de luz. A cabeca do martelo e grotescamente larga, com a inscricao "CENSURADO" pintada em letras vermelhas brilhantes que pulsam como neon. O cabo e longo, escuro, com rachaduras e fita isolante enrolada em alguns pontos. Cada martelada cria uma onda de choque visivel que "silencia" inimigos (remove falas/gritos) e causa dano em area. Ao acertar um inimigo, um carimbo gigante de "INQUERITO INSTAURADO" aparece estampado sobre ele em vermelho sangue. O projetil secundario e uma nota de multa de R$50M que voa girando.

O martelo deve parecer que pertence a um semideus burocratico que usa a Justica como arma de puro poder arbitrario. Visual grotesco, underground comix, Robert Crumb + horror juridico brasileiro.

---

## 1. Sprite da Arma (Segurada / Inventario)

**Dimensoes:** 64x64 px (arma de boss -- desproporcional)
**Anchor point:** Bottom-center (32, 60) -- ponto de empunhadura no cabo
**Sprite sheet:** 192x64 px (3 frames: static + 2 idle)

### Paleta de Cores

| Elemento                   | Hex       | Uso                                           |
|----------------------------|-----------|-----------------------------------------------|
| Madeira Cabo Escura        | `#3E2723` | Corpo principal do cabo do martelo             |
| Madeira Cabo Media         | `#5D4037` | Highlights do cabo, veios da madeira           |
| Madeira Cabo Clara         | `#795548` | Bordas iluminadas do cabo                      |
| Fita Isolante Preta        | `#1A1A1A` | Fita isolante enrolada no cabo (remendos)      |
| Cabeca Martelo Escura      | `#1B2631` | Sombra da cabeca do martelo (ferro velho)      |
| Cabeca Martelo Media       | `#2C3E50` | Corpo principal da cabeca (metal pesado)       |
| Cabeca Martelo Clara       | `#3D5A80` | Highlights metalicos da cabeca                 |
| Metal Brilho               | `#85929E` | Reflexo metalico nos cantos                    |
| Vermelho CENSURADO         | `#E60000` | Texto "CENSURADO" na cabeca                    |
| Vermelho Brilho Neon       | `#FF3333` | Glow pulsante do texto CENSURADO               |
| Vermelho Escuro            | `#8B0000` | Sombra do texto / manchas de sangue            |
| Amarelo Juridico           | `#DAA520` | Detalhes dourados (tachas, parafusos)          |
| Branco Flash               | `#FFFFFF` | Flash de impacto, brilho maximo                |
| Outline Preto              | `#0D0D0D` | Contornos grossos estilo Crumb (3px minimo)    |
| Shockwave Vermelho         | `#FF1A1A` | Ondas de choque concentricas                   |
| Shockwave Transparente     | `#FF1A1A40` | Ondas externas (semi-transparente)           |
| Carimbo Vermelho           | `#CC0000` | Texto "INQUERITO INSTAURADO" no inimigo        |
| Multa Papel                | `#F5F0DC` | Nota de multa (projetil)                       |
| Multa Verde Dinheiro       | `#2E7D32` | Cifras na nota de multa                        |
| Fumaca Cinza               | `#696969` | Fumaca de poeira pos-impacto                   |

### Descricao por Frame

#### Frame 0 -- Static / Icone de Inventario
- Martelo visto de cima (perspectiva top-down isometrica levemente inclinada)
- A CABECA DO MARTELO e o elemento dominante -- ocupa ~60% do frame horizontalmente
- Formato da cabeca: retangular largo com cantos levemente arredondados, metal pesado e envelhecido
- Na face principal da cabeca, inscricao "CENSURADO" em letras vermelhas GRANDES, grossas, estilo carimbo oficial -- as letras sao desiguais como carimbadas a mao
- Ao redor do texto, pequenas rachaduras no metal sugerindo anos de uso brutal
- 4 tachas douradas nos cantos da cabeca do martelo (2px cada, #DAA520)
- O cabo estende-se para baixo, longo e fino em comparacao com a cabeca absurda
- Cabo de madeira escura com 2-3 faixas de fita isolante preta enrolada (remendos improvisados)
- Veios da madeira visiveis no cabo (1px linhas mais claras no sentido vertical)
- Na juncao cabo-cabeca, um anel metalico escuro (reforco)
- Contornos GROSSOS e IRREGULARES (3px minimo) -- estilo Robert Crumb
- Sombra pesada no lado esquerdo/inferior (offset 3px, 50% opacidade)
- O martelo inteiro deve parecer PESADO -- voce quase sente o peso absurdo pelo visual
- Pequenas manchas escuras na cabeca sugerindo respingos secos (ambiguamente sangue ou tinta vermelha)

#### Frame 1 -- Idle Glow A (Pulsacao do CENSURADO)
- Identico ao Frame 0, porem:
- O texto "CENSURADO" emite um glow vermelho neon expandido (2px ao redor das letras)
- O glow usa #FF3333 com 60% de opacidade
- As tachas douradas tem um brilho minimo (1px branco no canto superior-direito de cada)
- Sutil "calor" emanando do texto -- 2-3 particulas vermelhas de 1px flutuando acima da inscricao
- O cabo tem um micro-deslocamento de 1px para a esquerda (respiracao idle)

#### Frame 2 -- Idle Glow B (Pulsacao alternada)
- Espelho do Frame 1:
- O glow do "CENSURADO" esta no ciclo FRACO -- texto em #E60000 sem glow externo
- Porem as tachas douradas agora brilham MAIS (2px de glow dourado)
- As particulas vermelhas flutuantes estao em posicoes diferentes (mais altas e desvanecendo)
- Cabo com micro-deslocamento de 1px para a direita
- Juntos, Frame 1 e Frame 2 em loop criam efeito de pulsacao ameacadora constante

---

## 2. Animacao de Swing / Ataque (Martelada)

**Dimensoes:** 64x64 px por frame
**Frames:** 4
**Sprite sheet:** 256x64 px (horizontal)
**FPS sugerido:** 8 fps (jerky, pesado -- cada frame deve "pesar")

#### Frame 0 -- Ergue (Wind-Up)
- O martelo e erguido acima da cabeca do boss (deslocado 8px para cima, 4px para tras)
- A cabeca do martelo aponta para CIMA, o cabo para baixo em diagonal (~60 graus do solo)
- A inscricao "CENSURADO" fica virada para o jogador, legivel e ameacadora
- Glow vermelho INTENSIFICADO (o texto brilha mais forte, preparando o golpe)
- 2-3 linhas de tensao radiando da cabeca do martelo (linhas brancas finas, 1px, 40% opacidade)
- A gravidade e implicita -- o personagem "esforcar" para segurar o martelo no alto
- Uma sombra no chao sob o boss DIMINUI (martelo levantado = sombra sobe)
- Pequena nuvem de poeira no ponto de apoio dos pes (2-3px cinza)

#### Frame 1 -- Descida (Mid-Swing)
- O martelo esta no meio do arco descendente (~45 graus)
- A cabeca do martelo agora aponta para frente-baixo, velocidade maxima
- MOTION BLUR massivo: 3-4 linhas de rastro (2px cada, cor do metal com opacidade decrescente: 80%, 60%, 40%, 20%)
- O texto "CENSURADO" esta parcialmente borrado pela velocidade
- Glow vermelho estica-se para tras como um cometa (trail vermelho de 6-8px)
- O ar ao redor do martelo parece se DEFORMAR (2 linhas curvas brancas representando compressao do ar)
- Pedacos de poeira/detritos (3-4 particulas de 1px) sao sugados no rastro
- Sensacao de peso DEVASTADOR em queda

#### Frame 2 -- Impacto (Contact)
- **FRAME PRINCIPAL DE IMPACTO** -- maximo de caos visual
- O martelo ESMAGA o chao/alvo -- cabeca achatada contra a superficie (squash extremo: cabeca ~40x20px, deformada)
- EXPLOSAO DE CONTATO:
  - Flash branco central (10px raio)
  - Rachadura no chao irradiando do ponto de impacto (4-6 linhas escuras divergentes, cada com 8-12px)
  - Detritos voando em todas as direcoes (6-8 particulas: pedacos de chao, metal, poeira -- tamanhos variados 1-3px)
  - O texto "CENSURADO" distorce-se com o impacto mas permanece legivel
- A ONDA DE CHOQUE COMECA: primeiro anel concentrico vermelho (#FF1A1A) aparecendo ao redor do ponto de impacto (raio 12px, 2px de espessura)
- Pequenos "X" vermelhos (simbolo de silencio/censura) aparecem dentro da onda de choque (3-4 X de 2x2px)
- Poeira levantando-se em nuvem ao redor da base do impacto (5-6px de altura, cinza-marrom)
- O cabo do martelo vibra visivelmente (linhas de vibracao laterais, 2 linhas onduladas de 1px)
- Screen shake sugerido: todo o frame tem micro-offset (elementos levemente desalinhados)

#### Frame 3 -- Follow-Through / Reverberacao
- O martelo comeca a se levantar do ponto de impacto (inclinado ~20 graus do chao)
- Residuo vermelho no ponto de impacto (mancha CENSURADO impressa no chao em vermelho fraco)
- A onda de choque expandiu-se (raio agora ~24px, ficando semi-transparente)
- Mais "X" de censura na onda expandida, tambem ficando transparentes
- Detritos ainda se dispersando, agora mais longe e menores
- Poeira assentando (3-4px de altura, mais esparsa)
- Uma segunda onda de choque menor comeca a se formar no ponto de impacto (raio 8px)
- O cabo ainda vibra levemente (1 linha ondulada)
- A fita isolante no cabo esta levemente descolada (detalhe de desgaste)

---

## 3. Efeito de Impacto -- Carimbo "INQUERITO INSTAURADO"

**Dimensoes:** 48x48 px por frame (overlay sobre o inimigo atingido)
**Frames:** 3
**Sprite sheet:** 144x48 px

#### Frame 0 -- Carimbo Aparece
- O texto "INQUERITO INSTAURADO" aparece ESTAMPADO sobre o alvo
- Estilo visual: carimbo oficial de cartorio, borda retangular dupla
- Letras em vermelho escuro (#CC0000) sobre fundo semi-transparente branco (#FFFFFF60)
- O texto esta levemente torto (~5 graus) como um carimbo batido as pressas
- As letras sao TOSCAS, irregulares -- tipografia de carimbo de borracha desgastado
- Tinta ainda "molhada" -- pequenas gotitas de tinta vermelha pingando das letras (2-3 gotas de 1px)
- Flash branco ao redor do carimbo (3px glow, 40% opacidade)
- O carimbo ocupa ~80% do frame de 48x48

#### Frame 1 -- Carimbo Intenso
- O carimbo esta no brilho maximo -- letras mais brilhantes (#E60000)
- A tinta "escorre" levemente para baixo (efeito de gravidade nas gotas)
- A borda dupla do carimbo pulsa com glow vermelho
- Adicao de um selo circular no canto inferior-direito do carimbo: circulo com "STF" dentro e estrelinhas (parodia de selo oficial)
- Particulas de poeira de tinta (3-4 pontos vermelhos de 1px) ao redor do carimbo
- Micro-rachaduras na "tinta" sugerindo a secagem rapida

#### Frame 2 -- Carimbo Desvanece
- O carimbo comeca a ficar semi-transparente (~50% opacidade)
- As gotas de tinta secaram (pontos fixos, mais escuros)
- O glow desapareceu
- O selo STF esta desbotando
- Efeito de "papel velho" -- o carimbo parece ja fazer parte do inimigo, como uma marca permanente
- Leve amarelecimento nos cantos (como documento envelhecido)
- Este frame faz transicao para o efeito de silencio no inimigo

---

## 4. Onda de Choque (Shockwave de Silencio)

**Dimensoes:** 96x96 px por frame (efeito de area grande -- arma de boss)
**Frames:** 4
**Sprite sheet:** 384x96 px

#### Frame 0 -- Onda Inicial
- Anel concentrico fino (2px) em vermelho brilhante (#FF1A1A) com raio de 16px, centrado
- Dentro do anel: pequenos simbolos "X" (icone de censura/mudo) em vermelho escuro, 3-4 unidades, tamanho 3x3px cada
- Distorcao de ar no centro (pixels levemente deslocados, efeito heat haze)
- Micro-particulas de poeira vermelha sendo empurradas pela onda (4-5 pontos de 1px)
- Fundo transparente -- este e um overlay de efeito

#### Frame 1 -- Onda Expandindo
- O anel cresceu para raio ~32px, agora com 3px de espessura
- Um SEGUNDO anel interno aparece (raio 16px, 1px de espessura, mais transparente)
- Os simbolos "X" estao agora ENTRE os dois aneis, se espalhando
- Novos "X" menores (2x2px) surgindo no anel externo
- A cor do anel externo comeca a ficar semi-transparente (#FF1A1A80)
- Linhas de forca radiais entre os aneis (6-8 linhas de 1px, vermelho claro)
- Efeito visual de "silencio": pequenas bolhas de fala (icones de dialogo) RISCADAS com X aparecem e desintegram (2-3 balaozinhos de 4x4px com X vermelho)

#### Frame 2 -- Onda Maxima
- Anel externo no raio maximo (~44px), fino e quase transparente (#FF1A1A30)
- Anel medio (raio ~28px, 2px de espessura, 60% opacidade)
- Anel interno residual (raio ~12px, desvanecendo)
- Os "X" de censura estao em todas as faixas entre aneis, variando de tamanho (2-4px)
- As bolhas de fala riscadas estao nos limites do anel externo, se dissolvendo
- Particulas de poeira vermelha atingiram a borda do frame
- No centro: uma marca residual escura no chao (circulo de queimadura, 8px)
- A onda comecar a perder forca visualmente (bordas irregulares, fragmentadas)

#### Frame 3 -- Onda Dissipando
- Apenas o anel externo permanece (raio ~44px, 1px de espessura, 15% opacidade)
- Os simbolos "X" estao desvanecendo (5-10% opacidade, maiores e mais esparsos)
- Ultimas bolhas de fala riscadas se desfazem em pixels
- Poeira vermelha assentando (2-3 pontos de 1px caindo)
- A marca no chao escurece ligeiramente
- Fragmentos residuais do anel se quebrando em segmentos curtos (arcos interrompidos)
- Transicao suave para ausencia de efeito

---

## 5. Projetil -- Multa do X (R$50M)

**Dimensoes:** 32x32 px por frame
**Frames:** 4 (rotacao em voo, loop)
**Sprite sheet:** 128x32 px

### Descricao Geral do Projetil
Uma nota de multa absurdamente grande (folha oficial com valor "R$ 50.000.000,00" em destaque) que voa girando pelo ar. A nota tem o logo do STF (parodia), a assinatura ilegivel de Xandao, e um carimbo vermelho. E basicamente uma arma burocratica voadora.

#### Frame 0 -- Rotacao 0 graus (frente)
- Nota de papel vista de frente, levemente amarelada (#F5F0DC)
- Ocupa ~24x28px dentro do frame 32x32
- Texto grande no centro: "R$ 50M" em vermelho escuro (#8B0000), fonte grossa
- Logo STF parodiado no topo (escudo pequeno, 4x4px, dourado)
- Linhas de texto ilegivel simulando o corpo do documento (3-4 linhas de scribble cinza)
- Assinatura grotesca na parte inferior (rabisco preto grosso)
- Carimbo vermelho circular no canto inferior-direito (3px diametro)
- Cantos do papel levemente dobrados/amarelados (desgaste)
- Contorno preto grosso (2px)
- Trail de 2-3 particulas de papel atras (1px, #F5F0DC, opacidade decrescente)

#### Frame 1 -- Rotacao 90 graus
- Nota de lado -- visivel como uma fina linha com perspectiva
- A nota parece fina como papel (3-4px de largura visual)
- Borda superior e inferior visiveis, detalhes do papel em perfil
- O texto "R$ 50M" aparece comprimido/distorcido pela perspectiva
- Trail de particulas mais longo (3-4 pontos, sugerindo velocidade)
- Brilho de papel na borda (1px branco highlight no canto)

#### Frame 2 -- Rotacao 180 graus (verso)
- Verso da nota visivel -- mais liso, com linhas horizontais finas (pautado)
- Um grande carimbo "PAGUE OU SERA PRESO" em vermelho, estilo carimbo torto, ocupa 60% do verso
- Marca d'agua sutil: silhueta grotesca de Xandao com toga (5x8px, cinza claro sobre o papel)
- Mesma nota amarelada com cantos dobrados
- Particulas de trail continuam

#### Frame 3 -- Rotacao 270 graus
- Nota em perfil novamente (lado oposto do Frame 1)
- Mesma representacao fina
- O carimbo vermelho lateral e parcialmente visivel como linha vermelha na borda
- Trail de particulas no maximo (4-5 pontos, o mais distante quase invisivel)
- Reflexo de papel na outra borda (1px branco)

---

## 6. Efeito de Silencio no Inimigo (Debuff de Censura)

**Dimensoes:** 32x32 px por frame (overlay sobre inimigo afetado)
**Frames:** 3 (loop durante duracao do debuff -- 4 segundos)
**Sprite sheet:** 96x32 px

#### Frame 0 -- Censurado A
- Tarja preta ("black bar") horizontal sobre a area da boca do inimigo (~16x4px, preto solido)
- A palavra "CENSURADO" em letras brancas microscropicas DENTRO da tarja (1px de altura)
- "X" vermelho sobre a area da boca (por cima da tarja)
- Icone de mudo no canto superior-direito: alto-falante com X (4x4px, vermelho)
- Leve tremedeira no sprite todo (implicada por 1px de offset aleatorio)
- Aura vermelha fraca ao redor do inimigo (1px borda, 20% opacidade)

#### Frame 1 -- Censurado B
- Tarja preta EXPANDIDA levemente (18x5px) -- efeito de pulsacao
- "CENSURADO" mais brilhante dentro da tarja
- O "X" vermelho esta em posicao diferente (levemente rotado 5 graus)
- Icone de mudo pisca (mais brilhante que Frame 0)
- Pequenas ondas de "silencio" emanando do inimigo (2 arcos finos semi-transparentes, 1px)
- Aura vermelha levemente mais intensa (25% opacidade)

#### Frame 2 -- Censurado C
- Tarja volta ao tamanho original (16x4px)
- "CENSURADO" no brilho minimo (quase invisivel)
- O "X" esta no angulo oposto do Frame 1
- Icone de mudo normal
- Ondas de silencio em posicoes diferentes (mais afastadas e dissipando)
- Aura volta a 20%
- Juntos, os 3 frames criam uma censura pulsante desconfortavel

---

## Resumo do Sprite Sheet

| Sheet                    | Frames | Tam. Frame | Tam. Total | Phaser Key                    |
|--------------------------|--------|------------|------------|-------------------------------|
| `martelao_static`        | 3      | 64x64      | 192x64     | `weapon_martelao_idle`        |
| `martelao_swing`         | 4      | 64x64      | 256x64     | `weapon_martelao_swing`       |
| `martelao_carimbo`       | 3      | 48x48      | 144x48     | `fx_inquerito_carimbo`        |
| `martelao_shockwave`     | 4      | 96x96      | 384x96     | `fx_martelao_shockwave`       |
| `martelao_multa`         | 4      | 32x32      | 128x32     | `projectile_multa_50m`        |
| `martelao_censurado`     | 3      | 32x32      | 96x32      | `fx_censurado_debuff`         |

## Configuracao Phaser 3

```javascript
// Sprite da arma
this.load.spritesheet('weapon_martelao_idle', 'assets/armas/martelao-censura/martelao_static.png', {
  frameWidth: 64,
  frameHeight: 64
});

// Animacao de ataque
this.load.spritesheet('weapon_martelao_swing', 'assets/armas/martelao-censura/martelao_swing.png', {
  frameWidth: 64,
  frameHeight: 64
});

// Carimbo de inquerito (overlay no inimigo)
this.load.spritesheet('fx_inquerito_carimbo', 'assets/armas/martelao-censura/martelao_carimbo.png', {
  frameWidth: 48,
  frameHeight: 48
});

// Onda de choque
this.load.spritesheet('fx_martelao_shockwave', 'assets/armas/martelao-censura/martelao_shockwave.png', {
  frameWidth: 96,
  frameHeight: 96
});

// Projetil multa
this.load.spritesheet('projectile_multa_50m', 'assets/armas/martelao-censura/martelao_multa.png', {
  frameWidth: 32,
  frameHeight: 32
});

// Debuff de censura
this.load.spritesheet('fx_censurado_debuff', 'assets/armas/martelao-censura/martelao_censurado.png', {
  frameWidth: 32,
  frameHeight: 32
});
```

## Animacoes Phaser 3

```javascript
// Idle pulsante
this.anims.create({
  key: 'martelao_idle',
  frames: this.anims.generateFrameNumbers('weapon_martelao_idle', { start: 1, end: 2 }),
  frameRate: 4,  // Lento, ameacador
  repeat: -1
});

// Swing (ataque)
this.anims.create({
  key: 'martelao_swing',
  frames: this.anims.generateFrameNumbers('weapon_martelao_swing', { start: 0, end: 3 }),
  frameRate: 8,  // Jerky, pesado
  repeat: 0
});

// Carimbo aparecendo no inimigo
this.anims.create({
  key: 'inquerito_stamp',
  frames: this.anims.generateFrameNumbers('fx_inquerito_carimbo', { start: 0, end: 2 }),
  frameRate: 6,
  repeat: 0
});

// Shockwave expandindo
this.anims.create({
  key: 'martelao_shockwave',
  frames: this.anims.generateFrameNumbers('fx_martelao_shockwave', { start: 0, end: 3 }),
  frameRate: 10,
  repeat: 0
});

// Multa voando (loop de rotacao)
this.anims.create({
  key: 'multa_flight',
  frames: this.anims.generateFrameNumbers('projectile_multa_50m', { start: 0, end: 3 }),
  frameRate: 12,
  repeat: -1
});

// Debuff de censura (loop)
this.anims.create({
  key: 'censurado_debuff',
  frames: this.anims.generateFrameNumbers('fx_censurado_debuff', { start: 0, end: 2 }),
  frameRate: 6,
  repeat: -1
});
```

---

## Notas para o Artista

- O martelao DEVE ser GROTESCAMENTE desproporcional -- a cabeca do martelo e quase do tamanho do Xandao inteiro
- O texto "CENSURADO" e o elemento visual mais iconica -- deve ser LEGIVEL mesmo em 64x64px (use pixels grossos)
- Os contornos sao GROSSOS E IRREGULARES (3px minimo, estilo Robert Crumb / Andre Guedes)
- A paleta e saturada-suja: vermelhos intensos mas com sujeira, metal envelhecido, madeira gasta
- O peso do martelo deve ser SENTIDO visualmente: frames de swing devem parecer pesados, nao rapidos
- A onda de choque com os "X" de censura e uma metafora visual direta: o silencio sendo imposto a forca
- O carimbo "INQUERITO INSTAURADO" deve parecer um documento REAL de cartorio -- mas grotesco e sanguinolento
- As multas voando sao absurdas por design -- burocracia como arma literal
- TUDO deve estar levemente "errado" -- assimetrico, tremido, vivo, perturbador
- O martelo nao e uma ferramenta de justica -- e uma ferramenta de OPRESSAO COSMICA. O visual deve transmitir isso.
- A fita isolante no cabo e um detalhe de humor negro: ate a arma do todo-poderoso esta remendada
- Referencia visual: um juiz insano em um tribunal de pesadelo B-movie brasileiro
