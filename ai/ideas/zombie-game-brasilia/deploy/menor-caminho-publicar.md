# Menor Caminho Para Publicar Zumbis de Brasilia na Web
### Tim Sweeney — Deploy Guide | Abril 2026

---

## 1. Recomendacao Principal: Cloudflare Pages

Use **Cloudflare Pages**. Ponto final.

Voce ja conhece Netlify — tudo bem, ele funciona. Mas para um jogo com assets pesados (sprites, audio, spritesheets) a diferenca e material: a CDN da Cloudflare tem mais de 300 PoPs globais contra ~100 do Netlify, o free tier da Cloudflare nao tem limite de bandwidth (Netlify corta em 100 GB/mes), e o tempo de build e ligeiramente mais rapido para projetos Vite. Em moeda pratica: voce nao vai pagar nada ate escalar de verdade, e nao vai ter surpresa de "bandwidth exceeded" quando seu amigo postar o link no Twitter.

O setup e tao simples quanto Netlify — conecta o repo, define `npm run build` e `dist/`, e empurra. O CI/CD nativo ja cuida de tudo, incluindo preview deploys por PR. Zero GitHub Actions necessario para o deploy em si.

---

## 2. Comparativo Rapido

| Criterio | Cloudflare Pages | Netlify | Vercel | GitHub Pages | Surge.sh |
|---|---|---|---|---|---|
| Free tier bandwidth | **Ilimitado** | 100 GB/mes | 100 GB/mes | ~100 GB soft | 100 GB/mes |
| Build minutes free | 500/mes | 300/mes | 6.000/mes | via Actions | sem build |
| Velocidade de build (Vite) | Rapida | Rapida | Rapida | depende do runner | N/A |
| Global CDN | 300+ PoPs | ~100 PoPs | ~80 PoPs | GitHub infra | Cloudflare CDN |
| Assets grandes (sprites/audio) | Sem limite por arquivo | 25 MB por arquivo | 50 MB por arquivo | Sem limite | Sem limite |
| Preview deploys por PR | Sim, nativo | Sim, nativo | Sim, nativo | Nao (manual) | Nao |
| Dominio custom + HTTPS | Gratis | Gratis | Gratis | Gratis | Gratis |
| Headers customizados | Sim (`_headers`) | Sim (`netlify.toml`) | Sim (`vercel.json`) | Nao (sem config) | Nao |
| Complexidade de setup | Baixa | Baixa | Baixa | Media | Minima |
| Ideal para este projeto | **Sim** | Sim (mas bandwidth) | Sim (mas foco em Next.js) | Nao (sem preview) | Nao (sem preview) |

**Vercel** e excelente mas foi construido para Next.js. Funciona com Vite, mas a DX e levemente mais atritosa e o free tier tem limites similares ao Netlify. Se voce ja tivesse no ecossistema Vercel, ficaria. Nao esta.

**GitHub Pages** cai fora: nao tem preview deploys, nao tem headers customizados (problema sério para CORS de audio), e o deploy via Actions adiciona complexidade sem beneficio.

**Surge.sh** e para landing pages simples. Sem CI/CD nativo, sem preview deploys.

---

## 3. Passo-a-Passo: Do Zero ao "Meu Amigo Abre a URL e Joga"

### 3.1 Prep do Projeto (5 minutos)

O Vite precisa saber o base path. Se voce for usar o dominio padrao do Cloudflare Pages (`seu-projeto.pages.dev`), o base path e `/`. Se for usar subpath em algum momento, configure agora.

No `vite.config.ts`, confirme:

```ts
export default defineConfig({
  base: '/',          // correto para dominio raiz
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    // chunk splitting para separar Phaser do codigo do jogo
    rollupOptions: {
      output: {
        manualChunks: {
          phaser: ['phaser'],
        },
      },
    },
  },
})
```

O `manualChunks` e importante. Phaser tem ~1 MB minificado. Se voce nao separar, o browser baixa tudo junto em cada deploy novo. Com chunks separados, o Phaser fica em cache e so o seu codigo muda entre deploys.

Crie o arquivo `public/_headers` (headers servidos junto com os assets):

```
/*
  Cache-Control: public, max-age=0, must-revalidate

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/*.js
  Cross-Origin-Embedder-Policy: require-corp
  Cross-Origin-Opener-Policy: same-origin
```

A linha `Cross-Origin-Embedder-Policy` resolve o problema de `SharedArrayBuffer` que alguns recursos de audio do Phaser podem precisar. Na duvida, coloque desde o inicio.

### 3.2 Conectar o Repo ao Cloudflare Pages (3 minutos)

1. Acesse [pages.cloudflare.com](https://pages.cloudflare.com)
2. Clique em "Create a project" > "Connect to Git"
3. Autorize o GitHub, selecione o repo do jogo
4. Configure o build:
   - **Framework preset**: None (ou Vite, se aparecer)
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
   - **Root directory**: `/` (ou o subpath se for monorepo, ex: `game/`)
5. Clique em "Save and Deploy"

Pronto. O primeiro deploy ja roda. URL padrao: `https://seu-projeto.pages.dev`.

### 3.3 CI/CD — Voce Nao Precisa de GitHub Actions

O Cloudflare Pages detecta push na branch configurada (normalmente `main`) e dispara o build automaticamente. Cada PR gera um preview deploy com URL unica. Nao escreva GitHub Actions para deploy — e redundancia sem beneficio.

A unica razao para adicionar GitHub Actions e se voce quiser rodar testes antes do deploy:

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'
      - run: npm ci
      - run: npm run build        # garante que o build nao quebra
      - run: npm run lint         # se tiver ESLint configurado
      # o deploy em si e feito pelo Cloudflare Pages automaticamente
```

Esse workflow apenas valida o build. O deploy continua sendo responsabilidade do Cloudflare Pages.

### 3.4 Deploy Automatico em Push na Main

Configurado por padrao. Push na `main` dispara build e deploy em producao. Nao precisa fazer mais nada.

### 3.5 Preview Deploys em PRs

Tambem configurado por padrao. Cada PR recebe uma URL no formato `https://abc123.seu-projeto.pages.dev`. Voce pode mandar essa URL para um amigo testar antes de mergiar.

### 3.6 Dominio Custom

No painel do Cloudflare Pages:
1. Aba "Custom domains" > "Set up a custom domain"
2. Digite `zumbisdebrasilia.com.br` (ou o que for)
3. Se o dominio ja esta no Cloudflare DNS (recomendado): configuracao automatica
4. Se o dominio esta em outro registrador: adicione um CNAME apontando para `seu-projeto.pages.dev`

HTTPS e provisionado automaticamente. Tempo total: 2 minutos se o dominio ja esta no Cloudflare, ate 48h de propagacao DNS se estiver em outro registrador.

---

## 4. Gotchas Especificos de Jogo Phaser

### Assets Grandes (Sprites e Audio)

O Cloudflare Pages nao tem limite por arquivo no free tier. O limite e de 25 MB por arquivo no plano Workers, mas Pages e diferente — arquivos estaticos passam direto. Na pratica, spritesheets de 2-5 MB funcionam sem problema.

O que voce precisa fazer e controlar o **tamanho total do bundle de assets** para o tempo de carregamento inicial. Regras praticas:
- Spritesheets: comprima com oxipng ou pngquant. Uma spritesheet de personagem bem otimizada cai de 4 MB para 1.5 MB sem perda visual perceptivel.
- Audio: use `.ogg` como formato primario (menor que MP3 para a mesma qualidade), `.mp3` como fallback. Phaser aceita array de formatos: `this.load.audio('trilha', ['trilha.ogg', 'trilha.mp3'])`.
- Lazy loading: nao carregue assets de fases futuras na BootScene. Carregue na transicao para cada fase.

### Cache de Browser (Jogo Atualiza mas Cliente Fica no Antigo)

Esse problema e resolvido pelo Vite + o `_headers` que configuramos. O Vite coloca hash no nome dos arquivos de assets (`assets/phaser.a3b2c1d4.js`). Quando voce faz um novo deploy, o hash muda. O browser baixa o arquivo novo.

O `index.html` tem `Cache-Control: no-cache` (pelo header `/*` no `_headers`), entao o browser sempre busca a versao mais recente do HTML, que por sua vez referencia os novos hashes. Ciclo fechado.

Se mesmo assim um usuario reclamar que esta no cache antigo: `Ctrl+Shift+R` (hard reload). Nao vale a pena implementar Service Worker para invalidacao nesta fase.

### CORS em Audio

O Phaser usa `Web Audio API` para tocar sons. O browser pode bloquear audio de cross-origin se o servidor nao servir os headers corretos.

Como os assets ficam no mesmo dominio (servidos pelo Cloudflare Pages junto com o jogo), isso nao e problema na producao. O `_headers` que criamos ja cobre.

O problema aparece em desenvolvimento local se voce tentar carregar assets de outro servidor. Nao faca isso. Deixe tudo em `public/assets/` e sirva via `npm run dev`.

Se voce precisar de `AudioContext` com `SharedArrayBuffer` (para audio multi-thread), os headers `Cross-Origin-Embedder-Policy` e `Cross-Origin-Opener-Policy` que colocamos no `_headers` resolvem.

### Build Size (Phaser ja e ~1 MB)

Com `manualChunks: { phaser: ['phaser'] }` no Vite, o resultado do build vai ser:
- `assets/phaser.[hash].js`: ~960 KB minificado (~300 KB gzipped — a CDN serve gzip automaticamente)
- `assets/index.[hash].js`: o codigo do seu jogo, tipicamente 50-200 KB
- HTML, CSS, assets estaticos: separados

O que o usuario baixa na primeira visita: ~300 KB (Phaser gzipped) + seu codigo + assets. Nas visitas seguintes, Phaser fica em cache. So o codigo do jogo e redownloadado quando voce faz deploy.

Para referencia: Fortnite no browser (se existisse) baixaria 50 MB. Voce esta em boa forma.

---

## 5. Checklist "Pronto Para Mostrar Pro Amigo"

- [ ] `npm run build` roda sem erros localmente e gera a pasta `dist/`
- [ ] `npx serve dist` (ou `vite preview`) abre o jogo no browser sem erros no console
- [ ] Arquivo `public/_headers` criado com regras de cache e CORS
- [ ] `vite.config.ts` tem `base: '/'` e `manualChunks` para Phaser
- [ ] Cloudflare Pages conectado ao repo e primeiro deploy concluido com sucesso
- [ ] URL `https://seu-projeto.pages.dev` abre o jogo em dispositivo movel (teste real no celular)
- [ ] Audio funciona no celular (iOS exige gesto do usuario antes de tocar audio — implemente `this.sound.unlock()` na BootScene)
- [ ] Score final esta sendo registrado no `localStorage` (highscore persiste entre sessoes)
- [ ] GA4 esta disparando eventos (`npm run build` + abrir em producao + verificar no GA4 Realtime)
- [ ] Botao de share na tela de Game Over gera URL correta (sem `localhost` hardcoded)

---

## 6. Quando Migrar

**Ate 10.000 usuarios/mes**: Cloudflare Pages free tier aguenta sem piscar. Bandwidth ilimitada, 500 builds/mes sao suficientes para um dev solo.

**Entre 10.000 e 100.000 usuarios/mes**: ainda no free tier, mas monitore o tempo de build. Se voce adicionar backend (leaderboard, auth), a decisao muda.

**Acima de 100.000 usuarios/mes ou quando adicionar backend**: avalie **Cloudflare Workers + Pages** para uma arquitetura edge. O frontend continua no Pages. A logica de backend vai para Workers (leaderboard serverless, por exemplo). Voce fica no ecossistema Cloudflare e nao precisa migrar o CDN.

Se em algum momento voce precisar de um servidor real (matchmaking, WebSockets persistentes), olhe para **Railway** ou **Fly.io** para o backend — mas o frontend estatico continua no Cloudflare Pages. Nao misture os dois na mesma plataforma so porque da.

A migracao para fora do Cloudflare Pages so faz sentido se voce precisar de features que Pages nao tem (ex: SSR com framework especifico, banco de dados embarcado). Para jogo client-side puro, Pages resolve ate escala de produto real.

---

## Resumo Executivo

```
1. vite.config.ts → base: '/', manualChunks para Phaser
2. public/_headers → cache + CORS headers
3. pages.cloudflare.com → conecta repo → build: "npm run build", out: "dist"
4. Push na main → deploy automatico
5. PR aberto → preview deploy com URL unica
6. Dominio custom → 2 minutos no painel
```

Tempo total do zero ao link funcionando: **15 minutos**. O jogo vai antes de voce terminar de ler este documento.
