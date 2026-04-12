# Chinelo Havaianas - Animation Specification

## Phaser 3 Animation Keys

### Animation: `chinelo_idle`
- **Type:** Loop
- **Frames:** [8, 9]
- **Frame Rate:** 4 fps
- **Frame Duration:** 250ms each
- **Repeat:** -1 (infinite loop)
- **Yoyo:** true (ping-pong: 8 -> 9 -> 8 -> 9...)
- **Description:** Gentle rubbery idle sway. The chinelo subtly rocks left/right with a squash-stretch cycle, suggesting the rubber material is alive and ready to strike.

```javascript
// Phaser 3 implementation
this.anims.create({
    key: 'chinelo_idle',
    frames: this.anims.generateFrameNumbers('weapon_chinelo', { start: 8, end: 9 }),
    frameRate: 4,
    repeat: -1,
    yoyo: true
});
```

---

### Animation: `chinelo_attack`
- **Type:** Play once
- **Frames:** [1, 2, 3, 4]
- **Frame Rate:** 12 fps (jerky Andre Guedes style -- fast slap)
- **Frame Durations (individual):**
  - Frame 1 (wind-up): 100ms -- quick pull-back
  - Frame 2 (mid-swing): 66ms -- fastest frame, peak velocity
  - Frame 3 (contact): 133ms -- slightly held for impact feel
  - Frame 4 (follow-through): 100ms -- recovery
- **Total Duration:** ~400ms
- **Repeat:** 0 (play once)
- **On Complete:** Return to `chinelo_idle`

```javascript
this.anims.create({
    key: 'chinelo_attack',
    frames: [
        { key: 'weapon_chinelo', frame: 1, duration: 100 },
        { key: 'weapon_chinelo', frame: 2, duration: 66 },
        { key: 'weapon_chinelo', frame: 3, duration: 133 },
        { key: 'weapon_chinelo', frame: 4, duration: 100 }
    ],
    frameRate: 12,
    repeat: 0
});
```

---

### Animation: `chinelo_impact`
- **Type:** Play once (overlay effect)
- **Frames:** [5, 6, 7]
- **Frame Rate:** 10 fps
- **Frame Durations (individual):**
  - Frame 5 (appear): 80ms -- snappy pop-in
  - Frame 6 (peak): 120ms -- held slightly for readability
  - Frame 7 (fade): 100ms -- quick dissolve
- **Total Duration:** ~300ms
- **Repeat:** 0
- **On Complete:** Destroy sprite (or set visible = false)
- **Spawn Position:** At hit target's position
- **Layer:** Above all game objects (UI overlay or high depth)

```javascript
this.anims.create({
    key: 'chinelo_impact',
    frames: [
        { key: 'weapon_chinelo', frame: 5, duration: 80 },
        { key: 'weapon_chinelo', frame: 6, duration: 120 },
        { key: 'weapon_chinelo', frame: 7, duration: 100 }
    ],
    frameRate: 10,
    repeat: 0
});
```

---

## Particle Effects

### On Attack (Frames 2-3)
- **Effect:** Rubber dust puff
- **Particle Count:** 2-4
- **Particle Size:** 2x2px
- **Particle Color:** `#A0785A` (skin/debris)
- **Particle Speed:** 40-80 px/s
- **Particle Direction:** Radial from impact point, biased in swing direction
- **Particle Lifespan:** 200-400ms
- **Particle Alpha:** 1.0 -> 0.0 (fade out)
- **Gravity:** 20 px/s^2 (slight downward drift)

```javascript
// Phaser 3 particle emitter config
const impactParticles = this.add.particles(x, y, 'particle_debris', {
    speed: { min: 40, max: 80 },
    angle: { min: swingAngle - 45, max: swingAngle + 45 },
    scale: { start: 1, end: 0 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 200, max: 400 },
    quantity: 3,
    gravityY: 20,
    tint: 0xA0785A,
    emitting: false
});
```

### On Hit Confirm (Frame 3)
- **Effect:** Starburst flash
- **Type:** Single white circle expanding
- **Start Size:** 4x4px
- **End Size:** 16x16px
- **Duration:** 100ms
- **Color:** `#FFFFFF` at 80% opacity, fading to 0%
- **Blend Mode:** ADD

---

## Visual Effects

### "THWACK" Onomatopeia
- **Trigger:** On successful hit (damage dealt)
- **Spawn:** At target enemy position, offset Y -8px (above head)
- **Animation:** Plays `chinelo_impact` (frames 5-6-7)
- **Scale Tween:**
  - 0ms: scale 0.5 (pop in small)
  - 80ms: scale 1.2 (overshoot)
  - 200ms: scale 1.0 (settle)
  - 300ms: scale 0.8, alpha 0 (fade out)
- **Rotation:** Random +-10 degrees for organic feel
- **Depth:** 9999 (always on top)

```javascript
// "THWACK" text overlay
const thwack = this.add.sprite(target.x, target.y - 8, 'weapon_chinelo', 5);
thwack.setDepth(9999);
thwack.setRotation(Phaser.Math.FloatBetween(-0.17, 0.17));

thwack.play('chinelo_impact');
this.tweens.add({
    targets: thwack,
    scaleX: { from: 0.5, to: 1.2, duration: 80, ease: 'Back.easeOut' },
    scaleY: { from: 0.5, to: 1.2, duration: 80, ease: 'Back.easeOut' },
    yoyo: false,
    onComplete: () => {
        this.tweens.add({
            targets: thwack,
            scale: 0.8,
            alpha: 0,
            duration: 200,
            onComplete: () => thwack.destroy()
        });
    }
});
```

### Screen Shake
- **Trigger:** On successful hit
- **Intensity:** 2px random offset (X and Y)
- **Duration:** 100ms
- **Decay:** Linear to 0

```javascript
this.cameras.main.shake(100, 0.005);
```

### Hit Flash
- **Trigger:** On successful hit (same frame as screen shake)
- **Effect:** Target enemy flashes white for 1 frame
- **Duration:** 66ms
- **Method:** Set tint to 0xFFFFFF, then clear tint

```javascript
target.setTint(0xFFFFFF);
this.time.delayedCall(66, () => target.clearTint());
```

---

## Sound Cue Timing

| Time (ms) | Event               | Sound Key           | Notes                           |
|------------|----------------------|---------------------|---------------------------------|
| 0          | Attack start         | `sfx_chinelo_whoosh`| Rubber whoosh, short            |
| ~166       | Impact moment        | `sfx_chinelo_slap`  | Loud rubber slap, reverb        |
| ~166       | "THWACK" appears     | `sfx_thwack_pop`    | Comic pop sound                 |
| ~180       | Screen shake start   | (no sound)          | Visual only                     |
| ~400       | Attack ends          | (no sound)          | Returns to idle                 |

### Sound Descriptions
- **`sfx_chinelo_whoosh`:** Short (150ms) rubber-cutting-air sound. Mid-frequency. Like snapping a rubber band through air.
- **`sfx_chinelo_slap`:** Sharp (200ms) rubber-on-flesh slap. Loud crack at start, quick decay. Satisfying "THWACK" sound. Slightly wet/meaty undertone.
- **`sfx_thwack_pop`:** Quick (100ms) comic-book pop. High-pitched percussive burst. Like a balloon pop mixed with a snare hit.

---

## Attack Cooldown
- **Minimum time between attacks:** 500ms
- **Visual feedback:** Chinelo held still (static frame 0) during cooldown, no idle wobble
- **Cooldown end:** Resume `chinelo_idle` animation

## Combo System (Optional)
- **Double-tap attack within 300ms:** Plays attack animation at 1.5x speed
- **Visual:** Second hit shows "THWACK" in larger size (scale 1.5x)
- **Sound:** Second slap plays at +2dB volume

---

## Integration Notes

### Phaser 3 Sprite Sheet Loading
```javascript
this.load.spritesheet('weapon_chinelo', 'assets/armas/01-chinelo-havaianas/sprites/chinelo.png', {
    frameWidth: 32,
    frameHeight: 32
});
```

### Hitbox
- **Shape:** Rectangle
- **Size:** 24x20px (slightly smaller than sprite for fair gameplay)
- **Offset from player:** 16px in facing direction
- **Active frames:** Only frames 2 and 3 (mid-swing and contact)
- **Damage:** Base 10 HP per hit

### Y-Sort Depth
```javascript
weapon.setDepth(player.y + 1); // Always renders just above player
```
