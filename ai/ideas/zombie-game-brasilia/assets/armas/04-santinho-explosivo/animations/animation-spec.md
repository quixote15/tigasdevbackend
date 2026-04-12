# Santinho Explosivo - Animation Specification

## Phaser 3 Animation Keys

### Animation: `santinho_idle`
- **Type:** Loop
- **Frames:** [8, 9]
- **Frame Rate:** 6 fps (fast fuse flicker -- urgency)
- **Frame Duration:** 166ms each
- **Repeat:** -1 (infinite loop)
- **Yoyo:** true (8 -> 9 -> 8 -> 9...)
- **Description:** The fuse on the held pamphlet flickers between bright and dim states, creating a sputtering "live explosive" idle feel. The politician's face subtly shifts expression with the flicker -- nervous when bright, fake-calm when dim. The smoke puff drifts between positions.

```javascript
this.anims.create({
    key: 'santinho_idle',
    frames: this.anims.generateFrameNumbers('weapon_santinho', { start: 8, end: 9 }),
    frameRate: 6,
    repeat: -1,
    yoyo: true
});
```

---

### Animation: `santinho_throw`
- **Type:** Play once
- **Frames:** [1, 2, 3]
- **Frame Rate:** 10 fps
- **Frame Durations (individual):**
  - Frame 1 (wind-up): 133ms -- pull back, anticipation
  - Frame 2 (release): 83ms -- fast release snap
  - Frame 3 (initial flight): 100ms -- transition to projectile
- **Total Duration:** ~316ms
- **Repeat:** 0 (play once)
- **On Complete:** Hide held weapon, spawn projectile entity at release position
- **Note:** Projectile spawns at start of Frame 3 (time offset ~216ms from throw start)

```javascript
this.anims.create({
    key: 'santinho_throw',
    frames: [
        { key: 'weapon_santinho', frame: 1, duration: 133 },
        { key: 'weapon_santinho', frame: 2, duration: 83 },
        { key: 'weapon_santinho', frame: 3, duration: 100 }
    ],
    frameRate: 10,
    repeat: 0
});
```

---

### Animation: `santinho_fly`
- **Type:** Loop (plays while projectile is in flight)
- **Frames:** [4, 5, 6, 7] (frisbee spin: face -> edge -> back -> edge)
- **Frame Rate:** 12 fps (fast spin -- jerky Andre Guedes style)
- **Frame Duration:** 83ms each
- **Full Rotation Duration:** ~332ms (one 360-degree spin)
- **Repeat:** -1 (loop until impact or max range)
- **Description:** The santinho tumbles through the air like a deadly frisbee, showing all four orientations in a rapid spin. The fuse burns shorter with each revolution. Spark and smoke trail follow.

```javascript
this.anims.create({
    key: 'santinho_fly',
    frames: this.anims.generateFrameNumbers('weapon_santinho', { start: 4, end: 7 }),
    frameRate: 12,
    repeat: -1
});
```

---

### Animation: `santinho_explode`
- **Type:** Play once (spawned at impact location, SEPARATE spritesheet)
- **Frames:** [0, 1, 2, 3, 4, 5] (from santinho_explosion spritesheet)
- **Frame Rate:** 8 fps
- **Frame Durations (individual):**
  - Frame 0 (detonation): 83ms -- instant flash
  - Frame 1 (fireball peak): 150ms -- held for visual impact and "BOOM!" readability
  - Frame 2 (confetti rain): 166ms -- the star of the show, held for comedy
  - Frame 3 (aftermath): 150ms -- settling dust and debris
  - Frame 4 (smoke A): 133ms -- clearing
  - Frame 5 (smoke B): 133ms -- final clear
- **Total Duration:** ~815ms
- **Repeat:** 0 (play once)
- **On Complete:** Destroy explosion sprite; spawn persistent scorch mark decal
- **Spawn Position:** At projectile impact point
- **Layer:** Depth 9999 (always on top during explosion)

```javascript
this.anims.create({
    key: 'santinho_explode',
    frames: [
        { key: 'santinho_explosion', frame: 0, duration: 83 },
        { key: 'santinho_explosion', frame: 1, duration: 150 },
        { key: 'santinho_explosion', frame: 2, duration: 166 },
        { key: 'santinho_explosion', frame: 3, duration: 150 },
        { key: 'santinho_explosion', frame: 4, duration: 133 },
        { key: 'santinho_explosion', frame: 5, duration: 133 }
    ],
    frameRate: 8,
    repeat: 0
});
```

---

## Particle Effects

### Fuse Sparks (During Idle + Throw, Frames 8-9, 1-3)
- **Effect:** Small sparks sputtering from the fuse tip
- **Emitter Position:** Fuse tip on held weapon
- **Particle Count:** 1-2 per 100ms
- **Particle Size:** 1x1px
- **Particle Color:** Random from [`#FFD700`, `#FF6600`, `#FFFFFF`]
- **Particle Speed:** 15-40 px/s
- **Particle Direction:** Mostly upward (gravity-defying sparks), 120deg spread upward
- **Particle Lifespan:** 100-200ms
- **Particle Alpha:** 1.0 -> 0.0
- **Blend Mode:** ADD

```javascript
const fuseSparks = this.add.particles(fuseX, fuseY, 'particle_spark', {
    speed: { min: 15, max: 40 },
    angle: { min: 240, max: 300 },
    scale: { start: 1, end: 0.1 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 100, max: 200 },
    frequency: 100,
    quantity: 1,
    tint: [0xFFD700, 0xFF6600, 0xFFFFFF],
    blendMode: 'ADD'
});
```

### Smoke Trail (During Flight, Frames 4-7)
- **Effect:** Gray smoke puffs trailing behind the spinning pamphlet
- **Emitter:** Follows projectile position
- **Particle Count:** 1 per 60ms
- **Particle Size:** 2x2px growing to 4x4px
- **Particle Color:** `#666666`
- **Particle Speed:** 5-15 px/s (slow drift)
- **Particle Direction:** Random, slight upward bias
- **Particle Lifespan:** 300-600ms
- **Particle Alpha:** 0.5 -> 0.0
- **Scale:** Start 0.5, end 1.5 (smoke expands)

```javascript
const smokeTrail = this.add.particles(0, 0, 'particle_smoke', {
    follow: projectile,
    speed: { min: 5, max: 15 },
    angle: { min: 250, max: 290 },
    scale: { start: 0.5, end: 1.5 },
    alpha: { start: 0.5, end: 0 },
    lifespan: { min: 300, max: 600 },
    frequency: 60,
    quantity: 1,
    tint: 0x666666
});
```

### Spark Trail (During Flight, Frames 4-7)
- **Effect:** Orange-yellow spark trail from burning fuse
- **Emitter:** Follows projectile position, offset to fuse location
- **Particle Count:** 1-2 per 50ms
- **Particle Size:** 1x1px
- **Particle Color:** Random [`#FFD700`, `#FF6600`]
- **Particle Speed:** 10-30 px/s
- **Particle Direction:** Opposite to flight direction (left behind)
- **Particle Lifespan:** 100-200ms
- **Blend Mode:** ADD

```javascript
const sparkTrail = this.add.particles(0, 0, 'particle_spark', {
    follow: projectile,
    followOffset: { x: -8, y: 0 },
    speed: { min: 10, max: 30 },
    scale: { start: 0.8, end: 0 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 100, max: 200 },
    frequency: 50,
    quantity: 1,
    tint: [0xFFD700, 0xFF6600],
    blendMode: 'ADD'
});
```

### Explosion Confetti Burst (On Impact, Frame 0-2 of explosion)
- **Effect:** Massive colorful confetti explosion
- **Particle Count:** 20-30 (the most particles of any weapon)
- **Particle Size:** 2x2px to 3x3px (varied)
- **Particle Colors:** Random from [`#009B3A`, `#FEDF00`, `#0044CC`, `#FF69B4`, `#F0EDE4`]
- **Particle Speed:** 40-120 px/s (wide range for natural scatter)
- **Particle Direction:** Radial 360deg
- **Particle Lifespan:** 500-1200ms (confetti stays visible long)
- **Particle Alpha:** 1.0 -> 0.0
- **Gravity:** 30 px/s^2 (confetti falls)
- **Rotation:** Random spin 90-360 deg/s (tumbling)
- **Delay:** Stagger -- 10 particles at 0ms, 10 at 50ms, 10 at 100ms

```javascript
const confettiBurst = this.add.particles(impactX, impactY, 'particle_confetti', {
    speed: { min: 40, max: 120 },
    angle: { min: 0, max: 360 },
    scale: { start: 1, end: 0.3 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 500, max: 1200 },
    quantity: 10,
    gravityY: 30,
    rotate: { min: 90, max: 360 },
    tint: [0x009B3A, 0xFEDF00, 0x0044CC, 0xFF69B4, 0xF0EDE4],
    emitting: false,
    frequency: 50,
    maxParticles: 30
});
```

### Paper Debris (On Impact)
- **Effect:** Pamphlet shreds flying out
- **Particle Count:** 4-6
- **Particle Size:** 2x3px (rectangular fragments)
- **Particle Color:** `#F0EDE4` with some `#DEB887` (face skin fragments)
- **Particle Speed:** 50-100 px/s
- **Particle Direction:** Radial 360deg
- **Particle Lifespan:** 300-600ms
- **Gravity:** 25 px/s^2
- **Rotation:** Random spin
- **Special:** 1-2 particles tinted `#DEB887` represent politician face fragments

### Fireball Flash (On Impact, Frame 0)
- **Effect:** Circular expanding flash
- **Type:** Single white circle
- **Start Size:** 6x6px
- **End Size:** 40x40px (large blast radius)
- **Duration:** 150ms
- **Color:** `#FFFFFF` center -> `#FFD700` -> `#FF6B00` edge
- **Blend Mode:** ADD
- **Alpha:** 0.9 -> 0.0

---

## Visual Effects

### "BOOM!" Onomatopeia
- **Trigger:** On explosion (0ms after impact)
- **Spawn:** At impact point, offset Y -12px
- **Style:** BLOCKIER and CHUNKIER than other weapons' text -- this is an EXPLOSION
- **Color:** Bright yellow (#FFD700) with orange (#FF6B00) drop shadow (2px offset)
- **Animation Tween:**
  - 0ms: scale 0.1, alpha 0, rotation random +-15deg
  - 50ms: scale 1.8, alpha 1.0 (explosive pop-in, BIGGER than other weapons)
  - 200ms: scale 1.4 (settle from overshoot)
  - 350ms: scale 1.5, letters begin drifting apart (each letter gets random drift vector)
  - 600ms: scale 1.2, alpha 0.4, letters separated by 3-5px each
  - 815ms: alpha 0 (fade with explosion)
- **Depth:** 10000 (above even the explosion sprite)

```javascript
const boom = this.add.sprite(impactX, impactY - 12, 'santinho_explosion', 1);
boom.setDepth(10000);
boom.setRotation(Phaser.Math.FloatBetween(-0.26, 0.26));

this.tweens.add({
    targets: boom,
    scale: [
        { value: 1.8, duration: 50, ease: 'Back.easeOut' },
        { value: 1.4, duration: 150 },
        { value: 1.2, duration: 300 }
    ],
    alpha: [
        { value: 1, duration: 50 },
        { value: 1, duration: 300 },
        { value: 0, duration: 465 }
    ],
    onComplete: () => boom.destroy()
});
```

### Screen Shake
- **Trigger:** On explosion
- **Intensity:** 6px random offset (THE BIGGEST shake of all weapons)
- **Duration:** 300ms
- **Decay:** Exponential to 0 (sharp initial shake, long rumble tail)

```javascript
this.cameras.main.shake(300, 0.02);
```

### Screen Flash
- **Trigger:** On explosion detonation (Frame 0)
- **Effect:** Entire screen flashes white for 2 frames
- **Duration:** 100ms
- **Color:** White at 60% opacity, then 30%, then gone
- **Implementation:** Camera flash effect

```javascript
this.cameras.main.flash(100, 255, 255, 255, false, (cam, progress) => {
    // Custom alpha curve for 2-frame flash
});
```

### Hit Flash (All Enemies in Blast Radius)
- **Trigger:** On explosion
- **Effect:** All enemies within blast radius flash orange (#FF6B00)
- **Duration:** 150ms
- **Range:** 48px radius from impact point (area damage)

```javascript
enemiesInRange.forEach(enemy => {
    enemy.setTint(0xFF6B00);
    this.time.delayedCall(150, () => enemy.clearTint());
});
```

### Scorch Mark Decal (Persistent)
- **Trigger:** After explosion animation completes
- **Effect:** Dark circular scorch mark left on ground
- **Size:** 16x16px
- **Color:** `#1A1A0D` at 40% opacity
- **Duration:** Persists for 30 seconds, then fades over 5 seconds
- **Depth:** Ground level (below all characters)
- **Max on screen:** 10 (oldest removed when exceeded)

```javascript
const scorch = this.add.circle(impactX, impactY, 8, 0x1A1A0D, 0.4);
scorch.setDepth(0);
this.time.delayedCall(30000, () => {
    this.tweens.add({
        targets: scorch,
        alpha: 0,
        duration: 5000,
        onComplete: () => scorch.destroy()
    });
});
```

---

## Sound Cue Timing

| Time (ms)  | Event                  | Sound Key                   | Notes                            |
|-------------|-------------------------|-----------------------------|----------------------------------|
| 0           | Throw start             | `sfx_santinho_whoosh`       | Paper cutting air                |
| ~83         | Release snap            | `sfx_paper_snap`            | Sharp paper flick                |
| ~216        | Projectile spawns       | `sfx_fuse_sizzle`           | Fuse burning loop starts         |
| (in flight) | Continuous              | `sfx_fuse_sizzle` (loop)    | Sizzling fuse, volume by distance|
| (on impact) | +0ms: Detonation        | `sfx_santinho_explode`      | LOUD explosion with debris       |
| (on impact) | +0ms: Screen flash      | (covered by explosion sfx)  | --                               |
| (on impact) | +50ms: "BOOM!" appears  | `sfx_boom_voice`            | Cartoon "BOOM" vocal sound       |
| (on impact) | +100ms: Confetti        | `sfx_confetti_pop`          | Festive popping confetti sound   |
| (on impact) | +300ms: Debris settling | `sfx_debris_rain`           | Paper and confetti falling        |
| (on impact) | +815ms: Explosion ends  | (no sound)                  | Returns to idle                   |

### Sound Descriptions
- **`sfx_santinho_whoosh`:** Short (100ms) paper-cutting-air whoosh. Lighter and fluttery compared to weapon whooshes. Like throwing a playing card hard.
- **`sfx_paper_snap`:** Very short (50ms) sharp snap. Like flicking a thick piece of card stock. Percussive.
- **`sfx_fuse_sizzle`:** Loopable (100ms loop) sizzling fuse sound. Classic cartoon bomb fuse. High-frequency crackling. Volume increases as fuse gets shorter (builds tension). Doppler shift optional as projectile passes.
- **`sfx_santinho_explode`:** The LOUDEST sound in the game (600ms). Layered explosion: deep boom (low freq), fiery whoosh (mid), paper shredding (high), with a slight echo/reverb tail. Not a military explosion -- a slapstick/comedy explosion with crunch. Think Wile E. Coyote meets Brazilian fireworks (fogos de artificio).
- **`sfx_boom_voice`:** Short (200ms) cartoon vocal "BOOM" -- like a voice saying "BOOM" processed through distortion. Adds humor layer on top of the actual explosion. Deep and exaggerated.
- **`sfx_confetti_pop`:** Festive (200ms) popping sound. Like a party popper / confetti cannon. Multiple small pops layered. Inappropriately cheerful for an explosion -- that is the joke.
- **`sfx_debris_rain`:** Gentle (400ms) settling sound. Paper fluttering, small impacts of confetti on ground. Like ticker-tape parade debris settling. Very soft volume -- ambient aftermath.

---

## Projectile Properties
- **Speed:** 180 px/s (slightly slower than urna vote -- heavier pamphlet)
- **Range:** 200px (about 4 tile widths -- thrown, not launched)
- **Arc:** Optional slight parabolic arc (rises 4px at midpoint, falls back) for frisbee feel
- **Damage (Direct Hit):** 15 HP
- **Damage (Blast Radius):** 30 HP to all enemies within 48px radius
- **Fire Rate:** 1 throw per 1200ms (includes throw animation + new pamphlet grab)
- **Projectile Hitbox:** 10x10px circle (centered on 32x32 sprite)
- **Blast Radius:** 48px circle from impact point
- **Piercing:** No (explodes on first contact)
- **Projectile Lifetime:** 2000ms (explodes on timeout if no hit -- air burst)
- **Ammo:** Limited to 5 per pickup (rare and powerful)

## Special Properties
- **Area of Effect:** ALL enemies within 48px blast radius take damage
- **Self-Damage:** Player takes 10 HP if within 24px of blast (too close!)
- **Friendly Fire Warning:** Screen edges tint orange when holding this weapon
- **Knockback:** 16px push outward from blast center (all affected entities)
- **Status Effect:** Enemies hit are "confused" for 2 seconds (walk randomly)

---

## Integration Notes

### Phaser 3 Sprite Sheet Loading
```javascript
// Held weapon + projectile flight
this.load.spritesheet('weapon_santinho', 'assets/armas/04-santinho-explosivo/sprites/santinho.png', {
    frameWidth: 32,
    frameHeight: 32
});

// Explosion effect (larger sheet)
this.load.spritesheet('santinho_explosion', 'assets/armas/04-santinho-explosivo/sprites/explosion.png', {
    frameWidth: 48,
    frameHeight: 48
});
```

### Projectile Spawn Logic
```javascript
weapon.on('animationupdate', (anim, frame) => {
    if (anim.key === 'santinho_throw' && frame.index === 2) { // Frame 3 = index 2
        // Hide held weapon
        weapon.setVisible(false);
        
        // Spawn projectile
        const santinho = this.physics.add.sprite(player.x, player.y, 'weapon_santinho');
        santinho.play('santinho_fly');
        
        // Start fuse sizzle sound
        const fuse = this.sound.add('sfx_fuse_sizzle', { loop: true });
        fuse.play();
        
        // Calculate velocity with optional arc
        const velocity = aimDirection.normalize().scale(180);
        santinho.setVelocity(velocity.x, velocity.y);
        
        // Set projectile lifetime -- explodes after 2s even without contact
        this.time.delayedCall(2000, () => {
            if (santinho.active) triggerExplosion(santinho.x, santinho.y);
        });
        
        // Start smoke and spark trail emitters
        smokeTrail.startFollow(santinho);
        sparkTrail.startFollow(santinho);
    }
});
```

### Explosion Trigger Logic
```javascript
function triggerExplosion(x, y) {
    // Stop projectile trails
    smokeTrail.stop();
    sparkTrail.stop();
    fuseSound.stop();
    
    // Spawn explosion sprite
    const explosion = this.add.sprite(x, y, 'santinho_explosion');
    explosion.setDepth(9999);
    explosion.play('santinho_explode');
    
    // Screen effects
    this.cameras.main.shake(300, 0.02);
    this.cameras.main.flash(100, 255, 255, 255);
    
    // Play explosion sounds
    this.sound.play('sfx_santinho_explode');
    this.time.delayedCall(50, () => this.sound.play('sfx_boom_voice'));
    this.time.delayedCall(100, () => this.sound.play('sfx_confetti_pop'));
    
    // Spawn confetti particles
    confettiBurst.emitParticleAt(x, y, 30);
    
    // Area damage
    const blastRadius = 48;
    enemies.getChildren().forEach(enemy => {
        const dist = Phaser.Math.Distance.Between(x, y, enemy.x, enemy.y);
        if (dist <= blastRadius) {
            enemy.damage(30);
            enemy.setTint(0xFF6B00);
            // Knockback
            const angle = Phaser.Math.Angle.Between(x, y, enemy.x, enemy.y);
            enemy.setVelocity(Math.cos(angle) * 200, Math.sin(angle) * 200);
        }
    });
    
    // Self-damage check
    const playerDist = Phaser.Math.Distance.Between(x, y, player.x, player.y);
    if (playerDist <= 24) {
        player.damage(10);
    }
    
    // Scorch mark after explosion
    explosion.on('animationcomplete', () => {
        explosion.destroy();
        spawnScorchMark(x, y);
    });
    
    // Re-show held weapon after cooldown
    this.time.delayedCall(1200, () => {
        weapon.setVisible(true);
        weapon.play('santinho_idle');
    });
}
```

### Y-Sort Depth
```javascript
weapon.setDepth(player.y + 1);         // Held weapon above player
projectile.setDepth(projectile.y + 5);  // In-flight above most things
explosion.setDepth(9999);               // Explosion on top
scorchMark.setDepth(0);                 // Scorch at ground level
confetti.setDepth(9998);                // Confetti just below explosion
```
