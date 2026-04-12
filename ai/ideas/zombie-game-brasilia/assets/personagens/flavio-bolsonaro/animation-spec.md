# Flavio Bolsonaro (O Herdeiro) - Animation Specification

## Engine: Phaser 3
## Character Key: `flavio_bolsonaro`

---

## 1. IDLE Animation

**Key:** `flavio_idle`
**Spritesheet:** `flavio_idle.png` (256x64px)
**Frames:** 4 | **Frame Size:** 64x64px
**FPS:** 8 | **Repeat:** -1 (infinite loop)
**Total Cycle:** 500ms

### Frame Timing
| Frame | Index | Duration | Description                          |
|-------|-------|----------|--------------------------------------|
| 0     | 0     | 150ms    | Pose moderada, sorriso ensaiado      |
| 1     | 1     | 80ms     | Piscar nervoso (RAPIDO -- tique)     |
| 2     | 2     | 180ms    | Pose moderada, cabeca inclinada      |
| 3     | 3     | 90ms     | Piscar duplo (nervosismo crescente)  |

### Phaser 3 Config
```javascript
this.anims.create({
    key: 'flavio_idle',
    frames: [
        { key: 'flavio_idle', frame: 0, duration: 150 },
        { key: 'flavio_idle', frame: 1, duration: 80 },
        { key: 'flavio_idle', frame: 2, duration: 180 },
        { key: 'flavio_idle', frame: 3, duration: 90 }
    ],
    repeat: -1
});
```

### Efeitos Especiais
- **Piscar Nervoso Timer:** A cada 3-5 segundos (random), adicionar um piscar EXTRA fora do ciclo normal. Usar `this.time.addEvent` com delay random entre 3000-5000ms para trigger frame 1 por 80ms.
- **Brilho Abotoaduras:** A cada 4 segundos, flash de 1 frame (40ms) com tint amarelo (#F0D060) nos pixels das abotoaduras.
- **Suor na Testa:** Particula unica (1x1px branco) que aparece na testa e escorre 2px para baixo a cada 6 segundos. Usar Phaser particle emitter com gravity Y: 10, lifespan: 800ms.

### Transicoes
- Idle -> Walk: Imediato (0ms blend)
- Idle -> Attack: Imediato (0ms blend)
- Idle -> Hit: Interrompe qualquer frame, prioridade alta
- Idle -> Special: Delay 100ms (preparacao)
- Idle -> Death: Interrompe, prioridade maxima

---

## 2. WALK Animation

**Key:** `flavio_walk`
**Spritesheet:** `flavio_walk.png` (384x64px)
**Frames:** 6 | **Frame Size:** 64x64px
**FPS:** 10 | **Repeat:** -1 (infinite loop)
**Total Cycle:** 600ms

### Frame Timing
| Frame | Index | Duration | Description                          |
|-------|-------|----------|--------------------------------------|
| 0     | 0     | 100ms    | Pe direito contato                   |
| 1     | 1     | 100ms    | Pe direito meio (bounce +1px Y)      |
| 2     | 2     | 100ms    | Pe esquerdo contato (mirror)         |
| 3     | 3     | 100ms    | Pe esquerdo meio (piscar nervoso)    |
| 4     | 4     | 100ms    | Impulso direito                      |
| 5     | 5     | 100ms    | Impulso esquerdo (sorriso treme)     |

### Phaser 3 Config
```javascript
this.anims.create({
    key: 'flavio_walk',
    frames: this.anims.generateFrameNumbers('flavio_walk', { start: 0, end: 5 }),
    frameRate: 10,
    repeat: -1
});
```

### Efeitos Especiais
- **Bounce Vertical:** Nos frames 1 e 3, sprite sobe 1px (Y offset -1). Usar `sprite.y -= 1` no frame callback e restaurar no proximo.
- **Rigidez do Terno:** O walk cycle deve parecer MECANICO. Sem easing -- linear transitions. O corpo se move como um boneco articulado.
- **Sorriso Treme (Frame 5):** No frame 5, aplicar micro-shake horizontal de 1px por 50ms no sprite inteiro. `this.tweens.add({ x: sprite.x + 1, duration: 25, yoyo: true })`.
- **Footstep Dust:** A cada Frame 0 e 2 (contato), emitir 2-3 particulas de poeira (cinza claro, 1x1px) no pe que toca o chao. Particle emitter: speed 10-20, lifespan 300ms, gravity Y: 5.

### Transicoes
- Walk -> Idle: Completa o frame atual, depois transiciona (max 100ms delay)
- Walk -> Attack: Interrompe imediato
- Walk -> Hit: Interrompe imediato, prioridade alta

### Direcoes (8-way)
```
Walk sprites sao para direcao DOWN (default).
Usar flipX para LEFT/RIGHT.
Para UP: usar sprite sheet separado OU flip vertical com ajuste.
Direcoes diagonais: interpolar entre os dois eixos mais proximos.
```

---

## 3. ATTACK Animation

**Key:** `flavio_attack`
**Spritesheet:** `flavio_attack.png` (192x64px)
**Frames:** 3 | **Frame Size:** 64x64px
**FPS:** 10 | **Repeat:** 0 (one-shot)
**Total Duration:** 300ms

### Frame Timing
| Frame | Index | Duration | Description                          |
|-------|-------|----------|--------------------------------------|
| 0     | 0     | 120ms    | Dedo em riste, balao forma           |
| 1     | 1     | 100ms    | GRITO -- balao explode, sonic waves  |
| 2     | 2     | 80ms     | Recomposicao instantanea             |

### Phaser 3 Config
```javascript
this.anims.create({
    key: 'flavio_attack',
    frames: [
        { key: 'flavio_attack', frame: 0, duration: 120 },
        { key: 'flavio_attack', frame: 1, duration: 100 },
        { key: 'flavio_attack', frame: 2, duration: 80 }
    ],
    repeat: 0
});

// Callback para hitbox
sprite.on('animationupdate', (anim, frame) => {
    if (anim.key === 'flavio_attack' && frame.index === 1) {
        this.activateAttackHitbox('flavio_sonic_cone');
    }
});

sprite.on('animationcomplete-flavio_attack', () => {
    this.deactivateAttackHitbox();
    sprite.play('flavio_idle');
});
```

### Hitbox
- **Tipo:** Cone frontal (sonic wave)
- **Alcance:** 80px a frente do personagem
- **Angulo:** 60 graus
- **Ativacao:** Frame 1 (100ms de duracao)
- **Dano:** 15 HP base

### Efeitos Especiais
- **Speech Bubble Explode (Frame 1):**
  - Spawnar 4-6 particulas de texto (sprites 4x4px com "#", "$", "%", "&", "!") voando em arco
  - Velocidade: 80-120 random, angulo: -45 a +45 graus a partir da frente
  - Lifespan: 400ms, fade out nos ultimos 100ms
  - Rotation: random 0-360 graus, angular velocity: 180deg/s

- **Sonic Waves (Frame 1):**
  - 3 arcos concentricos (sprites separados ou graphics draw)
  - Cor: `#4488CC` com alpha 0.4
  - Cada arco expande de 0 a 40px em 200ms
  - Delay entre arcos: 50ms (staggered)
  - Fade out: alpha 0.4 -> 0 em 200ms

- **Hair Break (Frame 1):** Tint shift sutil no topo da cabeca (2-3 pixels mais claros, gel falhando)

- **Screen Shake:** Micro-shake de 1px por 50ms no frame 1. `this.cameras.main.shake(50, 0.002)`.

### Transicoes
- Attack -> Idle: Automatico ao completar (80ms no frame 2, depois idle)
- Attack -> Hit: PODE interromper se hit chegar durante attack
- Attack -> Death: Interrompe imediato

---

## 4. DEATH Animation

**Key:** `flavio_death`
**Spritesheet:** `flavio_death.png` (256x64px)
**Frames:** 4 | **Frame Size:** 64x64px
**FPS:** 8 | **Repeat:** 0 (one-shot)
**Total Duration:** 500ms (+ hold no ultimo frame)

### Frame Timing
| Frame | Index | Duration | Description                          |
|-------|-------|----------|--------------------------------------|
| 0     | 0     | 100ms    | Impacto -- sorriso QUEBRA             |
| 1     | 1     | 120ms    | Queda -- terno rasga, tatuagem aparece |
| 2     | 2     | 130ms    | No chao -- tatuagem completa exposta  |
| 3     | 3     | 150ms    | Derrota final -- sorriso patetico     |

### Phaser 3 Config
```javascript
this.anims.create({
    key: 'flavio_death',
    frames: [
        { key: 'flavio_death', frame: 0, duration: 100 },
        { key: 'flavio_death', frame: 1, duration: 120 },
        { key: 'flavio_death', frame: 2, duration: 130 },
        { key: 'flavio_death', frame: 3, duration: 150 }
    ],
    repeat: 0,
    hideOnComplete: false
});

sprite.on('animationupdate', (anim, frame) => {
    if (anim.key === 'flavio_death') {
        switch(frame.index) {
            case 0: // Smile breaks
                this.cameras.main.shake(80, 0.005);
                this.spawnParticles('cufflink_gold', sprite.x, sprite.y, 1);
                break;
            case 1: // Suit tears
                this.spawnParticles('fabric_tear', sprite.x, sprite.y, 4);
                this.spawnParticles('cufflink_gold', sprite.x + 10, sprite.y, 1);
                break;
            case 2: // Tattoo reveal
                this.playSound('sfx_tattoo_reveal'); // bass hit
                break;
            case 3: // Pathetic smile + ghost
                this.spawnGhostSilhouette(sprite.x, sprite.y - 20);
                break;
        }
    }
});

sprite.on('animationcomplete-flavio_death', () => {
    // Hold no ultimo frame por 2 segundos, depois fade
    this.time.delayedCall(2000, () => {
        this.tweens.add({
            targets: sprite,
            alpha: 0,
            duration: 500,
            onComplete: () => sprite.destroy()
        });
    });
});
```

### Efeitos Especiais
- **Frame 0 -- Cufflink Pop:**
  - 1 particula dourada (#D4A940) voa em arco parabolico
  - Speed: 60, angulo: -60 a -30 graus, gravity Y: 100
  - Bounce: bounceY: 0.3, lifespan: 1200ms
  - Rotation: 720deg/s (spinning cufflink)

- **Frame 1 -- Fabric Tear:**
  - 3-4 particulas azul marinho (#1B2A4A) de tecido rasgado
  - Speed: 30-50, direcoes radiais, lifespan: 600ms
  - Sem gravidade (flutuam)
  - Tambem: 1 particula de sapato (marrom escuro) voando para cada lado

- **Frame 2 -- Tattoo Reveal Bass Hit:**
  - Screen flash vermelho (#CC2222) por 40ms a 20% opacity
  - Camera zoom in sutil: `this.cameras.main.zoomTo(1.05, 130)` e volta `zoomTo(1.0, 200)`
  - Sound: bass hit profundo + som de tecido rasgando

- **Frame 3 -- Ghost Silhouette:**
  - Sprite translucido (#8888AA, alpha 0.15) do pai aparece ATRAS e ACIMA
  - Fade in de 0 a 0.15 alpha em 300ms
  - Flutua levemente: tween Y -2 a +2, duration 1000ms, yoyo, repeat -1
  - Escala: 1.5x do personagem (sombra GRANDE e ameacadora)
  - Barras de prisao sobrepostas em linhas verticais (3 linhas pretas, 1px, alpha 0.1)

- **Frame 3 -- Estrelas Douradas:**
  - 3 sprites de estrela (#D4A940, 3x3px) circulando acima da cabeca
  - Orbit: raio 12px, velocidade angular 180deg/s
  - Lifespan: ate o sprite fazer fade out

### Audio Cues
| Timing | Sound                                         |
|--------|-----------------------------------------------|
| 0ms    | `sfx_impact_heavy` -- golpe no terno          |
| 100ms  | `sfx_fabric_rip` -- terno rasgando             |
| 220ms  | `sfx_bass_hit` -- revelacao da tatuagem        |
| 350ms  | `sfx_pathetic_smile` -- som comico de squeeze  |
| 350ms  | `vo_flavio_death` -- "Meu pai... e inocente..." (sussurro) |

---

## 5. HIT Animation

**Key:** `flavio_hit`
**Spritesheet:** `flavio_hit.png` (128x64px)
**Frames:** 2 | **Frame Size:** 64x64px
**FPS:** 12 | **Repeat:** 0 (one-shot)
**Total Duration:** 167ms

### Frame Timing
| Frame | Index | Duration | Description                          |
|-------|-------|----------|--------------------------------------|
| 0     | 0     | 100ms    | Sorriso TRAVA -- olhos panico        |
| 1     | 1     | 67ms     | Recuperacao robotica                 |

### Phaser 3 Config
```javascript
this.anims.create({
    key: 'flavio_hit',
    frames: [
        { key: 'flavio_hit', frame: 0, duration: 100 },
        { key: 'flavio_hit', frame: 1, duration: 67 }
    ],
    repeat: 0
});

sprite.on('animationupdate', (anim, frame) => {
    if (anim.key === 'flavio_hit' && frame.index === 0) {
        // Hit flash
        sprite.setTintFill(0xFFFFFF);
        this.time.delayedCall(40, () => sprite.clearTint());
        
        // Knockback
        const knockbackDir = Phaser.Math.Angle.Between(
            damageSource.x, damageSource.y, sprite.x, sprite.y
        );
        this.tweens.add({
            targets: sprite,
            x: sprite.x + Math.cos(knockbackDir) * 4,
            y: sprite.y + Math.sin(knockbackDir) * 4,
            duration: 80,
            ease: 'Power2'
        });
        
        // Sweat particles
        this.spawnParticles('sweat_drop', sprite.x, sprite.y - 20, 2);
    }
});

sprite.on('animationcomplete-flavio_hit', () => {
    sprite.play('flavio_idle');
});
```

### Efeitos Especiais
- **Hit Flash:** Tint branco total por 40ms no Frame 0
- **Knockback:** 4px na direcao oposta ao dano, ease Power2, 80ms
- **Sweat Drops:** 2 particulas brancas (1x1px) voam da testa, speed 40, angulo -90+-30, gravity Y: 50, lifespan: 400ms
- **Smile Freeze Sound:** Som sutil de "click" metalico quando o sorriso trava (como um mecanismo travando)

### Invulnerability Window
- **Duracao:** 300ms apos hit (167ms animacao + 133ms extra)
- **Visual:** Sprite pisca (alpha 0.5 e 1.0 alternando a cada 50ms) durante invulnerability

---

## 6. SPECIAL: "Sera?" Dance

**Key:** `flavio_special_sera`
**Spritesheet:** `flavio_special_sera.png` (512x64px)
**Frames:** 8 | **Frame Size:** 64x64px
**FPS:** 8 | **Repeat:** 0 (one-shot)
**Total Duration:** 1000ms (+ 3000ms stun effect on enemies)

### Frame Timing
| Frame | Index | Duration | Description                            |
|-------|-------|----------|----------------------------------------|
| 0     | 0     | 100ms    | Saca celular dourado                   |
| 1     | 1     | 120ms    | Comeca a dancar (ombros rigidos)       |
| 2     | 2     | 130ms    | "Se-" -- ondas hipnoticas iniciam      |
| 3     | 3     | 130ms    | "-ra?" -- ondas expandem, stun trigger |
| 4     | 4     | 130ms    | Giro 360 (costas, etiqueta visivel)    |
| 5     | 5     | 120ms    | Volta de frente, pose triunfal         |
| 6     | 6     | 120ms    | Pose influencer (coracao)              |
| 7     | 7     | 150ms    | Guarda celular, volta ao normal        |

### Phaser 3 Config
```javascript
this.anims.create({
    key: 'flavio_special_sera',
    frames: [
        { key: 'flavio_special_sera', frame: 0, duration: 100 },
        { key: 'flavio_special_sera', frame: 1, duration: 120 },
        { key: 'flavio_special_sera', frame: 2, duration: 130 },
        { key: 'flavio_special_sera', frame: 3, duration: 130 },
        { key: 'flavio_special_sera', frame: 4, duration: 130 },
        { key: 'flavio_special_sera', frame: 5, duration: 120 },
        { key: 'flavio_special_sera', frame: 6, duration: 120 },
        { key: 'flavio_special_sera', frame: 7, duration: 150 }
    ],
    repeat: 0
});
```

### Skill Mechanics Implementation
```javascript
sprite.on('animationupdate', (anim, frame) => {
    if (anim.key !== 'flavio_special_sera') return;
    
    switch(frame.index) {
        case 0: // Phone out
            this.playSound('sfx_tiktok_notification');
            this.spawnTikTokIcon(sprite.x + 20, sprite.y - 10);
            break;
            
        case 1: // Dance start
            this.playSound('music_sera_beat'); // TikTok beat loop
            this.startTikTokSparkles(sprite);
            break;
            
        case 2: // "Se-" hypnotic waves begin
            this.startHypnoticWaves(sprite, { 
                radius: 60, 
                color: [0xFF69B4, 0x00CED1], // pink + cyan
                alpha: 0.3,
                expandSpeed: 400 
            });
            this.spawnZemaMiniature(sprite.x + 24, sprite.y + 24);
            this.showSpeechBubble(sprite, "Se-", { 
                font: 'TikTok', color: '#FF69B4' 
            });
            break;
            
        case 3: // "-ra?" STUN TRIGGER
            this.expandHypnoticWaves({ radius: 120, alpha: 0.5 });
            this.showSpeechBubble(sprite, "Sera?", { 
                font: 'TikTok', color: '#FF69B4', size: 'large' 
            });
            // STUN all enemies in radius
            this.stunEnemiesInRadius(sprite.x, sprite.y, 120, 3000);
            this.spawnMusicNotes(sprite, 4);
            this.spawnTikTokHearts(sprite, 3);
            break;
            
        case 4: // Spin
            this.tweens.add({
                targets: sprite,
                angle: 360,
                duration: 130,
                onComplete: () => { sprite.angle = 0; }
            });
            this.spawnConfetti(sprite, 12); // pink, blue, white particles
            break;
            
        case 5: // Triumphant
            this.showFloatingText(sprite, "+10K", { 
                color: '#FF69B4', 
                floatUp: true, 
                duration: 800 
            });
            break;
            
        case 6: // Heart pose
            this.startFadeHypnoticWaves(500);
            break;
            
        case 7: // Back to normal
            this.stopTikTokSparkles();
            this.fadeZemaMiniature(300);
            this.stopMusic('music_sera_beat', 300);
            break;
    }
});

sprite.on('animationcomplete-flavio_special_sera', () => {
    sprite.play('flavio_idle');
});
```

### VFX Detail: Hypnotic Waves
```javascript
startHypnoticWaves(sprite, config) {
    const waveGroup = this.add.group();
    const colors = [0xFF69B4, 0x00CED1]; // alternating pink/cyan
    
    this.time.addEvent({
        delay: 200,
        repeat: 5,
        callback: () => {
            const ring = this.add.circle(sprite.x, sprite.y, 4, colors[waveGroup.getLength() % 2]);
            ring.setAlpha(config.alpha);
            ring.setStrokeStyle(1, colors[waveGroup.getLength() % 2], config.alpha);
            ring.setFillStyle(0x000000, 0); // hollow ring
            waveGroup.add(ring);
            
            this.tweens.add({
                targets: ring,
                radius: config.radius,
                alpha: 0,
                duration: config.expandSpeed,
                onComplete: () => ring.destroy()
            });
        }
    });
    
    return waveGroup;
}
```

### VFX Detail: Zema Miniature
```javascript
spawnZemaMiniature(x, y) {
    const zema = this.add.sprite(x, y, 'zema_mini'); // 16x16px sprite
    zema.setScale(0.5);
    zema.setAlpha(0.8);
    zema.play('zema_mini_dance');
    
    // Bobbing motion
    this.tweens.add({
        targets: zema,
        y: y - 3,
        duration: 250,
        yoyo: true,
        repeat: -1,
        ease: 'Sine.easeInOut'
    });
    
    return zema;
}
```

### VFX Detail: TikTok Confetti
```javascript
spawnConfetti(sprite, count) {
    const colors = [0xFF69B4, 0x00CED1, 0xFFFFFF, 0xFF1493, 0x00BFFF];
    const emitter = this.add.particles(sprite.x, sprite.y - 30, 'pixel_1x1', {
        speed: { min: 20, max: 60 },
        angle: { min: 200, max: 340 },
        gravityY: 40,
        lifespan: 1200,
        quantity: count,
        tint: colors,
        scale: { start: 1, end: 0.3 },
        rotate: { min: 0, max: 360 },
        maxParticles: count
    });
}
```

### Audio Cues
| Timing  | Sound                                              |
|---------|-----------------------------------------------------|
| 0ms     | `sfx_tiktok_notification` -- som de notificacao     |
| 100ms   | `music_sera_beat` -- beat do TikTok (loop 900ms)    |
| 230ms   | `vo_flavio_sera_1` -- "Se-"                         |
| 360ms   | `vo_flavio_sera_2` -- "-ra?" (tom questionador)     |
| 360ms   | `sfx_hypnotic_wave` -- woooosh reverb               |
| 490ms   | `sfx_whoosh` -- giro                                |
| 610ms   | `sfx_crowd_cheer` -- torcida pequena (ironica)      |
| 850ms   | `sfx_phone_lock` -- celular guardando               |

### Cooldown
- **Cooldown:** 15 segundos
- **Visual Cooldown Indicator:** Icone do TikTok (canto da tela) em greyscale, preenche de rosa conforme cooldown completa

---

## 7. ADDITIONAL SKILL ANIMATIONS (Future Implementation)

### "Moderacao Forcada" (Alternative Special)
**Frames:** 6 | **Duration:** 800ms
| Frame | Duration | Description                                            |
|-------|----------|--------------------------------------------------------|
| 0     | 120ms    | Maos levantadas em gesto de "calma"                    |
| 1     | 130ms    | Aura AZUL calma emana (#4488CC, 30% alpha)             |
| 2     | 150ms    | Aura expande, inimigos desaceleram 50%                 |
| 3     | 100ms    | FALHA -- aura CRACKS (50% chance)                      |
| 4     | 150ms    | Aura EXPLODE em vermelho (#CC3333), knockback inimigos |
| 5     | 150ms    | Recuperacao, sorriso torto, suor na testa              |

**Mecanica:** 50% chance de funcionar (aura azul stun 2s), 50% de falhar (aura vermelha enrage inimigos)

### "Heranca Maldita" (Ultimate)
**Frames:** 6 | **Duration:** 1200ms
| Frame | Duration | Description                                                  |
|-------|----------|--------------------------------------------------------------|
| 0     | 150ms    | Flavio fecha os olhos, concentra                              |
| 1     | 200ms    | Sombra GIGANTE do pai cresce atras dele (silhueta 2x)        |
| 2     | 250ms    | Sombra do pai faz gesto de ataque, barras de prisao projetam |
| 3     | 200ms    | ONDA de pressao politica (dano area + fear 2s)               |
| 4     | 200ms    | Sombra comeca a desaparecer, grades se dissolvem             |
| 5     | 200ms    | Flavio abre olhos, expressao de peso no ombro                |

### "Sorriso Ensaiado" (Crowd Control)
**Frames:** 4 | **Duration:** 600ms
| Frame | Duration | Description                                            |
|-------|----------|--------------------------------------------------------|
| 0     | 100ms    | Flavio vira de frente, olha diretamente para inimigos  |
| 1     | 200ms    | Sorriso INTENSIFICA a niveis perturbadores (zoom face) |
| 2     | 200ms    | Inimigos CONGELAM (freeze 2s) pelo uncanny valley      |
| 3     | 100ms    | Volta ao normal, ajusta gravata                        |

---

## 8. STATE MACHINE

```
                    ┌──────────┐
                    │   IDLE   │◄──────────────────────────────┐
                    └────┬─────┘                               │
                         │                                     │
              ┌──────────┼──────────┐                          │
              ▼          ▼          ▼                          │
         ┌────────┐ ┌────────┐ ┌─────────┐                   │
         │  WALK  │ │ ATTACK │ │ SPECIAL │                   │
         └───┬────┘ └───┬────┘ └────┬────┘                   │
             │          │           │                          │
             │          ▼           ▼                          │
             │     ┌─────────────────────┐                    │
             ├────►│        HIT          │────────────────────┘
             │     └─────────┬───────────┘
             │               │ (HP <= 0)
             │               ▼
             │     ┌─────────────────────┐
             └────►│       DEATH         │───► DESTROY
                   └─────────────────────┘
```

### State Priority (highest first)
1. **DEATH** -- Nao pode ser interrompido
2. **HIT** -- Interrompe tudo exceto death
3. **SPECIAL** -- Interrompe idle/walk, nao interrompe hit
4. **ATTACK** -- Interrompe idle/walk
5. **WALK** -- Interrompe idle
6. **IDLE** -- Estado default

---

## 9. PERFORMANCE NOTES

- **Total Sprite Memory:** ~1536x64px across all sheets (~96KB uncompressed PNG)
- **Particle Budget:** Max 20 particulas simultaneas para Flavio (waves + confetti + sparkles)
- **Audio Streams:** Max 3 simultaneos (music_sera_beat + sfx + vo)
- **Z-Index:** Base do sprite (Y + height) para Y-sorting isometrico
- **Collision Box:** 24x24px centered on sprite (menor que visual para gameplay justo)
- **Shadow:** Ellipse 20x8px, preto 30% alpha, offset Y: +28px do anchor
