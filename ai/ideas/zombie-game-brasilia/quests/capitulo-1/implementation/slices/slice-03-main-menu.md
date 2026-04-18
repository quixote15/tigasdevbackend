# Slice 03 — Menu Principal

**Objetivo:** Menu principal completo com background parallax da Esplanada, logo animado, 3 botoes funcionais (JOGAR / OPCOES / SAIR), e musica de menu tocando em loop.

---

## Entregaveis

```
apps/web/src/game/scenes/MainMenuScene.ts    (MODIFICAR: substituir placeholder)
public/assets/sprites/menu/
  logo_zumbis.png          (ASSET — Prompt 01 de quest-00-prompts.md)
  bg_sky.png               (ASSET — Prompt 02a)
  bg_congress.png          (ASSET — Prompt 02b)
  bg_ministries.png        (ASSET — Prompt 03)
public/assets/audio/music/
  menu_theme.ogg           (ASSET — Brief 08 de quest-00-prompts.md)
  menu_theme.mp3           (ASSET — fallback)
public/assets/audio/sfx/
  ui_hover.ogg             (ASSET — SFX brief 08)
  ui_click.ogg             (ASSET — SFX brief 08)
```

---

## Criterio de Pronto

- [ ] Background tem 3 camadas parallax visiveis (ceu, Congresso, ministerios)
- [ ] Logo "Zumbis de Brasilia" aparece no topo com leve flutuacao (tween seno)
- [ ] 3 botoes: JOGAR, OPCOES, SAIR — visiveis, clicaveis e funcionais
- [ ] JOGAR navega para ModeSelectScene
- [ ] OPCOES navega para SettingsScene
- [ ] SAIR mostra mensagem "Aqui nao tem saida. Isso e Brasilia."
- [ ] Musica do menu toca em loop (volume 0.7)
- [ ] Hover em botao: som `ui_hover.ogg` + mudanca visual
- [ ] Click em botao: som `ui_click.ogg` + animacao de press
- [ ] Particulas de gas verde flutuando (pelo menos 20)
- [ ] Versao do jogo no canto inferior esquerdo
- [ ] Sem erros no console

---

## Dependencias

- **Slice 01 pronto** (projeto roda)
- **Slice 02 pronto** (splash -> menu)
- **Assets criticos:** `bg_sky.png`, `logo_zumbis.png` — se nao existirem, usar placeholders de retangulos (ja no esqueleto atual)
- **Assets desejados:** `bg_congress.png`, `bg_ministries.png`, `menu_theme.ogg`

---

## Estimativa

**4 pomodoros:**
1. Implementar background parallax (3 layers, scroll-factor no create)
2. Logo com animacao de flutuacao
3. Botoes com hover/click feedback e sons
4. Particulas de gas + polish visual

---

## Spec Detalhada

### Layout das camadas (Z-depth order)

```
DEPTH -1000 : Layer SKY       (bg_sky.png, scrollFactor: 0) — ceu nunca se move
DEPTH -900  : Layer CONGRESS  (bg_congress.png, scrollFactor: 0.1) — quase parado
DEPTH -600  : Layer MINISTRIES (bg_ministries.png, scrollFactor: 0.25) — lento
DEPTH -400  : Particulas gas (circulos verdes, scrollFactor vario)
DEPTH 800   : Logo + Botoes + UI
```

### Parallax no menu (sem input de movimento)

O menu nao tem scroll de camera. O efeito parallax e simulado via tween lento
nos backgrounds, criando a ilusao de uma leve brisa / respiracao do cenario:

```typescript
// Congresso: move 4px para direita em 8s, volta, loop infinito
this.tweens.add({
  targets: congress,
  x: congress.x + 4,
  duration: 8000,
  yoyo: true,
  repeat: -1,
  ease: 'Sine.easeInOut',
});

// Ministerios: move 8px para direita em 6s (mais rapido que Congresso)
this.tweens.add({
  targets: ministries,
  x: ministries.x + 8,
  duration: 6000,
  yoyo: true,
  repeat: -1,
  ease: 'Sine.easeInOut',
});
```

### Logo: posicionamento e animacao

```typescript
// Posicao: X centrado, Y = 20% da altura (topo, nao centro)
const logoY = VIEWPORT.HEIGHT * 0.22;

// Se asset existe:
const logo = this.textures.exists('menu_logo')
  ? this.add.image(cx, logoY, 'menu_logo').setOrigin(0.5)
  : this.add.text(cx, logoY, 'ZUMBIS DE BRASILIA', { /* estilo */ }).setOrigin(0.5);

// Flutuacao suave (seno)
this.tweens.add({
  targets: logo,
  y: logoY - 4,
  duration: 2500,
  yoyo: true,
  repeat: -1,
  ease: 'Sine.easeInOut',
});
```

### Botoes: layout e espacamento

Viewport e 480x270. Logo ocupa a regiao superior.
Botoes ficam no centro-inferior:

```
Y = 155px : JOGAR
Y = 175px : OPCOES
Y = 195px : SAIR
```

Cada botao: 100x14px, centrado no X=240.

### Musica: iniciar no create()

```typescript
// Phaser so inicia audio apos gesto do usuario (iOS restriction).
// O unlock foi feito no BootScene. Aqui podemos tocar diretamente.
if (!this.sound.get('menu_music')) {
  this.sound.add('menu_music', { loop: true, volume: 0.7 });
}
const music = this.sound.get('menu_music') as Phaser.Sound.BaseSound;
if (music && !music.isPlaying) {
  music.play();
}
```

### SFX de hover: um por sessao de hover (nao repetir enquanto mouse nao sair)

```typescript
btn.on('pointerover', () => {
  this.sound.play('ui_hover', { volume: 0.5 });
  // ... mudanca visual
});
// pointerout nao toca som
btn.on('pointerout', () => {
  // ... reverter visual
});
```

### Shutdown: parar musica corretamente

```typescript
shutdown(): void {
  // Musica continua tocando entre scenes do menu — so para ao ir pro jogo
  // NÃO stopar aqui se for para ModeSelect ou Settings
  // Stopar so se for para Q101Gameplay
  // Implementar via EventBus.on(EVENTS.START_GAME, () => music.stop())
}
```

---

## Checklist de Polish

- [ ] Logo tem um "brilho" sutil pulsando atras (rectangle com alpha e glow tween)
- [ ] Gas verde aparece lentamente (fade-in de cada particula apos 500ms de enter)
- [ ] Texto de copyright minusculo no canto inferior direito: "© Andre Guedes 2026"
- [ ] Botao SAIR muda de cor para vermelho no hover (diferente dos outros)
- [ ] A mensagem "Aqui nao tem saida" tem fonte maior e um fundo semi-transparente
- [ ] Transicao ao clicar JOGAR: fade to black 400ms antes de iniciar ModeSelect
- [ ] Cursor personalizado (opcional — sprite de chinelo como cursor)
