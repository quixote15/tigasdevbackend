# XANDAO - Especificacao Completa de Animacoes

## Boss do STF Principal - "Zumbis de Brasilia"
## Implementacao Phaser 3

---

## Configuracao Global de Animacao

```javascript
// Constantes globais do Xandao
const XANDAO_CONFIG = {
    spriteWidth: 64,
    spriteHeight: 64,
    projectileSize: 32,
    defaultFrameRate: 10,
    scale: 1.5, // Boss e 1.5x maior que inimigos normais
    origin: { x: 0.5, y: 0.85 }, // Ancora nos pes
    hitboxWidth: 40,
    hitboxHeight: 56,
    bossHealthBarWidth: 300,
    bossHealthBarY: 32,
};
```

---

## 1. IDLE - Ameaca Latente

### Configuracao Phaser
```javascript
this.anims.create({
    key: 'xandao-idle',
    frames: this.anims.generateFrameNumbers('xandao-idle', {
        start: 0, end: 3
    }),
    frameRate: 8,
    repeat: -1, // Loop infinito
    yoyo: false
});
```

### Timing Detalhado
| Frame | Duracao (ms) | Evento |
|---|---|---|
| 0 | 125 | Postura base, brilho maximo da careca |
| 1 | 125 | Brilho da careca desloca, veias pulsam |
| 2 | 125 | Toga ondula, biceps flexionam |
| 3 | 125 | Biceps maximo, veias maximo, micro-treme martelo |

**Ciclo total**: 500ms (2 ciclos por segundo)

### Particulas e Efeitos

#### Brilho da Careca (Constante)
```javascript
// Emitter de particulas para brilho da careca
const carecaBrilho = this.add.particles(0, -24, 'particle-white', {
    speed: { min: 5, max: 15 },
    scale: { start: 0.3, end: 0 },
    alpha: { start: 0.6, end: 0 },
    lifespan: 400,
    frequency: 200,
    quantity: 1,
    angle: { min: 200, max: 340 },
    emitZone: {
        type: 'random',
        source: new Phaser.Geom.Circle(0, 0, 6)
    },
    tint: 0xFFFACD // Amarelo claro
});
```

#### Veias Pulsando (Shader/Tint)
```javascript
// Efeito de pulso nas veias - alternancia de tint sutil
this.tweens.add({
    targets: xandaoSprite,
    tint: { from: 0xFFFFFF, to: 0xFFEEEE },
    duration: 500,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

### Sons
| Momento | Som | Arquivo | Volume | Descricao |
|---|---|---|---|---|
| Loop constante | Respiracao pesada | `sfx/xandao-breathing.ogg` | 0.3 | Respiracao grave, ameacadora, loop a cada 2s |
| Frame 3 (biceps) | Estofo de tecido | `sfx/xandao-fabric-stretch.ogg` | 0.15 | Toga esticando com biceps |
| Aleatorio (5-10s) | Resmungo | `sfx/xandao-grumble.ogg` | 0.2 | "Hmph", "Tsc", resmungo de raiva |

### Easing
- **Transicao entre frames**: `Stepped` (sem interpolacao - manter jerky)
- **Particulas da careca**: `Sine.easeOut` (brilho suave natural)
- **Tint das veias**: `Sine.easeInOut` (pulso organico)

---

## 2. WALK - Marcha do Terror

### Configuracao Phaser
```javascript
this.anims.create({
    key: 'xandao-walk',
    frames: this.anims.generateFrameNumbers('xandao-walk', {
        start: 0, end: 5
    }),
    frameRate: 10,
    repeat: -1,
    yoyo: false
});
```

### Timing Detalhado
| Frame | Duracao (ms) | Evento |
|---|---|---|
| 0 | 100 | Pe direito contato, rachadura aparece |
| 1 | 100 | Peso no pe direito, corpo desce 2px, rachadura expande |
| 2 | 100 | Transicao, faiscas do martelo |
| 3 | 100 | Pe esquerdo contato, nova rachadura |
| 4 | 100 | Peso no pe esquerdo, corpo desce 2px |
| 5 | 100 | Transicao retorno, poeira sobe |

**Ciclo total**: 600ms por ciclo completo de caminhada

### Particulas e Efeitos

#### Rachadura no Chao (Cada Passo)
```javascript
// Emitir rachadura a cada passo (frames 0 e 3)
xandaoSprite.on('animationupdate', (anim, frame) => {
    if (frame.index === 0 || frame.index === 3) {
        // Spawn rachadura sprite
        const crack = this.add.sprite(
            xandaoSprite.x,
            xandaoSprite.y + 28,
            'xandao-fx-rachadura'
        );
        crack.play('crack-appear');
        crack.once('animationcomplete', () => {
            this.tweens.add({
                targets: crack,
                alpha: 0,
                duration: 2000,
                onComplete: () => crack.destroy()
            });
        });
    }
});
```

#### Faiscas do Martelo Arrastando
```javascript
const faiscasMartelo = this.add.particles(24, 26, 'particle-yellow', {
    speed: { min: 20, max: 50 },
    scale: { start: 0.4, end: 0 },
    alpha: { start: 1, end: 0 },
    lifespan: 200,
    frequency: 80,
    quantity: 2,
    angle: { min: 160, max: 200 },
    tint: [0xFFD700, 0xFF8C00, 0xFFFFFF],
    emitting: false // Ativar apenas durante walk
});
```

#### Poeira dos Passos
```javascript
const poeiraPassos = this.add.particles(0, 28, 'particle-dust', {
    speed: { min: 10, max: 30 },
    scale: { start: 0.5, end: 0.1 },
    alpha: { start: 0.5, end: 0 },
    lifespan: 500,
    frequency: -1, // Emissao manual
    quantity: 3,
    angle: { min: 220, max: 320 },
    tint: 0x8B7355,
    gravityY: -20
});
```

#### Screen Shake Sutil (Cada Passo)
```javascript
// Micro screen shake a cada passo pesado
xandaoSprite.on('animationupdate', (anim, frame) => {
    if (frame.index === 1 || frame.index === 4) {
        this.cameras.main.shake(50, 0.002); // Sutil, nao enjoativo
    }
});
```

#### Deslocamento Vertical (Peso dos Passos)
```javascript
// Corpo desce nos frames de peso (1 e 4)
this.tweens.add({
    targets: xandaoSprite,
    y: '+2',
    duration: 50,
    yoyo: true,
    ease: 'Quad.easeIn'
});
```

### Sons
| Momento | Som | Arquivo | Volume | Descricao |
|---|---|---|---|---|
| Frame 0, 3 | Impacto de passo | `sfx/xandao-stomp.ogg` | 0.5 | Passo pesado, como bigorna caindo |
| Frame 2, 5 | Martelo arrastando | `sfx/xandao-gavel-drag.ogg` | 0.3 | Metal raspando no concreto |
| Frame 1, 4 | Chao rachando | `sfx/xandao-ground-crack.ogg` | 0.25 | Concreto quebrando sutil |
| Frame 5 | Poeira | `sfx/xandao-dust-puff.ogg` | 0.1 | Puff de poeira leve |
| Constante | Passo ritmico | `sfx/xandao-march-rhythm.ogg` | 0.2 | Heartbeat ritmico grave sincronizado |

### Easing
- **Deslocamento vertical**: `Quad.easeIn` (impacto realista)
- **Faiscas**: `Linear` (direto, mecanico)
- **Poeira**: `Cubic.easeOut` (dispersa rapidamente depois devagar)

---

## 3. ATTACK - Martelada da Censura

### Configuracao Phaser
```javascript
this.anims.create({
    key: 'xandao-attack',
    frames: this.anims.generateFrameNumbers('xandao-attack', {
        start: 0, end: 2
    }),
    frameRate: 12,
    repeat: 0 // Executa uma vez
});
```

### Timing Detalhado
| Frame | Duracao (ms) | Evento |
|---|---|---|
| 0 | 83 | Windup - martelo sobe, biceps maximo, grito |
| 1 | 83 | IMPACTO - martelo desce, flash, "CENSURADO", dano aplicado |
| 2 | 83 | Shockwave - ondas de choque, poeira, cooldown visual |

**Duracao total**: ~250ms (ataque rapido e violento)

### Particulas e Efeitos

#### Flash de Impacto
```javascript
// Frame 1 - Explosao de impacto
const impactFlash = this.add.sprite(
    xandaoSprite.x + 20, // A frente
    xandaoSprite.y + 24,  // No chao
    'xandao-fx-impact'
);
impactFlash.setScale(1.5);
impactFlash.setBlendMode(Phaser.BlendModes.ADD);
this.tweens.add({
    targets: impactFlash,
    alpha: { from: 1, to: 0 },
    scale: { from: 1.5, to: 2.5 },
    duration: 200,
    onComplete: () => impactFlash.destroy()
});
```

#### Texto "CENSURADO" Voador
```javascript
// Projetil de texto que aparece no impacto
const censuradoText = this.add.sprite(
    xandaoSprite.x + 20,
    xandaoSprite.y - 10,
    'xandao-fx-censurado'
);
censuradoText.play('censurado-pulse');
this.tweens.add({
    targets: censuradoText,
    y: censuradoText.y - 20,
    alpha: { from: 1, to: 0 },
    scale: { from: 1, to: 1.8 },
    duration: 800,
    ease: 'Cubic.easeOut',
    onComplete: () => censuradoText.destroy()
});
```

#### Rachadura Estrela no Chao
```javascript
// Rachadura em padrao estrela - maior que a do walk
const crackStar = this.add.sprite(
    xandaoSprite.x + 20,
    xandaoSprite.y + 28,
    'xandao-fx-rachadura'
);
crackStar.setScale(2.0); // 2x maior que rachadura do walk
crackStar.play('crack-appear');
// Fade out em 3 segundos
this.tweens.add({
    targets: crackStar,
    alpha: 0,
    duration: 3000,
    delay: 500,
    onComplete: () => crackStar.destroy()
});
```

#### Onda de Choque (Frame 2)
```javascript
// Arco de shockwave
const shockwave = this.add.circle(
    xandaoSprite.x + 20,
    xandaoSprite.y + 28,
    4, // Raio inicial
    0xFFFFFF,
    0.6
);
shockwave.setStrokeStyle(2, 0xFFFFFF);
shockwave.setFillStyle(0xFFFFFF, 0.1);
this.tweens.add({
    targets: shockwave,
    radius: 60,
    alpha: 0,
    strokeAlpha: 0,
    duration: 400,
    ease: 'Cubic.easeOut',
    onComplete: () => shockwave.destroy()
});
```

#### Screen Shake FORTE
```javascript
// Shake INTENSO no impacto (frame 1)
this.cameras.main.shake(150, 0.008);
// Flash branco rapido
this.cameras.main.flash(100, 255, 255, 255, false, null, null, 0.3);
```

#### Nuvem de Poeira
```javascript
const dustCloud = this.add.particles(
    xandaoSprite.x + 20,
    xandaoSprite.y + 24,
    'particle-dust', {
        speed: { min: 30, max: 80 },
        scale: { start: 0.6, end: 0 },
        alpha: { start: 0.7, end: 0 },
        lifespan: 600,
        quantity: 8,
        angle: { min: 180, max: 360 },
        tint: [0x8B7355, 0x696969, 0xA09080],
        gravityY: -30,
        emitting: false
    }
);
dustCloud.explode(8);
```

### Sons
| Momento | Som | Arquivo | Volume | Descricao |
|---|---|---|---|---|
| Frame 0 | Grito de guerra | `sfx/xandao-scream-censurado.ogg` | 0.8 | "CENSURADOOO!" - grito grave e furioso |
| Frame 0 | Whoosh do martelo subindo | `sfx/xandao-gavel-raise.ogg` | 0.4 | Swoosh pesado para cima |
| Frame 1 | IMPACTO do martelo | `sfx/xandao-gavel-impact.ogg` | 1.0 | Pancada MASSIVA, explosiva, reverberante |
| Frame 1 | Chao quebrando | `sfx/xandao-ground-shatter.ogg` | 0.6 | Concreto estilhacando |
| Frame 1 | Carimbo "CENSURADO" | `sfx/xandao-stamp.ogg` | 0.5 | Som de carimbo de borracha amplificado |
| Frame 2 | Onda de choque | `sfx/xandao-shockwave.ogg` | 0.5 | Woooosh grave, ondulante |
| Frame 2 | Poeira | `sfx/xandao-dust-heavy.ogg` | 0.3 | Nuvem de poeira pesada |

### Easing
- **Flash de impacto**: `Linear` (instantaneo)
- **Texto CENSURADO subindo**: `Cubic.easeOut` (desacelera no topo)
- **Shockwave expandindo**: `Cubic.easeOut` (rapido no inicio, desacelera)
- **Poeira**: `Expo.easeOut` (dispersao explosiva)
- **Rachadura**: `Stepped` (aparece instantaneamente)

### Hitbox do Ataque
```javascript
const attackHitbox = {
    type: 'rectangle',
    x: xandaoSprite.x + 10, // A frente do corpo
    y: xandaoSprite.y - 10,
    width: 48,
    height: 40,
    activeFrames: [1], // So no frame de impacto
    damage: 35,
    knockback: 120,
    knockbackAngle: -30 // Para cima e para tras
};
```

---

## 4. DEATH - Queda do Regime

### Configuracao Phaser
```javascript
this.anims.create({
    key: 'xandao-death',
    frames: this.anims.generateFrameNumbers('xandao-death', {
        start: 0, end: 3
    }),
    frameRate: 8,
    repeat: 0,
    hideOnComplete: false // Manter ultimo frame visivel
});
```

### Timing Detalhado
| Frame | Duracao (ms) | Evento |
|---|---|---|
| 0 | 125 | Choque - recua, surpresa, careca piscando |
| 1 | 125 | Caindo - toga decompondo, papeis voando |
| 2 | 125 | No chao - martelo quebra, papeis espalhados |
| 3 | Permanente | Estado final - corpo coberto de papeis, careca opaca |

**Duracao ate estado final**: 500ms (depois permanece)

### Particulas e Efeitos

#### Papeis de Inquerito Voando
```javascript
// Sistema de particulas com textura de papel
const papelConfig = {
    texture: 'particle-paper',
    frames: [0, 1, 2, 3], // 4 variantes de papel
    speed: { min: 20, max: 80 },
    scale: { start: 0.5, end: 0.3 },
    alpha: { start: 1, end: 0.4 },
    lifespan: { min: 2000, max: 4000 },
    angle: { min: 0, max: 360 },
    rotate: { min: -180, max: 180 },
    gravityY: 15, // Caem devagar como papel
    quantity: 0,
    emitting: false
};

// Frame 1: poucos papeis
this.time.delayedCall(125, () => {
    paperEmitter.explode(6, xandaoSprite.x, xandaoSprite.y);
});

// Frame 2: muitos papeis
this.time.delayedCall(250, () => {
    paperEmitter.explode(12, xandaoSprite.x, xandaoSprite.y);
});

// Frame 3: ultimos papeis + espalhados no chao
this.time.delayedCall(375, () => {
    paperEmitter.explode(8, xandaoSprite.x, xandaoSprite.y);
    // Papeis estaticos no chao
    for (let i = 0; i < 6; i++) {
        const paper = this.add.sprite(
            xandaoSprite.x + Phaser.Math.Between(-30, 30),
            xandaoSprite.y + Phaser.Math.Between(10, 30),
            'particle-paper',
            Phaser.Math.Between(0, 3)
        );
        paper.setScale(0.4);
        paper.setRotation(Phaser.Math.FloatBetween(-0.5, 0.5));
        paper.setAlpha(0.8);
    }
});
```

#### Careca Piscando (Frame 0)
```javascript
// Brilho da careca pisca entre ligado e desligado
this.tweens.add({
    targets: carecaBrilhoEmitter,
    alpha: { from: 1, to: 0 },
    duration: 100,
    yoyo: true,
    repeat: 3,
    onComplete: () => {
        carecaBrilhoEmitter.stop(); // Para de brilhar permanentemente
    }
});
```

#### Martelo Quebrando (Frame 2)
```javascript
// Spawn 3 pedacos do martelo
const gavelPieces = ['gavel-piece-1', 'gavel-piece-2', 'gavel-piece-3'];
gavelPieces.forEach((piece, i) => {
    const p = this.add.sprite(
        xandaoSprite.x + 15 + (i * 8),
        xandaoSprite.y + 20,
        piece
    );
    this.tweens.add({
        targets: p,
        x: p.x + Phaser.Math.Between(-20, 20),
        y: p.y + Phaser.Math.Between(-5, 10),
        angle: Phaser.Math.Between(-90, 90),
        alpha: { from: 1, to: 0.5 },
        duration: 600,
        ease: 'Bounce.easeOut'
    });
});
```

#### Fade do Corpo (Frame 3)
```javascript
// Corpo fica semi-transparente
this.tweens.add({
    targets: xandaoSprite,
    alpha: 0.7,
    duration: 500,
    delay: 375,
    ease: 'Sine.easeIn'
});
```

#### Brilho Residual Vermelho nos Papeis
```javascript
// Glow vermelho sutil nos papeis espalhados
const residualGlow = this.add.pointlight(
    xandaoSprite.x,
    xandaoSprite.y + 15,
    0xFF0000,
    30, // Raio
    0.15 // Intensidade baixa
);
this.tweens.add({
    targets: residualGlow,
    intensity: { from: 0.15, to: 0.05 },
    duration: 3000,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

### Sons
| Momento | Som | Arquivo | Volume | Descricao |
|---|---|---|---|---|
| Frame 0 | Grunhido de dor | `sfx/xandao-death-grunt.ogg` | 0.8 | Surpresa e dor, grave |
| Frame 0 | Eletricidade falhando | `sfx/xandao-power-flicker.ogg` | 0.4 | Brilho da careca falhando |
| Frame 1 | Papeis voando | `sfx/xandao-papers-flutter.ogg` | 0.5 | Farfalhada de muitos papeis |
| Frame 1 | Tecido rasgando | `sfx/xandao-robe-tear.ogg` | 0.6 | Toga se desfazendo |
| Frame 2 | Corpo caindo | `sfx/xandao-body-fall.ogg` | 0.7 | Impacto pesado no chao |
| Frame 2 | Martelo quebrando | `sfx/xandao-gavel-break.ogg` | 0.8 | Madeira e metal se quebrando |
| Frame 3 | Silencio dramatico | --- | 0 | 500ms de silencio total |
| Apos silencio | Eco de "censurado" | `sfx/xandao-echo-censurado.ogg` | 0.2 | Eco distante e triste da palavra |
| Apos eco | Musica de boss derrotado | `music/xandao-defeated.ogg` | 0.4 | Tema melancolico 5 segundos |

### Easing
- **Papeis voando**: `Expo.easeOut` (explosao inicial depois flutuam)
- **Gravidade dos papeis**: Custom curve (cai devagar como papel real)
- **Careca piscando**: `Stepped` (liga/desliga binario)
- **Corpo fade**: `Sine.easeIn` (desaparece gradualmente)
- **Martelo quebrando**: `Bounce.easeOut` (pedacos quicam)

---

## 5. HIT - Furia Amplificada

### Configuracao Phaser
```javascript
this.anims.create({
    key: 'xandao-hit',
    frames: this.anims.generateFrameNumbers('xandao-hit', {
        start: 0, end: 1
    }),
    frameRate: 12,
    repeat: 0
});
```

### Timing Detalhado
| Frame | Duracao (ms) | Evento |
|---|---|---|
| 0 | 83 | Recuo, flash branco, olhos explodem vermelho |
| 1 | 83 | Raiva amplifica, corpo expande, aura vermelha |

**Duracao total**: ~167ms (muito rapido - boss nao fica vulneravel por muito tempo)

### Particulas e Efeitos

#### Flash de Dano (Frame 0)
```javascript
// Borda branca piscando
xandaoSprite.setTint(0xFFFFFF);
this.time.delayedCall(50, () => {
    xandaoSprite.clearTint();
});
// Deslocamento para tras
this.tweens.add({
    targets: xandaoSprite,
    x: xandaoSprite.x - 6,
    duration: 40,
    yoyo: true,
    ease: 'Cubic.easeOut'
});
```

#### Olhos Vermelhos Intensificados (Frame 0)
```javascript
// Particulas vermelhas saindo dos olhos
const eyeParticles = this.add.particles(0, -20, 'particle-red', {
    speed: { min: 40, max: 80 },
    scale: { start: 0.3, end: 0 },
    alpha: { start: 1, end: 0 },
    lifespan: 200,
    quantity: 4,
    angle: { min: -10, max: 10 }, // Horizontal para frente
    tint: [0xFF0000, 0xFF3333, 0xCC0000],
    emitting: false
});
eyeParticles.explode(4);
```

#### Expansao do Corpo (Frame 1)
```javascript
// Corpo "incha" de raiva
this.tweens.add({
    targets: xandaoSprite,
    scaleX: { from: 1.5, to: 1.58 }, // Cresce 5%
    scaleY: { from: 1.5, to: 1.58 },
    duration: 80,
    yoyo: true,
    ease: 'Quad.easeOut'
});
```

#### Aura Vermelha (Frame 1)
```javascript
// Glow vermelho temporario ao redor
const auraGlow = this.add.sprite(
    xandaoSprite.x,
    xandaoSprite.y,
    'xandao-idle',
    0
);
auraGlow.setTint(0xFF0000);
auraGlow.setAlpha(0.3);
auraGlow.setScale(1.65);
auraGlow.setBlendMode(Phaser.BlendModes.ADD);
this.tweens.add({
    targets: auraGlow,
    alpha: 0,
    duration: 300,
    onComplete: () => auraGlow.destroy()
});
```

#### Buff Visual (Enrage)
```javascript
// Se HP < 50%, hit ativa "enrage" permanente
if (xandao.hp < xandao.maxHp * 0.5) {
    xandao.enraged = true;
    // Particulas de raiva constantes
    const rageParticles = this.add.particles(0, -16, 'particle-red', {
        speed: { min: 10, max: 25 },
        scale: { start: 0.2, end: 0 },
        alpha: { start: 0.5, end: 0 },
        lifespan: 400,
        frequency: 150,
        quantity: 1,
        angle: { min: 250, max: 290 },
        tint: 0xFF0000
    });
    // Olhos brilham permanentemente
    // Aura vermelha constante leve
}
```

### Sons
| Momento | Som | Arquivo | Volume | Descricao |
|---|---|---|---|---|
| Frame 0 | Grunhido de raiva | `sfx/xandao-hit-grunt.ogg` | 0.7 | "ARGH!" grave e furioso |
| Frame 0 | Impacto no corpo | `sfx/xandao-hit-impact.ogg` | 0.5 | Som de golpe em carne |
| Frame 1 | Rugido de furia | `sfx/xandao-rage-roar.ogg` | 0.6 | Rugido curto, ameacador |
| Frame 1 (se enrage) | Power up | `sfx/xandao-enrage.ogg` | 0.8 | Som de energia crescendo, grave |

### Easing
- **Recuo**: `Cubic.easeOut` (rapido depois desacelera)
- **Expansao**: `Quad.easeOut` (incha rapido)
- **Aura fade**: `Linear` (desaparece uniforme)
- **Tint flash**: `Stepped` (binario, liga/desliga)

---

## 6. SPECIAL - Censura Monocratica

### Configuracao Phaser
```javascript
this.anims.create({
    key: 'xandao-special-censura',
    frames: this.anims.generateFrameNumbers('xandao-special-censura', {
        start: 0, end: 5
    }),
    frameRate: 10,
    repeat: 0
});
```

### Timing Detalhado
| Frame | Duracao (ms) | Evento |
|---|---|---|
| 0 | 100 | Preparacao - postura rigida, mao levantando |
| 1 | 100 | Mao levantada - aura vermelha na palma |
| 2 | 100 | Raios ativam - lasers dos olhos, levitacao |
| 3 | 100 | "CENSURADO" gigante aparece |
| 4 | 100 | Expansao - onda de silencio propaga |
| 5 | 100 | Conclusao - bracos cruzados, satisfacao |

**Duracao da animacao**: 600ms
**Duracao do efeito gameplay**: 5000ms (silencia area)

### Particulas e Efeitos

#### Aura na Mao (Frames 1-4)
```javascript
const handAura = this.add.particles(
    xandaoSprite.x - 10,
    xandaoSprite.y - 20,
    'particle-red', {
        speed: { min: 5, max: 15 },
        scale: { start: 0.4, end: 0 },
        alpha: { start: 0.8, end: 0 },
        lifespan: 300,
        frequency: 50,
        quantity: 2,
        angle: { min: 0, max: 360 },
        tint: [0xFF0000, 0xFF3333, 0xCC0000],
        emitZone: {
            type: 'random',
            source: new Phaser.Geom.Circle(0, 0, 5)
        }
    }
);
```

#### Raios dos Olhos (Frames 2-4)
```javascript
// Dois feixes laser dos olhos
const createEyeBeam = (yOffset) => {
    const beam = this.add.rectangle(
        xandaoSprite.x + 32,
        xandaoSprite.y - 22 + yOffset,
        0, 2,
        0xFF0000, 0.8
    );
    beam.setOrigin(0, 0.5);
    beam.setBlendMode(Phaser.BlendModes.ADD);

    // Beam cresce horizontalmente
    this.tweens.add({
        targets: beam,
        width: 80,
        duration: 150,
        ease: 'Cubic.easeOut',
        yoyo: true,
        hold: 200,
        onComplete: () => beam.destroy()
    });

    // Borda amarela
    const beamBorder = this.add.rectangle(
        beam.x, beam.y,
        0, 4,
        0xFFD700, 0.3
    );
    beamBorder.setOrigin(0, 0.5);
    beamBorder.setBlendMode(Phaser.BlendModes.ADD);
    // Mesma tween...
};

createEyeBeam(0);  // Olho esquerdo
createEyeBeam(3);  // Olho direito
```

#### Levitacao (Frames 2-5)
```javascript
this.tweens.add({
    targets: xandaoSprite,
    y: xandaoSprite.y - 4,
    duration: 200,
    yoyo: true,
    hold: 200,
    ease: 'Sine.easeInOut'
});
```

#### Texto "CENSURADO" Gigante (Frame 3-5)
```javascript
const censuradoGiant = this.add.text(
    xandaoSprite.x,
    xandaoSprite.y - 40,
    'CENSURADO',
    {
        fontFamily: 'Impact, sans-serif',
        fontSize: '24px',
        color: '#CC0000',
        stroke: '#000000',
        strokeThickness: 3,
        align: 'center'
    }
);
censuradoGiant.setOrigin(0.5);
censuradoGiant.setRotation(-0.1); // Levemente inclinado como carimbo
censuradoGiant.setAlpha(0);

this.tweens.add({
    targets: censuradoGiant,
    alpha: { from: 0, to: 1 },
    scale: { from: 0.5, to: 1.2 },
    duration: 200,
    yoyo: true,
    hold: 400,
    ease: 'Back.easeOut',
    onComplete: () => censuradoGiant.destroy()
});
```

#### Onda de Silencio (Frame 4-5)
```javascript
// Circulo expandindo representando area de efeito
for (let i = 0; i < 3; i++) {
    this.time.delayedCall(i * 100, () => {
        const wave = this.add.circle(
            xandaoSprite.x,
            xandaoSprite.y,
            5,
            0xFF0000,
            0.0
        );
        wave.setStrokeStyle(2, 0xFF0000, 0.6);

        this.tweens.add({
            targets: wave,
            radius: 120,
            strokeAlpha: 0,
            duration: 600,
            ease: 'Cubic.easeOut',
            onComplete: () => wave.destroy()
        });
    });
}
```

#### Area de Efeito Persistente (5 segundos)
```javascript
const silenceZone = this.add.circle(
    xandaoSprite.x,
    xandaoSprite.y,
    80,    // 5-tile radius
    0xFF0000,
    0.05   // Quase transparente
);
silenceZone.setStrokeStyle(1, 0xFF0000, 0.3);

// Pulsa durante a duracao
this.tweens.add({
    targets: silenceZone,
    strokeAlpha: { from: 0.3, to: 0.1 },
    fillAlpha: { from: 0.05, to: 0.02 },
    duration: 1000,
    yoyo: true,
    repeat: 4, // 5 segundos total
    onComplete: () => {
        this.tweens.add({
            targets: silenceZone,
            alpha: 0,
            duration: 500,
            onComplete: () => silenceZone.destroy()
        });
    }
});
```

### Sons
| Momento | Som | Arquivo | Volume | Descricao |
|---|---|---|---|---|
| Frame 0 | Toga endurece | `sfx/xandao-robe-stiffen.ogg` | 0.3 | Tecido ficando rigido |
| Frame 1 | Energia carregando | `sfx/xandao-power-charge.ogg` | 0.5 | Zumbido crescente |
| Frame 2 | Raios dos olhos | `sfx/xandao-eye-beams.ogg` | 0.7 | Laser + eletricidade |
| Frame 3 | CENSURADO carimbo | `sfx/xandao-stamp-giant.ogg` | 1.0 | CARIMBO MASSIVO reverberante |
| Frame 3 | Voz "MONOCRATICAMENTE!" | `sfx/xandao-voice-monocraticamente.ogg` | 0.9 | Bordao gritado |
| Frame 4 | Onda de silencio | `sfx/xandao-silence-wave.ogg` | 0.6 | Woosh invertido (som sumindo) |
| Frame 5 | Musica abafa | `sfx/xandao-muffle.ogg` | --- | Todos sons ficam abafados por 5s |
| Duracao do efeito | Silencio opressivo | `sfx/xandao-oppressive-silence.ogg` | 0.2 | Drone grave continuo 5s |

### Easing
- **Levitacao**: `Sine.easeInOut` (subida e descida suaves)
- **Raios dos olhos**: `Cubic.easeOut` (estendem rapido)
- **Texto CENSURADO**: `Back.easeOut` (overshoot dramatico)
- **Ondas de silencio**: `Cubic.easeOut` (expandem rapido)
- **Zona persistente**: `Sine.easeInOut` (pulso organico)

---

## 7. SPECIAL - Xandaquistao (Zona de Controle)

### Configuracao Phaser
```javascript
this.anims.create({
    key: 'xandao-special-xandaquistao',
    frames: this.anims.generateFrameNumbers('xandao-special-xandaquistao', {
        start: 0, end: 7
    }),
    frameRate: 8,
    repeat: 0
});
```

### Timing Detalhado
| Frame | Duracao (ms) | Evento |
|---|---|---|
| 0 | 125 | Declaracao - postura imperial, grito |
| 1 | 125 | Cravo no chao - martelo impacta |
| 2 | 125 | Zona comecando - circulo dourado expandindo |
| 3 | 125 | Bandeiras surgindo - X cortado |
| 4 | 125 | Zona expandindo - 75% completa |
| 5 | 125 | Zona completa - 100%, toga militar |
| 6 | 125 | Ativacao - efeitos interiores |
| 7 | Loop | Estado sustentado - pulsa enquanto ativo |

**Duracao da animacao**: 875ms + loop do frame 7
**Duracao do efeito gameplay**: Configuravel (10-15s sugerido)

### Particulas e Efeitos

#### Impacto do Martelo no Chao (Frame 1)
```javascript
// Similar ao attack mas com particulas douradas
const goldenImpact = this.add.particles(
    xandaoSprite.x,
    xandaoSprite.y + 28,
    'particle-gold', {
        speed: { min: 40, max: 100 },
        scale: { start: 0.5, end: 0 },
        alpha: { start: 1, end: 0 },
        lifespan: 400,
        quantity: 12,
        angle: { min: 200, max: 340 },
        tint: [0xDAA520, 0xFFD700, 0xB8860B],
        gravityY: 80,
        emitting: false
    }
);
goldenImpact.explode(12);
```

#### Zona Expandindo (Frames 2-5)
```javascript
const controlZone = this.add.circle(
    xandaoSprite.x,
    xandaoSprite.y + 28,
    0,
    0x8B0000, 0.0 // Comeca invisivel
);
controlZone.setStrokeStyle(3, 0xDAA520, 0.8);

// Expande progressivamente
this.tweens.add({
    targets: controlZone,
    radius: 100,
    fillAlpha: 0.15,
    duration: 500, // Frames 2-5
    ease: 'Cubic.easeOut'
});

// Chao interior muda de cor
const zoneFloor = this.add.circle(
    xandaoSprite.x,
    xandaoSprite.y + 28,
    0,
    0x4A0000, 0.0
);
this.tweens.add({
    targets: zoneFloor,
    radius: 98,
    fillAlpha: 0.2,
    duration: 500,
    ease: 'Cubic.easeOut'
});
```

#### Bandeiras com X Cortado (Frames 3-7)
```javascript
// 4 bandeiras em posicoes cardinais
const bannerPositions = [
    { x: -60, y: -20 },  // Esquerda
    { x: 60, y: -20 },   // Direita
    { x: 0, y: -60 },    // Cima
    { x: 0, y: 40 }      // Baixo
];

bannerPositions.forEach((pos, i) => {
    this.time.delayedCall(375 + (i * 62), () => { // Aparecem escalonados
        const banner = this.add.sprite(
            xandaoSprite.x + pos.x,
            xandaoSprite.y + pos.y,
            'xandao-banner-x'
        );
        banner.setScale(0);
        this.tweens.add({
            targets: banner,
            scale: 0.8,
            duration: 200,
            ease: 'Back.easeOut'
        });

        // Ondulacao da bandeira
        this.tweens.add({
            targets: banner,
            angle: { from: -5, to: 5 },
            duration: 800,
            yoyo: true,
            repeat: -1,
            ease: 'Sine.easeInOut'
        });
    });
});
```

#### Poeira Dourada Subindo (Frames 2-6)
```javascript
const goldenDust = this.add.particles(
    xandaoSprite.x,
    xandaoSprite.y + 28,
    'particle-gold', {
        speed: { min: 5, max: 20 },
        scale: { start: 0.3, end: 0 },
        alpha: { start: 0.6, end: 0 },
        lifespan: 1000,
        frequency: 100,
        quantity: 2,
        angle: { min: 250, max: 290 },
        tint: [0xDAA520, 0xFFD700],
        emitZone: {
            type: 'random',
            source: new Phaser.Geom.Circle(0, 0, 60)
        }
    }
);
```

#### Pulso da Zona Ativa (Frame 7 - Loop)
```javascript
// Borda da zona pulsa
this.tweens.add({
    targets: controlZone,
    strokeAlpha: { from: 0.8, to: 0.4 },
    radius: { from: 100, to: 103 },
    duration: 1500,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});

// Ondulacoes internas
const rippleTimer = this.time.addEvent({
    delay: 2000,
    callback: () => {
        const ripple = this.add.circle(
            xandaoSprite.x,
            xandaoSprite.y + 28,
            10,
            0xDAA520, 0.0
        );
        ripple.setStrokeStyle(1, 0xDAA520, 0.3);
        this.tweens.add({
            targets: ripple,
            radius: 95,
            strokeAlpha: 0,
            duration: 1500,
            ease: 'Cubic.easeOut',
            onComplete: () => ripple.destroy()
        });
    },
    loop: true
});
```

### Efeitos de Gameplay na Zona
```javascript
// Inimigos dentro da zona:
// - Velocidade reduzida em 40%
// - Indicador visual: linhas de velocidade invertidas (slow-mo)
// - Dano do Xandao aumentado em 25% dentro da zona
// - Xandao se cura 1% HP/s dentro da zona

const zoneDebuff = {
    slowMultiplier: 0.6,
    xandaoDamageMultiplier: 1.25,
    xandaoHealPerSecond: 0.01, // % do max HP
    radius: 100,
    duration: 12000 // 12 segundos
};
```

### Sons
| Momento | Som | Arquivo | Volume | Descricao |
|---|---|---|---|---|
| Frame 0 | Grito "XANDAQUISTAO!" | `sfx/xandao-voice-xandaquistao.ogg` | 1.0 | Bordao berrado |
| Frame 1 | Martelo cravando | `sfx/xandao-gavel-embed.ogg` | 0.8 | Metal entrando na pedra |
| Frame 1 | Onda sismica | `sfx/xandao-seismic.ogg` | 0.6 | Tremor grave |
| Frame 2-5 | Zona expandindo | `sfx/xandao-zone-expand.ogg` | 0.5 | Zumbido crescente dourado |
| Frame 3-4 | Bandeiras subindo | `sfx/xandao-banners-rise.ogg` | 0.4 | Pano estalando no vento |
| Frame 5 | Zona completa | `sfx/xandao-zone-complete.ogg` | 0.7 | GONG grave reverberante |
| Frame 6 | Ativacao | `sfx/xandao-zone-activate.ogg` | 0.5 | Hum eletrico |
| Loop (Frame 7) | Zona ativa | `sfx/xandao-zone-ambient.ogg` | 0.3 | Drone autoritario continuo |

### Easing
- **Zona expandindo**: `Cubic.easeOut` (rapido no inicio)
- **Bandeiras surgindo**: `Back.easeOut` (overshoot dramatico)
- **Bandeiras ondulando**: `Sine.easeInOut` (organico)
- **Pulso da zona**: `Sine.easeInOut` (ritmico)
- **Poeira dourada**: `Linear` (constante)
- **Impacto do martelo**: `Expo.easeOut` (explosivo)

---

## 8. SPECIAL - Apagao Digital (Ultimate)

### Configuracao Phaser
```javascript
this.anims.create({
    key: 'xandao-special-apagao',
    frames: this.anims.generateFrameNumbers('xandao-special-apagao', {
        start: 0, end: 5
    }),
    frameRate: 10,
    repeat: 0
});
```

### Timing Detalhado
| Frame | Duracao (ms) | Evento |
|---|---|---|
| 0 | 100 | Ergue mao - eletricidade comeca |
| 1 | 100 | Esfera eletrica se forma no dedo |
| 2 | 100 | DISPARO - tela escurece |
| 3 | 100 | Static TOTAL - HUD some, jogador cego |
| 4 | Sustentado 3000ms | Apagao mantido - static, silhueta rindo |
| 5 | 100 | Recuperacao - static dissipa |

**Duracao total**: 3500ms (com 3s de apagao efetivo)

### Particulas e Efeitos

#### Eletricidade no Corpo (Frames 0-2)
```javascript
// Arcos eletricos percorrendo o corpo
const electricArcs = this.add.particles(
    xandaoSprite.x,
    xandaoSprite.y - 10,
    'particle-electric', {
        speed: { min: 30, max: 60 },
        scale: { start: 0.3, end: 0 },
        alpha: { start: 0.9, end: 0 },
        lifespan: 150,
        frequency: 30,
        quantity: 3,
        angle: { min: 0, max: 360 },
        tint: [0x00BFFF, 0xFFFFFF, 0x4169E1],
        emitZone: {
            type: 'random',
            source: new Phaser.Geom.Rectangle(-16, -24, 32, 48)
        }
    }
);
```

#### Esfera de Energia (Frame 1-2)
```javascript
const energySphere = this.add.circle(
    xandaoSprite.x + 5,
    xandaoSprite.y - 30,
    2,
    0x00BFFF,
    0.8
);
energySphere.setBlendMode(Phaser.BlendModes.ADD);

// Esfera cresce
this.tweens.add({
    targets: energySphere,
    radius: 8,
    fillAlpha: 1,
    duration: 200,
    ease: 'Cubic.easeIn',
    onComplete: () => {
        // EXPLODE no frame 2
        energySphere.destroy();
        // Transicao para static
    }
});

// Arcos zigzag indo ate a esfera
// (renderizar como linhas graficas que mudam a cada frame)
```

#### APAGAO - Static na Tela Inteira (Frames 3-5)
```javascript
// EFEITO PRINCIPAL - cobre a tela toda
const staticOverlay = this.add.renderTexture(
    0, 0,
    this.cameras.main.width,
    this.cameras.main.height
);
staticOverlay.setScrollFactor(0); // Fixo na camera
staticOverlay.setDepth(9999); // Acima de TUDO

// Gera static randomico
const generateStatic = () => {
    staticOverlay.clear();
    const w = staticOverlay.width;
    const h = staticOverlay.height;

    // Pixels aleatorios
    for (let i = 0; i < 2000; i++) {
        const x = Phaser.Math.Between(0, w);
        const y = Phaser.Math.Between(0, h);
        const gray = Phaser.Math.Between(0, 255);
        const color = Phaser.Display.Color.GetColor(gray, gray, gray);
        staticOverlay.fill(color, 1, x, y, 2, 2);
    }

    // Scanlines horizontais
    for (let y = 0; y < h; y += 4) {
        staticOverlay.fill(0x000000, 0.2, 0, y, w, 1);
    }
};

// Atualiza static a cada frame
const staticTimer = this.time.addEvent({
    delay: 83, // ~12 fps de static
    callback: generateStatic,
    loop: true
});

// Silhueta do Xandao no centro do static
const silhouette = this.add.sprite(
    this.cameras.main.centerX,
    this.cameras.main.centerY,
    'xandao-idle', 0
);
silhouette.setScrollFactor(0);
silhouette.setDepth(10000);
silhouette.setTint(0x000000);
silhouette.setScale(2);
silhouette.setAlpha(0.7);
```

#### Esconder HUD (Frame 3)
```javascript
// Esconde TODOS os elementos de HUD
const hudElements = [
    playerHealthBar,
    bossHealthBar,
    scoreText,
    minimap,
    itemSlots,
    // ... todos elementos de UI
];

hudElements.forEach(el => {
    this.tweens.add({
        targets: el,
        alpha: 0,
        duration: 100
    });
});
```

#### Texto "SEM SINAL" / "CENSURADO" Alternando (Frames 4-5)
```javascript
const noSignalText = this.add.text(
    this.cameras.main.centerX,
    this.cameras.main.centerY - 60,
    'SEM SINAL',
    {
        fontFamily: 'Courier New, monospace',
        fontSize: '32px',
        color: '#FFFFFF',
        stroke: '#000000',
        strokeThickness: 2
    }
);
noSignalText.setOrigin(0.5);
noSignalText.setScrollFactor(0);
noSignalText.setDepth(10001);

// Alterna texto
const textAlternate = this.time.addEvent({
    delay: 500,
    callback: () => {
        noSignalText.text = noSignalText.text === 'SEM SINAL'
            ? 'CENSURADO'
            : 'SEM SINAL';
        // Tint alternado
        noSignalText.setColor(
            noSignalText.text === 'CENSURADO' ? '#CC0000' : '#FFFFFF'
        );
    },
    repeat: 5
});
```

#### Olhos Vermelhos na Silhueta (Frame 4-5)
```javascript
// Dois pontos vermelhos brilhantes (olhos do Xandao no static)
const leftEye = this.add.circle(
    this.cameras.main.centerX - 4,
    this.cameras.main.centerY - 8,
    2,
    0xFF0000,
    1
);
const rightEye = this.add.circle(
    this.cameras.main.centerX + 4,
    this.cameras.main.centerY - 8,
    2,
    0xFF0000,
    1
);
[leftEye, rightEye].forEach(eye => {
    eye.setScrollFactor(0);
    eye.setDepth(10002);
    eye.setBlendMode(Phaser.BlendModes.ADD);

    // Pulsa
    this.tweens.add({
        targets: eye,
        radius: { from: 2, to: 3 },
        alpha: { from: 1, to: 0.7 },
        duration: 300,
        yoyo: true,
        repeat: -1,
        ease: 'Sine.easeInOut'
    });
});
```

#### Recuperacao (Frame 5)
```javascript
// Static dissipa
this.tweens.add({
    targets: staticOverlay,
    alpha: 0,
    duration: 500,
    ease: 'Cubic.easeIn',
    onComplete: () => {
        staticOverlay.destroy();
        staticTimer.remove();
        silhouette.destroy();
        noSignalText.destroy();
        leftEye.destroy();
        rightEye.destroy();
    }
});

// HUD volta
hudElements.forEach(el => {
    this.tweens.add({
        targets: el,
        alpha: 1,
        duration: 300,
        delay: 200
    });
});

// Efeito de "TV ligando" - linhas horizontais convergindo
const tvOnEffect = this.add.rectangle(
    this.cameras.main.centerX,
    this.cameras.main.centerY,
    this.cameras.main.width,
    2,
    0xFFFFFF,
    0.8
);
tvOnEffect.setScrollFactor(0);
tvOnEffect.setDepth(9998);
this.tweens.add({
    targets: tvOnEffect,
    height: this.cameras.main.height,
    alpha: 0,
    duration: 300,
    ease: 'Cubic.easeOut',
    onComplete: () => tvOnEffect.destroy()
});
```

### Sons
| Momento | Som | Arquivo | Volume | Descricao |
|---|---|---|---|---|
| Frame 0 | Eletricidade crescendo | `sfx/xandao-electric-charge.ogg` | 0.5 | Zap crescente |
| Frame 0 | Risada maligna | `sfx/xandao-evil-laugh.ogg` | 0.6 | Risada cruel, baixa |
| Frame 1 | Esfera formando | `sfx/xandao-sphere-form.ogg` | 0.7 | Som de plasma concentrando |
| Frame 2 | DISPARO | `sfx/xandao-electric-discharge.ogg` | 1.0 | EXPLOSAO ELETRICA massiva |
| Frame 3 | Static de TV | `sfx/xandao-tv-static.ogg` | 0.8 | Chiado de TV sem sinal |
| Frame 3 | Todos sons cortam | --- | 0 | TODOS os sons do jogo param |
| Frame 3 | Voz distorcida | `sfx/xandao-voice-distorted.ogg` | 0.4 | "Faz silencio" com distorcao |
| Frame 4 (3s) | Static continuo | `sfx/xandao-static-loop.ogg` | 0.6 | Loop de static 3 segundos |
| Frame 4 | Heartbeat | `sfx/xandao-heartbeat.ogg` | 0.3 | Batimento cardiaco tenso, lento |
| Frame 5 | TV ligando | `sfx/xandao-tv-on.ogg` | 0.5 | Som de CRT ligando |
| Frame 5 | Sons do jogo voltam | --- | Gradual | Fade in de todos os sons em 500ms |
| Frame 5 | Voz "Viram?" | `sfx/xandao-voice-viram.ogg` | 0.7 | "Viram?" - arrogante |

### Gerenciamento de Audio Durante Apagao
```javascript
// CORTAR todos os sons do jogo durante o apagao
const allSounds = this.sound.sounds;
const savedVolumes = new Map();

// Salvar volumes e mutar
allSounds.forEach(sound => {
    if (!sound.key.startsWith('xandao-')) {
        savedVolumes.set(sound.key, sound.volume);
        this.tweens.add({
            targets: sound,
            volume: 0,
            duration: 100
        });
    }
});

// Apos 3 segundos, restaurar
this.time.delayedCall(3200, () => {
    savedVolumes.forEach((vol, key) => {
        const sound = this.sound.get(key);
        if (sound) {
            this.tweens.add({
                targets: sound,
                volume: vol,
                duration: 500
            });
        }
    });
});
```

### Easing
- **Eletricidade**: `Linear` (caotico, imprevisivel)
- **Esfera crescendo**: `Cubic.easeIn` (acelera antes de explodir)
- **Static aparecendo**: `Stepped` (instantaneo, digital)
- **Static desaparecendo**: `Cubic.easeIn` (dissolve gradual)
- **HUD sumindo**: `Stepped` (corte seco)
- **HUD voltando**: `Cubic.easeOut` (gradual, como TV esquentando)
- **Olhos pulsando**: `Sine.easeInOut` (ameaca ritmica)
- **TV ligando**: `Cubic.easeOut` (expansao rapida)

---

## ANIMACAO DA BARRA DE VIDA DO BOSS

### Aparicao Cinematica
```javascript
// Quando o boss aparece, barra de vida entra com efeito
const bossHealthBar = this.add.container(
    this.cameras.main.centerX,
    -40 // Comeca fora da tela
);

// Fundo da barra
const barBg = this.add.rectangle(0, 0, 300, 20, 0x1a1a1a, 0.8);
barBg.setStrokeStyle(2, 0xDAA520);

// Barra de vida
const barFill = this.add.rectangle(-148, 0, 296, 16, 0xCC0000);
barFill.setOrigin(0, 0.5);

// Nome do boss
const bossName = this.add.text(0, -18, 'XANDAO - MINISTRO DO STF', {
    fontFamily: 'Impact, sans-serif',
    fontSize: '14px',
    color: '#DAA520',
    stroke: '#000000',
    strokeThickness: 2
});
bossName.setOrigin(0.5);

// Icone
const bossIcon = this.add.sprite(-160, 0, 'xandao-portrait');

bossHealthBar.add([barBg, barFill, bossName, bossIcon]);
bossHealthBar.setScrollFactor(0);
bossHealthBar.setDepth(100);

// Entra deslizando de cima
this.tweens.add({
    targets: bossHealthBar,
    y: 32,
    duration: 800,
    ease: 'Bounce.easeOut',
    delay: 500 // Apos cutscene de entrada
});
```

### Efeito de Dano na Barra
```javascript
// Quando recebe dano:
// 1. Barra vermelha diminui
// 2. Barra "fantasma" branca mostra dano anterior
// 3. Shake na barra

const takeDamage = (amount) => {
    const newWidth = (xandao.hp / xandao.maxHp) * 296;

    // Barra fantasma (mostra quanto dano tomou)
    const ghost = this.add.rectangle(
        barFill.x + newWidth,
        barFill.y,
        barFill.width - newWidth,
        16,
        0xFFFFFF,
        0.6
    );
    ghost.setOrigin(0, 0.5);

    // Barra real diminui imediatamente
    barFill.width = newWidth;

    // Fantasma desaparece gradualmente
    this.tweens.add({
        targets: ghost,
        width: 0,
        alpha: 0,
        duration: 600,
        delay: 200,
        ease: 'Cubic.easeIn',
        onComplete: () => ghost.destroy()
    });

    // Shake na barra
    this.tweens.add({
        targets: bossHealthBar,
        x: bossHealthBar.x + 3,
        duration: 30,
        yoyo: true,
        repeat: 3
    });

    // Se HP < 50%, barra pulsa vermelho
    if (xandao.hp < xandao.maxHp * 0.5) {
        barFill.setFillStyle(0xFF0000);
        this.tweens.add({
            targets: barFill,
            alpha: { from: 1, to: 0.6 },
            duration: 500,
            yoyo: true,
            repeat: -1,
            ease: 'Sine.easeInOut'
        });
    }
};
```

---

## CUTSCENE DE ENTRADA DO BOSS

### Sequencia Cinematica
```javascript
const bossIntro = () => {
    // 1. Tela escurece
    const blackout = this.add.rectangle(
        this.cameras.main.centerX,
        this.cameras.main.centerY,
        this.cameras.main.width,
        this.cameras.main.height,
        0x000000, 0
    );
    blackout.setScrollFactor(0);
    blackout.setDepth(999);

    this.tweens.add({
        targets: blackout,
        fillAlpha: 0.7,
        duration: 1000,
        onComplete: () => {
            // 2. Texto "BOSS" aparece
            const bossText = this.add.text(
                this.cameras.main.centerX,
                this.cameras.main.centerY - 40,
                'BOSS DO STF',
                {
                    fontFamily: 'Impact',
                    fontSize: '48px',
                    color: '#CC0000',
                    stroke: '#000000',
                    strokeThickness: 4
                }
            );
            bossText.setOrigin(0.5);
            bossText.setScrollFactor(0);
            bossText.setDepth(1000);
            bossText.setScale(0);

            this.tweens.add({
                targets: bossText,
                scale: 1,
                duration: 500,
                ease: 'Back.easeOut',
                onComplete: () => {
                    // 3. Nome do boss
                    const nameText = this.add.text(
                        this.cameras.main.centerX,
                        this.cameras.main.centerY + 10,
                        '- X A N D A O -',
                        {
                            fontFamily: 'Impact',
                            fontSize: '36px',
                            color: '#DAA520',
                            stroke: '#000000',
                            strokeThickness: 3
                        }
                    );
                    nameText.setOrigin(0.5);
                    nameText.setScrollFactor(0);
                    nameText.setDepth(1000);
                    nameText.setAlpha(0);

                    this.tweens.add({
                        targets: nameText,
                        alpha: 1,
                        duration: 300,
                        hold: 1500,
                        onComplete: () => {
                            // 4. Tudo desaparece, luta comeca
                            this.tweens.add({
                                targets: [bossText, nameText, blackout],
                                alpha: 0,
                                duration: 500,
                                onComplete: () => {
                                    bossText.destroy();
                                    nameText.destroy();
                                    blackout.destroy();
                                    // LUTA COMECA
                                    startBossFight();
                                }
                            });
                        }
                    });
                }
            });
        }
    });

    // Som de intro
    this.sound.play('sfx/xandao-intro-theme', { volume: 0.8 });
    // Voz: "Monocraticamente, eu decreto..."
    this.time.delayedCall(1200, () => {
        this.sound.play('sfx/xandao-voice-intro', { volume: 0.9 });
    });
};
```

---

## TABELA RESUMO DE TODOS OS ASSETS DE AUDIO

| Arquivo | Tipo | Duracao | Descricao |
|---|---|---|---|
| `sfx/xandao-breathing.ogg` | Loop | 2s | Respiracao pesada idle |
| `sfx/xandao-fabric-stretch.ogg` | One-shot | 0.3s | Toga esticando |
| `sfx/xandao-grumble.ogg` | One-shot | 0.5s | Resmungo aleatorio |
| `sfx/xandao-stomp.ogg` | One-shot | 0.2s | Passo pesado |
| `sfx/xandao-gavel-drag.ogg` | One-shot | 0.4s | Martelo arrastando |
| `sfx/xandao-ground-crack.ogg` | One-shot | 0.3s | Chao rachando leve |
| `sfx/xandao-dust-puff.ogg` | One-shot | 0.2s | Poeira leve |
| `sfx/xandao-march-rhythm.ogg` | Loop | 0.6s | Ritmo de marcha |
| `sfx/xandao-scream-censurado.ogg` | One-shot | 0.8s | Grito CENSURADO |
| `sfx/xandao-gavel-raise.ogg` | One-shot | 0.3s | Martelo subindo |
| `sfx/xandao-gavel-impact.ogg` | One-shot | 0.5s | IMPACTO do martelo |
| `sfx/xandao-ground-shatter.ogg` | One-shot | 0.4s | Chao estilhacando |
| `sfx/xandao-stamp.ogg` | One-shot | 0.3s | Carimbo |
| `sfx/xandao-shockwave.ogg` | One-shot | 0.6s | Onda de choque |
| `sfx/xandao-dust-heavy.ogg` | One-shot | 0.4s | Poeira pesada |
| `sfx/xandao-death-grunt.ogg` | One-shot | 0.5s | Grunhido de morte |
| `sfx/xandao-power-flicker.ogg` | One-shot | 0.8s | Energia falhando |
| `sfx/xandao-papers-flutter.ogg` | One-shot | 1.5s | Papeis voando |
| `sfx/xandao-robe-tear.ogg` | One-shot | 0.6s | Toga rasgando |
| `sfx/xandao-body-fall.ogg` | One-shot | 0.4s | Corpo caindo |
| `sfx/xandao-gavel-break.ogg` | One-shot | 0.5s | Martelo quebrando |
| `sfx/xandao-echo-censurado.ogg` | One-shot | 2s | Eco distante |
| `music/xandao-defeated.ogg` | One-shot | 5s | Tema de derrota |
| `sfx/xandao-hit-grunt.ogg` | One-shot | 0.3s | Grunhido de raiva |
| `sfx/xandao-hit-impact.ogg` | One-shot | 0.2s | Golpe no corpo |
| `sfx/xandao-rage-roar.ogg` | One-shot | 0.4s | Rugido |
| `sfx/xandao-enrage.ogg` | One-shot | 1s | Power up |
| `sfx/xandao-robe-stiffen.ogg` | One-shot | 0.3s | Toga enrijece |
| `sfx/xandao-power-charge.ogg` | One-shot | 0.5s | Energia carregando |
| `sfx/xandao-eye-beams.ogg` | One-shot | 0.6s | Raios dos olhos |
| `sfx/xandao-stamp-giant.ogg` | One-shot | 0.8s | Carimbo gigante |
| `sfx/xandao-voice-monocraticamente.ogg` | One-shot | 1.2s | Bordao |
| `sfx/xandao-silence-wave.ogg` | One-shot | 0.8s | Onda de silencio |
| `sfx/xandao-muffle.ogg` | Effect | 5s | Abafa todos sons |
| `sfx/xandao-oppressive-silence.ogg` | Loop | 5s | Drone opressivo |
| `sfx/xandao-voice-xandaquistao.ogg` | One-shot | 1s | Bordao |
| `sfx/xandao-gavel-embed.ogg` | One-shot | 0.5s | Martelo cravando |
| `sfx/xandao-seismic.ogg` | One-shot | 0.6s | Tremor |
| `sfx/xandao-zone-expand.ogg` | One-shot | 2s | Zona expandindo |
| `sfx/xandao-banners-rise.ogg` | One-shot | 0.5s | Bandeiras subindo |
| `sfx/xandao-zone-complete.ogg` | One-shot | 1s | Gong |
| `sfx/xandao-zone-activate.ogg` | One-shot | 0.5s | Ativacao |
| `sfx/xandao-zone-ambient.ogg` | Loop | 3s | Drone da zona |
| `sfx/xandao-electric-charge.ogg` | One-shot | 0.8s | Eletricidade |
| `sfx/xandao-evil-laugh.ogg` | One-shot | 1.5s | Risada maligna |
| `sfx/xandao-sphere-form.ogg` | One-shot | 0.5s | Esfera formando |
| `sfx/xandao-electric-discharge.ogg` | One-shot | 0.8s | Descarga massiva |
| `sfx/xandao-tv-static.ogg` | One-shot | 0.5s | Static de TV |
| `sfx/xandao-voice-distorted.ogg` | One-shot | 1s | Voz distorcida |
| `sfx/xandao-static-loop.ogg` | Loop | 3s | Static continuo |
| `sfx/xandao-heartbeat.ogg` | Loop | 1s | Batimento cardiaco |
| `sfx/xandao-tv-on.ogg` | One-shot | 0.5s | TV ligando |
| `sfx/xandao-voice-viram.ogg` | One-shot | 0.5s | "Viram?" |
| `sfx/xandao-intro-theme.ogg` | One-shot | 4s | Tema de entrada |
| `sfx/xandao-voice-intro.ogg` | One-shot | 2s | Fala de intro |
