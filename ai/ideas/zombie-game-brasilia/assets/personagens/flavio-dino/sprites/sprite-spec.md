# FLAVIO DINO (A Muralha Burocratica) - Sprite Specification

## Overview
- **Personagem**: Flavio Dino — Boss STF
- **Titulo**: A Muralha Burocratica
- **Sprite Dimensions**: 64x64px
- **Sprite Sheet Layout**: Horizontal strip, 1 row por animacao
- **Format**: PNG com alpha transparency
- **Perspectiva**: Top-down levemente isometrica (Y-sorting)
- **Anchor Point**: Bottom-center (32, 60) — centro de massa baixo (personagem pesado)

## Anatomia Base do Personagem (64x64)

### Proporcoes Grotescas Andre Guedes
- **Cabeca**: ~18x16px. Careca reluzente, sem cabelo nenhum. Bigode GROSSO escuro ocupando metade do rosto inferior. Olhos pequenos, semicerrados, expressao de NEGACAO permanente. Sobrancelhas grossas e baixas.
- **Tronco**: ~28x20px. LARGO. Costas tao largas que o personagem parece um MURO visto de frente. Toga preta apertada demais — costuras visiveis estourando, tecido esticado ao maximo, botoes saltando.
- **Bracos**: ~12x24px CADA. DESPROPORCIONALMENTE enormes. Musculosos como de halterofilista. Biceps e triceps visiveis mesmo sob a toga (que estica). Antebracos grossos, maos enormes. Sao maiores que a cabeca — essa e a DEFORMIDADE principal.
- **Pernas**: ~8x18px cada. Normais-grossas. Suportam o peso da muralha. Sapatos sociais pretos.
- **Carimbo "NEGADO"**: ~16x20px. Do tamanho de um extintor de incendio. Corpo cilindrico VERMELHO BERRANTE (#CC0000). Base do carimbo com letras "NEGADO" em branco invertido. Cabo preto na parte de cima. DESPROPORCIONAL — quase do tamanho do torso.

### Paleta de Cores

| Elemento              | Hex       | Descricao                                |
|-----------------------|-----------|------------------------------------------|
| Careca (base)         | `#D4956A` | Tom de pele quente, brilho central       |
| Careca (brilho)       | `#F0C090` | Reflexo na careca (2-3px highlight)      |
| Careca (sombra)       | `#A06B42` | Sombra lateral                           |
| Bigode                | `#1A1A1A` | Preto quase absoluto, grosso             |
| Olhos                 | `#2C2C2C` | Escuros, semicerrados, raiva contida     |
| Sobrancelhas          | `#1A1A1A` | Grossas, baixas, franzidas               |
| Toga (base)           | `#0D0D0D` | Preto sujo, nao preto puro              |
| Toga (costura)        | `#3A3A3A` | Cinza — costuras visiveis esticadas      |
| Toga (esticada)       | `#1A1A1A` | Areas onde o tecido estica e clareia     |
| Toga (botao voando)   | `#C0C0C0` | Botoes metalicos que saltam              |
| Bracos (pele)         | `#D4956A` | Tom de pele, veias visiveis              |
| Bracos (veias)        | `#8B4726` | Veias saltadas de esforco                |
| Bracos (musculo)      | `#C08050` | Sombra dos musculos definidos            |
| Carimbo (corpo)       | `#CC0000` | Vermelho BERRANTE, alarme de incendio    |
| Carimbo (highlight)   | `#FF2020` | Brilho no vermelho                       |
| Carimbo (sombra)      | `#8B0000` | Sombra do cilindro                       |
| Carimbo (texto)       | `#FFFFFF` | "NEGADO" invertido na base               |
| Carimbo (cabo)        | `#1A1A1A` | Cabo preto no topo                       |
| Marca no chao         | `#CC0000` | Marca de carimbo "NEGADO" pos-ataque     |
| Sapatos               | `#0D0D0D` | Pretos, sociais                          |
| Outline               | `#0A0A0A` | Contorno grosso 2px (Crumb style)        |
| Sombra chao           | `#0D0D0D` | Drop shadow 50% opacity                  |
| Papel (emenda)        | `#F5F0DC` | Papel amarelado de documento oficial     |
| Papel (texto)         | `#333333` | Texto impresso nos papeis                |
| Carimbo marca (chao)  | `#CC0000` | Estampa "NEGADO" que fica no chao        |
| Gelo (bloqueio)       | `#A0D8EF` | Efeito de congelamento orcamentario      |
| Barreira (liminar)    | `#CC0000` | Muro vermelho translucido da liminar     |

---

## IDLE — 4 Frames (256x64px sprite sheet)

**Conceito**: Flavio Dino PARADO como uma muralha. Inamovivel. Bracos cruzados segurando o carimbo. Bigode tremendo microscopicamente de negacao constante. A toga pulsa porque os musculos dos bracos a esticam. Ele NAO se move — ele BLOQUEIA.

### Frame 0: Muralha Estatica
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Dino de frente, postura rigida como monumento. Bracos ENORMES cruzados sobre o peito, carimbo "NEGADO" seguro na mao direita (visivel acima do braco esquerdo). Careca brilhando com highlight de 3px no topo. Bigode grosso, reto, imovivel. Olhos semicerrados — expressao de "ja neguei antes de voce pedir". Toga APERTADISSIMA — costuras visiveis nos ombros, tecido esticado sobre os biceps colossais. Um botao da toga ja esta faltando (voou). Pernas afastadas, postura de porteiro cosmico. Sombra larga no chao (personagem ocupa muito espaco).
- **Notas de estilo**: Contorno de 2px grosso e irregular (Crumb). Assimetria proposital — braco direito LIGEIRAMENTE maior que o esquerdo (mao do carimbo). A careca tem um brilho seboso, nao limpo.

### Frame 1: Micro-Negacao 1
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: IDENTICO ao Frame 0 MAS: bigode mexe 1px para a esquerda (treme de negacao). Uma micro-veia pulsa no braco direito (1px mais escura). A careca tem o reflexo deslocado 1px. Um papelzinho (emenda) aparece caindo no canto superior direito (3x3px, papel amarelado).
- **Notas de estilo**: A mudanca e MINIMA — o personagem e uma MURALHA, nao se move quase nada. O tremor do bigode e a unica indicacao de que esta vivo.

### Frame 2: Micro-Negacao 2
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Bigode volta ao centro MAS os olhos apertam 1px (semicerram mais). O carimbo na mao brilha mais (highlight 1px mais forte no vermelho). A toga estica um POUQUINHO mais nos biceps (1px de gap na costura). O papelzinho do Frame 1 ja caiu mais (esta na altura da cintura, ainda caindo).
- **Notas de estilo**: Sensacao de tensao crescente. A qualquer momento ele pode NEGAR algo.

### Frame 3: Micro-Negacao 3
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Bigode treme 1px para a DIREITA agora. Olhos voltam ao semi-fechado normal. O papelzinho do Frame 1-2 esta no chao agora, com uma marca vermelha minuscula (foi carimbado). Braco esquerdo apertou 1px mais (cruzou mais forte). Boto da toga que estava faltando — agora o buraco e visivel (1px claro).
- **Notas de estilo**: Ciclo completo de micro-negacao. Quando loopado: bigode treme esq-centro-dir-centro, emendas caem e sao carimbadas. A MURALHA vive e respira negacao.

**Resumo Idle Sheet**:

| Frame | Nome              | Posicao   | Descricao curta                      |
|-------|-------------------|-----------|--------------------------------------|
| 0     | muralha_estatica  | 0-63      | Bracos cruzados, imovivel            |
| 1     | micro_negacao_1   | 64-127    | Bigode esq, veia pulsa, papel cai    |
| 2     | micro_negacao_2   | 128-191   | Olhos apertam, carimbo brilha        |
| 3     | micro_negacao_3   | 192-255   | Bigode dir, papel carimbado no chao  |

---

## WALK — 6 Frames (384x64px sprite sheet)

**Conceito**: Marcha PESADISSIMA de muralha ambulante. O CHAO TREME a cada passo. O carimbo arrasta no chao deixando marcas vermelhas. A toga ESTICA a cada passo (os musculos se contraem). Nao e andar — e AVANCAR. Como um tanque de guerra burocratico.

### Frame 0: Passo Esquerdo - Levanta
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Perna esquerda levantando (pe 4px acima do chao). Braco direito avanca com carimbo (balanca para frente). Braco esquerdo vai para tras. Toga PUXA nos ombros (esticada pelo movimento). Careca inclina 1px para frente (inerciam). Linhas de impacto no chao sob o pe direito que sustenta o peso (2 linhas de 1px irradiando).
- **Notas**: O peso do personagem deve ser EVIDENTE. Sombra no chao e GRANDE.

### Frame 1: Passo Esquerdo - Avanca
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Perna esquerda no ar, avancando. Tronco inclina 2px para frente. Carimbo na mao direita ARRASTA no chao (ponta vermelha toca o ground level). Marca vermelha de arrasto aparece atras (linha de 1px vermelha no chao). Toga estica nos biceps — gap de costura visivel no ombro direito. Bigode treme para tras (vento do movimento).
- **Notas**: O carimbo arrastando e ESSENCIAL. Onde Dino passa, fica marcado.

### Frame 2: Passo Esquerdo - Planta
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Pe esquerdo BATE no chao. IMPACTO VISUAL: 3 linhas de choque irradiando do pe (4px cada, 1px grossura). Pequenas particulas de poeira sobem (3-4 pixels cinza claro). O corpo inteiro TREME 1px para baixo (squash do impacto). Toga balanca. Carimbo levanta do chao (marca vermelha permanece atras). Careca brilha mais (suor do esforco).
- **Notas**: O IMPACTO do passo e a piada visual. Esse homem PESA como uma muralha.

### Frame 3: Passo Direito - Levanta
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Espelho do Frame 0 mas invertido. Perna direita levanta. Braco esquerdo avanca. Carimbo na mao direita levanta junto (nao arrasta neste frame). Toga puxa no lado oposto. Uma costura ESTOURA no ombro esquerdo (1px de gap novo).
- **Notas**: Espelhamento NAO e perfeito — assimetria proposital (Andre Guedes).

### Frame 4: Passo Direito - Avanca
- **Posicao no sheet**: 256,0 a 319,63
- **Descricao**: Perna direita avancando. Carimbo desce e toca o chao de novo (arrasto vermelho retoma). Tronco inclina para frente. Toga estica tanto que outro botao SALTA (botao de 2px voa para cima-direita como projetil comico). Bigode treme para tras. Veias nos bracos mais visiveis (esforco da marcha).
- **Notas**: Botao voando e detalhe comico ESSENCIAL. A toga nao aguenta os musculos.

### Frame 5: Passo Direito - Planta
- **Posicao no sheet**: 320,0 a 383,63
- **Descricao**: Pe direito BATE no chao. Mesmo impacto do Frame 2 mas MAIS FORTE (4 linhas de choque, particulas maiores). O chao parece RACHAR (1px de linha de rachadura). Corpo treme 2px para baixo (squash maior). Carimbo balanca violentamente. Marca "NEGADO" fica impressa no chao onde o pe bateu (marca vermelha 4x2px). Toda a imagem treme.
- **Notas**: O ultimo passo do ciclo e o mais pesado. AMPLIFICA tudo.

**Resumo Walk Sheet**:

| Frame | Nome                | Posicao   | Descricao curta                          |
|-------|---------------------|-----------|------------------------------------------|
| 0     | passo_esq_levanta   | 0-63      | Perna esq sobe, peso no pe dir           |
| 1     | passo_esq_avanca    | 64-127    | Avanca, carimbo arrasta no chao          |
| 2     | passo_esq_planta    | 128-191   | IMPACTO no chao, poeira, treme           |
| 3     | passo_dir_levanta   | 192-255   | Perna dir sobe, costura estoura          |
| 4     | passo_dir_avanca    | 256-319   | Avanca, botao da toga voa                |
| 5     | passo_dir_planta    | 320-383   | IMPACTO forte, chao racha, marca NEGADO  |

---

## ATTACK — 3 Frames (192x64px sprite sheet)

**Conceito**: CARIMBADA DEVASTADORA. Dino ergue o carimbo gigante com os bracos colossais, DESCE com forca apocaliptica, e a marca "NEGADO" fica estampada no chao/inimigo. E um ataque de ESMAGAMENTO BUROCRATICO.

### Frame 0: Ergue o Carimbo
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Dino de frente, pernas afastadas plantadas no chao. Ambos os bracos ENORMES erguidos acima da cabeca segurando o carimbo. O carimbo esta NO TOPO do frame, quase saindo (base do carimbo com "NEGADO" visivel de baixo). Bracos totalmente esticados — biceps e triceps em definicao MAXIMA, veias saltadas GROTESCAS (3-4 linhas de veias por braco). Toga RASGA nos ombros (gap de 3px nos dois lados — os musculos sao DEMAIS). Rosto olhando para cima, bigode apontando para cima, olhos ARREGALADOS de determinacao (unico momento que os olhos abrem). Boca fechada, mandibula travada.
- **Notas**: Este e o UNICO frame onde os olhos de Dino abrem completamente. E a unica coisa que o empolga: NEGAR.

### Frame 1: CARIMBA!
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: FRAME DE IMPACTO. Bracos desceram VIOLENTAMENTE. Carimbo BATEU no chao/inimigo. O carimbo esta no nivel do chao, ESMAGADO contra a superficie. Os bracos estao comprimidos (squash — mais curtos e mais grossos que o normal). ONDA DE CHOQUE: 6 linhas de impacto irradiando do carimbo (8px cada, 1px grossura, distribuidas radialmente). Marca "NEGADO" ENORME aparece em vermelho no chao (16x8px, letras grossas). Papeis voam em TODAS as direcoes (6-8 particulas de papel, 2x3px cada, papel amarelado com texto). Poeira e fragmentos de chao sobem (particulas cinza). A toga ESTOUROU uma costura inteira na lateral (gap de 5px mostrando camiseta branca por baixo). Rosto: olhos FECHADOS de forca, bigode comprimido, veias na testa (2px).
- **Notas**: FRAME PRINCIPAL. Maximizar caos visual. Tudo estoura, voa, racha. E o momento de NEGACAO ABSOLUTA.

### Frame 2: Pos-Carimbada
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Recuperacao. Dino de pe, carimbo ao lado do corpo (na mao direita, descansando). Bracos voltam a posicao natural (pendurados, relaxados, ainda enormes). Expressao de SATISFACAO CONTIDA — olhos semicerrados de novo, MAS com um MICRO-SORRISO debaixo do bigode (1px de curvatura no canto da boca). Marca "NEGADO" ainda visivel no chao, agora desbotando. Papeis ainda caindo (ultimos 2-3 no ar). Toga rasgada permanece rasgada. Uma leve aura de tinta vermelha no ar (2-3px vermelhos translucidos ao redor do carimbo).
- **Notas**: O micro-sorriso e CRUCIAL. "Eu nao bloqueio por prazer... ta, tambem por prazer." E o unico momento de quase-emocao.

**Resumo Attack Sheet**:

| Frame | Nome            | Posicao   | Descricao curta                          |
|-------|-----------------|-----------|------------------------------------------|
| 0     | ergue_carimbo   | 0-63      | Bracos erguidos, carimbo no alto         |
| 1     | CARIMBA         | 64-127    | IMPACTO! Marca NEGADO, papeis voam       |
| 2     | pos_carimbada   | 128-191   | Recupera, micro-sorriso, tinta no ar     |

---

## DEATH — 4 Frames (256x64px sprite sheet)

**Conceito**: A MURALHA DESMORONA. Os bracos (fonte do poder) MURCHAM primeiro. O carimbo QUEBRA. Papeis de emenda voam LIBERADOS (sao livres!). A toga finalmente EXPLODE (alivio). Dino vira escombros de burocracia.

### Frame 0: Primeira Rachadura
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Dino em pe MAS com rachaduras aparecendo no corpo (como uma muralha de concreto rachando). 3-4 linhas de rachadura brancas/cinza no tronco e bracos. Expressao de CHOQUE — olhos arregalados, bigode caindo (pontas para baixo pela primeira vez). Carimbo na mao treme (linhas de vibracao 2px ao redor). A toga tem uma rachadura tambem (como se fosse parte do corpo). Careca perde o brilho (highlight desaparece — sem energia).
- **Notas**: A muralha esta cedendo. Pela PRIMEIRA vez, Dino parece vulneravel.

### Frame 1: Bracos Murcham
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Os bracos ENORMES comecam a MURCHAR. Biceps perdem 30% do volume (pixels de musculo somem, substitutidos por contorno flacido). As veias somem. Os bracos agora parecem normais-finos — CHOCANTE em contraste com o que eram. A toga, que estava apertada, agora esta FOLGADA nos bracos (sobra tecido). Carimbo ESCORREGA da mao (esta caindo, angulo de 30 graus). Rachaduras no tronco se expandem. Papeis de emenda comecam a sair das rachaduras (como se estivessem presos DENTRO dele). 4-5 papeis escapando por fendas no corpo.
- **Notas**: Os bracos murchando e a PIADA VISUAL da morte. Sem os bracos, nao ha carimbo. Sem carimbo, nao ha muralha.

### Frame 2: Carimbo Quebra
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: O carimbo atingiu o chao e QUEBROU em 3-4 pedacos. Fragmentos vermelhos espalhados (4-5 particulas de 3x3px vermelhas). A base com "NEGADO" esta rachada ao meio. Dino caindo de joelhos (corpo na metade inferior do frame). Bracos completamente murchos — finos como palitos, pendurados. Toga EXPLODE: botoes voam em todas direcoes (4 botoes de 2px), costuras se abrem, tecido se abre revelando uma camiseta branca por baixo. DEZENAS de papeis de emenda voam para CIMA (15-20 particulas de papel em arco, como confete de libertacao). Bigode caindo mais (quase vertical).
- **Notas**: Os papeis voando para CIMA sao a IRONIA: com a muralha caindo, as emendas sao LIBERADAS. E comico e dramatico.

### Frame 3: Escombros Burocraticos
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Dino no chao como uma PILHA DE ESCOMBROS. O corpo virou fragmentos: pedacos de toga preta, restos de carimbo vermelho, papeis de emenda espalhados, botoes rolando. No centro, a careca ainda e visivel (brilhando fracamente) com o bigode ao lado (caiu separado, como bigode postico). Acima dos escombros, papeis de emenda flutuam em espiral para o ceu (5-6 papeis subindo, ficando menores). Um ultimo papel no topo tem uma marca de "NEGADO" que esta DESBOTANDO (o vermelho virando rosa, virando branco — a negacao morre).
- **Notas**: Frame final. A muralha agora e ruina. Os documentos estao livres. O "NEGADO" desbota. A burocracia perdeu.

**Resumo Death Sheet**:

| Frame | Nome                  | Posicao   | Descricao curta                          |
|-------|-----------------------|-----------|------------------------------------------|
| 0     | primeira_rachadura    | 0-63      | Rachaduras no corpo, careca sem brilho   |
| 1     | bracos_murcham        | 64-127    | Bracos perdem volume, papeis escapam     |
| 2     | carimbo_quebra        | 128-191   | Carimbo quebra, toga explode, emendas voam |
| 3     | escombros             | 192-255   | Pilha de ruinas, papeis livres no ceu    |

---

## HIT — 2 Frames (128x64px sprite sheet)

**Conceito**: A muralha RECEBE impacto mas nao cai — so fica MAIS BRAVA. A toga estica mais (quase estoura). A expressao muda de "negacao" para "negacao FURIOSA". O proximo carimbo vai ser PIOR.

### Frame 0: Impacto Recebido
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Dino recua 2px para tras (leve empurrao). Flash branco no corpo (tint overlay 50% branco por 1 frame). Olhos ABREM de surpresa-raiva (2px mais abertos). Bigode fica HORIZONTAL-RIGIDO (tenso). Bracos se CONTRAEM mais (biceps inflam 2px — ficam MAIORES com raiva). Toga estica VIOLENTAMENTE nos biceps — mais uma costura estoura (gap novo). Carimbo na mao BRILHA mais vermelho (esquenta de raiva). Linhas de choque ao redor do corpo (4 linhas brancas, 3px cada).
- **Notas**: A reacao ao hit e FICAR MAIS FORTE. A muralha nao cede — se reforaca.

### Frame 1: Recomposicao Furiosa
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Dino volta a posicao original MAS agora esta MAIS INTIMIDADOR. Olhos semicerrados MAIS apertados que o idle normal (raiva amplificada). Bigode treme com intensidade DOBRADA (2px de oscilacao em vez de 1px). Bracos permanecem inflados (nao voltam ao tamanho normal — ficam 2px maiores permanentemente durante a raiva). Uma veia nova aparece na testa (2px de linha escura). Carimbo tem uma AURA vermelha (2px de glow vermelho translucido ao redor). O chao sob os pes tem micro-rachaduras novas (peso da raiva).
- **Notas**: Pos-hit, Dino e PIOR do que antes. O jogador bateu na muralha e a muralha ficou com raiva.

**Resumo Hit Sheet**:

| Frame | Nome                  | Posicao   | Descricao curta                      |
|-------|-----------------------|-----------|--------------------------------------|
| 0     | impacto_recebido      | 0-63      | Flash branco, olhos abrem, raiva     |
| 1     | recomposicao_furiosa  | 64-127    | Volta MAIS forte, bracos inflados    |

---

## SPECIAL 1: BLOQUEIO ORCAMENTARIO — 4 Frames (256x64px)

**Conceito**: Dino CARIMBA O AR e pilhas de dinheiro/recursos CONGELAM. Numeros param. Inimigos congelam por 3 segundos. E um congelamento BUROCRATICO — nao e gelo magico, e BUROCRACIA tao densa que paralisa a realidade.

### Frame 0: Preparacao do Bloqueio
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Dino ergue o carimbo com UMA mao (direita). Braco esquerdo segura uma pilha de documentos no ar (papeis flutuando em arco). Olhos focados, concentrados. Bigode reto. Aura azul-gelada comeca a emanar do carimbo (3-4px de glow azul #A0D8EF ao redor). Particulas de numeros aparecem flutuando ao redor (2-3 numeros de 1-2px: "R$", "0", "%" — representando orcamento).
- **Notas**: Buildup. A burocracia esta se acumulando antes do golpe.

### Frame 1: Carimba o Ar
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Dino CARIMBA O AR. Braco direito desce e bate o carimbo no NADA (no meio do frame, sem superficie). Onda de choque AZUL-GELADA irradia do ponto de carimbo (6 linhas azuis irradiando, 10px cada). A marca "NEGADO" aparece FLUTUANDO no ar em azul-gelado (nao vermelho — esta congelada). Documentos na mao esquerda CONGELAM (ficam com borda azul, rigidos). Numeros flutuantes PARAM (congelam no lugar com cristais de gelo).
- **Notas**: A carimbada no ar e a piada visual. Ele carimba o PROPRIO ORCAMENTO.

### Frame 2: Propagacao do Congelamento
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Onda de congelamento se EXPANDE (alcanca as bordas do frame). Tudo no frame tem tonalidade azul-gelada. O chao mostra uma camada de "gelo burocratico" — papeis congelados no chao, moedas paralisadas, numeros rigidos. Dino no centro, INABALADO (nao e afetado pelo proprio bloqueio). Aura azul ao redor dele funciona como escudo. Carimbo com cristais de gelo na base (congelou de tao frio o bloqueio).
- **Notas**: Este frame representa o EFEITO — tudo congelou. Inimigos atingidos congelam por 3s.

### Frame 3: Bloqueio Estabelecido
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Dino volta a postura de muralha (bracos cruzados). Ao redor dele, o ambiente permanece congelado (tonalidade azul). Documentos flutuam congelados no ar. Numeros parados. Uma placa burocratica aparece flutuando acima de Dino: "BLOQUEADO" em azul (#A0D8EF). Careca sem brilho (reflexo esta azulado agora). Bigode tem cristais de gelo nas pontas (micro-detalhe comico). Satisfacao no rosto.
- **Notas**: Estado final. O bloqueio esta ativo. Nada se move. A burocracia venceu.

---

## SPECIAL 2: LIMINAR DIVINA — 6 Frames (384x64px)

**Conceito**: Dino bate o carimbo no chao e um MURO BUROCRATICO CRESCE do chao. Barreira vermelha INTRANSPONIVEL com "NEGADO" estampado. Dura 5 segundos. NINGUEM passa — nem aliados, nem inimigos. E uma LIMINAR fisicalizada.

### Frame 0: Invocacao Judicial
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Dino segura o carimbo com DUAS maos acima da cabeca. Bracos TOTALMENTE esticados, veias pulsando. Olhos ARREGALADOS (brilho vermelho nos olhos — unico special com isso). Uma aura vermelha INTENSA emana do carimbo (5px de glow vermelho). Papeis de processo judicial giram ao redor dele em espiral (6-8 papeis em orbita). O ar treme (linhas de distorcao ao redor do corpo).
- **Notas**: Momento EPICO. Dino esta invocando o poder MAXIMO da burocracia judicial.

### Frame 1: Carimba o Chao
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: IMPACTO SUPREMO. Carimbo BATE no chao com ambas as maos. Onda de choque VERMELHA (mais intensa que o ataque normal). Marca "NEGADO" no chao e COLOSSAL (24x12px, ocupa quase metade do frame). RACHADURA VERMELHA se abre no chao partindo da marca (linha vermelha brilhante que se estende para os lados). Papeis em orbita explodem para fora. Dino agachado pelo impacto, musculos maximos, toga rasga nos dois ombros.
- **Notas**: O impacto e BIBLICO. E uma liminar DIVINA, nao terrestre.

### Frame 2: Muro Comeca a Crescer
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Da rachadura vermelha no chao, um MURO comeca a CRESCER. O muro e feito de DOCUMENTOS COMPACTADOS — papeis prensados, carimbos, selos, assinaturas. Cor predominante: vermelho escuro (#8B0000) com textos brancos de "NEGADO" repetidos. O muro esta na altura da cintura de Dino (crescendo). Dino se levanta atras do muro, bracos abrindo como quem apresenta uma obra de arte. Particulas de papel voam para cima (muro em construcao).
- **Notas**: O muro e BUROCRATICO, nao magico. E feito de DOCUMENTOS. Processos, liminares, despachos.

### Frame 3: Muro na Metade
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Muro na altura do peito de Dino. Mais detalhado agora: selos de cera visiveis, carimbos "NEGADO" multiplos, textos de processos judiciais (ilegivel, mas presente). Cor vermelha com tonalidades (gradiente #CC0000 a #8B0000). Dino atras do muro, bracos cruzados, expressao de PODER ABSOLUTO. Apenas cabeca e ombros visiveis acima do muro. Papeis ainda subindo nas laterais (construcao).
- **Notas**: O muro esta se solidificando. Ja e intransponivel.

### Frame 4: Muro Completo
- **Posicao no sheet**: 256,0 a 319,63
- **Descricao**: MURO COMPLETO. Ocupa 2/3 do frame horizontalmente, altura total do frame (64px). Feito de documentos prensados em tons vermelhos. No centro do muro, um carimbo "NEGADO" ENORME em branco (16x8px). Nas laterais, selos de cera, assinaturas, numeros de processo. Dino INVISIVEL atras do muro (so a careca brilha por cima, ACIMA do muro — detalhe comico). Brilho vermelho emana do muro (aura de 3px). O chao dos dois lados do muro esta rachado.
- **Notas**: O muro e o PERSONAGEM agora. Dino sumiu atras dele. A careca brilhando por cima e a piada.

### Frame 5: Muro Ativo (Loop)
- **Posicao no sheet**: 320,0 a 383,63
- **Descricao**: Muro completo com PULSACAO. Identico ao Frame 4 MAS: o "NEGADO" central PULSA (brilho vermelho que aumenta e diminui). Particulas de papel flutuam ao redor do muro (4-5 papeis orbitando lentamente). A careca de Dino por cima do muro se move 1px esq-dir (esta patrulhando atras da muralha). Micro-rachaduras aparecem nas bordas do muro (sugerindo que vai cair quando o tempo acabar — 5s).
- **Notas**: Frame de loop enquanto o muro esta ativo. Pulsa como se fosse vivo.

---

## SPECIAL 3: MURALHA BUROCRATICA (Passiva) — 4 Frames (256x64px)

**Conceito**: Dino cruza os bracos, as costas EXPANDEM, e ele vira LITERALMENTE uma parede. Nao e uma skill ativada — e o estado PADRAO quando Dino quer bloquear passagem. Os bracos se fundem com o tronco e ele vira um BLOCO SOLIDO.

### Frame 0: Preparacao de Expansao
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Dino inspira PROFUNDAMENTE. Peito infla (tronco expande 4px horizontal). Bracos se abrem para os lados (pose de T). Toga ESTICA ao maximo — botoes remanescentes voam (2-3 botoes projeteis). Olhos fecham em concentracao. Bigode aponta para cima (inspiracao). Carimbo na mao direita em posicao vertical (como escudo). As costas (vistas da frente como largura do tronco) comecam a CRESCER.
- **Notas**: Buildup da transformacao. O corpo esta se expandindo.

### Frame 1: Expansao Lateral
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: As costas/tronco se expandem DRASTICAMENTE. Dino agora ocupa 80% da largura do frame (51px de largura). Bracos se fundem visualmente com o tronco — nao ha mais separacao clara entre braco e corpo. Tudo e UMA MURALHA. A toga rasgou COMPLETAMENTE nos bracos (sobrou so a parte central do peito). Textura do corpo muda: da pele normal para algo que parece CONCRETO (pixels cinza-bege com rachaduras, como muro de predio). Careca permanece no topo (unica parte ainda "humana"). Bigode fica horizontal, rigido como barra de ferro.
- **Notas**: A TRANSFORMACAO. De homem para MURO. A transicao de pele para concreto e GRADUAL.

### Frame 2: Muralha Formada
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: MURALHA COMPLETA. Dino e agora um BLOCO RETANGULAR que ocupa quase todo o frame (56x50px). Textura de MURO DE CONCRETO burocratico — cinza-bege com manchas, rachaduras decorativas, ate um grafite de "NEGADO" em vermelho. No topo do bloco, a careca de Dino aparece (com brilho) e o bigode. Os olhos estao ABERTOS, vigiando. Onde os bracos estavam, agora sao PILASTRAS laterais do muro. O carimbo esta INCRUSTADO no muro (metade para dentro, metade para fora — como decoracao). Na base do muro, os sapatos pretos ainda sao visiveis (detalhe comico — pe de muro).
- **Notas**: E um MURO COM ROSTO. Sapatos embaixo. Careca em cima. O resto e concreto.

### Frame 3: Muralha Ativa (Loop)
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Muralha identica ao Frame 2 MAS com sinais de vida: olhos se movem 1px (patrulhando), bigode treme, uma pequena nuvem de poeira sai de uma rachadura (2px cinza). O "NEGADO" incrustado no muro PULSA em vermelho. Os sapatos batem no chao alternadamente (micro-animacao de impaciencia). Uma placa aparece no topo do muro ao lado da careca: "PASSAGEM BLOQUEADA — ORDEM JUDICIAL". Particulas de cimento caem (2-3px cinza descendo).
- **Notas**: O muro esta vivo. Impaciente. Quer NEGAR mais. Os sapatos batendo de impaciencia sao ouro comico.

---

## Phaser 3 Atlas Keys

```javascript
// Sprite sheet loading
this.load.spritesheet('boss_dino_idle', 'assets/personagens/flavio-dino/sprites/dino_idle.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('boss_dino_walk', 'assets/personagens/flavio-dino/sprites/dino_walk.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('boss_dino_attack', 'assets/personagens/flavio-dino/sprites/dino_attack.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('boss_dino_death', 'assets/personagens/flavio-dino/sprites/dino_death.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('boss_dino_hit', 'assets/personagens/flavio-dino/sprites/dino_hit.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('boss_dino_bloqueio', 'assets/personagens/flavio-dino/sprites/dino_bloqueio.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('boss_dino_liminar', 'assets/personagens/flavio-dino/sprites/dino_liminar.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('boss_dino_muralha', 'assets/personagens/flavio-dino/sprites/dino_muralha.png', {
    frameWidth: 64,
    frameHeight: 64
});
```

---

## Sprite Sheets Resumo Final

| Animacao              | Arquivo                | Frames | Sheet Size  |
|-----------------------|------------------------|--------|-------------|
| Idle                  | `dino_idle.png`        | 4      | 256x64px    |
| Walk                  | `dino_walk.png`        | 6      | 384x64px    |
| Attack                | `dino_attack.png`      | 3      | 192x64px    |
| Death                 | `dino_death.png`       | 4      | 256x64px    |
| Hit                   | `dino_hit.png`         | 2      | 128x64px    |
| Bloqueio Orcamentario | `dino_bloqueio.png`    | 4      | 256x64px    |
| Liminar Divina        | `dino_liminar.png`     | 6      | 384x64px    |
| Muralha Burocratica   | `dino_muralha.png`     | 4      | 256x64px    |
| **TOTAL**             |                        | **33** |             |

---

## Notas para o Artista

1. **Dino e uma MURALHA, nao um homem.** Mesmo no idle, ele deve parecer IMOVIVEL, SOLIDO, IMPENETRAVEL.
2. **Os bracos sao TUDO.** A deformidade principal e os bracos enormes. Eles devem ser MAIORES que a cabeca. Sempre.
3. **O carimbo "NEGADO" e VERMELHO ALARME.** Nao vermelho escuro, nao carmesim. VERMELHO BERRANTE (#CC0000).
4. **A toga esta SEMPRE apertada demais.** Costuras estourando, botoes voando, tecido esticado. A toga sofre.
5. **O bigode TREME.** Em todo frame, o bigode tem micro-variacao. E o indicador de vida/negacao.
6. **Contornos GROSSOS e IRREGULARES** (2px minimo, estilo Robert Crumb). Nada limpo, nada simetrico.
7. **Sombras PESADAS.** Dino e volumoso. A sombra no chao e GRANDE.
8. **Cada passo TREME.** O peso do personagem deve ser transmitido visualmente.
9. **Papeis de emenda sao ONIPRESENTES.** Flutuam ao redor dele, caem, sao carimbados. Sao parte da atmosfera.
10. **A morte e uma RUINA.** Nao e um corpo caindo. E uma muralha desmoronando. Escombros de burocracia.
