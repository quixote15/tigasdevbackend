# Q1-01 — HORA EXTRA: Plano de Implementacao Frontend
### Frontend Implementation Plan | Quest Design Document | Capitulo 1
### Masahiro Sakurai — Game Feel & Frontend Architecture
### Abril 2026

---

> "Cada frame de animacao, cada efeito de impacto, cada transicao de tela importa. Nao porque o jogador vai notar conscientemente. Mas porque o corpo dele vai notar. E ele vai voltar pra jogar de novo."

---

## Premissas

Stack confirmada pelo `23-frontend-sideview-plan.md`:
- **Engine:** Phaser 3.88 com WebGL renderer
- **Frontend:** React 18 + Vite 5 + TypeScript
- **Physics:** Arcade Physics (AABB, sem rotacao)
- **Viewport:** 480x270px logicos, escala 2x/3x em CSS
- **Target FPS:** 60fps fixo
- **Plataformas:** Desktop browser + Mobile landscape (Android/iOS)

Este documento assume repo limpo. Sem assets externos ainda — usamos placeholders de cor ate os sprites chegarem. A arquitetura deve funcionar com ou sem arte final.

---

## ESTRUTURA DE PASTAS (setup inicial)

```
src/
  scenes/
    BootScene.ts          <- config Phaser, escala CSS
    PreloadScene.ts       <- carrega assets, progress bar
    CutsceneScene.ts      <- abertura narrada do Ze
    GameScene.ts          <- logica principal da quest
    GameOverScene.ts      <- tela "IMPRODUTIVO"
    VictoryScene.ts       <- Ze empurra o torniquete
  entities/
    Player.ts             <- controller, animacoes, HP
    Zombie.ts             <- base class (Burocrata)
    Carlao.ts             <- extends Zombie, dialogo especial
    Pickup.ts             <- vassoura, sanduiche, tablet
  systems/
    WaveSystem.ts         <- orquestra as 3 ondas da quest
    CombatSystem.ts       <- hitbox overlap, damage routing
    CombatFeedback.ts     <- hit-stop, flash, shake, particles
    ZombiePool.ts         <- object pool de zumbis
    TutorialSystem.ts     <- indicadores contextuais de controles
    CheckpointSystem.ts   <- salva estado pre-wave-3
    DialogueSystem.ts     <- caixas de texto do Ze e Carlao
    PickupSystem.ts       <- deteccao de coleta + efeitos
  ui/
    HUD.ts                <- HP bar + indicador de wave
    DamageNumbers.ts      <- numeros flutuantes
    Onomatopeias.ts       <- THWACK! pool de sprites
  config/
    ZombieConfigs.ts      <- stats de cada tipo de zumbi
    WeaponConfigs.ts      <- dano, durabilidade, animacao
    WaveConfigs.ts        <- ondas especificas da Q1-01
    AudioKeys.ts          <- constantes de chaves de audio
  react/
    App.tsx               <- monta o canvas do Phaser
    GameWrapper.tsx       <- useRef para o canvas + lifecycle
public/
  assets/                 <- sprites, tilesets (ver 23-frontend-sideview-plan.md)
  audio/                  <- ogg/mp3
  maps/                   <- tilemaps Tiled
```

---

## SCRIPTS NPM

```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "typecheck": "tsc --noEmit",
    "lint": "eslint src --ext .ts,.tsx"
  }
}
```

---

## FASES DE IMPLEMENTACAO

As fases sao sequenciais. Nao avance para a proxima sem o criterio de "feito" da fase atual estar verde. O criterio de feito e sempre testavel num browser aberto.

---

## FASE A — Player se move numa cena vazia

**Objetivo:** Ze aparece, anda para esquerda/direita, para com micro-desaceleracao. Keyboard funciona. Touch funciona em mobile. Nada mais.

### Tasks

**A1.** Inicializar repo com `npm create vite@latest` + TypeScript, instalar `phaser@3.88.0`.

**A2.** Criar `GameWrapper.tsx` que monta o canvas do Phaser num `div` via `useRef`. O componente destroi o jogo no cleanup do `useEffect` para evitar leak em hot-reload.

```typescript
// src/react/GameWrapper.tsx
import { useEffect, useRef } from 'react';
import Phaser from 'phaser';
import { BootScene } from '../scenes/BootScene';
import { GameScene } from '../scenes/GameScene';

export function GameWrapper() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const config: Phaser.Types.Core.GameConfig = {
      type: Phaser.WEBGL,
      width: 480,
      height: 270,
      parent: containerRef.current!,
      physics: { default: 'arcade', arcade: { gravity: { x: 0, y: 0 }, debug: false } },
      scene: [BootScene, GameScene],
    };
    const game = new Phaser.Game(config);
    return () => game.destroy(true);
  }, []);

  return <div ref={containerRef} style={{ imageRendering: 'pixelated' }} />;
}
```

**A3.** Criar `BootScene` que apenas chama `this.scene.start('GameScene')`. Nenhum asset ainda.

**A4.** Criar `Player.ts` como `Phaser.Physics.Arcade.Sprite`. Corpo de colisao de 16x36px. Stats de movimento: `WALK_SPEED = 120`, `ACCELERATION = 600`, `DECELERATION = 900` (ver detalhes no `23-frontend-sideview-plan.md`, secao 3.1). Placeholder visual: retangulo verde `setFillStyle(0x00FF00)` via Graphics — funciona sem nenhum sprite carregado.

**A5.** Criar input handler em `GameScene` que le `cursors` (teclado) e passa um `inputDir: {x: number}` para `player.update()`. Sem jump ainda.

**A6.** Criar joystick virtual para mobile: dois elementos HTML absolutamente posicionados sobre o canvas (outer ring + inner dot), com `pointermove`/`pointerdown`/`pointerup`. Joystick mapeia para o mesmo `inputDir.x`.

**A7.** `BootScene` configura a escala CSS: canvas renderiza em 480x270, CSS aplica `scale(2)` ou `scale(3)` dependendo de `window.devicePixelRatio`. Pixel art sem blur: `image-rendering: pixelated`.

**Criterio de feito:**
- Ze (retangulo) anda para direita e esquerda
- Ao soltar a tecla, Ze desacelera suavemente em ~4 frames (nao para instantaneamente)
- No mobile landscape, o joystick aparece e Ze responde ao toque
- Chrome DevTools mostra 60fps estavel na aba Performance

**Estimativa:** 3 pomodoros

**Riscos:**
- Hot-reload do Vite pode criar multiplas instancias do Phaser. O cleanup do `useEffect` (linha `game.destroy(true)`) resolve — confirme que esta ali antes de continuar.
- Joystick em iOS Safari: usar `touch-action: none` no CSS do container para evitar scroll da pagina capturar o toque.

---

## FASE B — Tilemap do Ministerio + colisao com chao

**Objetivo:** O cenario existe. Ze anda sobre o chao e bate nas paredes. Parallax dos backgrounds.

### Tasks

**B1.** Abrir Tiled (versao 1.10+). Criar mapa `ministerio_q1.tmj` com dimensoes `300 x 17` tiles de `16x16px` (4800px de largura total — 5 telas de 960px). Criar layers:
  - `ground` (TileLayer, colisao ativa)
  - `decoracao` (TileLayer, sem colisao)
  - `spawn_points` (ObjectLayer — posicoes de spawn de zumbis e itens)
  - `doors` (ObjectLayer — portas de spawn visual)

Usar um tileset placeholder monocromatico (cinza escuro para chao, cinza medio para paredes) ate os sprites do Ministerio chegarem.

**B2.** Exportar como JSON. Carregar em `PreloadScene`:
```typescript
this.load.tilemapTiledJSON('ministerio_map', 'maps/ministerio_q1.tmj');
this.load.image('ministerio_tiles', 'maps/tileset_ministerio.png');
```

**B3.** Em `GameScene.create()`, instanciar o tilemap e criar o layer de colisao:
```typescript
const map = this.make.tilemap({ key: 'ministerio_map' });
const tileset = map.addTilesetImage('ministerio_tiles', 'ministerio_tiles')!;
const groundLayer = map.createLayer('ground', tileset, 0, 0)!;
groundLayer.setCollisionByProperty({ collides: true });
this.physics.add.collider(this.player, groundLayer);
```

**B4.** Implementar parallax de 7 layers como descrito no `23-frontend-sideview-plan.md` secao 2. Para Q1-01 (interior do Ministerio), os layers sao adaptados:
  - L0: Retangulo bege (cor do Ministerio) — `scrollFactor: 0`
  - L1: Janelas ao fundo mostrando ceu azul — `scrollFactor: 0.05`
  - L2: Predio ao fundo (Congresso minusculo) — `scrollFactor: 0.1`
  - L3: Corredor do andar (fundo) — `scrollFactor: 0.4`
  - L4: Mesas, arquivos empilhados — `scrollFactor: 0.75`
  - L5: Chao/plataformas (tilemap) — `scrollFactor: 1.0`
  - L6: Entidades (player, zumbis) — `scrollFactor: 1.0`

`tilePositionX` dos TileSprites atualizado manualmente no `update()` baseado em `camX`.

**B5.** Camera segue Ze: `this.cameras.main.startFollow(player, true, 0.08, 0.08)`. Bounds limitados a largura do mapa. Deadzone de `80x40` para evitar micro-jitter.

**B6.** Adicionar as mesas como plataformas no tilemap (altura de 1 tile — 16px). Ze deve poder andar sobre elas. No Tiled, marcar tiles de mesa com `collides: true`.

**Criterio de feito:**
- Ze anda sobre o chao sem cair
- Ze bate nas paredes laterais das salas
- Ze sobe na mesa (um tile de altura)
- Parallax e visivel ao andar — backgrounds se movem em velocidades diferentes
- Sem pop-in visual nas bordas dos TileSprites ao scrollar

**Estimativa:** 4 pomodoros

**Riscos:**
- Tiled exporta coordenadas em pixels, Phaser espera tiles. Verificar `map.widthInPixels` vs `map.width * tileWidth`. Se o Ze estiver 16x menor ou maior, e esse bug.
- TileSprite com `setScrollFactor(0)` e parallax manual sao a combinacao correta. NAO usar `setScrollFactor(0.5)` em TileSprite — o Phaser move o objeto inteiro, nao o conteudo da textura, causando gap visual.

---

## FASE C — Combate corpo-a-corpo com vassoura contra dummy estatico

**Objetivo:** Ze ataca. Dummy recebe dano. Hit-stop, flash, screen shake. Numero de dano flutua. Dummy morre.

### Tasks

**C1.** Criar `WeaponConfigs.ts`:
```typescript
// src/config/WeaponConfigs.ts
export interface WeaponConfig {
  key: string;
  damage: number;
  durability: number;      // hits maximos (-1 = infinito)
  cooldown: number;        // ms entre ataques
  hitboxOffsetX: number;   // relativo ao player, em px logicos
  hitboxW: number;
  hitboxH: number;
  animKey: string;
  sfxKey: string;
}

export const WEAPONS: Record<string, WeaponConfig> = {
  soco: {
    key: 'soco', damage: 1, durability: -1, cooldown: 500,
    hitboxOffsetX: 20, hitboxW: 24, hitboxH: 20,
    animKey: 'player_attack_melee', sfxKey: 'sfx_punch'
  },
  vassoura: {
    key: 'vassoura', damage: 2, durability: 15, cooldown: 400,
    hitboxOffsetX: 28, hitboxW: 32, hitboxH: 20,
    animKey: 'player_attack_melee', sfxKey: 'sfx_carimbo'
  },
};
```

**C2.** Implementar `attackMelee()` no `Player.ts`. O ataque cria uma hitbox retangular temporaria na frente do Ze (posicao relativa ao `facingRight`). A hitbox existe por exatamente `1 frame` (ou um `delayedCall` de 16ms). O `CombatSystem` verifica overlap nesse frame.

```typescript
// src/entities/Player.ts
attackMelee(time: number): boolean {
  const weapon = this.currentWeapon;
  if (time < this.nextAttackTime) return false;
  if (this.animPriority >= 3) return false;

  this.nextAttackTime = time + weapon.cooldown;
  this.animState = 'attack_melee';
  this.animPriority = 2;
  this.play(weapon.animKey);

  // Durabilidade
  if (weapon.durability > 0) {
    weapon.durability--;
    if (weapon.durability <= 0) {
      this.scene.time.delayedCall(weapon.cooldown, () => this.equipWeapon('soco'));
    }
  }

  // Emite evento para CombatSystem calcular overlap
  this.scene.events.emit('playerAttack', {
    x: this.x + (this.facingRight ? weapon.hitboxOffsetX : -weapon.hitboxOffsetX),
    y: this.y - 10,
    w: weapon.hitboxW,
    h: weapon.hitboxH,
    weapon,
    attackerX: this.x,
  });

  return true;
}
```

**C3.** Criar `CombatSystem.ts` que ouve `playerAttack`, itera sobre zumbis ativos e verifica overlap com `Phaser.Geom.Rectangle.Overlaps`. Para cada zumbi atingido, chama `zombie.takeDamage()` e `combatFeedback.onHit()`.

**C4.** Implementar `CombatFeedback.ts` completo (ver `23-frontend-sideview-plan.md` secao 5):
  - `_applyHitStop(50ms)` — `timeScale = 0.05`, restaura em `delayedCall`
  - `flashSprite(target, 16ms)` — `setTintFill(0xffffff)`, `clearTint()`
  - `cameras.main.shake(40, 0.003)` para hit normal
  - Emissao de particulas de tinta na posicao do hit
  - `DamageNumbers.spawn()` — numero flutua 40px para cima em 600ms

**C5.** Criar dummy `Enemy.ts` (extends `Phaser.Physics.Arcade.Sprite`) com HP fixo de 30 e sem IA — fica parado. Colocar no mapa via ObjectLayer do Tiled.

**C6.** Quando o dummy chega a 0 HP, play na animacao de morte (retangulo desaparece com scale tween 1→0 em 300ms). `CombatFeedback.onKill()` dispara partículas extras e shake maior.

**C7.** Botao de ataque para mobile: circulo no canto inferior direito do canvas (HTML, sobre o Phaser). `pointerdown` chama `player.attackMelee()`.

**Criterio de feito:**
- Pressionar Z/Enter/botao mobile dispara o ataque
- O dummy pisco de branco por 1 frame ao ser atingido
- O jogo congela visivelmente por ~50ms (hit-stop) a cada acerto — testavel em slow-motion no Chrome DevTools
- Numero de dano sobe e desaparece em 600ms
- Tela treme suavemente a cada hit
- Apos 30 de dano acumulado, dummy morre com animacao
- Vassoura de dano 2 quebra apos 15 hits. Ze continua atacando com soco de dano 1.

**Estimativa:** 5 pomodoros

**Riscos:**
- Hit-stop via `timeScale`: `time.delayedCall` usa tempo REAL no Phaser, nao timeScale. Isso e correto — o callback de restaurar timeScale dispara mesmo com o jogo "congelado". Mas tweens de UI (numeros flutuantes) tambem sao afetados pelo timeScale. Solucao: usar `this.tweens.timeScale` separado, ou criar os tweens de UI na `UIScene` (cena separada com timeScale proprio).
- Hitbox de ataque: nunca use Arcade Physics para a hitbox de ataque melee. Use sobreposicao geometrica manual (`Phaser.Geom.Rectangle.Overlaps`). Arcade Physics hitbox existente e um corpo solido persistente — a hitbox de ataque e temporaria e nao deve ter fisica propria.

---

## FASE D — Burocrata-Zumbi com IA basica

**Objetivo:** O primeiro inimigo real. Anda em direcao ao Ze, ataca ao chegar perto, leva dano, morre. Dialogo de "protocolo... carimba aqui..." ao spawnar.

### Tasks

**D1.** Criar `ZombieConfigs.ts` com stats do Burocrata:
```typescript
// src/config/ZombieConfigs.ts
export const ZOMBIE_CONFIGS: Record<string, ZombieConfig> = {
  burocrata: {
    type: 'burocrata',
    hp: 30,            // 3 hits da vassoura (dano 2 nao bate em 30 exato, mas tem soco de backup)
    speed: 40,         // px/s — muito lento, proposital
    damage: 10,
    attackRange: 18,
    attackCooldown: 1500,
    scoreValue: 10,
    hitboxW: 16, hitboxH: 34,
    hitboxOffX: 14, hitboxOffY: 16,
  },
};
```

**D2.** Implementar `Zombie.ts` com maquina de estados simples: `walk` → `attack` (quando distancia <= attackRange) → `hurt` (ao tomar dano) → `dead`. Ver codigo completo em `23-frontend-sideview-plan.md` secao 4.1.

**D3.** Criar `ZombiePool.ts` com pool inicial de 20 instancias de Burocrata. `get()` retorna instancia inativa, `release()` a recicla. Nenhum `new Zombie()` durante o gameplay — somente no `create()` da cena.

**D4.** Implementar dialogo contextual do Burocrata. Ao spawnar, `DialogueSystem` exibe texto flutuante acima do sprite por 3 segundos:
```typescript
// src/systems/DialogueSystem.ts
export class DialogueSystem {
  spawnFloatingText(scene: Phaser.Scene, x: number, y: number, text: string): void {
    const t = scene.add.text(x, y - 40, text, {
      fontFamily: 'monospace', fontSize: '6px', color: '#C8C8C8',
      stroke: '#000000', strokeThickness: 1,
    }).setDepth(600).setOrigin(0.5);

    scene.tweens.add({
      targets: t, y: y - 55, alpha: 0,
      duration: 3000, ease: 'Sine.easeIn',
      onComplete: () => t.destroy(),
    });
  }
}
```

Textos de spawn do Burocrata (sorteado aleatoriamente):
- "protocolo... carimba aqui..."
- "assina em tres vias..."
- "processo numero... 0001..."

**D5.** Registrar colisao zumbi x chao (`physics.add.collider(zombieGroup, groundLayer)`) para que zumbis andem sobre o tilemap sem cair.

**D6.** Atacar o Burocrata com Ze deve produzir o som de carimbo batendo em papel (`sfx_carimbo`). Usar placeholder `AudioContext.createOscillator()` ate o audio final chegar — um beep curto e suficiente para testar o timing.

**D7.** Ao morrer, Burocrata executa animacao de morte e retorna ao pool. `CombatFeedback.onKill()` dispara.

**Criterio de feito:**
- Burocrata anda lentamente em direcao ao Ze
- Ao entrar no `attackRange`, para e ataca (Ze perde HP)
- Burocrata toma dano, faz flash branco, sofre knockback horizontal de ~200px
- Apos 30 de dano total, Burocrata morre, retorna ao pool
- Segundo Burocrata pode ser spawnado imediatamente (pool funciona)
- Zero `new Zombie()` no profiler durante o gameplay (confirmar no Chrome Memory tab)

**Estimativa:** 4 pomodoros

**Riscos:**
- Sincronizacao de ataque vs dano: o `zombieAttack` emitido pela IA precisa ser resolvido pelo `CombatSystem` no mesmo frame em que o frame de ataque da animacao e exibido. Nao no frame seguinte. Usar o evento `animationupdate` do Phaser para detectar o frame especifico de ataque (ex: frame 2 de 4 da animacao de ataque).
- Pool com tipos diferentes: a Fase D tem so Burocrata. A Fase E adiciona tipos. Garantir que `ZombiePool` e keyed por tipo desde o inicio (`pool['burocrata']`, `pool['carlao']`), mesmo que por ora so `burocrata` seja populado.

---

## FASE E — Sistema de waves com as 3 ondas da Q1-01

**Objetivo:** As 3 ondas da quest funcionam em sequencia. Wave 1 (corredor), Wave 2 (sala de reunioes com stealth), Wave 3 (escada rolante com 6 zumbis em pares). Checkpoint salvo antes da Wave 3.

### Tasks

**E1.** Criar `WaveConfigs.ts` especifico para Q1-01:
```typescript
// src/config/WaveConfigs.ts
export interface WaveConfig {
  id: number;
  label: string;
  spawns: SpawnEvent[];
  completionCondition: 'all_dead' | 'player_reaches_x';
  completionX?: number;  // para completionCondition 'player_reaches_x'
  checkpoint?: boolean;
}

export const Q1_01_WAVES: WaveConfig[] = [
  {
    id: 1,
    label: 'HORA EXTRA INVOLUNTARIA',
    spawns: [
      { type: 'burocrata', count: 1, delay: 0,    spawnX: 'right_edge' },
      { type: 'burocrata', count: 1, delay: 3000, spawnX: 'door_b7' },
    ],
    completionCondition: 'all_dead',
  },
  {
    id: 2,
    label: 'SALA DE REUNIOES',
    spawns: [
      { type: 'burocrata', count: 2, delay: 0,    spawnX: 'sala_reunioes_back', grouped: true },
      { type: 'burocrata', count: 2, delay: 0,    spawnX: 'sala_reunioes_door', alert: true },
    ],
    completionCondition: 'all_dead',
  },
  {
    id: 3,
    label: 'ESCADA ROLANTE',
    spawns: [
      { type: 'burocrata', count: 2, delay: 0,    spawnX: 'escada_base' },
      { type: 'burocrata', count: 2, delay: 4000, spawnX: 'escada_base' },
      { type: 'burocrata', count: 2, delay: 8000, spawnX: 'escada_base' },
    ],
    completionCondition: 'all_dead',
    checkpoint: true,  // checkpoint salvo AO INICIAR esta wave
  },
];
```

**E2.** Criar `WaveSystem.ts` que processa `Q1_01_WAVES` em sequencia:
- Exibe o titulo da wave (`label`) no centro da tela por 2 segundos (texto grande, estilo jornal satirico como descrito no design doc)
- Processa `spawns` respeitando `delay`
- Ouve `zombieDied` e verifica `completionCondition`
- Ao completar uma wave, aguarda 1.5 segundos antes de iniciar a proxima
- Emite `waveComplete` e `allWavesComplete`

**E3.** Implementar `CheckpointSystem.ts`:
```typescript
// src/systems/CheckpointSystem.ts
export interface CheckpointState {
  playerHP: number;
  playerX: number;
  waveIndex: number;
  weaponKey: string;
  weaponDurability: number;
}

export class CheckpointSystem {
  private savedState: CheckpointState | null = null;

  save(state: CheckpointState): void {
    this.savedState = { ...state };
  }

  restore(): CheckpointState | null {
    return this.savedState;
  }

  hasSave(): boolean {
    return this.savedState !== null;
  }
}
```

O estado e salvo em memoria (nao `localStorage`) — checkpoint vale somente para a sessao atual da quest. Ao iniciar a Wave 3, `WaveSystem` chama `checkpoint.save({ playerHP, playerX, waveIndex: 2, ... })`.

**E4.** Implementar logica de stealth para Wave 2. Quando Ze esta agachado sob uma mesa (`isCrouching = true`), os Burocratas em modo `alert: false` nao detectam Ze (raio de deteccao reduzido de infinito para 0). Os dois Burocratas `alert: true` acordam se Ze se mover ou atacar. Agachar: tecla S / botao mobile "abaixar".

**E5.** Exibir contador de wave no HUD (canto superior direito): "WAVE 1/3". Atualiza ao iniciar cada nova wave.

**E6.** Exibir o closet com a vassoura antes da Wave 1. Vassoura e um `Pickup` com brilho dourado (tween de `alpha` 1.0↔0.6 em loop de 400ms). Ze coleta ao passar por cima. `PickupSystem` equipa a vassoura e exibe o texto "VASSOURA DE PALHA — Dano: 2 | Durabilidade: 15 hits" por 1.5 segundos.

**E7.** Primeiro Burocrata spawna exatamente 1 segundo apos a vassoura ser coletada (nao antes). Isso e garantido por `EventEmitter`: `pickupSystem.on('weaponPickedUp', () => waveSystem.startWave(1))`.

**Criterio de feito:**
- Titulo de cada wave aparece e desaparece corretamente
- Wave 1: 2 Burocratas em sequencia (3s de intervalo). Ao matar ambos, Wave 2 inicia apos 1.5s.
- Wave 2: Ze pode passar pela sala sem acordar os 2 Burocratas dormentes se estiver agachado
- Wave 3: 6 Burocratas chegam em pares de 4 em 4 segundos
- Checkpoint salvo antes da Wave 3: matar Ze durante a Wave 3 e reiniciar retorna ao inicio da Wave 3 com o HP salvo, nao ao inicio da quest
- Vassoura coletada antes da Wave 1 e nunca antes do Ze entrar na tela do closet

**Estimativa:** 6 pomodoros

**Riscos:**
- Sincronizar o spawn da Wave 2 com o jogador chegando na sala: usar `player_reaches_x` como trigger geografico (quando `player.x >= sala_reunioes_trigger_x`, Wave 2 ativa), nao tempo. O jogador pode demorar na Wave 1.
- Stealth detection: nao usar raio circular. Usar um "field of view" retangular na frente do zumbi (`Phaser.Geom.Rectangle` projetado na direcao que ele enfrenta). Mais simples e mais previsivel para o jogador.

---

## FASE F — Carlao (inimigo narrativo especial)

**Objetivo:** Carlao aparece antes da Wave 3 (escada rolante). Tem dialogo ao ser visto, ao tomar hit e ao morrer. Solta o tablet como item narrativo.

### Tasks

**F1.** Criar `Carlao.ts` extends `Zombie`. Diferenca de stats: HP 50 (dano 2 da vassoura = 25 hits, ou combinacao de vassoura + soco). Velocidade 50px/s.

**F2.** Implementar dialogo contextual com maquina de estados propria:
```typescript
// src/entities/Carlao.ts
export class Carlao extends Zombie {
  private dialogueState: 'initial' | 'hit1' | 'dead' = 'initial';

  onDetectPlayer(): void {
    if (this.dialogueState !== 'initial') return;
    this.scene.dialogueSystem.showNPCDialogue(
      this, 'Ze... voce nao vai acreditar... o trending topic...'
    );
  }

  takeDamage(amount: number, knockbackDir: number): void {
    super.takeDamage(amount, knockbackDir);
    if (this.dialogueState === 'initial' && this.hp < this.maxHp) {
      this.dialogueState = 'hit1';
      this.scene.dialogueSystem.showNPCDialogue(this, 'Isso... vai virar meme...');
    }
  }

  protected _die(): void {
    this.dialogueState = 'dead';
    // Dropar tablet no chao
    this.scene.pickupSystem.spawnPickup('tablet', this.x, this.y);
    super._die();
  }
}
```

**F3.** Implementar efeito de morte especial do Carlao: ao morrer, tocar 3 vezes o som de notificacao de Twitter/X em pitch descendente (`sfx_twitter` com `rate` de 1.0, 0.75, 0.5`). Particulas de "tuites voando" (sprites de texto pequeno do atlas de particulas) explodem da posicao do Carlao.

**F4.** Tablet como item narrativo: `Pickup` com icone de tablet. Ao coletar, `DialogueSystem` abre um painel de inspecao com 3 tuites satiricos estilizados (texto mockado, nao HTML externo). Painel fecha ao pressionar qualquer botao.

**F5.** Posicionar Carlao no nivel via ObjectLayer do Tiled (objeto nomeado `carlao_spawn`). `WaveSystem` le a posicao do mapa, nao tem coordenadas hardcoded no codigo.

**Criterio de feito:**
- Carlao aparece com camisa polo laranja e cracha "CARLAO — COMUNICACAO INSTITUCIONAL" (ou placeholder de cor correspondente)
- Dialogo inicial dispara ao Ze entrar no range de deteccao
- Dialogo de hit dispara exatamente no primeiro hit recebido (nao nos subsequentes)
- Ao morrer: 3 sons de notificacao descendentes + particulas de tuites
- Tablet fica no chao. Coletar abre painel com tuites satiricos. Fechar volta ao jogo sem interrupcao.

**Estimativa:** 3 pomodoros

**Riscos:**
- Dialogo de Carlao vs dialogo do Burocrata: ambos usam `DialogueSystem`, mas Carlao tem dialogos mais longos e com estado. Evitar colocar logica de estado de dialogo no `DialogueSystem` global — cada entidade gerencia seu proprio `dialogueState`.
- Sons em pitch descendente: `Phaser.Sound` tem `rate` property que muda o pitch. `sfx_notificacao.play({ rate: 0.75 })`. Testar em iOS Safari — Web Audio API tem restricoes de autoplay que o Phaser nao contorna automaticamente. Exigir interacao do usuario antes do primeiro som (o toque no botao de inicio da quest conta).

---

## FASE G — HUD (HP bar + contador de waves)

**Objetivo:** HUD responsiva, clara, que nunca atrapalha o jogo. HP pulsa ao tomar dano. Wave muda com animacao.

### Tasks

**G1.** Criar `HUDScene` como cena Phaser separada (nao overlay React). Cenas paralelas no Phaser compartilham o mesmo renderer mas tem cameras independentes — a HUD tem camera fixa (sem scroll) enquanto a `GameScene` scrollar.

```typescript
// src/scenes/HUDScene.ts
export class HUDScene extends Phaser.Scene {
  private hpBar!: Phaser.GameObjects.Rectangle;
  private hpBarBg!: Phaser.GameObjects.Rectangle;
  private waveText!: Phaser.GameObjects.Text;

  create(): void {
    // HP Bar: canto superior esquerdo
    const barX = 8, barY = 8, barW = 60, barH = 6;
    this.hpBarBg = this.add.rectangle(barX, barY, barW, barH, 0x3A1A0A).setOrigin(0);
    this.hpBar = this.add.rectangle(barX, barY, barW, barH, 0xC8381A).setOrigin(0);

    // Texto "HP" acima da barra
    this.add.text(barX, barY - 8, 'HP', {
      fontFamily: 'monospace', fontSize: '6px', color: '#F0E8D0'
    });

    // Wave counter: canto superior direito
    this.waveText = this.add.text(472, 8, 'WAVE 1/3', {
      fontFamily: 'monospace', fontSize: '7px', color: '#F0E8D0',
      stroke: '#000000', strokeThickness: 1,
    }).setOrigin(1, 0);

    // Ouvir eventos da GameScene
    this.scene.get('GameScene').events.on('playerHPChanged', this._onHPChange, this);
    this.scene.get('GameScene').events.on('waveChanged', this._onWaveChange, this);
  }

  private _onHPChange(current: number, max: number): void {
    const ratio = current / max;
    this.hpBar.width = 60 * ratio;

    // Pulso de atencao ao tomar dano (HP diminuiu)
    this.tweens.add({
      targets: this.hpBar,
      scaleY: { from: 1.5, to: 1 },
      duration: 200, ease: 'Bounce.easeOut',
    });
  }

  private _onWaveChange(current: number, total: number): void {
    this.waveText.setText(`WAVE ${current}/${total}`);
    this.tweens.add({
      targets: this.waveText,
      scaleX: { from: 1.3, to: 1 }, scaleY: { from: 1.3, to: 1 },
      duration: 300, ease: 'Back.easeOut',
    });
  }
}
```

**G2.** Adicionar HUDScene ao config do Phaser e usar `this.scene.launch('HUDScene')` no `create()` da `GameScene`.

**G3.** Indicador de durabilidade da vassoura: pequenos pontos abaixo da HP bar. 15 pontos, um some a cada hit. Implementado como array de 15 retangulos de 3x3px.

**G4.** Quando vassoura quebra e Ze fica so com soco, o indicador de durabilidade desaparece com fade-out de 300ms. Icone de "punho" aparece no lugar.

**G5.** Quando Ze leva o primeiro hit de qualquer inimigo: HP bar pulsa 3 vezes rapidamente (tween `alpha 1→0.3→1` em 150ms, `repeat: 2`). Ze exibe texto flutuante "puta que pariu!" censurado como "*#@!" em estilo HQ.

**Criterio de feito:**
- HP bar dimunui proporcionalmente ao dano recebido
- HP bar pulsa ao ser reduzida (animacao de Bounce)
- Contador de wave atualiza com animacao de scale ao inicio de cada wave
- Durabilidade da vassoura visivel e decrementada a cada hit
- HUD NUNCA scrollar junto com o mundo — camera fixa confirmada

**Estimativa:** 2 pomodoros

**Riscos:**
- Cenas paralelas no Phaser: a `HUDScene` precisa ser lancada com `this.scene.launch('HUDScene')`, nao `this.scene.start()`. `launch` roda a cena em paralelo. `start` substituiria a cena atual.
- EventEmitter entre cenas: usar `this.scene.get('GameScene').events.on(...)` funciona, mas gera acoplamento direto. Alternativa mais limpa: usar um EventBus singleton (`EventEmitter` do Node importado via `import { EventEmitter } from 'events'` ou `mitt`). Para MVP, acoplamento direto e aceitavel.

---

## FASE H — Cutscene de abertura (narraçao do Ze)

**Objetivo:** A abertura da quest exatamente como descrita no design doc. Tela preta, texto em fade, Ze sentado na cadeira, naracao interna, o Carlao levantando.

### Tasks

**H1.** Criar `CutsceneScene.ts` que roda antes de `GameScene`. Estrutura em blocos sequenciais:

```typescript
// src/scenes/CutsceneScene.ts
type CutsceneBlock = {
  type: 'fade_text' | 'dialogue' | 'animation' | 'wait';
  text?: string;
  duration: number;
  speaker?: 'narrator' | 'ze' | 'carlao';
};

const HORA_EXTRA_OPENING: CutsceneBlock[] = [
  { type: 'fade_text', text: '8 de janeiro de 2023. 14h47.', duration: 2500 },
  { type: 'animation', duration: 1000 },  // Ze sentado na cadeira, ventilador
  { type: 'dialogue', speaker: 'ze',
    text: 'Hora extra voluntaria. Voluntaria entre aspas — o Carlao me disse que quem ficasse ate as 18h levava o dia como produtividade dobrada no relatorio. Eu nem sei o que isso significa, mas pareceu bem.',
    duration: 0 },  // duration 0 = aguarda input do jogador
  { type: 'animation', duration: 500 },   // vidro rachandos
  { type: 'dialogue', speaker: 'ze', text: 'Isso... nao e manifestacao normal.', duration: 0 },
  { type: 'animation', duration: 1500 },  // Carlao levantando
  { type: 'wait', duration: 800 },
  // -> inicia GameScene
];
```

**H2.** `DialogueSystem.showCutsceneDialogue()`: caixa de texto no canto inferior da tela (20px de margem de cada lado, 50px de altura). Background semi-transparente preto. Nome do personagem em destaque. Texto aparece letra por letra (typewriter effect a 40ms por caractere). Pressionar qualquer botao avanca.

**H3.** Sprite do Ze sentado na cadeira. Enquanto o ventilador gira (tween de rotacao leve no asset do ventilador), Ze olha pela janela. Animacao idle simples (Ze pisca a cada 3-4 segundos).

**H4.** Ao quebrar o vidro: `cameras.main.shake(300, 0.008)` + som de vidro. Depois, o Carlao levanta com animacao de "rise" (scale de 0.8 para 1.0 em 400ms).

**H5.** Titulo de wave aparece no centro: "WAVE 1: HORA EXTRA INVOLUNTARIA" em fonte grande, cor vermelha, estilo jornal satirico. Entra com fade-in de 300ms, fica 2 segundos, sai com fade-out. Entao controles sao liberados e `GameScene` inicia.

**H6.** Botao "PULAR" no canto superior direito do canvas. Ao pressionar, cutscene avanca para o ultimo bloco e `GameScene` inicia imediatamente. Critico para jogadores que recomecam apos game over.

**Criterio de feito:**
- Sequencia completa roda sem input (modo cinematografico)
- Cada dialogo aguarda input antes de avancar
- Botao "pular" pula toda a cutscene
- Ao final, transicao suave para `GameScene` (fade-out 500ms, fade-in 500ms)
- Em segundo playthrough: cutscene pode ser pulada imediatamente sem assistir nada

**Estimativa:** 4 pomodoros

**Riscos:**
- Typewriter effect e bloqueante se implementado com `setInterval` — usar tween encadeado ou `time.addEvent` do Phaser que respeita o ciclo de update.
- "Aguarda input" num sistema baseado em eventos: o bloco com `duration: 0` precisa registrar um listener `once('pointerdown', next)` e `once('keydown', next)`. Garantir que o listener e removido apos o avanco para nao duplicar eventos.

---

## FASE I — Game Over + Vitoria

**Objetivo:** As duas telas finais da quest. Game Over com o carimbo "IMPRODUTIVO". Vitoria com Ze empurrando o torniquete e encontrando Dona Marta.

### Tasks

**I1.** Criar `GameOverScene.ts`. Ao receber o evento `playerDied` emitido pelo Player:
  - Fade-out de 800ms para a GameScene
  - Animar Ze caindo no chao (animacao `player_death` finaliza)
  - Apos 1 segundo, mostrar Burocrata se ajoelhando e carimbando "IMPRODUTIVO" na testa do Ze
  - Texto na tela: "Hora extra encerrada. Motivo: apocalipse zumbi."
  - Subtexto: "Tente novamente?" com opcoes "SIM" e "NAO" (NAO volta ao menu principal)

**I2.** Resposta ao "SIM" no Game Over:
  - Se `CheckpointSystem.hasSave()`: restaura estado do checkpoint (HP, arma, posicao X, wave index) e reinicia a partir da Wave 3
  - Se nao tem checkpoint (morreu antes da Wave 3): reinicia a quest do inicio, exibe a cutscene (a menos que ja tenha sido pulada — salvar flag `hasSeenOpeningCutscene` em memoria)

**I3.** Criar `VictoryScene.ts`. Ao Ze atingir o `completionX` do tilemap (posicao do torniquete de saida):
  - Ze executa animacao de "empurrar torniquete" (sprite frame especifico)
  - Ze cai do outro lado ofegante
  - Janela do edificio atras e quebrada por um Burocrata (efeito visual: objeto de vidro cai em fragmentos — particulas)
  - Dialogo: Ze: "Pronto. Hora extra cancelada."
  - Cutscene final: Ze e Dona Marta no telheiro. Dialogue blocks em sequencia.
  - Fade-out final com texto "PROXIMO: Q1-02 — CORREDOR DOS MORTOS"

**I4.** Calcular e exibir pontuacao na tela de vitoria:
  - `kills x 10 + hpRestante x 5 + bonusTempo`
  - Se jogador usou stealth na Wave 2: exibir badge "FANTASMA DO FUNCIONALISMO" +200 pts
  - Animacao de contagem de pontos (numeros sobem de 0 ate o total em 1.5 segundos)

**I5.** Salvar no `localStorage` que Q1-01 foi completada. Desbloqueio do Burocrata-Zumbi no Bestiario (estado persistido entre sessoes).

**Criterio de feito:**
- Ze morrendo mostra carimbo "IMPRODUTIVO" apos 1 segundo
- "Tente novamente?" funciona: com checkpoint retorna a Wave 3, sem checkpoint reinicia a quest
- Ze chegando ao torniquete dispara a animacao de vitoria sem interrupcao de gameplay
- Cutscene final com Dona Marta completa, incluindo os 4 dialogos do design doc
- Pontuacao exibida com bonus de stealth quando aplicavel
- `localStorage` persistido (verificar em DevTools > Application > Local Storage)

**Estimativa:** 4 pomodoros

**Riscos:**
- Game Over durante a cutscene de abertura (improvavel mas possivel via bug): o Player deve ter `isInvincible = true` durante qualquer cutscene. Simples de garantir: setar `player.isInvincible = true` no `create()` da CutsceneScene e setar `false` quando GameScene assume controle.
- Pontuacao de tempo: calcular `tempoDecorrido` como `Date.now() - questStartTime`. Salvar `questStartTime` no momento em que o controle e liberado ao jogador (nao no inicio da cutscene).

---

## FASE J — Polish (o que transforma "funciona" em "wow")

**Objetivo:** Sem novas mecanicas. So camadas de feedback sensorial que fazem o jogo parecer vivo.

Esta fase nunca e cortada. Se o prazo aperta, corta-se features. Nunca o polish.

### Tasks

**J1.** Sonomatopeias como sprites (nao texto): implementar `OnomatopeiaPool` com pool de 10 sprites do atlas. THWACK ao acertar Burocrata. SLAP ao acertar Carlao. TALKEI? ao Carlao falar. Ver `23-frontend-sideview-plan.md` secao 5.3. Os sprites devem aparecer ligeiramente rotacionados (angulo aleatorio entre -15 e +15 graus) para parecerem naturais.

**J2.** Particulas de papel/santinhos ao matar Burocrata: ao morrer, 4-6 particulas de papel voam em arco parabolico e caem no chao. Permanecem no chao por 5 segundos antes de fazer `setVisible(false)`. Acumulo de papel no chao apos multiplas mortes e efeito visual importante — mostre o rastro do combate.

**J3.** Parallax de particulas de poluente verde nas janelas: particulas pequenas verdes derivam horizontalmente com velocidade muito baixa (0.5px/s) em loop. Sao da `UIScene` (camera fixa) e reforam o perigo externo sem distrair do gameplay.

**J4.** Screen shake calibrado por contexto:
  - Hit normal em Burocrata: `shake(40, 0.003)` — quase imperceptivel
  - Kill de Burocrata: `shake(80, 0.005)` — notavel
  - Morte do Carlao: `shake(150, 0.009)` — dramatico
  - Game Over (Ze morre): `shake(300, 0.015)` — brutal

**J5.** Hit-stop calibrado:
  - Hit normal: 50ms (`timeScale = 0.05`)
  - Hit crit (ultimo hit, kill): 83ms
  - Game Over: 200ms de freeze total + slow-motion de 1 segundo (`timeScale = 0.1`) antes de fade-out

**J6.** Animacao de vassoura ao coletar: Ze segura a vassoura na altura do peito com expressao "serve" (frame especifico da animacao de coleta). Duracao de 600ms antes de voltar ao idle. Ze NAO sorri. E pragmatico.

**J7.** Radio de fundo: audio `bgm_mpb_distorcida` comeca ao iniciar a quest. Ao spawnar o primeiro zumbi, a musica distorce progressivamente — implementado como segundo AudioNode com filtro de distorcao cujo `gain` aumenta de 0 a 0.4 em 3 segundos. Ao chegar no telheiro de saida, a musica para abruptamente. Silencio total por 2 segundos antes dos dialogos de Dona Marta.

**J8.** Micro-bounce no Ze ao pousar numa plataforma: ao detectar que Ze estava em queda livre e agora `body.blocked.down` e true, aplicar tween de `scaleY: {from: 0.85, to: 1}` em 80ms com ease `Bounce.easeOut`. Squash-and-stretch classico.

**J9.** Vibração haptica no mobile:
  - Hit normal: `navigator.vibrate(12)` — curto
  - Kill: `navigator.vibrate(30)` — medio
  - Game Over: `navigator.vibrate([50, 30, 80])` — padrao ritmico

**J10.** Indicadores de tutorial (seta animada sobre primeira mesa, seta sobre primeira vassoura) somem permanentemente apos o primeiro uso bem-sucedido da mecanica. Implementados como sprites pulsantes (`alpha` 1.0↔0.5 em loop). Nunca reaparecem na mesma sessao.

**Criterio de feito para Fase J (inteiro):**
- Um playtester novo (nunca viu o jogo) sorri ou ri em pelo menos 1 momento nos primeiros 2 minutos
- Ao acertar um Burocrata, a sensacao e de peso — identificavel sem audio (testar com volume zerado)
- A morte do Carlao produz um momento memoravel e compartilhavel
- Em mobile, vibracoes confirmam impactos sem ser intrusivas (testar em 3 devices diferentes)
- Nenhuma das animacoes de polish cria frame drops (confirmar com Chrome DevTools Performance)

**Estimativa:** 6 pomodoros (distribuidos ao longo de todas as fases — polish e incremental)

**Riscos:**
- `navigator.vibrate` nao funciona em iOS Safari (bloqueado pela Apple). Sem fallback necessario — simplesmente nao vai vibrar em iOS. Nao cravar comportamento.
- Acumulacao de particulas de papel: definir limite maximo de 30 sprites de papel no chao ao mesmo tempo. Pool gerenciado separadamente.
- Hit-stop de 200ms no Game Over interfere com o fade-out: o tween de fade-out deve ser criado DEPOIS que o `timeScale` volta a 1.0. Usar `time.delayedCall` para enfileirar, nao `setTimeout` (que ignora `timeScale`).

---

## PONTOS DE POLISH QUE NAO PODEM SER CORTADOS

Estes 5 itens definem se o jogo tem "feel" ou nao tem. Sem eles, o jogo funciona mas nao convence.

**1. Hit-stop de 50ms.**
O cerebro humano processa impacto fisico em parte pelos micro-pausas de movimento. Sem hit-stop, socos parecem toques. Com hit-stop, parecem pancadas. 50ms e o minimo. Nao negociar.

**2. Flash branco de 1 frame no inimigo.**
Confirmacao visual instantanea de que o hit registrou. Sem isso, o jogador nao tem certeza se acertou. Com isso, e inequivoco. Especialmente importante em mobile onde nao ha feedback tatil de botao.

**3. Texto flutuante de dano.**
O numero sobe e desaparece. Parece pequeno. E o que faz o jogador saber que esta progredindo. Sem isso, derrotar um Burocrata e abstrato. Com isso, e matematicamente satisfatorio.

**4. Dialogo do Burocrata ao spawnar.**
"protocolo... carimba aqui..." e o momento de humor que ancora o tom do jogo. Se isso nao funcionar, o Burocrata-Zumbi e so mais um inimigo generico de jogo indie. Com o dialogo, e uma piada de escritorio que virou arma. Nao cortar.

**5. Silencio total ao chegar no telheiro de saida.**
A musica para. So vento e tumulto distante. Esse contraste e o momento de respiracao que faz o jogador sentir que sobreviveu de verdade. Se a musica continuar tocando, o momento se perde completamente.

---

## CHECKLIST FINAL (antes de mandar pra QA/playtest)

### Funcional
- [ ] Quest completa de ponta a ponta sem crashes em Chrome, Firefox e Safari
- [ ] Game Over no inicio (sem checkpoint) reinicia a cutscene corretamente
- [ ] Game Over apos Wave 3 inicia (checkpoint) funciona e restaura HP/arma corretos
- [ ] Stealth na Wave 2 concede bonus "FANTASMA DO FUNCIONALISMO" na tela de vitoria
- [ ] Vassoura quebra apos 15 hits e Ze continua com soco (sem arma vazia)
- [ ] Tablet do Carlao e coletavel e exibe os tuites satiricos

### Feel / Feedback
- [ ] Hit-stop de 50ms visivel a olho nu (testar em slow-mo no DevTools)
- [ ] Flash branco confirma hit em 100% dos acertos
- [ ] Screen shake proporcional (hit < kill < Game Over)
- [ ] Onomatopeias THWACK/SLAP aparecem com rotacao aleatoria (nao todas iguais)
- [ ] Dialogo de Burocrata aparece ao spawnar (pelo menos 70% dos spawns)
- [ ] Silencio ao entrar no telheiro de saida

### Narrativa
- [ ] Todos os dialogos da cutscene de abertura presentes e na ordem correta
- [ ] Botao "pular" cutscene funciona
- [ ] Cutscene final com Dona Marta completa (4 falas)
- [ ] "PROXIMO: Q1-02 — CORREDOR DOS MORTOS" aparece no fade-out

### Performance
- [ ] 60fps estavel em Chrome Desktop (DevTools Performance tab, 5 minutos de gameplay)
- [ ] 30fps+ em Android mid-range simulado (Chrome DevTools device throttling: "Mid-tier mobile")
- [ ] Zero `new Zombie()` durante gameplay (Memory tab, heap estavel durante waves)
- [ ] Zero memory leaks: reiniciar a quest 5x seguidas, heap nao cresce indefinidamente

### Mobile
- [ ] Joystick responsivo em landscape (iPhone SE landscape + Galaxy A50 landscape)
- [ ] Botao de ataque acessivel com polegar direito sem cobrir a area central de jogo
- [ ] Canvas nao scrollar (touch-action: none ativo)
- [ ] Som funciona apos primeiro toque (Web Audio unlock confirmado)

---

## REFERENCIAS VISUAIS

**Combate e feel de impacto:**
- **Castle Crashers (The Behemoth, 2008)** — O padrao-ouro de hit-stop + knockback em beat-em-up 2D. Cada golpe tem peso fisico. Estudar o timing exato do freeze no hit e o arco de knockback.
- **Streets of Rage 4 (Dotemu, 2020)** — Versao moderna. Hit-flash e damage numbers implementados com precisao cirurgica. Referencia para calibrar a duracao do flash (exatamente 1 frame a 60fps = 16ms).
- **Dead Cells (Motion Twin, 2018)** — Particulas de sangue/tinta em impacto. A direcao das particulas espelha a direcao do golpe. Aprender esse angulo de emissao.

**Arte e estilo visual do nivel:**
- **Metal Slug 3 (SNK, 2000)** — Interior do nivel de base militar como referencia espiritual do Ministerio. Nivel de detalhe nos backgrounds, papeis empilhados, iluminacao fluorescente. O design doc cita diretamente.
- **Cuphead (StudioMDHR, 2017)** — Para as onomatopeias e o estilo de quadrinhos dos textos de dano. NAO para o gameplay — Cuphead e run-and-gun com dificuldade absurda. So a linguagem visual de texto-como-arte.
- **Hades (Supergiant Games, 2020)** — Para o sistema de dialogo contextual. Personagens falam enquanto o jogador controla, sem pausar o jogo. O Burocrata-Zumbi gemendo enquanto anda e diretamente inspirado nessa tecnica.

**Referencia de genero (side-scroller horde survival):**
- **Dead Ahead: Zombie Warfare (Mobirate, 2015)** — A referencia mais proxima do genero. Side-view, inimigos vindo da direita, progressao de waves. Estudar o balanceamento de velocidade de zumbis (eles erram intuitivamente na maioria dos jogos — lentos demais ou rapidos demais). Dead Ahead acerta.
- **Zombie Tsunami (Mobigame, 2012)** — Para entender o que NAO fazer: inimigos sem personalidade. Cada zumbi em Zumbis de Brasilia tem dialogo. Essa diferenca e o produto.

**Audio e musica:**
- **Hotline Miami (Dennaton Games, 2012)** — Para a relacao entre musica e gameplay. A trilha distorcida e sincopada de Hotline Miami cria ansiedade proposital. A MPB distorcida da Q1-01 deve criar leveza comica que contrasta com o caos — funcao oposta, mesma tecnica (musica como estado emocional, nao decoracao).
- **Tropico 6 (Limbic Entertainment, 2019)** — Para inspiracao de como tratar politica de forma satirica sem perder o tom. O humor politico brasileiro e mais agressivo que o caribenho de Tropico, mas a disposicao de ridicularizar instituicoes sem odio puro e a referencia certa.

---

## SUMARIO DE ESTIMATIVAS

| Fase | Descricao | Pomodoros |
|------|-----------|-----------|
| A | Player + input | 3 |
| B | Tilemap + parallax | 4 |
| C | Combate + dummy | 5 |
| D | Burocrata-Zumbi | 4 |
| E | Wave system | 6 |
| F | Carlao | 3 |
| G | HUD | 2 |
| H | Cutscene de abertura | 4 |
| I | Game Over + Vitoria | 4 |
| J | Polish (distribuido) | 6 |
| **Total** | | **41 pomodoros** |

Um pomodoro = 25 minutos de trabalho focado. 41 pomodoros = ~17 horas de desenvolvimento executado sem interrupcao. Na pratica com revisoes, testes em device, ajustes de feel e iteracoes de QA: multiplique por 1.8x. Estimativa realista: **30 horas de desenvolvimento para MVP jogavel**.

O ponto de corte de MVP minimo testavel e ao final da Fase E (wave system completo). Fases F-J adicionam profundidade narrativa e polish, mas o loop central ja e testavel e diagnosticavel com A-E.
