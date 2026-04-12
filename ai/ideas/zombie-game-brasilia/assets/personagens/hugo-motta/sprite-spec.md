# HUGO MOTTA (O Presidente da Camara dos Mortos) - Sprite Specification

## Overview
- **Tipo de Personagem:** Modelo Boss Final (Potencial 4/5)
- **Sprite Dimensions:** 64x64px (personagem), 32x32px (projeteis/efeitos)
- **Sprite Sheet Layout:** Horizontal strip por animacao
- **Direcoes:** 4 (frente, costas, esquerda, direita)
- **Formato:** PNG com alpha transparency
- **Anchor Point:** Bottom-center (32, 60) -- pes do personagem
- **Proporcoes:** Cabeca 1.5x, torso 2x, pernas 1.5x (~5 cabecas total, atarracado)

---

## Conceito Visual Core

Hugo Motta e o OPOSTO visual dos outros bosses. Enquanto Maduro e Xandao sao grotescos de forma OBVIA, Hugo Motta e grotesco de forma SUTIL. Ele parece "normal" a primeira vista -- terno cinza, sorriso de politico. Mas olhando mais de perto: os dedos sao DEMAIS, as orelhas sao GRANDES demais, os olhos NUNCA piscam. O horror vem da normalidade perturbadora, nao do exagero visivel. E o "uncanny valley" do politico brasileiro.

---

## Paleta de Cores

| Elemento                    | Hex Code  | Uso                                             |
|-----------------------------|-----------|--------------------------------------------------|
| Pele Base                   | `#D4A574` | Tom de pele principal -- saudavel demais         |
| Pele Sombra                 | `#B08050` | Sombras sutis                                    |
| Pele Highlight              | `#E8C090` | Brilho de pele bem cuidada (botox?)              |
| Terno Cinza                 | `#5A5A5A` | Cor principal do terno -- NEUTRA, invisivel       |
| Terno Cinza Escuro          | `#3A3A3A` | Sombras do terno                                 |
| Terno Cinza Claro           | `#7A7A7A` | Highlights do terno                              |
| Camisa Branca               | `#F0F0E8` | Camisa social por baixo                          |
| Gravata Vermelha Discreta   | `#8B3333` | Gravata -- vermelha mas nao chamativa            |
| Gravata Sombra              | `#5C1A1A` | Sombra da gravata                                |
| Cabelo Preto                | `#1A1A1A` | Cabelo penteado impecavel                        |
| Cabelo Highlight            | `#333333` | Reflexo do gel                                   |
| Sapato Preto                | `#1A1A1A` | Sapatos lustrados                                |
| Sapato Brilho               | `#444444` | Reflexo nos sapatos                              |
| Sorriso Branco              | `#FFFFFF` | Dentes -- brancos DEMAIS (clareamento excessivo) |
| Sorriso Brilho              | `#F0F0FF` | Brilho nos dentes (1px de "ping")                |
| Celular Preto               | `#0D0D0D` | Celular sempre presente                          |
| Celular Tela                | `#3399FF` | Tela do celular (azul)                           |
| Celular "VORCARO"           | `#FF3333` | Nome "VORCARO" na tela (pisca)                   |
| Orelha Pele Extra           | `#C49060` | Orelhas grandes -- tom levemente diferente       |
| Dedos Extra                 | `#D4A574` | Dedos a mais -- mesmo tom de pele                |
| Olho Branco                 | `#FFFFFF` | Esclerótica -- MUITO branca (nunca pisca)        |
| Iris Preto                  | `#1A1A1A` | Iris escura -- pupila indistinguivel             |
| Outline                     | `#1A1A1A` | Linhas grossas 2-4px irregulares                 |
| Cross-Hatch Shadow          | `#0D0D0D` | Sombras em cross-hatching                        |
| Aura Invisivel              | `#5A5A5A` | Halo sutil 15% opacidade (poder nos bastidores)  |
| Documento Branco            | `#F0F0E8` | Papeis e documentos (skill)                      |
| Documento Selo              | `#8B3333` | Selo vermelho nos documentos                     |
| Conexao Line                | `#FF3333` | Linha de conexao Vorcaro (skill)                 |
| Escudo Parlamentar          | `#FFD700` | Escudo dourado (imunidade)                       |

---

## Frame-by-Frame: IDLE (4 frames, loop)

### Frame 0: idle_01 -- O Sorriso Permanente
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Hugo Motta de frente, postura PERFEITA. Terno cinza impecavel -- sem uma ruga, sem uma mancha. Camisa branca alinhada. Gravata vermelha discreta centralizada. Cabelo preto penteado com gel (nenhum fio fora do lugar). SORRISO FIXO: boca aberta mostrando dentes brancos DEMAIS -- o sorriso que nunca sai. E o sorriso de politico que esconde TUDO. Olhos ABERTOS -- pupilas escuras, esclerótica MUITO branca. Os olhos NAO PISCAM (frame 0 a 3, zero piscadas -- isso e intencional e perturbador). Mao direita segura CELULAR (8x12px, tela azul). Mao esquerda no bolso -- mas a mao tem 6 DEDOS (o sexto e sutil, facil de perder, mas esta la). Orelhas GRANDES -- 2x o tamanho normal, projetando para fora do cabelo. Outline grosso 2-4px, cross-hatching nas sombras. Textura de papel.
- **Notas de Estilo:** A primeira impressao e "normal". O grotesco e SUTIL. O jogador precisa OLHAR de perto para ver os dedos extras, orelhas grandes, olhos que nao piscam. O horror esta no que parece estar certo mas NAO esta.

### Frame 1: idle_02 -- Celular Pisca
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Identico ao Frame 0, exceto: a tela do celular muda. Aparece brevemente o nome "VORCARO" em vermelho na tela. Hugo nao olha diretamente para o celular -- olha para FRENTE com o sorriso intacto, mas os olhos DESVIAM 1px na direcao do celular. Micro-tell de quem sabe que nao deveria estar vendo aquela mensagem mas ve mesmo assim. Sorriso nao muda. NADA mais muda. A perturbacao e na AUSENCIA de reacao.
- **Notas de Estilo:** O contraste entre a mensagem "VORCARO" (bomba politica) e a ZERO reacao facial e a piada. Ele sabe de TUDO e nao demonstra NADA.

### Frame 2: idle_03 -- Orelha Gira
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Identico ao Frame 0, exceto: uma orelha (a direita) GIRA levemente na direcao de um som imaginario -- como antena parabolica. Rotação de 10-15 graus. A orelha se move INDEPENDENTE da cabeca (como o bigode do Maduro, mas com orelhas). Hugo "ouve tudo" -- as orelhas grandes sao FUNCIONAIS. Sorriso inalterado. Olhos inalterados. Celular na mesma posicao.
- **Notas de Estilo:** Referencia a que Hugo Motta "ouve tudo nos bastidores". A orelha-antena e sutil -- o jogador talvez so perceba depois de varios loops.

### Frame 3: idle_04 -- Dedos Mexem
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Identico ao Frame 0, exceto: a mao no bolso (esquerda) se move -- os 6 DEDOS tambaleiam levemente, como se estivessem digitando algo no bolso ou contando dinheiro invisivelmente. O sexto dedo (mindinho extra) se destaca mais neste frame -- move-se INDEPENDENTE dos outros. Sorriso intacto. Olhos fixos. Celular na outra mao.
- **Notas de Estilo:** Os dedos extras representam "apertar mais maos" -- ter mais conexoes que o humanamente possivel. O movimento no bolso sugere negociacao invisivel constante.

---

## Frame-by-Frame: WALK (6 frames, loop)

### Frame 0: walk_01 -- Passo Confiante
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Passo direito a frente. Marcha de CORREDOR DO CONGRESSO -- nao militar, nao casual. E o andar de quem esta SEMPRE indo negociar algo. Postura ereta, ombros relaxados (confianca real, nao encenada). Terno flui sem amassar. Celular na mao direita, levemente erguido (pronto para atender). Mao esquerda balanca naturalmente -- 6 dedos visiveis no frame. Orelhas grandes captam os dois lados. Sorriso INTACTO mesmo andando. Olhos ABERTOS fixos na frente.
- **Notas de Estilo:** O walk deve comunicar PODER DISCRETO. Nao e intimidador como Xandao ou ridiculo como Maduro. E o andar de alguem que sabe que CONTROLA A PAUTA.

### Frame 1: walk_02 -- Transicao
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Transicao entre passos. Corpo levemente mais alto (bounce minimo -- 1px). Hugo anda com EFICIENCIA -- sem desperdicar energia. Celular levemente mais alto (checando notificacao). Sorriso intacto.

### Frame 2: walk_03 -- Passo Esquerdo
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Passo esquerdo. Mirror sutil do Frame 0. A mao dos 6 dedos agora esta na frente -- os dedos extras sao mais visiveis neste angulo. Uma orelha gira levemente (capta algo ao passar).

### Frame 3: walk_04 -- Transicao + Celular
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Transicao. Hugo olha brevemente para o celular (olhos descem 2px). Na tela: flash de "VORCARO" por 1 frame. Olhos voltam para frente instantaneamente. Sorriso nunca mudou.

### Frame 4: walk_05 -- Cumprimento Automatico
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** A cada 2 ciclos de walk, Hugo faz um CUMPRIMENTO automatico para alguem invisivel. Aceno com a mao dos 6 dedos (todos os dedos se abrem -- seis dedos claramente visiveis). O cumprimento e REFLEXO -- ele cumprimenta automaticamente, como se apertasse maos no ar. Sorriso aumenta 1px (mais dentes visiveis).
- **Notas de Estilo:** Ele cumprimenta AUTOMATICAMENTE. Nao importa se tem alguem ou nao. O gesto de cumprimento e reflexo de politico -- hardcoded.

### Frame 5: walk_06 -- Volta ao Normal
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Mao volta ao lado. Sorriso volta ao tamanho padrao. Tudo volta ao "normal". O cumprimento ja acabou. Como se nada tivesse acontecido. Segue andando.

---

## Frame-by-Frame: ATTACK -- Articulacao Suprema (8 frames)

### Frame 0: atk_01 -- Avaliação
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Hugo PARA. Olhos escaneiam a area (pupilas se movem pela primeira vez -- esquerda para direita, calculando). Sorriso muda para sorriso MENOR (nao some, diminui -- concentracao). Celular guarda no bolso interno do terno (gesto rapido e discreto). Maos se juntam na frente (posicao de negociador). Todos os 6 dedos de cada mao visiveis entrelaçados (12 dedos no total -- perturbador).
- **Notas de Estilo:** O ataque do Hugo NAO e explosivo. E CALCULADO. A anticipacao e FRIA.

### Frame 1: atk_02 -- O Gesto
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Hugo faz um gesto sutil -- levanta UMA mao (a dos 6 dedos) com palma virada para frente. E quase um "pare" ou um "eu resolvo". O gesto e MINIMO mas carrega PODER. Linhas de influencia INVISIVEIS emanam da mao (representadas por distorcao sutil do ar ao redor -- heat shimmer effect, 1-2px de ondulacao). Sorriso volta ao MAXIMO.

### Frame 2: atk_03 -- Ondas de Influencia
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** As ondas de influencia se expandem. NAO sao ondas sonoras coloridas como as do Maduro -- sao DISTORCOES NO AR, quase invisiveis. Representadas por linhas de grid deformadas (como gravitational lensing). Dentro das ondas: micro-icones de documentos, selos, notas de pauta. Hugo esta PARADO, mao ainda erguida, sorriso fixo.
- **Notas de Estilo:** O poder do Hugo e INVISIVEL. O efeito visual deve ser SUTIL -- diferente do caos do Maduro. E poder que voce so percebe quando ja foi afetado.

### Frame 3: atk_04 -- NPCs Mudam
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** As ondas atingem os inimigos. Efeito visual nos inimigos: olhos brilham brevemente (#FFD700, 1 frame). Inimigos mudam de comportamento (gameplay: param de atacar Hugo, atacam o player). Hugo abaixa a mao. Tira celular do bolso. Checa notificacao calmamente. Sorriso satisfeito.
- **Notas de Estilo:** O ataque ACONTECEU sem que Hugo fizesse nada dramatico. Ele apenas "articulou".

### Frame 4: atk_05 -- Controle
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** Hugo observa o caos que causou com as maos nos bolsos. Postura relaxada. Celular checando. NPCs ao redor agindo conforme SUA vontade (representado por linhas finas #5A5A5A de Hugo para cada NPC afetado -- strings de marionete quase invisiveis). Ele e o titereiro. Sorriso amplo.

### Frame 5: atk_06 -- Linhas Enfraquecem
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Linhas de marionete ficam mais finas e transparentes. NPCs comecam a voltar ao normal. Hugo percebe -- olhos se estreitam 1px (micro-calculo). Mao se move para o celular (vai precisar re-articular).

### Frame 6: atk_07 -- Perda de Controle
- **Posicao no sheet:** 384,0 a 447,63
- **Descricao:** Linhas de marionete se rompem uma por uma (snap visual -- pequeno flash em cada ruptura). NPCs voltam ao comportamento normal. Hugo guarda celular. Recompoe postura. Sorriso diminui 1px (micro-irritacao).

### Frame 7: atk_08 -- Reset
- **Posicao no sheet:** 448,0 a 511,63
- **Descricao:** Tudo volta ao "normal". Hugo de pe, terno perfeito, sorriso padrao. Como se NADA tivesse acontecido. Nenhuma evidencia do ataque. Apenas o resultado: alguns inimigos ainda confusos. Cooldown inicia.
- **Notas de Estilo:** A marca do Hugo e NAO DEIXAR RASTRO. O ataque comeca e termina com ele parecendo inofensivo.

---

## Frame-by-Frame: SKILL 1 -- Pauta Secreta (6 frames)

### Frame 0: pauta_01 -- Documento
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Hugo tira do bolso interno do terno um DOCUMENTO DOBRADO (8x12px). O documento e SIGILOSO -- selo vermelho, "CONFIDENCIAL" em micro-texto. Gesto sutil -- quase escondendo o documento da camera/jogador. Sorriso diminui (seriedade rara). Olhos fixos para frente (vigilancia).

### Frame 1: pauta_02 -- Leitura
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Desdobra o documento parcialmente (nao todo -- nunca revela tudo). Olhos descem para ler (primeira vez que olha para BAIXO). Orelhas viram para fora (checando se alguem esta ouvindo). Os 6 dedos seguram o documento -- dedos extras ajudam a esconder o conteudo dos outros.

### Frame 2: pauta_03 -- Ativa Pauta
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Dobra o documento de volta (rapido, eficiente). Guarda no terno. Faz um gesto de "ok" sutil com a mao (todos os 6 dedos formando o gesto -- perturbador). Efeito visual: NADA VISIVEL MUDA NO MAPA. Mas o gameplay muda silenciosamente. Sorriso volta ao maximo.
- **Notas de Estilo:** A Pauta Secreta e INVISIVEL. O efeito nao tem manifestacao visual obvia. O jogador so percebe que algo mudou pelos EFEITOS.

### Frame 3: pauta_04 -- Efeito Invisivel
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Hugo volta a posicao idle. Tudo PARECE normal. Mas no canto inferior do frame: um mini-icone de engrenagem girando (8x8px, 30% opacidade) indica que as regras estao mudando nos bastidores. Hugo checa celular casualmente.

### Frame 4: pauta_05 -- Regras Mudando
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** O mini-icone de engrenagem gira mais rapido. Hugo calmamente caminha (pode ativar walk durante este frame). Efeitos gameplay em andamento: spawn rates mudam, drops alteram, dificuldade oscila -- tudo SILENCIOSAMENTE.

### Frame 5: pauta_06 -- Fim Silencioso
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Mini-icone de engrenagem desaparece. Regras finalizaram mudanca. Hugo sorri. Celular recebe notificacao (tela pisca). O dano ja esta feito e NINGUEM sabe quem fez.

---

## Frame-by-Frame: SKILL 2 -- Conexao com o Master (6 frames)

### Frame 0: conexao_01 -- Celular Toca
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Celular de Hugo VIBRA (linhas de vibracao 1-2px). Tela mostra "VORCARO" em vermelho piscante. Hugo olha para o celular pela PRIMEIRA VEZ diretamente (olhos descem, sorriso se mantem). Orelhas se eriçam (ALERTA -- informacao importante chegando).

### Frame 1: conexao_02 -- Atende
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Leva celular a orelha (orelha grande engole metade do celular). Sorriso vira sorriso MENOR (concentracao). Vira levemente de lado (posicao de quem fala em segredo -- ombro virado para "esconder" a conversa). A mao livre (6 dedos) faz gesto de "espera" para ninguem.

### Frame 2: conexao_03 -- Link Estabelecido
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** LINHA VERMELHA (#FF3333) aparece saindo do celular e se estendendo para FORA DO FRAME -- em direcao ao Vorcaro (se estiver no mapa) ou em direcao abstrata. A linha e fina (1px) mas PULSA (alterna entre 1px e 2px). Ao longo da linha: micro-icones de cifrao ($) e documentos fluindo. Hugo assente com a cabeca (micro-nod).

### Frame 3: conexao_04 -- Defesa Ativa
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** A linha vermelha fica mais forte (2px constante, mais brilhante). Efeito de ESCUDO sutil ao redor de Hugo: halo dourado (#FFD700) quase invisivel (15-20% opacidade). +30% defesa ativo. Hugo desliga celular, guarda. Sorriso satisfeito -- negocio fechado. Linha se mantem mesmo sem o celular (a conexao e maior que a ligacao).

### Frame 4: conexao_05 -- Rede Ativa
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** Multiplas linhas finas se estendem de Hugo para varios pontos do mapa (nao so Vorcaro). Uma REDE de conexoes -- Hugo no centro como aranha. Cada linha e vermelha fina com micro-cifrao. O halo de defesa pulsa. Hugo parado, maos nos bolsos, SORRISO MAXIMO.
- **Notas de Estilo:** Este frame mostra Hugo como o que ele e: o CENTRO da teia de poder. Nao o mais forte, mas o MAIS CONECTADO.

### Frame 5: conexao_06 -- Rede Desvanece
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** Linhas ficam transparentes e somem uma a uma. Halo dourado diminui. Hugo tira celular do bolso novamente (ja planejando a proxima conexao). Tela mostra lista de contatos com MUITOS nomes (micro-texto ilegivel). Sorriso padrao restaurado.

---

## Frame-by-Frame: SKILL 3 -- Imunidade Parlamentar (4 frames)

### Frame 0: imunidade_01 -- Invocacao
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Hugo ergue a mao (6 dedos TODOS estendidos, bem abertos). Gesto autoritario mas CALMO. Acima da cabeca: ESCUDO DOURADO comeca a se formar. O escudo tem formato de BRASAO DA CAMARA estilizado (grotesco -- aguia deformada, louros murchos). Expressao: sorriso vira sorriso SERIO (raro -- ele SIM tem poder aqui).

### Frame 1: imunidade_02 -- Escudo Completo
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Escudo dourado COMPLETO ao redor de Hugo. Circulo de luz dourada (#FFD700, 40% opacidade). Dentro do escudo: Hugo intocavel. Projeteis que atingem o escudo RICOCHETEIAM com texto "IMUNE" micro (5px lettering). Mao abaixa. Postura relaxada -- esta protegido. Sorriso volta ao padrao (a normalidade do privilegio).

### Frame 2: imunidade_03 -- Escudo Ativo
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Escudo pulsando suavemente. Hugo ANDA normalmente dentro do escudo (overlay de escudo segue o sprite). Projeteis continuam ricocheteando. "IMUNE" aparece a cada ricochet. Hugo checa celular DENTRO do escudo (a calma de quem sabe que nao pode ser tocado).

### Frame 3: imunidade_04 -- Escudo Desvanece
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** Escudo dourado comeca a rachar (linhas de fratura no dourado). Brilho diminui. Ultimo "IMUNE" aparece com ponto de interrogacao ("IMUNE?"). Hugo percebe -- orelhas abaixam (micro-tell de preocupacao). Sorriso diminui 1px. Guarda celular rapidamente. Escudo some. Vulneravel novamente.

---

## Frame-by-Frame: HIT / DANO (3 frames)

### Frame 0: hit_01 -- Impacto Contido
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Flash branco sutil (30% opacidade -- MENOS que outros personagens). Corpo mal se move (1-2px de deslocamento). MAS: o sorriso CONGELA por 1 frame (nao some -- congela. Os musculos faciais travam). Celular cai da mao (voa 4px para o lado). OS OLHOS FINALMENTE PISCAM por 1 frame (o unico momento em que piscam -- o susto quebra o controle). Terno amassa levemente num ponto.
- **Notas de Estilo:** O hit do Hugo e CONTIDO. Ele nao grita, nao voa, nao faz drama. Mas os micro-tells revelam: sorriso congelado, olho piscando, celular caindo. Para quem presta atencao, o dano e DEVASTADOR internamente.

### Frame 1: hit_02 -- Recomposicao Instantanea
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Hugo ja esta se recompondo. Mao pega celular no ar (reflexo impressionante -- os 6 dedos agarram como aranha). Sorriso VOLTA (forcado -- 1px mais largo que o normal, tentando compensar). Terno se alinha. Olhos voltam a NAO PISCAR. Postura ereta.
- **Notas de Estilo:** A recomposicao e ASSUSTADORAMENTE rapida. Hugo nao quer que ninguem veja que foi atingido.

### Frame 2: hit_03 -- "Nada Aconteceu"
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** Volta EXATA ao idle padrao. Celular na mao, sorriso padrao, terno impecavel. A unica evidencia: uma MICRO-RUGA no terno (1px de sombra extra na lapela) que desaparece em 2 segundos. Hugo quer que voce acredite que nada aconteceu. E quase funciona.

---

## Frame-by-Frame: DEATH (8 frames, NAO loop)

### Frame 0: death_01 -- A Fachada Racha
- **Posicao no sheet:** 0,0 a 63,63
- **Descricao:** Golpe fatal. PELA PRIMEIRA VEZ: o sorriso SOME. Boca se abre em O de choque genuino. AMBOS os olhos piscam (incontrolavel agora). Celular voa. Terno comeca a RACHAR -- literalmente, como porcelana. Linhas de fratura aparecem no terno, na pele, no sorriso. A fachada de "tudo sob controle" QUEBRA.
- **Notas de Estilo:** Este e O MOMENTO. O jogador nunca viu Hugo sem sorriso. A ausencia do sorriso e MAIS perturbador que a presença.

### Frame 1: death_02 -- Documentos Escapam
- **Posicao no sheet:** 64,0 a 127,63
- **Descricao:** Do TERNO rachado, DOCUMENTOS comecam a VAZAR. Papeis, contratos, memorandos, notas de pauta -- CENTENAS de micro-documentos voam para fora do terno como se ele fosse feito de papel. Cada documento tem selo vermelho ("SIGILOSO"). Hugo tenta recolher mas tem documentos demais. Os 6 dedos de cada mao tentam agarrar tudo -- os dedos EXTRAS finalmente fazem sentido funcional (mais dedos = mais documentos = mais corrupcao).

### Frame 2: death_03 -- Celular Expoe
- **Posicao no sheet:** 128,0 a 191,63
- **Descricao:** O celular caido no chao, TELA PARA CIMA. Na tela, MAXIMIZADA: lista de contatos -- nomes de TODOS os outros personagens do jogo (micro-texto). Hugo olha para o celular com HORROR (primeira expressao de medo genuino). Tenta pisar no celular para quebrar a tela. Nao consegue -- pernas fraquejam.

### Frame 3: death_04 -- Terno Esvazia
- **Posicao no sheet:** 192,0 a 255,63
- **Descricao:** O terno comeca a ESVAZIAR. Como se Hugo fosse feito de documentos e agora eles estao saindo. O terno fica frouxo. Dentro: mais papeis, contratos, notas promissorias, cifraoes. Hugo ENCOLHE conforme os documentos saem -- a substancia dele era PAPEL.

### Frame 4: death_05 -- A Rede Aparece
- **Posicao no sheet:** 256,0 a 319,63
- **Descricao:** As linhas de conexao que eram INVISIVEIS durante o jogo agora se MATERIALIZAM ao redor do corpo caido. Linhas vermelhas finas se estendem para todos os lados, conectando Hugo a pontos invisiveis. A TEIA inteira e revelada. Hugo no centro, encolhido, cercado pela propria rede de corrupcao.

### Frame 5: death_06 -- Maos Agarram
- **Posicao no sheet:** 320,0 a 383,63
- **Descricao:** As linhas da rede comecam a PUXAR Hugo. Como marionete sendo recolhida. Corpo se deforma levemente em direcoes opostas (puxado por todas as conexoes). Orelhas esticam (puxadas pela informacao que absorveram). Dedos extras se agarram no chao tentando resistir. Expressao de desespero REAL -- sem sorriso, sem fachada.

### Frame 6: death_07 -- Dissolucao Burocratica
- **Posicao no sheet:** 384,0 a 447,63
- **Descricao:** Hugo se DISSOLVE em DOCUMENTOS. O corpo se transforma em papeis voando. Cada pixel do sprite se converte num micro-documento. E como se ele nunca tivesse sido uma pessoa -- sempre foi uma PILHA DE DOCUMENTOS em formato humano. O terno era a pasta, o sorriso era o selo, as maos eram as assinaturas.

### Frame 7: death_08 -- Resta o Celular
- **Posicao no sheet:** 448,0 a 511,63
- **Descricao:** Frame final. Hugo SUMIU. Nao ha corpo. Apenas uma PILHA DE DOCUMENTOS no chao e, no topo, o CELULAR. Tela ainda ligada. Tela mostra: mensagem de "VORCARO" nao lida. A tela pisca. Os documentos se acomodam. Silencio visual. Uma ultima notificacao aparece na tela: "Nova conexao disponivel". Fade gradual para transparencia.
- **Notas de Estilo:** A morte do Hugo e BUROCRATICA. Nao e explosiva. E a dissolucao em papeis. O celular e o unico "sobrevivente" -- as conexoes persistem mesmo sem ele.

---

## Sprite Sheets Summary

| Sheet              | Frames | Tamanho Sheet       | FPS  | Loop  |
|--------------------|--------|---------------------|------|-------|
| idle               | 4      | 256x64px            | 8    | Sim   |
| walk               | 6      | 384x64px            | 10   | Sim   |
| attack_articulacao | 8      | 512x64px            | 8    | Nao   |
| skill_pauta        | 6      | 384x64px            | 8    | Nao   |
| skill_conexao      | 6      | 384x64px            | 8    | Nao   |
| skill_imunidade    | 4      | 256x64px            | 8    | Nao   |
| hit                | 3      | 192x64px            | 12   | Nao   |
| death              | 8      | 512x64px            | 6    | Nao   |

---

## Projeteis e Efeitos (32x32px)

### Onda de Influencia (Articulacao Suprema)
- **Frames:** 4
- **Descricao:** Distorcao de ar SUTIL. Nao e uma onda colorida -- e um SHIMMER, como calor no asfalto. Representado por linhas de grid deformadas. Dentro: micro-icones de documentos e selos. Quase INVISIVEL -- o poder e discreto.

### Linha de Conexao (Conexao Master)
- **Frames:** 3
- **Descricao:** Linha vermelha fina (1-2px) pulsando. Ao longo: micro-cifraoes ($) fluindo na direcao de Hugo. A linha nao e reta -- faz curvas sutis (evitando deteccao).

### Escudo Parlamentar (Imunidade)
- **Frames:** 3
- **Descricao:** Halo dourado circular com brasao estilizado da Camara. Texto "IMUNE" aparece quando projetil atinge. Textura de documento oficial (selos, carimbos, linhas decorativas).

### Documento Sigiloso (Pauta Secreta)
- **Frames:** 2
- **Descricao:** Papel branco com selo vermelho "CONFIDENCIAL". Gira lentamente. Aparece e desaparece (nao fica visivel por muito tempo -- e SECRETO).

---

## Phaser 3 Atlas Keys

```
key: 'hugo_idle'            frameWidth: 64  frameHeight: 64
key: 'hugo_walk'            frameWidth: 64  frameHeight: 64
key: 'hugo_attack'          frameWidth: 64  frameHeight: 64
key: 'hugo_pauta'           frameWidth: 64  frameHeight: 64
key: 'hugo_conexao'         frameWidth: 64  frameHeight: 64
key: 'hugo_imunidade'       frameWidth: 64  frameHeight: 64
key: 'hugo_hit'             frameWidth: 64  frameHeight: 64
key: 'hugo_death'           frameWidth: 64  frameHeight: 64
key: 'hugo_proj_influencia' frameWidth: 32  frameHeight: 32
key: 'hugo_proj_conexao'    frameWidth: 32  frameHeight: 32
key: 'hugo_proj_escudo'     frameWidth: 32  frameHeight: 32
key: 'hugo_proj_documento'  frameWidth: 32  frameHeight: 32
```

---

## Notas para o Artista

1. **O SORRISO e o personagem.** Ele NUNCA sai, exceto na death. Se o sorriso sumiu e o personagem nao esta morrendo, o sprite esta errado.
2. **Os OLHOS NUNCA PISCAM.** Exceto no hit (1 frame) e na death. A vigilia constante e o horror sutil.
3. **Os DEDOS EXTRAS sao SUTIS.** O jogador deve precisar olhar de perto para notar o sexto dedo. Nao e obvio -- e perturbador.
4. **As ORELHAS se movem como antenas.** Giram independente da cabeca, captando informacao.
5. **O TERNO e IMPECAVEL.** Nunca amassa, nunca suja (exceto hit/death). A perfeicao e o disfarce.
6. **O CELULAR esta SEMPRE presente.** Em todo frame exceto walk e idle seletivos, o celular esta na mao ou no bolso.
7. **Cores NEUTRAS.** Hugo e o unico personagem cujas cores principais sao CINZA. Ele nao quer chamar atencao.
8. **O grotesco e SUTIL, nao OBVIO.** Diferente de todos os outros personagens. O desconforto vem da normalidade perturbadora.
9. **Cross-hatching nas sombras** mas MENOS que outros personagens. As sombras dele sao mais limpas (ele esconde a sujeira).
10. **Inspiracao: o politico que voce NAO percebe que e perigoso.** Enquanto voce olha pro Xandao e pro Maduro, o Hugo ja articulou nos bastidores.
