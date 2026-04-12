# SERGIO MORO (O Heroi Decaido) - Especificacao de Animacoes

## NPC / Ex-Aliado que Muda de Lado - "Zumbis de Brasilia"

---

## CONFIGURACAO GLOBAL

- **Engine**: Phaser 3
- **Frame rate base**: 10 fps (estilo jerky do Andre Guedes)
- **Interpolacao**: NENHUMA (snap entre frames, sem tweening suave)
- **Loop**: Idle/walk sao loop. Attack/death/special/transicao sao one-shot.
- **Sprite size**: 64x64px por frame
- **Formato atlas**: Sprite sheets horizontais (frames lado a lado)

### SISTEMA DE DEGRADACAO
O Moro tem 4 estagios visuais. Cada estagio tem seu PROPRIO conjunto de animacoes.
O swap de estagio acontece ao inicio de waves especificas, com animacao de transicao.

```
Estagio 1 (HEROI)     → Waves 1-3
Estagio 2 (DESGASTADO) → Waves 4-6
Estagio 3 (DECADENTE)  → Waves 7-9
Estagio 4 (IRRELEVANTE)→ Waves 10+
```

---

## ESTAGIO 1: HEROI (Waves 1-3)

### IDLE
```
Nome: moro_s1_idle
Arquivo: moro-stage1-hero.png
Frames: 4 (row 0, cols 0-3)
Dimensao sheet: 256x64px
FPS: 10
Loop: true
Repeat: -1
```

**Timing detalhado:**
| Frame | Duracao (ms) | Descricao do Movimento |
|-------|-------------|----------------------|
| 0 | 100 | Postura ereta, peito estufado. Martelo no ombro brilhando. |
| 1 | 100 | Olhos movem lateral (vigia). Martelo repousa. Reflexo de luz. |
| 2 | 100 | Ajusta gravata (autoridade). Martelo firme. |
| 3 | 100 | Volta ao frame 0 com respiracao (leve expansao peito). |

**Efeito permanente - Aura Heroica:**
- Tipo: Overlay circular, 96x96px, centrado no sprite
- Cor: #FFD700 a 40% alpha
- Animacao: pulsacao lenta (scale 95% → 105%, 1 segundo ciclo)
- Blend mode: ADD

---

### WALK
```
Nome: moro_s1_walk
Arquivo: moro-stage1-hero.png
Frames: 6 (row 1, cols 0-5)
Dimensao sheet: 384x64px
FPS: 10
Loop: true
Repeat: -1
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 100 | Marcha decidida, pe direito. Passos largos. |
| 1 | 100 | Meio passo. Corpo ereto. |
| 2 | 100 | Pe esquerdo. Marcha continua. |
| 3 | 100 | Passo firme. Queixo erguido. |
| 4 | 100 | Martelo taps ombro levemente. |
| 5 | 100 | Completa ciclo. Postura impecavel. |

**SFX sync:** Passos firmes em frames 0 e 3 ("boot_step" forte).

---

### ATTACK
```
Nome: moro_s1_attack
Arquivo: moro-stage1-hero.png
Frames: 3 (row 2, cols 0-2)
Dimensao sheet: 192x64px
FPS: 10
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 120 | Ergue martelo com 2 maos. Olhos ardem. **SFX "whoosh_up".** Flash no metal. |
| 1 | 80 | GOLPE para frente/baixo. **SPAWN efeito impacto (estrela dourada 32x32, 4 frames, posicao: sprite + facing_offset 24px). Dano: 30 (ALTO). SFX "hammer_slam" + "CONDENADO!" (voz). Screen shake: 2px, 100ms.** |
| 2 | 150 | Pos-golpe. Postura vitoriosa. Martelo volta ao ombro. **SFX "justice_served" (nota grave).** |

**Retorno:** Idle apos frame 2.

---

### DEATH
```
Nome: moro_s1_death
Arquivo: moro-stage1-hero.png
Frames: 4 (row 3, cols 0-3)
Dimensao sheet: 256x64px
FPS: 6
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | CHOQUE no rosto. Martelo voa. **SFX "gasp_heroic". Martelo sprite separado: voa 32px na direcao oposta, rotacao 360 em 500ms, gravidade.** |
| 1 | 200 | Cai de joelhos. **SPAWN silhueta heroica (flash 200ms, sprite ghost copy a alpha 30%, posicao estatica enquanto original cai). SFX "knee_hit".** |
| 2 | 200 | Cai de lado. Terno impecavel mesmo caindo. **Aura dourada FLICKER (on/off 50ms, 4x). SFX "body_fall".** |
| 3 | 400 | Deitado. Mao esticada para martelo. **Aura fade out (alpha 40% → 0%, 1s). SFX "last_breath_heroic".** |

**Pos-morte:** Frame 3 permanece 2.5s, fade out em 800ms.

---

### HIT
```
Nome: moro_s1_hit
Arquivo: moro-stage1-hero.png
Frames: 2 (row 4, cols 0-1)
Dimensao sheet: 128x64px
FPS: 12
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 80 | Recuo 3px. SURPRESA. **Flash branco 50ms. SFX "huh?!" (heroi nao espera hit). Aura pulsa (intensidade 2x por 100ms).** |
| 1 | 80 | Recupera RAPIDO. Postura de combate. **Martelo pronto. SFX "grunt_determined". Olhos mais determinados.** |

---

### SPECIAL: Heroi Decaido (Maximo Poder)
```
Nome: moro_s1_special
Arquivo: moro-stage1-hero.png
Frames: 4 (row 5, cols 0-3)
Dimensao sheet: 256x64px
FPS: 8
Loop: false
Repeat: 0
```

**Timing detalhado:**
| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 200 | Aura DOURADA engole. **Aura alpha 40% → 80%. Scale aura 100% → 150%. Martelo BRILHA (tint #FFFFFF, 100ms flash). SFX "power_surge_heroic".** |
| 1 | 150 | SALTA (+8px Y). **Martelo acima da cabeca. Terno esvoaca (sprite deform leve). SPAWN particulas douradas (20, radial, velocidade 50-100px/s). SFX "hero_jump".** |
| 2 | 100 | GOLPE DEVASTADOR. **SPAWN crater de impacto (48x48px, 6 frames, posicao frente). Onda de choque dourada (circulo expandindo, raio 0 → 128px, 300ms, alpha 80% → 0%). Dano: 60 (2x do normal). Screen shake: 4px, 200ms. SFX "massive_slam" + camera flash.** |
| 3 | 250 | Pousa heroicamente. **Particulas assentam. Aura volta a normal. SPAWN texto "Nos tempos da Lava Jato..." (branco, fade in, float up 24px em 2s, fade out). SFX "hero_land".** |

**Mecanica:**
- Dano: 60 (2x attack normal)
- Raio de efeito: 128px (onda de choque)
- Cooldown: 30 segundos
- IMPORTANTE: O dano deste special REDUZ a cada estagio (60 → 40 → 20 → 5)

---

## ESTAGIO 2: DESGASTADO (Waves 4-6)

### Diferencas Mecanicas do Estagio 1
- **Attack dano**: 30 → 22 (-27%)
- **Special dano**: 60 → 40 (-33%)
- **Walk speed**: 100% → 90%
- **Attack FPS**: 10 → 9 (levemente mais lento)
- **Aura**: Dourada → Amarelo-parda, alpha 40% → 25%

### IDLE
```
Nome: moro_s2_idle
Arquivo: moro-stage2-worn.png
Frames: 4 (row 0, cols 0-3)
FPS: 9 (levemente mais lento)
Loop: true
```

| Frame | Duracao (ms) | Descricao |
|-------|-------------|-----------|
| 0 | 110 | Quase ereto. Ombros levemente caidos. Martelo pesando no ombro. Olheiras leves. |
| 1 | 130 | SUSPIRO (peito infla e esvazia). Olhos desviam para baixo. Martelo escorrega 1px. |
| 2 | 110 | Tenta puxar ombros para cima (FALHA - voltam a cair). Gravata torta. |
| 3 | 130 | Olhar distante. Acaricia cabo martelo. Boca move ("Eu era respeitado..."). |

---

### WALK
```
Nome: moro_s2_walk
Arquivo: moro-stage2-worn.png
Frames: 6 (row 1, cols 0-5)
FPS: 9
Loop: true
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 110 | Passos MENORES. Martelo mais pesado. |
| 1 | 110 | Arrasto leve no pe. Corpo inclinando. |
| 2 | 110 | Terno amassando nas dobras. |
| 3 | 130 | Olha para tras (nostalgia). **SFX "sigh" leve.** |
| 4 | 110 | Volta a frente. Suspiro. |
| 5 | 110 | Postura pior que inicio. |

---

### ATTACK
```
Nome: moro_s2_attack
Arquivo: moro-stage2-worn.png
Frames: 3 (row 2, cols 0-2)
FPS: 9
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 140 | Ergue martelo com esforco VISIVEL. Bracos tremem. **SFX "strain".** |
| 1 | 100 | Golpe 70% forca. **SPAWN impacto (estrela menor 24x24, amarelo-desbotado, 3 frames). Dano: 22. SFX "hammer_thud" (menos potente). Sem screen shake.** |
| 2 | 180 | Pos-golpe ofegante. Mais tempo para recuperar. **SFX "heavy_breath".** |

---

### DEATH / HIT / SPECIAL
Mesma estrutura do Estagio 1 mas:
- **Death**: Menos dramatico, mais resignado
- **Hit**: Recuperacao mais lenta (frame 1: 120ms ao inves de 80ms)
- **Special**: Dano 40 ao inves de 60, aura amarelo-parda, particulas menos brilhantes

---

## ESTAGIO 3: DECADENTE (Waves 7-9)

### Diferencas Mecanicas
- **Attack dano**: 22 → 12 (-45%)
- **Special dano**: 40 → 20 (-50%)
- **Walk speed**: 90% → 70%
- **Attack FPS**: 9 → 7 (visivelmente mais lento)
- **Aura**: Cinza (#808080), alpha 15%, quase estatica
- **NOVO**: Particulas de ferrugem caindo do martelo PERMANENTEMENTE

### IDLE
```
Nome: moro_s3_idle
Arquivo: moro-stage3-decadent.png
Frames: 4 (row 0, cols 0-3)
FPS: 7
Loop: true
```

| Frame | Duracao (ms) | Descricao |
|-------|-------------|-----------|
| 0 | 150 | Postura CURVADA. Ombros CAIDOS 15 graus. Martelo enferrujado arrastando (nao no ombro). Olheiras PROFUNDAS. |
| 1 | 170 | Cabeca pende. Quase cochila. Martelo quase cai. **SPAWN particula ferrugem (1x).** |
| 2 | 140 | Acorda com susto leve. Tenta se recompor. Falha. **SFX "startled_weak".** |
| 3 | 170 | Suspiro PESADO. Corpo afunda. "A justica... a justica..." (boca move, nao completa). **SPAWN particula ferrugem (1x).** |

**Particulas de ferrugem permanentes:**
- Tamanho: 4x4px
- Cor: #8B6914 (laranja-ferrugem)
- Spawn rate: 1 a cada 700ms durante idle, 1 a cada 400ms durante walk
- Gravidade: 150px/s^2
- Lifetime: 800ms
- Origem: cabeca do martelo

---

### WALK
```
Nome: moro_s3_walk
Arquivo: moro-stage3-decadent.png
Frames: 6 (row 1, cols 0-5)
FPS: 7
Loop: true
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 150 | ARRASTA pes. Martelo arrastando no chao. **SPAWN risco de ferrugem no chao (particula linear, 2x2px, lifetime 3s). SPAWN ferrugem (1x).** |
| 1 | 140 | Cada passo um esforco. Terno desajustado. |
| 2 | 160 | TROPECA. Martelo enrosca. **SFX "stumble". SPAWN ferrugem (2x).** |
| 3 | 140 | Recupera mas quase cai. Amargura. |
| 4 | 140 | Arrasta. Olha pro chao. |
| 5 | 160 | Mais curvado que inicio. **Rastro de ferrugem visivel atras.** |

---

### ATTACK
```
Nome: moro_s3_attack
Arquivo: moro-stage3-decadent.png
Frames: 3 (row 2, cols 0-2)
FPS: 7
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 200 | TENTA erguer martelo. TREME muito. Mal sai da cintura. **SFX "struggle_lift". SPAWN ferrugem (3x do esforco).** |
| 1 | 130 | Golpe FRACO. Martelo mal sai do chao. **SPAWN ferrugem_scatter (5-6 particulas, raio 16px). Dano: 12. SFX "weak_thud" (pathetic). ZERO screen shake.** |
| 2 | 250 | Apoiado no martelo como BENGALA. Exausto. **SFX "exhausted_breath". Frame longo = patetismo.** |

---

### DEATH
```
Nome: moro_s3_death
Arquivo: moro-stage3-decadent.png
Frames: 4 (row 3, cols 0-3)
FPS: 5
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 200 | Quase ALIVIO na expressao. Martelo solta facil. |
| 1 | 250 | Cai de joelhos. Olheiras metade do rosto. **SFX "resigned_fall".** |
| 2 | 250 | Cai sentado. **Martelo QUEBRA em dois (SPAWN 2 pedacos: cabo + cabeca, voam em direcoes opostas). SPAWN ferrugem (10x explosion). SFX "metal_break".** |
| 3 | 400 | Deitado. Olhos abertos olhando o teto. VAZIO. **Pecas de ferrugem assentam. Aura cinza desaparece. SFX silencio total.** |

---

## ESTAGIO 4: IRRELEVANTE (Waves 10+)

### Diferencas Mecanicas
- **Attack dano**: 12 → 3 (-75%)
- **Special dano**: 20 → 5 (-75%)
- **Walk speed**: 70% → 50%
- **Attack FPS**: 7 → 5 (lentissimo)
- **Aura**: NENHUMA
- **Opacidade geral**: 85% (fantasma)
- **Particulas de ferrugem**: Frequencia dobrada (constante desmoronamento)
- **NOVO**: NPCs/inimigos ignoram Moro (aggro priority: -100)

### IDLE
```
Nome: moro_s4_idle
Arquivo: moro-stage4-irrelevant.png
Frames: 4 (row 0, cols 0-3)
FPS: 5 (lentissimo = quase estatico)
Loop: true
```

| Frame | Duracao (ms) | Descricao |
|-------|-------------|-----------|
| 0 | 200 | Formato "C". Ombros ao nivel da cintura. Martelo quebrado pendurado. Olheiras MONSTRO. Alpha 85%. **SPAWN ferrugem constante.** |
| 1 | 250 | Balanca (quase cai dormindo em pe). Baba. **SFX nenhum (silencio e pior que som).** |
| 2 | 200 | Murmura inaudivel. Olhos OPACOS. Mao treme. **Ferrugem do martelo cai.** |
| 3 | 250 | Pisca de volta a realidade. Olha martelo quebrado com TRISTEZA. Volta ao vazio. |

---

### WALK
```
Nome: moro_s4_walk
Arquivo: moro-stage4-irrelevant.png
Frames: 6 (row 1, cols 0-5)
FPS: 5
Loop: true
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 200 | Mal se move. Arrasta TUDO. Corpo em "C". Alpha 85%. **Ferrugem trail constante.** |
| 1 | 200 | Um passo leva o tempo de dois. Terno rasgado esvoaca. |
| 2 | 250 | PARA. Esqueceu pra onde ia. Olhos vagam. **SFX "..." (literalmente silencio intencional).** |
| 3 | 200 | Lembra (ou nao). Continua com dificuldade. |
| 4 | 200 | Tropecar sem recuperacao. Quase rastejando. |
| 5 | 200 | "Andando" mas parece um ZUMBI. Alpha flickers 85% ↔ 75%. |

---

### ATTACK
```
Nome: moro_s4_attack
Arquivo: moro-stage4-irrelevant.png
Frames: 3 (row 2, cols 0-2)
FPS: 5
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 250 | "Tenta" erguer martelo quebrado. Cabeca balanca no prego. **Nenhum SFX. Nada.** |
| 1 | 200 | Martelo cai por GRAVIDADE. **Dano: 3. NENHUM efeito visual. Nenhuma particula. Nenhum som de impacto. Silencio.** |
| 2 | 300 | Apoiado no cabo. "Por que eu ainda tento?" **Frame extra longo = futilidade pura.** |

---

### DEATH
```
Nome: moro_s4_death
Arquivo: moro-stage4-irrelevant.png
Frames: 4 (row 3, cols 0-3)
FPS: 4 (mais lento de todos = ARRASTADO)
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 200 | Mal nota o hit. Diferenca minima. |
| 1 | 300 | Simplesmente SENTA. Nao dramatico. So senta. **SFX "cloth_rustle" (unico som - o corpo sentando).** |
| 2 | 400 | Deita DEVAGAR como se fosse dormir. Olhos fecham. Expressao quase de PAZ. |
| 3 | 500 | Deitado. **FADE OUT: alpha 85% → 0% em 2000ms (LENTO). Ninguem nota que morreu. Martelo dissolve em ferrugem (SPAWN 15 particulas de ferrugem que se dispersam lentamente). Nenhum som. Vazio absoluto.** |

**Pos-morte:** SEM permanencia do sprite. Fade out gradual de 2 segundos. O jogo continua como se nada tivesse acontecido.

---

### SPECIAL: Heroi Decaido (Estagio 4 - Poder Esgotado)
```
Nome: moro_s4_special
Arquivo: moro-stage4-irrelevant.png
Frames: 4 (row 5, cols 0-3)
FPS: 5
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 250 | Tenta aura dourada: sai CINZA OPACA. **Tint cinza (#808080) em vez de dourado. Alpha aura: 10%. SPAWN particulas cinzas (5, lentas). Nenhum SFX heroico - so vento.** |
| 1 | 200 | "Salta" 2 pixels. **Sprite Y -= 2px (patetico). Martelo acima da cabeca 0.1s (100ms) antes de DESPENCAR. Sem brilho.** |
| 2 | 150 | Martelo cai por gravidade. **Impacto: NADA. Zero efeito. Zero som. Dano: 5 (90% menos que Estagio 1). Screen shake: 0.** |
| 3 | 350 | Olha martelo no chao. **SPAWN texto "Nos tempos da Lava Jato..." (CINZA ao inves de branco, 50% alpha, fade out rapido em 1s). Particulas cinzas dissipam. TRISTEZA pura.** |

---

## TRANSICOES DE DEGRADACAO

### Transicao 1→2 (Inicio Wave 4)
```
Nome: moro_degrade_1to2
Arquivo: moro-transitions.png
Frames: 4 (cols 0-3)
Dimensao: 256x64px
FPS: 4 (lento, dramatico)
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 300 | Para. Olha maos. Tremor. **FREEZE input 1.5s. Camera leve zoom 105%. SFX "realization_sting".** |
| 1 | 300 | Ombros DESCEM 5 graus. Terno AMASSA. Gravata TORCE. **Tween ombros: posY += 2px. Tween terno: add wrinkle overlay. SFX "cloth_wrinkle".** |
| 2 | 300 | Olheiras FADE IN. Martelo ESCURECE. **Tween olheiras: alpha 0% → 100%. Tween martelo: tint shift chrome → dull. SFX "metal_aging".** |
| 3 | 400 | SUSPIRO. Novo visual completo. **SFX "deep_sigh". Camera zoom volta 100%. Input liberado. SWAP sprite sheet para stage2.** |

---

### Transicao 2→3 (Inicio Wave 7)
```
Nome: moro_degrade_2to3
Arquivo: moro-transitions.png
Frames: 4 (cols 4-7)
FPS: 4
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 300 | Para. Olha martelo. FERRUGEM aparece ao vivo. **SPAWN particulas ferrugem no martelo (crescendo). Camera zoom 105%. SFX "rust_forming".** |
| 1 | 350 | Ombros DESPENCAM +10 graus. Terno amassa SEVERAMENTE. Cabelo GRISALHA. **Tween ombros: posY += 4px. Tween cabelo: tint shift brown → gray. SFX "aging_accelerated".** |
| 2 | 350 | Olheiras DOBRAM. Rugas SURGEM. Gravata AFROUXA. **Tween olheiras: scale 100% → 200%. SPAWN wrinkle lines overlay. SFX "face_aging".** |
| 3 | 400 | GRUNHIDO de dor. Martelo agora arrastando. **SFX "pain_grunt". Camera volta. SWAP para stage3. Particula system ativado (ferrugem constante).** |

---

### Transicao 3→4 (Inicio Wave 10)
```
Nome: moro_degrade_3to4
Arquivo: moro-transitions.png
Frames: 4 (cols 8-11)
FPS: 3 (o mais lento = o mais depressivo)
Loop: false
```

| Frame | Duracao (ms) | Evento |
|-------|-------------|--------|
| 0 | 400 | Para. OLHA PARA O JOGADOR (quarta parede). "Voce ainda esta me vendo?" **Camera zoom 110%. Sprite vira em direcao a camera. SFX: nenhum (silencio mais assustador que som).** |
| 1 | 400 | Corpo COLAPSA para "C". Ombros ao nivel da cintura. Terno PERDE COR. **Tween body: posture curve. Tween suit: desaturate 100%. SFX "collapse_slow".** |
| 2 | 400 | Opacidade cai para 85%. Martelo QUEBRA. Olheiras MONSTRO. **Tween alpha: 100% → 85%. SFX "metal_snap" (martelo quebrando). SPAWN 2 pedacos de martelo. Tween olheiras: scale → 300%.** |
| 3 | 500 | SILENCIO. Nenhuma expressao. Novo visual completo. **Camera volta. SFX: NADA. Absolutamente nada. SWAP para stage4. O mais deprimente frame do jogo.** |

---

## MAQUINA DE ESTADOS

```
                    ┌───────────────────────┐
                    │     STAGE MANAGER     │
                    │  (wave-based swap)     │
                    └───┬───┬───┬───┬───────┘
                        │   │   │   │
                   S1   S2  S3  S4
                   │    │   │   │
    Cada estagio tem:   │   │   │
                        ↓   ↓   ↓
              ┌──────────────────────────┐
              │   PER-STAGE STATE MACHINE │
              └──────────┬───────────────┘
                         │
                  ┌──────┴──────┐
                  │    IDLE     │ ← default
                  └──────┬──────┘
                         │
          ┌──────────────┼──────────────┬──────────────┐
          ↓              ↓              ↓              ↓
     ┌────────┐   ┌──────────┐   ┌──────────┐  ┌──────────┐
     │  WALK  │   │  ATTACK  │   │   HIT    │  │ SPECIAL  │
     └───┬────┘   └────┬─────┘   └────┬─────┘  └────┬─────┘
         │             │              │              │
         └─────────────┴──────────────┴──────────────┘
                              │
                              ↓
                       ┌──────────┐
                       │  DEATH   │ (terminal)
                       └──────────┘
```

**Regra de stage swap:**
1. Detecta wave transition
2. FREEZE current animation
3. Play transicao (moro_degrade_XtoY)
4. Ao final da transicao: SWAP sprite sheet reference
5. RESUME com idle do novo estagio

**Prioridades (igual para todos estagios):**
1. IDLE (0)
2. WALK (1)
3. SPECIAL (2)
4. ATTACK (3)
5. HIT (4)
6. DEATH (5)
7. STAGE_TRANSITION (6) - prioridade maxima

---

## TABELA DE DEGRADACAO MECANICA

| Parametro | S1 (Heroi) | S2 (Desgastado) | S3 (Decadente) | S4 (Irrelevante) |
|-----------|-----------|-----------------|----------------|-------------------|
| Attack Dano | 30 | 22 | 12 | 3 |
| Special Dano | 60 | 40 | 20 | 5 |
| Walk Speed | 100% | 90% | 70% | 50% |
| Anim FPS | 10 | 9 | 7 | 5 |
| Aura | Dourada 40% | Parda 25% | Cinza 15% | Nenhuma |
| Opacidade | 100% | 100% | 100% | 85% |
| Ferrugem | Nao | Nao | Sim (lenta) | Sim (constante) |
| Aggro Inimigos | Normal | Normal | Reduzido (-50%) | Ignorado (-100) |
| Impacto Visual | Grande | Medio | Minimo | Nenhum |
| Screen Shake | Sim | Nao | Nao | Nao |

---

## PHASER 3 - EXEMPLO DE IMPLEMENTACAO

```javascript
// Referencia para implementacao
class MoroCharacter {
  constructor(scene) {
    this.currentStage = 1;
    this.spriteSheets = {
      1: 'moro-stage1-hero',
      2: 'moro-stage2-worn',
      3: 'moro-stage3-decadent',
      4: 'moro-stage4-irrelevant'
    };
    this.degradationStats = {
      1: { damage: 30, specialDmg: 60, speed: 1.0, fps: 10, auraAlpha: 0.4, opacity: 1.0 },
      2: { damage: 22, specialDmg: 40, speed: 0.9, fps: 9, auraAlpha: 0.25, opacity: 1.0 },
      3: { damage: 12, specialDmg: 20, speed: 0.7, fps: 7, auraAlpha: 0.15, opacity: 1.0 },
      4: { damage: 3, specialDmg: 5, speed: 0.5, fps: 5, auraAlpha: 0, opacity: 0.85 }
    };
  }

  onWaveChange(waveNumber) {
    const newStage = waveNumber <= 3 ? 1 : waveNumber <= 6 ? 2 : waveNumber <= 9 ? 3 : 4;
    if (newStage !== this.currentStage) {
      this.playDegradationTransition(this.currentStage, newStage);
    }
  }

  playDegradationTransition(from, to) {
    // Freeze input
    // Play transition animation
    // Swap sprite sheet
    // Apply new stats
    // Resume
  }
}
```

---

## NOTAS DE IMPLEMENTACAO

1. **4 sprite sheets separadas** sao mais limpas que 1 mega-sheet para swap em runtime
2. A transicao de degradacao INTERROMPE qualquer acao (prioridade maxima)
3. O sistema de particulas de ferrugem (Estagios 3-4) deve ser INDEPENDENTE do sprite
4. No Estagio 4, a opacidade 85% se aplica ao sprite E a todas as particulas associadas
5. A ausencia de efeitos no Estagio 4 e INTENCIONAL - o silencio conta a historia
6. A morte no Estagio 4 com fade to 0 em 2 segundos e o momento mais impactante do personagem
7. NENHUMA interpolacao entre frames em NENHUM estagio (snap = estilo Andre Guedes)
8. O olhar para a quarta parede na transicao 3→4 requer que o sprite ROTACIONE para facing camera (breaking convention)
