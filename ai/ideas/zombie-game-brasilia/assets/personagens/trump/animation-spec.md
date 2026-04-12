# TRAMPI (Trump) - Especificacao Completa de Animacoes

## Boss Internacional - "Zumbis de Brasilia"

---

## Configuracao Global

- **Frame Rate**: 8 FPS (estilo jerky, Andre Guedes)
- **Interpolacao**: NENHUMA. Zero easing, zero tweening entre frames. Transicoes ABRUPTAS.
- **Motor**: Phaser 3 (SpriteSheet + AnimationManager)
- **Direcao**: Sprites base viram para a DIREITA. Flip horizontal para esquerda via `sprite.flipX = true`
- **Hitbox**: 40x56px centrado no sprite 64x64px (margem de 12px horizontal, 4px topo, 4px base)
- **Layers de Renderizacao** (da frente para tras):
  1. Particulas/Texto flutuante
  2. Micro-maos overlay (quando necessario)
  3. Cabelo overlay (quando necessario)
  4. Sprite principal
  5. Glow layer (pele laranja)
  6. Sombra do chao

---

## 1. IDLE -- "Tremendous Standing"

### Dados Tecnicos
- **Sprite Sheet**: `trump_idle.png` (256x64px)
- **Frames**: 4
- **Duracao Total do Ciclo**: 500ms (4 frames x 125ms cada)
- **Loop**: Sim, infinito
- **Prioridade**: 0 (mais baixa, qualquer animacao interrompe)

### Timeline Frame a Frame

| Frame | Duracao | Nome          | Eventos                                                     |
|-------|---------|---------------|-------------------------------------------------------------|
| 0     | 125ms   | idle_stand    | Pose base. Glow pele em 35% opacity. Cabelo: normal.       |
| 1     | 125ms   | idle_puff     | Peito infla +2px. Glow sobe para 50%. Cabelo: puff +1px.   |
| 2     | 125ms   | idle_adjust   | Mao tenta pegar gravata -- FALHA. Glow volta 35%.          |
| 3     | 125ms   | idle_smug     | Gesto OK com maos (impossivel). 2 sparkles dourados.       |

### Ciclo do Glow da Pele (Paralelo)
```
Glow Idle Cycle (independente dos frames):
  0ms:    opacity 30%
  500ms:  opacity 50% (pico)
  1000ms: opacity 30% (volta)
  Repeat: infinito
  Easing: sine (UNICA excecao de easing -- glow organico)
```

### Animacao das Micro-Maos (Overlay, Paralelo)
```
Frame 0: hand_idle (ambas as maos penduradas)
Frame 1: hand_idle (tremem levemente com o puff do peito)
Frame 2: hand_grab_try (mao direita) -> hand_grab_fail -> hand_drop
         Timing: grab_try nos primeiros 40ms, fail nos proximos 40ms, drop nos ultimos 45ms
Frame 3: hand_ok_attempt (ambas as maos) -- ficam tentando formar o circulo
```

### Animacao do Cabelo (Overlay, Paralelo)
```
Frame 0: hair_normal
Frame 1: hair_puff (infla com o ego)
Frame 2: hair_normal (volta)
Frame 3: hair_normal (leve tremor, 1px de jitter horizontal aleatorio)
```

### Particulas
- **Frame 3 apenas**: 2 sparkles dourados (1x1px, #FFD700) spawn nas posicoes das maos, sobe 4px em 125ms, fade de 100% para 0%

### Codigo Phaser 3
```javascript
this.anims.create({
  key: 'trump_idle',
  frames: this.anims.generateFrameNumbers('trump_idle', { start: 0, end: 3 }),
  frameRate: 8,
  repeat: -1
});
```

---

## 2. WALK -- "Presidential March"

### Dados Tecnicos
- **Sprite Sheet**: `trump_walk.png` (384x64px)
- **Frames**: 6
- **Duracao Total do Ciclo**: 750ms (6 frames x 125ms)
- **Loop**: Sim, enquanto em movimento
- **Prioridade**: 1

### Timeline Frame a Frame

| Frame | Duracao | Nome               | Eventos                                                         |
|-------|---------|--------------------|-----------------------------------------------------------------|
| 0     | 125ms   | walk_right_contact | Pe direito toca. Corpo inclina +2px dir. Camera shake 0.5px.   |
| 1     | 125ms   | walk_right_mid     | Transferencia. Corpo centraliza. Botao brilha.                  |
| 2     | 125ms   | walk_right_lift    | Pe levanta. Corpo sobe +2px. Terno flutua.                      |
| 3     | 125ms   | walk_left_contact  | Pe esquerdo toca. Corpo inclina +2px esq. Camera shake 0.5px.  |
| 4     | 125ms   | walk_left_mid      | Transferencia. Corpo centraliza.                                 |
| 5     | 125ms   | walk_left_lift     | Pe levanta. Corpo sobe +2px. Completa ciclo.                    |

### Efeitos Sincronizados

#### Camera Shake (micro)
```
Frames 0 e 3 (contato com chao):
  Intensidade: 0.5px horizontal, 0.3px vertical
  Duracao: 60ms
  Decay: linear
  NOTA: So aplica se boss esta proximo do jogador (< 200px)
```

#### Cabelo Physics
```
Frame 0: hair_wind_left (contra-movimento, pe direito = corpo vai pra direita = cabelo pra esquerda)
Frame 1: hair_normal (retorno)
Frame 2: hair_normal (leve compressao -1px vertical)
Frame 3: hair_wind_right (contra-movimento espelhado)
Frame 4: hair_normal
Frame 5: hair_normal (compressao)
```

#### Gravata Swing (procedural)
```
A gravata e um sprite separado (4x20px) ancorado no ponto (32, 18) do sprite.
Pendulo simples:
  Frame 0: rotacao -8 graus (balanca para esquerda)
  Frame 1: rotacao -3 graus (voltando)
  Frame 2: rotacao 0 graus (centro)
  Frame 3: rotacao +8 graus (balanca para direita)
  Frame 4: rotacao +3 graus (voltando)
  Frame 5: rotacao 0 graus (centro)
Periodo: sincronizado com walk cycle
Damping: NENHUM (balanca infinitamente -- gravata hipnotica)
```

#### Terno Flap
```
Frames 0 e 3: Aba do terno do lado do pe que toca se ABRE 3px
  Implementacao: sprite overlay de 8x12px (aba do terno)
  Posicao: lateral do torso, lado do contato
  Animacao: 0px -> 3px (instantaneo no frame de contato) -> 0px (125ms fade)
```

#### Maos Swing
```
Maos balancam em contra-fase com as pernas (caminhada natural):
  Frame 0: mao direita frente (Y-2px), mao esquerda tras (Y+2px)
  Frame 1: ambas centralizadas
  Frame 2: mao direita tras, mao esquerda frente
  Frame 3-5: espelho de 0-2
  
DETALHE COMICO (Frame 3 especificamente):
  A mao direita microscopica tenta segurar a aba do terno que abre.
  hand_grab_try (40ms) -> hand_grab_fail (40ms) -> aba escapa
  Acontece TODA VEZ. Ele nunca aprende.
```

#### SFX Triggers
```
Frame 0: sfx_step_heavy_1 (volume 0.3)
Frame 3: sfx_step_heavy_2 (volume 0.3)
```

---

## 3. ATTACK -- "Tremendous Swing"

### Dados Tecnicos
- **Sprite Sheet**: `trump_attack.png` (192x64px)
- **Frames**: 3
- **Duracao Total**: 375ms
- **Loop**: Nao (single play, retorna ao idle)
- **Prioridade**: 3 (alta)
- **Hitbox de Ataque**: Ativa no Frame 1, area de 32x32px a frente do sprite
- **Dano**: 25 HP
- **Cooldown**: 800ms

### Timeline Frame a Frame

| Frame | Duracao | Nome              | Eventos                                                          |
|-------|---------|-------------------|------------------------------------------------------------------|
| 0     | 150ms   | attack_windup     | Corpo gira 15deg. Mao tenta segurar taco. Glow 50%.             |
| 1     | 100ms   | attack_swing      | IMPACTO. Hitbox ativa. Corpo gira 30deg. Glow 70%. Shake 2px.   |
| 2     | 125ms   | attack_follow     | Pos-impacto. Texto "TREMENDOUS!". Smirk. Glow volta 40%.        |

### Detalhamento do Frame 0 -- Wind-up (150ms)

```
Sequencia interna (sub-frame events):
  0ms:   Corpo comeca a rotacionar. Sound: sfx_swoosh_start (volume 0.2)
  30ms:  Mao microscopica tenta agarrar taco de golfe
         Calculo RNG: 50% chance de sucesso
         SE FALHA: 
           - Taco escorrega 2px
           - Mao faz hand_grab_fail
           - Delay de 50ms enquanto tenta de novo
           - Segunda tentativa SEMPRE sucede
           - Texto flutuante: "..." (cor #CCCCCC, 3px altura, fade 200ms)
         SE SUCEDE:
           - hand_grab_success
           - Sem delay
  50ms:  Perna esquerda avanca como pivot (deslocamento 3px)
  100ms: Cabelo achata do lado do swing (hair_impact)
  120ms: Gravata comeca a voar na direcao oposta ao swing
  150ms: Transicao para Frame 1
```

### Detalhamento do Frame 1 -- Swing (100ms)

```
FRAME MAIS RAPIDO -- impacto maximo
  0ms:   Hitbox de ataque ATIVA (40x32px retangulo a frente)
         Corpo no auge da rotacao (30 graus)
         Camera shake: 2px horizontal, 1px vertical, 80ms decay
         Sound: sfx_golf_swing (volume 0.7) OU sfx_whoosh se erra
         Taco em motion blur (sprite substituido por versao blurred)
         3 sparkles dourados spawn na ponta do taco
         Cabelo estica 3px na direcao oposta (hair_wind, exagerado)
         Gravata enrolada ao redor do torso (sprite overlay)
         Glow da pele INTENSIFICA para 70%
  50ms:  SE HIT EM INIMIGO:
           - Particulas de impacto: 4 sprites 2x2px (#FFD700) irradiam
           - Sound: sfx_tremendous (voz "TREMENDOUS!")
           - Hitstop: 50ms de freeze frame (game feel)
           - Screen flash: branco 20% opacity por 30ms
         SE MISS:
           - Sound: sfx_fakenews (voz "FAKE NEWS!")
           - Trampi tropeca levemente (corpo avanca 2px involuntariamente)
           - Texto flutuante: "FAKE NEWS!" (vermelho, 4px, sobe 8px, fade 400ms)
  100ms: Transicao para Frame 2
```

### Detalhamento do Frame 2 -- Follow-through (125ms)

```
  0ms:   Corpo desacelera a rotacao, para em pose dramatica
         Braco estendido, taco apontando para baixo (completou o arco)
         Cabelo faz bounce: comprime 2px -> expande 1px -> normal
         Gravata comeca a desenrolar
         Glow volta para 40%
  30ms:  SE HIT: Texto "TREMENDOUS!" aparece (dourado #FFD700, outline preto)
                 Posicao: 8px acima da cabeca
                 Tamanho: 5px altura, letras irregulares
                 Animacao: scale 0% -> 120% -> 100% (bounce appear, 80ms)
                 Fade: inicia em 100% opacity, fade para 0% ao longo de 600ms
         SE MISS: Texto "FAKE NEWS!" ja esta visivel do frame anterior
  60ms:  Smirk de satisfacao (expressao muda)
         Mao esquerda microscopica tenta thumbs up (hand_thumbsup)
         So que e tao pequena que ninguem percebe
  125ms: Retorna para idle (transicao ABRUPTA, sem blend)
```

### Dano e Mecanica de Combate
```
Dano base: 25 HP
Dano critico (10% chance): 50 HP + "VERY TREMENDOUS!" texto
Knockback: 4px na direcao do swing
Efeito de debuff: "Tarifa" -- alvo fica 15% mais lento por 3 segundos
```

---

## 4. DEATH -- "You're Impeached"

### Dados Tecnicos
- **Sprite Sheet**: `trump_death.png` (256x64px)
- **Frames**: 4 (mais fade out processado pelo engine)
- **Duracao Total**: 2000ms (500ms por frame)
- **Loop**: Nao (play once, depois o sprite e removido/destroyed)
- **Prioridade**: 5 (maxima, nao pode ser interrompida)

### Timeline Frame a Frame

| Frame | Duracao | Nome           | Eventos                                                            |
|-------|---------|----------------|--------------------------------------------------------------------|
| 0     | 500ms   | death_hit      | Golpe fatal. Choque. Botoes voam. Cabelo explode parcial.          |
| 1     | 500ms   | death_fall     | Queda para tras. Careca revelada. Ketchup na camisa.               |
| 2     | 500ms   | death_ground   | No chao. Terno espalhado. Gravata no rosto. Dente voa.            |
| 3     | 500ms   | death_fade     | Glow morre. Pele empalidece. "FAKE NEWS..." fade.                 |

### Detalhamento do Frame 0 -- Hit Fatal (500ms)

```
SEQUENCIA DRAMATICA:
  0ms:   Game entra em SLOW MOTION (timeScale = 0.5) por 300ms
         Camera shake PESADO: 4px, 200ms, exponential decay
         Sound: sfx_death_hit (impacto grave, reverb)
         Sprite flasha branco 3 vezes (0ms, 60ms, 120ms) -- 30ms cada flash
         Glow da pele EXPLODE para 100% opacity, cor muda para branco
  
  100ms: PARTICULAS -- Botoes do terno:
         - 2 botoes dourados (2x2px, #DAA520)
         - Spawn na frente do torso
         - Velocidade: 60px/s em angulos 30deg e 150deg
         - Gravidade: 120px/s²
         - Bounce: 1x ao tocar Y do chao, coeficiente 0.3
         - Fade: 100% -> 0% ao longo de 800ms
         
  150ms: PARTICULAS -- Fios de cabelo:
         - 4-5 fios (1x3px cada, #FF8C00)
         - Spawn no topo da cabeca
         - Velocidade: 40px/s em direcoes aleatorias (arco de 180deg para cima)
         - Gravidade: 80px/s²
         - Rotacao: 360deg/s (rodopiando)
         - Fade: ao longo de 1200ms
  
  200ms: Corpo comeca a se curvar para tras
         Expressao muda para CHOQUE (olhos maximos: 3x3px cada)
         Boca abre ao maximo (5px abertura oval)
         Cabelo-ninho comeca a se desgrudar (hair_detach transition)
  
  300ms: Slow motion ACABA, velocidade normal
         Estrela de dor aparece (3x3px, #FFFF00) acima da cabeca
         Maos microscopicas se levantam em desespero patetico
         Sound: sfx_trump_scream (grito dramatico)
  
  500ms: Transicao para Frame 1
```

### Detalhamento do Frame 1 -- Queda (500ms)

```
  0ms:   Corpo em 45 graus de inclinacao, caindo para tras
         REVELACAO DA CARECA:
           - hair_detach -> interpolacao manual de 3 sub-frames:
             0ms:  Cabelo-ninho a 70% conectado (separacao 3px no lado direito)
             150ms: Cabelo a 40% conectado (separacao 8px, careca visivel 5x3px)
             300ms: Cabelo a 20% conectado (quase caindo, careca #FFB6C1 bem visivel)
           - A careca e ROSA PALIDA -- contraste chocante com o laranja neon
           - Cross-hatching na careca (3 linhas finas, textura de pele real)
         
  100ms: Terno se abre revelando camisa branca
         KETCHUP REVEAL:
           - 3 manchas de ketchup na camisa (#CC0000)
           - Posicoes: peito esquerdo (2x2px), barriga (3x2px), colarinho (1x1px)
           - Humor: o presidente come hamburger e se suja como crianca
         
  200ms: Gravata chicoteia e enrola no rosto (sprite overlay animado)
         Maos microscopicas tentam agarrar qualquer coisa no ar
         hand_grab_try em loop rapido (3 tentativas em 200ms)
         Cada tentativa FALHA -- maos pequenas demais para agarrar o ar
         
  350ms: Corpo atinge 70 graus de inclinacao
         Sound: sfx_suit_rip (tecido rasgando, sutil)
         1 costura do terno "abre" visualmente (linha dourada se separa 1px)
         
  500ms: Transicao para Frame 2
```

### Detalhamento do Frame 2 -- No Chao (500ms)

```
  0ms:   Corpo BATE no chao
         Sound: sfx_heavy_thud (impacto pesado) + sfx_coins_scatter (botoes)
         Camera shake: 3px, 150ms
         POSE FINAL NO CHAO:
           - Corpo horizontal, Y 40-60 do frame
           - Terno espalhado como poça dourada (#DAA520 area 40x12px)
           - Cabelo-ninho 80% descolado, pendurado por fios
           - Careca plenamente visivel (#FFB6C1, 8x5px)
           - Gravata jogada sobre o rosto cobrindo olho esquerdo
           - Olho direito visivel: formato X (nocaute classico)
           - Boca aberta, 1 dente faltando (buraco preto 1x1px)
         
  50ms:  PARTICULA -- Dente voando:
           - 1 dente (2x2px, #FFFFCC)
           - Spawn da boca
           - Velocidade: 50px/s, angulo 60deg para cima-direita
           - Gravidade: 100px/s²
           - Rotacao: 720deg/s
           - Bounce: 2x no chao, coeficiente 0.4
           - Sound ao bouncer: sfx_tooth_ping (tink metalico agudo)
           
  100ms: PARTICULA -- Sapato voando:
           - 1 sapato (3x2px, #1A1A1A)
           - Spawn do pe direito
           - Velocidade: 30px/s, angulo 80deg para cima
           - Gravidade: 100px/s²
           - Rotacao: 180deg/s
           - Cai fora do frame (nao volta)
           
  200ms: Maos microscopicas apontam para cima, RIGIDAS
         Parecem patas de inseto morto (hand_dead)
         Nao se movem mais ate o final
         
  400ms: Estabiliza. Poeira assenta. 
         2 particulas de poeira (1x1px, #AA9966) fade out
         
  500ms: Transicao para Frame 3
```

### Detalhamento do Frame 3 -- Fade Final (500ms)

```
  0ms:   TRANSFORMACAO VISUAL:
         A "mascara" cai -- toda a artificialidade do personagem se desfaz:
         
         PELE: Glow laranja faz fade de 50% -> 0% ao longo de 500ms
               Cor da pele transiciona: #FF6B00 -> #CC9966 (pele palida real)
               O laranja neon ERA TUDO FALSO -- a pele real e palida e sem graca
               Implementacao: color lerp no shader, 500ms
         
         CABELO: Encolhe de 18px -> 10px largura ao longo de 500ms
                 Muda de volumoso para murcho e ralo
                 Cor escurece: #FF8C00 -> #CC8844 (loiro sujo sem tintura)
                 hair_gone no final
         
         TERNO: Perde brilho dourado
                #DAA520 -> #CCCC66 (amarelo opaco, ouro falso revelado)
                Os "sparkles" somem completamente
         
         GRAVATA: Descolore de #CC0000 -> #884444 (vermelho desbotado)
         
  100ms: Sprite inteiro comeca a fade para 80% opacity
         Sound: sfx_sad_trombone (wah wah wah, volume 0.4)
         
  200ms: TEXTO FLUTUANTE: "FAKE NEWS..."
         - Posicao: 10px acima do corpo
         - Cor: #CC0000 (vermelho)
         - Estilo: italico irregular, letras tremulas
         - Tamanho: 6px de altura
         - Animacao: 
           * Aparece letra por letra (F..A..K..E.. ..N..E..W..S...) 40ms por letra
           * Depois de completo, fica visivel por 300ms
           * Fade out: 100% -> 0% ao longo de 400ms
         
  350ms: MAOS -- A ironia final:
         As maos microscopicas finalmente parecem PROPORCIONAIS ao corpo
         Porque o corpo todo encolheu/murchou
         Nao e uma mudanca real de tamanho das maos -- e o CORPO ficando patetico
         
  400ms: Sprite a 40% opacity. Quase sumindo.
  
  500ms: Sprite a 0% opacity.
         Trigger: onComplete callback
         - Remover sprite do scene
         - Spawn loot (se aplicavel)
         - Trigger: sfx_victory_sting
         - Trigger: screen_effect_remove_blue_red_filter (se ultimate estava ativo)
```

---

## 5. HIT -- "Unfair Treatment"

### Dados Tecnicos
- **Sprite Sheet**: `trump_hit.png` (128x64px)
- **Frames**: 2
- **Duracao Total**: 250ms
- **Loop**: Nao (play once, retorna a animacao anterior)
- **Prioridade**: 4 (alta, interrompe walk e idle, nao interrompe death)
- **Invulnerabilidade**: 400ms apos hit (i-frames)

### Timeline Frame a Frame

| Frame | Duracao | Nome           | Eventos                                                   |
|-------|---------|----------------|-----------------------------------------------------------|
| 0     | 125ms   | hit_recoil     | Flash branco. Knockback. Dor. Maos defensivas inuteis.   |
| 1     | 125ms   | hit_recover    | RAIVA instantanea. Glow intensifica. Olhos de furia.     |

### Detalhamento do Frame 0 -- Recoil (125ms)

```
  0ms:   HIT FLASH:
         - Sprite inteiro flasha BRANCO (tint #FFFFFF) por 40ms
         - Glow da pele flasha para branco (#FFFFFF, 100% opacity)
         - Sound: sfx_hit_impact (volume 0.5)
         
  10ms:  KNOCKBACK:
         - Corpo empurrado 3px na direcao oposta ao hit
         - Implementacao: tween de posicao, 3px, 80ms, ease: 'Power2'
         - (UNICA excecao de tween -- knockback precisa de ease pra game feel)
         
  40ms:  Flash branco ACABA, sprite volta as cores normais
         Expressao: DOR
         - Olhos squeeze shut (1x1px, linhas horizontais)
         - Boca em "O" de dor
         - Queixo duplo balanca (jitter vertical 1px)
         Cabelo: hair_impact (achata na direcao do hit)
         
  50ms:  PARTICULAS -- Estrelas de dor:
         - 2 estrelas (2x2px, #FFFF00)
         - Spawn acima da cabeca, posicoes aleatorias num raio de 6px
         - Orbita circular: raio 6px, 1 rotacao em 400ms
         - Fade: 100% -> 0% ao longo de 400ms
         
  70ms:  PARTICULA -- Fio de cabelo:
         - 1 fio (1x2px, #FF8C00)
         - Spawn do topo da cabeca
         - Velocidade: 20px/s para cima-aleatoria
         - Gravidade: 60px/s²
         - Fade: 300ms
         
  80ms:  Maos microscopicas se levantam "defensivamente"
         hand_fist (ambas) -- mas tao pequenas que nao protegem NADA
         E como erguer dois grao de arroz contra uma bazuca
         
  125ms: Transicao ABRUPTA para Frame 1 (ZERO transicao suave)
```

### Detalhamento do Frame 1 -- Recovery (125ms)

```
  0ms:   TRANSICAO INSTANTANEA DE EXPRESSAO:
         O rosto PULA de dor para FURIA sem transicao intermediaria
         Estilo twitchy do Andre Guedes -- a expressao "teleporta"
         
         Nova expressao: RAIVA ABSOLUTA
         - Sobrancelhas descem ao maximo (1px acima dos olhos)
         - Olhos se estreitam (1x2px, slots horizontais de furia)
         - Boca fechada em linha fina (1px de altura)
         - Queixo projetado para frente (+1px)
         - Veias na testa (2 linhas 1px em V invertido, #CC4400)
         
  10ms:  Glow da pele INTENSIFICA:
         - Opacity pula para 60% (acima do normal de 40%)
         - Cor muda para #FF4400 (mais vermelho -- raiva)
         - Dura 200ms, depois fade suave de volta para #FFAA33 40%
         
  30ms:  Cabelo bounce:
         - Comprime 2px vertical (hair_impact aftershock)
         - Depois expande 1px alem do normal
         - Depois volta ao normal
         - Timing: comprime 30ms, expande 30ms, normaliza 65ms
         
  50ms:  Maos mudam de hand_fist para hand_tremble
         Tremem de raiva (alternancia 2x3px / 3x2px, 40ms cada)
         
  80ms:  Corpo começa a voltar a posicao pre-hit (knockback recovery)
         
  125ms: RETORNO ABRUPTO a animacao anterior (idle ou walk)
         Nao ha blend, nao ha transicao
         Invulnerabilidade de 400ms comeca (sprite pisca: 100% -> 60% -> 100% a cada 100ms)
```

---

## 6. SPECIAL: BUILD THE WALL -- "Muro de Ouro Falso"

### Dados Tecnicos
- **Sprite Sheet Personagem**: `trump_special_wall.png` (256x64px)
- **Asset do Muro**: `trump_wall.png` (128x32px, sprite separado)
- **Frames do Personagem**: 4
- **Duracao Total**: 2000ms (500ms por frame)
- **Loop**: Nao
- **Cooldown**: 15 segundos
- **Efeito**: Muro de ouro falso bloqueia passagem por 8 segundos
- **Prioridade**: 3

### Timeline Completa

```
=== FRAME 0 (0-500ms): INVOCACAO ===
  0ms:   Trampi planta os pes firmemente (power stance largo)
         Sound: sfx_trump_grunt ("Tremendous wall!")
         Maos microscopicas se estendem a frente -- parecem duas ervilhas laranja
         Glow da pele sobe para 70%
         Cabelo: hair_puff (infla com a concentracao de poder)
  200ms: Tremor no chao (particulas de poeira ao redor dos pes)
         Camera shake leve: 0.5px, 300ms
         Sound: sfx_rumble_low (volume 0.3, loop por 1500ms)
  400ms: Rachaduras aparecem no chao a frente (3 linhas 1px, #CCAA33)

=== FRAME 1 (500-1000ms): CONSTRUCAO ===
  500ms: Tijolos dourados comecam a SUBIR do chao
         - 8-12 particulas retangulares (4x3px, #DAA520)
         - Spawn: linha de 64px a frente do personagem
         - Velocidade: 40px/s para cima
         - Intervalo: 1 tijolo a cada 60ms
         - Sound: sfx_brick_place (a cada tijolo, volume crescente 0.1 -> 0.5)
  700ms: Primeira fileira do muro visivel (8px de altura)
         Trampi sorri -- boca se abre em grin enorme
  900ms: Muro a 50% de altura (16px)
         Texto "TRUMP" comeca a se formar no muro (letra por letra, dourado brilhante)

=== FRAME 2 (1000-1500ms): MURO COMPLETO ===
  1000ms: Muro atinge altura total (32px)
          ASSET DO MURO (sprite independente):
            - Dimensao: 128x32px
            - Visual: Tijolos dourados irregulares (4x3px cada, tons de dourado)
            - Texto "TRUMP" centralizado em letras gigantes (12px altura)
            - Letras: #FFD700 com borda #B8860B, estilo cafona/gaudy
            - Brilho falso: 4-6 sparkles (1px, #FFFFFF) piscando aleatoriamente
            - Cross-hatching nas sombras dos tijolos
            - Colunas decorativas nas extremidades (kitsch maximo)
          Sound: sfx_wall_complete (fanfarra brega, tipo cassino barato)
          Particulas: 8 sparkles dourados explodem ao redor do muro
          
  1200ms: Muro faz "settling" -- treme 1px para baixo e volta (bounce de assentamento)

=== FRAME 3 (1500-2000ms): ORGULHO ===
  1500ms: Trampi vira para o muro e aponta com a mao direita microscopica
          A mao e tao pequena que o gesto de "apontar" e quase invisivel
          Expressao: orgulho maximo, peito inflado, queixo levantado
          Cabelo: hair_puff maximo (+3px em todas direcoes)
          Sound: sfx_trump_tremendous ("TREMENDOUS!")
  1700ms: Trampi faz um "kiss" em direcao ao muro (boca faz biquinho)
          Micro-mao tenta fazer heart sign -- impossivel com maos de 3x3px
  2000ms: Retorna ao idle
          Muro persiste como objeto de colisao por 8 segundos
          Timer visivel: numero "8" dourado acima do muro, countdown

=== MURO -- CICLO DE VIDA (8 segundos) ===
  0-6s:  Muro intacto. Sparkles piscando. "TRUMP" visivel.
         Bloqueia movimento de TODOS (jogador e inimigos)
         HP do muro: 200 (pode ser destruido com dano)
  6-7s:  Muro comeca a RACHAR (linhas diagonais #8B6914 aparecendo)
         Sparkles param de brilhar
         Sound: sfx_crack_stone
  7-8s:  Muro desmorona
         PARTICULAS: 15-20 tijolos dourados caem (4x3px cada)
         - Gravidade: 120px/s²
         - Bounce: 1x, coeficiente 0.2
         - Fade: 500ms apos bounce
         - Letras "TRUMP" se desfazem em particulas de 1x1px
         Sound: sfx_wall_crumble
  8s:    Muro removido. Area livre novamente.
```

---

## 7. SPECIAL: FAKE NEWS PRESIDENTIAL -- "Desinformacao Total"

### Dados Tecnicos
- **Sprite Sheet**: `trump_special_fakenews.png` (256x64px)
- **Frames**: 4
- **Duracao Total**: 1500ms
- **Efeito**: Todos os textos da interface mudam para informacoes falsas por 5 segundos
- **Cooldown**: 20 segundos
- **Prioridade**: 3

### Timeline Completa

```
=== FRAME 0 (0-375ms): PEGA O CELULAR ===
  0ms:   Trampi enfia a mao microscopica no bolso do terno
         PROBLEMA: O bolso e 8px de largura, a mao e 3px -- 
         a mao se PERDE dentro do bolso por 100ms
  100ms: Mao microscopica emerge com um celular (4x6px, #333333 com tela #87CEEB)
         MAS: O celular escorrega da mao (hand_grab_fail)
         Sound: sfx_phone_fumble
         Celular cai 4px, particula de "!" acima da cabeca
  200ms: Mao tenta novamente (hand_grab_try rapido)
         Desta vez PEGA (hand_grab_success)
         Expressao: determinacao furiosa
  375ms: Celular na mao, tela virada para frente

=== FRAME 1 (375-750ms): DIGITA FAKE NEWS ===
  375ms: Tela do celular BRILHA vermelho (#FF0000)
         Sound: sfx_phone_type (digitacao rapida, 200ms)
         Maos microscopicas "digitam" -- mas os dedos sao tao pequenos
         que ele usa a mao inteira como um bloco, apertando varias teclas ao mesmo tempo
  500ms: Texto "FAKE NEWS!" aparece na tela do celular (2px de altura, vermelho no branco)
         Glow do celular irradia (2px de vermelho ao redor do aparelho)
         Sound: sfx_notification_evil (notificacao distorcida)
  650ms: Trampi ergue o celular acima da cabeca com a mao microscopica
         O celular e maior que a mao (4x6px celular vs 3x3px mao)
         Visualmente absurdo -- parece um formiga segurando uma folha

=== FRAME 2 (750-1125ms): ONDAS DE DISTORCAO ===
  750ms: Ondas de distorcao emanam do celular
         IMPLEMENTACAO:
           - 3 circulos concentricos (outline #FF0000, 1px)
           - Circulo 1: raio 8px, spawna em 750ms
           - Circulo 2: raio 8px, spawna em 850ms
           - Circulo 3: raio 8px, spawna em 950ms
           - Cada circulo EXPANDE: 8px -> 80px de raio ao longo de 800ms
           - Opacity: 80% -> 0% conforme expande
           - Quando um circulo passa por texto da UI, o texto GLITCHA
         Sound: sfx_distortion_wave (woosh eletronico, volume crescente)
  900ms: Particulas de texto falso voam das ondas:
         - "150% APPROVAL", "$999 TRILLION", "BEST EVER", "NO COLLUSION"
         - Cada texto: 3px altura, cor vermelha, fonte irregular
         - Spawn nas bordas das ondas, voam em espiral
         - Fade: 600ms
  1125ms: Ondas atingem as bordas da tela

=== FRAME 3 (1125-1500ms): SATISFACAO MALEFICA ===
  1125ms: Trampi abaixa o celular
          Sorriso ENORME -- o maior de todas as animacoes
          Boca aberta mostrando todos os dentes (7 dentes irregulares)
          Olhos fechados de auto-satisfacao (arcos 2px, formato feliz)
          Glow da pele pulsa em sincronia com o sorriso (50% -> 70% -> 50%)
          Cabelo: hair_puff (ego no auge)
  1300ms: Mao microscopica guarda o celular (tenta -- o celular escorrega 2 vezes)
          Hand_grab_fail, hand_grab_fail, finalmente cai no bolso por gravidade
  1500ms: Retorna ao idle
  
=== EFEITO NA UI (5 segundos) ===
  Todos os textos da interface mudam para informacoes falsas:
  - Score "1.337" -> "999.999.999 (BIGGEST EVER)"
  - HP "75/100" -> "100/100 (PERFECT HEALTH)"
  - Timer "2:30" -> "FOREVER (TIME IS FAKE)"
  - Nome do inimigo -> "VERY BAD HOMBRE"
  - Dano recebido "15" -> "0 (NO DAMAGE BELIEVE ME)"
  - Textos da UI piscam entre vermelho e dourado a cada 500ms
  - Apos 5s: textos fazem glitch (200ms) e voltam ao normal
  Sound durante efeito: sfx_news_ticker_loop (loop de 5s)
```

---

## 8. SPECIAL: SANCAO ECONOMICA -- "Executive Debuff"

### Dados Tecnicos
- **Sprite Sheet**: `trump_special_sancao.png` (256x64px)
- **Frames**: 4
- **Duracao**: 1200ms
- **Efeito**: Debuff de velocidade -30% no jogador por 5 segundos
- **Cooldown**: 12 segundos
- **Prioridade**: 3

### Timeline Completa

```
=== FRAME 0 (0-300ms): ASSINA DECRETO ===
  0ms:   Mesa executiva aparece a frente do Trampi (prop sprite 24x12px, madeira)
         Trampi se inclina sobre a mesa
         Mao microscopica tenta segurar uma caneta dourada (1x4px, #FFD700)
         A caneta e maior que a mao inteira
         hand_grab_try -- FALHA INICIAL, caneta rola pela mesa
  100ms: hand_grab_try novamente -- SUCESSO (mas precario, caneta torta na mao)
         Sound: sfx_pen_scratch
  200ms: Trampi "assina" com movimentos exagerados da mao microscopica
         Rabisco dourado aparece no documento (3 linhas onduladas irregulares)
         Expressao: concentracao absoluta, lingua para fora (esforco)

=== FRAME 1 (300-600ms): DECRETO VOA ===
  300ms: Trampi levanta o documento assinado (8x6px, #F5F5DC com texto e selo)
         SELO DOURADO: circulo 3x3px, #FFD700, com "T" no centro
         Documento sai das maos (finalmente algo que as maos microscopicas LANCAM bem
         -- porque soltar e mais facil que segurar)
  400ms: Documento voa em direcao ao alvo (jogador)
         Velocidade: 120px/s, trajetoria em arco
         Rotacao: 180deg/s
         Trail: 2 particulas de sparkle dourado atras
         Sound: sfx_paper_whoosh
         Mesa some (fade 200ms)

=== FRAME 2 (600-900ms): CORRENTES ECONOMICAS ===
  600ms: Documento atinge o alvo (ou area do alvo)
         EFEITO DE IMPACTO:
           - Selo dourado "explode" em 4 correntes (sprites 4x4px cada, #B8860B)
           - Correntes se ENROSCAM ao redor do alvo (rotacao orbital, 4 direcoes)
           - Cada corrente faz 1 volta completa em 300ms
           - Sound: sfx_chains_rattle
         Texto flutuante no alvo: "SANCTIONED!" (#CC0000, 4px, bold irregular)
  800ms: Correntes se apertam (raio da orbita diminui de 16px para 8px)
         Alvo comeca a brilhar com tint azulado (#4444FF, 20% overlay)

=== FRAME 3 (900-1200ms): DEBUFF APLICADO ===
  900ms: Correntes SOMEM com flash (correntes -> particulas 1x1px douradas)
         Alvo fica com aura de "sanctioned":
           - Outline azulado piscante (1px, #4444AA, pisca a cada 300ms)
           - Icone de velocidade reduzida acima do alvo (setinha para baixo, vermelha)
           - Texto "-30% SPD" (3px altura, vermelho)
         Trampi cruza os bracos (na medida do possivel com maos microscopicas)
         Expressao: satisfacao corporativa, sorriso de CEO
         Sound: sfx_debuff_apply
  1200ms: Retorna ao idle
          Debuff persiste por 5 segundos no alvo
          Visual do debuff no alvo: aura azulada + icone de velocidade reduzida

=== DEBUFF ATIVO (5 segundos no alvo) ===
  - Velocidade de movimento: -30%
  - Visual: outline azulado piscante, particulas de "$" caindo do personagem
  - Particulas "$": spawn 1 por segundo, 2x3px, #4444AA, cai 20px, fade 400ms
  - Sound: sfx_economy_drain (loop sutil, 5s)
  - Ao expirar: Flash verde (#44FF44) no alvo, sound: sfx_debuff_end
```

---

## 9. ULTIMATE: AMERICA FIRST -- "Bombardeio OTAN"

### Dados Tecnicos
- **Sprite Sheet Personagem**: `trump_special_ultimate.png` (512x64px)
- **Assets Adicionais**:
  - `trump_eagle.png` (32x32px, aguia de aco dourado, 4 frames de voo)
  - `trump_flag.png` (16x32px, bandeira americana, 3 frames de ondulacao)
  - `trump_ultimate_overlay.png` (tela cheia, filtro azul-vermelho)
- **Frames do Personagem**: 8
- **Duracao Total**: 5000ms (625ms por frame)
- **Loop**: Nao
- **Cooldown**: 60 segundos (ultimate, 1 vez por luta idealmente)
- **Dano**: 60 HP em TODA A TELA (area attack)
- **Prioridade**: 5 (maxima)

### Pre-Condicao
- HP do Trampi abaixo de 30%
- OU depois de 90 segundos de luta
- OU quando um threshold de dano e atingido

### Timeline Completa

```
=== FRAME 0 (0-625ms): INVOCACAO -- "AMERICA..." ===
  0ms:   CUTSCENE MINI: Tela escurece nas bordas (vinheta preta, 20% opacity)
         Trampi para qualquer acao atual
         Gameplay PAUSA por 300ms (dramatic pause)
         Sound: sfx_dramatic_drum (tambor grave, 1 batida)
         
  300ms: Trampi levanta AMBAS as maos microscopicas para o ceu
         As maos sao tao pequenas que o gesto e PATETICO
         Parecem dois pontos laranja flutuando acima de um terno dourado
         MAS a energia e REAL -- o chao comeca a tremer
         Camera shake: 1px, constante, durante todo o ultimate
         Sound: sfx_trump_scream ("AMERICAAAA...")
         Cabelo: hair_puff MAXIMO -- o maior que fica em todo o jogo
         Glow da pele: 100% opacity, cor #FFAA33 pura
         
  500ms: Rachaduras no chao ao redor do Trampi (6-8 linhas irradiando)
         Particulas de detritos comecam a subir (gravidade reversa)
         Sound: sfx_rumble_crescendo (volume 0.3 -> 0.7 ao longo de 3s)

=== FRAME 1 (625-1250ms): CEU ESCURECE ===
  625ms: FILTRO AZUL-VERMELHO começa:
         - Overlay de tela cheia
         - Metade esquerda: tint azul #0000AA, 15% opacity
         - Metade direita: tint vermelho #AA0000, 15% opacity
         - A divisao "pulsa" -- a linha central se move 10px esquerda-direita, 500ms ciclo
         Sound: sfx_anthem_distorted (hino americano distorcido comeca, loop de 10s)
         - O hino e PROPOSITALMENTE desafinado e distorcido
         - Como se tocasse num alto-falante barato estourando
         
  800ms: Ceu escurece (background tint -30% brightness)
         Nuvens vermelho-escuras se formam (3-4 sprites de nuvem, 32x16px, #882222)
         Nuvens se movem em espiral lenta ao redor de um ponto central
         
  1000ms: Silhuetas de AGUIAS aparecem no ceu (3 sprites distantes, 8x8px, #443300)
          Sound: sfx_eagle_distant (grito de aguia ao longe)
          Trampi continua com as maos para cima, tremendo de energia
          Veias saltam na testa e pescoco (3-4 linhas 1px, #CC4400)

=== FRAME 2 (1250-1875ms): AGUIAS DESCEM ===
  1250ms: AGUIAS DE ACO DOURADO:
          - 3 aguias (sprite 32x32px cada)
          - Visual: Aguias mecanicas/steampunk, aco dourado (#DAA520 corpo, #FFD700 asas)
          - Detalhes: Olhos vermelhos (#FF0000, 2x2px), garras exageradas, asas abertas
          - Cross-hatching no corpo (textura metalica suja)
          - Estilo: mais maquinas de guerra grotescas que passaros elegantes
          
          Aguia 1: Spawna topo-esquerda, desce em diagonal ate centro-esquerda
          Aguia 2: Spawna topo-centro, desce vertical ate o centro
          Aguia 3: Spawna topo-direita, desce em diagonal ate centro-direita
          
          Velocidade de descida: 60px/s
          Animacao de voo: 4 frames, 100ms cada (asas batendo)
          Trail: particulas douradas (1x1px, #FFD700, 3 por aguia, fade 200ms)
          Sound: sfx_eagle_screech x3 (defasados 200ms entre si)
          
  1600ms: Aguias atingem nivel do jogador
          EXPLOSOES no ponto de impacto de cada aguia:
          - Starburst azul-branco-vermelho (3 cores alternantes)
          - Raio: 24px expandindo para 48px
          - 8-12 particulas de detritos por explosao
          - Camera shake: 4px, 300ms
          - Sound: sfx_explosion_patriotic (explosao com reverb majestoso)
          DANO: 20 HP por aguia (60 total se todas acertam)

=== FRAME 3 (1875-2500ms): EXPLOSOES PATRIOTICAS ===
  1875ms: Starbursts persistem e MULTIPLICAM:
          - 6 explosoes menores ao redor das originais
          - Cores: #0000FF, #FFFFFF, #FF0000 (rotacionam a cada 100ms por explosao)
          - Particulas: estrelas 5-pontas (3x3px) em vez de circulos
          - Shrapnel dourado (2x1px, #DAA520) voa em todas direcoes
          
  2100ms: BANDEIRAS AMERICANAS brotam do chao:
          - 5-8 bandeiras (sprite 16x32px cada)
          - Spawn: posicoes semi-aleatorias no mapa visivel
          - Animacao: brotar do chao em 200ms (scale Y: 0% -> 100%)
          - Depois: ondular (3 frames de ondulacao, loop)
          - Visual: bandeira americana com listras e estrelas (grotesca, mal desenhada)
          - As listras sao TORTAS, as estrelas sao IRREGULARES
          - Sound: sfx_flag_plant x5 (defasados 100ms)
          
  2300ms: Trampi se coloca em POWER POSE suprema
          Bracos abertos (na medida do possivel com maos microscopicas)
          Cabelo esvoaca ao vento das explosoes
          Gravata horizontal pelo vento
          Glow: 100%, pulsando

=== FRAME 4 (2500-3125ms): BANDEIRAS E DESTRUICAO ===
  2500ms: Mais bandeiras brotam (total de 12-15 no mapa)
          Chao racha onde cada bandeira brota
          Detritos voam de cada ponto de spawn
          EFEITO DE "PATRIOTISMO FORCADO":
          - Texto gigante "AMERICA FIRST" preenche o centro da tela
          - Letras: 12px de altura cada, #FFD700, outline #B8860B
          - Estilo: maquina de escrever burocrática, mas ENORME
          - Tremor nas letras: jitter aleatorio de 1px por letra
          - Sound: sfx_typewriter_giant (cada letra com som de maquina de escrever)
          
  2800ms: Texto "AMERICA FIRST" atinge opacidade maxima
          Flash de tela: branco 30% por 100ms
          Trampi no centro, imovel, pose de poder absoluto

=== FRAME 5 (3125-3750ms): VENTO DA DESTRUICAO ===
  3125ms: Vento horizontal forte ASSOLA a tela (esquerda para direita)
          EFEITOS DO VENTO:
          - Cabelo do Trampi estica 6px para a direita (deformacao maxima)
          - Gravata horizontal, estralando
          - Abas do terno voam
          - Bandeiras ondulam violentamente
          - Particulas de poeira/detritos voam horizontalmente (20-30 particulas 1x1px)
          - Todos os sprites menores se movem 2px para a direita
          Sound: sfx_wind_apocalyptic (volume 0.8)
          
  3400ms: Trampi RESISTE ao vento (power stance, inclinado para a esquerda contra o vento)
          Maos microscopicas tentam segurar o cabelo -- FALHAM
          hand_grab_try -> hand_grab_fail (cabelo e grande demais para maos tao pequenas)
          Expressao: determinacao insana, dentes cerrados, veias na testa

=== FRAME 6 (3750-4375ms): FLASH MAXIMO ===
  3750ms: FLASH BRANCO CRESCENTE:
          - Tela inteira faz fade para branco
          - 0ms: 20% branco
          - 200ms: 50% branco
          - 400ms: 80% branco (quase tudo invisivel)
          - So o Trampi permanece visivel como silhueta dourada
          Sound: sfx_flash_crescendo (som crescente agudo)
          
  4000ms: PICO: Tela 90% branca
          DANO ADICIONAL: 15 HP em todos os inimigos visiveis (dano de flash)
          
  4200ms: Flash comeca a recuar:
          - 80% -> 50% -> 20% -> 0% ao longo de 400ms
          Sound: sfx_flash_fade (reverb decrescente)

=== FRAME 7 (4375-5000ms): AFTERMATH ===
  4375ms: Tela limpa. O ESTRAGO:
          - Marcas de explosao no chao (sprites 8x8px, crateras, 3-5 no mapa)
          - Bandeiras permanecendo (fade lento ao longo de 10s)
          - Penas de aguia dourada caindo (6-8 particulas, 2x4px, #DAA520)
          - Penas: caem lentamente (20px/s), rotacao 90deg/s, fade 2000ms
          
  4500ms: Trampi em VICTORY POSE:
          - Bracos cruzados (maos microscopicas segurando os cotovelos -- ou tentando)
          - Smirk supremo: sorriso mais largo do jogo inteiro
          - Queixo levantado 2px, olhando de cima
          - Cabelo: hair_puff medio (voltando ao normal gradualmente)
          - Glow: fade de 100% para 40% ao longo de 2000ms
          Sound: sfx_trump_tremendous ("TREMENDOUS! AMERICA FIRST, baby!")
          
  4700ms: Filtro azul-vermelho comeca fade out (10s total para desaparecer completamente)
          Hino distorcido faz fade out (3s)
          Textura de fumaça leve no ar (overlay, 5% opacity, dissipa em 5s)
          
  5000ms: Retorna ao idle. Ultimate completo.
          Cooldown de 60s inicia.

=== FILTRO AZUL-VERMELHO POS-ULTIMATE (10 segundos) ===
  O filtro permanece APOS o ultimate:
  0-3s:  Intensidade 15% (como durante o ultimate)
  3-7s:  Fade gradual para 8%
  7-9s:  Fade para 3%
  9-10s: Fade para 0%, desaparece
  Durante todo o periodo: hino distorcido continua em volume decrescente
```

---

## 10. ANIMACAO ESPECIAL: MICRO-MAOS FUMBLING

### Gatilhos e Contexto

A animacao de "maos fumbling" nao e uma animacao separada -- e um SISTEMA que se aplica a qualquer momento em que o Trampi interage com objetos.

```
SISTEMA DE FUMBLE DAS MAOS MICROSCOPICAS:

Toda vez que Trampi precisa SEGURAR algo:
  1. Roll aleatorio: 50% chance de falha no primeiro grab
  2. Se FALHA:
     a. hand_grab_try (40ms)
     b. hand_grab_fail (40ms) -- objeto escorrega/cai
     c. Particula: objeto cai 4px com gravidade
     d. Sound: sfx_fumble_drop (plim comico)
     e. Delay: 80ms (pausa de "frustacao")
     f. hand_grab_try novamente (40ms)
     g. hand_grab_success (sempre sucede na segunda tentativa)
     h. Sound: sfx_fumble_catch (pega!)
  3. Se SUCEDE de primeira:
     a. hand_grab_success direto
     b. Sem delay

OBJETOS AFETADOS:
  - Taco de golfe (attack): 50% fumble
  - Celular (Fake News): 50% fumble
  - Caneta (Sancao): 50% fumble
  - Gravata (idle adjust): 100% fumble (SEMPRE falha com a gravata)
  - Aba do terno (walk): 100% fumble
  - Cabelo no vento (ultimate): 100% fumble

REGRA DE OURO: As maos NUNCA parecem adequadas para a tarefa.
Mesmo quando seguram algo, deve parecer precario, a ponto de soltar.
```

---

## 11. TRANSICOES ENTRE ANIMACOES

```
MAPA DE TRANSICOES (todas ABRUPTAS, zero blend):

idle -> walk:     Instantaneo (0ms blend)
idle -> attack:   Instantaneo
idle -> special:  Instantaneo
idle -> hit:      Instantaneo
idle -> death:    Instantaneo

walk -> idle:     Instantaneo (no frame atual, corta)
walk -> attack:   Instantaneo
walk -> hit:      Instantaneo
walk -> death:    Instantaneo

attack -> idle:   Apos ultimo frame do attack (sem blend)
attack -> hit:    INTERROMPE attack imediatamente
attack -> death:  INTERROMPE attack imediatamente

hit -> idle:      Apos ultimo frame do hit (sem blend)
hit -> walk:      Apos ultimo frame do hit
hit -> death:     Imediato (se HP chega a 0 durante hit)

special -> idle:  Apos ultimo frame do special
special -> death: INTERROMPE special (unica interrupcao possivel)
special -> hit:   NAO INTERROMPE (super armor durante specials)

death -> nada:    Death e terminal. Sprite removido apos fade.

PRIORIDADES:
  0: idle
  1: walk
  2: (reservado)
  3: attack, specials
  4: hit
  5: death, ultimate (nao interrompiveis exceto por morte)
```

---

## 12. SONS REFERENCIADOS (Lista para Audio Agent)

| Chave SFX                | Descricao                                    | Duracao  |
|--------------------------|----------------------------------------------|----------|
| sfx_step_heavy_1         | Passo pesado de boss (pe direito)            | 150ms    |
| sfx_step_heavy_2         | Passo pesado de boss (pe esquerdo)           | 150ms    |
| sfx_swoosh_start         | Inicio de swing                              | 200ms    |
| sfx_golf_swing           | Swing do taco de golfe                       | 300ms    |
| sfx_tremendous           | Voz: "TREMENDOUS!"                           | 600ms    |
| sfx_fakenews             | Voz: "FAKE NEWS!"                            | 500ms    |
| sfx_trump_scream         | Grito dramatico                              | 800ms    |
| sfx_trump_grunt          | Grunhido de esforco                          | 300ms    |
| sfx_trump_tremendous     | Voz: "TREMENDOUS!" (versao longa, celebracao)| 1200ms   |
| sfx_death_hit            | Impacto de golpe fatal                       | 400ms    |
| sfx_heavy_thud           | Corpo caindo no chao                         | 500ms    |
| sfx_coins_scatter        | Botoes/moedas espalhando                     | 600ms    |
| sfx_suit_rip             | Tecido rasgando                              | 300ms    |
| sfx_tooth_ping           | Dente pingando no chao                       | 200ms    |
| sfx_sad_trombone         | Wah wah wah                                  | 1500ms   |
| sfx_hit_impact           | Impacto de dano generico                     | 200ms    |
| sfx_fumble_drop          | Objeto caindo da mao (plim comico)           | 250ms    |
| sfx_fumble_catch         | Conseguiu pegar (pega!)                      | 150ms    |
| sfx_phone_fumble         | Celular escorregando                         | 300ms    |
| sfx_phone_type           | Digitacao rapida                             | 200ms    |
| sfx_notification_evil    | Notificacao distorcida                       | 300ms    |
| sfx_distortion_wave      | Onda de distorcao                            | 500ms    |
| sfx_news_ticker_loop     | Ticker de noticias (loop)                    | 5000ms   |
| sfx_pen_scratch          | Caneta assinando                             | 400ms    |
| sfx_paper_whoosh         | Documento voando                             | 300ms    |
| sfx_chains_rattle        | Correntes economicas                         | 500ms    |
| sfx_debuff_apply         | Debuff aplicado                              | 300ms    |
| sfx_economy_drain        | Drenagem economica (loop)                    | 5000ms   |
| sfx_debuff_end           | Debuff termina                               | 200ms    |
| sfx_rumble_low           | Tremor grave (loop)                          | 1500ms   |
| sfx_brick_place          | Tijolo colocado                              | 150ms    |
| sfx_wall_complete        | Fanfarra brega                               | 1000ms   |
| sfx_crack_stone          | Rachaduras em pedra                          | 400ms    |
| sfx_wall_crumble         | Muro desmoronando                            | 800ms    |
| sfx_dramatic_drum        | Tambor grave                                 | 500ms    |
| sfx_anthem_distorted     | Hino americano distorcido (loop)             | 10000ms  |
| sfx_eagle_distant        | Grito de aguia distante                      | 800ms    |
| sfx_eagle_screech        | Grito de aguia proximo                       | 600ms    |
| sfx_explosion_patriotic  | Explosao patriotica                          | 700ms    |
| sfx_flag_plant           | Bandeira plantada no chao                    | 300ms    |
| sfx_wind_apocalyptic     | Vento apocaliptico                           | 2000ms   |
| sfx_flash_crescendo      | Flash crescente                              | 600ms    |
| sfx_flash_fade           | Flash diminuindo                             | 400ms    |
| sfx_typewriter_giant     | Maquina de escrever (por letra)              | 100ms    |
| sfx_victory_sting        | Vitoria (pos-morte do boss)                  | 1500ms   |
