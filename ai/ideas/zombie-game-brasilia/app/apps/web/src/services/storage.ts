/**
 * storage.ts — Abstração de localStorage.
 *
 * Centraliza toda leitura/escrita de estado persistente.
 * Captura erros silenciosamente — modo incognito e outros contextos
 * podem bloquear localStorage sem aviso.
 */

export interface GameSettings {
  volumeMain: number;   // 0.0 - 1.0
  volumeMusic: number;  // 0.0 - 1.0
  volumeSfx: number;    // 0.0 - 1.0
  fullscreen: boolean;
}

export type GameMode = 'cidadao' | 'politico';

const STORAGE_KEY = 'zumbis_settings';
const MODE_KEY = 'zumbis_game_mode';

const DEFAULTS: GameSettings = {
  volumeMain: 0.7,
  volumeMusic: 0.7,
  volumeSfx: 0.8,
  fullscreen: false,
};

export const storage = {
  loadSettings(): GameSettings {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return { ...DEFAULTS };
      return { ...DEFAULTS, ...(JSON.parse(raw) as Partial<GameSettings>) };
    } catch {
      return { ...DEFAULTS };
    }
  },

  saveSettings(settings: GameSettings): void {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(settings));
    } catch {
      // localStorage bloqueado (modo incognito em alguns browsers) — ignorar
    }
  },

  resetSettings(): GameSettings {
    const defaults = { ...DEFAULTS };
    this.saveSettings(defaults);
    return defaults;
  },

  saveGameMode(mode: GameMode): void {
    try {
      localStorage.setItem(MODE_KEY, mode);
    } catch {
      // ignorar
    }
  },

  loadGameMode(): GameMode {
    try {
      const saved = localStorage.getItem(MODE_KEY);
      return (saved === 'politico') ? 'politico' : 'cidadao';
    } catch {
      return 'cidadao';
    }
  },

  isLocalStorageAvailable(): boolean {
    try {
      const testKey = '__zumbis_test__';
      localStorage.setItem(testKey, '1');
      localStorage.removeItem(testKey);
      return true;
    } catch {
      return false;
    }
  },
};
