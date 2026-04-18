# Slice 02 — Splash Screen

**Objetivo:** Exibir uma splash screen com o logo do jogo antes do menu principal. Logo faz fade-in (1.5s), fica 2s, fade-out (0.8s), transiciona para o MainMenu.

---

## Entregaveis

```
apps/web/
  src/game/scenes/SplashScene.ts       (NOVO)
  src/game/PhaserGame.ts               (MODIFICAR: adicionar SplashScene)
  src/game/scenes/PreloadScene.ts      (MODIFICAR: ir para SplashScene apos preload)
  public/assets/sprites/menu/
    logo_zumbis.png                    (ASSET — ver quest-00-prompts.md, Prompt 01)
    bg_sky.png                         (ASSET — placeholder se nao existir)
```

---

## Criterio de Pronto

- [ ] Apos o PreloadScene terminar, aparece a SplashScene (nao o MainMenu diretamente)
- [ ] Logo "Zumbis de Brasilia" aparece com fade-in de 1500ms (alpha 0 -> 1)
- [ ] Logo fica visivel por 2000ms com leve pulsacao (escala 1.0 -> 1.02 -> 1.0)
- [ ] Logo faz fade-out de 800ms
- [ ] Apos o fade-out, MainMenuScene inicia automaticamente (sem input do usuario)
- [ ] Background da splash: ceu apocaliptico (gradiente `#FF6B35 -> #8B0000 -> #2D0A0A`)
- [ ] Pressionar ESPACO ou clicar/tocar durante a splash pula para o menu imediatamente
- [ ] Sem erros no console

---

## Dependencias

- **Slice 01 pronto** (projeto roda)
- **Asset:** `logo_zumbis.png` — se nao existir, usar texto "ZUMBIS DE BRASILIA" como fallback (ja implementado como placeholder no MainMenuScene)

---

## Estimativa

**2 pomodoros:**
1. Implementar SplashScene com fade in/out e animacao de pulsacao
2. Conectar na cadeia de scenes (PreloadScene -> SplashScene -> MainMenu)

---

## Spec Detalhada

### SplashScene.ts — Implementacao completa

```typescript
// src/game/scenes/SplashScene.ts
import Phaser from 'phaser';
import { SCENES, VIEWPORT, DEPTHS, PALETTE } from '../config/GameConstants';

export default class SplashScene extends Phaser.Scene {
  private canSkip = false;

  constructor() {
    super({ key: SCENES.SPLASH });
  }

  create(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const cx = W / 2;
    const cy = H / 2;

    // Fundo: gradiente de ceu (retangulos empilhados como placeholder)
    // Substituir pelos layers parallax quando bg_sky.png existir
    this.add.rectangle(cx, H * 0.15, W, H * 0.3, PALETTE.LARANJA_SANGUE).setAlpha(0.8);
    this.add.rectangle(cx, H * 0.45, W, H * 0.4, PALETTE.VERMELHO_QUEIMADO).setAlpha(0.7);
    this.add.rectangle(cx, H * 0.75, W, H * 0.3, 0x2d0a0a).setAlpha(0.9);

    // Partículas de gas placeholder (pontos verdes flutuando)
    this.createToxicParticles();

    // Logo
    let logo: Phaser.GameObjects.Image | Phaser.GameObjects.Text;

    if (this.textures.exists('menu_logo')) {
      logo = this.add.image(cx, cy, 'menu_logo');
      logo.setOrigin(0.5);
    } else {
      // Fallback textual
      logo = this.add
        .text(cx, cy, 'ZUMBIS DE BRASILIA', {
          fontFamily: 'monospace',
          fontSize: '18px',
          color: '#F0E8D8',
          stroke: '#1A1A18',
          strokeThickness: 3,
        })
        .setOrigin(0.5);
    }

    logo.setAlpha(0).setDepth(DEPTHS.MENU_UI);

    // Subtitulo
    const sub = this.add
      .text(cx, cy + 30, 'Brasilia, 8 de jan de 2023.\nA nevoa verde subiu.', {
        fontFamily: 'monospace',
        fontSize: '7px',
        color: '#8A8580',
        align: 'center',
      })
      .setOrigin(0.5)
      .setAlpha(0)
      .setDepth(DEPTHS.MENU_UI);

    // Hint de skip
    const skipHint = this.add
      .text(cx, H - 10, 'TOQUE PARA PULAR', {
        fontFamily: 'monospace',
        fontSize: '5px',
        color: '#333333',
      })
      .setOrigin(0.5)
      .setAlpha(0)
      .setDepth(DEPTHS.MENU_UI);

    // Sequencia de animacao
    this.tweens.add({
      targets: [logo, sub],
      alpha: 1,
      duration: 1500,
      ease: 'Power2',
      onComplete: () => {
        this.canSkip = true;

        // Pulsacao sutil do logo
        this.tweens.add({
          targets: logo,
          scaleX: 1.02,
          scaleY: 1.02,
          duration: 1200,
          yoyo: true,
          repeat: -1,
          ease: 'Sine.easeInOut',
        });

        // Mostrar hint de skip
        this.tweens.add({ targets: skipHint, alpha: 0.6, duration: 500 });

        // Timer para ir automaticamente apos 2s
        this.time.delayedCall(2000, () => this.goToMenu());
      },
    });

    // Input para skip
    this.input.once('pointerdown', () => { if (this.canSkip) this.goToMenu(); });
    this.input.keyboard?.once('keydown-SPACE', () => { if (this.canSkip) this.goToMenu(); });
    this.input.keyboard?.once('keydown-ENTER', () => { if (this.canSkip) this.goToMenu(); });
  }

  private createToxicParticles(): void {
    // Pontos verdes flutuando — placeholder visual
    // Substituir por Phaser.GameObjects.Particles quando ui_atlas existir
    for (let i = 0; i < 15; i++) {
      const x = Phaser.Math.Between(0, VIEWPORT.WIDTH);
      const y = Phaser.Math.Between(20, VIEWPORT.HEIGHT - 40);
      const dot = this.add.circle(x, y, Phaser.Math.Between(1, 3), PALETTE.GAS_BASE, 0.4);
      dot.setDepth(DEPTHS.MENU_BG);

      this.tweens.add({
        targets: dot,
        y: y - Phaser.Math.Between(20, 50),
        alpha: 0,
        duration: Phaser.Math.Between(2000, 5000),
        delay: Phaser.Math.Between(0, 3000),
        repeat: -1,
        yoyo: false,
        onRepeat: () => {
          dot.setAlpha(0.4);
          dot.setY(y + Phaser.Math.Between(-10, 10));
        },
      });
    }
  }

  private goToMenu(): void {
    // Cancela tweens de repeat para evitar flickering no fade out
    this.tweens.killAll();

    this.cameras.main.fadeOut(800, 0, 0, 0, (_cam: Phaser.Cameras.Scene2D.Camera, progress: number) => {
      if (progress === 1) {
        this.scene.start(SCENES.MAIN_MENU);
      }
    });
  }
}
```

### Adicionar SPLASH ao SCENES e ao PhaserGame.ts

Em `GameConstants.ts`, adicionar na lista SCENES:
```typescript
SPLASH: 'Splash',
```

Em `PhaserGame.ts`, importar e adicionar SplashScene ao array:
```typescript
import SplashScene from './scenes/SplashScene';
// ...
scene: [BootScene, PreloadScene, SplashScene, MainMenuScene, ModeSelectScene, SettingsScene],
```

Em `PreloadScene.ts`, alterar a transicao final:
```typescript
// DE:
this.scene.start(SCENES.MAIN_MENU);
// PARA:
this.scene.start(SCENES.SPLASH);
```

---

## Checklist de Polish

- [ ] Gas verde flutuando no background (mesmo sem assets reais — use circulos)
- [ ] Subtitulo "Brasilia, 8 de jan de 2023. A nevoa verde subiu." aparece com o logo
- [ ] Skip hint aparece 200ms apos o fade-in completar (nao simultaneo)
- [ ] Transicao para menu e fade to black (nao corte abrupto)
- [ ] Em mobile: toque em qualquer parte da tela pula a splash
- [ ] Som: silencio durante a splash OU musica do menu ja comecando suavemente
