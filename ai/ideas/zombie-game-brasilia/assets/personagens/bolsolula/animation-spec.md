# BOLSOLULA (Fusao) — Animation Specification

## Overview
- **Engine:** Phaser 3
- **Sprite Size:** 96x96px
- **Base Frame Rate:** 8-12 fps (jerky Andre Guedes style — intentionally NOT smooth)
- **Perspective:** Top-down slightly isometric (Y-sorting)
- **Easing:** NONE for base animations. The jerkiness IS the style. Easing only on specific effects noted below.
- **Global Rule:** Every animation must feel like stop-motion paper cutouts animated by someone who is angry.

---

## 1. IDLE — `bolsolula_idle`

| Property | Value |
|---|---|
| Frames | 4 |
| Frame Rate | 8 fps |
| Loop | Yes |
| Duration per cycle | 500ms |
| Phaser key | `bolsolula_idle` |

### Timing Breakdown

| Frame | Duration | Description | Easing |
|---|---|---|---|
| 0 (Lula dominant) | 125ms | Lula side puffed, Bolso slumped | None (snap) |
| 1 (Bolso dominant) | 125ms | Bolso side puffed, Lula slumped | None (snap) |
| 2 (Argument) | 125ms | Both faces turned inward, screaming | None (snap) |
| 3 (Confusion) | 125ms | Both faces bewildered, arms limp | None (snap) |

### Side-Dominance System
- Every 5000ms (5 seconds), fire a `dominanceSwitchEvent`
- On switch: play a 200ms transition flash (seam glows `#F0C830` at 40% opacity)
- Lula Dominant: idle loops starting from frame 0
- Bolso Dominant: idle loops starting from frame 1
- The argument frame (2) plays at EVERY switch as a 1-frame interjection

### Particle Effects — Idle
| Particle | Emitter Config | Trigger |
|---|---|---|
| Fusion seam sparks | 1-2 particles/sec, `#F0C830`, 1x1px, lifespan 300ms, gravity 0, speed 10px/s radial, alpha fade 1.0->0.0 | Continuous during idle |
| Green gas wisps | 1 particle/2sec, `#4A7C59` at 30% alpha, 3x3px, lifespan 800ms, speed 5px/s upward, scale 1.0->0.5 | Continuous — seeps from fusion seam |
| Question mark (frame 3) | Static sprite, `#F0E8D8`, 6x6px, appears y-12px above head, alpha 0.0->1.0->0.0 over 400ms | Only during frame 3 |

### Sound Triggers — Idle
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Seam creak | `sfx_bolsolula_creak.ogg` | Every 2nd idle cycle | 0.3 |
| Dual mumble | `sfx_bolsolula_mumble.ogg` | Random, 15% chance per cycle | 0.4 |
| Bordao random | See `bolsolula-bordoes.md` | Every 15s while idle | 0.6 |

---

## 2. WALK — `bolsolula_walk`

| Property | Value |
|---|---|
| Frames | 6 |
| Frame Rate | 10 fps |
| Loop | Yes |
| Duration per cycle | 600ms |
| Phaser key | `bolsolula_walk` |

### Timing Breakdown

| Frame | Duration | Description | Notes |
|---|---|---|---|
| 0 (Left step) | 100ms | Lula leg forward, lean left | Normal timing |
| 1 (Weight left) | 100ms | Squash on left | Normal timing |
| 2 (Mid transition) | 100ms | Both legs even, bolt sparks | Normal timing |
| 3 (Right step) | 100ms | Bolso leg forward, lean right | Normal timing |
| 4 (Weight right) | 100ms | Squash on right | Normal timing |
| 5 (Stumble) | 150ms | Trip, all arms flail | **HELD LONGER** for comedy beat — 1.5x duration |

### Movement System
```javascript
// Walk speed: 60% of normal character speed (the monster is clumsy)
const BOLSOLULA_WALK_SPEED = 80; // pixels per second (vs normal 130)

// Walk wobble: body oscillates 2px left-right per step
// Implement as sinusoidal offset on x position:
// offset_x = Math.sin(walkCycleProgress * Math.PI * 2) * 2;

// Every 6th step cycle, play the stumble (frame 5) with extended hold
// Random chance (20%) to fully trip — play hit animation instead
```

### Particle Effects — Walk
| Particle | Emitter Config | Trigger |
|---|---|---|
| Dust puffs | 2-3 particles per step, `#C4A265` (grama morta), 2x2px, lifespan 400ms, gravity 20px/s, speed 15px/s radial, alpha 0.6->0.0 | On frames 0 and 3 (foot contact) |
| Stitch thread | 1 particle on stumble, `#1A1A18`, 1x4px line, lifespan 600ms, gravity 40px/s, speed 20px/s random direction | Frame 5 only |
| Bolt spark | 1 particle, `#F0C830`, 1x1px, lifespan 150ms, speed 0, alpha flash 1.0->0.0 | Frame 2 (transition spark) |

### Sound Triggers — Walk
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Footstep mismatched | `sfx_bolsolula_step_L.ogg` + `sfx_bolsolula_step_R.ogg` | Frame 0 (shoe) and Frame 3 (boot) — different sounds per foot | 0.4 |
| Seam stretch | `sfx_bolsolula_stretch.ogg` | Frame 5 (stumble) | 0.3 |
| Stumble grunt (dual) | `sfx_bolsolula_stumble.ogg` | Frame 5, 20% chance | 0.5 |

---

## 3. ATTACK — `bolsolula_attack`

| Property | Value |
|---|---|
| Frames | 3 |
| Frame Rate | 10 fps |
| Loop | No |
| Duration | 300ms |
| Phaser key | `bolsolula_attack` |
| Callback | On frame 1 complete: spawn `emenda_projectile` |

### Timing Breakdown

| Frame | Duration | Description | Easing |
|---|---|---|---|
| 0 (Windup) | 120ms | Pull back, compress body, pen glows | **Slight ease-in** (rare exception) — slow start for anticipation |
| 1 (Strike) | 80ms | SLAM forward, maximum stretch, starburst | **Instant** — snap to full extension |
| 2 (Follow-through) | 100ms | Arms extended, emenda flies, satisfaction | None |

### Attack Hitbox
```javascript
// Hitbox appears on Frame 1 ONLY
// Shape: arc in front of character, 120-degree sweep
// Range: 48px from center (half a tile beyond body edge)
// Damage: base 25 HP
// Knockback: 16px in hit direction
hitbox = {
  type: 'arc',
  angle: 120,
  radius: 48,
  offset: { x: 0, y: -16 }, // slightly forward
  activeFrame: 1,
  damage: 25,
  knockback: 16
};
```

### Projectile — Emenda Parlamentar Explosiva
```javascript
// Spawns at pen tip position on frame 1
// Travels in attack direction
emendaProjectile = {
  sprite: 'emenda_paper',
  size: { w: 8, h: 8 },
  speed: 120, // px/sec
  lifespan: 1500, // ms
  gravity: 30, // slight arc downward
  onExpire: 'explode', // AoE explosion
  explosionRadius: 24,
  explosionDamage: 15,
  explosionSprite: 'emenda_explosion', // gold starburst + paper confetti
  trailParticles: {
    type: 'ink_drip',
    colors: ['#8B1A1A', '#2E5A1C'], // alternating red/green ink
    rate: 8, // particles/sec
    size: 1,
    lifespan: 300
  }
};
```

### Particle Effects — Attack
| Particle | Emitter Config | Trigger |
|---|---|---|
| Pen glow (windup) | Aura around pen, `#CC2020` left + `#2E5A1C` right, 2px radius, pulsing alpha 0.2->0.6 at 10Hz | Frame 0 |
| Starburst (impact) | 8-ray star, `#F0C830`, 8x8px center, rays extend 12px, lifespan 150ms, alpha 1.0->0.0 | Frame 1 |
| Ink splatter | 4-6 particles, alternating `#8B1A1A` and `#2E5A1C`, 1x1px, speed 40px/s radial, lifespan 300ms | Frame 1 |
| Paper scraps | 2-3 particles, `#E8D8B0`, 2x2px, gravity 60px/s, rotation random, lifespan 500ms | Frame 2 |

### Sound Triggers — Attack
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Pen whoosh | `sfx_bolsolula_pen_whoosh.ogg` | Frame 0->1 transition | 0.6 |
| Dual scream | `sfx_bolsolula_dual_scream.ogg` | Frame 1 | 0.7 |
| Paper sign | `sfx_bolsolula_sign.ogg` | Frame 1 (pen scribble sound) | 0.4 |
| Emenda explosion | `sfx_emenda_explode.ogg` | On projectile expire | 0.6 |

### Screen Effects — Attack
| Effect | Trigger | Duration |
|---|---|---|
| Camera micro-shake | Frame 1 | 50ms, magnitude 2px |

---

## 4. DEATH — `bolsolula_death`

| Property | Value |
|---|---|
| Frames | 4 |
| Frame Rate | 6 fps (SLOW — dramatic) |
| Loop | No |
| Duration | 667ms |
| Phaser key | `bolsolula_death` |
| Post-animation | Hold frame 3 for 2000ms, then fade alpha 1.0->0.0 over 1000ms |

### Timing Breakdown

| Frame | Duration | Description | Easing |
|---|---|---|---|
| 0 (Shock) | 167ms | Fatal hit, arms splay, pen flies | None (snap) |
| 1 (Split start) | 167ms | Seam splits open, arms reach across gap | None |
| 2 (Collapse) | 167ms | Both halves sag, knees buckle, tears | **Ease-out** — slow deceleration into collapse |
| 3 (Final) | 167ms + 2000ms hold | Heap on ground, pool of ink/fluid | None (held static) |

### Particle Effects — Death
| Particle | Emitter Config | Trigger |
|---|---|---|
| Stitch snap sparks | 1 particle per stitch (5 total), `#F0C830`, 1x1px, burst over 300ms staggered, speed 20px/s upward | Frame 0-1 |
| Thread fragments | 5-7 particles, `#1A1A18`, 1x3px lines, gravity 40px/s, rotation random, lifespan 600ms | Frame 1 |
| Flesh chunks | 3-4 particles, `#8B3030`, 2x2px, speed 15px/s radial outward from seam, gravity 50px/s, lifespan 500ms | Frame 1-2 |
| Tears (Lula) | 2 particles, `#4A7AAA`, 1x2px, gravity 60px/s, starting from left eye, lifespan 400ms, repeat 3x | Frame 2-3 |
| Tear (Bolso) | 1 particle, `#4A7AAA`, 1x1px, gravity 60px/s, starting from right eye, lifespan 300ms, repeat 1x | Frame 2 only (single reluctant tear) |
| Green gas release | 6-8 particles, `#4A7C59` at 40% alpha, 3x3px, speed 8px/s upward-radial, lifespan 1200ms, scale 1.0->2.0->0.0 | Frame 2-3, continuous burst |
| Ink pool spread | Animated ground decal, starts 2x2px grows to 12x12px over 1500ms, mixed `#8B1A1A` + `#2E5A1C` blending to `#4A3A2A` (brown sludge), alpha 0.8 | Frame 3 hold period |

### Sound Triggers — Death
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Stitch rip | `sfx_bolsolula_stitch_rip.ogg` | Frame 0 | 0.6 |
| Void open | `sfx_bolsolula_void.ogg` | Frame 1 (deep bass rumble) | 0.5 |
| Dual whimper | `sfx_bolsolula_whimper.ogg` | Frame 2 (both voices, sad) | 0.7 |
| Body thud | `sfx_bolsolula_thud.ogg` | Frame 3 | 0.5 |
| Death bordao | `vox_bolsolula_death.ogg` — "Eu sou dois... e nenhum dos dois presta..." | Frame 2-3 | 0.8 |

### Screen Effects — Death
| Effect | Trigger | Duration |
|---|---|---|
| Slow motion | Frame 0 start | 400ms at 0.5x game speed |
| Camera zoom slight | Frame 1 | Zoom to 1.1x over 300ms, ease-out |
| Screen desaturate | Frame 3 hold | 10% desaturation for 1000ms |
| Boss HP bar shatter | Frame 0 | HP bar breaks into fragments that fall with gravity |

### Post-Death Sequence
```javascript
// After death animation + hold + fade:
// 1. Drop loot at body position
// 2. Spawn "EMENDAS" pickup (currency) x50-100, fountain burst upward
// 3. Play victory fanfare (dual melody — samba + marcha militar mashup)
// 4. Display "BOLSOLULA DERROTADO" text (split color: red left, green right)
// 5. If first kill: trigger achievement "Centrista Radical"
```

---

## 5. HIT — `bolsolula_hit`

| Property | Value |
|---|---|
| Frames | 2 |
| Frame Rate | 12 fps (FAST — snappy feedback) |
| Loop | No |
| Duration | 167ms |
| Phaser key | `bolsolula_hit` |
| Invincibility window | 300ms after hit start |

### Timing Breakdown

| Frame | Duration | Description | Easing |
|---|---|---|---|
| 0 (Impact) | 83ms | Rock backward, conflicting reactions, white flash | None (instant) |
| 1 (Recoil) | 83ms | Spring back, unified anger, color flash fade | **Ease-out** — bounce effect |

### Particle Effects — Hit
| Particle | Emitter Config | Trigger |
|---|---|---|
| Hit flash | Full-body white outline, 1px, `#FFFFFF` at 60% alpha, lifespan 83ms | Frame 0 |
| Star impacts | 2-3 particles, `#F0C830`, 3x3px star shape, speed 0 (static at impact point), alpha 1.0->0.0, lifespan 150ms | Frame 0 |
| Color tint (Lula) | Left-half overlay, `#8B1A1A` at 15%, lifespan 120ms, alpha 0.15->0.0 | Frame 1 |
| Color tint (Bolso) | Right-half overlay, `#CC5500` at 15%, lifespan 120ms, alpha 0.15->0.0 | Frame 1 |
| Bolt spark | 1 particle, `#F0C830`, 1x1px, lifespan 100ms | Frame 1 |

### Sound Triggers — Hit
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Flesh impact | `sfx_bolsolula_hit_flesh.ogg` | Frame 0 | 0.6 |
| Dual grunt | `sfx_bolsolula_grunt.ogg` (two voices overlapped) | Frame 0 | 0.5 |
| Bolt clang | `sfx_bolt_clang.ogg` | Frame 1, 30% chance | 0.3 |
| Bordao (hit) | See `bolsolula-bordoes.md` hit triggers | 30% chance | 0.6 |

### Screen Effects — Hit
| Effect | Trigger | Duration |
|---|---|---|
| Camera micro-shake | Frame 0 | 30ms, magnitude 1px |
| Hitstop (frame freeze) | Frame 0 | 33ms (2 game frames at 60fps) |

---

## 6. SPECIAL SKILLS

### 6A. POLARIZACAO TOTAL — `bolsolula_special_polarizacao`

| Property | Value |
|---|---|
| Frames | 2 (charge + blast) |
| Frame Rate | 8 fps |
| Loop | No |
| Total Skill Duration | 3000ms (250ms charge anim + 2750ms effect) |
| Cooldown | 12000ms |
| Phaser key | `bolsolula_special_polarizacao` |

### Timing
| Phase | Duration | Visual |
|---|---|---|
| Charge (frame 0) | 250ms | Halves pull apart, ground cracks, particles orbit |
| Blast (frame 1) | 250ms | Shockwave release, dual-color semicircles |
| Field active | 2500ms | Ground stays divided — red zone left, green zone right |
| Field fade | 500ms (overlap) | Colors fade, ground returns to normal |

### Particle Effects — Polarizacao
| Particle | Emitter Config | Phase |
|---|---|---|
| Red orbit (Lula) | 8 particles, `#8B1A1A`, 2x2px, circular orbit radius 20px, speed 180deg/sec, alpha 0.8 | Charge |
| Green orbit (Bolso) | 8 particles, `#2E5A1C`, 2x2px, circular orbit radius 20px, speed 180deg/sec, alpha 0.8 | Charge |
| Ground crack | Animated decal: black line (`#1A1A18`) extending from center outward, 2px/frame, total length 200px each direction | Charge -> Blast |
| Red shockwave | Semicircle expanding LEFT, `#8B1A1A` at 50% alpha, 3px thick arc, radius 0->200px over 500ms | Blast |
| Green shockwave | Semicircle expanding RIGHT, `#2E5A1C`+`#C8A832` at 50% alpha, 3px thick arc, radius 0->200px over 500ms | Blast |
| Field glow (red zone) | Full left-screen overlay, `#8B1A1A` at 10% alpha, subtle pulse (8%->12%->8% over 1000ms) | Field active |
| Field glow (green zone) | Full right-screen overlay, `#2E5A1C` at 10% alpha, subtle pulse | Field active |

### Gameplay Effect
```javascript
polarizacaoTotal = {
  fieldDuration: 2500,
  leftZone: { color: 'red', damageType: 'lula' },
  rightZone: { color: 'green', damageType: 'bolso' },
  // Players on the "wrong" side take 5 DPS
  // "Wrong" depends on which side is currently dominant
  damagePerSecond: 5,
  // Enemies are also affected — green enemies take damage in red zone, etc.
  affectsEnemies: true
};
```

### Sound — Polarizacao
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Charge hum | `sfx_polarizacao_charge.ogg` (rising dual-tone hum) | Charge start | 0.5->0.8 ramp |
| Shockwave | `sfx_polarizacao_blast.ogg` (bass drop + split stereo — L=red, R=green) | Blast | 0.8 |
| Field ambience | `sfx_polarizacao_field.ogg` (low political rally murmur, looped) | Field active | 0.3 |
| Bordao | `vox_bolsolula_polarizacao.ogg` — "A culpa e do outro lado!" | Charge | 0.7 |

---

### 6B. PALANQUE INFINITO — `bolsolula_special_palanque`

| Property | Value |
|---|---|
| Frames | 2 (summon + speech) |
| Frame Rate | 8 fps |
| Loop | Speech frame loops |
| Total Skill Duration | 5000ms |
| Cooldown | 15000ms |
| Phaser key | `bolsolula_special_palanque` |

### Timing
| Phase | Duration | Visual |
|---|---|---|
| Summon (frame 0) | 500ms | Two podiums erupt from ground, cloth drapes |
| Speech (frame 1) | 4000ms (loops) | Both mouths move, speech bubbles cycle, sound waves radiate |
| Podium crumble | 500ms (overlap) | Podiums sink back into ground, debris scatter |

### Particle Effects — Palanque
| Particle | Emitter Config | Phase |
|---|---|---|
| Ground eruption (x2) | Dirt chunks, `#C4A265`, 3x3px, 6 particles per podium, burst upward speed 40px/s, gravity 80px/s | Summon |
| Sound waves (left) | Concentric arcs expanding from left podium, `#8B1A1A` at 30% alpha, 1px thick, 3 arcs staggered 200ms, radius 0->60px, alpha fade | Speech (repeating) |
| Sound waves (right) | Same as left but from right podium, `#2E5A1C` at 30% alpha | Speech (repeating) |
| Speech bubble (left) | Sprite overlay, white bubble with red border, text cycles: "COMPANHEIRO!", "A GENTE VAMOS...", "NUNCA ANTES..." every 800ms | Speech |
| Speech bubble (right) | Sprite overlay, white bubble with green border, text cycles: "VAGABUNDO!", "TALKEI!", "MITO!" every 800ms | Speech |
| Mesmerized crowd | 4-6 tiny figures (3x3px, `#5C5C55`) spawn and drift toward podiums at 10px/s, stop at 20px distance, sway left-right 1px | Speech |
| Podium debris | Wood splinters, `#6B4423`, 2x2px, 4 per podium, burst upward, gravity 60px/s | Crumble |

### Gameplay Effect
```javascript
palanqueInfinito = {
  duration: 5000,
  // Creates two zones of "hypnosis"
  leftPodiumRadius: 48, // red zone
  rightPodiumRadius: 48, // green zone
  // Enemies entering a zone are STUNNED (mesmerized by speech)
  stunDuration: 2000,
  // Player takes slow DOT if standing in either zone (boredom damage)
  playerDOT: 3, // per second
  // BolsoLula heals during speech
  healPerSecond: 5
};
```

### Sound — Palanque
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Podium erupt | `sfx_podium_erupt.ogg` (wood cracking upward) | Summon | 0.5 |
| Microphone feedback | `sfx_mic_feedback.ogg` (annoying screech) | Summon + 200ms | 0.4 |
| Dual speech loop | `sfx_bolsolula_speech_loop.ogg` (overlapping gibberish comicio, 4s loop) | Speech | 0.5 |
| Crowd murmur | `sfx_crowd_murmur.ogg` (small crowd, looped) | Speech | 0.2 |
| Podium collapse | `sfx_podium_collapse.ogg` | Crumble | 0.4 |

---

### 6C. DEBATE ETERNO — `bolsolula_special_debate`

| Property | Value |
|---|---|
| Frames | 2 (start + sonic blast) |
| Frame Rate | 8 fps |
| Loop | No |
| Total Skill Duration | 2000ms |
| Cooldown | 10000ms |
| Phaser key | `bolsolula_special_debate` |

### Timing
| Phase | Duration | Visual |
|---|---|---|
| Debate start (frame 0) | 500ms | Faces turn inward, fingers point, energy crackles | 
| Sonic blast (frame 1) | 500ms | Massive circular sound wave expands |
| Aftershock | 1000ms | 2 more weaker rings expand, echo fading |

### Particle Effects — Debate
| Particle | Emitter Config | Phase |
|---|---|---|
| Crackling energy | Zigzag line between faces, alternating `#8B1A1A`/`#2E5A1C`, 1px, flickering 20Hz, length 12px | Debate start |
| Primary sound ring | Circular ring expanding from head center, 2px thick, segmented alternating red-green (8 segments), radius 0->150px over 500ms, alpha 0.8->0.0 | Sonic blast |
| Secondary ring 1 | Same as primary but delayed 300ms, thinner (1px), radius 0->120px, alpha 0.5->0.0 | Aftershock |
| Secondary ring 2 | Same, delayed 600ms, radius 0->100px, alpha 0.3->0.0 | Aftershock |
| Ear cover sparks | 2 particles per frame at each ear-covering hand (4 hands covering), `#F0C830`, 1x1px | Sonic blast |

### Gameplay Effect
```javascript
debateEterno = {
  damageType: 'sonic',
  aoeShape: 'circle',
  aoeRadius: 150,
  damage: 20, // burst
  knockback: 24, // pushes everything away
  stunChance: 0.3, // 30% chance to stun for 1000ms
  selfDamage: 5, // BolsoLula hurts itself too (both sides screaming)
  screenShake: { magnitude: 4, duration: 300 }
};
```

### Sound — Debate
| Sound | File | Trigger | Volume |
|---|---|---|---|
| "COMPANHEIRO!" | `vox_lula_companheiro.ogg` | Debate start | 0.7 (LEFT channel) |
| "VAGABUNDO!" | `vox_bolso_vagabundo.ogg` | Debate start + 100ms offset | 0.7 (RIGHT channel) |
| Sonic boom | `sfx_debate_sonic.ogg` (bass-heavy boom with political speech distortion) | Sonic blast | 0.9 |
| Echo | `sfx_debate_echo.ogg` (fading reverb of both voices overlapping) | Aftershock | 0.4->0.1 fade |

---

### 6D. TROCA DE LADO — `bolsolula_troca` (Passive)

| Property | Value |
|---|---|
| Type | Passive (no animation frames — uses idle transition) |
| Interval | 5000ms |
| Visual | Seam flash + body lean shift |

### Timing
| Phase | Duration | Visual |
|---|---|---|
| Warning pulse | 500ms before switch | Fusion seam pulses 3 times (100ms on/off), `#F0C830` at 40% |
| Switch flash | 100ms | Full-seam bright flash, body snaps to new lean direction |
| New dominant settle | 400ms | Subtle ease into new posture |

### Dominant Side Effects
```javascript
trocaDeLado = {
  interval: 5000,
  states: {
    lula: {
      attackType: 'cachaca_splash', // projectile: arc, AoE puddle
      movementBias: 'erratic', // stumbles more
      voiceLines: 'lula_set',
      colorTint: { r: 0.05, g: 0, b: 0 }, // slight red overlay
      bonusAbility: 'mentira_shield' // speech bubble blocks 1 hit
    },
    bolsonaro: {
      attackType: 'arma_brochavel', // projectile: straight line, jams 30% of time
      movementBias: 'rigid', // marches straighter
      voiceLines: 'bolsonaro_set',
      colorTint: { r: 0, g: 0.03, b: 0 }, // slight green overlay
      bonusAbility: 'motociata' // charge forward, knockback
    }
  }
};
```

### Sound — Troca
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Warning chime | `sfx_troca_warning.ogg` (political jingle distorted) | Warning pulse | 0.4 |
| Switch zap | `sfx_troca_switch.ogg` (electrical zap) | Switch flash | 0.5 |
| New dominant voice | Random bordao from new dominant side | Post-switch 200ms | 0.6 |

---

### 6E. CENTRAO GRAVITACIONAL — `bolsolula_special_centrao`

| Property | Value |
|---|---|
| Frames | 2 (pull + orbit) |
| Frame Rate | 8 fps |
| Loop | Orbit frame loops |
| Total Skill Duration | 6000ms |
| Cooldown | 18000ms |
| Phaser key | `bolsolula_special_centrao` |

### Timing
| Phase | Duration | Visual |
|---|---|---|
| Gravitational pull (frame 0) | 1000ms | Spiral lines, enemies dragged inward |
| Orbit established (frame 1) | 4000ms (loops) | Enemies circle, BolsoLula conducts |
| Release / scatter | 1000ms | Orbiting enemies flung outward in all directions |

### Particle Effects — Centrao
| Particle | Emitter Config | Phase |
|---|---|---|
| Spiral pull lines | 8 lines, `#1A1A18`, 1px, spiral inward from 120px radius to 40px, rotation 180deg/sec | Pull |
| Orbit path | Dashed circle, `#1A1A18` at 40% alpha, radius 40px, rotating 30deg/sec | Orbit |
| Emenda papers | 4-6 tiny papers, `#E8D8B0`, 2x2px, travel outward from pen to orbiting enemies along orbit path | Orbit |
| Release burst | All orbit particles change to radial outward, speed 100px/s, `#F0C830` flash at center | Release |

### Gameplay Effect
```javascript
centraoGravitacional = {
  pullRadius: 120,
  pullForce: 60, // px/s toward center
  orbitRadius: 40,
  orbitSpeed: 90, // degrees per second
  duration: 6000,
  // Enemies in orbit take 3 DPS from "emendas"
  orbitDamagePerSecond: 3,
  // On release: enemies flung outward at high speed
  releaseSpeed: 200,
  releaseDamage: 10, // collision damage with environment
  // Player is also pulled (but less — 40% force)
  playerPullMultiplier: 0.4,
  maxOrbitingEnemies: 8
};
```

### Sound — Centrao
| Sound | File | Trigger | Volume |
|---|---|---|---|
| Gravity hum | `sfx_centrao_hum.ogg` (deep bass drone, rising pitch) | Pull | 0.4->0.7 ramp |
| Orbit whoosh | `sfx_centrao_orbit.ogg` (whooshing loop, stereo rotation) | Orbit (loop) | 0.5 |
| Paper flutter | `sfx_paper_flutter.ogg` | Orbit, random | 0.2 |
| Release explosion | `sfx_centrao_release.ogg` (bass boom + scatter) | Release | 0.7 |
| Bordao | `vox_bolsolula_centrao.ogg` — "Todo mundo vem pra ca! Talkei, companheiro?" | Pull start | 0.7 |

---

## 7. FUSION SEQUENCE — `bolsolula_fusion`

| Property | Value |
|---|---|
| Frames | 10 |
| Frame Rate | 8 fps (frames 0-5), 6 fps (frames 6-9) |
| Loop | No |
| Total Duration | ~2300ms |
| Phaser key | `bolsolula_fusion` |
| Context | Plays ONCE as boss intro cutscene |

### Timing Breakdown

| Frame | Duration | Description | Camera |
|---|---|---|---|
| 0 (Approach) | 125ms | Two characters running toward center | Zoom to 1.5x, center on midpoint |
| 1 (Collision) | 125ms | IMPACT, starburst, shockwave | Screen shake 4px, 100ms |
| 2 (Merge start) | 125ms | Flesh melting/fusing, horror | Hold zoom |
| 3 (Body horror 1) | 125ms | 50% merged, extra limbs, eye on chest | Slow zoom to 1.8x |
| 4 (Body horror 2) | 125ms | 75% merged, stitches forming | Hold |
| 5 (Stitching) | 125ms | Bolt punches through, stitches rapid | Hold |
| 6 (Stabilize) | 167ms | Complete but trembling | Zoom ease back to 1.3x |
| 7 (First look) | 167ms | Looks at self, mirror shard | Hold |
| 8 (First words) | 167ms | Speech bubbles, defeated acceptance | Hold |
| 9 (Battle ready) | 500ms (HELD) | Rage stance, seam pulses | Zoom ease back to 1.0x, boss HP bar appears |

### Particle Effects — Fusion (cumulative)
| Particle | Emitter Config | Frames |
|---|---|---|
| Gas tendrils | 4 lines from top of screen to each character, `#4A7C59` at 40%, wavy, pulling motion | 0 |
| Collision starburst | Burst of 16 particles, `#FFFFFF`, radial, speed 60px/s, lifespan 300ms | 1 |
| Collision shockwave | Ring, `#F0C830`, 2px thick, radius 0->80px, alpha 0.8->0.0, 400ms | 1 |
| Fabric debris | 8 particles, 50% `#8B1A1A` 50% `#2E5A1C`, 2x2px, radial outward, gravity 40px/s | 1 |
| Flesh tendrils | Animated sprite: thin lines reaching across gap, `#B07850`/`#D4A574`, 1px, 6-8 tendrils | 2-3 |
| Misplaced eye | Single sprite, eye graphic 3x3px, appears on chest frame 3, fades by frame 4 | 3-4 |
| Stitch sparks | 1 spark per stitch formed, `#F0C830`, 1x1px, burst | 4-5 |
| Bolt emergence | Metal sprite 3x3px pushes outward from skin, skin displacement ring around it | 5 |
| Aftershock tremor | Body position jitters +/-1px random x and y, 10Hz | 6 |
| Mirror glint | 1 pixel, `#FFFFFF`, flash on mirror shard on ground, alpha 0->1->0, 300ms | 7 |
| Speech bubble anim | Two bubbles grow from 0 to full size over 300ms, ease-out | 8 |
| Seam pulse (final) | Full-seam glow, `#F0C830` at 40%, pulse up to 60% and back, 500ms | 9 |

### Sound Design — Fusion Sequence
| Sound | File | Frames | Volume | Notes |
|---|---|---|---|---|
| Running footsteps | `sfx_run_dual.ogg` | 0 | 0.4 | Two sets of footsteps, panned L and R |
| Magnetic pull | `sfx_magnetic_pull.ogg` | 0 | 0.3->0.6 | Rising drone, they can't stop |
| COLLISION | `sfx_fusion_collision.ogg` | 1 | 0.9 | Massive impact, bass-heavy |
| Flesh merge | `sfx_flesh_merge.ogg` | 2-3 | 0.6 | Wet, organic, horrifying, comedic squelch |
| Bone crack | `sfx_bone_crack.ogg` | 3-4 | 0.5 | Multiple cracks as skeleton restructures |
| Scream (Lula) | `vox_lula_scream.ogg` | 2-4 | 0.7 | Horror scream, left channel |
| Scream (Bolso) | `vox_bolso_scream.ogg` | 2-4 | 0.7 | Horror scream, right channel |
| Stitch sew | `sfx_stitch_sew.ogg` | 5 | 0.4 | Rapid thread-through-flesh sounds, 5x |
| Bolt punch | `sfx_bolt_punch.ogg` | 5 | 0.6 | Metal through flesh thunk |
| Heartbeat (dual) | `sfx_heartbeat_dual.ogg` | 6-8 | 0.3 | Two heartbeats trying to synchronize, slightly off |
| "Com...panheiro?" | `vox_bolsolula_first_word_L.ogg` | 8 | 0.7 | Left channel, uncertain |
| "...talkei?" | `vox_bolsolula_first_word_R.ogg` | 8 | 0.7 | Right channel, uncertain |
| BOSS MUSIC START | `bgm_bolsolula_theme.ogg` | 9 | 0.0->0.8 fade in over 2000ms | Samba + military march mashup |
| Seam pulse bass | `sfx_seam_pulse.ogg` | 9 | 0.6 | Deep bass thump synchronized with visual pulse |

### Screen Effects — Fusion
| Effect | Frames | Description |
|---|---|---|
| Letterbox | 0-9 | Black bars top and bottom (cinematic 2.39:1) — remove on transition to gameplay |
| Screen shake | 1 | 4px magnitude, 100ms |
| Color flash | 1 | White screen flash, 50ms, alpha 0.6 |
| Vignette darken | 2-5 | Screen edges darken (horror atmosphere) |
| Slow motion | 3-5 | Game time at 0.5x (body horror emphasis) |
| Desaturation pulse | 3 | 30% desaturate for 200ms (when misplaced eye appears) |
| Zoom | 0-9 | See camera column in timing table |
| Boss title card | 9 (held) | "BOLSOLULA" text appears in center, split color (red left / green right), Andre Guedes hand-drawn font, stays 1500ms then fades |

---

## 8. SPLIT / FUSAO REVERSA (Ultimate) — `bolsolula_split`

| Property | Value |
|---|---|
| Frames | 8 |
| Frame Rate | 8 fps (frames 0-3), 6 fps (frames 4-7) |
| Loop | No |
| Total Duration | ~1800ms (split) + 15000ms (chaos) + ~1200ms (re-fuse) |
| Phaser key | `bolsolula_split` |
| HP Threshold | Can only use below 40% HP |
| Uses per fight | 1 (or 2 on harder difficulties) |

### Timing Breakdown

| Frame | Duration | Description | Camera |
|---|---|---|---|
| 0 (Strain) | 125ms | Self-tearing, seam glows | Zoom to 1.3x |
| 1 (Stitches snap) | 125ms | Sequential stitch breaks, void visible | Screen shake 2px |
| 2 (Halfway) | 125ms | Connected at head and leg only | Hold |
| 3 (Head divides) | 125ms | THE SPLIT — massive flash | White flash 100ms |
| 4 (Separation) | 167ms | Two stumbling halves | Zoom eases back to 1.0x |
| 5 (Regenerate) | 167ms | New tissue grows over exposed sides | Hold |
| 6 (Two bosses) | 167ms | Fully separated, electrical arcs | Hold |
| 7 (Chaos begins) | 167ms | Both lunge at each other and player | Hold; 15s timer starts |

### Split Phase Particles
| Particle | Emitter Config | Frames |
|---|---|---|
| Seam glow | Full seam line, `#F0C830` at 80%, pulsing | 0 |
| Stitch sparks | 5 sparks sequential (100ms apart), `#F0C830`, 2x2px, burst outward | 1 |
| Thread fragments | 5-7 pieces, `#1A1A18`, 1x4px, gravity 40px/s, lifespan 500ms | 1 |
| Muscle fibers | 3-4 lines, `#8B3030`, stretch across gap then snap, 1px | 1-2 |
| Void energy | 6 particles, alternating `#8B1A1A`/`#2E5A1C`, 2x2px, chaotic inside gap | 2-3 |
| Head split flash | 24x24px starburst, `#FFFFFF` at 70%, lifespan 200ms | 3 |
| Bolt drop | 3x3px metallic object, gravity 80px/s, bounce once | 2 |
| Tissue particles | 4 per frame, `#8B3030`/skin tones, falling between halves | 3-4 |
| Electrical arcs | 3 zigzag lines between separated halves, `#F0C830`, 1px, flickering 15Hz | 6-7 |
| Regeneration pixels | Per-pixel fill of exposed side, skin tones, 2px/frame growth rate | 5 |

### 15-Second Chaos Phase
```javascript
fusaoReversaChaos = {
  duration: 15000,
  // Spawn two separate boss entities
  lulaHalf: {
    hp: currentHP * 0.5,
    sprite: 'boss_lula', // use Lula's normal boss sprite set
    aiType: 'aggressive_to_all', // attacks player AND bolsonaro half
    speed: 100, // faster than fused form
    attacks: ['cachaca_splash', 'faz_o_L', 'discurso'],
    targetPriority: 0.6 // 60% chance to target Bolsonaro half, 40% player
  },
  bolsonaroHalf: {
    hp: currentHP * 0.5,
    sprite: 'boss_bolsonaro', // use Bolsonaro's normal boss sprite set
    aiType: 'aggressive_to_all',
    speed: 110,
    attacks: ['arma_brochavel', 'motociata', 'live_rant'],
    targetPriority: 0.6 // 60% chance to target Lula half, 40% player
  },
  // They fight each other more than the player
  // Damage dealt between them is real — can weaken each other
  // If EITHER dies during split: the other absorbs it and re-fuses at 30% HP
  // If timer expires: automatic re-fusion at combined remaining HP
  timerDisplay: true, // show countdown HUD element
  timerColor: '#F0C830',
  reFusionAnimation: 'bolsolula_fusion_short' // abbreviated 4-frame re-merge
};
```

### Re-Fusion (after 15s or on half-death)
| Frame | Duration | Description |
|---|---|---|
| R0 | 167ms | Both halves pulled toward center by electrical arcs |
| R1 | 167ms | Collision at center, starburst (smaller than original fusion) |
| R2 | 167ms | Rapid re-merge, stitches re-form, bolt re-inserts |
| R3 | 500ms (hold) | BolsoLula back together, seam ANGRIER — more stitches, bolt bent, new scars |

### Sound Design — Split
| Sound | File | Frames | Volume |
|---|---|---|---|
| Strain groan | `sfx_split_strain.ogg` (wet tearing starting) | 0 | 0.6 |
| Stitch snaps | `sfx_stitch_snap_sequence.ogg` (5 rapid snaps) | 1 | 0.7 |
| Muscle tear | `sfx_muscle_tear.ogg` (wet, grotesque) | 1-2 | 0.5 |
| HEAD CRACK | `sfx_head_split.ogg` (massive bone crack + dual scream) | 3 | 0.9 |
| Bolt clatter | `sfx_bolt_fall.ogg` | 2 | 0.3 |
| Separation pop | `sfx_separation_pop.ogg` (suction release) | 4 | 0.6 |
| Tissue growth | `sfx_tissue_grow.ogg` (wet bubbling) | 5 | 0.4 |
| Electrical crackle | `sfx_electrical_arc.ogg` (constant crackle, looped) | 6-7 | 0.3 |
| Dual war cry | Both voices simultaneously: Lula "COMPANHEIRO!" + Bolso "IMBROCHAVEL!" | 7 | 0.8 |
| Chaos music | `bgm_bolsolula_chaos.ogg` (tempo doubles, both themes clash) | 7 -> +15s | 0.7 |
| Re-fusion collision | `sfx_refusion_slam.ogg` | Re-R1 | 0.7 |
| Re-stitch rapid | `sfx_restitch.ogg` | Re-R2 | 0.5 |

### Screen Effects — Split
| Effect | Frames | Description |
|---|---|---|
| Screen shake | 3 | 6px magnitude, 150ms |
| White flash | 3 | 100ms, alpha 0.5 |
| Slow motion | 3-4 | 0.5x game speed for 400ms |
| Split-screen hint | 6-7 | Subtle vertical line down center of screen (1px, `#1A1A18` at 20%) — removed when chaos starts |
| Timer HUD | 7 -> +15s | "15" countdown in `#F0C830`, top center, pulses red when <3s |
| Camera zoom out | 7 | Zoom to 0.9x to fit both bosses on screen |

---

## 9. GLOBAL ANIMATION RULES

### Dominance System (affects ALL animations)
```javascript
// The "dominant side" switches every 5 seconds
// This affects:
// 1. Which idle frame plays first
// 2. Walk direction bias (dominant side steps first)
// 3. Attack sub-type (Lula or Bolsonaro variant)
// 4. Voice lines (from dominant side's pool)
// 5. Slight color tint overlay (red for Lula, green for Bolsonaro)

dominanceSystem = {
  switchInterval: 5000,
  currentDominant: 'lula', // or 'bolsonaro'
  warningTime: 500, // seam pulses before switch
  transitionDuration: 200,
  onSwitch: (newSide) => {
    playSeamFlash();
    setIdleBias(newSide);
    setAttackVariant(newSide);
    setVoicePool(newSide);
    applyColorTint(newSide);
    emitEvent('dominanceSwitch', newSide);
  }
};
```

### Animation Priority (highest first)
1. Fusion Sequence (intro, plays once)
2. Death
3. Split / Fusao Reversa (ultimate)
4. Special Skills
5. Hit (interrupts current)
6. Attack
7. Walk
8. Idle (default)

### Transition Rules
| From | To | Transition |
|---|---|---|
| Idle | Walk | Instant cut |
| Walk | Idle | Instant cut (return to frame matching current dominant side) |
| Any | Hit | Instant interrupt, return to previous anim after |
| Any | Death | Instant interrupt, no return |
| Idle/Walk | Attack | Instant cut, return to Idle after |
| Idle/Walk | Special | Instant cut, return to Idle after |
| Any | Split | Instant interrupt (ultimate override) |
| Fusion | Idle | 500ms hold on last fusion frame, then crossfade |

### Fusion Seam — Persistent Effect
```javascript
// The fusion seam is a constant visual element with its own micro-animation
// Independent of the main sprite animation
fusionSeam = {
  sparkRate: 1, // sparks per second, always
  glowPulse: {
    color: '#F0C830',
    alphaRange: [0.05, 0.15],
    frequency: 0.5 // Hz
  },
  stressResponse: {
    // On hit: seam flares to 0.4 alpha for 200ms
    // On special: seam flares to 0.6 alpha for duration
    // On low HP (<25%): seam sparks increase to 4/sec, glow amplitude doubles
    // On very low HP (<10%): seam actively splits (4px gap, closing and opening)
  }
};
```

---

## 10. BOSS MUSIC SYNC

### Theme Structure
```
BPM: 120
Time Signature: alternating 2/4 (samba) and 4/4 (marcha militar)
Structure: Intro (fusion scene) -> Loop A (normal fight) -> Loop B (chaos/split) -> Loop A
```

### Beat-Synced Events
| Beat | Event |
|---|---|
| Every downbeat (beat 1) | Fusion seam spark |
| Every 4 bars | Dominance switch check (adjusted to nearest beat) |
| On musical accent | Attack animations start on beat when possible |
| Tempo double | Triggers on split (chaos phase) |
| Tempo halve | Triggers on re-fusion |

---

## 11. DEBUG VISUALIZATION (Dev Only)

```javascript
// Toggle with F9 in debug mode
debugOverlays = {
  showHitboxes: true, // red outlines on damage zones
  showDominantSide: true, // text overlay "LULA" or "BOLSO" above head
  showSeamStress: true, // number showing seam integrity percentage
  showSkillCooldowns: true, // bars above boss
  showAIState: true, // current AI behavior state
  showSplitTimer: true, // countdown during chaos phase
  showOrbitPaths: true // during centrao skill
};
```
