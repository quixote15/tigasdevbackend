# Calculadora Infernal - Animation Specification

## Phaser 3 Animation Keys

---

### Animation: `calculadora_idle`
- **Type:** Loop
- **Frames:** [9, 10]
- **Frame Rate:** 6 fps
- **Frame Duration:** 166ms each
- **Repeat:** -1 (infinite loop)
- **Yoyo:** true (ping-pong: 9 -> 10 -> 9 -> 10...)
- **Description:** Calculadora em descanso com teclas que se PRESSIONAM SOZINHAS. A cada ciclo, teclas diferentes afundam e soltam, como se a calculadora estivesse calculando autonomamente. Display mostra o total de impostos acumulados. Glow verde sutil. A calculadora esta VIVA.

```javascript
this.anims.create({
    key: 'calculadora_idle',
    frames: this.anims.generateFrameNumbers('weapon_calculadora', { start: 9, end: 10 }),
    frameRate: 6,
    repeat: -1,
    yoyo: true
});
```

#### Auto-Pressing Keys Effect (Idle)
- **Type:** Overlay tween on key sprites
- **Cycle:** Random keys press every 400-800ms
- **Depth:** 1px depression per key
- **Sound:** Subtle calculator click per press
- **Randomization:** 2 keys active at any time, random selection

```javascript
// Simulated auto-pressing effect
this.time.addEvent({
    delay: Phaser.Math.Between(400, 800),
    callback: () => {
        // Visual: tween key depression overlay
        this.tweens.add({
            targets: keyOverlay,
            y: '+1',
            duration: 80,
            yoyo: true
        });
        this.sound.play('sfx_calc_key_soft', { volume: 0.15 });
    },
    loop: true
});
```

#### Display Glow Pulse (Idle)
- **Type:** Tween on green glow overlay
- **Cycle:** 800ms
- **Alpha:** 0.15 -> 0.25 -> 0.15
- **Scale:** 1.0 -> 1.03 -> 1.0
- **Blend Mode:** ADD
- **Color:** #00FF41

---

### Animation: `calculadora_fire`
- **Type:** Play once
- **Frames:** [1, 2, 3]
- **Frame Rate:** 10 fps
- **Frame Durations (individual):**
  - Frame 1 (charge): 133ms -- numeros freneticos, energia acumula
  - Frame 2 (discharge): 100ms -- DISPARO do cifrao
  - Frame 3 (cooldown): 133ms -- recuperacao, fumaca verde
- **Total Duration:** ~366ms
- **Repeat:** 0 (play once)
- **On Complete:** Return to `calculadora_idle`
- **Description:** A calculadora carrega energia (display frenetico, teclas auto-pressionando), DISPARA um cifrao ($) como projetil do display, e se recupera com fumaca verde. Recuo de arma de fogo no disparo.

```javascript
this.anims.create({
    key: 'calculadora_fire',
    frames: [
        { key: 'weapon_calculadora', frame: 1, duration: 133 },
        { key: 'weapon_calculadora', frame: 2, duration: 100 },
        { key: 'weapon_calculadora', frame: 3, duration: 133 }
    ],
    frameRate: 10,
    repeat: 0
});
```

#### Projectile Spawn (Frame 2)
- **Type:** New sprite spawned at display position
- **Sprite:** Uses projectile frames [4, 5] alternating (rotation animation)
- **Spawn Position:** weapon.x + facing offset, weapon.y - 4 (display position)
- **Direction:** Toward target / facing direction
- **Speed:** 180 px/s
- **Rotation:** Continuous 360 deg/s (spinning dollar)
- **Lifespan:** 2000ms (max travel time before despawn)
- **Trail:** Green energy particles trailing behind

```javascript
// Spawn cifrao projectile
function fireCalculadora(weapon, targetAngle) {
    const cifrao = this.physics.add.sprite(weapon.x, weapon.y - 4, 'weapon_calculadora', 4);
    cifrao.setVelocity(
        Math.cos(targetAngle) * 180,
        Math.sin(targetAngle) * 180
    );

    // Spinning animation
    this.anims.create({
        key: 'cifrao_spin',
        frames: [
            { key: 'weapon_calculadora', frame: 4, duration: 100 },
            { key: 'weapon_calculadora', frame: 5, duration: 100 }
        ],
        frameRate: 10,
        repeat: -1
    });
    cifrao.play('cifrao_spin');

    // Green trail particles
    const trail = this.add.particles(0, 0, 'particle_green', {
        speed: 5,
        lifespan: 200,
        alpha: { start: 0.6, end: 0 },
        scale: { start: 0.5, end: 0 },
        follow: cifrao,
        tint: 0x00FF41,
        quantity: 1,
        frequency: 50
    });

    // Despawn after lifespan
    this.time.delayedCall(2000, () => {
        trail.destroy();
        cifrao.destroy();
    });

    return cifrao;
}
```

#### Recoil Effect (Frame 2)
- **Type:** Calculator sprite kickback
- **Direction:** Opposite to fire direction
- **Distance:** 3px
- **Duration:** 50ms out, 80ms return
- **Ease:** Elastic on return

```javascript
// Recoil
this.tweens.add({
    targets: weapon,
    x: weapon.x - Math.cos(fireAngle) * 3,
    y: weapon.y - Math.sin(fireAngle) * 3,
    duration: 50,
    yoyo: true,
    hold: 0,
    ease: 'Elastic.easeOut'
});
```

#### Display Number Frenzy (Frame 1)
- **Type:** Rapid text change on display overlay
- **Duration:** 133ms (entire charge phase)
- **Text changes:** Every 33ms (4 changes during charge)
- **Content:** Random numbers + tax rates: "15.5%", "R$ 42", "99.9%", "ICMS"

#### Energy Sparks (Frames 1-2)
- **Type:** Particle emitter from display area
- **Count:** 3-6 sparks
- **Size:** 1x1px
- **Color:** #FFFF00 (yellow)
- **Speed:** 30-60 px/s
- **Direction:** Radial from display center
- **Lifespan:** 100-200ms

```javascript
const sparks = this.add.particles(weapon.x, weapon.y - 8, 'particle_spark', {
    speed: { min: 30, max: 60 },
    angle: { min: 0, max: 360 },
    alpha: { start: 1, end: 0 },
    scale: { start: 0.5, end: 0 },
    lifespan: { min: 100, max: 200 },
    quantity: 4,
    tint: 0xFFFF00,
    emitting: false
});
sparks.explode();
```

#### Green Smoke (Frame 3)
- **Type:** 1-2 smoke wisps rising from display
- **Color:** #00FF41 at 20% opacity
- **Direction:** Upward (Y -20px over 400ms)
- **Size:** 3x3px -> 5x5px (expanding)
- **Alpha:** 0.2 -> 0

---

### Animation: `calculadora_impact`
- **Type:** Play once (overlay effect at target position)
- **Frames:** [6, 7, 8]
- **Frame Rate:** 8 fps
- **Frame Durations (individual):**
  - Frame 6 (stamp appear): 100ms -- "TAXADO" slams in
  - Frame 7 (stamp peak): 150ms -- held for max impact + ink drip
  - Frame 8 (stamp fade): 125ms -- dissolving
- **Total Duration:** ~375ms
- **Repeat:** 0
- **On Complete:** Destroy sprite
- **Spawn Position:** At hit target, offset Y -8px
- **Layer:** Depth 9999
- **Description:** O selo "TAXADO" slama no alvo como um carimbo oficial sendo batido. Tinta escorre. Cifroes ($) menores radiam. Numeros de imposto flutuam brevemente.

```javascript
this.anims.create({
    key: 'calculadora_impact',
    frames: [
        { key: 'weapon_calculadora', frame: 6, duration: 100 },
        { key: 'weapon_calculadora', frame: 7, duration: 150 },
        { key: 'weapon_calculadora', frame: 8, duration: 125 }
    ],
    frameRate: 8,
    repeat: 0
});
```

#### "TAXADO" Stamp Effect
- **Spawn:** At target position, offset Y -8px
- **Rotation:** Random +-10 degrees (imperfect stamp)
- **Scale Tween:**
  - 0ms: scale 2.0 (starts BIG -- slamming down from above)
  - 100ms: scale 1.0 (slams to final size, ease Bounce)
  - 250ms: hold at 1.0
  - 375ms: scale 0.85, alpha 0 (fade out)
- **Depth:** 9999

```javascript
const taxado = this.add.sprite(target.x, target.y - 8, 'weapon_calculadora', 6);
taxado.setDepth(9999);
taxado.setScale(2.0);
taxado.setRotation(Phaser.Math.FloatBetween(-0.17, 0.17));

taxado.play('calculadora_impact');
this.tweens.add({
    targets: taxado,
    scale: 1.0,
    duration: 100,
    ease: 'Bounce.easeOut',
    onComplete: () => {
        this.time.delayedCall(150, () => {
            this.tweens.add({
                targets: taxado,
                scale: 0.85,
                alpha: 0,
                duration: 125,
                onComplete: () => taxado.destroy()
            });
        });
    }
});
```

#### Score Drain Effect (On Impact)
- **Visual:** Numbers fly from target to display area
- **Content:** "-50", "-100", "-R$" etc
- **Path:** Arc from target position to weapon position (parabolic)
- **Duration:** 400ms per number
- **Count:** 2-3 numbers
- **Color:** Red (#CC0000) text on numbers being drained

```javascript
function drainScoreVisual(target, weapon, amount) {
    for (let i = 0; i < 3; i++) {
        const num = this.add.text(target.x, target.y, `-${Math.floor(amount/3)}`, {
            fontSize: '8px',
            color: '#CC0000',
            fontFamily: 'monospace'
        });
        num.setDepth(9998);

        this.tweens.add({
            targets: num,
            x: weapon.x,
            y: { value: weapon.y, ease: 'Sine.easeIn' },
            alpha: { from: 1, to: 0.3 },
            duration: 400,
            delay: i * 100,
            onComplete: () => num.destroy()
        });
    }
}
```

#### Ink Drip Effect (Frame 7)
- **Type:** 1-2 red drip particles
- **Spawn:** Bottom edge of "TAXADO" stamp
- **Direction:** Downward (gravity 100 px/s^2)
- **Color:** #CC0000
- **Size:** 1x2px
- **Lifespan:** 300ms
- **Alpha:** 0.8 -> 0

---

## Display Tax Level System

### Tax Accumulated States
Os numeros no display mostram o total de pontos drenados do jogador.

### State: LOW TAX (Frame 11)
- **Trigger:** 0-999 pontos drenados
- **Display:** "R$ 0.00" a "R$ 999"
- **Glow:** Fraco (1px)
- **Fire Rate:** 1 shot / 1.5s (lento)
- **Projectile Speed:** 150 px/s
- **Score Drain:** -10 por hit

### State: MID TAX (Frame 12)
- **Trigger:** 1000-4999 pontos drenados
- **Display:** "R$ 1,000+"
- **Glow:** Medio (2px)
- **Fire Rate:** 1 shot / 1.0s
- **Projectile Speed:** 180 px/s
- **Score Drain:** -25 por hit
- **New ability:** Fires 2 cifroes in spread (15 deg apart)

### State: HIGH TAX / OVERLOAD (Frame 13)
- **Trigger:** 5000+ pontos drenados
- **Display:** "R$ 99,999"
- **Glow:** Intenso (3px) + pulsing
- **Fire Rate:** 1 shot / 0.6s (rapido)
- **Projectile Speed:** 220 px/s
- **Score Drain:** -50 por hit
- **New ability:** Fires 3 cifroes in spread (15 deg apart each)
- **Overload effect:** Calculator body shakes constantly

```javascript
function updateCalculadoraState(weapon, totalTaxDrained) {
    if (totalTaxDrained >= 5000) {
        weapon.setFrame(13); // HIGH/OVERLOAD
        weapon.fireRate = 600;
        weapon.projectileSpeed = 220;
        weapon.scoreDrain = 50;
        weapon.spreadCount = 3;
    } else if (totalTaxDrained >= 1000) {
        weapon.setFrame(12); // MID
        weapon.fireRate = 1000;
        weapon.projectileSpeed = 180;
        weapon.scoreDrain = 25;
        weapon.spreadCount = 2;
    } else {
        weapon.setFrame(11); // LOW
        weapon.fireRate = 1500;
        weapon.projectileSpeed = 150;
        weapon.scoreDrain = 10;
        weapon.spreadCount = 1;
    }
}
```

### Display Number Update
- **Type:** Text overlay on calculator display area
- **Font:** Pixel LCD font, green (#00FF41)
- **Update trigger:** After each successful hit
- **Animation:** Current number -> blink -> new number (100ms)
- **Position:** Fixed on weapon sprite display area (top 8px)

```javascript
function updateDisplayNumber(displayText, newTotal) {
    // Flash effect
    displayText.setAlpha(0);
    this.time.delayedCall(50, () => {
        displayText.setText(`R$${newTotal.toLocaleString()}`);
        displayText.setAlpha(1);
    });
}
```

---

## Projectile ($) Behavior

### Cifrao Spin Animation
```javascript
this.anims.create({
    key: 'cifrao_spin',
    frames: [
        { key: 'weapon_calculadora', frame: 4 },
        { key: 'weapon_calculadora', frame: 5 }
    ],
    frameRate: 10,
    repeat: -1
});
```

### Projectile Physics
- **Speed:** Variable by tax state (150/180/220 px/s)
- **Acceleration:** None (constant speed)
- **Rotation:** 360 deg/s continuous
- **Hitbox:** Circle, 4px radius
- **Damage type:** Score drain (not HP damage)
- **Piercing:** No (destroys on first hit)
- **Bounce:** No
- **Gravity:** None (flies straight)

### On Projectile Hit
1. Projectile sprite destroyed
2. "TAXADO" stamp spawns at target (`calculadora_impact`)
3. Score drain applied (-10/-25/-50 based on state)
4. Target flash: gold tint for 100ms
5. Score drain visual: numbers fly from target to calculator
6. Total tax accumulated increments
7. Display number updates

```javascript
function onCifraoHit(cifrao, target) {
    cifrao.destroy();

    // TAXADO stamp
    spawnTaxadoStamp(target);

    // Score drain
    player.score -= weapon.scoreDrain;
    weapon.totalTaxDrained += weapon.scoreDrain;

    // Target flash
    target.setTint(0xFFD700);
    this.time.delayedCall(100, () => target.clearTint());

    // Score drain visual
    drainScoreVisual(target, weapon, weapon.scoreDrain);

    // Update display
    updateDisplayNumber(weapon.displayText, weapon.totalTaxDrained);

    // Check state change
    updateCalculadoraState(weapon, weapon.totalTaxDrained);
}
```

---

## Sound Cue Timing

| Time (ms) | Event                  | Sound Key                  | Notes                              |
|------------|------------------------|----------------------------|------------------------------------|
| 0          | Fire charge start      | `sfx_calc_charge`          | Electronic charge-up whine         |
| 133        | Fire discharge         | `sfx_calc_fire`            | Cash register BLAST + energy burst |
| 133        | Projectile spawns      | `sfx_cifrao_launch`        | Coin whoosh + zing                 |
| ongoing    | Projectile in flight   | `sfx_cifrao_hum`           | Spinning coin hum (positional)     |
| on hit     | Projectile impact      | `sfx_taxado_slam`          | Heavy stamp SLAM                   |
| on hit     | Score drain            | `sfx_score_drain`          | Coins being sucked + register ring |
| ongoing    | Idle key presses       | `sfx_calc_key_soft`        | Soft calculator key click          |
| state up   | Tax state increase     | `sfx_tax_escalate`         | Ominous escalation tone            |

### Sound Descriptions
- **`sfx_calc_charge`:** (130ms) Electronic charge-up whine. Ascending pitch. Like a capacitor charging. Tension building.
- **`sfx_calc_fire`:** (200ms) BLAST sound: cash register "ka-ching" mixed with energy cannon discharge. Two-part: mechanical + electronic. Satisfying and threatening.
- **`sfx_cifrao_launch`:** (100ms) Coin spinning through air + metallic zing. Like flicking a heavy gold coin at high speed.
- **`sfx_cifrao_hum`:** (loop, positional) Low spinning metallic hum. Pitch shifts with distance (Doppler-lite). Menacing.
- **`sfx_taxado_slam`:** (200ms) HEAVY rubber stamp slamming on paper/surface. Authoritative, final, bureaucratic violence. Deep thud + paper smack.
- **`sfx_score_drain`:** (400ms) Coins being sucked away (descending tinkle) + cash register bell at end. Loss. Financially painful.
- **`sfx_calc_key_soft`:** (30ms) Single soft calculator key press. Subtle. Like typing on a calculator in a quiet office.
- **`sfx_tax_escalate`:** (500ms) Ominous ascending tone. Like an alarm, but fiscal. Growing threat. Brass + electronic hybrid.

---

## Screen Effects

### On Player Hit by Cifrao
- **Screen Shake:** 3px, 120ms
- **Flash:** Gold tint on screen edges, 80ms
- **Score popup:** "-XX" in red, floats up and fades

```javascript
this.cameras.main.shake(120, 0.008);
this.cameras.main.flash(80, 255, 215, 0, false, 0.1); // gold flash
```

### Tax State OVERLOAD (HIGH)
- **Continuous effect:** Calculator hums louder, screen edge has subtle green tint
- **Visual warning:** Pulsing "!" icon near player score UI

---

## Integration Notes

### Phaser 3 Sprite Sheet Loading
```javascript
this.load.spritesheet('weapon_calculadora', 'assets/armas/calculadora-infernal/sprites/calculadora.png', {
    frameWidth: 32,
    frameHeight: 32
});
```

### Hitbox (Weapon itself)
- **Shape:** Rectangle
- **Size:** 28x24px (shield-sized)

### Projectile Hitbox
- **Shape:** Circle
- **Radius:** 4px

### Y-Sort Depth
```javascript
weapon.setDepth(player.y + 1);
```

### Ownership
- Arma principal do Taxadd (Haddad)
- Droppada pelo Zema ao ser derrotado (arma coletavel como loot)
- Quando usada pelo jogador: inversao -- drena score dos INIMIGOS para o jogador
- O display mostra quanto foi "arrecadado" (funciona como score multiplier)

### Attack Cooldown
- **Variable by state:**
  - LOW: 1500ms between shots
  - MID: 1000ms between shots
  - HIGH: 600ms between shots
- **Visual feedback:** Display flickers during cooldown, stable when ready
