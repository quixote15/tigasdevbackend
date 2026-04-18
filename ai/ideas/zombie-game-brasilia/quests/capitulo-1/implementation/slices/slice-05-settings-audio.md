# Slice 05 — Tela de Opcoes (Audio + Fullscreen)

**Objetivo:** Tela de configuracoes com sliders de volume (geral, musica, SFX) e toggle de fullscreen. Configuracoes persistem em localStorage entre sessoes.

---

## Entregaveis

```
apps/web/src/game/scenes/SettingsScene.ts      (MODIFICAR: implementar sliders)
apps/web/src/services/storage.ts               (NOVO: abstrai localStorage)
apps/web/src/game/config/GameConstants.ts      (MODIFICAR: adicionar defaults de settings)
```

---

## Criterio de Pronto

- [ ] Tela tem titulo "OPCOES" no topo
- [ ] 3 sliders funcionais: "VOLUME GERAL", "MUSICA", "SFX" (range 0-100, step 10)
- [ ] Slider de VOLUME GERAL controla `this.sound.volume` do Phaser
- [ ] Slider de MUSICA controla volume especificamente da `menu_music`
- [ ] Slider de SFX controla volume de sons de UI
- [ ] Toggle FULLSCREEN: abre/fecha modo tela cheia
- [ ] Ao mudar qualquer configuracao, ela e salva em localStorage imediatamente
- [ ] Ao entrar na tela, sliders mostram os valores salvos (ou defaults)
- [ ] Botao "RESTAURAR PADROES" reseta tudo para defaults e salva
- [ ] Botao "< VOLTAR" volta para MainMenu (musica nao reinicia)
- [ ] Sem erros no console

---

## Dependencias

- **Slice 03 pronto** (menu principal com musica tocando)
- **Sem assets adicionais** — tela e inteiramente em primitivas (retangulos + texto)

---

## Estimativa

**3 pomodoros:**
1. Implementar `storage.ts` + carregar/salvar settings
2. Implementar sliders (retangulos interativos, arrastar horizontalmente)
3. Toggle fullscreen + restaurar padroes + polish

---

## Spec Detalhada

### storage.ts — Abstração de localStorage

```typescript
// apps/web/src/services/storage.ts

export interface GameSettings {
  volumeMain: number;    // 0.0 - 1.0
  volumeMusic: number;   // 0.0 - 1.0
  volumeSfx: number;     // 0.0 - 1.0
  fullscreen: boolean;
}

const STORAGE_KEY = 'zumbis_settings';

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
      // localStorage bloqueado (modo incognito em alguns browsers) — ignorar silenciosamente
    }
  },

  resetSettings(): GameSettings {
    const defaults = { ...DEFAULTS };
    this.saveSettings(defaults);
    return defaults;
  },
};
```

### Implementar o slider em Phaser (sem biblioteca externa)

Um slider e: trilha (retangulo) + handle (circulo) + texto de valor. Arrastar o handle
muda o valor e dispara o callback.

```typescript
// Retorna o handle para que o caller possa destrui-lo no shutdown
private createSlider(
  x: number, y: number, label: string,
  initialValue: number,   // 0.0 - 1.0
  onChange: (value: number) => void,
): Phaser.GameObjects.Container {
  const container = this.add.container(x, y);
  const trackW = 160;
  const trackH = 4;

  // Label
  const labelText = this.add.text(-trackW / 2, -14, label, {
    fontFamily: 'monospace', fontSize: '7px', color: '#8A8580',
  });

  // Trilha
  const track = this.add.rectangle(0, 0, trackW, trackH, 0x333333);

  // Fill (a parte preenchida da trilha)
  const fill = this.add.rectangle(-trackW / 2, 0, trackW * initialValue, trackH, PALETTE.GAS_BASE);
  fill.setOrigin(0, 0.5);

  // Handle
  const handleX = -trackW / 2 + trackW * initialValue;
  const handle = this.add.circle(handleX, 0, 6, 0xF0E8D8);
  handle.setInteractive({ useHandCursor: true, draggable: true });

  // Valor numerico
  const valueText = this.add.text(trackW / 2 + 8, 0, `${Math.round(initialValue * 100)}%`, {
    fontFamily: 'monospace', fontSize: '6px', color: '#F0E8D8',
  }).setOrigin(0, 0.5);

  container.add([labelText, track, fill, handle, valueText]);

  // Drag logic
  let isDragging = false;
  handle.on('dragstart', () => { isDragging = true; });
  handle.on('drag', (_pointer: Phaser.Input.Pointer, dragX: number) => {
    const clampedX = Phaser.Math.Clamp(dragX, -trackW / 2, trackW / 2);
    const value = (clampedX + trackW / 2) / trackW;

    handle.setX(clampedX);
    fill.setSize(trackW * value, trackH);
    valueText.setText(`${Math.round(value * 100)}%`);
    onChange(value);
  });
  handle.on('dragend', () => { isDragging = false; });

  this.input.setDraggable(handle);

  return container;
}
```

### SettingsScene.create() — wiring completo

```typescript
create(): void {
  const settings = storage.loadSettings();
  const { WIDTH: W, HEIGHT: H } = VIEWPORT;
  const cx = W / 2;

  // Fundo
  this.add.rectangle(cx, H / 2, W, H, 0x0a0a0a);

  // Titulo
  this.add.text(cx, 18, 'OPCOES', { /* estilo */ }).setOrigin(0.5);

  // Sliders
  this.createSlider(cx, 70, 'VOLUME GERAL', settings.volumeMain, (v) => {
    this.sound.volume = v;
    settings.volumeMain = v;
    storage.saveSettings(settings);
  });

  this.createSlider(cx, 110, 'MUSICA', settings.volumeMusic, (v) => {
    const music = this.sound.get('menu_music') as Phaser.Sound.WebAudioSound | null;
    if (music) music.setVolume(v);
    settings.volumeMusic = v;
    storage.saveSettings(settings);
  });

  this.createSlider(cx, 150, 'EFEITOS SONOROS', settings.volumeSfx, (v) => {
    settings.volumeSfx = v;
    storage.saveSettings(settings);
    // Preview: tocar ui_hover ao soltar o slider
    this.time.delayedCall(100, () => this.sound.play('ui_hover', { volume: v }));
  });

  // Toggle fullscreen
  this.createFullscreenToggle(cx, 190, settings.fullscreen, (isFullscreen) => {
    settings.fullscreen = isFullscreen;
    storage.saveSettings(settings);
    if (isFullscreen) {
      this.scale.startFullscreen();
    } else {
      this.scale.stopFullscreen();
    }
  });

  // Restaurar padroes
  this.createButton(cx, H - 35, 'RESTAURAR PADROES', () => {
    const defaults = storage.resetSettings();
    // Reiniciar a scene para refletir os valores
    this.scene.restart();
  });

  // Voltar
  this.createBackButton();
}
```

### Toggle Fullscreen

```typescript
private createFullscreenToggle(
  x: number, y: number, initialState: boolean,
  onChange: (state: boolean) => void,
): void {
  let isOn = initialState;

  const bg = this.add.rectangle(x, y, 140, 16, 0x1a1a18, 0.9);
  bg.setStrokeStyle(1, PALETTE.CONCRETO_NIEMEYER);
  bg.setInteractive({ useHandCursor: true });

  const label = this.add.text(x - 40, y, 'TELA CHEIA:', {
    fontFamily: 'monospace', fontSize: '7px', color: '#8A8580',
  }).setOrigin(0, 0.5);

  const statusText = this.add.text(x + 20, y, isOn ? 'LIGADO' : 'DESLIGADO', {
    fontFamily: 'monospace', fontSize: '7px',
    color: isOn ? '#40B840' : '#C83030',
  }).setOrigin(0, 0.5);

  bg.on('pointerdown', () => {
    isOn = !isOn;
    statusText.setText(isOn ? 'LIGADO' : 'DESLIGADO');
    statusText.setColor(isOn ? '#40B840' : '#C83030');
    onChange(isOn);
  });
}
```

---

## Checklist de Polish

- [ ] Sliders respondem a toque em mobile (pointer events funcionam em dispositivos touch)
- [ ] Ao arrastar o slider de SFX, tocar um preview sonoro ao soltar (nao durante o arraste)
- [ ] Indicador de valor do slider arredonda para multiplos de 10 (visualmente 0, 10, 20, ...)
- [ ] Se `localStorage` nao esta disponivel (modo incognito), mostrar aviso "Configuracoes nao serao salvas"
- [ ] Fullscreen toggle mostra icone de monitor ao lado do texto
- [ ] Esc fecha a tela de opcoes (volta para MainMenu)
- [ ] Mudancas de volume entram em vigor IMEDIATAMENTE enquanto o handle esta sendo arrastado
