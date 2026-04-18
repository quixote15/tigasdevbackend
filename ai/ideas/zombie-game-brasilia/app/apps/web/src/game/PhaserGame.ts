import Phaser from 'phaser';
import BootScene from './scenes/BootScene';
import PreloadScene from './scenes/PreloadScene';
import SplashScene from './scenes/SplashScene';
import MainMenuScene from './scenes/MainMenuScene';
import ModeSelectScene from './scenes/ModeSelectScene';
import SettingsScene from './scenes/SettingsScene';
import { VIEWPORT } from './config/GameConstants';

/**
 * PhaserGame.ts — Factory do Phaser.Game.
 *
 * Unico ponto de criacao do Phaser.Game no projeto.
 * Recebe o container DOM (gerenciado pelo React) e retorna o game.
 *
 * Scenes registradas aqui: Boot, Preload, e as scenes da Quest 00.
 * Scenes de quests posteriores (Q101Gameplay etc.) serao adicionadas
 * via scene.add() no PreloadScene quando os assets estiverem prontos.
 *
 * Decisao de localizacao do projeto:
 * Repo em /Users/ricardo.ribeiro_1/Desktop/my-studies/zumbis-brasilia-game/
 * Separado do repo de docs/ideas para manter o historico de git limpo.
 * O repo de ideas fica como referencia. O codigo do jogo tem seu proprio repo.
 */
export default function StartGame(parent: HTMLElement): Phaser.Game {
  const config: Phaser.Types.Core.GameConfig = {
    type: Phaser.AUTO,

    // Viewport logico: 480x270 (16:9). Phaser escala para o container.
    width: VIEWPORT.WIDTH,
    height: VIEWPORT.HEIGHT,

    parent,

    backgroundColor: '#0a0a0a',

    scale: {
      mode: Phaser.Scale.FIT,
      autoCenter: Phaser.Scale.CENTER_BOTH,
    },

    render: {
      // Sprites pixel art preservados via CSS `image-rendering: pixelated` no canvas.
      // `pixelArt: true` no Phaser quebrava texto vetorial (monospace).
      antialias: false,
      pixelArt: false,
      roundPixels: true,
    },

    physics: {
      default: 'arcade',
      arcade: {
        // Side-scroller sem gravidade (nao e platformer no MVP)
        gravity: { x: 0, y: 0 },
        debug: import.meta.env.DEV,
      },
    },

    // Todas as scenes da Quest 00 registradas aqui.
    // Ordem importa: Boot e Preload vem primeiro, sao auto-iniciadas em sequencia.
    scene: [
      BootScene,
      PreloadScene,
      SplashScene,
      MainMenuScene,
      ModeSelectScene,
      SettingsScene,
    ],

    audio: {
      disableWebAudio: false,
    },
  };

  return new Phaser.Game(config);
}
