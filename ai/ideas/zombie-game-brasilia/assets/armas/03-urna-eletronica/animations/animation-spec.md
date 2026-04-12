# Urna Eletronica - Animation Specification

## Phaser 3 Animation Keys

### Animation: `urna_idle`
- **Type:** Loop
- **Frames:** [9, 10]
- **Frame Rate:** 2 fps (slow, eerie flicker)
- **Frame Duration:** 500ms each
- **Repeat:** -1 (infinite loop)
- **Yoyo:** false (sequential: 9 -> 10 -> 9 -> 10...)
- **Description:** The cracked CRT screen flickers between two static patterns. Exposed wires spark intermittently -- one wire lights up in frame A, a different one in frame B. The machine breathes with a faint green hum. It is always watching, always counting.

```javascript
this.anims.create({
    key: 'urna_idle',
    frames: this.anims.generateFrameNumbers('weapon_urna', { start: 9, end: 10 }),
    frameRate: 2,
    repeat: -1,
    yoyo: false
});
```

---

### Animation: `urna_fire`
- **Type:** Play once
- **Frames:** [1, 2, 3, 4]
- **Frame Rate:** 8 fps
- **Frame Durations (individual):**
  - Frame 1 (charge): 166ms -- deliberate power buildup, player feels the charge
  - Frame 2 (surge): 133ms -- escalating energy, wires arcing
  - Frame 3 (launch): 100ms -- fast ejection, the vote is cast
  - Frame 4 (recoil): 166ms -- machine settling back, smoke rising
- **Total Duration:** ~565ms
- **Repeat:** 0 (play once)
- **On Complete:** Return to `urna_idle`
- **Note:** Projectile spawns at start of Frame 3 (time offset ~299ms from attack start)

```javascript
this.anims.create({
    key: 'urna_fire',
    frames: [
        { key: 'weapon_urna', frame: 1, duration: 166 },
        { key: 'weapon_urna', frame: 2, duration: 133 },
        { key: 'weapon_urna', frame: 3, duration: 100 },
        { key: 'weapon_urna', frame: 4, duration: 166 }
    ],
    frameRate: 8,
    repeat: 0
});
```

---

### Animation: `urna_muzzle`
- **Type:** Play once (overlay, spawned at ejection slot position)
- **Frames:** [5] (single frame, tween handles animation)
- **Duration:** 100ms total
- **Repeat:** 0
- **Scale Tween:**
  - 0ms: scale 0.3, alpha 1.0
  - 50ms: scale 1.5, alpha 0.8
  - 100ms: scale 2.0, alpha 0.0
- **Blend Mode:** ADD
- **On Complete:** Destroy sprite
- **Spawn Position:** At ejection slot (left side of urna, offset X -20, Y 0 from center)

```javascript
const muzzle = this.add.sprite(urna.x - 20, urna.y, 'weapon_urna', 5);
muzzle.setBlendMode(Phaser.BlendModes.ADD);
muzzle.setDepth(9999);
this.tweens.add({
    targets: muzzle,
    scale: { from: 0.3, to: 2.0 },
    alpha: { from: 1.0, to: 0.0 },
    duration: 100,
    ease: 'Cubic.easeOut',
    onComplete: () => muzzle.destroy()
});
```

---

### Animation: `vote_projectile_fly`
- **Type:** Loop (plays while projectile is alive/in flight)
- **Frames:** [0, 1, 2, 3] (from projectile_vote spritesheet)
- **Frame Rate:** 12 fps (fast spin)
- **Frame Duration:** 83ms each
- **Full Rotation Duration:** ~332ms (one complete spin)
- **Repeat:** -1 (loop until projectile hits or leaves screen)
- **Description:** The ballot paper tumbles through the air in a rapid spin. Each frame shows a different rotation angle, creating the illusion of a flat paper spinning like a frisbee. A green tracer glow follows.

```javascript
this.anims.create({
    key: 'vote_projectile_fly',
    frames: this.anims.generateFrameNumbers('projectile_vote', { start: 0, end: 3 }),
    frameRate: 12,
    repeat: -1
});
```

---

### Animation: `urna_impact`
- **Type:** Play once (overlay effect at projectile hit point)
- **Frames:** [6, 7, 8]
- **Frame Rate:** 8 fps
- **Frame Durations (individual):**
  - Frame 6 (appear): 100ms -- "VOTO!" pops in with confetti burst
  - Frame 7 (peak): 150ms -- held for readability, "CONFIRMADO" stamp
  - Frame 8 (fade): 125ms -- dissolve
- **Total Duration:** ~375ms
- **Repeat:** 0
- **On Complete:** Destroy sprite
- **Spawn Position:** At projectile hit location
- **Layer:** Depth 9999 (always on top)

```javascript
this.anims.create({
    key: 'urna_impact',
    frames: [
        { key: 'weapon_urna', frame: 6, duration: 100 },
        { key: 'weapon_urna', frame: 7, duration: 150 },
        { key: 'weapon_urna', frame: 8, duration: 125 }
    ],
    frameRate: 8,
    repeat: 0
});
```

---

## Particle Effects

### Charge-Up Sparks (Frames 1-2)
- **Effect:** Electrical sparks from exposed wires
- **Particle Count:** 2-4 per frame
- **Particle Size:** 1x1px
- **Particle Color:** Random from [`#FFD700`, `#FFFFFF`]
- **Particle Speed:** 20-60 px/s
- **Particle Direction:** Random radial from wire tip positions
- **Particle Lifespan:** 100-250ms (brief sparks)
- **Particle Alpha:** 1.0 -> 0.0
- **Blend Mode:** ADD

```javascript
const chargeSparks = this.add.particles(x, y, 'particle_spark', {
    speed: { min: 20, max: 60 },
    angle: { min: 0, max: 360 },
    scale: { start: 1, end: 0.2 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 100, max: 250 },
    quantity: 3,
    tint: [0xFFD700, 0xFFFFFF],
    blendMode: 'ADD',
    emitting: false
});
```

### Vote Ejection Burst (Frame 3)
- **Effect:** Paper confetti and sparks from ejection slot
- **Particle Count:** 6-10
- **Particle Types:**
  - Paper confetti: 3x3px, white (#F5F5DC), slow (20-50 px/s), long life (400-800ms), flutter rotation
  - Electrical sparks: 1x1px, yellow (#FFD700), fast (60-120 px/s), short life (100-200ms)
- **Direction:** Primarily left (ejection direction), 60deg spread
- **Gravity:** 15 px/s^2 on paper (falls), -5 on sparks (rises briefly)

```javascript
const ejectConfetti = this.add.particles(slotX, slotY, 'particle_paper', {
    speed: { min: 20, max: 50 },
    angle: { min: 150, max: 210 },
    scale: { start: 0.8, end: 0.3 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 400, max: 800 },
    quantity: 4,
    gravityY: 15,
    rotate: { min: 0, max: 360 },
    tint: 0xF5F5DC,
    emitting: false
});
```

### Projectile Trail (During Flight)
- **Effect:** Green tracer glow + faint paper trail
- **Emitter:** Follows projectile position
- **Green Tracer:**
  - Particle Size: 2x2px fading to 1x1px
  - Color: `#00FF41` (screen glow green)
  - Speed: 0 (stationary, left behind)
  - Lifespan: 200ms
  - Alpha: 0.6 -> 0.0
  - Blend Mode: ADD
  - Frequency: Every 50ms
- **Paper Trail:**
  - Particle Size: 1x1px
  - Color: `#F5F5DC` (paper white)
  - Speed: 5-15 px/s (slight drift)
  - Lifespan: 300ms
  - Alpha: 0.3 -> 0.0
  - Frequency: Every 100ms

```javascript
const greenTracer = this.add.particles(0, 0, 'particle_glow', {
    follow: projectile,
    speed: 0,
    scale: { start: 0.5, end: 0.1 },
    alpha: { start: 0.6, end: 0 },
    lifespan: 200,
    frequency: 50,
    tint: 0x00FF41,
    blendMode: 'ADD'
});
```

### Impact Confetti (On Hit)
- **Effect:** Ballot paper explosion
- **Particle Count:** 8-15
- **Particle Types:**
  - Ballot confetti: 3x3px, white (#F5F5DC) with red marks, radial 360deg, 40-100 px/s
  - Green/yellow sparks: 1x1px, Brazil flag colors, radial, 60-140 px/s
  - Ink splatter: 2x2px, red (#CC0000), radial, 30-70 px/s (CONFIRMADO ink)
- **Lifespan:** 300-700ms
- **Gravity:** 20 px/s^2

---

## Visual Effects

### "VOTO!" Onomatopeia
- **Trigger:** On projectile hit (damage dealt)
- **Spawn:** At hit target's position, offset Y -10px
- **Animation:** Plays `urna_impact` (frames 6-7-8)
- **Scale Tween:**
  - 0ms: scale 0.2, alpha 1.0 (pop in small)
  - 60ms: scale 1.3 (overshoot with bounce)
  - 150ms: scale 1.0 (settle)
  - 250ms: scale 1.1, small bounce (confirmation pulse)
  - 375ms: scale 0.6, alpha 0 (fade out)
- **Rotation:** Random +-8 degrees
- **Depth:** 9999

```javascript
const voto = this.add.sprite(target.x, target.y - 10, 'weapon_urna', 6);
voto.setDepth(9999);
voto.setRotation(Phaser.Math.FloatBetween(-0.14, 0.14));
voto.play('urna_impact');

this.tweens.add({
    targets: voto,
    scale: [
        { value: 1.3, duration: 60, ease: 'Back.easeOut' },
        { value: 1.0, duration: 90 },
        { value: 1.1, duration: 100 },
        { value: 0.6, duration: 125 }
    ],
    alpha: { from: 1, to: 0, duration: 375, delay: 0 },
    onComplete: () => voto.destroy()
});
```

### "CONFIRMADO" Screen Flash
- **Trigger:** On fire (Frame 3)
- **Effect:** Brief green tint flash on the weapon sprite
- **Duration:** 100ms
- **Color:** `#00FF41` at 40% tint
- **Implementation:** Tint the weapon sprite green, then clear

```javascript
weapon.setTint(0x00FF41);
this.time.delayedCall(100, () => weapon.clearTint());
```

### Screen Shake
- **Trigger:** On projectile hit
- **Intensity:** 2px (ranged weapons have less shake than melee)
- **Duration:** 80ms
- **Decay:** Linear to 0

```javascript
this.cameras.main.shake(80, 0.004);
```

### Hit Flash
- **Trigger:** On projectile hit
- **Effect:** Target flashes blue (#0066FF) for 1 frame
- **Duration:** 83ms

```javascript
target.setTint(0x0066FF);
this.time.delayedCall(83, () => target.clearTint());
```

### CRT Scan Line Overlay (Optional)
- **Effect:** During charge-up (frames 1-2), overlay thin horizontal scan lines on the weapon
- **Implementation:** Render 1px-tall horizontal lines at 10% opacity green over the screen area
- **Scrolling:** Lines scroll downward at 30px/s for CRT authenticity

---

## Sound Cue Timing

| Time (ms) | Event                 | Sound Key                | Notes                           |
|------------|------------------------|--------------------------|----------------------------------|
| 0          | Charge start           | `sfx_urna_charge`        | Rising electronic hum            |
| ~166       | Power surge peak       | `sfx_urna_surge`         | Electrical crackle intensifies   |
| ~299       | Vote launches          | `sfx_urna_fire`          | Sharp ejection + paper whoosh    |
| ~299       | Muzzle flash           | `sfx_urna_spark`         | Bright electrical snap           |
| ~299       | "CONFIRMADO" voice     | `sfx_confirmado`         | Robotic TTS "Confirmado"         |
| ~465       | Recoil settles         | `sfx_urna_settle`        | Low mechanical clunk             |
| (on hit)   | Impact                 | `sfx_vote_hit`           | Paper slap + electronic beep     |
| (on hit)   | "VOTO!" appears        | `sfx_voto_confirm`       | Triumphant confirmation jingle   |

### Sound Descriptions
- **`sfx_urna_charge`:** Rising electronic hum (400ms). Starts low frequency, sweeps upward. Like a CRT monitor warming up. Slight crackle undertone. Builds tension.
- **`sfx_urna_surge`:** Intense electrical crackle (200ms). Multiple sparking sounds layered. Like a Tesla coil firing. High energy, slightly distorted.
- **`sfx_urna_fire`:** Sharp mechanical ejection (150ms) followed by paper whoosh. A "ka-CHUNK" of the machine mechanism, then the fluttering paper sound fading into distance. Combined mechanical and paper texture.
- **`sfx_urna_spark`:** Bright electrical snap (80ms). Like a camera flash capacitor discharging. Sharp transient.
- **`sfx_confirmado`:** Robotic text-to-speech saying "Confirmado" (500ms). Low-quality, distorted, slightly demonic. The original TSE voice but corrupted. Can be shortened to just "Con-fir-" for faster gameplay feel.
- **`sfx_urna_settle`:** Low mechanical clunk (150ms). Heavy electronic device settling. Transformers humming down. A sigh of exhausted machinery.
- **`sfx_vote_hit`:** Paper slap (100ms) layered with electronic confirmation beep (200ms). The ballot hits flesh, and the machine registers the "vote." Two-part sound.
- **`sfx_voto_confirm`:** Short triumphant jingle (300ms). A corrupted version of the real urna confirmation sound -- 3 ascending electronic tones. Slightly off-key, adding to the grotesque humor.

---

## Projectile Properties
- **Speed:** 200 px/s (moderate -- votes travel with bureaucratic determination)
- **Range:** 280px (about 6 tile widths)
- **Damage:** Base 25 HP per hit
- **Fire Rate:** 1 shot per 800ms (charge time limits rate)
- **Projectile Hitbox:** 12x12px circle (centered on 32x32 sprite)
- **Piercing:** No (projectile destroyed on first hit)
- **Projectile Lifetime:** 1500ms (destroyed if no hit)

## Weapon Hitbox (for melee range -- none)
- This weapon has NO melee hitbox
- Player must rely on projectile accuracy

---

## Integration Notes

### Phaser 3 Sprite Sheet Loading
```javascript
// Weapon body
this.load.spritesheet('weapon_urna', 'assets/armas/03-urna-eletronica/sprites/urna.png', {
    frameWidth: 48,
    frameHeight: 48
});

// Vote projectile
this.load.spritesheet('projectile_vote', 'assets/armas/03-urna-eletronica/sprites/vote.png', {
    frameWidth: 32,
    frameHeight: 32
});
```

### Projectile Spawn Logic
```javascript
// Spawn vote projectile when fire animation reaches frame 3
weapon.on('animationupdate', (anim, frame) => {
    if (anim.key === 'urna_fire' && frame.index === 2) { // 0-indexed, so frame 3 = index 2
        const vote = this.physics.add.sprite(weapon.x - 20, weapon.y, 'projectile_vote');
        vote.play('vote_projectile_fly');
        
        const velocity = new Phaser.Math.Vector2(aimDirection.x, aimDirection.y)
            .normalize()
            .scale(200);
        vote.setVelocity(velocity.x, velocity.y);
        vote.setRotation(Math.atan2(velocity.y, velocity.x));
    }
});
```

### Y-Sort Depth
```javascript
weapon.setDepth(player.y + 1);
projectile.setDepth(projectile.y); // Projectiles sort with world
impactOverlay.setDepth(9999); // "VOTO!" always on top
```
