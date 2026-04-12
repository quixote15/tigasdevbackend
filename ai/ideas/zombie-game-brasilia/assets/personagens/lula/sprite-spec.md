# LULA (O Cachaceiro) -- Sprite Specification
### Boss Principal (Lado Esquerdo) | Zumbis de Brasilia
### Estilo: Andre Guedes (Grotesco/Underground Comix)

---

## Especificacoes Gerais

- **Canvas**: 64x64 pixels por frame, PNG com transparencia (fundo alpha 0)
- **Sprite sheet**: horizontal, sem espacamento entre frames
- **Perspectiva**: top-down levemente isometrica (camera ~30 graus do topo, Y-sorting)
- **Escala do personagem**: corpo ocupa ~48x56px do canvas (margem de 8px para efeitos/sombra)
- **Direcoes**: 4 direcoes (down/up/left/right) -- cada animacao tem 4 rows no atlas
- **Outline**: contorno preto irregular de 2px, mais grosso nas deformidades (nariz, barriga)
- **Anti-alias**: NENHUM. Pixels duros. Sem suavizacao. Estilo cru.

---

## Paleta de Cores (Hex)

### Pele e Corpo
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Pele base | #D4956B | #A86B42 | #E8B88A |
| Nariz bulboso | #CC3333 | #8B1A1A | #E84444 |
| Bochechas ruborizadas | #B5443E | #8B2E2E | #D06060 |
| Barba branca | #C8C8C8 | #909090 | #E8E8E8 |
| Peito peludo | #5C3317 | #3B1F0B | #7A4B2A |

### Roupas
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Terno (base) | #3D3D3D | #1A1A1A | #555555 |
| Terno (reflexo sujo) | #4A4A3A | #2B2B1A | #5C5C4A |
| Gravata torta | #8B1A1A | #6B0F0F | #A82222 |
| Camisa (entreaberta) | #D9D0C0 | #B0A890 | #EDE6D8 |
| Sapatos | #2E1A0A | #1A0D05 | #4A3018 |

### Cicatriz Craniana (2026)
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Cicatriz base | #8B4060 | #6B2040 | #AA5878 |
| Pontos de sutura | #1A1A1A | #000000 | #333333 |
| Placa de titanio (brilho) | #8090A0 | #506070 | #B0C0D0 |
| Curativo parcial | #D8CFC0 | #B0A890 | #F0E8DA |
| Inflamacao | #CC4444 | #993333 | #E86666 |

### Acessorios
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Garrafa Velho Barreiro (vidro) | #2A5A2A | #1A3A1A | #3A7A3A |
| Rotulo garrafa | #D4AA00 | #AA8800 | #FFCC22 |
| Liquido cachaca | #CC8833 | #996622 | #EEAA44 |
| Copo de cachaca | #AACCEE | #88AACC | #CCDDEE |
| Microfone | #333333 | #111111 | #555555 |

---

## IDLE ANIMATION (4 frames)
**Ciclo**: frame 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> (loop ping-pong)
**Duracao total do ciclo**: 500ms (8fps)
**Descricao geral**: Lula parado, oscilando como bebado, segurando garrafa de Velho Barreiro na mao direita. Barriga sobe e desce com respiracao pesada. Nariz pulsa vermelho. Cabeca levemente inclinada.

### Frame 1 -- Posicao Neutra Bebada
- **Corpo**: Levemente inclinado para a esquerda (~5 graus). Centro de massa deslocado.
- **Cabeca**: Oval grande (18x16px), inclinada para direita. Cicatriz craniana visivel no topo -- linha irregular de 1px preto em zigue-zague com 3 pontos de sutura (pixels pretos 1x1 perpendiculares a linha). Placa de titanio: area 4x3px cinza metalico (#8090A0) no cranio superior esquerdo.
- **Rosto**: Olhos semicerrados -- 2 fendas de 3x1px cada, pupilas de 1px, palpebras pesadas 1px acima. Sobrancelhas grossas irregulares (4x2px cada, cinza escuro). Nariz MASSIVO: 8x7px bulboso vermelho (#CC3333) com veias finas (#8B1A1A, 1px) -- 3x maior que um nariz normal de personagem. Ponta do nariz com highlight (#E84444) 2x2px. Boca levemente aberta (3x1px), sorriso torto.
- **Barba**: Branca desgrenhada, cobre queixo e laterais do rosto. 6x4px de pixels irregular brancos/cinza (#C8C8C8, #909090), com fios individuais saindo para os lados (1px).
- **Terno**: Ombros desiguais -- esquerdo 2px mais alto que direito. Terno cinza escuro (#3D3D3D) com amassados indicados por linhas de sombra internas (#1A1A1A). Abertura frontal revelando camisa amarelada (#D9D0C0).
- **Gravata**: Torta para a esquerda, nao alinhada ao centro. 2x8px vermelho escuro (#8B1A1A), com no desfeito no topo.
- **Barriga**: Proeminente, estende 6px alem da linha do terno. Forma arredondada 10x8px sob a camisa. Botoes da camisa esticados (2 pixels brancos com gap).
- **Mao direita**: 5 dedos normais, segurando garrafa de Velho Barreiro (garrafa 4x10px, verde escuro, rotulo dourado 3x3px).
- **Mao esquerda**: 4 DEDOS (sem mindinho). Posicao relaxada ao lado do corpo. O gap onde o dedo faltaria e visivel -- coto de 1px rosado.
- **Pernas**: Levemente abertas para equilibrio de bebado. 2 colunas de 3px cada, sapatos escuros 4x2px.
- **Sombra**: Elipse 12x4px cinza translucida (#000000 alpha 40%) sob os pes.

### Frame 2 -- Oscilacao Direita + Gole
- **Corpo**: Inclinacao muda para a direita (~5 graus). Transferencia de peso.
- **Cabeca**: Inclina para tras levemente (1px para cima). Olhos ainda mais fechados (2x1px). Nariz: highlight 2x2px pisca mais forte (#E84444 -> #FF5555). A cicatriz craniana mostra 1 ponto de sutura a mais (4 total) -- efeito de "esticamento da pele" com a inclinacao.
- **Mao direita**: Garrafa levantada 3px mais alto. Angulo da garrafa muda -- inclinando em direcao a boca. Liquido dentro da garrafa desloca 1px (superficie do liquido #CC8833 ajusta angulo).
- **Barriga**: Expande 1px (inspiracao). Botao da camisa mais esticado.
- **Pernas**: Pe direito levantado 1px (desequilibrio).
- **Restante**: Identico ao frame 1 exceto posicoes ajustadas.

### Frame 3 -- Arroto + Balancar
- **Corpo**: Retorna ao centro mas passa 2 graus para a esquerda (overshoot de bebado).
- **Cabeca**: Boca aberta (3x2px) -- pixel de "nuvem" de arroto saindo (2x2px amarelo-esverdeado #99AA44 com 1px de distancia da boca). Olhos abrem levemente (3x2px, revelando mais iris).
- **Nariz**: Pulsa vermelho mais intenso (#DD3333) -- 1px de outline extra ao redor indicando vasodilatacao.
- **Mao direita**: Garrafa volta para baixo. 2 pixels de respingo de cachaca (#CC8833) saindo da boca da garrafa.
- **Barriga**: Contrai 1px (expiracao forcada do arroto).
- **Gravata**: Balanca 1px para a direita (inercia do movimento).

### Frame 4 -- Sossego Momentaneo
- **Corpo**: Quase reto, mas nunca perfeitamente alinhado (1 grau para esquerda).
- **Cabeca**: Olhos mais abertos que os outros frames (3x2px com pupila 1x1px visivel no centro). Expressao de "contentamento alcoolico". Boca fechada com sorriso (3x1px curvado para cima).
- **Cicatriz craniana**: Visibilidade maxima neste frame -- a inclinacao da cabeca expoe toda a linha de sutura (6px de comprimento no topo, com 5 pontos). Area ao redor levemente avermelhada (#CC4444).
- **Mao direita**: Garrafa na posicao mais baixa, relaxada.
- **Mao esquerda (4 dedos)**: Move 1px para frente, como se gesticulando para ninguem.
- **Pernas**: Ambos os pes no chao, posicao mais estavel do ciclo.

---

## WALK ANIMATION (6 frames)
**Ciclo**: frame 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> (loop)
**Duracao total do ciclo**: 600ms (10fps)
**Descricao geral**: Caminhada cambaleante de bebado. Nunca em linha reta -- o corpo oscila lateralmente a cada passo. Garrafa balanca. Barriga sacode. Gravata voa.

### Frame 1 -- Passo Esquerdo (Inicio)
- **Corpo**: Inclinado 8 graus para a direita (contrapeso do passo).
- **Perna esquerda**: Estendida para frente, pe 4px a frente da posicao idle. Pe levantado 2px do chao.
- **Perna direita**: Atras, apoiando peso. Joelho levemente dobrado.
- **Barriga**: Desloca 1px na direcao do movimento (inercia da massa).
- **Mao direita**: Garrafa balanca para tras (2px atras da posicao idle). Liquido inclina na garrafa.
- **Mao esquerda (4 dedos)**: Balanca para frente (2px). Os 4 dedos visiveis em posicao de caminhada.
- **Cabeca**: Levemente atrasada em relacao ao corpo (1px) -- efeito de bebado que o corpo vai primeiro.

### Frame 2 -- Passo Esquerdo (Contato)
- **Corpo**: Retorna a 3 graus de inclinacao.
- **Perna esquerda**: Pe toca o chao. Impacto: 2 pixels de "poeira" (#5C3317) saem do ponto de contato.
- **Barriga**: Sacode para baixo 1px (impacto).
- **Gravata**: Voa 2px para a esquerda (inercia).
- **Garrafa**: Respingo de 1px sai pela abertura.
- **Cicatriz**: Curativos parciais visiveiss -- 1 faixa branca (#D8CFC0) de 3x1px no topo do cranio balanca com o movimento.

### Frame 3 -- Transferencia de Peso (Centro)
- **Corpo**: Quase vertical. Momento de duplo apoio -- ambos os pes no chao.
- **Barriga**: Posicao maxima para frente (2px alem do normal) -- momento de avanco.
- **Rosto**: Olhos tentam focar a frente. Bochechas ruborizadas mais visiveis (#B5443E).
- **Nariz**: Balanca levemente (1px lateral) com o passo.
- **Mao esquerda**: Passa ao lado do corpo, 4 dedos claramente visiveis na silhueta.

### Frame 4 -- Passo Direito (Inicio)
- **Corpo**: Inclinado 8 graus para a esquerda agora.
- **Perna direita**: Estendida para frente. Pe levantado 2px.
- **Perna esquerda**: Apoio atras.
- **Barriga**: Desloca para o outro lado (inercia).
- **Garrafa**: Balanca para frente agora -- Lula quase perde o grip.
- **Mao esquerda (4 dedos)**: Balanca para tras. O coto do mindinho visivel em silhueta.

### Frame 5 -- Passo Direito (Contato)
- **Corpo**: Retorna a 3 graus.
- **Perna direita**: Contato com o chao. Menos poeira que frame 2 (pe mais leve).
- **Cabeca**: Faz micro-nod para frente (1px) como se concordasse com si mesmo.
- **Barriga**: Sacode para baixo.
- **Gravata**: Voa 2px para a direita.

### Frame 6 -- Tropeco Leve (Assinatura)
- **Corpo**: Inclinacao extra de 3 graus para frente -- quase tropeica.
- **Ambos os pes**: Proximos um do outro, como se estivesse se recomponedo.
- **Cabeca**: Levantada rapido (1px para cima) -- expressao de "ops".
- **Garrafa**: Inclina perigosamente, 3 pixels de cachaca voam.
- **Barriga**: Posicao maxima para baixo (gravidade puxando no tropeco).
- **Expressao facial**: Olhos arregalados momentaneamente (3x3px) antes de voltar ao semicerrado.

---

## ATTACK ANIMATION (3 frames) -- "Cachaçada Companheira"
**Ciclo**: frame 1 -> 2 -> 3 -> (volta para idle)
**Duracao total**: 375ms (8fps)
**Descricao geral**: Lula levanta garrafa de Velho Barreiro acima da cabeca e arremessa em arco. A garrafa voa e explode em area.

### Frame 1 -- Wind-Up (Preparacao)
- **Corpo**: Torso rotaciona para tras (posicao de arremesso). Ombro direito levantado 4px.
- **Mao direita**: Garrafa levantada acima e atras da cabeca. Garrafa agora em angulo de 45 graus, rotulo visivel. Brilho no vidro (#3A7A3A highlight).
- **Mao esquerda (4 dedos)**: Estendida para frente, apontando o alvo. Os 4 dedos abertos como leque -- o espaco do mindinho faltante e MUITO visivel.
- **Rosto**: Olhos arregalados de raiva bebada (4x3px, pupilas dilatadas, veias vermelhas 1px nos cantos). Boca aberta gritando (4x3px, dentes amarelados visiveiss 1x1px). Sobrancelhas em V de furia.
- **Nariz**: Vermelho maximo (#DD3333), pulsando, visivelmente maior que no idle (+1px cada lado).
- **Barriga**: Contraida -- Lula esta fazendo forca.
- **Cicatriz**: Pontos de sutura sob tensao -- area ao redor fica mais vermelha (#CC4444).
- **Pes**: Separados, posicao de arremessador, pe esquerdo atras.

### Frame 2 -- Arremesso
- **Corpo**: Rotacao rapida para frente. Torso descreve arco.
- **Mao direita**: VAZIA -- garrafa saiu. 2 pixels de borrão indicam a trajetoria de saida (blur trail). A mao permanece aberta no ar.
- **Garrafa em voo**: 6x12px, rotacionando (angulo ~70 graus). Trail de liquido: 3 gotículas de cachaca (#CC8833) em arco atras da garrafa. O rotulo "Velho Barreiro" (3x2px dourado) visivel.
- **Mao esquerda**: Puxada para o corpo (follow-through do arremesso).
- **Rosto**: Boca gritando "COMPANHEIRO!" -- exageradamente aberta (5x4px), lingua visivel (1x2px rosada).
- **Barriga**: Sacudida para frente com a inercia.
- **Pes**: Pe esquerdo agora na frente (transferencia de peso do arremesso).

### Frame 3 -- Follow-Through + Explosao
- **Corpo**: Desequilibrado para frente, quase caindo.
- **Mao direita**: Relaxada, caida.
- **Explosao (separada do sprite, efeito overlay)**: Circulo de 16x16px. Centro: flash branco-amarelo (#FFEE88). Anel medio: laranja fogo (#CC6600). Anel externo: manchas de cachaca marrom (#996622). Cacos de vidro: 4-6 pixels verdes (#2A5A2A) voando radialmente. Chamas azuladas (alcool queimando): pixels #4466CC em padrão irregular.
- **Rosto**: Sorriso satisfeito de malandro (3x1px curvado, olhos semicerrados com prazer). Nariz brilhante de suor (#E84444 highlight extra).
- **Expressao**: pura satisfacao alcoolica.

---

## DEATH ANIMATION (4 frames)
**Ciclo**: frame 1 -> 2 -> 3 -> 4 -> (fica no frame 4 / "Quarto Mandato" check)
**Duracao total**: 800ms (5fps -- mais lento para drama comico)
**Descricao geral**: Lula cai de forma dramatica, soltando a garrafa, em queda lenta tipo morte de novela. Se "Quarto Mandato" estiver disponivel, frame 4 pisca e ele levanta.

### Frame 1 -- Impacto Inicial
- **Corpo**: Empurrado para tras. Torso dobra na cintura.
- **Cabeca**: Jogada para tras, boca aberta em O de surpresa (4x4px circular). Olhos arregalados maximo (4x4px com pupilas minusculas 1x1px no centro -- expressao de choque).
- **Nariz**: Deforma levemente com o impacto -- achatado 1px na direcao do golpe.
- **Garrafa**: Solta da mao -- voa para cima-direita. 3 respingos de cachaca.
- **Cicatriz craniana**: Placa de titanio brilha com o impacto (#B0C0D0 highlight flash).
- **Barriga**: Onda de cima para baixo (inercia da gordura) -- a parte de cima ja esta indo para tras, a parte de baixo ainda avanca.
- **Pes**: Saem do chao 1px.
- **Gravata**: Voa para cima verticalmente.

### Frame 2 -- Queda
- **Corpo**: Caindo para tras, angulo de 45 graus com o chao.
- **Cabeca**: Mais para tras. Barba aponta para cima.
- **Olhos**: Fechando (voltando a semicerrado -- como se adormecendo).
- **Boca**: Murmurando "companheiro..." (3x2px, entreaberta).
- **Garrafa**: No ar, mais distante, rotacionando. 1 caco de vidro ja se soltou.
- **Mao esquerda (4 dedos)**: Estendida para cima, como se tentasse agarrar algo invisivel. Os 4 dedos espalhados dramaticamente.
- **Barriga**: Apontando para cima agora, proeminente.
- **Liquido de cachaca**: Pocinha se formando onde a garrafa impactou -- 4x2px marrom (#996622).

### Frame 3 -- Impacto no Chao
- **Corpo**: Horizontal. Costas no chao. Angulo 85 graus.
- **Cabeca**: Bateu no chao -- estrelinhas (3 pixels amarelos #FFCC00 ao redor, cada 1x1px, dispostos em triangulo). Cicatriz craniana: 1 ponto de sutura se solta (pixel preto individual se desloca 1px).
- **Barriga**: Saliencia maxima -- aponta para o ceu como uma colina.
- **Terno**: Aberto, camisa rasgada, peito peludo visivel (pixels marrons #5C3317 irregulares).
- **Garrafa**: Estilhaçada no chao -- 4x4px de cacos verdes (#2A5A2A) e poça de cachaca (#CC8833) 6x3px.
- **Mao direita**: Aberta, estendida ao lado.
- **Mao esquerda (4 dedos)**: Caida ao lado, dedos curvados.
- **Nuvem de poeira**: 8x3px ao redor do corpo (#8B7355 translucido).

### Frame 4 -- Morto (ou Quarto Mandato)
- **Corpo**: Completamente no chao, imóvel.
- **Olhos**: X_X (dois X de 2x2px cada, pixel art classico de morte).
- **Boca**: Lingua de fora, 1px rosado saindo do lado da boca.
- **Nariz**: Ainda vermelho mas apagado (#993333 -- sem pulsacao).
- **Barriga**: Imóvel, proeminente.
- **Gravata**: Caida sobre o rosto.
- **Garrafa**: Destroçada. Liquido se espalhando (animacao de particula separada -- pool cresce 1px a cada 200ms).
- **Cicatriz**: Visivel e grotesca -- sem curativos, pontos de sutura expostos, placa de titanio com reflexo opaco.
- **Fantasma de cachaca** (se Quarto Mandato ativado): Nuvem esverdeada (#99AA44 alpha 50%) sobe do corpo por 3 frames antes de ele piscar e levantar.
- **Sombra**: Espalhada sob o corpo inteiro, 20x6px.

---

## HIT ANIMATION (2 frames)
**Ciclo**: frame 1 -> 2 -> (volta para animacao anterior)
**Duracao total**: 200ms (10fps)
**Descricao geral**: Lula leva dano. Flash branco. Recuo. Expressao de dor/raiva.

### Frame 1 -- Flash de Dano
- **Corpo inteiro**: Flash branco -- todos os pixels do personagem mudam para branco (#FFFFFF) por 1 frame com alpha 70% overlay. Silhueta reconhecivel mas "queimada" de branco.
- **Outline**: Fica vermelho (#FF0000) em vez de preto.
- **Recuo**: Corpo inteiro desloca 3px na direcao oposta ao dano.
- **Particulas**: 3-4 pixels vermelhos (#CC0000) voam para fora do ponto de impacto (indicacao de dano).

### Frame 2 -- Reacao
- **Corpo**: Retorna a cor normal mas com tint avermelhado geral (cada pixel fica 15% mais avermelhado por 1 frame).
- **Rosto**: Expressao de RAIVA -- sobrancelhas em V extremo, boca quadrada gritando (4x3px), olhos de furia (3x2px, pupilas vermelhas 1x1px).
- **Nariz**: Pulsa extra (1px expansion), vermelho maximo.
- **Fala**: Balão de texto "FICO PUTO DA VIDA!" aparece acima (gerenciado pelo sistema de UI, nao no sprite).
- **Barriga**: Infla (inspiracao de raiva), +2px de volume.
- **Mao esquerda (4 dedos)**: Punho cerrado. O gap do mindinho visto na silhueta do punho.
- **Mao direita**: Aperta a garrafa com forca (garrafa levemente deformada -- squeeze de 1px).

---

## SPECIAL ANIMATIONS

### Special 1: "Fato Alternativo" (6 frames)
**Duracao**: 750ms (8fps)
**Descricao**: Lula aponta para a camera e MENTE. A UI do jogo se corrompe.

#### Frame 1 -- Preparacao do Discurso
- **Corpo**: Se endireita (posicao mais ereta que o normal -- raro para ele).
- **Mao direita**: Garrafa transferida para debaixo do braco esquerdo (presa pela axila).
- **Mao esquerda (4 dedos)**: Levantada, dedo indicador apontando para cima.
- **Rosto**: Sorriso de malandro confiante (3x1px, curvado, olhos de raposa).

#### Frame 2 -- O Apontamento
- **Mao esquerda**: 4 dedos apontando para a camera (para o jogador). Indicador esticado, outros 3 fechados. Gap do mindinho visivel.
- **Rosto**: Olhos abertos, sobrancelhas levantadas ("confia em mim").
- **Boca**: Aberta, formando "Eu quero dizer pra voces..." (3x2px).

#### Frame 3 -- Onda de Distorcao
- **Corpo**: Flash de energia vermelha (#8B1A1A alpha 60%) emana em circulo de 8px ao redor de Lula.
- **Ondulacao**: Linhas onduladas saem de Lula (efeito de "mentira" propagando) -- 3 arcos concentricos de 1px vermelho escuro, expandindo.
- **Olhos**: Brilham vermelho por 1 frame (#FF0000 nas pupilas).

#### Frame 4 -- Poder Ativado
- **Corpo**: Posicao de poder -- mao esquerda no ar, mao direita na cintura (garrafa solta atras).
- **Aura**: Particulas vermelhas (#8B1A1A) orbitam Lula em circulo, 6 particulas de 1x1px.
- **Rosto**: Sorriso maximo, olhos semicerrados de satisfacao.
- **Efeito na UI (fora do sprite)**: Barra de vida do jogador muda para "cheia" (falsa). Score multiplica x10 (falso). Dura 5 segundos.

#### Frame 5 -- Sustentacao
- **Corpo**: Mesma posicao, mas mao esquerda desce levemente.
- **Aura**: Particulas desacelerando.
- **Expressao**: Riso (boca 4x3px, dentes visiveis, olhos apertados).

#### Frame 6 -- Fim do Efeito
- **Corpo**: Volta a posicao bebada normal. Pega a garrafa de volta.
- **Aura**: Se dissipa -- particulas esfarelam.
- **Rosto**: Pisca (olhos fecham e abrem 1 frame) com sorriso residual.

---

### Special 2: "Dedo Perdido" -- Ataque Corpo-a-Corpo (4 frames)
**Duracao**: 400ms (10fps)
**Descricao**: Ataque melee -- dedada no olho do oponente com a mao de 4 dedos.

#### Frame 1 -- Investida
- **Corpo**: Avanca 4px na direcao do alvo. Posicao baixa (agachado levemente).
- **Mao esquerda**: Estendida com 4 dedos abertos em formato de garra. Dedos visiveis individualmente: indicador (3px), medio (3px), anelar (3px), polegar (2px). Gap onde o mindinho deveria estar: 2px de vazio.

#### Frame 2 -- Dedada
- **Mao esquerda**: Dois dedos (indicador + medio) formam V apontando para frente (Three Stooges eye poke mas com 4 dedos).
- **Corpo**: Esticado ao maximo para frente.
- **Rosto**: Expressao de maldade (sorriso torto, uma sobrancelha levantada).

#### Frame 3 -- Contato
- **Mao esquerda**: Em posicao de contato. Flash de impacto amarelo (#FFCC00) 3x3px no ponto de toque.
- **Efeito**: Estrelas de dor no alvo (gerenciado pelo sistema, nao no sprite do Lula).
- **Corpo**: Recuo leve do impacto.

#### Frame 4 -- Retorno
- **Corpo**: Volta para posicao normal.
- **Mao esquerda**: Sacudindo (os dedos se movem como se limpando). 1px de "suor" saindo.
- **Rosto**: Satisfacao ("funcionou").

---

### Special 3: "Quarto Mandato" -- Resurreicao (8 frames)
**Duracao**: 1600ms (5fps -- lento para drama)
**Descricao**: Lula "morto" no chao. Garrafa fantasma de cachaca flutua ate ele. Ele levanta como zumbi.

#### Frame 1 -- Corpo Morto
- Identico ao Death Frame 4. X_X nos olhos. Imóvel.

#### Frame 2 -- Garrafa Fantasma
- Corpo igual. Uma garrafa translucida (#2A5A2A alpha 50%) aparece flutuando 8px acima do corpo.
- Brilho sobrenatural: particulas douradas (#FFCC22) 2-3 pixels ao redor da garrafa.

#### Frame 3 -- A Cachaca Cai
- Garrafa desce ate a boca de Lula. Liquido fantasmagorico (#CC8833 alpha 60%) escorre para a boca.
- Mao direita: dedos twitcham (2 pixels se movem 1px).

#### Frame 4 -- Reacao
- Olhos de X_X comecam a mudar -- um X se desfaz, vira ponto. Outro ainda X.
- Barriga infla 1px (ar entrando).
- Cor da pele: retorna de palido (#CCBB99) para normal (#D4956B) gradativamente.

#### Frame 5 -- Sentando
- Torso levanta 30 graus do chao. Um braco apoia.
- Ambos os olhos agora semicerrados (padrao normal).
- Nariz volta a pulsar vermelho.
- Cachaca escorrendo pelo queixo (2 pixels #CC8833).

#### Frame 6 -- Levantando
- Torso a 60 graus. Outro braco apoia.
- Expressao de "ressaca mas vivo".
- Cicatriz craniana brilha (#B0C0D0 flash na placa de titanio).

#### Frame 7 -- Quase em Pe
- De pe mas curvado. Barriga pendurada. Terno mais desgrenhado que antes.
- Mao direita tateia o chao buscando a garrafa (agora solida, materializada).

#### Frame 8 -- Ressurreto
- Em pe, posicao idle, mas com diferenças: terno mais rasgado (+3 linhas de rasgo), 1 curativo a menos, expressao 10% mais furiosa. Barra de HP aparece a 25%.
- Fala (UI): "Mas eu acabei de ser reeleito, companheiro!"
- Aura: Residuo de particulas douradas por 500ms apos o frame.

---

### Special 4: "Empurra Mole / Faz o L" -- Onda de Choque (6 frames)
**Duracao**: 1200ms (5fps -- LENTO de proposito, "bem devagarinho")
**Descricao**: Lula faz o gesto do L com a mao esquerda (4 dedos) em camera lenta. Onda de choque empurra todos.

#### Frame 1 -- Preparacao
- **Corpo**: Se planta firmemente. Pes separados.
- **Mao esquerda**: Começa a subir. Dedos fechados.
- **Rosto**: Sorriso crescendo. Olhos focados.
- **Garrafa**: Guardada atras (mao direita nas costas com a garrafa).

#### Frame 2 -- Braco Subindo (Lento)
- **Mao esquerda**: Na altura do peito. Dedos comecam a se abrir.
- **Aura**: Energia vermelha (#8B1A1A alpha 30%) comeca a se acumular ao redor de Lula.
- **Particulas**: Poeira do chao levanta (4 pixels #8B7355 subindo lentamente).

#### Frame 3 -- L em Formacao
- **Mao esquerda**: Na altura do ombro. Indicador + polegar formam L. Os outros 2 dedos (medio + anelar) fechados. Gap do mindinho visivel. O L fica "errado" por ser mao esquerda com 4 dedos -- grotesco e comico.
- **Aura**: Intensifica (#8B1A1A alpha 50%). Circunferencia de 12px.
- **Chao**: Rachando (linhas de 1px escuras irradiam de Lula).

#### Frame 4 -- L Completo + Flash
- **Mao esquerda**: Totalmente estendida acima da cabeca. L perfeito (dentro do possivel com 4 dedos). Brilho vermelho no L (#CC3333 outline de 1px ao redor dos dedos).
- **Flash**: Tela inteira faz flash branco (#FFFFFF alpha 30%) por 1 frame.
- **Rosto**: Exultante. Boca aberta gritando "FAZ O L!" (5x4px).
- **Nariz**: Brilhante, pulsando.

#### Frame 5 -- Onda de Choque Saindo
- **Mao esquerda**: Mantendo L.
- **Onda**: Circulo de choque vermelho/marrom (#8B1A1A/#5C3317) expandindo de Lula para fora. Diametro crescendo de 16px a 48px. Linhas irregulares (nao circulo perfeito -- grotesco).
- **Corpo**: Rigido, plantado.
- **Efeito nos inimigos (sistema)**: Empurrados 4 tiles para tras. Quanto mais perto, mais dano.

#### Frame 6 -- Dissipacao
- **Corpo**: Relaxa. Mao desce.
- **Onda**: Ultimos residuos, particulas vermelhas se dissipando.
- **Rosto**: Sorriso satisfeito. Volta ao semicerrado.
- **Recupera garrafa**: Mao direita traz garrafa de volta a posicao frontal.

---

### Special 5: "Discurso de Hora e Meia" -- Ultimate (8 frames)
**Duracao**: 2000ms de animacao de setup + 8000ms de efeito
**Descricao**: Palanque surge do chao. Lula sobe. TODOS param por 8 segundos. Lula se cura.

#### Frame 1 -- Palanque Surgindo
- **Lula**: Olha para baixo surpreso. Chao se eleva sob seus pes.
- **Palanque**: Estrutura de madeira 24x8px surgindo do chao. Bandeiras vermelhas (#8B1A1A) penduradas 4x6px.
- **Efeito**: Terra se quebrando ao redor (pixels marrons #5C3317 voando).

#### Frame 2 -- Subida
- **Lula**: Sobre o palanque (elevado 8px do chao). Palanque completo: 24x12px com frente decorada.
- **Microfone**: Aparece na mao esquerda (transferiu garrafa para bolso interno do terno). Microfone: 2x6px preto (#333333) com esfera no topo 3x3px.
- **Postura**: Mais imponente que o normal (costas retas pela primeira vez).

#### Frame 3 -- Inicio do Discurso
- **Boca**: Aberta (4x3px). Ondas de som visiveis: 3 arcos concentricos saindo da boca (1px cinza cada, expandindo).
- **Mao direita**: Gesticulando no ar (palma aberta, 5 dedos).
- **Efeito**: Todos os sprites no mapa recebem efeito "sentando" (gerenciado pelo sistema). Zs aparecem sobre inimigos adormecidos pela labia.

#### Frame 4 -- Gestuculacao Intensa
- **Corpo**: Inclinado para frente sobre o palanque.
- **Mao direita**: Punho cerrado, socando o ar.
- **Mao esquerda (4 dedos)**: Segura microfone contra a boca.
- **Ondas de som**: Maiores, mais densas. Particulas de letras flutuando: "companheiro", "nunca antes", "maravilhoso" (pixels formando texto 1px se reconheciveis).

#### Frame 5 -- Pico Emocional
- **Rosto**: Olhos fechados de emocao (2 linhas curvadas). Boca enorme aberta (5x4px). Lagrima falsa: 1px azul (#4488CC) no canto do olho.
- **Corpo**: Mao direita no peito (emocionado).
- **Aura**: Dourada (#FFCC22 alpha 40%) por ter entrado no "modo discurso maximo".
- **Cura**: +HP visivel como particulas verdes (#44CC44) sendo absorvidas por Lula.

#### Frame 6 -- Circularidade
- **Boca**: Abrindo e fechando em loop rapido (2 sub-frames) -- falando sem parar.
- **Mao direita**: Gesto circular (como se explicando algo que nunca chega ao ponto).
- **Texto flutuando (UI)**: "Eu quero dizer... olha... eu quero dizer..." em loop.
- **Cura continua**: Mais particulas verdes.

#### Frame 7 -- Apice
- **Corpo**: Ambos os bracos abertos (posicao de "abraço ao povo").
- **Microfone**: Na mao esquerda (4 dedos) estendida.
- **Palanque**: Bandeiras vermelhas tremulando (frames alternados de 1px de deslocamento).
- **HP**: Quase cheio. Brilho branco geral no sprite de Lula.

#### Frame 8 -- Fim do Discurso
- **Corpo**: Volta a posicao normal.
- **Palanque**: Começa a afundar no chao (reverso do frame 1).
- **Microfone**: Desaparece. Garrafa volta a mao.
- **Rosto**: Satisfeito, suado (3 pixels de suor #88CCEE nas testa/bochechas).
- **Efeito global**: Todos os personagens "acordam", se levantam, sacudem a cabeca.

---

## ATLAS LAYOUT

O atlas final para Lula deve conter 2048x2048px maximo. Layout sugerido:

```
Row 0 (y=0):    Idle Down (4f)     | Idle Up (4f)      | Idle Left (4f)    | Idle Right (4f)
Row 1 (y=64):   Walk Down (6f)     | Walk Up (6f)      | Walk Left (6f)    | Walk Right (6f)
Row 2 (y=128):  Attack Down (3f)   | Attack Up (3f)    | Attack Left (3f)  | Attack Right (3f)
Row 3 (y=192):  Death (4f)         | Hit (2f)          | (vazio)           | (vazio)
Row 4 (y=256):  Fato Alternativo (6f) | Dedo Perdido (4f) | (vazio)        | (vazio)
Row 5 (y=320):  Quarto Mandato (8f)                                        
Row 6 (y=384):  Empurra Mole / Faz o L (6f)                                
Row 7 (y=448):  Discurso Ultimate (8f)                                      
Row 8-15:       Skin variants (mesmo layout, cores alteradas)               
```

Total frames estimados: ~200 (base + 4 direcoes + skins)
