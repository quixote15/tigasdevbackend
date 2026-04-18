# Slice 04 — Selecao de Modo

**Objetivo:** Tela de selecao entre "Ze Cidadao" e "Waldeco Politico" com retratos, descricao de gameplay e botao de confirmar. Ao confirmar, emite evento com o modo escolhido e transiciona para o prologo.

---

## Entregaveis

```
apps/web/src/game/scenes/ModeSelectScene.ts    (MODIFICAR: substituir placeholder)
public/assets/sprites/personagens/
  ze-cidadao/portrait.png             (ASSET — Prompt 04 de quest-00-prompts.md)
  waldeco-politico/portrait.png       (ASSET — Prompt 05)
public/assets/audio/sfx/
  mode_cidadao.ogg                    (ASSET — SFX brief 08)
  mode_politico.ogg                   (ASSET — SFX brief 08)
  ui_select_mode.ogg                  (ASSET — SFX brief 08)
```

---

## Criterio de Pronto

- [ ] Tela exibe dois cards lado a lado: Ze Cidadao (esquerda) e Waldeco Politico (direita)
- [ ] Cada card tem: retrato (96x96 sprite ou placeholder), nome, descricao de 3 linhas, botao "SELECIONAR"
- [ ] Hover no card: borda destaca, card levemente eleva (scale 1.02)
- [ ] Click em "SELECIONAR": toca `ui_select_mode.ogg`, fade-in de highlight no card escolhido
- [ ] Apos selecionar, botao "CONFIRMAR MODO" aparece no centro inferior (2s de delay)
- [ ] Click em CONFIRMAR: emite `EventBus.emit(EVENTS.MODE_SELECTED, modo)`, toca sfx especifico do modo, fade para black, inicia PrologueCutsceneScene com `{ mode }` como data
- [ ] Botao "< VOLTAR" funciona (volta para MainMenu)
- [ ] Musica do menu CONTINUA tocando (nao reinicia)
- [ ] Sem erros no console

---

## Dependencias

- **Slice 03 pronto** (menu principal funcionando)
- **Assets:** retratos `portrait.png` — se nao existirem, usar retangulos coloridos com inicial do personagem (ja no placeholder atual)
- **EventBus:** `MODE_SELECTED` evento definido em `EventBus.ts` (ja existe)

---

## Estimativa

**3 pomodoros:**
1. Layout dos dois cards com retratos e descricoes
2. Logica de selecao (highlight, botao confirmar aparece)
3. Transicao com evento e fade

---

## Spec Detalhada

### Estado da tela

A tela tem dois estados:
- **Estado inicial:** ambos os cards com mesma prominence, sem botao confirmar
- **Estado apos selecao:** card escolhido em destaque, card rejeitado em cinza (alpha 0.5), botao CONFIRMAR aparece

```typescript
type ModeSelectState = 'choosing' | 'selected';
type GameMode = 'cidadao' | 'politico';

private state: ModeSelectState = 'choosing';
private selectedMode: GameMode | null = null;
```

### Transicao de estado ao clicar SELECIONAR

```typescript
private onModeSelected(mode: GameMode): void {
  if (this.state === 'selected') return; // evita double-click
  this.state = 'selected';
  this.selectedMode = mode;

  // Destacar card selecionado
  const selected = mode === 'cidadao' ? this.cidadaoCard : this.politicoCard;
  const rejected = mode === 'cidadao' ? this.politicoCard : this.cidadaoCard;

  this.tweens.add({ targets: selected, scaleX: 1.04, scaleY: 1.04, duration: 200 });
  this.tweens.add({ targets: rejected, alpha: 0.4, duration: 300 });

  // Som
  if (this.sound.get('ui_select_mode')) {
    this.sound.play('ui_select_mode', { volume: 0.8 });
  }

  // Mostrar botao confirmar apos delay
  this.time.delayedCall(400, () => this.showConfirmButton());
}
```

### Botao CONFIRMAR

O botao CONFIRMAR aparece centrado abaixo dos cards (Y = altura * 0.88).
Ele nao existe no create() — e adicionado dinamicamente via `showConfirmButton()`.

```typescript
private showConfirmButton(): void {
  const { WIDTH: W, HEIGHT: H } = VIEWPORT;
  const cx = W / 2;
  const btnY = H * 0.88;

  const btn = this.add.rectangle(cx, btnY, 140, 16, 0x1a1a18, 0.9);
  btn.setStrokeStyle(2, this.selectedMode === 'cidadao' ? PALETTE.GAS_BASE : PALETTE.LARANJA_NIEMEYER);
  btn.setAlpha(0).setDepth(DEPTHS.MENU_UI);
  btn.setInteractive({ useHandCursor: true });

  const label = `CONFIRMAR: ${this.selectedMode === 'cidadao' ? 'ZE CIDADAO' : 'WALDECO POLITICO'}`;
  const text = this.add.text(cx, btnY, label, {
    fontFamily: 'monospace',
    fontSize: '7px',
    color: this.selectedMode === 'cidadao' ? '#40B840' : '#D47820',
  }).setOrigin(0.5).setAlpha(0).setDepth(DEPTHS.MENU_UI + 1);

  this.tweens.add({ targets: [btn, text], alpha: 1, duration: 400 });

  btn.on('pointerdown', () => this.confirmSelection());
}
```

### confirmSelection(): fade e transicao

```typescript
private confirmSelection(): void {
  if (!this.selectedMode) return;

  // SFX especifico do modo
  const sfxKey = this.selectedMode === 'cidadao' ? 'mode_cidadao' : 'mode_politico';
  if (this.sound.get(sfxKey)) {
    this.sound.play(sfxKey, { volume: 0.9 });
  }

  // Emitir evento para React (HUD pode precisar saber o modo)
  EventBus.emit(EVENTS.MODE_SELECTED, this.selectedMode);

  // Fade para proximo
  this.cameras.main.fadeOut(600, 0, 0, 0, (_cam, progress: number) => {
    if (progress === 1) {
      // Passa o modo como data para a proxima scene
      this.scene.start(SCENES.PROLOGUE_CUTSCENE, { mode: this.selectedMode });
    }
  });
}
```

### Descricoes dos modos (texto nos cards)

**Ze Cidadao:**
```
Servidor publico federal
Ministerio do Planejamento
Salario: R$ 4.200/mes

Estilo: Sobrevivencia por teimosia
Arma inicial: Chinelo Havaianas
Vantagem: Conhece todos os atalhos
Desvantagem: Sem imunidade parlamentar
```

**Waldeco Politico:**
```
Vereador - 3o mandato
Comissao de nada
Subsidio: R$ 22.800/mes

Estilo: Propina como escudo
Arma inicial: Santinho eleitor
Vantagem: Imunidade parlamentar (-)
Desvantagem: Zumbis o reconhecem
```

### Adicionar PROLOGUE_CUTSCENE ao SCENES (GameConstants.ts)

Se ainda nao existir, adicionar o placeholder de scene:

```typescript
SPLASH: 'Splash',
PROLOGUE_CUTSCENE: 'PrologueCutscene',  // implementado em Q1-01
```

E adicionar uma scene stub em `PhaserGame.ts` para evitar crash ao tentar iniciar:

```typescript
// Stub temporario enquanto PrologueCutsceneScene nao existe
class PrologueCutsceneStub extends Phaser.Scene {
  constructor() { super({ key: SCENES.PROLOGUE_CUTSCENE }); }
  create(): void {
    const d = this.scene.settings.data as { mode: string };
    this.add.text(240, 135, `Modo: ${d.mode}\nQ1-01 em breve`, {
      fontFamily: 'monospace', fontSize: '10px', color: '#F0E8D8', align: 'center',
    }).setOrigin(0.5);
    // ESC volta para menu
    this.input.keyboard?.once('keydown-ESC', () => this.scene.start(SCENES.MAIN_MENU));
  }
}
```

---

## Checklist de Polish

- [ ] Card hover tem som de `ui_hover.ogg` (1x por hover, nao repetir)
- [ ] Retrato do personagem tem leve animacao de idle (2 frames: respirar) quando o card esta em destaque
- [ ] Descricao do modo tem rollout text (letra por letra) quando o card e focado
- [ ] Seta de indicacao (>) pisca ao lado do botao CONFIRMAR
- [ ] Em mobile: swipe horizontal entre os dois cards (opcional para MVP)
- [ ] Background continua com parallax lento (igual ao MainMenu)
