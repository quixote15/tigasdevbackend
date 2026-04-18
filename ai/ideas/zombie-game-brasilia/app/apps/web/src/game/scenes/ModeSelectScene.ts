import Phaser from 'phaser';
import { SCENES, VIEWPORT, DEPTHS, PALETTE } from '../config/GameConstants';
import EventBus, { EVENTS } from '../EventBus';

/**
 * ModeSelectScene.ts — Esqueleto da tela de selecao de modo.
 *
 * Implementado no Slice 04.
 * Este arquivo e o esqueleto minimo para o projeto compilar.
 *
 * Layout da tela (480x270):
 *
 * +----------------------------------------------+
 * |  ESCOLHA SEU MODO                            |
 * |                                              |
 * |  [RETRATO Ze]    |    [RETRATO Waldeco]      |
 * |                  |                          |
 * |  ZE CIDADAO      |    WALDECO POLITICO       |
 * |  Servidor pub.   |    Vereador reeleito       |
 * |  Sem superpoder  |    Imunidade e propina     |
 * |  [SELECIONAR]    |    [SELECIONAR]           |
 * |                  |                          |
 * |  [VOLTAR]                                    |
 * +----------------------------------------------+
 *
 * Ver Slice 04 para spec completa.
 */

type GameMode = 'cidadao' | 'politico';

export default class ModeSelectScene extends Phaser.Scene {
  private selectedMode: GameMode | null = null;

  constructor() {
    super({ key: SCENES.MODE_SELECT });
  }

  create(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const cx = W / 2;

    // Fundo
    this.add.rectangle(cx, H / 2, W, H, 0x0a0a0a);
    this.add.rectangle(cx, H * 0.2, W, H * 0.4, PALETTE.LARANJA_SANGUE).setAlpha(0.4);

    // Titulo
    this.add
      .text(cx, 22, 'ESCOLHA SEU MODO', {
        fontFamily: 'monospace',
        fontSize: '32px',
        color: '#F0C830',
        stroke: '#1A1A18',
        strokeThickness: 3,
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI);

    this.add
      .text(cx, 40, 'Duas perspectivas. Um apocalipse.', {
        fontFamily: 'monospace',
        fontSize: '20px',
        color: '#8A8580',
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI);

    // Divisor central
    this.add
      .line(0, 0, cx, 45, cx, H - 30, PALETTE.CONCRETO_NIEMEYER, 0.3)
      .setDepth(DEPTHS.MENU_UI);

    // Modo Cidadao (esquerda)
    this.createModeCard(
      W * 0.25,
      H / 2 + 5,
      'cidadao',
      'ZE CIDADAO',
      'Servidor publico federal\nEsplanada, Asa Sul\nSalario: R$ 4.200/mes\n\nHabilidades:\n- Sobrevivencia por teimosia\n- Grito de "Meu Brasil"\n- Arremesso de chinelo',
      '#F0E8D8',
    );

    // Modo Politico (direita)
    this.createModeCard(
      W * 0.75,
      H / 2 + 5,
      'politico',
      'WALDECO POLITICO',
      'Vereador, 3o mandato\nComissao de nada\nSubsidio: R$ 22.800/mes\n\nHabilidades:\n- Imunidade parlamentar\n- Discurso sem sentido\n- Propina como escudo',
      '#D47820',
    );

    // Botao voltar
    this.createBackButton();

    EventBus.emit(EVENTS.SCENE_READY, SCENES.MODE_SELECT);
  }

  private createModeCard(
    x: number,
    y: number,
    mode: GameMode,
    name: string,
    description: string,
    accentColor: string,
  ): void {
    const cardW = 180;
    const cardH = 200;

    // Card background
    const bg = this.add.rectangle(x, y, cardW, cardH, 0x1a1a18, 0.9);
    bg.setStrokeStyle(1, mode === 'cidadao' ? 0x4a7c59 : 0xd47820);
    bg.setDepth(DEPTHS.MENU_UI);

    // Retrato: imagem real se disponivel, senao placeholder colorido
    const portraitKey = mode === 'cidadao' ? 'portrait_cidadao' : 'portrait_politico';
    const portraitY = y - 55;
    if (this.textures.exists(portraitKey)) {
      // Sprites 64x64 usados como retratos — escalados pra 96x96 com nearest via CSS.
      this.add
        .image(x, portraitY, portraitKey)
        .setOrigin(0.5)
        .setScale(1.5)
        .setDepth(DEPTHS.MENU_UI + 1);
    } else {
      // Fallback: retangulo colorido com inicial
      const portrait = this.add.rectangle(x, portraitY, 96, 96, 0x333333);
      portrait.setStrokeStyle(2, mode === 'cidadao' ? 0x4a7c59 : 0xd47820);
      portrait.setDepth(DEPTHS.MENU_UI + 1);

      this.add
        .text(x, portraitY, mode === 'cidadao' ? 'ZE' : 'WAL', {
          fontFamily: 'monospace',
          fontSize: '48px',
          color: accentColor,
        })
        .setOrigin(0.5)
        .setDepth(DEPTHS.MENU_UI + 2);
    }

    // Nome
    this.add
      .text(x, y + 10, name, {
        fontFamily: 'monospace',
        fontSize: '24px',
        color: accentColor,
        align: 'center',
        fontStyle: 'bold',
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI + 1);

    // Descricao
    this.add
      .text(x, y + 28, description, {
        fontFamily: 'monospace',
        fontSize: '16px',
        color: '#B8B5B0',
        align: 'center',
        wordWrap: { width: cardW - 16 },
        lineSpacing: 2,
      })
      .setOrigin(0.5, 0)
      .setDepth(DEPTHS.MENU_UI + 1);

    // Botao selecionar
    const btnY = y + cardH / 2 - 14;
    const btnBg = this.add.rectangle(x, btnY, 130, 22, 0x2a3a2a, 0.9);
    btnBg.setStrokeStyle(2, mode === 'cidadao' ? 0x4a7c59 : 0xd47820);
    btnBg.setDepth(DEPTHS.MENU_UI + 1);
    btnBg.setInteractive({ useHandCursor: true });

    this.add
      .text(x, btnY, 'SELECIONAR', {
        fontFamily: 'monospace',
        fontSize: '20px',
        color: accentColor,
        fontStyle: 'bold',
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI + 2);

    btnBg.on('pointerover', () => {
      btnBg.setFillStyle(mode === 'cidadao' ? 0x4a7c59 : 0xd47820, 0.4);
    });

    btnBg.on('pointerout', () => {
      btnBg.setFillStyle(0x2a3a2a, 0.9);
    });

    btnBg.on('pointerdown', () => {
      this.selectMode(mode);
    });
  }

  private selectMode(mode: GameMode): void {
    this.selectedMode = mode;
    EventBus.emit(EVENTS.MODE_SELECTED, mode);

    // Fade out e vai para prologo
    this.cameras.main.fadeOut(500, 0, 0, 0, (_cam: Phaser.Cameras.Scene2D.Camera, progress: number) => {
      if (progress === 1) {
        this.scene.start(SCENES.PROLOGUE_CUTSCENE, { mode });
      }
    });
  }

  private createBackButton(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const btn = this.add.rectangle(50, H - 18, 90, 22, 0x1a1a18, 0.8);
    btn.setStrokeStyle(1, PALETTE.CONCRETO_NIEMEYER);
    btn.setDepth(DEPTHS.MENU_UI);
    btn.setInteractive({ useHandCursor: true });

    this.add
      .text(50, H - 18, '< VOLTAR', {
        fontFamily: 'monospace',
        fontSize: '20px',
        color: '#B8B5B0',
        fontStyle: 'bold',
      })
      .setOrigin(0.5)
      .setDepth(DEPTHS.MENU_UI + 1);

    btn.on('pointerdown', () => {
      this.scene.start(SCENES.MAIN_MENU);
    });
  }

  shutdown(): void {
    EventBus.removeAllListeners(EVENTS.MODE_SELECTED);
  }
}
