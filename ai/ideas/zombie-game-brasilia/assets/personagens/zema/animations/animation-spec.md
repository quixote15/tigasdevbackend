# Zema (O Privatizador / "Sera?") - Animation Specification

## Phaser 3 Animation Keys

---

### Animation: `zema_idle`
- **Type:** Loop
- **Frames:** [0, 1, 2, 3]
- **Frame Rate:** 8 fps
- **Frame Duration:** 125ms each
- **Repeat:** -1 (infinite loop)
- **Yoyo:** false
- **Description:** Zema em pe com postura excessivamente ereta. Pupilas-numeros ciclam por um calculo (0.00 -> 1.25 -> 47.8 -> 0.00). Calculadora no bolso pisca sutilmente. Sorriso frio NUNCA muda. A ausencia de movimento e a tensao.

```javascript
this.anims.create({
    key: 'zema_idle',
    frames: this.anims.generateFrameNumbers('zema_idle', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1,
    yoyo: false
});
```

#### Pupil Number Cycle (Idle)
- **Type:** Timed sprite swap on eye area
- **Cycle:** Synced with animation frames
- **Frame 0:** "0.00" (verde #00FF41)
- **Frame 1:** "1.25" (calculando)
- **Frame 2:** "47.8" (calculo intenso)
- **Frame 3:** "0.00" (reset)
- **Size:** 4x3px per pupil

```javascript
// Atualizar pupilas a cada frame de idle
nikolas.on('animationupdate', (anim, frame) => {
    if (anim.key === 'zema_idle') {
        const pupilValues = ['0.00', '1.25', '47.8', '0.00'];
        updatePupilDisplay(pupilValues[frame.index]);
    }
});
```

#### Calculator Pocket Flash (Idle)
- **Trigger:** Frame 1 e Frame 2
- **Effect:** Display verde pisca brevemente
- **Duration:** 60ms on, 65ms off
- **Color:** #00FF41 at 40% opacity
- **Size:** 8x4px area no bolso do paleto

#### Ambient Dollar Sign (Idle Frame 3)
- **Type:** Single particle spawn
- **Spawn:** Near hand position
- **Size:** 3x3px
- **Color:** #FFD700 at 30% opacity
- **Lifespan:** 200ms (appear and vanish quickly)
- **Frequency:** Once per idle cycle (every 500ms)

---

### Animation: `zema_walk`
- **Type:** Loop
- **Frames:** [0, 1, 2, 3, 4, 5]
- **Frame Rate:** 10 fps
- **Frame Durations (individual):**
  - Frame 0 (stride L): 100ms
  - Frame 1 (neutral): 100ms
  - Frame 2 (stride R): 100ms
  - Frame 3 (neutral): 100ms
  - Frame 4 (stride L): 100ms
  - Frame 5 (complete): 100ms
- **Total Cycle:** 600ms
- **Repeat:** -1 (infinite loop)
- **Description:** Caminhada MEDIDA e EFICIENTE. Passadas exatas, postura ereta, nenhum desperdicio de energia. Onde os pes tocam, minusculos cifroes aparecem e desaparecem. Expressao NUNCA muda durante a caminhada (perturbador).

```javascript
this.anims.create({
    key: 'zema_walk',
    frames: this.anims.generateFrameNumbers('zema_walk', { start: 0, end: 5 }),
    frameRate: 10,
    repeat: -1
});
```

#### Footstep Dollar Signs (Walk)
- **Trigger:** Frame 0 e Frame 2 (quando pe toca o chao)
- **Effect:** Minusculo cifrao ($) aparece onde o pe pisa
- **Size:** 4x4px
- **Color:** #FFD700 at 50% opacity
- **Lifespan:** 300ms (fade in 50ms, hold 150ms, fade out 100ms)
- **Position:** Offset -2px Y de cada pe (atras)

```javascript
// Footstep dollar effect
zema.on('animationupdate', (anim, frame) => {
    if (anim.key === 'zema_walk' && (frame.index === 0 || frame.index === 2)) {
        const dollar = this.add.sprite(zema.x, zema.y + 4, 'fx_dollar_small');
        dollar.setAlpha(0);
        dollar.setScale(0.5);
        this.tweens.add({
            targets: dollar,
            alpha: { from: 0, to: 0.5 },
            scale: { from: 0.5, to: 0.8 },
            duration: 50,
            yoyo: false,
            hold: 150,
            onComplete: () => {
                this.tweens.add({
                    targets: dollar,
                    alpha: 0,
                    duration: 100,
                    onComplete: () => dollar.destroy()
                });
            }
        });
    }
});
```

#### Passive Privatization (Walk Frame 4)
- **Trigger:** Frame 4 SE houver objeto de cenario proximo (raio 24px)
- **Effect:** Cifrao ($) aparece sobre o objeto proximo por 400ms
- **Size:** 6x6px
- **Color:** #FFD700 at 60% opacity
- **Animation:** Pop in (scale 0 -> 1.0, 80ms) then fade out (300ms)

---

### Animation: `zema_attack`
- **Type:** Play once
- **Frames:** [0, 1, 2]
- **Frame Rate:** 10 fps
- **Frame Durations (individual):**
  - Frame 0 (draw calculator): 150ms -- elegante, como sacar uma arma
  - Frame 1 (privatization strike): 133ms -- disparo dos cifroes
  - Frame 2 (holster): 133ms -- guardar com compostura
- **Total Duration:** ~416ms
- **Repeat:** 0 (play once)
- **On Complete:** Return to `zema_idle`
- **Description:** Zema saca a calculadora do bolso como quem saca uma arma. Cifroes ($) disparam como projeteis. Alvo recebe selo "PRIVATIZADO". Tudo com calma fria.

```javascript
this.anims.create({
    key: 'zema_attack',
    frames: [
        { key: 'zema_attack', frame: 0, duration: 150 },
        { key: 'zema_attack', frame: 1, duration: 133 },
        { key: 'zema_attack', frame: 2, duration: 133 }
    ],
    frameRate: 10,
    repeat: 0
});
```

#### Dollar Sign Projectiles (Frame 1)
- **Type:** Burst emitter from calculator position
- **Count:** 3-4 cifroes
- **Direction:** Cone toward target, 30 degree spread
- **Speed:** 150-220 px/s
- **Size:** 6x6px each
- **Color:** #FFD700 with #B8860B shadow
- **Rotation:** Each cifrao spins 360 deg over lifespan
- **Lifespan:** 400ms
- **Alpha:** 1.0, fading in last 100ms

```javascript
const dollarBurst = this.add.particles(zema.x + 16, zema.y, 'fx_dollar_projectile', {
    speed: { min: 150, max: 220 },
    angle: { min: targetAngle - 15, max: targetAngle + 15 },
    rotate: { min: 0, max: 360 },
    alpha: { start: 1, end: 0 },
    scale: { start: 1, end: 0.6 },
    lifespan: 400,
    quantity: 4,
    emitting: false
});
dollarBurst.explode();
```

#### "PRIVATIZADO" Stamp (On Hit)
- **Spawn:** At target position
- **Size:** 32x16px
- **Rotation:** Random +-10 degrees (rubber stamp imperfection)
- **Color:** #CC0000
- **Animation:** Slam in (scale 2.0 -> 1.0, 60ms, ease Bounce) then hold 1500ms then fade out (500ms)
- **Depth:** 9999

```javascript
const stamp = this.add.sprite(target.x, target.y - 8, 'fx_privatizado_stamp');
stamp.setScale(2.0);
stamp.setRotation(Phaser.Math.FloatBetween(-0.17, 0.17));
stamp.setDepth(9999);
this.tweens.add({
    targets: stamp,
    scale: 1.0,
    duration: 60,
    ease: 'Bounce.easeOut',
    onComplete: () => {
        this.time.delayedCall(1500, () => {
            this.tweens.add({
                targets: stamp,
                alpha: 0,
                duration: 500,
                onComplete: () => stamp.destroy()
            });
        });
    }
});
```

#### Calculator Draw Sound Sync
- **0ms:** Fabric rustle (saca do bolso)
- **50ms:** Calculator button click (liga)
- **150ms:** Cash register "ka-ching" (cifroes disparam)
- **283ms:** Stamp slam sound (selo PRIVATIZADO)

---

### Animation: `zema_death`
- **Type:** Play once
- **Frames:** [0, 1, 2, 3]
- **Frame Rate:** 6 fps (lento para drama)
- **Frame Durations (individual):**
  - Frame 0 (first wrinkle): 200ms -- o HORROR de perder a compostura
  - Frame 1 (falling): 166ms
  - Frame 2 (ground): 200ms
  - Frame 3 (CEO death): 300ms -- hold final longo
- **Total Duration:** ~866ms
- **Repeat:** 0 (play once)
- **On Complete:** Freeze on frame 3
- **Description:** A morte mais dramatica: o terno DESALINHA pela primeira vez. A calculadora cai. O cabelo desmancha. Os numeros nas pupilas apagam. A frieza finalmente quebra -- nao com gritos, mas com silencio.

```javascript
this.anims.create({
    key: 'zema_death',
    frames: [
        { key: 'zema_death', frame: 0, duration: 200 },
        { key: 'zema_death', frame: 1, duration: 166 },
        { key: 'zema_death', frame: 2, duration: 200 },
        { key: 'zema_death', frame: 3, duration: 300 }
    ],
    frameRate: 6,
    repeat: 0
});
```

#### Suit Wrinkle Effect (Frame 0)
- **Visual:** Micro-deformation on suit sprite
- **Method:** Slight skew tween (skewX: 0 -> 0.05) applied to character sprite
- **Duration:** 100ms
- **This is THE MOMENT** -- a ruga no terno e o equivalente ao grito de morte de outro personagem

#### Calculator Drop (Frame 1)
- **Type:** Separate sprite detaches and falls
- **Start:** Pocket position (zema.x + 8, zema.y - 4)
- **End:** Ground (zema.x + 12, zema.y + 8)
- **Rotation:** 0 -> 180 degrees (tumble)
- **Duration:** 200ms
- **Bounce:** Small bounce on landing (4px up, 60ms)
- **Display:** Random numbers flickering then "ERROR"

```javascript
const calc = this.add.sprite(zema.x + 8, zema.y - 4, 'fx_calculator_dropped');
this.tweens.add({
    targets: calc,
    x: zema.x + 12,
    y: zema.y + 8,
    angle: 180,
    duration: 200,
    ease: 'Bounce.easeOut'
});
```

#### Dollar Signs Falling (Frames 1-3)
- **Type:** Dollar signs around Zema lose their gold and fall
- **Effect:** Color shift #FFD700 -> #808080 (gold to gray)
- **Movement:** Drift downward with gravity (80 px/s^2)
- **Alpha:** 1.0 -> 0
- **Count:** 5-8 dollars falling
- **Meaning:** "De-privatizacao" -- tudo que ele privatizou se desfaz

#### Pupil LED Fade (Frames 2-3)
- **Frame 2:** Green LED (#00FF41) dimming to (#005510)
- **Frame 3:** LED completely off (black #000000)

#### Excel Spreadsheet Shadow (Frame 3 - Easter Egg)
- **Type:** Ground shadow under body
- **Detail:** Shadow has subtle grid pattern (like Excel cells)
- **Size:** 40x20px
- **Opacity:** 15-20% (barely visible, reward for observant players)

---

### Animation: `zema_hit`
- **Type:** Play once
- **Frames:** [0, 1]
- **Frame Rate:** 12 fps (rapido -- ele se recompoe IMEDIATAMENTE)
- **Frame Durations:**
  - Frame 0 (recoil): 83ms -- o mais rapido possivel
  - Frame 1 (recompose): 100ms -- JA restaurado
- **Total Duration:** ~183ms (MAIS RAPIDO que qualquer outro personagem)
- **Repeat:** 0
- **On Complete:** Return to previous animation
- **Description:** Zema recua minimamente, micro-ruga aparece e desaparece, pupilas mostram incompreensao ("?!?"), e ele se recompoe MAIS RAPIDO que qualquer outro personagem. A recomposicao instantanea e o poder dele.

```javascript
this.anims.create({
    key: 'zema_hit',
    frames: [
        { key: 'zema_hit', frame: 0, duration: 83 },
        { key: 'zema_hit', frame: 1, duration: 100 }
    ],
    frameRate: 12,
    repeat: 0
});
```

#### Composure Restoration (Frame 1)
- **Effect:** Subtle "snap back" -- character tween from slight offset back to perfect center
- **Duration:** 50ms
- **Ease:** Elastic (slight overshoot then settle)
- **Message:** "Tudo sera contabilizado"

---

### Animation: `zema_special`
- **Type:** Play once
- **Name:** "PRIVATIZACAO EM MASSA" / "SERA?"
- **Frames:** [0, 1, 2, 3, 4, 5, 6, 7]
- **Frame Rate:** 8 fps
- **Frame Durations (individual):**
  - Frame 0 (prep): 125ms
  - Frame 1 (TikTok pose): 150ms -- held for comedic beat
  - Frame 2 (wave start): 125ms
  - Frame 3 (wave max): 175ms -- held for gameplay readability
  - Frame 4 (TikTok step): 150ms -- held for second comedic beat
  - Frame 5 (pricing): 175ms -- held for score drain readability
  - Frame 6 (retract): 100ms
  - Frame 7 (reset): 100ms
- **Total Duration:** ~1100ms
- **Repeat:** 0
- **On Complete:** Return to `zema_idle`
- **Cooldown:** 12000ms
- **Description:** O ultimate do Zema. Combina a danca "Sera?" do TikTok com uma onda de privatizacao que drena pontos do jogador. Tudo ao redor fica "privatizado" e cobra preco. A danca no meio e PERTURBADORA no contexto de apocalipse zumbi.

```javascript
this.anims.create({
    key: 'zema_special',
    frames: [
        { key: 'zema_special', frame: 0, duration: 125 },
        { key: 'zema_special', frame: 1, duration: 150 },
        { key: 'zema_special', frame: 2, duration: 125 },
        { key: 'zema_special', frame: 3, duration: 175 },
        { key: 'zema_special', frame: 4, duration: 150 },
        { key: 'zema_special', frame: 5, duration: 175 },
        { key: 'zema_special', frame: 6, duration: 100 },
        { key: 'zema_special', frame: 7, duration: 100 }
    ],
    frameRate: 8,
    repeat: 0
});
```

#### Golden Privatization Wave (Frames 2-6)
- **Type:** Expanding circle ground overlay
- **Frame 2:** Radius 0 -> 30px (initial burst)
- **Frame 3:** Radius 30 -> 100px (maximum expansion)
- **Frame 4-5:** Radius holds at 100px (pulsing)
- **Frame 6:** Radius 100 -> 50px (retracting)
- **Color:** #FFD700 at 40% opacity, dollar sign pattern
- **Blend Mode:** MULTIPLY
- **Depth:** Below characters, above ground tiles

```javascript
const privWave = this.add.circle(zema.x, zema.y, 0, 0xFFD700, 0.4);
privWave.setDepth(zema.depth - 1);

// Expand
this.tweens.add({
    targets: privWave,
    radius: 100,
    duration: 300,
    ease: 'Cubic.easeOut',
    hold: 500,
    onComplete: () => {
        // Retract
        this.tweens.add({
            targets: privWave,
            radius: 0,
            alpha: 0,
            duration: 200,
            onComplete: () => privWave.destroy()
        });
    }
});
```

#### Object Privatization (Frames 3-6)
- **Trigger:** Any scenery object within wave radius
- **Effect per object:**
  1. Dollar sign ($) appears above object (pop in, 80ms)
  2. "PRIVATIZADO" stamp appears (slam, 60ms)
  3. Price tag appears ("R$ XX", where XX = object value)
- **Score Drain:** Player loses points equal to sum of all prices

#### TikTok Dance Audio (Frames 1 and 4)
- **Frame 1:** Quick beat/jingle (200ms, catchy but WRONG in context)
- **Frame 4:** Second beat (continuation of the disturbing dance)

#### "SERA?" Text (Frame 1)
- **Spawn:** Above Zema's head
- **Text:** "Sera?" in italic, with question mark emphasized
- **Style:** Comic font, but cleaner than other onomatopeias (fits his character)
- **Color:** White with dark blue shadow
- **Duration:** 400ms (pop in, hold, fade)

---

## Sound Cue Timing

| Time (ms) | Animation     | Event                    | Sound Key                    | Notes                                 |
|------------|---------------|--------------------------|------------------------------|---------------------------------------|
| 0          | attack        | Draw calculator          | `sfx_zema_draw`              | Fabric rustle + button click          |
| 150        | attack        | Dollar projectiles       | `sfx_cash_register`          | Ka-ching cash register                |
| 283        | attack        | PRIVATIZADO stamp        | `sfx_stamp_slam`             | Heavy rubber stamp impact             |
| 0          | death         | First wrinkle            | `sfx_fabric_tear`            | Subtle fabric tearing sound           |
| 200        | death         | Calculator drop          | `sfx_calc_drop`              | Plastic on floor + button sounds      |
| 566        | death         | LED eyes off             | `sfx_power_down`             | Electronic power-down whine           |
| 0          | hit           | Recoil                   | `sfx_zema_hmm`               | Cold "Hmm" of disapproval             |
| 0          | special       | Preparation              | `sfx_zema_sera`              | "Sera?" voice clip                    |
| 150        | special       | TikTok pose              | `sfx_tiktok_beat`            | Short catchy beat                     |
| 275        | special       | Wave expanding           | `sfx_gold_wave`              | Shimmering golden sweep               |
| 450        | special       | Maximum privatization    | `sfx_cash_shower`            | Many cash registers overlapping       |
| 600        | special       | TikTok step 2            | `sfx_tiktok_beat_2`          | Second beat                           |
| 775        | special       | Score drain              | `sfx_coins_drain`            | Coins draining sound                  |

### Sound Descriptions
- **`sfx_zema_draw`:** (150ms) Soft fabric rustle + single calculator button click. Elegant, like drawing a weapon.
- **`sfx_cash_register`:** (200ms) Classic "ka-ching" cash register sound. Brass bell + mechanism.
- **`sfx_stamp_slam`:** (150ms) Heavy rubber stamp hitting paper. Authoritative, final.
- **`sfx_fabric_tear`:** (100ms) Subtle fabric stress sound. Not a full tear -- just the THREAT of one.
- **`sfx_calc_drop`:** (250ms) Plastic calculator hitting floor. Buttons clicking randomly on impact.
- **`sfx_power_down`:** (400ms) Electronic whine descending in pitch. LED dying sound.
- **`sfx_zema_hmm`:** (200ms) Cold, controlled "Hmm" of disapproval. Male, composed, slightly threatening.
- **`sfx_zema_sera`:** (400ms) "Sera?" spoken calmly with slight questioning lilt. Not uncertain -- rhetorical.
- **`sfx_gold_wave`:** (300ms) Shimmering metallic sweep. Gold coins sliding. Magical but corporate.
- **`sfx_cash_shower`:** (500ms) Multiple cash registers firing simultaneously. Chaotic wealth.
- **`sfx_coins_drain`:** (400ms) Coins being sucked away. Descending metallic tinkle. Loss.

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
- **Shape:** Rectangle (retangular -- combina com postura rigida)
- **Size:** 24x28px (centered on character)
- **Attack Hitbox:** Cone, 30 degree angle, 60px range (cifroes voam reto)
- **Special Hitbox:** Circle, 100px radius (onda de privatizacao)

### Y-Sort Depth
```javascript
zema.setDepth(zema.y);
```

### Mini-Boss Behavior Notes
- Zema e um MINI-BOSS: mais HP que NPCs normais, pattern de ataque previsivel
- Fase 1 (HP > 50%): Caminha e ataca com calculadora, calmo
- Fase 2 (HP 30-50%): Acelera ataques, comeca a privatizar objetos do cenario
- Fase 3 (HP < 30%): Usa Special "Privatizacao em Massa" + "Sera?"
- NUNCA foge, NUNCA grita, NUNCA perde a compostura (ate a morte)
- Ao ser derrotado: todos os objetos que ele privatizou voltam ao normal
- Drop: Calculadora Infernal (arma coletavel)
