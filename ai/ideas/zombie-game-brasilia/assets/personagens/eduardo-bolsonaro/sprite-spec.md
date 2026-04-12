# Eduardo Bolsonaro (Bananinha) - Sprite Specification

## Overview
- **Character Type:** Sidekick / Mini-boss
- **Sprite Dimensions:** 64x64px (personagem)
- **Projectile Dimensions:** 32x32px (banana boomerang)
- **Sprite Sheet Layout:** Horizontal strip, 1 row per animation
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (32, 60) -- pes do personagem
- **Perspective:** Top-down levemente isometrica (Y-sorting)

## Color Palette

| Element                  | Hex Code  | Usage                                    |
|--------------------------|-----------|------------------------------------------|
| Cabelo Loiro (base)     | `#D4A017` | Cabelo principal                         |
| Cabelo Loiro (light)    | `#F0C040` | Mechas / highlights                      |
| Cabelo Loiro (shadow)   | `#A07B10` | Sombras do cabelo                        |
| Pele (base)             | `#F5C6A0` | Rosto e bracos                           |
| Pele (shadow)           | `#D4A070` | Sombras da pele                          |
| Pele (highlight)        | `#FFE0C0` | Highlights do rosto redondo              |
| Camiseta Amarela (base) | `#F7DC6F` | Camiseta selecao brasileira              |
| Camiseta Amarela (dark) | `#D4AC0D` | Dobras/sombras da camiseta               |
| Camiseta Verde (detalhe)| `#1E8449` | Gola e detalhes da camiseta selecao      |
| Shorts Azul (base)      | `#2E86C1` | Shorts / bermuda                         |
| Shorts Azul (dark)      | `#1A5276` | Sombras do shorts                        |
| Banana Amarela          | `#F9E154` | Banana (arma principal)                  |
| Banana Madura           | `#C8A415` | Manchas na banana                        |
| Banana Ponta            | `#5D4E37` | Pontas da banana                         |
| Mala Marrom (base)      | `#8B5E3C` | Mala de viagem                           |
| Mala Marrom (dark)      | `#5B3A1E` | Sombras/detalhes da mala                 |
| Mala Metal              | `#A0A0A0` | Fecho/rodinhas da mala                   |
| Olhos (iris)            | `#5DADE2` | Olhos de cachorro abandonado (enormes)   |
| Olhos (brilho)          | `#FFFFFF` | Brilho lacrimal nos olhos                |
| Olhos (lagrima)         | `#AED6F1` | Lagrima permanente no canto do olho      |
| Outline Black           | `#1A1A1A` | Contornos grossos (2-3px, Crumb style)   |
| Shadow Dark             | `#0D0D0D` | Drop shadow, 50% opacity                 |
| Aura Buff (amarela)     | `#FFD700` | Aura Puxa-Saquismo (50% opacity)         |
| Aura Debuff (cinza)     | `#808080` | Aura Orfao Politico (40% opacity)        |
| Fumaca Fuga             | `#D5D8DC` | Particulas de fumaca na fuga             |
| Flash Branco            | `#FFFFFF` | Flash do teleporte                       |

## Anatomia da Caricatura

### Deformidades Chave (OBRIGATORIO em TODOS os frames)
1. **Rosto LUNAR**: Cabeca redonda desproporcional, tipo lua cheia. Ocupa ~40% do sprite. Ratio cabeca:corpo = 1:1.2 (quase igual)
2. **Olhos de Cachorro Abandonado**: Enormes (12-14px de diametro cada), brilhantes, sempre lacrimejantes. Pupilas dilatadas. Sobrancelhas caidas em angulo de suplica
3. **Queixo Inexistente**: Rosto vai do labio inferior direto pro pescoco. ZERO mandibula. Fraqueza literal
4. **Mala GRUDADA**: Mao direita permanentemente segurando a alcinha da mala de viagem. Nunca larga. NUNCA
5. **Banana na Mao Esquerda**: Sempre segurando banana (exceto durante arremesso)
6. **Expressao de Cachorro Perdido**: Boca ligeiramente aberta, labio inferior tremendo (1px vibration)

### Proporcoes (dentro dos 64x64px)
- Cabeca: ~28x26px (absurdamente grande)
- Corpo: ~22x20px
- Pernas: ~14px de altura
- Mala: ~16x14px (sempre ao lado direito)
- Banana: ~12x6px na mao esquerda

---

## IDLE ANIMATION (4 frames)
**Sprite Sheet:** `eduardo_idle.png` -- 256x64px (4 frames x 64px)
**Loop:** Sim, ping-pong
**Frame Rate:** 8 fps (125ms por frame)

### Frame 0: Idle Base
- **Position:** 0,0 a 63,63
- **Descricao:** Eduardo de pe, levemente curvado, postura submissa. Rosto lunar virado ligeiramente para cima (como se procurando o pai). Olhos enormes brilhantes com lagrima no canto esquerdo (1px azul claro). Cabelo loiro penteado pro lado, fios soltos. Camiseta amarela da selecao com gola verde, numero 17 estilizado nas costas (nao visivel neste angulo, mas a borda aparece). Shorts azul. Mao direita segura a alca da mala marrom com rodinhas (mala encostada no chao, ao lado). Mao esquerda segura banana apontando pra cima. Boca entreaberta, expressao perdida. Sombra no chao (4px offset, 40% opacity).
- **Style Notes:** O rosto DEVE ser grotescamente redondo. Os olhos DEVEM parecer os de um golden retriever abandonado na chuva. O corpo e pequeno demais pra cabeca. A mala parece mais pesada que ele.

### Frame 1: Idle Blink / Tremor
- **Position:** 64,0 a 127,63
- **Descricao:** Identico ao Frame 0 mas: olhos semi-fechados (piscada nervosa, palpebras cobrem 60% dos olhos). Labio inferior treme 1px pra baixo. A banana na mao esquerda balanca 1px pro lado. Mala identica. Uma segunda lagrima aparece no olho direito. Leve squash no corpo (1px mais largo, 1px mais baixo) -- ansiedade.
- **Style Notes:** A piscada deve parecer um tique nervoso, NAO um piscar normal. E medo.

### Frame 2: Idle Olhar Pro Lado
- **Position:** 128,0 a 191,63
- **Descricao:** Eduardo olha pra direita (direcao onde o pai estaria). Cabeca rotacionada ~15 graus. Olhos enormes virados pro canto direito, pupilas deslocadas. Sobrancelhas sobem em esperanca patética. Boca forma um "o" pequeno. Banana inclina junto com o corpo (2px pro lado). Mala puxa levemente -- o braco estica. Uma gotinha de suor (2x2px) aparece na testa esquerda.
- **Style Notes:** A expressao deve transmitir desespero de aprovacao. Ele esta SEMPRE procurando o pai.

### Frame 3: Idle Suspiro
- **Position:** 192,0 a 255,63
- **Descricao:** Eduardo suspira. Ombros caem 2px. Cabeca inclina pra frente (queixo -- ou a falta dele -- aponta mais pra baixo). Olhos meio fechados, nao de sono mas de tristeza. Boca fechada, cantos pra baixo. A banana na mao esquerda cai 3px (braco relaxa). Uma pequena nuvem de suspiro (3x2px, cinza claro, 40% opacity) sai da boca. Mala continua estatica, firme no chao.
- **Style Notes:** O suspiro mais patetico do mundo. Ele sente falta do pai. A nuvenzinha de ar e minuscula mas visivel.

---

## WALK ANIMATION (6 frames)
**Sprite Sheet:** `eduardo_walk.png` -- 384x64px (6 frames x 64px)
**Loop:** Sim, ciclico
**Frame Rate:** 10 fps (100ms por frame)
**Direcoes:** Gerar para baixo (default). Rotacionar/espelhar para 4/8 direcoes no Phaser.

### Frame 0: Walk - Passo Direito (contato)
- **Position:** 0,0 a 63,63
- **Descricao:** Pe direito toca o chao, perna esquerda atras. Corpo levemente inclinado pra frente (2px). Cabeca balanca MUITO mais que o corpo (inércia da cabecona -- 3px de oscilacao). Olhos arregalados olhando pra frente com medo. Mala na mao direita esta ARRASTANDO no chao -- rodinhas visiveis com uma linha de movimento (1px) atras. A banana na mao esquerda aponta pra frente como bussola. Sombra acompanha.
- **Style Notes:** A mala TEM que parecer um fardo. Ele arrasta ela com dificuldade visivel. A cabeca balanca como se fosse cair.

### Frame 1: Walk - Transicao Direita-Esquerda
- **Position:** 64,0 a 127,63
- **Descricao:** Ambos os pes quase juntos, corpo no ponto mais alto do ciclo (+2px Y). Cabeca oscila pro lado oposto do Frame 0. Mala levanta levemente do chao (1px -- as rodinhas saem do chao por um instante). Banana verticalmente reta. Olhos focados mas ansiosos.
- **Style Notes:** Momento de "suspensao" -- o corpo sobe mas a cabecona tem delay, cria efeito comico de mola.

### Frame 2: Walk - Passo Esquerdo (contato)
- **Position:** 128,0 a 191,63
- **Descricao:** Espelho do Frame 0 com pe esquerdo na frente. Cabeca balanca pro outro lado (3px). Mala arrasta com rodinha girando (frame alternado de rodinha). A banana aponta levemente pra cima (braco esquerdo oscila natural). Expressao de esforco -- boca apertada, olhos semicerrados.
- **Style Notes:** O esforco de carregar a mala E a cabeca gigante deve ser visivel. Ele se cansa rapido.

### Frame 3: Walk - Transicao Esquerda-Direita
- **Position:** 192,0 a 255,63
- **Descricao:** Similar ao Frame 1, corpo no ponto alto. Cabeca volta pro centro com atraso. Mala no chao novamente, rodinhas apoiadas. Gotinha de suor voa da testa (2x2px, azul claro, saindo pra tras). Banana em posicao neutra.

### Frame 4: Walk - Tropeco na Mala
- **Position:** 256,0 a 319,63
- **Descricao:** Eduardo QUASE tropeca na propria mala. Pe direito bate na roda da mala. Corpo inclina pra frente perigosamente (4px). Olhos ARREGALADOS de panico (pupilas minusculas por 1 frame). Boca aberta em "O". Braco da banana vai pra tras pra equilibrar. A mala gira levemente (~10 graus). Squash no corpo (2px mais largo).
- **Style Notes:** Este frame E a piada. Ele tropeca na PROPRIA mala de fuga. TODA vez que anda. A incompetencia encarnada.

### Frame 5: Walk - Recuperacao do Tropeco
- **Position:** 320,0 a 383,63
- **Descricao:** Eduardo se recupera do tropeco. Corpo volta pra vertical, mas exagerado pro outro lado (1px pra tras). Olhos aliviados mas ainda assustados. Mala volta a posicao normal. Banana aponta pra cima de novo. Respiro de alivio (pequena nuvem 2x2px). Retorna ao Frame 0 no proximo ciclo.
- **Style Notes:** O alivio dele e temporario. No proximo ciclo, vai tropecar de novo. Sisyphus com mala de viagem.

---

## ATTACK ANIMATION - Banana Boomerang (3 frames)
**Sprite Sheet:** `eduardo_attack.png` -- 192x64px (3 frames x 64px)
**Loop:** Nao (one-shot, volta pro idle)
**Frame Rate:** 10 fps (100ms por frame)

### Frame 0: Attack - Wind-up
- **Position:** 0,0 a 63,63
- **Descricao:** Eduardo puxa o braco esquerdo pra tras, banana atras da cabeca. Corpo rotacionado ~20 graus (ombro esquerdo pra tras). Rosto com expressao de determinacao FALHA -- sobrancelhas tentam fazer cara brava mas os olhos de cachorro continuam tristes. Boca cerrada (tentando parecer durão). Mala na mao direita fica firme no chao (ancora). Linhas de tensao (2 linhas curvas, 1px) ao redor do braco esquerdo.
- **Style Notes:** Ele TENTA parecer ameacador mas falha miseravelmente. A "cara de mau" com olhos de cachorro e a piada.

### Frame 1: Attack - Arremesso
- **Position:** 64,0 a 127,63
- **Descricao:** Braco esquerdo em arco completo, mao aberta -- banana ja saiu (agora e projetil separado). Corpo esticado na direcao do arremesso (stretch 3px). Cabeca acompanha o movimento com atraso (2px atras do corpo). Olhos seguem a banana com esperanca desesperada. Boca gritando "PAI!" (boca aberta oval). 3 linhas de velocidade (1px, branco 60% opacity) no arco do braco. A mala derrapa 2px no chao pelo impulso.
- **Style Notes:** O grito de "PAI!" durante o ataque e fundamental. Ele ataca invocando a figura paterna. Patetico e efetivo.

### Frame 2: Attack - Follow-through
- **Position:** 128,0 a 191,63
- **Descricao:** Braco esquerdo completou o arco, pendurado pra frente. Eduardo desequilibrado pelo arremesso -- corpo inclinado 5px pra frente, quase caindo. Olhos acompanham a trajetoria da banana (olhando pra cima-frente). Mao esquerda aberta, dedos esticados. Expressao ansiosa -- "sera que acertou?". Mala arrastou mais 1px. Pos-arremesso, vulneravel.
- **Style Notes:** A vulnerabilidade pos-ataque e proposital. Sem a banana, ele fica desarmado e patetico por 1-2 segundos ate ela voltar.

### Projetil: Banana Boomerang (sprite separado)
**Sprite Sheet:** `eduardo_banana_projectile.png` -- 128x32px (4 frames x 32px)
**Dimensoes:** 32x32px por frame
**Loop:** Sim, rotacao continua enquanto no ar

#### Projetil Frame 0: Banana Horizontal
- **Position:** 0,0 a 31,31
- **Descricao:** Banana vista de cima, horizontal. Formato classico curvo, amarelo saturado com manchas marrons. Pontas escuras. Grosseiramente desenhada, contornos grossos (2px). Leve brilho no topo.

#### Projetil Frame 1: Banana Diagonal (45 graus)
- **Position:** 32,0 a 63,31
- **Descricao:** Banana rotacionada 45 graus horario. Linhas de rotacao (1px, branco 40%) indicando spin. Manchas de banana se borraram levemente pelo movimento.

#### Projetil Frame 2: Banana Vertical
- **Position:** 64,0 a 95,31
- **Descricao:** Banana vertical, rotacao 90 graus. As pontas agora apontam cima/baixo. Efeito de motion blur leve nas bordas. Brilho deslocado.

#### Projetil Frame 3: Banana Diagonal (135 graus)
- **Position:** 96,0 a 127,31
- **Descricao:** Banana a 135 graus, completando o ciclo de rotacao. Voltara ao Frame 0 para rotacao continua. Trail de 2px amarelo atras (afterimage da banana girando).

---

## DEATH ANIMATION (4 frames)
**Sprite Sheet:** `eduardo_death.png` -- 256x64px (4 frames x 64px)
**Loop:** Nao (one-shot, fica no ultimo frame)
**Frame Rate:** 8 fps (125ms por frame)

### Frame 0: Death - Impacto Inicial
- **Position:** 0,0 a 63,63
- **Descricao:** Eduardo recebe o golpe final. Corpo vai pra tras (knockback 4px). Olhos MAXIMAMENTE arregalados -- pupilas viram pontinhos (2px). Boca escancarada em grito silencioso. Cabelo loiro espeta pra todos os lados. Banana voa da mao esquerda (saindo do frame, canto superior esquerdo, 45 graus). A mala FINALMENTE solta -- mas a mao ainda tenta agarrar (dedos esticados na direcao da mala que cai). Estrelas de impacto (3 estrelinhas 3x3px, amarelas) ao redor da cabeca.
- **Style Notes:** O momento mais dramatico: ele SOLTA a mala. A unica coisa que ele segurava. A banana tambem vai. Perdeu tudo.

### Frame 1: Death - Queda
- **Position:** 64,0 a 127,63
- **Descricao:** Eduardo caindo de costas. Corpo a 45 graus do chao. Cabeca (pesada) puxa ele pra tras. Bracos abertos em cruz. Pernas pra cima. Olhos girando (espiral classica de cartoon, 2 espirais 4x4px nos olhos). Boca aberta, lingua de fora (1 pixel rosa). A mala caiu de lado, aberta, roupas saindo (2-3 pixels coloridos representando roupas). Banana no chao, amassada.
- **Style Notes:** A mala aberta mostrando roupas e referencia a fuga. Ele literalmente "desfaz as malas" ao morrer.

### Frame 2: Death - No Chao
- **Position:** 128,0 a 191,63
- **Descricao:** Eduardo estatelado no chao, visto de cima. Corpo esparramado em X. Cabeca lunar gigante no centro-topo, achatada (squash 3px -- parece mais oval que redonda agora). Olhos com X classico de morte (X em cada olho, 3x3px). Lingua de fora (2px rosa). Camiseta amarela amassada. A mala aberta ao lado com roupas espalhadas. Banana amassada do outro lado. Uma unica lagrima escorre do olho (2px descendo pela bochecha).
- **Style Notes:** Mesmo morto, ele chora. A lagrima final e o toque comico-tragico. A mala aberta = a fuga falhou.

### Frame 3: Death - Fantasma Comico
- **Position:** 192,0 a 255,63
- **Descricao:** O "fantasma" de Eduardo sobe do corpo. Versao translucida (50% opacity) e menor (~40x40px) do Eduardo flutuando 10px acima do corpo. Fantasma com asas de anjo minusculas e ridiculas (4x3px cada). Olhos de cachorro AINDA lacrimejantes mesmo como fantasma. Segurando uma bandeirainha dos EUA (referencia a fuga pro exterior). Aureola torta (oval amarela 12x4px acima da cabeca, inclinada). O corpo embaixo permanece como no Frame 2.
- **Style Notes:** Ate como fantasma ele quer fugir pros EUA. A bandeirainha americana e o toque final. Aureola TORTA porque ele nao e santo.

---

## HIT ANIMATION (2 frames)
**Sprite Sheet:** `eduardo_hit.png` -- 128x64px (2 frames x 64px)
**Loop:** Nao (one-shot, volta pro idle)
**Frame Rate:** 12 fps (83ms por frame -- rapido, reacao instantanea)

### Frame 0: Hit - Dano Recebido
- **Position:** 0,0 a 63,63
- **Descricao:** Eduardo toma dano. Flash branco sobre todo o sprite (overlay branco 60% opacity). Corpo deforma pra tras (squash horizontal, stretch vertical -- 4px mais alto, 3px mais estreito). Olhos ESTICAM pra fora do rosto (estilo cartoon, saem 2px da cabeca). Boca em formato de onda (wwww). Banana aponta pra cima pelo impacto. Mala balanca mas NAO solta (agarra com forca). 2 gotas de suor voam (2x2px cada). Texto "AI!" em amarelo (miniatura, 8x6px) acima da cabeca.
- **Style Notes:** A reacao e exagerada e covarde. Ele sente MAIS dor que o dano justifica. Drama queen.

### Frame 1: Hit - Recuperacao Chorosa
- **Position:** 64,0 a 127,63
- **Descricao:** Eduardo voltando ao normal mas CHORANDO. Corpo volta as proporcoes normais (com bounce -- 1px overshoot). Olhos enormes agora com 2 lagrimas cada (4 lagrimas totais, 2x2px, escorrendo). Labio inferior tremendo (2px de variacao). Sobrancelhas no angulo maximo de "coitadinho". Banana volta a posicao normal. Mala firme. Tenta se recompor mas claramente quer chorar mais.
- **Style Notes:** A recuperacao e mais patetica que o dano. Ele se recupera FISICAMENTE rapido, mas EMOCIONALMENTE nunca.

---

## SPECIAL ANIMATION - Fuga Estrategica (6 frames)
**Sprite Sheet:** `eduardo_special_fuga.png` -- 384x64px (6 frames x 64px)
**Loop:** Nao (one-shot)
**Frame Rate:** 10 fps (100ms por frame)
**Trigger:** HP abaixo de 30%

### Frame 0: Special - Panico
- **Position:** 0,0 a 63,63
- **Descricao:** Eduardo percebe que o HP ta baixo. Olhos viram ENORME (ocupam 50% do rosto -- 16px cada). Pupilas contraem pra 1px. Boca abre em retangulo de panico (grito de Homer Simpson). Corpo treme (1px jitter em todas direcoes). Suor escorre de TODAS as direcoes (6 gotas, 2x2px cada, ao redor da cabeca). Banana cai da mao esquerda (comeca a cair, 3px abaixo da mao). Mala AGARRA COM DUAS MAOS agora (ambos bracos na alca).
- **Style Notes:** O panico e REAL. Ele larga a banana (a arma) pra segurar a mala (a fuga) com duas maos. Prioridades.

### Frame 1: Special - Pre-Teleporte (Carga)
- **Position:** 64,0 a 127,63
- **Descricao:** Eduardo comeca a brilhar. Aura amarela (6px ao redor, 40% opacity, cor #FFD700) envolve o corpo. Corpo comeca a ficar translucido (80% opacity). Olhos brilham branco puro. A mala tambem brilha (vai junto, obvio). Particulas de luz (4-5 quadrados 2x2px, amarelos, saindo radialmente). Pes saem do chao (+2px). Banana no chao abaixo dele, abandonada.
- **Style Notes:** A mala brilha junto porque ela FAZ PARTE dele neste ponto. A banana abandonada e simbolica.

### Frame 2: Special - Flash de Teleporte
- **Position:** 128,0 a 191,63
- **Descricao:** FLASH BRANCO. O sprite inteiro e 90% branco com apenas o outline vagamente visivel. Explosao de particulas radiais (8 linhas de 1px, brancas, saindo do centro). A silhueta de Eduardo + mala ainda reconhecivel dentro do flash. Pequena nuvem de fumaca comeca a se formar embaixo (base do sprite, cinza claro #D5D8DC).
- **Style Notes:** O flash deve ser CEGANTE. Quase todo branco. A silhueta com a mala dentro do flash e a piada visual.

### Frame 3: Special - Nuvem de Fumaca (Eduardo sumindo)
- **Position:** 192,0 a 255,63
- **Descricao:** Eduardo SUMIU. No lugar dele, uma nuvem de fumaca densa (preenche ~70% do frame). Fumaca cinza-esbranquicada (#D5D8DC base, #B0B0B0 sombras) com formas irregulares, estilo comic. Dentro da fumaca, VAGAMENTE visivel: apenas os olhos de cachorro (2 circulos azuis com brilho) olhando pra fora da fumaca. Banana abandonada no chao abaixo da nuvem. Particulas menores de fumaca se dissipam nas bordas.
- **Style Notes:** Os olhos visíveis dentro da fumaca sao ESSENCIAIS. Mesmo fugindo, os olhos pateticos traem sua presenca.

### Frame 4: Special - Fumaca Dissipando
- **Position:** 256,0 a 319,63
- **Descricao:** Nuvem de fumaca se desfaz (~40% do frame agora). Olhos ja nao aparecem (ele foi embora). Particulas de fumaca espalhadas. Banana no chao. No lugar onde ele estava, marcas de rodinhas da mala (2 linhas paralelas de 1px, marrom, no chao) indicam a direcao da fuga. Um bilhete (papel branco 4x3px) cai no ar (estava na mala?).
- **Style Notes:** As marcas de rodinha da mala no chao contam a historia: ele ARRASTOU a mala ate no teleporte.

### Frame 5: Special - Residuo
- **Position:** 320,0 a 383,63
- **Descricao:** Fumaca quase toda dissipada (restos 10%). Banana no chao (permanece como item coletavel). Marcas de rodinhas no chao. O bilhete no chao, legivel com lupa, diria "VOLTEI PRA DISNEY" (mas nos 64px aparece como papel com rabisco). Uma pena de galinha solitaria (referencia a "Fuga das Galinhas") cai lentamente (3x2px, branca). Sprite praticamente limpo, pronto pro respawn.
- **Style Notes:** A pena de galinha caindo e a referencia final. "A Fuga das Galinhas" = Eduardo fugindo pro exterior.

---

## BUFF/DEBUFF OVERLAY SPRITES

### Puxa-Saquismo (Buff) -- quando perto do pai
**Sprite:** `eduardo_buff_puxasaco.png` -- 256x64px (4 frames)
- Aura amarela dourada pulsando ao redor do Eduardo
- Frame 0: Aura 4px, 30% opacity
- Frame 1: Aura 6px, 40% opacity
- Frame 2: Aura 8px, 50% opacity (pico)
- Frame 3: Aura 6px, 40% opacity
- Loop continuo enquanto buff ativo
- Estrelinhas (#FFD700, 2x2px) orbiting ao redor, 3 estrelas em posicoes alternadas
- Expressao do Eduardo muda: olhos com coracoes (2px, rosa), sorriso ENORME

### Orfao Politico (Debuff) -- sem o pai por perto
**Sprite:** `eduardo_debuff_orfao.png` -- 256x64px (4 frames)
- Aura cinza triste (#808080, 40% opacity) ao redor
- Frame 0: Aura 3px, nuvem de chuva acima da cabeca (8x4px, cinza escuro)
- Frame 1: Aura 3px, gotas de chuva caindo (3 gotas, 1x2px, azul)
- Frame 2: Aura 4px, mais gotas, Eduardo encolhe 1px (depressao)
- Frame 3: Aura 3px, gotas diminuem
- Loop continuo enquanto debuff ativo
- Eduardo fica dessaturado (cores mais cinzentas, -30% saturation)
- Olhos mais lacrimejantes que o normal (lagrimas maiores, 3x2px)

---

## Sprite Sheet Summary

| Arquivo                          | Frames | Dimensao Sheet  | Loop    | FPS |
|----------------------------------|--------|-----------------|---------|-----|
| `eduardo_idle.png`               | 4      | 256x64px        | Sim     | 8   |
| `eduardo_walk.png`               | 6      | 384x64px        | Sim     | 10  |
| `eduardo_attack.png`             | 3      | 192x64px        | Nao     | 10  |
| `eduardo_banana_projectile.png`  | 4      | 128x32px        | Sim     | 12  |
| `eduardo_death.png`              | 4      | 256x64px        | Nao     | 8   |
| `eduardo_hit.png`                | 2      | 128x64px        | Nao     | 12  |
| `eduardo_special_fuga.png`       | 6      | 384x64px        | Nao     | 10  |
| `eduardo_buff_puxasaco.png`      | 4      | 256x64px        | Sim     | 8   |
| `eduardo_debuff_orfao.png`       | 4      | 256x64px        | Sim     | 8   |

## Phaser 3 Atlas Keys
```javascript
// Personagem principal
{ key: 'eduardo_idle', frameWidth: 64, frameHeight: 64 }
{ key: 'eduardo_walk', frameWidth: 64, frameHeight: 64 }
{ key: 'eduardo_attack', frameWidth: 64, frameHeight: 64 }
{ key: 'eduardo_death', frameWidth: 64, frameHeight: 64 }
{ key: 'eduardo_hit', frameWidth: 64, frameHeight: 64 }
{ key: 'eduardo_special_fuga', frameWidth: 64, frameHeight: 64 }
{ key: 'eduardo_buff_puxasaco', frameWidth: 64, frameHeight: 64 }
{ key: 'eduardo_debuff_orfao', frameWidth: 64, frameHeight: 64 }

// Projetil
{ key: 'eduardo_banana', frameWidth: 32, frameHeight: 32 }
```

## Notas para o Artista
- O rosto LUNAR e a feature principal. Se nao parecer uma lua cheia com olhos de cachorro, REFACA
- A mala NUNCA larga (exceto na morte). Ela e uma extensao do corpo dele
- Os olhos lacrimejantes sao PERMANENTES. Ele esta SEMPRE a ponto de chorar
- O queixo inexistente e critico -- o rosto vai do labio pro pescoco. Sem mandibula = sem firmeza
- A banana e secundaria a mala em importancia. Ele larga a banana, NUNCA a mala (exceto morte)
- Cada frame deve ter uma qualidade "patética" -- ele e o personagem mais patético do jogo
- Linhas GROSSAS e IRREGULARES. Robert Crumb. Underground comix. NADA limpo ou polido
- A camiseta da selecao deve parecer uma camiseta de camelô, nao a oficial
- Proporcoes ERRADAS de proposito: cabeca grande demais, corpo fraco, pernas finas
- A expressao DEFAULT e "cachorro que acabou de ser abandonado na beira da estrada"
