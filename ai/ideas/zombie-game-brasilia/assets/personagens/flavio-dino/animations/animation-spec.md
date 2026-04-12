# FLAVIO DINO (A Muralha Burocratica) - Animation Specification

## Phaser 3 Animation Definitions

---

### Animation: `dino_idle`
- **Tipo**: Loop infinito
- **Frames**: [0, 1, 2, 3]
- **Frame Rate**: 4 fps (lento — muralha nao tem pressa)
- **Duracao por frame**: 250ms cada
- **Repeat**: -1 (loop infinito)
- **Yoyo**: true (0 -> 1 -> 2 -> 3 -> 2 -> 1 -> 0...)
- **Descricao**: Micro-ciclo de negacao. Bigode treme esquerda-centro-direita-centro. Papeis de emenda caem e sao carimbados microscopicamente. A muralha RESPIRA negacao. Movimento quase imperceptivel — e o MINIMO para mostrar que esta vivo.

```javascript
this.anims.create({
    key: 'dino_idle',
    frames: this.anims.generateFrameNumbers('boss_dino_idle', { start: 0, end: 3 }),
    frameRate: 4,
    repeat: -1,
    yoyo: true
});
```

**Efeitos Visuais do Idle:**
- **Brilho da careca**: Tween sutil de alpha no highlight (0.6 -> 1.0 -> 0.6, 2s ciclo)
- **Sombra no chao**: Pulsa levemente (scale 1.0 -> 1.02 -> 1.0, 3s ciclo) — o peso muda
- **Particula de papel**: A cada 4s, spawn 1 particula de papel (3x3px, #F5F0DC) que cai do topo e recebe uma marca vermelha ao tocar o chao

```javascript
// Brilho da careca (tween sutil)
this.tweens.add({
    targets: carecaHighlight,
    alpha: { from: 0.6, to: 1.0 },
    duration: 2000,
    repeat: -1,
    yoyo: true,
    ease: 'Sine.easeInOut'
});

// Particula de emenda caindo (a cada 4s)
this.time.addEvent({
    delay: 4000,
    callback: () => {
        const paper = this.add.sprite(dino.x + Phaser.Math.Between(-8, 8), dino.y - 32, 'particle_paper');
        this.tweens.add({
            targets: paper,
            y: dino.y + 20,
            rotation: Phaser.Math.FloatBetween(-0.5, 0.5),
            duration: 1500,
            ease: 'Bounce.easeOut',
            onComplete: () => {
                // Flash vermelho (carimbado)
                paper.setTint(0xCC0000);
                this.time.delayedCall(200, () => paper.destroy());
            }
        });
    },
    loop: true
});
```

---

### Animation: `dino_walk`
- **Tipo**: Loop
- **Frames**: [0, 1, 2, 3, 4, 5]
- **Frame Rate**: 8 fps (marcha pesada, nao rapida)
- **Duracoes individuais**:
  - Frame 0 (levanta esq): 125ms — levanta leve
  - Frame 1 (avanca esq): 100ms — avanco
  - Frame 2 (planta esq): 150ms — IMPACTO (segurado pra sentir o peso)
  - Frame 3 (levanta dir): 125ms — levanta
  - Frame 4 (avanca dir): 100ms — avanco, botao voa
  - Frame 5 (planta dir): 175ms — IMPACTO MAXIMO (mais segurado)
- **Duracao total**: ~775ms por ciclo de caminhada
- **Repeat**: -1 (loop enquanto caminha)

```javascript
this.anims.create({
    key: 'dino_walk',
    frames: [
        { key: 'boss_dino_walk', frame: 0, duration: 125 },
        { key: 'boss_dino_walk', frame: 1, duration: 100 },
        { key: 'boss_dino_walk', frame: 2, duration: 150 },
        { key: 'boss_dino_walk', frame: 3, duration: 125 },
        { key: 'boss_dino_walk', frame: 4, duration: 100 },
        { key: 'boss_dino_walk', frame: 5, duration: 175 }
    ],
    frameRate: 8,
    repeat: -1
});
```

**Efeitos Visuais do Walk:**

#### Screen Shake por Passo (Frames 2 e 5)
```javascript
// No callback de frame da animacao:
dino.on('animationupdate', (anim, frame) => {
    if (anim.key === 'dino_walk') {
        if (frame.index === 2) {
            this.cameras.main.shake(80, 0.003); // shake leve
        }
        if (frame.index === 5) {
            this.cameras.main.shake(120, 0.005); // shake FORTE
        }
    }
});
```

#### Particulas de Poeira nos Impactos (Frames 2 e 5)
```javascript
const dustConfig = {
    speed: { min: 20, max: 60 },
    angle: { min: 200, max: 340 },
    scale: { start: 1, end: 0 },
    alpha: { start: 0.8, end: 0 },
    lifespan: { min: 300, max: 600 },
    quantity: 4,
    gravityY: 10,
    tint: 0x8B8B8B
};
// Emitir nos frames 2 e 5 na posicao do pe
```

#### Rastro de Carimbo no Chao (Frames 1 e 4)
```javascript
// Quando carimbo arrasta no chao, deixar marca vermelha
const trailMark = this.add.rectangle(dino.x - 8, dino.y + 24, 3, 1, 0xCC0000, 0.6);
this.tweens.add({
    targets: trailMark,
    alpha: 0,
    duration: 3000,
    onComplete: () => trailMark.destroy()
});
```

#### Botao Voando (Frame 4)
```javascript
// Botao da toga voa como projetil comico
const button = this.add.circle(dino.x + 8, dino.y - 10, 2, 0xC0C0C0);
this.tweens.add({
    targets: button,
    x: dino.x + 40,
    y: dino.y - 30,
    rotation: Math.PI * 4,
    alpha: 0,
    duration: 800,
    ease: 'Quad.easeOut',
    onComplete: () => button.destroy()
});
```

#### Rachadura no Chao (Frame 5)
```javascript
// Micro-rachadura no chao do impacto pesado
const crack = this.add.line(0, 0, dino.x - 4, dino.y + 28, dino.x + 4, dino.y + 28, 0x666666);
crack.setAlpha(0.5);
this.tweens.add({
    targets: crack,
    alpha: 0,
    duration: 5000,
    onComplete: () => crack.destroy()
});
```

---

### Animation: `dino_attack`
- **Tipo**: Play once
- **Frames**: [0, 1, 2]
- **Frame Rate**: 10 fps
- **Duracoes individuais**:
  - Frame 0 (ergue carimbo): 200ms — buildup dramatico, tensao
  - Frame 1 (CARIMBA!): 166ms — impacto segurado pra leitura visual
  - Frame 2 (pos-carimbada): 133ms — recuperacao rapida
- **Duracao total**: ~500ms
- **Repeat**: 0 (play once)
- **On Complete**: Retorna para `dino_idle`

```javascript
this.anims.create({
    key: 'dino_attack',
    frames: [
        { key: 'boss_dino_attack', frame: 0, duration: 200 },
        { key: 'boss_dino_attack', frame: 1, duration: 166 },
        { key: 'boss_dino_attack', frame: 2, duration: 133 }
    ],
    frameRate: 10,
    repeat: 0
});
```

**Efeitos Visuais do Attack:**

#### Screen Shake no Impacto (Frame 1)
```javascript
this.cameras.main.shake(200, 0.01); // shake FORTE — impacto de carimbo
```

#### Particulas de Papel Voando (Frame 1)
```javascript
const paperBurst = this.add.particles(dino.x, dino.y, 'particle_paper', {
    speed: { min: 60, max: 140 },
    angle: { min: 0, max: 360 },
    scale: { start: 1, end: 0.3 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 500, max: 1000 },
    quantity: 8,
    gravityY: 30,
    rotate: { min: -180, max: 180 },
    tint: 0xF5F0DC,
    emitting: false
});
paperBurst.explode(8); // burst de 8 papeis
```

#### Marca "NEGADO" no Chao (Frame 1)
```javascript
// Spawn projetil/efeito "NEGADO" na posicao do ataque
const negado = this.add.sprite(target.x, target.y, 'projectile_negado');
negado.setDepth(target.y - 1);
negado.setScale(0);

this.tweens.add({
    targets: negado,
    scaleX: { from: 0, to: 1.5, duration: 100, ease: 'Back.easeOut' },
    scaleY: { from: 0, to: 1.5, duration: 100, ease: 'Back.easeOut' },
    onComplete: () => {
        this.tweens.add({
            targets: negado,
            scale: 1.0,
            alpha: 0,
            duration: 2000,
            ease: 'Linear',
            onComplete: () => negado.destroy()
        });
    }
});
```

#### Particulas de Poeira/Fragmentos (Frame 1)
```javascript
const debrisBurst = this.add.particles(dino.x, dino.y + 20, 'particle_debris', {
    speed: { min: 30, max: 80 },
    angle: { min: 220, max: 320 },
    scale: { start: 0.8, end: 0 },
    alpha: { start: 0.9, end: 0 },
    lifespan: { min: 300, max: 600 },
    quantity: 5,
    gravityY: 40,
    tint: [0x8B8B8B, 0x666666, 0xA09070],
    emitting: false
});
debrisBurst.explode(5);
```

#### Flash no Inimigo (Frame 1)
```javascript
target.setTint(0xCC0000); // Flash VERMELHO (nao branco — e carimbo!)
this.time.delayedCall(100, () => {
    target.setTint(0xFFFFFF); // Depois branco
    this.time.delayedCall(66, () => target.clearTint());
});
```

#### Texto "NEGADO!" Comico (Frame 1)
```javascript
const text = this.add.text(target.x, target.y - 16, 'NEGADO!', {
    fontFamily: 'Impact, sans-serif',
    fontSize: '12px',
    color: '#CC0000',
    stroke: '#000000',
    strokeThickness: 2
});
text.setOrigin(0.5);
text.setDepth(9999);
text.setRotation(Phaser.Math.FloatBetween(-0.15, 0.15));

this.tweens.add({
    targets: text,
    y: target.y - 32,
    scaleX: { from: 0.5, to: 1.3 },
    scaleY: { from: 0.5, to: 1.3 },
    duration: 150,
    ease: 'Back.easeOut',
    onComplete: () => {
        this.tweens.add({
            targets: text,
            y: target.y - 40,
            alpha: 0,
            scale: 0.8,
            duration: 400,
            onComplete: () => text.destroy()
        });
    }
});
```

---

### Animation: `dino_death`
- **Tipo**: Play once
- **Frames**: [0, 1, 2, 3]
- **Frame Rate**: 6 fps (LENTO — morte epica de muralha desmoronando)
- **Duracoes individuais**:
  - Frame 0 (rachadura): 250ms — choque inicial
  - Frame 1 (bracos murcham): 333ms — LONGO, pra sentir a perda
  - Frame 2 (carimbo quebra): 250ms — climax da destruicao
  - Frame 3 (escombros): 400ms — frame final, segurado pra contemplacao
- **Duracao total**: ~1233ms
- **Repeat**: 0
- **On Complete**: Manter frame 3 (escombros) visivel por 2s, depois fade out

```javascript
this.anims.create({
    key: 'dino_death',
    frames: [
        { key: 'boss_dino_death', frame: 0, duration: 250 },
        { key: 'boss_dino_death', frame: 1, duration: 333 },
        { key: 'boss_dino_death', frame: 2, duration: 250 },
        { key: 'boss_dino_death', frame: 3, duration: 400 }
    ],
    frameRate: 6,
    repeat: 0
});
```

**Efeitos Visuais da Death:**

#### Frame 0 — Som de Rachadura
```javascript
dino.on('animationupdate', (anim, frame) => {
    if (anim.key === 'dino_death' && frame.index === 0) {
        this.sound.play('sfx_concrete_crack');
        // Tela treme levemente (a muralha esta cedendo)
        this.cameras.main.shake(150, 0.003);
    }
});
```

#### Frame 1 — Bracos Murcham (Efeito de Deflacao)
```javascript
// Particulas de "musculo perdido" — esferas cor de pele que saem dos bracos
const muscleLoss = this.add.particles(dino.x, dino.y, 'particle_skin', {
    speed: { min: 15, max: 40 },
    angle: { min: 0, max: 360 },
    scale: { start: 0.6, end: 0 },
    alpha: { start: 0.7, end: 0 },
    lifespan: { min: 400, max: 800 },
    quantity: 6,
    tint: 0xD4956A,
    emitting: false
});
muscleLoss.explode(6);

// Papeis escapando pelas rachaduras
for (let i = 0; i < 5; i++) {
    const paper = this.add.sprite(
        dino.x + Phaser.Math.Between(-12, 12),
        dino.y + Phaser.Math.Between(-8, 8),
        'particle_paper'
    );
    this.tweens.add({
        targets: paper,
        x: paper.x + Phaser.Math.Between(-30, 30),
        y: paper.y + Phaser.Math.Between(-40, -10),
        rotation: Phaser.Math.FloatBetween(-2, 2),
        alpha: 0,
        duration: 1200,
        ease: 'Quad.easeOut',
        onComplete: () => paper.destroy()
    });
}
```

#### Frame 2 — Carimbo Quebra (Explosao de Fragmentos + Confete de Emendas)
```javascript
// Fragmentos do carimbo (vermelhos)
const stampFragments = this.add.particles(dino.x, dino.y + 10, 'particle_debris', {
    speed: { min: 40, max: 100 },
    angle: { min: 200, max: 340 },
    scale: { start: 1, end: 0.2 },
    alpha: { start: 1, end: 0 },
    lifespan: { min: 600, max: 1200 },
    quantity: 5,
    gravityY: 60,
    tint: [0xCC0000, 0xFF2020, 0x8B0000],
    emitting: false
});
stampFragments.explode(5);

// Botoes da toga voam
for (let i = 0; i < 4; i++) {
    const btn = this.add.circle(dino.x, dino.y, 2, 0xC0C0C0);
    this.tweens.add({
        targets: btn,
        x: dino.x + Phaser.Math.Between(-50, 50),
        y: dino.y + Phaser.Math.Between(-50, 10),
        rotation: Math.PI * Phaser.Math.Between(2, 6),
        alpha: 0,
        duration: 1000,
        ease: 'Quad.easeOut',
        onComplete: () => btn.destroy()
    });
}

// CONFETE DE EMENDAS LIBERADAS (voam pra CIMA!)
for (let i = 0; i < 20; i++) {
    const emenda = this.add.sprite(
        dino.x + Phaser.Math.Between(-16, 16),
        dino.y,
        'particle_paper'
    );
    this.tweens.add({
        targets: emenda,
        x: emenda.x + Phaser.Math.Between(-40, 40),
        y: emenda.y - Phaser.Math.Between(60, 120), // PARA CIMA — liberadas!
        rotation: Phaser.Math.FloatBetween(-3, 3),
        scale: { from: 1, to: 0.3 },
        alpha: { from: 1, to: 0 },
        duration: Phaser.Math.Between(1500, 2500),
        ease: 'Quad.easeOut',
        onComplete: () => emenda.destroy()
    });
}

// Screen shake forte
this.cameras.main.shake(300, 0.008);
this.sound.play('sfx_stamp_shatter');
```

#### Frame 3 — Escombros (Fade Final)
```javascript
// Manter escombros visiveis por 2s, depois fade out
this.time.delayedCall(2000, () => {
    this.tweens.add({
        targets: dino,
        alpha: 0,
        duration: 1000,
        ease: 'Linear',
        onComplete: () => dino.destroy()
    });
});

// Ultimos papeis subindo pro ceu (5-6 papeis em espiral)
for (let i = 0; i < 6; i++) {
    const finalPaper = this.add.sprite(dino.x, dino.y - 10, 'particle_paper');
    const delay = i * 300;
    this.time.delayedCall(delay, () => {
        this.tweens.add({
            targets: finalPaper,
            y: dino.y - 100,
            x: finalPaper.x + Math.sin(i) * 20,
            scale: { from: 0.8, to: 0.1 },
            alpha: { from: 0.8, to: 0 },
            rotation: i * 0.5,
            duration: 2000,
            ease: 'Sine.easeIn',
            onComplete: () => finalPaper.destroy()
        });
    });
}
```

---

### Animation: `dino_hit`
- **Tipo**: Play once
- **Frames**: [0, 1]
- **Frame Rate**: 12 fps (rapido — reacao instantanea)
- **Duracoes individuais**:
  - Frame 0 (impacto): 100ms — flash rapido
  - Frame 1 (recomposicao): 133ms — volta MAIS forte
- **Duracao total**: ~233ms
- **Repeat**: 0
- **On Complete**: Retorna para `dino_idle` (mas com buffs visuais de raiva)

```javascript
this.anims.create({
    key: 'dino_hit',
    frames: [
        { key: 'boss_dino_hit', frame: 0, duration: 100 },
        { key: 'boss_dino_hit', frame: 1, duration: 133 }
    ],
    frameRate: 12,
    repeat: 0
});
```

**Efeitos Visuais do Hit:**

#### Flash de Impacto (Frame 0)
```javascript
dino.setTint(0xFFFFFF);
this.time.delayedCall(50, () => dino.clearTint());

// Linhas de choque
for (let i = 0; i < 4; i++) {
    const angle = (Math.PI / 2) * i;
    const line = this.add.line(0, 0,
        dino.x, dino.y,
        dino.x + Math.cos(angle) * 12, dino.y + Math.sin(angle) * 12,
        0xFFFFFF
    );
    line.setAlpha(0.8);
    this.tweens.add({
        targets: line,
        alpha: 0,
        duration: 200,
        onComplete: () => line.destroy()
    });
}
```

#### Buff Visual de Raiva (Frame 1 — persistente)
```javascript
// Aura vermelha no carimbo (persiste por 3s apos hit)
const rageAura = this.add.circle(dino.x + 10, dino.y, 14, 0xCC0000, 0.2);
this.tweens.add({
    targets: rageAura,
    scale: { from: 1, to: 1.3 },
    alpha: { from: 0.2, to: 0 },
    duration: 3000,
    repeat: 0,
    onComplete: () => rageAura.destroy()
});

// Veia na testa (persiste por 5s)
const vein = this.add.line(0, 0,
    dino.x - 4, dino.y - 24,
    dino.x + 2, dino.y - 22,
    0x8B4726
);
vein.setLineWidth(1.5);
this.tweens.add({
    targets: vein,
    alpha: { from: 1, to: 0 },
    duration: 5000,
    onComplete: () => vein.destroy()
});
```

---

### Animation: `dino_bloqueio` (Special 1 — Bloqueio Orcamentario)
- **Tipo**: Play once
- **Frames**: [0, 1, 2, 3]
- **Frame Rate**: 6 fps (ritual burocratico — lento e cerimonioso)
- **Duracoes individuais**:
  - Frame 0 (preparacao): 300ms — buildup
  - Frame 1 (carimba o ar): 200ms — impacto no vazio
  - Frame 2 (propagacao): 250ms — onda de congelamento
  - Frame 3 (estabelecido): 350ms — estado final segurado
- **Duracao total**: ~1100ms
- **Repeat**: 0
- **On Complete**: Manter efeito de congelamento por 3s no gameplay

```javascript
this.anims.create({
    key: 'dino_bloqueio',
    frames: [
        { key: 'boss_dino_bloqueio', frame: 0, duration: 300 },
        { key: 'boss_dino_bloqueio', frame: 1, duration: 200 },
        { key: 'boss_dino_bloqueio', frame: 2, duration: 250 },
        { key: 'boss_dino_bloqueio', frame: 3, duration: 350 }
    ],
    frameRate: 6,
    repeat: 0
});
```

**Efeitos Visuais do Bloqueio:**

#### Aura Gelada (Frame 0-3)
```javascript
// Anel de aura azul expandindo
const aura = this.add.circle(dino.x, dino.y, 10, 0xA0D8EF, 0);
aura.setStrokeStyle(2, 0xA0D8EF, 0.6);

this.tweens.add({
    targets: aura,
    radius: { from: 10, to: 120 },
    alpha: { from: 0.6, to: 0 },
    duration: 1500,
    ease: 'Quad.easeOut'
});
```

#### Congelamento de Inimigos (Frame 2 — gameplay)
```javascript
// Todos inimigos no raio recebem tint azul e param
const freezeRadius = 120;
enemies.forEach(enemy => {
    const dist = Phaser.Math.Distance.Between(dino.x, dino.y, enemy.x, enemy.y);
    if (dist < freezeRadius) {
        enemy.setTint(0xA0D8EF);
        enemy.body.setVelocity(0, 0);
        enemy.frozen = true;
        // Cristais de gelo no inimigo
        const ice = this.add.sprite(enemy.x, enemy.y - 8, 'particle_ice');
        ice.setAlpha(0.7);
        // Descongelar apos 3s
        this.time.delayedCall(3000, () => {
            enemy.clearTint();
            enemy.frozen = false;
            ice.destroy();
        });
    }
});
```

#### Numeros Flutuantes Congelando (Frame 1)
```javascript
// Numeros de orcamento que congelam no ar
const symbols = ['R$', '0', '%', '§', 'Art.'];
symbols.forEach((sym, i) => {
    const num = this.add.text(
        dino.x + Phaser.Math.Between(-30, 30),
        dino.y + Phaser.Math.Between(-30, 30),
        sym,
        { fontSize: '8px', color: '#A0D8EF', stroke: '#000', strokeThickness: 1 }
    );
    num.setDepth(9999);
    // Congelam no lugar
    this.tweens.add({
        targets: num,
        alpha: { from: 0, to: 1 },
        duration: 300,
        delay: i * 100,
        onComplete: () => {
            // Ficam parados por 3s depois somem
            this.time.delayedCall(3000, () => {
                this.tweens.add({
                    targets: num,
                    alpha: 0,
                    y: num.y - 10,
                    duration: 500,
                    onComplete: () => num.destroy()
                });
            });
        }
    });
});
```

---

### Animation: `dino_liminar` (Special 2 — Liminar Divina)
- **Tipo**: Play once
- **Frames**: [0, 1, 2, 3, 4, 5]
- **Frame Rate**: 6 fps
- **Duracoes individuais**:
  - Frame 0 (invocacao): 300ms — buildup epico
  - Frame 1 (carimba chao): 200ms — impacto supremo
  - Frame 2 (muro comeca): 250ms — construcao
  - Frame 3 (muro metade): 200ms — crescendo
  - Frame 4 (muro completo): 300ms — revelacao
  - Frame 5 (muro ativo): 250ms — estado final (depois loopa sozinho)
- **Duracao total**: ~1500ms
- **Repeat**: 0
- **On Complete**: Frame 5 loopa enquanto barreira esta ativa (5s)

```javascript
this.anims.create({
    key: 'dino_liminar',
    frames: [
        { key: 'boss_dino_liminar', frame: 0, duration: 300 },
        { key: 'boss_dino_liminar', frame: 1, duration: 200 },
        { key: 'boss_dino_liminar', frame: 2, duration: 250 },
        { key: 'boss_dino_liminar', frame: 3, duration: 200 },
        { key: 'boss_dino_liminar', frame: 4, duration: 300 },
        { key: 'boss_dino_liminar', frame: 5, duration: 250 }
    ],
    frameRate: 6,
    repeat: 0
});

// Loop do frame 5 enquanto barreira ativa
this.anims.create({
    key: 'dino_liminar_active',
    frames: [{ key: 'boss_dino_liminar', frame: 4 }, { key: 'boss_dino_liminar', frame: 5 }],
    frameRate: 2,
    repeat: -1,
    yoyo: true
});
```

**Efeitos Visuais da Liminar:**

#### Olhos Vermelhos (Frame 0)
```javascript
// Brilho vermelho nos olhos — UNICO special com isso
const eyeGlow = this.add.pointlight(dino.x - 3, dino.y - 24, 0xCC0000, 8, 0.6);
const eyeGlow2 = this.add.pointlight(dino.x + 3, dino.y - 24, 0xCC0000, 8, 0.6);
this.tweens.add({
    targets: [eyeGlow, eyeGlow2],
    intensity: { from: 0.3, to: 0.8 },
    duration: 300,
    yoyo: true,
    repeat: 2
});
```

#### Impacto Supremo (Frame 1)
```javascript
this.cameras.main.shake(300, 0.015); // Shake MAXIMO
this.cameras.main.flash(100, 204, 0, 0, true); // Flash vermelho

// Rachadura vermelha no chao
const crack = this.add.line(0, 0,
    dino.x - 40, dino.y + 20,
    dino.x + 40, dino.y + 20,
    0xCC0000
);
crack.setLineWidth(2);
crack.setAlpha(0);
this.tweens.add({
    targets: crack,
    alpha: { from: 0, to: 1 },
    scaleX: { from: 0, to: 1 },
    duration: 200,
    ease: 'Expo.easeOut'
});
```

#### Muro Crescendo (Frames 2-4)
```javascript
// Barreira fisica — retangulo que cresce
const wall = this.add.rectangle(dino.x, dino.y, 80, 0, 0x8B0000, 0.8);
wall.setStrokeStyle(2, 0xCC0000);
wall.setDepth(dino.y);

this.tweens.add({
    targets: wall,
    height: { from: 0, to: 64 },
    duration: 750,
    ease: 'Bounce.easeOut',
    onComplete: () => {
        // Muro completo — ativa colisao
        this.physics.add.existing(wall, true); // static body
        wall.body.setSize(80, 64);

        // Pulsacao do muro enquanto ativo
        this.tweens.add({
            targets: wall,
            alpha: { from: 0.8, to: 1 },
            duration: 500,
            repeat: 9, // 5s de pulsacao (500ms * 10)
            yoyo: true,
            onComplete: () => {
                // Muro desmorona apos 5s
                this.tweens.add({
                    targets: wall,
                    height: 0,
                    alpha: 0,
                    duration: 500,
                    ease: 'Back.easeIn',
                    onComplete: () => wall.destroy()
                });
            }
        });
    }
});
```

#### Texto "NEGADO" Flutuante no Muro (Frame 4)
```javascript
const wallText = this.add.text(wall.x, wall.y, 'NEGADO', {
    fontFamily: 'Impact, sans-serif',
    fontSize: '10px',
    color: '#FFFFFF',
    stroke: '#8B0000',
    strokeThickness: 2
});
wallText.setOrigin(0.5);
wallText.setDepth(wall.depth + 1);
```

---

### Animation: `dino_muralha` (Special 3 — Muralha Burocratica / Passiva)
- **Tipo**: Play once (transformacao) + loop (estado ativo)
- **Frames**: [0, 1, 2, 3]
- **Frame Rate**: 4 fps (transformacao LENTA e pesada)
- **Duracoes individuais**:
  - Frame 0 (inspiracao): 350ms — inhala, expande
  - Frame 1 (expansao): 400ms — transformacao (segurado — horror)
  - Frame 2 (muralha formada): 300ms — revelacao
  - Frame 3 (muralha ativa): 250ms — estado final (loopa)
- **Duracao total**: ~1300ms (transformacao)
- **Repeat**: 0 (transformacao), depois frame 2-3 loopa

```javascript
// Transformacao
this.anims.create({
    key: 'dino_muralha_transform',
    frames: [
        { key: 'boss_dino_muralha', frame: 0, duration: 350 },
        { key: 'boss_dino_muralha', frame: 1, duration: 400 },
        { key: 'boss_dino_muralha', frame: 2, duration: 300 },
        { key: 'boss_dino_muralha', frame: 3, duration: 250 }
    ],
    frameRate: 4,
    repeat: 0
});

// Estado ativo (loop)
this.anims.create({
    key: 'dino_muralha_active',
    frames: [{ key: 'boss_dino_muralha', frame: 2 }, { key: 'boss_dino_muralha', frame: 3 }],
    frameRate: 2,
    repeat: -1,
    yoyo: true
});
```

**Efeitos Visuais da Muralha:**

#### Botoes Voando (Frame 0)
```javascript
for (let i = 0; i < 3; i++) {
    const btn = this.add.circle(dino.x, dino.y - 10, 2, 0xC0C0C0);
    this.tweens.add({
        targets: btn,
        x: dino.x + Phaser.Math.Between(-40, 40),
        y: dino.y + Phaser.Math.Between(-40, -20),
        alpha: 0,
        rotation: Math.PI * 4,
        duration: 600,
        delay: i * 100,
        onComplete: () => btn.destroy()
    });
}
```

#### Expansao do Corpo (Frame 1 — tween de escala)
```javascript
// O sprite se estica horizontalmente
this.tweens.add({
    targets: dino,
    scaleX: { from: 1, to: 1.3 },
    duration: 400,
    ease: 'Cubic.easeInOut'
});
```

#### Colisao de Muralha (Frame 2 — gameplay)
```javascript
// Ativa hitbox ENORME que bloqueia passagem
dino.body.setSize(56, 50); // Quase todo o frame
dino.isWall = true;

// Colisao com TUDO — aliados e inimigos
this.physics.add.collider(player, dino);
this.physics.add.collider(enemies, dino);
this.physics.add.collider(allies, dino);
```

#### Sapatos Batendo de Impaciencia (Frame 3 — loop)
```javascript
// Micro-tween de Y nos pes (impaciencia)
this.tweens.add({
    targets: dinoFeetIndicator,
    y: { from: dino.y + 28, to: dino.y + 30 },
    duration: 300,
    repeat: -1,
    yoyo: true
});
```

#### Placa "PASSAGEM BLOQUEADA" (Frame 3)
```javascript
const sign = this.add.text(dino.x, dino.y - 36, 'PASSAGEM\nBLOQUEADA', {
    fontFamily: 'Impact, sans-serif',
    fontSize: '6px',
    color: '#FFFFFF',
    backgroundColor: '#CC0000',
    padding: { x: 2, y: 1 },
    align: 'center'
});
sign.setOrigin(0.5);
sign.setDepth(9999);

// Balanca levemente
this.tweens.add({
    targets: sign,
    rotation: { from: -0.05, to: 0.05 },
    duration: 1000,
    repeat: -1,
    yoyo: true
});
```

---

## Sound Cue Timing

### Idle
| Tempo | Evento            | Sound Key              | Notas                               |
|-------|--------------------|------------------------|--------------------------------------|
| Loop  | Bigode treme       | (sem som)              | Visual only                          |
| 4s    | Papel cai          | `sfx_paper_flutter`    | Papel flutuando, 200ms, sutil        |
| 4.5s  | Papel carimbado    | `sfx_stamp_tiny`       | Micro-carimbada, 100ms, distante     |

### Walk
| Tempo       | Evento          | Sound Key              | Notas                               |
|-------------|-----------------|------------------------|--------------------------------------|
| Frame 2     | Passo esq       | `sfx_heavy_stomp`      | Impacto pesado, grave, 300ms         |
| Frame 4     | Botao voa       | `sfx_button_pop`       | Estalido metalico, 100ms, comico     |
| Frame 5     | Passo dir       | `sfx_heavy_stomp_hard` | Impacto MAIS pesado, 400ms           |
| Frame 1,4   | Carimbo arrasta  | `sfx_stamp_drag`       | Arrasto metalico no chao, continuo   |

### Attack
| Tempo  | Evento          | Sound Key              | Notas                               |
|--------|-----------------|------------------------|--------------------------------------|
| 0ms    | Ergue carimbo   | `sfx_whoosh_heavy`     | Whoosh grave pesado, 200ms           |
| 200ms  | CARIMBA!        | `sfx_stamp_slam`       | IMPACTO ENORME, grave, reverb, 400ms |
| 200ms  | Papeis voam     | `sfx_paper_burst`      | Rajada de papeis, 300ms              |
| 200ms  | Screen shake    | (sem som)              | Visual only                          |
| 200ms  | "NEGADO!" texto | `sfx_dino_negado`      | VOZ: "NEGADO!" grave, autoritario    |
| 366ms  | Recuperacao     | `sfx_stamp_settle`     | Carimbo assentando, 150ms, metalico  |

### Death
| Tempo  | Evento              | Sound Key              | Notas                               |
|--------|----------------------|------------------------|--------------------------------------|
| 0ms    | Rachadura            | `sfx_concrete_crack`   | Concreto rachando, 400ms             |
| 250ms  | Bracos murcham       | `sfx_deflate`          | Balao murchando grotesco, 500ms      |
| 250ms  | Papeis escapam       | `sfx_paper_flutter`    | Papeis voando, 600ms                 |
| 583ms  | Carimbo quebra       | `sfx_stamp_shatter`    | Vidro/metal quebrando, 300ms         |
| 583ms  | Toga explode         | `sfx_fabric_rip`       | Tecido rasgando forte, 200ms         |
| 583ms  | Emendas liberadas    | `sfx_confetti_burst`   | Confete festivo (ironia!), 500ms     |
| 833ms  | Escombros            | `sfx_rubble_settle`    | Escombros acomodando, 800ms, grave   |

### Hit
| Tempo  | Evento              | Sound Key              | Notas                               |
|--------|----------------------|------------------------|--------------------------------------|
| 0ms    | Impacto              | `sfx_stone_hit`        | Pedra sendo atingida, 200ms          |
| 0ms    | Flash branco         | (sem som)              | Visual only                          |
| 100ms  | Recomposicao         | `sfx_muscle_flex`      | Musculo contraindo, grave, 150ms     |

### Bloqueio Orcamentario
| Tempo  | Evento              | Sound Key              | Notas                               |
|--------|----------------------|------------------------|--------------------------------------|
| 0ms    | Preparacao           | `sfx_freeze_buildup`   | Tom crescente gelado, 300ms          |
| 300ms  | Carimba o ar         | `sfx_stamp_air`        | Carimbo no ar + eco, 200ms           |
| 300ms  | Onda de gelo         | `sfx_freeze_wave`      | Onda se espalhando, 400ms            |
| 500ms  | Congelamento         | `sfx_ice_crackle`      | Cristais formando, 500ms             |
| 750ms  | Bloqueio ativo       | `sfx_dino_bloqueado`   | VOZ: "BLOQUEADO." grave, seco        |
| +3000ms| Descongelamento      | `sfx_ice_melt`         | Gelo derretendo, 400ms               |

### Liminar Divina
| Tempo  | Evento              | Sound Key              | Notas                               |
|--------|----------------------|------------------------|--------------------------------------|
| 0ms    | Invocacao            | `sfx_judicial_gavel`   | Martelo judicial + eco, 400ms        |
| 0ms    | Olhos vermelhos      | `sfx_power_hum`        | Hum eletrico grave, loop 300ms       |
| 300ms  | Carimba chao         | `sfx_slam_supreme`     | IMPACTO MAXIMO, grave, reverb, 500ms |
| 500ms  | Muro cresce          | `sfx_wall_grow`        | Concreto subindo, ranger, 750ms      |
| 500ms  | Rachadura vermelha   | `sfx_crack_deep`       | Rachadura profunda, 300ms            |
| 1250ms | Muro completo        | `sfx_wall_seal`        | Selo final, THUD grave, 200ms        |
| 1250ms | Texto                | `sfx_dino_liminar`     | VOZ: "LIMINAR CONCEDIDA." grave      |
| +5000ms| Muro desmorona       | `sfx_wall_crumble`     | Desmoronamento, 800ms                |

### Muralha Burocratica
| Tempo  | Evento              | Sound Key              | Notas                               |
|--------|----------------------|------------------------|--------------------------------------|
| 0ms    | Inspiracao           | `sfx_deep_breath`      | Respiracao profunda, 350ms           |
| 0ms    | Botoes voam          | `sfx_buttons_pop`      | 3 estalidos em sequencia, 300ms      |
| 350ms  | Expansao             | `sfx_concrete_form`    | Concreto se formando, ranger, 400ms  |
| 750ms  | Muralha formada      | `sfx_wall_thud`        | Thud solido pesado, 200ms            |
| 750ms  | Passagem bloqueada   | `sfx_dino_muralha`     | VOZ: "NINGUEM PASSA." grave          |
| Loop   | Sapatos batendo      | `sfx_foot_tap`         | Sapato batendo, ritmico, 150ms cada  |

---

## Descricoes de Sons (para Sound Designer)

### Bordoes / Vozes
- **`sfx_dino_negado`**: "NEGADO!" — Voz masculina GRAVE, autoritaria, seca. Sem emocao. Como carimbo humano. 600ms.
- **`sfx_dino_bloqueado`**: "BLOQUEADO." — Mesma voz. Mais fria. Quase sussurrada mas pesada. 500ms.
- **`sfx_dino_liminar`**: "LIMINAR CONCEDIDA." — Voz com eco de tribunal. Reverb judicial. Autoritaria. 1000ms.
- **`sfx_dino_muralha`**: "NINGUEM PASSA." — Voz grossa como muro. Impossivel de ignorar. 800ms.

### Efeitos de Impacto
- **`sfx_stamp_slam`**: Impacto de carimbo GIGANTE metalico no chao. Como bigorna caindo. Grave profundo, reverb curto. Satisfatorio de ouvir. 400ms.
- **`sfx_heavy_stomp`**: Passo pesado. Impacto grave com sub-bass. Como elefante pisando. 300ms.
- **`sfx_heavy_stomp_hard`**: Versao mais intensa do stomp. +3dB, mais sub-bass. 400ms.
- **`sfx_slam_supreme`**: O impacto MAXIMO. Combinacao de bigorna + trovao + terremoto. Faz o sub tremer. 500ms.

### Efeitos de Destruicao
- **`sfx_concrete_crack`**: Concreto rachando. Estalo seco seguido de ranger. 400ms.
- **`sfx_stamp_shatter`**: Carimbo metalico quebrando. Vidro + metal. Dramatico. 300ms.
- **`sfx_fabric_rip`**: Tecido rasgando com forca. Alto e agudo. 200ms.
- **`sfx_rubble_settle`**: Escombros acomodando. Grave, multiplos impactos pequenos. 800ms.

### Efeitos de Congelamento
- **`sfx_freeze_buildup`**: Tom crescente que sugere gelo se formando. Agudo -> medio. 300ms.
- **`sfx_freeze_wave`**: Onda se espalhando. Swoosh gelado. 400ms.
- **`sfx_ice_crackle`**: Cristais de gelo se formando. Crepitar delicado e frio. 500ms.
- **`sfx_ice_melt`**: Gelo derretendo rapido. Gotejamento acelerado. 400ms.

---

## Attack Cooldown
- **Tempo minimo entre ataques**: 700ms (boss pesado, ataque devastador)
- **Feedback visual durante cooldown**: Carimbo na mao sem aura (opaco), idle sem tremor de bigode
- **Fim do cooldown**: Carimbo volta a brilhar, bigode treme, retoma `dino_idle`

## Boss HP e Enrage

### Barra de HP
- **HP Total**: 500 (boss resistente — e uma MURALHA)
- **Posicao da barra**: Acima do personagem, 48x4px, borda preta 1px
- **Cor**: Verde -> Amarelo -> Vermelho (gradiente por HP)
- **Nome sobre a barra**: "FLAVIO DINO — A MURALHA BUROCRATICA" (fonte Impact, 8px)

### Enrage (abaixo de 25% HP)
- **Visual**: Aura vermelha permanente ao redor do corpo. Bracos inflados 120%. Carimbo BRILHA vermelho constante. Veias visiveis em todo o corpo. Tela tem leve tint vermelho.
- **Mecanica**: Velocidade de ataque +50%. Bloqueio Orcamentario congela por 5s (em vez de 3s). Muralha Burocratica ativa automaticamente.
- **Som**: `sfx_dino_enrage` — "EU NAO BLOQUEIO POR PRAZER... TA, TAMBEM POR PRAZER." — Voz grave, com sorriso audivel.

---

## Integracao Phaser 3

### Sprite Sheet Loading Completo
```javascript
// Em preload()
this.load.spritesheet('boss_dino_idle', 'assets/personagens/flavio-dino/sprites/dino_idle.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('boss_dino_walk', 'assets/personagens/flavio-dino/sprites/dino_walk.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('boss_dino_attack', 'assets/personagens/flavio-dino/sprites/dino_attack.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('boss_dino_death', 'assets/personagens/flavio-dino/sprites/dino_death.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('boss_dino_hit', 'assets/personagens/flavio-dino/sprites/dino_hit.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('boss_dino_bloqueio', 'assets/personagens/flavio-dino/sprites/dino_bloqueio.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('boss_dino_liminar', 'assets/personagens/flavio-dino/sprites/dino_liminar.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('boss_dino_muralha', 'assets/personagens/flavio-dino/sprites/dino_muralha.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('projectile_negado', 'assets/personagens/flavio-dino/sprites/negado_mark.png', { frameWidth: 32, frameHeight: 32 });

// Audio
this.load.audio('sfx_stamp_slam', 'assets/audio/sfx/dino/stamp_slam.mp3');
this.load.audio('sfx_heavy_stomp', 'assets/audio/sfx/dino/heavy_stomp.mp3');
this.load.audio('sfx_dino_negado', 'assets/audio/bordoes/dino/negado.mp3');
// ... etc
```

### Hitbox do Boss
```javascript
// Hitbox normal
dino.body.setSize(40, 50);
dino.body.setOffset(12, 10);

// Hitbox modo muralha (Special 3)
dino.body.setSize(56, 50);
dino.body.setOffset(4, 10);
```

### Y-Sort Depth
```javascript
dino.setDepth(dino.y);
// Ajustar a cada frame no update
```
