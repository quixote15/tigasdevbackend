# Eduardo Bolsonaro (Bananinha) - Animation Specification

## Phaser 3 Implementation Guide

### Overview
- **Engine:** Phaser 3.60+
- **Character Key:** `eduardo`
- **Scene Position:** Y-sorted (isometric top-down)
- **Base Sprite Size:** 64x64px
- **Projectile Size:** 32x32px
- **Collision Box:** 28x20px (centrado na base do sprite, menor que o visual)
- **Hitbox Offset:** { x: 18, y: 40, width: 28, height: 20 }

---

## 1. SPRITE SHEET LOADING

```javascript
// preload()
this.load.spritesheet('eduardo_idle', 'assets/personagens/eduardo-bolsonaro/eduardo_idle.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('eduardo_walk', 'assets/personagens/eduardo-bolsonaro/eduardo_walk.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('eduardo_attack', 'assets/personagens/eduardo-bolsonaro/eduardo_attack.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('eduardo_death', 'assets/personagens/eduardo-bolsonaro/eduardo_death.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('eduardo_hit', 'assets/personagens/eduardo-bolsonaro/eduardo_hit.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('eduardo_special_fuga', 'assets/personagens/eduardo-bolsonaro/eduardo_special_fuga.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('eduardo_buff_puxasaco', 'assets/personagens/eduardo-bolsonaro/eduardo_buff_puxasaco.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('eduardo_debuff_orfao', 'assets/personagens/eduardo-bolsonaro/eduardo_debuff_orfao.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('eduardo_banana', 'assets/personagens/eduardo-bolsonaro/eduardo_banana_projectile.png', {
    frameWidth: 32, frameHeight: 32
});
```

---

## 2. ANIMATION DEFINITIONS

### 2.1 Idle
```javascript
this.anims.create({
    key: 'eduardo_idle',
    frames: this.anims.generateFrameNumbers('eduardo_idle', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1,      // loop infinito
    yoyo: true        // ping-pong (0-1-2-3-2-1-0...)
});
```

**Timing Breakdown:**
| Frame | Duration | Descricao                  | Efeito Visual              |
|-------|----------|----------------------------|-----------------------------|
| 0     | 125ms    | Base (parado, olhando cima)| Postura submissa default    |
| 1     | 125ms    | Piscada nervosa            | Olhos semi-fechados, tremor |
| 2     | 125ms    | Olha pro lado (procura pai)| Cabeca vira, olhos deslizam |
| 3     | 125ms    | Suspiro                    | Ombros caem, nuvem de ar    |

**Ciclo Total:** 875ms (ida e volta com yoyo)

**Transicoes:**
- Idle -> Walk: imediata (sem blend)
- Idle -> Attack: imediata, cancela no frame atual
- Idle -> Hit: imediata, prioridade alta (interrompe idle)
- Idle -> Special: fade 100ms para o panico

---

### 2.2 Walk
```javascript
this.anims.create({
    key: 'eduardo_walk',
    frames: this.anims.generateFrameNumbers('eduardo_walk', { start: 0, end: 5 }),
    frameRate: 10,
    repeat: -1       // loop ciclico
});
```

**Timing Breakdown:**
| Frame | Duration | Descricao                    | Audio Cue              |
|-------|----------|------------------------------|------------------------|
| 0     | 100ms    | Pe direito (contato)         | sfx_step_right         |
| 1     | 100ms    | Transicao D-E (suspensao)    | sfx_suitcase_rattle    |
| 2     | 100ms    | Pe esquerdo (contato)        | sfx_step_left          |
| 3     | 100ms    | Transicao E-D (suspensao)    | sfx_suitcase_rattle    |
| 4     | 100ms    | TROPECO NA MALA              | sfx_stumble            |
| 5     | 100ms    | Recuperacao do tropeco        | sfx_gasp               |

**Ciclo Total:** 600ms por loop completo

**Comportamento da Cabeca (Head Bob):**
```javascript
// Aplicar offset Y na cabeca durante walk (separar head sprite se possivel)
// Frames 0,2: headOffsetY = -3  (cabeca balanca pra baixo)
// Frames 1,3: headOffsetY = +2  (cabeca balanca pra cima)
// Frame 4:    headOffsetY = -5  (cabeca vai pra frente no tropeco)
// Frame 5:    headOffsetY = +1  (cabeca volta, whiplash)
```

**Efeito de Mala Arrastando (Particle Trail):**
```javascript
// Emitir particulas de poeira atras da mala durante walk
const suitcaseDust = this.add.particles(0, 0, 'dust_particle', {
    follow: eduardoSprite,
    followOffset: { x: 20, y: 8 },   // posicao da mala
    speed: { min: 5, max: 15 },
    angle: { min: 160, max: 200 },    // pra tras
    scale: { start: 0.3, end: 0 },
    lifespan: 300,
    frequency: 150,                    // 1 particula a cada 150ms
    tint: 0x8B7355,                    // poeira marrom
    alpha: { start: 0.5, end: 0 }
});
```

**Direcoes (8-way):**
```javascript
// Usar flipX para espelhar esquerda/direita
// Para cima/baixo: trocar sprite sheet OU usar rotacao
// Direcoes diagonais: combinar flipX + offset

const DIRECTIONS = {
    DOWN:       { flipX: false, rotation: 0 },
    DOWN_RIGHT: { flipX: false, rotation: -0.3 },
    RIGHT:      { flipX: false, rotation: -Math.PI/2 },
    UP_RIGHT:   { flipX: false, rotation: -2.5 },
    UP:         { flipX: false, rotation: Math.PI },
    UP_LEFT:    { flipX: true,  rotation: -2.5 },
    LEFT:       { flipX: true,  rotation: -Math.PI/2 },
    DOWN_LEFT:  { flipX: true,  rotation: -0.3 }
};
// NOTA: idealmente ter 4 sprite sheets (down, up, left, right)
// e usar flipX para espelhar. Rotacao e fallback.
```

**Transicoes:**
- Walk -> Idle: quando velocidade = 0, transicao imediata
- Walk -> Attack: interrompe walk, inicia attack
- Walk -> Hit: interrompe imediatamente
- Walk -> Special: se HP < 30%, transicao via Frame 0 do Special (panico)

---

### 2.3 Attack (Banana Boomerang)
```javascript
this.anims.create({
    key: 'eduardo_attack',
    frames: this.anims.generateFrameNumbers('eduardo_attack', { start: 0, end: 2 }),
    frameRate: 10,
    repeat: 0         // one-shot
});
```

**Timing Breakdown:**
| Frame | Duration | Descricao          | Gameplay Event                    |
|-------|----------|--------------------|-----------------------------------|
| 0     | 100ms    | Wind-up            | Nenhum (anticipation)             |
| 1     | 100ms    | Arremesso          | SPAWN projetil banana neste frame |
| 2     | 100ms    | Follow-through     | Eduardo vulneravel (recovery)     |

**Duracao Total:** 300ms (ataque rapido)
**Cooldown:** 800ms antes de poder atacar novamente

**Spawn do Projetil (Frame 1):**
```javascript
eduardoSprite.on('animationupdate', (anim, frame) => {
    if (anim.key === 'eduardo_attack' && frame.index === 1) {
        spawnBananaBoomerang(eduardoSprite.x, eduardoSprite.y, targetAngle);
    }
});
```

**Banana Boomerang - Projetil:**
```javascript
this.anims.create({
    key: 'eduardo_banana_spin',
    frames: this.anims.generateFrameNumbers('eduardo_banana', { start: 0, end: 3 }),
    frameRate: 12,
    repeat: -1         // gira continuamente no ar
});
```

**Trajetoria do Boomerang:**
```javascript
function spawnBananaBoomerang(x, y, angle) {
    const banana = this.physics.add.sprite(x, y, 'eduardo_banana');
    banana.play('eduardo_banana_spin');

    // Trajetoria em arco (boomerang)
    const speed = 200;          // pixels/segundo
    const curveStrength = 150;  // intensidade da curva
    const maxDistance = 180;     // distancia maxima antes de voltar
    const returnSpeed = 180;    // velocidade de retorno (mais lento)

    // Fase 1: ida (arco pra frente)
    this.tweens.add({
        targets: banana,
        x: x + Math.cos(angle) * maxDistance,
        y: y + Math.sin(angle) * maxDistance,
        duration: maxDistance / speed * 1000,  // ~900ms
        ease: 'Sine.easeOut',
        onUpdate: () => {
            // Aplicar curva lateral
            banana.x += Math.cos(angle + Math.PI/2) * curveStrength * 0.016;
        },
        onComplete: () => {
            // Fase 2: volta (retorna pro Eduardo)
            this.tweens.add({
                targets: banana,
                x: eduardoSprite.x,
                y: eduardoSprite.y,
                duration: maxDistance / returnSpeed * 1000,
                ease: 'Sine.easeIn',
                onComplete: () => {
                    banana.destroy();
                    // Eduardo "pega" a banana de volta (rearma)
                }
            });
        }
    });

    // Dano
    banana.damage = 15;               // dano base
    banana.damageOnReturn = 10;        // dano na volta (menor)
    banana.canHitMultiple = true;      // atravessa inimigos

    // Trail de particula amarela
    const bananaTrail = this.add.particles(0, 0, 'particle_yellow', {
        follow: banana,
        speed: 0,
        scale: { start: 0.4, end: 0 },
        lifespan: 200,
        frequency: 30,
        tint: 0xF9E154,
        alpha: { start: 0.6, end: 0 }
    });
}
```

**Audio Cues do Ataque:**
- Frame 0 (wind-up): `sfx_eduardo_grunt` -- gemido de esforco
- Frame 1 (arremesso): `sfx_banana_throw` + `sfx_eduardo_pai` (grita "PAI!")
- Projetil em voo: `sfx_banana_whoosh` (loop suave enquanto no ar)
- Projetil retorno: `sfx_banana_return_whoosh`
- Projetil catch: `sfx_banana_catch` (slap na mao)

**Retorno ao Idle:**
```javascript
eduardoSprite.on('animationcomplete-eduardo_attack', () => {
    // Periodo vulneravel (sem banana por ~1.8s total da viagem)
    eduardo.isDisarmed = true;
    // Quando banana retorna:
    eduardo.isDisarmed = false;
    eduardoSprite.play('eduardo_idle');
});
```

---

### 2.4 Death
```javascript
this.anims.create({
    key: 'eduardo_death',
    frames: this.anims.generateFrameNumbers('eduardo_death', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: 0,
    hideOnComplete: false  // fica no ultimo frame (fantasma)
});
```

**Timing Breakdown:**
| Frame | Duration | Descricao              | Efeitos                              |
|-------|----------|------------------------|--------------------------------------|
| 0     | 125ms    | Impacto (knockback)    | Screen shake leve, flash branco      |
| 1     | 125ms    | Queda                  | Banana + mala voam (projeteis visuais)|
| 2     | 125ms    | No chao (X nos olhos)  | Spawn itens no chao (mala, banana)   |
| 3     | 125ms    | Fantasma comico sobe   | Fantasma flutua, desaparece apos 2s  |

**Duracao Total:** 500ms ate fantasma + 2000ms fantasma visivel = 2500ms total

**Efeitos de Morte:**
```javascript
eduardoSprite.on('animationupdate', (anim, frame) => {
    if (anim.key !== 'eduardo_death') return;

    switch (frame.index) {
        case 0: // Impacto
            // Screen shake
            this.cameras.main.shake(100, 0.005);
            // Flash branco no sprite
            eduardoSprite.setTintFill(0xFFFFFF);
            this.time.delayedCall(50, () => eduardoSprite.clearTint());
            break;

        case 1: // Queda -- objetos voam
            // Banana voa pro canto superior esquerdo
            spawnFlyingItem('banana', eduardo.x - 10, eduardo.y - 5, -45, 150);
            // Mala cai e abre
            spawnFlyingItem('mala_aberta', eduardo.x + 15, eduardo.y + 5, 30, 80);
            // Roupas espalhando da mala
            for (let i = 0; i < 3; i++) {
                spawnClothingDebris(eduardo.x + 15 + Phaser.Math.Between(-5, 5),
                                   eduardo.y + 5 + Phaser.Math.Between(-5, 5));
            }
            break;

        case 2: // No chao -- spawn itens coletaveis
            // Banana amassada (item coletavel?)
            spawnGroundItem('banana_squashed', eduardo.x - 12, eduardo.y + 8);
            // Mala aberta com roupas (cenario)
            spawnGroundItem('mala_aberta_ground', eduardo.x + 16, eduardo.y + 5);
            break;

        case 3: // Fantasma
            spawnGhost(eduardo.x, eduardo.y);
            break;
    }
});

function spawnGhost(x, y) {
    const ghost = this.add.sprite(x, y, 'eduardo_death', 3);
    ghost.setAlpha(0.5);

    // Fantasma flutua pra cima
    this.tweens.add({
        targets: ghost,
        y: y - 30,
        alpha: 0,
        duration: 2000,
        ease: 'Sine.easeIn',
        onComplete: () => ghost.destroy()
    });

    // Pequena oscilacao lateral enquanto sobe
    this.tweens.add({
        targets: ghost,
        x: { from: x - 3, to: x + 3 },
        duration: 400,
        yoyo: true,
        repeat: 4,
        ease: 'Sine.easeInOut'
    });
}
```

**Audio Cues da Morte:**
- Frame 0: `sfx_eduardo_death_cry` -- "PAAAAAI!" grito prolongado
- Frame 1: `sfx_suitcase_crash` + `sfx_banana_splat`
- Frame 2: `sfx_body_thud`
- Frame 3: `sfx_ghost_ascend` (som comico de harpa desafinada)

---

### 2.5 Hit
```javascript
this.anims.create({
    key: 'eduardo_hit',
    frames: this.anims.generateFrameNumbers('eduardo_hit', { start: 0, end: 1 }),
    frameRate: 12,
    repeat: 0
});
```

**Timing Breakdown:**
| Frame | Duration | Descricao            | Efeitos                     |
|-------|----------|----------------------|-----------------------------|
| 0     | 83ms     | Dano (flash branco)  | Knockback 4px, flash overlay|
| 1     | 83ms     | Recuperacao chorosa  | Lagrimas, tremor labio      |

**Duracao Total:** 166ms (reacao RAPIDA, covardia instantanea)

**Efeitos de Hit:**
```javascript
function playEduardoHit(damage) {
    eduardoSprite.play('eduardo_hit');

    // Flash branco overlay
    eduardoSprite.setTintFill(0xFFFFFF);
    this.time.delayedCall(40, () => eduardoSprite.clearTint());

    // Knockback
    const knockbackDir = Phaser.Math.Angle.Between(
        damageSource.x, damageSource.y,
        eduardo.x, eduardo.y
    );
    this.tweens.add({
        targets: eduardoSprite,
        x: eduardo.x + Math.cos(knockbackDir) * 8,
        y: eduardo.y + Math.sin(knockbackDir) * 8,
        duration: 100,
        ease: 'Back.easeOut'
    });

    // Particulas de suor/lagrima
    this.add.particles(eduardo.x, eduardo.y - 20, 'particle_tear', {
        speed: { min: 30, max: 60 },
        angle: { min: 200, max: 340 },
        scale: { start: 0.5, end: 0 },
        lifespan: 400,
        quantity: 4,
        tint: 0xAED6F1   // azul lagrima
    });

    // Texto "AI!" flutuante
    const aiText = this.add.text(eduardo.x, eduardo.y - 30, 'AI!', {
        fontSize: '8px',
        fontFamily: 'monospace',
        color: '#F7DC6F',
        stroke: '#1A1A1A',
        strokeThickness: 2
    }).setOrigin(0.5);

    this.tweens.add({
        targets: aiText,
        y: eduardo.y - 50,
        alpha: 0,
        duration: 600,
        ease: 'Cubic.easeOut',
        onComplete: () => aiText.destroy()
    });

    // Invulnerabilidade temporaria (i-frames)
    eduardo.isInvulnerable = true;
    // Piscar sprite
    this.tweens.add({
        targets: eduardoSprite,
        alpha: { from: 0.3, to: 1 },
        duration: 80,
        yoyo: true,
        repeat: 5,
        onComplete: () => {
            eduardo.isInvulnerable = false;
            eduardoSprite.setAlpha(1);
        }
    });

    // Voltar ao idle
    eduardoSprite.on('animationcomplete-eduardo_hit', () => {
        eduardoSprite.play('eduardo_idle');
    });
}
```

**Audio Cues do Hit:**
- Frame 0: `sfx_hit_impact` + `sfx_eduardo_ai` ("AI!" com voz aguda e covarde)
- Frame 1: `sfx_eduardo_whimper` (choramingo de cachorro)

---

### 2.6 Special - Fuga Estrategica
```javascript
this.anims.create({
    key: 'eduardo_special_fuga',
    frames: this.anims.generateFrameNumbers('eduardo_special_fuga', { start: 0, end: 5 }),
    frameRate: 10,
    repeat: 0
});
```

**Timing Breakdown:**
| Frame | Duration | Descricao                | Efeitos                               |
|-------|----------|--------------------------|---------------------------------------|
| 0     | 100ms    | Panico total             | Shake sprite, suor, larga banana      |
| 1     | 100ms    | Pre-teleporte (carga)    | Aura amarela, translucidez, flutua    |
| 2     | 100ms    | Flash de teleporte       | Flash branco 90%, particulas radiais  |
| 3     | 100ms    | Nuvem de fumaca          | Eduardo sumiu, olhos na fumaca        |
| 4     | 100ms    | Fumaca dissipando        | Marcas de rodinha, pena de galinha    |
| 5     | 100ms    | Residuo                  | Limpeza, itens no chao                |

**Duracao Total:** 600ms de animacao + teleporte instantaneo

**Efeitos da Fuga Estrategica:**
```javascript
function executeFugaEstrategica() {
    if (eduardo.hp / eduardo.maxHp > 0.3) return; // so ativa abaixo de 30% HP
    if (eduardo.fugaCooldown > 0) return;          // cooldown de 15 segundos

    eduardo.isInvulnerable = true;
    eduardoSprite.play('eduardo_special_fuga');

    // Frame 0: Panico -- shake no sprite
    eduardoSprite.on('animationupdate', (anim, frame) => {
        if (anim.key !== 'eduardo_special_fuga') return;

        switch(frame.index) {
            case 0: // Panico
                // Sprite shake local (jitter)
                this.tweens.add({
                    targets: eduardoSprite,
                    x: { from: eduardo.x - 2, to: eduardo.x + 2 },
                    duration: 30,
                    yoyo: true,
                    repeat: 3
                });
                // Spawn banana caindo
                spawnDroppedBanana(eduardo.x - 8, eduardo.y);
                // Particulas de suor
                emitSweatParticles(eduardo.x, eduardo.y, 6);
                break;

            case 1: // Pre-teleporte
                // Aura amarela crescente
                const aura = this.add.circle(eduardo.x, eduardo.y, 20, 0xFFD700, 0.4);
                this.tweens.add({
                    targets: aura,
                    scaleX: 1.5, scaleY: 1.5,
                    alpha: 0,
                    duration: 200,
                    onComplete: () => aura.destroy()
                });
                // Sprite translucido
                eduardoSprite.setAlpha(0.6);
                // Particulas de luz
                emitLightParticles(eduardo.x, eduardo.y, 5);
                break;

            case 2: // Flash
                // Flash branco na tela (leve)
                this.cameras.main.flash(100, 255, 255, 255, false, null, 0.3);
                // Sprite fica branco
                eduardoSprite.setTintFill(0xFFFFFF);
                // Radial lines (8 linhas)
                for (let i = 0; i < 8; i++) {
                    const angle = (Math.PI * 2 / 8) * i;
                    spawnRadialLine(eduardo.x, eduardo.y, angle, 20);
                }
                break;

            case 3: // Fumaca (Eduardo sumiu -- TELEPORTA AQUI)
                eduardoSprite.clearTint();
                // Calcular posicao de destino (longe dos inimigos)
                const escapePos = calculateEscapePosition(eduardo.x, eduardo.y);
                // Fumaca no local original
                spawnSmokeCloud(eduardo.x, eduardo.y);
                // Teleportar
                eduardo.x = escapePos.x;
                eduardo.y = escapePos.y;
                eduardoSprite.setPosition(escapePos.x, escapePos.y);
                eduardoSprite.setAlpha(0); // invisivel no destino por agora
                break;

            case 4: // Fumaca dissipando (no local antigo)
                // Nada no sprite principal (ele ja teleportou)
                // Efeitos sao no local antigo (particulas independentes)
                spawnWheelTracks(eduardo.previousX, eduardo.previousY);
                spawnChickenFeather(eduardo.previousX, eduardo.previousY);
                break;

            case 5: // Residuo + reaparecer
                // Eduardo reaparece no novo local com fade-in
                this.tweens.add({
                    targets: eduardoSprite,
                    alpha: 1,
                    duration: 300,
                    ease: 'Cubic.easeIn'
                });
                // Fumaca leve no destino
                spawnSmallSmoke(eduardo.x, eduardo.y);
                break;
        }
    });

    // Ao completar
    eduardoSprite.on('animationcomplete-eduardo_special_fuga', () => {
        eduardo.isInvulnerable = false;
        eduardoSprite.play('eduardo_idle');
        eduardo.fugaCooldown = 15000; // 15 segundos
    });
}

function calculateEscapePosition(currentX, currentY) {
    // Encontrar a direcao mais longe do inimigo mais proximo
    const nearestEnemy = findNearestEnemy(currentX, currentY);
    const escapeAngle = Phaser.Math.Angle.Between(
        nearestEnemy.x, nearestEnemy.y,
        currentX, currentY
    );
    const escapeDistance = 200; // pixels de distancia

    return {
        x: currentX + Math.cos(escapeAngle) * escapeDistance,
        y: currentY + Math.sin(escapeAngle) * escapeDistance
    };
}
```

**Audio Cues da Fuga:**
- Frame 0: `sfx_eduardo_panic_scream` ("AAAAAH!")
- Frame 1: `sfx_teleport_charge` (som eletrico crescente)
- Frame 2: `sfx_teleport_flash` (POP alto + flash sonoro)
- Frame 3: `sfx_smoke_poof` (som de fumaca classico cartoon)
- Frame 4: silencio (efeito dramatico)
- Frame 5: `sfx_eduardo_gasp` + `sfx_teleport_arrive` (som de reaparecer)

---

## 3. BUFF/DEBUFF ANIMATION OVERLAYS

### 3.1 Puxa-Saquismo (Buff Ativo)
```javascript
this.anims.create({
    key: 'eduardo_buff_puxasaco',
    frames: this.anims.generateFrameNumbers('eduardo_buff_puxasaco', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1
});

function activatePuxaSaquismo() {
    eduardo.buffActive = true;
    eduardo.attackMultiplier = 1.5;
    eduardo.speedMultiplier = 1.3;

    // Overlay sprite (adiciona por cima do sprite principal)
    const buffOverlay = this.add.sprite(eduardo.x, eduardo.y, 'eduardo_buff_puxasaco');
    buffOverlay.play('eduardo_buff_puxasaco');
    buffOverlay.setBlendMode(Phaser.BlendModes.ADD);  // blend aditivo pra aura brilhar
    buffOverlay.setAlpha(0.6);

    // Aura pulsante (tween adicional)
    this.tweens.add({
        targets: buffOverlay,
        scaleX: { from: 1.0, to: 1.15 },
        scaleY: { from: 1.0, to: 1.15 },
        alpha: { from: 0.4, to: 0.7 },
        duration: 500,
        yoyo: true,
        repeat: -1,
        ease: 'Sine.easeInOut'
    });

    // Estrelinhas orbitando
    const stars = [];
    for (let i = 0; i < 3; i++) {
        const star = this.add.sprite(0, 0, 'particle_star');
        star.setTint(0xFFD700);
        star.setScale(0.3);
        stars.push(star);
    }

    // Orbita das estrelas
    this.tweens.add({
        targets: {},
        duration: 2000,
        repeat: -1,
        onUpdate: (tween) => {
            const progress = tween.progress;
            stars.forEach((star, i) => {
                const angle = (progress * Math.PI * 2) + (i * Math.PI * 2 / 3);
                star.x = eduardo.x + Math.cos(angle) * 25;
                star.y = eduardo.y + Math.sin(angle) * 15; // elipse (isometrico)
            });
        }
    });
}
```

**Condicao de Ativacao:**
```javascript
// Checar distancia do Bolsonaro (pai) a cada frame
function checkPuxaSaquismo() {
    const pai = findCharacter('bolsonaro');
    if (!pai || pai.isDead) {
        deactivatePuxaSaquismo();
        activateOrfaoPolitico();
        return;
    }

    const distance = Phaser.Math.Distance.Between(
        eduardo.x, eduardo.y, pai.x, pai.y
    );

    if (distance < 150 && !eduardo.buffActive) {
        activatePuxaSaquismo();
    } else if (distance >= 150 && eduardo.buffActive) {
        deactivatePuxaSaquismo();
    }
}
```

---

### 3.2 Orfao Politico (Debuff Ativo)
```javascript
this.anims.create({
    key: 'eduardo_debuff_orfao',
    frames: this.anims.generateFrameNumbers('eduardo_debuff_orfao', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1
});

function activateOrfaoPolitico() {
    eduardo.debuffActive = true;
    eduardo.attackMultiplier = 0.5;    // perde 50% dano
    eduardo.speedMultiplier = 0.7;     // mais lento
    eduardo.defenseMultiplier = 0.5;   // mais vulneravel

    // Dessaturar o sprite principal
    const pipeline = this.renderer.pipelines.get('Desaturate');
    // Alternativa: usar tint cinzento
    eduardoSprite.setTint(0xA0A0A0);

    // Overlay sprite
    const debuffOverlay = this.add.sprite(eduardo.x, eduardo.y, 'eduardo_debuff_orfao');
    debuffOverlay.play('eduardo_debuff_orfao');
    debuffOverlay.setAlpha(0.5);

    // Nuvem de chuva pessoal
    const rainCloud = this.add.sprite(eduardo.x, eduardo.y - 35, 'rain_cloud');
    rainCloud.setScale(0.4);
    rainCloud.setTint(0x505050);

    // Gotas de chuva (particulas)
    const rainDrops = this.add.particles(0, 0, 'particle_rain', {
        follow: eduardoSprite,
        followOffset: { x: 0, y: -30 },
        speed: { min: 40, max: 60 },
        angle: { min: 85, max: 95 },     // quase reto pra baixo
        scale: { start: 0.3, end: 0.1 },
        lifespan: 300,
        frequency: 80,
        quantity: 2,
        tint: 0x5DADE2,
        alpha: { start: 0.7, end: 0 }
    });

    // Encolher sprite levemente (depressao)
    this.tweens.add({
        targets: eduardoSprite,
        scaleX: { from: 1.0, to: 0.95 },
        scaleY: { from: 1.0, to: 0.95 },
        duration: 2000,
        yoyo: true,
        repeat: -1,
        ease: 'Sine.easeInOut'
    });
}
```

---

## 4. PARTICLE EFFECTS REFERENCE

### 4.1 Suor (Sweat Drops)
```javascript
function emitSweatParticles(x, y, count) {
    this.add.particles(x, y - 20, 'particle_sweat', {
        speed: { min: 20, max: 50 },
        angle: { min: 180, max: 360 },
        scale: { start: 0.4, end: 0 },
        lifespan: 500,
        quantity: count,
        tint: 0xAED6F1,
        gravityY: 30
    });
}
```

### 4.2 Lagrimas (Tears - Idle/Hit)
```javascript
function emitTearParticles(x, y) {
    this.add.particles(x, y - 10, 'particle_tear', {
        speed: { min: 5, max: 15 },
        angle: { min: 80, max: 100 },
        scale: { start: 0.3, end: 0 },
        lifespan: 800,
        frequency: 600,      // 1 lagrima a cada 600ms
        quantity: 1,
        tint: 0xAED6F1,
        gravityY: 40
    });
}
// NOTA: lagrimas sao PERMANENTES. Emitir sempre que Eduardo esta vivo.
```

### 4.3 Fumaca de Teleporte
```javascript
function spawnSmokeCloud(x, y) {
    const smokeEmitter = this.add.particles(x, y, 'particle_smoke', {
        speed: { min: 10, max: 40 },
        angle: { min: 0, max: 360 },
        scale: { start: 1.0, end: 0 },
        lifespan: 1200,
        quantity: 12,
        tint: 0xD5D8DC,
        alpha: { start: 0.8, end: 0 }
    });

    // Auto-destroy apos emissao
    this.time.delayedCall(100, () => smokeEmitter.stop());
    this.time.delayedCall(1500, () => smokeEmitter.destroy());
}
```

### 4.4 Pena de Galinha (Fuga das Galinhas)
```javascript
function spawnChickenFeather(x, y) {
    const feather = this.add.sprite(x, y - 10, 'particle_feather');
    feather.setScale(0.3);
    feather.setTint(0xFFFFFF);

    // Cai lentamente em zigzag
    this.tweens.add({
        targets: feather,
        y: y + 20,
        duration: 2000,
        ease: 'Sine.easeIn'
    });
    this.tweens.add({
        targets: feather,
        x: { from: x - 5, to: x + 5 },
        duration: 300,
        yoyo: true,
        repeat: 6,
        ease: 'Sine.easeInOut'
    });
    this.tweens.add({
        targets: feather,
        alpha: 0,
        delay: 1800,
        duration: 200,
        onComplete: () => feather.destroy()
    });
}
```

### 4.5 Trilho de Rodinhas da Mala
```javascript
function spawnWheelTracks(x, y) {
    const graphics = this.add.graphics();
    graphics.lineStyle(1, 0x5B3A1E, 0.6);

    // Duas linhas paralelas na direcao da fuga
    const escapeAngle = eduardo.lastFacingAngle;
    const trackLength = 25;

    for (let offset of [-3, 3]) {  // duas rodinhas
        const perpAngle = escapeAngle + Math.PI / 2;
        const startX = x + Math.cos(perpAngle) * offset;
        const startY = y + Math.sin(perpAngle) * offset;
        const endX = startX + Math.cos(escapeAngle) * trackLength;
        const endY = startY + Math.sin(escapeAngle) * trackLength;

        graphics.lineBetween(startX, startY, endX, endY);
    }

    // Fade out
    this.tweens.add({
        targets: graphics,
        alpha: 0,
        delay: 2000,
        duration: 1000,
        onComplete: () => graphics.destroy()
    });
}
```

---

## 5. STATE MACHINE

```
                    ┌──────────┐
                    │   IDLE   │◄──────────────────────┐
                    └────┬─────┘                       │
                         │                              │
              ┌──────────┼──────────┐                   │
              ▼          ▼          ▼                   │
         ┌────────┐ ┌────────┐ ┌────────┐              │
         │  WALK  │ │ ATTACK │ │SPECIAL │              │
         └───┬────┘ └───┬────┘ └───┬────┘              │
             │          │          │                    │
             │          ▼          │                    │
             │     ┌─────────┐    │                    │
             ├────►│   HIT   │◄───┤                    │
             │     └────┬────┘    │                    │
             │          │         │                    │
             │          ▼         │                    │
             │     ┌─────────┐    │                    │
             └────►│  DEATH  │◄───┘                    │
                   └─────────┘                         │
                                                       │
              Todos os estados voltam ao IDLE ──────────┘
              (exceto DEATH)
```

### Prioridade de Animacao (maior numero = maior prioridade):
1. **Idle** -- prioridade 0 (default)
2. **Walk** -- prioridade 1
3. **Attack** -- prioridade 2
4. **Hit** -- prioridade 3 (interrompe tudo exceto death/special)
5. **Special** -- prioridade 4 (interrompe tudo exceto death)
6. **Death** -- prioridade 5 (interrompe TUDO, irreversivel)

---

## 6. BORDOES / VOICE LINES (Texto Flutuante)

```javascript
const EDUARDO_VOICELINES = {
    idle: [
        "Pai! Pai!",
        "Cadê o pai?",
        "Posso pedir uma embaixada?"
    ],
    attack: [
        "Foi brilhante, pai!",
        "Comunismo vai voltar com força!",
        "Toma banana!"
    ],
    hit: [
        "AI! Isso dói!",
        "Pai, me ajuda!",
        "Manda grana pra mim, pai!"
    ],
    death: [
        "Se o senhor não me apoiar, vou pro Twitter fazer textão!",
        "Frouxo! Covarde! Fujão!",
        "PAAAAAI!"
    ],
    special_fuga: [
        "Preciso fazer algo importantíssimo aqui na Disney!",
        "Recuo estratégico!",
        "Volto já! ...ou não!"
    ],
    buff_puxasaco: [
        "Foi brilhante, pai!",
        "O senhor é o melhor presidente!",
        "Estou aqui, pai!"
    ],
    debuff_orfao: [
        "Pai? ...Pai?",
        "Ninguém me liga...",
        "Tô sozinho de novo..."
    ]
};

function showVoiceLine(character, state) {
    const lines = EDUARDO_VOICELINES[state];
    if (!lines) return;

    const text = Phaser.Utils.Array.GetRandom(lines);
    const voiceBubble = this.add.text(character.x, character.y - 40, text, {
        fontSize: '7px',
        fontFamily: '"Press Start 2P", monospace',
        color: '#F7DC6F',
        stroke: '#1A1A1A',
        strokeThickness: 2,
        backgroundColor: '#1A1A1A80',
        padding: { x: 2, y: 1 }
    }).setOrigin(0.5);

    this.tweens.add({
        targets: voiceBubble,
        y: character.y - 60,
        alpha: 0,
        duration: 2000,
        delay: 500,
        ease: 'Cubic.easeOut',
        onComplete: () => voiceBubble.destroy()
    });
}
```

**Frequencia de Voice Lines:**
- Idle: 1 a cada 8-12 segundos (aleatorio)
- Attack: 40% de chance por ataque
- Hit: 60% de chance por hit
- Death: 100% (sempre)
- Special: 100% (sempre)
- Buff/Debuff: 1 ao ativar, depois 1 a cada 10 segundos

---

## 7. PERFORMANCE NOTES

- **Texture Atlas:** Combinar todos os sprite sheets em 1 atlas (Texture Packer) pra reduzir draw calls
- **Object Pool:** Reutilizar particulas de lagrima/suor (sao permanentes e frequentes)
- **Particle Budget:** Max 20 particulas simultaneas para Eduardo (lagrimas + suor + trail)
- **Animation Caching:** Criar as animacoes uma vez no `create()`, nao por instancia
- **Collision:** Usar hitbox menor que o sprite visual (28x20 vs 64x64)
- **Y-Sort:** Usar `eduardo.y + 60` como sort value (base dos pes)
