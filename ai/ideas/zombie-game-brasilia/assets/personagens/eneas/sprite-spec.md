# ENEAS CARNEIRO (O Fantasma Patriota) -- Sprite Specification

## Overview
- **Tipo**: NPC Lendario / Easter Egg
- **Sprite Dimensions**: 64x64px (personagem)
- **Sprite Sheet Layout**: Horizontal strip, 1 row por ciclo de animacao
- **Formato**: PNG com alpha transparency (CRITICO: multiplas camadas de transparencia para efeito holograma)
- **Anchor Point**: Bottom-center (32, 60)
- **Framerate**: 8-10fps (estilo jerky, porem com suavidade UNICA para este personagem -- a reverencia exige um toque menos grotesco que os demais)

> **NOTA FUNDAMENTAL**: Eneas e o UNICO personagem tratado com REVERENCIA. O estilo Andre Guedes se aplica, mas com DIGNIDADE. As deformacoes grotescas sao MINIMAS comparadas aos outros personagens. A deformidade principal (bigode com vida propria) e tratada com respeito comico, nao escarnio. Eneas e SAGRADO.

---

## Efeito Holograma -- Especificacao Tecnica

O efeito de holograma/fantasma e a MARCA VISUAL do Eneas. Todos os frames devem implementar:

### Camadas de Renderizacao (bottom to top)
1. **Aura Dourada** (background): Brilho difuso `#D4A017` alpha 15-25% ao redor da silhueta. Pulsa a cada 4 frames (15% -> 20% -> 25% -> 20% -> repete). Raio: 4-6px alem do corpo.
2. **Corpo Principal** (midground): O sprite do Eneas com alpha global entre 55-75%. NUNCA opaco. A transparencia oscila: 55% -> 65% -> 75% -> 65% -> 55% (ciclo de 5 frames sobrepostos ao ciclo principal).
3. **Scanlines** (overlay): Linhas horizontais de 1px a cada 3px verticais. Cor `#FFFFFF` alpha 8%. Deslocam 1px para baixo a cada frame (efeito de TV velha / holograma sci-fi).
4. **Brilho Branco** (highlight): Edge glow de 1px ao redor do contorno do corpo. Cor `#F0F0E8` alpha 30%. Pisca a cada 6 frames.
5. **Particulas Douradas** (foreground): 3-5 particulas flutuantes de 1x1px a 2x2px. Cor `#FFD700` alpha 40-70%. Sobem lentamente ao redor do corpo. Independentes do ciclo de animacao.

### Palette do Holograma

| Elemento | Hex + Alpha | Uso |
|---|---|---|
| Corpo translucido (base) | `#E8E0D0` alpha 65% | Terno branco fantasmagorico |
| Corpo translucido (sombra) | `#B0A890` alpha 50% | Dobras do terno, sombras |
| Corpo translucido (highlight) | `#F5F0E8` alpha 75% | Topo dos ombros, testa |
| Pele fantasma | `#D4B896` alpha 60% | Rosto, maos |
| Pele fantasma (sombra) | `#A08060` alpha 45% | Bochechas, queixo, dobras |
| Bigode PRINCIPAL | `#3A2A1A` alpha 80% | O bigode e a parte MAIS OPACA -- ele transcende o plano espiritual |
| Bigode highlight | `#5A4A3A` alpha 70% | Reflexos do bigode |
| Aura dourada interna | `#D4A017` alpha 25% | Glow ao redor do torso |
| Aura dourada externa | `#FFD700` alpha 12% | Glow externo difuso |
| Bandeira verde | `#009739` alpha 50% | Capa/bandeira -- verde |
| Bandeira amarelo | `#FEDD00` alpha 50% | Capa/bandeira -- losango |
| Bandeira azul | `#002776` alpha 50% | Capa/bandeira -- circulo |
| Bandeira branco | `#F0F0E8` alpha 55% | Capa/bandeira -- faixa |
| Scanline | `#FFFFFF` alpha 8% | Linhas horizontais de TV |
| Edge glow | `#F0F0E8` alpha 30% | Contorno brilhante |
| Particula dourada | `#FFD700` alpha 50% | Particulas flutuantes |
| Outline principal | `#1A1A1A` alpha 50% | Contorno do corpo (mais suave que outros personagens) |
| Outline bigode | `#1A1A1A` alpha 75% | Contorno do bigode (mais forte) |
| "56" projetil | `#FFD700` alpha 90% | Numero 56 como projetil |
| "56" outline | `#8B0000` alpha 85% | Contorno do projetil 56 |
| Rachadura tela | `#F0F0E8` alpha 90% | Linhas de rachadura no ultimate |

---

## Proporcoes do Personagem

Eneas segue as proporcoes do style guide (cabeca 1.5x, corpo atarracado ~5 cabecas) MAS com ajustes de DIGNIDADE:

- **Cabeca**: ~14x16px. Ligeiramente menos grotesca que outros personagens. Cabelos curtos grisalhos. Testa ampla.
- **Bigode**: ~18x8px (ULTRAPASSA a largura da cabeca!). O bigode e ENORME, farfalhudo, espesso. E a feature dominante. Ocupa quase 1/3 da largura total do sprite. Tem contorno MAIS OPACO que o resto do corpo (alpha 75-80% vs 60-65% do corpo).
- **Torso**: ~20x18px. Terno branco brilhante, ligeiramente translucido. Lapela visivel. Postura ERETA -- Eneas nao se curva.
- **Capa/Bandeira**: ~24x30px (flui atras e abaixo do corpo). Bandeira do Brasil esvoaçante. Movimento independente. Mais transparente que o corpo (alpha 45-55%).
- **Pernas**: ~16x16px. Calca branca do terno. Sapatos formais.
- **Maos**: 4x4px cada. Gesticulam com autoridade.

---

## Frame-by-Frame -- IDLE (4 frames, loop)

### Frame 0: `eneas_idle_01.png` (0,0 a 63,63)
**Descricao**: Eneas parado, postura militar ereta. Bracos ao lado do corpo, levemente afastados. O bigode aponta PARA FRENTE, simetrico, em posicao neutra. A capa/bandeira pende atras, levemente esvoaçante para a direita (como brisa suave). Aura dourada no nivel minimo (alpha 15%). Scanlines visiveis. O corpo pulsa em alpha 60%. Particulas douradas: 3 particulas subindo lentamente nos lados.
**Bigode**: Simetrico, pontas retas apontando para os lados. Ligeira curvatura para cima nas pontas. Relaxado.
**Expressao**: Sereno. Olhos semicerrados com dignidade. Boca oculta pelo bigode.

### Frame 1: `eneas_idle_02.png` (64,0 a 127,63)
**Descricao**: Micro-flutuacao para cima (corpo sobe 1px -- fantasmas nao tocam o chao firmemente). O bigode comeca a se mover: ponta direita sobe 1px, ponta esquerda desce 1px (movimento de "respiracao" do bigode). Capa flui 1px mais para a direita. Aura dourada sobe para alpha 20%. Alpha do corpo: 65%.
**Bigode**: Assimetrico. Ponta direita aponta levemente para cima, esquerda levemente para baixo. Microondulacao.
**Expressao**: Olhos se abrem levemente. Sobrancelhas sobem 1px.

### Frame 2: `eneas_idle_03.png` (128,0 a 191,63)
**Descricao**: Corpo no ponto mais alto da flutuacao (+2px do chao). O bigode inverte: ponta esquerda sobe, direita desce. Capa flui de volta para o centro, com ondulacao no tecido (2-3 pixels de diferenca na borda inferior). Aura dourada no maximo: alpha 25%. Alpha do corpo: 70%. Edge glow pisca (frame ON).
**Bigode**: Invertido do frame anterior. Ponta esquerda para cima, direita para baixo. O bigode parece "respirar".
**Expressao**: Olhos semicerrados novamente. Uma piscada sutil? NAO -- Eneas raramente pisca. Mantém o olhar fixo.

### Frame 3: `eneas_idle_04.png` (192,0 a 255,63)
**Descricao**: Corpo desce de volta (-1px, agora +1px do chao). O bigode retorna a posicao quase simetrica, com micro-tremor nas pontas (1px de variacao). Capa flui para a esquerda agora (direção alternada). Aura dourada: alpha 20% (descendo). Alpha do corpo: 65%. Edge glow OFF.
**Bigode**: Quase simetrico. Micro-tremor de 1px nas pontas. A "vida propria" e sutil no idle.
**Expressao**: Retorna ao sereno do Frame 0. Ciclo completo.

**Sprite Sheet IDLE**: 256x64px (4 frames)

---

## Frame-by-Frame -- WALK / FLUTUACAO (6 frames, loop)

Eneas NAO anda. Ele FLUTUA. Os pes ficam 2-4px acima do chao. O movimento e de deslizamento espectral.

### Frame 0: `eneas_walk_01.png`
**Descricao**: Corpo inclinado 3-5 graus na direcao do movimento. Pes juntos, 3px acima do chao. Rastro fantasmagorico: versao afterimage do corpo com alpha 20% na posicao anterior (2px atras). Bigode aponta na direcao do movimento (como bussola). Capa flui na direcao OPOSTA ao movimento (arrasto). Aura dourada forma um rastro sutil.
**Bigode**: APONTA na direcao do movimento como uma bussola magnetica. Ambas as pontas viram para onde ele vai.

### Frame 1: `eneas_walk_02.png`
**Descricao**: Corpo avanca. O afterimage do frame anterior permanece com alpha 10% (desbotando). Novo afterimage se forma. Bigode continua apontando. A capa ondula mais intensamente. Particulas douradas deixam rastro.
**Bigode**: Pontas oscilam levemente com o "vento" do movimento, mas mantem a direcao geral.

### Frame 2: `eneas_walk_03.png`
**Descricao**: Ponto maximo de velocidade visual. Afterimage mais longo (3px atras). O corpo atinge alpha 75% (mais visivel em movimento rapido). Scanlines parecem acelerar (deslocamento de 2px por frame em vez de 1px). Capa totalmente esticada para tras.
**Bigode**: Pontas vibram. Uma das pontas esta 2px a frente da outra (aerodinamica fantasma).

### Frame 3: `eneas_walk_04.png`
**Descricao**: Espelho do Frame 1. Inicio de desaceleracao visual. Afterimage diminui.
**Bigode**: Volta a alinhar as pontas. Micro-tremor.

### Frame 4: `eneas_walk_05.png`
**Descricao**: Espelho do Frame 0 com variacao: os bracos agora gesticulam levemente (mao direita sobe 2px).
**Bigode**: Quase simetrico novamente.

### Frame 5: `eneas_walk_06.png`
**Descricao**: Transicao para loop. Bracos retornam. Afterimage se dissolve completamente. Corpo alpha 60% (retorno ao padrao).
**Bigode**: Posicao neutra, pronto para re-loop.

**Sprite Sheet WALK**: 384x64px (6 frames)

---

## Frame-by-Frame -- APARICAO / SPAWN (8 frames, NAO loop -- toca uma vez)

A aparicao do Eneas e um EVENTO. Distorcao da realidade. Reverencia obrigatoria.

### Frame 0: `eneas_spawn_01.png`
**Descricao**: Tela normal. Nenhum Eneas visivel. Apenas um ponto de luz dourada de 2x2px no centro do frame. Uma UNICA particula dourada piscando.
**Efeito**: O ponto de luz aparece onde Eneas vai se materializar.

### Frame 1: `eneas_spawn_02.png`
**Descricao**: O ponto expande para um circulo de luz dourada de 8x8px. Scanlines comecam a aparecer no circulo. Uma vaga silhueta (shadow outline de 1px) do bigode -- so o bigode -- comeca a se formar DENTRO do circulo. O bigode se materializa ANTES do corpo.
**Efeito**: Distorcao visual: pixels ao redor do circulo tremem 1px.

### Frame 2: `eneas_spawn_03.png`
**Descricao**: Circulo de luz expande para 20x20px. O bigode agora e claramente visivel (alpha 40%) flutuando sem rosto. Uma forma vaga de cabeca comeca a se delinear atras do bigode. Ondulacoes concentricas de luz saem do centro (2 aneis de 1px dourado, alpha 20%).
**Efeito**: Pixels no raio de 16px do centro tremem 1px aleatoriamente.

### Frame 3: `eneas_spawn_04.png`
**Descricao**: A cabeca e o torso superior se materializam (alpha 35%). O bigode ja esta em alpha 60%. A capa/bandeira comeca a surgir como ondulacoes de cor por tras do torso. O circulo de luz se transforma em aura ao redor do corpo. Linhas de distorcao verticais (como interferencia de TV) nos 16px mais proximos.
**Efeito**: Tudo ao redor treme. A realidade "aceita" a presenca do Eneas com relutancia.

### Frame 4: `eneas_spawn_05.png`
**Descricao**: Corpo quase completo (alpha 50%). Pernas se formam de cima para baixo. O bigode em alpha 70%. A aura dourada expande ao maximo (8px raio). A capa comeca a esvoaçar. NESTE FRAME: todos os outros personagens na tela fazem uma pausa de 1 frame (efeito "O Verdadeiro Patriota").
**Efeito**: Flash branco sutil na tela inteira (alpha 5%). A reverencia comeca.

### Frame 5: `eneas_spawn_06.png`
**Descricao**: Corpo completo (alpha 55%). Eneas se torna totalmente visivel pela primeira vez. Postura ereta, militar. O bigode assume alpha 80% (quase solido). A capa flui. Particulas douradas EXPLODEM do centro (8-12 particulas saindo em todas as direcoes).
**Efeito**: Os NPCs proximos param completamente e OLHAM para o Eneas.

### Frame 6: `eneas_spawn_07.png`
**Descricao**: Alpha se estabiliza (corpo 65%, bigode 80%). A explosao de particulas se acalma (particulas continuam flutuando, mas em velocidade normal). A aura reduz para nivel padrao. Eneas levanta o queixo levemente (pose de dignidade).
**Efeito**: Som de "MEU NOME E ENEAS!" dispara aqui.

### Frame 7: `eneas_spawn_08.png`
**Descricao**: Frame de transicao para idle. Tudo se estabiliza nos valores padrao de idle. O bigode faz um ultimo flutter dramatico (pontas sobem 2px e descem). Pronto para acao.
**Efeito**: O jogo retorna ao normal. A reverencia acabou.

**Sprite Sheet SPAWN**: 512x64px (8 frames)

---

## Frame-by-Frame -- ATAQUE: Grito Patriota (4 frames)

Eneas grita "MEU NOME E ENEAS!" -- ondas sonoras visiveis causam dano.

### Frame 0: `eneas_grito_01.png`
**Descricao**: Eneas puxa ar. Torso expande 2px (peito inflando). Bigode se comprime (pontas vao para frente, preparando). Boca (normalmente oculta) comeca a se revelar atras do bigode -- o bigode se LEVANTA levemente. Aura concentra-se (raio diminui, alpha aumenta para 30%).

### Frame 1: `eneas_grito_02.png`
**Descricao**: BOCA ABERTA. O bigode se ergue completamente para cima (posicao impossivel -- as pontas apontam para o ceu a 45 graus). A boca e visivel pela primeira vez: enorme, exagerada, ocupa metade da cabeca. Ondas sonoras saem da boca: 3 arcos concentricos de 1px, cores alternando `#FFD700` e `#F0F0E8`, alpha 60%. As ondas comecam a 4px da boca.

### Frame 2: `eneas_grito_03.png`
**Descricao**: PICO DO GRITO. O texto "ENEAS!" aparece nas ondas sonoras (letras formadas pelas proprias ondas de choque). O bigode vibra violentamente (blur de 2px). O corpo inteiro brilha mais opaco (alpha 80% -- quase corporeo de tanta intensidade). Ondas se expandem para 16px da boca. Particulas douradas sao EMPURRADAS pelas ondas. A capa esvoaça na direcao oposta (soprada pelo grito).

### Frame 3: `eneas_grito_04.png`
**Descricao**: Aftershock. Ondas passaram. O bigode desce lentamente para a posicao normal. Boca se fecha. Alpha retorna para 65%. Particulas desaceleradas. Ecos visuais: 1 onda residual com alpha 20% se dissipando.

**Sprite Sheet GRITO**: 256x64px (4 frames)

---

## Frame-by-Frame -- ATAQUE: Projetil "56!" (4 frames para o spawn, 4 para o voo)

### Spawn do Numero (4 frames, 64x64px)

### Frame 0: `eneas_56_spawn_01.png`
**Descricao**: Eneas estende a mao direita para frente. No centro da palma, um ponto de luz dourada de 2x2px. O bigode aponta na direcao do alvo (bussola).

### Frame 1: `eneas_56_spawn_02.png`
**Descricao**: O numero "5" comeca a se formar na mao (feito de energia dourada, alpha 50%). O "6" comeca logo ao lado. Ambos em construcao -- pixels se montando de baixo para cima. Tamanho parcial: 8x12px.

### Frame 2: `eneas_56_spawn_03.png`
**Descricao**: "56" completo. Fonte grossa, bloco, estilo carimbo (nao typeset). Tamanho: 16x12px. Cor `#FFD700` com outline `#8B0000` de 1px. Alpha 90%. Brilha intensamente. O "56" flutua a 4px da mao.

### Frame 3: `eneas_56_spawn_04.png`
**Descricao**: Eneas empurra o "56" com um gesto de mao. O numero sai voando na direcao apontada pelo bigode. Linhas de velocidade (3 rastros brancos). Flash de luz na mao. O bigode recua pelo impacto (pontas vao 2px para tras).

### Projetil "56" em voo (4 frames, 32x32px, LOOP)

### Frame 0: `projetil_56_flight_01.png` (32x32px)
**Descricao**: "56" voando. Orientacao normal (numeros legiveis). Rotacao: 0 graus. Aura dourada de 2px ao redor. 2 linhas de velocidade atras (1px branco alpha 60%). O "5" e o "6" pulsam levemente (alpha oscila 80-95%).

### Frame 1: `projetil_56_flight_02.png` (32x32px)
**Descricao**: "56" rotacionado 15 graus (leve inclinacao). Aura pulsa: alpha 20% (frame fraco). Uma particula dourada se solta (debris do projetil). Linhas de velocidade se esticam.

### Frame 2: `projetil_56_flight_03.png` (32x32px)
**Descricao**: "56" rotacionado -15 graus (balanco na direcao oposta -- o numero oscila enquanto voa). Aura pulsa: alpha 30% (frame forte). Mais particulas. Trail dourado de 4px atras.

### Frame 3: `projetil_56_flight_04.png` (32x32px)
**Descricao**: "56" retorna a 0 graus. Frame identico ao Frame 0 com microvariacoes (particulas em posicoes diferentes). Loop completo.

**Sprite Sheet 56-SPAWN**: 256x64px (4 frames de 64x64)
**Sprite Sheet 56-FLIGHT**: 128x32px (4 frames de 32x32)

---

## Frame-by-Frame -- DESAPARICAO / DESPAWN (6 frames, NAO loop)

### Frame 0: `eneas_despawn_01.png`
**Descricao**: Eneas levanta o queixo. Olhar para cima. Aura comeca a intensificar (alpha 30%).

### Frame 1: `eneas_despawn_02.png`
**Descricao**: O corpo comeca a se dissolver de BAIXO PARA CIMA. Pes desaparecem (alpha 0%). Pernas ficam alpha 30%. Particulas douradas SOBEM do corpo (subindo como cinzas de fogueira). Bigode permanece alpha 80%.

### Frame 2: `eneas_despawn_03.png`
**Descricao**: Dissolucao ate a cintura. Torso inferior alpha 20%. Torso superior alpha 40%. A capa se desfaz em fios de luz dourada que sobem. Bigode alpha 75%. Muitas particulas subindo.

### Frame 3: `eneas_despawn_04.png`
**Descricao**: So resta a cabeca e o bigode flutuando. O corpo virou particulas douradas subindo. Rosto alpha 35%. Bigode alpha 65%. A silhueta do terno e visivel como contorno ghost (1px alpha 10%).

### Frame 4: `eneas_despawn_05.png`
**Descricao**: So o bigode. Literalmente SO O BIGODE flutuando no ar, alpha 50%. As particulas do rosto ainda sobem. Um ultimo flash de aura dourada.

### Frame 5: `eneas_despawn_06.png`
**Descricao**: O bigode se dissolve em particulas douradas finais. Alpha 15%. As particulas se dispersam. Um echo visual: a silhueta completa do Eneas aparece por 1 frame como afterimage alpha 5%, e desaparece. Saudade.

**Sprite Sheet DESPAWN**: 384x64px (6 frames)

---

## Frame-by-Frame -- ULTIMATE: "MEU NOME E ENEAS!" (10 frames, NAO loop, UNICA por partida)

Este e um evento CINEMATICO. O sprite de 64x64 e insuficiente -- o ultimate usa um sprite ESPECIAL de 256x256px para o rosto gigante, mais efeitos full-screen controlados pelo engine.

### Frame 0: `eneas_ult_01.png` (64x64)
**Descricao**: Eneas no chao. HP < 10%. Corpo MAIS translucido que o normal (alpha 40%). O bigode BRILHA -- alpha 90%. Eneas levanta os bracos.

### Frame 1: `eneas_ult_02.png` (64x64)
**Descricao**: Eneas comeca a subir. Flutua 8px acima do normal. Aura EXPLODE (raio 12px, alpha 40%). A capa se abre como asas. Particulas douradas em TODAS as direcoes.

### Frame 2: `eneas_ult_03.png` (256x256 -- ROSTO GIGANTE)
**Descricao**: TRANSICAO. O rosto do Eneas PREENCHE todo o frame de 256x256. Olhos serios, determinados. Bigode ENORME ocupa 1/3 inferior do frame. Fundo: ceu laranja-sangue do jogo (#FF6B35 -> #8B0000). O rosto e holografico (scanlines, alpha variavel, brilho dourado). A palavra "ENEAS" comeca a se formar atras do rosto em letras gigantes douradas.

### Frame 3: `eneas_ult_04.png` (256x256)
**Descricao**: O rosto atinge MAXIMO BRILLO. Alpha do rosto: 85% (quase solido -- o fantasma se torna QUASE real por pura forca de vontade). A boca se ABRE. O bigode se ERGUE. As letras "ENEAS" atras estao completas e brilhando. Rachadura #1 aparece na tela: uma linha diagonal de `#F0F0E8` alpha 90% cruzando o canto superior esquerdo.

### Frame 4: `eneas_ult_05.png` (256x256)
**Descricao**: "MEU NOME E..." -- ondas sonoras MASSIVAS saem da boca. Circulos concentricos de energia dourada. Rachadura #2 e #3 aparecem: mais linhas cruzando a tela. Fragmentos de "vidro" comecam a se desprender nas bordas das rachaduras (triangulos de 2-4px, `#F0F0E8` alpha 70%).

### Frame 5: `eneas_ult_06.png` (256x256)
**Descricao**: "...ENEAS!" -- PICO. A tela RACHA completamente. 8-12 linhas de rachadura irradiam do centro (da boca). Fragmentos voam. A imagem do rosto TREME (shake de 2px). Ondas sonoras atingem as bordas do frame. O bigode vibra com intensidade maxima. Flash branco full-screen (alpha 30%).

### Frame 6: `eneas_ult_07.png` (256x256)
**Descricao**: Aftermath. A tela esta rachada (rachaduras permanecem como overlay estatico). O rosto comeca a fade out (alpha 70%). As ondas se dissipam. Fragmentos de vidro flutuam e caem lentamente. O bigode ainda vibra.

### Frame 7: `eneas_ult_08.png` (256x256)
**Descricao**: O rosto dissolve para alpha 40%. As rachaduras na tela comecam a se "curar" -- os fragmentos voltam lentamente para seus lugares. A aura dourada diminui. O bigode para de vibrar.

### Frame 8: `eneas_ult_09.png` (256x256 -> transicao para 64x64)
**Descricao**: O rosto gigante encolhe rapidamente (efeito zoom out). As rachaduras se fecham ~70%. O sprite retorna ao tamanho normal (64x64). Eneas flutua no centro, alpha 55%, exausto mas DIGNO.

### Frame 9: `eneas_ult_10.png` (64x64)
**Descricao**: Eneas de volta ao tamanho normal. Postura ereta. As ultimas rachaduras se fecham (overlay). Aura minima. O bigode faz um ultimo flutter. Todos os inimigos na tela tem o debuff "respeito" (efeito visual: alpha deles reduzido 20%, velocidade reduzida). O Eneas faz um aceno minimo com a cabeca. Dignidade.

**Sprite Sheet ULTIMATE**: Composicao mista:
- `eneas_ult_ground.png`: 128x64px (frames 0-1, tamanho 64x64)
- `eneas_ult_face.png`: 1792x256px (frames 2-8, tamanho 256x256)
- `eneas_ult_return.png`: 64x64px (frame 9, tamanho 64x64)
- `eneas_ult_crack_overlay.png`: 256x256px (overlay de rachaduras, 4 frames de progressao)

---

## Sprite Sheet Summary -- Todas as Animacoes

| Sheet | Ciclo | Frames | Frame Size | Sheet Size | Loop? |
|---|---|---|---|---|---|
| `eneas_idle` | Idle / Flutuacao parado | 4 | 64x64 | 256x64 | Sim |
| `eneas_walk` | Flutuacao / Movimento | 6 | 64x64 | 384x64 | Sim |
| `eneas_spawn` | Aparicao | 8 | 64x64 | 512x64 | Nao |
| `eneas_grito` | Grito Patriota (ataque) | 4 | 64x64 | 256x64 | Nao |
| `eneas_56_spawn` | Spawn do projetil 56 | 4 | 64x64 | 256x64 | Nao |
| `eneas_56_flight` | Projetil 56 em voo | 4 | 32x32 | 128x32 | Sim |
| `eneas_despawn` | Desaparicao | 6 | 64x64 | 384x64 | Nao |
| `eneas_ult_ground` | Ultimate (chao) | 2 | 64x64 | 128x64 | Nao |
| `eneas_ult_face` | Ultimate (rosto gigante) | 7 | 256x256 | 1792x256 | Nao |
| `eneas_ult_return` | Ultimate (retorno) | 1 | 64x64 | 64x64 | Nao |
| `eneas_ult_crack` | Overlay rachaduras | 4 | 256x256 | 1024x256 | Nao |
| `eneas_aura_particles` | Particulas douradas | 4 | 16x16 | 64x16 | Sim |
| `eneas_bigode_idle` | Bigode independente (overlay) | 4 | 24x12 | 96x12 | Sim |

---

## Phaser 3 Atlas Keys

```javascript
// Personagem principal
{ key: 'npc_eneas', frameWidth: 64, frameHeight: 64 }

// Projetil 56
{ key: 'projectile_56', frameWidth: 32, frameHeight: 32 }

// Rosto gigante (ultimate)
{ key: 'eneas_ultimate_face', frameWidth: 256, frameHeight: 256 }

// Overlay de rachaduras (ultimate)
{ key: 'eneas_crack_overlay', frameWidth: 256, frameHeight: 256 }

// Particulas de aura
{ key: 'eneas_aura_particle', frameWidth: 16, frameHeight: 16 }

// Bigode overlay independente
{ key: 'eneas_bigode_overlay', frameWidth: 24, frameHeight: 12 }
```

---

## Notas para o Artista

1. **REVERENCIA**: Eneas e tratado com RESPEITO no estilo Andre Guedes. As deformacoes sao sutis comparadas a outros personagens. A comedia vem da reverencia ABSURDA, nao da zoacao.
2. **BIGODE E REI**: O bigode e o elemento visual mais importante. Ele e mais opaco, mais detalhado, mais animado que qualquer outra parte. O bigode tem personalidade propria.
3. **HOLOGRAMA NAO E NEGOCIAVEL**: Cada frame DEVE ter o efeito translucido. Se o Eneas parecer solido, esta errado (exceto no pico do ultimate, frames 3-5).
4. **OUTLINES MAIS SUAVES**: Enquanto outros personagens usam 2-4px de contorno irregular, Eneas usa 1-2px com menos irregularidade. Ele merece linhas mais limpas.
5. **AURA DOURADA SEMPRE**: Nao importa o frame -- a aura dourada esta SEMPRE presente. Pode variar em intensidade, nunca em existencia.
6. **A BANDEIRA E CAPA**: A bandeira do Brasil como capa e animada independentemente. Tem fisica de tecido simplificada. As cores da bandeira sao desaturadas/translucidas para manter a estetica fantasma.
7. **AFTERIMAGES NO MOVIMENTO**: Quando Eneas se move, ele deixa um rastro fantasmagorico (copies com alpha decrescente). Isso o diferencia de TODOS os outros personagens.
8. **ULTIMA COISA A SUMIR = BIGODE**: Em TODA animacao de desaparicao, o bigode e a ULTIMA parte a sumir. Sempre.
9. **SPAWN RULE**: O bigode se materializa ANTES do corpo. Sempre. O bigode lidera a existencia.
10. **SOM SINCRONIZADO**: O "MEU NOME E ENEAS!" no frame 6 do spawn e no frame 5 do ultimate sao momentos de sincronizacao critica com audio.
