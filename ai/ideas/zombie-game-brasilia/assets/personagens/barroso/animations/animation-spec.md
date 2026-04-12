# BARROSO — Animation Specification

## Boss STF — "O Professor no Ringue"

---

## Overview Geral

| Parametro                | Valor                                           |
|--------------------------|--------------------------------------------------|
| **Engine**               | Phaser 3                                         |
| **Sprite Size**          | 64x64px                                          |
| **Frame Rate Base**      | 8-12 fps (estilo jerky Andre Guedes)             |
| **Estilo de Animacao**   | Twitchy, jerky, deformacao organica. NAO suave.   |
| **Easing Padrao**        | Phaser.Math.Easing.Stepped (sem interpolacao suave)|
| **Personagem Anchor**    | Bottom-center (32, 60)                           |
| **Y-Sorting**            | Ativado (top-down isometrico)                    |
| **Total de Animacoes**   | 8 + 3 VFX + 1 UI                                |

---

## Sistema de Estado Emocional: BAROMETRO DE COMPOSTURA

Barroso tem um sistema UNICO de estado visual que afeta TODAS as animacoes. O estado emocional e controlado por tres variaveis visuais que mudam CONTINUAMENTE durante o gameplay:

### Veia da Testa (barometro principal)
```javascript
// Estado da veia — afeta rendering em todos os frames
veinState: {
    width: 1,          // 1px (calmo) a 6px (maximo)
    color: '#8B2252',  // normal -> '#CC1144' (inflamada) -> '#FF0000' (explodindo)
    pulseRate: 1.0,    // batimentos por segundo (1 = normal, 4 = furioso)
    branches: 0        // 0 (calmo) a 4 (ramificacoes visiveis)
}
```

### Oculos (indicador de raiva)
```javascript
glassesState: {
    fog: 0.0,          // 0.0 (transparente) a 1.0 (completamente opaco)
    lensColor: '#E8E8F0', // normal -> '#D4D4E0' (meio) -> '#C0C0D0' (opaco)
    position: 'normal',  // 'normal', 'slipping', 'fallen', 'crooked'
}
```

### Suor (indicador de stress acumulado)
```javascript
sweatState: {
    drops: 0,           // 0 (seco) a 8+ (encharcado)
    visibility: 'hidden', // 'hidden' (sob toga), 'peeking' (quase visivel), 'visible' (exposto)
    locations: []       // ['nuca', 'tempera', 'testa', 'queixo', 'costas', 'axilas']
}
```

### Regras de Transicao de Estado
```
CALMO (idle padrao):
  veia: 1px, #8B2252, pulse 1.0
  oculos: fog 0.0, normal
  suor: 0-2 drops, hidden

IRRITADO (apos receber hits):
  veia: 2-3px, #9B2262, pulse 2.0
  oculos: fog 0.3, normal
  suor: 2-4 drops, peeking

FURIOSO (barra paciencia > 70%):
  veia: 4-5px, #CC1144, pulse 3.0, branches 2
  oculos: fog 0.6-0.8, slipping
  suor: 4-6 drops, visible

EXPLOSAO (barra paciencia 100% / briga):
  veia: 6px, #FF0000, pulse 4.0, branches 4
  oculos: fog 1.0 ou fallen
  suor: 8+ drops, encharcado total
```

---

## ANIMACAO 1: IDLE

```javascript
this.anims.create({
    key: 'barroso_idle',
    frames: this.anims.generateFrameNumbers('barroso_idle', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1  // loop infinito
});
```

### Timing Detalhado

| Frame | Duracao | Evento Visual                           | Som                  |
|-------|---------|----------------------------------------|----------------------|
| 0     | 125ms   | Postura ereta, veia 1px                 | —                    |
| 1     | 125ms   | Veia PULSA (1px → 2px), tremor mao     | Pulso sutil (thump)  |
| 2     | 125ms   | Ajusta oculos, veia relaxa              | Toque leve em vidro  |
| 3     | 125ms   | Martelo treme, gota de suor escorre     | —                    |

**Ciclo total**: 500ms (0.5s)
**Easing entre frames**: NENHUM — corte seco (estilo jerky Andre Guedes)

### Particulas no Idle
```javascript
// Gota de suor (Frame 3 — escondida, quase invisivel)
sweatDrop: {
    emitZone: { x: 28, y: 18 },  // tempera direita
    speed: { min: 5, max: 10 },
    angle: { min: 85, max: 95 },  // cai quase vertical
    scale: { start: 0.3, end: 0.1 },
    lifespan: 400,
    tint: 0xF0E8D0,
    alpha: { start: 0.3, end: 0 },  // QUASE invisivel
    frequency: 2000,  // uma gota a cada 2s
    quantity: 1
}
```

### Tween da Veia (overlay pulsante)
```javascript
// Pulso da veia — overlay que muda de escala no frame 1
this.tweens.add({
    targets: veinOverlay,
    scaleX: { from: 1.0, to: 1.5 },
    scaleY: { from: 1.0, to: 1.2 },
    duration: 125,  // dura 1 frame
    yoyo: true,
    ease: 'Stepped',
    repeat: -1,
    repeatDelay: 375  // pausa ate o proximo pulso
});
```

### Tween do Tremor da Mao (Frame 3)
```javascript
// Tremor involuntario do martelo
this.tweens.add({
    targets: gavelSprite,
    x: { from: baseX, to: baseX - 2 },
    duration: 62,    // meio frame
    yoyo: true,
    ease: 'Sine.easeInOut',
    repeat: -1,
    repeatDelay: 438  // so no frame 3
});
```

---

## ANIMACAO 2: WALK

```javascript
this.anims.create({
    key: 'barroso_walk',
    frames: this.anims.generateFrameNumbers('barroso_walk', { start: 0, end: 5 }),
    frameRate: 10,
    repeat: -1
});
```

### Timing Detalhado

| Frame | Duracao | Evento Visual                                      | Som                    |
|-------|---------|----------------------------------------------------|------------------------|
| 0     | 100ms   | Passo direito, toga flui                            | Passo: sapato social   |
| 1     | 100ms   | Passo esquerdo, livro escorrega e reajusta          | Passo + papel          |
| 2     | 100ms   | Passada firme, autoridade, veia pulsa 1x            | Passo firme (louder)   |
| 3     | 100ms   | Passo direito, COSTAS REVELAM suor (1 frame!)       | Passo + gota           |
| 4     | 100ms   | Passo esquerdo, oculos escorregam 1px               | Passo                  |
| 5     | 100ms   | Recomposicao, ajusta oculos                         | Toque vidro + passo    |

**Ciclo total**: 600ms (0.6s)
**Velocidade de movimento**: 80px/s (mais LENTO que outros bosses — andar professoral)

### Particulas no Walk
```javascript
// Gota de suor nas costas (Frame 3 — revelada brevemente)
backSweatReveal: {
    emitZone: { x: 32, y: 35 },  // costas
    speed: { min: 3, max: 8 },
    angle: { min: 170, max: 190 },  // cai para baixo-tras
    scale: { start: 0.4, end: 0.1 },
    lifespan: 200,  // curta — so 1 frame de visibilidade
    tint: 0xF0E8D0,
    alpha: { start: 0.5, end: 0 },
    frequency: 600,  // 1 por ciclo de walk
    quantity: 1
}
```

### Efeito da Toga (Flutter)
```javascript
// Ondulacao da toga durante walk
togaFlutter: {
    amplitude: 3,      // pixels de ondulacao
    frequency: 0.6,    // sincronizado com ciclo de walk
    phase: Math.PI,    // oposto ao passo (balanca contrario)
    applyTo: 'bottom_hem'  // barra inferior da toga
}
```

### Audio Footsteps
```javascript
// Passos de sapato social — som PRECISO, RITMICO
footsteps: {
    asset: 'sfx_shoe_formal',
    volume: 0.3,
    pitch: { min: 0.95, max: 1.05 },  // variacao minima — passos UNIFORMES
    interval: 100  // a cada frame de walk
}
```

---

## ANIMACAO 3: ATTACK

```javascript
this.anims.create({
    key: 'barroso_attack',
    frames: this.anims.generateFrameNumbers('barroso_attack', { start: 0, end: 2 }),
    frameRate: 12,
    repeat: 0  // nao repete
});
```

### Timing Detalhado

| Frame | Duracao | Evento Visual                                 | Som                           |
|-------|---------|-----------------------------------------------|-------------------------------|
| 0     | 83ms    | Ergue martelo — elegancia calculada            | Whoosh sutil ascendente       |
| 1     | 83ms    | Martelo desce — "ORDEM!" + onda de choque      | BANG seco de martelo + "ORDEM"|
| 2     | 83ms    | Recuperacao — como se nada tivesse acontecido   | Silencio                      |

**Ataque completo**: 250ms (0.25s — RAPIDO e PRECISO)
**Hit Window**: Frame 1, 83ms
**Dano Base**: Medio (menor que Xandao, mas mais preciso)
**Area de Efeito**: Cone frontal, 48px de alcance

### Particulas do Ataque
```javascript
// Onda de choque "ORDEM!" (Frame 1)
shockwaveOrdem: {
    type: 'radial',
    center: { x: gavelImpactX, y: gavelImpactY },
    lines: 4,                    // 4 linhas radiais
    lineWidth: 1,
    lineLength: { start: 4, end: 16 },
    color: 0xFFD700,             // dourado
    alpha: { start: 0.8, end: 0 },
    duration: 200,
    ease: 'Power2'
}
```

### Texto Flutuante "ORDEM!"
```javascript
// Onomatopeia que aparece no Frame 1 e fade no Frame 2
ordemText: {
    text: 'ORDEM!',
    font: 'ComicCrumb',          // fonte hand-lettered
    fontSize: 10,
    color: '#FFD700',
    stroke: '#1A1A1A',
    strokeWidth: 2,
    position: { x: gavelX + 12, y: gavelY - 16 },
    animation: {
        appear: { duration: 40, scale: { from: 0.5, to: 1.2 } },
        hold: { duration: 83 },   // 1 frame
        fade: { duration: 120, alpha: { from: 1, to: 0 }, scale: { from: 1.2, to: 0.8 } }
    }
}
```

### Camera Shake (sutil)
```javascript
// Tremor de camera no impacto — SUTIL (nao e Xandao)
this.cameras.main.shake(80, 0.002);  // curto e leve
```

---

## ANIMACAO 4: DEATH

```javascript
this.anims.create({
    key: 'barroso_death',
    frames: this.anims.generateFrameNumbers('barroso_death', { start: 0, end: 3 }),
    frameRate: 6,
    repeat: 0,
    hideOnComplete: false  // congela no ultimo frame
});
```

### Timing Detalhado

| Frame | Duracao | Evento Visual                                     | Som                              |
|-------|---------|---------------------------------------------------|----------------------------------|
| 0     | 167ms   | Compostura racha — oculos deslocam, cabelo sai     | Crack sutil de vidro             |
| 1     | 167ms   | Toga amassa — martelo cai, livro abre e espalha     | Thud (martelo) + flutter (paginas)|
| 2     | 167ms   | Cai de joelhos — suor exposto, veia morta           | Impacto de joelhos no chao       |
| 3     | 167ms   | Deitado — mao estendida, alivio/derrota             | Silencio... respiro longo        |

**Morte completa**: 667ms (0.67s — LENTA, cada frame doi)
**Pos-morte**: Congela no Frame 3 por 2s antes de fade out

### Particulas da Morte
```javascript
// Paginas do livro voando (Frame 1-3)
bookPages: {
    emitZone: { x: 20, y: 45 },  // posicao do livro ao cair
    speed: { min: 20, max: 50 },
    angle: { min: -90, max: -30 },  // para cima e pros lados
    scale: { start: 0.4, end: 0.2 },
    lifespan: 1000,
    tint: 0xF5F5F0,               // branco-pagina
    alpha: { start: 0.9, end: 0 },
    rotate: { min: -180, max: 180 },  // paginas giram
    gravityY: 30,                  // caem lentamente
    frequency: 200,
    quantity: 1,
    maxParticles: 5
}

// Rachadura nos oculos (Frame 0-1)
glassCrack: {
    emitZone: { x: 30, y: 22 },  // posicao dos oculos
    speed: { min: 5, max: 15 },
    angle: { min: 0, max: 360 },
    scale: 0.2,
    lifespan: 300,
    tint: 0xE8E8F0,               // brilho de vidro
    alpha: { start: 0.7, end: 0 },
    quantity: 3,
    maxParticles: 3
}

// Suor revelado (Frame 1-3 — o segredo exposto)
sweatFlood: {
    emitZone: { x: 32, y: 30 },
    speed: { min: 10, max: 25 },
    angle: { min: 60, max: 120 },  // escorre para baixo
    scale: { start: 0.3, end: 0.15 },
    lifespan: 800,
    tint: 0xF0E8D0,
    alpha: { start: 0.6, end: 0 },
    frequency: 150,
    quantity: 2,
    maxParticles: 8
}
```

### Tween do Martelo Caindo
```javascript
this.tweens.add({
    targets: gavelSprite,
    x: gavelX + 15,
    y: gavelY + 20,
    angle: 90,
    duration: 300,
    ease: 'Bounce.easeOut',
    onComplete: () => {
        // Som de martelo batendo no chao
        this.sound.play('sfx_gavel_drop', { volume: 0.4 });
    }
});
```

### Tween da Veia Morrendo
```javascript
// A veia PARA de pulsar e MORRE — apaga como desligando uma maquina
this.tweens.add({
    targets: veinOverlay,
    tint: { from: 0x8B2252, to: 0x6B5B6B },  // roxo-vermelho -> cinza morto
    scaleX: { from: 1.5, to: 1.0 },
    alpha: { from: 1.0, to: 0.3 },
    duration: 500,
    ease: 'Power3'
});
```

### Tween do Cabelo Despenteando
```javascript
// DEVASTADOR — o cabelo que NUNCA sai do lugar, SAI
hairMessTween: {
    targets: hairOverlay,
    angle: { from: 0, to: 15 },      // cabelo pende pro lado
    scaleX: { from: 1.0, to: 1.3 },  // espalha
    duration: 300,
    delay: 100,  // comeca no Frame 0 da death
    ease: 'Back.easeOut'
}
```

---

## ANIMACAO 5: HIT

```javascript
this.anims.create({
    key: 'barroso_hit',
    frames: this.anims.generateFrameNumbers('barroso_hit', { start: 0, end: 1 }),
    frameRate: 10,
    repeat: 0
});
```

### Timing Detalhado

| Frame | Duracao | Evento Visual                          | Som                          |
|-------|---------|----------------------------------------|------------------------------|
| 0     | 100ms   | Impacto — oculos embacam, veia pulsa   | Hit impact + vidro embasando |
| 1     | 100ms   | Recuperacao — alisa toga, compostura    | Tecido alisando              |

**Hit completo**: 200ms
**Knockback**: 4px (MENOS que outros bosses — Barroso resiste ao recuo)

### Efeito de Embacamento dos Oculos
```javascript
// Oculos embacam com o hit — gradual return
glassFogOnHit: {
    immediate: { fog: 0.8, lensColor: '#C0C0D0' },
    recovery: {
        fog: { to: currentFogLevel, duration: 800 },
        lensColor: { to: currentLensColor, duration: 800 },
        ease: 'Sine.easeOut'
    }
}
```

### Flash de Dano (customizado para Barroso)
```javascript
// Flash SUTIL — Barroso nao faz escandalo
damageFlash: {
    color: 0xFF0000,
    alpha: 0.15,       // MUITO sutil — 15% opacity (outros bosses usam 40%)
    duration: 100,
    outline_only: true  // so o contorno pisca, nao o corpo todo
}
```

### Acumulo de Suor por Hit
```javascript
// Cada hit adiciona suor permanente ate reset
onHit: function() {
    this.sweatState.drops += 1;
    if (this.sweatState.drops > 3) {
        this.sweatState.visibility = 'peeking';
    }
    if (this.sweatState.drops > 6) {
        this.sweatState.visibility = 'visible';
    }
    // Incrementa barra de paciencia
    this.patienceBar.value += 8;  // cada hit enche 8% da barra
}
```

---

## ANIMACAO 6: SPECIAL — Paciencia Esgotada

```javascript
this.anims.create({
    key: 'barroso_special_paciencia',
    frames: this.anims.generateFrameNumbers('barroso_special_paciencia', { start: 0, end: 5 }),
    frameRate: 10,
    repeat: 0
});
```

### Timing Detalhado

| Frame | Duracao | Evento Visual                                      | Som                                    |
|-------|---------|----------------------------------------------------|----------------------------------------|
| 0     | 100ms   | Barra 80%, tremor visivel                          | Batimento cardiaco acelerando          |
| 1     | 100ms   | Barra 90%, veia ramificando, rosto vermelho        | Batimento mais rapido                  |
| 2     | 100ms   | Barra 99%, oculos opacos, cegueira de raiva        | Batimento MAXIMO + ar sendo puxado     |
| 3     | 100ms   | EXPLOSAO — "CHEGA!" — barra explode                | EXPLOSAO + GRITO "CHEGA!" + crack chao |
| 4     | 100ms   | Onda de furia elegante — dano em area              | Onda de choque + estrondo              |
| 5     | 100ms   | Silencio — recomposicao patetica                   | Silencio... respiracao pesada          |

**Sequencia completa**: 600ms de animacao + 2s de efeito gameplay
**Area de Efeito**: Circulo de 128px de raio centrado em Barroso
**Dano**: Alto (50% HP de inimigos na area)
**Cooldown**: Barra precisa recarregar do zero

### Barra de Paciencia (UI Element)
```javascript
patienceBar: {
    position: { x: spriteX - 20, y: spriteY - 40 },  // acima da cabeca
    width: 40,
    height: 6,
    border: { color: 0x1A1A1A, width: 1 },
    fill: {
        gradient: [
            { stop: 0.0, color: 0x4A8B4A },   // verde
            { stop: 0.5, color: 0xFFD700 },   // amarelo
            { stop: 0.75, color: 0xFF8C00 },  // laranja
            { stop: 1.0, color: 0xCC1144 },   // vermelho
        ]
    },
    pulseWhenFull: {
        scale: { min: 1.0, max: 1.1 },
        duration: 200,
        repeat: 3
    },
    shatterOnTrigger: {
        particles: 8,
        speed: { min: 30, max: 80 },
        colors: [0xCC1144, 0xFF8C00, 0xFFD700],
        lifespan: 500,
        gravity: 50
    }
}
```

### Particulas da Explosao "CHEGA!"
```javascript
// Frame 3 — a barra explode e Barroso tambem
chegaExplosion: {
    // Fragmentos da barra
    barShatter: {
        quantity: 8,
        speed: { min: 30, max: 80 },
        angle: { min: 0, max: 360 },
        colors: [0xCC1144, 0xFF8C00, 0xFFD700],
        scale: { start: 0.4, end: 0.1 },
        lifespan: 500,
        gravityY: 50
    },
    // Onda de furia
    furyWave: {
        type: 'circle',
        radius: { start: 10, end: 128 },
        lineWidth: 3,
        colors: [0xFFD700, 0xCC1144],
        alpha: { start: 0.8, end: 0 },
        duration: 400,
        ease: 'Power2'
    },
    // Rachaduras no chao
    groundCrack: {
        type: 'radial_lines',
        center: { x: spriteX, y: spriteY + 30 },
        lines: 6,
        length: { start: 0, end: 40 },
        width: 2,
        color: 0x3A3530,
        duration: 200,
        persist: 3000  // rachaduras ficam visiveis por 3s
    },
    // Poeira do impacto
    impactDust: {
        emitZone: { x: spriteX, y: spriteY + 30, width: 40, height: 10 },
        speed: { min: 10, max: 30 },
        angle: { min: -90, max: -30 },
        scale: { start: 0.5, end: 0.1 },
        lifespan: 600,
        tint: 0x8A8580,
        alpha: { start: 0.5, end: 0 },
        quantity: 5
    }
}
```

### Texto "CHEGA!" Flutuante
```javascript
chegaText: {
    text: 'CHEGA!',
    font: 'ComicCrumbBold',
    fontSize: 16,
    color: '#CC1144',
    stroke: '#1A1A1A',
    strokeWidth: 3,
    position: { x: spriteX, y: spriteY - 30 },
    animation: {
        appear: {
            duration: 60,
            scale: { from: 0.3, to: 1.5 },
            ease: 'Back.easeOut'
        },
        shake: {
            duration: 200,
            x: { min: -3, max: 3 },  // letras tremendo
            repeat: 2
        },
        hold: { duration: 300 },
        fade: {
            duration: 200,
            alpha: { from: 1, to: 0 },
            y: { offset: -20 },  // sobe enquanto some
            ease: 'Power2'
        }
    }
}
```

### Camera Shake (FORTE desta vez)
```javascript
// Diferente do attack sutil — aqui TREME DE VERDADE
this.cameras.main.shake(300, 0.008);
```

### Slow Motion Momentaneo
```javascript
// Frame 3: mundo desacelera por 200ms para dar IMPACTO
this.time.timeScale = 0.3;
this.time.delayedCall(200, () => { this.time.timeScale = 1.0; });
```

---

## ANIMACAO 7: SPECIAL — Sessao Encerrada

```javascript
this.anims.create({
    key: 'barroso_special_sessao',
    frames: this.anims.generateFrameNumbers('barroso_special_sessao', { start: 0, end: 3 }),
    frameRate: 10,
    repeat: 0
});
```

### Timing Detalhado

| Frame | Duracao | Evento Visual                                  | Som                                     |
|-------|---------|-------------------------------------------------|-----------------------------------------|
| 0     | 100ms   | Ergue martelo — autoridade maxima               | Silencio reverente                      |
| 1     | 200ms   | Martelo no ar — HOLD (frame duplicado)          | Tensao crescente (tom ascendente)       |
| 2     | 100ms   | MARTELADA — onda de congelamento                | BANG ENORME + "ENCERRADA!" + gelo       |
| 3     | 100ms   | Todos congelados — Barroso satisfeito           | Silencio gelido + cristais              |

**Sequencia completa**: 500ms de animacao + 2s de freeze no gameplay
**Area de Efeito**: MAPA INTEIRO (todos congelados)
**Efeito**: Freeze de 2s em TODOS os personagens (aliados e inimigos)
**Cooldown**: 30s

### Efeito de Congelamento Global
```javascript
sessionEndedFreeze: {
    // Onda expandindo do ponto de impacto
    freezeWave: {
        type: 'expanding_circle',
        radius: { start: 0, end: screenDiagonal },
        duration: 400,
        color: 0x4A6FA5,
        alpha: 0.4,
        lineWidth: 4,
        texture: 'legal_ice',  // textura de gelo juridico
        ease: 'Power3'
    },
    // Efeito em personagens atingidos
    onCharacterHit: {
        tint: 0xC0C0D0,          // monocromatico azul-cinza
        freeze: true,
        duration: 2000,           // 2 segundos
        particles: {
            type: 'ice_crystals',
            quantity: 3,
            colors: [0x4A6FA5, 0xC0C0E0, 0xFFFFFF],
            scale: 0.3,
            lifespan: 2000,
            gravityY: -5  // cristais flutuam levemente
        }
    },
    // Texto judicial
    text: {
        line1: { text: 'A sessao esta...', delay: 100, size: 8, color: '#1A1A1A' },
        line2: { text: 'ENCERRADA!', delay: 300, size: 14, color: '#CC1144', shake: true }
    }
}
```

### Efeito Visual de Gelo Juridico
```javascript
// Textura especial: cristais de gelo misturados com texto juridico
legalIceTexture: {
    base: 'ice_crystal_pattern',
    overlay: {
        type: 'scrolling_text',
        content: 'Art. 5o CF Art. 102 Regimento STF Clausula Petrea...',
        fontSize: 1,      // ILEGIVEL — apenas decorativo
        color: '#6A8AB5',
        alpha: 0.3,
        scrollSpeed: 5
    }
}
```

### Camera Effect
```javascript
// Tela pisca branco no momento do impacto
this.cameras.main.flash(150, 200, 220, 255, true, 0.3);  // flash azul-gelado
// Leve shake
this.cameras.main.shake(200, 0.005);
```

---

## ANIMACAO 8: SPECIAL — Briga com Gilmar

```javascript
this.anims.create({
    key: 'barroso_special_briga',
    frames: this.anims.generateFrameNumbers('barroso_special_briga', { start: 0, end: 7 }),
    frameRate: 8,
    repeat: 0
});
```

### Timing Detalhado (Keyframes — interpolados no gameplay para 10s)

| Frame | Duracao  | Evento Visual                                   | Som                                              |
|-------|----------|--------------------------------------------------|--------------------------------------------------|
| 0     | 200ms    | Deteccao — vira pra Gilmar, tensao               | Sting musical de tensao + "...Gilmar?"            |
| 1     | 1200ms   | Dedo em riste — "Fora de ordem!"                 | "Vossa Excelencia esta FORA DE ORDEM!"            |
| 2     | 1200ms   | Oculos caem — mascara racha                      | Oculos caindo + gasp                              |
| 3     | 1500ms   | "PESSOA HORRIVEL!" — boca grotesca               | "VOCE E UMA PESSOA HORRIVEL!" (gritado)           |
| 4     | 1500ms   | Empurrao — contato fisico                        | Impacto corpo + sapatos derrapando                |
| 5     | 1500ms   | "CALA A BOCA, GILMAR!" — grito maximo            | "GILMAR, PELO AMOR DE DEUS, CALA A BOCA!"        |
| 6     | 1500ms   | Exaustao — maos nos joelhos                      | Respiracao pesada ofegante                        |
| 7     | 1400ms   | Recomposicao fracassada                          | Oculos sendo colocados + toga sendo alisada (falha)|

**Sequencia completa**: ~10s de gameplay (keyframes interpolados com holds)
**Trigger**: Gilmar Mendes presente no mapa dentro de 200px
**Efeito**: AMBOS (Barroso e Gilmar) param de atacar o jogador e brigam ENTRE SI
**Gameplay**: Jogador fica livre para passar enquanto os dois se matam

### Sistema de Sincronizacao com Gilmar
```javascript
// A briga e uma INTERACAO ENTRE DOIS PERSONAGENS
barrosoGilmarFight: {
    trigger: {
        condition: 'gilmar_in_range',
        range: 200,  // pixels
        cooldown: 60000  // 1 minuto entre brigas
    },
    sync: {
        barroso: 'barroso_special_briga',
        gilmar: 'gilmar_special_briga',
        faceEachOther: true,
        distance: 40,  // pixels entre os dois
        lockMovement: true,
        lockAttack: true,
        duration: 10000  // 10 segundos
    },
    damageToEachOther: {
        barroso_to_gilmar: { perSecond: 5, type: 'verbal' },
        gilmar_to_barroso: { perSecond: 5, type: 'verbal' }
    },
    playerEffect: {
        canPassFreely: true,
        showPopcornEmote: true  // emoji de pipoca pro jogador
    }
}
```

### Particulas da Briga
```javascript
// Saliva voando durante gritaria (Frames 3-5)
spitParticles: {
    emitZone: { x: spriteX + 20, y: spriteY + 15 },  // boca
    speed: { min: 20, max: 60 },
    angle: { min: -20, max: 20 },  // na direcao do Gilmar
    scale: { start: 0.2, end: 0.05 },
    lifespan: 400,
    tint: 0xFFFFFF,
    alpha: { start: 0.6, end: 0 },
    frequency: 200,
    quantity: 2
}

// Simbolos de raiva (Frame 1-5)
angerSymbols: {
    type: 'comic_symbols',
    symbols: ['#!@', '!!', '?!', '*#@!'],
    font: 'ComicCrumb',
    fontSize: 6,
    colors: [0xCC1144, 0xFF0000, 0xFF8C00],
    emitZone: { x: spriteX, y: spriteY - 30, width: 30, height: 10 },
    lifespan: 800,
    speed: { min: 10, max: 30 },
    angle: { min: -100, max: -80 },
    frequency: 400
}

// Gotas de suor volumosas (Frame 4-7)
heavySweat: {
    emitZone: { x: spriteX, y: spriteY + 10, width: 20, height: 5 },
    speed: { min: 15, max: 40 },
    angle: { min: 60, max: 120 },
    scale: { start: 0.5, end: 0.2 },
    lifespan: 600,
    tint: 0xF0E8D0,
    alpha: { start: 0.7, end: 0 },
    frequency: 150,
    quantity: 3
}
```

### Baloes de Fala (Comic Book Style)
```javascript
// Cada frame de gritaria tem um balao de fala
speechBubbles: [
    {
        frame: 1,
        text: 'Vossa Excelencia esta\nFORA DE ORDEM!',
        style: 'angry',     // borda irregular, pontas agressivas
        fontSize: { normal: 5, emphasis: 8 },
        color: '#CC1144',
        duration: 1200
    },
    {
        frame: 3,
        text: 'VOCE E UMA\nPESSOA HORRIVEL!',
        style: 'scream',    // borda EXPLODIDA, pontas de estrela
        fontSize: 8,
        color: '#FF0000',
        shake: true,
        duration: 1500
    },
    {
        frame: 5,
        text: 'GILMAR, PELO\nAMOR DE DEUS,\nCALA A BOCA!',
        style: 'escalating', // texto cresce progressivamente
        fontSize: { min: 5, max: 10 },
        color: '#CC1144',
        duration: 1500
    },
    {
        frame: 7,
        text: '...eu mantenho\na serenidade.',
        style: 'whisper',    // borda fina, pontilhada, fonte italica
        fontSize: 4,
        color: '#6B5B6B',
        shake: true,         // texto treme — mentira
        duration: 1400
    }
]
```

### Camera Especial para a Briga
```javascript
// Camera faz zoom lento nos dois durante a briga
fightCamera: {
    zoomIn: {
        from: 1.0,
        to: 1.3,
        duration: 3000,
        ease: 'Sine.easeInOut'
    },
    shake: {
        frames: [3, 4, 5],  // treme nos frames mais intensos
        intensity: 0.004,
        duration: 300
    },
    zoomOut: {
        from: 1.3,
        to: 1.0,
        delay: 8000,  // comeca a voltar nos ultimos 2s
        duration: 2000,
        ease: 'Sine.easeInOut'
    }
}
```

---

## ANIMACAO EXTRA: Ultimate — "CHEGA! TOTAL" (Sugestao)

**Nota**: Ultimate nao definido oficialmente. Sugestao de implementacao para futuro.

```javascript
// "CHEGA!" TOTAL — versao amplificada da Paciencia Esgotada
this.anims.create({
    key: 'barroso_ultimate',
    frames: [
        // Reusa frames da paciencia + frames extras
        ...this.anims.generateFrameNumbers('barroso_special_paciencia', { start: 0, end: 3 }),
        // Frames extras: toga RASGA, veia EXPLODE visualmente, dano MASSIVO
    ],
    frameRate: 12,
    repeat: 0
});

ultimate: {
    name: 'CHEGA_TOTAL',
    description: 'Barroso perde a compostura COMPLETAMENTE. Toga rasga revelando suor, veia explode visualmente, onda de furia MASSIVA.',
    damage: 'instakill em inimigos normais, 80% HP em bosses',
    area: 'mapa inteiro',
    cooldown: 'uma vez por partida',
    visualEffects: {
        togaRip: true,            // toga RASGA ao meio
        veinExplode: true,        // veia pulsa e "explode" em particulas
        hairDestruction: true,    // cabelo despenteado TOTAL
        glassesShatter: true,     // oculos QUEBRAM
        sweatFlood: true,         // tsuname de suor
        groundShatter: true,      // chao racha em toda a area
        screenDistortion: true    // tela distorce brevemente
    }
}
```

---

## Tabela de Sons

| ID                        | Descricao                           | Trigger                  | Volume |
|---------------------------|-------------------------------------|--------------------------|--------|
| `sfx_vein_pulse`          | Batida de coracao abafada           | Veia pulsando            | 0.15   |
| `sfx_glasses_adjust`      | Toque leve em vidro                 | Ajuste dos oculos        | 0.2    |
| `sfx_shoe_formal`         | Passo de sapato social              | Walk frames              | 0.3    |
| `sfx_gavel_raise`         | Whoosh sutil ascendente             | Attack Frame 0           | 0.3    |
| `sfx_gavel_bang`          | Bang seco de martelo de juiz        | Attack Frame 1           | 0.5    |
| `sfx_gavel_drop`          | Martelo caindo no chao              | Death Frame 1            | 0.4    |
| `sfx_glasses_crack`       | Vidro rachando sutilmente           | Death Frame 0            | 0.3    |
| `sfx_pages_flutter`       | Paginas de livro esvoaçando         | Death Frame 1-3          | 0.2    |
| `sfx_knee_impact`         | Joelhos batendo no chao             | Death Frame 2            | 0.35   |
| `sfx_heartbeat_fast`      | Batimento cardiaco acelerado        | Paciencia building       | 0.4    |
| `sfx_explosion_elegant`   | Explosao contida mas poderosa       | "CHEGA!" Frame 3         | 0.7    |
| `sfx_ground_crack`        | Chao rachando                       | "CHEGA!" Frame 3-4       | 0.5    |
| `sfx_freeze_wave`         | Onda de gelo/autoridade expandindo  | Sessao Encerrada Frame 2 | 0.6    |
| `sfx_ice_crystals`        | Cristais de gelo formando           | Sessao Encerrada Frame 3 | 0.3    |
| `sfx_tension_sting`       | Sting musical de reconhecimento     | Briga Frame 0            | 0.5    |
| `sfx_spit`                | Saliva voando                       | Briga Frames 3-5         | 0.15   |
| `sfx_shove`               | Impacto de empurrao                 | Briga Frame 4            | 0.4    |
| `sfx_heavy_breathing`     | Respiracao pesada ofegante          | Briga Frame 6-7          | 0.3    |
| `sfx_cloth_smooth`        | Tecido sendo alisado                | Recomposicao             | 0.2    |

### Vozes (TTS / Gravacao)
| ID                        | Fala                                              | Emocao          | Volume |
|---------------------------|--------------------------------------------------|-----------------|--------|
| `vox_ordem`               | "ORDEM!"                                          | Autoridade fria | 0.6    |
| `vox_chega`               | "CHEGA!"                                          | Furia explodida | 0.8    |
| `vox_encerrada`           | "A sessao esta ENCERRADA!"                        | Autoridade      | 0.7    |
| `vox_fora_ordem`          | "Vossa Excelencia esta fora de ordem!"            | Raiva controlada| 0.6    |
| `vox_pessoa_horrivel`     | "VOCE E UMA PESSOA HORRIVEL!"                     | Furia pura      | 0.8    |
| `vox_cala_boca`           | "Gilmar, pelo amor de Deus, CALA A BOCA!"         | Desespero+furia | 0.8    |
| `vox_serenidade`          | "Eu mantenho a serenidade... eu mantenho... eu..." | Colapso         | 0.4    |
| `vox_nao_mantenho`        | "NAO MANTENHO MAIS!"                              | Explosao        | 0.7    |
| `vox_circo`               | "Isso aqui virou um circo."                       | Resignacao      | 0.5    |

---

## Notas Finais de Implementacao

1. **O CONTRASTE e implementado via SISTEMAS, nao so sprites**: O estado emocional (veia, oculos, suor) muda CONTINUAMENTE durante gameplay, nao so nos frames-chave. Isso exige overlay rendering em tempo real.
2. **Performance**: As overlays (veia, suor, oculos) devem ser sprites SEPARADOS que renderizam SOBRE o sprite base. Evitar bake em cada frame — usar composicao.
3. **A briga com Gilmar e um EVENTO**, nao uma skill ativavel. Triggera automaticamente. O jogador nao controla.
4. **Barra de paciencia e PERSISTENTE** — nao reseta entre encontros (exceto se Barroso morrer). Cada hit do jogador enche. O jogador pode ESTRATEGICAMENTE provocar Barroso para triggar a explosao.
5. **Pos-briga visual**: Apos a briga com Gilmar, Barroso volta ao idle MAS com estado visual "sujo" — toga amassada, oculos tortos, suor visivel. Gradualmente volta ao normal em 30s.
6. **Audio e CRITICO**: O silencio dos frames de idle e TÃO importante quanto os gritos. Barroso e definido pelo CONTRASTE entre silencio e explosao.
