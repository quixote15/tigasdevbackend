# ZUMBIS DE BRASILIA — UX Design: Side-View (Metal Slug Style)
### Jenova Chen | Experiencia Emocional Side-Scroller | Abril 2026

**Versao 1.0 — Pivot Side-View**
**Stack: React (menus/HUD overlay) + Phaser 3.88 (gameplay) | Responsive desktop + mobile**

---

> *"A perspectiva lateral nao e apenas estetica. E uma decisao emocional. Quando voce olha de lado, voce ve o rosto do personagem. Voce ve o medo nos olhos do cidadao. Voce ve a expressao grotesca do zumbi antes de ele te alcançar. A profundidade emocional de um jogo e diretamente proporcional a visibilidade do personagem. Side-view e a decisao correta."*

---

## Filosofia Central: O Plano Horizontal Como Tensao

No top-down, o perigo vem de todas as direcoes simultaneamente — e a mente processa isso como estrategia espacial. No side-view, o perigo vem da esquerda e da direita — e a mente processa isso como ameaca proxima, instintiva, visceral. Voce ve o zumbi. Voce ve a distancia entre voce e ele diminuindo. Voce sente o tempo.

Essa e a mudanca fundamental que o pivot traz: de *gerenciamento espacial* para *tensao linear*. De xadrez para corrida de obstaculos. Essa tensao linear e o que torna Metal Slug, Contra e Dead Ahead viciantes. E o que vai tornar Zumbis de Brasilia viciante.

Toda decisao de UX neste documento serve essa tensao.

---

## 1. Input Design — Controles Responsivos

### 1.1 Filosofia Dual-Input

O side-view muda a natureza do controle em relacao ao top-down. No top-down, o jogador precisava de controle omnidirecional (8 direcoes). No side-view, o movimento primario e horizontal, com pulo/agachamento como verticais. Isso simplifica o input e torna os controles mais fisicamente satisfatorios em ambos os paradigmas.

A regra permanece identica ao documento anterior: qualquer acao possivel no desktop e possivel no mobile. Zero acoes exclusivas de plataforma.

---

### 1.2 Mobile — Joystick Virtual + Botoes de Acao

#### Joystick de Movimento (Esquerda)

O joystick virtual e **dinamico**, nao fixo. Aparece onde o polegar toca na metade esquerda da tela. Raio externo: 56px. Raio do stick (cursor interno): 20px. Raio maximo de deslocamento: 36px.

**Dead zone:** 8px a partir do centro. Dentro dessa zona, nenhum movimento e registrado. Isso previne drift de posicionamento natural do polegar e elimina micro-movimentos indesejados que fragmentam a sensacao de controle.

```
Estrutura do Joystick Virtual:

        [  anel externo  ]
       /    raio: 56px    \
      |   [  dead zone  ]  |
      |   |    8px      |  |
      |   |   [stick]   |  |
      |   |   20px      |  |
      |   |_____________|  |
       \                  /
        [________________]

Alpha do anel externo: 40% (semi-transparente, nao bloqueia visibilidade)
Alpha do stick interno: 70%
Cor: #F0E8D0 (creme) com borda #3A2A1A (marrom escuro)
```

**Direcoes mapeadas:**
- Esquerda / Direita: movimento horizontal (primario)
- Cima (joystick para cima): pulo (se implementado) ou acao contextual
- Baixo (joystick para baixo): agachamento / rolar para desviar

**Resposta de movimento:** A velocidade e proporcional ao deslocamento do stick. 50% de deslocamento = 70% da velocidade maxima (curva de resposta ligeiramente exponencial para controle mais fino em velocidades baixas).

**Fade-out:** O joystick aparece em 80ms e desaparece 1.5 segundos apos o polegar levantar. Nao pisca, nao reposiciona abruptamente.

#### Botao de Ataque (Direita)

Toque simples na **metade direita da tela** dispara ataque. A area inteira e o botao — nao ha hitbox pequena para errar.

Tamanho da area de toque: 50% da largura da tela x 70% da altura (reservando topo para HUD e fundo para o botao especial).

**Auto-aim assistido (Mobile):**
O sistema de mira automatica no mobile segue esta hierarquia de alvos:
1. Inimigo mais proximo ao player no mesmo plano horizontal (prioridade maxima)
2. Inimigo na direcao atual do movimento
3. Inimigo com menor HP (desempate)

O lock-on e suave — uma leve correção da trajetoria do ataque, nao um snap teleporte. O jogador sente que seu ataque foi preciso, nao que o jogo "ajudou". A diferenca e sutil e intencional.

**Hitbox assistida:** Hitboxes dos inimigos sao 15% maiores no mobile. Invisivel ao jogador. Essencial para a sensacao de que atacar e satisfatorio.

#### Botao de Habilidade Especial (Direita, canto inferior)

Botao dedicado: 60x60px, canto inferior direito. Toque simples ativa a habilidade especial do personagem selecionado (arma especial, poder unico).

Area de toque real: 80x80px (maior que o visual para compensar imprecisao de polegar).

**Visual:** Icone da habilidade + barra circular de cooldown ao redor. Quando em cooldown, escurece para 40% de opacidade. Quando disponivel, pulsa levemente (scale 1.0 a 1.05 em 800ms, loop).

```
Layout Mobile Landscape (zona de controle):

┌─────────────────────────────────────────────────────┐
│  [HUD — HP / Score / Wave]                          │  ← React overlay
├──────────────────────────┬──────────────────────────┤
│                          │                          │
│   ZONA JOYSTICK          │   ZONA ATAQUE            │
│   (polegar esquerdo)     │   (polegar direito)      │
│                          │                          │
│   [====CANVAS PHASER====]│[========================]│
│                          │                          │
│   Joystick dinamico      │   Toque = ataque         │
│   aparece no touch       │                          │
│                          │        [ESPECIAL]        │
└──────────────────────────┴──────────────────────────┘
                                          ↑ 60x60px, canto inf. direito
```

#### Feedback Haptico (Mobile)

| Evento | Vibracao | Padrao |
|---|---|---|
| Hit confirmado (acertou zumbi) | 15ms | Curto, positivo |
| Recebeu dano | 30ms | Medio, negativo |
| Morte do player | 3x pulsos de 25ms (50ms intervalo) | Ritmo de fade |
| Coletou power-up | 10ms suave | Muito sutil, positivo |
| Habilidade especial ativada | 20ms + 10ms (100ms depois) | Dois toques = poder |
| Boss aparece | 40ms longo | Impacto, aviso |

Usa `navigator.vibrate()`. Fallback silencioso quando nao suportado.

---

### 1.3 Desktop — Teclado + Mouse

#### Movimento

**WASD** (padrao gamer) e **Setas direcionais** (padrao alternativo) funcionam simultaneamente.

| Input | Acao |
|---|---|
| A / Seta esquerda | Mover para esquerda |
| D / Seta direita | Mover para direita |
| W / Seta cima / Space (contexto) | Pulo (se aplicavel) |
| S / Seta baixo | Agachamento / esquiva |

Velocidade de movimento: constante ao pressionar. Sem aceleracao gradual — o controle de Metal Slug e imediato e isso e intencional. Cada frame pressionado = movimento maximo.

**Input buffering:** 1 frame de buffer. Se o jogador pressionar D + Space em rapida sucessao, ambos registram na ordem correta. Zero inputs perdidos por timing.

#### Ataque

**Clique esquerdo do mouse** ou **barra de espaco** disparam ataque.

No desktop, o sistema e **semi-assistido**: o ataque vai na direcao que o personagem esta virado (esquerda ou direita). O mouse nao controla a mira diretamente em side-view (diferente do top-down, onde havia twin-stick). A direcao do personagem e determinada pelo ultimo movimento horizontal.

**Racionale:** Em side-view, a mira por mouse criaria conflito cognitivo — o personagem pode estar indo para a esquerda e o jogador tentaria mirar para a direita com o mouse. Metal Slug resolve isso com ataque na direcao do movimento. Nos seguimos o mesmo principio.

**Excecao:** Armas de projetil com arco (urna eletronica) permitem angulo por mouse — o jogador clica na tela e o projetil vai naquela direcao com arco balístico.

#### Habilidade Especial

**E** ou **Shift** ativam a habilidade especial.

- E: botao de acao primaria (padrao RPG/action)
- Shift: acessivel com a mao esquerda sem sair do WASD

#### Camera Dead Zone

**Dead zone horizontal da camera:** 80px centrada no player. O player pode se mover ate 80px do centro sem a camera se mover. Alem disso, a camera segue suavemente (lerp 0.08 por frame).

Isso evita o efeito de "camera presa ao personagem" que e tonteante em side-scrollers. O jogador ve o que vem pela frente antes de chegar la.

**Dead zone vertical:** A camera nao se move verticalmente a menos que o player suba/desça mais que 40px da posicao base. O cenario e horizontalmente dominante.

```
Dead Zone da Camera (overhead view):

     ←  80px  →  ←  80px  →
   ╔══════════════════════════╗
   ║         VIEWPORT         ║
   ║   ┌──────────────┐       ║
   ║   │  dead zone   │       ║
   ║   │   [PLAYER]   │       ║
   ║   └──────────────┘       ║
   ║                          ║
   ╚══════════════════════════╝
   Camera so move quando player
   sai desta zona central
```

#### Pausa e Contexto de Trabalho

**Esc** ou **P** pausam. Critico: a aba que perde foco (usuário troca de aba) pausa automaticamente o jogo. Quando a aba recupera foco, o jogo exibe um overlay "PAUSA — clique para continuar" por 2 segundos antes de retomar. O jogador nao volta ao meio de uma horde sem aviso.

---

## 2. HUD Layout — React Overlay sobre Canvas Phaser

### 2.1 Arquitetura React + Phaser

O HUD e renderizado em React, posicionado absolutamente sobre o canvas Phaser via CSS:

```
┌─────────────────────────────────────┐
│  <div id="game-container">          │
│    <canvas id="phaser-canvas" />    │  ← Phaser 3.88
│    <div id="hud-overlay" />         │  ← React (z-index: 10)
│    <div id="menu-overlay" />        │  ← React menus (z-index: 20)
│  </div>                             │
└─────────────────────────────────────┘
```

A comunicacao entre Phaser e React usa um **EventEmitter** central (ou Zustand store):

- Phaser emite: `player:hp`, `player:score`, `wave:start`, `player:death`, `combo:update`, `weapon:ammo`
- React escuta e atualiza o HUD sem re-renderizar o canvas
- React emite: `game:pause`, `game:resume` (de botoes de menu)

### 2.2 HUD Desktop (Widescreen — 16:9)

```
┌──────────────────────────────────────────────────────────────────┐
│ [HP ██████████░░░░] [Personagem]    SCORE: 14.820    WAVE 3/5   │  ← top bar, 48px altura
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│                                                                   │
│                    [CANVAS PHASER — GAMEPLAY]                    │
│                                                                   │
│              [x3 COMBO]  ← floating, fade out 2s                │
│                                                                   │
├──────────────────────────────────────────────────────────────────┤
│ [CHINELO x∞] [URNA x3]              [████ ESPECIAL ████]  [II]  │  ← bottom bar, 56px
└──────────────────────────────────────────────────────────────────┘
  ↑ Arma atual + ammo                  ↑ Habilidade especial   ↑ Pausa
```

**Top Bar (48px, full width):**
- Esquerda: Barra de HP. Largura maxima 200px. Cor: #C41C1C (vermelho sangue) preenchido, #3A3530 vazio. Texto do HP numerico ao lado: "78 HP". Icone do personagem selecionado (24x24px) antes da barra.
- Centro: Score numerico. Fonte: Bebas Neue, 28px. Cor: #F0E8D0. Atualiza com animacao de contagem quando novos pontos sao adicionados (tween de 300ms).
- Direita: "WAVE 3/5". Fonte bold, 18px. Quando nova wave comeca, pulsa 3x em amarelo (#FFD700) antes de estabilizar.

**Bottom Bar (56px, full width):**
- Esquerda: Icone da arma atual (32x32px) + contador de municao. "CHINELO x∞" ou "URNA x3". Quando municicao chega em 1, fica vermelho e pisca.
- Direita: Barra de habilidade especial (icon 32x32px + texto do poder) + botao de pausa (32x32px).

**Minimap (opcional, bottom center):**
Quando implementado: mapa do segmento atual em miniatura (120x24px). Mostra posicao do player (ponto branco), spawn zones (pontos vermelhos), e progresso no segmento (borda que avanca). Aparece apenas no desktop. Em mobile, o espaco e muito precioso.

### 2.3 HUD Mobile Landscape

```
┌─────────────────────────────────────────────────────┐
│ [HP ████░░] [Nome]    14.820    W3   [II]           │  ← top, 36px, compacto
├─────────────────────────────────────────────────────┤
│                                                      │
│              [CANVAS PHASER]                         │
│                                                      │
│  [CHINELO x∞]                     [x3 COMBO] fade  │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                          [ESPECIAL] │  ← bottom-right, 48px
└─────────────────────────────────────────────────────┘
```

No mobile landscape, o HUD e mais compacto:
- Top bar: 36px (vs 48px desktop). Fonte reduzida proporcionalmente.
- HP bar: max 140px de largura
- Score: 22px. Wave counter: texto simples "W3"
- Bottom: arma atual + ammo fica no canto inferior ESQUERDO (proximo ao joystick, glanceable)
- Botao especial: canto inferior direito (44px minimo para touch target)
- Pausa: canto superior direito (44x44px)

### 2.4 Combo Counter (Floating)

O combo counter nao tem posicao fixa. Ele flutua acima do player no canvas (implementado como objeto Phaser, nao React — para ter posicao no mundo do jogo).

- Aparece quando combo >= 2
- Texto: "x2 COMBO", "x5 COMBO", "x12 COMBO"
- Fonte: Bebas Neue Bold, tamanho cresce com o combo (16px base + 2px por combo, max 36px)
- Cor: amarelo (#FFD700) ate x5, laranja (#FF6B00) de x5 a x10, vermelho (#C41C1C) acima de x10
- Animacao de entrada: scale de 1.5 para 1.0 em 200ms (punch in)
- Fade-out: apos 2 segundos sem novo hit, desaparece em 400ms (fade + slide up 8px)
- Quando o combo quebra: texto treme (shake) e desaparece em 300ms

```
Evolucao visual do combo:

x2  → amarelo, 18px, discreto
x5  → laranja, 24px, visivel
x10 → vermelho, 32px, dominante
x20 → vermelho pulsante, 36px + screen shake leve
```

### 2.5 Tokens de Informacao — Principio do Zero-Leitura

Cada elemento do HUD deve comunicar estado sem necessidade de leitura ativa. O jogador em flow state nao le — ele percebe perifericamente.

| Elemento | Leitura Zero | Como |
|---|---|---|
| HP bar | Posicao e cor da barra | Cheio=verde, Metade=amarelo, Baixo=vermelho + pisca |
| Score | Nao precisa de leitura | Numero grande, aumenta continuamente |
| Wave | Nao precisa de leitura durante gameplay | Visivel apenas na transicao |
| Ammo | Cor do texto | Normal=branco, Ultimo=vermelho |
| Especial | Brilho / opacidade | Disponivel=brilhante, Cooldown=escuro |

---

## 3. Screen Flow — React Pages e Components

### 3.1 Diagrama Completo

```
[SPLASH — 2s]
      |
      | auto-avança
      v
[MENU PRINCIPAL]
      |
      |──[JOGAR]──────────────────────────────────┐
      |──[SELECAO DE PERSONAGEM]──[CONFIRMAR]──┐  │
      |──[RANKING]                             |  │
      |──[OPCOES]                              |  │
      |──[CREDITOS]                            |  │
                                               |  │
                            ┌──────────────────┘  │
                            v                     │
                    [SELECAO PERSONAGEM]           │
                            |                     │
                            | confirma            │
                            v                     │
              ┌─────────────────────────┐         │
              │         GAMEPLAY        │←────────┘
              │  (Phaser canvas + HUD)  │
              └──────────┬──────────────┘
                         │
             ┌───────────┴───────────┐
             │                       │
          [PAUSA]               [MORTE / FIM]
          overlay               overlay
             │                       │
             |──[CONTINUAR]          |──[MAIS UMA] → GAMEPLAY
             |──[OPCOES]             |──[COMPARTILHAR]
             |──[MENU PRINCIPAL]     |──[RANKING]
                                     |──[MENU PRINCIPAL]
```

### 3.2 Splash Screen (2 segundos)

Animacao de abertura. Fundo preto. Texto datilografado aparece:

```
"Brasilia, abril de 2026.
O Congresso aprovou a Emenda 666.
Os mortos voltaram para votar."
```

Cada linha aparece em 400ms de datilografia. Total: ~1.8s. O logotipo do jogo (Zumbis de Brasilia) faz fade-in ao final. Automaticamente avança para o Menu Principal.

Se assets ainda estao carregando durante o splash, o splash aguarda — o tempo de splash e o tempo de loading. Nunca ha um spinner separado.

### 3.3 Menu Principal

Background: Phaser rodando em loop o cenario da Esplanada (sem interatividade — so animacao de ambiente). Zumbis lentos passam ao fundo. Paralax ativo. O menu existe como React overlay sobre esta animacao.

```
┌────────────────────────────────────────┐
│                                        │
│          [LOGOTIPO ANIMADO]            │
│       ZUMBIS DE BRASILIA               │
│       Congresso dos Mortos             │
│                                        │
│         ┌─────────────────┐            │
│         │   JOGAR AGORA   │            │  ← CTA primario, grande
│         └─────────────────┘            │
│                                        │
│    [Selecionar Personagem]             │  ← secundario
│    [Ranking]                           │
│    [Opcoes]                            │
│    [Creditos]                          │
│                                        │
│  [Entrar / Guest]     [Som: ON/OFF]    │  ← utilidades, discretas
└────────────────────────────────────────┘
```

"JOGAR AGORA" leva direto ao gameplay com o personagem padrao (nao exige selecao). "Selecionar Personagem" permite escolha antes. Respeita o imperativo de zero friccao.

### 3.4 Login / Guest Flow

Sem bloqueio obrigatorio. O jogador pode jogar sem conta (modo guest). Ranking local apenas.

```
[JOGAR AGORA] → detecta: tem conta?
                     |
              SIM ───┴─── NAO
               |           |
           [gameplay]  [pop-up suave, nao bloqueante]
                       "Salvar seu score?"
                       [Entrar com Google] [Jogar como Guest]
                       ← aparece depois do primeiro game over, nao antes
```

O login e sugerido, nunca exigido. Aparece na tela de Game Over, nao antes do jogo comecar.

### 3.5 Selecao de Personagem

Tela com scroll horizontal de personagens. Cada personagem ocupa ~60% da largura da tela (sprite grande, 96-128px de altura exibido em 4x scale). Informacoes ao lado:

- Nome do personagem
- Habilidade especial (icone + texto curto)
- 3 atributos em barras (Velocidade / Forca / Especial)
- Frase caracteristica (estilo satirico)

Selecao: click/tap no personagem + botao "CONFIRMAR". Personagem selecionado faz animacao idle mais exagerada (bounce leve).

### 3.6 Pause Menu (Overlay)

Overlay semi-transparente sobre o canvas Phaser. O jogo pausa imediatamente (Phaser scene paused). A animacao do canvas continua em slow-motion (20% da velocidade) para indicar que o tempo nao parou completamente — e uma pausa, nao um freeze.

```
┌─────────────────────────┐
│       // PAUSA //       │
│                         │
│  [    CONTINUAR     ]   │  ← foco inicial, tecla ESC fecha
│  [ Opcoes de Audio  ]   │
│  [ Sair para o Menu ]   │
│                         │
│  Dica satirica:         │
│  "Zumbi nao tira ferias │
│   nem recesso!"         │
└─────────────────────────┘
```

Uma dica satirica diferente a cada pausa. Nao e instrucao — e humor. O jogador ri, o estresse baixa, ele volta ao jogo.

### 3.7 Game Over Screen

Descrito em detalhes na secao 6 (Social/Share UX). E a tela mais importante do jogo para viralizacao.

---

## 4. Emotional Arc — Flow Theory Aplicada ao Side-View

### 4.1 O Mapa Emocional dos 5 Segmentos

A teoria do Flow de Csikszentmihalyi define o estado ideal como o equilíbrio entre desafio e habilidade. Muito facil = tedio. Muito dificil = ansiedade. O ponto de equilibrio e onde o jogador desaparece dentro do jogo.

Em Zumbis de Brasilia, construimos uma curva emocional deliberada ao longo dos 5 segmentos que nao apenas atinge o flow — mas usa saidas controladas do flow para criar contraste emocional, tornando o retorno ao flow ainda mais satisfatorio.

```
CURVA EMOCIONAL DOS 5 SEGMENTOS

Intensidade
    |
10  |                                          ████████  CLIMAX
    |                                        ████    ████
 9  |                            ████████████           ████
    |                     ██████                            ▓▓  (morte aqui
 8  |              ████████                                     e dramatica)
    |         █████                    ←DESESPERO→
 7  |     █████           ←TENSAO→
    |  ████
 6  |██                ←LIBERDADE→
    |        ←CONFORTO/TUTORIAL→
 5  |──────────────────────────────────────────────────────────── FLOW LINE
    |
 4  |
    |
 3  |
    |___________________________________________________________
        Seg1      Seg2      Seg3      Seg4      Seg5
      (0-90s)  (90-180s) (180-270s) (270-360s) (360-450s+)
```

### 4.2 Segmento 1 — Conforto e Tutorial Invisivel (0 a 90 segundos)

**Estado emocional alvo:** Curiosidade tranquila, sensacao de competencia crescente.

O jogador acabou de chegar na Esplanada. A iluminacao e mais quente do que nos outros segmentos — o laranja do ceu tem menos sangue, mais entardecer. Os ministerios ao fundo parecem quase normais. Dois ou tres vereadores-zumbi aparecem devagar, de frente.

**Por que emocionalmente funciona:** O lado-view revela o rosto dos zumbis pela primeira vez. O jogador ve as caricaturas — o queixao enorme, os olhos esbugalhados, o terno rasgado. A reacao imediata e visual antes de ser de gameplay. Voce ri antes de atacar.

**Mecanica emocional:** Cada kill e recompensado com uma onomatopeia gigante ("TCHAU!", "BENCAO!", "VOTO CANCELADO!") que toma conta da tela. O feedback e desproporcional — exagerado propositalmente. O jogador sente poderoso com esforco minimo. Esta e a fundamentacao do flow.

**Camera:** Neste segmento, a camera tem um zoom ligeiramente mais fechado (2x scale, player maior na tela). Da sensacao de proximidade e controle. Mais seguro. Como estar perto de casa.

### 4.3 Segmento 2 — Liberdade (90 a 180 segundos)

**Estado emocional alvo:** Expansao, maestria, flow state genuino.

O asfalto do Eixo Monumental se abre. O scroll acelera sutilmente (8% mais rapido que o segmento 1). O Congresso no horizonte, que antes parecia fixo, agora parece um pouco mais proximo — mas ainda distante. Os ministerios ao fundo exibem suas placas satiricas conforme o jogador avanca.

**Por que emocionalmente funciona:** O jogador agora domina os controles. O joystick (mobile) ou o WASD (desktop) esta internalizados. O jogador nao pensa mais em "como fazer" — apenas "o que fazer". Esse e o momento de flow. A cadencia de inimigos aumenta moderadamente, mas o jogador esta no pico de competencia. Cada combo soa como musica.

**Mecanica emocional:** Power-ups mais frequentes. A vassoura pode ser trocada pela urna eletronica, que tem um efeito visual especular — o projetil faz arco, bate em varios zumbis, e o sistema de combo explode. E o momento mais fotografavel do jogo. Muitos compartilhamentos acontecem aqui.

**Screen shake:** Neste segmento, o screen shake entra pela primeira vez em kills especiais (matar 3 ou mais com um projetil). Sutil — 4px, 100ms. Apresenta o vocabulario haptico visual que vai escalar nos proximos segmentos.

### 4.4 Segmento 3 — Tensao (180 a 270 segundos)

**Estado emocional alvo:** Concentracao intensa, leve ansiedade controlada.

A musica muda. O tom do ceu escurece (mais roxo, menos laranja). O Espelho D'Agua aparece ao fundo refletindo o ceu apocaliptico. Os inimigos comecam a aparecer de AMBOS os lados simultaneamente. O jogador precisa gerenciar duas frontes.

**Por que emocionalmente funciona:** A introducao de ameaca bidirecional em side-view e um momento de ruptura cognitiva. O jogador que estava relaxado no flow de repente precisa tomar decisoes: vou para a esquerda ou direita? Ataco primeiro quem esta mais perto? O desafio sobe acima do nivel de habilidade atual — e isso e exatamente onde precisa estar para criar tensao sem frustrar.

**Mecanica emocional:** Hit stop (congelar o jogo por 3-5 frames no momento do hit) e introduzido neste segmento para kills especiais. Quando o player acerta o Senador Vitalicio — o inimigo mais resistente ate agora — o hit stop cria um momento de drama. O tempo literalmente congela. O zumbi reage. O jogador respira. O mundo retoma.

**Camera:** Camera zoom-out sutil (de 2x para 1.9x). O jogador ve mais do nivel — mas tambem se sente um pouco menor, mais vulneravel. E uma decisao de direcao de camera que o jogador nao percebe conscientemente, mas sente.

### 4.5 Segmento 4 — Desespero (270 a 360 segundos)

**Estado emocional alvo:** Urgencia, adrenalina, sensacao de "nao vou conseguir".

O Congresso esta proximo agora — as cupulas dominam o ceu. A trilha sonora entra em modo "boss music" ligeiro. O scroll desacelera (a proximidade do objetivo cria peso). Inimigos sao mais rapidos, mais numerosos, mais grotescos. O Boss do segmento — o Candidato Eterno — faz sua primeira aparicao.

**Por que emocionalmente funciona:** O desespero controlado e o sabor emocional mais viciante dos jogos. E o momento em que o jogador morre mais, mas tambem e o momento que ele mais quer tentar de novo. A proximidade do objetivo (Congresso visivel!) cria uma tensao de "ja que to aqui, mais uma tentativa".

**Mecanica emocional:** Screen shake escala aqui. Golpes do boss causam shake de 8px por 200ms. O HP bar fica vermelho pulsante quando abaixo de 30%. O combo counter, se o jogador conseguir manter apesar do caos, fica vermelho brilhante e pulsa com o ritmo da musica. E visualmente lindo E funcionalmente urgente.

**Camera zoom dramatico em kills de boss:** Quando o jogador derrota o Candidato Eterno, a camera faz um zoom-in de 1.9x para 2.4x em 400ms, seguido de zoom-out lento de volta a 1.9x em 1200ms. O personagem do boss fica grande na tela por um momento antes de desaparecer. Cinematico. Merecido.

### 4.6 Segmento 5 — Climax (360 segundos+)

**Estado emocional alvo:** Euforia, epifania, "sou invencivel" seguido de colapso dramatico.

O Congresso esta imediatamente ao fundo. As cupulas, agora proximas, refletem o laranja-sangue do ceu. Os dois ultimos bosses aparecem: o Presidente da Camara dos Mortos (colossal) e o Xandao com seu martelo gigante. O nivel transborda com inimigos. A musica atinge o pico.

**Por que emocionalmente funciona:** O climax precisa ser simultaneamente o melhor e o pior momento. O melhor porque o jogador esta no pico de habilidade — ele chegar ate aqui ja e uma conquista. O pior porque o desafio e intencional e insuperavel no primeiro playthrough. A morte aqui nao e frustrante — e cinematica. "Eu quase!"

**Mecanica emocional:** Slow-motion na morte (0.3x velocidade por 1.5 segundos antes do fade). O player ve cada zumbi que vai le derrubar. Tem tempo de processar. A tela tinge de vermelho nas bordas (vinheta crescente). E a morte mais bela do jogo — e vai gerar o screenshot mais dramatico.

**Camera zoom em kills do climax:** Kills de boss no Segmento 5 tem um zoom adicional mais dramatico: 1.9x para 2.8x em 300ms, com um flash branco de 2 frames no momento do kill. Como um flash de camera. Como um momento historico sendo registrado.

### 4.7 Feedback Tatil — Vocabulario Visual Completo

| Evento | Screen Shake | Hit Stop | Camera Zoom | Outros |
|---|---|---|---|---|
| Hit normal em zumbi | Nenhum | Nenhum | Nenhum | Onomatopeia |
| Kill de zumbi comum | 2px / 80ms | Nenhum | Nenhum | Onomatopeia + particles |
| Kill de senador/lobista | 4px / 120ms | 3 frames | Nenhum | Onomatopeia grande |
| Kill de boss | 8px / 200ms | 5 frames | 2x→2.4x / 400ms | Explosao completa |
| Player recebe dano | 6px / 150ms | Nenhum | Nenhum | Flash vermelho (bordas) |
| Combo x5 | 3px / 100ms | Nenhum | Nenhum | Combo counter escala |
| Combo x10+ | 5px / 150ms | Nenhum | Nenhum | Combo counter pulsa |
| Morte do player | 0 (slow-mo) | Nenhum | Nenhum | Slow-mo + vinheta |
| Power-up coletado | Nenhum | Nenhum | Nenhum | Brilho + som |
| Wave nova comecando | 4px / 200ms | Nenhum | Nenhum | Texto de wave |

**Regra de ouro:** O screen shake nao pode ocorrer ao mesmo tempo que o hit stop. Hit stop primeiro (3-5 frames), depois shake. A sequencia cria ritmo — primeiro o impacto (hit stop = pausa dramática), depois a consequencia (shake = o mundo reagindo ao impacto).

---

## 5. Onboarding — Os Primeiros 30 Segundos

### 5.1 Filosofia: Ensinar Pelo Mundo, Nao Por Texto

Nenhum tutorial explicito. Nenhuma seta apontando para botoes. Nenhum pop-up de "pressione A para atacar". O jogo ensina atraves do design do nivel e do comportamento dos inimigos. O jogador aprende como aprende qualquer coisa na vida real: tentando, errando, entendendo.

**Referencia:** A abertura de Super Mario Bros (1985). Nenhuma instrucao. O cogumelo vem da direita. O foco de atencao do jogador vai para a direita. Mario corre para a direita. Ele aprende que ha inimigos. Ele pula. Ele aprende que o pulo funciona. Tudo isso em 15 segundos, sem uma palavra.

Nos fazemos o mesmo — so que em vez de cogumelo, ha um vereador-zumbi de terno rasgado.

### 5.2 Os Primeiros 5 Eventos (Scripted)

**Evento 1 — O Primeiro Zumbi (0 a 8 segundos)**

O jogo comeca. O player esta parado no centro-esquerda da tela. O cenario esta quieto. Dois segundos de silencio. Entao, pela direita, um vereador-zumbi aparece. Ele e MUITO lento (30% da velocidade normal). Ele cambaleia. Ele esta vindo em direcao ao player.

O que o jogador aprende: ha inimigos. Eles vem pela direita. Preciso fazer algo.

O botao de ataque (mobile) pulsa suavemente — nao e um tutorial, e um convite fisico. O cursor do mouse (desktop) muda para a mira estilizada ao passar sobre o zumbi.

O jogador ataca. O zumbi voa para traz com uma onomatopeia enorme. Satisfacao imediata.

**Evento 2 — O Segundo Zumbi (8 a 16 segundos)**

Agora um assessor-zumbi aparece pela ESQUERDA. Mais rapido que o primeiro. O jogador precisa se virar — precisa se mover.

O que o jogador aprende: inimigos vem de ambos os lados. O movimento e necessario, nao opcional.

Se o jogador nao se mover por 2 segundos, o cenario faz um leve tremer (dica visual: "algo esta chegando perto"). Isso incentiva o movimento sem instrucao verbal.

**Evento 3 — O Primeiro Power-Up (16 a 22 segundos)**

Apos os dois primeiros kills, um power-up aparece no chao — a Urna Eletronica. Ela brilha e tem uma animacao de flutuacao. Claramente e um objeto para pegar.

O que o jogador aprende: ha itens para coletar. Passar sobre eles os coleta.

Se o jogador nao coletar em 4 segundos, o item pulsa mais intensamente (escala 1.0 a 1.3, urgencia crescente). Ainda sem instrucao — apenas design visual.

**Evento 4 — O Primeiro Combo (22 a 28 segundos)**

Tres zumbis aparecem em rapida sucessao. Se o jogador matar dois em menos de 2 segundos, o contador de combo aparece pela primeira vez: "x2 COMBO!" com a animacao de punch-in.

O que o jogador aprende: matar rapidamente e bonificado. O ritmo de ataque importa.

**Evento 5 — O Primeiro Grupo (28 a 35 segundos)**

Um grupo de 4 assessores-zumbi aparecem juntos pela direita. E o primeiro momento em que o jogador precisa TOMAR UMA DECISAO: fujo para a esquerda ou enfrento?

O que o jogador aprende: o jogo exige escolhas. Ha tensao genuina. Estou jogando, nao executando instrucoes.

Este e o momento em que o onboarding termina e o jogo comeca de verdade.

### 5.3 Principios de Design do Onboarding

**Principio 1: Zero Zero (Zero texto, Zero espera)**
Nenhuma instrucao textual nos primeiros 30 segundos. Nenhuma tela de espera. O jogador esta em movimento desde o frame 1.

**Principio 2: Cada nova mecanica aparece sozinha primeiro**
O primeiro zumbi testa apenas ataque. O segundo testa apenas movimento. O power-up testa apenas coleta. Nunca duas mecanicas novas ao mesmo tempo.

**Principio 3: Falhar nao pune nos primeiros 15 segundos**
Se o jogador levar dano nos primeiros 15 segundos, o dano e reduzido a 50% do normal (sem aviso). Um erro de iniciante nao deve matar — deve ensinar. O jogo sera implacavel depois. Nos primeiros 15 segundos, e generoso.

**Principio 4: A primeira vitoria e garantida**
O primeiro zumbi e lento o suficiente para que qualquer jogador, mesmo nunca tendo jogado um jogo antes, consiga atacar antes de levar dano. A primeira vitoria cria confianca. A confianca cria engajamento.

---

## 6. Social / Share UX

### 6.1 Screenshot Automatico no Game Over

No momento da morte do player, antes do fade a preto, o jogo captura um screenshot do canvas Phaser + HUD React (via `html2canvas` ou `Canvas.toDataURL()`). O screenshot e guardado em memoria.

O screenshot captura o estado EXATO da tela no momento da morte: o player caindo, zumbis ao redor, score no HUD, cenario de fundo. Cada morte tem um screenshot unico. E o momento mais dramatico cristalizado.

**Composicao da Imagem Compartilhada (gerada em canvas separado, nao screenshot raw):**

```
┌──────────────────────────────────┐
│                                  │  Formato: 1200x630px (Open Graph)
│  [SCREENSHOT DO MOMENTO DA MORTE │  ou 1080x1920px (Stories vertical)
│   — mostra cenario, player       │
│   caindo, zumbis ao redor]       │
│                                  │
│  Overlay gradient escuro (bottom)│
│                                  │
│  ┌──────────────────────────┐    │
│  │ "MANDATO ENCERRADO"       │    │  Manchete satirica (gerada dinamicamente)
│  │ SCORE: 14.820             │    │  Score em destaque
│  │ 247 zumbis | 2min34s      │    │  Stats da partida
│  │ "Vereador dos Mortos"     │    │  Titulo politico ganho
│  └──────────────────────────┘    │
│                                  │
│  congressodosmortos.com.br       │  URL sempre visivel
└──────────────────────────────────┘
```

A imagem e gerada em `<canvas>` offscreen, sem exibir ao usuario. Quando o usuario clica "Compartilhar", a imagem ja esta pronta.

### 6.2 Botao de Compartilhamento

**Mobile — Web Share API:**
```javascript
navigator.share({
  title: 'Meu mandato acabou em Zumbis de Brasilia',
  text: `Sobrevivi ${tempoFormatado} e matei ${zombiesKilled} zumbis. Score: ${score}. Consegue mais?`,
  url: 'https://congressodosmortos.com.br',
  files: [imageFile] // screenshot gerado
})
```
Abre o share sheet nativo do iOS/Android. O usuario escolhe WhatsApp, Instagram Stories, etc.

**Desktop — Fallback:**
- Download da imagem automatico
- Texto pre-escrito copiado para o clipboard
- Links diretos para Twitter/X e WhatsApp Web

### 6.3 Titulos Satiricos por Score (Game Over Screen)

| Score | Manchete | Titulo Politico |
|---|---|---|
| 0 - 500 | "IMPUGNADO ANTES DE COMECAR" | Cabo Eleitoral Zumbi |
| 501 - 2.000 | "MANDATO DE ZERO DIAS" | Suplente dos Mortos |
| 2.001 - 5.000 | "APROVADO NA COMISSAO DE SOBREVIVENCIA" | Vereador dos Mortos |
| 5.001 - 10.000 | "REELEITO? NAO. COMIDO." | Deputado Estadual Zumbi |
| 10.001 - 20.000 | "FOI ATE ONDE PODIA, DEPUTADO" | Deputado Federal dos Mortos |
| 20.001 - 40.000 | "SENADOR BLINDADO (de verdade)" | Senador Vitalicio Zumbi |
| 40.001 - 80.000 | "CARGO COMISSIONADO NO APOCALIPSE" | Ministro da Resistencia |
| 80.001+ | "CANDIDATO ETERNO — APROVADO PELO POVO" | Candidato Eterno |

### 6.4 Deep Link para Desafio

Quando o usuario compartilha, o link contem um query param de desafio:

```
https://congressodosmortos.com.br?desafio=14820&from=João+Silva
```

Quando um amigo clica neste link:
1. O jogo carrega normalmente
2. No canto superior da tela aparece um banner discreto: "Desafio de Joao Silva: 14.820 pts"
3. Durante o gameplay, uma linha tracejada no score counter indica onde esta o score alvo
4. Se o jogador supera o desafio, animacao especial ("DESAFIO SUPERADO!") e novo screenshot automatico gerado

O deep link cria um loop social: jogar, compartilhar, desafiar, jogar.

### 6.5 Ranking Social

Tela de ranking acessivel pelo menu ou pelo botao na tela de Game Over. Nao bloqueia o jogo.

- Top 10 global
- Posicao do jogador (mesmo fora do top 10)
- Amigos (via OAuth social, opcional)
- Filtros: Hoje / Semana / Todos os tempos / Por personagem

---

## 7. Responsividade — Breakpoints e Comportamentos

### 7.1 Matriz de Breakpoints

| Breakpoint | Definicao | Comportamento |
|---|---|---|
| Mobile Portrait | < 768px largura, portrait | Bloqueado — exige rotacao |
| Mobile Landscape | >= 480px largura, landscape, altura <= 430px | Layout otimizado (secao 7.3) |
| Tablet | >= 768px, altura >= 500px | Layout intermediario |
| Desktop HD | >= 1280px | Layout completo (secao 2.2) |
| Desktop Wide | >= 1920px | Canvas 3x scale, HUD mais rico |

### 7.2 Mobile Portrait — Tela de Bloqueio

Quando o dispositivo esta em portrait e e mobile (largura < 768px), o jogo exibe uma tela de bloqueio gracioso:

```
┌────────────────┐
│                │
│   [ICONE DE    │
│    ROTACAO]    │
│                │
│  "Vire o       │
│   celular      │
│   para sobreviver"│
│                │
│  (o zumbi      │
│   tambem       │
│   nao consegue │
│   andar de     │
│   lado assim)  │
│                │
└────────────────┘
```

Texto satirico para manter o tom do jogo mesmo na tela de bloqueio. O jogo pausa e espera a rotacao — nao fecha, nao perde progresso.

Deteccao via:
```javascript
window.addEventListener('orientationchange', handleOrientation)
// E via media query: @media (orientation: portrait) and (max-width: 767px)
```

### 7.3 Mobile Landscape — Layout Otimizado

Canvas Phaser ocupa toda a largura. React HUD se adapta:

- Top bar: 36px (compactada)
- Bottom bar: removida — controles ficam sobre o canvas (transparentes)
- Joystick: dinamico, zona esquerda 45% da tela
- Botao especial: canto inferior direito, 48x48px
- Fonte minima de HUD: 14px
- Botao de pausa: canto superior direito, 44x44px (minimo touch target)

### 7.4 Phaser Canvas Resize via React

O canvas Phaser responde ao tamanho do container React:

```typescript
// GameContainer.tsx
const [canvasSize, setCanvasSize] = useState({ width: 0, height: 0 })

useEffect(() => {
  const updateSize = () => {
    const container = containerRef.current
    if (!container) return
    const { width, height } = container.getBoundingClientRect()
    setCanvasSize({ width, height })
    // Emite evento para Phaser redimensionar
    EventBus.emit('resize', { width, height })
  }

  const ro = new ResizeObserver(updateSize)
  ro.observe(containerRef.current!)
  return () => ro.disconnect()
}, [])
```

No lado Phaser:
```javascript
// PhaserGame.ts
EventBus.on('resize', ({ width, height }) => {
  game.scale.resize(width, height)
  // Reposiciona camera e HUD interno
})
```

O canvas Phaser mantem o aspect ratio 16:9 via `ScaleManager` com `FIT` mode:
- Sempre cabe dentro do container
- Barras pretas (letterbox) acima/abaixo se necessario — nunca deforma o jogo
- A logica de jogo usa coordenadas no espaco logico (480x270) — o scale e transparente

### 7.5 Font Scaling

Fontes do HUD React usam `clamp()` para escala proporcional:

```css
/* Score principal */
.hud-score {
  font-size: clamp(18px, 2.5vw, 32px);
}

/* HP label */
.hud-hp-label {
  font-size: clamp(12px, 1.5vw, 18px);
}

/* Wave counter */
.hud-wave {
  font-size: clamp(14px, 2vw, 24px);
}
```

Fontes no canvas Phaser (onomatopeias, combo counter) usam escala proporcional ao viewport logico (480x270). O combo counter em 36px no logico aparece em 72px na tela a 2x scale — sempre proporcional.

### 7.6 Touch Target Minimos

Todo elemento interativo respeita o minimo de **44x44px** de area de toque (Apple HIG / Google Material guideline):

| Elemento | Tamanho Visual | Area de Toque Real |
|---|---|---|
| Botao Especial | 60x60px | 60x60px (ja adequado) |
| Botao Pausa | 32x32px | 44x44px (padding adicional) |
| Botoes de Menu | min 48px altura | 48px altura, largura completa |
| Itens do Pause Menu | min 44px altura | 44px altura |
| Botao Compartilhar | 56px altura | 56px altura |
| Botao "Mais Uma" | 64px altura | 64px altura (CTA primario) |

### 7.7 Performance por Dispositivo

O jogo detecta capacidade do dispositivo no primeiro carregamento:

```javascript
// Deteccao simples por fps inicial
let frameCount = 0
const testStart = performance.now()
const testLoop = () => {
  frameCount++
  if (performance.now() - testStart < 500) {
    requestAnimationFrame(testLoop)
  } else {
    const fps = frameCount * 2 // fps nos primeiros 500ms
    applyQualityPreset(fps >= 55 ? 'high' : fps >= 35 ? 'medium' : 'low')
  }
}
requestAnimationFrame(testLoop)
```

| Preset | Parallax Layers | Particulas | Screen Shake | Shadow |
|---|---|---|---|---|
| High | 7 camadas | Completo | Full | Sim |
| Medium | 4 camadas | Reduzido (50%) | Full | Nao |
| Low | 2 camadas | Minimo | Reduzido | Nao |

O preset e aplicado silenciosamente. O jogador em dispositivo fraco nunca ve uma mensagem de "modo de baixo desempenho" — o jogo simplesmente funciona.

---

## 8. Componentes React — Mapa de Implementacao

### 8.1 Hierarquia de Componentes

```
<App>
  <Router>
    <SplashScreen />          // Rota: /splash (auto-redireciona)
    <MainMenu />              // Rota: /
    <CharacterSelect />       // Rota: /characters
    <GameContainer>           // Rota: /play
      <PhaserCanvas />        // Phaser 3.88 montado aqui
      <HUDOverlay>
        <TopBar>
          <HPBar />
          <ScoreCounter />
          <WaveIndicator />
        </TopBar>
        <ComboCounter />      // Posicionado sobre canvas via absolute
        <BottomBar>
          <WeaponInfo />
          <SpecialAbility />
          <PauseButton />
        </BottomBar>
        <MinimapWidget />     // Desktop only
      </HUDOverlay>
      <MobileControls>        // Mobile only
        <VirtualJoystick />
        <SpecialButton />
      </MobileControls>
      <PauseOverlay />        // Conditional
      <PortraitBlock />       // Mobile portrait only
    </GameContainer>
    <GameOver />              // Rota: /game-over
    <Ranking />               // Rota: /ranking
    <Options />               // Rota: /options
  </Router>
</App>
```

### 8.2 State Management

Zustand store central:

```typescript
interface GameStore {
  // Estado do jogo (sincronizado com Phaser via EventBus)
  hp: number
  maxHp: number
  score: number
  currentWave: number
  totalWaves: number
  combo: number
  weaponType: string
  ammo: number | 'infinite'
  specialCooldown: number // 0-1
  
  // Estado da sessao
  lastGameResult: GameResult | null
  
  // Estado da UI
  isPaused: boolean
  isGameOver: boolean
  orientation: 'portrait' | 'landscape'
  deviceType: 'mobile' | 'tablet' | 'desktop'
  qualityPreset: 'high' | 'medium' | 'low'
}
```

---

## 9. Principios de Acessibilidade Como Design

Acessibilidade neste jogo nao e uma lista de checagem — e uma extensao dos principios de design emocional. Um jogo que exclui pessoas por razoes tecnicas e um jogo com emocao incompleta.

**Contraste minimo:** Todos os elementos do HUD respeitam WCAG AA (4.5:1 para texto normal, 3:1 para texto grande e componentes UI). A paleta do jogo — fundo escuro, texto em `#F0E8D0` — ja favorece contraste naturalmente.

**Reducao de movimento:** `@media (prefers-reduced-motion: reduce)` desativa screen shake e hit stop. O jogo ainda e completamente jogavel — apenas sem os efeitos mais intensos de camera.

**Alto contraste:** `@media (prefers-contrast: high)` aumenta a opacidade do HUD para 100% e adiciona bordas brancas nos elementos interativos.

**Som opcional:** O jogo funciona completamente sem som. Todo feedback sonoro tem um equivalente visual. Nenhuma instrucao e transmitida apenas por audio.

**Tamanho de fonte ajustavel (Opcoes):** Configuracao de escala do HUD em 3 tamanhos (Normal / Grande / Muito Grande). Afeta apenas React HUD — o canvas Phaser usa suas proprias configuracoes.

---

## 10. Metricas de Sucesso UX

Os principios de design emocional precisam de metricas para validar que funcionam. Estas sao as metricas alvo para os primeiros 30 dias:

| Metrica | Definicao | Alvo |
|---|---|---|
| Time to First Action | Tempo do carregamento ate primeiro ataque | < 5 segundos |
| Session Duration (primeira sessao) | Quanto tempo o jogador passa na primeira visita | > 90 segundos |
| Replay Rate | % de jogadores que clicam "Mais Uma" apos o primeiro game over | > 60% |
| Share Rate | % de game overs que resultam em compartilhamento | > 15% |
| Mobile Completion | % de sessoes mobile que chegam ao Segmento 3+ | > 30% |
| Drop-off no Onboarding | % de jogadores que saem antes de 30 segundos | < 20% |

O Replay Rate e a metrica mais importante. Um jogo que nao faz o jogador querer jogar de novo falhou como experiencia emocional — independente de quantas features tem.

---

*Jenova Chen | Zumbis de Brasilia — UX Side-View Design | Abril 2026*
*"O jogo perfeito e aquele que o jogador nao percebe que esta aprendendo — porque esta vivendo."*
