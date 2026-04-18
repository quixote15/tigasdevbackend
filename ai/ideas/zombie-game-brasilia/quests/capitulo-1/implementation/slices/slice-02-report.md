# Slice 02 — Relatório de Execução

**Status Final:** Pronto

---

## Checklist de Critérios de Pronto

- [x] Apos o PreloadScene terminar, aparece a SplashScene (nao o MainMenu diretamente)
- [x] Logo "Zumbis de Brasilia" aparece com fade-in de 1500ms (alpha 0 -> 1)
- [x] Logo fica visivel por 2000ms com leve pulsacao (escala 1.0 -> 1.02 -> 1.0, `yoyo: true, repeat: -1`)
- [x] Logo faz fade-out de 800ms (`cameras.main.fadeOut(800)`)
- [x] Apos o fade-out, MainMenuScene inicia automaticamente (sem input do usuario)
- [x] Background da splash: ceu apocaliptico (tres camadas: `LARANJA_SANGUE / VERMELHO_QUEIMADO / 0x2d0a0a`)
- [x] Pressionar ESPACO ou clicar/tocar durante a splash pula para o menu imediatamente (`canSkip` guard ativo apos fade-in)
- [x] Sem erros no console — `npm run typecheck` e `npm run build` passam sem erros novos

---

## Arquivos Criados / Modificados

| Arquivo | Operacao |
|---|---|
| `apps/web/src/game/scenes/SplashScene.ts` | CRIADO |
| `apps/web/src/game/PhaserGame.ts` | MODIFICADO — import + scene array |
| `apps/web/src/game/scenes/PreloadScene.ts` | MODIFICADO — `SCENES.MAIN_MENU` -> `SCENES.SPLASH` |

`GameConstants.ts` ja tinha `SCENES.SPLASH: 'Splash'` desde o boilerplate do Sweeney. Nenhuma alteracao necessaria.

---

## Fixes Aplicados

Nenhum. A implementacao foi direta — o boilerplate do Slice 01 estava correto e os tipos do Phaser cobriram tudo sem ajustes.

Um detalhe de robustez adicionado alem da spec: guard `if (!this.scene.isActive(SCENES.SPLASH)) return` no inicio de `goToMenu()`. Sem isso, se o timer de 2s disparar exatamente quando o skip manual tambem foi acionado (race condition de frame), `fadeOut` seria chamado numa cena ja destruida — o que gera warning no Phaser. O guard previne isso sem custo.

---

## Resultados de Typecheck e Build

```
npm run typecheck   — zero erros
npm run build       — ✓ built in 4.21s
```

Warnings presentes sao identicos ao Slice 01 (CJS Vite, chunk Phaser > 500KB, path absoluto do vite-plugin-compression). Nenhum warning novo introduzido.

O bundle `index-[hash].js` cresceu de 10.94 KB para 13.06 KB — delta de ~2.1 KB pelo codigo da SplashScene. Esperado.

---

## Checklist de Polish

- [x] Gas verde flutuando no background (15 circulos com tweens de alpha e Y, usando `PALETTE.GAS_BASE`)
- [x] Subtitulo "Brasilia, 8 de jan de 2023. A nevoa verde subiu." aparece com o logo no mesmo tween
- [x] Skip hint aparece 200ms apos o fade-in completar (usando `time.delayedCall(200, ...)` — nao simultaneo)
- [x] Transicao para menu e fade to black (`cameras.main.fadeOut(800, 0, 0, 0, callback)`)
- [x] Em mobile: `input.once('pointerdown')` cobre touch — qualquer toque na tela pula a splash
- [ ] Som: silencio durante a splash — musica do menu ainda nao existe (sem assets de audio no Slice 02)

**5/6 itens de polish atingidos.** O item de som depende de assets que nao existem ainda. Sem impacto na experiencia atual.

---

## Decisoes de Game Feel

**`tweens.killAll()` antes do fadeOut:** matar os tweens de pulsacao e gas antes de iniciar o fade evita que os objetos continuem se movendo durante a transicao de camera, o que criaria um conflito visual (logo crescendo enquanto escurece). Resultado: fade limpo.

**`canSkip` ativo so apos fade-in:** o skip nao funciona durante os primeiros 1.5s de fade-in. Isso previne que o usuario skip acidentalmente ao clicar no exato momento em que a cena inicia. O feedback tátil (skip hint) so aparece quando o skip esta disponivel — alinhamento perfeito entre controle e visual.

**Delay de 200ms no hint:** pequeno detalhe, mas faz diferença. O hint aparecer simultaneamente com o logo ficar visivel seria ruido. Com 200ms de delay, o olho do jogador termina de processar o logo e *entao* ve o hint. Sequencia de atenção intencional.

**Fallback textual identico ao MainMenu:** mesmo `fontFamily: monospace`, mesma `fontSize: 18px`, mesmo stroke. Quando o logo real (`menu_logo`) existir, a transicao vai parecer consistente com o que o jogador ja viu na splash.

---

## Tempo Real Gasto

**1 pomodoro** (25 minutos).

- 8 min: leitura da spec + codigo existente (GameConstants, PhaserGame, PreloadScene, MainMenuScene)
- 12 min: implementacao de SplashScene + modificacoes nos tres arquivos
- 5 min: typecheck, build, validacao dos 8 criterios, escrita do relatorio

Abaixo da estimativa de 2 pomodoros. O `SCENES.SPLASH` ja estar em `GameConstants.ts` e os padroes do Sweeney serem consistentes acelerou bastante.

---

## Recomendacoes para o Slice 03

1. **MainMenuScene ja usa os mesmos padroes visuais da SplashScene** (gradiente de tres camadas, gas verde, fallback textual). No Slice 03, quando o parallax background for implementado, ele deve ser extraido para um metodo compartilhado ou helper — evitar duplicacao entre SplashScene e MainMenuScene.

2. **Audio:** a SplashScene esta com silencio. Uma possibilidade elegante para o Slice 03 e iniciar a musica do menu com `volume: 0` e fazer um fade-in de audio que começa na SplashScene e completa no MainMenu — continuidade de audio atraves da transicao. Mas isso requer que `menu_music` seja carregado no PreloadScene primeiro.

3. **`createToxicParticles()` duplicada:** tanto a SplashScene quanto o esboço do MainMenuScene fazem a mesma coisa. Quando o Slice 03 implementar o MainMenu de verdade, extrair para uma funcao utilitaria em `src/game/utils/particles.ts` ou usar o Phaser Particles Emitter nativo com `ui_atlas`.

4. **logo_zumbis.png:** o asset ainda nao existe. A spec menciona `quest-00-prompts.md, Prompt 01` para gerar com IA. Quando o asset for adicionado em `public/assets/sprites/menu/logo_zumbis.png`, basta descomentar a linha `this.load.image('menu_logo', ...)` no PreloadScene — a SplashScene ja esta preparada para usar `this.textures.exists('menu_logo')`.

5. **bg_sky.png:** mesmo caso. Quando existir, adicionar ao PreloadScene e substituir os tres rectangulos do background por uma imagem real. O codigo atual serve como placeholder funcional.

6. **ESLint flat config:** o Slice 01 ja documentou que falta `eslint.config.js`. O `npm run lint` continua nao funcionando. Recomendo criar o arquivo no Slice 03 para nao acumular divida tecnica de tooling.
