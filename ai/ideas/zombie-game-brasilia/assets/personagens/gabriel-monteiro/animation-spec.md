# GABRIEL MONTEIRO - Especificacao de Animacoes

## NPC do Limbo / Residente Permanente - "Zumbis de Brasilia"

---

## Parametros Globais de Animacao

| Parametro             | Valor                                                |
|-----------------------|------------------------------------------------------|
| Framerate base        | 8fps (jerky, twitchy)                                |
| Framerate acoes       | 10fps (Falsa Heroica -- mais rapido = mais comico)   |
| Framerate dissolve    | 6fps (lento, sombrio)                                |
| Estilo de movimento   | Arrastado, curvado, residuos de confianca que colapsam|
| Interpolacao          | NENHUMA -- snappy, frame a frame, sem tweening       |
| Deformacao organica   | Media no corpo, ALTA na sombra autonoma              |
| Easing                | Nao usar. Cortes secos entre frames                  |

---

## SISTEMA DE SOMBRA AUTONOMA (PERMANENTE)

Este e o sistema visual mais importante do personagem. A sombra e uma entidade SEMI-INDEPENDENTE.

### Especificacao Tecnica

| Parametro             | Valor                                               |
|-----------------------|-----------------------------------------------------|
| Tipo                  | Sprite separado, logica propria                     |
| Tamanho               | 120-130% do sprite principal                        |
| Cor                   | #1A0A1A (preto-roxo)                                |
| Opacidade             | 70-85%, variacao sinusoidal (periodo 3s)            |
| Delay de posicao      | 1-2 frames atras do corpo principal                 |
| Posicao (no Limbo)    | ATRAS do corpo (vertical, como fantasma erguido)    |
| Posicao (fora Limbo)  | No chao, achatada com skew, mas MAIOR               |

### Tabela de Comportamento por Estado

| Estado do corpo     | Comportamento da sombra                                  |
|--------------------|----------------------------------------------------------|
| IDLE (curvado)     | Ereta, ombros largos, bracos cruzados                    |
| WALK (arrastando)  | Andando com passada confiante (delay 1-2 frames)         |
| TALK (gesticulando)| Apontando agressivamente, punho cerrado                  |
| FALSA HEROICA      | SINCRONIZA com o corpo (unico momento). Ao tropecar, sombra continua correndo 1 frame extra |
| VIDEO ARMADO       | Sombra faz gesto de "para com isso" (envergonhada)       |
| HIT                | Sombra se AGITA (tremor, como se quisesse reagir)        |
| DISSOLVE           | Sombra e ULTIMA a desaparecer. Se contorce sozinha       |

### Animacao Propria da Sombra (Loop independente, 4 frames)

| Frame | Pose da sombra                                             |
|-------|-------------------------------------------------------------|
| 1     | Em pe, ereta, ombros largos. Bracos ao lado do corpo       |
| 2     | Bracos cruzados. Cabeca levemente inclinada (arrogancia)    |
| 3     | Mao direita apontando para frente (acusando/ameacando)      |
| 4     | Bracos flexionados (pose de forca) -- residuo de ex-policial|

### Interacao Sombra-Corpo (Momentos Especiais)
- **Quando Gabriel tenta endireitar os ombros**: Sombra PARA de se mover (como se percebesse)
- **Quando Gabriel tenta ser heroico**: Sombra COINCIDE por 2-3 frames, depois diverge
- **No Limbo profundo**: Sombra mais NITIDA que o proprio corpo (inversao)
- **Quando cracha pulsa**: Sombra estremece (como se sentisse dor)

---

## SISTEMA: Cracha "CANCELADO PERMANENTE" (PERMANENTE)

### Especificacao Tecnica

| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Posicao               | Centro do peito, 12px abaixo do pescoco            |
| Tamanho               | 16x6px                                             |
| Cor fundo             | #CC0000 (vermelho intenso)                         |
| Cor texto             | #FFFFFF (branco)                                   |
| Borda                 | 1px preta (#000000)                                |
| Pulso                 | A cada 16-20 frames, brilho vermelho +20% por 2 frames |
| Blend mode            | Normal (NAO additive -- e fisico, nao luz)         |
| Emissao de luz        | Sutil: 4px ao redor com #CC0000 a 15% opacidade    |

### Comportamento por Estado
- **IDLE**: Pulso regular, sutil
- **WALK**: Balanca com o corpo, pulso mantido
- **TALK**: Pulso INTENSIFICA quando Gabriel menciona o passado (frame 6 do talk)
- **FALSA HEROICA**: Pulso PARA durante a corrida (ele "esquece" que e cancelado), volta com forca DOBRADA apos o tropeço
- **VIDEO ARMADO**: Pulso constante e mais rapido (como heartbeat acelerado)
- **HIT**: Flash unico brilhante
- **DISSOLVE**: ULTIMO elemento a desaparecer. Brilho maximo antes de sumir

---

## SISTEMA: Cabelo Entropico (PERMANENTE)

### Especificacao Tecnica

| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Mechas visiveis       | 3-5 pixeis de cabelo saindo em direcoes diferentes |
| Mudanca entre estados | Mechas MUDAM de posicao aleatoriamente ao trocar animacao |
| Base                  | Formato de "corte militar que cresceu e desistiu"  |
| Gel residual          | 1-2 mechas ainda grudadas (brilho minimo), resto livre |
| Cor                   | #2A2010 (castanho escuro)                          |

### Regras
- NUNCA o cabelo esta igual em dois estados de animacao consecutivos
- Ao menos 1 mecha muda de posicao por transicao
- Na "Falsa Heroica", quando ele endireita: 1 frame de cabelo "quase arrumado" (gel ativa por memoria muscular), depois cai de novo
- No "Video Armado": tenta ajeitar com a mao (frame 7 do talk). Fica PIOR

---

## SISTEMA: Olheiras (PERMANENTE)

### Especificacao Tecnica

| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Cor                   | #4A3040 (roxo-escuro)                              |
| Tamanho               | 4x2px abaixo de cada olho                         |
| Profundidade          | No Limbo: mais escuras (#3A2030). Fora: padrao     |
| Variacao              | Nenhuma -- sempre presentes, nunca mudam            |

---

## ANIMACAO 1: IDLE

| Campo         | Valor                                |
|---------------|--------------------------------------|
| Frames        | 4                                    |
| FPS           | 8                                    |
| Loop          | Sim, infinito                        |
| Direcoes      | 4 (frente, costas, esquerda, direita)|

### Descricao Frame a Frame

**Frame 1 (base)**:
- Postura curvada, ombros caidos, cabeca levemente inclinada para frente
- Olhos abertos (arregados), olhando para frente sem foco
- Boca semi-aberta (entre palavras que nao saem)
- Cracha de CANCELADO visivel, brilho padrao
- Maos ao lado do corpo, leves, sem energia
- Sombra ATRAS: ereta, bracos cruzados (posicao 1 do loop da sombra)
- Camiseta pendurada, larga no torso

**Frame 2 (+125ms)**:
- Olhos se MOVEM para a esquerda (paranoia). Rapido, twitchy
- Cracha faz PULSO vermelho sutil (+20% brilho)
- Sombra: muda para posicao 2 (bracos cruzados, cabeca inclinada)
- Mecha de cabelo cai 1px para a direita
- Corpo: leve tremor (1px para baixo)

**Frame 3 (+250ms)**:
- Maos levantam levemente (gesto defensivo inconsciente -- palmas para frente, 3px acima da posicao de repouso)
- Ombros sobem 1px (encolhendo)
- Olhos voltam para frente, se arregalam mais 1px
- Sombra: muda para posicao 3 (apontando -- gesto agressivo que contrasta com o corpo defensivo)
- Cracha: brilho normal

**Frame 4 (+375ms)**:
- SUSPIRO: corpo inteiro desce 1px (exalacao), depois volta 1px
- Maos descem de volta ao repouso
- Ombros descem (relaxamento de derrota, nao de conforto)
- Olhos semi-fecham por 1 frame (micro-descanso)
- Sombra: muda para posicao 4 (flexionando), volta ao inicio

---

## ANIMACAO 2: WALK

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 6                              |
| FPS           | 8                              |
| Loop          | Sim, durante movimento         |
| Direcoes      | 4                              |

### Descricao Frame a Frame

**Frame 1**: Pe direito arrasta para frente (nao levanta, DESLIZA). Camiseta balanca para tras. Ombros curvados
**Frame 2**: Peso transfere. Tenta endireitar ombros (sobe 1px). Falha (desce 1px no frame seguinte). Cracha brilha. Sombra: andando confiante com delay
**Frame 3**: Pe esquerdo arrasta. Olhar para baixo (chao). Cabelo mexe com o ar. Mecha muda
**Frame 4**: FLASH de esperanca -- ergue a cabeca, olha para frente, ombros tentam subir. Sombra CRESCE 2px (mais ameaçadora). Dura UM frame
**Frame 5**: Cabeca desce de novo. Ombros caem. Desanimo visivel. Sombra volta ao tamanho normal
**Frame 6**: Completa ciclo. Arrastar continuo. Sombra "se acomoda" com delay final

### Notas de Timing
- A caminhada e 30% mais lenta que personagens normais (NPC do Limbo, sem pressa)
- O frame 4 (flash de esperanca) cria ritmo comico: up-DOWN, up-DOWN
- Sombra tem timing PROPRIO -- parece que "anda sozinha"
- Som: arrastar de pe, leve (nao pesado como zumbi -- ele nao e zumbi, e CANCELADO)

---

## ANIMACAO 3: TALK (Dialogo NPC)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 8                              |
| FPS           | 8                              |
| Loop          | Sim, durante dialogo ativo     |
| Direcoes      | 1 (frente -- vira para jogador)|

### Descricao Frame a Frame

**Frame 1 -- Encontro**:
- Vira para o jogador. Olhos arregalam MUITO (alguem esta falando com ele!)
- Boca abre (surpresa positiva). Corpo endireita um pouco
- Sombra: fica quieta, observando

**Frame 2 -- Animacao**:
- Mao direita levanta, gesticulando com energia
- Expressao animada (saudade de ter plateia)
- Sombra: bracos cruzados (desprezo)

**Frame 3 -- Auto-referencia**:
- APONTA PARA SI MESMO com AMBAS as maos (polegares no peito, ao redor do cracha)
- "EU ERA policial! EU ERA vereador! EU ERA YouTuber!"
- Momento de orgulho residual. Olhos brilham. Postura reta por 1 frame
- Sombra: COINCIDE (raro!) -- tambem aponta para si mesma

**Frame 4 -- Apresentador**:
- Maos abrem para os lados (gesto de YouTuber apresentando video)
- Queixo erguido, sorriso forcado (careta)
- Memoria muscular de "E AI GALERA". Camiseta estica
- Sombra: faz o mesmo gesto mas 2x maior (amplificado)

**Frame 5 -- Colapso**:
- Expressao muda BRUSCAMENTE para desculpa
- Ombros sobem defensivos. Maos na frente (palmas abertas)
- "Nao me olhem assim"
- Sombra: volta a cruzar bracos (desdenhosa)

**Frame 6 -- Paranoia**:
- Olhos disparam para esquerda, depois direita
- Cracha pulsa vermelho FORTE (mais que o normal)
- Corpo encolhe. Mao perto do cracha (tentando cobrir? Nao consegue)
- Sombra: tremula (agitada)

**Frame 7 -- Tentativa**:
- Tenta sorrir. Falha. Resultado e careta/grimace
- Mao vai ao cabelo (tentando arrumar). Resultado: PIOR
- Mecha extra sai do lugar
- Sombra: faz gesto de facepalm

**Frame 8 -- Desistencia**:
- Desiste. Ombros caem totalmente. Maos ao lado
- Suspiro visivel (corpo desce e sobe)
- Volta a postura curvada de idle
- Sombra: volta a posicao ereta silenciosa

---

## ANIMACAO 4: "Residente Permanente" (Aparicao no Limbo)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 8                              |
| FPS           | 6 (lento, atmosferico)         |
| Loop          | Nao, trigger quando jogador morre|
| Contexto      | Jogador acabou de morrer e chega ao Limbo |

### Descricao Frame a Frame

**Frame 1 -- Void**:
- Tela: void roxo-preto total. Nevoa rolando
- NO CENTRO: dois pontos brancos aparecem. Sao olhos. Arregados
- Nada mais visivel

**Frame 2 -- Olhos**:
- Olhos mais definidos. Olheiras visiveis ao redor
- Brilho vermelho MINIMO abaixo dos olhos (cracha, ainda fora de vista)
- Nevoa se move para os lados (algo se aproxima)

**Frame 3 -- Emergencia**:
- Silhueta emerge da nevoa. Ombros curvados. Camiseta larga
- Cracha de CANCELADO e a UNICA fonte de luz vermelha no void inteiro
- Sombra atras: ENORME, desproporcional, ameaçadora

**Frame 4 -- Aproximacao**:
- Mais detalhes visiveis. Cabelo caotico. Barba. Camiseta desbotada
- Caminha em direcao ao jogador (ponto de vista do jogador)
- Cada passo: cracha pulsa. Sombra segue com delay

**Frame 5 -- Parada**:
- Para na frente do jogador. Distancia de conversa
- Expressao: RECONHECIMENTO cansado. "Ah, voce tambem?"
- Olhos semi-cerram (nao surpresa -- ele VE MUITA GENTE chegar ao Limbo)

**Frame 6 -- Aceno**:
- Acena com a mao fraca (sem energia). Aceno de quem faz isso todo dia
- Meio sorriso triste (nao careta -- genuino)
- Sombra: repete o aceno com delay, mas com mais energia

**Frame 7 -- Boas vindas**:
- Gesto de "boas vindas" ironico -- bracos abrem como se mostrasse o Limbo
- Olha ao redor do void como se fosse sua "casa"
- Cracha pulsa forte

**Frame 8 -- Estabiliza**:
- Entra em idle. Pronto para dialogo
- Transicao para TALK loop se jogador interage
- Sombra se posiciona atras, silenciosa

---

## ANIMACAO 5: "Falsa Heroica" (Tentativa de Ajuda)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 10                             |
| FPS           | 10 (mais rapido = mais comico) |
| Loop          | Nao, evento scriptado          |
| Trigger       | Aleatorio durante gameplay no Limbo |

### Descricao Frame a Frame

**Frames 1-2 -- Determinacao**:
- Frame 1: Expressao MUDA completamente. Olhos focam. Maxilar cerra. A "memoria" de ser policial ATIVA
- Frame 2: Ombros endireitam DE VERDADE. Bate no peito (por cima do cracha -- ignora). Postura ERETA pela primeira vez
- Sombra: SINCRONIZA com o corpo (momento rarissimo. Por 1 instante, homem e sombra sao um so)
- Cracha: PARA de pulsar (esqueceu que e cancelado)

**Frames 3-4 -- Carga**:
- Frame 3: CORRE. Bracos bombando. Pernas levantando alto (nao mais arrastando). Camiseta estica no peito (residuo de musculatura)
- Frame 4: Continua correndo. Velocidade maxima. Sombra ACOMPANHA 1:1 (sincronia total)
- Visual: por estes 2 frames, ele PARECE o heroi que afirmava ser

**Frames 5-6 -- Desastre**:
- Frame 5: PE ENGANCHA no outro. Tropeça. Corpo inclina 45 graus para frente. Olhos arregalam (surpresa). Bracos tentam compensar
- Frame 6: FACEPLANT. Cai de boca no chao. Camiseta RASGA audível (1-2px de rasgo novo). Poeira levanta
- Sombra: CONTINUA correndo por 1 frame extra antes de TAMBEM cair (delay comico)

**Frames 7-8 -- Caos**:
- Frame 7: Rola no chao. Bracos e pernas espalhados. Acidentalmente chuta algo (item, inimigo, mobilia do Limbo)
- Frame 8: O que ele chutou vai na direcao ERRADA (empurra inimigo para PERTO do jogador, ou derruba item util para longe)
- Sombra: se levanta antes do corpo, cruzar bracos (envergonhada do corpo)

**Frames 9-10 -- Vergonha**:
- Frame 9: Levanta devagar. Poeira no corpo. Rasgo novo na camiseta visivel. Mao no joelho (doeu). Expressao de CULPA ABSOLUTA
- Frame 10: Maos abertas na frente (palmas expostas). "Desculpa! Eu tava tentando ajudar!" Ombros caem. Volta a postura curvada
- Cracha: VOLTA a pulsar com forca dobrada (realidade reafirmada)
- Sombra: dessincrona do corpo completamente. Volta a ser independente

---

## ANIMACAO 6: "Video Armado" (Finge Filmar)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 8                              |
| FPS           | 8                              |
| Loop          | Nao, evento scriptado          |
| Trigger       | Aleatorio quando algo "filmavel" acontece |

### Descricao Frame a Frame

**Frame 1 -- Impulso**:
- Algo acontece (explosao, NPC passa, situacao dramatica)
- Olhos de Gabriel BRILHAM (instinto YouTuber dispara)
- Mao vai ao bolso traseiro
- Sombra: faz gesto de "nao, para" (tentando impedir)

**Frame 2 -- Celular**:
- Tira celular ANTIGO do bolso. Tela rachada (3-4 linhas de rachadura visiveis). Modelo velho
- Segura com as duas maos. Postura ENDIREITA (apresentador mode)
- Expressao: concentracao + nostalgia

**Frame 3 -- REC**:
- Aponta celular para a cena. Indicador "REC" vermelho pisca no canto do celular
- Queixo ergue. SORRISO forcado aparece (nao natural -- musculo de youtuber)
- Postura de "apresentador de rua" -- pes afastados, corpo de frente para "camera"

**Frame 4 -- Performance**:
- No auge. Parece um YouTuber de verdade por 1 frame
- Boca aberta como se narrasse. Gesticulacao de "estamos aqui ao vivo"
- Sombra: COINCIDE brevemente (memoria do passado)
- Cracha: para de pulsar (esqueceu de novo)

**Frame 5 -- Realidade**:
- Olha para o celular. Tela nao tem views. Nao tem seguidores. Nao tem nada
- Sorriso COMECA a morrer (canto direito da boca desce)
- Celular treme na mao

**Frame 6 -- Colapso**:
- Sorriso MORREU. Expressao de tristeza genuina
- Celular abaixa lentamente
- Ombros comecam a cair
- Cracha: volta a pulsar MAIS FORTE (realidade se impoe)
- Sombra: faz gesto de "eu avisei"

**Frame 7 -- Guarda**:
- Guarda celular no bolso LENTAMENTE (cada pixel de guarda e deliberado)
- Cabeca abaixa
- Maos no bolso
- Momento de silencio visual (nenhum efeito -- pausa)

**Frame 8 -- Retorno**:
- Volta ao idle completo. Curvado. Olheiras mais visiveis por 1 frame
- Cracha pulsa no ritmo mais rapido das ultimas 3 animacoes
- Sombra: volta a posicao independente, ereta, bracos cruzados
- O celular ja esta guardado. O sonho de YouTuber tambem

---

## ANIMACAO 7: HIT/DAMAGE (Acidental)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 4                              |
| FPS           | 12 (rapido)                    |
| Loop          | Nao, single shot               |

### Sequencia

**Frame 1**: Flash ROXO (nao vermelho -- ele pertence ao Limbo, a cor do Limbo o atinge). Expressao de "DE NOVO?!"
**Frame 2**: Recuo EXAGERADO (4px para tras + 2px para cima). Bracos voam para os lados. Overreaction de YouTuber dramatico
**Frame 3**: Cracha de CANCELADO balanca violentamente. Sombra se AGITA (treme, expande 5%, contrai). Olhos arregalam ao maximo
**Frame 4**: Aterrissa. Maos abertas defensivas. "Ja estou no Limbo, que mais podem fazer?" Retorna ao estado anterior

---

## ANIMACAO 8: DISSOLVE/FADE (Saida do Limbo)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 8                              |
| FPS           | 6 (lento, sombrio)             |
| Loop          | Nao, single shot               |
| Contexto      | Quando jogador sai do Limbo (revive), Gabriel fica e dissolve |

### Descricao Frame a Frame

**Frame 1**: Olha o jogador indo embora. Expressao de solidao. Acena fraco. "Ate a proxima morte..."
**Frame 2**: Particulas roxas comecam a subir dos PES. O Limbo reabsorve ele. Pes ficam transparentes
**Frame 3**: Dissolucao chega as pernas. Particulas roxas subindo. Camiseta comeca a ficar transparente na base
**Frame 4**: Corpo 50% dissolvido. Torso se vai. Bracos transparentes. MAS o cracha de CANCELADO permanece SOLIDO e BRILHANTE
**Frame 5**: Corpo quase todo dissolvido. Restam: cabeca (parcial), cracha (100% solido), e SOMBRA (100% presente)
**Frame 6**: Cabeca se dissolve. Ultimos olhos arregados vistos antes de sumir. Cracha flutua sozinho, brilhando vermelho. Sombra permanece erguida, INTACTA
**Frame 7**: Cracha finalmente comeca a desaparecer. Brilho vermelho MAXIMO antes de sumir. Sombra se CONTORCE (gesticula sozinha, bracos se movem de forma agressiva)
**Frame 8**: Sombra SOZINHA por 1 frame final. Se dissolve em particulas roxas mais escuras. Ultimo frame: texto "CANCELADO PERMANENTE" flutuando no void, 1 frame, depois void puro

---

## Transicoes entre Animacoes

| De                   | Para             | Transicao                                        |
|---------------------|------------------|--------------------------------------------------|
| IDLE                | WALK             | Imediata. Sombra ajusta com delay 2 frames       |
| WALK                | IDLE             | 1 frame de "parada" (arrastar diminui)            |
| IDLE                | TALK             | 1 frame de "surpresa" (olhos arregalam mais)      |
| TALK                | IDLE             | Frame 8 do talk JA e transicao para idle          |
| IDLE                | RESIDENTE PERM.  | Trigger automatico. Nao transiciona -- SUBSTITUI  |
| RESIDENTE PERM.     | IDLE/TALK        | Frame 8 ja e idle. Se jogador interage -> TALK    |
| IDLE                | FALSA HEROICA    | 0 frames. Snap imediato (impulso subito)          |
| FALSA HEROICA       | IDLE             | Frame 10 ja e idle curvado                        |
| ANY                 | VIDEO ARMADO     | 1 frame de "olhos brilham" antes de comecar       |
| VIDEO ARMADO        | IDLE             | Frame 8 ja e idle                                 |
| ANY                 | HIT              | Interrompe QUALQUER animacao                      |
| HIT                 | (estado anterior)| Apos frame 4, volta ao que estava fazendo         |
| ANY                 | DISSOLVE         | Trigger de saida do Limbo. Interrumpe tudo        |

---

## Timing de Eventos Scriptados

### Quando o jogador MORRE pela primeira vez
1. Tela fade to roxo-preto (500ms)
2. Delay de 1 segundo (void puro)
3. Animacao "Residente Permanente" inicia (8 frames a 6fps = ~1.3s)
4. Gabriel entra em IDLE
5. Dialogo automatico: primeiro bordao ("Eu era policial! Eu era vereador! Eu era YouTuber!")
6. Loop TALK ate jogador encerrar

### Quando o jogador morre pela 2a, 3a, N-esima vez
1. Fade mais rapido (300ms)
2. Delay menor (500ms)
3. Gabriel JA ESTA ESPERANDO (no idle, nao emerge da nevoa)
4. Acena cansado. "De volta?"
5. Dialogo disponivel mas nao automatico

### "Falsa Heroica" -- Trigger
- Chance de 15% de ativar quando jogador esta em combate no Limbo
- Cooldown: 60 segundos entre ativacoes
- NAO pode ser desativada pelo jogador (ele vai "ajudar" quer voce queira ou nao)

### "Video Armado" -- Trigger
- Chance de 20% quando evento visual grande acontece (explosao, boss aparece, etc.)
- Cooldown: 45 segundos
- Puramente cosmetico (nao afeta gameplay)

---

## Prioridade de Renderizacao (Z-Order)

1. (atras) Background do Limbo (void roxo + nevoa)
2. Sombra autonoma de Gabriel
3. Sprite de Gabriel
4. Cracha "CANCELADO PERMANENTE" (renderizado SOBRE o sprite, nunca obstruido)
5. Efeitos do Limbo (particulas roxas, nevoa proxima)
6. Baloes de fala / texto de bordao
7. (frente) UI do jogador

---

## Notas Finais de Animacao

1. **A sombra e o segundo personagem**. Ela tem logica de animacao PROPRIA. Investir tempo nela
2. **Humor tragico**: o timing comico depende do CONTRASTE entre esperanca e colapso. Frame 4 do walk (esperanca) seguido de frame 5 (colapso) = piada visual
3. **Nao e zumbi**: Gabriel nao e morto-vivo. Ele e CANCELADO. O movimento e de derrota, nao de decomposicao
4. **O Limbo e silencioso**: animacoes devem ter poucos efeitos de particula (diferente de bosses). O impacto e na EXPRESSAO e no CORPO
5. **A sombra conta a historia**: Sem ler nenhum dialogo, so olhando a sombra vs. corpo, o jogador deve entender que esse personagem "era mais" do que e agora
6. **O cracha e a corrente**: Como corrente de fantasma. Sempre la. Sempre lembrando. O pulso vermelho e o "batimento cardiaco" do cancelamento
