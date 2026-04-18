# Q1-06 — O GENERAL DE PIJAMA
### Quest Design Document | Capitulo 1 | Boss Fight — Modo Cidadao + Politico

---

## IDENTIDADE

| Campo | Valor |
|---|---|
| **ID** | Q1-06 |
| **Titulo** | O General de Pijama |
| **Modo** | Ambos — boss fight compartilhado, dialogos e recompensas distintos por modo |
| **Duracao estimada** | 6-8 minutos |
| **Dificuldade** | 4/5 — Boss com tres fases, aplica todas as mecanicas aprendidas |
| **Posicao no cap** | Quest final. Climax do Capitulo 1. |

---

## PRE-REQUISITOS

Q1-05 concluida. O grupo esta na Praca dos Tres Poderes, frente ao Congresso.

---

## SETUP NARRATIVO DE ABERTURA

*A arena se abre: um segmento de 4 telas de largura em frente a rampa do Planalto, com o Congresso ao fundo e os Tres Poderes enquadrando o espaço. E a maior arena do Capitulo 1.*

**VERSAO CIDADAO:**

> **GENERAL** *(ao ver Ze)*: "SOLDADO! Voce esta do lado ERRADO da historia! Eu tenho informacao PRIVILEGIADA de que a cavalaria vem! Ta no grupo!"
> **ZE:** "Qual grupo? O de trezentas pessoas que ninguem pediu pra entrar?"
> **GENERAL** *(pausa. Olha o celular.)*: "Eu tenho oitocentos e quarenta e sete grupos."
> **ZE:** "...Que Deus tenha misericordia de voce."

**VERSAO POLITICO:**

> **GENERAL** *(ao ver Waldeco)*: "Deputado Waldeco! Voce veio nos libertar!"
> **WALDECO:** "Eu vim fazer campanha. Libertar e efeito colateral."
> **GENERAL** *(processando. Processando. Rugido.)*: "TRAIDOOOOR! EU TE VOTEI!"
> **WALDECO:** "Todo mundo diz isso. Eu nao tenho como verificar."

*O General levanta o celular em diracao ao ceu. Uma corneta de WhatsApp toca. O titulo da boss fight aparece na tela em fonte maxima:*

**"GENERAL DE PIJAMA"**
*(Subtitulo: "Zumbi-Lider. Cabo Reformado. 847 Grupos de Telegram.")*

*Barra de HP do General aparece no topo da tela. Cheia.*

---

## ARENA

**Dimensoes:** 4 telas de largura (scroll horizontal livre dentro da arena, sem saida pelas laterais)
**Plataformas:**
- Gradis tombados (altura de 1 pulo): espalhados pela arena, criados pelos movimentos do General ao longo do combate
- Arquibancadas improvisadas do acampamento (altura de 2 pulos): nas bordas
- Rampa do Planalto (lateral direita): Ze/Waldeco pode subir parcialmente para evitar ataques rasteiros

**Elementos do cenario usados no combate:**
- Bandeiras do Brasil espetadas no chao (o General usa como obstaculos e armas)
- Carros de som do acampamento (o General pode empurra-los como projeteis na Fase 3)
- Cameras de TV ao vivo (Waldeco pode interagir com elas; Ze as ignora)

---

## O BOSS: GENERAL DE PIJAMA

**Visual (conforme storytelling):** Gordao, pijama ESTAMPADO de camuflagem (nao e farda — e pijama de dormir com estampa de camuflagem), chinelo de couro arrastando no asfalto, celular na mao direita com tela rachada mas ainda funcionando, boina torta, oculos de sol de camelô, medalhas falsas no peito do pijama (olhando de perto, sao tampas de garrafa).

**HP total:** 60 pontos de vida (divididos em 3 fases de 20 HP cada)
**Velocidade base:** Lenta (40px/s)
**Tamanho:** 2x a altura de Ze/Waldeco

**Regra geral:** O General telegrafar TODOS os ataques com audio e animacao antes de executar. Nenhum ataque e inescapavel se o jogador prestar atencao. O combate e sobre ler os sinais, nao sobre reflexo puro.

---

## FASE 1 (HP: 60-40) — "A INFORMACAO PRIVILEGIADA"

**Tema:** O General ainda acredita no plano. Ataques basicos, convocacao de horda.

### Ataque 1A — "Atencao, Tropa!"
**Telegrafio:** O General levanta o celular com o braco esticado. Som de corneta de WhatsApp toca (2 segundos de animacao de carregamento antes do efeito).
**Efeito:** 3 Patriotas-Zumbi spawnados das bordas da tela. Vem de ambos os lados.
**Frequencia:** A cada 20 segundos na Fase 1.
**Contra:** Matar os Patriotas antes que cheguem; usar ranged para desorientar o General durante a convocacao (interrompe o ataque se o General for atingido durante os 2 segundos de carregamento).
**Tells do dialogo:** "REFORCO CHEGANDO! TO NO GRUPO!"

### Ataque 1B — "Caminhada do Pijama"
**Telegrafio:** O General abaixa o celular e começa a andar lentamente em direcao ao jogador. Seus chinelos arrastam fazendo barulho especifico (PLASC PLASC PLASC).
**Efeito:** Dano de contato. 5 de dano se o jogador for atingido pelo corpo do General.
**Frequencia:** Continuo — o General sempre anda em direcao ao jogador entre outros ataques.
**Contra:** Manter distancia. O General e lento. Facil de evitar se o jogador nao estiver ocupado com horda.

### Ataque 1C — "Celularada"
**Telegrafio:** O General levanta o celular acima da cabeca (animacao de arremesso, 1 segundo).
**Efeito:** O celular voa em trajetoria reta e bate no jogador (3 de dano). O celular cai no chao e TOca notificacao de WhatsApp. Se o jogador PEGAR o celular caido (passar por cima), ve uma mensagem satirica no display (item narrativo).
**Frequencia:** A cada 15 segundos.
**Contra:** Pular ou agachar. O celular e um projetil rasteiro (altura do torso) ou alto (altura da cabeca) alternando.

**Transicao para Fase 2 (ao chegar em 40 HP):**
O General toma dano suficiente para perder o equilibrio. Cai de joelhos. Para. Olha para as maos. Olha para Ze/Waldeco.

> **GENERAL** *(a 40 HP)*: "EU SERVI ESTE PAIS! Eu mereco RESPEITO! Eu fui... fui..."
> *(longa pausa)*
> "...cabo reformado."

*Silencio. Depois o General ruge e muda de comportamento.*

---

## FASE 2 (HP: 40-20) — "FAKE NEWS TATICA"

**Tema:** O General fica mais agressivo e imprevisivel. Ataques de area e confusao visual.

### Ataque 2A — "Fake News Tatica!"
**Telegrafio:** O General para no centro da arena, levanta os bracos (animacao de abencoamento involuntario), e o celular no chao (do ataque 1C) explode em luz.
**Efeito:** Manchetes falsas cobrindo 30% da tela por 2 segundos ("INVASAO DE ZUMBIS E FAKE NEWS, AFIRMA GENERAL", "ZE/WALDECO E AGENTE DE SOROS", "A NEVOA VERDE E SO FUMAÇA DE CHURRASCO"). Dano indireto: o jogador nao ve ataques que chegam durante os 2 segundos de tela coberta.
**Frequencia:** A cada 25 segundos.
**Contra:** Memorizar posicao dos inimigos antes das manchetes aparecerem. Nao se mover durante os 2 segundos — ficar parado e mais seguro que tentar avancar as cegas.

### Ataque 2B — "Bandeirão!"
**Telegrafio:** O General pega um bandeirão do Brasil espetado no chao (animacao de arrancar do chao, 1.5 segundos). Som de tecido rasgando ao erguer.
**Efeito:** O General avanca com o bandeirão como escudo frontal (cobre 60% da altura do General) e faz varredura horizontal. Dano de contato: 6. A varredura tem alcance de meia tela.
**Frequencia:** 2 vezes por fase.
**Contra:** Pular por cima do bandeirão e atacar pelas costas enquanto o General passa. Ou usar ranged (Sinalizador) para desorientar antes que o avanco comece.
**Nota:** O bandeirão do Brasil protegendo o General e a piada politica mais densa do boss fight. E intencional.

### Ataque 2C — "Grupo do Telegram!"
**Telegrafio:** O General pega um segundo celular (de onde? Ninguem sabe. Esta escondido no pijama) e comeca a digitar frenético (animacao de dois polegares digitando, 2 segundos).
**Efeito:** 5 Patriotas-Zumbi spawnados — mais que a Fase 1 e mais rapidos.
**Frequencia:** 1 vez na Fase 2.
**Contra:** Matar o General antes que os Patriotas cheguem, ou usar ranged para eliminar os Patriotas ao spawnarem.

**Transicao para Fase 3 (ao chegar em 20 HP):**
O General cai no chao. Fica de quatro. Respira fundo. Levanta olhando diretamente para o jogador. Os olhos verdes pulsam mais forte. Os chinelos... ficam para tras. Descalco agora.

> **GENERAL:** "...A cavalaria... vem... confiem... no plano..."

*Sem piada. Sem ironia. Apenas a crenca sincera. O game design aqui pede um beat de silencio — o General e ridiculo e simultaneamente tragico. 1.5 segundos sem ataque, sem audio. Depois:*

> *(Celular toca. Audio de WhatsApp: "BOM DIA GRUPO!")*

*O General ruge. Fase 3.*

---

## FASE 3 (HP: 20-0) — "INTERVENCAO!"

**Tema:** O General perde o controle racional e entra em modo de furia pura. Ataques mais rapidos, area maior, mais dano.

**Mudanca visual:** O pijama do General tem rasgos agora. As medalhas de tampinha de garrafa caem no chao (efeito visual de particulas). A boina voa. O General esta... mais humano? Mais zumbi? Os dois ao mesmo tempo.

### Ataque 3A — "Carga Final!"
**Telegrafio:** O General recua para a extremidade oposta da tela (2 segundos de recuo, muito claro). Sorri. Corre.
**Efeito:** Dash horizontal de ponta a ponta da arena, velocidade 3x a normal. Dano: 8. Area de hit: o corpo inteiro do General durante o dash.
**Frequencia:** A cada 18 segundos.
**Contra:** Pular para cima e deixar o General passar por baixo (se o jogador estiver no chao quando o dash começa, tomar dano e inevitavel — o sinal visual e para pular ANTES do dash).

### Ataque 3B — "Carro de Som!"
**Telegrafio:** O General empurra um carro de som do acampamento pelo cenario (animacao de empurrar, 2.5 segundos com som de motor ligando).
**Efeito:** O carro de som rola pela arena causando dano de 5 ao contato. Ele nao para — vai de uma borda a outra e volta (efeito de bounce). Fica ativo por 10 segundos antes de explodir.
**Frequencia:** 1 vez na Fase 3.
**Contra:** Pular o carro na primeira passagem, usar ranged para explodir o carro antes do tempo (Sinalizador no carro = explosao imediata, mas dano de area).

### Ataque 3C — "INTERVENCAO MILITAR!"
**Telegrafio:** O General para. Levanta os bracos para o ceu. Voz amplificada por nao se sabe qual tecnologia: "EU... PECO... INTERVENCAO!"
**Efeito (FASE ESPECIAL — 1 vez por boss fight):** Por 5 segundos, a tela escurece e manchetes chegam de todos os angulos como projeteis (6 manchetes simultaneas, voando em diagonais). Cada manchete que acerta: 3 de dano. O jogador deve se mover constantemente para desviar.
**Contra:** O "olho" do ataque e o General parado — se o jogador atingir o General durante os 5 segundos de carregamento, o ataque e interrompido (bonus: o General fica atordoado por 3 segundos).

**Kill:**
Ao levar o ultimo hit, o General cai lentamente. Devagar. O celular cai antes dele. Tela do celular mostrando uma mensagem de WhatsApp nao enviada: "CHEGOU A CAVALARIA CAMARADAS".

O General cai. O celular toca uma ultima notificacao: **"BOM DIA GRUPO!"**

O General sorri levemente. Os olhos verdes apagam.

---

## DIALOGOS COMPLETOS DO BOSS FIGHT

**MODO CIDADAO:**

| HP | Dialogo |
|---|---|
| 100% (abertura) | GENERAL: "SOLDADO! Voce esta do lado ERRADO da historia! Eu tenho informacao PRIVILEGIADA de que a cavalaria vem! Ta no grupo!" / ZE: "Qual grupo? O de trezentas pessoas que ninguem pediu pra entrar?" |
| 80% | GENERAL: "Eu NAO sou zumbi! Eu sou PATRIOTA! Ha uma diferenca!" / ZE: "Quais sao as diferencas especificas?" / GENERAL: "..." |
| 60% | GENERAL (fase 1 acaba): "EU SERVI ESTE PAIS! Eu mereco RESPEITO! Eu fui... fui... cabo reformado." |
| 40% | GENERAL: "A cavalaria vem! Esta no grupo privado! So pra quem aguenta a verdade!" |
| 20% | GENERAL (fase 2 acaba): "...A cavalaria... vem... confiem... no plano..." |
| 10% | ZE: "General. Nao tem cavalaria. Nunca teve cavalaria." / GENERAL: "...Tinha. Ta atrasada." |
| 0% | CELULAR: "BOM DIA GRUPO!" |

**MODO POLITICO:**

| HP | Dialogo |
|---|---|
| 100% (abertura) | GENERAL: "Deputado Waldeco! Voce veio nos libertar!" / WALDECO: "Eu vim fazer campanha. Libertar e efeito colateral." / GENERAL: "TRAIDOOOOR! EU TE VOTEI!" |
| 80% | GENERAL: "Voce nao e diferente dos outros! Voce so quer foto!" / WALDECO: "Isso e uma critica valida e eu nao tenho como refutar." |
| 60% | GENERAL: "EU SERVI ESTE PAIS! / WALDECO: (baixinho, para o celular, gravando) "...cabo reformado..." |
| 40% | GENERAL: "Se voce me ajudar, eu divulgo nos grupos! Oitocentos e quarenta e sete grupos!" / WALDECO: "...Isso... isso pode ser util." / (Waldeco faz uma pausa no combate. Ze grita: "NAO NEGOCIA COM ELE!") |
| 20% | (fase 2 acaba, mesma linha: "...A cavalaria vem...") |
| 10% | WALDECO: "General. O senhor foi usado. Por politicos que nao vieram ate aqui. Eu vim." / GENERAL: "...Voce veio pra foto." / WALDECO: "...Sim. Mas eu vim." |
| 0% | CELULAR: "BOM DIA GRUPO!" |

---

## CONDICAO DE SUCESSO

O General cai. Silencio na arena. Patriotas-Zumbi restantes param confusos (sem lider, perdem o "objetivo") e ficam desorientados, andando em circulos.

**VERSAO CIDADAO:**
Ze esta em pe. Dona Marta chega ao lado dele. Luciana (se sobreviveu) segura a mao da mae.

> **ZE:** *(olhando o General caido)* "Acabou."
> **DONA MARTA:** "Esse acabou. Tem mais por ai."
> **ZE:** "...Quanto mais?"
> **DONA MARTA:** "Meu filho, Brasilia tem quinhentos e dez parlamentares, duas mil assessorias, quatorze mil funcionarios comissionados e quarenta anos de corrupcao enterrada nas fundacoes. A nevoa nao fez zumbi novo. So revelou o que ja estava morto."

**VERSAO POLITICO:**
Waldeco esta em pe. Ze esta ao lado. Waldeco olha o General. Pega o celular caido. Olha os 847 grupos.

> **WALDECO:** *(muito quieto, para si mesmo)* "Oitocentos e quarenta e sete grupos. Isso e... isso e uma rede eleitoral."
> **ZE:** "Voce ta pensando em votos agora?"
> **WALDECO:** "Eu penso em votos quando acordo, quando como, quando durmo e aparentemente quando luto contra zumbi."
> **ZE:** "Isso e doentio."
> **WALDECO:** "Isso e politica. A diferenca e pequena."

---

## CONDICAO DE FALHA

Ze/Waldeco chega a 0 HP durante qualquer fase.

**Game Over especifica do boss fight:**
O General esta em pe sobre o jogador caido. Levanta o celular. Tira uma selfie. A selfie aparece em tempo real: General sorrindo, jogador desacordado no chao. Legenda da selfie: "Vitoria da Democracia".

*Texto:* "Derrota. Mas a cavalaria ainda vem."
*Subtexto:* "Continuar de onde parou?"

**Checkpoint:** Inicio do boss fight (ao entrar na arena). Nao ha checkpoint dentro das fases do boss — a luta e continua, mas o jogador reinicia com os itens que tinha ao entrar.

---

## RECOMPENSAS

**Narrativa:**
- Cutscene de fechamento do Capitulo 1 (ver abaixo)
- Desbloqueio do Bestiario completo do Capitulo 1

**Gameplay — Cidadao:**
- Conquista: **"Tecnico Administrativo do Apocalipse"** — completou o Capitulo 1 como Cidadao
- Item permanente para o Capitulo 2: **Cracha Funcional Atualizado** (Ze recebe um cracha de acesso especial que abre mais portas em Brasilia)
- Bonus de pontuacao: cada fase do General derrotada sem levar dano = +500 por fase

**Gameplay — Politico:**
- Conquista: **"Apareceu na Historia"** — completou o Capitulo 1 como Politico
- Item permanente para o Capitulo 2: **Celular do General** (Waldeco herda os 847 grupos — funciona como recurso de Popularidade passivo no inicio do Capitulo 2)
- Bonus de pontuacao: cada dialogo do General respondido com opcao de dialogo (se implementado) = +200

**Replay incentive:**
- Ao completar o Capitulo 1 nos dois modos, conquista especial: **"Duas Perspectivas, Um Pais"** (+1000 pontos, banner de titulo especial)
- Dialogo exclusivo de Ze e Waldeco se o jogador os encontra tendo jogado os dois modos: Ze diz "Eu te vi la em cima. Voce tava gravando video." Waldeco: "E voce tava suando muito."

---

## CUTSCENE DE FECHAMENTO DO CAPITULO 1

*Comum a ambos os modos, com pequenas variacoes de camera e dialogo.*

*A Praca dos Tres Poderes. Final da tarde de 8 de janeiro. O sol esta baixo, laranja, sobre o horizonte de Brasilia. A nevoa verde se estende pela Esplanada inteira. Ao fundo, o Congresso com algumas janelas quebradas. O Supremo com a nevoa entrando pelas frestas.*

> **NARRADOR** *(voz do Andre Guedes, tom seco)*: "No dia 8 de janeiro de 2023, quatro mil pessoas invadiram os Tres Poderes. A conta do prejuizo foi de onze milhoes de reais so no Supremo. A democracia nao tem como calcular o proprio prejuizo."

> "A nevoa verde que subiu das fundacoes de Brasilia naquele dia nao foi um acidente. Foi uma revelacao. A podridao ja estava la. A data so acelerou o processo."

> "Nas semanas seguintes, o governo tentou chamar de contaminacao ambiental. Os cientistas chamaram de sindrome desconhecida. O povo chamou de zumbi. E o povo, como de costume, estava mais perto da verdade."

*Camera recua ate mostrar Ze (ou Waldeco) de longe, pequeno, na Praca enorme e vazia, entre os Tres Poderes.*

> **NARRADOR:** "Isso foi o começo."

*Tela preta. Texto:*

**"CAPITULO 1 CONCLUIDO"**

*Depois:*

**"PROXIMO: CAPITULO 2 — O PRESO"**
*(Ago/Nov 2025 — O condominio do Lago Sul. A tornozeleira. O ferro de solda.)*

---

## OBSERVACOES DE ARTE E AUDIO

**Arena:**
- A Praca dos Tres Poderes como arena de boss e o cenario mais iconico do jogo. O Congresso ao fundo deve ser desenhado com precisao arquitetural suficiente para ser reconhecivel, mas com exagero caricatural que honra o estilo Andre Guedes.
- O ceu laranja do fim de tarde contrasta com o verde da nevoa — paleta deliberada (dourado vs. verde toxico = Brasil vs. corrupção, ou sol vs. podridao).
- Particulas constantes: santinhos de campanha velhos voando. Bandeiras rasgadas. Papeis de processos judiciais. Tudo isso deve ser visualmente presente sem prejudicar legibilidade dos personagens.

**Audio do boss fight:**
- Musica: orquestra que mistura "Hino Nacional" com distorcao progressiva de heavy metal. A cada fase perdida pelo General, a distorcao aumenta.
- Ataque "Atencao, Tropa!": audio real de corneta de WhatsApp (satira do meme cultural).
- Ataque "Fake News Tatica!": ao cobrir a tela com manchetes, o audio muda para multiplos locutores de radio falando ao mesmo tempo, incompreensiveis.
- Morte do General: a musica para. Silencio. O celular toca "BOM DIA GRUPO!" no silencio total. Esse e o momento de ouro. Cada jogador que ouvir isso vai querer clipar.
- Pos-boss: vento. Distancia. O som de Brasilia vazia.

**Detalhe de animacao critico:**
- A morte do General deve ter slow-motion nos ultimos 0.5 segundos. Ele cai em camadas: a boina primeiro, as medalhas de tampinha, o celular, o corpo. Tudo com som de impacto separado para cada item.
- O celular mostrando a mensagem nao enviada ("CHEGOU A CAVALARIA CAMARADAS") deve ser legivel pelo jogador. Zoom sutil no celular por 1.5 segundos antes do "BOM DIA GRUPO!" final.
- A expressao do General ao morrer e importante: nao e raiva, nao e medo. E convicta. Ele acreditou ate o final. Isso e a satira mais honesta do personagem.
