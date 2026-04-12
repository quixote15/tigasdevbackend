# ZUMBIS DE BRASILIA -- Arquitetura Tecnica: React + Phaser 3.88 Side-Scroller
### John Carmack -- CTO & Arquitetura de Engenharia | Abril 2026

---

> *"Phaser dentro de React e como colocar um motor V8 dentro de um chassi que ja tem painel, ar-condicionado e GPS. O React cuida da experiencia ao redor do jogo -- menus, HUD overlay, login, rankings. O Phaser cuida do que importa: renderizar 50 zumbis de terno a 60fps enquanto um chinelo voa pela Esplanada. A fronteira entre os dois precisa ser cirurgica. Uma funcao de callback. Um EventEmitter. Nada mais. Se voce esta passando state do Redux pro game loop, voce errou."*

---

## 0. Contexto desta Revisao

O documento 12 (Tech Strategy MVP Web) definiu a stack correta: Phaser 3.88, TypeScript, Vite, Cloudflare Pages. Zero backend. Tudo client-side. Isso continua valido.

O que mudou:

| Aspecto | Doc 12 (Anterior) | Doc 19 (Este) |
|---|---|---|
| **Perspectiva** | Top-down (Vampire Survivors) | Side-view (Metal Slug) |
| **Framework UI** | Phaser-only (tudo no canvas) | React + Phaser (React para UI, Phaser para gameplay) |
| **Backend** | Zero | Minimo viavel: Auth (Google login/guest) + Rankings (leaderboard) |
| **Viewport** | 720x1280 portrait | 480x270 logico, landscape |
| **Physics** | Arcade (AABB generico) | Arcade (AABB otimizado para side-view com gravidade) |
| **Layers** | Simples (poucas camadas) | 7 parallax layers + foreground + HUD |
| **Input** | Touch joystick + keyboard | Virtual joystick (mobile) + WASD/Space (desktop) |

Os principios nao mudam: simplicidade radical, ship first, otimizar para o pior caso (Galaxy A06 Chrome), object pooling everywhere, zero alocacoes no game loop.

---

## 1. Arquitetura React + Phaser 3.88

### 1.1 Principio Fundamental: Separacao Cirurgica

React e Phaser vivem em universos diferentes. React vive no DOM. Phaser vive num canvas WebGL. Eles nao devem se conhecer intimamente. A comunicacao entre eles e um tubo fino -- um EventEmitter -- e nada mais.

```
React (DOM)                          Phaser (Canvas WebGL)
┌──────────────────────┐             ┌──────────────────────┐
│  App.tsx             │             │  Game Instance        │
│  ├── MainMenu        │  ────────>  │  ├── BootScene       │
│  ├── PhaserGame ─────│─ useRef ──> │  ├── PreloadScene    │
│  │   (container div) │             │  ├── GameScene        │
│  ├── HUDOverlay      │  <──────── │  │   ├── Player       │
│  ├── PauseMenu       │  events    │  │   ├── ZombiePool   │
│  ├── GameOverScreen  │             │  │   ├── Projectiles  │
│  ├── LeaderboardPage │             │  │   └── Parallax     │
│  └── LoginPage       │             │  └── GameOverScene    │
└──────────────────────┘             └──────────────────────┘
         │                                      │
         │         EventBus (mitt)              │
         └──────────────────────────────────────┘
```

**Regra de ouro:** React NUNCA acessa `this.scene` diretamente. Phaser NUNCA manipula o DOM. Toda comunicacao passa pelo EventBus.

### 1.2 Componente PhaserGame

```typescript
// src/components/PhaserGame.tsx
import { useRef, useEffect, forwardRef, useImperativeHandle } from 'react';
import Phaser from 'phaser';
import { gameConfig } from '../phaser/config';
import { EventBus } from '../events/EventBus';

export interface PhaserGameRef {
  game: Phaser.Game | null;
  scene: Phaser.Scene | null;
}

export const PhaserGame = forwardRef<PhaserGameRef>((_props, ref) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const gameRef = useRef<Phaser.Game | null>(null);

  useImperativeHandle(ref, () => ({
    get game() { return gameRef.current; },
    get scene() {
      return gameRef.current?.scene.getScene('GameScene') ?? null;
    }
  }));

  useEffect(() => {
    if (!containerRef.current || gameRef.current) return;

    const config: Phaser.Types.Core.GameConfig = {
      ...gameConfig,
      parent: containerRef.current,
    };

    gameRef.current = new Phaser.Game(config);

    // Cleanup: destruir Phaser quando React desmonta
    return () => {
      if (gameRef.current) {
        gameRef.current.destroy(true);
        gameRef.current = null;
        EventBus.all.clear();
      }
    };
  }, []);

  return (
    <div
      ref={containerRef}
      id="phaser-container"
      style={{
        width: '100%',
        height: '100%',
        position: 'absolute',
        top: 0,
        left: 0,
      }}
    />
  );
});
```

### 1.3 EventBus (mitt -- 200 bytes)

```typescript
// src/events/EventBus.ts
import mitt from 'mitt';

type GameEvents = {
  // Phaser -> React
  'score-update': { score: number; combo: number };
  'hp-update': { current: number; max: number };
  'wave-update': { wave: number; totalWaves: number };
  'game-over': { score: number; kills: number; wave: number; time: number };
  'scene-ready': { scene: string };

  // React -> Phaser
  'start-game': { skinVariant: number };
  'pause-game': void;
  'resume-game': void;
  'restart-game': void;
  'mute-toggle': { muted: boolean };
};

export const EventBus = mitt<GameEvents>();
```

**Por que mitt e nao o EventEmitter do Phaser?** Porque mitt e framework-agnostico (200 bytes), type-safe com TypeScript generics, e nao cria dependencia do Phaser no lado React. O EventEmitter do Phaser esta acoplado a instancia da Scene -- se a Scene for destruida, os listeners somem. mitt vive independente.

### 1.4 Phaser emitindo para React

```typescript
// src/phaser/scenes/GameScene.ts
import { EventBus } from '../../events/EventBus';

export class GameScene extends Phaser.Scene {
  private score = 0;
  private combo = 0;

  create() {
    // ... setup do jogo ...
    EventBus.emit('scene-ready', { scene: 'GameScene' });
  }

  onZombieKilled() {
    this.score += 100 * this.combo;
    this.combo++;
    // Emite para o React atualizar o HUD overlay
    EventBus.emit('score-update', {
      score: this.score,
      combo: this.combo,
    });
  }

  onPlayerHit(damage: number) {
    this.player.hp -= damage;
    EventBus.emit('hp-update', {
      current: this.player.hp,
      max: this.player.maxHp,
    });
  }

  onGameOver() {
    EventBus.emit('game-over', {
      score: this.score,
      kills: this.killCount,
      wave: this.currentWave,
      time: this.elapsedTime,
    });
  }
}
```

### 1.5 React ouvindo Phaser

```typescript
// src/components/HUDOverlay.tsx
import { useState, useEffect } from 'react';
import { EventBus } from '../events/EventBus';

export function HUDOverlay() {
  const [score, setScore] = useState(0);
  const [combo, setCombo] = useState(0);
  const [hp, setHp] = useState({ current: 100, max: 100 });
  const [wave, setWave] = useState({ wave: 1, totalWaves: 15 });

  useEffect(() => {
    const onScore = (data: { score: number; combo: number }) => {
      setScore(data.score);
      setCombo(data.combo);
    };
    const onHp = (data: { current: number; max: number }) => {
      setHp(data);
    };
    const onWave = (data: { wave: number; totalWaves: number }) => {
      setWave(data);
    };

    EventBus.on('score-update', onScore);
    EventBus.on('hp-update', onHp);
    EventBus.on('wave-update', onWave);

    return () => {
      EventBus.off('score-update', onScore);
      EventBus.off('hp-update', onHp);
      EventBus.off('wave-update', onWave);
    };
  }, []);

  return (
    <div className="hud-overlay" style={{
      position: 'absolute',
      top: 0,
      left: 0,
      width: '100%',
      pointerEvents: 'none', // Cliques passam direto pro canvas
      zIndex: 10,
    }}>
      <div className="hud-score">Score: {score}</div>
      <div className="hud-combo">{combo > 1 ? `${combo}x COMBO` : ''}</div>
      <div className="hud-hp">
        <div className="hp-bar" style={{
          width: `${(hp.current / hp.max) * 100}%`
        }} />
      </div>
      <div className="hud-wave">Wave {wave.wave}/{wave.totalWaves}</div>
    </div>
  );
}
```

### 1.6 React comandando Phaser

```typescript
// src/components/MainMenu.tsx
import { EventBus } from '../events/EventBus';

export function MainMenu() {
  const [skinVariant, setSkinVariant] = useState(0);

  const handleStartGame = () => {
    EventBus.emit('start-game', { skinVariant });
  };

  return (
    <div className="main-menu">
      <h1>CONGRESSO DOS MORTOS</h1>
      <SkinSelector value={skinVariant} onChange={setSkinVariant} />
      <button onClick={handleStartGame}>JOGAR</button>
    </div>
  );
}
```

### 1.7 App Root: Orquestracao

```typescript
// src/App.tsx
import { useRef, useState, useEffect } from 'react';
import { PhaserGame, PhaserGameRef } from './components/PhaserGame';
import { MainMenu } from './components/MainMenu';
import { HUDOverlay } from './components/HUDOverlay';
import { GameOverScreen } from './components/GameOverScreen';
import { LoginPage } from './components/LoginPage';
import { LeaderboardPage } from './components/LeaderboardPage';
import { EventBus } from './events/EventBus';

type AppState = 'login' | 'menu' | 'playing' | 'gameover' | 'leaderboard';

export function App() {
  const phaserRef = useRef<PhaserGameRef>(null);
  const [appState, setAppState] = useState<AppState>('menu');
  const [gameOverData, setGameOverData] = useState(null);

  useEffect(() => {
    EventBus.on('scene-ready', ({ scene }) => {
      if (scene === 'GameScene') setAppState('playing');
    });
    EventBus.on('game-over', (data) => {
      setGameOverData(data);
      setAppState('gameover');
    });
    return () => {
      EventBus.off('scene-ready');
      EventBus.off('game-over');
    };
  }, []);

  return (
    <div id="app" style={{ width: '100vw', height: '100vh', position: 'relative' }}>
      {/* Phaser canvas -- SEMPRE montado, visibilidade controlada por CSS */}
      <PhaserGame ref={phaserRef} />

      {/* React UI layers -- renderizacao condicional */}
      {appState === 'login' && <LoginPage />}
      {appState === 'menu' && <MainMenu />}
      {appState === 'playing' && <HUDOverlay />}
      {appState === 'gameover' && <GameOverScreen data={gameOverData} />}
      {appState === 'leaderboard' && <LeaderboardPage />}
    </div>
  );
}
```

### 1.8 Por que React para UI e nao tudo no Canvas

| Aspecto | UI no Canvas (Phaser) | UI no DOM (React) |
|---|---|---|
| **Texto** | Bitmap fonts, sem quebra de linha nativa, sem scroll | CSS fonts, text-overflow, scroll nativo |
| **Formularios (login)** | Precisa de DOM overlay de qualquer forma | Nativo |
| **Responsividade** | Manual (calcular posicoes para cada resolucao) | CSS flexbox/grid, media queries |
| **Animacoes de UI** | Tweens do Phaser (OK mas limitado) | CSS transitions, framer-motion |
| **Acessibilidade** | Zero | Screen readers, ARIA, tab navigation |
| **Leaderboard (tabela scrollable)** | Pesadelo no canvas | `<table>` com overflow-y: auto |
| **Performance** | Cada pixel de UI e um draw call a mais | DOM e free -- browser ja renderiza |
| **Dev experience** | Layouts manuais com x,y absolutos | JSX + CSS = 10x mais rapido de iterar |

**Conclusao:** Menus, login, leaderboard, HUD texto e Game Over screen sao DOM puro via React. O canvas do Phaser renderiza APENAS gameplay: sprites, tiles, particulas, fisica.

---

## 2. Phaser 3.88 Side-Scroller Architecture

### 2.1 Game Config

```typescript
// src/phaser/config.ts
import Phaser from 'phaser';
import { BootScene } from './scenes/BootScene';
import { PreloadScene } from './scenes/PreloadScene';
import { GameScene } from './scenes/GameScene';

export const GAME_WIDTH = 480;
export const GAME_HEIGHT = 270;

export const gameConfig: Phaser.Types.Core.GameConfig = {
  type: Phaser.WEBGL,
  width: GAME_WIDTH,
  height: GAME_HEIGHT,
  pixelArt: true, // Nearest neighbor scaling, sem antialiasing
  roundPixels: true, // Sem sub-pixel rendering -- crispy pixels
  antialias: false,
  backgroundColor: '#1a0a0a',
  scale: {
    mode: Phaser.Scale.FIT, // Escala mantendo aspect ratio
    autoCenter: Phaser.Scale.CENTER_BOTH,
    // FIT, nao RESIZE. O viewport logico e SEMPRE 480x270.
    // O Phaser escala o canvas inteiro via CSS transform.
    // Isso garante pixel-perfect em qualquer resolucao.
  },
  physics: {
    default: 'arcade',
    arcade: {
      gravity: { x: 0, y: 0 }, // Zero gravity -- side-scroller, nao platformer
      // Personagens andam no chao, nao pulam.
      // Sem gravidade = sem necessidade de ground check.
      debug: false, // true em dev, false em prod
      // Otimizacoes de physics:
      tileBias: 16, // Tamanho do tile para colisao otimizada
      overlapBias: 4, // Tolerancia de overlap (evita tunneling)
    },
  },
  scene: [BootScene, PreloadScene, GameScene],
  // Sem MenuScene nem GameOverScene -- React cuida disso
  render: {
    batchSize: 4096, // Max sprites por batch (default 4096, bom para nos)
    maxTextures: 8, // Max texture units do GPU (Galaxy A06 Mali-G52 tem 8)
    // Phaser auto-detect mas definir explicitamente evita probing overhead
  },
  input: {
    activePointers: 3, // Max 3 toques simultaneos (joystick + 2 botoes)
  },
  banner: false, // Remove o banner do console do Phaser
  fps: {
    target: 60,
    forceSetTimeOut: false, // Usa requestAnimationFrame (melhor)
  },
};
```

**Por que `gravity: { y: 0 }` e nao `{ y: 300 }`?** Porque este jogo NAO e um platformer. O Andre Guedes definiu: "Superficie plana, sem plataformas elevadas no MVP -- nao e platformer." Os personagens caminham horizontalmente no chao. Sem pulo, sem queda, sem plataformas. Adicionar gravidade significa adicionar ground collision detection, landing logic, coyote time -- complexidade gratuita para um horde shooter de lado. Metal Slug tem gravidade porque tem pulo. Nos nao temos pulo. Zero gravity. Simples.

### 2.2 Scene Structure

```
BootScene          -> Carrega assets minimos (logo, progress bar)
     |
PreloadScene       -> Carrega todos os assets (atlas, tilemaps, audio)
     |                Mostra barra de progresso
     |
GameScene          -> Gameplay principal
     |                - 7 parallax layers
     |                - Player + enemies + projectiles
     |                - Arcade Physics
     |                - Camera follow
     |                - Emite eventos para React (score, hp, wave, gameover)
```

**Nota:** Nao existe MenuScene nem GameOverScene no Phaser. React renderiza essas telas como componentes DOM sobre o canvas. O Phaser so tem 3 scenes: Boot, Preload, Game. Menos scenes = menos transicoes = menos bugs de lifecycle.

### 2.3 Scene Lifecycle

```typescript
// src/phaser/scenes/BootScene.ts
export class BootScene extends Phaser.Scene {
  constructor() {
    super('BootScene');
  }

  preload() {
    // APENAS o logo e a imagem da barra de progresso
    this.load.image('logo', 'assets/ui/logo.png');
    this.load.image('progress-bar', 'assets/ui/progress-bar.png');
  }

  create() {
    this.scene.start('PreloadScene');
  }
}

// src/phaser/scenes/PreloadScene.ts
export class PreloadScene extends Phaser.Scene {
  constructor() {
    super('PreloadScene');
  }

  preload() {
    // Progress bar visual
    const bar = this.add.image(240, 135, 'progress-bar');
    this.load.on('progress', (value: number) => {
      bar.setCrop(0, 0, bar.width * value, bar.height);
    });

    // === SPRITE ATLASES ===
    this.load.atlas('characters', 'assets/sprites/characters.png', 'assets/sprites/characters.json');
    this.load.atlas('zombies', 'assets/sprites/zombies.png', 'assets/sprites/zombies.json');
    this.load.atlas('projectiles', 'assets/sprites/projectiles.png', 'assets/sprites/projectiles.json');
    this.load.atlas('vfx', 'assets/sprites/vfx.png', 'assets/sprites/vfx.json');
    this.load.atlas('ui-game', 'assets/sprites/ui-game.png', 'assets/sprites/ui-game.json');

    // === TILEMAP ===
    this.load.tilemapTiledJSON('esplanada-map', 'assets/tilemap/esplanada-sideview.json');
    this.load.image('esplanada-tiles', 'assets/tilemap/esplanada-sideview.png');

    // === BACKGROUNDS (parallax) ===
    this.load.image('congresso-sideview', 'assets/bg/congresso-320x120.png');
    this.load.image('ministerios-distantes', 'assets/bg/ministerios-dist-1920x120.png');
    this.load.image('ministerios-proximos', 'assets/bg/ministerios-prox-2400x180.png');

    // === AUDIO ===
    this.load.audio('music-main', ['assets/audio/music-main.ogg', 'assets/audio/music-main.mp3']);
    this.load.audio('sfx-hit', ['assets/audio/sfx-hit.ogg', 'assets/audio/sfx-hit.mp3']);
    this.load.audio('sfx-death', ['assets/audio/sfx-death.ogg', 'assets/audio/sfx-death.mp3']);
    this.load.audio('sfx-powerup', ['assets/audio/sfx-powerup.ogg', 'assets/audio/sfx-powerup.mp3']);
    this.load.audio('sfx-combo', ['assets/audio/sfx-combo.ogg', 'assets/audio/sfx-combo.mp3']);
  }

  create() {
    this.scene.start('GameScene');
  }
}
```

### 2.4 GameScene: 7 Parallax Layers

```typescript
// src/phaser/scenes/GameScene.ts
import { EventBus } from '../../events/EventBus';
import { GAME_WIDTH, GAME_HEIGHT } from '../config';
import { ZombiePool } from '../entities/ZombiePool';
import { ProjectilePool } from '../entities/ProjectilePool';
import { VFXPool } from '../entities/VFXPool';
import { Player } from '../entities/Player';

const LEVEL_WIDTH = 9600; // 600 tiles x 16px
const HORIZON_Y = 120;    // Linha do horizonte no viewport
const GROUND_Y = 190;     // Topo do chao (onde entidades andam)

export class GameScene extends Phaser.Scene {
  private player!: Player;
  private zombiePool!: ZombiePool;
  private projectilePool!: ProjectilePool;
  private vfxPool!: VFXPool;

  // Parallax layers que precisam de update manual
  private distantMinistries!: Phaser.GameObjects.TileSprite;
  private nearMinistries!: Phaser.GameObjects.TileSprite;

  constructor() {
    super('GameScene');
  }

  create() {
    // ================================================================
    // LAYER 0: CEU (scrollFactor 0 -- estatico)
    // ================================================================
    // Gradiente via Graphics -- zero texture, zero draw call adicional
    const sky = this.add.graphics();
    sky.fillGradientStyle(
      0xCC4400, 0xCC4400, // top: laranja-sangue
      0x1A0A0A, 0x1A0A0A, // bottom: preto
      1, 1, 1, 1
    );
    sky.fillRect(0, 0, GAME_WIDTH, HORIZON_Y);
    sky.setScrollFactor(0);
    sky.setDepth(-1000);

    // Nuvens toxicas: particulas lentas, semi-transparentes
    const cloudEmitter = this.add.particles(0, 0, 'vfx', {
      frame: 'cloud-toxic',
      x: { min: 0, max: GAME_WIDTH },
      y: { min: 20, max: 80 },
      lifespan: 20000,
      speedX: { min: 2, max: 5 },
      alpha: { start: 0.15, end: 0 },
      scale: { start: 1.5, end: 2.5 },
      frequency: 3000,
      quantity: 1,
    });
    cloudEmitter.setScrollFactor(0.05);
    cloudEmitter.setDepth(-995);

    // ================================================================
    // LAYER 1: CONGRESSO (scrollFactor 0.1)
    // ================================================================
    const congress = this.add.image(
      LEVEL_WIDTH / 2, // Centro do nivel -- o Congresso esta "la no fundo"
      HORIZON_Y,
      'congresso-sideview'
    );
    congress.setOrigin(0.5, 1); // Ancora na base
    congress.setScrollFactor(0.1);
    congress.setDepth(-900);

    // Brilho verde pulsante entre as torres
    const glow = this.add.pointlight(
      LEVEL_WIDTH / 2, HORIZON_Y - 60,
      0x3D6B3A, // verde
      80, 0.3, 0.05
    );
    glow.setScrollFactor(0.1);
    glow.setDepth(-899);
    // Pulso: amplitude suave
    this.tweens.add({
      targets: glow,
      intensity: { from: 0.2, to: 0.5 },
      duration: 3000,
      yoyo: true,
      repeat: -1,
      ease: 'Sine.easeInOut',
    });

    // ================================================================
    // LAYER 2: MINISTERIOS DISTANTES (scrollFactor 0.25)
    // ================================================================
    this.distantMinistries = this.add.tileSprite(
      0, HORIZON_Y - 120, // Posiciona acima do horizonte
      GAME_WIDTH, 120,
      'ministerios-distantes'
    );
    this.distantMinistries.setOrigin(0, 0);
    this.distantMinistries.setScrollFactor(0); // Manual parallax via tilePositionX
    this.distantMinistries.setDepth(-800);

    // ================================================================
    // LAYER 3: MINISTERIOS PROXIMOS (scrollFactor 0.5)
    // ================================================================
    this.nearMinistries = this.add.tileSprite(
      0, HORIZON_Y - 160,
      GAME_WIDTH, 180,
      'ministerios-proximos'
    );
    this.nearMinistries.setOrigin(0, 0);
    this.nearMinistries.setScrollFactor(0); // Manual parallax via tilePositionX
    this.nearMinistries.setDepth(-600);

    // ================================================================
    // LAYER 4: OBJETOS DE FUNDO (scrollFactor 0.75)
    // ================================================================
    this.createBackgroundObjects();

    // ================================================================
    // LAYER 5: CHAO / TILEMAP SIDE-SCROLLER (scrollFactor 1.0)
    // ================================================================
    const map = this.make.tilemap({ key: 'esplanada-map' });
    const tileset = map.addTilesetImage('esplanada-sideview', 'esplanada-tiles')!;

    // Superficie: onde os personagens andam
    const groundSurface = map.createLayer('ground-surface', tileset, 0, GROUND_Y)!;
    groundSurface.setDepth(0);
    groundSurface.setCollisionByProperty({ collides: true });

    // Subsolo: visual only, sem colisao
    const subsoil = map.createLayer('ground-subsurface', tileset, 0, GROUND_Y + 16)!;
    subsoil.setDepth(-1);

    // ================================================================
    // LAYER 6: ENTIDADES (scrollFactor 1.0)
    // ================================================================
    this.player = new Player(this, 100, GROUND_Y - 24); // 24px acima do chao (metade da altura do sprite)
    this.zombiePool = new ZombiePool(this, 50); // Pre-aloca 50 zumbis
    this.projectilePool = new ProjectilePool(this, 30); // Pre-aloca 30 projeteis
    this.vfxPool = new VFXPool(this, 40); // Pre-aloca 40 efeitos visuais

    // ================================================================
    // LAYER 7: FOREGROUND (scrollFactor 1.2-1.5)
    // ================================================================
    this.createForegroundElements();

    // ================================================================
    // PHYSICS COLLISIONS
    // ================================================================
    this.physics.add.collider(this.player, groundSurface);
    this.physics.add.overlap(
      this.projectilePool.group,
      this.zombiePool.group,
      this.onProjectileHitZombie,
      undefined,
      this
    );
    this.physics.add.overlap(
      this.player,
      this.zombiePool.group,
      this.onPlayerTouchZombie,
      undefined,
      this
    );

    // ================================================================
    // CAMERA
    // ================================================================
    this.cameras.main.startFollow(this.player, true, 0.08, 0.08);
    this.cameras.main.setBounds(0, 0, LEVEL_WIDTH, GAME_HEIGHT);
    this.cameras.main.setDeadzone(80, 20);
    // Deadzone: 80px horizontal = player pode andar 40px em cada
    // direcao sem a camera se mover. Evita camera "grudenta".
    // 20px vertical = quase nenhum jogo vertical, mas permite
    // micro-ajuste se o player sobe/desce por desnivel.

    // Notifica React que a cena esta pronta
    EventBus.emit('scene-ready', { scene: 'GameScene' });

    // Ouve comandos do React
    EventBus.on('pause-game', () => this.scene.pause());
    EventBus.on('resume-game', () => this.scene.resume());
    EventBus.on('restart-game', () => this.scene.restart());
    EventBus.on('mute-toggle', ({ muted }) => {
      this.sound.mute = muted;
    });
  }

  update(time: number, delta: number) {
    this.player.update(time, delta);
    this.zombiePool.update(time, delta);
    this.projectilePool.update(time, delta);

    // Parallax manual para TileSprites
    // (TileSprites com scrollFactor 0 precisam de offset manual)
    const camX = this.cameras.main.scrollX;
    this.distantMinistries.tilePositionX = camX * 0.25;
    this.nearMinistries.tilePositionX = camX * 0.5;
  }

  // ... collision handlers, wave spawner, etc.
}
```

### 2.5 Por que TileSprite com scrollFactor 0 + offset manual em vez de scrollFactor direto?

Quando voce usa `setScrollFactor(0.25)` num sprite normal, o Phaser move o sprite automaticamente com a camera. Funciona. Mas com `TileSprite`, se voce usar `setScrollFactor(0.25)`, o tile nao repete corretamente -- o Phaser move o SPRITE mas nao atualiza o `tilePositionX`, entao voce ve a textura se deslocando de forma errada.

A solucao correta: TileSprite com `scrollFactor(0)` (fixo na tela) e `tilePositionX` atualizado manualmente no `update()`. Isso garante que o tile repete infinitamente e o parallax funciona. 3 linhas de codigo, zero bugs de rendering.

### 2.6 Camera Deadzone

```
Camera viewport (480x270):
┌──────────────────────────────────────────────┐
│                                              │
│        ┌────────────────────┐                │
│        │                    │                │
│        │     DEADZONE       │                │
│        │     80 x 20        │                │
│        │   [PLAYER]         │                │
│        │                    │                │
│        └────────────────────┘                │
│                                              │
└──────────────────────────────────────────────┘

Player dentro da deadzone: camera NAO se move
Player cruza a borda da deadzone: camera comeca a seguir
lerp 0.08: camera chega suavemente (nao "gruda" no player)
```

Sem deadzone, a camera se move a cada pixel que o player se move. Fica nervoso, especialmente com joystick analogico no mobile. A deadzone de 80px horizontal da uma "folga" confortavel -- o jogador pode ajustar posicao sem a tela inteira deslizar.

---

## 3. Object Pooling Strategy

### 3.1 Principio: Zero `new` no Game Loop

Alocacao de memoria durante gameplay e o inimigo numero 1 da performance em JavaScript. Cada `new Sprite()` durante o jogo e uma alocacao de memoria. Memoria alocada precisa ser coletada pelo garbage collector. O GC do V8 faz "minor GC" (scavenge) a cada ~1-2 MB alocados, pausando a execucao por 1-5ms. A 60fps, voce tem 16.67ms por frame. Uma pausa de 5ms e 30% do seu budget de frame. Resultado: micro-stutter. Imperceptivel individualmente, mas acumulado em 3 minutos de gameplay cria a sensacao de "jogo meio travado".

Solucao: pre-alocar TUDO antes do gameplay comecar. Durante o jogo, REUSAR objetos ja alocados. Zumbi morreu? Nao destrua -- desative e devolva pra pool. Projetil saiu da tela? Desative e devolva. Particula terminou? Desative e devolva.

### 3.2 Pool de Zumbis

```typescript
// src/phaser/entities/ZombiePool.ts
import Phaser from 'phaser';
import { Zombie, ZombieType, ZOMBIE_CONFIG } from './Zombie';

const MAX_ZOMBIES = 50;

export class ZombiePool {
  public group: Phaser.Physics.Arcade.Group;
  private scene: Phaser.Scene;

  constructor(scene: Phaser.Scene, maxSize: number = MAX_ZOMBIES) {
    this.scene = scene;
    this.group = scene.physics.add.group({
      classType: Zombie,
      maxSize,
      runChildUpdate: true, // Chama update() de cada zombie ativo
      createCallback: (zombie: Phaser.GameObjects.GameObject) => {
        const z = zombie as Zombie;
        z.setActive(false);
        z.setVisible(false);
        (z.body as Phaser.Physics.Arcade.Body).enable = false;
      },
    });

    // Pre-aloca todos os zumbis de uma vez (no create, nao no update)
    for (let i = 0; i < maxSize; i++) {
      const zombie = new Zombie(scene, 0, 0);
      zombie.setActive(false);
      zombie.setVisible(false);
      this.group.add(zombie);
    }
  }

  spawn(x: number, y: number, type: ZombieType): Zombie | null {
    // Pega um zumbi inativo da pool
    const zombie = this.group.getFirstDead(false) as Zombie | null;
    if (!zombie) return null; // Pool cheia -- todos os 50 estao ativos

    zombie.activate(x, y, type);
    return zombie;
  }

  update(time: number, delta: number) {
    // runChildUpdate: true ja chama update() dos ativos
    // Aqui so fazemos culling de zumbis fora da camera
    const cam = this.scene.cameras.main;
    const margin = 64; // Margem de seguranca (sprite width)

    this.group.getChildren().forEach((child) => {
      const zombie = child as Zombie;
      if (!zombie.active) return;

      // Se o zumbi esta muito longe da camera, desativa
      if (zombie.x < cam.scrollX - margin * 4 ||
          zombie.x > cam.scrollX + cam.width + margin * 4) {
        zombie.deactivate();
      }
    });
  }

  getActiveCount(): number {
    return this.group.countActive(true);
  }
}
```

```typescript
// src/phaser/entities/Zombie.ts
export type ZombieType = 'vereador' | 'assessor' | 'senador' | 'lobista' | 'boss';

export const ZOMBIE_CONFIG: Record<ZombieType, {
  hp: number;
  speed: number;
  damage: number;
  score: number;
  width: number;
  height: number;
  frame: string; // Frame no atlas 'zombies'
}> = {
  vereador:  { hp: 30,  speed: 40,  damage: 10, score: 100,  width: 28, height: 44, frame: 'vereador-idle-0' },
  assessor:  { hp: 20,  speed: 55,  damage: 15, score: 150,  width: 24, height: 48, frame: 'assessor-idle-0' },
  senador:   { hp: 80,  speed: 25,  damage: 20, score: 250,  width: 36, height: 52, frame: 'senador-idle-0' },
  lobista:   { hp: 40,  speed: 45,  damage: 12, score: 175,  width: 28, height: 48, frame: 'lobista-idle-0' },
  boss:      { hp: 500, speed: 20,  damage: 35, score: 1000, width: 44, height: 64, frame: 'boss-idle-0' },
};

export class Zombie extends Phaser.Physics.Arcade.Sprite {
  private zombieType: ZombieType = 'vereador';
  private hp = 0;
  private maxHp = 0;
  private speed = 0;
  private damageValue = 0;
  private scoreValue = 0;
  private state: 'chase' | 'attack' | 'dying' = 'chase';

  constructor(scene: Phaser.Scene, x: number, y: number) {
    super(scene, x, y, 'zombies', 'vereador-idle-0');
    scene.add.existing(this);
    scene.physics.add.existing(this);
  }

  activate(x: number, y: number, type: ZombieType) {
    const config = ZOMBIE_CONFIG[type];
    this.zombieType = type;
    this.hp = config.hp;
    this.maxHp = config.hp;
    this.speed = config.speed;
    this.damageValue = config.damage;
    this.scoreValue = config.score;
    this.state = 'chase';

    this.setPosition(x, y);
    this.setActive(true);
    this.setVisible(true);
    this.setFrame(config.frame);
    this.setSize(config.width, config.height);

    const body = this.body as Phaser.Physics.Arcade.Body;
    body.enable = true;
    body.setSize(config.width, config.height);
    body.setOffset(
      (this.width - config.width) / 2,
      this.height - config.height
    );
    body.reset(x, y);

    this.setDepth(200); // Layer 6: Entidades
    this.setAlpha(1);
    this.clearTint();

    // Inicia animacao
    this.play(`${type}-walk`);
  }

  deactivate() {
    this.setActive(false);
    this.setVisible(false);
    const body = this.body as Phaser.Physics.Arcade.Body;
    body.enable = false;
    body.stop();
    this.state = 'chase';
  }

  takeDamage(amount: number): boolean {
    this.hp -= amount;
    // Hit flash: tint branco por 80ms
    this.setTintFill(0xffffff);
    this.scene.time.delayedCall(80, () => {
      if (this.active) this.clearTint();
    });

    if (this.hp <= 0) {
      this.die();
      return true; // Morreu
    }
    return false;
  }

  private die() {
    this.state = 'dying';
    (this.body as Phaser.Physics.Arcade.Body).enable = false;
    this.play(`${this.zombieType}-death`);
    this.once('animationcomplete', () => {
      this.deactivate(); // Volta pra pool
    });
  }

  preUpdate(time: number, delta: number) {
    super.preUpdate(time, delta);
    if (this.state !== 'chase') return;

    // Chase: move em direcao ao player
    const player = (this.scene as any).player;
    if (!player) return;

    const dx = player.x - this.x;
    const direction = Math.sign(dx);
    this.setVelocityX(direction * this.speed);
    this.setFlipX(direction < 0);

    // Se perto o suficiente, ataca
    if (Math.abs(dx) < 20) {
      this.state = 'attack';
      this.setVelocityX(0);
      this.play(`${this.zombieType}-attack`);
      this.once('animationcomplete', () => {
        this.state = 'chase';
        this.play(`${this.zombieType}-walk`);
      });
    }
  }
}
```

### 3.3 Pool de Projeteis

```typescript
// src/phaser/entities/ProjectilePool.ts
export type ProjectileType = 'chinelo' | 'urna' | 'santinho';

const PROJECTILE_CONFIG: Record<ProjectileType, {
  speed: number;
  damage: number;
  frame: string;
  width: number;
  height: number;
  lifespan: number; // ms antes de auto-desativar
}> = {
  chinelo:  { speed: 300, damage: 25, frame: 'chinelo',  width: 16, height: 16, lifespan: 2000 },
  urna:     { speed: 200, damage: 50, frame: 'urna',     width: 20, height: 16, lifespan: 1500 },
  santinho: { speed: 400, damage: 10, frame: 'santinho', width: 8,  height: 12, lifespan: 3000 },
};

const MAX_PROJECTILES = 30;

export class ProjectilePool {
  public group: Phaser.Physics.Arcade.Group;
  private scene: Phaser.Scene;

  constructor(scene: Phaser.Scene, maxSize: number = MAX_PROJECTILES) {
    this.scene = scene;
    this.group = scene.physics.add.group({
      maxSize,
      allowGravity: false,
    });

    // Pre-alocacao
    for (let i = 0; i < maxSize; i++) {
      const proj = scene.physics.add.sprite(0, 0, 'projectiles', 'chinelo');
      proj.setActive(false);
      proj.setVisible(false);
      (proj.body as Phaser.Physics.Arcade.Body).enable = false;
      proj.setDepth(500);
      this.group.add(proj);
    }
  }

  fire(x: number, y: number, direction: number, type: ProjectileType): Phaser.Physics.Arcade.Sprite | null {
    const proj = this.group.getFirstDead(false) as Phaser.Physics.Arcade.Sprite | null;
    if (!proj) return null;

    const config = PROJECTILE_CONFIG[type];
    proj.setPosition(x, y);
    proj.setActive(true);
    proj.setVisible(true);
    proj.setFrame(config.frame);
    proj.setSize(config.width, config.height);

    const body = proj.body as Phaser.Physics.Arcade.Body;
    body.enable = true;
    body.reset(x, y);
    body.setVelocityX(direction * config.speed);
    proj.setFlipX(direction < 0);

    // Rotacao visual (chinelo gira)
    if (type === 'chinelo') {
      this.scene.tweens.add({
        targets: proj,
        angle: direction > 0 ? 360 : -360,
        duration: 500,
        repeat: -1,
      });
    }

    // Auto-desativar apos lifespan (evita projeteis eternos)
    this.scene.time.delayedCall(config.lifespan, () => {
      if (proj.active) {
        proj.setActive(false);
        proj.setVisible(false);
        body.enable = false;
        body.stop();
      }
    });

    // Guardar damage no data do sprite para uso no collision handler
    proj.setData('damage', config.damage);
    proj.setData('type', type);

    return proj;
  }

  update(_time: number, _delta: number) {
    // Desativar projeteis fora da camera
    const cam = this.scene.cameras.main;
    this.group.getChildren().forEach((child) => {
      const proj = child as Phaser.Physics.Arcade.Sprite;
      if (!proj.active) return;
      if (proj.x < cam.scrollX - 64 || proj.x > cam.scrollX + cam.width + 64) {
        proj.setActive(false);
        proj.setVisible(false);
        (proj.body as Phaser.Physics.Arcade.Body).enable = false;
      }
    });
  }
}
```

### 3.4 Pool de Particulas

```typescript
// src/phaser/entities/ParticleConfig.ts
// Phaser 3.60+ usa ParticleEmitter integrado ao add.particles()
// Nao precisa de pool manual -- o Phaser gerencia internamente
// Mas precisamos LIMITAR a quantidade total

export function createParticleSystems(scene: Phaser.Scene) {
  // Gas toxico verde (ambiente -- emitter persistente)
  const gasEmitter = scene.add.particles(0, 0, 'vfx', {
    frame: 'gas-particle',
    lifespan: { min: 2000, max: 4000 },
    speed: { min: 5, max: 15 },
    angle: { min: 250, max: 290 }, // Para cima e levemente pros lados
    alpha: { start: 0.3, end: 0 },
    scale: { start: 0.5, end: 1.5 },
    tint: 0x3D6B3A,
    frequency: 500,
    quantity: 1,
    maxParticles: 20, // LIMITE ABSOLUTO
  });
  gasEmitter.setDepth(650);

  // Santinhos voando (ambiente -- emitter persistente)
  const santinhoEmitter = scene.add.particles(0, 0, 'vfx', {
    frame: ['santinho-1', 'santinho-2', 'santinho-3'],
    lifespan: { min: 3000, max: 6000 },
    speedX: { min: -30, max: 30 },
    speedY: { min: -10, max: 10 },
    angle: { min: 0, max: 360 },
    rotate: { min: -180, max: 180 },
    alpha: { start: 0.6, end: 0 },
    scale: { start: 0.8, end: 0.3 },
    frequency: 2000,
    quantity: 1,
    maxParticles: 15,
  });
  santinhoEmitter.setDepth(700);

  // Poeira de impacto (on-demand -- nao usa frequency)
  const dustEmitter = scene.add.particles(0, 0, 'vfx', {
    frame: 'dust',
    lifespan: 400,
    speed: { min: 20, max: 60 },
    angle: { min: 200, max: 340 },
    alpha: { start: 0.5, end: 0 },
    scale: { start: 0.3, end: 0.8 },
    quantity: 5,
    maxParticles: 30,
    emitting: false, // Nao emite automaticamente -- chamamos explode()
  });
  dustEmitter.setDepth(600);

  return { gasEmitter, santinhoEmitter, dustEmitter };
}
```

### 3.5 Pool de VFX (Hit Flashes, Onomatopeias)

```typescript
// src/phaser/entities/VFXPool.ts
const MAX_VFX = 40;

export class VFXPool {
  private scene: Phaser.Scene;
  private hitFlashGroup: Phaser.GameObjects.Group;
  private onomatopoeiaGroup: Phaser.GameObjects.Group;

  constructor(scene: Phaser.Scene, maxSize: number = MAX_VFX) {
    this.scene = scene;

    // Hit flashes: sprite de "impacto" que aparece por 150ms
    this.hitFlashGroup = scene.add.group({
      maxSize: 20,
    });
    for (let i = 0; i < 20; i++) {
      const flash = scene.add.sprite(0, 0, 'vfx', 'hit-flash-0');
      flash.setActive(false);
      flash.setVisible(false);
      flash.setDepth(750);
      this.hitFlashGroup.add(flash);
    }

    // Onomatopeias: "POW!", "CRACK!", "DEFERIDO!"
    this.onomatopoeiaGroup = scene.add.group({
      maxSize: 20,
    });
    for (let i = 0; i < 20; i++) {
      const text = scene.add.bitmapText(0, 0, 'pixel-font', '', 8);
      text.setActive(false);
      text.setVisible(false);
      text.setDepth(800);
      this.onomatopoeiaGroup.add(text);
    }
  }

  showHitFlash(x: number, y: number) {
    const flash = this.hitFlashGroup.getFirstDead(false) as Phaser.GameObjects.Sprite | null;
    if (!flash) return;

    flash.setPosition(x, y);
    flash.setActive(true);
    flash.setVisible(true);
    flash.play('hit-flash-anim');
    flash.once('animationcomplete', () => {
      flash.setActive(false);
      flash.setVisible(false);
    });
  }

  showOnomatopoeia(x: number, y: number, text: string) {
    const label = this.onomatopoeiaGroup.getFirstDead(false) as Phaser.GameObjects.BitmapText | null;
    if (!label) return;

    label.setPosition(x, y - 10);
    label.setText(text);
    label.setActive(true);
    label.setVisible(true);
    label.setAlpha(1);

    // Float up + fade out
    this.scene.tweens.add({
      targets: label,
      y: y - 40,
      alpha: 0,
      duration: 600,
      ease: 'Power2',
      onComplete: () => {
        label.setActive(false);
        label.setVisible(false);
      },
    });
  }
}
```

### 3.6 Pool Summary

| Pool | Max Ativos | Tipo | Pre-alocados | Recycle Trigger |
|---|---|---|---|---|
| **Zumbis** | 50 | Physics Sprite | 50 | Morte (deactivate apos animacao), fora da camera |
| **Projeteis** | 30 | Physics Sprite | 30 | Hit (deactivate), fora da camera, lifespan expirado |
| **Gas particles** | 20 | Particle | Managed by Phaser | lifespan (auto) |
| **Santinhos particles** | 15 | Particle | Managed by Phaser | lifespan (auto) |
| **Dust particles** | 30 | Particle | Managed by Phaser | lifespan (auto) |
| **Hit flashes** | 20 | Sprite | 20 | animationcomplete |
| **Onomatopeias** | 20 | BitmapText | 20 | Tween complete (600ms) |
| **TOTAL** | **185** | | **~120 pre-alocados + Phaser particles** | |

**Budget maximo em tela:** 50 zumbis + 30 projeteis + 65 particulas + 20 VFX + 1 player = **~166 entidades**. Dentro do budget de 150 do doc 12 (as particulas sao leves demais para contar full).

---

## 4. Backend Architecture (Minimo Viavel)

### 4.1 Filosofia: Backend Existe para Duas Coisas

1. **Auth** -- Saber quem e o jogador (para vincular score a uma identidade)
2. **Rankings** -- Leaderboard global (motivacao de replay)

Nada mais. Sem inventario, sem save game na nuvem, sem chat, sem friends list, sem achievements server-side. O jogo continua 100% jogavel sem backend -- auth e ranking sao features de retencao, nao de gameplay.

### 4.2 Stack: Supabase (PostgreSQL Managed)

| Opcao | Pros | Contras | Veredicto |
|---|---|---|---|
| **Supabase** | Auth pronto (Google OAuth), PostgreSQL real, Row Level Security, SDK JS, free tier generoso (50K MAU auth, 500MB DB), API REST + Realtime | Vendor lock-in leve | **ESCOLHA** |
| Firebase Firestore | Auth pronto, SDK maduro, free tier OK | NoSQL (leaderboard queries sao dolorosas), pricing imprevisivel | NAO |
| Node.js/Express + PostgreSQL self-hosted | Controle total, sem vendor lock | Precisa de servidor, deploy, manter infra. Complexidade gratuita para MVP | NAO |
| Cloudflare Workers + D1 | Edge computing, barato | D1 e beta, SQLite (limitacoes de query), Auth tem que implementar na mao | FUTURO (v2) |

**Por que Supabase e nao Firebase?** Porque ranking e uma query SQL trivial (`SELECT * FROM scores ORDER BY score DESC LIMIT 100`). No Firestore, voce precisa criar indices compostos, lidar com queries limitadas, e paginar de forma nao-intuitiva. PostgreSQL faz isso dormindo. Supabase te da PostgreSQL com auth pronto e RLS (Row Level Security) que resolve permissoes sem escrever middleware.

### 4.3 Schema do Banco

```sql
-- Supabase PostgreSQL

-- Profiles: criado automaticamente pelo trigger de auth
CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  display_name TEXT NOT NULL DEFAULT 'Cidadao Anonimo',
  avatar_url TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Scores: cada partida completa gera um registro
CREATE TABLE scores (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  score INTEGER NOT NULL,
  kills INTEGER NOT NULL DEFAULT 0,
  wave_reached INTEGER NOT NULL DEFAULT 0,
  time_survived INTEGER NOT NULL DEFAULT 0, -- em segundos
  political_title TEXT NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indices para queries de leaderboard
CREATE INDEX idx_scores_global ON scores (score DESC);
CREATE INDEX idx_scores_daily ON scores (created_at DESC, score DESC);
CREATE INDEX idx_scores_user ON scores (user_id, score DESC);

-- View: leaderboard global top 100
CREATE VIEW leaderboard_global AS
SELECT
  s.score,
  s.kills,
  s.wave_reached,
  s.time_survived,
  s.political_title,
  s.created_at,
  p.display_name,
  p.avatar_url,
  ROW_NUMBER() OVER (ORDER BY s.score DESC) as rank
FROM scores s
JOIN profiles p ON s.user_id = p.id
ORDER BY s.score DESC
LIMIT 100;

-- View: leaderboard diario (top 100 de hoje)
CREATE VIEW leaderboard_daily AS
SELECT
  s.score,
  s.kills,
  s.wave_reached,
  s.political_title,
  s.created_at,
  p.display_name,
  p.avatar_url,
  ROW_NUMBER() OVER (ORDER BY s.score DESC) as rank
FROM scores s
JOIN profiles p ON s.user_id = p.id
WHERE s.created_at >= CURRENT_DATE
ORDER BY s.score DESC
LIMIT 100;

-- RLS: usuario so pode inserir seus proprios scores
ALTER TABLE scores ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can insert own scores"
  ON scores FOR INSERT
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Anyone can read scores"
  ON scores FOR SELECT
  USING (true);

-- RLS: profiles
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Public profiles are viewable"
  ON profiles FOR SELECT
  USING (true);

CREATE POLICY "Users can update own profile"
  ON profiles FOR UPDATE
  USING (auth.uid() = id);
```

### 4.4 API Client (Supabase JS SDK)

```typescript
// src/services/supabase.ts
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const supabase = createClient(supabaseUrl, supabaseAnonKey);

// --- AUTH ---

// Google OAuth login
export async function loginWithGoogle() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: window.location.origin,
    },
  });
  return { data, error };
}

// Guest mode: anonymous sign-in
export async function loginAsGuest() {
  const { data, error } = await supabase.auth.signInAnonymously();
  return { data, error };
}

// Get current user
export async function getCurrentUser() {
  const { data: { user } } = await supabase.auth.getUser();
  return user;
}

// Logout
export async function logout() {
  await supabase.auth.signOut();
}

// --- SCORES ---

// POST /score (submit a game score)
export async function submitScore(scoreData: {
  score: number;
  kills: number;
  wave_reached: number;
  time_survived: number;
  political_title: string;
}) {
  const user = await getCurrentUser();
  if (!user) return { error: 'Not authenticated' };

  const { data, error } = await supabase
    .from('scores')
    .insert({
      user_id: user.id,
      ...scoreData,
    });

  return { data, error };
}

// GET /leaderboard (global top 100)
export async function getLeaderboardGlobal() {
  const { data, error } = await supabase
    .from('leaderboard_global')
    .select('*');

  return { data, error };
}

// GET /leaderboard/daily (today's top 100)
export async function getLeaderboardDaily() {
  const { data, error } = await supabase
    .from('leaderboard_daily')
    .select('*');

  return { data, error };
}

// GET /leaderboard/personal (user's best scores)
export async function getPersonalBest() {
  const user = await getCurrentUser();
  if (!user) return { data: [], error: null };

  const { data, error } = await supabase
    .from('scores')
    .select('score, kills, wave_reached, political_title, created_at')
    .eq('user_id', user.id)
    .order('score', { ascending: false })
    .limit(10);

  return { data, error };
}
```

### 4.5 API Endpoints (Logico)

Supabase expoe tudo via REST auto-gerado + RLS. Nao precisa de servidor Express. Mas conceitualmente, os endpoints sao:

| Metodo | Endpoint (logico) | Descricao | Auth Required |
|---|---|---|---|
| `POST` | `/auth/google` | OAuth flow com Google | Nao |
| `POST` | `/auth/anonymous` | Cria sessao guest | Nao |
| `POST` | `/auth/logout` | Encerra sessao | Sim |
| `POST` | `/scores` | Submete score de uma partida | Sim (RLS) |
| `GET` | `/leaderboard_global` | Top 100 all-time | Nao |
| `GET` | `/leaderboard_daily` | Top 100 de hoje | Nao |
| `GET` | `/scores?user_id=X` | Best scores do usuario | Nao |

### 4.6 Custo do Backend

| Item | Free Tier Supabase | Se exceder |
|---|---|---|
| **Auth (MAU)** | 50.000 usuarios/mes | $0.00325/MAU |
| **Database** | 500 MB | $0.125/GB/mes |
| **API requests** | Sem limite documentado (fair use) | Pro plan $25/mes |
| **Realtime** | 500 conexoes simultaneas | Pro plan |
| **Bandwidth** | 5 GB/mes | $0.09/GB |

Para o MVP com ~50K jogadores, o free tier e mais que suficiente. Score de uma partida e ~200 bytes. 50K jogadores x 5 partidas/dia = 250K inserts/dia x 200 bytes = ~50 MB/dia. Em 30 dias: 1.5 GB. Precisa do Pro plan ($25/mes) apos ~10 dias se o jogo viralizar. Custo aceitavel.

### 4.7 Anti-Cheat Basico

Para o MVP, anti-cheat elaborado e overkill. Mas medidas minimas:

```typescript
// Score validation no RLS (PostgreSQL function)
CREATE OR REPLACE FUNCTION validate_score()
RETURNS TRIGGER AS $$
BEGIN
  -- Score maximo teorico: ~50.000 em 3 minutos
  -- Qualquer coisa acima e suspicious
  IF NEW.score > 100000 THEN
    RAISE EXCEPTION 'Score exceeds theoretical maximum';
  END IF;
  
  -- Kills maximo: ~300 em 3 minutos (5 waves x 60 zumbis)
  IF NEW.kills > 500 THEN
    RAISE EXCEPTION 'Kill count exceeds theoretical maximum';
  END IF;
  
  -- Time survived: max 300 segundos (5 minutos com bonus)
  IF NEW.time_survived > 600 THEN
    RAISE EXCEPTION 'Time survived exceeds maximum';
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_validate_score
  BEFORE INSERT ON scores
  FOR EACH ROW
  EXECUTE FUNCTION validate_score();
```

Nao e perfeito. Nao impede alguem de mandar um POST com score 99.999. Mas impede os casos grotescos. Anti-cheat real (replay validation, server-side simulation) e trabalho para v2.0 se o leaderboard virar competitivo.

---

## 5. Responsive Strategy

### 5.1 Viewport e Scaling

```
Resolucao logica do jogo: 480 x 270 pixels
Aspect ratio: 16:9

O Phaser renderiza internamente em 480x270.
O Scale Manager (mode: FIT) escala o canvas para caber na tela.
CSS faz o resto.
```

| Device | Tela (px) | Orientacao | Canvas renderizado | Escala |
|---|---|---|---|---|
| Galaxy A06 | 720x1600 | Landscape (1600x720) | 1280x720 | 2.67x |
| iPhone 14 | 1170x2532 | Landscape (2532x1170) | 2080x1170 | 4.33x |
| Desktop 1080p | 1920x1080 | Landscape | 1920x1080 | 4.0x |
| Desktop 1440p | 2560x1440 | Landscape | 2560x1440 | 5.33x |
| iPad | 2048x1536 | Landscape (2048x1536) | 2048x1152* | 4.27x |

*iPad em 4:3 tera letterbox (barras pretas em cima/baixo) porque o jogo e 16:9. Melhor que esticar e distorcer os pixels.

### 5.2 Scale Mode: FIT vs RESIZE

**FIT:** O canvas e renderizado em 480x270 e escalado com CSS. Pixel art permanece intacto. Letterbox se o aspect ratio nao bater. Todos os calculos de posicao sao em coordenadas logicas (480x270).

**RESIZE:** O canvas muda de tamanho conforme a janela. Mais complexo -- posicoes de UI dependem da resolucao real. HUD pode quebrar em resoluces inesperadas.

**Decisao: FIT.** Pixel art e 480x270 e ponto. O mundo do jogo nao precisa se adaptar a resolucao -- e a resolucao que se adapta ao jogo. Menos bugs, menos edge cases, comportamento previsivel.

### 5.3 Orientation Lock: Landscape

```typescript
// src/utils/orientation.ts

export function setupOrientationLock() {
  // Tenta usar a Screen Orientation API
  try {
    screen.orientation.lock('landscape').catch(() => {
      // Silently fail -- nem todos os browsers suportam
    });
  } catch {
    // API nao disponivel
  }
}

// Detectar e avisar quando em portrait
export function checkOrientation(): boolean {
  if (window.innerHeight > window.innerWidth) {
    // Portrait -- mostrar aviso "Gire o celular"
    return false;
  }
  return true;
}
```

```typescript
// src/components/OrientationOverlay.tsx
import { useState, useEffect } from 'react';
import { checkOrientation } from '../utils/orientation';

export function OrientationOverlay() {
  const [isPortrait, setIsPortrait] = useState(!checkOrientation());

  useEffect(() => {
    const handleResize = () => {
      setIsPortrait(!checkOrientation());
    };
    window.addEventListener('resize', handleResize);
    window.addEventListener('orientationchange', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
      window.removeEventListener('orientationchange', handleResize);
    };
  }, []);

  if (!isPortrait) return null;

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      background: '#1a0a0a',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 9999,
      color: '#ff4444',
      fontFamily: '"Press Start 2P", monospace',
    }}>
      <div style={{ fontSize: '48px', marginBottom: '24px' }}>
        &#x21BB; {/* Unicode rotate symbol */}
      </div>
      <div style={{ fontSize: '14px', textAlign: 'center', padding: '0 32px' }}>
        GIRE O CELULAR
      </div>
    </div>
  );
}
```

### 5.4 Input: Mobile Touch + Desktop Keyboard

```typescript
// src/phaser/input/InputManager.ts
export class InputManager {
  private scene: Phaser.Scene;
  private cursors!: Phaser.Types.Input.Keyboard.CursorKeys;
  private wasd!: { W: Phaser.Input.Keyboard.Key; A: Phaser.Input.Keyboard.Key; S: Phaser.Input.Keyboard.Key; D: Phaser.Input.Keyboard.Key };
  private spaceKey!: Phaser.Input.Keyboard.Key;
  private isMobile: boolean;

  // Virtual joystick state (atualizado pelo React component)
  public joystickX = 0; // -1 a 1
  public joystickY = 0; // -1 a 1
  public attackPressed = false;

  constructor(scene: Phaser.Scene) {
    this.scene = scene;
    this.isMobile = !scene.sys.game.device.os.desktop;

    if (!this.isMobile && scene.input.keyboard) {
      this.cursors = scene.input.keyboard.createCursorKeys();
      this.wasd = {
        W: scene.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.W),
        A: scene.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.A),
        S: scene.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.S),
        D: scene.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.D),
      };
      this.spaceKey = scene.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);
    }
  }

  getMovement(): { x: number; y: number } {
    if (this.isMobile) {
      return { x: this.joystickX, y: this.joystickY };
    }

    let x = 0;
    let y = 0;
    if (this.cursors.left.isDown || this.wasd.A.isDown) x = -1;
    if (this.cursors.right.isDown || this.wasd.D.isDown) x = 1;
    if (this.cursors.up.isDown || this.wasd.W.isDown) y = -1;
    if (this.cursors.down.isDown || this.wasd.S.isDown) y = 1;

    return { x, y };
  }

  isAttacking(): boolean {
    if (this.isMobile) return this.attackPressed;
    return this.spaceKey.isDown || this.scene.input.activePointer.isDown;
  }
}
```

### 5.5 Virtual Joystick (React component com touch events)

```typescript
// src/components/VirtualJoystick.tsx
import { useRef, useCallback, useEffect } from 'react';
import { EventBus } from '../events/EventBus';

const JOYSTICK_SIZE = 120; // px visual
const KNOB_SIZE = 48;
const MAX_DISTANCE = 40; // px maximo que o knob se move

export function VirtualJoystick() {
  const baseRef = useRef<HTMLDivElement>(null);
  const knobRef = useRef<HTMLDivElement>(null);
  const touchIdRef = useRef<number | null>(null);
  const centerRef = useRef({ x: 0, y: 0 });

  const handleTouchStart = useCallback((e: React.TouchEvent) => {
    if (touchIdRef.current !== null) return; // Ja tem um toque ativo

    const touch = e.changedTouches[0];
    touchIdRef.current = touch.identifier;

    const rect = baseRef.current!.getBoundingClientRect();
    centerRef.current = {
      x: rect.left + rect.width / 2,
      y: rect.top + rect.height / 2,
    };
  }, []);

  const handleTouchMove = useCallback((e: React.TouchEvent) => {
    for (let i = 0; i < e.changedTouches.length; i++) {
      const touch = e.changedTouches[i];
      if (touch.identifier !== touchIdRef.current) continue;

      const dx = touch.clientX - centerRef.current.x;
      const dy = touch.clientY - centerRef.current.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      const clamped = Math.min(distance, MAX_DISTANCE);
      const angle = Math.atan2(dy, dx);

      const normalizedX = (clamped / MAX_DISTANCE) * Math.cos(angle);
      const normalizedY = (clamped / MAX_DISTANCE) * Math.sin(angle);

      // Move knob visualmente
      if (knobRef.current) {
        knobRef.current.style.transform =
          `translate(${normalizedX * MAX_DISTANCE}px, ${normalizedY * MAX_DISTANCE}px)`;
      }

      // Envia para Phaser via EventBus
      EventBus.emit('joystick-move' as any, { x: normalizedX, y: normalizedY });
    }
  }, []);

  const handleTouchEnd = useCallback((e: React.TouchEvent) => {
    for (let i = 0; i < e.changedTouches.length; i++) {
      if (e.changedTouches[i].identifier !== touchIdRef.current) continue;
      touchIdRef.current = null;

      if (knobRef.current) {
        knobRef.current.style.transform = 'translate(0px, 0px)';
      }

      EventBus.emit('joystick-move' as any, { x: 0, y: 0 });
    }
  }, []);

  // So renderiza em mobile
  const isMobile = /Mobi|Android/i.test(navigator.userAgent);
  if (!isMobile) return null;

  return (
    <div
      ref={baseRef}
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      onTouchEnd={handleTouchEnd}
      style={{
        position: 'absolute',
        bottom: '24px',
        left: '24px',
        width: `${JOYSTICK_SIZE}px`,
        height: `${JOYSTICK_SIZE}px`,
        borderRadius: '50%',
        background: 'rgba(255,255,255,0.1)',
        border: '2px solid rgba(255,255,255,0.2)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        touchAction: 'none', // CRITICO: impede scroll do browser
        zIndex: 20,
        pointerEvents: 'auto',
      }}
    >
      <div
        ref={knobRef}
        style={{
          width: `${KNOB_SIZE}px`,
          height: `${KNOB_SIZE}px`,
          borderRadius: '50%',
          background: 'rgba(255,68,68,0.6)',
          border: '2px solid rgba(255,68,68,0.8)',
          transition: 'none', // Sem CSS transition -- precisa ser instantaneo
        }}
      />
    </div>
  );
}
```

**Por que o joystick e React (DOM) e nao Phaser (canvas)?** Porque touch events no DOM sao instantaneos. O browser ja otimiza multi-touch tracking. Fazer joystick dentro do canvas significa reimplementar hit testing, multi-pointer tracking, e visual feedback -- tudo que o DOM ja faz nativamente. Alem disso, o joystick nao participa do game world (nao tem colisao, nao se move com a camera), entao nao precisa estar no Phaser.

### 5.6 Attack Button (Mobile)

```typescript
// src/components/AttackButton.tsx
export function AttackButton() {
  const isMobile = /Mobi|Android/i.test(navigator.userAgent);
  if (!isMobile) return null;

  return (
    <button
      onTouchStart={(e) => {
        e.preventDefault();
        EventBus.emit('attack-press' as any, undefined);
      }}
      onTouchEnd={(e) => {
        e.preventDefault();
        EventBus.emit('attack-release' as any, undefined);
      }}
      style={{
        position: 'absolute',
        bottom: '32px',
        right: '32px',
        width: '80px',
        height: '80px',
        borderRadius: '50%',
        background: 'rgba(255,68,68,0.4)',
        border: '3px solid rgba(255,68,68,0.7)',
        color: '#ff4444',
        fontSize: '24px',
        fontFamily: '"Press Start 2P", monospace',
        touchAction: 'none',
        zIndex: 20,
        pointerEvents: 'auto',
        WebkitUserSelect: 'none',
        userSelect: 'none',
      }}
    >
      ATK
    </button>
  );
}
```

---

## 6. Performance Budget

### 6.1 Target: 60fps no Galaxy A06 Chrome

O Galaxy A06 e o pior caso realista para o publico brasileiro. Specs:

| Spec | Galaxy A06 |
|---|---|
| **SoC** | MediaTek Helio G85 |
| **GPU** | Mali-G52 MC2 |
| **RAM** | 4 GB |
| **Tela** | 720x1600 (HD+) |
| **Browser** | Chrome Android |
| **WebGL** | 2.0 |
| **Max Texture Size** | 4096x4096 |
| **Max Texture Units** | 8 |

### 6.2 Frame Budget

```
Target: 60 fps = 16.67ms por frame

Budget breakdown:
├── JavaScript (game logic, AI, pools)     6.0 ms    36%
├── Physics (Arcade, colisoes)             2.0 ms    12%
├── WebGL rendering (draw calls, batching) 4.0 ms    24%
├── Browser overhead (compositor, events)  2.0 ms    12%
├── HEADROOM (para GC, spikes)             2.67 ms   16%
└── TOTAL                                  16.67 ms  100%
```

### 6.3 Draw Call Budget

| Layer | Assets | Draw Calls | Notas |
|---|---|---|---|
| Sky gradient | 1 Graphics | 1 | fillGradientStyle |
| Toxic clouds | 1 ParticleEmitter | 1 | Mesmo atlas que VFX |
| Congresso | 1 Image | 0* | Batched com proximo |
| PointLight (glow) | 1 Light | 1 | Pipeline separado |
| Ministerios distantes | 1 TileSprite | 1 | Textura propria |
| Ministerios proximos | 1 TileSprite | 1 | Textura propria |
| Background objects | N Sprites (1 atlas) | 1 | Batched num unico atlas |
| Ground tilemap | 2 Layers | 2 | Surface + subsurface |
| Characters atlas | 1 atlas | 1 | Player + all zombies |
| Projectiles atlas | 1 atlas | 1 | Batched com characters se no mesmo atlas |
| Particles/VFX | 1 atlas | 1 | vfx atlas |
| Foreground | N Sprites (1 atlas) | 1 | Batched |
| **TOTAL** | | **~12** | |

*Sprites com a mesma textura e adjacentes em depth sao batched automaticamente pelo WebGL renderer do Phaser.

**12 draw calls por frame.** O doc 12 estipulava <20 para mobile. Estamos dentro com margem. O Mali-G52 do Galaxy A06 lida com 50+ draw calls sem suar. 12 e trivial.

### 6.4 Sprite/Entity Budget

| Categoria | Max em Tela | Sprites por Entidade | Total Sprites |
|---|---|---|---|
| Player | 1 | 1 | 1 |
| Zumbis | 50 | 1 | 50 |
| Projeteis | 30 | 1 | 30 |
| Particles (gas+santinhos+dust) | 65 | 1 | 65 |
| VFX (hit flash + onomatopeia) | 10 | 1 | 10 |
| Background objects (L4) | ~15 visiveis | 1 | 15 |
| Foreground objects (L7) | ~5 visiveis | 1 | 5 |
| **TOTAL** | | | **~176** |

O Phaser 3.60+ renderiza 15.000+ sprites a 60fps no iPhone SE via WebGL batching. 176 sprites e 1.2% desse capacity. Headroom imenso.

### 6.5 Texture Atlas Strategy

```
Atlas 1: characters.png (2048x2048)
  - Cidadao (3 skin variants x 25 frames) = 75 frames
  - Cada frame ~68x68px
  - Total: 75 x 68x68 = ~347 KB descomprimido
  - Cabe facilmente em 2048x2048

Atlas 2: zombies.png (2048x2048)
  - 5 tipos x 25 frames = 125 frames
  - Cada frame ~68x68px (vereador/assessor/lobista)
  - Boss frames maiores (~112x112px)
  - Total: ~125 frames
  - Cabe em 2048x2048

Atlas 3: vfx.png (1024x1024)
  - Projeteis (chinelo, urna, santinho) = ~10 frames
  - Particles (gas, dust, santinhos) = ~10 frames
  - Hit flash = 4 frames
  - Onomatopeias (texto sprites) = ~10 frames
  - Total: ~34 frames, maioria pequena (16x16 a 32x32)
  - Cabe em 1024x1024 facil

Atlas 4: ui-game.png (512x512)
  - Joystick, botoes, icones de HUD
  - Pequeno

Background textures (separadas -- nao atlas):
  - congresso-320x120.png
  - ministerios-dist-1920x120.png
  - ministerios-prox-2400x180.png
  - Tileset do chao (256x256 ou 512x512)
```

| Atlas | Dimensao | Tamanho PNG (estimado) | Textura Units GPU |
|---|---|---|---|
| characters.png | 2048x2048 | ~400 KB | 1 |
| zombies.png | 2048x2048 | ~500 KB | 1 |
| vfx.png | 1024x1024 | ~100 KB | 1 |
| ui-game.png | 512x512 | ~50 KB | 1 |
| congresso.png | 320x120 | ~15 KB | 1* |
| ministerios-dist.png | 1920x120 | ~80 KB | 1* |
| ministerios-prox.png | 2400x180 | ~150 KB | 1* |
| tileset.png | 512x512 | ~80 KB | 1 |
| **TOTAL** | | **~1.4 MB** | **8** |

*Background textures pode ser batched pelo Phaser se nao exceder maxTextures.

8 texture units = exatamente o limite do Mali-G52. Se precisar de mais, consolidar backgrounds num unico atlas.

**Total de assets (estimado):**

| Tipo | Tamanho |
|---|---|
| Sprite atlases | ~1.4 MB |
| Tilemap JSON | ~50 KB |
| Audio (OGG + MP3) | ~1.5 MB |
| Phaser 3.88 (minified) | ~350 KB gzipped |
| Game code (TS compiled) | ~100-150 KB gzipped |
| React + React-DOM | ~45 KB gzipped |
| mitt + supabase-js | ~20 KB gzipped |
| **TOTAL** | **~3.5 MB** |

First load em 4G (10 Mbps): ~2.8 seconds. Aceitavel.
Subsequent loads (Service Worker cache): <500ms.

### 6.6 Dynamic Quality Scaling

```typescript
// src/phaser/systems/QualityManager.ts
export class QualityManager {
  private scene: Phaser.Scene;
  private fpsHistory: number[] = [];
  private qualityLevel: 'high' | 'medium' | 'low' = 'high';
  private checkInterval = 2000; // ms
  private lastCheck = 0;

  // Quality settings per level
  private static readonly QUALITY_SETTINGS = {
    high: {
      maxZombies: 50,
      maxParticles: 65,
      maxProjectiles: 30,
      screenShake: true,
      foregroundAlpha: 0.3,
    },
    medium: {
      maxZombies: 35,
      maxParticles: 30,
      maxProjectiles: 20,
      screenShake: true,
      foregroundAlpha: 0.15,
    },
    low: {
      maxZombies: 25,
      maxParticles: 15,
      maxProjectiles: 15,
      screenShake: false,
      foregroundAlpha: 0,
    },
  };

  constructor(scene: Phaser.Scene) {
    this.scene = scene;
  }

  update(time: number) {
    // Amostra FPS a cada frame
    this.fpsHistory.push(this.scene.game.loop.actualFps);
    if (this.fpsHistory.length > 120) this.fpsHistory.shift(); // Ultimos 2 segundos

    // Checa a cada 2 segundos
    if (time - this.lastCheck < this.checkInterval) return;
    this.lastCheck = time;

    const avgFps = this.fpsHistory.reduce((a, b) => a + b, 0) / this.fpsHistory.length;

    if (avgFps < 40 && this.qualityLevel !== 'low') {
      this.qualityLevel = 'low';
      this.applySettings();
    } else if (avgFps < 50 && this.qualityLevel === 'high') {
      this.qualityLevel = 'medium';
      this.applySettings();
    }
    // Nao sobe de qualidade automaticamente -- evita oscilacao
  }

  getSettings() {
    return QualityManager.QUALITY_SETTINGS[this.qualityLevel];
  }

  private applySettings() {
    const settings = this.getSettings();
    console.log(`[QualityManager] Switching to ${this.qualityLevel} quality`);
    // Os sistemas consultam getSettings() no proximo frame
    // Nada e destruido -- apenas limites sao ajustados
  }
}
```

### 6.7 Performance Checklist (Pre-Launch)

```
[ ] Phaser config: pixelArt: true, roundPixels: true, antialias: false
[ ] Canvas scale mode: FIT (nao RESIZE)
[ ] Viewport logico: 480x270 (nao resolucao nativa)
[ ] Todas as entidades usam object pooling (zero new no game loop)
[ ] Todos os sprites empacotados em atlas (TexturePacker)
[ ] Atlas max 2048x2048 (compativel com todos os GPUs mobile)
[ ] Audio: OGG + MP3 dual format
[ ] Animacoes: 8-12 fps (nao 60fps)
[ ] Arcade Physics (nao Matter.js)
[ ] Entidades fora da camera: body.enable = false (nao so invisible)
[ ] TileSprite parallax com scrollFactor(0) + manual offset
[ ] Max draw calls: <15
[ ] Max sprites em tela: <200
[ ] Max particles: <65
[ ] Dynamic quality scaling implementado
[ ] Testado no Galaxy A06 Chrome (ou device equivalente)
[ ] 60fps sustentado por 5 minutos sem drops abaixo de 50
[ ] GC pauses: < 5ms (verificar via Chrome DevTools Performance tab)
[ ] Total asset size: < 4 MB (comprimido)
[ ] First load < 3 seconds (4G)
```

---

## 7. Estrutura de Diretorios do Projeto

```
congresso-dos-mortos/
├── index.html                         # Entry point
├── vite.config.ts                     # Vite config
├── tsconfig.json                      # TypeScript config
├── package.json                       # { phaser, react, react-dom, mitt, @supabase/supabase-js }
├── .env                               # VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY
├── public/
│   ├── og-image.png                   # OpenGraph (1200x630)
│   ├── icons/                         # PWA icons
│   ├── assets/
│   │   ├── sprites/
│   │   │   ├── characters.png         # Atlas: cidadao (3 skins)
│   │   │   ├── characters.json        # TexturePacker JSON Hash
│   │   │   ├── zombies.png            # Atlas: 5 tipos de zumbi
│   │   │   ├── zombies.json
│   │   │   ├── vfx.png               # Atlas: projeteis, particles, flashes
│   │   │   ├── vfx.json
│   │   │   ├── ui-game.png           # Atlas: HUD in-game sprites
│   │   │   └── ui-game.json
│   │   ├── bg/
│   │   │   ├── congresso-320x120.png  # Congresso silhueta
│   │   │   ├── ministerios-dist-1920x120.png
│   │   │   └── ministerios-prox-2400x180.png
│   │   ├── tilemap/
│   │   │   ├── esplanada-sideview.json  # Tiled JSON
│   │   │   └── esplanada-sideview.png   # Tileset image
│   │   ├── fonts/
│   │   │   └── pixel-font.fnt          # Bitmap font (onomatopeias)
│   │   └── audio/
│   │       ├── music-main.ogg
│   │       ├── music-main.mp3
│   │       ├── sfx-hit.ogg
│   │       ├── sfx-hit.mp3
│   │       ├── sfx-death.ogg
│   │       ├── sfx-death.mp3
│   │       ├── sfx-powerup.ogg
│   │       ├── sfx-powerup.mp3
│   │       ├── sfx-combo.ogg
│   │       └── sfx-combo.mp3
├── src/
│   ├── main.tsx                        # React entry: ReactDOM.createRoot()
│   ├── App.tsx                         # Root component (state machine: menu/playing/gameover)
│   ├── components/
│   │   ├── PhaserGame.tsx             # Phaser container (useRef + useEffect)
│   │   ├── MainMenu.tsx               # Skin selection + Start button
│   │   ├── HUDOverlay.tsx             # Score, HP, Wave, Combo (DOM over canvas)
│   │   ├── GameOverScreen.tsx         # Score card, share, play again
│   │   ├── LoginPage.tsx              # Google login / Guest mode
│   │   ├── LeaderboardPage.tsx        # Top 100 global + daily
│   │   ├── VirtualJoystick.tsx        # Touch joystick (mobile only)
│   │   ├── AttackButton.tsx           # Touch attack (mobile only)
│   │   ├── OrientationOverlay.tsx     # "Gire o celular" (portrait warning)
│   │   └── PauseMenu.tsx             # Pause overlay
│   ├── events/
│   │   └── EventBus.ts                # mitt<GameEvents> -- React <-> Phaser bridge
│   ├── services/
│   │   ├── supabase.ts               # Supabase client + auth + scores
│   │   ├── analytics.ts              # GA4 + GameAnalytics wrapper
│   │   ├── ads.ts                     # H5 Ad Placement API wrapper
│   │   └── share.ts                   # Web Share API + fallbacks
│   ├── phaser/
│   │   ├── config.ts                  # Phaser.Types.Core.GameConfig
│   │   ├── scenes/
│   │   │   ├── BootScene.ts           # Load logo + progress bar assets
│   │   │   ├── PreloadScene.ts        # Load all game assets
│   │   │   └── GameScene.ts           # Gameplay (parallax, entities, physics, waves)
│   │   ├── entities/
│   │   │   ├── Player.ts             # Player sprite + movement + attack
│   │   │   ├── Zombie.ts             # Zombie base class (activate/deactivate pattern)
│   │   │   ├── ZombiePool.ts         # Phaser.Physics.Arcade.Group pool
│   │   │   ├── ProjectilePool.ts     # Projectile pool
│   │   │   └── VFXPool.ts            # Hit flash + onomatopoeia pool
│   │   ├── systems/
│   │   │   ├── WaveManager.ts        # Wave spawning logic
│   │   │   ├── ScoreManager.ts       # Score + combo + political titles
│   │   │   ├── PowerUpManager.ts     # Power-up spawning and effects
│   │   │   ├── ParticleConfig.ts     # Gas, santinhos, dust emitter configs
│   │   │   ├── QualityManager.ts     # Dynamic quality scaling
│   │   │   └── AudioManager.ts       # SFX + music control
│   │   └── input/
│   │       └── InputManager.ts        # Keyboard + joystick input abstraction
│   ├── data/
│   │   ├── gameOverPhrases.json       # 50+ frases de Game Over
│   │   ├── politicalTitles.json       # Titulos por faixa de score
│   │   ├── waveConfig.json            # Configuracao das 15 waves
│   │   └── zombieConfig.json          # Stats por tipo de zumbi
│   ├── utils/
│   │   ├── orientation.ts             # Screen orientation detection
│   │   └── storage.ts                # localStorage wrapper
│   └── styles/
│       └── global.css                 # Reset + fonts + base styles
├── sw.ts                              # Service Worker (Workbox)
├── supabase/
│   └── migrations/
│       └── 001_initial_schema.sql     # SQL do schema (profiles, scores, RLS)
└── .github/
    └── (Cloudflare Pages auto-deploy via Git integration)
```

**Estimativa de linhas de codigo:**

| Area | Linhas |
|---|---|
| React components (UI) | ~800 |
| Phaser scenes + entities + systems | ~2,500 |
| Services (supabase, analytics, ads, share) | ~400 |
| EventBus + Input + utils | ~200 |
| Config + data JSON | ~300 |
| CSS | ~150 |
| **TOTAL** | **~4,350** |

---

## 8. Stack Completo (Revisado)

| Camada | Tecnologia | Versao | Justificativa |
|---|---|---|---|
| **Game engine** | Phaser | 3.88.x | Battle-tested, Arcade Physics, camera, particles, audio integrados |
| **UI framework** | React | 18.x | Menus, HUD overlay, login, leaderboard em DOM |
| **Linguagem** | TypeScript | 5.x | Type safety para game code + UI |
| **Bundler** | Vite | 6.x | HMR instantaneo, build <10s |
| **Event bridge** | mitt | 3.x | 200 bytes, type-safe, React <-> Phaser |
| **Backend** | Supabase | - | Auth (Google OAuth + anonymous), PostgreSQL, RLS |
| **Hosting** | Cloudflare Pages | Free tier | Bandwidth ilimitado, CDN Brasil |
| **Analytics** | GA4 + GameAnalytics | - | Gratis |
| **Ads** | Google H5 Games Ads | Ad Placement API | Interstitial + rewarded |
| **Share** | Web Share API | Native | Zero dependencia |
| **PWA** | Workbox | 7.x | Pre-cache para offline + fast loads |
| **Package mgr** | pnpm | 10.x | Rapido, disk-efficient |
| **Sprite tool** | TexturePacker | - | Atlas otimizados com trim + rotation |
| **Tilemap** | Tiled | 1.11.x | JSON export para Phaser |

### Custo Mensal (MVP)

| Item | Custo |
|---|---|
| Cloudflare Pages | R$ 0 |
| Supabase (free tier) | R$ 0 |
| Google Analytics + GameAnalytics | R$ 0 |
| Dominio | ~R$ 3/mes |
| **TOTAL** | **~R$ 3/mes** |

Se viralizar (>50K MAU): Supabase Pro ($25/mes = ~R$ 130/mes). Ainda insignificante.

---

## 9. Riscos Tecnicos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| 1 | **React re-renders causam frame drops no Phaser** | Media | Alto | HUD updates via setState sao assincronos e nao bloqueiam o game loop. Phaser roda em requestAnimationFrame, React roda no microtask queue. Nao competem. Mas se HUD atualizar a cada frame (60x/s), o React DOM reconciliation pode custar. Mitigacao: throttle updates (max 10 HUD updates/segundo, nao 60). Score muda quando zumbi morre (evento), nao a cada frame. |
| 2 | **Parallax TileSprite tem artefatos visuais** | Media-Baixa | Medio | TileSprite com texturas nao-power-of-two pode ter seams. Mitigacao: garantir que textures de TileSprite tenham dimensoes POT (ou usar Phaser's TileSprite fix). Testar no dia 1. |
| 3 | **Supabase free tier rate-limited sob carga** | Baixa | Medio | Supabase free tier tem limites nao documentados agressivamente. Se 10K jogadores postam score ao mesmo tempo: pode throttle. Mitigacao: batch score submission (fila local, envia a cada 5s). Fallback: localStorage como cache, sync quando possivel. |
| 4 | **Google OAuth popup bloqueado em mobile browsers** | Media | Alto | Alguns browsers mobile bloqueiam popups de OAuth. Mitigacao: usar redirect mode (nao popup). Supabase suporta ambos. `redirectTo: window.location.origin`. Guest mode como fallback imediato -- jogador nao precisa de login para jogar, so para o leaderboard. |
| 5 | **Virtual joystick lag em devices low-end** | Media | Alto | Touch events no DOM sao rapidos, mas se o React re-render interferir: lag. Mitigacao: joystick component usa useRef para posicao (nao useState), evitando re-renders. Apenas a posicao visual do knob muda via style direto (nao via state). |
| 6 | **Phaser + React bundle size excessivo** | Baixa | Medio | Phaser (~350 KB gzip) + React (~45 KB gzip) + game code = ~550 KB JS. Dentro do budget. Mas se adicionar libs extras (framer-motion, zustand, etc.): pode crescer. Mitigacao: ZERO libs extras alem de mitt e supabase-js. React puro, CSS puro. |
| 7 | **Side-view parallax 7 layers = GPU bottleneck no A06** | Baixa | Alto | 7 layers = 7 draw calls adicionais. Total ~12 draw calls. Mali-G52 suporta centenas. Risco real e fill rate (quantos pixels o GPU precisa pintar por frame). Layers de 1920x120px com alpha blending sao pesadas. Mitigacao: layers distantes (L2, L3) com resolucao menor. Testar no dia 1 do PoC. |
| 8 | **Scope creep: "agora que tem React, vamos fazer X no DOM"** | Alta | Critico | React e tentador. "Vamos adicionar um chat." "Vamos fazer um profile editor." "Vamos meter um Tailwind." NAO. React existe para: MainMenu, HUDOverlay, GameOverScreen, LoginPage, LeaderboardPage, VirtualJoystick, AttackButton. 8 componentes. Nada mais. |

---

## 10. Nota Final do CTO

Reli meu documento anterior. Estava certo sobre o fundamental: Phaser 3.88, TypeScript, Vite, object pooling, Arcade Physics, texture atlas, 60fps no Galaxy A06. Tudo isso permanece.

O que muda com este documento e a camada ao redor do Phaser. React para UI e a decisao correta quando voce precisa de login, leaderboard e menus que nao sejam um pesadelo de posicionamento manual em canvas. Supabase para backend e a decisao correta quando voce precisa de auth + PostgreSQL e nao quer manter servidor.

A integracao React-Phaser e simples se voce respeitar a fronteira. Um EventBus. Um useRef para o container. Um useEffect para criar e destruir. Pronto. Se voce precisa de mais que isso, voce esta fazendo errado.

O side-view adiciona complexidade visual (7 parallax layers, sprites maiores, foreground) mas REMOVE complexidade logica (sem Y-sort, sem 8 direcoes de sprite, sem pathfinding 2D). Trade-off positivo. Menos codigo, mais impacto visual. Andre Guedes estava certo.

O budget de performance e confortavel: 176 sprites, 12 draw calls, 8 texture units, 3.5 MB total. O Galaxy A06 tem headroom de sobra. O risco nao e performance -- e disciplina. Nao adicionar "so mais uma feature". Nao meter Tailwind porque "e mais facil". Nao colocar state management global porque "e padrao no React".

Oito componentes React. Tres scenes Phaser. Um EventBus de 200 bytes. Um banco PostgreSQL com duas tabelas. Isso e tudo.

**Ship it.**

---

**John Carmack**
**CTO & Arquiteto de Engenharia**
**Abril 2026**
