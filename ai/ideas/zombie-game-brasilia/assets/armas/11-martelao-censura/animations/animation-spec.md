# Martelao da Censura -- Animation Specification

**Weapon ID:** 11
**Boss:** Xandao (Alexandre de Moraes)
**Target FPS:** 10 fps (100ms base frame duration)
**Style:** Twitchy, jerky Andre Guedes animation

---

## 1. Idle Animation (Held Weapon)

**Sprite sheet:** `martelao-idle.png`
**Frames:** 3 (static + 2 glow variants)
**Loop:** Yes, continuous
**Total cycle:** 500ms

| Frame | Duration | Description                               |
|-------|----------|-------------------------------------------|
| 1     | 200ms    | Static pose, faint blue aura              |
| 2     | 150ms    | Blue pulse left, CENSURADO glow brighter  |
| 3     | 150ms    | Blue pulse right, handle shimmer          |

### Particle Effects (Idle)
- **Blue judicial motes:** 1 particle per 400ms
  - Color: `#3366CC` to `#6699FF`
  - Size: 1-2px
  - Position: random around gavel head
  - Velocity: slow drift upward 5-8 px/s, slight circular motion
  - Lifespan: 500ms
  - Alpha: 0.6 to 0.0

- **Iron band crackle:** 1 spark per 600ms (alternating bands)
  - Color: `#CCDDFF` (white-blue)
  - Size: 2px, star/zigzag shape
  - Position: on one of the two iron bands
  - Lifespan: 80ms (brief flash)

- **Authority aura:** constant glow
  - Color: `#3366CC` at alpha 0.08
  - Radius: 3px beyond gavel head outline
  - Pulse: alpha oscillates 0.05 to 0.12 over 500ms

---

## 2. Strike Animation

**Sprite sheet:** `martelao-strike.png`
**Frames:** 4
**Loop:** No (plays once per attack)
**Total duration:** 600ms

| Frame | Duration | Description         | Sound Cue                                     |
|-------|----------|---------------------|-----------------------------------------------|
| 1     | 120ms    | Raise               | `sfx_gavel_raise_whoosh.ogg` at 0ms           |
| 2     | 180ms    | Apex hold (LONGER)  | `sfx_energy_charge.ogg` at 0ms                |
| 3     | 100ms    | Downswing (FAST)    | `sfx_air_cut_heavy.ogg` at 0ms                |
| 4     | 200ms    | Impact              | `sfx_gavel_slam_earthquake.ogg` at 0ms        |

### Dramatic Timing Note
- Frame 2 (apex) is deliberately LONG (180ms) to build tension
- Frame 3 (downswing) is deliberately SHORT (100ms) for brutal speed
- This creates the "slow raise, FAST slam" comedic/dramatic rhythm

### Visual Effects (Strike)

**Frame 1 -- Raise:**
- Blue energy particles: 4-6 particles spawn from ground, spiral TOWARD gavel head
  - Color: `#3366CC`, `#6699FF`
  - Size: 2px
  - Velocity: converging on gavel, 60 px/s
  - Lifespan: matches travel time to gavel
- Shadow on ground: grows from normal to 1.5x size
  - Color: `#000000` at alpha 0.2 to 0.3

**Frame 2 -- Apex Hold:**
- Concentrated energy cloud: 8-10 particles orbiting gavel head
  - Color: `#6699FF`, `#CCDDFF`
  - Size: 1-3px
  - Velocity: circular orbit, 120 degrees/100ms
  - Radius: 6-8px from head center
- Iron band electricity: continuous zigzag lines between bands
  - Color: `#FFFFFF` to `#CCDDFF`
  - 2-3 arcs, each lasting 60ms, replaced
- Screen effect: subtle blue vignette
  - Color: `#3366CC` at alpha 0.05 on screen edges
  - Duration: entire frame

**Frame 3 -- Downswing:**
- Speed lines: 5-6 bold parallel lines
  - Color: `#1A1A1A` (black) at alpha 0.7
  - Direction: matching swing arc
  - Length: 16-24px
  - Duration: 80ms (appear and fade within frame)
- Blue comet trail: continuous stream from gavel head
  - Color: `#3366CC` to `#6699FF`, 5-8 particles
  - Size: 3-4px, shrink to 1px
  - Velocity: opposite of swing direction, 80 px/s
  - Lifespan: 120ms
- Air compression ring: white semi-circle ahead of gavel
  - Color: `#FFFFFF` at alpha 0.3
  - Size: 8px radius
  - Duration: 60ms

**Frame 4 -- Impact:**
- Ground crack pattern: radiates from impact point
  - 6-8 dark lines (`#1A1A1A`) extending 12-20px outward
  - Appear: staggered over 80ms (not all at once)
  - Persist: remain for 2 seconds, then fade over 500ms
- Debris burst: 8-10 ground particles
  - Colors: `#7B5B3A` (wood), `#666666` (stone), `#444444` (dust)
  - Size: 2-4px
  - Velocity: radial outward 60-120 px/s, upward arc
  - Lifespan: 400-600ms
  - Gravity: 100 px/s^2
  - Bounce: 1 at 0.3 coefficient
- Dust cloud: expanding ring
  - Color: `#999999` at alpha 0.4
  - Size: starts 8px radius, expands to 24px over 200ms
  - Lifespan: 300ms, fade to 0

### Screen Effects (Strike)
- **Screen shake (Frame 4 -- Impact):**
  - Intensity: 8px random offset (HEAVY shake -- this is a MASSIVE gavel)
  - Duration: 400ms
  - Decay: exponential, with 2-3 "aftershock" bumps
  - Frequency: fast, 30ms per displacement

- **White impact flash (Frame 4):**
  - Color: `#FFFFFF` at alpha 0.4
  - Duration: 60ms
  - Full screen overlay

- **Blue judicial flash (Frame 4, after white):**
  - Color: `#3366CC` at alpha 0.2
  - Duration: 100ms
  - Replaces white flash, feels like judicial authority

- **Camera slam:**
  - Trigger: Frame 4
  - Camera zooms to 1.05x over 40ms
  - Returns to 1.0x over 160ms (slow recovery)
  - Adds WEIGHT to the impact

### Onomatopeia (Strike)
- **"CENSURADO!!!"** text popup
  - Font: extreme bold, blocky, official stamp-like
  - Colors: `#CC0000` (red) fill, `#1A1A1A` 3px stroke
  - Size: starts 30px, scales to 40px over 150ms
  - Position: centered on impact point
  - Duration: 500ms
  - Animation: SLAMS down (drops 4px instantly), then slight bounce up 2px, then fade
  - Matches the gavel's slam rhythm
  - Three exclamation marks shaking independently (1px random offset each)

---

## 3. Shockwave Animation

**Sprite sheet:** `martelao-shockwave.png`
**Frames:** 4
**Loop:** No
**Total duration:** 480ms
**Trigger:** Spawned at Frame 4 of strike animation (simultaneous with impact)

| Frame | Duration | Description                | Sound Cue                              |
|-------|----------|----------------------------|----------------------------------------|
| 1     | 80ms     | Shockwave birth            | (overlaps with impact sound)           |
| 2     | 120ms    | Shockwave expansion        | `sfx_shockwave_rumble.ogg` at 0ms      |
| 3     | 150ms    | Maximum range              | (continuation)                         |
| 4     | 130ms    | Dissipation                | `sfx_shockwave_fade.ogg` at 50ms       |

### Shockwave Ring Physics
- **Expansion speed:** ring travels from center to max radius over 350ms
  - Start: 0px radius
  - End: 96px radius (the 96x96 sprite edges)
  - Speed: approximately 275 px/s
  - Easing: fast start, slight deceleration (ease-out curve)

- **Ring visual:**
  - Width: starts 4px, thins to 1px at maximum range
  - Color: `#3366CC` outer, `#CCDDFF` inner, `#FFFFFF` leading edge
  - Alpha: starts 0.8, ends 0.1 at maximum range
  - Inner rings follow at 40ms, 80ms delays (creating 3-ring pattern)

### Particle Effects (Shockwave)
- **CENSURADO echo texts:** 4-6 spawned at Frame 1
  - Text: "CENSURADO" in small (6px) red font
  - Velocity: radial outward, riding the shockwave ring
  - Lifespan: matches shockwave duration
  - Alpha: 0.5 to 0.0
  - Rotation: slight tumble

- **Blue energy wisps:** 8-12 along ring edge
  - Color: `#6699FF`
  - Size: 2-3px
  - Velocity: follow ring expansion
  - Lifespan: individual 200ms, replaced continuously
  - Create "sparkle at ring edge" effect

- **Dust/debris lifted by wave:** 4-6 at expanding ring position
  - Color: `#888888`, `#666666`
  - Size: 1-2px
  - Velocity: upward 20 px/s after ring passes
  - Lifespan: 300ms

### Sound
- **Sub-bass rumble:** `sfx_shockwave_rumble.ogg`
  - Deep 40-80Hz rumble
  - Duration: 400ms
  - Volume: starts 0.8, fades
  - Triggers gamepad vibration if available

---

## 4. "INQUERITO INSTAURADO" Stamp Effect

**Sprite sheet:** `martelao-stamp.png`
**Frames:** 3
**Loop:** No
**Total duration:** 800ms
**Trigger:** When shockwave hits an enemy

| Frame | Duration | Description          | Sound Cue                                    |
|-------|----------|----------------------|----------------------------------------------|
| 1     | 100ms    | Stamp appear (SLAM)  | `sfx_rubber_stamp_slam.ogg` at 0ms           |
| 2     | 400ms    | Stamp hold           | (none -- ominous silence)                    |
| 3     | 300ms    | Stamp fade           | `sfx_paper_dissolve.ogg` at 100ms            |

### Stamp Animation Details
- **Appear (Frame 1):**
  - Stamp drops from above (Y offset: -8px to 0px in 60ms)
  - Overshoot: goes to +2px then bounces back to 0px
  - Red ink splatter: 4 small dots at corners burst outward (3px each)
  - Brief red flash on stamped enemy (alpha 0.3, 40ms)
  - Mini screen shake: 2px, 60ms (stamp force)

- **Hold (Frame 2):**
  - Stamp stable over enemy
  - Text fully visible and clear
  - Enemy sprite underneath tinted slightly grey (suppressed/silenced)
  - Small yellow shock stars orbit stamp (3-4 stars, circular path)
    - Size: 2px
    - Orbit radius: 4px beyond stamp edge
    - Speed: 1 full orbit per 400ms

- **Fade (Frame 3):**
  - Letters dissolve individually (random order)
  - Each letter becomes particles: 3-4 red specs per letter
    - Velocity: random drift, 10-20 px/s
    - Lifespan: 200ms each
  - Border breaks into dashed segments, then fades
  - Final puff of bureaucratic dust (grey, 6px, 150ms)

---

## 5. Silence Effect on Enemies

**Sprite sheet:** `martelao-silence.png`
**Frames:** 2
**Loop:** Yes (for silence duration)
**Total cycle:** 400ms
**Duration:** varies (e.g., 3-5 seconds)

| Frame | Duration | Description            |
|-------|----------|------------------------|
| 1     | 200ms    | Mute icon normal       |
| 2     | 200ms    | Mute icon pulse/larger |

### Silence Visual Effects (on enemy)
- **Mute icon:** positioned 4px above enemy head center
  - Vertical bob: +/- 1px, 600ms period

- **Enemy sprite effects while silenced:**
  - Grey tint overlay: `#888888` at alpha 0.15
  - No attack animations play (visually "frozen" attacks)
  - Blue "shush" particles: 1 per 300ms
    - Color: `#3366CC`
    - Size: 1px
    - Rises from enemy, 10 px/s upward
    - Lifespan: 250ms

- **Silence end effect:**
  - Mute icon shatters: breaks into 4-5 blue fragments
    - Velocity: radial outward 40 px/s
    - Lifespan: 200ms
  - Small "pop" sound: `sfx_silence_end_pop.ogg`
  - Enemy tint instantly removed
  - Brief white flash on enemy (alpha 0.2, 60ms)

---

## Phaser 3 Animation Keys

```
martelao_idle          -- 3 frames, 500ms cycle, loop
martelao_strike        -- 4 frames, 600ms, no loop
martelao_shockwave     -- 4 frames, 480ms, no loop (spawned at strike Frame 4)
martelao_stamp         -- 3 frames, 800ms, no loop (spawned on enemy hit)
martelao_silence       -- 2 frames, 400ms cycle, loop (duration: silence_time)
```

### Attack Sequence Timeline

```
0ms      -- Strike Frame 1 (raise) begins
120ms    -- Strike Frame 2 (apex hold) begins
300ms    -- Strike Frame 3 (downswing) begins -- FAST
400ms    -- Strike Frame 4 (impact) begins
400ms    -- Shockwave Frame 1 spawned simultaneously
400ms    -- Screen shake begins (8px, 400ms)
400ms    -- "CENSURADO!!!" onomatopeia appears
480ms    -- Shockwave Frame 2
~500ms   -- Shockwave reaches first enemy -> stamp spawns on that enemy
600ms    -- Strike animation ends, return to idle
600ms    -- Shockwave Frame 3 (maximum range)
~650ms   -- Shockwave reaches far enemies -> more stamps
730ms    -- Shockwave Frame 4 (dissipation)
880ms    -- Shockwave fully dissipated
~1300ms  -- Stamps begin fading on enemies
~1700ms  -- All stamps fully faded, silence icons remain
```

### Cooldown
- Attack cooldown: 1200ms (heavy gavel, slow recovery)
- During cooldown: Xandao pulls gavel back to idle (implied, not animated separately)
- Silence on enemies lasts: 4000ms per hit
