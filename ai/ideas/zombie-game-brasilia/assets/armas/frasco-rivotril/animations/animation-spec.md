# Frasco de Rivotril Turbo - Animation Specification

## Phaser 3 Animation Keys

---

### Animation: `rivotril_idle`
- **Type:** Loop
- **Frames:** [10, 11]
- **Frame Rate:** 4 fps
- **Frame Duration:** 250ms each
- **Repeat:** -1 (infinite loop)
- **Yoyo:** true (ping-pong: 10 -> 11 -> 10 -> 11...)
- **Description:** Frasco em descanso com sway sutil e liquido borbulhando. Bolhas sobem dentro do liquido azul. O frasco balanca levemente (efeito de vidro pesado). Brilho azulado pulsa.

```javascript
this.anims.create({
    key: 'rivotril_idle',
    frames: this.anims.generateFrameNumbers('weapon_rivotril', { start: 10, end: 11 }),
    frameRate: 4,
    repeat: -1,
    yoyo: true
});
```

---

### Animation: `rivotril_attack`
- **Type:** Play once
- **Frames:** [1, 2, 3]
- **Frame Rate:** 12 fps (jerky Andre Guedes style -- swing pesado)
- **Frame Durations (individual):**
  - Frame 1 (wind-up): 100ms -- puxar frasco pra tras
  - Frame 2 (mid-swing): 66ms -- velocidade maxima (mais rapido)
  - Frame 3 (contact): 150ms -- impacto PESADO (held slightly for weight feel)
- **Total Duration:** ~316ms
- **Repeat:** 0 (play once)
- **On Complete:** Return to `rivotril_idle`
- **Description:** Swing pesado de clava farmaceutica. O frasco e PESADO -- o wind-up e rapido mas o impacto tem PESO. Liquido azul balanca dentro durante o swing. No contato, particulas azuis explodem.

```javascript
this.anims.create({
    key: 'rivotril_attack',
    frames: [
        { key: 'weapon_rivotril', frame: 1, duration: 100 },
        { key: 'weapon_rivotril', frame: 2, duration: 66 },
        { key: 'weapon_rivotril', frame: 3, duration: 150 }
    ],
    frameRate: 12,
    repeat: 0
});
```

---

### Animation: `rivotril_impact`
- **Type:** Play once (overlay effect)
- **Frames:** [4, 5, 6]
- **Frame Rate:** 8 fps
- **Frame Durations (individual):**
  - Frame 4 (appear): 100ms -- "SEDADO" aparece
  - Frame 5 (peak): 150ms -- held longer para leitura + Zzz effect
  - Frame 6 (dissolve): 125ms -- dissolve em particulas
- **Total Duration:** ~375ms
- **Repeat:** 0
- **On Complete:** Destroy sprite (or set visible = false)
- **Spawn Position:** At hit target's position, offset Y -8px
- **Layer:** Above all game objects (depth 9999)
- **Description:** "SEDADO" aparece com ondas azuladas concentricas. Letras tremem como se estivessem sob efeito. Se transformam em "Zzz" antes de desaparecer. Efeito visual inteiro parece "embebedado".

```javascript
this.anims.create({
    key: 'rivotril_impact',
    frames: [
        { key: 'weapon_rivotril', frame: 4, duration: 100 },
        { key: 'weapon_rivotril', frame: 5, duration: 150 },
        { key: 'weapon_rivotril', frame: 6, duration: 125 }
    ],
    frameRate: 8,
    repeat: 0
});
```

---

### Animation: `rivotril_panic`
- **Type:** Loop (while empty)
- **Frames:** [12, 13]
- **Frame Rate:** 10 fps (rapido -- tremor frenetico)
- **Frame Duration:** 100ms each
- **Repeat:** -1 (loops while empty state active)
- **Description:** Frasco vazio tremendo freneticamente. Glow vermelho de panico pulsando. Ciro esta sem Rivotril -- abstinencia. Visual DESESPERADOR. O jogador precisa ATACAR para "recarregar" (metaforicamente).

```javascript
this.anims.create({
    key: 'rivotril_panic',
    frames: this.anims.generateFrameNumbers('weapon_rivotril', { start: 12, end: 13 }),
    frameRate: 10,
    repeat: -1
});
```

---

## Liquid Level System

### Estado: CHEIO (Frame 7 base)
- **Trigger:** Arma com 70-100% de uso restante
- **Visual:** Frasco cheio, glow azul intenso (3px), vidro limpo
- **Idle overlay:** Usa frame 7 como base + idle animation overlay
- **Damage bonus:** +20% dano
- **Sedation duration:** 3s

### Estado: MEIO (Frame 8 base)
- **Trigger:** Arma com 30-69% de uso restante
- **Visual:** Frasco meio cheio, glow reduzido (1px), micro-rachaduras
- **Idle overlay:** Usa frame 8 como base + idle animation (bolhas menores)
- **Damage bonus:** Normal (0%)
- **Sedation duration:** 2s

### Estado: VAZIO (Frame 9 base)
- **Trigger:** Arma com 1-29% de uso restante
- **Visual:** Frasco quase vazio, sem glow, rachaduras visiveis, rotulo gasto
- **Idle overlay:** Usa frame 9 como base + idle reduzido (sem bolhas)
- **Damage bonus:** -30% dano
- **Sedation duration:** 1s

### Estado: PANICO (Frames 12-13)
- **Trigger:** 0% de uso restante (10s sem atacar OU totalmente gasto)
- **Visual:** Frasco vazio tremendo, glow VERMELHO
- **Animation:** `rivotril_panic` loop
- **Efeito em Ciro:** Autoano 5 HP/s, velocidade -30%, visao distorcida
- **Como sair:** Atacar qualquer inimigo (o ato de atacar "recarrega" psicologicamente)

```javascript
// Liquid level state machine
function updateRivotrilState(weapon, usagePercent) {
    if (usagePercent <= 0) {
        weapon.play('rivotril_panic');
        weapon.setTint(0xFF4040); // red tint
        startPanicDamage();
    } else if (usagePercent < 30) {
        weapon.setFrame(9); // empty state base
        weapon.clearTint();
    } else if (usagePercent < 70) {
        weapon.setFrame(8); // mid state base
        weapon.clearTint();
    } else {
        weapon.setFrame(7); // full state base
        weapon.clearTint();
    }
}
```

### Liquid Level Transition Tween
- **Type:** Smooth visual transition between states
- **Duration:** 500ms
- **Method:** Cross-fade between state frames
- **Sound:** Liquid sloshing sound on transition

```javascript
// Transicao visual entre estados
function transitionLiquidLevel(weapon, fromFrame, toFrame) {
    const overlay = this.add.sprite(weapon.x, weapon.y, 'weapon_rivotril', toFrame);
    overlay.setAlpha(0);
    this.tweens.add({
        targets: overlay,
        alpha: 1,
        duration: 500,
        onComplete: () => {
            weapon.setFrame(toFrame);
            overlay.destroy();
        }
    });
}
```

---

## Particle Effects

### On Attack Impact (Frame 3)
- **Effect:** Blue sedation splash
- **Particle Count:** 4-6
- **Particle Size:** 2x2px
- **Particle Color:** `#4AE0FF` (cyan-blue)
- **Particle Speed:** 50-100 px/s
- **Particle Direction:** Radial from impact point, biased in swing direction
- **Particle Lifespan:** 300-500ms
- **Particle Alpha:** 1.0 -> 0.0 (fade out)
- **Gravity:** 15 px/s^2 (slight downward drift -- liquid is heavy)

```javascript
const sedationSplash = this.add.particles(x, y, 'particle_blue_drop', {
    speed: { min: 50, max: 100 },
    angle: { min: swingAngle - 45, max: swingAngle + 45 },
    scale: { start: 1, end: 0 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 300, max: 500 },
    quantity: 5,
    gravityY: 15,
    tint: 0x4AE0FF,
    emitting: false
});
sedationSplash.explode();
```

### Sedation Effect on Target
- **Trigger:** On successful hit
- **Visual:** Target tinted blue (#4A8BB8, 30% overlay) for sedation duration
- **Particle:** "Zzz" sprites floating above target
  - Count: 1 every 800ms
  - Float: Upward 20px over 800ms
  - Scale: 0.5 -> 0 (shrink to nothing)
  - Color: White with blue tint

```javascript
// Sedation tint on target
target.setTint(0x4A8BB8);
this.time.delayedCall(sedationDuration, () => target.clearTint());

// Zzz particles
const zzzEmitter = this.add.particles(target.x, target.y - 16, 'zzz_particle', {
    speedY: -25,
    alpha: { start: 1, end: 0 },
    scale: { start: 0.5, end: 0 },
    lifespan: 800,
    quantity: 1,
    frequency: 800,
    maxParticles: Math.ceil(sedationDuration / 800)
});
```

### Blue Glow Pulse (Idle -- Full State)
- **Type:** Tween on glow overlay sprite
- **Cycle:** 600ms
- **Alpha:** 0.3 -> 0.5 -> 0.3
- **Scale:** 1.0 -> 1.08 -> 1.0
- **Blend Mode:** ADD
- **Color:** #4AE0FF

```javascript
this.tweens.add({
    targets: rivotrilGlow,
    alpha: { from: 0.3, to: 0.5 },
    scaleX: { from: 1.0, to: 1.08 },
    scaleY: { from: 1.0, to: 1.08 },
    duration: 600,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

### Panic Red Pulse (Panic State)
- **Type:** Tween on red glow overlay
- **Cycle:** 300ms (fast, frantic)
- **Alpha:** 0.2 -> 0.7 -> 0.2 (dramatic pulse)
- **Blend Mode:** ADD
- **Color:** #FF2020
- **Additional:** Screen edge vignette tinted red (5% opacity)

```javascript
this.tweens.add({
    targets: panicGlow,
    alpha: { from: 0.2, to: 0.7 },
    duration: 300,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

---

## Visual Effects

### "SEDADO" Onomatopoeia
- **Trigger:** On successful hit (damage dealt)
- **Spawn:** At target enemy position, offset Y -8px
- **Animation:** Plays `rivotril_impact` (frames 4-5-6)
- **Scale Tween:**
  - 0ms: scale 0.5 (pop in small)
  - 100ms: scale 1.1 (overshoot with wobble -- sedated feel)
  - 250ms: scale 1.0 (settle, but WOBBLING slightly)
  - 375ms: scale 0.7, alpha 0 (dissolve out)
- **Rotation:** Oscillating +-5 degrees during display (wobbly/drugged look)
- **Depth:** 9999
- **Color scheme:** Yellow text (#F4D03F) + Blue shadow (#2A80B0)

```javascript
const sedado = this.add.sprite(target.x, target.y - 8, 'weapon_rivotril', 4);
sedado.setDepth(9999);
sedado.play('rivotril_impact');

// Wobble rotation (sedated feel)
this.tweens.add({
    targets: sedado,
    angle: { from: -5, to: 5 },
    duration: 150,
    yoyo: true,
    repeat: 2
});

// Scale pop
this.tweens.add({
    targets: sedado,
    scaleX: { from: 0.5, to: 1.1, duration: 100, ease: 'Back.easeOut' },
    scaleY: { from: 0.5, to: 1.1, duration: 100, ease: 'Back.easeOut' },
    onComplete: () => {
        this.tweens.add({
            targets: sedado,
            scale: 0.7,
            alpha: 0,
            duration: 275,
            onComplete: () => sedado.destroy()
        });
    }
});
```

### Screen Effects (Panic State)
- **Red Vignette:** Camera post-processing, red tint at screen edges
- **Chromatic Aberration:** Slight RGB split (1px offset) -- "withdrawal" visual
- **Screen Shake:** Continuous micro-shake 1px, 50ms period

```javascript
// Panic screen effects
this.cameras.main.setBackgroundColor('rgba(255, 0, 0, 0.05)');
this.cameras.main.shake(999999, 0.002); // continuous micro-shake
```

### Liquid Slosh (During Swing)
- **Visual:** Blue liquid sprite inside bottle tilts opposite to swing direction
- **Frame 1:** Liquid tilts right (swing going left)
- **Frame 2:** Liquid hits right wall and splashes
- **Frame 3:** Liquid splashes back on impact

---

## Sound Cue Timing

| Time (ms) | Event               | Sound Key              | Notes                              |
|------------|----------------------|------------------------|------------------------------------|
| 0          | Attack start         | `sfx_rivotril_swoosh`  | Heavy glass whoosh (weighty)       |
| ~166       | Impact               | `sfx_rivotril_smash`   | Glass-on-flesh + liquid splash     |
| ~166       | "SEDADO" appears     | `sfx_sedado_pop`       | Drugged pop + Zzz whisper          |
| ~166       | Liquid splash        | `sfx_liquid_splash`    | Blue liquid splatter               |
| ongoing    | Sedation active      | `sfx_sedated_drone`    | Low drone/hum while target sedated |
| ongoing    | Panic state          | `sfx_withdrawal_buzz`  | Frantic buzz/heartbeat             |
| transition | Level change         | `sfx_liquid_slosh`     | Liquid sloshing in bottle          |

### Sound Descriptions
- **`sfx_rivotril_swoosh`:** (150ms) Heavy glass-through-air whoosh. Lower pitch than chinelo. Weighty, like swinging a bottle.
- **`sfx_rivotril_smash`:** (250ms) Glass impact + liquid splash. Two-part: hard THUNK + wet splatter. Satisfying but grotesque.
- **`sfx_sedado_pop`:** (200ms) Dreamy pop sound + whispered "Zzz". Like a bubble popping underwater. Slightly reverbed.
- **`sfx_liquid_splash`:** (150ms) Liquid splatter. Blue-coded (associated with sedation). Wet and medical.
- **`sfx_sedated_drone`:** (loop, 2-3s) Low frequency drone/hum. Sedation atmosphere. Like slow heartbeat + ambient pharmacy hum.
- **`sfx_withdrawal_buzz`:** (loop) Frantic heartbeat + electrical buzz. Anxiety sound. Pitch rises over time (10s -> crescendo).
- **`sfx_liquid_slosh`:** (200ms) Liquid sloshing inside glass container. Level-dependent: more liquid = heavier slosh.

---

## Rivotril-Specific Mechanics

### Usage Timer (Panic Mechanic)
```
10s without attacking
    → Ciro enters panic
    → rivotril_panic animation plays
    → 5 HP/s self-damage
    → Player MUST attack to reset timer
    → Each attack resets timer to 10s
    → Visual: liquid level represents timer (drains over 10s)
```

### Sedation Debuff on Enemy
```
On hit:
    → Target speed: -50% for sedation duration
    → Target tint: blue overlay 30%
    → "Zzz" particles above target
    → Sedation duration based on liquid level:
        Full: 3.0s
        Mid: 2.0s
        Empty: 1.0s
```

### Attack Cooldown
- **Minimum time between attacks:** 600ms (heavier weapon = slower)
- **Visual feedback:** Frasco held still during cooldown, no idle wobble
- **Cooldown end:** Resume `rivotril_idle`

---

## Integration Notes

### Phaser 3 Sprite Sheet Loading
```javascript
this.load.spritesheet('weapon_rivotril', 'assets/armas/frasco-rivotril/sprites/rivotril.png', {
    frameWidth: 32,
    frameHeight: 32
});
```

### Hitbox
- **Shape:** Rectangle
- **Size:** 20x24px (slightly smaller than sprite)
- **Offset from player:** 18px in facing direction (heavier weapon = closer range)
- **Active frames:** Only frames 2 and 3 (mid-swing and contact)
- **Base Damage:** 15 HP per hit (heavier than chinelo)

### Y-Sort Depth
```javascript
weapon.setDepth(player.y + 1);
```

### Ciro-Specific Integration
- This weapon is BOUND to Ciro -- cannot be used by other characters
- The panic mechanic ties to Ciro's personality (addiction/dependency)
- Visual: when Ciro holds it, his hand trembles slightly (idle overlay)
- If Ciro drops the weapon (death), the frasco shatters with blue liquid pool
