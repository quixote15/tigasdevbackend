# Garrafa de Velho Barreiro Incendiaria -- Animation Specification

**Weapon ID:** 08
**Boss:** Lula
**Target FPS:** 10 fps (100ms base frame duration)
**Style:** Twitchy, jerky Andre Guedes animation

---

## 1. Idle Animation (Held Weapon)

**Sprite sheet:** `garrafa-idle.png`
**Frames:** 3 (static + 2 glow variants)
**Loop:** Yes, continuous
**Total cycle:** 400ms

| Frame | Duration | Description                     |
|-------|----------|---------------------------------|
| 1     | 150ms    | Static pose, flame centered     |
| 2     | 125ms    | Flame leans left, glow shift A  |
| 3     | 125ms    | Flame leans right, glow shift B |

### Particle Effects (Idle)
- **Flame embers:** 1-2 particles per 200ms, rising from fuse
  - Color: `#FFD700` (yellow) and `#FF6B00` (orange)
  - Size: 1-2px
  - Velocity: upward 10-15 px/s with slight random X drift (-3 to +3 px/s)
  - Lifespan: 300-500ms
  - Fade: alpha from 1.0 to 0.0 over lifespan

- **Ambient smoke:** 1 wisp per 400ms
  - Color: `#666666` semi-transparent (alpha 0.3)
  - Size: 2-3px, grows to 4-5px
  - Velocity: upward 5-8 px/s
  - Lifespan: 600ms

---

## 2. Throw Animation

**Sprite sheet:** `garrafa-throw.png`
**Frames:** 4
**Loop:** No (plays once per attack)
**Total duration:** 450ms

| Frame | Duration | Description         | Sound Cue                         |
|-------|----------|---------------------|-----------------------------------|
| 1     | 120ms    | Wind-up             | (none)                            |
| 2     | 100ms    | Mid-swing           | `sfx_whoosh_heavy.ogg` at 0ms     |
| 3     | 100ms    | Release             | `sfx_bottle_throw.ogg` at 0ms     |
| 4     | 130ms    | Follow-through      | (none)                            |

### Visual Effects (Throw)
- **Motion lines:** 3 curved lines appear Frame 2-3, fade over 150ms
  - Color: `#1A1A1A` (black) at alpha 0.5, fading to 0.0
- **Amber droplets (Frame 4):** 3-4 particles burst from release point
  - Color: `#C68E17`
  - Size: 2px
  - Velocity: random spread 30-50 px/s, downward drift
  - Lifespan: 200ms
  - Gravity: 80 px/s^2

---

## 3. Projectile Flight

**Sprite sheet:** `garrafa-projectile.png`
**Frames:** 4 (rotation cycle)
**Loop:** Yes (while in flight)
**Total cycle:** 320ms
**Projectile speed:** 180 px/s

| Frame | Duration | Description          |
|-------|----------|----------------------|
| 1     | 80ms     | 0 degree rotation    |
| 2     | 80ms     | 90 degree rotation   |
| 3     | 80ms     | 180 degree rotation  |
| 4     | 80ms     | 270 degree rotation  |

### Particle Trail (Flight)
- **Flame trail:** 3-4 particles per frame
  - Colors: `#FFD700`, `#FF6B00`, `#4488FF` (yellow/orange/blue mix)
  - Size: 2-3px, shrinks to 1px
  - Spawn: at bottle neck position
  - Velocity: opposite of travel direction, 20-40 px/s with slight spread
  - Lifespan: 250-400ms
  - Fade: alpha 0.8 to 0.0

- **Ember dots:** 1-2 per frame
  - Color: `#FFD700`
  - Size: 1px
  - Random scatter from trail
  - Lifespan: 150ms

- **Smoke wisps:** 1 per 2 frames
  - Color: `#888888` alpha 0.2
  - Size: 2px grows to 4px
  - Lifespan: 300ms

### Sound
- `sfx_fire_whoosh_loop.ogg` -- looping while in flight, volume proportional to distance

---

## 4. Impact / Explosion

**Sprite sheet:** `garrafa-explosion.png`
**Frames:** 4
**Loop:** No
**Total duration:** 500ms

| Frame | Duration | Description           | Sound Cue                                  |
|-------|----------|-----------------------|--------------------------------------------|
| 1     | 80ms     | Glass shatter         | `sfx_glass_shatter.ogg` at 0ms             |
| 2     | 120ms    | Fireball expansion    | `sfx_fire_explosion.ogg` at 0ms            |
| 3     | 180ms    | Maximum explosion     | (continuation of explosion)                |
| 4     | 120ms    | Dissipating           | `sfx_fire_crackle_start.ogg` at 0ms        |

### Screen Effects
- **Screen shake:**
  - Trigger: Frame 1 (impact moment)
  - Intensity: 6px random offset
  - Duration: 300ms
  - Decay: exponential falloff
  - Direction: random per-frame

- **Flash:**
  - Trigger: Frame 1
  - Color: `#FFA500` (orange) at alpha 0.3
  - Duration: 100ms full-screen overlay
  - Decay: instant off

- **Camera zoom micro-punch:**
  - Trigger: Frame 2
  - Zoom: 1.02x for 80ms, return to 1.0x

### Particle Effects (Explosion)
- **Glass shards:** 8-12 particles burst
  - Colors: `#4A8B2F`, `#6BBF47`, `#2E5A1C` (greens)
  - Size: 2-4px irregular shapes
  - Velocity: radial outward 80-150 px/s
  - Rotation: random spin
  - Lifespan: 400-600ms
  - Gravity: 60 px/s^2
  - Bounce: 1 bounce at 0.3 coefficient

- **Liquid splash:** 10-15 droplets
  - Color: `#C68E17` (amber)
  - Size: 2-3px
  - Velocity: radial outward 60-120 px/s
  - Lifespan: 300-500ms
  - Gravity: 100 px/s^2

- **Fire particles:** 15-20 particles
  - Colors: `#FFD700`, `#FF6B00`, `#4488FF` mix
  - Size: 3-5px, grows to 5-8px, then shrinks
  - Velocity: radial outward 30-80 px/s, then upward drift
  - Lifespan: 500-800ms

### Onomatopeia
- **"KABOOM!"** text popup
  - Font: bold, jagged edges, comic book style
  - Colors: `#FF6B00` fill, `#1A1A1A` 2px stroke
  - Size: starts 24px, scales to 32px over 200ms, then fades
  - Position: centered on impact
  - Duration: 400ms total
  - Animation: scale up + slight rotation wobble (+/- 5 degrees)

- **"SAUDE!"** secondary text (smaller, satirical toast)
  - Appears 200ms after KABOOM
  - Size: 12px
  - Color: `#F5E6C8`
  - Duration: 300ms
  - Position: offset slightly right and down

---

## 5. Fire Pool (Area Denial)

**Sprite sheet:** `garrafa-firepool.png`
**Frames:** 4
**Loop:** Yes (while pool active)
**Total cycle:** 480ms
**Pool duration:** 5000ms (then fade out over 500ms)

| Frame | Duration | Description       |
|-------|----------|-------------------|
| 1     | 120ms    | Active Pool A     |
| 2     | 120ms    | Active Pool B     |
| 3     | 120ms    | Active Pool C     |
| 4     | 120ms    | Active Pool D     |

### Particle Effects (Fire Pool)
- **Rising flames:** 2-3 particles per frame
  - Colors: `#FFD700`, `#FF6B00`, `#4488FF`
  - Size: 2-4px
  - Velocity: upward 15-30 px/s, slight X wobble
  - Lifespan: 300-500ms
  - Spawn area: within 24px radius of pool center

- **Smoke:** 1 wisp per 200ms
  - Color: `#555555` alpha 0.3
  - Size: 3-5px, grows to 8px
  - Velocity: upward 8-12 px/s
  - Lifespan: 500ms

- **Crackling sparks:** 1 per 300ms
  - Color: `#FFFFFF` then `#FFD700`
  - Size: 1px
  - Velocity: upward burst 40 px/s
  - Lifespan: 100ms

### Sound
- `sfx_fire_crackle_loop.ogg` -- continuous loop while pool active
- Volume: starts 0.8, fades to 0.0 over final 500ms

### Pool Fade-Out (Death)
- Alpha: 1.0 to 0.0 over 500ms (linear)
- Flames reduce in spawn rate: from 3/frame to 0/frame
- Final puff of smoke: 3 large grey particles

---

## 6. "Drunk" Status Effect

**Sprite sheet:** `garrafa-drunk-overlay.png`
**Frames:** 3
**Loop:** Yes (for 3000ms total duration)
**Total cycle:** 360ms

| Frame | Duration | Description     |
|-------|----------|-----------------|
| 1     | 120ms    | Spirals + bottles orbit position A |
| 2     | 120ms    | Spirals + blush + music note       |
| 3     | 120ms    | Spirals + stars + green pulse      |

### Gameplay Effect Visual Feedback
- **Control inversion indicator:**
  - Inverted arrow icons flash above enemy: small arrow pointing opposite direction
  - Color: `#FF0000` pulsing alpha 0.5 to 1.0
  - Cycle: 300ms

- **Enemy sprite tint:**
  - Green-amber overlay: `#C68E17` at alpha 0.15
  - Pulse: alpha oscillates 0.10 to 0.20 over 500ms cycle

- **Stumble offset:**
  - Enemy sprite randomly offsets 1-2px per frame (simulates stumbling)
  - Creates natural "drunk walk" visual

### Sound
- `sfx_drunk_hiccup.ogg` -- plays once at effect start
- `sfx_drunk_mumble_loop.ogg` -- loops for 3 seconds (low volume 0.3)
- `sfx_drunk_end_burp.ogg` -- plays when effect ends

### Effect End
- All overlays fade out over 200ms
- Final "SBRIO!" onomatopeia text popup
  - Color: `#4A8B2F` (green)
  - Size: 10px
  - Duration: 250ms

---

## Phaser 3 Animation Keys

```
garrafa_idle          -- 3 frames, 400ms cycle, loop
garrafa_throw         -- 4 frames, 450ms, no loop
garrafa_projectile    -- 4 frames, 320ms cycle, loop
garrafa_explosion     -- 4 frames, 500ms, no loop
garrafa_firepool      -- 4 frames, 480ms cycle, loop (5s then fade)
garrafa_drunk_overlay -- 3 frames, 360ms cycle, loop (3s duration)
```
