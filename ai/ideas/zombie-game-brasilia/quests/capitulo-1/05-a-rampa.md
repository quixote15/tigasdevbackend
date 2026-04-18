# Q1-05 — A RAMPA
### Quest Design Document | Capitulo 1 | Modo Cidadao + Politico (Variacao)

---

## IDENTIDADE

| Campo | Valor |
|---|---|
| **ID** | Q1-05 |
| **Titulo** | A Rampa |
| **Modo** | Ambos, com variacao de objetivo e dialogo |
| **Duracao estimada** | 5-7 minutos |
| **Dificuldade** | 3/5 — Maior concentracao de inimigos ate agora, ataque ranged introduzido obrigatoriamente |
| **Posicao no cap** | Penultima quest. Imediatamente antes do boss fight. |

---

## PRE-REQUISITOS

Q1-03 concluida. Todo o grupo esta junto: Ze (ou Waldeco como protagonista), Dona Marta, Luciana, e o NPC do outro protagonista.

---

## SETUP NARRATIVO DE ABERTURA

*O elevador de servico se abre. Luz do dia. A Esplanada dos Ministerios, exterior. A Praca dos Tres Poderes visivel ao fundo — distante, mas grande. A rampa do Palacio do Planalto no centro da composicao visual, com figuras cambalendo descendo dela.*

**VERSAO CIDADAO:**

> **ZE:** "A saida do Congresso e do outro lado dessa Praca."
> **DONA MARTA:** *(olhando para a Rampa)* "Meu filho, essa rampa... isso sao os que entraram no STF. Saindo. Mas saindo diferentes."
> **ZE:** "A gente precisa atravessar isso."
> **WALDECO:** *(ja digitando no celular)* "Eu sei um caminho. Ha tres blocos de ministerios entre nos e a saida. Mas ha um atalho: pelo Espelho D'Agua, do lado do Congresso. Menos exposto."
> **ZE:** "O senhor conhece o Espelho D'Agua?"
> **WALDECO:** "Eu me vejo nele todo dia quando venho trabalhar."

**VERSAO POLITICO:**

> **WALDECO:** "La esta. A Rampa. Se eu chegar la — ao topo daquela rampa — e aparecer nas cameras da TV ao VIVO... eu existo. Eu sou o deputado que sobreviveu ao 8 de Janeiro."
> **ZE:** "A gente nao deveria estar tentando sair da Praca?"
> **WALDECO:** "Saimos depois. Primeiro, eu preciso aparecer la em cima."
> **DONA MARTA:** "Voce e absolutamente insano."
> **WALDECO:** "Eu sou politico. A semantica e diferente."

*A diferenca de objetivo entre os modos e narrativa, nao mecanica: Ze quer atravessar a Praca para sair pela saida norte. Waldeco quer subir a Rampa para aparecer nas cameras antes de sair. O percurso e o mesmo — a destino final antes do boss e diferente (saida norte vs. topo da rampa). O boss aparece no mesmo lugar para os dois.*

---

## OBJETIVO DO JOGADOR

**Modo Cidadao:** Atravessar a Praca dos Tres Poderes usando o Espelho D'Agua como cobertura e chegar a saida norte (portao externo do Congresso).

**Modo Politico:** Atravessar a Praca dos Tres Poderes e subir a Rampa do Planalto para chegar ao ponto mais visivel (topo da rampa, cameras de TV).

**Objetivo comum aos dois modos:** Sobreviver a HORDA ABERTA da Praca — o maior numero de inimigos ao mesmo tempo ate este ponto do jogo.

---

## LOCALIZACAO

**Praca dos Tres Poderes**
Brasilia, DF — o coração do governo federal

**Estrutura do nivel:**

```
[INICIO]                                                    [SAIDA]
Saida do    Trecho        Espelho     Trecho       Rampa do
elevador -> aberto da  -> D'Agua   -> exposto   -> Planalto
            Esplanada    (cobertura, (Black Blocs  [ou Portao
           (Patriotas)   plataformas) + PMs)        Norte para
                                                    Cidadao]
```

**Elemento visual central:** O Congresso agora domina o background inteiro. O Supremo Tribunal Federal visivel a esquerda. O Palacio do Planalto a direita. O jogador esta literalmente no meio dos Tres Poderes. Isso deve ser visualmente esmagador — o maior cenario do Capitulo 1.

**Espelho D'Agua:**
- Agua rasa (nao toxico aqui, diferente do tunel) — Ze pode caminhar dentro mas com velocidade reduzida em 20%.
- Oferece cobertura visual baixa (agachado no Espelho = invisivel para Patriotas que estao na borda, visiveis para Black Blocs que estao em posicao elevada).
- Plataformas: bordas do Espelho (nao entrar na agua), postes de iluminacao tombados sobre o Espelho.

**Rampa do Planalto:**
- Segmento final do nivel antes do boss.
- Inclinada (45 graus em perspectiva side-scroller): Ze/Waldeco sobem mais devagar.
- Inimigos descendo a rampa tem velocidade aumentada em 30% (fisica da gravidade exagerada para efeito comico-horrifico).
- No topo: cameras de TV ao vivo, abandonadas. Waldeco PODE entrar no frame — isso dispara um efeito de Popularidade (+10).

---

## INIMIGOS PRESENTES

### Patriota-Zumbi (retorno) — Praca aberta

A maior concentracao de Patriotas do jogo ate agora: hordas de 8-12 em sequencia, com 5 segundos de intervalo entre grupos. O trecho aberto da Esplanada e literalmente uma corrida pelo fogo aberto.

**Variante nova: Patriota com Bandeirão**
- Visual identico ao Patriota comum, mas carrega um bandeirão do Brasil (2x maior que o corpo) como escudo frontal improvisado.
- O bandeirão absorve 2 hits antes de rasgar.
- Ao rasgar o bandeirão, o Patriota fica confuso por 2 segundos (gemendo "a bandeira... a bandeira...").
- Mecanica de aprendizado: o jogador precisa dar 2 hits frontais ou 1 hit por tras (sem o bandeirão bloqueando).

### Black Bloc-Zumbi (retorno) — Trecho exposto

Black Blocs em posicao elevada (sobre os gradis e monumentos da Praca), arremessando pedras de cima para baixo. Este e o primeiro momento em que o jogador enfrenta projeteis vindos de ACIMA, nao da lateral.

**O problema:** A solucao natural (pular) nao funciona aqui porque os Black Blocs estao alto demais. A solucao e o ataque RANGED — a primeira vez que o jogo FORCE o jogador a usar um projetil.

**Como o jogo forca o uso de ranged:**
- Na entrada do trecho exposto, ha uma caixa brilhando no chao: **Sinalizador de Fumaca** (5 usos, dano 3 de area, alcance medio).
- O primeiro Black Bloc elevado esta numa posicao que so pode ser atingido com o Sinalizador (alto demais para corpo-a-corpo, nenhuma plataforma que leve ate ele).
- Dona Marta: "Tem que acertar de longe, meu filho. Ha trinta e sete anos eu sei que ha problemas que nao se resolve chegando perto."
- O jogador usa o Sinalizador. O Black Bloc cai. O jogo confirma a mecanica.

### PM-Zumbi em formacao (retorno) — Trecho exposto e Rampa

PMs em formacao de 3, bloqueando o acesso ao Espelho D'Agua e, depois, bloqueando a rampa. Os jogadores ja sabem como lidar com eles (flanquear ou atacar por cima).

**Variante nova: PM com Escudo Reforçado**
- O escudo absorve 5 hits em vez de 3.
- Vulnerabilidade por cima permanece.
- Introducao implicita: o jogador ja sabe atacar PM por cima, mas agora precisa ser mais preciso.

---

## MECANICAS DE GAMEPLAY INTRODUZIDAS

### 1. Ataque ranged obrigatorio (Sinalizador de Fumaca)

**Como funciona:**
- Item no inventario, slot separado (botao B ou tecla E no teclado, indicador no HUD).
- Waldeco/Ze lanca o sinalizador em arco. Trajetoria parabolica.
- Ao impacto: explosao de fumaca colorida (verde-amarela para ironia), dano de area em raio de 60px, dura 2 segundos.
- Inimigos no raio tomam dano continuo (1 por segundo) e ficam desorientados.
- 5 usos totais nesta quest. Recarregavel com drop de inimigo (20% de chance).

**Por que e obrigatorio aqui:** O design do nivel torna o ranged necessario para os Black Blocs elevados. O jogador descobre que tem a ferramenta certa no momento em que mais precisa. Esse e o momento de "aha!" desta quest.

### 2. Gerenciamento de grupo em espaco aberto

Com Dona Marta, Luciana e o NPC do outro protagonista, o grupo de 4 precisar atravessar espaco aberto. Dona Marta combate automaticamente. Luciana NAO combate (ela carrega suprimentos — se ela morrer, Ze/Waldeco perdem acesso a heals ate o proximo checkpoint). O NPC do outro protagonista combate moderadamente.

**Tensao de design:** O jogador tem que dividir atencao entre combater e garantir que Luciana (o NPC mais fragil) nao leve hits acidentais das pedras dos Black Blocs.

**Momento de decisao:** Na metade do trecho exposto, Luciana esta em posicao exposta enquanto dois Black Blocs arremessam de cima. Ze/Waldeco precisam eliminar os Black Blocs ANTES de avancar para que Luciana passe. Isso premia planejamento, nao apenas reflexo.

### 3. Inclinacao da rampa (fisica de plataformas)

A Rampa do Planalto tem angulo de 45 graus. Regras:
- Subida: velocidade reduzida em 20%, salto alcanca menos distancia horizontal
- Descida: velocidade aumentada em 15%, inercia empurra para baixo
- Inimigos descendo: mais rapidos e perigosos
- Inimigos subindo: mais lentos, mais faceis de eliminar

Esta e a unica rampa do Capitulo 1. E introducao de fisica inclinada para o restante do jogo.

---

## ITENS COLETAVEIS / ARMAS INTRODUZIDAS

| Item | Local | Efeito | Nota |
|---|---|---|---|
| Sinalizador de Fumaca (x5) | Caixa no trecho exposto | Ranged, dano de area, desorientacao | Arma ranged principal desta quest |
| Capacete de PM (drop) | Drop de PM | Reduz proximo dano recebido em 50% (1 uso) | Primeiro item defensivo equipavel |
| Sanduiche Tupperware | Luciana distribui no Espelho D'Agua | Restaura 40% HP (unico heal desta quest) | Luciana distribui automaticamente se Ze/Waldeco estiver abaixo de 30% HP |
| Camera de TV (item narrativo) | Topo da rampa | Waldeco: +20 Popularidade ao interagir. Ze: dialogo satirico. | Recompensa diferente por modo |

---

## CONDICAO DE SUCESSO

**Modo Cidadao:** Ze e o grupo chegam ao portao norte do Congresso. O portao esta fechado — mas do outro lado, a sombra de uma figura grande e visivel. Uma figura que nao parece um zumbi comum.

**Modo Politico:** Waldeco chega ao topo da Rampa. As cameras de TV ao vivo estao ligadas. Waldeco aparece na transmissao por 5 segundos antes de ver, do alto, a figura que bloqueia o caminho de volta.

**Ambos os modos:** A mesma figura aparece. O General de Pijama esta aqui. E ele trouxe amigos.

---

## CONDICAO DE FALHA

- Protagonista chega a 0 HP, OU
- Luciana morre (grupo perde todos os heals restantes e o jogo indica que Ze/Waldeco esta sozinho para o boss fight — ainda completavel, mas mais difícil)

**Tela de Game Over:**
Waldeco/Ze caem no meio da Praca. A camera se afasta lentamente mostrando a Praca inteira. Os Tres Poderes ao fundo. O sol de janeiro. Inimigos caminhando por tudo.
Texto: *"A Praca pertence a eles agora. Tente de novo."*

**Checkpoint:** Saida do Espelho D'Agua (antes do trecho exposto).

---

## RECOMPENSAS

**Narrativa:**
- O grupo chega ao ponto de confronto. Dona Marta reconhece o General de Pijama: "Eu conheo esse homem. Ele ficou seis meses acampado aqui do lado. Ele trouxe uma marmita de frango toda semana. Agora olha ele."

**Gameplay:**
- Desbloqueio: Patriota com Bandeirão e PM com Escudo Reforçado adicionados ao Bestiario
- Sinalizadores de Fumaca restantes carregam para o boss fight
- Se Luciana sobreviveu: ela fornece 1 kit de primeiros socorros antes do boss fight (50% HP restore)
- Se Waldeco usou camera de TV: conquista **"Em Cadeia Nacional"** (Popularidade +20 permanente para Capitulo 2)

---

## SETUP NARRATIVO DE FECHAMENTO

*O grupo para. A frente do Congresso. O General de Pijama e imponente — maior que um zumbi normal, lento, mas com o celular na mao exibindo o mapa de todos os grupos de WhatsApp que ele administra.*

**VERSAO CIDADAO:**

> **GENERAL (sem ver Ze ainda):** "...CAVALARIA VEM... CONFIEM NO PLANO..."
> **DONA MARTA:** *(sussurrando)* "Ze. Aquele homem controlou metade dos grupos de Telegram do acampamento. Ele foi quem organizou a marcha."
> **ZE:** "E agora ele e zumbi."
> **DONA MARTA:** "A diferenca foi pequena."

**VERSAO POLITICO:**

> **GENERAL (vendo Waldeco no topo da rampa):** "DEPUTADO! Voce veio nos libertar!"
> **WALDECO:** "Eu vim fazer campanha. Libertar e efeito colateral."
> **GENERAL:** *(pausa. Processa. Ruge.)*

*O General levanta o celular. Audio de corneta. Patriotas-Zumbi ao redor se juntam. A fase do boss comeca.*

**PROXIMO: Q1-06 — O GENERAL DE PIJAMA**

---

## OBSERVACOES DE ARTE E AUDIO

**Background do nivel:**
- A Praca dos Tres Poderes deve ser o cenario mais impressionante do Capitulo 1. O Congresso (dois semicirculos, cupula) ao fundo. O Supremo a esquerda. O Planalto a direita. O Espelho D'Agua no centro, refletindo tudo de forma distorcida (efeito de agua com shader basico ou sprite animado).
- O ceu ainda e azul claro de janeiro, mas a nevoa verde e agora visivel nas extremidades da tela, chegando do horizonte.
- Debris da invasao: cadeiras do Congresso jogadas pelas janelas e visiveis no gramado. Grades tombadas. Vitrine quebrada. Um piano de cauda no gramado (ninguem explica o piano — e so absurdo brasileiro).
- Cameras de TV abandonadas no topo da rampa: logotipos ficticios visiveis, transmissao ao vivo ainda ativa (luz vermelha piscando).

**Audio:**
- Musica da Praca: orquestra sinfonicas distorcida, como se o "Hino Nacional" estivesse sendo regido por alguem que nunca ouviu a partitura original. Cresce em volume ao aproximar da rampa.
- Espelho D'Agua: splash sonoro ao entrar na agua. Echo diferente enquanto dentro.
- Black Blocs elevados: som de pedra cortando o ar antes de atingir. Aviso audio antes do impacto — o jogador treinado vai aprender a reagir ao som antes de ver a pedra.
- Ao chegar ao topo da rampa: o vento. O som da cidade ao longe. E o silencio de um momento que historicamente importou. 3 segundos sem musica. Depois, a corneta do General.
