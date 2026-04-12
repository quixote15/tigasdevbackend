# Calculadora Infernal - Animation Specification

## Animation Sets

### 1. FIRING SEQUENCE (Ranged Tax Attack)
**Phaser Animation Key:** `calculadora_fire`
**Frames:** 0, 1, 2, 3
**Total Duration:** 480ms
**Loop:** false
**Y-Sort Priority:** weapon layer (above character)

| Frame | Name              | Duration (ms) | Notes                                    |
|-------|-------------------|---------------|------------------------------------------|
| 0     | static            | 60            | Brief hold before charge                 |
| 1     | fire_charge       | 140           | Buttons light up, display cycles         |
| 2     | fire_calculate    | 140           | All buttons red, number forming          |
| 3     | fire_launch       | 140           | Number launches, recoil                  |

**On Frame 1 (charge):**
- Sound cue: `sfx_calc_beep_sequence` -- rapid calculator button beeps ascending (140ms, 8 quick beeps)
- Particle: Button glow -- red highlights appear on button grid, bottom-to-top sweep (timed across 140ms)
- Particle: 2 orange sparks from cracks (1x1px, speed 40px/s, lifetime 200ms)
- Particle: 2 grey smoke wisps rise from top edge (1x1px, speed 15px/s upward, lifetime 300ms)
- Display effect: Digits cycle animation on last digit position (8 cycles in 140ms)

**On Frame 2 (calculate):**
- Sound cue: `sfx_calc_slam` -- heavy mechanical button SLAM (100ms)
- Sound cue: `sfx_infernal_hum` -- deep demonic hum building (200ms, crescendo)
- Screen effect: Subtle red vignette appears at screen edges (10% opacity, 140ms)
- Particle: Red shockwave from display (ring, 8px to 30px diameter, infernal red, 40% opacity, 200ms)
- Particle: 3 fire particles from cracks (1x1px, orange/yellow, speed 60px/s upward, lifetime 250ms)
- Particle: Ghost number materializing above display (white "%" fading in from 0% to 60% opacity)

**On Frame 3 (launch):**
- Sound cue: `sfx_tax_launch` -- sharp whoosh with cash register "cha-ching" (200ms)
- Sound cue: `sfx_paper_tear` -- receipt paper tearing sound (100ms)
- Screen shake: 3px amplitude, 150ms, exponential decay (recoil)
- Particle: Infernal fire burst from display -- 6 orange/red particles radial (speed 100px/s, lifetime 200ms)
- Particle: 3 ember trails following the launched projectile (1x1px orange, speed matching projectile, lifetime 300ms, fade)
- Particle: Smoke puff at display (4x4px, grey, 30% opacity, 300ms, expand then fade)
- Spawn: Tax number projectile in aim direction (speed 160px/s)
- Damage: Randomize projectile damage tier (1-24% = low/yellow, 25-49% = medium/orange, 50-99% = high/red)

---

### 2. TAX NUMBER PROJECTILE (Flying Numbers)
**Phaser Animation Key:** `calculadora_tax_number`
**Frames:** 4, 5, 6, 5 (loop with flicker)
**Total Duration:** 400ms per cycle
**Loop:** true (while in flight)
**Speed:** 160px/s

| Frame | Name           | Duration (ms) | Notes                              |
|-------|----------------|---------------|------------------------------------|
| 4     | taxnum_launch  | 100           | Initial number form                |
| 5     | taxnum_mid     | 100           | Maximum intensity                  |
| 6     | taxnum_flicker | 100           | Glitch flicker (jerky style)       |
| 5     | taxnum_mid     | 100           | Return to intensity                |

**Continuous particles (while in flight):**
- Receipt trail: Cream paper fragments (2x3px) spawn every 80ms at projectile tail, tumble with slight rotation (lifetime 400ms, gravity 20px/s2, fade)
- Flame trail: Orange 1x1px particles spawn every 60ms, lifetime 200ms, fade
- Smoke: Grey 1x1px every 150ms, speed 10px/s upward, lifetime 300ms
- Sound: `sfx_tax_whistle` -- ominous descending whistle (looping, volume increases with proximity to target)

**On spawn:**
- Sound cue: `sfx_number_born` -- digital chime with infernal undertone (150ms)
- Particle: Number color set based on damage tier (yellow/orange/red shader applied)

**Pre-impact (Frame 7):**
- Played once when within 16px of target
- Duration: 100ms
- Particle: Red impact ring forms (20px diameter, 1px, pulsing)
- The number throbs (scale tween: 1.0 > 1.1 > 0.9 > 1.0, 100ms)

---

### 3. IMPACT (On Hit)
**Phaser Animation Key:** `calculadora_impact`
**Frames:** 8, 9, 10
**Total Duration:** 480ms
**Loop:** false

| Frame | Name             | Duration (ms) | Notes                          |
|-------|------------------|---------------|--------------------------------|
| 8     | taxado_appear    | 130           | Paperwork explosion + text     |
| 9     | taxado_peak      | 200           | Maximum bureaucratic fury      |
| 10    | taxado_fade      | 150           | Scorched receipt remains       |

**On Frame 8:**
- Sound cue: `sfx_taxado` -- aggressive voice shouting "TAXADO!" with cash register sound (500ms)
- Sound cue: `sfx_paper_explosion` -- burst of rustling paper (300ms)
- Screen shake: 5px amplitude, 250ms, exponential decay
- Screen flash: Red, 50ms, 25% opacity
- Particle: Paper explosion -- 10 cream rectangles (2x3px to 4x6px, random sizes) burst radially (speed 120px/s, lifetime 500ms, gravity 30px/s2, slight rotation)
- Particle: Fire burst -- 6 orange/red particles radial (speed 150px/s, lifetime 300ms)
- Particle: "R$" symbol spawns near text (green, 4x4px, static, lifetime 400ms)
- Particle: Red starburst behind text (24px diameter, 100ms, fade)

**On Frame 9:**
- Screen shake: 3px amplitude, 150ms (secondary)
- Particle: Paper fragments burning (add 1px orange pixel to corner of each remaining paper particle)
- Particle: "R$" multiplies -- 2 more spawn, orbit text (orbit radius 20px, speed 240deg/s, lifetime 200ms)
- Particle: Gold coins -- 4 tiny circles (2x2px, gold) fall from above (speed 60px/s downward, lifetime 300ms)
- Particle: Percentage number persists at center (specific % that hit, green calculator font, 200ms then fade)
- Screen flash: Red border, 40ms, 30% opacity
- Slowdown: Game speed 0.8x for 200ms

**On Frame 10:**
- Particle: Paper fragments settle -- remaining pieces flutter downward (speed reduces to 20px/s, gravity increases to 60px/s2)
- Particle: Burn edges on papers intensify (more orange pixels)
- Particle: Coins on ground (static, persist 2000ms then fade 500ms)
- Particle: Scorched receipt decal at center (8x4px, cream with dark burns, persists 4000ms then fades 500ms)
- Particle: 3 grey smoke wisps drift upward (speed 20px/s, lifetime 500ms, fade)
- Sound: Paper rustling fades, fire crackle fades (300ms)

---

### 4. IDLE (Resting)
**Phaser Animation Key:** `calculadora_idle`
**Frames:** 11, 12
**Total Duration:** 1600ms
**Loop:** true (continuous while equipped)

| Frame | Name          | Duration (ms) | Notes                        |
|-------|---------------|---------------|------------------------------|
| 11    | pulse_bright  | 800           | Display brightens, glow up   |
| 12    | pulse_dim     | 800           | Display dims, glow down      |

**Continuous particles (idle):**
- Ember: 1 orange 1x1px drifts from random crack every 1500ms (speed 15px/s upward, lifetime 400ms, fade)
- Smoke: 1 grey 1x1px wisp rises every 2000ms (speed 10px/s, lifetime 500ms, fade from 20% to 0%)
- Sound: `sfx_calc_ambient` -- very faint mechanical hum with occasional single beep, looping (volume 8%)

**Tween behavior:**
- Display brightness: alpha of green text oscillates 0.6 to 1.0 over 800ms, ease sine
- Infernal glow: crack glow alpha oscillates 0.2 to 0.35 over 800ms, ease sine, offset 400ms from display
- Random button flash: Timer triggers every 1200ms, picks random button, flashes red for 200ms then returns to grey
- Receipt paper: Tip position oscillates 1px left/right over 1600ms

---

### 5. SPECIAL - RECEIPT TSUNAMI (Area Attack)
**Phaser Animation Key:** `calculadora_receipt_storm`
**Frames:** 13, 14, 15
**Total Duration:** 900ms
**Loop:** false
**Trigger:** Special attack input (cooldown-based)

| Frame | Name              | Duration (ms) | Notes                           |
|-------|-------------------|---------------|---------------------------------|
| 13    | receipt_build     | 250           | Paper starts flooding           |
| 14    | receipt_vortex    | 300           | Paper vortex forms              |
| 15    | receipt_tsunami   | 350           | Paper wave explodes outward     |

**On Frame 13 (building):**
- Sound cue: `sfx_printer_haywire` -- printer going crazy, rapid paper feeding (500ms, starts here, continues)
- Sound cue: `sfx_infernal_crescendo` -- demonic humming building in intensity (900ms, spans full animation)
- Particle: Receipt streams -- 3 cream paper strips spawn from calculator top, each growing outward (speed 40px/s, curl with sine wave path, width 3px)
- Particle: Tax text appears on strips as they extend ("ICMS", "ISS", "IRPF" stamps, 1px marks)
- Display effect: Digits cycle at maximum speed (blur)
- Button effect: Random buttons flash red rapidly (50ms per flash, 5 flashes during frame)

**On Frame 14 (vortex):**
- Sound cue: `sfx_paper_tornado` -- swirling paper whoosh sound (300ms)
- Particle: Paper strips curve into clockwise spiral pattern (orbit radius expanding from 16px to 32px)
- Particle: "TOTAL" stamps appear on strips (red marks, 2px)
- Particle: Burning edges -- 1-2 orange pixels per strip on leading edges
- Particle: "%" symbols (3, white, 3-4px) spawn and ride the paper spiral (orbit with strips)
- Particle: Fire from calculator cracks -- 4 flame shapes (2x3px, orange/yellow) lick upward
- All buttons RED simultaneously (static hold)
- Screen effect: Subtle rotation of red vignette (5deg oscillation, 150ms period)

**On Frame 15 (tsunami):**
- Sound cue: `sfx_tax_tsunami` -- massive whoosh + explosion + cash register (400ms)
- Screen shake: 8px amplitude, 350ms, exponential decay
- Screen flash: White, 60ms, 35% opacity, then red, 40ms, 20% opacity
- Particle: Paper wave explosion -- ALL receipt strips break into 20+ fragments burst radially (speed 180px/s, lifetime 600ms, gravity 20px/s2)
- Particle: Large "%" symbols (3, red, 6-10px) fly outward at 120deg intervals (speed 140px/s, lifetime 500ms)
- Particle: Tax form fragments (4-6, 4x6px, cream with grid lines) in the wave (speed 150px/s, lifetime 500ms)
- Particle: "R$" in flames (1 instance, gold with orange fire border, speed 100px/s upward, lifetime 400ms)
- Particle: Fire burst from calculator center -- 8 flame particles radial (speed 120px/s, lifetime 300ms)
- Damage: AoE damage in 64px radius around calculator, damage based on how many paper fragments hit
- All enemies in radius: knockback 24px away from calculator center
- Ground decal: Scattered receipt papers remain (6-8, 2x3px cream, persist 5000ms, fade 500ms)

---

## Onomatopoeia Rendering

| Text           | Font Style             | Color      | Shadow     | Size   | Trigger            |
|----------------|------------------------|------------|------------|--------|--------------------|
| "TAXADO!"      | Bold angular comic     | #FF0000    | #1A1A1A    | 24px   | On projectile hit  |
| "99,99%"       | LCD calculator font    | #00FF66    | #00AA44    | 16px   | Always on display  |
| "R$"           | Bold serif             | #00AA44    | #006622    | 10px   | Impact particles   |
| "CALCULANDO..."| LCD scrolling          | #00FF66    | none       | 8px    | During special     |

## Screen Shake Table

| Event              | Amplitude | Duration | Direction     | Easing              |
|--------------------|-----------|----------|---------------|---------------------|
| Projectile launch  | 3px       | 150ms    | Recoil (back) | Exponential decay   |
| Projectile hit     | 5px       | 250ms    | Random        | Exponential decay   |
| Hit secondary      | 3px       | 150ms    | Random        | Linear decay        |
| Receipt tsunami    | 8px       | 350ms    | Radial out    | Exponential decay   |

## Particle System Summary

| Particle          | Sprite      | Count  | Lifetime | Speed     | Gravity  | Alpha     |
|-------------------|-------------|--------|----------|-----------|----------|-----------|
| Receipt fragments | 2-6px cream | 10-20  | 500ms    | 120px/s   | 30px/s2  | 1.0 > 0  |
| Fire burst        | 1-2px org   | 6-8    | 300ms    | 150px/s   | 0        | 0.8 > 0  |
| Embers (idle)     | 1x1 orange  | 1      | 400ms    | 15px/s up | 0        | 0.4 > 0  |
| Smoke wisps       | 1x1 grey    | 1-3    | 500ms    | 10-20px/s | 0        | 0.2 > 0  |
| Receipt trail     | 2x3 cream   | stream | 400ms    | match proj| 20px/s2  | 1.0 > 0  |
| Flame trail       | 1x1 orange  | stream | 200ms    | match proj| 0        | 0.6 > 0  |
| Gold coins        | 2x2 gold    | 3-4    | 300ms    | 60px/s dn | 0        | 1.0 > 0  |
| "R$" symbol       | 4x4 green   | 1-3    | 400ms    | orbit     | 0        | 1.0 > 0  |
| Scorch receipt    | 8x4 cream   | 1      | 4500ms   | 0         | 0        | 0.4 > 0  |
| Tax forms         | 4x6 cream   | 4-6    | 500ms    | 150px/s   | 20px/s2  | 1.0 > 0  |
| "%" symbols       | 3-10px red  | 3      | 500ms    | 140px/s   | 0        | 1.0 > 0  |

## Special Behavior Notes

### Tax Damage Tiers
- Projectile damage scales with the displayed percentage:
  - 1-24%: LOW damage (yellow number, common drop)
  - 25-49%: MEDIUM damage (orange number, less common)
  - 50-99%: HIGH damage (red number, rare but devastating)
  - 99.99%: CRITICAL (always red, rare proc, maximum damage)
- Higher tiers have more dramatic visual effects (larger fire, more particles)
- The number displayed on the projectile corresponds to the damage tier
- Drop rates: 50% low, 30% medium, 15% high, 5% critical

### Receipt Paper Physics
- Receipt strips use Phaser rope/path physics for curling behavior
- Paper fragments have slight rotation on spawn (random angular velocity +/- 90deg/s)
- Paper burns from edges inward (progressive tint change: cream > tan > dark brown > gone)
- Ground receipts can be walked over by all characters (no collision, decoration only)

### Display Animation
- The "99,99%" LCD display uses a custom bitmap font (7-segment style)
- Digit cycling effect: rapidly swap last digit through 0-9 (one swap per 20ms)
- "CALCULANDO..." scrolls right-to-left across display (8 characters visible at once, 50ms per pixel scroll)
- Display green color can intensity-shift via shader (0.6 to 1.0 brightness range)
