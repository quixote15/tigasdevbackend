# FUMACA SANTA -- Sprite Sheet de Particulas
### O Ataque Mais Poderoso do Jogo | Efeito de Particula
### Zumbis de Brasilia | Abril 2026

---

> *"A fumaca santa nao e fumaca normal. E a manifestacao FISICA da fe do Daciolo. E dourada porque e DIVINA. E quente porque QUEIMA o pecado. E quando toca um zumbi, ele vira po. Porque o mal nao resiste a fe genuina."*

---

## Specs Tecnicas

| Propriedade | Valor |
|---|---|
| Tamanho por frame | 16x16px |
| Total de frames | 8 |
| Sheet total | 128x16px (horizontal) |
| Formato | PNG com transparencia |
| Frame rate | 10 fps |
| Loop | Sim (ciclo continuo durante efeito) |
| Estilo | Organico, fluido, dourado-branco |

---

## Frame-by-Frame

### Frame 1 -- Nascimento da Particula
```
16x16px. Centro do frame.

Ponto de fumaca NASCENDO. Formato: circulo irregular pequeno (4x4px no centro).
Cor: dourado INTENSO (#FFD700), opacidade 100%. Borda IRREGULAR (nao circular
perfeito -- organico, Andre Guedes). 1px de glow ao redor (branco 50% opacity).

E o INICIO da fumaca divina. O momento em que a fe se torna materia.
```

### Frame 2 -- Expansao Inicial
```
16x16px. Centro do frame.

Fumaca EXPANDIU para 6x6px. Formato: mais irregular, AMORFO, tentaculos de fumaca
comecando a sair (2-3 wisps curtos). Cor: dourado (#FFD700) centro, dourado-claro
(#FFE44D) nas bordas. Opacidade 95%. Glow 2px.

A fumaca ganha FORMA. Organica. Viva. Como se tivesse vontade propria.
```

### Frame 3 -- Rotacao Inicial
```
16x16px.

Fumaca 8x8px. Comeca a GIRAR (wisps curvam em sentido horario). Formato: espiral
nascente. Centro: branco (#FFFFFF, transicao de dourado para branco). Bordas:
dourado. Opacidade 90%. Trail de 1-2px atras de cada wisp (transparencia gradiente).

A rotacao e a ASSINATURA da fumaca santa. Espiral divina. Geometria sagrada.
```

### Frame 4 -- Pico de Intensidade
```
16x16px.

Fumaca 10x10px. PICO de brilho e tamanho. Centro: branco PURO (#FFFFFF).
Meio: dourado claro (#FFE44D). Bordas: dourado (#FFD700). Espiral mais pronunciada.
Opacidade 100% no centro, 80% nas bordas. Glow 3px (maximo).

Wisps mais longos (4-5px saindo do corpo principal). Detalhes: micro-cruzes (+)
dentro da fumaca (1x1px, mal visiveis mas ESTAO LA -- easter egg visual).

Este e o frame de MAXIMO PODER. A particula no auge.
```

### Frame 5 -- Inicio da Dissolucao
```
16x16px.

Fumaca 10x10px mantida mas comeca a ficar TRANSLUCIDA. Centro: branco 80%.
Bordas comecam a se separar do corpo (fragmentacao). Wisps se alongam e afinam.
Opacidade geral 75%. Glow diminui para 2px.

A fumaca cumpriu seu proposito. Comeca a retornar ao divino.
```

### Frame 6 -- Fragmentacao
```
16x16px.

Fumaca FRAGMENTOU em 3-4 pedacos menores. Cada pedaco: 3x3px, espaçados.
Cor: dourado claro (#FFE44D) -> branco. Opacidade 60%. Rotacao continua
individualmente em cada fragmento.

Wisps se SEPARARAM do corpo. Cada um vira uma mini-particula independente.
A unidade divina se multiplica.
```

### Frame 7 -- Dissipacao Avancada
```
16x16px.

Fragmentos diminuiram para 2x2px cada. Espalhados pelo frame (dispersao).
Cor: quase todo branco, tracos de dourado. Opacidade 35%. Glow minimo (1px).

Quase transparente. A fumaca retornando ao plano espiritual.
```

### Frame 8 -- Dissolucao Final
```
16x16px.

1-2 pixels restantes. PONTOS minusculos de luz branca. Opacidade 15%.
Praticamente invisivel. O ULTIMO brilho antes do desaparecimento.

A particula deixa o plano fisico. Mas o efeito ja foi feito.
Os zumbis ja sao po.
```

---

## Comportamento no Phaser 3 (Particle Emitter)

### Configuracao do Emitter Principal

```javascript
// A Fumaca Santa usa DOIS emitters: principal (fumaca) + detalhes (cruzes)

// Emitter 1: Fumaca principal
const fumacaSantaConfig = {
    frame: { frames: [0, 1, 2, 3, 4, 5, 6, 7], cycle: true },
    x: 0,
    y: 0,
    lifespan: { min: 1200, max: 2000 },
    speed: { min: 20, max: 80 },
    angle: { min: 0, max: 360 },  // radial, TODAS as direcoes
    scale: { start: 0.8, end: 2.5 },
    alpha: { start: 0.7, end: 0 },
    rotate: { min: 0, max: 360 },
    tint: [0xFFD700, 0xFFE44D, 0xFFFFFF],
    blendMode: Phaser.BlendModes.ADD,  // blend aditivo = brilho
    frequency: 20,   // 1 particula a cada 20ms = 50/s durante efeito
    quantity: 3,
    radial: true,
    emitZone: {
        type: 'random',
        source: new Phaser.Geom.Circle(0, 0, 8),  // comeca pequeno
        quantity: 3
    }
};

// Emitter 2: Micro-cruzes dentro da fumaca
const crucesConfig = {
    frame: 'micro-cruz',  // sprite separado 4x4px
    lifespan: { min: 800, max: 1500 },
    speed: { min: 15, max: 60 },
    angle: { min: 0, max: 360 },
    scale: { start: 0.5, end: 0.1 },
    alpha: { start: 0.6, end: 0 },
    rotate: { min: 0, max: 180 },
    tint: 0xFFFFFF,
    blendMode: Phaser.BlendModes.ADD,
    frequency: 80,  // menos frequente que a fumaca
    quantity: 1,
    radial: true
};
```

### Fases de Expansao

```javascript
executeFumacaSanta(originX, originY, maxRadius) {
    const emitter = this.add.particles('fumaca-santa-particle');
    const mainEmit = emitter.createEmitter(fumacaSantaConfig);
    const cruzEmit = emitter.createEmitter(crucesConfig);

    mainEmit.setPosition(originX, originY);
    cruzEmit.setPosition(originX, originY);

    // FASE 1: Concentracao (0-300ms)
    // Particulas puxadas PARA o centro (vacuum)
    mainEmit.setSpeed({ min: -30, max: -10 });  // velocidade negativa = para dentro
    mainEmit.setScale({ start: 0.3, end: 0.1 });

    // FASE 2: Detonacao (300ms)
    this.time.delayedCall(300, () => {
        mainEmit.setSpeed({ min: 30, max: 100 });  // EXPLODE para fora
        mainEmit.setScale({ start: 0.8, end: 2.5 });
        mainEmit.setFrequency(10);  // DOBRA a frequencia
        mainEmit.setQuantity(6);
    });

    // FASE 3: Expansao (300-1500ms)
    // Raio do emitZone cresce gradualmente
    const expansion = { radius: 8 };
    this.tweens.add({
        targets: expansion,
        radius: maxRadius,
        duration: 1200,
        ease: 'Quad.easeOut',
        onUpdate: () => {
            mainEmit.setEmitZone({
                type: 'random',
                source: new Phaser.Geom.Circle(0, 0, expansion.radius)
            });
            cruzEmit.setEmitZone({
                type: 'random',
                source: new Phaser.Geom.Circle(0, 0, expansion.radius * 0.8)
            });
        }
    });

    // FASE 4: Pico (1500-2000ms)
    // Manter no maximo

    // FASE 5: Dissipacao (2000-3500ms)
    this.time.delayedCall(2000, () => {
        mainEmit.setFrequency(50);  // reduz
        mainEmit.setQuantity(1);
        mainEmit.setAlpha({ start: 0.4, end: 0 });

        // Para completamente
        this.time.delayedCall(1500, () => {
            mainEmit.stop();
            cruzEmit.stop();
            // Cleanup apos ultimas particulas morrerem
            this.time.delayedCall(2000, () => {
                emitter.destroy();
            });
        });
    });
}
```

### Interacao com Zumbis (Destruicao Dourada)

```javascript
// Quando fumaca toca zumbi: efeito especial de destruicao
onFumacaTouchesZombie(zombie) {
    // Zumbi vira PO DOURADO (nao morre normal)
    const poDorado = this.add.particles('gold-dust').createEmitter({
        x: zombie.x,
        y: zombie.y,
        speed: { min: 10, max: 40 },
        angle: { min: 0, max: 360 },
        scale: { start: 0.5, end: 0 },
        alpha: { start: 0.9, end: 0 },
        tint: [0xFFD700, 0xFFA500, 0xFFFFFF],
        lifespan: { min: 400, max: 800 },
        quantity: 15,
        maxParticles: 15,
        blendMode: Phaser.BlendModes.ADD
    });

    // Flash branco no zumbi antes de desintegrar
    zombie.setTint(0xFFFFFF);
    this.tweens.add({
        targets: zombie,
        alpha: 0,
        scaleX: 1.3,
        scaleY: 0.5,
        duration: 200,
        onComplete: () => {
            zombie.destroy();
            this.time.delayedCall(800, () => poDorado.stop());
        }
    });
}
```

---

## Paleta de Cores da Fumaca

| Fase | Cor Central | Cor Media | Cor Borda | Opacity |
|---|---|---|---|---|
| Nascimento | `#FFD700` | -- | -- | 100% |
| Expansao | `#FFD700` | `#FFE44D` | `#FFE44D` | 95% |
| Rotacao | `#FFFFFF` | `#FFD700` | `#FFD700` | 90% |
| Pico | `#FFFFFF` | `#FFE44D` | `#FFD700` | 100% |
| Dissolucao 1 | `#FFFFFF` 80% | `#FFE44D` | `#FFD700` | 75% |
| Fragmentacao | `#FFE44D` | -- | -- | 60% |
| Dissipacao | `#FFFFFF` | -- | `#FFD700` traces | 35% |
| Final | `#FFFFFF` | -- | -- | 15% |

---

## Blend Mode e Layering

```
ORDEM DE RENDERIZACAO (back to front):

1. Background / mapa
2. Sombra da fumaca no chao (circulos escuros, opacity 15%)
3. Inimigos/aliados
4. Fumaca principal (blend: ADD)
5. Micro-cruzes (blend: ADD)
6. Daciolo (silhueta no centro)
7. Aureola glow (blend: ADD)
8. Flash de detonacao (overlay, blend: SCREEN)
9. Ondas de choque (overlay)
```

---

## Notas de Otimizacao

- Limitar particulas simultaneas a 200 (performance)
- Usar object pooling para as particulas (evitar GC)
- Em dispositivos low-end: reduzir frequency para 40ms, quantity para 2
- Fumaca LONGE da camera: reduzir resolucao de particula pela metade
- O blend mode ADD e CARO -- monitorar FPS durante Fumaca Santa
- Fallback low-end: substituir por circulo expandindo com alpha fade (sem particulas)
