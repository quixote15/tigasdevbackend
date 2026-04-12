# DANIEL VORCARO - Especificacao de Sprites

## Boss Nomeado / Vilao Real de 2026 - "Zumbis de Brasilia"

---

## Dados Tecnicos Gerais

| Parametro        | Valor                                      |
|------------------|--------------------------------------------|
| Tipo             | Boss nomeado (Vilao Real)                  |
| Resolucao sprite | 64x64px                                    |
| Resolucao projeteis | 32x32px                                 |
| Framerate alvo   | 8-12fps (jerky, twitchy)                   |
| Linhas           | 2-4px irregulares, tremulas                |
| Sombreamento     | Cross-hatching denso                       |
| Textura          | Papel envelhecido/sujo                     |
| Proporcoes       | Cabeca 1.5x, torso 2x, pernas 1.5x (~5 cabecas total) |

---

## Paleta de Cores

| Elemento               | Hex       | Descricao                                    |
|------------------------|-----------|----------------------------------------------|
| Terno (principal)      | #1A1A2E  | Azul-noite luxuoso, quase preto              |
| Terno (risca)          | #C9A82C  | Dourado opulento (riscas finíssimas)         |
| Camisa                 | #F5F5F0  | Branco-perola (caro demais)                  |
| Gravata                | #8B0000  | Vermelho-sangue com brilho cetim             |
| Pele                   | #C4956A  | Tom quente, ligeiramente cinza (corrupcao)   |
| Cabelo engomado        | #1C1C1C  | Preto brilhante, gel excessivo               |
| Dentes                 | #FFFFFF  | Branco OBSCENO, brilho artificial            |
| Brilho dos dentes      | #E0F0FF  | Flash de luz azulada nos dentes              |
| Olhos ($ cifrao)       | #00CC00  | Verde dinheiro nas pupilas                   |
| Iris (fundo)           | #004400  | Verde escuro atras do cifrao                 |
| Celular (tela)         | #00CCFF  | Azul-branco, brilho constante               |
| Celular (corpo)        | #2A2A2A  | Preto grafite, moldura fina                  |
| Notas/dinheiro (R$)    | #2E8B57  | Verde-cedula                                 |
| Notas/dinheiro (brilho)| #FFD700  | Dourado das moedas flutuantes                |
| Aura corrupcao         | #3D1F00  | Marrom-dourado, fuligem de riqueza           |
| Sangue (ceu fundo)     | #CC4400  | Laranja-sangue do ceu                        |
| Sombras                | #0A0A0A  | Preto profundo, cross-hatching cerrado       |

---

## Spritesheet Principal - IDLE

### Frame 1 (pose base)
- **Postura**: Em pe, ligeiramente inclinado para frente, postura de quem esta acima de todos
- **Cabeca**: 1.5x proporcional. Cabelo engomado PERFEITAMENTE para tras, brilho de gel. Rosto com sorriso largo permanente
- **Deformidade principal**: DENTES exageradamente brancos, brilhando como neon. Flash de luz nos dentes a cada 3 frames. Ocupam 40% do rosto quando sorrindo
- **Olhos**: Pupilas sao CIFROES ($) verdes. Nao tem iris normal. Os cifroes giram levemente (animacao)
- **Torso**: Terno ABSURDAMENTE luxuoso -- riscas douradas visiveis mesmo em 64px. Abotoadura brilhando. Gravata vermelha de seda. Lenco no bolso. Tudo EXCESSIVO
- **Maos**: Dedos em movimento CONSTANTE, como se contassem dinheiro invisivel. Mao esquerda segura celular. Mao direita com dedos twitching
- **Celular**: Na mao esquerda, tela sempre acesa em azul-branco, linhas de texto rolando (conversas com politicos)
- **Particulas**: 4-6 notas de R$ e moedas douradas flutuando ao redor do corpo, orbitando devagar. SEMPRE presentes
- **Pes**: Sapatos italianos brilhantes, ridiculamente engraxados

### Frame 2-4 (variacao idle)
- Frame 2: Dentes fazem FLASH de brilho. Cifroes nos olhos giram 15 graus. Dedos da mao direita fecham levemente
- Frame 3: Celular emite pulso de luz azul. Notas flutuantes sobem 2px. Sobrancelha levanta (arrogancia)
- Frame 4: Dedos completam gesto de "contar". Volta ao frame 1. Moedas completam rotacao orbital

### Contagem de Frames: 4 frames, loop a 8fps

---

## Spritesheet - WALK

### Ciclo de 6 frames
- **Estilo de caminhada**: Passos CONFIANTES, quase arrogantes. Nao anda -- DESFILA. Ombros largos, queixo erguido
- **Frame 1**: Pe direito a frente, celular na mao, notas flutuando para tras (movimento)
- **Frame 2**: Transferencia de peso, terno balanca levemente, brilho nos sapatos
- **Frame 3**: Pe esquerdo a frente, sorriso se abre mais, dentes flasham
- **Frame 4**: Peso no pe esquerdo, dedos direitos contando no ar
- **Frame 5**: Pe direito levantando, celular emite notificacao (flash na tela)
- **Frame 6**: Transicao, moedas flutuantes reagrupam ao redor

### Notas sobre walk:
- Particulas de dinheiro SEMPRE acompanham, com leve delay (arrasto)
- Celular NUNCA sai da mao -- ele anda olhando para o celular frequentemente
- Sorriso nunca fecha. Dentes sempre visiveis
- A cada 2 ciclos completos: uma nota extra aparece e desaparece

---

## Spritesheet - ATTACK (Normal)

### "Contagem Regressiva" - Ataque basico (8 frames)
- **Frame 1-2**: Levanta o celular como se mostrasse uma conversa comprometedora
- **Frame 3-4**: Tela do celular brilha intensamente (flash branco-azulado)
- **Frame 5-6**: Onda de notas de dinheiro disparada para frente como projeteis
- **Frame 7-8**: Retorna a posicao, sorriso mais largo, cifroes nos olhos giram rapido

---

## Spritesheet - SKILL 1: "R$52 Bilhoes"

### Explosao de notas em area (12 frames)
- **Frame 1-3**: Vorcaro ergue AMBAS as maos (celular flutua sozinho ao lado). Aura dourada intensifica. Expressao muda de sorriso para GARGALHADA
- **Frame 4-5**: Cifroes nos olhos CRESCEM (ocupam o olho inteiro). Notas flutuantes aceleram freneticamente. O chao sob ele racha com simbolos de $
- **Frame 6-8**: EXPLOSAO -- centenas de notas de R$ disparam em TODAS as direcoes. Ondas concentricas de moedas douradas. Tela do celular mostra "R$ 52.000.000.000"
- **Frame 9-10**: Notas chovem, area de efeito visivel (circulo de destruicao financeira)
- **Frame 11-12**: Vorcaro recolhe celular, ajusta gravata, sorriso satisfeito. Algumas notas ainda caindo

### Projeteis (32x32px):
- Nota de R$100 em chamas (4 frames animacao)
- Moeda dourada girando (3 frames rotacao)
- Cifrao ($) verde brilhante pulsando (2 frames)

---

## Spritesheet - SKILL 2: "Delacao Premiada"

### Ativada ao ser derrotado -- Todos bosses perdem 20% defesa (10 frames)
- **Frame 1-2**: Vorcaro cai de joelhos (nao de derrota, de ESTRATEGIA). Sorriso permanece. Celular erguido
- **Frame 3-4**: Celular projeta HOLOGRAMA de todos os outros bosses conectados por linhas vermelhas (teia de corrupcao)
- **Frame 5-6**: Linhas vermelhas EXPLODEM. Cada boss conectado recebe flash vermelho. Vorcaro diz (texto): "Quem eu entrego primeiro?"
- **Frame 7-8**: Ondas de choque saem do celular em todas as direcoes. Selo "DELACAO PREMIADA" aparece sobre a cabeca
- **Frame 9-10**: Efeito de debuff visivel -- icone de escudo rachado aparece sobre todos os bosses. Vorcaro se levanta, ajusta terno

---

## Spritesheet - SKILL 3: "Celular Bomba"

### Revela segredos, paralisa inimigos por 3s (10 frames)
- **Frame 1-2**: Ergue celular dramaticamente acima da cabeca. Tela brilha intenso
- **Frame 3-4**: Celular emite ondas sonicas visiveis (circulos concentricos azuis). Icones de WhatsApp, chamadas, fotos vazam da tela
- **Frame 5-7**: Bolhas de "mensagens" explodem pelo ar -- cada uma com fragmento de conversa ilegivel. Inimigos atingidos congelam com expressao de panico
- **Frame 8-9**: Simbolo de cadeado ABERTO aparece sobre cada inimigo paralisado
- **Frame 10**: Vorcaro guarda celular com calma, sorriso de quem sabe tudo

---

## Spritesheet - SKILL 4: "Captura Financeira"

### Corrompe inimigos para protege-lo (12 frames)
- **Frame 1-3**: Vorcaro estala os dedos. Chuva de notas converge sobre um inimigo alvo
- **Frame 4-6**: Inimigo e envolvido por TORNADO de dinheiro. Olhos do inimigo mudam para cifroes ($)
- **Frame 7-9**: Inimigo corrompido recebe aura dourada. Barra de vida muda de cor (vermelho para dourado)
- **Frame 10-12**: Inimigo corrompido vira escudo, posicionando-se entre Vorcaro e o jogador. Vorcaro cruza bracos, satisfeito

---

## Spritesheet - DEATH

### 12 frames (mais elaborado -- e um Boss)
- **Frame 1-2**: Expressao de surpresa GENUINA pela primeira vez. Sorriso FINALMENTE desaparece. Celular cai da mao
- **Frame 3-4**: Terno comeca a se desfazer -- riscas douradas viram cinza. Cifroes nos olhos piscam, falham
- **Frame 5-6**: Celular no chao explode em luz -- TODAS as conversas vazam como fantasmas luminosos subindo
- **Frame 7-8**: Notas flutuantes pegam fogo e viram cinzas. Moedas derretem. Dentes perdem brilho
- **Frame 9-10**: Corpo encolhe dentro do terno agora grande demais. Olhos voltam ao normal (pupilas comuns) pela unica vez
- **Frame 11-12**: Colapsa em pilha de cinzas, terno vazio, celular destruido. Ultima nota de R$ cai do ar e queima. Texto final: "R$52 bilhoes em fumaca"

---

## Spritesheet - HIT/DAMAGE

### 4 frames
- **Frame 1**: Flash vermelho no corpo. Sorriso se contorce (NÃO desaparece -- ele sorri mesmo tomando dano)
- **Frame 2**: Recuo leve. Algumas notas flutuantes caem. Celular oscila na mao
- **Frame 3**: Cifroes nos olhos piscam em vermelho. Terno tem marca de impacto
- **Frame 4**: Recupera compostura. Ajusta gravata. Sorriso volta com forca total. "Isso nao me atinge"

---

## Spritesheet - TAUNT/PROVOCACAO

### 6 frames (antes de batalha)
- **Frame 1-2**: Mostra celular para o jogador. Tela com lista de nomes (sugere delacao)
- **Frame 3-4**: Gargalhada. Dentes brilham intenso. Notas explodem para cima como confete
- **Frame 5-6**: Aponta para o jogador com dedo que se move contando. Bordao: "Eu conheco TODO MUNDO."

---

## Efeitos Permanentes (SEMPRE ativos)

1. **Particulas de dinheiro**: 4-6 notas/moedas orbitando o corpo. Nunca param. Velocidade varia com estado (calmo = devagar, ataque = rapido)
2. **Brilho do celular**: Pulsacao azul-branca constante na mao esquerda. Nunca apaga
3. **Flash dos dentes**: A cada 12-16 frames, flash de brilho artificial nos dentes
4. **Cifroes girando**: Rotacao sutil e constante nas pupilas
5. **Dedos contando**: Micro-animacao nos dedos da mao direita, loop de 4 frames sobreposto a qualquer estado

---

## Hitbox e Collider

| Elemento     | Offset X | Offset Y | Largura | Altura |
|-------------|----------|----------|---------|--------|
| Corpo       | 16       | 8        | 32      | 48     |
| Cabeca      | 18       | 4        | 28      | 20     |
| Ataque (notas) | -16   | -16      | 96      | 96     |
| Skill area  | -48      | -48      | 160     | 160    |

---

## Notas para Implementacao

1. As particulas de dinheiro sao um SISTEMA SEPARADO de particulas, nao parte do spritesheet
2. O celular emite luz -- usar blend mode additivo para o brilho da tela
3. Boss com barra de vida EXTENDIDA (3x vida de inimigo normal)
4. A "Delacao Premiada" e uma mecanica UNICA -- precisa de referencia a todos os outros bosses carregados na fase
5. NUNCA remover o sorriso (exceto na death animation) -- e a marca visual principal
6. Os cifroes nos olhos devem ser renderizados com contorno preto 1px para visibilidade em 64px
