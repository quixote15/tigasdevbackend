# Carimbo de Protocolo — Animation & Effects Specification

## Weapon Type
**Melee Special** — A devastating ground-slam weapon that stuns enemies on hit. The comically oversized rubber stamp is raised high and brought down with earth-shaking force, leaving an "INDEFERIDO" mark on everything it hits. Slow but powerful, with area-of-effect stun.

---

## Animation Cycles

### 1. Swing / Slam Animation
**Trigger:** Player attack input
**Total duration:** 550ms

| Frame          | Duration | Description                                    |
|----------------|----------|------------------------------------------------|
| `swing_01`     | 100ms    | Raise: stamp lifted overhead                   |
| `swing_02`     | 150ms    | Apex: dramatic pause at maximum height (longer for comedic timing) |
| `swing_03`     | 80ms     | Downswing: violent fast descent (shortest frame = speed) |
| `swing_04`     | 220ms    | SLAM: ground impact held for weight (longest frame = impact) |

- **Playback:** Once per attack. Cannot cancel mid-animation.
- **Frame rate:** Variable (see durations). Deliberately uneven for Andre Guedes jerky style.
- **Player locked:** Full movement lock during entire 550ms. The player commits to the slam. This is the weapon's tradeoff — devastating but leaves you vulnerable.
- **Hitbox active:** Only on Frame 4 (slam). Damage dealt at the 330ms mark.
- **Attack area:** 40x40px rectangle in front of player (AoE zone).

### 2. Impact / Stun Effect
**Trigger:** Stamp connects with one or more enemies (overlaps with slam Frame 4)
**Total duration:** 400ms

| Frame           | Duration | Description                                  |
|-----------------|----------|----------------------------------------------|
| `impact_01`     | 80ms     | Hit flash + ink explosion begin               |
| `impact_02`     | 180ms    | Peak: full ink spread + "INDEFERIDO" stamp visible (held long for readability) |
| `impact_03`     | 140ms    | Recovery: stamp lifts with sticky ink strand   |

- **Playback:** Once per hit. Plays as an overlay effect at the hit position, independent of weapon sprite.
- **Frame rate:** ~8 fps.
- **Multiple enemies:** If slam hits 3 enemies, 3 separate impact effects play simultaneously at each enemy position.

### 3. Stun Stars (Looping on Stunned Enemy)
**Trigger:** Enemy hit by stamp
**Duration:** Loops for full stun duration (1500ms)

| Frame             | Duration | Description                        |
|-------------------|----------|------------------------------------|
| `stun_star_rot_0` | 250ms    | Three gold stars at 0-degree orbit |
| `stun_star_rot_1` | 250ms    | Stars rotated 30 degrees           |
| `stun_star_rot_2` | 250ms    | Stars rotated 60 degrees           |
| `stun_star_rot_3` | 250ms    | Stars rotated 90 degrees           |

- **Playback:** Loops 1.5 times over 1500ms stun duration, then stars shrink and vanish (200ms fade-out).
- **Position:** Centered above the stunned enemy sprite, orbiting in a circle (12px radius).
- **Note:** Stun stars are a shared sprite used by the stun system, not weapon-specific. But this weapon is the primary stun source.

### 4. Idle Glow (Looping)
**Trigger:** Weapon equipped, player not attacking
**Total duration per loop:** 1200ms

| Frame         | Duration | Description                     |
|---------------|----------|---------------------------------|
| `idle_01`     | 600ms    | Ink drip forming on stamp base  |
| `idle_02`     | 600ms    | Drip has fallen, reset          |

- **Playback:** Continuous slow loop. The stamp's idle is deliberately slow and menacing.
- **Frame rate:** ~1.7 fps (extremely slow, atmospheric).
- **Supplemental animation:** The tiny fly buzzes in a procedural random pattern (not frame-based; a separate sprite that orbits the stamp with Phaser tween random paths, speed 20-40px/s, reversing direction every 800-1200ms).

---

## Particle Effects

### Ink Splatter (On Slam)
- **Emitter:** One-shot burst at slam impact position.
- **Count:** 10-16 ink particles per slam.
- **Particle sprites:** `ink_splat_01`, `ink_splat_02`, `ink_splat_03` (weighted: 40% blob, 35% streak, 25% drop).
- **Particle behavior:**
  - Radial explosion: velocity 80-160px/s in random 360-degree directions.
  - Rotation: Random -180 to 180 degrees (ink tumbles).
  - Lifetime: 500ms.
  - Scale: Start 1.0, end 0.6 (shrinks slightly as it settles).
  - Alpha: Start 1.0, end 0.3 (fades but doesn't fully disappear — ink stains remain).
  - Gravity: 0 (top-down view, ink lands on ground plane).
- **Ink stain persistence:** After particles fade, they leave behind static decals at their final positions for 5 seconds (alpha 0.3, then fade to 0 over 2 seconds). This creates accumulating ink mess.
- **Visual result:** A violent splatter of red bureaucratic ink radiating from every stamp slam.

### Dust Cloud (On Slam)
- **Emitter:** One-shot burst at slam position, layered behind ink splatters.
- **Count:** 6-8 dust particles.
- **Particle sprites:** Simple 8x8 brown-gray circles (#C4B99F) with soft edges.
- **Particle behavior:**
  - Radial expansion: velocity 40-80px/s outward.
  - Lifetime: 350ms.
  - Scale: Start 0.5, end 2.0 (dust expands as it dissipates).
  - Alpha: Start 0.6, end 0.0.
- **Visual result:** A ground-level dust eruption from the impact force, giving weight to the slam.

### Ink Drip (During Idle)
- **Emitter:** Slow single-particle drip from stamp base.
- **Spawn rate:** 1 drip every 1200ms (synced to idle loop).
- **Particle sprite:** `ink_splat_03` (small round drop).
- **Particle behavior:**
  - Velocity: 15px/s downward (toward ground in isometric Y).
  - Lifetime: 400ms.
  - Scale: Start 0.5, end 0.8 (grows slightly as it falls, like a real drip).
  - Alpha: 1.0 constant until last 100ms, then fade to 0.
- **Ground splat:** When drip "lands" (end of lifetime), spawn a tiny static 4x4 red dot decal that fades over 3 seconds.
- **Visual result:** The stamp perpetually oozes red ink, reinforcing its grotesque personality.

---

## Visual Effects

### Onomatopoeia — "PLAFT!"
- **Trigger:** On slam (Frame 4).
- **Font style:** Massive, chunky, impact-style pixel font. Red (#CC1111) fill with 2px black outline and 1px white inner highlight.
- **Size:** 40x16px text sprite (nearly full weapon frame width).
- **Position:** Appears centered above the slam impact, 12px above ground.
- **Animation:**
  - 0ms: Scale 0.0, alpha 0.0. Invisible.
  - 40ms: Scale 1.5, alpha 1.0. Explosive pop-in overshoot.
  - 120ms: Scale 1.0, alpha 1.0. Settle to final size with slight bounce.
  - 200ms: Scale 1.0, alpha 1.0. Hold for readability.
  - 400ms: Scale 0.8, alpha 0.0. Shrink and fade out.
  - Total: 400ms.
- **Drift:** Moves upward 10px over its lifetime.
- **Rotation:** Slight random tilt (-5 to +5 degrees) on spawn for organic comic feel.
- **Variant:** On critical hit, text changes to "ARQUIVADO!" in dark purple (#4A0080).

### "INDEFERIDO" Ground Stamp Decal
- **Trigger:** On slam (appears at Frame 4, 330ms).
- **Sprite:** `stamp_mark_ground.png` (48x16px).
- **Position:** Centered at impact point, on the ground layer (below characters).
- **Rotation:** Random -5 to +5 degrees (real stamps are never perfectly straight).
- **Animation:**
  - 0ms: Alpha 0.0, scale 1.2. Appears.
  - 60ms: Alpha 0.6, scale 1.0. Pop in, settle. Ink "absorbing" into ground.
  - 3000ms: Alpha 0.6. Holds visible.
  - 5000ms: Alpha 0.0. Fully faded.
  - Total: 5000ms.
- **Stacking:** Multiple stamp marks can overlap, creating a dense collage of denial.

### "INDEFERIDO" Enemy Stamp Mark
- **Trigger:** On enemy hit.
- **Sprite:** `stamp_mark_enemy.png` (32x32px).
- **Position:** Overlaid on stunned enemy sprite, centered.
- **Duration:** Matches stun duration (1500ms) + 300ms fade.
- **Animation:**
  - 0ms: Alpha 0.0, scale 1.3.
  - 80ms: Alpha 0.8, scale 1.0. Stamped on.
  - 1500ms: Alpha 0.8. Holds during stun.
  - 1800ms: Alpha 0.0. Fades as stun wears off.

### Screen Shake — On Slam
- **Trigger:** Frame 4 of swing animation (slam connects with ground).
- **Intensity:** 4px random offset (HEAVY — this is a power weapon).
- **Duration:** 250ms.
- **Pattern:** 5 oscillations, decaying: 4px, 3px, 3px, 2px, 1px, center.
- **Note:** Shake triggers even on miss (hitting ground). The stamp is so heavy it shakes the earth regardless.

### Screen Flash — On Slam
- **Trigger:** Same as screen shake.
- **Color:** Red (#CC1111).
- **Alpha:** 0.2 (noticeable red tint flash).
- **Duration:** 80ms flash, then fade to 0 over next 120ms.
- **Total:** 200ms. The red tint reinforces the ink splatter theme.

### Impact Shockwave Ring
- **Trigger:** On slam, on enemy hit.
- **Visual:** Expanding white circle outline (1px stroke).
- **Animation:**
  - 0ms: Radius 4px, alpha 0.8.
  - 200ms: Radius 32px, alpha 0.0.
- **Visual result:** A satisfying ripple that sells the weight of the impact.

---

## Sound Cue Timing

| Event                | Timing                     | Sound Description                                     |
|----------------------|----------------------------|-------------------------------------------------------|
| Raise stamp          | Frame 1 (0ms)              | Heavy wooden creak + chain rattle (effort sound)      |
| Apex pause           | Frame 2 (100ms)            | Brief silence (tension beat) then quiet whoosh intake  |
| Downswing            | Frame 3 (250ms)            | Fast heavy whoosh descending — deep, weighty           |
| SLAM impact          | Frame 4 (330ms)            | MASSIVE wet thud + rubber slap + ink splash combo      |
| "PLAFT!" pop         | Frame 4 + 40ms (370ms)     | Comic book impact pop, deep bass "thoom"               |
| Ink splatter         | Frame 4 + 60ms (390ms)     | Wet splashing, liquid scatter                          |
| Enemy stun start     | On hit                      | Descending "bwaaaah" comedy horn + cartoon stars sound |
| Stun stars loop      | During stun (1500ms)       | Subtle twinkling chime, looping, getting quieter       |
| Stun end             | 1500ms after hit           | Small "ding!" release sound                            |
| Idle drip            | Each 1200ms in idle        | Quiet "plink" of ink droplet hitting floor             |
| Idle fly buzz        | Continuous in idle         | Very quiet buzzing, panning left-right with fly        |
| Stamp lift (impact)  | Impact frame 3             | Sticky "squelch" peeling sound (wet adhesion release)  |

---

## Damage & Gameplay Timing

| Property                    | Value          |
|-----------------------------|----------------|
| Base damage                 | 35             |
| Stun duration               | 1500ms         |
| Attack wind-up              | 250ms (frames 1-2, vulnerable window) |
| Attack active frame         | Frame 4 only   |
| Attack cooldown             | 800ms after slam completes |
| Total attack cycle          | 1350ms (550ms animation + 800ms cooldown) |
| Area of Effect              | 40x40px rectangle in front of player |
| Knockback                   | 8px push away from impact center |
| Critical hit chance          | 8%            |
| Critical hit multiplier      | 2.5x          |
| Critical hit bonus          | +500ms stun duration |
| Can hit multiple enemies     | Yes (AoE)     |
| Movement during attack       | Locked (550ms) |

---

## Phaser 3 Implementation Notes

```
Animation keys:
- 'carimbo_swing'   -> frames 0-3, variable frame duration via frameRate override:
    Use anims.create with custom frame objects:
    frames: [
      { key: 'carimbo', frame: 0, duration: 100 },
      { key: 'carimbo', frame: 1, duration: 150 },
      { key: 'carimbo', frame: 2, duration: 80 },
      { key: 'carimbo', frame: 3, duration: 220 }
    ]
- 'carimbo_impact'  -> frames 0-2, frameRate: 8, repeat: 0
- 'carimbo_idle'    -> frames 0-1, frameRate: 2, repeat: -1

Screen shake:
- this.cameras.main.shake(250, 0.008)  // 4px at 500px camera width

Screen flash:
- this.cameras.main.flash(200, 204, 17, 17, false, null, null, 0.2)

Ink splatter emitter:
- emitter.explode(12, impactX, impactY)
- emitter.setSpeed({ min: 80, max: 160 })
- emitter.setLifespan(500)
- emitter.setScale({ start: 1.0, end: 0.6 })
- emitter.setAlpha({ start: 1.0, end: 0.3 })

Dust cloud emitter:
- dustEmitter.explode(7, impactX, impactY)
- dustEmitter.setSpeed({ min: 40, max: 80 })
- dustEmitter.setLifespan(350)
- dustEmitter.setScale({ start: 0.5, end: 2.0 })
- dustEmitter.setAlpha({ start: 0.6, end: 0 })

INDEFERIDO decal:
- Use Phaser.GameObjects.Image with setAlpha(0.6)
- Add tween: { alpha: 0, duration: 2000, delay: 3000 }
- Random rotation: Phaser.Math.FloatBetween(-0.087, 0.087) // -5 to +5 degrees in radians

Stun stars:
- Use 3 star sprites in a Phaser.GameObjects.Container
- Container rotates via tween: { angle: 360, duration: 1000, repeat: -1 }
- After stun expires: tween scale to 0 over 200ms, then destroy
```
