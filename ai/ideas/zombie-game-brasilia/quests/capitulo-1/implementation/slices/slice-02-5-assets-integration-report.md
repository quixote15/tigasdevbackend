# Slice 02.5 — Relatorio de Integracao de Assets
### Frontend: Masahiro Sakurai | Abril 2026

---

## Status Geral

- Typecheck: ZERO erros (tsc --noEmit)
- Build: PASSA (vite build, 3.38s)
- Dev server: HTTP 200 confirmado
- Assets copiados: 4 arquivos
- Assets gerados via PixelLab: ZERO — MCP indisponivel (detalhes abaixo)

---

## PixelLab MCP — Situacao

O MCP `pixellab` (ferramentas `mcp__pixellab__*`) NAO ESTA DISPONIVEL nesta sessao de Claude Code. A busca via ToolSearch retornou zero resultados. Nenhuma geracao de imagem foi possivel nesta etapa.

Impacto: os assets criticos listados na secao "O que ainda falta" precisam ser gerados manualmente usando os prompts em `/ideas/zombie-game-brasilia/assets/prompts/quest-00-prompts.md`.

---

## O que foi copiado (Etapa 1)

### Assets copiados para o projeto de jogo

| Origem | Destino no projeto | Dimensoes | Decisao |
|---|---|---|---|
| `tiles/esplanada/generated/bg-congresso-nacional.png` | `public/assets/sprites/menu/bg_congress.png` | 256x96 RGBA | Backup top-down |
| `tiles/esplanada/generated/sideview/sideview-bg-congresso.png` | `public/assets/sprites/menu/bg_congress_sideview.png` | 320x120 RGBA | **Em uso** — perspectiva lateral correta |
| `tiles/esplanada/generated/sideview/sideview-ministerio-far.png` | `public/assets/sprites/menu/bg_ministries.png` | 80x100 RGBA | Ministerio distante, espelhado no codigo |
| `personagens/lula/sprites/humano/animations/idle/idle-south_frame0.png` | `public/assets/sprites/personagens/cidadao/portrait_placeholder.png` | 64x64 RGBA | Portrait provisorio Ze Cidadao |
| `personagens/flavio-bolsonaro/sprites/humano/animations/idle/idle-south_frame0.png` | `public/assets/sprites/personagens/politico/portrait_placeholder.png` | 64x64 RGBA | Portrait provisorio Waldeco Politico |

### Assets espelhados no design system

Copiados tambem para `ideas/zombie-game-brasilia/assets/menu/`:
- `bg_congress.png`
- `bg_congress_sideview.png`
- `bg_ministries.png`

---

## Decisoes de design

### Qual Congresso usar

O arquivo `bg_congress_sideview.png` (320x120) e o correto para o jogo pivotado para side-scroller. Ele mostra a silhueta do Congresso em perspectiva lateral com brilho verde entre as torres. E carregado com chave `menu_bg_congress` e ativo no PreloadScene.

O `bg_congress.png` (256x96, top-down) foi copiado como backup mas nao esta em uso.

### Portrait do Ze Cidadao

Decisao deliberada: usar `lula/idle-south_frame0.png` como face do modo Cidadao. Ironia narrativa — o zumbi imortal institucionalizado como arquetipo do "servidor publico comum". O jogo e satira. O jogador que escolhe o modo Cidadao esta escolhendo uma vida de sobrevivencia metabolica. A face reconhecivel refor o absurdo.

### Portrait do Waldeco Politico

`flavio-bolsonaro/idle-south_frame0.png` como politico generico. Terno, postura, expressao — funciona como arquetipo. Substituir quando o portrait real do Waldeco for gerado.

### Sprites top-down como retratos

Os sprites existentes sao 64x64 top-down. Para um portrait estatico congelado no menu, isso e aceitavel — o jogador ve um personagem de cima, o que cria um efeito levemente estranho mas coerente com a estetica grotesca do jogo. Nao e o ideal. E funcional.

### Ministerios espelhados

`bg_ministries.png` (80x100) e pequeno para o viewport. No MainMenuScene ele e renderizado duas vezes — normal na esquerda, flipX na direita — criando ilusao de dois blocos ministeriais nos flancos. Depth MENU_BG (-500), atras do Congresso (DEPTHS.MENU_BG + 1 = -499).

---

## O que foi gerado via PixelLab

NENHUM. MCP indisponivel.

---

## O que ainda falta (critico para Quest 00)

### Bloqueadores de Slice 02 (Splash com logo real)
- `public/assets/sprites/menu/logo_zumbis.png` — 320x80px
  - Prompt: ASSET 01 em `quest-00-prompts.md`
  - Ferramentas: PixelLab, Retrodiffusion, Aseprite, ou qualquer gerador de pixel art

### Bloqueadores de Slice 03 (MainMenu completo)
- `public/assets/sprites/menu/bg_sky.png` — 480x270px, gradiente apocaliptico
  - Prompt: ASSET 02 (layer ceu) em `quest-00-prompts.md`
- `public/assets/sprites/menu/bg_ministries.png` — 480x160px (versao completa com dois lados)
  - Prompt: ASSET 03 em `quest-00-prompts.md`
  - O placeholder atual (80x100) nao e suficiente para o parallax completo

### Bloqueadores de Slice 04 (ModeSelect com portraits definitivos)
- `public/assets/sprites/personagens/ze-cidadao/portrait.png` — 96x96px
  - Prompt: ASSET 04 em `quest-00-prompts.md`
- `public/assets/sprites/personagens/waldeco-politico/portrait.png` — 96x96px
  - Prompt: ASSET 05 em `quest-00-prompts.md`

### Bloqueadores de Slice 05 (Settings com UI real)
- `public/assets/sprites/ui_atlas.png` + `ui_atlas.json`
  - Prompt: ASSET 06 em `quest-00-prompts.md`

### Audio (todos os slices interativos)
- `public/assets/audio/music/menu_theme.ogg`
- `public/assets/audio/sfx/ui_click.ogg`
- `public/assets/audio/sfx/ui_hover.ogg`
- `public/assets/audio/sfx/ui_back.ogg`
- Brief: ASSET 08 em `quest-00-prompts.md`

### Fontes bitmap
- `public/assets/fonts/manchete.png` + `manchete.xml`
- `public/assets/fonts/corpo.png` + `corpo.xml`
- Instrucoes: ASSET 07 em `quest-00-prompts.md` (Littera ou Press Start 2P como placeholder)

---

## O que o usuario ve agora

### Tela de Loading (PreloadScene)
Fundo preto. Texto "ZUMBIS DE BRASILIA" em monospace creme. Barra de progresso verde (#4A7C59) preenchendo enquanto 4 assets carregam (bg_congress_sideview + bg_ministries + portrait_cidadao + portrait_politico). Texto de porcentagem abaixo. Total de tempo: rapido, assets somam menos de 50KB.

### Splash (SplashScene)
Tres camadas de gradiente apocaliptico (laranja sangue / vermelho queimado / quase preto). Particulas de gas verde flutuando. Texto "ZUMBIS DE BRASILIA" pulsando lentamente (escala 1.0 -> 1.02 -> 1.0). Subtitulo narrativo "Brasilia, 8 de jan de 2023. A nevoa verde subiu." em cinza. Hint de skip no rodape.

Sem logo real ainda. Quando `logo_zumbis.png` existir, o SplashScene ja tem o fallback implementado — simplesmente descomentar `this.load.image('menu_logo', ...)` no PreloadScene.

### Menu Principal (MainMenuScene)
Gradiente de ceu placeholder + silhueta do Congresso Nacional na base da tela (320x120, escalada 1.5x para preencher 480px de largura, ancoragem inferior). Dois blocos de ministerio nos flancos (espelhados). Tres botoes: JOGAR, OPCOES, SAIR. Hover: fundo verde, texto dourado. Click: squish 95% rapido (80ms).

### Selecao de Modo (ModeSelectScene)
Dois cards lado a lado. Card esquerdo (Ze Cidadao): portrait do Lula idle-south 64x64, borda verde, descricao do servidor publico federal. Card direito (Waldeco Politico): portrait do Flavio Bolsonaro idle-south 64x64, borda ambar, descricao do vereador. Botao SELECIONAR em cada card. Botao VOLTAR no rodape.

---

## Alteracoes de codigo

### PreloadScene.ts
- Descomentado: `this.load.image('menu_bg_congress', ...)` — aponta para bg_congress_sideview.png
- Descomentado: `this.load.image('menu_bg_ministries', ...)`
- Descomentado: `this.load.image('portrait_cidadao', ...)` — aponta para placeholder
- Descomentado: `this.load.image('portrait_politico', ...)` — aponta para placeholder
- Comentados com TODO: menu_bg_sky, menu_logo (ainda nao existem), e paths finais dos portraits

### MainMenuScene.ts
- Adicionado: render condicional do `menu_bg_congress` (silhueta do Congresso ancoranda na base)
- Adicionado: render condicional do `menu_bg_ministries` (dois blocos espelhados nos flancos)
- Guards `this.textures.exists()` garantem que a scene nao quebra se o asset faltar

### ModeSelectScene.ts
- Substituido: rectangle placeholder por `this.add.image()` condicional para portraits reais
- Fallback: rectangle + texto inicial caso a textura nao exista (mesma UX anterior)

---

## Proximos passos recomendados

1. Gerar `logo_zumbis.png` com PixelLab ou Retrodiffusion usando prompt ASSET 01. Descomentar no PreloadScene. Ganho imediato de polish na Splash.

2. Gerar `bg_sky.png` (480x270). Integrar na SplashScene e MainMenuScene substituindo os rectangulos empilhados. Maior impacto visual por menor esforco.

3. Gerar portraits Ze Cidadao e Waldeco Politico (96x96). Criar diretorios `ze-cidadao/` e `waldeco-politico/` em `public/assets/sprites/personagens/`. Atualizar paths no PreloadScene.

4. Considerar Press Start 2P como fonte bitmap provisoria para Slice 03. Zero custo, disponivel via Google Fonts, funciona como BitmapFont no Phaser com conversao simples.

5. Gerar SFX prioritarios: `ui_click.ogg` e `ui_hover.ogg`. Mesmo sendo curtos, eles elevam brutalmente o game feel. O carimbo de protocolo como click e imprescindivel para a identidade sonora do jogo.
