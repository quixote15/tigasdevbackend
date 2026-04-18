import Phaser from 'phaser';
import { SCENES } from '../config/GameConstants';

/**
 * BootScene.ts — Primeira scene. Carrega APENAS o ui_atlas (sprites de UI/loading).
 *
 * Regras:
 * - Nao carrega assets de gameplay aqui (isso e responsabilidade do PreloadScene)
 * - Registra todas as outras scenes no Phaser via this.scene.add()
 *   (lazy loading — scenes nao sao instanciadas ate serem iniciadas)
 * - Faz unlock do AudioContext (necessario para iOS)
 * - Transiciona para PreloadScene assim que o ui_atlas estiver pronto
 *
 * Por que registrar scenes aqui e nao no PhaserGame.ts?
 * Porque scenes de quest (Q101Gameplay etc.) importam entidades pesadas.
 * Se as importassemos no PhaserGame.ts, elas entrariam no bundle inicial.
 * Aqui, o import() dinamico garante que so carregam quando necessario.
 */
export default class BootScene extends Phaser.Scene {
  constructor() {
    super({ key: SCENES.BOOT });
  }

  preload(): void {
    // Unico asset carregado aqui: atlas de UI (botoes, fonte bitmap, loading bar)
    // Quando nao existe ainda, usamos um retangulo de cor como placeholder
    // REMOVER este bloco quando ui_atlas.png existir:
    this.createPlaceholderGraphics();
  }

  create(): void {
    // Unlock do AudioContext — iOS exige gesto do usuario. A BootScene
    // e a primeira scene, entao registramos o unlock aqui.
    // Phaser 3.88 faz isso automaticamente com game.sound.unlock(),
    // mas registrar explicitamente garante compatibilidade.
    if (this.sound && 'unlock' in this.sound) {
      (this.sound as Phaser.Sound.WebAudioSoundManager).unlock();
    }

    // Registra scenes dinamicamente (lazy — nao instanciadas ainda)
    this.registerScenes();

    // Vai para PreloadScene
    this.scene.start(SCENES.PRELOAD);
  }

  private createPlaceholderGraphics(): void {
    // Placeholder para desenvolvimento: cria texturas simples em runtime
    // Remove este metodo quando os assets reais existirem

    // Textura de loading bar background
    const bgGfx = this.make.graphics({ x: 0, y: 0 });
    bgGfx.fillStyle(0x333333);
    bgGfx.fillRect(0, 0, 400, 20);
    bgGfx.generateTexture('loading_bar_bg', 400, 20);
    bgGfx.destroy();

    // Textura de loading bar fill
    const fillGfx = this.make.graphics({ x: 0, y: 0 });
    fillGfx.fillStyle(0x4a7c59);
    fillGfx.fillRect(0, 0, 400, 20);
    fillGfx.generateTexture('loading_bar_fill', 400, 20);
    fillGfx.destroy();
  }

  private registerScenes(): void {
    // Importamos as scenes aqui para que nao entrem no bundle inicial do Phaser.
    // Nota: dynamic import() em Phaser scenes requer que a scene seja
    // adicionada via scene.add() antes de scene.start().
    // Por simplicidade no MVP, importamos estaticamente mas as scenes
    // so sao INICIADAS quando necessario (scene.start()).
    //
    // TODO Quest 02+: migrar para import() dinamico para reduzir bundle inicial.

    // As scenes serao importadas e adicionadas pelo PreloadScene apos o carregamento.
    // Ver PreloadScene.registerGameScenes() para a lista completa.
  }
}
