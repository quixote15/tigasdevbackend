# Arma Brochavel (As Vezes) — Arma Exclusiva do BOLSONARO

## Visao Geral

**Dono**: BOLSONARO (O Mito)
**Tipo**: Projetil de distancia (Revolver de cauboi)
**Subtipo**: Ranged + RNG (30% falha) + Self-damage
**Dimensoes Sprite**: 32x32px (arma), 16x16px (bala), 24x24px (fumaca de falha)
**Perspectiva**: Top-down levemente isometrica

---

## Descricao Visual

Revolver de cauboi DOURADO, absurdamente brilhante e cafona. Cano longo demais (compensacao). Adesivo da bandeira do Brasil colado torto no cabo. Cilindro visivel com 6 balas (algumas enferrujadas). O dourado nao e elegante — e dourado de CAMELÔ, brilhoso demais, quase plastico. O cabo tem marcas de dedos gordurosos. Uma fita verde-amarela amarrada no gatilho como amuleto.

### Cores Hex
| Elemento | Cor | Hex |
|---|---|---|
| Corpo dourado | Ouro cafona | #DAA520 |
| Reflexo dourado | Brilho excessivo | #FFD700 |
| Sombra do metal | Dourado escuro sujo | #8B6914 |
| Cabo madeira | Marrom avermelhado | #5C3317 |
| Adesivo bandeira verde | Verde Brasil | #009739 |
| Adesivo bandeira amarelo | Amarelo Brasil | #FFDF00 |
| Adesivo bandeira azul | Azul Brasil | #002776 |
| Cilindro interno | Cinza metalico | #708090 |
| Balas | Cobre enferrujado | #B87333 |
| Fumaca de falha | Cinza patetico | #A9A9A9 |
| Flash de disparo | Amarelo explosivo | #FFFF00 |
| Sangue (self-damage) | Vermelho do Mito | #8B0000 |

---

## Estados da Arma

### 1. Em Mao (Idle) — 3 frames loop
- **Frame 1**: Bolsonaro segura o revolver com as duas maos (postura de filme de acao dos anos 80). Arma apontada pra frente. Brilho excessivo no dourado. Expressao de machao confiante.
- **Frame 2**: Mesma pose. Bolsonaro faz "arminha" com a outra mao ao lado do revolver (gesto icônico). Brilho de lens flare ridiculo no cano.
- **Frame 3**: Bolsonaro gira o revolver no dedo como cauboi. Quase derruba. Recupera. Finge que nao aconteceu.
- **Timing**: 400ms, 400ms, 600ms (giro mais lento pra comedia)

### 2. Mirar — 2 frames
- **Frame 1**: Bolsonaro fecha um olho (mira de atirador amador). Lingua pra fora de concentracao. Arma levantada. Queixo enorme projetado pra frente.
- **Frame 2**: Arma estabilizada. Mira com o cano tremendo levemente (nao e tao bom atirador quanto pensa). Suor na testa.
- **Timing**: 200ms, 150ms

### 3A. Disparo BEM-SUCEDIDO (70%) — 4 frames
- **Frame 1**: BANG! Flash amarelo enorme na ponta do cano. Recuo empurra Bolsonaro pra tras (barriga absorve o impacto). Bala sai com trilha dourada.
- **Frame 2**: Nuvem de fumaca no cano. Bolsonaro recuperando a postura. Sorriso de satisfacao. Shell casing voando pro lado.
- **Frame 3**: Fumaca dispersando. Bolsonaro com pose de "deu certo". Aponta pro inimigo atingido com a mao livre.
- **Frame 4**: Volta a posicao idle. Sopra a fumaca do cano como cauboi (mas de um jeito patetico, nao cool).
- **Timing**: 60ms, 120ms, 200ms, 300ms
- **Audio**: BANG potente + "TALKEI?" confiante

### 3B. FALHA / BROCHA (30%) — 5 frames
- **Frame 1**: Click. Nada acontece. Bolsonaro confuso. "?" aparece sobre a cabeca.
- **Frame 2**: Bolsonaro olha pro cano da arma (NUNCA FACA ISSO). Fumacinha patetica saindo — nao uma nuvem de fumaca epica, uma fumacinha triste, tipo cigarro apagando.
- **Frame 3**: A bala sai PELA CULATRA. Flash na parte de tras do revolver. Bolsonaro tomando o tiro no proprio peito/barriga (na cicatriz da facada — IRONIA). Expressao de dor e surpresa.
- **Frame 4**: Bolsonaro cambaleando pra tras. Segurando a barriga. Sangue saindo (pouco — e cartunesco). Revolver soltando fumaca patetica.
- **Frame 5**: Bolsonaro de joelhos momentaneamente. Olha pra arma com raiva. Levanta com dificuldade. Expressao de "porque eu?"
- **Timing**: 200ms, 250ms, 100ms, 300ms, 400ms (falha e LENTA — a piada precisa de timing)
- **Audio**: click fraco + silencio + POP patetico + "TALKEI?..." (triste, descendente)
- **Self-damage**: 15% do dano que FARIA no inimigo

### 4. Projetil — Bala Dourada (16x16px) — 2 frames loop
- **Frame 1**: Bala dourada alongada com trilha de luz. Speed lines ao redor. Brilho.
- **Frame 2**: Bala com trilha mais longa. Leve rotacao.
- **Timing**: 40ms por frame (rapido)
- **Velocidade**: 450px/s (rapido quando funciona)
- **Alcance**: 350px

### 5. Impacto de Bala — 3 frames (24x24px)
- **Frame 1**: Flash dourado no ponto de impacto. Estrela de 4 pontas.
- **Frame 2**: Particulas douradas se espalhando. Flash diminuindo.
- **Frame 3**: Residuo dourado no chao (desaparece em 500ms).
- **Timing**: 60ms, 100ms, 150ms

---

## Animacao de Recarga — 4 frames

- **Frame 1**: Bolsonaro abre o cilindro. Shells caem (4-6 casings voando). Expressao de pressa.
- **Frame 2**: Enfia a mao no bolso procurando balas. Tira bala, uma moeda, um santinho de campanha e um chiclete. 
- **Frame 3**: Coloca as balas no cilindro uma por uma. Algumas caem no chao (mao tremendo). Fecha o cilindro com flip dramatico.
- **Frame 4**: Gira o cilindro. Click. Pronto. Sorriso de "agora vai".
- **Timing**: 300ms, 400ms, 350ms, 250ms (total 1300ms — reload lento)

---

## Efeitos de Particula

### Disparo Normal
- 8-12 particulas no flash
- Cores: #FFFF00 (amarelo), #FFD700 (dourado), #FFA500 (laranja)
- Tamanho: 2-5px
- Lifetime: 200ms
- Direcao: radial frontal (90 graus)

### Fumaca de Falha
- 3-5 particulas tristes
- Cor: #A9A9A9 (cinza patetico)
- Tamanho: 4-8px (crescem lentamente — pateticos)
- Lifetime: 800ms (ficam no ar — pateticas)
- Direcao: para cima, devagar

### Self-Damage
- 5-8 particulas de sangue
- Cor: #8B0000 (vermelho escuro)
- Tamanho: 2-4px
- Lifetime: 400ms
- Direcao: radial do ponto de impacto no Bolsonaro
- EXTRA: estrelinhas de dor (#FFFF00) ao redor da cabeca — 3 particulas girando

### Shell Casings
- 1 particula por disparo
- Cor: #B87333 (cobre)
- Tamanho: 3x6px (elongado)
- Lifetime: 600ms
- Fisica: arco parabolico com bounce

---

## Audio Sincronizado

| Evento | Som | Duracao | Trigger |
|---|---|---|---|
| Idle giro | metal spinning + quase drop | 600ms | Frame 3 idle |
| Mira | click de armar + respiracao | 300ms | Frame 1 mira |
| Disparo OK | BANG potente + shell casing tink | 400ms | Frame 1 disparo |
| Falha click | click seco, patetico, triste | 150ms | Frame 1 falha |
| Falha culatra | POP fraco + oof de dor | 350ms | Frame 3 falha |
| Recarga | shells caindo + fumble + click cilindro | 1200ms | Sequencia completa |
| Bordao disparo OK | "TALKEI?!" (confiante, alto) | 600ms | Random 40% disparo OK |
| Bordao falha | "Talkei..." (triste, baixo, descendente) | 800ms | Sempre na falha |
| Bordao disparo 2 | "BOMBA!" | 400ms | Random 20% disparo OK |
| Bordao falha 2 | "Minha arma e brochavel..." | 1200ms | Random 50% falha |
| Bordao crit | "CPF cancelado!" | 800ms | No critical hit |

---

## Interacoes Especiais

### Com Lula
- Se acertar Lula na cabeca: dano reduzido 80% (placa de titanio). Som: CLANG metalico. Bolsonaro: "Ate a cabeca dele e blindada!"
- Se a arma brochar contra o Lula: Lula ri. "Brochavel igual a politica dele, companheiro!"

### Com Xandao
- Bolsonaro TREME ao mirar em Xandao. Chance de falha sobe de 30% pra 60%.
- Se acertar Xandao: dano normal mas Xandao nem flinch. Olha com desdenhoo.
- Se brochar: Xandao ri e o Bolsonaro perde 1s adicional stunado de medo.

### Com BolsoLula
- A metade Bolsonaro do BolsoLula tenta atirar de volta com uma arma identica — ambas brocham simultaneamente. Comedia.

### Com Eduardo
- Se Eduardo esta proximo e a arma brocha: Eduardo tenta consertar. 50% de chance de consertar, 50% de chance de piorar (proxima falha causa dano 2x).

---

## Upgrade Path

| Nivel | Nome | Efeito | Visual |
|---|---|---|---|
| 1 | Arma Brochavel Original | 30% falha, dano base | Revolver dourado camelô |
| 2 | Arma Semi-Brochavel | 25% falha, +15% dano | Dourado mais polido, menos cafona |
| 3 | Arma do Mito | 20% falha, +30% dano, balas explosivas | Gravura "MITO" no cano |
| 4 | Arma Imbrochavel | 10% falha, +50% dano, 2 tiros por disparo | Dourado reluzente + adesivo "IMBROCHAVEL" |

---

## Easter Egg: "Roleta Russa Politica"
Se o jogador pressionar o botao de ataque 6 vezes seguidas sem acertar nada, Bolsonaro entra em modo "Roleta Russa Politica" — aponta a arma pra propria cabeca, gira o cilindro, e puxa o gatilho. 83% de chance de nada acontecer (click dramatico), 17% de chance de... a arma brochar de novo. Nunca funciona. Nem pra se matar o Bolsonaro consegue usar a arma direito.
