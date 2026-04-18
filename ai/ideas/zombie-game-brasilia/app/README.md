# Zumbis de Brasilia — Jogo

Side-scroller horde survival. Metal Slug + caricatura politica brasileira.
Brasilia, 8 de janeiro de 2023. A nevoa verde subiu. Sobreviva.

## Stack

- Vite 5 + React 18 + TypeScript (strict)
- Phaser 3.88 (canvas de jogo)
- React gerencia menus e HUD. Phaser gerencia o gameplay.
- Comunicacao via EventBus (zero acoplamento direto)

## Como rodar

```bash
# Instala dependencias (uma vez)
npm install

# Desenvolvimento com hot reload
npm run dev
# Abre em: http://localhost:5173

# Typecheck
npm run typecheck

# Build de producao
npm run build
# Saida em: apps/web/dist/

# Preview do build de producao
npm run preview
```

## Estrutura

```
apps/
  web/
    index.html             -- Entry point HTML
    vite.config.ts         -- Vite + manualChunks para Phaser
    tsconfig.json          -- TypeScript strict + noUncheckedIndexedAccess
    public/
      _headers             -- Cache-Control + CORS para Cloudflare Pages
      assets/
        sprites/           -- Spritesheets e atlases
        audio/             -- OGG/MP3
        fonts/             -- Fontes bitmap
    src/
      main.tsx             -- React entry point
      App.tsx              -- Container principal
      index.css            -- Reset global
      components/
        PhaserGame.tsx     -- Wrapper React do canvas Phaser
      game/
        PhaserGame.ts      -- Factory do Phaser.Game (StartGame)
        EventBus.ts        -- Canal React <-> Phaser
        config/
          GameConstants.ts -- VIEWPORT, DEPTHS, PALETTE, SCENES, PHYSICS
        scenes/
          BootScene.ts     -- Carrega ui_atlas, unlock audio iOS
          PreloadScene.ts  -- Barra de progresso, carrega todos os assets
          MainMenuScene.ts -- Menu principal (3 botoes)
          ModeSelectScene.ts -- Selecao Cidadao / Politico
          SettingsScene.ts -- Volume, fullscreen
```

## Decisoes de arquitetura

**Por que separado do repo de docs?**
O repo `ai/ideas/zombie-game-brasilia/` tem historico de decisoes (ADRs, storytelling, arte). Misturar codigo fonte com documentos de design polui o git log e complica PRs. O jogo tem seu proprio ciclo de release.

**Por que React + Phaser e nao so Phaser?**
Menus em Phaser puro sao verbosos e dificeis de iterar. React renderiza botoes, HUD, modais e leaderboard de forma muito mais produtiva. O canvas do Phaser fica isolado dentro de um div — os dois nao brigam.

**Por que 480x270?**
Viewport logico 16:9 minimo que permite pixel art de 48px (personagens) ser visivel em qualquer tela. Em 2x (960x540) os sprites ficam crisp em 1080p. Em 3x (1440x810) ficam maiores em monitores 4K. O Phaser.Scale.FIT trata o resto.

**Por que noUncheckedIndexedAccess: true?**
Catches undefined at compile time para acessos de array e objeto. Previne runtime crashes durante gameplay (ex: pool vazio, config de wave inexistente).

## Quests / Sprints

- Quest 00 (este repo): Boot, PreloadScene, MainMenu, ModeSelect, Settings
- Quest 01 (Q1-01): Hora Extra — gameplay da Esplanada, wave system, Ze vs zumbis

## Deploy

Cloudflare Pages. Ver `ideas/zombie-game-brasilia/deploy/menor-caminho-publicar.md`.

```
Build command: npm run build
Build output:  apps/web/dist
Root dir:      /
```
