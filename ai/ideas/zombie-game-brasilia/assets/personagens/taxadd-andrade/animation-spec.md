# TAXADD / ANDRADE - Especificacao de Animacoes

## Mini-Boss (Taxadd) / NPC Inutil (Andrade) - "Zumbis de Brasilia"

---

## CONFIGURACAO GLOBAL

- **Engine**: Phaser 3
- **Frame rate base**: 10 fps (estilo jerky do Andre Guedes)
- **Interpolacao**: NENHUMA (snap entre frames, sem tweening suave)
- **Loop**: Todas as animacoes de idle/walk sao loop. Attack/death/special sao one-shot.
- **Sprite size**: 64x64px por frame
- **Formato atlas**: Sprite sheets horizontais (frames lado a lado)

---

## ANDRADE (NPC Inutil)

### IDLE
```
Nome: andrade_idle
Arquivo: andrade-spritesheet.png
Frames: 4 (row 0, cols 0-3)
Dimensao sheet: 256x64px
FPS: 8 (mais lento que normal = letargia)
Loop: true
Repeat: -1 (infinito)
```

**Timing detalhado:**
| Frame | Duracao (ms) | Descricao do Movimento |
|-------|-------------|----------------------|
| 0 | 125 | Postura neutra. Sem movimento. |
| 1 | 150 | Cabeca inclina DIREITA (tween SNAP, nao suave). Olhos sobem. |
| 2 | 125 | Volta centro. Mao sobe timida, desiste. |
| 3 | 150 | Cabeca inclina ESQUERDA. Corpo balanca. |

**Transicao para outros estados:**
- idle → walk: IMEDIATO (sem transicao, snap para frame 0 do walk)
- idle → attack: IMEDIATO
- idle → hit: IMEDIATO (prioridade alta, interrompe qualquer frame)
- idle → special: 100ms delay (tempo de "reagir")

---

### WALK
```
Nome: andrade_walk
Arquivo: andrade-spritesheet.png
Frames: 6 (row 1, cols 0-5)
Dimensao sheet: 384x64px
FPS: 10
Loop: true
Repeat: -1
```

**Timing detalhado:**
| Frame | Duracao (ms) | Descricao do Movimento |
|-------|-------------|----------------------|
| 0 | 100 | Pe direito a frente. Mochila balanca esquerda. |
| 1 | 100 | Meio passo. Lancheira visivel. |
| 2 | 100 | Pe esquerdo a frente. Mochila balanca direita. |
| 3 | 120 | TROPECA (frame levemente mais longo para comedia). |
| 4 | 80 | Recupera RAPIDO (frame curto = susto). |
| 5 | 100 | Volta ao normal, terno desajustado. |

**Efeito sonoro sync:**
- Frame 3: SFX "tropecar" (shuffle sound)
- Frame 4: SFX "gasp" (susto breve)

---

### ATTACK (Lancheira)
```
Nome: andrade_attack
Arquivo: andrade-spritesheet.png
Frames: 3 (row 2, cols 0-2)
Dimensao sheet: 192x64px
FPS: 10
Loop: false
Repeat: 0 (uma vez)
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | Levanta lancheira. **No frame 0: SFX "grunt" fraco.** |
| 1 | 100 | JOGA lancheira. **No frame 1: SPAWN projetil "merenda" na posicao do sprite + offset (16, -8). Direcao: facing direction. Velocidade: 150px/s.** |
| 2 | 200 | Pos-ataque (frame longo = patetismo). **SFX "oops".** |

**Projetil "Merenda":**
- Sprite: lancheira 32x32px
- Velocidade: 150px/s
- Dano: 5 (baixo)
- Ao colidir: spawna 4 sub-particulas (sanduiche, suco, biscoito, maca) que se espalham em 45/135/225/315 graus, cada uma 16x16px, dano 1 cada

**Retorno:** Apos frame 2, volta para idle automaticamente.

---

### DEATH
```
Nome: andrade_death
Arquivo: andrade-spritesheet.png
Frames: 4 (row 3, cols 0-3)
Dimensao sheet: 256x64px
FPS: 6 (mais lento = dramatico comico)
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | Olhos viram espirais. Mochila abre. **SFX "bonk"**. |
| 1 | 200 | Cai de joelhos. **SPAWN particulas de merenda (5-8 itens) em arco 180 graus.** |
| 2 | 200 | Cai de lado. Merenda ao redor. **SFX "thud" suave.** |
| 3 | 300 | Deitado. Sorriso. **SPAWN particula "fantasma" subindo (alpha fade out, 1s).** Colider desativado. |

**Pos-morte:** Sprite permanece no frame 3 por 2 segundos, depois fade out (alpha 100% → 0% em 500ms).

---

### HIT
```
Nome: andrade_hit
Arquivo: andrade-spritesheet.png
Frames: 2 (row 4, cols 0-1)
Dimensao sheet: 128x64px
FPS: 12 (rapido = impacto)
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 80 | Recuo 4px na direcao oposta ao hit. Flash branco (overlay, 50ms). **SFX "ow" fraco.** |
| 1 | 100 | Volta a posicao. Cambaleio. |

**Retorno:** Volta para estado anterior (idle ou walk) imediatamente apos frame 1.

---

### SPECIAL: Merenda Infinita
```
Nome: andrade_special_merenda
Arquivo: andrade-spritesheet.png
Frames: 6 (row 5, cols 0-5)
Dimensao sheet: 384x64px
FPS: 8
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | Abre mochila. **SPAWN particula "luz amarela" de dentro da mochila.** |
| 1 | 200 | Retira sanduiche gigante. **SFX "ta-da!" comico.** |
| 2 | 100 | MORDIDA. **SPAWN particulas "migalhas" (6-8) em cone frontal. SFX "chomp".** |
| 3 | 200 | Mastigando. Bochechas inflam. **SPAWN particula "coracao" flutuante.** |
| 4 | 150 | Engole. **EFEITO: Onda verde de cura (circulo expandindo, raio 32px, alpha fade, 300ms). HP += heal_amount.** |
| 5 | 200 | ARROTO. Migalhas no terno. **SFX "burp". SPAWN 3-4 particulas "migalhas" caindo.** |

**Mecanica:** Cura 25% do HP maximo. Cooldown 30 segundos.

---

### SPECIAL: Invisibilidade do Andrade
```
Nome: andrade_special_invisible
Arquivo: andrade-spritesheet.png
Frames: 4 (row 6, cols 0-3)
Dimensao sheet: 256x64px
FPS: 6
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 200 | Normal. **Inicia tween de alpha: 100% → 75%.** |
| 1 | 200 | Alpha 75%. Contornos suavizam. **Inimigos dentro de 128px perdem aggro.** |
| 2 | 200 | Alpha 30%. So contorno e mochila visiveis. **Todos inimigos perdem aggro.** |
| 3 | 300 | Alpha 0% EXCETO sombra no chao e lancheira flutuando. **Invulneravel por 5 segundos.** |

**Mecanica:** Invisivel por 5 segundos. Qualquer acao (attack, move) cancela. Cooldown 45 segundos.

---

## TAXADD (Mini-Boss)

### IDLE
```
Nome: taxadd_idle
Arquivo: taxadd-spritesheet.png
Frames: 4 (row 0, cols 0-3)
Dimensao sheet: 256x64px
FPS: 10
Loop: true
Repeat: -1
```

**Timing detalhado:**
| Frame | Duracao (ms) | Descricao do Movimento |
|-------|-------------|----------------------|
| 0 | 100 | Postura poder. Cifras $ em 12h/6h. Moedas caem bolso esquerdo. |
| 1 | 100 | Dedos digitam calculadora (tap). Cifras rotam 3h/9h. Reflexo verde. |
| 2 | 100 | Levanta calculadora (resultado). Sorriso mais largo. Cifras 1h/7h. |
| 3 | 100 | Acaricia carimbo. Cifras voltam 12h/6h. Oculos brilham. |

**Sistema de Particulas Permanentes (SEMPRE ativo):**
- **Cifras $ Orbitantes:**
  - Quantidade: 4
  - Orbita: circular, raio 12px do centro
  - Velocidade orbital: 180 graus/segundo (1 rotacao completa em 2s)
  - Tamanho: 8x8px
  - Alpha: 80%
  - Cor: #FFD700
  - Variacao de brilho: onda senoidal, amplitude 20%, periodo 1s

- **Moedas Caindo:**
  - Spawn: 1 a cada 500ms durante idle, 1 a cada 300ms durante walk
  - Tamanho: 4x4px
  - Gravidade: 200px/s^2
  - Bounce: 1 vez, coeficiente 0.3
  - Lifetime: 1000ms
  - Spawn point: bolso mais proximo (esquerdo ou direito alternando)

---

### WALK
```
Nome: taxadd_walk
Arquivo: taxadd-spritesheet.png
Frames: 6 (row 1, cols 0-5)
Dimensao sheet: 384x64px
FPS: 10
Loop: true
Repeat: -1
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 100 | Marcha decidida. Cifras seguem com delay 50ms. **SPAWN moeda.** |
| 1 | 100 | Mao enorme aberta. Moedas caem. |
| 2 | 100 | Calculadora balanca. Cifras se reorganizam. **SPAWN moeda.** |
| 3 | 100 | Reflexo verde pulsa. Bolsos transbordam. |
| 4 | 100 | Inclina para frente (ansioso). Maos abertas. Cifras expandem. **SPAWN moeda.** |
| 5 | 100 | Retoma postura. Sorriso intensifica. |

**Efeito de trilha:**
- A cada 200ms durante walk, SPAWN 1 moeda no chao na posicao anterior (trilha de moedas)
- Moedas da trilha: 4x4px, lifetime 3 segundos, fade out nos ultimos 500ms

---

### ATTACK: Calculadora Infernal
```
Nome: taxadd_attack
Arquivo: taxadd-spritesheet.png
Frames: 3 (row 2, cols 0-2)
Dimensao sheet: 192x64px
FPS: 10
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | Levanta calculadora. Tela brilha verde. Cifras giram rapido. **SFX "charge-up" crescente.** |
| 1 | 100 | DISPARA cifras $. **SPAWN 3 projeteis "$" em cone (angulo central + -15deg e +15deg). Velocidade: 250px/s. Dano: 15 cada. SFX "TAXADO!" (voz). SFX "pew-pew" metalico.** |
| 2 | 200 | Pos-ataque. Fumaca. Carimbo "TAXADO" aparece. **SPAWN efeito "TAXADO" na direcao do ataque (32x32px, 500ms lifetime). SPAWN 4-6 moedas explodindo dos bolsos.** |

**Projetil "$" (Cifrao):**
- Sprite: 32x32px, animacao 4 frames (rotacao Y)
- Velocidade: 250px/s
- Dano: 15
- Trail: particulas douradas menores (4x4px) a cada 50ms atras do projetil
- Ao colidir: SPAWN efeito "TAXADO" (32x32px) sobre o alvo por 1 segundo

**Retorno:** Volta para idle apos frame 2.

---

### DEATH
```
Nome: taxadd_death
Arquivo: taxadd-spritesheet.png
Frames: 4 (row 3, cols 0-3)
Dimensao sheet: 256x64px
FPS: 6
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | Oculos racham. Calculadora voa. **SFX "glass crack". Cifras $ scatter em direcoes aleatorias (velocidade 100-200px/s). STOP particulas de moedas orbitantes.** |
| 1 | 200 | Cai de joelhos. Bolsos explodem. **SPAWN 20-30 moedas em explosao radial (360 graus). Oculos caem. SWAP sprite olhos → olhos de Andrade (perdidos).** |
| 2 | 200 | Cai de costas. **TWEEN cor terno: verde → cinza (500ms). Calculadora quebrada ao lado. Moedas formam poca.** |
| 3 | 400 | Deitado como Andrade. **Cifras $ fade out uma a uma (100ms entre cada). Ultima moeda rola (particula 4x4, velocidade 50px/s, direcao aleatoria). SFX "single coin rolling".** |

**Pos-morte:** Frame 3 permanece 3 segundos. Fade out total em 1 segundo.

---

### HIT
```
Nome: taxadd_hit
Arquivo: taxadd-spritesheet.png
Frames: 2 (row 4, cols 0-1)
Dimensao sheet: 128x64px
FPS: 12
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 80 | Recuo 6px. Oculos torcem. Cifras $ embaralham. **Flash vermelho (overlay, 50ms). SPAWN 3-4 moedas do impacto. SFX "ugh" irritado.** |
| 1 | 100 | Agarra calculadora com forca. Sorriso forjado. Oculos reajustam. **Cifras $ voltam a orbita mas tremendo (amplitude jitter 2px por 500ms).** |

---

### SPECIAL: Taxa Infinita
```
Nome: taxadd_special_taxa
Arquivo: taxadd-spritesheet.png
Frames: 8 (row 5, cols 0-7)
Dimensao sheet: 512x64px
FPS: 8
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | Bracos abrem. **Aura verde inicia (raio 0 → 32px, alpha 0 → 40%). Cifras multiplicam 4 → 8. SFX "power-up" grave.** |
| 1 | 150 | Aura expande. **Raio 32 → 64px. Cifras 8 → 12. SPAWN moedas do chao (10, flutuam para cima). SFX crescendo.** |
| 2 | 150 | Aura raio maximo 96px. **EFEITO DRAIN: particulas douradas de TODOS os personagens dentro do raio sao SUGADAS para Taxadd (particulas 4x4, velocidade 150px/s em direcao ao centro). DANO: 5/s a todos no raio. SFX "suction".** |
| 3 | 125 | Corpo incha. **Scale sprite 100% → 110%. Bolsos inflam (deformacao). Calculadora numeros subindo.** |
| 4 | 125 | Maximo poder. **Pulsacao verde (flash on/off, 100ms). Cifras freneticas (velocidade orbital 3x). Moedas orbitando (raio 24px). SFX "maximum power".** |
| 5 | 125 | Libera excesso. **Ondas de choque verdes (3 circulos expandindo, raio 96 → 192px, alpha 60% → 0%, 500ms cada, defasados 100ms). DANO: 10 a todos que a onda toca. SFX "shockwave".** |
| 6 | 200 | Explosao 360. **SPAWN 20 cifras $ e 30 moedas em explosao radial. Efeito "TAXADO" gigante (64x64px) aparece no centro, 1s. SFX "TAXADO!" (voz, eco).** |
| 7 | 200 | Retorno. **Scale 110% → 100%. Cifras voltam a 4 em orbita normal. Aura dissipa (alpha 40% → 0%, 500ms). Residuo verde no ar (particulas 2x2, floating, 3s lifetime). Sorriso satisfeito.** |

**Mecanica:**
- Raio de efeito: 96px (3 tiles)
- Dano continuo: 5 HP/segundo a todos dentro do raio durante 4 segundos
- Dano de onda: 10 HP one-shot
- Cooldown: 60 segundos
- Drena recursos: score -2/segundo durante efeito

---

### SPECIAL: Taxacao Universal (Ultimate)
```
Nome: taxadd_ultimate
Arquivo: taxadd-spritesheet.png
Frames: 8 (row 6, cols 0-7)
Dimensao sheet: 512x64px
FPS: 6 (mais lento = dramatico)
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 200 | Pose dramatica. **FREEZE todos os inimigos por 500ms (stunned). Camera shake leve. SFX "dramatic chord".** |
| 1 | 200 | Coluna de luz verde. **SPAWN beam vertical (8px largura, tela toda, verde #00FF00, alpha 80%). Borda da tela comeca a ficar DOURADA (tween 0 → 100% em 500ms). SFX "beam ascending".** |
| 2 | 200 | Onda de choque verde. **Circulo expandindo do centro: raio 0 → tela toda, velocidade 500px/s. Tudo que toca: SPAWN efeito "TAXADO" (32x32, vermelho, permanente por 10s). SFX "shockwave massive".** |
| 3 | 250 | Efeitos de gameplay. **APLICAR: power-ups scale 100% → 50%. Score pisca (on/off, 200ms). HP bars de TODOS: scale Y 100% → 80%. Speed global: 100% → 80%. SFX "debuff applied".** |
| 4 | 250 | UI taxada. **SPAWN efeito "TAXADO" sobre CADA elemento de HUD (score, HP bar, mini-map, timer). Score congela com "$" prefixo. Barras de vida com texto "-%20". SFX "stamp stamp stamp" (rapido).** |
| 5 | 200 | Taxadd flutuando. **Sprite Y -= 16px (float). SPAWN centenas de $ e moedas orbitando (emitter: 50 particulas/s, raio 48px, dourado). Maos em T-pose. Sorriso DEMONICO. SFX "evil laugh".** |
| 6 | 200 | Desce. **Sprite Y += 16px. Selos piscam vermelho (flash 100ms on, 100ms off, 3 ciclos). SFX "stamps pulsing".** |
| 7 | 300 | Pousa. Idle. **Tudo permanece taxado por 10 segundos. Ajusta oculos (gesto de mao ENORME passando pelo rosto). SFX "glasses adjust" + "hmph" satisfeito.** |

**Mecanica:**
- Duracao total do efeito: 10 segundos
- Power-ups: -50% valor
- Score: CONGELADO (nao ganha pontos)
- HP de todos: -20% do maximo
- Velocidade global: -20%
- Cooldown: 120 segundos (so usa 1-2x por boss fight)
- A UI deve ser RESTAURADA apos 10s (selos somem, valores voltam ao normal)

---

### SPECIAL: Imposto Retroativo
```
Nome: taxadd_special_retroativo
Arquivo: taxadd-spritesheet.png
Frames: 4 (row 7, cols 0-3)
Dimensao sheet: 256x64px
FPS: 8
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | Puxa relogio. **SPAWN sprite relogio (16x16) na mao esquerda ENORME. Cifras ficam azuladas (tint #6666FF). SFX "clock tick".** |
| 1 | 200 | Gira ponteiros. **Efeito rewind: linhas de tempo (particulas lineares, azul #6666FF, radiais do relogio). Corpo pisca (alpha toggle 100%/50%, 50ms). SFX "rewind" (tape reverse).** |
| 2 | 150 | Selo "RETROATIVO". **SPAWN texto "RETROATIVO" (vermelho, 32x16px) sobre HUD do score. Score REDUZ (numeros voam do HUD para Taxadd, particulas numericas). SFX "score drain".** |
| 3 | 200 | Guarda relogio. **Relogio despawna. Cifras voltam a dourado. Score do alvo REDUZIDO (valor dos ultimos 10s de pontuacao). SFX "coin pocket" (moedas no bolso).** |

**Mecanica:**
- Remove score equivalente aos ultimos 10 segundos de pontuacao do jogador
- Cooldown: 45 segundos

---

## TRANSFORMACAO ANDRADE → TAXADD

```
Nome: andrade_to_taxadd
Arquivo: andrade-to-taxadd-transform.png
Frames: 6
Dimensao sheet: 384x64px
FPS: 6 (lento = dramatico)
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 200 | Andrade normal. **Trigger: condicao de transformacao atingida. SFX "discovery" (nota musical curiosa). Camera leve zoom (105%) no personagem.** |
| 1 | 200 | Olhos arregalam. **Tint do sprite shift: cinza → verde (tween 500ms). Flash verde nos olhos. Mochila comeca a cair (particula, gravidade). SFX "power surge" crescendo.** |
| 2 | 200 | Oculos materializam. **SPAWN oculos overlay (fade in 200ms). Terno 50% verde. Maos iniciam SCALE (100% → 150%). Primeiras moedas spawnam nos bolsos. SFX "transformation" mid.** |
| 3 | 200 | Terno completo. **Terno totalmente verde com pattern $. Maos 200%. Calculadora fade in na mao direita. Primeiras 2 cifras $ spawnam em orbita. SFX "calculator startup".** |
| 4 | 150 | Mochila explode. **SPAWN 8 particulas de mochila (pedacos marrons, direcoes aleatorias). Carimbo aparece no cinto. Bolsos ENCHEM (animacao de preenchimento). Cifras: 4 em orbita. SFX "explosion small".** |
| 5 | 300 | TAXADD completo. **Flash verde INTENSO (overlay, 100ms). Pose de poder. Todas particulas em posicao final. SPAWN texto "TAXADD" acima da cabeca (fade in, float up 16px, fade out em 2s). SFX "boss_entrance" + "evil_laugh". Camera zoom volta a 100%.** |

**Trigger de transformacao:**
- Condicao: Andrade NPC recebe X dano ou wave Y comeca
- Pre-transformacao: Andrade para de andar, freeze por 500ms
- Pos-transformacao: Taxadd fica invulneravel por 2s, depois boss fight comeca

---

## MAQUINA DE ESTADOS DE ANIMACAO

### Andrade
```
          ┌──────────┐
          │   IDLE   │ ← estado padrao
          └────┬─────┘
               │
    ┌──────────┼──────────┬──────────────┐
    ↓          ↓          ↓              ↓
┌──────┐  ┌───────┐  ┌──────┐   ┌───────────┐
│ WALK │  │ATTACK │  │ HIT  │   │ SPECIAL   │
└──┬───┘  └───┬───┘  └──┬───┘   │(merenda/  │
   │          │         │       │invisible) │
   │          │         │       └─────┬─────┘
   └──────────┴─────────┴─────────────┘
                    │
                    ↓
              ┌──────────┐
              │  DEATH   │ (terminal - sem retorno)
              └──────────┘
                    │
                    ↓
              ┌──────────────┐
              │ TRANSFORM    │ (condicional)
              │ → TAXADD     │
              └──────────────┘
```

### Taxadd
```
          ┌──────────┐
          │   IDLE   │ ← estado padrao
          └────┬─────┘
               │
    ┌──────────┼──────────┬──────────────────────────┐
    ↓          ↓          ↓                          ↓
┌──────┐  ┌───────┐  ┌──────┐   ┌───────────────────────────┐
│ WALK │  │ATTACK │  │ HIT  │   │ SPECIAL                   │
└──┬───┘  └───┬───┘  └──┬───┘   │(taxa_infinita/            │
   │          │         │       │ taxacao_universal/         │
   │          │         │       │ imposto_retroativo)        │
   └──────────┴─────────┘       └──────────┬────────────────┘
                    │                      │
                    ↓                      │
              ┌──────────┐                 │
              │  DEATH   │ ← ─────────────┘
              │(→Andrade)│
              └──────────┘
```

**Prioridades de animacao (maior numero = maior prioridade):**
1. IDLE (0)
2. WALK (1)
3. SPECIAL (2)
4. ATTACK (3)
5. HIT (4) — interrompe qualquer coisa exceto DEATH
6. DEATH (5) — prioridade absoluta, terminal

---

## PHASER 3 - EXEMPLO DE CONFIGURACAO

```javascript
// Referencia para implementacao
// Andrade
this.anims.create({
  key: 'andrade_idle',
  frames: this.anims.generateFrameNumbers('andrade', { start: 0, end: 3 }),
  frameRate: 8,
  repeat: -1
});

// Taxadd com particulas
this.taxaddParticles = this.add.particles('coin');
this.taxaddEmitter = this.taxaddParticles.createEmitter({
  speed: { min: 20, max: 50 },
  gravityY: 200,
  lifespan: 1000,
  frequency: 500,
  bounce: 0.3,
  scale: { start: 0.5, end: 0 }
});

// Cifras orbitantes (custom update no game loop)
// Atualizar posicao: x = centerX + cos(time * speed) * radius
//                    y = centerY + sin(time * speed) * radius
```

---

## NOTAS DE IMPLEMENTACAO

1. **NENHUMA interpolacao** entre frames (snap imediato = estilo jerky Andre Guedes)
2. As particulas do Taxadd (cifras $ e moedas) sao objetos SEPARADOS do sprite, gerenciados pelo particle emitter do Phaser
3. A transformacao Andrade→Taxadd deve DESATIVAR o NPC Andrade e ATIVAR o Boss Taxadd como entidade nova
4. O efeito "TAXADO" sobre a UI requer manipulacao do HUD layer (overlay sobre elementos de interface)
5. A Taxacao Universal DEVE taxar a interface - isso e o ponto alto comico do personagem
6. Sons devem ser pre-carregados no preload da cena para evitar delay
7. O sistema de particulas de moedas deve ter pool de objetos (max 50 moedas ativas simultaneamente)
8. Death do Taxadd reverte para sprite de Andrade - necessario ter referencia aos dois sprite sheets carregados
