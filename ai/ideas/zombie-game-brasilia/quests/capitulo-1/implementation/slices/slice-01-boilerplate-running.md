# Slice 01 — Boilerplate Rodando

**Objetivo:** O projeto compila, `npm run dev` abre a tela preta com o texto "Zumbis de Brasilia" em branco. Nenhum erro no console.

---

## Entregaveis (arquivos novos/modificados)

```
zumbis-brasilia-game/
  package.json                         (root workspace)
  README.md
  apps/web/
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
    index.html
    public/_headers
    src/
      main.tsx
      App.tsx
      index.css
      components/
        PhaserGame.tsx
      game/
        PhaserGame.ts
        EventBus.ts
        config/
          GameConstants.ts
        scenes/
          BootScene.ts
          PreloadScene.ts
          MainMenuScene.ts        (esqueleto — so o titulo em texto)
          ModeSelectScene.ts      (esqueleto — so um texto "em breve")
          SettingsScene.ts        (esqueleto — so um texto "em breve")
```

Todos estes arquivos ja estao criados pelo Tech Lead em
`/Users/ricardo.ribeiro_1/Desktop/my-studies/zumbis-brasilia-game/`.
O trabalho do Slice 01 e executar `npm install` e confirmar que roda.

---

## Criterio de Pronto (testavel, binario)

- [ ] `cd zumbis-brasilia-game && npm install` roda sem erro
- [ ] `npm run dev` inicia o servidor em `http://localhost:5173`
- [ ] Browser abre e mostra canvas preto com o texto "ZUMBIS DE BRASILIA" e "Brasilia, 8 de jan de 2023. A nevoa subiu." em fonte monospace branca
- [ ] Console do browser: zero erros, zero warnings
- [ ] `npm run typecheck` passa sem erros
- [ ] Phaser inicia no modo AUTO (WebGL se disponivel, Canvas como fallback)
- [ ] `npm run build` gera `apps/web/dist/` sem erros

---

## Dependencias

- Nenhuma. Este e o ponto de partida.
- Requer: Node.js >= 22, npm >= 10

---

## Estimativa

**3 pomodoros** (25min cada):
1. npm install, corrigir eventuais conflitos de versao
2. Verificar que o Phaser inicializa, ajustar config se necessario
3. Typecheck + build limpo

---

## Spec Detalhada

### Passo 1: Instalar dependencias

```bash
cd /Users/ricardo.ribeiro_1/Desktop/my-studies/zumbis-brasilia-game
npm install
```

Se houver conflito de versao entre Phaser e React, verificar `apps/web/package.json`.
Phaser 3.88.x nao tem peerDep de React — nao deve conflitar.

### Passo 2: Iniciar em dev

```bash
npm run dev
```

Deve abrir `http://localhost:5173`. O Vite deve logar:
```
  VITE v5.x.x  ready in Xms
  ➜  Local:   http://localhost:5173/
  ➜  Network: http://192.168.x.x:5173/
```

### Passo 3: Verificar no browser

Abrir `http://localhost:5173` e confirmar:
1. Canvas preto (background `#0a0a0a`) ocupa toda a janela
2. Centralizado com `Phaser.Scale.FIT` e `CENTER_BOTH`
3. Textos visiveis: "ZUMBIS DE BRASILIA" e o subtitulo
4. Menu com 3 botoes: JOGAR, OPCOES, SAIR (em texto, sem sprites)
5. Botoes respondem ao hover (cor muda) e ao click (muda de scene)

### Passo 4: Verificar console

F12 > Console. Aceitar:
- `[Phaser v3.88.x] Jogo iniciado` (log normal do Phaser)
- Warnings de `[Deprecation]` do browser (nao do jogo)

Nao aceitar:
- `TypeError`, `ReferenceError`, `Cannot read properties of undefined`
- `404 Not Found` para arquivos `.ts` ou `.js`
- Qualquer erro vermelho

### Passo 5: Typecheck

```bash
npm run typecheck
```

Saida esperada: nenhuma linha de erro. Pode ter 0 linhas de output (sucesso silencioso).

### Passo 6: Build de producao

```bash
npm run build
```

Verificar:
- Pasta `apps/web/dist/` criada
- `dist/index.html` existe
- `dist/assets/phaser.[hash].js` existe (chunk separado do Phaser)
- `dist/assets/index.[hash].js` existe (codigo do jogo)
- Sem `ERROR` no output do build

---

## Possíveis problemas e solucoes

**Problema:** `Cannot find module 'phaser'`
**Solucao:** `npm install` nao rodou dentro de `apps/web/`. Verificar que o workspace resolveu corretamente: `ls apps/web/node_modules/phaser`

**Problema:** TypeScript erro em `PhaserGame.tsx` — `Phaser` nao e reconhecido como tipo
**Solucao:** Phaser nao tem tipos separados — os tipos estao no pacote principal. Verificar que `"phaser": "^3.88.0"` esta em `dependencies` (nao em `devDependencies`).

**Problema:** `Cross-Origin-Embedder-Policy` bloqueia recursos
**Solucao:** Esse header ja esta no `vite.config.ts` (secao `server.headers`). Se o browser reclamar mesmo assim, temporariamente remover o header de COEP do vite.config para desenvolvimento.

**Problema:** Canvas aparece pequeno ou esticado
**Solucao:** Verificar `index.css` — `html, body, #root` devem ter `width: 100%, height: 100%, overflow: hidden`. Verificar que o `Phaser.Scale.FIT` esta configurado no `PhaserGame.ts`.

---

## Checklist de Polish (nao e criterio de pronto, mas sinaliza qualidade)

- [ ] Cursor do mouse muda para `pointer` ao passar sobre os botoes
- [ ] Phaser roda em WebGL (verificar no console: "Renderer: WebGL")
- [ ] `image-rendering: pixelated` no CSS do canvas (verificar no DevTools)
- [ ] Titulo "Zumbis de Brasilia" tem stroke `#1A1A18` de 3px
- [ ] Versao "v0.1.0 - Quest 00" visivel no canto inferior esquerdo
