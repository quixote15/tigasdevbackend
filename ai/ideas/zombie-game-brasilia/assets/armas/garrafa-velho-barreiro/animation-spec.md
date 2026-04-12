# Animation Spec — Garrafa de Velho Barreiro Incendiaria

## Configuracao Phaser 3

```javascript
// Sprite sheet config
const VELHO_BARREIRO = {
  key: 'arma-velho-barreiro',
  frameWidth: 32,  // projetil
  frameHeight: 32,
  explosionFrameWidth: 48,  // explosao e poca
  explosionFrameHeight: 48,
  fps: 10, // base fps estilo jerky Andre Guedes
};
```

---

## Animacoes

### 1. idle_hold — Garrafa em mao
| Propriedade | Valor |
|---|---|
| Frames | 0-1 |
| Frame rate | 2 fps (lento, bebado) |
| Loop | true |
| Easing | none (step) |
| Duracao total | 1000ms/loop |

**Notas de animacao:**
- Frame 0 (500ms): Garrafa parada, liquido centralizado
- Frame 1 (500ms): Liquido deslocado pra direita (balanco de bebado)
- Transicao entre frames: CUT direto, sem interpolacao (estilo jerky)
- Adicionar leve sway na posicao Y: sin(time * 0.002) * 2px

### 2. ignite — Acender pavio
| Propriedade | Valor |
|---|---|
| Frames | 2-4 |
| Frame rate | variavel |
| Loop | false |
| Easing | none (step) |
| Duracao total | 450ms |

**Timing detalhado:**
- Frame 2 (150ms): Isqueiro aproxima. SFX: click de isqueiro em t=0ms
- Frame 3 (100ms): Faisca. Particle emitter ON: fire_spark (2-4 particulas). SFX: fwoosh em t=150ms
- Frame 4 (200ms): Pavio aceso. Particle emitter ON: fire_wick (loop contínuo). SFX: crackle loop START em t=250ms
- Callback onComplete: transicao para throw_ready state

### 3. throw — Arremesso
| Propriedade | Valor |
|---|---|
| Frames | 5-8 |
| Frame rate | variavel |
| Loop | false |
| Easing | custom |
| Duracao total | 460ms |

**Timing detalhado:**
- Frame 5 (120ms): Windup. Sprite desloca -8px X (puxa pra tras). SFX: grunt do Lula em t=0ms. Camera shake: 0
- Frame 6 (80ms): Braco no topo. Sprite desloca +4px Y (sobe). Anticipation frame.
- Frame 7 (60ms): RELEASE! Spawn projetil na posicao da mao. SFX: whoosh em t=200ms. Projetil inicia com velocidade 280px/s na direcao do target. Particle burst: fumaca (3 particulas)
- Frame 8 (200ms): Follow-through/recovery. Sprite desloca +4px X (cambaleio). Sway: sin curve 6px amplitude. Lula quase cai. SFX: bordao random 30% ("Vai uma Velho Barreiro, companheiro!") em t=260ms

**Easing custom:**
```
Frame 5-6: ease-in (acelerando)
Frame 7: instant (snap)
Frame 8: ease-out com bounce (cambaleio de bebado)
```

### 4. projectile_fly — Projetil em voo
| Propriedade | Valor |
|---|---|
| Frames | 9-12 |
| Frame rate | 12.5 fps (rapido) |
| Loop | true |
| Easing | linear rotation |
| Duracao total | 320ms/loop |

**Comportamento:**
- Rotacao: 360 graus por loop (90 graus por frame)
- Velocidade: 280px/s linear
- Alcance max: 200px (depois cai)
- Trail emitter: smoke_trail (1 particula/frame, lifetime 600ms)
- Trail emitter 2: fire_trail (2 particulas/frame, lifetime 300ms)
- Se alcance max atingido sem impacto: transicao para fall_arc (arco parabolico descendente + impacto no chao)

**Fisica do projetil:**
```
velocityX: cos(angle) * 280
velocityY: sin(angle) * 280
rotation: += 5.625 graus/frame (360/64 para rotacao suave)
gravity: 0 (arremesso reto)
```

### 5. impact_explosion — Impacto e explosao
| Propriedade | Valor |
|---|---|
| Frames | 13-18 |
| Frame rate | variavel |
| Loop | false |
| Sprite size | 48x48px |
| Easing | ease-out |
| Duracao total | 1010ms |

**Timing detalhado:**
- Frame 13 (60ms): Contato com chao. Flash branco (additive blend, opacity 1.0 -> 0.0 em 60ms). SFX: CRASH de vidro em t=0ms. Camera shake: intensity 3, duration 200ms
- Frame 14 (100ms): EXPLOSAO! Particle burst: glass_shards (8-12 particulas, radial, velocity 200px/s, gravity 300, bounce 0.3). Particle burst: fire_splash (15 particulas, radial, velocity 150px/s). Particle burst: liquid_splash (10 particulas, amber, velocity 100px/s). SFX: WHOOMPF em t=60ms. Scale: 0.5 -> 1.5 em 100ms (squash and stretch). Hitbox ativo: 48px raio, dano 25HP
- Frame 15 (150ms): Chamas no maximo. Emitter ON: ground_fire (loop, 6 particulas/frame, cores #FF6B00 + #3355AA). Emitter ON: dense_smoke (3 particulas/frame, #5A5A4A). Scale normaliza: 1.5 -> 1.0
- Frame 16 (200ms): Chamas diminuindo. Emitter rate: ground_fire reduz para 3/frame. Emitter ON: stink_lines (sinusoidal, #4A7A3A, 3 instancias). Opacity: 1.0 -> 0.8
- Frame 17 (200ms): Fogo menor. Emitter rate: ground_fire reduz para 1/frame. Cacos de vidro pousando (glass_shards gravity completes). Opacity: 0.8 -> 0.6
- Frame 18 (300ms): Transicao para poca persistente. Sprite swap para pool_hazard spritesheet. Emitters transicionam.

### 6. pool_hazard — Poca persistente no chao
| Propriedade | Valor |
|---|---|
| Frames | 19-21 |
| Frame rate | 3.3 fps (lento) |
| Loop | true |
| Sprite size | 48x48px |
| Duracao total | 4000ms (entao destroi) |

**Comportamento:**
- Loop continuo por 4000ms
- Scale: 1.0 -> 0.7 ao longo de 4000ms (poca encolhendo)
- Opacity: 0.8 -> 0.3 ao longo de 4000ms (poca apagando)
- Emitter: low_fire (2 particulas/frame, #FF6B00 + #3355AA, lifetime 400ms)
- Emitter: stink_lines (1 particula/500ms, sinusoidal #4A7A3A, lifetime 1000ms)
- Emitter: bubbles (1 particula/800ms, #B8860B, lifetime 300ms, upward)
- SFX: crackle loop (volume fade 1.0 -> 0.0 ao longo de 4000ms)
- SFX: bubble pop random (1x a cada 800ms, volume 0.3)
- Hitbox: circulo 24px raio (encolhe com a poca)
- Dano: 5HP/s para qualquer entidade no hitbox
- Debuff on enter: controles invertidos 3000ms (flag: drunk=true)
- On debuff apply: SFX "Companheiro alcool em mim!" (1200ms, volume 0.7)

**Destruicao:**
- Em t=4000ms: fade out final 500ms
- Emitters: stop com fade
- Ultimo SFX: tiny fizzle (100ms)
- Destroi sprite e hitbox

---

## Particle Systems (Phaser 3 Config)

### fire_spark
```javascript
{
  lifespan: 300,
  speed: { min: 30, max: 80 },
  angle: { min: 250, max: 290 }, // upward
  scale: { start: 0.3, end: 0.0 },
  tint: [0xFF6B00, 0xFFD700, 0xFF4500],
  quantity: { min: 2, max: 4 },
  blendMode: 'ADD',
}
```

### fire_wick (loop enquanto pavio aceso)
```javascript
{
  lifespan: 300,
  speed: { min: 10, max: 30 },
  angle: { min: 260, max: 280 },
  scale: { start: 0.2, end: 0.0 },
  tint: [0xFF6B00, 0xFFD700],
  frequency: 100, // 1 a cada 100ms
  blendMode: 'ADD',
}
```

### smoke_trail (durante voo)
```javascript
{
  lifespan: 600,
  speed: { min: 5, max: 15 },
  angle: { min: 260, max: 280 },
  scale: { start: 0.2, end: 0.5 },
  alpha: { start: 0.6, end: 0.0 },
  tint: 0x5A5A4A,
  frequency: 80,
  blendMode: 'NORMAL',
}
```

### glass_shards (na explosao)
```javascript
{
  lifespan: 800,
  speed: { min: 100, max: 250 },
  angle: { min: 0, max: 360 },
  scale: { start: 0.3, end: 0.2 },
  tint: [0x8B6914, 0x3B2610, 0x7A5C2E],
  quantity: { min: 8, max: 12 },
  gravityY: 300,
  bounce: 0.3,
  blendMode: 'NORMAL',
}
```

### stink_lines (cheiro da cachaca)
```javascript
{
  // Custom: usar path sinusoidal em vez de emitter padrao
  // Cada "linha de cheiro" e um graphics object com sine wave
  // amplitude: 4px, frequencia: 0.01, velocidade Y: -20px/s
  lifespan: 1000,
  speed: { min: 15, max: 25 },
  angle: { min: 260, max: 280 },
  alpha: { start: 0.3, end: 0.0 },
  tint: 0x4A7A3A,
  frequency: 500,
  // Render como sine wave path, nao particula pontual
}
```

---

## Sincronizacao de Audio (Timeline)

### Sequencia completa: acender + arremessar + impacto
```
t=0ms      : ignite START
t=0ms      : SFX click_isqueiro (150ms)
t=150ms    : SFX fwoosh_ignite (200ms)
t=250ms    : SFX crackle_loop START
t=450ms    : throw START
t=450ms    : SFX lula_grunt (200ms)
t=650ms    : SFX whoosh_throw (300ms)
t=710ms    : crackle_loop volume 0.5 (projetil se afasta)
t=710ms    : projectile_fly START
t=710ms    : SFX whistle_descend START (loop)
  ... projetil voa ...
t=IMPACT   : SFX whistle_descend STOP
t=IMPACT   : SFX crash_vidro (300ms)
t=IMPACT+60: SFX whoompf_fire (400ms)
t=IMPACT+60: Camera shake 200ms
t=IMPACT+60: SFX crackle_ground START (loop, 4000ms fade)
  ... poca ativa ...
t=IMPACT+4060: SFX crackle_ground STOP (faded to 0)
t=IMPACT+4060: SFX fizzle_out (100ms)
```

### Bordao random (30% de chance no arremesso)
```
t=710ms    : RANDOM(0.3) -> SFX "vai_uma_velho_barreiro_companheiro" (1500ms, volume 0.8)
```

### Debuff audio (quando inimigo pisa na poca)
```
t=STEP     : SFX "companheiro_alcool_em_mim" (1200ms, volume 0.7)
t=STEP     : SFX drunk_stumble (500ms, volume 0.5)
```
