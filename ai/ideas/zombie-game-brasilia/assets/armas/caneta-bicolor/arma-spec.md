# Caneta Bicolor — Arma Exclusiva do BOLSOLULA

## Visao Geral

**Dono**: BOLSOLULA (Fusao)
**Tipo**: Melee + Projetil hibrido (Caneta BIC gigante)
**Subtipo**: Dual-mode (vermelho/verde-amarelo) + Area denial + Infinita
**Dimensoes Sprite**: 40x16px (caneta em mao), 24x24px (emenda explosiva)
**Perspectiva**: Top-down levemente isometrica

---

## Descricao Visual

Uma caneta BIC GIGANTE (do tamanho de um bastao de baseball) com corpo hexagonal classico. Metade do corpo e VERMELHA (lado Lula), metade e VERDE-AMARELA (lado Bolsonaro). A tampa de um lado e vermelha, do outro e verde. A ponta escreve em ambas as cores simultaneamente — deixando um rastro bicolor no chao. O plastico e barato, rachado, com marcas de mordida (politico que morde caneta de nervoso). O clip da caneta e uma miniatura da bandeira do Brasil torta.

A caneta NUNCA ACABA — igual mandato de politico. Referencia visual: o furo de ventilacao do corpo BIC esta entupido de documentos microscopicos (emendas parlamentares enroladas).

### Cores Hex
| Elemento | Cor | Hex |
|---|---|---|
| Corpo lado Lula | Vermelho PT | #8B1A1A |
| Corpo lado Bolsonaro | Verde militar | #2E5A1C |
| Tampa Lula | Vermelho mais vivo | #B22222 |
| Tampa Bolsonaro | Amarelo Brasil | #CCAA00 |
| Ponta metalica | Prata suja | #808080 |
| Tinta vermelha | Vermelho sangue | #CC0000 |
| Tinta verde-amarela | Verde vivo | #00AA00 |
| Corpo plastico | Branco sujo translucido | #D4C9B0 |
| Clip bandeira | Verde/amarelo/azul | #009739/#FFDF00/#002776 |
| Emenda (projetil) | Papel amarelado | #D4C170 |
| Explosao emenda | Dourado corrupto | #DAA520 |
| Rastro de tinta chao | Bicolor | #CC0000 / #00AA00 |

---

## Mecanica Dual-Mode

A caneta tem DOIS MODOS que alternam automaticamente com a Troca de Lado do BolsoLula (a cada 5s):

### Modo Lula (Vermelho)
- Escreve emendas vermelhas que CURAM aliados na area (mentira que parece verdade)
- Projetil mais lento, area maior
- Trail vermelho no chao
- Som: som de caneta escrevendo rapido + murmúrio "companheiro"

### Modo Bolsonaro (Verde-Amarelo)  
- Escreve decretos verde-amarelos que causam DANO DIRETO
- Projetil mais rapido, area menor
- Trail verde-amarelo no chao
- Som: carimbo batendo + "TALKEI" sussurrado

---

## Estados da Arma

### 1. Em Mao (Idle) — 4 frames loop
- **Frame 1**: BolsoLula segura a caneta gigante com 2 bracos (um de cada lado). Caneta horizontal. Ponta gotejando tinta bicolor. A caneta pulsa levemente — como se tivesse vida propria.
- **Frame 2**: Mesma pose. A cor dominante da caneta brilha mais (vermelho se Lula domina, verde se Bolsonaro domina). Gota de tinta cai no chao.
- **Frame 3**: BolsoLula gira a caneta 180 graus — troca a ponta de direcao. O lado que estava em cima vai pra baixo. Efeito visual de transicao de cor.
- **Frame 4**: Caneta estabilizada na nova orientacao. Os outros 2 bracos (livres) fazem gestos contraditorios — um faz "arminha", o outro faz "L".
- **Timing**: 600ms, 500ms, 300ms, 600ms (ritmo irregular — esquizofrenico como o dono)

### 2. Assinar Emenda (Ataque Melee) — 3 frames
- **Frame 1**: BolsoLula ergue a caneta gigante com 4 bracos como se fosse uma espada. Tinta respingando das duas pontas. Os dois rostos sorrindo (pela primeira vez concordam em algo: assinar coisas).
- **Frame 2**: SLASH diagonal! A caneta corta o ar deixando um rastro BICOLOR (metade vermelha, metade verde). Respingos de tinta em 360 graus. O rastro forma brevemente as letras "EC 667" (Emenda Constitucional) antes de se dissolver.
- **Frame 3**: Follow-through. A caneta bate no chao e ESCREVE automaticamente uma emenda no piso. Texto ilegivel (juridiques microscopico). A emenda-no-chao pulsa e depois explode em area (24x24px).
- **Timing**: 200ms, 100ms, 350ms
- **Dano melee**: 18 HP (contato direto)
- **Dano area (emenda)**: 12 HP (explosao)
- **Range melee**: 48px (caneta e gigante)

### 3. Lancar Emenda (Ataque Ranged) — 4 frames
- **Frame 1**: BolsoLula aponta a caneta pra frente. A ponta brilha intensamente (carregando). Tinta borbulhando na ponta como lava. Os rostos fazem expressoes opostas (Lula concentrado, Bolsonaro ansioso OU vice-versa).
- **Frame 2**: DISPARO! Um rolo de papel (emenda parlamentar) sai da ponta da caneta como projetil. O rolo se desenrola no ar, girando. Texto visivel no papel: numeros absurdos ("R$ 999.999.999,99") e carimbos.
- **Frame 3**: Recuo da caneta. BolsoLula absorve o recuo com 4 bracos. Tinta respinga pra tras.
- **Frame 4**: Recovery. Tinta da ponta se regenera (nunca acaba). Caneta pronta para proximo disparo.
- **Timing**: 250ms, 80ms, 150ms, 200ms

### 4. Projetil — Emenda Parlamentar (24x24px) — 3 frames loop
- **Frame 1**: Rolo de papel desenrolando no ar. Texto juridico ilegivel. Selos e carimbos visiveis. Brilho dourado de corrupcao. Cor do papel muda conforme modo (rosado no modo Lula, esverdeado no modo Bolsonaro).
- **Frame 2**: Papel se contorcendo no ar como se tivesse vida propria. Numeros com cifrao ($) voando ao redor como particulas. Carimbo "APROVADO" aparecendo e sumindo.
- **Frame 3**: Papel quase fechando de novo em rolo. Pulsando. Prestes a explodir.
- **Timing**: 80ms por frame
- **Velocidade**: Modo Lula 200px/s / Modo Bolsonaro 320px/s
- **Alcance**: 250px

### 5. Explosao de Emenda — 5 frames (32x32px)
- **Frame 1**: Emenda atinge o alvo. Papel explode em confete de documentos. Flash dourado.
- **Frame 2**: EXPLOSAO DE BUROCRACIA! Pedacos de papel, carimbos, selos, assinaturas voando em todas as direcoes. No centro, um holograma momentaneo do valor da emenda ("R$ 61 BILHOES") em texto dourado.
- **Frame 3**: Confete de documentos caindo como neve. Area de efeito marcada no chao com tinta bicolor (circulo vermelho/verde).
- **Frame 4**: Documentos pousando. Alguns pegam fogo espontaneamente. Cinzas.
- **Frame 5**: Residuo: marca bicolor no chao (desaparece em 2s). Ultimo confete caindo.
- **Timing**: 60ms, 120ms, 200ms, 250ms, 300ms

---

## Efeitos de Particula

### Tinta Gotejando (Idle)
- 1 particula a cada 500ms
- Cor: alternando #CC0000 e #00AA00
- Tamanho: 2-3px
- Lifetime: 800ms (espalha ao tocar chao)

### Rastro de Tinta (Walk)
- Trail continuo atras do BolsoLula
- Duas linhas paralelas (vermelha + verde)
- Largura: 2px cada
- Opacity: 0.4 -> 0.0 em 3000ms
- Efeito: marca o caminho por onde BolsoLula passou

### Respingos de Ataque
- 8-15 particulas por ataque
- Cores: mix de #CC0000 e #00AA00
- Tamanho: 1-4px
- Lifetime: 300ms
- Direcao: radial do ponto de contato

### Confete de Emenda
- 20-30 particulas na explosao
- Cores: #D4C170 (papel), #DAA520 (dourado), #CC0000/#00AA00 (tinta)
- Tamanho: 3-6px (retangulares — pedacos de papel)
- Lifetime: 800ms
- Fisica: queda lenta com rotacao (como confete real)

### Cifrao Flutuante
- 3-5 particulas "$" por explosao de emenda
- Cor: #DAA520 (dourado corrupto)
- Tamanho: texto 8px
- Lifetime: 1200ms
- Movimento: flutuam pra cima lentamente

---

## Audio Sincronizado

| Evento | Som | Duracao | Trigger |
|---|---|---|---|
| Idle pulsacao | hum eletrico bicolor (dois tons) | loop 600ms | Durante idle |
| Giro de caneta | whoosh + click plastico | 300ms | Frame 3 idle |
| Melee windup | som de caneta gigante cortando o ar | 200ms | Frame 1 melee |
| Melee impacto | SLASH + papel rasgando + carimbo | 350ms | Frame 2 melee |
| Emenda escrita | scribble furioso + carimbo APROVADO | 350ms | Frame 3 melee |
| Ranged disparo | WHOMP + papel desenrolando rapido | 300ms | Frame 2 ranged |
| Projetil voo | flutter de papel + buzz burocratico | loop 80ms | Durante projetil |
| Explosao | POP + confete + cash register "cha-ching" | 500ms | Frame 2 explosao |
| Modo Lula ativado | "Assina ai, companheiro!" (voz Lula) | 800ms | Na troca de modo |
| Modo Bolsonaro ativado | "Canetada, talkei!" (voz Bolsonaro) | 700ms | Na troca de modo |
| Bordao ataque | "A caneta e bicolor igual a corrupcao!" | 1500ms | Random 25% |
| Bordao dual | "Compan-- VAGABU-- companhei-- TALKEI!" | 1200ms | Random 15% (ambas vozes brigando) |

---

## Interacoes Especiais

### Trail de Tinta como Hazard
- O rastro bicolor no chao causa slow (20%) em quem pisar
- Inimigos que pisam no rastro VERMELHO ficam "hipnotizados" por 1s (efeito do populismo Lula)
- Inimigos que pisam no rastro VERDE ficam "confusos" por 1s (controles invertidos — efeito das fake news)
- Se um inimigo pisar em AMBOS os rastros simultaneamente: stun 2s (paralisia por polarizacao)

### Com Lula ou Bolsonaro (se separados pela Fusao Reversa)
- Se Lula pega a caneta: so escreve em vermelho, dano 1.5x, sem modo dual
- Se Bolsonaro pega a caneta: so escreve em verde, velocidade 1.5x, sem modo dual
- A caneta VOLTA magicamente pro BolsoLula quando ele se refunde

### Emenda Infinita
- A caneta NUNCA precisa recarregar (igual mandato de politico — nunca acaba)
- Se o jogador tenta contar quantas emendas foram lancadas, o numero no HUD comeca a bugar (referencia ao orcamento secreto que ninguem consegue rastrear)

---

## Upgrade Path

| Nivel | Nome | Efeito | Visual |
|---|---|---|---|
| 1 | BIC do Povo | Dano base, trail fino | Caneta BIC classica bicolor |
| 2 | Montblanc da Republica | +30% dano, trail medio, slow 30% | Caneta mais grossa, detalhes dourados |
| 3 | Caneta do Orcamento Secreto | +60% dano, trail largo, emendas rastreiam | Caneta pulsante com aura dourada |
| 4 | Caneta da Emenda 666 | +100% dano, trail permanente, emendas zumbificam | Caneta viva — se contorce, goteja gas verde, olhos no corpo |

---

## Easter Egg: "Assinatura Bipartidaria"
Se BolsoLula usar a caneta para "assinar" (atacar) exatamente 666 vezes numa partida, uma cutscene especial e triggered: a caneta escreve sozinha no chao a frase "EMENDA CONSTITUCIONAL 667 — Perenidade Parlamentar II" e o chao comeca a rachar com gas verde saindo pelas fissuras. Referencia direta ao plot do jogo. O texto aparece metade em vermelho, metade em verde. Os dois rostos do BolsoLula olham pro chao, olham um pro outro, e riem juntos pela primeira vez. Arrepiante.
