# Animation Spec — Arma Brochavel (Revolver Dourado do Bolsonaro)

## Configuracao Phaser 3

```javascript
const ARMA_BROCHAVEL = {
  key: 'arma-brochavel',
  frameWidth: 32,
  frameHeight: 32,
  bulletFrameWidth: 16,
  bulletFrameHeight: 16,
  impactFrameWidth: 24,
  impactFrameHeight: 24,
  fps: 10,
};
```

---

## Animacoes

### 1. idle_hold — Arma em mao
| Propriedade | Valor |
|---|---|
| Frames | 0-2 |
| Frame rate | variavel |
| Loop | true |
| Easing | none (step) |
| Duracao ciclo | 1400ms |

**Timing:**
- Frame 0 (400ms): Postura machao, duas maos. Brilho dourado pulsa: tint lerp #DAA520 <-> #FFD700 (sin wave, 800ms ciclo)
- Frame 1 (400ms): Gesto de arminha com mao livre. Lens flare sprite overlay no cano (additive blend, alpha pulse 0.0 -> 0.6 -> 0.0)
- Frame 2 (600ms): Giro no dedo. Rotacao sprite: 0 -> 720 graus em 500ms, ease-in-out. Nos ultimos 100ms: wobble (rotacao +-15 graus, 3 oscilacoes rapidas). SFX: metal_spin em t=0ms do frame, quase_drop em t=500ms

### 2. aim — Mira
| Propriedade | Valor |
|---|---|
| Frames | 3-4 |
| Frame rate | variavel |
| Loop | false |
| Duracao | 350ms |

**Timing:**
- Frame 3 (200ms): Olho fecha (concentracao). SFX: click_armar em t=0ms. Arma desloca +8px na direcao do alvo. Tint flash: #FFD700 (brilho de mira)
- Frame 4 (150ms): Arma estabilizada com TREMOR. Offset sinusoidal: X += sin(time*0.02)*1.5px, Y += cos(time*0.03)*1px. O tremor visual mostra que nao e tao bom atirador. Suor particula: 1 gota (#AAAAFF) caindo da testa.

**Apos aim:** Random roll 70/30 -> disparo OK ou falha

### 3A. fire_success — Disparo bem-sucedido (70%)
| Propriedade | Valor |
|---|---|
| Frames | 5-8 |
| Frame rate | variavel |
| Loop | false |
| Duracao | 680ms |

**Timing:**
- Frame 5 (60ms): BANG! Flash overlay (additive, circle 24px, #FFFF00, alpha 1.0 -> 0.0 em 60ms). Particle burst: muzzle_flash (8-12 particulas, frontal 90deg arc). SFX: bang_potente em t=0ms. Camera shake: intensity 2, 100ms. Spawn bullet projetil. Shell casing spawn: arco parabolico direita.
- Frame 6 (120ms): Recuo. Sprite desloca -6px na direcao oposta ao tiro. Scale squash: 0.9x horizontal, 1.1x vertical (recuo). Smoke emitter ON no cano (3 particulas, #A9A9A9)
- Frame 7 (200ms): Recovery. Sprite volta a posicao original (ease-out). Sorriso (expression swap). Mao livre aponta pro alvo (dedo esticado)
- Frame 8 (300ms): Sopra fumaca. Smoke stream do cano: 5 particulas em sequencia, direction scattered (patetico, nao cool). Lips overlay animado (2 frames, pucker). SFX: bordao random — 40% "TALKEI?!" (confiante) OU 20% "BOMBA!" OU 10% "CPF cancelado!" em t=200ms

### 3B. fire_fail — BROCHA (30%)
| Propriedade | Valor |
|---|---|
| Frames | 9-13 |
| Frame rate | variavel |
| Loop | false |
| Duracao | 1250ms |

**Timing:**
- Frame 9 (200ms): Click. Nada. SFX: click_seco (150ms, volume 0.4 — patetico). Particula "?" flutuante acima (scale 0 -> 1.0, bounce). Tint da arma: #DAA520 -> #8B6914 (fica mais fosco — menos brilho)
- Frame 10 (250ms): Olha pro cano (ERRO CRITICO). Sprite rota arma 180 graus (cano pra si). Fumacinha triste: 1-2 particulas #A9A9A9, velocidade 5px/s, muito lentas e patéticas. SFX: fumaca_triste (som de balao esvaziando, 300ms)
- Frame 11 (100ms): BACKFIRE! Flash na culatra (nao no cano): circle 16px, #FFA500, alpha 1.0 -> 0.0. Particulas de sangue: 5-8, #8B0000, radial do peito/barriga. SFX: pop_patetico em t=0ms (volume 0.6 — nao e um BANG, e um POP). Dano: self.hp -= 15% do dano_base. Camera shake: intensity 1, 80ms (leve — nem o universo leva a serio)
- Frame 12 (300ms): Cambaleando. Sprite desloca +10px pra tras (knockback self). Wobble: rotacao +-10 graus, 4 oscilacoes. Estrelinhas de dor: 3 particulas #FFFF00 girando em circulo ao redor da cabeca (radius 12px, velocidade angular 720deg/s). SFX: bolsonaro_oof (gemido de dor comico)
- Frame 13 (400ms): Recuperacao lenta. De joelhos (sprite swap temporario). Olha pra arma com RAIVA. Levanta devagar (position Y: +4px -> 0px, ease-out 400ms). SFX: bordao — 100% "Talkei..." (triste, descendente, volume 0.5) OU 50% adicional "Minha arma e brochavel..." (1200ms)

**Cooldown pos-falha:** 500ms adicional antes de poder atirar de novo (penalidade por brochar)

### 4. bullet_fly — Bala dourada em voo
| Propriedade | Valor |
|---|---|
| Frames | 14-15 |
| Frame rate | 25 fps (rapido) |
| Loop | true |
| Sprite size | 16x16px |
| Duracao | ate impacto ou max range |

**Comportamento:**
- Velocidade: 450px/s
- Alcance max: 350px
- Trail: golden_trail emitter (frequency 30ms, tint #FFD700, lifespan 200ms, scale 0.2 -> 0.0)
- Leve rotacao: 180deg/s
- Hitbox: circle 4px radius

### 5. bullet_impact — Impacto de bala
| Propriedade | Valor |
|---|---|
| Frames | 16-18 |
| Frame rate | variavel |
| Sprite size | 24x24px |
| Loop | false |
| Duracao | 310ms |

**Timing:**
- Frame 16 (60ms): Flash dourado star-shape. 4-pointed star, scale 0 -> 1.5 -> 1.0. Tint: #FFD700
- Frame 17 (100ms): Particulas douradas espalhando (6-8, radial, velocity 80px/s). Flash fade.
- Frame 18 (150ms): Residuo dourado no chao (circle 8px, alpha 0.3, fade out 500ms). Destroi sprite.

### 6. reload — Recarga
| Propriedade | Valor |
|---|---|
| Frames | 19-22 |
| Frame rate | variavel |
| Loop | false |
| Duracao | 1300ms |

**Timing:**
- Frame 19 (300ms): Cilindro abre. SFX: cylinder_open. Particulas: 4-6 shell_casings (arco parabolico, bounce, tint #B87333). Gravity: 200, bounce: 0.4
- Frame 20 (400ms): Mao no bolso. Particulas saindo: bullet, coin (#DAA520), santinho (#FFFFFF, retangular), chiclete (#FF69B4). SFX: fumble_pocket (rustling). Comico: itens voam pra todos os lados
- Frame 21 (350ms): Inserindo balas. 1-2 balas caem no chao (particula bounce). SFX: bullet_insert x3-4 (cliques metalicos). Cylinder snap shut: SFX click_metalico
- Frame 22 (250ms): Giro do cilindro. SFX: cylinder_spin (whirr). Sorriso. Arma pronta. Flash dourado de "pronto" (tint pulse #FFD700, 1 ciclo)

---

## Particle Systems (Phaser 3 Config)

### muzzle_flash
```javascript
{
  lifespan: 200,
  speed: { min: 50, max: 120 },
  angle: { min: -45, max: 45 }, // frontal arc relative to aim
  scale: { start: 0.4, end: 0.0 },
  tint: [0xFFFF00, 0xFFD700, 0xFFA500],
  quantity: { min: 8, max: 12 },
  blendMode: 'ADD',
}
```

### sad_smoke (falha)
```javascript
{
  lifespan: 800,
  speed: { min: 3, max: 8 },
  angle: { min: 260, max: 280 },
  scale: { start: 0.15, end: 0.4 },
  alpha: { start: 0.4, end: 0.0 },
  tint: 0xA9A9A9,
  quantity: { min: 1, max: 3 },
  blendMode: 'NORMAL',
}
```

### pain_stars (self-damage)
```javascript
{
  // Orbital motion, nao emitter padrao
  // 3 estrelas girando ao redor da cabeca
  lifespan: 1500,
  speed: 0, // orbital, nao linear
  scale: { start: 0.3, end: 0.0 },
  tint: 0xFFFF00,
  quantity: 3,
  // Custom update: position = center + (cos/sin)(time * angularSpeed) * radius
  // angularSpeed: 720 deg/s, radius: 12px
}
```

### shell_casing
```javascript
{
  lifespan: 600,
  speed: { min: 40, max: 80 },
  angle: { min: -120, max: -60 }, // eject right-ish
  scale: 0.25,
  tint: 0xB87333,
  quantity: 1,
  gravityY: 200,
  bounce: 0.4,
}
```

### golden_trail (bala em voo)
```javascript
{
  lifespan: 200,
  speed: 0,
  scale: { start: 0.2, end: 0.0 },
  alpha: { start: 0.8, end: 0.0 },
  tint: 0xFFD700,
  frequency: 30,
  blendMode: 'ADD',
}
```

---

## Sincronizacao de Audio

### Disparo bem-sucedido
```
t=0ms     : aim START
t=0ms     : SFX click_armar (100ms)
t=350ms   : fire_success START
t=350ms   : SFX bang_potente (400ms, volume 1.0)
t=350ms   : SFX shell_casing_tink (200ms, volume 0.3, delay 150ms)
t=410ms   : recoil
t=530ms   : recovery
t=730ms   : SFX blow_smoke (300ms, volume 0.2)
t=730ms   : RANDOM(0.4) -> "TALKEI?!" (600ms, volume 0.9, confiante)
           : RANDOM(0.2) -> "BOMBA!" (400ms, volume 1.0)
           : RANDOM(0.1) -> "CPF cancelado!" (800ms, volume 0.8)
```

### Falha / Brocha
```
t=0ms     : aim START
t=0ms     : SFX click_armar (100ms)
t=350ms   : fire_fail START
t=350ms   : SFX click_seco (150ms, volume 0.4)
t=550ms   : SFX silencio_constrangedor (250ms — literalmente silencio com reverb ambiente)
t=600ms   : SFX fumaca_balao (300ms, volume 0.3)
t=850ms   : SFX pop_patetico (200ms, volume 0.6)
t=850ms   : SFX bolsonaro_oof (300ms, volume 0.7)
t=950ms   : pain_stars START
t=1150ms  : SFX "Talkei..." (800ms, volume 0.5, pitch descendente)
           : RANDOM(0.5) -> "Minha arma e brochavel..." (1200ms, volume 0.6)
t=1600ms  : COOLDOWN 500ms (nao pode atirar)
```

### Recarga
```
t=0ms     : SFX cylinder_open (200ms)
t=0ms     : shell_casings particles
t=300ms   : SFX fumble_pocket (400ms, volume 0.5)
t=700ms   : SFX bullet_insert x3 (100ms cada, intervalo 80ms)
t=1050ms  : SFX cylinder_snap (100ms)
t=1050ms  : SFX cylinder_spin (200ms)
t=1250ms  : SFX pronto_click (50ms)
```
