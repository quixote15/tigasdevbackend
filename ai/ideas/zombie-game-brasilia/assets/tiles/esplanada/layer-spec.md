# Layer Spec — 6 Layers Phaser 3 | Esplanada dos Ministerios

> Cada layer tem uma funcao especifica. A ordem de depth determina o que aparece na frente do que.
> O Phaser 3 nao usa z-index como CSS — usa setDepth() e ordem de criacao.

---

## Visao Geral das Layers

```
┌─────────────────────────────────────────────────┐
│  LAYER 5: HUD (Camera separada, sem scroll)     │  depth: 1000+
│  Score, HP, Combo, Timer, Joystick virtual       │
├─────────────────────────────────────────────────┤
│  LAYER 4: VFX                                    │  depth: 800-999
│  Explosoes, fumaca, gas verde, flash de dano     │
├─────────────────────────────────────────────────┤
│  LAYER 3: Projectiles                            │  depth: 600-799
│  Press releases, santinhos-arma, ondas sonicas   │
├─────────────────────────────────────────────────┤
│  LAYER 2: Entities (Y-sorted)                    │  depth: entity.y
│  Player, zumbis, NPCs, pickups, landmarks        │
├─────────────────────────────────────────────────┤
│  LAYER 1: Ground (Tilemap)                       │  depth: 0-100
│  Tiles base, transicoes, decoracoes de chao      │
├─────────────────────────────────────────────────┤
│  LAYER 0: Background (Parallax, sem scroll)      │  depth: -1000
│  Ceu gradient, silhueta do Congresso             │
└─────────────────────────────────────────────────┘
```

---

## Layer 0 — Background

### Funcao
Ceu laranja-sangue permanente + silhueta do Congresso Nacional ao fundo. NAO scrolla com o tilemap (ou scrolla muito lento — parallax).

### Conteudo
| Elemento | Tipo | Tamanho | scrollFactor | depth |
|---|---|---|---|---|
| Sky gradient | Graphics (fillGradientStyle) | Tela inteira | 0 | -1000 |
| Congresso silhueta | Sprite estatico | 128x48px | 0.3 | -999 |
| Congresso glow | PointLight | raio 100px | 0.3 | -998 |
| Nuvens (opcional) | Sprite, alpha baixo | 64x16px | 0.1 | -997 |

### Implementacao
```javascript
// GameScene.create()
// Sky — retangulo gradiente fullscreen
this.skyBg = this.add.graphics();
this.skyBg.fillGradientStyle(0x2D0A0A, 0x2D0A0A, 0xFF6B35, 0xFF6B35);
this.skyBg.fillRect(0, 0, this.cameras.main.width, SKY_HEIGHT);
this.skyBg.setScrollFactor(0);
this.skyBg.setDepth(-1000);

// Congresso — silhueta com parallax
this.congress = this.add.image(CONGRESS_X, HORIZON_Y, 'congresso-silhouette');
this.congress.setScrollFactor(0.3);
this.congress.setDepth(-999);

// Glow
this.congressGlow = this.add.pointlight(CONGRESS_X, HORIZON_Y, 0x3D6B3A, 100, 0.3);
this.congressGlow.setScrollFactor(0.3);
this.congressGlow.setDepth(-998);
```

---

## Layer 1 — Ground (Tilemap)

### Funcao
Tiles base da Esplanada. O chao sobre o qual tudo acontece. Usa Tiled Map Editor para layout.

### Sub-layers do Tilemap
O Tiled permite multiplas layers dentro do mesmo mapa. Usar 3 sub-layers:

| Sub-layer | Conteudo | depth |
|---|---|---|
| `ground-base` | Tiles T01-T10 (concreto, grama, agua, asfalto) | 0 |
| `ground-transitions` | Tiles de transicao entre terrenos | 1 |
| `ground-decor` | Decoracoes de chao (D01-D10): lixo, crateras, manchas | 2 |
| `ground-shadows` | Sombras dos ministerios (tiles com alpha) | 3 |

### Implementacao
```javascript
const map = this.make.tilemap({ key: 'esplanada-map' });
const tileset = map.addTilesetImage('esplanada-tileset', 'esplanada-tiles');

// Sub-layers
this.groundBase = map.createLayer('ground-base', tileset, 0, 0);
this.groundBase.setDepth(0);

this.groundTransitions = map.createLayer('ground-transitions', tileset, 0, 0);
this.groundTransitions.setDepth(1);

this.groundDecor = map.createLayer('ground-decor', tileset, 0, 0);
this.groundDecor.setDepth(2);

this.groundShadows = map.createLayer('ground-shadows', tileset, 0, 0);
this.groundShadows.setDepth(3);
this.groundShadows.setAlpha(0.3);

// Collision no ground-base
this.groundBase.setCollisionByProperty({ collision: true });
```

### Dimensoes do Mapa
| Parametro | Valor |
|---|---|
| **Mapa em tiles** | 60 x 40 tiles (960 x 640 px) |
| **Mapa em pixels** | 960 x 640 px |
| **Viewport** | 480 x 320 px (camera segue player) |
| **Escala** | 2x (cada pixel do tile = 2px na tela) |
| **Resolucao efetiva** | 960 x 640 na tela |

---

## Layer 2 — Entities (Y-Sorted)

### Funcao
Todos os personagens, inimigos, pickups e landmarks interagiveis. Y-sorted significa que entidades mais abaixo na tela (maior Y) aparecem na frente de entidades mais acima.

### Conteudo
| Grupo | Tipo Phaser | Pool Size | Notas |
|---|---|---|---|
| `player` | Arcade.Sprite | 1 | Protagonista |
| `zombies` | Arcade.Group | 50 (pool) | Todos os tipos de zumbi |
| `pickups` | Group | 10 (pool) | Power-ups, armas, cura |
| `landmarks` | StaticGroup | ~10 | Ministerios, ambulancia, etc. |
| `npcs` | Group | 3 | Tiozao, Jornalista, Motoboy (futuro) |

### Y-Sort Implementation
```javascript
// GameScene.update() — chamado TODO frame
// O(n) com n <= ~70 entidades = irrelevante para performance
this.entitiesGroup.getChildren().forEach(entity => {
    entity.setDepth(entity.y);
});
```

### Depth Range
- Entities usam depth = entity.y (valor do pixel Y no mapa)
- Com mapa de 640px de altura, entities vao de depth 0 a 640
- Isso fica ENTRE ground (0-100) e projectiles (600+)
- Para garantir: offset entities depth por +100

```javascript
entity.setDepth(100 + entity.y);
```

### Landmarks como Entities
Landmarks grandes (ministerios, helicoptero, ambulancia) sao entities, NAO tiles:
- Permite collision mais precisa (hitbox customizada)
- Permite interacao (cura na ambulancia, cover no helicoptero)
- Y-sort funciona naturalmente (atras = menor Y, frente = maior Y)

---

## Layer 3 — Projectiles

### Funcao
Projeteis disparados por zumbis e pelo player. Separados de entities para facilitar collision checks.

### Conteudo
| Projetil | Sprite | Pool Size | Velocidade | Dano |
|---|---|---|---|---|
| Press release (Assessor) | 8x8, papel branco girando | 20 | 120 px/s | 10 |
| Onda sonica (Candidato) | 32x8, linhas de energia | 5 | 80 px/s | 25 |
| Bengalada (Senador) | 16x16, arco de swing | 3 | N/A (melee area) | 20 |
| Notas de dinheiro (Lobista) | 8x8, verde-dourado | 10 | 100 px/s (ao alvo zumbi) | 0 (buff) |
| Projetil player (armas ranged) | Varia por arma | 10 | 200 px/s | Varia |

### Implementacao
```javascript
// Pool de projeteis — pre-alocado na create()
this.projectiles = this.physics.add.group({
    classType: Projectile,
    maxSize: 30,
    runChildUpdate: true
});
this.projectiles.setDepth(700);
```

### Depth
- Todos os projeteis: depth 600-799
- Projeteis voam ACIMA das entities (parecem no ar)
- Excecao: santinhos do chao (T09) sao tiles, NAO projeteis

---

## Layer 4 — VFX (Visual Effects)

### Funcao
Efeitos visuais transitorios: explosoes, fumaca, flash de dano, gas verde, onomatopeias.

### Conteudo
| Efeito | Tipo | Sprite | Lifetime | Pool |
|---|---|---|---|---|
| **Gas verde ambiente** | ParticleEmitter | 8x8 difuso | 8-15s | 30 |
| **Santinhos voando** | ParticleEmitter | 16x16, 4 frames | 10-20s | 15 |
| **Fragmentos de papel** | ParticleEmitter | 2x3 | 3-6s | 20 |
| **Explosao de morte** | Sprite animation | 32x32, 6 frames | 500ms | 10 (pool) |
| **Flash de dano (player)** | Camera flash | N/A | 100ms | N/A |
| **Tinta-sangue splat** | Sprite | 16x16, 3 variantes | Permanece no chao | 20 |
| **Fumaca de cura** | ParticleEmitter | 8x8 branco | 2s | 5 |
| **Onomatopeia** | BitmapText | "HIT!", "SLAP!" | 500ms (6 frames) | 5 (pool) |
| **Brilho de power-up** | Sprite glow | 16x16 | Loop enquanto ativo | 5 |
| **Aura de imunidade (Senador)** | Sprite semi-transparente | 32x32 | Loop enquanto ativo | 3 |

### Onomatopeias (Estilo HQ)
```
Sprites de texto pre-renderizados:
- "THWACK!" — vassoura acertando
- "SLAP!" — chinelo acertando  
- "BONK!" — urna acertando
- "SPLAT!" — morte de zumbi
- "POW!" — ataque critico
- "FAKE!" — press release acertando player

Estilo: Fonte irregular, bold, com outline grosso
Cores: #FFFFFF texto, #1A1A18 outline, background splash colorido
Tamanho: 32x16px cada
Animacao: Scale up de 0.5 para 1.2, depois fade out (6 frames, 12fps)
```

### Implementacao
```javascript
// VFX container — depth alto
this.vfxLayer = this.add.container(0, 0);
this.vfxLayer.setDepth(800);

// Gas e santinhos sao emitters separados (ver atmosphere-spec.md)
// Onomatopeias sao sprites poolados
this.onomatopoeiaPool = this.add.group({
    classType: Phaser.GameObjects.Sprite,
    maxSize: 5,
    active: false
});
```

---

## Layer 5 — HUD (Camera Separada)

### Funcao
Interface do jogador. NUNCA scrolla. NUNCA e afetada por efeitos de gameplay. Camera separada.

### Layout do HUD
```
┌─────────────────────────────────────────────────┐
│ [HP BAR ██████░░░░]     WAVE 3     [SCORE 12450]│  ← Topo
│                                                  │
│                                                  │
│                                                  │
│                                                  │
│                    GAMEPLAY                       │
│                                                  │
│                                                  │
│                                                  │
│ [COMBO x5]                    [POWER-UP: Urna]   │  ← Base
│              [JOYSTICK]  [ATK]                   │  ← Mobile only
└─────────────────────────────────────────────────┘
```

### Elementos do HUD
| Elemento | Posicao | Tamanho | Cor | Fonte |
|---|---|---|---|---|
| **HP Bar** | Top-left (8, 8) | 80x8px | `#C83030` fill, `#1A1A18` border | N/A |
| **Wave Counter** | Top-center | — | `#D47820` | Bold condensada |
| **Score** | Top-right | — | `#F0C830` | Bold condensada |
| **Combo** | Bottom-left (8, -24) | — | `#F0C830`, scale pulse | Bold condensada |
| **Power-up Icon** | Bottom-right (-48, -24) | 24x24px | Varia | N/A |
| **Timer (wave)** | Below wave counter | — | `#F0E8D8` | Regular |
| **Virtual Joystick** | Bottom-left (mobile) | 64x64px | `#FFFFFF` alpha 30% | N/A |
| **Attack Button** | Bottom-right (mobile) | 48x48px | `#C83030` alpha 50% | N/A |

### Implementacao (Camera Separada)
```javascript
// Criar camera de HUD que ignora o scroll
this.hudCamera = this.cameras.add(0, 0, config.width, config.height);
this.hudCamera.setScroll(0, 0);

// Fazer camera principal ignorar objetos de HUD
this.cameras.main.ignore(this.hudContainer);

// Fazer camera de HUD ignorar objetos de gameplay
this.hudCamera.ignore([
    this.groundBase,
    this.entitiesGroup,
    this.projectiles,
    this.vfxLayer
]);
```

### Estilo Visual do HUD
- **Fonte:** Bold, condensada, com textura de carimbo (custom bitmap font)
- **Bordas:** Irregulares, como se cortadas a mao
- **Background de score/combo:** Retangulo com bordas rasgadas, `#1A1A18` alpha 60%
- **HP bar:** Borda irregular (nao retangulo perfeito), pulsa quando baixa
- **Wave announcement:** Texto grande que entra deslizando, estilo manchete de tabloide
  - Ex: "WAVE 3 — A BANCADA ATACA"
  - Permanece 2s, sai deslizando

---

## Ordem de Criacao no GameScene

```javascript
class GameScene extends Phaser.Scene {
    create() {
        // === LAYER 0: BACKGROUND ===
        this.createSkyBackground();
        this.createCongressSilhouette();
        
        // === LAYER 1: GROUND (TILEMAP) ===
        this.createTilemap();
        
        // === LAYER 2: ENTITIES ===
        this.createLandmarks();    // Ministerios, ambulancia, etc.
        this.createPlayer();
        this.createZombiePool();
        this.createPickupPool();
        
        // === LAYER 3: PROJECTILES ===
        this.createProjectilePool();
        
        // === LAYER 4: VFX ===
        this.createParticleEmitters(); // Gas, santinhos, papel
        this.createOnomatopoeiaPool();
        this.createSplatPool();
        
        // === LAYER 5: HUD ===
        this.createHUD();
        this.createHUDCamera();
        
        // === PHYSICS ===
        this.setupCollisions();
        
        // === CAMERA ===
        this.cameras.main.startFollow(this.player);
        this.cameras.main.setBounds(0, 0, MAP_WIDTH, MAP_HEIGHT);
    }
    
    update(time, delta) {
        // Y-sort entities
        this.entitiesGroup.getChildren().forEach(e => {
            e.setDepth(100 + e.y);
        });
        
        // Update systems
        this.waveSystem.update(time, delta);
        this.combatSystem.update(time, delta);
        this.scoreSystem.update(time, delta);
    }
}
```

---

## Performance Budget por Layer

| Layer | Max GameObjects | Draw Calls | Notas |
|---|---|---|---|
| Background | 3 | 1 | Estatico, nao muda |
| Ground | 2400 tiles (60x40) | 1 (batched tilemap) | Tilemap e 1 draw call |
| Entities | ~70 | 1 (mesmo atlas) | Atlas unico = 1 batch |
| Projectiles | 30 | 1 (mesmo atlas) | Pool fixo |
| VFX | 65 particulas + 20 sprites | 2-3 | Emitters separados |
| HUD | ~15 | 1-2 | Camera separada |
| **TOTAL** | ~2600 | **~7-9 draw calls** | Target: < 10 |
