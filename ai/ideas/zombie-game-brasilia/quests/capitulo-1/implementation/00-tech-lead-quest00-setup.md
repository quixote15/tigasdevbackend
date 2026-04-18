# Quest 00 — Setup Master
### Tim Sweeney — Tech Lead | Abril 2026

---

> *"Quest 00 nao tem gameplay. Mas e onde o jogador decide se vai continuar ou nao. Menu lento, botao que nao reage, musica que nao toca no iOS — cada um desses mata a sessao antes do primeiro zumbi aparecer. Faz isso certo primeiro."*

---

## Status de Assets (Etapa 1)

### Inventario completo

| Asset | Existe? | Caminho atual | Acao necessaria |
|---|---|---|---|
| Sprites de personagens (bosses) | SIM | `assets/personagens/lula/sprites/`, `bolsonaro/sprites/` etc. | Usar como referencia para Ze/Waldeco |
| Armas (chinelo, vassoura, etc.) | SIM | `assets/armas/chinelo/`, `assets/armas/vassoura/` | Usar em Q1-01 |
| Tiles Esplanada (spec completa) | SIM (spec) | `assets/tiles/esplanada/`, `PLANO-CENARIOS-MVP.md` | Gerar sprites a partir da spec |
| Paleta de cores | SIM | `assets/tiles/color-palette.md` | Referencia para todos os novos assets |
| Audio: bordoes dos personagens | SIM | `assets/audio/bordoes/` (25 arquivos) | Usar em Q1-01 |
| Audio: musica (pasta vazia) | SIM (pasta) | `assets/audio/musica/` | Vazia — gerar com brief do quest-00-prompts.md |
| Audio: sfx (pasta vazia) | SIM (pasta) | `assets/audio/sfx/` | Vazia — gerar com brief do quest-00-prompts.md |
| Audio: ambiente (pasta vazia) | SIM (pasta) | `assets/audio/ambiente/` | Vazia — para Q1-01 |
| Prompts de personagens (agentes) | SIM | `assets/prompts/agent-01-bosses.md` ate `agent-08-audio.md` | Referencia para Ze e Waldeco |
| Context base de prompts | SIM | `assets/prompts/context-base.md` | Usar em todos os novos prompts |
| **Logo "Zumbis de Brasilia"** | **NAO** | `assets/sprites/menu/logo_zumbis.png` | **GERAR** — Prompt 01 |
| **Background ceu (menu)** | **NAO** | `assets/sprites/menu/bg_sky.png` | **GERAR** — Prompt 02a |
| **Silhueta Congresso** | **NAO** | `assets/sprites/menu/bg_congress.png` | **GERAR** — Prompt 02b |
| **Fachadas Ministerios** | **NAO** | `assets/sprites/menu/bg_ministries.png` | **GERAR** — Prompt 03 |
| **Retrato Ze Cidadao** | **NAO** | `assets/sprites/personagens/ze-cidadao/portrait.png` | **GERAR** — Prompt 04 |
| **Retrato Waldeco Politico** | **NAO** | `assets/sprites/personagens/waldeco-politico/portrait.png` | **GERAR** — Prompt 05 |
| **UI Atlas (botoes, cards)** | **NAO** | `assets/sprites/ui_atlas.png` | **GERAR** — Prompt 06 |
| **Fontes bitmap** | **NAO** | `assets/fonts/manchete.png+xml` | **GERAR** — Manual (Littera) |
| **Trilha menu** | **NAO** | `assets/audio/music/menu_theme.ogg` | **GERAR** — Brief 08 |
| **SFX de UI** | **NAO** | `assets/audio/sfx/ui_*.ogg` | **GERAR** — Brief 08 |

### Assets criticos vs. desejados

**Criticos (sem eles o jogador nao ve nada profissional — mas o codigo roda):**
- Logo — Slice 02 tem fallback em texto
- Retratos — Slice 04 tem fallback em retangulos
- Background ceu — Slice 03 tem fallback em gradiente de retangulos

**Desejados (melhoram muito mas nao bloqueiam):**
- Trilha do menu — silencio funciona
- SFX de UI — interacao funciona sem som

**Conclusao:** O Sakurai (frontend dev) pode implementar todos os 6 slices sem esperar os assets. Os placeholders no codigo sao funcionais. Os assets sao substituicao de sprint posterior.

---

## Plano de Geracao de Assets Faltantes (Etapa 2)

Todos os prompts detalhados estao em:
`/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/assets/prompts/quest-00-prompts.md`

### Ordem de prioridade de geracao

1. **Logo** (Prompt 01) — Impacto visual imediato, primeira impressao. Gerar antes de qualquer demo.
2. **Background Ceu + Congresso** (Prompts 02a e 02b) — Define o tom visual do menu principal.
3. **Retratos Ze + Waldeco** (Prompts 04 e 05) — Necessarios para o flow de selecao ser narrativo.
4. **SFX de UI** (Brief 08, secao SFX) — Podem ser gerados em 1-2h com ferramentas de SFX gratuitas.
5. **Ministerios Background** (Prompt 03) — Detalhe de polish no parallax.
6. **UI Atlas** (Prompt 06) — Ultimo, pois os botoes placeholder funcionam bem.
7. **Trilha do menu** (Brief 08) — Mais trabalhoso. Contratar compositor ou usar Suno/Udio.
8. **Fontes bitmap** — Manual no Littera. Ultimo pois monospace funciona como fallback.

### Ferramentas recomendadas

| Asset | Ferramenta primaria | Alternativa |
|---|---|---|
| Logo, backgrounds, retratos, UI | PixelLab (quando MCP voltar) | Aseprite manual + Retrodiffusion |
| SFX de UI | Bfxr / Sfxr (gratuito) | Freesound.org (licenca CC0) |
| Trilha do menu | Suno / Udio | Contratar musico brasileiro |
| Fontes bitmap | Littera (online, gratuito) | Aseprite font tool |

---

## Boilerplate Criado (Etapa 3)

### Localizacao do projeto

**Decisao:** O codigo do jogo fica em `/Users/ricardo.ribeiro_1/Desktop/my-studies/zumbis-brasilia-game/` — repositorio separado do repo de docs.

**Justificativa:** O repo `ai/ideas/zombie-game-brasilia/` tem 25+ documentos de design, ADRs, storytelling e arte. Misturar codigo fonte nele polui o historico de git, complica code review (PR mistura docs e codigo) e torna o bundle de CI mais lento (o CI precisaria ignorar todos os `.md`). Separar e a pratica padrao (monorepo de docs vs. monorepo de codigo).

### Arquivos criados

```
/Users/ricardo.ribeiro_1/Desktop/my-studies/zumbis-brasilia-game/
  package.json                    root workspace npm
  README.md                       instrucoes de como rodar
  apps/web/
    package.json                  dependencias: Phaser 3.88, React 18, Vite 5, TS 5.4
    tsconfig.json                 strict + noUncheckedIndexedAccess
    tsconfig.node.json            para o vite.config.ts
    vite.config.ts                manualChunks: { phaser }, brotli + gzip, aliases
    index.html                    Cache-Control: no-cache, viewport mobile
    public/
      _headers                    Cloudflare Pages: cache + CORS headers
    src/
      main.tsx                    React entry, strictMode
      App.tsx                     container, passa ref para PhaserGame
      index.css                   reset, image-rendering: pixelated
      components/
        PhaserGame.tsx            wrapper React do canvas, cleanup no unmount
      game/
        PhaserGame.ts             StartGame() factory, todas as scenes registradas
        EventBus.ts               singleton Phaser.Events.EventEmitter, EVENTS enum
        config/
          GameConstants.ts        VIEWPORT, LEVEL, PHYSICS, DEPTHS, SCROLL_FACTORS, PALETTE, SCENES
        scenes/
          BootScene.ts            unlock audio iOS, placeholder textures
          PreloadScene.ts         loading bar, comentarios de assets a carregar
          MainMenuScene.ts        3 botoes, parallax animado, particulas gas
          ModeSelectScene.ts      2 cards, selecao, confirmacao, EventBus.MODE_SELECTED
          SettingsScene.ts        esqueleto para Slice 05
```

---

## Slices de Entrega

| Slice | Titulo | Estimativa | Arquivo |
|---|---|---|---|
| 01 | Boilerplate Rodando | 3 pomodoros | `slices/slice-01-boilerplate-running.md` |
| 02 | Splash Screen | 2 pomodoros | `slices/slice-02-splash-screen.md` |
| 03 | Menu Principal | 4 pomodoros | `slices/slice-03-main-menu.md` |
| 04 | Selecao de Modo | 3 pomodoros | `slices/slice-04-mode-selection.md` |
| 05 | Opcoes de Audio | 3 pomodoros | `slices/slice-05-settings-audio.md` |
| 06 | Transicao para Q1-01 | 2 pomodoros | `slices/slice-06-transition-to-quest01.md` |
| **Total** | | **17 pomodoros (~7h)** | |

---

## Ordem de Execucao Recomendada

```
Slice 01 (boilerplate)
   |
   v
Slice 02 (splash) -- pode ser feito em paralelo com Slice 03 se houver 2 devs
   |
   v
Slice 03 (menu principal)
   |
   v
Slice 04 (selecao de modo)
   |
   v
Slice 05 (settings) -- pode ser feito em paralelo com Slice 06
   |
   v
Slice 06 (transicao Q1-01)
   |
   v
[Quest 00 entregue -- iniciar Q1-01]
```

O Slice 05 pode ser desenvolvido em paralelo com o Slice 06 se houver disponibilidade,
pois SettingsScene nao e dependencia de PrologueCutsceneScene.

---

## Bloqueadores e Decisoes Pendentes

### Bloqueadores resolvidos (sem acao necessaria do usuario)

1. **MCP pixellab desconectado** — Resolvido documentando prompts em `quest-00-prompts.md`. Quando o MCP voltar, os prompts estao prontos para execucao. Enquanto isso, os placeholders de retangulos/texto funcionam para desenvolvimento.

2. **Ausencia dos docs 03-tech-strategy.md e 04-product-requirements.md** — Recuperados via `git show` nos commits anteriores. Toda a informacao necessaria estava em `17-art-direction-pivot-sideview.md`, `22-tech-lead-sideview-arch.md`, `03-tech-lead-architecture.md` (Q1-01) e `24-storytelling-modos-de-jogo.md`.

### Decisoes pendentes (precisam de input)

1. **Personagem do Modo Politico:** O storytelling menciona "Ze" como nome do Cidadao, mas o Modo Politico nao tem nome definitivo nos docs. Usei "Waldeco Politico" como placeholder. Confirmar nome real com o diretor criativo (Andre Guedes).

2. **Prologo compartilhado vs. por modo:** O doc `03-tech-lead-architecture.md` define `PrologueCutsceneScene` como "cutscene comum a ambos os modos". O `24-storytelling-modos-de-jogo.md` define prologo so do ponto de vista do Cidadao. Clarificar: o Modo Politico tem prologo diferente ou entra direto na fase?

3. **SplashScene antes ou depois do PreloadScene?** O boilerplate atual coloca a sequencia como `Boot -> Preload -> Splash -> MainMenu`. Alternativa: `Boot -> Splash (logo sem assets) -> Preload (com barra) -> MainMenu`. A segunda opcao mostra algo imediatamente e e melhor UX em conexoes lentas. Decisao de produto — atual (Splash apos Preload) e mais simples de implementar.

### Nao e bloqueador mas precisa atenção antes da Q1-01

- `PrologueCutsceneScene` e um stub. Antes de Q1-01 ser implementada, o time de quest precisa decidir o script completo da cutscene de prologo e alimentar o `CutscenePlayer` definido em `03-tech-lead-architecture.md`.

---

## Como o Sakurai (Frontend Dev) Usa Este Material

1. `git clone` ou `cp -r` do diretorio `zumbis-brasilia-game/`
2. `cd zumbis-brasilia-game && npm install`
3. Executar Slice 01: confirmar que roda
4. Executar Slices 02-06 em sequencia, um por vez
5. Para cada slice: ler o `.md` do slice, implementar os arquivos listados, validar o criterio de pronto
6. Assets: se um asset nao existe, o placeholder de codigo ja esta no esqueleto. Nao bloquear por asset.
7. Quando todos os 6 slices estiverem verdes: abrir PR, taguear @tech-lead para review
