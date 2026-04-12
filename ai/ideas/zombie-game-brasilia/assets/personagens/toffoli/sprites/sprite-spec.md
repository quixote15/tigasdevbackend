# TOFFOLI (Dias Toffoli) - Especificacao de Sprites

## Boss Secundario STF - "O Rato do STF / O Espiao" - "Zumbis de Brasilia"

---

## Especificacoes Tecnicas Gerais

| Propriedade          | Valor                                    |
|---------------------|------------------------------------------|
| Tamanho sprite      | 64x64 pixels                             |
| Tamanho projeteis   | 32x32 pixels                             |
| Formato             | PNG com transparencia                    |
| Layout spritesheet  | Horizontal (frames lado a lado)          |
| Framerate alvo      | 8-12 fps (twitchy/jerky, estilo Andre Guedes) |
| Motor               | Phaser 3                                 |
| Estilo artistico    | Grotesco, underground comix, Andre Guedes |

---

## IDLE - "Cara de Paisagem" (4 frames)

**Arquivo**: `toffoli_idle.png` (256x64 px)

### Frame 1 — Posicao Base
- **Corpo**: Toffoli de frente, levemente virado 3/4. Toga preta desbotada cobrindo o corpo inteiro. Postura ereta mas RELAXADA demais — como se nao tivesse nada acontecendo.
- **Rosto**: Expressao ABSOLUTAMENTE VAZIA. Boca reta sem curva nenhuma. Olhos abertos mas sem brilho, sem interesse, sem alma. A cara mais sem graca do elenco inteiro — PROPOSITAL.
- **Orelhas**: Enormes, desproporcionais (2x o tamanho normal). Posicao neutra, apontando levemente pra cima. Formato de antena parabolica com pele.
- **Olhos**: Olho esquerdo olhando reto pra frente (mantendo cara de paisagem). Olho direito TAMBEM olhando pra frente neste frame.
- **Maos**: Mao direita segurando gravador discretamente, quase escondido na manga da toga. Mao esquerda pendurada ao lado.
- **Detalhes da toga**: 3-4 microfones ESCONDIDOS mas VISIVEIS pro jogador: um na gola (camuflado como botao), um na manga (ponta aparecendo), um no peito (disfarçado de broche). Fio de fone de ouvido saindo da orelha direita, quase invisivel.
- **Luz REC**: Pequeno ponto vermelho no gravador — SEMPRE gravando.

### Frame 2 — Orelha Esquerda Captando
- **Corpo**: Identico ao frame 1.
- **Rosto**: MESMA expressao vazia. Nenhuma mudanca.
- **Orelhas**: Orelha ESQUERDA se inclina 15 graus pro lado esquerdo, como captando um som. Orelha direita permanece neutra.
- **Olhos**: Olho esquerdo continua reto. Olho direito MOVE levemente pro lado esquerdo (acompanhando a orelha, espiando).
- **Maos**: Identicas. Gravador pisca luz REC mais forte.
- **Detalhe**: Ondas sonoras sutis (2-3 linhas curvas verdes semi-transparentes) chegando na orelha esquerda.

### Frame 3 — Orelha Direita Captando
- **Corpo**: Identico.
- **Rosto**: MESMA expressao vazia. Zero emocao.
- **Orelhas**: Orelha DIREITA se inclina 15 graus pro lado direito. Orelha esquerda volta a posicao neutra.
- **Olhos**: Olho esquerdo continua reto (SEMPRE reto, ancorando a cara de paisagem). Olho direito move pro lado direito.
- **Maos**: Gravador na mao direita se levanta 2-3 pixels, como se ajustando a direcao de gravacao.
- **Detalhe**: Ondas sonoras chegando na orelha direita agora.

### Frame 4 — Microfone Brilha
- **Corpo**: Identico.
- **Rosto**: MESMA expressao. Absolutamente nada mudou na cara.
- **Orelhas**: Ambas em posicao neutra, mas levemente MAIORES que no frame 1 (como se tivessem "inflado" com informacao).
- **Olhos**: Ambos olhando pra frente. Mas o olho direito tem um MICRO brilho — quase imperceptivel — de satisfacao. Ele gravou algo bom.
- **Maos**: Gravador brilha forte (luz REC pulsando).
- **Detalhe**: Um dos microfones da toga (o do peito) pisca brevemente, indicando que captou algo.

---

## WALK - "Espiao Discreto" (6 frames)

**Arquivo**: `toffoli_walk.png` (384x64 px)

### Frame 1 — Passo Esquerdo Inicio
- **Corpo**: Perna esquerda avancando, perna direita atras. Toga balancando levemente. O andar e DISCRETO, quase furtivo — nao e marcha, e deslizar.
- **Rosto**: Cara de paisagem INTACTA. Boca reta. Nenhuma expressao.
- **Orelhas**: Apontando pra frente, como "cheirando" o caminho. Enormes, desproporcionais.
- **Olhos**: Esquerdo olhando pra frente. Direito espiando pro lado ESQUERDO (vigiando o flanco).
- **Maos**: Gravador na mao direita, proximo ao corpo, escondido na toga. Mao esquerda levemente levantada.

### Frame 2 — Passo Esquerdo Meio
- **Corpo**: Peso transferido pro pe esquerdo. Leve inclinacao pra frente. Toga abrindo levemente, revelando MAIS um microfone escondido na parte interna.
- **Rosto**: Mesma expressao vazia.
- **Orelhas**: Orelha esquerda gira pro lado esquerdo (escaneando). Orelha direita permanece frontal.
- **Olhos**: Esquerdo reto. Direito voltando pro centro.
- **Detalhe**: Fone de ouvido brilha verde brevemente — recebendo transmissao.

### Frame 3 — Passo Direito Inicio
- **Corpo**: Perna direita avancando agora. Toga balanca pro outro lado. Andar continua furtivo.
- **Rosto**: NADA. Paisagem total.
- **Orelhas**: Ambas apontando pra frente.
- **Olhos**: Esquerdo reto. Direito espiando pro lado DIREITO agora.
- **Maos**: Gravador sobe 2 pixels — como se estivesse ajustando volume.

### Frame 4 — Passo Direito Meio
- **Corpo**: Peso no pe direito. Toga fechando.
- **Rosto**: Vazio.
- **Orelhas**: Orelha direita gira pro lado direito (escaneando area). Esquerda frontal.
- **Olhos**: Esquerdo reto. Direito fixo no lado direito.
- **Detalhe**: Ondas sonoras sutis sendo captadas pela orelha direita.

### Frame 5 — Meio Passo (Transicao)
- **Corpo**: Ambos os pes quase juntos, corpo levemente agachado — como se estivesse se esgueirando.
- **Rosto**: Mesma cara de nada.
- **Orelhas**: AMBAS girando em direcoes opostas simultaneamente (esquerda pra esquerda, direita pra direita) — escaneamento de 180 graus.
- **Olhos**: AMBOS olhando em direcoes diferentes — esquerdo espia esquerda, direito espia direita. MAXIMO de "olhos independentes".
- **Maos**: Gravador proximo a boca, como se fosse sussurrar uma anotacao.

### Frame 6 — Retomada
- **Corpo**: Voltando a posicao ereta, pronto pro proximo ciclo. Toga se acomoda.
- **Rosto**: Paisagem.
- **Orelhas**: Voltam a posicao frontal neutra.
- **Olhos**: Ambos voltam ao centro. Um micro-piscar de satisfacao no olho direito.
- **Detalhe**: Gravador pulsa vermelho — gravou algo durante a caminhada.

---

## ATTACK - "Gravacao Comprometedora" (3 frames)

**Arquivo**: `toffoli_attack.png` (192x64 px)

### Frame 1 — Puxa Gravador
- **Corpo**: Toffoli para abruptamente. Corpo se vira levemente pro alvo. Toga abre no movimento, revelando 2-3 microfones extras.
- **Rosto**: PELA PRIMEIRA VEZ quase uma expressao — um MICRO sorriso no canto da boca. Quase imperceptivel. Os olhos brilham com malicia contida.
- **Orelhas**: Apontam na direcao do alvo, como antenas direcionais.
- **Maos**: Mao direita LEVANTA o gravador a altura do rosto. Gravador e desproporcional — maior do que deveria ser, estilo anos 80, com fita cassete visivel.
- **Detalhe**: Luz REC pulsando forte. Dedo sobre o botao PLAY.

### Frame 2 — Aperta Play
- **Corpo**: Firme, plantado. Toga se abre mais com uma rajada de ar do som.
- **Rosto**: Sorriso cresce UM pixel. Olhos arregalados com malicia. A "cara de paisagem" QUEBRA por este frame.
- **Orelhas**: Vibram com a forca do som saindo do gravador.
- **Maos**: Dedo APERTANDO o play. Gravador emite ondas sonoras visiveis.
- **Projetil**: Onda sonora sai do gravador — forma circular/conica expandindo, cor verde-matrix (#00FF88). Dentro da onda, silhuetas de palavras "comprometedoras" — "GRAVEI!", "FLAGRA", "DOSSIÊ". Tamanho do projetil: 32x32 px.
- **Detalhe**: Fita cassete girando visivelmente dentro do gravador.

### Frame 3 — Impacto Sonoro
- **Corpo**: Recuo leve do corpo (knockback do som). Toga balanca pra tras.
- **Rosto**: VOLTA a cara de paisagem INSTANTANEAMENTE. Como se nada tivesse acontecido. Boca reta. Olhos mortos.
- **Orelhas**: Voltam a posicao neutra.
- **Maos**: Gravador volta a posicao escondida na toga. Movimento fluido de guardar evidencia.
- **Detalhe**: Ultimas ondas sonoras se dissipando. O gravador ja esta de volta na posicao "discreto".

---

## DEATH - "Queda do Espiao" (4 frames)

**Arquivo**: `toffoli_death.png` (256x64 px)

### Frame 1 — Impacto Inicial
- **Corpo**: Toffoli toma o golpe final. Corpo inclina pra tras. Toga COMECA a abrir.
- **Rosto**: CHOQUE ABSOLUTO. Pela primeira e unica vez, expressao de SURPRESA GENUINA. Boca aberta, olhos arregalados — os dois olhando na mesma direcao pela primeira vez.
- **Orelhas**: Se levantam retas de choque, como orelhas de gato assustado.
- **Maos**: Gravador voa da mao. Mao tenta agarrar a toga que esta abrindo.
- **Detalhe**: Fone de ouvido cai, revelando o fio conectado ao gravador.

### Frame 2 — Microfones Revelados
- **Corpo**: Corpo caindo pra tras. Toga ABRE COMPLETAMENTE revelando a quantidade ABSURDA de microfones escondidos — 15, 20, 30 microfones de todos os tipos e tamanhos. Microfones de lapela, microfones direcionais, bugs eletronicos, mini-gravadores.
- **Rosto**: Expressao muda pra PÂNICO. Os olhos voltam a se mover independentemente — cada um pra um lado, tentando ver se alguem ta vendo.
- **Orelhas**: Comecam a MURCHAR. Perdendo o ar como baloes furados.
- **Maos**: Tentando segurar microfones que estao caindo, mas sao muitos.
- **Detalhe**: Microfones caindo em cascata. Cada microfone e detalhado — fios, antenas, luzinhas.

### Frame 3 — Dossies Explodem
- **Corpo**: Corpo quase no chao. Toga aberta como capa.
- **Rosto**: Volta a CARA DE PAISAGEM mesmo caindo — ultimo instinto.
- **Orelhas**: MURCHAS, penduradas como orelhas de cachorro triste. Metade do tamanho original.
- **Maos**: Soltas, sem forca.
- **Detalhe principal**: DOSSIES EXPLODEM de dentro da toga. 6-8 pastas amareladas voando pro ar. Cada pasta tem uma etiqueta com nome de outro boss: "XANDAO", "GILMAR", "BARROSO", "LULA", "BOLSO", "VORCARO". Papeis soltos voando em espiral. Carimbos "CONFIDENCIAL" visiveis em vermelho.
- **Mecanica visual**: Este e o momento do "drop" — informacoes que enfraquecem outros bosses.

### Frame 4 — Corpo no Chao
- **Corpo**: Deitado no chao de costas. Toga espalhada ao redor como poça preta. Silhueta formando contorno de corpo de cena de crime.
- **Rosto**: Olhos fechados. Boca com MICRO sorriso — mesmo morto, ele sabe que os dossies vao causar estrago.
- **Orelhas**: Completamente murchas, planas contra a cabeca. Voltaram ao tamanho normal (ironicamente, morto e quando parecem normais).
- **Maos**: Uma mao ainda segura UM unico microfone — o ultimo, que nunca largou.
- **Detalhe**: Microfones espalhados ao redor do corpo. Dossies flutuando no ar acima. Gravador quebrado ao lado, fita cassete saindo. Luz REC finalmente apaga (ultimo brilho vermelho se extinguindo).
- **Easter egg**: Se olhar de perto, a fita cassete desenrolada forma a frase "EU GRAVEI TUDO".

---

## HIT - "A Mascara Cai (Por 1 Frame)" (2 frames)

**Arquivo**: `toffoli_hit.png` (128x64 px)

### Frame 1 — Surpresa (O UNICO FRAME COM EXPRESSAO)
- **Corpo**: Knockback leve pra tras. Toga sacode.
- **Rosto**: EXPRESSAO MUDA. Este e O frame. Sobrancelhas sobem. Olhos arregalam. Boca forma um "O" pequeno. E a UNICA vez no jogo que Toffoli mostra emocao genuina (exceto death). A reacao deve ser MINIMA mas perceptivel — como se a mascara de paisagem tivesse rachado por um milissegundo.
- **Orelhas**: Ficam retas de susto (como antenas captando perigo).
- **Olhos**: AMBOS olham pro atacante — na mesma direcao, pela unica vez no idle/walk normal.
- **Detalhe**: Fone de ouvido cai da orelha direita, revelando que estava escutando algo. Fio visivel.
- **Importancia narrativa**: Este frame e a PIADA. O jogador espera a cara de paisagem e recebe uma microexpressao humana. Deve ser sutil o suficiente pra duvidar se viu.

### Frame 2 — Recuperacao Instantanea
- **Corpo**: Volta a posicao normal IMEDIATAMENTE. Sem transicao suave — corte seco, estilo Andre Guedes jerky.
- **Rosto**: Cara de paisagem RESTAURADA. Como se nada tivesse acontecido. Boca reta. Olhos mortos.
- **Orelhas**: Voltam a posicao normal de "antena captando".
- **Olhos**: Voltam a se mover independentemente. Direito ja espiando pro lado.
- **Detalhe**: Fone de ouvido de volta na orelha (como se tivesse se recolocado sozinho). Maos ajustam a toga discretamente, escondendo microfones que possam ter aparecido.
- **Importancia**: A velocidade da recuperacao e a piada — foi TAO rapido que o jogador se pergunta se viu a expressao ou imaginou.

---

## SPECIAL 1 - "Escuta Secreta" (4 frames)

**Arquivo**: `toffoli_special_escuta.png` (256x64 px)

**Mecanica**: Grava acoes inimigas e usa contra eles. Captura o proximo ataque que o inimigo faria.

### Frame 1 — Ativacao
- **Corpo**: Toffoli planta os pes no chao. Corpo rigido, concentrado. Toga fecha ao redor como casulo protetor.
- **Rosto**: Cara de paisagem, mas os olhos BRILHAM com um verde sutil (#00FF88).
- **Orelhas**: Comecam a CRESCER. Ja sao grandes, mas agora crescem MAIS — 3x o tamanho normal. Parecem antenas parabolicas de verdade.
- **Maos**: Gravador levantado, apertado contra o peito. Dedo no botao REC.
- **Detalhe**: Fone de ouvido brilha verde. Microfones na toga acendem todos de uma vez (luzes REC em cascata).

### Frame 2 — Expansao Auditiva
- **Corpo**: Identico, imóvel como estátua.
- **Rosto**: Mesmo.
- **Orelhas**: TAMANHO MAXIMO — 4x o tamanho normal. Ocupam quase metade do sprite. Detalhes internos visiveis (canais auditivos grotescamente detalhados, veias pulsando dentro da cartilagem).
- **Maos**: Gravador aperta REC. Fita cassete comeca a girar.
- **Detalhe**: Ondas sonoras VISIVEIS — circulos concentricos verdes (#00FF88) emanando de cada orelha, cobrindo area ampla. Cada onda tem "dados" dentro — numeros, letras, simbolos, como se captasse TUDO.

### Frame 3 — Captacao
- **Corpo**: Micro-tremor de concentracao.
- **Rosto**: Paisagem, mas SUOR aparece na testa — esforco de processar tanta informacao.
- **Orelhas**: Tremem, vibram com a quantidade de som captado. Vermelhas nas pontas pelo esforco.
- **Maos**: Gravador brilha VERMELHO INTENSO. Fita girando visivelmente rapido.
- **Detalhe**: Ondas sonoras se concentram, formam setas apontando pro gravador. Tudo sendo REGISTRADO. Balao de texto aparece com "REC" piscando.

### Frame 4 — Escuta Completa
- **Corpo**: Relaxa levemente.
- **Rosto**: Aquele MICRO sorriso de canto de boca. Satisfacao contida. "Gravei."
- **Orelhas**: Voltam ao tamanho "normal" (que ja e enorme). Pulsam com energia verde.
- **Maos**: Gravador volta pra posicao escondida, mas agora com aura verde ao redor — carregado com a gravacao.
- **Detalhe**: Aura verde ao redor do Toffoli inteiro por alguns frames apos o special — indicando que a escuta esta ativa e o proximo ataque inimigo sera capturado.

---

## SPECIAL 2 - "Dossie Secreto" (6 frames)

**Arquivo**: `toffoli_special_dossie.png` (384x64 px)

**Mecanica**: Ao ser ativado (ou ao morrer), dropa informacoes que enfraquecem permanentemente outros bosses.

### Frame 1 — Alcanca Dentro da Toga
- **Corpo**: Toffoli para. Uma mao vai pra dentro da toga, como se buscasse algo em bolso interno secreto.
- **Rosto**: Cara de paisagem. Nada.
- **Orelhas**: Neutras, relaxadas.
- **Olhos**: AMBOS olham pra baixo, pro interior da toga, pela unica vez.
- **Detalhe**: Toga se abre levemente, revelando CAMADAS de bolsos internos cheios de papeis.

### Frame 2 — Puxa a Pasta
- **Corpo**: Braço sai de dentro da toga segurando uma PASTA GIGANTE. A pasta e desproporcional — quase do tamanho do Toffoli. Amarelada, velha, com etiqueta "ULTRA-SECRETO" em vermelho.
- **Rosto**: MICRO levantada de sobrancelha. Quase imperceptivel.
- **Orelhas**: Levantam em antecipacao.
- **Maos**: Ambas segurando a pasta enorme. Gravador guardado.
- **Detalhe**: A pasta tem adesivos, carimbos, manchas de cafe, fita adesiva remendando — parece que existe ha DECADAS.

### Frame 3 — Abre a Pasta
- **Corpo**: Segura a pasta aberta na frente do corpo.
- **Rosto**: SORRISO COMPLETO. Unico momento alem do death/attack onde a cara de paisagem QUEBRA significativamente. E um sorriso SINISTRAMENTE satisfeito.
- **Orelhas**: Vibrando de excitacao.
- **Olhos**: Brilhando verde, AMBOS focados na pasta.
- **Detalhe**: Luz emana de dentro da pasta (como briefcase do Pulp Fiction). Documentos comecam a se soltar.

### Frame 4 — Documentos Voam
- **Corpo**: Braco levanta a pasta pro alto.
- **Rosto**: Volta a cara de paisagem (a diversao acabou, agora e trabalho).
- **Orelhas**: Enormes, apontando pra cima.
- **Detalhe principal**: DOCUMENTOS VOAM em todas as direcoes. 8-10 folhas visiveis. Cada folha tem:
  - Nome de um boss na etiqueta (XANDAO, GILMAR, BARROSO, LULA, BOLSO, VORCARO, FLAVIO DINO, HUGO MOTTA)
  - Carimbo "CONFIDENCIAL" em vermelho
  - Fotos borradas (silhuetas reconheciveis dos bosses)
  - Texto ilegivel mas ameacador
- **Efeito**: Documentos giram em espiral ascendente, brilhando em verde.

### Frame 5 — Informacao se Espalha
- **Corpo**: Pasta vazia na mao, braço abaixando.
- **Rosto**: Paisagem total.
- **Orelhas**: Neutras.
- **Detalhe**: Documentos se transformam em particulas de luz verde que se espalham pela tela, indo na direcao de cada boss referenciado. Efeito visual de "debuff aplicado".
- **UI implicado**: Icone de "ENFRAQUECIDO" apareceria sobre bosses afetados.

### Frame 6 — Pasta Vazia
- **Corpo**: Guarda a pasta vazia de volta na toga. Ajusta a toga.
- **Rosto**: Cara de paisagem, mas com AQUELE micro sorriso de canto. "O estrago ta feito."
- **Orelhas**: Relaxadas, satisfeitas.
- **Maos**: Ajustando toga, escondendo evidencias.
- **Detalhe**: Pasta sumindo de volta nos bolsos internos. Um unico papel esquecido flutuando pro chao ao lado dele (detalhe comico).

---

## SPECIAL 3 - "Gravacao Fantasma" (6 frames)

**Arquivo**: `toffoli_special_fantasma.png` (384x64 px)

**Mecanica**: Repete a ultima acao do inimigo contra o proprio inimigo (ataque refletido via gravacao).

### Frame 1 — Prepara Gravador
- **Corpo**: Toffoli em posicao firme. Corpo virado pro inimigo.
- **Rosto**: Cara de paisagem... mas com um BRILHO nos olhos que nao deveria estar la.
- **Orelhas**: Apontadas pro inimigo, vibrando.
- **Maos**: Gravador LEVANTADO a altura da cabeca. O gravador BRILHA verde intenso (#00FF88) — esta carregado com a gravacao anterior (do special "Escuta Secreta").
- **Detalhe**: Fita cassete visivel, girando. Luz REC pulsando. Aura verde ao redor do gravador.

### Frame 2 — Aperta Play
- **Corpo**: Braço estende o gravador na direcao do inimigo.
- **Rosto**: SORRISO DIABOLICO. A mascara cai completamente neste momento. E o Toffoli mais expressivo do jogo — porque finalmente esta usando a informacao que coletou.
- **Orelhas**: Retas, tensas.
- **Olhos**: AMBOS focados no inimigo, brilhando verde.
- **Maos**: Dedo aperta PLAY com forca.
- **Detalhe**: Som visivel saindo do gravador — onda conica verde. A fita cassete gira ao contrario (playback).

### Frame 3 — Holograma Aparece
- **Corpo**: Toffoli firma, segurando gravador apontado.
- **Rosto**: Sorriso diminui pro micro-sorriso usual.
- **Detalhe principal**: Do gravador, emana um HOLOGRAMA VERDE do inimigo. O holograma e uma silhueta translucida do boss/inimigo que foi gravado, feita de linhas verdes com ruido estatico. O holograma esta em posicao de ATAQUE — reproduzindo exatamente o que o inimigo fez.
- **Efeito visual**: Linhas de varredura horizontais sobre o holograma (como TV antiga). Brilho verde pulsante. Particulas de dados flutuando.

### Frame 4 — Holograma Ataca
- **Corpo**: Toffoli imóvel, assistindo.
- **Rosto**: Cara de paisagem RESTAURADA. Assistindo como se nao tivesse nada a ver.
- **Detalhe principal**: O HOLOGRAMA executa o ataque do inimigo — mas CONTRA o inimigo original. A silhueta verde avanca, replica o movimento exato. E como assistir um replay fantasmagorico.
- **Efeito visual**: Rastro verde atras do holograma. Distorcao visual ao redor. Som visivel (ondas) emanando.

### Frame 5 — Impacto
- **Corpo**: Toffoli da um micro-passo pra tras (onda de choque).
- **Rosto**: Paisagem imperturbavel.
- **Detalhe**: Holograma faz contato com o inimigo. EXPLOSAO de particulas verdes e brancas. Flash de luz. Distorcao de tela (shake). O inimigo e atingido pelo proprio ataque.
- **Efeito visual**: Circulos concentricos de impacto (verde + branco). Fragmentos de dados explodindo. "PLAYBACK" em texto pixelado flutuando.

### Frame 6 — Dissipacao
- **Corpo**: Volta a posicao normal. Gravador volta pra posicao escondida.
- **Rosto**: Cara de paisagem PERFEITA. Como se NADA tivesse acontecido.
- **Orelhas**: Neutras, satisfeitas.
- **Detalhe**: Holograma se dissolve em particulas verdes que se dispersam. Fita cassete para de girar. Luz REC apaga (gravacao usada). Gravador volta a ser "discreto".
- **Detalhe comico**: Um ultimo fragmento de holograma mostra a "cara de choque" do inimigo, congelada, antes de se dissolver.

---

## PROJETEIS E EFEITOS (32x32 px)

### Projetil — Onda Sonora de Ataque
**Arquivo**: `toffoli_proj_onda.png` (128x32 px — 4 frames de animacao)
- **Frame 1**: Circulo concentrico verde (#00FF88) pequeno, com texto "GRAVEI" visivel.
- **Frame 2**: Circulo expande, texto muda pra "FLAGRA!", ondulacao visivel.
- **Frame 3**: Circulo quase tamanho maximo, texto "DOSSIÊ", distorcao nas bordas.
- **Frame 4**: Circulo se dissipa, particulas de texto explodindo.
- **Transparencia**: Fundo transparente. Onda semi-transparente (opacity 70%).

### Efeito — Ondas de Escuta (Passive)
**Arquivo**: `toffoli_fx_escuta.png` (128x32 px — 4 frames)
- Circulos concentricos verdes emanando das orelhas.
- Cada frame o circulo expande e fica mais transparente.
- Pulsa no ritmo de 2 fps (lento, constante).

### Efeito — Documentos Voando
**Arquivo**: `toffoli_fx_dossie.png` (192x32 px — 6 frames)
- Folhas de papel amareladas girando no ar.
- Cada frame muda a rotacao e posicao das folhas.
- Carimbos "CONFIDENCIAL" visiveis em vermelho em algumas folhas.
- Nomes de bosses legiveis nas etiquetas.

### Efeito — Holograma Fantasma
**Arquivo**: `toffoli_fx_holograma.png` (192x32 px — 6 frames)
- Silhueta verde translucida de humanoide generico.
- Linhas de varredura horizontal (como TV antiga).
- Ruido estatico piscando.
- Cada frame aumenta/diminui o brilho (pulsacao).

### Efeito — Luz REC
**Arquivo**: `toffoli_fx_rec.png` (64x32 px — 2 frames)
- Frame 1: Ponto vermelho brilhante + texto "REC" em branco.
- Frame 2: Ponto vermelho apagado (piscando).
- Usado como overlay no gravador em diversas animacoes.

---

## SPRITESHEET COMPLETA — Resumo

| Animacao            | Frames | Arquivo                          | Tamanho Total     |
|--------------------|--------|----------------------------------|-------------------|
| Idle               | 4      | `toffoli_idle.png`               | 256x64 px         |
| Walk               | 6      | `toffoli_walk.png`               | 384x64 px         |
| Attack             | 3      | `toffoli_attack.png`             | 192x64 px         |
| Death              | 4      | `toffoli_death.png`              | 256x64 px         |
| Hit                | 2      | `toffoli_hit.png`                | 128x64 px         |
| Special: Escuta    | 4      | `toffoli_special_escuta.png`     | 256x64 px         |
| Special: Dossie    | 6      | `toffoli_special_dossie.png`     | 384x64 px         |
| Special: Fantasma  | 6      | `toffoli_special_fantasma.png`   | 384x64 px         |
| Proj: Onda Sonora  | 4      | `toffoli_proj_onda.png`          | 128x32 px         |
| FX: Escuta         | 4      | `toffoli_fx_escuta.png`          | 128x32 px         |
| FX: Dossie         | 6      | `toffoli_fx_dossie.png`          | 192x32 px         |
| FX: Holograma      | 6      | `toffoli_fx_holograma.png`       | 192x32 px         |
| FX: Luz REC        | 2      | `toffoli_fx_rec.png`             | 64x32 px          |

**Total de frames**: 4+6+3+4+2+4+6+6+4+4+6+6+2 = **57 frames**

---

## Notas para o Artista

1. **CARA DE PAISAGEM e LEI**: Em 90% dos frames, a expressao e NADA. Vazio. Paisagem. A ausencia de expressao E a expressao.
2. As EXCECOES sao especificas e RARAS: micro-sorriso no attack F1, surpresa no hit F1, sorriso no dossie F3, sorriso diabolico no fantasma F2. Cada quebra da paisagem e uma recompensa visual pro jogador.
3. **Orelhas sao o elemento expressivo principal**: Ja que o rosto nao se move, as ORELHAS fazem o trabalho emocional. Elas giram, captam, murcham, crescem. Sao o verdadeiro "rosto" do Toffoli.
4. **Olhos independentes**: SEMPRE um olho olhando pra frente (mantendo fachada) e outro espiando pro lado. Excecao: hit e death (ambos na mesma direcao por choque).
5. **Microfones escondidos**: Devem ser TECNICAMENTE escondidos (na narrativa) mas VISUALMENTE obvios (pro jogador). E a piada visual central.
6. **Linhas grossas, sombras pesadas**: Estilo Andre Guedes. Underground comix. Robert Crumb brasileiro.
7. **Cores saturadas-sujas**: Nada brilhante ou limpo. Ate o verde do holograma deve ter "sujeira".
8. **Animacao jerky**: Transicoes BRUSCAS entre frames. Sem interpolacao. Corte seco. 8-12 fps.
9. **O gravador e quase um personagem**: Tem personalidade propria — pisca, brilha, gira a fita. E a extensao da alma do Toffoli.
10. **Contraste e TUDO**: O personagem mais visualmente "sem graca" do jogo E o mais perigoso. Isso deve transparecer nos detalhes, nao na aparencia geral.
