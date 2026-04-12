# Nikolas Ferreira (O Influencer-Politico) - Animation Specification

## Phaser 3 Animation Keys

---

### Animation: `nikolas_idle`
- **Type:** Loop
- **Frames:** [0, 1, 2, 3]
- **Frame Rate:** 8 fps
- **Frame Duration:** 125ms each
- **Repeat:** -1 (infinite loop)
- **Yoyo:** false
- **Description:** Nikolas em pe olhando o celular com deboche. Ring light pulsa suavemente, numeros de views flutuam ao redor, polegar enorme faz scroll na tela. Ciclo sutil de brilho no ring light (dim -> bright -> max -> dim).

```javascript
this.anims.create({
    key: 'nikolas_idle',
    frames: this.anims.generateFrameNumbers('nikolas_idle', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1,
    yoyo: false
});
```

#### Particle System: View Count Numbers (Idle)
- **Emitter:** Continuous during idle
- **Particles:** Text sprites ("1.2M", "♥50K", "10K", "LIVE")
- **Count:** 2-3 simultaneously visible
- **Orbit:** Circular path around character, radius 20-28px
- **Speed:** 15-25 px/s orbital velocity
- **Lifespan:** 2000-3000ms
- **Alpha:** 0 -> 1.0 (200ms fade in) -> 1.0 -> 0 (200ms fade out)
- **Scale:** 0.5 -> 0.8 (subtle pulse)
- **Colors:** Green (#00FF41) for numbers, Red (#FF4136) for hearts/likes

```javascript
const viewCountEmitter = this.add.particles(0, 0, 'view_numbers', {
    speed: 20,
    lifespan: 2500,
    alpha: { start: 0, end: 1, ease: 'Sine.easeIn' },
    scale: { start: 0.5, end: 0.8 },
    quantity: 1,
    frequency: 800,
    radial: true,
    follow: nikolas,
    followOffset: { x: 0, y: -16 }
});
```

#### Ring Light Pulse (Idle)
- **Type:** Tween on ring light overlay sprite
- **Cycle:** 500ms
- **Alpha:** 0.3 -> 0.6 -> 0.8 -> 0.3
- **Scale:** 1.0 -> 1.05 -> 1.1 -> 1.0
- **Blend Mode:** ADD

```javascript
this.tweens.add({
    targets: ringLightOverlay,
    alpha: { from: 0.3, to: 0.8 },
    scaleX: { from: 1.0, to: 1.1 },
    scaleY: { from: 1.0, to: 1.1 },
    duration: 500,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

---

### Animation: `nikolas_walk`
- **Type:** Loop
- **Frames:** [0, 1, 2, 3, 4, 5]
- **Frame Rate:** 10 fps
- **Frame Durations (individual):**
  - Frame 0 (stride L): 100ms
  - Frame 1 (neutral): 100ms
  - Frame 2 (stride R): 100ms
  - Frame 3 (stumble): 120ms -- held slightly longer for comedy
  - Frame 4 (recover): 90ms -- quick recovery
  - Frame 5 (complete): 90ms
- **Total Cycle:** ~600ms
- **Repeat:** -1 (infinite loop)
- **Description:** Nikolas caminha olhando SOMENTE o celular. No frame 3 ele tropeca levemente (porque nao olha pra frente) mas nem percebe. O ring light trail atrás e os numeros de views formam uma "cauda" de movimento.

```javascript
this.anims.create({
    key: 'nikolas_walk',
    frames: [
        { key: 'nikolas_walk', frame: 0, duration: 100 },
        { key: 'nikolas_walk', frame: 1, duration: 100 },
        { key: 'nikolas_walk', frame: 2, duration: 100 },
        { key: 'nikolas_walk', frame: 3, duration: 120 },
        { key: 'nikolas_walk', frame: 4, duration: 90 },
        { key: 'nikolas_walk', frame: 5, duration: 90 }
    ],
    frameRate: 10,
    repeat: -1
});
```

#### Particle Trail (Walk)
- **Type:** Trail emitter following character
- **Particles:** View count numbers + ring light afterglow
- **Direction:** Opposite to movement direction (trails behind)
- **Emission Rate:** 1 particle every 150ms
- **Lifespan:** 400ms
- **Alpha:** 0.8 -> 0
- **Speed:** 5 px/s (slow drift)

```javascript
const walkTrail = this.add.particles(0, 0, 'view_numbers', {
    speed: 5,
    lifespan: 400,
    alpha: { start: 0.8, end: 0 },
    quantity: 1,
    frequency: 150,
    follow: nikolas,
    angle: movementAngle + 180 // trails behind
});
```

#### Stumble Effect (Frame 3)
- **Camera:** Micro-shake 1px, 50ms
- **Character Offset:** +2px Y (dips down slightly)
- **Ring Light:** Flicker (alpha 0.8 -> 0.2 -> 0.8 in 120ms)

---

### Animation: `nikolas_attack`
- **Type:** Play once
- **Frames:** [0, 1, 2]
- **Frame Rate:** 10 fps
- **Frame Durations (individual):**
  - Frame 0 (wind-up): 133ms -- dramatic pause raising phone
  - Frame 1 (flash): 100ms -- FAST flash burst
  - Frame 2 (follow-through): 133ms -- recovery with satisfaction
- **Total Duration:** ~366ms
- **Repeat:** 0 (play once)
- **On Complete:** Return to `nikolas_idle`
- **Description:** Nikolas ergue o celular e dispara o FLASH como arma. O flash cega inimigos. "GRAVA!" aparece como onomatopeia.

```javascript
this.anims.create({
    key: 'nikolas_attack',
    frames: [
        { key: 'nikolas_attack', frame: 0, duration: 133 },
        { key: 'nikolas_attack', frame: 1, duration: 100 },
        { key: 'nikolas_attack', frame: 2, duration: 133 }
    ],
    frameRate: 10,
    repeat: 0
});
```

#### Flash Effect (Frame 1)
- **Type:** Expanding white circle + radial lines
- **Start Size:** 8x8px
- **End Size:** 48x48px
- **Duration:** 100ms
- **Color:** #FFFFFF at 90% opacity -> 0%
- **Blend Mode:** ADD
- **Radial Lines:** 6-8 lines from center, length 20-32px, 1px wide, white

```javascript
// Flash burst effect
const flash = this.add.circle(nikolas.x + 16, nikolas.y - 8, 4, 0xFFFFFF, 0.9);
flash.setBlendMode(Phaser.BlendModes.ADD);
this.tweens.add({
    targets: flash,
    radius: 24,
    alpha: 0,
    duration: 100,
    onComplete: () => flash.destroy()
});
```

#### "GRAVA!" Onomatopoeia (Frame 1)
- **Spawn:** At nikolas.x, nikolas.y - 24 (above head)
- **Style:** Grotesque comic letters, yellow (#F4D03F) with red (#E74C3C) shadow
- **Scale Tween:** 0.3 -> 1.2 (80ms, Back.easeOut) -> 1.0 (50ms) -> 0.8 alpha 0 (150ms)
- **Rotation:** Random +-8 degrees
- **Depth:** 9999

```javascript
const grava = this.add.sprite(nikolas.x, nikolas.y - 24, 'onomatopeia_grava');
grava.setDepth(9999);
grava.setScale(0.3);
grava.setRotation(Phaser.Math.FloatBetween(-0.14, 0.14));
this.tweens.add({
    targets: grava,
    scale: 1.2,
    duration: 80,
    ease: 'Back.easeOut',
    onComplete: () => {
        this.tweens.add({
            targets: grava,
            scale: 0.8, alpha: 0,
            duration: 150,
            onComplete: () => grava.destroy()
        });
    }
});
```

#### View Count Projectiles (Frame 1-2)
- **Type:** Burst emitter from phone position
- **Count:** 5-8 number particles
- **Direction:** Cone toward attack target, 60 degree spread
- **Speed:** 120-200 px/s
- **Lifespan:** 300ms
- **Content:** "+1K", "+10K", "♥", "👍"
- **Gravity:** 0 (fly straight)

---

### Animation: `nikolas_death`
- **Type:** Play once
- **Frames:** [0, 1, 2, 3]
- **Frame Rate:** 6 fps (slower for dramatic effect)
- **Frame Durations (individual):**
  - Frame 0 (shock): 200ms -- held for horror
  - Frame 1 (falling): 166ms
  - Frame 2 (ground): 200ms -- held for pathos
  - Frame 3 (dead): 250ms -- final hold
- **Total Duration:** ~816ms
- **Repeat:** 0 (play once)
- **On Complete:** Freeze on frame 3
- **Description:** Morte dramatica digital. Celular cai, tela racha, ring light apaga, numeros de views despencam a zero. A morte de um influencer e a morte da conectividade.

```javascript
this.anims.create({
    key: 'nikolas_death',
    frames: [
        { key: 'nikolas_death', frame: 0, duration: 200 },
        { key: 'nikolas_death', frame: 1, duration: 166 },
        { key: 'nikolas_death', frame: 2, duration: 200 },
        { key: 'nikolas_death', frame: 3, duration: 250 }
    ],
    frameRate: 6,
    repeat: 0
});
```

#### View Count Crash (Frames 0-3)
- **Type:** Numbers falling with gravity
- **Content Sequence:**
  - Frame 0: "1.2M" -> "500K" -> "100K" (numbers shrinking rapidly)
  - Frame 1: "0 VIEWS", "UNFOLLOW", "BLOCKED" (negative metrics raining down)
  - Frame 2: "0", "CANCELADO", "404" (digital death)
  - Frame 3: "..." (fading to nothing)
- **Gravity:** 200 px/s^2 (heavy fall)
- **Alpha:** 1.0 -> 0 over lifespan
- **Color shift:** Green -> Yellow -> Red -> Gray (dying metrics)

```javascript
// View count crash effect
const crashEmitter = this.add.particles(nikolas.x, nikolas.y - 20, 'view_numbers_death', {
    speed: { min: 20, max: 60 },
    angle: { min: 70, max: 110 }, // mostly downward
    gravityY: 200,
    alpha: { start: 1, end: 0 },
    lifespan: 800,
    quantity: 3,
    frequency: 200,
    tint: [0x00FF41, 0xFFFF00, 0xFF4136, 0x808080]
});
```

#### Ring Light Death (Frames 0-3)
- **Frame 0:** Flickering rapidly (ON 50ms / OFF 50ms alternating)
- **Frame 1:** Shattering - ring breaks into 4-6 arc fragments falling with gravity
- **Frame 2:** Fragments on ground, faint glow fading
- **Frame 3:** Completely dark, only dark ring frame outline visible

```javascript
// Ring light flicker (Frame 0)
this.tweens.add({
    targets: ringLight,
    alpha: { from: 1, to: 0 },
    duration: 50,
    yoyo: true,
    repeat: 3
});

// Ring light shatter (Frame 1)
this.time.delayedCall(200, () => {
    ringLight.setVisible(false);
    spawnRingFragments(nikolas.x, nikolas.y - 20, 5);
});
```

#### Phone Drop (Frame 1-2)
- **Tween:** Phone sprite separates from character, falls with arc
- **Rotation:** 0 -> 720 degrees (tumbling)
- **Position:** nikolas hand -> ground (offset +10x, +15y)
- **Duration:** 300ms
- **On Land:** Crack overlay appears, screen goes dark

---

### Animation: `nikolas_hit`
- **Type:** Play once
- **Frames:** [0, 1]
- **Frame Rate:** 12 fps (fast reaction -- jerky Andre Guedes style)
- **Frame Durations:**
  - Frame 0 (recoil): 100ms -- quick knockback
  - Frame 1 (recover): 133ms -- slightly held (already filming)
- **Total Duration:** ~233ms
- **Repeat:** 0
- **On Complete:** Return to previous animation
- **Description:** Nikolas recua do impacto mas NAO solta o celular (polegar ENORME segura). Expressao muda de dor para INDIGNACAO para oportunismo ("isso vai render views!"). Ja no frame 1 ele esta filmando o que aconteceu.

```javascript
this.anims.create({
    key: 'nikolas_hit',
    frames: [
        { key: 'nikolas_hit', frame: 0, duration: 100 },
        { key: 'nikolas_hit', frame: 1, duration: 133 }
    ],
    frameRate: 12,
    repeat: 0
});
```

#### Hit Flash (Frame 0)
- **Effect:** White tint overlay
- **Duration:** 66ms
- **Method:** setTint(0xFFFFFF) then clearTint

#### Ring Light Blink (Frame 0)
- **Effect:** Ring light OFF for 100ms, then ON
- **Visual:** Suggests "signal loss" on impact

#### View Count Glitch (Frame 0)
- **Effect:** Floating numbers glitch/static for 100ms
- **Visual:** Numbers briefly show "???", "ERR", "NaN"
- **Duration:** 100ms then resolve back to normal numbers

#### "+100K" Popup (Frame 1)
- **Spawn:** Above head
- **Text:** "+100K" in green (#00FF41)
- **Animation:** Pop in (scale 0 -> 1.2 -> 1.0), float up 10px, fade out
- **Duration:** 400ms
- **Meaning:** Getting hit = content = more views

---

### Animation: `nikolas_special`
- **Type:** Play once
- **Name:** "LIVESTREAM APOCALIPTICA"
- **Frames:** [0, 1, 2, 3, 4, 5]
- **Frame Rate:** 8 fps
- **Frame Durations (individual):**
  - Frame 0 (prep): 150ms -- raising phone
  - Frame 1 (activate): 125ms -- ring light explosion
  - Frame 2 (notifications): 150ms -- projectile burst
  - Frame 3 (peak): 175ms -- held for maximum impact readability
  - Frame 4 (dissipate): 125ms
  - Frame 5 (recover): 125ms
- **Total Duration:** ~850ms
- **Repeat:** 0
- **On Complete:** Return to `nikolas_idle`
- **Cooldown:** 8000ms
- **Description:** Nikolas entra em LIVE apocaliptica. Ring light explode em tamanho, celular emite onda de choque de notificacoes (coracoes, sinos, cifras) que danificam todos os inimigos na area.

```javascript
this.anims.create({
    key: 'nikolas_special',
    frames: [
        { key: 'nikolas_special', frame: 0, duration: 150 },
        { key: 'nikolas_special', frame: 1, duration: 125 },
        { key: 'nikolas_special', frame: 2, duration: 150 },
        { key: 'nikolas_special', frame: 3, duration: 175 },
        { key: 'nikolas_special', frame: 4, duration: 125 },
        { key: 'nikolas_special', frame: 5, duration: 125 }
    ],
    frameRate: 8,
    repeat: 0
});
```

#### Ring Light Explosion (Frames 1-4)
- **Type:** Expanding circle overlay
- **Frame 0:** Normal size (radius 12px)
- **Frame 1:** EXPLODES (radius 12 -> 40px in 125ms), intense white glow
- **Frame 2:** Holds at maximum (radius 40px), pulsing
- **Frame 3:** Starts dimming (radius 40 -> 30px)
- **Frame 4-5:** Returns to normal (radius 30 -> 12px)
- **Blend Mode:** ADD
- **Alpha:** 0.5 -> 1.0 -> 1.0 -> 0.6 -> 0.3

```javascript
this.tweens.add({
    targets: ringLightSpecial,
    radius: { from: 12, to: 40 },
    alpha: { from: 0.5, to: 1.0 },
    duration: 125,
    ease: 'Expo.easeOut',
    onComplete: () => {
        this.tweens.add({
            targets: ringLightSpecial,
            radius: { from: 40, to: 12 },
            alpha: { from: 1.0, to: 0.3 },
            duration: 500,
            ease: 'Sine.easeInOut'
        });
    }
});
```

#### Notification Projectile Burst (Frames 2-3)
- **Type:** Radial burst emitter
- **Particle Types:** Hearts (♥), Bells, Dollar signs ($), Thumbs up
- **Count:** 20-30 particles total
- **Direction:** 360 degrees (all directions)
- **Speed:** 80-160 px/s
- **Lifespan:** 600-1000ms
- **Damage Radius:** 120px from character center
- **Alpha:** 1.0 -> 0 over lifespan
- **Rotation:** Each particle spins (180 deg/s)

```javascript
const notificationBurst = this.add.particles(nikolas.x, nikolas.y, 'notification_icons', {
    speed: { min: 80, max: 160 },
    angle: { min: 0, max: 360 },
    rotate: { min: 0, max: 360 },
    alpha: { start: 1, end: 0 },
    scale: { start: 1, end: 0.3 },
    lifespan: { min: 600, max: 1000 },
    quantity: 25,
    emitting: false
});
notificationBurst.explode();
```

#### Shockwave Ring (Frame 1)
- **Type:** Expanding circle outline
- **Start:** Radius 8px at character center
- **End:** Radius 120px (damage area)
- **Duration:** 300ms
- **Stroke:** 2px white, alpha 0.8 -> 0
- **Blend Mode:** ADD

#### "VIRALIZA!!" Text (Frame 3)
- **Spawn:** Above character, large
- **Style:** 48x24px, grotesque comic letters
- **Color:** Yellow (#F4D03F) with red (#E74C3C) shadow
- **Scale Tween:** 0.2 -> 1.5 (150ms, Back.easeOut) -> hold 175ms -> 0.8 alpha 0 (200ms)
- **Rotation:** Random +-5 degrees
- **Depth:** 9999

---

## Sound Cue Timing

| Time (ms) | Animation     | Event                    | Sound Key                    | Notes                                 |
|------------|---------------|--------------------------|------------------------------|---------------------------------------|
| 0          | attack        | Wind-up                  | `sfx_nikolas_phone_raise`    | Quick whoosh + phone notification     |
| 133        | attack        | Flash burst              | `sfx_nikolas_flash`          | Loud camera flash pop + static burst  |
| 133        | attack        | "GRAVA!" text            | `sfx_comic_pop`              | Comic book pop sound                  |
| 0          | death         | Shock                    | `sfx_nikolas_gasp`           | Sharp intake of breath                |
| 200        | death         | Phone drop               | `sfx_phone_crack`            | Glass cracking + plastic on floor     |
| 400        | death         | Ring light off            | `sfx_electric_fizzle`        | Electric fizzle dying out             |
| 0          | hit           | Recoil                   | `sfx_nikolas_outrage`        | Short "Ah!" of indignation            |
| 100        | hit           | "+100K" popup            | `sfx_notification_ding`      | Quick notification chime              |
| 0          | special       | Preparation              | `sfx_nikolas_going_live`     | "Going live!" voice clip              |
| 150        | special       | Ring light explosion     | `sfx_ring_light_burst`       | Electrical burst + bright tone        |
| 300        | special       | Notification burst       | `sfx_notification_swarm`     | Many notification sounds overlapping  |
| 475        | special       | "VIRALIZA!!"             | `sfx_viraliza`               | "Viraliza!" voice + comic pop         |

### Sound Descriptions
- **`sfx_nikolas_phone_raise`:** Quick (100ms) upward whoosh + single notification ding. Mid-frequency.
- **`sfx_nikolas_flash`:** Sharp (150ms) camera flash pop. High-pitched percussive burst with electrical crackle. Like a camera flash capacitor discharging.
- **`sfx_nikolas_gasp`:** Short (200ms) dramatic gasp of horror. Young male voice, high pitch.
- **`sfx_phone_crack`:** (300ms) Glass shattering + plastic impact. Two-part sound: crack then clatter.
- **`sfx_ring_light_burst`:** (200ms) Electrical surge crescendo. Like a fluorescent light exploding.
- **`sfx_notification_swarm`:** (500ms) Dozens of notification sounds overlapping chaotically. Dings, pings, chimes all at once.
- **`sfx_viraliza`:** (400ms) "VIRALIZA!" voice shout + comic pop. Young male, excited/manic tone.

---

## State Machine

```
            ┌──────────┐
    ┌──────►│   IDLE   │◄──────┐
    │       └────┬─────┘       │
    │            │              │
    │     ┌──────▼──────┐      │
    │     │    WALK     │      │
    │     └──────┬──────┘      │
    │            │              │
    │     ┌──────▼──────┐      │
    ├─────┤   ATTACK    ├──────┤
    │     └─────────────┘      │
    │                          │
    │     ┌─────────────┐      │
    ├─────┤   SPECIAL   ├──────┘
    │     └─────────────┘
    │
    │     ┌─────────────┐
    ├─────┤     HIT     ├──────► (return to previous)
    │     └─────────────┘
    │
    │     ┌─────────────┐
    └─────┤    DEATH    ├──────► (freeze on last frame)
          └─────────────┘
```

## Integration Notes

### Hitbox
- **Shape:** Circle
- **Radius:** 20px (centered on character)
- **Attack Hitbox:** Cone, 45 degree angle, 48px range (flash direction)
- **Special Hitbox:** Circle, 120px radius (notification burst area)

### Y-Sort Depth
```javascript
nikolas.setDepth(nikolas.y);
```

### NPC Behavior Notes
- Nikolas e um NPC PROVOCADOR - ele provoca o jogador deliberadamente
- Quando o jogador se aproxima, ele comeca a FILMAR (ataque automatico)
- Se atacado, ele NAO foge - ele filma o ataque ("conteudo!")
- Special trigger: quando HP < 30% (livestream apocaliptica como ultimo recurso)
- Numeros de views ao redor AUMENTAM conforme mais jogadores interagem com ele
