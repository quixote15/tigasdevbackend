# TRAMPI (Trump) - Especificacao Completa de Sprites

## Boss Internacional - "Zumbis de Brasilia"

---

## Visao Geral

- **Nome no Jogo**: Trampi
- **Tipo**: Boss Internacional (4/5 potencial)
- **Dimensao do Sprite**: 64x64px
- **Layout da Sprite Sheet**: Strip horizontal, 1 linha por animacao
- **Total de Frames**: 23 frames base + 16 frames especiais = 39 frames
- **Formato**: PNG com alpha transparency
- **Anchor Point**: Bottom-center (32, 60) -- centro dos pes
- **Direcoes**: Sprite virado para direita (flip horizontal para esquerda)

---

## Paleta de Cores

| Elemento                  | Hex Code    | Uso                                        |
|---------------------------|-------------|--------------------------------------------|
| Pele Laranja NEON         | `#FF6B00`   | Rosto, maos microscopicas, pescoco          |
| Pele Laranja Highlight    | `#FF9933`   | Highlights da pele, glow effect             |
| Pele Laranja Shadow       | `#CC4400`   | Sombras da pele, cross-hatching             |
| Pele Glow (emissivo)      | `#FFAA33`   | Glow externo 1px ao redor da pele, 40% op. |
| Cabelo Laranja            | `#FF8C00`   | Volume principal do cabelo-ninho            |
| Cabelo Highlight          | `#FFB347`   | Mechas soltas, brilho                       |
| Cabelo Shadow             | `#CC6600`   | Base do cabelo, sombras internas            |
| Cabelo Fios Soltos        | `#FFCC66`   | Fios individuais saindo do ninho            |
| Terno Dourado             | `#DAA520`   | Corpo do terno oversized                    |
| Terno Dourado Light       | `#FFD700`   | Highlights do terno, costuras               |
| Terno Dourado Dark        | `#B8860B`   | Sombras do terno, dobras                    |
| Terno Dourado Brilho      | `#FFF8DC`   | Pontos de brilho metalico (1px)             |
| Gravata Vermelha          | `#CC0000`   | Gravata longa ate o joelho                  |
| Gravata Highlight         | `#FF1A1A`   | Brilho da gravata                           |
| Gravata Shadow            | `#8B0000`   | Sombras e dobras da gravata                 |
| Camisa Branca             | `#F5F5DC`   | Camisa sob o terno (visivel no colarinho)   |
| Sapato Preto              | `#1A1A1A`   | Sapatos sociais                             |
| Sapato Highlight          | `#333333`   | Brilho do sapato                            |
| Outline Principal         | `#0D0D0D`   | Linhas grossas 2-4px irregulares            |
| Outline Secundario        | `#1A1A1A`   | Detalhes internos                           |
| Sombra Chao               | `#0D0D0D`   | Drop shadow, 40% opacity                   |
| Dentes (sorriso bully)    | `#FFFFCC`   | Dentes grandes, irregulares                 |
| Olhos Brancos             | `#FFFFFF`   | Esclerotica                                 |
| Iris Azul Claro           | `#87CEEB`   | Iris pequena, quase perdida no branco       |
| Pupila                    | `#000000`   | Pupila contraida (bully stare)              |

---

## Anatomia do Personagem (Proporcoes Andre Guedes)

### Estrutura Geral (5 cabecas de altura, atarracado)
- **Cabeca + Cabelo**: 20px de altura (cabelo-ninho ocupa 10px no topo, craneo 10px)
- **Cabelo-Ninho**: 18px de largura -- ENORME, volumoso, formato de ninho de passarinho, fios saindo em todas as direcoes, 3-4 fios individuais escapando (1px cada)
- **Rosto**: Laranja NEON fluorescente. Queixo duplo pronunciado (4px de queixo extra). Boca larga em formato de "O" arrogante ou sorriso de bully. Olhos pequenos e apertados (2x2px cada), sobrancelhas loiras finas. Nariz bulboso (3x3px).
- **Torso**: 20px de altura, 24px de largura -- OVERSIZED. Terno dourado absurdamente grande, ombros desproporcionais (4px alem do corpo real). Terno brilha com pontos de 1px dourado-claro espalhados. Gravata vermelha SAI do colarinho e desce ate o joelho (ponto Y=48).
- **Maos MICROSCOPICAS**: 3x3px MAXIMO. Sao patologicamente pequenas. Dedos individuais nao sao visiveis -- sao apenas blobs arredondados cor-de-laranja-neon. As maos ficam perdidas nas mangas oversized do terno. Cada mao tem 1px de glow laranja ao redor.
- **Pernas**: 16px de altura. Curtas em relacao ao torso. Calcas do terno dourado. Sapatos pretos brilhantes.
- **Glow Effect**: 1px de borda semi-transparente (#FFAA33, 40% opacity) ao redor de TODA a pele exposta (rosto, maos). Simula o autobronzeador industrial. Em frames de idle, o glow pulsa levemente.

### Deformidade Anatomica Principal: MAOS MICROSCOPICAS
- As maos sao a piada central. Em 64x64px, cada mao tem 3x3px no MAXIMO.
- As mangas do terno sao largas (6px de abertura) e as maos mal aparecem na ponta.
- Em certos frames, as maos tentam agarrar objetos e FALHAM -- o objeto escorrega/cai.
- O contraste entre o corpo ENORME e as maos MINUSCULAS deve ser o mais gritante possivel.

---

## Animacao IDLE (4 frames)

### Sprite Sheet: `trump_idle.png` -- 256x64px

#### Frame 0: Idle Base - "Power Stance"
- **Posicao**: 0,0 a 63,63
- **Descricao**: Trampi em pe, pernas levemente afastadas (power stance presidencial). Corpo virado 3/4 para a direita. Terno dourado oversized com ombros exagerados. Gravata vermelha pendurada ate o joelho, levemente torta. Cabelo-ninho volumoso, 2 fios escapando para a direita. Rosto laranja NEON com glow de 1px. Expressao de bully: olhos apertados, boca em "smirk" assimetrico mostrando 3 dentes no canto direito. Queixo duplo proeminente. Maos microscopicas penduradas nas laterais -- quase invisiveis saindo das mangas enormes. Mao direita tenta segurar a gravata mas os dedos sao pequenos demais, a gravata escorrega. Sombra no chao: elipse 20x6px, 40% opacity.
- **Cross-hatching**: Sombra sob o queixo (3 linhas diagonais 1px), sombra interna do terno nos flancos (4 linhas verticais 1px), textura do cabelo (linhas curvas irregulares).

#### Frame 1: Idle Puff - "Ego Inflate"
- **Posicao**: 64,0 a 127,63
- **Descricao**: Trampi infla o peito 2px para fora (ego inflando). Ombros sobem 1px. Queixo se levanta 1px. Cabelo-ninho treme levemente -- 1 fio muda de posicao. Glow da pele INTENSIFICA para 2px por 1 frame. Boca abre levemente mais (arrogancia crescendo). Maos microscopicas fazem um gesto de "palmas abertas" -- tentam abrir mas sao tao pequenas que parecem apenas blobs tremendo. Gravata balanca 1px para a esquerda com o movimento do peito.
- **Detalhe tecnico**: O glow laranja pulsa de 40% para 60% opacity neste frame.

#### Frame 2: Idle Adjust - "Fix the Tie"
- **Posicao**: 128,0 a 191,63
- **Descricao**: Trampi tenta ajustar a gravata com a mao direita microscopica. A mao se move ate a gravata (animacao de alcance) mas os dedos sao PEQUENOS DEMAIS para agarrar. A gravata escorrega entre os micro-dedos. Expressao muda levemente -- sobrancelha direita sobe 1px (frustacao breve). Cabelo-ninho se acomoda, fios voltam a posicao original. Peito volta ao tamanho normal. Glow retorna a 40%.
- **Detalhe das maos**: A mao direita tem 3x3px. Ao tentar pegar a gravata (que tem 4px de largura no ponto de contato), os pixels da mao se sobrepoe mas nao "fecham" ao redor -- visualmente claro que nao consegue agarrar.

#### Frame 3: Idle Smug - "Tremendous Pose"
- **Posicao**: 192,0 a 255,63
- **Descricao**: Trampi faz o gesto icônico com AMBAS as maos microscopicas -- tenta fazer o "OK sign" (polegar+indicador formando circulo) mas as maos sao tao pequenas que o gesto e ilegivel. Parece apenas dois blobs laranja tremendo na frente do peito. Boca em formato de "O" pronunciando algo (provavelmente "TREMENDOUS"). Olhos mais abertos que nos outros frames (2x3px). Cabelo-ninho vibra com a energia do gesto. Gravata balanca 2px. 1 ponto de brilho extra no terno (1px dourado-claro no ombro).
- **Particulas**: 2 sparkles dourados (1x1px, #FFD700) flutuam ao redor das maos -- satirizando o "brilho" que ele acha que tem.

---

## Animacao WALK (6 frames)

### Sprite Sheet: `trump_walk.png` -- 384x64px

#### Frame 0: Walk - Passo Direito (Contato)
- **Posicao**: 0,0 a 63,63
- **Descricao**: Pe direito toca o chao. Perna direita esticada a frente, perna esquerda atras. O corpo INTEIRO se inclina 2px para a direita com o peso (andar pesado de boss). Terno dourado balanca -- a aba direita do terno se abre 3px mostrando o forro (dourado mais escuro). Gravata balanca para a esquerda (inercia). Cabelo-ninho se deforma 1px para a esquerda (contra o movimento). Maos microscopicas balancam nos lados -- a mao direita a frente, a esquerda atras, ambas pateticamente pequenas contra as mangas enormes. Expressao: bully determinado, olhos fixos para frente.
- **Sombra**: Elipse no chao se deforma levemente com o passo.

#### Frame 1: Walk - Passo Direito (Meio)
- **Posicao**: 64,0 a 127,63
- **Descricao**: Peso transferindo. Corpo se levanta 1px (fase de impulso). Perna esquerda passando pela direita. Terno se fecha levemente. Gravata no centro, vertical. Cabelo-ninho volta ao centro. Maos cruzam o centro do corpo -- tao pequenas que quase desaparecem atras do terno. Um botao dourado do terno brilha (1px branco).
- **Detalhe**: Cross-hatching nas dobras do terno na regiao da cintura (2 linhas diagonais).

#### Frame 2: Walk - Passo Direito (Elevacao)
- **Posicao**: 128,0 a 191,63
- **Descricao**: Pe direito se levanta do chao. Corpo no ponto mais alto do ciclo (+2px). Terno "flutua" levemente -- barra inferior sobe 1px. Gravata estica verticalmente (gravidade). Cabelo-ninho comprime 1px verticalmente (inércia). Maos nos lados, mao esquerda comecando a ir para frente. Sapato direito mostra a sola brevemente (1px de detalhe).
- **Glow**: Pele glow normal a 40%.

#### Frame 3: Walk - Passo Esquerdo (Contato)
- **Posicao**: 192,0 a 255,63
- **Descricao**: Espelho do Frame 0 mas com pe esquerdo. Corpo inclina 2px para a esquerda. Aba esquerda do terno se abre. Gravata para a direita. Cabelo para a direita. Mao esquerda a frente, direita atras. DETALHE ESPECIAL: neste frame, a mao direita microscopica tenta segurar a aba do terno que esta abrindo -- mas os dedos sao pequenos demais e a aba escapa. Expressao identica ao Frame 0.

#### Frame 4: Walk - Passo Esquerdo (Meio)
- **Posicao**: 256,0 a 319,63
- **Descricao**: Espelho do Frame 1. Peso transferindo. Corpo sobe 1px. Perna direita passando pela esquerda. Tudo centralizado momentaneamente. Gravata vertical. Cross-hatching nas dobras do terno (2 linhas).

#### Frame 5: Walk - Passo Esquerdo (Elevacao)
- **Posicao**: 320,0 a 383,63
- **Descricao**: Espelho do Frame 2. Pe esquerdo levantando. Corpo no ponto alto. Terno flutua. Completa o ciclo -- loop volta ao Frame 0.

---

## Animacao ATTACK (3 frames)

### Sprite Sheet: `trump_attack.png` -- 192x64px

#### Frame 0: Attack - Wind-up "Executive Order"
- **Posicao**: 0,0 a 63,63
- **Descricao**: Trampi puxa o braco direito para tras (preparando swing do taco de golfe OU soco executivo). O terno se ESTICA na direcao do braco -- costuras visualmente forçadas (2-3 linhas de tensao no ombro, 1px cada). Corpo rotaciona 15 graus no sentido horario. Perna esquerda a frente como pivot. Cabelo-ninho se achata do lado direito com o movimento (deformacao organica, estilo Andre Guedes). Gravata voa para a esquerda com a rotacao. Rosto: boca aberta em grito, mostrando todos os dentes (5 dentes irregulares, #FFFFCC). Olhos arregalados com furia.
- **Maos**: A mao direita microscopica tenta segurar o taco de golfe. Os 3x3px da mao mal cobrem a empunhadura. Ha 50% de chance visual de o taco estar "escorregando" -- neste frame, 1px de gap entre mao e taco.
- **Motion lines**: 2 linhas de movimento (1px, branco 30% opacity) atras do braco.

#### Frame 1: Attack - Swing "TREMENDOUS Hit"
- **Posicao**: 64,0 a 127,63
- **Descricao**: Trampi no auge do swing. Corpo girou 30 graus. Braco direito estendido a frente em arco. Taco de golfe (se visivel) em blur de movimento. Terno DEFORMADO pelo movimento -- ombro direito 4px a frente do normal, botoes parecem a ponto de estourar (1px de gap entre botoes). Cabelo-ninho se deforma no sentido oposto ao movimento -- alonga 3px para a esquerda como se fosse ser arrancado pelo vento. Gravata enrolada ao redor do torso pela rotacao. Rosto: grito maximo, boca 4px de abertura, queixo duplo tremendo.
- **Particulas de impacto**: 3 sparkles dourados (1x1px) irradiam do ponto de ataque.
- **Maos**: Mao direita em desfoque (2x2px blur). Mao esquerda tenta se segurar no terno mas escorrega.

#### Frame 2: Attack - Follow-through "Believe Me"
- **Posicao**: 128,0 a 191,63
- **Descricao**: Pos-impacto. Corpo continua a rotacao e para em pose dramatica. Braco direito estendido alem do corpo, taco (se presente) apontando para o chao apos completar o arco. Terno comeca a se reacomodar mas ainda deformado. Cabelo-ninho voltando ao normal com 1 frame de bounce (comprime e expande). Gravata desenrolando. Rosto: sorriso satisfeito, smirk assimetrico, 1 olho mais aberto que o outro (wink de bully). Queixo projetado para frente (arrogancia pos-ataque).
- **Texto flutuante**: Pequeno texto "TREMENDOUS!" aparece acima da cabeca (5px de altura, letras irregulares, #FFD700 com outline preto 1px). Aparece neste frame e desaparece.
- **Maos**: Mao direita soltou o taco (ou esta aberta em gesto de "ta-da"). Mao esquerda faz thumbs up microscopico (praticamente invisivel).

---

## Animacao DEATH (4 frames)

### Sprite Sheet: `trump_death.png` -- 256x64px

#### Frame 0: Death - Hit Inicial "Impeachment Incoming"
- **Posicao**: 0,0 a 63,63
- **Descricao**: Trampi recebe golpe fatal. Corpo se curva para tras em arco. Cabelo-ninho EXPLODE parcialmente -- 4-5 fios individuais se soltam e voam (1px cada, laranja). O terno começa a se desfazer -- 1 botao dourado salta (2x2px, com motion line). Gravata chicoteia para cima. Rosto: CHOQUE ABSOLUTO. Boca aberta oval (5px), olhos arregalados (3x3px, os maiores que ficam em toda a sprite sheet). Pele laranja INTENSIFICA o glow para 3px (reacao de dor ao estilo neon). Maos microscopicas se levantam em gesto de "nao!" -- tao pequenas que parece desespero patetico.
- **Particulas**: 2 botoes dourados voando, 3 fios de cabelo, 1 estrela de dor (3x3px amarela) acima da cabeca.

#### Frame 1: Death - Queda "Covfefe"
- **Posicao**: 64,0 a 127,63
- **Descricao**: Trampi caindo para tras. Angulo do corpo 45 graus com o chao. Cabelo-ninho se separa parcialmente da cabeca -- revelando uma careca rosada embaixo (2px de careca visivel, #FFB6C1). MOMENTO DE HUMILHACAO MAXIMA: O cabelo era parcialmente postico. Terno se abre completamente mostrando camisa branca manchada de ketchup (2-3 pontos vermelhos #CC0000 na camisa). Gravata enrolada no rosto. Maos microscopicas tentam inutilmente agarrar o ar -- parecem pes de passarinho desesperados.
- **Detalhe crucial**: A CARECA aparecendo sob o cabelo e o momento comico maximo. Apenas 2px para sugerir, mas suficiente.
- **Particulas**: Mais fios de cabelo voando, botoes, sparkles dourados sumindo.

#### Frame 2: Death - Chao "You're Fired"
- **Posicao**: 128,0 a 191,63
- **Descricao**: Trampi no chao, deitado de costas. Corpo horizontal na parte inferior do frame (Y 40-60). Terno espalhado ao redor como poça dourada. Cabelo-ninho desgrenhado, parcialmente descolado, revelando mais careca. Gravata jogada sobre o rosto cobrindo um olho. O olho visivel esta em formato de "X" (nocauteado). Boca aberta com 1 dente caido (dente voando como particula 2x2px). Maos microscopicas apontam para cima, rigidas, como patas de inseto morto. Sapatos descolaram dos pes (1 sapato voando, 2x3px).
- **Cross-hatching**: Sombra pesada sob o corpo no chao (5 linhas horizontais irregulares).

#### Frame 3: Death - Final "Fake News"
- **Posicao**: 192,0 a 255,63
- **Descricao**: Trampi completamente derrotado. Corpo comeca a ficar semi-transparente (80% opacity). O glow laranja da pele APAGA -- a pele muda de #FF6B00 para #CC9966 (revela que o laranja era tudo bronzeador, a pele real e palida). O cabelo-ninho encolhe e murcha (de 18px para 10px de largura). Terno perde o brilho dourado, fica amarelo opaco (#CCCC66). Gravata descolorida. O MAIS IMPORTANTE: As maos microscopicas finalmente ficam PROPORCIONAIS ao corpo -- porque o corpo encolheu. Ironia final.
- **Texto flutuante**: "FAKE NEWS..." aparece e desaparece lentamente acima do corpo (fade out, 6px de altura, vermelho #CC0000, italico irregular).
- **Efeito**: Todo o sprite faz fade para 0% opacity apos este frame (4 frames de fade handled pelo engine).

---

## Animacao HIT (2 frames)

### Sprite Sheet: `trump_hit.png` -- 128x64px

#### Frame 0: Hit - Reacao "Not Fair!"
- **Posicao**: 0,0 a 63,63
- **Descricao**: Trampi recebe dano. Corpo empurrado 3px para tras. Cabeca se joga para tras (whiplash). Cabelo-ninho deforma na direcao oposta ao hit (stretcha 3px). Terno vibra -- outline do terno duplica por 1px (efeito de vibracao/blur). Boca em formato de "O" de dor/indignacao. Olhos SQUEEZE shut (1x1px, linhas). Queixo duplo balanca. Pele laranja FLASHA para branco por 50% do frame (efeito de hit flash padrao). Maos microscopicas se levantam defensivamente -- mas sao tao pequenas que nao protegem nada.
- **Particulas**: 2 estrelas de dor (2x2px, amarelas), 1 fio de cabelo se solta.
- **Glow**: Pele glow muda de laranja para branco (#FFFFFF) durante o flash.

#### Frame 1: Hit - Recuperacao "This is Unfair"
- **Posicao**: 64,0 a 127,63
- **Descricao**: Trampi se recupera. Corpo volta para frente. Cabelo-ninho faz bounce (comprime 2px, depois volta). Expressao muda de dor para RAIVA: sobrancelhas descem, boca se fecha em linha fina, olhos se estreitam mais que o normal (1x2px, slots de furia). Pele volta ao laranja NEON com glow intensificado temporariamente (60% opacity por 1 frame). Terno se reacomoda. Maos microscopicas fecham em "punhos" -- que parecem apenas 2x2px blobs.
- **Detalhe expressivo**: A transicao de dor para raiva deve ser ABRUPTA (estilo twitchy, nao suave). O rosto pula de "surpresa" para "furia" sem transicao.

---

## Animacoes SPECIAL (Detalhadas em animation-spec.md)

### Resumo dos frames especiais necessarios:

#### Special 1: "Build the Wall" (4 frames)
- Sprite Sheet: `trump_special_wall.png` -- 256x64px
- Frame 0: Trampi planta os pes e estende as maos microscopicas
- Frame 1: Tijolos dourados comecam a subir do chao (particulas 4x4px)
- Frame 2: Muro se forma (asset separado, 128x32px) com "TRUMP" em letras douradas
- Frame 3: Trampi aponta para o muro com orgulho, mao microscopica mal visivel

#### Special 2: "Fake News Presidential" (4 frames)
- Sprite Sheet: `trump_special_fakenews.png` -- 256x64px
- Frame 0: Trampi pega celular (mao microscopica derruba 1 vez)
- Frame 1: Tela de celular brilha, "FAKE NEWS!" em vermelho
- Frame 2: Ondas de distorcao emanam do celular (3 circulos concentricos)
- Frame 3: Trampi sorri satisfeito, textos do HUD comecam a mudar

#### Special 3: "Sancao Economica" (4 frames)
- Sprite Sheet: `trump_special_sancao.png` -- 256x64px
- Frame 0: Trampi assina decreto executivo (mao microscopica mal segura a caneta)
- Frame 1: Documento voa com selo dourado
- Frame 2: Correntes economicas (sprites 4x4px) envolvem o alvo
- Frame 3: Alvo fica com efeito de slowdown (sprites azulados)

#### Special 4: "AMERICA FIRST" - Ultimate (8 frames)
- Sprite Sheet: `trump_special_ultimate.png` -- 512x64px
- Frame 0: Trampi levanta AMBAS as maos microscopicas para o ceu
- Frame 1: Ceu escurece, filtro azul-vermelho começa
- Frame 2: Aguias de aco dourado descem (sprites separados 32x32px)
- Frame 3: Explosoes patrioticas (starburst azul-branco-vermelho)
- Frame 4: Bandeiras americanas brotam do chao (sprites 16x32px)
- Frame 5: Trampi em pose de poder, vento soprando cabelo e gravata
- Frame 6: Flash branco maximo (tela 80% branca)
- Frame 7: Retorno ao normal, Trampi em power pose, tudo destruido ao redor

---

## Sprite Sheet de Maos Microscopicas (Asset Especial)

### Sprite Sheet: `trump_microhands.png` -- 192x16px (12 frames de 16x16px)

As maos tem seu proprio sprite sheet para overlay, permitindo animacao independente.

| Frame | Nome              | Descricao                                                   |
|-------|-------------------|-------------------------------------------------------------|
| 0     | hand_idle         | Mao pendurada, 3x3px blob laranja neon                     |
| 1     | hand_grab_try     | Mao tentando fechar (2x3px, esticada)                      |
| 2     | hand_grab_fail    | Mao falhando, objeto escorregando (3x2px, aberta)          |
| 3     | hand_drop         | Mao aberta, objeto caindo (2x2px, dedos separados)         |
| 4     | hand_point        | Mao apontando (3x2px, 1px esticado como "dedo")            |
| 5     | hand_ok_attempt   | Tenta fazer OK sign (3x3px, circulo impossivel)             |
| 6     | hand_fist         | Punho fechado (2x2px blob)                                  |
| 7     | hand_wave         | Acenar (3x3px, blur de 1px no topo)                        |
| 8     | hand_thumbsup     | Thumbs up microscopico (3x4px, 1px para cima)              |
| 9     | hand_grab_success | RARO: Consegue segurar algo (3x3px apertado ao redor)       |
| 10    | hand_tremble      | Mao tremendo (alternancia 2x3px / 3x2px)                   |
| 11    | hand_dead         | Mao rigida, pata de inseto morto (2x3px, dedos para cima)  |

---

## Sprite do Cabelo-Ninho (Asset Especial)

### Sprite Sheet: `trump_hair.png` -- 128x16px (8 frames de 16x16px)

O cabelo tem animacao independente para reacoes a vento, impacto e emocao.

| Frame | Nome               | Descricao                                                  |
|-------|--------------------|-------------------------------------------------------------|
| 0     | hair_normal        | Ninho intacto, volumoso, 2 fios escapando                  |
| 1     | hair_wind_right    | Vento para direita, ninho deforma 3px, 4 fios voando       |
| 2     | hair_wind_left     | Espelho do frame 1                                         |
| 3     | hair_impact        | Ninho achata com impacto, alarga 2px                       |
| 4     | hair_puff          | Ninho infla (ego), +2px em todas direcoes                  |
| 5     | hair_messy         | Ninho desgrenhado, fios para todos os lados                |
| 6     | hair_detach        | Ninho parcialmente descolado, revelando careca             |
| 7     | hair_gone          | So a careca rosada, ninho como objeto caindo separado      |

---

## Efeito de Glow da Pele (Implementacao Tecnica)

O glow da pele laranja fluorescente e implementado como:

1. **Layer base**: Sprite normal do personagem
2. **Layer glow**: Copia do outline da pele exposta, expandida 1px, cor #FFAA33, opacity pulsante:
   - Idle: 30% -> 50% -> 30% (ciclo de 2 segundos)
   - Hit: Flash para 100% branco, depois volta
   - Death: Fade de 50% para 0% (glow morre)
   - Attack: 60% constante (energia)
   - Ultimate: 100% constante + cor muda para azul-branco-vermelho alternante

---

## Notas para o Artista

1. **A PIADA E AS MAOS**: Se voce tiver que sacrificar detalhe em qualquer parte do sprite, NUNCA sacrifique a visibilidade das maos microscopicas. Elas devem ser SEMPRE visiveis (por serem absurdamente pequenas em contraste com o corpo enorme).

2. **O LARANJA E NEON**: A pele nao e um laranja qualquer. E FLUORESCENTE. Como se ele tivesse caido num tanque de autobronzeador industrial. O sprite deve BRILHAR. Use o glow layer.

3. **ESTILO ANDRE GUEDES**: Linhas irregulares, NUNCA perfeitamente retas. Cross-hatching nas sombras. Textura de papel sujo. Proporcoes grotescas. O terno dourado deve parecer CAFONA, nao elegante.

4. **OVERSIZED vs MICROSCOPICO**: O contraste e TUDO. Terno GIGANTE, cabelo ENORME, gravata COMPRIDA, ego INFLADO -- versus maos PATOLOGICAMENTE PEQUENAS. Este contraste visual e o humor inteiro do personagem.

5. **ANIMACAO TWITCHY**: Nenhuma transicao deve ser suave. Tudo e ABRUPTO, JERKY. O cabelo pula, o corpo treme, as expressoes mudam INSTANTANEAMENTE. 8fps maximo.

6. **REFERENCIA**: O Trampi do Andre Guedes nos videos de referencia tem pele absurdamente laranja, cabelo como algodao-doce mutante, e terno que parece roubado de um boneco de cera. SIGA ESSE CAMINHO.

---

## Phaser 3 Atlas Keys

```javascript
// Configuracoes de atlas para cada sprite sheet
const TRUMP_ATLAS = {
  idle:     { key: 'trump_idle',     frameWidth: 64, frameHeight: 64, frames: 4  },
  walk:     { key: 'trump_walk',     frameWidth: 64, frameHeight: 64, frames: 6  },
  attack:   { key: 'trump_attack',   frameWidth: 64, frameHeight: 64, frames: 3  },
  death:    { key: 'trump_death',    frameWidth: 64, frameHeight: 64, frames: 4  },
  hit:      { key: 'trump_hit',      frameWidth: 64, frameHeight: 64, frames: 2  },
  special_wall:     { key: 'trump_sp_wall',     frameWidth: 64, frameHeight: 64, frames: 4 },
  special_fakenews: { key: 'trump_sp_fakenews', frameWidth: 64, frameHeight: 64, frames: 4 },
  special_sancao:   { key: 'trump_sp_sancao',   frameWidth: 64, frameHeight: 64, frames: 4 },
  special_ultimate: { key: 'trump_sp_ultimate',  frameWidth: 64, frameHeight: 64, frames: 8 },
  microhands:       { key: 'trump_microhands',   frameWidth: 16, frameHeight: 16, frames: 12 },
  hair:             { key: 'trump_hair',          frameWidth: 16, frameHeight: 16, frames: 8  },
};
```
