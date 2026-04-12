# ZUMBIS DE BRASÍLIA — Plano de Frontend Web MVP
### Cada Frame Importa. Cada Toque Importa. Cada Pixel Importa. No Browser.

**Versão 1.0 | Abril 2026**
**Masahiro Sakurai — Game Feel & Frontend Architecture (Browser Edition)**

---

> *"Quando me pediram para fazer Kirby correr em 60fps num Game Boy, eu não disse 'o hardware não permite'. Eu perguntei: 'o que posso cortar sem o jogador notar?' A pergunta certa nunca é o que a máquina aguenta. É o que o jogador SENTE. Um browser é uma máquina de jogar. Duas semanas é tempo suficiente para fazer sentir certo."*

---

## Contexto do Pivot

O plano original (documento 07) foi escrito para Godot 4 rodando em Android nativo — Samsung Galaxy A06, Helio G85, OpenGL ES 3.0. Era um plano correto para aquela plataforma.

O CEO e o André Guedes tomaram a decisão certa: **browser game primeiro**. Duas semanas, HTML5, sem download. Isso muda a plataforma de execução, mas não muda a filosofia. Game feel não é feature de engine. Game feel é intenção.

Este documento é a tradução fiel do plano original para o browser. Cada conceito que importava em Godot tem um equivalente aqui. Onde não tem equivalente direto, tem solução melhor.

---

## 1. Rendering no Browser — Canvas 2D vs WebGL

### A Decisão: WebGL com Phaser 3 (não Canvas 2D puro)

Canvas 2D nativo do browser é lento para jogos com muitos sprites simultâneos. O problema não é o rasterizador — é o overhead de JavaScript chamando a API de Canvas a cada frame. Com 50+ entidades em tela, cada `drawImage()` individual vai fragmentar o frame budget.

**A solução é usar WebGL via Phaser 3.** O Phaser usa WebGL por padrão e faz batching automático de sprites com a mesma textura numa única draw call. O fallback para Canvas 2D existe para devices muito antigos, mas em 2026 qualquer Android com Chrome suporta WebGL 1.0.

```
Pipeline de Rendering no Phaser 3:

[Objetos do jogo (GameObjects)]
          ↓
[Phaser WebGL Renderer]
          ↓
[Batching por textura — sprites com mesmo atlas = 1 draw call]
          ↓
[SpriteBatch pipeline — até 4096 sprites por batch]
          ↓
[WebGL Context → GPU → Display]
```

**Por que isso importa para 60fps:** O Samsung Galaxy A06 (Helio G85 com Mali-G57) aguenta WebGL sem problema. O gargalo não é GPU — é CPU. Cada draw call separada tem overhead de CPU. Manter tudo num atlas único significa que 200 zumbis em tela custam a mesma CPU que 1 zumbi.

### Arquitetura de Layers no Phaser

```
Scene: GameScene
├── Layer 0 — Background (profundidade fixa)
│   ├── Sky gradient (retângulo colorido — sem sprite)
│   └── Congresso silhueta (1 sprite estático, parallax lento)
│
├── Layer 1 — Tilemap / Ground
│   └── TilemapLayer — Esplanada (tileset único 512×512)
│
├── Layer 2 — Entities (y-sorted)
│   ├── Grupo "zombies" (Phaser.GameObjects.Group)
│   ├── Objeto "player" (Phaser.Physics.Arcade.Sprite)
│   └── Grupo "pickups" (pool de power-ups)
│
├── Layer 3 — Projectiles
│   └── Grupo "projectiles" (pool de press releases do Assessor)
│
├── Layer 4 — VFX
│   └── ParticleManager (emissores poolados)
│
├── Layer 5 — Onomatopeias (HIT!, SLAP!, THWACK!)
│   └── Grupo temporário com lifetime de 6 frames
│
└── HUD (câmera separada — sem scroll, sem parallax)
    ├── Timer, HP, Score, Combo
    └── Virtual joystick + botão de power-up
```

**Y-Sort:** O Phaser não faz y-sort automático. Implementar manualmente via `setDepth()` a cada frame no grupo de entidades:

```javascript
// GameScene.update() — chamado todo frame
this.entitiesGroup.getChildren().forEach(entity => {
    entity.setDepth(entity.y); // y maior = mais à frente na tela
});
```

Custo: O(n) por frame. Com n <= 100 entidades, irrelevante.

### Como Atingir 60fps com Centenas de Sprites

**Regra de ouro:** um atlas. Todos os sprites do jogo — player, zumbis, UI, VFX — em um único spritesheet de 2048×2048px. O Phaser faz batching automático por textura. Se tudo está no mesmo atlas, é literalmente uma draw call para o mundo inteiro.

| Estratégia | Impacto no FPS |
|---|---|
| Atlas único (todos os sprites) | +++ (batching máximo) |
| setDepth() em vez de containers aninhados | ++ (evita grupos pesados) |
| Object pooling (zumbis, projéteis, partículas) | +++ (sem GC no mid-game) |
| Desativar entidades fora do viewport | ++ (sem render overhead) |
| requestAnimationFrame nativo (Phaser usa por padrão) | +++ (sync com vsync do browser) |
| Desativar Physics debug em produção | + (óbvio, mas acontece) |

**Target de draw calls:** menos de 10 por frame. Um jogo bem batched com 150 zumbis em tela pode rodar em 3-4 draw calls.

---

## 2. Animation System Web

### Sprite Sheets no Browser: Implementação com Phaser

A lógica do plano original se mantém: sprite sheets, 12fps para personagens, frames expressivos em vez de interpolação suave. Isso é deliberado. O estilo André Guedes é de quadrinhos — frames discretos têm personalidade.

**Estrutura do atlas:**

```
zombie-atlas.png (2048×2048)
├── Linha 0-3:   player_idle (2 frames × 64×64)
├── Linha 4-9:   player_run (4 frames × 64×64)
├── Linha 10-13: player_attack (3 frames × 64×64)
├── Linha 14-15: player_hurt (2 frames × 64×64)
├── Linha 16-21: player_death (3 frames × 64×64)
├── Linha 22-27: vereador_walk (4 frames)
├── Linha 28-31: vereador_attack (2 frames)
├── Linha 32-35: vereador_death (4 frames)
│   ... (todos os zumbis no mesmo atlas)
└── Linha N:     VFX, onomatopeias, pickups
```

**Definição de animações no Phaser:**

```javascript
// src/anims/registerAnims.js
export function registerAllAnims(scene) {
    // Player
    scene.anims.create({
        key: 'player_idle',
        frames: scene.anims.generateFrameNames('atlas', {
            prefix: 'player_idle_', start: 0, end: 1
        }),
        frameRate: 6,
        repeat: -1
    });

    scene.anims.create({
        key: 'player_run',
        frames: scene.anims.generateFrameNames('atlas', {
            prefix: 'player_run_', start: 0, end: 3
        }),
        frameRate: 12,
        repeat: -1
    });

    scene.anims.create({
        key: 'player_attack',
        frames: scene.anims.generateFrameNames('atlas', {
            prefix: 'player_attack_', start: 0, end: 2
        }),
        frameRate: 24, // wind-up rápido — responsividade
        repeat: 0
    });

    scene.anims.create({
        key: 'player_hurt',
        frames: scene.anims.generateFrameNames('atlas', {
            prefix: 'player_hurt_', start: 0, end: 1
        }),
        frameRate: 12,
        repeat: 0
    });

    // Zumbi Vereador
    scene.anims.create({
        key: 'vereador_walk',
        frames: scene.anims.generateFrameNames('atlas', {
            prefix: 'vereador_walk_', start: 0, end: 3
        }),
        frameRate: 8, // mais lento que o player — arrastado, morto-vivo
        repeat: -1
    });

    // ... restante dos zumbis
}
```

### Frame Timing e Prioridade de Animações

O Godot tinha um sistema de prioridade explícito (`AnimPriority`). No Phaser, implementar equivalente:

```javascript
// src/entities/Player.js
class Player extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y) {
        super(scene, x, y, 'atlas', 'player_idle_0');
        this.animPriority = 0;
        // 0=idle, 1=move, 2=attack, 3=hurt, 4=death
    }

    playAnim(key, priority, force = false) {
        if (priority >= this.animPriority || force) {
            this.animPriority = priority;
            if (this.anims.currentAnim?.key !== key) {
                this.play(key);
            }
        }
    }

    // Callback: quando animação one-shot termina, prioridade cai
    onAnimComplete(anim) {
        if (['player_attack', 'player_hurt'].includes(anim.key)) {
            this.animPriority = 0;
        }
    }
}
```

### Efeitos de Animação: Hit Flash e Tint

No Godot era um `ShaderMaterial`. No browser, o equivalente é `setTint()` do Phaser (converte para WebGL tint nativo) ou um shader de fragmento simples via pipeline customizado.

**Abordagem pragmática para 2 semanas:** usar `setTint(0xffffff)` com `clearTint()` dois frames depois. Não é exatamente "flash branco puro" como um shader faria, mas a diferença é imperceptível durante gameplay a 60fps.

```javascript
// src/systems/CombatFeedback.js
flashWhite(sprite, durationMs = 33) { // 33ms ≈ 2 frames a 60fps
    sprite.setTintFill(0xffffff); // tint fill = substitui cor completamente
    this.scene.time.delayedCall(durationMs, () => {
        sprite.clearTint();
    });
}
```

### Frame Rates por Tipo de Animação (Adaptados para Web)

| Tipo | FPS | Implementação Web |
|---|---|---|
| Personagem idle/run | 12fps | `frameRate: 12` no Phaser |
| Ataque wind-up | 24fps | `frameRate: 24`, one-shot |
| Hit stop (congelamento) | Pausa no frame | `scene.time.timeScale = 0.05` por 50ms |
| Morte de zumbi | 12fps | One-shot + destroy após último frame |
| VFX de impacto | 24fps | Partículas com lifetime curto |
| UI transitions | 60fps | CSS transitions ou Phaser Tweens |

---

## 3. Input Dual — Teclado+Mouse (Desktop) + Touch (Mobile)

### Filosofia: Input Unificado em Vetor de Movimento

Tanto teclado quanto joystick virtual produzem o mesmo output: um `Vector2` de direção normalizado. O sistema de jogo não sabe se o input vem de teclado ou touch — só recebe `{ x: -0.7, y: 0.3, attacking: true }`.

```javascript
// src/input/InputManager.js
export class InputManager {
    constructor(scene) {
        this.scene = scene;
        this.direction = { x: 0, y: 0 };
        this.powerUp = false;

        // Desktop: cursors + WASD + Space
        this.cursors = scene.input.keyboard.createCursorKeys();
        this.wasd = scene.input.keyboard.addKeys({
            up: Phaser.Input.Keyboard.KeyCodes.W,
            down: Phaser.Input.Keyboard.KeyCodes.S,
            left: Phaser.Input.Keyboard.KeyCodes.A,
            right: Phaser.Input.Keyboard.KeyCodes.D,
            powerUp: Phaser.Input.Keyboard.KeyCodes.SPACE
        });

        // Mobile: joystick virtual
        this.joystick = new VirtualJoystick(scene);

        // Detecta modo de input predominante
        this.mode = 'keyboard'; // 'keyboard' ou 'touch'
        scene.input.on('pointerdown', () => { this.mode = 'touch'; });
        scene.input.keyboard.on('keydown', () => { this.mode = 'keyboard'; });
    }

    update() {
        if (this.mode === 'keyboard') {
            this._updateKeyboard();
        } else {
            this._updateTouch();
        }
    }

    _updateKeyboard() {
        let dx = 0, dy = 0;

        if (this.cursors.left.isDown || this.wasd.left.isDown) dx -= 1;
        if (this.cursors.right.isDown || this.wasd.right.isDown) dx += 1;
        if (this.cursors.up.isDown || this.wasd.up.isDown) dy -= 1;
        if (this.cursors.down.isDown || this.wasd.down.isDown) dy += 1;

        // Normaliza diagonal (evita movimento 41% mais rápido na diagonal)
        const len = Math.sqrt(dx * dx + dy * dy);
        this.direction = len > 0
            ? { x: dx / len, y: dy / len }
            : { x: 0, y: 0 };

        this.powerUp = Phaser.Input.Keyboard.JustDown(this.wasd.powerUp);
    }

    _updateTouch() {
        this.direction = this.joystick.direction; // { x, y } normalizado
        this.powerUp = this.joystick.powerUpPressed;
    }
}
```

### Virtual Joystick — Implementação Web

O comportamento do joystick dinâmico do plano original se mantém integralmente. A diferença é que usamos eventos de `pointer` do Phaser em vez de `InputEventScreenDrag` do Godot.

```javascript
// src/input/VirtualJoystick.js
export class VirtualJoystick {
    constructor(scene) {
        this.scene = scene;
        this.direction = { x: 0, y: 0 };
        this.powerUpPressed = false;

        this.DEAD_ZONE = 8;     // pixels mínimos para registrar movimento
        this.MAX_RADIUS = 60;   // raio máximo do joystick (pixels)
        this.HALF_W = scene.scale.width / 2;

        this.activePointerId = null;
        this.originX = 0;
        this.originY = 0;

        // Sprites do joystick (no HUD, câmera fixa)
        this.outerRing = scene.add.image(0, 0, 'atlas', 'joystick_outer')
            .setAlpha(0).setScrollFactor(0).setDepth(100);
        this.innerDot = scene.add.image(0, 0, 'atlas', 'joystick_inner')
            .setAlpha(0).setScrollFactor(0).setDepth(101);

        this._bindEvents();
    }

    _bindEvents() {
        const input = this.scene.input;

        input.on('pointerdown', (ptr) => {
            // Metade ESQUERDA da tela = joystick zone
            if (ptr.x > this.HALF_W) return;
            if (this.activePointerId !== null) return; // já tem joystick ativo

            this.activePointerId = ptr.id;
            this.originX = ptr.x;
            this.originY = ptr.y;
            this._showAt(ptr.x, ptr.y);
        });

        input.on('pointermove', (ptr) => {
            if (ptr.id !== this.activePointerId) return;
            this._updateDirection(ptr.x, ptr.y);
        });

        input.on('pointerup', (ptr) => {
            if (ptr.id !== this.activePointerId) return;
            this._release();
        });

        // Metade DIREITA = botão de power-up (toque simples)
        input.on('pointerdown', (ptr) => {
            if (ptr.x <= this.HALF_W) return;
            this.powerUpPressed = true;
        });
        input.on('pointerup', (ptr) => {
            if (ptr.x <= this.HALF_W) return;
            this.powerUpPressed = false;
        });
    }

    _updateDirection(px, py) {
        const dx = px - this.originX;
        const dy = py - this.originY;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < this.DEAD_ZONE) {
            this.direction = { x: 0, y: 0 };
            this.innerDot.setPosition(this.originX, this.originY);
            return;
        }

        const norm = { x: dx / dist, y: dy / dist };
        this.direction = norm;

        const clampedDist = Math.min(dist, this.MAX_RADIUS);
        this.innerDot.setPosition(
            this.originX + norm.x * clampedDist,
            this.originY + norm.y * clampedDist
        );
    }

    _showAt(x, y) {
        this.outerRing.setPosition(x, y).setAlpha(0);
        this.innerDot.setPosition(x, y).setAlpha(0);
        this.scene.tweens.add({
            targets: [this.outerRing, this.innerDot],
            alpha: { from: 0, to: 1 },
            duration: 80 // fade-in suave, não pop
        });
    }

    _release() {
        this.activePointerId = null;
        this.direction = { x: 0, y: 0 };
        this.scene.tweens.add({
            targets: [this.outerRing, this.innerDot],
            alpha: 0,
            duration: 100,
        });
    }
}
```

### Ataque Automático (decisão do André Guedes)

O André Guedes tomou a decisão de ataque automático — o cidadão ataca o zumbi mais próximo sem input explícito. Isso simplifica os controles mobile e reduz desenvolvimento. Para o game feel, o risco é o combate parecer passivo. A solução é: animação de ataque clara, som imediato, e feedback visual forte em cada hit. O jogador não clica para atacar, mas SENTE cada golpe.

```javascript
// src/systems/AutoAttack.js — executado no update do player
update(player, zombiesGroup, time) {
    if (time < player.nextAttackTime) return;

    const nearest = this._findNearest(player, zombiesGroup);
    if (!nearest) return;

    const dist = Phaser.Math.Distance.Between(
        player.x, player.y, nearest.x, nearest.y
    );
    if (dist > player.attackRange) return;

    // Executa ataque
    player.playAnim('player_attack', 2);
    player.flipX = nearest.x < player.x; // vira para o inimigo
    player.nextAttackTime = time + player.attackCooldown;

    // Dispara evento de hit para o CombatSystem processar
    this.scene.events.emit('playerHit', nearest, player.x, player.y);
}

_findNearest(player, group) {
    let nearest = null;
    let minDist = Infinity;

    group.getChildren().forEach(zombie => {
        if (!zombie.active) return;
        const d = Phaser.Math.Distance.Between(player.x, player.y, zombie.x, zombie.y);
        if (d < minDist) {
            minDist = d;
            nearest = zombie;
        }
    });

    return nearest;
}
```

### Input Buffering para Ativação de Power-up

O power-up não é automático — requer input explícito (botão direito no mobile, Espaço no desktop). Implementar buffer de 6 frames para tolerância de timing:

```javascript
// src/input/InputManager.js — dentro da classe
updatePowerUpBuffer() {
    if (this.powerUp) {
        this._powerUpBuffer = 6; // 6 frames ≈ 100ms a 60fps
    }
    if (this._powerUpBuffer > 0) {
        this._powerUpBuffer--;
        if (this.scene.powerUpSystem.canActivate()) {
            this.scene.powerUpSystem.activate();
            this._powerUpBuffer = 0;
        }
    }
}
```

---

## 4. Combat Feel no Browser

### A Anatomia de um Kill — Sequência Exata

O hit stop é a peça mais crítica. 3 frames de "mundo congelado" (50ms) são imperceptíveis como tempo, mas registram como peso físico. O cérebro não percebe a pausa — percebe o impacto.

```javascript
// src/systems/CombatSystem.js
processHit(target, attackerX, attackerY, weaponData) {
    const isCrit = Math.random() < this.scene.gameState.critChance;

    // 1. HIT STOP — desacelera o tempo do jogo
    this._applyHitStop(isCrit ? 4 : 3);

    // 2. HIT FLASH — sprite branco por 2 frames
    this.feedback.flashWhite(target.sprite, 33);

    // 3. SFX imediato (não espera hit stop)
    this.audio.playSFX(weaponData.sfxHit, { pitch: 0.9 + Math.random() * 0.2 });

    // 4. Knockback
    const angle = Phaser.Math.Angle.Between(attackerX, attackerY, target.x, target.y);
    target.body.velocity.x = Math.cos(angle) * weaponData.knockback;
    target.body.velocity.y = Math.sin(angle) * weaponData.knockback;

    // 5. Damage number popup (objeto do pool)
    this.damageNumbers.spawn(target.x, target.y - 20, weaponData.damage, isCrit);

    // 6. Onomatopeia visual (SLAP!, THWACK!, INDEFERIDO!)
    this.onomatopeias.spawn(target.x, target.y, weaponData.id);

    // 7. Screen shake via câmera
    this.scene.cameras.main.shake(
        isCrit ? 80 : 50,        // duração (ms)
        isCrit ? 0.006 : 0.003   // intensidade
    );

    // 8. Vibração haptic no mobile
    if (navigator.vibrate) {
        navigator.vibrate(isCrit ? 30 : 15);
    }

    // Aplica dano depois de toda a apresentação visual
    target.takeDamage(weaponData.damage);
}

_applyHitStop(frames) {
    const duration = (frames / 60) * 1000; // frames → ms
    this.scene.time.timeScale = 0.05; // quase congelado
    this.scene.time.delayedCall(duration, () => {
        this.scene.time.timeScale = 1.0;
    });
    // NOTA: o time.delayedCall usa tempo real (ignora timeScale)
    // O Phaser usa timers em ms reais, não em frames — funciona perfeitamente
}
```

### Screen Shake no Phaser

O Phaser tem `cameras.main.shake()` nativo. Diferente do Godot (onde implementamos o trauma manualmente), no Phaser é uma linha:

```javascript
// Parâmetros: shake(duração ms, intensidade 0-1)
this.scene.cameras.main.shake(50, 0.003);  // hit normal
this.scene.cameras.main.shake(80, 0.006);  // hit crítico
this.scene.cameras.main.shake(120, 0.01);  // boss hit
this.scene.cameras.main.shake(300, 0.02);  // boss kill
this.scene.cameras.main.shake(400, 0.025); // explosão de urna
```

O `cameras.main.shake()` já usa interpolação quadrática internamente. A intensidade do Phaser é diferente da escala do Godot, mas o efeito é equivalente.

### Particles no Browser

O Phaser tem um sistema de partículas WebGL nativo. Para 60fps mobile, o budget é mais apertado que no Godot (sem GPU dedicada móvel):

```javascript
// src/systems/ParticleSystem.js
class ParticleSystem {
    constructor(scene) {
        this.scene = scene;

        // Cria emissores pré-configurados por tipo
        this.emitters = {
            hitDust: this._createHitDustEmitter(),
            zombieDeath: this._createZombieDeathEmitter(),
            bloodSplat: this._createBloodSplatEmitter(),
            confetti: this._createConfettiEmitter(), // boss kill
            pressRelease: this._createPressReleaseEmitter(), // Assessor morte
        };
    }

    _createHitDustEmitter() {
        return this.scene.add.particles(0, 0, 'atlas', {
            frame: 'particle_dust',
            lifespan: 400,
            speed: { min: 30, max: 80 },
            scale: { start: 0.8, end: 0 },
            quantity: 5,           // por explosão
            maxParticles: 30,      // pool máximo — não cria mais que isso
            emitting: false        // apenas sob demanda
        });
    }

    spawnHit(x, y) {
        this.emitters.hitDust.setPosition(x, y);
        this.emitters.hitDust.explode(5); // burst de 5 partículas
    }

    spawnZombieDeath(x, y, type) {
        const count = { vereador: 8, assessor: 12, senador: 15, banqueiro: 18 };
        this.emitters.zombieDeath.setPosition(x, y);
        this.emitters.zombieDeath.explode(count[type] || 8);
    }
}
```

**Budget de partículas para 60fps mobile:**

| Tipo | Partículas por evento | Simultâneas máx | Lifetime |
|---|---|---|---|
| Hit dust | 5 | 40 | 400ms |
| Morte vereador | 8 | 30 | 600ms |
| Morte senador | 15 | 20 | 800ms |
| Morte boss | 50 (one-shot) | 50 | 2000ms |
| Press releases (Assessor) | 8 papéis | 20 | 1200ms |
| Power-up brilho (loop) | 3 contínuos | 15 | loop |
| **Total simultâneo máx** | | **~175** | |

**175 partículas simultâneas** é conservador o suficiente para manter 60fps no A06 via browser.

### Damage Numbers — Pool de Objetos

```javascript
// src/ui/DamageNumberPool.js
export class DamageNumberPool {
    constructor(scene, maxSize = 20) {
        this.scene = scene;
        this.pool = [];

        // Pré-aloca
        for (let i = 0; i < maxSize; i++) {
            const text = scene.add.text(0, 0, '', {
                fontSize: '20px',
                fontFamily: 'Bebas Neue',
                color: '#ffffff',
                stroke: '#000000',
                strokeThickness: 3
            }).setVisible(false).setScrollFactor(1).setDepth(50);
            this.pool.push(text);
        }
    }

    spawn(x, y, damage, isCrit) {
        const text = this.pool.find(t => !t.visible);
        if (!text) return; // pool cheio — descarta (melhor que criar novo objeto)

        text.setText(isCrit ? `${damage}!` : `${damage}`);
        text.setFontSize(isCrit ? 28 : 20);
        text.setColor(isCrit ? '#FFD700' : '#ffffff');
        text.setPosition(x, y).setVisible(true).setAlpha(1);

        // Animação: sobe e desaparece
        this.scene.tweens.add({
            targets: text,
            y: y - 40,
            alpha: 0,
            duration: 600,
            ease: 'Power2',
            onComplete: () => text.setVisible(false)
        });
    }
}
```

---

## 5. Audio Web — Web Audio API e Restrições de Autoplay

### O Problema de Autoplay no Mobile Browser

**Regra de ouro do audio mobile no browser:** o browser NÃO vai tocar áudio sem que o usuário tenha interagido com a página primeiro. Nenhum evento de toque ainda = nenhum som. Isso é uma restrição do browser (desde Chrome 66, iOS Safari desde sempre), não um bug do jogo.

**Solução:** usar a primeira interação do jogador (toque na tela de "escolher tom de pele" ou "jogar") para desbloquear o AudioContext.

```javascript
// src/audio/AudioUnlocker.js
export class AudioUnlocker {
    constructor(game) {
        this.unlocked = false;
        this.game = game;

        // Phaser tenta desbloquear automaticamente no primeiro toque
        // Mas em iOS Safari precisa de handling manual
        if (game.sound.locked) {
            game.sound.once('unlocked', () => {
                this.unlocked = true;
                this._onUnlocked();
            });
        } else {
            this.unlocked = true;
        }
    }

    _onUnlocked() {
        // Toca um som silencioso para "aquecer" o AudioContext
        this.game.sound.play('silence');
        console.log('[Audio] Context unlocked — full audio enabled');
    }
}
```

**No fluxo do jogo:** a tela de seleção de skin (primeira tela depois do loading) serve como "unlock screen" implícita. O jogador toca para escolher o tom de pele → audio context desbloqueado → jogo começa com som.

### Arquitetura de Audio no Phaser

```javascript
// src/audio/AudioManager.js
export class AudioManager {
    constructor(scene) {
        this.scene = scene;
        this.MAX_CONCURRENT_SFX = 8;
        this.MAX_COMBAT_SFX = 4;
        this.activeCount = 0;

        // Volumes por categoria (0-1)
        this.volumes = {
            music: 0.6,
            sfxCombat: 0.8,
            sfxUI: 0.9,
            sfxAmbient: 0.3
        };
    }

    playSFX(key, options = {}) {
        if (this.activeCount >= this.MAX_CONCURRENT_SFX) return;

        this.activeCount++;
        const sound = this.scene.sound.add(key, {
            volume: (options.volume || 1.0) * this.volumes.sfxCombat,
        });

        if (options.pitch) {
            // Web Audio API suporta detune: 100 cents = 1 semitom
            sound.setDetune((options.pitch - 1) * 1200);
        }

        sound.once('complete', () => {
            this.activeCount--;
            sound.destroy();
        });

        sound.play();
    }

    playMusic(key, loop = true) {
        // Para música anterior com fade
        if (this._currentMusic) {
            this.scene.tweens.add({
                targets: this._currentMusic,
                volume: 0,
                duration: 500,
                onComplete: () => this._currentMusic.destroy()
            });
        }

        this._currentMusic = this.scene.sound.add(key, {
            volume: 0,
            loop
        });
        this._currentMusic.play();

        this.scene.tweens.add({
            targets: this._currentMusic,
            volume: this.volumes.music,
            duration: 500
        });
    }

    setMasterMute(muted) {
        this.scene.sound.mute = muted;
        // Salva preferência no localStorage
        localStorage.setItem('zombies_muted', muted ? '1' : '0');
    }
}
```

### Como Lidar com Mute no Mobile

Em mobile, o usuário frequentemente quer jogar sem som (ônibus, reunião, banheiro). Implementar botão de mute visível e persistente:

- Botão de mute/unmute no HUD (canto superior esquerdo — longe do botão de power-up)
- Estado salvo em `localStorage` — jogo lembra da preferência entre sessões
- Ícone claro: speaker com X quando mudo
- **Não usar o botão físico de volume para controle de mute do jogo** — é comportamento inesperado

### Formatos de Audio: OGG + MP3 Fallback

```javascript
// Phaser carrega automaticamente o formato suportado
this.load.audio('hit_vassoura', [
    'assets/audio/hit_vassoura.ogg',  // Chrome, Firefox, Android
    'assets/audio/hit_vassoura.mp3'   // iOS Safari (não suporta OGG)
]);
```

**OGG Vorbis** é o formato principal (melhor qualidade/tamanho). **MP3** como fallback obrigatório para iOS Safari.

### Budget de Audio (< 5MB total)

| Asset | Formato | Tamanho estimado |
|---|---|---|
| Música gameplay (1:30 loop) | OGG 96kbps | ~1.1MB |
| Música boss (0:45 loop) | OGG 96kbps | ~0.5MB |
| SFX combate (20 sons) | OGG 64kbps curtos | ~0.8MB |
| SFX ambiente (4 loops) | OGG 64kbps | ~0.6MB |
| Falas dos zumbis (síntese) | OGG 64kbps | ~0.5MB |
| **Total** | | **~3.5MB** |

Budget restante de 1.5MB para contingência. Sprites + código ficam em separado.

---

## 6. Performance Mobile Browser

### RequestAnimationFrame e o Loop do Phaser

O Phaser usa `requestAnimationFrame` nativo, que já está sincronizado com o vsync do display. Isso é o equivalente exato ao `_physics_process` do Godot — o browser chama o callback quando é hora de renderizar o próximo frame.

**Diferença crítica do Godot:** No browser, o frame rate não é garantido. Se o tab perde foco, o `requestAnimationFrame` é pausado pelo browser (comportamento correto — não processa jogo em background). Se o device sofre throttling térmico, os frames ficam mais longos.

**Solução:** usar `delta time` em todas as movimentações. Nunca mover por "pixels por frame" — sempre "pixels por segundo × delta".

```javascript
// ERRADO — velocidade varia com o FPS
player.x += 5;

// CORRETO — velocidade constante independente do FPS
// O Phaser passa delta em ms para update()
player.x += (player.speed * delta) / 1000;

// Ou usando a física do Phaser (recomendado)
player.body.velocity.x = player.speed; // pixels/segundo automático
```

### Object Pooling — Implementação

O maior inimigo do 60fps em JavaScript é o Garbage Collector. Criar e destruir objetos durante gameplay causa GC pauses que dropam frames. A solução é criar todos os objetos antes do jogo começar e reutilizá-los.

```javascript
// src/pools/ZombiePool.js
export class ZombiePool {
    constructor(scene, type, maxSize) {
        this.scene = scene;
        this.type = type;

        // Cria e desativa todos os objetos ANTES da gameplay
        this.group = scene.physics.add.group({
            classType: ZombieFactory.getClass(type),
            maxSize,
            runChildUpdate: true,
            createMultiple: {
                quantity: maxSize,
                key: 'atlas',
                frame: ZombieFactory.getIdleFrame(type),
                active: false,
                visible: false
            }
        });
    }

    spawn(x, y) {
        const zombie = this.group.get(x, y);
        if (!zombie) return null; // pool esgotado

        zombie.setActive(true).setVisible(true);
        zombie.init(x, y); // reset de estado (HP, velocidade, etc)
        return zombie;
    }

    release(zombie) {
        zombie.setActive(false).setVisible(false);
        zombie.body.stop();
        // Objeto volta ao pool — não é destruído, não há GC
    }
}
```

**Pools necessários para o MVP:**

| Pool | Tamanho | Justificativa |
|---|---|---|
| VereadorZombie | 40 | Horda básica — muitos simultâneos |
| AssessorZombie | 15 | Atirador — menos frequente |
| SenadorZombie | 8 | Tank — raro, lento |
| BanqueiroZombie | 5 | Elite — muito raro |
| Boss | 1 | Apenas 1 simultâneo |
| Projectile (press releases) | 30 | Do Assessor |
| DamageNumber | 20 | (já implementado acima) |
| ParticleEmitter | 10 | Reuso de emissores |

### Gerenciamento de Garbage Collection

Regras para não criar lixo durante gameplay:

```javascript
// ERRADO — cria objeto novo a cada frame
update() {
    const pos = { x: this.x, y: this.y }; // GC bait
    checkCollision(pos);
}

// CORRETO — objeto reutilizado
constructor() {
    this._tempPos = { x: 0, y: 0 }; // criado uma vez
}
update() {
    this._tempPos.x = this.x;
    this._tempPos.y = this.y;
    checkCollision(this._tempPos);
}
```

**Outras regras:**
- Nunca usar `Array.filter()`, `Array.map()`, ou `Array.reduce()` no loop principal — criam arrays novos
- Usar `for` loop clássico com índice numérico em código crítico de performance
- Strings de animação como constantes, nunca como template literals no update
- Eventos: usar `on()` no `create()`, nunca criar novos listeners no `update()`

### Profiling no Chrome DevTools

Como verificar se está no budget de 60fps em um device real:

1. Chrome em Android → Configurações → Ativar depuração USB
2. Abrir `chrome://inspect` no desktop
3. Aba Performance → gravar 5 segundos de gameplay intenso
4. Verificar:
   - **Frame time:** deve ser < 16.6ms por frame consistentemente
   - **Scripting:** < 8ms por frame (metade do budget)
   - **Rendering:** < 4ms por frame
   - **GC pauses:** nenhum GC durante gameplay ativo

**Target mobile:** Samsung Galaxy A06 (Helio G85) rodando Chrome 124+. Testar com `chrome://flags#enable-gpu-rasterization` ativado.

---

## 7. Os 4+1 Zumbis no Browser — Specs de Animação e VFX

### Zumbi #1 — O Vereador-Zumbi (Horda Básica)

**Spritesheet:** 4 frames de caminhada (8fps) + 2 frames de ataque + 4 frames de morte.

```javascript
// Configuração no Phaser
anims.create({ key: 'vereador_walk', frameRate: 8, repeat: -1 });
anims.create({ key: 'vereador_attack', frameRate: 12, repeat: 0 });
anims.create({ key: 'vereador_death', frameRate: 10, repeat: 0 });
```

**VFX ao morrer:**
- Burst de 8 partículas de "pó político" (cinza-esverdeado)
- Onomatopeia "SLAP!" ou "VOTO!" por 6 frames
- Drop de moeda pequena (10% chance de power-up)
- Frase de morte via `scene.add.text()` com lifetime de 2s: "FUI ELEITO DEMOCRATICAMEEENTE!"

**Comportamento:** movimento linear em direção ao player, sem pathfinding. A 60fps com arcade physics do Phaser, 40 vereadores simultâneos são triviais.

### Zumbi #2 — O Assessor de Fake News (Atirador)

**Spritesheet:** 4 frames de caminhada lateral (8fps) + 3 frames de arremesso + 3 frames de morte.

**Projétil — Manchete:** sprite de papel com texto gerado dinamicamente.

```javascript
// Cria manchete como texto + retângulo (sem sprite de arte necessário)
spawnHeadline(x, y, angle) {
    const headlines = [
        "CIDADÃO SUSPEITO DE TER OPINIÃO",
        "IA GERA IMAGEM DE POLÍTICO HONESTO — SISTEMA TRAVA",
        "FONTE ANÔNIMA CONFIRMA QUE FONTES ANÔNIMAS MENTEM",
        "DATAFOLHA MOSTRA QUE NINGUÉM SABE DE NADA",
    ];

    const text = this.scene.add.text(x, y,
        headlines[Math.floor(Math.random() * headlines.length)],
        { fontSize: '10px', fontFamily: 'Arial', color: '#111111',
          backgroundColor: '#ffffcc', padding: { x: 4, y: 2 } }
    );

    // Rotação e movimento via tweens
    this.scene.tweens.add({
        targets: text,
        x: x + Math.cos(angle) * 400,
        y: y + Math.sin(angle) * 400,
        rotation: 0.3,
        duration: 1500,
        onComplete: () => text.destroy()
    });
}
```

**VFX ao morrer:** burst de "press releases" (papéis voando) — 8 partículas de sprite de papel.

### Zumbi #3 — O Senador Blindado (Tank)

**Spritesheet:** 3 frames de caminhada lenta (6fps) + escudo visível como sprite separado + 4 frames de morte lenta.

**Escudo de Imunidade Parlamentar:**

```javascript
class SenadorZombie extends BaseZombie {
    constructor(scene, x, y) {
        super(scene, x, y, 'senador');
        this.shieldHits = 3;
        this.shield = scene.add.image(x, y, 'atlas', 'senador_shield')
            .setAlpha(0.7).setTint(0xffd700); // dourado semi-transparente
    }

    takeDamage(amount) {
        if (this.shieldHits > 0) {
            this.shieldHits--;

            // VFX: flash dourado + texto de imunidade
            this.scene.cameras.main.shake(30, 0.002);
            this._spawnImmunityText();

            // Ao quebrar o escudo: efeito especial
            if (this.shieldHits === 0) {
                this._breakShield();
            }
            return; // dano ignorado enquanto escudo ativo
        }
        super.takeDamage(amount);
    }

    _breakShield() {
        // Chuva de moedas (emenda parlamentar caindo)
        this.scene.particles.spawnCoins(this.x, this.y, 12);
        this.scene.sound.play('sfx_shield_break');
        this.scene.cameras.main.shake(150, 0.008);

        this.scene.tweens.add({
            targets: this.shield,
            scaleX: 0, scaleY: 0, alpha: 0,
            duration: 200,
            onComplete: () => this.shield.destroy()
        });
    }

    _spawnImmunityText() {
        const texts = ["IMUNIDADE!", "FORO PRIVILEGIADO!", "RECURSO EM ANDAMENTO!"];
        const t = this.scene.add.text(
            this.x, this.y - 30,
            texts[Math.floor(Math.random() * texts.length)],
            { fontSize: '12px', fontFamily: 'Bebas Neue', color: '#ffd700',
              stroke: '#000', strokeThickness: 2 }
        );
        this.scene.tweens.add({
            targets: t, y: t.y - 20, alpha: 0,
            duration: 800, onComplete: () => t.destroy()
        });
    }
}
```

### Zumbi #4 — O Banqueiro-Zumbi (Elite/Raro)

**O zumbi mais interessante em termos de game feel.** Não ataca diretamente — corrompe outros zumbis ao redor, dando a eles aura dourada e 2x velocidade/resistência.

```javascript
class BanqueiroZombie extends BaseZombie {
    constructor(scene, x, y) {
        super(scene, x, y, 'banqueiro');
        this.corruptRadius = 150; // pixels
        this.corruptCooldown = 3000; // ms entre corrupções
        this.nextCorrupt = 0;

        // Notas de dinheiro voando — partículas contínuas
        this._setupMoneyParticles();
    }

    update(time, delta) {
        super.update(time, delta);

        if (time > this.nextCorrupt) {
            this._corruptNearbyZombies();
            this.nextCorrupt = time + this.corruptCooldown;
        }
    }

    _corruptNearbyZombies() {
        const zombies = this.scene.zombieGroups.getAll();
        zombies.forEach(zombie => {
            if (zombie === this) return;
            const dist = Phaser.Math.Distance.Between(
                this.x, this.y, zombie.x, zombie.y
            );
            if (dist > this.corruptRadius) return;

            zombie.setCorrupted(true); // aura dourada, 2x stats por 5s
            this.scene.particles.spawnMoneyBurst(zombie.x, zombie.y);
        });

        this.scene.sound.play('sfx_corrupcao');
    }
}
```

**VFX ao morrer:** celular cai no chão → "abre" mostrando lista de contatos com emojis de coração → particulas de notas de dinheiro espalhando. Drop especial: "Delação Premiada".

### Boss — O Candidato Eterno

**Escala:** 3× o tamanho dos sprites normais (via `setScale(3)`). Custo de rendering = 1 sprite. Sem impacto no performance.

**Onda sônica de discurso:** implementada como retângulo semi-transparente expandindo da boca do boss + physics overlap com o player.

```javascript
_spawnDiscursoWave() {
    // Anel de "onda sonora" visual
    const wave = this.scene.add.circle(this.x, this.y, 10,
        0xffff00, 0.3);

    this.scene.tweens.add({
        targets: wave,
        scaleX: 15, scaleY: 5,
        alpha: 0,
        duration: 600,
        onComplete: () => wave.destroy()
    });

    // Knockback no player se na área
    const dist = Phaser.Math.Distance.Between(
        this.x, this.y,
        this.scene.player.x, this.scene.player.y
    );
    if (dist < 150) {
        const angle = Phaser.Math.Angle.Between(
            this.x, this.y,
            this.scene.player.x, this.scene.player.y
        );
        this.scene.player.body.velocity.x = Math.cos(angle) * 300;
        this.scene.player.body.velocity.y = Math.sin(angle) * 300;
    }

    this.scene.sound.play('sfx_discurso');
}
```

**"Segundo Turno" (ressurreição com 25% HP):**

```javascript
die() {
    if (!this.hasRevived) {
        this.hasRevived = true;
        this.hp = this.maxHp * 0.25;

        // Jingle distorcido + texto dramático
        this.scene.sound.play('sfx_segundo_turno');
        this.scene.cameras.main.shake(500, 0.015);

        const text = this.scene.add.text(
            this.scene.scale.width / 2,
            this.scene.scale.height / 2,
            'VOLTO EM 4 ANOS!',
            { fontSize: '48px', fontFamily: 'Bebas Neue',
              color: '#ff0000', stroke: '#ffffff', strokeThickness: 4 }
        ).setOrigin(0.5).setScrollFactor(0).setDepth(200);

        this.scene.tweens.add({
            targets: text,
            scaleX: 1.3, scaleY: 1.3, alpha: 0,
            duration: 1500,
            onComplete: () => text.destroy()
        });
        return; // não morre — revive
    }

    // Morte definitiva
    super.die();
    this._spawnFinalDeathVFX();
}

_spawnFinalDeathVFX() {
    // Chuva de santinhos
    this.scene.particles.spawnConfetti(this.x, this.y, 60);
    this.scene.cameras.main.shake(400, 0.025);

    const text = this.scene.add.text(
        this.scene.scale.width / 2,
        this.scene.scale.height / 2,
        'CANDIDATO ETERNO — 0 VOTOS',
        { fontSize: '36px', fontFamily: 'Bebas Neue',
          color: '#ffffff', stroke: '#000000', strokeThickness: 4 }
    ).setOrigin(0.5).setScrollFactor(0).setDepth(200);

    this.scene.time.delayedCall(3000, () => text.destroy());
}
```

---

## 8. Lista Priorizada de Implementação — 10 Dias Úteis

Esta é a ordem exata. Cada item deve estar funcionando antes do próximo começar. Não há "implementação paralela" de mecânicas dependentes.

### Dia 1 — Fundação (Dia 1 de 10)

**Objetivo:** jogador se movendo na tela, teclas e touch funcionando.

- [ ] Setup do projeto Phaser 3 + TypeScript (opcional) + Vite como bundler
- [ ] Estrutura de pastas: `src/scenes/`, `src/entities/`, `src/systems/`, `src/input/`, `src/pools/`, `src/audio/`, `src/ui/`
- [ ] `BootScene` — carrega assets, mostra loading bar
- [ ] `GameScene` — cena principal vazia
- [ ] `InputManager` — teclado (WASD + setas) funcionando
- [ ] Sprite do player se movendo com física arcade
- [ ] Camera seguindo o player com lerp suave
- [ ] Deploy no Vercel (CI/CD configurado — cada push atualiza o link de teste)

**Critério de done:** abrir no celular, tocar o link, ver o player se mover.

### Dia 2 — Input Mobile e Inimigos Básicos

**Objetivo:** joystick virtual funcionando, primeiro zumbi perseguindo.

- [ ] `VirtualJoystick` — metade esquerda da tela
- [ ] Botão de power-up — metade direita (placeholder visual)
- [ ] `ZombiePool` para Vereador (20 instâncias)
- [ ] Vereador spawna, persegue o player, colide
- [ ] Flip horizontal do sprite baseado na direção de movimento
- [ ] Y-sort básico (`setDepth(y)`)

**Critério de done:** jogar no celular com joystick, vereador perseguindo.

### Dia 3 — Combate e Game Feel Core

**Objetivo:** matar zumbis com satisfação.

- [ ] `AutoAttack` — ataque automático no zumbi mais próximo no range
- [ ] `CombatSystem.processHit()` completo: hit stop, flash branco, knockback
- [ ] Screen shake via `cameras.main.shake()`
- [ ] Animação de ataque do player
- [ ] Animação de morte do zumbi (one-shot) → release para pool
- [ ] SFX de hit (placeholder: 1 som de impacto)
- [ ] `DamageNumberPool` — números subindo ao acertar

**Critério de done:** matar um vereador e SENTIR. Se não houver weight no hit, o dia não acabou.

### Dia 4 — Sistema de Waves e HUD Básico

**Objetivo:** progressão de dificuldade nos 3 minutos.

- [ ] `WaveManager` — 6 waves em 3 minutos, spawn em ritmo crescente
- [ ] Timer de 3 minutos no HUD (conta regressiva)
- [ ] HP do player (3-5 corações) no HUD
- [ ] Score no HUD com bounce animation a cada kill
- [ ] `ComboSystem` — multiplicador × 2, × 3, × 5, × 10 por kills rápidos
- [ ] Texto de combo no HUD

**Critério de done:** jogar 3 minutos, ver dificuldade crescer, morrer (ou sobreviver).

### Dia 5 — Os 4 Zumbis Completos

**Objetivo:** todos os zumbis MVP implementados e funcionando.

- [ ] `AssessorZombie` — lógica de ficar à distância + projetar manchetes
- [ ] `SenadorZombie` — escudo, imunidade, quebra do escudo com VFX
- [ ] `BanqueiroZombie` — radius de corrupção, aura dourada nos corrompidos
- [ ] Pools para todos os 3 novos tipos
- [ ] WaveManager atualizado para spawnar mix de zumbis por wave

**Critério de done:** wave 4 com Banqueiro corrompendo Vereadores — caos legível, não poluição visual.

### Dia 6 — Power-ups e Boss

**Objetivo:** power-ups funcionando, boss com segunda fase.

- [ ] 5 power-ups implementados: Chinelo Voador, Urna Eletrônica, Café, Carimbo do INSS, Delação Premiada
- [ ] `PowerUpSystem` — drop de zumbis, coleta, ativação, timer visual
- [ ] `BossZombie` — spawn a cada 60s ou wave 5+
- [ ] Boss: onda sônica, hitpoints alto, segunda fase ("VOLTO EM 4 ANOS!")
- [ ] VFX de morte do boss (confetti + texto dramático)

**Critério de done:** primeiro playthrough completo de 3 minutos com boss.

### Dia 7 — Tela de Game Over e Compartilhamento

**Objetivo:** a feature mais importante do jogo (dixit André Guedes).

- [ ] `GameOverScene` — tela de resultado com título político
- [ ] Cálculo de título baseado em score (6 faixas)
- [ ] Frases de Game Over randomizadas (50+ frases carregadas de JSON)
- [ ] Card de compartilhamento via `canvas.toDataURL()` → PNG
- [ ] Web Share API (`navigator.share()`) com fallback para clipboard
- [ ] Botões: "JOGAR DE NOVO" e "COMPARTILHAR"
- [ ] Seleção de skin (3 tons de pele) na tela de início

**Critério de done:** jogar, morrer, compartilhar no WhatsApp. Link abre no browser. Funciona.

### Dia 8 — Polimento Visual e Audio Completo

**Objetivo:** som e visual com qualidade de lançamento.

- [ ] `AudioManager` completo: desbloqueio de audiocontext, fade entre músicas
- [ ] Todos os SFX integrados: hits, mortes, power-ups, boss
- [ ] Botão de mute persistente (localStorage)
- [ ] Partículas calibradas para 60fps mobile (ajustar budget conforme testes)
- [ ] Onomatopeias visuais implementadas (SLAP!, THWACK!, etc)
- [ ] Background parallax (Congresso ao fundo, movimento lento)
- [ ] Telas de início e Game Over com arte final

**Critério de done:** jogar 10 partidas ouvindo. O som deve dar peso a cada hit.

### Dia 9 — QA Mobile e Responsividade

**Objetivo:** funciona em todos os targets de device.

- [ ] Teste no Samsung Galaxy A06 (Helio G85) — 60fps confirmado
- [ ] Teste no Motorola G (device low-end de R$ 800)
- [ ] Teste no iPhone SE (iOS Safari — menor screen)
- [ ] Teste no iPad / tablet (landscape mode)
- [ ] Teste no Chrome Desktop (Windows + Mac)
- [ ] Ajuste de layout para portrait mobile, landscape tablet, widescreen desktop
- [ ] Verificar: áudio funciona após primeiro toque em iOS
- [ ] Verificar: joystick responsivo em touch lento (idoso com dedo grande)
- [ ] Performance: DevTools Timeline — confirmar < 16ms/frame no A06

**Critério de done:** passa nos 5 devices acima sem crash, sem 30fps drops, sem áudio mudo.

### Dia 10 — Analytics, Ads e Deploy Final

**Objetivo:** medir e monetizar desde o lançamento.

- [ ] Google Analytics 4 — eventos: `game_start`, `game_over`, `score_final`, `share_clicked`, `powerup_used`
- [ ] Google AdSense ou AdinPlay — banner footer (fora da área de jogo)
- [ ] Rewarded video entre partidas (opcional, somente se não prejudicar fluxo)
- [ ] Domínio `congressodosmortos.com.br` apontando para Vercel
- [ ] Cloudflare CDN na frente (latência baixa, proteção DDoS, custo R$ 0)
- [ ] Teste de carga: 100 usuários simultâneos (jogo é 100% client-side — servidor só serve assets estáticos)
- [ ] Verificar: bundle size total < 5MB (sprites + audio + código)
- [ ] Smoke test final: link → escolhe skin → joga → morre → compartilha. Zero fricção.

**Critério de done:** link funcional em congressodosmortos.com.br. Alguém que nunca viu o jogo consegue jogar em 5 segundos.

---

## 9. O que do Plano Original se Aplica — Conceitos que Migram de Godot para Web

### O que migra com zero adaptação (conceitos puros):

**1. A filosofia de game feel**
Hit stop, screen shake, flash branco, knockback, damage numbers — tudo isso migra 1:1. A diferença é só a API. O conceito de "3 frames de hitstop = peso físico" funciona igual no browser. O cérebro humano não sabe que é Canvas.

**2. Y-Sort para profundidade**
O sistema de `z_index = position.y / 10` do Godot vira `setDepth(entity.y)` no Phaser. Mesma lógica, mesma sensação de profundidade sem câmera 3D.

**3. Animação prioritária (AnimPriority)**
O sistema de priority `IDLE < MOVE < ATTACK < HURT < DEATH` migra com pequenas adaptações. A lógica é a mesma — animações de maior prioridade interrompem as de menor, e one-shots liberam prioridade ao terminar.

**4. Joystick dinâmico (aparece onde o dedo está)**
O `VirtualJoystick.gd` do plano original foi traduzido quase linha a linha para JavaScript. A filosofia de "input que desaparece" — joystick surge onde o dedo toca, sem posição fixa — é totalmente implementável no browser.

**5. Object Pooling como mandamento**
A filosofia do pool é mais crítica no browser que no Godot. JavaScript tem GC pauses que o Godot (com seu memory model manual em C++) não tem. Cada zombie, projectile, damage number e particle emitter começa pré-alocado.

**6. Budget de partículas**
Os números mudam (300 → 175 simultâneas) mas o princípio permanece: limite hard no número de partículas ativas, lifetime curto, destruição explícita. O Phaser tem `maxParticles` que age como o pool size do Godot.

**7. Sistema de Audio com prioridade e throttle**
`MAX_CONCURRENT_SFX = 8` e `MAX_COMBAT_SFX = 4` do plano original migram direto. O Web Audio API tem menos canais físicos que o AudioServer do Godot, mas a lógica de "descartar sons menos importantes quando cheio" é idêntica.

**8. Dead zones no input**
8px de dead zone no joystick, input buffer de 6 frames para o power-up — esses números foram calculados para o A06 e são válidos para qualquer mobile browser. Tremor de mão é igual no Godot e no browser.

**9. Flip horizontal para direção**
`$AnimatedSprite2D.flip_h = target.x < global_position.x` vira `sprite.flipX = target.x < this.x`. Exatamente igual.

**10. Música adaptativa**
O sistema de crossfade entre estados (menu, gameplay, boss) do `AudioManager.gd` migra direto para Phaser Tweens de volume. A lógica de "boss music sobe enquanto gameplay music cai" é idêntica.

### O que NÃO migra (específico do Godot/nativo):

| Conceito Godot | Por que não migra | Alternativa Web |
|---|---|---|
| `Engine.time_scale` global | Phaser usa `time.timeScale` (scene) — mais granular | `scene.time.timeScale = 0.05` — funciona melhor |
| `Input.vibrate_handheld()` | API diferente | `navigator.vibrate()` — funciona em Android Chrome |
| `ShaderMaterial` para hit flash | GLSL shader custom requer pipeline complexo | `setTintFill(0xffffff)` — 90% do efeito, 0% da complexidade |
| `CanvasLayer` para HUD | Conceito de layer separado do Godot | `setScrollFactor(0)` no Phaser + câmera separada |
| `CPUParticles2D` vs `GPUParticles2D` | Decisão de renderização interna do Godot | Phaser WebGL particles — sempre GPU |
| `GDScript` com tipos estáticos | Linguagem proprietária | JavaScript/TypeScript — tradeoff de familiaridade |
| `CharacterBody2D.move_and_slide()` | API do Godot Physics | Phaser Arcade Physics — mais simples, suficiente para o escopo |
| `@export var` no Inspector | Sistema de editor Godot | Constantes no código ou config JSON |

### A conclusão sobre a migração:

O plano original foi escrito para Godot, mas a maior parte do documento era sobre **intenção de design**, não sobre sintaxe de engine. "Hit stop de 3 frames" não é uma feature do Godot — é uma decisão de game feel. "Dead zone de 8px no joystick" não é uma limitação do A06 — é uma calibração para mãos humanas.

Tudo que importa migra. O que não migra são detalhes de API que têm equivalentes diretos. A filosofia — cada frame importa, cada toque importa, cada pixel importa — não tem versão de engine. É o jogo.

---

## Apêndice: Stack Técnica Resumida

| Categoria | Escolha | Justificativa |
|---|---|---|
| **Framework de jogo** | Phaser 3.60+ | Maduro, WebGL nativo, comunidade grande, docs excelentes |
| **Linguagem** | JavaScript (TypeScript opcional) | Menor overhead de setup para 2 semanas |
| **Bundler** | Vite | Hot reload instantâneo, bundle otimizado, zero config |
| **Hosting** | Vercel | Deploy em 1 comando, CDN global, HTTPS automático, free tier generoso |
| **CDN/DDoS** | Cloudflare | Proteção grátis para o pico de lançamento viral |
| **Analytics** | Google Analytics 4 + eventos customizados | Free, rico, integra com Ads |
| **Audio** | Web Audio API via Phaser | Abstração suficiente, controle total |
| **Physics** | Phaser Arcade Physics | Simples, rápido, suficiente para top-down 2D |
| **Ads** | AdinPlay ou Google AdSense | AdinPlay especializado em browser games (CPM melhor) |
| **Compartilhamento** | Web Share API + canvas.toDataURL() | Nativo do browser, sem dependência externa |
| **Persistência** | localStorage | Score, preferências de mute, skin — zero backend |

---

*"Em Kirby's Dream Land, eu tinha 64KB de ROM. Nenhuma desculpa de hardware vai me fazer aceitar 30fps num browser em 2026."*

— Masahiro Sakurai
