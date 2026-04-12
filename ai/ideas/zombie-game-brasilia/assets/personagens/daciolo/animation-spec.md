# CABO DACIOLO (O Profeta) -- Animation Specification
### Phaser 3 Implementation Guide | Ciclos, Timing, Particulas, Transicoes
### Zumbis de Brasilia | Abril 2026

---

> *"A animacao do Daciolo deve ser TWITCHY, JERKY, ORGANICA. Nada suave. Ele vibra com energia divina que NAO consegue ser contida num corpo mortal."*

---

## 1. CONFIGURACAO GLOBAL (Phaser 3)

### Sprite Sheet Loading

```javascript
// preload()
this.load.spritesheet('daciolo-idle-down', 'assets/personagens/daciolo/sprites/daciolo-idle-down.png', {
    frameWidth: 64,
    frameHeight: 64
});
// Repetir para cada sheet e direcao: idle-up, idle-left, idle-right, walk-*, attack-*, etc.
```

### Constantes de Animacao

```javascript
const DACIOLO_ANIM = {
    // Frame rates (estilo jerky -- NAO suave)
    IDLE_FPS: 8,
    WALK_FPS: 10,
    ATTACK_FPS: 12,
    DEATH_FPS: 6,
    HIT_FPS: 12,
    SPECIAL_FUMACA_FPS: 10,
    SPECIAL_GLORIA_FPS: 10,
    SPECIAL_EXORCISMO_FPS: 8,
    SPECIAL_RORAIMA_FPS: 10,
    SPECIAL_URSAL_FPS: 8,
    SPECIAL_CANDIDATURA_FPS: 10,
    SPECIAL_EXORCISMO_MASSA_FPS: 8,
    ERRO_COMICO_FPS: 10,

    // Duracao de efeitos pos-animacao (ms)
    FUMACA_RESIDUAL_DURATION: 1500,
    AUREOLA_DIM_AFTER_FUMACA: 30000,
    CURA_GLOW_DURATION: 2000,
    EXORCISMO_MASSA_GLOW_DURATION: 3000,
    CONFUSAO_DURATION: 3000,
    STUN_DURATION: 3000,
    RORAIMA_TOTAL_DURATION: 8000,
    RORAIMA_FIRE_LOOP_DURATION: 4000,
    DEATH_PARTICLES_AFTER: 2000,
    SANTINHO_GROUND_DURATION: 10000,

    // Cooldowns (ms)
    COOLDOWN_FUMACA: 45000,
    COOLDOWN_GLORIA: 12000,
    COOLDOWN_EXORCISMO: 20000,
    COOLDOWN_RORAIMA: 35000,
    COOLDOWN_URSAL: 60000,
    COOLDOWN_CANDIDATURA: 15000,
    COOLDOWN_EXORCISMO_MASSA: 40000,

    // Chance de erro comico
    ERRO_CHANCE: 0.10,  // 10%

    // Knockback reduzido
    HIT_KNOCKBACK_MULTIPLIER: 0.5,

    // Hit flash cor (dourado ao inves de vermelho)
    HIT_FLASH_COLOR: 0xFFD700,
};
```

---

## 2. CICLOS DE ANIMACAO -- Definicoes Phaser 3

### 2.1 IDLE

```javascript
// create()
this.anims.create({
    key: 'daciolo-idle-down',
    frames: this.anims.generateFrameNumbers('daciolo-idle-down', { start: 0, end: 3 }),
    frameRate: DACIOLO_ANIM.IDLE_FPS,
    repeat: -1  // loop infinito
});
// Repetir para idle-up, idle-left, idle-right
```

**Ciclo**: 0 -> 1 -> 2 -> 3 -> 0 (loop)

**Timing**:
- Frame 0: 125ms (base)
- Frame 1: 125ms (giro)
- Frame 2: 125ms (boca abre)
- Frame 3: 125ms (tremble + sorriso)
- Ciclo completo: 500ms

**Efeitos sobrepostos no idle**:
```javascript
// Fumaca permanente nas maos (particle emitter)
const fumacaIdleEmitter = this.add.particles('fumaca-particle').createEmitter({
    x: { min: -4, max: 4 },   // offset das maos
    y: { min: -8, max: -4 },
    speed: { min: 5, max: 15 },
    angle: { min: 250, max: 290 },  // sobe
    scale: { start: 0.3, end: 0 },
    alpha: { start: 0.6, end: 0 },
    tint: [0xFFD700, 0xFFFFFF],  // dourado -> branco
    lifespan: 800,
    frequency: 200,  // uma particula a cada 200ms (idle calmo)
    quantity: 1
});

// Aureola glow pulsante (overlay sprite)
this.tweens.add({
    targets: aureola,
    alpha: { from: 0.7, to: 1.0 },
    duration: 600,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});

// Micro-grito aleatorio (10% chance a cada ciclo de idle)
this.time.addEvent({
    delay: 2000,  // check a cada 2s
    callback: () => {
        if (Math.random() < 0.10) {
            this.triggerMicroGrito();  // flash branco 1 frame + boca abre
        }
    },
    loop: true
});
```

**Micro-grito (idle event)**:
```javascript
triggerMicroGrito() {
    // Flash branco 1 frame
    this.cameras.main.flash(50, 255, 255, 255, false, 0.3);
    // Forcar frame de boca aberta por 100ms
    daciolo.anims.pause();
    daciolo.setFrame(2);  // frame de boca aberta
    this.time.delayedCall(100, () => {
        daciolo.anims.resume();
    });
    // Aureola flash
    aureola.setAlpha(1.5);  // over-bright momentaneo
    this.tweens.add({
        targets: aureola,
        alpha: 1.0,
        duration: 200
    });
}
```

---

### 2.2 WALK

```javascript
this.anims.create({
    key: 'daciolo-walk-down',
    frames: this.anims.generateFrameNumbers('daciolo-walk-down', { start: 0, end: 5 }),
    frameRate: DACIOLO_ANIM.WALK_FPS,
    repeat: -1
});
```

**Ciclo**: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0 (loop)

**Timing**:
- Cada frame: 100ms
- Ciclo completo: 600ms
- Velocidade de movimento: 120 px/s (determinado, nao rapido)

**Efeitos sobrepostos no walk**:
```javascript
// Fumaca trail (intensificada vs idle)
const fumacaWalkEmitter = this.add.particles('fumaca-particle').createEmitter({
    follow: daciolo,
    followOffset: { x: 0, y: -10 },
    speed: { min: 10, max: 25 },
    angle: { min: 170, max: 190 },  // trail para tras
    scale: { start: 0.4, end: 0 },
    alpha: { start: 0.5, end: 0 },
    tint: [0xFFD700, 0xFFFFFF],
    lifespan: 600,
    frequency: 100,  // mais frequente que idle
    quantity: 1
});

// Rosario pendulo (physics simples)
this.tweens.add({
    targets: rosario,
    angle: { from: -10, to: 10 },
    duration: 300,  // sincronizado com meio ciclo de walk
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});

// Aureola wobble com movimento
this.tweens.add({
    targets: aureola,
    x: { from: -2, to: 2 },
    duration: 300,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

---

### 2.3 ATTACK -- Biblia Sagrada

```javascript
this.anims.create({
    key: 'daciolo-attack-down',
    frames: this.anims.generateFrameNumbers('daciolo-attack-down', { start: 0, end: 2 }),
    frameRate: DACIOLO_ANIM.ATTACK_FPS,
    repeat: 0  // single play
});
```

**Ciclo**: 0 -> 1 -> 2 (fim, volta a idle)

**Timing**:
- Frame 0 (Wind-up): 83ms
- Frame 1 (Strike): 83ms
- Frame 2 (Impact): 83ms + 200ms hold
- Total: ~450ms incluindo hold

**Transicao**: Attack -> Idle (imediato apos hold do frame 2)

**Efeitos de impacto (frame 2)**:
```javascript
onAttackImpact() {
    // Screen shake
    this.cameras.main.shake(100, 0.003);

    // Paginas da Biblia voando (particulas)
    const paginasEmitter = this.add.particles('pagina-biblia').createEmitter({
        x: impactPoint.x,
        y: impactPoint.y,
        speed: { min: 40, max: 100 },
        angle: { min: 0, max: 360 },
        scale: { start: 0.5, end: 0.1 },
        alpha: { start: 1, end: 0 },
        rotate: { min: 0, max: 360 },
        lifespan: 800,
        quantity: 5,
        maxParticles: 5  // burst unico
    });

    // Flash dourado no ponto de impacto
    const flashImpact = this.add.circle(impactPoint.x, impactPoint.y, 12, 0xFFD700, 0.8);
    this.tweens.add({
        targets: flashImpact,
        alpha: 0,
        scale: 2,
        duration: 200,
        onComplete: () => flashImpact.destroy()
    });

    // Ondas de choque
    for (let i = 0; i < 3; i++) {
        this.time.delayedCall(i * 50, () => {
            const ring = this.add.circle(impactPoint.x, impactPoint.y, 4, 0xFFD700, 0);
            ring.setStrokeStyle(1, 0xFFD700, 0.8 - i * 0.2);
            this.tweens.add({
                targets: ring,
                radius: 20 + i * 8,
                alpha: 0,
                duration: 300,
                onComplete: () => ring.destroy()
            });
        });
    }

    // Cruz de luz momentanea
    const cruz = this.add.text(impactPoint.x, impactPoint.y, '+', {
        fontSize: '16px', color: '#FFD700', fontStyle: 'bold'
    }).setOrigin(0.5);
    this.tweens.add({
        targets: cruz,
        alpha: 0,
        scale: 2,
        duration: 300,
        onComplete: () => cruz.destroy()
    });

    // SFX
    this.sound.play('gloria-a-deus', {
        volume: Phaser.Math.FloatBetween(0.6, 1.0),  // intensidade aleatoria
        rate: Phaser.Math.FloatBetween(0.9, 1.1)      // pitch variation
    });
}
```

---

### 2.4 DEATH -- Ascensao Divina

```javascript
this.anims.create({
    key: 'daciolo-death',
    frames: this.anims.generateFrameNumbers('daciolo-death', { start: 0, end: 3 }),
    frameRate: DACIOLO_ANIM.DEATH_FPS,
    repeat: 0
});
```

**Ciclo**: 0 -> 1 -> 2 -> 3 (hold frame 3 indefinidamente)

**Timing**:
- Frame 0 (Golpe): 167ms
- Frame 1 (Elevacao): 500ms (lento, dramatico)
- Frame 2 (Transfiguracao): 500ms
- Frame 3 (Partida): hold indefinido ate respawn
- Total pre-hold: ~1170ms

**Transicoes e efeitos**:
```javascript
onDacioloDeath() {
    daciolo.play('daciolo-death');

    // Frame 0: Biblia cai (spawn objeto fisico)
    this.time.delayedCall(0, () => {
        const bibliaCaida = this.physics.add.sprite(daciolo.x + 8, daciolo.y + 16, 'biblia-ground');
        bibliaCaida.setVelocityX(30);
        bibliaCaida.setVelocityY(20);
        bibliaCaida.setAngularVelocity(90);
        bibliaCaida.setBounce(0.3);
    });

    // Frame 1: Raios de luz descendo
    this.time.delayedCall(167, () => {
        for (let i = 0; i < 5; i++) {
            const ray = this.add.line(
                0, 0,
                daciolo.x + Phaser.Math.Between(-20, 20), 0,
                daciolo.x + Phaser.Math.Between(-10, 10), daciolo.y,
                0xFFD700, 0.6
            );
            ray.setLineWidth(2);
            this.tweens.add({
                targets: ray,
                alpha: { from: 0, to: 0.8 },
                duration: 300,
                yoyo: true,
                repeat: 3
            });
        }

        // Levitacao
        this.tweens.add({
            targets: daciolo,
            y: daciolo.y - 20,
            duration: 2000,
            ease: 'Quad.easeOut'
        });
    });

    // Frame 2: Translucidez + raios multiplicam
    this.time.delayedCall(667, () => {
        this.tweens.add({
            targets: daciolo,
            alpha: 0.7,
            duration: 500
        });
        // Notas musicais douradas
        for (let i = 0; i < 8; i++) {
            this.time.delayedCall(i * 100, () => {
                const nota = this.add.text(
                    daciolo.x + Phaser.Math.Between(-16, 16),
                    daciolo.y + Phaser.Math.Between(-20, 0),
                    Phaser.Utils.Array.GetRandom(['♪', '♫', '♬']),
                    { fontSize: '8px', color: '#FFD700' }
                ).setOrigin(0.5);
                this.tweens.add({
                    targets: nota,
                    y: nota.y - 30,
                    alpha: 0,
                    duration: 1000,
                    onComplete: () => nota.destroy()
                });
            });
        }
    });

    // Frame 3: Coluna de luz + desaparecimento
    this.time.delayedCall(1167, () => {
        // Coluna de luz
        const coluna = this.add.rectangle(daciolo.x, daciolo.y - 50, 16, 120, 0xFFD700, 0.6);
        this.tweens.add({
            targets: coluna,
            alpha: { from: 0, to: 0.8 },
            duration: 500,
            yoyo: true,
            hold: 1000,
            onComplete: () => coluna.destroy()
        });

        // Sprite desaparece
        this.tweens.add({
            targets: daciolo,
            alpha: 0.1,
            duration: 800
        });

        // Biblia + rosario formam cruz no chao
        const bibliaCruz = this.add.sprite(daciolo.x, daciolo.y + 20, 'biblia-rosario-cruz');
        bibliaCruz.setAlpha(0);
        this.tweens.add({
            targets: bibliaCruz,
            alpha: 1,
            duration: 500
        });

        // Particulas de luz (vagalumes divinos) -- continuam 2s apos
        const vagalumes = this.add.particles('light-particle').createEmitter({
            x: daciolo.x,
            y: daciolo.y,
            speed: { min: 10, max: 30 },
            angle: { min: 250, max: 290 },
            scale: { start: 0.3, end: 0 },
            alpha: { start: 0.8, end: 0 },
            tint: [0xFFD700, 0xFFFFFF, 0x87CEEB],
            lifespan: 1500,
            frequency: 100,
            quantity: 2
        });
        this.time.delayedCall(DACIOLO_ANIM.DEATH_PARTICLES_AFTER, () => {
            vagalumes.stop();
        });

        // Buff para aliados proximos
        this.applyInspiracaoDivina(daciolo.x, daciolo.y, 150);
    });
}

// Respawn (inverso da death)
onDacioloRespawn(x, y) {
    daciolo.setPosition(x, y - 40);
    daciolo.setAlpha(0.1);

    // Coluna de luz desce
    const coluna = this.add.rectangle(x, y - 50, 16, 120, 0xFFD700, 0.6);
    this.tweens.add({
        targets: coluna,
        alpha: { from: 0.8, to: 0 },
        duration: 1000,
        onComplete: () => coluna.destroy()
    });

    // Daciolo desce e materializa
    this.tweens.add({
        targets: daciolo,
        y: y,
        alpha: 1,
        duration: 1000,
        ease: 'Quad.easeIn',
        onComplete: () => {
            daciolo.play('daciolo-idle-down');
        }
    });
}
```

---

### 2.5 HIT -- Fe Inabalavel

```javascript
this.anims.create({
    key: 'daciolo-hit',
    frames: this.anims.generateFrameNumbers('daciolo-hit', { start: 0, end: 1 }),
    frameRate: DACIOLO_ANIM.HIT_FPS,
    repeat: 0
});
```

**Ciclo**: 0 -> 1 (volta a animacao anterior)

**Timing**:
- Frame 0: 83ms
- Frame 1: 83ms
- Total: 166ms (RAPIDO -- fe inabalavel, recuperacao instantanea)

**Efeitos**:
```javascript
onDacioloHit() {
    // Interrupcao minima
    daciolo.play('daciolo-hit');

    // Flash DOURADO (nao vermelho)
    daciolo.setTint(DACIOLO_ANIM.HIT_FLASH_COLOR);
    this.time.delayedCall(100, () => daciolo.clearTint());

    // Knockback REDUZIDO
    const knockbackForce = baseKnockback * DACIOLO_ANIM.HIT_KNOCKBACK_MULTIPLIER;

    // Burst de fumaca defensiva
    const fumacaBurst = this.add.particles('fumaca-particle').createEmitter({
        x: daciolo.x,
        y: daciolo.y - 16,
        speed: { min: 20, max: 50 },
        angle: { min: 0, max: 360 },
        scale: { start: 0.5, end: 0 },
        alpha: { start: 0.7, end: 0 },
        tint: [0xFFD700],
        lifespan: 400,
        quantity: 8,
        maxParticles: 8
    });

    // Apos animacao de hit, voltar a animacao anterior
    daciolo.on('animationcomplete-daciolo-hit', () => {
        daciolo.play(previousAnimation);
    });

    // Contador de hits consecutivos
    this.dacioloConsecutiveHits++;
    this.time.delayedCall(2000, () => { this.dacioloConsecutiveHits = 0; });
    if (this.dacioloConsecutiveHits >= 3) {
        this.triggerDacioloQuote('sinto-cheiro-satanas');
        // "Sinto o cheiro de Satanas neste recinto!"
    }
}
```

---

### 2.6 SPECIAL: Fumaca Santa

```javascript
this.anims.create({
    key: 'daciolo-fumaca-santa',
    frames: this.anims.generateFrameNumbers('daciolo-special-fumaca', { start: 0, end: 7 }),
    frameRate: DACIOLO_ANIM.SPECIAL_FUMACA_FPS,
    repeat: 0
});
```

**Ciclo**: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (fim)

**Timing detalhado**:
- Frame 0 (Preparacao): 200ms (estendido, build-up)
- Frame 1 (Concentracao): 150ms
- Frame 2 (Elevacao): 150ms
- Frame 3 (Detonacao): 100ms (RAPIDO -- explosao)
- Frame 4 (Expansao 1): 100ms
- Frame 5 (Expansao 2): 100ms
- Frame 6 (Pico): 200ms (hold no pico)
- Frame 7 (Dissipacao): 300ms (lento, voltando)
- Total sprite: ~1300ms
- Efeito de particula continua apos: +1500ms

**Sequencia completa de efeitos**:
```javascript
onFumacaSanta() {
    daciolo.play('daciolo-fumaca-santa');

    // === FRAME 0-1: Build-up ===
    // Particulas sendo puxadas PARA Daciolo (vacuum)
    const vacuumEmitter = this.add.particles('light-particle').createEmitter({
        x: { min: daciolo.x - 60, max: daciolo.x + 60 },
        y: { min: daciolo.y - 60, max: daciolo.y + 60 },
        moveToX: daciolo.x,
        moveToY: daciolo.y - 16,
        speed: 60,
        scale: { start: 0.3, end: 0 },
        alpha: { start: 0.5, end: 0 },
        tint: [0xFFD700, 0x87CEEB],
        lifespan: 500,
        frequency: 30,
        quantity: 3
    });

    // Aureola spin
    this.tweens.add({
        targets: aureola,
        angle: 360,
        duration: 800,
        repeat: 1
    });

    // === FRAME 2: Levitacao ===
    this.time.delayedCall(350, () => {
        this.tweens.add({
            targets: daciolo,
            y: daciolo.y - 10,
            duration: 300,
            ease: 'Back.easeOut'
        });
    });

    // === FRAME 3: DETONACAO ===
    this.time.delayedCall(500, () => {
        vacuumEmitter.stop();

        // Flash branco
        this.cameras.main.flash(150, 255, 255, 255, false, 0.8);

        // Fumaca santa expandindo (particle emitter principal)
        const fumacaSantaEmitter = this.add.particles('fumaca-santa-particle').createEmitter({
            x: daciolo.x,
            y: daciolo.y - 10,
            speed: { min: 30, max: 80 },
            angle: { min: 0, max: 360 },
            scale: { start: 0.8, end: 2.5 },
            alpha: { start: 0.7, end: 0 },
            tint: [0xFFD700, 0xFFFFFF, 0xFFA500],
            lifespan: 2000,
            frequency: 20,
            quantity: 8,
            radial: true
        });

        // Camera zoom out
        this.cameras.main.zoomTo(0.8, 500);

        // SFX
        this.sound.play('fumaca-santa-sfx');
        this.sound.play('coro-anjos', { volume: 0.5, delay: 0.2 });

        // Dano AoE expandindo
        const fumacaRadius = { value: 0 };
        this.tweens.add({
            targets: fumacaRadius,
            value: 200,  // raio maximo em pixels
            duration: 1500,
            ease: 'Quad.easeOut',
            onUpdate: () => {
                this.applyFumacaDamage(daciolo.x, daciolo.y, fumacaRadius.value);
            }
        });

        // Parar e limpar apos expansao
        this.time.delayedCall(2000, () => {
            fumacaSantaEmitter.stop();
        });

        // === FRAME 7: Dissipacao ===
        this.time.delayedCall(1800, () => {
            // Camera volta
            this.cameras.main.zoomTo(1.0, 500);

            // Daciolo desce
            this.tweens.add({
                targets: daciolo,
                y: daciolo.y + 10,
                duration: 400,
                ease: 'Quad.easeIn'
            });

            // Aureola dim (cooldown visual)
            this.tweens.add({
                targets: aureola,
                alpha: 0.3,
                duration: 500
            });
            this.time.delayedCall(DACIOLO_ANIM.AUREOLA_DIM_AFTER_FUMACA, () => {
                this.tweens.add({
                    targets: aureola,
                    alpha: 1.0,
                    duration: 2000
                });
            });

            // Marcas no chao
            const groundMarks = this.add.circle(daciolo.x, daciolo.y, 200, 0xFFD700, 0.2);
            this.tweens.add({
                targets: groundMarks,
                alpha: 0,
                duration: 5000,
                onComplete: () => groundMarks.destroy()
            });
        });
    });
}

// Destruicao de zumbis pela fumaca: viram PO DOURADO
applyFumacaDamage(cx, cy, radius) {
    this.enemies.getChildren().forEach(enemy => {
        const dist = Phaser.Math.Distance.Between(cx, cy, enemy.x, enemy.y);
        if (dist <= radius && enemy.active) {
            // Zumbi vira po dourado
            const poEmitter = this.add.particles('gold-dust').createEmitter({
                x: enemy.x,
                y: enemy.y,
                speed: { min: 10, max: 40 },
                angle: { min: 0, max: 360 },
                scale: { start: 0.5, end: 0 },
                tint: [0xFFD700, 0xFFA500],
                lifespan: 600,
                quantity: 12,
                maxParticles: 12
            });
            enemy.destroy();
        }
    });
}
```

---

### 2.7 SPECIAL: GLORIA A DEUS!

```javascript
this.anims.create({
    key: 'daciolo-gloria',
    frames: this.anims.generateFrameNumbers('daciolo-special-gloria', { start: 0, end: 5 }),
    frameRate: DACIOLO_ANIM.SPECIAL_GLORIA_FPS,
    repeat: 0
});
```

**Ciclo**: 0 -> 1 -> 2 -> 3 -> 4 -> 5 (fim)

**Timing**:
- Frame 0: 150ms (inspiracao)
- Frame 1: 150ms (build-up)
- Frame 2: 100ms (GLOOO-)
- Frame 3: 100ms (-ORIA A)
- Frame 4: 100ms (DEUS!!! -- pico)
- Frame 5: 200ms (eco)
- Total: ~800ms

**Sistema de 10% de falha**:
```javascript
onGloriaADeus(direction) {
    // Rolar chance de erro
    if (Math.random() < DACIOLO_ANIM.ERRO_CHANCE) {
        this.onErroComico();
        return;
    }

    daciolo.play('daciolo-gloria');

    // === FRAMES 0-1: Build-up ===
    // Inflacao do peito (scale tween)
    this.tweens.add({
        targets: daciolo,
        scaleX: 1.15,
        duration: 200,
        yoyo: true,
        ease: 'Back.easeOut'
    });

    // Vacuum de particulas
    const vacuum = this.add.particles('light-particle').createEmitter({
        x: { min: daciolo.x - 40, max: daciolo.x + 40 },
        y: { min: daciolo.y - 40, max: daciolo.y + 40 },
        moveToX: daciolo.x,
        moveToY: daciolo.y,
        speed: 40,
        scale: { start: 0.2, end: 0 },
        tint: 0xFFD700,
        lifespan: 300,
        frequency: 50,
        quantity: 2
    });

    // === FRAME 2-4: SHOCKWAVES ===
    this.time.delayedCall(300, () => {
        vacuum.stop();

        // Calcular cone de direcao
        const coneAngle = this.getDirectionAngle(direction);
        const coneSpread = 30;  // 60 graus total

        // Gerar 5 ondas de choque com delay
        for (let i = 0; i < 5; i++) {
            this.time.delayedCall(i * 60, () => {
                const ring = this.add.circle(daciolo.x, daciolo.y, 8, 0xFFD700, 0);
                ring.setStrokeStyle(2 - i * 0.3, 0xFFD700, 0.9 - i * 0.15);
                this.tweens.add({
                    targets: ring,
                    radius: 60 + i * 15,
                    alpha: 0,
                    x: ring.x + Math.cos(coneAngle) * (60 + i * 15),
                    y: ring.y + Math.sin(coneAngle) * (60 + i * 15),
                    duration: 400,
                    onComplete: () => ring.destroy()
                });
            });
        }

        // Flash no pico (frame 4)
        this.time.delayedCall(200, () => {
            this.cameras.main.flash(80, 255, 255, 255, false, 0.5);
        });

        // Stun em inimigos no cone
        this.enemies.getChildren().forEach(enemy => {
            if (this.isInCone(daciolo, enemy, coneAngle, coneSpread, 120)) {
                this.stunEnemy(enemy, DACIOLO_ANIM.STUN_DURATION);
            }
        });

        // SFX
        this.sound.play('gloria-a-deus-full', { volume: 1.0 });

        // Aureola tamanho 3x
        this.tweens.add({
            targets: aureola,
            scale: 3,
            duration: 200,
            yoyo: true,
            hold: 100
        });
    });

    // === FRAME 5: Eco ===
    this.time.delayedCall(700, () => {
        // Linhas de calor no ar
        for (let i = 0; i < 4; i++) {
            const heatLine = this.add.graphics();
            heatLine.lineStyle(1, 0xFFD700, 0.3);
            const startX = daciolo.x + Phaser.Math.Between(-20, 20);
            const startY = daciolo.y + Phaser.Math.Between(-20, 0);
            heatLine.beginPath();
            heatLine.moveTo(startX, startY);
            for (let j = 0; j < 5; j++) {
                heatLine.lineTo(
                    startX + j * 6 + Phaser.Math.Between(-2, 2),
                    startY + Phaser.Math.Between(-3, 3)
                );
            }
            heatLine.strokePath();
            this.tweens.add({
                targets: heatLine,
                alpha: 0,
                y: '-=10',
                duration: 800,
                onComplete: () => heatLine.destroy()
            });
        }
    });
}
```

---

### 2.8 SPECIAL: Exorcismo Eleitoral

```javascript
this.anims.create({
    key: 'daciolo-exorcismo',
    frames: this.anims.generateFrameNumbers('daciolo-special-exorcismo', { start: 0, end: 5 }),
    frameRate: DACIOLO_ANIM.SPECIAL_EXORCISMO_FPS,
    repeat: 0
});
```

**Ciclo**: 0 -> 1 -> 2 -> 3 -> 4 -> 5 (fim)

**Timing**:
- Cada frame: 125ms
- Total: 750ms + efeitos residuais

**Efeitos de cura**:
```javascript
onExorcismoEleitoral() {
    daciolo.play('daciolo-exorcismo');

    // Raios de luz da palma (frame 1-3)
    this.time.delayedCall(125, () => {
        // Raios finos dourados
        for (let i = 0; i < 6; i++) {
            const angle = Phaser.Math.DegToRad(daciolo.angle + Phaser.Math.Between(-30, 30));
            const rayLength = 40;
            const ray = this.add.line(0, 0,
                daciolo.x + 10, daciolo.y - 8,
                daciolo.x + 10 + Math.cos(angle) * rayLength,
                daciolo.y - 8 + Math.sin(angle) * rayLength,
                0xFFD700, 0.7
            );
            ray.setLineWidth(1);
            this.tweens.add({
                targets: ray,
                alpha: 0,
                duration: 600,
                delay: i * 50,
                onComplete: () => ray.destroy()
            });
        }
    });

    // Cruz de luz (frame 2-3)
    this.time.delayedCall(250, () => {
        const cruzH = this.add.rectangle(daciolo.x + 20, daciolo.y - 8, 20, 4, 0xFFD700, 0.8);
        const cruzV = this.add.rectangle(daciolo.x + 20, daciolo.y - 8, 4, 20, 0xFFD700, 0.8);
        this.tweens.add({
            targets: [cruzH, cruzV],
            alpha: 0,
            scale: 2,
            angle: 90,
            duration: 500,
            delay: 300,
            onComplete: () => { cruzH.destroy(); cruzV.destroy(); }
        });
    });

    // Cura em area (frame 3-4)
    this.time.delayedCall(375, () => {
        this.allies.getChildren().forEach(ally => {
            const dist = Phaser.Math.Distance.Between(daciolo.x, daciolo.y, ally.x, ally.y);
            if (dist <= 100) {
                // Cura 25% HP
                ally.heal(ally.maxHP * 0.25);

                // Numero verde subindo
                const healNum = this.add.text(ally.x, ally.y - 16, `+${Math.floor(ally.maxHP * 0.25)}`, {
                    fontSize: '10px', color: '#32CD32', fontStyle: 'bold'
                }).setOrigin(0.5);
                this.tweens.add({
                    targets: healNum,
                    y: healNum.y - 20,
                    alpha: 0,
                    duration: 800,
                    onComplete: () => healNum.destroy()
                });

                // Remove debuffs
                ally.clearAllDebuffs();

                // Aura de cura
                const curaAura = this.add.circle(ally.x, ally.y, 16, 0x32CD32, 0.3);
                this.tweens.add({
                    targets: curaAura,
                    alpha: 0,
                    scale: 1.5,
                    duration: 1000,
                    onComplete: () => curaAura.destroy()
                });
            }
        });

        // SFX
        this.sound.play('queima-jesus');
        this.sound.play('sino-igreja', { volume: 0.3, delay: 0.3 });
    });

    // Glow residual nos aliados (frame 5-6)
    this.time.delayedCall(625, () => {
        this.allies.getChildren().forEach(ally => {
            ally.setTint(0xFFD700);
            this.time.delayedCall(DACIOLO_ANIM.CURA_GLOW_DURATION, () => {
                ally.clearTint();
            });
        });
    });
}
```

---

### 2.9 SPECIAL: Monte Roraima Sagrado

**Ciclo**: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> [6 <-> 7 loop durante duracao] -> 7 (fim)

**Timing**:
- Frames 0-5: 100ms cada = 600ms (emergencia)
- Frames 6-7: loop durante 4000ms (chuva de fogo)
- Frame 7 final: 300ms (descida)
- Total: ~4900ms + efeitos

```javascript
onMonteRoraima() {
    daciolo.play('daciolo-special-roraima');

    // Screen shake durante emergencia (frames 1-3)
    this.time.delayedCall(100, () => {
        this.cameras.main.shake(1500, 0.005);
    });

    // Particulas de terra/rocha (frames 2-4)
    this.time.delayedCall(200, () => {
        const rochasEmitter = this.add.particles('rocha-particle').createEmitter({
            x: daciolo.x,
            y: daciolo.y + 20,
            speed: { min: 30, max: 80 },
            angle: { min: 220, max: 320 },
            scale: { start: 0.5, end: 0.1 },
            tint: [0x8B4513, 0x696969, 0x556B2F],
            lifespan: 1000,
            frequency: 30,
            quantity: 3
        });
        this.time.delayedCall(1200, () => rochasEmitter.stop());
    });

    // Montanha sprite (separado, ver monte-roraima-surgindo.md)
    this.time.delayedCall(200, () => {
        const montanha = this.add.sprite(daciolo.x, daciolo.y + 32, 'monte-roraima');
        montanha.play('monte-roraima-emerge');

        // Daciolo sobe com a montanha
        this.tweens.add({
            targets: daciolo,
            y: daciolo.y - 30,
            duration: 1500,
            ease: 'Back.easeOut'
        });

        // Chuva de fogo (frames 6-7 loop)
        this.time.delayedCall(1500, () => {
            const fogoEmitter = this.add.particles('fogo-santo').createEmitter({
                x: { min: daciolo.x - 80, max: daciolo.x + 80 },
                y: daciolo.y - 40,
                speed: { min: 40, max: 80 },
                angle: { min: 80, max: 100 },  // cai para baixo
                scale: { start: 0.6, end: 0.2 },
                tint: [0xFFD700, 0xFFA500, 0xFF6600],
                lifespan: 800,
                frequency: 60,
                quantity: 2
            });

            // Impactos de cruz no chao
            this.time.addEvent({
                delay: 200,
                callback: () => {
                    const impactX = daciolo.x + Phaser.Math.Between(-80, 80);
                    const impactY = daciolo.y + Phaser.Math.Between(20, 60);
                    const cruz = this.add.text(impactX, impactY, '+', {
                        fontSize: '12px', color: '#FFD700', fontStyle: 'bold'
                    }).setOrigin(0.5);
                    this.tweens.add({
                        targets: cruz,
                        alpha: 0, scale: 2,
                        duration: 500,
                        onComplete: () => cruz.destroy()
                    });
                    // Dano AoE no ponto
                    this.applyPointDamage(impactX, impactY, 20, 30);
                },
                repeat: Math.floor(DACIOLO_ANIM.RORAIMA_FIRE_LOOP_DURATION / 200),
                callbackScope: this
            });

            // Parar chuva apos duracao
            this.time.delayedCall(DACIOLO_ANIM.RORAIMA_FIRE_LOOP_DURATION, () => {
                fogoEmitter.stop();

                // Montanha afunda
                this.tweens.add({
                    targets: montanha,
                    y: montanha.y + 64,
                    alpha: 0,
                    duration: 1000,
                    onComplete: () => montanha.destroy()
                });

                // Daciolo desce
                this.tweens.add({
                    targets: daciolo,
                    y: daciolo.y + 30,
                    duration: 800,
                    ease: 'Quad.easeIn'
                });

                // Cratera com marca de cruz
                const cratera = this.add.sprite(daciolo.x, daciolo.y + 32, 'cratera-cruz');
                this.tweens.add({
                    targets: cratera,
                    alpha: 0,
                    duration: 5000,
                    delay: 2000,
                    onComplete: () => cratera.destroy()
                });
            });
        });
    });

    // SFX
    this.sound.play('terremoto', { volume: 0.7 });
    this.time.delayedCall(1500, () => {
        this.sound.play('coro-anjos', { volume: 0.4 });
        this.sound.play('vento-forte', { volume: 0.5 });
    });
}
```

---

### 2.10 SPECIAL: URSAL Cataclismica (Ultimate)

**Ciclo**: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (fim)

**Timing**:
- Frame 0: 200ms (revelacao)
- Frame 1: 250ms (sombra)
- Frame 2: 200ms (descida 1)
- Frame 3: 200ms (descida 2)
- Frame 4: 100ms (IMPACTO)
- Frame 5: 200ms (devastacao)
- Frame 6: 300ms (aftermath)
- Frame 7: 300ms (victoria)
- Total: ~1750ms

```javascript
onURSALCataclismica() {
    daciolo.play('daciolo-special-ursal');

    // === FRAME 0: Revelacao ===
    this.sound.play('daciolo-a-ursal-existe');

    // === FRAME 1: Sombra crescente ===
    this.time.delayedCall(200, () => {
        const sombra = this.add.ellipse(daciolo.x, daciolo.y, 10, 8, 0x000000, 0.3);
        this.tweens.add({
            targets: sombra,
            scaleX: 25,
            scaleY: 20,
            duration: 1000,
            ease: 'Quad.easeIn'
        });

        // Ceu escurece
        const darkOverlay = this.add.rectangle(
            this.cameras.main.centerX, this.cameras.main.centerY,
            this.cameras.main.width, this.cameras.main.height,
            0x000000, 0
        ).setScrollFactor(0).setDepth(100);
        this.tweens.add({
            targets: darkOverlay,
            alpha: 0.4,
            duration: 800
        });
    });

    // === FRAMES 2-3: Mapa descendo ===
    this.time.delayedCall(450, () => {
        const mapaURSAL = this.add.sprite(daciolo.x, -100, 'ursal-map');
        mapaURSAL.setDepth(101);
        mapaURSAL.setScale(0.5);

        this.tweens.add({
            targets: mapaURSAL,
            y: daciolo.y,
            scale: 2,
            duration: 600,
            ease: 'Quad.easeIn',
            onComplete: () => {
                // === FRAME 4: IMPACTO ===
                // Flash
                this.cameras.main.flash(200, 255, 255, 255, false, 1.0);
                // Screen shake MAXIMO
                this.cameras.main.shake(500, 0.01);
                // Camera zoom out
                this.cameras.main.zoomTo(0.6, 300);

                // Onda de choque
                for (let i = 0; i < 4; i++) {
                    this.time.delayedCall(i * 80, () => {
                        const shockRing = this.add.circle(daciolo.x, daciolo.y, 10, 0xFFD700, 0);
                        shockRing.setStrokeStyle(3 - i * 0.5, 0xFFD700, 0.9 - i * 0.2);
                        shockRing.setDepth(102);
                        this.tweens.add({
                            targets: shockRing,
                            radius: 150 + i * 30,
                            alpha: 0,
                            duration: 500,
                            onComplete: () => shockRing.destroy()
                        });
                    });
                }

                // Fragmentos de mapa voando
                for (let i = 0; i < 15; i++) {
                    const frag = this.add.rectangle(
                        daciolo.x + Phaser.Math.Between(-10, 10),
                        daciolo.y + Phaser.Math.Between(-10, 10),
                        Phaser.Math.Between(3, 8),
                        Phaser.Math.Between(3, 8),
                        Phaser.Utils.Array.GetRandom([0xCC0000, 0x008000, 0xFFD700]),
                        0.8
                    );
                    frag.setDepth(102);
                    this.tweens.add({
                        targets: frag,
                        x: frag.x + Phaser.Math.Between(-80, 80),
                        y: frag.y + Phaser.Math.Between(-80, 80),
                        alpha: 0,
                        angle: Phaser.Math.Between(0, 720),
                        duration: 1000,
                        onComplete: () => frag.destroy()
                    });
                }

                // Eliminar TODOS inimigos na area
                this.enemies.getChildren().forEach(enemy => {
                    const dist = Phaser.Math.Distance.Between(daciolo.x, daciolo.y, enemy.x, enemy.y);
                    if (dist <= 250) {
                        // Particulas de destruicao
                        const destroyEmitter = this.add.particles('debris').createEmitter({
                            x: enemy.x, y: enemy.y,
                            speed: { min: 30, max: 70 },
                            angle: { min: 0, max: 360 },
                            scale: { start: 0.4, end: 0 },
                            lifespan: 500,
                            quantity: 6,
                            maxParticles: 6
                        });
                        enemy.destroy();
                    }
                });

                // Mapa desaparece, cratera fica
                this.tweens.add({
                    targets: mapaURSAL,
                    alpha: 0,
                    duration: 300,
                    delay: 200,
                    onComplete: () => mapaURSAL.destroy()
                });

                // Letras URSAL piscando no centro
                const ursalText = this.add.text(daciolo.x, daciolo.y, 'URSAL', {
                    fontSize: '16px', color: '#CC0000', fontStyle: 'bold',
                    stroke: '#000000', strokeThickness: 2
                }).setOrigin(0.5).setDepth(102);

                this.tweens.add({
                    targets: ursalText,
                    alpha: { from: 1, to: 0.3 },
                    duration: 200,
                    yoyo: true,
                    repeat: 10,
                    onComplete: () => {
                        this.tweens.add({
                            targets: ursalText,
                            alpha: 0,
                            duration: 500,
                            onComplete: () => ursalText.destroy()
                        });
                    }
                });

                // === FRAMES 6-7: Aftermath + Victoria ===
                this.time.delayedCall(500, () => {
                    // Camera volta
                    this.cameras.main.zoomTo(1.0, 800);
                    // Overlay escuro remove
                    // daciolo: "EU AVISEI!"
                    this.triggerDacioloQuote('eu-avisei-ursal');
                });

                // SFX
                this.sound.play('sirene-alerta', { volume: 0.6 });
                this.sound.play('trovao', { volume: 0.8, delay: 0.1 });
                this.sound.play('impacto-nuclear', { volume: 1.0, delay: 0.15 });
            }
        });
    });
}
```

---

### 2.11 SPECIAL: Candidatura Divina 2026

```javascript
onCandidaturaDivina(direction) {
    daciolo.play('daciolo-special-candidatura');

    // Frame 2: Santinho aparece
    this.time.delayedCall(200, () => {
        const santinho = this.add.sprite(daciolo.x + 12, daciolo.y - 8, 'santinho-daciolo');
        santinho.setScale(0.5);

        // Glow divino no santinho
        const santinhoGlow = this.add.circle(santinho.x, santinho.y, 10, 0xFFD700, 0.3);
        this.tweens.add({
            targets: santinhoGlow,
            alpha: { from: 0.3, to: 0.6 },
            scale: { from: 1, to: 1.5 },
            duration: 300,
            yoyo: true,
            repeat: 2
        });

        // Frame 3: Espiral hipnotica
        this.time.delayedCall(200, () => {
            // Espiral dourada
            const espiral = this.add.sprite(santinho.x + 15, santinho.y, 'espiral-hipnotica');
            espiral.play('espiral-spin');

            // Confundir inimigos no raio
            this.enemies.getChildren().forEach(enemy => {
                const dist = Phaser.Math.Distance.Between(daciolo.x, daciolo.y, enemy.x, enemy.y);
                if (dist <= 80) {
                    this.confuseEnemy(enemy, DACIOLO_ANIM.CONFUSAO_DURATION);

                    // "?" sobre inimigo
                    const questionMark = this.add.text(enemy.x, enemy.y - 20, '?', {
                        fontSize: '12px', color: '#FFD700', fontStyle: 'bold'
                    }).setOrigin(0.5);
                    this.tweens.add({
                        targets: questionMark,
                        y: questionMark.y - 10,
                        alpha: { from: 1, to: 0 },
                        duration: DACIOLO_ANIM.CONFUSAO_DURATION,
                        onComplete: () => questionMark.destroy()
                    });
                }
            });

            // SFX
            this.sound.play('jingle-campanha-distorcido', { volume: 0.5 });
            this.sound.play('daciolo-nao-estou-a-venda');
        });

        // Frame 4: Santinho flutua e cai no chao
        this.time.delayedCall(400, () => {
            this.tweens.add({
                targets: santinho,
                y: daciolo.y + 24,
                angle: 360,
                duration: 800,
                ease: 'Bounce.easeOut'
            });
            santinhoGlow.destroy();

            // Santinho no chao (interactable)
            this.time.delayedCall(800, () => {
                santinho.setInteractive();
                santinho.on('pointerdown', () => {
                    // Buff: "Considerando o voto" +5% speed 10s
                    this.applyBuff('considerando-voto', player, 10000);
                    santinho.destroy();
                });
                // Auto-destroy apos tempo
                this.time.delayedCall(DACIOLO_ANIM.SANTINHO_GROUND_DURATION, () => {
                    if (santinho.active) {
                        this.tweens.add({
                            targets: santinho,
                            alpha: 0,
                            duration: 500,
                            onComplete: () => santinho.destroy()
                        });
                    }
                });
            });
        });
    });
}
```

---

### 2.12 SPECIAL: Exorcismo em Massa

```javascript
onExorcismoEmMassa() {
    daciolo.play('daciolo-special-exorcismo-massa');

    // Esfera de luz expandindo
    const esfera = this.add.circle(daciolo.x, daciolo.y, 10, 0xFFD700, 0.2);

    this.tweens.add({
        targets: esfera,
        radius: 150,
        duration: 2000,
        ease: 'Quad.easeOut',
        onUpdate: () => {
            // Curar aliados conforme esfera os alcanca
            this.allies.getChildren().forEach(ally => {
                const dist = Phaser.Math.Distance.Between(daciolo.x, daciolo.y, ally.x, ally.y);
                if (dist <= esfera.radius && !ally.getData('massExorcised')) {
                    ally.setData('massExorcised', true);

                    // Cura 25%
                    ally.heal(ally.maxHP * 0.25);
                    // Remove debuffs
                    ally.clearAllDebuffs();

                    // Visual: flash verde + numero
                    ally.setTint(0xFFFFFF);
                    this.time.delayedCall(100, () => ally.clearTint());

                    const healNum = this.add.text(ally.x, ally.y - 16, `+${Math.floor(ally.maxHP * 0.25)}`, {
                        fontSize: '10px', color: '#32CD32', fontStyle: 'bold'
                    }).setOrigin(0.5);
                    this.tweens.add({
                        targets: healNum,
                        y: healNum.y - 20, alpha: 0,
                        duration: 800,
                        onComplete: () => healNum.destroy()
                    });
                }
            });
        },
        onComplete: () => {
            // Limpar flag
            this.allies.getChildren().forEach(ally => ally.setData('massExorcised', false));

            // Esfera dissipa
            this.tweens.add({
                targets: esfera,
                alpha: 0,
                duration: 500,
                onComplete: () => esfera.destroy()
            });
        }
    });

    // Mandala no chao (frame 5)
    this.time.delayedCall(1200, () => {
        const mandala = this.add.sprite(daciolo.x, daciolo.y, 'mandala-dourada');
        mandala.setAlpha(0);
        this.tweens.add({
            targets: mandala,
            alpha: 0.5,
            angle: 360,
            duration: 2000,
            onComplete: () => {
                this.tweens.add({
                    targets: mandala,
                    alpha: 0,
                    duration: 1000,
                    onComplete: () => mandala.destroy()
                });
            }
        });
    });

    // Notas musicais descendo (coro de anjos)
    for (let i = 0; i < 12; i++) {
        this.time.delayedCall(500 + i * 150, () => {
            const nota = this.add.text(
                daciolo.x + Phaser.Math.Between(-60, 60),
                daciolo.y - 50,
                Phaser.Utils.Array.GetRandom(['♪', '♫', '♬']),
                { fontSize: '8px', color: '#FFD700' }
            ).setOrigin(0.5);
            this.tweens.add({
                targets: nota,
                y: nota.y + 80,
                alpha: 0,
                duration: 1200,
                onComplete: () => nota.destroy()
            });
        });
    }

    // Silhuetas angelicais (frame 7)
    this.time.delayedCall(1800, () => {
        for (let i = 0; i < 3; i++) {
            const anjo = this.add.sprite(
                daciolo.x + Phaser.Math.Between(-40, 40),
                daciolo.y + Phaser.Math.Between(-30, -10),
                'anjo-silhueta'
            );
            anjo.setAlpha(0);
            this.tweens.add({
                targets: anjo,
                alpha: 0.3,
                duration: 300,
                yoyo: true,
                hold: 200,
                onComplete: () => anjo.destroy()
            });
        }
    });

    // Glow residual nos aliados
    this.time.delayedCall(2500, () => {
        this.allies.getChildren().forEach(ally => {
            ally.setTint(0xFFD700);
            this.time.delayedCall(DACIOLO_ANIM.EXORCISMO_MASSA_GLOW_DURATION, () => {
                ally.clearTint();
            });
        });
    });

    // SFX
    this.sound.play('coro-anjos-completo', { volume: 0.7 });
    this.time.delayedCall(2000, () => {
        this.sound.play('daciolo-pela-honra-gloria');
    });
}
```

---

### 2.13 ERRO COMICO

```javascript
this.anims.create({
    key: 'daciolo-erro-comico',
    frames: this.anims.generateFrameNumbers('daciolo-erro-comico', { start: 0, end: 3 }),
    frameRate: DACIOLO_ANIM.ERRO_COMICO_FPS,
    repeat: 0
});

onErroComico() {
    daciolo.play('daciolo-erro-comico');

    // Frame 1: identico ao gloria (player nao sabe que vai falhar)

    // Frame 2: Onda fraca e patetica
    this.time.delayedCall(100, () => {
        const ondaFraca = this.add.circle(daciolo.x, daciolo.y, 5, 0xFFD700, 0);
        ondaFraca.setStrokeStyle(0.5, 0xFFD700, 0.3);
        this.tweens.add({
            targets: ondaFraca,
            radius: 15,  // 30% do normal
            alpha: 0,
            duration: 300,
            ease: 'Sine.easeOut',
            onComplete: () => ondaFraca.destroy()
        });
    });

    // Frame 3: Vergonha
    this.time.delayedCall(200, () => {
        // Aureola APAGA
        this.tweens.add({
            targets: aureola,
            alpha: 0,
            duration: 50,
            yoyo: true,
            hold: 100
        });

        // Gota de suor anime
        const suor = this.add.text(daciolo.x + 10, daciolo.y - 20, '💧', {
            fontSize: '8px'
        });
        this.tweens.add({
            targets: suor,
            y: suor.y + 5,
            alpha: 0,
            duration: 600,
            onComplete: () => suor.destroy()
        });

        // Biblia cai (bounce)
        const bibliaCai = this.add.sprite(daciolo.x + 8, daciolo.y, 'biblia-ground');
        bibliaCai.setVelocityY = 30;
        this.tweens.add({
            targets: bibliaCai,
            y: daciolo.y + 16,
            duration: 200,
            ease: 'Bounce.easeOut'
        });

        // SFX: "Gloria a sap-- opa, Gloria a Deus!"
        this.sound.play('daciolo-erro-gloria');
    });

    // Frame 4: Tentativa de correcao
    this.time.delayedCall(300, () => {
        // Pega biblia de volta (tween)
        // Aureola volta timida (50%)
        this.tweens.add({
            targets: aureola,
            alpha: 0.5,
            duration: 300
        });

        // "?" nos aliados proximos
        this.allies.getChildren().forEach(ally => {
            const dist = Phaser.Math.Distance.Between(daciolo.x, daciolo.y, ally.x, ally.y);
            if (dist <= 60) {
                const q = this.add.text(ally.x, ally.y - 20, '?', {
                    fontSize: '10px', color: '#FFFFFF'
                }).setOrigin(0.5);
                this.tweens.add({
                    targets: q,
                    y: q.y - 10, alpha: 0,
                    duration: 1000,
                    onComplete: () => q.destroy()
                });
            }
        });

        // Se tem boss na tela: boss RI
        this.enemies.getChildren().forEach(enemy => {
            if (enemy.getData('isBoss')) {
                enemy.play('boss-laugh');
            }
        });

        // NENHUM efeito de stun -- skill FALHOU
        // Cooldown normal ainda se aplica (punicao)

        // Recuperar aureola gradualmente
        this.time.delayedCall(3000, () => {
            this.tweens.add({
                targets: aureola,
                alpha: 1.0,
                duration: 2000
            });
        });
    });
}
```

---

## 3. SISTEMA DE TRANSICOES

### Tabela de transicoes permitidas

| De | Para | Tipo | Delay |
|---|---|---|---|
| idle | walk | Imediato | 0ms |
| walk | idle | Imediato | 0ms |
| idle/walk | attack | Interrompe | 0ms |
| attack | idle | Apos complete | ~450ms |
| idle/walk | hit | Interrompe | 0ms |
| hit | (anterior) | Apos complete | ~166ms |
| idle/walk | special (qualquer) | Interrompe | 0ms |
| special | idle | Apos complete | variavel |
| qualquer | death | Interrompe TUDO | 0ms |
| death | idle (respawn) | Coluna de luz | ~1000ms |

### State Machine basica

```javascript
const DACIOLO_STATES = {
    IDLE: 'idle',
    WALKING: 'walking',
    ATTACKING: 'attacking',
    HIT: 'hit',
    USING_SPECIAL: 'special',
    DYING: 'dying',
    DEAD: 'dead',
    ASCENDING: 'ascending'  // estado unico do Daciolo
};

class DacioloStateMachine {
    constructor(daciolo) {
        this.daciolo = daciolo;
        this.currentState = DACIOLO_STATES.IDLE;
        this.previousState = null;
        this.lockedUntil = 0;  // timestamp ate quando esta travado em animacao
    }

    canTransitionTo(newState) {
        // Death SEMPRE interrompe
        if (newState === DACIOLO_STATES.DYING) return true;
        // Hit interrompe idle e walk
        if (newState === DACIOLO_STATES.HIT &&
            [DACIOLO_STATES.IDLE, DACIOLO_STATES.WALKING].includes(this.currentState)) return true;
        // Specials interrompem idle e walk
        if (newState === DACIOLO_STATES.USING_SPECIAL &&
            [DACIOLO_STATES.IDLE, DACIOLO_STATES.WALKING].includes(this.currentState)) return true;
        // Attack interrompe idle e walk
        if (newState === DACIOLO_STATES.ATTACKING &&
            [DACIOLO_STATES.IDLE, DACIOLO_STATES.WALKING].includes(this.currentState)) return true;
        // Idle/walk entre si
        if ([DACIOLO_STATES.IDLE, DACIOLO_STATES.WALKING].includes(newState) &&
            [DACIOLO_STATES.IDLE, DACIOLO_STATES.WALKING].includes(this.currentState)) return true;
        // Apos lock timer
        if (Date.now() >= this.lockedUntil) return true;

        return false;
    }

    transition(newState, lockDuration = 0) {
        if (!this.canTransitionTo(newState)) return false;
        this.previousState = this.currentState;
        this.currentState = newState;
        if (lockDuration > 0) {
            this.lockedUntil = Date.now() + lockDuration;
        }
        return true;
    }
}
```

---

## 4. LISTA DE ASSETS DE PARTICULA NECESSARIOS

| Asset | Dimensao | Descricao |
|---|---|---|
| `fumaca-particle.png` | 16x16 | Wisp de fumaca generica (dourado-branco) |
| `fumaca-santa-particle.png` | 16x16 (8 frames = 128x16) | Sheet de fumaca santa (ver spec separado) |
| `light-particle.png` | 8x8 | Particula de luz generica |
| `gold-dust.png` | 8x8 | Po dourado (destruicao de zumbis) |
| `pagina-biblia.png` | 16x16 | Pagina de biblia (retangulo com texto) |
| `fogo-santo.png` | 16x16 | Bola de fogo dourado |
| `rocha-particle.png` | 8x8 | Pedra/terra marrom |
| `debris.png` | 8x8 | Fragmento generico |
| `biblia-ground.png` | 32x32 | Biblia no chao (item coletavel) |
| `biblia-rosario-cruz.png` | 32x32 | Biblia + rosario formando cruz |
| `santinho-daciolo.png` | 16x24 | Panfleto de campanha |
| `espiral-hipnotica.png` | 32x32 (4 frames) | Espiral dourada girando |
| `mandala-dourada.png` | 64x64 | Mandala sagrada no chao |
| `anjo-silhueta.png` | 32x32 | Silhueta translucida de anjo |
| `cratera-cruz.png` | 64x64 | Marca de cratera em forma de cruz |
| `aureola-overlay.png` | 32x32 (4 frames) | Aureola pulsante (ver spec separado) |
| `raios-olhos.png` | 32x16 (4 frames) | Raios saindo dos olhos (ver spec separado) |

---

## 5. LISTA DE ASSETS DE AUDIO NECESSARIOS

| Asset | Descricao | Trigger |
|---|---|---|
| `gloria-a-deus.ogg` | Grito em varias intensidades (3 variantes) | Attack |
| `gloria-a-deus-full.ogg` | Grito completo com reverb | Special Gloria |
| `fumaca-santa-sfx.ogg` | Explosao reverberada santa | Special Fumaca |
| `coro-anjos.ogg` | Coro angelical (loop) | Fumaca, Death, Exorcismo Massa |
| `coro-anjos-completo.ogg` | Coro angelical com crescendo | Exorcismo Massa |
| `queima-jesus.ogg` | "Queima, Jesus! Shabalaba!" | Exorcismo |
| `sino-igreja.ogg` | Sino de igreja | Exorcismo |
| `terremoto.ogg` | Rumble de terremoto | Monte Roraima |
| `vento-forte.ogg` | Vento no topo da montanha | Monte Roraima |
| `daciolo-a-ursal-existe.ogg` | "A URSAL! A URSAL EXISTE!" | URSAL Ultimate |
| `sirene-alerta.ogg` | Sirene de emergencia | URSAL |
| `trovao.ogg` | Trovao pesado | URSAL |
| `impacto-nuclear.ogg` | Impacto massivo | URSAL |
| `daciolo-eu-avisei-ursal.ogg` | "EU AVISEI!" | URSAL aftermath |
| `jingle-campanha-distorcido.ogg` | Musica de campanha distorcida | Candidatura |
| `daciolo-nao-estou-a-venda.ogg` | "Nao estou a venda!" | Candidatura |
| `daciolo-erro-gloria.ogg` | "Gloria a sap-- opa!" | Erro Comico |
| `daciolo-sinto-cheiro-satanas.ogg` | "Sinto o cheiro de Satanas!" | 3 hits consecutivos |
| `daciolo-pela-honra-gloria.ogg` | "Pela honra e gloria..." | Exorcismo Massa |
| `daciolo-carissimo.ogg` | "Carissimo! Dignissimo!" | Aleatorio/Idle |
| `daciolo-venham-comigo.ogg` | "Venham comigo!" | Aleatorio/Walk |
