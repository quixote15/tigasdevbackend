# Bigode da Justica - Animation Specification

## Animation Sets

### 1. THROW (Boomerang Launch)
**Phaser Animation Key:** `bigode_throw`
**Frames:** 0, 1, 2, 3
**Total Duration:** 440ms
**Loop:** false
**Y-Sort Priority:** weapon layer (above character)

| Frame | Name              | Duration (ms) | Notes                                    |
|-------|-------------------|---------------|------------------------------------------|
| 0     | static            | 60            | Brief hold before detachment             |
| 1     | throw_detach      | 120           | Grotesque rip from face                  |
| 2     | throw_windup      | 130           | Justice aura charges, boomerang forms    |
| 3     | throw_release     | 130           | Spinning launch with patriotic burst     |

**On Frame 1 (detachment):**
- Sound cue: `sfx_mustache_rip` -- wet tearing/ripping sound with a yelp (200ms)
- Particle: Skin fragments -- 3 skin-colored 1x1px particles fly from center base (speed 50px/s, lifetime 300ms, gravity 40px/s2)
- Particle: Golden flash -- 4x4px justice gold burst at detachment point (100ms, fade)
- Screen shake: 2px amplitude, 80ms (pain shake)
- Eneas face: If visible, upper lip exposed (pink, vulnerable -- separate sprite overlay)

**On Frame 2 (wind-up):**
- Sound cue: `sfx_justice_charge` -- ascending harmonic tone, like a sword being drawn but hairier (200ms)
- Particle: Golden justice aura -- 3px glow around mustache (justice gold, 40% opacity, pulses)
- Particle: 3 gold sparkles at mustache tips (1x1px, spawn staggered over 130ms, lifetime 150ms)
- Particle: Wind spiral -- white 1px dots trace a spiral path around mustache (4 dots, 60deg apart, orbit radius 16px, speed 540deg/s)
- Sound: Subtle wind whoosh building (100ms, crescendo)

**On Frame 3 (release):**
- Sound cue: `sfx_bigode_launch` -- sharp whoosh with a "SHING" metallic cutting sound (200ms)
- Sound cue: `sfx_patriotic_burst` -- short brass fanfare note (150ms)
- Screen shake: 3px amplitude, 120ms, in launch direction
- Particle: Patriotic burst -- 2 green + 2 yellow + 1 blue 1x1px particles (Brazilian flag colors, speed 80px/s radial, lifetime 350ms)
- Particle: Golden arc trails from tips (2 trails, 1px gold, 8px long, 200ms, fade)
- Particle: Gold shockwave ring (24px diameter, 1px, 200ms, fade from 40% to 0%)
- Particle: 3 white wind circles around launch path (1px, 150ms, fade)
- Spawn: Bigode projectile in aim direction (speed 180px/s, returns after 400ms or hitting target)

---

### 2. SPINNING MUSTACHE PROJECTILE (Boomerang Flight)
**Phaser Animation Key:** `bigode_spin`
**Frames:** 4, 5, 6, 7
**Total Duration:** 320ms per full rotation
**Loop:** true (while in flight)
**Speed:** 180px/s outbound, 140px/s return
**Trajectory:** Boomerang arc (Phaser curved path, outbound 200px then curves back)

| Frame | Name           | Duration (ms) | Notes                              |
|-------|----------------|---------------|------------------------------------|
| 4     | spin_0deg      | 80            | Horizontal                         |
| 5     | spin_90deg     | 80            | Vertical                           |
| 6     | spin_180deg    | 80            | Horizontal flipped                 |
| 7     | spin_270deg    | 80            | Vertical flipped                   |

**Continuous particles (while in flight):**
- Golden aura trail: Justice gold 1x1px particles spawn every 40ms at mustache edges, lifetime 250ms, fade from 50% to 0%
- Blood drops: Red 1x1px, spawn every 120ms at tips, lifetime 200ms, slight gravity 20px/s2
- Wind trail: White 1px dots trace the curved boomerang path behind (spawn every 60ms, lifetime 300ms, static position once spawned)
- Sound: `sfx_bigode_whoosh_loop` -- rhythmic spinning whoosh, 80ms cycle matching rotation, looping

**On each rotation (every 320ms):**
- Particle: Patriotic sparkle -- 1 particle of random Brazilian flag color (green/yellow/blue), spawns at center, drifts outward (speed 30px/s, lifetime 200ms)

**Damage behavior:**
- Damages ALL enemies in the flight path (piercing -- does not stop on hit)
- Can hit the same enemy on outbound AND return paths (double hit potential)
- Hitbox: 28px wide on horizontal frames, 10px wide on vertical frames (alternating, reflects visual shape)

**Boomerang trajectory:**
- Phase 1 (outbound): Straight line in aim direction, 200px, 180px/s
- Phase 2 (curve): 90deg arc turn, 100px radius, decelerating to 140px/s
- Phase 3 (return): Curved path back to Eneas' position, 140px/s, homing
- Total flight time: ~800ms (variable based on distance)

---

### 3. IMPACT (On Hit -- plays at EACH enemy hit during flight)
**Phaser Animation Key:** `bigode_impact`
**Frames:** 8, 9, 10
**Total Duration:** 420ms
**Loop:** false
**Note:** Does NOT stop the projectile -- impact animation plays at hit location while mustache continues flight

| Frame | Name             | Duration (ms) | Notes                          |
|-------|------------------|---------------|--------------------------------|
| 8     | justica_appear   | 110           | Cut line + text appears        |
| 9     | justica_peak     | 180           | Maximum justice                |
| 10    | justica_fade     | 130           | Dignified dissipation          |

**On Frame 8:**
- Sound cue: `sfx_justica_shout` -- Eneas' voice, POWERFUL and AUTHORITATIVE, shouting "JUSTICA!" (600ms, clear, not distorted)
- Sound cue: `sfx_blade_cut` -- sharp cutting sound (100ms)
- Screen shake: 5px amplitude, 200ms, perpendicular to flight path
- Particle: Cut line -- 2px wide red line, 40px long, horizontal across hit point (appears instantly, fades over 400ms from bright red to dark red)
- Particle: Hair debris -- 8 black 1x2px fragments burst radially (speed 100px/s, lifetime 400ms, gravity 30px/s2)
- Particle: Blood splatter -- 5 red 1-2px dots scatter near cut line (speed 80px/s, lifetime 350ms, gravity 40px/s2)
- Particle: Patriotic burst -- 5 particles (2 green, 2 yellow, 1 blue, 1x1px, speed 60px/s radial, lifetime 300ms)
- Particle: Golden starburst -- 24px, justice gold, 150ms, fade

**On Frame 9:**
- Screen flash: Gold, 40ms, 25% opacity
- Particle: 2 additional cut lines at angles (crossing original, creating triple slash, same fade behavior)
- Particle: Raised fist silhouette (4x6px, dark, 30% opacity, 200ms at center behind text, then fade)
- Slowdown: Game speed 0.75x for 180ms (dramatic justice impact)
- Particle: Gold starburst intensifies -- adds patriotic colored rays (alternating green/yellow/gold, 32px diameter)

**On Frame 10:**
- Particle: Golden star mark -- 8x8px gold star persists at hit center (lifetime 2000ms, then fades 500ms) -- "mark of justice" ground decal
- All cut lines shift from bright red to dark red (drying blood)
- Hair debris settles to ground
- Blood splatter persists as ground decal (lifetime 3000ms, then fade 500ms)
- Sound: `sfx_justice_echo` -- reverberating authoritative echo (400ms, volume 40%)

---

### 4. IDLE (Resting on Face)
**Phaser Animation Key:** `bigode_idle`
**Frames:** 11, 12
**Total Duration:** 1800ms
**Loop:** true (continuous while weapon equipped and mustache is attached)

| Frame | Name          | Duration (ms) | Notes                        |
|-------|---------------|---------------|------------------------------|
| 11    | bristle_left  | 900           | Hair flexes left             |
| 12    | bristle_right | 900           | Hair flexes right            |

**Continuous effects (idle):**
- Golden aura: Very subtle 1px justice gold outline at 15% opacity, constant
- Sound: `sfx_bigode_ambient` -- almost inaudible low hum of justice, looping (volume 5%)

**Tween behavior:**
- Hair strand positions at edges: interpolate between left-lean and right-lean positions (smooth sine, not jerky -- the idle is DIGNIFIED)
- Tip curl tightness: subtle oscillation in tip position (1px range, 900ms, ease sine)
- Grey streak highlight: single bright pixel alternates position between strands (every 900ms, coincides with frame change)

**While mustache is in flight (Frames 4-7 active):**
- Idle animation does NOT play
- Instead: Eneas' face shows exposed upper lip (separate sprite overlay, pink, static)
- Eneas receives a "vulnerable" visual state (no mustache = no dignity)
- Optional: Sweat drop on Eneas' face while mustache is away (anxiety about his weapon returning)

---

### 5. BOOMERANG RETURN (Mustache Coming Home)
**Phaser Animation Key:** `bigode_return`
**Frames:** 13, 14, 15
**Total Duration:** 450ms
**Loop:** false
**Trigger:** When projectile completes its return arc and reaches Eneas' position

| Frame | Name              | Duration (ms) | Notes                           |
|-------|-------------------|---------------|---------------------------------|
| 13    | return_incoming   | 150           | Mustache approaching with trail |
| 14    | return_approach   | 150           | Decelerating, threads reaching  |
| 15    | return_reattach   | 150           | SNAP! Back on face              |

**On Frame 13 (incoming):**
- Sound cue: `sfx_bigode_incoming` -- reverse whoosh, approaching (200ms, crescendo)
- Particle: Golden comet tail -- justice gold trail (3px wide, 12px long, attached to mustache, fading from 60% to 10%)
- Particle: Debris trail -- 3-4 dark 1x1px particles trailing behind (enemy hair/matter from the cuts, lifetime 300ms)
- Particle: 1 patriotic yellow sparkle in trail (1x1px, lifetime 200ms)
- The projectile spin animation continues but slows (Frames 4-7 at 400ms per rotation instead of 320ms)

**On Frame 14 (approach):**
- Sound cue: `sfx_magnetic_pull` -- subtle magnetic hum (150ms)
- Particle: Golden threads -- 3 thin gold lines (1px) extend from mustache center toward Eneas' face position (magnetic attraction visual, grow from 0px to 8px over 150ms)
- Projectile spin stops -- mustache settles to near-horizontal (15deg tilt)
- Particle: Comet tail shortens (6px)
- Blood on tips transitions: bright red to dark red (drying during return)

**On Frame 15 (reattachment):**
- Sound cue: `sfx_bigode_snap` -- satisfying magnetic SNAP/click (100ms)
- Sound cue: `sfx_justice_restored` -- brief brass note, resolving chord (200ms)
- Screen flash: Gold, 30ms, 15% opacity (subtle victorious flash)
- Particle: Gold flash at connection point (6x4px, justice gold, 80ms, fade)
- Particle: Gold shockwave ring from connection (16px diameter, 1px, 200ms, fade from 40% to 0%)
- Particle: 3 gold sparkles pop at base (1x1px, speed 40px/s upward, lifetime 200ms)
- Particle: Patriotic flash -- 1 green + 1 yellow + 1 blue 1x1px at base (100ms, fade)
- Blood absorption: Any remaining blood on tips fades to 0% (100ms) -- justice purifies
- Mustache state: Returns to idle animation (Frames 11-12)
- Eneas state: Exposed lip overlay removed, normal face restored
- Weapon ready: Can throw again immediately after reattachment

---

## Onomatopoeia Rendering

| Text        | Font Style                | Color      | Shadow     | Size   | Trigger          |
|-------------|---------------------------|------------|------------|--------|------------------|
| "JUSTICA!"  | Bold authoritative serif  | #FFD700    | #002776    | 24px   | On each hit      |
| "SNAP!"     | Sharp mechanical          | #FFD700    | #1A1A1A    | 12px   | On reattachment  |
| "SHING!"    | Italic cutting font       | #C0C0C0    | #404040    | 14px   | On throw (opt.)  |

**Important note on "JUSTICA!" text style:**
Unlike ALL other weapons in the game whose onomatopoeias are shaky, wobbly, and uneven, Eneas' "JUSTICA!" must be BOLD, STABLE, and AUTHORITATIVE. The letters do NOT shake. They are planted with CONVICTION. This visual contrast with every other weapon's text is deliberate and defines Eneas' character.

## Screen Shake Table

| Event              | Amplitude | Duration | Direction              | Easing              |
|--------------------|-----------|----------|------------------------|---------------------|
| Face detachment    | 2px       | 80ms     | Up (pain)              | Linear              |
| Throw release      | 3px       | 120ms    | Launch direction       | Exponential decay   |
| Each enemy hit     | 5px       | 200ms    | Perpendicular to path  | Exponential decay   |
| Reattachment       | 1px       | 50ms     | Down (snap)            | Linear              |

## Particle System Summary

| Particle           | Sprite       | Count  | Lifetime | Speed     | Gravity  | Alpha     |
|--------------------|--------------|--------|----------|-----------|----------|-----------|
| Skin fragments     | 1x1 skin     | 3      | 300ms    | 50px/s    | 40px/s2  | 0.8 > 0  |
| Golden aura trail  | 1x1 gold     | stream | 250ms    | 0         | 0        | 0.5 > 0  |
| Blood drops        | 1x1 red      | stream | 200ms    | trailing  | 20px/s2  | 0.8 > 0  |
| Wind trail dots    | 1px white    | stream | 300ms    | 0 (static)| 0        | 0.3 > 0  |
| Patriotic sparkles | 1x1 G/Y/B   | 5      | 300ms    | 60-80px/s | 0        | 1.0 > 0  |
| Hair debris        | 1x2 black    | 8      | 400ms    | 100px/s   | 30px/s2  | 1.0 > 0  |
| Blood splatter     | 1-2px red    | 5      | 350ms    | 80px/s    | 40px/s2  | 0.8 > 0  |
| Cut line           | 2px red line | 1-3    | 400ms    | 0         | 0        | 1.0 > 0  |
| Gold starburst     | radial gold  | 1      | 150ms    | expand    | 0        | 0.6 > 0  |
| Justice star mark  | 8x8 gold     | 1      | 2500ms   | 0         | 0        | 0.4 > 0  |
| Golden threads     | 1px gold     | 3      | 150ms    | 0 (grow)  | 0        | 0.4 > 0.6|
| Snap flash         | 6x4 gold     | 1      | 80ms     | 0         | 0        | 1.0 > 0  |
| Comet tail         | 3px gold     | 1      | continuous| match proj| 0        | 0.6 > 0.1|

## Special Behavior Notes

### Boomerang Mechanics
- The mustache ALWAYS returns to Eneas, regardless of what happens during flight
- If Eneas moves while the mustache is in flight, the return trajectory adjusts (homing)
- The mustache can hit enemies on both outbound and return paths (double damage potential)
- Flight path: straight outbound (200px) -> 90deg arc turn -> curved return to Eneas
- Total flight time: ~800ms (cannot throw again until reattachment completes)
- The mustache pierces through enemies (does NOT stop on hit -- continues flight path)
- Each enemy can be hit ONCE per pass direction (once outbound, once on return)

### Eneas Without Mustache State
- While the mustache is in flight, Eneas' character sprite should show his bare upper lip
- This is a vulnerable state both visually and thematically (Eneas is INCOMPLETE without his mustache)
- Optional: Eneas takes 10% more damage while mustache is away (risk/reward for using the weapon)
- The exposed lip should look WRONG -- pink, naked, disturbing (the absence is the horror)
- This creates urgency for the boomerang to return quickly

### Justice Aura Scaling
- The golden aura intensity scales with consecutive hits:
  - 0 hits: 15% opacity (idle)
  - 1 hit: 30% opacity
  - 2 hits: 45% opacity
  - 3+ hits: 60% opacity (maximum justice)
- Aura decays back to idle over 5 seconds without hitting
- At maximum justice, the mustache deals 25% bonus damage
- Visual feedback: the brighter the aura, the more powerful the next throw
