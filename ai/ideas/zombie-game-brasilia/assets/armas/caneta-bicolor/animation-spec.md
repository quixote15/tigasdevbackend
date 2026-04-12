# Animation Spec — Caneta Bicolor (Arma do BolsoLula)

## Configuracao Phaser 3

```javascript
const CANETA_BICOLOR = {
  key: 'arma-caneta-bicolor',
  frameWidth: 40,  // caneta em mao (larga)
  frameHeight: 16,
  meleeFrameWidth: 64,  // ataque melee (area grande)
  meleeFrameHeight: 64,
  projectileFrameWidth: 24,
  projectileFrameHeight: 24,
  explosionFrameWidth: 32,
  explosionFrameHeight: 32,
  fps: 10,
};
```

---

## Animacoes

### 1. idle_hold — Caneta em mao (4 bracos)
| Propriedade | Valor |
|---|---|
| Frames | 0-3 |
| Frame rate | variavel |
| Loop | true |
| Duracao ciclo | 2000ms |

**Timing:**
- Frame 0 (600ms): Caneta horizontal, 2 bracos segurando. Tint pulse na cor dominante: se Lula domina, lado vermelho pulsa (#8B1A1A alpha 0.5 -> 1.0 -> 0.5); se Bolsonaro domina, lado verde pulsa (#2E5A1C alpha 0.5 -> 1.0 -> 0.5). Ink drip: 1 particula a cada 600ms alternando #CC0000 e #00AA00, gravity 100, lifespan 800ms
- Frame 1 (500ms): Cor dominante brilha mais forte. Aura overlay no lado dominante (circle 20px, cor correspondente, alpha 0.2, pulse). Gota de tinta caindo. A caneta PULSA organicamente: scale 1.0 -> 1.02 -> 1.0 (sin wave 500ms) — parece viva
- Frame 2 (300ms): Caneta gira 180 graus (troca de ponta). Rotacao: 0 -> 180 em 300ms, ease-in-out. SFX: whoosh_plastico + click. Transicao visual de cor (a ponta que estava em cima vai pra baixo)
- Frame 3 (600ms): Bracos livres fazendo gestos contraditorios. O sprite dos bracos extras: braco_esquerdo faz "L" (animacao 2 frames, 300ms), braco_direito faz "arminha" (animacao 2 frames, 300ms). Os gestos sao SIMULTANEOS e CONTRADITORIOS

**Evento de Troca de Lado (a cada 5000ms globais):**
- Flash overlay na caneta inteira (branco, 100ms)
- Cor dominante troca
- Tint transition: 500ms crossfade
- SFX: mode_change_lula "Assina ai, companheiro!" (800ms) OU mode_change_bolsonaro "Canetada, talkei!" (700ms)
- Particle burst: 5 particulas da COR NOVA saindo radialmente da caneta

### 2. melee_slash — Assinar Emenda (Melee)
| Propriedade | Valor |
|---|---|
| Frames | 4-6 |
| Frame rate | variavel |
| Sprite size | 64x64px |
| Loop | false |
| Duracao | 650ms |

**Timing:**
- Frame 4 (200ms): Caneta erguida acima com 4 bracos. Scale: 0.8 -> 1.2 (windup squash). Ink splatter particles: 4-6 particulas de AMBAS as cores (#CC0000 + #00AA00), radial upward. SFX: whoosh_pesado em t=0ms. Ambas as faces sorrindo (raro!) — expression overlay swap
- Frame 5 (100ms): SLASH! Caneta corta diagonalmente. Trail overlay: linha bicolor (metade vermelha, metade verde) do canto superior esquerdo ao inferior direito, alpha 1.0 -> 0.0 em 200ms. Ink splatter burst: 10-15 particulas, 360 graus, ambas cores. O trail forma letras "EC 667" momentaneamente (text sprite overlay, 200ms lifetime, alpha 1.0 -> 0.0). SFX: slash_tinta em t=0ms. Hitbox melee ativo: arc 180 graus, range 48px, dano 18HP. Camera shake: intensity 2, 80ms
- Frame 6 (350ms): Caneta bate no chao. Spawn ground_emenda sprite na posicao de impacto. A emenda no chao: circle 24px, bicolor pulsante (#CC0000/#00AA00 alternando), com texto juridico microscopico. Apos 300ms: emenda EXPLODE (transicao para emenda_explosion). SFX: pen_hit_ground em t=0ms. SFX: scribble_furioso (350ms) — som de caneta escrevendo freneticamente

**Ground Emenda Timer:**
```
t=0ms   : spawn ground_emenda sprite
t=0-300ms: emenda pulsa (scale 0.5 -> 1.0, tint pulse bicolor)
t=300ms : EXPLODE! -> transicao para emenda_explosion sequence
         Hitbox ativo: circle 24px, dano 12HP
```

### 3. ranged_launch — Lancar Emenda (Ranged)
| Propriedade | Valor |
|---|---|
| Frames | 7-10 |
| Frame rate | variavel |
| Loop | false |
| Duracao | 680ms |

**Timing:**
- Frame 7 (250ms): Caneta apontada pra frente. Ponta carregando: glow overlay na ponta (#DAA520, scale 0 -> 1.0, alpha pulse). Tinta borbulhando: bubble particles na ponta (3-5, tiny, #CC0000 ou #00AA00 conforme modo). SFX: charge_hum (250ms, pitch ascending). Faces fazem expressoes opostas (expression overlay)
- Frame 8 (80ms): DISPARO! Spawn projetil emenda_parlamentar. Projetil sai da ponta da caneta. Flash na ponta (#DAA520, 80ms). SFX: whomp_launch (200ms). Projetil velocidade: 200px/s (modo Lula) ou 320px/s (modo Bolsonaro). Ink trail emitter no projetil: frequency 50ms, cor conforme modo
- Frame 9 (150ms): Recuo. Sprite desloca -4px (4 bracos absorvem). Scale squash: 1.1x -> 1.0x em 150ms. Tinta respinga pra tras: 3-4 particulas, direcao oposta ao tiro
- Frame 10 (200ms): Recovery. Tinta na ponta se regenera (glow fade in #DAA520 -> cor_modo em 200ms). Caneta pronta. SFX: pen_ready_click

### 4. projectile_emenda — Emenda em voo
| Propriedade | Valor |
|---|---|
| Frames | 11-13 |
| Frame rate | 12.5 fps |
| Sprite size | 24x24px |
| Loop | true |
| Duracao | ate impacto ou max range (250px) |

**Comportamento:**
- Rotacao: 360 graus/s (rolo de papel girando)
- Cor varia com modo: tint lerp rosado (#FFCCCC) no modo Lula, esverdeado (#CCFFCC) no modo Bolsonaro
- Particle emitter: dollar_signs ("$", tint #DAA520, frequency 200ms, lifespan 500ms, upward drift)
- Particle emitter: stamp_flash (text "APROVADO", frequency 800ms, lifespan 300ms, random position ao redor do projetil)
- Golden glow: aura #DAA520 ao redor, alpha pulse 0.2 -> 0.5 -> 0.2 (400ms ciclo)
- Hitbox: circle 8px

### 5. emenda_explosion — Explosao de emenda
| Propriedade | Valor |
|---|---|
| Frames | 14-18 |
| Frame rate | variavel |
| Sprite size | 32x32px |
| Loop | false |
| Duracao | 930ms |

**Timing:**
- Frame 14 (60ms): Contato. Flash dourado (#DAA520, circle 16px, alpha 1.0 -> 0.0). SFX: pop_papel
- Frame 15 (120ms): EXPLOSAO BUROCRATICA! Particle burst: confete_docs (20-30 particulas, retangulares 3x6px, cores #D4C170/#DAA520/#CC0000/#00AA00, radial 360deg, velocity 100-200px/s, gravity 80, rotation random). Text overlay: "R$ 61 BILHOES" (#DAA520, scale 0 -> 1.5 -> 0, 400ms lifetime, center). SFX: cha_ching + confete_burst. Bicolor ink splash no chao: circle 32px, metade vermelha metade verde. Camera shake: intensity 1, 60ms. Hitbox: circle 24px, dano 12HP (ranged) ou 12HP (ground emenda)
- Frame 16 (200ms): Confete caindo como neve. Paper_confetti: gravity increases, flutter rotation. Alguns papeis pegam fogo: 3-4 particulas com fire overlay. Dollar signs flutuando pra cima: 3-5 "$" particulas, #DAA520, slow upward
- Frame 17 (250ms): Quase tudo pousou. Ultimos confetes. Fogo em papeis diminuindo. Cinzas: 2-3 particulas cinza subindo
- Frame 18 (300ms): Marca bicolor no chao (circle 24px, metade #CC0000 metade #00AA00, alpha 0.3). Fade out em 2000ms. Cleanup: destroi todas particulas residuais

### 6. ink_trail — Rastro de tinta no chao
| Propriedade | Valor |
|---|---|
| Tipo | Continuous trail (nao spritesheet) |
| Render | Graphics object / tileable texture |
| Loop | continuous while BolsoLula walks |

**Comportamento:**
- Renderiza 2 linhas paralelas atras do BolsoLula enquanto anda
- Linha esquerda: #CC0000 (vermelho), 2px largura
- Linha direita: #00AA00 (verde), 2px largura
- Espacamento entre linhas: 4px
- Alpha: 0.4 no ponto de criacao -> 0.0 em 3000ms (fade over time)
- Onde as linhas se cruzam (curvas fechadas): cria zona "corrupta" marrom (#8B4513)
- Hitbox das linhas: rectangle 8px largura, slow 20% para quem pisar
- Debuffs: vermelho = hipnotizado 1s, verde = confuso 1s, ambos = stun 2s

---

## Particle Systems (Phaser 3 Config)

### ink_drip
```javascript
{
  lifespan: 800,
  speed: 0,
  gravityY: 100,
  scale: { start: 0.15, end: 0.25 },
  alpha: { start: 0.8, end: 0.0 },
  // tint alternates: [0xCC0000, 0x00AA00]
  frequency: 600,
  blendMode: 'NORMAL',
}
```

### confete_docs
```javascript
{
  lifespan: 1200,
  speed: { min: 100, max: 200 },
  angle: { min: 0, max: 360 },
  scale: { start: 0.3, end: 0.2 },
  tint: [0xD4C170, 0xDAA520, 0xCC0000, 0x00AA00],
  quantity: { min: 20, max: 30 },
  gravityY: 80,
  rotate: { min: -180, max: 180 }, // flutter
  blendMode: 'NORMAL',
}
```

### dollar_signs
```javascript
{
  // Custom text particle "$"
  lifespan: 500,
  speed: { min: 10, max: 25 },
  angle: { min: 250, max: 290 }, // upward
  scale: { start: 0.3, end: 0.0 },
  alpha: { start: 0.7, end: 0.0 },
  tint: 0xDAA520,
  frequency: 200,
}
```

### ink_splatter (melee)
```javascript
{
  lifespan: 300,
  speed: { min: 60, max: 150 },
  angle: { min: 0, max: 360 },
  scale: { start: 0.2, end: 0.1 },
  tint: [0xCC0000, 0x00AA00], // both colors
  quantity: { min: 10, max: 15 },
  blendMode: 'NORMAL',
}
```

### mode_change_burst
```javascript
{
  lifespan: 400,
  speed: { min: 40, max: 100 },
  angle: { min: 0, max: 360 },
  scale: { start: 0.3, end: 0.0 },
  // tint: cor do NOVO modo (#CC0000 or #00AA00)
  quantity: 5,
  blendMode: 'ADD',
}
```

---

## Sincronizacao de Audio

### Troca de modo (a cada 5000ms)
```
t=0ms    : SFX flash_whoosh (100ms)
t=0ms    : mode_change_burst particles
t=100ms  : SE modo Lula -> SFX "assina_ai_companheiro" (800ms, volume 0.7)
           SE modo Bolsonaro -> SFX "canetada_talkei" (700ms, volume 0.7)
```

### Ataque melee completo
```
t=0ms    : melee_slash Frame 4 START
t=0ms    : SFX whoosh_pesado (200ms)
t=200ms  : Frame 5 — SLASH
t=200ms  : SFX slash_tinta (150ms, volume 0.9)
t=200ms  : ink_splatter burst
t=200ms  : Camera shake
t=300ms  : Frame 6 — Caneta no chao
t=300ms  : SFX pen_hit_ground (100ms)
t=300ms  : SFX scribble_furioso (350ms, volume 0.6)
t=300ms  : ground_emenda spawn
t=600ms  : ground_emenda EXPLODE
t=600ms  : SFX pop_papel (100ms) + cha_ching (300ms)
t=600ms  : confete_docs burst
t=600ms  : Camera shake leve
t=850ms  : cleanup
```

### Ataque ranged completo
```
t=0ms    : ranged_launch Frame 7 START
t=0ms    : SFX charge_hum (250ms, pitch ascend)
t=250ms  : Frame 8 — DISPARO
t=250ms  : SFX whomp_launch (200ms)
t=250ms  : projectile spawn
  ... projetil voa ...
t=IMPACT : emenda_explosion START
t=IMPACT : SFX pop_papel (100ms)
t=IMPACT+60: SFX cha_ching + confete_burst
t=IMPACT+60: confete_docs burst
t=IMPACT+60: Camera shake
  ... confete caindo ...
t=IMPACT+930: cleanup
```

### Bordoes random durante ataques
```
RANDOM(0.25): SFX "a_caneta_e_bicolor_igual_a_corrupcao" (1500ms, volume 0.7)
RANDOM(0.15): SFX "compan_vagabu_companhei_talkei" (1200ms, volume 0.8)
              // Ambas vozes brigando simultaneamente
              // Mixar 2 tracks: voz_lula + voz_bolsonaro com 200ms offset
```
