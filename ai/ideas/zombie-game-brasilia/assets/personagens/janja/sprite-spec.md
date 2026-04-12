# Janja (A Verdadeira Presidente) - Especificacao de Sprites

## Dados Gerais

| Propriedade         | Valor                                      |
|--------------------|--------------------------------------------|
| Tipo                | NPC / Mini-boss                            |
| Sprite size         | 64x64px                                    |
| Projetil size       | 32x32px                                    |
| Perspectiva         | Top-down levemente isometrica              |
| Sprite atlas        | 2048x2048px (compartilhado)                |
| Formato             | PNG com transparencia                      |
| Orientacoes         | 4 direcoes (S, N, E, W)                   |

---

## PALETA DE CORES

### Cores Primarias
| Elemento                 | Hex       | Notas                                       |
|-------------------------|-----------|----------------------------------------------|
| Cabelo capacete          | #DAA520  | Dourado escuro, loiro saturado-sujo          |
| Cabelo highlights        | #FFD700  | Dourado brilhante nos pontos de luz          |
| Cabelo sombra            | #B8860B  | Dourado escuro pras sombras do volume        |
| Pele (normal)            | #D4956A  | Tom quente mediterraneo                      |
| Pele (gritando)          | #CC3333  | Vermelho -- furia G20                        |
| Roupa grife (base)       | #0D0D0D  | Preto quase total, vestido caro              |
| Roupa grife (logos)      | #C0C0C0  | Prata -- logos de grife sutilmente visiveis  |
| Roupa grife (detalhes)   | #8B0000  | Vermelho escuro nos acessorios               |
| Bolsa gigante            | #5C4033  | Marrom couro caro                            |
| Bolsa fivela             | #FFD700  | Dourado brilhante                            |
| Tapete vermelho          | #8B0000  | Vermelho sangue escuro, aveludado            |
| Tapete franja            | #FFD700  | Dourado nas bordas                           |
| Notas de dinheiro        | #228B22  | Verde dinheiro                               |
| Notas detalhe            | #006400  | Verde escuro pro simbolo do R$               |
| Cartao corporativo       | #1C1C1C  | Preto com chip dourado                       |
| Cartao chip              | #FFD700  | Dourado metalico                             |
| Celular                  | #2F2F2F  | Cinza escuro, tela brilhante                 |
| Celular tela             | #00BFFF  | Azul luminoso (app de compras)               |
| Unhas garras             | #8B0000  | Vermelho escuro, compridas                   |
| Olhos                    | #3D2B1F  | Castanho escuro, determinados                |
| Olhos (furia)            | #FF0000  | Vermelho injetado                            |
| Batom                    | #CC0033  | Vermelho vivo, boca ENORME                   |
| Brincos                  | #FFD700  | Dourado, grandes, balancam                   |
| Sombras                  | #0D0D0D  | Preto quase total                            |
| Linhas de contorno       | #000000  | Preto puro, grossas (2px em 64x64)          |

---

## ANATOMIA DO SPRITE (64x64px)

### Proporcoes (Caricatura Grotesca)
- Cabelo capacete: ~28x18px (DESPROPORCIONAL, ocupa quase metade da largura -- e a piada)
- Cabeca (sob o cabelo): ~16x14px (normal-pequena, esmagada pelo cabelo)
- Boca: ~12x6px (ENORME, ocupa 75% do rosto -- fala mais que todo mundo)
- Tronco: ~14x14px (vestido preto justo, logos de grife em pixels)
- Pernas: ~10x16px (salto alto exagerado, 4px so de salto)
- Bracos: ~6x18px (finos, terminam em unhas-garras de 4px)
- Bolsa: ~20x16px (MAIOR que o tronco -- grotescamente grande)

### Deformidade Principal: CABELO CAPACETE
- Volume absurdo: o cabelo e maior que a cabeca em si
- Em idle: pulsa levemente (1px expansao/contracao)
- Em walk: balanca como uma massa solida, nao como cabelo real
- Em grito (Fora Elon): o cabelo se ARREPIA e cresce +4px momentaneamente
- Highlights dourados (#FFD700) se movem frame a frame simulando brilho

### Deformidade Secundaria: BOCA ENORME
- Desproporcional ao rosto, labios vermelhos grossos
- Em idle: boca entreaberta, sempre prestes a falar
- Em attack/special: boca abre MAIS que o rosto permitiria (deformacao)
- Em grito: boca ocupa 90% do rosto, ondas sonoras visiveis

### Deformidade Terciaria: UNHAS-GARRAS
- Unhas compridas nos 5 dedos, curvadas como garras
- Vermelho escuro (#8B0000), 3-4px de comprimento
- Sempre agarrando algo: celular, cartao, bolsa
- Em attack: brilham com flash dourado

---

## ACESSORIOS (posicao nos sprites)

### Bolsa Gigante de Grife (item essencial)
- Tamanho: 20x16px (MAIOR que o torso)
- Posicao: pendurada no braco esquerdo (idle/walk), arremessada (attack)
- Fivela dourada visivel (#FFD700), 3x2px
- Logos de grife: pixels cinza-prata (#C0C0C0) formando padrao
- Na death: EXPLODE em notas de dinheiro

### Cartao Corporativo
- Tamanho: 8x5px
- Posicao: mao direita (idle), levantado acima da cabeca (attack)
- Chip dourado visivel (#FFD700), 2x2px
- Brilho: 1px de highlight branco
- Ao usar: particulas douradas saem dele

### Celular
- Tamanho: 4x7px
- Posicao: mao direita quando nao esta com cartao
- Tela brilhante (#00BFFF), sempre acesa
- Notificacoes: pontinhos vermelhos 1x1px piscando

### Tapete Vermelho (acessorio de chao)
- Tamanho: 48x12px (se estende na frente da Janja)
- Posicao: sempre sob os pes, desenrola na direcao do walk
- Cor: #8B0000 com franja dourada #FFD700 nas bordas
- Atras: tapete se desfaz em notas de dinheiro voando (particulas)

### Brincos
- Tamanho: 2x3px cada
- Posicao: nas laterais da cabeca, sob o cabelo
- Balancam independentemente do corpo (1px offset alternado)

---

## ANIMACOES

### 1. IDLE (4 frames, 8 FPS)
Sprite sheet: 256x64px (4 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Pose de poder: queixo levantado, mao esquerda segurando bolsa gigante, mao direita com celular. Cabelo capacete no tamanho maximo. Boca entreaberta com batom vermelho. Pernas cruzadas em salto alto. Tapete vermelho sob os pes. |
| 2     | Cabelo PULSA -- expande 1px em todas direcoes. Brincos balancam pra esquerda. Bolsa balanca 1px pra baixo (peso). Olhar de superioridade, sobrancelha arqueada. Celular pisca notificacao. |
| 3     | Cabelo contrai 1px (volta ao normal). Brincos balancam pra direita. Boca abre levemente mais -- como se fosse falar. Mao com celular sobe 1px (checando mensagem). Unha-garra visivel segurando celular. |
| 4     | Suspiro de tedio: ombros levantam 1px e descem. Bolsa balanca 1px pra cima. Cabelo volta a expandir. Expressao de "eu mando aqui". Notas de dinheiro flutuam atras (2 particulas 2x3px). |

### 2. WALK (6 frames, 10 FPS)
Sprite sheet: 384x64px (6 frames x 64px) -- 4 direcoes = 384x256px total

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Perna esquerda a frente, salto alto visivel (4px). Tapete vermelho se desenrola 4px na frente. Bolsa balanca pra tras. Cabelo capacete firme (massa solida). Atras: 1 nota de dinheiro se solta do tapete. |
| 2     | Transicao: pernas quase juntas. Corpo levemente empinado (postura arrogante). Tapete desenrola +4px. Celular na mao, olhando pra tela enquanto anda. Brincos em movimento. |
| 3     | Perna direita a frente. Bolsa balanca pra frente (momentum). Cabelo balanca como bloco solido (1px offset oposto ao corpo). Tapete continua. Atras: mais 1 nota se solta. |
| 4     | Transicao: passos determinados. Queixo levantado. Mao com cartao corporativo ao lado do corpo. Tapete vermelho continuo sob os pes. |
| 5     | Perna esquerda novamente. Bolsa quase arrasta no chao pelo peso. Cabelo brilha (highlight muda de posicao). Atras: 2 notas voam. |
| 6     | Passo final do ciclo: momento de "deslize" -- corpo parece flutuar 1px (ela NAO anda, ela DESFILA). Tapete intacto na frente, desintegrando atras. |

**Nota**: Walk deve parecer um DESFILE, nao uma caminhada. Pose sempre altiva, como se houvesse cameras apontadas.

### 3. ATTACK -- Cartao Corporativo (3 frames, 12 FPS)
Sprite sheet: 192x64px (3 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Windup: Janja levanta o cartao corporativo acima da cabeca com a mao direita (unhas-garras visiveis). Boca abre ENORME (deformacao -- ocupa 80% do rosto). Grita: bolha "COMPRA!" (8x6px). Bolsa brilha. Cabelo se arrepia 2px. |
| 2     | Swipe: cartao corta o ar -- trail dourado (2px streak). Do cartao CAEM projeteis de luxo (sprites separados 32x32px): bolsa, sapato, colar. Rosto satisfeito. Flash dourado no cartao. |
| 3     | Impact: itens de luxo atingem o chao/inimigos em area. Explosao de cifras "$" e "R$" (particulas 3x3px douradas). Janja posa com cartao, sorriso de vitoria. Notas voam em todas direcoes. |

### 4. DEATH (4 frames, 6 FPS)
Sprite sheet: 256x64px (4 frames x 64px)
Animacao especial: "Queda da Primeira-Dama"

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Impacto: corpo jogado pra tras, bracos abertos. Bolsa gigante voa da mao (projetil separado 32x32px). Boca em "O" de choque. Cartao corporativo voa pro outro lado. Celular quebra no chao. |
| 2     | Desmoronamento: o CABELO CAPACETE comeca a desmontar -- fios saindo pra todos os lados como se a peruca estivesse caindo. Brincos voam. Salto alto quebra (1 pe fica torto). Tapete sob ela comeca a se enrolar. |
| 3     | No chao: corpo de lado, cabelo totalmente desmontado (ocupa +8px de area irregular em volta da cabeca). Bolsa EXPLODE em notas de dinheiro (8-10 particulas verdes voando em leque). Maquiagem borrada (pixels vermelhos desalinhados no rosto). |
| 4     | Fade: mesma pose, olhos fechando. Notas de dinheiro caem lentamente ao redor. Tapete vermelho se dissolve em particulas. Cores dessaturam 30%. Ultima nota cai. Bolha de fala fraca: "a conta..." (6x4px, transparencia crescente). |

**Nota**: Frames 3-4 duram mais (3 segundos antes de desaparecer). A bolsa explodindo em notas e o momento visual principal.

### 5. HIT (2 frames, 12 FPS)
Sprite sheet: 128x64px (2 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Recuo: corpo jogado 2px pra tras. Flash branco no corpo inteiro (1 frame). Boca ABRE ENORME -- expressao de INDIGNACAO pura. Bolha: "COMO OUSAM?!" (12x6px). Cabelo capacete treme violentamente. Bolsa quase cai. Brincos voam pro lado. |
| 2     | Recuperacao: volta a posicao, MAIS FURIOSA. Olhos estreitados (#FF0000). Unhas-garras parecem maiores (+1px). Agarra a bolsa com forca. Queixo mais levantado que antes. Expressao de "voce vai pagar por isso". |

### 6. SPECIAL: FORA ELON MUSK! (6 frames, 10 FPS)
Sprite sheet: 384x64px (6 frames x 64px)
Efeito: Desativa toda tecnologia no mapa por 3 segundos

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Preparacao: Janja para, planta os pes no tapete. Inspira fundo -- peito expande 2px. Mao larga o celular (ironia). Rosto comeca a ficar vermelho (#CC3333). Cabelo comeca a se arrepiar. |
| 2     | Buildup: cabelo CRESCE +4px (arrepia como capacete de eletricidade estatica). Rosto #FF2222. Boca comeca a abrir ENORMEMENTE. Punhos cerrados nos lados. Energia visivel ao redor (particulas amarelas #FFD700 surgindo). |
| 3     | GRITO: boca ocupa 90% do rosto (deformacao maxima). Ondas sonoras concentricas saem da boca (3 arcos, #FF4500, expandindo). Texto "FORA ELON!" voa como projetil (32x12px, vermelho bold). Cabelo no maximo volume (+6px). Todo o sprite treme 2px. |
| 4     | Onda de choque: circulo de EMP se expande do centro da Janja (raio 48px, azul eletrico #00BFFF, alpha decrescente). Dispositivos eletronicos proximos faiscam. Particulas de eletricidade (#FFD700) em todas direcoes. |
| 5     | Efeito continua: tela do jogo faz leve "static" (referencia a tecnologia desativando). Janja ainda na pose de grito, bracos abertos agora. Onda de choque se dissipa nos cantos. Inimigos com icone de "sem sinal" (X vermelho sobre celular). |
| 6     | Recuperacao: Janja fecha a boca, sorriso de satisfacao. Cabelo volta ao normal lentamente (-2px por frame). Rosto voltando ao tom normal. Pega o celular de volta. Pose vitoriosa com mao no quadril. |

### 7. SPECIAL: SUSSURRO PRESIDENCIAL (4 frames, 8 FPS)
Sprite sheet: 256x64px (4 frames x 64px)
Efeito: Controla NPC Lula-zumbi (ele obedece ao proximo comando)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Janja se inclina pro lado (direcao do Lula-zumbi). Mao sobre a boca (sussurrando). Olhos estreitados, sorriso maquiavelico. Bolha de fala com "psss..." em fonte pequena (6x4px). |
| 2     | Mais perto: sprite de Janja se sobrepoe levemente ao do Lula. Boca perto da orelha dele. Particulas roxas (#660066) saem da boca dela ate a cabeca dele (3-4 pontinhos em trail). Mao com unhas-garras no ombro do Lula. |
| 3     | Sussurro completo: Lula-zumbi tem olhos em espiral (hipnotizado). Icone de "controlado" acima dele (olho roxo 4x4px). Janja se afasta com sorriso largo. Particulas roxas se dissipam. |
| 4     | Pose final: Janja de bracos cruzados, olhando satisfeita. Lula-zumbi ao lado com pose rigida de "aguardando ordens". Bolha dele: "Sim, amor" (8x4px). Ela com bolha: "Bom menino" (8x4px). |

### 8. SPECIAL: TAPETE VERMELHO (4 frames, 8 FPS)
Sprite sheet: 256x64px (4 frames x 64px)
Efeito: Area de slow -- inimigos no tapete ficam 50% mais lentos

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Janja estala os dedos (flash dourado nos dedos). Unhas-garras brilham. Tapete sob os pes comeca a PULSAR vermelho mais intenso (#FF0000). Bolha: "Estendam o tapete!" (10x4px). |
| 2     | Tapete se ESTENDE rapidamente na direcao apontada (16px por frame). Franjas douradas nas bordas se desenrolam. Particulas de luxo surgem no tapete (brilhos 1x1px dourados). |
| 3     | Tapete atinge extensao maxima (96px de comprimento, 16px de largura). Brilho aveludado pulsa. Inimigos que pisam ficam com icone de "pes grudados" (correntes douradas nos pes). Notas de dinheiro flutuam das bordas do tapete. |
| 4     | Tapete estabiliza: pulsacao suave (1px de expansao/contracao nas bordas). Janja caminha sobre ele com pose de desfile. Atras dela, tapete comeca a se desfazer em notas lentamente. Ciclo pode repetir enquanto skill estiver ativa. |

### 9. SPECIAL: REFORMA COMPULSORIA (4 frames, 8 FPS)
Sprite sheet: 256x64px (4 frames x 64px)
Efeito: Muda cenario temporariamente (efeito visual de luxo)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Janja tira o cartao corporativo e o BEIJA. Flash de luz dourada. Olhos com cifrao (simbolo $ nos olhos, 2x2px). Bolha: "Mais uma reforminha!" (10x4px). |
| 2     | Cartao BRILHA intensamente -- raios dourados saem em 8 direcoes (linhas de 1px). Onda circular dourada se expande (efeito similar ao EMP mas dourado #FFD700). Notas de dinheiro voam radialmente. |
| 3     | Area de efeito: tiles ao redor mudam temporariamente -- chao vira marmore, paredes ganham molduras douradas, postes viram lustres (overlay 50% alpha). Janja no centro com bracos abertos admirando. |
| 4     | Efeito estabiliza: cenario luxuoso pulsando suavemente. Janja com pose satisfeita, bolsa apertada contra o peito. Notas caem como confete. Expressao: "Ficou lindo, amor". Timer visivel indicando duracao do efeito. |

---

## BARRA DE GASTOS (UI Element -- Recurso da Janja)

### Posicao
- Acima da cabeca: 32x4px barra com icone de cartao 6x4px ao lado
- Ou no HUD se Janja for selecionada

### Estados Visuais

| Nivel       | Cor da Barra | Comportamento do Sprite                          |
|------------|-------------|---------------------------------------------------|
| 100-75%    | #FFD700     | Orçamento cheio. Janja calma, gastando livremente. |
| 75-50%     | #FFA500     | Gasto moderado. Bolsa parece mais leve.           |
| 50-25%     | #FF4500     | Ficando sem credito. Unhas tremem. Olhar ansioso. |
| 25-1%      | #FF0000     | Desespero: tenta usar cartao, "RECUSADO" aparece. |
| 0%         | Vazio       | FRENESI: ataque fisico com a bolsa (modo berserker). |

### Sprites da Barra
- Barra cheia: retangulo #FFD700 com borda #333333
- Barra diminuindo: gradiente da cor atual
- Barra vazia: retangulo vazio com borda vermelha PULSANTE, texto "RECUSADO" 1px
- Icone: mini cartao 6x4px ao lado esquerdo com chip dourado

---

## PROJETEIS (32x32px)

### Itens de Luxo (Cartao Corporativo)
4 variantes, cada uma com 2 frames de rotacao:

| Projetil       | Descricao                                            |
|---------------|------------------------------------------------------|
| Bolsa grife    | 32x32px, marrom couro com fivela dourada, gira no ar |
| Sapato salto   | 32x24px, preto com salto vermelho, tumbles           |
| Colar diamante | 24x24px, brilhos brancos piscando, gira              |
| Joia/anel      | 16x16px, dourado com pedra vermelha, trail de brilho |

- Trail: particulas douradas (#FFD700) de 1x1px atras de cada item
- Impacto: explosao de cifras "R$" (4-6 particulas 3x3px douradas) + flash branco

### Texto-Projetil "FORA ELON!"
- 32x12px, texto pixelado bold em vermelho (#FF0000)
- Borda amarela (#FFD700) de 1px
- Ondas sonoras ao redor (arcos concentricos)
- 2 frames: texto pisca/treme entre frames

### Nota de Dinheiro (particula de tapete)
- 8x4px, verde (#228B22) com detalhe escuro (#006400)
- 4 frames de rotacao (tumble no ar)
- Usada como particula do tapete E da explosao de morte

---

## EFEITOS DE PARTICULAS (por sprite)

| Efeito                  | Tamanho   | Cor         | Quantidade | Contexto                           |
|------------------------|-----------|-------------|------------|------------------------------------|
| Notas de dinheiro       | 8x4px     | #228B22     | 4-10       | Tapete, death, reforma, idle       |
| Brilho de luxo          | 1x1px     | #FFD700     | 6-12       | Cartao, tapete, reforma            |
| Cifras R$               | 3x3px     | #FFD700     | 4-6        | Impacto de projetil                |
| Ondas sonoras           | arco 2px  | #FF4500     | 3          | Fora Elon, grito                   |
| Onda EMP                | circulo   | #00BFFF     | 1 (expande)| Fora Elon                          |
| Particulas de controle  | 2x2px     | #660066     | 3-4        | Sussurro Presidencial              |
| Eletricidade estatica   | 2x3px     | #FFD700     | 4-8        | Fora Elon, cabelo arrepiado       |
| Fragmentos de maquiagem | 2x2px     | #CC0033     | 3-4        | Death, hit                         |
| Brilho de tapete        | 1x1px     | #FFD700     | 8-12       | Tapete ativo                       |
| Confete dourado         | 2x2px     | #FFD700     | 10-15      | Reforma Compulsoria                |

---

## LAYOUT NO ATLAS (2048x2048px)

Posicao sugerida para sprites de Janja no atlas compartilhado:

| Animacao                | Posicao no Atlas | Tamanho Total        |
|------------------------|------------------|----------------------|
| Idle (4dir)             | (0, 1024)        | 256x256px            |
| Walk (4dir)             | (256, 1024)      | 384x256px            |
| Attack (4dir)           | (640, 1024)      | 192x256px            |
| Death                   | (832, 1024)      | 256x64px             |
| Hit (4dir)              | (0, 1280)        | 128x256px            |
| Fora Elon Musk          | (128, 1280)      | 384x64px             |
| Sussurro Presidencial   | (512, 1280)      | 256x64px             |
| Tapete Vermelho          | (768, 1280)      | 256x64px             |
| Reforma Compulsoria     | (1024, 1280)     | 256x64px             |
| Projeteis (luxo)        | (0, 1344)        | 256x32px             |
| Projeteis (texto)       | (256, 1344)      | 64x32px              |
| Particulas              | (320, 1344)      | 128x64px             |
| Barra de Gastos         | (448, 1344)      | 128x16px             |

---

## INTERACAO COM LULA-ZUMBI

### Sprites de Duo (Janja + Lula juntos)
Quando Janja usa "Sussurro Presidencial", sprites adicionais de interacao:

| Sprite                  | Tamanho   | Descricao                                          |
|------------------------|-----------|-----------------------------------------------------|
| Sussurro (duo)          | 96x64px   | Janja inclinada sussurrando na orelha do Lula-zumbi |
| Lula controlado         | 64x64px   | Lula com olhos em espiral e aura roxa               |
| Ordem executada         | 64x64px   | Lula fazendo acao com icone de marionete acima      |

---

## BORDOES (Bolhas de Fala)

As bolhas de fala sao sprites separados que aparecem acima da Janja em contextos especificos:

| Texto                                              | Tamanho    | Contexto           |
|---------------------------------------------------|------------|---------------------|
| "Querido, gostou da reforma?"                      | 24x8px     | Reforma Compulsoria |
| "Para quem eu mando a conta, amor?"                | 28x8px     | Attack              |
| "FORA, ELON MUSK!"                                 | 20x8px     | Special Fora Elon   |
| "Quem manda aqui sou eu, amor. Voce so assina."    | 32x8px     | Sussurro            |
| "Mais uma reforminha, presidente?"                  | 28x8px     | Idle aleatorio      |
| "COMO OUSAM?!"                                      | 14x6px     | Hit                 |
| "a conta..."                                         | 10x4px     | Death (fade)        |
