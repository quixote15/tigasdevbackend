# LULA (O Cachaceiro) -- Animation Specification
### Boss Principal (Lado Esquerdo) | Zumbis de Brasilia
### Motor: Phaser 3 | Estilo: Andre Guedes (Jerky/Twitchy)

---

## Principios Gerais de Animacao

### Estilo Andre Guedes -- Regras de Movimento
1. **NUNCA suave.** Todas as transicoes sao abruptas, twitchy, com micro-pauses.
2. **Sem easing bezier.** Usar linear ou step() para transicoes. Se easing for necessario, usar easeInQuad (agressivo, nao suave).
3. **Deformacao organica**: Partes moles do corpo (barriga, bochechas, nariz) usam squash & stretch EXAGERADO, partes rigidas (ossos, placa de titanio) nao.
4. **Assimetria SEMPRE**: Nenhum frame e simetrico. Corpo sempre inclinado, ombros desiguais, pes em angulos diferentes.
5. **Overshoot em tudo**: Quando para, vai 1-2px alem e volta. Quando gira, gira demais e corrige.
6. **Frame rate deliberadamente baixo**: 8-12fps para animacoes normais, 5fps para animacoes dramaticas (morte, ultimate). O "jerkiness" e INTENCIONAL.

### Configuracao Phaser 3
```javascript
// Constantes de animacao para Lula
const LULA_ANIM_CONFIG = {
  idle: { frameRate: 8, repeat: -1, yoyo: true },
  walk: { frameRate: 10, repeat: -1, yoyo: false },
  attack: { frameRate: 8, repeat: 0, yoyo: false },
  death: { frameRate: 5, repeat: 0, yoyo: false },
  hit: { frameRate: 10, repeat: 0, yoyo: false },
  special_fato: { frameRate: 8, repeat: 0, yoyo: false },
  special_dedo: { frameRate: 10, repeat: 0, yoyo: false },
  special_mandato: { frameRate: 5, repeat: 0, yoyo: false },
  special_fazol: { frameRate: 5, repeat: 0, yoyo: false },
  ultimate_discurso: { frameRate: 5, repeat: 0, yoyo: false },
};
```

---

## IDLE ANIMATION

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 125 | 125 | Posicao neutra bebada |
| 2 | 125 | 250 | Oscilacao direita, garrafa sobe |
| 3 | 125 | 375 | Arroto, nuvem de gas |
| 4 | 125 | 500 | Sossego momentaneo |
| 3* | 125 | 625 | Retorno (yoyo) |
| 2* | 125 | 750 | Retorno (yoyo) |

**Ciclo total**: 750ms (yoyo), loop infinito

### Easing por Elemento
- **Corpo (oscilacao lateral)**: `Phaser.Math.Easing.Stepped` -- pula entre posicoes, sem interpolacao.
- **Garrafa (subida/descida)**: `linear` -- movimento mecanico de mao de bebado.
- **Nariz (pulsacao)**: Independente do frame -- tint overlay que pulsa a cada 400ms entre #CC3333 e #DD3333. Usar `scene.tweens.add({ targets: nose_overlay, alpha: { from: 0.7, to: 1.0 }, duration: 400, yoyo: true, repeat: -1 })`.
- **Barriga (respiracao)**: Scale Y oscila entre 1.0 e 1.03 em sincronia com frames (expande no frame 2, contrai no frame 3).

### Particulas
- **Nuvem de arroto (Frame 3)**: Emitter burst de 3-5 particulas.
  - Textura: 2x2px amarelo-esverdeado (#99AA44)
  - Velocidade: 10-20 px/s, direcao: para cima e levemente para frente
  - Lifetime: 300ms
  - Alpha: fade de 0.8 a 0.0
  - Gravidade: -10 (sobe)

### Sons Sincronizados
| Frame | Som | Arquivo | Volume | Descricao |
|-------|-----|---------|--------|-----------|
| 2 | Gole de cachaca | `sfx/lula_gole.ogg` | 0.3 | Som de liquido sendo bebido, "glug" |
| 3 | Arroto | `sfx/lula_arroto.ogg` | 0.4 | Arroto curto e satisfeito |
| 4 | Suspiro | `sfx/lula_suspiro.ogg` | 0.2 | "Ahh" de contentamento |

### Eventos Aleatorios durante Idle
- **A cada 5-8s** (random): Lula murmura um bordao. Escolha aleatoria de:
  - `bordoes/lula_eu_quero_dizer.ogg` (0.3 vol)
  - `bordoes/lula_ta_maravilhoso.ogg` (0.3 vol)
  - `bordoes/lula_companheiro.ogg` (0.3 vol)
- **A cada 10-15s** (random): Lula faz um micro-tropeco (interrompe idle por 200ms com body tilt extra de 5 graus e volta).

---

## WALK ANIMATION

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 100 | 100 | Passo esquerdo levanta |
| 2 | 100 | 200 | Passo esquerdo pousa -- impacto |
| 3 | 100 | 300 | Transferencia de peso |
| 4 | 100 | 400 | Passo direito levanta |
| 5 | 100 | 500 | Passo direito pousa -- impacto |
| 6 | 100 | 600 | Tropeco leve |

**Ciclo total**: 600ms, loop infinito

### Easing por Elemento
- **Corpo (lateral oscillation)**: Sem easing -- step entre posicoes. Oscilacao lateral de +/-3px a cada frame.
- **Barriga (jiggle)**: `Phaser.Math.Easing.Bounce.Out` no frame de impacto (2 e 5). Scale Y: 1.00 -> 1.05 -> 1.00 em 100ms.
- **Garrafa (swing)**: Rotacao pendular de -15 a +15 graus em sincronia com bracos.
- **Gravata (fly)**: Rotacao de -10 a +10 graus, OPOSTA ao corpo (inercia).
- **Cabeca (lag)**: Posicao X da cabeca atrasa 1 frame em relacao ao corpo (follow delay).

### Particulas
- **Poeira de passo (Frames 2 e 5)**: Emitter burst no pe que toca o chao.
  - Textura: 1x1px marrom (#5C3317)
  - Quantidade: 2-4 particulas
  - Velocidade: 5-15 px/s, direcao radial do pe
  - Lifetime: 200ms
  - Alpha: fade 0.6 a 0.0

- **Respingos de cachaca (Frame 6 -- tropeco)**: Emitter burst na garrafa.
  - Textura: 1x1px marrom-dourado (#CC8833)
  - Quantidade: 2-3 particulas
  - Velocidade: 15-25 px/s, direcao para cima
  - Lifetime: 250ms
  - Alpha: fade 0.8 a 0.0
  - Gravidade: 50 (cai apos subir)

### Sons Sincronizados
| Frame | Som | Arquivo | Volume | Descricao |
|-------|-----|---------|--------|-----------|
| 2 | Passo pesado L | `sfx/passo_pesado_1.ogg` | 0.3 | Thud grave de sapato no chao |
| 5 | Passo pesado R | `sfx/passo_pesado_2.ogg` | 0.25 | Thud levemente mais leve |
| 6 | Tropeco | `sfx/lula_tropeco.ogg` | 0.2 | Scuff + "opa" abafado |
| 1-6 | Tinido de garrafa | `sfx/garrafa_tink.ogg` | 0.1 | Loop continuo baixo do vidro batendo |

### Movimento Real (Gameplay)
- Velocidade base: 48 px/s (LENTO -- e um bebado de terno gordo)
- Velocidade buff (pos-Quarto Mandato): 60 px/s (+25%)
- Hitbox de colisao durante walk: 24x32px (centro inferior do sprite)
- Path: nunca em linha perfeitamente reta -- adicionar wobble sinusoidal de +/-2px perpendicular a direcao de movimento. `offset_x = Math.sin(time * 3) * 2`

---

## ATTACK ANIMATION -- "Cachaçada Companheira"

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 150 | 150 | Wind-up: garrafa sobe |
| 2 | 100 | 250 | Arremesso: garrafa sai |
| 3 | 125 | 375 | Follow-through |

**Duracao total**: 375ms, nao repete

### Sequencia de Eventos Detalhada

#### T=0ms -- Inicio do Wind-Up
- Corpo rotaciona (sprite troca para attack_frame_1)
- Camera: micro-shake 1px por 50ms (anticipation)
- Som: `sfx/lula_grunt_arremesso.ogg` (vol 0.4) -- grunhido de esforco

#### T=150ms -- Arremesso
- Sprite troca para attack_frame_2
- **SPAWN DO PROJETIL**: Objeto `GarrafaVelhoBarreiro` criado na posicao da mao direita de Lula
  - Velocidade: 180 px/s na direcao do alvo
  - Rotacao: 360 graus/s (girando no ar)
  - Trail: emitter de gotículas de cachaca atras (2 part/frame, #CC8833, lifetime 150ms)
  - Sprite do projetil: 8x12px (garrafa em voo)
- Som: `sfx/garrafa_whoosh.ogg` (vol 0.5) -- whoosh de arremesso
- Bordao (30% chance): `bordoes/lula_companheiro_alcool.ogg` (vol 0.6) -- "Companheiro alcool em mim!"

#### T=250ms -- Follow-Through
- Sprite troca para attack_frame_3
- Lula desequilibrado -- nao pode se mover por 200ms (recovery)

#### T=250-600ms -- Projetil em Voo (paralelo ao recovery de Lula)
- Garrafa viaja ate o ponto de impacto
- Trail de cachaca diminuindo

#### IMPACTO DO PROJETIL (quando garrafa atinge alvo ou chao)
- **Explosao**:
  - Sprite de explosao: 16x16px, 3 frames a 12fps (flash -> fogo -> dissipacao)
  - Particulas de vidro: 4-6 shards (#2A5A2A), velocidade 40-80 px/s radial, lifetime 400ms, gravidade 60
  - Particulas de fogo: 6-10 (#CC6600, #FFAA33), velocidade 20-40 px/s radial, lifetime 300ms
  - Particulas de cachaca: 4-8 (#CC8833), velocidade 30-60 px/s, lifetime 350ms
- **Poça de cachaca** (hazard): Spawn no ponto de impacto
  - Tamanho: 16x8px (elipse top-down)
  - Duracao: 4000ms antes de evaporar
  - Efeito em inimigos que pisam: controles invertidos por 3000ms ("bebados")
  - Animacao da poca: flame flicker (alpha oscila 0.3-0.7 a cada 200ms), chamas azuladas (#4466CC)
- **Screen shake**: 3px por 150ms
- **Som**: `sfx/garrafa_quebra_explosao.ogg` (vol 0.7) -- vidro quebrando + whoosh de fogo

### Cooldown
- 2500ms entre ataques
- Durante cooldown: Lula pega "nova garrafa" (animacao rapida de 200ms de mao entrando no bolso do terno e saindo com garrafa)

### Area de Dano
- Ponto de impacto: raio de 24px
- Dano no centro: 35 HP
- Dano na borda: 15 HP
- Dano da poca (por segundo): 5 HP

---

## DEATH ANIMATION

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 200 | 200 | Impacto + recoil |
| 2 | 200 | 400 | Queda lenta |
| 3 | 200 | 600 | Impacto no chao |
| 4 | 200 | 800 | Morto (ou trigger Quarto Mandato) |

**Duracao total**: 800ms, nao repete

### Sequencia de Eventos Detalhada

#### T=0ms -- Impacto
- Sprite troca para death_frame_1
- Camera: shake 4px por 200ms
- Time scale: 0.7 (slow motion leve -- morte dramatica)
- Som: `sfx/lula_impacto_death.ogg` (vol 0.6) -- thud de corpo + "UGH"
- Garrafa voa: spawn objeto `garrafa_solta` com velocidade 60px/s para cima-direita, gravidade 100
- Particulas de sangue: 3-5 (#8B1A1A), direcao oposta ao dano, velocidade 30-50px/s, lifetime 300ms

#### T=200ms -- Queda
- Sprite troca para death_frame_2
- Time scale volta a 1.0
- Garrafa_solta: continua em arco parabolico
- Som: `bordoes/lula_companheiro_murmur.ogg` (vol 0.2) -- "companheiro..." murmurado
- Tween: alpha do sprite oscila 1.0 -> 0.9 -> 1.0 (flicker de "quase apagando")

#### T=400ms -- Impacto no Chao
- Sprite troca para death_frame_3
- Camera: shake 2px por 100ms
- Garrafa_solta: impacta o chao -- sprite de estilhaco (4x4px cacos + poca)
- Som: `sfx/corpo_no_chao.ogg` (vol 0.5) -- thud pesado
- Som: `sfx/garrafa_quebra.ogg` (vol 0.4) -- vidro quebrando (atrasado 50ms)
- Particulas de poeira: burst circular, 8-12 particulas (#8B7355), 15-30px/s, lifetime 400ms
- Estrelinhas: 3 objetos animados (#FFCC00, 2x2px) orbitando a cabeca por 500ms

#### T=600ms -- Estado Final
- Sprite troca para death_frame_4
- Time scale: normal
- Estrelinhas: desaceleram e somem
- Poca de cachaca: expande lentamente (cresce 1px a cada 200ms por 2s)

#### T=800ms -- Check Quarto Mandato
- **SE `mandato_count < 3`**:
  - Flash dourado (#FFCC22) por 200ms
  - Transicao para Special: Quarto Mandato (ver abaixo)
  - `mandato_count++`
- **SE `mandato_count >= 3`**:
  - Lula permanece morto
  - Tween: alpha de 1.0 a 0.3 em 2000ms (fade parcial)
  - Spawn: poça permanente de cachaca no local
  - Som (1500ms apos morte): `bordoes/lula_culpa_bolsonaro.ogg` (vol 0.3, eco/reverb) -- "A culpa e do Bolsonaro..." como fantasma

---

## HIT ANIMATION

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 80 | 80 | Flash branco + knockback |
| 2 | 120 | 200 | Reacao de raiva |

**Duracao total**: 200ms, nao repete, retorna a animacao anterior

### Sequencia de Eventos Detalhada

#### T=0ms -- Flash
- Sprite troca para hit_frame_1 (OU: usa tint branco no sprite atual)
- Implementacao alternativa: `sprite.setTintFill(0xFFFFFF)` por 80ms
- Knockback: tween da posicao de Lula 3px na direcao oposta ao dano, duracao 80ms, ease `Quad.Out`
- Som: `sfx/hit_flesh.ogg` (vol 0.5) -- impacto em corpo gordo
- Particulas: 3-4 pixels (#CC0000) do ponto de impacto, velocidade 40-60px/s, lifetime 200ms
- Invencibilidade: 200ms (i-frames)

#### T=80ms -- Raiva
- Sprite troca para hit_frame_2 (ou remove tint)
- Tint residual: `sprite.setTint(0xFF8888)` por 120ms, depois limpa
- Som (50% chance): `bordoes/lula_fico_puto.ogg` (vol 0.5) -- "Fico puto da vida!"
- Knockback: desacelera e para
- Barriga: tween scale 1.0 -> 1.05 -> 1.0 em 100ms (inflate de raiva)

#### T=200ms -- Retorno
- Remove todos os tints
- Retorna a animacao anterior (idle/walk)
- Lula pode agir novamente

### Mecanica Especial: Cirurgia Craniana
- **SE dano veio de HEADSHOT (hitbox superior)**:
  - Dano reduzido em 80%
  - Som diferente: `sfx/titanio_clank.ogg` (vol 0.6) -- som metalico de bala/golpe em placa de titanio
  - Particula especial: spark (#B0C0D0) no ponto de impacto, 2-3 particulas
  - Flash: cor da placa (#8090A0) em vez de branco
  - Texto flutuante: "-80% PLACA DE TITANIO" (dano UI)
  - O Lula NAO faz expressao de dor -- faz sorriso de malandro ("Essa cicatriz e do povo, companheiro")

---

## SPECIAL 1: "Fato Alternativo"

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 125 | 125 | Preparacao -- se endireita |
| 2 | 125 | 250 | Apontamento para o jogador |
| 3 | 100 | 350 | Onda de distorcao |
| 4 | 100 | 450 | Poder ativado |
| 5 | 100 | 550 | Sustentacao |
| 6 | 100 | 650 | Fim da animacao (efeito continua) |

**Duracao da animacao**: 650ms
**Duracao do EFEITO**: 5000ms apos frame 4

### Sequencia de Eventos

#### T=0ms -- Preparacao
- Lula para de cambalar (pela primeira vez, fica quase reto)
- Garrafa transferida para debaixo do braco
- Som: `sfx/lula_dramatic_pause.ogg` (vol 0.3) -- pausa dramatica, silencio subito

#### T=125ms -- Apontamento
- Mao esquerda (4 dedos) aponta para a camera
- Som: `bordoes/lula_eu_quero_dizer.ogg` (vol 0.7) -- "Eu quero dizer pra voces..."
- Efeito: camera faz zoom-in leve (1.05x) em Lula por 500ms

#### T=250ms -- Onda de Distorcao
- Flash vermelho escuro (#8B1A1A, alpha 60%) emana de Lula
- 3 aneis concentricos expandem de 0 a 64px de raio em 300ms
- Shader: wave distortion no buffer (se disponivel): `scene.cameras.main.flash(100, 139, 26, 26, true)`
- Som: `sfx/distorcao_realidade.ogg` (vol 0.5) -- som grave de "realidade se quebrando", bass reverberado
- Olhos de Lula: flash vermelho 1 frame

#### T=350ms -- UI Corruption Ativada
- **EFEITO PRINCIPAL**: UI do jogador se corrompe por 5000ms
  - Barra de vida: muda para 100% (FALSA) -- cor ligeiramente diferente para jogadores atentos (#00FF00 em vez do verde normal)
  - Score: multiplica display x10 (valor real nao muda)
  - Mapa: espelha horizontalmente por 5s (tudo invertido)
  - Texto de alerta: "NUNCA ANTES NA HISTORIA DESTE PAIS..." pisca na tela em vermelho
- Aura de particulas vermelhas orbita Lula: 6 particulas (#8B1A1A, 1x1px) em circulo de 16px raio, velocidade angular 180 graus/s
- Som: `sfx/ui_glitch.ogg` (vol 0.4) -- glitch digital, static

#### T=5350ms -- Fim do Efeito
- UI restaura com flash breve
- Aura se dissipa
- Som: `sfx/ui_restore.ogg` (vol 0.3) -- "pop" de retorno ao normal
- Texto: "MENTIRA DESMASCARADA" aparece por 1s

### Cooldown: 15000ms

---

## SPECIAL 2: "Dedo Perdido"

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 80 | 80 | Investida para frente |
| 2 | 80 | 160 | Dedada (V-poke) |
| 3 | 80 | 240 | Contato + flash |
| 4 | 120 | 360 | Retorno |

**Duracao total**: 360ms

### Sequencia de Eventos

#### T=0ms -- Investida
- Lula avanca 8px em direcao ao alvo em 80ms (dash curto)
- Posicao: abaixada
- Som: `sfx/lula_grunt_melee.ogg` (vol 0.3) -- grunhido curto

#### T=80ms -- Dedada
- Mao esquerda (4 dedos) em posicao de eye-poke (V)
- Hitbox ativa: retangulo 8x4px na frente de Lula
- Som: `sfx/poke_whoosh.ogg` (vol 0.3)

#### T=160ms -- Contato
- Flash amarelo (#FFCC00) 3x3px no ponto de impacto
- Dano aplicado: 25 HP
- Efeito no alvo: stun 500ms + particulas de "estrelinhas" ao redor do rosto do alvo
- Camera: micro-shake 1px por 50ms
- Som: `sfx/poke_impact.ogg` (vol 0.5) -- "pok" comico
- Bordao (40% chance): `bordoes/lula_dedo.ogg` (vol 0.4) -- "Voce nao sabe o que e perder um dedo, companheiro!"

#### T=240ms -- Retorno
- Lula volta para posicao original
- Sacudir mao: tween de rotacao da mao +/-5 graus 2x em 120ms
- Recovery: 200ms antes de poder agir

### Cooldown: 3000ms
### Range: 16px (melee)

---

## SPECIAL 3: "Quarto Mandato" (Resurreicao)

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 300 | 300 | Corpo morto (pausa dramatica) |
| 2 | 200 | 500 | Garrafa fantasma aparece |
| 3 | 200 | 700 | Cachaca cai na boca |
| 4 | 200 | 900 | Sinais de vida |
| 5 | 200 | 1100 | Sentando |
| 6 | 200 | 1300 | Levantando |
| 7 | 150 | 1450 | Quase em pe |
| 8 | 150 | 1600 | Ressurreto! |

**Duracao total**: 1600ms

### Sequencia de Eventos

#### T=0ms -- Dramatica Pausa
- Lula no chao, morto (death frame 4)
- Silencio por 300ms (nenhum som do jogo, ou volume geral reduzido a 30%)
- Particulas: cinzas (#666666) flutuando lentamente para cima do corpo
- Outros inimigos e o jogador podem agir normalmente

#### T=300ms -- Garrafa Fantasma
- Garrafa translucida (#2A5A2A, alpha 50%) materializa 12px acima do corpo
- Particulas douradas (#FFCC22): 4-6 orbitando a garrafa, 1x1px
- Som: `sfx/supernatural_chime.ogg` (vol 0.3) -- sino sobrenatural, reverberado
- Tween da garrafa: oscila verticalmente +/-2px (flutuando)

#### T=500ms -- Cachaca Cai
- Garrafa inclina e liquido fantasmagorico escorre para a boca de Lula
- Emitter: stream de particulas (#CC8833, alpha 60%) da garrafa para a boca, 3 part/frame
- Dedos da mao direita twitcham (sprite sub-frame ou tween de 1px)
- Som: `sfx/supernatural_pour.ogg` (vol 0.4) -- liquido sendo despejado, eco sobrenatural

#### T=700ms -- Sinais de Vida
- Olhos mudam de X_X para "waking up"
- Pele clareia: tween de tint de #CCBB99 (palido) para #D4956B (normal) em 400ms
- Barriga infla 1px (respiracao retornando)
- Nariz: comeca a pulsar vermelho novamente (tween de tint)
- Som: `sfx/lula_gasp.ogg` (vol 0.3) -- inspiracao profunda

#### T=900ms -- Sentando
- Torso se levanta (tween de rotacao de 0 a 30 graus em 200ms, ease Quad.Out)
- Garrafa fantasma se solidifica (alpha 50% -> 100%)
- Cachaca escorrendo pelo queixo: 2 particulas #CC8833 descendo
- Som: `bordoes/lula_reeleito.ogg` (vol 0.5) -- "Mas eu acabei de ser reeleito, companheiro!"

#### T=1100ms -- Levantando
- Torso a 60 graus
- Bracos apoiando
- Placa de titanio: flash (#B0C0D0) por 100ms
- Particulas douradas: intensificam (8-10)
- Som: `sfx/rising_power.ogg` (vol 0.4) -- som crescente de poder

#### T=1300ms -- Quase em Pe
- De pe mas curvado
- Garrafa fantasma agora e garrafa real na mao
- Terno mais rasgado (skin damage incrementada)
- Curativo a menos visivel

#### T=1450ms -- Ressurreto
- Posicao idle completa
- Flash dourado final: tela flash (#FFCC22, alpha 30%) por 100ms
- HP bar: aparece a 25% com animacao de preenchimento
- Particulas douradas: dissipam-se em 500ms
- Aura residual: glow dourado no sprite por 1000ms (alpha fade 0.3 -> 0)
- Som: `sfx/resurrection_complete.ogg` (vol 0.5) -- acorde de "renascimento" comico
- Texto flutuante: "MANDATO [N]/3" (onde N e o numero atual)

### Condicoes
- Maximo 3 ativacoes por luta
- HP apos ressurreicao: 25% do maximo
- Invulnerabilidade durante toda a animacao (1600ms)
- Velocidade de movimento +10% apos cada ressurreicao (acumula)

---

## SPECIAL 4: "Empurra Mole / Faz o L"

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 200 | 200 | Se planta |
| 2 | 250 | 450 | Braco subindo (LENTO) |
| 3 | 250 | 700 | L em formacao |
| 4 | 200 | 900 | L completo + flash |
| 5 | 200 | 1100 | Onda de choque |
| 6 | 100 | 1200 | Dissipacao |

**Duracao total**: 1200ms (deliberadamente LENTO -- "bem devagarinho")

### Sequencia de Eventos

#### T=0ms -- Se Planta
- Lula para de se mover completamente
- Pes se afastam (posicao de poder)
- Garrafa guardada atras
- Time scale do jogo: 0.8 (TUDO desacelera levemente -- o jogador sente a desaceleracao)
- Som: `bordoes/lula_empurra_mole.ogg` (vol 0.6) -- "Se o Tadala ta caro... empurra mole mesmo..."

#### T=200ms -- Braco Subindo
- Mao esquerda começa a subir EM CAMERA LENTA
- Tween: posicao Y da mao de cintura ate ombro, 250ms, ease `Sine.InOut` (excepcionalmente suave aqui -- o contraste com o resto do jogo e o ponto)
- Aura vermelha (#8B1A1A, alpha 30%) comeca a se acumular: circulo de 8px raio, pulsando
- Particulas de poeira do chao: 4 particulas (#8B7355) subindo lentamente
- Audio continua: "...mas empurra pensando no Lula..."
- Chao: linhas de rachaduras (1px escuras) comecam a irradiar de Lula

#### T=450ms -- L em Formacao
- Mao na altura do ombro, dedos formando L
- O L e GROTESCO -- com 4 dedos fica errado, torto, comico
- Aura intensifica: alpha 50%, raio 12px
- Chao: mais rachaduras
- Camera: zoom-in lento para Lula (1.0 -> 1.1 em 500ms)
- Audio continua: "...faz o L..."
- Screen vignette: bordas escurecem levemente

#### T=700ms -- L Completo + Flash
- L acima da cabeca, totalmente formado
- Flash: tela inteira (#FFFFFF, alpha 30%) por 100ms
- Glow vermelho ao redor dos dedos (#CC3333 outline animado)
- Boca: enorme, gritando "FAZ O L!"
- Time scale: 0.5 (AINDA MAIS LENTO no pico)
- Audio: "...bem devagarinho!" (pico do audio)
- Camera shake: tremor continuo 1px
- Particulas de energia: burst de 12 particulas vermelhas (#8B1A1A) do L para fora

#### T=900ms -- Onda de Choque
- Time scale retorna a 1.0 ABRUPTAMENTE (snap back to normal speed = impacto)
- **SHOCKWAVE**: Circulo irregular de energia vermelho/marrom expandindo de Lula
  - Raio inicial: 16px
  - Raio final: 128px (2 tiles em todas as direcoes)
  - Velocidade de expansao: 100px em 200ms (LENTO -- "empurra mole")
  - Visual: anel de 4px de espessura, cores #8B1A1A e #5C3317 alternando
  - Distorcao: shader de ondulacao atras do anel
- **Efeito nos alvos**:
  - Todos dentro do raio: knockback de 64px (4 tiles) na direcao oposta a Lula
  - Dano: 20 HP base, +5 HP para cada tile mais perto de Lula
  - Slow: velocidade de movimento -50% por 2000ms
- Camera: retorna ao zoom normal
- Som: `sfx/shockwave_boom.ogg` (vol 0.8) -- boom grave, profundo, reverberante

#### T=1100ms -- Dissipacao
- Onda desaparece
- Particulas residuais vermelhas se dissipam
- Lula recupera garrafa
- Retorna a idle
- Time scale: 1.0

### Cooldown: 20000ms
### Easter Egg: Se ativado, 10% de chance de tocar o audio viral completo do Discord em vez do bordao normal.

---

## SPECIAL 5: "Discurso de Hora e Meia" -- ULTIMATE

### Timing
| Frame | Duracao (ms) | Acumulado (ms) | Evento |
|-------|-------------|----------------|--------|
| 1 | 300 | 300 | Palanque surgindo |
| 2 | 200 | 500 | Lula sobe |
| 3 | 250 | 750 | Inicio do discurso |
| 4 | 250 | 1000 | Gesticulacao intensa |
| 5 | 250 | 1250 | Pico emocional |
| 6 | 250 | 1500 | Circularidade |
| 7 | 250 | 1750 | Apice |
| 8 | 250 | 2000 | Fim + palanque afunda |
| -- | 8000 | 10000 | Efeito global ativo |

**Duracao da animacao**: 2000ms setup
**Duracao do EFEITO**: 8000ms (todos parados)
**Duracao total**: 10000ms

### Sequencia de Eventos

#### T=0ms -- Palanque Surgindo
- Tween: objeto `palanque` sobe do chao (Y offset de +16 a 0 em 300ms, ease `Bounce.Out`)
- Palanque sprite: 24x12px, madeira (#8B7355) com bandeiras vermelhas (#8B1A1A) nos cantos
- Particulas de terra: 6-8 (#5C3317) explodem ao redor conforme palanque rompe o chao
- Camera: shake 3px
- Som: `sfx/palanque_surge.ogg` (vol 0.6) -- madeira quebrando/surgindo + terra se abrindo

#### T=300ms -- Lula Sobe
- Tween: Lula sobe 8px (para cima do palanque) em 200ms, ease `Quad.Out`
- Garrafa guardada (desaparece do sprite)
- Microfone aparece na mao esquerda (4 dedos segurando mic)
- Postura: costas retas pela PRIMEIRA E UNICA VEZ no jogo
- Som: `sfx/crowd_murmur.ogg` (vol 0.2) -- multidao murmurada no fundo

#### T=500ms -- Inicio do Discurso
- **FREEZE GLOBAL**: `scene.physics.pause()` ou equivalente
  - TODOS os sprites (aliados E inimigos) recebem animacao de "sentando"
  - Zs flutuantes aparecem sobre cada NPC a cada 500ms
  - O JOGADOR nao pode se mover, atirar, ou usar habilidades
  - Unica excecao: score continua contando
- Ondas de som: arcos concentricos (#AAAAAA, alpha 30%) saindo da boca de Lula, expandindo e fading
- Bordao loop: `bordoes/lula_discurso_loop.ogg` (vol 0.7) -- "Eu quero dizer pra voces... olha... eu quero dizer... eu quero dizer uma coisa..." (audio de 8s em loop que NUNCA CHEGA AO PONTO)
- Texto na tela (UI): captions do discurso aparecendo e desaparecendo, nunca concluindo uma frase

#### T=750ms -> T=8500ms -- Discurso Ativo (ciclo dos frames 4-7 em loop)
- **Ciclo visual**: Frames 4 -> 5 -> 6 -> 7 em loop a cada 1000ms durante os 8s
- **Cura progressiva**:
  - HP de Lula: sobe 12.5% por segundo (100% em 8s, cura total)
  - Visual: particulas verdes (#44CC44) sendo absorvidas por Lula, 2-3 por segundo
  - Barra de HP: animacao de preenchimento continuo
- **Aura crescente**:
  - Comeca dourada (#FFCC22, alpha 20%)
  - Cresce ate alpha 50% no segundo 4
  - Raio: de 16px a 32px
- **Bandeiras**: tremulam (frames alternados com 1px de deslocamento horizontal)
- **Efeito no cenario**: iluminacao fica levemente vermelha (#220000 overlay) -- tom de comicio

#### T=8500ms -- Fim do Discurso
- Sprite troca para frame 8
- **UNFREEZE**: `scene.physics.resume()`
- Todos os NPCs "acordam": animacao de sacudir cabeca (1 frame custom por NPC)
- Palanque afunda: tween Y de 0 a +16 em 300ms, ease `Quad.In`
- Particulas de terra novamente
- Microfone desaparece, garrafa volta
- Lula volta ao chao (tween Y para posicao normal)
- Camera: zoom-out de volta ao normal
- Flash: branco (#FFFFFF, alpha 20%) por 100ms

#### T=9000ms+ -- Recovery
- Lula de volta ao chao em posicao idle
- HP: 100% (cura total)
- Suado: 3 particulas de suor (#88CCEE) na testa que escorrem e somem
- Jogador pode agir normalmente
- Som: `sfx/crowd_confused.ogg` (vol 0.3) -- murmuracao confusa de multidao se dispersando

### Condicoes para Ativar
- Barra de ultimate: carrega com dano recebido e dano causado
- Necessita 100% da barra (acumula ao longo de ~60s de combate)
- Usavel 1 vez por vida (reseta com Quarto Mandato)

### Cooldown: Barra de ultimate deve recarregar do zero

---

## TABELA RESUMO DE TIMINGS

| Animacao | Frames | FPS | Duracao (ms) | Loop | Tipo |
|----------|--------|-----|-------------|------|------|
| Idle | 4 | 8 | 750 (yoyo) | Sim | Ping-pong |
| Walk | 6 | 10 | 600 | Sim | Forward |
| Attack (Cachaçada) | 3 | 8 | 375 | Nao | One-shot |
| Death | 4 | 5 | 800 | Nao | One-shot |
| Hit | 2 | 10 | 200 | Nao | One-shot |
| Fato Alternativo | 6 | 8 | 650 + 5000 efeito | Nao | One-shot + timer |
| Dedo Perdido | 4 | 10 | 360 | Nao | One-shot |
| Quarto Mandato | 8 | 5 | 1600 | Nao | One-shot (3x max) |
| Empurra Mole / Faz o L | 6 | 5 | 1200 | Nao | One-shot |
| Discurso Ultimate | 8 | 5 | 2000 + 8000 efeito | Nao | One-shot |

---

## LISTA COMPLETA DE ASSETS DE AUDIO

### SFX (Sound Effects)
| Arquivo | Descricao | Duracao | Prioridade |
|---------|-----------|---------|------------|
| `sfx/lula_gole.ogg` | Gole de cachaca (glug) | 300ms | Alta |
| `sfx/lula_arroto.ogg` | Arroto curto | 400ms | Alta |
| `sfx/lula_suspiro.ogg` | Suspiro "ahh" | 500ms | Media |
| `sfx/lula_tropeco.ogg` | Scuff + "opa" | 300ms | Media |
| `sfx/garrafa_tink.ogg` | Tinido de garrafa | 200ms loop | Baixa |
| `sfx/passo_pesado_1.ogg` | Thud de sapato (esquerdo) | 150ms | Media |
| `sfx/passo_pesado_2.ogg` | Thud de sapato (direito) | 150ms | Media |
| `sfx/lula_grunt_arremesso.ogg` | Grunhido de arremesso | 200ms | Alta |
| `sfx/garrafa_whoosh.ogg` | Whoosh de garrafa voando | 300ms | Alta |
| `sfx/garrafa_quebra_explosao.ogg` | Vidro + fogo | 500ms | Alta |
| `sfx/garrafa_quebra.ogg` | Vidro quebrando (so) | 300ms | Media |
| `sfx/corpo_no_chao.ogg` | Thud de corpo gordo | 300ms | Alta |
| `sfx/lula_impacto_death.ogg` | Impacto + "ugh" | 400ms | Alta |
| `sfx/hit_flesh.ogg` | Impacto em corpo | 150ms | Alta |
| `sfx/titanio_clank.ogg` | Metal clank (headshot) | 200ms | Alta |
| `sfx/poke_whoosh.ogg` | Whoosh de dedada | 150ms | Media |
| `sfx/poke_impact.ogg` | "Pok" comico | 100ms | Alta |
| `sfx/supernatural_chime.ogg` | Sino sobrenatural | 800ms | Alta |
| `sfx/supernatural_pour.ogg` | Liquido fantasma | 500ms | Alta |
| `sfx/lula_gasp.ogg` | Inspiracao profunda | 400ms | Media |
| `sfx/rising_power.ogg` | Som crescente de poder | 500ms | Alta |
| `sfx/resurrection_complete.ogg` | Acorde de renascimento | 600ms | Alta |
| `sfx/shockwave_boom.ogg` | Boom grave | 800ms | Alta |
| `sfx/distorcao_realidade.ogg` | Bass de distorcao | 500ms | Alta |
| `sfx/ui_glitch.ogg` | Glitch digital | 300ms | Media |
| `sfx/ui_restore.ogg` | Pop de restauracao | 200ms | Media |
| `sfx/palanque_surge.ogg` | Madeira + terra | 500ms | Alta |
| `sfx/crowd_murmur.ogg` | Multidao murmurada | 2000ms loop | Baixa |
| `sfx/crowd_confused.ogg` | Multidao confusa | 1500ms | Media |
| `sfx/lula_dramatic_pause.ogg` | Silencio subito | 500ms | Media |

### Total de assets de audio por Lula: ~30 SFX + ~12 bordoes = ~42 arquivos de audio
