import Phaser from 'phaser';
import { SCENES, VIEWPORT, DEPTHS, PALETTE } from '../config/GameConstants';
import EventBus, { EVENTS } from '../EventBus';

/**
 * MainMenuScene.ts — Esqueleto da tela principal do menu.
 *
 * Implementado no Slice 03.
 * Este arquivo e o esqueleto minimo para o projeto compilar.
 *
 * Estrutura visual (quando assets existirem):
 * - Layer 0: Sky gradient (#FF6B35 -> #8B0000 -> #2D0A0A)
 * - Layer 1: Congresso Nacional silhueta (parallax 0.1)
 * - Layer 2: Ministerios distantes (parallax 0.25)
 * - Layer 3: Logo "Zumbis de Brasilia" (centrado, topo)
 * - Layer 4: 3 botoes: JOGAR | OPCOES | SAIR
 * - Layer 5: Particulas de gas verde flutuando
 *
 * Ver Slice 03 para spec completa.
 */
export default class MainMenuScene extends Phaser.Scene {
  private menuMusic?: Phaser.Sound.BaseSound;

  constructor() {
    super({ key: SCENES.MAIN_MENU });
  }

  create(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const cx = W / 2;
    const cy = H / 2;

    // Fundo: ceu apocaliptico (gradiente placeholder — substituir por bg_sky.png quando gerado)
    this.add.rectangle(cx, cy, W, H, 0x0a0a0a);
    this.add.rectangle(cx, H * 0.15, W, H * 0.3, PALETTE.LARANJA_SANGUE).setAlpha(0.6);
    this.add.rectangle(cx, H * 0.4, W, H * 0.3, PALETTE.VERMELHO_QUEIMADO).setAlpha(0.5);

    // Layer: Congresso Nacional sideview (320x120, ancoragem na base)
    // Escala proporcional para preencher a largura do viewport (480/320 = 1.5)
    if (this.textures.exists('menu_bg_congress')) {
      this.add
        .image(cx, H - 30, 'menu_bg_congress')
        .setOrigin(0.5, 1)
        .setScale(1.5)
        .setDepth(DEPTHS.MENU_BG + 1)
        .setAlpha(0.9);
    }

    // Layer: Ministerios distantes (parallax leve via scrollFactor — implementar no Slice 03)
    if (this.textures.exists('menu_bg_ministries')) {
      // Espelha o ministerio para criar ilusao de dois lados da esplanada
      const mLeft = this.add
        .image(40, H - 40, 'menu_bg_ministries')
        .setOrigin(0.5, 1)
        .setDepth(DEPTHS.MENU_BG)
        .setAlpha(0.7);
      const mRight = this.add
        .image(W - 40, H - 40, 'menu_bg_ministries')
        .setOrigin(0.5, 1)
        .setFlipX(true)
        .setDepth(DEPTHS.MENU_BG)
        .setAlpha(0.7);
      void mLeft;
      void mRight;
    }

    // Titulo placeholder (substituir por logo sprite no Slice 02/03)
    this.add
      .text(cx, cy - 70, 'ZUMBIS DE BRASILIA', {
        fontFamily: 'monospace',
        fontSize: '28px',
        color: '#F0E8D8',
        stroke: '#1A1A18',
        strokeThickness: 3,
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI);

    this.add
      .text(cx, cy - 52, 'Brasilia, 8 de jan de 2023. A nevoa subiu.', {
        fontFamily: 'monospace',
        fontSize: '12px',
        color: '#8A8580',
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI);

    // Botoes do menu principal
    this.createMenuButton(cx, cy - 10, 'JOGAR', () => {
      this.scene.start(SCENES.MODE_SELECT);
    });

    this.createMenuButton(cx, cy + 14, 'OPCOES', () => {
      this.scene.start(SCENES.SETTINGS);
    });

    this.createMenuButton(cx, cy + 38, 'SAIR', () => {
      // Em web nao tem "sair" real — mostra uma mensagem ou vai para uma tela de creditos
      this.showExitMessage();
    });

    // Versao no canto inferior
    this.add
      .text(4, H - 6, 'v0.1.0 - Quest 00', {
        fontFamily: 'monospace',
        fontSize: '20px',
        color: '#333333',
      })
      .setOrigin(0, 1)
      .setDepth(DEPTHS.MENU_UI);

    EventBus.emit(EVENTS.SCENE_READY, SCENES.MAIN_MENU);
  }

  private createMenuButton(
    x: number,
    y: number,
    label: string,
    onClick: () => void,
  ): Phaser.GameObjects.Container {
    const container = this.add.container(x, y);
    container.setDepth(DEPTHS.MENU_UI);

    const bg = this.add.rectangle(0, 0, 100, 14, 0x1a1a18, 0.8);
    bg.setStrokeStyle(1, PALETTE.CONCRETO_NIEMEYER);

    const text = this.add
      .text(0, 0, label, {
        fontFamily: 'monospace',
        fontSize: '16px',
        color: '#F0E8D8',
      })
      .setOrigin(0.5);

    container.add([bg, text]);

    // Interatividade
    bg.setInteractive({ useHandCursor: true });

    bg.on('pointerover', () => {
      bg.setFillStyle(PALETTE.GAS_BASE, 0.6);
      text.setColor('#F0C830');
    });

    bg.on('pointerout', () => {
      bg.setFillStyle(0x1a1a18, 0.8);
      text.setColor('#F0E8D8');
    });

    bg.on('pointerdown', () => {
      this.tweens.add({
        targets: container,
        scaleX: 0.95,
        scaleY: 0.95,
        duration: 80,
        yoyo: true,
        onComplete: onClick,
      });
    });

    return container;
  }

  private showExitMessage(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const overlay = this.add.rectangle(W / 2, H / 2, W, H, 0x000000, 0.7);
    overlay.setDepth(DEPTHS.MENU_OVERLAY);
    overlay.setInteractive();

    const msg = this.add
      .text(W / 2, H / 2, 'Aqui nao tem saida.\nIsso e Brasilia.', {
        fontFamily: 'monospace',
        fontSize: '20px',
        color: '#F0E8D8',
        align: 'center',
        stroke: '#1A1A18',
        strokeThickness: 2,
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_OVERLAY + 1);

    overlay.once('pointerdown', () => {
      overlay.destroy();
      msg.destroy();
    });
  }

  shutdown(): void {
    // Limpar listeners do EventBus registrados nesta scene
    EventBus.removeAllListeners(EVENTS.PAUSE_GAME);
    EventBus.removeAllListeners(EVENTS.RESUME_GAME);

    if (this.menuMusic) {
      this.menuMusic.stop();
    }
  }
}
