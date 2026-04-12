# Cartao Corporativo - Sprite Specification

## Overview
- **Weapon Type:** Ranged / Summon (Special Weapon - Janja)
- **Sprite Dimensions:** 32x32px (cartao + projeteis de luxo)
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 30 (1 static + 3 swipe attack + 4 luxury projectiles + 4 projectile rotation + 4 money explosion + 2 idle float + 3 special guillotine + 5 luxury items individual + 4 "APROVADO!" FX)
- **Sprite Sheet Size:** 960x32px
- **Format:** PNG with alpha transparency
- **Anchor Point:** Center (16, 16) -- card center point

## Color Palette

| Element                    | Hex Code  | Usage                                     |
|----------------------------|-----------|-------------------------------------------|
| Card Gold (main)           | `#C4A020` | Cartao base color, platinum gold          |
| Card Gold (bright)         | `#E8C840` | Card highlights, embossed shine           |
| Card Gold (dark)           | `#8A7010` | Card shadows, edge depth                  |
| Card Platinum              | `#D4C898` | Platinum shimmer layer                    |
| Card Platinum (bright)     | `#F0E8C8` | Platinum peak highlights                  |
| Card Black (stripe)        | `#1A1A1A` | Magnetic stripe on back                   |
| Card Black (text)          | `#2A2018` | Card numbers, text                        |
| Chip Gold                  | `#D4A830` | EMV chip square                           |
| Chip Gold (lines)          | `#A08020` | Chip circuit lines                        |
| Logo Red                   | `#CC2200` | "GASTAO CARD" logo accent                 |
| Logo Text                  | `#1A1A1A` | "GASTAO CARD" lettering                   |
| Money Green                | `#2A7A2A` | Nota de dinheiro base                     |
| Money Green (light)        | `#4AAA4A` | Nota highlights                           |
| Money Green (dark)         | `#1A5A1A` | Nota shadows, print lines                 |
| Money Symbol               | `#C4A020` | Cifrao "$" nas notas                      |
| Luxury Pink                | `#CC6688` | Bolsa designer base                       |
| Luxury Pink (bright)       | `#E888AA` | Bolsa highlights                          |
| Luxury Red (shoe)          | `#AA2222` | Sapato de salto base                      |
| Luxury Red (bright)        | `#CC4444` | Sapato highlights                         |
| Champagne Gold             | `#D4B870` | Garrafa champagne base                    |
| Champagne Green            | `#2A4A2A` | Garrafa champagne vidro                   |
| Champagne Bubble           | `#F8F0D0` | Bolhas de champagne                       |
| Jewel Blue                 | `#2244AA` | Joia safira base                          |
| Jewel Sparkle              | `#88AAFF` | Joia brilho/reflexo                       |
| Perfume Purple             | `#7744AA` | Frasco perfume base                       |
| Perfume Purple (bright)    | `#9966CC` | Frasco perfume highlights                 |
| Perfume Mist               | `#CC99EE` | Nuvem de perfume, particulas              |
| Approval Green             | `#00AA44` | "APROVADO!" text color                    |
| Flash White                | `#FFFFF0` | Transaction flash, card swipe glow        |
| Outline Black              | `#1A1A1A` | Thick 2px outlines (Crumb style)          |
| Shadow Dark                | `#0D0D0D` | Drop shadow, 50% opacity                  |
| Guillotine Blade           | `#C4B880` | Lâmina dourada do cartao gigante          |
| Blood Gold                 | `#AA8820` | "Sangue" dourado do special (nao vermelho)|

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 31,31
- **Description:** Cartao de credito ENORME visto em top-down isometrico, preenchendo ~85% do frame 32x32. Formato retangular classico de cartao (proporcao 86x54mm escalada) mas EXAGERADAMENTE grosso e brilhante -- nao e um cartao normal, e um cartao que GRITA riqueza obscena. Cor DOURADA/PLATINA (#C4A020 base com shimmer #D4C898). Chip EMV visivel no canto esquerdo (quadrado 4x4px, #D4A830, com linhas de circuito #A08020). NUMEROS DO CARTAO visíveis: "666 666 666 666" em fonte embossada (#2A2018 sobre fundo dourado) -- os numeros sao grotescamente grandes para o tamanho do cartao. Abaixo dos numeros: "PRIMEIRA DAMA LTDA" como nome do titular em letras menores. No canto inferior direito: logo "GASTAO CARD" -- um cifrão gordo estilizado em vermelho (#CC2200) com texto preto. Faixa magnetica preta (#1A1A1A) visivel na borda superior (vista isometrica mostra a espessura). O cartao TEM BRILHO -- 3-4 pixels de highlight (#F0E8C8) nos cantos e bordas sugerindo superficie polida. Contornos grossos pretos (2px). Sombra de drop (2px, 50% opacity). O cartao transborda opulencia vulgar.
- **Style Notes:** O cartao deve parecer OBSCENAMENTE caro -- ouro demais, brilho demais, espessura demais. E um objeto de status grotesco. O "666 666 666 666" e a piada visual obvia (numero do cartao = numero da besta). O logo "GASTAO CARD" e a bandeira ficticia -- deve parecer uma paroquia das bandeiras reais de cartao mas com um cifrão gordo e comico. Tudo RELUZ de forma incomoda.

### Frame 1: Swipe Attack - Card Out
- **Position in sheet:** 32,0 to 63,31
- **Description:** Janja SACA o cartao com velocidade. Cartao em angulo de ~30 graus, saindo de uma posicao "bolso" implicita. Motion blur trail (2 linhas, 1px, #C4A020, 50% opacity) atras do cartao. O chip EMV BRILHA com o atrito do movimento (1px #E8C840 ao redor). Numeros "666" parcialmente visiveis. O cartao parece estar sendo BRANDIDO como uma arma branca -- a borda parece afiada. Particulas de brilho dourado (2-3, 1x1px, #E8C840) se desprendem durante o saque.

### Frame 2: Swipe Attack - Transaction!
- **Position in sheet:** 64,0 to 95,31
- **Description:** Frame CENTRAL do ataque. Cartao na horizontal, sendo "passado" no ar como se houvesse uma maquininha invisivel. Um FLASH BRANCO (#FFFFF0, 8x8px) irradia do chip -- o momento da "transacao". Linhas de energia dourada (#E8C840, 4 linhas radiais, 6px cada) explodem do cartao. O logo "GASTAO CARD" brilha intensamente. Uma FATURA INVISIVEL esta sendo processada -- particulas numericas ("$", "R$", numeros aleatorios, 1px, #C4A020) cascateiam para baixo do cartao. O cartao treme com a "aprovacao" -- linhas de vibracao (2 onduladas, 1px) ao redor.

### Frame 3: Swipe Attack - Items Summoned
- **Position in sheet:** 96,0 to 127,31
- **Description:** Frame apos a transacao. O cartao se estabiliza, levemente inclinado. Do TOPO do frame, 3-4 silhuetas de itens de luxo (2x2px cada, cores variadas -- rosa, vermelho, verde, azul) comecam a CAIR como meteoros de consumismo. Cada silhueta tem um pequeno trail dourado atras (1px). O cartao ainda brilha com residuo do flash. Um mini recibo (3x5px, branco com texto ilegivel) se materializa ao lado do cartao e comeca a enrolar. A mensagem visual: a "compra" invocou projeteis de luxo.

### Frame 4: Luxury Projectile - Bolsa Designer (32x32)
- **Position in sheet:** 128,0 to 159,31
- **Description:** BOLSA DE GRIFE voando como projetil, 32x32. A bolsa e GROTESCAMENTE cara-aparecendo -- cor rosa escuro (#CC6688) com hardware dourado (#C4A020) exagerado (fivela gigante, corrente grossa, logo ficticio "JANJA" em dourado). Formato classico de bolsa de luxo (tipo Kelly/Birkin parodia) mas DESPROPORCIONAL -- a fivela e quase do tamanho da bolsa. A bolsa GIRA em voo -- este frame mostra a frente. Ziper dourado brilha. 1 etiqueta de preco (#FFFFF0, 2x1px) pende da alca com cifrao. Contorno preto grosso. A bolsa parece mais cara que um apartamento.

### Frame 5: Luxury Projectile - Sapato de Salto (32x32)
- **Position in sheet:** 160,0 to 191,31
- **Description:** SAPATO DE SALTO ALTISSIMO voando como projetil, 32x32. Vermelho (#AA2222) brilhante com sola (#1A1A1A) e salto ABSURDAMENTE alto (stiletto, 14px de salto para 18px de sapato -- proporcao impossivel). O salto parece uma ARMA -- fino e pontudo como um estilete. Brilho em verniz (#CC4444) no couro. Vista lateral, o sapato gira em voo com a ponta do salto como projetil perfurante. Mini logo ficticio "LOUBOUTIN*" (* = "com dinheiro publico" em micro-texto ilegivel) na sola. O sapato e ARMA e simbolo de status simultaneamente.

### Frame 6: Luxury Projectile - Garrafa Champagne (32x32)
- **Position in sheet:** 192,0 to 223,31
- **Description:** GARRAFA DE CHAMPAGNE voando como projetil, 32x32. Garrafa escura (#2A4A2A vidro) com rotulo dourado (#D4B870) elaborado -- parodia de Dom Perignon com texto "DOM CORPORATIVO" ilegivel. ROLHA (#8A6A3A) parcialmente expulsa, espumando. Bolhas de champagne (#F8F0D0, 4-5 particulas 1x1px) escapam do gargalo formando trail. A garrafa gira em voo com espuma trilhando atras. Papel aluminio dourado (#C4A020) no gargalo amassado. Peso visual: a garrafa e DENSA e perigosa.

### Frame 7: Luxury Projectile - Joia/Safira (32x32)
- **Position in sheet:** 224,0 to 255,31
- **Description:** JOIA GIGANTE voando como projetil, 32x32. Uma safira (#2244AA) em corte cushion ABSURDAMENTE grande -- do tamanho de um punho, montada em anel de ouro (#C4A020) igualmente desproporcional. Facetas da pedra refletem luz (3-4 pixels #88AAFF em posicoes estrategicas). A pedra BRILHA internamente (1px #FFFFF0 no centro -- brilho de lapidacao). Sparkles de joalheria (2-3 particulas #88AAFF, 1x1px) irradiam. O anel de ouro e tao grosso que parece um soco-ingles. A joia e tao grande que e ofensiva.

### Frame 8: Luxury Projectile - Perfume (32x32)
- **Position in sheet:** 256,0 to 287,31
- **Description:** FRASCO DE PERFUME voando como projetil, 32x32. Frasco de cristal (#7744AA roxo translucido) com tampa dourada (#C4A020) elaborada -- formato art-deco exagerado (mais arte que funcao). Liquido visivel dentro (roxo mais escuro, sloshing em voo). NUVEM DE PERFUME (#CC99EE, 6x6px, 40% opacity) trilha atras do frasco como uma cauda de cometa odorífera. O frasco tem etiqueta ficticia "No5 PLANALTO" em micro-texto dourado. Spray ativo: micro-goticulas (#CC99EE, 1x1px, 3-4 particulas) aspergem da tampa. O perfume e TOXICO de tao forte -- a nuvem tem linhas onduladas como o "cheiro" visivel do Velho Barreiro, mas em ROXO LUXUOSO.

### Frame 9: Projectile Rotation - Turn 1 (Generic, all items)
- **Position in sheet:** 288,0 to 319,31
- **Description:** Frame generico de ROTACAO de projetil de luxo -- mostra o conceito de rotacao para QUALQUER item. O item e representado como uma silhueta dourada generica (#C4A020) em posicao 0 graus (frente), com linhas de brilho e trail. Este frame demonstra o principio: todos os 5 projeteis de luxo GIRAM ao cair do ceu. Linhas de velocidade (2, 1px, dourado) trilham acima (o item cai). Sparkles (#E8C840, 2 particulas) atras.

### Frame 10: Projectile Rotation - Turn 2
- **Position in sheet:** 320,0 to 351,31
- **Description:** Mesmo conceito, rotacao a 90 graus. Silhueta de item vista de lado -- mais fina. Trail de queda mais longo. Sparkles mais dispersos. A rotacao em queda cria o efeito de "chuva de luxo".

### Frame 11: Projectile Rotation - Turn 3
- **Position in sheet:** 352,0 to 383,31
- **Description:** Rotacao a 180 graus -- item de costas/invertido. Sombra mais pesada (vindo de cima = mais escuro). Trail maximo. Speedlines de queda intensas.

### Frame 12: Projectile Rotation - Turn 4
- **Position in sheet:** 384,0 to 415,31
- **Description:** Rotacao a 270 graus -- quase completando o ciclo. Item inclinado, prestes a atingir o chao. FLASH de impacto iminente (1px #FFFFF0 abaixo do item). Trail diminuindo. O item esta no ultimo momento antes da explosao de dinheiro.

### Frame 13: Money Explosion - Impact 1 (Contact)
- **Position in sheet:** 416,0 to 447,31
- **Description:** Momento do IMPACTO do item de luxo no alvo. O item se DEFORMA no contato (squash). NOTAS DE DINHEIRO (#2A7A2A) comecam a EXPLODIR do ponto de impacto -- 4 notas iniciais, cada uma 4x2px com micro-cifrao "#C4A020" impresso. Starburst dourado (#E8C840, 6x6px) no centro. Flash branco (4x4px, #FFFFF0). O item rachou -- fragmentos do objeto de luxo + notas de dinheiro mixados na explosao. Um RECIBO (3x5px, branco) com "R$ 999.999,99" em micro-texto ilegivel se materializa.

### Frame 14: Money Explosion - Scatter
- **Position in sheet:** 448,0 to 479,31
- **Description:** EXPLOSAO MAXIMA de dinheiro. 8-12 notas de dinheiro (#2A7A2A com #4AAA4A highlights) VOAM em todas as direcoes -- radial 360 graus. Cada nota gira individualmente enquanto voa. Fragmentos do item de luxo (2-3 pedacos nas cores do item original, 2x2px) misturados. MOEDAS douradas (#C4A020, 2x2px circulares, 3-4) tambem voam. O centro ainda brilha. O recibo voa para cima, enrolando. A imagem e de DINHEIRO EXPLODINDO -- grotescamente abundante.

### Frame 15: Money Explosion - Rain
- **Position in sheet:** 480,0 to 511,31
- **Description:** Notas de dinheiro em "chuva" descendente. 6-8 notas descendo (gravidade), virando e girando. Moedas rebatendo no chao (1-2 faiscas ao atingir). Os fragmentos do item de luxo quase sumiram. O brilho central desvanece para 40%. Uma FATURA longa (1x8px, branco) desenrola do topo -- o custo de tudo isso. Atmosfera de "dinheiro caindo do ceu".

### Frame 16: Money Explosion - Residue
- **Position in sheet:** 512,0 to 543,31
- **Description:** Frame final. 2-3 notas de dinheiro no chao (pousadas, flat, #2A7A2A). 1 moeda rodando e caindo (#C4A020, diminuindo). A fatura esta completamente desenrolada e se dissolve. Um brilho residual dourado (8x8px, 15% opacity, #C4A020) marca o ponto de impacto. Nenhum vestigio do item de luxo -- transformou-se 100% em dinheiro. O ground tell: onde caiu luxo, restou divida.

### Frame 17: Idle Float - Hover High
- **Position in sheet:** 544,0 to 575,31
- **Description:** Cartao FLUTUANDO ao lado da posicao implicita de Janja. O cartao paira 2px acima da posicao de repouso -- levitacao de opulencia. Leve inclinacao para a esquerda (5 graus). BRILHO CONSTANTE -- 2-3 pixels de highlight (#F0E8C8) cintilam nas bordas, como se o cartao fosse feito de metal precioso real. Os numeros "666 666 666 666" pulsam levemente (1px de glow #E8C840 ao redor). O logo "GASTAO CARD" brilha em vermelho. Uma particula de dinheiro (#2A7A2A, 1x1px, uma nota minuscula) orbita preguicosamente ao redor do cartao -- dinheiro e atraido gravitacionalmente ao cartao. O chip EMV pisca como um LED de "standby".

### Frame 18: Idle Float - Hover Low
- **Position in sheet:** 576,0 to 607,31
- **Description:** Espelha o Frame 17 mas cartao 2px ABAIXO da posicao de repouso (descendo na flutuacao). Inclinacao oposta (5 graus para a direita). Highlights deslocam para os cantos opostos. A mini-nota de dinheiro orbital move para o outro lado do cartao. Chip EMV apaga momentaneamente (pisca off). Os numeros "666" param de brilhar neste frame (alternancia de glow). Juntos Frames 17-18 criam uma flutuacao suave e irritantemente ostensiva -- o cartao EXIBE-SE.

### Frame 19: Special - Cartao Gigante Descendo 1 (Aparicao)
- **Position in sheet:** 608,0 to 639,31
- **Description:** SPECIAL ATTACK: Um cartao GIGANTE comeca a descer do topo do frame. O cartao gigante e uma versao ampliada (preenche a largura toda do frame, 30x20px) vista de lado (perspectiva de guilhotina descendo). A borda inferior do cartao e AFIADA -- reflete luz (#FFFFF0) como uma lamina de guilhotina. Numeros "666 666 666 666" estao visiveis ENORMES. O logo "GASTAO CARD" ameacadoramente presente. Sombra MASSIVA (#0D0D0D, 60% opacity) projeta-se abaixo, escurecendo o frame. O cartao esta a 25% descido. Speedlines douradas (#C4A020) acima indicam velocidade de queda. A atmosfera e de JULGAMENTO FINANCEIRO IMINENTE.

### Frame 20: Special - Cartao Guilhotina 2 (Descendo)
- **Position in sheet:** 640,0 to 671,31
- **Description:** Cartao gigante a 60% descido. A lamina dourada agora domina o frame. REFLEXO de luz branca (#FFFFF0) corre pela borda de corte (2px de animacao de brilho). Notas de dinheiro (#2A7A2A, 3-4, 2x2px) sao EMPURRADAS para os lados pelo vento do cartao descendo. A sombra abaixo e ainda mais escura e larga. O chip EMV do cartao gigante brilha intensamente (#E8C840). Particulas douradas (#C4A020, 4-5, 1x1px) se desprendem das bordas com a velocidade. Pressao de ar visivel (linhas de compressao abaixo do cartao). O momento e de TERROR FINANCEIRO.

### Frame 21: Special - Guilhotina Impacto 3 (Corte)
- **Position in sheet:** 672,0 to 703,31
- **Description:** Cartao gigante ATINGE o chao. IMPACTO MASSIVO. A borda cortante finca no ponto de impacto. EXPLOSAO LATERAL de notas de dinheiro (10-12 notas voam para os lados, cada uma 3x2px #2A7A2A). Moedas (#C4A020, 4-5, 2x2px) saltam e ricocheteiam. FLASH de aprovacao (#FFFFF0 + #00AA44 "APROVADO!" em micro-texto, 8x3px) aparece no chip do cartao. A terra/chao RACHA (2-3 linhas de fissura, 1px #0D0D0D) irradiando do ponto de impacto. "Sangue" DOURADO (#AA8820) -- nao vermelho -- espirra dos lados (o cartao sangra OURO). Shockwave dourado (1px #C4A020 ring, 28px diametro). O impacto e GROTESCAMENTE opulento.

### Frame 22: Bolsa Designer - Variant Angle
- **Position in sheet:** 704,0 to 735,31
- **Description:** BOLSA DE GRIFE em angulo alternativo (vista de cima/3-quarters). Hardware dourado EXTRA visivel -- corrente, fivela, puxador de ziper, logo "JANJA". Interior VERMELHO (#AA2222) parcialmente visivel pela abertura. Uma nota de R$100 (#2A7A2A) esta saindo de dentro da bolsa como lingua de cobra. A bolsa e ABSURDA -- mais acessorios dourados que superficie de couro. Etiqueta de preco gigante (3x2px, branco com "#" simbolo).

### Frame 23: Sapato - Variant Angle
- **Position in sheet:** 736,0 to 767,31
- **Description:** SAPATO DE SALTO em angulo alternativo (vista de frente/cima). O salto stiletto aponta para baixo como ESTACA. Brilho de verniz exagerado (#CC4444). Lacinhos ou fivela dourada (#C4A020) no peito do pe. A sola vermelha e visivel (parodia da sola vermelha iconica). O sapato parece capaz de perfurar aco.

### Frame 24: Champagne - Variant (Estourando)
- **Position in sheet:** 768,0 to 799,31
- **Description:** GARRAFA DE CHAMPAGNE no momento do ESTOURO. Rolha (#8A6A3A) voando para cima (3px acima do gargalo). EXPLOSAO de espuma (#F8F0D0, 10x6px) irrompendo do gargalo. Bolhas (#F8F0D0, 6-8 particulas) em cascata. Spray de champagne em arco. A garrafa vibra com a pressao liberada. Papel aluminio (#C4A020) se rasga. E uma CELEBRACAO ARMADA.

### Frame 25: Joia - Variant (Brilho Maximo)
- **Position in sheet:** 800,0 to 831,31
- **Description:** SAFIRA em brilho MAXIMO -- a pedra (#2244AA) emite raios de luz (#88AAFF, 6 raios, 4px cada) como uma estrela. O anel de ouro (#C4A020) reflete o brilho. A joia parece ter PODER -- nao e so bonita, e intimidante. Sparkles (#FFFFF0, 4-5 particulas) irradiam. A safira quase parece radioativa de tao brilhante.

### Frame 26: Perfume - Variant (Nuvem Toxica)
- **Position in sheet:** 832,0 to 863,31
- **Description:** FRASCO DE PERFUME com nuvem MAXIMA. A nuvem de perfume (#CC99EE, 20x16px, 50% opacity) domina o frame -- o frasco (#7744AA) mal e visivel dentro da nuvem. Linhas onduladas de cheiro (3-4 ondas, 1px, #9966CC) irradiam. Particulas de spray (#CC99EE, 6-8, 1x1px) formam constelacao. Micro-corações (#CC6688, 1x1px, 2-3) flutuam na nuvem (parodia de perfume de luxo). O perfume e tao forte que e uma ARMA QUIMICA fashion.

### Frame 27: "APROVADO!" FX - Appear
- **Position in sheet:** 864,0 to 895,31
- **Description:** Texto onomatopeico "APROVADO!" aparecendo em estilo comic-book. Letras CHUNKY (#00AA44 verde "aprovacao") com sombra dourada (#C4A020). Fonte mao-desenhada, irregular, GRITADA. Um mini recibo (fundo branco) se materializa atras do texto. Cifroes ("$", 2x3px, #C4A020) orbitam. O VERDE e o verde de "transacao aprovada" das maquininhas de cartao. Flash de tela (1px borda branca, 20% opacity).

### Frame 28: "APROVADO!" FX - Peak
- **Position in sheet:** 896,0 to 927,31
- **Description:** "APROVADO!" no tamanho MAXIMO (110% scale). Letras vibram (1px deslocamento aleatorio cada). O verde (#00AA44) intensifica. Cifroes multiplicam (5-6 orbitando). O recibo atras cresce e comecar a ENROLAR (desenrolamento infinito sugerido). Um CARIMBO visual (circulo 8x8px, vermelho #CC2200, com "OK" dentro) aparece por cima como aprovacao burocratica. Starburst de notas de dinheiro (4 notas minusculas voando dos cantos). MAXIMO CONSUMISMO visual.

### Frame 29: "APROVADO!" FX - Fade
- **Position in sheet:** 928,0 to 959,31
- **Description:** "APROVADO!" desvanecendo -- 50% opacity, 80% scale. Verde clareando para #44CC88. Cifroes dispersando. Recibo enrolando-se e desaparecendo. Carimbo vermelho sumindo. Uma FATURA (2x6px, branco amarelado) desce suavemente de onde o texto estava -- o custo final da aprovacao. Notas de dinheiro pousando. Transicao para gameplay.

## Sprite Sheet Summary

| Frame | Name                    | Position   | Purpose                          |
|-------|-------------------------|------------|----------------------------------|
| 0     | static                  | 0-31       | Inventory / UI icon              |
| 1     | swipe_draw              | 32-63      | Card drawn for attack            |
| 2     | swipe_transaction       | 64-95      | Transaction flash moment         |
| 3     | swipe_summon            | 96-127     | Luxury items begin falling       |
| 4     | proj_bolsa              | 128-159    | Designer bag projectile          |
| 5     | proj_sapato             | 160-191    | High heel projectile             |
| 6     | proj_champagne          | 192-223    | Champagne bottle projectile      |
| 7     | proj_joia               | 224-255    | Giant jewel projectile           |
| 8     | proj_perfume            | 256-287    | Perfume bottle projectile        |
| 9     | proj_rotate_1           | 288-319    | Falling rotation 0 deg           |
| 10    | proj_rotate_2           | 320-351    | Falling rotation 90 deg          |
| 11    | proj_rotate_3           | 352-383    | Falling rotation 180 deg         |
| 12    | proj_rotate_4           | 384-415    | Falling rotation 270 deg         |
| 13    | money_impact            | 416-447    | Contact + money burst start      |
| 14    | money_scatter           | 448-479    | Maximum money explosion          |
| 15    | money_rain              | 480-511    | Money raining down               |
| 16    | money_residue           | 512-543    | Bills on ground, aftermath       |
| 17    | idle_hover_high         | 544-575    | Card floating up                 |
| 18    | idle_hover_low          | 576-607    | Card floating down               |
| 19    | special_descend_1       | 608-639    | Giant card appearing from above  |
| 20    | special_descend_2       | 640-671    | Giant card guillotine falling    |
| 21    | special_impact          | 672-703    | Giant card slams ground          |
| 22    | variant_bolsa           | 704-735    | Bag alternate angle              |
| 23    | variant_sapato          | 736-767    | Shoe alternate angle             |
| 24    | variant_champagne       | 768-799    | Champagne popping                |
| 25    | variant_joia            | 800-831    | Jewel max sparkle                |
| 26    | variant_perfume         | 832-863    | Perfume toxic cloud              |
| 27    | fx_aprovado_1           | 864-895    | "APROVADO!" appear               |
| 28    | fx_aprovado_2           | 896-927    | "APROVADO!" peak                 |
| 29    | fx_aprovado_3           | 928-959    | "APROVADO!" fade                 |

## Phaser 3 Atlas Key
```
key: 'weapon_cartao_corporativo'
frameWidth: 32
frameHeight: 32
```

## Phaser 3 Animation Config
```javascript
// Card swipe attack
this.anims.create({
    key: 'cartao_swipe',
    frames: this.anims.generateFrameNumbers('weapon_cartao_corporativo', { start: 1, end: 3 }),
    frameRate: 10,
    repeat: 0
});

// Luxury projectile rotation (overlay on any projectile during fall)
this.anims.create({
    key: 'cartao_proj_rotate',
    frames: this.anims.generateFrameNumbers('weapon_cartao_corporativo', { start: 9, end: 12 }),
    frameRate: 12,
    repeat: -1
});

// Money explosion on impact
this.anims.create({
    key: 'cartao_money_explode',
    frames: this.anims.generateFrameNumbers('weapon_cartao_corporativo', { start: 13, end: 16 }),
    frameRate: 8,
    repeat: 0
});

// Idle float
this.anims.create({
    key: 'cartao_idle',
    frames: this.anims.generateFrameNumbers('weapon_cartao_corporativo', { start: 17, end: 18 }),
    frameRate: 2, // Slow, ostentatious float
    repeat: -1
});

// Special: Giant card guillotine
this.anims.create({
    key: 'cartao_guillotine',
    frames: this.anims.generateFrameNumbers('weapon_cartao_corporativo', { start: 19, end: 21 }),
    frameRate: 8,
    repeat: 0
});

// "APROVADO!" effect
this.anims.create({
    key: 'cartao_aprovado',
    frames: this.anims.generateFrameNumbers('weapon_cartao_corporativo', { start: 27, end: 29 }),
    frameRate: 8,
    repeat: 0
});

// Individual projectile selection (random pick on attack)
const luxuryItems = [
    { key: 'proj_bolsa', frame: 4 },
    { key: 'proj_sapato', frame: 5 },
    { key: 'proj_champagne', frame: 6 },
    { key: 'proj_joia', frame: 7 },
    { key: 'proj_perfume', frame: 8 }
];
// Use: Phaser.Math.RND.pick(luxuryItems) to select random projectile per attack
```

## Particle Effects

### Money Bills (on every impact)
- 8-12 notas por impacto
- Cor: #2A7A2A base, #4AAA4A highlights, #C4A020 cifrao
- Tamanho: 3x2px (notas), 2x2px (moedas)
- Lifetime: 800-1200ms
- Direcao: radial 360 graus com gravidade
- Rotacao: cada nota gira individualmente (180-360 graus/s)
- Opacity: 1.0 -> 0.3 (persiste como ground litter brevemente)

### Gold Sparkles (constante ao redor do cartao)
- 2-4 particulas por segundo
- Cor: #E8C840, #F0E8C8 alternando
- Tamanho: 1x1px
- Lifetime: 400ms
- Direcao: radial lento, drift para cima
- Opacity: 0.0 -> 0.8 -> 0.0 (appear, flash, fade)

### Transaction Flash (on swipe)
- 1 flash unico
- Cor: #FFFFF0 core, #00AA44 halo
- Tamanho: 8x8px expandindo para 16x16px em 100ms
- Lifetime: 200ms
- Radiação: linhas verdes (#00AA44) irradiam como circuito digital

### Luxury Trail (behind falling items)
- 1-2 particulas por frame durante queda
- Cor: #C4A020 (trilha dourada)
- Tamanho: 1-2px
- Lifetime: 300ms
- Direcao: para cima (oposto a queda)
- Opacity: 0.6 -> 0.0

### Perfume Cloud (perfume projectile only)
- 3-5 particulas por frame
- Cor: #CC99EE com #9966CC
- Tamanho: 3-6px (cresce)
- Lifetime: 800ms
- Direcao: dispersao lateral lenta
- Opacity: 0.4 -> 0.0
- Bonus: micro-coracoes (#CC6688, 1px) aparecem 20% do tempo

### Champagne Bubbles (champagne projectile only)
- 2-4 particulas por frame
- Cor: #F8F0D0
- Tamanho: 1-2px (circular)
- Lifetime: 500ms
- Direcao: para cima (bolhas sobem)
- Opacity: 0.5 -> 0.0

---

## Audio Sincronizado

| Evento | Som | Duracao | Trigger |
|---|---|---|---|
| Swipe (saque) | Swoosh metalico + "bling" de cartao premium | 300ms | Frame 1 |
| Transacao | Beep de maquininha + "APROVADO!" voz robotica | 500ms | Frame 2 |
| Item caindo | Whoosh descendente + tinkle de luxo | 400ms | Cada projetil |
| Impacto bolsa | THUD oco + crack de couro | 300ms | Bolsa impact |
| Impacto sapato | STAB agudo + click de salto | 250ms | Sapato impact |
| Impacto champagne | POP de rolha + SPLASH efervescente | 400ms | Champagne impact |
| Impacto joia | CRASH cristalino + reverb de pedra preciosa | 350ms | Joia impact |
| Impacto perfume | PSSSH de spray + cough toxico | 400ms | Perfume impact |
| Dinheiro explodindo | FWOOSH de papel + tilintar de moedas | 600ms | Frames 13-14 |
| Idle | Hum eletronico sutil + "bling" periodico | loop 2000ms | Frames 17-18 |
| Guilhotina (special) | WHOOSH pesado crescendo + SLAM metalico | 800ms | Frames 19-21 |
| "APROVADO!" | Voz de maquininha de cartao amplificada + fanfarra | 1000ms | Frames 27-29 |
| Bordao Janja | "Isso vai pro cartao corporativo!" / "Compra aprovada, amor!" | 1500ms | Random 25% |

---

## Mecanica do Ataque (Game Design Notes)

### Ataque Normal: Luxury Rain
1. Janja passa o cartao (swipe, 300ms)
2. Flash de transacao (200ms)
3. 3-5 itens de luxo ALEATORIOS caem do ceu em area (AoE cone, 120px frente)
4. Cada item e selecionado aleatoriamente dos 5 tipos
5. Cada item gira ao cair (rotation frames)
6. No impacto, cada item explode em notas de dinheiro
7. "APROVADO!" aparece apos cada explosao

### Dano por Tipo de Item
| Item | Dano | Efeito Especial |
|---|---|---|
| Bolsa | 12 HP | Slow 2s (peso da bolsa esmaga) |
| Sapato | 18 HP | Perfuração (ignora 30% defesa) |
| Champagne | 10 HP | AoE splash 24px (espuma) |
| Joia | 15 HP | Stun 1.5s (cegueira do brilho) |
| Perfume | 8 HP | Poison 3s, 3HP/s (nuvem toxica) |

### Special Attack: Cartao Guilhotina
- Cooldown: 15s
- Um cartao GIGANTE desce do ceu como guilhotina
- AoE: linha reta, 160px comprimento, 32px largura
- Dano: 50 HP + knockback massivo
- "Sangue dourado" no impacto
- Todos os inimigos na area sao empurrados para os lados

---

## Interacoes Especiais

### Contra Bolsonaro
- Bolsonaro ROUBA 1 projetil de luxo 20% das vezes ("privatizacao")
- O item roubado cura Bolsonaro 5 HP
- Janja: "LADRAAAO!" (texto onomatopeico vermelho)

### Contra Daciolo
- Projeteis de luxo sao REPELIDOS pela aura de fe de Daciolo (30% de deflect)
- Itens deflectidos caem no chao sem explodir
- Daciolo: "Dinheiro nao compra a GLORIA!"

### Contra Lula
- ZERO dano -- Lula e protegido (aliado)
- Em vez de dano, itens de luxo que atingem Lula se transformam em CERVEJA (cura 5 HP)
- "E nois, companheira!"

### Contra BolsoLula (boss fusion)
- Dano normal na metade Bolsonaro
- Itens se transformam em cerveja na metade Lula
- Se acertar no CENTRO: cartao CLONA -- spawna 2 cartoes atacando (dano 1.5x)

---

## Art Generation Prompts

### Style Preamble (prepend to ALL prompts)
```
Style: grotesque underground comix, Robert Crumb inspired, thick uneven black outlines,
heavy shadows, saturated-dirty colors, pixel art 32x32, top-down isometric perspective,
Brazilian satirical political cartoon, B-movie horror meets vulgar wealth, intentionally
rough and asymmetric. Everything screams OBSCENE WEALTH and CONSUMER EXCESS. Gold
everywhere, tasteless luxury, grotesque opulence.
```

### Frame 0: Static / Inventory Icon

**Stable Diffusion / DALL-E:**
```
A grotesquely oversized gold/platinum credit card viewed from above in top-down isometric
perspective, pixel art 32x32 pixels. The card is OBSCENELY golden and shiny (#C4A020),
impossibly thick for a credit card. Visible EMV chip in gold, embossed numbers "666 666 666
666" across the middle, text "PRIMEIRA DAMA LTDA" below. A fictional card brand logo in the
corner with a fat dollar sign symbol in red. Magnetic stripe visible on edge. Multiple shine
highlights suggesting polished metal surface. Thick uneven black outlines (2px), Robert Crumb
underground comix style. Drop shadow beneath. Transparent background. The card oozes vulgar
wealth. Game weapon sprite asset.
```

**Midjourney:**
```
/imagine pixel art 32x32, top-down view of grotesquely oversized gold platinum credit card,
obscenely shiny, embossed "666" numbers, fat dollar sign logo, EMV chip, Robert Crumb thick
outlines underground comix, vulgar wealth aesthetic, satirical Brazilian political cartoon,
game weapon sprite, transparent background --ar 1:1 --s 250 --no photorealistic
```

### Frames 1-3: Swipe Attack

**Stable Diffusion / DALL-E:**
```
Three frame sprite sheet (96x32) of a gold credit card being swiped as an attack weapon,
pixel art 32x32 per frame. Frame 1: Card drawn at angle, motion blur, golden sparkles.
Frame 2: Card horizontal mid-swipe, massive white/green transaction flash from chip, digital
energy lines, dollar signs cascading. Frame 3: Card stabilizing, tiny luxury item silhouettes
falling from above, mini receipt materializing. Underground comix style, thick outlines.
Transparent background. Game attack animation. The card IS the weapon.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 96x32, 3 frames of gold credit card swipe attack, drawn
brandished like weapon, transaction energy flash, luxury items summoned falling, Robert Crumb
underground comix thick outlines, game attack animation, transparent background --ar 3:1 --s 250
```

### Frames 4-8: Luxury Projectiles (Individual Items)

**Stable Diffusion / DALL-E:**
```
Five pixel art sprites in a row (160x32 sprite sheet), each 32x32, showing luxury items as
grotesque projectiles flying through air. Item 1: Oversized pink designer handbag with absurd
gold hardware, price tag dangling. Item 2: Red stiletto high heel shoe with impossibly tall
spike heel like a weapon. Item 3: Dark champagne bottle with gold label, cork popping, foam
spraying. Item 4: Enormous sapphire ring with comically thick gold band, sparkle rays. Item 5:
Art-deco perfume bottle with toxic purple mist cloud trailing behind. All items are
GROTESQUELY oversized and OFFENSIVELY luxurious. Robert Crumb underground comix style, thick
outlines. Each item spinning in flight. Transparent background. Game projectile sprites.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 160x32, 5 luxury item projectile sprites 32x32 each, pink
designer bag with gold hardware, red stiletto heel weapon, champagne bottle popping, giant
sapphire ring sparkling, perfume bottle with purple toxic cloud, all grotesquely oversized
and offensively luxurious, Robert Crumb underground comix, game projectile sprites, transparent
background --ar 5:1 --s 250
```

### Frames 13-16: Money Explosion

**Stable Diffusion / DALL-E:**
```
Four frame sprite sheet (128x32) showing money explosion on impact, pixel art 32x32 per frame.
Frame 1: Starburst with money bills starting to burst outward, white flash. Frame 2: MAXIMUM
explosion of green money bills and gold coins flying in all directions, 360 degrees radial.
Frame 3: Money raining down with gravity, coins bouncing, long receipt unfurling. Frame 4:
Bills settled on ground, last coin falling, golden glow residue at impact point. Underground
comix style, thick outlines. The money explosion is OBSCENELY abundant. Transparent background.
Game impact VFX.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 128x32, 4 frames of money explosion impact, bills and coins
bursting flying raining settling, green money gold coins, obscenely abundant cash explosion,
Robert Crumb underground comix, game impact VFX animation, transparent background --ar 4:1 --s 250
```

### Frames 19-21: Special Guillotine Attack

**Stable Diffusion / DALL-E:**
```
Three frame sprite sheet (96x32) of a GIANT gold credit card descending from above like a
guillotine, pixel art 32x32 per frame. Frame 1: Enormous card appearing at top of frame,
sharp bottom edge gleaming like a blade, massive shadow below. Frame 2: Card 60% descended,
blade edge reflecting light, money bills pushed aside by wind, golden particles. Frame 3:
Card SLAMS into ground, massive impact, money bills explode sideways, ground cracks, golden
"blood" sprays, green "APROVADO!" text flashes. Underground comix style. The credit card is
a WEAPON OF FINANCIAL DESTRUCTION. Transparent background. Game special attack animation.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 96x32, 3 frames of giant gold credit card descending like
guillotine from above, sharp blade edge gleaming, slamming into ground with money explosion
and golden blood, ground cracking, "APROVADO" text, Robert Crumb underground comix, game
special attack animation, transparent background --ar 3:1 --s 250
```

### Frames 27-29: "APROVADO!" Effect

**Stable Diffusion / DALL-E:**
```
Three frame sprite sheet (96x32) of comic book onomatopoeia "APROVADO!" text effect, pixel art
32x32 per frame. Frame 1: Bold chunky green (#00AA44) hand-lettered "APROVADO!" appearing with
gold shadow, dollar signs orbiting, receipt materializing behind. Frame 2: Text at maximum size,
vibrating letters, multiple dollar signs, red approval stamp circle overlaid, mini money bills
flying from corners. Frame 3: Text fading to 50%, receipt curling away, invoice dropping down,
bills settling. Underground comix style hand-lettered text, intentionally rough. Transparent
background. Game VFX text effect.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 96x32, 3 frames of "APROVADO!" comic text effect green with
gold, approval stamp, dollar signs orbiting, money bills, receipt, fading transition, Robert
Crumb underground comix hand-lettered style, game VFX, transparent background --ar 3:1 --s 250
```

---

## Post-Processing Notes
- Limpar para grid exato de 32x32 pixels por frame
- Contornos pretos GROSSOS e IRREGULARES (2px minimo)
- Transparencia limpa sem artefatos
- Cores ajustadas aos hex codes da paleta -- o DOURADO deve ser consistente em todos os frames
- O brilho do cartao deve ser EXCESSIVO mas nao clean -- e brilho GROTESCO, nao elegante
- Os numeros "666 666 666 666" devem ser legiveis quando possivel
- Cada item de luxo deve ter personalidade propria mas compartilhar a estetica "excesso vulgar"
- Notas de dinheiro devem parecer REAIS (verde com cifrao) mas em escala de pixel art
- O logo "GASTAO CARD" deve ser parodia reconhecivel de logos de bandeiras de cartao
- Montar sprite sheet horizontal final: 960x32 (30 frames)
- Assimetria intencional -- nada perfeito, nada elegante, tudo GROTESCAMENTE rico

## Notes for Artist
- O Cartao Corporativo e a arma mais SATIRICA do jogo -- cada ataque e uma compra publica absurda
- O humor esta na transformacao: arma -> compra -> item de luxo -> projetil mortal -> dinheiro explodindo -> fatura
- O ciclo completo de um ataque conta uma HISTORIA de consumismo descontrolado
- Cada item de luxo deve ser reconhecivel mas EXAGERADO -- a bolsa e grande demais, o salto alto demais, a joia brilhante demais
- O "APROVADO!" e o equivalente do "GLORIA!" do Daciolo mas para consumismo -- igualmente dramatico
- O special da guilhotina e a PECA DE RESISTENCIA -- um cartao do tamanho de uma guilhotina e absurdo o suficiente para funcionar
- O "sangue dourado" no impacto da guilhotina reforça que neste mundo, ate violencia e DOURADA
- O numero "666" no cartao e OBVIO E PROPOSITAL -- nao e sutil, e COMIX
- Os projeteis de luxo devem parecer itens de catalogo de revista de alto padrao mas desenhados por Robert Crumb em dia de raiva
- A mosca do perfume sao CORACOES -- parodia de propaganda de perfume
- NUNCA faca o cartao parecer um cartao real -- e uma PARODIA grotesca que ninguem pode confundir
- Robert Crumb style: riqueza obscena desenhada com repulsa, cada brilho dourado e um comentario sobre excesso
