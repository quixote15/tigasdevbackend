# ALCKMIN (Alcool em Mim) - Animation Specification

## Phaser 3 Sprite Sheet Loading

```javascript
// Personagem principal (64x64)
this.load.spritesheet('npc_alckmin_idle', 'assets/personagens/alckmin/sprites/alckmin_idle.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('npc_alckmin_walk', 'assets/personagens/alckmin/sprites/alckmin_walk.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('npc_alckmin_attack', 'assets/personagens/alckmin/sprites/alckmin_attack.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('npc_alckmin_death', 'assets/personagens/alckmin/sprites/alckmin_death.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('npc_alckmin_hit', 'assets/personagens/alckmin/sprites/alckmin_hit.png', {
    frameWidth: 64,
    frameHeight: 64
});
this.load.spritesheet('npc_alckmin_special', 'assets/personagens/alckmin/sprites/alckmin_special.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Projetil (32x32)
this.load.spritesheet('npc_alckmin_projetil', 'assets/personagens/alckmin/sprites/alckmin_projetil.png', {
    frameWidth: 32,
    frameHeight: 32
});
```

---

## Animation Definitions

### Animation: `alckmin_idle`
- **Type:** Loop
- **Frames:** [0, 1, 2, 3]
- **Frame Rate:** 8 fps
- **Frame Durations (individuais):**
  - Frame 0 (base): 200ms -- pausa no sorriso estavel
  - Frame 1 (tremor esquerda): 100ms -- tremor rapido
  - Frame 2 (recuperacao): 150ms -- leve pausa ao estabilizar
  - Frame 3 (tremor direita): 100ms -- tremor rapido
- **Total Cycle:** ~550ms
- **Repeat:** -1 (infinite loop)
- **Yoyo:** false (loop direto: 0 -> 1 -> 2 -> 3 -> 0)
- **Descricao:** Alckmin parado com bandeja de cafe tremendo sutilmente. O corpo fica imóvel, apenas a bandeja oscila. O sorriso NUNCA muda. Gotas de cafe pingam nos frames 1 e 3.

```javascript
this.anims.create({
    key: 'alckmin_idle',
    frames: [
        { key: 'npc_alckmin_idle', frame: 0, duration: 200 },
        { key: 'npc_alckmin_idle', frame: 1, duration: 100 },
        { key: 'npc_alckmin_idle', frame: 2, duration: 150 },
        { key: 'npc_alckmin_idle', frame: 3, duration: 100 }
    ],
    repeat: -1
});
```

---

### Animation: `alckmin_walk`
- **Type:** Loop
- **Frames:** [0, 1, 2, 3, 4, 5]
- **Frame Rate:** 10 fps (passos curtos e rapidos)
- **Frame Durations (individuais):**
  - Frame 0 (passo esq contato): 100ms
  - Frame 1 (passo esq impulso): 80ms -- rapido, bounce
  - Frame 2 (transicao): 100ms
  - Frame 3 (passo dir contato): 100ms
  - Frame 4 (passo dir impulso): 80ms -- rapido, bounce
  - Frame 5 (deslize): 120ms -- micro-pausa servil
- **Total Cycle:** ~580ms
- **Repeat:** -1
- **Yoyo:** false
- **Descricao:** Caminhada de mordomo eficiente -- passos curtos, rapidos, rasteiros. O corpo superior mal se move (bandeja estavel), apenas as pernas trabalham freneticamente. Estilo "deslizamento servil".

```javascript
this.anims.create({
    key: 'alckmin_walk',
    frames: [
        { key: 'npc_alckmin_walk', frame: 0, duration: 100 },
        { key: 'npc_alckmin_walk', frame: 1, duration: 80 },
        { key: 'npc_alckmin_walk', frame: 2, duration: 100 },
        { key: 'npc_alckmin_walk', frame: 3, duration: 100 },
        { key: 'npc_alckmin_walk', frame: 4, duration: 80 },
        { key: 'npc_alckmin_walk', frame: 5, duration: 120 }
    ],
    repeat: -1
});
```

**Walk Speed:**
- **Velocidade base:** 80 px/s (mais lento que o jogador -- ele e NPC aliado)
- **Velocidade quando seguindo Lula:** 120 px/s (corre para servir)
- **Velocidade com Mordomo Supremo ativo:** 100 px/s (multitask reduz velocidade)

---

### Animation: `alckmin_attack`
- **Type:** Play once
- **Frames:** [0, 1, 2]
- **Frame Rate:** 12 fps (rapido, estilo jerky Andre Guedes)
- **Frame Durations (individuais):**
  - Frame 0 (wind-up): 133ms -- puxa bandeja para tras
  - Frame 1 (arremesso): 83ms -- RAPIDO, pico de velocidade
  - Frame 2 (recuperacao): 166ms -- pausa com nova bandeja
- **Total Duration:** ~382ms
- **Repeat:** 0 (play once)
- **On Complete:** Return to `alckmin_idle`
- **Descricao:** Arremessa cafe quente nos inimigos. A animacao e rapida e "servil" -- ele SERVE cafe, mas como arma.

```javascript
this.anims.create({
    key: 'alckmin_attack',
    frames: [
        { key: 'npc_alckmin_attack', frame: 0, duration: 133 },
        { key: 'npc_alckmin_attack', frame: 1, duration: 83 },
        { key: 'npc_alckmin_attack', frame: 2, duration: 166 }
    ],
    repeat: 0
});
```

**Attack Projectile Spawn:**
```javascript
// Spawn do projetil de cafe no frame 1 (arremesso)
this.anims.get('alckmin_attack').frames[1].onUpdate = () => {
    spawnCoffeeProjectile(alckmin.x, alckmin.y, targetDirection);
};
```

**Attack Cooldown:** 800ms (precisa preparar outro cafe)

---

### Animation: `alckmin_death`
- **Type:** Play once
- **Frames:** [0, 1, 2, 3]
- **Frame Rate:** 6 fps (LENTO, dramatico, ironico)
- **Frame Durations (individuais):**
  - Frame 0 (hit fatal): 200ms -- PAUSA no sorriso quebrando (momento chave!)
  - Frame 1 (joelhos): 200ms -- queda gradual
  - Frame 2 (chao): 300ms -- held longo, ninguem percebe
  - Frame 3 (fade): 400ms -- desaparecimento lento
- **Total Duration:** ~1100ms
- **Repeat:** 0
- **On Complete:** Fade out sprite + spawn bandeja como drop item
- **Descricao:** A morte mais TRISTE e COMICA do jogo. O sorriso quebra pela primeira vez (Frame 0), volta vazio (Frame 1), permanece no cadaver (Frame 2), e o corpo some mas a bandeja fica (Frame 3). Nenhum outro NPC reage.

```javascript
this.anims.create({
    key: 'alckmin_death',
    frames: [
        { key: 'npc_alckmin_death', frame: 0, duration: 200 },
        { key: 'npc_alckmin_death', frame: 1, duration: 200 },
        { key: 'npc_alckmin_death', frame: 2, duration: 300 },
        { key: 'npc_alckmin_death', frame: 3, duration: 400 }
    ],
    repeat: 0
});

// Apos death animation
alckmin.on('animationcomplete-alckmin_death', () => {
    // Fade out do corpo
    this.tweens.add({
        targets: alckmin,
        alpha: 0,
        duration: 500,
        onComplete: () => {
            // Spawn bandeja como drop item (ela e mais importante que ele)
            const bandeja = this.add.sprite(alckmin.x + 8, alckmin.y, 'item_bandeja_cafe');
            bandeja.setDepth(alckmin.y);
            // A bandeja fica no chao por 10 segundos
            this.time.delayedCall(10000, () => {
                this.tweens.add({
                    targets: bandeja,
                    alpha: 0,
                    duration: 1000,
                    onComplete: () => bandeja.destroy()
                });
            });
            alckmin.destroy();
        }
    });
});
```

---

### Animation: `alckmin_hit`
- **Type:** Play once
- **Frames:** [0, 1]
- **Frame Rate:** 10 fps
- **Frame Durations (individuais):**
  - Frame 0 (panico pelo cafe): 150ms -- expressao de horror
  - Frame 1 (cafe salvo): 100ms -- alivio instantaneo
- **Total Duration:** ~250ms
- **Repeat:** 0
- **On Complete:** Return to `alckmin_idle`
- **Descricao:** Leva dano mas o PANICO e pelo cafe derramado, nao pela dor. Transicao de horror para sorriso em 1 frame -- perturbador.

```javascript
this.anims.create({
    key: 'alckmin_hit',
    frames: [
        { key: 'npc_alckmin_hit', frame: 0, duration: 150 },
        { key: 'npc_alckmin_hit', frame: 1, duration: 100 }
    ],
    repeat: 0
});
```

---

### Animation: `alckmin_special` (Mordomo Supremo)
- **Type:** Play once
- **Frames:** [0, 1, 2, 3, 4, 5]
- **Frame Rate:** 10 fps
- **Frame Durations (individuais):**
  - Frame 0 (ativacao): 200ms -- momento de transformacao
  - Frame 1 (multitask cafe): 150ms -- serve cafe
  - Frame 2 (multitask limpa): 150ms -- limpa e carrega
  - Frame 3 (multitask PEAK): 200ms -- held mais tempo, maximo caos
  - Frame 4 (desaceleracao): 150ms -- voltando ao normal
  - Frame 5 (retorno): 200ms -- subserviencia restaurada
- **Total Duration:** ~1050ms
- **Repeat:** 0
- **On Complete:** Return to `alckmin_idle` + aplicar efeitos de cura/buff
- **Descricao:** O momento SUPREMO do Alckmin. As costas se endireitam (unica vez), bracos viram blur de multitask. Cura HP, limpa debuffs, serve, carrega, limpa -- TUDO ao mesmo tempo. E MAGNIFICO. E ninguem agradece.

```javascript
this.anims.create({
    key: 'alckmin_special',
    frames: [
        { key: 'npc_alckmin_special', frame: 0, duration: 200 },
        { key: 'npc_alckmin_special', frame: 1, duration: 150 },
        { key: 'npc_alckmin_special', frame: 2, duration: 150 },
        { key: 'npc_alckmin_special', frame: 3, duration: 200 },
        { key: 'npc_alckmin_special', frame: 4, duration: 150 },
        { key: 'npc_alckmin_special', frame: 5, duration: 200 }
    ],
    repeat: 0
});
```

---

### Animation: `alckmin_projetil` (Cafe Voando)
- **Type:** Play once
- **Frames:** [0, 1, 2]
- **Frame Rate:** 12 fps
- **Frame Durations:**
  - Frame 0 (xicara voando): 83ms
  - Frame 1 (mid-flight com splash): 83ms
  - Frame 2 (impacto/quebra): 100ms
- **Total Duration:** ~266ms
- **Repeat:** 0
- **On Complete:** Destroy projetil + spawn particulas de cafe
- **Velocidade do projetil:** 200 px/s
- **Dano:** 15 HP (queimadura de cafe) + slow 20% por 2s

```javascript
this.anims.create({
    key: 'alckmin_projetil',
    frames: this.anims.generateFrameNumbers('npc_alckmin_projetil', { start: 0, end: 2 }),
    frameRate: 12,
    repeat: 0
});
```

---

## Particle Effects

### Vapor do Cafe (idle, walk, attack)
- **Emitter:** Contínuo durante idle e walk
- **Particle Count:** 1-2 por frame
- **Particle Size:** 2x2px
- **Particle Color:** `#D4C5A9` (vapor bege)
- **Particle Speed:** 10-20 px/s (sobe lentamente)
- **Particle Direction:** Para cima (270 graus +/- 15)
- **Particle Lifespan:** 400-800ms
- **Particle Alpha:** 0.5 -> 0.0 (fade out suave)
- **Gravity:** -10 px/s^2 (sobe)
- **Spawn Position:** Acima da xicara (alckmin.x + 16, alckmin.y - 24)

```javascript
const cafeVapor = this.add.particles(0, 0, 'particle_vapor', {
    speed: { min: 10, max: 20 },
    angle: { min: 255, max: 285 },
    scale: { start: 0.8, end: 0 },
    alpha: { start: 0.5, end: 0 },
    lifespan: { min: 400, max: 800 },
    quantity: 1,
    frequency: 200,
    gravityY: -10,
    tint: 0xD4C5A9,
    follow: alckmin,
    followOffset: { x: 16, y: -24 }
});
```

### Gotas de Cafe (idle tremor, hit)
- **Trigger:** Frames 1 e 3 do idle, Frame 0 do hit
- **Particle Count:** 1 (idle), 6-8 (hit)
- **Particle Size:** 2x2px
- **Particle Color:** `#3E1F0D` (cafe marrom escuro)
- **Particle Speed:** 20-40 px/s (idle), 60-100 px/s (hit)
- **Particle Direction:** Radial para baixo (45-135 graus)
- **Particle Lifespan:** 200-400ms
- **Particle Alpha:** 1.0 -> 0.0
- **Gravity:** 80 px/s^2 (cai rapido)

```javascript
const cafeDrip = this.add.particles(0, 0, 'particle_cafe_drop', {
    speed: { min: 20, max: 40 },
    angle: { min: 45, max: 135 },
    scale: { start: 1, end: 0.5 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 200, max: 400 },
    quantity: 1,
    gravityY: 80,
    tint: 0x3E1F0D,
    emitting: false
});
```

### Bolhas de Sabao (special, frames 2-3)
- **Trigger:** Frames 2-3 do special (Mordomo Supremo)
- **Particle Count:** 3-5 por frame
- **Particle Size:** 2x2px a 4x4px
- **Particle Color:** `#87CEEB` (azul sabao) com `#FFFFFF` highlight
- **Particle Speed:** 30-60 px/s
- **Particle Direction:** Radial (0-360 graus)
- **Particle Lifespan:** 600-1000ms
- **Particle Alpha:** 0.7 -> 0.0
- **Scale:** Start 0.5, mid 1.2, end 0 (expande e estoura)
- **Gravity:** -5 px/s^2 (flutua para cima levemente)

```javascript
const soapBubbles = this.add.particles(0, 0, 'particle_bubble', {
    speed: { min: 30, max: 60 },
    angle: { min: 0, max: 360 },
    scale: { start: 0.5, end: 0, ease: 'Sine.easeInOut' },
    alpha: { start: 0.7, end: 0 },
    lifespan: { min: 600, max: 1000 },
    quantity: 4,
    gravityY: -5,
    tint: [0x87CEEB, 0xADD8E6, 0xFFFFFF],
    emitting: false
});
```

### Estrelas de Esforco (special, frames 1-4)
- **Trigger:** Frames 1-4 do special
- **Particle Count:** 2-3 por frame
- **Particle Size:** 3x3px (forma de estrela/cruz)
- **Particle Color:** `#FFD700` (amarelo dourado)
- **Particle Speed:** 40-80 px/s
- **Particle Direction:** Radial para cima (225-315 graus)
- **Particle Lifespan:** 300-500ms
- **Particle Alpha:** 1.0 -> 0.0
- **Rotation:** Gira 360 graus durante lifespan

```javascript
const effortStars = this.add.particles(0, 0, 'particle_star', {
    speed: { min: 40, max: 80 },
    angle: { min: 225, max: 315 },
    scale: { start: 1, end: 0 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 300, max: 500 },
    quantity: 2,
    rotate: { start: 0, end: 360 },
    tint: 0xFFD700,
    emitting: false
});
```

### Splash de Cafe no Impacto (projetil frame 2)
- **Trigger:** Projetil atinge alvo
- **Particle Count:** 8-12
- **Particle Size:** 2x2px a 3x3px
- **Particle Color:** `#3E1F0D` (cafe) + `#D4C5A9` (vapor)
- **Particle Speed:** 80-150 px/s
- **Particle Direction:** Radial (0-360 graus)
- **Particle Lifespan:** 300-600ms
- **Particle Alpha:** 1.0 -> 0.0
- **Gravity:** 60 px/s^2

```javascript
const coffeeSplash = this.add.particles(target.x, target.y, 'particle_cafe_splash', {
    speed: { min: 80, max: 150 },
    angle: { min: 0, max: 360 },
    scale: { start: 1, end: 0 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 300, max: 600 },
    quantity: 10,
    gravityY: 60,
    tint: [0x3E1F0D, 0x3E1F0D, 0x3E1F0D, 0xD4C5A9],
    emitting: false
});
```

---

## Visual Effects (Tweens)

### Sorriso Flash (quando serve cafe com sucesso)
- **Trigger:** Cafe atinge inimigo com sucesso
- **Efeito:** Dentes do Alckmin brilham branco por 1 frame
- **Duracao:** 80ms
- **Metodo:** Flash branco na regiao da boca

```javascript
// Flash nos dentes ao servir cafe com sucesso
alckmin.setTint(0xFFFFFF);
this.time.delayedCall(80, () => alckmin.clearTint());
```

### Aura de Mordomo Supremo (special)
- **Trigger:** Frame 0 do special
- **Efeito:** Glow amarelo pulsante ao redor do Alckmin
- **Duracao:** Toda a animacao special (~1050ms)
- **Cor:** `#FFD700` a 30% opacity
- **Raio:** 6px do sprite, pulsando 6px -> 8px -> 6px

```javascript
const aura = this.add.circle(alckmin.x, alckmin.y, 40, 0xFFD700, 0.3);
aura.setDepth(alckmin.depth - 1);

this.tweens.add({
    targets: aura,
    scaleX: { from: 1, to: 1.3, ease: 'Sine.easeInOut' },
    scaleY: { from: 1, to: 1.3, ease: 'Sine.easeInOut' },
    alpha: { from: 0.3, to: 0.15, ease: 'Sine.easeInOut' },
    duration: 300,
    yoyo: true,
    repeat: 3,
    onComplete: () => aura.destroy()
});
```

### Invisibilidade Politica (skill 2)
- **Trigger:** Ativacao da skill "Invisibilidade Politica"
- **Efeito:** Alckmin fica gradualmente transparente ate alpha 0.1
- **Duracao da transicao:** 500ms (fade out)
- **Duracao do efeito:** 5000ms (invisivel)
- **Retorno:** 500ms (fade in)
- **Nota:** NAO e um poder. E que ninguem se importa.

```javascript
// Invisibilidade Politica -- ninguem nota o vice
this.tweens.add({
    targets: alckmin,
    alpha: 0.1,
    duration: 500,
    ease: 'Power2',
    onComplete: () => {
        // Alckmin fica "invisivel" por 5 segundos
        // Inimigos ignoram completamente
        alckmin.setData('invisible', true);

        this.time.delayedCall(5000, () => {
            this.tweens.add({
                targets: alckmin,
                alpha: 1,
                duration: 500,
                ease: 'Power2',
                onComplete: () => alckmin.setData('invisible', false)
            });
        });
    }
});

// Texto flutuante comico
const txt = this.add.text(alckmin.x, alckmin.y - 32,
    'Alguem viu o vice?', { fontSize: '8px', color: '#888888' });
this.tweens.add({
    targets: txt,
    y: txt.y - 16,
    alpha: 0,
    duration: 2000,
    onComplete: () => txt.destroy()
});
```

### Interinidade Fantasma (skill 3)
- **Trigger:** Lula com HP < 20% ou Lula desativado
- **Efeito:** Flash MUITO sutil na UI indicando troca (mas nada muda visivelmente)
- **Duracao:** 3000ms
- **Visual:** Micro-borda dourada no HUD por 1 frame (100ms), depois some

```javascript
// Interinidade Fantasma -- ninguem percebe
// Flash tao sutil que o jogador provavelmente nao nota
const interimFlash = this.add.rectangle(
    this.cameras.main.centerX, this.cameras.main.centerY,
    this.cameras.main.width, this.cameras.main.height,
    0xFFD700, 0.02 // 2% opacity -- quase invisivel
);
interimFlash.setScrollFactor(0);
interimFlash.setDepth(10000);

this.tweens.add({
    targets: interimFlash,
    alpha: 0,
    duration: 100,
    onComplete: () => interimFlash.destroy()
});

// Texto que NINGUEM le
const interimText = this.add.text(
    this.cameras.main.centerX, 10,
    'Alckmin assumiu interinamente',
    { fontSize: '6px', color: '#666666', alpha: 0.3 }
);
interimText.setScrollFactor(0).setOrigin(0.5, 0);
this.time.delayedCall(3000, () => interimText.destroy());
```

### Cafe Revigorante (skill 1)
- **Trigger:** Alckmin serve cafe para aliados
- **Efeito:** Area de cura ao redor do Alckmin
- **Raio:** 80px
- **Cura:** +15 HP por servida
- **Visual:** Particulas de vapor dourado subindo + icone de xicara acima dos aliados curados
- **Cooldown:** 5000ms

```javascript
// Cafe Revigorante -- cura aliados
const healZone = this.add.circle(alckmin.x, alckmin.y, 80, 0xC8A96E, 0.1);
healZone.setDepth(alckmin.depth - 1);

// Particulas de vapor dourado
const healVapor = this.add.particles(alckmin.x, alckmin.y, 'particle_vapor', {
    speed: { min: 15, max: 30 },
    angle: { min: 250, max: 290 },
    scale: { start: 0.6, end: 0 },
    alpha: { start: 0.6, end: 0 },
    lifespan: { min: 500, max: 1000 },
    quantity: 3,
    frequency: 100,
    gravityY: -15,
    tint: 0xFFD700
});

// Curar aliados na area
allies.forEach(ally => {
    if (Phaser.Math.Distance.Between(alckmin.x, alckmin.y, ally.x, ally.y) <= 80) {
        ally.heal(15);
        // Icone de xicara acima do aliado
        const cupIcon = this.add.sprite(ally.x, ally.y - 20, 'icon_coffee_cup');
        this.tweens.add({
            targets: cupIcon,
            y: cupIcon.y - 12,
            alpha: 0,
            duration: 800,
            onComplete: () => cupIcon.destroy()
        });
    }
});

// Cleanup
this.time.delayedCall(1000, () => {
    healVapor.destroy();
    this.tweens.add({
        targets: healZone,
        alpha: 0,
        duration: 300,
        onComplete: () => healZone.destroy()
    });
});
```

---

## Screen Effects

### Screen Shake (projetil de cafe impacta)
- **Intensidade:** 1.5px (sutil -- e cafe, nao bomba)
- **Duracao:** 80ms
- **Decay:** Linear

```javascript
this.cameras.main.shake(80, 0.003);
```

### Coffee Stain Overlay (hit no jogador com cafe)
- **Trigger:** Se o projetil de cafe atingir algo
- **Efeito:** Mancha marrom semitransparente na tela por 200ms
- **Opacity:** 15%
- **Cor:** `#3E1F0D`

```javascript
const stain = this.add.rectangle(
    target.x, target.y, 16, 16, 0x3E1F0D, 0.15
);
stain.setDepth(target.depth + 1);
this.tweens.add({
    targets: stain,
    alpha: 0,
    scale: 1.5,
    duration: 200,
    onComplete: () => stain.destroy()
});
```

---

## Sound Cue Timing

| Tempo (ms) | Evento                    | Sound Key                | Notas                                    |
|------------|---------------------------|--------------------------|------------------------------------------|
| 0          | Idle start                | `sfx_alckmin_hum`       | Humming suave de mordomo (loop)          |
| idle:100ms | Cafe pinga (idle)         | `sfx_cafe_drip`         | Gota caindo, sutil                       |
| 0          | Walk start                | `sfx_alckmin_steps`     | Passos rapidos e rasteiros (loop)        |
| walk:500ms | Bandeja tilts             | `sfx_tray_clink`        | Tilinteiro metalico sutil                |
| 0          | Attack wind-up            | `sfx_cafe_whoosh`       | Bandeja puxada para tras                 |
| atk:133ms  | Cafe lancado              | `sfx_cafe_throw`        | Splash liquido + whoosh                  |
| atk:133ms  | Bordao ataque             | `sfx_alckmin_serve`     | "Cafe quentinho pra voce!"              |
| atk:216ms  | Nova bandeja              | `sfx_tray_materialize`  | Pop magico sutil                         |
| 0          | Hit recebido              | `sfx_cafe_spill`        | Cafe derramando URGENTE                  |
| hit:0ms    | Panico                    | `sfx_alckmin_gasp`      | Gasp de horror (pelo cafe)               |
| 0          | Death frame 0             | `sfx_tray_clatter`      | Bandeja caindo metalico                  |
| death:200  | Death frame 1             | `sfx_cafe_splash_big`   | Cafe espirra no chao                     |
| death:400  | Death frame 2             | (silencio)              | Ninguem percebeu                         |
| death:700  | Death frame 3             | `sfx_alckmin_whisper`   | "Alguem notou...?" (sussurro)            |
| 0          | Special start             | `sfx_mordomo_transform` | Power-up sound, servil                   |
| spec:200ms | Multitask peak            | `sfx_multitask_chaos`   | Coisas batendo, cafe passando, varrendo  |
| spec:800ms | Cooldown                  | `sfx_alckmin_sigh`      | Suspiro de mordomo cansado               |
| spec:1050  | "Mais alguma coisa?"      | `sfx_alckmin_mais`      | Bordao final                             |

### Bordoes (Voice Lines)

| Key                        | Texto                                              | Trigger                          |
|----------------------------|----------------------------------------------------|---------------------------------|
| `vo_alckmin_alcool`        | "Eu adoro esse nome, alcool em mim!"               | Spawn / a cada 60s              |
| `vo_alckmin_resolve`       | "Companheiro Lula, eu resolvo!"                    | Ao usar attack                  |
| `vo_alckmin_cafe`          | "Quer que eu passe o cafe?"                        | Ao usar Cafe Revigorante        |
| `vo_alckmin_governando`    | "Eu estava governando esse tempo todo... alguem notou?" | Interinidade Fantasma       |
| `vo_alckmin_mais`          | "Mais alguma coisa, presidente? Cafe? Pastel? Minha dignidade?" | Apos Mordomo Supremo  |

---

## State Machine

```
                    ┌──────────┐
                    │  SPAWN   │
                    └────┬─────┘
                         │
                         v
                 ┌───────────────┐
          ┌──────│     IDLE      │◄─────────────────────┐
          │      └───┬───┬───┬───┘                      │
          │          │   │   │                           │
     move │   attack │   │   │ hit                      │
     input│   input  │   │   │ received                 │
          │          │   │   │                           │
          v          v   │   v                           │
    ┌──────────┐ ┌──────┐│ ┌──────┐                     │
    │  WALK    │ │ATTACK││ │  HIT │──── on complete ────┘
    └────┬─────┘ └──┬───┘│ └──┬───┘
         │          │    │    │
    stop │  on      │    │    │ HP <= 0
    input│  complete│    │    │
         │          │    │    v
         └──────────┘    │ ┌──────┐
                         │ │DEATH │──── on complete ──> DESTROY
                         │ └──────┘
                         │
                    special input
                         │
                         v
                    ┌─────────┐
                    │ SPECIAL │──── on complete ────> IDLE
                    └─────────┘
```

---

## Y-Sort Depth

```javascript
// NPC Alckmin sempre renderiza baseado na posicao Y (perspectiva isometrica)
alckmin.setDepth(alckmin.y);

// A bandeja renderiza 1 acima do Alckmin
bandeja.setDepth(alckmin.y + 1);

// Vapor renderiza 2 acima
vapor.setDepth(alckmin.y + 2);
```

---

## AI Behavior (NPC)

### Follow Pattern
- Segue o jogador (ou Lula se presente) a 48px de distancia
- Se o jogador para, Alckmin para e entra em idle
- Se inimigos estao a 120px, Alckmin ataca automaticamente com cafe
- A cada 15 segundos, usa Cafe Revigorante (cura) se aliados estiverem com HP < 70%
- Se HP do Alckmin < 30%, usa Invisibilidade Politica (ninguem nota mesmo)

### Interaction
- Se o jogador interage com Alckmin, ele oferece cafe (+10 HP)
- Cooldown de interacao: 10 segundos
- Bordao aleatorio a cada interacao
