import Phaser from 'phaser';
import { SCENES, VIEWPORT } from '../config/GameConstants';
import EventBus, { EVENTS } from '../EventBus';

/**
 * PreloadScene.ts — Carrega todos os assets com barra de progresso.
 *
 * Estrutura:
 * 1. create(): monta a tela de loading (barra, texto, logo placeholder)
 * 2. preload(): dispara o carregamento de todos os assets
 * 3. Listener 'progress': atualiza a barra visualmente
 * 4. Listener 'complete': registra scenes de gameplay e vai para MainMenu
 *
 * Assets carregados aqui:
 * - Spritesheets de personagens (cidadao, politico, zumbis comuns)
 * - Tiles da Esplanada (side-scroller)
 * - UI atlas (botoes, fontes bitmap)
 * - Audio (musica do menu, SFX de UI)
 * - Background layers do menu (parallax)
 *
 * IMPORTANTE: assets de quests especificas (Q1-02, Q1-03...) NAO sao
 * carregados aqui. Cada quest tem seu proprio mini-preload na transicao.
 */
export default class PreloadScene extends Phaser.Scene {
  private loadingBar?: Phaser.GameObjects.Image;
  private loadingBg?: Phaser.GameObjects.Image;
  private loadingText?: Phaser.GameObjects.Text;
  private percentText?: Phaser.GameObjects.Text;

  constructor() {
    super({ key: SCENES.PRELOAD });
  }

  preload(): void {
    this.createLoadingUI();
    this.setupProgressListeners();

    // =========================================================
    // BACKGROUNDS DO MENU (Quest 00)
    // =========================================================
    // bg_sky: FALTANDO — gerar com PixelLab (prompt 02a em quest-00-prompts.md)
    // TODO: this.load.image('menu_bg_sky', '/assets/sprites/menu/bg_sky.png');

    // bg_congress_sideview: silhueta 320x120 perspectiva lateral — EXISTE
    this.load.image('menu_bg_congress', '/assets/sprites/menu/bg_congress_sideview.png');

    // bg_ministries: ministerio distante 80x100 sideview — EXISTE (parcial)
    this.load.image('menu_bg_ministries', '/assets/sprites/menu/bg_ministries.png');

    // menu_logo: FALTANDO — gerar com PixelLab (prompt 01 em quest-00-prompts.md)
    // TODO: this.load.image('menu_logo', '/assets/sprites/menu/logo_zumbis.png');

    // =========================================================
    // RETRATOS DOS MODOS (Quest 00 — tela de selecao)
    // =========================================================
    // Portraits provisorios: sprites top-down 64x64 usados como retratos congelados.
    // Ze Cidadao = lula idle-south frame0 (ironia narrativa: o zumbi imortal como "cidadao comum")
    // Waldeco Politico = flavio-bolsonaro idle-south frame0
    // Substituir por portraits reais 96x96 quando gerados via PixelLab (prompts 04/05)
    this.load.image('portrait_cidadao', '/assets/sprites/personagens/cidadao/portrait_placeholder.png');
    this.load.image('portrait_politico', '/assets/sprites/personagens/politico/portrait_placeholder.png');

    // Paths finais (quando PixelLab gerar):
    // TODO: this.load.image('portrait_cidadao', '/assets/sprites/personagens/ze-cidadao/portrait.png');
    // TODO: this.load.image('portrait_politico', '/assets/sprites/personagens/waldeco-politico/portrait.png');

    // =========================================================
    // UI ATLAS (botoes, icones, cursor)
    // =========================================================
    // this.load.atlas('ui_atlas', '/assets/sprites/ui_atlas.png', '/assets/sprites/ui_atlas.json');

    // =========================================================
    // AUDIO DO MENU
    // =========================================================
    // this.load.audio('menu_music', ['/assets/audio/music/menu_theme.ogg', '/assets/audio/music/menu_theme.mp3']);
    // this.load.audio('ui_click', '/assets/audio/sfx/ui_click.ogg');
    // this.load.audio('ui_hover', '/assets/audio/sfx/ui_hover.ogg');
    // this.load.audio('ui_back', '/assets/audio/sfx/ui_back.ogg');

    // =========================================================
    // ASSETS DE Q1-01 (carregados aqui pois sao a primeira quest)
    // =========================================================
    // this.load.atlas('game_atlas', '/assets/sprites/game_atlas.png', '/assets/sprites/game_atlas.json');
    // this.load.tilemapTiledJSON('esplanada', '/assets/tilemaps/esplanada.json');
    // this.load.image('esplanada_tiles', '/assets/tilemaps/esplanada_tiles.png');
  }

  create(): void {
    // preload() já rodou antes de create() pelo lifecycle do Phaser.
    // A transição para a próxima scene é feita pelo listener 'complete' em setupProgressListeners.
  }

  private createLoadingUI(): void {
    const W = VIEWPORT.WIDTH;
    const H = VIEWPORT.HEIGHT;
    const cx = W / 2;
    const cy = H / 2;

    // Fundo preto
    this.add.rectangle(cx, cy, W, H, 0x0a0a0a);

    // Titulo placeholder (substituir por logo real no slice-02)
    this.add
      .text(cx, cy - 60, 'ZUMBIS DE BRASILIA', {
        fontFamily: 'monospace',
        fontSize: '36px',
        color: '#F0E8D8',
        stroke: '#1A1A18',
        strokeThickness: 2,
      })
      .setOrigin(0.5);

    // Barra de progresso
    const barW = 200;
    const barH = 12;
    const barX = cx - barW / 2;
    const barY = cy + 20;

    // Background da barra
    this.add.rectangle(cx, barY + barH / 2, barW + 4, barH + 4, 0x333333);

    // Fill da barra (começa com width 0)
    const barFill = this.add.rectangle(barX, barY, 0, barH, 0x4a7c59).setOrigin(0, 0);
    this.loadingBar = barFill as unknown as Phaser.GameObjects.Image;

    // Texto de porcentagem
    this.percentText = this.add
      .text(cx, barY + barH + 12, '0%', {
        fontFamily: 'monospace',
        fontSize: '18px',
        color: '#8A8580',
      })
      .setOrigin(0.5, 0);

    // Store barX for use in progress callback
    (this as unknown as Record<string, unknown>)['_barX'] = barX;
    (this as unknown as Record<string, unknown>)['_barW'] = barW;
    (this as unknown as Record<string, unknown>)['_barFill'] = barFill;
  }

  private setupProgressListeners(): void {
    const data = this as unknown as Record<string, unknown>;

    this.load.on('progress', (value: number) => {
      const barFill = data['_barFill'] as Phaser.GameObjects.Rectangle | undefined;
      const barW = (data['_barW'] as number | undefined) ?? 200;

      if (barFill) {
        barFill.setSize(barW * value, 12);
      }
      if (this.percentText) {
        this.percentText.setText(`${Math.round(value * 100)}%`);
      }
    });

    this.load.on('complete', () => {
      this.registerGameScenes();

      // Pequeno delay para o jogador ver 100% antes de ir para a splash
      this.time.delayedCall(300, () => {
        EventBus.emit(EVENTS.SCENE_READY, SCENES.PRELOAD);
        this.scene.start(SCENES.SPLASH);
      });
    });
  }

  private registerGameScenes(): void {
    // Importa e registra as scenes de gameplay aqui, apos o preload.
    // Isso garante que as scenes so existem em memoria quando necessarias.
    //
    // Padrao: this.scene.add(key, SceneClass, false)
    // O 'false' significa "nao inicie automaticamente"

    // TODO: adicionar imports e registros quando as scenes estiverem implementadas
    // import MainMenuScene from './MainMenuScene';
    // import ModeSelectScene from './ModeSelectScene';
    // import SettingsScene from './SettingsScene';
    // this.scene.add(SCENES.MAIN_MENU, MainMenuScene, false);
    // this.scene.add(SCENES.MODE_SELECT, ModeSelectScene, false);
    // this.scene.add(SCENES.SETTINGS, SettingsScene, false);

    // Por enquanto, MainMenu e adicionado diretamente no PhaserGame.ts
    // para que o scene.start() funcione antes deste ponto
  }
}
