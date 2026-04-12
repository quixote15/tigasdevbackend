# ALCKMIN (Alcool em Mim) - Sprite Specification

## Overview
- **Character Type:** NPC Aliado comico
- **Sprite Dimensions:** 64x64px (personagem), 32x32px (projeteis de cafe)
- **Sprite Sheet Layout:** Horizontal strip, 1 row por animacao
- **Format:** PNG com transparencia alpha
- **Anchor Point:** Bottom-center (32, 60) -- base dos pes
- **Perspectiva:** Top-down levemente isometrica (Y-sorting)

## Silhueta Geral

Alckmin e um homem de meia-idade com postura de mordomo servil. A PIADA ANATOMICA e que suas costas sao PERMANENTEMENTE curvadas (de tanto se curvar para servir), bracos desproporcionalmente longos (de tanto carregar malas), sorriso que NUNCA sai do rosto (perturbador, fixo como mascara), e pescoco inclinado 30 graus para cima (sempre olhando para o chefe). Cabelo impecavelmente penteado -- nunca fora do lugar, nem no apocalipse zumbi. Aventalzinho de mordomo marrom sobre camisa branca. Bandeja de cafe equilibrada na mao direita com xicara fumegante.

A cabeca e ligeiramente grande demais (proporcao Andre Guedes 1:5). O sorriso ocupa 60% do rosto -- dentes perfeitamente alinhados, olhos apertados de subserviencia. As costas formam um arco permanente de ~40 graus. Os bracos alcancam abaixo dos joelhos.

## Paleta de Cores

| Elemento               | Hex Code  | Uso                                |
|------------------------|-----------|------------------------------------|
| Camisa branca          | `#E8E5DA` | Camisa de mordomo (branco encardido)|
| Camisa branca (light)  | `#F5F3EB` | Highlights da camisa               |
| Camisa branca (shadow) | `#C4C0B3` | Sombras/dobras da camisa           |
| Calca preta            | `#1A1A1A` | Calca social                       |
| Calca preta (light)    | `#2D2D2D` | Highlights calca                   |
| Avental marrom          | `#6B4226` | Aventalzinho de mordomo            |
| Avental marrom (light)  | `#8B5E3C` | Highlights avental                 |
| Avental marrom (dark)   | `#4A2E1A` | Sombras avental                    |
| Bandeja bege           | `#C8A96E` | Bandeja de cafe                    |
| Bandeja bege (light)   | `#D9BE88` | Reflexo metalico na bandeja        |
| Bandeja bege (shadow)  | `#A08040` | Sombra da bandeja                  |
| Cafe marrom escuro     | `#3E1F0D` | Liquido do cafe na xicara          |
| Cafe vapor             | `#D4C5A9` | Fumaca/vapor do cafe (50% opacity) |
| Pele                   | `#E0B898` | Pele do rosto/maos                 |
| Pele (shadow)          | `#C49A78` | Sombras da pele                    |
| Cabelo preto           | `#1E1E1E` | Cabelo penteado impecavel          |
| Cabelo (brilho)        | `#3A3A3A` | Brilho do gel no cabelo            |
| Dentes                 | `#F0E8D0` | Sorriso permanente                 |
| Olhos                  | `#2C2C2C` | Olhos apertados de subserviencia   |
| Xicara branca          | `#F0EDE5` | Xicara de cafe                     |
| Outline                | `#0D0D0D` | Linhas grossas 2px (Crumb style)   |
| Shadow                 | `#0A0A0A` | Drop shadow, 50% opacity           |
| Sorriso rosa           | `#D4868A` | Labios do sorriso perturbador      |
| Faixa presidencial     | `#2E7D32` | Faixa verde-amarela (skin interino)|
| Faixa amarela          | `#F9A825` | Detalhe da faixa presidencial      |

---

## IDLE - 4 Frames (idle_alckmin)

**Sprite Sheet:** `alckmin_idle.png` -- 256x64px (4 frames x 64px)

### Frame 0: Idle Base
- **Posicao:** 0,0 a 63,63
- **Descricao:** Alckmin em posicao padrao de mordomo. Costas curvadas 40 graus, pescoco esticado para cima e para frente. Bandeja de cafe na mao direita estendida (braco longo), xicara fumegante com 2 pixels de vapor subindo. Mao esquerda atras das costas (postura de mordomo classico). Sorriso ENORME e fixo -- dentes visiveis, olhos apertados. Cabelo impecavelmente penteado com brilho de gel. Aventalzinho marrom sobre camisa branca. Calca preta com sapatos sociais. Linhas grossas de contorno (2px). Sombra embaixo.
- **Estilo:** Exagero maximo nas proporcoes -- bracos longos demais, costas curvadas demais, sorriso largo demais. O sorriso deve parecer PERTURBADOR de tao permanente. Tracejado Crumb: irregular, pesado, organico.

### Frame 1: Bandeja Tremor 1
- **Posicao:** 64,0 a 127,63
- **Descricao:** Identico ao Frame 0 MAS a bandeja inclina 3px para a esquerda. O cafe na xicara inclina correspondentemente. Uma gotinha de cafe (2x2px marrom escuro) pinga da borda da xicara. O sorriso se mantem identico -- ele NAO percebe o tremor. 1 pixel de vapor sobe.
- **Detalhe humor:** A bandeja treme mas o sorriso e INABALAVEL.

### Frame 2: Bandeja Tremor 2
- **Posicao:** 128,0 a 191,63
- **Descricao:** Bandeja volta ao centro. A gotinha de cafe sumiu (caiu). Vapor do cafe se move 1px para a direita. Leve ajuste na postura -- tronco endireita 2px (tenta manter compostura). Sorriso identico. Olhos talvez 1px mais apertados (esforco de equilibrar).
- **Detalhe humor:** A luta silenciosa entre a gravidade e a subserviencia.

### Frame 3: Bandeja Tremor 3
- **Posicao:** 192,0 a 255,63
- **Descricao:** Bandeja inclina 2px para a DIREITA. Outra gotinha de cafe no ar. O corpo compensa a inclinacao curvando 1px mais para a esquerda. Vapor do cafe se move. Sorriso identico -- perturbadoramente fixo. Micro-gota de suor (1px) na testa.
- **Detalhe humor:** Ele esta derramando cafe EM LOOP e ninguem nota.

---

## WALK - 6 Frames (walk_alckmin)

**Sprite Sheet:** `alckmin_walk.png` -- 384x64px (6 frames x 64px)

### Frame 0: Passo Esquerdo - Contato
- **Posicao:** 0,0 a 63,63
- **Descricao:** Pe esquerdo a frente, toque no chao. Corpo curvado em arco permanente. Bandeja na mao direita (estendida pelo braco longo) perfeitamente nivelada APESAR da caminhada torta. Mao esquerda estendida carregando mala invisivel (habito). Sorriso intacto. Cabelo perfeito. Passo curto e apressado de quem serve.
- **Movimento:** Caminhada de mordomo eficiente -- rapida, rasteira, quase deslizando.

### Frame 1: Passo Esquerdo - Impulso
- **Posicao:** 64,0 a 127,63
- **Descricao:** Corpo transfere peso para pe esquerdo. Leve bounce do tronco (2px para baixo). A bandeja sobe 1px (compensacao). O braco esquerdo balanca para tras. Sorriso intacto. Avental ondula levemente com o movimento.

### Frame 2: Passo Direito - Transicao
- **Posicao:** 128,0 a 191,63
- **Descricao:** Ambos os pes no chao brevemente. Corpo em posicao mais alta (1px up). Bandeja perfeitamente estavel. Vapor do cafe se movimenta com a direcao do passo. O cabelo permanece impecavel -- NEM UM FIO se move.

### Frame 3: Passo Direito - Contato
- **Posicao:** 192,0 a 255,63
- **Descricao:** Pe direito a frente. Espelho do Frame 0 mas com pe trocado. A curvatura das costas se mantem constante. Bandeja agora inclina 1px (compensacao do passo) mas corrige instantaneamente. Sorriso permanente. Passos curtos -- pernas se movem rapido mas cobrem pouca distancia.

### Frame 4: Passo Direito - Impulso
- **Posicao:** 256,0 a 319,63
- **Descricao:** Espelho do Frame 1 com pe trocado. O corpo bounces 2px. A mao esquerda faz gesto sutil de "estou chegando!" (indicador apontando para frente). Avental ondula. Sorriso, cabelo, curvatura -- tudo fixo.

### Frame 5: Transicao / Deslize
- **Posicao:** 320,0 a 383,63
- **Descricao:** Micro-deslize -- os pes se arrastam levemente (1px motion blur nos sapatos). Corpo se inclina 2px na direcao do movimento. A bandeja compensa perfeitamente. Uma gotinha de cafe quase pinga mas NAO pinga (tensao). O sorriso e tao fixo que parece pintado.
- **Detalhe humor:** Ele caminha como se estivesse em hotel 5 estrelas servindo hóspedes, mas esta no meio de um apocalipse zumbi.

---

## ATTACK - 3 Frames (attack_alckmin)

**Sprite Sheet:** `alckmin_attack.png` -- 192x64px (3 frames x 64px)

### Frame 0: Wind-up -- Levanta Bandeja
- **Posicao:** 0,0 a 63,63
- **Descricao:** Alckmin puxa a bandeja para tras com os bracos longos (a bandeja vai LONGE atras da cabeca). A xicara de cafe inclina perigosamente. O sorriso AUMENTA ligeiramente -- ele vai "servir" cafe. O corpo se desdobra um pouco das costas curvadas (2px mais ereto) para dar impulso. Vapor do cafe se intensifica (3-4px de particulas). Motion blur lines (1px) na bandeja.
- **Expressao:** Sorriso que vai de "subserviente" para "servindo com entusiasmo".

### Frame 1: Mid-swing -- Arremesso de Cafe
- **Posicao:** 64,0 a 127,63
- **Descricao:** ARREMESSO! A bandeja e lancada para frente numa arc. O cafe voa da xicara em forma de projetil marrom (gotoes de 4x4px). A xicara vai junto, girando. 3 motion blur lines. O corpo se estende ao maximo -- os bracos longos dao um alcance absurdo. Sorriso no maximo. Expressao de "cafe quentinho pra voce!". Squash-stretch no corpo (esticado horizontalmente).
- **Projetil:** Jato de cafe quente (sprite separado 32x32, marrom escuro com particulas de vapor).

### Frame 2: Follow-through -- Recupera Bandeja
- **Posicao:** 128,0 a 191,63
- **Descricao:** Alckmin magicamente ja tem OUTRA bandeja com cafe (de onde veio? ninguem sabe). Postura voltando ao arco curvado. Sorriso voltando ao normal subserviente. Uma mancha de cafe na camisa (2-3px marrom). Leve expressao de satisfacao. 1 particula de vapor sobe da nova xicara.
- **Detalhe humor:** A bandeja se materializa como se ele tivesse um estoque infinito. E um mordomo PREPARADO.

---

## DEATH - 4 Frames (death_alckmin)

**Sprite Sheet:** `alckmin_death.png` -- 256x64px (4 frames x 64px)

### Frame 0: Hit Fatal -- Bandeja Voa
- **Posicao:** 0,0 a 63,63
- **Descricao:** Alckmin recebe o golpe final. O corpo se arqueia para tras (curvatura inverte por um instante). A bandeja SAI VOANDO para cima (4px acima da cabeca). A xicara gira no ar com cafe espirrado. O sorriso FINALMENTE vacila -- boca em O de surpresa (PRIMEIRO frame em todo o jogo onde o sorriso some). Cabelo: UM UNICO fio sai do lugar.
- **Impacto emocional:** A quebra do sorriso e o momento CHOCANTE. O jogador nunca viu isso.

### Frame 1: Queda -- Joelhos
- **Posicao:** 64,0 a 127,63
- **Descricao:** Alckmin cai de joelhos. A bandeja esta no ar caindo. Cafe respinga em arco (3-4 gotas 2x2px). O avental se desata. O sorriso VOLTA (reflexo condicionado) mas os olhos estao sem vida. Mao direita ainda estendida na posicao de segurar bandeja (habito muscular). Mao esquerda no chao.
- **Detalhe perturbador:** O sorriso voltou mas e VAZIO. Pior que sem sorriso.

### Frame 2: No Chao -- Ninguem Percebe
- **Posicao:** 128,0 a 191,63
- **Descricao:** Alckmin caido no chao de brucos. A bandeja aterrissa ao lado (intacta, claro). A xicara quebrou em 3 pedacos (2x2px cada). Poça de cafe ao redor da xicara. O sorriso permanece -- caido, morto, sorrindo. O cabelo AINDA esta penteado (mesmo no chao). O avental esta jogado sobre ele como cobertor.
- **Detalhe humor:** Nenhum outro personagem reage. Ninguem nota que ele morreu. O jogo continua normalmente.

### Frame 3: Fade -- Invisibilidade Final
- **Posicao:** 192,0 a 255,63
- **Descricao:** O sprite de Alckmin comeca a ficar transparente (alpha 70%). A bandeja permanece visivel (alpha 100%) -- a bandeja e mais memoravel que ele. Poça de cafe seca. Um texto flutuante micro (se possivel) ou tooltip: "Alguem viu o Alckmin?". O corpo some mas a bandeja FICA.
- **Detalhe humor:** A bandeja de cafe e mais importante que o proprio personagem. Ela permanece como drop item.

---

## HIT - 2 Frames (hit_alckmin)

**Sprite Sheet:** `alckmin_hit.png` -- 128x64px (2 frames x 64px)

### Frame 0: Impacto -- Derrama Cafe
- **Posicao:** 0,0 a 63,63
- **Descricao:** Alckmin toma hit. O corpo recua 4px. A bandeja inclina 15 graus e DERRAMA cafe significativamente (6-8 gotas de 2x2px voam). EXPRESSAO DE PANICO ABSOLUTO -- nao pelo dano, pelo CAFE DERRAMADO. O sorriso some, substituido por boca aberta de horror. Olhos ARREGALADOS. As costas curvam MAIS (defesa). Cabelo: perfeitamente no lugar.
- **Detalhe humor:** Ele nao se importa com a propria vida, se importa com o CAFE.

### Frame 1: Recuperacao -- Salva o Cafe
- **Posicao:** 64,0 a 127,63
- **Descricao:** Alckmin compensa a inclinacao desesperadamente. Bandeja volta a posicao. O cafe que sobrou na xicara esta seguro. SORRISO VOLTA instantaneamente (transicao de panico para subserviencia em 1 frame). Corpo volta a posicao curvada normal. Uma mancha de cafe no avental (novo dano cosmetico). Micro-expressao de alivio nos olhos.
- **Detalhe humor:** O cafe sobreviveu. ISSO e o que importa.

---

## SPECIAL - 6 Frames (special_alckmin / Mordomo Supremo)

**Sprite Sheet:** `alckmin_special.png` -- 384x64px (6 frames x 64px)

### Frame 0: Preparacao -- Modo Mordomo Ativado
- **Posicao:** 0,0 a 63,63
- **Descricao:** Alckmin endireita as costas pela primeira vez (postura ereta!). Olhos brilham com determinacao servil. O avental parece mais limpo/novo. Na mao direita: bandeja de cafe. Na mao esquerda: uma mala. Aos pes: balde e vassoura. QUATRO ITENS ao mesmo tempo. O sorriso atinge nivel MAXIMO -- dentes brilham com flash branco (1px highlight).
- **Transformacao:** A curvatura das costas SOME -- e a unica vez que ele fica ereto.

### Frame 1: Multitask 1 -- Serve Cafe
- **Posicao:** 64,0 a 127,63
- **Descricao:** Braco direito estende a bandeja servindo cafe (particulas de vapor douradas -- cafe ESPECIAL). Braco esquerdo segura mala E vassoura simultaneamente. O pe chuta o balde para a posicao. DOIS bracos fazendo QUATRO tarefas. Motion blur nos bracos (estao se movendo rapido demais). Sorriso maximo. Aureola de competencia domestica (3px glow amarelo ao redor).
- **Efeito:** O cafe servido cura HP dos aliados na area.

### Frame 2: Multitask 2 -- Limpa e Carrega
- **Posicao:** 128,0 a 191,63
- **Descricao:** Agora o braco direito carrega DUAS malas (empilhadas). Braco esquerdo esfrega o chao com vassoura EM VELOCIDADE (motion blur circular). A bandeja de cafe esta EQUILIBRADA NA CABECA (impossivel, mas ele consegue). Pes deslizam no chao (limpando com os sapatos). O avental se transforma em utility belt com itens de limpeza. Sorriso identico. CAOS ORGANIZADO.
- **Efeito:** Limpa debuffs dos aliados.

### Frame 3: Multitask 3 -- Cafe + Malas + Limpeza
- **Posicao:** 192,0 a 255,63
- **Descricao:** TUDO AO MESMO TEMPO. Bracos viraram blur (movendo tao rapido que aparecem em 4 posicoes simultaneamente -- ghosting de 3 bracos extras semitransparentes). Bandeja servindo, mala carregando, chao limpando, cafe passando. Particulas de vapor, bolhas de sabao (2x2px azuis), e estrelas de esforco (1px amarelas) ao redor. O corpo de Alckmin e o centro de um TORNADO DE SERVICO.
- **Peak do special:** Maximo dano/cura. Visualmente o frame mais caótico.

### Frame 4: Exaustao -- Desacelerando
- **Posicao:** 256,0 a 319,63
- **Descricao:** Os bracos-fantasma desaparecem. Velocidade diminui. A bandeja quase cai (inclinada 20 graus). As malas estao empilhadas ao lado. O chao esta limpo (brilhando). Alckmin volta a curvar as costas (2px por frame). Suor aparece (3 gotas 1px na testa). O sorriso NUNCA vacilou.
- **Transicao:** De heroi domestico para mordomo cansado.

### Frame 5: Retorno -- Subserviencia Restaurada
- **Posicao:** 320,0 a 383,63
- **Descricao:** Volta a posicao curvada padrao. Bandeja nivelada novamente com cafe novo. Mala guardada. Vassoura atras das costas. Tudo organizado. Uma plaquinha flutuante (se possivel): "Mais alguma coisa, presidente?". Sorriso subserviente normalizado. Como se nada tivesse acontecido.
- **Detalhe humor:** O mordomo SUPREMO voltou ao mordomo normal. Ninguem agradeceu.

---

## Sprite Sheet Summary

| Animacao | Arquivo                   | Frames | Sheet Size  | FPS   |
|----------|---------------------------|--------|-------------|-------|
| idle     | `alckmin_idle.png`        | 4      | 256x64px    | 8     |
| walk     | `alckmin_walk.png`        | 6      | 384x64px    | 10    |
| attack   | `alckmin_attack.png`      | 3      | 192x64px    | 12    |
| death    | `alckmin_death.png`       | 4      | 256x64px    | 6     |
| hit      | `alckmin_hit.png`         | 2      | 128x64px    | 10    |
| special  | `alckmin_special.png`     | 6      | 384x64px    | 10    |

## Projetil -- Cafe Quente

| Animacao | Arquivo                   | Frames | Sheet Size  | FPS   |
|----------|---------------------------|--------|-------------|-------|
| cafe_fly | `alckmin_projetil.png`    | 3      | 96x32px     | 12    |

### Projetil Frame 0: Xicara Voando
- **Posicao:** 0,0 a 31,31
- **Descricao:** Xicara branca vista de cima, girando. Cafe marrom escuro dentro com vapor. Rotacao 0 graus.

### Projetil Frame 1: Xicara Mid-flight
- **Posicao:** 32,0 a 63,31
- **Descricao:** Xicara rotacionada 120 graus. Cafe espirra pelas bordas (3 gotas). Trail de vapor atras.

### Projetil Frame 2: Xicara Impacto
- **Posicao:** 64,0 a 95,31
- **Descricao:** Xicara quebrando. Splash de cafe quente (8px raio). Fragmentos de ceramica (3 pedacos 2x2px). Vapor intenso. Starburst de queimadura.

---

## Phaser 3 Atlas Keys

```
key: 'npc_alckmin_idle'       frameWidth: 64  frameHeight: 64
key: 'npc_alckmin_walk'       frameWidth: 64  frameHeight: 64
key: 'npc_alckmin_attack'     frameWidth: 64  frameHeight: 64
key: 'npc_alckmin_death'      frameWidth: 64  frameHeight: 64
key: 'npc_alckmin_hit'        frameWidth: 64  frameHeight: 64
key: 'npc_alckmin_special'    frameWidth: 64  frameHeight: 64
key: 'npc_alckmin_projetil'   frameWidth: 32  frameHeight: 32
```

## Notas para o Artista
- O SORRISO e a feature principal. Deve parecer PERTURBADOR de tao fixo. Nunca sai, exceto no Frame 0 de death e Frame 0 de hit
- As costas curvadas sao EXAGERADAS -- arco de 40 graus, como se a coluna fosse feita de borracha
- Os bracos DEVEM parecer longos demais -- chegam abaixo dos joelhos, estilo orangotango
- O cabelo NUNCA se move. Nem em explosao. Gel de titanio
- A bandeja de cafe e quase um personagem independente -- ela tem mais presenca que o Alckmin
- Outlines grossas e irregulares (Robert Crumb). Sombras pesadas. Nada limpo ou bonito
- O avental de mordomo e levemente ridículo -- curto demais, amarrado com laco atras
- A xicara de cafe SEMPRE tem vapor -- e o unico elemento "vivo" do personagem
- Em caso de duvida: mais grotesco, mais curvado, mais subserviente
