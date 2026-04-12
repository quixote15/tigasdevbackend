# Gilmar Mendes — Sprite Specification

## Overview
- **Personagem**: Gilmar Mendes — Boss do STF / O Coringa do STF
- **Sprite Dimensions**: 64x64px
- **Sprite Sheet Layout**: Horizontal strip, 1 row por animacao
- **Format**: PNG com alpha transparency
- **Anchor Point**: Bottom-center (32, 60) — pes do personagem
- **Perspectiva**: Top-down levemente isometrica (Y-sorting)
- **Frame Rate**: 8-10 fps (jerky, estilo Andre Guedes — NUNCA fluido)

## Proporcoes do Personagem (dentro do frame 64x64)

O Gilmar ocupa aproximadamente 48x58px dentro do frame. Proporcoes grotescas Andre Guedes:

| Parte | Proporcao | Pixels Aprox | Notas |
|---|---|---|---|
| Cabeca + oculos | 40% da altura | ~24px | ENORME, desproporcional. Oculos ocupam 60% da cabeca |
| Papada tripla | Extensao da cabeca | ~8px abaixo do queixo | Tres camadas distintas de papada, tremem independentemente |
| Torso (toga) | 35% da altura | ~20px | Toga larga, manchada, bolsos estufados |
| Pernas | 15% da altura | ~10px | Curtissimas (velhinho baixinho) |
| Cabelo ralo | Topo da cabeca | ~4px | Penteado pro lado, fios contaveis (5-7 fios) |

## Paleta de Cores

| Elemento | Hex | Uso |
|---|---|---|
| Toga Preta Base | `#1A1A18` | Corpo da toga, manchada |
| Toga Preta Sombra | `#0D0D0D` | Dobras e sombras da toga |
| Toga Highlight | `#2A2A28` | Luz na toga (reflexo sutil) |
| Mancha Pastel (oleo) | `#C8A832` | Manchas gordurosas na toga |
| Mancha Pastel (molho) | `#8B4513` | Manchas de molho de carne |
| Migalha | `#D4A855` | Migalhas na toga e no chao |
| Pele Base | `#D4A574` | Rosto e maos (pele envelhecida) |
| Pele Sombra | `#A0785A` | Sombras na pele, rugas profundas |
| Pele Highlight | `#E8C8A0` | Destaques na pele (bochecha, testa) |
| Papada Rosa | `#C89880` | Papada tripla (mais rosada que o rosto) |
| Papada Sombra | `#A07868` | Sombras entre as camadas de papada |
| Oculos Armacao | `#5A3A1A` | Armacao marrom anos 70 ENORME |
| Oculos Lente | `#A8C8D8` | Lente com reflexo (semi-transparente) |
| Oculos Reflexo | `#FFFFFF` alpha 60% | Brilho cinico nas lentes |
| Cabelo Ralo | `#8A7A6A` | Fios ralos grisalhos |
| Sorriso/Dentes | `#E8D8B0` | Dentes amarelados (sorrisinho cinico) |
| Celular | `#2A2A2A` | Celular com tela brilhando |
| Tela Celular | `#40B840` | Tela do celular (contato Vorcaro visivel) |
| Dinheiro | `#3D8B3A` | Notas caindo do bolso |
| Dinheiro Highlight | `#5AAA5A` | Luz nas notas |
| Pastel Base | `#D4A040` | Corpo do pastel (dourado gorduroso) |
| Pastel Recheio | `#8B4513` | Recheio escorrendo |
| Pastel Oleo | `#C8A832` alpha 50% | Oleo escorrendo |
| Outline | `#1A1A18` | Contorno grosso 2-3px (Crumb style) |
| Documento HC | `#E8D8B0` | Documentos de habeas corpus |
| Documento Brilho | `#FFD700` | Aura dourada do habeas corpus |

---

## IDLE — 4 Frames (Loop)

**Sprite Sheet**: `gilmar_idle.png` — 256x64px (4 frames x 64px)

### Frame 0: Papada Tremendo
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Gilmar em posicao padrao, levemente inclinado pra frente (postura de velhinho). Oculos enormes anos 70 dominam o rosto — armacao grossa marrom, lentes que ocupam metade da cabeca. Papada tripla em repouso (3 camadas visiveis, a terceira quase toca o peito). Cabelo ralo penteado pro lado esquerdo (5-7 fios visiveis, grotescamente detalhados). Sorrisinho cinico permanente — canto direito da boca levantado. Toga preta com 3-4 manchas de oleo de pastel amarelado na frente. Bolso esquerdo estufado com notas de dinheiro (2-3 pixels verdes saindo). Mao direita segura meio pastel mordido. Mao esquerda segura celular (tela verde com texto minusculo "VORCARO"). Pes mal aparecem sob a toga comprida.
- **Detalhe tecnico**: A papada esta no ponto MAXIMO de extensao — esticada pra baixo pela gravidade. No frame seguinte vai subir (tremida).
- **Estilo**: Linhas de contorno de 2-3px, irregulares (mao humana). Cross-hatching nas sombras da papada e nas dobras da toga. Textura de papel sutil (noise 3%) sobre toda a sprite.

### Frame 1: Oculos Brilhando
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: IDENTICO ao Frame 0 com duas diferencas: (1) A papada sobe 2px — tremida involuntaria, a segunda camada comprime contra a primeira. (2) Reflexo branco nas lentes dos oculos INTENSIFICA — um flash de luz cinica. O reflexo e assimetrico: lente esquerda tem brilho redondo (4x4px branco 60% alpha), lente direita tem brilho menor (2x2px). Isso cria o efeito de "oculos brilhando com malicia" classico de vilao de anime adaptado ao grotesco.
- **Detalhe tecnico**: O brilho nos oculos comunica ao jogador que Gilmar esta "tramando algo". E o idle padrao de um personagem que NUNCA para de maquinar.

### Frame 2: Mordendo Pastel
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Gilmar leva o pastel a boca. A mao direita sobe 6px. O pastel encosta na boca — mandibula aberta mostrando 4-5 dentes amarelados. A papada se COMPRIME (as 3 camadas se amassam juntas, formando uma massa de carne rosada). Migalhas (3-4 pixels dourados) voam da boca em direcoes aleatorias. Oleo do pastel escorre na papada (1-2 pixels amarelos translucidos). O sorrisinho cinico se abre pra dar a mordida — vira um sorriso LARGO momentaneo. O celular na mao esquerda permanece visivel. Uma nota de dinheiro (2x4px verde) cai do bolso no momento da mordida (o corpo se mexe e solta a nota).
- **Detalhe tecnico**: Este frame DEFINE o personagem. Gilmar comendo pastel durante sessao do STF como se nada estivesse acontecendo. E a imagem iconica.

### Frame 3: Sorrisinho de Deboche
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Pos-mordida. Gilmar mastigando com a boca fechada. A papada volta a posicao original (3 camadas separadas novamente, tremida residual — 1px de deslocamento lateral). Os olhos se estreitam ATRAS dos oculos — pupilas menores, palpebras meio fechadas, expressao de "eu sei algo que voce nao sabe". O sorrisinho volta ao canto direito da boca (posicao padrao). Uma migalha grudada no canto da boca (1px dourado). O brilho dos oculos diminui em relacao ao Frame 1 mas NAO desaparece. Postura relaxa 1px pra tras.
- **Detalhe tecnico**: Este e o frame de "reset" do loop. A transicao Frame 3 -> Frame 0 deve ser quase imperceptivel. O loop inteiro comunica: "Gilmar parado, comendo, tramando, debochando. Repetir."

---

## WALK — 6 Frames (Loop)

**Sprite Sheet**: `gilmar_walk.png` — 384x64px (6 frames x 64px)

### Frame 0: Passo Direito — Impulso
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Gilmar inicia passo com pe direito. Corpo inclina levemente pra frente (2px). Perna direita avanca sob a toga (a toga deforma mostrando o joelho — protuberancia de 3px). Perna esquerda plantada. A toga balanca pra esquerda no movimento (assimetria de 3px). Manchas de pastel na toga sao visiveis durante o balanco. Dinheiro comeca a escorregar do bolso (nota aparece 3px mais pra fora que no idle). A papada tripla balanca na DIRECAO OPOSTA ao corpo (inercia — 2px pra tras). Celular na mao esquerda treme com o passo.
- **Estilo**: Movimento jerky. A transicao de idle pra walk deve parecer "cortada", nao suave.

### Frame 1: Passo Direito — Contato
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Pe direito toca o chao. IMPACTO. O corpo inteiro chacoalha 1px pra baixo (squash sutil). A papada DESPENCA (3 camadas comprimem violentamente, a terceira bate no peito). Os oculos deslizam 1px pra baixo no nariz. O pastel na mao direita sacode — 2 migalhas novas voam (pixels dourados). Uma nota de dinheiro se SOLTA do bolso e flutua 4px atras do Gilmar (nota de 3x5px verde, angulada 15 graus). A toga assenta no chao e levanta poeira sutil (2-3 pixels cinza-claro no chao).
- **Detalhe tecnico**: Este e o frame de IMPACTO de cada passo. A papada batendo no peito e o sound cue visual.

### Frame 2: Passo Direito — Recuperacao
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Corpo se ergue do squash (volta a altura normal). Peso transfere pro pe direito. A papada REBATE pra cima (bounce de 2px acima da posicao normal — as 3 camadas se separam e tremem). Os oculos voltam a posicao. A nota de dinheiro que caiu no Frame 1 agora esta 8px atras, caindo (quase no chao, angulada 30 graus). O sorrisinho cinico permanece INALTERADO durante toda a walk — Gilmar nao perde o deboche ao andar. O celular treme menos.

### Frame 3: Passo Esquerdo — Impulso
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: ESPELHO do Frame 0 mas pro lado esquerdo. Perna esquerda avanca, toga balanca pra DIREITA. A papada balanca pra direcao oposta (pra esquerda agora). DIFERENCA do Frame 0: uma NOVA mancha de pastel fica visivel na toga do lado direito (que estava escondida pelo angulo). O dinheiro do bolso esta mais folgado (nota 4px pra fora — prestes a cair). O pastel na mao direita esta 1px mais mordido que no Frame 0 (Gilmar COME ENQUANTO ANDA).

### Frame 4: Passo Esquerdo — Contato
- **Posicao no sheet**: 256,0 a 319,63
- **Descricao**: ESPELHO do Frame 1 pro lado esquerdo. Impacto do pe esquerdo. Squash de 1px. A papada DESPENCA novamente. Os oculos deslizam. DIFERENCA: desta vez DUAS notas de dinheiro caem do bolso (o segundo passo sacudiu mais). Nota 1 esta 8px atras (do passo anterior), Nota 2 acaba de sair (4px atras). Trilha de dinheiro se formando. O pastel perde mais uma migalha.

### Frame 5: Passo Esquerdo — Recuperacao
- **Posicao no sheet**: 320,0 a 383,63
- **Descricao**: ESPELHO do Frame 2. Corpo se ergue. Papada rebate. DIFERENCA FINAL: as duas notas estao no chao atras (quase fora do frame, desaparecendo — elas nao sao permanentes, sao efeito visual do walk cycle). O celular na mao esquerda mostra a tela brevemente mais brilhante (notificacao do Vorcaro — flash verde de 1 frame). Gilmar olha pro celular por 1px de rotacao da cabeca.
- **Detalhe tecnico**: O walk cycle completo comunica: velhinho baixinho andando pesado, toga suja balancando, dinheiro caindo, pastel sendo devorado, celular apitando. CADA PASSO deixa rastro de corrupcao.

---

## ATTACK — 3 Frames

**Sprite Sheet**: `gilmar_attack.png` — 192x64px (3 frames x 64px)

### Frame 0: Arremesso de Pastel (Wind-up)
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Gilmar puxa o braco direito pra tras, segurando o pastel como uma granada. O corpo rotaciona 20 graus pra direita. A toga estica na direcao do puxao. O sorrisinho cinico se abre num sorriso LARGO de prazer sadico — dentes amarelados todos visiveis. Os oculos brilham com reflexo INTENSO (flash branco em ambas as lentes). A papada se comprime do lado direito (o corpo puxou pra la). O celular na mao esquerda fica guardado no bolso da toga momentaneamente. O pastel na mao e GRANDE — desproporcional, 12x8px, gorduroso, escorrendo oleo.
- **Estilo**: Postura exagerada tipo pitcher de baseball. Um velhinho com vigor desproporcional.

### Frame 1: Toga Reflete Projetil (Teflon Flash)
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Frame de TRANSICAO que mostra a propriedade Teflon da toga. A toga do Gilmar BRILHA momentaneamente — um flash de energia percorre a superficie (3-4 pixels brancos 40% alpha formando uma onda da esquerda pra direita). E o visual de "nada gruda em mim". Ao mesmo tempo, o braco direito esta no meio do arremesso (angulo de 90 graus, pastel saindo da mao). Linhas de movimento (2 linhas brancas 40% alpha) acompanham o pastel. A papada sacude violentamente com o movimento do arremesso. Migalhas explodem do pastel em arco (5-6 pixels dourados em semicirculo). O sorriso atinge MAXIMO de largura.
- **Detalhe tecnico**: Este frame aparece brevemente (1/10s) e comunica DUAS coisas: o ataque ofensivo (pastel voando) e a defesa passiva (toga Teflon). E o frame mais "cheio" de informacao visual.

### Frame 2: Gargalhada Pos-Ataque
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Follow-through do arremesso. Braco direito estendido na direcao do alvo. A mao esta vazia (pastel ja foi). O corpo esta inclinado pra frente (2px) pelo impulso. MAS O IMPORTANTE: Gilmar esta GARGALHANDO. Boca aberta 180 graus (exagero grotesco), papada tripla tremendo descontroladamente (cada camada vibrando independentemente, 1-2px de deslocamento aleatorio entre elas). Os oculos subiram no nariz com a forca da risada (2px acima da posicao normal). Olhos fechados de tanto rir (arcos invertidos). Linhas de impacto da risada irradiam da boca (3 linhas curvas, 1px, brancas 30% alpha). O sorrisinho cinico virou GARGALHADA ABERTA — a essencia do Gilmar e que ele se DIVERTE causando caos.
- **Detalhe tecnico**: A transicao do attack de volta pro idle deve mostrar Gilmar "se recompondo" da risada. O deboche e a marca registrada ate no combate.

---

## DEATH — 4 Frames (NAO faz loop — sequencia unica)

**Sprite Sheet**: `gilmar_death.png` — 256x64px (4 frames x 64px)

### Frame 0: Impacto Mortal — Oculos Deslocam
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: O golpe fatal acertou. O corpo de Gilmar se inclina 10 graus pra tras. OS OCULOS SAO O FOCO: eles saem do rosto 4px, angulados 15 graus, como se tivessem sido arrancados pelo impacto. Uma lente racha (1px de linha diagonal na lente esquerda). A papada tripla ESTICA pra frente (inercia — o corpo foi pra tras mas a papada segue adiante). O sorrisinho permanece — Gilmar AINDA esta debochando mesmo levando o golpe fatal. O pastel cai da mao (4px abaixo e 2px a direita). O celular cai da outra mao (3px abaixo e 3px a esquerda, tela ainda brilhando com "VORCARO").
- **Estilo**: Momento de camera lenta visual. Cada pixel de deslocamento deve ser sentido.

### Frame 1: Queda — Papada Murcha
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Gilmar cai pra tras. Angulo de 30 graus. As pernas saem debaixo da toga (visiveis pela primeira vez — magras e curtas, desproporcao maxima com o torso). A PAPADA MURCHA: as 3 camadas colapsam uma sobre a outra, perdendo volume (de 8px de extensao para 4px), como se fosse um balao esvaziando. A pele da papada fica MAIS cinzenta (perda de vitalidade — pixels de pele mudam de `#D4A574` para `#B8A090`). Os oculos agora estao a 10px do rosto, girando no ar (angulo de 45 graus). O pastel no chao se desmonta (massa, recheio e oleo se separam em 3 elementos visuais). Documentos de habeas corpus comecam a sair dos bolsos da toga (3-4 retangulos brancos-amarelados, 3x5px cada, voando em direcoes aleatorias).
- **Detalhe tecnico**: A papada murchando e o equivalente visual da careca do Xandao "apagando". E O SINAL de que Gilmar esta morrendo.

### Frame 2: Colapso — Toga Vira Pasteis
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Gilmar quase no chao (angulo de 60 graus). A toga comeca a se TRANSFORMAR: o tecido preto se fragmenta em formas douradas — pasteis. A toga esta virando uma PILHA DE PASTEIS literalmente. Pixels pretos da toga (`#1A1A18`) se convertem em pixels dourado-gorduroso (`#D4A040`). Neste frame, 40% da toga ja virou pastel. O rosto do Gilmar e visivel entre os pasteis — e o SORRISINHO ainda esta la. Ate morrendo, debochando. Os oculos estao no chao a 15px do corpo, lentes rachadas, mas com um ultimo brilho de reflexo (1px branco numa lente). O celular no chao mostra tela rachada mas AINDA LIGADO — "VORCARO" piscando. Notas de dinheiro flutuam por todo o frame (8-10 pixels verdes em posicoes aleatorias, simulando uma chuva de dinheiro saindo dos bolsos enquanto a toga se desfaz).
- **Detalhe tecnico**: O visual de "toga virando pasteis" e SURREAL e define a morte do Gilmar. Nao e uma morte normal — e uma metamorfose grotesca.

### Frame 3: Final — Pilha de Pasteis + Oculos
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Gilmar SUMIU. No lugar dele: uma PILHA DE PASTEIS grotescos (7-8 pasteis sobrepostos, todos dourados e gordurosos, oleo escorrendo formando poca no chao). Sobre a pilha, OS OCULOS — perfeitos em cima da pilha, intactos agora (as rachaduras sumiram), com reflexo cinico brilhando como se o Gilmar AINDA estivesse vivo la dentro, olhando, debochando. Ao lado da pilha: celular com tela "VORCARO — Chamada Perdida (3)". Notas de dinheiro espalhadas ao redor (5-6 notas no chao). Um unico documento de habeas corpus dourado, brilhando, flutuando 2px acima da pilha (como se fosse um espirito do Gilmar tentando se soltar — mas um habeas corpus pra si mesmo). Migalhas formando um circulo ao redor.
- **Detalhe tecnico**: Este e o "corpo" que fica no mapa. E iconica: pilha de pasteis com oculos. O jogador VE e sabe: "matei o Gilmar". O habeas corpus dourado flutuante pode ser um collectible.

---

## HIT — 2 Frames

**Sprite Sheet**: `gilmar_hit.png` — 128x64px (2 frames x 64px)

### Frame 0: Oculos Torcem
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Gilmar tomou dano. O corpo faz um micro-recuo de 2px. MAS A PIADA: em vez de expressao de dor, Gilmar faz cara de INDIGNACAO DIVERTIDA. Como se alguem tivesse cometido uma falta de educacao. Os oculos TORCEM — armacao entorta 10 graus (lente esquerda mais alta que a direita). A papada tripla VIBRA lateralmente (as 3 camadas se deslocam 2px pra esquerda, fora de sincronia entre si — efeito de gelatina). O sorrisinho cinico permanece mas com um toque de surpresa (sobrancelha esquerda levanta 2px). Flash branco (hit flash) de 1px de borda ao redor do personagem todo (30% alpha). A toga ondula com o impacto. O pastel na mao espirra oleo (2 pixels amarelos pra frente).
- **Detalhe tecnico**: Gilmar NAO demonstra dor. Demonstra INDIGNACAO. Como se o hit fosse um insulto social, nao um ataque fisico.

### Frame 1: Papada Chacoalha (Recuperacao)
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Recuperacao do hit. O corpo volta a posicao normal. Os oculos voltam a posicao (com micro-atraso — ainda 3 graus tortos, corrigindo). A papada faz o CHACOALHO DE RECUPERACAO: as 3 camadas balancam pra direita (oposto do Frame 0), criando efeito de pendulo de carne. A segunda camada chega depois da primeira, a terceira depois da segunda (onda de papada). O sorriso AUMENTA — agora e um sorriso de desafio: "E so isso?" Os oculos voltam ao brilho cinico. O flash branco desaparece. A toga volta ao repouso. Gilmar retorna ao idle com a mensagem visual clara: "Isso nao me afetou."
- **Detalhe tecnico**: A transicao hit -> idle deve ser RAPIDA (2 frames = ~0.2s a 10fps). Gilmar se recupera rapido porque NADA o abala.

---

## SPECIAL 1: HABEAS CORPUS TRIPLO — 4 Frames

**Sprite Sheet**: `gilmar_special_habeas.png` — 256x64px (4 frames x 64px)

### Frame 0: Puxa Documento #1
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Gilmar mergulha a mao direita dentro da toga (como tirando algo de um bolso secreto). O braco desaparece ate o cotovelo dentro da toga. Expressao de concentracao cinica — olhos focados, sobrancelhas juntas, mas sorriso MANTIDO. Os oculos brilham com aura dourada (bordas das lentes emitem 1px de luz `#FFD700`). A papada treme em antecipacao. A mao esquerda guarda o celular no bolso (precisa das duas maos pro ritual).

### Frame 1: Puxa Documento #2
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: A mao direita SAI da toga segurando UM documento de habeas corpus. O documento e grande (10x14px), papel amarelado (`#E8D8B0`), com texto ilegivel (linhas finas simulando escrita) e um selo dourado no canto (`#FFD700`, 3x3px). AURA DOURADA: particulas douradas (4-5 pixels `#FFD700` em 30% alpha) flutuam ao redor do documento. A papada PARA DE TREMER — momento de solenidade cinica. Os oculos emitem brilho dourado continuo. A toga se infla levemente (como se houvesse vento mistico soprando).

### Frame 2: Puxa Documento #3 (Triplo!)
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: AGORA SAO TRES. Gilmar segura 3 documentos de habeas corpus em leque na mao direita (como cartas de baralho). Cada documento identico mas em angulos diferentes (0, 15, -15 graus). A AURA DOURADA EXPLODE: particulas douradas por TODA a sprite (12-15 pixels `#FFD700` variando entre 20-60% alpha). O corpo todo de Gilmar brilha com contorno dourado (1px `#FFD700` ao redor da silhueta). A expressao muda: de concentracao para TRIUNFO ABSOLUTO. Sorriso MAXIMO. Oculos brilham tanto que as pupilas desaparecem (lentes sao puro brilho branco-dourado). A papada treme de EXCITACAO. A toga vibra com energia. E o frame de PODER MAXIMO do Gilmar.

### Frame 3: Brilho Dourado — Invulnerabilidade
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Os 3 documentos se FUNDEM numa explosao de luz dourada. Onde estavam os documentos, agora ha uma esfera de energia dourada (16x16px, centro da sprite) que pulsa. O corpo de Gilmar esta envolvido em AURA DE INVULNERABILIDADE: contorno dourado de 2px, pulsante (alternando entre `#FFD700` e `#C8A832`). A expressao e de EXTASE CINICO — olhos fechados, sorriso beatífico, papada relaxada (ele sabe que nada pode toca-lo). A toga brilha dourada em vez de preta. O celular no bolso emite notificacao (tela verde brilhando — Vorcaro mandou "parabens"). Este frame marca o INICIO do estado invulneravel.

---

## SPECIAL 2: STF DA PASTELARIA — 6 Frames

**Sprite Sheet**: `gilmar_special_pastelaria.png` — 384x64px (6 frames x 64px)

### Frame 0: Invocacao do Balcao
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Gilmar bate palmas (ambas as maos juntas no centro, pastel e celular guardados). Uma fissura aparece no chao a frente dele (3-4 pixels de rachadura escura, `#0D0D0D`). Fumaca de oleo quente sobe da fissura (5-6 pixels `#C8A832` em 40% alpha, formando nuvem). A expressao e de ALEGRIA GENUINA — o unico momento em que o cinismo da lugar a felicidade REAL. Oculos brilham com reflexo de oleo (tom amarelado em vez de branco). A papada treme de antecipacao gastronomica.

### Frame 1: Balcao Aparece
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Um BALCAO DE PASTELARIA brota do chao. E tosco, de madeira barata (`#6B4423`), com bancada de aluminio amassado (`#8A8580`). Altura: 20px (nao bloqueia visao do Gilmar). Largura: toda a sprite (64px). Sobre o balcao: 3 pasteis em fila (cada um 6x4px, dourados e gordurosos), um pote de molho (`#8B0000`, 4x5px), e uma fritadeira improvisada borbulhando (pixels de oleo `#C8A832` saltando 2px acima da superficie). Gilmar esta ATRAS do balcao, como um pasteleiro profissional. A toga agora parece avental (mancha de oleo DOMINA a frente). Sorriso de orgulho.

### Frame 2: Pegando Pastel
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: Gilmar pega o primeiro pastel do balcao com a mao direita. O pastel e ENORME pra mao dele (12x8px — desproporcional). Oleo escorre do pastel (2-3 gotas amarelas caindo, 1px cada). A fritadeira borbulha mais intensamente (pixels de oleo saltam 4px). Vapor sobe (3-4 pixels brancos 20% alpha). Os outros 2 pasteis no balcao tremem (como se tivessem vida propria). O pote de molho transborda levemente. A papada de Gilmar ja esta SALIVANDO (1px de brilho na papada inferior).

### Frame 3: Mordida Extase
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: Gilmar MORDE o pastel com ferocidade desproporcional. Boca aberta 150 graus. Dentes afundam no pastel. Recheio EXPLODE (5-6 pixels marrons `#8B4513` voam em todas as direcoes). Oleo espirra do pastel (3-4 pixels amarelos em arco). Migalhas formam NUVEM ao redor da cabeca (8-10 pixels dourados). A papada VIBRA com a mordida (onda de cima pra baixo, cada camada reagindo em sequencia). Os oculos embacam pelo vapor do pastel quente (lentes ficam `#A8C8D8` com 80% alpha — semi-opacas). ESTE E O FRAME DE INVULNERABILIDADE: enquanto Gilmar come, borda dourada de 1px pulsa ao redor dele. Nada no mundo importa quando se come pastel.

### Frame 4: Oleo Espirra (Area de Efeito)
- **Posicao no sheet**: 256,0 a 319,63
- **Descricao**: A fritadeira TRANSBORDA. Oleo quente espirra em TODAS as direcoes (8-10 pixels `#C8A832` em 60% alpha, irradiando do centro do balcao ate as bordas do frame). E o AREA OF EFFECT visual — inimigos proximos levariam este oleo. Gilmar continua mastigando (boca fechada, bochechas infladas), completamente INDIFERENTE ao caos da fritadeira. Pasteis no balcao fritam descontroladamente. O vapor agora e DENSO (6-8 pixels brancos, 40% alpha, subindo). Os oculos comecam a desembacar (lentes clareando). A papada tem manchas de oleo novas.

### Frame 5: Satisfacao Final
- **Posicao no sheet**: 320,0 a 383,63
- **Descricao**: O balcao comeca a afundar no chao (descendo 4px — esta sumindo). Gilmar da um ARROTO visual: boca em O, papada inflando momentaneamente (1px de expansao em todas as camadas), olhos surpresos pela forca do proprio arroto. Na mao, so o papel gorduroso do pastel (formato amassado, 4x3px amarelado com manchas de oleo). Os oculos voltam ao brilho normal. A aura de invulnerabilidade comeca a dissipar (borda dourada pisca). Migalhas por todo lado. O sorrisinho cinico volta — momento de felicidade acabou, volta o deboche. A transicao de volta pro idle mostra Gilmar limpando a boca com a toga (mancha nova).

---

## SPECIAL 3: BRIGA COM BARROSO — 8 Frames

**Sprite Sheet**: `gilmar_special_briga.png` — 512x64px (8 frames x 64px)

**NOTA**: Esta animacao requer o sprite do Barroso no mapa. Os 8 frames sao do ponto de vista do GILMAR. O Barroso tem sua propria sprite sheet de briga.

### Frame 0: Detecta o Barroso
- **Posicao no sheet**: 0,0 a 63,63
- **Descricao**: Gilmar PARA o que esta fazendo (congela mid-action). A cabeca gira 30 graus na direcao do Barroso. Os oculos brilham com luz VERMELHA (raiva, nao cinismo — `#CC3030` no reflexo em vez de branco). A papada se ENRIJECE (camadas comprimem, musculo tenso). O sorrisinho cinico muda pra SORRISO DE COMBATE — dentes cerrados, cantos da boca levantados. O celular cai da mao (nao importa mais — Barroso esta aqui). O pastel e jogado pro lado (4px a esquerda, caindo). A toga se infla com a raiva.

### Frame 1: Vira Pro Barroso
- **Posicao no sheet**: 64,0 a 127,63
- **Descricao**: Gilmar gira o corpo 90 graus, ENCARANDO o Barroso diretamente (sprite vira lateral se necessario). Postura muda COMPLETAMENTE: de velhinho curvo pra BULL de briga. Ombros levantam 3px. Peito infla (toga estica). Queixo levanta (papada tripla se exibe como ameaca — e GRANDE e esta IRRITADA). Punho direito cerrado. Punho esquerdo cerrado. Os oculos refletem vermelho INTENSO. Os fios de cabelo ralo se ERIÇAM (de penteados pra espetados, cada fio 1px mais alto). Veias aparecem no pescoco (2-3 linhas de 1px, `#CC3030`). O Gilmar baixinho de repente parece PERIGOSO.

### Frame 2: Grita "VAGABUNDO!" #1
- **Posicao no sheet**: 128,0 a 191,63
- **Descricao**: PRIMEIRO "VAGABUNDO!". Boca ESCANCARADA (abertura maxima, 20px de largura na boca — desproporcional grotesco). A papada tripla EXPANDE com o grito (as 3 camadas inflam com o ar do berro, cada uma 2px mais larga). Linhas de impacto sonoro irradiam da boca (4 linhas curvas, 1px, brancas, emanando pra frente). Os oculos tremem no rosto com a vibracao do grito. Um "!" aparece sobre a cabeca (8px de altura, `#CC3030`, estilo quadrinhos). A toga balanca com a forca do grito. Saliva visivel (2 pixels de spray saindo da boca, brancos 40% alpha). O corpo inteiro se inclina pra frente no grito.

### Frame 3: Grita "VAGABUNDO!" #2
- **Posicao no sheet**: 192,0 a 255,63
- **Descricao**: SEGUNDO "VAGABUNDO!" (repeticao x3 — e o TIQUE do Gilmar). Identico ao Frame 2 mas com DIFERENCA CRITICA: o "!" sobre a cabeca agora e "!!" (dois pontos de exclamacao). A boca esta 2px MAIS aberta que no Frame 2. A papada esta 1px MAIS inflada. As linhas de impacto sonoro sao 2px MAIS longas. O grito esta ESCALANDO. Os oculos deslizam 1px pra baixo com a intensidade. A veias no pescoco estao 1px MAIS grossas. Mais saliva spray (3 pixels agora). A repeticao comunica: ESTA FICANDO PIOR.

### Frame 4: Grita "VAGABUNDO!" #3
- **Posicao no sheet**: 256,0 a 319,63
- **Descricao**: TERCEIRO E ULTIMO "VAGABUNDO!" — o climax. TUDO no maximo: boca MAXIMA (22px — impossivel anatomicamente, grotesco puro), papada MAXIMA de inflacao (parece que vai explodir), "!!!" sobre a cabeca (3 exclamacoes, `#CC3030`, pulsando). As linhas de impacto sonoro chegam ATE A BORDA DO FRAME. Os oculos quase saem do rosto (3px deslocados). As veias no pescoco sao VISIVELMENTE pulsantes (2px de espessura). Spray de saliva MAXIMO (5 pixels). O corpo todo treme com a forca do berro. A toga se deforma com a vibração. E O FRAME MAIS GROTESCO de toda a sprite sheet. O Andre Guedes viveria neste frame.

### Frame 5: Empurrao #1 (Avanca)
- **Posicao no sheet**: 320,0 a 383,63
- **Descricao**: Gilmar AVANCA pro Barroso. Passo agressivo de 4px pra frente (NAO e o walk normal — e uma INVESTIDA). As duas maos estendidas pra frente em posicao de empurrao. A boca fecha mas o sorriso de combate permanece. A papada balanca violentamente (bounce de 3px pra frente, todas as camadas). Os oculos estao tortos (3 graus) mas Gilmar nem liga. A toga esvoaca pra tras com o avanco rapido. Poeira sobe dos pes (3-4 pixels cinza). O velhinho baixinho virou um TOURO.

### Frame 6: Empurrao #2 (Contato)
- **Posicao no sheet**: 384,0 a 447,63
- **Descricao**: As maos de Gilmar FAZEM CONTATO (com o Barroso — implícito, fora do frame ou no frame do Barroso). SQUASH nas maos (dedos achatados contra superficie). O corpo de Gilmar comprime 2px (squash de impacto). A papada BATE NO PEITO com a desaceleracao subita (SLAP visual — 3 camadas comprimem violentamente). Os oculos saltam 2px pra cima. Uma onda de choque emana do ponto de contato (2-3 linhas de impacto, semicirculares, pra frente). O sorriso de combate vira GARGALHADA de satisfacao. Migalhas de pastel residuais voam do corpo com o impacto.

### Frame 7: Pose de Vitoria (e Deboche)
- **Posicao no sheet**: 448,0 a 511,63
- **Descricao**: Gilmar recua 2px (pos-empurrao). Postura de VENCEDOR: peito estufado, queixo erguido, papada exibida como trofeu. O sorriso cinico voltou AMPLIFICADO — e o sorriso de quem GANHOU a briga (mesmo que nao tenha ganho). Os oculos voltam a posicao com brilho branco cinico MAXIMO. As maos estao nos quadris (pose de poder). A toga assenta com dignidade falsa (ainda suja de pastel, mas agora Gilmar a usa como MANTO DE VITORIA). Os fios de cabelo voltam a posicao penteada. O celular e pego de volta do chao (na mao esquerda — primeira coisa que faz). A expressao diz: "Eu sempre ganho. Sempre ganho. Sempre ganho."
- **Detalhe tecnico**: Este frame faz transicao de volta ao idle. A briga acabou. Gilmar volta ao cinismo padrao. Ate a proxima vez que encontrar o Barroso.

---

## Sprite Sheet Summary

| Animacao | Arquivo | Frames | Tamanho Sheet | Proposito |
|---|---|---|---|---|
| Idle | `gilmar_idle.png` | 4 | 256x64px | Papada tremendo, pastel, deboche (loop) |
| Walk | `gilmar_walk.png` | 6 | 384x64px | Andar velhinho, toga balancando, dinheiro caindo (loop) |
| Attack | `gilmar_attack.png` | 3 | 192x64px | Arremesso de pastel + toga Teflon + gargalhada |
| Death | `gilmar_death.png` | 4 | 256x64px | Oculos caem, papada murcha, toga vira pasteis |
| Hit | `gilmar_hit.png` | 2 | 128x64px | Oculos torcem, papada chacoalha (rapido) |
| Habeas Corpus | `gilmar_special_habeas.png` | 4 | 256x64px | Puxa 3 documentos, aura dourada |
| STF Pastelaria | `gilmar_special_pastelaria.png` | 6 | 384x64px | Balcao aparece, come pastel, oleo espirra |
| Briga Barroso | `gilmar_special_briga.png` | 8 | 512x64px | Detecta, grita "Vagabundo!" x3, empurra |

## Phaser 3 Atlas Keys

```javascript
// Idle
this.load.spritesheet('gilmar_idle', 'assets/personagens/gilmar/sprites/gilmar_idle.png', {
    frameWidth: 64, frameHeight: 64
});

// Walk
this.load.spritesheet('gilmar_walk', 'assets/personagens/gilmar/sprites/gilmar_walk.png', {
    frameWidth: 64, frameHeight: 64
});

// Attack
this.load.spritesheet('gilmar_attack', 'assets/personagens/gilmar/sprites/gilmar_attack.png', {
    frameWidth: 64, frameHeight: 64
});

// Death
this.load.spritesheet('gilmar_death', 'assets/personagens/gilmar/sprites/gilmar_death.png', {
    frameWidth: 64, frameHeight: 64
});

// Hit
this.load.spritesheet('gilmar_hit', 'assets/personagens/gilmar/sprites/gilmar_hit.png', {
    frameWidth: 64, frameHeight: 64
});

// Special: Habeas Corpus
this.load.spritesheet('gilmar_special_habeas', 'assets/personagens/gilmar/sprites/gilmar_special_habeas.png', {
    frameWidth: 64, frameHeight: 64
});

// Special: STF da Pastelaria
this.load.spritesheet('gilmar_special_pastelaria', 'assets/personagens/gilmar/sprites/gilmar_special_pastelaria.png', {
    frameWidth: 64, frameHeight: 64
});

// Special: Briga com Barroso
this.load.spritesheet('gilmar_special_briga', 'assets/personagens/gilmar/sprites/gilmar_special_briga.png', {
    frameWidth: 64, frameHeight: 64
});
```

## Notas para o Artista

1. **GROTESCO SEMPRE** — Gilmar deve parecer repugnante e ADORAVEL ao mesmo tempo. Ele e o vilao que voce ama odiar.
2. **A papada e VIVA** — trate a papada tripla como um personagem independente. Ela reage, treme, inflama, murcha. Tem vida propria.
3. **Oculos = Personalidade** — Os oculos enormes sao a IDENTIDADE do Gilmar. Sem oculos, nao e Gilmar. Eles brilham, torcem, caem, embacam — mas SEMPRE comunicam cinismo.
4. **O sorrisinho NUNCA desaparece** — Mesmo no hit, mesmo na death. Gilmar morre debochando. Isso e inegociavel.
5. **Manchas de pastel na toga sao CANONICAS** — Toda frame da toga deve ter manchas amareladas. A toga e um registro historico de pasteis comidos.
6. **Tudo em TRES** — 3 papadas, 3 gritos, 3 documentos, 3 pasteis. O numero 3 e o motif visual do Gilmar.
7. **Contorno irregular 2-3px** — Linhas NUNCA uniformes. Variam de espessura. Simulam mao humana tremula.
8. **Cross-hatching nas sombras** — NAO usar gradientes. Sombras com linhas cruzadas 45 graus, 2px de espacamento.
9. **Textura de papel** — Noise gaussiano 3-5% monocromatico sobre TODOS os frames.
10. **Cores NUNCA puras** — Toda cor e "suja". Se parece digital, adicionar 10% de `#5C5C55` e refazer.
