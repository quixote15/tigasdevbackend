# Biblia Sagrada Blindada - Sprite Specification

## Overview
- **Weapon Type:** Melee + AoE Special (Boss Weapon - Cabo Daciolo)
- **Sprite Dimensions:** 48x48px (arma principal -- BOSS SCALE, absurdamente gigante)
- **Particle Sprite Dimensions:** 32x32px (aura, paginas voando, raio divino)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 24 (1 static + 3 swing + 4 impact + 2 idle + 4 aura particles + 4 page particles + 3 divine ray + 3 demon special)
- **Sprite Sheet Size:** 1152x48px (weapon) / 576x32px (particles/FX)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (24, 44) -- spine grip point

## Color Palette

| Element                   | Hex Code  | Usage                                      |
|---------------------------|-----------|---------------------------------------------|
| Leather Black (cover)     | `#1A1410` | Bible cover, worn black leather             |
| Leather Brown (aged)      | `#3B2A18` | Cover creases, aged leather patches         |
| Leather Brown (light)     | `#5A3D22` | Worn edge highlights, scuff marks           |
| Gold Cross (main)         | `#D4A017` | Cross on cover, central emblem              |
| Gold Cross (bright)       | `#FFD700` | Cross glow, divine activation               |
| Gold Cross (dim)          | `#A07A10` | Cross shadows, depth                        |
| Gold Leaf Trim            | `#C4960E` | Edge gilding on cover border                |
| Page Cream                | `#F0E6C8` | Page edges, flying page particles           |
| Page Yellow (aged)        | `#D4C8A0` | Aged page discoloration                     |
| Page Shadow               | `#B0A480` | Page depth, folded shadows                  |
| Spine Metal               | `#6B7B8A` | Reinforced metal spine plate                |
| Spine Metal (light)       | `#8C9EAE` | Metal highlights, rivets                    |
| Spine Metal (dark)        | `#4A5A68` | Metal shadows, dents                        |
| Rivet Steel               | `#7A8A9A` | Individual rivet heads on spine             |
| Bookmark Red              | `#8B1A1A` | Multiple bookmark ribbons                   |
| Bookmark Blue             | `#1A3A8B` | Bookmark ribbon variant                     |
| Bookmark Green            | `#2A6B2A` | Bookmark ribbon variant                     |
| Bookmark Purple           | `#5A1A7A` | Bookmark ribbon variant                     |
| Bookmark Yellow           | `#C4A830` | Bookmark ribbon variant                     |
| Aura Gold (core)          | `#FFE066` | Divine aura inner glow                      |
| Aura Gold (outer)         | `#FFD700` | Divine aura mid ring                        |
| Aura Gold (fade)          | `#C4960E` | Divine aura outer fade                      |
| Divine Ray White          | `#FFFFF0` | Central ray of divine light                 |
| Divine Ray Yellow         | `#FFF8B0` | Ray halo, secondary glow                    |
| Faith Particle            | `#FFE8A0` | Tiny faith sparkle particles                |
| Demon Burn Red            | `#CC2200` | Glow when hitting demonic enemies           |
| Outline Black             | `#1A1A1A` | Thick 2px outlines (Crumb style)            |
| Shadow Dark               | `#0D0D0D` | Drop shadow, 50% opacity                   |
| "GLORIA" Gold             | `#FFD700` | Onomatopeia text color                      |
| Page Text Scrawl          | `#3B2A18` | Tiny illegible scripture on flying pages    |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon (48x48)
- **Position in sheet:** 0,0 to 47,47
- **Description:** BIBLIA GIGANTESCA vista em top-down isometrico. DESPROPORCIONAL -- quase do tamanho do torso do Daciolo, preenche 90% do frame 48x48. Capa de couro PRETO (#1A1410) gasto e desgastado com rachaduras visiveis no couro (linhas finas #3B2A18 irregulares). Uma CRUZ DOURADA (#D4A017) domina a capa frontal -- cruza de ponta a ponta, ligeiramente torta (mao-desenhada, imperfeita). A cruz tem brilho sutil (1px #FFD700 ao redor das bordas). Paginas visiveis na lateral direita -- GROSSAS como um tijolo, amareladas (#F0E6C8 a #D4C8A0), empilhamento visivel de centenas de paginas. Borda dourada nas paginas (#C4960E) gasta e irregular. LOMBADA REFORCADA COM METAL -- uma placa de aco (#6B7B8A) e rebitada na lombada com 6 rebites visiveis (#7A8A9A, 2x2px cada), parece blindagem MEDIEVAL. Dentes e arranhoes na placa metalica -- esta Biblia viu COMBATE. MARCADORES DE PAGINA coloridos saindo de TODOS os lados -- no minimo 5 fitas (vermelho #8B1A1A, azul #1A3A8B, verde #2A6B2A, roxo #5A1A7A, amarelo #C4A830) penduradas desordenadamente como tentaculos de medusa. Contornos grossos pretos (2px) em TUDO. Sombra de drop (3px, 50% opacity). O livro e BRUTAL -- parece que pode matar alguem e absolver ao mesmo tempo.
- **Style Notes:** O contraste entre sagrado (cruz dourada, paginas de escritura) e brutal (placa metalica rebitada, tamanho absurdo, cantos gastos de BATER em coisas) e a piada visual central. A Biblia parece uma arma medieval que acidentalmente tem conteudo religioso. Os marcadores de pagina sao CAOTICOS -- nao organizados, parecem que Daciolo marca CADA pagina que le.

### Frame 1: Swing - Wind-up (Levantando ao Ceu)
- **Position in sheet:** 48,0 to 95,47
- **Description:** Biblia erguida acima da posicao implicita de Daciolo, inclinada para tras ~50 graus. O livro BRILHA de dentro -- 2px de contorno dourado (#FFE066) aparece ao redor da Biblia inteira, SOBRE o contorno preto. A cruz na capa INTENSIFICA seu brilho (pixels #FFD700 expandem 2px ao redor da cruz). Paginas comecam a se ABRIR levemente na base -- 3-4px de fan de paginas creme. Marcadores de pagina VOAM para cima com o movimento (todos as 5 fitas esticadas para cima pelo vento). Placa metalica da lombada reflete luz (highlight #8C9EAE intensifica no topo). 2 linhas de movimento brancas (1px, 40% opacity) trilham abaixo. Uma FAISCAS de fe (2-3 particulas #FFE8A0, 1x1px) flutuam ao redor como vagalumes divinos. A atmosfera e de JULGAMENTO IMINENTE.

### Frame 2: Swing - Divine Smite (Descendo com Furia Sagrada)
- **Position in sheet:** 96,0 to 143,47
- **Description:** Biblia no pico de velocidade, descendo em arco AMPLO a ~30 graus. Stretch maximo (4px alongada na direcao do swing). RAIOS DIVINOS (4 raios, 2px largura, #FFF8B0 core com #FFD700 outer) EXPLODEM da cruz durante o swing -- cada raio tem 10px de comprimento, em angulos de 45 graus. Paginas VOAM VIOLENTAMENTE -- 6-8 particulas de pagina (#F0E6C8, 2x3px cada) com micro-texto ilegivel (#3B2A18) sao arrancadas do livro e flutuam no ar. Marcadores de pagina CHICOTEIAM atras como bandeiras em tempestade. Placa metalica da lombada BORRA com a velocidade. 3 linhas de movimento grossas (2px, 60% opacity, brancas). O livro inteiro VIBRA com furia sagrada -- linhas onduladas de energia ao redor. Mini-GLORIAS (#FFD700, 1px) irradiam ao redor como particulas.

### Frame 3: Swing - Contact (JULGAMENTO FINAL)
- **Position in sheet:** 144,0 to 191,47
- **Description:** Biblia ESMAGA no ponto de impacto. Squash MASSIVO (44x28px, deformada como panqueca divina). A placa metalica da lombada RACHA no impacto -- linhas de fratura (1px #4A5A68) irradiam do ponto de contato. EXPLOSAO DE LUZ SAGRADA -- 8 raios irrompem do centro (#FFF8B0 core, #FFD700 outer, cada 12px comprimento, 2px largura). PAGINAS ERUPTAM para cima -- 8-10 paginas (#F0E6C8 com texto #3B2A18) voam em TODAS as direcoes como confetti divino. Um RAIO DE LUZ DIVINA (#FFFFF0 core, 6px largura) desce do topo do frame ate o ponto de impacto -- como se Deus aprovasse o ataque. A cruz na capa esta BRANCA de tao brilhante (#FFFFF0). Anel de choque dourado (#FFD700, 44px diametro, 1px) expande do hit point. Marcadores de pagina ARRANCADOS e voando separadamente. Sparks (#FFE8A0, 4-5 particulas 1x1px) estrelam ao redor. O impacto tem peso FISICO e ESPIRITUAL simultaneamente.

### Frame 4: Impact - "GLORIA!" Frame 1 (Aparicao)
- **Position in sheet:** 192,0 to 239,47
- **Description:** Starburst massivo de luz sagrada preenche ~80% do frame. No centro, texto "GLORIA!" em letras CHUNKY mao-desenhadas -- letras em ouro (#FFD700) com highlight branco (#FFFFF0) interno e sombra marrom (#3B2A18). Letras sao ENORMES, tremulas, desiguais -- como alguem GRITANDO com toda forca. Raios de luz radiais (8 raios, alternando #FFF8B0 e #FFD700, do centro ate as bordas). Paginas flutuantes (4-5, creme, 3x2px) espiralando ao redor do texto. Uma MINI CRUZ (4x4px, branco puro) flutua acima do "I" de GLORIA. Marcadores de pagina coloridos giram ao redor como confetti.

### Frame 5: Impact - "GLORIA!" Frame 2 (Maximo)
- **Position in sheet:** 240,0 to 287,47
- **Description:** "GLORIA!" no tamanho MAXIMO (110% scale). Letras VIBRAM -- cada uma deslocada 1px em direcao aleatoria do Frame 4. Raios de luz ultrapassam as bordas do frame. Cores intensificam -- dourado vira quase branco nos centros. Exclamacoes adicionais aparecem ("GLORIA!!!") em tamanho menor orbitando o texto principal. Paginas nas bordas, quase sumindo. Frame inteiro tem borda branca (2px, 40% opacity) -- flash de tela. Asinhas de anjo (3x2px, branco) flanqueiam o texto. Notas musicais (2x3px, dourado) flutuam -- como se o impacto emitisse musica celestial. Toda a composicao GRITA divindade.

### Frame 6: Impact - "GLORIA!" Frame 3 (Dissipacao)
- **Position in sheet:** 288,0 to 335,47
- **Description:** "GLORIA!" desvanecendo -- texto a 80% scale, 50% opacity. Cores mudam de ouro para creme morno. Raios afinam para 1px e retraem em direcao ao centro. Paginas sumiram. Um circulo dourado residual (20px diametro, 20% opacity) persiste no centro do impacto -- a "marca da bencao". A mini cruz sobe e desvanece. Notas musicais desaparecem uma por uma. Frame de transicao de volta ao gameplay.

### Frame 7: Impact - Raio de Luz Divina (Coluna)
- **Position in sheet:** 336,0 to 383,47
- **Description:** Frame ESPECIAL: coluna de luz divina. Um pilar de luz (#FFFFF0 core 4px, #FFF8B0 halo 8px, #FFD700 outer glow 12px) desce do topo do frame ate o centro. Particulas de fe (#FFE8A0, 6-8 particulas) sobem dentro da coluna como bolhas. Paginas de escritura (3-4, 2x3px) espiralando DENTRO da coluna de luz como se fossem sugadas. Mini cruzes (2x2px, brancas) aparecem e desaparecem aleatoriamente dentro do pilar. Este frame e usado como OVERLAY quando a Biblia atinge um inimigo particularmente forte. Contorno externo do pilar tremula e pisca.

### Frame 8: Idle - Biblia Pulsa 1 (Luz Crescente)
- **Position in sheet:** 384,0 to 431,47
- **Description:** Biblia em repouso com animacao de PULSACAO DIVINA. A cruz dourada na capa BRILHA mais forte -- pixels #FFD700 expandem 2px ao redor da cruz, formando um halo dourado sutil. Uma aura de luz sagrada (1px, #FFE066, 30% opacity) contorna todo o livro. Paginas TREMEM levemente -- 1-2 cantos de pagina levantam (#F0E6C8, 1px) como se um vento invisivel (o Espirito Santo?) as agitasse. Marcadores de pagina oscilam suavemente para a esquerda. Placa metalica da lombada reflete um brilho (1px highlight desloca do Frame 0). 1 sparkle de fe (#FFE8A0, 1x1px) aparece no canto superior direito. O livro parece VIVO e RESPIRANDO.

### Frame 9: Idle - Biblia Pulsa 2 (Luz Diminuindo)
- **Position in sheet:** 432,0 to 479,47
- **Description:** Cruz retorna ao brilho normal, halo retrai e desaparece. O sparkle move para o canto oposto (superior esquerdo). Marcadores de pagina oscilam para a direita. Cantos de pagina pousam. Uma micro-particula de fe (#FFE8A0) sobe suavemente do livro e se dissipa (sugestao constante de poder divino contido). Brilho metalico desloca para borda oposta. Juntos Frames 8-9 criam uma respiracao divina suave e reverente quando em loop. A Biblia nunca esta completamente "desligada" -- sempre ha um residuo de poder.

### Frame 10: Aura Particle - Full (32x32 FX sheet)
- **Position in particle sheet:** 0,0 to 31,31
- **Description:** Particula de AURA DOURADA em intensidade maxima. Um glow circular suave (20px diametro) com nucleo #FFE066 brilhante (8px diametro), anel medio #FFD700 (14px), e borda exterior #C4960E difusa (20px, 30% opacity). Micro-sparkles (#FFFFF0, 3-4 pixels 1x1px) distribuidos no anel medio. A particula nao e um circulo PERFEITO -- tem irregularidades organicas, mais brilhante em cima (como chama). Este e o efeito de "particulas de fe" que orbita constantemente ao redor da Biblia.

### Frame 11: Aura Particle - Mid
- **Position in particle sheet:** 32,0 to 63,31
- **Description:** Aura a 70% intensidade. Nucleo menor (6px), halos proporcionalmente reduzidos. 2 sparkles. Ligeiramente mais transparente. A particula parece estar "respirando" -- contraida em relacao ao Frame 10.

### Frame 12: Aura Particle - Dim
- **Position in particle sheet:** 64,0 to 95,31
- **Description:** Aura a 40% intensidade. Nucleo minimo (4px), halos quase invisiveis. 1 sparkle. A particula mal se distingue do fundo -- e um eco de divindade.

### Frame 13: Aura Particle - Flicker
- **Position in particle sheet:** 96,0 to 127,31
- **Description:** Aura em "flicker" -- nucleo pisca irregularmente (metade dos pixels do nucleo apagados aleatoriamente). Cria efeito de vela ao vento. Halo fragmentado (gaps de 2px). Este frame QUEBRA o ritmo suave dos outros 3, criando a imprevisibilidade do estilo Andre Guedes. A fe e poderosa mas INSTAVEL.

### Frame 14: Page Particle - Fresh (32x32 FX sheet)
- **Position in particle sheet:** 128,0 to 159,31
- **Description:** Uma PAGINA DE ESCRITURA arrancada, voando, 32x32. Folha de papel retangular (~16x20px) creme (#F0E6C8) com bordas rasgadas IRREGULARES (1px #B0A480 nos cantos, nao retos). Micro-texto ilegivel em linhas (#3B2A18, 1px) -- 4-5 linhas horizontais de "texto" que sao apenas riscos. A pagina esta CURVADA -- nao plana, ondulada como se o vento a deformasse (borda direita curva 2px para cima). Uma mancha amarelada (#D4C8A0) no canto sugere idade. Contorno preto fino (1px neste caso -- e uma particula, nao a arma principal).

### Frame 15: Page Particle - Tumbling
- **Position in particle sheet:** 160,0 to 191,31
- **Description:** Pagina no meio de um TUMBLE -- rotacionada 45 graus, vista parcialmente de lado (mais fina, ~16x12px). O "texto" e visivel em perspectiva. A ondulacao e mais pronunciada. Borda rasgada mais visivel. Uma segunda camada de pagina visivel atras (1px de #D4C8A0 atras da pagina frontal) sugerindo que MULTIPLAS paginas voam juntas.

### Frame 16: Page Particle - Flat
- **Position in particle sheet:** 192,0 to 223,31
- **Description:** Pagina vista quase de frente, girando para posicao "flat" -- ocupa area maxima (~18x22px). Texto mais "legivel" (ainda ilegivel, mas as linhas sao mais definidas). Um VERSICULO SUBLINHADO em vermelho (#8B1A1A, 1px) aparece -- Daciolo sublinhou passagens. A pagina tremula nas bordas (1px de variacao ondulante).

### Frame 17: Page Particle - Disintegrating
- **Position in particle sheet:** 224,0 to 255,31
- **Description:** Pagina se DESINTEGRANDO em particulas de fe. Metade da pagina ainda visivel (#F0E6C8), a outra metade se dissolve em sparkles dourados (#FFE8A0, 4-5 particulas 1x1px). As linhas de texto se transformam em particulas de luz. A borda rasgada brilha dourado. A mensagem visual: as escrituras se CONVERTEM em poder divino. Frame final antes da particula desaparecer.

### Frame 18: Divine Ray - Launch (32x32 FX sheet)
- **Position in particle sheet:** 256,0 to 287,31
- **Description:** RAIO DE LUZ DIVINA em fase de lancamento. Feixe concentrado: nucleo branco (#FFFFF0, 2px largura), halo amarelo (#FFF8B0, 4px), glow dourado externo (#FFD700, 2px, 40% opacity). Ponta em forma de CRUZ (4x4px, branco puro). O raio e ~24px de comprimento, 8px de largura, centralizado no frame. Mini-texto de escritura (#3B2A18, 1px ilegivel) espiralando ao redor do feixe como se as palavras sagradas FOSSEM o poder. Trail de sparkles (3 particulas diminuindo: 2x2, 1x1, 1x1) atras.

### Frame 19: Divine Ray - Peak
- **Position in particle sheet:** 288,0 to 319,31
- **Description:** Raio em intensidade MAXIMA. Nucleo expande para 3px. Cruz na ponta rota 45 graus (agora X). Halo pulsa mais largo (6px). Texto de escritura espiralando mais rapido -- parece um vortex de palavras sagradas. 5 sparkles em trail. O raio VIBRA lateralmente (1px oscilacao) criando efeito de poder instavel. Uma mini aureola (#FFE066, 8px diametro, 1px) aparece ao redor da cruz na ponta.

### Frame 20: Divine Ray - Fading
- **Position in particle sheet:** 320,0 to 351,31
- **Description:** Raio enfraquecendo. Nucleo a 1px, intermitente. Halo fragmentado (gaps). Cruz na ponta desaparecendo (2x2px, 50% opacity). Texto de escritura se dispersa em particulas soltas. Trail particles espalhados. O raio "engasga" visualmente -- nao morre suavemente, FALHA de forma irregular como equipamento divino com defeito. Humor visual: ate o poder de Deus tem problemas tecnicos.

### Frame 21: Demon Special - Cross Ignites (48x48)
- **Position in sheet:** 480,0 to 527,47
- **Description:** Frame ESPECIAL ativado APENAS quando a Biblia atinge um inimigo "demoniaco". A cruz na capa da Biblia IGNITA -- muda de dourado (#D4A017) para VERMELHO INCANDESCENTE (#CC2200) com nucleo branco. O brilho vermelho irradia 4px ao redor da cruz. As paginas do livro TREMEM VIOLENTAMENTE -- bordas de paginas vibram 2px para cada lado. Marcadores de pagina ENDURECEM (ficam retos, apontando para o inimigo como agulhas). A placa metalica da lombada BRILHA com calor (#8C9EAE muda para #CC8844 nas bordas). 6-8 particulas de FOGO SAGRADO (#CC2200 + #FFD700 mix) irradiam do livro. A Biblia inteira TREME no frame -- outline ondula. A mensagem visual: o livro DETECTOU mal e esta REAGINDO.

### Frame 22: Demon Special - Holy Judgment
- **Position in sheet:** 528,0 to 575,47
- **Description:** A cruz vermelha atinge BRILHO MAXIMO -- quase toda a capa esta banhada em vermelho (#CC2200). Do livro, 4 colunas de luz VERMELHA-DOURADA (mix #CC2200 + #FFD700) disparam nas 4 direcoes cardeais (cada coluna 3px largura, 20px comprimento). Paginas ERUPTAM mais violentamente que no swing normal -- 10-12 paginas voam, e cada uma esta PEGANDO FOGO nas bordas (1px #CC2200 ao redor de cada pagina #F0E6C8). Texto "EXORCIZA!" aparece em letras pequenas (16x6px) acima do livro -- vermelho (#CC2200) com sombra preta. A Biblia parece uma BOMBA NUCLEAR DE FE prestes a detonar.

### Frame 23: Demon Special - Purification Complete
- **Position in sheet:** 576,0 to 623,47
- **Description:** Frame final da sequencia demoniaca. A luz vermelha RETRAI rapidamente para a cruz. As colunas de luz se recolhem. Paginas flamejantes descem flutuando (5-6 paginas com fogo apagando). A cruz retorna ao dourado (#D4A017) mas com residuo de brilho vermelho nas bordas (1px #CC2200, 30% opacity) -- levara 2 segundos para desaparecer completamente. Um circulo de CINZA SAGRADA (#4A4A4A com sparkles #FFE8A0) marca o chao ao redor do ponto de impacto (20px diametro). O texto "EXORCIZA!" desvanece. A Biblia "respira" pesadamente -- pulsacao mais intensa que o idle normal.

## Sprite Sheet Summary

### Weapon Sheet (48x48 per frame, 1152x48 total)

| Frame | Name                    | Position      | Purpose                          |
|-------|-------------------------|---------------|----------------------------------|
| 0     | static                  | 0-47          | Inventory / UI icon              |
| 1     | swing_windup            | 48-95         | Attack wind-up                   |
| 2     | swing_smite             | 96-143        | Attack peak velocity             |
| 3     | swing_contact           | 144-191       | Hit moment / judgment            |
| 4     | impact_gloria_1         | 192-239       | "GLORIA!" appear                 |
| 5     | impact_gloria_2         | 240-287       | "GLORIA!" peak                   |
| 6     | impact_gloria_3         | 288-335       | "GLORIA!" fade                   |
| 7     | impact_divine_pillar    | 336-383       | Light column overlay             |
| 8     | idle_pulse_bright       | 384-431       | Idle holy pulse A                |
| 9     | idle_pulse_dim          | 432-479       | Idle holy pulse B                |
| 10    | demon_cross_ignite      | 480-527       | Demon detection activation       |
| 11    | demon_holy_judgment     | 528-575       | Demon purification peak          |
| 12    | demon_purified          | 576-623       | Demon purification complete      |

### Particle/FX Sheet (32x32 per frame, 576x32 total)

| Frame | Name                    | Position      | Purpose                          |
|-------|-------------------------|---------------|----------------------------------|
| 0     | aura_full               | 0-31          | Faith particle full glow         |
| 1     | aura_mid                | 32-63         | Faith particle mid glow          |
| 2     | aura_dim                | 64-95         | Faith particle dim               |
| 3     | aura_flicker            | 96-127        | Faith particle unstable flicker  |
| 4     | page_fresh              | 128-159       | Flying page intact               |
| 5     | page_tumbling           | 160-191       | Flying page mid-rotation         |
| 6     | page_flat               | 192-223       | Flying page face-on              |
| 7     | page_disintegrate       | 224-255       | Page dissolving to faith sparks  |
| 8     | divine_ray_launch       | 256-287       | Holy ray projectile start        |
| 9     | divine_ray_peak         | 288-319       | Holy ray max intensity           |
| 10    | divine_ray_fade         | 320-351       | Holy ray failing/fading          |

## Phaser 3 Atlas Key
```
key: 'weapon_biblia_sagrada'
frameWidth: 48
frameHeight: 48
```
```
key: 'fx_biblia_particles'
frameWidth: 32
frameHeight: 32
```

## Phaser 3 Animation Config
```javascript
// Swing attack (3 frames, fast and heavy)
this.anims.create({
    key: 'biblia_swing',
    frames: this.anims.generateFrameNumbers('weapon_biblia_sagrada', { start: 1, end: 3 }),
    frameRate: 10,
    repeat: 0
});

// Impact "GLORIA!" (with divine pillar)
this.anims.create({
    key: 'biblia_impact',
    frames: this.anims.generateFrameNumbers('weapon_biblia_sagrada', { start: 4, end: 7 }),
    frameRate: 8,
    repeat: 0
});

// Idle holy pulse
this.anims.create({
    key: 'biblia_idle',
    frames: this.anims.generateFrameNumbers('weapon_biblia_sagrada', { start: 8, end: 9 }),
    frameRate: 2, // Slow, reverent breathing
    repeat: -1
});

// Demon special sequence
this.anims.create({
    key: 'biblia_demon_special',
    frames: this.anims.generateFrameNumbers('weapon_biblia_sagrada', { start: 10, end: 12 }),
    frameRate: 6,
    repeat: 0
});

// Aura particle cycle (spawn multiple, offset timing)
this.anims.create({
    key: 'biblia_aura',
    frames: this.anims.generateFrameNumbers('fx_biblia_particles', { start: 0, end: 3 }),
    frameRate: 4,
    repeat: -1
});

// Flying page lifecycle
this.anims.create({
    key: 'biblia_page_fly',
    frames: this.anims.generateFrameNumbers('fx_biblia_particles', { start: 4, end: 7 }),
    frameRate: 6,
    repeat: 0
});

// Divine ray projectile
this.anims.create({
    key: 'biblia_divine_ray',
    frames: this.anims.generateFrameNumbers('fx_biblia_particles', { start: 8, end: 10 }),
    frameRate: 10,
    repeat: -1
});
```

## Particle Effects

### Aura de Fe (constante ao redor da Biblia)
- 4-6 particulas orbitando simultaneamente
- Usa frames aura_full -> aura_mid -> aura_dim -> aura_flicker em ciclo
- Orbita eliptica (20px x 14px) ao redor da Biblia
- Velocidade de orbita: 1 volta completa em 3000ms
- Cada particula em offset de timing diferente
- Opacity: 0.4 base, pisca ate 0.8 aleatoricamente

### Paginas Voando (durante ataque)
- 6-10 particulas spawnam no momento do swing_contact
- Usa frames page_fresh -> page_tumbling -> page_flat -> page_disintegrate
- Direcao: radial 360 graus com gravidade leve (arco parabolico)
- Velocidade inicial: 100-200px/s (variado)
- Lifetime: 800-1200ms
- Rotacao: cada pagina gira individualmente (90-180 graus/s)
- No final, cada pagina se dissolve em 2-3 sparkles de fe (#FFE8A0)

### Raio Divino (projetil de longo alcance)
- Spawna da cruz da Biblia durante ataques especiais
- Usa frames divine_ray_launch -> divine_ray_peak -> divine_ray_fade em loop
- Velocidade: 300px/s
- Alcance: 200px
- Dano: 25 HP + "blessed" debuff (zumbi lento por 2s)
- Colisao: ao atingir, spawna 4-6 faith particles + 2-3 pages

### Faith Sparkles (ambient, sempre ativo)
- Emitter permanente: 1 particula a cada 500ms
- Cor: #FFE8A0
- Tamanho: 1-2px
- Lifetime: 600ms
- Direcao: flutuam para cima com leve drift lateral
- Opacity: 0.3 -> 0.8 -> 0.0 (appear, peak, fade)

---

## Audio Sincronizado

| Evento | Som | Duracao | Trigger |
|---|---|---|---|
| Wind-up | Coro angelical crescendo + whoosh pesado | 500ms | Frame 1 |
| Smite | THUD massivo + paginas farfalhando + flash celestial | 400ms | Frame 3 |
| "GLORIA!" | VOZ DE DACIOLO gritando "GLORIA A DEUS!" | 1200ms | Frame 4 |
| Raio divino | Harpa celestial distorcida + zap eletrico | 300ms | Projetil spawn |
| Idle | Sussurro de oracoes + hum grave | loop 2000ms | Frames 8-9 |
| Page flutter | Farfalhar de paginas antigo | 200ms | Particula de pagina spawn |
| Demon detect | Grito demoniaco reverso + alarme de igreja | 600ms | Frame 10 |
| Exorcismo | Coro dramatico + explosao + "SAAAAI DEMONIO!" | 1500ms | Frame 11 |
| Purificacao | Sino de igreja + eco reverberante | 800ms | Frame 12 |
| Bordao random | "GLORIA A DEUUUUS!" / "HABACUQUE!" / "O NOME DE JESUS!" | 1500ms | Random 30% |

---

## Interacoes Especiais

### Contra Inimigos "Demoniacos" (flag: demonic)
- Ativa sequencia demon_cross_ignite -> demon_holy_judgment -> demon_purified
- Dano 3x contra inimigos com flag demoniaca
- Area of effect: 48px ao redor do impacto (purificacao em area)
- Inimigos demoniacos sao CONVERTIDOS em aliados temporarios por 5s (andam desorientados gritando "GLORIA!")

### Contra Bolsonaro
- A Biblia brilha EXTRA -- Daciolo considera que esta exorcizando o anticristo
- Dano 1.5x + stun 2s
- Texto especial: "ARREPENDE-TE!" ao inves de "GLORIA!"

### Contra Lula
- Nenhuma interacao especial de dano
- Mas paginas voando formam brevemente a palavra "URSAL" antes de se dispersar (easter egg)

### Contra BolsoLula (boss fusion)
- Ativa automaticamente demon_special em LOOP -- a Biblia detecta niveis extremos de mal
- Dano 2x continuo + conversao forcada tenta dividir a fusao
- "GLORIIIIA! SAAAAI SATANAS! SAAAAI COMUNISTA! SAAAAI TUDO!"

---

## Art Generation Prompts

### Style Preamble (prepend to ALL prompts)
```
Style: grotesque underground comix, Robert Crumb inspired, thick uneven black outlines,
heavy shadows, saturated-dirty colors, pixel art, top-down isometric perspective,
Brazilian satirical political cartoon, B-movie horror meets religious iconography,
intentionally rough and asymmetric. The Bible looks like a MEDIEVAL WAR WEAPON
that happens to contain scripture. Sacred AND brutal simultaneously.
```

### Frame 0: Static / Inventory Icon (48x48)

**Stable Diffusion / DALL-E:**
```
A MASSIVE grotesquely oversized Holy Bible viewed from above in top-down isometric perspective,
pixel art 48x48 pixels. Worn black leather cover cracked with age, a large golden cross
dominates the front cover (hand-drawn, imperfect). The spine is REINFORCED WITH A STEEL PLATE
bolted on with visible hex rivets -- looks like medieval armor welded to a holy book. Pages
visible on the side are THICK like a brick, cream-colored with gold gilt edges worn and
irregular. Multiple colorful bookmark ribbons (red, blue, green, purple, yellow) hang
chaotically from all sides like tentacles. Dents and scratches on the metal plate -- this
Bible has seen COMBAT. Thick 2px black outlines, Robert Crumb underground comix style.
Drop shadow. Transparent background. Game weapon sprite. The book is BRUTAL -- it could kill
someone and absolve them simultaneously.
```

**Midjourney:**
```
/imagine pixel art 48x48, top-down view of grotesquely oversized Holy Bible with steel-plated
reinforced spine and rivets, worn black leather cover with golden cross, thick brick-like
pages, chaotic colorful bookmark ribbons everywhere, battle-damaged, Robert Crumb underground
comix thick outlines, medieval war weapon meets scripture, game weapon sprite, transparent
background --ar 1:1 --s 250 --no photorealistic
```

### Frames 1-3: Swing Animation (48x48)

**Stable Diffusion / DALL-E:**
```
Three frame sprite sheet (144x48) of a giant Holy Bible being swung as a weapon, pixel art
48x48 per frame. Frame 1: Bible raised high, glowing from within, pages splaying open at base,
golden cross brightening, divine sparkles. Frame 2: Bible at peak velocity smashing downward,
holy rays shooting from cross, pages flying violently, bookmark ribbons whipping behind.
Frame 3: Bible SLAMS flat at impact, massive squash deformation, explosion of holy light rays,
pages ERUPT upward, divine light column descends from above, shockwave ring. Steel spine plate
cracks on impact. Robert Crumb underground comix style, thick outlines. Transparent background.
Game attack animation.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 144x48, 3 frames of giant Holy Bible swing attack, wind-up
with divine glow, peak velocity with holy rays and flying pages, massive impact with light
explosion and page eruption, steel-reinforced spine, Robert Crumb underground comix, game
weapon animation, transparent background --ar 3:1 --s 250
```

### Frames 4-7: Impact "GLORIA!" + Divine Pillar (48x48)

**Stable Diffusion / DALL-E:**
```
Four frame sprite sheet (192x48) showing holy impact effects, pixel art 48x48 per frame.
Frames 1-3: Comic book onomatopoeia "GLORIA!" appearing, peaking at maximum size with vibrating
letters, then fading. Gold chunky hand-lettered text with white highlights, radial holy light
rays, floating scripture pages, angel wings flanking text, musical notes. Frame 4: A column
of divine light descending from above, white core with yellow and gold halos, faith particles
rising within, tiny crosses appearing and disappearing. Underground comix style, hand-lettered
text. Transparent background. Game VFX sprites.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 192x48, 4 frames of "GLORIA!" holy impact text effect and
divine light pillar, gold hand-lettered comic text appearing growing fading, radial holy
rays, floating pages and angel wings, plus holy light column, underground comix style, game
VFX animation, transparent background --ar 4:1 --s 250
```

### Frames 8-9: Idle Holy Pulse (48x48)

**Stable Diffusion / DALL-E:**
```
Two frame sprite sheet (96x48) of a giant Holy Bible at rest with subtle divine idle animation,
pixel art 48x48 per frame. Frame 1: Golden cross on cover pulses brighter with faint holy
halo around the book, page corners lifting as if stirred by invisible wind, bookmark ribbons
sway left, faith sparkle in corner. Frame 2: Cross dims, halo fades, sparkle moves to opposite
corner, ribbons sway right, pages settle. Steel-reinforced spine, worn black leather cover.
Robert Crumb underground comix style. Transparent background. Subtle sacred breathing effect.
```

**Midjourney:**
```
/imagine pixel art 96x48 sprite sheet, 2 frames of giant Holy Bible idle animation, golden
cross pulsing glow, faint divine halo, pages stirring, bookmark ribbons swaying, faith
sparkles, steel-plated spine, Robert Crumb underground comix thick outlines, top-down game
sprite, transparent background --ar 2:1 --s 250
```

### Frames 10-12: Demon Special (48x48)

**Stable Diffusion / DALL-E:**
```
Three frame sprite sheet (144x48) of a Holy Bible reacting to demonic presence, pixel art
48x48 per frame. Frame 1: The golden cross on the cover IGNITES to incandescent RED, glowing
intensely, pages trembling violently, bookmark ribbons stiffen like needles pointing at enemy,
sacred fire particles radiate. Frame 2: Red-golden light columns blast in 4 cardinal directions,
burning pages fly everywhere (pages with fire edges), text "EXORCIZA!" appears above in red
letters. Frame 3: Red light retracts to cross, burning pages float down with fire dying,
ash circle on ground with gold sparkles, cross returns to gold with red residue fading.
Grotesque underground comix style. Transparent background. INTENSE holy warfare.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 144x48, 3 frames of Holy Bible detecting demon and activating
exorcism, cross igniting red, sacred fire particles, light columns blasting, burning pages
flying, "EXORCIZA!" text, then purification with ash and fading glow, underground comix
Robert Crumb style, game special attack animation, transparent background --ar 3:1 --s 250
```

### Particle Sprites: Aura, Pages, Divine Rays (32x32)

**Stable Diffusion / DALL-E:**
```
Sprite sheet of holy effect particles (352x32, 11 frames at 32x32 each), pixel art.
Frames 1-4: Golden faith aura particles cycling from full glow to mid to dim to flickering
(circular soft glow, gold/yellow colors, sparkle pixels). Frames 5-8: Flying scripture page
lifecycle -- intact cream page with illegible text, tumbling at angle, face-on with underlined
verse, disintegrating into golden sparkles. Frames 9-11: Divine ray projectile -- concentrated
holy beam with cross tip launching, at peak intensity with scripture spiraling, then fading/failing.
All in Robert Crumb underground comix style, rough edges, intentionally imperfect. Transparent
background. Game particle/VFX sprite assets.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 352x32, 11 frames of holy effect particles at 32x32 each,
golden faith aura glow cycle, flying scripture pages tumbling and disintegrating, divine light
ray beam with cross tip, Robert Crumb underground comix style, game VFX particle sprites,
transparent background --ar 11:1 --s 250
```

---

## Post-Processing Notes
- Apos geracao, limpar para grids exatos de 48x48 (weapon) e 32x32 (particles)
- Contornos pretos GROSSOS e IRREGULARES (2px minimo na arma, 1px em particulas)
- Transparencia limpa, sem artefatos
- Cores ajustadas aos hex codes da paleta
- A cruz NUNCA deve ser perfeitamente simetrica -- mao-desenhada, torta
- Os rebites na placa metalica devem ser VISIVEIS e GRANDES
- Paginas voando devem ter micro-texto mesmo que ilegivel
- Os marcadores de pagina coloridos sao ESSENCIAIS ao visual -- nao simplificar
- Assimetria intencional em TUDO -- nada reto, nada limpo
- Montar sprite sheets horizontais: 624x48 (weapon, 13 frames) e 352x32 (particles, 11 frames)

## Notes for Artist
- A Biblia do Daciolo e a fusao IMPOSSIVEL de objeto sagrado e arma bruta -- este paradoxo e o humor
- A placa metalica na lombada deve parecer SOLDADA por alguem sem treinamento -- brutalmente funcional
- Os marcadores de pagina CAOTICOS sugerem que Daciolo marca TUDO como importante (porque TUDO e importante para ele)
- A aura dourada constante mostra que a fe e REAL neste universo do jogo -- a Biblia tem poder literal
- O efeito "GLORIA!" deve ser GRITADO visualmente -- letras tremendo, tamanho exagerado, impossivel de ignorar
- A reacao a demonios e VISCERAL -- a Biblia DETECTA e REAGE sozinha, Daciolo apenas segura
- O raio divino como projetil combina distancia com a personalidade melee da arma (dualidade sagrado/mundano)
- Robert Crumb style: tracos grossos, textura pesada, NADA e limpo ou sagrado de verdade -- tudo e grotesco, mesmo o divino
- A Biblia deve parecer que PESA -- movimento pesado, impacto pesado, presenca pesada
- O contraste entre a reverencia religiosa e a violencia absurda e ESSENCIAL para o tom do jogo
