# Animation Spec — MONARK (O Rei do Limbo)

> NPC do Game Over / Loja do Limbo. Todas as animacoes acontecem com ele SENTADO.
> Framerate geral: 4-10fps (estilo jerky, twitchy — NUNCA suave).
> Sprites 64x64px. Spritesheets horizontais.
> Engine: Phaser 3 (sprite.anims.play / sprite.play).

---

## 1. Tabela Geral de Animacoes

| ID | Nome | Frames | FPS | Loop | Trigger | Spritesheet |
|---|---|---|---|---|---|---|
| A01 | Idle | 4 | 4 | Sim | Default (nenhuma interacao) | `monark-idle.png` |
| A02 | Talking | 6 | 8 | Sim | Durante dialogo ativo | `monark-talking.png` |
| A03 | Offering Deal | 4 | 6 | Sim | Menu de loja aberto | `monark-deal.png` |
| A04 | Happy Reaction | 6 | 10 | Nao (play once) | Jogador aceita deal | `monark-happy.png` |
| A05 | Shrug | 4 | 6 | Nao (play once) | Jogador recusa deal | `monark-shrug.png` |
| A06 | Podcast Intro | 8 | 8 | Nao (play once) | Inicio do mini-desafio | `monark-podcast-intro.png` |
| A07 | Smoke Loop | 6 | 6 | Sim | SEMPRE (overlay independente) | `monark-smoke.png` |
| A08 | Chair Bob | 2 | 2 | Sim | SEMPRE (tween, nao spritesheet) | N/A (tween) |
| A09 | Entrance | 10 | 8 | Nao (play once) | Primeira vez na tela de Game Over | `monark-entrance.png` |
| A10 | ON AIR Blink | 2 | 1 | Sim | SEMPRE (LED do microfone) | `monark-onair.png` |

---

## 2. Detalhamento Frame-a-Frame

### A01 — IDLE (Sentado no Podcast)
**Contexto**: Estado default. Monark esta sentado, olhando pro nada, chapado. O jogador acabou de morrer e esta vendo o Monark pela primeira vez (ou de novo).

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 250ms | Postura neutra. Olhos semicerrados normais. Sorriso bobo padrao. Mao esquerda no braco da cadeira, mao direita proxima ao microfone. | BASE |
| 1 | 250ms | Palpebras descem 1px (olhos MAIS fechados). Leve inclinacao da cabeca pra esquerda (1px). Ombros relaxam 1px pra baixo. | Olhos -1px, cabeca -1px lateral |
| 2 | 250ms | Palpebras sobem 1px (voltam ao normal). Cabeca volta ao centro. Dedos da mao direita mexem levemente (1px). | Olhos +1px, mao detalhe |
| 3 | 250ms | Palpebras descem 1px de novo. Leve sorriso MAIS largo (+1px canto da boca). Ombro esquerdo sobe 1px (como se respirasse). | Olhos -1px, boca +1px, ombro +1px |

**Loop**: 0 → 1 → 2 → 3 → 0 (suave-ish, mas jerky pelo FPS baixo)

**Efeito combinado com overlays**:
- A07 (Smoke) roda simultaneamente sobre a cabeca
- A08 (Chair Bob) aplica offset Y de +/-2px em todo o sprite
- A10 (ON AIR) pisca o LED do microfone independentemente

---

### A02 — TALKING (Dialogo Ativo)
**Contexto**: Quando caixa de dialogo esta aberta e Monark esta "falando". Os bordoes aparecem em texto enquanto esta animacao roda.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 125ms | Boca ABERTA (retangulo escuro 4x2px). Sobrancelha esquerda sobe 1px. Mao direita sobe 2px (começa gesticulacao). | Boca abre, mao sobe |
| 1 | 125ms | Boca SEMI-FECHADA (2x1px). Sobrancelha direita sobe 1px. Mao direita no ponto mais alto (+4px do idle). | Boca semi, mao +2px |
| 2 | 125ms | Boca ABERTA grande (5x3px, maximo). Ambas sobrancelhas altas. Mao comeca a descer. Chapeu treme (1px lateral). | Boca max, chapeu treme |
| 3 | 125ms | Boca FECHADA (sorriso bobo normal). Sobrancelhas voltam. Mao descendo. | Reset parcial |
| 4 | 125ms | Boca ABERTA novamente (4x2px). Mao volta a posicao quase idle. Olhos abrem LIGEIRAMENTE mais (1px — momento de "lucidez" falsa). | Boca abre, olhos +1px |
| 5 | 125ms | Boca SEMI-FECHADA. Tudo voltando ao neutro. Olhos voltam a semicerrar. Ombros relaxam. | Reset quase completo |

**Loop**: 0 → 1 → 2 → 3 → 4 → 5 → 0
**Nota**: O ciclo de boca NAO sincroniza com o texto (proposital — ele fala no ritmo dele, nao do texto).

---

### A03 — OFFERING DEAL (Loja do Limbo)
**Contexto**: Menu de loja aberto. Monark oferece itens com precos inflacionados.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 167ms | Inclina-se pra frente 2px. Mao esquerda estendida palma pra cima. Sorriso mais largo. Pupilas com reflexo verde (1px `#3D6B3A`). | Lean +2px, mao estende |
| 1 | 167ms | Inclinacao mantida. Mao oscila pra cima 1px (como "pesando" algo). Reflexo verde nas pupilas intensifica. | Mao +1px |
| 2 | 167ms | Inclinacao mantida. Mao desce 1px. Sobrancelha ergue (expressao de "e ai, vai querer?"). Chapeu desliza pra frente 1px. | Mao -1px, chapeu +1px |
| 3 | 167ms | Volta pra tras 1px (mas nao totalmente ao idle). Mao ainda estendida. Reflexo verde some. | Lean -1px, glow off |

**Loop**: 0 → 1 → 2 → 3 → 0

---

### A04 — HAPPY REACTION (Jogador aceita)
**Contexto**: Jogador comprou algo ou aceitou o deal de "segunda chance".

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 100ms | Olhos ABREM (2px mais que normal — revelando pupilas dilatadas por inteiro). | Olhos shock open |
| 1 | 100ms | Bracos comecam a subir. Sorriso se alarga pra MAXIMO. Chapeu comeca a levantar. | Bracos up, smile max |
| 2 | 100ms | Bracos no alto! Chapeu SAI da cabeca (2px acima, flutuando). Fumaca EXPLODE em rajada. Olhos no maximo de abertura. | Chapeu voa, smoke burst |
| 3 | 100ms | Chapeu no ponto mais alto (4px acima da cabeca). Bracos tremem de excitacao. Cadeira balanca 1px lateral. | Chapeu +2px, tremor |
| 4 | 100ms | Chapeu comeca a descer. Bracos descendo. Fumaca dissipando. Olhos comecam a fechar de volta. | Settling |
| 5 | 100ms | Chapeu pousa de volta na cabeca (TORTO pro outro lado agora). Tudo volta quase ao normal. Sorriso ainda largo. | Reset, chapeu flip |

**Play once**, depois retorna a A01 (Idle) ou A03 (Deal) dependendo do contexto.

---

### A05 — SHRUG (Jogador recusa)
**Contexto**: Jogador disse "nao" pro deal. Monark nao liga.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 167ms | Ombros comecam a subir. Olhos fecham MAIS (quase totalmente). Canto da boca vira levemente pra baixo por 1px (mas nao tristeza, indiferenca). | Ombros up, olhos down |
| 1 | 167ms | Ombros no MAXIMO (orelhas quase encobertas). Cabeca inclina ligeiramente pro lado. Palmas das maos viradas pra cima (gesto universal de "tanto faz"). | Ombros max, palms up |
| 2 | 167ms | Ombros comecam a descer. Olhos voltam a semicerrar normal. Boca volta ao sorriso bobo. | Settling |
| 3 | 167ms | Volta ao normal. Uma fumaca extra sai das orelhas (como suspiro). | Reset + suspiro smoke |

**Play once**, depois retorna a A01 (Idle).

---

### A06 — PODCAST INTRO (Mini-desafio)
**Contexto**: Monark oferece "participar do podcast" como condicao para reviver. Esta e a intro do mini-desafio.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 125ms | Mao alcanca o microfone. Expressao fica "seria" por um instante (sobrancelhas descem, boca fecha). | Mao ao mic, serio |
| 1 | 125ms | Ajusta microfone (puxa 2px mais perto). Limpa garganta (corpo treme 1px vertical). | Mic adjust, tremor |
| 2 | 125ms | Olha pro "lado" (cabeca vira 1px, como verificando se ta gravando). LED de ON AIR ACENDE com brilho (antes era dim). | Head turn, LED bright |
| 3 | 125ms | Volta a olhar pra frente. LED agora em full brightness. | Reset head |
| 4 | 125ms | Faz gesto de "3" com a mao (contagem regressiva). Expressao voltando a chapada. | Countdown 3 |
| 5 | 125ms | Gesto de "2". Sorriso bobo voltando. | Countdown 2 |
| 6 | 125ms | Gesto de "1". Sorriso total de volta. Fumaca intensifica. | Countdown 1 |
| 7 | 125ms | Aponta pro jogador (dedo estirado). Boca aberta tipo "E AI MANO!". Fumaca explode. | Point + shout |

**Play once**, depois transiciona para A02 (Talking) durante o mini-desafio.

---

### A07 — SMOKE LOOP (Overlay Independente)
**Contexto**: Fumaca saindo das orelhas. Roda SEMPRE, independente do state do personagem. E um overlay separado posicionado sobre a cabeca.

| Frame | Duracao | Descricao |
|---|---|---|
| 0 | 167ms | 2 wisps de fumaca: esquerdo sobe 2px, direito sobe 1px. Formato organico A. |
| 1 | 167ms | Esquerdo sobe +2px e se expande 1px lateral. Direito sobe +2px. Formato B. |
| 2 | 167ms | Esquerdo no topo, comeca a dissipar (alpha diminui). Direito subindo. Formato C. |
| 3 | 167ms | Esquerdo quase invisivel. Direito no topo, expandindo. Novo wisp esquerdo comeca. Formato D. |
| 4 | 167ms | Novo esquerdo subindo. Direito dissipando. Formato E. |
| 5 | 167ms | Ciclo quase completo. Ambos em transicao. Formato F. |

**Spritesheet**: `monark-smoke.png` — 6 frames de 32x32px (area acima da cabeca), posicionado como overlay.
**Alpha base**: 50%, com variacao por frame (40%-60%).
**Cor**: `#6A8A6A` principal, `#4A7C59` mais denso no centro do wisp.
**IMPORTANTE**: A fumaca deve parecer ORGANICA — nunca geometrica, nunca simetrica.

---

### A08 — CHAIR BOB (Tween, nao spritesheet)
**Contexto**: Cadeira flutuante sobe e desce infinitamente. Aplicado via tween do Phaser, nao via spritesheet.

```javascript
// Implementacao Phaser 3
this.tweens.add({
    targets: [monarkSprite, monarkSmoke, monarkOnAir],
    y: '+=2',         // Desce 2px
    duration: 2000,   // 2 segundos pra descer
    yoyo: true,       // Volta pra cima
    repeat: -1,       // Loop infinito
    ease: 'Sine.easeInOut'  // Movimento suave (excecao ao jerky — flutuacao e eterea)
});
```

**Nota**: Este e o UNICO movimento suave do personagem. A flutuacao da cadeira no void e eterea, contrastando com os movimentos jerky do corpo.

---

### A09 — ENTRANCE (Primeira Aparicao)
**Contexto**: Jogador morre pela primeira vez. Tela escurece. Monark MATERIALIZA no void. So toca uma vez por sessao (depois, ele ja esta la).

| Frame | Duracao | Descricao |
|---|---|---|
| 0 | 125ms | Tela preta. Apenas um ponto de luz verde `#3D6B3A` no centro. |
| 1 | 125ms | Ponto de luz se expande. Silhueta da cadeira comeca a aparecer (contorno `#D47820` apenas). |
| 2 | 125ms | Cadeira mais visivel. Silhueta de uma pessoa sentada comeca (contorno fino). |
| 3 | 125ms | Detalhes do corpo aparecem de baixo pra cima (cadeira → pernas → torso). Tudo ainda escuro, contornos apenas. |
| 4 | 125ms | Rosto aparece. Chapeu de pescador. Pupilas BRILHAM no escuro (2 pontos `#3D6B3A`). |
| 5 | 125ms | Luz de podcast ACENDE de repente (flash). Todo o personagem iluminado por um instante. |
| 6 | 125ms | Iluminacao volta ao normal (dim podcast light). Monark totalmente visivel agora. |
| 7 | 125ms | LED de ON AIR acende. |
| 8 | 125ms | Monark ajusta o chapeu com uma mao. |
| 9 | 125ms | Sorriso bobo aparece. Fumaca comeca a sair das orelhas. PRONTO — transiciona para A01 ou A02. |

**Play once** (primeira morte apenas). Depois, Monark ja esta na tela quando o jogador morre de novo.

---

### A10 — ON AIR BLINK (LED do Microfone)
**Contexto**: O LED vermelho de "ON AIR" no microfone pisca constantemente. Overlay minusculo mas importante para a atmosfera.

| Frame | Duracao | Descricao |
|---|---|---|
| 0 | 500ms | LED aceso: 1px `#CC3030` brilhante + 1px `#FF4040` glow ao redor |
| 1 | 500ms | LED apagado: 1px `#4A2020` escuro (nao totalmente preto, LED desligado) |

**Spritesheet**: `monark-onair.png` — 2 frames de 8x8px, posicionado sobre o microfone.
**Loop infinito**.

---

## 3. Maquina de Estados (State Machine)

```
                    ┌──────────────┐
                    │              │
     ┌──────────────┤  ENTRANCE    │ (A09, play once, primeira morte)
     │              │              │
     │              └──────┬───────┘
     │                     │
     │                     v
     │              ┌──────────────┐
     │              │              │◄──────────────────────┐
     │              │    IDLE      │ (A01 + A07 + A08 +    │
     │              │              │  A10, todos em loop)   │
     │              └──────┬───────┘                        │
     │                     │                                │
     │            Jogador interage                          │
     │                     │                                │
     │                     v                                │
     │              ┌──────────────┐                        │
     │              │              │                        │
     │              │   TALKING    │ (A02 + overlays)       │
     │              │              │                        │
     │              └──────┬───────┘                        │
     │                     │                                │
     │           Dialogo oferece opcao                      │
     │            /                 \                       │
     │           v                   v                     │
     │  ┌──────────────┐    ┌──────────────┐               │
     │  │              │    │              │               │
     │  │ OFFERING     │    │ PODCAST      │               │
     │  │ DEAL (A03)   │    │ INTRO (A06)  │               │
     │  │              │    │              │               │
     │  └──────┬───────┘    └──────┬───────┘               │
     │         │                   │                       │
     │    Aceita / Recusa     Mini-desafio                 │
     │    /           \            │                       │
     │   v             v           v                       │
     │ ┌─────────┐ ┌─────────┐  ┌─────────┐               │
     │ │ HAPPY   │ │ SHRUG   │  │TALKING  │               │
     │ │ (A04)   │ │ (A05)   │  │(A02)    │               │
     │ └────┬────┘ └────┬────┘  └────┬────┘               │
     │      │           │            │                     │
     │      └───────────┴────────────┴─────────────────────┘
     │                (todos retornam a IDLE)
     │
     │  OVERLAYS PERMANENTES (rodam SEMPRE, independente do state):
     │  - A07 (Smoke Loop)
     │  - A08 (Chair Bob)
     │  - A10 (ON AIR Blink)
     └───────────────────────────────────────────────────────
```

---

## 4. Transicoes Entre States

| De | Para | Transicao | Duracao |
|---|---|---|---|
| ENTRANCE → IDLE | Fade in completo | Imediata (ultimo frame de A09 = primeiro de A01) |
| IDLE → TALKING | Corte seco (jerky) | 0ms — troca instantanea (estilo choppy) |
| TALKING → OFFERING | Corte seco | 0ms |
| TALKING → PODCAST INTRO | Corte seco | 0ms |
| OFFERING → HAPPY | Corte seco | 0ms |
| OFFERING → SHRUG | Corte seco | 0ms |
| HAPPY → IDLE | Ultimo frame de A04 → primeiro frame de A01 | 100ms fade |
| SHRUG → IDLE | Ultimo frame de A05 → primeiro frame de A01 | 100ms fade |
| PODCAST INTRO → TALKING | Ultimo frame de A06 → primeiro frame de A02 | 0ms |

**REGRA**: Transicoes sao CORTES SECOS (jerky, choppy). Nenhum blend suave entre animacoes. A UNICA excecao e o retorno de reacao (Happy/Shrug) para Idle, que tem um micro-fade de 100ms.

---

## 5. Implementacao Phaser 3

### Configuracao de Animacoes
```javascript
// Em GameOverScene.create()

// Carregar spritesheets
this.load.spritesheet('monark-idle', 'assets/personagens/monark/sprites/monark-idle.png', 
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('monark-talking', 'assets/personagens/monark/sprites/monark-talking.png', 
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('monark-deal', 'assets/personagens/monark/sprites/monark-deal.png', 
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('monark-happy', 'assets/personagens/monark/sprites/monark-happy.png', 
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('monark-shrug', 'assets/personagens/monark/sprites/monark-shrug.png', 
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('monark-podcast-intro', 'assets/personagens/monark/sprites/monark-podcast-intro.png', 
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('monark-entrance', 'assets/personagens/monark/sprites/monark-entrance.png', 
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('monark-smoke', 'assets/personagens/monark/sprites/monark-smoke.png', 
    { frameWidth: 32, frameHeight: 32 });
this.load.spritesheet('monark-onair', 'assets/personagens/monark/sprites/monark-onair.png', 
    { frameWidth: 8, frameHeight: 8 });

// Registrar animacoes
this.anims.create({
    key: 'monark-idle',
    frames: this.anims.generateFrameNumbers('monark-idle', { start: 0, end: 3 }),
    frameRate: 4,
    repeat: -1
});

this.anims.create({
    key: 'monark-talking',
    frames: this.anims.generateFrameNumbers('monark-talking', { start: 0, end: 5 }),
    frameRate: 8,
    repeat: -1
});

this.anims.create({
    key: 'monark-deal',
    frames: this.anims.generateFrameNumbers('monark-deal', { start: 0, end: 3 }),
    frameRate: 6,
    repeat: -1
});

this.anims.create({
    key: 'monark-happy',
    frames: this.anims.generateFrameNumbers('monark-happy', { start: 0, end: 5 }),
    frameRate: 10,
    repeat: 0  // play once
});

this.anims.create({
    key: 'monark-shrug',
    frames: this.anims.generateFrameNumbers('monark-shrug', { start: 0, end: 3 }),
    frameRate: 6,
    repeat: 0  // play once
});

this.anims.create({
    key: 'monark-podcast-intro',
    frames: this.anims.generateFrameNumbers('monark-podcast-intro', { start: 0, end: 7 }),
    frameRate: 8,
    repeat: 0  // play once
});

this.anims.create({
    key: 'monark-entrance',
    frames: this.anims.generateFrameNumbers('monark-entrance', { start: 0, end: 9 }),
    frameRate: 8,
    repeat: 0  // play once
});

this.anims.create({
    key: 'monark-smoke',
    frames: this.anims.generateFrameNumbers('monark-smoke', { start: 0, end: 5 }),
    frameRate: 6,
    repeat: -1
});

this.anims.create({
    key: 'monark-onair',
    frames: this.anims.generateFrameNumbers('monark-onair', { start: 0, end: 1 }),
    frameRate: 1,
    repeat: -1
});
```

### Logica de Troca de State
```javascript
// Exemplo de troca de animacao
monarkSprite.on('animationcomplete', (anim) => {
    if (anim.key === 'monark-happy' || anim.key === 'monark-shrug') {
        monarkSprite.play('monark-idle');
    }
    if (anim.key === 'monark-podcast-intro') {
        monarkSprite.play('monark-talking');
    }
    if (anim.key === 'monark-entrance') {
        monarkSprite.play('monark-idle');
    }
});
```

---

## 6. Efeitos Visuais Adicionais (Nao-Spritesheet)

### Screen Shake no HAPPY
Quando Monark fica feliz (jogador aceita deal), leve screen shake:
```javascript
this.cameras.main.shake(200, 0.005); // 200ms, intensidade 0.005
```

### Flash Verde no PODCAST INTRO
Quando LED de ON AIR acende com forca (frame 2 de A06):
```javascript
this.cameras.main.flash(100, 61, 107, 58, true); // Flash verde rapido (#3D6B3A)
```

### Particulas de Fumaca Extra no HAPPY
Rajada de particulas de fumaca ao redor da cabeca:
```javascript
smokeEmitter.explode(8); // 8 particulas extras de uma vez
```

---

## 7. Timing de Dialogo vs Animacao

### Bordoes e Sincronizacao
Os bordoes do Monark aparecem em caixas de texto. A animacao de TALKING NAO sincroniza com o texto — ela roda no ritmo dela enquanto o texto avanca letra por letra (typewriter).

| Bordao | Animacao During | Duracao Texto | Nota |
|---|---|---|---|
| "E ai mano, bem-vindo ao Limbo..." | A02 (Talking) | 3s typewriter | Primeira fala, sempre |
| "Quer um baseado... digo, segunda chance?" | A02 → A03 (Deal) | 2.5s → menu abre | Transiciona pra loja |
| "Mano, pensa comigo..." | A02 (Talking) | 1.5s | Intro de filosofia |
| "Aqui no Limbo todo mundo e igual." | A02 (Talking) | 2s | Fala generica |
| "Voce foi cancelado por que? Ah, morreu?" | A02 (Talking) | 2.5s | Meta-humor |
| "A liberdade de expressao deveria valer ate no inferno." | A02 (Talking) | 3s | Fala longa |

---

## 8. Checklist de Producao de Animacao

- [ ] Desenhar frame 0 de A01 (sprite base referencia)
- [ ] Validar proporcoes e silhueta do frame 0
- [ ] Completar todos os 4 frames de A01 (Idle)
- [ ] Testar loop de A01 a 4fps — deve parecer "vivo mas chapado"
- [ ] Completar 6 frames de A02 (Talking)
- [ ] Testar ciclo de boca em A02 — deve ser energetico mas descoordenado
- [ ] Completar 4 frames de A03 (Offering)
- [ ] Completar 6 frames de A04 (Happy) — CHAPEU DEVE VOAR
- [ ] Completar 4 frames de A05 (Shrug)
- [ ] Completar 8 frames de A06 (Podcast Intro)
- [ ] Criar overlay de fumaca A07 (6 frames, 32x32)
- [ ] Criar overlay ON AIR A10 (2 frames, 8x8)
- [ ] Criar animacao de entrada A09 (10 frames)
- [ ] Montar spritesheets horizontais
- [ ] Implementar state machine no Phaser 3
- [ ] Configurar tween de Chair Bob (A08)
- [ ] Testar todas as transicoes entre states
- [ ] Testar overlays (smoke + onair + bob) rodando simultaneamente
- [ ] Verificar performance com todos os efeitos ativos
- [ ] Aplicar textura de papel overlay em todos os frames finais
