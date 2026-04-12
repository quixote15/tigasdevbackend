# SERGIO MORO (O Heroi Decaido) - Script de Audio

## NPC / Ex-Aliado que Muda de Lado - "Zumbis de Brasilia"

---

## CONFIGURACAO TECNICA

- **Formato**: OGG Vorbis (primario) + MP3 (fallback)
- **Sample rate**: 44100 Hz
- **Bit depth**: 16-bit
- **Canais**: Mono (para posicional audio / panning)
- **Volume padrao**: Varia por estagio (parte da mecanica de degradacao)
- **Compressao**: -16 LUFS (loudness normalizado)

---

## SISTEMA DE DEGRADACAO SONORA

Assim como o visual, o AUDIO do Moro degrada ao longo dos estagios. Cada bordao tem 4 versoes.

| Parametro | S1 (Heroi) | S2 (Desgastado) | S3 (Decadente) | S4 (Irrelevante) |
|-----------|-----------|-----------------|----------------|-------------------|
| Volume geral | 0.8 | 0.65 | 0.5 | 0.3 |
| Tom de voz | Grave, firme | Medio, cansado | Rouco, fraco | Sussurro, quase inaudivel |
| Velocidade | Normal | Levemente lenta | Lenta | Arrastada |
| Confianca | 100% | 65% | 30% | 0% |
| Efeito de processamento | Nenhum (limpo) | Leve reverb (eco da duvida) | Reverb + lowpass (distante) | Reverb pesado + lowpass + volume baixissimo (fantasma) |

---

## VOZES - ESTAGIO 1 (HEROI)

### Direcao de Voz - Estagio 1
- **Tom**: GRAVE, firme, AUTORITARIO
- **Velocidade**: Decidida, sem hesitacao
- **Sotaque**: Curitibano/paranaense, pronuncia clara
- **Personalidade vocal**: Juiz implacavel. Cada palavra e um veredito. Confianca absoluta.
- **Referencia**: Narrador de documentario sobre justica + heroi de acao dos anos 80

---

### BORDAO 1: "Nos tempos da Lava Jato..."
```
Arquivo: moro_s1_vo_lavajato.ogg
Texto: "Nos tempos da Lava Jato..."
Entonacao: NOSTALGICO mas ORGULHOSO. Como veterano de guerra contando historias.
             "Nos tempos"(tom grave, solene, olhar distante)
             "da Lava Jato..."(tom subindo com orgulho, ponto final firme)
Duracao: 2.0 segundos
Volume: 0.8
Trigger: Ativar special "Heroi Decaido" / Idle ha mais de 20 segundos
Cooldown: 30 segundos
```

**Variante Estagio 2:**
```
Arquivo: moro_s2_vo_lavajato.ogg
Mesma frase, mas: tom mais CANSADO, leve suspiro antes, velocidade 90%
Volume: 0.65
Duracao: 2.3 segundos
```

**Variante Estagio 3:**
```
Arquivo: moro_s3_vo_lavajato.ogg
Mesma frase, mas: voz ROUCA e FRACA, pausa longa no meio ("Nos tempos... da Lava Jato..."),
como se lembrasse com dor. Reverb de eco (voz perdida em corredor vazio).
Volume: 0.5
Duracao: 3.0 segundos
```

**Variante Estagio 4:**
```
Arquivo: moro_s4_vo_lavajato.ogg
Mesma frase, mas: quase INAUDIVEL. Sussurro. Nao completa - "Nos tempos da..."
e para. Silencio. Nao tem forca pra terminar. Reverb pesado como se falasse
numa sala vazia enorme.
Volume: 0.3
Duracao: 2.5 segundos (com 1s de silencio no final)
```

---

### BORDAO 2: "Eu era respeitado, sabia?"
```
Arquivo: moro_s1_vo_respeitado.ogg
Texto: "Eu era respeitado, sabia?"
Entonacao: AFIRMATIVO, sem duvida. Nao e pergunta, e declaracao.
             "Eu era respeitado,"(firme, factual)
             "sabia?"(retorico, queixo erguido)
Duracao: 1.8 segundos
Volume: 0.8
Trigger: Encontrar outro NPC / proximo a inimigos
Cooldown: 30 segundos
```

**Variante Estagio 2:**
```
Arquivo: moro_s2_vo_respeitado.ogg
Tom DEFENSIVO. Precisando se convencer. "Eu ERA respeitado, sabia?" (enfase no ERA).
Volume: 0.65. Duracao: 2.0s
```

**Variante Estagio 3:**
```
Arquivo: moro_s3_vo_respeitado.ogg
Tom SUPLICANTE. Perguntando de verdade, nao mais retorico.
"Eu era respeitado... sabia?" (voz quebrando, quase chorando)
Volume: 0.5. Duracao: 2.5s
```

**Variante Estagio 4:**
```
Arquivo: moro_s4_vo_respeitado.ogg
Quase INAUDIVEL. Murmura para si mesmo. Ninguem ouve.
"...respeitado..." (so o meio da frase, sussurro)
Volume: 0.25. Duracao: 1.0s
```

---

### BORDAO 3: "A justica... a justica..."
```
Arquivo: moro_s1_vo_justica.ogg
Texto: "A justica prevalece!"
Entonacao: PROCLAMACAO. Veredito final. Martelo batendo.
             "A justica"(solene, grave)
             "prevalece!"(forte, definitivo, ponto de exclamacao sonoro)
Duracao: 1.5 segundos
Volume: 0.85
Trigger: Eliminar inimigo / Attack conecta
Cooldown: 15 segundos
```

**Variante Estagio 2:**
```
Arquivo: moro_s2_vo_justica.ogg
"A justica... prevalece." Menos enfatico. Ponto final ao inves de exclamacao.
Pausa no meio (hesitacao). Volume: 0.6. Duracao: 2.0s
```

**Variante Estagio 3:**
```
Arquivo: moro_s3_vo_justica.ogg
"A justica... a justica..." NAO COMPLETA A FRASE. Voz quebrando. Repete
"a justica" como disco arranhado tentando lembrar o que vem depois.
Volume: 0.45. Duracao: 2.5s
```

**Variante Estagio 4:**
```
Arquivo: moro_s4_vo_justica.ogg
"...justica..." Uma unica palavra. Sussurro. Sem contexto. Sem frase.
So o eco de algo que um dia significou alguma coisa.
Volume: 0.2 (quase silencio). Duracao: 1.5s (1s e silencio)
```

---

### BORDAO 4: "CONDENADO!"
```
Arquivo: moro_s1_vo_condenado.ogg
Texto: "CONDENADO!"
Entonacao: VEREDITO. Grito de poder. Martelo descendo.
             "CON-DE-NA-DO!"(cada silaba martelada, crescendo, climax no DO!)
Duracao: 0.8 segundos
Volume: 0.9 (ALTO - momento de poder)
Trigger: Attack frame 1 (golpe de martelo)
Cooldown: 5 segundos
Variantes: 3 gravacoes (intensidade variada)
```

**Variante Estagio 2:**
```
Arquivo: moro_s2_vo_condenado.ogg
"Condenado." Menos enfatico. Mais como carimbo burocratico que veredito epico.
Volume: 0.65. Duracao: 0.7s
```

**Variante Estagio 3:**
```
Arquivo: moro_s3_vo_condenado.ogg
"Cond..." Comeca mas nao termina. Falta folego. Voz falha no meio.
Volume: 0.4. Duracao: 0.5s
```

**Variante Estagio 4:**
```
Arquivo: moro_s4_vo_condenado.ogg
SILENCIO. Nenhum som. O ataque nao tem voz.
(Arquivo existe mas contem 0.3s de silencio intencional)
Volume: 0.0. Duracao: 0.3s
```

---

### BORDAO 5: "Ja vi esse filme antes."
```
Arquivo: moro_s1_vo_filme.ogg
Texto: "Ja vi esse filme antes."
Entonacao: CÍNICO, sabedoria de quem conhece os truques.
             "Ja vi"(casual, confiante)
             "esse filme antes."(olhos estreitados, sorriso sutil)
Duracao: 1.5 segundos
Volume: 0.7
Trigger: Encontrar boss / situacao de perigo
Cooldown: 45 segundos
```

**Estagio 4:**
```
Arquivo: moro_s4_vo_filme.ogg
"Ja vi..." (trail off. Nao lembra o resto. Ou nao importa mais.)
Volume: 0.25. Duracao: 1.0s
```

---

### BORDAO 6: "Pra tras! Em nome da lei!"
```
Arquivo: moro_s1_vo_lei.ogg
Texto: "Pra tras! Em nome da lei!"
Entonacao: COMANDO MILITAR. Ordem inapelavel.
             "Pra tras!"(grito breve, autoritario)
             "Em nome da lei!"(grave, majestoso)
Duracao: 1.5 segundos
Volume: 0.85
Trigger: Receber hit (counter-attack voice)
Cooldown: 20 segundos
```

**Estagio 4:**
```
Arquivo: moro_s4_vo_lei.ogg
"...lei..." (sussurro patologico. A lei e um fantasma. Ele e um fantasma.)
Volume: 0.15. Duracao: 0.5s
```

---

## VOZES - TRANSICOES DE DEGRADACAO

### Transicao 1→2 (Wave 4)
```
Arquivo: moro_degrade_1to2_vo.ogg
Texto: [Sequencia]
  0.0s - Suspiro pesado (exalacao longa)
  0.5s - "Hm." (surpresa contida ao perceber cansaco)
  1.0s - "Eu consigo. Eu consigo..." (repetindo para se convencer, voz levemente tremula)
Duracao: 2.0 segundos
Volume: 0.7
```

### Transicao 2→3 (Wave 7)
```
Arquivo: moro_degrade_2to3_vo.ogg
Texto: [Sequencia]
  0.0s - Gemido de dor/cansaco (grave, gutural)
  0.5s - "O que... aconteceu comigo?" (genuinamente confuso, voz quebrando)
  1.5s - "Eu era..." (nao completa. Silencio.)
Duracao: 2.5 segundos
Volume: 0.55
```

### Transicao 3→4 (Wave 10)
```
Arquivo: moro_degrade_3to4_vo.ogg
Texto: [Sequencia]
  0.0s - NADA por 1 segundo inteiro (silencio)
  1.0s - Sussurro quase inaudivel: "...alguem..." (perguntando se alguem nota)
  1.8s - Silencio novamente
  2.5s - Exalacao (o ultimo som com intencao)
  3.0s - Silencio permanente
Duracao: 3.5 segundos
Volume: 0.3 decrescendo para 0.1
Nota: O SILENCIO e o som mais importante desta transicao.
```

---

## VOZES - DEATH (por Estagio)

### Death Estagio 1
```
Arquivo: moro_s1_vo_death.ogg
Texto: "Nao! Isso nao pode..." (incredulidade heroica)
Entonacao: CHOQUE. Heroi que nao aceita cair.
Duracao: 1.2 segundos
Volume: 0.8
```

### Death Estagio 2
```
Arquivo: moro_s2_vo_death.ogg
Texto: "Eu... deveria ter ficado no tribunal..." (arrependimento)
Entonacao: Resignacao com um toque de arrependimento.
Duracao: 2.0 segundos
Volume: 0.6
```

### Death Estagio 3
```
Arquivo: moro_s3_vo_death.ogg
Texto: "Pelo menos... acaba..." (alivio)
Entonacao: ALIVIO genuino. Cansaco terminando.
Duracao: 1.5 segundos
Volume: 0.4
```

### Death Estagio 4
```
Arquivo: moro_s4_vo_death.ogg
Texto: [SILENCIO TOTAL]
Nota: Nenhum som. Nada. Ele morre sem que ninguem note.
O arquivo contem 2 segundos de silencio absoluto.
Duracao: 2.0 segundos
Volume: 0.0
```

---

## SFX (Efeitos Sonoros)

### Martelo de Juiz (4 Estagios)
| Arquivo | Estagio | Descricao | Duracao |
|---------|---------|-----------|---------|
| sfx_hammer_s1_swing.ogg | S1 | Whoosh potente (martelo cortando ar com velocidade) | 0.3s |
| sfx_hammer_s1_impact.ogg | S1 | SLAM pesado + eco de tribunal (poderoso, reverberante) | 0.5s |
| sfx_hammer_s2_swing.ogg | S2 | Whoosh mais fraco + rangido de madeira | 0.3s |
| sfx_hammer_s2_impact.ogg | S2 | Thud pesado sem eco (perda de majestade) | 0.4s |
| sfx_hammer_s3_swing.ogg | S3 | Arrasto no chao + rangido de ferrugem | 0.4s |
| sfx_hammer_s3_impact.ogg | S3 | Thud fraco + particulas de ferrugem (tinido seco) | 0.3s |
| sfx_hammer_s4_swing.ogg | S4 | Quase silencio. Rangido fraco de prego solto. | 0.2s |
| sfx_hammer_s4_impact.ogg | S4 | NADA. O martelo cai sem som de impacto. Silencio. | 0.1s |

### Passos (4 Estagios)
| Arquivo | Estagio | Descricao | Duracao |
|---------|---------|-----------|---------|
| sfx_step_s1.ogg | S1 | Passo FIRME de bota (boot on marble, decidido) | 0.2s |
| sfx_step_s2.ogg | S2 | Passo mais suave (sapato em carpete) | 0.15s |
| sfx_step_s3.ogg | S3 | Arrasto (sola raspando no chao) | 0.25s |
| sfx_step_s4.ogg | S4 | Quase inaudivel (shuffle fraco, fantasma) | 0.1s |

### Ferrugem (Estagios 3-4)
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_rust_flake.ogg | Lascas de ferrugem caindo (tinido seco minusculo) | 0.1s | Particula ferrugem spawn |
| sfx_rust_crumble.ogg | Ferrugem desmoronando (crepitar seco) | 0.3s | Attack impact S3-S4 |
| sfx_hammer_break.ogg | Martelo quebrando em dois (CRACK metalico + madeira) | 0.5s | Death S3 frame 2 / Transicao 3→4 |

### Transicoes de Degradacao
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_degrade_sting.ogg | Nota musical descendente (violino, triste, lenta) | 1.5s | Inicio de transicao |
| sfx_cloth_wrinkle.ogg | Terno amassando (pano comprimindo) | 0.5s | Terno degradando |
| sfx_aging_bones.ogg | Ossos estalando (crac-crac suave) | 0.4s | Ombros caindo |
| sfx_fade_out.ogg | Tom decrescente ate silencio (representa desaparecimento) | 2.0s | Transicao 3→4 |

### Combate Geral
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_moro_hit_s1.ogg | Hit heroico (impacto + grunt surpreso) | 0.3s | Hit S1 |
| sfx_moro_hit_s4.ogg | Quase nada (pano amassando levemente) | 0.15s | Hit S4 |
| sfx_aura_pulse.ogg | Pulso de aura dourada (hum grave, etereo) | 0.5s | Aura pulsando S1 |
| sfx_aura_fade.ogg | Aura desaparecendo (hum decrescendo para silencio) | 1.5s | Death S1 / Transicao |

### Efeito de Impacto de Ataque (4 Estagios)
| Arquivo | Estagio | Descricao | Duracao |
|---------|---------|-----------|---------|
| sfx_impact_s1.ogg | S1 | Estrela dourada - shimmer brilhante + gong | 0.4s |
| sfx_impact_s2.ogg | S2 | Estrela menor - shimmer fraco | 0.3s |
| sfx_impact_s3.ogg | S3 | Ferrugem dispersa - crepitar seco | 0.25s |
| sfx_impact_s4.ogg | S4 | SILENCIO (arquivo vazio intencional) | 0.1s |

---

## MUSICA TEMATICA

### Tema do Moro (4 Estagios de Degradacao Musical)

#### Estagio 1 - Marcha Heroica
```
Arquivo: music_moro_s1.ogg
Estilo: Marcha triunfal orquestral. Fanfarra. Horns. Timbale.
BPM: 120 (decidido, marcial)
Instrumentos: Trompete (melodia heroica), timbales (percussao forte),
              cordas (harmonia majestosa), pratos (acentos)
Tom: Re maior (heroico, brilhante)
Melodia: Ascendente, confiante, resoluta
Loop: Sim
Duracao: 30 segundos (loop)
Volume: 0.7
```

#### Estagio 2 - Marcha Hesitante
```
Arquivo: music_moro_s2.ogg
Estilo: MESMA melodia do S1 mas: trompete DESAFINA levemente,
        timbales mais FRACOS, cordas com DISSONANCIA sutil,
        tempo DESACELERA para 110 BPM
BPM: 110
Tom: Re menor (mudanca sutil, tristeza emergente)
Volume: 0.55
Nota: O ouvinte deve sentir "algo esta errado" sem saber exatamente o que.
```

#### Estagio 3 - Elegia
```
Arquivo: music_moro_s3.ogg
Estilo: MESMA melodia mas agora em VIOLONCELO SOLO. Trompete sumiu.
        Timbales substituidos por heartbeat (batida cardiaca).
        Dissonancia ABERTA.
BPM: 80 (lento, arrastado)
Instrumentos: Violoncelo solo (melodia, choro), heartbeat (percussao),
              cordas graves sustentadas (drones), silencio entre frases
Tom: Si bemol menor (escuro, pesado)
Volume: 0.4
```

#### Estagio 4 - Silencio Quase Total
```
Arquivo: music_moro_s4.ogg
Estilo: Drone ambiental MINIMO. Nota unica sustentada. Nao e musica.
        E a AUSENCIA de musica. Ocasionalmente, um FRAGMENTO da melodia
        original aparece por 2-3 notas (fantasma musical) e desaparece.
BPM: Nenhum (ambient, sem ritmo)
Instrumentos: Drone de synth pad (frequencia baixa, 60Hz),
              fantasma de trompete (2-3 notas, reverb massivo, distante),
              silencio (o instrumento principal)
Tom: Indefinido (atonal, vazio)
Volume: 0.2
Nota: A MAIORIA do audio e silencio. Os fragmentos melodicos devem ser
      PERTURBADORAMENTE raros - 1 ocorrencia a cada 20 segundos.
```

### Transicao Musical entre Estagios
```
A transicao entre temas musicais deve ser um CROSSFADE de 3 segundos:
- Tema atual: fade out em 1.5s
- 1 segundo de silencio (respiro)
- Tema novo: fade in em 1.5s

Durante a animacao de transicao visual, usar sfx_degrade_sting como bridge.
```

---

## TABELA DE PRIORIDADE DE AUDIO

| Prioridade | Tipo | Exemplo | Pode Ser Cortado |
|-----------|------|---------|------------------|
| 1 (max) | Theme Music | music_moro_sX | Nao |
| 2 | Voice (bordao) | moro_sX_vo_lavajato | Sim (por mesmo de maior prioridade) |
| 3 | SFX combate | sfx_hammer_sX_impact | Nao |
| 4 | SFX ambiente | sfx_rust_flake | Sim |
| 5 | SFX transicao | sfx_degrade_sting | Nao (durante transicao tem prioridade 1) |
| 6 (min) | Silencio intencional | moro_s4_vo_death | Nao (o silencio e o som) |

**Max vozes simultaneas**: 6 canais (menos que Taxadd - Moro e mais "limpo" sonoramente)
**Espacializacao**: Pan baseado na posicao X
**Atenuacao**: SFX atenuam a 200px, silenciam a 500px

---

## DESIGN SONORO - FILOSOFIA

### O Som da Decadencia
O audio do Moro conta a MESMA historia que o visual: a queda de um heroi.

1. **Estagio 1**: CHEIO de som. Fanfarra. Gritos de poder. Impactos fortes. O jogador SENTE o poder.
2. **Estagio 2**: Sons comecam a FALHAR. Notas desafinam. Volumes caem. A duvida e audivel.
3. **Estagio 3**: MAIORIA dos sons desapareceu. O que resta e DISTORCIDO. A solidao e sonora.
4. **Estagio 4**: SILENCIO e o SOM. A ausencia total de audio E a mensagem. O unico som e o silencio.

### A Regra do Silencio
No Estagio 4, o silencio nao e um bug, e uma feature. Cada arquivo de audio do Estagio 4 que contem silencio DEVE existir como arquivo (nao pule o load). O sistema deve CARREGAR e TOCAR o silencio - porque o ato de tentar falar e nao conseguir e diferente de nao existir som.

---

## NOTAS DE PRODUCAO

1. Gravar TODAS as 4 variantes de cada bordao em SEQUENCIA na mesma sessao (manter consistencia do ator)
2. O ator de voz deve ser briefado: "Voce esta envelhecendo 30 anos em 4 takes"
3. Prioridade de gravacao: "CONDENADO!" (4 variantes) > "Nos tempos da Lava Jato..." (4v) > demais
4. Os SFX de martelo por estagio podem ser o MESMO sample com processing diferente (lowpass progressivo, volume reduction)
5. A musica dos 4 estagios deve ser composta como UMA peca que DEGRADA (nao 4 musicas separadas)
6. Testar o audio do Estagio 4 com FONES DE OUVIDO - deve ser quase inaudivel mas PRESENTE
7. O momento mais impactante sonoramente: a transicao 3→4 onde a musica vira drone e a voz vira silencio
8. Considerar usar IA de voz para prototipagem (ElevenLabs/Bark) antes de casting de ator final
9. O silencio intencional do S4 deve ser testado pelo QA - jogadores podem achar que o audio bugou
10. Incluir nos options: "Silencio do Moro e intencional" tooltip quando volume do Moro parece zerado
