# ZUMBIS DE BRASILIA — Product Requirements Document
### O jogo que precisa ser divertido nos primeiros 5 segundos

**Documento de Produto | Abril 2026**
**Visao: Shigeru Miyamoto | Game Design e Produto**

---

> *"Quando eu assisti pela primeira vez alguem jogar Mario Bros, nao precisei de nenhuma explicacao. A pessoa tocou no botao, o Mario pulou, e ela sorriu. Esse sorriso e o produto. Todo o resto e embalagem."*

---

## 1. Visao do Produto

### O que faz este jogo DIVERTIDO

Antes de falar de mecanicas, tecnologia ou monetizacao, precisamos responder a pergunta mais importante: **por que alguem vai baixar este jogo as 23h numa quarta-feira depois de um dia horrivel e ficar jogando por 20 minutos?**

A resposta tem tres camadas:

**Camada 1: A Fantasia de Poder Imediata**
O Brasil vive uma exaustao coletiva com politica. Cada brasileiro tem uma lista mental de politicos que gostaria de "eliminar" — metaforicamente. Zumbis de Brasilia entrega exatamente isso: um politico-zumbi grotesco se aproxima babando, e voce o amassa com uma vassoura. O feedback e instantaneo, visceral e catartico. Isso nao e violencia — e humor fisico, no estilo das animacoes de Andre Guedes. O prazer nao vem da crueldade; vem do *reconhecimento* seguido da *resolucao*. Voce ve o Zumbi-Assessor de Comunicacao vindo em sua direcao com press releases e voce pensa "conheco esse sujeito" — e entao o despacha com um chinelo voador. Gargalhada garantida.

**Camada 2: O Loop que Vicia**
Um jogo de horde survival funciona porque o loop e perfeito na sua simplicidade: *ameaca cresce → voce responde → sobrevive um pouco mais → ameaca cresce de novo*. Cada segundo que passa, a tensao aumenta. Cada zumbi eliminado da uma pequena dose de dopamina. O jogador esta sempre 3 segundos antes de morrer. Isso e design de tension masterclass — e e o que faz jogos como Vampire Survivors, Brotato e Hades serem impossíveis de lagar.

**Camada 3: O Humor como Combustivel de Viralidade**
O humor politico de Andre Guedes nao e o prato principal — e o tempero que transforma um bom jogo num fenomeno cultural. Quando o Zumbi-Senador cai com animacao de "votacao perdida" e a legenda "Aprovado!" aparece em vermelho na tela, isso e um momento de screenshot. Quando o jogador morre e a tela de game over diz "Seu mandato acabou", isso e um momento de compartilhamento. O jogo precisa gerar esses momentos organicamente, a cada 30 segundos.

### Declaracao de Produto

**Zumbis de Brasilia e um jogo mobile de survival horde ambientado na Esplanada dos Ministerios, onde o jogador — um cidadao brasileiro armado com objetos cotidianos — enfrenta hordas de politicos-zumbis grotescos em ondas de dificuldade crescente. O core loop e tao imediato e satisfatorio que qualquer pessoa entende em 5 segundos e quer jogar mais uma wave sempre.**

### Principios de Design (Nao Negociaveis)

1. **Fun first, sempre.** Se uma mecanica nao e divertida no prototipo, ela nao entra — independente de quanto tempo custou fazer.
2. **Zero friccao na entrada.** O jogador deve estar em gameplay em menos de 30 segundos a partir do launch. Tutorial integrado ao gameplay, nao uma tela separada.
3. **Cada morte deve parecer justa.** O jogador nunca deve pensar "o jogo me matou". Ele deve pensar "eu errei — mais uma".
4. **O humor serve o gameplay.** Nenhuma piada politica pode interromper o fluxo. Ela aparece no contexto da acao, nunca pausa o jogo.
5. **Jogue com uma mao.** Celular. Metrô. Fila do banco. O jogo funciona com polegar unico.

---

## 2. Core Game Loop

### O Loop de 30 Segundos que Vicia

O loop central do jogo tem tres niveis de duração. A magia esta em como eles se encaixam:

**Loop Micro (3-5 segundos):**
Zumbi se aproxima → jogador mira com joystick → ataca → zumbi morre → drop de recurso → coleta → proximo zumbi

**Loop Medio (30-90 segundos — uma wave):**
Wave comeca → zumbis aparecem progressivamente → tensao aumenta → wave boss entra → jogador usa power-up → sobrevive → resultado da wave → recompensa → proxima wave

**Loop Macro (uma sessao de 5-15 minutos):**
Seleciona arma inicial → sobrevive waves → acumula score → morre eventualmente → ve posicao no leaderboard → opção de rewarded ad para continuar → repete ou fecha

### Diagrama do Core Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                     SESSAO DE JOGO                              │
│                                                                 │
│  ┌───────────┐    ┌──────────────┐    ┌─────────────────────┐  │
│  │  TELA     │───▶│  WAVE INICIA │───▶│  GAMEPLAY (20-90s)  │  │
│  │ INICIAL   │    │  (5s prep)   │    │                     │  │
│  └───────────┘    └──────────────┘    │  Zumbis aparecem ↓  │  │
│         ▲                             │  Jogador se move ↓  │  │
│         │                             │  Ataca + Coleta  ↓  │  │
│         │                             │  Combo cresce    ↓  │  │
│         │                             │  Boss wave ↑     ↓  │  │
│         │                             └──────────┬──────────┘  │
│         │                                        │             │
│         │                         ┌──────────────▼──────────┐  │
│         │                         │   SOBREVIVEU A WAVE?    │  │
│         │                         └──────┬──────────┬───────┘  │
│         │                                │ SIM      │ NAO      │
│         │                    ┌───────────▼──┐   ┌───▼────────┐ │
│         │                    │  RECOMPENSA  │   │  MORREU    │ │
│         │                    │  +Moedas     │   │            │ │
│         │                    │  +Power-up   │   │ Score final│ │
│         │                    │  +Upgrade?   │   │ Leaderboard│ │
│         │                    └───────┬──────┘   │ Rewarded Ad│ │
│         │                            │          │ Continuar? │ │
│         │                    ┌───────▼──────┐   └─────┬──────┘ │
│         │                    │ PROXIMA WAVE │         │        │
│         │                    │ (dificuldade │    SIM  │  NAO   │
│         │                    │  crescente)  │         │        │
│         │                    └──────────────┘  +1 vida│  Game  │
│         │                                       ▲      │  Over  │
│         └───────────────────────────────────────┘      │        │
│                                                         ▼        │
│                                               TELA FINAL / SHARE │
└─────────────────────────────────────────────────────────────────┘
```

### O Momento da Virada (por que "mais uma wave" e inevitavel)

O design usa um principio classico: **a proxima wave sempre parece possivel**. Quando o jogador morre, ele esta com 80% de clareza sobre o que fez de errado. Ele sabe que se tivesse usado aquele power-up 10 segundos antes, teria sobrevivido. Isso e o gancho. Nao e o jogo sendo dificil — e o jogo sendo **justo o suficiente** para que o jogador acredite que pode ganhar na proxima tentativa.

---

## 3. Mecanicas de Gameplay

### 3.1 Controles Touch

**Principio**: Funcionar com polegar direito em telas de 5" a 7". Zero frustração de controle.

**Joystick Virtual (esquerda)**
- Posicao: canto inferior esquerdo, raio de 60dp
- Movimento: 8 direcoes, velocidade proporcional a distancia do centro
- Snap automatico: joystick "aparece" onde o dedo toca na metade esquerda da tela (nao fixo)
- Animacao do personagem sincronizada com direcao

**Botao de Ataque (direita)**
- Posicao: canto inferior direito
- Logica: toque simples = ataque na direcao do movimento ou do inimigo mais proximo (auto-aim suave)
- Hold: armas com carga seguram o ataque
- Feedback haptico leve em cada hit confirmado

**Swipe especial (opcional, para power-ups)**
- Swipe rapido na tela com segundo dedo = ativa power-up coletado
- Design intencional: maos nao precisam se mover

**Auto-mira Assistida (ajustavel)**
- Angulo de assistencia: 30 graus (pode ser desativado nas configuracoes)
- Prioriza inimigos com mais hp, tiebreak por distancia
- Nunca substitui o controle — apenas suaviza angulos proximos

**Por que sem dual stick puro:**
O dual stick tradicional (como em shooters) exige coordenacao que inviabiliza jogar com uma mao no transporte. O sistema de "move + auto-aim suave" permite jogar no metrô, na fila, com o celular numa mao.

### 3.2 Sistema de Combate

**Hit Feel (o mais importante)**
O combate so e satisfatorio se o *hit feel* for bom. Isso nao e subjetivo — e tecnico:
- Hit stop: 2-3 frames de "congelamento" no impacto (sensacao de peso)
- Screen shake: leve em hits normais, forte em kills e combos
- Hit flash: sprite do inimigo pisca branco por 1 frame
- Pop de score: numero flutuante colorido com velocidade e escala proporcional ao dano
- Audio: cada arma tem SFX de impacto distinto e satisfatorio (vassoura = "THWACK", chinelo = "FLAP-BAM")

**Sistema de Dano**
- Cada zumbi tem barra de vida visivel (simples, acima da cabeca)
- Dano baseado em: arma base + multiplicador de combo + modificador de poder do inimigo
- Critico: 10% de chance, 2x dano, efeito visual dourado
- Headshot: area de hit na cabeca = 1.5x dano (incentiva mirar alto)

**Combo System**
- Contador de combo: sobe a cada kill sem levar dano
- Multiplicador: x1 (0-4 kills) → x1.5 (5-9) → x2 (10-19) → x3 (20-29) → x4 (30+)
- Timer de combo: 3 segundos sem kill reinicia o contador
- Visual: numero de combo fica maior e mais chamativo conforme sobe
- Som: pitch do SFX de kill sobe conforme combo cresce (feedback auditivo de progresso)

**Knockback e Movimentacao**
- Zumbis tem knockback variavel por tipo (leve para pesados, alto para fracos)
- Jogador nao tem knockback — apenas animacao de dano e invencibilidade de 0.5s
- Empurrar zumbis uns nos outros e mecanica valida e recompensada (bonus de score)

### 3.3 Movimento e Posicionamento

O mapa da Esplanada e aberto mas tem estrutura: colunas dos ministerios, gramados, escadarias. O posicionamento e mecanica emergente — nao explicada, descoberta:

- **Kiting**: correr enquanto ataca com arma ranged
- **Chokepoint**: usar colunas para canalizar zumbis em fila
- **Rooftop escape**: subir escadarias da Esplanada separa o player dos zumbis lentos
- **Aglomeracao bonus**: eliminar 3+ zumbis simultaneos com ataque em area = bonus de score

### 3.4 Arsenal de Armas (MVP: 3-5 armas)

| Arma | Tipo | Alcance | Dano Base | Cadencia | Flavor Text |
|---|---|---|---|---|---|
| **Vassoura da Dona Maria** | Melee | Curto | Alto | Media | "A arma do povo desde sempre" |
| **Chinelo Voador** | Ranged | Medio | Baixo | Alta | "Tecnologia brasileira de precisao cirurgica" |
| **Urna Eleitoral** | Area (throw) | Curto-Medio | Medio | Baixa (cooldown 8s) | "Um voto de confianca... no seu cranio" |
| **Santinho de Campanha** | Ranged (pierce) | Longo | Baixo | Alta | "Vai perfurar qualquer um. Como sempre." |
| **Microfone de Palanque** | Melee pesado | Curto | Muito alto | Muito lenta | "Para dar uma palavra final" |

**Dinamica de selecao de arma (MVP):**
- O jogador escolhe 1 arma ao iniciar a partida
- Power-ups dropados por zumbis podem dar acesso a arma secundaria temporaria (30s)
- A arma inicial e uma escolha de playstyle: Vassoura (tanky, corpo a corpo) / Chinelo (kiting, distancia) / Santinho (pierce, horde clear)

**Feel de cada arma precisa ser distinto:**
- Vassoura: animacao de swing ampla, som grosso, pausa pos-ataque (peso real)
- Chinelo: animacao de lancamento snap, som de "whoosh-slap", bounce no inimigo
- Urna: animacao de arremesso, explosao com papeis e confetes voando, som de apuracao
- Santinho: stream continuo de papeis voando, som de impressora, vai atravessando zumbis

### 3.5 Power-ups (drops de zumbis)

Power-ups aparecem como drops aleatorios ao matar zumbis. Duram 10-20 segundos ou tem uso unico.

| Power-up | Efeito | Gatilho de Drop | Descricao Humoristica |
|---|---|---|---|
| **Propina em Dinheiro Vivo** | +50% velocidade de movimento por 15s | Zumbi-Lobista | "Correr e mais facil com os bolsos cheios" |
| **CPI Imaginaria** | Congelamento de todos os zumbis por 5s | Boss wave | "Nada paralisa um politico como uma CPI" |
| **Tapa de Vassoura Sagrada** | 3x dano por 10s | Combo x20+ | "Energizado pela raiva do contribuinte" |
| **Escudo Constitucional** | Invulnerabilidade por 4s | Levar dano critico | "Nenhuma lei se aplica por alguns segundos" |
| **Pit-stop do Carro-Pipa** | Cura 30% da vida | Zumbi especial | "Agua, finalmente. Obrigado, TCU" |
| **Orçamento Impositivo** | Dupla pontuacao por 20s | Wave 5+ | "Dinheiro que aparece do nada" |

**Regra de design**: Cada power-up precisa de um *momento de uso* claro. O jogador deve imediatamente entender quando usar "CPI Imaginaria" (quando cercado) vs "Tapa Sagrada" (quando esta com combo alto).

---

## 4. Sistema de Progressao

### Filosofia: Progressao Sem Pay-to-Win

Toda progressao e baseada em habilidade e tempo jogado — nunca em dinheiro gasto. Um jogador F2P tem acesso a exatamente o mesmo power de combate que um pagante. O pagante apenas tem cosmeticos diferentes. Essa nao e apenas uma escolha etica — e uma escolha de design: jogos onde o dinheiro compra poder destroem o sentimento de conquista para todos.

### 4.1 Progressao de Personagem (MVP)

**Sistema de Nivel Local**
- Cada partida termina com XP ganho (baseado em score, waves, combo max)
- Level 1-20 para o MVP (expandido em v1.0)
- A cada level: escolha entre 1 de 3 upgrades permanentes

**Arvore de Upgrades (MVP — 20 niveis)**

| Nivel | Upgrade Disponivel (escolhe 1 de 3 aleatorios) |
|---|---|
| 2 | +10% velocidade / +1 vida maxima / +15% dano base |
| 4 | Combo demora 1s a mais para resetar / Drops de power-up 20% mais frequentes / +20% alcance |
| 6 | Critico chance +5% / Cura 5% ao completar wave / +1 uso de Rewarded Ad por sessao gratis |
| 8 | Headshot dano +25% / Knockback aumentado / Spawn de power-up raro desbloqueado |
| 10 | **MILESTONE**: Desbloqueia skin cosmética (3 opcoes) |
| ... | Continua com upgrades progressivamente mais interessantes |
| 20 | **MILESTONE**: Personagem alternativo desbloqueado |

**Nota de design**: Os upgrades nao devem ser numericos chatos. Cada um muda *como* o jogador joga, nao apenas o quao forte ele e. "Combo nao reseta por 1s a mais" muda a estrategia. "+5% de dano" e esquecivel.

### 4.2 Sistema de Records e Conquistas

**Leaderboard Semanal** (Firebase)
- Top 100 global
- Posicao do jogador sempre visivel (mesmo fora do top 100)
- Reset toda segunda-feira, recompensa cosmética para top 10

**Conquistas Locais** (sem server, MVP)
- "Primeira Sangria": kill 100 zumbis total
- "Faxina Nacional": complete 10 waves sem morrer
- "Combo Presidencial": atinja combo x30
- "Resistencia Economica": sobreviva 10 minutos numa partida
- "Heroi do Povo": compartilhe score 5 vezes
- Conquistas dao moedas cosmeticas (sem impacto em gameplay)

### 4.3 Progressao de Missoes Diarias (v1.0)

Missoes diarias geram engajamento recorrente sem forcar o jogador:
- "Mate 50 zumbis usando apenas o Chinelo"
- "Complete 3 waves sem usar power-up"
- "Atinja combo x15 em uma partida"
- Recompensa: moedas cosmeticas, XP bonus

---

## 5. Tipos de Zumbi

### Filosofia de Design dos Zumbis

Cada tipo de zumbi cumpre uma funcao mecanica E tem uma piada politica integrada no comportamento. O humor nao e decoracao — ele **explica** a mecanica. "Zumbi-Lobista vem de lado" nao e apenas design aleatorio; e piada e mecanica ao mesmo tempo.

**Os 7 Tipos do MVP:**

---

### Zumbi #1 — O Vereador
**Tier de ameaca**: Basico  
**Apelido interno**: "Carne de canon"  
**Visual**: Terno barato rasgado, crachá de vereador pendurado torto, expressao vaga  
**Comportamento**: Caminha diretamente em direcao ao jogador em linha reta. Velocidade media. Pouca vida. Ataque lento de "abraco voraz".  
**Habilidade especial**: Nenhuma. E o mais simples.  
**Spawn**: Grupos de 3-5. Aparecem desde a wave 1.  
**Mecanica de humor**: Ao morrer, grita "Fui eleito democraticamente!" e cai de brucos. Ao acertar o jogador, diz "Tenho imunidade parlamentar!"  
**Funcao de design**: Ensinar os controles basicos. Faceis de matar, criam densidade de horde.

---

### Zumbi #2 — O Assessor de Comunicacao
**Tier de ameaca**: Medio  
**Apelido interno**: "Spam"  
**Visual**: Camisa social branca manchada, pilha de press releases na mao, cabelo de apresentador de telejornal  
**Comportamento**: Corre em zigzag. Para de 3 em 3 segundos para "lancar press release" — projétil de papel voador que causa dano leve mas atordoa por 0.3s.  
**Habilidade especial**: Lanca 3 santinhos ao mesmo tempo ao morrer (evitar area).  
**Spawn**: Individual ou duplas. Wave 2+.  
**Mecanica de humor**: Ao ser atingido, grita "Isso e Fake News!". Ao matar o jogador: "A narrativa prevaleceu."  
**Funcao de design**: Introduz projétil inimigo. Forca o jogador a nao ficar parado.

---

### Zumbi #3 — O Senador Vitalicio
**Tier de ameaca**: Tanque  
**Apelido interno**: "Blindado"  
**Visual**: Terno de tres pecas, distintivo dourado, bengala como arma, expressao soberba  
**Comportamento**: Extremamente lento, mas com o dobro de vida de qualquer outro zumbi. Ao atingir 50% de vida, ativa "Imunidade Parlamentar": invulneravel por 3s, continua avancando.  
**Habilidade especial**: "Reeleicao" — ao chegar a 10% de vida, ganha +30% velocidade por 5s.  
**Spawn**: Individual ou maximo em dupla. Wave 3+.  
**Mecanica de humor**: Ao entrar em tela: tema musical de senado. Ao ativar imunidade: um escudo translucido em forma de balsa aparece. Ao morrer: "Tenho foro privilegiado mesmo depois de morto!"  
**Funcao de design**: Ensina o jogador a manter distancia, usar kiting, e que nem todo inimigo deve ser atacado diretamente. E o primeiro teste de paciencia.

---

### Zumbi #4 — O Lobista
**Tier de ameaca**: Esquivo  
**Apelido interno**: "Cobra"  
**Visual**: Terno elegante, pasta de couro, oculos escuros, sorriso permanente  
**Comportamento**: Nao ataca diretamente. Circula o jogador pelos flancos. Ao ficar proximo, "corrompe" outros zumbis proximos: os zumbis afetados ficam com +50% de velocidade por 5s.  
**Habilidade especial**: "Emenda" — ao ser atacado de frente, esquiva para o lado automaticamente (50% de chance).  
**Spawn**: Sempre sozinho, mas sempre perto de grupo. Wave 4+.  
**Mecanica de humor**: Quando corrompe outros zumbis: maletinha dourada voa e as notas de dinheiro se espalham. Ao morrer: "Fui mal assessorado!"  
**Funcao de design**: Forca o jogador a mudar o foco e prioritizar targetting. E o primo esperto do Senador Vitalicio.

---

### Zumbi #5 — A Ministra da Economia
**Tier de ameaca**: Especial / Controlador  
**Apelido interno**: "Nervo"  
**Visual**: Terninho, planilhas voando ao redor, calculadora na mao, expressao de quem esta sempre cortando algo  
**Comportamento**: Nao ataca fisicamente. Cria "Zonas de Corte Orcamentario" — areas no chao onde o jogador recupera vida 50% mais devagar e power-ups expiram 2x mais rapido.  
**Habilidade especial**: Ao morrer, dropa "Emenda Constitucional" — power-up especial que cancela todas as zonas de corte e cura 15% da vida do jogador.  
**Spawn**: 1 por wave boss. Wave 5+.  
**Mecanica de humor**: As zonas sao visualizadas como "orçamento contingenciado" (area cinzenta com graficos de queda). Ao criar zona: "Nao existe almoço gratis!"  
**Funcao de design**: Elemento de controle de espaco. Forca o jogador a se mover e a priorizar eliminar ela.

---

### Zumbi #6 — O Candidato Eterno
**Tier de ameaca**: Boss (aparece como boss de wave)  
**Apelido interno**: "Imortal"  
**Visual**: Combinacao grotesca de terno e carisma artificial — sorriso enormemente exagerado, cabelo impossivel, bandeiras de partido rasgadas  
**Comportamento**: Boss de wave. 3x mais vida que Senador Vitalicio. Ataque em area com "discurso": ondas sonicas que empurram o jogador. Invoca 2 Vereadores a cada 20 segundos.  
**Habilidade especial**: "Segundo Turno" — ao morrer pela primeira vez, levanta com 25% da vida, animacao de "voce realmente achou que eu ia desistir?". Morre definitivamente na segunda vez.  
**Spawn**: Boss da wave 5, wave 10, e cada 5 waves subsequentes.  
**Mecanica de humor**: Ao reaparecer: "VOLTO EM 4 ANOS (ou antes, quem sabe)". Ao morrer definitivamente: resultado eleitoral falso na tela — "Candidato Eterno - 0 votos".  
**Funcao de design**: Momento climático da wave. Requer que o jogador gerencie adds e foque o boss. O "segundo turno" e a surpresa que ensina a nao baixar a guarda.

---

### Zumbi #7 — O Servidor Fantasma
**Tier de ameaca**: Suporte / Multiplicador  
**Apelido interno**: "Invisivel"  
**Visual**: Terno com carimbo "CARGO COMISSIONADO", praticamente transparente, so visivel por outline  
**Comportamento**: Se move invisivelmente (apenas outline visivel). Ao chegar proximo ao jogador, "carimba" um debuff: -20% velocidade de movimento por 8s. Acumula com outros Fantasmas.  
**Habilidade especial**: Ao morrer, drooa "Aviso de Exoneracao" — remove todos os debuffs de velocidade ativos.  
**Spawn**: Grupos de 3-4. Wave 6+.  
**Mecanica de humor**: Ao aplicar debuff: som de carimbo repetido. Ao morrer: "Fui exonerado... mas volto no proximo governo."  
**Funcao de design**: Cria urgencia e desordem. O jogador precisa elimina-los mesmo sendo "chatos" em vez de ameacadores.

---

### Tabela Resumo dos Zumbis

| Zumbi | Vida | Velocidade | Ameaca Principal | Wave de Estreia |
|---|---|---|---|---|
| Vereador | Baixa | Media | Volume / Horde | 1 |
| Assessor | Baixa | Alta | Projétil / Zigzag | 2 |
| Senador Vitalicio | Alta | Lenta | Tanque / Imunidade | 3 |
| Lobista | Media | Media | Buff inimigos | 4 |
| Ministra Economia | Baixa | Media | Controle de espaco | 5 |
| Candidato Eterno | Boss | Media | Boss / "Segundo Turno" | Wave 5 (boss) |
| Servidor Fantasma | Baixa | Alta | Debuff invisivel | 6 |

---

## 6. Mapa: Esplanada dos Ministérios

### Por que a Esplanada e o Mapa Perfeito para o MVP

A Esplanada nao e escolhida por ser famosa — e escolhida por ser um design de mapa excepcional para survival horde:
- **Eixo central longo**: Permite kiting e corridas. Zumbis precisam percorrer distancia.
- **Obstaculos naturais**: Colunas dos ministerios criam chokepoints organicos.
- **Elevacao**: Escadarias dos blocos criam posicoes elevadas (vantagem de visibilidade, desvantagem de fuga).
- **Espaco aberto com ilhas**: Gramados entre os blocos criam arenas naturais.
- **Reconhecimento imediato**: Todo brasileiro reconhece o Congresso ao fundo. E imersivo sem precisar de exposicao.

### 6.1 Layout do Mapa

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  [CONGRESSO - FUNDO] ← skyline, nao interagivel                │
│                                                                 │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐           │
│  │  M1  │  │  M2  │  │  M3  │  │  M4  │  │  M5  │           │
│  │ Bloco│  │ Bloco│  │ Bloco│  │ Bloco│  │ Bloco│  ← MINISTERIOS │
│  │  A   │  │  B   │  │  C   │  │  D   │  │  E   │           │
│  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘           │
│     │         │         │         │         │               │
│     ══════════════════EIXO MONUMENTAL═══════════             │
│     │         │         │         │         │               │
│  [GRAMADO A] [ESPELHO  [GRAMADO B][JARDIM C][ESTAC]          │
│              D'AGUA]                                          │
│                                                               │
│  [SPAWN ZONE A] ←→ [ARENA CENTRAL] ←→ [SPAWN ZONE B]        │
│                                                               │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Zonas do Mapa e Funcoes de Design

**Eixo Monumental (corredor central)**
- Area mais ampla do mapa
- Zona de kiting principal: boa para armas ranged
- Spawn de zumbis nas extremidades
- Sem obstaculos: vulneravel mas com visibilidade total
- Tiles: concreto historico + gramado lateral

**Blocos dos Ministerios (norte e sul do eixo)**
- Colunas sao obstaculos que bloqueiam tanto zumbis quanto projéteis
- Escadarias = elevacao (leve vantagem estrategica)
- Espaços entre colunas = chokepoints naturais para armas de area
- Tiles: marmore branco + sombra dramatica das colunas

**Gramados e Jardins (areas abertas laterais)**
- Mais lentos para mover (animacao de "lama de obra publica")
- Spawn secundario de zumbis comuns
- Power-up drops mais frequentes nestas areas
- Visual: grama seca (um detalhe politico subtil — nao rega o jardim publico)

**Espelho D'Agua**
- Obstaculo intransponivel (ambos os lados)
- Cria divisao natural do mapa — force decisao de qual lado segurar
- Visual bonito: reflexo do Congresso invertido na agua
- Easter egg: alguns zumbis caem e afundam dramaticamente

**Parking / Estacionamento (extremidade leste)**
- Zona de spawn de Servidores Fantasma especificamente
- Carros capotados como obstaculos pequenos (cobertura parcial)
- Ambiente mais fechado: desvantagem para jogador kiter, vantagem para melee

### 6.3 Pontos de Interesse e Landmarks

| Ponto | Funcao Mecanica | Funcao de Humor |
|---|---|---|
| **Placa "Ministerio de X"** | Marco visual de zona de spawn | Cada placa tem nome de ministerio inventado: "Min. da Bagunca", "Min. do Puxadinho" |
| **Cabine de Votacao Abandonada** | Ponto de spawn de power-up garantido por wave | "A democracia estava aqui" |
| **Helicoptero Quebrado** | Obstáculo imóvel com cobertura parcial | Tem placa "Manutencao Preventiva desde 1987" |
| **Ambulancia da Saude Publica** | Ponto de cura passiva (fila, e claro) | Jogador precisa esperar 3 segundos parado para curar (satirizando filas do SUS) |
| **Mesa de Buffet do Jantar de Gala** | Drop de power-up de score duplo | "Comida do contribuinte — ajuda a ganhar mais pontos" |

### 6.4 Iluminacao e Atmosfera

- **Horario**: Anoitecer (dourado-alaranjado). Cores quentes amplificam o grotesco das caricaturas.
- **Parallax**: 4 camadas — ceu (nuves lentas), Congresso ao fundo, postes e arvores, chao.
- **Iluminacao dramatica**: Zumbis tem sombra que avanca antes deles — aviso visual de chegada.
- **Efeitos de ambiente**: Papel de santinho voando constantemente. Confetes de resultado eleitoral ocasionais. Pomba de paz morta de vez em quando.
- **Skyline**: Congresso, Catedral (silhueta ao fundo), Torre de TV (extrema direita), Torre Digital (extrema esquerda).

---

## 7. Monetizacao — MVP (Apenas Ads)

### Principio Fundamental

No MVP, a unica fonte de receita e publicidade. Isso nao e limitacao — e estrategia. Remover o atrito de IAP no primeiro contato com o jogador maximiza o crescimento organico. Um jogador feliz que nunca gastou um centavo recomenda o jogo. Um jogador que sentiu pressao de compra abandona e deixa review negativa.

### 7.1 Rewarded Video Ads ("Ads com Valor")

O rewarded ad so aparece quando o jogador *quer* — nunca e forcado.

**Gatilho de morte (principal)**
- Ao morrer, tela mostra: "Quer continuar? Assista 1 video e ganhe 1 VIDA EXTRA"
- Visual: personagem deitado no chao, botao "CONTINUAR" com icone de video
- Timing: aparece automaticamente 1.5s apos a morte (nao imediato — espera o jogador processar o game over)
- Limite: max 2 rewarded ads de revive por sessao (evita abuse e mantem desafio)
- Frequencia: disponivel em toda partida

**Gatilho de power-up (secundario)**
- No menu inicial: "Assista um video e comece com 1 power-up aleatorio"
- Aparece como botao opcional, nunca popup

**Gatilho de bonus de score (opcional)**
- Ao terminar uma partida (morte natural, sem revive): "Dobre seu score para o leaderboard. Assista 1 video."
- Apenas efeito cosmetico no ranking — nao afeta progression

**Regras de ouro para rewarded ads:**
1. O jogador NUNCA e interrompido durante gameplay por um ad
2. O botao de "nao obrigado" e sempre visivel e imediatamente clicavel
3. O reward e imediato e satisfatorio (nao "ganhou 5 moedas que nao significam nada")

### 7.2 Interstitial Ads ("Ads de Transicao")

Ads que aparecem entre sessoes, nunca durante gameplay.

**Quando aparecem:**
- A cada 3 partidas completas (nao waves, partidas inteiras)
- Na transicao entre "tela de game over → tela inicial" — nunca na volta ao jogo
- Nunca duas vezes seguidas

**Controle de frequencia:**
- Maximo 4 interstitials por hora por jogador
- Nao aparece nas primeiras 2 partidas do jogador (onboarding protegido)
- Nao aparece se o jogador acabou de ver um rewarded ad (menos de 5 minutos)

**Formato preferido:** Video curto 15s com skip apos 5s, ou banner que fecha apos 5s. Sem ads de audio forcado.

### 7.3 Metricas de Ads Esperadas (MVP)

| Metrica | Target Conservador | Target Base | Fonte |
|---|---|---|---|
| Rewarded Ad Rate | 25% das mortes | 40% das mortes | Benchmark mobile BR |
| Interstitial CTR | 1.5% | 2.5% | AdMob BR media |
| eCPM Rewarded (BR) | R$ 15 | R$ 25 | AdMob benchmarks 2025 |
| eCPM Interstitial (BR) | R$ 8 | R$ 15 | AdMob benchmarks 2025 |
| Ads por sessao (media) | 1.2 | 2.0 | Baseado em sessao de 7 min |
| **ARPDAU (so ads)** | **R$ 0,04** | **R$ 0,08** | Calculado |

### 7.4 Integracao Tecnica de Ads

- **Plataforma**: AdMob (Google) como rede primaria
- **Mediacao**: LevelPlay (AppLovin) para maximizar eCPM com multiplas redes
- **Redes secundarias**: Unity Ads, Meta Audience Network, Pangle
- **LGPD**: Banner de consentimento na primeira sessao. Opcao de opt-out de ads personalizados (mantendo ads genericos).
- **Implementacao Godot**: godot-admob-plugin (Poing Studios) — maduro e mantido

---

## 8. Monetizacao — v1.0+ (Battle Pass, Skins, IAP)

### Cronograma de Ativacao

A monetizacao paga so e ativada quando o jogo provar produto-mercado fit:
- **Gate para ativar**: D7 retention > 18% E MAU > 50.000 por 4 semanas consecutivas
- **Se gate nao for atingido**: Continuar apenas com ads, investigar problemas de retencao antes de adicionar IAP

### 8.1 Battle Pass Sazonal ("Temporada X: [Nome Politico]")

**Preco**: R$ 14,90/temporada (30 dias)
**Estrutura**: 30 niveis, recompensas por nivel completadas via gameplay

| Nivel | Recompensa Gratis (track basico) | Recompensa Battle Pass (premium) |
|---|---|---|
| 1 | 100 moedas cosmeticas | Moldura de perfil exclusiva da temporada |
| 5 | Emote de vitoria basico | Skin de arma tematica |
| 10 | Conquista de temporada | Skin de personagem "Candidato" |
| 15 | 200 moedas cosmeticas | Animacao especial de morte de zumbi |
| 20 | Titulo de jogador | Trilha sonora de campanha customizada |
| 25 | Emblema de temporada | Power-up cosmético (nao afeta gameplay) |
| 30 | 500 moedas cosmeticas | **Skin Lendaria Exclusiva** + Titulo Permanente |

**Principios do Battle Pass:**
- 100% dos niveis atingiveis jogando ~20-30 min/dia (sem farming excessivo)
- Recompensas do track gratis sao genuinamente uteis (moedas, nao detritos)
- Skins lendarias do BP nao sao vendidas separadamente (exclusividade gera FOMO saudavel)
- Temporada dura exatamente 30 dias — nunca extendida (cria urgencia real)

### 8.2 Loja de Cosmeticos ("Cabide da Republica")

**Skins de Personagem** (nao afetam gameplay, exceto animacoes)

| Skin | Preco | Descricao |
|---|---|---|
| **Coxinha Raivoso** | R$ 9,90 | Visual de manifestante anti-tudo com bandeira do Brasil |
| **Mortadela Saudoso** | R$ 9,90 | Boina vermelha, camiseta de partido, sorriso de quem sabe o que e bom |
| **Cabo Eleitoral** | R$ 7,90 | Colete de cabos, celular na mao, 1000 santinhos |
| **Influencer Politico** | R$ 12,90 | Ring light no personagem, sempre filmando os zumbis |
| **Jornalista Investigativo** | R$ 7,90 | Gravador, bloco de notas, sempre olhando pro lado |
| **Cidadao do Futuro** | R$ 19,90 | Skin especial: o Brasil que poderia ter sido |

**Skins de Arma**

| Skin | Arma Base | Preco | Descricao |
|---|---|---|---|
| **Vassoura Dourada** | Vassoura | R$ 4,90 | Com alca de ouro macico (provavelmente de fundo de pensao) |
| **Chinelo Versace** | Chinelo | R$ 4,90 | Grife importada para pés do povo |
| **Urna Criptografada** | Urna | R$ 6,90 | Versao high-tech com QR code e blockchain |
| **Santinho em 4K** | Santinho | R$ 3,90 | Fotografado por fotografo eleitoral profissional |
| **Microfone do Debate** | Microfone | R$ 6,90 | Modelo premium, nunca cortado pela moderacao |

**Emotes e Reacoes**

| Emote | Preco | Uso |
|---|---|---|
| **"E isso aí"** | R$ 2,90 | Ao completar wave |
| **"Parabens ao vencedor"** | R$ 2,90 | No leaderboard |
| **"Voto Nulo"** | R$ 1,90 | Emote de derrota (ironia maxima) |
| **Danca Eleitoral** | R$ 3,90 | Idle animation customizada |

### 8.3 IAP Diretos (v1.0+)

| Item | Preco | O que e |
|---|---|---|
| **Remover Interstitial Ads** | R$ 7,90/mes | So para interstitials. Rewarded ainda disponivel por escolha. |
| **Pacote de Moedas P** | R$ 4,90 = 500 moedas | Apenas cosméticos |
| **Pacote de Moedas M** | R$ 9,90 = 1.200 moedas | Apenas cosméticos |
| **Pacote de Moedas G** | R$ 19,90 = 2.800 moedas | Apenas cosméticos |
| **Starter Pack** (30 dias apos install) | R$ 9,90 | Skin basica + 1.000 moedas + remocao de interstitials por 30 dias |

**Regra absoluta**: Nenhum IAP afeta poder de combate. Zero. Nunca.

### 8.4 Roadmap de Monetizacao

| Fase | Timeline | Novidades de Monetizacao |
|---|---|---|
| **MVP** | Set/2026 | Apenas rewarded ads + interstitials |
| **v1.0** | Nov/2026 | Battle Pass Temporada 1 + Loja de skins basica |
| **v1.1** | Jan/2027 | IAP diretos (pacotes de moedas) + remocao de interstitials |
| **v1.5** | Mar/2027 | Battle Pass Temporada 2 + emotes + skins lendarias |
| **v2.0** | Jun/2027 | Novo mapa (Congresso) + pacote de fundador + system de guild/amigos |

---

## 9. Features Priorizadas — MoSCoW

### MVP (lancamento setembro 2026)

#### MUST HAVE (sem isso, nao lanca)
- [ ] Core gameplay: movimento, ataque melee e ranged
- [ ] 1 mapa completo (Esplanada) com tileset e parallax
- [ ] 7 tipos de zumbi com comportamentos distintos
- [ ] 5 armas com feel distinto
- [ ] Sistema de waves com dificuldade crescente (minimo 15 waves)
- [ ] 4 power-ups funcionando
- [ ] HUD: vida, score, wave counter, combo
- [ ] Tutorial integrado (nao tela separada)
- [ ] Leaderboard global + semanal (Firebase)
- [ ] Rewarded ad (revive) integrado e funcionando
- [ ] Interstitial ad (entre partidas) integrado
- [ ] Save local de nivel e progresso
- [ ] Share de score (WhatsApp, Instagram, TikTok)
- [ ] Analytics (Firebase): sessao, morte, wave, ads
- [ ] Crash reporting (Firebase Crashlytics)
- [ ] 60fps em Samsung Galaxy A06
- [ ] APK < 40MB
- [ ] Funciona offline (apenas leaderboard requer net)
- [ ] Suporte a Android 8+ e iOS 14+

#### SHOULD HAVE (importante, mas workaround existe)
- [ ] 6 upgrades de nivel desbloqueaveis
- [ ] 5 conquistas locais
- [ ] Sistema de combo visual elaborado (numero flutuante, escala)
- [ ] Screen shake configuravel (acessibilidade)
- [ ] Boss wave especial a cada 5 waves
- [ ] Modo de qualidade grafica reduzida (para devices muito fracos)
- [ ] Feedback haptico nos hits
- [ ] Som de ambiente (Brasilia satirica: papagaios falando besteira, helicoptero rondando)
- [ ] Animacao de introducao curta (5s) do mapa antes da primeira partida

#### COULD HAVE (nice to have, entra se houver tempo)
- [ ] Segunda arma temporaria (drops de zumbis)
- [ ] Placar local (top 5 de sessoes do proprio device)
- [ ] Opcao de idioma (PT-BR e EN para futuras expansoes)
- [ ] Configuracoes de audio detalhadas (SFX, musica, separados)
- [ ] Daltonismo mode (paletas alternativas)
- [ ] 2 skins cosmeticas gratuitas (desbloqueadas por nivel 10 e 20)

#### WON'T HAVE no MVP (documentado para evitar scope creep)
- Battle pass ou IAP de qualquer tipo
- PvP ou co-op
- Segundo mapa
- Personagem alternativo jogavel
- Sistema de guild/amigos
- Daily missions
- Push notifications
- Sistema de clans ou social
- Procedural generation de mapas
- Narrativa elaborada ou cinemáticas longas
- Cloud save (save local e suficiente)
- Modo offline de leaderboard

---

### v1.0 (novembro 2026)

#### MUST HAVE para v1.0
- [ ] Battle Pass funcional com 30 niveis
- [ ] Loja de cosmeticos (pelo menos 3 skins de personagem, 3 skins de arma)
- [ ] Daily missions (3 por dia)
- [ ] Push notifications re-engagement
- [ ] Cloud save (progresso sincronizado)
- [ ] 20 conquistas (expansao das 5 do MVP)
- [ ] Segundo personagem jogavel (cosmetico com mecanica identica)
- [ ] Modo de dificuldade selecionavel (Normal / Brasilia Mode)

#### SHOULD HAVE para v1.0
- [ ] Evento de temporada (novembro: pos-eleicao tematico)
- [ ] Placar de amigos (Google Play Games)
- [ ] 2 novas armas (total 7)
- [ ] 2 novos tipos de zumbi (total 9)

---

## 10. User Stories

### As 20 User Stories Mais Importantes

**[US-001] — Primeiro Contato**
*Como jogador novo que baixou o app, quero comecar a jogar em menos de 30 segundos sem ler instrucoes para entender imediatamente o que fazer.*
- Criterio: Tempo do launch ate primeiro kill < 30 segundos
- Criterio: 90% dos playtesters entendem os controles sem explicacao verbal

**[US-002] — O Loop Viciante**
*Como jogador no intervalo do trabalho, quero que cada partida dure entre 3-15 minutos para caber em qualquer janela de tempo livre.*
- Criterio: Sessao media de 5-10 minutos nos primeiros 7 dias
- Criterio: Mais de 60% dos jogadores jogam mais de 1 partida por sessao

**[US-003] — Morte Justa**
*Como jogador que morreu, quero entender por que morri para querer tentar de novo sem frustração.*
- Criterio: Tela de game over mostra wave atingida, score, causa da morte
- Criterio: Botao de "jogar novamente" e a acao primaria, com toque de 1 dedo

**[US-004] — Revive com Ads**
*Como jogador que morreu em uma wave dificil, quero a opcao de continuar assistindo um video para nao perder meu progresso sem ser forcado a isso.*
- Criterio: Botao de revive aparece claramente mas sem pressao (botao "nao obrigado" igualmente visivel)
- Criterio: Ad toca imediatamente, sem loading prolongado
- Criterio: Vida restaurada instantaneamente apos ad

**[US-005] — Reconhecimento Cultural**
*Como brasileiro que acompanha politica, quero reconhecer referencias politicas nos zumbis para me sentir "parte da piada".*
- Criterio: Pelo menos 3 playtesters por zumbi identificam a referencia sem explicacao
- Criterio: Cada zumbi tem pelo menos 1 frase/animacao especifica que gera riso nos playtesters

**[US-006] — Progressao Sentida**
*Como jogador recorrente, quero sentir que meu personagem esta ficando mais forte para ter motivacao de voltar amanha.*
- Criterio: Level up visivel apos cada sessao de jogo moderada (20+ min)
- Criterio: Cada upgrade e imediatamente perceptivel no gameplay (nao so numerico)

**[US-007] — Compartilhamento Organico**
*Como jogador que acabou de bater meu recorde, quero compartilhar meu score de forma facil e visualmente atraente para mostrar pra galera.*
- Criterio: Botao de share na tela de game over, 1 toque
- Criterio: Screenshot gerado automaticamente com score, wave, e visual do jogo
- Criterio: Abre WhatsApp/Instagram/TikTok diretamente sem copiar e colar

**[US-008] — Competicao Saudavel**
*Como jogador competitivo, quero ver minha posicao no leaderboard global e semanal para ter um objetivo de curto prazo.*
- Criterio: Leaderboard visivel na tela inicial (top 10 + posicao do jogador)
- Criterio: Atualiza em < 5 segundos apos o fim da partida
- Criterio: Reset semanal com notificacao do resultado final

**[US-009] — Diversidade de Armas**
*Como jogador que ja dominou uma arma, quero experimentar estilos de jogo diferentes para que o jogo nao fique repetitivo.*
- Criterio: Cada arma tem curva de aprendizado diferente e valida
- Criterio: Melee e ranged sao equivalentes em poder (apenas estilos diferentes)

**[US-010] — Performance no Celular Basico**
*Como usuario de Samsung Galaxy A06, quero que o jogo rode sem travamento para nao ter experiencia degradada.*
- Criterio: 60fps estavel por 15+ minutos no Galaxy A06
- Criterio: Sem crashs durante gameplay nas primeiras 48h de uso

**[US-011] — Onboarding Sem Atrito**
*Como usuario que baixou o jogo sem criar conta, quero jogar imediatamente sem cadastro para nao desistir antes de comecar.*
- Criterio: Zero obrigatoriedade de login na primeira sessao
- Criterio: Firebase Anonymous Auth em background (invisivel para o usuario)
- Criterio: Upgrade opcional para Google Sign-In apenas ao acessar leaderboard

**[US-012] — Feedback de Combate Satisfatorio**
*Como jogador no meio de uma horde, quero sentir fisicamente cada hit que aplico para que o combate seja visceralmente satisfatorio.*
- Criterio: Feedback haptico em todos os hits (configuravel)
- Criterio: Hit stop de 2-3 frames visivel e sentido
- Criterio: SFX de hit distinto por tipo de arma (5 sons diferentes)

**[US-013] — Escalada de Dificuldade**
*Como jogador veterano, quero que o jogo fique progressivamente mais dificil para ser desafiado mesmo apos dias de jogo.*
- Criterio: Wave 10+ notoriamente mais dificil que wave 1 (stats comparaveis)
- Criterio: Wave 15+ requer conhecimento de todos os tipos de zumbi para sobreviver
- Criterio: Boss wave e claramente diferente visualmente e mecanicamente

**[US-014] — Ads Nao Intrusivos**
*Como jogador regular, quero que a publicidade nao interrompa meu fluxo de jogo para nao me frustrar e desinstalar o app.*
- Criterio: Zero ads durante gameplay ativo
- Criterio: Interstitial apenas entre partidas completas, nao entre waves
- Criterio: Rewarded ad e sempre opt-in com "nao obrigado" visivel

**[US-015] — Save Confiavel**
*Como jogador que jogou 1 hora, quero que meu progresso seja salvo automaticamente para nao perder conquistas se fechar o app.*
- Criterio: Save local apos cada partida completada
- Criterio: Nunca perder mais de 1 partida de progresso
- Criterio: Funciona offline completamente

**[US-016] — Humor Atualizado**
*Como jogador que acompanha noticias, quero que o humor do jogo reflita eventos recentes para que o conteudo fique relevante.*
- Criterio: Firebase Remote Config permite atualizar nomes/frases de zumbis sem update de app
- Criterio: Pelo menos 1 atualizacao de conteudo de humor por mes (via config)

**[US-017] — Acessibilidade Basica**
*Como jogador com dificuldade de visao, quero controles ajustaveis para poder jogar confortavelmente.*
- Criterio: Tamanho do joystick virtual ajustavel (P/M/G)
- Criterio: Screen shake pode ser desativado
- Criterio: Modo de contraste alto disponivel nas configuracoes

**[US-018] — Sessao Rapida Funciona**
*Como jogador com apenas 5 minutos disponíveis, quero conseguir ter uma sessao completa e satisfatoria mesmo em pouco tempo.*
- Criterio: Uma partida de wave 1-7 + death + game over cabe em 4 minutos
- Criterio: Nao ha loading prolongado entre telas (< 2s em device P0)

**[US-019] — Engajamento de Retorno**
*Como jogador que nao joga ha 3 dias, quero receber uma notificacao relevante e nao intrusiva para lembrar que o jogo existe.*
- Criterio: Push notification com mensagem humoristica (nao generica)
- Criterio: Maximo 1 notificacao por dia
- Criterio: Facil de desativar nas configuracoes

**[US-020] — Legibilidade em Tela Pequena**
*Como usuario com tela de 5 polegadas, quero ler todos os elementos de UI sem aproximar o olho da tela.*
- Criterio: Texto minimo de 14sp em todos os elementos de UI
- Criterio: Botoes de acao com area de toque minima de 48dp x 48dp
- Criterio: Score e combo legiveis durante gameplay intenso (contraste minimo de 4.5:1)

---

## 11. KPIs e Metricas

### Metricas de Validacao (Gate de Lancamento)

Estes sao os criterios que determinam se o produto esta pronto para escalar:

| KPI | Minimo para Continuar | Target | Kill Condition |
|---|---|---|---|
| **Retencao D1** | > 30% | > 40% | < 20% |
| **Retencao D7** | > 12% | > 18% | < 8% |
| **Retencao D30** | > 5% | > 8% | < 3% |
| **Sessao media** | > 4 min | > 7 min | < 2 min |
| **Sessoes por dia (DAU ativo)** | > 2 | > 3,5 | < 1,5 |
| **Crash rate** | < 2% | < 1% | > 5% |
| **FPS medio (Galaxy A06)** | > 55 fps | 60 fps | < 45 fps |
| **APK size** | < 50 MB | < 35 MB | > 80 MB |

### Metricas de Monetizacao (Ads — MVP)

| KPI | Target Soft Launch | Target Lancamento | Fonte de Benchmark |
|---|---|---|---|
| **Rewarded Ad Watch Rate** | > 25% das mortes | > 35% das mortes | Applovin 2025 |
| **Interstitial Fill Rate** | > 85% | > 92% | AdMob BR |
| **eCPM Rewarded** | > R$ 15 | > R$ 22 | AdMob BR media |
| **eCPM Interstitial** | > R$ 6 | > R$ 12 | AdMob BR media |
| **Ads por sessao** | > 1.0 | > 1.8 | Estimativa interna |
| **ARPDAU (ads)** | > R$ 0,04 | > R$ 0,07 | Calculado |
| **CPI (Android BR)** | < R$ 3,00 | < R$ 1,50 | UA benchmarks BR |

### Metricas de Produto (Gameplay)

| KPI | O que mede | Target |
|---|---|---|
| **Wave media atingida** | Dificuldade calibrada corretamente | Wave 7-10 na primeira semana |
| **% jogadores que chegam na wave 5** | Curva de dificuldade nao e cruel | > 40% |
| **% jogadores que usam rewarded** | Engajamento + valor percebido | > 30% |
| **% jogadores que compartilham score** | Viralizacao organica | > 10% |
| **Tutorial completion rate** | Onboarding funcional | > 75% |
| **Arma mais usada** | Balance entre armas | Nenhuma acima de 45% |
| **Tipo de zumbi que mais mata** | Balance de dificuldade | Distribuicao entre 3+ tipos |

### Metricas de Aquisicao (Go-to-Market)

| KPI | Target Soft Launch | Target Lancamento |
|---|---|---|
| **Downloads diarios** | 500-2.000/dia | 5.000-20.000/dia (semana do lancamento) |
| **Rating (App Store)** | > 4.0 | > 4.2 |
| **Numero de reviews** | > 50 | > 500 |
| **Organic vs Paid split** | 60% organic | 50% organic |

### Dashboard de Metricas Prioritarias (Daily Standup)

Os 5 numeros que o time olha todo dia:
1. **DAU** (usuarios ativos diarios)
2. **Retencao D1** (rolling 7 dias)
3. **ARPDAU** (receita por usuario ativo)
4. **Crash rate** (ultimas 24h)
5. **Sessao media** (ultimas 24h)

---

## 12. Roadmap

### Visao Geral

```
MAI 2026  ████ VALIDACAO TECNICA (2 semanas)
JUN 2026  ████████████ PROTOTIPO JOGAVEL (6 semanas)
JUL 2026  ████████ MVP POLISH (4 semanas)
AGO 2026  ████████ SOFT LAUNCH — Android BR (4 semanas)
SET 2026  ████ LANCAMENTO GLOBAL (Android + iOS)
OUT 2026  ████████ LIVE OPS — PICO ELEITORAL
NOV 2026  ████ ANALISE + DECISAO v1.0
DEZ 2026  ████████ DESENVOLVIMENTO v1.0
JAN 2027  ████ LANCAMENTO v1.0
MAR 2027  ████████ v1.5
JUN 2027  ████████████ v2.0
```

---

### FASE 0: Validacao Tecnica
**Maio 2026 — Semanas 1-2**

Objetivo: Provar que a stack tecnologica funciona ANTES de construir qualquer feature de produto.

| Entrega | Criterio de Sucesso |
|---|---|
| Build Godot rodando 200 sprites a 60fps no Galaxy A06 | FPS estavel, sem stuttering |
| AdMob integrado mostrando ad de teste | Request → Fill → Close funcionando |
| Firebase Auth + Firestore (write/read de score) | Latencia < 500ms |
| Prototipo de controle (joystick + botao de ataque) | 3 playtesters entendem sem instrucao |
| Primeiro sprite no estilo Andre Guedes animado | "Parece o estilo dele" — aprovado por Andre |

**GATE 0**: Se alguma dessas provas de conceito falhar, avaliar pivot para Unity antes de qualquer trabalho adicional.

---

### FASE 1: MVP — Prototipo Jogavel
**Maio-Julho 2026 — Semanas 3-12**

**Semanas 3-4**: Core gameplay (movimento, ataque, dano, morte)
**Semanas 5-6**: Wave system + 3 tipos de zumbi + HUD basico
**Semanas 7-8**: Mapa Esplanada (tileset + parallax) + Firebase leaderboard
**Semana 8**: PLAYTEST INTERNO — o jogo e divertido por 5 minutos?
**Semanas 9-10**: 7 tipos de zumbi completos + 5 armas com feel distinto
**Semanas 10-11**: Power-ups + screen shake + hit feel + combo system
**Semana 11**: Sound design (SFX combate + musica + ambience) + share
**Semana 12**: Performance pass + QA em 5 devices reais
**Semana 12**: PLAYTEST COM 20+ USUARIOS EXTERNOS — D1 retention > 30%?

**GATE 1**: D1 retention > 30% em playtest externo. Se nao, iteracao antes de soft launch.

---

### FASE 2: Soft Launch (Android Brasil)
**Agosto 2026 — Semanas 13-16**

Objetivo: Validar metricas em audiencia real antes do lancamento completo.

| Semana | Atividade |
|---|---|
| 13 | Upload Google Play (beta aberto, regiao BR) |
| 13-16 | Monitoramento diario de metricas: retencao, sessao, crashes, eCPM |
| 14-15 | Iteracao rapida baseada em dados (balance, bugs criticos, UX) |
| 14 | ASO: screenshots, descricao, keywords |
| 15-16 | Preparacao iOS (TestFlight) |
| 16 | **GATE 2**: CPI < R$ 3, D7 > 12%, crash rate < 2%? |

---

### FASE 3: Lancamento (Android + iOS)
**Setembro 2026 — Semanas 17-18**

| Atividade | Responsavel |
|---|---|
| Lancamento Android BR (Google Play publico) | Dev + Marketing |
| Lancamento iOS BR (App Store) | Dev |
| War room 24h por 48h pos-lancamento | Todo o time |
| Trailer com Andre Guedes publicado no canal dele (1.48M inscritos) | Marketing + Andre |
| Campanha de influencers gaming + humor | Marketing |
| PR para sites de games e politica | Marketing |

---

### FASE 4: Live Ops — Pico Eleitoral
**Outubro-Novembro 2026**

| Data | Evento |
|---|---|
| 1 outubro | Ativacao evento "Semana da Eleicao": mapa decorado, zumbis com acessorios eleitorais |
| 4 outubro (1o turno) | Evento especial "Dia da Eleicao": bonus de score 2x, novo boss temporario |
| 6-24 outubro | Conteudo entre turnos (se houver 2o turno): novos drops, piadas sobre resultados |
| 25 outubro (2o turno) | Repeticao do evento especial, versao "Segundo Turno" |
| Novembro | Temporada "Pos-Eleicao": analise de metricas, decisao de escalar para v1.0 |

Todos os conteudos de eventos sao entregues via Firebase Remote Config + asset bundles — sem update de app necessario.

**GATE 3**: Apos periodo eleitoral, avaliar: MAU > 50K por 4 semanas E D7 > 18%? Se sim, verde para v1.0 com IAP.

---

### v1.0 — Monetizacao e Profundidade
**Dezembro 2026 — Janeiro 2027**

**Features principais:**
- Battle Pass "Temporada 1: A Virada" (30 niveis, R$ 14,90)
- Loja de cosmeticos ("Cabide da Republica")
- Daily missions (3 por dia, recompensas de moedas)
- Cloud save
- Push notifications de re-engagement
- 2 novos tipos de zumbi
- 2 novas armas
- Modo de dificuldade "Brasilia Mode" (hardcore)
- Placar de amigos (Google Play Games)

**KPIs de sucesso para v1.0:**
- Taxa de conversao IAP > 3%
- ARPDAU total (ads + IAP) > R$ 0,15
- Battle Pass conversion > 5% dos DAU

---

### v1.5 — Novo Conteudo e Expansao
**Marco 2027**

- **Segundo mapa**: Congresso Nacional (interior, corredores, plenario)
- Battle Pass Temporada 2
- Sistema de achievements expandido
- Modo evento limitado mensal
- Personagem jogavel 2 (com mecanica ligeiramente diferente — ex: mais lento mas mais resistente)
- Integracao com TikTok (share direto de clips de gameplay)

---

### v2.0 — Multiplayer e Expansao de IP
**Junho 2027**

- **Co-op assimetrico**: 2 jogadores no mesmo mapa (online)
- Terceiro mapa: Palacio do Planalto
- Sistema de guilds ("Partidos" — ironia maxima)
- PvP indireto: desafios de score entre amigos
- Expansao internacional: Argentina (com contexto local adaptado)
- Versao PC/Mac via Steam (Godot exporta nativamente)

---

## 13. Riscos de Produto

### O que pode fazer este jogo nao ser divertido

Esta secao existe para ser consultada em cada decisao de design. Se algo no jogo viola esses riscos, e urgencia de produto — nao backlog.

---

**RISCO #1 — O humor envelhecer mais rapido que o jogo**
*Probabilidade: Alta | Impacto: Alto*

Piadas politicas tem validade. Um zumbi baseado em escandalo de 2018 e irrelevante em 2026. Se o humor for "fixo" demais, o jogo perde relevancia em semanas.

*Mitigacao*: Todo conteudo de humor (nomes de zumbis, frases, referencias) e parametrizado via Firebase Remote Config. Andre Guedes faz revisao semanal. Novo conteudo de humor e entregue via config sem update de app. O motor de humor e atualizado mesmo sem novas features.

---

**RISCO #2 — Controles frustrantes em celular**
*Probabilidade: Media | Impacto: Critico*

Se o jogador sentir que morreu porque o controle nao respondeu, ele desinstala. Nao e raiva do jogo — e raiva de si mesmo por ter baixado "aquela porcaria".

*Mitigacao*: Playtest de controles em semana 3, iteracao semanal. Auto-aim suave configuravel. Joystick "snaps" para onde o dedo toca (nao fixo). 5 playtesters externos devem jogar sem instrucao antes de qualquer outra feature entrar.

---

**RISCO #3 — Dificuldade mal calibrada**
*Probabilidade: Alta | Impacto: Alto*

Muito facil = entediante em 3 minutos. Muito dificil = frustrante em 30 segundos. A curva perfeita e impossivel de acertar no primeiro dia.

*Mitigacao*: Firebase Remote Config controla todos os parametros de dificuldade (velocidade de zumbi, vida, spawn rate). Nunca hardcodar valores de balance no jogo. Primeira semana de soft launch = iteracao diaria de balance baseada em wave media atingida e dropout rate por wave.

---

**RISCO #4 — Ads destruindo a experiencia**
*Probabilidade: Media | Impacto: Critico*

Um ad no momento errado pode transformar um jogador engajado em um review de 1 estrela. Nao e hiperbole — e o maior risco de monetizacao.

*Mitigacao*: Protocolo rigido: zero ads durante gameplay. Interstitial apenas entre partidas completas. Nunca dois interstitials seguidos. Rewarded e sempre opt-in. Monitoramento diario de taxa de abandono pos-ad.

---

**RISCO #5 — O jogo nao viralizar**
*Probabilidade: Media | Impacto: Alto*

O modelo de negocio depende de aquisicao organica via conteudo viral. Se o jogo for "bom mas nao compartilhavel", a matematica de CPI nao fecha.

*Mitigacao*: Projetar explicitamente "momentos de screenshot" — animacao de game over hilarante, tela de resultado com arte do Andre Guedes, frase unica de game over a cada morte. O share deve ser um botao imediatamente visivel e o conteudo gerado deve ser visualmente atraente mesmo sem contexto.

---

**RISCO #6 — Performance insatisfatoria nos devices-alvo**
*Probabilidade: Media | Impacto: Alto*

Se o jogo travar no Samsung Galaxy A06 — o device mais vendido no Brasil — 30% do publico-alvo tem experiencia ruim.

*Mitigacao*: Profiling semanal no Galaxy A06 e regra nao negociavel. Budget de performance e lei: <150 sprites, <30 draw calls, <300MB RAM. Dynamic quality system para reduzir automaticamente particulas em devices fracos.

---

**RISCO #7 — Processo juridico por satira politica**
*Probabilidade: Baixa | Impacto: Muito Alto*

Politicos brasileiros tem historico de usar o judiciario para suprimir satira. Um mandado de remocao durante o pico eleitoral e catastrofico.

*Mitigacao*: Consultor juridico contratado antes do lancamento (ver documento legal). Nenhum zumbi e *nominalmente identificavel* — sao arquétipos (Senador, Vereador, Lobista), nao pessoas reais. Frases e visuais passam por revisao juridica. Zumbis nao representam partido especifico. Humor e apartidario e satiriza todos os lados.

---

**RISCO #8 — Parceria com Andre Guedes nao se concretizar**
*Probabilidade: Media | Impacto: Alto*

Sem Andre, o jogo perde sua alma, seu canal de marketing inicial (1.48M inscritos) e sua autenticidade.

*Mitigacao*: Negociacao iniciada em maio 2026 como prioridade zero. Revenue share + fee de consultoria e modelo mais atrativo para criadores. Contrato claro sobre direitos de IP. Se negociacao falhar: avaliar criar IP original inspirada (nao derivada) do universo de Andre.

---

**RISCO #9 — Core loop nao sendo divertido o suficiente**
*Probabilidade: Baixa-Media | Impacto: Critico*

Se o loop fundamental (toque-mata-coleta) nao for satisfatorio, nenhuma outra feature salva o jogo. Isso e o risco mais importante.

*Mitigacao*: O hit feel e a primeira coisa a ser implementada, nao a ultima. Playtest de hit feel em semana 3 com questao direta: "Matar esse zumbi foi satisfatorio?" Se a resposta media for abaixo de 8/10, tudo para. Iteracao em screen shake, hit stop, SFX, e animacao de morte do zumbi ate chegar em 8+.

---

**RISCO #10 — Janela eleitoral fechar sem produto pronto**
*Probabilidade: Media | Impacto: Alto*

O timing com as eleicoes de outubro 2026 e o maior catalogo de viralidade. Se o lancamento atrasar para novembro, a janela fecha.

*Mitigacao*: Escopo do MVP e inegociavel — sem features nao-essenciais. Gate de soft launch em agosto e gate de lancamento em setembro devem ser respeitados. Se em julho o produto nao estiver em estado de soft launch, escopo e cortado, nao timeline. "Uma ideia atrasada e eventualmente boa. Uma ideia apressada e eternamente ruim." — mas desta vez, o timing e o produto. Corte features, nao qualidade de core.

---

## Apendice: Glossario de Design

| Termo | Definicao no Contexto do Jogo |
|---|---|
| **Hit feel** | Sensacao subjetiva de satisfacao ao acertar um inimigo. Composto de: hit stop, screen shake, SFX, animacao de dano. |
| **Hit stop** | Pausa de 2-3 frames em ambos personagem e inimigo no momento do impacto, criando sensacao de peso. |
| **Kiting** | Tecnica de movimento onde o jogador mantém distancia do inimigo enquanto ataca, evitando dano de melee. |
| **Chokepoint** | Area do mapa que afunila multiplos inimigos para um ponto, tornando AOE (area of effect) mais eficiente. |
| **Core loop** | O ciclo basico e repetitivo de gameplay. Aqui: mover → atacar → coletar. Tudo gira em torno disso. |
| **Wave** | Onda de inimigos. Cada wave tem composicao e dificuldade crescente. Boss waves ocorrem a cada 5 waves. |
| **ARPDAU** | Average Revenue Per Daily Active User. Receita media por usuario ativo diario. Metrica central de monetizacao. |
| **D1/D7/D30** | Retencao no dia 1, 7 e 30 apos instalacao. Metricas fundamentais de engajamento e produto-mercado fit. |
| **Rewarded Ad** | Publicidade que o usuario *escolhe* assistir em troca de beneficio in-game. Modelo mais aceito pelos jogadores. |
| **Remote Config** | Firebase Remote Config: sistema para atualizar parametros do jogo (dificuldade, humor, eventos) sem update de app. |
| **Object Pooling** | Tecnica de performance: reutilizar objetos ja criados (zumbis, projeteis) em vez de criar e destruir constantemente. |

---

*Documento escrito por Shigeru Miyamoto (simulado) | Abril 2026*
*Este PRD e um documento vivo. Qualquer feature que nao sobreviver ao teste "e isso divertido?" deve ser questionada, independente de quanto custou para especificar.*
