# ZUMBIS DE BRASILIA — PRD do MVP Web
### Product Requirements Document | Browser Game | 2 Semanas

**Documento de Produto | Abril 2026**
**Visao: Shigeru Miyamoto | PM & Game Design**

---

> *"Quando eu criei o Mario, eu nao queria que as pessoas lessem um manual. Eu queria que elas tocassem no controle e SORRISSEM. O browser game precisa do mesmo principio: clicou no link, esta jogando em 5 segundos, esta sorrindo em 10. Sem fricao, sem tutorial, sem explicacao. O jogo ensina jogando."*

---

## CONTEXTO DO PIVOT

O plano original era um jogo mobile F2P de R$ 2,5M e 6 meses de desenvolvimento. O Jason Schreier analisou e tinha razao em dar 5.5/10 — o timeline era fantasia e o risco era catastrofico. O Andre Guedes, nosso diretor criativo, veio com a decisao certa: fazer um browser game em 2 semanas, sem download, jogavel em 3 minutos, altamente compartilhavel.

Este PRD define exatamente o que este browser game e — e o que ele NAO e.

**Regra de ouro: 14 itens de funcionalidade. Nada mais. Se uma feature nao esta nesta lista, ela nao existe para este MVP.**

---

## 1. OS 14 ITENS DO MVP

Lista fechada. Imutavel. Se alguem propuser o item 15, a resposta e nao.

| # | Funcionalidade | Descricao Resumida |
|---|---|---|
| 1 | **Motor de movimento** | WASD/setas no desktop, joystick virtual no mobile. 8 direcoes, velocidade constante. |
| 2 | **Auto-attack** | O cidadao ataca automaticamente o inimigo mais proximo dentro do raio de alcance. Zero botao de ataque. |
| 3 | **Sistema de waves (6 ondas em 3 minutos)** | Estrutura fixa de dificuldade crescente, cronometro visivel na tela. |
| 4 | **4 tipos de zumbi** | Vereador (basico), Assessor de Fake News (atirador), Senador Blindado (tanque), Banqueiro-Zumbi (multiplicador). |
| 5 | **Boss: O Candidato Eterno** | Aparece na wave 5. Tem "segundo turno" — levanta com 25% de HP ao ser derrotado pela primeira vez. |
| 6 | **5 power-ups como drops** | Chinelo Voador, Urna Eletronica, Cafe da Esplanada, Carimbo do INSS, Delacao Premiada. Coletaveis no chao. |
| 7 | **Sistema de score com combo** | Multiplicador x2/x3/x5/x10. Texto "APROVADO!" na tela ao atingir x5. |
| 8 | **Tela de Game Over compartilhavel** | Frase acida + titulo satirico baseado no score + botao de compartilhamento (link + screenshot). |
| 9 | **Cenario unico: A Esplanada** | Arena retangular. Congresso ao fundo pulsando verde. Ministerios como obstaculos. Espelho d'agua como zona de perigo. |
| 10 | **Protagonista com 3 variantes de tom de pele** | Selecao em 1 toque antes de comecar. Polo azul desbotada, bermuda jeans, chinelo. |
| 11 | **Audio basico (4 loops + SFX essenciais)** | Loop de gameplay, loop de wave alta, game over, mais SFX de kill, dano e power-up. |
| 12 | **Tela inicial (5 segundos)** | Texto da "Emenda 666" + botao gigante "JOGAR". Nenhuma outra opcao. |
| 13 | **Leaderboard local (sessao)** | Score salvo no browser (localStorage). Sem servidor, sem login, sem cadastro. |
| 14 | **URL compartilhavel + figurinhas de WhatsApp** | congressodosmortos.com.br. Pack de 6 figurinhas dos zumbis para WhatsApp, disponivel desde o dia 1. |

**O que NAO e um item:** tutorial separado, login, sistema de progresso entre sessoes, upgrades permanentes, sistema de moedas, leaderboard global, monetizacao (vem na semana 2, pos-validacao), multiplos mapas, multiplayer, ranking semanal, missoes diarias.

---

## 2. CORE LOOP REVISADO

### O Loop de 30 Segundos para Browser (mais simples que o mobile)

O loop mobile original tinha 3 niveis (micro, medio, macro) e incluia progressao de personagem, upgrades entre sessoes, leaderboard e rewarded ads. Para o browser, cortamos tudo isso. O loop tem apenas dois niveis:

**Loop Micro (3-5 segundos):**
```
Zumbi aparece → cidadao ataca automatico → zumbi morre → drop cai no chao
→ jogador move para coletar drop (ou nao) → proximo zumbi
```

A decisao do jogador nao e "quando atacar" — e "para onde se mover". Isso e o coracao do Vampire Survivors. Posicionamento, nao reflexo.

**Loop de Sessao (3 minutos exatos):**
```
Clicou no link → tela inicial (5s) → escolhe tom de pele (5s)
→ JOGA 3 minutos (6 waves) → Game Over ou sobreviveu
→ ve titulo satirico + score → compartilha → clica "jogar de novo"
```

### Por que 3 minutos FIXOS e nao "ate morrer"

Esta e a decisao de design mais importante do MVP. O timer fixo:

1. **Facilita comparacao de scores** — todo mundo jogou pelo mesmo tempo, logo o score e comparavel. Isso cria competitividade viral.
2. **Elimina sessoes infinitas que frustram** — o jogador sabe que "faltam 47 segundos". Isso cria tensao gerenciada.
3. **Encaixa no horario do almoco** — 3 minutos e o tempo de espera de um elevador, de uma fila de cafe, do intervalo de uma reuniao.
4. **Simplifica o desenvolvimento** — sem sistema de "continuar", sem calcular dificuldade para sessoes longas, sem balance de economia de moedas.

Se o jogador morre antes dos 3 minutos, o timer para e mostra o score parcial. Se sobrevive aos 3 minutos inteiros, ganha bonus de score e o titulo "Cidadao Sobrevivente".

---

## 3. MECANICAS

### Controles

**Desktop (teclado):**
- WASD ou setas direcionais: movimento
- Sem botao de ataque (auto-attack)
- Tecla E ou barra de espaco: ativa power-up coletado mais recente
- Nenhuma outra tecla necessaria

**Mobile (touch):**
- Joystick virtual no canto inferior esquerdo, raio de 60dp
- Joystick nao e fixo — aparece onde o polegar toca na metade esquerda da tela
- Botao de power-up no canto inferior direito
- Sem botao de ataque (auto-attack)
- Funciona com polegar unico — o outro polegar segura o telefone

**Por que auto-attack e a escolha certa para o browser:**
O jogo e sobre esquivar de hordas e decidir qual zumbi priorizar pelo posicionamento, nao sobre apertar botoes no momento certo. Auto-attack reduz carga cognitiva, elimina frustracao de "errei o clique", e permite que o jogador foque no movimento — que e onde esta a tensao real. Alem disso, reduz o escopo de desenvolvimento de controles pela metade.

### Auto-attack: Logica

- O cidadao ataca o inimigo mais proximo dentro de um raio de alcance fixo (proporcional a arma)
- Cadencia de ataque fixa por tipo de arma (nao ha cooldown manual)
- Se nenhum inimigo esta no raio: animacao de idle
- Auto-aim suave: o sprite do cidadao vira na direcao do alvo

### Hit Feel (inegociavel)

O combate so e satisfatorio se o *hit feel* for correto. Isso nao e subjetivo:

- **Hit stop**: 2 frames de congelamento no impacto (sensacao de peso)
- **Hit flash**: sprite do inimigo pisca branco por 1 frame
- **Pop de score**: numero flutuante colorido sobe da cabeca do inimigo morto
- **Screen shake leve** em kills; **shake forte** ao matar boss
- **SFX distinto por arma**: vassoura = "THWACK" grosso; chinelo (power-up) = "FLAP-BAM" agudo; urna (power-up) = som de apuracao + confetes

### Power-ups: Comportamento

Power-ups dropam do chao ao matar zumbis (chance aleatoria, ponderada por tipo). O jogador precisa ANDAR ATE ELE para coletar — a coleta nunca e automatica. Isso cria decisao: vale o risco de se expor para pegar o drop?

Apenas 1 power-up ativo por vez. Coletar um novo substitui o anterior (se nao usou ainda, perdeu).

| Power-up | Efeito | Duracao | Como Dropar |
|---|---|---|---|
| **Chinelo Voador** | Chinelos giram ao redor do cidadao causando dano em area | 8 segundos | Qualquer zumbi (10% chance) |
| **Urna Eletronica** | Dispara numeros em todas as direcoes como projeteis | 5 segundos | Senador Blindado (garantido) |
| **Cafe da Esplanada** | Velocidade de movimento x2 | 10 segundos | Assessor de Fake News (25% chance) |
| **Carimbo do INSS** | Proximo ataque = 3x dano + texto "INDEFERIDO" aparece no zumbi | 1 uso | Banqueiro-Zumbi (garantido) |
| **Delacao Premiada** | Todos os zumbis na tela ficam atordoados por 3 segundos (apontam uns pros outros) | Efeito instantaneo | Boss Candidato Eterno (garantido na primeira morte do boss) |

### Waves: Estrutura dos 3 Minutos

```
00:00-00:30  WAVE 1 — "Sessao Ordinaria"
             Apenas Vereadores. 5-8 unidades. Lento. Jogador aprende movendo.

00:30-01:00  WAVE 2 — "Requerimento de Urgencia"
             Vereadores + Assessores de Fake News. Projeteis entram no jogo.
             Tensao sobe. Jogador aprende a nao ficar parado.

01:00-01:30  WAVE 3 — "Sessao Extraordinaria"
             Mix + primeiro Senador Blindado. Jogador descobre que ele e diferente.
             Escudo de "Imunidade Parlamentar" confunde a primeira vez.

01:30-02:00  WAVE 4 — "Sessao Secreta"
             Horda densa + Banqueiro-Zumbi aparece. Banqueiro corrompe zumbis ao redor,
             deixando-os 2x mais rapidos. Caos instalado. Primeiras mortes aqui.

02:00-02:30  WAVE 5 — "Plenario dos Mortos"
             Tudo junto + Boss Candidato Eterno. Musica muda.
             Boss discursa (onda sonica empurra jogador). Ao morrer: "VOLTO EM 4 ANOS!"
             Levanta com 25% de HP. Mate de novo para derrotar.

02:30-03:00  WAVE 6 — "Mandato Eterno"
             Sobrevivencia pura. Todos os tipos juntos. Cronometro visivel e vermelho.
             Score multiplicado por 1.5x nesta wave.

03:00        FIM. Tela de resultado.
```

---

## 4. OS 4+1 ZUMBIS

### Filosofia de Design dos Zumbis para Web

Cada zumbi tem tres camadas: **mecanica clara** (o jogador entende o que fazer), **piada politica integrada** (o humor explica a mecanica, nao decora ela) e **visual instantaneamente legivel** (em menos de 1 segundo o jogador sabe o que esta enfrentando).

Para web, priorizamos legibilidade na tela pequena e comportamentos simples de entender mas que criam emergencia quando combinados.

---

### Zumbi #1 — O Vereador (Horda Basica)

**Funcao mecanica:** Ensinar os controles. Criar pressao de numeros.

**Visual:** Terno barato azul marinho. Cracha de vereador pendurado torto. Sorriso congelado de santinho. Celular na mao mostrando a trend "Sera?" (referencia a Zema e Flavio, trend do TikTok de 2026). Pele acinzentada-esverdeada. Tamanho: 100% da escala base.

**Comportamento:** Anda em linha reta em direcao ao jogador. Velocidade: lenta. Vida: baixa. Sem habilidade especial. Spawn em grupos de 3 a 8.

**Piada mecanica:** Ao morrer, grita "Fui eleito democraticameeente!" e cai de brucos. Ao acertar o jogador: "Tenho imunidade parlamentar!" A ameaca nao vem da forca individual — vem do numero. Exatamente como funciona o Congresso.

**Score ao matar:** 10 pontos.

---

### Zumbi #2 — O Assessor de Fake News (Atirador)

**Funcao mecanica:** Introduzir projeteis. Forcar o jogador a se mover constantemente.

**Visual:** Camisa social branca manchada de tinta. Cabelo de apresentador de TV. Celular grudado na mao. Microfone de lapela. Tamanho: 90% da escala base (mais agil, parece menor).

**Comportamento:** Fica a distancia (raio de seguranca). Arremessa MANCHETES como projeteis a cada 2 segundos. Ao ser atingido, recua. Ao acertar o jogador, uma manchete satirica aparece na tela por 2 segundos:
- "CIDADAO SUSPEITO DE TER OPINIAO"
- "DATAFOLHA MOSTRA QUE NINGUEM SABE DE NADA"
- "IA GERA IMAGEM DE POLITICO HONESTO — SISTEMA TRAVA"
- "FONTE ANONIMA CONFIRMA QUE FONTES ANONIMAS MENTEM"

**Drop garantido:** Cafe da Esplanada (25% de chance).

**Piada mecanica:** Ele nunca chega perto. Ataca de longe. Exatamente como assessoria de comunicacao.

**Score ao matar:** 25 pontos.

---

### Zumbi #3 — O Senador Blindado (Tanque)

**Funcao mecanica:** Ensinar a priorizar targets. Introduzir a ideia de "escudo que cai".

**Visual:** Terno de 3 pecas impecavel. Cabelo grisalho com brilhantina. Papada quadrupla. Anel de ouro. Bengala de marfim (falso). Escudo translucido dourado em forma de balsa presidencial sobre o corpo inteiro. Tamanho: 130% da escala base.

**Comportamento:** Extremamente lento. Vida: alta (4x o Vereador). O escudo bloqueia os 3 primeiros ataques com texto flutuante: "IMUNIDADE!" / "FORO PRIVILEGIADO!" / "RECURSO EM ANDAMENTO!". Apos o 3o ataque bloqueado, o escudo quebra com som de caixa registradora e moedas caindo. Agora pode ser danificado normalmente.

**Ao ser derrotado:** Moedas caem do corpo (referencia aos R$ 61 bilhoes em emendas). Grita "Tenho foro privilegiado mesmo depois de morto!"

**Drop garantido:** Urna Eletronica.

**Piada mecanica:** Nao e que ele e mais forte. E que as leis nao se aplicam a ele — ate que se aplicam. A espera faz parte da piada.

**Score ao matar:** 50 pontos.

---

### Zumbi #4 — O Banqueiro-Zumbi (Multiplicador)

**Funcao mecanica:** Forcas o jogador a mudar de prioridade. Criar senso de urgencia mesmo quando longe.

**Visual:** Terno italiano cinza antracite. Oculos escuros. Sorriso de vendedor. Maleta dourada transbordando de dinheiro verde (notas voam ao redor dele). Celular na outra mao com tela brilhando (lista de contatos). Diferente dos outros — parece quase normal. Quase humano. Esse e o horror. Tamanho: 110% da escala base.

**Inspiracao:** Daniel Vorcaro. Banco Master. R$ 22 bilhoes. O celular com contato de todo mundo.

**Comportamento:** Nao ataca o jogador diretamente. Circula o mapa. Quando fica a 3 tiles de qualquer outro zumbi, CORROMPE os proximos: joga dinheiro neles, que ficam com aura dourada e ficam 2x mais rapidos e resistentes por 5 segundos. Se o jogador nao o mata rapidamente, a horda inteira vira uma maquina de destruicao.

**Drop garantido ao morrer:** Carimbo do INSS. Ao cair, o celular explode no chao mostrando lista de contatos: "Pres. da Camara", "Senador X", "Min. Y" — todos com emojis de coracao.

**Frase ao morrer:** "Fui mal assessorado!" / "Tem que ver com meu advogado!" / "Era tudo declarado!"

**Piada mecanica:** Ele nao e o mais forte. Ele torna os outros mais fortes. Exatamente como funciona a corrupcao sistemica.

**Score ao matar:** 75 pontos.

---

### Boss — O Candidato Eterno

**Aparece:** Wave 5 (aos 2:00 do cronometro).

**Visual:** 3x o tamanho de um Vereador. Sorriso de orelha a orelha impossivel. Cabelo pompadour. Faixa presidencial de "CANDIDATO". Botoes de campanha de todas as cores colados no terno. Palmas abertas em posicao de discurso eterno.

**Comportamento:**
- Fase 1: Anda em direcao ao jogador. A cada 8 segundos, para e DISCURSA — onda sonica que empurra o jogador para tras (nao causa dano, mas derruba o posicionamento).
- Ao chegar a 0 HP: cai, jingle distorcido toca, texto na tela: "SEGUNDO TURNO!" — levanta com 25% de HP e velocidade aumentada em 50%.
- Fase 2: Mais rapido, sem pausa para discursar. Vem direto.
- Morte definitiva: "Candidato Eterno — 0 votos". Chuva de santinhos. Drop garantido: Delacao Premiada.

**Frase caracteristica:** "VOLTO EM 4 ANOS!" (ao ressuscitar na Fase 2).

**Score ao matar:** 200 pontos (fase 1) + 200 pontos (fase 2) = 400 pontos totais.

---

## 5. SISTEMA DE SCORE E COMPARTILHAMENTO

### Sistema de Combo

- Cada kill em sequencia rapida (menos de 2 segundos entre kills) incrementa o multiplicador
- x1 (0-4 kills) → x2 (5-9) → x3 (10-19) → x5 (20-29) → x10 (30+)
- Ao atingir x5: texto "APROVADO!" aparece em vermelho no centro da tela por 1.5 segundos
- Levar dano nao quebra o combo — apenas ficar 2 segundos sem kill

### Calculos de Score

```
Score por kill = Pontos Base do Zumbi × Multiplicador de Combo × Bonus de Wave (wave 6 = 1.5x)
Score final = Soma de todos os kills + Bonus de sobrevivencia (se chegou ao 3:00) de 500 pontos
```

### Titulos Satiricos (base no Score Final)

| Faixa de Score | Titulo | Texto Compartilhavel |
|---|---|---|
| 0 — 500 | **"Estagiario da Esplanada"** | "Nao aguentei nem uma reuniao. Mas pelo menos tentei." |
| 501 — 1.500 | **"Vereador Suplente dos Mortos"** | "Eleito por acidente. Durei mais do que a maioria." |
| 1.501 — 3.000 | **"Deputado Federal Sobrevivente"** | "Apresentei projeto de lei: SOBREVIVER. Foi aprovado." |
| 3.001 — 5.000 | **"Senador da Resistencia"** | "Imunidade parlamentar: duracao de 3 minutos." |
| 5.001 — 8.000 | **"Ministro da Defesa Zumbi"** | "O Planalto ta seguro. Por enquanto." |
| 8.001 — 12.000 | **"Presidente dos Vivos"** | "Primeiro mandato: sobrevivencia. Segundo: impossivel." |
| 12.001+ | **"Lenda da Esplanada"** | "Sobreviveu ao que nenhum brasileiro conseguiu: o sistema inteiro." |

### Tela de Game Over — O Produto Viral

A tela de Game Over E o produto de marketing. Ela precisa ser screenshot-perfeita:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   [Arte do zumbi que matou o jogador, caricaturada] │
│                                                     │
│         MANDATO ENCERRADO                           │
│                                                     │
│    [TITULO SATIRICO EM FONTE GRANDE]                │
│                                                     │
│    Score: 3.847 pontos                              │
│    Sobreviveu: 1:43 de 3:00                         │
│    Zumbis eliminados: 89                            │
│    Maior combo: x5                                  │
│                                                     │
│    "Apresentei projeto de lei: SOBREVIVER.          │
│     Foi aprovado."                                  │
│                                                     │
│  [ COMPARTILHAR ]     [ JOGAR DE NOVO ]             │
│                                                     │
│  congressodosmortos.com.br                         │
└─────────────────────────────────────────────────────┘
```

**Botao COMPARTILHAR faz:**
1. Gera um screenshot da tela de Game Over (via Canvas API ou html2canvas)
2. Abre share sheet nativo do mobile (Web Share API) com: imagem + texto + link
3. Texto padrao: "Fui [TITULO] no Congresso dos Mortos! Meu score: [X] pontos. Voce consegue mais? congressodosmortos.com.br"
4. No desktop: copia link para clipboard + botoes diretos de Twitter/X e WhatsApp

**Frases acidas de Game Over (rotacionam aleatoriamente):**
- "Seu mandato acabou."
- "O sistema venceu. Dessa vez."
- "Ate proximo pleito."
- "A sessao esta encerrada."
- "Votacao: 1 x 254."
- "Recurso indeferido."
- "O Banqueiro agradece sua contribuicao."
- "A CPMI investigara o ocorrido. Sem prazo."

---

## 6. SESSAO DE JOGO — FLUXO COMPLETO

### Do link ao compartilhamento: o funil inteiro em 4 minutos

```
ETAPA 1 — CHEGADA (0-15 segundos)
Jogador recebe link no WhatsApp / vê no Twitter
→ Clica no link
→ Abre no browser do celular (sem instalacao, sem login, sem permissao)
→ Tela preta. Texto datilografado (5 segundos):
   "Brasilia, abril de 2026.
    O Congresso aprovou a Emenda 666 — nenhum parlamentar perde o cargo.
    Nunca. Nem com a morte.
    Ninguem leu o texto. Ninguem nunca le."
→ Botao gigante: [JOGAR AGORA]

ETAPA 2 — CUSTOMIZACAO (5 segundos)
3 circulos: tom de pele claro / medio / escuro
Toca em um. Jogo comeca imediatamente.
(Sem nome, sem cadastro, sem mais opcoes)

ETAPA 3 — TUTORIAL ZERO (primeiros 30 segundos = Wave 1)
3 Vereadores lentos aparecem na tela.
O cidadao ataca automaticamente o mais proximo.
O jogador percebe: "preciso me mover para sobreviver."
Nenhuma instrucao explicita. A mecanica ensina a si mesma.

ETAPA 4 — ESCALADA (00:30 a 02:00)
Waves 2, 3 e 4. Tensao cresce. Primeiras mortes.
Assessor atira manchetes. Senador tem escudo. Banqueiro corrompe.
Jogador aprende a priorizar, a se mover em circulo, a pegar drops.

ETAPA 5 — CLIMAX (02:00 a 03:00)
Candidato Eterno aparece na wave 5. Musica muda.
Caos total na wave 6. Cronometro vermelho.

ETAPA 6 — FIM (03:00 ou morte antes)
Tela de Game Over: titulo satirico + score + arte do ultimo zumbi que matou.
Dois botoes: [COMPARTILHAR] e [JOGAR DE NOVO].

ETAPA 7 — COMPARTILHAMENTO (15-30 segundos)
Jogador clica COMPARTILHAR.
Screenshot gerado automaticamente.
Share sheet do celular abre.
Jogador manda no grupo da familia, no Twitter, para o amigo rival.
Texto: "Fui [TITULO]. Voce consegue mais? congressodosmortos.com.br"

ETAPA 8 — REJEITO (imediato apos compartilhar)
Botao [JOGAR DE NOVO] esta sempre visivel.
Jogador quer melhorar o score.
Loop recomeca na ETAPA 2.
```

### O Gancho do "Mais Uma"

O jogador morre e sabe exatamente o que fez de errado. "Se eu tivesse pegado a Delacao Premiada antes do Boss, teria sobrevivido." Essa clareza e o gancho. O jogo e justo o suficiente para que o jogador acredite que pode fazer melhor. Porque pode.

---

## 7. KPIS DO MVP — CRITERIOS GO/NO-GO

### Metricas de Validacao (medidas em 2-4 semanas pos-lancamento)

| Metrica | NO-GO | Minimo para GO | Excelente |
|---|---|---|---|
| **Usuarios unicos (semana 1)** | < 50K | > 200K | > 1M |
| **Taxa de compartilhamento** | < 2% dos jogadores | > 5% | > 15% |
| **Retencao D1** | < 15% | > 25% | > 40% |
| **Retencao D7** | < 5% | > 10% | > 20% |
| **Sessoes por usuario na semana** | < 2 | > 4 | > 8 |
| **Mencoes em midia (veiculos)** | 0 | > 5 | > 20 |
| **Trending redes sociais** | Nao aparece | Regional | Nacional |
| **Sentimento do feedback** | < 40% positivo | > 70% positivo | > 85% positivo |

### Interpretacao dos Cenarios

**Cenario A — NO-GO:**
A tese nao funciona. O publico de memes politicos nao converte em jogadores. Prejuizo: R$ 30-50K. Aprendizado: economizamos R$ 2,45M. Seguimos em frente.

**Cenario B — GO CONDICIONAL:**
Ha interesse mas nao e fenomeno viral. Opcoes: iterar o browser game com novos zumbis baseados em eventos politicos recentes, ou lancar crowdfunding modesto (R$ 100-200K) para versao mobile simplificada.

**Cenario C — GO PLENO:**
Jogo virou fenomeno. Acionar crowdfunding agressivo (meta R$ 300K+), abordar investidores com dados reais, e iniciar desenvolvimento mobile em paralelo com updates do browser game.

### Kill Conditions (quando parar tudo)

| Condicao | Quando | Acao |
|---|---|---|
| Menos de 50K usuarios na semana 1 | Semana 1 | PAUSA — analisar se e distribuicao ou produto |
| Retencao D7 < 3% | Semana 2 | NO-GO para mobile |
| Zero mencoes em midia | Semana 2 | Reavaliar estrategia de distribuicao |
| Feedback majoritariamente negativo | Semana 1 | PAUSA — analisar e iterar |
| Andre Guedes se distancia do projeto | Qualquer momento | NO-GO — sem Andre, sem alma |

---

## 8. O QUE FOI CORTADO DO PRD ORIGINAL

Esta lista e explicita e intencional. Cada item foi cortado por uma razao especifica. Eles nao foram "adiados" — foram removidos do MVP. Podem ou nao entrar numa versao futura.

| Feature Cortada | Por Que Saiu |
|---|---|
| **Joystick virtual + botao de ataque manual** | Auto-attack e mais simples, mais rapido de desenvolver, e mais adequado para browser. Posicionamento e mais interessante que timing de ataque. |
| **Arsenal de 5 armas selecionaveis** | Escolha de arma inicial cria complexidade de onboarding desnecessaria. No browser, o jogador quer jogar em 5 segundos, nao escolher build. |
| **Sistema de upgrades permanentes (nivel 1-20)** | Progressao entre sessoes requer backend, aumenta escopo de desenvolvimento em 40%. Para um MVP de 2 semanas, e impossivel. |
| **Leaderboard global (Firebase)** | Requer backend, autenticacao, moderacao anti-cheat. Leaderboard local (localStorage) valida o conceito com zero infraestrutura. |
| **Sistema de moedas cosmeticas** | Sem progressao entre sessoes, moedas nao tem propósito. |
| **Skins e cosmeticos desbloqueaveis** | Sem sistema de progressao, sem proposito. 3 tons de pele de selecao direta e suficiente. |
| **Rewarded Ads para continuar** | Ads sao semana 2, pos-validacao. Nao entram no MVP de funcionalidades. |
| **Missoes diarias** | Requer backend e sessoes recorrentes trackadas. Fora do escopo. |
| **Campanha de missoes diarias** | Mesma razao. |
| **3 atos narrativos e 5 regioes** | O PRD original tinha ambicao narrativa de jogo completo. Para browser de 3 minutos, a narrativa e o texto da Emenda 666 (5 segundos) e as piadas integradas aos zumbis. Nada mais. |
| **Zumbis #5 a #7 do PRD original** (Ministra da Economia, outros tipos) | 4 tipos + 1 boss e o limite para o artista executar em 2 semanas com qualidade. Cada tipo a mais dilui o tempo de polish dos que ficaram. |
| **Sistema de combo com reset por dano** | Simplificado: combo reseta apenas por falta de kill, nao por levar dano. Menos frustrante, mais facil de entender. |
| **Hit stop de 2-3 frames com haptico** | Hit flash + pop de score resolvem o hit feel para browser. Haptico nao e controlavel em browser de forma confiavel. |
| **Multiplayer** | Nao estava no PRD original. Nunca entrou em consideracao para o MVP. |
| **Sistema de headshot** | Requer mira manual. Auto-attack elimina a necessidade. |
| **Chokepoints e verticalizacao do mapa** | Arena flat simplifica o desenvolvimento sem perder a mecanica de posicionamento, que e o coracao do jogo. |

### A Logica dos Cortes em Uma Frase

Qualquer feature que requeira backend, progressao entre sessoes, mira manual, ou mais de 2 semanas para polir corretamente foi cortada. O MVP e um loop perfeito, nao um jogo incompleto.

---

## NOTAS FINAIS DO PM

Este PRD foi escrito com uma perspectiva simples: **o primeiro jogador que abrir o link nunca ouviu falar deste jogo**. Ele esta no WhatsApp, um amigo mandou o link, ele tem 3 minutos antes da reuniao comecar. Se em 5 segundos ele nao entendeu o que fazer, e em 10 segundos ele nao sorriu, o jogo falhou.

Tudo neste documento serve a esse momento. Os 14 itens servem a esse momento. Os 4 zumbis servem a esse momento. O auto-attack serve a esse momento. A tela de Game Over compartilhavel serve a esse momento.

Esse e o produto. Tudo mais e futuro, se os KPIs mandarem.

---

*"Um bom jogo ensina suas regras nos primeiros 30 segundos de gameplay — sem nenhuma palavra escrita."*
*— Shigeru Miyamoto*

---

**congressodosmortos.com.br**
**Lancamento: Semana da gamescom latam — 30 abril a 3 de maio de 2026**
