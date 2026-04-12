# Toga de Teflon -- Animation Specification

**Weapon ID:** 12
**Boss:** Gilmar (Gilmar Mendes)
**Target FPS:** 10 fps (100ms base frame duration)
**Style:** Twitchy, jerky Andre Guedes animation

---

## 1. Idle Animation (Worn)

**Sprite sheet:** `toga-idle.png`
**Frames:** 3 (static + 2 shimmer variants)
**Loop:** Yes, continuous
**Total cycle:** 600ms

| Frame | Duration | Description                           |
|-------|----------|---------------------------------------|
| 1     | 200ms    | Static, teflon sheen at rest          |
| 2     | 200ms    | Shimmer A -- highlights shift CW      |
| 3     | 200ms    | Shimmer B -- highlights shift CCW     |

### Particle Effects (Idle)
- **Teflon gleam:** 1 particle per 500ms
  - Color: `#A0AEC0` to `#E2E8F0` (silver)
  - Size: 1-2px, brief star shape
  - Position: random on toga surface (one of the teflon patches)
  - Lifespan: 120ms (quick flash)

- **Money drop:** 1 bill particle per 2000ms (SLOW but constant)
  - Sprite: `toga-money.png` (16x16, 4 frames)
  - Spawn: at pocket position
  - Animation: plays 4-frame flutter cycle over 600ms
  - Velocity: 0 horizontal initially, then slight drift based on Gilmar's movement direction
  - Final frame (landed bill): remains on ground as decal
    - Alpha: 0.7
    - Lifespan as decal: 10 seconds, then fade over 2 seconds
  - Creates a TRAIL of money wherever Gilmar walks

- **Grease shimmer:** subtle
  - Each grease stain (3-4 on toga): slight alpha pulse
  - `#E8C547` alpha oscillates 0.6 to 0.8 over 800ms
  - Each stain on offset cycle (creates slow "greasy movement")

---

## 2. Deflection Animation (Reactive -- Triggered by Incoming Projectile)

**Sprite sheet:** `toga-deflect.png`
**Frames:** 4
**Loop:** No (plays once per deflection)
**Total duration:** 500ms

| Frame | Duration | Description           | Sound Cue                                      |
|-------|----------|-----------------------|------------------------------------------------|
| 1     | 80ms     | Projectile contact    | `sfx_teflon_ding.ogg` at 0ms                   |
| 2     | 120ms    | Teflon activation     | `sfx_teflon_slide.ogg` at 0ms                  |
| 3     | 180ms    | Reflect OR absorb     | See branching below                            |
| 4     | 120ms    | Recovery              | `sfx_fabric_settle.ogg` at 50ms                |

### Deflection Trigger
- Triggered automatically when ANY projectile collides with Gilmar's hitbox
- The toga is ALWAYS active (passive defensive weapon)
- 100% of projectiles are deflected (never takes direct projectile damage)
- 33% of deflected projectiles REFLECT back to attacker
- 67% of deflected projectiles are simply ABSORBED (nullified)

### Visual Effects (All Deflections)

**Frame 1 -- Contact:**
- Impact flash at collision point
  - Color: `#E2E8F0` (bright silver)
  - Shape: 6-pointed star, 6px
  - Duration: 60ms
  - Rotation: random angle
- Ripple effect on toga fabric
  - Concentric semi-circles from impact point (2 rings)
  - Color: `#4A5568` (teflon) at alpha 0.3
  - Expansion: 10px over 80ms
- Sound: metallic "ding" -- like hitting a non-stick pan

**Frame 2 -- Teflon Activation:**
- ALL teflon sheen patches glow simultaneously
  - Color: brightens from `#4A5568` to `#A0AEC0`
  - Duration: 120ms
- Silver-blue energy field
  - Color: `#63B3ED` at alpha 0.2
  - Shape: follows toga outline, 3px beyond edges
  - Pulse: single pulse brightening to alpha 0.4, back to 0.2
- Sliding visual: directional streak marks
  - Color: `#E2E8F0` (silver)
  - 2-3 short lines (4-6px) moving ACROSS toga surface in deflection direction
  - Speed: fast, 100 px/s
  - Lifespan: 80ms
- "NADA PEGA" micro-text
  - Color: `#A0AEC0`
  - Size: 6px
  - Position: near impact point
  - Alpha: 0.4 (very subtle)
  - Lifespan: 100ms

### Branching at Frame 3

#### Branch A -- Reflection (33%)

**Sound:** `sfx_teflon_reflect_whoosh.ogg` at 0ms

**Effects:**
- Reflected projectile spawns
  - Direction: back toward original attacker
  - Speed: 1.2x original projectile speed (FASTER return)
  - Sprite: `toga-reflected-projectile.png` (red-tinted version)
  - Spawn position: toga surface at contact point
- Launch flash
  - Color: `#FF4444` (red) + `#E2E8F0` (silver) mixed star
  - Size: 8px
  - Duration: 60ms
- Speed lines from toga outward
  - Color: `#1A1A1A` at alpha 0.5
  - 3-4 lines radiating from launch point
  - Length: 12px
  - Duration: 100ms
- Toga ripple outward (reverse of contact ripple)
  - Fabric pushes outward from launch point
  - 2 concentric rings moving OUT
- **"DEVOLVIDO!"** text popup
  - Color: `#FF4444` (red) fill, `#1A1A1A` stroke
  - Size: 12px
  - Duration: 300ms
  - Animation: punch out from toga, drift in projectile direction, fade

#### Branch B -- Absorption (67%)

**Sound:** `sfx_teflon_absorb_soft.ogg` at 0ms

**Effects:**
- Projectile dissolve sequence
  - Plays `toga-absorb.png` (3 frames, 180ms) at contact point
  - Projectile sprite fades while silver particles replace it
- Silver sparkle cloud
  - 5-6 particles at dissolution point
  - Color: `#A0AEC0`, `#E2E8F0`
  - Size: 1-2px
  - Velocity: drift TOWARD toga center (absorbed inward), 15-25 px/s
  - Lifespan: 200ms
- Subtle toga "gulp" -- toga briefly brightens (absorbing energy)
  - Global brightness: +10% for 80ms
- **"R$" money symbol** floats up from absorption
  - Color: `#2D8B4E` (money green)
  - Size: 6px
  - Velocity: upward 12 px/s
  - Lifespan: 300ms
  - Alpha: 0.8 to 0.0
  - Commentary: even absorbed projectile energy becomes money for Gilmar

**Frame 4 -- Recovery (both branches):**
- Teflon sheen dims back to idle levels over 120ms
- Silver sparkles: 2-3 remaining, fading
- Toga settles (fabric ripples subside)
- Money in pocket: one bill may have slipped further out
  - Random: 20% chance per deflection that an EXTRA bill drops from pocket
  - This is purely visual/narrative (corruption overflowing under pressure)

### Screen Effects (Deflection)
- **Screen shake:** NONE for absorption, MINIMAL (2px, 80ms) for reflection
  - The toga is SMOOTH -- impacts are absorbed, not transmitted
  - This contrasts with the Martelao's heavy shakes

- **Flash:**
  - Reflection: brief silver flash (`#E2E8F0` at alpha 0.15, 40ms)
  - Absorption: no flash (silent and smooth)

---

## 3. Reflected Projectile Flight

**Sprite sheet:** `toga-reflected-projectile.png`
**Frames:** 3
**Loop:** Yes (while in flight)
**Total cycle:** 240ms
**Projectile speed:** 1.2x original projectile speed

| Frame | Duration | Description              |
|-------|----------|--------------------------|
| 1     | 80ms     | Reflected shot A         |
| 2     | 80ms     | Reflected shot B         |
| 3     | 80ms     | Reflected shot C         |

### Particle Trail (Reflected Projectile)
- **Silver-blue teflon wisps:** 2 per frame
  - Color: `#63B3ED` to `#A0AEC0`
  - Size: 2px, shrinks to 1px
  - Velocity: opposite of flight direction, 20 px/s
  - Lifespan: 150ms

- **Red corruption tint particles:** 1 per 2 frames
  - Color: `#FF4444`
  - Size: 1px
  - Random scatter from trail
  - Lifespan: 100ms

### Sound (Reflected Projectile)
- `sfx_reflected_whoosh.ogg` -- quick single-shot whoosh
- No looping sound (reflected projectile is fast, short-lived)

### Impact (Reflected Projectile Hitting Attacker)
- Uses the ORIGINAL weapon's impact animation but with added red tint
- Additional effect: "DEVOLVIDO" stamp briefly appears on hit enemy
  - Color: `#FF4444`
  - Size: 10px text
  - Duration: 200ms
  - Angle: -8 degrees

---

## 4. Money Trail (Passive Continuous Effect)

**Sprite sheet:** `toga-money.png`
**Frames:** 4
**Loop:** No (plays once per spawned bill, then becomes static decal)
**Total cycle:** 600ms per bill

| Frame | Duration | Description            |
|-------|----------|------------------------|
| 1     | 150ms    | Bill flutter A (0 deg) |
| 2     | 150ms    | Bill flutter B (+20)   |
| 3     | 150ms    | Bill flutter C (-20)   |
| 4     | 150ms    | Bill flutter D (land)  |

### Money Trail System
- **Spawn rate:** 1 bill every 2000ms while Gilmar is alive
- **Spawn position:** Gilmar's pocket (right side of sprite)
- **Fall trajectory:**
  - Vertical: pocket height to ground, over 600ms
  - Horizontal: inherits 30% of Gilmar's velocity (bills drift in his wake)
- **Ground state (after landing):**
  - Uses Frame 4 as static decal
  - Alpha: 0.7
  - Rotation: random (0/90/180/270)
  - Lifespan: 10 seconds as ground decal, then fades over 2 seconds
  - Max ground bills: 30 (oldest despawn when limit reached)
- **Narrative purpose:** Gilmar leaves a literal trail of money wherever he goes

### Sound
- `sfx_bill_flutter.ogg` -- very quiet (volume 0.1), plays per bill
- At high bill density: sounds create ambient "rustling money" effect

---

## 5. "NADA PEGA" Text Popup (On Deflection)

**Sprite:** `toga-nadapega.png` (code-animated)
**Frames:** 1 (static, animated via tween)
**Duration:** 350ms

### Animation Tween
```
0ms     -- Appear at contact point, alpha 0.0, scale 0.5x
50ms    -- Alpha 0.6, scale 1.0x (pop in)
100ms   -- Alpha 0.8, scale 1.0x, begin drift upward
250ms   -- Alpha 0.4, drifted 6px upward
350ms   -- Alpha 0.0, drifted 10px upward (gone)
```

### Teflon Sheen on Text
- A silver highlight moves LEFT to RIGHT across the text over 200ms
  - Color: `#E2E8F0` at alpha 0.3
  - Width: 4px "wipe" band
  - Creates the "non-stick surface" visual on the letters themselves

---

## 6. Pastel Grease Accumulation (Phase Mechanic -- Optional)

**Implementation note:** If the boss fight has multiple phases, grease stains can INCREASE over time:

| Phase | Grease Stains | Visual Change                                 |
|-------|---------------|-----------------------------------------------|
| 1     | 3 stains      | Standard (as described in Frame 1)            |
| 2     | 5 stains      | Two new stains appear, one with a larger crumb |
| 3     | 7 stains      | Toga is visibly FILTHY, grease dripping        |

- New stains appear via `sfx_grease_splat.ogg` (quiet, wet sound)
- Each new stain: yellow blob (`#E8C547`) expands from 0 to 5-8px over 200ms
- Grease particles drip from toga in later phases:
  - Color: `#C4A030`
  - Size: 1px
  - Rate: 1 per 1000ms (Phase 2), 1 per 400ms (Phase 3)
  - Falls to ground, leaves small grease spot decal

---

## Phaser 3 Animation Keys

```
toga_idle                -- 3 frames, 600ms cycle, loop
toga_deflect             -- 4 frames, 500ms, no loop (Frame 3 is branched)
toga_absorb              -- 3 frames, 180ms, no loop (plays at contact point)
toga_reflected_proj      -- 3 frames, 240ms cycle, loop (while reflected projectile flies)
toga_money               -- 4 frames, 600ms, no loop (per spawned bill)
toga_nadapega            -- 1 frame, code-tweened, 350ms
```

### Deflection Logic (Game Code Reference)

```
on_projectile_hit(projectile):
  // Toga ALWAYS deflects -- Gilmar never takes projectile damage
  play("toga_deflect")
  
  roll = random(0.0, 1.0)
  if roll < 0.33:
    // REFLECT: send it back
    reflected = spawn_projectile_at(gilmar.position, 
      direction = -projectile.direction,
      speed = projectile.speed * 1.2,
      sprite = "toga_reflected_proj",
      damage = projectile.damage * 0.8)
    play_sound("sfx_teflon_reflect_whoosh")
    show_text("DEVOLVIDO!")
    screen_shake(2, 80)
  else:
    // ABSORB: nullify
    play("toga_absorb", at = projectile.position)
    play_sound("sfx_teflon_absorb_soft")
    spawn_money_symbol(projectile.position)  // even absorbed attacks become $
  
  show_text("NADA PEGA", at = contact_point)
  
  // 20% chance an extra bill falls on deflection
  if random() < 0.20:
    spawn_extra_bill(gilmar.pocket_position)
```

### Vulnerability Note
- The toga deflects PROJECTILES only
- Gilmar IS vulnerable to MELEE attacks (you have to get close)
- This creates the core gameplay tension: ranged is useless, melee is dangerous
- Visual hint: when player is in melee range, toga stops shimmering (teflon does not protect against direct contact)

### Sound Design Note
- All toga sounds should feel SMOOTH, SLICK, UNCTUOUS
- No harsh impacts -- everything slides, glides, absorbs
- Contrast with Martelao (which is all HEAVY IMPACTS)
- The money rustling should feel constant and slightly nauseating
- "NADA PEGA" should be whispered, not shouted (Gilmar is subtle, not loud)
