# SERGIO MORO (O Heroi Decaido) - Especificacao de Sprites

## NPC / Ex-Aliado que Muda de Lado - "Zumbis de Brasilia"

---

## Especificacoes Tecnicas Gerais

- **Tamanho do sprite**: 64x64px por frame
- **Formato**: PNG com transparencia (RGBA)
- **Perspectiva**: Top-down levemente isometrica (Y-sorting)
- **Sprite sheets**: Horizontais (frames lado a lado)
- **Frame rate alvo**: 10 fps (estilo jerky/twitchy do Andre Guedes)

### IMPORTANTE: 4 Estagios de Degradacao Visual
Cada estagio tem sua propria variante de TODAS as animacoes. Isso pode ser implementado como:
- **Opcao A**: 4 sprite sheets separadas (uma por estagio)
- **Opcao B**: 1 mega sprite sheet com 4 linhas (uma por estagio)
- **Recomendado**: Opcao A para facilitar swap dinamico em runtime

1. **moro-stage1-hero.png** - Heroi da Lava Jato (waves 1-3)
2. **moro-stage2-worn.png** - Desgastado (waves 4-6)
3. **moro-stage3-decadent.png** - Decadente (waves 7-9)
4. **moro-stage4-irrelevant.png** - Irrelevante (waves 10+)

---

## PALETA DE CORES (4 Estagios)

### Estagio 1 - HEROI
| Elemento | Cor | Hex |
|----------|-----|-----|
| Pele | Saudavel, bronzeada | `#D4A574` |
| Cabelo | Castanho escuro, penteado | `#3B2716` |
| Terno (corpo) | Azul marinho impecavel | `#1A237E` |
| Terno (sombras) | Azul escuro | `#0D1542` |
| Camisa | Branco puro | `#FFFFFF` |
| Gravata | Vermelho poder | `#B71C1C` |
| Martelo de juiz | Madeira brilhante + metal cromado | `#8B4513` / `#C0C0C0` |
| Olheiras | Inexistentes | - |
| Ombros | ERETOS, largos | - |
| Contorno | Preto grosso | `#1A1A1A` |

### Estagio 2 - DESGASTADO
| Elemento | Cor | Hex |
|----------|-----|-----|
| Pele | Levemente palida | `#C9A07A` |
| Cabelo | Castanho, leve despenteado | `#3B2716` |
| Terno (corpo) | Azul marinho levemente desbotado | `#283593` |
| Terno (sombras) | Azul medio | `#1A237E` |
| Camisa | Branco amarelado | `#F5F0E0` |
| Gravata | Vermelho escurecido, levemente torta | `#8B1A1A` |
| Martelo de juiz | Madeira com manchas + metal escurecido | `#7A4012` / `#A0A0A0` |
| Olheiras | Leves, marrom-arroxeado | `#7B6080` |
| Ombros | Levemente caidos (5 graus) | - |
| Contorno | Preto grosso | `#1A1A1A` |

### Estagio 3 - DECADENTE
| Elemento | Cor | Hex |
|----------|-----|-----|
| Pele | Palida, acinzentada | `#B8967A` |
| Cabelo | Castanho grisalho, despenteado | `#5A4A3A` |
| Terno (corpo) | Azul desbotado, visivelmente amassado | `#3949AB` |
| Terno (sombras) | Azul acinzentado | `#303F6F` |
| Camisa | Amarelado sujo | `#E8DCC0` |
| Gravata | Vermelha desbotada, frouxa | `#6B1515` |
| Martelo de juiz | Madeira descascando + metal enferrujado | `#6B3810` / `#8B6914` |
| Olheiras | Profundas, roxo escuro | `#4A3050` |
| Ombros | Visivelmente caidos (15 graus) | - |
| Rugas | Linhas extras no rosto | `#8A7060` |
| Contorno | Preto grosso | `#1A1A1A` |

### Estagio 4 - IRRELEVANTE
| Elemento | Cor | Hex |
|----------|-----|-----|
| Pele | Cinza-palida (quase morta) | `#A08870` |
| Cabelo | Grisalho, ralo, desgrenhado | `#7A7A6A` |
| Terno (corpo) | Cinza desbotado (azul sumiu) | `#5C6070` |
| Terno (sombras) | Cinza escuro | `#3D4050` |
| Camisa | Cinza-amarelado, manchado | `#D0C8A8` |
| Gravata | Cor indefinida, quase caindo | `#5A4040` |
| Martelo de juiz | Madeira podre + metal todo enferrujado/quebrado | `#503010` / `#6B4500` |
| Olheiras | ENORMES, quase metade do rosto | `#302030` |
| Ombros | TOTALMENTE caidos (25+ graus) | - |
| Rugas | Multiplas, profundas | `#706050` |
| Transparencia geral | 85% opacidade (ficando invisivel) | - |
| Contorno | Preto grosso | `#1A1A1A` |

---

## ANATOMIA BASE - TODOS OS ESTAGIOS

- **Cabeca**: Formato QUADRADO/ANGULAR (contraste com Taxadd redondo)
- **Queixo**: Proeminente, angular (vai ficando mais CAIDO a cada estagio)
- **Olhos**: Pequenos, penetrantes (vao ficando mais OPACOS)
- **Sobrancelhas**: Grossas, fruncidas (vao ficando mais CAIDAS)
- **Boca**: Linha reta, seria (vai ficando mais CURVADA para baixo)
- **Ombros**: A DEFORMIDADE PRINCIPAL - caem progressivamente
- **Martelo**: Item iconico - degrada junto com o personagem
- **Corpo**: Ereto → curvado progressivamente

---

## ESTAGIO 1: HEROI (Waves 1-3)

### IDLE - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Postura ERETA, peito estufado. Martelo de juiz BRILHANTE apoiado no ombro direito. Queixo ERGUIDO. Olhar determinado para frente. Terno impecavel, sem uma ruga. |
| 2 | Leve movimento do martelo (repousa no ombro). Olhos se movem lateralmente (vigia, alerta). Postura militar. Reflexo de luz no metal do martelo. |
| 3 | Ajusta a gravata com mao livre (gesto de autoridade). Martelo firme no ombro. Expressao inabalavel. |
| 4 | Volta ao frame 1 mas com leve balanco no corpo (respiracao profunda de confianca). Martelo brilha. |

### WALK - 6 frames (384x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Marcha DECIDIDA, pe direito a frente. Martelo no ombro, firme. Postura de quem vai resolver problemas. Passos LARGOS. |
| 2 | Meio passo. Corpo ereto. Martelo levemente balanca. Expressao determinada. |
| 3 | Pe esquerdo a frente. Marcha continua. Terno perfeito, sem deformacao. |
| 4 | Passo firme. Queixo sempre erguido. Olhos fixos a frente. |
| 5 | Ritmo militar. Martelo bate levemente no ombro (tap). |
| 6 | Completa ciclo. Postura impecavel mantida. |

### ATTACK - 3 frames (192x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | ERGUE o martelo acima da cabeca com as duas maos. Olhos ARDENDO. Corpo tenso. Terno esticado pelo movimento. Flash de luz no metal. |
| 2 | DESFERE golpe para frente/baixo com FORCA TOTAL. Arco de luz seguindo o martelo. Impacto visual GRANDE: ondas de choque, cracas no chao. "CONDENADO!" |
| 3 | Pos-golpe. Martelo no chao, postura vitoriosa. Levanta o martelo de volta. Expressao de dever cumprido. |

### DEATH - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Recebe golpe. Expressao de CHOQUE (heroi nao esperava cair). Martelo voa da mao. |
| 2 | Cai de joelhos. FLASHBACK rapido - silhueta do heroi que ele era. Martelo no chao ao lado. |
| 3 | Cai de lado. Terno ainda impecavel mesmo caindo. Expressao de incredulidade. |
| 4 | Deitado. Mao esticada tentando alcançar o martelo. Olhos abertos mas sem vida. Heroi caido. |

### HIT - 2 frames (128x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Recuo breve. SURPRESA no rosto (heroi nao esta acostumado a apanhar). Flash branco. Martelo balanca no ombro. |
| 2 | Recupera RAPIDO. Postura de combate. Martelo pronto. Olhos mais determinados. "Isso nao me derruba." |

### SPECIAL: "Heroi Decaido" (Golpe Maximo Inicial) - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | AURA DOURADA envolve o Moro. Martelo BRILHA intensamente. Pose heroica - bracos abertos, peito estufado. |
| 2 | SALTA levemente. Martelo acima da cabeca com brilho solar. Terno esvoaca como capa de heroi. |
| 3 | DESCEM martelo com forca DEVASTADORA. Crater de impacto. Onda de choque dourada. Dano MAXIMO. |
| 4 | Pousa heroicamente. Particulas douradas se dissipam. Expressao stoica. TEXTO: "Nos tempos da Lava Jato..." |

---

## ESTAGIO 2: DESGASTADO (Waves 4-6)

### Diferencas Visuais do Estagio 1
- Ombros caidos 5 graus
- Olheiras LEVES aparecendo
- Terno com 2-3 RUGAS visiveis
- Martelo com manchas escuras (comecando a perder brilho)
- Gravata levemente torta
- Expressao: de "determinada" para "cansada mas resistindo"

### IDLE - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Postura quase ereta, ombros LEVEMENTE caidos. Martelo no ombro mas pesando mais. Olheiras sutis sob os olhos. Terno com rugas. |
| 2 | SUSPIRO visivel (peito enche e esvazia). Olhos desviam para baixo brevemente. Martelo escorrega 1px no ombro. |
| 3 | Tenta ajustar postura (puxa ombros para cima) mas eles voltam a cair. Gravata torta. |
| 4 | Olhar distante, nostalgico. Acaricia o cabo do martelo. "Eu era respeitado..." (boca move levemente). |

### WALK - 6 frames (384x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Caminhada MENOS decidida. Passos menores. Martelo no ombro mas mais pesado. Ombros caidos. |
| 2 | Leve arrasto no pe. Corpo levemente curvado. |
| 3 | Continua andando. Terno amassando nas dobras. Gravata balanca torta. |
| 4 | Olha para tras brevemente (nostalgia do que era). |
| 5 | Voltam a frente. Suspiro. Martelo reposiciona. |
| 6 | Completa ciclo. Postura pior que o inicio. |

### ATTACK - 3 frames (192x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Ergue martelo com esforco VISIVEL (bracos tremem). Olheiras destacadas. Terno amassa no movimento. |
| 2 | Golpe com forca REDUZIDA (70% do Estagio 1). Arco de luz MENOR, mais opaco. Impacto visual menor. |
| 3 | Pos-golpe. Ofegante. Martelo mais pesado para levantar. Expressao de frustacao. |

### DEATH - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Recebe golpe. Menos surpresa, mais resignacao. Martelo cai pesado. |
| 2 | Cai de joelhos. Olheiras proeminentes. "Eu sabia que isso ia acontecer..." |
| 3 | Cai de lado. Terno amassado se espalha. Martelo rola para longe. |
| 4 | Deitado. Expressao cansada. Nao tenta alcançar o martelo (ja desistiu um pouco). |

### HIT - 2 frames (128x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Recuo mais lento. Menos surpreso, mais "de novo?". Flash branco mais fraco. Ombros caem mais. |
| 2 | Recupera DEVAGAR. Postura reestabelecida mas pior que antes. Martelo quase cai. |

---

## ESTAGIO 3: DECADENTE (Waves 7-9)

### Diferencas Visuais do Estagio 2
- Ombros caidos 15 graus (MUITO visivel)
- Olheiras PROFUNDAS (roxo escuro, cobrindo 30% do rosto)
- Terno AMASSADO com manchas
- Martelo ENFERRUJADO (cor mudou de cromado para marrom-laranja)
- Gravata FROUXA, quase desamarrada
- Cabelo com fios grisalhos visiveis, despenteado
- Rugas no rosto (2-3 linhas extras)
- Expressao: AMARGA, boca curvada para baixo permanentemente

### IDLE - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Postura CURVADA. Ombros CAIDOS visivelmente. Martelo enferrujado arrastando na mao (nao mais no ombro). Olheiras PROFUNDAS. Gravata frouxa. |
| 2 | Cabeca PENDE para frente. Quase cochila. Martelo quase cai da mao. Olhos semi-cerrados de cansaco. |
| 3 | ACORDA com susto leve. Tenta se recompor. Falha. Ombros caem mais. Olha para o martelo com tristeza. |
| 4 | Suspiro PESADO. Corpo todo afunda. "A justica... a justica..." (boca move mas nao completa). Olheiras PULSAM. |

### WALK - 6 frames (384x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | ARRASTA os pes. Martelo arrastando no chao (risco visivel). Corpo curvado. Ombros DESPENCADOS. |
| 2 | Cada passo e um esforco. Terno desajustado completamente. Gravata quase caindo. |
| 3 | TROPECA levemente. Martelo enrosca no chao. Olheiras enormes. |
| 4 | Recupera mas quase cai. Expressao de amargura pura. |
| 5 | Continua arrastando. Olha para o chao. Cabelo desgrenhado. |
| 6 | Completa ciclo. Mais curvado que o inicio. Rastro de ferrugem do martelo no chao. |

### ATTACK - 3 frames (192x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | TENTA erguer martelo. Bracos TREMEM muito. Quase nao consegue levantar acima da cintura. Rosto de esforco extremo. |
| 2 | Golpe FRACO (40% do Estagio 1). Martelo mal sai do chao. Particulas de ferrugem voam do impacto. Impacto visual minimo. |
| 3 | Pos-golpe. EXAUSTO. Apoiado no martelo como bengala. Ofegante. "Isso ja foi mais facil..." |

### DEATH - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Recebe golpe. Quase ALIVIO na expressao. Martelo enferrujado se solta facil. |
| 2 | Cai de joelhos. Nao resiste. Olheiras tomam metade do rosto. "Pelo menos acaba..." |
| 3 | Cai sentado. Martelo quebra em dois ao cair. Pedacos de ferrugem voam. |
| 4 | Deitado de costas. Olhos abertos olhando o teto. Expressao VAZIA. Martelo em pedacos. Peca de ferrugem rola. |

### HIT - 2 frames (128x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Mal reage. Corpo ja tao curvado que o recuo e minimo. Flash branco fraco. Martelo cai da mao. |
| 2 | Pega martelo do chao com esforco visivel. Volta a postura curvada. Sem expressao de revide. Resignacao. |

---

## ESTAGIO 4: IRRELEVANTE (Waves 10+)

### Diferencas Visuais do Estagio 3
- Ombros TOTALMENTE caidos (25+ graus, quase deslocados)
- Olheiras ENORMES (cobrindo 50% do rosto, quase mascara)
- Terno DESTRUIDO (manchado, rasgado, cor sumiu)
- Martelo QUEBRADO (so o cabo, cabeca pendurada por um prego)
- Gravata quase caindo, manchada
- Cabelo GRISALHO, ralo, desgrenhado completamente
- Rugas por TODO o rosto
- Opacidade geral: 85% (ficando TRANSLUCIDO - invisivel politicamente)
- Expressao: VAZIA, olhar de mil metros, boca entreaberta sem proposito

### IDLE - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Postura de DERROTA total. Quase em formato de "C". Ombros ao nivel da cintura. Martelo quebrado pendurado na mao como peso morto. Olheiras MONSTRO. 85% opaco. |
| 2 | Balanca levemente (quase cai dormindo em pe). Martelo quebrado range. Boca entreaberta, baba ameaca cair. Translucido. |
| 3 | Murmura algo inaudivel ("Nos tempos da Lava Jato..."). Olhos OPACOS, sem brilho. Mao livre treme (Parkinson da alma). |
| 4 | PISCA de volta a realidade brevemente. Olha para o martelo quebrado com TRISTEZA profunda. Depois volta ao vazio. Alpha volta a 85%. |

### WALK - 6 frames (384x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Mal se move. Arrasta TUDO. Corpo em "C". Martelo quebrado arrasta no chao (sem forca pra segurar). Translucido. |
| 2 | Um passo leva o tempo de dois. Terno rasgado esvoaca. Gravata arrastando. |
| 3 | PARA brevemente (esqueceu pra onde ia). Olhos vagam. |
| 4 | Lembra (ou nao) e continua. Cada passo com dificuldade. |
| 5 | Tropecar sem recuperacao elegante. Quase rastejando. |
| 6 | "Andando" mas parece um zumbi (IRONIA: o jogo e de zumbis). Translucido permanente. |

### ATTACK - 3 frames (192x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | "Tenta" erguer martelo quebrado. Mal sai do chao. A cabeca do martelo balanca no prego. Patetic. |
| 2 | "Golpe" e mais uma queda controlada do martelo. Dano MINIMO (15% do Estagio 1). Nenhum efeito visual. Silencio. |
| 3 | Se apoia no cabo do martelo. Ofegante por minutos. Olhar de "por que eu ainda tento?". |

### DEATH - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Recebe golpe mas quase nao nota. Corpo ja tao debilitado que a diferenca e minima. |
| 2 | Simplesmente SENTA no chao. Nao e dramatico. So senta. Cansou. Martelo cai ao lado. |
| 3 | Deita devagar, como se fosse dormir. Fecha os olhos. Expressao quase de PAZ (alivio da irrelevancia). |
| 4 | Deitado. FADE OUT lento (alpha de 85% para 0%). Ninguem nota que ele morreu. O martelo se desfaz em particulas de ferrugem. Vazio. |

### HIT - 2 frames (128x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | ZERO REACAO. Corpo absorve o golpe sem expressao. Ja nao sente mais nada. Flash branco quase inexistente. |
| 2 | Mesma posicao. Nada mudou. "..." (nenhuma fala, nenhuma reacao). |

### SPECIAL: "Heroi Decaido" (Versao Enfraquecida) - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Tenta invocar aura dourada mas sai CINZA OPACA. Martelo quebrado mal levanta. Pose "heroica" patologica (curvada). |
| 2 | "Salta" 2 pixels. Martelo acima da cabeca por 0.1s antes de despencar. Sem brilho. |
| 3 | Martelo cai no chao por GRAVIDADE, nao por forca. Impacto: NENHUM efeito visual. Dano quase zero. |
| 4 | Fica olhando o martelo no chao. "Nos tempos da Lava Jato..." Particulas cinzas se dissipam. TRISTEZA pura. |

---

## DEGRADACAO PROGRESSIVA - Detalhes Tecnicos

### Transicoes entre Estagios
As transicoes acontecem DURANTE o gameplay, ao inicio de waves especificas:

#### Transicao 1→2 (Wave 4) - 4 frames de transicao
| Frame | Descricao |
|-------|-----------|
| 1 | Moro para de andar. Olha para as proprias maos. Leve tremor. |
| 2 | Ombros DESCEM 5 graus. Terno AMASSA visivelmente. Gravata TORCE. |
| 3 | Olheiras APARECEM (fade in). Martelo ESCURECE (perde brilho). |
| 4 | SUSPIRO. Novo visual completo. Continua andando mais devagar. |

#### Transicao 2→3 (Wave 7) - 4 frames de transicao
| Frame | Descricao |
|-------|-----------|
| 1 | Para novamente. Olha para o martelo. FERRUGEM comeca a aparecer ao vivo. |
| 2 | Ombros DESPENCAM mais 10 graus. Terno AMASSA severamente. Cabelo GRISALHA. |
| 3 | Olheiras DOBRAM de tamanho. Rugas SURGEM. Gravata AFROUXA. |
| 4 | GRUNHIDO de dor/cansaco. Martelo agora arrastando. Novo visual completo. |

#### Transicao 3→4 (Wave 10) - 4 frames de transicao
| Frame | Descricao |
|-------|-----------|
| 1 | Para. OLHA para o jogador pela quarta parede. Expressao de "voce ainda esta me vendo?" |
| 2 | Corpo COLAPSA para postura em "C". Ombros vao ao nivel da cintura. Terno PERDE cor. |
| 3 | Opacidade cai para 85%. Martelo QUEBRA (cabeca se solta, fica pendurada). Olheiras MONSTRO. |
| 4 | SILENCIO. Nenhuma expressao. Nenhum som. Novo visual completo. Ele e um fantasma vivo. |

---

## PROJETEIS / EFEITOS

### Golpe de Martelo (Efeito de Impacto) - 32x32px
- **Estagio 1**: Estrela de impacto dourada, brilhante, 4 frames (aparece → expande → brilha → dissipa)
- **Estagio 2**: Estrela menor, mais opaca, amarelo-desbotado, 3 frames
- **Estagio 3**: Particulas de ferrugem dispersas, marrom-laranja, 3 frames
- **Estagio 4**: NADA. Nenhum efeito visual. O golpe e silencioso e invisivel.

### Particulas de Ferrugem (Estagio 3-4) - 8x8px
- **Cor**: Marrom-laranja (#8B6914) com variacao
- **Comportamento**: Caem do martelo durante WALK e ATTACK
- **Quantidade**: 2-3 por frame de walk, 5-6 por frame de attack
- **Vida**: 0.5 segundos antes de desaparecer

### Aura Heroica → Aura Cinza
- **Estagio 1**: Aura dourada (#FFD700) a 40% alpha, pulsa lentamente
- **Estagio 2**: Aura amarelo-parda (#C4A035) a 25% alpha, pulsa devagar
- **Estagio 3**: Aura cinza (#808080) a 15% alpha, quase estatica
- **Estagio 4**: SEM AURA. Nada. Vazio.

---

## NOTAS DE PRODUCAO

1. A DEGRADACAO e o conceito central - CADA pixel deve contar a historia da queda
2. Ombros caindo e a deformidade MAIS IMPORTANTE - deve ser exagerada ao MAXIMO estilo Andre Guedes
3. O martelo de juiz e o item narrativo principal - sua degradacao PARALELA a do Moro
4. No Estagio 4, Moro deve parecer um FANTASMA - quase invisivel, quase inexistente
5. Contorno PRETO GROSSO (2px) em TODOS os sprites de TODOS os estagios
6. Rosto QUADRADO/ANGULAR em contraste com rosto REDONDO do Taxadd
7. A paleta de cores degrada de SATURADA (Estagio 1) para DESSATURADA (Estagio 4)
8. Estagios 3-4 devem ter particulas de ferrugem caindo do martelo como efeito constante
9. O fade out da morte no Estagio 4 (alpha → 0) e o momento mais PATETICO e deve ser LENTO (2 segundos)
10. Considerar que jogadores que so jogam poucas waves podem nunca ver Estagios 3-4, entao 1-2 devem ser visualmente COMPLETOS e satisfatorios
