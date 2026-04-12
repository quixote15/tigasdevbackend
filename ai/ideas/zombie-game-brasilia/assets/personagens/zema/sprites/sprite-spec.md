# Zema (O Privatizador / "Sera?") - Sprite Specification

## Overview
- **Character Type:** NPC / Mini-boss de Fase
- **Sprite Dimensions:** 64x64px per frame
- **Perspective:** Top-down levemente isometrica (Y-sorting)
- **Format:** PNG com transparencia
- **Anchor Point:** Bottom-center (32, 60)
- **Style:** Caricatura grotesca, underground comix, Robert Crumb + Andre Guedes

## Deformidades Anatomicas (OBRIGATORIAS em TODOS os frames)
1. **Pupilas de numeros** - os olhos nao tem pupilas normais; no lugar, digitos de calculadora/planilha que mudam sutilmente
2. **Maos de privatizacao** - tudo que as maos tocam ganha um efeito visual de cifrao ($); maos parecem levemente maiores e mais angulares que o normal
3. **Postura rigida demais** - coluna EXCESSIVAMENTE ereta, quase robotica (eficiencia corporativa no corpo)
4. **Sorriso frio permanente** - como se estivesse calculando o custo-beneficio de sorrir

## Color Palette

| Element                | Hex Code  | Usage                                  |
|------------------------|-----------|----------------------------------------|
| Skin Base              | `#E8D0B8` | Pele clara de escritorio (nunca ve sol)|
| Skin Shadow            | `#C4A882` | Sombras na pele                        |
| Skin Highlight         | `#F5E6D0` | Highlights (luz de escritorio fria)    |
| Hair Dark Brown        | `#3A2A1A` | Cabelo impecavel de executivo          |
| Hair Highlight         | `#5A4A3A` | Brilho discreto no cabelo             |
| Suit Dark Blue         | `#1A2744` | Terno azul escuro (corpo principal)    |
| Suit Highlight         | `#2A3E66` | Terno highlights (lapela, ombros)      |
| Suit Shadow            | `#0E1A30` | Sombras profundas no terno             |
| Shirt White            | `#F5F3EE` | Camisa branca por baixo do terno       |
| Tie Red                | `#8B1A1A` | Gravata vermelho escuro (discreto)     |
| Calculator Body        | `#1A1A1A` | Calculadora no bolso do paleto         |
| Calculator Display     | `#00FF41` | Display LED verde da calculadora       |
| Cifrao Gold            | `#FFD700` | Cifrao ($) efeito de privatizacao      |
| Cifrao Shadow          | `#B8860B` | Sombra do cifrao                       |
| Eye White              | `#F5F5F0` | Branco dos olhos                       |
| Eye Pupil Numbers      | `#00FF41` | Pupilas = numeros verdes (display LED) |
| Outline Black          | `#1A1A1A` | Contorno grosso (2px, Crumb style)     |
| Shadow Ground          | `#0D0D0D` | Sombra no chao (50% opacity)           |
| Privatized Stamp Red   | `#CC0000` | Selo "PRIVATIZADO"                     |
| Smile Line             | `#C4A882` | Linhas do sorriso frio                 |
| Shoe Black             | `#0A0A0A` | Sapato social impecavel                |

## Sprite Sheets

### IDLE (4 frames) - `zema_idle.png` (256x64px)
**Frame Rate:** 8 fps | **Loop:** infinito

#### Frame 0 (0,0 a 63,63)
- Zema em pe, postura EXCESSIVAMENTE ereta (coluna reta como regua)
- Terno azul escuro perfeitamente cortado (justo, sem rugas visíveis -- OPOSTO do terno largo de outros politicos)
- Maos juntas na frente (pose corporativa classica, dedos entrelaçados)
- Maos levemente MAIORES que o normal, angulares, como ferramentas
- Calculadora financeira visivel no bolso do paleto (display verde apagado)
- Pupilas: numeros verdes (#00FF41) no lugar de pupilas normais - neste frame mostram "0.00"
- Cabelo impecavel, penteado de executivo, nenhum fio fora do lugar
- Sorriso FRIO: labios curvados mas olhos vazios/calculistas
- Gravata vermelha escura, no perfeitamente centrada
- Sapatos sociais brilhando
- Contornos grossos 2px, sombras pesadas no terno

#### Frame 1 (64,0 a 127,63)
- Mesma pose, pupilas-numeros mudam: "0.00" -> "1.25" (calculando algo)
- Dedos entrelaçados apertam levemente (1px de movimento, sutil)
- Display da calculadora no bolso acende brevemente (flash verde fraco)
- Sorriso identico (perturbadoramente estatico)

#### Frame 2 (128,0 a 191,63)
- Mesma pose, pupilas-numeros: "1.25" -> "47.8" (calculando mais rapido)
- Leve inclinacao da cabeça para a direita (2px) - avaliando algo
- Display da calculadora mostra um numero brevemente
- Uma mao se move 1px (como se fosse tocar algo -- instinto de privatizar)

#### Frame 3 (192,0 a 255,63)
- Volta a pose base, pupilas-numeros: "47.8" -> "0.00" (ciclo completo)
- Cabeca volta ao centro
- Display da calculadora apaga
- Tudo reseta -- ciclo de calculo perpetuo
- Um cifrao ($) MUITO sutil e MUITO pequeno (3x3px) aparece e desaparece perto da mao (reflexo)

---

### WALK (6 frames) - `zema_walk.png` (384x64px)
**Frame Rate:** 10 fps | **Loop:** infinito

#### Frame 0 (0,0 a 63,63)
- Perna esquerda a frente, passada MEDIDA (eficiente, sem desperdicio de energia)
- Postura ereta MESMO caminhando (coluna reta, nunca curva)
- Bracos balancam minimamente (controlado, nao natural)
- Pupilas-numeros: calculando distancia/custo do deslocamento
- Onde o pe toca o chao: minusculo flash de cifrao (privatizando o caminho)

#### Frame 1 (64,0 a 127,63)
- Transicao de pernas, posicao neutra
- Terno se move naturalmente mas SEM RUGAS (magicamente impecavel)
- Mao direita se aproxima do bolso do paleto (perto da calculadora)
- Cifrao do frame anterior se dissipa

#### Frame 2 (128,0 a 191,63)
- Perna direita a frente
- Pupilas-numeros mudam (novo calculo)
- Outro flash de cifrao onde o pe toca
- Calculadora no bolso pisca verde brevemente

#### Frame 3 (192,0 a 255,63)
- Transicao neutra
- Mao esquerda faz gesto SUTIL de "valor" (polegar e indicador quase se tocando, gesto universal de dinheiro)
- Sorriso frio permanece identico

#### Frame 4 (256,0 a 319,63)
- Perna esquerda a frente novamente
- Se passa perto de objeto do cenario: cifrao ($) aparece no objeto (efeito de privatizacao passiva)
- Pupilas-numeros aceleram

#### Frame 5 (320,0 a 383,63)
- Completando ciclo, voltando a posicao inicial
- Cifrao no objeto do cenario se dissipa
- Tudo volta ao equilibrio calculado
- Expressao nao mudou em nenhum momento (PERTURBADOR)

---

### ATTACK (3 frames) - `zema_attack.png` (192x64px)
**Frame Rate:** 10 fps | **Play once**

#### Frame 0 (0,0 a 63,63) - Wind-up: Saca a Calculadora
- Mao direita puxa a calculadora do bolso do paleto (movimento elegante, como quem saca uma arma)
- Calculadora cresce para tamanho exagerado (32x20px) -- GROTESCAMENTE grande para uma calculadora
- Display acende: numeros verdes correndo rapidamente
- Pupilas-numeros SINCRONIZAM com o display da calculadora
- Postura ainda ereta, controlada, sem pressa
- Sorriso ALARGA levemente (o prazer de calcular/privatizar)

#### Frame 1 (64,0 a 127,63) - Strike: Toque de Privatizacao
- Mao estendida para frente com a calculadora apontada
- Do display da calculadora DISPARAM cifroes ($) como projeteis (3-4 cifroes dourados)
- Cada cifrao e 6x6px, dourado (#FFD700) com contorno grosso
- Onde os cifroes atingem: selo "PRIVATIZADO" aparece (carimbo vermelho, #CC0000)
- Pupilas-numeros: "$$$$" (cifroes no lugar de numeros)
- Teclas da calculadora se pressionam sozinhas (animacao das teclas)
- Expressao: satisfacao fria de CEO fechando um deal

#### Frame 2 (128,0 a 191,63) - Follow-through: Guarda a Calculadora
- Mao recolhendo a calculadora de volta ao bolso
- Cifroes projeteis se dissipando
- Selo "PRIVATIZADO" fica visivel no alvo por 2s
- Pupilas-numeros voltam a "0.00"
- Retorno a postura perfeita, como se nada tivesse acontecido
- Display da calculadora apaga ao entrar no bolso

---

### DEATH (4 frames) - `zema_death.png` (256x64px)
**Frame Rate:** 6 fps | **Play once**

#### Frame 0 (0,0 a 63,63) - Primeiro Impacto
- MOMENTO MAIS IMPORTANTE: o terno DESALINHA pela primeira vez
- Gravata torta, um botao do paleto se solta
- Postura perde a rigidez -- ombros caem 2px
- Pupilas-numeros: "ERR" (erro de calculo -- nao previu isso)
- Calculadora QUASE cai do bolso (se projeta para fora)
- Expressao: CHOQUE FRIO (boca levemente aberta, mas sem grito -- CEOs nao gritam)
- Uma ruga aparece no terno (o HORROR absoluto para Zema)

#### Frame 1 (64,0 a 127,63) - Perdendo o Controle
- Zema de joelhos, terno visivelmente amassado
- Calculadora CAI do bolso, no chao, display mostrando numeros aleatorios
- Pupilas-numeros: "0.00" piscando freneticamente
- Cabelo: UM FIO fora do lugar (para Zema, isso e apocaliptico)
- Gravata completamente torta
- Mao estendida tentando pegar a calculadora
- Cifroes ($) que estavam perto dele CAEM como folhas (efeito de des-privatizacao)

#### Frame 2 (128,0 a 191,63) - No Chao
- Deitado de lado, terno em estado LAMENTAVEL (rugas, manchas)
- Calculadora no chao ao lado, display: "0.00000" (muitos zeros -- falencia)
- Pupilas-numeros apagando (luz verde diminuindo)
- Sapatos perderam o brilho
- Cabelo finalmente desarrumado (varios fios fora do lugar)
- Cifroes ao redor mudando de dourado para cinza (desvalorizacao)
- Uma mao ainda esticada em direcao a calculadora

#### Frame 3 (192,0 a 255,63) - Morte do CEO
- Imovel, olhos abertos mas pupilas APAGADAS (sem numeros, tela preta)
- Calculadora ao lado com display mostrando "ERROR" estatico
- Terno completamente desarranjado (a maior indignidade)
- Cifroes ao redor: todos cinza/apagados, caindo no chao
- Sorriso frio FINALMENTE desaparece (boca em linha reta neutra)
- Sombra se espalha -- parece uma planilha de Excel por baixo do corpo (easter egg sutil)

---

### HIT (2 frames) - `zema_hit.png` (128x64px)
**Frame Rate:** 12 fps | **Play once**

#### Frame 0 (0,0 a 63,63)
- Zema recua 2px mas MANTEM a postura ereta (nao curva)
- Terno tremula levemente (primeira micro-ruga)
- Pupilas-numeros: "?!?" (incompreensao -- nao estava no orcamento)
- Calculadora no bolso treme
- Flash branco no corpo (tint 50% white)
- Expressao: sobrancelha levantada de DESAPROVACAO (nao de dor)
- Sorriso diminui 1px (quase imperceptivel)

#### Frame 1 (64,0 a 127,63)
- Zema se recompoe IMEDIATAMENTE (diferente de outros personagens)
- Terno volta ao normal (as rugas desaparecem -- compostura restaurada)
- Pupilas-numeros: calculando o "custo" do hit recebido
- Mao ajusta a gravata com eficiencia
- Sorriso frio RETORNA completamente
- Expressao: "isso sera contabilizado" (ameaca fria)
- Display da calculadora no bolso mostra um numero brevemente (registrando o dano)

---

### SPECIAL (8 frames) - `zema_special.png` (512x64px)
**Frame Rate:** 8 fps | **Play once**
**Nome:** "PRIVATIZACAO EM MASSA" / "SERA?"

#### Frame 0 (0,0 a 63,63) - Preparacao
- Zema levanta a mao direita (gesto de "atenção")
- Pupilas-numeros: "$$$" acelerando
- Calculadora sai do bolso, flutua ao lado do corpo
- Sorriso alarga para o mais largo possivel (ainda frio)
- Comeca a mover os pes (inicio de danca?)

#### Frame 1 (64,0 a 127,63) - "Sera?"
- Zema faz POSE DE TIKTOK (a mesma do "Sera?" com Flavio)
- Mao na cintura, outra apontando para cima
- PERTURBADORAMENTE natural para um politico em zona de zumbi
- Pupilas-numeros: "?" piscando
- Calculadora flutuando gira levemente

#### Frame 2 (128,0 a 191,63) - Onda de Privatizacao Comeca
- Dos pes do Zema, uma ONDA circular se expande pelo chao
- Onda e dourada (#FFD700) com textura de cifrao
- Tudo que a onda toca vira "propriedade privada" (cifroes aparecem)
- Zema no centro, bracos abertos (gesto de magnata)
- Pupilas-numeros: valores CRESCENDO rapidamente

#### Frame 3 (192,0 a 255,63) - Expansao Maxima
- Onda dourada no ponto maximo (raio 100px do personagem)
- TODOS os objetos na area tem cifroes ($) aparecendo
- Selo "PRIVATIZADO" aparece em cada coisa tocada
- Calculadora flutuante mostra "999,999,999.99"
- Zema com expressao de EXTASE FRIO (os olhos brilham mais verde)

#### Frame 4 (256,0 a 319,63) - Danca do TikTok
- Zema FAZ UM PASSO DE DANCA no meio da privatizacao
- Movimento de TikTok incongruente e PERTURBADOR
- Onda dourada pulsando
- Selos "PRIVATIZADO" piscando em todos os objetos
- Pupilas-numeros: emoji de dinheiro

#### Frame 5 (320,0 a 383,63) - Cobranca
- Todos os objetos privatizados mostram PRECOS (valor em pontos)
- "R$ 50", "R$ 100", "R$ 999" aparecem sobre cada objeto
- Jogador perde pontos automaticamente (drenagem de score)
- Zema cruza os bracos (satisfeito com a "gestao")
- Calculadora mostra o total arrecadado

#### Frame 6 (384,0 a 447,63) - Dissipacao
- Onda dourada comeca a recolher
- Precos e cifroes comecam a fade out
- Zema volta a postura padrao
- Calculadora retorna ao bolso
- Pupilas-numeros desacelerando

#### Frame 7 (448,0 a 511,63) - Retorno
- Tudo volta ao normal visual
- Zema perfeitamente composto como se nada tivesse acontecido
- Ultimo cifrao desaparece
- Pupilas-numeros: "0.00" (reset)
- Sorriso frio padrao restaurado
- Calculadora de volta no bolso, display apagado

---

## Sprite Sheet Summary

| Sheet           | Frames | Dimensions  | File                | Atlas Key       |
|-----------------|--------|-------------|---------------------|-----------------|
| Idle            | 4      | 256x64px    | `zema_idle.png`     | `zema_idle`     |
| Walk            | 6      | 384x64px    | `zema_walk.png`     | `zema_walk`     |
| Attack          | 3      | 192x64px    | `zema_attack.png`   | `zema_attack`   |
| Death           | 4      | 256x64px    | `zema_death.png`    | `zema_death`    |
| Hit             | 2      | 128x64px    | `zema_hit.png`      | `zema_hit`      |
| Special         | 8      | 512x64px    | `zema_special.png`  | `zema_special`  |

## Phaser 3 Atlas Keys
```javascript
this.load.spritesheet('zema_idle', 'assets/personagens/zema/sprites/zema_idle.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('zema_walk', 'assets/personagens/zema/sprites/zema_walk.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('zema_attack', 'assets/personagens/zema/sprites/zema_attack.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('zema_death', 'assets/personagens/zema/sprites/zema_death.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('zema_hit', 'assets/personagens/zema/sprites/zema_hit.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('zema_special', 'assets/personagens/zema/sprites/zema_special.png', { frameWidth: 64, frameHeight: 64 });
```

## Notas para o Artista
- Zema e FRIO e CALMO -- isso e o que o torna PERTURBADOR no meio do caos zumbi
- O TERNO NUNCA tem rugas (exceto death animation -- o horror e perder a compostura)
- PUPILAS DE NUMEROS sao o detalhe mais perturbador -- devem parecer displays LED verdes
- CIFROES aparecem em tudo que ele toca -- e uma maldicao/poder visual
- Contornos GROSSOS (2px minimo), estilo underground comix
- A DANCA DE TIKTOK no special deve parecer ERRADA no contexto (humor perturbador)
- Ele NUNCA grita, NUNCA perde a compostura (ate a morte) -- o humor e a calma impossivel
- A calculadora e como a espada de um cavaleiro -- sempre presente, sempre pronta
- Sapatos SEMPRE brilhando, cabelo SEMPRE impecavel
- Estilo Andre Guedes: grotesco mas DIFERENTE -- o grotesco do Zema e a PERFEICAO excessiva
