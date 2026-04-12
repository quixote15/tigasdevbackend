# Ciro Gomes - Especificacao de Sprites

## Dados Gerais

| Propriedade         | Valor                              |
|--------------------|------------------------------------|
| Tipo                | NPC Comico (Comic Relief Supremo)  |
| Sprite size         | 64x64px                            |
| Projetil size       | 32x32px                            |
| Perspectiva         | Top-down levemente isometrica      |
| Sprite atlas        | 2048x2048px (compartilhado)        |
| Formato             | PNG com transparencia              |
| Orientacoes         | 4 direcoes (S, N, E, W)           |

---

## PALETA DE CORES

### Cores Primarias
| Elemento             | Hex       | Notas                               |
|---------------------|-----------|--------------------------------------|
| Terno               | #1B2A4A  | Azul marinho escuro, bem cortado     |
| Gravata             | #8B0000  | Vermelho sangue escuro               |
| Camisa              | #F0F0F0  | Branco levemente sujo                |
| Pele (estado normal)| #D4956A  | Tom quente, mediterraneo             |
| Pele (irritado)     | #CC3333  | Vermelho vivo                        |
| Pele (panico)       | #FF2222  | Vermelho berrante, pulsante          |
| Cabelo              | #8C8C8C  | Grisalho prateado, brilhante        |
| Veias               | #660066  | Roxo escuro, pulsam com raiva        |
| Sapatos             | #1A1A1A  | Preto lustrado                       |
| Rivotril (frasco)   | #FF6B00  | Laranja farmaceutico                 |
| Rivotril (liquido)  | #00BFFF  | Azul ciano luminoso                  |
| Olhos (normais)     | #3D2B1F  | Castanho escuro                      |
| Olhos (raiva)       | #FF0000  | Vermelho injetado                    |
| Cirocracia (cupula) | #4169E1  | Azul royal, translucido              |
| Sombras             | #0D0D0D  | Preto quase total                    |
| Linhas de contorno  | #000000  | Preto puro, grossas (2px em 64x64)  |

---

## ANATOMIA DO SPRITE (64x64px)

### Proporcoes (Caricatura Grotesca)
- Cabeca: ~24x20px (ENORME, 37% da altura) — cabeca grande = arrogancia intelectual
- Tronco: ~16x16px (terno justo, ombros largos de politico convicto)
- Pernas: ~12x18px (curtas em relacao ao corpo, apressadas)
- Bracos: ~8x20px (gesticulam freneticamente)
- Pescoco: ~8x6px (GROSSO, cheio de veias saltadas)
- Maxilar: Quadrado, travado, proeminente

### Deformidade Principal: VEIAS DO PESCOCO
- 3-4 veias visiveeis que vao do pescoco ate a testa
- Em estado normal: linhas finas roxas (#660066)
- Irritado: veias se dilatam (2x largura), pulsam em frames alternados
- Panico (sem Rivotril): veias SALTAM do pescoco como tentaculos, 3D quase, ocupam 4-6px extras ao redor da cabeca
- Animacao: veias se movem independentemente como vermes/cobras

### Deformidade Secundaria: ROSTO VERMELHO PROGRESSIVO
- Estado 1 (calmo): pele #D4956A, normal
- Estado 2 (irritado): pele #CC3333, suor na testa
- Estado 3 (furioso): pele #FF2222, vapor saindo das orelhas
- Estado 4 (panico): rosto inteiro pulsa entre #FF2222 e #FF0000 a cada frame

---

## ACESSORIOS (posicao nos sprites)

### Frasco de Rivotril (item essencial)
- Tamanho: 8x12px
- Posicao: mao esquerda (quando idle), bolso do terno (durante walk)
- Liquido visivel dentro: nivel diminui conforme "barra de Rivotril"
- Brilho: 1px de highlight branco no vidro
- Quando vazio: rachadura no frasco, sem liquido

### Livro de Economia
- Tamanho: 10x8px
- Posicao: debaixo do braco direito (idle/walk), jogado no chao (attack)
- Titulo ilegivel mas visivel
- Capa: #8B4513 (marrom couro)

### Xicara de Cafe
- Tamanho: 6x6px
- Posicao: mao quando em Debate Unilateral
- Fumaca: 2-3 pixels brancos acima, animados

---

## ANIMACOES

### 1. IDLE (4 frames, 8 FPS)
Sprite sheet: 256x64px (4 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Pose arrogante: queixo levantado, mao esquerda com Rivotril, livro no braco direito. Veias normais. Rosto #D4956A. |
| 2     | Leve inclinacao pra frente como quem vai comecar a falar. Boca entreaberta. Veias pulsam 1px. Sobrancelha levantada. |
| 3     | Volta a posicao 1 mas com micro-tremor na mao do Rivotril (1px deslocamento). Olhar impaciente. |
| 4     | Suspiro: ombros sobem 1px e descem. Expressao de desprezo. Fumaca do cafe (se visivel). |

### 2. WALK (6 frames, 10 FPS)
Sprite sheet: 384x64px (6 frames x 64px) — 4 direcoes = 384x256px total

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Perna esquerda a frente, braco direito balanca pra tras. Terno estica nos ombros. Passo determinado. |
| 2     | Transicao: ambas pernas quase juntas, corpo levemente inclinado pra frente. Rivotril no bolso. |
| 3     | Perna direita a frente, braco esquerdo balanca. Gravata move 1px pro lado. |
| 4     | Transicao: passo largo, cabeca levemente inclinada (arrogante). |
| 5     | Perna esquerda a frente novamente. Livro quase caindo debaixo do braco. |
| 6     | Passos apressados: quadro de transicao rapida, blur de 1px nas pernas. |

**Nota**: Walk deve parecer APRESSADO e IRRITADO, como quem esta sempre atrasado pra um debate.

### 3. ATTACK (3 frames, 12 FPS)
Sprite sheet: 192x64px (3 frames x 64px)
Arma: Frasco de Rivotril Turbo (clava gigante)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Windup: braco direito levanta o frasco gigante (16x20px) acima da cabeca. Rosto #CC3333 (irritado). Veias dilatadas. Corpo inclina pra tras. |
| 2     | Swing: braco desce em arco. Frasco no ponto mais baixo do arco. Blur de movimento (2px trail). Veias MAXIMAMENTE dilatadas. Boca aberta gritando. |
| 3     | Impact: frasco no chao/inimigo. Ondas de impacto (3 circulos concentricos 2px). Liquido espirra (3-4 gotinhas azuis #00BFFF). Rosto satisfeito por 1 frame. |

### 4. DEATH (4 frames, 6 FPS)
Sprite sheet: 256x64px (4 frames x 64px)
Animacao especial: "Pacoca Mental"

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Impacto: corpo jogado pra tras, bracos abertos. Rivotril voa da mao (projetil separado 32x32). Expressao de choque. Livro cai. |
| 2     | Desabando: joelhos dobram, terno amassa. Rosto fica TRAVADO numa expressao vazia. Olhos arregalados. Gravata solta. |
| 3     | No chao: corpo de lado, boca se move repetindo "pacoca". Bolha de fala com "pacoca..." (8x6px acima). Veias ainda pulsando fracamente. |
| 4     | Fade: mesma pose mas olhos fechando. Bolha de fala "pacoca..." ficando transparente. Veias param. Cores dessaturam 20%. |

**Nota**: Frame 3-4 duram mais (3 segundos no total antes de desaparecer). Apos death, trigger CANDIDATURA ETERNA: respawn com sprite "ressurreicao" (ver Special).

### 5. HIT (2 frames, 12 FPS)
Sprite sheet: 128x64px (2 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Recuo: corpo jogado 2px na direcao oposta ao hit. Rosto #CC3333 (irritado). Boca aberta xingando. Flash branco de 1 frame no corpo inteiro. Rivotril quase cai. |
| 2     | Recuperacao: volta a posicao, MAIS IRRITADO. Veias mais dilatadas que antes. Punho cerrado. Rosto #FF2222. |

### 6. SPECIAL: CIROCRACIA (8 frames, 8 FPS)
Sprite sheet: 512x64px (8 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Ciro levanta os bracos. Particulas azuis (#4169E1) comecam a surgir aos pes. |
| 2     | Energia sobe em espiral ao redor do corpo. Terno tremula. Cabelo se arrepia levemente. |
| 3     | Cupula de energia comeca a se formar (semi-esfera, 48x48px, translucida #4169E1 alpha 100). |
| 4     | Cupula completa: 56x56px ao redor de Ciro. Ciro dentro com pose de "eu sei de tudo". Bracos cruzados. |
| 5     | Cupula pulsa (expande 2px, contrai 2px). Inimigos proximos sao empurrados. Particulas circulam na borda. |
| 6     | Cupula comeca a rachar (linhas brancas na superficie). Ciro dentro fica surpreso. |
| 7     | Cupula instavel: pisca entre visivel e invisivel. Ciro em panico dentro. |
| 8     | Cupula estoura: fragmentos azuis voam (8-10 particulas). Ciro fica tonto, estrelinhas na cabeca. |

### 7. SPECIAL: RAGE DO RIVOTRIL (6 frames, 10 FPS)
Sprite sheet: 384x64px (6 frames x 64px)
Trigger: HP < 25%

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Ciro olha pro frasco: VAZIO. Olhos arregalados. Suor escorre. Mao treme. |
| 2     | Transicao pra panico: rosto vai de #D4956A pra #FF2222 em gradiente. Veias EXPLODEM no pescoco. Olhos ficam vermelhos (#FF0000). |
| 3     | FURIA: Ciro agarra o frasco vazio com as duas maos e comeca a girar. Motion blur circular ao redor. |
| 4     | Area damage: onda de choque circular (32px raio). Ciro no centro girando. Dano em tudo (inimigos E aliados). |
| 5     | Self-damage: Ciro cai tonto. Estrelas na cabeca (3 estrelas 4x4px girando). HP dele tambem diminui. |
| 6     | Recuperacao: Ciro de joelhos, respirando pesado. Rosto voltando lentamente pro normal. Veias ainda grossas. |

### 8. SPECIAL: CANDIDATURA ETERNA - Ressurreicao (4 frames, 6 FPS)
Sprite sheet: 256x64px (4 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Corpo no chao (pose de death frame 4). Brilho dourado comeca nas bordas. |
| 2     | Corpo levita 4px. Brilho se intensifica. Terno magicamente se ajusta. Gravata se endireita sozinha. |
| 3     | Ciro de pe, MENOR que antes (sprite 60x60 -> diminui 2px a cada morte). Olhos abertos, confuso. |
| 4     | Pose de "eu voltei": dedo apontando pro alto. Mas claramente mais fraco (cores 10% mais desbotadas que antes). |

### 9. SPECIAL: DEBATE UNILATERAL (4 frames, 8 FPS)
Sprite sheet: 256x64px (4 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Ciro para e abre os bracos. Xicara de cafe na mao direita. Boca aberta, pose de orador. |
| 2     | Gesticulacao: mao esquerda aponta pra frente. Bolha de fala grande aparece (16x12px) com "!@#$%". Inimigos ao redor ficam com "?" na cabeca. |
| 3     | Discurso intensifica: bolha de fala dobra de tamanho. Ciro fica vermelho. Cafe espirra da xicara. Aliados proximos com expressao de irritacao. |
| 4     | Fim: Ciro sorri satisfeito como se tivesse convencido alguem. Ninguem ao redor mudou de opiniao. Bolha some. |

### 10. SPECIAL: XINGAMENTO ERUDITO (4 frames, 10 FPS)
Sprite sheet: 256x64px (4 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Ciro inspira fundo. Peito expande 2px. Rosto vai ficando vermelho. |
| 2     | BOCA ABRE ENORME (cabeca deforma, boca ocupa 60% do rosto). Onda sonora visivel (linhas concentricas saindo da boca). |
| 3     | Texto "BOSSALOIDE!" ou "PATIFE!" em bold pixelado voa em direcao ao inimigo (projetil de texto 32x16px). |
| 4     | Inimigo stunado: estrelas ao redor. Ciro satisfeito, endireitando a gravata. |

### 11. SPECIAL: TERCEIRA VIA - Dash (4 frames, 12 FPS)
Sprite sheet: 256x64px (4 frames x 64px)

| Frame | Descricao                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| 1     | Ciro se prepara pra esquiva: corpo abaixa, olhar pro lado. |
| 2     | DASH: afterimage (ghost trail de 3 copias semi-transparentes). Corpo esticado na direcao do dash. |
| 3     | Afterimage ainda visivel. Ciro passa PELOS inimigos sem acertar nada (hitbox desligada). |
| 4     | Ciro para do outro lado. Olha pra tras confuso. Inimigos intactos. |

---

## BARRA DE RIVOTRIL (UI Element)

### Posicao
- Acima da cabeca do Ciro: 32x4px barra
- Ou no HUD se Ciro for selecionado

### Estados Visuais

| Nivel       | Cor da Barra | Comportamento do Sprite                      |
|------------|-------------|-----------------------------------------------|
| 100-75%    | #00BFFF     | Normal. Ciro calmo (relativamente).           |
| 75-50%     | #FFD700     | Ciro comeca a tremer (1px random offset/frame). Veias visiveis. |
| 50-25%     | #FF8C00     | Tremor intenso (2px). Rosto vermelho. Xingamentos aleatorios. |
| 25-1%      | #FF0000     | PANICO: tremor 3px, veias maximais, rosto berrante, suor excessivo. |
| 0%         | Vazio       | RAGE DO RIVOTRIL ativada automaticamente.     |

### Sprites da Barra
- Barra cheia: retangulo #00BFFF com borda #333333
- Barra diminuindo: gradiente da cor atual
- Barra vazia: retangulo vazio com borda vermelha PULSANTE
- Icone: mini frasco 8x8px ao lado esquerdo da barra

---

## PROJETEIS (32x32px)

### Frasco de Rivotril (arremesso)
- 4 frames de rotacao (girando no ar)
- Trail de liquido azul (#00BFFF) atras
- Impacto: explosao de liquido (6 goticulas em direcoes radiais)

### Texto-Projetil "BOSSALOIDE!"
- 32x16px, texto pixelado bold em vermelho (#FF0000)
- Onda sonora ao redor (linhas concentricas #FFD700)
- 2 frames de animacao (texto pisca/tremula)

### Texto-Projetil "PATIFE!"
- 32x16px, identico ao acima mas texto diferente
- Pode rotacionar variantes: "CANALHA!", "LIBERALZINHO!"

---

## EFEITOS DE PARTICULAS (por sprite)

| Efeito                | Tamanho   | Cor         | Quantidade | Contexto                    |
|-----------------------|-----------|-------------|------------|-----------------------------|
| Gotas de suor         | 2x3px     | #87CEEB     | 2-4        | Panico, raiva               |
| Veias pulsantes       | 1-2px     | #660066     | 3-4        | Sempre (intensidade varia)  |
| Vapor das orelhas     | 3x6px     | #FF6347     | 2          | Raiva maxima                |
| Estrelas de tontura   | 4x4px     | #FFD700     | 3          | Apos rage, hit              |
| Fragmentos de cupula  | 3x3px     | #4169E1     | 8-10       | Cirocracia quebra           |
| Particulas de energia | 2x2px     | #4169E1     | 12-16      | Cirocracia ativa            |
| Gotas de Rivotril     | 2x2px     | #00BFFF     | 4-6        | Impacto de frasco           |
| Fumaca de cafe        | 2x3px     | #FFFFFF a40 | 2-3        | Debate Unilateral           |
| Brilho de ressurreicao| 3x3px     | #FFD700     | 8-12       | Candidatura Eterna          |

---

## LAYOUT NO ATLAS (2048x2048px)

Posicao sugerida para sprites de Ciro no atlas compartilhado:

| Animacao              | Posicao no Atlas | Tamanho Total        |
|-----------------------|------------------|----------------------|
| Idle (4dir)           | (0, 512)         | 256x256px            |
| Walk (4dir)           | (256, 512)       | 384x256px            |
| Attack (4dir)         | (640, 512)       | 192x256px            |
| Death                 | (832, 512)       | 256x64px             |
| Hit (4dir)            | (0, 768)         | 128x256px            |
| Cirocracia            | (128, 768)       | 512x64px             |
| Rage Rivotril         | (640, 768)       | 384x64px             |
| Candidatura Eterna    | (1024, 768)      | 256x64px             |
| Debate Unilateral     | (0, 832)         | 256x64px             |
| Xingamento Erudito    | (256, 832)       | 256x64px             |
| Terceira Via          | (512, 832)       | 256x64px             |
| Projeteis             | (768, 832)       | 128x32px             |
| Particulas            | (896, 832)       | 64x64px              |
| Barra Rivotril        | (960, 832)       | 128x16px             |
