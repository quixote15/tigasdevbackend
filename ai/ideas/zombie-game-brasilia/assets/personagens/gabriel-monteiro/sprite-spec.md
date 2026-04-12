# GABRIEL MONTEIRO - Especificacao de Sprites

## NPC do Limbo / Residente Permanente - "Zumbis de Brasilia"

---

## Dados Tecnicos Gerais

| Parametro        | Valor                                           |
|------------------|-------------------------------------------------|
| Tipo             | NPC do Limbo (Cancelado Permanente)             |
| Resolucao sprite | 64x64px                                         |
| Framerate alvo   | 8-12fps (jerky, twitchy)                        |
| Linhas           | 2-4px irregulares, tremulas                     |
| Sombreamento     | Cross-hatching denso                            |
| Textura          | Papel envelhecido/sujo                          |
| Proporcoes       | Cabeca 1.5x, torso 2x, pernas 1.5x (~5 cabecas total) |

---

## Paleta de Cores

| Elemento                  | Hex       | Descricao                                      |
|---------------------------|-----------|------------------------------------------------|
| Camiseta (operacao)       | #2B4B2B  | Verde-militar desbotado, quase cinza           |
| Texto camiseta            | #8B8B6B  | Letras gastas, quase ilegiveis                 |
| Calca                     | #3B3B3B  | Preta desgastada, cinza-encardida              |
| Pele                      | #B8956A  | Tom quente, porem ACINZENTADO (degradacao Limbo)|
| Pele (sombras Limbo)      | #887766  | Sombras mais frias, levemente roxas            |
| Cabelo (caotico)          | #2A2010  | Castanho escuro, bagunçado, mechas para cima   |
| Olhos                     | #6B4423  | Castanhos, arregados, perpetuamente surpresos  |
| Olheiras                  | #4A3040  | Roxo-escuro profundo (nao dorme no Limbo)      |
| Cracha CANCELADO          | #CC0000  | Vermelho INTENSO, borda preta grossa           |
| Texto cracha              | #FFFFFF  | "CANCELADO PERMANENTE" em branco sobre vermelho|
| Sombra (projetada)        | #1A0A1A  | Preto-roxo, MAIOR que o personagem             |
| Barba (por fazer)         | #3A3020  | Sombra de barba, 1-2 dias sem fazer            |
| Brilho do video (quando filma)| #FF4444 | Vermelho de "REC" piscando                  |
| Fundo Limbo               | #1A0A1A  | Void roxo-preto                                |
| Nevoa Limbo               | #332244  | Roxo fantasmagorico                            |

---

## Spritesheet Principal - IDLE

### Frame 1 (pose base)
- **Postura**: Ombros caidos, levemente curvado. Postura de quem JA FOI ereto e confiante mas agora desmoronou. Residuo de postura "heroica" -- tenta ficar reto mas nao consegue
- **Cabeca**: 1.5x proporcional. Cabelo que JA FOI arrumado -- gel seco, mechas descontroladas, penteado desmoronando. Era um corte militar/YouTuber, agora e caos
- **Rosto**: Expressao de quem foi PEGO e sabe. Olhos arregados com olheiras profundas. Boca semi-aberta (entre desculpa e surpresa). Barba de 2 dias
- **Deformidade principal**: CRACHA DE "CANCELADO PERMANENTE" grudado no peito. Vermelho vivo, nao sai. Parece soldado/tatuado na camiseta. Brilha levemente em vermelho a cada poucos frames
- **Deformidade secundaria**: SOMBRA projetada no chao e MAIOR e mais AMEAÇADORA que o proprio corpo. A sombra tem forma levemente diferente -- mais agressiva, mais larga, bracos mais compridos. A sombra e quem ele ERA
- **Torso**: Camiseta verde-militar desbotada com texto "OPERACAO [ilegivel]" (letras gastas). Tudo nele e o que SOBROU. A camiseta era justa (tipo policial forte), agora esta larga
- **Maos**: Vazias. Ocasionalmente gesticulam defensivamente (maos abertas na frente, "nao fui eu")
- **Pes**: Tenis surrados, desamarrados. Meia aparecendo

### Frame 2-4 (variacao idle)
- Frame 2: Olhos se mexem para o lado (paranoia, checando se alguem esta julgando). Cracha de "CANCELADO" faz pulso vermelho sutil. Sombra no chao se mexe 1px de forma independente
- Frame 3: Maos fazem gesto defensivo rapido (abre as palmas na frente do corpo, recua). Ombros sobem (encolhimento). Cabelo muda 1px (mexa cai)
- Frame 4: Volta ao repouso. Sombra volta a posicao. Olhos voltam para frente. Suspiro (corpo desce 1px e volta)

### Contagem de Frames: 4 frames, loop a 8fps

---

## Spritesheet - WALK

### Ciclo de 6 frames
- **Estilo de caminhada**: Arrastando os pes. Ombros baixos. Caminhada de LIMBO -- sem pressa, sem destino. Ocasionalmente tenta andar com postura reta (residuo de ex-policial) mas recai
- **Frame 1**: Pe direito arrasta. Camiseta balanca (larga). Sombra se move com delay
- **Frame 2**: Peso transfere. Tenta endireitar ombros (falha). Cracha brilha
- **Frame 3**: Pe esquerdo arrasta. Olhar para baixo. Cabelo mexe com o movimento
- **Frame 4**: Ergue a cabeca (momento de "falsa esperanca"). Sombra atras CRESCE 1px
- **Frame 5**: Cabeca desce de novo. Pe direito. Desanimo
- **Frame 6**: Completa ciclo. Sombra "se acomoda" -- volta ao tamanho anterior

### Notas sobre walk:
- A SOMBRA se move com delay de 1-2 frames, como entidade semi-independente
- Sombra as vezes e 20-30% maior que o sprite real
- Caminhada nunca e confiante. Sempre arrastada
- A cada 3 ciclos: tenta endireitar a coluna por 1 frame, depois desiste

---

## Spritesheet - TALK (Interacao NPC)

### Ciclo de 8 frames (loop durante dialogo)
- **Frame 1**: Vira para o jogador. Olhos arregalam. Boca abre para falar
- **Frame 2**: Mao direita levanta (gesticulando). Expressao animada (saudade de ser ouvido)
- **Frame 3**: APONTA PARA SI MESMO com ambas as maos. "EU ERA..." (auto-referencia)
- **Frame 4**: Maos abrem para os lados (gesticulacao tipo YouTuber -- residuo de quando fazia videos)
- **Frame 5**: Expressao muda para DESCULPA. Ombros sobem. Maos na frente
- **Frame 6**: Olha para os lados (paranoia). Cracha pulsa vermelho
- **Frame 7**: Tentativa de sorriso (falha -- parece careta). Mao no cabelo (tentando arrumar)
- **Frame 8**: Desiste. Ombros caem. Volta a postura curvada. Suspiro

---

## Spritesheet - SKILL NPC 1: "Residente Permanente"

### Aparicao no Limbo quando jogador morre (8 frames)
- **Frame 1-2**: Escuridao do Limbo. Dois olhos arregados aparecem na nevoa roxa
- **Frame 3-4**: Gabriel emerge da nevoa, caminhando em direcao ao jogador. Cracha de CANCELADO brilha intenso (unica luz no void). Sombra ENORME atras dele
- **Frame 5-6**: Para na frente do jogador. Expressao de "ah, voce tambem?". Acena com a mao
- **Frame 7-8**: Faz gesto de "boas vindas" ironico. Mostra cracha. "Eu moro aqui"

---

## Spritesheet - SKILL NPC 2: "Falsa Heroica"

### Tenta ajudar o jogador mas ATRAPALHA (10 frames)
- **Frame 1-2**: Expressao muda para DETERMINACAO (residuo de heroi). Endireita os ombros. Bate no peito (por cima do cracha)
- **Frame 3-4**: CORRE em direcao ao perigo (animacao acelerada, bracos bombando). Sombra o persegue, MAIOR que ele
- **Frame 5-6**: TROPEÇA no proprio pe. Cai de cara. Camiseta rasga mais um pouco
- **Frame 7-8**: Rola no chao. Acidentalmente derruba um item do jogador ou empurra um inimigo para PERTO do jogador (piora a situacao)
- **Frame 9-10**: Levanta, poeira no corpo. Maos abertas defensivas. "Desculpa! Eu tava tentando ajudar!" Volta a postura curvada

---

## Spritesheet - SKILL NPC 3: "Video Armado"

### Finge filmar algo espontaneo (8 frames)
- **Frame 1-2**: Tira celular ANTIGO do bolso (tela rachada, modelo velho). Olhos brilham (saudade de ser YouTuber). Postura endireita
- **Frame 3-4**: Aponta celular para o jogador/cena. Indicador vermelho "REC" piscando. Expressao de "apresentador" (sorriso forcado, queixo erguido)
- **Frame 5-6**: REALIZA que ninguem se importa. Sorriso murcha. Celular treme na mao
- **Frame 7-8**: Guarda celular lentamente. Ombros caem. Cracha de CANCELADO pulsa vermelho mais forte que o normal. Volta ao idle

---

## Spritesheet - DEATH/FADE (NPC nao morre -- DESFAZ no Limbo)

### 8 frames
- **Frame 1-2**: Corpo comeca a se dissolver em particulas roxas (nevoa do Limbo absorvendo)
- **Frame 3-4**: Cracha de CANCELADO e a ULTIMA coisa a desaparecer -- brilha vermelho intenso enquanto o corpo some
- **Frame 5-6**: Sombra permanece 2 frames APOS o corpo sumir. Sombra se contorce sozinha
- **Frame 7-8**: Sombra finalmente dissolve. Ultima coisa visivel: o texto "CANCELADO PERMANENTE" flutuando no ar por 1 frame antes de sumir

---

## Spritesheet - HIT/DAMAGE (quando atingido acidentalmente)

### 4 frames
- **Frame 1**: Flash roxo (cor do Limbo, nao vermelho -- ele pertence ao Limbo). Expressao de "de novo?!"
- **Frame 2**: Recua exageradamente (overreaction -- residuo dramatico de YouTuber)
- **Frame 3**: Cracha de CANCELADO balanca. Sombra se agita
- **Frame 4**: Volta, maos abertas defensivas. "Eu ja estou no Limbo, que mais podem fazer?"

---

## Efeitos Permanentes (SEMPRE ativos)

1. **Cracha "CANCELADO PERMANENTE"**: Sempre visivel no peito. Pulso vermelho sutil a cada 16-20 frames. NUNCA sai
2. **Sombra autonoma**: Projetada atras/abaixo, 20-30% MAIOR que o sprite. Move com delay de 1-2 frames. Ocasionalmente faz gestos DIFERENTES do corpo (sombra mais agressiva)
3. **Olheiras**: Sempre presentes. Escurecem 1 shade quando no Limbo profundo
4. **Cabelo entropico**: Sempre em degradacao. Mechas mudam de posicao levemente entre animacoes (nunca igual duas vezes)
5. **Camiseta frouxa**: Balanca com movimento, mais que deveria para a velocidade

---

## A SOMBRA - Especificacao Detalhada

A sombra e a feature visual mais UNICA de Gabriel Monteiro. Merece especificacao propria.

### Comportamento
| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Tamanho relativo      | 120-130% do sprite principal                       |
| Cor                   | #1A0A1A (preto-roxo)                               |
| Opacidade             | 70-85% (varia)                                     |
| Delay de movimento    | 1-2 frames atras do corpo                          |
| Direcao               | Oposta a "luz" do ambiente (ou fixa atras)         |
| Deformacao            | Bracos mais longos, ombros mais largos, postura mais ereta |

### Personalidade da Sombra
A sombra representa QUEM ELE ERA (ou quem ele fingia ser):
- Quando Gabriel esta curvado, a sombra esta ERETA
- Quando Gabriel gesticula defensivo, a sombra gesticula AGRESSIVAMENTE
- Quando Gabriel tenta ser heroico (Falsa Heroica), a sombra COINCIDE brevemente com o corpo (unico momento de sincronia)
- No Limbo profundo, a sombra e MAIS nitida que o proprio corpo

### Renderizacao
- Camada ABAIXO do sprite principal
- Projecao com skew (achatada no eixo Y para parecer chao, OU erguida atras como entidade)
- NO LIMBO: sombra fica ATRAS (vertical, como fantasma), nao no chao
- FORA DO LIMBO (se aplicavel): sombra no chao, achatada, mas desproporcional

---

## Hitbox e Collider (NPC)

| Elemento     | Offset X | Offset Y | Largura | Altura | Nota                    |
|-------------|----------|----------|---------|--------|-------------------------|
| Corpo       | 18       | 10       | 28      | 44     | Interacao de NPC        |
| Hitbox talk | 8        | 4        | 48      | 56     | Area de ativacao dialogo|
| Sombra      | N/A      | N/A      | N/A     | N/A    | Sem collider (visual only)|

---

## Notas para Implementacao

1. Gabriel e NPC, NAO inimigo. O jogador interage com ele por DIALOGO no Limbo
2. A sombra e um sprite SEPARADO com logica propria de movimento (nao e sombra automatica)
3. Quando o jogador morre e vai ao Limbo, Gabriel e SEMPRE o primeiro NPC que aparece
4. As skills de NPC sao eventos scriptados, nao combate
5. "Falsa Heroica" deve ter colisao real -- ele REALMENTE atrapalha (empurra coisas, derruba itens)
6. O cracha de "CANCELADO" deve ter prioridade de render ALTA -- sempre visivel, nunca obstruido
7. No Limbo, a iluminacao e diferente: tudo roxo-escuro. O cracha vermelho e a unica luz "quente"
8. A expressao padrao e DESCONFORTO EXISTENCIAL. Nunca neutro. Nunca feliz (exceto flash de falsa heroica)
