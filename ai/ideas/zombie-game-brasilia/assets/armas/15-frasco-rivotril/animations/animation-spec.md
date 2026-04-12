# Frasco de Rivotril Turbo - Animation Specification

## Animation Sets

### 1. SWING (Melee Club Attack)
**Phaser Animation Key:** `rivotril_swing`
**Frames:** 0, 1, 2, 3, 4
**Total Duration:** 480ms
**Loop:** false
**Y-Sort Priority:** weapon layer (above character)

| Frame | Name              | Duration (ms) | Notes                                    |
|-------|-------------------|---------------|------------------------------------------|
| 0     | static            | 60            | Brief hold                               |
| 1     | swing_windup      | 110           | Desperate grab, liquid sloshes up        |
| 2     | swing_mid         | 80            | FAST -- peak velocity, pills scatter     |
| 3     | swing_contact     | 110           | Impact, pill explosion, sedation cloud   |
| 4     | swing_followthrough| 120           | Pills tumbling, cloud lingers            |

**On Frame 1 (wind-up):**
- Sound cue: `sfx_bottle_rattle` -- pills rattling inside plastic bottle (200ms)
- Sound cue: `sfx_liquid_slosh` -- liquid sloshing sound (150ms)
- Particle: 1 blue pill (1x1px) flies upward from cap (speed 60px/s, lifetime 300ms, gravity 40px/s2)
- Particle: 2 sweat drops (2x3px, light blue) spawn near grip (static, lifetime matches frame duration)

**On Frame 2 (mid-swing):**
- Sound cue: `sfx_bottle_whoosh` -- heavy plastic whoosh (120ms)
- Particle: 3-4 blue pills escape cap, trail behind swing arc (1x1px blue, speed 80px/s tangential, lifetime 400ms, gravity 30px/s2)
- Particle: Purple sedation wisp -- 2 purple 1px particles trail from pills (lifetime 250ms, fade out)
- Particle: Orange motion lines -- 2 lines along swing arc (1px, orange, 150ms)

**On Frame 3 (contact):**
- Sound cue: `sfx_bottle_smash` -- heavy plastic-on-flesh impact with pill rattle burst (400ms)
- Sound cue: `sfx_sedation_hiss` -- chemical gas release hiss (300ms, starts 50ms after impact)
- Screen shake: 5px amplitude, 250ms, exponential decay
- Screen flash: Purple tint, 60ms, 25% opacity
- Particle: Pill explosion -- 10 blue pills burst radially (1-2px each, speed 140px/s, lifetime 500ms, gravity 50px/s2)
- Particle: Sedation cloud spawn -- purple gas (15px diameter, sedation purple, 50% opacity, expands to 25px over 500ms, persists 3000ms then fades 500ms)
- Particle: Amber liquid splash -- 5 amber droplets (1x1px, speed 100px/s, lifetime 300ms, gravity 80px/s2)
- Particle: Stars -- 3 yellow 3x3px cartoon stars orbit impact point (orbit radius 12px, speed 360deg/s, lifetime 600ms, fade out)
- Particle: White starburst -- 8x8px at contact center (100ms, fade out)
- Damage applied
- Sedation debuff applied: target speed -50% for 3 seconds
- Reset Ciro's panic timer to 0

**On Frame 4 (follow-through):**
- Particle: 3 blue pills tumble from open bottle mouth (speed 40px/s downward, lifetime 400ms, gravity 60px/s2)
- Particle: 2 amber drops drip from opening (speed 20px/s downward, lifetime 300ms)
- Particle: Sedation cloud continues expanding at hit point
- Sound cue: `sfx_pill_scatter` -- tiny pills hitting ground sound (200ms)

---

### 2. SEDATION CLOUD PROJECTILE (Area Denial)
**Phaser Animation Key:** `rivotril_sedate_cloud`
**Frames:** 5, 6, 7, 6 (loop with pulse)
**Total Duration:** 480ms per cycle
**Loop:** true (while cloud active, 3 second lifetime)
**Speed:** 60px/s (slow, drifting)

| Frame | Name           | Duration (ms) | Notes                              |
|-------|----------------|---------------|------------------------------------|
| 5     | cloud_launch   | 120           | Initial puff                       |
| 6     | cloud_expand   | 120           | Growing                            |
| 7     | cloud_pulse    | 120           | Jerky contraction                  |
| 6     | cloud_expand   | 120           | Return to growing                  |

**Continuous particles (while cloud active):**
- "Z" symbols: Yellow "z" (2-4px) spawns every 400ms from cloud surface, drifts upward (speed 20px/s, lifetime 600ms, fade out)
- Purple wisps: Sedation purple particles (1x1px) shed from cloud edges every 200ms (lifetime 300ms, random drift)
- Sound: `sfx_sedation_ambient` -- low chemical hissing drone, looping (volume 15%, 3D positioned)

**On contact with enemy:**
- Enemy receives sedation debuff: speed -50% for 3 seconds
- Particle: "Zzz" burst (3 yellow Z symbols, various sizes, burst from enemy position)
- Sound cue: `sfx_sedated` -- heavy drowsy sound effect (300ms)
- Enemy sprite tint: Purple overlay 20%, fades over 3 seconds

**Sedation debuff visual on enemy (3 second duration):**
- "Z" symbols float above enemy head (1 spawns every 600ms, yellow, 2px, drift upward, lifetime 500ms)
- Enemy sprite wobble: gentle sine wave horizontal oscillation (amplitude 1px, period 400ms)
- Purple tint on enemy sprite: starts 20%, fades to 0% over 3 seconds

---

### 3. IMPACT (On Hit)
**Phaser Animation Key:** `rivotril_impact`
**Frames:** 9, 10, 11
**Total Duration:** 480ms
**Loop:** false

| Frame | Name             | Duration (ms) | Notes                          |
|-------|------------------|---------------|--------------------------------|
| 9     | nocaute_appear   | 130           | Text + cloud detonation        |
| 10    | nocaute_peak     | 200           | Maximum sedation, text droops  |
| 11    | nocaute_fade     | 150           | Dissipation                    |

**On Frame 9:**
- Sound cue: `sfx_nocaute` -- heavy knockout sound with chemical whoosh (500ms)
- Screen shake: 4px amplitude, 200ms
- Particle: Purple gas explosion -- expanding circle (10px to 40px diameter, 300ms, sedation purple, fade from 60% to 20%)
- Particle: "Z" symbols -- 5 yellow Z's of various sizes burst from center (speed 60px/s radial, lifetime 500ms)
- Particle: Stars orbit -- 4 yellow stars at impact (orbit radius 16px, speed 270deg/s)
- Particle: Blue pill rain -- 5 blue 1px pills fall downward (speed 40px/s, gravity 30px/s2, lifetime 400ms)

**On Frame 10:**
- Screen tint: Purple overlay, 15% opacity, 200ms
- Particle: Additional "Z" symbols spawn (3 more, larger, 6-8px)
- Particle: Hypnotic swirl -- concentric purple circles pulse at center (2 rings, 10px and 20px diameter, 20% opacity, 200ms)
- Particle: Clock spawns (4x4px, static, at edge of effect, persists 400ms)
- Slowdown: Game speed 0.85x for 200ms (drowsy slow-motion)
- Stars slow to 180deg/s (getting sedated themselves)

**On Frame 11:**
- Particle: Purple residue circle at impact (18px diameter, 20% opacity, persists 2000ms then fades 500ms) -- sedation zone marker
- All "Z" symbols float upward and fade
- Stars dissipate
- Purple gas retracts toward center
- Sound: Chemical hiss fades out (300ms)

---

### 4. IDLE (Resting)
**Phaser Animation Key:** `rivotril_idle`
**Frames:** 12, 13
**Total Duration:** 1400ms
**Loop:** true (continuous while weapon equipped)

| Frame | Name          | Duration (ms) | Notes                        |
|-------|---------------|---------------|------------------------------|
| 12    | slosh_left    | 700           | Liquid shifts left           |
| 13    | slosh_right   | 700           | Liquid shifts right          |

**Continuous particles (idle):**
- Sleepy "z": Single yellow "z" (2px) spawns every 2000ms from cap area, drifts upward (speed 10px/s, lifetime 800ms, fade out)
- Sound: `sfx_pill_rattle_quiet` -- very faint pill rattle, looping (volume 5%)

**Panic timer tracking:**
- A hidden timer starts counting from last attack
- At 7 seconds: Bottle sprite begins subtle vibration (1px horizontal oscillation, 100ms period) -- FORESHADOWING
- At 10 seconds: Triggers PANIC animation

---

### 5. PANIC (Self-Damage Mechanic)
**Phaser Animation Key:** `rivotril_panic`
**Frames:** 14, 15, 14, 15, 16
**Total Duration:** 1200ms
**Loop:** false
**Trigger:** 10 seconds without attacking

| Frame | Name          | Duration (ms) | Notes                              |
|-------|---------------|---------------|------------------------------------|
| 14    | panic_1       | 200           | Shaking begins, stress lines       |
| 15    | panic_2       | 200           | Cap pops, gas leaks                |
| 14    | panic_1       | 200           | Return to shaking (ping-pong)      |
| 15    | panic_2       | 200           | Peak panic                         |
| 16    | panic_selfdose| 400           | Ciro chugs from weapon, self-damage|

**On Frame 14 (first play):**
- Sound cue: `sfx_panic_heartbeat` -- fast anxious heartbeat (loops for full panic duration, 1200ms)
- Sound cue: `sfx_bottle_rattle_hard` -- aggressive pill rattling (200ms)
- Particle: Red stress lines -- 3 lines radiate from bottle (1px, panic red, 8px long, 200ms)
- Particle: Sweat drops -- 3 light blue drops spawn around bottle (2x3px, static for frame duration)
- Screen effect: Subtle screen vibration (1px, 100ms period) -- the player feels the anxiety
- UI: Exclamation "!" appears over Ciro's head (red, 4x6px)

**On Frame 15 (first play):**
- Sound cue: `sfx_cap_pop` -- plastic cap popping off (100ms)
- Particle: Cap flies upward (white cap sprite, 3x3px, speed 80px/s upward, lifetime 400ms, gravity 60px/s2)
- Particle: Purple gas leaks -- 3 purple wisps rise from open bottle (speed 30px/s, lifetime 500ms, fade)
- Particle: Sweat drops multiply -- 5 total, larger (4x5px)
- Particle: Orange plastic chips -- 2 fragments break from bottle (1x1px, speed 40px/s, lifetime 300ms)
- Screen effect: Screen vibration increases (2px, 80ms period)

**On Frame 14 (second play):**
- Sound: Heartbeat continues (faster tempo)
- Stress lines double (6 lines)
- Screen vibration maintains

**On Frame 15 (second play):**
- Peak panic -- all particles at maximum intensity
- Sound cue: `sfx_panic_scream` -- Ciro's panicked yelp (200ms)
- UI: "!!" double exclamation, flashing

**On Frame 16 (self-dose):**
- Sound cue: `sfx_gulp_gulp` -- desperate gulping/drinking sounds (400ms)
- Sound cue: `sfx_self_damage` -- painful "oof" with pill crunch (200ms, at 200ms offset)
- Screen flash: Red, 40ms, 20% opacity (damage flash)
- Particle: Blue pill stream -- 6 pills pour from bottle toward Ciro (arc trajectory, speed 60px/s, lifetime 300ms)
- Particle: Purple gas billows in pour direction (3 wisps, speed 40px/s, 400ms)
- Particle: Stars above Ciro -- 4 yellow stars orbit his head (orbit radius 10px, speed 270deg/s, lifetime 800ms)
- Damage: Ciro takes self-damage (configurable, suggest 5% max HP)
- Effect: Ciro becomes briefly invulnerable for 1 second (the medication "helps" momentarily)
- Effect: Panic timer resets
- Particle: "-HP" text floats above Ciro (red, drift upward, speed 30px/s, lifetime 600ms, fade)
- Screen: Brief purple tint 10% (Ciro is now slightly sedated)
- After self-dose: Return to idle animation with 2-second immunity from panic retrigger

---

## Onomatopoeia Rendering

| Text         | Font Style             | Color      | Shadow     | Size   | Trigger            |
|--------------|------------------------|------------|------------|--------|--------------------|
| "NOCAUTE!"   | Droopy wobbly letters  | #8844AA    | #FFE040    | 22px   | On hit             |
| "Zzzzz"      | Various sizes, floating| #FFE040    | none       | 2-8px  | Ongoing sedation   |
| "-HP"        | Sharp angular          | #FF2020    | #CC0000    | 14px   | On self-damage     |
| "!!" / "!"   | Bold exclamation       | #FF2020    | #CC0000    | 4-6px  | Panic warning      |
| "DOSE!"      | Shaky desperate        | #CC2020    | #FFE040    | 16px   | Self-dose (optional)|

## Screen Shake Table

| Event              | Amplitude | Duration | Direction  | Easing              |
|--------------------|-----------|----------|------------|---------------------|
| Melee contact      | 5px       | 250ms    | Random     | Exponential decay   |
| Sedation impact    | 4px       | 200ms    | Random     | Linear decay        |
| Panic state        | 1-2px     | continuous| Horizontal | Sine oscillation    |
| Self-damage        | 3px       | 150ms    | Down       | Exponential decay   |

## Particle System Summary

| Particle          | Sprite     | Count  | Lifetime | Speed     | Gravity  | Alpha     |
|-------------------|------------|--------|----------|-----------|----------|-----------|
| Blue pills burst  | 1-2px blue | 10     | 500ms    | 140px/s   | 50px/s2  | 1.0 > 0  |
| Amber splash      | 1x1 amber  | 5      | 300ms    | 100px/s   | 80px/s2  | 0.8 > 0  |
| Sedation cloud    | circle purp| 1      | 3000ms   | expand    | 0        | 0.5 > 0.1|
| Z sleep symbols   | 2-8px yel  | stream | 500-600ms| 20-60px/s | 0        | 1.0 > 0  |
| Stars (cartoon)   | 3x3 yellow | 3-4    | 600ms    | orbit     | 0        | 1.0 > 0  |
| Purple wisps      | 1x1 purp   | stream | 300ms    | 30px/s    | 0        | 0.4 > 0  |
| Sweat drops       | 2-5px blue | 3-5    | static   | 0         | 0        | 0.8      |
| Stress lines      | 1px red    | 3-6    | 200ms    | 0         | 0        | 0.7      |
| Orange chips      | 1x1 orange | 2      | 300ms    | 40px/s    | 0        | 0.6 > 0  |
| Self-dose pills   | 1px blue   | 6      | 300ms    | 60px/s    | 0        | 1.0 > 0  |
| Purple residue    | circle purp| 1      | 2500ms   | 0         | 0        | 0.2 > 0  |

## Special Behavior Notes

### Panic Timer System
1. Timer starts at 0 when weapon is equipped or after any attack/self-dose
2. At 7 seconds: visual foreshadowing begins (bottle vibration)
3. At 10 seconds: PANIC animation plays automatically (cannot be cancelled)
4. Self-dose at end of PANIC: deals self-damage, resets timer
5. 2-second grace period after self-dose before timer restarts
6. If Ciro attacks before 10 seconds: timer resets silently
7. The DESPERATION of the mechanic is the point -- Ciro must keep fighting or suffer

### Sedation Debuff Stack
- Sedation does NOT stack -- refreshes duration instead
- Visual: purple tint + Z symbols persist while debuffed
- Speed reduction: 50% movement speed
- Does not affect attack speed (enemies can still fight, just slowly)
