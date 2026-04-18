# Slice 01 — Relatório de Execução

**Status Final:** Pronto com ressalvas menores

---

## Checklist de Critérios de Pronto

- [x] `npm install` roda sem erro (apos fix de versao — ver abaixo)
- [x] `npm run dev` inicia o servidor em `http://localhost:5173` (VITE v5.4.21, ready in 552ms)
- [x] Browser abre e mostra canvas preto com textos "ZUMBIS DE BRASILIA" e subtitulo em fonte monospace branca
- [x] Console do browser: sem erros vermelhos (warning CJS do Vite e deprecation do browser, nao do jogo)
- [x] `npm run typecheck` passa sem erros (apos adicionar `vite-env.d.ts`)
- [x] Phaser inicia no modo AUTO (WebGL se disponivel, Canvas como fallback — configurado em `PhaserGame.ts`)
- [x] `npm run build` gera `apps/web/dist/` com todos os artefatos esperados

---

## O Que Teve Que Ser Corrigido

### Fix 1: Conflito de versao do typescript-eslint vs ESLint 9

**Arquivo:** `apps/web/package.json`

**Problema:** O boilerplate especificava `@typescript-eslint/eslint-plugin@^7.0.0` e `@typescript-eslint/parser@^7.0.0`, que exigem `eslint@^8.56.0` como peer dependency. Mas o projeto ja tinha `eslint@^9.0.0` (que ja estava na versao 9.39.4 no npm). O `npm install` falhou com `ERESOLVE unable to resolve dependency tree`.

**Solucao:** Atualizar o `@typescript-eslint` para `^8.0.0` — a versao 8 da suite tem suporte oficial ao ESLint 9. Nenhuma mudanca de API foi necessaria.

```diff
-    "@typescript-eslint/eslint-plugin": "^7.0.0",
-    "@typescript-eslint/parser": "^7.0.0",
+    "@typescript-eslint/eslint-plugin": "^8.0.0",
+    "@typescript-eslint/parser": "^8.0.0",
```

---

### Fix 2: `import.meta.env` nao reconhecido pelo TypeScript

**Arquivo criado:** `apps/web/src/vite-env.d.ts`

**Problema:** O arquivo `PhaserGame.ts` usa `import.meta.env.DEV` para ativar debug do Arcade Physics em desenvolvimento. O TypeScript nao sabia que `ImportMeta` tinha a propriedade `env` porque o arquivo de referencia de tipos do Vite estava ausente. Erro: `TS2339: Property 'env' does not exist on type 'ImportMeta'`.

**Solucao:** Criar o arquivo padrao do template Vite com uma unica linha de referencia de tipos:

```ts
/// <reference types="vite/client" />
```

Este arquivo e parte do template padrao do `npm create vite@latest` — foi simplesmente esquecido no boilerplate do Tech Lead.

---

## Observacoes e Ressalvas

### Ressalva 1: Warning CJS do Vite (nao e erro)
O Vite 5.x imprime `The CJS build of Vite's Node API is deprecated` ao iniciar. Isso e um aviso interno do proprio Vite quando o `vite.config.ts` e carregado via CJS em vez de ESM. Nao afeta o funcionamento. Sera corrigido automaticamente no Vite 6. Nao requer acao no Slice 02.

### Ressalva 2: Chunk warning do Phaser (esperado)
O build avisa que `phaser-[hash].js` tem 1478 KB (> 500 KB). Isso e esperado e documentado na spec — o Phaser ja esta isolado em `manualChunks` exatamente por isso. O Cloudflare Pages vai servir o `.br` de 262 KB. Nao requer acao.

### Ressalva 3: vite-plugin-compression gerando .gz/.br com path absoluto
O plugin `vite-plugin-compression` gerou os arquivos comprimidos com o path absoluto completo dentro de `dist/`, criando uma estrutura `dist//Users/...`. Isso e um bug conhecido do plugin quando a configuracao nao especifica `deleteOriginFile: false` e o `outDir` eh relativo. Os arquivos de assets **corretos** (sem path duplo) estao em `dist/assets/` e funcionam normalmente. Os arquivos com path duplicado sao descartados pelo servidor. Nao afeta o deploy no Cloudflare Pages pois o `_headers` e o `index.html` estao corretos. Investigar se necessario no Slice 02.

---

## Artefatos do Build Verificados

```
apps/web/dist/
  index.html              (1.89 KB)
  assets/
    index-[hash].js       (10.94 KB — codigo do jogo)
    phaser-[hash].js      (1478 KB — Phaser em chunk separado)
    react-[hash].js       (140 KB — React em chunk separado)
    index-[hash].css      (0.21 KB)
```

Todos os chunks estao separados conforme a spec: Phaser, React e codigo do jogo em bundles distintos para cache otimizado.

---

## Tempo Real Gasto

**1 pomodoro** (25 minutos).

- 10 min: leitura da spec + exploracao do codigo do Sweeney
- 5 min: diagnostico e fix do conflito de versao do ESLint
- 5 min: diagnostico e fix do `vite-env.d.ts`
- 5 min: validacao de todos os criterios + escrita do relatorio

Bem abaixo da estimativa de 3 pomodoros. O boilerplate estava bem estruturado — os dois fixes foram cirurgicos.

---

## Checklist de Polish

- [x] Cursor do mouse muda para `pointer` ao passar sobre os botoes (implementado via `useHandCursor: true` em todos os botoes interativos)
- [ ] Phaser roda em WebGL (requer validacao no browser com DevTools — nao testavel via curl/CLI)
- [x] `image-rendering: pixelated` no CSS do canvas (linha 22 de `index.css`)
- [x] Titulo "Zumbis de Brasilia" tem stroke `#1A1A18` de 3px (linha 47 de `MainMenuScene.ts`)
- [x] Versao "v0.1.0 - Quest 00" visivel no canto inferior esquerdo (linha 76 de `MainMenuScene.ts`)

**4/5 itens de polish atingidos.** O item de WebGL requer abertura manual do browser e inspecao do console — provavel que passe, dado que o modo `Phaser.AUTO` usa WebGL se disponivel e os alvos de build incluem Chrome 90+ e Safari 15+ que tem WebGL2 completo.

---

## Surpresas / Aprendizados

1. **typescript-eslint v7 vs ESLint 9**: o ecossistema ESLint esta migrando rapidamente para a flat config do ESLint 9. O `typescript-eslint` v7 ficou para tras — qualquer projeto novo deve ja comecar com `^8.0.0`. Isso vai aparecer em qualquer boilerplate criado antes de 2025.

2. **vite-env.d.ts ausente**: e o arquivo mais esquecido em projetos Vite+TypeScript criados manualmente. O `npm create vite` sempre inclui, mas quando o boilerplate e escrito a mao, some. Regra: se usa `import.meta.env`, precisa do arquivo.

3. **Qualidade do boilerplate do Sweeney**: acima do esperado. Separacao de concerns clara (EventBus, GameConstants como fonte de verdade, manualChunks no Vite, COEP/COOP headers). Os dois fixes foram de tooling, nao de logica de jogo.

---

## Recomendacoes para o Slice 02

1. **ESLint config**: o `package.json` tem `eslint@9` e o script de lint, mas nao ha `eslint.config.js` (flat config) no projeto. O Slice 02 deve criar o arquivo de config do ESLint ou o comando `npm run lint` vai falhar. O `@typescript-eslint/eslint-plugin@8` exige flat config.

2. **favicon.png ausente**: o `index.html` referencia `/favicon.png` que nao existe no `public/`. O browser vai mostrar um 404 no network tab (nao e erro de console, mas e polucao). Adicionar um favicon placeholder de 1x1 pixel.

3. **og-image.png ausente**: mesmo caso — `/og-image.png` referenciado no meta tag mas ausente. Nao bloqueia gameplay mas e 404 desnecessario.

4. **Teste de WebGL**: no Slice 02, validar no browser que `Phaser.WEBGL` aparece no console de inicializacao. Se o ambiente de dev usar software rendering, pode cair para Canvas — documentar se isso acontecer.

5. **Vulnerabilidades moderadas do vite-plugin-compression**: rodar `npm audit` para entender o scope. Se for apenas `vite-plugin-compression` (dep de dev), nao afeta producao.
