# Janja (A Verdadeira Presidente) - Animation Spec (Phaser 3)

## Configuracao Geral

```javascript
// Phaser 3 Animation Config -- Janja
const JANJA_CONFIG = {
  spriteWidth: 64,
  spriteHeight: 64,
  projectileSize: 32,
  directions: ['south', 'north', 'east', 'west'],
  atlasKey: 'janja-atlas',
  defaultDirection: 'south'
};
```

---

## 1. IDLE -- Pose de Poder

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-idle-{direction}`                  |
| Frames         | 4                                         |
| Frame rate     | 8 FPS                                     |
| Repeat         | -1 (loop infinito)                        |
| Yoyo           | false                                     |
| Sheet size     | 256x64px (4 frames x 64px)               |
| Sheet (4dir)   | 256x256px                                 |

### Timing Detalhado

| Frame | Duracao (ms) | Evento                                           |
|-------|-------------|---------------------------------------------------|
| 0     | 125         | Pose base. Cabelo tamanho normal.                 |
| 1     | 125         | Cabelo pulsa +1px. Brincos esquerda. Celular pisca. |
| 2     | 125         | Cabelo contrai -1px. Brincos direita. Boca abre.  |
| 3     | 125         | Suspiro. Bolsa balanca. Notas flutuam atras.      |

### Efeitos Concorrentes (Particulas)

```javascript
// Particulas de notas de dinheiro flutuando (idle)
const idleMoneyParticles = {
  key: 'money-bill',
  quantity: 2,
  frequency: 800,        // 1 nota a cada 800ms
  lifespan: 2000,
  speed: { min: 5, max: 15 },
  angle: { min: 160, max: 200 },  // flutuam pra tras e pra cima
  scale: { start: 0.8, end: 0.3 },
  alpha: { start: 0.8, end: 0 },
  gravityY: -10,         // flutuam pra cima
  rotate: { min: -180, max: 180 }
};
```

### Overlay: Cabelo Pulsante

```javascript
// O cabelo pulsa independentemente como overlay
const hairPulse = {
  property: 'scaleX',
  from: 1.0,
  to: 1.03,              // expansao sutil de 3%
  duration: 250,
  yoyo: true,
  repeat: -1,
  ease: 'Sine.easeInOut'
};
```

### Codigo Phaser 3

```javascript
this.anims.create({
  key: 'janja-idle-south',
  frames: this.anims.generateFrameNumbers('janja-idle', {
    start: 0, end: 3
  }),
  frameRate: 8,
  repeat: -1
});

// Bolha de fala aleatoria (a cada 8-15 segundos no idle)
this.time.addEvent({
  delay: Phaser.Math.Between(8000, 15000),
  callback: () => {
    const bordoes = [
      'Mais uma reforminha, presidente?',
      'Para quem eu mando a conta, amor?',
      'Quem manda aqui sou eu, amor.'
    ];
    this.showSpeechBubble(
      bordoes[Phaser.Math.Between(0, bordoes.length - 1)]
    );
  },
  loop: true
});
```

---

## 2. WALK -- Desfile no Tapete

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-walk-{direction}`                  |
| Frames         | 6                                         |
| Frame rate     | 10 FPS                                    |
| Repeat         | -1 (loop infinito)                        |
| Yoyo           | false                                     |
| Sheet size     | 384x64px (6 frames x 64px)               |
| Sheet (4dir)   | 384x256px                                 |

### Timing Detalhado

| Frame | Duracao (ms) | Evento                                           |
|-------|-------------|---------------------------------------------------|
| 0     | 100         | Perna esq a frente. Tapete desenrola +4px.        |
| 1     | 100         | Transicao. Olha celular. Tapete +4px.             |
| 2     | 100         | Perna dir a frente. Bolsa balanca. Tapete +4px.   |
| 3     | 100         | Transicao. Cartao ao lado. Tapete continua.       |
| 4     | 100         | Perna esq. Bolsa pesa. Cabelo highlight muda.     |
| 5     | 100         | Deslize. Corpo flutua 1px. Tapete desfaz atras.   |

### Sistema de Tapete Vermelho (Walk)

```javascript
// O tapete e um objeto separado que segue a Janja
class TapeteVermelho extends Phaser.GameObjects.TileSprite {
  constructor(scene, janja) {
    super(scene, janja.x, janja.y, 48, 12, 'tapete-tile');
    this.janja = janja;
    this.maxLength = 48;
    this.decayRate = 0.5;        // pixels de decay por frame atras
  }

  update() {
    // Posiciona sob a Janja, estende na direcao do movimento
    this.x = this.janja.x;
    this.y = this.janja.y + 28;  // offset pra baixo dos pes

    // Direcao baseada no facing da Janja
    const dir = this.janja.facing;
    switch(dir) {
      case 'south': this.angle = 0; break;
      case 'north': this.angle = 180; break;
      case 'east':  this.angle = 90; break;
      case 'west':  this.angle = 270; break;
    }
  }
}
```

### Particulas de Notas (Decay do Tapete)

```javascript
// Notas que se soltam de tras do tapete enquanto Janja anda
const walkMoneyParticles = {
  key: 'money-bill',
  quantity: 1,
  frequency: 300,         // nota a cada 300ms (mais frequente que idle)
  lifespan: 1500,
  speed: { min: 10, max: 30 },
  angle: { min: -30, max: 30 },  // espalham pros lados atras
  scale: { start: 1.0, end: 0.2 },
  alpha: { start: 1.0, end: 0 },
  gravityY: -15,          // flutuam
  rotate: { min: -360, max: 360 },
  emitZone: {
    type: 'edge',
    source: new Phaser.Geom.Line(-24, 0, 24, 0),  // atras do tapete
    quantity: 1
  }
};
```

### Codigo Phaser 3

```javascript
this.anims.create({
  key: 'janja-walk-south',
  frames: this.anims.generateFrameNumbers('janja-walk-s', {
    start: 0, end: 5
  }),
  frameRate: 10,
  repeat: -1
});

// Brincos como sub-sprite com delay
this.brincos = this.scene.add.sprite(0, 0, 'janja-brincos');
this.brincos.setOrigin(0.5, 0);

// Brincos balancam com offset do body velocity
this.scene.tweens.add({
  targets: this.brincos,
  x: { from: -1, to: 1 },
  duration: 200,
  yoyo: true,
  repeat: -1,
  ease: 'Sine.easeInOut'
});
```

---

## 3. ATTACK -- Cartao Corporativo

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-attack-{direction}`                |
| Frames         | 3                                         |
| Frame rate     | 12 FPS                                    |
| Repeat         | 0 (uma vez)                               |
| Yoyo           | false                                     |
| Sheet size     | 192x64px (3 frames x 64px)               |
| Sheet (4dir)   | 192x256px                                 |

### Timing Detalhado

| Frame | Duracao (ms) | Evento / Callback                                |
|-------|-------------|---------------------------------------------------|
| 0     | 83          | Windup. Levanta cartao. Boca abre. SPAWN bolha "COMPRA!" |
| 1     | 83          | Swipe. Trail dourado. SPAWN 3-4 projeteis de luxo. |
| 2     | 83          | Impact. Explosao de cifras. Pose vitoriosa. SFX: ka-ching. |

### Projeteis de Luxo (Spawning)

```javascript
// No frame 1 do attack, spawna projeteis de luxo caindo do ceu
onAttackFrame1() {
  const luxuryItems = ['bolsa-grife', 'sapato-salto', 'colar-diamante', 'joia-anel'];
  const numProjectiles = Phaser.Math.Between(3, 4);

  for (let i = 0; i < numProjectiles; i++) {
    const item = luxuryItems[Phaser.Math.Between(0, luxuryItems.length - 1)];
    const offsetX = Phaser.Math.Between(-32, 32);
    const offsetY = Phaser.Math.Between(-48, -32);

    const proj = this.scene.physics.add.sprite(
      this.x + offsetX,
      this.y + offsetY,
      item
    );

    // Rotacao no ar
    this.scene.tweens.add({
      targets: proj,
      angle: 360,
      duration: 400,
      repeat: 0
    });

    // Queda
    proj.body.setGravityY(300);
    proj.body.setVelocityX(Phaser.Math.Between(-50, 50));

    // Trail dourado
    const trail = this.scene.add.particles(proj.x, proj.y, 'gold-sparkle', {
      follow: proj,
      frequency: 50,
      lifespan: 300,
      scale: { start: 0.5, end: 0 },
      alpha: { start: 0.8, end: 0 },
      tint: 0xFFD700
    });

    // Impacto
    proj.body.onWorldBounds = true;
    this.scene.time.delayedCall(500, () => {
      this.spawnCifraoExplosion(proj.x, proj.y);
      trail.destroy();
      proj.destroy();
    });
  }
}
```

### Explosao de Cifras (Impacto)

```javascript
spawnCifraoExplosion(x, y) {
  const cifras = this.scene.add.particles(x, y, 'cifrao-rs', {
    quantity: 5,
    lifespan: 600,
    speed: { min: 30, max: 80 },
    angle: { min: 0, max: 360 },
    scale: { start: 1.0, end: 0.3 },
    alpha: { start: 1.0, end: 0 },
    gravityY: -20,
    tint: 0xFFD700
  });

  // Flash branco no ponto de impacto
  const flash = this.scene.add.circle(x, y, 16, 0xFFFFFF, 0.8);
  this.scene.tweens.add({
    targets: flash,
    alpha: 0,
    scale: 2,
    duration: 200,
    onComplete: () => flash.destroy()
  });

  this.scene.time.delayedCall(800, () => cifras.destroy());
}
```

### Codigo Phaser 3

```javascript
this.anims.create({
  key: 'janja-attack-south',
  frames: this.anims.generateFrameNumbers('janja-attack-s', {
    start: 0, end: 2
  }),
  frameRate: 12,
  repeat: 0
});

// Callback por frame
this.sprite.on('animationupdate', (anim, frame) => {
  if (anim.key.startsWith('janja-attack')) {
    if (frame.index === 0) this.showSpeechBubble('COMPRA!');
    if (frame.index === 1) this.spawnLuxuryProjectiles();
    if (frame.index === 2) this.scene.cameras.main.shake(80, 0.005);
  }
});

// Retorna pra idle ao terminar
this.sprite.on('animationcomplete-janja-attack-south', () => {
  this.sprite.play('janja-idle-south');
});
```

---

## 4. DEATH -- Queda da Primeira-Dama

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-death`                             |
| Frames         | 4                                         |
| Frame rate     | 6 FPS                                     |
| Repeat         | 0 (uma vez)                               |
| Yoyo           | false                                     |
| Sheet size     | 256x64px (4 frames x 64px)               |
| Direcao unica  | Sim (sem 4 direcoes)                      |

### Timing Detalhado

| Frame | Duracao (ms) | Evento / Callback                                         |
|-------|-------------|-------------------------------------------------------------|
| 0     | 166         | Impacto. SPAWN bolsa voando (projetil). SPAWN cartao voando. SPAWN celular quebrando. |
| 1     | 166         | Cabelo desmonta. SPAWN brincos voando. SFX: gasp dramatico. |
| 2     | 1500        | No chao. TRIGGER bolsa explode em notas (10 particulas). Maquiagem borra. |
| 3     | 1500        | Fade. Notas caem. Tapete dissolve. Cores dessaturam. Bolha: "a conta..." |

**Nota**: Frames 2-3 tem duracao ESTENDIDA (1500ms cada) para efeito dramatico.

### Bolsa Explodindo em Notas

```javascript
onDeathFrame2() {
  // A bolsa cai e EXPLODE em notas de dinheiro
  const bolsaX = this.x - 10;
  const bolsaY = this.y + 5;

  // Explosao em leque
  const moneyExplosion = this.scene.add.particles(bolsaX, bolsaY, 'money-bill', {
    quantity: 10,
    lifespan: 2000,
    speed: { min: 40, max: 100 },
    angle: { min: 200, max: 340 },  // leque pra cima e pros lados
    scale: { start: 1.0, end: 0.5 },
    alpha: { start: 1.0, end: 0 },
    gravityY: 20,           // caem lentamente
    rotate: { min: -360, max: 360 },
    emitZone: {
      type: 'random',
      source: new Phaser.Geom.Circle(0, 0, 4)
    }
  });

  // Camera shake na explosao
  this.scene.cameras.main.shake(200, 0.01);

  this.scene.time.delayedCall(2500, () => moneyExplosion.destroy());
}
```

### Tapete Dissolvendo

```javascript
onDeathFrame3() {
  // Tapete se dissolve em particulas
  if (this.tapete) {
    this.scene.tweens.add({
      targets: this.tapete,
      alpha: 0,
      scaleX: 0.5,
      duration: 1500,
      ease: 'Power2',
      onComplete: () => this.tapete.destroy()
    });

    // Particulas de tapete se soltando
    const tapeteParticles = this.scene.add.particles(
      this.tapete.x, this.tapete.y, 'tapete-fragment', {
        quantity: 8,
        lifespan: 1200,
        speed: { min: 10, max: 30 },
        angle: { min: 0, max: 360 },
        scale: { start: 0.6, end: 0 },
        alpha: { start: 0.8, end: 0 },
        tint: 0x8B0000
      }
    );

    this.scene.time.delayedCall(1500, () => tapeteParticles.destroy());
  }
}
```

### Dessaturacao

```javascript
onDeathFrame3Continued() {
  // Dessatura o sprite inteiro em 30%
  const desatPipeline = this.scene.renderer.pipelines.get('Desaturate');
  this.sprite.setPipeline(desatPipeline);

  // Ou com tween manual de tint
  this.scene.tweens.add({
    targets: this.sprite,
    tint: 0x888888,
    duration: 1500,
    ease: 'Linear'
  });
}
```

### Codigo Phaser 3

```javascript
this.anims.create({
  key: 'janja-death',
  frames: this.anims.generateFrameNumbers('janja-death', {
    start: 0, end: 3
  }),
  frameRate: 6,
  repeat: 0,
  // Duracao customizada por frame
  // Implementada via callback (Phaser nao suporta duracao por frame nativamente)
});

// Controle manual de duracao por frame
playDeathAnimation() {
  const frameDurations = [166, 166, 1500, 1500];
  let currentFrame = 0;

  const advanceFrame = () => {
    this.sprite.setFrame(currentFrame);
    this.triggerDeathFrameEvent(currentFrame);

    if (currentFrame < 3) {
      this.scene.time.delayedCall(frameDurations[currentFrame], () => {
        currentFrame++;
        advanceFrame();
      });
    } else {
      // Apos ultimo frame, fade out e destroy
      this.scene.time.delayedCall(frameDurations[3], () => {
        this.scene.tweens.add({
          targets: this.sprite,
          alpha: 0,
          duration: 500,
          onComplete: () => this.destroy()
        });
      });
    }
  };

  advanceFrame();
}
```

---

## 5. HIT -- Indignacao

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-hit-{direction}`                   |
| Frames         | 2                                         |
| Frame rate     | 12 FPS                                    |
| Repeat         | 0 (uma vez)                               |
| Yoyo           | false                                     |
| Sheet size     | 128x64px (2 frames x 64px)               |
| Sheet (4dir)   | 128x256px                                 |

### Timing Detalhado

| Frame | Duracao (ms) | Evento / Callback                                |
|-------|-------------|---------------------------------------------------|
| 0     | 83          | Recuo 2px. Flash branco. SPAWN bolha "COMO OUSAM?!" Cabelo treme. |
| 1     | 83          | Recuperacao. Olhos vermelhos. Unhas maiores. Mais furiosa. |

### Flash de Dano

```javascript
onHit(damage, direction) {
  // Recuo
  const knockbackX = direction === 'east' ? -2 : direction === 'west' ? 2 : 0;
  const knockbackY = direction === 'south' ? -2 : direction === 'north' ? 2 : 0;

  this.sprite.x += knockbackX;
  this.sprite.y += knockbackY;

  // Flash branco (1 frame)
  this.sprite.setTintFill(0xFFFFFF);
  this.scene.time.delayedCall(83, () => {
    this.sprite.clearTint();
  });

  // Bolha de indignacao
  this.showSpeechBubble('COMO OUSAM?!');

  // Play hit animation
  this.sprite.play('janja-hit-' + this.facing);

  // Apos hit, volta pro idle mais furiosa (tint levemente vermelho)
  this.sprite.on('animationcomplete-janja-hit-' + this.facing, () => {
    this.sprite.setTint(0xFFCCCC);  // leve tint vermelho de raiva
    this.sprite.play('janja-idle-' + this.facing);
    // Tint some apos 2 segundos
    this.scene.time.delayedCall(2000, () => this.sprite.clearTint());
  });
}
```

---

## 6. SPECIAL: FORA ELON MUSK! -- Grito EMP

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-fora-elon`                         |
| Frames         | 6                                         |
| Frame rate     | 10 FPS                                    |
| Repeat         | 0 (uma vez)                               |
| Yoyo           | false                                     |
| Sheet size     | 384x64px (6 frames x 64px)               |
| Direcao unica  | Sim (sempre sul/frente, o grito e omni)   |
| Cooldown       | 15 segundos                               |

### Timing Detalhado

| Frame | Duracao (ms) | Evento / Callback                                         |
|-------|-------------|-------------------------------------------------------------|
| 0     | 100         | Preparacao. Para, planta pes. Larga celular. Rosto avermelha. |
| 1     | 100         | Buildup. Cabelo CRESCE +4px. Eletricidade estática spawn. Punhos cerrados. |
| 2     | 100         | O GRITO. Boca 90% do rosto. Ondas sonicas. Projetil "FORA ELON!" spawn. Camera shake. |
| 3     | 100         | Onda EMP. Circulo azul expande. Dispositivos faiscam. Particulas eletricidade. |
| 4     | 100         | EMP continua. Static na tela. Icones "sem sinal" nos inimigos. |
| 5     | 100         | Recuperacao. Boca fecha. Sorriso. Cabelo deflata. Pega celular. |

### Ondas Sonicas (Frame 2)

```javascript
spawnSonicWaves() {
  // 3 ondas concentricas que se expandem da boca
  for (let i = 0; i < 3; i++) {
    const wave = this.scene.add.arc(
      this.x, this.y - 8,  // posicao da boca
      8 + (i * 4),          // raio inicial escalonado
      0, 360, false,
      0xFF4500, 0.6 - (i * 0.15)  // laranja-vermelho, alpha decrescente
    );
    wave.setStrokeStyle(2, 0xFF4500);
    wave.setFillStyle();  // sem fill, so stroke

    this.scene.tweens.add({
      targets: wave,
      scaleX: 4 + i,
      scaleY: 4 + i,
      alpha: 0,
      duration: 600 + (i * 100),
      ease: 'Power1',
      delay: i * 80,       // escalonamento temporal
      onComplete: () => wave.destroy()
    });
  }
}
```

### Onda EMP (Frames 3-4)

```javascript
spawnEMPWave() {
  // Circulo azul eletrico que se expande
  const emp = this.scene.add.circle(
    this.x, this.y, 4, 0x00BFFF, 0.4
  );
  emp.setStrokeStyle(2, 0x00BFFF, 0.8);

  this.scene.tweens.add({
    targets: emp,
    scaleX: 12,        // raio final de ~48px
    scaleY: 12,
    alpha: 0,
    duration: 800,
    ease: 'Power2',
    onComplete: () => emp.destroy()
  });

  // Particulas de eletricidade ao longo da onda
  const empParticles = this.scene.add.particles(this.x, this.y, 'electricity', {
    quantity: 8,
    lifespan: 500,
    speed: { min: 80, max: 160 },
    angle: { min: 0, max: 360 },
    scale: { start: 0.8, end: 0.1 },
    alpha: { start: 1.0, end: 0 },
    tint: 0xFFD700,
    frequency: 100,
    maxParticles: 20
  });

  // Efeito de desativar tecnologia: todos inimigos recebem debuff
  this.scene.enemies.forEach(enemy => {
    const dist = Phaser.Math.Distance.Between(this.x, this.y, enemy.x, enemy.y);
    if (dist <= 192) {  // raio de efeito (3 tiles)
      enemy.disableTech(3000);  // 3 segundos

      // Icone de "sem sinal" acima do inimigo
      const noSignal = this.scene.add.sprite(enemy.x, enemy.y - 36, 'no-signal-icon');
      this.scene.tweens.add({
        targets: noSignal,
        alpha: { from: 1, to: 0 },
        duration: 3000,
        onComplete: () => noSignal.destroy()
      });
    }
  });

  // Screen static effect
  this.scene.cameras.main.shake(300, 0.008);
  // Opcional: post-processing static overlay por 3s
  this.showStaticOverlay(3000);

  this.scene.time.delayedCall(1000, () => empParticles.destroy());
}
```

### Projetil "FORA ELON!" (Frame 2)

```javascript
spawnForaElonProjectile() {
  // Texto como projetil que voa na direcao do facing
  const text = this.scene.add.bitmapText(
    this.x, this.y - 12,
    'pixel-font-bold', 'FORA ELON!', 8
  );
  text.setTint(0xFF0000);
  text.setOrigin(0.5);

  // Borda amarela simulada com shadow
  // Ou usar sprite pre-renderizado 32x12px

  const dirVectors = {
    south: { x: 0, y: 200 },
    north: { x: 0, y: -200 },
    east:  { x: 200, y: 0 },
    west:  { x: -200, y: 0 }
  };

  const vel = dirVectors[this.facing];

  this.scene.tweens.add({
    targets: text,
    x: text.x + vel.x,
    y: text.y + vel.y,
    alpha: 0,
    duration: 1000,
    ease: 'Power1',
    onComplete: () => text.destroy()
  });
}
```

---

## 7. SPECIAL: SUSSURRO PRESIDENCIAL -- Mind Control

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-sussurro`                          |
| Frames         | 4                                         |
| Frame rate     | 8 FPS                                     |
| Repeat         | 0 (uma vez)                               |
| Yoyo           | false                                     |
| Sheet size     | 256x64px (4 frames x 64px)               |
| Requer alvo    | Lula-zumbi dentro de 48px                 |
| Cooldown       | 20 segundos                               |

### Timing Detalhado

| Frame | Duracao (ms) | Evento / Callback                                         |
|-------|-------------|-------------------------------------------------------------|
| 0     | 125         | Janja se inclina. Bolha "psss..." spawn.                   |
| 1     | 125         | Aproxima do Lula. Particulas roxas trail boca -> cabeca.   |
| 2     | 125         | Lula com olhos espiral. Icone controlado spawn.            |
| 3     | 125         | Pose satisfeita. Bolhas de dialogo duplas.                 |

### Particulas de Controle Mental (Roxo)

```javascript
spawnMindControlTrail(target) {
  // Trail de particulas roxas da boca da Janja ate a cabeca do Lula
  const startX = this.x + 8;   // offset boca
  const startY = this.y - 10;
  const endX = target.x;
  const endY = target.y - 20;  // offset cabeca do alvo

  // Curva bezier para o trail
  const curve = new Phaser.Curves.CubicBezier(
    new Phaser.Math.Vector2(startX, startY),
    new Phaser.Math.Vector2(startX + 10, startY - 15),
    new Phaser.Math.Vector2(endX - 10, endY - 10),
    new Phaser.Math.Vector2(endX, endY)
  );

  // Particulas seguindo a curva
  for (let i = 0; i < 4; i++) {
    const particle = this.scene.add.circle(startX, startY, 2, 0x660066, 0.8);

    const point = { t: 0 };
    this.scene.tweens.add({
      targets: point,
      t: 1,
      duration: 500,
      delay: i * 80,
      ease: 'Sine.easeInOut',
      onUpdate: () => {
        const pos = curve.getPoint(point.t);
        particle.x = pos.x;
        particle.y = pos.y;
      },
      onComplete: () => {
        // Flash ao atingir a cabeca
        particle.setFillStyle(0x9933FF, 1);
        this.scene.tweens.add({
          targets: particle,
          alpha: 0,
          scale: 2,
          duration: 200,
          onComplete: () => particle.destroy()
        });
      }
    });
  }
}
```

### Efeito de Hipnose no Lula

```javascript
applyMindControl(lulaZombie) {
  // Olhos em espiral (overlay animado)
  const spiralEyes = this.scene.add.sprite(
    lulaZombie.x, lulaZombie.y - 16, 'spiral-eyes'
  );
  spiralEyes.play('spiral-rotate');  // animacao de espiral girando

  // Icone de "controlado" acima
  const controlIcon = this.scene.add.sprite(
    lulaZombie.x, lulaZombie.y - 36, 'control-eye-icon'
  );
  controlIcon.setTint(0x660066);

  // Aura roxa pulsante no Lula
  this.scene.tweens.add({
    targets: lulaZombie.sprite,
    tint: { from: 0xFFFFFF, to: 0xCC99FF },
    duration: 400,
    yoyo: true,
    repeat: -1
  });

  // Lula agora segue comandos da Janja por 10 segundos
  lulaZombie.setControlled(true, this, 10000);

  // Bolhas de dialogo
  this.scene.time.delayedCall(400, () => {
    this.showSpeechBubble('Bom menino');
    lulaZombie.showSpeechBubble('Sim, amor');
  });

  // Cleanup apos duracao
  this.scene.time.delayedCall(10000, () => {
    spiralEyes.destroy();
    controlIcon.destroy();
    lulaZombie.sprite.clearTint();
    lulaZombie.setControlled(false);
  });
}
```

---

## 8. SPECIAL: TAPETE VERMELHO -- Area Slow

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-tapete`                            |
| Frames         | 4                                         |
| Frame rate     | 8 FPS                                     |
| Repeat         | 0 (uma vez, tapete persiste)              |
| Yoyo           | false                                     |
| Sheet size     | 256x64px (4 frames x 64px)               |
| Direcao unica  | Sim (tapete se estende no facing)         |
| Cooldown       | 12 segundos                               |
| Duracao efeito | 8 segundos                                |

### Timing Detalhado

| Frame | Duracao (ms) | Evento / Callback                                         |
|-------|-------------|-------------------------------------------------------------|
| 0     | 125         | Estala dedos. Flash dourado. Bolha: "Estendam o tapete!"   |
| 1     | 125         | Tapete se estende 16px/frame. Franjas douradas. Brilhos.   |
| 2     | 125         | Tapete maximo (96x16px). Slow zone ativa. Notas flutuam.  |
| 3     | 125         | Tapete estabiliza. Pulsacao suave. Janja desfila.          |

### Objeto Tapete (Skill Area)

```javascript
class TapeteVermelhoSkill extends Phaser.GameObjects.TileSprite {
  constructor(scene, x, y, direction) {
    // Tapete comeca pequeno e se estende
    super(scene, x, y, 16, 16, 'tapete-vermelho-tile');
    this.scene = scene;
    this.direction = direction;
    this.maxLength = 96;
    this.currentLength = 16;
    this.slowFactor = 0.5;      // inimigos ficam 50% mais lentos
    this.duration = 8000;        // 8 segundos

    scene.add.existing(this);
    scene.physics.add.existing(this, true);  // static body

    this.extend();
  }

  extend() {
    // Tween de extensao
    this.scene.tweens.add({
      targets: this,
      width: this.maxLength,
      duration: 400,
      ease: 'Power2',
      onUpdate: () => {
        this.body.setSize(this.width, this.height);
        this.setDisplaySize(this.width, this.height);
      }
    });

    // Particulas de brilho no tapete
    this.sparkles = this.scene.add.particles(this.x, this.y, 'gold-sparkle', {
      frequency: 200,
      lifespan: 600,
      scale: { start: 0.5, end: 0 },
      alpha: { start: 0.6, end: 0 },
      tint: 0xFFD700,
      emitZone: {
        type: 'random',
        source: new Phaser.Geom.Rectangle(-48, -8, 96, 16)
      }
    });

    // Notas flutuando das bordas
    this.moneyEmitter = this.scene.add.particles(this.x, this.y, 'money-bill', {
      frequency: 600,
      lifespan: 1200,
      quantity: 1,
      speed: { min: 8, max: 20 },
      angle: { min: 240, max: 300 },
      scale: { start: 0.7, end: 0.2 },
      alpha: { start: 0.6, end: 0 },
      gravityY: -15,
      emitZone: {
        type: 'edge',
        source: new Phaser.Geom.Rectangle(-48, -8, 96, 16),
        quantity: 1
      }
    });

    // Auto-destroy apos duracao
    this.scene.time.delayedCall(this.duration, () => this.fadeOut());
  }

  fadeOut() {
    this.sparkles.stop();
    this.moneyEmitter.stop();

    this.scene.tweens.add({
      targets: this,
      alpha: 0,
      width: 8,
      duration: 1000,
      ease: 'Power2',
      onComplete: () => {
        this.sparkles.destroy();
        this.moneyEmitter.destroy();
        this.destroy();
      }
    });
  }
}
```

### Slow Effect nos Inimigos

```javascript
// Overlap check no update loop
this.scene.physics.overlap(tapete, enemyGroup, (tapete, enemy) => {
  if (!enemy.isSlowed) {
    enemy.isSlowed = true;
    enemy.originalSpeed = enemy.speed;
    enemy.speed *= tapete.slowFactor;

    // Visual: correntes douradas nos pes
    const chains = this.scene.add.sprite(enemy.x, enemy.y + 24, 'gold-chains');
    chains.play('chains-wiggle');
    enemy.chainSprite = chains;

    // Quando sair do tapete
    enemy.once('exitTapete', () => {
      enemy.speed = enemy.originalSpeed;
      enemy.isSlowed = false;
      if (enemy.chainSprite) enemy.chainSprite.destroy();
    });
  }
});
```

---

## 9. SPECIAL: REFORMA COMPULSORIA -- Cenario Luxo

### Ciclo de Animacao

| Propriedade    | Valor                                     |
|---------------|-------------------------------------------|
| Key            | `janja-reforma`                           |
| Frames         | 4                                         |
| Frame rate     | 8 FPS                                     |
| Repeat         | 0 (uma vez, efeito persiste)              |
| Yoyo           | false                                     |
| Sheet size     | 256x64px (4 frames x 64px)               |
| Direcao unica  | Sim                                       |
| Cooldown       | 25 segundos                               |
| Duracao efeito | 10 segundos                               |
| Raio           | 128px (2 tiles em todas direcoes)         |

### Timing Detalhado

| Frame | Duracao (ms) | Evento / Callback                                         |
|-------|-------------|-------------------------------------------------------------|
| 0     | 125         | Beija cartao. Olhos cifrao. Bolha: "Mais uma reforminha!"  |
| 1     | 125         | Cartao brilha. Raios dourados 8 direcoes. Onda dourada.    |
| 2     | 125         | Tiles mudam (overlay luxo). Notas voam radialmente.        |
| 3     | 125         | Cenario estabiliza. Confete cai. Pose satisfeita.          |

### Onda Dourada (Frame 1)

```javascript
spawnGoldenWave() {
  // Raios em 8 direcoes
  for (let angle = 0; angle < 360; angle += 45) {
    const ray = this.scene.add.line(
      this.x, this.y,
      0, 0,
      Math.cos(angle * Math.PI / 180) * 8,
      Math.sin(angle * Math.PI / 180) * 8,
      0xFFD700, 0.8
    );
    ray.setLineWidth(1);

    this.scene.tweens.add({
      targets: ray,
      scaleX: 16,
      scaleY: 16,
      alpha: 0,
      duration: 500,
      ease: 'Power1',
      onComplete: () => ray.destroy()
    });
  }

  // Onda circular dourada
  const wave = this.scene.add.circle(this.x, this.y, 4, 0xFFD700, 0.3);
  wave.setStrokeStyle(2, 0xFFD700, 0.6);

  this.scene.tweens.add({
    targets: wave,
    scaleX: 32,
    scaleY: 32,
    alpha: 0,
    duration: 800,
    ease: 'Power2',
    onComplete: () => wave.destroy()
  });
}
```

### Overlay de Luxo nos Tiles

```javascript
applyLuxuryOverlay(centerX, centerY, radius) {
  const overlayTiles = [];
  const tileSize = 32;

  // Encontra todos tiles no raio
  for (let dx = -radius; dx <= radius; dx += tileSize) {
    for (let dy = -radius; dy <= radius; dy += tileSize) {
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist <= radius) {
        const overlay = this.scene.add.sprite(
          centerX + dx, centerY + dy,
          'luxury-overlay'
        );
        overlay.setAlpha(0);
        overlay.setDepth(0.5);  // entre chao e personagens

        // Fade in com delay baseado na distancia
        this.scene.tweens.add({
          targets: overlay,
          alpha: 0.5,
          duration: 300,
          delay: dist * 2,  // mais longe = mais delay (onda)
          ease: 'Power1'
        });

        overlayTiles.push(overlay);
      }
    }
  }

  // Confete dourado caindo
  const confetti = this.scene.add.particles(centerX, centerY - 64, 'confete-dourado', {
    quantity: 15,
    lifespan: 3000,
    frequency: 200,
    speed: { min: 10, max: 40 },
    angle: { min: 60, max: 120 },  // cai de cima
    scale: { start: 0.8, end: 0.3 },
    alpha: { start: 0.8, end: 0 },
    gravityY: 30,
    rotate: { min: -180, max: 180 },
    emitZone: {
      type: 'random',
      source: new Phaser.Geom.Rectangle(-radius, -32, radius * 2, 32)
    }
  });

  // Cleanup apos 10 segundos
  this.scene.time.delayedCall(10000, () => {
    overlayTiles.forEach(tile => {
      this.scene.tweens.add({
        targets: tile,
        alpha: 0,
        duration: 1000,
        onComplete: () => tile.destroy()
      });
    });
    confetti.stop();
    this.scene.time.delayedCall(3000, () => confetti.destroy());
  });
}
```

---

## TRANSICOES ENTRE ANIMACOES

### Tabela de Transicoes

| De                    | Para                  | Condicao                    | Blend (ms) |
|----------------------|----------------------|-----------------------------|------------|
| idle                  | walk                  | velocity > 0                | 0          |
| walk                  | idle                  | velocity == 0               | 0          |
| idle/walk             | attack                | input attack                | 0          |
| attack                | idle                  | animacao completa           | 50         |
| idle/walk             | hit                   | recebe dano                 | 0          |
| hit                   | idle                  | animacao completa           | 50         |
| qualquer              | death                 | HP <= 0                     | 0          |
| idle                  | fora-elon             | input special 1             | 0          |
| fora-elon             | idle                  | animacao completa           | 100        |
| idle                  | sussurro              | input special 2 + alvo perto| 0          |
| sussurro              | idle                  | animacao completa           | 100        |
| idle                  | tapete                | input special 3             | 0          |
| tapete                | walk                  | animacao completa           | 0          |
| idle                  | reforma               | input special 4             | 0          |
| reforma               | idle                  | animacao completa           | 100        |

### Prioridade de Animacao (maior = prioridade)

| Prioridade | Animacao         |
|-----------|------------------|
| 5         | death             |
| 4         | hit               |
| 3         | fora-elon         |
| 3         | sussurro          |
| 3         | tapete            |
| 3         | reforma           |
| 2         | attack            |
| 1         | walk              |
| 0         | idle              |

### State Machine

```javascript
class JanjaAnimationController {
  constructor(sprite) {
    this.sprite = sprite;
    this.currentState = 'idle';
    this.currentPriority = 0;
    this.facing = 'south';
    this.locked = false;  // true durante animacoes nao-interruptiveis
  }

  play(animName, priority, lock = false) {
    if (this.locked && priority < 5) return;  // so death interrompe lock
    if (priority < this.currentPriority) return;

    this.currentState = animName;
    this.currentPriority = priority;
    this.locked = lock;

    const key = `janja-${animName}-${this.facing}`;
    this.sprite.play(key);

    if (lock) {
      this.sprite.once('animationcomplete', () => {
        this.locked = false;
        this.currentPriority = 0;
        this.play('idle', 0);
      });
    }
  }

  update(velocity) {
    if (this.locked) return;

    if (velocity.length() > 0) {
      this.updateFacing(velocity);
      this.play('walk', 1);
    } else {
      this.play('idle', 0);
    }
  }

  updateFacing(velocity) {
    if (Math.abs(velocity.x) > Math.abs(velocity.y)) {
      this.facing = velocity.x > 0 ? 'east' : 'west';
    } else {
      this.facing = velocity.y > 0 ? 'south' : 'north';
    }
  }
}
```

---

## SISTEMA DE PARTICULAS -- RESUMO CONSOLIDADO

### Emitters Ativos por Estado

| Estado        | Emitters Ativos                                         |
|--------------|----------------------------------------------------------|
| idle          | money-bills (lento), hair-pulse (tween)                 |
| walk          | money-bills (rapido), tapete-trail                      |
| attack        | luxury-projectiles, cifrao-explosion, gold-trail        |
| death         | money-explosion, tapete-dissolve, makeup-fragments      |
| hit           | (nenhum emitter novo, so flash)                         |
| fora-elon     | sonic-waves, emp-circle, electricity, static-overlay    |
| sussurro      | purple-mind-control-trail, spiral-eyes-overlay          |
| tapete        | gold-sparkles, money-from-edges, chains-on-enemies      |
| reforma       | golden-rays, golden-wave, luxury-overlay, confetti      |

### Performance Budget

| Metrica                     | Limite                |
|----------------------------|------------------------|
| Particulas simultaneas max  | 60                     |
| Emitters ativos max         | 4                      |
| Projeteis ativos max        | 8                      |
| Overlays ativos max         | 32 (reforma)           |
| Target FPS                  | 60 (jogo), 8-12 (sprite anim) |

---

## AUDIO TRIGGERS (Referencia para SFX)

| Animacao        | Frame | SFX Sugerido                              |
|----------------|-------|-------------------------------------------|
| idle            | 3     | "hmm" de desprezo (baixo)                 |
| walk            | 0,3   | click de salto alto                       |
| attack          | 0     | "COMPRA!" (voz)                           |
| attack          | 2     | ka-ching metalico                         |
| death           | 0     | gasp dramatico                            |
| death           | 2     | notas espalhando (paper flutter)          |
| hit             | 0     | "COMO OUSAM?!" (voz)                      |
| fora-elon       | 2     | "FORA ELON MUSK!" (grito, voz)           |
| fora-elon       | 3     | zap eletrico / EMP whoosh                 |
| sussurro        | 0     | "psss..." (sussurro, voz)                 |
| sussurro        | 3     | "Bom menino" (satisfeita, voz)            |
| tapete          | 0     | snap de dedos                             |
| tapete          | 1     | carpet unroll (swoosh de tecido)          |
| reforma         | 0     | beijo (smack)                             |
| reforma         | 1     | brilho magico (shimmer)                   |
