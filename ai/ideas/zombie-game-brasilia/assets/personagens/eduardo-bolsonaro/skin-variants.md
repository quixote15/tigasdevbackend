# Eduardo Bolsonaro (Bananinha) - Skin Variants

## Overview
- **Total de Skins:** 5
- **Dimensoes:** 64x64px por frame (mantém specs do sprite base)
- **Formato:** PNG com transparencia
- **Estrutura:** Cada skin tem sprite sheets completos (idle, walk, attack, death, hit, special)
- **Desbloqueio:** Sistema progressivo (gameplay ou Easter eggs)

---

## SKIN 0: Normal (Default)
**Arquivo Prefixo:** `eduardo_default_`
**Condicao de Desbloqueio:** Disponivel desde o inicio

### Descricao Visual
A skin padrao de Eduardo Bolsonaro (Bananinha). A referencia canonica para todas as outras skins.

| Elemento         | Descricao                                           | Cor Principal |
|------------------|-----------------------------------------------------|---------------|
| Cabelo           | Loiro, penteado pro lado, fios soltos               | `#D4A017`     |
| Rosto            | LUNAR, redondo desproporcional, sem queixo           | `#F5C6A0`     |
| Olhos            | Enormes, cachorro abandonado, lacrimejantes          | `#5DADE2`     |
| Camiseta         | Selecao brasileira (amarela, gola verde), camelô     | `#F7DC6F`     |
| Shorts           | Azul basico                                          | `#2E86C1`     |
| Mao Direita      | Segurando alca da mala de viagem marrom              | `#8B5E3C`     |
| Mao Esquerda     | Segurando banana                                     | `#F9E154`     |
| Acessorios       | Nenhum extra                                         | --            |

### Notas
- Esta e a base. Todas as deformidades anatomicas (rosto lunar, olhos de cachorro, queixo zero, mala grudada) sao OBRIGATORIAS em todas as skins
- A camiseta e de camelô -- costura torta, tecido barato, numero "17" mal estampado
- A banana e normal, amarela, classica

### Bordoes Exclusivos
- Sem bordoes exclusivos (usa o set default)

---

## SKIN 1: Exilado 2026 (Bananinha Americana)
**Arquivo Prefixo:** `eduardo_exilado_`
**Condicao de Desbloqueio:** Completar a fase "Aeroporto de Guarulhos" ou encontrar Easter egg do passaporte

### Descricao Visual
Eduardo apos fugir para os Estados Unidos em marco/2025. Look americanizado, turistao brasileiro perdido na Flórida. A encarnacao do meme "Bananinha Americana".

| Elemento         | Descricao                                              | Cor Principal |
|------------------|--------------------------------------------------------|---------------|
| Cabelo           | Mesmo loiro, mas com bone MAGA vermelho por cima       | `#CC2020`     |
| Rosto            | Identico (lunar, sem queixo), mas BRONZEADO FAKE       | `#E8A065`     |
| Olhos            | Mesmos olhos de cachorro, agora com oculos de sol no topo da cabeca (NAO nos olhos, empurrados pra cima) | `#1A1A1A` |
| Camiseta         | Camiseta estampada "I LOVE FLORIDA" branca, letras vermelhas/rosas, com palmeira | `#F0F0E8` |
| Shorts           | Bermudão cargo americano, caqui, bolsos exagerados     | `#C4A86A`     |
| Calcado          | Crocs verdes (visivel em top-down como manchas verdes nos pés) | `#27AE60` |
| Mao Direita      | MESMA mala de viagem, mas agora com adesivos (bandeira EUA, Mickey Mouse, "MAGA") | `#8B5E3C` |
| Mao Esquerda     | Banana, mas agora com bandeirinha americana espetada nela | `#F9E154` + `#3C3B6E` |
| Acessorios Extra | Pochete na cintura (fanny pack), preta                 | `#2C2C2C`     |

### Paleta de Cores Adicional

| Elemento              | Hex Code  | Usage                             |
|-----------------------|-----------|-----------------------------------|
| Bone MAGA Vermelho    | `#CC2020` | Base do bone                      |
| Bone MAGA Texto       | `#FFFFFF` | "MAGA" escrito na frente          |
| Pele Bronzeada Fake   | `#E8A065` | Tom de pele mais laranja           |
| Camiseta Branca       | `#F0F0E8` | Base da camiseta I LOVE FLORIDA   |
| Camiseta Texto Rosa   | `#E74C3C` | Coração e texto "LOVE"            |
| Bermuda Caqui         | `#C4A86A` | Bermudao cargo                    |
| Bermuda Caqui Shadow  | `#A08850` | Sombras/dobras da bermuda         |
| Crocs Verde           | `#27AE60` | Crocs nos pes                     |
| Pochete Preta         | `#2C2C2C` | Pochete/fanny pack                |
| Adesivo EUA           | `#3C3B6E` | Adesivo bandeira americana na mala|
| Oculos Escuros        | `#1A1A1A` | Oculos de sol no topo da cabeca   |

### Mudancas de Animacao
- **Walk:** Crocs fazem barulho diferente (`sfx_crocs_flop` em vez de `sfx_step`). O flip-flop dos Crocs adiciona 1px de bounce extra nos pes
- **Idle:** Puxa o celular do bolso da bermuda cargo pra tirar selfie no Frame 2 (em vez de olhar pro lado procurando o pai, ele olha pro celular)
- **Attack:** Banana com bandeirinha americana gira mais (a bandeira cria drag visual, trail azul-vermelho-branco)
- **Death:** Em vez de fantasma com bandeira EUA, fantasma tenta entrar num aviao minusculo (referencia a fuga)
- **Special Fuga:** No residuo, em vez de pena de galinha, cai um cartao de embarque

### Bordoes Exclusivos
```
"Preciso fazer algo importantíssimo aqui na Disney!"
"Isso aqui é que é liberdade, taokay?"
"Gente, o In-N-Out Burger é brilhante!"
"Pai, estou protegendo a democracia... de longe!"
"Make Bolsonaro Great Again!"
```

### Referencia Memetica
- Meme do "Bananinha Americana" (março 2025)
- Comparacoes com turista brasileiro perdido em Orlando
- Bone MAGA como declaracao de alianca politica (e moda questionavel)
- Crocs como calçado definitivo do brasileiro nos EUA

---

## SKIN 2: Zombie (Zumbi Bananinha)
**Arquivo Prefixo:** `eduardo_zombie_`
**Condicao de Desbloqueio:** Morrer 10 vezes com Eduardo OU completar o modo "Outbreak"

### Descricao Visual
Eduardo zumbificado. A versao morta-viva mantém TODAS as deformidades originais mas amplificadas pelo horror. O rosto lunar agora e uma lua PODRE. Os olhos de cachorro agora sao olhos de cachorro MORTO. A mala continua grudada (ate a morte nao separa).

| Elemento         | Descricao                                              | Cor Principal |
|------------------|--------------------------------------------------------|---------------|
| Cabelo           | Loiro agora esverdeado, ralo, caindo em tufos. Couro cabeludo visivel (cinza-esverdeado) | `#8B9A3C` |
| Rosto            | Lunar AINDA MAIS INCHADO (edema pos-mortem), verde-acinzentado. Veias visiveis (roxas). Pedaço do labio faltando no lado esquerdo, mostrando dentes | `#7A8B5A` |
| Olhos            | MESMOS olhos enormes de cachorro, mas agora um esta normal (pupila dilatada, amarelada) e o outro esta CAIDO (pendurado no nervo otico, fora da orbita, balancando) | `#C8C830` |
| Camiseta         | Selecao brasileira RASGADA e manchada de sangue seco (marrom-escuro). Numero 17 parcialmente visivel. Buracos mostrando pele verde embaixo | `#B8A43C` (amarelo sujo) |
| Shorts           | Azul agora cinza-azulado, rasgado na barra, manchas escuras | `#5A6A7A` |
| Mao Direita      | Ossos dos dedos visiveis, mas AINDA segurando a mala. Mala agora coberta de limo verde | `#3A5E3C` |
| Mao Esquerda     | Segurando banana PODRE (marrom-preta, com moscas). 2 dedos faltando | `#4A3A20` |
| Pele             | Verde-acinzentado com manchas roxas de decomposicao. Pedacos faltando no braco | `#7A8B5A` |
| Extras           | Vermes (1-2px rosa) saindo do pescoco. Mosca orbitando a banana podre | `#E8A0B0` |

### Paleta de Cores Adicional

| Elemento                | Hex Code  | Usage                              |
|-------------------------|-----------|-------------------------------------|
| Pele Zombie Base        | `#7A8B5A` | Tom verde-cinzento de pele morta    |
| Pele Zombie Light       | `#9AAB7A` | Highlights (areas inchadas)         |
| Pele Zombie Dark        | `#5A6B3A` | Sombras profundas                   |
| Veias Roxas             | `#6A3A7A` | Veias visiveis no rosto             |
| Sangue Seco             | `#5A2A1A` | Manchas na roupa                    |
| Sangue Fresco           | `#AA2020` | Gotejando do labio rasgado          |
| Olho Amarelado          | `#C8C830` | Iris do olho "bom"                  |
| Olho Morto              | `#E8E8D0` | Olho pendurado (esbranquicado)      |
| Banana Podre            | `#4A3A20` | Banana em decomposicao              |
| Limo Verde              | `#3A5E3C` | Limo na mala e roupas               |
| Vermes                  | `#E8A0B0` | Vermes saindo do corpo              |
| Moscas                  | `#1A1A1A` | Pontinhos pretos orbitando          |
| Cabelo Esverdeado       | `#8B9A3C` | Cabelo em decomposicao              |
| Dentes Expostos         | `#D8D0A0` | Dentes visiveis pelo labio rasgado  |

### Mudancas de Animacao
- **Idle:** Corpo balança como se fosse cair (rigor mortis irregular). O olho pendurado balanca como pendulo (1px oscilação). Moscas orbitam a banana podre (2 particulas pretas, circulo de 8px raio)
- **Walk:** Mancando. Frame rate REDUZIDO para 6 fps (mais lento, arrastado). Uma perna arrasta (marca no chão). A mala agora RANGE (particulas de ferrugem/limo caindo). Gemido zombie constante como audio
- **Attack:** Arremessa a banana PODRE. Ela se despedaca no ar, gerando particulas de banana podre (marrom) e moscas extras. Trail de gosma ao inves de limpo. Dano causa envenenamento (DOT: 3 dmg/sec por 3 sec)
- **Death:** Como ja e zombie... a "morte" e DESMONTAGEM. Frame 0: cabeça cai pro lado. Frame 1: bracos se separam (mao direita AINDA segura a mala enquanto cai). Frame 2: corpo colapsa em pilha. Frame 3: poça de gosma verde se expande. SEM fantasma (ele ja e o fantasma)
- **Special Fuga:** Em vez de teleporte limpo, ele se DESINTEGRA em moscas/vermes, reaparecendo em outro lugar como as moscas se reagrupam. Nojento. Efetivo

### Bordoes Exclusivos
```
"Paaaaaai... braaaains..."
"Embaaaixaaadaaaa..."
"Brilhaaanteee..."
"*gemido zombie ininteligivel*"
"Baaanaaanaaaa..."
```

### Notas de Estilo
- O HORROR e a piada aqui. Mesmo como zombie, o mais patetico do bando
- O olho pendurado e a feature principal -- ele balanca em TODA animacao
- A mala grudada na mao ossificada e body horror real
- A banana podre atrai moscas o tempo todo (ambient particles)
- Os olhos de cachorro abandonado AINDA estao presentes no olho que funciona. Mesmo morto ele e patetico

---

## SKIN 3: Bananas de Pijama
**Arquivo Prefixo:** `eduardo_bananapijama_`
**Condicao de Desbloqueio:** Easter egg -- encontrar 10 bananas escondidas no mapa OU digitar "B1B2" no menu

### Descricao Visual
Eduardo vestido como um dos Bananas de Pijama (B1 ou B2, o programa infantil australiano). Referencia direta ao apelido "Bananinha". Visual absurdo, comico, completamente fora de contexto num jogo de zombie.

| Elemento         | Descricao                                              | Cor Principal |
|------------------|--------------------------------------------------------|---------------|
| Corpo Inteiro    | Fantasia de banana amarela cobrindo o corpo todo. Formato de banana curvo de cima a baixo. O rosto lunar de Eduardo sai pelo buraco central | `#FFE135` |
| Rosto            | IDENTICO ao default (lunar, sem queixo, olhos de cachorro). Sai do meio da fantasia de banana como se fosse a abertura facial | `#F5C6A0` |
| Olhos            | Mesmos olhos de cachorro lacrimejantes, mas agora parecendo ainda mais ridiculos saindo de uma banana | `#5DADE2` |
| Pijama           | Listras azuis e brancas no pijama por baixo da fantasia de banana. Visivel nos bracos e pernas | `#5DADE2` + `#FFFFFF` |
| Pes              | Pantufas de banana (amarelas, formato de banana nos pes) | `#F0C040` |
| Mao Direita      | Segurando a mala, mas agora a mala tem adesivo de banana | `#8B5E3C` |
| Mao Esquerda     | Segurando banana REAL (ironia de banana segurando banana) | `#F9E154` |
| Acessorios       | Gorro de dormir listrado azul-branco no topo da cabeca | `#5DADE2` + `#FFFFFF` |

### Paleta de Cores Adicional

| Elemento              | Hex Code  | Usage                              |
|-----------------------|-----------|-------------------------------------|
| Fantasia Banana Base  | `#FFE135` | Corpo da fantasia amarela           |
| Fantasia Banana Dark  | `#C8A800` | Sombras/dobras da fantasia          |
| Fantasia Banana Light | `#FFF06A` | Highlights                          |
| Pijama Azul           | `#5DADE2` | Listras azuis do pijama             |
| Pijama Branco         | `#FFFFFF` | Listras brancas do pijama           |
| Gorro Topo            | `#5DADE2` | Gorro de dormir                     |
| Gorro Pompom          | `#FFFFFF` | Pompom do gorro                     |
| Pantufa Base          | `#F0C040` | Pantufas de banana                  |

### Mudancas de Animacao
- **Idle:** A fantasia de banana balanca como roupa oversized. O pompom do gorro oscila (1px, independente). Eduardo parece DESCONFORTAVEL dentro da fantasia (se coçando no Frame 2)
- **Walk:** Mais desajeitado que o normal (fantasia atrapalha). Os pes em pantufas de banana escorregam (Frame 4 do tropeco agora tem ESCORREGAO em vez de tropeco -- banana peel no proprio pe). Frame rate reduzido pra 8 fps (fantasia pesada)
- **Attack:** Arremessa banana com tanto fervor que a fantasia desloca (gira 10 graus). A fantasia voltando ao lugar e parte da animacao de recovery
- **Death:** A fantasia "descasca" como uma banana real. Frame por frame a casca de banana amarela se abre revelando Eduardo de pijama listrado por baixo, caido, patetico, de pijama
- **Special Fuga:** Desliza dentro da fantasia como se estivesse escorregando numa casca de banana. Smoke e amarelo em vez de cinza. Residuo: casca de banana no chao

### Bordoes Exclusivos
```
"Bananas de Pijama descendo a escada!"
"Eu sou o B1! ...ou B2? Esqueci."
"São iguais mas não são! ...Espera, sou eu mesmo."
"Tá na hora de brincar? NÃO, TÁ NA HORA DE FUGIR!"
"*cantarola o tema dos Bananas de Pijama*"
```

### Notas de Estilo
- A skin e 100% COMICA. Zero seriedade
- A fantasia de banana deve ser BAGGY e mal-ajustada, como se fosse alugada
- O contraste do rosto patetico de Eduardo saindo de uma fantasia de banana e a piada
- As listras do pijama sao referencia direta ao programa de TV
- O gorro de dormir com pompom adiciona ao absurdo
- BANANA segurando BANANA -- a meta-ironia deve ser visivel

---

## SKIN 4: Ronald McDonald (Bananinha McFugitive)
**Arquivo Prefixo:** `eduardo_ronald_`
**Condicao de Desbloqueio:** Visitar 5 lanchonetes no mapa OU derrotar o mini-boss "Gerente da Loja" no modo arcade

### Descricao Visual
Eduardo vestido como Ronald McDonald. Referencia direta aos memes da internet que compararam Eduardo a Ronald McDonald apos a fuga para os EUA em 2025. A parodia perfeita: o palhaco da politica brasileira literalmente vestido de palhaco.

| Elemento         | Descricao                                              | Cor Principal |
|------------------|--------------------------------------------------------|---------------|
| Cabelo           | PERUCA VERMELHA de palhaco por cima do cabelo loiro (tufos loiros saindo pelas bordas) | `#CC2020` |
| Rosto            | Lunar, sem queixo, MAS agora com maquiagem de palhaco: nariz vermelho esponja (6x6px), boca pintada de branco estendida, bochechas com circulos vermelhos | `#F5C6A0` + `#CC2020` |
| Olhos            | Mesmos olhos de cachorro, mas com sombra amarela ao redor (maquiagem). As lagrimas borram a maquiagem | `#5DADE2` |
| Roupa Superior   | Macacao amarelo com listras vermelhas verticais (uniforme palhaco McDonald's). Gola de palhaco branca com bolinhas vermelhas | `#FFE135` + `#CC2020` |
| Roupa Inferior   | Calcas amarelas do macacao, muito largas, sapatões de palhaco vermelhos (enormes, 8px cada pe) | `#FFE135` |
| Sapatos          | Sapatões GIGANTES de palhaco vermelho (desproporcional - quase do tamanho da cabeca) | `#CC2020` |
| Mao Direita      | Segurando a mala, mas mala agora parece caixa de Happy Meal gigante (vermelha com arcos amarelos) | `#CC2020` + `#FFE135` |
| Mao Esquerda     | Em vez de banana, segura um MILKSHAKE (copo vermelho com canudo). O milkshake vira o projetil | `#CC2020` + `#F0C040` |
| Acessorios       | Luvas brancas oversize (tipo Mickey Mouse). Flor de brincadeira na lapela (que espirra agua) | `#FFFFFF` |

### Paleta de Cores Adicional

| Elemento              | Hex Code  | Usage                              |
|-----------------------|-----------|-------------------------------------|
| Peruca Vermelha       | `#CC2020` | Cabelo de palhaco                   |
| Peruca Dark           | `#8B1515` | Sombras da peruca                   |
| Nariz Esponja         | `#E74C3C` | Nariz de palhaco (GRANDE)           |
| Maquiagem Branca      | `#F8F8F0` | Base de maquiagem no rosto          |
| Maquiagem Bochecha    | `#CC2020` | Circulos nas bochechas              |
| Macacao Amarelo       | `#FFE135` | Base do uniforme                    |
| Listras Vermelhas     | `#CC2020` | Listras no macacao                  |
| Gola Palhaco Branca   | `#FFFFFF` | Gola com babados                    |
| Gola Bolinhas         | `#CC2020` | Bolinhas vermelhas na gola          |
| Sapatão Vermelho      | `#CC2020` | Sapatões gigantes                   |
| Sapatão Sola          | `#8B1515` | Sola dos sapatões                   |
| Happy Meal Box        | `#CC2020` | "Mala" de Happy Meal                |
| Arcos Dourados        | `#FFE135` | Logo "M" na caixa (parodia)        |
| Milkshake Copo        | `#CC2020` | Copo do milkshake                   |
| Milkshake Liquido     | `#F0C040` | Milkshake de banana (amarelo)       |
| Luvas Brancas         | `#FFFFFF` | Luvas de palhaco                    |

### Mudancas de Animacao
- **Idle:** Os sapatões gigantes fazem o idle comico -- ele tenta manter equilibrio com pes enormes. Nariz de esponja pulsa 1px (squash/stretch). A maquiagem derrete levemente com as lagrimas (lagrimas deixam trilha na maquiagem branca, revelando pele embaixo)
- **Walk:** ABSOLUTAMENTE DESAJEITADO. Sapatões batem um no outro. O tropeco do Frame 4 agora e TRIPLO -- ele tropeca nos proprios sapatões, na caixa de Happy Meal, e nos cadarcos. Frame rate: 8 fps (mais lento, cada passo e uma aventura). Som: `sfx_clown_shoes_flop` (slap cômico)
- **Attack:** Arremessa o MILKSHAKE em vez de banana. O milkshake explode ao atingir (splash de liquido amarelo). Trail: gotas de milkshake (particulas amarelo-creme). Ao retornar (boomerang), o copo volta vazio. Sound: `sfx_milkshake_splash`
- **Death:** Frame 0: nariz de esponja cai primeiro (BOING). Frame 1: peruca voa. Frame 2: maquiagem derrete revelando rosto patetico por baixo. Frame 3: em vez de fantasma, sai um balao de helio com formato do rosto dele (referencia baloes de festa). Buzina de palhaco toca
- **Special Fuga:** Entra num carro minusculo de palhaco (4 frames de miniatura vermelha aparecendo, ele se espremendo dentro, carro saindo com buzina). Residuo: confetes e uma buzina de palhaco no chao

### Projetil Alternativo: Milkshake
**Sprite Sheet:** `eduardo_ronald_milkshake_projectile.png` -- 128x32px (4 frames)
- Frame 0: Copo de milkshake horizontal (vermelho, canudo, liquido amarelo)
- Frame 1: Copo girando 45 graus, milkshake espirra gotas
- Frame 2: Copo girando 90 graus, mais gotas
- Frame 3: Copo girando 135 graus, trilha de gotas
- Ao impactar: SPLASH de milkshake (particulas amarelo-creme, raio 16px, 8 particulas)
- Inimigos atingidos ficam com mancha amarela por 2 segundos (visual de milkshake)

### Bordoes Exclusivos
```
"Amo muito tudo isso! ...Menos zumbis!"
"Isso é um McLanche Feliz? NÃO!"
"Ba da ba ba baaaa! ...AI!"
"Pedido pra viagem! Viagem pra LONGE!"
"Aceita Pix? Não? Cartão do pai?"
"Me confundiram com o Ronald de novo..."
```

### Referencia Memetica
- Memes da internet comparando Eduardo a Ronald McDonald (2025)
- A fuga pro exterior = "McFugitive"
- Palhaco da politica vestido de palhaco = meta-humor
- Happy Meal como mala de viagem = consumismo da fuga
- Maquiagem derretendo com lagrimas = mascara caindo (literal e figurativamente)

---

## Matriz de Sprites por Skin

Cada skin precisa dos seguintes sprite sheets:

| Sprite Sheet              | Frames | Tamanho Sheet | Default | Exilado | Zombie | Banana Pijama | Ronald |
|---------------------------|--------|---------------|---------|---------|--------|---------------|--------|
| `*_idle.png`              | 4      | 256x64        | Sim     | Sim     | Sim    | Sim           | Sim    |
| `*_walk.png`              | 6      | 384x64        | Sim     | Sim     | Sim    | Sim           | Sim    |
| `*_attack.png`            | 3      | 192x64        | Sim     | Sim     | Sim    | Sim           | Sim    |
| `*_death.png`             | 4      | 256x64        | Sim     | Sim     | Sim    | Sim           | Sim    |
| `*_hit.png`               | 2      | 128x64        | Sim     | Sim     | Sim    | Sim           | Sim    |
| `*_special_fuga.png`      | 6      | 384x64        | Sim     | Sim     | Sim    | Sim           | Sim    |
| `*_buff_puxasaco.png`     | 4      | 256x64        | Sim     | Sim     | -      | Sim           | Sim    |
| `*_debuff_orfao.png`      | 4      | 256x64        | Sim     | Sim     | -      | Sim           | Sim    |
| `*_projectile.png`        | 4      | 128x32        | Banana  | Banana+Flag | Banana Podre | Banana | Milkshake |

**Total de arquivos por skin:** 9 sprite sheets
**Total geral:** 45 sprite sheets (5 skins x 9 sheets) + skins do Zombie sem buff/debuff = 43

---

## Skin Selection UI

### Thumbnail Preview (para menu de selecao)
- **Tamanho:** 96x96px por thumbnail
- **Formato:** Frame 0 do idle de cada skin, escalado 1.5x
- **Layout:** Horizontal, 5 thumbnails lado a lado
- **Background:** Fundo cinza escuro (#1A1A1A) com borda fina (#F7DC6F amarela para skin selecionada)
- **Lock Icon:** Cadeado 16x16px sobre skins nao desbloqueadas (cinza, 70% opacity)

### Nomes de Display no Menu

| Skin           | Nome no Menu              | Subtitulo                           |
|----------------|---------------------------|-------------------------------------|
| Default        | "Bananinha"               | "O eterno puxa-saco"                |
| Exilado 2026   | "Bananinha Americana"     | "Fugiu pra Disney"                  |
| Zombie         | "Zumbi Bananinha"         | "Nem morto larga a mala"            |
| Banana Pijama  | "B1 (ou B2?)"             | "Descendo a escada pro inferno"     |
| Ronald McDonald| "McFugitive"              | "Amo muito fugir de tudo isso"      |

### Implementacao Phaser 3
```javascript
const EDUARDO_SKINS = {
    default:   { prefix: 'eduardo_default_',   unlocked: true,  name: 'Bananinha' },
    exilado:   { prefix: 'eduardo_exilado_',   unlocked: false, name: 'Bananinha Americana' },
    zombie:    { prefix: 'eduardo_zombie_',    unlocked: false, name: 'Zumbi Bananinha' },
    banana:    { prefix: 'eduardo_bananapijama_', unlocked: false, name: 'B1 (ou B2?)' },
    ronald:    { prefix: 'eduardo_ronald_',    unlocked: false, name: 'McFugitive' }
};

function loadSkinSprites(skinKey) {
    const skin = EDUARDO_SKINS[skinKey];
    const prefix = skin.prefix;

    this.load.spritesheet(`${prefix}idle`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}idle.png`, { frameWidth: 64, frameHeight: 64 });
    this.load.spritesheet(`${prefix}walk`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}walk.png`, { frameWidth: 64, frameHeight: 64 });
    this.load.spritesheet(`${prefix}attack`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}attack.png`, { frameWidth: 64, frameHeight: 64 });
    this.load.spritesheet(`${prefix}death`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}death.png`, { frameWidth: 64, frameHeight: 64 });
    this.load.spritesheet(`${prefix}hit`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}hit.png`, { frameWidth: 64, frameHeight: 64 });
    this.load.spritesheet(`${prefix}special_fuga`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}special_fuga.png`, { frameWidth: 64, frameHeight: 64 });

    if (skinKey !== 'zombie') {
        this.load.spritesheet(`${prefix}buff_puxasaco`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}buff_puxasaco.png`, { frameWidth: 64, frameHeight: 64 });
        this.load.spritesheet(`${prefix}debuff_orfao`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}debuff_orfao.png`, { frameWidth: 64, frameHeight: 64 });
    }

    // Projetil
    const projectileKey = skinKey === 'ronald' ? 'milkshake' : 'banana';
    this.load.spritesheet(`${prefix}projectile`, `assets/personagens/eduardo-bolsonaro/skins/${skinKey}/${prefix}${projectileKey}_projectile.png`, { frameWidth: 32, frameHeight: 32 });
}
```

---

## Notas Finais para o Artista

1. **TODAS as skins mantêm as deformidades base**: rosto lunar, olhos de cachorro, queixo inexistente, mala grudada
2. A skin apenas VESTE o personagem diferente -- a essência patética permanece
3. Skins mais absurdas (Banana Pijama, Ronald) devem ter o contraste entre a fantasia ridicula e a expressao miseravel
4. A skin Zombie e a unica que altera a ANATOMIA (decomposicao), todas as outras sao cosmeticas
5. Projeteis alternativos (milkshake do Ronald) devem ter o mesmo comportamento boomerang, so muda o visual
6. Cada skin deve ser imediatamente reconhecivel em 64x64px -- testar em escala 1:1 antes de finalizar
7. Manter consistencia de outlines grossos e estilo underground comix em TODAS as skins
8. A mala e o item mais persistente -- ela aparece em TODA skin, em TODA animacao. E a mala da fuga. E a alma dele
