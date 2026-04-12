# Animation Spec — ARTHUR DO VAL / MAMAE FALEI (Co-Apresentador do Limbo)

> NPC co-apresentador do Limbo. Todas as animacoes sentado, COMPLEMENTANDO o Monark.
> Framerate geral: 6-12fps (MAIS RAPIDO que Monark — ele e nervoso, frenetico).
> Sprites 64x64px. Spritesheets horizontais.
> Engine: Phaser 3.

---

## 1. Tabela Geral de Animacoes

| ID | Nome | Frames | FPS | Loop | Trigger | Spritesheet |
|---|---|---|---|---|---|---|
| A01 | Idle (Inquieto) | 6 | 6 | Sim | Default (nenhuma interacao) | `arthur-idle.png` |
| A02 | Ranting (Reclamando) | 8 | 10 | Sim | Durante dialogo dele | `arthur-ranting.png` |
| A03 | Tirado de Contexto | 6 | 8 | Nao (play once) | Reacao defensiva | `arthur-context.png` |
| A04 | Whispering (Dicas) | 6 | 8 | Sim | Skill "Denuncia do Limbo" | `arthur-whispering.png` |
| A05 | Interrupting | 4 | 12 | Nao (play once) | Ele corta o Monark | `arthur-interrupt.png` |
| A06 | Defeated | 4 | 4 | Nao (play once) | Momento raro de silencio | `arthur-defeated.png` |
| A07 | Phone Glow Loop | 3 | 2 | Sim | SEMPRE (overlay tela celular) | `arthur-phone.png` |
| A08 | Chair Wobble | N/A | N/A | Sim | SEMPRE (tween) | N/A (tween) |
| A09 | Mouth Tremble | 4 | 8 | Sim | SEMPRE durante idle (overlay) | `arthur-mouth.png` |
| A10 | Hair Twitch | 2 | 3 | Sim | SEMPRE (overlay) | `arthur-hair.png` |

---

## 2. Detalhamento Frame-a-Frame

### A01 — IDLE (Inquieto na Cadeira)
**Contexto**: Estado default. Arthur nao consegue ficar parado. Mesmo sem falar, o corpo se mexe, a boca murmura, as maos nao param. OPOSTO do idle calmo do Monark.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 167ms | Sentado com peso na direita. Mao esquerda na coxa, mao direita proxima a cabeca (quase coçando). Boca semi-aberta murmurando. Olhos arregalados olhando pra frente. | BASE |
| 1 | 167ms | Peso transfere pra esquerda (corpo inclina 1px). Mao direita SOBE pra cabeca (coçando). Boca fecha 1px. Olhos olham pra esquerda (checando Monark). | Lean -1px, mao head, olhos left |
| 2 | 167ms | Peso volta ao centro. Mao direita desce (desistiu de cocar). Boca abre novamente. Mao esquerda sobe da coxa pro braco da cadeira. Olhos voltam ao centro. | Reset parcial, mao swap |
| 3 | 167ms | Inclina pra FRENTE 2px (ansioso). Ambas maos nos bracos da cadeira apertando. Boca abre mais (prestes a falar). Ombros sobem 1px (tensao). | Lean forward, grip, boca open |
| 4 | 167ms | Volta a posicao neutra. Ombros descem. Boca fecha parcialmente. Mao esquerda vai pra coxa de novo. Olhos olham pra CIMA (tipo "meu Deus"). | Reset, olhos up |
| 5 | 167ms | Quase identico ao frame 0 MAS mao direita em posicao diferente (no joelho em vez de perto da cabeca). Cadeira inclina 1px pro lado. | Loop point ligeiramente off |

**Loop**: 0 → 1 → 2 → 3 → 4 → 5 → 0
**IMPORTANTE**: O idle do Arthur tem 6 frames vs 4 do Monark, e roda a 6fps vs 4fps. Isso cria uma diferenca de "energia" visivel — Arthur esta SEMPRE mais agitado, mesmo parado.

---

### A02 — RANTING (Reclamando)
**Contexto**: Dialogo do Arthur ativo. Ele reclama, gesticula, se indigna. E a versao MAXIMA da energia dele.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 100ms | Inclina pra frente 3px. Boca ABRE no maximo (8x4px, dentes e lingua visivel). Mao direita SOBE apontando pra cima (dedo acusatorio). Sobrancelhas no pico. | FULL LEAN, boca MAX, mao UP |
| 1 | 100ms | Mao direita no ponto mais alto. Mao esquerda BATE na coxa (impacto — coxa deforma 1px). Boca fecha parcial (respirando). Corpo treme 1px vertical. | Mao peak, slap coxa, tremor |
| 2 | 100ms | Mao direita DESCE apontando pro lado (acusando alguem invisivel). Boca ABRE de novo. Mao esquerda sobe (gesticulacao dupla). Cadeira balanca 2px. | Mao redirect, boca open, cadeira tilt |
| 3 | 100ms | Ambas maos pro ALTO (exasperacao total). Boca FECHADA brevemente (engoliu ar). Olhos MAIS arregalados (sobrancelhas mais altas). Cabelo treme. | Bracos up, boca close, olhos MAX |
| 4 | 100ms | Boca ABRE enorme de novo. Mao direita desce batendo no braco da cadeira. Mao esquerda aponta pro Monark (esquerda). Corpo inclina pra esquerda. | Boca open, direcional, lean left |
| 5 | 100ms | Mao esquerda volta. Mao direita gesticula rodando (circulo). Boca semi. Corpo volta ao centro. Respiro momentaneo. | Transition |
| 6 | 100ms | Volta a inclinar pra frente. Boca abre. Mao direita bate na PROPRIA testa (frustacao). Cadeira balanca pro outro lado. | Facepalm, cadeira swing |
| 7 | 100ms | Transicao de volta. Mao desce da testa. Boca semi-aberta. Postura quase neutra mas tensa. Pronto pra loop. | Reset tenso |

**Loop**: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 0
**Nota**: 8 frames a 10fps = loop de 0.8 segundos. MUITO mais rapido que qualquer animacao do Monark. A ideia e que Arthur parece em "fast forward" comparado ao Monark em "slow motion".

---

### A03 — TIRADO DE CONTEXTO (Reacao Defensiva)
**Contexto**: Monark diz algo, ou o jogador confronta Arthur, e ele entra em modo defesa. "EU FUI TIRADO DE CONTEXTO!"

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 125ms | JOGA corpo pra tras na cadeira (recuo 3px). Olhos MAXIMO arregalamento. Boca forma O perfeito. Maos comecam a subir. | Recoil 3px, shock face |
| 1 | 125ms | Maos a frente, palmas ABERTAS (gesto de PARA/STOP). Cadeira inclina pra tras 2px (perigosamente). Celular brilha VERMELHO (em vez de azul). | Palms up, cadeira tilt, phone RED |
| 2 | 125ms | Posicao mantida. Dedos TREMEM (maos tremem 1px). Boca muda de O para grito aberto (retangulo). Gotas de suor (2 pixels brancos) saem da testa. | Tremor, suor, boca muda |
| 3 | 125ms | Comeca a voltar pra frente. Maos descem levemente. Boca fecha parcial. Olhos ainda arregalados mas descendo. Celular volta a azul. | Settling parcial |
| 4 | 125ms | Quase voltou a posicao. Uma mao vai ao peito (gesto de "EU? EU??"). Boca abre pro lado (expressao de indignacao). | Mao peito, boca assimetrica |
| 5 | 125ms | Retorna a posicao de idle (mas tenso). Expressao de "isso e um absurdo" congelada. Cadeira para de balançar. | Reset tenso |

**Play once**, depois retorna a A01 (Idle) ou A02 (Ranting) dependendo do contexto.

---

### A04 — WHISPERING (Dicas — "Denuncia do Limbo")
**Contexto**: Arthur oferece "informacoes exclusivas" sobre o proximo nivel. Mistura dicas reais com reclamacoes inuteis.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 125ms | Inclina pro LADO direito (pra perto do jogador/camera). Mao esquerda ao lado da boca (gesto de sussurro). Olhos olham pra esquerda (checando se Monark ta ouvindo). | Lean right, hand mouth, eyes left |
| 1 | 125ms | Boca move atras da mao (sussurrando). Olhos voltam pra frente (pro jogador). Sobrancelha esquerda ergue (conspiratorio). | Boca move, eyes front, eyebrow |
| 2 | 125ms | Mao direita pega "documentos invisiveis" (mao se fecha como segurando papeis). Olhos olham pra esquerda de novo (paranoia). Celular brilha VERMELHO (info quente). | Mao grab, eyes left, phone RED |
| 3 | 125ms | Mostra "documentos" pro jogador (mao direita estende). Boca abre mais (falando mais alto — esqueceu que era segredo). Celular volta a azul. | Mao extend, boca louder |
| 4 | 125ms | Percebe que falou alto. Mao esquerda volta a boca. Olhos arregalados (ops). Corpo encolhe 1px. | Panic cover, shrink |
| 5 | 125ms | Volta a sussurrar. Postura de sussurro restaurada. Sobrancelha ergue de novo. Loop point. | Reset conspirator |

**Loop**: 0 → 1 → 2 → 3 → 4 → 5 → 0
**Efeito gameplay**: Enquanto essa animacao roda, o texto mostra dicas REAIS misturadas com reclamacoes do Arthur. A animacao de "ops falei alto" (frame 4) coincide com as dicas piores/erradas.

---

### A05 — INTERRUPTING (Cortando o Monark)
**Contexto**: Monark esta falando e Arthur simplesmente CORTA. Acontece aleatoriamente durante dialogos do Monark.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 83ms | PULA na cadeira (sobe 3px inteiro). Cadeira BALANCA violentamente. Mao direita dispara na direcao do Monark (esquerda). | Jump 3px, mao shoot left |
| 1 | 83ms | No ar. Boca ABERTA MAXIMA. Mao alcancou a direcao do Monark. Cabelo todo pra cima (inércia do pulo). Olhos faiscando. | Air, boca MAX, hair up |
| 2 | 83ms | Descendo. Mao volta. Boca comeca a falar (retangulo). Cadeira voltando. Cabelo descendo. | Landing, talking starts |
| 3 | 83ms | Pousa. Cadeira ainda tremendo. Boca em posicao de fala. Mao volta ao corpo. TRANSICAO DIRETA pra A02 (Ranting). | Landed, transition ready |

**Play once**, depois transiciona DIRETAMENTE para A02 (Ranting) — ele interrompe PRA RECLAMAR.
**FPS 12**: O mais rapido de todas as animacoes. A interrupcao e SUBITA, sem aviso.

---

### A06 — DEFEATED (Momento Raro de Silencio)
**Contexto**: Acontece RARAMENTE. Arthur aceita por um breve momento que foi cancelado com razao. Dura pouco.

| Frame | Duracao | Descricao | Delta vs Frame Anterior |
|---|---|---|---|
| 0 | 250ms | Ombros CAEM 3px. Cabeca comeca a descer. Olhos perdem o arregalamento (ficam normais). Boca comeca a fechar. | Deflate starts |
| 1 | 250ms | Cabeca ABAIXA (queixo no peito). Maos nos joelhos. Boca FECHADA (primeira e unica vez). Celular na orelha APAGA (tela escura). | Full deflate, phone off |
| 2 | 250ms | Mao passa pelo cabelo (gesto de desespero). Cabelo amassa sob a mao. Olhar no chao. Respiro profundo (ombros sobem 1px e descem). | Hand through hair, sigh |
| 3 | 250ms | Comeca a erguer a cabeca. Olhos começam a arregalar de novo. Boca comeca a abrir. Celular REACENDE. A "derrota" acabou — volta ao normal. | Recovery starts |

**Play once**, depois retorna a A01 (Idle).
**FPS 4**: O MAIS LENTO de todas as animacoes do Arthur. Contraste brutal com sua energia normal. Esse e o unico momento em que ele se parece com o Monark em ritmo.

---

### A07 — PHONE GLOW LOOP (Overlay Celular)
**Contexto**: A tela do celular grudado na orelha pulsa e muda de cor. Roda SEMPRE como overlay.

| Frame | Duracao | Descricao |
|---|---|---|
| 0 | 500ms | Tela azul `#4A9ACA` brilho normal. Ilumina lado direito do rosto levemente. |
| 1 | 500ms | Tela azul `#4A9ACA` brilho aumenta (alpha +10%). Leve pulsacao. |
| 2 | 500ms | Tela azul brilho diminui (alpha -10%). Voltando ao normal. |

**Spritesheet**: `arthur-phone.png` — 3 frames de 8x8px, posicionado sobre a orelha direita.
**Loop infinito**.

**VARIACAO CONTEXTUAL**: Durante A03 (Tirado de Contexto) e A04 (Whispering), a cor muda para VERMELHO `#CC3030`. Isso e feito via tint no Phaser, nao spritesheet separado.

---

### A08 — CHAIR WOBBLE (Tween — Cadeira Instavel)
**Contexto**: A cadeira do Arthur nao flutua suavemente como a do Monark. Ela BALANCA, TREMULA, parece prestes a tombar.

```javascript
// Implementacao Phaser 3 — Cadeira instavel

// Bob vertical (igual Monark mas com mais variacao)
this.tweens.add({
    targets: [arthurSprite, arthurPhoneOverlay, arthurHairOverlay],
    y: '+=3',          // Desce 3px (mais que Monark — instavel)
    duration: 1500,    // 1.5s (mais rapido que Monark — ansiedade)
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});

// Wobble lateral (EXCLUSIVO do Arthur — Monark nao tem)
this.tweens.add({
    targets: [arthurSprite, arthurPhoneOverlay, arthurHairOverlay],
    x: '+=1',          // Desloca 1px pro lado
    duration: 800,     // Rapido
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});

// Micro-rotacao (cadeira quase tombando)
this.tweens.add({
    targets: arthurSprite,
    angle: { from: -1, to: 1 },  // 1 grau de rotacao
    duration: 2000,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

**Nota**: A cadeira do Arthur tem TRES tweens vs UM do Monark. Isso cria uma flutuacao CAÓTICA vs SERENA. Hierarquia visual atraves do movimento.

---

### A09 — MOUTH TREMBLE (Overlay Boca)
**Contexto**: Mesmo no idle, a boca do Arthur treme. Murmura sem parar. Overlay que roda sobre a boca no idle.

| Frame | Duracao | Descricao |
|---|---|---|
| 0 | 125ms | Boca semi-aberta, posicao A (labio inferior 1px a esquerda) |
| 1 | 125ms | Boca semi-aberta, posicao B (labio inferior centro) |
| 2 | 125ms | Boca semi-aberta, posicao C (labio inferior 1px a direita) |
| 3 | 125ms | Boca semi-aberta, posicao D (labio inferior 1px abaixo — quase abrindo) |

**Spritesheet**: `arthur-mouth.png` — 4 frames de 10x6px, posicionado sobre a area da boca.
**Loop infinito durante A01 (Idle) apenas**. Durante outros states, a boca e parte do sprite principal.

---

### A10 — HAIR TWITCH (Overlay Cabelo)
**Contexto**: Uma mecha especifica do cabelo tem vida propria. Twitcha independentemente.

| Frame | Duracao | Descricao |
|---|---|---|
| 0 | 333ms | Mecha central apontando pra cima-esquerda |
| 1 | 333ms | Mecha central move pra cima-direita (1px lateral) |

**Spritesheet**: `arthur-hair.png` — 2 frames de 16x8px, posicionado sobre o topo da cabeca.
**Loop infinito**.

---

## 3. Maquina de Estados (State Machine)

```
                 ┌──────────────┐
                 │              │
                 │    IDLE      │ (A01 + A07 + A08 + A09 + A10)
                 │  (inquieto)  │◄──────────────────────────┐
                 │              │                            │
                 └──────┬───────┘                            │
                        │                                    │
              Monark fala / jogador interage                 │
                /                  \                         │
               v                    v                        │
     ┌──────────────┐      ┌──────────────┐                  │
     │              │      │              │                  │
     │   RANTING    │      │ WHISPERING   │                  │
     │   (A02)      │      │ (A04-dicas)  │                  │
     │              │      │              │                  │
     └──────┬───────┘      └──────┬───────┘                  │
            │                     │                          │
            │              Dicas acabaram                    │
            │                     │                          │
            │                     └──────────────────────────┤
            │                                                │
     Algo o incomoda / defende-se / aceita                   │
     /              |              \                         │
    v               v               v                       │
┌─────────┐  ┌──────────┐  ┌──────────┐                     │
│INTERRUPT │  │ TIRADO   │  │DEFEATED  │                     │
│(A05)     │  │CONTEXTO  │  │(A06)     │                     │
│          │  │(A03)     │  │          │                     │
└────┬─────┘  └────┬─────┘  └────┬─────┘                     │
     │             │              │                          │
     v             │              │                          │
  RANTING          │              │                          │
  (A02)            └──────────────┴──────────────────────────┘
                     (retornam a IDLE)
                    
  OVERLAYS PERMANENTES (rodam SEMPRE):
  - A07 (Phone Glow)
  - A08 (Chair Wobble — 3 tweens)
  - A09 (Mouth Tremble — durante idle)
  - A10 (Hair Twitch)
```

---

## 4. Transicoes Entre States

| De | Para | Transicao | Duracao |
|---|---|---|---|
| IDLE → RANTING | Corte seco (MUITO jerky) | 0ms |
| IDLE → WHISPERING | Corte seco | 0ms |
| RANTING → TIRADO DE CONTEXTO | Corte seco (reacao subita) | 0ms |
| RANTING → INTERRUPT | Corte seco (explosao) | 0ms |
| INTERRUPT → RANTING | Direto (ultimo frame A05 → primeiro A02) | 0ms |
| TIRADO DE CONTEXTO → IDLE | Ultimo frame → fade 100ms → idle | 100ms |
| WHISPERING → IDLE | Corte seco | 0ms |
| DEFEATED → IDLE | Slow fade (contraste dramatico) | 300ms |
| Qualquer → DEFEATED | Fade to (unica transicao nao-jerky) | 200ms |

**REGRA**: TODAS as transicoes sao corte seco EXCETO transicoes envolvendo DEFEATED — porque esse e o unico momento "calmo" e merece tratamento diferente.

---

## 5. Sincronizacao com Monark

### Interacoes Duplas (Animacoes que Reagem ao Monark)

| Monark Faz | Arthur Reage | Timing |
|---|---|---|
| A01 (Idle) | A01 (Idle, mas inquieto) | Simultaneo |
| A02 (Talking) | A01 (Idle) ou A05 (Interrupt) aleatoriamente | 70% idle, 30% interrupt |
| A03 (Offering Deal) | A02 (Ranting — reclamando do preco) | Imediato |
| A04 (Happy) | A03 (Tirado de Contexto — "EU tambem contribui!") | 200ms delay |
| A05 (Shrug) | A02 (Ranting — "como assim 'tanto faz'??") | 100ms delay |
| A06 (Podcast Intro) | A01 → A05 (Interrupt) → A02 (Ranting) | Sequencia rapida |

### Codigo de Sincronizacao
```javascript
// Quando Monark muda de state, Arthur reage
monarkSprite.on('animationcomplete', (anim) => {
    if (anim.key === 'monark-talking') {
        // 30% chance de Arthur interromper
        if (Math.random() < 0.3) {
            arthurSprite.play('arthur-interrupt');
        }
    }
    if (anim.key === 'monark-happy') {
        // Arthur reage indignado 200ms depois
        this.time.delayedCall(200, () => {
            arthurSprite.play('arthur-context');
        });
    }
});
```

---

## 6. Implementacao Phaser 3

### Configuracao de Animacoes
```javascript
// Em GameOverScene.create()

// Carregar spritesheets
this.load.spritesheet('arthur-idle', 'assets/personagens/arthur-do-val/sprites/arthur-idle.png',
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('arthur-ranting', 'assets/personagens/arthur-do-val/sprites/arthur-ranting.png',
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('arthur-context', 'assets/personagens/arthur-do-val/sprites/arthur-context.png',
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('arthur-whispering', 'assets/personagens/arthur-do-val/sprites/arthur-whispering.png',
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('arthur-interrupt', 'assets/personagens/arthur-do-val/sprites/arthur-interrupt.png',
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('arthur-defeated', 'assets/personagens/arthur-do-val/sprites/arthur-defeated.png',
    { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('arthur-phone', 'assets/personagens/arthur-do-val/sprites/arthur-phone.png',
    { frameWidth: 8, frameHeight: 8 });
this.load.spritesheet('arthur-mouth', 'assets/personagens/arthur-do-val/sprites/arthur-mouth.png',
    { frameWidth: 10, frameHeight: 6 });
this.load.spritesheet('arthur-hair', 'assets/personagens/arthur-do-val/sprites/arthur-hair.png',
    { frameWidth: 16, frameHeight: 8 });

// Registrar animacoes
this.anims.create({
    key: 'arthur-idle',
    frames: this.anims.generateFrameNumbers('arthur-idle', { start: 0, end: 5 }),
    frameRate: 6,
    repeat: -1
});

this.anims.create({
    key: 'arthur-ranting',
    frames: this.anims.generateFrameNumbers('arthur-ranting', { start: 0, end: 7 }),
    frameRate: 10,
    repeat: -1
});

this.anims.create({
    key: 'arthur-context',
    frames: this.anims.generateFrameNumbers('arthur-context', { start: 0, end: 5 }),
    frameRate: 8,
    repeat: 0
});

this.anims.create({
    key: 'arthur-whispering',
    frames: this.anims.generateFrameNumbers('arthur-whispering', { start: 0, end: 5 }),
    frameRate: 8,
    repeat: -1
});

this.anims.create({
    key: 'arthur-interrupt',
    frames: this.anims.generateFrameNumbers('arthur-interrupt', { start: 0, end: 3 }),
    frameRate: 12,
    repeat: 0
});

this.anims.create({
    key: 'arthur-defeated',
    frames: this.anims.generateFrameNumbers('arthur-defeated', { start: 0, end: 3 }),
    frameRate: 4,
    repeat: 0
});

this.anims.create({
    key: 'arthur-phone',
    frames: this.anims.generateFrameNumbers('arthur-phone', { start: 0, end: 2 }),
    frameRate: 2,
    repeat: -1
});

this.anims.create({
    key: 'arthur-mouth',
    frames: this.anims.generateFrameNumbers('arthur-mouth', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1
});

this.anims.create({
    key: 'arthur-hair',
    frames: this.anims.generateFrameNumbers('arthur-hair', { start: 0, end: 1 }),
    frameRate: 3,
    repeat: -1
});
```

---

## 7. Efeitos Visuais Adicionais

### Screen Shake na INTERRUPCAO
Quando Arthur pula na cadeira (A05):
```javascript
this.cameras.main.shake(150, 0.003); // Menor que o happy do Monark
```

### Flash Azul do Celular no "TIRADO DE CONTEXTO"
Celular muda pra vermelho — flash sutil:
```javascript
arthurPhoneOverlay.setTint(0xCC3030); // Tint vermelho
this.time.delayedCall(750, () => {
    arthurPhoneOverlay.clearTint(); // Volta ao normal
});
```

### Gotas de Suor no "TIRADO DE CONTEXTO"
Particulas de suor (2-3 pixels brancos subindo da testa):
```javascript
const sweatEmitter = this.add.particles(arthurSprite.x, arthurSprite.y - 20, 'sweat-drop', {
    speed: { min: 10, max: 30 },
    angle: { min: -120, max: -60 },
    lifespan: 500,
    scale: 0.5,
    maxParticles: 3,
    tint: 0xE8E0D0
});
sweatEmitter.explode(3);
```

---

## 8. Comparacao de Timing: Arthur vs Monark

| Aspecto | Monark | Arthur | Ratio |
|---|---|---|---|
| Idle frames | 4 | 6 | 1:1.5 |
| Idle FPS | 4 | 6 | 1:1.5 |
| Talking frames | 6 | 8 | 1:1.33 |
| Talking FPS | 8 | 10 | 1:1.25 |
| Fastest anim FPS | 10 (Happy) | 12 (Interrupt) | 1:1.2 |
| Slowest anim FPS | 1 (ON AIR) | 4 (Defeated) | — |
| Chair bob duration | 2000ms | 1500ms | 1.33:1 |
| Chair bob amplitude | 2px | 3px | 1:1.5 |
| Lateral wobble | Nenhum | 1px | 0:1 |
| Overlays permanentes | 3 (smoke, bob, onair) | 4 (phone, wobble, mouth, hair) | 1:1.33 |

**Conclusao**: Arthur e consistentemente 25-50% mais rapido/agitado que Monark em TUDO. Isso e a piada visual — um e zen, o outro e caos.

---

## 9. Checklist de Producao

- [ ] Desenhar frame 0 de A01 (sprite base referencia)
- [ ] Validar proporcoes, deformidades (boca + celular) e POSICAO RELATIVA ao Monark
- [ ] Completar 6 frames de A01 (Idle)
- [ ] Testar loop de A01 a 6fps — deve parecer INQUIETO
- [ ] Completar 8 frames de A02 (Ranting)
- [ ] Testar ciclo de A02 — deve parecer FRENETICO
- [ ] Completar 6 frames de A03 (Tirado de Contexto) — REAÇÃO DRAMATICA
- [ ] Completar 6 frames de A04 (Whispering)
- [ ] Completar 4 frames de A05 (Interrupt) — PULO na cadeira
- [ ] Completar 4 frames de A06 (Defeated) — unico momento calmo
- [ ] Criar overlay Phone Glow A07 (3 frames, 8x8)
- [ ] Criar overlay Mouth Tremble A09 (4 frames, 10x6)
- [ ] Criar overlay Hair Twitch A10 (2 frames, 16x8)
- [ ] Montar spritesheets horizontais
- [ ] Implementar state machine no Phaser 3
- [ ] Configurar tweens de Chair Wobble (A08 — 3 tweens!)
- [ ] Implementar sincronizacao com Monark
- [ ] Testar todas as transicoes
- [ ] Testar overlays simultaneos (phone + wobble + mouth + hair)
- [ ] Testar DUPLA funcionando junto (Monark + Arthur na mesma cena)
- [ ] Verificar performance com ambos personagens + todos efeitos
- [ ] Aplicar textura de papel em todos os frames finais
