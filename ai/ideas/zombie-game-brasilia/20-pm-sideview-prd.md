# ZUMBIS DE BRASILIA — PRD Side-View (Metal Slug Style)
### Product Requirements Document | Browser Game | Post-Pivot | Abril 2026

**Versao:** 2.0 (Side-View Pivot)
**Base:** PRD 13 (MVP Web) + Art Direction 17 (Side-View)
**Stack:** React + Phaser 3.88, Arcade Physics, Object Pooling, Backend para login e ranking
**PM:** Shigeru Miyamoto (perspectiva)

---

> *"Um jogo atrasado eventualmente sera bom, mas um jogo ruim sera ruim para sempre. Para um MVP, a regra e diferente: um loop perfeito lancado hoje vale mais do que um jogo completo lancado nunca. A diferenca e que voce nao pode comprometer o core loop. Nem um frame."*

---

## POR QUE O PIVOT MUDA O PRD

O PRD anterior (13-pm-mvp-web-prd.md) foi escrito para um jogo top-down estilo Vampire Survivors. O pivot para side-view Metal Slug nao e apenas uma mudanca estetica. Ele muda:

- **O core loop micro:** O jogador nao orbita em torno de hordas. Ele avanca horizontalmente e reage ao que vem de frente e de tras.
- **A estrutura do nivel:** Nao e mais uma arena circular. E um nivel linear com 5 segmentos ate o boss no Congresso.
- **O spawn de inimigos:** Nao vem de bordas de um mapa 2D. Vem das laterais da tela e das portas dos ministerios no background.
- **A legibilidade dos personagens:** O grande trunfo do side-view. O jogador ve a caricatura inteira. Ve o queixao, o terno rasgado, a expressao grotesca. Isso e o Andre Guedes. Isso e o produto.
- **O sistema de armas:** Auto-attack top-down nao funciona em side-view. O jogador precisa de controle de direcao do ataque, o que abre espaco para um arsenal com mecânicas distintas.

O que NAO muda: a paleta de cores, o humor politico, os personagens, o tom horror-comedia, o Phaser 3 como engine, o objetivo viral.

---

## 1. CORE LOOP ATUALIZADO PARA SIDE-VIEW

### Micro Loop (3-5 segundos) — A Decisao Fundamental

```
Zumbi aparece pela lateral direita da tela (ou porta de ministerio)
→ Jogador le o tipo de zumbi (leitura imediata pelo visual)
→ Jogador decide: avanca, recua ou salta
→ Posiciona personagem no eixo horizontal
→ Ataca na direcao do inimigo (arma atual)
→ Zumbi morre → drop cai no chao
→ Jogador decide se vai buscar o drop (risco vs. recompensa)
→ Proximo zumbi aparece
```

A diferenca critica em relacao ao top-down: a decisao nao e apenas "para onde ir". E "atacar agora ou esperar o momento certo". Em side-view, o timing do ataque importa. O posicionamento horizontal importa. O salto (para esquivar de projeteis rasteiros) importa.

Isso e mais rico que Vampire Survivors. Mais proximo de Metal Slug: acao, reacao, expressao do personagem visivel a cada frame.

### Medio Loop (30-90 segundos) — A Wave

```
Anuncio da wave (titulo satirico aparece na tela)
→ Spawn de zumbis pelas laterais + portas dos ministerios
→ Intensidade cresce ao longo da wave (mais zumbis, mais rapidos)
→ Mini-boss ou evento especial no pico da wave
→ Intervalo de 3-5 segundos (sem spawn, jogador pega drops)
→ Proxima wave
```

Cada wave tem um nome e um evento central. O nome aparece em fonte grande no inicio. O jogador sabe o que esta vindo.

### Macro Loop — 5 Segmentos ate o Congresso

```
SEGMENTO 1: Explanada Norte (Ministerios da Esquerda)
SEGMENTO 2: Eixo Monumental Central (Horda Aberta)
SEGMENTO 3: Espelho D'Agua (Zona de Perigo + Lobistas)
SEGMENTO 4: Rampa do Congresso (Escada Final)
SEGMENTO 5: Plenario dos Mortos (Boss + Sobrevivencia)
```

O progresso e geografico e narrativo. O jogador VENCE TERRITORIO. Ele ve o Congresso ficando maior no background (scroll factor 0.1 significa que o Congresso cresce lentamente mas visivelmente). Quando ele finalmente chega ao Plenario, o Congresso domina a tela inteira. E entao aparece o boss.

---

## 2. FEATURE LIST MVP — 2 SEMANAS

### P0 — Must Have (sem isso nao existe jogo)

| # | Feature | Descricao |
|---|---|---|
| P0-01 | **Movimento horizontal** | Esquerda/direita + salto. WASD/setas no desktop, joystick virtual no mobile. |
| P0-02 | **Ataque direcional** | Botao de ataque (ou swipe no mobile). Ataca na direcao que o personagem esta virado. Sem auto-attack — o jogador mira. |
| P0-03 | **3 tipos de zumbi** | Vereador (basico), Assessor de Fake News (atirador), Senador Blindado (tanque). Cada um com comportamento e visual distintos. |
| P0-04 | **2 armas no MVP** | Chinelo Havaianas (melee rapido) e Vassoura da Esplanada (melee lento, alcance). Selecao no inicio da sessao. |
| P0-05 | **3 segmentos de nivel** | Explanada Norte, Eixo Monumental, Espelho D'Agua. Scroll horizontal continuo. |
| P0-06 | **Spawn lateral + portas** | Zumbis spawnam pelas laterais direita/esquerda e pelas portas dos ministerios no background. |
| P0-07 | **HUD basico** | HP (coracoes), score atual, wave atual, combo atual, arma equipada. |
| P0-08 | **Game Over + compartilhamento** | Tela de game over com titulo satirico, score, screenshot compartilhavel via Web Share API. |
| P0-09 | **Hit feel** | Hit stop (2 frames), hit flash (branco 1 frame), score pop flutuante, screen shake leve em kills. |
| P0-10 | **Parallax 3 layers** | Ceu estatico, ministerios distantes (0.25), chao (1.0). Minimo viavel para o efeito de profundidade. |

### P1 — Should Have (entra na semana 2 se P0 estiver done)

| # | Feature | Descricao |
|---|---|---|
| P1-01 | **Parallax completo (7 layers)** | Adiciona Congresso (0.1), ministerios proximos (0.5), objetos de fundo (0.75), foreground (1.2). |
| P1-02 | **Power-ups** | Urna Eletronica (projeteis), Cafe da Esplanada (velocidade), Carimbo do INSS (1 hit kill). Droppam de zumbis, coleta manual. |
| P1-03 | **Mecanica de brocha** | Cada arma tem fail rate (veja secao 5). Visual: arma pisca vermelho, animacao de falha, zumbi da risada. |
| P1-04 | **5 segmentos completos** | Adiciona Rampa do Congresso e Plenario dos Mortos. |
| P1-05 | **Ranking online** | Score + username (sem login obrigatorio, pode ser anonimo). Leaderboard global + diario. Backend simples (Node + PostgreSQL). |
| P1-06 | **Banqueiro-Zumbi** | 4o tipo de zumbi. Corrompe outros zumbis ao redor (velocidade x2). Nao ataca diretamente. |
| P1-07 | **Sistema de combo visual** | x2/x3/x5/x10 com texto "APROVADO!" em x5. Reset apos 2s sem kill. |
| P1-08 | **Audio basico** | 3 loops de musica (gameplay, wave intensa, game over) + SFX essenciais (hit, kill, power-up, brocha). |

### P2 — Nice to Have (pos-lancamento, se KPIs mandarem)

| # | Feature | Descricao |
|---|---|---|
| P2-01 | **Boss fight** | O Candidato Eterno. Aparece no segmento 5. Segundo turno (ressuscita com 25% HP). |
| P2-02 | **Skins do protagonista** | 3 tons de pele + variantes de roupa. Selecao antes de comecar. |
| P2-03 | **Compartilhamento aprimorado** | Screenshot automatico do cenario de fundo + score. Pack de figurinhas WhatsApp. |
| P2-04 | **Tutorial contextual** | Dicas que aparecem na primeira jogada, integradas ao gameplay. Sumem permanentemente. |
| P2-05 | **Xandao Boss** | Boss alternativo. 80px, toga, martelo. Aparece no segmento 4. |
| P2-06 | **Login e progresso** | Conta salva, historico de scores, badges. |
| P2-07 | **Missoes diarias** | 3 objetivos por dia (ex: "mate 50 vereadores"). Requer backend. |

---

## 3. USER STORIES PRIORIZADAS

Formato: Como [persona], quero [acao], para [beneficio].

**Personas definidas:**
- **Caio** — 28 anos, recebeu o link no WhatsApp, tem 3 minutos antes da reuniao
- **Marina** — 35 anos, jogadora casual, quer superar o score da amiga
- **Renato** — 42 anos, nao joga videogame ha 10 anos, veio pelo meme politico

---

### Bloco P0 — Jogo Funciona

**US-01** (P0)
Como Caio, quero comecar a jogar em menos de 5 segundos apos clicar no link, para nao perder o intervalo que tenho.

Criterios:
- Tela inicial carrega em menos de 3 segundos em 4G
- Botao "JOGAR" e o unico elemento interativo visivel
- Primeiro input do jogador coloca o personagem em movimento imediatamente

---

**US-02** (P0)
Como Renato, quero entender os controles sem ler nenhum texto, para nao me sentir burro logo de cara.

Criterios:
- Primeira wave tem apenas 3 Vereadores lentos vindo da direita
- O personagem reage visivelmente ao primeiro input (movimento imediato)
- O zumbi morre com 2-3 ataques simples
- Nenhum texto de instrucao aparece na tela

---

**US-03** (P0)
Como Caio, quero sentir que meus ataques tem peso e impacto, para que matar zumbis seja satisfatorio.

Criterios:
- Hit stop de 2 frames em todo ataque que conecta
- Hit flash branco de 1 frame no zumbi atingido
- Score pop sobe da cabeca do zumbi morto
- SFX distinto por tipo de zumbi ao morrer

---

**US-04** (P0)
Como Marina, quero ver claramente qual tipo de zumbi esta vindo, para tomar a decisao correta de posicionamento.

Criterios:
- Cada tipo de zumbi tem silhueta unica (Vereador = baixo largo, Assessor = magro com microfone, Senador = alto com escudo dourado)
- Leitura do tipo em menos de 0.5 segundos
- Comportamento coerente com visual (Assessor fica longe e atira, Senador avanca devagar)

---

**US-05** (P0)
Como Caio, quero que o jogo funcione no meu celular sem instalar nada, para jogar agora mesmo.

Criterios:
- Joystick virtual aparece onde o polegar esquerdo toca
- Botao de ataque no canto inferior direito
- Botao de salto no canto inferior direito (acima do ataque)
- 60fps em iPhone 12+ e Android equivalente
- Nenhum prompt de instalacao

---

**US-06** (P0)
Como Renato, quero uma tela de game over com algo engraçado, para compartilhar mesmo quando perco.

Criterios:
- Titulo satirico gerado baseado no score (7 faixas definidas)
- Screenshot compartilhavel em 1 toque
- Botao "JOGAR DE NOVO" igualmente proeminente ao de compartilhar
- URL do jogo visivel na tela de game over

---

### Bloco P1 — Jogo Tem Profundidade

**US-07** (P1)
Como Marina, quero escolher minha arma antes de comecar, para experimentar estrategias diferentes.

Criterios:
- Selecao de arma na tela inicial (apos selecao de personagem)
- 2 armas no MVP: Chinelo (rapido, curto) e Vassoura (lento, longo)
- Preview visual da arma ao selecionar
- Selecao nao demora mais de 10 segundos no total

---

**US-08** (P1)
Como Marina, quero power-ups que mudam o jogo por alguns segundos, para ter momentos de fantasia de poder.

Criterios:
- Drops aparecem no chao apos matar certos zumbis
- Jogador precisa se mover ate o drop para coletar (nao e automatico)
- Efeito visual imediato e obvio (velocidade duplica? Particulas ao redor? Numeros voando?)
- Duracao clara no HUD (barra regressiva)

---

**US-09** (P1)
Como Caio, quero ver o Congresso ficando mais perto enquanto avanço, para sentir que estou progredindo.

Criterios:
- Congresso visivel no background desde o segmento 1 (scrollFactor 0.1)
- Congresso cresce visivelmente ao entrar no segmento 3
- Congresso domina ~60% da tela no segmento 5
- Transicao entre segmentos tem anuncio visual (titulo do segmento)

---

**US-10** (P1)
Como Marina, quero ver meu score no ranking global depois de jogar, para comparar com outros jogadores.

Criterios:
- Leaderboard aparece na tela de game over (top 10 global + posicao do jogador)
- Nome opcional (campo de texto simples, pode deixar em branco)
- Atualiza em tempo real (polling a cada 30s no leaderboard)
- Sem login obrigatorio, sem senha, sem email

---

**US-11** (P1)
Como Renato, quero que o jogo seja tecnicamente estavel no meu telefone velho, para nao ser excluido da piada.

Criterios:
- Object pooling para zumbis (maximo 20 objetos simultaneos no MVP)
- FPS nao cai abaixo de 30fps em dispositivos de 2021+
- Sem memory leaks visiveis em 10+ sessoes seguidas
- Carregamento inicial de assets em menos de 5 segundos em WiFi

---

**US-12** (P1)
Como Marina, quero que o jogo fique mais dificil de forma justa ao longo do nivel, para sentir que estou melhorando.

Criterios:
- Segmento 1: apenas Vereadores, ritmo baixo
- Segmento 3: mix de todos os 3 tipos
- Segmento 5: Banqueiro presente, spawn acelerado
- Dificuldade aumenta por numero de zumbis simultaneos E velocidade, nao apenas por HP dos inimigos

---

### Bloco P2 — Jogo Tem Alma

**US-13** (P2)
Como Caio, quero compartilhar um screenshot bonito do meu score, para que meus amigos vejam o contexto do jogo (nao so o numero).

Criterios:
- Screenshot inclui cenario de fundo (segmento em que morreu)
- Titulo satirico em fonte grande
- Score e stats visiveis
- URL do jogo embaixo

---

**US-14** (P2)
Como Marina, quero enfrentar o boss final no Congresso, para ter uma sensacao de climax narrativo.

Criterios:
- Boss aparece apenas no segmento 5
- Boss tem fase 2 (segundo turno com 25% HP)
- Musica muda quando o boss aparece
- Matar o boss completa o jogo (tela de vitoria diferente do game over)

---

**US-15** (P2)
Como Renato, quero que a arma falhe de forma engraçada, para rir mesmo quando nao consigo matar o zumbi.

Criterios:
- Brocha tem animacao visivel (arma pisca vermelho, personagem faz expressao de desespero)
- Zumbi reage a brocha (da risada, continua avancando)
- SFX de brocha e distinto e comico
- Fail rate depende da arma (veja secao 5)

---

## 4. WAVE DESIGN — SIDE-VIEW

### Filosofia de Spawn em Side-View

Em top-down, zumbis vinham de todas as bordas do mapa. Em side-view, o mundo tem direcao: o jogador avanca para a direita. Isso define o spawn:

- **Spawn pela direita:** O perigo primario. Zumbis vem de onde o jogador esta indo. Cria tensao de "o que esta esperando la frente".
- **Spawn pela esquerda:** O perigo secundario. Zumbis perseguidores. Criam a sensacao de ser encurralado. Usados a partir do segmento 2.
- **Spawn pelas portas dos ministerios:** O perigo ambiental. Zumbis saem diretamente das fachadas no background (layer 3). Visualmente sao as portas escuras dos pilotis de Niemeyer. Criam surpresa e conectam o cenario ao gameplay.

### Segmento 1 — Explanada Norte (Waves 1-2)

**Ambiente:** Calcada de concreto rachado. Ministerios proximos dos dois lados. Fachadas com placas satiricas. Congresso visivel mas pequeno ao fundo.

**Wave 1 — "Sessao Ordinaria"**
- Spawn: apenas pela direita
- Zumbis: 5-8 Vereadores em fila irregular
- Velocidade: 0.6x base
- Comportamento especial: nenhum
- Objetivo pedagogico: jogador aprende movimento + ataque basico
- Intervalo pos-wave: 4 segundos

**Wave 2 — "Requerimento de Urgencia"**
- Spawn: direita + primeira porta de ministerio
- Zumbis: 4 Vereadores + 2 Assessores de Fake News (ficam atras, atiram)
- Velocidade: 0.8x base
- Comportamento especial: Assessor recua se jogador se aproxima
- Objetivo pedagogico: jogador aprende a priorizar targets (atira ou avanca?)
- Intervalo pos-wave: 3 segundos
- Transicao: Anuncio "SEGMENTO 2 — EIXO MONUMENTAL" antes de continuar

### Segmento 2 — Eixo Monumental (Waves 3-4)

**Ambiente:** Asfalto aberto, menos predios nas laterais. Ministerios distantes. Mais espaco, o que paradoxalmente e mais perigoso: os zumbis tem mais area para cercar o jogador.

**Wave 3 — "Sessao Extraordinaria"**
- Spawn: direita + esquerda (primeiro spawn pela esquerda do jogo)
- Zumbis: 4 Vereadores + 2 Assessores + 1 Senador Blindado
- Velocidade: 1.0x base
- Comportamento especial: Senador tem escudo que absorve 3 hits, depois quebra
- Objetivo pedagogico: jogador aprende que nem todo inimigo morre da mesma forma
- Evento: Quando o escudo do Senador quebra, SFX de caixa registradora + moedas voando

**Wave 4 — "Sessao Secreta"**
- Spawn: direita + esquerda + 2 portas de ministerio simultaneas
- Zumbis: 6 Vereadores + 3 Assessores + 1 Senador + 1 Banqueiro (se P1 ativo)
- Velocidade: 1.2x base
- Comportamento especial: Banqueiro orbita o campo, corrompe outros (aura dourada, 2x velocidade)
- Objetivo pedagogico: jogador aprende a ler ameacas de nivel diferente (Banqueiro e prioridade, mesmo nao te atacando)
- Primeiras mortes acontecem aqui para jogadores casuais
- Intervalo pos-wave: 2 segundos
- Transicao: "SEGMENTO 3 — ESPELHO D'AGUA"

### Segmento 3 — Espelho D'Agua (Waves 5-6)

**Ambiente:** Grama seca invadindo o asfalto. Reflexos no chao (efeito de shader simples). Zona de perigo: se o jogador pisar na agua, velocidade -30%.

**Wave 5 — "Plenario dos Mortos"**
- Spawn: direita + esquerda + 3 portas (maxima diversidade de spawn)
- Zumbis: Mix de todos os tipos, densidade alta
- Velocidade: 1.4x base
- Evento especial: "Onda Lobista" — 3 Lobistas aparecem carregando maletas (subtipo novo, rapido, fraco, mas em numero)
- Objetivo: pressao maxima de posicionamento, jogador precisa usar o cenario (agua = risco)

**Wave 6 — "Mandato Eterno"**
- Spawn: apenas pela direita (concentrado)
- Zumbis: Horda final, todos os tipos
- Velocidade: 1.6x base
- Mecanica especial: Score x1.5 durante esta wave (visivel no HUD)
- Fim da wave: transicao cinematica para os segmentos 4-5
- Intervalo pos-wave: 5 segundos (respiro antes do climax)
- Transicao: "SEGMENTO 4 — RAMPA DO CONGRESSO"

### Segmento 4 — Rampa do Congresso (Wave 7) [P1]

**Ambiente:** Concreto cerimonial. Sem vegetacao. O Congresso ocupa 40% da tela ao fundo. Leve inclinacao no chao (estetica, sem impacto no gameplay no MVP).

**Wave 7 — "Escada Final"**
- Spawn: apenas pela direita, em grupos rapidos
- Zumbis: Alta densidade de Senadores Blindados + Assessores
- Velocidade: 1.5x base (ligeiramente menor que wave 6 — essa wave testa estrategia, nao reflexo)
- Objetivo: Limpar o caminho para o boss. O jogador sente que esta chegando.

### Segmento 5 — Plenario dos Mortos (Boss) [P2]

**Ambiente:** Interior do Congresso. Fundo fixo (sem parallax). Plenario vazio com bancadas em perspectiva lateral. Luz verde intensa. Silencio antes do boss aparecer.

**Boss — O Candidato Eterno**
- HP: 500
- Fase 1: Anda em direcao ao jogador. A cada 8s, para e DISCURSA (onda sonica empurra jogador)
- Ao chegar a 0 HP: "SEGUNDO TURNO!" — levanta com 125 HP (25%) e velocidade +50%
- Fase 2: Avanca direto, sem pausas para discurso. Mais agressivo.
- Derrota definitiva: chuva de santinhos, jingle distorcido, drop garantido de Delacao Premiada
- Score: 200 (fase 1) + 200 (fase 2)
- Pos-boss: Tela de vitoria. Diferente da tela de game over.

---

## 5. WEAPON SYSTEM

### Filosofia das Armas em Side-View

Em top-down com auto-attack, a arma definia o raio de alcance. Em side-view com ataque manual, a arma define o verbo do combate. Cada arma muda o que o jogador faz, nao so os numeros.

### Arsenal MVP (P0 e P1)

**Arma 1 — Chinelo Havaianas (P0)**
- Tipo: Melee rapido
- Alcance: Curto (1 tile a frente)
- Dano: 15 por hit
- Cadencia: 3 ataques/segundo
- Brocha: 10% de chance por ataque
  - Animacao de brocha: Chinelo voa na direcao errada e cai no chao. Jogador precisa pegar de volta (2 segundos de espera ou perde e fica sem arma por 1 segundo).
  - Piada: "O chinelo brasileiro — preciso e traidor."
- Animacao de ataque: Swing horizontal para frente
- SFX: "FLAP-BAM" agudo
- Estrategia ideal: Zumbis isolados, combate rapido e frenético

**Arma 2 — Vassoura da Esplanada (P0)**
- Tipo: Melee longo
- Alcance: Longo (2.5 tiles a frente)
- Dano: 30 por hit
- Cadencia: 1 ataque/segundo
- Brocha: 5% de chance por ataque
  - Animacao de brocha: Cabo da vassoura parte no meio. Jogador joga fora e pega uma nova vassoura (spawn automatico do chao apos 3 segundos).
  - Piada: "Licitacao aprovada sem concurso. Qualidade zero."
- Animacao de ataque: Swing vertical descendente (vassoura vai de cima para baixo)
- SFX: "THWACK" grave
- Estrategia ideal: Grupos de inimigos proximos, timing preciso

**Arma 3 — Urna Eletronica (P1) — Power-up, nao arma base**
- Tipo: Ranged (arremesso)
- Alcance: Atravessa a tela inteira
- Dano: 45 por projetil
- Cadencia: 2 projetis/segundo
- Brocha: 40% de chance por projetil (a mais alta do jogo)
  - Embasamento narrativo: "Urna eletronica com 40% de fail rate — referencia direta a AK-47 do Bolsonaro com 40% de pecas falsas (CPI das armas, 2023)."
  - Animacao de brocha: Urna apita com erro, tela mostra "FALHA NO SISTEMA", projetil nao sai.
  - Piada: A brocha e o punchline. A urna E confiavel — o problema sao as pessoas que nao confiam.
- Disponivel como: Drop garantido do Senador Blindado
- Duracao: 5 segundos como power-up ativo
- SFX: Som de apuracao + "URNA APROVADA" ao acertar

**Arma 4 — Cracha Afiado (P1) — Power-up secundario**
- Tipo: Ranged rapido (projetil pequeno)
- Alcance: Medio (metade da tela)
- Dano: 20 por cracha
- Cadencia: 5 projeteis/segundo
- Brocha: 15% de chance
  - Animacao de brocha: Cracha quica de volta e acerta o proprio jogador (1 dano de auto-hit, piada de karma)
  - Piada: "Disse que era servidor concursado. Mentiu no curriculo."
- Disponivel como: Drop do Assessor de Fake News (20% de chance)
- Duracao: 6 segundos como power-up ativo

**Arma 5 — Biblia Blindada (P2)**
- Tipo: Escudo/melee combo
- Mecanica unica: Bloqueia projeteis (mantendo o botao de ataque) OU da hit melee (clique rapido)
- Dano melee: 25
- Brocha: 20% de chance ao bloquear
  - Animacao de brocha: Biblia abre e santinhos saem voando (itens coletaveis viram confete)
  - Piada: "Palavra de Deus. Mas impressa em papel reciclado sem licitacao."
- Disponivel como: Drop do Banqueiro-Zumbi (30% de chance)

### Tabela Resumo de Brocha

| Arma | Fail Rate | Consequencia | Piada |
|---|---|---|---|
| Chinelo Havaianas | 10% | Chinelo voa errado, precisa pegar | Traidor nato |
| Vassoura da Esplanada | 5% | Cabo parte, espera 3s | Licitacao sem qualidade |
| Urna Eletronica (power-up) | 40% | Projetil nao sai | Referencia a AK-47 do Bolsonaro |
| Cracha Afiado (power-up) | 15% | Acerta o proprio jogador | Karma de mentira no curriculo |
| Biblia Blindada (P2) | 20% | Santinhos voam, perde o bloqueio | Papel reciclado sem licitacao |

---

## 6. RANKING SYSTEM

### Formula de Score

```
Score por kill = Pontos_Base_Zumbi x Multiplicador_Combo x Bonus_Segmento

Pontos base por zumbi:
- Vereador:         10 pts
- Assessor:         25 pts
- Senador Blindado: 50 pts
- Banqueiro-Zumbi:  75 pts
- Boss (fase 1):   200 pts
- Boss (fase 2):   200 pts

Multiplicador de combo (kills em sequencia, menos de 2s entre kills):
- x1: 0-4 kills
- x2: 5-9 kills
- x3: 10-19 kills
- x5: 20-29 kills (dispara texto "APROVADO!" na tela)
- x10: 30+ kills

Bonus de segmento:
- Segmentos 1-2: x1.0
- Segmentos 3-4: x1.2
- Segmento 5:    x1.5

Bonus de vitoria (chegou ao boss e sobreviveu): +500 pts fixos

Score final = Soma de todos os kills + Bonus de vitoria (se aplicavel)
```

### Leaderboard

**Leaderboard Global:**
- Top 100 de todos os tempos
- Atualiza em tempo real
- Filtro por: "Todos os tempos" / "Esta semana" / "Hoje"
- Colunas: posicao, nome (ou "Anonimo"), score, titulo satirico, data

**Leaderboard Diario:**
- Reset a meia-noite (BRT)
- Top 50 do dia
- Destaque nas primeiras 3 posicoes (ouro/prata/bronze)
- Icone de "Hoje" no leaderboard da tela de game over

**Meu Score:**
- Sempre visivel na tela de game over, mesmo se nao esta no top 100
- Mostra posicao relativa: "Voce esta na posicao #1.847 de 23.401 jogadores hoje"

**Anti-cheat (MVP):**
- Score calculado no backend, nao no frontend
- Frontend envia apenas os eventos (kills, combo, segmento, tempo)
- Backend valida a consistencia (ex: nao e possivel ter 50.000 kills em 3 minutos)
- Scores invalidos sao silenciosamente descartados (sem aviso ao jogador)

### Compartilhamento do Score

**O que e gerado:**
1. Screenshot automatico da tela de game over (canvas API ou html2canvas)
2. Cenario de fundo visivel na tela de resultado (ultimo segmento em que morreu)
3. Titulo satirico em fonte grande
4. Tres stats principais: score, zumbis eliminados, maior combo
5. URL: congressodosmortos.com.br
6. Numero da posicao no ranking (se disponivel): "Top 5% hoje"

**Como e compartilhado:**
- Mobile: Web Share API (abre share sheet nativo do sistema)
  - Texto: "Fui [TITULO SATIRICO] no Congresso dos Mortos! Score: [X] pts. Consegue mais? congressodosmortos.com.br"
  - Imagem: screenshot da tela de game over
- Desktop: botoes diretos de Twitter/X e WhatsApp + copia link

**Titulos por faixa de score:**

| Faixa de Score | Titulo | Texto Compartilhavel |
|---|---|---|
| 0 — 500 | "Estagiario da Esplanada" | "Nao aguentei nem uma reuniao. Mas pelo menos tentei." |
| 501 — 1.500 | "Vereador Suplente dos Mortos" | "Eleito por acidente. Durei mais do que a maioria." |
| 1.501 — 3.000 | "Deputado Federal Sobrevivente" | "Apresentei projeto de lei: SOBREVIVER. Foi aprovado." |
| 3.001 — 5.000 | "Senador da Resistencia" | "Imunidade parlamentar: duracao de 3 minutos." |
| 5.001 — 8.000 | "Ministro da Defesa Zumbi" | "O Planalto ta seguro. Por enquanto." |
| 8.001 — 12.000 | "Presidente dos Vivos" | "Primeiro mandato: sobrevivencia. Segundo: impossivel." |
| 12.001+ | "Lenda da Esplanada" | "Sobreviveu ao que nenhum brasileiro conseguiu: o sistema inteiro." |

---

## 7. SPRINT PLAN — 2 SEMANAS (10 DIAS UTEIS)

### Principios do Sprint

1. P0 deve estar jogavel no fim do dia 5 (semana 1).
2. P1 entra na semana 2 se e somente se P0 esta done e polido.
3. Cada dia tem um entregavel claro. Se o entregavel nao esta done ao fim do dia, o time pausa e pergunta o que bloqueou.
4. "Polido" significa: hit feel correto, sem bugs visiveis, roda em desktop e mobile.

### Semana 1 — Foundation (Dias 1-5)

**Dia 1 — Setup e Camera**
- Setup: repo, Phaser 3.88 dentro de React via useRef, scene structure
- Camera: viewport 480x270, escala 2x, scroll horizontal configurado
- Parallax minimo (P0-10): 3 layers funcionando (ceu estatico, ministerios distantes 0.25, chao 1.0)
- Entregavel: tela preta com parallax rolando ao pressionar tecla

Definition of Done: parallax scrollando sem artifacts, 60fps no Chrome desktop, sem memory leaks em 1 minuto de scroll.

---

**Dia 2 — Personagem e Movimento**
- Sprite do protagonista (placeholder de cor solida se arte nao esta pronta)
- Movimento horizontal (WASD + setas no desktop)
- Salto com fisica arcade (gravity, jump velocity)
- Joystick virtual no mobile (aparece onde o polegar toca)
- Colisao com chao
- Entregavel: personagem se move e salta nos dois dispositivos

Definition of Done: movimento fluido sem jitter, salto com curva fisica correta (nao linear), joystick responsivo no mobile sem latencia perceptivel.

---

**Dia 3 — Ataque e Hit Feel**
- Ataque melee direcional (personagem vira esquerda/direita)
- Hitbox de ataque (Phaser Arcade overlap)
- Hit stop (2 frames de timescale 0 no Phaser)
- Hit flash (setTintFill branco por 1 frame no sprite do inimigo)
- Score pop flutuante (texto que sobe e desaparece com tween)
- Screen shake leve (camera.shake)
- SFX placeholder de hit
- Entregavel: atacar um dummy com hit feel completo

Definition of Done: hit stop perceptivel mas nao irritante, flash branco visivel, score pop aparece em 1 frame apos o hit, shake nao causa enjoo.

---

**Dia 4 — 3 Tipos de Zumbi + Spawn**
- Vereador: movimento reto em direcao ao jogador, HP baixo, morte com animacao de queda
- Assessor: fica a distancia, dispara projetil a cada 2s, recua se jogador se aproxima
- Senador: lento, escudo que absorve 3 hits (contador visivel), quebra do escudo com SFX
- Spawn pela direita (timer-based para MVP, nao event-driven ainda)
- Spawn pelas portas dos ministerios (posicoes fixas no layer 3)
- Object pooling para os 3 tipos (maximo 20 zumbis ativos simultaneos)
- Entregavel: 3 tipos de zumbi spawnando e atacando o jogador

Definition of Done: cada tipo legivel visualmente em menos de 1 segundo, comportamentos distintos e coerentes, 60fps com 20 zumbis na tela, pool funcionando (sem new() durante gameplay).

---

**Dia 5 — HUD, Game Over e Sessao Completa**
- HUD: HP (coracoes), score, wave, combo, arma equipada
- Sistema de HP do jogador (recebe dano, pisca, morre)
- Tela de game over com titulo satirico por faixa de score
- Botao "JOGAR DE NOVO" (reload da scene)
- Tela inicial simples (texto da Emenda 666 + botao JOGAR)
- 3 segmentos de nivel (P0-05): transicao por distancia percorrida
- Entregavel: sessao completa jogavel do inicio ao fim, com game over

Definition of Done: fluxo completo sem crashes, titulo satirico aparece corretamente por faixa, botao de jogar de novo funciona sem memory leak, wave system avanca corretamente pelos 3 segmentos.

---

### Semana 2 — Polish e P1 (Dias 6-10)

**Dia 6 — 2 Armas + Brocha**
- Chinelo Havaianas implementado com todas as specs (P0-04)
- Vassoura da Esplanada implementado com todas as specs (P0-04)
- Selecao de arma na tela inicial (2 opcoes)
- Sistema de brocha com animacoes
- SFX de brocha (distinto do hit normal)
- Entregavel: player escolhe arma, brocha ocorre com animacao completa

Definition of Done: fail rate correto (10% chinelo, 5% vassoura), animacao de brocha tem timing correto, zumbi reage a brocha visualmente.

---

**Dia 7 — Parallax Completo + Polish Visual (P1-01)**
- Layer 1: Congresso (scrollFactor 0.1, sprite 320x120px)
- Layer 3: Ministerios proximos (scrollFactor 0.5, fachadas com pilotis e portas)
- Layer 4: Objetos de fundo (scrollFactor 0.75, arvores secas, postes)
- Layer 7: Foreground (scrollFactor 1.2, elementos semi-transparentes)
- Transicao visual entre segmentos (fade de ambientacao)
- Entregavel: parallax completo com 7 layers rodando a 60fps

Definition of Done: sem artifacts de tiling, sem pop-in de sprites, 60fps com parallax completo + 20 zumbis na tela, Congresso visivel e crescendo ao longo do nivel.

---

**Dia 8 — Power-ups e Combo Visual (P1-02, P1-07)**
- Urna Eletronica como power-up (drop do Senador)
- Cafe da Esplanada como power-up (drop do Assessor)
- Carimbo do INSS como power-up (drop do Banqueiro)
- Drop cai no chao, coleta por aproximacao
- HUD de power-up ativo (icone + barra regressiva)
- Texto "APROVADO!" em x5 combo
- Banqueiro-Zumbi completo (P1-06)
- Entregavel: 3 power-ups funcionando com efeitos visuais completos

Definition of Done: efeito de cada power-up obvio sem instrucao (velocidade visivelmente dobra, urna dispara projeteis claro), duracao termina sem crashes, Banqueiro corrompe outros zumbis corretamente.

---

**Dia 9 — Ranking Online (P1-05)**
- Backend: endpoint POST /score (recebe eventos, calcula score no servidor)
- Backend: endpoint GET /leaderboard (global, diario)
- Anti-cheat basico: validacao de consistencia no backend
- Frontend: tela de leaderboard integrada ao game over
- Campo de nome opcional (sem login, sem senha)
- Entregavel: score salvo e exibido no leaderboard apos cada sessao

Definition of Done: score salvo em menos de 500ms, leaderboard exibe top 10 corretamente, score invalido e descartado silenciosamente, funciona em mobile com boa latencia (< 1s).

---

**Dia 10 — Compartilhamento, Audio e Lancamento (P0-08, P1-08)**
- Screenshot automatico da tela de game over (html2canvas ou canvas API)
- Web Share API no mobile
- Botoes Twitter/X e WhatsApp no desktop
- URL do jogo na tela de game over
- 3 loops de musica (pode ser placeholder de audio livre)
- SFX essenciais: hit, kill (por tipo de zumbi), power-up, brocha, game over
- Testes em iPhone 12, Android 2021, Chrome desktop, Safari desktop
- Entregavel: build de lancamento, deploy em congressodosmortos.com.br

Definition of Done: compartilhamento funciona em iOS Safari e Android Chrome, screenshot inclui titulo e score, audio nao crasha em mobile, 60fps no dispositivo de referencia (iPhone 12).

---

## 8. O QUE FOI CORTADO EM RELACAO AO PRD 13 (E POR QUE)

| Feature do PRD 13 | Status | Razao |
|---|---|---|
| Auto-attack | REMOVIDO | Side-view exige ataque direcional. Auto-attack elimina a dimensao de timing que e o coracao do Metal Slug. |
| Arena circular (top-down) | REMOVIDO | Substituido por nivel linear com scroll horizontal. |
| Timer fixo de 3 minutos | ADAPTADO | Mantido como referencia de sessao, mas agora o progresso e por distancia/segmento, nao so por tempo. O timer e o "par", nao o limite absoluto. |
| Leaderboard local (localStorage) | ELEVADO para P1 | Com backend ja planejado para login futuro, leaderboard online no MVP faz mais sentido estrategico. localStorage como fallback se backend falhar. |
| Boss na wave 5 | MOVIDO para P2 | Boss completo requer 2-3 dias de trabalho (arte, mecanica de 2 fases, musica especial). No MVP de 2 semanas com pivot recente, P2 e correto. |
| 4 tipos de zumbi no MVP | REDUZIDO para 3 (P0) + 1 (P1) | Banqueiro-Zumbi em P1. 3 tipos sao suficientes para validar o loop. O Banqueiro entra na semana 2 se P0 estiver done. |
| Leaderboard de sessao (WhatsApp) | MANTIDO | URL compartilhavel continua. |

---

## 9. KPIS — CRITERIOS GO/NO-GO

Identicos ao PRD 13, com um adicional especifico para o side-view:

| Metrica | NO-GO | Minimo GO | Excelente |
|---|---|---|---|
| Usuarios unicos (semana 1) | < 50K | > 200K | > 1M |
| Taxa de compartilhamento | < 2% | > 5% | > 15% |
| Retencao D1 | < 15% | > 25% | > 40% |
| Retencao D7 | < 5% | > 10% | > 20% |
| Sessoes por usuario/semana | < 2 | > 4 | > 8 |
| Mencoes em midia | 0 | > 5 | > 20 |
| **FPS medio (mobile)** | < 30fps | > 45fps | 60fps estavel |
| **Taxa de completar segmento 1** | < 40% | > 60% | > 80% |
| **Taxa de compartilhamento apos vitoria** | < 10% | > 20% | > 40% |

A taxa de completar segmento 1 e nova e critica: se menos de 60% dos jogadores completa o primeiro segmento, o problema e no onboarding ou na performance. Isso e mensuravel e acionavel.

---

## 10. DEFINICAO DE "DONE" PARA O MVP

O MVP esta pronto quando:

1. Um pessoa que nunca jogou abre o link no celular, entende o que fazer em 5 segundos sem ler nada, e sorri em 10.
2. A sessao completa (inicio ao game over) roda sem crash em iOS Safari e Android Chrome.
3. O botao de compartilhamento funciona e gera um screenshot legivel.
4. 60fps no iPhone 12 com parallax completo e 20 zumbis na tela.
5. O leaderboard exibe o score do jogador em menos de 1 segundo.
6. Nenhum PM, desenvolvedor ou artista do time precisou explicar as mecanicas para o testador.

O ponto 6 e o "Miyamoto stare" deste projeto. Se voce teve que explicar, a mecanica falhou. Volta para o dia 3 e muda o hit feel, o spawn, ou o visual do zumbi — o que for necessario para que a compreensao seja imediata.

---

## NOTAS FINAIS DO PM

O pivot para side-view nao foi so uma escolha estetica. Foi uma decisao de produto.

Em top-down, o Andre Guedes nao podia fazer o que sabe fazer. Caricaturas com queixao, veias, expressoes grotescas — tudo isso some em 16 pixels vistos de cima. O produto viral que o Andre vende e o VISUAL POLITICO. A satira que faz o brasileiro dar risada e mandar para o grupo da familia.

Em side-view, o personagem e grande. O jogador ve o Senador Blindado com o escudo dourado de "Imunidade Parlamentar" quebrando. Ve o Assessor de Fake News recuando com o microfone de lapela e o cabelo de apresentador. Ve o Banqueiro de terno italiano com o celular cheio de contatos. ISSO e o produto.

A mecanica de ataque direcional com brocha adiciona uma camada de humor que o auto-attack nao tinha. A urna com 40% de fail rate E o punchline. A brocha do chinelo E a piada. O jogo nao tem texto politico — o gameplay E o texto politico.

Lancamento: Semana da Gamescom LATAM — 30 de abril a 3 de maio de 2026.

congressodosmortos.com.br

---

*"Quando os jogadores entendem as regras antes de ler qualquer coisa, voce fez seu trabalho direito."*
*— Shigeru Miyamoto*
