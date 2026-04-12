# XANDAO - Especificacao Completa de Sprites

## Boss do STF Principal - "Zumbis de Brasilia"

---

## Especificacoes Tecnicas Gerais

| Propriedade | Valor |
|---|---|
| **Tamanho por frame** | 64x64 pixels |
| **Projeteis** | 32x32 pixels |
| **Formato** | PNG com transparencia |
| **Sprite sheet** | Horizontal (frames lado a lado) |
| **Frame rate** | 8-12 fps (estilo twitchy/jerky) |
| **Paleta base** | Preto da toga, pele morena-avermelhada, vermelho sangue (olhos/veias), dourado sujo (detalhes toga), branco brilhante (careca) |
| **Direcao padrao** | Virado para a direita. Espelhar horizontalmente para esquerda. |

---

## ANATOMIA BASE DO XANDAO (Proporcoes no grid 64x64)

```
Distribuicao vertical (64px total):
- Careca/Cabeca: 20px de altura (DESPROPORCIONAL - cabeca grande)
- Pescoco grosso: 4px (largo, com veias visiveis)
- Tronco/Toga: 24px (ombros largos, biceps estourando a toga)
- Pernas: 16px (curtas em relacao ao corpo - estilo grotesco)

Distribuicao horizontal:
- Corpo centralizado: ~28px de largura
- Martelo: ultrapassa a bounding box do sprite (ate 48px de largura quando apoiado)
- Toga: ondula 4-6px alem do corpo

Destaques anatomicos obrigatorios em TODOS os frames:
1. CARECA - ocupa topo do sprite, brilho branco/amarelo (highlight pixel variando)
2. SOBRANCELHA - grossa, franzida SEMPRE, 2px de altura
3. OLHOS - pequenos, vermelhos, furiosos (pupilas minusculas)
4. MANDIBULA - quadrada, proeminente, 6px de largura
5. PESCOCO - mais largo que o normal, veias como linhas escuras
6. BICEPS - bolhas musculares sob a toga, deformam o tecido
7. TOGA - preta, linhas irregulares, amarrotada, bordas rasgadas
8. MARTELO - SEMPRE presente, tamanho variavel por animacao
9. VEIAS - na testa e pescoco, em cor escura/vermelha
```

---

## 1. IDLE - 4 Frames

**Arquivo**: `xandao-idle.png` (256x64 - 4 frames de 64x64)
**Frame rate**: 8 fps
**Loop**: Sim, infinito
**Sensacao**: Poder contido, ameaca latente, "eu estou te observando"

### Frame 1 - Postura Base
- **Corpo**: Ereto, levemente inclinado para frente (intimidacao)
- **Careca**: Brilho MAXIMO - highlight branco de 3x3px no topo centro
- **Olhos**: Vermelhos, estreitados, olhando para frente
- **Sobrancelha**: Franzida ao maximo
- **Boca**: Fechada, cantos para baixo, mandibula cerrada
- **Toga**: Repouso, linhas de dobra visiveis, bordas irregulares
- **Biceps**: Visivel sob toga, tamanho "normal" (ja exagerado)
- **Martelo**: Apoiado no ombro direito, cabo descendo atras do corpo
- **Veias**: Visiveis na testa (2 linhas finas)
- **Pernas**: Afastadas, postura de poder

### Frame 2 - Careca Pulsando
- **Diferenca do Frame 1**: Highlight da careca MUDA de posicao (2px para esquerda)
- **Veias**: Levemente mais grossas (+1px em uma veia)
- **Toga**: Micro-ondulacao na borda inferior esquerda (1px de deslocamento)
- **Olhos**: Identicos ao Frame 1
- **Efeito**: Sugere que a careca esta BRILHANDO e refletindo luz

### Frame 3 - Toga Ondulando
- **Diferenca do Frame 1**: Borda da toga ondula para direita (2px de deslocamento)
- **Careca**: Highlight volta ao centro mas com forma diferente (2x4px ao inves de 3x3px)
- **Biceps**: FLEXIONAM - 1px maior que Frame 1 (toga estica)
- **Veias**: Pulsam - mais visiveis no pescoco (cor mais intensa)
- **Expressao**: Sobrancelha sobe 1px (micro-raiva)

### Frame 4 - Biceps Flexionando
- **Diferenca do Frame 1**: Biceps no MAXIMO - 2px maiores, toga esticada ao limite
- **Careca**: Brilho mais fraco (highlight 2x2px) - preparando proximo pulso
- **Veias**: MAXIMO - todas visiveis, cor vermelha intensa
- **Mandibula**: Levemente aberta (1px) como se resmungando
- **Toga**: Puxa nos ombros por causa dos biceps
- **Martelo**: Treme levemente (1px de deslocamento horizontal)

---

## 2. WALK - 6 Frames

**Arquivo**: `xandao-walk.png` (384x64 - 6 frames de 64x64)
**Frame rate**: 10 fps
**Loop**: Sim, enquanto caminhando
**Sensacao**: Marcha militar, peso absurdo, chao protestando, intimidacao ambulante

### Frame 1 - Passo Direito (Contato)
- **Perna direita**: Esticada a frente, pe tocando o chao
- **Perna esquerda**: Atras, levantando
- **Corpo**: Leve inclinacao para frente
- **Martelo**: Arrastando no chao atras (cabo na mao direita, cabeca no chao)
- **Chao**: 2-3 pixels de "rachadura" onde o martelo toca
- **Careca**: Brilho medio
- **Toga**: Esvoaca para tras (movimento)
- **Expressao**: Raiva padrao, olhos fixos a frente

### Frame 2 - Passo Direito (Peso)
- **Perna direita**: Flexionada, absorvendo peso
- **Perna esquerda**: Levantada, deslocando para frente
- **Corpo**: Mais baixo (2px - agachamento do peso)
- **Chao**: Rachadura EXPANDE (+2px) onde o pe pisa
- **Martelo**: Levanta levemente do chao (1-2px)
- **Careca**: Brilho INTENSO (impacto do passo gera vibracao)
- **Veias**: Saltando no pescoco
- **Toga**: Comprimida pela posicao agachada

### Frame 3 - Transicao (Meio)
- **Ambas pernas**: Uma passando pela outra, posicao neutra
- **Corpo**: Altura normal
- **Martelo**: Arrastando novamente, faiscas na ponta (2-3 pixels amarelos)
- **Careca**: Brilho pulsando
- **Toga**: Ondulando lateralmente
- **Rastro no chao**: Linha irregular onde martelo passou

### Frame 4 - Passo Esquerdo (Contato)
- **Espelho do Frame 1** mas com perna esquerda a frente
- **Martelo**: Muda de angulo levemente (oscila com o caminhar)
- **Chao**: Nova rachadura na posicao do pe esquerdo
- **Toga**: Esvoaca para lado oposto

### Frame 5 - Passo Esquerdo (Peso)
- **Espelho do Frame 2** com perna esquerda
- **Corpo**: Desce 2px
- **Chao**: Rachadura expande
- **Veias**: MAXIMO (esforco de carregar o martelo gigante)
- **Biceps**: Tensos, visiveis

### Frame 6 - Transicao (Retorno)
- **Espelho do Frame 3** mas com detalhes diferentes
- **Martelo**: Mais levantado (preparando proximo ciclo)
- **Expressao**: Queixo empinado (arrogancia)
- **Toga**: Momento de maior esvoaco
- **Particulas**: Poeira subindo dos pes (2-3 pixels cinza)

---

## 3. ATTACK - 3 Frames

**Arquivo**: `xandao-attack.png` (192x64 - 3 frames de 64x64)
**Frame rate**: 12 fps (rapido - impacto violento)
**Loop**: Nao - executa uma vez por ataque
**Sensacao**: PANCADA ABSURDA, "CENSURADO" marcado na realidade

### Frame 1 - Ergue o Martelo
- **Corpo**: Levemente recuado, peso na perna traseira
- **Martelo**: ACIMA da cabeca, cabeca do martelo no topo do sprite (quase saindo)
- **Biceps**: NO MAXIMO ABSOLUTO - toga rasgando nos ombros
- **Veias**: TODAS vissiveis, vermelhas vivas
- **Olhos**: Arregalados, brilho vermelho intenso
- **Boca**: Aberta - gritando "CENSURADO!"
- **Careca**: Brilho maximo (esforco fisico)
- **Toga**: Esticada ao limite, costuras aparecendo
- **Inscricao no martelo**: "CENSURADO" em vermelho (legivel mesmo em 64x64 - 1px de altura por letra)

### Frame 2 - Martela com "CENSURADO"
- **Corpo**: Inclinado TOTALMENTE para frente, peso na perna dianteira
- **Martelo**: Na posicao de IMPACTO - na frente do corpo, embaixo
- **Ponto de impacto**: Flash branco/vermelho (6x6px de explosao)
- **Texto "CENSURADO"**: Aparece em vermelho ACIMA do ponto de impacto (projetil separado 32x32)
- **Chao**: Rachadura em estrela no ponto de impacto
- **Toga**: Esvoaca violentamente para cima com o movimento
- **Biceps**: Contraidos, deformando a toga
- **Expressao**: Grito de guerra, veias ao maximo
- **Screen shake**: Indicar nos metadados que deve haver shake de 2px

### Frame 3 - Onda de Choque
- **Corpo**: Recuperando postura, martelo no chao a frente
- **Onda de choque**: Arco concentrico saindo do ponto de impacto (linhas brancas)
- **Chao**: Rachaduras se expandindo em 3 direcoes
- **Poeira**: Nuvem de particulas (6-8 pixels cinza-marrom)
- **Texto "CENSURADO"**: Pulsando/desaparecendo
- **Expressao**: Sorriso cruel, satisfacao de poder
- **Careca**: Brilho voltando ao normal
- **Toga**: Assentando

---

## 4. DEATH - 4 Frames

**Arquivo**: `xandao-death.png` (256x64 - 4 frames de 64x64)
**Frame rate**: 8 fps (dramatico, lento)
**Loop**: Nao - executa uma vez, fica no ultimo frame
**Sensacao**: Queda epica, poder se esvaindo, toga vira papelada

### Frame 1 - Impacto Inicial
- **Corpo**: Recua violentamente, inclinado para tras
- **Olhos**: ARREGALADOS de choque (primeira vez que nao esta com raiva - esta SURPRESO)
- **Boca**: Aberta em O de surpresa
- **Martelo**: Escapando da mao, inclinado
- **Careca**: Brilho PISCANDO (alternando entre brilhante e opaco)
- **Toga**: Comeca a se desfazer nas bordas (pixels se soltando)
- **Veias**: Pulsam irregularmente

### Frame 2 - Caindo
- **Corpo**: Caindo para tras, joelhos dobrando
- **Martelo**: No chao, separado do corpo, rachando
- **Toga**: 30% decomposta - pedacos voando como PAPEIS DE INQUERITO
- **Papeis**: 4-6 retangulos brancos pequenos (2x3px) voando
- **Careca**: Brilho FRACO - apenas 1x1px de highlight
- **Olhos**: Fechando, vermelho esvaindo
- **Texto em papeis**: Sugestao de texto (linhas finas representando escrita)

### Frame 3 - No Chao
- **Corpo**: Caido de costas, pernas levantadas
- **Martelo**: Estilhacado em 3 pedacos ao lado
- **Toga**: 70% decomposta em papeis - papeis espalhados pelo chao
- **Papeis voando**: 8-10 retangulos em varias alturas
- **Careca**: SEM BRILHO - cor opaca, sem highlight
- **Olhos**: Fechados
- **Veias**: Desaparecendo (cor enfraquecendo)
- **Alguns papeis**: Com "INQUERITO" legivel em vermelho tiny

### Frame 4 - Estado Final (Permanece)
- **Corpo**: Silhueta no chao, quase coberta por papeis
- **Martelo**: Apenas cabo visivel entre papeis
- **Toga**: 100% decomposta - nao existe mais, so papeis
- **Papeis**: Espalhados ao redor, cobrindo parcialmente o corpo
- **Careca**: COMPLETAMENTE OPACA - parece pedra, zero brilho
- **Expressao**: Olhos fechados, boca fechada, raiva COMPLETAMENTE AUSENTE
- **Unico brilho**: Leve reflexo vermelho nos papeis (resquicio de poder)
- **Efeito final**: Corpo meio transparente (alpha 70%), papeis opacos

---

## 5. HIT - 2 Frames

**Arquivo**: `xandao-hit.png` (128x64 - 2 frames de 64x64)
**Frame rate**: 12 fps (rapido)
**Loop**: Nao - executa uma vez, volta para idle
**Sensacao**: "VOCE OUSOU ME BATER?!" - raiva multiplicada

### Frame 1 - Recua Furioso
- **Corpo**: Deslocado 4px para tras do centro, levemente inclinado
- **Flash de dano**: Borda do sprite pisca branco (outline de 1px)
- **Olhos**: ARREGALADOS, vermelho MAXIMO, brilho expandido (3x3px de glow vermelho cada olho)
- **Boca**: Aberta, gritando "FALA SERIO!"
- **Careca**: Brilho VERMELHO (nao branco - raiva contamina o brilho)
- **Veias**: DOBRAM de tamanho, pulsam em vermelho vivo
- **Biceps**: Incham instantaneamente (+3px)
- **Toga**: Ondula violentamente
- **Martelo**: Segurado com mais forca (mao crispada, branca)
- **Particulas**: 3-4 pixels vermelhos saindo dos olhos (inicio de raios)

### Frame 2 - Raiva Intensificada
- **Corpo**: Volta a posicao mas MAIOR (1px extra em cada direcao - "inchando" de raiva)
- **Olhos**: Raios vermelhos curtos saindo (4px de comprimento cada)
- **Veias**: NO MAXIMO ABSOLUTO - visiveis ate nos bracos
- **Careca**: Brilho voltando a branco mas MAIS INTENSO que o normal (4x4px highlight)
- **Mandibula**: Cerrada, musculos visiveis
- **Toga**: Esticando com o corpo expandido
- **Aura**: Leve glow vermelho ao redor do corpo (1px de borda vermelha semi-transparente)
- **Efeito visual**: Boss esta agora MAIS PERIGOSO (comunicar visualmente ao jogador)

---

## 6. SPECIAL - Censura Monocratica (6 Frames)

**Arquivo**: `xandao-special-censura.png` (384x64 - 6 frames de 64x64)
**Frame rate**: 10 fps
**Loop**: Nao
**Efeito gameplay**: Silencia inimigos em area por 5 segundos
**Sensacao**: Poder absoluto, silencio forcado, "EU MANDO AQUI"

### Frame 1 - Preparacao
- **Corpo**: Se endireita, postura RIGIDA, militar
- **Mao esquerda**: Levantando, palma para frente (gesto de "pare")
- **Martelo**: Transferido para mao direita apenas, apontado para baixo
- **Olhos**: Estreitando, brilho vermelho crescendo
- **Careca**: Brilho concentrando no centro (como se carregando energia)
- **Boca**: Fechada, labios apertados
- **Toga**: Parada, rigida (nao ondula - CONTROLE TOTAL)

### Frame 2 - Mao Levantada
- **Mao esquerda**: TOTALMENTE levantada, dedos espalmados
- **Aura na mao**: Glow vermelho ao redor da palma (3x3px)
- **Olhos**: Comecam a brilhar mais intenso
- **Expressao**: Concentracao de poder puro
- **Ar ao redor**: Ondulacao (distorcao de calor - pixels levemente deslocados)
- **Texto aparecendo**: "MONOCRATICAMENTE!" comeca a se formar (primeiras letras)

### Frame 3 - Raios dos Olhos Ativam
- **Olhos**: DISPARAM raios vermelhos horizontais (estendem 8px para fora do sprite)
- **Raios**: 2px de espessura, vermelho brilhante, com borda amarela
- **Mao**: Mantida, aura expandida (4x4px)
- **Corpo**: Leve levitacao (2px acima do chao)
- **Toga**: Esvoaca para cima (vento de poder)
- **Careca**: BRILHO VERMELHO MAXIMO
- **Chao**: Tremendo (linhas irregulares)

### Frame 4 - "CENSURADO" Gigante Aparece
- **Raios dos olhos**: Convergem em ponto a frente
- **Texto "CENSURADO"**: GIGANTE - ocupa area acima do sprite, vermelho brilhante
- **Letras**: Estilo carimbo, inclinadas, com borda preta grossa
- **Corpo**: Flutuando 3px do chao
- **Toga**: Totalmente esvoaca, quase horizontal
- **Mao**: Punho cerrado agora (mudou de "pare" para "decretado")
- **Onda**: Onda sonora visivel saindo do "CENSURADO" (arcos concentricos)

### Frame 5 - Expansao do Efeito
- **"CENSURADO"**: Expande e pulsa (maior que frame anterior)
- **Onda de silencio**: Se propaga em todas direcoes (arcos maiores)
- **Corpo**: Descendo de volta ao chao
- **Olhos**: Raios diminuindo
- **Toga**: Comecando a assentar
- **Area de efeito**: Indicador visual de 5-tile radius (borda vermelha semi-transparente)
- **Particulas**: Letras "C", "E", "N" voando como estilhacos

### Frame 6 - Conclusao
- **"CENSURADO"**: Pulsando fraco, desaparecendo
- **Corpo**: Pousa completamente
- **Olhos**: Voltam ao vermelho normal
- **Postura**: Bracos cruzados, sorriso arrogante
- **Careca**: Brilho voltando ao branco
- **Toga**: Assentada mas levemente fumegante
- **Efeito residual**: Leve glow vermelho persistente no chao da area afetada

---

## 7. SPECIAL - Xandaquistao (8 Frames)

**Arquivo**: `xandao-special-xandaquistao.png` (512x64 - 8 frames de 64x64)
**Frame rate**: 8 fps
**Loop**: Nao
**Efeito gameplay**: Cria zona de controle por duracao limitada
**Sensacao**: Ditadura instaurada, territorio conquistado, poder territorial

### Frame 1 - Declaracao
- **Corpo**: Postura imperial, queixo empinado
- **Martelo**: Erguido como cetro (vertical, acima da cabeca)
- **Olhos**: Brilho dourado (nao vermelho - poder DIFERENTE)
- **Boca**: Aberta, gritando "XANDAQUISTAO!"
- **Toga**: Comeca a mudar - bordas ficando douradas
- **Careca**: Brilho dourado

### Frame 2 - Cravo no Chao
- **Martelo**: DESCE com forca total, cravando no chao
- **Impacto**: Explosao de particulas douradas/vermelhas no ponto
- **Chao**: Rachadura em estrela, MAIOR que no attack normal
- **Corpo**: Inclinado para frente pelo esforco
- **Toga**: Esvoaca violentamente
- **Onda**: Onda sismica saindo do ponto de impacto

### Frame 3 - Zona Comecando a Formar
- **Chao**: Circulo de influencia comeca a se formar (borda dourada expandindo)
- **Martelo**: Fincado no chao, vibrando
- **Corpo**: Se endireitando, bracos abertos
- **Particulas**: Poeira dourada subindo do chao ao redor
- **Toga**: Transformando - faixas douradas aparecendo

### Frame 4 - Bandeiras Surgindo
- **Zona**: Circulo 50% formado
- **Bandeiras**: 2 bandeiras surgem nas laterais do sprite - bandeiras vermelhas com X CORTADO (nao logo do Twitter - X generico riscado)
- **Corpo**: Postura de conquista, olhos dourados intensos
- **Chao dentro da zona**: Muda de cor (mais escuro, vermelho-marrom)
- **Toga**: Agora com detalhes dourados claros

### Frame 5 - Zona Expandindo
- **Zona**: 75% formada, borda dourada brilhante
- **Bandeiras**: 4 bandeiras agora, ondulando
- **Chao**: Totalmente transformado dentro da zona
- **Corpo**: Flutuando 2px, aura de poder
- **Particulas**: Mais intensas, douradas e vermelhas
- **Martelo**: Brilhando no centro, ancora da zona

### Frame 6 - Zona Completa
- **Zona**: 100% formada - borda dourada solida
- **Interior**: Chao vermelho-escuro, textura diferente (ladrilho? padrao?)
- **Bandeiras**: 4 bandeiras em posicoes cardinais dentro da zona
- **Corpo**: Pousa dentro da zona, agora com toga TRANSFORMADA (mais militar)
- **Olhos**: Voltando a vermelho, dourado esvaindo
- **Martelo**: Arranca do chao, volta para a mao

### Frame 7 - Ativacao dos Efeitos
- **Zona**: Pulsa (borda expande/contrai 1px)
- **Efeito interior**: Ondulacoes no chao (linhas mostrando campo de forca)
- **Inimigos na zona**: Indicador visual de lentidao (linhas de velocidade invertidas)
- **Corpo**: Patrulhando dentro da zona, pose de guarda
- **Expressao**: Sorriso cruel, satisfacao territorial
- **Bandeiras**: Ondulando continuamente

### Frame 8 - Estado Sustentado
- **Zona**: Ativa, pulsando levemente
- **Corpo**: Postura de vigia, martelo no ombro
- **Expressao**: Dominacao total, olhos varrendo
- **Toga**: Versao militar estabilizada
- **Efeito**: Frame que loopa enquanto a zona esta ativa
- **Particulas reduzidas**: Apenas leve glow na borda da zona

---

## 8. SPECIAL - Apagao Digital / Ultimate (6 Frames)

**Arquivo**: `xandao-special-apagao.png` (384x64 - 6 frames de 64x64)
**Frame rate**: 10 fps
**Loop**: Nao
**Efeito gameplay**: "Desliga a internet" do jogo por 3 segundos (HUD desaparece, tela escurece, static)
**Sensacao**: CAOS ABSOLUTO, queda do sistema, "EU DESLIGO O QUE EU QUISER"

### Frame 1 - Ergue a Mao do Poder
- **Corpo**: Postura IMPONENTE, peito estufado
- **Mao direita**: Levantada, dedo indicador apontando para cima
- **Martelo**: Na mao esquerda, apoiado no chao
- **Olhos**: Brilho branco-azulado (eletricidade, nao vermelho)
- **Careca**: Reflexo azulado (como tela de computador)
- **Toga**: Eletricidade estatica percorrendo (linhas finas branco-azuladas)
- **Expressao**: Sorriso MALIGNO, "eu vou desligar tudo"
- **Ambiente**: Leve escurecimento ao redor

### Frame 2 - Eletricidade Concentra
- **Mao levantada**: Esfera de eletricidade se forma na ponta do dedo (4x4px, branco-azul)
- **Arcos eletricos**: Saindo do corpo para a esfera (linhas zigzag finas)
- **Careca**: BRILHA AZUL forte
- **Olhos**: Totalmente brancos (sem pupila)
- **Toga**: Ondula com campo eletromagnetico
- **Ambiente**: Mais escuro, particulas eletronicas (pixels coloridos como static de TV)
- **Martelo**: Eletricidade percorrendo o cabo

### Frame 3 - DISPARO / Tela "Erro de Conexao"
- **Mao**: DESCE violentamente, esfera dispara para cima
- **Corpo**: Pose de poder total, inclinado para tras
- **SOBREPOSICAO NA TELA**: Icone de "sem internet" comeca a aparecer (wifi com X)
- **Eletricidade**: Explode em todas direcoes a partir da esfera
- **Ambiente**: Escurece DRASTICAMENTE
- **Particulas**: Pixels de static INTENSOS
- **Toga**: Levanta com a forca do disparo

### Frame 4 - Static Total
- **TELA INTEIRA**: Coberta por static de TV (padrao de pixels aleatorios preto/branco/cores)
- **Xandao**: VISIVEL APENAS como silhueta escura no centro do static
- **Careca**: Unico ponto de brilho (azul) na silhueta
- **Texto**: "CONEXAO PERDIDA" ou "SEM SINAL" piscando
- **Efeito sonoro visual**: Barras de "no signal" nas bordas
- **Este frame**: Representa o momento que a HUD some e o jogador fica cego

### Frame 5 - Sustentando o Apagao
- **Static**: Levemente reduzido, mas ainda intenso
- **Silhueta do Xandao**: Mais visivel, rindo (boca aberta)
- **Olhos**: 2 pontos vermelhos brilhantes na silhueta (UNICA cor viva)
- **Texto**: Alternando entre "CENSURADO" e "SEM SINAL"
- **Bordas da tela**: Linhas de scanline horizontais (efeito CRT)
- **Duracao**: Este e o frame 3 representam o periodo de 3s de apagao

### Frame 6 - Volta / Recuperacao
- **Static**: Dissipando rapidamente (pixels sumindo)
- **Xandao**: Voltando a ser visivel completamente
- **Postura**: Bracos cruzados, sorriso de satisfacao
- **Careca**: Voltando a brilho branco normal
- **Olhos**: Voltando a vermelho padrao
- **Toga**: Assentando, leve fumaca de eletricidade residual
- **Ambiente**: Clareia gradualmente
- **Particulas residuais**: Ultimos pixels de static desaparecendo
- **Expressao**: "Viram? Eu posso desligar tudo."

---

## PROJETEIS E EFEITOS SEPARADOS (32x32px)

### Projetil: Multa do X
**Arquivo**: `xandao-proj-multa.png` (128x32 - 4 frames de 32x32)
- **Frame 1**: Icone do X/Twitter com cifrao ($) sobreposto, girando
- **Frame 2**: Rotacao 90 graus, brilho vermelho
- **Frame 3**: Rotacao 180 graus, particulas de dinheiro voando
- **Frame 4**: Rotacao 270 graus, trail de "R$" atras

### Projetil: Raio do Olho
**Arquivo**: `xandao-proj-raio.png` (64x32 - 2 frames de 32x32)
- **Frame 1**: Feixe vermelho horizontal, brilhante, borda amarela
- **Frame 2**: Feixe pulsando (ligeiramente maior), cor mais intensa

### Efeito: Texto CENSURADO
**Arquivo**: `xandao-fx-censurado.png` (96x32 - 3 frames de 32x32)
- **Frame 1**: Texto "CENSURADO" aparecendo (fade in), estilo carimbo vermelho
- **Frame 2**: Texto pulsando, borda expandindo
- **Frame 3**: Texto desaparecendo (fade out), letras se fragmentando

### Efeito: Rachadura no Chao
**Arquivo**: `xandao-fx-rachadura.png` (64x32 - 2 frames de 32x32)
- **Frame 1**: Rachadura aparecendo (linhas finas escuras em padrao estrela)
- **Frame 2**: Rachadura expandida, poeira subindo

### Efeito: Static/Apagao (Overlay)
**Arquivo**: `xandao-fx-static.png` (128x32 - 4 frames de 32x32, tileable)
- **Frame 1-4**: Padroes diferentes de static de TV (para tile na tela toda)
- Deve ser tileable horizontalmente e verticalmente

---

## ICONE DO BOSS (UI)

### Retrato para HUD
**Arquivo**: `xandao-portrait.png` (32x32, frame unico)
- Close-up do rosto: careca brilhante, sobrancelha franzida, olhos vermelhos
- Fundo: vermelho escuro com textura de toga
- Borda: dourada, estilo brasao

### Icone da Barra de HP
**Arquivo**: `xandao-hp-icon.png` (16x16, frame unico)
- Mini careca brilhante com olhos vermelhos
- Fundo transparente
- Usado na barra de vida do boss

---

## NOTAS PARA O ARTISTA

### Paleta de Cores Exata (Hex)
| Cor | Hex | Uso |
|---|---|---|
| Toga Preta | #1a1a1a | Base da toga |
| Toga Sombra | #0d0d0d | Sombras da toga |
| Toga Dobra | #2a2a2a | Dobras iluminadas |
| Pele Base | #8B6914 | Tom de pele |
| Pele Sombra | #6B4F10 | Sombras de pele |
| Pele Highlight | #A67C1A | Highlights de pele |
| Careca Brilho | #FFFFFF | Highlight principal da careca |
| Careca Glow | #FFFACD | Glow secundario da careca |
| Olho Vermelho | #FF0000 | Iris/brilho dos olhos |
| Olho Raio | #FF3333 | Raios dos olhos |
| Raio Borda | #FFD700 | Borda dos raios |
| Veia | #8B0000 | Veias (escuro) |
| Veia Pulsando | #CC0000 | Veias (ativo) |
| Martelo Cabo | #4A3728 | Madeira do cabo |
| Martelo Metal | #808080 | Cabeca do martelo |
| Martelo Brilho | #C0C0C0 | Highlight do martelo |
| Texto Censurado | #CC0000 | Inscricao no martelo / texto voador |
| Dourado Zona | #DAA520 | Zona Xandaquistao |
| Eletricidade | #00BFFF | Apagao Digital |
| Static | #808080 | Base do static |
| Bandeira Fundo | #8B0000 | Fundo das bandeiras |
| Papel Inquerito | #F5F5DC | Papeis na animacao de death |

### Regras de Pixel Art
1. **SEM anti-aliasing** - bordas duras sempre, estilo retro
2. **Dithering PERMITIDO** - para transicoes de sombra na toga e pele
3. **Outline preto obrigatorio** - 1px de contorno escuro em tudo
4. **Assimetria proposital** - nada deve ser perfeitamente simetrico (grotesco)
5. **Exagero de proporcoes** - cabeca 30% maior que real, martelo 200% maior que real
6. **Shading limitado** - maximo 3 tons por material (base, sombra, highlight)
7. **Transparencia** - fundo SEMPRE alpha 0, sem halo
8. **Referencia de tamanho**: Xandao deve parecer 1.5x maior que zumbis normais em sprite
