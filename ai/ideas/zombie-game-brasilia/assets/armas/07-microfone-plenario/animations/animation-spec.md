# Microfone do Plenario — Animation & Effects Specification

## Weapon Type
**Ranged (Sonic)** — A Congress podium microphone that fires expanding sound wave rings as projectiles. The mic channels audio feedback into a weaponized screech that damages and pushes back enemies. Fast fire rate, moderate damage, unique expanding-ring projectile mechanic. The sound wave rings grow as they travel, covering more area at range but becoming weaker.

---

## Animation Cycles

### 1. Fire Animation
**Trigger:** Player attack input
**Total duration:** 440ms

| Frame        | Duration | Description                                      |
|--------------|----------|--------------------------------------------------|
| `fire_01`    | 80ms     | Charge-up: electricity crackles, wave forming     |
| `fire_02`    | 100ms    | Feedback build: vibration, arcs intensify         |
| `fire_03`    | 120ms    | SCREECH RELEASE: blast fires, ring launches (held longer for impact) |
| `fire_04`    | 140ms    | Post-fire: smoking, recovery, next wave forming   |

- **Playback:** Once per shot. Can queue next shot during Frame 4.
- **Frame rate:** ~9 fps average (variable durations for jerky Andre Guedes feel).
- **Player movement:** Reduced speed (50%) during frames 1-3, full speed at Frame 4. Not fully locked — this is a mobile ranged weapon.
- **Projectile spawn:** Sound wave ring entity spawns at Frame 3 (200ms into animation), at mic head position, traveling in aim direction.
- **Recoil:** Player nudged 2px backward on Frame 3 (sonic kickback).

### 2. Sound Wave Projectile Flight (Looping)
**Trigger:** Projectile spawned from fire animation
**Total duration per loop:** 400ms (loops until hit or max range)

| Frame              | Duration | Description                       |
|--------------------|----------|-----------------------------------|
| `wave_flight_01`   | 100ms    | Tight ring (16px visual)          |
| `wave_flight_02`   | 100ms    | Expanding ring (20px visual)      |
| `wave_flight_03`   | 100ms    | Wide ring (24px visual)           |
| `wave_flight_04`   | 100ms    | Maximum ring (28px visual)        |

- **Playback:** Loops continuously during flight.
- **Scaling behavior:** In addition to the frame animation, the sprite itself scales:
  - At spawn: scale 0.6x (small, concentrated blast).
  - At max range: scale 1.8x (large, wide wave).
  - Linear interpolation over flight distance.
- **This means:** The expanding ring animation AND the scale increase compound, creating a dramatic wave-spreading effect.
- **Flight speed:** 200px/s (moderate — sound waves shouldn't be instant, they should be visible and dodgeable by fast enemies).
- **Max range:** 250px (approximately 7.8 tiles).
- **Hitbox:** Circular, matching the visible ring radius. Grows from 12px to 36px over flight distance.
- **Piercing:** No. Hits first enemy and triggers impact.
- **Multiple projectiles:** Up to 3 on screen simultaneously.

### 3. Impact Animation
**Trigger:** Sound wave hits enemy or reaches max range
**Total duration:** 350ms

| Frame           | Duration | Description                               |
|-----------------|----------|-------------------------------------------|
| `impact_01`     | 80ms     | Ring shatters, flash burst, distortion begins |
| `impact_02`     | 150ms    | Peak chaos: full distortion, "SCREEEECH!" text, lightning (held long for readability) |
| `impact_03`     | 120ms    | Echo fade: sparkles dissolve, text scatters, calm returns |

- **Playback:** Once. Effect plays at the hit position as an overlay.
- **Frame rate:** ~8 fps.
- **At max range (miss):** Same animation plays but with 50% alpha (weaker visual, suggesting the wave dissipated naturally). No "SCREEEECH!" text on miss.

### 4. Idle Glow (Looping)
**Trigger:** Weapon equipped, player not attacking
**Total duration per loop:** 1000ms

| Frame        | Duration | Description                      |
|--------------|----------|----------------------------------|
| `idle_01`    | 500ms    | Hum A: LED bright, arc position 1 |
| `idle_02`    | 500ms    | Hum B: LED dim, arc position 2    |

- **Playback:** Continuous slow loop.
- **Frame rate:** 2 fps (very slow idle hum).
- **Supplemental:** Procedural electricity arc effect (not frame-based) — a small tween-animated arc sprite jumps to random positions on the gooseneck every 300-600ms, lasting 100ms each. Creates a "crackling with energy" ambient effect.

---

## Particle Effects

### Electricity Arcs (During Fire)
- **Emitter:** Attached to mic head position.
- **Active during:** Fire animation frames 1-3 (0-300ms).
- **Spawn rate:** 1 arc every 60ms during charge, 1 every 30ms during screech release.
- **Particle sprites:** `electric_arc_01`, `electric_arc_02` (alternating).
- **Particle behavior:**
  - Position: Random offset 0-8px from mic head center.
  - Rotation: Random 0-360 degrees.
  - Lifetime: 100ms (rapid flash-on/flash-off).
  - Scale: Random 0.5-1.2.
  - Alpha: 0 -> 1.0 -> 0 over 100ms lifetime (flash effect).
- **Visual result:** A crackling corona of electricity around the mic head, intensifying as the screech builds.

### Smoke Wisps (Post-fire)
- **Emitter:** Attached to mic head, active during fire Frame 4.
- **Count:** 2-3 wisps.
- **Particle sprite:** Simple 4x4px gray circles (#808080) with soft edges.
- **Particle behavior:**
  - Velocity: Upward (in isometric Y) 10-20px/s, slight random lateral drift.
  - Lifetime: 400ms.
  - Scale: Start 0.3, end 1.0 (wisps expand as they rise).
  - Alpha: Start 0.5, end 0.0.
  - Rotation: Slow random spin 30-60 deg/s.
- **Visual result:** The mic smokes after firing, like an overheated amplifier.

### Sound Wave Trail Distortion (During Projectile Flight)
- **Emitter:** Trail behind the sound wave projectile.
- **Spawn rate:** 1 every 60ms.
- **Particle sprite:** `static_crackle.png` (TV noise pixels).
- **Particle behavior:**
  - Position: At projectile's current position (left behind as projectile moves).
  - Velocity: 0 (stationary once spawned).
  - Lifetime: 300ms.
  - Scale: Start 1.0, end 0.5.
  - Alpha: Start 0.6, end 0.0.
- **Visual result:** A fading trail of digital static noise left in the sound wave's wake, as if the air itself is distorted.

### Impact Ring Fragments
- **Emitter:** One-shot burst at impact position.
- **Count:** 8-10 arc fragments.
- **Particle sprite:** Small curved blue arc sprites (8x8px, #44BBFF, curved 1px line).
- **Particle behavior:**
  - Radial explosion: velocity 60-120px/s outward.
  - Rotation: Random high-speed spin 180-540 deg/s.
  - Lifetime: 350ms.
  - Scale: Start 1.0, end 0.0.
  - Alpha: Start 1.0, end 0.0.
- **Visual result:** The sound ring visibly breaks apart into curved shards on impact.

### Impact Lightning Bolts
- **Emitter:** One-shot burst at impact, layered over ring fragments.
- **Count:** 4-5 lightning bolts.
- **Particle sprite:** `electric_arc_01.png`.
- **Particle behavior:**
  - Radial directions: evenly spaced around 360 degrees.
  - Velocity: 80-100px/s outward.
  - Lifetime: 200ms.
  - Scale: 1.5 (larger than normal arcs for drama).
  - Alpha: Start 1.0, end 0.0.
  - Rotation: Random.
- **Visual result:** Lightning bolts shoot out from the impact, adding electrical violence to the sonic hit.

---

## Visual Effects

### Onomatopoeia — "SCREEEECH!"
- **Trigger:** On enemy hit (not on miss).
- **Font style:** Jagged, distorted, unstable pixel font. Each letter slightly different size and rotation (as if vibrating apart). Yellow (#FFDD00) fill with blue (#44BBFF) outline (1px). Some letters have visible "glitch" artifacts (1px offset or color shift).
- **Size:** 48x14px text sprite (wide, as a screech should be).
- **Position:** Appears 10px above impact point.
- **Animation:**
  - 0ms: Scale 0.5, alpha 0.3. Forming, jittery.
  - 60ms: Scale 1.3, alpha 1.0. Pop-in with overshoot. Text vibrates (random 1px offset each frame).
  - 150ms: Scale 1.0, alpha 1.0. Settle, but still vibrating.
  - 250ms: Scale 1.0, alpha 1.0. Letters begin separating — each letter drifts 1-2px in random direction.
  - 350ms: Scale 0.8, alpha 0.0. Letters fully scattered and faded. Text disintegrates.
  - Total: 350ms.
- **Vibration:** Throughout its lifetime, the text has a constant 1px random position jitter applied every 50ms. This is unique to this weapon's text — other weapons' onomatopoeias are stable.
- **Sound sync:** The "SCREEEECH!" visual appears at the same moment the impact sound plays.

### Feedback Screech Cone (During Fire Frame 3)
- **Trigger:** Fire animation Frame 3.
- **Visual:** A conical burst of yellow-white energy from the mic head in the attack direction. Shaped like a 45-degree cone, 16px long.
- **Animation:**
  - 0ms: Cone appears, full brightness (#FFFFFF center, #FFDD00 edges).
  - 60ms: Cone at full size, brightness pulsing.
  - 120ms: Cone fading, shrinking.
  - 180ms: Gone.
- **Note:** This is a visual effect only, not a hitbox. The hitbox is on the ring projectile.

### Screen Shake — On Impact
- **Trigger:** Sound wave hits enemy.
- **Intensity:** 3px random offset (moderate — less than the stamp, more than the badge).
- **Duration:** 180ms.
- **Pattern:** 4 oscillations, rapid: alternating X and Y offsets (simulating vibration rather than a single-direction shake, fitting the sonic theme).
- **Frequency:** High — the shake should feel like a vibration, not a thud.

### Screen Flash — On Fire
- **Trigger:** Fire animation Frame 3 (screech release).
- **Color:** White (#FFFFFF).
- **Alpha:** 0.12 (very subtle — just enough to feel the sonic blast).
- **Duration:** 40ms instant flash, then 40ms fade. Total 80ms.

### Air Distortion / Heat Shimmer (On Impact)
- **Trigger:** Impact frames 1-2.
- **Visual:** Wavy displacement effect in a 32px radius around impact. Pixels in the affected area appear to ripple/undulate.
- **Implementation:** In Phaser, apply a small sine-wave displacement shader to the area, or simulate with overlapping semi-transparent wavy line sprites.
- **Duration:** 300ms, matching impact animation.
- **Intensity:** Start strong (2px displacement), fade to 0.
- **Visual result:** The air visibly warps around the sonic impact, selling the "weaponized sound" concept.

### "ON AIR" LED Pulse (Persistent)
- **Always active** when weapon is equipped.
- **Visual:** The red LED on the mic base gently pulses.
- **Animation:** Alpha oscillates between 0.5 and 1.0, period 800ms, sinusoidal.
- **The glow halo:** Radius oscillates between 3px and 5px, synced with alpha.
- **Meaning:** The mic is always "broadcasting." Always on. Always dangerous.

---

## Sound Cue Timing

| Event                  | Timing                       | Sound Description                                        |
|------------------------|------------------------------|----------------------------------------------------------|
| Charge-up start        | Frame 1 (0ms)                | Rising electronic hum + static crackle building          |
| Feedback build         | Frame 2 (80ms)               | Higher pitch ascending whine + electrical buzzing         |
| SCREECH release        | Frame 3 (180ms)              | LOUD harsh feedback screech — the weapon's signature sound. Distorted, ear-piercing, like a PA system gone wrong. 300ms duration. |
| Post-fire smoke        | Frame 4 (300ms)              | Quiet sizzle/hiss (hot electronics cooling)               |
| Projectile flight      | During flight (looping)      | Low continuous hum that Doppler-shifts (pitch drops as wave expands). Subtle, background. |
| Impact hit             | Impact frame 1 (0ms)         | Sharp "CRACK" of sonic boom + glass-shatter sound         |
| "SCREEEECH!" text pop  | Impact frame 1 + 30ms        | Secondary feedback squeal (shorter, higher pitch)         |
| Impact distortion      | Impact frames 1-2            | Deep bass rumble / sub-bass vibration (felt more than heard) |
| Impact echo fade       | Impact frame 3               | Reverberating echo decay, descending pitch                |
| Idle hum               | Continuous when equipped      | Very low 60Hz electrical hum. Constant, almost subliminal. Volume 10%. |
| Idle arc pop           | Each random arc (300-600ms)  | Tiny electrical "zzt" pop. Random pitch variation.         |
| LED pulse              | Continuous                   | No sound (visual only).                                    |

---

## Damage & Gameplay Timing

| Property                      | Value          |
|-------------------------------|----------------|
| Base damage (close range)     | 20             |
| Base damage (max range)       | 10             |
| Damage falloff                | Linear, 20 -> 10 over 250px range |
| Fire rate                     | 1 shot per 500ms (440ms animation + 60ms buffer) |
| Projectile speed              | 200px/s        |
| Projectile max range          | 250px          |
| Projectile max lifetime       | 1250ms         |
| Knockback (close)             | 12px push away  |
| Knockback (far)               | 4px push away   |
| Player recoil on fire         | 2px backward    |
| Simultaneous projectiles max  | 3               |
| Piercing                      | No              |
| Critical hit chance           | 12%             |
| Critical hit multiplier       | 1.8x            |
| Critical hit bonus            | Ring does NOT expire on hit — pierces through and continues |
| Stun                          | None (knockback is the crowd control) |
| Movement during fire          | 50% speed (frames 1-3), 100% (frame 4) |

---

## Phaser 3 Implementation Notes

```
Animation keys:
- 'mic_fire'         -> frames 0-3, variable frame duration:
    frames: [
      { key: 'mic', frame: 0, duration: 80 },
      { key: 'mic', frame: 1, duration: 100 },
      { key: 'mic', frame: 2, duration: 120 },
      { key: 'mic', frame: 3, duration: 140 }
    ]
- 'wave_projectile'  -> frames 0-3, frameRate: 10, repeat: -1
- 'mic_impact'       -> frames 0-2, variable:
    frames: [
      { key: 'mic_impact', frame: 0, duration: 80 },
      { key: 'mic_impact', frame: 1, duration: 150 },
      { key: 'mic_impact', frame: 2, duration: 120 }
    ]
- 'mic_idle'         -> frames 0-1, frameRate: 2, repeat: -1

Projectile scaling (sound wave expansion):
- On projectile update:
    const progress = distanceTraveled / maxRange; // 0 to 1
    projectile.setScale(0.6 + progress * 1.2);   // 0.6x to 1.8x
    projectile.hitboxRadius = 12 + progress * 24; // 12px to 36px

Damage falloff:
- On hit:
    const progress = distanceTraveled / maxRange;
    const damage = 20 - (progress * 10); // 20 at point-blank, 10 at max range

Knockback falloff:
- const knockback = 12 - (progress * 8); // 12px close, 4px far

Electricity arc procedural effect (idle/fire):
- Create a pool of 3-4 arc sprites
- Timer event every Phaser.Math.Between(300, 600) ms:
    arcSprite.setPosition(
      micHead.x + Phaser.Math.Between(-8, 8),
      micHead.y + Phaser.Math.Between(-8, 8)
    );
    arcSprite.setRotation(Phaser.Math.FloatBetween(0, Math.PI * 2));
    arcSprite.setAlpha(1);
    tweens.add({ targets: arcSprite, alpha: 0, duration: 100 });

Air distortion (shader-free approach):
- Create 3-4 semi-transparent wavy line sprites in a container
- Tween their y positions with sine wave offset:
    tweens.add({
      targets: wavyLine,
      y: originalY + 2 * Math.sin(time * 0.01),
      alpha: { from: 0.4, to: 0 },
      duration: 300
    });

Screen shake (vibration style):
- Custom shake using a rapid-fire tween:
    cameras.main.shake(180, new Phaser.Math.Vector2(0.006, 0.006));
    // Or manual: alternate X/Y offsets every 45ms for 4 cycles

ON AIR LED pulse:
- tweens.add({
    targets: ledSprite,
    alpha: { from: 0.5, to: 1.0 },
    duration: 400,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
  });

SCREEEECH text vibration:
- On each frame callback while text is alive:
    screeechText.x = baseX + Phaser.Math.Between(-1, 1);
    screeechText.y = baseY + Phaser.Math.Between(-1, 1);
```
