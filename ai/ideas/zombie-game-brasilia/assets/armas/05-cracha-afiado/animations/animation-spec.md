# Cracha Afiado — Animation & Effects Specification

## Weapon Type
**Throwing / Boomerang** — The badge is thrown in an arc, damages enemies in its path, and returns to the player. It spins continuously during flight and leaves a trail of bureaucratic paper fragments.

---

## Animation Cycles

### 1. Throw Animation
**Trigger:** Player attack input
**Total duration:** 400ms

| Frame         | Duration | Description                              |
|---------------|----------|------------------------------------------|
| `throw_01`    | 80ms     | Wind-up: badge pulled back               |
| `throw_02`    | 80ms     | Release: badge leaves hand               |
| `throw_03`    | 120ms    | Spin acceleration (held slightly longer)  |
| `throw_04`    | 120ms    | Full release into projectile state        |

- **Playback:** Once, then transitions to projectile flight loop.
- **Frame rate:** ~10 fps (jerky Andre Guedes style).
- **Player locked:** Player cannot move during frames 1-2 (160ms wind-up lock). Free to move after release.

### 2. Projectile Flight (Looping)
**Trigger:** After throw animation completes
**Total duration per loop:** 400ms (loops until return or max range)

| Frame          | Duration | Description                     |
|----------------|----------|---------------------------------|
| `flight_01`    | 100ms    | 0-degree rotation               |
| `flight_02`    | 100ms    | 90-degree rotation              |
| `flight_03`    | 100ms    | 180-degree rotation             |
| `flight_04`    | 100ms    | 270-degree rotation             |

- **Playback:** Continuous loop. Even frame timing creates smooth, hypnotic spin.
- **Flight path:** Outbound arc (slight curve right), pause at max range (200ms), then return arc (same frames in reverse: 04, 03, 02, 01).
- **Max range:** 180px from player (approximately 5.6 tile widths).
- **Return speed:** 1.3x outbound speed (satisfying snap-back feel).
- **Hitbox:** Active on both outbound and return paths. 24x24px centered hitbox within 32x32 sprite.

### 3. Impact Animation
**Trigger:** Projectile collides with enemy
**Total duration:** 300ms

| Frame          | Duration | Description                                    |
|----------------|----------|------------------------------------------------|
| `impact_01`    | 80ms     | Hit flash + paper burst                         |
| `impact_02`    | 120ms    | Full paper explosion + onomatopoeia (peak)      |
| `impact_03`    | 100ms    | Badge pulls free, begins return                 |

- **Playback:** Once, then resumes flight loop (return path).
- **Note:** Badge does NOT stop on hit. It damages and passes through (piercing), then continues boomerang arc. Impact plays at the hit location as a separate effect overlay.

### 4. Idle Glow (Looping)
**Trigger:** Weapon equipped, player not attacking
**Total duration per loop:** 800ms

| Frame        | Duration | Description                    |
|--------------|----------|--------------------------------|
| `idle_01`    | 400ms    | Shimmer A: glint upper-right/lower-left |
| `idle_02`    | 400ms    | Shimmer B: glint upper-left/lower-right |

- **Playback:** Continuous slow loop. Subtle, non-distracting.
- **Frame rate:** 2.5 fps intentionally slow for idle atmospheric effect.

---

## Particle Effects

### Paper Trail (During Flight)
- **Emitter:** Attached to projectile, offset -8px behind movement direction.
- **Spawn rate:** 1 paper every 80ms (12.5 particles/sec).
- **Particle sprites:** `paper_particle_01`, `paper_particle_02`, `paper_particle_03` (random selection).
- **Particle lifetime:** 600ms.
- **Particle behavior:**
  - Initial velocity: Random 10-30px/s in direction opposite to flight + random lateral offset (-15 to +15 px/s).
  - Rotation: Random spin speed 90-270 deg/s.
  - Scale: Start 1.0, end 0.3 (shrink as they fade).
  - Alpha: Start 0.9, end 0.0 (fade out linearly).
  - Gravity: Slight downward drift 5px/s (simulates paper floating down in top-down pseudo-3D).
- **Max particles alive:** 8 at any time.
- **Visual result:** A fluttering trail of yellowed government documents scattered behind the spinning badge.

### Impact Paper Burst
- **Emitter:** One-shot burst at impact position.
- **Count:** 8-12 paper particles in single burst.
- **Particle sprites:** Same paper particles + additional small white flash particles.
- **Particle behavior:**
  - Radial explosion: velocity 60-120px/s in random 360-degree directions.
  - Rotation: Random high-speed spin 360-720 deg/s.
  - Lifetime: 400ms.
  - Scale: Start 1.2, end 0.0.
  - Alpha: Start 1.0, end 0.0.
- **Visual result:** A satisfying burst of bureaucratic confetti on hit.

### Corner Glint Sparkles (During Flight)
- **Emitter:** Small 1px white dots at each razor corner.
- **Spawn rate:** 1 sparkle per corner per rotation cycle (every 400ms, 4 sparkles per cycle).
- **Particle lifetime:** 150ms.
- **Behavior:** Stationary, flash in then out. Alpha: 0 -> 1.0 -> 0 over 150ms.
- **Visual result:** Razor-sharp corners wink with metallic menace as the badge spins.

---

## Visual Effects

### Onomatopoeia — "PLONK!"
- **Trigger:** On enemy hit.
- **Font style:** Blocky, bold, angular pixel font. Red (#CC0000) with 1px black outline.
- **Size:** 24x12px text sprite.
- **Position:** Appears 8px above impact point.
- **Animation:**
  - 0ms: Scale 0.3, alpha 0.5. Appear.
  - 80ms: Scale 1.2, alpha 1.0. Pop-in overshoot.
  - 160ms: Scale 1.0, alpha 1.0. Settle.
  - 300ms: Scale 1.0, alpha 0.0. Fade out.
  - Total: 300ms.
- **Drift:** Moves upward 6px over its lifetime (floats up).
- **Variant:** On critical hit, text changes to "DEFERIDO!" in green (#228B22). Same timing.

### Screen Shake — On Hit
- **Trigger:** Badge connects with enemy.
- **Intensity:** 2px random offset (mild).
- **Duration:** 120ms.
- **Pattern:** 3 oscillations: right(2px), left(2px), right(1px), center.
- **Note:** Mild shake because the badge is a precision weapon, not a brute-force one.

### Screen Flash — On Hit
- **Trigger:** Same as screen shake.
- **Color:** White (#FFFFFF).
- **Alpha:** 0.15 (very subtle).
- **Duration:** 60ms flash, then fade to 0 over next 60ms.

### Boomerang Return Arc Indicator
- **Trigger:** While badge is in flight.
- **Visual:** A thin (1px) dashed arc line showing the predicted return path.
- **Color:** Gold (#C4A35A) at alpha 0.3.
- **Update:** Redraws each frame based on current badge position and player position.
- **Disappears:** When badge is caught by player.

### Catch Flash
- **Trigger:** Badge returns to player successfully.
- **Visual:** Small gold (#C4A35A) circular burst (8px radius), 4 sparkle particles flying outward.
- **Duration:** 150ms.
- **Sound cue sync:** Catch sound plays at frame 0 of this effect.

---

## Sound Cue Timing

| Event              | Timing                   | Sound Description                                  |
|--------------------|--------------------------|---------------------------------------------------|
| Throw wind-up      | Frame 1 (0ms)            | Sharp metallic "shing" — blade unsheathing sound   |
| Throw release      | Frame 2 (80ms)           | Whipping "whoosh" — fast air displacement           |
| Flight loop        | Each full rotation (400ms)| Subtle spinning "whir-whir" — repeating buzz       |
| Paper trail        | Each spawn (every 80ms)  | Very quiet paper rustle (mix into ambient, low vol) |
| Enemy hit          | Impact frame 1 (0ms)     | Satisfying metallic "THUNK" + paper scatter sound   |
| Onomatopoeia pop   | Impact frame 1 + 40ms    | Comic book "boing" pop (subtle)                     |
| Boomerang return   | Return start             | Reverse whoosh (ascending pitch)                    |
| Player catch       | Catch moment             | Crisp metallic "clink" — badge caught in hand       |
| Idle shimmer       | Each glint (400ms cycle) | Near-silent high-pitched "ting" (barely audible)    |

---

## Damage & Gameplay Timing

| Property                  | Value        |
|---------------------------|--------------|
| Base damage (per hit)     | 15           |
| Return hit damage         | 10           |
| Cooldown after catch      | 300ms        |
| Max flight time           | 1200ms       |
| Stun duration on hit      | 0ms (no stun)|
| Piercing                  | Yes (hits all enemies in path) |
| Max enemies per throw     | Unlimited (path-based)         |
| Critical hit chance        | 10%          |
| Critical hit multiplier    | 2.0x         |

---

## Phaser 3 Implementation Notes

```
Animation keys:
- 'cracha_throw'   → frames 0-3, frameRate: 10, repeat: 0
- 'cracha_flight'  → frames 0-3, frameRate: 10, repeat: -1
- 'cracha_impact'  → frames 0-2, frameRate: 10, repeat: 0
- 'cracha_idle'    → frames 0-1, frameRate: 2, repeat: -1

Projectile path:
- Use Phaser.Curves.QuadraticBezier for boomerang arc
- Control point offset perpendicular to throw direction
- Return path: new curve from current position back to player

Particle emitter config (paper trail):
- emitter.setSpeed({ min: 10, max: 30 })
- emitter.setLifespan(600)
- emitter.setScale({ start: 1.0, end: 0.3 })
- emitter.setAlpha({ start: 0.9, end: 0 })
- emitter.setFrequency(80)
- emitter.setQuantity(1)
```
