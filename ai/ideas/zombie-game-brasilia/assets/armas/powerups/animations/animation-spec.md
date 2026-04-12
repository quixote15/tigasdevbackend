# Power-Ups — Animation Specification

> Phaser 3 animation configs, timing, particle effects, and screen feedback
> Frame rate: 8-12 fps (jerky Andre Guedes style)
> All durations in milliseconds

---

## 1. Idle / Ground Animations

All power-ups on the ground share the same base behaviors: **pulse**, **bob**, and **glow**. These run continuously from spawn until pickup.

### 1.1 Pulse Animation (Sprite Frame Cycling)

Alternates between `idle_pulse_1` (frame 0) and `idle_pulse_2` (frame 1).

```javascript
// Generic idle pulse — apply to ALL 6 power-ups
const POWERUP_KEYS = [
  'powerup_cafe', 'powerup_coxinha', 'powerup_picanha',
  'powerup_santinho', 'powerup_cracha_vip', 'powerup_emenda_pix'
];

POWERUP_KEYS.forEach(key => {
  this.anims.create({
    key: `${key}_idle`,
    frames: this.anims.generateFrameNumbers(key, { start: 0, end: 1 }),
    frameRate: 3,        // slow, hypnotic pulse (3 fps)
    repeat: -1,          // loop forever
    yoyo: true           // 0 -> 1 -> 0 -> 1 ...
  });
});
```

| Parameter     | Value  | Notes                                      |
|---------------|--------|--------------------------------------------|
| Frame rate    | 3 fps  | Deliberately slow pulse, not frenetic      |
| Repeat        | -1     | Infinite loop                              |
| Yoyo          | true   | Ping-pong between frames 0 and 1          |
| Effective cycle | ~667ms | One full pulse cycle (0->1->0)           |

### 1.2 Vertical Bob (Tween)

Items float 1-2px up and down to signal "I am interactive, pick me up."

```javascript
// Apply to each power-up sprite after spawning
function applyIdleBob(sprite) {
  sprite.scene.tweens.add({
    targets: sprite,
    y: sprite.y - 2,       // bob 2px upward
    duration: 800,         // 800ms per half-cycle
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut' // smooth sinusoidal bob
  });
}
```

| Parameter     | Value          | Notes                                  |
|---------------|----------------|----------------------------------------|
| Amplitude     | 2px            | Subtle, not distracting                |
| Duration      | 800ms half     | 1600ms full cycle                      |
| Ease          | Sine.easeInOut | Smooth floating feel                   |
| Repeat        | -1             | Infinite                               |

### 1.3 Glow Effect (Graphics Overlay)

A colored circle rendered behind the sprite at low opacity, pulsing in sync.

```javascript
function createGlow(scene, sprite, color, baseAlpha) {
  const glow = scene.add.circle(sprite.x, sprite.y, sprite.width * 0.8, color, baseAlpha);
  glow.setBlendMode(Phaser.BlendModes.ADD);
  glow.setDepth(sprite.depth - 1);

  // Pulse the glow in sync with the sprite bob
  scene.tweens.add({
    targets: glow,
    alpha: { from: baseAlpha, to: baseAlpha + 0.15 },
    scaleX: { from: 1.0, to: 1.2 },
    scaleY: { from: 1.0, to: 1.2 },
    duration: 800,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
  });

  return glow;
}
```

#### Glow Colors per Item

| Item          | Glow Color  | Base Alpha | Mood                    |
|---------------|-------------|------------|-------------------------|
| Cafe          | `0xD47820`  | 0.35       | Warm orange (comfort)   |
| Coxinha       | `0xD4A840`  | 0.35       | Warm gold (appetite)    |
| Picanha       | `0xCC4040`  | 0.40       | Deep red (premium)      |
| Santinho      | `0xF0C830`  | 0.40       | Bright yellow (score!)  |
| Cracha VIP    | `0xE0C850`  | 0.45       | Golden prestige (power) |
| Emenda Pix    | `0x4A7C59`  | 0.40       | Toxic green (corruption)|

### 1.4 Item-Specific Idle Particles

Some items have unique idle particles beyond the basic pulse/bob/glow.

#### Cafe: Steam Wisps
```javascript
const steamEmitter = scene.add.particles(sprite.x, sprite.y - 4, 'particle_white', {
  speed: { min: 5, max: 15 },
  angle: { min: 250, max: 290 },  // mostly upward
  scale: { start: 0.3, end: 0 },
  alpha: { start: 0.5, end: 0 },
  lifespan: 600,
  frequency: 400,                  // one wisp every 400ms
  quantity: 1,
  tint: 0xF0E8D8,
  blendMode: 'ADD'
});
```

#### Coxinha: Oil Glint
```javascript
// Occasional sparkle on the crust
const oilEmitter = scene.add.particles(sprite.x, sprite.y, 'particle_sparkle', {
  speed: 0,                         // stationary sparkle
  scale: { start: 0.4, end: 0 },
  alpha: { start: 0.7, end: 0 },
  lifespan: 300,
  frequency: 800,                   // occasional
  quantity: 1,
  tint: 0xE0C060,
  emitZone: {
    type: 'random',
    source: new Phaser.Geom.Circle(0, 0, 6)
  }
});
```

#### Picanha: Sizzle Steam
```javascript
const sizzleEmitter = scene.add.particles(sprite.x, sprite.y - 3, 'particle_white', {
  speed: { min: 8, max: 20 },
  angle: { min: 240, max: 300 },
  scale: { start: 0.4, end: 0 },
  alpha: { start: 0.45, end: 0 },
  lifespan: 500,
  frequency: 300,                   // more frequent than cafe — sizzling
  quantity: 1,
  tint: 0xF0E8D8,
  blendMode: 'ADD'
});
```

#### Santinho: Floating Sparkles
```javascript
const sparkleEmitter = scene.add.particles(sprite.x, sprite.y, 'particle_sparkle', {
  speed: { min: 3, max: 10 },
  angle: { min: 0, max: 360 },
  scale: { start: 0.5, end: 0 },
  alpha: { start: 0.8, end: 0 },
  lifespan: 500,
  frequency: 500,
  quantity: 1,
  tint: 0xFFFFF0,
  emitZone: {
    type: 'random',
    source: new Phaser.Geom.Circle(0, 0, 8)
  }
});
```

#### Cracha VIP: Star Sparkles
```javascript
const starEmitter = scene.add.particles(sprite.x, sprite.y, 'particle_star', {
  speed: { min: 2, max: 8 },
  angle: { min: 0, max: 360 },
  scale: { start: 0.6, end: 0 },
  alpha: { start: 0.9, end: 0 },
  lifespan: 600,
  frequency: 400,
  quantity: 1,
  tint: 0xFFFFF0,
  rotate: { min: 0, max: 360 },
  emitZone: {
    type: 'edge',
    source: new Phaser.Geom.Circle(0, 0, 10),
    quantity: 8
  }
});
```

#### Emenda Pix: Orbiting Green Particles
```javascript
// Green data particles orbiting the diamond
const pixEmitter = scene.add.particles(sprite.x, sprite.y, 'particle_dot', {
  speed: 20,
  angle: { min: 0, max: 360 },
  scale: { start: 0.4, end: 0.1 },
  alpha: { start: 0.7, end: 0.2 },
  lifespan: 1200,
  frequency: 350,
  quantity: 1,
  tint: [0x4A7C59, 0x5A9A6A],      // mix of greens
  emitZone: {
    type: 'edge',
    source: new Phaser.Geom.Circle(0, 0, 10),
    quantity: 12
  }
});
```

---

## 2. Pickup Animations

Triggered when the player collides with/picks up the item. This must feel REWARDING.

### 2.1 Pickup Sprite Animation (Frames 2-3-4)

```javascript
// Generic pickup animation — apply to ALL 6 power-ups
POWERUP_KEYS.forEach(key => {
  this.anims.create({
    key: `${key}_pickup`,
    frames: this.anims.generateFrameNumbers(key, { start: 2, end: 4 }),
    frameRate: 10,         // fast (10 fps) — snappy pickup feel
    repeat: 0,             // play once
    hideOnComplete: true   // sprite disappears after animation
  });
});
```

| Parameter     | Value   | Notes                                     |
|---------------|---------|-------------------------------------------|
| Frame rate    | 10 fps  | Fast and punchy                           |
| Total duration| 300ms   | 3 frames at 10fps                         |
| Repeat        | 0       | Single play                               |
| hideOnComplete| true    | Sprite removed from scene                 |

### 2.2 Pickup Flash (Camera / Overlay)

A brief screen flash tinted to the item's color. Signals "you got something!"

```javascript
function pickupFlash(scene, item, color, intensity) {
  // Full-screen tint flash
  scene.cameras.main.flash(150, 
    (color >> 16) & 0xFF,    // R
    (color >> 8) & 0xFF,     // G
    color & 0xFF,            // B
    true,                    // force
    null,                    // callback
    null                     // context
  );
  // intensity multiplier via alpha of an overlay rectangle
  const overlay = scene.add.rectangle(
    scene.cameras.main.centerX,
    scene.cameras.main.centerY,
    scene.cameras.main.width,
    scene.cameras.main.height,
    color,
    intensity
  ).setScrollFactor(0).setDepth(9999);
  
  scene.tweens.add({
    targets: overlay,
    alpha: 0,
    duration: 200,
    onComplete: () => overlay.destroy()
  });
}
```

#### Flash Parameters per Item

| Item          | Flash Color | Intensity | Duration | Mood            |
|---------------|-------------|-----------|----------|-----------------|
| Cafe          | `0xD47820`  | 0.08      | 150ms    | Subtle warm     |
| Coxinha       | `0xD4A840`  | 0.12      | 150ms    | Moderate warm   |
| Picanha       | `0xCC4040`  | 0.18      | 200ms    | Strong red      |
| Santinho      | `0xF0C830`  | 0.15      | 150ms    | Bright gold     |
| Cracha VIP    | `0xE0C850`  | 0.22      | 250ms    | Intense gold    |
| Emenda Pix    | `0x4A7C59`  | 0.18      | 200ms    | Toxic green     |

> Rare items (Picanha, Cracha VIP) have STRONGER and LONGER flashes. The rarer the item, the more dramatic the feedback.

### 2.3 Pickup Particle Burst

An explosion of particles at the pickup location, colored to match the item.

```javascript
function pickupBurst(scene, x, y, tint, count) {
  const burst = scene.add.particles(x, y, 'particle_dot', {
    speed: { min: 30, max: 80 },
    angle: { min: 0, max: 360 },
    scale: { start: 0.6, end: 0 },
    alpha: { start: 1, end: 0 },
    lifespan: 400,
    quantity: count,
    tint: tint,
    blendMode: 'ADD',
    emitCallback: (particle) => {
      // Add slight gravity pull downward for grounding
      particle.accelerationY = 40;
    }
  });

  // Auto-destroy after particles die
  scene.time.delayedCall(500, () => burst.destroy());
}
```

#### Burst Parameters per Item

| Item          | Tint(s)                     | Count | Notes                           |
|---------------|-----------------------------|-------|---------------------------------|
| Cafe          | `0x6B3A1A`                  | 6     | Brown coffee droplets           |
| Coxinha       | `0xC8952A, 0xD4A840`        | 8     | Golden breadcrumbs              |
| Picanha       | `0x8B2020, 0xE0D0B0`        | 10    | Meat + fat particles            |
| Santinho      | `0xF0E8D0, 0xCC3030, 0x2A3A5A` | 12 | Paper confetti (multi-color)    |
| Cracha VIP    | `0xC8A832, 0xFFFFF0`        | 10    | Gold + star sparkles            |
| Emenda Pix    | `0x4A7C59, 0x5A9A6A, 0xC8A832` | 10 | Green data + gold corruption    |

### 2.4 Pickup Floating Text

Score/heal feedback text that floats upward and fades.

```javascript
function pickupText(scene, x, y, text, color, fontSize) {
  const txt = scene.add.text(x, y - 8, text, {
    fontFamily: '"Press Start 2P", monospace', // pixel font
    fontSize: fontSize,
    color: color,
    stroke: '#1A1A18',
    strokeThickness: 2
  }).setOrigin(0.5).setDepth(9998);

  scene.tweens.add({
    targets: txt,
    y: y - 28,            // float 20px upward
    alpha: { from: 1, to: 0 },
    duration: 800,
    ease: 'Cubic.easeOut',
    onComplete: () => txt.destroy()
  });
}
```

#### Text per Item

| Item          | Text         | Color     | Font Size | Notes                      |
|---------------|--------------|-----------|-----------|----------------------------|
| Cafe          | `"+15%"`     | `#C83030` | 8px       | Small red heal text        |
| Coxinha       | `"+35%"`     | `#C83030` | 10px      | Medium red heal text       |
| Picanha       | `"+60%"`     | `#FFD700` | 12px      | LARGE gold heal text       |
| Santinho      | `"+500"`     | `#F0C830` | 10px      | Yellow score text          |
| Cracha VIP    | `"BLINDADO!"`| `#E0C850` | 10px      | Gold, Brazilian slang      |
| Emenda Pix    | `"2x PIX!"`  | `#5A9A6A` | 10px      | Green multiplier text      |

### 2.5 Pickup Sound Cues (Reference Keys)

| Item          | Sound Key              | Description                               |
|---------------|------------------------|-------------------------------------------|
| Cafe          | `sfx_pickup_cafe`      | Quick slurp + plastic cup crunch          |
| Coxinha       | `sfx_pickup_coxinha`   | Satisfying bite crunch + oil sizzle       |
| Picanha       | `sfx_pickup_picanha`   | Dramatic sizzle + "hmmmm" vocal           |
| Santinho      | `sfx_pickup_santinho`  | Paper flutter + cash register "cha-ching" |
| Cracha VIP    | `sfx_pickup_cracha`    | Metallic badge swipe + shield "BWOMM"     |
| Emenda Pix    | `sfx_pickup_pix`       | Digital "bleep-bloop" Pix notification    |

> Sound design spec is separate (see audio/bordoes/). These keys are placeholders for the audio agent.

### 2.6 Complete Pickup Sequence (Orchestration)

When the player overlaps a power-up, this full sequence executes:

```javascript
function onPickup(scene, player, powerupSprite, itemType) {
  const x = powerupSprite.x;
  const y = powerupSprite.y;
  const config = PICKUP_CONFIG[itemType]; // lookup table with all per-item values

  // 1. Stop idle animations immediately
  powerupSprite.anims.stop();
  if (powerupSprite.bobTween) powerupSprite.bobTween.remove();
  if (powerupSprite.glowSprite) powerupSprite.glowSprite.destroy();
  if (powerupSprite.idleEmitter) powerupSprite.idleEmitter.destroy();

  // 2. Play pickup sprite animation (frames 2-3-4)
  powerupSprite.play(`${config.key}_pickup`);

  // 3. Camera flash (simultaneous)
  pickupFlash(scene, powerupSprite, config.flashColor, config.flashIntensity);

  // 4. Particle burst (simultaneous)
  pickupBurst(scene, x, y, config.burstTints, config.burstCount);

  // 5. Floating text (slight delay for readability)
  scene.time.delayedCall(100, () => {
    pickupText(scene, x, y, config.text, config.textColor, config.fontSize);
  });

  // 6. Sound effect
  scene.sound.play(config.soundKey, { volume: config.soundVolume });

  // 7. Apply gameplay effect
  applyEffect(scene, player, itemType);

  // 8. Screen shake for rare items
  if (config.rarity === 'rare') {
    scene.cameras.main.shake(100, 0.005);
  }
}
```

**Timing summary:**

```
t=0ms     Idle stops, pickup anim starts, flash fires, burst fires, sound plays
t=100ms   Floating text appears
t=100ms   Screen shake (rare items only)
t=300ms   Pickup sprite animation completes (hideOnComplete)
t=400ms   Burst particles fully faded
t=500ms   Flash overlay fully faded
t=800ms   Floating text fully faded and destroyed
```

---

## 3. Active Effect Animations (Timed Power-Ups)

Only applies to **Cracha VIP** (invulnerability) and **Emenda Pix** (score multiplier).

### 3.1 Cracha VIP — Invulnerability Shield Aura

Applied to the PLAYER sprite for 5 seconds after pickup.

#### Shield Overlay Animation (Frames 5-6)

```javascript
this.anims.create({
  key: 'powerup_cracha_vip_active',
  frames: this.anims.generateFrameNumbers('powerup_cracha_vip', { start: 5, end: 6 }),
  frameRate: 6,            // moderate shimmer
  repeat: -1,
  yoyo: true
});
```

#### Shield Aura Implementation

```javascript
function activateCrachaVIP(scene, player) {
  const DURATION = 5000;    // 5 seconds
  const WARN_TIME = 1500;   // last 1.5 seconds: flicker warning

  // Create shield overlay sprite, following player
  const shield = scene.add.sprite(player.x, player.y, 'powerup_cracha_vip');
  shield.play('powerup_cracha_vip_active');
  shield.setBlendMode(Phaser.BlendModes.ADD);
  shield.setAlpha(0.6);
  shield.setDepth(player.depth + 1);

  // Follow player every frame
  const followEvent = scene.events.on('update', () => {
    shield.setPosition(player.x, player.y);
  });

  // Golden tint on player sprite
  player.setTint(0xE0C850);

  // Shield particle ring around player
  const shieldParticles = scene.add.particles(player.x, player.y, 'particle_star', {
    speed: 15,
    angle: { min: 0, max: 360 },
    scale: { start: 0.5, end: 0 },
    alpha: { start: 0.7, end: 0 },
    lifespan: 400,
    frequency: 200,
    quantity: 1,
    tint: [0xC8A832, 0x2E86C1],    // gold + blue
    emitZone: {
      type: 'edge',
      source: new Phaser.Geom.Circle(0, 0, 14),
      quantity: 12
    }
  });

  // Update particle position to follow player
  const particleFollow = scene.events.on('update', () => {
    shieldParticles.setPosition(player.x, player.y);
  });

  // Warning flicker at WARN_TIME before end
  scene.time.delayedCall(DURATION - WARN_TIME, () => {
    // Double the frame rate for frantic flicker
    shield.anims.setTimeScale(2.0);
    
    // Flash the shield alpha rapidly
    scene.tweens.add({
      targets: shield,
      alpha: { from: 0.6, to: 0.15 },
      duration: 100,
      yoyo: true,
      repeat: Math.floor(WARN_TIME / 200),
      ease: 'Stepped',
      easeParams: [2]         // stepped easing = jerky on/off
    });
  });

  // Deactivate after DURATION
  scene.time.delayedCall(DURATION, () => {
    shield.destroy();
    shieldParticles.destroy();
    scene.events.off('update', followEvent);
    scene.events.off('update', particleFollow);
    player.clearTint();
    
    // Brief flash on deactivation
    scene.cameras.main.flash(100, 200, 200, 80);
    
    // "Pop" sound when shield breaks
    scene.sound.play('sfx_shield_break', { volume: 0.6 });
  });
}
```

#### Shield Timeline

```
t=0s        Shield activates. Golden-blue aura appears around player.
            Player tinted gold. Star particles orbit.
            Frame rate: 6 fps (steady shimmer).

t=0-3.5s   Normal active state. Shield pulses calmly.
            Player is INVULNERABLE — all damage = 0.
            Enemies that touch player take 10 knockback damage.

t=3.5s      WARNING PHASE. Shield flicker begins.
            Frame rate doubles to 12 fps.
            Alpha oscillates rapidly (0.6 <-> 0.15).
            This tells the player "shield is ending SOON."

t=5.0s      Shield BREAKS. Brief blue-white camera flash.
            Shield sprite destroyed. Particles pop outward.
            Player tint cleared. "Pop" sound effect.
            Player is vulnerable again.
```

### 3.2 Emenda Pix — Score Multiplier Trail

Applied for 10 seconds after pickup. All score gains are doubled.

#### Multiplier Overlay Animation (Frames 5-6)

```javascript
this.anims.create({
  key: 'powerup_emenda_pix_active',
  frames: this.anims.generateFrameNumbers('powerup_emenda_pix', { start: 5, end: 6 }),
  frameRate: 6,
  repeat: -1,
  yoyo: true
});
```

#### Multiplier Aura Implementation

```javascript
function activateEmendaPix(scene, player) {
  const DURATION = 10000;    // 10 seconds
  const WARN_TIME = 2000;    // last 2 seconds: flicker warning
  const MULTIPLIER = 2;

  // Floating "2x" text above player
  const multiplierText = scene.add.text(player.x, player.y - 16, '2x', {
    fontFamily: '"Press Start 2P", monospace',
    fontSize: '8px',
    color: '#F0C830',
    stroke: '#3D6B3A',
    strokeThickness: 2
  }).setOrigin(0.5).setDepth(player.depth + 2);

  // Bob the text
  scene.tweens.add({
    targets: multiplierText,
    y: multiplierText.y - 3,
    duration: 500,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
  });

  // Green particle trail behind player
  const trailParticles = scene.add.particles(player.x, player.y, 'particle_dot', {
    speed: { min: 5, max: 15 },
    angle: { min: 160, max: 200 },   // trail behind (downward in top-down)
    scale: { start: 0.5, end: 0 },
    alpha: { start: 0.6, end: 0 },
    lifespan: 600,
    frequency: 80,                    // dense trail
    quantity: 1,
    tint: [0x4A7C59, 0x5A9A6A, 0x3D6B3A],
    blendMode: 'ADD'
  });

  // Green aura overlay on player
  const aura = scene.add.sprite(player.x, player.y, 'powerup_emenda_pix');
  aura.play('powerup_emenda_pix_active');
  aura.setBlendMode(Phaser.BlendModes.ADD);
  aura.setAlpha(0.35);
  aura.setDepth(player.depth + 1);

  // Green tint on player
  player.setTint(0x5A9A6A);

  // Follow player
  const followEvent = scene.events.on('update', () => {
    multiplierText.setPosition(player.x, player.y - 16);
    trailParticles.setPosition(player.x, player.y + 4);
    aura.setPosition(player.x, player.y);
  });

  // Set score multiplier
  scene.registry.set('scoreMultiplier', MULTIPLIER);

  // Warning flicker
  scene.time.delayedCall(DURATION - WARN_TIME, () => {
    // Triple frame rate for frantic flicker
    aura.anims.setTimeScale(3.0);
    
    // Multiplier text flashes
    scene.tweens.add({
      targets: multiplierText,
      alpha: { from: 1, to: 0.2 },
      duration: 80,
      yoyo: true,
      repeat: Math.floor(WARN_TIME / 160),
      ease: 'Stepped',
      easeParams: [2]
    });

    // Trail particles thin out
    trailParticles.setFrequency(200);
  });

  // Deactivate
  scene.time.delayedCall(DURATION, () => {
    aura.destroy();
    trailParticles.destroy();
    multiplierText.destroy();
    scene.events.off('update', followEvent);
    player.clearTint();
    scene.registry.set('scoreMultiplier', 1);
    
    // Green flash on deactivation
    scene.cameras.main.flash(100, 74, 124, 89);
    
    scene.sound.play('sfx_pix_end', { volume: 0.5 });
  });
}
```

#### Multiplier Timeline

```
t=0s        Multiplier activates. Green aura appears around player.
            "2x" text floats above player, bobbing.
            Green particle trail follows movement.
            Player tinted green.
            All score gains x2.

t=0-8s      Normal active state. Green aura pulses at 6 fps.
            Dense green particle trail behind player.
            "2x" text bobs steadily.

t=8s        WARNING PHASE. Aura flicker begins.
            Frame rate triples to 18 fps (frantic).
            "2x" text flashes rapidly.
            Trail particles thin out (less frequent).
            This tells the player "multiplier ending SOON."

t=10s       Multiplier ENDS. Brief green camera flash.
            All effects destroyed.
            Player tint cleared.
            Score multiplier reset to 1x.
            Digital "power down" sound.
```

---

## 4. Spawn Animation

When a power-up first appears in the world (dropped by enemy, spawned by wave system).

```javascript
function spawnPowerup(scene, x, y, itemType) {
  const config = PICKUP_CONFIG[itemType];
  const sprite = scene.add.sprite(x, y - 20, config.key); // start 20px above
  sprite.setAlpha(0);
  sprite.setScale(0.3);

  // Drop in from above with bounce
  scene.tweens.add({
    targets: sprite,
    y: y,
    alpha: 1,
    scaleX: 1,
    scaleY: 1,
    duration: 400,
    ease: 'Bounce.easeOut',
    onComplete: () => {
      // Start idle animation after landing
      sprite.play(`${config.key}_idle`);
      applyIdleBob(sprite);
      sprite.glowSprite = createGlow(scene, sprite, config.glowColor, config.glowAlpha);
      // Start item-specific idle particles...
    }
  });

  // Landing impact — small dust puff
  scene.time.delayedCall(350, () => {
    const dust = scene.add.particles(x, y + 4, 'particle_dust', {
      speed: { min: 10, max: 25 },
      angle: { min: 230, max: 310 },
      scale: { start: 0.4, end: 0 },
      alpha: { start: 0.4, end: 0 },
      lifespan: 300,
      quantity: 4,
      tint: 0x8A8580,           // concrete dust color
      gravityY: 30
    });
    scene.time.delayedCall(400, () => dust.destroy());
  });

  return sprite;
}
```

| Phase       | Duration | Description                         |
|-------------|----------|-------------------------------------|
| Drop        | 400ms    | Falls from 20px above with bounce   |
| Scale in    | 400ms    | Grows from 30% to 100% (synced)     |
| Fade in     | 400ms    | 0% to 100% opacity (synced)         |
| Dust puff   | 300ms    | Small ground impact particles        |
| Idle start  | t=400ms  | Pulse/bob/glow begin after landing  |

---

## 5. Despawn Animation (Time-out)

If a power-up is not picked up within its lifetime, it fades away.

```javascript
function despawnPowerup(scene, sprite, lifetime) {
  const WARN_PHASE = 3000; // last 3 seconds: flicker

  // Start warning flicker
  scene.time.delayedCall(lifetime - WARN_PHASE, () => {
    scene.tweens.add({
      targets: sprite,
      alpha: { from: 1, to: 0.2 },
      duration: 150,
      yoyo: true,
      repeat: Math.floor(WARN_PHASE / 300),
    });
  });

  // Final despawn
  scene.time.delayedCall(lifetime, () => {
    // Shrink and fade
    scene.tweens.add({
      targets: sprite,
      scaleX: 0,
      scaleY: 0,
      alpha: 0,
      duration: 200,
      ease: 'Back.easeIn',
      onComplete: () => {
        if (sprite.glowSprite) sprite.glowSprite.destroy();
        if (sprite.idleEmitter) sprite.idleEmitter.destroy();
        sprite.destroy();
      }
    });
  });
}
```

#### Lifetimes per Item

| Item          | Lifetime | Rationale                              |
|---------------|----------|----------------------------------------|
| Cafe          | 15s      | Common, short lived — keep pressure on |
| Coxinha       | 20s      | Moderate, gives time to reach it       |
| Picanha       | 12s      | Rare and powerful — grab it FAST       |
| Santinho      | 15s      | Common, moderate lifetime              |
| Cracha VIP    | 10s      | Very rare — creates urgency            |
| Emenda Pix    | 18s      | Moderate rarity, generous window       |

---

## 6. Required Particle Assets

These tiny textures are needed by the particle emitters above. All are 4x4px or 8x8px PNGs.

| Asset Key          | Size  | Description                                    |
|--------------------|-------|------------------------------------------------|
| `particle_white`   | 4x4   | Soft white circle, feathered edges             |
| `particle_dot`     | 4x4   | Hard-edged colored circle (tinted at runtime)  |
| `particle_sparkle` | 8x8   | 4-point star/diamond shape, white              |
| `particle_star`    | 8x8   | 5-point star shape, white                      |
| `particle_dust`    | 4x4   | Irregular blob shape, gray-brown               |

---

## 7. Performance Notes

- **Max simultaneous power-ups on screen:** 6 (one of each type)
- **Max particles per power-up idle:** 1 emitter, 1-2 active particles at any time
- **Max particles during pickup burst:** 12 (for 400ms only, then destroyed)
- **Active effects (shield/trail):** Max 1 of each at a time; picking up a second refreshes the timer, does not stack
- **All particle emitters** must be destroyed when their parent sprite is destroyed
- **Object pooling** recommended for frequently spawned items (Cafe, Santinho)
- **Blend mode ADD** on glows/particles -- ensure WebGL renderer is active (Phaser default)

---

## 8. Animation Summary Table

| Animation            | Frames     | FPS   | Duration | Repeat | Trigger          |
|----------------------|------------|-------|----------|--------|------------------|
| Idle pulse           | 0-1        | 3     | 667ms/cy | -1     | On spawn         |
| Idle bob (tween)     | n/a        | n/a   | 1600ms/cy| -1     | On spawn         |
| Glow pulse (tween)   | n/a        | n/a   | 1600ms/cy| -1     | On spawn         |
| Spawn drop (tween)   | n/a        | n/a   | 400ms    | 0      | On world spawn   |
| Pickup flash (sprite)| 2-3-4      | 10    | 300ms    | 0      | On player overlap|
| Pickup camera flash   | n/a       | n/a   | 150-250ms| 0      | On player overlap|
| Pickup burst (particles)| n/a    | n/a   | 400ms    | 0      | On player overlap|
| Pickup text (tween)  | n/a        | n/a   | 800ms    | 0      | On player overlap|
| Active aura (shield) | 5-6        | 6/12* | 5000ms   | -1     | Cracha pickup    |
| Active trail (pix)   | 5-6        | 6/18* | 10000ms  | -1     | Emenda pickup    |
| Despawn flicker      | n/a        | n/a   | 3000ms   | ~10    | Before timeout   |
| Despawn shrink       | n/a        | n/a   | 200ms    | 0      | On timeout       |

> *FPS increases during the warning phase before the effect expires.
