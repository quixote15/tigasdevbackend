# CABO DACIOLO (O Profeta) -- Sprite Specification
### O CORACAO de Zumbis de Brasilia | Abril 2026
### Estilo Andre Guedes -- Caricatura grotesca, underground comix, horror B-movie

---

> *"O unico personagem cujos poderes sobrenaturais sao REAIS. Num mundo de mentirosos e corruptos, o maluco que grita GLORIA A DEUS no plenario e o unico que entrega o que promete."*

---

## Specs Tecnicas Globais

| Propriedade | Valor |
|---|---|
| Tamanho sprite | 64x64px |
| Formato | PNG com transparencia |
| Sprite sheet | Horizontal (frames lado a lado) |
| Frame rate | 8-12 fps (estilo jerky/twitchy) |
| Perspectiva | Top-down levemente isometrica (Y-sorting) |
| Paleta base | Branco puro, dourado, azul celeste, amarelo, carne desenhada |
| Contorno | Linhas grossas pretas (2-3px no sprite), irregular |
| Sombras | Pesadas, projetadas, exageradas |

---

## Anatomia Base do Personagem

### Proporcoes Grotescas (a la Andre Guedes)
- **Cabeca**: 40% da altura total do sprite (desproporcional, e a piada)
- **Olhos**: 3x maiores que o normal -- ARREGALADOS de iluminacao divina, pupilas minusculas, branco dos olhos domina, veias vermelhas visiveis
- **Boca**: Desproporcional, SEMPRE aberta ou semi-aberta como se prestes a gritar "GLORIA A DEUS", maxilar proeminente, dentes visiveis
- **Maos**: ENORMES (2x o tamanho normal), para segurar a Biblia Gigante, fumaca santa saindo permanentemente
- **Corpo**: Alto e magro/esguio, pernas finas, pescoco longo
- **Postura**: Ereta, quase rigida -- a fe nao deixa ele curvar

### Vestuario Fixo
- **Camisa social branca**: SEMPRE impecavelmente limpa (milagre no apocalipse zumbi), mangas ate o cotovelo arregacadas, dois botoes abertos no peito
- **Calca social**: Preta/cinza escuro, vincos marcados
- **Sapatos**: Sociais pretos, surrados mas inteiros
- **SEM gravata**: Homem do povo
- **Rosario no pescoco**: Contas marrons, crucifixo dourado, balanca durante movimento
- **Aureola**: Torta (15 graus inclinada), dourada, brilha/pulsa, SEMPRE visivel

### Acessorios Permanentes
- **Biblia Gigante**: Proporcao exagerada (quase do tamanho do torso), capa de couro marrom-dourado, paginas amareladas, cantos gastos, PESADA (influencia animacao de walk e attack)
- **Fumaca Santa**: Particulas douradas/brancas saindo das maos permanentemente, mais intensas durante skills
- **Aureola**: Overlay torto sobre a cabeca, glow pulsante dourado

---

## SPRITES -- Especificacao Frame a Frame

---

### 1. IDLE (4 frames) -- "O Profeta Aguarda"
**Sheet**: `daciolo-idle.png` (256x64px -- 4 frames de 64x64)
**Loop**: Sim, ciclico
**FPS**: 8
**Direcoes**: 4 (down, up, left, right) = 4 sheets

| Frame | Descricao Detalhada |
|---|---|
| **1** | Postura ereta, pes juntos, Biblia segurada com as duas maos contra o peito. Olhos arregalados olhando para frente. Boca semi-aberta. Aureola brilho MAXIMO (dourado intenso). Fumaca nas maos: volume MINIMO, 2-3 wisps. Rosario pendente, imivel. |
| **2** | Micro-movimento: cabeca gira 5 graus para a esquerda como se "sentindo algo". Olhos ficam AINDA MAIS arregalados. Biblia sobe 2px (apertando contra o peito). Aureola brilho MEDIO. Fumaca nas maos: volume MEDIO, wisps sobem. |
| **3** | Cabeca volta ao centro. Boca abre MAIS (preparando grito silencioso). Olhos voltam ao normal-arregalado. Biblia desce 2px. Aureola brilho MINIMO (quase transparente). Fumaca nas maos: volume MAXIMO momentaneo, burst de 4-5 wisps. |
| **4** | Micro-tremble no corpo inteiro (1px shake). Expressao volta ao frame 1 mas com LEVISSIMO sorriso -- o sorriso de quem sabe que Deus esta presente. Aureola brilho MEDIO. Fumaca volta ao minimo. |

**Notas de animacao**:
- O idle deve transmitir "extase religioso contido" -- ele esta sempre em estado de quase-revelacao
- A fumaca nas maos NUNCA para completamente
- A aureola NUNCA apaga, apenas varia intensidade
- Cada 4o ciclo do idle: chance de 10% de trigger do "micro-grito" (boca abre full, flash branco 1 frame, volta ao normal)

---

### 2. WALK (6 frames) -- "Caminhada do Determinado"
**Sheet**: `daciolo-walk.png` (384x64px -- 6 frames de 64x64)
**Loop**: Sim, ciclico
**FPS**: 10
**Direcoes**: 4 = 4 sheets

| Frame | Descricao Detalhada |
|---|---|
| **1** | Pe direito a frente, pe esquerdo atras. Biblia na mao direita (segurando por baixo, peso visivel). Mao esquerda estendida a frente como se abrindo caminho/pregando. Aureola inclina com o movimento. Rosario balanca para esquerda. |
| **2** | Transicao: pe esquerdo comeca a passar. Corpo levemente inclinado para frente (determinacao). Biblia balanca para baixo com a gravidade. Mao esquerda sobe 3px (gesticulando). Fumaca trail atras das maos. |
| **3** | Pe esquerdo a frente, pe direito atras. ESPELHADO do frame 1 mas NAO exatamente simetrico (organico). Biblia do outro lado. Rosario balanca para direita. Boca mais aberta (murmurando oracoes). |
| **4** | Transicao: pe direito comeca a passar. Identico ao frame 2, espelhado. Aureola wobble para o outro lado. |
| **5** | Variacao do frame 1: pe direito a frente mas Biblia LEVANTADA 5px acima (como se mostrando para o mundo). Olhos olham para cima 1 frame. Flash minimo na aureola. |
| **6** | Variacao do frame 3: pe esquerdo a frente mas mao livre faz gesto de bencao (dedos juntos, polegar separado). Fumaca nas maos intensifica neste frame. |

**Notas de animacao**:
- Walk speed: determinado, quase marcial, mas com graca -- ele NAO corre, ele caminha com FE
- A Biblia tem PESO -- influencia o balance do corpo
- Trail de fumaca dourada fica para tras 3-4px durante movimento
- Rosario deve ter physics basica (pendulo simples)

---

### 3. ATTACK -- Biblia Sagrada (3 frames) -- "A Palavra de Deus... Literalmente"
**Sheet**: `daciolo-attack.png` (192x64px -- 3 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 12 (rapido, impactante)
**Direcoes**: 4 = 4 sheets

| Frame | Descricao Detalhada |
|---|---|
| **1 (Wind-up)** | Biblia levantada acima da cabeca com as DUAS maos enormes. Corpo inclinado para tras 15 graus. Olhos LASER (pupilas brilhando amarelo). Boca ESCANCARADA preparando grito. Aureola brilho MAXIMO + spin rapido. Fumaca nas maos EXPLODE para cima. Musculatura dos bracos exagerada neste frame (deformacao de esforco). |
| **2 (Strike)** | Biblia DESCENDO em arco. Corpo projetado para frente. Motion blur na Biblia (2-3px de trail). Impacto visual: linhas de velocidade saindo da Biblia. Flash dourado no ponto de impacto. Boca: "GLOOO-" (meio do grito). Aureola deslocada para tras pelo momentum. |
| **3 (Impact)** | Biblia no chao/no inimigo. EXPLOSION de paginas biblicas (4-5 paginas voando como particulas). Flash branco 50% opacity no frame todo. Ondas de choque circulares a partir do ponto de impacto (douradas). Corpo recuperando postura. Boca: "-ORIA!" (fim do grito). Cruz de luz momentanea no ponto de impacto. |

**Notas de animacao**:
- O attack e VIOLENTO e SAGRADO ao mesmo tempo
- Paginas que voam sao particulas separadas (sprite sheet de particula 16x16)
- Dano extra contra tipo "demoniaco" -- flash vermelho no inimigo
- Hit feedback: screen shake minimo (2px, 100ms)
- SFX trigger: "GLORIA A DEUS!" gritado (varias intensidades aleatorias)

---

### 4. DEATH (4 frames) -- "A Ascensao do Profeta"
**Sheet**: `daciolo-death.png` (256x64px -- 4 frames de 64x64)
**Loop**: Nao, single play + hold ultimo frame
**FPS**: 6 (lento, dramatico, EPICO)
**Direcoes**: 1 (universal, sempre facing camera)

| Frame | Descricao Detalhada |
|---|---|
| **1 (O Golpe)** | Daciolo atingido. Corpo arqueado para tras. Biblia cai da mao (separando do corpo). Olhos AINDA mais arregalados (surpresa divina, NAO medo). Boca formando um "O" perfeito. Aureola FLICKER (pisca rapido). Fumaca nas maos intensifica MASSIVAMENTE. |
| **2 (A Elevacao)** | Corpo comeca a FLUTUAR. Pes saem do chao 5px. Bracos abrem em cruz (pose cristica). Raios de luz DOURADOS comecam a descer do topo do frame (4-5 raios diagonais). Aureola ESTABILIZA e brilha MAXIMO. Biblia no chao brilha. Expressao muda para EXTASE PURO -- sorriso beatico. Fumaca vira AURA completa ao redor do corpo. |
| **3 (A Transfiguracao)** | Corpo sobe mais 10px. Comeca a ficar TRANSLUCIDO (opacity 70%). Vestes ficam BRANCAS PURAS (mais brancas que o branco normal). Aureola DUPLICA (duas aureolas sobrepostas). Raios de luz multiplicam (8-10 raios). Coro de anjos visual: notas musicais douradas flutuando. Biblia no chao abre sozinha, paginas brilham. Expressao: paz absoluta, olhos semi-fechados pela primeira vez. |
| **4 (A Partida)** | Corpo quase invisivel (opacity 20%). Apenas silhueta dourada. COLUNA DE LUZ sobe do chao ate o topo do frame. Aureola vira estrela de 8 pontas. Fumaca dourada enche a area. No chao: Biblia aberta + rosario formando uma CRUZ PERFEITA. Flash branco final. Particulas de luz sobem como vagalumes divinos. |

**Notas de animacao**:
- Daciolo NUNCA morre normalmente. Ele ASCENDE
- Esta e a unica death animation do jogo com raios de luz e coro
- A Biblia que fica no chao pode ser "coletada" por outro jogador (buff temporario)
- Apos o frame 4: particulas de luz continuam por 2s no local
- Se Daciolo "morrer" perto de aliados: buff de +10% dano por 10s (inspiracao divina)
- Respawn: DESCE DO CEU com a mesma coluna de luz (inverso da death)

---

### 5. HIT (2 frames) -- "Fe Inabalavel"
**Sheet**: `daciolo-hit.png` (128x64px -- 2 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 12
**Direcoes**: 1 (universal)

| Frame | Descricao Detalhada |
|---|---|
| **1 (Impacto)** | Corpo recua 3px. Expressao: ZERO medo, apenas leve irritacao divina ("quem ousou?"). Flash branco momentaneo. Aureola flicker 1x. Biblia levantada defensivamente. Fumaca nas maos BURST (reacao instintiva divina). Olhos ficam AINDA mais arregalados -- impossivel, mas acontece. |
| **2 (Recuperacao)** | Corpo volta a posicao. Expressao volta ao extase normal. Micro-glow dourado no corpo todo (1 frame de aura protetiva). Biblia volta a posicao normal. Murmura algo (boca move minimo). Aureola estabiliza. |

**Notas de animacao**:
- Daciolo mal reage a dano. A fe PROTEGE
- Hit flash: dourado (NAO vermelho como outros personagens)
- Knockback reduzido vs outros personagens (50% do normal)
- Sound cue: "Queima, Jesus!" murmurado (baixo volume)
- Se levar 3 hits consecutivos: trigger fala "Sinto o cheiro de Satanas neste recinto!"

---

### 6. SPECIAL: Fumaca Santa (8 frames) -- AoE Massivo
**Sheet**: `daciolo-special-fumaca.png` (512x64px -- 8 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 10
**Direcoes**: 1 (universal, radial)

| Frame | Descricao Detalhada |
|---|---|
| **1 (Preparacao)** | Daciolo para. Fecha os olhos (UNICA vez que fecha os olhos). Biblia guardada nas costas (flutuando sozinha). Maos juntas em oracao na frente do peito. Fumaca concentra nas maos (volume crescendo). Aureola comeca spin lento. |
| **2 (Concentracao)** | Olhos ABREM -- pupilas brilhando DOURADO puro (sem iris visivel). Maos comecam a se separar lentamente. Entre as maos: esfera de fumaca dourada-branca se formando (8px, depois 12px). Aureola spin RAPIDO. Rosario levita. Aura azul celeste aparece. |
| **3 (Elevacao)** | Corpo levita 5px. Bracos abrem em V para cima. Esfera de fumaca agora entre as maos elevadas (16px). Tremor visual no sprite (1px shake). Vento radial visual: particulas sendo puxadas para o centro. |
| **4 (Detonacao)** | Bracos ABERTOS em cruz total. Esfera EXPLODE. Frame dominado por fumaca dourada-branca expandindo do centro. Daciolo no centro, silhueta escura contra a luz. Flash BRANCO INTENSO (opacity 80%). Grito: "FUMAAACA SANTAAAA!!" |
| **5 (Expansao 1)** | Fumaca expandiu para 50% do raio maximo. Detalhes visiveis: rostos angelicais na fumaca (pareidolia intencional). Zumbis no raio comecam a se desintegrar. Daciolo flutuando, bracos abertos, expressao de extase MAXIMO. |
| **6 (Expansao 2)** | Fumaca em 75% do raio. Cores: centro branco, meio dourado, borda levemente azulada. Particulas de cruz (+) voando dentro da fumaca. Destruicao total de zumbis em contato. |
| **7 (Pico)** | Fumaca em 100% do raio maximo. Tela inteira TOMADA. Visibilidade reduzida -- so se ve Daciolo como silhueta brilhante no centro. Raios de luz saindo em todas as direcoes. MAXIMUM HOLY ENERGY. |
| **8 (Dissipacao)** | Fumaca comeca a dissipar de fora para dentro. Daciolo desce ao chao. Expressao: exausto mas satisfeito (sorriso cansado). Bracos abaixam. Aureola volta ao brilho normal. Fumaca residual permanece por 1.5s. No chao: circulos dourados onde a fumaca tocou. |

**Notas de animacao**:
- O ataque MAIS PODEROSO DO JOGO
- Particulas de fumaca sao sprite sheet separado (`fumaca-santa-particles.md`)
- Destruicao de zumbis: eles viram PO DOURADO (particula especial)
- Cooldown visual: aureola fica DIM por 30s apos uso
- Camera zoom out 20% durante frames 4-7 para mostrar area de efeito
- SFX: coro de anjos + explosion reverb + "FUMAAACA SANTAAAA!"

---

### 7. SPECIAL: GLORIA A DEUS! (6 frames) -- Grito Supersonico
**Sheet**: `daciolo-special-gloria.png` (384x64px -- 6 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 10
**Direcoes**: 4 = 4 sheets (ondas de choque vao na direcao)

| Frame | Descricao Detalhada |
|---|---|
| **1 (Inspiracao)** | Daciolo puxa ar (peito infla GROTESCAMENTE, camisa estica). Maos na cintura. Biblia flutuando ao lado. Olhos fecham (concentracao). Aureola pulsa rapido. |
| **2 (Build-up)** | Boca comeca a abrir. Bochechas inflam. Corpo treme (anticipation). Olhos abrem -- LASER dourado comecando a vazar. Vento visual puxando particulas para ele (sucao). Cabelo (pouco) levanta. |
| **3 (GLOOOO-)** | Boca ESCANCARADA (ocupa 50% da cabeca -- deformacao GROTESCA Andre Guedes maximo). Primeiro anel de onda de choque (ring dourado expandindo). Olhos disparam raios LASER de fe. Corpo inclinado para tras pelo recoil do grito. Biblia voou para tras. Rosario horizontal pelo vento. |
| **4 (-ORIA A)** | Segundo e terceiro aneis de choque (menores atras do primeiro). Onda principal empurrando tudo. Daciolo mantendo grito, veias no pescoco visiveis (exagero anatomico). Linhas de velocidade radiais. |
| **5 (DEUS!!!)** | Quarto e quinto aneis. Pico de intensidade: flash branco momentaneo. Todos os inimigos no cone: stunned (estrelinhas + passarinhos ao redor da cabeca deles, estilo cartoon). Daciolo: expressao de FURIA SANTA. Aureola EXPLODE em tamanho (3x). |
| **6 (Eco)** | Aneis se dissipam. Daciolo recupera postura. Boca fecha para sorriso satisfeito. Biblia volta flutuando para a mao. Eco visual: linhas onduladas no ar (tipo calor). Aureola volta ao normal com bounce. |

**Notas de animacao**:
- Cone de efeito: 60 graus na direcao do grito
- Stun duration: 3 segundos em todos os inimigos no cone
- Ondas de choque sao overlay separado (nao parte do sprite)
- 10% chance de FALHA COMICA: ver sprite sheet de Erro Comico
- SFX: "GLORIA A DEUS!" delay reverb massivo
- Inimigos stunned: animacao de tontura (circulos sobre cabeca)

---

### 8. SPECIAL: Exorcismo Eleitoral (6 frames) -- Cura + Remove Debuffs
**Sheet**: `daciolo-special-exorcismo.png` (384x64px -- 6 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 8 (mais lento, cerimonial)
**Direcoes**: 1 (universal)

| Frame | Descricao Detalhada |
|---|---|
| **1 (Invocacao)** | Daciolo planta os pes firme. Biblia aberta na mao esquerda (paginas brilhando). Mao direita levantada, palma para frente. Expressao: seriedade divina. Aureola estabiliza. Fumaca concentra na mao direita. |
| **2 (Imposicao)** | Mao direita projeta para frente (imposicao de maos). Raios de luz saem da palma (5-6 raios finos dourados). Biblia brilha mais. Boca: "QUEIMA..." Olhos: pupilas douradas. |
| **3 (QUEIMA)** | "...JESUS!" -- Explosao de luz da mao. Raios se multiplicam (10-12). Cruz de luz se forma no ar na frente da mao. Aliados no raio: aura verde de cura aparece. Brilho intenso. |
| **4 (Purificacao)** | Aliados: debuffs removidos (icones de debuff EXPLODEM em particulas). Cura visivel: numeros verdes subindo (+HP). Cruz de luz gira. Mao continua projetada. Fumaca SANTA envolve aliados. |
| **5 (SHABALABA)** | Daciolo grita "SHABALABA!" -- distorcao sonora visual (linhas onduladas saindo da boca). Pulso final de cura. Cruz de luz dissolve em particulas de estrela. Fumaca nas maos pico maximo. |
| **6 (Bencao)** | Mao abaixa. Biblia fecha. Expressao volta ao extase calmo. Aliados curados tem brilho dourado residual 2s. Aureola de Daciolo: flash agradecimento. Sussurra oracao (boca move minimo). |

**Notas de animacao**:
- Area de efeito: circulo ao redor de Daciolo (raio medio)
- Cura: 25% HP de todos aliados na area
- Remove TODOS debuffs (veneno, slow, corruption, etc)
- Visual de cura nos aliados: espiral dourada subindo + flash verde
- SFX: "Queima, Jesus! Shabalaba!" + som de sino de igreja + coro suave

---

### 9. SPECIAL: Monte Roraima Sagrado (8 frames) -- Invoca Montanha + Chuva de Fogo
**Sheet**: `daciolo-special-roraima.png` (512x64px -- 8 frames de 64x64)
**Loop**: Nao, single play (frames 6-8 loop durante duracao)
**FPS**: 10
**Direcoes**: 1 (universal)

| Frame | Descricao Detalhada |
|---|---|
| **1 (Invocacao)** | Daciolo ergue as duas maos para o ceu. Biblia flutuando. Olhos para cima, brilhando. Boca: "MONTE..." Aureola sobe 5px acima da cabeca. Terra ao redor comeca a tremer (linhas de rachadura). |
| **2 (Terremoto)** | Chao RACHA. Screen shake 3px. Pedras comecam a subir do chao. Fumaca de poeira (marrom) mistura com fumaca santa (dourada). Daciolo imivel, concentrado, maos ainda para cima. |
| **3 (Emergencia)** | Ponta do Monte Roraima IRROMPE do chao (topo plano caracteristico). Rochas e terra voando como particulas. Daciolo pula para cima (ou e levantado pela montanha). Flash de luz na base. |
| **4 (Ascensao)** | Montanha subiu 50%. Forma de mesa/tepui visivel. Daciolo na lateral, subindo junto. Cachoeiras comecam a cair das bordas (referencia real ao Roraima). Particulas de terra continuam. |
| **5 (Topo)** | Montanha COMPLETA. Daciolo no TOPO, silhueta contra o ceu. Bracos abertos em V. Nuvens ao redor do topo. Aureola brilho MAXIMO. Transicao: ceu fica dourado. |
| **6 (Fogo Santo 1)** | Comeca CHUVA DE FOGO SANTO do topo. Bolas de fogo dourado caindo em padrao AoE. Daciolo no topo fazendo gestos de direcao (apontando onde o fogo cai). Impactos no chao: explosoes de cruz (+). |
| **7 (Fogo Santo 2)** | Intensidade maxima da chuva de fogo. Multiplos impactos simultaneos. Chao coberto de cruzes de fogo. Daciolo: gritando oracao (boca aberta full). Inimigos no raio: dano massivo + on fire. |
| **8 (Descida)** | Chuva diminui. Montanha comeca a AFUNDAR de volta no chao. Daciolo desce suavemente (flutuando). Montanha desaparece, deixando cratera com marca de cruz. Fumaca residual. Daciolo pousa, postura de oracao. |

**Notas de animacao**:
- Duracao total do efeito: 8 segundos
- Montanha e sprite separado (ver `monte-roraima-surgindo.md`)
- Chuva de fogo: particulas separadas 16x16px
- Dano AoE continuo durante frames 6-7 (loop)
- Screen shake durante frames 2-4 (3px, diminuindo)
- SFX: terremoto + vento + coro angelical + impactos de fogo

---

### 10. SPECIAL: URSAL Cataclismica (8 frames) -- Ultimate Ability
**Sheet**: `daciolo-special-ursal.png` (512x64px -- 8 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 8 (cinematico, pesado)
**Direcoes**: 1 (universal)

| Frame | Descricao Detalhada |
|---|---|
| **1 (Revelacao)** | Daciolo olha para CIMA com terror SANTO. Aponta para o ceu com uma mao. Outra mao segura Biblia contra o peito. Grita: "A URSAL! A URSAL EXISTE!" Olhos MAXIMOS. Aureola pisca frenetico. |
| **2 (Sombra)** | Sombra comeca a crescer no CHAO. Forma vagamente continental (America Latina). Ceu escurece. Daciolo recua 3px, ainda apontando para cima. Vento ascendente (cabelo/roupas pra cima). |
| **3 (Descida 1)** | O MAPA DA URSAL aparece no topo do frame, descendo. Estilizado: contorno grosso da America Latina, URSAL escrito em vermelho vivo, estrelas comunistas nos cantos. Sombra no chao 50%. Daciolo: bracos em posicao de defesa/adoracao. |
| **4 (Descida 2)** | Mapa em 50% da descida. ENORME (ocupa 70% do frame). Detalhes visiveis: paises delineados, simbolos parodicos, letras URSAL pulsando vermelho. Daciolo corre para fora do ponto de impacto. Tremor no chao. |
| **5 (IMPACTO!)** | MAPA ATINGE O CHAO. EXPLOSAO TOTAL. Flash branco 100% opacity (1 sub-frame). Onda de choque circular MASSIVA expandindo. Particulas de mapa voando (pedacos de continente). Screen shake MAXIMO (5px, 500ms). Poeira, fumaca, destruicao. |
| **6 (Devastacao)** | Pos-impacto. Cratera com formato da America Latina no chao. Ondas de choque continuam (2o e 3o anel). Todos os inimigos na area: ELIMINADOS (particulas). Fragmentos de mapa flutuam. Letras "URSAL" PISCANDO no centro da cratera (vermelho neon). |
| **7 (Aftermath)** | Poeira baixando. Cratera visivel com glow vermelho. Letras URSAL continuam piscando. Daciolo caminha DE VOLTA para o centro da cratera. Expressao: vindicacao total ("EU AVISEI!"). Aureola brilho MAXIMO. |
| **8 (Victoria)** | Daciolo no centro da cratera, braco erguido com Biblia. Pose heroica. Fala: "EU AVISEI! A URSAL EXISTE!" Glow dourado emana dele. Letras URSAL desvanecem. Cratera comeca a fechar. Particulas de estrela sobem. |

**Notas de animacao**:
- ULTIMATE ABILITY -- mais poderoso que Fumaca Santa em dano puro
- Mapa da URSAL e sprite separado (ver `ursal-cataclismica.md`)
- Dano: elimina TODOS inimigos na area do mapa (area GIGANTE)
- Cooldown: o mais longo do jogo (60s+)
- Camera: zoom out 40% durante frames 3-7
- SFX: sirene de alerta + trovao + impacto nuclear + "A URSAL EXISTE!" echo

---

### 11. SPECIAL: Candidatura Divina 2026 (4 frames) -- Confusao
**Sheet**: `daciolo-special-candidatura.png` (256x64px -- 4 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 10
**Direcoes**: 4 = 4 sheets

| Frame | Descricao Detalhada |
|---|---|
| **1 (O Bolso)** | Daciolo coloca mao no bolso da calca. Expressao: sorriso maroto (RARO). Biblia na outra mao. Aureola pisca "?" (easter egg visual). Fumaca nas maos diminui. |
| **2 (O Santinho)** | Puxa SANTINHO do bolso. Panfleto eleitoral: "DACIOLO 2026 -- MOBILIZA!" com foto dele sorrindo (mini-retrato no panfleto, meta-humor). Apresenta com orgulho, braco estendido. Brilho divino no santinho (LOL). |
| **3 (A Distribuicao)** | Estende santinho na direcao do inimigo. Brilho HIPNOTICO emana do santinho (espiral dourada). Inimigo PARA de atacar, olhando fixo para o santinho. Expressao do inimigo: confusao total, cocando a cabeca (se tiver mao). Bolha de pensamento: "?" aparece sobre inimigos. |
| **4 (A Duvida)** | Inimigos no raio: estado CONFUSO (3s). Caminham em circulos, atacam aliados deles. Santinho continua brilhando no ar (flutuou da mao). Daciolo: braco cruzados, sorriso satisfeito, aureola com formato de coracao (1 frame). Fala: "Nao estou a venda para o sistema!" |

**Notas de animacao**:
- A skill mais COMICA do kit
- Inimigos confusos: animacao especial de "tontura" + "?" flutuando
- O santinho fisico fica no chao apos uso (interactable, dura 10s)
- Se outro jogador pega o santinho: buff comico "Considerando o voto" (+5% speed 10s)
- SFX: jingle de campanha distorcido + "Nao estou a venda!"
- Metalinguagem 2026: referencia REAL a pre-candidatura pelo Mobiliza

---

### 12. SPECIAL: Exorcismo em Massa (8 frames) -- Mega Cura
**Sheet**: `daciolo-special-exorcismo-massa.png` (512x64px -- 8 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 8 (majestoso)
**Direcoes**: 1 (universal)

| Frame | Descricao Detalhada |
|---|---|
| **1** | Daciolo planta pes, abre bracos em cruz. Biblia flutuando acima. Olhos fecham (oracao profunda). Aureola brilha constante. |
| **2** | Esfera de luz dourada se forma ao redor de Daciolo (raio pessoal). Maos comecam a emitir raios em TODAS as direcoes. Biblia abre no ar, paginas brilhando. |
| **3** | Esfera EXPANDE (raio medio). Raios dourados tocam aliados proximos. Onde tocam: flash de cura verde + debuffs sendo "queimados" (icones pegando fogo e desaparecendo). |
| **4** | Esfera em RAIO MAXIMO. Cobre area gigante. TODOS aliados no raio: brilho de cura. Coro de anjos visual: notas musicais douradas descendo do topo. |
| **5** | Pico de cura: +25% HP para todos. Numeros verdes "+HP" subindo de cada aliado. Raios dourados formando padrao de MANDALA no chao. Biblia girando. |
| **6** | Debuffs de TODOS aliados: REMOVIDOS (explosao de icones). Cada aliado: brilho individual branco 1 frame. Daciolo: expressao de esforco maximo. |
| **7** | Coro de anjos atinge pico: entidades angelicais translucidas aparecem brevemente (silhuetas, nao detalhadas). Raios formam CRUZ no ceu acima. |
| **8** | Energia retrai para Daciolo. Olhos abrem. Sorriso sereno. Aureola volta ao normal. Aliados: glow dourado residual 3s. Biblia volta a mao. Sussurra: "Pela honra e gloria de Nosso Senhor." |

---

### 13. ERRO COMICO (4 frames) -- "Gloria a sap-- opa!"
**Sheet**: `daciolo-erro-comico.png` (256x64px -- 4 frames de 64x64)
**Loop**: Nao, single play
**FPS**: 10
**Direcoes**: 1 (universal)
**Trigger**: 10% de chance quando usa GLORIA A DEUS!

| Frame | Descricao Detalhada |
|---|---|
| **1 (Build-up identico)** | Mesma preparacao do GLORIA A DEUS! -- ar puxado, peito inflado, boca abrindo. Idencia ao especial normal. Jogador acha que e o ataque normal. |
| **2 (O Erro)** | Boca abre. Onda de choque comeca... mas SAI FRACA (anel fino, sem brilho, wobble patético). Tamanho: 30% do normal. Cor: dourado desbotado. Daciolo: olhos arregalam de SURPRESA (nao de poder). "Glo-glo-glo..." gagueijo visual (boca abre-fecha-abre). |
| **3 (A Vergonha)** | Onda de choque dissipa imediatamente. Daciolo: MAO NA BOCA. Expressao de "ops". Aureola APAGA por 1 frame (vergonha divina). Rubor vermelho nas bochechas. Gota de suor classica de anime no lado da cabeca. Biblia cai da mao (bounce no chao). Fala: "Gloria a sap-- opa!" |
| **4 (A Correcao)** | Daciolo rapidamente se recompoe. Pega Biblia do chao. Limpa a garganta (mao no pescoco). Aureola volta (timidamente, brilho 50%). Grita rapido: "GLORIA A DEUS!" -- mas SEM efeito de dano (so o grito). Expressao: "finge que nao aconteceu". Aliados proximos: animacao de "?" (confusos). |

**Notas de animacao**:
- 10% de chance APENAS no GLORIA A DEUS! -- nunca nos outros specials
- O efeito de stun NAO acontece (skill falha)
- Inimigos: NAO sao afetados, podem aproveitar para atacar
- E a UNICA vulnerabilidade comica do Daciolo
- SFX: "GLOO-- *engasgo* --ria a sap-- opa, Gloria a Deus!" (audio especial)
- Se o erro acontecer com um boss na tela: o boss RIA (animacao especial de reacao)

---

## Resumo de Sprite Sheets

| Arquivo | Dimensoes | Frames | FPS | Direcoes |
|---|---|---|---|---|
| `daciolo-idle.png` | 256x64 | 4 | 8 | 4 |
| `daciolo-walk.png` | 384x64 | 6 | 10 | 4 |
| `daciolo-attack.png` | 192x64 | 3 | 12 | 4 |
| `daciolo-death.png` | 256x64 | 4 | 6 | 1 |
| `daciolo-hit.png` | 128x64 | 2 | 12 | 1 |
| `daciolo-special-fumaca.png` | 512x64 | 8 | 10 | 1 |
| `daciolo-special-gloria.png` | 384x64 | 6 | 10 | 4 |
| `daciolo-special-exorcismo.png` | 384x64 | 6 | 8 | 1 |
| `daciolo-special-roraima.png` | 512x64 | 8 | 10 | 1 |
| `daciolo-special-ursal.png` | 512x64 | 8 | 8 | 1 |
| `daciolo-special-candidatura.png` | 256x64 | 4 | 10 | 4 |
| `daciolo-special-exorcismo-massa.png` | 512x64 | 8 | 8 | 1 |
| `daciolo-erro-comico.png` | 256x64 | 4 | 10 | 1 |

**Total de sprite sheets**: 13 base + variantes por direcao = **33 arquivos PNG**

---

## Paleta de Cores (Hex)

| Cor | Hex | Uso |
|---|---|---|
| Branco Puro (camisa) | `#FFFFFF` | Camisa, flashes de luz |
| Branco Sujo (highlights) | `#F5F0E6` | Highlights de pele, reflexos |
| Dourado Aureola | `#FFD700` | Aureola, raios divinos, fumaca |
| Dourado Intenso | `#FFA500` | Glow de poder, explosoes |
| Azul Celeste (aura) | `#87CEEB` | Aura divina, efeitos de cura |
| Amarelo Raios | `#FFFF00` | Raios dos olhos, flashes |
| Pele Base | `#D4956A` | Pele |
| Pele Sombra | `#A0694B` | Sombras na pele |
| Preto Contorno | `#1A1A1A` | Linhas grossas, contornos |
| Marrom Biblia | `#8B4513` | Capa da Biblia |
| Marrom Dourado | `#B8860B` | Detalhes Biblia, rosario |
| Cinza Calca | `#3C3C3C` | Calca social |
| Vermelho URSAL | `#CC0000` | Letras URSAL, efeitos especiais |
| Verde Cura | `#32CD32` | Numeros de cura, efeitos heal |
| Rosa Vergonha | `#FF6B6B` | Rubor do erro comico |
