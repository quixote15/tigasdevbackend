# BOLSONARO (O Mito) -- Animation Specification

## Technical Baseline
- **Engine:** Phaser 3
- **Frame Dimensions:** 64x64px
- **Target Frame Rate:** 8-12 fps (jerky Andre Guedes style -- intentionally NOT smooth)
- **Easing:** SteppedEase for most animations (preserves jerky feel). Linear only for particle movement.
- **Sprite Rendering:** Nearest-neighbor scaling (NO anti-aliasing, NO smoothing)
- **Y-Sort Anchor:** Bottom-center (32, 60)

---

## 1. IDLE ANIMATION

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 500ms (2 fps effective per frame transition) |
| Frames           | 4 (0, 1, 2, 3)  |
| Frame Duration   | 125ms each       |
| Loop Mode        | Ping-pong (0-1-2-3-2-1-0...) |
| FPS              | 8                |
| Easing           | SteppedEase(4)   |
| Repeat           | -1 (infinite)    |

### Frame Timing Breakdown
```
0ms    -- Frame 0: "Talkei Stance" (base pose, chin forward, thumbs up)
125ms  -- Frame 1: "Chin Jut" (chin extends +2px, chest inflates)
250ms  -- Frame 2: "Belly Breath" (belly inflates, scar stretches)
375ms  -- Frame 3: "Restless Gunhand" (gun lifts, paranoid glance)
500ms  -- Frame 2 (reverse): Belly deflating
625ms  -- Frame 1 (reverse): Chin returning
750ms  -- Frame 0 (restart): Base pose
```

### Particle Effects
| Effect           | Trigger        | Duration | Properties                           |
|------------------|----------------|----------|--------------------------------------|
| Sweat drop       | Frame 0, 2     | 300ms    | 1px white pixel, gravity fall from temple, alpha fade 1.0->0.0 |
| Gun glint        | Frame 3        | 100ms    | 1px white flash on revolver barrel, instant appear/fade |
| Chin wobble line | Frame 3        | 200ms    | 1px dark line under chin, horizontal oscillation +/-1px |

### Sound Sync
| Timing   | Sound                    | Volume | Notes                                |
|----------|--------------------------|--------|--------------------------------------|
| 0ms      | `bolsonaro_idle_breath`  | 0.2    | Subtle nasal breathing loop, heavy   |
| Random (every 8-15s) | Random bordao  | 0.6    | See bordoes-bolsonaro.md for pool    |
| Frame 3 (every 3rd cycle) | `gun_click_soft` | 0.15 | Subtle gun fidget click           |

---

## 2. WALK ANIMATION

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 600ms            |
| Frames           | 6 (0-5)         |
| Frame Duration   | 100ms each       |
| Loop Mode        | Cyclic (0-1-2-3-4-5-0...) |
| FPS              | 10               |
| Easing           | SteppedEase(6)   |
| Repeat           | -1 (while moving)|

### Frame Timing Breakdown
```
0ms    -- Frame 0: Right step forward (dust cloud spawns)
100ms  -- Frame 1: Right foot plants (SQUASH: scaleY 0.95, scaleX 1.05 for 50ms)
200ms  -- Frame 2: Mid-stride peak (STRETCH: scaleY 1.05, scaleX 0.95 for 50ms)
300ms  -- Frame 3: Left step forward (dust cloud spawns)
400ms  -- Frame 4: Left foot plants (SQUASH: scaleY 0.95, scaleX 1.05 for 50ms)
500ms  -- Frame 5: Mid-stride return (STRETCH: scaleY 1.05, scaleX 0.95 for 50ms)
600ms  -- Loop restart
```

### Squash & Stretch Tween
```javascript
// Applied on foot-plant frames (1, 4)
this.tweens.add({
    targets: sprite,
    scaleX: 1.05,
    scaleY: 0.95,
    duration: 50,
    ease: 'Quad.easeOut',
    yoyo: true
});
```

### Particle Effects
| Effect           | Trigger        | Duration | Properties                           |
|------------------|----------------|----------|--------------------------------------|
| Dust puff        | Frame 0, 3     | 250ms    | 3x3px tan (#C4A882) cloud at foot position, alpha 0.6->0.0, scale 1.0->1.5 |
| Belly jiggle     | Frame 1, 4     | 150ms    | Belly sprite region oscillates +/-1px horizontal, damped sine |
| Chin motion line | Frame 2, 5     | 100ms    | 1px white line trailing chin, 40% opacity, horizontal, 4px long |
| Sweat trail      | Frame 3        | 400ms    | 1px blue pixel detaches from forehead, parabolic arc, gravity fall |
| Faixa flutter    | All frames     | Continuous| Presidential sash sways +/-2px, sine wave, 300ms period |

### Sound Sync
| Timing   | Sound                    | Volume | Notes                                |
|----------|--------------------------|--------|--------------------------------------|
| Frame 1  | `step_heavy_R`           | 0.4    | Heavy boot stomp, right foot         |
| Frame 4  | `step_heavy_L`           | 0.4    | Heavy boot stomp, left foot          |
| Frame 0-5| `faixa_cloth_rustle`     | 0.1    | Continuous subtle cloth sound         |
| Frame 2  | `belly_jiggle_subtle`    | 0.08   | Faint flesh wobble (grotesque detail)|

### Movement Speed
- **Walk speed:** 80 px/s
- **Boss multiplier:** 0.7x (boss walks slower: 56 px/s effective)
- **Enraged multiplier:** 1.3x (when below 30% HP: 72.8 px/s)

---

## 3. ATTACK ANIMATION -- "Arma que Brocha"

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 450ms (SUCCESS) / 700ms (FAIL) |
| Frames           | 3 (0, 1 or 2)   |
| Frame 0 Duration | 200ms            |
| Frame 1 Duration | 150ms (success)  |
| Frame 2 Duration | 500ms (fail)     |
| Loop Mode        | None (play once) |
| FPS              | 10               |
| Cooldown         | 800ms            |

### Frame Timing Breakdown -- SUCCESS PATH (70%)
```
0ms    -- Frame 0: "Draw/Aim" (200ms hold)
         - Body leans back, gun raised, cowboy squint
         - SFX: gun_cock at 50ms
200ms  -- Frame 1: "Fire SUCCESS" (150ms hold)
         - Muzzle flash spawns at 200ms
         - Recoil tween: body.x -= 3px over 80ms, bounce back over 70ms
         - Screen shake: intensity 2, duration 100ms
         - SFX: gun_fire_loud at 200ms
         - SFX: shell_casing_tink at 280ms
350ms  -- Return to idle
         - Smoke particles linger for 400ms
```

### Frame Timing Breakdown -- FAIL PATH (30%)
```
0ms    -- Frame 0: "Draw/Aim" (200ms hold) -- IDENTICAL to success
         - SFX: gun_cock at 50ms
200ms  -- Frame 2: "Fire FAIL / Brocha" (500ms hold)
         - Gun droop tween: gun sprite rotates -30deg over 200ms, ease Quad.easeIn
         - Pathetic puff particle at 200ms (gray cloud, 4x4px, 300ms lifespan)
         - Self-damage flash: body tints red (#FF0000, 30% opacity) at 300ms for 150ms
         - "?" particle spawns above head at 350ms, floats up 8px over 200ms, fades
         - SFX: gun_click_empty at 200ms (dry metallic click)
         - SFX: sad_trombone_short at 350ms (0.3 volume)
         - SFX: talkei_sad at 500ms (0.5 volume, dejected "talkei?" voice)
700ms  -- Return to idle
         - Bolsonaro shakes head tween: rotation +/-3deg, 3 oscillations over 300ms
```

### Particle Effects
| Effect           | Trigger        | Duration | Properties                           |
|------------------|----------------|----------|--------------------------------------|
| Muzzle flash     | Frame 1 start  | 80ms     | 12x12px golden starburst at gun barrel tip. Scale 0.5->1.5->0.0. Additive blend. Colors: #FFD700 core, #FF6600 edge, #FFFFFF center point. |
| Bullet trail     | Frame 1 +30ms  | 200ms    | 2x1px golden rectangle, velocity 400px/s rightward, alpha 1.0->0.0. Spawn 3 at 30ms intervals. |
| Shell casing     | Frame 1 +60ms  | 500ms    | 2x2px #DAA520 pixel. Velocity: x +40px/s, y -80px/s initial. Gravity: 200px/s^2. Rotation: 720deg/s. Bounce once on ground. Alpha: hold 1.0 for 300ms, then 1.0->0.0. |
| Smoke wisps      | Frame 1 +100ms | 600ms    | 3x3px gray (#888888) cloud. Velocity: y -15px/s, x random +/-5px/s. Alpha: 0.4->0.0. Scale: 1.0->2.0. Spawn 3 particles. |
| Sad puff (fail)  | Frame 2 start  | 400ms    | 5x5px light gray (#CCCCCC) cloud. Velocity: y -8px/s. Alpha: 0.5->0.0. Scale: 1.0->0.5 (it SHRINKS -- even the smoke is pathetic). Comical sad-cloud shape. |
| Question mark    | Frame 2 +150ms | 350ms    | "?" character, 4px tall, yellow #FFD700. Float up 8px. Alpha: 0.0->1.0 over 100ms, hold 150ms, 1.0->0.0 over 100ms. |
| Self-damage flash| Frame 2 +100ms | 150ms    | Full-body red tint overlay. #FF0000 at 30% opacity. Instant on, fade to 0% over 150ms. |

### Damage Values
| Outcome  | Target  | Damage | Range      | Knockback |
|----------|---------|--------|------------|-----------|
| SUCCESS  | Enemy   | 35 HP  | 120px      | 8px       |
| FAIL     | Self    | 10 HP  | 0 (self)   | 0         |

### RNG Implementation
```javascript
const fireSuccess = Math.random() < 0.70; // 70% success, 30% fail
if (fireSuccess) {
    this.anims.play('bolsonaro_attack_success');
    // damage target
} else {
    this.anims.play('bolsonaro_attack_fail');
    // damage self
}
```

---

## 4. DEATH ANIMATION

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 1600ms           |
| Frames           | 4 (0-3)         |
| Frame Durations  | 200ms, 300ms, 400ms, hold |
| Loop Mode        | None (hold last frame) |
| FPS              | 8                |

### Frame Timing Breakdown
```
0ms     -- Frame 0: "Impact Hit" (200ms)
           - All accessories begin detaching
           - Blood particles spawn (3-4 red dots, random velocities outward)
           - SFX: death_impact_heavy at 0ms
           - SFX: gun_clatter at 100ms (revolver falling)
           - SFX: sunglasses_crack at 150ms
50ms    -- Body recoil tween: y -= 4px over 100ms (knocked upward)
100ms   -- Phone detach: spawn phone sprite at pocket position, velocity y -60px/s, x +20px/s, gravity 150px/s^2
150ms   -- Sunglasses detach: spawn sunglasses sprite at head position, velocity y -80px/s, x +30px/s, gravity 150px/s^2, rotation 360deg/s

200ms   -- Frame 1: "Falling" (300ms)
           - Body tilt tween: rotation 0->30deg over 300ms, ease Quad.easeIn
           - Revolver continues trajectory (further from body)
           - One shoe detaches at 250ms
           - SFX: body_fall_whoosh at 200ms (wind sound)
           - SFX: shoe_pop at 250ms
250ms   -- Shoe detach: spawn shoe sprite, velocity x +25px/s, y -40px/s, gravity 200px/s^2

500ms   -- Frame 2: "Floor Impact" (400ms)
           - SCREEN SHAKE: intensity 4, duration 200ms
           - Dust cloud particle burst (8x6px, 12 particles radiating outward)
           - Body SQUASH tween: scaleY 0.7, scaleX 1.3, duration 100ms, ease Bounce.easeOut, yoyo partial (settle at scaleY 0.85, scaleX 1.15)
           - Blood pool sprite fades in (alpha 0->0.6 over 400ms)
           - KO stars begin orbiting (3 yellow stars, 2px each, circular orbit radius 12px, speed 720deg/s)
           - SFX: body_slam_heavy at 500ms (LOUD impact)
           - SFX: chin_crunch at 520ms (comedic bone crunch -- chin hitting first)
           - SFX: glass_shatter_small at 550ms (phone screen cracking)
600ms   -- Sunglasses fragments land (3 separate 1px sprites, bounce once each)
700ms   -- Revolver lands 8px away, bounces once, barrel droops (rotation -30deg, ease Quad.easeOut)

900ms   -- Frame 3: "Final Defeated" (HOLD indefinitely)
           - KO stars slow: orbit speed 720deg/s -> 180deg/s over 2000ms, ease Quad.easeOut
           - Dust settles: remaining particles alpha -> 0 over 500ms
           - Blood pool at final size
           - All detached items at rest
           - Phone screen: "LIVE ENDED" text flickers (alpha oscillation 0.3-0.8 at 2Hz for 3s, then steady 0.5)
           - SFX: stars_chime_slow at 900ms (cartoony twinkle)
           - SFX: phone_static at 1000ms (brief digital noise)
           - SFX: crowd_distant_boo at 1200ms (distant booing, 0.15 volume, comedic)
```

### Accessory Physics (all detached items)
```javascript
// Generic detached accessory behavior
const accessory = {
    velocityX: initialVX,     // varies per item
    velocityY: initialVY,     // varies per item
    gravity: 180,             // px/s^2
    rotation: rotationSpeed,  // deg/s, varies per item
    bounce: 0.3,              // coefficient of restitution
    friction: 0.8,            // horizontal velocity multiplier on bounce
    fadeAfterBounce: true,    // alpha 1.0->0.3 after final bounce over 500ms
};
```

### Loot Drop (on death complete)
- Spawn after Frame 3 settles (at 1500ms)
- Drop items from body center with fountain physics
- Possible drops: Golden Revolver (weapon pickup), Faixa Fragment (collectible), Phone (intel item)

---

## 5. HIT ANIMATION

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 350ms            |
| Frames           | 2 (0, 1)        |
| Frame 0 Duration | 150ms            |
| Frame 1 Duration | 200ms            |
| Loop Mode        | None (return to previous anim) |
| FPS              | 12               |

### Frame Timing Breakdown
```
0ms    -- Frame 0: "Impact Flash" (150ms)
          - White flash: full body tint #FFFFFF at 40% opacity, fade to 0% over 100ms
          - Body knockback: x += 3px * hitDirection over 80ms, ease Quad.easeOut
          - Chin compress tween: chin region scaleY 0.8 over 80ms (chin retreats into neck!)
          - Sweat drops: 2 particles, 1px, velocity outward from forehead, gravity fall
          - SFX: hit_flesh_heavy at 0ms
          - SFX: gasp_angry at 50ms (sharp intake of breath)
80ms   -- Knockback settle: x returns 1px (net displacement: 2px in hit direction)

150ms  -- Frame 1: "Recovery Anger" (200ms)
          - Chin OVERCOMPENSATE tween: chin region scaleY 1.2 over 100ms (2px LARGER than normal)
          - Red rage aura: 1px red outline appears around body, alpha 0->0.2 over 100ms, hold 100ms, fade over 200ms
          - Veins pulse: 2-3 forehead vein pixels flash red (alpha 0->0.8->0 over 200ms)
          - Body puff: scaleX 1.02, scaleY 1.02 over 100ms (angry inflation), ease Back.easeOut
          - SFX: angry_growl at 150ms (guttural "grr")
          - SFX: cracking_knuckles at 250ms (subtle, 0.2 volume)
300ms  -- Chin settles at scaleY 1.05 (stays slightly larger than pre-hit -- rage residue)

350ms  -- Return to previous animation state
          - Chin scaleY tweens back to 1.0 over 500ms (slow anger cooldown)
```

### Damage Number Display
```
- Spawn at body center + offset (0, -20px)
- Float upward: y -= 30px over 600ms
- Scale: 1.0 -> 1.3 over 100ms, then 1.3 -> 1.0 over 200ms (pop effect)
- Alpha: 1.0 hold 400ms, then 1.0 -> 0.0 over 200ms
- Color: #FF0000 for normal damage, #FFD700 for critical
- Font: thick pixel font, 8px height
- Slight random x offset: +/- 4px (prevents stacking)
```

---

## HUMAN FORM ANIMATIONS

> As animacoes abaixo se aplicam a **Versao Humana** do Bolsonaro -- corpo magricela com ponchete de cerveja, AK-47 como arma, tons de pele humana, e personalidade covarde. Todas usam o mesmo frame size (64x64px), mesma perspectiva isometrica, e mesmo estilo Andre Guedes grotesco. A versao humana existe ANTES da Mordida Zumbi transformar o personagem na versao default (zumbi).

### H1. IDLE (Humano) -- "Medo Disfarçado"

#### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 500ms            |
| Frames           | 4 (0, 1, 2, 3)  |
| Frame Duration   | 125ms each       |
| Loop Mode        | Ping-pong (0-1-2-3-2-1-0...) |
| FPS              | 8                |
| Easing           | SteppedEase(4)   |
| Repeat           | -1 (infinite)    |

#### Frame Timing Breakdown
```
0ms    -- Frame 0: "Medo Base" (corpo magricela, AK-47 no peito, olhos arregalados)
         - Ponchete de cerveja em posicao neutra, cicatriz esticada
         - AK-47 segurada na altura do peito, knuckles brancos de apertar
         - Olhos ABERTOS demais, pupilas pequenas, brancos visiveis
         - Sorriso forcado mas com MEDO atras -- dentes cerrados de tensao
         - 2-3 gotas de suor (1px cada) na testa e temporas
125ms  -- Frame 1: "Olhada Esquerda" (cabeca gira 2px para esquerda, olhos ARREGALADOS)
         - Queixao gira junto mas TREME (1px jitter line)
         - AK-47 acompanha a olhada, cano aponta ligeiramente a esquerda
         - Ponchete balanca 1px na direcao oposta (peso da barriga com delay)
         - Ombros sobem 1px (tensao aumenta)
         - Uma gota de suor CATA do temple (1px, trajetoria parabolica)
250ms  -- Frame 2: "Ponchete Respira" (barriga INFLA grotescamente com respiracao nervosa)
         - Ponchete expande 3px para fora (respiracao ofegante, mais intensa que o zumbi)
         - Cicatriz ESTICA visivelmente -- pixels do scar se separam 1px
         - AK-47 sobe/desce com a respiracao (cano treme)
         - Olhos voltam ao centro mas MAIS ARREGALADOS
         - Boca abre 1px -- hiperventilacao visivel
         - Suor acumula (mais 1-2 gotas novas)
375ms  -- Frame 3: "Checagem Paranoica" (cabeca gira 2px para DIREITA, corpo encolhe)
         - AK-47 aponta para direita, finger PERTO do gatilho (trigger discipline = zero)
         - Ponchete desinfla voltando ao normal, jiggle residual
         - Um olho MAIS ABERTO que o outro (paranoia assimetrica, igual ao zumbi)
         - Joelhos flexionam 1px (pronto para correr, nao para lutar)
         - Queixao aponta para a direita mas SEM a confianca do zumbi
500ms  -- Loop restart (ping-pong reverso)
```

#### Particle Effects
| Effect           | Trigger        | Duration | Properties                           |
|------------------|----------------|----------|--------------------------------------|
| Suor cronico     | Todos os frames| 300ms    | 1px gotas brancas/azuis, caem da testa, 3-4 ativas simultaneamente. Mais suor que o zumbi -- ele esta CONSTANTEMENTE suando. |
| Ponchete wobble  | Frame 0, 2     | 200ms    | Regiao da barriga oscila +/-2px horizontal, sine amortecido. Mais pronunciado que o belly jiggle do zumbi porque a barriga e mais solta. |
| AK-47 tremble    | Frame 1, 3     | Continuo | Cano da AK-47 treme 1px random (x e y). A arma e pesada demais para o corpo magricela. |
| Gun click nervoso| Frame 3 (a cada 2 ciclos) | 50ms | 1px flash no safety switch -- ele fica tirando e colocando a trava por nervosismo. |

#### Sound Sync
| Timing   | Sound                    | Volume | Notes                                |
|----------|--------------------------|--------|--------------------------------------|
| 0ms      | `bolsonaro_human_breath_nervous` | 0.3 | Respiracao ofegante, mais rapida que a versao zumbi |
| Random (cada 5-10s) | `bolsonaro_human_gulp` | 0.4 | Engolir seco de medo |
| Frame 3 (a cada 3 ciclos) | `ak47_safety_click` | 0.1 | Click metalico da trava |

---

### H2. WALK (Humano) -- "Corrida Covarde"

#### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 600ms            |
| Frames           | 6 (0-5)         |
| Frame Duration   | 100ms each       |
| Loop Mode        | Cyclic (0-1-2-3-4-5-0...) |
| FPS              | 10               |
| Easing           | SteppedEase(6)   |
| Repeat           | -1 (while moving)|

#### Frame Timing Breakdown
```
0ms    -- Frame 0: Passo direito cauteloso (passo CURTO, 3px ao inves dos 4px do zumbi)
         - AK-47 sweep: cano varre para a esquerda, checando flancos
         - Ponchete bounce: barriga inicia o upswing (+1px)
         - Dust cloud MENOR que o zumbi (1x1px, ele pisa mais leve por ser magricela)
         - Ombros curvados, cabeça baixa (tentando parecer pequeno)
         - Queixao ainda lidera mas SEM a confianca -- parece mais um tartaruga esticando o pescoco
100ms  -- Frame 1: Pé direito planta (SQUASH mais sutil: scaleY 0.97, scaleX 1.03)
         - Ponchete DESCE com impacto -- a barriga chega atrasada, jiggle de 2px para baixo
         - AK-47 absorve impacto, cano wobble
         - Cicatriz shift com a pele da barriga
         - Impacto mais LEVE que o zumbi (corpo mais magro = menos peso)
200ms  -- Frame 2: Meio do passo (corpo no ponto mais alto)
         - AK-47 sweep: cano varre para a DIREITA
         - Ponchete no centro, pendulando
         - Olhos fazem SCAN rapido (pupilas movem 2px de um lado para o outro em 100ms)
         - Queixao no ponto maximo frontal mas com micro-tremble
300ms  -- Frame 3: Passo esquerdo cauteloso
         - Mirror do Frame 0
         - AK-47 sweep inverte direcao
         - Ponchete bounce restart
         - Gota de suor destaca da testa (1px, arco parabolico para cima e para tras)
400ms  -- Frame 4: Pé esquerdo planta
         - Mirror do Frame 1
         - Ponchete jiggle para a ESQUERDA neste impacto
500ms  -- Frame 5: Meio do passo retorno
         - Mirror do Frame 2
         - Lingua lambida rapida nos labios (1px pink, mesmo tic nervoso do zumbi)
         - AK-47 magazine rattle (1px movement no magazine -- a arma esta SOLTA, mal montada)
600ms  -- Loop restart
```

#### Diferencas-chave vs Walk Zumbi
| Aspecto | Walk Zumbi | Walk Humano |
|---------|-----------|-------------|
| Postura | Peito estufado, chin-first STRUT | Curvado, cauteloso, tentando parecer pequeno |
| Passo | 4px, pesado, arrogante | 3px, leve, tatical |
| Arma | Revolver no quadril, casual | AK-47 no peito, varrendo, nervosa |
| Barriga | Belly jiggle discreto (barril) | Ponchete BOUNCE pronunciado (barriga solta) |
| Confianca | 100% -- ele acha que e dono do lugar | 0% -- ele sabe que esta ferrado |
| Dust clouds | 3x3px (peso) | 1x1px (leve) |

#### Movement Speed
- **Walk speed:** 80 px/s (full speed -- nao tem penalidade de zumbificacao)
- **Sprint multiplier:** 1.2x (96 px/s -- corrida de panico por 3s, cooldown 8s)
- **Fear boost:** Quando abaixo de 20% HP, 1.4x (112 px/s -- adrenalina de covarde)

---

### H3. ATTACK -- AK-47 "Fuzil que Brocha" (Humano)

#### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 500ms (SUCCESS) / 800ms (FAIL) |
| Frames           | 3 (0, 1 ou 2)   |
| Frame 0 Duration | 200ms            |
| Frame 1 Duration | 200ms (success)  |
| Frame 2 Duration | 600ms (fail)     |
| Loop Mode        | None (play once) |
| FPS              | 10               |
| Cooldown         | 600ms            |

#### Frame Timing Breakdown -- SUCCESS PATH (60%)
```
0ms    -- Frame 0: "Apontar Tremendo" (200ms hold)
         - Corpo magricela tenta firmar a AK-47 no ombro
         - Ombros estreitos MAL SEGURAM o rifle -- stock escorrega no ombro ossudo
         - Ponchete aperta contra o rifle (barriga atrapalha a mira)
         - Olhos FECHAM por antecipacao (ele tem MEDO do recoil)
         - Queixao cerra, dentes TRINCADOS de tensao
         - SFX: ak47_cock at 80ms (som metalico de armar)
         - SFX: nervous_exhale at 150ms
200ms  -- Frame 1: "Rajada SUCCESS" (200ms hold)
         - AK-47 MUZZLE FLASH: starburst alaranjado (#FF8800 core, #FFFFFF center, mais AGRESSIVO que o flash dourado do revolver)
         - Burst fire: 3 casings ejetam em sequencia rapida (a cada 40ms)
         - RECOIL MAXIMO: corpo magricela e empurrado 5px para tras (mais que os 3px do zumbi -- menos massa corporal)
         - Ponchete SACOLEJA violentamente com o recoil
         - Pes arrastam no chao (marcas de arrasto, 2px cada)
         - Olhos ABREM de susto com o barulho
         - Boca abre num GRITO involuntario
         - Faixa voa horizontal
         - Screen shake: intensity 3, duration 120ms (mais intenso que o revolver)
         - SFX: ak47_burst_fire at 200ms (rajada curta, 3 tiros)
         - SFX: brass_rain at 240ms (casings caindo)
         - SFX: bolsonaro_human_yelp at 250ms (grito de susto)
400ms  -- Return to idle
         - Fumaca da AK-47 persiste por 500ms
         - Corpo se recompoe tremendo
```

#### Frame Timing Breakdown -- FAIL/BROCHA PATH (40%)
```
0ms    -- Frame 0: "Apontar Tremendo" (200ms hold) -- IDENTICO ao success
         - SFX: ak47_cock at 80ms
200ms  -- Frame 2: "TRAVOU / BROCHA DA AK" (600ms hold)
         - AK-47 faz um CLICK patetico -- sem flash, sem tiro
         - Casing PRESO no ejection port (2x2px brass pixel travado em 45 graus, visivel)
         - Fumaca cinza triste (#AAAAAA, 40% opacity) sai do cano -- nuvem patetica em forma de "suspiro"
         - Expressao de PANICO TOTAL: olhos ENORMES, boca aberta de horror, queixao TREME
         - Ambas as maos SACODEM o rifle tentando destravar (classic AK slap)
           - Tween: rifle shake horizontal +/-3px a 20Hz por 300ms
         - Auto-dano: mao bate no receptor metalico (flash vermelho na mao, 30% opacity)
         - Ponchete balanca com a sacudida frenetica
         - "?!?!" spawn acima da cabeça (5px, amarelo, flutua 8px, fade)
         - SFX: ak47_jam_click at 200ms (click seco, metalico, patetico)
         - SFX: bolsonaro_human_panic at 300ms ("NAO NAO NAO" murmurado)
         - SFX: metal_slap at 400ms (mao batendo no rifle)
         - SFX: sad_trombone_short at 600ms (0.3 volume)
800ms  -- Return to idle
         - Bolsonaro olha para a AK-47 com traicao pessoal
         - Head shake tween: rotation +/-3deg, 2 oscilacoes, 200ms
```

#### Damage Values
| Outcome  | Target  | Damage | Range      | Knockback | Notes |
|----------|---------|--------|------------|-----------|-------|
| SUCCESS  | Enemy   | 28 HP  | 160px      | 6px       | Menos dano mas MAIS alcance que o revolver (28 vs 35 HP, 160 vs 120px) |
| FAIL     | Self    | 8 HP   | 0 (self)   | 0         | Dano da mao batendo no rifle (menos que o auto-dano do revolver) |

#### RNG Implementation
```javascript
const fireSuccess = Math.random() < 0.60; // 60% success, 40% fail (PIOR que o revolver zumbi!)
if (fireSuccess) {
    this.anims.play('bolsonaro_human_attack_success');
    // damage target -- 28HP, range 160px
} else {
    this.anims.play('bolsonaro_human_attack_fail');
    // damage self -- 8HP
    // play panic animation overlay
}
```

---

### H4. TRANSFORMACAO (Humano → Zumbi) -- "A Mordida"

#### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 3000ms           |
| Frames           | 8 (0-7)         |
| Frame Durations  | Variavel (veja breakdown) |
| Loop Mode        | None (play once, transition to zombie idle) |
| FPS              | 8                |
| Interruptible    | NAO -- sequencia cinematica, jogador perde controle |

#### Frame Timing Breakdown
```
0ms     -- Frame 0: "A Mordida" (400ms)
           - Flash vermelho no corpo (mordida recebida)
           - Corpo magricela CAIDE JOELHOS (y += 8px, sprite comprime vertical)
           - AK-47 escorrega das maos (spawn AK-47 sprite caindo, velocity x -20px/s, y +10px/s)
           - Expressao de CHOQUE PURO -- boca aberta, olhos maximos
           - Marca da mordida aparece no ombro (2x3px, vermelho escuro com borda esverdeada)
           - SFX: zombie_bite_wet at 0ms (mordida molhada, nojenta)
           - SFX: bolsonaro_human_scream at 50ms (grito de horror)
           - Screen shake: intensity 3, 200ms
           - Slowdown: game speed 0.5x durante este frame

400ms   -- Frame 1: "A Negacao" (400ms)
           - Maos vao ate a marca da mordida, tentando esfregar
           - Pele ao redor da mordida comeca a esverdeear (2px radius, transicao gradual)
           - AK-47 no chao atras, abandonada
           - Olhos procuram ajuda (pupilas movem left-right freneticamente)
           - Queixao treme (jitter 1px constante)
           - Ponchete comeca a pulsar com a infeccao (1px expand/contract, 200ms ciclo)
           - Veias esverdeadas comecam a aparecer no braco (1-2 linhas verdes, 1px, crescendo do ombro)
           - SFX: skin_crackle at 400ms (pele rachando, sutil)
           - SFX: heartbeat_accelerating at 400ms (loop, 0.3 volume, vai acelerar)

800ms   -- Frame 2: "Veias Verdes" (350ms)
           - Veias esverdeadas ESPALHAM pelo corpo (5-6 linhas de 1px, ramificando do ponto de mordida)
           - Pele do braco inteiro agora esverdeada
           - Rosto comeca a mudar: sombras verdes sob os olhos, queixao ganha tom esverdeado
           - Roupa comeca a ficar apertada nos ombros (costuras visualmente tensionadas, 1px linhas)
           - Ponchete pulsa MAIS RAPIDO (100ms ciclo agora)
           - Maos deixam o ombro e vao para a cabeca (dor, confusao)
           - SFX: bone_crack_growing at 800ms (ossos expandindo, grotesco)

1150ms  -- Frame 3: "A Mutacao Corporal" (400ms)
           - TORSO COMECA A INFLAR -- ombros alargam 2px cada lado
           - Camisa RASGA nos ombros (2-3 rasgos diagonais, com pixels de tecido se separando)
           - Ponchete de cerveja comeca a redistribuir -- barriga solta TRANSICIONA para peito de barril
           - Corpo se levanta dos joelhos lentamente (y -= 4px, metade do caminho)
           - Pele 60% esverdeada agora
           - Queixao CRESCE: +1px extensao frontal neste frame
           - Sorriso forcado comeca a CONGELAR -- musculos param de responder, rigor mortis iniciando
           - SFX: cloth_rip_heavy at 1150ms (camisa rasgando)
           - SFX: flesh_expand at 1250ms (som de carne inchando, nojento)

1550ms  -- Frame 4: "Troca de Armas" (350ms)
           - AK-47 no chao comeca a DISSOLVER (particulas cinzas subindo, alpha fade out)
           - Na mao direita: particulas DOURADAS comecam a coalescr (1px gold sparkles convergindo)
           - Torso 80% inflado para forma zumbi
           - Pele 80% esverdeada
           - Queixao CRESCE: mais +1px (total +2px desde o inicio)
           - Olhos: iris comeca a mudar para verde (transicao gradual de cor)
           - Rigor mortis do sorriso a 60% -- metade forcado humano, metade congelado zumbi
           - SFX: weapon_dissolve at 1550ms (som metalico reverso)
           - SFX: golden_materialize at 1700ms (som magico/brilhante, ironico)

1900ms  -- Frame 5: "O Revolver Aparece" (350ms)
           - Revolver dourado MATERIALIZA completamente na mao (flash dourado de confirmacao)
           - Corpo quase totalmente inflado -- barril chest a 90%
           - Pele completamente esverdeada (#7D8A6A)
           - Queixao no tamanho MAXIMO (+3px total -- maior que o idle zumbi normal por um frame)
           - Olhos: iris verde brilhante (#44FF44), glow suave (2px radius, 30% opacity)
           - Sorriso de rigor mortis a 90%
           - Faixa presidencial se ajusta ao corpo mais largo (estica, costuras aparecem)
           - SFX: revolver_cock at 1900ms (armar do revolver dourado -- som familiar do zumbi)
           - Heartbeat SFX desacelera (batimento cardíaco parando)

2250ms  -- Frame 6: "A Aceitacao" (400ms)
           - Corpo TOTALMENTE transformado em versao zumbi
           - Se levanta completamente (y volta a posicao normal)
           - Postura MUDA: ombros para tras, peito estufado, queixao agressivo
           - Revolver dourado na mao direita, posicao de bravata
           - Olhos totalmente verdes com glow constante
           - Rigor mortis COMPLETO -- o sorriso e identico ao forced grin do zumbi
           - A roupa rasgada nos ombros e o novo normal
           - Ponchete sumiu -- barril chest took over
           - SFX: heartbeat PARA (silencio subito, 200ms)
           - SFX: zombie_growl_low at 2400ms (primeiro som de zumbi)

2650ms  -- Frame 7: "Primeiro Passo Zumbi" (350ms)
           - Primeiro STRUT step -- pe direito bate no chao com PESO (dust cloud 3x3px)
           - Postura completa de bravata zumbi
           - Queixao retrai para tamanho normal do zumbi idle (de +3px volta para o tamanho padrao)
           - Flash de transicao: brief golden aura (1px, 20% opacity, 100ms) marca o fim da transformacao
           - Game speed retorna a 1.0x
           - Controle retorna ao jogador
           - VELOCIDADE APLICADA: 80 px/s → 48 px/s (-40% permanente)
           - SFX: transformation_complete_whoosh at 2650ms (som de finalizacao cinematica)
           - SFX: bolsonaro_zombie_talkei at 2800ms ("TALKEI" em tom de zumbi -- gutural, sem vida)
3000ms  -- Transicao para idle zumbi padrao
```

#### Tween Chain (Phaser 3)
```javascript
// Transformacao completa -- sequencia de tweens encadeados
this.tweens.timeline({
    targets: sprite,
    tweens: [
        // Fase 1: Cair de joelhos
        { y: '+= 8', scaleY: 0.9, duration: 400, ease: 'Quad.easeIn' },
        // Fase 2-3: Corpo comeca a inflar
        { scaleX: 1.1, scaleY: 1.0, duration: 750, ease: 'Sine.easeInOut' },
        // Fase 4-5: Inflacao maxima, troca de arma
        { scaleX: 1.15, scaleY: 1.05, duration: 700, ease: 'Back.easeOut' },
        // Fase 6: Levantar completo
        { y: '-= 8', scaleX: 1.0, scaleY: 1.0, duration: 400, ease: 'Power2.easeOut' },
        // Fase 7: Primeiro passo -- transicao para idle zumbi
        { scaleX: 1.0, scaleY: 1.0, duration: 350, ease: 'Stepped', onComplete: () => {
            this.anims.play('bolsonaro_idle'); // zumbi idle
            this.moveSpeed *= 0.6; // -40% permanente
            this.isZombie = true;
            this.weapon = 'golden_revolver';
            this.meleeEnabled = true;
            this.canInfect = true;
        }}
    ]
});
```

#### Skin Tint Transition
```javascript
// Transicao gradual de cor da pele humana para zumbi
// Executar em paralelo com os tweens acima
this.tweens.add({
    targets: sprite,
    tint: { from: 0xD4A574, to: 0x7D8A6A }, // Human skin -> Zombie skin
    duration: 2250, // Completa durante frames 0-5
    ease: 'Sine.easeIn'
});

// Eye glow -- comeca no frame 4
this.time.delayedCall(1550, () => {
    this.tweens.add({
        targets: eyeGlowSprite,
        alpha: { from: 0, to: 0.6 },
        duration: 1000,
        ease: 'Quad.easeIn'
    });
});
```

#### Particle Effects
| Effect           | Trigger        | Duration | Properties                           |
|------------------|----------------|----------|--------------------------------------|
| Mordida mark     | Frame 0        | Hold     | 2x3px vermelho escuro com borda verde no ombro, permanece visivel |
| Veias verdes     | Frame 1-3      | 1100ms   | Linhas de 1px verde escuro (#3D6B3A), ramificam do ombro, crescem 2px/100ms |
| Roupa rasgando   | Frame 3        | 200ms    | 3-4 pixels de tecido (#CCAA00 jersey yellow) se desprendem dos ombros |
| AK-47 dissolve   | Frame 4        | 350ms    | Particulas cinzas (#4A4A4A) sobem da arma no chao, 8-10 particulas, alpha fade |
| Revolver materialize | Frame 4-5  | 700ms    | Particulas douradas (#DAA520) convergem para a mao, 12-15 sparkles, spiral inward |
| Transformation flash | Frame 7    | 100ms    | Golden aura 1px ao redor do corpo, 20% opacity, fade rapido |
| Heartbeat visual | Frame 1-6      | 1850ms   | Pulsacao vermelha sutil no peito (0.1 opacity, synced com SFX heartbeat) |

---

## 6. SPECIAL -- "Arma Brochavel" (Enhanced Attack)

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 1200ms (SUCCESS) / 1800ms (FAIL) |
| Frames           | 4 (0-3)         |
| Cooldown         | 5000ms           |
| Mana/Energy Cost | 20               |

### Frame Timing Breakdown -- SUCCESS
```
0ms     -- Frame 0: "Dramatic Draw" (300ms)
            - Camera zoom tween: camera.zoom 1.0 -> 1.15 over 250ms, ease Cubic.easeOut
            - Vignette effect: dark border overlay alpha 0->0.3 over 200ms
            - Time slow: game.time.timeScale = 0.5 for 300ms (slow-mo draw)
            - SFX: spaghetti_western_sting at 0ms (twangy guitar hit, 0.5 volume)
            - SFX: heartbeat_slow at 100ms (single thump)

300ms   -- Frame 1: "Gun Out" (250ms)
            - Gun motion arc: golden trail particle (3px yellow line, curves from hip to aim position, 200ms lifespan)
            - Wind effect: hair/faixa blown back tween, 2px offset, 150ms
            - Flash on gun: 2px white starburst, 50ms
            - Time returns to normal: game.time.timeScale = 1.0
            - SFX: gun_draw_metallic at 300ms (sharp sliding metal)

550ms   -- Frame 2: "Fire SUCCESS" (300ms)
            - TRIPLE muzzle flash: 3 sequential flashes at 550ms, 600ms, 650ms (rapid fire)
            - Each flash: 10x10px starburst, staggered positions (spread shot)
            - 3 bullet trails: golden rectangles, velocity 500px/s, spread angle +/-10deg
            - MASSIVE recoil: body x -= 5px over 100ms
            - Screen shake: intensity 5, duration 200ms
            - Shell casings: 3 casings eject at 50ms intervals
            - Smoke cloud: 8x6px, spawns at barrel, drifts upward over 600ms
            - SFX: triple_shot_blast at 550ms (three rapid gunshots overlaid)
            - SFX: ricochet_whiz at 650ms (bullet whiz past)

850ms   -- Frame 3: "Aftermath SUCCESS" (350ms)
            - Smoke clearing particles (4-5 gray wisps, alpha 0.3->0.0, 350ms)
            - Cowboy pose hold: gun raised, smoke trailing
            - Lip purse tween: mouth sprite shifts to "blowing smoke" variant
            - Camera zoom returns: 1.15 -> 1.0 over 300ms
            - Vignette fades: alpha 0.3 -> 0.0 over 300ms
            - SFX: smoke_blow at 900ms (soft breath)
            - SFX: belt_buckle_clink at 1000ms (holstering)

1200ms  -- Return to idle
```

### Frame Timing Breakdown -- FAIL
```
0ms-550ms -- IDENTICAL to SUCCESS (build-up is the same -- comedy of expectation)

550ms   -- Frame 2: "Fire FAIL" (600ms)
            - Gun droop tween: gun rotation 0 -> -45deg over 300ms, ease Elastic.easeOut (bouncy droop)
            - Pathetic puff: 5x5px gray cloud, scale 1.0->0.3 (it SHRINKS), 400ms
            - Face split expression: left half tween to manic, right half to devastated (shader or sprite swap)
            - Self-damage: HP -= 15, red flash on body at 650ms
            - "?" spawns at 700ms, floats up
            - Sad trombone particle: small music notes (gray, descending) near gun, 3 notes falling
            - Camera zoom JERKS: zoom 1.15 -> 0.95 (pulls BACK in disappointment), 200ms
            - SFX: gun_click_empty_loud at 550ms
            - SFX: sad_trombone_full at 600ms (wah wah wah wahhh)
            - SFX: crowd_groan at 700ms (distant disappointed crowd, 0.2 volume)

1150ms  -- Frame 3: "Aftermath FAIL" (650ms)
            - Gun held at arm's length like a dead fish
            - Head hanging tween: head y += 4px, chin points down, 300ms
            - Kicked-dirt: 3-4 small dust particles at feet (frustration)
            - Phone buzz: pocket glow flashes (supporters sending "???")
            - Camera returns to normal
            - Vignette fades
            - SFX: talkei_defeated at 1200ms ("talkei?" in the most defeated voice possible)
            - SFX: phone_buzz_multiple at 1300ms (vibration barrage)

1800ms  -- Return to idle
            - Residual shame: idle plays with 10% darker color tint for 3000ms (shame afterglow)
```

### Damage Values (Special)
| Outcome  | Target  | Damage | Range      | Knockback | Special           |
|----------|---------|--------|------------|-----------|-------------------|
| SUCCESS  | Enemy   | 75 HP  | 150px, 20deg spread | 16px | Pierces 1 enemy  |
| FAIL     | Self    | 15 HP  | 0          | 0         | 3s attack debuff  |

---

## 7. SPECIAL -- "Motociata"

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 3000ms           |
| Frames           | 6 (0-5)         |
| Cooldown         | 12000ms          |
| Mana/Energy Cost | 35               |

### Frame Timing Breakdown
```
0ms     -- Frame 0: "Mount Up" (400ms)
            - Motorcycle sprite spawns at bolsonaro.x - 20px
            - Mount tween: bolsonaro.y -= 8px (leg swing), then y += 4px (settle on seat)
            - SFX: motorcycle_approach at 0ms (engine growing louder)
            - SFX: boot_leather at 200ms (mounting)

400ms   -- Frame 1: "Rev Engine" (500ms)
            - Screen shake: intensity 2, duration 500ms, frequency high (engine vibration)
            - Exhaust particles: verde-amarelo (#006400, #FFD700) puffs, 4/frame, growing
            - Engine vibration: bike sprite jitters +/-1px at 30Hz
            - SFX: engine_rev_heavy at 400ms (LOUD Harley rumble, builds for 500ms)

900ms   -- Frame 2: "Launch" (400ms)
            - Wheelie tween: bike front tilts up 20deg over 200ms
            - Speed lines activate: 5 horizontal white lines spawn at right edge, move left at 200px/s
            - Ghost motos begin: first 2-3 green translucent bikes spawn at bolsonaro.x - 30px, follow with 200ms delay
            - Tire burn particles: orange/red sparks at rear wheel, 8 particles
            - SFX: tire_screech at 900ms
            - SFX: engine_roar at 950ms (RPM redline)

1300ms  -- Frame 3: "Full Speed" (500ms)
            - Boss and bike MOVE: x velocity = 250px/s rightward (crosses screen)
            - Ghost motos multiply: new ghost spawns every 100ms, up to 6 total
            - Ghost motos follow in V-formation, each offset 8px behind and +/-6px vertically
            - Speed lines MAXIMUM: 8+ lines, full width, varying opacity
            - Damage zone: continuous hitbox along path, 64px wide, deals damage every 100ms
            - SFX: motorcycle_charge at 1300ms (continuous engine + wind)
            - SFX: ghost_whisper at 1400ms (eerie moto ghost sound loop)

1800ms  -- Frame 4: "Impact" (400ms)
            - Impact starburst: 20x20px at collision point, golden-white
            - Ghost motos CHAIN CRASH: each ghost stops and explodes in sequence (100ms apart)
            - Ghost explosion: 6x6px green particle burst per ghost (8 particles each, random velocity)
            - Bike tilt: rotation += 45deg (tilting over)
            - Bolsonaro separation begins: y -= 6px (launching off bike)
            - Screen shake: intensity 6, duration 300ms
            - SFX: crash_metal_heavy at 1800ms
            - SFX: ghost_dissipate at 1900ms (whooshing fade)

2200ms  -- Frame 5: "Aftermath / Dismount Fail" (800ms)
            - Bolsonaro ragdoll: tumble tween rotation 0->180deg, arc trajectory (parabola, apex 20px up)
            - Landing SQUASH: scaleY 0.6, scaleX 1.4 at ground contact, bounce back over 200ms
            - Bike slides away: x += 30px over 400ms, decelerating, sparks trailing
            - Bike wheel spin: rear wheel sprite rotates 1440deg/s, decelerating to 0 over 2000ms
            - Ghost wisps: green particle fade (alpha 0.3->0.0 over 800ms)
            - KO stars: 3 golden stars orbit head, 540deg/s
            - Weak thumbs-up: at 2800ms, hand sprite raises 4px, thumb extends (300ms tween)
            - SFX: body_tumble at 2200ms (rolling/scraping)
            - SFX: body_slam at 2500ms (final ground impact)
            - SFX: stars_twinkle at 2600ms
            - SFX: talkei_broken at 2800ms ("ta...lkei..." weak, cracking voice)

3000ms  -- Return to idle (Bolsonaro stands up dazed, 400ms recovery tween)
```

### Damage Values (Motociata)
| Phase       | Damage/tick | Tick Rate | Width  | Total Possible |
|-------------|-------------|-----------|--------|----------------|
| Charge      | 15 HP       | 100ms     | 64px   | 75 HP (5 ticks)|
| Ghost motos | 8 HP each   | on impact | 32px   | 48 HP (6 ghosts)|
| Impact zone | 25 HP       | once      | 96px   | 25 HP          |
| **Max total**| --         | --        | --     | **148 HP**     |

---

## 8. SPECIAL -- "Golpe Frustrado"

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 4500ms           |
| Frames           | 8 (0-7)         |
| Cooldown         | 20000ms          |
| Mana/Energy Cost | 30               |
| Damage           | 0 (this skill always fails comically) |

### Frame Timing Breakdown
```
0ms     -- Frame 0: "Military Salute" (400ms)
            - Rigid pose tween: body straightens, snap to attention
            - Camo overlay: 20% opacity green camo pattern fades onto clothes
            - SFX: boots_click at 0ms (military heel click)
            - SFX: patriotic_trumpet_start at 100ms (begins triumphant, will be cut short)

400ms   -- Frame 1: "Summoning Call" (500ms)
            - Mouth opens: 3 concentric arc particles from mouth, expanding 16px each, 1px white
            - Ground crack: 2 dark line sprites at feet, grow outward 4px
            - Trumpet icon spawns at 500ms, floats beside head
            - SFX: war_cry_bolsonaro at 400ms (commanding shout)
            - SFX: trumpet_fanfare at 500ms (military trumpet)

900ms   -- Frame 2: "Waiting..." (600ms) *** COMEDIC PAUSE ***
            - Arms slowly lower tween: y += 2px over 400ms
            - "..." particle: 3 gray dots appear sequentially (200ms apart) above head
            - Trumpet icon SHATTERS at 1100ms (breaks into 4 fragments)
            - Awkward silence: ALL ambient sound drops to 30% volume for 600ms
            - Tumbleweed particle: small brown circle rolls across bottom of frame at 1200ms (optional comedy)
            - SFX: cricket_chirp at 1200ms (single cricket, maximum awkwardness)
            - SFX: trumpet_dying at 1100ms (deflating trumpet sound)

1500ms  -- Frame 3: "Eduardo Appears Wrong" (500ms)
            - Eduardo sprite spawns at right edge of screen
            - Eduardo runs LEFT (toward Bolsonaro, WRONG DIRECTION)
            - Eduardo speed: 120px/s leftward
            - Eduardo holds phone in selfie position (phone screen glow)
            - Bolsonaro jaw drop tween: chin y += 2px (chin drops further)
            - Bolsonaro eye bulge: eyes scale 1.0 -> 1.3 over 200ms
            - SFX: record_scratch at 1500ms (classic comedy record scratch)
            - SFX: selfie_shutter at 1600ms (Eduardo taking selfie mid-run)
            - SFX: bolsonaro_gasp at 1650ms (horrified intake of breath)

2000ms  -- Frame 4: "Eduardo Runs Wrong Way" (500ms)
            - Eduardo continues running across frame in wrong direction
            - Eduardo trail: phone screen light trails behind him
            - Bolsonaro pointing tween: both arms animate to point in OPPOSITE direction of Eduardo
            - Bolsonaro face: rage + embarrassment shader (red tint 20%, 300ms pulse)
            - Small crowd laugh particle: "HA" text in small letters at frame edges
            - SFX: running_footsteps_fast at 2000ms (Eduardo's panicked running)
            - SFX: bolsonaro_yell at 2100ms ("EDUARDO! PRA LA!" angry shout)

2500ms  -- Frame 5: "Eduardo Falls in Hole" (600ms)
            - Hole sprite: 8x8px dark void appears at Eduardo's path
            - Eduardo disappears into hole over 200ms (y += 64px, falling)
            - Eduardo's legs remain visible, still running (cycling in void)
            - Phone launches upward from hole: parabolic arc, 15px apex, cracked on landing
            - Dust cloud around hole: 6 particles, radial burst
            - Bolsonaro freeze: all tweens stop, 200ms of pure frozen horror
            - SFX: hole_open at 2500ms (cartoony ground crumble)
            - SFX: eduardo_falling_yell at 2550ms (classic falling "aaaaaah" with doppler effect, fading)
            - SFX: phone_smash at 2800ms (cracking glass)

3100ms  -- Frame 6: "Facepalm" (600ms)
            - Both hands to face tween: hands rise over 200ms, cover eyes (chin still visible -- too big to cover)
            - Body slump: y += 3px, overall shrink scale 0.95 (deflation)
            - Shame cloud: dark gray 4x3px cloud, alpha 0.15, hovers around body
            - Eduardo's legs in hole slow down and stop
            - Sunglasses slide off: fall from head to ground, 200ms
            - SFX: facepalm_slap at 3100ms (hand hitting face)
            - SFX: shame_sigh at 3300ms (deep defeated exhale)

3700ms  -- Frame 7: "Angry Recovery" (800ms)
            - Hands slam down from face: fast tween, 100ms
            - VOLCANIC RAGE expression: red overlay 15%, veins pulse
            - Points at Eduardo's hole accusingly
            - Other hand raises gun (accidentally pointing at self -- dark comedy)
            - Body trembles: 1px vibration at 20Hz for 400ms
            - Eduardo's hand waves weakly from hole (small white flag on a stick)
            - Single tear: 1px blue pixel on cheek, trickles 2px down over 400ms
            - SFX: angry_outburst at 3700ms (incoherent rage yelling)
            - SFX: gun_wave at 3900ms (accidental gun pointing sound)
            - SFX: white_flag_flutter at 4000ms (tiny cloth sound)

4500ms  -- Return to idle
            - All hole sprites fade over 500ms
            - Eduardo despawns
            - Bolsonaro residual anger: idle plays with vein overlay for 5000ms
```

### Gameplay Effect
- This skill intentionally does NO damage to enemies
- It is a failed summon that wastes the cooldown
- The comedy IS the effect -- player chooses it for humor or mistakenly
- Eduardo might accidentally damage Bolsonaro (5 HP friendly fire from phone throw)
- Debuff on Bolsonaro: "Embarrassed" -- 15% attack reduction for 8s

---

## 9. SPECIAL -- "Pintou um Clima"

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 4000ms           |
| Frames           | 4 (0-3)         |
| Effect Duration  | 3000ms (paralysis)|
| Cooldown         | 15000ms          |
| Mana/Energy Cost | 25               |

### Frame Timing Breakdown
```
0ms     -- Frame 0: "Uncomfortable Lean" (500ms)
            - Lean tween: body tilts 5deg toward nearest player, x -= 4px (closing distance)
            - Creepy smile: mouth sprite swaps to "smarmy" variant
            - Eyes half-lid: eye sprite swaps to half-closed variant
            - Wiggle hand: left hand oscillates rotation +/-10deg at 4Hz
            - SFX: uncomfortable_music_box at 0ms (off-key music box, 0.3 volume, unsettling)
            - SFX: heavy_breathing at 200ms (too-close breathing, 0.2 volume)

500ms   -- Frame 1: "The Phrase" (500ms)
            - Speech indicator: small wedge from mouth, 2px
            - Cringe aura ACTIVATES: pink-purple energy field expands from body
            - Aura expand tween: radius 0 -> 80px over 400ms, ease Quad.easeOut
            - Aura appearance: concentric semicircles, pink (#FF69B4) core, purple (#800080) edge
            - Aura opacity: 0.0 -> 0.3 over 400ms
            - "!" particles: 5 exclamation marks spawn randomly within aura radius, 2px yellow
            - SFX: pintou_um_clima at 500ms (Bolsonaro's voice saying it, creepy delivery)
            - SFX: record_slowdown at 600ms (music slowing/warping)
            - All enemies within 80px radius: movement speed = 0, attack disabled (3s paralysis)

1000ms  -- Frame 2: "Area Effect Active" (2000ms)
            - Aura PULSES: radius oscillates 80px +/- 5px at 2Hz
            - Aura color shifts: pink<->purple gradient rotates
            - "!" particles float in random directions within zone, 1px/frame drift
            - Bolsonaro still in smarmy pose, OBLIVIOUS
            - Affected enemies: play stunned animation (frozen with "cringe" face overlay)
            - Pulsing visual on all affected entities: pink tint flash, 0.1 opacity, 500ms cycle
            - Phone glow through pocket: blue-white pulse (people are clipping this moment)
            - SFX: cringe_ambient at 1000ms (loop, 2s, uncomfortable sustained tone)
            - SFX: distant_sirens at 2000ms (very faint, comedic implication, 0.05 volume)

3000ms  -- Frame 3: "Effect End / Confusion" (1000ms)
            - Aura COLLAPSE: radius 80px -> 0px over 500ms, ease Quad.easeIn
            - Pink color drains (desaturation tween over 500ms)
            - "!" particles fade (alpha 1.0 -> 0.0 over 300ms)
            - Bolsonaro straightens up: lean tween reverses, 300ms
            - Adjusts sunglasses: hand to head, 200ms
            - Adjusts faixa: hand to chest, 200ms
            - Returns to normal idle stance
            - Affected enemies: unfreeze, play "shaking off cringe" animation (shiver + head shake)
            - Sparkle dissipation: 4 white 1px pixels at aura perimeter, fade over 200ms
            - SFX: spell_break at 3000ms (crystal shattering/releasing)
            - SFX: crowd_uncomfortable_murmur at 3200ms (0.2 volume)
            - SFX: bolsonaro_normal_breath at 3500ms (casual, unbothered -- he has NO idea)

4000ms  -- Return to idle
```

### Damage Values
| Effect        | Value    | Duration | Range    |
|---------------|----------|----------|----------|
| Paralysis     | 0 HP     | 3000ms   | 80px radius |
| Shame debuff  | -10% ATK | 5000ms   | All affected |

---

## 10. SPECIAL -- "Live da Cela"

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 5500ms           |
| Frames           | 6 (0-5)         |
| Cooldown         | 25000ms          |
| Mana/Energy Cost | 40               |

### Frame Timing Breakdown
```
0ms     -- Frame 0: "Secret Phone Pull" (600ms)
            - Eyes dart tween: eye sprite x oscillates +/-2px at 4Hz (paranoid glance)
            - Body hunch: scaleY 0.95 (crouching/sneaking)
            - Hand reaches into pocket: hand sprite moves to hip, phone glow visible through fabric
            - "Shh" gesture: other hand to lips
            - Prison bar overlay (2026 skin): 3 vertical gray lines, 20% opacity, foreground layer
            - SFX: cloth_rustle at 0ms (reaching in pocket)
            - SFX: nervous_gulp at 300ms

600ms   -- Frame 1: "Live Start" (500ms)
            - Phone OUT: phone sprite appears at face level (3x5px, blue-white screen)
            - "LIVE" dot: 1px red circle on phone, pulse alpha 0.5->1.0 at 2Hz
            - Face illuminate: blue-white highlight pixels activate on chin/nose/cheeks
            - PERSONALITY SWITCH: instant tween from hunch (scaleY 0.95) to proud (scaleY 1.05)
            - Smile swap: mouth sprite instant-swaps from tight-lipped to MANIC GRIN
            - Thumbs up with free hand
            - Viewer count: small "1...10...100..." number sprite on phone, incrementing
            - SFX: live_start_chime at 600ms (social media live notification sound)
            - SFX: bolsonaro_live_greeting at 700ms ("TALKEI! Bom dia a todos!")

1100ms  -- Frame 2: "Broadcasting" (600ms)
            - Gesticulating: free hand oscillates rapidly, 2px motion blur
            - Mouth WIDE: clearly ranting (mouth sprite = wide open variant)
            - Signal waves: 3 curved lines emit from phone rightward, expand and fade, 400ms cycle
            - Phone shows recursive face: tiny 1x2px face sprite on phone screen
            - Viewer count rising: number sprite increments faster
            - "LIVE" dot steady bright red
            - SFX: bolsonaro_rant_loop at 1100ms (1s loop of animated ranting, muffled)

1700ms  -- Frame 3: "Ghost Motos Spawn" (800ms)
            - Signal waves SOLIDIFY: 3 waves stop expanding and form into motorcycle shapes
            - Ghost moto spawn: 3 translucent green (#44FF44, 30% opacity) motorcycles materialize
            - Each ghost moto: spawn position at signal wave endpoints, 200ms materialize tween (alpha 0->0.3)
            - Each ghost rider: crude green silhouette with Brazil flag (1x1px verde-amarelo dots)
            - Notification icons: hearts and thumbs float up from phone, 6-8 small icons, 1px each
            - Triumphant expression: eyes blaze, chin maximum
            - Points at ghosts with gun-as-pointer
            - SFX: digital_materialize at 1700ms (glitchy materialization sound)
            - SFX: motorcycle_ghost_rev at 2000ms (distant, echoing engine sound)
            - SFX: notification_barrage at 1800ms (rapid-fire notification pings)

2500ms  -- Frame 4: "Ghost Horde Active" (2000ms)
            - Ghost motos MULTIPLY: new ghost spawns every 400ms, max 6 total
            - Ghosts orbit Bolsonaro at radius 60px, speed 90deg/s
            - Ghost motos deal damage on contact with enemies: 12 HP each
            - Green exhaust haze: particle system, verde mist across lower 8px, alpha 0.2
            - Bolsonaro conductor pose: phone held high, free arm spread wide
            - Expression: ECSTASY of power (widest smile, widest eyes)
            - Notification icons multiply: 12+ small hearts/thumbs floating upward continuously
            - Signal wave continuous: phone emits constant waves, lower opacity (0.15)
            - SFX: ghost_moto_whoosh_loop at 2500ms (loop for duration, ghostly engine + wind)
            - SFX: battle_shout at 3000ms ("BRASIL ACIMA DE TUDO!")

4500ms  -- Frame 5: "Signal Fade / Return" (1000ms)
            - Ghost motos FADE: all ghosts alpha 0.3 -> 0.0 over 600ms, one by one (100ms stagger)
            - Ghost explosion: each ghost pixelates into 8 green 1px particles that scatter, 400ms
            - Phone HIDDEN: arm jams into pocket over 300ms (frantic hiding)
            - Personality SWITCH BACK: scale 1.05 -> 0.95 (back to hunching/sneaky)
            - Smile swap: MANIC GRIN -> tight-lipped "wasn't me"
            - "LIVE" dot: final blink, off
            - Green haze clears: alpha 0.2 -> 0.0 over 500ms
            - Notification icons: fall like dead pixels (gravity, tumble to ground)
            - Whistling: small music notes (2px, gray) near mouth, 3 notes floating up
            - SFX: signal_lost at 4500ms (digital static, fading)
            - SFX: phone_pocket_rustle at 4600ms (frantic shoving)
            - SFX: innocent_whistling at 4800ms (casual, terrible whistling)

5500ms  -- Return to idle
```

### Damage Values
| Element       | Damage | Behavior                         |
|---------------|--------|----------------------------------|
| Ghost moto    | 12 HP  | Contact damage, orbiting at 60px radius |
| Total ghosts  | 6 max  | Each lives for full duration     |
| Max damage    | 72 HP  | If all 6 hit the same target     |

---

## 11. SPECIAL -- "Imorrivel, Imbrochavel, Incomivel"

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 6500ms           |
| Frames           | 4 (0, 1-2 loop, 3) |
| Invuln Duration  | 5000ms           |
| Cooldown         | 45000ms          |
| Mana/Energy Cost | 50               |

### Frame Timing Breakdown
```
0ms     -- Frame 0: "Activation Pose" (500ms)
            - Arms cross tween: both arms to X position over 200ms
            - Head tilt back: rotation -10deg over 200ms
            - Golden aura START: 1px gold outline appears, alpha 0->0.3 over 500ms
            - Body glow: all highlight colors brighten 20% via shader tint
            - Scar transforms: scar color tweens from #D35D6E -> #DAA520 (pink to gold) over 400ms
            - Text spawn: "IMORRIVEL" begins forming above head, letter by letter, 60ms per letter
            - SFX: power_charge at 0ms (building energy hum)
            - SFX: bolsonaro_imorrivel at 200ms ("Eu sou IMORRIVEL..." voice, building in intensity)

500ms   -- Frames 1-2 LOOP for 5000ms: "Invulnerable State"
            - INVULNERABILITY FLAG: this.isInvulnerable = true
            - All incoming damage = 0
            - Golden aura: 3px glow, alpha 0.6, pulses (0.5-0.7) at 1Hz
            - Aura expand/contract: radius oscillates +/-2px at 1Hz (breathing)
            - "PING" particles: whenever hit, spawn 2px white starburst at hit point, 100ms lifespan
            - Text cycles: "IMORRIVEL" -> "IMBROCHAVEL" -> "INCOMIVEL" -> repeat (2s per word)
            - Text pulse: scale 1.0->1.2->1.0 on each word change, 200ms
            - Golden overlay: 20% opacity gold tint on entire sprite
            - Golden particles: 4 gold 1px pixels orbit body, circular path radius 14px, speed 180deg/s
            - Faixa rigid: no flutter, held by energy
            - SFX: invulnerable_hum_loop at 500ms (continuous golden energy hum)
            - SFX: bolsonaro_imbrochavel at 2500ms ("IMBROCHAVEL!" shout)
            - SFX: bolsonaro_incomivel at 4500ms ("INCOMIVEL!" shout)
            - SFX: ping_deflect on each hit received (metallic ping, 0.4 volume)

5500ms  -- Frame 3: "Deactivation" (1000ms)
            - Aura SHATTER: golden glow fragments outward as 10 gold 2x2px shards
            - Shard velocity: random direction, 50-100px/s, gravity 100px/s^2, alpha 1.0->0.0 over 500ms
            - Body flash: gold -> normal colors INSTANT (0ms transition -- jarring on purpose)
            - Text dissolve: letters fall individually with gravity, 100ms stagger
            - Stagger tween: body tilts 5deg, one hand on knee
            - Exhaustion: scaleY 0.93 (body shrinks from energy drain)
            - Eyes droop: eye sprite swaps to exhausted variant
            - Gray cloud: 4x3px dark gray, alpha 0.2, passes over body, 800ms
            - Sweat drops: 4 drops spray from body, all directions
            - VULNERABILITY WINDOW: all damage taken is 1.3x for 3000ms after deactivation
            - SFX: aura_shatter at 5500ms (glass-like shattering with golden reverb)
            - SFX: exhaustion_gasp at 5700ms (heavy exhausted breathing)
            - SFX: vulnerability_warning at 5800ms (subtle low tone, gameplay warning)

6500ms  -- Return to idle (weakened idle for 3s, then normal)
```

---

## 12. ULTIMATE -- "Motociata do Juizo Final"

### Timing
| Property         | Value            |
|------------------|------------------|
| Total Duration   | 8000ms           |
| Frames           | 8 (0-7)         |
| Cooldown         | 60000ms (once per boss fight phase) |
| Mana/Energy Cost | 100 (full bar)   |
| Activation       | Below 30% HP     |

### Frame Timing Breakdown
```
0ms     -- Frame 0: "Whistle / Summon" (600ms)
            - Camera: zoom 1.0 -> 1.3 over 500ms (dramatic close-up)
            - Vignette: alpha 0 -> 0.5 (heavy darkening)
            - Time scale: 0.3 (super slow-mo)
            - Whistle pose: fingers to mouth
            - Sound waves: 5 MASSIVE concentric arcs from mouth, each 4px thick, expanding 200px
            - Ground vibration: all ground tiles jitter +/-1px at 15Hz
            - Small debris: 6-8 1px particles bounce on ground
            - Warning indicator: red ! above all player characters
            - SFX: whistle_loud at 0ms (piercing two-finger whistle)
            - SFX: ground_rumble at 200ms (low bass rumble, building)
            - SFX: dramatic_drums at 300ms (taiko drum buildup)
            - MUSIC: battle_music fades to 30% volume

600ms   -- Frame 1: "Golden Harley Arrives" (700ms)
            - Golden Harley sprite: enters from left at 300px/s, decelerating to 0 at Bolsonaro's position
            - Bike spark trail: 12 orange 1px sparks trailing under tires, each 200ms lifespan
            - Bolsonaro LEAP: parabolic arc, apex 12px above ground, 400ms, lands on bike seat
            - Expression swap: PURE JOY (only genuine smile in the entire sprite set)
            - Camera follows bike entry: slight pan left to right
            - Verde-amarelo exhaust: 8 particles on bike arrival, oversized cloud
            - Time scale returns to 0.5
            - SFX: motorcycle_screech_arrival at 600ms (tire screech + heavy engine)
            - SFX: bolsonaro_war_cry at 800ms (ecstatic battle shout)
            - SFX: bike_settle at 1000ms (suspension bounce)

1300ms  -- Frame 2: "Mount + Rev" (600ms)
            - Throttle crank: right hand twists handlebar, visible motion
            - Engine vibration: EVERYTHING shakes (camera, sprites, UI) at 20Hz, 2px amplitude
            - Exhaust cloud FILLS bottom 20% of screen
            - Ghost motos BEGIN: 3 green translucent bikes materialize behind (alpha 0->0.3 staggered)
            - Ghost materialization: digital glitch effect (horizontal lines, pixel displacement) for 200ms per ghost
            - Ground cracks radiate from rear tire: 5 dark lines, growing outward 2px/frame
            - Head thrown back in howl: mouth at MAXIMUM open
            - Time scale returns to 1.0
            - SFX: engine_rev_ultimate at 1300ms (DEAFENING Harley roar, sustained, building)
            - SFX: ghost_summon_echo at 1500ms (ethereal motorcycle engines joining, echo effect)

1900ms  -- Frame 3: "Charge Launch" (800ms)
            - WHEELIE: front wheel 8px up, 200ms tween
            - LAUNCH: bike + bolsonaro velocity = 350px/s rightward
            - Speed lines: 10+ white horizontal lines, full screen width, 1-2px thick, varying opacity
            - Ghost motos MULTIPLY: new ghost every 80ms, up to 12 total
            - Ghost V-formation: each new ghost slots into position 10px behind and alternating +/-8px vertical
            - Tire fire: LARGE flame sprite at rear wheel (8x4px, animated 4-frame fire)
            - Faixa becomes a straight line streaming behind (scaleX stretched)
            - Debris in wake: paper, leaves, hat, 8 assorted small sprites blowing backward
            - Screen edge warning: right side of screen flashes red (incoming damage zone)
            - SFX: launch_explosion at 1900ms (engine + backfire + tire screech combined)
            - SFX: wind_extreme at 2000ms (hurricane wind, sustained)
            - SFX: crowd_ghost_chant at 2100ms ("MITO! MITO!" ghostly chant, echoing)

2700ms  -- Frame 4: "Full Horde Charge" (700ms)
            - MAXIMUM VELOCITY: 400px/s
            - Damage zone: continuous, 96px wide, FULL SCREEN HEIGHT
            - Every entity in path takes damage every 50ms: 20 HP per tick
            - 12 ghost motos in V-formation, ALL active
            - Ghost rider details: red eye dots, flag waving, exhaust trail per ghost
            - Speed blur: Bolsonaro's features smear horizontally (motion blur shader)
            - Headlight: 4px white circle, blinding bloom effect radius 20px
            - Screen: everything except the charge path dims to 40% brightness
            - Ground destruction: tire marks left behind (permanent dark line sprites on ground)
            - Camera: pan speed matches charge speed
            - SFX: motorcycle_stampede at 2700ms (12+ engines combined, overwhelming)
            - SFX: destruction_path at 2700ms (continuous crashing/smashing)

3400ms  -- Frame 5: "Impact Zone" (600ms)
            - Collision with screen edge or major obstacle
            - MEGA STARBURST: 24x24px golden-white explosion, center screen
            - Bloom effect: screen whites out to 60% for 100ms
            - Ghost motos CHAIN CRASH: sequential explosions at 50ms intervals
            - Each ghost crash: 8x8px green particle burst (10 particles, random velocity 50-120px/s)
            - Bike begins SEPARATING from Bolsonaro
            - Bike tilt: rotation 0->90deg over 300ms
            - Bolsonaro lift-off: y velocity = -120px/s (launched upward)
            - Debris field: 20+ small sprites of chrome, gold, flag fragments, green ghost shards
            - Screen shake: intensity 8 (MAXIMUM), duration 400ms
            - SFX: ultimate_impact at 3400ms (massive explosion + metal crash + glass shatter combined)
            - SFX: ghost_death_collective at 3500ms (12 ghosts wailing and dissipating)
            - MUSIC: dramatic silence for 500ms (everything cuts out)

4000ms  -- Frame 6: "The Fall" (1000ms)
            - Bolsonaro RAGDOLL: full rotation (360deg), parabolic arc trajectory
            - Arc: apex 32px above ground, 800ms total arc time
            - Limbs: each arm/leg has slight independent oscillation (+/-2px, random phase)
            - Bike sliding away: x += 60px, decelerating, spark trail, rotation 45deg
            - Bike wheel spin: 2160deg/s, decelerating
            - Ghost motos: only green wisps remain, fading
            - Expression during tumble: PURE TERROR (eyes circles, mouth O)
            - Faixa wrapped around leg (tangled)
            - Gun detaches: flies in separate arc, 20px from body at max
            - Sunglasses: detached during impact, fragments scattered
            - One shoe: already gone
            - Time scale: 0.7 (slight slow-mo for comedic effect)
            - SFX: body_tumble_air at 4000ms (whooshing tumble)
            - SFX: bolsonaro_scream at 4200ms ("AAAAAAH!" terrified scream, doppler shift)
            - SFX: items_scatter at 4300ms (clinking of accessories)

5000ms  -- Frame 7: "Crash Landing" (3000ms hold)
            - GROUND IMPACT: chin hits first (chin-crater: 4x2px dark indent in ground sprite)
            - SQUASH: scaleY 0.5, scaleX 1.5 for 100ms, bounce to scaleY 0.8, scaleX 1.2
            - Crater cracks: 8 radial lines from chin impact point, 6px each
            - Dust MUSHROOM CLOUD: 16x12px, 20 particles, billow upward over 1000ms
            - Blood pool: small, alpha 0->0.4 over 500ms at body
            - Star orbit: 5 golden stars, 2px each, tight circle (radius 10px), speed 720deg/s -> 180deg/s over 2000ms
            - Bike: toppled 16px away, wheel spin decelerating (2160deg/s -> 0 over 3000ms)
            - Bike exhaust: final sputters (3 puffs at 500ms intervals, diminishing size)
            - Gun: lands 16px away, barrel droops (rotation -40deg, brochavel in death)
            - Faixa: limp, draped over body
            - Green wisps: final 3-4 ghost particles fade over 1000ms
            
            *** THE THUMBS UP (the defining moment) ***
            - At 6500ms (1500ms after crash): right hand begins to RISE
            - Hand rise tween: y -= 4px over 500ms, ease Quad.easeOut
            - Thumb extends: thumb pixel separates from fist, 200ms
            - Trembling: hand oscillates +/-0.5px at 3Hz (weak, shaking)
            - A single tear: 1px blue pixel on one visible cheek
            
            - SFX: body_crash_final at 5000ms (heavy impact, low bass)
            - SFX: chin_crater at 5020ms (comedic crunch -- chin creating crater)
            - SFX: dust_billow at 5100ms (whooshing dust)
            - SFX: stars_orchestra at 5200ms (cartoony star twinkle, musical)
            - SFX: bike_sputter at 5500ms, 6000ms, 6500ms (dying engine, each shorter)
            - SFX: silence_beat at 6000ms (complete silence for 500ms -- comedic pause)
            - SFX: talkei_final at 7000ms ("ta...l...kei..." barely a whisper, maximum pathos)
            - SFX: single_clap at 7500ms (one distant sarcastic slow clap, 0.1 volume)
            - MUSIC: resumes at 7500ms, normal battle music

8000ms  -- End of ultimate
            - Boss stands up (recovery animation, 1000ms)
            - Residual effects: limping walk for 5000ms (walk speed 0.5x)
            - Missing one shoe for remainder of fight (visual only)
            - Faixa permanently disheveled (no longer pristine)
```

### Damage Values (Ultimate)
| Phase          | Damage/tick | Tick Rate | Width     | Duration  | Max Damage |
|----------------|-------------|-----------|-----------|-----------|------------|
| Charge path    | 20 HP       | 50ms      | 96px      | 1400ms    | 560 HP     |
| Ghost moto hit | 15 HP       | contact   | 32px each | one-time  | 180 HP (12)|
| Impact zone    | 50 HP       | once      | 128px rad | instant   | 50 HP      |
| Debris scatter | 5 HP        | random    | 64px rad  | 1000ms    | ~25 HP     |
| **Total max**  | --          | --        | --        | --        | **~815 HP**|

### Dodge Window
- Telegraph: 600ms whistle phase is the dodge window
- Warning: red ! indicator on all players at 200ms
- Safe zone: behind Bolsonaro (he charges FORWARD only)
- Jump timing: if player jumps at 1800-2000ms, they can avoid the charge

---

## GLOBAL ANIMATION RULES

### Priority System
```
ULTIMATE > DEATH > SPECIAL > HIT > ATTACK > WALK > IDLE
```
Higher priority animations interrupt lower ones. HIT can interrupt ATTACK (flinch). DEATH interrupts everything. ULTIMATE cannot be interrupted.

### Transition Rules
| From      | To        | Transition Time | Method                    |
|-----------|-----------|-----------------|---------------------------|
| IDLE      | WALK      | 0ms             | Instant frame swap        |
| WALK      | IDLE      | 100ms           | Deceleration (last walk frame -> idle frame 0) |
| ANY       | HIT       | 0ms             | Instant interrupt         |
| HIT       | Previous  | 200ms           | Blend back to interrupted anim |
| ANY       | DEATH     | 0ms             | Instant interrupt, no return |
| IDLE/WALK | ATTACK    | 50ms            | Quick draw transition     |
| ATTACK    | IDLE      | 100ms           | Settle back               |
| ANY       | SPECIAL   | 100ms           | Pose transition           |
| ANY       | ULTIMATE  | 0ms             | Hard cut, camera zoom     |

### Chin Physics (persistent sub-animation)
The chin has its own micro-physics that runs ON TOP of all animations:
```javascript
// Chin jiggle system -- runs every frame
chinOffset.y = Math.sin(Date.now() * 0.003) * 0.5; // gentle constant wobble
chinOffset.x = currentMovementX * 0.1; // leads in movement direction
chinOffset.scale = 1.0 + (currentSpeed / maxSpeed) * 0.1; // grows slightly at speed
// On hit: chinOffset.y += hitForce * 0.3; // chin recoils from impacts
// On attack: chinOffset.x += 2; // chin thrusts forward on attack
```

### Belly Scar System (persistent visual)
The scar has reactive behavior:
```javascript
// Scar glow system
scarGlow = 0.0; // 0.0 = normal, 1.0 = full glow
// On take damage: scarGlow = min(1.0, scarGlow + 0.3);
// On invulnerable: scarColor = GOLD;
// Decay: scarGlow -= 0.05 per frame (fades back to normal)
// Visual: scar pixels tint toward red proportional to scarGlow
```

### Faixa Physics (persistent cloth sim)
```javascript
// Simple cloth simulation for presidential sash
faixaAngle = Math.sin(Date.now() * 0.002) * 5; // base sway +/-5deg
faixaAngle += currentMovementX * -0.5; // trails behind movement
faixaAngle += windForce; // responds to nearby explosions
// Clamp: -30deg to +30deg
// On death: faixa detaches from fixed point, becomes free physics object
```
