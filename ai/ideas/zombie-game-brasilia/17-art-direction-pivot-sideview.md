# ZUMBIS DE BRASILIA -- PIVOT DE ART DIRECTION: Side-View Metal Slug
### Andre Guedes -- Diretor Criativo | Abril 2026

---

> *"Eu olhei pro preview top-down e pensei: 'Cadê o meu personagem? Cadê a cara grotesca dele? Cadê o queixão, a veia estourando, o terno rasgado?' Tava tudo lá, em 16 pixels de altura, invisivel como promessa de campanha. O jogador precisa VER o horror. Precisa VER a caricatura. Precisa VER o chinelo acertando a cara do zumbi. De cima, o máximo que você vê é o brilho da careca do Xandão. De lado, você vê o bicho inteiro. E é isso que a gente vai fazer."*

---

# PARTE 0 -- POR QUE A MUDANCA

## O Problema do Top-Down

O preview atual (960x640px, tiles 16x16, visao top-down) tem um problema fatal para o estilo Andre Guedes: **voce nao ve os personagens**.

O que define o meu trabalho sao CARICATURAS. Narizes enormes. Bocas desproporcionais. Olhos arregalados. Queixoes. Veias saltando. Togas rasgadas. Ternos baratos estourando nos ombros. Tudo isso desaparece quando o personagem tem 16 pixels de altura visto de cima. Vira um bonequinho generico. Podia ser qualquer jogo de zumbi. E esse jogo nao e qualquer jogo de zumbi -- e o MEU jogo de zumbi.

Metal Slug resolveu isso ha 30 anos: camera de lado, personagem grande, cenario rolando atras. Voce ve a expressao do soldado, ve o tanque explodindo, ve cada bala. E exatamente isso que a gente precisa. So que em vez de soldados, sao cidadaos brasileiros. Em vez de tanques, sao carros de som com jingle de campanha. E em vez de balas, sao chinelos, urnas e press releases.

## O Que Muda

| Aspecto | ANTES (Top-Down) | DEPOIS (Side-View) |
|---|---|---|
| **Perspectiva** | Vista de cima, levemente isometrica | Vista lateral (side-scroller) |
| **Tile size** | 16x16px | 16x16px (chao) / backgrounds em camadas |
| **Tamanho do personagem** | ~16-24px (perdido no mapa) | 48-64px (protagonista da tela) |
| **Cenario** | Mapa completo visivel, scroll 2D | Parallax layers, scroll horizontal |
| **Esplanada** | Vista aerea como planta baixa | Vista do nivel da rua, predios ao fundo |
| **Ministerios** | Retangulos vistos de cima | Fachadas brutalistas em perspectiva lateral |
| **Congresso** | Silhueta distante (128x48px) | Silhueta IMPONENTE no horizonte (320x120px) |
| **Espelho D'Agua** | Retangulo azul-verde no mapa | Reflexo no chao com parallax proprio |
| **Referencia visual** | Vampire Survivors / Crimsonland | Metal Slug / Contra / Dead Ahead |

## O Que NAO Muda

- Paleta de cores (color-palette.md continua 100% valida)
- Estilo de traco grotesco (Andre Guedes permanece a referencia)
- Tom horror-comedia
- Narrativa dos 3 atos
- Gameplay de horde survival (so muda a perspectiva, nao o genero)
- Phaser 3 como engine
- Assets de particulas (gas, santinhos, papel)
- HUD layout (adapta mas mantem os mesmos elementos)
- Audio e bordoes

---

# PARTE 1 -- A NOVA PERSPECTIVA VISUAL

## 1.1 Camera: Posicao, Angulo e Zoom

### Posicao da Camera
A camera esta posicionada ao **nivel dos olhos do personagem**, levemente acima. Imagine voce parado na Esplanada dos Ministerios olhando para o horizonte. O Congresso Nacional esta la ao fundo, com as duas cupulas recortadas contra o ceu laranja-sangue. Os blocos dos ministerios se erguem dos dois lados como monolitos brutalistas. O asfalto do Eixo Monumental se estende a sua frente. Zumbis de terno vem cambaleando pela rua.

### Angulo
- **Angulo horizontal:** 0 graus (perfeitamente lateral, como Metal Slug)
- **Angulo vertical:** Levemente acima da linha do horizonte (~5-10 graus para baixo), mostrando um pouco mais do chao do que do ceu
- **Sem rotacao:** A camera nunca gira. O mundo e uma faixa horizontal infinita

### Zoom Level
- **Viewport (resolucao logica):** 480 x 270px (ratio 16:9)
- **Escala de renderizacao:** 2x ou 3x (960x540 ou 1440x810 na tela)
- **O personagem ocupa ~18-24% da altura da tela** (48-64px num viewport de 270px)
- **Comparacao Metal Slug:** Os soldados do Metal Slug tem ~40px de altura num viewport de ~224px = ~18% da tela. Nos vamos no range de 18-24% dependendo do personagem

### Scroll
- **Horizontal:** Scroll continuo, camera segue o jogador
- **Vertical:** Scroll minimo (o chao e relativamente plano, com leves desniveis)
- **Direcao primaria:** Esquerda para direita (o jogador avanca em direcao ao Congresso)
- **Backtrack:** Permitido, mas a camera incentiva avanco (zumbis spawnam mais atras)

```
Viewport 480x270 (logico):

     Ceu laranja-sangue + nuvens toxicas
     _______________________________________________
    |                                               |  0px
    |   [Congresso silhueta ao fundo]               |  ~40px
    |                                               |
    |  [Ministerio]          [Ministerio]           |  ~80-160px
    |  [Fachada L]           [Fachada R]            |
    |                                               |
    |    Arvores secas, postes, placas              |  ~160-190px
    |                                               |
    |  ZUMBI    PLAYER    ZUMBI   ZUMBI             |  ~190-230px (ACAO)
    |_________ chao/rua/calcada ____________________|  ~230-250px
    |  detritos, santinhos, sangue-tinta no chao    |  ~250-270px
    |_______________________________________________|
```

## 1.2 Tamanho dos Personagens na Tela

### Protagonista (Cidadao Brasileiro)
- **Altura do sprite:** 48px (tamanho base no canvas ~68px com margem para animacao)
- **Largura base:** ~24-28px (corpo magro, brasileiro comum)
- **Na tela a 2x:** 96px de altura = personagem BEM visivel
- **Na tela a 3x:** 144px de altura = cada veia, cada ruga, cada gota de suor visivel

### Zumbis Comuns (Vereadores, Assessores)
- **Altura:** 48px (mesmo do player, mas posturas diferentes)
- **Variacao:** Vereadores ligeiramente mais baixos (44px), Senadores mais altos (52px)
- **Largura:** Mais largos que o player (ternos estufados, barrigas, ombros inflados)

### Bosses
- **Altura:** 64-96px (1.5x a 2x o tamanho do player)
- **Xandao:** 80px de altura, toga enorme, martelo ultrapassa o sprite
- **Candidato Eterno:** 64px mas com sorriso que ultrapassa a bounding box
- **Presidente da Camara dos Mortos:** 96px, sentado numa cadeira que tem mais 32px

### Comparacao com Metal Slug
| Elemento | Metal Slug (Neo Geo) | Zumbis de Brasilia |
|---|---|---|
| Viewport | 320x224 | 480x270 |
| Soldado player | ~38-42px | 48px |
| Inimigo comum | ~35-40px | 44-52px |
| Boss | ~80-160px | 64-96px |
| Veiculos | ~60-100px | N/A (carros abandonados = cenario) |

## 1.3 Parallax Layers (7 Camadas)

A Esplanada de lado e um espetaculo de profundidade. Sete camadas, cada uma scrollando em velocidade diferente, criando a ilusao de que voce esta caminhando por aquele corredor brutalista interminavel.

### Layer 0 -- Ceu (scrollFactor: 0)
- **Conteudo:** Gradiente laranja-sangue permanente (identico ao anterior)
- **Tamanho:** 480x120px (ocupa ~44% superior do viewport)
- **Scroll:** ZERO. O ceu nao se move. O apocalipse congelou tudo.
- **Efeitos adicionais:**
  - Nuvens toxicas (sprites semi-transparentes, scrollFactor 0.05, muito lento)
  - Pulso de brilho sutil (amplitude 0.95-1.0, frequencia 0.1Hz)
- **Depth:** -1000

### Layer 1 -- Congresso Nacional (scrollFactor: 0.1)
- **Conteudo:** Silhueta do Congresso Nacional em vista FRONTAL
- **Tamanho do sprite:** 320x120px (imponente, domina o horizonte)
- **Posicao:** Centrado no background, base alinhada com linha do horizonte (~pixel 120 do viewport)
- **Scroll:** Muito lento (0.1). O Congresso parece distante, quase inatingivel. Voce anda e anda e ele continua la. Como na vida real.
- **Detalhes visiveis nessa escala:**
  - Cupula concava da Camara (lado esquerdo) -- formato de prato/bowl
  - Cupula convexa do Senado (lado direito) -- formato de domo
  - Torres gemeas entre as cupulas -- retangulos verticais
  - Brilho verde pulsante entre as torres (efeito PointLight)
  - Rampa de acesso com sombras longas
- **Paleta:** `#1A1A18` silhueta, `#3D6B3A` brilho verde, ceu atras
- **Depth:** -900

### Layer 2 -- Ministerios Distantes (scrollFactor: 0.25)
- **Conteudo:** Silhuetas dos blocos ministeriais mais distantes
- **Tamanho:** Blocos de 80x100px cada, 3-4 visiveis ao mesmo tempo
- **Posicao:** Base na linha do horizonte, topos em ~pixel 60
- **Scroll:** Lento-medio. Os ministerios se movem um pouco mais que o Congresso
- **Detalhes visiveis:**
  - Formas retangulares brutalistas (Oscar Niemeyer)
  - Janelas como olhos mortos (retangulos `#1A1A18` em grid regular)
  - Silhueta mais clara que o Congresso (mais perto = mais detalhe)
  - Nenhuma placa legivel nessa distancia
- **Paleta:** `#5C5C55` corpo, `#1A1A18` janelas, `#3A3530` sombras
- **Depth:** -800

### Layer 3 -- Ministerios Proximos (scrollFactor: 0.5)
- **Conteudo:** Fachadas laterais dos ministerios em primeiro plano de fundo
- **Tamanho:** Blocos de 120x160px cada, 1-2 visiveis ao mesmo tempo
- **Posicao:** Base no chao (~pixel 230), topos em ~pixel 70
- **Scroll:** Medio. Estes sao os predios que realmente parecem passar ao lado do jogador
- **Detalhes visiveis nessa escala:**
  - Pilares/colunas brutalistas na base (pilotis de Niemeyer)
  - Janelas individuais distinguiveis (6x4px cada, grid 4x8)
  - Placas satiricas dos ministerios (legivel em 2x scale)
    - "MIN. DA ENROLACAO"
    - "MIN. DO PUXADINHO"
    - "MIN. DA PROMESSA NAO CUMPRIDA"
    - "MIN. DO JEITINHO"
    - "MIN. DA PLANILHA INFINITA"
  - Concreto rachado, manchas de umidade, infiltracoes
  - Portas escuras de onde saem zumbis (spawn points visuais)
  - Janelas quebradas em andares superiores
  - Santinhos grudados na fachada
  - Pichacoes iLegiveis (textura, nao texto real)
- **Paleta:** `#8A8580` concreto, `#1A1A18` janelas, `#2A5A3A` placas, `#F0E8D0` texto
- **Depth:** -600

### Layer 4 -- Objetos de Fundo (scrollFactor: 0.75)
- **Conteudo:** Elementos entre os predios e a rua
- **Tamanho:** Variado (16-64px por objeto)
- **Posicao:** Ao longo da "calcada" entre os ministerios e o chao de acao
- **Scroll:** Rapido-medio. Quase na mesma velocidade do chao
- **Objetos:**
  - Arvores secas do cerrado (troncos retorcidos, sem folhas, 32x48px)
  - Postes de luz tombados (diagonais, 16x48px)
  - Placas de campanha fincadas na grama morta (16x24px)
  - Lixeiras transbordando (16x20px)
  - Cones de transito (8x12px)
  - Bancos de praca destruidos (32x16px)
  - Grades/cercas de obra (segmentos de 32x24px)
  - Carros abandonados (48x24px, parcialmente visivel)
  - Barricadas improvisadas (32x20px)
- **Importante:** Estes objetos NAO tem colisao. Sao puramente decorativos no fundo.
- **Depth:** -400

### Layer 5 -- Chao / Rua (scrollFactor: 1.0)
- **Conteudo:** A superficie onde a acao acontece
- **Tamanho:** Tiles de 16x16px arranjados horizontalmente (tilemap de side-scroller)
- **Altura util:** ~40px de espessura visual (2.5 tiles) do chao como plataforma
- **Scroll:** 1:1 com a camera. E o chao real do jogo.
- **Composicao:**
  - **Superficie (topo do chao):** Asfalto rachado do Eixo Monumental, com faixa amarela desbotada
  - **Transicao:** Borda superior do asfalto com detritos, grama morta invadindo
  - **Subsolo (debaixo da superficie):** Corte transversal mostrando camadas de terra/entulho (estetica de plataforma)
- **Variantes de terreno (ao longo do nivel):**
  - Segmento 1: Calcada de concreto rachado (inicio, area dos ministerios)
  - Segmento 2: Asfalto do Eixo Monumental (area central, mais rapido)
  - Segmento 3: Grama seca invadindo o asfalto (area do Espelho D'Agua)
  - Segmento 4: Concreto cerimonial (area proxima ao Congresso)
- **Propriedades de gameplay:**
  - Superficie plana (sem plataformas elevadas no MVP -- nao e platformer)
  - Speed modifiers por tipo de terreno (identico ao top-down: grama 0.85, asfalto 1.0)
  - Detritos decorativos sobre o chao (santinhos, papeis, sangue-tinta)
- **Depth:** 0

### Layer 6 -- Personagens e Entidades (scrollFactor: 1.0)
- **Conteudo:** Player, zumbis, NPCs, pickups, projeteis
- **Scroll:** 1:1 (mesmo do chao)
- **Y-sort:** NAO necessario em side-view (nao ha profundidade relativa entre entidades no mesmo plano)
- **Z-order:** Baseado em tipo de entidade
  - Pickups/itens no chao: depth 100
  - Zumbis (mais distantes): depth 200
  - Player: depth 300
  - Zumbis (mais proximos, overlap proposital): depth 400
  - Projeteis: depth 500
  - VFX (explosoes, onomatopeias): depth 600-800
- **Depth range:** 100-800

### Layer 7 -- Primeiro Plano / Foreground (scrollFactor: 1.2-1.5)
- **Conteudo:** Elementos na FRENTE da acao, entre a camera e o jogador
- **Tamanho:** Variado
- **Scroll:** MAIS RAPIDO que a camera (parallax invertido, objetos passam depressa)
- **Objetos:**
  - Postes de luz em primeiro plano (silhueta parcial, cortada pela borda inferior)
  - Grade de protecao / alambrado (semi-transparente, alpha 30%)
  - Detritos voando (santinhos maiores, mais perto da camera)
  - Folhagem seca de arvore no canto superior (parcialmente visivel)
- **Efeito:** Da profundidade e sensacao de estar DENTRO do cenario, nao olhando de fora
- **Alpha:** Baixo (20-40%) para nao atrapalhar a jogabilidade
- **Depth:** 900-999 (abaixo do HUD que e 1000+)

```
Diagrama de Parallax (velocidades relativas):

Camera move 100px para direita:

Layer 0 (Ceu):         move 0px     ████████████████████████
Layer 1 (Congresso):   move 10px    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
Layer 2 (Minist.dist): move 25px    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
Layer 3 (Minist.prox): move 50px    ░░░░░░░░░░░░░░░░░░░░░░░
Layer 4 (Obj.fundo):   move 75px    ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
Layer 5 (Chao):        move 100px   ═══════════════════════
Layer 6 (Entidades):   move 100px   [PLAYER] [ZUMBI]
Layer 7 (Foreground):  move 120px   ┃    ┃    ┃    ┃    ┃
```

---

# PARTE 2 -- DIMENSOES DOS NOVOS ASSETS

## 2.1 Viewport e Resolucao

| Parametro | Valor | Notas |
|---|---|---|
| **Resolucao logica (viewport)** | 480 x 270px | Ratio 16:9, pixel-perfect |
| **Escala de renderizacao** | 2x (padrao), 3x (telas grandes) | 960x540 ou 1440x810 |
| **Resolucao na tela (2x)** | 960 x 540px | HD padrao |
| **Resolucao na tela (3x)** | 1440 x 810px | Monitores maiores |
| **Aspect ratio** | 16:9 | Universal (mobile landscape, desktop, tablet) |
| **FPS target** | 60fps | Identico ao anterior |

### Por que 480x270 e nao 480x320?
O formato anterior (480x320) era 3:2, otimizado para top-down. Para side-view, 16:9 e o padrao da industria (Metal Slug XX, Broforce, Dead Ahead). Alem disso, 270px de altura e divisivel por 16 (16.875 tiles -- arredondamos para 17 tiles de altura no viewport) e e um bom balanço entre mostrar ceu suficiente e manter o personagem grande.

## 2.2 Personagens

| Personagem | Altura (px) | Largura (px) | Canvas Total | Notas |
|---|---|---|---|---|
| **Protagonista (Cidadao)** | 48 | 24-28 | 68x68 | Magro, brasileiro comum |
| **Vereador Zumbi** | 44 | 28-32 | 64x64 | Mais baixo, mais largo |
| **Assessor Zumbi** | 48 | 24-28 | 68x68 | Magro, crachas balancando |
| **Senador Vitalicio** | 52 | 36-40 | 72x72 | Alto, gordo, imponente |
| **Lobista** | 48 | 28-32 | 68x68 | Medio, bolsos cheios |
| **Boss: Candidato Eterno** | 64 | 40-44 | 90x90 | Grande, sorriso impossivel |
| **Boss: Xandao** | 80 | 48-52 | 112x112 | Enorme, toga esvoaçante |
| **Boss: Pres. Camara Mortos** | 96 | 64+ | 136x136 | Colossal + cadeira |
| **NPC: Tiozao do Zap** | 44 | 28 | 64x64 | Aliado, chapeu de sol |
| **NPC: Jornalista** | 48 | 24 | 68x68 | Aliado, microfone |

### Sprite Sheets (Animacoes Side-View)

Em side-view, os personagens so precisam de 2 direcoes (esquerda/direita) em vez de 4 ou 8. Isso REDUZ drasticamente o numero de sprites necessarios:

| Animacao | Frames | Direcoes | Total Frames | FPS |
|---|---|---|---|---|
| Idle | 4 | 2 (flip horizontal) | 4 (flip = gratis) | 8 |
| Walk/Run | 6 | 2 (flip) | 6 | 10 |
| Attack (melee) | 4 | 2 (flip) | 4 | 12 |
| Attack (ranged) | 3 | 2 (flip) | 3 | 12 |
| Hit/Damage | 2 | 2 (flip) | 2 | 8 |
| Death | 6 | 1 (sempre cai para o lado) | 6 | 8 |
| **Total por personagem** | | | **~25 frames** | |

**Economia vs top-down:** No top-down com 8 direcoes, seriam ~25 frames x 8 = 200 frames. Em side-view com flip horizontal, sao ~25 frames TOTAL. Reducao de **87.5%** no trabalho de sprite.

## 2.3 Tiles de Chao (Side-Scroller Tileset)

| Parametro | Valor | Notas |
|---|---|---|
| **Tile size** | 16x16px | Mesmo do top-down |
| **Tileset format** | Side-scroller (PixelLab) | Transparencia, sem background |
| **Tiles de superficie** | Topo plano com transicao | Asfalto, concreto, grama |
| **Tiles de preenchimento** | Interior da plataforma | Terra, entulho, concreto cortado |
| **Transition tiles** | Bordas de terreno | Wang tiles side-scroller |
| **Mapa em tiles (por segmento)** | 120 x 17 tiles (1920 x 272px) | Um segmento de nivel |
| **Mapa total (completo)** | 600 x 17 tiles (9600 x 272px) | Nivel inteiro, 5 segmentos |

### Estrutura do Chao (Corte Lateral)

```
Pixel Y no viewport:

190  ┌─────────────────────────────────────┐  ← Linha do chao
     │  Superficie: asfalto/concreto/grama │  16px (1 tile)
206  ├─────────────────────────────────────┤
     │  Transicao: borda superior suja     │  8px (meio tile, overlap)
214  ├─────────────────────────────────────┤
     │  Subsolo: terra/entulho cortado     │  16px (1 tile)
230  ├─────────────────────────────────────┤
     │  Subsolo profundo: mais escuro      │  16px (1 tile)
246  ├─────────────────────────────────────┤
     │  Base: preto/muito escuro           │  24px (ate borda inferior)
270  └─────────────────────────────────────┘
```

## 2.4 Backgrounds (Parallax Layers)

| Layer | Dimensao (px) | Formato | Repetição | Scroll Factor |
|---|---|---|---|---|
| **Ceu (L0)** | 480x120 | Gradiente (codigo) | Estatico | 0 |
| **Nuvens toxicas** | 960x60 | PNG sprite sheet | Loop horizontal | 0.05 |
| **Congresso (L1)** | 320x120 | PNG sprite | Nao repete (unico) | 0.1 |
| **Ministerios dist. (L2)** | 1920x120 | PNG tileable | Loop horizontal | 0.25 |
| **Ministerios prox. (L3)** | 2400x180 | PNG tileable | Loop horizontal | 0.5 |
| **Objetos fundo (L4)** | Sprites individuais | PNG cada | Distribuidos | 0.75 |
| **Chao (L5)** | 9600x80 (tilemap) | Tilemap JSON | Nao repete | 1.0 |
| **Foreground (L7)** | Sprites individuais | PNG cada | Distribuidos | 1.2-1.5 |

### Detalhamento dos Background Sprites

**Congresso Nacional (320x120px) -- Vista Frontal Side-View:**
```
                          ┌──┐ ┌──┐
                          │  │ │  │     Torres gemeas
                    ______│  │ │  │______
                   /      │  │ │  │      \
          ___     / CAMARA│  │ │  │SENADO  \     ___
         /   \   /        │  │ │  │         \   /   \
        | ))) | /         │  │ │  │          \ | ((( |
        |_____|/          └──┘ └──┘           \|_____|
         concavo                                convexo
         (prato)                                (domo)
         
Escala: Muito maior que o top-down. 320px de largura = quase o viewport inteiro.
O Congresso DOMINA o horizonte. Voce sente o peso daquele predio.
Brilho verde pulsante entre as torres (PointLight ampliado).
```

**Bloco Ministerial (120x160px) -- Vista Lateral:**
```
    ┌─────────────────────────┐
    │ ┌──┐ ┌──┐ ┌──┐ ┌──┐   │   Janelas = olhos mortos (#1A1A18)
    │ │  │ │  │ │  │ │  │   │   Grid regular, brutalismo puro
    │ └──┘ └──┘ └──┘ └──┘   │
    │ ┌──┐ ┌──┐ ┌──┐ ┌──┐   │   Concreto rachado (#8A8580)
    │ │  │ │  │ │  │ │  │   │   Manchas de infiltracao
    │ └──┘ └──┘ └──┘ └──┘   │   Santinhos grudados na fachada
    │ ┌──┐ ┌──┐ ┌──┐ ┌──┐   │
    │ │  │ │  │ │  │ │  │   │
    │ └──┘ └──┘ └──┘ └──┘   │
    │                         │   Pilotis (colunas) na base
    │ ║    ║    ║    ║    ║  │   Portas escuras (spawn de zumbis)
    ├─╨────╨────╨────╨────╨──┤
    │  [PLACA DO MINISTERIO]  │   Placa satirica legivel
    └─────────────────────────┘
```

## 2.5 Armas (Side-View)

| Arma | Tamanho Sprite | Notas |
|---|---|---|
| **Chinelo Havaianas** | 16x16 | Acoplada a mao do player, flip com direcao |
| **Vassoura da Esplanada** | 8x32 | Vertical quando idle, horizontal no swing |
| **Urna Eletronica** | 20x16 | Projetil arremessado |
| **Cracha Afiado** | 8x8 | Projetil rapido, shuriken style |
| **Carimbo Protocolo** | 12x12 | Melee, estampa "DEFERIDO" no zumbi |
| **Biblia Blindada** | 14x18 | Escudo/melee combo |
| **Garrafa Velho Barreiro** | 10x16 | Molotov brasileiro |
| **Taco de Golfe Nuclear** | 8x32 | Melee longo alcance |

---

# PARTE 3 -- REDESIGN DA ESTRUTURA DE LAYERS (Phaser 3)

## 3.1 Nova Hierarquia Completa

```
┌─────────────────────────────────────────────────┐
│  LAYER HUD: Interface (Camera separada)          │  depth: 1000+
│  HP, Score, Wave, Combo, Power-ups, Joystick     │  scrollFactor: 0
├─────────────────────────────────────────────────┤
│  LAYER 7: Foreground / Primeiro Plano            │  depth: 900-999
│  Postes proximos, grades, detritos voando        │  scrollFactor: 1.2-1.5
├─────────────────────────────────────────────────┤
│  LAYER 6: VFX                                    │  depth: 600-800
│  Explosoes, onomatopeias, splats, flash          │  scrollFactor: 1.0
├─────────────────────────────────────────────────┤
│  LAYER 6: Entidades                              │  depth: 100-500
│  Player, zumbis, NPCs, pickups, projeteis        │  scrollFactor: 1.0
├─────────────────────────────────────────────────┤
│  LAYER 5: Chao / Tilemap Side-Scroller           │  depth: 0
│  Superficie + subsolo + detritos                 │  scrollFactor: 1.0
├─────────────────────────────────────────────────┤
│  LAYER 4: Objetos de Fundo                       │  depth: -400
│  Arvores, postes, placas, carros abandonados     │  scrollFactor: 0.75
├─────────────────────────────────────────────────┤
│  LAYER 3: Ministerios Proximos                   │  depth: -600
│  Fachadas detalhadas com placas e pilotis        │  scrollFactor: 0.5
├─────────────────────────────────────────────────┤
│  LAYER 2: Ministerios Distantes                  │  depth: -800
│  Silhuetas com janelas                           │  scrollFactor: 0.25
├─────────────────────────────────────────────────┤
│  LAYER 1: Congresso Nacional                     │  depth: -900
│  Silhueta imponente + brilho verde               │  scrollFactor: 0.1
├─────────────────────────────────────────────────┤
│  LAYER 0: Ceu                                    │  depth: -1000
│  Gradiente laranja-sangue + nuvens toxicas        │  scrollFactor: 0
└─────────────────────────────────────────────────┘
```

## 3.2 Implementacao Phaser 3 (Pseudocodigo)

```javascript
class GameScene extends Phaser.Scene {
    create() {
        // === LAYER 0: CEU ===
        this.createSkyGradient();        // fillGradientStyle, scrollFactor(0), depth(-1000)
        this.createToxicClouds();        // ParticleEmitter, scrollFactor(0.05), depth(-995)

        // === LAYER 1: CONGRESSO ===
        this.congress = this.add.image(LEVEL_CENTER_X, HORIZON_Y, 'congresso-sideview');
        this.congress.setScrollFactor(0.1);
        this.congress.setDepth(-900);
        this.createCongressGlow();       // PointLight, pulsante, depth(-899)

        // === LAYER 2: MINISTERIOS DISTANTES ===
        this.distantMinistries = this.add.tileSprite(
            0, HORIZON_Y, LEVEL_WIDTH, 120, 'ministerios-distantes'
        );
        this.distantMinistries.setScrollFactor(0.25);
        this.distantMinistries.setDepth(-800);

        // === LAYER 3: MINISTERIOS PROXIMOS ===
        this.nearMinistries = this.add.tileSprite(
            0, 60, LEVEL_WIDTH, 180, 'ministerios-proximos'
        );
        this.nearMinistries.setScrollFactor(0.5);
        this.nearMinistries.setDepth(-600);

        // === LAYER 4: OBJETOS DE FUNDO ===
        this.bgObjects = this.add.group();
        this.placeBackgroundObjects();   // Arvores, postes, placas
        this.bgObjects.setScrollFactor(0.75);
        this.bgObjects.setDepth(-400);

        // === LAYER 5: CHAO (TILEMAP SIDE-SCROLLER) ===
        const map = this.make.tilemap({ key: 'esplanada-sideview-map' });
        const tileset = map.addTilesetImage('esplanada-sideview', 'esplanada-sideview-tiles');
        this.groundLayer = map.createLayer('ground-surface', tileset, 0, GROUND_Y);
        this.groundLayer.setDepth(0);
        this.subsoilLayer = map.createLayer('ground-subsurface', tileset, 0, GROUND_Y + 16);
        this.subsoilLayer.setDepth(-1);

        // === LAYER 6: ENTIDADES ===
        this.createPlayer();             // depth(300)
        this.createZombiePool();         // depth(200 ou 400)
        this.createPickupPool();         // depth(100)
        this.createProjectilePool();     // depth(500)

        // === VFX ===
        this.createParticleEmitters();   // Gas, santinhos, papel - depth(600-800)
        this.createOnomatopoeiaPool();

        // === LAYER 7: FOREGROUND ===
        this.createForegroundElements(); // depth(900-999), scrollFactor(1.2-1.5)

        // === HUD ===
        this.createHUD();                // Camera separada, depth(1000+)

        // === CAMERA ===
        this.cameras.main.startFollow(this.player, true, 0.1, 0.1);
        this.cameras.main.setBounds(0, 0, LEVEL_WIDTH, 270);
        this.cameras.main.setDeadzone(60, 20); // Zona morta para scroll mais suave
    }

    update(time, delta) {
        // Em side-view NAO precisa de Y-sort!
        // Entidades no mesmo plano = mesma profundidade base
        // Economiza CPU no loop principal
        
        this.waveSystem.update(time, delta);
        this.combatSystem.update(time, delta);
        this.parallaxUpdate(); // Atualiza tileSprite offsets para L2/L3
    }

    parallaxUpdate() {
        // TileSprite parallax manual (para layers que usam tileSprite)
        const camX = this.cameras.main.scrollX;
        this.distantMinistries.tilePositionX = camX * 0.25;
        this.nearMinistries.tilePositionX = camX * 0.5;
    }
}
```

## 3.3 Performance Budget (Side-View vs Top-Down)

| Metrica | Top-Down (anterior) | Side-View (novo) | Diferenca |
|---|---|---|---|
| Tiles no mapa | 2400 (60x40) | ~2040 (120x17) por segmento | -15% |
| Draw calls (background) | 1 | 4-5 (parallax layers) | +4 |
| Draw calls (tilemap) | 1 | 1-2 | +1 |
| Draw calls (entidades) | 1 (atlas) | 1 (atlas) | 0 |
| Draw calls (VFX) | 2-3 | 2-3 | 0 |
| Draw calls (HUD) | 1-2 | 1-2 | 0 |
| Draw calls (foreground) | 0 | 1 | +1 |
| **Total draw calls** | **~7-9** | **~11-14** | +4-5 |
| Particulas max | 65 | 65 | 0 |
| Y-sort por frame | ~70 entidades | 0 (nao necessario) | -70 ops/frame |
| Sprites de personagem | ~200 frames (8 dir) | ~25 frames (2 dir flip) | **-87.5%** |
| **Target FPS** | **60** | **60** | 0 |

**Analise:** O side-view adiciona ~5 draw calls pelos parallax layers, mas ELIMINA o Y-sorting e REDUZ drasticamente o numero de sprites por personagem. Trade-off amplamente positivo.

---

# PARTE 4 -- A VIBE VISUAL: A ESPLANADA VISTA DO CHAO

## Descricao Narrativa (Tom Andre Guedes)

Imagina o seguinte. Voce esta parado no meio do Eixo Monumental. O asfalto debaixo dos seus pes esta rachado como a promessa de um candidato no segundo turno. A faixa amarela da pista -- aquela faixa que deveria separar os sentidos do trafego, mas que nao separa mais nada porque nao tem mais trafego, nao tem mais sentido, nao tem mais nada -- esta desbotada ate virar um borrão cor de mostarda seca.

Voce olha para os lados e os ministerios se erguem como tumulos de concreto. Oscar Niemeyer deve estar se revirando no tumulo DELE, porque aquelas fachadas brutalistas que ele projetou para serem simbolo de modernidade agora parecem os blocos de uma penitenciaria abandonada. As janelas sao buracos pretos. Cada uma delas e um olho morto te observando. Tem santinho de campanha grudado na parede do terceiro andar -- como e que chegou la? Ninguem sabe. Promessa de politico chega em qualquer lugar. A placa na entrada do primeiro bloco, que deveria dizer "Ministerio da Fazenda" ou algo assim, agora diz "MINISTERIO DA ENROLACAO" em letras que parecem ter sido escritas por alguem que ja desistiu de tudo. Debaixo dos pilotis, nas sombras entre as colunas de concreto, voce ve movimento. Algo se arrasta. Algo de terno.

E la no fundo, dominando tudo, aquela coisa. O Congresso Nacional. As duas cupulas -- a concava da Camara, como um prato esperando ser enchido de verba, e a convexa do Senado, como um tumor que cresceu no centro do poder -- recortadas contra um ceu que nao e mais ceu. E um gradiente de laranja-sangue para vermelho queimado para noite eterna. O sol nao se poe em Brasilia. O sol MORREU em Brasilia. E entre as duas torres gemeas do Congresso, um brilho verde pulsa. Lento. Ritmico. Como a respiracao de algo que nao deveria estar respirando. O gas da Emenda 666 sai dali como fumaca de churrasco do inferno. So que em vez de cheiro de picanha, cheira a documento mofado e promessa vencida.

O chao entre voce e o Congresso esta coberto de santinhos eleitorais. Milhares deles. Voando no vento quente do cerrado, grudando nos seus sapatos, formando pequenos montes contra os postes tombados. Cada santinho tem um rosto. Cada rosto tem um sorriso. E cada sorriso e identico ao rigor mortis dos zumbis que estao vindo na sua direcao.

Voce olha pro chinelo na sua mao. Olha pros zumbis de terno. Olha pro Congresso la no fundo.

E pensa: "Nao tinha como o dia de hoje ser pior do que ontem. Mas eu moro no Brasil."

---

# PARTE 5 -- MAPA DO NIVEL (Progressao Horizontal)

## Estrutura do Nivel Completo

O nivel e uma faixa horizontal continua que representa a caminhada do cidadao desde a area dos ministerios ate o Congresso Nacional. Cinco segmentos, cada um com cenario e desafios proprios.

```
DIRECAO DE AVANCO →

[SEGMENTO 1]     [SEGMENTO 2]     [SEGMENTO 3]     [SEGMENTO 4]     [SEGMENTO 5]
Ministerios      Eixo Monumental   Espelho D'Agua    Rampa/Acesso     Congresso
(Waves 1-3)      (Waves 4-7)       (Waves 8-11)      (Waves 12-15)   (Boss Final)
                  
1920px           1920px            1920px            1920px           1920px
= 120 tiles      = 120 tiles       = 120 tiles       = 120 tiles      = 120 tiles
─────────────────────────────────────────────────────────────────────────────────
TOTAL: 9600px = 600 tiles de largura
```

### Segmento 1 -- Area dos Ministerios (0-1920px)

**Background:**
- L2/L3: Ministerios em AMBOS os lados (frente e fundo), criando "corredor"
- L4: Arvores secas, cones, placas de campanha
- Iluminacao: Sombras longas dos predios (escuro nos cantos)

**Chao:**
- Concreto rachado (calcadas) alternando com grama morta
- Detritos: Santinhos densos, crateras pequenas

**Gameplay:**
- Waves 1-3: Vereadores e Assessores saindo das portas dos ministerios
- Ritmo: Introdutorio, tutorial implicito

### Segmento 2 -- Eixo Monumental (1920-3840px)

**Background:**
- L2/L3: Ministerios se afastam, horizonte se abre
- L4: Postes tombados, carros abandonados, barricadas
- Iluminacao: Mais aberta, ceu mais visivel

**Chao:**
- Asfalto puro com faixa amarela desbotada
- Speed boost: Velocidade maxima do player neste terreno
- Detritos: Vidro de carro, metal retorcido

**Gameplay:**
- Waves 4-7: Senadores, Lobistas, inimigos mais rapidos
- Sem cobertura: Area aberta, kiting e mobilidade

### Segmento 3 -- Espelho D'Agua (3840-5760px)

**Background:**
- L2/L3: Congresso começa a crescer no horizonte
- L4: Margens do Espelho D'Agua, vegetacao morta
- Efeito especial: Reflexo na agua (sprite invertido do ceu com tint verde)

**Chao:**
- Concreto cerimonial + bordas de agua turva
- Zona de agua: Kill zone (zumbis podem ser empurrados para dentro)
- Detritos: Peixes mortos, garrafas, documentos encharcados

**Gameplay:**
- Waves 8-11: Servidores Fantasma, Ministra da Economia
- Mecanica de posicionamento: Empurrar zumbis na agua

### Segmento 4 -- Rampa de Acesso (5760-7680px)

**Background:**
- L1: Congresso ENORME, ocupa 2/3 do horizonte
- L3: Laterais da rampa cerimonial, pilares
- Gas verde muito denso (particulas 200% densidade)

**Chao:**
- Rampa de concreto (leve inclinacao visual, sem efeito de gameplay)
- Tapete vermelho rasgado no centro
- Detritos: Crachas, documentos da Emenda 666

**Gameplay:**
- Waves 12-15: Todas as bancadas juntas, caos total
- Fragmentos narrativos finais
- Gas reduz visibilidade (efeito de fog parcial)

### Segmento 5 -- Congresso (7680-9600px)

**Background:**
- Congresso ocupa o fundo INTEIRO (nao e mais silhueta, e a fachada completa)
- Interior do plenario (transicao de exterior para interior)
- Brilho verde maximo, pulso acelerado

**Chao:**
- Carpete vermelho + piso de marmore rachado
- Cadeiras do plenario como obstaculos/cobertura

**Gameplay:**
- Boss Final: Presidente da Camara dos Mortos
- Sessao de votacao zumbi

---

# PARTE 6 -- ESPECIFICACOES TECNICAS PARA GERACAO DE ASSETS

## 6.1 Tilesets Side-Scroller (PixelLab create_sidescroller_tileset)

### Tileset SS01 -- Asfalto Rachado
```
lower_description: "cracked dark asphalt road surface, urban decay, 
    potholes and cracks, dirty muted gray-brown tones, 
    underground comix aesthetic, rough texture"
transition_description: "dead yellow grass and debris invading from top, 
    broken concrete edge, scattered campaign flyers, 
    dirty straw-colored dead vegetation"
tile_size: { width: 16, height: 16 }
transition_size: 0.3
detail: "highly detailed"
outline: "selective outline"
shading: "detailed shading"
```

### Tileset SS02 -- Concreto Cerimonial
```
lower_description: "cracked gray concrete sidewalk, brutalist government 
    district pavement, stained and weathered, dark patches"
transition_description: "dead grass tufts and scattered papers on surface, 
    campaign flyers, dirt accumulation at edges"
tile_size: { width: 16, height: 16 }
transition_size: 0.25
detail: "highly detailed"
outline: "selective outline"
shading: "detailed shading"
```

### Tileset SS03 -- Grama Morta
```
lower_description: "dry dead earth and subsoil, cracked tan dirt,
    exposed roots, construction rubble mixed with soil"
transition_description: "dead straw-yellow grass, dry cerrado vegetation,
    tufts of dead plants, bare patches of dirt"
tile_size: { width: 16, height: 16 }
transition_size: 0.4
detail: "highly detailed"
outline: "selective outline"
shading: "detailed shading"
```

### Tileset SS04 -- Carpete Vermelho (Congresso Interior)
```
lower_description: "dark marble floor cracked and stained, 
    formal government building interior, debris and dust"
transition_description: "torn dark red carpet, VIP parliament carpet 
    ripped and stained, woven texture visible at edges"
tile_size: { width: 16, height: 16 }
transition_size: 0.35
detail: "highly detailed"
outline: "selective outline"
shading: "detailed shading"
```

## 6.2 Map Objects Side-View (PixelLab create_map_object)

### Congresso Nacional (Background)
```
description: "Brazilian National Congress building front view silhouette, 
    two distinctive domes (one concave bowl shape, one convex dome), 
    twin towers between domes, Oscar Niemeyer brutalist architecture, 
    sinister green glow between towers, dark imposing government building,
    pixel art, dark silhouette against apocalyptic orange sky,
    thick irregular outlines, underground comix style"
view: "side"
width: 320
height: 120
detail: "high detail"
outline: "single color outline"
shading: "detailed shading"
```

### Bloco Ministerial Proximo
```
description: "brutalist government ministry building side view, 
    rectangular concrete block with dark empty window grid,
    pilotis columns at ground level, cracked concrete facade,
    campaign flyers stuck to walls, satirical sign at entrance,
    Oscar Niemeyer inspired architecture, decay and abandonment,
    pixel art, thick outlines, underground comix style"
view: "side"
width: 120
height: 160
detail: "high detail"
outline: "single color outline"
shading: "detailed shading"
```

### Bloco Ministerial Distante
```
description: "distant brutalist government building silhouette side view,
    rectangular shape with small dark window grid, simplified detail,
    concrete gray tones, atmospheric perspective making it slightly 
    faded and blue-gray, pixel art"
view: "side"
width: 80
height: 100
detail: "medium detail"
outline: "selective outline"
shading: "medium shading"
```

### Arvore Seca do Cerrado
```
description: "dead twisted cerrado tree, bare branches, no leaves,
    dry Brazilian savanna tree, gnarled trunk, apocalyptic wasteland,
    pixel art, dark silhouette style, underground comix"
view: "side"
width: 32
height: 48
detail: "medium detail"
outline: "single color outline"
shading: "basic shading"
```

### Poste de Luz Tombado
```
description: "fallen street lamp post, broken at base, leaning diagonal,
    cracked light fixture, exposed wires, urban decay,
    pixel art, side view"
view: "side"
width: 48
height: 48
detail: "medium detail"
outline: "single color outline"
shading: "basic shading"
```

### Carro Abandonado
```
description: "abandoned damaged car side view, flat tires, broken windows,
    covered in dust and campaign stickers, urban apocalypse,
    compact Brazilian car (Gol/Palio style), pixel art"
view: "side"
width: 48
height: 32
detail: "medium detail"
outline: "single color outline"
shading: "medium shading"
```

### Placa de Campanha
```
description: "political campaign sign on stick planted in dead grass,
    torn poster with faded candidate face, side view,
    election propaganda sign, Brazilian style, pixel art"
view: "side"
width: 16
height: 32
detail: "low detail"
outline: "single color outline"
shading: "basic shading"
```

### Barricada Improvisada
```
description: "improvised barricade made of office furniture and sandbags,
    overturned desks, filing cabinets, government office debris,
    side view, apocalypse survival, pixel art"
view: "side"
width: 48
height: 32
detail: "medium detail"
outline: "single color outline"
shading: "medium shading"
```

## 6.3 Personagens Side-View (PixelLab create_character)

### Protagonista -- Cidadao Brasileiro
```
name: "Cidadao Brasileiro"
description: "ordinary Brazilian citizen, thin male, messy dark hair, 
    worried expression, sweat drops, cheap polo shirt slightly torn,
    jeans, flip flops (chinelo), holding a broom as weapon,
    grotesque caricature style, thick outlines, exaggerated features,
    Robert Crumb inspired character design"
view: "side"
size: 48
body_type: "humanoid"
proportions: '{"type": "preset", "name": "cartoon"}'
detail: "high detail"
outline: "single color black outline"
shading: "detailed shading"
mode: "pro"
```

### Vereador Zumbi
```
name: "Vereador Zumbi"
description: "zombie politician in cheap ill-fitting suit, green-tinted skin,
    sunken eyes glowing green, dangling ID badge on lanyard,
    arms outstretched reaching forward, torn suit jacket,
    grotesque caricature, exaggerated jaw, undead Brazilian politician,
    thick outlines, underground comix style"
view: "side"
size: 44
body_type: "humanoid"
proportions: '{"type": "preset", "name": "cartoon"}'
detail: "high detail"
outline: "single color black outline"
shading: "detailed shading"
mode: "pro"
```

### Boss: Xandao
```
name: "Xandao - STF Boss"
description: "giant muscular bald zombie judge in flowing black robe,
    enormous jaw, tiny furious red eyes, thick furrowed brow,
    bulging biceps bursting through judicial robe, holding massive 
    gavel weapon, veins pulsing on bald head and neck,
    imposing grotesque caricature, underground comix style,
    thick black outlines, exaggerated proportions"
view: "side"
size: 80
body_type: "humanoid"
proportions: '{"type": "custom", "head_size": 1.8, "shoulder_width": 1.6, "arms_length": 1.2, "legs_length": 0.8}'
detail: "high detail"
outline: "single color black outline"
shading: "detailed shading"
mode: "pro"
```

---

# PARTE 7 -- MIGRACOES E COMPATIBILIDADE

## 7.1 O Que Pode Ser Reaproveitado do Top-Down

| Asset | Reaproveitavel? | Como |
|---|---|---|
| **color-palette.md** | SIM, 100% | Paleta nao depende de perspectiva |
| **Particulas (gas, santinhos, papel)** | SIM, 100% | Particulas sao agniosticas de perspectiva |
| **Audio/bordoes** | SIM, 100% | Audio nao depende de visual |
| **Narrativa (09-storytelling)** | SIM, 100% | Historia nao muda |
| **Specs de armas (dano, rate, etc)** | SIM, 90% | Numeros permanecem, sprites mudam |
| **HUD design** | SIM, 80% | Layout adapta para 16:9 mas conceito mantem |
| **Tiles top-down gerados** | NAO | Perspectiva incompativel |
| **Sprites de personagem top-down** | NAO | Precisam de redesign side-view |
| **Layout do mapa (layout-spec.md)** | NAO | Mapa agora e linear horizontal |
| **Layer spec (layer-spec.md)** | PARCIAL | Conceito de layers mantem, implementacao muda |

## 7.2 Arquivos Que Precisam de Atualizacao

| Arquivo | Status | Acao |
|---|---|---|
| `tileset-spec.md` | SUBSTITUIR | Novo spec para side-scroller tilesets |
| `layer-spec.md` | SUBSTITUIR | Este documento (17) substitui |
| `layout-spec.md` | SUBSTITUIR | Novo layout horizontal (Parte 5 deste doc) |
| `art-prompts.md` | SUBSTITUIR | Novos prompts para side-view (Parte 6 deste doc) |
| `atmosphere-spec.md` | ATUALIZAR | Emitters continuam, posicoes mudam |
| `sprite-spec.md` (personagens) | SUBSTITUIR | Side-view = novo design por personagem |
| `generated/*` | REGENERAR | Todos os PNGs devem ser refeitos em side-view |

## 7.3 Ordem de Geracao dos Novos Assets

Prioridade de producao para o MVP side-view:

```
FASE 1 (Dia 1-2): Foundation
├── 1.1 Gerar tilesets side-scroller (SS01-SS04)
├── 1.2 Gerar Congresso Nacional side-view (320x120)
├── 1.3 Gerar 2 blocos ministeriais (proximo + distante)
└── 1.4 Montar parallax basico (layers 0-3 + 5)

FASE 2 (Dia 3-4): Personagens
├── 2.1 Gerar protagonista (Cidadao) side-view 48px
├── 2.2 Gerar Vereador Zumbi side-view 44px
├── 2.3 Gerar Assessor Zumbi side-view 48px
└── 2.4 Testar escala: personagem no cenario

FASE 3 (Dia 5-6): Polish
├── 3.1 Gerar objetos de fundo (arvores, postes, carros)
├── 3.2 Gerar foreground elements
├── 3.3 Adaptar emitters de particulas para nova viewport
├── 3.4 Gerar armas side-view
└── 3.5 Preview completo do novo visual
```

---

# PARTE 8 -- CHECKLIST DE MIGRACAOO

- [ ] Criar tilesets side-scroller via PixelLab (SS01-SS04)
- [ ] Criar Congresso Nacional side-view (320x120px)
- [ ] Criar blocos ministeriais side-view (proximo 120x160, distante 80x100)
- [ ] Criar protagonista side-view (48px, modo pro)
- [ ] Criar Vereador Zumbi side-view (44px)
- [ ] Criar Assessor Zumbi side-view (48px)
- [ ] Criar Boss Xandao side-view (80px)
- [ ] Criar objetos de fundo side-view (arvores, postes, carros, placas, barricadas)
- [ ] Criar foreground elements
- [ ] Montar preview do parallax completo (todas as 7 layers)
- [ ] Adaptar emitters de particulas para viewport 480x270
- [ ] Atualizar HUD layout para 16:9
- [ ] Criar tilemap side-scroller no Tiled (ou equivalente)
- [ ] Atualizar GameScene.ts para nova estrutura de layers
- [ ] Testar performance (target: 60fps, max 14 draw calls)
- [ ] Validar que personagens sao VISIVEIS e RECONHECIVEIS a 2x scale
- [ ] Validar que humor/caricatura funciona na nova escala
- [ ] Atualizar tileset-spec.md para side-scroller
- [ ] Atualizar layout-spec.md para progressao horizontal
- [ ] Atualizar atmosphere-spec.md para novo viewport

---

# NOTA FINAL DO DIRETOR CRIATIVO

Essa mudanca nao e um capricho estetico. E uma questao de IDENTIDADE. O meu trabalho -- o que define "Zumbis de Brasilia" como marca -- sao as CARAS. Sao as expressoes. E o queixao do Xandao, o sorriso congelado do Candidato Eterno, o brilho de desespero nos olhos do cidadao segurando um chinelo contra uma horda de senadores vitalicios. Nada disso aparece em 16 pixels vistos de cima.

Metal Slug provou ha 30 anos que side-view e o formato perfeito para acao com personagens expressivos. Broforce provou de novo. Dead Ahead provou com zumbis. Agora nos vamos provar com politicos-zumbis brasileiros.

O Congresso Nacional visto do nivel da rua, com aquelas cupulas recortadas contra o ceu de sangue, com o gas verde saindo dentre as torres -- isso e CINEMA. Isso e um quadro que o jogador vai pausar pra tirar screenshot. Isso e o fundo perfeito pra foto de score compartilhada no WhatsApp.

E quando o jogador ver o Xandao entrando em cena -- 80 pixels de puro grotesco, careca brilhando, toga esvoaçando, martelo do tamanho de um carro -- ninguem vai perguntar "o que e esse bonequinho?". Todo mundo vai saber exatamente quem e. E vai rir. E vai ter medo. E vai compartilhar.

Esse e o jogo que eu quero fazer.

*-- Andre Guedes, Abril de 2026*
