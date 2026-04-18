import Phaser from 'phaser';
import { SCENES, VIEWPORT, DEPTHS, PALETTE } from '../config/GameConstants';
import EventBus, { EVENTS } from '../EventBus';

/**
 * SettingsScene.ts — Tela de opcoes. Implementado no Slice 05.
 *
 * Controles:
 * - Volume geral (0-100, slider)
 * - Volume musica (0-100, slider)
 * - Volume SFX (0-100, slider)
 * - Fullscreen toggle
 *
 * Persistencia: localStorage via storage.ts (implementado no Slice 05).
 */
export default class SettingsScene extends Phaser.Scene {
  constructor() {
    super({ key: SCENES.SETTINGS });
  }

  create(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const cx = W / 2;

    this.add.rectangle(cx, H / 2, W, H, 0x0a0a0a);

    this.add
      .text(cx, 20, 'OPCOES', {
        fontFamily: 'monospace',
        fontSize: '20px',
        color: '#F0C830',
        stroke: '#1A1A18',
        strokeThickness: 2,
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI);

    // TODO Slice 05: implementar sliders de volume e toggle fullscreen

    this.add
      .text(cx, H / 2, 'Em breve: opcoes de audio e video', {
        fontFamily: 'monospace',
        fontSize: '14px',
        color: '#8A8580',
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI);

    // Botao voltar
    const btn = this.add.rectangle(40, H - 15, 60, 14, 0x1a1a18, 0.8);
    btn.setStrokeStyle(1, PALETTE.CONCRETO_NIEMEYER);
    btn.setDepth(DEPTHS.MENU_UI);
    btn.setInteractive({ useHandCursor: true });

    this.add
      .text(40, H - 15, '< VOLTAR', {
        fontFamily: 'monospace',
        fontSize: '12px',
        color: '#8A8580',
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI + 1);

    btn.on('pointerdown', () => {
      this.scene.start(SCENES.MAIN_MENU);
    });

    EventBus.emit(EVENTS.SCENE_READY, SCENES.SETTINGS);
  }

  shutdown(): void {
    // Nenhum listener de EventBus adicionado nesta scene por enquanto
  }
}
