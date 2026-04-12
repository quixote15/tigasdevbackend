# Arma que Brocha (as Vezes) -- Animation Specification

**Weapon ID:** 09
**Boss:** Bolsonaro
**Target FPS:** 10 fps (100ms base frame duration)
**Style:** Twitchy, jerky Andre Guedes animation

---

## 1. Idle Animation (Held Weapon)

**Sprite sheet:** `arma-brocha-idle.png`
**Frames:** 3 (static + 2 gleam variants)
**Loop:** Yes, continuous
**Total cycle:** 500ms

| Frame | Duration | Description                      |
|-------|----------|----------------------------------|
| 1     | 200ms    | Static pose, no gleam            |
| 2     | 150ms    | Gold gleam on barrel tip         |
| 3     | 150ms    | Gold gleam shifted to grip       |

### Particle Effects (Idle)
- **Gold sparkle:** 1 particle per 300ms
  - Color: `#FFD700` then `#FFEAA7` (bright gold to pale)
  - Size: 1-2px, star shape
  - Position: random on gun surface
  - Lifespan: 200ms
  - Animation: appear, flash bright, disappear

- **Ego aura (subtle):** Faint gold glow around entire gun
  - Color: `#DAA520` at alpha 0.08
  - Pulse: alpha oscillates 0.05 to 0.12 over 600ms
  - Radius: 4px beyond gun outline

---

## 2. Successful Shot Animation (70% Branch)

**Sprite sheet:** `arma-brocha-fire-success.png`
**Frames:** 4
**Loop:** No (plays once per attack)
**Total duration:** 380ms

| Frame | Duration | Description          | Sound Cue                                |
|-------|----------|----------------------|------------------------------------------|
| 1     | 80ms     | Aim                  | `sfx_revolver_cock.ogg` at 0ms           |
| 2     | 100ms    | Fire                 | `sfx_revolver_shot_loud.ogg` at 0ms      |
| 3     | 100ms    | Recoil peak          | (continuation)                           |
| 4     | 100ms    | Recovery             | `sfx_shell_casing_tink.ogg` at 50ms      |

### Screen Effects (Successful Shot)
- **Screen shake:**
  - Trigger: Frame 2 (fire)
  - Intensity: 5px random offset
  - Duration: 200ms
  - Decay: fast linear

- **Muzzle flash overlay:**
  - Trigger: Frame 2
  - Color: `#FFFFFF` at alpha 0.4 (full screen)
  - Duration: 60ms, instant off

- **Directional zoom:**
  - Trigger: Frame 2
  - Camera micro-push toward target: 2px over 80ms, return

### Particle Effects (Successful Shot)
- **Muzzle flash particles:** 8-10 burst at Frame 2
  - Colors: `#FFFFFF`, `#FFD700`, `#FF8C00`
  - Size: 2-4px
  - Velocity: forward cone (30 degree spread), 100-200 px/s
  - Lifespan: 100-200ms

- **Smoke cloud:** spawns at Frame 2-3
  - Color: `#888888` to `#AAAAAA`
  - Size: 4px, grows to 12px
  - Velocity: forward 10 px/s, then upward drift
  - Lifespan: 400ms
  - Alpha: 0.6 to 0.0

- **Shell casing:** 1 particle at Frame 3
  - Color: `#DAA520` (gold)
  - Size: 3x2px rectangle
  - Velocity: sideways 40 px/s, downward 20 px/s
  - Rotation: spinning
  - Lifespan: 600ms
  - Gravity: 80 px/s^2
  - Bounce: 2 bounces at 0.4 coefficient
  - Sound: `sfx_shell_casing_tink.ogg` on first bounce

### Onomatopeia (Successful Shot)
- **"BAAANG!"** text popup
  - Font: extra bold, jagged edges, massive
  - Colors: `#FFD700` (gold) fill, `#1A1A1A` 3px stroke
  - Size: starts 28px, scales to 36px over 150ms
  - Position: offset toward target from muzzle
  - Duration: 350ms
  - Rotation: slight tilt matching shot direction
  - Animation: punch-scale up, then fade

---

## 3. Backfire Animation (30% Branch)

**Sprite sheet:** `arma-brocha-fire-fail.png`
**Frames:** 4
**Loop:** No (plays once per attack)
**Total duration:** 700ms (deliberately SLOW for comedic timing)

| Frame | Duration | Description          | Sound Cue                                 |
|-------|----------|----------------------|-------------------------------------------|
| 1     | 100ms    | Aim (identical)      | `sfx_revolver_cock.ogg` at 0ms            |
| 2     | 150ms    | Misfire              | `sfx_dry_click.ogg` at 0ms                |
| 3     | 200ms    | Backfire damage      | `sfx_pathetic_pop.ogg` at 50ms            |
| 4     | 250ms    | Embarrassment (LONG) | `sfx_talkei_sad.ogg` at 100ms             |

### Screen Effects (Backfire)
- **Anti-shake (comedic stillness):**
  - Trigger: Frame 2
  - Brief 80ms FREEZE (game pauses for comedic beat)
  - Followed by tiny 2px shake for 100ms

- **Desaturation flash:**
  - Trigger: Frame 3
  - Screen briefly desaturates 30% for 150ms (world goes slightly grey)
  - Represents Bolsonaro's failure affecting reality

- **Sad vignette:**
  - Trigger: Frame 4
  - Dark edges (vignette) alpha 0.15 for 200ms
  - Emphasizes pathetic mood

### Particle Effects (Backfire)
- **Pathetic smoke puff:** at Frame 2
  - Color: `#888888` to `#666666`
  - Size: 3px, grows to 8px (tiny compared to real shot)
  - Velocity: forward only 5 px/s (no force)
  - Lifespan: 400ms
  - Shape: lumpy, drooping

- **Soot burst (backward):** at Frame 3
  - Color: `#333333` (dark soot)
  - 4-5 particles directed BACK toward Bolsonaro
  - Size: 2-3px
  - Velocity: backward 30-50 px/s
  - Lifespan: 300ms

- **Gold flakes falling:** at Frame 3-4
  - Color: `#DAA520` (gold paint chips)
  - 3-4 tiny rectangles
  - Velocity: slow drift downward 10-15 px/s
  - Rotation: slow tumble
  - Lifespan: 500ms

- **Sad sweat drop:** at Frame 4
  - Color: `#66AAFF` (blue)
  - Size: 3px teardrop shape
  - Position: beside gun barrel
  - Animation: appears, slides down 5px over 200ms, fades

### "TALKEI?" Popup (Backfire)
- **Trigger:** Frame 4, 100ms after frame start
- **Sound:** `sfx_talkei_sad.ogg` (Bolsonaro's voice, deflated/sad tone)
- **Text:** "TALKEI?"
  - Speech bubble: white fill, 2px black outline
  - Font: bold red comic book, letters slightly trembling
  - Size: 16px, does NOT scale up (stays small and pathetic, unlike the "BAAANG!")
  - Position: above Bolsonaro's head
  - Duration: 500ms
  - Animation: gentle float upward 3px, then fade
  - Wobble: letters randomly offset 0.5px each frame

### Onomatopeia (Backfire)
- **"pfft..."** text popup (instead of "BAAANG!")
  - Font: thin, italic, lowercase (opposite of the bold success text)
  - Color: `#888888` (grey, not gold)
  - Size: 10px (tiny)
  - Position: at muzzle
  - Duration: 300ms
  - Animation: slow drift upward, fade
  - No scaling, no drama

### Self-Damage Visual (Backfire)
- Bolsonaro takes self-damage: red flash on his sprite
  - Color: `#FF0000` tint at alpha 0.3
  - Duration: 150ms, 2 pulses
  - Small red "-HP" text floats from Bolsonaro upward
    - Color: `#FF0000`
    - Size: 8px
    - Lifespan: 400ms

---

## 4. Projectile Flight (Successful Only)

**Sprite sheet:** `arma-brocha-bullet.png`
**Frames:** 4 (spin cycle)
**Loop:** Yes (while in flight)
**Total cycle:** 240ms
**Projectile speed:** 280 px/s (fast -- it is a bullet)

| Frame | Duration | Description            |
|-------|----------|------------------------|
| 1     | 60ms     | Bullet flight A        |
| 2     | 60ms     | Bullet flight B        |
| 3     | 60ms     | Bullet flight C        |
| 4     | 60ms     | Bullet flight D        |

### Particle Trail (Flight)
- **Gold streak:** continuous trail
  - Color: `#FFD700` to `#DAA520`
  - Size: 2px, shrinks to 1px
  - Spawn rate: every 10ms (dense trail)
  - Lifespan: 150ms
  - Fade: alpha 0.6 to 0.0

- **Flame wisps:** 1 per frame
  - Colors: `#FF8C00`, `#FF6B00`
  - Size: 2px
  - Velocity: opposite of bullet direction, 15 px/s
  - Lifespan: 100ms

### Sound (Flight)
- `sfx_bullet_whiz.ogg` -- quick pass sound, not looping
- Doppler pitch shift based on distance

---

## 5. Bullet Impact

**Sprite sheet:** `arma-brocha-impact.png`
**Frames:** 3
**Loop:** No
**Total duration:** 250ms

| Frame | Duration | Description         | Sound Cue                     |
|-------|----------|---------------------|-------------------------------|
| 1     | 60ms     | Impact flash        | `sfx_bullet_impact.ogg` at 0ms |
| 2     | 100ms    | Star expansion      | (continuation)                |
| 3     | 90ms     | Fade with "MITO!"   | (continuation)                |

### Screen Effects (Impact)
- **Screen shake:**
  - Trigger: Frame 1
  - Intensity: 3px
  - Duration: 150ms

- **Hit flash on enemy:**
  - Color: `#FFD700` (gold) at alpha 0.4
  - Duration: 80ms

### Onomatopeia (Impact)
- **"MITO!"** text popup (satirical)
  - Color: `#FFD700` fill, `#8B7500` stroke
  - Size: 14px
  - Duration: 300ms
  - Position: at impact point
  - Animation: scale up, slight rotation, fade

---

## Phaser 3 Animation Keys

```
arma_brocha_idle           -- 3 frames, 500ms cycle, loop
arma_brocha_fire_success   -- 4 frames, 380ms, no loop
arma_brocha_fire_fail      -- 4 frames, 700ms, no loop
arma_brocha_bullet         -- 4 frames, 240ms cycle, loop
arma_brocha_impact         -- 3 frames, 250ms, no loop
arma_brocha_puff           -- 3 frames, 350ms, no loop
arma_brocha_talkei         -- 1 frame (code-animated), 500ms
```

### Branching Logic (Game Code Reference)

```
on_attack():
  roll = random(0.0, 1.0)
  if roll < 0.70:
    play("arma_brocha_fire_success")
    spawn_projectile("arma_brocha_bullet")
  else:
    play("arma_brocha_fire_fail")
    play("arma_brocha_puff")
    show_popup("arma_brocha_talkei")
    apply_self_damage(bolsonaro, BACKFIRE_DAMAGE)
```
