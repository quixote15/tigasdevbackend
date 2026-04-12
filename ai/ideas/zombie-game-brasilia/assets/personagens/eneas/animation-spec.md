# ENEAS CARNEIRO (O Fantasma Patriota) -- Especificacao de Animacao

## Diretrizes Globais

- **Framerate base**: 8-10fps (jerky como o style guide, porem com transicoes levemente mais suaves que outros personagens -- Eneas merece essa diferenciacao)
- **Efeito holograma**: PERMANENTE. Em todos os ciclos, sem excecao. Alpha corpo 55-75%, bigode 75-85%, scanlines 8% sempre.
- **Bigode**: Elemento de animacao INDEPENDENTE. Tem seu proprio ciclo de "respiracao" de 4 frames que se sobrepoem a qualquer outra animacao. O bigode e um sub-sprite com animacao propria.
- **Capa/Bandeira**: Segundo elemento independente. Physics de tecido simplificada (3 frames de ondulacao em loop).
- **Particulas**: Sistema de particulas separado -- NAO baked nos sprites. 3-5 particulas douradas subindo a todo momento.
- **Afterimage**: No movimento, copias fantasma com alpha decrescente (20% -> 10% -> 5%) nos 3 frames anteriores.

---

## 1. IDLE -- Flutuacao Serena

### Configuracao
| Parametro | Valor |
|---|---|
| Frames | 4 |
| Framerate | 8fps |
| Duracao do ciclo | 0.5s |
| Loop | Sim (infinito) |
| Sprite sheet | `eneas_idle.png` 256x64px |

### Timeline

```
Frame 0 (0.000s): Posicao base
  - Corpo: posicao Y+0, alpha 60%
  - Bigode: simetrico, pontas retas, alpha 80%
  - Capa: pendendo levemente para direita (+2px X offset borda inferior)
  - Aura: alpha 15%, raio 28px
  - Scanlines: offset Y+0

Frame 1 (0.125s): Inicio da flutuacao
  - Corpo: posicao Y-1 (subindo), alpha 65%
  - Bigode: ponta direita +1px Y (sobe), ponta esquerda -1px Y (desce)
  - Capa: retornando ao centro
  - Aura: alpha 20%, raio 30px
  - Scanlines: offset Y+1 (descem 1px)

Frame 2 (0.250s): Pico da flutuacao
  - Corpo: posicao Y-2 (ponto mais alto), alpha 70%
  - Bigode: ponta esquerda +1px Y (sobe), ponta direita -1px Y (desce) -- INVERTE
  - Capa: fluindo para esquerda (-2px X offset borda inferior)
  - Aura: alpha 25%, raio 32px (MAXIMO)
  - Scanlines: offset Y+2
  - Edge glow: ON (1px branco alpha 30% ao redor do contorno)

Frame 3 (0.375s): Descida
  - Corpo: posicao Y-1 (descendo), alpha 65%
  - Bigode: retornando a quase-simetrico (micro-tremor 1px)
  - Capa: retornando ao centro com ondulacao
  - Aura: alpha 20%, raio 30px
  - Scanlines: offset Y+3 (loop de scanline e independente)
  - Edge glow: OFF

-> Loop para Frame 0
```

### Bigode -- Sub-animacao Independente (overlay)
O bigode tem seu PROPRIO ciclo de 4 frames que roda EM CIMA da animacao idle:

```
Bigode Frame 0: Simetrico. Pontas retas.
Bigode Frame 1: Ponta direita ondula +1px para cima.
Bigode Frame 2: Ambas as pontas ondulam +1px para cima (bigode "sorri").
Bigode Frame 3: Ponta esquerda ondula +1px para cima, direita volta.

O ciclo do bigode roda a 6fps (nao 8fps como o corpo).
Isso cria uma DESSINCRONIZACAO intencional entre corpo e bigode,
reforçando que o bigode tem vida propria.
```

---

## 2. WALK / FLUTUACAO DIRECIONAL

### Configuracao
| Parametro | Valor |
|---|---|
| Frames | 6 |
| Framerate | 10fps |
| Duracao do ciclo | 0.6s |
| Loop | Sim |
| Sprite sheet | `eneas_walk.png` 384x64px |
| Direcoes | 4 (up, down, left, right) ou 8 com flip horizontal |

### Timeline

```
Frame 0 (0.000s): Inicio do deslizamento
  - Corpo: inclinacao 3deg na direcao do movimento
  - Pes: juntos, 3px acima do chao
  - Bigode: APONTA na direcao do movimento (bussola!) -- pontas viram
  - Capa: arrasto na direcao OPOSTA ao movimento
  - Afterimage: nenhum ainda
  - Alpha corpo: 60%

Frame 1 (0.100s): Aceleracao
  - Corpo: avanca 1px na direcao
  - Afterimage FRAME 0 aparece na posicao anterior, alpha 20%
  - Bigode: continua apontando, pontas oscilam levemente
  - Capa: estica para tras (5px offset oposto)
  - Alpha corpo: 65%
  - Particulas: trail dourado comeca a se formar atras

Frame 2 (0.200s): Velocidade maxima
  - Corpo: avanca mais 1px
  - Afterimage FRAME 0: alpha 10% (esmaecendo)
  - Afterimage FRAME 1: alpha 20% (novo)
  - Bigode: vibra levemente (blur de 1px nas pontas)
  - Capa: totalmente esticada, ondulando rapidamente
  - Alpha corpo: 75% (MAIS visivel em alta velocidade -- efeito Doppler fantasma)
  - Scanlines: deslocamento 2px/frame (acelerado)
  - Trail dourado: 4px de comprimento atras

Frame 3 (0.300s): Sustentacao
  - Espelho do Frame 1 com variacao: bracos em posicao diferente
  - Afterimages continuam em cascata
  - Bigode: alinha pontas (uma 2px a frente da outra, efeito aerodinamico)
  - Alpha corpo: 70%

Frame 4 (0.400s): Inicio de desaceleracao visual (para loop suave)
  - Afterimage mais antigo desaparece
  - Bigode: começa a relaxar direcionalidade
  - Capa: reduz oscilacao
  - Alpha corpo: 65%

Frame 5 (0.500s): Transicao para loop
  - Afterimages se dissolvem
  - Bigode: posicao direcional suave (ainda aponta, mas menos intenso)
  - Corpo retorna a inclinacao de 3deg
  - Alpha corpo: 60%

-> Loop para Frame 0
```

### Nota sobre Direcoes
- **Esquerda/Direita**: Usar flip horizontal do sprite. O bigode e a capa sao espelhados.
- **Cima**: Eneas visto de costas. Bigode NAO visivel (so pontas saem dos lados da cabeca). Capa MUITO visivel (flui para baixo/atras).
- **Baixo**: Eneas visto de frente. Bigode em MAXIMO destaque. Capa oculta atras.

---

## 3. APARICAO / SPAWN -- Sequencia Epica

### Configuracao
| Parametro | Valor |
|---|---|
| Frames | 8 |
| Framerate | 8fps |
| Duracao | 1.0s |
| Loop | NAO (toca uma vez) |
| Sprite sheet | `eneas_spawn.png` 512x64px |
| Trigger | HP do jogador < 10% |

### Timeline Detalhada

```
Frame 0 (0.000s): Presagio
  [EFEITO NO JOGO]: Tela treme 1px por 0.125s. Audio: ruido de frequencia baixa.
  - Visual: ponto de luz dourada 2x2px surge no centro do ponto de spawn
  - Nenhum personagem visivel ainda
  - Particulas: 1 unica particula dourada piscando no ponto

Frame 1 (0.125s): O Bigode Precede
  [EFEITO NO JOGO]: NPCs num raio de 128px reduzem velocidade 50%.
  - Ponto de luz expande para 8x8px circulo dourado
  - DENTRO do circulo: silhueta do BIGODE comeca a se formar (alpha 25%)
  - So o bigode. Nada mais. O bigode lidera a existencia.
  - Scanlines comecam dentro do circulo
  - Distorcao: pixels num raio de 12px do centro tremem 1px

Frame 2 (0.250s): O Bigode Se Revela
  [EFEITO NO JOGO]: Audio "reverb crescendo" começa.
  - Circulo de luz: 20x20px
  - Bigode CLARAMENTE visivel flutuando sem rosto (alpha 45%)
  - Contorno vago de cabeca comeca a se formar atras do bigode (alpha 15%)
  - Ondulacoes concentricas de energia dourada saem do centro (2 aneis)
  - Distorcao: raio de 16px, pixels tremem 1px aleatorio

Frame 3 (0.375s): Materializacao Parcial
  [EFEITO NO JOGO]: Audio crescendo intensifica.
  - Cabeca e torso superior materializam (alpha 35%)
  - Bigode: alpha 60% (sempre a frente)
  - Capa/bandeira comeca como ondulacoes de cor atras do torso
  - Circulo de luz se transforma em AURA ao redor do corpo
  - Distorcao vertical (linhas de interferencia de TV) nos 16px mais proximos

Frame 4 (0.500s): Quase Completo
  [EFEITO NO JOGO]: TODOS os personagens na tela pausam por 1 frame. Flash branco alpha 5%.
  - Corpo quase completo (alpha 50%), pernas se formam de cima para baixo
  - Bigode: alpha 70%
  - Aura dourada no MAXIMO (raio 8px, alpha 35%)
  - Capa comeca a esvoaçar
  - Passiva "O Verdadeiro Patriota" ativa: onda dourada visivel

Frame 5 (0.625s): Manifestacao Completa
  [EFEITO NO JOGO]: Audio "MEU NOME E ENEAS!" comeca a buildar (reverb crescendo).
  - Corpo COMPLETO (alpha 55%)
  - Postura ereta, militar
  - Bigode: alpha 80% (quase solido)
  - Capa flui completamente
  - EXPLOSAO de particulas: 8-12 particulas douradas disparam em todas as direcoes
  - NPCs proximos OLHAM para Eneas (suas sprites giram para encara-lo)

Frame 6 (0.750s): O Grito
  [AUDIO SYNC]: "MEU NOME E ENEAS!" toca EXATAMENTE neste frame.
  [EFEITO NO JOGO]: Screen shake leve (2px, 0.25s). Stun em inimigos no raio de 96px.
  - Alpha estabiliza (corpo 65%, bigode 80%)
  - Explosao de particulas se acalma
  - Eneas LEVANTA O QUEIXO com autoridade absoluta
  - O bigode faz um FLUTTER dramatico (pontas sobem 3px e descem em 1 frame)
  - Ondas sonoras visiveis: 3 arcos de 1px dourado saindo da boca

Frame 7 (0.875s): Estabilizacao
  [EFEITO NO JOGO]: Jogo retorna ao normal. "Saudade do Que Nao Tivemos" (passiva) ativa.
  - Todos os valores se estabilizam nos niveis de idle
  - Aura reduz para nivel padrao
  - Particulas em velocidade normal
  - Bigode: ultimo flutter, retorna a posicao neutra
  - Eneas faz um aceno MINIMO com a cabeca
  - Transicao suave para ciclo IDLE

-> Transiciona para IDLE loop
```

### Easing da Aparicao
```
Alpha do corpo: ease-in-out
  0.0s: 0% -> 0.5s: 50% -> 1.0s: 65%

Alpha do bigode: ease-out (rapido no inicio)
  0.0s: 0% -> 0.25s: 45% -> 0.5s: 70% -> 1.0s: 80%

Raio da aura: elastic overshoot
  0.0s: 0px -> 0.5s: 8px (MAXIMO) -> 1.0s: 5px (padrao)

Distorcao: ease-out
  0.0s: 0px -> 0.25s: 1px -> 0.5s: 1px -> 0.75s: 0px -> 1.0s: 0px
```

---

## 4. GRITO PATRIOTA -- Ataque Principal

### Configuracao
| Parametro | Valor |
|---|---|
| Frames | 4 |
| Framerate | 10fps |
| Duracao | 0.4s |
| Loop | NAO |
| Sprite sheet | `eneas_grito.png` 256x64px |
| Cooldown | 5s |
| Area de efeito | Cone frontal, 120 graus, 96px raio |
| Dano | Alto (stun massivo + dano medio) |

### Timeline

```
Frame 0 (0.000s): Inspiracao -- 0.1s
  - Torso EXPANDE 2px (peito inflando)
  - Bigode se COMPRIME (pontas vao para frente, como orelhas de gato em alerta)
  - Boca comeca a aparecer (normalmente escondida pelo bigode)
  - Aura CONCENTRA-SE: raio diminui de 5px para 3px, alpha sobe de 20% para 35%
  - O corpo fica MAIS opaco (alpha 75%) -- concentrando energia

Frame 1 (0.100s): Abertura -- 0.1s
  - BOCA ABERTA: visivel pela primeira vez sob o bigode
  - Bigode SE ERGUE: pontas apontam 45deg para cima (posicao impossivel)
  - A boca e ENORME, exagerada, ocupa metade da cabeca (estilo grotesco)
  - Ondas sonoras Frame 1: 3 arcos de 1px saindo da boca a 4px de distancia
    Cores alternadas: #FFD700 e #F0F0E8, alpha 60%
  - Screen shake INICIA: 1px por frame

Frame 2 (0.200s): PICO DO GRITO -- 0.1s
  [AUDIO]: "ENEAS!" (pico do audio) NESTE frame
  - Ondas sonoras se expandem para 16px da boca
  - TEXTO "ENEAS!" se forma DENTRO das ondas de choque
    (as letras sao compostas pelas proprias ondas -- nao sobrepostas)
  - Bigode VIBRA violentamente (blur de 2px horizontal)
  - Corpo atinge MAXIMO alpha: 80% (quase corporeo)
  - Particulas sao EMPURRADAS pelas ondas (se afastam do Eneas)
  - Capa esvoaça na direcao oposta (soprada pelo grito)
  - Aura EXPLODE: raio 10px, alpha 40%
  - Screen shake: 2px por frame
  [GAMEPLAY]: Hit detection neste frame. Stun de 1.5s em inimigos no cone.

Frame 3 (0.300s): Aftershock -- 0.1s
  - Ondas passam e se dissipam (alpha 20%, continuam expandindo)
  - Bigode DESCE lentamente para posicao normal
  - Boca se fecha (bigode cobre novamente)
  - Alpha retorna para 65% (desaceleracao de opacidade)
  - Particulas desaceleram e retomam flutuacao normal
  - Eco visual: 1 onda residual alpha 15% se dissipando
  - Aura retorna a raio 5px, alpha 20%
  - Screen shake: cessa

-> Retorna para IDLE
```

---

## 5. PROJETIL "56!" -- Lancamento e Voo

### 5a: Lancamento (personagem, 64x64px)
| Parametro | Valor |
|---|---|
| Frames | 4 |
| Framerate | 10fps |
| Duracao | 0.4s |
| Loop | NAO |

```
Frame 0 (0.000s): Mao estendida, ponto de luz dourada na palma (2x2px).
  Bigode APONTA para o alvo como mira.

Frame 1 (0.100s): "5" e "6" se formam na palma. Energia dourada se acumula.
  Os numeros se constroem pixel por pixel, de baixo para cima.

Frame 2 (0.200s): "56" completo na palma. 16x12px, dourado com outline vermelho.
  O "56" flutua 4px acima da mao, pronto para lancamento.
  Brilho intenso -- flash branco 1px ao redor.

Frame 3 (0.300s): LANCAMENTO. Gesto de empurrar. O "56" SAI do sprite do personagem
  na direcao apontada pelo bigode. Linhas de velocidade (3 rastros brancos).
  Flash na mao. Bigode recua 2px pelo impacto do lancamento.
  [SPAWN]: Projetil "56" e criado como entidade separada neste frame.
```

### 5b: Projetil em Voo (projetil, 32x32px)
| Parametro | Valor |
|---|---|
| Frames | 4 |
| Framerate | 12fps |
| Duracao do ciclo | 0.333s |
| Loop | Sim (ate impacto) |
| Velocidade | 180px/s |
| Alcance | 256px |

```
Frame 0: "56" legivel, rotacao 0deg.
  Aura dourada 2px. Linhas de velocidade atras. Alpha 90%.

Frame 1: "56" inclinado +15deg. Aura pulsa fraco (alpha 15%).
  1 particula se solta. Linhas de velocidade mais longas.

Frame 2: "56" inclinado -15deg. Aura pulsa forte (alpha 30%).
  Trail dourado de 4px. Mais particulas.

Frame 3: "56" volta a 0deg. Microvariacoes. Loop.
```

### 5c: Impacto do "56" (efeito, 32x32px)
| Parametro | Valor |
|---|---|
| Frames | 3 |
| Framerate | 10fps |
| Duracao | 0.3s |
| Loop | NAO |

```
Frame 0: IMPACTO. "56" se comprime contra o alvo (squash horizontal).
  Explosao de 6-8 particulas douradas radiais.
  Flash branco 4px raio no ponto de contato.
  Texto "56!" aparece em vermelho e dourado (estilo THWACK/PLONK dos outros projeteis).

Frame 1: Numeros "5" e "6" se SEPARAM e voam em direcoes opostas.
  "5" vai para cima-esquerda, "6" vai para baixo-direita (ou vice-versa).
  Cada numero com trail de 2px. Flash se expande e esmaece.
  Particulas se espalham mais. Dano aplicado.

Frame 2: "5" e "6" se desfazem em particulas douradas.
  Flash desaparece. Particulas flutuam e desaparecem.
  Residuo visual: circulo dourado alpha 10% no ponto de impacto por 0.5s.
```

---

## 6. APARICAO FANTASMA -- Skill de Teleporte/Dano

### Configuracao
| Parametro | Valor |
|---|---|
| Frames | 6 |
| Framerate | 8fps |
| Duracao | 0.75s |
| Loop | NAO |
| Cooldown | 12s |

### Timeline

```
Frame 0 (0.000s): Eneas comeca a desvanecer no local atual.
  Alpha corpo: 65% -> 30%. Efeito de "dissolucao" -- pixels do corpo aleatorios
  ficam transparentes (efeito dither). Bigode: alpha 80% -> 50%.

Frame 1 (0.125s): Eneas e apenas uma silhueta de particulas douradas no local original.
  Alpha corpo: 10%. Particulas dominam. Nuvem de 12-16 particulas.

Frame 2 (0.250s): LOCAL ORIGINAL vazio. Particulas se dispersam.
  NOVO LOCAL: ponto de luz dourada aparece (identico ao spawn Frame 1).
  [TELEPORTE INSTANTANEO]: sprite muda de posicao.

Frame 3 (0.375s): No novo local: bigode se materializa primeiro (alpha 50%).
  Onda de choque: circulo de 1px dourado se expande do ponto (ataque).
  [DANO]: Inimigos num raio de 48px levam dano no momento da materializacao.

Frame 4 (0.500s): Corpo se materializa rapidamente (alpha 40% -> 60% em 1 frame).
  Onda de choque continua expandindo (raio 32px -> 64px).
  Bigode: alpha 75%.

Frame 5 (0.625s): Totalmente materializado no novo local.
  Onda de choque se dissipa. Alpha padrao restaurado.
  Bigode faz flutter dramatico. Pose de autoridade.

-> Retorna para IDLE no novo local
```

---

## 7. SAUDADE DO QUE NAO TIVEMOS -- Passiva Aura

### Configuracao
| Parametro | Valor |
|---|---|
| Efeito visual | Aura dourada permanente no raio de 128px ao redor de Eneas |
| Buff | +20% dano aliados na area |
| Frames (da aura) | 4 (loop continuo) |
| Framerate | 6fps |

### Visual da Aura
```
A aura de buff e um efeito de CHAO, nao do personagem.
Circulo dourado semi-transparente no chao, raio 128px.

Frame 0: Circulo com borda definida (1px #FFD700 alpha 30%), interior alpha 5%.
  3-4 particulas flutuam na area.

Frame 1: Borda pulsa (alpha 35%), interior alpha 8%.
  Particulas se movem levemente.

Frame 2: Borda no maximo (alpha 40%), interior alpha 10%.
  Novas particulas surgem. Efeito de "calor" (distorcao de 1px nos pixels do chao).

Frame 3: Borda diminui (alpha 35%), interior alpha 7%.
  Transicao suave para loop.

Aliados DENTRO da aura recebem um sutil glow dourado (overlay #FFD700 alpha 8%)
em seus sprites, indicando o buff ativo.
```

---

## 8. ULTIMATE: "MEU NOME E ENEAS!" -- Sequencia Cinematica Completa

### Configuracao CRITICA
| Parametro | Valor |
|---|---|
| Frames totais | 10 (misto de tamanhos) |
| Duracao total | 4.0s |
| Loop | NAO (UNICA por partida) |
| Trigger | HP < 10% + input do jogador |
| Dano | MASSIVO em todos os inimigos na tela |
| Debuff | "Respeito" -- -30% velocidade e -20% dano por 10s |

### Timeline Completa

```
=== FASE 1: ASCENSAO (frames 0-1, 0.0-0.8s, 64x64) ===

Frame 0 (0.000s, duracao 0.4s):
  [TRIGGER]: HP < 10% confirmado. Input aceito.
  [AUDIO]: Reverb baixo começa. Musica do jogo PARA.
  [EFEITO]: Tela escurece levemente (overlay preto alpha 15%).
  - Eneas treme (shake 1px). Alpha desce para 40% (quase invisivel).
  - O bigode BRILHA: alpha SOBE para 90% (contrastando com corpo apagado).
  - Aura EXPLODE para raio 12px, alpha 40%.
  - Eneas comeca a SUBIR (flutua +8px acima do normal).
  - Bracos se abrem lentamente para os lados.

Frame 1 (0.400s, duracao 0.4s):
  [AUDIO]: Crescendo dramatico. Batida de timpano.
  [EFEITO]: Tela escurece mais (overlay preto alpha 25%).
  - Eneas no ponto mais alto da flutuacao (+16px).
  - Bracos totalmente abertos -- pose de cruz/ascensao.
  - Capa se abre como ASAS atras dele, totalmente esticada.
  - Particulas douradas VOAM para cima (20+ particulas).
  - Alpha corpo: 50%. Bigode: 90%. Aura: raio 16px.
  - Todos os personagens na tela PARAM (freeze frame).

=== FASE 2: MANIFESTACAO DO ROSTO (frames 2-6, 0.8-2.8s, 256x256) ===

Frame 2 (0.800s, duracao 0.4s):
  [TRANSICAO]: Sprite 64x64 faz ZOOM IN. Camera se aproxima do rosto.
  [EFEITO]: Transicao para sprite 256x256. Overlay fullscreen.
  - O ROSTO do Eneas preenche a tela progressivamente.
  - Olhos serios, determinados, dourados.
  - Bigode ENORME ocupa 1/3 inferior (still o mais opaco).
  - Background: ceu laranja-sangue (#FF6B35 -> #8B0000).
  - Scanlines dramaticas (alpha 12% -- mais fortes que normal).
  - "ENEAS" comeca a se formar em letras douradas atras do rosto.

Frame 3 (1.200s, duracao 0.4s):
  [AUDIO]: Silencio tenso. Pausa dramatica.
  [EFEITO]: O rosto esta QUASE SOLIDO (alpha 85%!). O fantasma se torna REAL pela forca
  da vontade pura.
  - Boca comeca a ABRIR.
  - Bigode se ERGUE (preparando para o grito).
  - Letras "ENEAS" completas e brilhando atras.
  - RACHADURA #1: linha diagonal no canto superior esquerdo.
    Cor: #F0F0E8 alpha 90%. 2px de espessura.
    Fragmentos minusculos (2px) se desprendem.

Frame 4 (1.600s, duracao 0.4s):
  [AUDIO]: "MEU NOME E..." (inicio do grito, voz TREMENDO a tela).
  [EFEITO]: Screen shake INTENSO (3px por frame, aleatorio).
  - Ondas sonoras MASSIVAS da boca: 5-7 arcos concentricos
    Cores: #FFD700 e #F0F0E8 alternados, alpha 50-70%.
    Se expandem da boca para as bordas do frame.
  - RACHADURA #2 e #3: mais linhas cruzando o frame.
    Fragmentos de "vidro" se desprendem (triangulos 2-6px).
  - O bigode vibra com BLUR de 3px (intensidade maxima).
  - Particulas douradas sao empurradas pelas ondas.

Frame 5 (2.000s, duracao 0.4s):
  [AUDIO]: "...ENEEEEAS!" (PICO ABSOLUTO do grito).
  [EFEITO]: FLASH BRANCO fullscreen (alpha 40%, dura 0.1s). Screen shake 4px.
  [GAMEPLAY]: DANO MASSIVO aplicado a TODOS os inimigos visiveis na tela.
  - TELA RACHA COMPLETAMENTE: 8-12 linhas de rachadura irradiam DO CENTRO (da boca).
  - Fragmentos de vidro VOAM em todas as direcoes.
  - A imagem do rosto TREME violentamente (shake 4px).
  - Ondas atingem as bordas. Tudo PULSA.
  - Alpha do rosto: 90% (MAXIMO -- quase completamente corporeo).
  - Bigode: vibração maxima, quase um borrão.
  - Momento mais EPICO de todo o jogo.

Frame 6 (2.400s, duracao 0.4s):
  [AUDIO]: Eco do grito reverberando. Frequencia baixa.
  [EFEITO]: Flash branco desaparece. Rachaduras PERMANECEM como overlay.
  - Rosto comeca a fade (alpha 70%).
  - Ondas se dissipam.
  - Fragmentos de vidro flutuam e comecam a CAIR lentamente (gravidade).
  - Bigode para de vibrar. Desce lentamente.
  - Debuff "Respeito" aplicado a todos os inimigos sobreviventes:
    Visual: inimigos ficam com overlay cinza-dourado (alpha 15%).

=== FASE 3: RECONSTITUICAO (frames 7-9, 2.8-4.0s, transicao 256x256 -> 64x64) ===

Frame 7 (2.800s, duracao 0.4s):
  [AUDIO]: Musica do jogo retorna lentamente (fade in).
  [EFEITO]: Rachaduras comecam a se CURAR -- fragmentos flutuam de VOLTA.
  - Rosto dissolve para alpha 40%.
  - Fragmentos de vidro retornam magneticamente para as rachaduras.
  - ~40% das rachaduras se fecham neste frame.
  - Aura diminui. Particulas desaceleram.

Frame 8 (3.200s, duracao 0.4s):
  [TRANSICAO]: ZOOM OUT. O rosto ENCOLHE. Camera se afasta.
  [EFEITO]: 256x256 -> 64x64 (smooth interpolation de 0.4s).
  - ~75% das rachaduras se fecharam.
  - O rosto se afasta, revela o corpo completo novamente.
  - Eneas flutua no centro, exausto mas DIGNO.
  - Alpha corpo: 55%. Bigode: 80%.

Frame 9 (3.600s, duracao 0.4s):
  [EFEITO]: Ultimas rachaduras se fecham (100% curadas). Overlay limpo.
  [AUDIO]: Musica do jogo em volume normal.
  - Eneas de volta ao tamanho normal (64x64).
  - Postura ereta. Um ACENO minimo com a cabeca.
  - Aura retorna ao padrao.
  - Bigode faz ultimo flutter (reconhecimento silencioso).
  - Tela completamente limpa. Jogo retoma.
  - Inimigos com debuff "Respeito" visivelmente lentos e fracos.

-> Transiciona para IDLE (ou DESPAWN se for one-shot)
```

### Reconstituicao da Tela (Overlay)
```
O overlay de rachaduras tem 4 estagios:

Crack Stage 0: Sem rachaduras (pre-ultimate / pos-cura completa)
Crack Stage 1: 2-3 rachaduras, poucos fragmentos (Frame 3 do ultimate)
Crack Stage 2: 6-8 rachaduras, fragmentos multiplos (Frame 4)
Crack Stage 3: 8-12 rachaduras, fragmentos voando (Frame 5 -- MAXIMO)

A cura inverte: Stage 3 -> 2 -> 1 -> 0 nos frames 7-9.
Cada fragmento tem uma animacao de "retorno magnetico" (move em linha reta
de volta para sua posicao original na rachadura).
Velocidade do retorno: ease-in (comeca lento, acelera).
```

---

## 9. DESAPARICAO / DESPAWN

### Configuracao
| Parametro | Valor |
|---|---|
| Frames | 6 |
| Framerate | 8fps |
| Duracao | 0.75s |
| Loop | NAO |
| Sprite sheet | `eneas_despawn.png` 384x64px |

### Timeline

```
Frame 0 (0.000s): Eneas olha para cima. Queixo levanta. Aura intensifica (alpha 30%).
  Um ultimo momento de dignidade.

Frame 1 (0.125s): Dissolucao começa DOS PES. Alpha das pernas: 20%.
  Particulas douradas SOBEM do corpo (como cinzas). Torso ainda alpha 65%.
  Bigode: alpha 80% (firme).

Frame 2 (0.250s): Dissolucao ate a cintura. Pernas: alpha 0% (sumiram).
  Torso inferior: alpha 20%. Torso superior: alpha 40%.
  Capa se desfaz em fios de luz dourada que sobem.
  Bigode: alpha 75%. Particulas abundantes.

Frame 3 (0.375s): So resta cabeca e bigode flutuando.
  Corpo inteiro virou particulas subindo. Rosto: alpha 35%.
  Bigode: alpha 65%. Contorno ghost do terno visivel (1px alpha 10%).

Frame 4 (0.500s): SO O BIGODE.
  Literalmente so o bigode flutuando no ar. Alpha 50%.
  Particulas do rosto ainda subindo. Um ultimo flash de aura.
  Nenhum outro elemento do personagem visivel.

Frame 5 (0.625s): O bigode se dissolve em particulas finais.
  Alpha: 15%. Particulas se dispersam lentamente.
  ECHO VISUAL: silhueta COMPLETA do Eneas aparece como afterimage
  (alpha 5%, dura 1 frame). Uma memoria. Uma saudade.
  E desaparece.

-> Eneas sumiu. Fica ausente ate o proximo trigger (HP < 10% novamente).
   Cooldown: 180s (3 minutos) antes de poder reapareccer.
```

### Regra de Ouro da Desaparicao
```
ORDEM DE DISSOLUCAO (sempre):
1. Pes (primeiro a sumir)
2. Pernas
3. Torso inferior
4. Capa
5. Torso superior
6. Bracos/maos
7. Rosto
8. Bigode (ULTIMO a sumir -- SEMPRE)

O bigode SEMPRE e a ultima coisa visivel.
Ele persiste por pelo menos 1 frame SOZINHO.
```

---

## 10. BIGODE DA JUSTICA -- Ataque com Arma Exclusiva

### Configuracao
| Parametro | Valor |
|---|---|
| Duracao total | 2.0s (destaque + voo + retorno) |
| Loop | NAO |
| Cooldown | 8s |
| Ver tambem | `/assets/armas/bigode-justica/` para specs do projetil |

### Sequencia no Personagem (64x64px)

```
Frame 0 (0.000s): Eneas leva a mao ao bigode. Expressao de concentracao.
  O bigode TREME (vibrando, se preparando para decolar).

Frame 1 (0.100s): O bigode se DESTACA do rosto.
  Momento de separacao: 2px de gap entre rosto e bigode.
  ROSTO SEM BIGODE: Eneas cobre a boca com a mao OU vira de lado.
  NUNCA mostrar o rosto sem bigode claramente -- e misterio sagrado.
  O bigode flutua a 4px do rosto.

Frame 2 (0.200s): O bigode SAI VOANDO do sprite do personagem.
  [SPAWN]: Projetil "Bigode da Justica" criado como entidade separada.
  Eneas fica com a mao sobre onde o bigode estava.
  Seu rosto (alpha ja reduzido por ser fantasma) fica AINDA MAIS translucido
  na area do bigode ausente (alpha 30% na regiao).
  Flash de luz no ponto de lancamento.

[VOOS DO BIGODE: ver /assets/armas/bigode-justica/animation-spec.md]

Frame 3 (retorno, ~1.5s depois): O bigode retorna.
  Trail dourado atras do bigode retornando.
  Eneas vira o rosto para receber.

Frame 4 (re-acoplamento): O bigode se REACLOPLA ao rosto.
  SNAP magnetico: flash branco 1px no ponto de contato.
  O bigode treme por 2 frames se acomodando.
  Eneas faz um gesto de satisfacao sutil (aceno de cabeca minimo).
  Alpha da regiao do bigode retorna para 80%.

-> Retorna para IDLE
```

---

## 11. O VERDADEIRO PATRIOTA -- Efeito de Entrada (Passiva)

### Sequencia Visual (overlay em OUTROS personagens, NAO no Eneas)
```
Quando Eneas aparece, TODOS os outros personagens (aliados E inimigos)
pausam por 1.5 segundos em "respeito silencioso".

Visual em CADA personagem afetado:
Frame 0: Personagem para de animar (freeze frame).
Frame 1: Overlay dourado sutil (alpha 8%) sobre o sprite congelado.
Frame 2: O personagem VIRA para encarar o Eneas (sprite muda direcao).
         Overlay dourado alpha 10%.
Frame 3-11 (1.5s): Permanecem congelados, olhando para Eneas.
         Overlay dourado pulsa entre alpha 5% e 12%.
Frame 12: Overlay some. Personagens retomam acao normal.

Este efeito INCLUI os inimigos.
Zumbis param de atacar.
Bosses pausam mid-ataque.
TODO MUNDO respeita o Eneas.
```

---

## Resumo de Todos os Ciclos de Animacao

| # | Ciclo | Frames | FPS | Duracao | Loop | Sheet Size | Trigger |
|---|---|---|---|---|---|---|---|
| 1 | Idle | 4 | 8 | 0.5s | Sim | 256x64 | Padrao |
| 2 | Walk | 6 | 10 | 0.6s | Sim | 384x64 | Movimento |
| 3 | Spawn | 8 | 8 | 1.0s | Nao | 512x64 | HP < 10% |
| 4 | Grito Patriota | 4 | 10 | 0.4s | Nao | 256x64 | Skill 1 |
| 5a | Projetil 56 spawn | 4 | 10 | 0.4s | Nao | 256x64 | Skill 2 |
| 5b | Projetil 56 voo | 4 | 12 | 0.33s | Sim | 128x32 | Automatico |
| 5c | Projetil 56 impacto | 3 | 10 | 0.3s | Nao | 96x32 | Automatico |
| 6 | Aparicao Fantasma | 6 | 8 | 0.75s | Nao | 384x64 | Skill 3 |
| 7 | Saudade (aura chao) | 4 | 6 | 0.67s | Sim | overlay | Passiva |
| 8 | Ultimate (chao) | 2 | varies | 0.8s | Nao | 128x64 | HP<10%+input |
| 8 | Ultimate (rosto) | 7 | varies | 2.8s | Nao | 1792x256 | Continuacao |
| 8 | Ultimate (retorno) | 1 | varies | 0.4s | Nao | 64x64 | Continuacao |
| 8 | Ultimate (crack overlay) | 4 stages | varies | 4.0s total | Nao | 1024x256 | Overlay |
| 9 | Despawn | 6 | 8 | 0.75s | Nao | 384x64 | Timer/evento |
| 10 | Bigode Justica (char) | 5 | varies | 2.0s | Nao | 320x64 | Arma |
| 11 | Verdadeiro Patriota | 12 | 8 | 1.5s | Nao | overlay | Passiva |
| -- | Bigode sub-anim | 4 | 6 | 0.67s | Sim | 96x12 | Permanente |
| -- | Particulas aura | 4 | 6 | 0.67s | Sim | 64x16 | Permanente |

---

## Notas Tecnicas para Implementacao (Phaser 3)

### Composicao de Layers
```javascript
// Ordem de renderizacao (bottom to top):
// 1. Saudade aura (chao) -- depth: character.depth - 1
// 2. Afterimage trail -- depth: character.depth - 0.5
// 3. Aura dourada -- depth: character.depth + 0
// 4. Corpo principal -- depth: character.depth + 1
// 5. Bigode overlay -- depth: character.depth + 2
// 6. Capa/bandeira -- depth: character.depth + 0.5 (atras do corpo, frente da aura)
// 7. Particulas -- depth: character.depth + 3
// 8. Edge glow -- depth: character.depth + 4
// 9. Scanlines -- depth: character.depth + 5
// 10. Crack overlay (ultimate) -- depth: 9999 (TOP de tudo)
```

### Sincronizacao de Audio
```
SPAWN Frame 6 -> "MEU NOME E ENEAS!" (audio trigger)
GRITO Frame 2 -> "ENEAS!" (pico do grito)
ULTIMATE Frame 4 -> "MEU NOME E..." (inicio do grito cinematico)
ULTIMATE Frame 5 -> "...ENEEEEAS!" (pico do grito cinematico + flash + dano)
```
