# Q1-04 — SANTINHO NO CAOS
### Quest Design Document | Capitulo 1 | Modo Politico

---

## IDENTIDADE

| Campo | Valor |
|---|---|
| **ID** | Q1-04 |
| **Titulo** | Santinho no Caos |
| **Modo** | Politico (Waldeco) |
| **Duracao estimada** | 5-7 minutos |
| **Dificuldade** | 2/5 — Mecanicas novas de Popularidade, combate padrao |
| **Posicao no cap** | Quest inicial do Modo Politico. Paralela a Q1-01 e Q1-02 (mesmo evento, perspectiva diferente). |

---

## PRE-REQUISITOS

Nenhum. Esta e a quest de abertura do Modo Politico. O jogador acabou de assistir a cutscene do Prologo e selecionou "Modo Politico".

---

## SETUP NARRATIVO DE ABERTURA

*Tela preta. Texto em fade-in:*

> **8 de janeiro de 2023. 13h15.**

*Waldeco esta no acampamento do QG, entre tendas e bandeiras. Ele distribui santinhos para manifestantes. Sorri para todo mundo. Cumprimenta criancas. O santinho tem sua foto com expressao sorridente e o slogan: "WALDECO — O DEPUTADO QUE APARECE".*

> **WALDECO (narracao interna):** "Cinco mil eleitores num so lugar. A maior concentracao de base eleitoral desde a posse. Eu precisava estar aqui. Nao pelo acampamento. Pelo banco de dados. Nome, bairro, telefone. Cada santinho distribuido e um contato novo."

*Som de explosao distante. Depois outro. A multidao comeca a se mover na direcao da Esplanada.*

> **WALDECO:** "E ai... eu tive uma ideia."

*A barra de Popularidade aparece no HUD pela primeira vez: 0%*

*Texto aparece no centro da tela:*

**"POPULARIDADE: 0%"**
*(Subtitulo: "Toda carreira politica comeca do zero. Ou de um escandalo que voce sobreviveu.")*

*Controles liberados. Quest iniciada.*

---

## OBJETIVO DO JOGADOR

Waldeco precisa atravessar o acampamento do QG (agora parcialmente infectado) em direcao ao corredor de acesso ao tunel subterraneo, enquanto distribui santinhos, recruta cabos eleitorais e toma a decisao sobre os 50 refugiados presos no acampamento.

**Objetivo de gameplay:** Chegar ao portao de acesso ao tunel com Popularidade acima de 20%.
**Objetivo bonus:** Chegar com Popularidade acima de 40% (afeta dialogo em quests futuras).

---

## LOCALIZACAO

**Acampamento do QG do Exercito**
Setor Militar Urbano, em frente ao Quartel-General do Exercito — Brasilia, DF

**Estrutura do nivel:**

```
[INICIO]                                                      [SAIDA]
Waldeco na    Area do      Palco do      Area dos     Portao do
tenda       -> acampamento -> acampamento -> refugiados -> tunel QG
(tutorial     (primeiros    (santinhos,   (DILEMA       (mini-boss
Popularidade)  zumbis,       cabos         MORAL #1)     de fechamento)
               recrutar)     eleitorais)
```

**Ambiente:**
- Acampamento com tendas, carros de som, bandeiras do Brasil e Bolsonaro por todo lado
- Palco com caixas de som ligadas (musicas patrioticas que vao distorcendo conforme a nevoa avanca)
- Barracas de comida e cafe comunitarios (items de cura espalhados)
- Ao fundo: QG do Exercito, portao fechado. A parede do QG e visivel o tempo todo — o Exercito nao vai abrir. Ninguem vai salvar ninguem.

---

## INIMIGOS PRESENTES

### Patriota-Zumbi (presente desde o inicio — mesmo tipo de Q1-03)

No acampamento, o Patriota-Zumbi e a ironia maxima: e um manifestante que veio pedir intervencao militar e acabou se tornando zumbi. Waldeco os encontra primeiro em pequenos grupos de 2-3.

**Comportamento especifico desta quest:** Alguns Patriotas-Zumbi (1 em cada 5) ainda estao semi-conscientes e respondem ao santinho de Waldeco. Ao receber um santinho, ficam confusos por 3 segundos (nao atacam). Waldeco pode passar por eles sem combater.

**Mecanica tutorial implicita de Popularidade:** Ao distribuir o primeiro santinho para o Patriota semi-consciente, um +5 aparece na barra de Popularidade. O jogador entende: distribuir santinhos = Popularidade.

**Quantidades:**
- Area do acampamento: 8 Patriotas, 3 semi-conscientes
- Palco do acampamento: 5 Patriotas infectados + 2 semi-conscientes
- Area dos refugiados: 10 Patriotas em volta (bloqueando saida dos refugiados)
- Portao do tunel: 4 Patriotas (mini-boss area)

---

## MECANICAS DE GAMEPLAY EXCLUSIVAS DO MODO POLITICO

### 1. Sistema de Popularidade (INTRODUCAO)

**Como funciona:**
- Barra de 0-100% no HUD, lado direito
- Acoes que aumentam Popularidade nesta quest:
  - Distribuir santinho para civil vivo: +5
  - Matar zumbi na frente de civil: +3
  - Salvar civil de ataque iminente de zumbi: +10
  - Completar o DILEMA MORAL favoravelmente ao povo: +15
- Acoes que diminuem Popularidade:
  - Levar dano (fraqueza visivel): -2
  - Abandonar civil sem santinho: -1
  - Opção C do Dilema (efeito visual de "povo desconfiado"): 0 agora, -10 depois

**Como e ensinado:**
- O primeiro civil vivo do jogo esta sentado em uma cadeira dobravel, olhando o caos com expressao de quem nao entende o que esta acontecendo. Um santinho brilha no inventario de Waldeco. A seta de dica aponta brevemente para o civil.
- Waldeco distribui o santinho: o civil sorri, diz "Vota em voce sim, deputado!", a barra sobe +5.
- Waldeco continua sem instrucao adicional. O sistema e claro.

### 2. Recrutamento de cabos eleitorais

**Como funciona:**
- Civis vivos (reconheciveis: sem olhos verdes, expressao de panico normal) podem ser recrutados como cabos eleitorais.
- Para recrutar: Waldeco distribui um santinho (custo: 1 santinho do inventario, começa com 20) e o civil escolhe entrar ou nao.
- Civil recrutado: luta por Waldeco por 30 segundos, dano 1 por ataque, HP baixo (3 hits).
- Cada civil recrutado aumenta Popularidade em +3.
- Cabos eleitorais sao descartaveis por design — eles morrem e isso e esperado. Waldeco nao tem reacao emocional a morte deles. Ze (no Modo Cidadao) teria. Isso diferencia os personagens.

**Quantidades de civis recrulaveis nesta quest:** 6 (dos quais 2 estao presos na area dos refugiados e so podem ser recrutados se voce os salvar primeiro)

### 3. Celular de Waldeco como HUD narrativo

O celular de Waldeco aparece no canto inferior direito da tela, exibindo em tempo real:
- Numero de seguidores (sobe com cada kill visivel para civis)
- Trending topics ficticios que mudam conforme o caos avanca
- Status do WhatsApp: grupos ativos, mensagens chegando (satiricos)

Isso e HUD passivo — nao afeta gameplay, mas e hilario e viralizavel.

---

## DILEMA MORAL #1 — OS REFUGIADOS DO QG

**Contexto:** Na Area dos Refugiados, 50 manifestantes estao presos entre tendas cercadas por 10 Patriotas-Zumbi. Eles gritam por ajuda. Um homem grita: "DEPUTADO! Vota em voce! Me salva!"

**O jogo pausa o combate. Tres opcoes aparecem na tela (5 segundos de tempo para escolher antes de uma opcao default ser aplicada):**

---

**OPCAO A — "SALVAR TODOS"**
> *"Vamos! Voce fica atras de mim!"*

- Ze/jogador precisa enfrentar os 10 Patriotas-Zumbi em combate direto para abrir caminho.
- Combate mais difícil desta quest (maior concentracao de inimigos até agora).
- Recompensa: Popularidade +15. Os 50 salvos saem correndo. 2 deles se oferecem para acompanhar Waldeco como cabos eleitorais extras.
- Dialogo pos-escolha: um dos salvos pega o celular e filma Waldeco lutando. Waldeco acena para a camera.

---

**OPCAO B — "SALVAR OS QUE PROMETEM VOTAR"**
> *"Quem votar no Waldeco Pereira, me segue. Os outros... Deus e grande."*

- Waldeco grita isso. Os 50 refugiados se dividem: 35 levantam a mao (prometem votar), 15 ficam sentados olhando com expressao de julgamento.
- Waldeco luta apenas pelos 35 (5 Patriotas-Zumbi, mais facil).
- Recompensa: Popularidade +5. 15 civis ficam pra tras.
- Dialogo pos-escolha: um dos 15 abandonados, no chao, soluça: "...eu nao podia levantar o braco. Luxacao." Waldeco ja foi embora.

---

**OPCAO C — "DISCURSO PRIMEIRO, SAIDA DEPOIS"**
> *"CIDADAOS! Nao temam! Waldeco Pereira, deputado pelo povo, VEIO LUTAR!"*

- Waldeco sobe numa cadeira e discursa. Os 50 refugiados assistem confusos. Os Patriotas-Zumbi param por 8 segundos (atraidos pelo barulho do discurso) — janela para fugir.
- Waldeco foge pelo lado enquanto os refugiados sao deixados para tras.
- Os refugiados so sao infectados depois. Waldeco nao ve.
- Recompensa: Popularidade +20 imediata (cobertura de camera por um refugiado que filmou o discurso). Sem penalidade agora.
- CONSEQUENCIA FUTURA: Na Fase 4, um dos refugiados da entrevista para um portal: "Ele discursou e fugiu enquanto nossos parentes viravam zumbi." Popularidade -10 em Q4.

---

**DEFAULT (sem escolha em 5s):** Opcao C automaticamente. Waldeco congela de indecisao e foge por instinto.

---

## ITENS COLETAVEIS / ARMAS INTRODUZIDAS

| Item | Local | Efeito | Nota |
|---|---|---|---|
| Santinhos (x20) | Inventario inicial de Waldeco | +5 Popularidade por uso em civil. Sem efeito em zumbi. | Recurso unico do Modo Politico |
| Selfie Stick (arma) | Drop de NPC photographer-zumbi | Dano 2, alcance ligeiramente maior que vassoura. Animacao de golpe e um selfie tirado durante o ataque. | Arma iconica do Politico |
| Power Bank | Barracas de suprimento | Restaura 25% HP E recarrega 3 santinhos | Heal + recurso combinado |
| Pasta de Financiamento | Tenda de liderança do acampamento | Item narrativo — revela lista de doadores do acampamento (satirico, nomes ficticios mas eventos reais) | Waldeco: "Util. Muito util." |

---

## CONDICAO DE SUCESSO

Waldeco chega ao portao do tunel com Popularidade acima de 20%. O portao e uma grade metalica trancada — mas Waldeco encontra a chave em um grupo de WhatsApp de politicos. Ao abrir o portao, uma mini-horda de 4 Patriotas-Zumbi aparece. Este e o combate de fechamento da quest.

*Animacao de saida:* Waldeco entra no tunel, vira para tras, tira uma selfie com o caos ao fundo, e fecha o portao. A selfie aparece como notificacao de post nas redes sociais: 847 likes em 3 segundos.

---

## CONDICAO DE FALHA

- Waldeco chega a 0 HP, OU
- Waldeco chega ao portao com Popularidade 0% (foi tao impopular que ninguem abre o portao — literalmente ninguem quer que ele entre)

**Tela de Game Over especifica:**
Se Waldeco morre: ele cai com um santinho na mao. Um Patriota-Zumbi pega o santinho, olha, e come.
Se Popularidade 0%: a grade nao abre. Um porteiro aparece do nada: "Candidato com 0% de aprovacao nao entra." Texto: *"Nem no apocalipse tem eleitor. Tente novamente."*

**Checkpoint:** Entrada da Area dos Refugiados (antes do Dilema Moral).

---

## RECOMPENSAS

**Narrativa:**
- Waldeco esta no tunel. Apos o portao fechar, ele continua para a camara de sobreviventes onde vai encontrar Ze e Dona Marta (Q1-03).
- Monolog interno de Waldeco: "Eles vao lembrar de mim. Num dia em que tudo virou zumbi, eu estava la. Lutando. Aparecendo. Isso e o que politico faz: aparece." (Ze nao ouve este pensamento — so o jogador.)

**Gameplay:**
- Desbloqueio: Sistema de Popularidade explicado no menu de ajuda (acessivel, nao obrigatorio)
- Selfie Stick permanece no inventario
- Bonus por Opcao A do dilema: conquista **"Mandato Genuino"** (+500 pontos)
- Bonus por Opcao C do dilema: conquista **"Marketing Politico"** (+200 pontos, mas com aviso: "Efeito colateral futuro detectado")

---

## SETUP NARRATIVO DE FECHAMENTO

*No tunel. Waldeco caminha sozinho por alguns segundos. Seu celular ilumina o caminho. Notificacoes chegando.*

> **WALDECO (olhando o celular):** "Trending topic. 'Politico distribui santinho no apocalipse zumbi'. Duzentas e quarenta compartilhamentos. Isso e... isso e exatamente o que eu precisava."
> *(Para. Ouve passos a frente.)*
> "...Tem alguem ai?"

*Luz ao fundo do tunel. Vozes. Ze e Dona Marta.*

**PROXIMO: Q1-03 — A ALIANCA DA VASSOURA**

---

## OBSERVACOES DE ARTE E AUDIO

**Background do nivel:**
- Acampamento do QG deve ser RICO em detalhe: tendas de camping, carros de som com adesivos de Bolsonaro, bandeiras em todo lugar. Cozinha comunitaria com panelas ainda fumegando. Banheiro quimico tombado no fundo (Waldeco nao passa perto).
- O QG do Exercito ao fundo: portao fechado, guardas immoveis atras do portao (podem ser zumbis tambem, mas o portao nao abre de jeito nenhum). Esta imagem — o exercito nao intervindo — e deliberada e deve ser visualmente clara.
- Palco do acampamento: microfone caido, bandeiras rasgadas, som distorcido ainda saindo das caixas ("...PADRAO DEU NO MARA DO..."). A distorcao do som e progressiva conforme a nevoa avanca.

**Audio:**
- Musica de fundo: marcha militar de fanfarra, lenta e soturna, que começa a desafinar gradualmente.
- Som do santinho distribuido: papel amassado + ding de notificacao. Satisfatorio. Viciante.
- Som de Popularidade subindo: som de vitoria pequena (3 notas ascendentes de trompete, discreto).
- Som de Popularidade caindo: som de booo da plateia (muito discreto, so pra quem presta atencao).
- Dilema Moral: musica para completamente. So som ambiente. A decisao e silenciosa para aumentar peso.
- Selfie Stick como arma: ao atacar, som de shutter de camera. Cada hit = foto tirada. O zumbi congela no frame por 0.1 segundo antes de cair.

**Visual do HUD politico vs. HUD cidadao:**
- Ze: HP bar simples, contador de score.
- Waldeco: HP bar + barra de Popularidade + celular no canto (seguidores, trending). O HUD de Waldeco e mais poluido intencionalmente — e a vida de um politico.
