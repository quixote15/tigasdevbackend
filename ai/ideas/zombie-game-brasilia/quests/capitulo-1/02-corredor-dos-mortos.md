# Q1-02 — CORREDOR DOS MORTOS
### Quest Design Document | Capitulo 1 | Modo Cidadao

---

## IDENTIDADE

| Campo | Valor |
|---|---|
| **ID** | Q1-02 |
| **Titulo** | Corredor dos Mortos |
| **Modo** | Cidadao (Ze) |
| **Duracao estimada** | 4-6 minutos |
| **Dificuldade** | 2/5 — Dois inimigos novos, mecanica de escudo introduzida |
| **Posicao no cap** | Segunda quest. Assume conclusao de Q1-01. |

---

## PRE-REQUISITOS

Q1-01 concluida. Ze tem Dona Marta como NPC aliada desde o fechamento da quest anterior.

---

## SETUP NARRATIVO DE ABERTURA

*Ze e Dona Marta na entrada nordeste da Esplanada dos Ministerios. A nevoa verde e densa mas nao opaca. Da pra ver o Congresso ao fundo. Da pra ver que ha corpos se movendo entre os ministerios.*

> **DONA MARTA:** "A cantina do Congresso fica no subsolo do Anexo II. Tem um tunel de servico que sai daquela manutencao ali." *(aponta para um edificio de manutencao a direita, entre dois blocos ministeriais)* "Eu usei ele essa manha."
> **ZE:** "Tem zumbi la?"
> **DONA MARTA:** "Obviamente. Mas eu conheo cada corredor desse lugar. Trinta e sete anos. Eu passo. A questao e voce."
> **ZE:** "E se eu ficar juntinho da senhora?"
> **DONA MARTA:** "Se voce ficar juntinho de mim voce vai morrer igual a crianca que fica no pe da mae no supermercado. Fique atras de mim. E se eu falar 'agacha', voce agacha."

*Titulo da wave aparece:*

**"WAVE: O CORREDOR DE TUBA"**
*(Subtitulo em fonte menor: "Tuba = Tecnico Universitario de Brasilia Area. Nao confundir com instrumento.")*

---

## OBJETIVO DO JOGADOR

Ze e Dona Marta devem atravessar o corredor de servico entre os blocos ministeriais e chegar ao tunel subterraneo de acesso ao Congresso, sem que Dona Marta tome dano suficiente para ser incapacitada (a aliada tem barra de HP propria).

**Condicao secundaria opcional:** Passar pelo trecho da Sala de Imprensa sem ativar o alarme (bonus de pontuacao).

---

## LOCALIZACAO

**Corredor externo entre Bloco K e Bloco L dos Ministerios + Edificio de Manutencao M-01**
Esplanada dos Ministerios, setor norte — Brasilia, DF

**Estrutura do nivel:**

```
[INICIO]                                                        [SAIDA]
Ze+Marta     Passarela    Sala de      Deposito     Acesso ao
na entrada -> coberta   -> Imprensa  -> de Grafica -> Tunel M-01
             (PM-Zumbis   (stealth    (Black Blocs   (mini-horda
              em formacao) avancado)   aparecem)      de fechamento)
```

**Plataformas:**
- Topo dos veiculos de reportagem abandonados (passarela coberta)
- Janelas abertas do segundo andar (atalho opcional que evita metade dos PMs)
- Paletes de papel no deposito de grafica (proteção fisica, pode ser empurrada)

---

## INIMIGOS PRESENTES

### PM-Zumbi (INTRODUCAO — novo inimigo desta quest)

**Visual:** Farda da Policia Militar do DF — azul escuro, escudo transparente de proteção antimanifestacao na frente, capacete com viseira, cassetete na mao direita. Olhos verdes visíveis pela viseira.

**HP:** 6 hits totais (3 hits no escudo para quebrar + 3 hits no corpo)
**Velocidade:** Media (60px/s)

**Comportamento:**
- Avanca em formacao de dois, um atras do outro. O da frente segura o escudo. O de tras golpeia por cima do ombro do primeiro.
- O escudo absorve todos os ataques frontais. **Frontalmente e invulneravel.**
- Pontos fracos: costas (vulneravel ao ataque pelas costas), topo da cabeca (vulneravel a pulo no topo + ataque descendente), ou flancos quando o escudo quebra.
- Quando o escudo quebra (3 hits), o PM-Zumbi fica confuso por 1.5 segundos (janela de ataque garantida).

**Como o jogo ensina a vulnerabilidade:**
- O primeiro PM-Zumbi aparece sozinho, bloqueando o caminho, escudo na frente.
- Ze ataca de frente: o escudo absorve e Ze leva contragolpe leve (1 de dano).
- Dona Marta comenta: *(sem quebrar o fluxo do jogo, como dialogo flutuante)* "Pelo lado, meu filho. Eu passo trinta e sete anos passando pano nas costas deles."
- Ha uma plataforma (teto do veiculo de reportagem) que permite Ze subir e atacar pelo topo. Ou contornar pelo fundo.
- O jogo nunca diz explicitamente qual e o caminho certo.

**Quantidades por segmento:**
- Passarela coberta: 2 PMs em formacao, 1 solo
- Sala de Imprensa: 1 PM em patrulha (pode ser evitado com stealth)
- Mini-horda de fechamento: 3 PMs + 2 Burocratas misturados

---

### Black Bloc-Zumbi (INTRODUCAO — segundo novo inimigo desta quest)

**Visual:** Roupa preta, capuz, mascara de gás artesanal (pano molhado amarrado no rosto), pedra na mao esquerda, coquetel molotov na mao direita (variante avancada, apenas no deposito de grafica).

**HP:** 4 hits
**Velocidade:** Alta (90px/s, mais rapido que qualquer inimigo visto ate agora)

**Comportamento:**
- Nao avanca em linha reta. Zig-zag horizontal, dificultando acerto.
- Arremessa pedras: projetil rasteiro (altura do torso) com alcance de meia tela. Jogador deve pular ou se agachar para desviar.
- Variante com coquetel: ao morrer, explode em area pequena de fogo por 2 segundos. Jogador aprende a nao ficar em cima do Black Bloc ao matar.

**Como o jogo ensina o projetil:**
- O primeiro Black Bloc aparece a distancia, do outro lado do deposito, e arremessa uma pedra ANTES de avancar. Ze leva a pedra se nao desviar.
- Se Ze levar a pedra (provavelmente vai na primeira vez), Dona Marta diz: "Pula quando ver o braco levantar."
- Se Ze desviar, Dona Marta diz: "Isso. Reflexo de servidor publico. Ja desvia de proposta de melhoria a distancia."

**Quantidades:**
- Deposito de grafica: 3 Black Blocs basicos + 1 variante com coquetel
- Nenhum Black Bloc aparece antes do deposito (inimigo e completamente novo aqui)

---

## MECANICAS DE GAMEPLAY INTRODUZIDAS

### 1. NPC aliada com HP propria (Dona Marta como acompanhante)

**Como funciona:**
- Dona Marta tem barra de HP propria visivel no HUD (canto superior direito, menor que a de Ze).
- Ela ataca automaticamente qualquer inimigo a menos de 150px dela, com a vassoura (dano 1 por hit, velocidade de ataque moderada).
- Ela NAO segue Ze automaticamente em plataformas altas. Ze precisa tomar rotas de chao para mante-la junto.
- Se Dona Marta chega a 0 HP, ela cai, Ze a carrega (velocidade reduzida em 40%) e precisa chegar ao proximo checkpoint para ela "descansar e recuperar".

**Momento de aprendizado:** A primeira vez que Dona Marta toma dano, Ze exclama "Cuidado, Dona Marta!" e o jogador percebe que ela nao e imortal. Isso cria tensao genuina — Ze e mais forte com ela do que sem ela, mas protege-la e uma responsabilidade.

**Por que importa:** Este e o primeiro exemplo de mecanica de "proteger aliado" do jogo. Treina o jogador para situacoes analogas em Capitulos futuros (escoltas de NPCs civis, dilemas morais de salvar/abandonar).

### 2. Agachamento como esquiva de projetil

**Como funciona:**
- Ze pode agachar (baixo no controle). Agachado, ele nao se move horizontalmente mas ocupa metade da altura vertical.
- Pedras arremessadas pelo Black Bloc passam por cima do Ze agachado.
- Cassetete do PM-Zumbi e um ataque rasante (passa por baixo do Ze se ele pular).

**Momento de aprendizado:** Ze leva a primeira pedra do Black Bloc no deposito de grafica. Apos isso, o proximo Black Bloc e introduzido a distancia, dando tempo para o jogador testar a esquiva.

### 3. Quebrando o escudo do PM com pulo descendente

**Como funciona:**
- Se Ze pula e esta diretamente acima do PM-Zumbi, o ataque durante a descida ignora o escudo e aplica dano direto.
- O escudo bloqueia ataques horizontais, nao verticais.

**Momento de aprendizado:** A plataforma do veiculo de reportagem esta exatamente na altura certa para o jogador pular e cair sobre o PM. O nivel e construido para sugerir esse caminho sem forcá-lo.

---

## ITENS COLETAVEIS / ARMAS INTRODUZIDAS

| Item | Local | Efeito | Nota |
|---|---|---|---|
| Escudo Quebrado (drop PM) | Passarela coberta | Equipa como item de defesa passiva — absorve 1 hit antes de quebrar | Nao recomendado pegar se Ze ja tem vassoura (sem equipamento duplo no MVP) |
| Spray de Pimenta Institucional | Sala de Imprensa (gaveta aberta) | Projetil de curto alcance, dano 1, cega inimigo por 2s | Primeira arma ranged do jogo (limitada, 5 usos) |
| Relatorio Sigiloso | Deposito de grafica (caixa) | Item narrativo — ao inspecionar, exibe texto satirico sobre gastos de seguranca publica | Nenhum efeito de gameplay |
| Agua Mineral da Cantina | Drop do ultimo Black Bloc | Restaura 30% HP | Maior heal disponivel ate agora |

**Nota sobre o Spray de Pimenta:** Esta e a introducao silenciosa do ataque ranged. O item tem apenas 5 usos, entao o jogador e encorajado a experimentar sem se tornar dependente. O Spray e apresentado como solucao opcional para a Sala de Imprensa (pode usar para cegar o PM em patrulha e passar sem combate), ensinando o conceito de "arma certa para a situacao".

---

## CONDICAO DE SUCESSO

Ze e Dona Marta chegam ao Tunel M-01 (escada metalica descendo para o subsolo). Dona Marta deve ter pelo menos 1 ponto de HP.

*Animacao de sucesso:* Ze abre a escotilha da escada. Ela range. Os dois descem. Ze fecha a escotilha acima da cabeca. Silencio relativo. A nevoa verde esta acima, nao abaixo.

> **ZE:** "Subterraneo. Certeza que tem caminho ate la?"
> **DONA MARTA:** "Certeza absoluta. Esse tunel foi construido em 1966 pelo pessoal que queria sair do Congresso sem ser visto. Nunca foi para entrar."
> **ZE:** "Quem construiu?"
> **DONA MARTA:** "Os politicos que votaram a reforma constitucional de 66. Mas isso e historia."

---

## CONDICAO DE FALHA

- Ze chega a 0 HP, OU
- Dona Marta chega a 0 HP sem Ze estar no raio de carregamento (Ze abandona Dona Marta), OU
- Alarme da Sala de Imprensa e ativado E Ze nao consegue liquidar os PMs adicionais convocados em tempo (5 PMs extras em 20 segundos)

**Tela de Game Over especifica:**
Se Ze morre: Ze cai e um PM-Zumbi bate um carimbo de "AUTUADO" na testa de Ze.
Se Dona Marta e abandonada: Ze chega ao tunel, fecha a escotilha, olha para baixo — e nada. A camera recua. Ze esta sozinho. Texto: *"Voce esqueceu alguem. Tente de novo."*

**Checkpoint:** Inicio do deposito de grafica (antes dos Black Blocs).

---

## RECOMPENSAS

**Narrativa:**
- Ze e Dona Marta estao no tunel subterraneo. Dona Marta conta, enquanto caminham, sobre os 37 anos de servico, os governos que viu passar, os escândalos que limpou literalmente.
- Ao final do tunel, uma luz — e vozes. Vozes que nao sao de zumbi. Sao de mais de uma pessoa. Ze e Dona Marta chegam a uma camara subterranea onde ha um grupo de sobreviventes: um vereador (personagem politico com sotaque), dois estudantes universitarios, e um homem de terno que nao se apresenta.

**Gameplay:**
- Desbloqueio: PM-Zumbi e Black Bloc-Zumbi adicionados ao Bestiario
- Se jogador completou a Sala de Imprensa sem ativar alarme: conquista **"Invisivel ao Sistema"** (+300 pontos, badge)
- Spray de Pimenta Institucional permanece no inventario (com os usos restantes)

---

## SETUP NARRATIVO DE FECHAMENTO

*Na camara subterranea. Um grupo de sobreviventes. O homem de terno se apresenta:*

> **WALDECO:** "Deputado Federal Waldeco Pereira, PL de Taguatinga. Estou aqui ha duas horas. Quem e voce?"
> **ZE:** "Ze. Servidor publico. Ministerio do Planejamento."
> **WALDECO:** *(anotando algo no celular)* "Ze. Servidor publico. Potencial eleitor. Excelente."
> **DONA MARTA:** "Ele quer saber se a minha filha esta la em cima."
> **WALDECO:** "Ah, a cantina. Sim, tem gente la. Eu precisava ir la buscar alguem tambem, por coincidencia."

*Ze e Dona Marta trocam um olhar.*

> **ZE (baixinho para Dona Marta):** "Por que eu nao confio nesse homem?"
> **DONA MARTA (baixinho):** "Porque voce e inteligente, meu filho."

*Fade out.*

**PROXIMO: Q1-03 — A ALIANCA DA VASSOURA** *(Waldeco se junta ao grupo)*

---

## OBSERVACOES DE ARTE E AUDIO

**Background do nivel:**
- Passarela coberta: ceu azul claro visivel por cima. Ministerios ao fundo. Carros de TV capotados ou abandonados, logos das emissoras visiveis (emissoras ficticias: "TV BRASILIA URGENTE", "CANAL PATRIOTA", "GBN — GLOBO BRASILIA NOTICIAS"). Camaras de TV tombadas no chao.
- Sala de Imprensa: telas mostrando transmissoes ao vivo (congeladas no momento da invasao). Uma tela exibe um placar de "CHAMADA URGENTE: INVASAO DOS TRES PODERES". Outra tela exibe uma novela das 21h normalmente.
- Deposito de grafica: caixas de papel, maquinas de impressao velhas, santinhos de campanhas passadas espalhados no chao como folhas caidas.

**Audio:**
- Musica ambiente: batucada de fanfarra de manifestacao (como se viesse de fora, distante) misturada com eco metalico dos corredores.
- Ao entrar no tunel: silencio total por 3 segundos antes da musica subterranea comecar (tom mais sombrio, mas nao de terror — de suspense discreto).
- Som de impacto do Spray de Pimenta: som de spray de cozinha + gemido de PM confuso.
- Morte do Black Bloc com coquetel: som de estalo + grito curto + WHOOSH do fogo. O fogo deve ser visualmente satisfatorio mas nao excessivo (restricao de engine — Phaser Arcade Physics, sem fisica de fluido real).

**Animacao especifica:**
- Dona Marta atacando com a vassoura tem animacao diferente de Ze: ela faz varredura lateral (sweep) de baixo para cima, como quem varre o chao. Mais lento que Ze mas com area maior.
- PM-Zumbi com escudo quebrado: ao perder o escudo, a animacao e o PM olhando para o escudo partido com expressao confusa, gemendo "...regulamento... procedimento..." antes de reorientar o ataque.
