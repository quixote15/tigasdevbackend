# Q1-01 HORA EXTRA -- ESTRATEGIA TECNICA
### John Carmack -- CTO | Abril 2026

---

> *"A Quest 01 tem um problema que ninguem percebeu ainda: o doc de quest design descreve platforming -- pulo simples, pulo duplo, mesas como plataformas, corrimao de escada rolante. Os docs de arquitetura (19 e 22) foram escritos para um side-scroller FLAT com gravity zero. Isso nao e um detalhe. Isso e uma decisao fundamental de fisica que muda a arquitetura inteira do Player, do level design e do input system. Eu preciso resolver isso ANTES de qualquer linha de codigo."*

---

## 1. STACK: CONFIRMADA COM RESSALVA

**React 18 + Phaser 3.88 + Vite + TypeScript.** Continua correto. Nao muda.

Justificativa rapida -- ja foi dada nos docs 19 e 22, mas repito o essencial:

- **Phaser 3.88** e a unica engine web madura com Arcade Physics embutido, tilemap loader nativo, sprite atlas support, e zero build complexity. Alternativas (PixiJS, BabylonJS, Three.js) exigem reimplementar fisica, camera, tilemap, scene management. Nao compensa para um side-scroller 2D.
- **React** cuida do DOM: menus, HUD overlay, dialogos/caixas de texto narrativas, tela de game over. Phaser renderiza APENAS gameplay no canvas.
- **Vite** porque e o bundler mais rapido para dev iteration e tree-shakes Phaser corretamente.
- **TypeScript** porque Phaser sem tipos e suicidio -- a API e enorme e a documentacao e irregular.

**Ressalva critica:** A Quest 01 introduz platforming. Os docs 19 e 22 assumiram `gravity: { y: 0 }`. Isso MUDA. Ver secao 2.1.

---

## 2. TRADE-OFFS CRITICOS

### 2.1 Gravidade e Platforming: gravity ON vs gravity OFF

**O problema:** O quest design de "Hora Extra" descreve:
- Mesas de escritorio como plataformas (pulo simples)
- Arquivos empilhados (pulo duplo)
- Corrimao de escada rolante como plataforma
- Ze inicia sentado e LEVANTA ao pressionar direcao

Isso e platformer. Os docs de arquitetura diziam "nao e platformer, zero gravity". Alguem mudou o design sem avisar a engenharia. Acontece.

| Opcao | Pros | Contras |
|---|---|---|
| **A: Gravity ON (platformer leve)** | Respeita o quest design tal como escrito. Pulo sobre mesas e satisfatorio. Verticalidade adiciona profundidade ao combate. | Requer ground check, coyote time, variable jump height, one-way platforms. Mais complexo. |
| **B: Gravity OFF (flat walker)** | Mais simples. Menos bugs. Mais rapido de implementar. | Ignora o quest design. Remove a mesa como obstaculo/plataforma. Remove o corrimao da escada. |

**Minha recomendacao: A. Gravity ON. Platformer leve.**

O quest design tem RAZAO. A mesa bloqueando o caminho e o primeiro momento de aprendizado do jogador. Remover isso degrada o tutorial. O custo tecnico e real mas gerenciavel -- estamos falando de Arcade Physics com gravidade, nao Matter.js com joints e torque. Sao 4 variaveis extras no Player: `isGrounded`, `jumpVelocity`, `coyoteTimer`, `jumpBuffer`. Uns 80 linhas de codigo. Vale a pena.

**Implicacao imediata:** `gravity: { y: 800 }` no Phaser config. Ground collision layer no tilemap. One-way platforms para mesas e corrimao.

**Parametros de pulo para Q1-01:**
```
JUMP_VELOCITY: -280         // px/s (negativo = para cima)
GRAVITY: 800                // px/s^2
COYOTE_TIME: 80             // ms (tolerancia pos-borda)
JUMP_BUFFER: 100            // ms (input antes de pousar)
VARIABLE_JUMP_CUTOFF: 0.4   // multiplicador se soltar botao cedo
```

Esses numeros dao um pulo que leva ~350ms ate o apice e ~350ms de queda. Altura maxima de ~49px no viewport logico (480x270). Suficiente para pular uma mesa de escritorio de 32px.

---

### 2.2 Waves: Timer-based vs Trigger-based vs Scripted

| Opcao | Descricao | Pros | Contras |
|---|---|---|---|
| **A: Timer-based** | Waves aparecem em intervalos fixos | Previsivel, facil de balancear | Ignora posicao do jogador. Pode spawnar inimigo fora da tela atras do jogador. |
| **B: Trigger-based** | Waves ativam quando jogador cruza ponto no mapa | Respeita o ritmo do jogador. Nenhum spawn desperdicado. | Requer trigger zones no tilemap. |
| **C: Scripted (sequencial)** | Script linear: "ao entrar na sala X, spawna Y" | Controle total narrativo | Rigido. Dificil de reusar. |

**Minha recomendacao: B com fallback de C para momentos narrativos.**

Quest 01 e LINEAR. O jogador vai da esquerda para a direita por 5 telas. Cada sala tem inimigos especificos. Trigger zones sao a abordagem natural: colisao invisivel no tilemap que dispara o spawn.

Implementacao: retangulos de overlap no tilemap layer "triggers". Quando o player body entra no retangulo, o WaveManager ativa o spawn config associado. Simples, declarativo, testavel.

Para momentos narrativos (Carlao aparecendo, dialogo do tutorial), usar um script sequencial dentro do trigger -- um array de acoes com delays.

```typescript
// Exemplo de config de trigger zone para Wave 1
{
  triggerId: 'corredor-wave1',
  bounds: { x: 640, y: 0, w: 64, h: 270 },
  once: true,  // so dispara uma vez
  spawn: [
    { type: 'burocrata', x: 800, y: GROUND_Y, delay: 0 },
    { type: 'burocrata', x: 860, y: GROUND_Y, delay: 3000 },
  ],
  onEnter: [
    { action: 'showText', text: 'WAVE 1: HORA EXTRA INVOLUNTARIA', duration: 2000 }
  ]
}
```

---

### 2.3 IA dos Zumbis: State Machine Simples vs Behavior Tree

| Opcao | Pros | Contras |
|---|---|---|
| **A: FSM (Finite State Machine)** | Simples, debugavel, performance previsivel | Escala mal com muitos estados. Explosao combinatorial. |
| **B: Behavior Tree** | Extensivel, composavel, industria-padrao para IA de jogos | Overhead de travessia da arvore. Overkill para inimigos simples. |

**Minha recomendacao: A. FSM. Sem pensar duas vezes.**

Os Burocratas-Zumbi da Quest 01 tem TRES estados: `IDLE`, `WALK_TOWARD_PLAYER`, `ATTACK`. O Carlao adiciona `DIALOG` antes de `WALK`. Quatro estados. Behavior tree para isso e como usar um banco de dados relacional para guardar uma lista de compras.

```typescript
enum ZombieState {
  IDLE,
  PATROL,      // andar em fila indiana
  CHASE,       // detectou player, vai em direcao
  ATTACK,      // alcance de ataque, ataca
  STAGGER,     // tomou hit, recuo
  DEAD,        // pool return
}
```

Cada estado e um metodo. O update do zumbi e um switch/case. Sem alocacao, sem travessia de arvore, sem overhead. 30 zumbis em tela a 60fps com folga.

**Quando migrar para Behavior Tree:** Capitulo 1 Quest 06 (boss General de Pijama com 3 fases). Boss fights justificam BT. Inimigos comuns nao.

---

### 2.4 Colisao: Arcade Physics vs Matter.js

**Recomendacao: Arcade. Ponto final.**

Arcade Physics usa AABB (axis-aligned bounding boxes). Retangulos. Rapido, previsivel, sem rotacao. Matter.js adiciona: corpos poligonais, joints, constraints, rotacao, torque, mass, friction, restitution. Nenhuma dessas coisas existe no design da Quest 01.

O que precisamos de colisao:
1. Player vs Ground (chao + plataformas)
2. Player vs Enemies (dano + knockback)
3. Player attack hitbox vs Enemies (vassoura swing)
4. Player vs Items (coleta)
5. Player vs Trigger zones (wave spawning)

Tudo isso e overlap/collide de retangulos. Arcade resolve em O(n) com spatial hash (que o Phaser ja faz internamente). Matter.js resolveria com iteracoes de solver -- 3x mais CPU, zero beneficio.

**Hitbox customizada para a vassoura:** O swing da vassoura nao e o body do player. E um retangulo temporario que spawna na direcao do ataque por ~200ms. Object pool de hitboxes de ataque. Zero `new`, zero GC.

---

### 2.5 State Management: Phaser Scenes vs React State vs Ambos

**Recomendacao: Gameplay state no Phaser. UI state no React. EventBus no meio.**

Ja definido nos docs 19 e 22. Nao mudo nada. Mas preciso ser especifico para Quest 01:

**Estado que vive no Phaser (nunca sai de la):**
- Posicao de todas as entidades (player, zumbis, itens)
- Physics bodies e velocidades
- Estado da FSM de cada zumbi
- Durabilidade da vassoura (contador: 15, 14, 13...)
- Triggers ja ativados (Set de IDs)
- Checkpoint data (posicao do player, HP, itens, waves completadas)

**Estado que o Phaser EMITE para o React via EventBus:**
- HP do player (para a barra de vida no HUD)
- Wave atual (para o wave counter)
- Score (para o display)
- Texto de dialogo (para as caixas de texto narrativas)
- Game over data (kills, score, tempo, causa da morte)
- Tutorial prompts ("seta animada para cima" = React overlay, nao canvas)

**Estado que vive no React (nunca entra no Phaser):**
- App state (menu / playing / paused / gameover)
- Configuracoes de audio (muted, volume)
- Dados de login (se/quando tiver)

**Regra absoluta:** O game loop do Phaser (update a 60fps) NUNCA le estado do React. O React le estado do Phaser via eventos assincrono. Fluxo unidirecional no hot path.

---

### 2.6 Sprites: Atlas vs Spritesheets Individuais

| Opcao | Pros | Contras |
|---|---|---|
| **A: Texture Atlas (recomendado)** | Uma draw call para todos os sprites do mesmo atlas. Menos texture swaps na GPU. Empacotamento eficiente (menos espaco desperdicado). | Requer ferramenta de packing (TexturePacker / free-tex-packer). |
| **B: Spritesheets individuais** | Simples de gerenciar. Um arquivo por personagem. | Multiplas draw calls. Cada spritesheet e uma textura separada na GPU. Espaco desperdicado em frames de tamanho desigual. |

**Recomendacao: A. Texture Atlas. Obrigatorio.**

Para Quest 01, precisamos de sprites de: Ze (idle, walk, jump, attack, hit, crouch), Burocrata-Zumbi (idle, walk, attack, stagger, death), Carlao (idle, walk, dialog, attack, death), itens (vassoura, sanduiche, tablet, cracha). Tudo isso cabe em UM atlas de 1024x1024 (talvez 2048x1024 se os frames forem generosos).

Um atlas = uma texture bind na GPU = todas as sprites renderizadas em UMA draw call via batching do Phaser. Em mobile barato (Mali-G52, Adreno 610), texture swaps sao o gargalo principal. Minimizar texturas e a otimizacao mais impactante que existe.

**Ferramenta:** free-tex-packer (open source) ou TexturePacker (pago, melhor). Output: PNG + JSON (Phaser format). Integrar no build com script npm.

---

### 2.7 Audio: Howler.js vs Phaser Sound Manager

| Opcao | Pros | Contras |
|---|---|---|
| **A: Phaser Sound Manager** | Integrado. Gerencia lifecycle com scenes. Suporta WebAudio + HTML5 fallback. Zero deps extras. | API menos ergonomica que Howler. Spatial audio limitado. |
| **B: Howler.js** | API limpa. Sprite audio (multiplos sons num arquivo). Spatial audio. Comprovado. | Dependencia extra (~10KB). Lifecycle desacoplado do Phaser -- precisa gerenciar manualmente. |

**Recomendacao: A. Phaser Sound Manager.**

Quest 01 precisa de: musica de fundo (MPB distorcida), SFX de hit (carimbo), SFX de morte do Carlao (notificacao Twitter), SFX de ambiente (vidro quebrando, helicoptero). Nada disso requer spatial audio ou sprite audio sofisticado.

Phaser Sound Manager ja faz tudo isso. Adicionar Howler e adicionar uma dependencia para resolver um problema que nao existe. Quando e se precisarmos de spatial audio (inimigos fora da tela com som direcional), revisitamos. Nao agora.

**Formato:** OGG (primario, melhor compressao, suportado em tudo menos Safari legacy) + MP3 (fallback Safari). Phaser resolve o fallback automaticamente com array de sources.

---

## 3. PERFORMANCE BUDGET

### 3.1 Target

| Metrica | Target | Justificativa |
|---|---|---|
| **FPS** | 60fps estavel em desktop, 30fps minimo em mobile | Quest 01 e tutorial. Se travar aqui, o jogador desinstala. |
| **Hardware minimo desktop** | Chrome 100+, qualquer GPU integrada pos-2018 | WebGL 1.0 e suficiente. Phaser 3.88 roda em WebGL 1. |
| **Hardware minimo mobile** | Galaxy A06 (Mali-G52), iPhone SE 2020 | Pior caso realista do publico brasileiro. |
| **Orientacao** | Landscape obrigatorio. Lock via Screen Orientation API. | Side-scroller em portrait e ilegivel. |

### 3.2 Memory Budget

| Recurso | Budget | Nota |
|---|---|---|
| **Atlas de sprites (Quest 01)** | 2MB (1 atlas 2048x1024 RGBA) | Ze + Burocratas + Carlao + itens + VFX |
| **Tilemap + tileset** | 500KB | 5 telas de 120 tiles x 17 tiles = 10.200 tiles |
| **Backgrounds parallax** | 1.5MB (4-5 imagens) | Interior do Ministerio, janelas com Esplanada |
| **Audio total** | 2MB | ~1MB musica OGG loop + ~1MB SFX |
| **JS bundle (Phaser + React + game code)** | 600KB gzipped | Phaser ~350KB gzip, React ~45KB gzip, game ~100KB |
| **TOTAL em memoria** | < 40MB runtime | Galaxy A06 tem 2-3GB RAM, Chrome consome ~200MB base. 40MB e seguro. |

### 3.3 Loading Time

| Metrica | Target |
|---|---|
| **First Meaningful Paint** | < 1.5s (logo + progress bar) |
| **Gameplay ready** | < 4s em 4G (download ~2Mbps efetivo) |
| **Total asset size** | < 7MB (pre-gzip) / < 4MB (gzip) |

**Estrategia de loading para Quest 01:**
1. BootScene carrega APENAS logo + progress bar (~20KB). Renderiza em <500ms.
2. PreloadScene carrega tudo o resto com barra de progresso visual.
3. SEM lazy loading por area -- Quest 01 e curta (5 telas). Carregar tudo upfront e mais simples e evita hitches durante gameplay.

---

## 4. ENGINEERING PRINCIPLES PARA QUEST 01

### P1: Zero alocacoes no game loop

Nenhum `new`, nenhum array literal, nenhum object spread no `update()`. Tudo pre-alocado. Pools para zumbis, hitboxes de ataque, particulas de VFX, textos flutuantes. O GC do V8 e geracional e rapido, mas um GC pause de 16ms em 60fps e um frame perdido. Nao aceito.

### P2: Frame-perfect input

O pulo precisa responder no frame EXATO em que o botao e pressionado. Nao no proximo frame, nao com 1 frame de delay. Input polling no inicio do update(), antes de qualquer logica de fisica. Jump buffer de 100ms (se o jogador apertar pulo 100ms antes de pousar, o pulo acontece automaticamente ao pousar). Coyote time de 80ms (se o jogador pular ate 80ms depois de sair da plataforma, o pulo ainda conta).

### P3: Hitboxes menores que os sprites

A hitbox de dano do Ze deve ser 60-70% da largura do sprite. Se o sprite do Ze tem 24px de largura, a hitbox tem 16px. O jogador SENTE que "quase nao pegou" -- isso e justo. Hitbox do ataque de vassoura pode ser mais generosa (110% do visual) para dar satisfacao.

### P4: Knockback e hitstop antes de tudo

Quando Ze bate num zumbi: 3 frames de hitstop (o jogo CONGELA por 50ms). Quando Ze leva hit: knockback de 180px/s com decay de 0.85x por frame + invencibilidade de 1200ms com sprite piscando. Sem hitstop, combate nao tem peso. Doom 1993 tinha hitstop. Nao e opcional.

### P5: State nunca undefined

Toda variavel de gameplay tem valor inicial explicito. Nenhum `undefined` em runtime. TypeScript strict mode: `strict: true`, `noUncheckedIndexedAccess: true`, `exactOptionalPropertyTypes: true`. Se o compilador reclama, o codigo esta errado.

### P6: O dialogo narrativo nao pausa o game loop

Caixas de texto do Ze ("Isso... nao e manifestacao normal") aparecem como overlays DOM (React) enquanto o jogo continua rodando. O jogador NAO e interrompido. Se quiser ler, le. Se quiser ignorar e correr, corre. A unica excecao e o encontro do Carlao, que tem um trigger zone que spawna o Carlao e mostra o dialogo dele -- mas mesmo ai, o jogador pode atacar durante o dialogo.

---

## 5. O QUE CORTAR E O QUE NAO CORTAR

### NAO CORTAR (engenharia de verdade aqui)

| Feature | Motivo |
|---|---|
| **Pulo + plataformas (gravity ON)** | E o primeiro momento de aprendizado. Sem isso, o tutorial nao funciona. |
| **Hitstop + knockback** | Sem game feel, o jogo parece flash game de 2006. |
| **Object pooling (zumbis + hitboxes + VFX)** | GC pause em mobile mata. Nao e otimizacao prematura, e requisito. |
| **Texture atlas** | Uma draw call vs seis. Em Mali-G52, isso e a diferenca entre 60fps e 40fps. |
| **Checkpoint na Wave 3** | O doc de quest design define checkpoint na escada rolante. Implementar e trivial (serializar state em objeto). Nao implementar e perder jogadores frustrados. |
| **Durabilidade da vassoura** | Mecanica core. Ze aprende que armas quebram. Sao 2 variaveis (durability, maxDurability) e 1 condicional. |

### CORTAR SEM REMORSO (shortcut aceitavel)

| Feature | O que fazer em vez disso |
|---|---|
| **Stealth completo (agachado = invisivel)** | Simplificar: agachar reduz a hitbox verticalmente. Zumbis que estao atras de mesa nao detectam jogador agachado. Nao precisa de "cone de visao" nem "detection meter". Bool: `isCrouching ? skipDetection : normalDetection`. |
| **Carlao como "mini-boss" com IA especial** | Carlao e um Burocrata-Zumbi com HP=5 em vez de HP=3 e um trigger de dialogo. Mesma FSM, stats diferentes. Nao merece classe propria. Config diferente na mesma classe. |
| **Background interativo (fotos de presidentes, post-its com siglas)** | Sao tiles decorativos no tilemap. Zero logica. O artista coloca, o Tiled exporta, o Phaser renderiza. |
| **Efeito de tuites voando na morte do Carlao** | Particulas de sprite. 5-8 sprites de "tuite" pre-renderizados disparados como particulas com velocidade aleatoria + rotacao + fade. ParticleEmitter do Phaser faz isso em 10 linhas. Nao precisa de simulacao de Twitter. |
| **Pontuacao (kills x 10 + HP x 5 + bonus tempo)** | Calcular no GameScene.onQuestComplete(). Nao precisa de ScoreSystem separado para Quest 01. Uma funcao pura de 5 linhas. |
| **Bestiario (menu de lore)** | localStorage: `bestiary: ['burocrata-zumbi']`. Listar no menu e um `map()` sobre esse array. Nao e feature de engine. |

---

## 6. RISCOS TECNICOS ESPECIFICOS DA QUEST 01

### Risco 1: Platforming nao previsto na arquitetura base

**Severidade:** ALTA
**Descricao:** Os docs 19 e 22 assumiram gravity zero. Quest 01 tem pulo, mesas como plataformas, escada rolante com plataformas. Implementar platforming em cima de uma arquitetura que nao previa platforming pode gerar cascata de bugs: double jump nao registra, player fica preso em plataformas, colisao one-way falha.

**Mitigacao:** Fazer o platforming PRIMEIRO. Antes de qualquer inimigo, antes de qualquer wave, antes de qualquer narrativa. Player + gravidade + ground + 3 plataformas de teste. Iterar o feel do pulo ate ficar bom. So depois adicionar inimigos. Se o pulo nao estiver bom em 2 dias, reduzir para pulo simples apenas (sem pulo duplo) e redesignar o level.

### Risco 2: Performance em mobile com 6 zumbis simultaneos + parallax

**Severidade:** MEDIA
**Descricao:** Wave 3 (escada rolante) tem 6 Burocratas-Zumbi entrando aos pares. Com parallax de 7 layers + player + 6 zumbis animados + particulas de VFX, o frame budget de 16.6ms (60fps) pode estourar em Galaxy A06.

**Mitigacao:** Profile cedo. Rodar Phaser debug overlay (`this.game.config.physics.arcade.debug = true`) + Chrome DevTools Performance tab no Galaxy A06 real (ou emulado via throttling 4x CPU). Se estourar budget: (a) reduzir parallax layers de 7 para 4 em mobile, (b) reduzir particulas, (c) aceitar 30fps em mobile como target (quest 01 e tutorial, nao boss fight). Nao otimizar especulativamente -- medir primeiro.

### Risco 3: Dialogo + gameplay simultaneo e confuso

**Severidade:** BAIXA-MEDIA
**Descricao:** O design pede que dialogos do Ze e do Carlao aparecam DURANTE o gameplay sem pausar. Se a caixa de texto do dialogo cobre a acao, ou se o jogador nao percebe o texto, a narrativa se perde.

**Mitigacao:** Caixa de texto no BOTTOM da tela (abaixo do player sprite). Semi-transparente. Max 2 linhas. Auto-dismiss em 3 segundos. Se o jogador entra em combate enquanto ha dialogo, o dialogo some instantaneamente (fade 200ms). Prioridade: gameplay > narrativa. Sempre.

### Risco 4: O level e muito curto ou muito longo

**Severidade:** MEDIA
**Descricao:** "5 telas de largura" e vago. Se cada tela tem 480px de viewport logico, sao 2400px de level. O player anda a 120px/s. Isso sao 20 segundos de caminhada pura sem parar. Com combate e exploracolo, 5-7 minutos parece realista. Mas se as waves forem muito faceis (HP 3 = 2 hits de vassoura), o jogador passa voando em 3 minutos.

**Mitigacao:** Construir o level COMPLETO com todas as 5 telas e placeholder art (retangulos coloridos). Cronometrar playtest interno antes de investir em arte final. Se for muito rapido, adicionar 1 wave extra ou aumentar HP dos zumbis para 4. Se for muito lento, remover 1 wave ou reduzir level para 4 telas.

---

## 7. BUILD / CI MINIMO PARA COMECAR

### Ferramentas obrigatorias no dia 1

```bash
# Package manager
node 22 LTS + npm (workspaces)

# Build
vite 5.x (dev server + production build)

# Linting/Formatting
eslint 9 (flat config) + @typescript-eslint
prettier (single quotes, no semicolons -- ou com, nao me importo, so seja consistente)

# Type checking
typescript 5.4+ strict mode

# Atlas packing
free-tex-packer-cli (npm install -D free-tex-packer-cli)
# ou TexturePacker CLI se tiver licenca
```

### Scripts npm essenciais

```json
{
  "dev": "vite",
  "build": "tsc --noEmit && vite build",
  "preview": "vite preview",
  "typecheck": "tsc --noEmit",
  "lint": "eslint src/",
  "pack-atlas": "free-tex-packer --input assets/raw/ --output public/assets/sprites/"
}
```

### CI (GitHub Actions) -- minimo viavel

```yaml
name: CI
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci
      - run: npm run typecheck
      - run: npm run lint
      - run: npm run build
```

Sem testes unitarios no dia 1. Nao porque testes sao opcionais -- porque o ROI de testar game logic (posicao de sprites, FSM transitions, colisao) com Jest e pessimo. A unica "test suite" que importa no dia 1 e: **roda no browser? roda no celular? 60fps?** Isso se testa abrindo o jogo.

Testes automatizados entram quando tivermos: (a) logica pura separada do Phaser (score calculation, wave config parsing, damage formulas), (b) um sistema de replay para testar gameplay deterministicamente. Nao no dia 1.

### Deploy

Cloudflare Pages. Free tier. Push to main = deploy automatico. Custom domain. SSL. CDN global. Zero config de servidor. O jogo e 100% client-side para Quest 01 -- nao precisa de backend.

---

## 8. RESUMO: PRIMEIROS 5 DIAS DE TRABALHO

| Dia | Entrega | Criterio de sucesso |
|---|---|---|
| **D1** | Scaffold: Vite + React + Phaser. BootScene + PreloadScene com placeholder. EventBus configurado. HUD overlay vazio. | `npm run dev` abre browser com canvas preto do Phaser + React rendering. |
| **D2** | Player com gravity, pulo, movimento horizontal. 3 plataformas de teste (retangulos). Camera follow. | Ze (retangulo azul) anda, pula, pousa em plataformas. Feel do pulo esta bom. |
| **D3** | Tilemap do level completo (placeholder art). 5 telas. Trigger zones. Parallax basico (2 layers). | Camera segue player por todo o level. Triggers disparam console.log. |
| **D4** | Burocrata-Zumbi (FSM: IDLE -> CHASE -> ATTACK -> STAGGER -> DEAD). Pool de 8. Colisao player vs zumbi. Vassoura com durabilidade. Hitstop + knockback. | Ze mata zumbi com vassoura. Vassoura quebra apos 15 hits. Ze continua com soco. Sente BOM. |
| **D5** | Waves 1-3 com trigger zones. HP bar + wave counter no HUD. Checkpoint na Wave 3. Carlao como Burocrata com HP=5 e trigger de dialogo. Game over + restart. | Jogavel do inicio ao fim. 5-7 minutos. Cronometrado. |

Arte placeholder ate D5. Sprites reais entram depois. O gameplay vem primeiro. Se nao for divertido com retangulos, nao vai ser divertido com pixel art.

---

> *"Ship the fun. Ship it ugly. Ship it now. Polish is what you do AFTER you know the game works."*
