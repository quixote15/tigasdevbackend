# Nikolas Ferreira (O Influencer-Politico) - Sprite Specification

## Overview
- **Character Type:** NPC Provocador
- **Sprite Dimensions:** 64x64px per frame
- **Perspective:** Top-down levemente isometrica (Y-sorting)
- **Format:** PNG com transparencia
- **Anchor Point:** Bottom-center (32, 60)
- **Style:** Caricatura grotesca, underground comix, Robert Crumb + Andre Guedes

## Deformidades Anatomicas (OBRIGATORIAS em TODOS os frames)
1. **Polegar ENORME** - mao direita com polegar 3x maior que o normal (de tanto usar celular)
2. **Pescoco curvado para frente** - angulo de ~45 graus permanente (vicio de tela)
3. **Cabeca levemente desproporcional** - maior que o corpo (estilo caricatura)
4. **Ring light como aureola** - circulo de luz ao redor da cabeca (substitui aureola religiosa)

## Color Palette

| Element                | Hex Code  | Usage                              |
|------------------------|-----------|-------------------------------------|
| Skin Base              | `#D4A574` | Pele bronzeada de ring light        |
| Skin Shadow            | `#A67B5B` | Sombras na pele                     |
| Skin Highlight         | `#E8C9A0` | Highlights (iluminacao ring light)  |
| Hair Black             | `#1A1A1A` | Cabelo escuro arrumado              |
| Hair Highlight         | `#3D3D3D` | Brilho no cabelo (gel excessivo)    |
| Shirt White            | `#F0EDE8` | Camisa/camiseta de influencer       |
| Shirt Shadow           | `#C8C4BC` | Sombras na roupa                    |
| Pants Dark             | `#2C2C2C` | Calca escura                        |
| Phone Screen Blue      | `#4A90D9` | Tela do celular (brilho)            |
| Phone Body Black       | `#0D0D0D` | Corpo do celular                    |
| Ring Light White       | `#FFFDE0` | Ring light aureola (quente)         |
| Ring Light Glow        | `#FFF8B0` | Glow do ring light (30% opacity)   |
| Views Green            | `#00FF41` | Numeros de views flutuantes         |
| Views Red              | `#FF4136` | Notificacao/like flutuante          |
| Thumb Skin             | `#D4A574` | Polegar enorme (mesma cor de pele)  |
| Thumb Nail             | `#F0E0D0` | Unha do polegar gigante             |
| Outline Black          | `#1A1A1A` | Contorno grosso (2px, Crumb style)  |
| Shadow Ground          | `#0D0D0D` | Sombra no chao (50% opacity)        |
| Deboche Smile          | `#C0392B` | Sorriso de deboche (labios)         |
| Eye White              | `#F5F5F0` | Branco dos olhos                    |
| Pupil Dark             | `#0A0A0A` | Pupilas (olhando pra tela)          |

## Sprite Sheets

### IDLE (4 frames) - `nikolas_idle.png` (256x64px)
**Frame Rate:** 8 fps | **Loop:** infinito

#### Frame 0 (0,0 a 63,63)
- Nikolas em pe, corpo levemente curvado pelo pescoco para frente
- Celular na mao direita, erguido na frente do rosto (pose de selfie/gravacao)
- POLEGAR ENORME da mao direita apoiado na tela do celular, ocupando ~40% da largura do telefone
- Pescoco curvado 45 graus para frente, olhando a tela
- Ring light ao redor da cabeca: circulo fino branco-quente (#FFFDE0), levemente pulsante
- 2-3 numeros de views flutuando ao redor (pequenos "1.2M", "♥ 50K" em verde/vermelho, 4-5px de altura)
- Cabelo excessivamente arrumado, gel brilhando
- Expressao de deboche: sorriso enviesado, uma sobrancelha levantada
- Olhos olhando para a tela do celular, nao para frente
- Contornos grossos 2px, sombras pesadas

#### Frame 1 (64,0 a 127,63)
- Mesma pose base, leve inclinacao do celular para a esquerda (2px)
- Ring light pulsa levemente mais brilhante (glow area +2px)
- Numeros de views se movem 1-2px para cima (flutuando)
- Polegar enorme move levemente na tela (scrollando)
- Brilho na tela do celular se desloca levemente

#### Frame 2 (128,0 a 191,63)
- Pose base, celular volta ao centro
- Ring light no brilho maximo (glow area +4px)
- Numeros de views no ponto mais alto da flutuacao
- Um novo numero aparece ("📱 LIVE" em vermelho)
- Sorriso de deboche aumenta levemente (1px mais largo)

#### Frame 3 (192,0 a 255,63)
- Pose base, leve inclinacao do celular para a direita (2px)
- Ring light diminui brilho (voltando ao normal)
- Numeros de views comecam a descer (ciclo de flutuacao)
- Polegar enorme faz gesto de "scroll up" (posicao ligeiramente diferente)
- Expressao volta ao deboche padrao

---

### WALK (6 frames) - `nikolas_walk.png` (384x64px)
**Frame Rate:** 10 fps | **Loop:** infinito

#### Frame 0 (0,0 a 63,63)
- Perna esquerda a frente, direita atras (passo 1)
- Corpo inteiro curvado para frente (pescoco + postura de quem anda olhando celular)
- Celular erguido na mao direita, polegar ENORME na tela
- Ring light segue a cabeca, com leve trail de luz (2px atras)
- Numeros de views trail atras do personagem (efeito de movimento)
- NAO olha para frente - olha SOMENTE para o celular

#### Frame 1 (64,0 a 127,63)
- Transicao: pernas em posicao neutra (passando)
- Corpo balance levemente para a esquerda
- Celular estavel, tela brilha
- Ring light com motion blur sutil (1px)

#### Frame 2 (128,0 a 191,63)
- Perna direita a frente, esquerda atras (passo 2)
- Corpo balance para a direita
- Polegar enorme desliza na tela (posicao diferente do frame 0)
- Numeros de views se dispersam levemente com o movimento

#### Frame 3 (192,0 a 255,63)
- Transicao: pernas em posicao neutra
- Leve tropecon (porque nao olha pra frente) - corpo desequilibra 2px
- Celular quase cai mas polegar enorme segura firme
- Ring light treme com o tropecon

#### Frame 4 (256,0 a 319,63)
- Perna esquerda a frente novamente, recuperando do tropecon
- Expressao nao muda (deboche permanente, nem percebeu que quase caiu)
- Volta a scrollar normalmente
- Numeros de views voltam a orbitar

#### Frame 5 (320,0 a 383,63)
- Transicao final, voltando a posicao inicial
- Leve speed up no scroll do polegar
- Ring light estabiliza
- 1 novo numero de view aparece ("+10K")

---

### ATTACK (3 frames) - `nikolas_attack.png` (192x64px)
**Frame Rate:** 10 fps | **Play once**

#### Frame 0 (0,0 a 63,63) - Wind-up
- Nikolas ergue o celular acima da cabeca com as duas maos
- Polegar ENORME brilha com luz da tela
- Ring light INTENSIFICA (glow area dobra, +8px)
- Tela do celular vira FLASH de camera (branco puro)
- Expressao: sorriso maniaco de quem vai gravar algo "epico"
- Numeros de views comecam a girar mais rapido ao redor

#### Frame 1 (64,0 a 127,63) - Flash Attack
- Celular aponta diretamente para o alvo
- FLASH EXPLODE da tela: raios de luz branca saem do celular (6-8 linhas radiais)
- Ring light no maximo absoluto (quase funde com o flash)
- "📸 GRAVA!" aparece como onomatopeia (letras grotescas, amarelo com sombra vermelha)
- Polegar enorme pressiona o botao de gravar
- Onda de numeros de views disparada na direcao do ataque

#### Frame 2 (128,0 a 191,63) - Follow-through
- Flash diminuindo, raios de luz se dissipando
- Nikolas puxa celular de volta para posicao de selfie
- Tela mostra "1M VIEWS" piscando
- Ring light voltando ao normal com afterglow
- Expressao de satisfacao (boca aberta, "isso vai viralizar!")
- Particulas residuais de luz e numeros flutuando

---

### DEATH (4 frames) - `nikolas_death.png` (256x64px)
**Frame Rate:** 6 fps | **Play once**

#### Frame 0 (0,0 a 63,63) - Hit Fatal
- Nikolas levanta as maos em choque, celular balanca
- Ring light pisca freneticamente (ON/OFF)
- Expressao de PANICO absoluto (boca escancarada, olhos arregalados)
- Numeros de views comecam a cair (literalmente, caindo como gravidade)
- Tela do celular mostra "SEM SINAL"

#### Frame 1 (64,0 a 127,63) - Queda
- Nikolas caindo de joelhos, celular escapando da mao
- MAS o polegar ENORME ainda tenta segurar o celular (ultimos dedos agarrados)
- Ring light quebrando em pedacos (fragmentos de luz caindo)
- Numeros de views: "0 VIEWS", "UNFOLLOW", "BLOCKED" caindo como chuva
- Tela do celular rachando

#### Frame 2 (128,0 a 191,63) - No Chao
- Nikolas no chao, esticando a mao em direcao ao celular que caiu
- Celular no chao com tela completamente rachada, luz fraca
- Ring light completamente apagado, apenas armacao escura visivel
- Polegar enorme treme tentando alcançar o celular
- Numeros mudaram para "0", "CANCELADO", "404"

#### Frame 3 (192,0 a 255,63) - Morte Digital
- Nikolas deitado, imóvel, mão esticada em direção ao celular
- Celular com tela PRETA (morto)
- Ring light: apenas contorno escuro, sem luz
- Onde estavam numeros de views: "..." (reticencias piscando e apagando)
- Polegar enorme e o ultimo detalhe visível (a deformidade permanece)
- Sombra se espalha sob o corpo

---

### HIT (2 frames) - `nikolas_hit.png` (128x64px)
**Frame Rate:** 12 fps | **Play once**

#### Frame 0 (0,0 a 63,63)
- Nikolas recua, corpo jogado para tras
- Celular quase cai mas polegar ENORME segura
- Ring light pisca (OFF neste frame)
- Expressao de ULTRAJE (nao de dor - "como OUSAM me interromper?!")
- Numeros de views tremem/glitcham
- Flash branco no corpo (tint 50% white)

#### Frame 1 (64,0 a 127,63)
- Nikolas se recompoe rapidamente
- Celular de volta na posicao de gravar (ja voltou a filmar o que aconteceu)
- Ring light volta (ON)
- Expressao muda para INDIGNACAO + sorriso ("isso vai render views!")
- Numeros de views: "+100K" aparece (porque o hit gera conteudo)

---

### SPECIAL (6 frames) - `nikolas_special.png` (384x64px)
**Frame Rate:** 8 fps | **Play once**
**Nome:** "LIVESTREAM APOCALIPTICA"

#### Frame 0 (0,0 a 63,63) - Preparacao
- Nikolas ergue celular no alto com as duas maos (polegar ENORME dominando o grip)
- Olha diretamente para o celular (nunca para o "publico")
- Ring light comeca a EXPANDIR (circulo cresce de 20px para 30px de diametro)
- Tela mostra: "GOING LIVE..." em vermelho
- Numeros de views aceleram rotacao ao redor

#### Frame 1 (64,0 a 127,63) - Ativacao
- Ring light EXPLODE em tamanho (preenche quase todo o frame 64x64)
- Luz branca-quente intensa emana da cabeca
- Celular emite onda de choque circular (linha fina branca expandindo)
- "🔴 LIVE" aparece em vermelho intenso acima da cabeca
- Polegar enorme pressiona botao com forca visivel

#### Frame 2 (128,0 a 191,63) - Onda de Notificacoes
- Do celular saem DEZENAS de icones de notificacao como projeteis:
  - Coracoes (♥) vermelhos
  - Polegares para cima (👍) - ironicamente menores que o polegar dele
  - Sinos de notificacao (🔔) amarelos
  - Cifras de monetizacao ($) verdes
- Icones se espalham radialmente em todas as direcoes
- Ring light pulsando no maximo
- Nikolas com expressao EXTASIADA

#### Frame 3 (192,0 a 255,63) - Impacto Maximo
- Onda de notificacoes no ponto maximo de expansao
- Tela do celular mostra "10M VIEWS" em numeros gigantes
- Ring light emite pulsos (linhas circulares concentricas)
- "VIRALIZA!!" como onomatopeia GRANDE (estilo comic, amarelo/vermelho)
- Numeros de views ENORMES dominam a tela: "100M", "1B"

#### Frame 4 (256,0 a 319,63) - Dissipacao
- Notificacoes comecam a se dissipar nas bordas
- Ring light diminui gradualmente
- Tela do celular volta para modo normal
- Nikolas baixa celular para posicao de selfie
- Expressao de SATISFACAO absoluta
- Numeros de views altos persistem: "50M"

#### Frame 5 (320,0 a 383,63) - Recuperacao
- Volta quase ao idle, mas com afterglow
- Ring light com residuo de brilho extra (glow +2px alem do normal)
- Celular na posicao padrao
- Ultimas particulas de notificacao desaparecendo
- Expressao volta ao deboche padrao
- Numeros de views normalizando

---

## Sprite Sheet Summary

| Sheet           | Frames | Dimensions  | File                  | Atlas Key         |
|-----------------|--------|-------------|-----------------------|-------------------|
| Idle            | 4      | 256x64px    | `nikolas_idle.png`    | `nikolas_idle`    |
| Walk            | 6      | 384x64px    | `nikolas_walk.png`    | `nikolas_walk`    |
| Attack          | 3      | 192x64px    | `nikolas_attack.png`  | `nikolas_attack`  |
| Death           | 4      | 256x64px    | `nikolas_death.png`   | `nikolas_death`   |
| Hit             | 2      | 128x64px    | `nikolas_hit.png`     | `nikolas_hit`     |
| Special         | 6      | 384x64px    | `nikolas_special.png` | `nikolas_special` |

## Phaser 3 Atlas Keys
```javascript
// Carregamento
this.load.spritesheet('nikolas_idle', 'assets/personagens/nikolas-ferreira/sprites/nikolas_idle.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('nikolas_walk', 'assets/personagens/nikolas-ferreira/sprites/nikolas_walk.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('nikolas_attack', 'assets/personagens/nikolas-ferreira/sprites/nikolas_attack.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('nikolas_death', 'assets/personagens/nikolas-ferreira/sprites/nikolas_death.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('nikolas_hit', 'assets/personagens/nikolas-ferreira/sprites/nikolas_hit.png', { frameWidth: 64, frameHeight: 64 });
this.load.spritesheet('nikolas_special', 'assets/personagens/nikolas-ferreira/sprites/nikolas_special.png', { frameWidth: 64, frameHeight: 64 });
```

## Notas para o Artista
- O POLEGAR ENORME e o detalhe mais importante - deve ser GROTESCO e impossivel de ignorar
- O celular NUNCA sai da mao (exceto na death animation, e mesmo assim ele tenta segurar)
- O RING LIGHT e como uma aureola corrupta - sempre presente, sempre pulsando
- Numeros de views sao como parasitas visuais - sempre orbitando
- Expressao de DEBOCHE e o padrao - ele acha tudo engraçado e "conteudo"
- Contornos GROSSOS (2px minimo), sombras PESADAS, assimetria PROPOSITAL
- NUNCA desenhar limpo/moderno - tudo deve ser sujo e grotesco no estilo Andre Guedes
- O pescoco curvado deve parecer DOENTIO, nao natural
