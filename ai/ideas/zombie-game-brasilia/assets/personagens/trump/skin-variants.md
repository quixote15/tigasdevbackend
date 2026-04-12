# TRAMPI (Trump) - Variantes de Skin

## Boss Internacional - "Zumbis de Brasilia"

---

## Visao Geral das Skins

| #  | Nome                | Desbloqueio                                    | Raridade  |
|----|---------------------|------------------------------------------------|-----------|
| 1  | Golden Emperor      | Skin padrao (disponivel desde o inicio)        | Comum     |
| 2  | Golf Course         | Derrotar Trampi sem levar dano                 | Raro      |
| 3  | Prison Orange       | Completar o jogo no modo dificil               | Epico     |
| 4  | MAGA Rally          | Coletar 100 bandeiras americanas no ultimate   | Raro      |
| 5  | Impeached           | Derrotar Trampi 10 vezes                       | Epico     |
| 6  | Zombie-Trump        | Modo especial "Infeccao Total"                 | Lendario  |

---

## SKIN 1: GOLDEN EMPEROR (Padrao)

### Descricao Narrativa
O Trampi na sua forma "presidencial" -- ou seja, o absurdo encarnado. Terno dourado cafona, pele laranja NEON, cabelo-ninho de passarinho, gravata vermelha ate o joelho, maos MICROSCOPICAS. Esta e a versao que o mundo conhece. Esta e a versao que o mundo teme. Nao porque e poderoso, mas porque e REAL.

### Paleta de Cores
| Elemento              | Hex       | Notas                                    |
|-----------------------|-----------|------------------------------------------|
| Pele                  | `#FF6B00` | Laranja NEON fluorescente                |
| Pele Glow             | `#FFAA33` | Glow emissivo 1px ao redor              |
| Cabelo                | `#FF8C00` | Laranja algodao-doce mutante            |
| Terno                 | `#DAA520` | Dourado cafona (goldenrod)              |
| Terno Brilho          | `#FFD700` | Pontos de destaque metalico             |
| Gravata               | `#CC0000` | Vermelho sangue                          |
| Camisa                | `#F5F5DC` | Branco sujo (beige)                     |
| Sapatos               | `#1A1A1A` | Preto social brilhante                  |

### Detalhes Visuais Especificos
- Terno brilha com 4-6 sparkles (1px, aleatorios, piscam a cada 800ms)
- Glow da pele pulsa em ciclo sine de 2 segundos (30%-50% opacity)
- Cabelo tem 2-3 fios escapando permanentemente
- Gravata balanca com cada movimento (pendulo fisico)
- Botoes do terno dourados (2px cada, 3 botoes na frente)
- Ombros do terno 4px mais largos que o corpo real (oversized)
- Maos microscopicas: 3x3px, laranja neon com glow proprio

### Sprite Sheet Adicional
Nenhum -- usa os sprite sheets base.

---

## SKIN 2: GOLF COURSE ("Trampi no Campo")

### Descricao Narrativa
Trampi no seu habitat natural: o campo de golfe. Enquanto o mundo pega fogo, ele esta no buraco 7 tentando um eagle. Polo branca com gola levantada ("pop the collar"), bermuda caqui ate o joelho, tenis brancos imaculados (os unicos brancos no outfit inteiro -- tudo mais esta sujo de grama), viseira vermelha com "MAGA" escrito em fonte Comic Sans irregular. O taco de golfe e permanente nesta skin -- esta sempre na mao (ou tentando estar, com as maos microscopicas).

### Paleta de Cores
| Elemento              | Hex       | Notas                                    |
|-----------------------|-----------|------------------------------------------|
| Pele                  | `#FF6B00` | Igual (laranja neon NUNCA muda)          |
| Pele Glow             | `#FFAA33` | Igual                                    |
| Cabelo                | `#FF8C00` | Visivel sob a viseira, mais achatado     |
| Polo                  | `#F5F5F5` | Branca com colarinho levantado           |
| Polo Manchas Grama    | `#556B2F` | 2-3 manchas de grama na barriga         |
| Bermuda               | `#C3B091` | Caqui/khaki                              |
| Viseira               | `#CC0000` | Vermelha com texto "MAGA"                |
| Texto MAGA            | `#FFFFFF` | Branco, Comic Sans irregular, 2px       |
| Tenis                 | `#F0F0F0` | Brancos (ironicamente limpos)            |
| Meia Alta             | `#FFFFFF` | Meias brancas compridas (ate o joelho)   |
| Taco de Golfe         | `#DAA520` | Dourado, sempre presente                 |

### Detalhes Visuais Especificos
- Viseira MAGA substitui o cabelo-ninho no topo, mas o cabelo SAI por baixo da viseira em todas as direcoes (mais ridiculo que sem viseira)
- Polo com gola POP (levantada, 2px de colarinho vertical) -- tentativa de parecer cool
- Bermuda caqui com vinco perfeito (1px de highlight vertical na frente de cada perna)
- Manchas de grama na polo (ele caiu no campo pelo menos 1 vez)
- Meias brancas ALTAS -- mid-calf, visiveis entre bermuda e tenis
- Taco de golfe permanente na mao direita microscopica (sempre escorregando)
- Sem gravata (substituida pelo colarinho levantado)
- Maos microscopicas IDENTICAS em tamanho -- nao mudam entre skins

### Mudancas de Animacao
- **Idle**: Pratica swing de golfe em loop (wind-up -> swing -> olha ao longe com mao microscopica na testa como "viseira")
- **Walk**: Anda como se estivesse no green -- passos mais leves, taco apoiado no ombro
- **Attack**: IDENTICO ao padrao (taco de golfe ja esta na mao)
- **Death**: Viseira voa (particula extra), cai no "bunker" (sprite de areia aparece embaixo)
- **Hit**: Viseira entorta (gira 15deg), depois volta ao lugar

### Sprite Sheet Adicional
`trump_skin_golf.png` -- mesmas dimensoes dos sheets base, redesenhado com o outfit

---

## SKIN 3: PRISON ORANGE ("Laranja sobre Laranja")

### Descricao Narrativa
A IRONIA SUPREMA: Trampi de uniforme prisional laranja. O problema? A pele dele JA E LARANJA. O uniforme se CONFUNDE com a pele. A primeira vista, parece que ele esta nu e laranja (o que e perturbador). So olhando de perto voce ve a diferenca sutil entre o laranja da pele (#FF6B00) e o laranja do uniforme (#FF8C00). Numero de prisioneiro estampado no peito: "45-47" em preto. Algemas nos pulsos -- mas sao MAIORES que as maos microscopicas, entao escorregam constantemente.

### Paleta de Cores
| Elemento              | Hex       | Notas                                    |
|-----------------------|-----------|------------------------------------------|
| Pele                  | `#FF6B00` | Laranja NEON (identico)                  |
| Pele Glow             | `#FFAA33` | Glow identico                            |
| Uniforme              | `#FF8C00` | Laranja LEVEMENTE diferente da pele      |
| Uniforme Shadow       | `#CC6600` | Sombras do uniforme                      |
| Numero "45-47"        | `#1A1A1A` | Preto, peito esquerdo, 3px altura        |
| Cabelo                | `#FF8C00` | Mais desgrenhado (sem gel/spray)         |
| Algemas               | `#808080` | Cinza metalico                           |
| Algemas Brilho        | `#C0C0C0` | Highlights metalicos                     |
| Chinelos Prisao       | `#FF6600` | Laranja (sim, MAIS laranja)              |
| Corrente              | `#696969` | Elos entre algemas                       |

### Detalhes Visuais Especificos
- O PONTO COMICO: A pele e o uniforme sao QUASE a mesma cor. Parece nu a distancia.
- Diferenciar com: linhas do uniforme (costuras em 1px #CC6600), numero do prisioneiro, e textura (uniforme tem textura de tecido grosso, pele tem glow)
- Algemas nos pulsos SAO MAIORES que as maos (algemas 5x3px, maos 3x3px). As maos PASSAM PELAS ALGEMAS sem problemas. As algemas escorregam. Inutil.
- Corrente entre algemas: 12px de comprimento, pende quando as maos estao paradas
- Cabelo mais desgrenhado que o normal: sem produto, fios para todos os lados, 20px de largura (maior que o padrao porque nao tem manutencao)
- Sem gravata, sem terno, sem luxo. Uniforme prison jumpsuit de uma peca.
- Chinelos de prisao laranja nos pes (MAIS laranja se misturando)
- Expressao: entre indignacao ("isso e INJUSTO") e falsa confianca ("vou sair em 5 minutos")

### Mudancas de Animacao
- **Idle**: Tenta cruzar os bracos mas as algemas atrapalham. Corrente balanca. Olha ao redor nervosamente (olhos se movem, cabeca nao).
- **Walk**: Arrastar de pe (chinelos de prisao). Corrente tine. Passo mais curto (restringido).
- **Attack**: Usa a CORRENTE como arma (swing da corrente), maos microscopicas seguram nada -- a corrente balanca por momento angular puro.
- **Death**: Algemas finalmente CAEM porque as maos sao pequenas demais para segura-las. Ironia: as algemas nunca prenderam nada.
- **Hit**: Corrente balanca descontrolada. Algemas batem no rosto. Auto-dano comico.

### Sprite Sheet Adicional
`trump_skin_prison.png`

---

## SKIN 4: MAGA RALLY ("Comicio de Trampi")

### Descricao Narrativa
Trampi como aparece nos comicios -- a versao "homem do povo" (de povo ele nao tem NADA). Bone vermelho MAGA (maior que o normal, quase cobrindo os olhos), terno escuro "casual" (paletó aberto, sem gravata), camisa branca com os 2 botoes de cima abertos (revelando pele laranja do pescoco), calca social preta, sapatos de plataforma (3px de sola extra -- ele MENTE sobre a altura). Segura um microfone com a mao microscopica (mal segura, obvio). Na outra mao, tenta acenar para a multidao.

### Paleta de Cores
| Elemento              | Hex       | Notas                                    |
|-----------------------|-----------|------------------------------------------|
| Pele                  | `#FF6B00` | Laranja NEON (identico)                  |
| Pele Glow             | `#FFAA33` | Glow identico                            |
| Bone MAGA             | `#CC0000` | Vermelho escuro, texto branco            |
| Texto "MAGA"          | `#FFFFFF` | Fonte serif irregular, 2px              |
| Paleto                | `#2C2C2C` | Escuro, nao preto (grafite)             |
| Paleto Lapela         | `#3A3A3A` | Highlight nas lapelas                    |
| Camisa                | `#F5F5DC` | Branca suja, colarinho aberto           |
| Calca                 | `#1A1A1A` | Preta social                             |
| Sapato Plataforma     | `#1A1A1A` | Preto, 3px de sola extra (mentira)      |
| Microfone             | `#333333` | Corpo preto com cabeca prateada          |
| Microfone Cabeca      | `#C0C0C0` | Prata, esfera 3x3px                     |
| Pin Bandeira          | `#FF0000` / `#0000FF` / `#FFFFFF` | Pin na lapela, 2x2px  |
| Cabelo                | `#FF8C00` | Saindo pelas bordas do bone              |

### Detalhes Visuais Especificos
- Bone MAGA e GRANDE (14px de largura, 6px de altura) -- quase cobre os olhos apertados
- Cabelo escapa por baixo do bone em TODAS as direcoes (mais que na versao golf)
- Paleto aberto: nenhum botao fechado, lapelas largas, ombros oversized
- Camisa com 2 botoes abertos: area triangular de pele laranja visivel no peito (3x4px de skin, glow visivel)
- Pin de bandeira americana na lapela esquerda (2x2px, vermelho-azul-branco)
- Microfone na mao direita: mao microscopica mal alcanca a empunhadura. O microfone esta TORTO.
- Sapatos de plataforma: 3px de sola extra (sola visivelmente desproporcional). ELE MENTE SOBRE ALTURA.
- Sem gravata. A ausencia de gravata faz o peito parecer MAIS largo (intimidacao casual)

### Mudancas de Animacao
- **Idle**: Fala no microfone (boca abre e fecha em loop). Mao esquerda microscopica tenta gesticular (gesto "pinch" impossivel). Aceno ocasional.
- **Walk**: Anda "cumprimentando apoiadores imaginarios" -- vira para cada lado a cada 2 passos, acenar com mao livre
- **Attack**: USA O MICROFONE COMO ARMA. Swing com microfone. Texto de impacto: "TREMENDOUS!" via microfone (eco)
- **Death**: Microfone faz feedback (particula sonora visual: circulos de "EEEE"). Bone MAGA voa. Cai do "palco" (sprite cai 8px extra).
- **Hit**: Bone entorta. Microfone cai (hand_grab_fail). Feedback de microfone como dano visual extra.

### Sprite Sheet Adicional
`trump_skin_maga.png`

---

## SKIN 5: IMPEACHED ("O Presidente Impichado")

### Descricao Narrativa
O Trampi APOS o impeachment. Tudo deu errado. O terno esta amassado, a gravata frouxa e torta, o cabelo DESMORONANDO (metade do ninho caiu), um olho inchado (como se tivesse levado um soco institucional), manchas de ketchup MAIS EVIDENTES na camisa, sapatos desamarrados. A expressao base nao e mais arrogancia -- e RAIVA DESESPERADA. As maos microscopicas tremem constantemente. O glow da pele esta IRREGULAR (pulsando de forma erratica, como se o autobronzeador estivesse falhando).

### Paleta de Cores
| Elemento              | Hex       | Notas                                    |
|-----------------------|-----------|------------------------------------------|
| Pele                  | `#FF6B00` | Laranja neon MAS com patches de palido   |
| Pele Patches          | `#CC9966` | Areas onde bronzeador falhou (2-3 patches)|
| Pele Glow             | `#FFAA33` | ERRATICO (pulsa irregularmente)          |
| Cabelo Remanescente   | `#FF8C00` | Metade do ninho, desgrenhado             |
| Cabelo Faltante       | `#FFB6C1` | Careca rosada visivel (40% do topo)      |
| Terno Amassado        | `#B8960B` | Dourado mais escuro/sujo que o padrao    |
| Terno Vincos          | `#8B6508` | Linhas de amassado profundas             |
| Gravata Frouxa        | `#AA0000` | Vermelho desbotado, torta 15deg          |
| Camisa Suja           | `#E8E0C8` | Branco-sujo com manchas                  |
| Ketchup               | `#CC0000` | 4-5 manchas na camisa (mais que o padrao)|
| Olho Inchado          | `#8B668B` | Roxo-inchado ao redor do olho esquerdo   |
| Sapato Desamarrado    | `#1A1A1A` | Cadarco solto (1px serpentina no chao)   |

### Detalhes Visuais Especificos
- CABELO METADE CAIDO: O lado esquerdo do ninho esta intacto (9px). O lado direito DESMORONOU -- fios caidos, careca visivel (#FFB6C1, area de 5x3px). O penteado e assimetrico e tragico.
- PELE COM PATCHES: 2-3 areas de 2x2px no rosto onde o bronzeador falhou. Pele real visivel: palida (#CC9966). Cria um efeito de "maquiagem derretendo".
- GLOW ERRATICO: Em vez de pulsar suavemente (sine wave), o glow pulsa IRREGULARMENTE: 30% -> 70% -> 20% -> 50% -> 10% -> 60%... aleatorio, assincrono. Como um neon piscando.
- TERNO AMASSADO: 5-6 linhas de vinco profundas (1px, #8B6508) no torso. Ombro esquerdo caido 2px. Botao do meio faltando (buraco).
- GRAVATA TORTA: Rotacionada 15deg no sentido horario, no frouxamente amarrada, pende mais de um lado.
- OLHO INCHADO: Olho esquerdo cercado por area roxa (#8B668B, 4x3px). O olho em si esta semi-fechado (1px de abertura vs 2px do direito).
- KETCHUP AUMENTADO: 5 manchas (vs 3 na death animation padrao). Na gola, peito, barriga, manga, e uma no ROSTO.
- CADARCOS SOLTOS: 1px de linha serpenteando ao redor de cada sapato no chao.
- MAOS TREMEM: hand_tremble CONSTANTE. Nunca param de tremer nesta skin.

### Mudancas de Animacao
- **Idle**: Maos tremem sem parar. Olha ao redor paranóico (olhos se movem rapidamente). Tenta arrumar o cabelo com mao microscopica (FALHA -- pior que antes). Gravata balanca irregularmente.
- **Walk**: Tropeca a cada 3 passos (cadarco). Manca levemente do pe esquerdo. Terno desamassa e amassa de novo com cada passo.
- **Attack**: MAIS DESESPERADO. Swing mais rapido mas menos preciso. 30% de chance de auto-fumble (taco escapa da mao e precisa recuperar). Grita mais alto.
- **Death**: REDUNDANTE -- ele ja parece derrotado. A death animation simplesmente o faz SENTAR no chao e chorar (maos microscopicas nos olhos). Sem drama. So patetismo.
- **Hit**: Glow da pele faz SHORT-CIRCUIT (flash erratico 100ms). Cabelo perde mais 1 fio (cumulativo durante a luta). Ao levar 5 hits, fica praticamente careca.

### Mecanica Especial da Skin
- PERDA CUMULATIVA DE CABELO: A cada hit, 1 fio de cabelo se solta como particula. Apos 5 hits, o cabelo-ninho esta em 50% do tamanho. Apos 10 hits, praticamente careca. Nao regenera durante a luta.

### Sprite Sheet Adicional
`trump_skin_impeached.png`

---

## SKIN 6: ZOMBIE-TRUMP ("Zumbi Laranja")

### Descricao Narrativa
A versao FINAL. Trampi foi infectado pelo virus zumbi de Brasilia. A pele laranja NEON agora e laranja PODRE -- como uma tangerina esquecida no sol por 3 semanas. O terno dourado esta rasgado e manchado de verde-vomito. O cabelo-ninho tem MOFO crescendo (patches verdes). Metade do rosto esta decomposto (cranio visivel do lado direito). Um olho saltou da orbita e pende pelo nervo optico (1px de fio). A gravata se fundiu com o peito (esta DENTRO da carne). As maos microscopicas estao AINDA MAIS microscopicas -- os dedos cairam, restam apenas stumps. Mas o pior: ELE AINDA FALA. "TREMENDOUS..." mas com voz de zumbi gargling.

### Paleta de Cores
| Elemento              | Hex       | Notas                                    |
|-----------------------|-----------|------------------------------------------|
| Pele Zumbi            | `#996633` | Laranja PODRE (marrom-esverdeado)        |
| Pele Necrose          | `#556B2F` | Verde de decomposicao                    |
| Pele Glow (residual)  | `#CC8833` | Glow fraco, intermitente, DOENTIO       |
| Cranio Exposto        | `#E8DCC8` | Osso amarelado no lado direito do rosto  |
| Cabelo + Mofo         | `#8B7500` | Laranja escurecido com patches verdes    |
| Mofo no Cabelo        | `#2E8B57` | Patches de mofo (3-4 areas de 2x2px)    |
| Terno Rasgado         | `#8B7500` | Dourado sujo/enferrujado                 |
| Terno Rasgos          | `#556B2F` | Buracos revelando carne zumbi           |
| Gravata Fundida       | `#660000` | Vermelho escuro, parcialmente DENTRO do peito |
| Olho Pendente         | `#FF6B00` | O olho ainda e laranja neon (ironico)    |
| Nervo Optico          | `#CC3333` | Fio de 1px conectando olho a orbita      |
| Orbita Vazia          | `#1A1A1A` | Buraco negro onde o olho era             |
| Baba Zumbi            | `#9ACD32` | Verde-amarelado, escorrendo da boca      |
| Stumps de Maos        | `#996633` | Cotos onde dedos eram (2x2px, sem dedos) |
| Sangue Seco           | `#8B0000` | Manchas escuras no terno e rosto         |

### Detalhes Visuais Especificos
- PELE PODRE: A pele laranja neon se transformou. Ainda tem RESIDUOS de laranja fluorescente em patches (3-4 areas de 2x2px onde o autobronzeador resistiu ao apodrecimento). O resto e marrom-esverdeado de decomposicao. O contraste entre os patches neon e a podridao e REVOLTANTE.
- GLOW MORIBUNDO: O glow da pele agora e fraco (#CC8833, 10-20% opacity), intermitente (pisca a cada 1.5s por 200ms, depois apaga), e limitado aos patches onde a pele laranja sobreviveu.
- CRANIO VISIVEL: Lado direito do rosto, area de 5x4px. O osso amarelado (#E8DCC8) com linhas de sutura cranianas visiveis (1px, #999999). A carne ao redor esta rasgada com bordas irregulares (#996633 para #E8DCC8 transicao abrupta).
- OLHO PENDENTE: O olho direito saiu da orbita. Pende por 1px de "nervo optico" (#CC3333) ate o nivel do queixo. O olho em si AINDA E LARANJA NEON (#FF6B00) -- a unica parte que mantem a cor original. Ironico. O olho pisca ocasionalmente (sim, funciona).
- CABELO COM MOFO: O ninho ainda existe, mas com 3-4 patches de mofo verde (#2E8B57). Alguns fios estao quebradiços (caem em particulas mais facilmente). O volume e 70% do original.
- TERNO RASGADO: 4-5 rasgos no terno (buracos de 2x3px) revelando carne zumbi embaixo (#996633 com textura de linhas verticais irregulares). O brilho dourado e FERRUGEM agora.
- GRAVATA FUNDIDA: A gravata vermelha esta parcialmente EMBUTIDA no peito. 60% da gravata e visivel, os outros 40% "entram" na carne (transicao de #660000 para #996633 na area do esterno). Parece que a carne cresceu por cima.
- MAOS STUMP: As maos microscopicas perderam os dedos. Agora sao COTOS de 2x2px. Sem nenhuma funcionalidade de garra. Pior que antes (se isso e possivel).
- BABA ZUMBI: Fio de 1px de baba verde-amarelada (#9ACD32) escorrendo do canto da boca. Goteja (particula de 1x1px cai a cada 800ms com gravidade).
- SANGUE SECO: 6-8 manchas de sangue seco (#8B0000) espalhadas pelo terno, rosto e maos.

### Mudancas de Animacao
- **Idle**: Oscila como zumbi (corpo balanca 2px esquerda-direita, 1.5s ciclo). Olho pendente balanca como pendulo. Baba goteja. Tenta falar: boca abre e fecha mas so sai gargling. Cabelo mofo solta esporo ocasional (particula verde 1x1px, sobe).
- **Walk**: ARRASTAR CLASSICO DE ZUMBI. Perna direita arrasta. Braco esquerdo estendido a frente (mas com stump, nao com mao). Velocidade 60% do normal. Terno pedacos caem (particula dourada a cada 3 passos).
- **Attack**: Tenta usar o taco de golfe mas os stumps NAO SEGURAM NADA. O taco cai SEMPRE. Em vez disso, ataca com mordida (cabeca avanca, boca aberta mostrando dentes podres). Texto: "TREHHH...MENDOUSSS..." (distorcido).
- **Death**: Corpo se DECOMPOE. Frame a frame, mais carne desaparece revelando osso. No frame final, e so um esqueleto dourado (ossos tingidos de dourado pelo terno) com um tufinho de cabelo alaranjado no craneo.
- **Hit**: Pedacos do corpo SAO ARRANCADOS como particulas (2x2px de carne zumbi). O olho pendente chicoteia violentamente. Baba espirra para os lados.
- **Special**: Build the Wall usa OSSOS e CARNE em vez de tijolos dourados. O muro e organico, pulsa, e tem olhos. "TRUMP" escrito em sangue seco.

### Mecanica Especial da Skin
- DECOMPOSICAO PROGRESSIVA: Ao longo da luta, o Zombie-Trump vai perdendo pedacos. A cada 15 segundos, 1 novo rasgo aparece no sprite. Apos 2 minutos, esta mais osso que carne. Isto NAO afeta gameplay -- e puramente cosmético.
- INFECCAO PASSIVA: Inimigos que Zombie-Trump ataca tem 20% de chance de ficarem "infectados" (tint verde por 3s, slowdown 10%). Espalha a infecção.

### Sprite Sheet Adicional
`trump_skin_zombie.png` + `trump_zombie_particles.png` (sheet de particulas de decomposicao, 10 frames de 8x8px)

---

## Notas Gerais para Todas as Skins

### Elementos que NUNCA Mudam
1. **Tamanho das maos**: SEMPRE microscopicas (3x3px ou menos). NENHUMA skin aumenta as maos.
2. **Proporcoes corporais**: 5 cabecas de altura, atarracado. Mesmas proporcoes em todas as skins.
3. **Hitbox**: 40x56px. Nao muda com a skin.
4. **Dimensao do sprite**: 64x64px. Todas as skins cabem no mesmo frame.

### Elementos que SEMPRE Mudam
1. **Paleta de cores**: Cada skin tem paleta propria (tabelas acima).
2. **Cabelo**: Formato e estado mudam por skin (intacto, sob bone, decomposto...).
3. **Expressao base**: Golden Emperor = arrogancia. Golf = despreocupacao. Prison = indignacao. MAGA = populismo. Impeached = desespero. Zombie = fome cerebral.

### Implementacao Tecnica
```javascript
// Estrutura de skins no game code
const TRUMP_SKINS = {
  golden_emperor: {
    sheet: 'trump_default',
    unlock: 'always',
    glowColor: 0xFFAA33,
    glowIntensity: { min: 0.3, max: 0.5 }
  },
  golf_course: {
    sheet: 'trump_skin_golf',
    unlock: 'defeat_trump_no_damage',
    glowColor: 0xFFAA33,
    glowIntensity: { min: 0.3, max: 0.5 }
  },
  prison_orange: {
    sheet: 'trump_skin_prison',
    unlock: 'complete_hard_mode',
    glowColor: 0xFFAA33,
    glowIntensity: { min: 0.3, max: 0.5 },
    specialAnims: { handcuffs: true }
  },
  maga_rally: {
    sheet: 'trump_skin_maga',
    unlock: 'collect_100_flags',
    glowColor: 0xFFAA33,
    glowIntensity: { min: 0.3, max: 0.5 },
    props: ['microphone']
  },
  impeached: {
    sheet: 'trump_skin_impeached',
    unlock: 'defeat_trump_10x',
    glowColor: 0xFFAA33,
    glowIntensity: 'erratic',
    specialMechanics: ['hair_loss_cumulative']
  },
  zombie_trump: {
    sheet: 'trump_skin_zombie',
    unlock: 'infection_total_mode',
    glowColor: 0xCC8833,
    glowIntensity: { min: 0.0, max: 0.2, pattern: 'intermittent' },
    specialMechanics: ['decomposition_progressive', 'passive_infection'],
    particleSheet: 'trump_zombie_particles'
  }
};
```
