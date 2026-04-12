# XANDAO - Variantes de Skin

## Boss do STF Principal - "Zumbis de Brasilia"

---

## Visao Geral das Skins

| # | Nome | Slug | Desbloqueio | Raridade | Descricao Curta |
|---|---|---|---|---|---|
| 1 | Normal | `xandao-skin-normal` | Padrao | Comum | Toga preta classica, o Xandao em sua forma mais pura |
| 2 | Xandaquistao | `xandao-skin-xandaquistao` | Derrotar boss 3x | Rara | Ditador militar, farda + toga, autoritarismo maximo |
| 3 | Sancionado | `xandao-skin-sancionado` | Easter egg EUA | Epica | Selo de sancao americano grudado, constrangido-furioso |
| 4 | Mao TSE Tung | `xandao-skin-mao` | Censurar 100 inimigos | Epica | Toga comunista vermelha, referencia ao meme |
| 5 | Dormindo | `xandao-skin-dormindo` | Meme da volta do X | Lendaria | Pijama de bolinhas, a unica skin onde Xandao NAO esta com raiva |

---

## SKIN 1: NORMAL (Padrao)

### Descricao Completa
A forma canonica do Xandao. Toga preta de ministro do STF, suja e amarrotada como se tivesse dormido com ela por 3 dias seguidos. Martelo de juiz do tamanho de um poste de luz. Careca brilhante como farol de caminhao. Expressao de quem quer censurar o universo inteiro.

### Paleta de Cores
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Toga | #1A1A1A (preto) | #0D0D0D | #2A2A2A |
| Pele | #8B6914 | #6B4F10 | #A67C1A |
| Careca | #8B6914 | #6B4F10 | #FFFFFF (brilho) |
| Olhos | #FF0000 | #8B0000 | #FF3333 |
| Martelo (cabo) | #4A3728 | #2D2118 | #5C4A3A |
| Martelo (cabeca) | #808080 | #505050 | #C0C0C0 |
| Veias | #8B0000 | --- | #CC0000 (pulsando) |
| Texto CENSURADO | #CC0000 | #8B0000 | #FF0000 |

### Detalhes Visuais
- **Toga**: Linhas irregulares simulando tecido amarrotado. Costuras visiveis nos ombros onde os biceps forcam. Barra inferior rasgada e desfiada (3-4px de fios soltos). Manchas sutis (1-2 pixels mais claros em areas aleatorias = suor/sujeira).
- **Careca**: Oval perfeita no topo do sprite. Highlight de 3x3px branco puro (#FFFFFF) que muda de posicao entre frames. Glow secundario de 5x5px amarelo claro (#FFFACD) com alpha 50%.
- **Olhos**: 2x2px cada, vermelhos. Esclerotica nao visivel neste tamanho - so o brilho vermelho importa. Em certas animacoes os olhos emitem raios (linhas horizontais vermelhas).
- **Martelo**: Desproporcional. Cabeca do martelo tem 16x10px. Cabo de 2px de largura. Inscricao "CENSURADO" representada por pixels vermelhos na face da cabeca (nao precisa ser legivel em 64x64 - sugestao de texto basta).
- **Veias**: Linhas de 1px em #8B0000 na testa (2 linhas diagonais) e pescoco (3 linhas verticais). Pulsam entre #8B0000 e #CC0000 nos frames de atividade intensa.
- **Biceps**: Protuberancias de 4-6px nos bracos, VISIVEIS sob a toga. A toga estica ao redor formando vincos.

### Sprites Necessarios
```
xandao-normal-idle.png       (256x64 - 4 frames)
xandao-normal-walk.png       (384x64 - 6 frames)
xandao-normal-attack.png     (192x64 - 3 frames)
xandao-normal-death.png      (256x64 - 4 frames)
xandao-normal-hit.png        (128x64 - 2 frames)
xandao-normal-censura.png    (384x64 - 6 frames)
xandao-normal-xandaquistao.png (512x64 - 8 frames)
xandao-normal-apagao.png     (384x64 - 6 frames)
```

### Efeitos Especificos da Skin
- Particulas de brilho da careca: branco/amarelo claro
- Raios dos olhos: vermelho puro
- Onda de choque: branco
- Zona Xandaquistao: dourado
- Apagao: azul eletrico

---

## SKIN 2: XANDAQUISTAO (Ditador Militar)

### Descricao Completa
O meme do "Xandaquistao" ganha vida. Xandao com toga MILITAR - uma fusao grotesca de farda de general de republica de banana com toga de ministro. Ombreiras com dragonas douradas. Medalhas absurdas no peito (uma delas e um martelo em miniatura). Quepe militar na careca (mas a careca continua brilhando por baixo, o quepe FLUTUA acima). Faixa no braco com X cortado. Botas de combate em vez de sapatos. Charuto no canto da boca (referencia a ditadores).

### Paleta de Cores
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Toga-Farda | #2F4F2F (verde militar escuro) | #1C3A1C | #3D6B3D |
| Dragonas/Medalhas | #DAA520 (dourado) | #B8860B | #FFD700 |
| Quepe | #2F4F2F | #1C3A1C | #3D6B3D |
| Quepe Aba | #1A1A1A (preto) | #0D0D0D | #2A2A2A |
| Quepe Emblema | #DAA520 | #B8860B | #FFD700 |
| Faixa do Braco | #8B0000 (vermelho escuro) | #5C0000 | #CC0000 |
| X Cortado na Faixa | #FFFFFF | --- | --- |
| Charuto | #8B4513 | #5C2D0A | #A0522D |
| Brasa do Charuto | #FF4500 | #CC3700 | #FF6347 |
| Botas | #1A1A1A | #0D0D0D | #333333 |
| Pele | #8B6914 (igual normal) | #6B4F10 | #A67C1A |
| Careca | Igual normal mas com brilho VERDE-DOURADO | --- | #ADFF2F |

### Detalhes Visuais
- **Toga-Farda**: Mesma silhueta da toga normal mas em verde militar. Bolsos no peito (2x3px retangulos mais escuros). Cinto com fivela dourada na cintura (linha horizontal com ponto dourado). Botoes dourados na frente (3 pontos de 1px).
- **Dragonas**: Ombreiras douradas com franjas (3-4 pixels pendurados em cada ombro). Sobem e descem com movimento.
- **Medalhas**: 3-4 pontos coloridos no peito (1px cada: dourado, prata, vermelho, verde). Uma em formato de martelinho (2x3px dourado).
- **Quepe**: Retangulo verde militar no topo da cabeca. ABA PRETA proeminente na frente. Emblema dourado no centro (2x2px). Careca brilha POR BAIXO do quepe - o quepe flutua 1px acima em idle, criando gap onde o brilho escapa.
- **Faixa do Braco**: Retangulo vermelho no braco esquerdo (4x3px). X branco cortado dentro (pixels formando X com linha diagonal).
- **Charuto**: 4px de comprimento horizontal saindo do canto da boca. Brasa na ponta (1px laranja que alterna com vermelho). Particulas de fumaca subindo (1-2 pixels cinza claro por frame).
- **Botas**: Pes em preto pesado, maiores que na skin normal (+1px cada). Solado mais grosso.

### Modificacoes de Animacao
- **Idle**: Fumaca sobe do charuto constantemente (particle effect extra). Medalhas brilham alternadamente.
- **Walk**: Botas fazem barulho mais pesado (som diferente). Quepe balanca levemente. Dragonas sacudem.
- **Attack**: Charuto cai da boca no windup, volta no recovery. Medalhas chacoalham.
- **Death**: Quepe cai primeiro (frame 1), medalhas se espalham com os papeis, charuto no chao fumegando.
- **Hit**: Quepe pula da cabeca momentaneamente, volta.
- **Censura Monocratica**: Igual mas ondas de silencio sao VERDES (militar).
- **Xandaquistao Special**: AMPLIFICADO - zona verde militar, bandeiras maiores, mais bandeiras (6 ao inves de 4).
- **Apagao Digital**: Static tem tint verde (como radar militar).

### Sprites Necessarios
```
xandao-xandaquistao-idle.png       (256x64)
xandao-xandaquistao-walk.png       (384x64)
xandao-xandaquistao-attack.png     (192x64)
xandao-xandaquistao-death.png      (256x64)
xandao-xandaquistao-hit.png        (128x64)
xandao-xandaquistao-censura.png    (384x64)
xandao-xandaquistao-zone.png       (512x64) // Xandaquistao zone AMPLIFICADA
xandao-xandaquistao-apagao.png     (384x64)
```

### Efeitos Exclusivos
- Particula: fumaca de charuto (cinza claro, sobe devagar)
- Particula: brilho de medalha (dourado, aleatorio)
- Som: marcha militar mais pronunciada
- Som: charuto crepitando (sutil, constante)

---

## SKIN 3: SANCIONADO (Sancoes dos EUA)

### Descricao Completa
Referencia direta aos memes das sancoes americanas contra Moraes. Toga preta NORMAL mas com um ENORME selo vermelho de "SANCTIONED" / "SANCIONADO" carimbado nas costas e no peito. Bandeirinhas americanas grudadas na toga como post-its. Expressao que mistura raiva com constrangimento - a UNICA skin onde Xandao mostra um pingo de desconforto (mas ainda com raiva predominante). Careca com suor (gotas). Martelo agora tem selo "BLOCKED" em vez de "CENSURADO". Papeis da OFAC (Office of Foreign Assets Control) voam ao redor durante specials.

### Paleta de Cores
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Toga | #1A1A1A (preto, igual normal) | #0D0D0D | #2A2A2A |
| Selo SANCTIONED | #CC0000 (vermelho) | #8B0000 | #FF0000 |
| Texto do Selo | #FFFFFF | --- | --- |
| Borda do Selo | #8B0000 | --- | --- |
| Bandeirinhas EUA (vermelho) | #B22234 | #8B1A28 | --- |
| Bandeirinhas EUA (azul) | #3C3B6E | #2D2C52 | --- |
| Bandeirinhas EUA (branco) | #FFFFFF | #E0E0E0 | --- |
| Gotas de Suor | #87CEEB (azul claro) | --- | #FFFFFF |
| Texto BLOCKED | #B22234 | #8B1A28 | #CC2234 |
| Papeis OFAC | #F5F5DC (bege) | #D2C5A0 | #FFFFFF |
| Pele (mais vermelha) | #9B6914 | #7B5010 | #B08020 |
| Careca (suada) | #8B6914 | #6B4F10 | #87CEEB (gotas) |

### Detalhes Visuais
- **Toga**: Identica a normal MAS com adesivos/selos grudados:
  - Selo grande no peito: circulo de 8x8px, vermelho, com texto branco pequeno (sugestao de "SANCTIONED")
  - Selo nas costas: mesmo padrao, visivel quando vira
  - 3-4 bandeirinhas americanas: retangulos de 3x4px com linhas vermelhas/brancas e canto azul, "grudados" irregularmente na toga como post-its
  - Borda de alguns selos descascando (1px saindo do selo)
- **Expressao**: MIX de raiva (70%) e constrangimento (30%). Sobrancelha franzida MAS um olho levemente mais aberto que o outro (assimetria de desconforto). Boca torcida para o lado (nao simetrica como na normal).
- **Gotas de Suor**: 2-3 gotas de 1x2px azul claro na testa e lateral do rosto. Escorrem em animacao (deslocam 1px para baixo entre frames).
- **Careca**: Brilho IRREGULAR - como se suor atrapalhasse o reflexo. Highlight pisca entre branco e azul claro.
- **Martelo**: Mesmo tamanho, mas inscricao "BLOCKED" em vermelho-americano (#B22234) ao inves de "CENSURADO".
- **Papeis OFAC**: Retangulos bege com selo vermelho e texto (linhas finas). Voam ao redor durante certas animacoes.

### Modificacoes de Animacao
- **Idle**: Gotas de suor escorrem. Xandao olha para os lados nervoso (olhos deslocam 1px lateralmente entre frames). Tenta arrancar uma bandeirinha (mao se move para o peito em frame 3) mas desiste.
- **Walk**: Passos levemente MENOS confiantes (corpo oscila 1px mais). Papeis OFAC voam atras dele como rastro.
- **Attack**: Grita "BLOCKED!" ao inves de "CENSURADO!". Impacto gera papeis de sancao ao inves de so rachadura.
- **Death**: Alem de papeis de inquerito, caem SELOS de sancao e bandeirinhas americanas. A frase "SANCTIONED" fica visivel no corpo caido.
- **Hit**: Gotas de suor MULTIPLICAM. Uma bandeirinha se solta e voa.
- **Censura Monocratica**: Texto "CENSURADO" alterna com "BLOCKED". Ondas de silencio tem tint vermelho/azul/branco alternando.
- **Xandaquistao**: Zona agora tem bandeirinhas americanas grudadas na borda (ironico - tentando remover).
- **Apagao Digital**: Static mostra momentaneamente logos de CNN, Fox News (como se captando TV americana). Texto alterna: "SEM SINAL" / "SANCTIONED" / "CONNECTION BLOCKED".

### Sprites Necessarios
```
xandao-sancionado-idle.png       (256x64)
xandao-sancionado-walk.png       (384x64)
xandao-sancionado-attack.png     (192x64)
xandao-sancionado-death.png      (256x64)
xandao-sancionado-hit.png        (128x64)
xandao-sancionado-censura.png    (384x64)
xandao-sancionado-zone.png       (512x64)
xandao-sancionado-apagao.png     (384x64)
```

### Efeitos Exclusivos
- Particula: gotas de suor (azul claro, caem)
- Particula: papeis OFAC voando (bege com selo vermelho)
- Particula: bandeirinhas se soltando (vermelho/azul/branco)
- Som: grunhidos mais constrangidos (menos confiantes)
- Som: papel colando/descolando (selos)
- Interacao especial: skill "Sancao do Trump" faz 2x dano nesta skin

---

## SKIN 4: MAO TSE TUNG (Comunista)

### Descricao Completa
Referencia ao meme "Mao TSE Tung" (Tribunal Superior Eleitoral). Xandao com toga VERMELHA estilo comunista chines. Colarinho Mao (gola alta rigida). Estrelas douradas no peito. Segura um "Livrinho Vermelho" na mao esquerda (quando nao esta usando). Martelo redesenhado com foice e martelo cruzados na cabeca. Poster de propaganda sovietica no fundo das animacoes de special (textura extra). Careca agora reflete VERMELHO como estrela vermelha.

### Paleta de Cores
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Toga Comunista | #CC0000 (vermelho) | #8B0000 | #FF0000 |
| Colarinho Mao | #CC0000 | #8B0000 | #FF3333 |
| Estrelas | #FFD700 (dourado) | #DAA520 | #FFFF00 |
| Livrinho Vermelho | #8B0000 (vermelho escuro) | #5C0000 | #CC0000 |
| Capa do Livro | #FFD700 (borda) | --- | --- |
| Martelo/Foice | #808080 (metal) | #505050 | #C0C0C0 |
| Emblema Foice/Martelo | #FFD700 | #DAA520 | #FFFF00 |
| Pele | #8B6914 (igual) | #6B4F10 | #A67C1A |
| Careca (brilho vermelho) | #8B6914 | #6B4F10 | #FF0000 |
| Fundo Propaganda | #CC0000 | #8B0000 | #FFD700 |
| Texto Propaganda | #FFD700 | --- | #FFFF00 |

### Detalhes Visuais
- **Toga Comunista**: VERMELHA intensa. Mesmo corte da toga normal mas em vermelho. Colarinho Mao: gola alta de 3px que sobe ate o queixo (rigida, reta). Botoes dourados na frente (3 pontos 1px). Dobras e amassados agora em tons de vermelho escuro/claro.
- **Estrelas**: Uma estrela grande no peito esquerdo (5x5px, dourada, 5 pontas em pixel art). Duas menores nos ombros (3x3px).
- **Livrinho Vermelho**: 4x5px, retangulo vermelho escuro com borda dourada de 1px. Segurado na mao esquerda durante idle e walk. No attack, e jogado para cima e pego de volta.
- **Martelo Redesenhado**: Cabeca do martelo agora tem emblema dourado de foice e martelo cruzados (pixel art simples: L invertido + arco). O cabo e vermelho escuro ao inves de marrom.
- **Careca**: Brilho VERMELHO. O highlight principal e vermelho (#FF0000) ao inves de branco. Secundario dourado (#FFD700). Cria efeito de "estrela vermelha brilhando".
- **Poster de Propaganda** (nas specials): Retangulo bege/vermelho que aparece atras durante censura e xandaquistao. Linhas de texto dourado ilegivel (sugestao de slogans). Raios saindo do centro (estilo poster sovietico classico).

### Modificacoes de Animacao
- **Idle**: Segura livrinho vermelho na mao esquerda, martelo no ombro direito. Livrinho brilha levemente (particula dourada rara). Careca brilha VERMELHO em pulso lento (como estrela).
- **Walk**: Marcha mais RITMADA (inspiracao Exercito Vermelho). Livrinho levantado como tocha. Passos perfeitamente sincronizados.
- **Attack**: Joga livrinho para cima (frame 1), martela (frame 2), pega livrinho de volta (frame 3). Impacto gera estrelas vermelhas ao inves de rachadura simples.
- **Death**: Toga vermelha se desfaz em BANDEIRAS VERMELHAS (nao papeis). Estrelas voam como particulas. Livrinho cai aberto no chao. Careca apaga do vermelho para preto.
- **Hit**: Estrelas do peito brilham em protesto. Livrinho e apertado contra o peito (protegendo-o). Brilho vermelho da careca intensifica.
- **Censura Monocratica**: Texto "CENSURADO" em DOURADO SOBRE VERMELHO (estilo propaganda). Poster aparece ao fundo com raios. Ondas de silencio sao vermelhas com brilho dourado.
- **Xandaquistao**: Zona VERMELHA com estrelas douradas. Bandeiras vermelhas com estrela (nao X cortado). Chao muda para vermelho. Visual de "republica popular do Xandaquistao".
- **Apagao Digital**: Static tem tint VERMELHO. Silhueta do Xandao tem estrela brilhando na careca. Texto alterna: "SEM SINAL" / "CENSURADO PELO PARTIDO" / "TSE DETERMINA".

### Sprites Necessarios
```
xandao-mao-idle.png       (256x64)
xandao-mao-walk.png       (384x64)
xandao-mao-attack.png     (192x64)
xandao-mao-death.png      (256x64)
xandao-mao-hit.png        (128x64)
xandao-mao-censura.png    (384x64)
xandao-mao-zone.png       (512x64)
xandao-mao-apagao.png     (384x64)
```

### Efeitos Exclusivos
- Particula: estrelas vermelhas/douradas (specials)
- Particula: brilho dourado do livrinho (idle)
- Particula: raios de propaganda (poster background)
- Textura: poster propaganda (overlay para specials)
- Som: marcha mais ritmada, inspiracao militar sovietica
- Som: paginas virando (livrinho)
- Som: hino distorcido ao fundo (muito sutil, durante specials)

### Interacao de Gameplay
- Skill "Mao TSE Tung" ganha visual extra: poster de propaganda como AOE visual
- Quando Xandao usa qualquer skill, texto "TSE DETERMINA" aparece brevemente
- Zona Xandaquistao dura 20% mais tempo nesta skin

---

## SKIN 5: DORMINDO (Pijama - Meme da Volta do X)

### Descricao Completa
A skin LENDARIA e mais memetica. Baseada no meme viral "aproveitando que o Xandao ta dormindo" que surgiu quando o X voltou ao Brasil. Xandao de PIJAMA DE BOLINHAS AZUIS, touca de dormir (mas a careca brilha por baixo), chinelos fofos, abraca um travesseiro gigante ao inves do martelo. Expressao SONOLENTA - a UNICA skin onde Xandao NAO esta furioso. Olhos semi-cerrados, boca aberta com baba escorrendo. ZZZ flutuando acima da cabeca. O travesseiro tem bordado "STF" em dourado. E a skin MAIS forte paradoxalmente - porque "o Xandao dormindo e mais perigoso que acordado".

### Paleta de Cores
| Elemento | Cor Principal | Sombra | Highlight |
|---|---|---|---|
| Pijama | #4169E1 (azul royal) | #2850A8 | #5B84F0 |
| Bolinhas do Pijama | #FFFFFF | #E0E0E0 | --- |
| Touca de Dormir | #4169E1 | #2850A8 | #5B84F0 |
| Pompom da Touca | #FFFFFF | #E0E0E0 | --- |
| Travesseiro | #F5F5F5 (branco sujo) | #D3D3D3 | #FFFFFF |
| Bordado STF | #DAA520 (dourado) | #B8860B | #FFD700 |
| Chinelos | #FF69B4 (rosa) | #CC5599 | #FF88CC |
| Baba | #87CEEB (azul claro) | --- | #FFFFFF |
| ZZZ | #4169E1 (azul) | --- | #87CEEB |
| Pele (mais clara, descansada) | #9B7924 | #7B6010 | #B0892A |
| Careca (brilho fraco) | #9B7924 | #7B6010 | #FFFACD (fraco) |
| Olhos (nao vermelhos!) | #4169E1 (azul sonolento) | --- | --- |

### Detalhes Visuais
- **Pijama**: Azul royal com bolinhas brancas (padrao: 1px branco a cada 3px). Botoes na frente (2 pontos brancos). Manga longa, cobrindo os biceps (biceps AINDA visiveis mas menos exagerados - ele esta "relaxado"). Calca do pijama combinando. Barra arrastando no chao.
- **Touca de Dormir**: Touca classica pontuda caindo para o lado. Azul com bolinhas brancas (mesmo padrao). Pompom branco na ponta que balanca com movimento. Careca BRILHA POR BAIXO da touca - brilho FRACO e difuso (#FFFACD com alpha 30% - ele ta dormindo, o poder esta adormecido).
- **Travesseiro**: Retangulo branco macio de 12x8px. Bordado "STF" em dourado no centro (3 letras tiny). Amassado em um dos lados (pixels irregulares). Segurado debaixo do braco esquerdo ou abraca com ambos os bracos no idle. Substitui o martelo como arma visual.
- **Chinelos**: Rosa (!!) com formato de bicho (urso? gato?). 3x4px cada pe. Ponta arredondada com 1px preto (olhinho do bicho). Absurdo para o personagem mais intimidador do jogo - COMEDIA PURA.
- **Expressao SONOLENTA**: Olhos SEMI-CERRADOS (1px de abertura ao inves de 2px). AZUIS, nao vermelhos. Sobrancelha RELAXADA (nao franzida pela primeira vez). Boca ABERTA com linha de baba escorrendo (1px azul claro descendo do canto da boca). Bocejo periodico (boca abre mais em certos frames).
- **ZZZ**: Letras "Z" flutuando acima da cabeca. 3 Z de tamanhos diferentes (3px, 4px, 5px). Sobem e desaparecem continuamente.
- **Baba**: Fio de baba de 1px de largura, azul claro, do canto da boca ate 3-4px abaixo. Oscila com movimento. Gota na ponta que cresce e cai periodicamente.

### Modificacoes de Animacao
- **Idle**: SONAMBULO. Corpo oscila levemente (1-2px lado a lado). ZZZ constante. Baba escorrendo. Bocejo a cada 3 ciclos (boca abre grande, olhos apertam, depois volta). Abraca travesseiro. Pompom da touca balanca.
- **Walk**: SONAMBULISMO. Caminha com bracos esticados a frente (classico sonambulo). Olhos fechados ou semi-cerrados. Tropecos (a cada 3 ciclos, frame extra com "escorregao" - corpo inclina 3px a mais). Chinelos fazem "flap flap". Arrasta travesseiro pelo chao.
- **Attack**: AINDA DORMINDO - ataca com o travesseiro! Ergue travesseiro (frame 1), ACOERTA com travesseiro (frame 2) - mas o impacto e DEVASTADOR (penas explodem + dano massivo). Frame 3: penas voando, chao rachado (como e possivel?!). Expressao: ainda dormindo durante todo o ataque.
- **Death**: Deita no travesseiro confortavelmente (nao parece morte - parece que finalmente foi DORMIR DE VERDADE). Pijama intacto. Touca no lugar. ZZZ ficam MAIORES (dorme mais profundamente). "Morte" mais pacifica do jogo. Ironia total.
- **Hit**: ACORDA MOMENTANEAMENTE! Olhos ARREGALAM e ficam VERMELHOS por 1 frame (lampejo do Xandao real). Grito de susto. Volta a dormir imediatamente (olhos fecham, voltam a azul). Pior frame do jogo para o jogador - ver o verdadeiro Xandao por 1 frame e TERROR PURO.
- **Censura Monocratica**: SONAMBULO. Levanta mao DORMINDO. Murmura "censurado..." em vez de gritar. ZZZ se transformam em letras "CENSURADO" por um momento. Efeito IDENTICO ao normal porem - silencia area igual. "O Xandao dormindo censura igual."
- **Xandaquistao**: Zona se forma ao redor de onde ele esta deitado. Pijamas aparecem nas bandeiras (ao inves de X cortado). Zona e azul ao inves de dourada. Travesseiros nas bordas da zona.
- **Apagao Digital**: Em vez de eletricidade, o sono SE ESPALHA. Tela fica com filtro azul escuro (nao static). "SHHH... O XANDAO TA DORMINDO" aparece no lugar de "SEM SINAL". ZZZ gigantes na tela. Todos os inimigos TAMBEM adormecem por 3s.

### Sprites Necessarios
```
xandao-dormindo-idle.png       (256x64)
xandao-dormindo-walk.png       (384x64)
xandao-dormindo-attack.png     (192x64)
xandao-dormindo-death.png      (256x64)
xandao-dormindo-hit.png        (128x64)
xandao-dormindo-censura.png    (384x64)
xandao-dormindo-zone.png       (512x64)
xandao-dormindo-apagao.png     (384x64)
```

### Efeitos Exclusivos
- Particula: ZZZ flutuando (azul, sobem e somem)
- Particula: penas do travesseiro (brancas, no attack e hit)
- Particula: gotas de baba (azul claro, caem)
- Particula: bolinhas de sono (circulos azuis transparentes, flutuam)
- Particula: estrelinhas de bocejo (amarelas pequenas, raro)
- Som: ronco constante (baixo volume, loop)
- Som: "flap flap" dos chinelos (walk)
- Som: bocejo periodico (idle, raro)
- Som: travesseiro impactando (absurdamente pesado para um travesseiro)
- Som: "shhh..." (censura monocratica)
- Som: murmuro dormindo (substitui gritos - "censurado..." "monocraticamente..." murmurados)

### Interacao de Gameplay ESPECIAL
- **Dano aumentado em 50%**: "O Xandao dormindo e mais perigoso"
- **Velocidade reduzida em 30%**: Esta sonambulo, anda devagar
- **Habilidades custam 50% menos cooldown**: "Nao precisa nem pensar, ja sai"
- **Easter egg**: Se o jogador nao atacar por 30s, Xandao acorda e vira skin Normal com HP cheio (GAME OVER praticamente)
- **Condicao de desbloqueio**: Derrotar Xandao Normal sem ser censurado nenhuma vez (dificil)

---

## TABELA DE PRIORIDADE DE PRODUCAO

| Prioridade | Skin | Razao |
|---|---|---|
| 1 - CRITICA | Normal | Skin padrao, obrigatoria para o jogo funcionar |
| 2 - ALTA | Dormindo | Skin mais memetica, maior apelo para o publico |
| 3 - MEDIA | Xandaquistao | Tematica forte, ja existe na habilidade |
| 4 - MEDIA | Sancionado | Atual, relevante politicamente |
| 5 - BAIXA | Mao TSE Tung | Meme mais de nicho, pode ser DLC |

---

## TOTAL DE SPRITES NECESSARIOS POR SKIN

| Animacao | Frames | Resolucao | Por Skin |
|---|---|---|---|
| Idle | 4 | 256x64 | 1 spritesheet |
| Walk | 6 | 384x64 | 1 spritesheet |
| Attack | 3 | 192x64 | 1 spritesheet |
| Death | 4 | 256x64 | 1 spritesheet |
| Hit | 2 | 128x64 | 1 spritesheet |
| Censura Monocratica | 6 | 384x64 | 1 spritesheet |
| Xandaquistao Zone | 8 | 512x64 | 1 spritesheet |
| Apagao Digital | 6 | 384x64 | 1 spritesheet |
| **TOTAL por skin** | **39 frames** | --- | **8 spritesheets** |
| **TOTAL todas skins** | **195 frames** | --- | **40 spritesheets** |

### Extras Compartilhados (todas skins usam)
| Asset | Frames | Resolucao |
|---|---|---|
| Projetil Multa do X | 4 | 128x32 |
| Projetil Raio do Olho | 2 | 64x32 |
| FX Censurado | 3 | 96x32 |
| FX Rachadura | 2 | 64x32 |
| FX Static (tileable) | 4 | 128x32 |
| Portrait HUD | 1 | 32x32 |
| Icone HP | 1 | 16x16 |
| Banner X Cortado | 1 | 16x24 |
| Particula Papel | 4 | 16x16 |
| **TOTAL extras** | **22 frames** | --- |

### Grande Total
- **217 frames** de pixel art no total
- **40 spritesheets** de animacao
- **~10 assets** avulsos de efeito/UI
- **5 paletas de cores** distintas
- **~55 arquivos de audio** (ver animation-spec.md)
