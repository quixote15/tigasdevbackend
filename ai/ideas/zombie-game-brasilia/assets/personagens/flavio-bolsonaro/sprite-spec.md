# Flavio Bolsonaro (O Herdeiro) - Sprite Specification

## Overview
- **Character Type:** Mini-boss / Rival do Eduardo / Candidato 2026
- **Sprite Dimensions:** 64x64px
- **Sprite Sheet Layout:** Horizontal strip, 1 row per animation
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (32, 60) -- pes no chao
- **Perspective:** Top-down levemente isometrica (Y-sorting)

## Color Palette

| Element                | Hex Code  | Usage                                    |
|------------------------|-----------|------------------------------------------|
| Terno Azul Marinho     | `#1B2A4A` | Corpo do terno, principal                |
| Terno Azul (highlight) | `#2C3E6B` | Dobras iluminadas do terno               |
| Terno Azul (shadow)    | `#0D1A2E` | Sombras pesadas do terno                 |
| Camisa Branca          | `#F0EDE5` | Camisa por baixo do terno                |
| Camisa (shadow)        | `#C8C4BA` | Dobras/sombras da camisa                 |
| Gravata Vermelha       | `#8B1A1A` | Gravata discreta                         |
| Gravata (highlight)    | `#A82828` | Brilho na gravata                        |
| Pele                   | `#D4A574` | Tom de pele base                         |
| Pele (shadow)          | `#B08050` | Sombras do rosto/maos                    |
| Pele (highlight)       | `#E8C49A` | Pontos de luz na pele                    |
| Cabelo Castanho        | `#3D2B1F` | Cabelo penteado                          |
| Cabelo (highlight)     | `#5A4030` | Brilho do gel no cabelo                  |
| Dourado Abotoaduras    | `#D4A940` | Abotoaduras e detalhes de ostentacao     |
| Dourado (brilho)       | `#F0D060` | Flash das abotoaduras                    |
| Outline Black          | `#1A1A1A` | Linhas grossas 2px (Crumb style)         |
| Shadow Dark            | `#0D0D0D` | Drop shadow, 50% opacity                |
| Dentes Brancos         | `#F5F5E0` | Sorriso ensaiado (dentes expostos)       |
| Dentes (shadow)        | `#D0D0B8` | Sombra nos dentes                        |
| Tatuagem Vermelha      | `#CC2222` | "BOLSONARO" no peito (death/zombie)      |
| Tatuagem (shadow)      | `#8B1515` | Sombra da tatuagem                       |
| Aura Azul              | `#4488CC` | Aura "moderacao" (30% opacity)           |
| Aura Vermelha          | `#CC3333` | Aura "falha" quando provocado            |
| Fantasma Cinza         | `#8888AA` | Sombra do pai (Heranca Maldita)          |

---

## Sprite Sheets

### 1. IDLE - `flavio_idle.png` (256x64px, 4 frames)

**Ciclo:** Loop continuo | **FPS:** 8 | **Duracao ciclo:** 500ms

#### Frame 0: Pose Moderada A
- **Position:** 0,0 to 63,63
- **Description:** Flavio de frente (top-down isometrica), em pe com postura rigidamente ereta -- como se tivesse engolido uma regua. Terno azul marinho impecavel, camisa branca, gravata vermelha discreta. Cabelo penteado com gel (brilho exagerado, 2-3px de highlight no topo). Maos cruzadas na frente do corpo (pose "estadista"). SORRISO ENSAIADO dominante -- boca aberta mostrando fileira de dentes brancos perfeitos DEMAIS, antinatural. Olhos abertos normalmente. Queixo levemente projetado para frente (forcando pose de autoridade). Abotoaduras douradas visiveis nos punhos. Sombra no chao.
- **Deformidade:** O sorriso ocupa ~40% da largura do rosto. Dentes sao levemente grandes demais. Expressao de quem ensaiou 47 vezes no espelho.
- **Style Notes:** Linhas grossas 2px. O terno deve parecer caro mas desconfortavel. Ombros levemente levantados (tensao). Contraste com Eduardo -- este e a versao "seria".

#### Frame 1: Pose Moderada B (Piscar Nervoso)
- **Position:** 64,0 to 127,63
- **Description:** Identico ao Frame 0, EXCETO: ambos os olhos fechados em piscar exagerado. O piscar e FORTE demais -- as palpebras se fecham completamente com forza, criando rugas ao redor dos olhos (2-3 linhas de tensao). O sorriso se mantem RIGIDAMENTE no lugar apesar do piscar. Leve movimento dos ombros (1px para cima) como micro-tensao.
- **Deformidade:** O piscar e tao forte que parece um tique nervoso. O contraste entre olhos apertados e sorriso congelado e perturbador.

#### Frame 2: Pose Moderada C
- **Position:** 128,0 to 191,63
- **Description:** Volta ao Frame 0 mas com micro-variacao: cabeca inclinada 2px para a direita (pose ensaiada de "estou ouvindo"), sorriso IDENTICO (congelado na mesma posicao exata). Uma das maos levemente levantada (2px) como se fosse fazer gesto de "calma". Abotoaduras brilham (highlight pixel).
- **Deformidade:** A rigidez do sorriso enquanto o corpo se move sutilmente e uncanny valley. O rosto e uma mascara.

#### Frame 3: Pose Moderada D (Piscar Duplo)
- **Position:** 192,0 to 255,63
- **Description:** PISCAR DUPLO RAPIDO -- olhos se fecham duas vezes em sequencia (neste frame estao no meio do segundo piscar, semi-abertos). Sorriso CONGELADO no lugar. Sobrancelhas levemente levantadas (tentando parecer natural e falhando). Leve suor na testa (1-2px de brilho extra).
- **Deformidade:** O nervosismo transparece apesar da pose ensaiada. Goticulas de suor no terno? Nao -- ele e "moderado", suor so na testa.

---

### 2. WALK - `flavio_walk.png` (384x64px, 6 frames)

**Ciclo:** Loop continuo | **FPS:** 10 | **Duracao ciclo:** 600ms

#### Frame 0: Passo Direito - Contato
- **Position:** 0,0 to 63,63
- **Description:** Pe direito a frente, peso sobre ele. Terno move minimamente (rigido). Braco esquerdo levemente a frente, braco direito levemente atras (caminhada ensaiada de politico). Sorriso MANTIDO. Cabelo NAO se move (gel forte). Queixo projetado. Abotoaduras visiveis.
- **Style Notes:** A caminhada e RIGIDA demais -- parece um boneco de cera tentando parecer natural. O terno restringe movimento. Contraste total com a caminhada solta do Eduardo.

#### Frame 1: Passo Direito - Meio
- **Position:** 64,0 to 127,63
- **Description:** Transicao, corpo levemente mais alto (1px -- bounce minimo). Pe esquerdo saindo do chao. O terno QUASE nao deforma -- material rigido. Maos em posicao neutra. Sorriso IDENTICO ao frame anterior (nao muda NUNCA durante walk). Piscar nervoso sutil (olhos 80% abertos).

#### Frame 2: Passo Esquerdo - Contato
- **Position:** 128,0 to 191,63
- **Description:** Mirror do Frame 0 -- pe esquerdo a frente. Braco direito a frente, esquerdo atras. MESMA expressao facial exata (sorriso ensaiado). A gravata balanca 1px. Abotoaduras do outro punho agora visiveis.

#### Frame 3: Passo Esquerdo - Meio
- **Position:** 192,0 to 255,63
- **Description:** Mirror do Frame 1. Corpo levemente mais alto. PISCAR completo neste frame (olhos fechados) -- nervosismo enquanto caminha. Sorriso CONGELADO. Suor sutil na testa.

#### Frame 4: Passo Direito - Impulso
- **Position:** 256,0 to 319,63
- **Description:** Pe direito empurrando o chao. Postura levemente inclinada para frente (2px). Queixo ainda mais projetado (tentando parecer determinado). O terno estica levemente nas costas. Maos fazem gesto sutil de "vamos em frente" (1 mao levemente aberta).

#### Frame 5: Passo Esquerdo - Impulso
- **Position:** 320,0 to 383,63
- **Description:** Mirror do Frame 4. Pe esquerdo empurrando. Neste frame, um MICRO-TIQUE: o canto do sorriso treme 1px (a mascara quase cai). Recupera no proximo ciclo. Abotoaduras douradas flasham (highlight).

---

### 3. ATTACK - `flavio_attack.png` (192x64px, 3 frames)

**Ciclo:** One-shot | **FPS:** 10 | **Duracao:** 300ms

#### Frame 0: Preparacao - "Discurso Decorado"
- **Position:** 0,0 to 63,63
- **Description:** Flavio levanta o dedo indicador direito (gesto classico de politico fazendo discurso). Boca abre MAIS (sorriso vira boca de discurso). Olhos se abrem mais (intensidade ensaiada). O braco sobe rigidamente como se fosse mecanico. Balao de fala comeca a se formar (pequena nuvem branca com outline preto acima da cabeca, ~8x6px). Corpo levemente inclinado para frente. Abotoaduras brilham no gesto.
- **Style Notes:** O gesto e IDENTICO ao que todo politico faz -- dedo em riste. Mas exagerado, mecanico, ensaiado.

#### Frame 1: Ataque - "Discurso em Acao"
- **Position:** 64,0 to 127,63
- **Description:** BALAO DE FALA EXPLODE para fora -- letras garbled/simbolos voam do balao (#$%&!) em arco. O dedo aponta diretamente para frente. Boca ESCANCARADA (exagero grotesco -- boca ocupa 50% do rosto). Ondas sonicas visiveis saindo da boca (3 arcos concentricos, 1px cada, azul claro 40% opacity). O cabelo FINALMENTE se move (1-2 fios saem do lugar pelo volume da voz). Gravata flutua com a forca do discurso.
- **VFX:** Ondas sonicas sao o hitbox -- dano em cone frontal.

#### Frame 2: Recuperacao - "Volta ao Sorriso"
- **Position:** 128,0 to 191,63
- **Description:** Flavio rapidamente recompoe o sorriso ensaiado. O braco desce mecanicamente. Boca fecha e TRAVA no sorriso novamente (transicao brusca, sem suavidade). Os simbolos do balao se dissipam. 1-2 fios de cabelo ainda fora do lugar (ajeitando com a mao esquerda). A gravata ainda balancando. Micro-suor na testa.
- **Style Notes:** A velocidade com que ele recompoe a mascara e perturbadora. Em 1 frame vai de grito a sorriso perfeito.

---

### 4. DEATH - `flavio_death.png` (256x64px, 4 frames)

**Ciclo:** One-shot | **FPS:** 8 | **Duracao:** 500ms

#### Frame 0: Impacto Inicial
- **Position:** 0,0 to 63,63
- **Description:** Flavio recebe golpe fatal. Corpo joga para tras. O SORRISO FINALMENTE QUEBRA -- expressao de choque genuino, boca aberta em "O", olhos arregalados. O terno comeca a rasgar na frente (1-2 rasgos diagonais na camisa). Gravata voa para o lado. Uma abotoaduras solta voando. Cabelo SAI DO GEL (3-4 fios espetados).
- **Style Notes:** A quebra do sorriso e o momento CATARTICO. Pela primeira vez ele mostra emocao real.

#### Frame 1: Queda - Terno Rasga
- **Position:** 64,0 to 127,63
- **Description:** Caindo para tras, angulo ~45 graus. O terno RASGA NO PEITO -- camisa abre revelando o inicio da tatuagem "BOLSO-" em vermelho (#CC2222) no peito. Expressao de PANICO (sorriso impossivel agora). Abotoaduras voando em arco. Sapatos saindo dos pes. Gravata enrolada no pescoco. Cabelo completamente despenteado.
- **Deformidade Revelada:** A tatuagem que ele escondia comeca a aparecer. O "moderado" e desmascarado.

#### Frame 2: No Chao - Tatuagem Exposta
- **Position:** 128,0 to 191,63
- **Description:** Flavio no chao, de costas, terno completamente aberto. TATUAGEM COMPLETA "BOLSONARO" visivel em arco no peito (letras vermelhas grossas, estilo presidiario). Expressao: olhos em espiral (tontura comica), boca tremendo entre sorriso e choro (metade sorriso, metade careta). A gravata forma um "X" no pescoco. Sapatos ao lado do corpo.
- **Deformidade Peak:** O contraste entre o terno caro destruido e a tatuagem brega e a piada visual maxima.

#### Frame 3: Derrota Final
- **Position:** 192,0 to 255,63
- **Description:** Flavio flat no chao, estrelinhas girando acima da cabeca (3 estrelas douradas, referencia abotoaduras). ULTIMO SUSPIRO: tenta recompor o sorriso ensaiado mesmo derrotado -- consegue um sorriso torto, patetico, com 1 dente faltando. A tatuagem "BOLSONARO" pulsa levemente (1px glow vermelho). Fantasma translucido do pai (silhueta com terno) comeca a aparecer atras dele (10% opacity).
- **Style Notes:** Mesmo na derrota, tenta manter a pose. Patetico e comico ao mesmo tempo.

---

### 5. HIT - `flavio_hit.png` (128x64px, 2 frames)

**Ciclo:** One-shot | **FPS:** 12 | **Duracao:** 167ms

#### Frame 0: Sorriso Trava (FREEZE)
- **Position:** 0,0 to 63,63
- **Description:** Flavio recebe hit. O corpo faz knockback (2px para tras), MAS O SORRISO CONGELA COMPLETAMENTE. O rosto fica TRAVADO -- olhos arregalam em panico, sobrancelhas sobem, MAS A BOCA NAO MUDA. Sorriso ensaiado IDENTICO ao idle, porem os olhos contradizem totalmente. O terno amassa no ponto de impacto. Flash branco no corpo (hit flash, 50% opacity overlay). 2 gotas de suor voam da testa.
- **Deformidade Core:** Este e O momento signature do personagem -- o sorriso que nao consegue desligar mesmo quando deveria.

#### Frame 1: Recuperacao Mecanica
- **Position:** 64,0 to 127,63
- **Description:** Flavio se recompoe MECANICAMENTE. Ajusta o terno (mao puxando a lapela), cabelo volta ao lugar (como se tivesse mola). Os olhos FINALMENTE se alinham com o sorriso novamente (forza o olhar calmo). Uma veia pulsa na testa (2px, vermelha). O corpo volta 2px para frente. Pequenas particulas de poeira saindo do terno (onde foi atingido).
- **Style Notes:** A velocidade de recuperacao e ROBOTICA. Parece um animatronic resetando.

---

### 6. SPECIAL: "Sera?" Dance - `flavio_special_sera.png` (512x64px, 8 frames)

**Ciclo:** One-shot | **FPS:** 8 | **Duracao:** 1000ms

#### Frame 0: Preparacao - Saca o Celular
- **Position:** 0,0 to 63,63
- **Description:** Flavio tira celular do bolso do terno (celular dourado, claro). Olha para a camera com sorriso ensaiado intensificado (MAIS dentes visiveis). Uma mao segura o celular na altura do rosto, outra faz "V" de vitoria. Fundo comeca a piscar (indicador de que TikTok esta gravando). Pequeno icone de TikTok (nota musical rosa/azul, 4x4px) flutua ao lado.

#### Frame 1: Inicio da Danca - Ombros
- **Position:** 64,0 to 127,63
- **Description:** Comeca a mover os ombros para os lados (danca RIGIDA de politico que nao sabe dancar). Ombro direito sobe, esquerdo desce. O terno restringe o movimento (parece que vai rasgar). Sorriso MAXIMO. Celular agora em selfie mode. Particulas de brilho (TikTok sparkle) ao redor, 3-4 pontos rosa/azul.

#### Frame 2: "Se-" (Primeira Silaba)
- **Position:** 128,0 to 191,63
- **Description:** Boca forma a silaba "Se-" (labios arredondados). Corpo faz um shimmy para a direita. Balao de fala com "Se-" em fonte estilizada rosa/azul (TikTok style). O terno finalmente se solta um pouco (ele esta se esforçando). Notas musicais (colcheias, 3x3px) saem ao redor. Zema (miniatura 16x16px, canto inferior direito) aparece dançando junto.
- **VFX:** Ondas hipnoticas rosa/azul começam a emanar (circulares, 30% opacity).

#### Frame 3: "-ra?" (Segunda Silaba)
- **Position:** 192,0 to 255,63
- **Description:** Boca forma "-ra?" com sobrancelhas levantadas (expressao de pergunta exagerada). Corpo faz shimmy para a esquerda. Balao agora mostra "Sera?" completo em rosa neon. As ondas hipnoticas se EXPANDEM (agora cobrem ~50% do frame). Zema miniatura mirror da dança. Celular com hearts flutuando (like icons). Os olhos de Flavio brilham rosa por 1 frame.
- **VFX:** Ondas hipnoticas sao o hitbox -- inimigos no raio ficam stunned.

#### Frame 4: Danca Peak - Giro
- **Position:** 256,0 to 319,63
- **Description:** Flavio faz um GIRO (360 graus, neste frame esta de costas). Costas do terno visivel -- ETIQUETA DE GRIFE gigante pendurada (esqueceu de tirar, 4x2px branco). Celular balanca na mao estendida. Ondas hipnoticas no MAXIMO (cobrem frame inteiro). Confete TikTok cai do topo (particulas rosa, azul, branco). Zema miniatura fazendo o mesmo giro.

#### Frame 5: Danca Peak - Volta de Frente
- **Position:** 320,0 to 383,63
- **Description:** Completa o giro, agora de frente com pose TRIUNFAL -- bracos abertos, celular em uma mao, outra mao com dedos em "hang loose". Sorriso no MAXIMO ABSOLUTO (dentes brilham com highlight branco). Terno levemente amassado do giro. Ondas hipnoticas pulsam. Numero "+10K" flutua acima (likes do TikTok). Zema miniatura bate palma.

#### Frame 6: Finalizacao - Pose de Influencer
- **Position:** 384,0 to 447,63
- **Description:** Flavio faz pose de influencer -- celular para baixo, ambas as maos fazem coracao (gesto coreano de coracao). Sorriso trava na posicao de "acabou de gravar". Ondas hipnoticas comecam a diminuir. Confete desacelerando. O terno tem uma mancha de suor na axila (esforcou demais na dança). Zema miniatura desaparece (fade out).

#### Frame 7: Volta ao Normal - Guarda Celular
- **Position:** 448,0 to 511,63
- **Description:** Guarda celular no bolso do terno. Recompoe postura "moderada" (costas retas, queixo projetado). Ajusta gravata com a mao. O sorriso volta ao ensaiado padrao (menos intenso que o TikTok). Ultimas particulas de confete caem. Mancha de suor na axila permanece (detalhe). Piscar nervoso -- "sera que viralizou?"

---

## Sprite Sheet Summary

| Sheet                | Filename                     | Frames | Size       | FPS | Loop     |
|----------------------|------------------------------|--------|------------|-----|----------|
| Idle                 | `flavio_idle.png`            | 4      | 256x64px   | 8   | Loop     |
| Walk                 | `flavio_walk.png`            | 6      | 384x64px   | 10  | Loop     |
| Attack               | `flavio_attack.png`          | 3      | 192x64px   | 10  | One-shot |
| Death                | `flavio_death.png`           | 4      | 256x64px   | 8   | One-shot |
| Hit                  | `flavio_hit.png`             | 2      | 128x64px   | 12  | One-shot |
| Special (Sera?)      | `flavio_special_sera.png`    | 8      | 512x64px   | 8   | One-shot |

## Phaser 3 Atlas Keys
```
// Idle
key: 'flavio_idle'
frameWidth: 64
frameHeight: 64

// Walk
key: 'flavio_walk'
frameWidth: 64
frameHeight: 64

// Attack
key: 'flavio_attack'
frameWidth: 64
frameHeight: 64

// Death
key: 'flavio_death'
frameWidth: 64
frameHeight: 64

// Hit
key: 'flavio_hit'
frameWidth: 64
frameHeight: 64

// Special
key: 'flavio_special_sera'
frameWidth: 64
frameHeight: 64
```

## Notes for Artist
- O SORRISO ENSAIADO e a feature #1 -- deve ser perturbadoramente perfeito e rigido
- O piscar nervoso e o segundo elemento mais importante -- exagerar frequencia e intensidade
- O terno deve parecer CARO mas DESCONFORTAVEL -- ombros tensos, postura rigida
- Contraste visual com Eduardo: Flavio e mais velho, mais "serio", mais contido
- A tatuagem "BOLSONARO" no peito so aparece na death animation -- e a revelacao comica
- Abotoaduras douradas = ostentacao disfarçada de "moderacao"
- O cabelo com gel NUNCA se move (exceto em death e attack extremo)
- Cada frame deve ter linhas grossas Robert Crumb, assimetria proposital
- Queixo PROEMINENTE forcado em toda pose (tentando parecer forte)
- O celular na special e DOURADO (ostentacao disfarçada v2)
- Zema miniatura na special e um detalhe comico -- pode ser simplificado (silhueta com oculos)
