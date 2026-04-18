/**
 * GameConstants.ts — Constantes globais do jogo.
 *
 * Unica fonte de verdade para viewport, fisica, profundidades e pools.
 * Nao use magic numbers nas scenes — sempre referencie aqui.
 */

export const VIEWPORT = {
  WIDTH: 960,
  HEIGHT: 540,
  SCALE: 1,         // 1:1 em 1080p; CSS escala proporcionalmente
  SCALE_MOBILE: 1,
  ASPECT: 16 / 9,
} as const;

export const LEVEL = {
  TILE_SIZE: 16,
  TILES_WIDE: 600,     // 5 segmentos x 120 tiles
  TILES_TALL: 17,
  WIDTH: 9600,         // 600 * 16
  HEIGHT: 272,         // 17 * 16
  GROUND_Y: 190,       // pixel Y do chao no viewport logico
  SEGMENT_WIDTH: 1920, // 120 tiles * 16px
} as const;

export const PHYSICS = {
  GRAVITY: 0,
  PLAYER_SPEED: 120,
  PLAYER_SPEED_GRASS: 102,    // 0.85x em grama
  PLAYER_SPEED_ASPHALT: 120,  // 1.0x no asfalto
  ZOMBIE_BASE_SPEED: 60,
  PROJECTILE_SPEED: 200,
  KNOCKBACK_FORCE: 180,
  KNOCKBACK_DECAY: 0.85,
} as const;

// Depth map — tudo ordenado aqui, nunca hardcoded nas scenes
export const DEPTHS = {
  SKY: -1000,
  TOXIC_CLOUDS: -995,
  CONGRESS: -900,
  CONGRESS_GLOW: -899,
  MINISTRIES_FAR: -800,
  MINISTRIES_NEAR: -600,
  BG_OBJECTS: -400,
  GROUND: 0,
  SUBSURFACE: -1,
  PICKUP: 100,
  ZOMBIE_BACK: 200,
  PLAYER: 300,
  ZOMBIE_FRONT: 400,
  PROJECTILE: 500,
  VFX: 600,
  ONOMATOPOEIA: 700,
  FOREGROUND: 900,
  HUD: 1000,
  // Quest 00: camadas do menu
  MENU_BG: -500,
  MENU_UI: 800,
  MENU_OVERLAY: 1100,
} as const;

export const SCROLL_FACTORS = {
  SKY: 0,
  TOXIC_CLOUDS: 0.05,
  CONGRESS: 0.1,
  MINISTRIES_FAR: 0.25,
  MINISTRIES_NEAR: 0.5,
  BG_OBJECTS: 0.75,
  GROUND: 1.0,
  ENTITIES: 1.0,
  FOREGROUND: 1.3,
} as const;

export const POOL_SIZES = {
  ZOMBIES: 50,
  PROJECTILES: 30,
  PARTICLES: 100,
  ONOMATOPOEIAS: 20,
  PICKUPS: 15,
} as const;

// Paleta de referencia — use em tints, particles, debug
export const PALETTE = {
  LARANJA_SANGUE: 0xFF6B35,
  VERMELHO_QUEIMADO: 0x8B0000,
  NOITE_MORTA: 0x2D0A0A,
  CONCRETO_NIEMEYER: 0x8A8580,
  JANELA_VAZIA: 0x1A1A18,
  GAS_BASE: 0x4A7C59,
  CONGRESSO_SILHUETA: 0x1A1A18,
  CONGRESSO_BRILHO: 0x3D6B3A,
  UI_TEXTO: 0xF0E8D8,
  UI_SCORE: 0xF0C830,
  UI_HP: 0xC83030,
  UI_POWERUP: 0x40B840,
} as const;

// Scene keys — unica fonte de verdade para transicoes
export const SCENES = {
  // Quest 00 (menus)
  BOOT: 'Boot',
  PRELOAD: 'Preload',
  SPLASH: 'Splash',
  MAIN_MENU: 'MainMenu',
  MODE_SELECT: 'ModeSelect',
  SETTINGS: 'Settings',
  // Quest 01 (Capitulo 1)
  PROLOGUE_CUTSCENE: 'PrologueCutscene',
  Q101_INTRO: 'Q101IntroCutscene',
  Q101_GAMEPLAY: 'Q101Gameplay',
  Q101_GAMEOVER: 'Q101GameOver',
  Q101_OUTRO: 'Q101OutroCutscene',
} as const;

export const PALETTE_EXTRA = {
  LARANJA_NIEMEYER: 0xD47820,
} as const;

export type SceneKey = (typeof SCENES)[keyof typeof SCENES];
