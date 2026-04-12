# Biblia Sagrada Blindada - Animation Specification

## Animation Sets

### 1. SWING (Melee Attack)
**Phaser Animation Key:** `biblia_swing`
**Frames:** 0, 1, 2, 3, 4
**Total Duration:** 500ms
**Loop:** false
**Y-Sort Priority:** weapon layer (above character)

| Frame | Name              | Duration (ms) | Notes                                    |
|-------|-------------------|---------------|------------------------------------------|
| 0     | static            | 80            | Brief hold before swing starts           |
| 1     | swing_windup      | 120           | Slow wind-up, building divine tension    |
| 2     | swing_mid         | 80            | FAST -- peak velocity, shortest frame    |
| 3     | swing_contact     | 100           | Impact frame, trigger effects here       |
| 4     | swing_followthrough| 120           | Deceleration, return to rest             |

**On Frame 1 (wind-up):**
- Sound cue: `sfx_bible_raise` -- deep choir "aaah" ascending note (200ms)
- Particle: 2 small white sparkles rise from book position (lifetime 300ms)

**On Frame 2 (mid-swing):**
- Sound cue: `sfx_bible_whoosh` -- heavy whoosh with harmonic overtone (150ms)
- Particle: Holy ray trail -- 3 golden light particles spawn behind weapon path (lifetime 200ms, fade out)
- Camera: Subtle pre-shake (1px, 50ms) to telegraph impact

**On Frame 3 (contact):**
- Sound cue: `sfx_bible_slam` -- MASSIVE impact sound, metal on flesh with church bell resonance (400ms)
- Screen shake: HEAVY -- 6px amplitude, 300ms duration, decreasing
- Screen flash: White flash, 80ms, 40% opacity
- Particle: Page explosion -- 8 cream-colored rectangles (2x3px) burst radially (speed 120px/s, lifetime 500ms, gravity 40px/s2, fade out)
- Particle: Holy sparks -- 6 golden 1x1px particles burst radially (speed 200px/s, lifetime 300ms)
- Particle: Shockwave ring -- expanding gold circle (start 8px, end 48px diameter, 300ms, fade from 60% to 0% opacity)
- Damage applied this frame
- Conversion roll check triggered this frame

**On Frame 4 (follow-through):**
- Particle: 3 golden ember particles drift upward (speed 30px/s, lifetime 400ms, fade out)
- Sound cue: `sfx_bible_echo` -- reverberating church echo (600ms, volume 40%)

---

### 2. HOLY RAY PROJECTILE (Ranged Component)
**Phaser Animation Key:** `biblia_holy_ray`
**Frames:** 5, 6, 7, 6 (ping-pong flicker)
**Total Duration:** 400ms (loops while in flight)
**Loop:** true
**Speed:** 180px/s

| Frame | Name           | Duration (ms) | Notes                              |
|-------|----------------|---------------|------------------------------------|
| 5     | ray_launch     | 100           | Initial beam form                  |
| 6     | ray_midflight  | 100           | Maximum intensity                  |
| 7     | ray_flicker    | 100           | Jerky flicker (Andre Guedes style) |
| 6     | ray_midflight  | 100           | Return to intensity before loop    |

**Continuous particles (while in flight):**
- Trail: Golden sparkle particles, spawn every 60ms at beam tail, 1x1px, lifetime 200ms, fade out
- Scripture: Tiny dark gold pixel clusters spawn every 150ms, orbit beam at 2px radius, lifetime 300ms
- Sound: `sfx_holy_hum` -- continuous angelic hum, looping, volume increases as beam approaches target

**On spawn:**
- Sound cue: `sfx_holy_launch` -- sharp ascending chime (200ms)
- Camera: 1px nudge in firing direction (50ms)

**Pre-impact (Frame 8):**
- Played once when projectile is within 16px of target
- Duration: 100ms
- Particle: Gold ring appears around beam tip (12px diameter, 100ms)

---

### 3. IMPACT (On Hit)
**Phaser Animation Key:** `biblia_impact`
**Frames:** 9, 10, 11
**Total Duration:** 450ms
**Loop:** false
**Play condition:** Triggers at hit location

| Frame | Name             | Duration (ms) | Notes                          |
|-------|------------------|---------------|--------------------------------|
| 9     | gloria_appear    | 120           | Text materializes              |
| 10    | gloria_peak      | 180           | Maximum intensity, hold longer |
| 11    | gloria_fade      | 150           | Dissipation                    |

**On Frame 9:**
- Sound cue: `sfx_gloria_shout` -- Daciolo's voice screaming "GLORIA!" (500ms, distorted, reverb heavy)
- Particle: 8 radial light rays from center (gold, 1px wide, extend from 4px to 32px, 300ms)
- Particle: 4 page fragments burst outward (2x3px, cream, speed 80px/s, lifetime 400ms)
- Screen flash: Gold tint, 60ms, 20% opacity

**On Frame 10:**
- Screen shake: 4px amplitude, 200ms
- Sound cue: `sfx_choir_blast` -- short choir stab (300ms)
- Particle: Additional exclamation marks ("!!") spawn orbiting main text (3 instances, orbit radius 16px, speed 360deg/s)
- Screen flash: White, 40ms, 30% opacity (secondary flash)
- Slowdown: Game speed 0.8x for 180ms (hit impact feel)

**On Frame 11:**
- Particle: Golden residue circle at impact point (20px diameter, 20% opacity, persists 2000ms then fades over 500ms) -- "blessing mark"
- All previous particles begin fade-out
- Sound: `sfx_gloria_shout` reverb tail continues

---

### 4. IDLE (Resting)
**Phaser Animation Key:** `biblia_idle`
**Frames:** 12, 13
**Total Duration:** 1600ms
**Loop:** true (continuous while weapon equipped)

| Frame | Name          | Duration (ms) | Notes                        |
|-------|---------------|---------------|------------------------------|
| 12    | holy_pulse_1  | 800           | Cross brightens, halo appears|
| 13    | holy_pulse_2  | 800           | Cross dims, halo fades       |

**Continuous particles (idle):**
- Sparkle: Single white 1x1px sparkle spawns every 1200ms at random position on book surface, lifetime 400ms, fade in then out
- Sound: `sfx_bible_ambient` -- very quiet, low angelic drone (looping, volume 10%)

---

### 5. CONVERSION SPECIAL (Zombie Ally Creation)
**Phaser Animation Key:** `biblia_convert`
**Frames:** 14, 15, 16
**Total Duration:** 800ms
**Loop:** false
**Trigger:** When swing attack critically hits AND conversion roll succeeds

| Frame | Name              | Duration (ms) | Notes                           |
|-------|-------------------|---------------|---------------------------------|
| 14    | convert_blast     | 250           | Bible opens, cross beam erupts  |
| 15    | convert_halo_form | 300           | Halo materializes over target   |
| 16    | convert_hallelujah| 250           | Halo locks, conversion complete |

**On Frame 14:**
- Sound cue: `sfx_bible_open` -- dramatic book opening with blinding light sound (300ms)
- Screen flash: WHITE, 100ms, 60% opacity -- BLINDING
- Screen shake: 8px amplitude, 200ms (Bible OPENING is violent)
- Particle: Cross beam -- 4 directional light bars (up/down/left/right) expand from center (start 4px, end 32px, 250ms)
- Particle: Scripture fragments -- 6 dark gold 1px marks spiral outward (orbit radius expanding 4px to 20px, 500ms lifetime)

**On Frame 15:**
- Sound cue: `sfx_halo_form` -- crystalline chime descending, like glass forming (400ms)
- Particle: Halo ring materializes over target -- gold circle (30px diameter) with red crack lines, assembles from 4 arc segments that rotate into position
- Particle: White sparkles (5 instances) orbit the forming halo (orbit radius 18px, speed 270deg/s, lifetime matches frame duration)
- Camera: Slow zoom to 1.05x centered on target (300ms, ease out)

**On Frame 16:**
- Sound cue: `sfx_hallelujah` -- distorted "HALLELUJAH!" voice clip (600ms)
- Sound cue: `sfx_music_notes` -- quick musical notes ascending (400ms)
- Particle: Musical notes (3 instances, gold, 2x3px) float upward from halo (speed 40px/s, lifetime 800ms, gentle sine wave horizontal motion amplitude 4px)
- Particle: "GLORIA!" text pops above halo (gold, small, 300ms then fade)
- Camera: Zoom returns to 1.0x (200ms, ease in)
- Game effect: Target zombie receives `converted` status (5 second duration)
- Spawn: Crooked halo sprite attached above converted zombie's head (persists for 5s, uses Frame 16 sprite as status indicator, gentle bob animation 2px up/down over 800ms loop)

---

### 6. CONVERTED ZOMBIE STATUS (Ally Marker)
**Phaser Animation Key:** `converted_zombie_halo`
**Frames:** 16 (single frame, external animation via tween)
**Total Duration:** 5000ms (conversion duration)
**Loop:** true (while status active)

**Tween behavior:**
- Y position: bob up/down 2px, duration 800ms, ease sine, yoyo true
- Alpha: pulse between 0.7 and 1.0, duration 1200ms, ease sine, yoyo true
- Rotation: gentle wobble +/- 5deg, duration 1000ms, ease sine, yoyo true

**At 4000ms (1 second warning before expiration):**
- Halo alpha pulses faster (flash between 0.3 and 1.0, 200ms cycle)
- Sound: `sfx_halo_crack` -- cracking sound (300ms)
- Particle: Red crack particles fall from halo (2-3 instances, 1x1px red, speed 60px/s downward, lifetime 400ms)

**At 5000ms (expiration):**
- Sound: `sfx_halo_shatter` -- glass breaking sound (200ms)
- Particle: Halo shatters into 6 gold arc fragments that fly outward (speed 100px/s, lifetime 300ms, fade out, slight gravity 20px/s2)
- Zombie reverts to enemy state immediately
- Small puff of golden dust at halo position (8 particles, 1x1px, radial burst, lifetime 200ms)

---

## Onomatopoeia Rendering

| Text       | Font Style           | Color      | Shadow     | Size    | Trigger            |
|------------|----------------------|------------|------------|---------|--------------------|
| "GLORIA!"  | Chunky hand-lettered | #FFD700    | #3B2410    | 24px    | On melee hit       |
| "GLORIA!!!"| Same, with extras    | #FFFEF0    | #3B2410    | 28px    | On crit/peak       |
| "ALELUIA!" | Wobbly serif         | #FFE066    | #5B3A1A    | 16px    | On conversion      |

## Screen Shake Table

| Event              | Amplitude | Duration | Direction  | Easing      |
|--------------------|-----------|----------|------------|-------------|
| Melee contact      | 6px       | 300ms    | Random     | Exponential decay |
| Projectile impact  | 4px       | 200ms    | Away from source | Linear decay |
| Conversion blast   | 8px       | 200ms    | Random     | Exponential decay |
| Bible open         | 8px       | 200ms    | Radial     | Exponential decay |

## Particle System Summary

| Particle          | Sprite     | Count | Lifetime | Speed    | Gravity  | Alpha     |
|-------------------|------------|-------|----------|----------|----------|-----------|
| Holy sparks       | 1x1 gold   | 6     | 300ms    | 200px/s  | 0        | 1.0 > 0  |
| Page fragments    | 2x3 cream  | 8     | 500ms    | 120px/s  | 40px/s2  | 1.0 > 0  |
| Shockwave ring    | circle gold| 1     | 300ms    | expand   | 0        | 0.6 > 0  |
| Golden embers     | 1x1 gold   | 3     | 400ms    | 30px/s up| 0        | 0.8 > 0  |
| Sparkle trail     | 1x1 white  | stream| 200ms    | 0        | 0        | 0 > 1 > 0|
| Scripture spiral  | 1px dkgold | 6     | 500ms    | orbit    | 0        | 0.7 > 0  |
| Musical notes     | 2x3 gold   | 3     | 800ms    | 40px/s up| 0        | 1.0 > 0  |
| Halo shatter      | arc gold   | 6     | 300ms    | 100px/s  | 20px/s2  | 1.0 > 0  |
| Blessing mark     | circle gold| 1     | 2500ms   | 0        | 0        | 0.2 > 0  |
