# ZUMBIS DE BRASÍLIA — UX Design Document
### Projetado por Jenova Chen | Experiência Emocional e Game Feel

**Versão 1.0 | Abril 2026**

---

> *"Um jogo não é o que você vê — é o que você sente enquanto está jogando. Se você precisa explicar por que é divertido, você falhou. O jogo deve fazer a pessoa sentir algo antes de entender qualquer coisa."*

---

## 1. Filosofia de UX — Como o Jogo Deve SENTIR

### A Emoção Central: Catarse com Risos

Zumbis de Brasília não é um jogo de terror. Não é um jogo de ação. É um jogo de **catarse política com humor**.

Pense em como um brasileiro se sente ao abrir o feed de notícias em 2026: uma mistura de raiva, fadiga, ironia e resignação. O jogo deve pegar exatamente esse estado emocional e **transformá-lo em poder**. Você chega exausto. Você sai satisfeito. Esse é o arco emocional que tudo deve servir.

### Os Três Pilares Emocionais

**Pilar 1: Reconhecimento ("Conheço esse sujeito")**
O momento em que o jogador vê um zumbi e pensa "é o tipo igualzinho ao cara que vi no noticiário essa semana" — esse instante de reconhecimento vale mais que qualquer mecânica. É o flash de conexão cultural que transforma um sprite 2D em personagem. O design visual, os gritos de morte, os nomes — tudo serve a criar esse momento.

**Pilar 2: Competência Crescente ("Estou melhorando")**
Mihaly Csikszentmihalyi definiu flow state como o ponto de equilíbrio entre desafio e habilidade. Zumbis de Brasília deve manter o jogador nesse fio de navalha: sempre difícil o suficiente para ser emocionante, sempre possível o suficiente para continuar. A curva de dificuldade não é uma linha ascendente — é uma onda. Sobe, dá uma respirada, sobe mais.

**Pilar 3: Antecipação do "Mais Uma" ("Dessa vez vai")**
O loop de "mais uma partida" não nasce de recompensas. Nasce da convicção do jogador de que ele *quase* conseguiu. Design de morte justa é design de esperança: você sabe o que errou, você sabe o que faria diferente, e essa clareza é irresistível.

### O Princípio da Mínima Interface Possível

Cada elemento de UI compete com o gameplay pela atenção do jogador. No flow state, o ideal é zero interface — o jogador processa o espaço de jogo como realidade. Portanto: a interface existe apenas quando o jogador precisa dela, se comunica com o mínimo de leitura possível, e nunca interrompe o ritmo.

**Regra de ouro**: Se um elemento de UI pode ser substituído por um som, uma animação ou uma mudança de cor — ele deve ser substituído.

### Design para o Contexto Brasileiro de 2026

O jogador típico está no metrô de São Paulo às 18h40. O celular está na mão direita. A linha está lotada. Ele tem 7 minutos antes de descer. O jogo precisa:
- Ser iniciado com um toque
- Estar em gameplay em 10 segundos
- Funcionar sem olhar para a tela por 3 segundos (situational awareness)
- Ser pausável sem punição
- Ter momentos de baixa intensidade que permitem distrações

---

## 2. Jornada Emocional — Curva de Engajamento do Jogador

### A Curva Completa

```
EMOÇÃO
  │
  │                                      ╭──── FLOW STATE (loop)
  │                                  ╭──╯
  │                    PRIMEIRA     ╭╯
  │            "OK"    CONQUISTA   ╭╯
  │          ╭──╮  ╭──╮  ╭────────╯
  │        ╭─╯  ╰──╯  ╰──╯
  │     ╭──╯
  │  ╭──╯  CURIOSIDADE
  │──╯
  └──────────────────────────────────────────────────────── TEMPO
     |       |        |         |          |
   ÍCONE   SPLASH   1a MORTE  WAVE 5   "MAIS UMA"
```

---

### Fase 1: O Primeiro Toque (0 segundos — antes de abrir o app)

**Estado emocional alvo**: Curiosidade + Reconhecimento cultural

O ícone do app é a porta de entrada. Antes de qualquer UX, é uma decisão de marketing: o rosto grotesco de um político-zumbi familiar, expressão de terror idiota, paleta saturada e suja que imediatamente comunica "humor brasileiro, não é sério". Alguém vê no TikTok do amigo, baixa, abre.

**Micro-jornada do download até o gameplay:**
- Ícone visto → curiosidade (2 segundos de persuasão visual)
- Splash screen → reconhecimento (André Guedes, "ah, é aquele cara")
- Tela de menu → "parece fácil de entender"
- Primeiro toque → gameplay imediato (zero tutorial, zero loading longo)

---

### Fase 2: Os Primeiros 30 Segundos (aprendizado sem tutorial)

**Estado emocional alvo**: Descoberta + Pequenas Vitórias

O jogador aparece na Esplanada. Um Vereador-zumbi caminha lentamente em sua direção. Não há instruções. Há apenas um joystick virtual que aparece onde o dedo toca.

**O que acontece emocionalmente:**
1. O personagem responde ao movimento — satisfação imediata ("funciona")
2. O zumbi se aproxima — tensão natural ("o que faço?")
3. O botão de ataque pulsa suavemente — dica visual intuitiva
4. O jogador toca — o zumbi voa para trás com um "THWACK" e um número de score
5. *Momento de ouro*: o zumbi cai e grita "Fui eleito democraticamente!"
6. **O jogador ri.** Não sorri — ri.

Esse riso é o contrato emocional assinado. A partir dali, o jogador está dentro.

**Princípio de Miyamoto aplicado**: Nunca diga ao jogador o que fazer. Crie uma situação onde a ação correta é a mais intuitiva e a mais recompensadora. O zumbi vem, você precisa agir, o botão pisca gentilmente. Não precisa de mais nada.

---

### Fase 3: A Primeira Morte (minuto 2-4)

**Estado emocional alvo**: Surpresa → Leve frustração → Resolução imediata

A primeira morte deve acontecer de forma *justa e cômica*. O Assessor de Comunicação entrou pelo flanco. O jogador ficou parado demais. Os press releases voadores causaram o knockback final. O personagem cai, a tela congela, e aparece em fonte de jornal rasgado:

**"SEU MANDATO ACABOU"**

Abaixo, pequena letras de rodapé: *"(por enquanto)"*

E logo em seguida, a opção de continuar ou tentar novamente.

**Por que isso funciona:**
- A causa da morte foi *visível* (o jogador sabe o que aconteceu)
- A mensagem é engraçada (quebra a frustração com humor)
- A opção "mais uma" está na frente (não precisa navegar nada)
- O jogo não punidão — não perde progresso, não perde XP
- A tela de game over mostra o score e a wave — o jogador vê *quanto progrediu*

**Armadilha a evitar**: Morte por "câmera traidora", dano invisível ou lógica opaca. Se o jogador morrer e não entender por quê, a frustração não converte em "mais uma" — converte em desinstalação.

---

### Fase 4: O Momento "Ah, Entendi" (wave 3-4)

**Estado emocional alvo**: Competência + Estratégia emergente

Quando o Senador Vitalício entra em cena pela primeira vez, algo muda. O jogador tenta bater frontalmente — e percebe que é muito lento. Começa a correr. Kiting acontece naturalmente. "Posso usar os blocos dos Ministérios como barreira" — pensamento emergente, sem que ninguém disse isso.

Esse é o momento em que o jogador se torna um *estrategista*. Não mais um executante — um pensador.

**Design de reforço**: Quando o jogador faz algo "inteligente" pela primeira vez (kiting, chokepoint, matar vários com uma área), o jogo recompensa com um bonus de score colorido e um som ascendente. Não é uma conquista formal — é feedback imediato que diz "isso foi elegante, continue".

---

### Fase 5: A Primeira Wave 5 — O Boss (minuto 7-12)

**Estado emocional alvo**: Tensão máxima → Triunfo épico

O Candidato Eterno entra com tema musical. Tudo muda. A música fica mais urgente. O boss domina a tela com aquele sorriso impossível. O jogador usa tudo que aprendeu.

E quando o boss cai pela *primeira vez* e levanta (Segundo Turno), o momento de "não acabou" cria um pico de tensão excepcional. Quando finalmente morre de vez e aparece o placar de votos "0 votos" — é uma liberação de tensão seguida de risada. Esse é o pico emocional da sessão.

**Após essa vitória:** O jogador está no flow state. A onda seguinte já começou antes de ele perceber. Ele não está "jogando um game" — ele está *dentro* de algo.

---

### Fase 6: O Loop de "Mais Uma" (reengajamento infinito)

**Estado emocional alvo**: Confiança + Antecipação

Após a primeira sessão completa (independente de como terminou), o jogador tem um modelo mental do jogo. Ele sabe os tipos de zumbi. Sabe como se mover. Tem uma arma favorita.

Na próxima sessão, ele começa *melhor*. Isso é design de competência progressiva — não é level up no sentido tradicional, é habilidade real crescendo. E essa sensação de "estou melhorando de verdade" é o combustível mais poderoso para retenção.

**O gancho da segunda sessão**: A tela de menu mostra o "Melhor score" e a "Melhor wave" da sessão anterior. Uma pequena barra de progresso para o próximo upgrade de personagem. Uma missão diária nova. Tudo comunica: "tem mais pra descobrir".

---

## 3. Art Direction — Identidade Visual

### A Paleta de André Guedes

O estilo visual é underground comix brasileiro: cores saturadas-sujas, traços grossos com irregularidades intencionais, proporções deformadas, expressões exageradas ao limite do reconhecível. Não é cartoon limpo. Não é pixel art. É caricatura política em movimento.

**Paleta Principal:**

| Cor | Hex | Uso | Sensação |
|---|---|---|---|
| Amarelo-esverdeado sujo | #C8B84A | Gramados da Esplanada, zumbis Vereador | Brasil deteriorado |
| Laranja queimado | #D4621A | Céu do anoitecer, UI de alerta | Urgência, calor |
| Verde-azulado escuro | #1A3A2E | Sombras, fundo noturno | Opressão, profundidade |
| Vermelho sangue-tijolo | #8B1A1A | Sangue estilizado, dano crítico | Perigo sem realismo |
| Bege-creme envelhecido | #E8D8B4 | Pele dos personagens, papel | Humanidade degradada |
| Preto com textura | #1A1410 | Contornos, texto, sombras | Peso do traço |
| Branco-sujo | #F0E8D8 | Highlights, press releases, papel | Papel de jornal barato |

**Paleta de UI (separada do mundo do jogo):**

| Elemento | Cor | Lógica |
|---|---|---|
| Score / Combo | Amarelo-ouro vibrante | Recompensa, positivo |
| Vida / HP | Vermelho pulsante | Urgência legível |
| Power-ups | Verde neon sujo | Ação disponível |
| Alertas de wave | Laranja queimado | Transição, atenção |
| Texto de UI | Branco-sujo sobre fundo escuro | Legibilidade máxima |

### Estilo Visual — Do's e Don'ts

**FAÇA:**
- Traços irregulares com espessura variável (não linhas perfeitas de vetor)
- Proporções grotescas: cabeças enormes, corpos deformados, expressões ao limite
- Paleta suja e saturada — cores que parecem impressas em papel barato
- Animações com poucos frames mas extremamente expressivas (12fps para personagens, 24fps para efeitos)
- Texturas de papel e tinta sobre os sprites (não tela de vidro limpa)
- Sombras dramáticas e duras (não gradient suave)
- Tipografia com personalidade (manchetes de jornal barato, escrita de panfleto)

**NÃO FAÇA:**
- Clean lines de produção AAA — isso mata o estilo
- Shading gradiente suave nos personagens
- Fontes sans-serif neutras para texto de gameplay (use fontes com personalidade)
- Cenário mais detalhado que os personagens (os zumbis devem dominar visualmente)
- Sangue realista — use vermelho espalhoso, estilizado, quase tinta
- Efeitos de partícula que parecem Unity Asset Store padrão
- Cores frias para momentos positivos (o jogo é quente, mesmo os momentos de perigo)

### Referências Visuais por Elemento

**Personagem principal (jogador):**
Robert Crumb encontra charge política do O Pasquim: figura ligeiramente caricata mas reconhecível, roupas de cidadão comum (camisa polo, tênis, não herói), expressão determinada com pitada de descrença total.

**Zumbis:**
George Romero (movimentação lerda e expressão vaga) + caricaturas do Angeli dos anos 80 (deformação expressiva, detalhes de status social exagerados — gravatas enormes, crachás visíveis, pastas estufadas).

**Cenário:**
Brasília como viu um arquiteto com ressaca: a grandiosidade de Niemeyer interpretada com cores de fim de tarde, concreto que parece suado, gramados que parecem ter sede. Monumental e decadente ao mesmo tempo.

**Efeitos de impacto:**
Onomatopeias visuais no estilo HQ americana antiga — "THWACK", "FLAP-BAM", "SPLAT" — com tipografia irregular, cor sólida, tamanho exagerado. Aparecem e somem em 4 frames.

**UI geral:**
Manchete de tablóide barato dos anos 90. Bordas irregulares. Stamps de carimbos. Papel envelhecido como fundo. Tudo parece impresso em pressa.

---

## 4. Fluxo do Jogador

### Mapa de Fluxo Completo

```
PRIMEIRO DOWNLOAD
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│  SPLASH SCREEN (1.5s)                                   │
│  Logo + assinatura "baseado no universo de André Guedes"│
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│  TELA DE MENU PRINCIPAL                                 │
│  [JOGAR] [MELHOR SCORE] [SKINS] [CONFIGURAÇÕES]        │
│  Animação de fundo: Esplanada com zumbis wandering      │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│  SELEÇÃO DE ARMA (1 tela, máximo 3 segundos)           │
│  Cards visuais: Vassoura / Chinelo / Santinho           │
│  Toque no card = destaque + preview de animação         │
│  Botão "IR PRA GUERRA" (não "Confirmar")               │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│  GAMEPLAY                                               │
│  Wave intro (2s) → Horde → Wave clear → Próxima wave   │
│                         │                               │
│                    MORREU?                              │
│                    ┌────┴────┐                          │
│                   NÃO      SIM                          │
│                    │        │                           │
│              Continua   TELA DE MORTE                   │
│                         │                               │
│                    ┌────┴────────────────┐              │
│               CONTINUAR (rewarded ad)  ENCERRAR         │
│                    │                    │               │
│               +1 Vida             TELA DE RESULTADO     │
│               volta ao jogo            │                │
│                                   [MAIS UMA]            │
│                                   [COMPARTILHAR]        │
│                                   [MENU]               │
└─────────────────────────────────────────────────────────┘
```

### Onboarding (Primeiras 3 Sessões)

**Sessão 1 — Descoberta:**
- Sem tutorial explícito
- Joystick aparece onde o dedo toca (dinâmico)
- Botão de ataque pisca suavemente nos primeiros 5 segundos
- Wave 1: apenas Vereadores (lentos, volume baixo) — ensina movimento + ataque
- Wave 2: Assessores aparecem — ensina a se mover enquanto ataca
- Se o jogador morrer antes da wave 3: tela de morte com dica contextual (1 linha, baseada na causa da morte)

**Sessão 2 — Progressão:**
- Notificação de "você desbloqueou seu primeiro upgrade de personagem"
- Sistema de upgrade aparece após a primeira morte da sessão 2 (não sessão 1)
- 3 opções de upgrade apresentadas com icones grandes e texto de 3 palavras

**Sessão 3 — Profundidade:**
- Missão diária aparece no menu
- Power-ups começam a dropar com mais frequência (o jogo "apresenta" o sistema)

### Core Loop (Sessão Típica — 7 minutos)

```
Menu (10s) → Seleção de arma (5s) → Gameplay waves 1-6 (5 min)
→ Morte ou vitória parcial → Tela de resultado (20s)
→ Opção de ad para continuar (15s) OU encerrar
→ Menu com progresso atualizado → "Mais uma?"
```

### Metagame (Engajamento entre Sessões)

- Leaderboard semanal visível no menu (posição atual do jogador sempre em destaque)
- Missões diárias com barra de progresso visível sem entrar no jogo (widget/notificação)
- Progresso de level de personagem sempre visível na tela de menu
- Conquistas desbloqueadas mostram popup na tela de resultado (nunca interrompem gameplay)

### Reengajamento (Depois de 1+ dias sem jogar)

- Notificação push com copy no estilo do jogo: "O Vereador está com saudades. Venha eliminá-lo."
- Ao abrir: menu mostra "missão de retorno" — objetivo simples (matar 20 zumbis) com recompensa garantida
- Score pessoal da última sessão visível: convida à competição consigo mesmo

---

## 5. UI Design — Interface Minimalista para Mobile One-Handed

### Filosofia de HUD

O HUD deve existir na periferia da atenção. O jogador não deve precisar olhar para o HUD — ele deve *sentir* o estado do jogo através de feedback audiovisual do mundo.

**Regra dos 80%**: 80% do tempo, o jogador deve estar olhando para o centro da tela (onde estão os zumbis e o personagem), não para os cantos do HUD.

### Layout do HUD (720p, aspecto 16:9 / 18:9)

```
┌────────────────────────────────────┐  ← 720p width
│ ❤❤❤❤❤          [WAVE 3]    SCORE │  ← HUD topo (32dp altura)
│                                   │
│                                   │
│         ÁREA DE GAMEPLAY          │
│         (80% da tela)             │
│                                   │
│                                   │
│  ╔════╗                  ╔══════╗ │  ← HUD baixo (safe area)
│  ║ JS ║                  ║ATAQUE║ │
│  ║    ║                  ╚══════╝ │
│  ╚════╝         [POWER-UP SLOT]   │
└────────────────────────────────────┘
```

### Elementos do HUD

**Barra de Vida (topo esquerdo):**
- Representada por coraçõezinhos (5 no total — não uma barra percentual)
- Coraçõezinhos pulsam quando HP está baixo (menos que 2)
- Ao perder vida: coração "quebra" com animação de 4 frames + screen flash vermelho suave
- Ao ganhar vida: coração "aparecer" com animação pop + flash verde suave
- *Por quê coraçõezinhos e não barra de porcentagem*: contagem discreta é mais legível em movimento e mais emocional

**Indicador de Wave (topo centro):**
- Texto simples: "WAVE 3" em fonte bold de manchete
- Durante wave boss: pisca em laranja com texto "BOSS WAVE"
- Contador de zumbis restantes na wave (número pequeno abaixo): "7 restantes"
- Desaparece 3 segundos após o jogador começar a se mover na wave (sem distrações)

**Score (topo direito):**
- Número grande, fonte bold, amarelo-ouro
- Ao ganhar pontos: número "salta" para cima com efeito de bounce
- Multiplicador de combo aparece abaixo do score quando combo ≥ 5: "x2" em laranja

**Joystick Virtual (baixo esquerdo):**
- *Dinâmico*: aparece onde o dedo toca, não fixo
- Raio externo: 60dp, semi-transparente (40% opacidade)
- Ponto central: 20dp, totalmente opaco
- Faixa de detecção: metade esquerda da tela
- Desaparece suavemente ao soltar o dedo

**Botão de Ataque (baixo direito):**
- Círculo de 72dp, ícone da arma atual no centro
- Cooldown visual: arco que se preenche (para armas com cooldown)
- Pulsa suavemente quando inimigo está no alcance de ataque (hint sem texto)
- Feedback háptico: vibração de 15ms a cada hit confirmado

**Slot de Power-up (baixo centro):**
- Aparece APENAS quando um power-up foi coletado (não fica vazio na tela)
- Ícone do power-up com contador regressivo visual (arco se esgotando)
- Ativado por swipe rápido de segundo dedo OU toque longo no ícone

### Feedback Visual de Combate

**Hit Numbers (dano flutuante):**
- Cor por tipo: branco = dano normal, amarelo = crítico, laranja = headshot
- Tamanho proporcional ao dano (crítico é 1.5x maior)
- Trajetória: sobe levemente, arco leve para a direita, desaparece em 0.8s
- Fonte: bold, irregular, estilo manchete

**Onomatopeias de Impacto:**
- Aparecem no ponto de impacto, não no HUD
- Duração: 6 frames (0.25s)
- Por arma: THWACK (vassoura), SLAP (chinelo), BOOM (urna), WHOOSH (santinho), WHAM (microfone)
- Cor combina com a arma

**Flash de Dano no Personagem:**
- Ao levar dano: screen flash vermelho (30% opacidade, 4 frames) + personagem pisca branco
- Invencibilidade de 0.5s sinalizada por personagem piscando em silhueta clara

### Tipografia

**Hierarquia de fontes (3 fontes máximo):**

| Uso | Fonte | Característica |
|---|---|---|
| Headlines / Score / Wave | Bebas Neue Bold | Impacto de manchete, toda maiúscula |
| Texto de UI / Menus / Flavor text | Oswald Regular | Legível, personalidade, não genérica |
| Texto de zumbis / falas / humor | Fonte manuscrita irregular | Estilo HQ, quebrante, informal |

**Tamanhos mínimos para mobile 720p:**
- Texto de UI principal: 18sp
- Labels secundários: 14sp
- Nunca abaixo de 12sp em qualquer elemento clicável

**Legibilidade:** Todo texto sobre imagem usa shadow de 1px ou background pill semi-transparente. Zero texto cinza sobre cinza.

### Iconografia

- Ícones são desenhados no estilo André Guedes: linhas irregulares, personalizados, não de icon pack
- Cada power-up tem ícone que communica o efeito visualmente sem ler o nome
- Botões de ação têm ícone + texto curto (touch targets mínimos: 48dp)
- Coração para vida, cédula para moedas, troféu para conquistas — iconografia universal mas reestilizada

---

## 6. Juice & Game Feel — O que Faz Cada Kill Satisfatória

### A Anatomia de um Kill Perfeito

Um kill em Zumbis de Brasília deve ser uma *performance* em 6 atos que dura 0.4 segundos:

```
Ataque lançado
    ↓ (0.02s)
Hit stop: 2-3 frames de "congelamento" do zumbi (sensação de peso real)
    ↓ (0.05s)
Hit flash: sprite do zumbi pisca branco (confirmação visual do hit)
    ↓ (0.02s)
SFX de impacto: som distinto da arma (THWACK, SLAP, etc.)
    ↓ (0.02s)
Knockback: zumbi vai para trás com velocidade proporcional ao dano
    ↓ (0.03s)
Score popup: número flutua para cima com bounce, onomatopeia aparece
    ↓ (continua)
Animação de morte: cada zumbi tem animação única de morte cômica
    ↓ (0.3-0.5s)
Fala de morte: linha de humor contextual (nem sempre, 40% das mortes)
```

### Screen Shake

**Não exagere — contextualize:**

| Evento | Intensidade | Duração | Frequência |
|---|---|---|---|
| Hit normal (vassoura) | Leve (2px) | 0.1s | Cada hit |
| Hit crítico | Médio (4px) | 0.15s | Cada crítico |
| Boss hit | Médio-alto (6px) | 0.2s | Cada hit no boss |
| Kill normal | Nenhum | — | — |
| Kill em combo x10+ | Leve (2px) | 0.1s | Cada kill |
| Boss kill | Forte (8px) | 0.3s | Uma vez |
| Levar dano | Leve (3px) | 0.12s | Cada dano |
| Explosão de urna | Alto (10px) | 0.25s | Cada uso |

**Importante**: Screen shake deve ter opção de redução/desativação nas configurações de acessibilidade (motion sensitivity).

### Particle Effects

**Morte de Vereador:**
- Alguns papéis de lei voam para cima (4-6 partículas)
- Pequenas notas de dinheiro (2-3 partículas)
- Crachá de vereador voa para longe com spin
- Pó de poeira laranja se espalha no ponto de impacto

**Morte de Assessor de Comunicação:**
- Press releases explodem em leque (8-10 papéis)
- Alguns flutuam para baixo devagar (efeito de papel caindo)
- Câmera invisível estala (SFX)

**Morte de Senador Vitalício:**
- Bengala voa para um lado
- Distintivo dourado sobe com brilho
- Confetes de "votação" (estrelinha, não círculos) em vermelho e amarelo
- Animação de "tombamento" longa e dramática (0.8s — inimigo pesado cai devagar)

**Morte de Boss (Candidato Eterno):**
- Pausa de 0.3s (hit stop prolongado) — o momento precisa de peso
- Explosão de bandeiras de partido rasgadas
- Score gigante aparece no centro da tela
- Tela brevemente branqueia (flash)
- Chuva de confetes por 2 segundos
- SFX: apuração eleitoral + multidão

**Explosão de Urna Eleitoral:**
- Papéis de voto voam em todas as direções (12-15 partículas)
- Pequenos confetes "apuração" (estrelinhas coloridas)
- Anel de impacto se expande (shockwave visual)
- SFX: BOOM seguido de "apuração de votos" em loop rápido

**Combo crescente:**
- A cada múltiplo de 10 no combo: o número explodir com partículas douradas antes de resetar para o novo valor
- x10: explosão pequena, x20: média, x30: grande, x40+: tela inteira com borda de luz dourada por 0.5s

### Sons

**Filosofia de design sonoro:** Cada arma tem uma identidade sonora que você reconhece sem ver a tela. Os zumbis têm falas que são engraçadas na primeira vez e *ainda funcionam* na centésima (timing, não conteúdo).

**Armas:**
- Vassoura: "THWACK" pesado + whoosh antes do impacto (madeira em movimento + madeira batendo)
- Chinelo: "WHOOSH" leve + "SLAP" de borracha (reconhecível imediatamente como brasileiro)
- Urna: "CLONK" metálico + "BOOM" de explosão + som de apuração
- Santinho: Som de impressora em loop + "WHOOSH" de papel cortando
- Microfone: Feedback de microfone + "WHAM" pesado

**Interface:**
- Toque em botão: "click" leve de papel
- Ganhar recompensa: som de cédula + moeda
- Transição de wave: fanfarra curta de banda de rua (zabumba + trompete)
- Power-up coletado: som de "caixinha de dinheiro" (clink-clink)
- Game over: som de microfone cortado + silêncio de 0.3s antes da tela aparecer

**Música:**
- Durante gameplay: loop de batida de baile funk distorcido + fundo de marchinha eleitoral
- Boss wave: música muda para algo mais tenso (versão menor da marchinha)
- Pós-boss: volta à versão triumfal da marchinha por 3 segundos, depois volta ao loop normal
- Menu: versão ambient da marchinha (mais lenta, mais melodiosa)
- Tudo deve funcionar com volume baixo ou até sem som (metrô sem fone)

### Vibração Háptica

| Evento | Padrão | Intensidade |
|---|---|---|
| Hit confirmado | Pulso único curto | Leve (10ms) |
| Hit crítico | Pulso duplo | Médio (15ms + 15ms) |
| Levar dano | Vibração contínua curta | Médio (30ms) |
| Morte | Vibração longa decrescente | Alto (50ms fade-out) |
| Boss kill | Padrão de confetes | Alto (3 pulsos com intervalos) |
| Power-up coletado | Pulso único suave | Muito leve (8ms) |
| Wave cleared | Pulso triplo progressivo | Médio (crescente) |

*Háptico deve ser desativável nas configurações — alguns jogadores acham intrusivo.*

### Animações de Personagem

**O personagem principal precisa de:**
- Idle: animação leve de respiração (2 frames, loop) — sinaliza que o jogo está vivo
- Corrida: animação expressiva com braço que segura a arma (4 frames)
- Ataque: animação de wind-up + impacto (3 frames) — não pode ser instantânea
- Dano: personagem "encolhe" por 2 frames antes de voltar
- Morte: queda teatral, exagerada, 8 frames

---

## 7. Onboarding — Os Primeiros 60 Segundos

### Princípio: O Jogo Ensina Jogando

Não existe tutorial. Não existe texto de instrução. O jogo ensina através de design — colocando o jogador em situações onde a ação correta é a mais intuitiva e a mais recompensadora.

### Os 60 Segundos Detalhados

**0s — Toque em "JOGAR":**
- Transição imediata para seleção de arma (sem loading screen maior que 1s)
- 3 cards visuais com imagem grande, nome curto, uma linha de flavor text
- Toque → destaque do card → preview de animação de ataque (1 segundo loop)
- Botão "IR PRA GUERRA" fica verde quando uma arma está selecionada

**3s — Chegada na Esplanada:**
- Personagem aparece no centro do mapa com animação de "olhar ao redor"
- Tudo visível: o mapa, as colunas, a gramado, o skyline
- Câmera dá um leve pan para mostrar o espaço disponível (1.5 segundos, automático)
- Silêncio de 0.5s antes da Wave 1 começar — cria antecipação

**5s — Primeiro Zumbi:**
- 1 único Vereador aparece ao longe, caminha em direção ao jogador
- O joystick não existe ainda — aparece quando o dedo toca na metade esquerda da tela
- Se o jogador não se mover em 3 segundos: seta contextual aparece apontando para o zumbi (desaparece em 2s)

**8s — Primeiro Ataque:**
- Botão de ataque aparece quando o zumbi fica a 150px de distância (ainda fora de alcance)
- Botão pulsa *suavemente* (não vibra em pânico — apenas diz "eu existo")
- Quando o jogador toca: THWACK + hit flash + número de score
- Primeiro kill: "TCHU-TCHU-TCHU" (contagem) + score grande + fala do zumbi

**15s — Volume cresce:**
- 3 Vereadores aparecem ao mesmo tempo de direções diferentes
- O joystick já foi descoberto; o desafio agora é coordenação
- Sem nenhuma instrução: o jogador aprende que pode se mover E atacar

**30s — Power-up drop:**
- Ao matar o 5o zumbi: primeiro power-up cai (Propina em Dinheiro Vivo — o mais simples)
- O item brilha e pulsa — convida a coletar sem instrução
- Ao coletar: velocidade aumenta perceptivelmente, ícone aparece no slot com contador regressivo
- O jogador entende: "mato zumbi → pego item → fico mais forte"

**45s — Wave 1 completa:**
- Todos os Vereadores morrem; tela exibe brevemente "WAVE 1 COMPLETA" (2s)
- Score da wave e XP ganho aparecem (simples, 3 segundos, sem interação necessária)
- Automático: Wave 2 começa com prep de 3 segundos

**60s — Assessor aparece:**
- O primeiro Assessor de Comunicação entra correndo em zigzag
- Lança um press release voador — o jogador leva o primeiro hit
- Flash vermelho + vibração leve + -1 coração
- Resposta instintiva: "tem que evitar o projétil" — aprendido por dano, não por aviso

**Por que isso funciona:**
- Cada mecânica é introduzida por necessidade, não por instrução
- O prazer da descoberta pertence ao jogador, não ao tutorial
- Cada nova situação cria um momento de "ah!" que o jogador sente como inteligência própria

---

## 8. Acessibilidade

### Daltonismo

**Problema:** Distinção entre vida (vermelho) e power-ups (verde) pode ser problemática para deuteranopia (1 em 12 homens brasileiros).

**Soluções:**
- HP representado por ícones (corações) em vez de cor pura — forma supera cor
- Power-ups têm ícones únicos por tipo — ícone é primário, cor é secundário
- Modo "alto contraste" nas configurações: substitui verde/vermelho por azul/amarelo
- Barras de vida dos inimigos: branca por padrão, não verde
- Dano crítico: ícone de estrela + cor dourada (não depende de "amarelo vs verde")

### Dificuldades Motoras

**Auto-aim suave (padrão ativo):**
- 30 graus de assistência por padrão (configurável: 0, 15, 30, 45 graus)
- Para jogadores com tremor ou baixa precisão motora: 45 graus de assistência disponível

**Tamanho dos alvos de toque:**
- Todos os botões: mínimo 48dp × 48dp (WCAG padrão)
- Botão de ataque: 72dp (generoso intencionalmente)
- Joystick dinâmico: raio de 60dp de detecção

**Pausa sem penalidade:**
- Botão de pausa sempre visível (canto superior esquerdo, 40dp)
- O jogo pode ser pausado a qualquer momento sem perda de estado
- Nenhuma mecânica exige reação rápida abaixo de 200ms para jogar no básico

**One-handed design verificado:**
- Todos os elementos interativos cabem no alcance natural do polegar direito (cone de 60% da tela)
- Joystick *dinâmico* é especificamente para acomodar diferentes tamanhos de mão

### Tamanho de Texto

- Escala de texto: 80% / 100% / 120% / 140% (nas configurações)
- Nenhum texto crítico de gameplay está abaixo de 14sp no 100%
- Falas dos zumbis (humor) podem ser ampliadas sem quebrar layout

### Sensibilidade a Movimento

- Screen shake: 3 níveis (nenhum / reduzido / completo) — padrão é "reduzido"
- Efeitos de flash intenso: opção de desativar flashes brancos de boss (importante para fotossensibilidade)
- Animações de câmera no menu: podem ser desativadas (modo de baixo movimento)

### Audio

- Todos os elementos críticos de gameplay têm feedback visual equivalente
- O jogo é 100% jogável sem som (feedback visual cobre tudo)
- Legenda para falas dos zumbis (on/off nas configurações)

---

## 9. Referências Culturais Brasileiras — O Tempero que Conecta

### Visual

**Estética Política Brasileira:**
- Santinhos de campanha (papel ruim, impressão de má qualidade, foto com sorriso forçado)
- Placa de obra pública com logo de prefeito (formato específico, prazos impossíveis)
- Bandeirolas de festa junina em cores de partido
- Crachá de servidor público (cor por órgão, foto 3x4 séria)
- Saco de dinheiro com cifra — não saco de banco internacional, saco de supermercado
- Faixa de "INAUGURAÇÃO" em toda obra (mesmo obra parada há 3 anos)

**Brasília específica:**
- Arquitetura Niemeyer em estado de uso real (pichações discretas, marcas de umidade)
- Grama ressecada (Cerrado brasileiro, não parque europeu)
- Fila para tudo — fila do SUS visível no cenário de fundo
- Placa "Não alimente os pombos" com pombos por toda parte

**Cultura Pop Brasileira:**
- Chinelo havaianas como arma (escolha cultural precisa — não "chinelo genérico")
- Vassoura de taquara (não vassoura "moderna" — a vassoura específica)
- Camisa polo de malha com bolso (o traje do servidor público não-executivo)
- Boné de empresa (presente em algumas skins)

### Sonoro

- Zabumba e trompete de marchinha política (fundo musical)
- Jingle de campanha distorcido como motivo do boss
- Som de apuração eleitoral (muito específico para brasileiro — inconfundível)
- "Mídia é golpista" como fala aleatória do Assessor
- Estática de rádio AM (transição entre waves)
- Baile funk como base rítmica do gameplay (BPM de 130 é o ritmo de combate ideal)

### Texto e Humor

**Regras do humor político de André Guedes:**
- Igualmente ácido com todos os lados (nenhuma facção política é poupada)
- Específico e reconhecível (não genérico: "o senador que apresentou 23 emendas sobre aquele tema específico que todo mundo viu no Twitter")
- Tem coração — a sátira não vem de ódio mas de decepção com aquilo que poderia ser melhor
- Absurdista: leva situações reais ao limite lógico absurdo

**Exemplos de textos de UI no estilo certo:**
- Botão de replay: "MAIS UMA SESSÃO LEGISLATIVA" (não "Replay")
- Game over: "SEU MANDATO ACABOU — aprovação: 3%" (não "Game Over")
- Seleção de arma: "ESCOLHA SUA PLATAFORMA DE GOVERNO" (não "Select Weapon")
- Configurações: "MINISTÉRIO DA PREFERÊNCIA PESSOAL"
- Loja: "CABIDE DA REPÚBLICA"
- Conquistas: "DIÁRIO OFICIAL"
- Score: "APROVAÇÃO POPULAR"
- Wave 1: "PRIMEIRA LEGISLATURA" / Wave 5 Boss: "COMISSÃO ESPECIAL"

**Flavor texts de armas (escritos na voz do universo André Guedes):**
- Vassoura: "A arma do povo desde sempre. Limpa o que o governo não limpa."
- Chinelo: "Tecnologia brasileira de precisão cirúrgica. Registrada na INPI."
- Santinho: "Vai perfurar qualquer um. Como sempre faz."

---

## 10. Mockups Descritivos — 7 Telas-Chave

### TELA 1: Home Screen / Menu Principal

**Composição visual:**
A Esplanada ao entardecer ocupa 70% da tela como plano de fundo vivo — não uma imagem estática, mas uma animação loop lenta. Alguns Vereadores-zumbi deambulam ao fundo sem ameaça (escala pequena, comportamento wandering suave). O Congresso Nacional na skyline, silhueta no laranja do fim de tarde. Partículas de santinho voando lentamente.

**Hierarquia de elementos (de cima para baixo):**
1. Logo "ZUMBIS DE BRASÍLIA" — fonte de manchete, encosta no topo, com assinatura "universo André Guedes" em tipo menor abaixo
2. Score pessoal em destaque: "MELHOR SCORE: 47.820" com pequena bandeira brasileira pixelada ao lado
3. Botão principal "JOGAR" — grande, centralizado, verde-tijolo sujo, ocupa 40% da largura
4. Botão secundário "ARMAS" — menor, à esquerda do JOGAR
5. Botão terciário "RANKING" — à direita do JOGAR
6. Ícone de configurações: canto superior direito, pequeno
7. Progresso de nível: barra discreta no rodapé, nível atual + XP para próximo

**Animações:**
- Botão JOGAR tem leve pulsação de escala (1.0 → 1.03 → 1.0, loop 2s)
- Logo tem animação de "trêmulo" de 2 frames (como se o título tivesse medo do próprio jogo)
- Zumbis ao fundo caminham; ocasionalmente um tropeça e levanta (animação cómica, 0.5% chance por frame)

**Atmosfera sonora:** Marchinha política em tom ambient, suave, loop de 30 segundos

---

### TELA 2: Seleção de Arma

**Composição:**
Tela modal sobre o menu (fundo escurece 60%). Três cards grandes lado a lado, ocupando 90% da largura.

**Cada card (aproximadamente 200dp × 280dp):**
- Imagem da arma desenhada no estilo André Guedes (ocupa 60% do card)
- Nome da arma em fonte de manchete: "VASSOURA DA DONA MARIA"
- Três ícones de atributo (alcance / dano / velocidade) — ícones visuais, sem números
- Flavor text em uma linha de fonte manuscrita: *"A arma do povo desde sempre"*
- Borda do card quando selecionado: laranja queimado com leve glow

**Interação:**
- Toque no card: anima a arma (preview de attack animation em loop)
- Card selecionado se expande ligeiramente (104% escala)
- Botão "IR PRA GUERRA" aparece na base, inativo (cinza) até selecionar uma arma

**Detalhe de design:** O texto de cada arma é escrito como se fosse panfleto de campanha da arma concorrendo a algum cargo: Vassoura "candidata a arma mais honesta do povo", Chinelo "sua arma para todas as situações", Santinho "aprovado por 100% das ruas".

---

### TELA 3: Gameplay — Mid-Session (Wave 4, Combo × 8)

**HUD ativo:**
- Topo esquerdo: 3 corações cheios + 1 meio + 1 vazio (personagem com 70% de vida)
- Topo centro: "WAVE 4" em laranja + "12 restantes" em tipo menor
- Topo direito: "23.450" em dourado, pulsando

**Área de jogo:**
- Personagem no centro, animação de corrida para a esquerda
- 3 Vereadores à direita, 1 Senador Vitalício à esquerda (avançando lento)
- 1 Lobista circulando pelo flanco superior
- Combo "×8" flutuando acima do personagem em laranja (ainda não chegou ao multiplicador)
- Power-up "CPI Imaginária" brilhando no chão à direita

**Partículas e efeitos ativos:**
- Rastro de movimento sutil no personagem (2-3 frames de trail)
- Press releases do Assessor morto ainda flutuando no ar
- Sombra do Senador avançando antes dele (aviso visual de chegada)

**HUD inferior:**
- Joystick dinâmico materializado onde o dedo está
- Botão de ataque pulsando (inimigo no alcance)
- Slot de power-up: vazio (ainda não coletou o que está no chão)

---

### TELA 4: Morte / Game Over

**Momento de impacto (0.3s antes da tela):**
- Screen shake forte (8px, 0.3s)
- Tela congela em branco por 2 frames
- Som de microfone cortado

**A tela em si:**

Fundo: foto do personagem caído, levemente desfocado, filtro de cor para sépia-amarelado sujo.

Elemento central — moldura de jornal rasgado com título:
```
━━━━━━━━━━━━━━━━━━━━━━━
  DIÁRIO DA REPÚBLICA
━━━━━━━━━━━━━━━━━━━━━━━
  SEU MANDATO ACABOU
  (aprovação: 3%)
━━━━━━━━━━━━━━━━━━━━━━━
  Wave chegada: 4
  Score final: 23.450
  Melhor combo: ×8
━━━━━━━━━━━━━━━━━━━━━━━
```

Abaixo do jornal, dois botões com estética de urna eleitoral:
- **[▶ CONTINUAR — ASSISTA 1 VÍDEO]** (verde-sujo, destaque)
- **[ENCERRAR SESSÃO]** (menor, texto simples)

No rodapé: "Você ficou na posição 847 no ranking desta semana" (em tipo pequeno, sempre visível)

**Animação:** O jornal aparece como se estivesse sendo jogado da câmera para o leitor (zoom-in dramático de 80% → 100% em 0.4s).

---

### TELA 5: Wave Cleared / Resultado de Wave

**Aparece automaticamente por 3 segundos, sem interação necessária:**

Sobreposição semi-transparente sobre o jogo (fundo não some totalmente — o campo de batalha ainda está visível).

```
╔══════════════════════════╗
║   WAVE 4 — CONCLUÍDA!    ║
║                          ║
║  +1.250 XP               ║
║  +80 MOEDAS COSMÉTICAS   ║
║  COMBO MÁXIMO: ×8        ║
║                          ║
║  [━━━━━━━━░░░░] Nív. 7   ║
║   520 / 1000 XP           ║
╚══════════════════════════╝
       WAVE 5 EM 3...
```

**Design:** Fundo da caixa tem textura de papel de jornal. A contagem regressiva "WAVE 5 EM 3..." usa estética de contador eleitoral. O jogo não para — apenas sobrepõe informação e continua.

**Se for boss wave (wave 5):**
A caixa muda de cor (laranja → vermelho), o texto "WAVE 5 — COMISSÃO ESPECIAL" aparece em estilo de alerta de rádio, e a música muda para o tema de boss.

---

### TELA 6: Resultado Final / Score Screen

**Após morte definitiva ou encerramento manual.**

**Layout de jornal completo (tela inteira):**

```
┌──────────────────────────────────┐
│  GAZETA DO PLENÁRIO              │
│  Edição Especial  — Hoje         │
├──────────────────────────────────┤
│                                  │
│  CIDADÃO RESISTE                 │
│  23 WAVES NA ESPLANADA           │
│                                  │
│  Score: 87.340      #234 Global  │
│  Melhor wave: 7     #89 Semanal  │
│  Zumbis: 156                     │
│  Combo máx: ×14                  │
│                                  │
├──────────────────────────────────┤
│  +2.100 XP  [█████░░░░░] Nív. 8 │
├──────────────────────────────────┤
│                                  │
│  [COMPARTILHAR]  [MAIS UMA!]     │
│                                  │
│  [MENU PRINCIPAL]                │
└──────────────────────────────────┘
```

**Botão "COMPARTILHAR":** Gera imagem com o design do jornal mais o score — pronto para TikTok/Instagram Stories. O share card tem o logo do jogo + score + wave + uma frase aleatória de humor político. Viral-first design.

**Botão "MAIS UMA!" é o maior e mais visível** — intencionalmente.

---

### TELA 7: Configurações / Ministério da Preferência Pessoal

**Título:** "MINISTÉRIO DA PREFERÊNCIA PESSOAL" em cima, com carimbo "CONFIDENCIAL" ao lado.

**Seções como documentos de pasta:**

*Pasta 1: Gameplay*
- Auto-mira: [OFF | 15° | 30° | 45°]
- Dificuldade: [VEREADOR | SENADOR | MINISTRO | CANDIDATO ETERNO]

*Pasta 2: Acessibilidade*
- Tremor de câmera: [Nenhum | Reduzido | Completo]
- Modo daltônico: [OFF | Deuteranopia | Protanopia]
- Flashes: [OFF | Reduzidos | Completos]
- Tamanho do texto: [A | A | A | A] (4 tamanhos)
- Vibração háptica: [ON | OFF]

*Pasta 3: Audio*
- Música: [slider 0-100%]
- SFX: [slider 0-100%]
- Falas dos zumbis: [ON | OFF]
- Legendas: [ON | OFF]

*Pasta 4: Privacidade*
- Ads personalizados: [ON | OFF]
- (Link para política de privacidade)

**Design:** Cada seção é uma "pasta de processo" diferente com grampo de metal no topo. Toggles parecem carimbos de aprovação/reprovação. Sliders parecem régua de medição de formulário antigo.

---

## Nota de Implementação para o Time

### Priorização para o MVP (Godot 4.4 / Samsung Galaxy A06)

**Crítico para MVP (sem isso, o jogo não funciona emocionalmente):**
1. Hit stop de 2-3 frames em todo impacto — é o item mais barato e de maior retorno em game feel
2. Hit flash (sprite pisca branco) + som único por arma
3. Score popup flutuante com bounce
4. Screen shake configurável (com opção de desativar)
5. Animação de morte única para cada tipo de zumbi
6. Joystick dinâmico (aparece onde o dedo toca)

**Importante para MVP mas pode ser simplificado:**
7. Partículas de morte (versão mínima: 3-4 sprites básicos por tipo de zumbi)
8. Haptic feedback (um pulso = um padrão, sem necessidade de biblioteca complexa)
9. Tela de game over com identidade visual correta

**Pode ser v1.0:**
10. Animações de boss completamente polidas
11. Sistema de compartilhamento de score com imagem gerada
12. Todas as falas de zumbi dubladas (text-to-speech pode cobrir o MVP)

### Performance Target (A06 — 4GB RAM, Snapdragon 460)

- 60 FPS durante gameplay com até 15 sprites ativos simultâneos
- Partículas: máximo 50 partículas ativas simultaneamente
- Screen shake: implementar como offset de câmera, não como movimento de sprites
- Sprites: máximo 512×512px por personagem, atlas de textura por cena
- Audio: mono para SFX, stereo apenas para música, OGG Vorbis (não WAV)

---

*"O jogo perfeito é aquele que o jogador não consegue parar de jogar — não porque seja viciante por design escuro, mas porque cada sessão deixa uma sensação boa. Esse é o jogo que vale construir."*

— Jenova Chen
