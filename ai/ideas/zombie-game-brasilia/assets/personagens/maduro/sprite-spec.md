# MADURO (O Ditador Palhaco) - Sprite Specification

## Overview
- **Tipo de Personagem:** Guest Character / Boss Internacional Secundario
- **Sprite Dimensions:** 64x64px (personagem), 32x32px (projeteis)
- **Sprite Sheet Layout:** Horizontal strip por animacao
- **Direcoes:** 4 (frente, costas, esquerda, direita)
- **Formato:** PNG com alpha transparency
- **Anchor Point:** Bottom-center (32, 60) -- pes do personagem
- **Proporcoes:** Cabeca 1.5x, torso 2x, pernas 1.5x (~5 cabecas total, atarracado)

---

## Paleta de Cores

| Elemento                  | Hex Code  | Uso                                          |
|---------------------------|-----------|----------------------------------------------|
| Pele Base                 | `#C68E5B` | Tom de pele principal                        |
| Pele Sombra               | `#9E6B3A` | Sombras do rosto e maos                      |
| Pele Highlight            | `#D9A76C` | Destaques nas bochechas e nariz              |
| Bigode Preto              | `#1A1A1A` | Bigode DESPROPORCIONAL (o core do personagem)|
| Bigode Sombra             | `#0D0D0D` | Profundidade do bigode, volume               |
| Bigode Highlight          | `#333333` | Reflexo oleoso do bigode                     |
| Boina Vermelha            | `#8B1A1A` | Boina militar torta                          |
| Boina Vermelha Escuro     | `#5C0E0E` | Sombra da boina                              |
| Boina Estrela             | `#F4D03F` | Estrela dourada (torta) na boina             |
| Uniforme Verde            | `#2E5930` | Corpo do uniforme militar                    |
| Uniforme Verde Escuro     | `#1A3A1C` | Sombras do uniforme                          |
| Uniforme Verde Claro      | `#3D7340` | Highlights do uniforme                       |
| Medalhas Aluminio         | `#C0C0C0` | Medalhas FALSAS (papel aluminio)             |
| Medalhas Brilho           | `#E8E8E8` | Reflexo barato das medalhas                  |
| Medalhas Sombra           | `#8A8A8A` | Sombra revelando que sao de papel            |
| Faixa Presidencial        | `#F4D03F` | Faixa amarela no torso                       |
| Faixa Vermelha            | `#CC2222` | Listras vermelhas da faixa                   |
| Barriga Proeminente       | `#3D7340` | Tecido esticado na barriga                   |
| Sapato Preto              | `#1A1A1A` | Sapatos militares                            |
| Sapato Brilho             | `#333333` | Reflexo nos sapatos                          |
| Pintura Facial Branco     | `#F0E6D6` | Base involuntaria de palhaco no rosto        |
| Pintura Facial Vermelho   | `#CC3333` | Bochechas/nariz vermelho de palhaco          |
| Outline                   | `#1A1A1A` | Linhas grossas 2-4px irregulares             |
| Cross-Hatch Shadow        | `#0D0D0D` | Sombras em cross-hatching                    |
| Dinheiro Verde             | `#4CAF50` | Notas de bolivar voando (skill)             |
| Dinheiro Desvalorizado     | `#8D6E4A` | Notas amareladas/velhas                     |
| Gas Verde Doentio          | `#7CFC00` | Efeito de gas da skill                      |
| Ceu Laranja Sangue         | `#D4500A` | Referencia de fundo (nao no sprite)         |

---

## Frame-by-Frame: IDLE (4 frames, loop)

### Frame 0: idle_01 -- Pose Base
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Maduro de frente, postura tentando ser imponente mas RIDICULA. Barriga proeminente empurrando o uniforme (botoes quase estourando -- 1-2px de gap entre botoes). Boina militar TORTA para o lado esquerdo, quase caindo. Bigode GIGANTE cobrindo 80% da boca -- o bigode e tao grande que parece ter vida propria. Medalhas de papel aluminio no peito (3-4 medalhas, visivelmente FALSAS -- com dobras e amassados). Faixa presidencial amarela/vermelha no torso, tambem torta. Maquiagem involuntaria de palhaco: base branca irregular no rosto, bochechas vermelhas exageradas, nariz levemente vermelho. Olhos tentando parecer serios mas com pupilas minusculas de medo. Maos nos quadris tentando pose de "lider supremo". Outline grosso 2-4px irregular. Cross-hatching nas sombras. Textura de papel.
- **Notas de Estilo:** O ridículo deve ser OBVIO. Nao e um ditador assustador -- e um PALHACO que acha que e ditador. Cada elemento e uma piada visual.

### Frame 1: idle_02 -- Bigode Treme (Esquerda)
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Identico ao Frame 0, exceto: bigode se move 2px para a ESQUERDA. Um lado do bigode levanta como se tivesse vontade propria. Uma gota de suor aparece na testa (1-2px). Olhos se estreitam levemente -- como se estivesse prestes a mentir. O bigode funciona como "detector de mentira invertido": quando o personagem mente, o bigode se MEXE.
- **Notas de Estilo:** O movimento do bigode e a piada central. Deve parecer que o bigode esta VIVO e tentando escapar do rosto.

### Frame 2: idle_03 -- Medalhinha Cai
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Identico ao Frame 0, exceto: uma das medalhas de aluminio se DESCOLA levemente (2px para baixo, pendurada por um fio). Maduro percebe com olhar de panico lateral (pupilas deslocadas). Boca (visivel embaixo do bigode) forma um micro-pout de preocupacao. Boina escorrega mais 1px.
- **Notas de Estilo:** A inseguranca do ditador-palhaco. Suas medalhas falsas nao seguram, sua boina nao para no lugar. Tudo e fachada.

### Frame 3: idle_04 -- Bigode Treme (Direita)
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Identico ao Frame 0, exceto: bigode se move 2px para a DIREITA. Outro lado do bigode levanta. Medalha voltou ao lugar (colou com fita?). Gota de suor do outro lado da testa. Micro-sorriso nervoso sob o bigode.
- **Notas de Estilo:** Loop do idle: 0-1-2-3-0... criando efeito de bigode INQUIETO e ditador ANSIOSO.

---

## Frame-by-Frame: WALK (6 frames, loop)

### Frame 0: walk_01 -- Passo Direito
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Perna direita a frente, esquerda atras. Marcha militar RIDICULA -- pernas levantam DEMAIS (joelhos na altura da barriga), como parada militar de pais comunista exagerada. Barriga balanca para o lado esquerdo com o passo. Medalhas tilintam (2-3px de deslocamento). Bigode aponta na direcao do movimento. Boina quase voando. Braco esquerdo balanca rigido (tentando parecer disciplinado). Braco direito segura a faixa presidencial que escorrega.
- **Notas de Estilo:** A marcha deve parecer a de alguem que VIU marchas militares na TV e esta imitando mal.

### Frame 1: walk_02 -- Transicao
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Ambas as pernas quase juntas, momento de transicao. Corpo levemente mais alto (1-2px) no bounce. Barriga no centro. Medalhas ainda em movimento (inercia). Bigode tremendo com o impacto do passo.

### Frame 2: walk_03 -- Passo Esquerdo
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Perna esquerda a frente, direita atras. Mirror do Frame 0 com ajustes. Barriga balanca para direita. Uma medalha se solta parcialmente. Bigode para o outro lado.

### Frame 3: walk_04 -- Transicao 2
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Transicao novamente. Corpo no ponto mais baixo do bounce (1px mais baixo que frames de transicao). Medalha se reposiciona. Gota de suor se forma (cansaco -- ditadores nao sao atleticos).

### Frame 4: walk_05 -- Tropeço Leve
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** A cada 2 ciclos de walk, Maduro TROPECA levemente. Corpo inclina 5-8 graus para frente. Boina voa 3px para cima. Olhos arregalados em micro-panico. Maos se abrem tentando equilibrar. Uma medalha voa. O bigode fica ERETO de susto (como gato assustado).
- **Notas de Estilo:** O tropeco e essencial para a comedia. Ninguem respeita um ditador que tropeca.

### Frame 5: walk_06 -- Recuperacao
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Se recompoe rapidamente. Finge que nada aconteceu. Postura exageradamente ereta (overcompensando). Queixo erguido. Medalha de volta (grudada com fita visivel). Bigode se achata de volta. Expressao de "eu QUIS fazer isso".

---

## Frame-by-Frame: ATTACK -- Ditadura Express (8 frames)

### Frame 0: atk_01 -- Wind-up
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Maduro puxa um MEGAFONE GIGANTE (32x20px) de tras das costas. O megafone e desproporcional -- quase do tamanho do torso. Decorado com estrelas venezuelanas e adesivos "Revolucion". Corpo se inclina para tras carregando o peso. Barriga empinada. Bigode ERIÇA de excitacao.

### Frame 1: atk_02 -- Preparacao
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Megafone posicionado na boca (embaixo do bigodao). Olhos fechados com forca -- concentracao MAXIMA. Peito inflado (inhala profundamente). Corpo se expande 2px em todas as direcoes (squash-stretch). Medalhas tremem com a vibracao do peito.

### Frame 2: atk_03 -- GRITO Inicial
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** BOCA ABERTA (bigode se parte ao meio temporariamente, revelando boca gritando). Megafone emite ONDA SONORA visivel -- circulos concentricos saindo (3-4 arcos, cores verde/amarelo doentio). Corpo empurrado para tras pelo recuo. Boina voa. Notas de bolivar DESVALORIZADAS voam para fora do megafone junto com o som (2-3 notas de papel, marrom/verde).

### Frame 3: atk_04 -- Grito Maximo
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Ondas sonoras no MAXIMO (preenchem 50% do frame). Dentro das ondas: frases visiveis em micro-texto ("IMPERIALISMO!", "REVOLUCION!"). Maduro no canto esquerdo, comprimido pelo recuo. Notas de bolivar agora sao uma CHUVA. Medalhas todas voaram. Bigode horizontal como bandeira ao vento.

### Frame 4: atk_05 -- Zona de Ditadura (efeito)
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** Area de efeito se forma no chao: circulo vermelho/dourado com estrela venezuelana distorcida. Dentro da zona: regras invertidas (representado por icones de setas invertidas, sinais de interrogacao). Gas verde doentio emana das bordas. Maduro sorri (bigode levanta nas pontas formando curva).

### Frame 5: atk_06 -- Zona Ativa
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Zona completamente ativa. Efeitos caoticos dentro: notas de dinheiro girando, setas de direcao trocadas, icones de confusao. Maduro faz pose de "lider supremo" com uma mao erguida (estilo propaganda sovietica, mas patetico). Gas verde no pico.

### Frame 6: atk_07 -- Zona Enfraquecendo
- **Posicao no sheet:** 384,0 a 447,63
- **Descricao:** Efeitos diminuem. Zona fica mais transparente. Notas de dinheiro caem no chao. Gas se dissipa. Maduro percebe que o efeito ta acabando -- expressao de panico. Tenta gritar mais no megafone mas sai so ESTÁTICA.

### Frame 7: atk_08 -- Fim do Ataque
- **Posicao no sheet:** 448,0 a 511,63
- **Descricao:** Zona some. Maduro fica de pe segurando megafone apagado, ofegante. Suor escorrendo. Medalhas no chao ao redor. Boina caida sobre um olho. Bigode caido (triste). Expressao de "isso costumava funcionar".

---

## Frame-by-Frame: SKILL 1 -- Passa Pano (6 frames)

### Frame 0: passapano_01 -- Procura o Lula
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Maduro olha ao redor desesperadamente procurando Lula no mapa. Olhos grandes e pidoes. Maos juntas em posicao de "por favor". Bigode tremendo de medo. Boca forma um bico (visivel embaixo do bigode).

### Frame 1: passapano_02 -- Corre Pro Lula
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Maduro corre em direcao a Lula (direcao variavel). Corrida COMICA -- bracos para cima, boina voando, barriga balancando. Megafone abandonado no chao. Lagrimas comicas voando (2-3px).

### Frame 2: passapano_03 -- Se Esconde Atras
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Maduro se posiciona ATRAS de Lula (se Lula estiver no mapa). Aparece so o bigode e os olhos por cima do ombro de Lula. Maos agarrando as costas de Lula.

### Frame 3: passapano_04 -- Escudo Ativa
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Campo de energia se forma entre Maduro e Lula. Escudo circular com cor vermelha (PT) e estrelas. Texto micro "COMPANHEIRO" aparece no escudo. Maduro sorri de alivio. Bigode relaxa.

### Frame 4: passapano_05 -- Escudo Maximo
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** Escudo no maximo. Ataques ricocheteiam visivelmente. Maduro da joinha por tras do escudo. Expressao de "eu SEMPRE tive amigos poderosos".

### Frame 5: passapano_06 -- Escudo Desvanece
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Escudo fica transparente. Lula se afasta (cansou de passar pano). Maduro tenta segurar mas Lula ja foi. Expressao de abandono. Bigode cai. Sozinho de novo.

---

## Frame-by-Frame: SKILL 2 -- Plano Economico Absurdo (6 frames)

### Frame 0: plano_01 -- Ideia
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Lampada acende sobre a cabeca de Maduro (mas a lampada e uma NOTA DE DINHEIRO brilhando). Dedo erguido -- "EUREKA!". Olhos brilhando de loucura. Bigode aponta para cima de excitacao. Expressao maniacalmente feliz.

### Frame 1: plano_02 -- Puxa o Quadro
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Puxa do nada um QUADRO BRANCO com graficos ABSURDOS: setas apontando para todos os lados, numeros impossiveis ("PIB = infinito", "Inflacao = -500%"), graficos de pizza com 200%. O quadro e maior que ele (cobre 40% do frame).

### Frame 2: plano_03 -- Explica o Plano
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Aponta para o quadro com bastao (bastao e um SALAME?). Expressao de professor lunático. Graficos no quadro MUDAM SOZINHOS (numeros trocam). Notas de bolivar comecam a cair do ceu como neve.

### Frame 3: plano_04 -- Implementacao
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Area de efeito se forma: zona de CAOS ECONOMICO. Dentro da zona: precos mudam aleatoriamente (icones de setas subindo/descendo), dinheiro perde valor visivelmente (notas ficam transparentes), regras da fase se invertem. Maduro conduz como maestro com os bracos.

### Frame 4: plano_05 -- Caos Total
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** Zona no pico de caos. Tudo invertido. Maduro danÇa de alegria no meio da destruicao (danca CRINGE -- tipo salsa mal feita). Bigode gira como helice. Medalhas orbitam ao redor dele. Notas voando por todos os lados.

### Frame 5: plano_06 -- Resultado
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Zona se desfaz. Destruicao visivel: icones quebrados, notas no chao sem valor. Maduro olha ao redor surpreso, como se NAO esperasse esse resultado. Quadro branco pegou fogo. Expressao: "...mas no PowerPoint funcionava".

---

## Frame-by-Frame: HIT / DANO (3 frames)

### Frame 0: hit_01 -- Impacto
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Flash branco no corpo todo (50% opacidade). Corpo comprimido (squash horizontal). Boina voa. Todas as medalhas voam para fora. Bigode se DESPREGA parcialmente (um lado solta). Olhos arregalados MAXIMOS. Boca aberta redonda de choque.

### Frame 1: hit_02 -- Reacao
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Corpo volta com bounce (stretch vertical). Medalhas ainda no ar. Bigode preso por um fio. Lagrimas comicas (4-5 gotas). Grita "LULA!" (balao de fala minusculo). Bracos para cima em panico.

### Frame 2: hit_03 -- Recuperacao
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Recolhe medalhas do chao apressadamente. Gruda bigode de volta (com fita visivel). Endireita boina. Tenta recuperar dignidade. Postura exageradamente ereta novamente. Expressao furiosa tentando esconder medo.

---

## Frame-by-Frame: DEATH (8 frames, NAO loop)

### Frame 0: death_01 -- Golpe Final
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Impacto fatal. Corpo arqueado para tras dramaticamente. Bigode se SEPARA do rosto completamente (voa como entidade independente). Boina voa para fora do frame. Todas as medalhas explodem para fora.

### Frame 1: death_02 -- Queda Dramatica
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Maduro caindo para tras. Mao estendida tentando agarrar o bigode que voa. Faixa presidencial se desenrola. Maquiagem de palhaco fica MAIS VISIVEL (base branca, bochechas vermelhas -- sempre esteve la, agora e inegavel).

### Frame 2: death_03 -- No Chao
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Corpo no chao, barriga para cima. Uniforme rasgado revelando camiseta por baixo com estampa de "I LOVE SOCIALISMO" (ou similar). Medalhas espalhadas ao redor -- CLARAMENTE de papel aluminio agora.

### Frame 3: death_04 -- Bigode Retorna
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** O bigode, como entidade viva, VOLTA voando e pousa no rosto de Maduro. Mas pousa ERRADO -- de lado, ou de ponta cabeca. O bigode tenta se ajeitar sozinho.

### Frame 4: death_05 -- Ultima Tentativa
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** Maduro tenta se levantar apoiado no megafone. Nao consegue. Megafone quebra embaixo dele. Barriga impede de rolar. Bigode finalmente no lugar mas tremendo.

### Frame 5: death_06 -- Discurso Final
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Ainda no chao, levanta o megafone quebrado e tenta gritar. Sai apenas um SOM TRISTE (onomatopeia "pfrrrt" em balao). Notas de bolivar desvalorizadas caem como confete ao redor.

### Frame 6: death_07 -- Desinflando
- **Posicao no sheet:** 384,0 a 447,63
- **Descricao:** Corpo comeca a DESINFLAR como balao. Uniforme fica frouxo. Barriga encolhe. E como se a persona de ditador fosse AR QUENTE e agora esta vazando. Bigode murcha junto. Som de balao desinflando (representado por linhas onduladas de ar saindo).

### Frame 7: death_08 -- Palhaco Revelado
- **Posicao no sheet:** 448,0 a 511,63
- **Descricao:** Frame final. Maduro e agora visivelmente so um PALHACO caido. Uniforme vazio ao redor como roupa descartada. Maquiagem de circo agora 100% visivel e impossivel de negar. Nariz de palhaco vermelho brilhando. Bigode ao lado, inerte, finalmente morto. Medalhas de aluminio amassadas. Uma unica nota de bolivar pousa sobre o corpo -- escrito "SEM VALOR". Fade gradual para transparencia.

---

## Sprite Sheets Summary

| Sheet            | Frames | Tamanho Sheet       | FPS  | Loop  |
|------------------|--------|---------------------|------|-------|
| idle             | 4      | 256x64px            | 8    | Sim   |
| walk             | 6      | 384x64px            | 10   | Sim   |
| attack_ditadura  | 8      | 512x64px            | 10   | Nao   |
| skill_passapano  | 6      | 384x64px            | 8    | Nao   |
| skill_plano      | 6      | 384x64px            | 8    | Nao   |
| hit              | 3      | 192x64px            | 12   | Nao   |
| death            | 8      | 512x64px            | 8    | Nao   |

---

## Projeteis e Efeitos (32x32px)

### Onda Sonora (Ditadura Express)
- **Frames:** 4
- **Descricao:** Arcos concentricos verde-doentio/amarelo saindo do megafone. Dentro dos arcos: micro-icones de estrelas venezulanas e notas de bolivar. Cada frame o arco se expande. Linhas irregulares (nao circulos perfeitos).

### Nota de Bolivar (Plano Economico)
- **Frames:** 4 (rotacao)
- **Descricao:** Nota de dinheiro girando no ar. Comeca verde, vai ficando marrom/transparente (desvalorizando em tempo real). Numeros no canto mudam a cada frame (100 -> 1.000 -> 1.000.000 -> "???"). Papel amassado e sujo.

### Escudo Passa Pano
- **Frames:** 3
- **Descricao:** Bolha de protecao vermelha com estrela do PT. Pulsa levemente. Textura oleosa (o "pano" sendo passado). Particulas vermelhas orbitando.

---

## Phaser 3 Atlas Keys

```
key: 'maduro_idle'          frameWidth: 64  frameHeight: 64
key: 'maduro_walk'          frameWidth: 64  frameHeight: 64
key: 'maduro_attack'        frameWidth: 64  frameHeight: 64
key: 'maduro_passapano'     frameWidth: 64  frameHeight: 64
key: 'maduro_plano'         frameWidth: 64  frameHeight: 64
key: 'maduro_hit'           frameWidth: 64  frameHeight: 64
key: 'maduro_death'         frameWidth: 64  frameHeight: 64
key: 'maduro_proj_onda'     frameWidth: 32  frameHeight: 32
key: 'maduro_proj_bolivar'  frameWidth: 32  frameHeight: 32
key: 'maduro_proj_escudo'   frameWidth: 32  frameHeight: 32
```

---

## Notas para o Artista

1. **O BIGODE e o personagem.** Ele se move independente, reage ao humor, tem personalidade propria. Se o bigode nao parece VIVO, o sprite falhou.
2. **Medalhas sao FALSAS.** Devem parecer feitas de papel aluminio de cozinha. Amassadas, brilho barato, cola aparente.
3. **A maquiagem de palhaco e INVOLUNTARIA.** Maduro nao sabe que parece palhaco. A maquiagem esta "embaixo" da pele, como se fosse sua verdadeira natureza.
4. **Proporcoes Crumb:** Cabeca 1.5x maior que o normal, torso largo e barrigudo, pernas curtas e grossas.
5. **Linhas GROSSAS e IRREGULARES (2-4px).** Nunca linhas finas ou uniformes. O tremor da mao e intencional.
6. **Cross-hatching nas sombras.** Nao usar gradientes suaves -- usar linhas cruzadas para sombra.
7. **A barriga SEMPRE se move.** Em todo frame, a barriga tem inercia propria, como gelatina.
8. **Boina SEMPRE torta.** Nunca centralizada, nunca correta. Sempre prestes a cair.
9. **Inspiracao visual direta:** Caricaturas do Andre Guedes do Maduro no TikTok -- distorcao grotesca, cores sujas, humor acido.
10. **NÃO e um ditador ASSUSTADOR. E um ditador PATETICO.** Toda escolha visual deve reforcar o ridiculo.
