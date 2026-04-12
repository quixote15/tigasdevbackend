# BRIGA GILMAR vs BARROSO -- Especificacao Completa de Animacao

## Mecanica Especial de Interacao entre Bosses | Zumbis de Brasilia

**Duracao total:** 10 segundos (10.000ms)
**Tipo:** Cutscene interativa / Evento ambiental automatico
**Tom:** COMEDIA PURA. Opera bufa. Circo do STF. Dois palhacos de toga se destruindo.
**Referencia historica:** Briga real entre Gilmar Mendes e Luis Roberto Barroso no plenario do STF, 2018. Virou musica, samba, poema recitado por Maria Bethania, memes eternos.

---

> *"Voce e uma pessoa horrivel, uma mistura do mal com atraso e pitadas de psicopatia."*
> -- Barroso para Gilmar, ao vivo, no plenario do STF, com camera ligada

> *"Vagabundo! Vagabundo! Vagabundo!"*
> -- Gilmar para Barroso, 3 vezes, porque tudo no Gilmar vem em TRIOS

---

# 1. CONDICOES DE ATIVACAO (TRIGGER)

## 1.1 Condicao Principal

| Parametro              | Valor                                                     |
|------------------------|-----------------------------------------------------------|
| Tipo de trigger        | Proximidade entre dois bosses no mesmo mapa               |
| Raio de deteccao       | 128px (2x o tamanho do sprite de cada um)                 |
| Bosses necessarios     | `boss_gilmar` E `boss_barroso` ambos VIVOS no mesmo mapa  |
| Estado minimo          | Ambos devem estar em estado `ACTIVE` (nao em death/spawn) |
| Cooldown               | 60 segundos apos o termino da briga anterior              |
| Prioridade             | MAXIMA -- interrompe qualquer acao de ambos os bosses      |
| Pode ser interrompida  | NAO. Uma vez ativada, roda ate o fim dos 10 segundos      |

## 1.2 O Que Acontece com o Jogador

| Parametro                     | Valor                                                          |
|-------------------------------|----------------------------------------------------------------|
| Controle do jogador           | MANTIDO -- jogador pode se mover livremente                    |
| Ataques do jogador            | HABILITADOS -- pode atacar ambos durante a briga               |
| Dano ao jogador               | NENHUM dos dois bosses ataca o jogador durante a briga         |
| Posicao sugerida              | Camera faz leve zoom out (1.2x) para enquadrar ambos           |
| Indicador visual              | Seta piscante apontando para a briga se jogador estiver longe  |
| Aggro dos outros zumbis       | Zumbis normais PAUSAM e assistem (idle de espectador)           |

## 1.3 Sequencia de Ativacao

```
1. boss_gilmar E boss_barroso entram no raio de 128px
2. Ambos PARAM instantaneamente (cancelam acao atual)
3. Ambos viram um pro outro (sprite orientation = face_target)
4. Flash de "!" acima de ambas as cabecas (16x16px, 200ms)
5. Overlay "BRIGA NO STF!" aparece no centro da tela (300ms, fonte pixelada vermelha)
6. Camera faz zoom out suave (500ms, de 1.0x pra 1.2x)
7. Timer de 10 segundos inicia
8. Briga comeca
```

## 1.4 Como a Briga Termina

| Condicao                   | Resultado                                                             |
|----------------------------|-----------------------------------------------------------------------|
| Timer de 10s esgota        | Ambos sao separados por "forca invisivel" (empurrao de 64px cada)     |
| Um dos dois morre          | O sobrevivente faz pose de vitoria (2s) e volta a atacar o jogador    |
| Ambos morrem               | Duplo death simultaneo -- JACKPOT para o jogador                      |
| Jogador morre durante      | Game Over normal -- a briga continua no background (comedia)          |

## 1.5 Pos-Briga

- Ambos ficam com **50% do HP que tinham ao INICIAR** a briga (se destruiram mutuamente)
- Debuff de 5 segundos: `HUMILHADO` -- ambos se movem 30% mais devagar, atacam 20% mais fraco
- Toga de ambos fica visivelmente danificada ate o fim da fase (sprite swap permanente)
- Cooldown de 60 segundos antes de poder brigar novamente
- Se o jogador causou dano durante a briga, ambos ganham aggro DOBRADO no jogador apos a briga

---

# 2. FASES DA BRIGA (10 Segundos)

## FASE 1: DETECCAO (0.0s -- 2.0s) | "O Reencontro"

**Tom:** Suspense comico. Dois inimigos mortais se reconhecem no campo de batalha.

### Timeline Detalhada

| Tempo (ms) | Gilmar                                           | Barroso                                         | Efeito Visual                          |
|------------|--------------------------------------------------|--------------------------------------------------|----------------------------------------|
| 0-200      | PARA. Corpo trava. Pastel cai da mao.            | PARA. Martelo congela no ar.                     | Flash branco de 1 frame na tela        |
| 200-500    | Vira lentamente pro Barroso. Oculos brilham.     | Vira pro Gilmar. Oculos comecam a embacar.       | "!" acima de ambos (sprite 16x16)      |
| 500-800    | Sorrisinho cinico se forma. Papada treme.        | Veia da testa comeca a pulsar. Mandibula trava.  | Zoom out da camera (1.0x -> 1.1x)     |
| 800-1200   | Aponta o dedo. Boca abre. Papada BALANCA.        | Mao aperta o martelo. Rosto avermelha.           | Linhas de tensao entre ambos (efeito)  |
| 1200-1500  | "Heh heh heh" -- risadinha de deboche visivel    | Respira fundo. Peito expande. Tenta se controlar.| Tremor na tela (1px, sutil)            |
| 1500-2000  | Toma posicao de confronto. Mao no bolso da toga. | Compostura DESMORONANDO. Dedo levanta.           | "BRIGA NO STF!" overlay aparece        |

### Sprites Necessarios -- Fase 1

**GILMAR (6 frames, 64x64px cada):**

| Frame | Nome                    | Descricao Detalhada                                                                                        |
|-------|-------------------------|------------------------------------------------------------------------------------------------------------|
| F1-01 | `gilmar_detect_freeze`  | Gilmar congela mid-action. O que quer que estivesse fazendo, PARA. Pastel no ar comecando a cair. Olhos arregalados por 1 frame (UNICO momento de surpresa -- depois vira deboche). Papada estatica. |
| F1-02 | `gilmar_detect_turn`    | Corpo virando 45 graus em direcao ao Barroso. Oculos refletem luz (flash branco de 2px nas lentes). Sorrisinho COMECANDO a se formar no canto da boca. Papada comeca a tremer com o movimento da virada. |
| F1-03 | `gilmar_detect_smirk`   | Sorrisinho COMPLETO. O sorriso cinico de quem encontrou seu brinquedo favorito. Oculos brilhando com malicia. Papada tripla tremendo de antecipacao. Uma das maos levantando lentamente para apontar. |
| F1-04 | `gilmar_detect_point`   | Dedo esticado na direcao do Barroso. Boca aberta em risada muda. Corpo inclinado pra frente, agressivo mas DIVERTIDO. Papada balancando como gelatina. Toga com pastel amassado no ombro. |
| F1-05 | `gilmar_detect_laugh`   | Gargalhada: boca ABERTA mostrando dentes (4px de boca). Papada TREMENDO violentamente. Corpo sacode com a risada. Oculos descem 1px no nariz. Os olhos sao fendas de prazer maligno. |
| F1-06 | `gilmar_detect_stance`  | Posicao de combate do Gilmar: pernas afastadas, ombros pra frente, mao no bolso (buscando outro pastel?), sorriso agora FIXO e AMEACADOR. Papada projetada. Oculos firmes. |

**BARROSO (6 frames, 64x64px cada):**

| Frame | Nome                      | Descricao Detalhada                                                                                        |
|-------|---------------------------|------------------------------------------------------------------------------------------------------------|
| F1-01 | `barroso_detect_freeze`   | Barroso congela com o martelo no ar. Expressao de quem sentiu um cheiro ruim. Olhos se estreitam. Corpo RIGIDO. Toga impecavel (por enquanto). Veia da testa APARECE pela primeira vez (1px de largura). |
| F1-02 | `barroso_detect_turn`     | Vira em direcao ao Gilmar com postura ERECTA, professoral. Queixo levantado. Ombros pra tras. Tentando manter superioridade. Oculos perfeitamente posicionados. Veia pulsa (2px). |
| F1-03 | `barroso_detect_tense`    | Mandibula TRAVA. Dentes cerrados visiveis. Mao aperta o martelo ate os dedos ficarem brancos (#FFFFFF nas juntas). Veia pulsa mais rapido. Oculos comecam a EMBACAR levemente na borda. |
| F1-04 | `barroso_detect_flush`    | Rosto comeca a avermelhar: pele muda de #D4A574 para #C87A5A. Veia cresce (3px). Mao livre se fecha em punho. Oculos 20% embasados. Respiracao visivel (peito sobe/desce 1px). |
| F1-05 | `barroso_detect_breathe`  | Inspira PROFUNDAMENTE. Peito expande 2px. Tentativa VISIVEL de se controlar. Olhos fecham por 1 frame. Quando abrem, estao FURIOSOS. Veia LATEJANDO. Oculos 40% embasados. |
| F1-06 | `barroso_detect_stance`   | Compostura RACHANDO: dedo comeca a levantar para acusacao. Postura ainda ereta mas TREMENDO. Rosto #C85A5A (vermelho subindo). Veia 4px. Oculos 50% embasados. Toga comeca a amarrotar nos ombros. |

---

## FASE 2: ESCALADA VERBAL (2.0s -- 5.0s) | "As Frases que Viraram Meme"

**Tom:** COMEDIA DE GRITARIA. Opera do absurdo. Dois homens de toga se xingando como vizinhos brigando por causa de muro.

### Timeline Detalhada

| Tempo (ms) | Gilmar                                           | Barroso                                         | Dialogo / Efeito                                  |
|------------|--------------------------------------------------|--------------------------------------------------|----------------------------------------------------|
| 2000-2500  | Escuta. Sorri. Papada treme de prazer.            | EXPLODE: "Voce e uma pessoa HORRIVEL!"           | Balao de fala do Barroso (128x48px) com texto       |
| 2500-3000  | Riso. Deboche TOTAL. Aponta e ri.                | "Uma mistura do mal com atraso..."                | Texto aparece em sequencia no balao                  |
| 3000-3500  | Sorrisinho vira FURIA subita                     | "...e pitadas de psicopatia!"                     | Barroso: veia MAXIMA. Gilmar: transicao de riso->raiva |
| 3500-4000  | "VAGABUNDO!" -- grito ENORME                      | Recua 2px. Oculos escorregam.                    | Balao do Gilmar EXPLODE na tela. Camera shake.       |
| 4000-4500  | "VAGABUNDO!!" -- segundo grito, MAIS alto        | Tenta responder, boca abre e fecha. Interrompido.| Segundo balao. Letras MAIORES que o primeiro.        |
| 4500-5000  | "VAGABUNDO!!!" -- terceiro, APOCALIPTICO         | "Nao consegue articular um argumento!"            | Ambos gritando simultaneamente. Baloes COLIDEM.      |

### Sprites Necessarios -- Fase 2

**GILMAR -- Sequencia Verbal (8 frames, 64x64px):**

| Frame | Nome                    | Descricao Detalhada                                                                                        |
|-------|-------------------------|------------------------------------------------------------------------------------------------------------|
| F2-01 | `gilmar_listen_smirk`   | Ouvindo o Barroso com PRAZER. Braco cruzado. Cabeca levemente inclinada pro lado. Sorrisinho de "continue, por favor". Papada relaxada. Oculos empurrados pro alto da testa como quem nao acredita no que ouve. |
| F2-02 | `gilmar_listen_laugh`   | GARGALHADA de deboche ao ouvir "pessoa horrivel". Boca ESCANCARADA. Papada TREMELICANDO como pudim num terremoto. Corpo se curva pra frente de tanto rir. Lagrima de riso (1px brilhante no canto do olho). |
| F2-03 | `gilmar_laugh_point`    | Apontando pro Barroso ENQUANTO ri. Dedo esticado tremendo de riso. Outra mao segurando a barriga. Oculos tortos de tanto rir. Papada em pleno caos. Migalhas de pastel caindo da toga com o sacolejo. |
| F2-04 | `gilmar_rage_transition`| TRANSICAO: riso morre. Sorriso congela. Olhos se estreitam. Em 1 frame, Gilmar vai de "isto e hilario" para "agora voce vai ver". Papada PARA de tremer (sinal de perigo). Mao desce e fecha em punho. |
| F2-05 | `gilmar_vagabundo_1`    | PRIMEIRO "VAGABUNDO!": boca ENORME (ocupa 40% do rosto). Corpo inteiro projetado pra frente. Dedo na cara do Barroso. Papada SOLIDA de tensao. Veias no pescoco aparecendo. Oculos quase caindo. Toga esvoaca com a forca do grito. |
| F2-06 | `gilmar_vagabundo_2`    | SEGUNDO "VAGABUNDO!!": MAIS intenso. Corpo se levanta nas pontas dos pes (ganha 2px de altura). Boca AINDA MAIOR. Papada vermelha. CUSPE visivel saindo da boca (2-3 particulas de 1px). Oculos pendurados numa orelha. |
| F2-07 | `gilmar_vagabundo_3`    | TERCEIRO "VAGABUNDO!!!": O APICE. Gilmar parece ter DOBRADO de tamanho. Boca ocupa METADE do sprite. Onda sonora visivel saindo da boca (linhas concentricas). Oculos VOAM do rosto (sprite separado). Papada vibra tao rapido que vira blur. Toga RASGANDO nas costuras. Pastel que estava no bolso SAI VOANDO com a forca do berro. |
| F2-08 | `gilmar_scream_sustain` | Grito sustentado: mesma posicao do frame 7 mas com tremor de 1px random. Rosto roxo de gritar. Veias do pescoco SALTANDO. Boca travada aberta. Este frame LOOPA por 500ms para dar sensacao de grito continuo. |

**BARROSO -- Sequencia Verbal (8 frames, 64x64px):**

| Frame | Nome                       | Descricao Detalhada                                                                                        |
|-------|----------------------------|------------------------------------------------------------------------------------------------------------|
| F2-01 | `barroso_accuse_start`     | Dedo levantado, postura professoral. Boca abre com DIGNIDADE FORJADA. Olhar de superioridade. "Voce..." -- o inicio do discurso. Veia 4px mas controlada. Oculos 50% embasados. Toga ainda relativamente arrumada. |
| F2-02 | `barroso_accuse_pessoa`    | "...e uma pessoa HORRIVEL" -- a palavra HORRIVEL deforma o rosto. Boca abre MAIS do que o normal. Sobrancelhas cerradas ao MAXIMO. Dedo treme apontando. Veia PULSA visivelmente (alternancia 4px/5px entre frames). Testa com suor (3 gotas de 1px). |
| F2-03 | `barroso_accuse_mistura`   | "Uma mistura do mal com atraso" -- gesticulacao de professor. Mao faz gesto de "lista" (contando nos dedos). Postura TENTA ser academica mas o corpo TREME de raiva. Rosto #C85A5A. Veia 5px. Oculos 60% embasados. |
| F2-04 | `barroso_accuse_psicopatia`| "...e pitadas de PSICOPATIA!" -- a palavra PSICOPATIA e CUSPIDA. Corpo INTEIRO se projeta pra frente. ABANDONA postura professoral. Boca deformada de raiva. Oculos ESCORREGAM do nariz (ficam na ponta, 2px mais baixo). Veia 6px. Toga amarrotando. |
| F2-05 | `barroso_recoil_1`         | Recebendo o primeiro "VAGABUNDO!": recua 2px. Olhos arregalados de surpresa por 1 frame. Oculos saltam. Cabelo se desalinha (1-2 fios saem do lugar -- PRIMEIRA VEZ no jogo). Veia EXPLODE pra 7px. |
| F2-06 | `barroso_recoil_2`         | Recebendo o segundo "VAGABUNDO!!": recua mais 1px. Tenta falar mas Gilmar nao deixa. Boca abre-fecha-abre (3 posicoes em 1 frame, blur de boca). Mao levantada em gesto de "espera" que e ignorado. Oculos CAEM ate a ponta do nariz. |
| F2-07 | `barroso_counter_yell`     | CONTRA-ATAQUE VERBAL: "Nao consegue articular um ARGUMENTO!" -- finalmente consegue gritar. Mas ja esta DESCOMPOSTO. Cabelo desalinhado. Oculos tortos. Veia 8px (ENORME). Toga com vincos. A compostura MORREU. |
| F2-08 | `barroso_scream_overlap`   | Gritando SIMULTANEAMENTE com o Gilmar. Ambas as bocas abertas. O som de ambos se cancela visualmente (baloes de fala COLIDEM e se destroem). Barroso esta IRRECONHECIVEL: cabelo bagunçado, oculos pendendo de uma orelha, toga amassada, suor escorrendo, veia pulsando como stroboscope. |

### Baloes de Fala -- Especificacao

| Balao | Tamanho    | Texto                                                              | Fonte           | Cor Fundo  | Cor Texto  | Efeito                          |
|-------|------------|--------------------------------------------------------------------|-----------------|------------|------------|----------------------------------|
| B-01  | 128x48px   | "VOCE E UMA PESSOA HORRIVEL!"                                     | Pixel bold 8px  | #FFFFFF    | #CC1144    | Texto aparece letra por letra    |
| B-02  | 160x32px   | "Uma mistura do mal com atraso e pitadas de psicopatia!"           | Pixel italic 6px| #FFFFFF    | #8B0000    | Texto scrolls da esquerda        |
| B-03  | 96x48px    | "VAGABUNDO!"                                                       | Pixel ULTRA BOLD 12px | #FF0000 | #FFFFFF  | Aparece com EXPLOSAO. Camera shake. |
| B-04  | 112x56px   | "VAGABUNDO!!"                                                      | Pixel ULTRA BOLD 14px | #FF0000 | #FFFFFF  | MAIOR que o anterior. Fonte CRESCE. |
| B-05  | 128x64px   | "VAGABUNDO!!!"                                                     | Pixel ULTRA BOLD 16px | #FF0000 | #FFD700  | ENORME. Texto PULSA. RACHA a borda. |
| B-06  | 96x32px    | "Nao consegue articular um argumento!"                             | Pixel bold 7px  | #FFFFFF    | #4A2A8A    | Aparece rapido mas e ATROPELADO pelo B-05 |
| B-07  | 80x24px    | "@#$%&*!" (ambos simultaneos)                                      | Pixel 8px       | #FF6600    | #000000    | Simbolos GIRAM dentro do balao   |

---

## FASE 3: COMEDIA FISICA (5.0s -- 8.0s) | "O Circo Pegou Fogo"

**Tom:** SLAPSTICK PURO. Dois homens idosos de toga se empurrando, puxando cabelo, batendo com pastel e martelo. Three Stooges no plenario do STF.

### Timeline Detalhada

| Tempo (ms) | Gilmar                                           | Barroso                                         | Efeito Visual                                     |
|------------|--------------------------------------------------|--------------------------------------------------|----------------------------------------------------|
| 5000-5500  | Empurra o Barroso com as duas maos               | Empurrado, cambaleia 4px pra tras                | Particulas de poeira no chao. "PUSH!" onomatopeia. |
| 5500-6000  | Ri do Barroso cambaleando                         | Recupera. PUXA a toga do Gilmar.                 | Toga do Gilmar estica como borracha (comedia)        |
| 6000-6500  | Toga RASGA. Pastel CAI do bolso secreto.          | Tropeça na propria toga ao puxar.                | Pastel voa em arco. Barroso no chao.                |
| 6500-7000  | ARREMESSA o pastel no Barroso                     | Recebe pastel NA CARA. Oculos quebram.           | SPLAT! Particulas de pastel. Oculos em cacos.        |
| 7000-7500  | Avanca pra cima do Barroso                        | Bate com o martelo na canela do Gilmar           | "BONK!" onomatopeia. Gilmar pula de dor.            |
| 7500-8000  | Togas se EMARANHAM. Ambos caem num BOLO.         | Togas emaranhadas. Braco de um, perna de outro.  | Nuvem de briga classica (poeira + estrelas + bracos) |

### Sprites Necessarios -- Fase 3

**SPRITES DE INTERACAO (tamanho especial: 128x64px -- ambos no mesmo frame):**

Estes sprites sao ESPECIAIS: ambos os personagens aparecem no MESMO sprite, pois estao fisicamente interagindo.

| Frame | Nome                        | Tamanho   | Descricao Detalhada                                                                                        |
|-------|-----------------------------|-----------|-----------------------------------------------------------------------------------------------------------|
| F3-01 | `briga_push`                | 128x64px  | Gilmar (esquerda) empurra Barroso (direita) com as duas maos no peito. Gilmar: expressao de FURIA DIVERTIDA, papada projetada pra frente, pes fincados no chao. Barroso: corpo inclinado 20 graus pra tras, bracos abertos tentando equilibrio, toga flutuando com o impacto, oculos escorregando. Linhas de impacto (3 linhas radiando do ponto de contato). |
| F3-02 | `briga_toga_pull`           | 128x64px  | Barroso (direita) puxa a toga do Gilmar (esquerda) com as duas maos. A toga do Gilmar ESTICA grotescamente como borracha, 16px alem do corpo. Gilmar: arregalado, surpreso, corpo puxado em direcao ao Barroso. Pastel visivel num bolso interno que se revela com o puxao. Barroso: puxando com expressao de "agora voce vai ver", dentes cerrados, pe apoiado pra tras dando forca. |
| F3-03 | `briga_toga_rip`            | 128x64px  | RIIIIIP! Toga do Gilmar RASGA. Pedaco de toga fica na mao do Barroso. Gilmar: olha pra baixo pra toga rasgada, expressao de ULTRAGE FALSO (ele nao liga, mas finge). Pastel ENORME cai do bolso secreto da toga (revelando que carregava pastel dentro da toga o tempo todo). Barroso: segurando pedaco de toga, perdendo equilibrio pra tras. Fios de tecido voam. |
| F3-04 | `briga_pastel_throw`        | 128x64px  | Gilmar (esquerda) em pose de arremesso atletico. Pastel no ar entre os dois (sprite de projetil separado de 16x16px, arco parabolico). Gilmar: sorriso MANIACAMENTE feliz, como crianca jogando bola de neve. Corpo girado pos-arremesso. Barroso: olhos arregalados seguindo o pastel, boca em "O", mao levantada em defesa inutil. Camera angle sugere slow-motion. |
| F3-05 | `briga_pastel_hit`          | 128x64px  | SPLAT! Pastel EXPLODE na cara do Barroso. Oleo, massa e recheio de carne moida espalhados pelo rosto, toga, cabelo IMPECAVEL (nao mais). Gilmar: GARGALHADA DEMONÍACA, corpo dobrado de rir, papada tremendo como terremoto. Barroso: rosto coberto de pastel, oculos QUEBRAM (um lente racha, armacao entorta), cabelo com massa de pastel, toga com manchas amarelo-gorduroso. A DIGNIDADE do Barroso morreu neste frame. |
| F3-06 | `briga_martelo_canela`      | 128x64px  | Barroso (direita, sujo de pastel) bate o martelo na canela do Gilmar. Martelo no ponto de impacto. Gilmar: PULA de dor (ambos os pes no ar, 4px acima do chao), boca aberta em UIVO, oculos voam pra cima, papada balanca pra cima com o pulo. Barroso: agachado, martelo estendido, sorriso VINGATIVO pela primeira vez (raro -- Barroso quase nunca sorri no jogo). Estrelas de dor ao redor da canela do Gilmar (3 estrelas 4x4px). |
| F3-07 | `briga_tangle`              | 128x64px  | EMARANHAMENTO: as togas de ambos se cruzam e ENGANCHAM. Ambos caindo. Bracos de um se misturam com pernas de outro. IMPOSSIVEL dizer onde um comeca e o outro termina. Nuvem de confusao (particulas de poeira, estrelas, exclamacoes). Um sapato do Gilmar voando pra fora. O martelo do Barroso voando pro outro lado. CAOS PURO. |
| F3-08 | `briga_dustcloud`           | 128x64px  | A NUVEM DE BRIGA CLASSICA de desenho animado: circulo de poeira (96x64px) com bracos, pernas, oculos, pedacos de toga e pasteis saindo e entrando da nuvem. Dentro: flashes de impacto (estrelas amarelas). Onomatopeias rotativas ao redor: "POW!", "SLAP!", "CRACK!", "@#$%!". A nuvem se move 2px random por frame (trepidacao). |

### Particulas da Fase 3

| Particula               | Tamanho | Cor         | Quantidade | Trigger                  | Comportamento                                |
|--------------------------|---------|-------------|------------|--------------------------|----------------------------------------------|
| Poeira de impacto        | 3x3px   | #C0A878     | 4-6        | Push, queda              | Radial do ponto de impacto, fade 300ms       |
| Fios de toga             | 2x6px   | #0A0A0A     | 3-4        | Toga rasga               | Flutuam pra baixo com gravidade leve          |
| Gotas de oleo de pastel  | 2x2px   | #DAA520     | 6-8        | Pastel explode           | Radial explosivo, escorrem para baixo         |
| Migalhas de pastel       | 1x1px   | #E8C864     | 8-12       | Pastel explode           | Espirram em todas direcoes, gravidade rapida  |
| Estrelas de dor          | 4x4px   | #FFD700     | 3          | Martelo na canela        | Giram ao redor do ponto de impacto, 500ms     |
| Cacos de oculos          | 3x2px   | #E8E8F0     | 4-5        | Oculos quebram           | Caem com gravidade, 1 flash de reflexo cada   |
| Suor/respingos           | 1x2px   | #87CEEB     | 4-6        | Esforco fisico           | Saem da cabeca, arco parabolico               |
| Fragmentos de onomatopeia| 8x8px   | Variado     | 3-4        | Nuvem de briga           | "POW", "BAM" entram e saem da nuvem           |

---

## FASE 4: CLIMAX E SEPARACAO (8.0s -- 10.0s) | "O Desfecho Opulento"

**Tom:** Anticlimactico e hilario. Depois de TODA essa guerra, ambos se separam exaustos, arrasados, ridiculamente destruidos. A dignidade de ambos foi para o esgoto da Esplanada.

### Timeline Detalhada

| Tempo (ms) | Gilmar                                           | Barroso                                          | Efeito Visual                                    |
|------------|--------------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| 8000-8500  | Nuvem se dissipa. Ambos de costas no chao.       | No chao, do outro lado. Toga rasgada.            | Nuvem de poeira se dissipa lentamente             |
| 8500-9000  | Tenta levantar. Cai. Tenta de novo.              | Levanta com dificuldade. Descobre toga rasgada.  | Camera volta ao zoom normal (1.2x -> 1.0x)       |
| 9000-9500  | De pe, cambaleando. Procura os oculos.            | De pe. Tenta arrumar o cabelo. NAO CONSEGUE.    | Zumbis espectadores voltam ao normal              |
| 9500-10000 | Coloca oculos tortos. Sorrisinho de volta.        | Desiste de arrumar. Olha pro jogador. Recomeca.  | Timer "BRIGA NO STF!" desaparece. Musica some.   |

### Sprites Necessarios -- Fase 4

**GILMAR -- Pos-Briga (6 frames, 64x64px):**

| Frame | Nome                      | Descricao Detalhada                                                                                        |
|-------|---------------------------|------------------------------------------------------------------------------------------------------------|
| F4-01 | `gilmar_ground`           | Gilmar ESTATELADO no chao, de costas. Toga rasgada, aberta, revelando camisa de baixo (com estampa de "EU AMO HABEAS CORPUS" -- easter egg). Oculos a 32px de distancia do corpo. Papada escorrida pro lado como massa. Pastel amassado do lado. Expressao: AINDA sorrindo. Mesmo no chao, destruido, o Gilmar SORRI. |
| F4-02 | `gilmar_getup_fail`       | Tentando levantar: bracos empurram o chao, corpo sobe 4px, FALHA, desaba de volta. Pernas bambas. Toga presa debaixo do corpo. Papada balanca com a queda. Expressao: levemente irritado consigo mesmo mas AINDA com resquicio de sorriso. |
| F4-03 | `gilmar_getup_success`    | De pe, CAMBALEANDO. Corpo em S (coluna torta). Toga pendendo de um ombro so. Outro ombro com camisa exposta. Pastel no cabelo. Procurando os oculos no chao com a mao tateando o ar. Papada mole, cansada, mas voltando ao formato normal. |
| F4-04 | `gilmar_find_glasses`     | Encontra os oculos: tortos, uma lente rachada, armacao entortada. Coloca no rosto assim mesmo. Olha pela lente rachada com expressao de "serve". Começa a endireitar a toga com a outra mao. |
| F4-05 | `gilmar_post_fight_idle`  | NOVO IDLE POS-BRIGA (permanente ate fim da fase): toga rasgada e remendada (amarrada com no), oculos tortos com lente rachada, mancha de pastel no ombro, cabelo desgrenhado, MAS -- o sorrisinho cinico VOLTOU. Mais cinico que nunca. Papada voltou a tremer normalmente. O Gilmar ja esta se divertindo com a MEMORIA da briga. |
| F4-06 | `gilmar_post_fight_taunt` | Opcional: Gilmar olha na direcao onde o Barroso esta e faz "tsc tsc tsc" com o dedo (gesto de repreensao debochada). Papada balanca com o gesto. |

**BARROSO -- Pos-Briga (6 frames, 64x64px):**

| Frame | Nome                       | Descricao Detalhada                                                                                        |
|-------|----------------------------|------------------------------------------------------------------------------------------------------------|
| F4-01 | `barroso_ground`           | Barroso estatelado no chao, de brucos. Toga COMPLETAMENTE destruida: rasgada em 3 lugares, mancha de pastel amarelo-gordurosa no ombro e cabelo, vincos permanentes. Cabelo PELA PRIMEIRA VEZ completamente desalinhado -- mechas pra todos os lados. Oculos a 16px do rosto, lente quebrada. Martelo a 48px, rolou pra longe. Veia da testa AINDA pulsando mesmo no chao. Expressao: derrota existencial. |
| F4-02 | `barroso_getup_slow`       | Levantando com a dignidade de um homem que perdeu toda dignidade. Movimentos LENTOS, doloridos. Mao no joelho, empurrando pra cima. Toga penduricalha. Cabelo impossivel. Ao levantar, descobre mancha de pastel no ombro -- expressao de HORROR ao ver a toga suja. |
| F4-03 | `barroso_fix_hair_fail`    | De pe, PRIMEIRA COISA que faz: tenta arrumar o cabelo. Mao passa pelo cabelo grisalho. O cabelo NAO OBEDECE. Fica pior. Mecha espetada pra cima. Expressao de panico VERDADEIRO (Barroso se preocupa mais com o cabelo do que com a briga). Veia pulsa em panico capilar. |
| F4-04 | `barroso_fix_toga_fail`    | Tenta arrumar a toga. Puxa de um lado, rasga do outro. Desiste. Olha pros proprios bracos com desgosto. Pastel escorrendo do ombro. Oculos colocados no rosto mas completamente tortos (uma lente mais alta que a outra). |
| F4-05 | `barroso_post_fight_idle`  | NOVO IDLE POS-BRIGA (permanente ate fim da fase): toga rasgada e suja de pastel, cabelo desalinhado (3-4 mechas fora do lugar), oculos tortos com lente rachada, postura TENTANDO ser ereta mas falhando (leve curvatura de exaustao). Veia pulsando em ritmo CANSADO (mais lento que normal). Expressao: FURIA CONTIDA misturada com HUMILHACAO. O "adulto na sala" virou o palhaco do circo. |
| F4-06 | `barroso_post_fight_glare` | Opcional: Barroso olha na direcao do Gilmar com olhar ASSASSINO. Mas a toga rasgada, o cabelo bagunçado e o pastel no ombro tornam o olhar assassino... comico. Veia PULSA uma vez com forca, depois para. Ele desiste de manter a raiva. |

---

# 3. EFEITOS VISUAIS DETALHADOS

## 3.1 Baloes de Fala e Texto

### Sistema de Baloes

| Propriedade       | Valor                                                |
|--------------------|------------------------------------------------------|
| Estilo             | Balao de HQ grotesco -- bordas irregulares, NAO lisas |
| Borda              | 2px, preta (#000000), com tremor de 1px (jitter)     |
| Rabinho            | Aponta pro personagem, TREMENDO quando gritando       |
| Fonte              | Pixel art custom -- grotesca, irregular, como escrita de louco |
| Animacao de texto  | Typewriter (letra por letra) para falas normais       |
| Animacao de grito  | EXPLODE inteiro de uma vez, com camera shake           |
| Duracao            | 1.5s para falas normais, 1.0s para gritos             |
| Layer              | Acima de TUDO (depth 9999)                            |

### Texto Overlay "BRIGA NO STF!"

| Propriedade   | Valor                                                    |
|---------------|----------------------------------------------------------|
| Tamanho       | 256x48px                                                  |
| Posicao       | Centro-topo da tela                                       |
| Fonte         | Pixel ULTRA BOLD, estilo "ROUND 1 -- FIGHT!"             |
| Cor texto     | #FF0000 com borda #FFD700 (vermelho com ouro)             |
| Cor fundo     | Semi-transparente #000000 alpha 60%                       |
| Animacao IN   | Zoom de 2.0x pra 1.0x em 300ms, com bounce               |
| Animacao OUT  | Fade out em 500ms no segundo 10                           |
| Efeito extra  | Texto TREME (1px jitter) durante toda a briga             |
| Sub-texto     | "Round [N]" se nao for a primeira briga (cooldown)        |

### Simbolos Censurados

Quando ambos gritam simultaneamente (Fase 2, final e Fase 3), os baloes de fala contem:

```
@#$%&*!  @#$%!  #$%&@!  *#@$%!
```

- Cada simbolo e um sprite de 4x4px com cor aleatoria entre: #FF0000, #FF6600, #FFD700, #00BFFF, #FF00FF
- Simbolos GIRAM dentro do balao (rotacao de 30 graus/frame)
- Alguns ESCAPAM do balao e flutuam pra cima como bolhas de raiva

## 3.2 Efeitos nos Personagens

### Pastel Voador (Projetil Especial)

| Propriedade      | Valor                                                |
|-------------------|------------------------------------------------------|
| Sprite            | 16x16px, pastel grotesco do Andre Guedes             |
| Cor massa         | #E8C864 (dourado gorduroso)                          |
| Cor recheio       | #8B4513 (marrom carne moida, visivel nos cantos)     |
| Cor oleo          | #DAA520 (dourado translucido, trilha atras)          |
| Animacao de voo   | Rotacao de 45 graus/frame, arco parabolico           |
| Trilha            | 3-4 gotas de oleo atras (particulas 2x2px, fade 200ms)|
| Impacto           | SPLAT: explosao radial de 24px de massa e oleo        |
| Sujo permanente   | Deixa mancha no personagem atingido (sprite overlay)  |

### Embasamento dos Oculos do Barroso

| Fase   | Nivel     | Descricao Visual                                              |
|--------|-----------|---------------------------------------------------------------|
| Fase 1 | 0-20%     | Lentes normais (#E8E8F0), leve brilho de reflexo              |
| Fase 1 | 20-50%    | Bordas das lentes ficam opacas (#C0C0D0), centro ainda visivel|
| Fase 2 | 50-80%    | Lentes quase totalmente opacas, olhos DESAPARECEM atras       |
| Fase 2 | 80-100%   | Completamente embasados, VAPOR sai de cima dos oculos (2px)   |
| Fase 3 | QUEBRADO  | Uma lente racha (linha diagonal), outra cai. Armacao entorta. |

### Veia da Testa do Barroso -- Evolucao

| Fase   | Largura | Cor        | Comportamento                                            |
|--------|---------|------------|-----------------------------------------------------------|
| Fase 1 | 1-4px   | #8B2252    | Pulsa lentamente (1 ciclo/segundo)                        |
| Fase 2 | 4-7px   | #CC1144    | Pulsa RAPIDO (3 ciclos/segundo), CRESCE visivelmente      |
| Fase 3 | 7-10px  | #FF0000    | STROBOSCOPE: pisca entre visivel e invisivel a 6hz         |
| Fase 4 | 5-6px   | #8B2252    | Pulsa LENTO, cansado, como coracao desacelerando          |

### Papada do Gilmar -- Fisica de Gelatina

| Acao                  | Comportamento da Papada                                              |
|-----------------------|----------------------------------------------------------------------|
| Parado                | Treme levemente a cada 2 frames (1px oscilacao vertical)             |
| Rindo                 | BALANCA violentamente: 3px oscilacao lateral, delay de 2 frames      |
| Gritando              | VIBRA como motor: blur de 1px, tremor de alta frequencia             |
| Empurrando            | Projeta pra frente 2px com o corpo, depois BOING volta               |
| Sendo empurrado       | Vai pra frente (inércia) enquanto corpo vai pra tras -- efeito comico |
| No chao               | ESCORRE pro lado como massa. Deforma. Grotesco.                      |
| Pos-briga             | Voltou ao normal mas com micro-tremor de exaustao                     |

### Oculos do Gilmar Voando

| Propriedade   | Valor                                                       |
|---------------|--------------------------------------------------------------|
| Trigger       | Frame F2-07 (`gilmar_vagabundo_3`)                           |
| Sprite        | 12x8px, oculos anos 70 enormes, armacao grossa               |
| Animacao      | Saem do rosto em arco, giram 360 graus durante o arco        |
| Ponto mais alto| 16px acima da cabeca do Gilmar                               |
| Pouso         | Caem no chao com BOUNCE (2 quiques antes de parar)           |
| Reflexo       | Flash de brilho na lente a cada 90 graus de rotacao          |
| Reutilizacao  | Gilmar os recolhe na Fase 4                                   |

## 3.3 Efeitos de Camera e Tela

### Camera Shake

| Momento                  | Intensidade | Duracao | Tipo                        |
|--------------------------|-------------|---------|------------------------------|
| "VAGABUNDO!" (1o)        | 3px         | 200ms   | Random X+Y                   |
| "VAGABUNDO!!" (2o)       | 5px         | 300ms   | Random X+Y, mais intenso     |
| "VAGABUNDO!!!" (3o)      | 8px         | 500ms   | Random X+Y + zoom pulse 1.05x|
| Empurrao                 | 2px         | 150ms   | Direcional (direcao do push) |
| Pastel na cara           | 4px         | 250ms   | Random X+Y                   |
| Martelo na canela        | 6px         | 300ms   | Vertical (bounce)            |
| Nuvem de briga           | 2px constante| 2500ms | Tremor continuo sutil        |

### Flash de Tela

| Momento                  | Cor         | Duracao | Alpha   |
|--------------------------|-------------|---------|---------|
| Deteccao inicial         | #FFFFFF     | 100ms   | 40%     |
| "VAGABUNDO!!!" (3o)      | #FF0000     | 150ms   | 30%     |
| Pastel na cara           | #FFD700     | 100ms   | 25%     |

## 3.4 NPCs Espectadores (Opcional)

Quando a briga comeca, 4-6 mini-NPCs (32x32px) aparecem nas bordas da tela para ASSISTIR.

| NPC              | Sprite    | Comportamento                                          |
|------------------|-----------|--------------------------------------------------------|
| Assessor 1       | 32x32px   | Segura celular filmando. "Gravando!" acima da cabeca.  |
| Assessor 2       | 32x32px   | Esconde atras de pilastra, espia um olho.              |
| Jornalista       | 32x32px   | Microfone estendido, suando, tentando se aproximar.    |
| Seguranca do STF | 32x32px   | De bracos cruzados, olhando pro outro lado (se recusa a intervir). |
| Toffoli          | 32x32px   | Sentado numa cadeira de praia comendo pipoca. NAO SE ENVOLVE. |
| Xandao (cameo)   | 32x32px   | Aparece por 1 segundo com martelo, olha, balanca a cabeca, vai embora. |

---

# 4. ESPECIFICACAO DE AUDIO

## 4.1 Timeline Completa de Audio

| Tempo (ms) | Canal: Voz                            | Canal: SFX                             | Canal: Musica                        |
|------------|---------------------------------------|----------------------------------------|---------------------------------------|
| 0          | --                                    | `sfx_tension_sting` (impacto orquestral)| Musica de fase PARA abruptamente      |
| 200        | --                                    | `sfx_dramatic_whoosh`                   | --                                    |
| 500        | --                                    | `sfx_crowd_gasp` (sutil)               | `bgm_circus_stf` comeca (pianissimo)  |
| 1500       | `vo_gilmar_heh` (risadinha)           | --                                      | Musica sobe levemente                 |
| 2000       | `vo_barroso_horrivel` (fala completa) | --                                      | Musica tensa, circo sombrio           |
| 2500       | --                                    | --                                      | Crescendo                             |
| 3000       | `vo_barroso_psicopatia` (final frase) | `sfx_glass_crack` (oculos embasando)    | --                                    |
| 3500       | `vo_gilmar_vagabundo_1`               | `sfx_impact_heavy`                      | Musica: primeiro impacto de pratos    |
| 4000       | `vo_gilmar_vagabundo_2`               | `sfx_impact_heavier` + camera shake     | Musica: segundo impacto, mais forte   |
| 4500       | `vo_gilmar_vagabundo_3`               | `sfx_explosion_comic` + screen flash    | Musica: CLIMAX de pratos e tuba       |
| 4700       | `vo_barroso_argumento` (contra-ataque)| --                                      | Musica: breve silencio                |
| 5000       | `vo_both_grunts` (esforco fisico)     | `sfx_push_heavy`                        | `bgm_circus_stf` volta FORTE (forte) |
| 5500       | `vo_gilmar_grunt`                     | `sfx_fabric_rip` (toga rasgando)        | Musica: gallop comico                 |
| 6000       | --                                    | `sfx_fabric_tear` + `sfx_pastel_drop`   | --                                    |
| 6500       | `vo_gilmar_haha` (risada de arremesso)| `sfx_whoosh_pastel`                     | Musica: pausa comica (1 segundo)      |
| 7000       | `vo_barroso_aaagh` (pastel na cara)   | `sfx_splat_wet` + `sfx_glasses_break`   | Musica: BUM! Prato de orquestra       |
| 7500       | `vo_gilmar_ouch` (martelo na canela)  | `sfx_bonk_wood` + `sfx_comic_stars`     | Musica: trombone descendente (wah wah)|
| 7800       | `vo_both_scramble` (briga emaranhada) | `sfx_dustcloud_loop` (2 segundos)       | Musica: polca acelerada               |
| 9000       | `vo_both_panting` (ofegantes)         | `sfx_dustcloud_dissipate`               | Musica: desacelera, desafina          |
| 9500       | `vo_gilmar_tsc` (deboche)             | `sfx_glasses_place` (oculos no rosto)   | Musica: ultima nota de tuba, morre    |
| 10000      | --                                    | `sfx_fight_end_sting`                   | Musica de fase RETORNA gradualmente   |

## 4.2 Descricao dos Sons

### Vozes (sintetizadas ou gravadas em estilo caricato)

| Key                          | Descricao                                                                 | Duracao  |
|------------------------------|---------------------------------------------------------------------------|----------|
| `vo_gilmar_heh`              | Risadinha curta, nasal, debochada. "Heh heh heh." Tom de velhinho maligno.| 800ms    |
| `vo_barroso_horrivel`        | "Voce e uma pessoa HORRIVEL!" Voz tensa, crescendo, quebrando no final.  | 2000ms   |
| `vo_barroso_psicopatia`      | "...pitadas de psicopatia!" Cuspido. Voz tremendo de raiva.               | 1200ms   |
| `vo_gilmar_vagabundo_1`      | "VAGABUNDO!" Grito curto, seco, explosivo. Voz grossa de velhinho furioso.| 600ms    |
| `vo_gilmar_vagabundo_2`      | "VAGABUNDO!!" Mais alto, mais longo, mais raivoso. Eco sutil.             | 800ms    |
| `vo_gilmar_vagabundo_3`      | "VAGABUNDO!!!" APOCALIPTICO. Distorcao leve. Reverb. PARECE que o STF tremeu. | 1000ms |
| `vo_barroso_argumento`       | "Nao consegue articular um argumento!" Rapido, atropelado, desesperado.   | 1500ms   |
| `vo_gilmar_haha`             | Gargalhada maligna de quem esta se divertindo DEMAIS.                     | 600ms    |
| `vo_barroso_aaagh`           | Grito de nojo/surpresa ao receber pastel na cara. "AAARGH!"              | 500ms    |
| `vo_gilmar_ouch`             | "AI!" de dor exagerada, operatica, de quem apanha pela primeira vez.      | 400ms    |
| `vo_both_grunts`             | Grunhidos de esforco fisico sobrepostos. Bufando. Empurrando.             | Loop 500ms |
| `vo_both_scramble`           | Barulho de briga: grunhidos, gemidos, xingamentos abafados, tapa.         | Loop 500ms |
| `vo_both_panting`            | Ofegando. Exaustos. Respiracao pesada de dois homens idosos apos briga.   | 2000ms   |
| `vo_gilmar_tsc`              | "Tsc tsc tsc." Deboche. Provocacao final.                                 | 600ms    |

### Efeitos Sonoros

| Key                     | Descricao                                                           | Duracao |
|-------------------------|---------------------------------------------------------------------|---------|
| `sfx_tension_sting`     | Acorde orquestral de suspense. Tipo filme de Hitchcock versao forro.| 500ms   |
| `sfx_dramatic_whoosh`   | Whoosh cinematico. Acompanha o zoom-out da camera.                  | 400ms   |
| `sfx_crowd_gasp`        | Suspiro coletivo de surpresa ("ooooh!"). 4-5 vozes.                 | 600ms   |
| `sfx_glass_crack`       | Estalo de vidro rachando. Sutil. Sinistro.                          | 200ms   |
| `sfx_impact_heavy`      | Impacto grave de corpo contra corpo. Peso. Massa.                   | 300ms   |
| `sfx_impact_heavier`    | Mesmo que acima, mais grave, mais alto, com reverb.                 | 400ms   |
| `sfx_explosion_comic`   | Explosao COMICA, nao realista. Estilo Looney Tunes. Cartunesca.     | 500ms   |
| `sfx_push_heavy`        | Som de empurrao: roupa arrastando, corpo deslocando ar.             | 300ms   |
| `sfx_fabric_rip`        | Tecido rasgando. Puxao rapido. RIIIIIP.                             | 400ms   |
| `sfx_fabric_tear`       | Continuacao do rasgao. Mais lento, como pedaco se separando.        | 500ms   |
| `sfx_pastel_drop`       | Pastel caindo: som molhado e gordo de massa caindo no chao.         | 200ms   |
| `sfx_whoosh_pastel`     | Pastel cortando o ar. Mais molhado que um whoosh normal.            | 300ms   |
| `sfx_splat_wet`         | SPLAT ENORME. Molhado, gorduroso, nauseante. O som do pastel na cara.| 400ms  |
| `sfx_glasses_break`     | Oculos quebrando: estalo de armacao + tinido de lente rachando.     | 300ms   |
| `sfx_bonk_wood`         | BONK! Madeira (martelo) contra osso (canela). Cartunesco, oco.      | 250ms   |
| `sfx_comic_stars`       | Tinido magico de estrelinhas girando. Brilhante, comico.            | 600ms   |
| `sfx_dustcloud_loop`    | Barulho continuo de pancadaria generica: tapas, socos, grunhidos.   | Loop    |
| `sfx_dustcloud_dissipate`| Poeira assentando. Vento suave. Fim.                                | 800ms   |
| `sfx_glasses_place`     | Oculos sendo colocados no rosto. Click sutil de armacao.            | 150ms   |
| `sfx_fight_end_sting`   | Nota final comica. Tuba tocando "wah wah waaah". Fim da piada.     | 1000ms  |

## 4.3 Musica de Fundo: `bgm_circus_stf`

### Conceito Musical

**"Circo do Supremo"** -- Uma composicao original que mistura:
- **Marcha de circo** (entrada de palhacos) como base ritmica
- **Samba de breque** nos momentos de pausa comica
- **Musica de tribunal dramatica** (orgao) nos momentos de gritaria
- **Polca acelerada** na fase de briga fisica

### Estrutura

| Trecho (tempo) | Estilo                    | Instrumentacao                              | BPM  | Intensidade |
|-----------------|---------------------------|---------------------------------------------|------|-------------|
| 0-2s            | Suspense comico           | Orgao solitario + pratos sutis              | 80   | Pianissimo  |
| 2-3.5s          | Tribunal dramatico        | Orgao + cordas tensas + tuba ameacadora     | 100  | Mezzo-forte |
| 3.5-5s          | CAOS orquestral           | Tudo junto + pratos + bumbo + grito de tuba | 140  | FORTISSIMO  |
| 5-8s            | Polca/gallop de circo     | Acordeao + tuba + caixa + apito de circo    | 160  | Forte       |
| 8-9.5s          | Desacelerando             | Tuba solo, desafinando, notas erradas       | 100->60 | Diminuendo |
| 9.5-10s         | Nota final                | Tuba: "wah wah waaaaah" (derrota comica)    | --   | Piano       |

### Alternativa: Versao Samba

Se o tom de circo nao funcionar, alternativa com **samba**:

- Base de surdo e tamborim
- Cavaquinho fazendo a melodia comica
- Nos gritos de "VAGABUNDO!", o surdo bate FORTE (sincronizado)
- Na briga fisica, batucada acelerada como escola de samba em desfile
- No final, pandeiro solo desacelerando ate parar
- Referencia: a briga REAL virou samba -- a musica feita por internautas em 2018

---

# 5. IMPACTO NA GAMEPLAY

## 5.1 Dano Mutuo

| Acao durante a briga              | Dano no Gilmar | Dano no Barroso | Notas                            |
|------------------------------------|----------------|-----------------|-----------------------------------|
| Empurrao (F3-01)                   | 0              | 5% HP           | Gilmar e mais pesado              |
| Puxao de toga (F3-02/03)           | 3% HP          | 2% HP           | Ambos se machucam                 |
| Pastel na cara (F3-04/05)         | 0              | 8% HP           | Dano + humilhacao                 |
| Martelo na canela (F3-06)         | 10% HP         | 0               | O martelo do Barroso doi          |
| Nuvem de briga (F3-07/08)         | 12% HP         | 12% HP          | Ambos apanham igual               |
| **TOTAL por briga**               | **~25% HP**    | **~27% HP**     | Barroso leva levemente mais       |

**Resultado pos-briga:** Ambos ficam com 50% do HP que tinham ao INICIAR a briga (o dano mutuo mais o ajuste automatico garantem isso).

## 5.2 Intervencao do Jogador

| Acao do jogador           | Efeito                                                    |
|---------------------------|-----------------------------------------------------------|
| Atacar Gilmar durante     | Dano NORMAL. Gilmar nao reage (focado no Barroso).        |
| Atacar Barroso durante    | Dano NORMAL. Barroso nao reage (focado no Gilmar).        |
| Usar projetil durante     | Dano normal. Pode acertar qualquer um dos dois.           |
| Ficar parado assistindo   | NAO ganha XP/recompensa extra, mas ambos ficam fracos.    |
| Matar um durante a briga  | O outro FAZ POSE DE VITÓRIA por 2s, depois ataca jogador. |
| Matar AMBOS durante       | ACHIEVEMENT: "Juiz da Briga" -- recompensa especial.      |

## 5.3 Debuff Pos-Briga: `HUMILHADO`

| Parametro        | Valor                                              |
|-------------------|----------------------------------------------------|
| Duracao           | 5 segundos apos o fim da briga                     |
| Velocidade        | -30% de move speed para ambos                      |
| Dano de ataque    | -20% de dano para ambos                            |
| Visual            | Sprite pos-briga (toga rasgada, oculos tortos)     |
| Icone de debuff   | Toga rasgada vermelha (8x8px) acima da cabeca       |
| Remocao           | Automatica apos 5 segundos. Sprite volta ao normal.|

## 5.4 Cooldown e Repeticao

| Parametro                    | Valor                                          |
|-------------------------------|------------------------------------------------|
| Cooldown entre brigas         | 60 segundos (1 minuto real)                    |
| Maximo de brigas por fase     | 3 (se ambos sobreviverem)                      |
| Escalonamento                 | Cada briga subsequente e 15% mais rapida       |
| Dialogo muda?                 | SIM -- segunda briga tem xingamentos diferentes |
| Terceira briga                | CAOS TOTAL -- pula direto pra Fase 3 (briga fisica) |

### Dialogos Alternativos (Segunda Briga)

| Personagem | Fala                                                    |
|------------|----------------------------------------------------------|
| Barroso    | "De NOVO voce?! Eu nao acredito!"                        |
| Gilmar     | "Sentiu saudade, VAGABUNDO?"                              |
| Barroso    | "Vossa Excelencia e um DESASTRE ambulante!"               |
| Gilmar     | "Pelo menos eu sei fritar um pastel, seu INUTIL!"         |

### Dialogos Alternativos (Terceira Briga)

Nenhum dialogo. Ambos se olham. Silencio de 0.5 segundo. Partem pra briga IMEDIATAMENTE. Nuvem de poeira em 1 segundo. A raiva ja e AUTOMATICA.

## 5.5 Conquistas Relacionadas

| Achievement               | Condicao                                     | Icone          | Descricao                              |
|---------------------------|----------------------------------------------|----------------|----------------------------------------|
| "Juiz da Briga"          | Matar ambos durante a briga                   | Martelo dourado | "Sessao encerrada. Definitivamente."   |
| "Espectador VIP"         | Assistir 3 brigas sem interferir               | Pipoca         | "Melhor que BBB."                      |
| "Oportunista"            | Matar um boss durante a briga, com 1 hit       | Faca nas costas| "Aproveitou o momento."                |
| "Diplomata"              | Completar fase sem que a briga aconteca        | Pomba branca   | "Como? Eles estavam no MESMO mapa!"    |
| "Causa Mortis: Pastel"   | Barroso morre pelo dano do pastel na briga     | Pastel         | "Gordura trans. Literalmente."         |
| "Vagabundo x3"           | Ouvir os 3 "VAGABUNDO!" em todas as 3 brigas  | Megafone       | "9 vagabundos. Novo recorde."          |

---

# 6. ESPECIFICACAO TECNICA (PHASER 3)

## 6.1 Sprite Sheets

### Sheet Principal -- Sprites Individuais

| Sprite Sheet           | Tamanho Total | Frames | Frame Size | FPS  |
|------------------------|---------------|--------|------------|------|
| `gilmar_briga_fase1`   | 384x64px      | 6      | 64x64px    | 8    |
| `gilmar_briga_fase2`   | 512x64px      | 8      | 64x64px    | 10   |
| `gilmar_briga_fase4`   | 384x64px      | 6      | 64x64px    | 8    |
| `barroso_briga_fase1`  | 384x64px      | 6      | 64x64px    | 8    |
| `barroso_briga_fase2`  | 512x64px      | 8      | 64x64px    | 10   |
| `barroso_briga_fase4`  | 384x64px      | 6      | 64x64px    | 8    |

### Sheet Especial -- Sprites de Interacao (Fase 3)

| Sprite Sheet           | Tamanho Total | Frames | Frame Size | FPS  |
|------------------------|---------------|--------|------------|------|
| `briga_interacao`      | 1024x64px     | 8      | 128x64px   | 10   |

### Sprites Avulsos

| Sprite              | Tamanho  | Uso                                      |
|---------------------|----------|-------------------------------------------|
| `pastel_projetil`   | 16x16px  | Pastel voando                             |
| `oculos_gilmar_fly` | 12x8px   | Oculos do Gilmar voando                   |
| `oculos_barroso_break` | 12x8px | Oculos do Barroso quebrando              |
| `martelo_fly`       | 10x14px  | Martelo do Barroso voando                 |
| `toga_pedaco`       | 8x12px   | Pedaco de toga rasgada                    |
| `balao_fala`        | Variavel | Baloes de dialogo (ver secao 3.1)         |
| `overlay_briga_stf` | 256x48px | Texto "BRIGA NO STF!"                    |
| `npc_espectador`    | 32x32px  | NPCs que assistem (6 variantes)           |

## 6.2 Implementacao Phaser 3

### Carregamento

```javascript
// Sprite sheets individuais
this.load.spritesheet('gilmar_briga_f1', 'assets/personagens/gilmar/sprites/briga_fase1.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('gilmar_briga_f2', 'assets/personagens/gilmar/sprites/briga_fase2.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('gilmar_briga_f4', 'assets/personagens/gilmar/sprites/briga_fase4.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('barroso_briga_f1', 'assets/personagens/barroso/sprites/briga_fase1.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('barroso_briga_f2', 'assets/personagens/barroso/sprites/briga_fase2.png', {
    frameWidth: 64, frameHeight: 64
});
this.load.spritesheet('barroso_briga_f4', 'assets/personagens/barroso/sprites/briga_fase4.png', {
    frameWidth: 64, frameHeight: 64
});
// Interacao (ambos no mesmo sprite)
this.load.spritesheet('briga_interacao', 'assets/personagens/gilmar/sprites/briga_interacao.png', {
    frameWidth: 128, frameHeight: 64
});
// Projeteis e efeitos
this.load.image('pastel_projetil', 'assets/personagens/gilmar/sprites/pastel_projetil.png');
this.load.image('oculos_gilmar_fly', 'assets/personagens/gilmar/sprites/oculos_fly.png');
this.load.image('overlay_briga_stf', 'assets/ui/overlay_briga_stf.png');
```

### Animacoes

```javascript
// === FASE 1: DETECCAO ===
this.anims.create({
    key: 'gilmar_briga_detect',
    frames: this.anims.generateFrameNumbers('gilmar_briga_f1', { start: 0, end: 5 }),
    frameRate: 8,
    repeat: 0
});
this.anims.create({
    key: 'barroso_briga_detect',
    frames: this.anims.generateFrameNumbers('barroso_briga_f1', { start: 0, end: 5 }),
    frameRate: 8,
    repeat: 0
});

// === FASE 2: VERBAL ===
this.anims.create({
    key: 'gilmar_briga_verbal',
    frames: [
        { key: 'gilmar_briga_f2', frame: 0, duration: 500 },  // listen_smirk
        { key: 'gilmar_briga_f2', frame: 1, duration: 500 },  // listen_laugh
        { key: 'gilmar_briga_f2', frame: 2, duration: 500 },  // laugh_point
        { key: 'gilmar_briga_f2', frame: 3, duration: 300 },  // rage_transition
        { key: 'gilmar_briga_f2', frame: 4, duration: 400 },  // vagabundo_1
        { key: 'gilmar_briga_f2', frame: 5, duration: 400 },  // vagabundo_2
        { key: 'gilmar_briga_f2', frame: 6, duration: 500 },  // vagabundo_3
        { key: 'gilmar_briga_f2', frame: 7, duration: 400 }   // scream_sustain (loopavel)
    ],
    frameRate: 10,
    repeat: 0
});
this.anims.create({
    key: 'barroso_briga_verbal',
    frames: [
        { key: 'barroso_briga_f2', frame: 0, duration: 500 },  // accuse_start
        { key: 'barroso_briga_f2', frame: 1, duration: 500 },  // accuse_pessoa
        { key: 'barroso_briga_f2', frame: 2, duration: 500 },  // accuse_mistura
        { key: 'barroso_briga_f2', frame: 3, duration: 500 },  // accuse_psicopatia
        { key: 'barroso_briga_f2', frame: 4, duration: 400 },  // recoil_1
        { key: 'barroso_briga_f2', frame: 5, duration: 400 },  // recoil_2
        { key: 'barroso_briga_f2', frame: 6, duration: 400 },  // counter_yell
        { key: 'barroso_briga_f2', frame: 7, duration: 300 }   // scream_overlap
    ],
    frameRate: 10,
    repeat: 0
});

// === FASE 3: COMEDIA FISICA (interacao) ===
this.anims.create({
    key: 'briga_fisica',
    frames: [
        { key: 'briga_interacao', frame: 0, duration: 400 },  // push
        { key: 'briga_interacao', frame: 1, duration: 450 },  // toga_pull
        { key: 'briga_interacao', frame: 2, duration: 400 },  // toga_rip
        { key: 'briga_interacao', frame: 3, duration: 350 },  // pastel_throw
        { key: 'briga_interacao', frame: 4, duration: 450 },  // pastel_hit
        { key: 'briga_interacao', frame: 5, duration: 400 },  // martelo_canela
        { key: 'briga_interacao', frame: 6, duration: 350 },  // tangle
        { key: 'briga_interacao', frame: 7, duration: 700 }   // dustcloud (mais longo)
    ],
    frameRate: 10,
    repeat: 0
});

// === FASE 4: SEPARACAO ===
this.anims.create({
    key: 'gilmar_briga_pos',
    frames: this.anims.generateFrameNumbers('gilmar_briga_f4', { start: 0, end: 5 }),
    frameRate: 8,
    repeat: 0
});
this.anims.create({
    key: 'barroso_briga_pos',
    frames: this.anims.generateFrameNumbers('barroso_briga_f4', { start: 0, end: 5 }),
    frameRate: 8,
    repeat: 0
});
```

### Controller da Briga (Logica Principal)

```javascript
class BrigaGilmarBarroso {
    constructor(scene, gilmar, barroso) {
        this.scene = scene;
        this.gilmar = gilmar;
        this.barroso = barroso;
        this.isActive = false;
        this.cooldownTimer = 0;
        this.brigaCount = 0;
        this.COOLDOWN_MS = 60000;
        this.DETECTION_RADIUS = 128;
        this.BRIGA_DURATION = 10000;
    }

    update(time, delta) {
        if (this.isActive) return;
        if (this.cooldownTimer > 0) {
            this.cooldownTimer -= delta;
            return;
        }
        if (!this.gilmar.active || !this.barroso.active) return;

        const dist = Phaser.Math.Distance.Between(
            this.gilmar.x, this.gilmar.y,
            this.barroso.x, this.barroso.y
        );

        if (dist <= this.DETECTION_RADIUS) {
            this.iniciarBriga();
        }
    }

    iniciarBriga() {
        this.isActive = true;
        this.brigaCount++;

        // Salvar HP inicial
        this.gilmarHpInicial = this.gilmar.hp;
        this.barrosoHpInicial = this.barroso.hp;

        // Desabilitar aggro no jogador
        this.gilmar.setAggroTarget(null);
        this.barroso.setAggroTarget(null);

        // Pausar zumbis normais
        this.scene.events.emit('briga_stf_start');

        // Camera zoom out
        this.scene.cameras.main.zoomTo(0.83, 500); // 1/1.2

        // Overlay "BRIGA NO STF!"
        this.showOverlay();

        // Musica
        this.scene.sound.play('bgm_circus_stf', { volume: 0.3 });

        // Sequencia de fases
        if (this.brigaCount >= 3) {
            // Terceira briga: pula direto pra fase 3
            this.fase3(0);
        } else {
            this.fase1();
        }
    }

    fase1() {
        // Fase 1: Deteccao (0-2s)
        this.scene.sound.play('sfx_tension_sting');
        this.gilmar.play('gilmar_briga_detect');
        this.barroso.play('barroso_briga_detect');

        this.scene.time.delayedCall(2000, () => this.fase2());
    }

    fase2() {
        // Fase 2: Verbal (2-5s)
        this.gilmar.play('gilmar_briga_verbal');
        this.barroso.play('barroso_briga_verbal');

        // Baloes de fala sincronizados (ver timeline audio)
        this.showDialogos();

        this.scene.time.delayedCall(3000, () => this.fase3(3000));
    }

    fase3(offsetMs) {
        // Fase 3: Comedia fisica (5-8s)
        // Substituir sprites individuais por sprite de interacao
        const midX = (this.gilmar.x + this.barroso.x) / 2;
        const midY = (this.gilmar.y + this.barroso.y) / 2;

        this.gilmar.setVisible(false);
        this.barroso.setVisible(false);

        this.interacaoSprite = this.scene.add.sprite(midX, midY, 'briga_interacao');
        this.interacaoSprite.play('briga_fisica');

        // Aplicar dano mutuo
        this.aplicarDanoMutuo();

        const remainTime = 3000 - offsetMs;
        this.scene.time.delayedCall(Math.max(remainTime, 2000), () => this.fase4());
    }

    fase4() {
        // Fase 4: Separacao (8-10s)
        this.interacaoSprite.destroy();
        this.gilmar.setVisible(true);
        this.barroso.setVisible(true);

        // Separar fisicamente
        this.gilmar.x -= 64;
        this.barroso.x += 64;

        this.gilmar.play('gilmar_briga_pos');
        this.barroso.play('barroso_briga_pos');

        // Ajustar HP para 50% do inicial
        this.gilmar.hp = Math.floor(this.gilmarHpInicial * 0.5);
        this.barroso.hp = Math.floor(this.barrosoHpInicial * 0.5);

        // Aplicar debuff HUMILHADO
        this.gilmar.addDebuff('humilhado', 5000);
        this.barroso.addDebuff('humilhado', 5000);

        // Swap para sprites danificados
        this.gilmar.setPostFightSprite(true);
        this.barroso.setPostFightSprite(true);

        // Camera volta ao normal
        this.scene.cameras.main.zoomTo(1.0, 500);

        this.scene.time.delayedCall(2000, () => this.finalizarBriga());
    }

    finalizarBriga() {
        this.isActive = false;
        this.cooldownTimer = this.COOLDOWN_MS;

        // Remover overlay
        this.hideOverlay();

        // Retomar musica normal
        this.scene.sound.stopByKey('bgm_circus_stf');
        this.scene.sound.play('sfx_fight_end_sting');

        // Reativar aggro
        this.scene.events.emit('briga_stf_end');

        // Velocidade aumentada para brigas subsequentes
        // (15% mais rapida a cada vez)
    }

    aplicarDanoMutuo() {
        // Dano distribuido ao longo da Fase 3
        const danoGilmar = Math.floor(this.gilmar.maxHp * 0.25);
        const danoBarroso = Math.floor(this.barroso.maxHp * 0.27);

        // Aplicar gradualmente em 6 ticks
        let tickCount = 0;
        const danoTimer = this.scene.time.addEvent({
            delay: 500,
            callback: () => {
                this.gilmar.takeDamage(Math.floor(danoGilmar / 6));
                this.barroso.takeDamage(Math.floor(danoBarroso / 6));
                tickCount++;
                if (tickCount >= 6) danoTimer.remove();
            },
            repeat: 5
        });
    }
}
```

## 6.3 Layout no Atlas (2048x2048px)

Posicao sugerida para sprites da briga no atlas compartilhado:

| Asset                    | Posicao no Atlas | Tamanho Total    |
|--------------------------|------------------|-------------------|
| gilmar_briga_fase1       | (0, 1024)        | 384x64px          |
| gilmar_briga_fase2       | (384, 1024)      | 512x64px          |
| gilmar_briga_fase4       | (896, 1024)      | 384x64px          |
| barroso_briga_fase1      | (0, 1088)        | 384x64px          |
| barroso_briga_fase2      | (384, 1088)      | 512x64px          |
| barroso_briga_fase4      | (896, 1088)      | 384x64px          |
| briga_interacao (128w)   | (0, 1152)        | 1024x64px         |
| projeteis + efeitos      | (1024, 1152)     | 256x64px          |
| baloes de fala           | (0, 1216)        | 512x64px          |
| overlay BRIGA NO STF     | (512, 1216)      | 256x48px          |
| npcs espectadores        | (768, 1216)      | 192x32px          |

---

# 7. ART PROMPTS (Stable Diffusion / DALL-E)

## Estilo Base para TODOS os Prompts

```
Prefixo obrigatorio:
"underground comix style, grotesque political caricature, thick black ink outlines,
heavy crosshatching shadows, André Guedes cartoon style, pixel art 64x64,
Brazilian political satire, exaggerated proportions, jerky animation frame,
dirty saturated color palette, PNG transparency, top-down slight isometric view"
```

## Prompt 1: Deteccao -- Gilmar Reconhece o Barroso

```
underground comix style, grotesque political caricature, thick black ink outlines,
heavy crosshatching shadows, André Guedes cartoon style, pixel art 64x64,
Brazilian political satire, exaggerated proportions,

short old man in torn black judge robe with fried pastel grease stains,
enormous 1970s eyeglasses reflecting malicious light,
triple chin (papada) wobbling with anticipation,
cynical smirk forming on face like Cheshire cat,
one hand raised pointing accusingly,
short stubby body leaning forward aggressively,

discovering his nemesis across the battlefield,
expression transitioning from surprise to SADISTIC GLEE,
eyes narrowing behind huge glasses,
crumbs of pastel falling from robe pocket,

dirty yellow-brown-black color palette,
heavy shadows under chin folds,
pixel art sprite frame for 2D game,
transparent background PNG
```

## Prompt 2: Barroso Perdendo a Compostura

```
underground comix style, grotesque political caricature, thick black ink outlines,
heavy crosshatching shadows, André Guedes cartoon style, pixel art 64x64,
Brazilian political satire, exaggerated proportions,

tall thin man in perfectly pressed black judge robe that is starting to wrinkle,
silver-gray hair perfectly combed but ONE STRAND coming loose,
intellectual glasses fogging up from rage heat,
ENORMOUS THROBBING VEIN on forehead (bright red-purple),
face progressively turning red from collar upward,
mouth open wide shouting with academic fury,
index finger pointing in accusation trembling with rage,
small wooden gavel gripped white-knuckle tight in other hand,
sweat drops appearing on temples,

the composure of a professor CRUMBLING in real time,
toga starting to crease at shoulders,
controlled fury becoming UNCONTROLLED,

clean-to-dirty color transition palette,
heavy vein rendering with pulsing effect suggestion,
pixel art sprite frame for 2D game,
transparent background PNG
```

## Prompt 3: "VAGABUNDO!!!" -- O Grito Supremo do Gilmar

```
underground comix style, grotesque political caricature, thick black ink outlines,
heavy crosshatching shadows, André Guedes cartoon style, pixel art 64x64,
Brazilian political satire, exaggerated proportions,

short old man SCREAMING with mouth occupying HALF of the face,
1970s eyeglasses FLYING OFF the face in an arc,
triple chin VIBRATING like jelly in an earthquake creating motion blur,
entire body projected forward aggressively,
standing on tip-toes gaining extra height from rage,
black judge robe flapping open from force of scream,
visible sonic wave lines emanating from open mouth,
spit particles (2-3 droplets) flying forward,
neck veins bulging grotesquely,
fried pastel flying out of robe pocket from the force,

the ULTIMATE SCREAM of a man who has said the same word three times
each time louder, this being the THIRD and APOCALYPTIC version,

extreme red-purple face coloring,
maximum deformation and exaggeration,
pixel art sprite frame for 2D game,
transparent background PNG
```

## Prompt 4: Pastel na Cara do Barroso (SPLAT!)

```
underground comix style, grotesque political caricature, thick black ink outlines,
heavy crosshatching shadows, André Guedes cartoon style, pixel art 128x64,
Brazilian political satire, exaggerated proportions,

TWO CHARACTERS in same frame interaction sprite:

LEFT: short old man in torn judge robe, LAUGHING DEMONICALLY,
body bent forward from laughter, triple chin shaking,
broken glasses on face, expression of PURE JOY,

RIGHT: tall thin man just HIT IN THE FACE with a large fried PASTEL,
Brazilian fried pastry EXPLODED across face covering glasses and hair,
grease and meat filling dripping from previously immaculate silver hair,
glasses CRACKING from impact, one lens shattering,
judge robe now stained with yellow grease and brown meat filling,
expression of ABSOLUTE HORROR AND DISGUST visible through pastel debris,
formerly perfect appearance COMPLETELY DESTROYED,

splatter particles of pastel in all directions,
grease drops and crumbs flying,
the moment of maximum comedy in a fight between two supreme court judges,

grotesque food impact rendering,
dual character interaction frame,
pixel art sprite frame for 2D game,
transparent background PNG
```

## Prompt 5: Nuvem de Briga Classica (Dustcloud)

```
underground comix style, grotesque political caricature, thick black ink outlines,
heavy crosshatching shadows, André Guedes cartoon style, pixel art 128x64,
Brazilian political satire, slapstick comedy,

classic cartoon FIGHT DUST CLOUD in center of frame,
large oval cloud of dust and debris (96x64 pixels),
ARMS and LEGS sticking out of cloud at random angles,
some arms in judge robes (black), some with torn sleeves,
one pair of enormous 1970s GLASSES flying out of cloud,
one small wooden GAVEL flying out opposite side,
pieces of torn black ROBE floating around cloud,
a squashed PASTEL (Brazilian fried pastry) on the ground nearby,
broken GLASSES with cracked lenses below cloud,

COMIC ONOMATOPOEIA floating around cloud:
"POW!" in red, "SLAP!" in yellow, "CRACK!" in white, "@#$%!" in orange,

tiny IMPACT STARS (yellow) flashing inside cloud,
dust particles emanating from edges,

two supreme court judges in an undignified fistfight
reduced to a classic Looney Tunes style brawl,

slapstick comedy at maximum grotesque,
pixel art sprite frame for 2D game,
transparent background PNG
```

## Prompt 6: Pos-Briga -- Ambos Destruidos

```
underground comix style, grotesque political caricature, thick black ink outlines,
heavy crosshatching shadows, André Guedes cartoon style, pixel art 128x64,
Brazilian political satire, aftermath comedy,

TWO CHARACTERS standing apart after epic fight:

LEFT: short old man, judge robe TORN and tied with a knot,
one sleeve missing, shirt visible underneath with stains,
enormous 1970s glasses CROOKED with one cracked lens,
triple chin hanging exhausted but STILL SMIRKING,
pastel crumbs in hair, bruise suggestion on shin,
expression: CYNICAL SATISFACTION despite destruction,
"I had fun" energy radiating from damaged figure,

RIGHT: tall thin man, formerly impeccable judge robe now
TORN in three places with yellow grease stains,
silver gray hair COMPLETELY DISHEVELED for first time ever,
multiple strands sticking up in all directions,
intellectual glasses CROOKED one lens higher than other,
forehead vein STILL PULSING but slower from exhaustion,
dried pastel on shoulder and in hair,
expression: HUMILIATED FURY mixed with EXHAUSTION,
trying to maintain dignity with ZERO dignity remaining,

space between them suggesting recent violent separation,
debris on ground: pastel crumbs, robe pieces, glass shards,

the aftermath of the most undignified supreme court moment in history,

maximum character destruction while maintaining recognition,
pixel art sprite frame for 2D game,
transparent background PNG
```

## Prompt 7: Toffoli Comendo Pipoca (NPC Espectador)

```
underground comix style, grotesque political caricature, thick black ink outlines,
heavy crosshatching shadows, André Guedes cartoon style, pixel art 32x32,
Brazilian political satire, background comedy NPC,

small figure sitting in a beach chair wearing judge robe,
eating POPCORN from a large bucket with expression of entertainment,
watching something off-screen with amused expression,
legs crossed casually, zero concern about the chaos nearby,
small gavel resting on the ground next to chair unused,

the ultimate "not my problem" energy,
tiny background NPC sprite for crowd scene,

miniature character design,
pixel art sprite for 2D game,
transparent background PNG
```

---

# 8. RESUMO DE ASSETS NECESSARIOS

## Contagem Total

| Categoria                     | Quantidade | Formato           |
|-------------------------------|------------|-------------------|
| Sprites individuais Gilmar    | 18 frames  | 64x64px PNG       |
| Sprites individuais Barroso   | 18 frames  | 64x64px PNG       |
| Sprites interacao (ambos)     | 8 frames   | 128x64px PNG      |
| Sprites projeteis/objetos     | 6 sprites  | Variado PNG       |
| Sprites de baloes de fala     | 7 baloes   | Variado PNG       |
| Overlay de texto              | 1 sprite   | 256x48px PNG      |
| NPCs espectadores             | 6 sprites  | 32x32px PNG       |
| Efeitos de particulas         | 8 tipos    | 1-4px PNG         |
| Sons de voz                   | 14 clips   | OGG/MP3           |
| Efeitos sonoros               | 18 clips   | OGG/MP3           |
| Musica de fundo               | 1 track    | OGG/MP3 (10s loop)|
| **TOTAL de assets unicos**    | **~105**   |                   |

## Prioridade de Producao

| Prioridade | Assets                                    | Razao                                    |
|------------|-------------------------------------------|------------------------------------------|
| P0 (MVP)   | Sprites de interacao Fase 3 (8 frames)    | A parte mais ICONICA e reconhecivel       |
| P0 (MVP)   | Baloes "VAGABUNDO!" e "pessoa horrivel"   | As falas sao o CORE da piada              |
| P0 (MVP)   | Overlay "BRIGA NO STF!"                   | Feedback visual instantaneo pro jogador   |
| P0 (MVP)   | `sfx_splat_wet` + `sfx_bonk_wood`         | Os sons que fazem a comedia funcionar     |
| P1         | Sprites individuais Fase 2 (verbal)       | A escalada verbal e essencial pro ritmo   |
| P1         | Vozes sintetizadas dos dialogos            | As FRASES sao a alma da mecanica          |
| P1         | `bgm_circus_stf` (musica)                 | Define o tom comico de TODA a sequencia   |
| P2         | Sprites Fase 1 (deteccao)                 | Bom buildup mas pode ser simplificado     |
| P2         | Sprites Fase 4 (pos-briga)               | Pode reutilizar sprites danificados       |
| P2         | NPCs espectadores                          | Comedia extra, nao essencial              |
| P3         | Particulas avancadas                       | Nice-to-have, pode usar particulas genericas |
| P3         | Dialogos alternativos (2a/3a briga)       | Rejogabilidade, mas MVP funciona com 1 set |

---

# 9. NOTAS FINAIS DO DIRETOR DE ARTE

## O que FAZ essa cena funcionar

1. **O CONTRASTE**: Gilmar esta se DIVERTINDO. Barroso esta DESMORONANDO. O comico nasce do contraste entre o deboche cinico de um e a furia elegante do outro.

2. **A ESCALADA**: Comeca com olhares. Vira palavras. Vira gritos. Vira empurrao. Vira pastel na cara. Vira nuvem de poeira. Cada segundo deve ser MAIS absurdo que o anterior.

3. **AS FRASES REAIS**: "Voce e uma pessoa horrivel" e "VAGABUNDO!" nao sao inventadas. Foram ditas ao vivo, no plenario, com camera ligada. O jogador que conhece a referencia MORRE de rir. O que nao conhece ri assim mesmo porque e ABSURDO.

4. **O PASTEL**: O pastel na cara e o climax visual. Todo mundo lembra do pastel. E a marca registrada do Gilmar no jogo. USAR O PASTEL COMO ARMA contra o Barroso e o momento de ouro.

5. **A IRREVERSIBILIDADE VISUAL**: Apos a briga, ambos ficam VISIVELMENTE destruidos pelo resto da fase. O jogador VE as consequencias. A toga rasgada do Barroso, o oculos torto do Gilmar -- sao trofeus visuais da briga.

6. **O ANTICLÍMAX**: Apos toda a guerra epica, ambos levantam, se olham, e voltam a atacar o jogador como se nada tivesse acontecido. Exceto que ambos estao DESTRUIDOS e ENFRAQUECIDOS. A briga nao resolve nada. Como no STF real.

## O que NAO fazer

- NAO tornar a briga "seria" ou "dramatica". E COMEDIA. Sempre.
- NAO fazer animacao fluida. O jerky e o ESTILO. Dois frames onde um bastaria.
- NAO censurar os xingamentos. "VAGABUNDO!" e dito por inteiro. Os simbolos censurados (@#$%) sao so pra quando gritam AO MESMO TEMPO (porque ninguem entende nada mesmo).
- NAO fazer um vencedor claro. A briga e EMPATE. Ambos se destroem igualmente. Como na vida real.
- NAO esquecer que o jogador PODE atacar durante a briga. Isso e uma OPORTUNIDADE estrategica, nao so uma cutscene.

---

*"A briga entre Gilmar e Barroso e o momento em que o STF admitiu, ao vivo e em rede nacional, que aquilo tudo e um circo. E nos estamos transformando esse circo em GAMEPLAY."*

-- Diretor de Arte, Zumbis de Brasilia
