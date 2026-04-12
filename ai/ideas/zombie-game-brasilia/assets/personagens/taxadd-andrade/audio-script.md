# TAXADD / ANDRADE - Script de Audio

## Mini-Boss (Taxadd) / NPC Inutil (Andrade) - "Zumbis de Brasilia"

---

## CONFIGURACAO TECNICA

- **Formato**: OGG Vorbis (primario) + MP3 (fallback)
- **Sample rate**: 44100 Hz
- **Bit depth**: 16-bit
- **Canais**: Mono (para posicional audio / panning)
- **Volume padrao**: 0.7 (70% do maximo)
- **Compressao**: -16 LUFS (loudness normalizado)

---

## VOZES - ANDRADE (NPC Inutil)

### Direcao de Voz
- **Tom**: Agudo-medio, FRACO, sem conviccao nenhuma
- **Velocidade**: Lenta, hesitante, com pausas de inseguranca
- **Sotaque**: Paulistano suave, sem carisma
- **Personalidade vocal**: Crianca perdida no corpo de adulto. Submisso. Confuso.
- **Referencia**: Imaginar alguem perguntando "com licenca?" num funeral

---

### BORDAO 1: "Que horas e a merenda?"
```
Arquivo: andrade_vo_merenda.ogg
Texto: "Que horas e a merenda?"
Entonacao: Pergunta genuina, esperancosa mas insegura.
             "Que horas"(tom subindo, curioso)
             "e a merenda?"(tom descendo com esperanca infantil)
Duracao: 1.8 segundos
Volume: 0.6 (mais baixo que outros - ele e irrelevante)
Trigger: Idle ha mais de 15 segundos / Proximo a itens de comida
Cooldown: 30 segundos
Variantes: 3 gravacoes diferentes (mesma frase, leves variacoes de timing)
```

### BORDAO 2: "Ninguem me ve..."
```
Arquivo: andrade_vo_invisivel.ogg
Texto: "Ninguem me ve..."
Entonacao: Triste mas resignado. Sem drama, so fato.
             "Ninguem"(tom neutro, quase sussurro)
             "me ve..."(trail off, voz sumindo)
Duracao: 1.5 segundos
Volume: 0.4 (MUITO baixo - quase inaudivel, como o personagem)
Trigger: Ativar special "Invisibilidade do Andrade"
Cooldown: 45 segundos
```

### BORDAO 3: "O Lula mandou eu vir aqui..."
```
Arquivo: andrade_vo_lula.ogg
Texto: "O Lula mandou eu vir aqui..."
Entonacao: Explicativo, como se justificasse existencia.
             "O Lula"(tom de reverencia, subserviente)
             "mandou eu vir aqui..."(trail off inseguro)
Duracao: 2.0 segundos
Volume: 0.5
Trigger: Spawn inicial / Primeiro encontro com jogador
Cooldown: 60 segundos (raro)
```

### BORDAO 4: "Posso ir embora?"
```
Arquivo: andrade_vo_embora.ogg
Texto: "Posso ir embora?"
Entonacao: Suplicante, cansado de estar ali.
             "Posso"(hesitante)
             "ir embora?"(esperancoso)
Duracao: 1.3 segundos
Volume: 0.5
Trigger: HP abaixo de 30%
Cooldown: 20 segundos
```

### BORDAO 5: "Trouxe um lanchinho..."
```
Arquivo: andrade_vo_lanchinho.ogg
Texto: "Trouxe um lanchinho..."
Entonacao: Timido, oferecendo algo que ninguem pediu.
             "Trouxe"(baixo, timido)
             "um lanchinho..."(levemente animado, esperando aprovacao)
Duracao: 1.5 segundos
Volume: 0.55
Trigger: Usar special "Merenda Infinita"
Cooldown: 30 segundos
```

---

## VOZES - TAXADD (Mini-Boss)

### Direcao de Voz
- **Tom**: GRAVE-MEDIO, AUTORITARIO, com entusiasmo compulsivo
- **Velocidade**: Rapida, decidida, sem hesitacao
- **Sotaque**: Paulistano mais forte, burocrata empoderado
- **Personalidade vocal**: Vilao que genuinamente acha que esta AJUDANDO. Entusiasmado com impostos. Compulsivo.
- **Referencia**: Vendedor de telemarketing que AMA o produto + vilao de desenho animado

---

### BORDAO 1: "TAXADO!"
```
Arquivo: taxadd_vo_taxado.ogg
Texto: "TAXADO!"
Entonacao: EXPLOSIVO. Grito de satisfacao. Como jogador de futebol gritando "GOL!"
             "TA-"(forte, staccato)
             "-XADO!"(mais forte ainda, prolongado, triunfante)
Duracao: 0.8 segundos
Volume: 0.9 (ALTO - e o bordao principal)
Trigger: Cada ataque da Calculadora Infernal que acerta
Cooldown: 3 segundos (pode repetir frequentemente)
Variantes: 5 gravacoes diferentes (variacoes de intensidade e timing)
  - taxadd_vo_taxado_01.ogg (neutro)
  - taxadd_vo_taxado_02.ogg (mais entusiasmado)
  - taxadd_vo_taxado_03.ogg (gritado)
  - taxadd_vo_taxado_04.ogg (sussurrado, sinistro)
  - taxadd_vo_taxado_05.ogg (cantado, melodico)
```

### BORDAO 2: "Ta cheio outra vez!"
```
Arquivo: taxadd_vo_cheio.ogg
Texto: "Ta cheio outra vez!"
Entonacao: Surpresa FALSA, fingindo que nao esperava.
             "Ta cheio"(tom de descoberta, olhos arregalando)
             "outra vez!"(satisfacao mal disfarçada)
Duracao: 1.5 segundos
Volume: 0.8
Trigger: Bolsos transbordando (visual de moedas no maximo)
Cooldown: 20 segundos
```

### BORDAO 3: "Nao e imposto, e contribuicao!"
```
Arquivo: taxadd_vo_contribuicao.ogg
Texto: "Nao e imposto, e contribuicao!"
Entonacao: CORRECAO enfatica, como professor corrigindo aluno.
             "Nao e imposto,"(negacao rapida, dedo levantado)
             "e contribuicao!"(tom de quem explica obviedade, sorrindo)
Duracao: 2.2 segundos
Volume: 0.75
Trigger: Ativar special "Taxa Infinita"
Cooldown: 60 segundos
```

### BORDAO 4: "Vou pensar em taxas mais democraticas!"
```
Arquivo: taxadd_vo_democraticas.ogg
Texto: "Vou pensar em taxas mais democraticas!"
Entonacao: PROMESSA falsa, politico prometendo.
             "Vou pensar"(pausado, pensativo teatral)
             "em taxas mais democraticas!"(acelerado, como se fosse convincente)
Duracao: 2.5 segundos
Volume: 0.7
Trigger: HP abaixo de 50% (tentando negociar)
Cooldown: 45 segundos
```

### BORDAO 5: "Simplificamos! Agora ninguem entende de forma mais eficiente!"
```
Arquivo: taxadd_vo_simplificamos.ogg
Texto: "Simplificamos! Agora ninguem entende de forma mais eficiente!"
Entonacao: ORGULHO genuino de uma conquista absurda.
             "Simplificamos!"(triunfante, como anuncio de novidade)
             "Agora ninguem entende"(tom natural, como se fosse normal)
             "de forma mais eficiente!"(clímax, orgulho maximo)
Duracao: 3.5 segundos
Volume: 0.75
Trigger: Ativar special "Reforma Tributaria" / "Taxacao Universal"
Cooldown: 90 segundos (raro - so para momentos epicos)
```

### BORDAO 6: "A economia agradece!"
```
Arquivo: taxadd_vo_economia.ogg
Texto: "A economia agradece!"
Entonacao: Paternalista, como se fizesse um favor.
             "A economia"(tom solene, respeitoso)
             "agradece!"(sorriso na voz, satisfacao)
Duracao: 1.5 segundos
Volume: 0.7
Trigger: Ao coletar moedas / drain resources de inimigos
Cooldown: 15 segundos
```

### BORDAO 7: "Imposto e amor!"
```
Arquivo: taxadd_vo_amor.ogg
Texto: "Imposto e amor!"
Entonacao: APAIXONADO, como se declarasse amor.
             "Imposto"(tom carinhoso, quase sussurrado)
             "e amor!"(explosao de paixao, coracoes na voz)
Duracao: 1.2 segundos
Volume: 0.8
Trigger: Ativar special "Taxa do Amor"
Cooldown: 45 segundos
```

---

## VOZES - TRANSFORMACAO

### Andrade → Taxadd
```
Arquivo: transform_andrade_taxadd.ogg
Texto: [Sequencia de sons, nao fala unica]
Sequencia:
  0.0s - Andrade: "Hm?" (surpresa suave, sussurro)
  0.3s - SFX: power-up surge (crescendo eletronico)
  0.8s - Voz distorcida (meio Andrade, meio Taxadd): "O que... o que esta..."
  1.5s - Taxadd emergindo: "Sim... SIM..."
  2.2s - Taxadd completo: "TAXADD!" (grito de nascimento do vilao)
  2.8s - Risada: "HAHAHA!" (risada grave, vilao)
Duracao total: 3.5 segundos
Volume: Crescendo de 0.4 a 0.9
Trigger: Animacao de transformacao
```

### Taxadd → Andrade (na Death)
```
Arquivo: transform_taxadd_andrade.ogg
Texto: [Sequencia reversa]
Sequencia:
  0.0s - Taxadd: "N-nao!" (surpresa, medo)
  0.5s - SFX: power-down (decrescendo eletronico)
  1.0s - Voz confusa (meio Taxadd, meio Andrade): "As taxas... as taxas..."
  1.5s - Andrade: "Que horas e a merenda?" (voz fraca, perdida)
  2.2s - Silencio
Duracao total: 2.5 segundos
Volume: Decrescendo de 0.8 a 0.3
Trigger: Death animation do Taxadd (frames 2-3)
```

---

## SFX (Efeitos Sonoros)

### Calculadora
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_calc_tap.ogg | Tecla de calculadora pressionada (bip agudo) | 0.1s | Idle frame 1 (digitando) |
| sfx_calc_charge.ogg | Calculadora carregando (crescendo eletronico, whine) | 0.5s | Attack frame 0 |
| sfx_calc_fire.ogg | Disparo de cifras (pew metalico + tinido de moeda) | 0.3s | Attack frame 1 |
| sfx_calc_display.ogg | Resultado na tela (ding satisfatorio) | 0.2s | Idle frame 2 |

### Moedas
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_coin_drop.ogg | Moeda caindo no chao (tinido metalico pequeno) | 0.2s | Particula moeda spawn |
| sfx_coin_bounce.ogg | Moeda quicando (tinido + impact suave) | 0.15s | Particula moeda bounce |
| sfx_coin_cascade.ogg | Cascata de moedas (multiplos tinidos sobrepostos) | 1.0s | Death frame 1 (bolsos explodem) |
| sfx_coin_roll.ogg | Moeda rolando (tinido decrescente, metalico) | 1.5s | Death frame 3 (ultima moeda) |
| sfx_coin_pocket.ogg | Moedas entrando no bolso (tinido + pano) | 0.3s | Drain de recursos |

### Carimbo
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_stamp_hit.ogg | Carimbo batendo (THUMP grave + tinta espirrando) | 0.3s | Efeito "TAXADO" aparecendo |
| sfx_stamp_ink.ogg | Tinta de carimbo (splash molhado) | 0.15s | Carimbo tocando superficie |

### Merenda (Andrade)
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_lunch_open.ogg | Lancheira abrindo (metal click + zipper) | 0.3s | Special merenda frame 0 |
| sfx_lunch_chomp.ogg | Mordida grande (crunch carnudo) | 0.2s | Special merenda frame 2 |
| sfx_lunch_burp.ogg | Arroto (comico, medio, nao nojento) | 0.5s | Special merenda frame 5 |
| sfx_lunch_throw.ogg | Lancheira arremessada (whoosh + metal) | 0.3s | Attack frame 1 |
| sfx_lunch_splat.ogg | Merenda esparramando (splat comico) | 0.3s | Projetil merenda impacto |

### Combate
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_andrade_hit.ogg | Andrade recebendo hit (ow fraco, patetismo) | 0.3s | Andrade hit frame 0 |
| sfx_taxadd_hit.ogg | Taxadd recebendo hit (ugh irritado, mais grave) | 0.3s | Taxadd hit frame 0 |
| sfx_andrade_death.ogg | Andrade morrendo (thud suave, pacífico) | 0.5s | Andrade death frame 2 |
| sfx_taxadd_death.ogg | Taxadd morrendo (vidro quebrando + moedas) | 0.8s | Taxadd death frame 0 |

### Specials
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_taxa_aura.ogg | Aura de taxa expandindo (hum grave crescente + moedas) | 2.0s | Taxa Infinita frames 0-2 |
| sfx_taxa_drain.ogg | Dreno de recursos (succao + moedas sugadas) | 1.5s | Taxa Infinita frames 2-3 |
| sfx_taxa_shockwave.ogg | Onda de choque fiscal (BOOM grave + tinido massivo) | 1.0s | Taxa Infinita frames 5-6 |
| sfx_taxa_universal.ogg | Taxacao Universal (acorde sinistro + sinos + moedas) | 3.0s | Taxacao Universal frames 0-2 |
| sfx_stamp_rapid.ogg | Carimbos rapidos (stamp-stamp-stamp-stamp) | 1.0s | Taxacao Universal frame 4 |
| sfx_evil_laugh.ogg | Risada sinistra do Taxadd | 2.0s | Taxacao Universal frame 5 |
| sfx_retroativo_rewind.ogg | Efeito de rebobinar (tape reverse) | 1.0s | Imposto Retroativo frame 1 |
| sfx_score_drain.ogg | Score sendo drenado (numeros digitais descendo) | 0.8s | Imposto Retroativo frame 2 |

### Transformacao
| Arquivo | Descricao | Duracao | Trigger |
|---------|-----------|---------|---------|
| sfx_transform_surge.ogg | Surge de poder (eletronico crescente) | 1.5s | Transformacao frames 1-3 |
| sfx_backpack_explode.ogg | Mochila explodindo (pop + itens voando) | 0.5s | Transformacao frame 4 |
| sfx_boss_entrance.ogg | Entrada de boss (acorde grave + impacto) | 1.0s | Transformacao frame 5 |

---

## MUSICA TEMATICA (Opcional)

### Tema do Andrade (NPC)
```
Arquivo: music_andrade_theme.ogg
Estilo: Musica de elevador TRISTE. Bossa nova deprimente. Violao desafinado.
BPM: 70 (lento, arrastado)
Instrumentos: Violao acustico desafinado, flauta doce (tocada mal), trianguçlo timido
Tom: Do menor (triste)
Loop: Sim
Duracao: 30 segundos (loop)
Volume: 0.3 (background, quase inaudivel - como o personagem)
Trigger: Andrade presente na tela
```

### Tema do Taxadd (Boss)
```
Arquivo: music_taxadd_theme.ogg
Estilo: Funk carioca FISCAL. Batida pesada com samples de caixa registradora.
BPM: 130 (rapido, agressivo)
Instrumentos: Batida funk (tamborzao), synth graves, samples de moedas e calculadora,
              caixa registradora como percussao, alarme fiscal como lead
Tom: Mi menor (ameacador)
Loop: Sim
Duracao: 45 segundos (loop)
Volume: 0.7 (PRESENTE - boss theme)
Trigger: Taxadd como boss ativo / Boss fight
Transicao: Fade in 2 segundos ao transformar de Andrade
```

---

## TABELA DE PRIORIDADE DE AUDIO

| Prioridade | Tipo | Exemplo | Pode Ser Cortado |
|-----------|------|---------|------------------|
| 1 (max) | Boss Music | music_taxadd_theme | Nao |
| 2 | Voice (bordao) | taxadd_vo_taxado | Sim (por outro de mesma/maior prioridade) |
| 3 | SFX combate | sfx_calc_fire | Nao |
| 4 | SFX ambiente | sfx_coin_drop | Sim |
| 5 (min) | SFX particula | sfx_coin_bounce | Sim |

**Max vozes simultaneas**: 8 canais
**Espacializacao**: Pan baseado na posicao X do sprite na tela (esquerda-direita)
**Atenuacao por distancia**: SFX atenuam a partir de 200px, silenciam a 500px

---

## NOTAS DE PRODUCAO

1. O "TAXADO!" e o som mais IMPORTANTE do personagem - investir em 5 variantes de qualidade
2. A voz do Andrade deve ser QUASE INAUDIVEL - a irrelevancia e sonora tambem
3. A transicao vocal Andrade→Taxadd (transform) e um momento narrativo chave
4. Todos os SFX de moedas devem soar SATISFATORIOS (psicologia de reward)
5. O tema musical do Taxadd deve ser GRUDENTO (earworm) para o jogador associar ao boss
6. Volume do Andrade (0.4-0.6) vs Volume do Taxadd (0.7-0.9) reflete o contraste de poder
7. Considerar text-to-speech para prototipagem rapida antes de gravar vozes finais
8. A risada sinistra (sfx_evil_laugh) NAO deve ser a risada "hue hue" brasileira - deve ser VILAO CLASSICO
9. O arroto da merenda (sfx_lunch_burp) deve ser comico mas NAO nojento
10. Priorizar gravacao de: "TAXADO!" > transform voice > outros bordoes > SFX
