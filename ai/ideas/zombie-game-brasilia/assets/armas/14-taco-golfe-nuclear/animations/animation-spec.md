# Taco de Golfe Nuclear - Animation Specification

## Animation Sets

### 1. SWING (Golf Swing Attack)
**Phaser Animation Key:** `golfe_swing`
**Frames:** 0, 1, 2, 3, 4
**Total Duration:** 550ms
**Loop:** false
**Y-Sort Priority:** weapon layer (above character)

| Frame | Name              | Duration (ms) | Notes                                    |
|-------|-------------------|---------------|------------------------------------------|
| 0     | static            | 80            | Brief hold before backswing              |
| 1     | swing_backswing   | 140           | Slow deliberate wind-up                  |
| 2     | swing_downswing   | 80            | FAST -- maximum velocity                 |
| 3     | swing_contact     | 120           | Impact explosion, spawn projectile       |
| 4     | swing_followthrough| 130           | Victory pose recovery                    |

**On Frame 1 (backswing):**
- Sound cue: `sfx_golf_windup` -- metallic whoosh ascending (180ms)
- Particle: 3-4 gold sparkle pixels flash on club head (1x1px, lifetime 100ms each, staggered spawn)
- Particle: Nuclear green glow pulse (club head, radius 6px to 8px, 140ms)
- Golf ball appears at tee position (16px below club, static)

**On Frame 2 (downswing):**
- Sound cue: `sfx_golf_whoosh` -- heavy metallic whoosh with nuclear hum undertone (120ms)
- Particle: Nuclear green trail -- 5 green pixels spawn along swing arc (lifetime 200ms, fade from 60% to 0%)
- Particle: Dollar sign ($) particles -- 2 gold, 2px each, scatter from club path (speed 60px/s, lifetime 300ms)
- Particle: Gold motion streaks -- 3 lines along swing arc (1px, gold, 150ms, fade out)

**On Frame 3 (contact):**
- Sound cue: `sfx_golf_hit` -- EXPLOSIVE metallic crack with nuclear bass rumble (500ms)
- Screen shake: HEAVY -- 7px amplitude, 350ms, decreasing
- Screen flash: Gold flash, 60ms, 35% opacity
- Particle: Nuclear burst -- green-gold starburst, 8 rays from contact (20px length, 2px wide, 300ms)
- Particle: Gold fragments -- 5 sparkle pieces fly radially (speed 150px/s, lifetime 350ms, fade)
- Particle: Dollar bills -- 3 tiny "$" symbols erupt upward (speed 80px/s, lifetime 500ms, gravity 30px/s2)
- Particle: Green energy ring -- expanding circle (8px to 40px diameter, 250ms, green, fade from 50% to 0%)
- Spawn: Trump Ball projectile launched in aim direction (speed 200px/s)
- Damage: Melee damage applied at contact if enemy in range

**On Frame 4 (follow-through):**
- Particle: Green smoke puff at tee position (4x4px, nuclear green, 40% opacity, 400ms, expand then fade)
- Particle: 2 residual gold sparkles drift (speed 20px/s, lifetime 300ms)
- Sound cue: `sfx_golf_echo` -- reverberating metallic ring (400ms, volume 30%)

---

### 2. TRUMP BALL PROJECTILE (Explosive Golf Ball)
**Phaser Animation Key:** `golfe_trump_ball`
**Frames:** 5, 6, 7, 6 (loop with wobble)
**Total Duration:** 400ms per cycle
**Loop:** true (while in flight)
**Speed:** 200px/s

| Frame | Name           | Duration (ms) | Notes                              |
|-------|----------------|---------------|------------------------------------|
| 5     | ball_launch    | 100           | Initial flight, face forward       |
| 6     | ball_midflight | 100           | Spinning, face sideways            |
| 7     | ball_wobble    | 100           | Erratic wobble (jerky style)       |
| 6     | ball_midflight | 100           | Return to spin before loop         |

**Continuous particles (while in flight):**
- Nuclear trail: Green pixels, spawn every 50ms at ball tail, 1x1px, lifetime 250ms, fade out
- Dollar wake: Gold "$" pixel, spawn every 200ms, 1x1px, lifetime 300ms, drift downward
- Sound: `sfx_nuclear_hum` -- ominous low hum, looping, volume increases as ball travels

**On spawn:**
- Sound cue: `sfx_ball_launch` -- sharp "thwock" with ascending whistle (300ms)
- Camera: 2px nudge in launch direction (60ms)

**Pre-impact (Frame 8):**
- Played once when projectile is within 12px of target
- Duration: 80ms
- Sound cue: `sfx_nuclear_warning` -- brief alarm beep (80ms)
- Particle: Red warning ring (16px, 1px, flashes twice in 80ms)

---

### 3. IMPACT - HIT ("TREMENDOUS!")
**Phaser Animation Key:** `golfe_hit_tremendous`
**Frames:** 9, 10, 11
**Total Duration:** 550ms
**Loop:** false
**Trigger:** Projectile hits enemy

| Frame | Name               | Duration (ms) | Notes                          |
|-------|--------------------|---------------|--------------------------------|
| 9     | tremendous_appear  | 150           | Fireball + text materializes   |
| 10    | tremendous_peak    | 220           | Maximum explosion, hold longer |
| 11    | tremendous_fade    | 180           | Mushroom cloud dissipates      |

**On Frame 9:**
- Sound cue: `sfx_tremendous` -- Trump-like voice shouting "TREMENDOUS!" (distorted, echoed, 600ms)
- Sound cue: `sfx_nuclear_explosion` -- deep bass explosion (800ms)
- Screen shake: 8px amplitude, 400ms, exponential decay
- Screen flash: Orange, 100ms, 50% opacity
- Particle: Fireball -- expanding orange-red circle (start 8px, peak 36px, 300ms)
- Particle: Ball fragments -- 6 white 1x1px pieces fly radially (speed 180px/s, lifetime 400ms)
- Particle: Fire particles -- 8 orange/red 2x2px, radial burst (speed 100px/s, lifetime 500ms, fade)
- Particle: Radiation green sparkles -- 4 green 1x1px in explosion (lifetime 350ms)

**On Frame 10:**
- Screen shake: 5px amplitude, 200ms (secondary shake)
- Screen flash: Red, 40ms, 25% opacity
- Particle: Mushroom cloud stem + cap (formed from particle group, orange gradient, holds 220ms then dissipates)
- Particle: Dollar rain -- 4 gold "$" symbols (2px) fall from explosion top (speed 50px/s downward, lifetime 400ms)
- Particle: Radiation symbol -- brief green 3-wedge icon at cloud center (6x6px, 150ms, fade)
- Slowdown: Game speed 0.7x for 220ms (dramatic impact feel)

**On Frame 11:**
- Particle: Smoke wisps -- 4 grey 2x2px drift upward (speed 25px/s, lifetime 500ms, fade from 40% to 0%)
- Particle: Green residue circle at ground (16px diameter, nuclear green, 30% opacity, persists 3000ms then fades 500ms)
- Particle: Scorch mark -- dark circle (8px) at center, persists 5000ms
- Sound: Explosion reverb tail continues, crackling fire fades (500ms)

---

### 4. IMPACT - MISS ("FAKE NEWS!")
**Phaser Animation Key:** `golfe_miss_fakenews`
**Frames:** 12, 13, 14
**Total Duration:** 500ms
**Loop:** false
**Trigger:** Projectile hits ground/wall without hitting enemy

| Frame | Name              | Duration (ms) | Notes                          |
|-------|-------------------|---------------|--------------------------------|
| 12    | fakenews_appear   | 140           | Pathetic poof + angry text     |
| 13    | fakenews_peak     | 200           | Maximum indignation            |
| 14    | fakenews_fade     | 160           | Sad aftermath                  |

**On Frame 12:**
- Sound cue: `sfx_fake_news` -- Trump-like voice shouting "FAKE NEWS!" (angry, clipped, 500ms)
- Sound cue: `sfx_golf_dud` -- pathetic thud (150ms)
- Screen shake: 2px amplitude, 100ms (deliberately weak compared to hit)
- Particle: Dirt poof -- 5 brown 2x2px particles, weak radial burst (speed 40px/s, lifetime 300ms, gravity 60px/s2)
- Spawn: Tiny American flag at miss point (4x3px sprite, plants vertically)
- Spawn: Trump face fragment on ground (3x3px, scowling, static decal)

**On Frame 13:**
- Particle: Tumbleweed (2x2px, brown) rolls across from left to right (speed 30px/s, lifetime 600ms)
- Sound cue: `sfx_sad` -- quiet deflated voice "Sad..." (300ms, low volume)
- "SAD!" text spawns below main "FAKE NEWS!" text (gold, smaller)
- Flag waves: tiny flag oscillates +/- 5deg (200ms cycle)

**On Frame 14:**
- Flag falls: tilts to 45deg over 160ms
- Particle: Final dust settles (2 brown 1x1px, fall to ground, 160ms)
- Crack decal: 4px dark line at impact point, persists 3000ms
- Trump face fragment persists 2000ms then fades over 500ms
- All text fades to 0% opacity

---

### 5. IDLE (Resting)
**Phaser Animation Key:** `golfe_idle`
**Frames:** 15 (single frame, tweened)
**Total Duration:** continuous
**Loop:** true (tween-based)

**Tween behavior (applied to Frame 15):**
- Sparkle travel: A highlight point (1x1px white) traverses the club head surface in an arc over 1200ms, loops
- Nuclear pulse: Green glow alpha oscillates between 0.2 and 0.4 over 800ms, ease sine, yoyo true
- Diamond twinkle: 3 diamond highlight points, each toggles between bright (1.0) and dim (0.6) alpha on staggered 400ms timers
- Shaft gleam: 1px white line moves from grip to head over 1600ms, loops with 400ms delay

**Continuous particles (idle):**
- Gold sparkle: 1 sparkle spawns every 800ms at random position on club head, 1x1px white>gold, lifetime 300ms
- Sound: `sfx_gold_shimmer` -- very faint metallic shimmer, looping (volume 8%)

---

## Onomatopoeia Rendering

| Text          | Font Style            | Color      | Shadow   | Size   | Trigger     |
|---------------|-----------------------|------------|----------|--------|-------------|
| "TREMENDOUS!" | Bold chunky comic     | #FF0000    | #FFD700  | 24px   | On hit      |
| "FAKE NEWS!"  | Jagged angry letters  | #0040FF    | #FFFFFF  | 22px   | On miss     |
| "SAD!"        | Small deflated serif  | #FFD700    | #A07D14  | 12px   | On miss +200ms |
| "FORE!"       | Bold italic           | #FFD700    | #1A1A1A  | 16px   | On swing (optional) |

## Screen Shake Table

| Event              | Amplitude | Duration | Direction        | Easing              |
|--------------------|-----------|----------|------------------|---------------------|
| Golf swing contact | 7px       | 350ms    | Swing direction  | Exponential decay   |
| Hit explosion      | 8px       | 400ms    | Random           | Exponential decay   |
| Hit secondary      | 5px       | 200ms    | Random           | Linear decay        |
| Miss (pathetic)    | 2px       | 100ms    | Down             | Linear decay        |

## Particle System Summary

| Particle          | Sprite       | Count  | Lifetime | Speed     | Gravity  | Alpha     |
|-------------------|--------------|--------|----------|-----------|----------|-----------|
| Nuclear trail     | 1x1 green    | stream | 250ms    | 0         | 0        | 0.6 > 0  |
| Gold sparkles     | 1x1 gold     | 5      | 350ms    | 150px/s   | 0        | 1.0 > 0  |
| Dollar signs      | 2px gold "$" | 3-4    | 500ms    | 80px/s    | 30px/s2  | 1.0 > 0  |
| Green burst rays  | 2px green    | 8      | 300ms    | expand    | 0        | 0.5 > 0  |
| Fireball          | circle org   | 1      | 300ms    | expand    | 0        | 0.8 > 0  |
| Ball fragments    | 1x1 white    | 6      | 400ms    | 180px/s   | 0        | 1.0 > 0  |
| Mushroom cloud    | composite    | 1      | 420ms    | 0         | 0        | 0.7 > 0  |
| Dirt poof (miss)  | 2x2 brown    | 5      | 300ms    | 40px/s    | 60px/s2  | 0.6 > 0  |
| Tumbleweed        | 2x2 brown    | 1      | 600ms    | 30px/s    | 0        | 0.5      |
| Green residue     | circle green | 1      | 3500ms   | 0         | 0        | 0.3 > 0  |
| Scorch mark       | circle dark  | 1      | 5000ms   | 0         | 0        | 0.4 > 0  |

## Special Behavior Notes

### Hit vs Miss System
- The game must detect if the projectile hits an enemy (HIT) or misses (MISS)
- HIT triggers the `golfe_hit_tremendous` animation with massive explosion
- MISS triggers the `golfe_miss_fakenews` animation with pathetic failure
- The CONTRAST between the two is the primary comedic mechanic
- Hit explosion should feel 10x more powerful than miss poof
- Screen shake on hit should be 4x stronger than on miss
