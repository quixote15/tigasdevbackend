# Vassoura da Esplanada - Animation Specification

## Phaser 3 Animation Keys

### Animation: `vassoura_idle`
- **Type:** Loop
- **Frames:** [10, 11]
- **Frame Rate:** 3 fps (slow, deliberate sway)
- **Frame Duration:** 333ms each
- **Repeat:** -1 (infinite loop)
- **Yoyo:** true (ping-pong: 10 -> 11 -> 10 -> 11...)
- **Description:** Bristles sway gently left and right like the broom is breathing. A tiny dust mote floats near the tips. The old broom never fully rests -- decades of sweeping have given it a life of its own.

```javascript
this.anims.create({
    key: 'vassoura_idle',
    frames: this.anims.generateFrameNumbers('weapon_vassoura', { start: 10, end: 11 }),
    frameRate: 3,
    repeat: -1,
    yoyo: true
});
```

---

### Animation: `vassoura_attack`
- **Type:** Play once
- **Frames:** [1, 2, 3, 4]
- **Frame Rate:** 10 fps (slightly slower than chinelo -- heavier weapon)
- **Frame Durations (individual):**
  - Frame 1 (wind-up): 133ms -- deliberate pull-back, the broom has weight
  - Frame 2 (full sweep): 100ms -- acceleration through the arc
  - Frame 3 (contact): 150ms -- held slightly for satisfying impact
  - Frame 4 (follow-through): 133ms -- momentum carrying through
- **Total Duration:** ~516ms
- **Repeat:** 0 (play once)
- **On Complete:** Return to `vassoura_idle`

```javascript
this.anims.create({
    key: 'vassoura_attack',
    frames: [
        { key: 'weapon_vassoura', frame: 1, duration: 133 },
        { key: 'weapon_vassoura', frame: 2, duration: 100 },
        { key: 'weapon_vassoura', frame: 3, duration: 150 },
        { key: 'weapon_vassoura', frame: 4, duration: 133 }
    ],
    frameRate: 10,
    repeat: 0
});
```

---

### Animation: `vassoura_impact`
- **Type:** Play once (overlay effect)
- **Frames:** [5, 6, 7]
- **Frame Rate:** 8 fps
- **Frame Durations (individual):**
  - Frame 5 (appear): 100ms -- dust eruption begins
  - Frame 6 (peak): 150ms -- held for "SWOOOSH" readability
  - Frame 7 (fade): 125ms -- dissipation
- **Total Duration:** ~375ms
- **Repeat:** 0
- **On Complete:** Destroy sprite
- **Spawn Position:** At sweep arc center (offset from player in facing direction)
- **Layer:** Above ground, below UI (depth = target.y + 2)

```javascript
this.anims.create({
    key: 'vassoura_impact',
    frames: [
        { key: 'weapon_vassoura', frame: 5, duration: 100 },
        { key: 'weapon_vassoura', frame: 6, duration: 150 },
        { key: 'weapon_vassoura', frame: 7, duration: 125 }
    ],
    frameRate: 8,
    repeat: 0
});
```

---

### Animation: `vassoura_dust_trail`
- **Type:** Loop (plays during sweep frames 2-4)
- **Frames:** [8, 9]
- **Frame Rate:** 8 fps
- **Frame Duration:** 125ms each
- **Repeat:** -1 (loops while sweep is active, stopped on attack end)
- **Description:** Small ground-level dust puffs that follow the broom head during the sweep, creating a continuous trail effect on the ground.

```javascript
this.anims.create({
    key: 'vassoura_dust_trail',
    frames: this.anims.generateFrameNumbers('weapon_vassoura', { start: 8, end: 9 }),
    frameRate: 8,
    repeat: -1
});
```

---

## Particle Effects

### Continuous Dust Trail (During Sweep, Frames 2-4)
- **Effect:** Ground dust puffs following broom head
- **Emitter:** Follows broom head position with 4px random offset
- **Particle Count:** 1-2 per frame
- **Particle Size:** 3x3px to 5x5px (random)
- **Particle Color:** Random from [`#C4A35A`, `#E8D5A0`, `#8B7D3F`]
- **Particle Speed:** 10-30 px/s (slow drift)
- **Particle Direction:** Perpendicular to sweep direction, slight upward drift
- **Particle Lifespan:** 400-800ms
- **Particle Alpha:** 0.8 -> 0.0 (slow fade)
- **Gravity:** -5 px/s^2 (dust rises slightly)

```javascript
const dustTrail = this.add.particles(x, y, 'particle_dust', {
    speed: { min: 10, max: 30 },
    angle: { min: 0, max: 360 },
    scale: { start: 0.8, end: 0.2 },
    alpha: { start: 0.8, end: 0 },
    lifespan: { min: 400, max: 800 },
    frequency: 80,
    quantity: 1,
    gravityY: -5,
    tint: [0xC4A35A, 0xE8D5A0, 0x8B7D3F],
    emitting: false
});
```

### Impact Dust Burst (On Hit, Frame 3)
- **Effect:** Large dust explosion
- **Particle Count:** 8-12
- **Particle Size:** 4x4px to 8x8px
- **Particle Color:** Dust palette (beige/brown mix)
- **Particle Speed:** 30-80 px/s
- **Particle Direction:** Radial 360deg, biased in sweep direction
- **Particle Lifespan:** 500-1000ms
- **Particle Alpha:** 1.0 -> 0.0
- **Gravity:** -8 px/s^2 (dust billows upward)
- **Additional:** 2-3 "debris" particles (paper scraps, cigarette butts) mixed in
  - Debris Speed: 50-100 px/s
  - Debris Lifespan: 300-600ms
  - Debris Rotation: random spin
  - Debris Color: `#F0F0E8` (paper), `#808080` (cigarette)

```javascript
const dustBurst = this.add.particles(x, y, 'particle_dust', {
    speed: { min: 30, max: 80 },
    angle: { min: sweepAngle - 60, max: sweepAngle + 60 },
    scale: { start: 1.2, end: 0.3 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 500, max: 1000 },
    quantity: 10,
    gravityY: -8,
    tint: [0xC4A35A, 0xE8D5A0, 0x8B7D3F],
    emitting: false
});
```

### Straw Debris (On Hit, Frame 3)
- **Effect:** Broken straw bits fly off
- **Particle Count:** 2-4
- **Particle Size:** 1x3px (elongated)
- **Particle Color:** `#D4A017` (straw)
- **Particle Speed:** 60-120 px/s
- **Particle Direction:** Mostly perpendicular to sweep direction
- **Particle Lifespan:** 200-500ms
- **Particle Rotation:** Random spin 180-360 deg/s
- **Gravity:** 30 px/s^2 (heavier than dust)

---

## Visual Effects

### "SWOOOSH" Onomatopeia
- **Trigger:** On successful hit (damage dealt)
- **Spawn:** At the center of the sweep arc path
- **Animation:** Plays `vassoura_impact` (frames 5-6-7)
- **Scale Tween:**
  - 0ms: scaleX 0.3, scaleY 1.0 (compressed horizontally -- speed squash)
  - 100ms: scaleX 1.3, scaleY 0.9 (stretched wide -- whoosh effect)
  - 250ms: scaleX 1.0, scaleY 1.0 (settle)
  - 375ms: scale 0.7, alpha 0 (fade away with dust)
- **Rotation:** Aligned with sweep direction (so text follows the arc)
- **Depth:** 9999 (always on top)
- **Tint Shift:** Starts at `#DEB887`, shifts toward `#8B7D3F` as it fades (dust integration)

```javascript
const swooosh = this.add.sprite(sweepCenter.x, sweepCenter.y, 'weapon_vassoura', 5);
swooosh.setDepth(9999);
swooosh.setRotation(sweepAngle);

swooosh.play('vassoura_impact');
this.tweens.add({
    targets: swooosh,
    scaleX: { from: 0.3, to: 1.3, duration: 100, ease: 'Cubic.easeOut' },
    onComplete: () => {
        this.tweens.add({
            targets: swooosh,
            scaleX: 1.0,
            scaleY: 1.0,
            duration: 150,
            onComplete: () => {
                this.tweens.add({
                    targets: swooosh,
                    scale: 0.7,
                    alpha: 0,
                    duration: 125,
                    onComplete: () => swooosh.destroy()
                });
            }
        });
    }
});
```

### Screen Shake
- **Trigger:** On successful hit
- **Intensity:** 3px random offset (slightly more than chinelo -- heavier weapon)
- **Duration:** 150ms
- **Decay:** Linear to 0

```javascript
this.cameras.main.shake(150, 0.008);
```

### Dust Fog Overlay (Optional Area Effect)
- **Trigger:** After impact in enclosed areas
- **Effect:** Semi-transparent dust layer covers a 96x96px area around impact
- **Color:** `#C4A35A` at 15% opacity
- **Duration:** 2000ms fade out
- **Gameplay:** Enemies inside dust fog move 20% slower (can't see)

```javascript
const dustFog = this.add.rectangle(impactX, impactY, 96, 96, 0xC4A35A, 0.15);
this.tweens.add({
    targets: dustFog,
    alpha: 0,
    duration: 2000,
    onComplete: () => dustFog.destroy()
});
```

---

## Sound Cue Timing

| Time (ms) | Event               | Sound Key             | Notes                              |
|------------|----------------------|-----------------------|------------------------------------|
| 0          | Attack start         | `sfx_vassoura_whoosh` | Deep wooden whoosh, longer         |
| ~100       | Sweep acceleration   | `sfx_straw_scrape`    | Straw scraping ground              |
| ~233       | Impact moment        | `sfx_vassoura_thud`   | Heavy thud + dust explosion        |
| ~233       | "SWOOOSH" appears    | `sfx_dust_burst`      | Breathy dust burst sound           |
| ~250       | Screen shake start   | (no sound)            | Visual only                        |
| ~300       | Debris settles       | `sfx_debris_tinkle`   | Tiny debris settling sound         |
| ~516       | Attack ends          | (no sound)            | Returns to idle                    |

### Sound Descriptions
- **`sfx_vassoura_whoosh`:** Medium-length (200ms) deep whoosh with wooden resonance. Heavier than chinelo's rubber whoosh. Suggests a heavy pole cutting air. Low-to-mid frequency sweep.
- **`sfx_straw_scrape`:** Short (150ms) scratchy straw-on-concrete sound. High-frequency texture. Like raking leaves on pavement.
- **`sfx_vassoura_thud`:** Heavy (250ms) impact combining dull thud with straw crunch. Low-frequency boom with high-frequency straw snap overlay. Satisfying weight.
- **`sfx_dust_burst`:** Breathy (300ms) puff sound. Like a bag of flour hitting the ground. Mid-frequency "fwoomp" with airy tail.
- **`sfx_debris_tinkle`:** Delicate (200ms) settling sound. Tiny metallic and paper sounds. Very low volume -- ambient detail.

---

## Attack Properties
- **Cooldown:** 700ms (slower than chinelo -- heavier weapon)
- **Attack Arc:** 120 degrees (wide sweep)
- **Range:** 40px from player center (longer than chinelo's 16px)
- **Damage:** Base 18 HP per hit (area damage)
- **Special:** Hits ALL enemies in the sweep arc (not just first contact)
- **Knockback:** 8px push in sweep direction

## Hitbox
- **Shape:** Arc / pie slice
- **Radius:** 40px
- **Arc Angle:** 120 degrees centered on facing direction
- **Active Frames:** Only frames 2 and 3 (full sweep and contact)
- **Multi-hit:** Yes -- all enemies within arc take damage

---

## Integration Notes

### Phaser 3 Sprite Sheet Loading
```javascript
this.load.spritesheet('weapon_vassoura', 'assets/armas/02-vassoura-esplanada/sprites/vassoura.png', {
    frameWidth: 48,
    frameHeight: 48
});
```

### Y-Sort Depth
```javascript
weapon.setDepth(player.y + 1);
// Dust trail particles render at ground level
dustTrail.setDepth(player.y - 10);
// Impact overlay renders above everything
impactOverlay.setDepth(9999);
```

### Sweep Direction
The sweep animation should be flipped based on player facing direction:
```javascript
if (facingLeft) {
    weapon.setFlipX(true);
    // Reverse sweep arc for left-facing
}
```
