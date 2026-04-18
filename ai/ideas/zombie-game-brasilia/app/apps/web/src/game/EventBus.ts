import Phaser from 'phaser';

/**
 * EventBus.ts — Canal de comunicacao React <-> Phaser.
 *
 * Singleton. Qualquer lugar do codigo pode emitir ou ouvir eventos
 * sem criar acoplamento direto entre React e scenes do Phaser.
 *
 * Convencao de nomes de eventos:
 *   - 'scene-ready'        : uma scene foi criada e esta pronta
 *   - 'game-over'          : jogador morreu
 *   - 'score-update'       : novo score a ser exibido no HUD React
 *   - 'hp-update'          : HP atual do player
 *   - 'wave-announce'      : inicio de nova wave (exibe banner React)
 *   - 'pause-game'         : React pede pause
 *   - 'resume-game'        : React pede resume
 *
 * Regras:
 * 1. Scenes do Phaser EMITEM eventos — React OUVE e re-renderiza
 * 2. React EMITE comandos — Scenes OUVEM e executam
 * 3. Nunca passe referencias a objetos Phaser para o React via EventBus
 *    (causa memory leaks e re-renders desnecessarios)
 * 4. Sempre removeListener no cleanup do useEffect para evitar leaks
 */
const EventBus = new Phaser.Events.EventEmitter();

export default EventBus;

// Tipos exportados para type safety nos listeners
export const EVENTS = {
  // Phaser -> React
  SCENE_READY: 'scene-ready',
  GAME_OVER: 'game-over',
  SCORE_UPDATE: 'score-update',
  HP_UPDATE: 'hp-update',
  WAVE_ANNOUNCE: 'wave-announce',

  // React -> Phaser
  PAUSE_GAME: 'pause-game',
  RESUME_GAME: 'resume-game',
  MUTE_AUDIO: 'mute-audio',
  SET_VOLUME: 'set-volume',

  // Navegacao (Menu -> Game)
  START_GAME: 'start-game',
  MODE_SELECTED: 'mode-selected',
  GO_TO_MENU: 'go-to-menu',
} as const;

export type EventName = (typeof EVENTS)[keyof typeof EVENTS];
