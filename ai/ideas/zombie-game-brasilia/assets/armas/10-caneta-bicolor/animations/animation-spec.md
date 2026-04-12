# Caneta Bicolor -- Animation Specification

**Weapon ID:** 10
**Boss:** BolsoLula (Fusion Boss)
**Target FPS:** 10 fps (100ms base frame duration)
**Style:** Twitchy, jerky Andre Guedes animation

---

## 1. Idle Animation (Held Weapon)

**Sprite sheet:** `caneta-bicolor-idle.png`
**Frames:** 3 (static + 2 pulse variants)
**Loop:** Yes, continuous
**Total cycle:** 600ms

| Frame | Duration | Description                          |
|-------|----------|--------------------------------------|
| 1     | 200ms    | Static, both ends equally glowing    |
| 2     | 200ms    | Red pulse (Lula side dominant)       |
| 3     | 200ms    | Green pulse (Bolsonaro side dominant) |

### Particle Effects (Idle)
- **Red ink drip:** 1 particle per 500ms from red nib
  - Color: `#E60000`
  - Size: 2px circle
  - Velocity: downward 8 px/s
  - Lifespan: 300ms
  - Gravity: 40 px/s^2

- **Green ink drip:** 1 particle per 500ms from green nib (offset 250ms from red)
  - Color: `#00AA44`
  - Size: 2px circle
  - Velocity: downward 8 px/s
  - Lifespan: 300ms
  - Gravity: 40 px/s^2

- **Dual aura glow:** constant
  - Red side: `#CC0000` at alpha 0.10, pulses to 0.18
  - Green side: `#009739` at alpha 0.10, pulses to 0.18
  - Pulse cycle: 600ms, opposite phase (when red peaks, green is at low)
  - Radius: 3-5px from pen edges

- **Infinity symbol:** floating near pen
  - Sprite: `caneta-infinity.png`
  - Position: 6px above pen center
  - Animation: 2-frame loop, 400ms cycle
  - Alpha: 0.5 (subtle indicator)
  - Bob: +/- 1px vertical oscillation over 800ms

---

## 2. Signature / Attack Animation

**Sprite sheet:** `caneta-bicolor-attack.png`
**Frames:** 4
**Loop:** No (plays once per attack)
**Total duration:** 520ms

| Frame | Duration | Description            | Sound Cue                                   |
|-------|----------|------------------------|---------------------------------------------|
| 1     | 100ms    | Lift                   | `sfx_pen_click.ogg` at 0ms                  |
| 2     | 120ms    | Downstroke start       | `sfx_pen_scratch_heavy.ogg` at 0ms          |
| 3     | 150ms    | Signature flourish     | `sfx_pen_scratch_flourish.ogg` at 0ms       |
| 4     | 150ms    | Stamp/release          | `sfx_stamp_aprovado.ogg` at 50ms            |

### Visual Effects (Attack)
- **Ink spray (Frame 2-3):** continuous stream
  - Red ink: 3-4 particles per frame from red nib
    - Color: `#E60000`
    - Size: 1-3px
    - Velocity: follow pen motion direction, 40-80 px/s
    - Lifespan: 200-400ms
    - Stain: leaves persistent ground mark (alpha 0.3)
  - Green ink: 3-4 particles per frame from green nib
    - Color: `#00AA44`
    - Size: 1-3px
    - Velocity: follow pen motion, offset 15 degrees from red
    - Lifespan: 200-400ms
    - Stain: leaves persistent ground mark (alpha 0.3)

- **Paper materialization (Frame 2):** 
  - Cream rectangle (`#FFF8DC`) fades in at pen position
  - Size: 16x10px
  - Alpha: 0 to 0.8 over 100ms
  - Stays until Frame 4 transforms into projectile

- **Signature trail (Frame 2-3):**
  - Dual-color line following pen tip motion
  - Red line on left, green line on right
  - Line width: 1px each
  - Creates illegible scrawl pattern on paper

- **APROVADO stamp (Frame 4):**
  - Red stamp text appears on document: "APROVADO"
  - Color: `#CC0000` 
  - Angle: slight diagonal tilt (-10 degrees)
  - Animation: instant appear with 1px "slam" downward
  - Small dust particles (4-5 cream specs) burst on stamp impact

- **R$ money float (Frame 4):**
  - "R$" golden text rises from document
  - Color: `#FFD700`
  - Size: 8px
  - Velocity: upward 15 px/s, slight random X drift
  - Lifespan: 400ms
  - Alpha: 1.0 to 0.0

### Screen Effects (Attack)
- **Mini-shake on stamp (Frame 4):**
  - Intensity: 2px
  - Duration: 80ms
  - Conveys bureaucratic force

---

## 3. Projectile Flight -- Explosive Amendment

**Sprite sheet:** `caneta-bicolor-projectile.png`
**Frames:** 4 (flutter cycle)
**Loop:** Yes (while in flight)
**Total cycle:** 400ms
**Projectile speed:** 120 px/s (slower than bullets -- it is a fluttering paper)

| Frame | Duration | Description               |
|-------|----------|---------------------------|
| 1     | 100ms    | Amendment flight A (flat) |
| 2     | 100ms    | Amendment flight B (tilt) |
| 3     | 100ms    | Amendment flight C (tilt) |
| 4     | 100ms    | Amendment flight D (flat) |

### Particle Trail (Flight)
- **Red ink drops:** 1 per frame, trailing left
  - Color: `#E60000`
  - Size: 1-2px
  - Velocity: left 10 px/s + backward 5 px/s
  - Lifespan: 300ms

- **Green ink drops:** 1 per frame, trailing right
  - Color: `#00AA44`
  - Size: 1-2px
  - Velocity: right 10 px/s + backward 5 px/s
  - Lifespan: 300ms

- **Paper ash particles:** 1 per 2 frames
  - Color: `#D4C4A0` (singed cream)
  - Size: 1px
  - Velocity: random drift, 5 px/s
  - Lifespan: 250ms

- **Pulsing glow:** on projectile sprite
  - Alternates: red tint (Frames 1-2), green tint (Frames 3-4)
  - Alpha: oscillates 0.1 to 0.25

### Sound (Flight)
- `sfx_paper_flutter_loop.ogg` -- continuous while in flight
- Volume: 0.4, subtle rustling sound
- Pitch shift: slight randomization per instance

---

## 4. Impact / Explosion -- Bureaucratic Detonation

**Sprite sheet:** `caneta-bicolor-explosion.png`
**Frames:** 4
**Loop:** No
**Total duration:** 550ms

| Frame | Duration | Description             | Sound Cue                                  |
|-------|----------|-------------------------|--------------------------------------------|
| 1     | 80ms     | Paper burst             | `sfx_paper_rip_explosion.ogg` at 0ms       |
| 2     | 150ms    | Ink explosion           | `sfx_ink_splash_heavy.ogg` at 0ms          |
| 3     | 180ms    | Maximum expansion       | `sfx_bureaucratic_boom.ogg` at 0ms         |
| 4     | 140ms    | Aftermath               | `sfx_coins_scatter.ogg` at 50ms            |

### Screen Effects (Explosion)
- **Screen shake:**
  - Trigger: Frame 1
  - Intensity: 5px
  - Duration: 250ms
  - Decay: exponential

- **Dual-color flash:**
  - Trigger: Frame 1
  - Left half of screen: `#CC0000` (red) at alpha 0.15
  - Right half of screen: `#009739` (green) at alpha 0.15
  - Duration: 80ms
  - (Reinforces the bicolor theme even in screen effects)

- **Camera zoom:**
  - Trigger: Frame 2
  - Zoom: 1.03x for 100ms, return

### Particle Effects (Explosion)
- **Paper confetti:** 12-15 particles at Frame 1
  - Color: `#FFF8DC` (cream) with some `#D4C4A0` (singed)
  - Size: 2-4px rectangles
  - Velocity: radial outward 60-120 px/s
  - Rotation: random spin
  - Lifespan: 500-800ms
  - Gravity: 40 px/s^2
  - Some particles have tiny text on them (decorative only)

- **Red ink splash:** 10-12 particles at Frame 1-2
  - Color: `#E60000` to `#CC0000`
  - Size: 3-6px irregular blobs
  - Velocity: radial outward WEST hemisphere, 40-100 px/s
  - Lifespan: 400-600ms
  - Ground stain: each particle leaves persistent red mark (alpha 0.2, 2-3px)

- **Green ink splash:** 10-12 particles at Frame 1-2
  - Color: `#00AA44` to `#009739`
  - Size: 3-6px irregular blobs
  - Velocity: radial outward EAST hemisphere, 40-100 px/s
  - Lifespan: 400-600ms
  - Ground stain: each particle leaves persistent green mark (alpha 0.2, 2-3px)

- **Mixed ink center:** 4-6 particles
  - Color: `#5C4033` (muddy brown -- red+green mix)
  - Size: 4-8px
  - Velocity: slow radial, 20-40 px/s
  - Lifespan: 600ms
  - Represents political mixing

- **R$ money symbols:** 4-6 at Frame 2-3
  - Color: `#FFD700` (gold)
  - Size: 6-8px text "R$"
  - Velocity: radial outward 50-80 px/s, then float upward
  - Rotation: spinning
  - Lifespan: 800ms
  - Alpha: 1.0, fade after 500ms

- **Stamp fragments:** 3-4 at Frame 1
  - Tiny text shards: "URG-", "SIG-", "CONF-" (torn bureaucratic stamps)
  - Color: `#CC0000` (red ink)
  - Size: 4-6px
  - Velocity: radial 60-90 px/s
  - Lifespan: 400ms

### Onomatopeia
- **"EMENDAAAA!"** text popup
  - Font: bold, bureaucratic serif (like official document font), but cracked/exploding
  - Colors: gradient RED to GREEN left-to-right, `#1A1A1A` 2px stroke
  - Size: starts 20px, scales to 30px over 200ms
  - Position: centered on impact
  - Duration: 450ms
  - Animation: scale up, letters separate slightly (explosion force), then fade
  - Rotation: slight wobble +/- 3 degrees

- **"APROVADO!"** secondary stamp
  - Appears 150ms after EMENDAAAA
  - Red stamp aesthetic: `#CC0000` text in rectangular border
  - Angle: -10 degrees (classic stamp tilt)
  - Size: 12px
  - Duration: 300ms
  - Animation: slam down (2px drop), then fade

---

## 5. Ink Trail (Persistent Ground Effect)

**Sprite sheet:** `caneta-bicolor-trail.png`
**Frames:** 2
**Loop:** No (placed as static decals)
**Lifespan:** 8 seconds, then alpha fade over 2 seconds

| Frame | Description              |
|-------|--------------------------|
| 1     | Trail variant A          |
| 2     | Trail variant B          |

### Placement Logic
- One trail decal placed every 32px along projectile path
- Randomly selects variant A or B
- Random rotation (0, 90, 180, 270 degrees)
- Alpha: starts 0.5, fades to 0.0 over final 2 seconds of 8-second lifespan

---

## 6. Infinity Symbol (UI Indicator)

**Sprite sheet:** `caneta-infinity.png`
**Frames:** 2
**Loop:** Yes, continuous
**Total cycle:** 400ms

| Frame | Duration | Description                      |
|-------|----------|----------------------------------|
| 1     | 200ms    | Infinity: red left, green right  |
| 2     | 200ms    | Infinity: green left, red right  |

- Positioned 6px above weapon sprite
- Alpha: 0.5 (subtle, not distracting)
- Vertical bob: sinusoidal +/- 1px, 800ms period

---

## Phaser 3 Animation Keys

```
caneta_idle          -- 3 frames, 600ms cycle, loop
caneta_attack        -- 4 frames, 520ms, no loop
caneta_projectile    -- 4 frames, 400ms cycle, loop
caneta_explosion     -- 4 frames, 550ms, no loop
caneta_trail         -- 2 frames, static decal placement (no animation)
caneta_infinity      -- 2 frames, 400ms cycle, loop
```

### Attack Cooldown
- Cooldown between attacks: 800ms (BolsoLula signs fast but not instant)
- During cooldown: pen returns to idle animation
- No ammo system -- infinite ink, infinite amendments, infinite spending
