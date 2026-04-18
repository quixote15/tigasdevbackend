# Quest 00 — Prompts de Geracao de Assets
### Tim Sweeney — Asset Pipeline | Abril 2026

---

> Assets para a Quest 00 (tela inicial, menu principal, selecao de modo).
> Todos os prompts estao prontos para uso em PixelLab, Aseprite + Stable Diffusion, ou Retrodiffusion.
> Referencia visual base: doc `17-art-direction-pivot-sideview.md` (estilo Andre Guedes, grotesco brasileiro).

---

## Convencoes Globais

- **Viewport logico:** 480x270px (16:9)
- **Paleta:** Sempre usar cores "sujas" — nunca puras. Ver `assets/tiles/color-palette.md`
- **Estilo:** Caricatura grotesca brasileira. Tracos grossos, proporcoes exageradas, textura de impressao offset barata.
- **Fundo:** Sempre ceu apocaliptico — gradiente `#FF6B35 -> #8B0000 -> #2D0A0A` de baixo para cima
- **Pixel art:** Anti-aliasing OFF. `image-rendering: pixelated` no CSS.
- **Exportacao:** PNG com transparencia quando necessario. Sem fundo branco.

---

## ASSET 01 — Logo "Zumbis de Brasilia"

**Arquivo destino:** `public/assets/sprites/menu/logo_zumbis.png`
**Tamanho:** 320x80px
**Frames:** 1 (estatico) + opcional: 3 frames de "sangue gotejando" (32px cada para animar)

### Prompt para PixelLab / Retrodiffusion:

```
Pixel art logo. Text "ZUMBIS DE BRASILIA" in bold grotesque hand-lettered style.
Font inspired by Brazilian cordel literature woodcut prints, thick uneven strokes.
Letters slightly warped, as if written with dripping blood.
Color scheme: main text #F0E8D8 (cream/off-white), thick outline #1A1A18 (near-black).
Drop shadow: #8B0000 (dark red), offset 2px right and 2px down.
Green toxic drips hanging from letters: #4A7C59 (muted green), 3-4 drops of varying length.
Background: transparent.
Style: 1990s Brazilian horror B-movie poster lettering.
Canvas: 320x80px, pixel art, no antialiasing.
```

### Prompt alternativo para Stable Diffusion (img2img com sketch):

```
Pixel art game logo "ZUMBIS DE BRASILIA", Brazilian political zombie game.
Style: 16-bit retro, Metal Slug pixel art aesthetic combined with Brazilian cordel literature woodcuts.
Bold outlined letters with green toxic slime drips. Blood red shadows.
Color palette: cream text, near-black outline, dark red shadows, toxic green drips.
Transparent background. 320x80 pixels. No antialiasing. Crisp pixel edges.
Reference: Robert Crumb underground comics lettering meets arcade game logo.
```

### Variantes necessarias:
- `logo_zumbis.png` — versao completa (320x80)
- `logo_zumbis_small.png` — versao reduzida para HUD (160x40)

---

## ASSET 02 — Background do Menu Principal: Ceu + Congresso

**Arquivo destino:** `public/assets/sprites/menu/bg_sky.png` + `bg_congress.png`
**Tamanho:** 480x270px (layer de ceu) / 320x120px (Congresso isolado)
**Frames:** 1 (estatico, parallax feito no codigo)

### Prompt — Layer Ceu (bg_sky.png):

```
Pixel art background layer. Sky gradient from bottom to top:
- Bottom 30%: #FF6B35 (bloody orange), intense apocalyptic sunset
- Middle 40%: #8B0000 (dark red), heavy oppressive atmosphere
- Top 30%: #2D0A0A (near-black), night closing in
Scattered toxic clouds: semi-transparent green (#4A7C59 at 40% opacity), irregular shapes.
Clouds have a sickly glow, not fluffy — they look like gas emissions.
3-4 cloud clusters at different Y positions.
Paper texture overlay: 3-5% gaussian noise simulating cheap offset printing.
Style: Brazilian B-movie horror, apocalyptic Brazilian cerrado sky.
Canvas: 480x270px. No figures, no buildings — ONLY sky and clouds.
```

### Prompt — Silhueta do Congresso Nacional (bg_congress.png):

```
Pixel art silhouette of the Brazilian Congress building (Congresso Nacional, Brasilia).
Viewed from street level, frontal perspective. The iconic architecture:
- Left side: concave dome (Câmara dos Deputados) — bowl/plate shape facing down
- Right side: convex dome (Senado Federal) — inverted bowl/dome facing up
- Center: two tall rectangular towers between the domes
- Long horizontal base connecting everything, with a ceremonial ramp

Silhouette color: #1A1A18 (near-black), with ZERO interior detail at this scale.
Sinister green glow emanating from between the towers: #3D6B3A, pulsing light effect.
Green glow subtly illuminates the tops of the domes from within.
Background: transparent (sky added by code).

Canvas: 320x120px. The building fills the canvas horizontally.
Style: ominous silhouette, like a haunted castle in a side-scroller.
Pixel art, no antialiasing, crisp edges.
Reference: actual Congress building architecture — get the dome shapes right.
```

---

## ASSET 03 — Background dos Ministerios (menu parallax layer)

**Arquivo destino:** `public/assets/sprites/menu/bg_ministries.png`
**Tamanho:** 480x160px (as duas fileiras de blocos ficam nos lados, ceu ao centro)
**Frames:** 1

### Prompt:

```
Pixel art background. Two rows of brutalist ministry buildings, viewed from street level,
as if standing in the middle of the Esplanada dos Ministerios (Brasilia, Brazil) looking forward.
Buildings on LEFT side and RIGHT side of the frame, leaving center open.

Building style: Oscar Niemeyer brutalist concrete blocks.
- Color: #8A8580 (dirty concrete gray), variations #7A7A72 for shadows
- Windows: #1A1A18 (dead black), arranged in regular grids like dead eyes
- Cracks and humidity stains on concrete surfaces
- Green satirical signs visible on some buildings (text too small to read clearly)
- Some windows broken on upper floors

Left buildings taller, right buildings slightly shorter — depth perspective.
Foreground hint: dead cerrado trees (twisted trunks, no leaves, #5C5C55), 
knocked-over lamp posts, campaign poster placards.

Background: transparent (sky added by code behind this layer).
Canvas: 480x160px. Buildings should be 120-160px tall on the sides.
Pixel art, no antialiasing. Thick outlines #1A1A18 2-3px on silhouettes.
Style: Metal Slug background art + Brazilian political satire.
```

---

## ASSET 04 — Retrato Ze Cidadao (menu selecao de modo)

**Arquivo destino:** `public/assets/sprites/personagens/ze-cidadao/portrait.png`
**Tamanho:** 96x96px (retrato para menu) + sprite sheet separado para gameplay
**Frames:** 1 (retrato estatico)

### Referencia de personagem (de 24-storytelling-modos-de-jogo.md):
Ze, 34 anos. Servidor publico federal. Ministerio do Planejamento.
- Cabeca grande, corpo atarracado
- Polo azul desbotada comprada no Bras
- Bermuda jeans cortada
- Chinelo Havaianas azul com tiras soltas
- Olheiras profundas
- Cracha funcional no pescoco
- Expressao: desespero pragmatico, nao heroismo

### Prompt:

```
Pixel art character portrait. Brazilian "Ze Cidadao" (average government worker).
Bust-up portrait (head and shoulders), facing slightly right, looking at viewer with tired resignation.

Physical description:
- Big head (30% of canvas), disproportionately large per caricature style
- Short, stocky body
- Faded blue polo shirt (cheap quality, slightly too tight)
- Cut-off jean shorts visible at bottom frame
- Blue Havaianas flip-flops straps visible
- Deep dark circles under eyes (someone who catches bus at 5:30am)
- Federal employee badge hanging from neck (small, barely readable)
- 3 skin tone variants needed: light, medium, dark (separate PNG files)

Expression: exhausted, sarcastic "why is this my problem" face.
NOT heroic — more like a man who just wants to go home.

Color palette: Faded blues and grays for clothing. Skin tones "dirty" not pure.
Background: transparent for portrait, dark vignette gradient around edges.

Style: Andre Guedes Brazilian political caricature meets Metal Slug sprite art.
Robert Crumb-inspired grotesque proportions. Thick outlines. Cross-hatching for shadows.
Canvas: 96x96px. Pixel art, no antialiasing.
```

---

## ASSET 05 — Retrato Waldeco Politico (menu selecao de modo)

**Arquivo destino:** `public/assets/sprites/personagens/waldeco-politico/portrait.png`
**Tamanho:** 96x96px
**Frames:** 1

### Referencia de personagem:
Waldeco, vereador em 3o mandato. Comissao de nada. Subsidio de R$ 22.800/mes.
- Terno barato que parece caro de longe
- Barriga proeminente, ombros inflados
- Sorriso de campanha permanente (nao chega aos olhos)
- Cabelo impecavelmente penteado (esconde calvice)
- Crachá de partido na lapela
- Sapato de verniz, muito brilhoso

### Prompt:

```
Pixel art character portrait. Brazilian "Waldeco Politico" (corrupt local politician, vereador).
Bust-up portrait, facing slightly left, giving exaggerated campaign-smile to viewer.

Physical description:
- Big head, bigger smile (teeth too white, too many teeth visible)
- Cheap suit that tries to look expensive: #2A3A5A (dirty blue), ill-fitting
- Belly straining against suit jacket buttons
- Inflated shoulders (power pose)
- Hair perfectly combed, covering bald spot, slightly shiny (#5C4030 brown)
- Party badge on lapel (abstract, no real party colors — mix of all colors)
- Eyes: small, shifty, not matching the smile. Politicians eyes.
- Gold ring on right hand, visible at frame edge.

Expression: campaign-poster smile hiding calculation and survival instincts.
The smile does NOT reach the eyes. Practiced insincerity.

Color palette: Dirty blues and grays for suit. Gold accents. 
Background: transparent, dark vignette.

Style: same Andre Guedes grotesque caricature style as Ze Cidadao portrait.
More exaggerated — this character is less human, more political archetype.
Canvas: 96x96px. Pixel art, no antialiasing. Thick outlines, cross-hatching shadows.
```

---

## ASSET 06 — Botoes e UI Atlas

**Arquivo destino:** `public/assets/sprites/ui_atlas.png` + `ui_atlas.json`
**Tamanho do atlas:** 256x256px (TexturePacker ou manual)
**Sprites incluidos:**

### Prompt — Sprites individuais para compor o atlas:

```
Pixel art UI sprite sheet for Brazilian zombie game. Individual sprites to be packed into atlas.

BUTTONS (each 100x14px, 3 states: normal / hover / pressed):
- btn_play_normal: "JOGAR" button, dark background #1A1A18, cream text #F0E8D8, green border #4A7C59
- btn_play_hover: same, green fill #4A7C59 at 40%, golden text #F0C830
- btn_play_pressed: slightly smaller scale (95%), same as hover
- btn_options_*: "OPCOES" button, same dimensions, same 3 states
- btn_back_*: "< VOLTAR" button, 60x14px, muted gray style

SELECTION CARDS (100x160px each):
- card_cidadao_normal: card border in green #4A7C59, dark fill
- card_cidadao_hover: green border brighter, fill lighter
- card_politico_normal: card border in amber #D47820, dark fill  
- card_politico_hover: amber border brighter, fill lighter

DECORATIVE:
- divider_line: 1x100px vertical line, concreto gray #8A8580
- corner_ornament: 8x8px corner decoration, brutalist concrete style

ICONS (16x16px each):
- icon_volume: speaker icon, cream color
- icon_music: music note, cream color
- icon_fullscreen: expand arrows, cream color
- icon_back: left arrow, cream color

Style: All sprites pixel art, thick outlines #1A1A18, no antialiasing.
Consistent visual language: brutalist concrete UI meets Brazilian B-movie aesthetic.
```

---

## ASSET 07 — Fontes Bitmap

**Arquivo destino:** `public/assets/fonts/`
**Formato:** PNG + XML (Phaser BitmapFont format, compativel com Phaser.GameObjects.BitmapText)

### Instrucoes de geracao (nao ha prompt de IA — fontes bitmap sao manuais):

```
Para gerar as fontes bitmap, usar Littera (littera.gulash.com) ou bmGlyph:

FONTE 01: "Manchete" (titulos e botoes)
- Base: fonte Bold condensada, altamente stylized
- Tamanho: 16px de altura (no atlas)
- Caracteres: A-Z, 0-9, !, ., -, _, espaço, e acentuados (A,E,I,O,U com acento)
- Cor: #F0E8D8 (cream) com outline 2px #1A1A18
- Exportar como: manchete.png + manchete.xml

FONTE 02: "Corpo" (descricoes e texto pequeno)
- Base: fonte monospace, clean mas com personalidade
- Tamanho: 8px de altura (no atlas)
- Caracteres: completo A-Z, a-z, 0-9, pontuacao basica, acentuados
- Cor: #8A8580 (concreto) com outline 1px #1A1A18
- Exportar como: corpo.png + corpo.xml

Alternativa rapida: usar "Press Start 2P" do Google Fonts como placeholder.
E pixel art nativa, gratuita, e funciona bem em bitmap. Trocar no polish.
```

---

## ASSET 08 — Trilha Sonora do Menu

**Arquivo destino:** `public/assets/audio/music/menu_theme.ogg`
**Duracao:** 60-90 segundos (loop perfeito)
**Formato:** OGG Vorbis (primario) + MP3 (fallback)

### Brief para compositor / prompt para AI music tools (Suno, Udio, etc.):

```
Music brief for Brazilian zombie game main menu theme.

Genre: Choro-punk, Brazilian samba-funk with horror undertones.
Tempo: 85 BPM (slower than in-game action tracks — this is menu, build anticipation).

Structure (60 seconds, perfect loop):
- 0:00-0:08: Intro — single cavaquinho picking a sinister chord progression
- 0:08-0:20: Main theme enters — baiao rhythm on drums + cavaquinho + low brass
- 0:20-0:40: Full arrangement — zombie groans as rhythmic element, zabumba kick
- 0:40-0:52: Bridge — music gets tense, trumpet screech, chaos builds
- 0:52-1:00: Return to beginning with slight variation, loops seamlessly

Instrumentation: cavaquinho, zabumba, surdo, pandeiro, trombone, trumpet, electric bass.
Horror elements: occasional moan/groan (political speech samples pitched down), 
scratchy vinyl noise, distant crowd chanting (distorted).

Mood: ominous comedy. Like a forró version of a zombie movie theme.
Reference audio: "Forró do Zumbi" meets Goblin's "Dawn of the Dead" soundtrack.
NO jump scares in the menu theme. Build tension, not startle.
Instrumentation must feel distinctly Brazilian — no American rock/metal.
```

### SFX do Menu (arquivos individuais em `public/assets/audio/sfx/`):

```
ui_hover.ogg — hover sobre botao:
  Sound: single cavaquinho string pluck, short (0.2s), pitch G4, slightly muffled
  NOT a digital beep. Organic string instrument feel.

ui_click.ogg — clique em botao:
  Sound: stamp on paper + rubber seal sound, 0.3s
  Think: carimbo de protocolo batendo na mesa. Bureaucratic satisfaction.

ui_back.ogg — botao voltar:
  Sound: paper crumple + brief air escape, 0.2s
  Think: formulario sendo amassado e jogado fora.

ui_select_mode.ogg — selecionar modo (Cidadao ou Politico):
  Sound: broadcast jingle (2-note sting), 0.5s, brass + fanfare feel
  Like: opening jingle of a Brazilian TV news show, but slightly wrong/ominous.

mode_cidadao.ogg — confirmar modo Cidadao:
  Sound: worn Havaianas flip-flop thwap + crowd murmur fading in
  Duration: 0.8s

mode_politico.ogg — confirmar modo Politico:
  Sound: microphone feedback squeal + single clap echoing in empty chamber
  Duration: 0.8s
```

---

## Resumo: Assets Faltantes vs Existentes

| Asset | Status | Arquivo de Destino | Acao |
|---|---|---|---|
| Logo "Zumbis de Brasilia" | FALTANDO | `sprites/menu/logo_zumbis.png` | Gerar com prompt 01 |
| Background: ceu | FALTANDO | `sprites/menu/bg_sky.png` | Gerar com prompt 02a |
| Background: Congresso silhueta | FALTANDO | `sprites/menu/bg_congress.png` | Gerar com prompt 02b |
| Background: Ministerios | FALTANDO | `sprites/menu/bg_ministries.png` | Gerar com prompt 03 |
| Retrato Ze Cidadao | FALTANDO | `sprites/personagens/ze-cidadao/portrait.png` | Gerar com prompt 04 |
| Retrato Waldeco Politico | FALTANDO | `sprites/personagens/waldeco-politico/portrait.png` | Gerar com prompt 05 |
| UI Atlas (botoes, cards) | FALTANDO | `sprites/ui_atlas.png` | Gerar com prompt 06 |
| Fonte bitmap "Manchete" | FALTANDO | `fonts/manchete.png+xml` | Manual (Littera) |
| Fonte bitmap "Corpo" | FALTANDO | `fonts/corpo.png+xml` | Manual (Littera) |
| Trilha menu | FALTANDO | `audio/music/menu_theme.ogg` | Brief prompt 08 |
| SFX UI (hover, click, back) | FALTANDO | `audio/sfx/ui_*.ogg` | SFX prompt 08 |
| Sprites Ze (gameplay) | EXISTE (parcial) | `personagens/lula/` (ref) | Adaptar para Ze |
| Sprites politicos (gameplay) | EXISTE | `personagens/*/sprites/` | Usar Q1-01 |
| Tiles Esplanada | EXISTE (spec) | `tiles/esplanada/` | Ver PLANO-CENARIOS-MVP.md |
| Paleta de cores | EXISTE | `tiles/color-palette.md` | Referencia base |
| Prompts de personagens | EXISTE | `prompts/agent-0*.md` | Referencia para Ze/Waldeco |

### Assets Criticos para Quest 00 (bloqueiam slices):
- **Slice 02 (splash):** precisa `logo_zumbis.png`
- **Slice 03 (menu):** precisa `bg_sky.png`, `bg_congress.png`, `bg_ministries.png`
- **Slice 04 (mode select):** precisa `portrait_cidadao.png`, `portrait_politico.png`
- **Slice 05 (settings):** precisa `ui_atlas.png` (botoes e sliders)
- **Todos os slices:** `ui_hover.ogg`, `ui_click.ogg` (SFX de interacao)

### O que pode ser desenvolvido SEM os assets (placeholders funcionam):
- Slice 01: tela preta + texto. Zero assets necessarios.
- Slices 02-06: todos tem fallback de retangulos coloridos + texto monospace no codigo.
  O desenvolvedor pode entregar os slices e os assets sao substituidos depois.
