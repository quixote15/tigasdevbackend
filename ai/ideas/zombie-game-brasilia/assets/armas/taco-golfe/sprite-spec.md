# Taco de Golfe Nuclear - Especificacao de Sprites

## Arma Exclusiva do Trampi - "Zumbis de Brasilia"

---

## Visao Geral

- **Nome**: Taco de Golfe Nuclear
- **Tipo**: Arma corpo-a-corpo (melee) com projetil secundario
- **Dono**: Trampi (exclusiva)
- **Dimensao do Taco**: 32x32px (sprite da arma)
- **Dimensao do Projetil**: 32x32px (bola de golfe com cara do Trump)
- **Dimensao da Explosao**: 48x48px (efeito de explosao)
- **Layout da Sprite Sheet**: Strip horizontal, 1 linha por animacao
- **Formato**: PNG com alpha transparency

---

## Paleta de Cores -- Taco

| Elemento                | Hex Code    | Uso                                        |
|-------------------------|-------------|--------------------------------------------|
| Shaft Dourado           | `#DAA520`   | Corpo principal do taco (haste)            |
| Shaft Highlight         | `#FFD700`   | Highlights metalicos ao longo da haste     |
| Shaft Shadow            | `#B8860B`   | Sombra lateral da haste                    |
| Shaft Brilho            | `#FFF8DC`   | Pontos de brilho (1px, espalhados)         |
| Clubhead                | `#CFB53B`   | Cabeca do taco (parte que bate)            |
| Clubhead Face           | `#FFD700`   | Face de impacto (mais brilhante)           |
| Clubhead Shadow         | `#8B7500`   | Sombra da cabeca                           |
| Grip                    | `#8B0000`   | Empunhadura (couro vermelho escuro)        |
| Grip Textura            | `#660000`   | Cross-hatching na empunhadura              |
| Outline                 | `#0D0D0D`   | Linhas grossas irregulares 2px             |
| Simbolo Nuclear         | `#FFFF00`   | Trefoil nuclear na cabeca do taco          |
| Simbolo Nuclear BG      | `#1A1A1A`   | Fundo do simbolo nuclear                   |
| Glow Nuclear            | `#CCFF00`   | Glow esverdeado-amarelado ao redor         |

## Paleta de Cores -- Bola de Golfe (Projetil)

| Elemento                | Hex Code    | Uso                                        |
|-------------------------|-------------|--------------------------------------------|
| Bola Branca             | `#F5F5F5`   | Corpo da bola                              |
| Bola Shadow             | `#CCCCCC`   | Sombra inferior da bola                    |
| Bola Dimples            | `#E0E0E0`   | Textura de dimples (2-3px, padrao circular)|
| Rosto Trump - Pele      | `#FF6B00`   | Rosto laranja neon do Trump na bola        |
| Rosto Trump - Cabelo    | `#FF8C00`   | Topete miniatura                           |
| Rosto Trump - Boca      | `#CC0000`   | Boca aberta gritando                       |
| Rosto Trump - Olhos     | `#000000`   | Olhos apertados (1px cada)                 |
| Trail Flamejante        | `#FF4500`   | Trail de fogo ao voar                      |
| Trail Interno           | `#FFFF00`   | Centro do trail (mais quente)              |

## Paleta de Cores -- Explosao

| Elemento                | Hex Code    | Uso                                        |
|-------------------------|-------------|--------------------------------------------|
| Explosao Centro         | `#FFFFFF`   | Centro branco do flash                     |
| Explosao Medio          | `#FFD700`   | Anel dourado                               |
| Explosao Exterior       | `#FF4500`   | Anel externo alaranjado                    |
| Detritos Dourados       | `#DAA520`   | Particulas de ouro falso                   |
| Texto "TREMENDOUS"      | `#FFD700`   | Texto que aparece na explosao              |
| Texto Outline           | `#8B0000`   | Outline do texto                           |
| Nuvem de Fumaca         | `#CCAA33`   | Fumaca dourada pos-explosao                |
| Fumaca Shadow           | `#8B7500`   | Sombra da fumaca                           |

---

## SPRITE SHEET 1: Taco de Golfe -- Estados

### Sprite Sheet: `taco_golfe_states.png` -- 320x32px (10 frames de 32x32px)

#### Frame 0: Taco -- Icone de Inventario
- **Posicao**: 0,0 a 31,31
- **Descricao**: Taco de golfe visto de frente, diagonal 45 graus (grip embaixo-esquerda, clubhead topo-direita). Taco DOURADO CAFONA -- nao elegante, nao sutil. Dourado GRITANTE como joalheria de camelô. Haste com 3px de largura, levemente irregular (nao perfeitamente reta -- estilo Crumb). Clubhead desproporcional (8x6px -- grande demais para a haste). Face do clubhead com simbolo nuclear simplificado (trefoil 3x3px: circulo central 1px + 3 "petala" de 1px, amarelo no fundo preto). Empunhadura com textura de couro (cross-hatching diagonal vermelho escuro, 6px de comprimento). 2-3 pontos de brilho (1px branco) ao longo da haste. Glow esverdeado sutil ao redor do clubhead (1px, #CCFF00, 30% opacity) -- radiacao nuclear.
- **Outline**: 2px, irregular, preto. O taco deve parecer PESADO e CAFONA.

#### Frame 1: Taco -- Segurado em Idle (mao microscopica)
- **Posicao**: 32,0 a 63,31
- **Descricao**: Taco na posicao de repouso, vertical, apoiado no chao. A empunhadura esta no topo onde a mao microscopica do Trampi a segura (ou tenta). DETALHE CRUCIAL: A mao do Trampi (3x3px) cobre apenas 50% da empunhadura. O resto esta exposto. O taco parece a PONTO DE CAIR. 1px de gap entre mao e grip (sugerindo grip precario). Clubhead no chao, face virada para a "camera". Glow nuclear constante.
- **Nota**: Este frame e usado como OVERLAY no sprite do Trampi durante idle.

#### Frame 2: Taco -- Wind-up (puxado para tras)
- **Posicao**: 64,0 a 95,31
- **Descricao**: Taco puxado para tras e para cima, angulo 135 graus (clubhead atras-acima). Haste CURVADA levemente (2px de bow) pelo esforço -- exagero de deformacao organica. Empunhadura com a mao microscopica mais agarrada (hand_grab_success, mas precario). 1 motion line (1px, branco 30% opacity) indicando inicio de movimento. Glow nuclear se intensifica para 50% durante o wind-up.

#### Frame 3: Taco -- Mid-Swing (velocidade maxima)
- **Posicao**: 96,0 a 127,31
- **Descricao**: Taco em BLUR de swing. Nesta velocidade, a haste e quase invisivel -- substituida por um ARCO de motion blur (3 linhas paralelas de 1px: dourado, branco 50%, dourado). O clubhead e um BORRÃO dourado na ponta (5x5px de blur, cores mescladas de dourado e branco). 3 motion lines fortes atras (1px cada, branco 60%, 40%, 20% opacity decrescente). Glow nuclear se torna TRAIL (streak de #CCFF00 ao longo do arco do swing).
- **Nota tecnica**: Este frame e o mais "abstrato" -- a velocidade impossibilita detalhes. So linhas de forca e blur.

#### Frame 4: Taco -- Impacto (momento do contato)
- **Posicao**: 128,0 a 159,31
- **Descricao**: Taco no MOMENTO EXATO de contato com bola/inimigo. Clubhead DEFORMADO pelo impacto: face achata 2px (squash), bordas se expandem 1px (splash metalico). Haste vibra (representado por 2 linhas paralelas em vez de 1 -- vibracao visual). Starburst de impacto no ponto de contato (6x6px, branco-amarelo, 8 raios). Simbolo nuclear no clubhead BRILHA (glow maximo, #CCFF00 2px). 2-3 particulas de "faísca dourada" (1x1px, #FFD700) no ponto de impacto. Empunhadura vibra na mao microscopica (mao e taco se desfocam juntos).

#### Frame 5: Taco -- Follow-through (pos-impacto)
- **Posicao**: 160,0 a 191,31
- **Descricao**: Taco apos o impacto, continuando o arco. Angulo 45 graus (oposto ao wind-up). Haste voltando a forma normal (bounce metalico). Clubhead com resíduo de impacto: 1-2 particulas douradas ainda saindo. Motion lines decrescentes (1px, fade). Glow nuclear retornando ao normal (50% -> 30%). A mao microscopica QUASE solta o taco -- 2px de separacao entre grip e mao (quase escapou mas segurou).

#### Frame 6: Taco -- Disparo de Bola (lancamento de projetil)
- **Posicao**: 192,0 a 223,31
- **Descricao**: Frame especial para quando o taco DISPARA uma bola de golfe. O clubhead esta aberto (face virada para frente) e uma bola de golfe (6x6px, branca) esta SAINDO da face com starburst de lancamento. A bola ja mostra a carinha do Trump (miniatura 3x3px: pele laranja, topete, boca aberta). Arco de energia entre clubhead e bola (2 linhas curvas, #FFD700, 1px). Fumaca de lancamento atras do clubhead (3x3px, #CCAA33, 50% opacity).

#### Frame 7: Taco -- Dano (taco danificado)
- **Posicao**: 224,0 a 255,31
- **Descricao**: Taco apos muito uso -- DANIFICADO. Haste com 1 rachadura (linha diagonal 1px, #8B7500). Clubhead levemente entortado (2px de desalinhamento com a haste). Brilho dourado reduzido (menos pontos de highlight). Glow nuclear IRREGULAR (pisca em vez de constante). Grip desgastado (cross-hatching mais esparso). O taco parece que vai QUEBRAR a qualquer momento.
- **Nota**: Usado quando HP do Trampi esta baixo ou quando taco acerta muitos hits.

#### Frame 8: Taco -- Idle Flutuante (icone de loot)
- **Posicao**: 256,0 a 287,31
- **Descricao**: Taco flutuando no ar como item de loot. Rotacao lenta sugerida (angulo ligeiramente diferente do frame 0 -- 50 graus em vez de 45). Brilho MAXIMO -- todos os pontos de highlight ativos. Glow nuclear FORTE (2px, #CCFF00, 60% opacity). Particulas de sparkle ao redor (3 sparkles de 1px, dourados, posicoes aleatorias no frame). Sombra no chao abaixo (elipse 12x4px, 30% opacity).
- **Nota**: Para quando o jogador pode coletar o taco.

#### Frame 9: Taco -- Quebrado (destruido)
- **Posicao**: 288,0 a 319,31
- **Descricao**: Taco PARTIDO AO MEIO. Haste separada em 2 pedacos com gap de 3px entre eles. Clubhead descolado, inclinado. Fragmentos dourados flutuando (3 particulas 1x1px). Glow nuclear APAGADO (0% -- a energia morreu). Simbolo nuclear rachado (linhas de fratura cruzando o trefoil). Grip solto, caindo. Tudo em decomposicao metalica.
- **Nota**: Frame final quando o taco e destruido ou na death animation do Trampi.

---

## SPRITE SHEET 2: Bola de Golfe (Projetil)

### Sprite Sheet: `taco_golfe_projetil.png` -- 256x32px (8 frames de 32x32px)

#### Frame 0: Bola -- Idle/Spawn
- **Posicao**: 0,0 a 31,31
- **Descricao**: Bola de golfe flutuando momentaneamente apos ser lancada. Esfera branca (#F5F5F5) de 12x12px centralizada no frame. Textura de dimples: 8-10 pontos levemente mais escuros (#E0E0E0) distribuidos na superficie em padrao semi-regular. ROSTO DO TRUMP centralizado na bola: Area de 8x8px no centro frontal.
  - **Rosto na Bola**: Fundo laranja neon (#FF6B00) circular. Topete miniatura (3px, #FF8C00) no topo. Olhos apertados de furia (2 pixels pretos, 1x1px cada, proximos). Boca aberta gritando (2x1px, #CC0000). Nariz bulboso (1px, #CC4400). EXPRESSAO: raiva/grito -- a bola GRITA enquanto voa.
- **Glow**: 1px de glow alaranjado ao redor (#FF6B00, 30% opacity) por causa do rosto.

#### Frame 1: Bola -- Voo (rotacao 0 graus)
- **Posicao**: 32,0 a 63,31
- **Descricao**: Bola em voo, rosto do Trump virado para frente. Trail de fogo atras: 3 particulas em triangulo (3x2px cada, cores: #FFFF00 mais proximo, #FF4500 medio, #CC0000 mais distante). A bola em si rota levemente -- dimples em posicao A. Motion lines: 2 linhas de 1px (#FFFFFF, 40% opacity) saindo de tras. Bola ligeiramente squashed na direcao do voo (11x13px em vez de 12x12 -- compressao de velocidade).

#### Frame 2: Bola -- Voo (rotacao 90 graus)
- **Posicao**: 64,0 a 95,31
- **Descricao**: Bola girou 90 graus -- rosto do Trump agora de PERFIL (lado esquerdo visivel). Topete no topo-esquerdo. 1 olho visivel. Nariz projetado para a esquerda (1px). Boca visivel de perfil. Trail de fogo mais longo (4 particulas). Dimples em posicao B (rotacao da textura). Motion lines mais intensas (3 linhas).

#### Frame 3: Bola -- Voo (rotacao 180 graus)
- **Posicao**: 96,0 a 127,31
- **Descricao**: Bola girou 180 graus -- rosto do Trump virado para TRAS (nuca visivel). Ve-se: parte de tras do topete (3px, #FF8C00), nuca laranja neon, SEM face. A bola parece "inocente" por um frame -- so uma bola branca com um topete atras. Trail de fogo maximo (5 particulas, mais brilhante).

#### Frame 4: Bola -- Voo (rotacao 270 graus)
- **Posicao**: 128,0 a 159,31
- **Descricao**: Bola girou 270 graus -- rosto de PERFIL DIREITO. Espelho do Frame 2. Topete no topo-direito. Completa o ciclo de rotacao (frames 1-4 em loop = bola girando). Trail diminuindo (3 particulas -- bola perdendo energia).

#### Frame 5: Bola -- Pre-Impacto (piscando)
- **Posicao**: 160,0 a 191,31
- **Descricao**: Bola prestes a explodir. Rosto do Trump com expressao de PANICO: olhos arregalados (2x2px cada -- o DOBRO do normal), boca em "O" de medo, topete eriçado. A bola PISCA: alternando entre normal e branco-brilhante (#FFFFFF tint 50%) a cada 60ms. Glow ao redor intensifica para 3px (#FF4500). Trail para, bola desacelerando. Rachaduras comecam na superficie (2 linhas finas de 1px).

#### Frame 6: Bola -- Explosao Inicial
- **Posicao**: 192,0 a 223,31
- **Descricao**: MOMENTO DA EXPLOSAO. A bola se desfaz. Centro: flash branco (6x6px, #FFFFFF). Anel medio: dourado explosivo (10x10px anel, #FFD700). Anel externo: laranja-fogo (14x14px anel, #FF4500). Fragmentos da bola voam: 4-6 pedacos brancos (2x2px cada) irradiando em direcoes cardinais. O ROSTO DO TRUMP se separa da bola e voa como particula independente (4x4px, subindo). Micro-topete se desintegra em 2 fios (1px cada, subindo).
- **Texto**: "TREMENDOUS!" comeca a aparecer (letras aparecendo da esquerda, 3px de altura, #FFD700, outline #8B0000).

#### Frame 7: Bola -- Explosao Final
- **Posicao**: 224,0 a 255,31
- **Descricao**: Explosao se expandindo e dissipando. Centro: 8x8px de fumaca dourada (#CCAA33, 60% opacity). Aneis se expandem para 20x20px e 26x26px, opacidade caindo para 30%. Fragmentos da bola nos cantos do frame, quase sumindo. Rosto do Trump particula faz FADE (50% opacity, subindo). "TREMENDOUS!" em tamanho maximo (preenche 70% da largura do frame), comecando fade (80% opacity). 4-6 sparkles dourados finais dispersando. Nuvem de fumaca dourada se forma (8x5px, #CCAA33, parte inferior do frame).
- **SE A BOLA ERROU**: Em vez de "TREMENDOUS!", aparece "FAKE NEWS!" em vermelho (#CC0000). A explosao e MENOR (aneis 60% do tamanho). O rosto do Trump na particula tem expressao de RAIVA em vez de satisfacao.

---

## SPRITE SHEET 3: Efeito de Explosao Expandido

### Sprite Sheet: `taco_golfe_explosao.png` -- 192x48px (4 frames de 48x48px)

#### Frame 0: Explosao -- Flash Inicial
- **Posicao**: 0,0 a 47,47
- **Descricao**: Flash branco puro no centro (12x12px, #FFFFFF 100%). Starburst de 8 raios saindo do centro (1px cada, #FFD700, comprimento 10px). Onda de choque circular comecando (outline 1px, #FF4500, raio 8px). Detritos dourados iniciais: 6 particulas (2x2px, #DAA520) comecando a se mover do centro. O chao sob a explosao racha (3 linhas radiais 1px).

#### Frame 1: Explosao -- Expansao
- **Posicao**: 48,0 a 95,47
- **Descricao**: Flash diminui para 8x8px (60% opacity). Starburst raios se estendem para 18px. Onda de choque expande para raio 16px (outline mais fino, 1px, #FF4500, 70% opacity). Bola de fogo se forma: esfera de 10x10px, gradiente de #FFFFFF centro -> #FFD700 meio -> #FF4500 borda. Detritos dourados espalhando: 8 particulas em todas direcoes, cada vez mais distantes. Fumaca comeca a subir (2-3 wisps de 3x2px, #CCAA33, 40% opacity).

#### Frame 2: Explosao -- Pico
- **Posicao**: 96,0 a 143,47
- **Descricao**: PICO DA EXPLOSAO. Bola de fogo em tamanho maximo: 16x16px, core dourado brilhante. "TREMENDOUS!" (ou "FAKE NEWS!") em tamanho MAXIMO: 6px de altura, preenche a largura do frame. Onda de choque no limite do frame (raio 22px, quase saindo, 30% opacity). Detritos dourados nos cantos. Fumaca grossa: 4-5 wisps, #CCAA33 com #8B7500, 50% opacity, subindo. Framgmentos da face do Trump visiveis na fumaca (1-2 pixels laranja dispersos).

#### Frame 3: Explosao -- Dissipacao
- **Posicao**: 144,0 a 191,47
- **Descricao**: Explosao dissipando. Bola de fogo em fade: 12x12px, 40% opacity, cor mudando para #CCAA33 (fumaca). Sem starburst. Sem onda de choque. Texto fazendo fade (30% opacity, sumindo). Fumaca dominante: 6-8 wisps ocupando 60% do frame, dourado-sujo, dissipando para cima. Poucos detritos restantes (2-3 particulas lentas, quase paradas). Marca no chao: circulo de 10px de diâmetro, escurecido (#333333, 20% opacity) -- cratera da explosao.
- **Nota**: Apos este frame, apenas a marca no chao persiste (fade de 5 segundos no engine).

---

## SPRITE SHEET 4: Swing Completo do Taco (Overlay para Trampi)

### Sprite Sheet: `taco_golfe_swing.png` -- 128x32px (4 frames de 32x32px)

Estes frames sao usados como OVERLAY no sprite do Trampi durante o ataque.

#### Frame 0: Swing -- Posicao Traseira
- **Posicao**: 0,0 a 31,31
- **Descricao**: Taco atras do Trampi, angulo 140 graus (quase vertical para tras). Empunhadura na area da mao do personagem (overlay se alinha com hand position). Haste curvada com tensao. Clubhead no topo, brilhando. Anchor point: (8, 24) -- posicao da mao.

#### Frame 1: Swing -- Arco Descendente
- **Posicao**: 32,0 a 63,31
- **Descricao**: Taco descendo em arco. Angulo 90 graus (horizontal). Motion blur na cabeca do taco (3px de streak). Haste em deformacao de chicote (curva em S leve). Glow nuclear intensificado. Trail dourado.

#### Frame 2: Swing -- Ponto Baixo (Impacto)
- **Posicao**: 64,0 a 95,31
- **Descricao**: Taco no ponto mais baixo do arco (ponto de impacto). Angulo 0 graus (apontando para a direita). Clubhead DEFORMADO pelo squash de impacto. Starburst no ponto de contato. Vibracao na haste (linhas duplas). Glow MAXIMO.

#### Frame 3: Swing -- Follow-Through Ascendente
- **Posicao**: 96,0 a 127,31
- **Descricao**: Taco subindo apos impacto. Angulo 40 graus (apontando frente-cima). Haste voltando a forma normal. Clubhead com residuo de brilho decrescente. Motion lines fracas. Glow retornando ao normal.

---

## Mecanica da Arma

### Ataque Melee (Swing Basico)
```
Dano: 25 HP
Alcance: 32px a frente do Trampi
Hitbox: Arco de 90 graus, raio 32px
Cooldown: 800ms
Animacao: 375ms (3 frames de ataque do Trampi + overlay do taco)
```

### Ataque Projetil (Bola de Golfe)
```
Dano: 35 HP (impacto) + 15 HP (explosao AoE)
Alcance: 200px (distancia maxima antes de explodir sozinha)
Velocidade: 180px/s
Hitbox da bola: circulo 8px raio
Hitbox da explosao: circulo 24px raio
Cooldown: 3000ms (separado do melee)
Rotacao da bola: 4 frames loop (frames 1-4 do projetil sheet), 100ms por frame

Comportamento:
  - Lancada do clubhead na direcao que o Trampi esta virado
  - Rota continuamente (loop frames 1-4)
  - Trail de fogo atras (particulas procedurais)
  - Ao atingir alvo OU ao percorrer 200px:
    - Frame 5 (pre-impacto, 100ms)
    - Frame 6 (explosao inicial, 80ms)
    - Frame 7 (explosao final, 120ms)
    - Explosao expandida (sheet 3, 4 frames, 400ms total)
  - HIT: "TREMENDOUS!" aparece + dano
  - MISS: "FAKE NEWS!" aparece + Trampi reage
```

### Sistema de Fumble (Interacao com Micro-Maos)
```
A cada swing, roll de 50% para fumble:
  SE FUMBLE:
    - Taco escorrega da mao (sprite do taco move 2px para frente)
    - Delay de 80ms (Trampi tenta re-agarrar)
    - Taco volta a mao (hand_grab_success)
    - Swing com 50ms de atraso (total 425ms em vez de 375ms)
    - Dano reduzido em 20% (20 HP em vez de 25)
  
  SE NAO FUMBLE:
    - Swing normal, dano total
    
NOTA: O fumble NAO afeta o projetil (bola). So o melee.
O lancamento da bola SEMPRE funciona porque soltar e mais facil que segurar.
```

---

## Phaser 3 Atlas Keys

```javascript
const TACO_GOLFE_ATLAS = {
  states:   { key: 'taco_golfe_states',   frameWidth: 32, frameHeight: 32, frames: 10 },
  projetil: { key: 'taco_golfe_proj',      frameWidth: 32, frameHeight: 32, frames: 8  },
  explosao: { key: 'taco_golfe_explosion', frameWidth: 48, frameHeight: 48, frames: 4  },
  swing:    { key: 'taco_golfe_swing',     frameWidth: 32, frameHeight: 32, frames: 4  },
};

// Animacoes
this.anims.create({
  key: 'taco_proj_fly',
  frames: this.anims.generateFrameNumbers('taco_golfe_proj', { start: 1, end: 4 }),
  frameRate: 10,
  repeat: -1
});

this.anims.create({
  key: 'taco_proj_explode',
  frames: this.anims.generateFrameNumbers('taco_golfe_proj', { start: 5, end: 7 }),
  frameRate: 10,
  repeat: 0
});

this.anims.create({
  key: 'taco_explosion_full',
  frames: this.anims.generateFrameNumbers('taco_golfe_explosion', { start: 0, end: 3 }),
  frameRate: 10,
  repeat: 0
});

this.anims.create({
  key: 'taco_swing',
  frames: this.anims.generateFrameNumbers('taco_golfe_swing', { start: 0, end: 3 }),
  frameRate: 12, // Ligeiramente mais rapido que 8fps para swing feel
  repeat: 0
});
```

---

## Notas para o Artista

1. **O TACO E CAFONA**: Dourado de CAMELÔ, nao de joalheria. Brilha demais. Parece falso. PORQUE E FALSO. E ouro de faz-de-conta em cima de metal barato.

2. **O SIMBOLO NUCLEAR E HUMOR**: O taco e "nuclear" mas o simbolo de radiacao e desenhado de qualquer jeito, como se alguem tivesse colado um adesivo torto no clubhead. Nada profissional.

3. **A BOLA COM CARA DO TRUMP E FUNDAMENTAL**: O rosto na bola GRITA enquanto voa. A expressao muda: raiva durante o voo, panico antes de explodir. Isso E a piada visual da arma.

4. **"TREMENDOUS!" vs "FAKE NEWS!"**: A dualidade do resultado e ESSENCIAL. Hit = celebracao ("TREMENDOUS!"). Miss = negacao da realidade ("FAKE NEWS!"). Ambos em fontes irregulares, NUNCA tipografadas.

5. **EXPLOSAO DOURADA**: A explosao nao e fogo normal. E UMA EXPLOSAO DE OURO FALSO. Particulas douradas, fumaca dourada, detritos dourados. Tudo cafona, tudo excessivo.

6. **O FUMBLE DAS MAOS**: O sistema de fumble de 50% e a essencia comica. O Trampi e um BOSS PODEROSO que nao consegue segurar a propria arma. A tensao entre poder e incompetencia manual e o humor INTEIRO.

7. **OUTLINES IRREGULARES SEMPRE**: Nenhuma linha reta. Nenhuma curva perfeita. Tudo tremido, tudo organico, tudo grotesco. Robert Crumb no pixel art.

8. **GLOW NUCLEAR**: O glow esverdeado-amarelado (#CCFF00) no clubhead deve ser SUTIL no idle e INTENSO durante ataques. Sugere perigo real numa embalagem ridicula.
