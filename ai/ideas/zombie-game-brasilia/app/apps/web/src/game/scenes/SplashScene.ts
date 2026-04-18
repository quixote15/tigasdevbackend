import Phaser from 'phaser';
import { SCENES, VIEWPORT, DEPTHS, PALETTE } from '../config/GameConstants';

/**
 * SplashScene.ts — Tela de splash com logo do jogo.
 *
 * Sequencia:
 *   fade-in 1500ms  -> logo + subtitulo aparecem
 *   hold   2000ms   -> logo pulsa levemente (scale 1.0 -> 1.02 -> 1.0)
 *   fade-out 800ms  -> camera.fadeOut(800) -> MainMenu
 *
 * Skip: ESPACO, ENTER ou click/toque durante o hold dispara goToMenu()
 * imediatamente.
 *
 * Fallback: se 'menu_logo' nao existir no cache de texturas (assets ainda
 * nao gerados), renderiza o texto "ZUMBIS DE BRASILIA" como placeholder.
 */
export default class SplashScene extends Phaser.Scene {
  private canSkip = false;

  constructor() {
    super({ key: SCENES.SPLASH });
  }

  create(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const cx = W / 2;
    const cy = H / 2;

    // ------------------------------------------------------------------
    // Background: gradiente de ceu apocaliptico
    // Tres camadas de rectangulos empilhados — substituir por bg_sky.png
    // quando o asset existir. Cores: #FF6B35 -> #8B0000 -> #2D0A0A
    // ------------------------------------------------------------------
    this.add.rectangle(cx, H * 0.15, W, H * 0.3, PALETTE.LARANJA_SANGUE).setAlpha(0.8);
    this.add.rectangle(cx, H * 0.45, W, H * 0.4, PALETTE.VERMELHO_QUEIMADO).setAlpha(0.7);
    this.add.rectangle(cx, H * 0.75, W, H * 0.3, 0x2d0a0a).setAlpha(0.9);

    // Gas verde flutuando (placeholder visual)
    this.createToxicParticles();

    // ------------------------------------------------------------------
    // Logo — imagem real ou fallback textual
    // ------------------------------------------------------------------
    let logo: Phaser.GameObjects.Image | Phaser.GameObjects.Text;

    if (this.textures.exists('menu_logo')) {
      logo = this.add.image(cx, cy, 'menu_logo').setOrigin(0.5);
    } else {
      logo = this.add
        .text(cx, cy, 'ZUMBIS DE BRASILIA', {
          fontFamily: 'monospace',
          fontSize: '36px',
          color: '#F0E8D8',
          stroke: '#1A1A18',
          strokeThickness: 3,
        })
        .setOrigin(0.5);
    }

    logo.setAlpha(0).setDepth(DEPTHS.MENU_UI);

    // ------------------------------------------------------------------
    // Subtitulo narrativo
    // ------------------------------------------------------------------
    const sub = this.add
      .text(cx, cy + 30, 'Brasilia, 8 de jan de 2023.\nA nevoa verde subiu.', {
        fontFamily: 'monospace',
        fontSize: '14px',
        color: '#8A8580',
        align: 'center',
      })
      .setOrigin(0.5)
      .setAlpha(0)
      .setDepth(DEPTHS.MENU_UI);

    // ------------------------------------------------------------------
    // Hint de skip — aparece apos o fade-in
    // ------------------------------------------------------------------
    const skipHint = this.add
      .text(cx, H - 10, 'TOQUE PARA PULAR', {
        fontFamily: 'monospace',
        fontSize: '10px',
        color: '#333333',
      })
      .setOrigin(0.5)
      .setAlpha(0)
      .setDepth(DEPTHS.MENU_UI);

    // ------------------------------------------------------------------
    // Sequencia de animacao principal
    // ------------------------------------------------------------------
    this.tweens.add({
      targets: [logo, sub],
      alpha: 1,
      duration: 1500,
      ease: 'Power2',
      onComplete: () => {
        this.canSkip = true;

        // Pulsacao sutil: scale 1.0 -> 1.02 -> 1.0, loop infinito
        this.tweens.add({
          targets: logo,
          scaleX: 1.02,
          scaleY: 1.02,
          duration: 1200,
          yoyo: true,
          repeat: -1,
          ease: 'Sine.easeInOut',
        });

        // Hint de skip aparece 200ms apos o fade-in completar
        this.time.delayedCall(200, () => {
          this.tweens.add({ targets: skipHint, alpha: 0.6, duration: 500 });
        });

        // Vai automaticamente apos 2s de hold
        this.time.delayedCall(2000, () => this.goToMenu());
      },
    });

    // ------------------------------------------------------------------
    // Input para pular a splash
    // ------------------------------------------------------------------
    this.input.once('pointerdown', () => {
      if (this.canSkip) this.goToMenu();
    });
    this.input.keyboard?.once('keydown-SPACE', () => {
      if (this.canSkip) this.goToMenu();
    });
    this.input.keyboard?.once('keydown-ENTER', () => {
      if (this.canSkip) this.goToMenu();
    });
  }

  // --------------------------------------------------------------------
  // Gas toxico flutuando — pontos verdes placeholder
  // Substituir por Phaser.GameObjects.Particles quando ui_atlas existir
  // --------------------------------------------------------------------
  private createToxicParticles(): void {
    for (let i = 0; i < 15; i++) {
      const x = Phaser.Math.Between(0, VIEWPORT.WIDTH);
      const y = Phaser.Math.Between(20, VIEWPORT.HEIGHT - 40);
      const dot = this.add
        .circle(x, y, Phaser.Math.Between(1, 3), PALETTE.GAS_BASE, 0.4)
        .setDepth(DEPTHS.MENU_BG);

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

  // --------------------------------------------------------------------
  // Transicao para o menu — fade to black, entao inicia MainMenu
  // --------------------------------------------------------------------
  private goToMenu(): void {
    if (!this.scene.isActive(SCENES.SPLASH)) return;

    // Cancela tweens de repeat para evitar flickering durante o fade out
    this.tweens.killAll();

    this.cameras.main.fadeOut(
      800,
      0,
      0,
      0,
      (_cam: Phaser.Cameras.Scene2D.Camera, progress: number) => {
        if (progress === 1) {
          this.scene.start(SCENES.MAIN_MENU);
        }
      },
    );
  }
}
