# Slice 06 — Transicao para Quest 01

**Objetivo:** Ao confirmar o modo no ModeSelectScene, a transicao flui corretamente para a PrologueCutsceneScene (stub) e, quando a Q1-01 for implementada, para o Q101IntroCutsceneScene. A cadeia de scenes esta correta e o estado do modo (cidadao/politico) persiste atraves das transicoes.

---

## Entregaveis

```
apps/web/src/game/scenes/PrologueCutsceneScene.ts     (NOVO: stub expandivel)
apps/web/src/game/PhaserGame.ts                       (MODIFICAR: registrar PrologueCutscene)
apps/web/src/game/config/GameConstants.ts             (VERIFICAR: SCENES.PROLOGUE_CUTSCENE existe)
apps/web/src/services/storage.ts                      (MODIFICAR: adicionar saveGameMode)
```

---

## Criterio de Pronto

- [ ] Ao clicar CONFIRMAR em ModeSelectScene, ocorre fade para preto (600ms)
- [ ] `PrologueCutsceneScene` inicia com `{ mode: 'cidadao' | 'politico' }` como scene data
- [ ] PrologueCutsceneScene exibe: "Modo: [ZE CIDADAO / WALDECO POLITICO]" + "Prologue em breve" + instrucao ESC para voltar
- [ ] O modo selecionado e salvo em localStorage via `storage.saveGameMode()`
- [ ] Pressionar ESC na PrologueCutscene volta para MainMenu
- [ ] Pressionar ENTER ou ESPACO na PrologueCutscene navega para Q101Gameplay (ou mostra "Q1-01 nao disponivel ainda")
- [ ] Musica do menu e parada (fade out de 500ms) antes de entrar na PrologueCutscene
- [ ] O flow completo funciona: MainMenu -> ModeSelect -> PrologueCutscene -> (back para MainMenu)
- [ ] Sem erros no console em nenhum ponto do flow

---

## Dependencias

- **Slice 04 pronto** (selecao de modo funcionando)
- **Sem assets novos** — esta scene e texto puro

---

## Estimativa

**2 pomodoros:**
1. Implementar PrologueCutsceneScene stub + registrar scenes
2. Garantir que o modo persiste (storage.saveGameMode), testar flow completo

---

## Spec Detalhada

### PrologueCutsceneScene.ts — Stub expandivel

Este arquivo sera expandido pelo time de Q1-01. O stub so precisa garantir
que a passagem de `data` funciona e que o flow de navegacao esta correto.

```typescript
// apps/web/src/game/scenes/PrologueCutsceneScene.ts
import Phaser from 'phaser';
import { SCENES, VIEWPORT, DEPTHS } from '../config/GameConstants';
import { storage } from '../../services/storage';

interface PrologueData {
  mode: 'cidadao' | 'politico';
}

export default class PrologueCutsceneScene extends Phaser.Scene {
  private mode: 'cidadao' | 'politico' = 'cidadao';

  constructor() {
    super({ key: SCENES.PROLOGUE_CUTSCENE });
  }

  init(data: PrologueData): void {
    // init() e chamado antes de create(), ideal para receber scene data
    this.mode = data.mode ?? 'cidadao';
    // Persistir o modo para uso posterior (Q1-01 GameplayScene, HUD, etc.)
    storage.saveGameMode(this.mode);
  }

  create(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const cx = W / 2;
    const cy = H / 2;

    // Fundo preto total (cutscene)
    this.add.rectangle(cx, cy, W, H, 0x000000);

    const modeLabel = this.mode === 'cidadao' ? 'ZE CIDADAO' : 'WALDECO POLITICO';
    const modeColor = this.mode === 'cidadao' ? '#40B840' : '#D47820';

    // Titulo do prologo
    this.add.text(cx, cy - 50, 'BRASILIA, 8 DE JANEIRO DE 2023', {
      fontFamily: 'monospace', fontSize: '8px', color: '#F0E8D8',
    }).setOrigin(0.5).setDepth(DEPTHS.MENU_UI);

    this.add.text(cx, cy - 35, '15h20. A nevoa verde subiu.', {
      fontFamily: 'monospace', fontSize: '6px', color: '#8A8580',
    }).setOrigin(0.5).setDepth(DEPTHS.MENU_UI);

    // Modo selecionado
    this.add.text(cx, cy, `VOCE E: ${modeLabel}`, {
      fontFamily: 'monospace', fontSize: '10px', color: modeColor,
      stroke: '#1A1A18', strokeThickness: 2,
    }).setOrigin(0.5).setDepth(DEPTHS.MENU_UI);

    // Indicador de desenvolvimento
    this.add.text(cx, cy + 30, '[PROLOGO - Q1-01 EM BREVE]', {
      fontFamily: 'monospace', fontSize: '6px', color: '#444444',
    }).setOrigin(0.5).setDepth(DEPTHS.MENU_UI);

    // Instrucoes
    this.add.text(cx, H - 25, 'ENTER / ESPACO — Continuar', {
      fontFamily: 'monospace', fontSize: '6px', color: '#555555',
    }).setOrigin(0.5).setDepth(DEPTHS.MENU_UI);

    this.add.text(cx, H - 14, 'ESC — Voltar ao menu', {
      fontFamily: 'monospace', fontSize: '6px', color: '#555555',
    }).setOrigin(0.5).setDepth(DEPTHS.MENU_UI);

    // Input handlers
    this.input.keyboard?.once('keydown-ESC', () => {
      this.cameras.main.fadeOut(300, 0, 0, 0, (_cam, progress: number) => {
        if (progress === 1) this.scene.start(SCENES.MAIN_MENU);
      });
    });

    this.input.keyboard?.once('keydown-SPACE', () => this.tryStartGameplay());
    this.input.keyboard?.once('keydown-ENTER', () => this.tryStartGameplay());
    this.input.once('pointerdown', () => this.tryStartGameplay());

    // Fade in da cena
    this.cameras.main.fadeIn(500, 0, 0, 0);
  }

  private tryStartGameplay(): void {
    // Verificar se Q101Gameplay scene existe antes de tentar iniciar
    if (this.scene.get(SCENES.Q101_GAMEPLAY)) {
      this.cameras.main.fadeOut(400, 0, 0, 0, (_cam, progress: number) => {
        if (progress === 1) {
          this.scene.start(SCENES.Q101_GAMEPLAY, { mode: this.mode });
        }
      });
    } else {
      // Q1-01 ainda nao implementada
      this.showQ101NotReady();
    }
  }

  private showQ101NotReady(): void {
    const { WIDTH: W, HEIGHT: H } = VIEWPORT;
    const msg = this.add.text(W / 2, H / 2 + 60, 'Q1-01 ainda em desenvolvimento.\nVolte em breve.', {
      fontFamily: 'monospace', fontSize: '7px', color: '#C83030',
      align: 'center',
    }).setOrigin(0.5).setAlpha(0).setDepth(DEPTHS.MENU_OVERLAY);

    this.tweens.add({ targets: msg, alpha: 1, duration: 300 });
    this.time.delayedCall(2500, () => {
      this.tweens.add({ targets: msg, alpha: 0, duration: 300, onComplete: () => msg.destroy() });
    });
  }

  shutdown(): void {
    // Nenhum listener de EventBus nesta scene
  }
}
```

### Adicionar saveGameMode ao storage.ts

```typescript
// Em storage.ts — adicionar ao objeto storage:
saveGameMode(mode: 'cidadao' | 'politico'): void {
  try {
    localStorage.setItem('zumbis_game_mode', mode);
  } catch {
    // ignorar
  }
},

loadGameMode(): 'cidadao' | 'politico' {
  try {
    const saved = localStorage.getItem('zumbis_game_mode');
    return (saved === 'politico') ? 'politico' : 'cidadao';
  } catch {
    return 'cidadao';
  }
},
```

### Parar musica ao entrar na cutscene

Em `ModeSelectScene.confirmSelection()`, antes do fade:

```typescript
// Fade out da musica do menu
const music = this.sound.get('menu_music') as Phaser.Sound.WebAudioSound | null;
if (music?.isPlaying) {
  this.tweens.add({
    targets: music,
    volume: 0,
    duration: 500,
    onComplete: () => music.stop(),
  });
}
```

### Registrar PrologueCutsceneScene em PhaserGame.ts

```typescript
import PrologueCutsceneScene from './scenes/PrologueCutsceneScene';

// No array scene:
scene: [
  BootScene,
  PreloadScene,
  SplashScene,
  MainMenuScene,
  ModeSelectScene,
  SettingsScene,
  PrologueCutsceneScene,  // ADICIONADO
],
```

### Verificar cadeia completa com console

Abrir DevTools > Console. Ao navegar pelo flow completo, confirmar:
- Nenhum "Scene not found" erro
- Cada scene emite `EVENTS.SCENE_READY` quando inicializa
- `localStorage.getItem('zumbis_game_mode')` retorna 'cidadao' ou 'politico' apos confirmar

---

## Notas para Q1-01

Quando a Quest 01 for implementada:

1. `Q101GameplayScene` deve ser importada e registrada no `PhaserGame.ts`
2. `PrologueCutsceneScene.tryStartGameplay()` automaticamente encontra a scene e inicia
3. O `{ mode }` passado como scene data estara disponivel em `Q101GameplayScene.init(data)`
4. O `storage.loadGameMode()` pode ser usado como fallback se a scene data nao estiver disponivel

O stub garante que o contrato da interface (`{ mode: 'cidadao' | 'politico' }`) esteja
documentado e testavel antes da Q1-01 existir.

---

## Checklist de Polish

- [ ] Tela preta com fade-in (nao aparece abruptamente)
- [ ] Modo do jogador exibido na cor correta (verde para cidadao, ambar para politico)
- [ ] Cursor do mouse desaparece (tela cheia) ou vira cursor padrao (modo janela)
- [ ] Tecla ESC funciona em qualquer ponto do flow de Q00 (boa pratica de UX)
- [ ] "Q1-01 em breve" tem um estilo discreto (nao chama mais atencao que o conteudo narrativo)
