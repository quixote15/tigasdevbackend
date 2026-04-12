# BARROSO — Sprite Specification

## Boss STF — "O Professor no Ringue"

---

## Overview

| Parametro              | Valor                                        |
|------------------------|----------------------------------------------|
| **Sprite Dimensions**  | 64x64px                                      |
| **Sprite Sheet Layout**| Horizontal strip, 1 row por animacao         |
| **Total de Frames**    | 37 frames (distribuidos em 8 animacoes)      |
| **Formato**            | PNG com alpha transparency                   |
| **Anchor Point**       | Bottom-center (32, 60) — base dos pes        |
| **Perspectiva**        | Top-down levemente isometrica (3/4 view)     |
| **Frame Rate**         | 8-12 fps (estilo jerky Andre Guedes)         |
| **Estilo**             | Grotesco, underground comix, Robert Crumb    |

---

## Paleta de Cores do Sprite

| Elemento                | Hex       | Pixels Aprox | Notas                              |
|-------------------------|-----------|-------------|--------------------------------------|
| Toga (preto impecavel)  | #0A0A0A   | Corpo todo  | ENGOMADA — contraste com outros STF  |
| Toga (suor escondido)   | #1A1A2E   | Axilas/costas | Visivel so de perto               |
| Cabelo grisalho         | #B8B8C0   | Topo cabeca | PERFEITAMENTE penteado               |
| Pele (normal)           | #D4A574   | Rosto/maos  | Bem cuidado                          |
| Pele (raiva)            | #C85A5A   | Rosto       | Vermelho gradual                     |
| Veia da testa           | #8B2252   | 2-3px       | PULSA entre frames                   |
| Veia (explodindo)       | #CC1144   | 3-4px       | Nos specials                         |
| Oculos (armacao)        | #2C2C2C   | Rosto       | Intelectual, fino                    |
| Oculos (lente normal)   | #E8E8F0   | 4x2px cada  | Transparentes                        |
| Oculos (embasado)       | #C0C0D0   | 4x2px cada  | Opaco de raiva                       |
| Olheiras (maquiadas)    | #6B5B6B   | Sob olhos   | Quase invisiveis, mas LA             |
| Martelo (madeira)       | #4A3A2A   | Arma        | MENOR que o do Xandao                |
| Martelo (metal)         | #8B8B7A   | Cabeca      | Fosco, autoritario                   |
| Suor (gotas)            | #F0E8D0   | 1-2px       | Gotas escondidas                     |
| Livro de Direito        | #3A2A1A   | Acessorio   | Couro marrom escuro                  |
| Outline (grosso)        | #1A1A1A   | 2px minimo  | Estilo Crumb                         |
| Onomatopeia "ORDEM!"    | #FFD700   | VFX         | Dourado autoritario                  |

---

## Proporcoes do Personagem (dentro do 64x64)

```
    [CABELO GRISALHO IMPECAVEL] — 8px altura, NENHUM fio fora do lugar
    [TESTA COM VEIA] — 4px, veia ocupa 2-3px pulsando
    [OCULOS INTELECTUAIS] — 8x4px, armacao fina preta
    [ROSTO CONTROLADO] — expressao de serenidade forcada
    [PESCOCO] — normal (nao e bombado como Xandao)
    [OMBROS RETOS] — postura academica perfeita
    [TOGA ENGOMADA] — 20px largura, PRETA, LIMPA, sem dobra
        [POR BAIXO: suor, camisa encharcada — ESCONDIDO]
    [MAO DIREITA: MARTELO] — menor, preciso, nao desproporcional
    [MAO ESQUERDA: LIVRO DE DIREITO] — debaixo do braco
    [PES] — sapatos sociais pretos, polidos
```

**REGRA CRITICA DE PROPORCAO**: Barroso tem proporcoes mais NORMAIS que os outros bosses do STF. Cabeca levemente exagerada (40% do corpo vs 30% normal), mas nada comparado ao Xandao. O exagero do Barroso e SUTIL — esta nos detalhes (veia, suor, tremor), nao na deformidade grosseira. Ele PARECE normal. Esse e o horror.

---

## ANIMACAO 1: IDLE (4 frames)

**Sprite Sheet**: `barroso_idle.png` — 256x64px (4 frames x 64px)
**Loop**: Sim, ciclico infinito
**FPS**: 8 fps (1 ciclo completo = 0.5s)

### Frame 0 (0,0 a 63,63): Postura Ereta — Serenidade
- **Descricao**: Barroso em pe, postura PERFEITAMENTE ereta. Cabelo grisalho impecavel, toga engomada sem uma dobra. Mao direita segura martelo apoiado no ombro (posicao de repouso — nao ameacadora). Mao esquerda segura livro de direito contra o corpo. Oculos limpos, transparentes. Expressao facial: serenidade controlada — boca fechada em linha reta, sobrancelhas niveladas, olhos calmos por fora.
- **Detalhe critico**: A veia da testa esta VISIVEL mas FINA — apenas 1px de largura, cor #8B2252. Esta la. Pulsa sutilmente. Mas voce so nota se olhar com atencao.
- **Detalhe escondido**: 1-2 pixels de suor (#F0E8D0) na nuca, quase invisiveis. Olheiras (#6B5B6B) sob os olhos — 1px, maquiadas mas presentes.
- **Mao no martelo**: Dedos BRANCOS de apertar — pele mais clara nos nos dos dedos (#E8C8A0). Tremor invisivel neste frame.

### Frame 1 (64,0 a 127,63): Veia Pulsa — Primeiro Sinal
- **Descricao**: IDENTICO ao Frame 0 em postura. MAS: a veia da testa PULSA — cresce de 1px para 2px de largura. Cor intensifica levemente (#8B2252 → #9B2262). E como se um segundo coracao batesse na testa. O UNICO movimento visivel em todo o corpo.
- **Detalhe critico**: O resto do corpo esta EXATAMENTE igual. A compostura nao quebrou. Mas a veia denuncia. E um pulso. Um sinal de que algo ferve por baixo.
- **Detalhe escondido**: A mao no martelo treme 1px para a direita (tremor quase imperceptivel).

### Frame 2 (128,0 a 191,63): Ajuste dos Oculos — Tique Nervoso
- **Descricao**: Barroso ergue a mao esquerda (livro vai para debaixo do braco, preso pelo cotovelo) e AJUSTA OS OCULOS com o indicador no ponte do nariz. Gesto CLASSICO de professor — tique nervoso disfarçado de habito intelectual. Veia volta a 1px (relaxa momentaneamente).
- **Detalhe critico**: O gesto e preciso demais, ensaiado demais. Nao e natural — e um mecanismo de defesa. Os oculos NAO estavam tortos. Ele ajusta por NERVOSISMO.
- **Detalhe escondido**: Leve brilho de suor na testa (#F0E8D0, 1px) revelado quando a mao passa perto. 2 gotas de suor ESCONDIDAS atras da orelha.

### Frame 3 (192,0 a 255,63): Tremor no Martelo — O Corpo Denuncia
- **Descricao**: Mao esquerda volta ao livro. Postura identica ao Frame 0. MAS: a mao DIREITA treme visivelmente — o martelo oscila 2px para a esquerda. O tremor e INVOLUNTARIO. Barroso NAO percebe (ou finge nao perceber). Veia da testa em 1.5px — entre o normal e o pulsante.
- **Detalhe critico**: O rosto mantem a mesma expressao serena do Frame 0. Zero emocao facial. Mas o corpo denuncia: mao tremendo, veia semi-pulsante, suor acumulando. A mascara esta QUASE perfeita. Quase.
- **Detalhe escondido**: Uma UNICA gota de suor escorre da tempera para o queixo (1px, #F0E8D0, trajetoria de 3px). Nenhum outro frame mostra isso — e o vazamento.

---

## ANIMACAO 2: WALK (6 frames)

**Sprite Sheet**: `barroso_walk.png` — 384x64px (6 frames x 64px)
**Loop**: Sim, ciclico
**FPS**: 10 fps (1 ciclo completo = 0.6s)

### Frame 0 (0,0 a 63,63): Passo Direito — Postura Academica
- **Descricao**: Barroso da o primeiro passo com pe direito. Postura ERETA, quase militar — costas retas, queixo levantado, olhar para frente. Toga flui elegantemente ao redor do corpo. Livro de direito firme debaixo do braco esquerdo. Martelo apoiado no ombro direito. Andar de quem caminha ate o podio de uma aula magna, nao de quem foge de zumbis.
- **Detalhe de toga**: A toga se move com fluidez (2-3px de ondulacao na barra inferior). LIMPA. ENGOMADA. Sem dobra. MAS: na axila esquerda, 2px de mancha de suor (#1A1A2E) — escondida pela posicao do braco.

### Frame 1 (64,0 a 127,63): Passo Esquerdo — Livro Ajusta
- **Descricao**: Pe esquerdo avanca. O livro de direito escorrega LEVEMENTE (1px para baixo) e Barroso o reacomoda com pressao do cotovelo. Toga ondula no sentido oposto. Cabelo permanece PERFEITO (zero movimento — como se fosse esculpido em pedra).
- **Detalhe escondido**: Gota de suor pinga do queixo para a toga (1px caindo). A toga absorve e esconde.

### Frame 2 (128,0 a 191,63): Passada Firme — Autoridade no Caminhar
- **Descricao**: Ambos os pes plantados no chao momentaneamente. Postura mais larga, peito aberto. Momento de AUTORIDADE no caminhar — como professor que entra na sala de aula e todos silenciam. Martelo muda de ombro (agora apoiado no esquerdo, mao trocou).
- **Detalhe critico**: Veia da testa pulsa 1x (2px por 1 frame). O andar e tao controlado que parece ensaiado. E. Barroso ENSAIA como andar.

### Frame 3 (192,0 a 255,63): Passo Direito — Suor Escorre
- **Descricao**: Repeticao do ciclo, pe direito. MAS: a camera (angulo) revela brevemente as costas — e la esta: MANCHA DE SUOR ENORME nas costas da camisa, escondida pela toga. A toga se abre 2px com o movimento e revela o segredo por um instante.
- **Detalhe critico**: Ninguem VE o suor porque a toga cobre. Mas o jogador atento nota: quando Barroso vira levemente, as costas suadas aparecem por 1 frame. O corpo GRITA o que o rosto esconde.

### Frame 4 (256,0 a 319,63): Passo Esquerdo — Oculos Escorregam
- **Descricao**: Pe esquerdo. Os oculos escorregam 1px pelo nariz (suor no nariz faz escorregar). Barroso NAO ajusta imediatamente — tenta ignorar. Livro firme. Toga fechada novamente, suor das costas escondido de volta.
- **Detalhe escondido**: A mao do martelo treme 1px. O tremor so aparece durante o walk porque o movimento amplifica.

### Frame 5 (320,0 a 383,63): Passo Final — Recomposicao
- **Descricao**: Barroso ergue a mao e ajusta os oculos DE VOLTA ao lugar perfeito. Gesto rapido, preciso, ENSAIADO. Como se dissesse "nada aconteceu". Postura volta ao Frame 0. Ciclo recomeça.
- **Detalhe critico**: O ajuste dos oculos e o unico sinal PUBLICO de imperfeicao que Barroso permite. Todo o resto (suor, tremor, veia) e escondido. Os oculos sao a UNICA concessao.

---

## ANIMACAO 3: ATTACK (3 frames)

**Sprite Sheet**: `barroso_attack.png` — 192x64px (3 frames x 64px)
**Loop**: Nao (dispara 1x por ataque)
**FPS**: 12 fps (ataque completo = 0.25s — RAPIDO e PRECISO)

### Frame 0 (0,0 a 63,63): Ergue o Martelo — Elegancia Calculada
- **Descricao**: Barroso ergue o martelo com a mao direita acima da cabeca. NAO e um levantar bruto como Xandao — e um movimento PRECISO, CIRURGICO, como professor erguendo o giz antes de escrever no quadro. Braco esticado, cotovelo alinhado, punho firme. Livro guardado debaixo do braco esquerdo (nao solta o livro NEM pra atacar).
- **Expressao**: Sobrancelhas levemente franzidas. Nao raiva — DETERMINACAO. Boca apertada. Oculos brilham com reflexo de luz (2px brancos nas lentes).
- **Veia**: 2px, pulsando. A raiva esta la, mas CONTIDA. Canalizada no martelo.
- **Onomatopeia**: Nenhuma ainda — o silencio antes do golpe.

### Frame 1 (64,0 a 127,63): Martelo Desce — "ORDEM!"
- **Descricao**: O martelo desce em arco preciso. NAO e uma martelada de forca bruta — e uma SENTENCA. O martelo atinge a posicao frontal com impacto seco. Onda de choque sutil (3-4 linhas radiais de 1px, #FFD700 dourado) emanando do ponto de impacto. A onomatopeia "ORDEM!" aparece em letras douradas (#FFD700) com borda preta, estilo comic book, acima do martelo.
- **Expressao**: Olhos ABERTOS — nao de raiva, de AUTORIDADE. Como juiz que bate o martelo sabendo que sua palavra e lei.
- **Veia**: 2.5px — pulsou com o esforco.
- **Toga**: Ondula com o movimento do braco (3px de flutter na manga direita). Mantem-se IMPECAVEL.
- **Texto "ORDEM!"**: Letras grossas, hand-lettered, levemente tortas (estilo Crumb). Tamanho: 20x8px, posicionado acima-direita do martelo. Cor dourada (#FFD700) com outline preto (#1A1A1A, 1px).

### Frame 2 (128,0 a 191,63): Recuperacao — Como Se Nada Tivesse Acontecido
- **Descricao**: Barroso puxa o martelo de volta ao ombro em um movimento fluido. Onda de choque dissipando (linhas radiais ficam mais finas, fade out). "ORDEM!" comecando a desaparecer (alpha 60%). Postura retorna ao idle. Expressao volta a serenidade neutra. Como se nao tivesse acabado de bater em alguem.
- **Detalhe critico**: A VELOCIDADE da recuperacao e o que define Barroso. Xandao fica em pose de poder apos atacar. Barroso IMEDIATAMENTE volta ao normal. "Isso? Isso nao foi nada. Eu estou sereno."
- **Veia**: Volta a 1.5px (desacelerando).
- **Suor**: 2 gotas novas apareceram na testa (o ataque custou mais esforco do que ele quer admitir).

---

## ANIMACAO 4: DEATH (4 frames)

**Sprite Sheet**: `barroso_death.png` — 256x64px (4 frames x 64px)
**Loop**: Nao (plays 1x e congela no ultimo frame)
**FPS**: 6 fps (morte LENTA — 0.67s — cada frame doi)

### Frame 0 (0,0 a 63,63): A Compostura Racha
- **Descricao**: Barroso leva o golpe final. Oculos DESLOCAM do nariz (3px para baixo, tortos pela primeira vez). A expressao de serenidade RACHA — sobrancelha esquerda sobe, boca abre levemente em surpresa. Mao do martelo afrouxa (martelo começa a cair, 2px abaixo do ombro). O livro de direito escorrega do braco.
- **Veia da testa**: PARA DE PULSAR. Congela em 2px. Sem vida. Como se desligassem a maquina.
- **Cabelo**: PELA PRIMEIRA VEZ, 2-3 fios saem do lugar. E DEVASTADOR. O cabelo que nunca despenteava DESPENTEIA. O sinal mais claro de derrota.

### Frame 1 (64,0 a 127,63): A Toga Amassa
- **Descricao**: Barroso cai para frente, joelhos dobrando. A toga AMASSA — dobras visíveis pela primeira vez (4-5 linhas de dobra, #2A2A2A). O martelo CAI da mao e toca o chao (posicao: ao lado do pe direito). O livro ABRE ao cair e as paginas se espalham (3-4 retangulos brancos de 2x3px voando). Oculos pendurados em uma orelha so.
- **Suor**: VISIVEL AGORA. Suor escorre abertamente pelo rosto — 3-4 gotas grandes (#F0E8D0). As olheiras que estavam maquiadas aparecem CLARAMENTE (#6B5B6B, 2px sob cada olho). Todo o disfarce desmorona.
- **Expressao**: Boca aberta em "O" — nao e grito, e CHOQUE. Como professor que leva uma prova que nao estudou.

### Frame 2 (128,0 a 191,63): O Professor Cai
- **Descricao**: Barroso cai de joelhos. Toga completamente amarrotada, servindo agora como pano de chao. Maos apoiadas no chao (posicao de derrota). Cabelo COMPLETAMENTE despenteado — mechas para todos os lados. Oculos no chao ao lado (caidos, uma lente rachada — 1px de linha de rachadura). Suor formando poca pequena sob o rosto (2x2px, #F0E8D0).
- **Veia da testa**: Apagada. Cor mudou de #8B2252 para #6B5B6B (cinza — morta). Nao pulsa. Nao vive.
- **Detalhe**: A camisa branca por baixo da toga agora COMPLETAMENTE visivel — ENCHARCADA de suor, quase translucida. O segredo que ele escondeu o jogo inteiro esta exposto.

### Frame 3 (192,0 a 255,63): Derrota do Professor — Frame Final
- **Descricao**: Barroso deitado no chao, de lado. Toga espalhada como lencol amarrotado ao redor. Martelo a 10px de distancia (alcance impossivel). Livro aberto com paginas ao vento (2-3 paginas flutuando acima, 2x3px). Oculos quebrados no chao. Cabelo uma BAGUNCA completa. Mao estendida na direcao do martelo (nao alcanca — nunca vai alcancar).
- **Expressao final**: Olhos semi-abertos, expressao de EXAUSTAO TOTAL — nao de raiva, nao de surpresa. ALIVIO MISTURADO COM DERROTA. Como se secretamente estivesse feliz que acabou. O professor finalmente pode descansar.
- **Veia**: Invisivel. Sumiu. O segundo coracao parou.
- **Detalhe final**: Um UNICO fio de cabelo ainda perfeitamente penteado no meio do caos — ultima resistencia da compostura, ridicula no contexto. Comedia no horror.

---

## ANIMACAO 5: HIT (2 frames)

**Sprite Sheet**: `barroso_hit.png` — 128x64px (2 frames x 64px)
**Loop**: Nao (dispara 1x por hit recebido)
**FPS**: 10 fps (hit completo = 0.2s)

### Frame 0 (0,0 a 63,63): Impacto — Oculos Embacam
- **Descricao**: Barroso recebe dano. Corpo empurrado 2px para tras. Reacao CONTIDA — nao grita, nao faz escandalo. Maxilar TRAVA (mandibula apertada, 1px de distorcao na boca). Oculos EMBACAM INSTANTANEAMENTE — lentes mudam de #E8E8F0 para #C0C0D0 (opaco). Como se a raiva interna gerasse CALOR que condensasse nos oculos.
- **Veia da testa**: PULSA FORTE — 3px de largura, cor #CC1144 (vermelho vivo). O hit ativou a raiva. A veia GRITA o que a boca nao diz.
- **Toga**: Amassa levemente na area do impacto (2-3px de deformacao). Mas Barroso IMEDIATAMENTE tenta alisar (mao esquerda se move para a toga).
- **Flash**: Pisca vermelho sutil (#FF0000, 20% opacity) no contorno do personagem por 1 frame.

### Frame 1 (64,0 a 127,63): Recuperacao — Compostura Forcada
- **Descricao**: Barroso volta a posicao ereta. Mao esquerda ALISANDO A TOGA (passando a mao na area amassada). Oculos ainda levemente embasados (transitando de #C0C0D0 de volta para #E8E8F0, estao em #D4D4E0 — meio caminho). Expressao: labios APERTADOS, maxilar TRAVADO, respiracao visivel (peito expande 1px).
- **Veia**: Ainda em 2.5px — descendo de 3 mas nao voltou ao normal. Cor transitando de #CC1144 de volta para #8B2252.
- **Suor**: 2 gotas novas na testa (cada hit adiciona suor — sistema acumulativo).
- **Detalhe**: O cabelo permanece PERFEITO mesmo apos o hit. Barroso prioriza o cabelo acima de TUDO.

---

## ANIMACAO 6: SPECIAL — Paciencia Esgotada (6 frames)

**Sprite Sheet**: `barroso_special_paciencia.png` — 384x64px (6 frames x 64px)
**Loop**: Nao (dispara 1x quando a barra enche)
**FPS**: 10 fps (sequencia completa = 0.6s)
**Trigger**: Barra de paciencia atinge 100%

### Frame 0 (0,0 a 63,63): Barra Enchendo — Tremor Visivel
- **Descricao**: Barroso em pe, postura ereta, MAS tremendo VISIVELMENTE agora. Todo o corpo oscila 1px para esquerda/direita. Maos fechadas em punho (martelo e livro seguros com forca). Barra de paciencia visivel acima da cabeca: retangulo 30x4px, preenchido 80% em vermelho (#CC1144), borda preta.
- **Veia**: 3px e PULSANDO RAPIDO — muda de #8B2252 para #CC1144 a cada frame.
- **Oculos**: Embasando — #D4D4E0, meio caminho para opaco.
- **Suor**: 4-5 gotas VISIVEIS no rosto todo. O disfarce acabou.

### Frame 1 (64,0 a 127,63): Veia Crescendo — Quase La
- **Descricao**: Barra de paciencia em 90%. A veia da testa CRESCE — agora 4px de largura, ramificando-se em veias menores (2-3 ramificacoes de 1px). Rosto AVERMELHA (#C85A5A → #B83A3A). Oculos quase OPACOS (#C0C0D0). Boca entreaberta — dentes cerrados, respiracao pesada. Toga amassando involuntariamente (maos cerradas puxam o tecido).
- **Detalhe**: Cabelo AINDA perfeito. Mesmo neste ponto, o cabelo resiste. E absurdo. E comico.

### Frame 2 (128,0 a 191,63): Oculos Embasam Completamente — Cegueira de Raiva
- **Descricao**: Barra de paciencia em 99%. Oculos COMPLETAMENTE embasados — branco opaco (#C0C0D0), IMPOSSIVEL ver os olhos por tras. Barroso esta CEGO de raiva, literalmente. Veia em 5px — MONSTRUOSA, ramificada, pulsando como algo vivo. Rosto vermelho total (#B83A3A). O corpo inteiro treme 2px.
- **Momento de transicao**: Barroso abre a boca para gritar. Ar entra. Peito expande 3px. E o momento antes da explosao.

### Frame 3 (192,0 a 255,63): "CHEGA!" — A EXPLOSAO
- **Descricao**: BARRA EXPLODE (particulas de barra voando, 4-5 fragmentos vermelhos de 2x2px). Barroso GRITA — boca ABERTA TOTAL (ocupa 30% do rosto), texto "CHEGA!" aparece ENORME em letras vermelhas (#CC1144) com borda preta, estilo comic book, acima da cabeca (24x10px). Martelo levantado ACIMA da cabeca com AMBAS as maos (livro JOGADO pro chao — PELA PRIMEIRA VEZ solta o livro).
- **Veia**: QUASE EXPLODINDO — 6px, cor #FF0000, ramificacoes por toda a testa. Parece que vai RASGAR a pele.
- **Onda de furia**: Linhas de choque radiais (8-10 linhas de 1-2px, #FFD700 dourado e #CC1144 vermelho) emanando do corpo em todas as direcoes. O CHAO ao redor começa a rachar (2-3 linhas de rachadura no tile abaixo).
- **Toga**: Ondula VIOLENTAMENTE. Algumas costuras estourando (2-3 pontos de #3A3A3A aparecendo — tecido rasgando).
- **CABELO**: UM UNICO fio sai do lugar. UM. E suficiente. O universo trinca.

### Frame 4 (256,0 a 319,63): Onda de Furia Elegante — Dano em Area
- **Descricao**: A onda de choque se EXPANDE. Circulo de furia (#FFD700 com #CC1144, 2px de largura) crescendo a partir de Barroso ate ocupar 50% do frame. Tudo dentro da onda toma dano. Barroso no centro: martelo plantado no chao (bateu com forca TOTAL), postura de quem acabou de SENTENCIAR o mundo.
- **Expressao**: Olhos ABERTOS (oculos voaram do rosto — estao a 8px de distancia, flutuando/caindo), raiva PURA mas ARTICULADA — nao e caos, e FURIA CONTROLADA QUE SE DESCONTROLOU. A diferenca e sutil mas CRITICA.
- **Texto "CHEGA!"**: Ainda presente mas maior (30x12px), pulsando, comecando a dissipar.
- **Chao**: Rachado em padrao radial. Poeira subindo (3-4 particulas cinza #8A8580, 2x2px).

### Frame 5 (320,0 a 383,63): Silencio Pos-Explosao — Recomposicao Patetica
- **Descricao**: Tudo para. Onda de choque dissipada (linhas fantasma em alpha 20%). "CHEGA!" desapareceu. Silencio visual total. Barroso de pe, RESPIRANDO PESADO (peito sobe e desce 2px). Mao tremendo segurando o martelo. Ele olha ao redor como quem acordou de um sonho.
- **Recomposicao patetica**: Barroso se ABAIXA para pegar os oculos do chao. AJUSTA os oculos no rosto (tortos — nao consegue colocar direito, as maos tremem). Tenta ALISAR a toga (passa a mao, nao resolve). Tenta ARRUMAR o cabelo (nao volta ao lugar). Pega o livro do chao.
- **Detalhe COMICO**: Ele TENTA voltar a serenidade e FRACASSA MISERAVELMENTE. Tudo esta fora do lugar. O cabelo, a toga, os oculos, a dignidade. Ele tenta e nao consegue. E HILARIO e TRAGICO.
- **Veia**: Voltando a 2px. Ainda grossa. Nao vai desinflar tao rapido.

---

## ANIMACAO 7: SPECIAL — Sessao Encerrada (4 frames)

**Sprite Sheet**: `barroso_special_sessao.png` — 256x64px (4 frames x 64px)
**Loop**: Nao (dispara 1x)
**FPS**: 10 fps (sequencia completa = 0.4s)
**Efeito**: Congela TODOS no mapa por 2s

### Frame 0 (0,0 a 63,63): Ergue o Martelo — Autoridade Maxima
- **Descricao**: Barroso ergue o martelo com AMBAS as maos acima da cabeca (livro preso debaixo do braco pelo cotovelo). Postura de JUIZ PRESIDENTE — nao de guerreiro, de AUTORIDADE LEGAL SUPREMA. Costas retas, queixo erguido, olhos semicerrados de determinacao.
- **Expressao**: Nao e raiva — e CANSACO ABSOLUTO disfarçado de autoridade. "Chega. Isso encerrou. EU encerrei."
- **Veia**: 2px, estavel. Nao e raiva, e AUTORIDADE FRIA.
- **Detalhe**: Toga se abre com o movimento de erguer os bracos, revelando BREVEMENTE a camisa encharcada por baixo (1 frame de exposicao).

### Frame 1 (64,0 a 127,63): Martelo No Ar — Silencio Antes do Impacto
- **Descricao**: Martelo no ponto mais alto. CONGELADO por 1 frame extra (hold frame — duplicar no codigo). O mundo PARA antes do golpe. Linhas de tensao (4 linhas de 1px, #FFD700) irradiando do martelo. Todos no mapa PRESSENTEM o que vem.
- **Texto**: "A sessao esta..." aparece em letras menores (16x4px), preto sobre fundo branco, como legenda de tribunal.

### Frame 2 (128,0 a 191,63): MARTELADA — Onda de Congelamento
- **Descricao**: Martelo BATE com forca monumental. Impacto no chao gera onda de gelo/autoridade: circulo azul-gelado (#4A6FA5 com alpha 60%) expandindo do ponto de impacto. Tudo que a onda toca CONGELA (efeito visual: personagens ficam em #C0C0D0 monocromatico, estaticos).
- **Texto COMPLETO**: "...ENCERRADA!" aparece em letras GRANDES (24x8px), vermelhas (#CC1144), com borda preta grossa. Estilo carimbo judicial.
- **Veia**: PULSA uma vez forte (4px) com o impacto — o esforco da autoridade.
- **Efeito de onda**: A onda de congelamento tem textura de GELO JURIDICO — parece uma certidao judicial se expandindo. Cristais de gelo misturados com letras juridicas minusculas (1px, ilegíveis, decorativas).

### Frame 3 (192,0 a 255,63): Silencio Absoluto — Todos Congelados
- **Descricao**: Barroso de pe, martelo apoiado no chao (posicao pos-golpe). Ao redor: TODOS os personagens visiveis estao CONGELADOS em azul-cinza (#C0C0D0). Nenhum movimento no mapa exceto Barroso. Ele ajusta os oculos. Endireita a toga. Respira.
- **Expressao**: Satisfacao MOMENTANEA. Por 2 segundos, ele e o ADULTO NA SALA e funcionou. A serenidade voltou. De verdade. Mas vai durar so 2 segundos.
- **Texto**: "ENCERRADA!" fazendo fade out (alpha 40%). Efeito de congelamento comecando a rachar (linhas de rachadura no gelo, indicando que vai acabar).

---

## ANIMACAO 8: SPECIAL — Briga com Gilmar (8 frames)

**Sprite Sheet**: `barroso_special_briga.png` — 512x64px (8 frames x 64px)
**Loop**: Nao (dispara 1x quando Gilmar esta no mapa, dura 10s no jogo — frames sao keyframes, interpolados)
**FPS**: 8 fps (animacao extendida com holds)
**Trigger**: Gilmar Mendes presente no mapa
**NOTA**: Esta animacao requer o sprite do Gilmar para funcionar. Barroso VIRA em direcao ao Gilmar.

### Frame 0 (0,0 a 63,63): Deteccao — "...Gilmar?"
- **Descricao**: Barroso PARA o que estava fazendo. Corpo gira na direcao do Gilmar. Oculos brilham com reflexo (2px brancos — reconhecimento). Expressao muda de serenidade para TENSAO INSTANTANEA. Boca aperta. Maxilar trava. Veia COMEÇA a pulsar (1px → 2px IMEDIATAMENTE).
- **Detalhe**: O livro de direito e apertado contra o corpo como escudo emocional. O martelo e levantado INVOLUNTARIAMENTE — reflexo de combate que Barroso nao controla.
- **Texto interno (nao exibido)**: "Nao... nao de novo... nao ele..."

### Frame 1 (64,0 a 127,63): Confronto Verbal — Dedo em Riste
- **Descricao**: Barroso APONTA o dedo indicador na direcao do Gilmar (livro jogado pro chao — prioridades mudaram). Mao tremendo de raiva. Oculos comecam a embacar (#D4D4E0). Boca ABERTA — gritando. Veia em 3px.
- **Texto flutuante**: "Vossa Excelencia esta FORA DE ORDEM!" em letras vermelhas (18x4px), saindo da boca como balao de HQ sem borda.
- **Toga**: Comeca a amascar. Barroso nao percebe — esta focado demais no Gilmar.

### Frame 2 (128,0 a 191,63): Oculos Caem — A Mascara Racha
- **Descricao**: O calor da raiva (suor no nariz) faz os OCULOS CAIREM. Escorregam do nariz e ficam pendurados em uma orelha (inclinados 45 graus). Barroso NAO PEGA — esta ocupado demais gritando. Sem oculos, os OLHOS ficam expostos: olheiras ENORMES (#6B5B6B, agora 3px — sem maquiagem para esconder), olhos vermelhos de estresse (#CC3333 na esclerotica).
- **Veia**: 4px, ramificando. Pulsacao visivel.
- **Rosto**: Vermelho (#B83A3A). Suor escorrendo livremente (5+ gotas).

### Frame 3 (192,0 a 255,63): Gritaria — "VOCE E UMA PESSOA HORRIVEL!"
- **Descricao**: Barroso GRITANDO com boca ABERTA TOTAL (ocupa 40% da area do rosto — desproporcional, GROTESCO, estilo Crumb). Saliva voando (2-3 particulas brancas de 1px). Bracos abertos, martelo esquecido no chao. Toga completamente amassada, uma ombreira caida.
- **Texto ENORME**: "VOCE E UMA PESSOA HORRIVEL!" em letras VERMELHAS TREMENDO (24x6px, com efeito de tremor — letras ligeiramente desalinhadas entre si). Referencia direta ao momento real.
- **Veia**: 5px. Ramificacoes cobrindo TODA a testa. Parece um mapa de rios de raiva.
- **Cabelo**: 3-4 fios fora do lugar. O impensavel.

### Frame 4 (256,0 a 319,63): Empurrao — Contato Fisico
- **Descricao**: Barroso AVANCA na direcao do Gilmar. Maos estendidas para EMPURRAR (palmas abertas, dedos esticados). Postura inclinada para frente (15 graus). Toga esvoaçando atras como capa de super-heroi as avessas. Sapatos sociais derrapando no chao (2px de linhas de arrasto).
- **Expressao**: FURIA TOTAL. Zero compostura. Zero serenidade. Zero professor. E um HOMEM brigando com outro HOMEM. O ringue politico nu e cru.
- **Veia**: 6px — tamanho maximo. Quase RASGA a pele.
- **Oculos**: No chao, a 15px de distancia. Esquecidos. Irrelevantes.

### Frame 5 (320,0 a 383,63): Xingamento — "CALA A BOCA, GILMAR!"
- **Descricao**: Barroso com o dedo na cara do Gilmar (indicador a 2px do rosto do outro). GRITANDO a plenos pulmoes. Corpo tremendo INTEIRO (oscilacao de 2px). Veias do PESCOCO agora visiveis tambem (2-3 veias em #8B2252 no pescoco). Toga caindo de um ombro, revelando a camisa encharcada.
- **Texto**: "GILMAR, PELO AMOR DE DEUS, CALA A BOCA!" em letras que CRESCEM progressivamente — "Gilmar" pequeno (8px), "CALA A BOCA" ENORME (20px). Efeito de grito crescendo.
- **Suor**: Pocas. Literal. Gotas grossas caindo.

### Frame 6 (384,0 a 447,63): Exaustao da Briga — Mãos nos Joelhos
- **Descricao**: Barroso PAROU de gritar — exaustao. Curvado para frente, maos nos joelhos, respirando pesado (peito subindo e descendo 3px). Rosto VERMELHO total (#9A2A2A). Suor escorrendo em RIOS. Toga pendurada como pano de cozinha — sem forma, sem engomar, sem dignidade.
- **Expressao**: Olhos arregalados, boca aberta buscando ar. O "adulto na sala" teve um colapso nervoso publico. De novo.
- **Veia**: 4px — voltando, mas devagar. Ainda grossa.
- **Cabelo**: DESTRUIDO. Metade para um lado, metade para outro. Fios colados de suor na testa.

### Frame 7 (448,0 a 511,63): Tentativa de Recomposicao — Fracasso Total
- **Descricao**: Barroso se endireita. Tenta DESESPERADAMENTE voltar ao normal. Pega os oculos do chao (tortos, uma lente com marca de dedo). Coloca no rosto (ficam TORTOS). Tenta alisar a toga (nao alisa). Tenta arrumar o cabelo (piora). Pega o martelo e o livro do chao. Tenta a postura ereta.
- **Resultado**: PARODY da postura do Frame 0 do idle. Tudo no lugar ERRADO. Oculos tortos, toga amassada, cabelo bagunçado, suor por toda parte, veia AINDA grossa. Mas Barroso FINGE que esta tudo bem. A expressao e de serenidade forcada, mas o corpo diz TUDO.
- **Texto sutil**: "...eu mantenho a serenidade." em letras minusculas (12x3px), italico, tremendo. Mentira.
- **Transicao**: Este frame faz bridge de volta para o idle loop (que agora esta "sujo" — Barroso pos-briga e visivelmente diferente do Barroso pre-briga).

---

## Resumo de Sprite Sheets

| Animacao             | Arquivo                          | Frames | Tamanho      | FPS |
|----------------------|----------------------------------|--------|--------------|-----|
| Idle                 | `barroso_idle.png`               | 4      | 256x64px     | 8   |
| Walk                 | `barroso_walk.png`               | 6      | 384x64px     | 10  |
| Attack               | `barroso_attack.png`             | 3      | 192x64px     | 12  |
| Death                | `barroso_death.png`              | 4      | 256x64px     | 6   |
| Hit                  | `barroso_hit.png`                | 2      | 128x64px     | 10  |
| Paciencia Esgotada   | `barroso_special_paciencia.png`  | 6      | 384x64px     | 10  |
| Sessao Encerrada     | `barroso_special_sessao.png`     | 4      | 256x64px     | 10  |
| Briga com Gilmar     | `barroso_special_briga.png`      | 8      | 512x64px     | 8   |

**Total**: 37 frames, 8 sprite sheets

---

## Phaser 3 Atlas Keys

```javascript
// Idle
this.load.spritesheet('barroso_idle', 'assets/personagens/barroso/sprites/barroso_idle.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Walk
this.load.spritesheet('barroso_walk', 'assets/personagens/barroso/sprites/barroso_walk.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Attack
this.load.spritesheet('barroso_attack', 'assets/personagens/barroso/sprites/barroso_attack.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Death
this.load.spritesheet('barroso_death', 'assets/personagens/barroso/sprites/barroso_death.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Hit
this.load.spritesheet('barroso_hit', 'assets/personagens/barroso/sprites/barroso_hit.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Special - Paciencia Esgotada
this.load.spritesheet('barroso_special_paciencia', 'assets/personagens/barroso/sprites/barroso_special_paciencia.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Special - Sessao Encerrada
this.load.spritesheet('barroso_special_sessao', 'assets/personagens/barroso/sprites/barroso_special_sessao.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Special - Briga com Gilmar
this.load.spritesheet('barroso_special_briga', 'assets/personagens/barroso/sprites/barroso_special_briga.png', {
    frameWidth: 64,
    frameHeight: 64
});
```

---

## Notas para o Artista

1. **O CONTRASTE E TUDO**: Barroso PARECE normal. Esse e o horror. Todos os outros bosses do STF sao OBVIAMENTE grotescos. Barroso e grotesco NOS DETALHES. Voce precisa olhar de perto pra ver que ele esta desmoronando.
2. **Outlines grossos e irregulares** (estilo Robert Crumb) — 2px minimo, preto #1A1A1A
3. **O cabelo NUNCA despenteie** exceto em death e briga com Gilmar. E SAGRADO.
4. **A veia da testa e o ELEMENTO CENTRAL** — e o barometro emocional. De 1px (calmo) a 6px (quase explodindo). SEMPRE visivel, SEMPRE pulsando.
5. **Os oculos embacam GRADUALMENTE** — transparente (#E8E8F0) → meio (#D4D4E0) → opaco (#C0C0D0). Escala de raiva.
6. **O suor e ESCONDIDO** no idle/walk e EXPOSTO nos specials/death. A transicao de escondido→exposto e a NARRATIVA VISUAL do personagem.
7. **O martelo e MENOR que o do Xandao** — autoridade, nao forca bruta. Proporcionado, nao desproporcional.
8. **A toga e a MAIS LIMPA do STF** — engomada, sem mancha (por fora). O unico sinal de sujeira e ESCONDIDO (suor por dentro).
9. **Cada frame que nao e grotesco e uma MENTIRA** — e essa a piada. Barroso e a mentira de normalidade num mundo grotesco.
10. **Na briga com Gilmar, TUDO desmorona** — e o unico momento em que Barroso e tao deformado quanto os outros. E catartico. E hilario. E tragico.
