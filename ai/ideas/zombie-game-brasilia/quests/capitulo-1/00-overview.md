# CAPITULO 1 — OVERVIEW
## "O Dia Que o Chao Abriu" / "O Oportunista no Acampamento"
### Zumbis de Brasilia | Quest Design Document | Abril 2026

---

## 1. RESUMO NARRATIVO

**Evento real:** 8 de janeiro de 2023. Invasao dos Tres Poderes.

O Capitulo 1 cobre o mesmo evento a partir de duas perspectivas irreconciliaveis — e essa tensao e o coração do replay.

**Perspectiva Cidadao (Ze):**
Ze esta fazendo hora extra no Ministerio do Planejamento por causa do ar-condicionado quando a invasao comeca. Nao e heroi. Nao e patriota. E um servidor publico tentando nao morrer. A nevoa verde sobe do chao quando os invasores entram no STF e a Esplanada se transforma num campo de batalha zumbi. Ze foge para dentro do Congresso, atravessa os corredores com Dona Marta (faxineira, 62 anos, vassoura como arma), e precisa chegar a saida do Anexo II antes que o General de Pijama feche todos os corredores.

**Perspectiva Politico (Waldeco):**
Waldeco esta no acampamento do QG distribuindo santinho — nao por idealismo, por estrategia eleitoral. Quando a nevoa chega e o caos explode, ele enxerga oportunidade: ser o unico politico vivo filmando no meio do apocalipse. O mesmo mapa, os mesmos inimigos, mas o objetivo de Waldeco nao e sobreviver. E capitalizar.

**Ponto de convergencia:** Os dois protagonistas enfrentam o mesmo boss (General de Pijama) no mesmo lugar (Praca dos Tres Poderes), com dialogos diferentes e recompensas diferentes. Isso e deliberado: o jogador que jogar os dois modos vai reconhecer o momento e sorrir.

---

## 2. LISTA DE QUESTS

| # | Arquivo | Titulo | Modo | Duracao estimada |
|---|---|---|---|---|
| Q1-01 | `01-hora-extra.md` | Hora Extra no Apocalipse | Cidadao | 5-7 min |
| Q1-02 | `02-corredor-dos-mortos.md` | Corredor dos Mortos | Cidadao | 4-6 min |
| Q1-03 | `03-alianca-da-vassoura.md` | A Alianca da Vassoura | Cidadao + Politico | 3-5 min |
| Q1-04 | `04-santinho-no-caos.md` | Santinho no Caos | Politico | 5-7 min |
| Q1-05 | `05-a-rampa.md` | A Rampa | Ambos (variacao) | 5-7 min |
| Q1-06 | `06-general-de-pijama.md` | O General de Pijama | Ambos (boss fight) | 6-8 min |

**Total estimado por run:** 28-40 minutos (uma perspectiva completa)
**Total com as duas perspectivas:** 56-80 minutos (o Capitulo 1 completo)

---

## 3. FLUXOGRAMA DE PROGRESSAO

```
[PROLOGO — Cutscene]
        |
        v
  [Modo selecionado?]
      /       \
CIDADAO     POLITICO
    |             |
  Q1-01         Q1-04
(Hora Extra)  (Santinho
               no Caos)
    |             |
  Q1-02           |
(Corredor)        |
    |             |
    +-----> Q1-03 <----+
         (Alianca da
          Vassoura)
               |
               v
             Q1-05
           (A Rampa)
        [variacao por modo]
               |
               v
             Q1-06
         (General de
          Pijama)
        [boss + dialogo
         por modo]
               |
               v
        [Cutscene final]
        "A nevoa se espalha"
               |
               v
         [FIM CAP 1]
    Desbloqueia Capitulo 2
```

**Estrutura:** Ramificada nos primeiros atos, convergente no climax. O jogador que escolhe Cidadao vive Q1-01 e Q1-02 antes de encontrar Waldeco em Q1-03. O jogador que escolhe Politico vai direto para Q1-04 e encontra Ze em Q1-03. A convergencia em Q1-03 e o momento que revela que os dois protagonistas existem no mesmo mundo.

---

## 4. OBJETIVOS DE APRENDIZADO — TUTORIAL DISFARÇADO

O Capitulo 1 e um tutorial completo. Nenhuma tela de "Como Jogar" deve existir. Cada quest introduz exatamente uma mecanica nova e nao mais que uma.

| Quest | Mecanica introduzida | Como e ensinada |
|---|---|---|
| Q1-01 | Movimento horizontal + pulo basico | Primeiro inimigo (Burocrata-Zumbi) bloqueia o corredor. Pular e a unica saida. |
| Q1-01 | Ataque corpo-a-corpo | Vassoura encontrada no primeiro quarto do nivel. Tutorial implicito: item brilhante no chao. |
| Q1-02 | Inimigo com escudo frontal (PM-Zumbi) | Impossivel de atacar de frente. O cenario tem plataforma atras do inimigo para contornar. |
| Q1-02 | Stealth / agachamento | Burocrata-Zumbi nao ve jogador agachado sob mesa. |
| Q1-03 | NPC aliado seguindo o jogador | Dona Marta segue e ataca automaticamente. Jogador aprende a proteger NPC. |
| Q1-04 | Sistema de Popularidade (Politico) | Primeiro dilema moral aparece com consequencia imediata e visivel. |
| Q1-04 | Recrutar civil como aliado temporario | Primeiro civil recrutavel aparece em area segura, facil de recrutar. |
| Q1-05 | Projeteis e esquiva por salto | Black Bloc-Zumbi arremessa pedras. Plataformas ajudam a demonstrar esquiva vertical. |
| Q1-05 | Ataque ranged (arma de longo alcance) | Primeiro arma ranged aparece como drop obrigatorio no meio do nivel. |
| Q1-06 | Boss com tres fases e padroes | Cada ataque do General e telegrafado com audio + animacao antes de executar. |

**Principio:** O jogador nunca deve morrer sem entender por que morreu. Cada inimigo novo aparece primeiro sozinho ou em dupla, nunca em horda. A horda vem depois que o jogador ja demonstrou que entendeu o inimigo.

---

## 5. METRICAS DE SUCESSO

### Tempo
- **Meta de conclusao por run (1 modo):** 30-40 minutos
- **Alerta de design:** Se o playtest mostrar media acima de 45 min, remover uma wave ou reduzir HP de inimigos comuns. Cap 1 deve ser prazeroso, nao cansativo.
- **Alerta de design:** Se a media for abaixo de 20 min, o boss esta fraco ou faltam waves nos niveis intermediarios.

### Engajamento
- **Taxa de replay (Cidadao -> Politico ou vice-versa):** Meta de 40% dos jogadores que completam um modo tentam o outro dentro da mesma sessao. Indicador principal de que a narrativa dual funcionou.
- **Drop-off por quest:** Nenhuma quest individual deve ter taxa de abandono acima de 15%. Se Q1-01 perder mais de 15%, o onboarding esta quebrado.
- **Taxa de completude do Cap 1:** Meta de 70% dos jogadores que comecar Q1-01 chegam ao fim de Q1-06.

### Momentos "wow" (qualitativos, medidos em sessoes de playtest)
- Q1-01: Jogador ri ao ler o dialogo do Burocrata-Zumbi ("protocolo... carimba aqui..."). Objetivo: 80% de reacao visivel.
- Q1-03: Jogador percebe que Waldeco e Ze estao no mesmo evento. Objetivo: expressao de reconhecimento observada.
- Q1-06: Jogador ri ao ouvir "BOM DIA GRUPO!" na morte do General. Objetivo: 90% de reacao.

### Viralidade
- O dialogo do General ("EU SERVI ESTE PAIS! Eu fui... fui... cabo reformado!") deve ser clipavel e postavel. O evento de morte do boss deve produzir um frame unico, shareavel, com o celular tocando o audio de WhatsApp.

---

## 6. NOTAS DE DESIGN GERAL

**Paleta e tom:** Todo o Capitulo 1 se passa na luz do dia de janeiro. Ceu claro, sol brasiliense, que contrasta com o verde toxico da nevoa. Essa dissonancia visual (dia ensolarado + apocalipse) e intencional e deve ser mantida em todos os backgrounds das quests.

**Audio:** Sem musica de horror. O Cap 1 usa MPB distorcida, batucada de fanfarra de manifestacao que vai desafinando progressivamente conforme a nevoa se espalha. O General usa corneta de WhatsApp como mecanica de gameplay, nao apenas de narrativa.

**Personagens auxiliares:** Dona Marta (Cidadao) e os Cabos Eleitorais (Politico) sao os tutores implicitos de cada modo. Eles verbalizam dicas como comentarios sarcasticos, nunca como instrucoes diretas. "Meu filho, esse PM nao cai pela frente, nao. Ha trinta anos eu passo pano nas costas deles" = dica de ataque por tras.
