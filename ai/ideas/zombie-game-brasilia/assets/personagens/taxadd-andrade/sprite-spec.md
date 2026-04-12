# TAXADD / ANDRADE - Especificacao de Sprites

## Mini-Boss (Taxadd) / NPC Inutil (Andrade) - "Zumbis de Brasilia"

---

## Especificacoes Tecnicas Gerais

- **Tamanho do sprite**: 64x64px por frame
- **Formato**: PNG com transparencia (RGBA)
- **Perspectiva**: Top-down levemente isometrica (Y-sorting)
- **Sprite sheets**: Horizontais (frames lado a lado)
- **Frame rate alvo**: 10 fps (estilo jerky/twitchy do Andre Guedes)

### IMPORTANTE: DUAS Sprite Sheets Separadas
1. **andrade-spritesheet.png** - NPC Inutil (persona Andrade)
2. **taxadd-spritesheet.png** - Mini-Boss (persona Taxadd)
3. **andrade-to-taxadd-transform.png** - Animacao de transformacao

---

## PALETA DE CORES

### Andrade
| Elemento | Cor | Hex |
|----------|-----|-----|
| Pele | Bege acinzentado (palidez) | `#D4B896` |
| Cabelo | Castanho apagado | `#4A3728` |
| Terno (corpo) | Cinza desbotado (emprestado do PT) | `#6B6B6B` |
| Terno (sombras) | Cinza escuro | `#3D3D3D` |
| Gravata | Vermelha PT desbotada | `#8B2020` |
| Mochila | Marrom escolar | `#8B5A2B` |
| Olhos | Marrom claro (perdido/vazio) | `#A67B5B` |
| Merenda (lancheira) | Amarelo sujo | `#C4A035` |
| Contorno | Preto grosso | `#1A1A1A` |

### Taxadd
| Elemento | Cor | Hex |
|----------|-----|-----|
| Pele | Bege mais vivo (poder) | `#D4A574` |
| Cabelo | Castanho (mesmo base) | `#4A3728` |
| Terno (corpo) | Verde-dinheiro saturado | `#1B5E20` |
| Terno (estampa $) | Dourado/amarelo | `#FFD700` |
| Gravata | Vermelha PT intensa | `#CC0000` |
| Oculos de vilao | Preto com reflexo verde | `#0D0D0D` / `#00FF00` |
| Calculadora | Cinza metalico | `#808080` |
| Cifras flutuantes ($) | Dourado brilhante | `#FFD700` |
| Carimbo "TAXADO" | Vermelho carimbo | `#CC0000` |
| Aura de taxa | Verde doentio translucido | `#00FF0044` |
| Moedas (bolsos) | Dourado | `#DAA520` |
| Contorno | Preto grosso | `#1A1A1A` |

---

## SPRITE SHEET 1: ANDRADE (NPC Inutil)

### Anatomia Base - Andrade
- Cabeca: REDONDA, 60% do sprite (cabeca grande, corpo pequeno)
- Olhos: Grandes, redondos, PERDIDOS (pupilas pequenas, olhando para cima)
- Boca: Pequena, levemente aberta (expressao de confusao permanente)
- Corpo: Pequeno em relacao a cabeca, terno LARGO demais (manga cobrindo as maos)
- Mochila escolar: Visivel nas costas, com lancheira amarela pendurada
- Deformidade: Cabeca desproporcional (grande) + corpo encolhido (pequeno) = infantilismo

### IDLE - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Postura neutra, olhos olhando para frente mas sem foco. Mochila nas costas. Mangas do terno cobrindo metade das maos. Boca levemente aberta. |
| 2 | Leve inclinacao da cabeca para direita (confusao). Olhos movem para cima (pensando em merenda). Pisca levemente. |
| 3 | Volta ao centro. Mao direita sobe timidamente como se fosse perguntar algo mas desiste. Olhos voltam ao vazio. |
| 4 | Cabeca inclina para esquerda. Leve balanco do corpo (inseguranca). Mochila treme levemente. |

### WALK - 6 frames (384x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Pe direito a frente, corpo inclinado. Mochila balanca para esquerda. Olhos olhando para baixo (inseguro). |
| 2 | Meio passo, ambos os pes no chao. Mochila no centro. Lancheira visivel balancando. |
| 3 | Pe esquerdo a frente. Mochila balanca para direita. Mangas do terno se arrastando. |
| 4 | Leve tropecar (pe pega no terno largo). Expressao de susto breve. |
| 5 | Recupera equilibrio. Mochila quase cai. Olhos arregalados. |
| 6 | Volta a postura de caminhada normal mas com leve desajuste no terno. |

### ATTACK - 3 frames (192x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | LEVANTA a lancheira de merenda acima da cabeca (preparando para jogar). Olhos arregalados (surpresa propria). |
| 2 | JOGA a lancheira para frente. Braco esticado, corpo se desequilibrando para tras. Expressao de esforco desproporcional. |
| 3 | Pos-ataque: quase cai para tras. Mochila aberta com itens de merenda caindo. Expressao de "ops". |

### DEATH - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Leva hit. Olhos viram espirais. Mochila se abre. |
| 2 | Cai de joelhos. Merenda esparrama pelo chao (sanduiche, suco, biscoitos). Terno se abre. |
| 3 | Cai de lado. Merenda rodeando o corpo. Olhos fechados. Expressao pacifica (aliviado por nao ter que fazer nada). |
| 4 | Deitado no chao cercado de merenda. Boca aberta com leve sorriso (morreu feliz pensando em merenda). Leve brilho de "fantasma" subindo. |

### HIT - 2 frames (128x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | RECUO para tras. Corpo curvado. Olhos ARREGALADOS. Flash branco sobre o sprite. Mochila balanca violentamente. |
| 2 | Volta a posicao mas cambaleando. Terno mais desajustado. Olhos ainda arregalados. |

### SPECIAL: "Merenda Infinita" - 6 frames (384x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Abre a mochila. Luz amarela sai de dentro. Olhos brilham de felicidade. |
| 2 | RETIRA sanduiche GIGANTE (desproporcional) da mochila. Baba escorrendo. |
| 3 | MORDIDA enorme. Pedacos voando. Coracao flutuando sobre a cabeca. |
| 4 | Mastigando com bochechas infladas (2x o tamanho normal). Olhos fechados de prazer. |
| 5 | Engole. Onda verde de cura emana do corpo. HP visualmente restaurado. |
| 6 | ARROTO. Volta ao normal mas com migalhas no terno. Expressao satisfeita. |

### SPECIAL: "Invisibilidade do Andrade" - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Normal. Ninguem olhando para ele. |
| 2 | Comeca a ficar TRANSLUCIDO (alpha 75%). Contornos se suavizam. |
| 3 | Quase INVISIVEL (alpha 30%). So se ve o contorno e a mochila. |
| 4 | COMPLETAMENTE transparente exceto pela sombra no chao e a lancheira flutuando. Efeito de "ninguem se importa". |

---

## SPRITE SHEET 2: TAXADD (Mini-Boss)

### Anatomia Base - Taxadd
- Cabeca: MESMA base redonda do Andrade, mas com OCULOS DE VILAO (verdes brilhantes)
- Expressao: Sorriso LARGO e COMPULSIVO (dentes a mostra, sorriso de quem "esta ajudando")
- Corpo: Mais ereto que Andrade (postura de poder)
- Maos: DESPROPORCIONALMENTE GRANDES (3x o tamanho normal) - para agarrar dinheiro
- Bolsos: INFINITOS que TRANSBORDAM moedas em TODOS os frames
- Terno: Verde-dinheiro com estampa de notas de dinheiro (padrao sutil)
- Calculadora: GIGANTE na mao direita (quase do tamanho do torso)
- Carimbo: Pendurado no cinto, visivel em todos os frames
- Cifras ($): 3-4 cifras douradas flutuando ao redor PERMANENTEMENTE
- Deformidade principal: MAOS ENORMES + bolsos infinitos transbordando

### IDLE - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Postura de poder. Calculadora na mao direita. Sorriso largo. Cifras $ flutuam na posicao 12h e 6h. Moedas caem lentamente do bolso esquerdo. |
| 2 | Dedos ENORMES digitam na calculadora (tap tap). Cifras $ rotacionam para 3h e 9h. Reflexo verde nos oculos. Moedas caem do bolso direito. |
| 3 | LEVANTA calculadora mostrando resultado. Sorriso MAIS largo. Cifras $ flutuam para 1h e 7h. Brilho dourado na tela da calculadora. |
| 4 | Acaricia o carimbo no cinto com mao esquerda (ENORME). Cifras $ voltam a 12h e 6h. Olhos brilham atras dos oculos. Bolsos PULSAM com moedas. |

### WALK - 6 frames (384x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Marcha decidida, pe direito a frente. Calculadora na mao. Cifras $ seguem o personagem com leve atraso. TRILHA DE MOEDAS no chao. |
| 2 | Meio passo. Mao esquerda (ENORME) aberta como se fosse AGARRAR algo. Moedas caindo dos bolsos. |
| 3 | Pe esquerdo a frente. Calculadora balanca. Cifras $ se reorganizam. Carimbo balanca no cinto. |
| 4 | Passo firme. Reflexo verde nos oculos pulsa. Bolsos TRANSBORDAM mais moedas. |
| 5 | Inclinacao para frente (ansioso para taxar). Maos enormes abertas. Cifras $ se expandem. |
| 6 | Retoma postura. Sorriso mais intenso. Calculadora brilha. Moedas continuam caindo. |

### ATTACK: "Calculadora Infernal" - 3 frames (192x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | LEVANTA calculadora acima da cabeca com mao ENORME. Tela da calculadora brilha VERDE INTENSO. Cifras $ giram rapido ao redor. Olhos BRILHAM atras dos oculos. |
| 2 | DISPARA cifras ($) como projeteis da calculadora. 3-4 cifras saem em cone para frente. Flash dourado de luz. GRITA "TAXADO!" (boca aberta enorme). |
| 3 | Pos-ataque. Fumaca da calculadora. Sorriso SATISFEITO. Carimbo "TAXADO" aparece brevemente no ar na direcao do ataque. Moedas EXPLODEM dos bolsos. |

### DEATH - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Recebe golpe. Oculos RACHAM. Calculadora voa da mao. Cifras $ se dispersam em panico. |
| 2 | Cai de joelhos. Bolsos EXPLODEM - cascata de moedas derrama para TODOS os lados. Oculos caem. REVELA olhos de Andrade (perdidos, confusos). |
| 3 | Cai de costas. Transformacao reversa comeca - terno verde volta a ser cinza. Calculadora quebrada ao lado. Moedas formam poca dourada ao redor. |
| 4 | Deitado. VOLTOU a ser Andrade. Terno cinza largo. Expressao perdida. Cifras $ se apagam uma a uma. Unica moeda restante rola para longe. |

### HIT - 2 frames (128x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | RECUO violento. Oculos torcem. Cifras $ se embaralham. Flash vermelho. Moedas JORRAM dos bolsos com impacto. Calculadora quase cai. |
| 2 | Recupera agressivamente. AGARRA calculadora com mao ENORME. Sorriso volta mas FORJADO. Oculos reajustados. Cifras $ voltam a orbitar mas tremendo. |

### SPECIAL: "Taxa Infinita" - 8 frames (512x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Abre os bracos (maos ENORMES abertas). Aura verde comeca a emanar do corpo. Cifras $ se multiplicam (de 4 para 8). Oculos brilham VERDE INTENSO. |
| 2 | Aura verde se EXPANDE em circulo (raio crescendo). Cifras se multiplicam para 12. Moedas flutuam do chao ao redor. Sorriso MANIACAL. |
| 3 | Aura atinge raio maximo. DRENA visualmente - particulas douradas sao SUGADAS dos arredores para o Taxadd. Olhos brilham como holofotes verdes. |
| 4 | Corpo INCHA levemente (alimentado pelas taxas). Bolsos INFLAM. Calculadora mostra numeros subindo rapido. |
| 5 | MAXIMO de poder. Corpo pulsando verde. TODAS as cifras girando freneticamente. Moedas orbitando como satelites. |
| 6 | Comeca a liberar excesso. Ondas de choque verdes. Cifras $ DISPARAM em todas as direcoes. |
| 7 | Explosao de moedas e cifras em 360 graus. CARIMBO "TAXADO" gigante se materializa no ar sobre a area de efeito. |
| 8 | Retorno ao normal mas com residuo verde no ar. Cifras voltam a orbita normal (4). Sorriso satisfeito. Moedas assentam. |

### SPECIAL: "Taxacao Universal" (Ultimate) - 8 frames (512x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | POSE DRAMATICA. Maos enormes erguidas ao ceu. Calculadora levita. TODAS as cifras $ do mapa comecam a tremer. |
| 2 | COLUNA de luz verde sobe do Taxadd ate o topo da tela. Tela comecar a ter BORDA DOURADA (interface sendo taxada). |
| 3 | Onda de choque verde se expande do centro. TUDO que a onda toca recebe selo "TAXADO" vermelho. |
| 4 | Power-ups no mapa encolhem 50%. Score pisca. HP bars de todos encolhem 20%. Velocidade cai. |
| 5 | INTERFACE DO JOGO e taxada - HUD fica com selo "TAXADO", score congela com cifrao, barras de vida com % removido. |
| 6 | Taxadd no centro, flutuando, rodeado por CENTENAS de cifras $. MAOS enormes abertas em "T". Sorriso DEMONICO. |
| 7 | Comeca a descer. Efeitos permanentes se estabelecem. Selos "TAXADO" piscam em vermelho por todo o mapa. |
| 8 | Pousa. Volta ao idle. Mas TUDO ao redor permanece taxado (selos visiveis). Cifras voltam a orbita normal. Ajusta os oculos com ar de "dever cumprido". |

### SPECIAL: "Imposto Retroativo" - 4 frames (256x64px total)
| Frame | Descricao |
|-------|-----------|
| 1 | Puxa RELOGIO de bolso (mao ENORME segurando relogio desproporcional). Oculos brilham. Cifras $ ficam azuladas (tempo). |
| 2 | Gira ponteiros do relogio PARA TRAS. Efeito de rewind visual (linhas de tempo ao redor). Corpo pisca entre presente e passado. |
| 3 | SELO "RETROATIVO" aparece. Pontos dos ultimos 10 segundos sao SUGADOS do score (numeros voando do HUD para o Taxadd). |
| 4 | Guarda relogio. Sorriso satisfeito. Score do alvo REDUZIDO. Cifras $ voltam a dourado. Moedas extras no bolso. |

---

## SPRITE SHEET 3: TRANSFORMACAO ANDRADE → TAXADD (6 frames, 384x64px)

| Frame | Descricao |
|-------|-----------|
| 1 | ANDRADE normal (NPC). Olhos perdidos. Terno cinza. Mochila nas costas. De repente, OLHA para algo (dinheiro?). |
| 2 | Olhos se ARREGALAM. Brilho verde nos olhos. Mochila comeca a cair. Terno comeca a MUDAR de cor (cinza → verde). |
| 3 | OCULOS DE VILAO materializam no rosto. Terno 50% verde. Maos comecam a CRESCER. Primeiras moedas saem dos bolsos. |
| 4 | Terno completamente verde com estampa $. Maos ENORMES. Calculadora MATERIALIZA na mao direita. Primeiras cifras $ aparecem flutuando. |
| 5 | Mochila EXPLODE e se transforma no carimbo (pendurado no cinto). Bolsos ENCHEM de moedas. Cifras $ em orbita. Sorriso se ALARGA. |
| 6 | TAXADD COMPLETO. Pose de poder. Flash verde. Todas as cifras $ em posicao. Moedas transbordando. "TAXADD" aparece brevemente sobre a cabeca como titulo de boss. |

---

## PROJETEIS

### Cifras $ (Projetil da Calculadora Infernal) - 32x32px
- **Sprite**: Cifrao dourado ($) com brilho
- **Animacao**: 4 frames de rotacao (giro no eixo Y)
- **Cores**: Dourado (#FFD700) com contorno preto (#1A1A1A) e brilho branco (#FFFFFF) no centro
- **Trail**: Rastro de particulas douradas menores atras

### Carimbo "TAXADO" (Efeito Visual) - 32x32px
- **Sprite**: Retangulo vermelho com texto "TAXADO" em branco
- **Animacao**: 3 frames (aparece, pulsa, desaparece gradualmente)
- **Cores**: Vermelho carimbo (#CC0000) com texto branco (#FFFFFF) e borda preta
- **Aplicacao**: Aparece sobre inimigos/objetos atingidos

### Moedas (Particula) - 16x16px
- **Sprite**: Moeda dourada simples
- **Animacao**: 4 frames de rotacao horizontal
- **Cores**: Dourado (#DAA520) com contorno preto e brilho central

### Merenda (Projetil do Andrade) - 32x32px
- **Sprite**: Lancheira amarela (#C4A035)
- **Animacao**: 3 frames (rotacao no ar)
- **Impacto**: Sanduiche, suco e biscoitos se espalham (4 sub-sprites de 16x16px)

---

## PARTICULAS PERMANENTES DO TAXADD

### Cifras $ Orbitantes
- **Quantidade**: 3-4 cifras SEMPRE visivel ao redor do Taxadd
- **Movimento**: Orbita circular lenta (1 rotacao completa a cada 2 segundos)
- **Raio**: 8-12px do centro do sprite
- **Tamanho**: 8x8px cada
- **Alpha**: 80% (levemente translucido)
- **Cor**: Dourado (#FFD700) com variacao de brilho

### Moedas Caindo dos Bolsos
- **Frequencia**: 1 moeda a cada 0.5 segundos durante WALK
- **Tamanho**: 4x4px (miniatura)
- **Comportamento**: Cai do bolso, quica 1x, desaparece apos 1 segundo
- **Cor**: Dourado com variacao

---

## NOTAS DE PRODUCAO

1. Andrade e Taxadd compartilham a MESMA base de rosto redondo - a transformacao deve ser CRIVEL
2. A diferenca visual entre os dois deve ser INSTANTANEAMENTE reconhecivel mesmo em 64x64px
3. As maos ENORMES do Taxadd sao o elemento mais distinto - exagerar ao MAXIMO
4. Cifras $ devem ter alto contraste (dourado sobre qualquer fundo) para serem visiveis
5. O carimbo "TAXADO" deve ser legivel mesmo em tamanho pequeno (32x32px)
6. Manter contorno PRETO GROSSO (2px) em TODOS os sprites (estilo Andre Guedes)
7. Sombras pesadas no lado direito-inferior de cada sprite
8. A transformacao e o momento visual mais importante - deve ser IMPACTANTE mesmo em pixel art
