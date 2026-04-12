# Atmosphere Spec — Esplanada dos Ministerios

> "Brasilia nao e so cenario. Brasilia e PERSONAGEM."
> A atmosfera e 50% do horror-comedia. Sem ela, e um tilemap generico.

---

## 1. Ceu Laranja-Sangue (Background Permanente)

O apocalipse congelou Brasilia as 15h de uma tarde de abril. O ceu NUNCA muda.

### Gradiente Permanente
```
Posicao no canvas:
┌─────────────────────────────────────┐
│  #2D0A0A  — Noite Morta (topo)      │  ← 100% do gradient
│                                     │
│  #8B0000  — Vermelho Queimado       │  ← 45-55%
│                                     │
│  #D47820  — Laranja Niemeyer        │  ← 20-30%
│                                     │
│  #FF6B35  — Laranja Sangue (base)   │  ← 0% (horizonte)
├─────────────────────────────────────┤
│  TILEMAP COMECA AQUI                │
└─────────────────────────────────────┘
```

### Implementacao Phaser 3
```javascript
// GameScene.create() — Layer 0: Background
const skyGradient = this.add.graphics();
skyGradient.fillGradientStyle(
    0x2D0A0A, 0x2D0A0A,  // top
    0xFF6B35, 0xFF6B35,  // bottom
    1, 1, 1, 1           // alphas
);
skyGradient.fillRect(0, 0, config.width, SKY_HEIGHT);
skyGradient.setScrollFactor(0); // Nao scrolla com camera
skyGradient.setDepth(-1000);
```

### Efeito de Pulso
O ceu tem um pulso sutil que simula "respiracao" do apocalipse:
- **Frequencia:** 0.1 Hz (1 ciclo a cada 10 segundos)
- **Amplitude:** Alpha varia de 0.95 a 1.0
- **Efeito:** Imperceptivel conscientemente, mas gera desconforto subliminar

---

## 2. Gas Verde Doentio (Particulas Flutuantes)

Emendas parlamentares liquefazeitas em estado gasoso. Onipresente. Mais denso perto do Congresso.

### Specs da Particula
| Parametro | Valor |
|---|---|
| **Sprite** | Circulo difuso 8x8px, `#4A7C59` |
| **Alpha** | 0.15 — 0.40 (aleatorio por particula) |
| **Tamanho** | Scale 0.5 — 2.0 (aleatorio) |
| **Velocidade** | 5 — 15 px/s horizontal (vento leve) |
| **Direcao** | Predominante esquerda→direita (vento de Brasilia) |
| **Ondulacao vertical** | Sine wave, amplitude 3px, freq 0.3Hz |
| **Lifetime** | 8 — 15 segundos |
| **Spawn rate** | 3 — 5 particulas/segundo |
| **Max particulas** | 30 (pool fixo para performance) |
| **Densidade por zona** | Normal: 100%, Perto Congresso: 200%, Bordas: 50% |

### Implementacao Phaser 3
```javascript
// Emitter de gas — Layer 4 (VFX)
const gasEmitter = this.add.particles(0, 0, 'gas-particle', {
    x: { min: 0, max: MAP_WIDTH },
    y: { min: 0, max: MAP_HEIGHT },
    scale: { min: 0.5, max: 2.0 },
    alpha: { start: 0.3, end: 0 },
    speed: { min: 5, max: 15 },
    angle: { min: -10, max: 10 },
    lifespan: { min: 8000, max: 15000 },
    frequency: 200,     // 1 particula a cada 200ms = 5/s
    maxParticles: 30,
    blendMode: 'ADD'    // Brilho esverdeado
});
```

### Sprite do Gas (8x8px)
```
Arte do sprite gas-particle.png:
   ░░░░░░░░
   ░░▒▒▒▒░░
   ░▒▓▓▓▓▒░
   ░▒▓██▓▒░
   ░▒▓██▓▒░
   ░▒▓▓▓▓▒░
   ░░▒▒▒▒░░
   ░░░░░░░░

Onde: ░=transparente, ▒=#4A7C59 alpha 20%, ▓=#4A7C59 alpha 40%, █=#4A7C59 alpha 60%
Borda difusa — NUNCA hard edge
```

---

## 3. Santinhos Voando (Particulas de Papel)

Panfletos eleitorais voam pelo ar como folhas de outono. O principal efeito visual de "apocalipse eleitoral".

### Sprite Sheet (16x16, 4 frames)
```
Frame 0: Santinho de frente (retangulo 6x8px creme, texto ilegivel)
Frame 1: Santinho girando 45deg (mais fino, perspectiva)
Frame 2: Santinho de lado (linha fina 1x8px)
Frame 3: Santinho girando -45deg (oposto do frame 1)
```

### Specs da Particula
| Parametro | Valor |
|---|---|
| **Sprite** | santinho-flying.png (spritesheet 4 frames) |
| **Cor** | `#F0E8D0` com variacao +-5% por particula |
| **Alpha** | 0.6 — 0.9 |
| **Tamanho** | Scale 0.8 — 1.2 |
| **Velocidade horizontal** | 20 — 40 px/s (vento) |
| **Velocidade vertical** | -5 — +5 px/s (oscilacao) |
| **Rotacao** | Animacao de 4 frames a 6fps |
| **Turbulencia** | Sine wave vertical, amplitude 5px, freq 0.5Hz |
| **Lifetime** | 10 — 20 segundos |
| **Spawn rate** | 1 — 2 particulas/segundo |
| **Max particulas** | 15 (pool fixo) |
| **Spawn zone** | Borda esquerda do viewport + area acima |

### Comportamento
- Santinhos entram pela esquerda e saem pela direita (vento)
- Alguns grudam temporariamente no chao (despawnam suave)
- Quando o player passa correndo, 2-3 santinhos extras sao lancados (interacao)
- Nunca param no ar — sempre em movimento

---

## 4. Vento Carregando Papel (Efeito de Particula Secundario)

Fragmentos menores de papel/poeira que reforçam a sensacao de vento.

### Specs
| Parametro | Valor |
|---|---|
| **Sprite** | Retangulo 2x3px, branco-sujo `#E8E0D0` |
| **Alpha** | 0.3 — 0.5 |
| **Velocidade** | 30 — 60 px/s (mais rapido que santinhos) |
| **Direcao** | Esquerda → Direita, leve inclinacao |
| **Lifetime** | 3 — 6 segundos |
| **Spawn rate** | 5 — 8 por segundo |
| **Max particulas** | 20 |

---

## 5. Congresso Pulsante (Background Animado)

O Congresso Nacional ao fundo do mapa pulsa com luz verde sinistra entre as cupulas.

### Sprite do Congresso (Background)
- **Tamanho:** 128x48px (silhueta low-detail)
- **Cor base:** `#1A1A18` (quase preto)
- **Posicao:** Centro do background, acima do horizonte
- **Parallax:** scrollFactor 0.3 (se move lento quando camera se move)

### Efeito de Pulso
```javascript
// Brilho verde entre as cupulas
const congressGlow = this.add.pointlight(
    CONGRESS_X, CONGRESS_Y,
    0x3D6B3A,     // cor verde
    100,          // raio
    0.3           // intensidade base
);
// Pulso sinistro
this.tweens.add({
    targets: congressGlow,
    intensity: { from: 0.2, to: 0.5 },
    duration: 3000,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

### Silhueta do Congresso (128x48px)
```
Simplificacao top-down da vista frontal:
                 ___
    ___         /   \         ___
   /   \   ___/     \___    /   \
  |     | |             |  |     |
  |  C  | |   TORRES    |  |  S  |
  | AMA | |             |  | ENA |
  | RA  | |_____________|  | DO  |
  |_____|                  |_____|

C = Cupula concava (Camara) — formato de prato
S = Cupula convexa (Senado) — formato de domo
Torres = 2 torres gemeas entre as cupulas

Brilho verde emana do espaco entre as torres.
```

---

## 6. Atmosfera Sonora (Referencia Audio)

**NAO sao assets visuais, mas precisam ser referenciados para coerencia.**

| Som | Tipo | Loop | Volume | Notas |
|---|---|---|---|---|
| **Vento com papel** | Ambiente | Sim | 30% | Base constante. Papers rustling + wind |
| **Alarmes distantes** | Ambiente | Sim | 15% | Sirenes longinquas, esporadicas |
| **AC zumbindo** | Ambiente | Sim | 10% | Hum eletrico constante. Perto de ministerios |
| **Discursos distorcidos** | Ambiente | Sim | 5% | Vozes invertidas/reverso. Alto-falante longe |
| **Corvos** | Pontual | Nao | 20% | A cada 30-60s. 1-2 grasnados |
| **Metal rangendo** | Pontual | Nao | 15% | Postes tombados ao vento. A cada 45s |
| **Eco de passos** | Contextual | — | 25% | Quando player esta perto de ministerios |

### Mix de Audio por Zona
| Zona | Vento | Alarmes | AC | Discursos | Extras |
|---|---|---|---|---|---|
| Gramados | 100% | 50% | 0% | 30% | Corvos |
| Eixo Monumental | 80% | 80% | 0% | 50% | Metal rangendo |
| Perto de Ministerios | 40% | 30% | 100% | 80% | Eco de passos |
| Perto do Espelho | 60% | 20% | 0% | 20% | Agua (novo) |
| Perto do Congresso | 30% | 100% | 50% | 100% | Pulso grave (novo) |

---

## 7. Iluminacao

### Nao ha sistema de iluminacao dinamica (performance)
Em vez disso, a iluminacao e "pintada" nos tiles:
- Tiles no centro do mapa: mais claros (luz do ceu laranja)
- Tiles perto de ministerios: sombras pintadas (hachura, mais escuros)
- Tiles perto do espelho d'agua: reflexo esverdeado pintado

### Efeito de Sombra dos Ministerios
Os blocos ministeriais projetam sombras longas (fim de tarde):
- **Direcao:** Nordeste → Sudoeste (sol a noroeste, 15h)
- **Implementacao:** Tiles especificos de "sombra" (overlay com alpha 30% preto) colocados no Ground layer ao lado dos ministerios
- **Comprimento:** 3-4 tiles de distancia do edificio

### Vinheta nas Bordas
```javascript
// Vinheta escura nas bordas da camera
const vignette = this.add.graphics();
// Gradiente radial: centro transparente, bordas escuras
vignette.setScrollFactor(0);
vignette.setDepth(900); // Acima de tudo exceto HUD
vignette.setAlpha(0.4);
```

---

## 8. Efeitos Climaticos (Futuro)

Para expansoes pos-MVP:
- **Chuva acida:** Particulas finas descendo, amareladas
- **Tempestade de santinhos:** Wave especial com 10x santinhos
- **Eclipse parcial:** Escurece 30%, gas fica mais visivel
- **Nevoeiro burocrático:** Fog of war verde perto do Congresso

---

## 9. Checklist de Producao

- [ ] Criar sprite gas-particle.png (8x8, difuso verde)
- [ ] Criar spritesheet santinho-flying.png (16x16, 4 frames)
- [ ] Criar sprite fragmento-papel.png (2x3, branco-sujo)
- [ ] Criar sprite congresso-silhouette.png (128x48, preto)
- [ ] Implementar gradiente de ceu no GameScene
- [ ] Configurar particle emitters (gas, santinhos, papel)
- [ ] Implementar pulso do Congresso (PointLight + tween)
- [ ] Criar tiles de sombra dos ministerios
- [ ] Aplicar vinheta nas bordas
- [ ] Testar performance com todos os emitters ativos (target: 60fps, max 30+15+20 = 65 particulas)
