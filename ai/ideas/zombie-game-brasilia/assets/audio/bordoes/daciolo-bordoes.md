# CABO DACIOLO (O Profeta / O Exorcista) -- Bordoes de Audio

**Voz**: Media, potente, projecao de pastor pentecostal. Grita como se cada palavra fosse uma oracao. Sotaque carioca forte com cadencia evangelica. Variacoes extremas: do sussurro devoto ao GRITO COSMICO. Emotividade MAXIMA em cada fala -- volume ALTO natural.
**TTS Voice**: `pt-BR-AntonioNeural` -- ajustar pitch +2Hz, rate +5% para cadencia pastoral
**Alternativa**: ESSENCIAL gravar com voice actor -- TTS nao captura a intensidade evangelica
**PRIORIDADE**: Daciolo e o personagem mais importante em termos de bordoes. Mais variantes, mais intensidades, mais frequencia.

---

### 1. "GLORIA A DEUS!" (Sussurro Reverente)
- **Trigger**: pre_heal / idle em area segura (oracao pessoal)
- **Emocao**: Devocao tranquila, sussurro de quem conversa com Deus, gratidao intima
- **Volume**: 3/10
- **Duracao**: 0.8s
- **Frequencia**: Antes de usar skill de cura / cada 25s em idle seguro
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Gloria a Deus..." --rate "-10%" --pitch "+0Hz" --volume "-30%" --write-media daciolo-01a-gloria-sussurro.mp3`
- **Efeitos de pos-producao**: Eco suave (reverb curto, 0.3s decay), tom baixo, sem distorcao
- **Notas**: Sussurro devoto. Olhos fechados. Maos juntas. Momento intimo de fe antes da cura. Contraste total com o grito cosmico.

### 2. "GLORIA A DEUS!" (Normal)
- **Trigger**: idle aleatorio / walk / spawn
- **Emocao**: Entusiasmo religioso padrao, saudacao compulsiva
- **Volume**: 7/10
- **Duracao**: 1.2s
- **Frequencia**: Cada 12s -- compulsivo, involuntario, o Daciolo nao consegue evitar
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "GLORIA A DEUS!" --rate "+5%" --pitch "+3Hz" --write-media daciolo-01b-gloria-normal.mp3`
- **Efeitos de pos-producao**: Sem eco. Som limpo, direto. Tom medio.
- **URL referencia**: Videos reais do Daciolo -- bordao gritado compulsivamente em toda frase
- **Notas**: Tom de pastor em pulpito. A cada 3 frases, esse bordao aparece automaticamente. E como respirar para o Daciolo.

### 3. "GLOOORIA A DEEEEEUS!" (GRITO MAXIMO / Skill)
- **Trigger**: special / ultimate / kill_boss (skill "Gloria a Deus")
- **Emocao**: Extase religioso total, conexao divina, grito supersonico
- **Volume**: 10/10
- **Duracao**: 2.0s
- **Frequencia**: Ao ativar skill "GLORIA A DEUS!" ou ultimate
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "GLOOOOORIA A DEEEEEUS!" --rate "+15%" --pitch "+8Hz" --write-media daciolo-01c-gloria-cosmico.mp3`
- **Efeitos de pos-producao**: Eco cathedral (reverb pesado, 2.5s decay), tom altissimo, distorcao leve no pico, reverb de catedral gotica
- **URL referencia**: Daciolo gritando em plenario -- videos virais
- **Notas**: GRITO que ESTUNA todos os inimigos. O GRITO MAIS ALTO do jogo inteiro. Reverb pesado como se estivesse dentro de uma catedral. Raios de luz no audio.

### 4. "GLORIA A DEUS!" (Extatico / Pos-Kill)
- **Trigger**: kill_enemy / kill_combo
- **Emocao**: Euforia pos-vitoria, voz quebrando de emocao, alegria incontrolavel
- **Volume**: 9/10
- **Duracao**: 1.5s
- **Frequencia**: Apos matar inimigo (40% de chance)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "GLORIA A DEUS!" --rate "+10%" --pitch "+6Hz" --write-media daciolo-01d-gloria-extatico.mp3`
- **Efeitos de pos-producao**: Tom agudo, voz quebrando/falhando de emocao (pitch wobble +/-3Hz), leve crack vocal
- **Notas**: Diferente do grito maximo -- aqui a voz QUEBRA de emocao. Quase chorando de gratidao. A vitoria e de Deus.

### 5. "Queima Jesus! Shabalaba!"
- **Trigger**: attack / special (skill "Exorcismo Eleitoral")
- **Emocao**: Exorcismo urgente, glossolalia, transe religioso
- **Volume**: 9/10
- **Duracao**: 1.5s
- **Frequencia**: Ao usar skill de exorcismo / ataque especial
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Queima Jesus! Shabalaba!" --rate "+10%" --pitch "+5Hz" --write-media daciolo-02-queima.mp3`
- **Efeitos de pos-producao**: Eco de fogo (reverb medio), voz grave->aguda (pitch rise de -2Hz para +5Hz ao longo da fala)
- **URL referencia**: Bordao real do Daciolo em cultos/comicios
- **Notas**: "Shabalaba" e glossolalia -- linguas estranhas. Deve soar como transe espiritual genuino. A voz começa grave e sobe para aguda durante "Shabalaba".

### 6. "A URSAL EXISTE!"
- **Trigger**: ultimate (skill "URSAL Cataclismica") / revelacao conspiratoria
- **Emocao**: GRITO de revelacao conspiratoria, tom urgente, "EU AVISEI", vindication absoluta
- **Volume**: 10/10
- **Duracao**: 2.0s
- **Frequencia**: Ao ativar ultimate
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A URSAAAAL EXISTE!" --rate "+15%" --pitch "+5Hz" --write-media daciolo-03-ursal.mp3`
- **Efeitos de pos-producao**: Reverb epico (2.0s decay), trovao ao fundo, eco dramatico
- **URL referencia**: Debate presidencial 2018 -- momento iconico
- **Notas**: URSAL = Uniao das Republicas Socialistas da America Latina. Tom URGENTE como quem revela segredo de estado. O mapa da URSAL cai do ceu como bomba.

### 7. "Sinto o cheiro de Satanas neste recinto!"
- **Trigger**: enemy_spawn / boss_appear / entrada em area nova perigosa
- **Emocao**: Alerta divino, deteccao demoniaca, nojo + alarme
- **Volume**: 8/10
- **Duracao**: 2.5s
- **Frequencia**: Quando inimigos especiais aparecem
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Sinto o cheiro de Satanas neste recinto!" --rate "+5%" --pitch "+3Hz" --write-media daciolo-04-satanas.mp3`
- **Efeitos de pos-producao**: SFX de sniffing (0.3s) ANTES da fala, tom de nojo + alarme
- **URL referencia**: Frase real do Daciolo no plenario
- **Notas**: Dito com CONVICCAO absoluta. Nariz levantado, farejando. Som de "sniff sniff" antes da fala. Tom de quem realmente sente o enxofre.

### 8. "Gloria a sap-- opa, Gloria a Deus!"
- **Trigger**: idle / attack (10% de chance de SUBSTITUIR qualquer "Gloria a Deus")
- **Emocao**: Confusao momentanea, erro de fala, constrangimento, risada nervosa
- **Volume**: 6/10
- **Duracao**: 2.0s
- **Frequencia**: 10% de chance de tocar NO LUGAR de qualquer "Gloria a Deus" normal
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Gloria a sap... opa, Gloria a Deus!" --rate "+5%" --pitch "+3Hz" --write-media daciolo-05-falha.mp3`
- **Efeitos de pos-producao**: Gaguejar no "sap-", pausa de constrangimento (0.4s), risada nervosa sutil no final (0.3s)
- **URL referencia**: Erro real do Daciolo em discurso -- ia dizer "Sapo" ou "Satanas" e se corrigiu
- **Notas**: FALHA COMICA. Quando acontece, o efeito do grito sai 50% mais fraco. O Daciolo pisca surpreso. Mecanica de gameplay: 10% de falha critica comica.

### 9. "Pela honra e gloria de Nosso Senhor!"
- **Trigger**: attack_charge / pre-boss / entrada em area de boss
- **Emocao**: Juramento sagrado, preparacao para batalha santa, solenidade
- **Volume**: 8/10
- **Duracao**: 2.0s
- **Frequencia**: Antes de enfrentar boss
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Pela honra e gloria de Nosso Senhor!" --rate "+0%" --pitch "+2Hz" --write-media daciolo-06-juramento.mp3`
- **Efeitos de pos-producao**: Tom solene, sem eco excessivo, reverb curto (0.5s)
- **Notas**: Tom solene. Diferente dos gritos -- aqui e JURAMENTO. Momento serio num personagem comico. Gravidade genuina.

### 10. "Carissimo! Dignissimo!"
- **Trigger**: idle / interact_npc / encontro com qualquer personagem
- **Emocao**: Formalidade excessiva, tratamento respeitoso a TODOS (ate zumbis)
- **Volume**: 6/10
- **Duracao**: 1.0s
- **Frequencia**: Ao interagir com qualquer personagem
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Carissimo! Dignissimo!" --rate "+5%" --pitch "+3Hz" --write-media daciolo-07-carissimo.mp3`
- **Efeitos de pos-producao**: Tom formal-religioso, cadencia de politico de plenario
- **Notas**: Trata ATE os zumbis com formalidade. Sincero ao extremo. Tom de deputado em sessao solene.

### 11. "O Estado e laico? E o Satanas!"
- **Trigger**: idle / reacao a evento politico / debate entre personagens
- **Emocao**: Indignacao pura, logica Daciolo (non sequitur religioso)
- **Volume**: 8/10
- **Duracao**: 2.0s
- **Frequencia**: Raro -- cada 40s em idle / ao encontrar itens "laicos"
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "O Estado e laico? E o Satanas!" --rate "+5%" --pitch "+4Hz" --write-media daciolo-08-laico.mp3`
- **Efeitos de pos-producao**: Tom de indignacao crescente, "E o Satanas!" como acusacao final
- **Notas**: Non sequitur perfeito. A logica e: laicidade = obra do demonio. Tom de quem acabou de resolver uma equacao matematica e descobriu a verdade universal.

### 12. "Venham comigo, nao vao ficar ai!"
- **Trigger**: ally_buff / group_move / quando aliados estao longe
- **Emocao**: Lideranca genuina, protecao paterna, urgencia
- **Volume**: 8/10
- **Duracao**: 1.5s
- **Frequencia**: Quando aliados estao proximos mas parados
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Venham comigo, nao vao ficar ai!" --rate "+10%" --pitch "+3Hz" --write-media daciolo-09-lideranca.mp3`
- **Efeitos de pos-producao**: Tom de lider militar com fe, urgencia na voz
- **URL referencia**: Ep. 1 de Zumbis em Brasilia -- Daciolo salva todo mundo
- **Notas**: Momento de lideranca real. Diferente do tom comico -- aqui ele e GENUINO. O Daciolo que realmente protege as pessoas.

### 13. "Acho que isso faz de mim o novo lider de Brasilia"
- **Trigger**: kill_boss / clear_area / pos-vitoria significativa
- **Emocao**: Satisfacao inocente, auto-proclamacao ingenua, sorriso na voz
- **Volume**: 7/10
- **Duracao**: 2.5s
- **Frequencia**: Apos derrotar boss ou limpar area
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Acho que isso faz de mim o novo lider de Brasilia" --rate "+0%" --pitch "+2Hz" --write-media daciolo-10-lider-brasilia.mp3`
- **Efeitos de pos-producao**: Tom satisfeito/inocente, sem eco, som limpo e honesto
- **Notas**: Dito com INOCENCIA total. Nao e arrogancia -- e genuina confusao sobre como a lideranca funciona. O Daciolo sinceramente acha que matar zumbis = eleicao automatica.

### 14. "Nao estou a venda para o sistema!"
- **Trigger**: spawn / inicio de wave (skin 2026) / recusar item corrompido
- **Emocao**: Indignacao justa, incorruptibilidade, desafio ao establishment
- **Volume**: 8/10
- **Duracao**: 2.0s
- **Frequencia**: Spawn (versao 2026) / ao recusar itens do tipo "propina"
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Nao estou a venda para o sistema!" --rate "+5%" --pitch "+3Hz" --write-media daciolo-11-sistema.mp3`
- **Efeitos de pos-producao**: Tom desafiador, voz firme, sem tremor
- **URL referencia**: Discurso real abril 2026 -- pre-candidatura pelo Mobiliza!
- **Notas**: Referencia direta a pre-candidatura real de 2026. Tom desafiador contra o sistema. Metalinguagem insana.

### 15. "Estou aqui anunciando o reino!"
- **Trigger**: spawn / inicio de episodio / skin 2026
- **Emocao**: Profecia, missao divina, tom profetico
- **Volume**: 8/10
- **Duracao**: 1.5s
- **Frequencia**: Ao iniciar novo episodio/fase (versao 2026)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Estou aqui anunciando o reino!" --rate "+5%" --pitch "+4Hz" --write-media daciolo-12-reino.mp3`
- **Efeitos de pos-producao**: Tom profetico, eco leve (reverb 0.8s), sensacao de "anuncio divino"
- **Notas**: Tom de profeta do Velho Testamento. O "reino" e tanto o reino de Deus quanto o reino dele em Brasilia pos-apocaliptica.

### 16. "Brasil acima de tudo, Deus acima de todos!"
- **Trigger**: pre-boss / momento epico / rally de aliados
- **Emocao**: Fe genuina, patriotismo sincero, grito de guerra
- **Volume**: 9/10
- **Duracao**: 2.5s
- **Frequencia**: Antes de boss fight epico / rally de grupo
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Brasil acima de tudo, Deus acima de todos!" --rate "+5%" --pitch "+4Hz" --write-media daciolo-13-brasil-deus.mp3`
- **Efeitos de pos-producao**: Tom de fe genuina, reverb medio (1.0s), eco patriotico
- **Notas**: Dito com FE GENUINA -- diferente de quando outros usam essa frase por oportunismo. No Daciolo e 100% sincero. Grito de guerra antes da batalha final.

### 17. "SAAAI, SATANAS! SAI DO CORPO DESSE CONGRESSO!"
- **Trigger**: special (skill "Exorcismo em Massa")
- **Emocao**: Exorcismo epico, transe maximo, cura em massa
- **Volume**: 10/10
- **Duracao**: 4.0s
- **Frequencia**: Ao ativar exorcismo em massa
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "SAAAI, SATANAS! SAI DO CORPO DESSE CONGRESSO!" --rate "+10%" --pitch "+5Hz" --write-media daciolo-14-exorcismo.mp3`
- **Efeitos de pos-producao**: Grito de exorcismo MAXIMO, reverb cathedral (3.0s), coro de anjos ao fundo (SFX layer), raios de luz no audio (distorcao + reverb longo)
- **Notas**: Remove TODOS os debuffs. Cura 25% de TODOS os aliados. O audio mais epico do Daciolo.

### 18. "MEU NUMERO E O QUE DEUS MANDAR!"
- **Trigger**: special (skill "Candidatura Divina 2026")
- **Emocao**: Fe cega, entrega total, absurdo sagrado
- **Volume**: 9/10
- **Duracao**: 2.0s
- **Frequencia**: Ao usar skill de confusao
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "MEU NUMERO E O QUE DEUS MANDAR!" --rate "+10%" --pitch "+5Hz" --write-media daciolo-15-numero.mp3`
- **Efeitos de pos-producao**: Tom de conviccao absoluta, eco medio
- **Notas**: Variante do "56" do Eneas mas com twist divino. Inimigo fica confuso tentando votar. Skill de confusao em area.

---

## Variantes de Intensidade (Especial para Daciolo)

| "GLORIA A DEUS!" | Volume | Pitch | Duracao | Efeito de Audio | Contexto de Gameplay |
|---|---|---|---|---|---|
| Sussurro Reverente | 3/10 | +0Hz | 0.8s | Eco suave (reverb 0.3s) | Pre-cura / idle seguro |
| Normal | 7/10 | +3Hz | 1.2s | Sem eco | Idle/walk padrao |
| Extatico (pos-kill) | 9/10 | +6Hz | 1.5s | Voz quebrando (pitch wobble) | Apos matar inimigo |
| GRITO MAXIMO | 10/10 | +8Hz | 2.0s | Eco cathedral + reverb pesado | Skill / ultimate / boss |
| Falha Comica (10%) | 6/10 | +3Hz | 2.0s | Gaguejar + risada nervosa | Substitui qualquer Gloria (10%) |

## Regras de Frequencia (Daciolo-Especificas)

1. **"Gloria a Deus"** em qualquer variante deve tocar a cada ~12s em idle -- e COMPULSIVO
2. **Falha comica** (bordao 8) tem 10% de chance de substituir QUALQUER "Gloria a Deus"
3. **Bordoes 2026** (14, 15) so ativam com skin de 2026 equipada
4. **Exorcismo em Massa** (17) e o audio mais longo -- 4.0s com layers de SFX
5. Daciolo tem MAIS bordoes que qualquer outro personagem -- e o mais vocal do elenco

## Referencias de Audio Original
- Debate presidencial 2018: "A URSAL EXISTE!" -- videos completos
- Plenario: Daciolo gritando "GLORIA A DEUS" no Congresso
- Cultos/comicios: "Queima Jesus" + glossolalia
- Andre Guedes: Serie "Daciolo vs URSAL" (5+ episodios)
- Pre-candidatura 2026: Discurso do Mobiliza! (abril 2026)
- Compilacao "Melhores momentos Daciolo" -- YouTube
