# ZUMBIS DE BRASILIA — Tech Strategy: MVP Web
### Arquitetura, stack e plano de execucao para browser game em 2 semanas

**Documento de Estrategia Tecnica Revisada | Abril 2026**
**Visao: John Carmack | CTO & Arquitetura de Engenharia**

---

> *"Vampire Survivors foi feito com Phaser por um cara desempregado que gastou 1.100 libras. Rodou no browser. Virou um dos jogos mais lucrativos da decada. A tecnologia nunca foi o gargalo. O gargalo e entregar algo que as pessoas querem jogar. Nosso trabalho e nao atrapalhar."*

---

## 0. Contexto da Mudanca

Li o documento do CEO. Li a proposta do Andre Guedes. Li minha propria tech strategy anterior. Vou ser direto: **meu documento anterior esta 80% obsoleto.** Godot, Firebase, AdMob mobile, CI/CD com Codemagic, pipeline de APK -- tudo isso vai pro lixo.

O pivot e radical e correto. O CEO tomou a decisao certa. Meu trabalho agora e redefinir a stack tecnica para uma realidade completamente diferente:

| Antes | Agora |
|---|---|
| Godot 4.4 + GDScript | HTML5 + JavaScript/TypeScript |
| Mobile nativo (APK/IPA) | Browser game (URL) |
| Firebase backend | Zero backend |
| 5 pessoas, 6 meses | 1-2 devs, 2 semanas |
| R$ 2,5M | R$ 30-50K |
| App Store/Google Play | Link compartilhavel |

O principio nao muda: **simplicidade radical, ship first, otimizar para o pior caso.** So que agora o "pior caso" nao e um Galaxy A06 rodando um APK Godot -- e o Chrome do Galaxy A06 rodando JavaScript.

Vamos.

---

## 1. Framework/Engine — A Decisao Final

### O Veredito: Phaser 3.88+ (estavel)

**Phaser 3. Sem discussao.**

Dois dias atras (10 de abril de 2026), a Phaser lançou o **v4.0.0 "Caladan"** -- rewrite completo do renderer WebGL, arquitetura nova de render nodes, SpriteGPULayer que renderiza 1 milhao de sprites num unico draw call. Impressionante. E eu **nao vou usar**.

Por que? Porque Phaser 4 tem **2 dias de vida em producao**. E nos temos **2 semanas para entregar um jogo**. Nao existe cenario onde usar um framework recem-lancado num projeto com deadline apertado e uma decisao racional. Phaser 3.88 tem 8 anos de battle-testing, milhares de jogos em producao, documentacao madura, e uma comunidade que ja resolveu todo bug que voce vai encontrar.

### Comparativo Tecnico (Abril 2026)

| Criterio | Phaser 3.88 | PixiJS 8.x | Kaplay | Canvas Puro |
|---|---|---|---|---|
| **Tipo** | Game framework completo | Rendering library | Game library | API nativa |
| **Inclui fisica** | SIM (Arcade + Matter.js) | NAO | SIM (basica) | NAO |
| **Inclui audio** | SIM (Web Audio API wrapper) | NAO | SIM | NAO |
| **Inclui input (touch/teclado)** | SIM | NAO | SIM | NAO |
| **Inclui scene management** | SIM | NAO | NAO | NAO |
| **Inclui sprite sheets/atlas** | SIM | SIM | SIM | Manual |
| **Inclui tweens/particulas** | SIM | Parcial (via plugins) | SIM | NAO |
| **Inclui camera system** | SIM | NAO | SIM | NAO |
| **Tamanho minificado** | ~1.2 MB | ~450 KB | ~300 KB | 0 KB |
| **Performance (sprites)** | 15K+ sprites a 60fps (mobile) | 20K+ sprites a 60fps | Inferior ao Phaser | Depende da implementacao |
| **Renderer** | WebGL + Canvas fallback | WebGL (primario) | WebGL + Canvas | Canvas |
| **Maturidade** | 8+ anos, milhares de jogos | 10+ anos, foco em rendering | 1-2 anos (fork do Kaboom) | Eterna |
| **Documentacao** | Excelente, exemplos extensivos | Boa | Em crescimento | MDN |
| **Comunidade** | Massiva (47K stars GitHub) | Grande (44K stars) | Pequena (~4K stars) | N/A |
| **Vampire Survivors** | **SIM — foi feito com Phaser** | NAO | NAO | NAO |

### Por que Phaser 3 e nao PixiJS

PixiJS e um renderer. Nao e um game framework. Se eu usar PixiJS, vou precisar implementar: sistema de fisica, sistema de audio, input handling, scene management, camera system, sprite sheet parser, tween system, particle system. Isso e **2 semanas de trabalho so em infraestrutura** antes de escrever uma linha de gameplay.

Phaser te da tudo isso pronto. E o Luca Galante provou que funciona — Vampire Survivors, o jogo que LITERALMENTE inspirou o design do nosso jogo, foi feito com Phaser. Nao existe argumento mais forte que esse.

### Por que Phaser 3 e nao Kaplay

Kaplay e interessante para prototipos e game jams. Mas uma review comparativa de fevereiro de 2026 e clara: *"KAPLAY e o mais facil de aprender mas o menos escalavel dos 3 frameworks testados"* e *"a performance do KAPLAY nao chega nem perto da oferecida pelo Phaser."* Para um jogo com 100-200 entidades em tela com fisica, particulas e audio simultaneo, Kaplay nao tem a maturidade necessaria. Num deadline de 2 semanas, nao posso arriscar encontrar um bug de performance que ninguem na comunidade (4K stars) ja resolveu.

### Por que Phaser 3 e nao Canvas Puro

Porque nao estamos em 1993. Eu nao escrevi meu proprio software renderer para Doom porque era divertido — escrevi porque nao existia alternativa. Em 2026, a alternativa existe, tem 8 anos de maturidade, e e gratis. Reinventar a roda e vaidade de engenheiro.

### Performance Real: Phaser 3 em Mobile

O Phaser 3.60+ introduziu melhorias significativas de mobile performance. Num iPhone SE, o v3.24 renderizava 5.248 texture binds a 60fps; o 3.60 saltou para 15.104 — quase 3x mais. O Arcade Physics mantém 60fps com ate 200 corpos ativos em mobile.

Para nosso jogo — maximo de ~150 entidades em tela (zumbis + projeteis + power-ups + particulas) — Phaser 3 tem headroom de sobra. O Galaxy A06 com Helio G85 e Mali-G52 suporta WebGL 2.0 e roda Chrome com aceleracao de hardware. Nao vai ser o problema.

**Decisao final: Phaser 3.88.x. Estavel, testado, documentado, e literalmente a engine do Vampire Survivors original.**

---

## 2. Arquitetura do MVP — Tudo Client-Side

### Principio: ZERO Backend

O CEO foi claro: sem backend, sem Firebase, sem servidor. Concordo 100%. Para o MVP, qualquer backend e complexidade gratuita. O jogo e single-player, offline-capable, e toda a logica roda no browser.

### Diagrama de Arquitetura

```
┌────────────────────────────────────────────────────────────────────┐
│                    BROWSER (Chrome/Safari/Firefox)                  │
│                                                                    │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                      PHASER 3.88                             │  │
│  │                                                              │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐   │  │
│  │  │  Game Loop    │  │  Scene Mgr   │  │  Input Handler  │   │  │
│  │  │  (60fps)      │  │  (Menu,Game, │  │  (Touch+Keys)   │   │  │
│  │  │              │  │   GameOver)  │  │                 │   │  │
│  │  └──────┬───────┘  └──────┬───────┘  └────────┬────────┘   │  │
│  │         │                 │                    │            │  │
│  │  ┌──────┴─────────────────┴────────────────────┴────────┐   │  │
│  │  │                 GAMEPLAY SYSTEMS                      │   │  │
│  │  │  ┌──────────┐ ┌───────────┐ ┌──────────┐ ┌────────┐ │   │  │
│  │  │  │ Player   │ │ Wave      │ │ Combat   │ │ Score  │ │   │  │
│  │  │  │ Movement │ │ Spawner   │ │ System   │ │ /Combo │ │   │  │
│  │  │  └──────────┘ └───────────┘ └──────────┘ └────────┘ │   │  │
│  │  │  ┌──────────┐ ┌───────────┐ ┌──────────┐           │   │  │
│  │  │  │ PowerUp  │ │ Enemy AI  │ │ Object   │           │   │  │
│  │  │  │ Manager  │ │ (State M.)│ │ Pooling  │           │   │  │
│  │  │  └──────────┘ └───────────┘ └──────────┘           │   │  │
│  │  └────────────────────────────────────────────────────┘   │  │
│  │                                                              │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────────┐   │  │
│  │  │ Arcade      │  │ Web Audio   │  │ WebGL Renderer   │   │  │
│  │  │ Physics     │  │ (SFX+Music) │  │ (Canvas fallback)│   │  │
│  │  └─────────────┘  └─────────────┘  └──────────────────┘   │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐    │
│  │ localStorage  │  │ Web Share    │  │ Canvas-to-PNG        │    │
│  │ (high score,  │  │ API          │  │ (card compartilhavel)│    │
│  │  settings)    │  │ (share score)│  │                      │    │
│  └──────────────┘  └──────────────┘  └──────────────────────┘    │
│                                                                    │
│  ┌──────────────┐  ┌──────────────────────────────────────────┐  │
│  │ GA4 / gtag   │  │ Google H5 Ad Placement API              │  │
│  │ (analytics)  │  │ (interstitial + rewarded)                │  │
│  └──────────────┘  └──────────────────────────────────────────┘  │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
         │                    │                    │
         │ HTTPS              │ HTTPS              │ HTTPS
         v                    v                    v
┌──────────────┐   ┌──────────────┐   ┌──────────────────────┐
│ Cloudflare   │   │ Google       │   │ Google AdSense       │
│ Pages (CDN)  │   │ Analytics    │   │ H5 Games Ads         │
│ (hosting)    │   │ (metricas)   │   │ (monetizacao)        │
└──────────────┘   └──────────────┘   └──────────────────────┘
```

### Data Flow — Sessao de Jogo

```
Jogador clica no link (congressodosmortos.com.br)
    │
    v
[1] Cloudflare Pages serve HTML + JS + assets (~3-5 MB total)
    │
    v
[2] Service Worker cacheia tudo (proxima vez: instantaneo)
    │
    v
[3] Tela inicial: escolhe tom de pele (1 toque)
    │
    v
[4] Phaser inicia: Game Loop a 60fps
    │   - ZERO chamadas de rede durante gameplay
    │   - Toda logica e local
    │   - Object pooling: zero alocacoes
    │
    v
[5] 3 minutos de gameplay (6 waves)
    │
    v
[6] Game Over
    ├── Score salvo em localStorage
    ├── GA4 envia evento (score, wave_reached, zombies_killed, titulo)
    ├── Card de resultado gerado via Canvas-to-PNG
    ├── Botao COMPARTILHAR: Web Share API (WhatsApp, Twitter, etc.)
    └── Botao JOGAR DE NOVO: volta para [4]
    │
    v
[7] Entre partidas (a cada 3 jogos):
    └── Google H5 Ad Placement API mostra interstitial
```

### Decisoes Chave

| Decisao | Escolha | Justificativa |
|---|---|---|
| Backend | **Nenhum** | Single-player, sem leaderboard global no MVP, zero complexidade |
| Persistencia | **localStorage** | High score, melhor titulo, preferencia de skin. 5 KB no maximo |
| Rendering | **WebGL (Phaser auto-detect)** | WebGL se disponivel, Canvas fallback automatico |
| Fisica | **Arcade Physics (Phaser)** | Simples, rapida, suficiente para colisao AABB |
| Audio | **Web Audio API (via Phaser)** | Nativo do browser, zero dependencia |
| Compartilhamento | **Web Share API + Canvas** | Nativo do browser. Gera imagem + texto, compartilha via OS |
| State management | **Scene-based (Phaser)** | BootScene, MenuScene, GameScene, GameOverScene |
| Leaderboard global | **NAO no MVP** | Vem na v1.2 (semana 3) se metricas justificarem. Supabase ou Firebase serverless |

---

## 3. Stack Completo

### Tabela de Stack

| Camada | Tecnologia | Versao | Justificativa |
|---|---|---|---|
| **Framework de jogo** | Phaser | 3.88.x | Engine do Vampire Survivors. Melhor framework 2D web, 8 anos de maturidade |
| **Linguagem** | TypeScript | 5.x | Type safety sem overhead de runtime. Phaser tem tipagens TS excelentes |
| **Bundler** | Vite | 8.x (Rolldown) | Build de producao em <6s. HMR instantaneo em dev. Suporte nativo a TS |
| **Package manager** | pnpm | 10.x | Mais rapido que npm, dedup nativo, disk-efficient |
| **Hosting** | Cloudflare Pages | Free tier | Bandwidth ilimitado gratis. CDN global. Deploy via Git push |
| **CDN** | Cloudflare (embutido) | - | PoPs em Sao Paulo e Rio. Latencia <30ms no Brasil |
| **DNS** | Cloudflare | Free | Junto com Pages, zero config adicional |
| **Dominio** | congressodosmortos.com.br | - | Registro.br, ~R$ 40/ano |
| **Analytics** | Google Analytics 4 (gtag.js) | - | Gratis. Eventos customizados client-side. Funil, retencao, demographics |
| **Analytics (game-specific)** | GameAnalytics | Free tier | Especializado em games. Sessao media, retencao D1/D7, funil de waves |
| **Ads** | Google AdSense H5 Games Ads | Ad Placement API | Interstitial + rewarded. API dedicada para jogos HTML5 |
| **Compartilhamento** | Web Share API (nativo) | - | Zero dependencia. Suporte em Chrome, Safari, Edge (67% compat.) |
| **Card de resultado** | Canvas API (nativo) | - | Gera PNG do card de Game Over direto no browser |
| **PWA / Offline** | Service Worker (Workbox) | - | Pre-cache de assets. Jogo funciona offline apos primeiro load |
| **Controle de versao** | Git + GitHub | - | CI/CD integrado com Cloudflare Pages |
| **CI/CD** | Cloudflare Pages (auto) | - | Push na main = deploy em producao em <60 segundos |
| **Linting** | ESLint + Prettier | - | Consistencia de codigo com zero esforco |
| **Sprites** | Aseprite (producao) + TexturePacker (atlas) | - | Artista cria em Aseprite, dev empacota em atlas otimizado |
| **Audio** | Audacity/FMOD (producao) | - | Freelancer entrega OGG + MP3. Dois formatos = 100% compatibilidade |
| **Design** | Figma | - | UI mockups, card de Game Over |
| **Comunicacao** | Discord ou WhatsApp | - | 2-3 pessoas, nao precisa de Jira |

### Custo Total de Infra

| Item | Custo Mensal | Custo Anual |
|---|---|---|
| Cloudflare Pages (hosting) | **R$ 0** | **R$ 0** |
| Cloudflare CDN | **R$ 0** | **R$ 0** |
| Google Analytics 4 | **R$ 0** | **R$ 0** |
| GameAnalytics | **R$ 0** (free tier) | **R$ 0** |
| Google AdSense H5 (gera receita, nao custo) | **R$ 0** | **R$ 0** |
| Dominio (congressodosmortos.com.br) | ~R$ 3 | ~R$ 40 |
| GitHub (free tier) | **R$ 0** | **R$ 0** |
| SSL/TLS (Cloudflare) | **R$ 0** | **R$ 0** |
| **TOTAL** | **~R$ 3/mes** | **~R$ 40/ano** |

Leu certo. **Quarenta reais por ano.** Bandwidth ilimitado. CDN global. SSL gratis. Deploy automatico. O custo de infraestrutura e tao proximo de zero que arredonda para zero.

Compare com o documento anterior: Firebase custaria R$ 60-21.000/mes dependendo do tier. Codemagic R$ 275-550/mes. Agora o custo caiu **99,95%**. Essa e a beleza de um jogo 100% client-side com hosting estatico.

---

## 4. Performance em Mobile Browser

### O Problema Real

O target device e o Samsung Galaxy A06: Helio G85, Mali-G52, 4GB RAM, tela 720x1600, rodando Chrome Android. O jogo precisa rodar a 60fps nesse hardware dentro do browser.

Isso e factivel. Mas nao e trivial. JavaScript no browser e 2-5x mais lento que codigo nativo. O overhead do browser (compositor, GC, event loop) come CPU e memoria. O WebGL no Android ainda tem quirks. Aqui esta como garantimos performance.

### Budgets de Performance (Mobile Browser)

| Recurso | Budget MVP | Justificativa |
|---|---|---|
| **RAM total do jogo** | <150 MB | Chrome Android reserva ~200-300 MB por tab. Precisamos de margem |
| **RAM de texturas** | <40 MB | Atlas comprimidos, sprites pequenos (96x96 max) |
| **RAM de audio** | <10 MB | Loops em OGG compressed. SFX curtos em memoria |
| **Tamanho total de assets** | <3 MB (comprimido) | Para load rapido em 4G. <5 MB descomprimido |
| **Tamanho do bundle JS** | <500 KB (gzipped) | Phaser minificado (~350 KB gzip) + game code (~100-150 KB) |
| **Entidades em tela (max)** | 150 | Zumbis + projeteis + power-ups + particulas |
| **Draw calls por frame** | <20 | Texture atlas = 1 draw call por atlas. 3-4 atlas max |
| **FPS target** | 60 fps | requestAnimationFrame |
| **FPS minimo aceitavel** | 45 fps | Abaixo disso: reduzir particulas automaticamente |
| **Tempo de first load** | <3 segundos (4G) | Assets comprimidos + CDN Brasil |
| **Tempo de load subsequente** | <1 segundo | Service Worker cache |

### Estrategias de Otimizacao (Checklist)

**1. Object Pooling — A otimizacao #1**
Toda entidade que spawna e morre (zumbis, projeteis, particulas, power-ups, textos de dano) usa pool pre-alocado. Zero `new` durante gameplay. Zero pressao no garbage collector. Isso sozinho e responsavel por 50% da performance estavel.

```
// Pool de zumbis: pre-aloca 100, reusa
zombiePool = this.add.group({
    classType: Zombie,
    maxSize: 100,
    runChildUpdate: true
});
```

**2. Texture Atlas — Sprites em um unico atlas**
Todos os sprites de uma categoria empacotados num unico PNG via TexturePacker. Resultado: 1 draw call para todos os zumbis, 1 para o jogador, 1 para UI. Total: ~3-5 draw calls em vez de ~200.

**3. Arcade Physics, nao Matter.js**
Arcade Physics do Phaser usa AABB (Axis-Aligned Bounding Box) — retangulos. E O(n) para colisao. Matter.js usa formas complexas e SAT — 5-10x mais lento. Para nosso jogo, AABB e mais que suficiente. Zumbi e retangulo. Jogador e retangulo. Projetil e retangulo. Pronto.

**4. Visibilidade culling**
Zumbis fora da camera nao sao renderizados. Phaser faz isso automaticamente com camera bounds, mas precisamos tambem desativar o `update()` de entidades fora de tela para economizar CPU.

**5. Sprite sheet animations em 12fps, nao 60fps**
O estilo visual e cartoon tosco (no bom sentido). Animacoes de 6-8 frames rodando a 12fps ficam charmosas e economizam 80% da memoria comparado a 60fps. Nao e limitacao — e escolha artistica que alinha com performance.

**6. Audio: OGG + MP3 dual format**
Chrome Android aceita OGG (melhor compressao). Safari precisa de MP3. Entregar ambos. Phaser seleciona automaticamente. Loops de musica em streaming (nao carrega inteiro na RAM).

**7. Dynamic quality scaling**
Na inicializacao, medir FPS por 2 segundos. Se < 50fps:
- Reduzir particulas em 50%
- Desativar screen shake
- Reduzir max zumbis simultaneos de 100 para 60
- Usar Canvas renderer em vez de WebGL (fallback automatico do Phaser)

**8. Resolucao fixa: 720x1280**
Nao renderizar na resolucao nativa do device. Fixar o game canvas em 720x1280 (portrait) ou 1280x720 (landscape). CSS scale para preencher a tela. Isso reduz o numero de pixels renderizados em devices Full HD em 55%.

**9. Evitar CSS transforms no game canvas**
O canvas do Phaser deve ser o unico elemento na viewport durante gameplay. Sem overlays de HTML. Sem divs animadas. Sem blur de CSS. Tudo que e visual acontece DENTRO do canvas.

**10. requestAnimationFrame, nao setInterval**
Phaser ja usa rAF por padrao. Mas e importante nao ter NADA fora do game loop usando timers. Todo efeito de delay usa os timers internos do Phaser.

### Teste de Validacao (Dia 1)

Antes de escrever qualquer gameplay, o primeiro commit deve ser:
- Phaser inicializado
- 200 sprites animados em tela, movendo-se aleatoriamente
- Arcade Physics com colisao entre eles
- 1 loop de audio tocando
- Rodar no Chrome do Galaxy A06

**Se nao atingir 55+ fps: parar tudo e diagnosticar.** Se atingir (vai atingir): seguir em frente com confianca.

---

## 5. Hosting e Deploy

### Cloudflare Pages — A Escolha

| Criterio | Cloudflare Pages | Vercel | Netlify | itch.io |
|---|---|---|---|---|
| **Bandwidth (free)** | **Ilimitado** | 100 GB/mes | 100 GB/mes | Ilimitado |
| **Build minutes (free)** | 500/mes | 6.000/mes | 300/mes | N/A |
| **Deploys (free)** | 500/mes | Ilimitado | Ilimitado | Manual |
| **CDN global** | SIM (330+ PoPs) | SIM (Edge Network) | SIM (Cloudflare-based) | SIM |
| **PoP Brasil** | SIM (Sao Paulo, Rio) | SIM | SIM (via Cloudflare) | SIM |
| **Custom domain** | SIM (gratis) | SIM (gratis) | SIM (gratis) | Parcial |
| **SSL** | SIM (auto) | SIM (auto) | SIM (auto) | SIM |
| **Headers customizados** | SIM | SIM | SIM | NAO |
| **GitHub integration** | SIM | SIM | SIM | NAO |
| **Preco se escalar** | Gratis ate muito alto | US$ 20/mes (Pro) | US$ 19/mes (Pro) | Gratis |

**Veredito: Cloudflare Pages.**

Bandwidth ilimitado no free tier e o fator decisivo. Se o jogo viralizar e tivermos 2 milhoes de sessoes na semana 1, cada uma carregando 3-5 MB de assets, estamos falando de 6-10 TB de bandwidth. No Vercel e Netlify, isso estoura o free tier no primeiro dia e gera uma conta de centenas de dolares. No Cloudflare Pages, o custo e zero.

Alem disso, Cloudflare tem PoPs em Sao Paulo e Rio de Janeiro. Para nosso publico (100% Brasil), a latencia de primeiro load sera <30ms ate o edge node mais proximo. Para loads subsequentes, o Service Worker resolve e a latencia e zero.

### Pipeline de Deploy

```
Developer push no GitHub (branch main)
    │
    v
Cloudflare Pages detecta push (webhook)
    │
    v
Build: pnpm install && vite build (< 10 segundos)
    │
    v
Deploy: assets servidos via CDN global (< 30 segundos)
    │
    v
Invalidacao de cache automatica
    │
    v
Jogo atualizado para TODOS os usuarios
(proximo refresh ou novo acesso)
```

**Tempo total de push-to-production: < 60 segundos.**

Compare com o pipeline anterior: GitHub Actions → Codemagic → build Android/iOS → Firebase App Distribution → QA → Google Play Console → review da loja → publicacao. Dias vs. segundos. Essa e a diferenca entre web e mobile.

### Estrategia de Updates Rapidos

O CEO e o Andre Guedes mencionaram "atualizacoes relampago" baseadas em eventos politicos. Com Cloudflare Pages, isso e trivial:

1. Aconteceu escandalo novo (dia normal no Brasil)
2. Dev adiciona nova frase de Game Over no JSON de frases
3. `git commit -m "add frase sobre [escandalo]" && git push`
4. 60 segundos depois: todos os jogadores veem a nova frase

Sem review de loja. Sem build de APK. Sem distribuicao gradual. Push e ta no ar. Isso e uma **vantagem competitiva massiva** para um jogo de satira politica que depende de relevancia temporal.

### itch.io como Canal Secundario

Alem do hosting principal no Cloudflare Pages com dominio proprio, publicar tambem no itch.io como canal de descoberta. O itch.io tem 900.000+ projetos e uma comunidade ativa. E gratis, aceita jogos HTML5 embeddados, e o dev escolhe o revenue share (pode ser 100% para o dev). Nao substitui o dominio proprio, mas adiciona um canal de aquisicao gratis.

---

## 6. Analytics sem Backend

### Camada 1: Google Analytics 4 (Essencial)

GA4 via gtag.js e 100% client-side. Zero backend. Um snippet de JavaScript no HTML e pronto. Gratis para o volume que precisamos.

**Eventos customizados a rastrear:**

| Evento | Parametros | Por que |
|---|---|---|
| `game_start` | `skin_variant`, `device_type`, `viewport_size` | Saber quem joga e em que device |
| `wave_reached` | `wave_number`, `score_at_wave`, `time_elapsed` | Entender onde os jogadores morrem |
| `game_over` | `final_score`, `waves_survived`, `zombies_killed`, `title_earned`, `time_survived` | Metrica principal de engajamento |
| `share_click` | `share_method` (whatsapp, twitter, copy_link, screenshot) | Metrica de viralidade |
| `share_complete` | `share_method` | Compartilhamento efetivo (Web Share API callback) |
| `ad_view` | `ad_type` (interstitial, rewarded), `placement` | Metricas de monetizacao |
| `ad_click` | `ad_type` | Engajamento com ads |
| `powerup_collected` | `powerup_type` | Game design: quais power-ups sao populares |
| `play_again` | `session_game_count` | Quantas partidas por sessao |
| `page_visibility_change` | `state` (hidden/visible) | Detectar alt-tab / troca de app |
| `return_visit` | `days_since_last`, `total_visits` | Retencao |

**Implementacao:**

```typescript
// Inicializacao (index.html)
// gtag.js snippet padrao do GA4

// Game Over (GameOverScene.ts)
gtag('event', 'game_over', {
    final_score: score,
    waves_survived: waveNumber,
    zombies_killed: killCount,
    title_earned: politicalTitle,
    time_survived: elapsedSeconds
});
```

### Camada 2: GameAnalytics (Game-Specific)

GameAnalytics e gratis para jogos indie e especializado em metricas de games: sessao media, retencao D1/D7/D30, funil de progressao, heatmaps de dificuldade. Complementa o GA4 com metricas que fazem sentido para game design.

**Implementacao:** SDK JavaScript (7 KB gzipped). Inicializa uma vez. Envia eventos automaticos (session_start, session_end) e customizados.

### Camada 3: Feature Flags (localStorage)

Para A/B testing simples sem backend:

```typescript
// No primeiro acesso, sorteia um grupo
if (!localStorage.getItem('ab_group')) {
    localStorage.setItem('ab_group', Math.random() < 0.5 ? 'A' : 'B');
}

// Usa o grupo para variar comportamento
const group = localStorage.getItem('ab_group');
const WAVE_DIFFICULTY = group === 'A' ? 1.0 : 1.2;

// Envia o grupo no evento de game_over
gtag('event', 'game_over', { ab_group: group, ... });
```

Isso permite testar hipoteses de game design (dificuldade, timing de power-ups, frequencia de ads) sem nenhum backend. Os dados vao para o GA4, onde podemos segmentar por grupo e comparar retencao/score.

### Dashboard de Metricas (Pre-Lancamento)

Configurar ANTES do lancamento no GA4:

1. **DAU / WAU / MAU** — Volume
2. **Sessoes por usuario por dia** — Engajamento
3. **Retencao D1, D3, D7** — Core metric de validacao
4. **Shares por sessao** — Metrica viral (K-factor)
5. **Tempo medio de sessao** — Deve ser ~3-5 min (1-2 partidas)
6. **Distribuicao de scores** — Curva de dificuldade (deve ser sino)
7. **Wave reached (media)** — Onde os jogadores morrem mais
8. **Device breakdown** — % mobile vs desktop, modelos mais comuns
9. **Receita de ads (AdSense dashboard)** — eCPM, impressoes, revenue

---

## 7. Ads no Browser

### Google AdSense H5 Games Ads — A Escolha

O Google lancou a **H5 Games Ad Placement API** especificamente para jogos HTML5. Substituiu o antigo IMA SDK com algo mais simples e melhor integrado. Dados do Google: *"publishers com H5 Games Ads viram session time 2x maior e ad revenue 3x maior"* comparado a implementacoes ad-hoc.

### Formatos de Ads

| Formato | Quando | Implementacao | Impacto na UX |
|---|---|---|---|
| **Interstitial** | A cada 3 partidas (entre Game Over e novo jogo) | `adBreak({ type: 'next', ... })` | Medio — jogador ja morreu, momento natural |
| **Rewarded** | "Assista e ganhe 1 revive" (apos Game Over) | `adBreak({ type: 'reward', ... })` | Baixo — opt-in, jogador ESCOLHE assistir |
| **Banner** | NAO | - | - |

**Por que sem banner:** Banners durante gameplay sao cancer de UX. Ocupam espaco precioso na tela (especialmente mobile), distraem, e geram eCPM baixissimo (R$ 1-3 CPM). O interstitial entre partidas gera R$ 15-30 CPM e o rewarded R$ 20-40 CPM. Faz mais sentido economico E de UX.

### Implementacao

```typescript
// Inicializacao (index.html, apos AdSense snippet)
window.adBreak = window.adBreak || function(o) { o.afterAd?.(); };
window.adConfig = window.adConfig || function(o) {};

adConfig({ preloadAdBreaks: 'on' }); // Pre-carrega ads

// Entre partidas (GameOverScene)
let gameCount = 0;

function onPlayAgain() {
    gameCount++;
    if (gameCount % 3 === 0) {
        adBreak({
            type: 'next',
            name: 'between-games',
            beforeAd: () => { /* pausa audio */ },
            afterAd: () => { startNewGame(); },
            adBreakDone: (placementInfo) => {
                gtag('event', 'ad_view', {
                    ad_type: 'interstitial',
                    status: placementInfo.breakStatus
                });
            }
        });
    } else {
        startNewGame();
    }
}

// Rewarded (revive)
function onReviveClick() {
    adBreak({
        type: 'reward',
        name: 'revive-reward',
        beforeReward: (showAdFn) => { showAdFn(); },
        adViewed: () => { revivePlayer(); },
        adDismissed: () => { /* jogador cancelou, sem revive */ },
        adBreakDone: (placementInfo) => {
            gtag('event', 'ad_view', {
                ad_type: 'rewarded',
                status: placementInfo.breakStatus
            });
        }
    });
}
```

### Projecao de Receita de Ads

| Cenario | Sessoes/mes | Interstitials/mes (1 a cada 3 jogos) | eCPM Interstitial | Rewarded/mes (20% opt-in) | eCPM Rewarded | **Receita/mes** |
|---|---|---|---|---|---|---|
| Pessimista | 300K | 100K | R$ 12 | 60K | R$ 25 | **R$ 2.700** |
| Base | 2M | 667K | R$ 15 | 400K | R$ 30 | **R$ 22.000** |
| Otimista | 10M | 3.3M | R$ 18 | 2M | R$ 35 | **R$ 129.400** |

### Alternativas a Considerar (Pos-Lancamento)

Se o jogo ganhar tracao e quisermos maximizar receita de ads:

- **AdinPlay**: Especializado em jogos HTML5. Mediacao de multiplas redes. Melhor fill rate.
- **Venatus**: Foco em gaming/entertainment. Premium advertisers.
- **Poki SDK**: Se distribuir na Poki, o SDK deles tem ads integrados com revenue share.

Para o lancamento, Google AdSense H5 Games Ads e suficiente. E o mais simples de integrar, nao precisa de aprovacao especial, e o eCPM no Brasil e decente.

---

## 8. Compartilhamento

### A Feature Mais Importante do Jogo

Vou repetir o que o Andre Guedes e o CEO disseram porque nao pode ser subestimado: **o compartilhamento e a feature mais importante do jogo inteiro.** Mais que o gameplay, mais que o humor, mais que os graficos. Se o botao de compartilhar nao funcionar perfeitamente, o jogo nao viraliza. Ponto.

### Web Share API

A Web Share API tem score de compatibilidade de 67/100 entre browsers. Chrome (Android e desktop), Safari (iOS e macOS) e Edge suportam nativamente. Firefox exige flag habilitada.

Para os 90%+ do publico brasileiro (Chrome Android + Safari iOS): funciona.

**Implementacao:**

```typescript
async function shareScore(scoreData: ScoreData, cardImage: Blob) {
    const shareData: ShareData = {
        title: 'Congresso dos Mortos',
        text: `Sobrevivi ${scoreData.timeFormatted} na Esplanada dos Zumbis e virei "${scoreData.title}"! `
            + `Score: ${scoreData.score} | Zumbis eliminados: ${scoreData.kills}\n`
            + `Quanto voce aguenta? congressodosmortos.com.br`,
        url: 'https://congressodosmortos.com.br',
        files: [new File([cardImage], 'meu-score.png', { type: 'image/png' })]
    };

    if (navigator.canShare?.(shareData)) {
        await navigator.share(shareData);
        gtag('event', 'share_complete', { method: 'web_share_api' });
    } else {
        // Fallback: copiar texto para clipboard
        await navigator.clipboard.writeText(shareData.text + '\n' + shareData.url);
        showToast('Link copiado! Cole no WhatsApp ou onde quiser.');
        gtag('event', 'share_complete', { method: 'clipboard_fallback' });
    }
}
```

### Canvas-to-PNG (Card de Resultado)

O card de Game Over que o Andre Guedes projetou precisa ser gerado como imagem PNG direto no browser. Sem servidor. Sem API externa.

```typescript
function generateScoreCard(scoreData: ScoreData): Promise<Blob> {
    const canvas = document.createElement('canvas');
    canvas.width = 1080;
    canvas.height = 1350; // Aspect ratio ideal para Instagram Stories
    const ctx = canvas.getContext('2d')!;

    // Background
    ctx.fillStyle = '#1a0a0a';
    ctx.fillRect(0, 0, 1080, 1350);

    // Titulo
    ctx.font = 'bold 64px "Press Start 2P", monospace';
    ctx.fillStyle = '#ff4444';
    ctx.textAlign = 'center';
    ctx.fillText('CONGRESSO DOS MORTOS', 540, 120);

    // Score, titulo politico, stats...
    // [renderizacao do card completo]

    // URL do jogo (sempre visivel)
    ctx.font = '32px sans-serif';
    ctx.fillStyle = '#888';
    ctx.fillText('congressodosmortos.com.br', 540, 1300);

    return new Promise(resolve => {
        canvas.toBlob(blob => resolve(blob!), 'image/png');
    });
}
```

### OpenGraph Meta Tags

Para que o link `congressodosmortos.com.br` tenha preview bonito quando compartilhado:

```html
<meta property="og:title" content="Congresso dos Mortos — Sobreviva a Esplanada dos Zumbis">
<meta property="og:description" content="Browser game gratis de satira politica. Mate zumbis-politicos com vassoura. 3 minutos. Sem download.">
<meta property="og:image" content="https://congressodosmortos.com.br/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="https://congressodosmortos.com.br">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Congresso dos Mortos">
<meta name="twitter:description" content="Sobreviva a Esplanada dos Zumbis. Browser game gratis. 3 minutos. Sem download.">
<meta name="twitter:image" content="https://congressodosmortos.com.br/og-image.png">
```

A imagem de OG precisa ser de alta qualidade — e a primeira impressao de quem recebe o link no WhatsApp. Deve ser feita pelo artista, nao gerada automaticamente.

---

## 9. PWA — Vale a Pena?

### Resposta Curta: SIM, mas Minimalista

Em 2026, service workers nao sao opcionais — sao esperados. Mas para nosso caso, o objetivo nao e "instalar o jogo como app". E **cache de assets para load instantaneo no segundo acesso**.

### O que Implementar

| Feature PWA | Implementar? | Justificativa |
|---|---|---|
| **Service Worker com pre-cache** | SIM | Apos primeiro load, todo o jogo (~3-5 MB) fica no cache. Segundo acesso e instantaneo. Funciona offline |
| **Web App Manifest** | SIM | Permite "Adicionar a tela inicial" no Android. Abre fullscreen, sem barra de URL. Experiencia de app |
| **Icone de app** | SIM | Icone bonito na home screen. Branding |
| **Push notifications** | NAO | Complexidade desnecessaria. Precisa de backend para push server. Nao vale no MVP |
| **Background sync** | NAO | Nao temos dados para sincronizar (sem backend) |
| **Install prompt customizado** | NAO (v1.2) | Nao queremos distrair do jogo no primeiro acesso. Talvez na v1.2 apos engajamento comprovado |

### Implementacao com Workbox

```typescript
// service-worker.ts (gerado pelo Vite plugin)
import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { CacheFirst } from 'workbox-strategies';

// Pre-cache todos os assets do build
precacheAndRoute(self.__WB_MANIFEST);

// Cache-first para imagens e audio (nunca mudam entre deploys)
registerRoute(
    ({ request }) => request.destination === 'image' || request.destination === 'audio',
    new CacheFirst({ cacheName: 'assets-cache' })
);
```

**Resultado:** Primeiro load em 4G = ~2-3 segundos. Segundo load (ou offline) = **< 500ms**. O jogo literalmente abre instantaneamente.

### manifest.json

```json
{
    "name": "Congresso dos Mortos",
    "short_name": "CongressoMortos",
    "description": "Sobreviva a Esplanada dos Zumbis. Browser game de satira politica.",
    "start_url": "/",
    "display": "fullscreen",
    "orientation": "portrait",
    "background_color": "#1a0a0a",
    "theme_color": "#ff4444",
    "icons": [
        { "src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
        { "src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
    ]
}
```

### Offline: O Jogo Funciona Sem Internet

Apos o primeiro acesso, o Service Worker cacheia TUDO. O jogador pode:
- Abrir o jogo no metro (sem sinal)
- Jogar normalmente (tudo e client-side)
- Score salva no localStorage
- Analytics envia quando voltar online (GA4 tem queue offline nativo)
- Ads nao aparecem offline (obvio), mas o jogo funciona

Isso e uma vantagem que poucos browser games oferecem. E vem de graca com 20 linhas de Service Worker.

---

## 10. O que Cortar vs. Manter da Tech Strategy Original

### O que vai pro LIXO

| Item Original | Status | Por que |
|---|---|---|
| **Godot 4.4** | DESCARTADO | Web game, nao mobile nativo |
| **GDScript** | DESCARTADO | TypeScript agora |
| **Firebase Auth** | DESCARTADO | Zero backend. Sem login |
| **Firebase Firestore** | DESCARTADO | Zero backend. localStorage |
| **Firebase Cloud Functions** | DESCARTADO | Zero backend |
| **Firebase Crashlytics** | DESCARTADO | Browser nao precisa. `window.onerror` + GA4 |
| **Firebase Remote Config** | DESCARTADO | Feature flags no codigo + redeploy em 60s |
| **Firebase Cloud Messaging** | DESCARTADO | Sem push notifications no MVP |
| **AdMob (mobile)** | DESCARTADO | Google H5 Games Ads (web) |
| **Google Play Billing / IAP** | DESCARTADO | Sem compras in-app no MVP |
| **Codemagic CI/CD** | DESCARTADO | Cloudflare Pages auto-deploy |
| **Git LFS** | DESCARTADO | Assets <5 MB total. Git normal |
| **Spine 2D** | DESCARTADO | Sprite sheets simples |
| **FMOD** | DESCARTADO | Phaser audio nativo |
| **APK size optimization** | DESCARTADO | Nao existe APK |
| **ETC2/PVRTC texture compression** | DESCARTADO | PNG/WebP padrao |
| **Pipeline iOS (TestFlight, App Store)** | DESCARTADO | Nao existe app |
| **Pipeline Android (Google Play Console)** | DESCARTADO | Nao existe app |
| **Equipe de 5 pessoas** | REDUZIDO | 1-2 devs + 1 artista |

### O que PERMANECE (Principios que Atravessam Plataformas)

| Principio Original | Status | Adaptacao para Web |
|---|---|---|
| **Simplicidade Radical** | MANTIDO | Ainda mais radical. Zero backend |
| **Ship First, Optimize Later** | MANTIDO | Ainda mais importante com 2 semanas |
| **Otimizar para o Pior Caso** | MANTIDO | Galaxy A06 no Chrome, nao nativo |
| **Object Pooling** | MANTIDO | Mesma tecnica, agora em JS |
| **Texture Atlas** | MANTIDO | TexturePacker → Phaser atlas |
| **Sprite reuse com palette swap** | MANTIDO | Funciona igual na web |
| **Animacao limitada (12fps)** | MANTIDO | Estilo e performance |
| **Audio: SFX curtos + music streaming** | MANTIDO | Web Audio API |
| **Visibilidade culling** | MANTIDO | Phaser camera bounds |
| **Score local + sync async** | MANTIDO (parcial) | Score so local no MVP. Sync na v1.2 |
| **Build vs Buy vs Skip** | MANTIDO | Principio universal |
| **Metricas de validacao (D1, D7, sessao)** | MANTIDO | Agora via GA4 + GameAnalytics |
| **Gate decisions** | MANTIDO | Validacao tecnica no dia 1 |

### O que era SKIP e Continua SKIP

| Feature | Status | Quando |
|---|---|---|
| Leaderboard global | SKIP (MVP) → v1.2 (semana 3) | Se metricas justificarem |
| Battle Pass | SKIP | Versao mobile |
| Skins/cosmeticos | SKIP | Versao mobile |
| IAP | SKIP | Versao mobile |
| PvP/Co-op | SKIP | Versao mobile |
| Multiplos mapas | SKIP | v2.0 web ou mobile |
| Anti-cheat | SKIP | Irrelevante sem leaderboard global |
| Social/clans | SKIP | Versao mobile |

---

## 11. Timeline Tecnico de 2 Semanas

### Premissa: 2 Devs + 1 Artista

**Dev 1 (Lead):** Senior em JavaScript/TypeScript, experiencia com Phaser ou jogos web. Responsavel pelo core gameplay.
**Dev 2 (Support):** Pleno+ em frontend. Foco em UI, ads, analytics, compartilhamento, responsividade.
**Artista:** Experiencia com pixel art/sprite art. Traduz o estilo de Andre Guedes para sprites de jogo.

### SEMANA 1 — BUILD

| Dia | Dev 1 (Core Gameplay) | Dev 2 (Systems/UI) | Artista |
|---|---|---|---|
| **Dia 1** | Setup: Vite + Phaser + TS. PoC de performance (200 sprites no Galaxy A06). Camera, viewport, input basico | Setup: projeto, repo GitHub, Cloudflare Pages, analytics (GA4 + GameAnalytics), PWA basico (manifest + SW) | Setup: Aseprite. Cidadao sprite sheet (3 tons de pele): idle, andar (4 frames cada) |
| **Dia 2** | Player movement (touch joystick + WASD). Ataque automatico (nearest enemy targeting). Arcade Physics colisao | Tela de menu (minimalista: escolha de skin + botao JOGAR). Responsivo mobile/desktop. Fullscreen API | Cidadao: atacar, dano, morte (3 frames cada). Vereador-Zumbi: andar, atacar, morte (3 frames cada) |
| **Dia 3** | Wave spawner (6 waves em 3 minutos). Dificuldade progressiva. Enemy AI: state machine (chase, attack, die) | Sistema de score + combo multiplier. HUD: timer, score, HP bar, combo indicator, wave counter | Assessor de Fake News: andar, atirar, morte. Manchetes como sprites de projetil |
| **Dia 4** | 4 tipos de zumbi implementados com comportamentos unicos. Senador com escudo. Banqueiro com corromper. Boss | Tela de Game Over: layout do card, titulo politico, stats. Canvas-to-PNG do card compartilhavel | Senador Blindado: andar, escudo ativo, dano, morte. Banqueiro-Zumbi: andar, corromper, morte |
| **Dia 5** | Power-ups: 5 tipos implementados. Object pooling para tudo (zumbis, projeteis, power-ups, efeitos) | Web Share API: compartilhar card + texto. Fallback clipboard. OpenGraph meta tags | Candidato Eterno (boss): andar, discurso, "2o turno", morte. Power-up sprites (5) |
| **Dia 6** | Balanceamento inicial: HP dos zumbis, velocidades, spawn rates, dano, duracao de power-ups | Google H5 Games Ads: interstitial a cada 3 jogos + rewarded para revive | Cenario: Esplanada tileset, Congresso de fundo, Espelho D'Agua, ministerios como blocos |
| **Dia 7** | Integracao arte + codigo. First playable COMPLETO. Teste no Galaxy A06. Fix de performance se necessario | Integracao ads + analytics end-to-end. Teste de compartilhamento real (WhatsApp, Twitter). Feature flags | UI elements: botoes, icones, HUD sprites. Card de Game Over arte final. Figurinhas WhatsApp (bonus) |

### SEMANA 2 — POLISH + LAUNCH

| Dia | Dev 1 (Polish Gameplay) | Dev 2 (Polish Systems) | Artista |
|---|---|---|---|
| **Dia 8** | Efeitos visuais: screen shake, hit flash (tint branco), squash-and-stretch nas mortes. Particulas de santinhos voando | 50+ frases de Game Over implementadas (JSON). Titulos politicos por faixa de score. Randomizacao | Efeitos visuais: particulas de dano, explosao de moedas (senador), aura do banqueiro. Polish nos sprites |
| **Dia 9** | Audio: integracao SFX (ataques, mortes, power-ups, combo) + loops de musica + ambience. Mixagem | Audio: testes de reproducao em mobile (autoplay policies). Botao de mute. Volume control | OG image (1200x630) para preview de link. Icone do PWA (192 + 512). Favicon |
| **Dia 10** | QA: teste em 5+ devices reais (Galaxy A06, iPhone SE, Moto G, desktop Chrome, desktop Firefox) | QA: teste de ads em diferentes cenarios. Analytics validacao (eventos chegando no GA4?). Lighthouse audit | Fix de sprites baseado em feedback do QA. Ajustes de cores/contraste para legibilidade |
| **Dia 11** | Balanceamento final: sessao de playtest com 5-10 pessoas. Ajuste de curva de dificuldade baseado em feedback | Deploy de staging. Teste de carga (Lighthouse, WebPageTest). Cache headers. Compressao de assets | Assets finais entregues. TexturePacker atlas gerados |
| **Dia 12** | Bug fixes criticos. Performance final pass. Ultima rodada de testes no Galaxy A06 | Bug fixes. Analytics dashboard configurado no GA4. Alertas de metricas | Backup: qualquer sprite que precise de correcao |
| **Dia 13** | FEATURE FREEZE. Nenhum codigo novo. So bug fixes | Pre-lancamento: teasers (Andre Guedes posta). Build final no Cloudflare Pages staging | Materiais de marketing: screenshots, GIFs de gameplay |
| **Dia 14** | **LANCAMENTO.** Monitoramento ao vivo. Hotfix pipeline pronto | **LANCAMENTO.** Analytics em tempo real. Monitoramento de ads. Monitoramento de erros (window.onerror → GA4) | |

### Gates de Validacao

| Gate | Quando | Criterio | Se falhar |
|---|---|---|---|
| **PoC Performance** | Dia 1 | 200 sprites + audio + physics a 55+ fps no Galaxy A06 Chrome | PARAR. Diagnosticar. Se impossivel: reduzir escopo visual (menos particulas, sprites menores) |
| **First Playable** | Dia 7 | Jogo jogavel end-to-end: menu → gameplay → game over → share → replay | Dia 8-9 terminam gameplay. Push do polish para semana 3 |
| **Ads Funcionando** | Dia 7 | Interstitial e rewarded rodando em producao | Fallback: lançar sem ads, adicionar na v1.1 |
| **QA Mobile** | Dia 10 | 60fps estavel em Galaxy A06, sem crashes, audio funcional | Dia 11-12: otimizacao de emergencia |
| **Launch Ready** | Dia 13 | Tudo funcional, analytics validado, assets finais, build de producao | Atrasar lancamento em 1-2 dias (margem aceitavel) |

### Pos-Lancamento (Semanas 3-4)

| Semana | Atividade |
|---|---|
| **Semana 3** | Monitorar metricas. Bug fixes. v1.1 com balanceamento baseado em dados. Submeter na Poki e CrazyGames. Atualizacoes relampago (novas frases de Game Over baseadas em eventos politicos). Se metricas justificarem: iniciar leaderboard global com Supabase |
| **Semana 4** | v1.2 com leaderboard global (se metricas OK). Distribuicao nas plataformas de browser games. Analise completa de metricas. Decisao GO/NO-GO para mobile |

---

## 12. Riscos Tecnicos

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| 1 | **Performance no Chrome Android (Galaxy A06) abaixo de 50fps** | Baixa | Critico | PoC no dia 1. Se falhar: reduzir max entidades (100 em vez de 150), desativar particulas, resolucao de canvas reduzida (540x960). Em ultimo caso: usar Canvas renderer em vez de WebGL |
| 2 | **Touch controls com lag perceptivel em mobile** | Media-Baixa | Alto | Testar joystick virtual no dia 2 em device real. Se lag: implementar joystick custom com touch events raw (nao Phaser input). Alternativa: controle simplificado (arrasta para mover, sem joystick visual) |
| 3 | **Web Audio API bloqueada (autoplay policy)** | Alta | Medio | Chrome/Safari exigem interacao do usuario antes de tocar audio. Solucao: iniciar AudioContext no primeiro toque (botao JOGAR). Phaser ja lida com isso, mas validar em mobile |
| 4 | **Web Share API nao funciona em algum browser** | Media | Alto | Fallback para clipboard copy ja implementado. Segundo fallback: mostrar texto + imagem para o usuario copiar manualmente. Testar em Chrome Android, Safari iOS, Samsung Internet |
| 5 | **Google AdSense rejeitando o site (conteudo satirico)** | Media | Alto | AdSense pode considerar satira politica como "conteudo sensivel". Mitigacao: disclaimers claros ("obra de ficcao"), sem nomes reais de politicos nos ads placement. Fallback: AdinPlay ou Venatus como ad provider alternativo. Pior caso: lancar sem ads, monetizar via "pague um cafe" (Apoia.se/Pix) |
| 6 | **Cloudflare Pages atingindo algum rate limit nao documentado** | Muito Baixa | Critico | Para conteudo 100% estatico, e praticamente impossivel. Cloudflare e projetado para servir bilhoes de requests. Mas ter Vercel como hosting backup configurado (10 min de setup) |
| 7 | **Scope creep: "so mais uma feature"** | Alta | Critico | O Andre Guedes listou 14 itens. O CEO disse NADA mais. Eu digo NADA mais. Se nao esta no timeline, nao existe. Qualquer ideia nova vai para o backlog da v1.1 |
| 8 | **Dev nao domina Phaser** | Media | Alto | Phaser tem a melhor documentacao e exemplos de qualquer framework de jogos web. Curva de aprendizado para dev JS/TS senior: 2-3 dias para produtividade. Dia 1 e setup + PoC, entao o dev "aprende" construindo |
| 9 | **Safari iOS quirks (WebGL, audio, fullscreen)** | Media | Medio | Safari e o IE do mobile. Testar no dia 10. Problemas comuns: AudioContext precisa de `resume()` manual; WebGL tem limites de textura menores; fullscreen nao funciona em iPhone (limitacao da Apple). Mitigacao: testar cedo, ter workarounds prontos |
| 10 | **Jogo muito facil ou muito dificil no lancamento** | Alta | Medio | Impossivel acertar o balanceamento sem dados reais. Solucao: feature flags para parametros de dificuldade (spawn rate, HP dos zumbis, velocidade). Ajustar no dia seguinte ao lancamento baseado em dados de GA4 (wave_reached, time_survived). Deploy em 60 segundos |

### Matriz de Contingencia

```
Se performance falhar no Galaxy A06    → Reduzir resolucao canvas + desativar particulas
Se touch controls forem ruins         → Simplificar para "drag to move" sem joystick
Se AdSense rejeitar                   → AdinPlay/Venatus como alternativa, ou launch sem ads
Se Web Share API falhar               → Clipboard copy + "cole no WhatsApp"
Se Safari iOS quebrar                 → Priorizar Chrome Android (80%+ do target)
Se dev nao dominar Phaser a tempo     → Escopo reduzido (3 tipos de zumbi em vez de 4)
Se arte atrasar                       → Placeholder sprites coloridos + substituir depois
Se TUDO der errado                    → Um dev, 1 mapa, 2 zumbis, sem ads, sem PWA.
                                        Mas o jogo EXISTE e o link FUNCIONA.
```

---

## 13. Estrutura de Diretorios do Projeto

```
congresso-dos-mortos/
├── index.html                    # Entry point (OG tags, AdSense, GA4, manifest)
├── manifest.json                 # PWA manifest
├── vite.config.ts                # Vite config (build, plugins, Workbox)
├── tsconfig.json                 # TypeScript config
├── package.json                  # Dependencies (phaser, workbox, vite)
├── public/
│   ├── og-image.png              # OpenGraph preview image (1200x630)
│   ├── icons/
│   │   ├── icon-192.png          # PWA icon
│   │   ├── icon-512.png          # PWA icon
│   │   └── favicon.ico           # Browser favicon
│   └── assets/
│       ├── sprites/
│       │   ├── characters.png    # Atlas: cidadao (3 variantes)
│       │   ├── characters.json   # Atlas metadata
│       │   ├── zombies.png       # Atlas: todos os zumbis
│       │   ├── zombies.json      # Atlas metadata
│       │   ├── effects.png       # Atlas: particulas, power-ups, projeteis
│       │   ├── effects.json      # Atlas metadata
│       │   └── ui.png            # Atlas: HUD, botoes, icones
│       ├── tilemap/
│       │   ├── esplanada.png     # Tileset do cenario
│       │   └── esplanada.json    # Tilemap (Tiled format)
│       └── audio/
│           ├── music-main.ogg    # Loop principal
│           ├── music-main.mp3    # Fallback Safari
│           ├── sfx-hit.ogg       # SFX: ataque acerta
│           ├── sfx-death.ogg     # SFX: zumbi morre
│           ├── sfx-powerup.ogg   # SFX: coleta power-up
│           ├── sfx-combo.ogg     # SFX: combo alto
│           └── sfx-gameover.ogg  # SFX: game over
├── src/
│   ├── main.ts                   # Entry: Phaser.Game config, inicializacao
│   ├── config.ts                 # Constantes do jogo (velocidades, HP, spawn rates)
│   ├── scenes/
│   │   ├── BootScene.ts          # Preload de assets, setup
│   │   ├── MenuScene.ts          # Tela inicial: skin selection, botao JOGAR
│   │   ├── GameScene.ts          # Gameplay principal (o coracao do jogo)
│   │   └── GameOverScene.ts      # Resultado, card, share, ads
│   ├── entities/
│   │   ├── Player.ts             # Jogador: movimento, HP, auto-attack
│   │   ├── Zombie.ts             # Base class para zumbis
│   │   ├── Vereador.ts           # Zumbi basico (horda)
│   │   ├── Assessor.ts           # Zumbi atirador (manchetes)
│   │   ├── Senador.ts            # Zumbi tank (escudo)
│   │   ├── Banqueiro.ts          # Zumbi elite (corromper)
│   │   └── Boss.ts               # Candidato Eterno
│   ├── systems/
│   │   ├── WaveManager.ts        # Logica de waves (spawn, dificuldade, timer)
│   │   ├── ScoreManager.ts       # Score, combo, titulos politicos
│   │   ├── PowerUpManager.ts     # Spawn e efeitos de power-ups
│   │   ├── PoolManager.ts        # Object pooling centralizado
│   │   └── AudioManager.ts       # Controle de audio (SFX, musica, mute)
│   ├── ui/
│   │   ├── HUD.ts                # HP bar, score, timer, combo, wave
│   │   ├── VirtualJoystick.ts    # Touch joystick para mobile
│   │   └── ShareCard.ts          # Geracao do card PNG compartilhavel
│   ├── data/
│   │   ├── gameOverPhrases.json  # 50+ frases de Game Over
│   │   ├── politicalTitles.json  # Titulos por faixa de score
│   │   ├── headlineProjectiles.json # Manchetes do Assessor
│   │   └── waveConfig.json       # Configuracao das 6 waves
│   └── utils/
│       ├── analytics.ts          # Wrapper GA4 + GameAnalytics
│       ├── ads.ts                # Wrapper H5 Ad Placement API
│       ├── share.ts              # Web Share API + fallbacks
│       └── storage.ts            # localStorage wrapper (high score, settings)
├── sw.ts                         # Service Worker (Workbox)
└── .github/
    └── (sem CI/CD config — Cloudflare Pages faz tudo)
```

**Total estimado de linhas de codigo:** ~3.000-5.000 linhas de TypeScript. Factivel para 2 devs em 2 semanas.

---

## 14. Nota Final do CTO

Li a tech strategy que escrevi ha 2 semanas atras. Godot 4.4, Firebase, Codemagic, pipeline de APK, equipe de 5 pessoas, 6 meses. Era um documento solido para o problema errado. O CEO mudou o problema — e o problema novo e ordens de magnitude mais simples.

O Luca Galante fez Vampire Survivors com Phaser, sozinho, gastando 1.100 libras. O jogo rodava no browser. Usava assets prontos. O codigo provavelmente era feio. Nao importava. O que importava era que o game loop era viciante, a progressao era satisfatoria, e o jogo era facil de compartilhar.

Nos temos vantagens que ele nao tinha: uma IP de um humorista com 1,48M de inscritos, um momento politico unico, um budget de R$ 30-50K (vs 1.100 libras), e 2 devs em vez de 1. Se nao conseguirmos entregar um MVP funcional em 2 semanas com essas vantagens, o problema nao e tecnico — e de execucao.

A stack e simples: **Phaser 3, TypeScript, Vite, Cloudflare Pages.** Quatro tecnologias. O resto e disciplina.

Zero backend. Zero Firebase. Zero servidor. Zero complexidade desnecessaria.

O jogo e um arquivo HTML, uns PNGs e um bocado de JavaScript servido por um CDN. Exatamente como o Doom era um executavel, uns WADs e um bocado de assembly servido por um disquete. A simplicidade nao e limitacao — e a maior feature.

**Ship it.**

---

**John Carmack**
**CTO & Arquiteto de Engenharia**
**Abril 2026**

---

## Fontes

### Frameworks e Engine
- [JS Game Rendering Benchmark — Phaser, PixiJS, Kaplay e outros](https://github.com/Shirajuki/js-game-rendering-benchmark)
- [Web Game Engines Comparison 2026 — Cinevva](https://app.cinevva.com/guides/web-game-engines-comparison.html)
- [Phaser vs PixiJS: JavaScript Game Framework Comparison 2025](https://generalistprogrammer.com/comparisons/phaser-vs-pixijs)
- [PixiJS vs Phaser: The Gold Standard — Aircada](https://aircada.com/blog/pixijs-vs-phaser)
- [Phaser v4.0.0 Release — Phaser](https://phaser.io/download/release/v4.0.0)
- [Phaser 4 Dev Log: Simplex Noise, Tiling, Flow](https://phaser.io/news/2026/04/phaser-4-simplex-noise)
- [I Tried 3 Web Game Frameworks — JSLegendDev (Kaplay review)](https://jslegenddev.substack.com/p/i-tried-3-web-game-frameworks-so)
- [Phaser.js: How We Build 2D Games with JavaScript 2026](https://www.seeles.ai/resources/blogs/phaser-js-game-development-2026)

### Vampire Survivors
- [Vampire Survivors Development — Open-Source Fueled Fever Dream](https://www.gamedeveloper.com/design/vampire-survivors-development-sounds-like-an-open-source-fueled-fever-dream)
- [Quick HTML5 Prototype of Vampire Survivors Built with Phaser](https://emanueleferonato.com/2024/11/29/quick-html5-prototype-of-vampire-survivors-built-with-phaser-like-the-original-game/)
- [How Vampire Survivors Was Rebuilt for Xbox — Xbox Wire](https://news.xbox.com/en-us/2023/04/13/vampire-survivors-dlc-2-launch/)

### Performance Mobile
- [How I Optimized My Phaser 3 Action Game — 2025](https://franzeus.medium.com/how-i-optimized-my-phaser-3-action-game-in-2025-5a648753f62b)
- [Phaser 3.60 Mobile Performance Improvements](https://github.com/phaserjs/phaser/blob/v3.60.0/changelog/3.60/MobilePerformance.md)
- [HTML5 Game Optimization Guide — Will Eastcott](https://gitnation.com/contents/optimizing-html5-games-10-years-of-learnings)
- [High Performance Mobile Game Development in HTML5 — Asad Memon](https://asadmemon.com/blog/perf-game-dev/)
- [What to Do When Your HTML5 Game Runs Slow on Mobile](https://www.gamedeveloper.com/programming/what-to-do-when-your-html5-game-runs-slow-on-mobile-devices)

### Hosting
- [Cloudflare Pages vs Netlify vs Vercel: Static Site Hosting Compared 2026](https://danubedata.ro/blog/cloudflare-pages-vs-netlify-vs-vercel-static-hosting-2026)
- [The Complete 2026 Guide to Frontend Hosting](https://www.juxtaposedtides.com/post/the-complete-2026-guide-to-frontend-hosting-every-platform-compared-for-performance-pricing-and-s)
- [Cloudflare vs Vercel vs Netlify for Engineering Websites 2026](https://www.luniq.io/en/resources/blog/cloudflare-vs-vercel-vs-netlify-for-engineering-websites-in-2026)

### Analytics
- [GA4 Games Reporting Collection — Google](https://support.google.com/analytics/answer/12925133?hl=en)
- [5 Best Analytics Tools for Gaming Companies 2026](https://mitzu.io/post/top-5-gaming-analytics-tools-to-use/)
- [Google Analytics vs GameAnalytics — StackShare](https://stackshare.io/stackups/gameanalytics-vs-google-analytics)

### Ads e Monetizacao
- [Google AdSense H5 Games Ads](https://adsense.google.com/start/h5-games-ads/)
- [H5 Games Ads API: The Ultimate Integration Guide — Boomie Studio](https://boomiestudio.com/blog/h5-games-ads-guide)
- [Best AdSense Alternatives for H5 Game Monetization — MonetizeMore](https://www.monetizemore.com/blog/best-adsense-alternatives-for-h5-game/)
- [Best Ad Networks to Monetize HTML5 Games — DoonDookStudio](https://doondook.studio/best-ad-networks-monetize-html5-games/)
- [HTML5 Gaming Trends and Monetization Strategy — Think with Google](https://www.thinkwithgoogle.com/intl/en-apac/marketing-strategies/app-and-mobile/html5-gaming-trends-monetization-strategy/)

### Distribuicao
- [Navigating Web Gaming Platforms for Indie Developers — Hology](https://hology.app/blog/web-gaming-1)
- [The Huge, Hidden Web Game Market — Gamedeveloper](https://www.gamedeveloper.com/business/the-huge-hidden-web-game-market-no-one-talks-about-and-how-to-get-in-)
- [CrazyGames Developer Portal](https://developer.crazygames.com/)
- [Poki for Developers](https://developers.poki.com/guide/web-game-engines)
- [How to Make Money on Itch.io — Indie Game Revenue Guide 2026](https://generalistprogrammer.com/tutorials/how-to-make-money-on-itchio-indie-game-guide)

### PWA e Service Workers
- [Progressive Web Apps in 2026: Service Workers Explained — jsmanifest](https://jsmanifest.com/service-workers-pwa-guide)
- [Offline-First PWAs: Service Worker Caching Strategies](https://www.magicbell.com/blog/offline-first-pwas-service-worker-caching-strategies)
- [Making the PWA Work Offline with Service Workers — MDN](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Tutorials/js13kGames/Offline_Service_workers)

### Vite e Build
- [Vite 8 Debuts with Unified Rolldown Bundler — AlternativeTo](https://alternativeto.net/news/2026/3/vite-8-debuts-with-unified-and-faster-rolldown-bundler-integrated-devtools-and-wasm-ssr/)
- [Vite Guide: Setup, Config, Build Optimization 2026](https://devtoolbox.dedyn.io/blog/vite-complete-guide)

### Web Share API
- [Web Share API — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Share_API)
- [Cross Browser Compatibility Score of Web Share API](https://www.testmu.ai/web-technologies/web-share/)
