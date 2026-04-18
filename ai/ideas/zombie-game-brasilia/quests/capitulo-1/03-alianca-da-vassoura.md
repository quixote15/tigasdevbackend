# Q1-03 — A ALIANCA DA VASSOURA
### Quest Design Document | Capitulo 1 | Modo Cidadao + Politico (Convergencia)

---

## IDENTIDADE

| Campo | Valor |
|---|---|
| **ID** | Q1-03 |
| **Titulo** | A Alianca da Vassoura |
| **Modo** | Ambos — Cidadao e Politico convergem aqui |
| **Duracao estimada** | 3-5 minutos |
| **Dificuldade** | 2/5 — Foco narrativo, combate moderado |
| **Posicao no cap** | Quest de convergencia. Cidadao chega apos Q1-02. Politico chega apos Q1-04. |

---

## PRE-REQUISITOS

- **Modo Cidadao:** Q1-02 concluida. Ze e Dona Marta acabaram de chegar ao tunel subterraneo e encontraram Waldeco.
- **Modo Politico:** Q1-04 concluida. Waldeco vem do acampamento do QG, desceu para o tunel fugindo da onda de Patriotas-Zumbi.

---

## SETUP NARRATIVO DE ABERTURA

**VERSAO CIDADAO:**

> **ZE (narracao):** "O tunel tinha cinco pessoas. Dois estudantes de direito da UnB, um vereador de Samambaia que nao parava de reclamar da falta de cobertura de TV, a Dona Marta — e esse sujeito de terno que ficava olhando o celular como se tivesse recebendo informacoes de inteligencia. Ficamos sabendo depois que era status do WhatsApp."

**VERSAO POLITICO:**

> **WALDECO (narracao):** "O tunel era a saida. Eu tinha entrado pelo acesso do QG — um tunel que nenhum civil conhece, eu descobri num grupo de Telegram em 2021. La dentro, tinha uma mulher com vassoura que parecia mais perigosa que qualquer zumbi que eu ja vi, e um cidadao com cara de quem nao dorme bem desde 2018. Nome: Ze. Servidor publico. Potencial base eleitoral."

*Os dois grupos se encontram na camara subterranea. O jogo exibe um split momentaneo: se o jogador chegou pelo Modo Cidadao, ve a cena pelo angulo de Ze. Se chegou pelo Modo Politico, ve pelo angulo de Waldeco. A cutscene e a mesma — so a camera e diferente.*

> **WALDECO:** "Deputado Waldeco Pereira. Estou feliz em ver sobreviventes. Precisamos organizar uma saida."
> **ZE:** "Organizar como? O senhor tem plano?"
> **WALDECO:** "Tenho. Mas preciso de voce para executar."
> **DONA MARTA:** *(sem olhar do celular)* "Ele quer dizer que ele tem o mapa e voce tem o corpo."
> **WALDECO:** "Eu diria que e uma parceria estrategica."

*A quest e iniciada: o grupo precisa sair do subsolo juntos.*

---

## OBJETIVO DO JOGADOR

O grupo deve atravessar o corredor de manutencao subterranea e chegar ao elevador de servico do Congresso (Anexo II, nivel -1), onde a filha de Dona Marta, Luciana, trabalha na cantina. O percurso tem inimigos, mas o foco desta quest e estabelecer a dinamica de grupo e o dilema de confianca entre Ze e Waldeco.

**Mecanica central desta quest:** Ze (Cidadao) e Waldeco (Politico) nao jogam juntos diretamente — voce so joga com um deles. Mas o NPC do personagem que voce nao esta jogando acompanha o grupo como aliado com comportamento diferente:

- Se voce esta jogando Ze, **Waldeco-NPC** fica atras do grupo e ocasionalmente "desaparece" por 10-15 segundos (vai "verificar o caminho" mas na verdade esta gravando um video dele mesmo nos tuneis para redes sociais). Volta com um aliado civil recrutado.
- Se voce esta jogando Waldeco, **Ze-NPC** e o que fica na linha de frente do combate enquanto Waldeco posiciona.

---

## LOCALIZACAO

**Tunel subterraneo entre Ministerios e Congresso**
Subsolo da Esplanada — corredor de manutencao, decadas sem reforma

**Estrutura do nivel:**

```
[INICIO]                                                    [SAIDA]
Camara de    Tunel de     Camara de    Corredor     Elevador
sobreviventes -> manutencao -> bombeamento -> da cantina -> de servico
(conversa)     (Burocratas)  (inundado,    (Patriotas    (boss prep)
                              plataformas)  emergem)
```

**Plataformas:**
- Tubos de agua e energia no teto da camara de bombeamento (pendurar + saltar)
- Caixas de material de construcao nunca utilizadas
- Passarelas de metal sobre area alagada (nivel de agua varia)

**Elemento ambiental especial:** A Camara de Bombeamento tem agua verde toxico no nivel do chao. Contato com a agua causa dano lento (1 HP por segundo). O nivel da agua sobe e desce em ciclo de 8 segundos, forcando o jogador a usar as passarelas e tubos. Este e o primeiro elemento de perigo ambiental do jogo.

---

## INIMIGOS PRESENTES

### Burocrata-Zumbi (retorno) — Tunel de manutencao

3 Burocratas no corredor estreito do tunel. Espaco exiguo. Nao da para contornar facilmente. O grupo e obrigado a passar por eles em ordem. Waldeco-NPC (se no Modo Cidadao) grita "Eu tenho imunidade parlamentar!" antes de se esconder atras de Ze.

### Patriota-Zumbi (INTRODUCAO — novo inimigo desta quest)

**Visual:** Camisa da selecao brasileira amarela, bandeira do Brasil amarrada no pescoco como capa, apito no peito. Olhos verdes. Expressao de quem ouviu uma fake news e acreditou completamente.

**HP:** 5 hits
**Velocidade:** Lenta (50px/s), mas vem em HORDA (grupos de 6-10)

**Comportamento:**
- Nao vem sozinho. Sempre em grupo. Se um Patriota-Zumbi ve o jogador, assobie com o apito, acordando todos os Patriotas na tela.
- O assobio tem delay de 1.5 segundos antes de acordar os outros. Janela para matar o primeiro antes do alarme.
- Avanca em linha reta gemendo "MINHA BANDEIRA JAMAIS SERA..." (sem terminar a frase).
- Ao morrer, a bandeira do Brasil que ele carrega cai no chao e vira item coletavel (nao tem efeito, mas Ze tem dialogo especifico ao pegar: "Respeito a bandeira. Nao respeito o que fizeram com ela.").

**Por que e introduzido aqui:** O Patriota e o inimigo de horda do jogo. Esta quest e a primeira com espaco aberto suficiente para uma horda funcionar. O corredor estreito anterior (Burocratas) prepara o contraste: Patriotas emergem num espaco mais aberto, o que e assustador.

**Quantidades:**
- Corredor da cantina: 2 grupos de 6, aparecem de portas laterais

---

## MECANICA EXCLUSIVA DESTA QUEST

### Conversa durante o combate (Waldeco x Ze)

Durante o combate no corredor da cantina, Waldeco e Ze dialogam enquanto lutam. O dialogo muda conforme o desempenho do jogador:

**Se Ze/Waldeco esta indo bem (menos de 30% HP perdido):**
> **WALDECO:** "Voce luta bem para ser servidor."
> **ZE:** "Voce foge bem para ser deputado."

**Se Ze/Waldeco esta com HP baixo:**
> **WALDECO:** "Ei, ei, ei — voce nao pode morrer! Eu preciso de voce para as eleicoes de 2026!"
> **ZE:** "Muito motivador. Obrigado."

**Se o jogador esta no Modo Politico e acertou o dilema moral anterior (salvou os refugiados):**
> **WALDECO:** (ao ver Ze combatendo) "Esse... esse cidadao e o tipo de eleitor que eu precisava. Principios. Determinacao. Sem perspectiva de poder."
> *[Ze nao ouve este monologo interno de Waldeco — apenas o jogador ouve]*

### Dilema de rota (escolha rapida, 5 segundos)

Na entrada do corredor da cantina, ha dois caminhos:

**Rota A — Direto (esquerda):** Corredor com 12 Patriotas-Zumbi. Mais combate, mais risco, mais drops.

**Rota B — Desvio (direita):** Sala de arquivo abandonada. Sem Patriotas, mas um cadeado bloqueia a saida. Waldeco tem a chave (historia diferente de como ele a tem dependendo do modo). Mais rapido, menos recursos.

O jogo da 5 segundos para o jogador escolher antes de fechar a porta de Rota B automaticamente (pressao de tempo — Patriotas comecam a aparecer no corredor).

---

## ITENS COLETAVEIS / ARMAS INTRODUZIDAS

| Item | Local | Efeito | Nota |
|---|---|---|---|
| Cabo de Enxada (arma) | Deposito de manutencao | Dano 3, durabilidade 20. Mais lento que vassoura. | Upgrade natural da vassoura |
| Kit de Primeiros Socorros | Camara de bombeamento (caixa vermelha) | Restaura 50% HP | Maior heal da quests iniciais |
| Pasta Confidencial | Escritorio abandonado | Item narrativo — revela plano de evacuacao do Congresso de 2019 (satirico) | Waldeco tem dialogo especifico: "Util. Muito util." |
| Bandeira do Brasil (drop Patriota) | Drop de Patriota-Zumbi | Sem efeito. Ze tem dialogo ao pegar. | Item de cor para o bestiario |

---

## CONDICAO DE SUCESSO

O grupo chega ao elevador de servico com pelo menos Ze (ou Waldeco) e Dona Marta vivos. A filha de Dona Marta, Luciana, esta no proximo andar — a camera do elevador mostra ela no monitor de seguranca, viva, agachada atras de um freezer.

---

## CONDICAO DE FALHA

- Protagonista chega a 0 HP, OU
- Dona Marta e abandonada sem ser carregada e morre no nivel de agua da camara de bombeamento

**Tela de Game Over:** O elevador sobe vazio. O monitor de seguranca mostra o corredor. Texto: *"Voce nao chegou a tempo."*

**Checkpoint:** Entrada do corredor da cantina.

---

## RECOMPENSAS

**Narrativa:**
- Luciana, a filha de Dona Marta, esta no elevador. 23 anos, estagiaria de nutricao na cantina do Congresso. Ela vai acompanhar o grupo daqui para frente (NPC adicional, sem combate — ela carrega suprimentos).
- Waldeco tem um momento de calculo: ao ver Luciana, ele pergunta discretamente "Voce tem celular? Camera ligada?" — Ze ouve e o olha. Waldeco finge que foi outra coisa.

**Gameplay:**
- Desbloqueio: Patriota-Zumbi adicionado ao Bestiario
- Cabo de Enxada permanece no inventario
- Se o jogador escolheu Rota A: bonus **"Frente Ampla"** (+200 pontos)
- Se o jogador escolheu Rota B: bonus **"Articulacao Politica"** (+150 pontos + Waldeco comenta positivamente no dialogo seguinte)

---

## SETUP NARRATIVO DE FECHAMENTO

*O grupo esta no elevador. Quatro pessoas (Ze, Dona Marta, Luciana, Waldeco) num elevador de servico 2x2 metros. A nevoa verde visivel pelas frestas.*

> **LUCIANA:** "Pra onde a gente vai?"
> **ZE:** "Pra fora."
> **WALDECO:** "Para a Praca dos Tres Poderes. Preciso chegar la."
> **ZE:** "A Praca? Por quel? E justamente la que a nevoa subiu."
> **WALDECO:** "Exatamente. E la que as cameras estao. E la que o povo esta olhando. Se eu aparecer la — VIVO, de pe, lutando — eu existo para a historia."
> **DONA MARTA:** "O senhor e doido."
> **WALDECO:** "Eu sou politico. E a mesma coisa."

*Elevador chega. Portas abrem. Luz do dia. Esplanada.*

**PROXIMO: Q1-05 — A RAMPA** *(Os modos Cidadao e Politico voltam a divergir aqui)*

*Nota: Q1-04 (Santinho no Caos) e a quest do Politico que acontece ANTES desta. O jogador do Modo Politico ja viu Q1-04 antes de chegar em Q1-03. O jogador do Modo Cidadao que rejoga como Politico vai reconhecer este elevador e ter uma perspectiva diferente do que Waldeco estava fazendo antes de entrar no tunel.*

---

## OBSERVACOES DE ARTE E AUDIO

**Background do nivel:**
- Tunel de manutencao: concreto cinza escuro, canos expostos, iluminacao de emergencia vermelha piscando. Fios pelados. Goteiras. Paredes com grafites de trabalhadores de construcao de decadas atras ("AQUI TRABALHOU A CONSTRUTORA NORBERTO ODEBRECHT — 1972").
- Camara de bombeamento: teto alto, nivel de agua verde brilhante no chao. A agua reflete as luzes de emergencia criando efeito visual de destaque. A plataforma metalica sobre a agua deve ser visualmente clara — nao ha ambiguidade sobre onde pisar.
- Corredor da cantina: azulejos brancos, cheiro visual (particulas de vapor saindo de panelas tombadas, comida espalhada). Cardapio do dia visivel na parede: "CARDAPIO 08/01: Frango assado, arroz, feijao, zumbi de brinde."

**Audio:**
- Tunel: echo pronunciado em todos os sons. Passos ecoam. Sons de zumbi vem de direcoes imprevisiveis por causa do eco.
- Camara de bombeamento: som de agua, bombas mecanicas batendo em ritmo. Cria tensao sem musica.
- Corredor da cantina: distante, barulho da Esplanada acima. Eco da manifestacao chegando pelo concreto.
- Momento do elevador: silencio total. So o mecanismo do elevador. Esse silencio e o "breath" antes do climax da quest seguinte.

**Animacao especifica:**
- Waldeco no Modo Cidadao: quando ele "desaparece" para gravar o video, ele some pela direita e volta pela esquerda com expressao satisfeita e o celular na mao. Ze nao ve, mas o jogador ve.
- Nenhum personagem usa lanterna ou luz artificial — a iluminacao de emergencia vermelha e suficiente e cria a estetica visual sem precisar de mecanica adicional.
