# Q1-01 — HORA EXTRA NO APOCALIPSE
### Quest Design Document | Capitulo 1 | Modo Cidadao

---

## IDENTIDADE

| Campo | Valor |
|---|---|
| **ID** | Q1-01 |
| **Titulo** | Hora Extra no Apocalipse |
| **Modo** | Cidadao (Ze) |
| **Duracao estimada** | 5-7 minutos |
| **Dificuldade** | 1/5 — Tutorial ativo, morrer aqui e quase impossivel |
| **Posicao no cap** | Primeira quest. Nenhum conhecimento previo assumido. |

---

## PRE-REQUISITOS

Nenhum. Esta e a quest de abertura do Modo Cidadao. O jogador acabou de assistir a cutscene do Prologo e selecionou "Modo Cidadao".

---

## SETUP NARRATIVO DE ABERTURA

*Tela preta. Texto em fade-in:*

> **8 de janeiro de 2023. 14h47.**

*Ze aparece sentado na cadeira de escritorio, ventilador ligado, olhando pela janela do 3o andar do Ministerio do Planejamento. A Esplanada esta cheia de gente, bandeiras, fumaça.*

> **ZE (narração interna, caixa de texto no canto inferior):** "Hora extra voluntaria. Voluntaria entre aspas — o Carlao me disse que quem ficasse ate as 18h levava o dia como produtividade dobrada no relatorio. Eu nem sei o que isso significa, mas pareceu bem."

*Som de vidro quebrando. Ze levanta. A janela do fundo do escritorio racha. Uma onda de barulho entra — gritos, bombas de efeito moral, helicoptero passando baixo.*

> **ZE:** "Isso... nao e manifestacao normal."

*O Carlao do cubiculo B7 levanta vagarosamente. Olhos verdes. Caminha em direcao a Ze gemendo: "...inter... ven... cao... mi... li... tar..."*

*Texto aparece no centro da tela, fonte grande, tom de jornal satirico:*

**"WAVE 1: HORA EXTRA INVOLUNTARIA"**

*Controles liberados. Quest iniciada.*

---

## OBJETIVO DO JOGADOR

Sair do terceiro andar do Ministerio do Planejamento e chegar a saida do edificio (telheiro de vidro, portao de segurança) antes que a onda de Burocratas-Zumbi bloqueia todos os corredores.

---

## LOCALIZACAO

**Ministerio do Planejamento, Orcamento e Gestao**
Esplanada dos Ministerios, Bloco K — Brasilia, DF

**Estrutura do nivel (side-scroller, esquerda para direita):**

```
[INICIO]                                               [SAIDA]
  Ze na       Corredor     Sala de    Escada         Telheiro
cadeira   ->  do andar  -> Reunioes -> rolante  ->   de vidro
             (tutorial     (stealth   (horda       (boss area
              movimento)   opcional)   pequena)      preparatoria)
```

**Comprimento total do nivel:** 5 telas de largura (scroll horizontal continuo)
**Plataformas:** Mesas de escritorio (pulo simples), arquivos empilhados (pulo duplo), corrimao da escada rolante

**Background:** Janelas do lado esquerdo mostram a Esplanada em caos. Fumaça verde comecando a aparecer nas bordas das janelas. Santinhos de campanha e documentos oficiais voando do lado de fora. O Congresso visivel ao fundo, minusculo, la no horizonte.

---

## INIMIGOS PRESENTES

### Wave 1 — Corredor do Andar (tutorial de movimento)

**Burocrata-Zumbi x2**
- Visual: Terno cinza amassado, cracha no pescoco (nome ilegivel), pasta de plastico na mao, olhos verdes
- HP: 3 hits
- Comportamento: Andam em fila indiana, muito lentos (velocidade 40px/s). Gemem "protocolo... carimba aqui... assina em tres vias..." em loop
- Spawn: Um de cada vez, com 3 segundos de intervalo. O segundo aparece da porta do fundo enquanto o jogador lida com o primeiro.
- **Proposito de design:** Inimigo mais lento do jogo. Existe para que o jogador aprenda que pode passar por eles sem necessariamente atacar, ou que pode atacar antes que cheguem. Nao ha pressao real aqui.

### Wave 2 — Sala de Reunioes (tutorial de stealth opcional)

**Burocrata-Zumbi x4**
- Mesmos stats, mas dispostos em grupos de dois
- A sala tem MESAS que o jogador pode usar como cobertura (agachado sob a mesa = invisivel para Burocrata)
- Dois deles estao comendo (o que?) atras da porta. Se o jogador os agitar, os quatro acordam.
- **Proposito de design:** Primeira bifurcacao implicita — combater (4 inimigos frageis) ou stealth (passar por baixo das mesas). Nenhuma e obrigatoria. O jogo nao diz qual e melhor. O jogador descobre.

### Wave 3 — Escada Rolante (primeira horda pequena)

**Burocrata-Zumbi x6, entrando aos pares a cada 4 segundos**
- Aparecem subindo a escada rolante (que esta, ironicamente, funcionando normalmente)
- Espaco e mais apertado. Plataformas: corrimao da escada e arquivos empilhados no patear intermediario
- **Proposito de design:** Primeira situacao de pressao. O jogador ja sabe atacar. Agora tem que manter ritmo. Nenhuma mecanica nova — so volume.

### Inimigo especial — O Carlao (tutorial de contexto narrativo)

**Carlao-Zumbi** (nao e boss, e inimigo narrativo unico desta quest)
- Visual: Gordinho, social-media manager do Ministerio, camisa polo laranja, cracha "CARLAO — COMUNICACAO INSTITUCIONAL", tablet na mao exibindo tuites de 8 de janeiro
- HP: 5 hits (ligeiramente mais resistente que Burocrata comum)
- Comportamento: Ao ver Ze, diz: "Ze... voce nao vai acreditar... o trending topic..."
- Ao tomar primeiro hit: "Isso... vai virar meme..."
- Ao morrer: Solta o tablet no chao. O tablet exibe tuites reais estilizados na tela de morte (efeito visual: tuites voando como particulas)
- **Proposito de design:** Introduz o conceito de inimigos com personalidade e dialogo. Prepara o jogador para os bosses mais ricos do jogo. O tablet e coletavel (item narrativo, nao gameplay).

---

## MECANICAS DE GAMEPLAY INTRODUZIDAS

### 1. Movimento horizontal + pulo simples (primeiro 30 segundos)

**Como e ensinado:**
- Ze inicia na posicao sentado. Ao pressionar qualquer direcao, ele levanta e o jogo exibe por 2 segundos um indicador discreto (seta animada) mostrando os controles de movimento.
- O primeiro Burocrata-Zumbi aparece a altura do chao mas com uma mesa bloqueando o caminho. A mesa tem altura de 1 pulo. O indicador de pulo (seta para cima) aparece brevemente sobre a mesa.
- Assim que o jogador pula a mesa pela primeira vez, os indicadores somem e nao voltam mais.

**Por que funciona:** O jogador nunca le "pressione X para pular". Ele ve um obstaculo, ve um indicador discreto, e descobre sozinho. O prazer de descoberta e preservado.

### 2. Ataque corpo-a-corpo com vassoura (primeiro minuto)

**Como e ensinado:**
- Antes de encontrar o Carlao-Zumbi, ha um closet de limpeza com a porta entreaberta. Dentro, uma vassoura BRILHANDO (brilho dourado sutil, mesma linguagem visual de todo item coletavel do jogo).
- Quando Ze pega a vassoura, um texto aparece por 1.5 segundos: **"VASSOURA DE PALHA — Dano: 2 | Durabilidade: 15 hits"**
- O primeiro Burocrata-Zumbi aparece exatamente 1 segundo depois da vassoura ser pega. Nao ha inimigos antes disso neste corredor especifico.
- **Detalhe critico:** A vassoura tem durabilidade. Ao quebrar (15 hits), Ze continua com soco (dano: 1). Isso e ensinado naturalmente quando a vassoura quebra no Carlao e Ze ainda pode atacar. O jogador aprende que nunca fica totalmente desarmado.

### 3. Barra de HP e dano (passivo, aprendido ao levar o primeiro hit)

- Ao levar o primeiro hit de qualquer inimigo, a barra de HP no canto superior esquerdo pulsa rapidamente por 1 segundo chamando atencao.
- Ze exclama: "Puta que pariu!" (texto flutuante sobre o personagem)
- Nao ha instrucao explicita. O jogador ve a barra diminuir e conecta causa e efeito.

### 4. Drop de item no chao (final da Wave 2)

**Como e ensinado:**
- Um dos Burocratas da Sala de Reunioes solta um **Sanduiche do Refeitorio** ao morrer (restaura 20% de HP).
- O item cai no chao e brilha. Ze pode coletá-lo passando por cima.
- Nao ha instrucao. O brilho indica "pode pegar". O jogador vai querer.

---

## ITENS COLETAVEIS / ARMAS INTRODUZIDAS

| Item | Local | Efeito | Nota |
|---|---|---|---|
| Vassoura de Palha | Closet de limpeza (corredor 1) | Dano 2, 15 hits de durabilidade | Primeira arma do jogo |
| Sanduiche do Refeitorio | Drop do Burocrata na Sala de Reunioes | Restaura 20% HP | Primeiro heal do jogo |
| Tablet do Carlao | Drop do Carlao-Zumbi | Item narrativo (nao tem efeito de gameplay) | Exibe tuites satiricos ao ser inspecionado |
| Cracha Funcional de Ze | Inventario desde o inicio | Abre portas de segurança do Ministerio | Usado na Wave 3 para uma porta bloqueada |

---

## CONDICAO DE SUCESSO

Ze alcanca o telheiro de vidro (portao de seguranca da saida do Ministerio) com pelo menos 1 ponto de HP. A animacao de saida e ativada: Ze empurra o torniquete de seguranca e cai do outro lado do portao, ofegante, enquanto a janela do edificio atras dele e quebrada por dentro por um Burocrata-Zumbi.

> **ZE:** "Pronto. Hora extra cancelada."

---

## CONDICAO DE FALHA

Ze chega a 0 HP em qualquer ponto do nivel.

**Tela de Game Over especifica desta quest:**
Ze cai no chao do corredor. Um Burocrata-Zumbi se ajoelha sobre ele e carimba o relatorio de produtividade na testa de Ze com um carimbo gigante vermelho: **"IMPRODUTIVO"**.

*Texto na tela:* **"Hora extra encerrada. Motivo: apocalipse zumbi."**
*Subtexto:* "Tente novamente?"

**Checkpoint:** A quest tem checkpoint no inicio da Wave 3 (escada rolante). Morte apos esse ponto retorna ao checkpoint, nao ao inicio da quest.

---

## RECOMPENSAS

**Narrativa:**
- Ze encontra Dona Marta no telheiro de vidro da saida — ela veio de baixo, do subsolo do Ministerio, pelo tunel de servico. Este e o primeiro encontro com a aliada principal do Modo Cidadao.
- Ze ve pela primeira vez, com seus proprios olhos, a escala do caos: a Esplanada inteira, do angulo externo do Ministerio. A nevoa verde e visivel no horizonte, subindo da Praca dos Tres Poderes.

**Gameplay:**
- Desbloqueio permanente: **Burocrata-Zumbi** adicionado ao Bestiario (menu de lore do jogo)
- Pontuacao base da quest calculada: kills x 10 + HP restante x 5 + bonus de tempo
- Se jogador usou rota de stealth na Sala de Reunioes: bonus **"Fantasma do Funcionalismo"** (+200 pontos, conquista narrativa)
- Vassoura de Palha permanece no inventario se ainda tiver durabilidade

---

## SETUP NARRATIVO DE FECHAMENTO

*Ze e Dona Marta estao no telheiro externo. A camera recua lentamente mostrando a Esplanada completa. Centenas de figuras cambalendo. A nevoa verde densa nas ruas. Helicoptero da Policia Militar passando.*

> **DONA MARTA:** *(vassoura no ombro, respirando tranquila)* "Bom. Voce saiu. Eu achei que ia ter que te carregar."
> **ZE:** "A senhora... a senhora esta bem? Seus olhos nao estao verdes."
> **DONA MARTA:** "Meu filho, eu trabalho no Congresso ha 37 anos. Ja fui imune a coisas piores que nevoa. Ja fui imune a emenda constitucional votada as 3 da manha."
> **ZE:** "A gente precisa sair da Esplanada."
> **DONA MARTA:** "Nao." *(aponta para o Congresso ao longe)* "A gente precisa ir pra la. Minha filha ta presa la dentro. Na cantina. O turno dela era ate as 18h."

*Ze olha para o Congresso. Olha para a nevoa. Olha para Dona Marta.*

> **ZE:** "...Tudo bem. Mas pelo caminho eu preciso de uma arma melhor que vassoura."

*Fade out. Titulo aparece:*

**PROXIMO: Q1-02 — CORREDOR DOS MORTOS**

---

## OBSERVACOES DE ARTE E AUDIO

**Background do nivel:**
- Interior: estilo cubista caricatural, mesas de Ministerio com papeis empilhados ate o teto, canecas de cafe frias, post-its cobertos de siglas inventadas (ex: "PPA/LOA/LDO — alinhar com SUBGESTO/COPLAN"). Visivel pela janela: Esplanada em caos, bandeiras, fumaca.
- O ceu ao fundo (visivel pelas janelas) deve ser AZUL CLARO de verao brasiliense, sem nuvens. Esse constraste com o caos na rua e a nevoa verde e crucial para o tom.

**Paleta interior:** Tons de bege e cinza para o Ministerio. Verde toxico APENAS na nevoa e nos olhos dos zumbis. Nenhum outro elemento verde no nivel — isso garante que verde = perigo, leitura imediata.

**Audio:**
- Musica ambiente: MPB instrumental levemente distorcida, como radio de escritorio com pilha fraca.
- Ao aparecer o primeiro zumbi: a radio distorce mais, o ritmo desafina sutilmente.
- Efeito de hit no Burocrata: som de carimbo gigante batendo em papel.
- Morte do Carlao: som de notificacao de Twitter/X, repetindo 3 vezes em pitch descendente.
- Ao chegar no telheiro externo: a musica para completamente. So vento e o barulho distante de tumulto. Esse silencio e o momento de respiracao antes do Capitulo escalar.

**Animacao especifica de Ze:**
- Ao pegar a vassoura, Ze a segura na altura do peito e faz uma expressao de "serve". Nao e entusiasmado. E pragmatico. Esse e o personagem.
- Ao levar hit: Ze grita uma palavrao, mas o texto na tela e censurado com "*#@!" no estilo HQ.

**Referencia de estilo:** Interior identico (espiritualmente) ao cenario de Ministerio do Metal Slug 3, mas com grafismo de caricatura politica brasileira estilo Andre Guedes. Cartazes de campanha velhos na parede. Foto emoldurada de todos os presidentes desde Sarney na parede do corredor (Ze passa por ela correndo sem olhar).
