# ZUMBIS DE BRASILIA -- Plano de Frontend Side-View
### Masahiro Sakurai -- Game Feel & Frontend Architecture
### Abril 2026

---

> *"Metal Slug nao e so perspectiva lateral. E uma promessa ao jogador: voce vai VER tudo. Cada expressao. Cada bala. Cada zumbi de terno explodindo em tinta vermelha. O lado e a direcao certa porque o horror que Andre Guedes desenha precisa de espaco horizontal para existir. Nosso trabalho agora e fazer o engine honrar essa promessa. Cada frame. Cada impacto. Cada scroll."*

---

## Stack Confirmada

- **Engine:** Phaser 3.88 com WebGL renderer
- **Frontend:** React 18 + Vite 5
- **Physics:** Arcade Physics (AABB, sem rotacao, perfeito para side-scroller 2D)
- **Integration:** Phaser dentro de React via `useRef` + `useEffect`
- **Target viewport:** 480x270px logicos, escala 2x/3x em CSS
- **Target FPS:** 60fps fixo (requestAnimationFrame com vsync)
- **Plataformas:** Desktop browser (Chrome/Firefox/Safari) + Mobile browser (landscape)

---

## 1. Asset Pipeline

### 1.1 Inventario Atual e Organizacao em Disco

Com 300+ PNGs do Bolsonaro, 28 cenarios side-view e tilesets ja gerados pelo PixelLab, o primeiro trabalho e organizar antes de empacotar. A estrutura de diretorios deve espelhar os atlas finais -- um diretorio por atlas, cada um com todos os frames brutos antes do TexturePacker.

```
assets/
  raw/                         <- sprites brutos do PixelLab, nunca tocados
    characters/
      player/
        idle_0.png ... idle_3.png
        run_0.png ... run_5.png
        attack_melee_0.png ... attack_melee_3.png
        attack_ranged_0.png ... attack_ranged_2.png
        hurt_0.png hurt_1.png
        death_0.png ... death_5.png
      zombies/
        vereador/              <- walk, attack, death
        senador/
        assessor/
        lobista/
        boss_candidato/
        boss_xandao/
        boss_presidente_camara/
    backgrounds/
      sky_gradient.png         <- 480x120, fundo de ceu estatico
      toxic_clouds_sheet.png   <- spritesheet das nuvens
      congresso_sideview.png   <- 320x120, sprite unico
      ministerios_dist_tile.png  <- tileable 960x120
      ministerios_prox_tile.png  <- tileable 1200x180
      bg_objects/
        arvore_seca.png arvorei_seca_2.png
        poste_tombado.png
        placa_campanha_*.png
        carro_abandonado.png
        barricada.png
        lixeira.png
        grade_obra.png
    tilesets/
      esplanada_surface.png    <- tiles de chao, side-scroller format
      esplanada_subsurface.png
    ui/
      hud_hp_bar.png
      hud_wave_badge.png
      hud_score_frame.png
      joystick_outer.png
      joystick_inner.png
      button_attack.png
      button_powerup.png
      pause_panel.png
      gameover_screen.png
    particles/
      ink_splat_0.png ... ink_splat_3.png
      santinho_0.png santinho_1.png
      gas_cloud.png
      paper_scrap_0.png ... paper_scrap_2.png
    onomatopeias/
      thwack.png
      slap.png
      talkei.png
      indeferido.png
      pow.png
      sem_saldo.png
    weapons/
      chinelo.png
      vassoura.png
      urna.png
      cracha.png
      carimbo.png
      biblia.png
      garrafa.png
      taco_golfe.png
    pickups/
      pickup_hp.png
      pickup_speed.png
      pickup_powerup.png

  packed/                      <- saida do TexturePacker, versionado no git
    atlas_characters.png
    atlas_characters.json
    atlas_backgrounds.png
    atlas_backgrounds.json
    atlas_ui.png
    atlas_ui.json
    atlas_particles.png
    atlas_particles.json

  maps/                        <- tilemaps exportados do Tiled
    esplanada_sideview.json
    tileset_esplanada.png      <- tileset referenciado pelo mapa
```

### 1.2 TexturePacker: Configuracao por Atlas

Quatro atlas de 2048x2048px. O limite e o WebGL MAX_TEXTURE_SIZE minimo garantido (4096px), mas 2048px funciona em todo Android desde 2018. Mais que isso e GC pressure sem ganho real.

**Atlas: characters (2048x2048)**

Contem tudo que e sprite animado de entidade viva. Personagens e zumbis no mesmo atlas e a decisao mais importante para batching -- player e zombies sao renderizados em sequencia e vao para a mesma draw call.

```
TexturePacker settings:
  Output: atlas_characters.png / atlas_characters.json
  Max size: 2048x2048
  Algorithm: MaxRects (BestAreaFit)
  Padding: 2px entre frames (evita bleeding em pixel art)
  Allow rotation: FALSE (quebraria animacoes de flip)
  Trim mode: Trim (remove pixels transparentes, economiza ~30% de area)
  Extrude: 1px (evita artifacts de sub-pixel em bordas)
  Format: JSON Hash (recomendado para Phaser -- acesso por nome de frame)
  Naming: {folder}_{basename}  ex: player_idle_0, vereador_walk_2
```

Organizacao interna estimada do atlas_characters 2048x2048:
```
  Player completo (~25 frames de 68x68px) =   ~120.000px2
  5 tipos de zumbi comum (~25 frames cada) =  ~300.000px2
  3 bosses (frames maiores, 90-136px)      =  ~180.000px2
  2 NPCs aliados                           =   ~60.000px2
  Weapons sprites acoplados ao player      =   ~20.000px2
  TOTAL estimado                           =  ~680.000px2 de 4.194.304px2 totais
  Ocupacao: ~16% -- sobra espaco para novas armas e inimigos sem novo atlas
```

**Atlas: backgrounds (2048x2048)**

Sprites de cenario que NAO repetem por tile (Congresso, objetos de fundo individuais, nuvens). Os layers que repetem (ministerios_dist, ministerios_prox) ficam fora do atlas como texturas proprias -- o TileSprite precisa de textura separada para wrap repeat.

```
  congresso_sideview (320x120)
  toxic_clouds frames
  bg_objects: arvores, postes, placas, carros, grades, barricadas
  foreground: postes proximos, alambrados, folhagens
```

**Atlas: ui (2048x2048)**

Tudo que e HUD e interface. Em atlas separado porque a HUD usa camera fixa (sem scroll) e pode ter batching independente. Joystick, botoes, barras de HP, badges de wave, telas de menu.

**Atlas: particles (2048x2048)**

Tudo que e efeito visual temporario: ink splats, santinhos voando, gas, papeis, frames de onomatopeias. Separar em atlas proprio permite desativar o emitter inteiro no modo low-end sem afetar rendering de personagens.

### 1.3 Sprite Sheet Format para Phaser

Usar **JSON Hash** em todos os atlas. JSON Hash acessa frames por nome (string) em vez de indice numerico. Isso e critico para o Phaser `generateFrameNames()` e para debugar -- "player_attack_2" e inequivoco, "frame_47" nao e.

```json
// Exemplo de saida do TexturePacker em JSON Hash
{
  "frames": {
    "player_idle_0": {
      "frame": { "x": 0, "y": 0, "w": 68, "h": 68 },
      "sourceSize": { "w": 68, "h": 68 },
      "spriteSourceSize": { "x": 0, "y": 0, "w": 68, "h": 68 }
    },
    "player_run_0": {
      "frame": { "x": 68, "y": 0, "w": 68, "h": 68 },
      ...
    }
  },
  "meta": {
    "image": "atlas_characters.png",
    "size": { "w": 2048, "h": 2048 },
    "scale": 1
  }
}
```

### 1.4 Preload Strategy com Progress Bar

Boot -> Preload -> Menu -> Game. O Preload carrega assets em duas fases: essenciais (o que aparece no primeiro segundo de jogo) e diferidos (bosses, assets de fases avancadas). Isso elimina tela de loading longa.

```javascript
// src/scenes/PreloadScene.js
export class PreloadScene extends Phaser.Scene {
    constructor() { super({ key: 'PreloadScene' }); }

    preload() {
        // Cria progress bar com elementos primitivos (antes dos assets carregados)
        this._createProgressBar();

        // Fase 1: ESSENCIAIS (bloqueante -- jogo nao comeca sem estes)
        // Atlas de personagens e o mais critico (player + primeiros zumbis)
        this.load.atlas('characters', 'packed/atlas_characters.png', 'packed/atlas_characters.json');
        this.load.atlas('ui', 'packed/atlas_ui.png', 'packed/atlas_ui.json');

        // Backgrounds da fase 1 (o jogador ve imediatamente)
        this.load.image('congresso', 'assets/backgrounds/congresso_sideview.png');
        this.load.image('ministerios_dist', 'assets/backgrounds/ministerios_dist_tile.png');
        this.load.image('ministerios_prox', 'assets/backgrounds/ministerios_prox_tile.png');

        // Tilemap do nivel
        this.load.tilemapTiledJSON('esplanada_map', 'maps/esplanada_sideview.json');
        this.load.image('esplanada_tiles', 'maps/tileset_esplanada.png');

        // Audio essencial (SFX de hit e musica do menu)
        this.load.audio('sfx_hit', 'audio/hit.ogg');
        this.load.audio('sfx_death', 'audio/zombie_death.ogg');
        this.load.audio('bgm_game', 'audio/bgm_esplanada.ogg');

        // Fase 2: DIFERIDOS (carregados durante menu ou early gameplay)
        this.load.atlas('particles', 'packed/atlas_particles.png', 'packed/atlas_particles.json');
        this.load.atlas('backgrounds', 'packed/atlas_backgrounds.png', 'packed/atlas_backgrounds.json');

        // Progress events
        this.load.on('progress', (value) => this._updateProgress(value));
        this.load.on('complete', () => this._onComplete());
    }

    _createProgressBar() {
        const cx = 240, cy = 135; // centro do viewport 480x270
        const barW = 200, barH = 12;

        // Background da barra
        this.add.rectangle(cx, cy, barW + 4, barH + 4, 0x1A1A18);

        // Barra de progresso (cresce da esquerda)
        this.progressBar = this.add.rectangle(
            cx - barW / 2, cy, 0, barH, 0xC8381A
        ).setOrigin(0, 0.5);

        // Texto "CARREGANDO..."
        this.add.text(cx, cy - 20, 'CARREGANDO A ESPLANADA...', {
            fontFamily: 'monospace',
            fontSize: '8px',
            color: '#F0E8D0'
        }).setOrigin(0.5);

        // Logo do jogo (rectangulo placeholder se o logo ainda nao carregou)
        this.add.text(cx, cy - 60, 'ZUMBIS DE BRASILIA', {
            fontFamily: 'monospace',
            fontSize: '14px',
            color: '#C8381A'
        }).setOrigin(0.5);
    }

    _updateProgress(value) {
        // value: 0.0 a 1.0
        this.progressBar.width = 200 * value;
    }

    _onComplete() {
        // Pequeno delay para o jogador ver 100% antes de transicao
        this.time.delayedCall(200, () => {
            this.scene.start('MenuScene');
        });
    }
}
```

---

## 2. Parallax Implementation (7 Layers)

### 2.1 Decisao por Layer: TileSprite vs Image

A diferenca e critica para performance e para correto comportamento visual:

| Layer | Tipo Phaser | Motivo |
|---|---|---|
| L0 Ceu | `add.rectangle` com fillGradientStyle | Gradiente puro -- sem textura, sem draw call de sprite |
| L0 Nuvens toxicas | `add.tileSprite` | Repete horizontalmente em loop continuo |
| L1 Congresso | `add.image` | Sprite UNICO, aparece uma vez no nivel, nao repete |
| L2 Ministerios dist. | `add.tileSprite` | Textura tileable, repete enquanto o jogador anda |
| L3 Ministerios prox. | `add.tileSprite` | Idem, textura diferente |
| L4 Objetos de fundo | `add.group` de `add.image` | Objetos individuais posicionados no nivel, nao repetem |
| L5 Chao | `make.tilemap` | Tilemap do Tiled, geometria de colisao integrada |
| L6 Entidades | `physics.arcade.sprite` | Fisicas, colisao, animacao |
| L7 Foreground | `add.image` com alpha | Sprites na frente da acao, parcialmente transparentes |

### 2.2 ScrollFactor por Layer

```
Camera move 100px para a direita:

Layer 0 - Ceu gradient:      move  0px   (scrollFactor: 0)    -- CONGELADO
Layer 0 - Nuvens toxicas:    move  5px   (scrollFactor: 0.05) -- quasi-estatico
Layer 1 - Congresso:         move 10px   (scrollFactor: 0.1)  -- distante, lento
Layer 2 - Minist. distantes: move 25px   (scrollFactor: 0.25) -- lento-medio
Layer 3 - Minist. proximos:  move 50px   (scrollFactor: 0.5)  -- medio
Layer 4 - Objetos de fundo:  move 75px   (scrollFactor: 0.75) -- rapido-medio
Layer 5 - Chao:              move 100px  (scrollFactor: 1.0)  -- 1:1 com camera
Layer 6 - Entidades:         move 100px  (scrollFactor: 1.0)  -- 1:1 com camera
Layer 7 - Foreground:        move 120px  (scrollFactor: 1.2)  -- mais rapido (parallax invertido)
```

### 2.3 Implementacao dos TileSprites com Parallax Correto

O TileSprite com `setScrollFactor()` NAO faz parallax automaticamente no Phaser -- o scrollFactor afeta a posicao do objeto, mas o tilePositionX precisa ser atualizado manualmente para o loop correto.

```javascript
// src/scenes/GameScene.js -- create()
create() {
    const LEVEL_W = 9600; // largura total do nivel (600 tiles x 16px)
    const VIEWPORT_W = 480;
    const HORIZON_Y = 120; // Y onde os predios encontram o ceu

    // L0: Ceu -- gradiente puro
    const sky = this.add.rectangle(240, 60, 480, 120, 0x000000);
    sky.setScrollFactor(0);
    sky.setDepth(-1000);
    sky.fillGradientStyle(0xC8381A, 0xC8381A, 0x1A1A18, 0x1A1A18, 1);

    // L0: Nuvens toxicas (TileSprite que loopa)
    this.toxicClouds = this.add.tileSprite(240, 30, VIEWPORT_W, 60, 'toxic_clouds');
    this.toxicClouds.setScrollFactor(0); // posicao fixa, tilePosition animado no update
    this.toxicClouds.setAlpha(0.6);
    this.toxicClouds.setDepth(-995);

    // L1: Congresso -- Image unica, scrollFactor via setScrollFactor
    this.congress = this.add.image(LEVEL_W * 0.5, HORIZON_Y, 'congresso');
    this.congress.setScrollFactor(0.1);
    this.congress.setOrigin(0.5, 1.0); // ancora na base
    this.congress.setDepth(-900);

    // Brilho verde pulsante no Congresso (PointLight)
    this.congressLight = this.lights.addLight(
        LEVEL_W * 0.5, HORIZON_Y - 60, 120, 0x3D6B3A, 1.5
    );
    this.lights.enable().setAmbientColor(0x404040);

    // L2: Ministerios distantes (TileSprite)
    // setScrollFactor(0) aqui -- parallax e feito manualmente no update()
    this.distantMinistries = this.add.tileSprite(
        VIEWPORT_W / 2, HORIZON_Y - 60, VIEWPORT_W, 120, 'ministerios_dist'
    );
    this.distantMinistries.setScrollFactor(0);
    this.distantMinistries.setDepth(-800);

    // L3: Ministerios proximos (TileSprite)
    this.nearMinistries = this.add.tileSprite(
        VIEWPORT_W / 2, HORIZON_Y, VIEWPORT_W, 180, 'ministerios_prox'
    );
    this.nearMinistries.setScrollFactor(0);
    this.nearMinistries.setDepth(-600);

    // Camera setup
    this.cameras.main.startFollow(this.player, true, 0.08, 0.08);
    this.cameras.main.setBounds(0, 0, LEVEL_W, 270);
    // Deadzone: camera so se move quando player sai desta area central
    this.cameras.main.setDeadzone(80, 40);
}

update(time, delta) {
    const camX = this.cameras.main.scrollX;

    // Parallax manual para TileSprites
    // tilePositionX move o CONTEUDO da textura, nao o objeto em si
    this.toxicClouds.tilePositionX += 0.02; // drift autonomo das nuvens
    this.distantMinistries.tilePositionX = camX * 0.25;
    this.nearMinistries.tilePositionX = camX * 0.5;

    // Pulso do brilho verde do Congresso
    this.congressLight.intensity = 1.5 + Math.sin(time * 0.002) * 0.3;
}
```

### 2.4 Segment Transition: Trocar Backgrounds Entre Segmentos

O nivel tem 5 segmentos de ~1920px cada (120 tiles de 16px). Cada segmento tem variante diferente de chao e pode ter variante de ministerio. A transicao entre segmentos precisa ser imperceptivel -- crossfade de 800ms durante o scroll.

```javascript
// src/systems/SegmentManager.js
export class SegmentManager {
    constructor(scene) {
        this.scene = scene;
        this.currentSegment = 0;

        // Mapa de quais assets usar por segmento
        this.segmentConfig = [
            { ground: 'calcada_concreto', ministries: 'ministerios_prox', atX: 0 },
            { ground: 'asfalto_eixo',     ministries: 'ministerios_prox', atX: 1920 },
            { ground: 'grama_seca',       ministries: 'ministerios_prox_2', atX: 3840 },
            { ground: 'concreto_espelho', ministries: 'ministerios_prox',   atX: 5760 },
            { ground: 'cerimonial',       ministries: 'ministerios_congresso', atX: 7680 },
        ];
    }

    update(cameraX) {
        for (let i = 0; i < this.segmentConfig.length; i++) {
            const seg = this.segmentConfig[i];
            const nextSeg = this.segmentConfig[i + 1];
            if (!nextSeg) continue;

            // Quando camera atinge 80% do segmento atual, inicia transicao
            const transitionPoint = seg.atX + (nextSeg.atX - seg.atX) * 0.8;

            if (cameraX >= transitionPoint && this.currentSegment === i) {
                this.currentSegment = i + 1;
                this._crossfadeBackground(nextSeg.ministries);
            }
        }
    }

    _crossfadeBackground(newTextureKey) {
        const scene = this.scene;

        // Layer temporaria com nova textura, alpha 0
        const newLayer = scene.add.tileSprite(
            240, scene.nearMinistries.y,
            480, 180,
            newTextureKey
        );
        newLayer.setScrollFactor(0);
        newLayer.setDepth(-599); // um tick acima do nearMinistries existente
        newLayer.setAlpha(0);
        newLayer.tilePositionX = scene.nearMinistries.tilePositionX;

        // Crossfade
        scene.tweens.add({
            targets: newLayer,
            alpha: 1,
            duration: 800,
            ease: 'Linear',
            onComplete: () => {
                // Substitui a layer antiga
                scene.nearMinistries.destroy();
                scene.nearMinistries = newLayer;
                scene.nearMinistries.setDepth(-600);
            }
        });
    }
}
```

---

## 3. Player Controller (Side-View)

### 3.1 Movimento Horizontal: Aceleracao e Desaceleracao

Em Metal Slug, o Marco Rossi nao para imediatamente. Tem uma micro-desaceleracao (~3-4 frames) que da peso ao personagem. Sem isso, o controle parece de jogo de browser barato. Com isso, parece Metal Slug.

```javascript
// src/entities/Player.js
export class Player extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y) {
        super(scene, x, y, 'characters', 'player_idle_0');
        scene.add.existing(this);
        scene.physics.add.existing(this);

        // Stats de movimento
        this.WALK_SPEED = 120;       // pixels/segundo -- velocidade maxima
        this.ACCELERATION = 600;     // pixels/segundo2 -- quanto tempo pra max speed
        this.DECELERATION = 900;     // pixels/segundo2 -- mais rapido que accel = stops crisply
        this.GROUND_Y = 210;         // Y do chao no viewport (em coords de nivel)

        // Colisao: hitbox menor que o sprite (mais justo para o jogador)
        this.body.setSize(16, 36);   // corpo da colisao: 16px largo, 36px alto
        this.body.setOffset(26, 20); // centraliza dentro do canvas de 68x68

        // Estado da maquina de animacao
        this.animState = 'idle';     // idle | run | attack_melee | attack_ranged | hurt | dead
        this.animPriority = 0;       // 0=idle, 1=move, 2=attack, 3=hurt, 4=dead
        this.facingRight = true;

        // Cooldowns
        this.attackCooldown = 400;   // ms entre ataques melee
        this.nextAttackTime = 0;
        this.isInvincible = false;   // frames de invincibilidade pos-dano
        this.INVINCIBLE_DURATION = 800; // ms

        // Arma atual
        this.currentWeapon = 'chinelo'; // chinelo | vassoura | urna | cracha | carimbo

        this.anims.on('animationcomplete', this._onAnimComplete, this);
    }

    update(time, delta, inputDir) {
        if (this.animState === 'dead') return;

        this._handleMovement(inputDir, delta);
        this._handleFacing(inputDir);
        this._updateAnimState(inputDir);
    }

    _handleMovement(inputDir, delta) {
        const body = this.body;
        const dt = delta / 1000; // delta em segundos

        if (inputDir.x !== 0) {
            // Aceleracao na direcao do input
            const targetVX = inputDir.x * this.WALK_SPEED;
            const diff = targetVX - body.velocity.x;
            const step = this.ACCELERATION * dt;
            body.velocity.x += Math.sign(diff) * Math.min(Math.abs(diff), step);
        } else {
            // Desaceleracao: freia mais rapido do que acelera
            const step = this.DECELERATION * dt;
            if (Math.abs(body.velocity.x) <= step) {
                body.velocity.x = 0;
            } else {
                body.velocity.x -= Math.sign(body.velocity.x) * step;
            }
        }

        // Clamp para nao ultrapassar speed maxima (por exemplo durante knockback que decai)
        body.velocity.x = Phaser.Math.Clamp(body.velocity.x, -this.WALK_SPEED * 1.5, this.WALK_SPEED * 1.5);
    }

    _handleFacing(inputDir) {
        if (inputDir.x > 0 && !this.facingRight) {
            this.facingRight = true;
            this.setFlipX(false);
        } else if (inputDir.x < 0 && this.facingRight) {
            this.facingRight = false;
            this.setFlipX(true);
        }
    }

    _updateAnimState(inputDir) {
        const isMoving = Math.abs(this.body.velocity.x) > 10;

        if (this.animPriority >= 3) return; // hurt ou dead tem prioridade total

        if (this.animPriority >= 2) return; // ataque em curso

        if (isMoving && this.animState !== 'run') {
            this.animState = 'run';
            this.animPriority = 1;
            this.play('player_run', true);
        } else if (!isMoving && this.animState !== 'idle') {
            this.animState = 'idle';
            this.animPriority = 0;
            this.play('player_idle', true);
        }
    }

    _onAnimComplete(anim) {
        // Animacoes one-shot devolvem controle para idle/run
        if (anim.key === 'player_attack_melee' || anim.key === 'player_attack_ranged') {
            this.animPriority = 0;
            this.animState = 'idle';
        }
        if (anim.key === 'player_hurt') {
            this.animPriority = 0;
            this.animState = 'idle';
        }
    }

    attackMelee(time) {
        if (time < this.nextAttackTime) return false;
        if (this.animPriority >= 3) return false;

        this.nextAttackTime = time + this.attackCooldown;
        this.animState = 'attack_melee';
        this.animPriority = 2;
        this.play('player_attack_melee');
        return true;
    }

    attackRanged(time) {
        if (this.currentWeapon !== 'urna' && this.currentWeapon !== 'cracha') return false;
        if (this.animPriority >= 3) return false;

        this.animState = 'attack_ranged';
        this.animPriority = 2;
        this.play('player_attack_ranged');
        return true;
    }

    takeDamage(amount) {
        if (this.isInvincible) return;
        if (this.animState === 'dead') return;

        this.hp -= amount;

        if (this.hp <= 0) {
            this._die();
            return;
        }

        this.animState = 'hurt';
        this.animPriority = 3;
        this.play('player_hurt');

        // Invincibility frames pos-dano
        this.isInvincible = true;
        this.scene.time.delayedCall(this.INVINCIBLE_DURATION, () => {
            this.isInvincible = false;
        });

        // Blink durante invincibilidade (visual feedback classico)
        this.scene.tweens.add({
            targets: this,
            alpha: { from: 0.3, to: 1 },
            duration: 80,
            repeat: Math.floor(this.INVINCIBLE_DURATION / 160),
            yoyo: true,
            onComplete: () => { this.setAlpha(1); }
        });
    }

    _die() {
        this.animState = 'dead';
        this.animPriority = 4;
        this.body.setVelocity(0, 0);
        this.body.enable = false;
        this.play('player_death');
        this.scene.events.emit('playerDied');
    }

    switchWeapon(weaponKey) {
        this.currentWeapon = weaponKey;
        this.scene.events.emit('weaponChanged', weaponKey);
    }
}
```

### 3.2 Jump: Decisao Consciente

**Decisao: SEM JUMP no MVP.**

Metal Slug tem jump porque e um run-and-gun horizontal onde voce precisa evitar projéteis e alcançar plataformas. Zumbis de Brasilia e horde survival side-view num chao PLANO. Jump adiciona:
- Complexidade de estado (aer, land, fall animations)
- Physics mais complexas (gravidade, floor detection)
- Necessidade de plataformas no design de nivel
- Superficie de bug drasticamente maior

O que ganhamos sem jump: controle mais simples no mobile, menos estados de animacao, mais foco em combate horizontal. Dead Ahead (referencia direta do genero) nao tem jump. Funcionou muito bem.

Se a decisao mudar no futuro: o Arcade Physics do Phaser tem `body.setGravityY()` e `body.setVelocityY()` prontos. A arquitetura do Player aqui nao fecha a porta -- so nao abre ela agora.

### 3.3 Animation State Machine

```
                      [IDLE] <─── qualquer input zerado
                        │
                   move input
                        │
                        v
                      [RUN] ─── input zerado ──> [IDLE]
                        │
              attack input / auto-attack range
                        │
                        v
              [ATTACK_MELEE] ──onComplete──> [IDLE/RUN]
                        │
              (arma ranged equipada)
                        │
                        v
             [ATTACK_RANGED] ──onComplete──> [IDLE/RUN]

Dano recebido (de qualquer estado exceto DEAD):
                        │
                        v
                     [HURT] ──onComplete──> [IDLE/RUN]

HP <= 0 (de qualquer estado):
                        │
                        v
                     [DEAD] ──onComplete──> (emite playerDied)
```

Implementado via `animPriority`:
- 0: idle/run (interruptivel por qualquer coisa)
- 1: run (interruptivel por ataque e hurt)
- 2: attack (interruptivel por hurt, nao por outro ataque)
- 3: hurt (interruptivel por death)
- 4: dead (ininterruptivel)

---

## 4. Zombie AI (Side-View)

### 4.1 Comportamento Base

Em side-view, a AI dos zumbis e radicalmente mais simples que top-down. Nao ha pathfinding. Os zumbis andam horizontalmente em direcao ao player. O resultado visual e um MURO DE CARNE avancando -- que e exatamente a estetica correta para horde survival.

```javascript
// src/entities/Zombie.js
export class Zombie extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y, config) {
        super(scene, x, y, 'characters', `${config.type}_walk_0`);
        scene.add.existing(this);
        scene.physics.add.existing(this);

        this.type = config.type;         // 'vereador' | 'assessor' | 'senador' | 'lobista'
        this.hp = config.hp;
        this.maxHp = config.hp;
        this.speed = config.speed;       // pixels/segundo
        this.damage = config.damage;
        this.scoreValue = config.score;
        this.attackRange = config.attackRange || 20; // px de distancia para melee

        this.attackCooldown = config.attackCooldown || 1200;
        this.nextAttackTime = 0;
        this.isDead = false;

        // Hitbox menor que o sprite (consistente com o player)
        this.body.setSize(config.hitboxW || 20, config.hitboxH || 36);
        this.body.setOffset(config.hitboxOffX || 22, config.hitboxOffY || 18);

        // Inicia andando
        this.play(`${config.type}_walk`);
    }

    update(time, playerX, playerY) {
        if (this.isDead) return;

        const dirX = playerX > this.x ? 1 : -1;

        // Flip do sprite baseado na direcao
        this.setFlipX(dirX < 0);

        const distToPlayer = Math.abs(playerX - this.x);

        if (distToPlayer <= this.attackRange) {
            // Parado, atacando
            this.body.setVelocityX(0);

            if (time >= this.nextAttackTime) {
                this._attack(time);
            }
        } else {
            // Movendo em direcao ao player
            this.body.setVelocityX(dirX * this.speed);

            if (this.anims.currentAnim?.key !== `${this.type}_walk`) {
                this.play(`${this.type}_walk`, true);
            }
        }
    }

    _attack(time) {
        this.nextAttackTime = time + this.attackCooldown;
        this.play(`${this.type}_attack`);
        this.scene.events.emit('zombieAttack', this);
    }

    takeDamage(amount, knockbackDir) {
        if (this.isDead) return;

        this.hp -= amount;

        if (this.hp <= 0) {
            this._die();
            return;
        }

        // Knockback horizontal
        const kbX = knockbackDir * 200;
        this.body.setVelocityX(kbX);
        this.scene.time.delayedCall(100, () => {
            if (this.active && !this.isDead) {
                this.body.setVelocityX(0);
            }
        });

        this.play(`${this.type}_hurt`, true);
    }

    _die() {
        this.isDead = true;
        this.body.enable = false;
        this.body.setVelocity(0, 0);
        this.play(`${this.type}_death`);

        // Loot drop antes da animacao de morte terminar
        this.scene.events.emit('zombieDied', this.x, this.y, this.scoreValue, this.type);

        this.once('animationcomplete', () => {
            // Retorna ao pool em vez de destruir
            this.scene.zombiePool.release(this);
        });
    }
}
```

### 4.2 Variantes de Zumbi

| Tipo | Sprite | HP | Speed | Damage | Comportamento Especial |
|---|---|---|---|---|---|
| Vereador | 44x64 canvas | 30 | 50px/s | 10 | Base. Anda devagar, morre facil. Spawna em grupos de 5-8 |
| Assessor | 48x68 canvas | 20 | 90px/s | 8 | Rapido, fraco. Vem em bando de 3. Surpresa de velocidade |
| Senador Vitalicio | 52x72 canvas | 80 | 30px/s | 20 | Lento, tanque. Empurra outros zumbis com o volume |
| Lobista | 48x68 canvas | 50 | 60px/s | 15 | Medio. Joga maleta (projetil a 300px de distancia) |

**Tank (Senador Vitalicio) -- comportamento de bump:**
O Senador eh grande. Quando ele colide com outros zumbis na mesma camada, eles sao empurrados. Implementado via Arcade Physics separateX automatico -- o Phaser ja faz isso em colisores do mesmo grupo. O resultado visual e o Senador abrindo caminho na horda, o que e perfeitamente caracterizante.

**Ranged (Lobista) -- projetil:**
```javascript
// No update do Lobista, quando distancia <= 300px e cooldown ok:
_throwBriefcase(time, playerX, playerY) {
    this.nextAttackTime = time + 2000; // 2s entre arremessos
    this.play('lobista_attack_ranged');

    // Pega projétil do pool
    const proj = this.scene.enemyProjectilePool.get(this.x, this.y);
    if (!proj) return;

    const angle = Phaser.Math.Angle.Between(this.x, this.y, playerX, playerY);
    this.scene.physics.velocityFromAngle(
        Phaser.Math.RadToDeg(angle), 180, proj.body.velocity
    );
    proj.setActive(true).setVisible(true);
}
```

### 4.3 Spawn: Bordas + Ministry Doors

Dois tipos de spawn para variedade visual:

**Tipo 1: Bordas da tela**
```javascript
// src/systems/WaveSystem.js
_spawnFromEdge(zombieType) {
    const cam = this.scene.cameras.main;
    // Spawna fora do viewport + 32px de margem
    const side = Phaser.Math.RND.pick(['left', 'right']);
    const spawnX = side === 'left'
        ? cam.scrollX - 32
        : cam.scrollX + 480 + 32;
    const spawnY = GROUND_Y - 10; // na superficie do chao

    const zombie = this.scene.zombiePool.get(spawnX, spawnY, zombieType);
    zombie.setActive(true).setVisible(true);
}
```

**Tipo 2: Ministry Doors (spawn visual)**
Os ministerios proximos tem portas escuras na fachada. Esses sao spawn points decorativos: o zumbi aparece com uma animacao de "saindo pela porta" (emerge de dentro para fora -- scale de 0.5 a 1.0 em 200ms + fade in).

```javascript
_spawnFromDoor(zombieType) {
    // Ministry doors sao posicoes fixas no nivel, definidas no Tiled
    const doors = this.scene.ministryDoorPositions; // array de {x, y}
    const door = Phaser.Math.RND.pick(doors.filter(d => this._isDoorVisible(d)));
    if (!door) return this._spawnFromEdge(zombieType); // fallback

    const zombie = this.scene.zombiePool.get(door.x, door.y, zombieType);
    zombie.setAlpha(0).setScale(0.5).setActive(true).setVisible(true);

    // Animacao de saida
    this.scene.tweens.add({
        targets: zombie,
        alpha: 1,
        scaleX: 1,
        scaleY: 1,
        duration: 200,
        ease: 'Back.easeOut'
    });
}
```

### 4.4 Object Pool de Zumbis

Nenhum `destroy()` no mid-game. O pool mantém instancias inativas e as reutiliza.

```javascript
// src/systems/ZombiePool.js
export class ZombiePool {
    constructor(scene, poolSize = 60) {
        this.scene = scene;
        this.pool = {}; // chaveado por tipo de zumbi

        const types = ['vereador', 'assessor', 'senador', 'lobista'];
        types.forEach(type => {
            this.pool[type] = [];
            for (let i = 0; i < poolSize / types.length; i++) {
                const z = new Zombie(scene, -1000, -1000, ZOMBIE_CONFIGS[type]);
                z.setActive(false).setVisible(false);
                this.pool[type].push(z);
            }
        });
    }

    get(x, y, type) {
        const available = this.pool[type]?.find(z => !z.active);
        if (!available) {
            // Pool esgotado: expande dinamicamente (raro, mas seguro)
            const z = new Zombie(this.scene, x, y, ZOMBIE_CONFIGS[type]);
            this.pool[type].push(z);
            return z;
        }

        available.setPosition(x, y);
        available.hp = ZOMBIE_CONFIGS[type].hp;
        available.isDead = false;
        available.body.enable = true;
        available.setAlpha(1).setScale(1);
        return available;
    }

    release(zombie) {
        zombie.setActive(false).setVisible(false);
        zombie.body.enable = false;
        zombie.setPosition(-1000, -1000);
        zombie.body.setVelocity(0, 0);
    }
}
```

### 4.5 Horde Density Management

O Wave System controla quantos zumbis existem na tela ao mesmo tempo. Spawn rate aumenta com o tempo, mas o numero MAX de zumbis ativos e fixo para manter performance.

```javascript
// Configuracao de density por wave
const WAVE_CONFIGS = {
    1:  { maxActive: 8,  spawnInterval: 3000, types: ['vereador'] },
    2:  { maxActive: 12, spawnInterval: 2500, types: ['vereador', 'assessor'] },
    3:  { maxActive: 16, spawnInterval: 2000, types: ['vereador', 'assessor'] },
    5:  { maxActive: 20, spawnInterval: 1800, types: ['vereador', 'assessor', 'senador'] },
    7:  { maxActive: 25, spawnInterval: 1500, types: ['vereador', 'assessor', 'senador', 'lobista'] },
    10: { maxActive: 30, spawnInterval: 1200, types: 'all', bossSpawn: true },
};
```

---

## 5. Combat Feel: O Polish que Faz a Diferença

Esta secao e a mais importante do documento. Tudo o que esta acima e prerequisito. Isto aqui e o que separa um jogo que as pessoas JOGAM de um jogo que as pessoas SENTEM.

### 5.1 CombatFeedback System: Sequencia Completa de Hit

Cada hit executa esta sequencia exata, em ordem:

```javascript
// src/systems/CombatFeedback.js
export class CombatFeedback {
    constructor(scene) {
        this.scene = scene;
        this.damageNumbers = new DamageNumberPool(scene, 20);
        this.onomatopeias = new OnomatopeiaPool(scene, 10);
        this.inkParticles = scene.add.particles(0, 0, 'particles', {
            frame: ['ink_splat_0', 'ink_splat_1', 'ink_splat_2', 'ink_splat_3'],
            lifespan: 400,
            speed: { min: 80, max: 200 },
            scale: { start: 1.0, end: 0.2 },
            alpha: { start: 1, end: 0 },
            quantity: 6,
            emitting: false, // manual emit apenas no hit
        });
    }

    // Chamado pelo CombatSystem a cada hit confirmado
    onHit(target, attackerX, isCrit, weaponId) {
        const hitX = target.x;
        const hitY = target.y - 20;

        // 1. HIT STOP: 3 frames (50ms) normais, 5 frames (83ms) em crit
        //    Pausa o timeScale do jogo. O cerebro nao percebe o delay --
        //    mas registra como impacto fisico. Obrigatorio.
        this._applyHitStop(isCrit ? 83 : 50);

        // 2. HIT FLASH: sprite do inimigo fica branco por 1 frame (16ms)
        //    setTintFill substitui TODA a cor do sprite por branco puro.
        //    clearTint devolvs a aparencia normal.
        //    Nao e sutil. Nao deve ser sutil. E uma CONFIRMACAO de hit.
        this.flashSprite(target, 16);

        // 3. KNOCKBACK: empurra o zumbi na direcao do golpe
        //    200px/s por 100ms. Decai naturalmente com velocidade zero no body.
        const kbDir = attackerX < target.x ? 1 : -1;
        target.body.setVelocityX(kbDir * 200);
        this.scene.time.delayedCall(100, () => {
            if (target.active) target.body.setVelocityX(0);
        });

        // 4. SCREEN SHAKE: imperceptivel em normal, notavel em crit
        //    Escala progressiva: hit normal < hit crit < boss hit < boss kill
        this.scene.cameras.main.shake(
            isCrit ? 80 : 40,
            isCrit ? 0.006 : 0.003
        );

        // 5. INK PARTICLES: spray de pixels vermelhos estilo Andre Guedes
        //    Emite na posicao do hit, dispersa em angulo baseado na direcao
        this.inkParticles.setPosition(hitX, hitY);
        this.inkParticles.emitParticle(isCrit ? 10 : 6);

        // 6. DAMAGE NUMBER: numero flutuante sobe e desaparece em 600ms
        this.damageNumbers.spawn(hitX, hitY, weaponId.damage, isCrit);

        // 7. ONOMATOPEIA: texto estilo quadrinhos por 40 frames (~666ms)
        if (isCrit || Math.random() < 0.4) {
            this.onomatopeias.spawn(hitX, hitY - 30, weaponId);
        }

        // 8. HAPTIC (mobile only): vibracao confirma o peso do golpe
        if (navigator.vibrate) {
            navigator.vibrate(isCrit ? 30 : 12);
        }
    }

    onKill(target, isCrit) {
        // Kill ganha efeitos adicionais em cima dos de hit
        this.inkParticles.setPosition(target.x, target.y - 20);
        this.inkParticles.emitParticle(15); // mais particulas

        // Shake mais longo no kill
        this.scene.cameras.main.shake(
            isCrit ? 120 : 80,
            isCrit ? 0.009 : 0.005
        );

        // Score pop: onomatopeia especial de kill
        this.onomatopeias.spawnKill(target.x, target.y);
    }

    _applyHitStop(durationMs) {
        // timeScale afeta tudo no Phaser (tweens, physics, animacoes)
        // MAS time.delayedCall usa tempo REAL -- o callback dispara certo
        // mesmo com timeScale baixo. Isso e critico.
        this.scene.time.timeScale = 0.05;
        this.scene.time.delayedCall(durationMs, () => {
            this.scene.time.timeScale = 1.0;
        });
    }

    flashSprite(sprite, durationMs = 16) {
        sprite.setTintFill(0xffffff);
        this.scene.time.delayedCall(durationMs, () => {
            if (sprite.active) sprite.clearTint();
        });
    }
}
```

### 5.2 Damage Number Pool

Numeros flutuantes. Sobem 40px e somem. Criticos ficam maiores e amarelos.

```javascript
// src/systems/DamageNumberPool.js
export class DamageNumberPool {
    constructor(scene, poolSize) {
        this.pool = [];
        for (let i = 0; i < poolSize; i++) {
            const text = scene.add.text(-1000, -1000, '', {
                fontFamily: 'monospace',
                fontSize: '10px',
                color: '#FFFFFF',
                stroke: '#000000',
                strokeThickness: 2,
            });
            text.setDepth(700).setActive(false).setVisible(false);
            this.pool.push(text);
        }
    }

    spawn(x, y, damage, isCrit) {
        const text = this.pool.find(t => !t.active);
        if (!text) return;

        text.setText(isCrit ? `${damage}!!` : `${damage}`);
        text.setStyle({
            fontSize: isCrit ? '14px' : '10px',
            color: isCrit ? '#FFD700' : '#FFFFFF',
        });
        text.setPosition(x, y).setAlpha(1).setScale(1);
        text.setActive(true).setVisible(true);

        text.scene.tweens.add({
            targets: text,
            y: y - 40,
            alpha: 0,
            scaleX: isCrit ? 1.4 : 1.0,
            scaleY: isCrit ? 1.4 : 1.0,
            duration: 600,
            ease: 'Sine.easeOut',
            onComplete: () => {
                text.setActive(false).setVisible(false).setPosition(-1000, -1000);
            }
        });
    }
}
```

### 5.3 Onomatopeias Pool: THWACK! SLAP! TALKEI?

A onomatopeia e um sprite (nao texto) -- isso e critico. Texto renderizado on-the-fly tem custo de CPU para rasterizacao. Sprite pre-renderizado no atlas e uma draw call.

```javascript
// src/systems/OnomatopeiaPool.js
const WEAPON_ONOMATOPEIAS = {
    chinelo:  ['thwack', 'slap'],
    vassoura: ['thwack', 'pow'],
    urna:     ['talkei', 'sem_saldo'],
    cracha:   ['indeferido', 'slap'],
    carimbo:  ['indeferido', 'pow'],
};

export class OnomatopeiaPool {
    constructor(scene, poolSize) {
        this.pool = [];
        for (let i = 0; i < poolSize; i++) {
            const img = scene.add.image(-1000, -1000, 'particles', 'thwack');
            img.setDepth(750).setActive(false).setVisible(false);
            this.pool.push(img);
        }
    }

    spawn(x, y, weaponData) {
        const img = this.pool.find(i => !i.active);
        if (!img) return;

        const options = WEAPON_ONOMATOPEIAS[weaponData.id] || ['pow'];
        const frameName = Phaser.Math.RND.pick(options);

        img.setFrame(frameName);
        img.setPosition(x + Phaser.Math.Between(-20, 20), y);
        img.setScale(0.5).setAlpha(1).setAngle(Phaser.Math.Between(-15, 15));
        img.setActive(true).setVisible(true);

        img.scene.tweens.add({
            targets: img,
            scaleX: 1.2,
            scaleY: 1.2,
            alpha: 0,
            duration: 400,
            ease: 'Back.easeOut',
            onComplete: () => {
                img.setActive(false).setVisible(false).setPosition(-1000, -1000);
            }
        });
    }

    spawnKill(x, y) {
        // TALKEI especial no kill -- maior, mais dramatico
        const img = this.pool.find(i => !i.active);
        if (!img) return;

        img.setFrame('talkei');
        img.setPosition(x, y - 20).setScale(0.3).setAlpha(1).setAngle(0);
        img.setActive(true).setVisible(true);

        img.scene.tweens.add({
            targets: img,
            scaleX: 2.0,
            scaleY: 2.0,
            alpha: 0,
            duration: 700,
            ease: 'Bounce.easeOut',
            onComplete: () => {
                img.setActive(false).setVisible(false).setPosition(-1000, -1000);
            }
        });
    }
}
```

### 5.4 Ink Particles: Blood Estilo Andre Guedes

O efeito de sangue-tinta e o detalhe visual mais identitario do Andre Guedes. Pixels vermelhos dispersando em angulo de golpe. O `inkSplats` no atlas tem 4 frames de manchas diferentes.

```javascript
// Configuracao do emitter de tinta (criado no GameScene.create())
this.inkEmitter = this.add.particles(0, 0, 'particles', {
    frame: { frames: ['ink_splat_0', 'ink_splat_1', 'ink_splat_2', 'ink_splat_3'], cycle: false },
    lifespan: { min: 250, max: 500 },
    speed: { min: 60, max: 180 },
    angle: { min: -30, max: 30 }, // angulo ajustado no emit por direcao do golpe
    gravityY: 120,    // splats caem levemente (tinta e pesada)
    scale: { start: 0.8, end: 0.1 },
    alpha: { start: 1, end: 0 },
    tint: [0xC8381A, 0x8B1A10, 0xFF4422], // variacoes de vermelho
    quantity: 6,
    emitting: false,  // NUNCA emite automaticamente -- sempre manual
    depth: 650,
});

// No hit, chama:
hitEmit(x, y, dirX) {
    this.inkEmitter.setPosition(x, y);
    // Ajusta angulo baseado na direcao do golpe
    // Golpe da esquerda para direita = tinta voa para direita (0 a 60 graus)
    // Golpe da direita para esquerda = tinta voa para esquerda (120 a 180 graus)
    const baseAngle = dirX > 0 ? 20 : 160;
    this.inkEmitter.setEmitterAngle({ min: baseAngle - 40, max: baseAngle + 40 });
    this.inkEmitter.emitParticle(6);
}
```

---

## 6. Responsive Controls

### 6.1 Auto-Detect de Input Method

O sistema detecta automaticamente o metodo de input e adapta a UI. Nao pergunta para o usuario, nao mostra settings -- simplesmente observa qual input foi usado mais recentemente e adapta.

```javascript
// src/input/InputManager.js
export class InputManager {
    constructor(scene) {
        this.scene = scene;
        this._mode = 'keyboard'; // 'keyboard' | 'touch'
        this.direction = { x: 0 };
        this.attackPressed = false;
        this.powerUpPressed = false;

        // Keyboard
        this.keys = scene.input.keyboard.addKeys({
            left:    Phaser.Input.Keyboard.KeyCodes.LEFT,
            right:   Phaser.Input.Keyboard.KeyCodes.RIGHT,
            a:       Phaser.Input.Keyboard.KeyCodes.A,
            d:       Phaser.Input.Keyboard.KeyCodes.D,
            attack:  Phaser.Input.Keyboard.KeyCodes.Z,
            attack2: Phaser.Input.Keyboard.KeyCodes.X,
            powerUp: Phaser.Input.Keyboard.KeyCodes.SPACE,
        });

        // Touch (VirtualJoystick)
        this.joystick = new VirtualJoystick(scene);
        this.attackButton = new TouchButton(scene, 380, 210, 'button_attack', () => {
            this.attackPressed = true;
        });
        this.powerUpButton = new TouchButton(scene, 440, 175, 'button_powerup', () => {
            this.powerUpPressed = true;
        });

        // Deteccao de modo
        scene.input.on('pointerdown', () => this._setMode('touch'));
        scene.input.keyboard.on('keydown', () => this._setMode('keyboard'));
    }

    _setMode(mode) {
        if (this._mode === mode) return;
        this._mode = mode;

        // Mostra/esconde controles virtuais
        this.joystick.setVisible(mode === 'touch');
        this.attackButton.setVisible(mode === 'touch');
        this.powerUpButton.setVisible(mode === 'touch');
    }

    update() {
        // Reset de single-frame states
        this.attackPressed = false;
        this.powerUpPressed = false;

        if (this._mode === 'keyboard') {
            this._updateKeyboard();
        } else {
            this._updateTouch();
        }
    }

    _updateKeyboard() {
        let dx = 0;
        if (this.keys.left.isDown || this.keys.a.isDown) dx -= 1;
        if (this.keys.right.isDown || this.keys.d.isDown) dx += 1;
        this.direction = { x: dx };

        if (Phaser.Input.Keyboard.JustDown(this.keys.attack) ||
            Phaser.Input.Keyboard.JustDown(this.keys.attack2)) {
            this.attackPressed = true;
        }

        if (Phaser.Input.Keyboard.JustDown(this.keys.powerUp)) {
            this.powerUpPressed = true;
        }
    }

    _updateTouch() {
        this.direction = { x: this.joystick.x }; // -1 a 1 do joystick
        // attackPressed e powerUpPressed sao setados pelos TouchButton callbacks
    }
}
```

### 6.2 VirtualJoystick: Implementacao

VirtualJoystick dinamico (aparece onde o dedo toca, nao em posicao fixa). Este e o padrao de joystick que reduce fatiga -- o jogador nao precisa mover o polegar para uma posicao especifica.

```javascript
// src/input/VirtualJoystick.js
export class VirtualJoystick {
    constructor(scene) {
        this.scene = scene;
        this.x = 0; // -1 a 1, output normalizado
        this._visible = false;

        const DEAD_ZONE = 8;
        const MAX_RADIUS = 50;

        // Sprites do joystick no HUD (camera fixa, sem scroll)
        this.outer = scene.add.image(-200, -200, 'ui', 'joystick_outer')
            .setScrollFactor(0).setDepth(1010).setAlpha(0.7);
        this.inner = scene.add.image(-200, -200, 'ui', 'joystick_inner')
            .setScrollFactor(0).setDepth(1011).setAlpha(0.9);

        // Escala os botoes para 44px minimo (Apple HIG / Material Design)
        // joystick_outer = 88px no atlas (2x do minimo para conforto)
        this.outer.setScale(1); // assume 88px no atlas
        this.inner.setScale(0.5);

        let originX = 0, originY = 0;
        let activeId = null;

        // METADE ESQUERDA da tela = zona do joystick
        scene.input.on('pointerdown', (ptr) => {
            if (ptr.x > scene.scale.width * 0.5) return;
            if (activeId !== null) return;

            activeId = ptr.id;
            originX = ptr.x;
            originY = ptr.y;

            this.outer.setPosition(ptr.x, ptr.y).setAlpha(0.7);
            this.inner.setPosition(ptr.x, ptr.y).setAlpha(0.9);
        });

        scene.input.on('pointermove', (ptr) => {
            if (ptr.id !== activeId) return;
            const dx = ptr.x - originX;
            const dy = ptr.y - originY;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < DEAD_ZONE) {
                this.x = 0;
                this.inner.setPosition(originX, originY);
                return;
            }

            const normX = dx / dist;
            const clampedDist = Math.min(dist, MAX_RADIUS);
            this.x = normX; // apenas eixo X -- side-scroller e 1D

            this.inner.setPosition(
                originX + normX * clampedDist,
                originY + (dy / dist) * clampedDist
            );
        });

        scene.input.on('pointerup', (ptr) => {
            if (ptr.id !== activeId) return;
            activeId = null;
            this.x = 0;
            this.outer.setPosition(-200, -200);
            this.inner.setPosition(-200, -200);
        });
    }

    setVisible(visible) {
        this._visible = visible;
        if (!visible) {
            this.outer.setPosition(-200, -200);
            this.inner.setPosition(-200, -200);
        }
    }
}
```

### 6.3 TouchButton: Botoes de Acao Mobile

```javascript
// src/input/TouchButton.js
export class TouchButton {
    constructor(scene, x, y, frameKey, onPress) {
        // Tamanho minimo 44px conforme HIG. Em viewport 480px, usamos 48px.
        this.hitArea = scene.add.rectangle(x, y, 48, 48, 0xFFFFFF, 0)
            .setScrollFactor(0).setDepth(1012).setInteractive();

        this.visual = scene.add.image(x, y, 'ui', frameKey)
            .setScrollFactor(0).setDepth(1011).setAlpha(0.85);

        this.hitArea.on('pointerdown', () => {
            onPress();
            // Feedback visual de pressionado: escurece levemente
            scene.tweens.add({
                targets: this.visual,
                alpha: 0.5,
                scaleX: 0.9,
                scaleY: 0.9,
                duration: 50,
                yoyo: true,
                onComplete: () => {
                    this.visual.setAlpha(0.85).setScale(1);
                }
            });
        });
    }

    setVisible(visible) {
        this.hitArea.setVisible(visible);
        this.visual.setVisible(visible);
    }
}
```

### 6.4 Desktop Key Mapping

```
Movimento:     WASD ou Setas
Ataque melee:  Z ou X ou Click esquerdo
Ataque ranged: E ou Click direito
Trocar arma:   Q ou scroll do mouse
Power-up:      Espaco ou F
Pause:         Escape ou P
```

A decisao de ataque manual (nao automatico como no plano anterior top-down) e especifica do side-view: em side-view, o jogador precisa de controle sobre quando atacar para gerenciar o fluxo da horde. O ataque automatico nesse contexto tira o controle em momentos criticos (ex: quando voce quer recuar antes de atacar).

---

## 7. Integration: React + Phaser

### 7.1 Montagem do Phaser dentro do React

```javascript
// src/components/GameCanvas.jsx
import { useEffect, useRef } from 'react';
import Phaser from 'phaser';
import { BootScene } from '../scenes/BootScene';
import { PreloadScene } from '../scenes/PreloadScene';
import { MenuScene } from '../scenes/MenuScene';
import { GameScene } from '../scenes/GameScene';
import { GameOverScene } from '../scenes/GameOverScene';

export function GameCanvas({ onScoreUpdate, onGameOver }) {
    const containerRef = useRef(null);
    const gameRef = useRef(null);

    useEffect(() => {
        if (gameRef.current) return; // StrictMode double-mount guard

        const config = {
            type: Phaser.WEBGL,
            width: 480,
            height: 270,
            parent: containerRef.current,
            backgroundColor: '#1A1A18',
            pixelArt: true,       // CRITICO: desativa anti-aliasing para pixel art
            roundPixels: true,    // evita sub-pixel blurring
            physics: {
                default: 'arcade',
                arcade: {
                    gravity: { y: 0 }, // side-scroller plano, sem gravidade global
                    debug: false,      // nunca ligar em producao
                }
            },
            scale: {
                mode: Phaser.Scale.FIT,        // escala mantendo aspect ratio
                autoCenter: Phaser.Scale.CENTER_BOTH,
                min: { width: 320, height: 180 },
                max: { width: 1920, height: 1080 },
            },
            scene: [BootScene, PreloadScene, MenuScene, GameScene, GameOverScene],
            callbacks: {
                postBoot: (game) => {
                    // Injeta callbacks do React no registry do Phaser
                    game.registry.set('onScoreUpdate', onScoreUpdate);
                    game.registry.set('onGameOver', onGameOver);
                }
            }
        };

        gameRef.current = new Phaser.Game(config);

        return () => {
            gameRef.current?.destroy(true);
            gameRef.current = null;
        };
    }, []); // sem dependencies -- instancia unica durante o lifecycle do componente

    return (
        <div
            ref={containerRef}
            style={{
                width: '100%',
                height: '100%',
                touchAction: 'none', // previne scroll do browser durante touch no canvas
            }}
        />
    );
}
```

### 7.2 HUD como React Overlay

O HUD (HP, score, wave counter, combo) vive em React, fora do Phaser. Comunicacao via `game.registry` (observer pattern) para nao criar acoplamento direto.

```javascript
// src/components/GameHUD.jsx
import { useState, useEffect } from 'react';

export function GameHUD({ gameRef }) {
    const [hp, setHp] = useState(100);
    const [score, setScore] = useState(0);
    const [wave, setWave] = useState(1);
    const [combo, setCombo] = useState(0);
    const [weapon, setWeapon] = useState('chinelo');

    useEffect(() => {
        const game = gameRef.current;
        if (!game) return;

        // Escuta eventos do Phaser Registry
        const onHpChange = (parent, value) => setHp(value);
        const onScoreChange = (parent, value) => setScore(value);
        const onWaveChange = (parent, value) => setWave(value);
        const onComboChange = (parent, value) => setCombo(value);
        const onWeaponChange = (parent, value) => setWeapon(value);

        game.registry.events.on('changedata-hp', onHpChange);
        game.registry.events.on('changedata-score', onScoreChange);
        game.registry.events.on('changedata-wave', onWaveChange);
        game.registry.events.on('changedata-combo', onComboChange);
        game.registry.events.on('changedata-weapon', onWeaponChange);

        return () => {
            game.registry.events.off('changedata-hp', onHpChange);
            game.registry.events.off('changedata-score', onScoreChange);
            game.registry.events.off('changedata-wave', onWaveChange);
            game.registry.events.off('changedata-combo', onComboChange);
            game.registry.events.off('changedata-weapon', onWeaponChange);
        };
    }, [gameRef]);

    return (
        <div style={styles.hud}>
            <HpBar current={hp} max={100} />
            <ScoreDisplay score={score} combo={combo} />
            <WaveBadge wave={wave} />
            <WeaponIcon weapon={weapon} />
        </div>
    );
}

const styles = {
    hud: {
        position: 'absolute',
        top: 0, left: 0, right: 0, bottom: 0,
        pointerEvents: 'none', // HUD nao intercepta cliques/touches do jogo
        userSelect: 'none',
    }
};
```

---

## 8. Implementation Sprint: 10 Dias

### D1 -- Scaffold + Boot/Preload

**Meta:** Phaser rodando dentro do React, tela de loading funcional.

Tarefas:
- `npm create vite@latest zumbis-brasilia -- --template react`
- Instala Phaser 3.88: `npm i phaser@3.88.0`
- Cria `GameCanvas.jsx` com config basica (480x270, WEBGL, pixelArt: true)
- Cria `BootScene.js` (adiciona font, define constantes globais)
- Cria `PreloadScene.js` com progress bar primitiva
- Cria assets placeholder (retangulos coloridos) para testar sem PNG final
- Verifica 60fps no Chrome DevTools Performance
- **Criterio de aceite:** progress bar aparece, transiciona para tela preta

Arquivos criados: `src/scenes/BootScene.js`, `PreloadScene.js`, `src/components/GameCanvas.jsx`, `vite.config.js` com `assetsInclude` para PNGs

### D2 -- Parallax + Camera + Segment Loading

**Meta:** Esplanada visivel com todos os 7 layers scrollando.

Tarefas:
- Cria `GameScene.js` com todos os layers (usando placeholders de cor)
- Implementa `parallaxUpdate()` com tilePositionX correto
- Configura camera com `startFollow`, `setBounds`, `setDeadzone`
- Implementa `SegmentManager.js` com crossfade de 800ms
- Adiciona player placeholder (retangulo 16x36) com movimento basico para testar parallax
- Testa: scroll a 120px/s, verifica que layers seguem scrollFactor correto
- **Criterio de aceite:** 7 layers visiveis, parallax correto, sem tearing

### D3 -- Player Controller + Animacoes

**Meta:** Player sprite com state machine completa rodando.

Tarefas:
- Importa primeiros sprites do PixelLab (player completo)
- Empacota com TexturePacker em `atlas_characters.json`
- Cria `Player.js` com a classe completa desta doc
- Registra animacoes em `src/anims/registerAnims.js`
- Implementa `InputManager.js` (keyboard apenas por enquanto)
- Conecta input ao player no `GameScene.update()`
- Testa: idle/run/flip, aceleracao/desaceleracao
- **Criterio de aceite:** personagem anda suavemente, para suavemente, flip correto

### D4 -- Zombie Pool + AI Basica

**Meta:** Vereadores spawnam nas bordas e andam ate o player.

Tarefas:
- Importa sprites dos primeiros 2 tipos de zumbi (vereador, assessor)
- Cria `Zombie.js` com a classe desta doc
- Cria `ZombiePool.js` com pool de 30 instancias
- Cria `WaveSystem.js` com Wave 1 (apenas vereadores)
- Configura `Arcade.addCollider()` entre player e zombies
- Testa: 10 vereadores na tela, todos andam, pool funciona (sem alocacao nova)
- **Criterio de aceite:** 30 zumbis ativos sem frame drop, pool confirmado via profiler

### D5 -- Combat System + Hit Feel

**Meta:** Atacar um zumbi deveParecer Peso. Cada hit deve ter impacto fisico.

Tarefas:
- Cria `CombatSystem.js` com hitbox melee temporal
- Cria `CombatFeedback.js` com toda a sequencia desta doc
- Cria `DamageNumberPool.js` e `OnomatopeiaPool.js`
- Configura ink particles
- Implementa hit stop (timeScale 0.05 por 50ms)
- Implementa flash branco (setTintFill)
- Implementa knockback
- Implementa screen shake
- Testa: ataca um zumbi 20 vezes. Cada hit deve sentir diferente (pitch variation, random onomatopeia)
- **Criterio de aceite (subjetivo):** mostrar para alguem que nao sabe do projeto. Se a pessoa sorrir no hit, passou.

### D6 -- Wave System + Spawning

**Meta:** Jogo progride por waves, density management funciona.

Tarefas:
- Expande `WaveSystem.js` com config de Waves 1-10
- Implementa spawn das bordas
- Implementa spawn das ministry doors (posicoes no Tiled)
- Implementa density cap (maxActive por wave)
- Implementa timer de wave (30s por wave, +5s por wave)
- Testa: jogar por 5 waves sem frame drop
- **Criterio de aceite:** Wave 5 tem 20 zumbis ativos, FPS estavel em 60

### D7 -- HUD + Score + React Overlay

**Meta:** Interface completa do jogo visivel e atualizada em tempo real.

Tarefas:
- Cria `GameHUD.jsx` com os 4 elementos (HP, Score, Wave, Combo)
- Conecta via `game.registry` como documentado
- Sistema de Combo: hits em sequencia sem levar dano multiplica score
- Cria `GameOverScene.js` e `GameOverScreen.jsx`
- Implementa high score com localStorage
- Testa: score atualiza sem lag visivelna tela, combo quebra corretamente ao levar dano
- **Criterio de aceite:** HP bar nao pisca (sem React re-render desnecessario)

### D8 -- Weapons + Power-ups

**Meta:** 3 armas funcionais, 2 power-ups.

Tarefas:
- Implementa `chinelo` (melee basico, ja existe), `vassoura` (melee longo alcance, 32px hitbox), `urna` (ranged arremessado)
- Cria `ProjectilePool.js` para urnas e crachas
- Implementa 2 power-ups: Chinelada Sagrada (damage x3 por 5s), Urna Invicta (ranged infinito por 5s)
- Pickups dropam de zumbis com chance 5%
- Testa: troca de arma durante combate, projeteis collidindo com zumbis
- **Criterio de aceite:** urna acerta zumbi a 150px de distancia, colisao correta

### D9 -- Mobile Controls + Testing

**Meta:** Jogo jogavel no celular em landscape.

Tarefas:
- Implementa `VirtualJoystick.js` e `TouchButton.js` desta doc
- Adiciona `touchAction: 'none'` no container e previne eventos de browser
- Testa em dispositivo real (iPhone Safari + Android Chrome obrigatorios)
- Verifica 44px minimo de touch targets
- Verifica que joystick nao causa scroll da pagina
- Ajusta posicao dos botoes para nao sobrepor a acao central
- **Criterio de aceite:** 5 minutos de jogo no celular sem mao cansar, sem input perdido

### D10 -- Polish, Bug Fix, Deploy

**Meta:** Jogo publicado e jogavel por alguem de fora do time.

Tarefas:
- Audit de FPS: Profile no Chrome em CPU 4x throttle (simula hardware medio)
- Comprime atlas com pngquant (sem perda visual em pixel art)
- Configura Vite `build` com code splitting
- Configura `vite-plugin-compression` para gzip/brotli dos assets
- Deploy no Netlify ou Vercel (build estatico, CDN automatico)
- Testa o link em 3 celulares diferentes
- Fix dos bugs encontrados no D9
- **Criterio de aceite:** link funciona, jogo carrega em menos de 5s em 4G

---

## Apendice A: Constantes do Projeto

```javascript
// src/constants.js
export const VIEWPORT = { W: 480, H: 270 };
export const GROUND_Y = 210;       // Y do topo do chao (em coords de nivel)
export const HORIZON_Y = 120;      // Y da linha do horizonte
export const LEVEL_W = 9600;       // largura total do nivel em pixels
export const SEGMENT_W = 1920;     // largura de cada segmento
export const SCALE = 2;            // fator de escala CSS (2x = 960x540 na tela)

// Depth constants (uma constante por layer evita magic numbers)
export const DEPTH = {
    SKY:              -1000,
    CONGRESS:          -900,
    MINISTRIES_DIST:   -800,
    MINISTRIES_NEAR:   -600,
    BG_OBJECTS:        -400,
    GROUND:               0,
    PICKUPS:            100,
    ZOMBIES_FAR:        200,
    PLAYER:             300,
    ZOMBIES_NEAR:       400,
    PROJECTILES:        500,
    VFX_LOW:            600,
    ONOMATOPEIAS:       750,
    VFX_HIGH:           800,
    FOREGROUND:         900,
    HUD:               1000,
    JOYSTICK:          1010,
};

export const ZOMBIE_CONFIGS = {
    vereador:  { hp: 30,  speed: 50,  damage: 10, score: 10,  attackCooldown: 1500, hitboxW: 18, hitboxH: 34 },
    assessor:  { hp: 20,  speed: 90,  damage: 8,  score: 8,   attackCooldown: 1200, hitboxW: 14, hitboxH: 34 },
    senador:   { hp: 80,  speed: 30,  damage: 20, score: 25,  attackCooldown: 2000, hitboxW: 24, hitboxH: 40 },
    lobista:   { hp: 50,  speed: 60,  damage: 15, score: 20,  attackCooldown: 2000, hitboxW: 20, hitboxH: 36, attackRange: 300 },
};
```

---

## Apendice B: Performance Budget

| Metrica | Target | Hard Limit |
|---|---|---|
| FPS | 60fps constante | Nenhum frame abaixo de 30fps |
| Draw calls por frame | menos de 15 | 25 |
| Zumbis ativos simultaneos | ate 30 | 50 (pool size) |
| Particulas ativas | ate 40 | 65 |
| Atlas size | 4x 2048px | sem 4096px (risco de compat.) |
| JS bundle inicial | menor que 200kb gzip | 400kb |
| Assets total (packed) | menor que 8MB | 20MB |
| Tempo de carregamento (4G) | menor que 5s | 10s |
| Memoria JS heap (mid-game) | menor que 80MB | 120MB |

---

*Cada frame de animacao conta. Cada hit precisa ter peso e impacto. Um jogador que nunca tocou no jogo deve sentir o chinelo chegando antes de ouvir o THWACK. Isso e o game feel. Isso e o trabalho.*
