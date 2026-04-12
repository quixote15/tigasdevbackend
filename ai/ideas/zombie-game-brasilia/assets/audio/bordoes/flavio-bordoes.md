# FLAVIO BOLSONARO (O Senador / O Moderado) -- Bordoes de Audio

**Voz**: Adulta, tentando parecer grave/seria mas sem convencer. Sotaque carioca controlado (tenta esconder). Tom geral: politico tentando parecer estadista mas falhando. Voz de quem ensaia frases no espelho e ainda assim soa artificial.
**TTS Voice**: `pt-BR-AntonioNeural` -- ajustar pitch -1Hz para voz tentando ser grave, rate -5% para tom ensaiado/politico
**Alternativa**: Voice actor masculino (35-45 anos) com voz que TENTA ser grave/seria mas escorrega para o natural (mais leve, menos grave)

---

### 1. "Eu sou MODERADO!"
- **Trigger**: hit (ao levar dano) / quando acusado / interacao com aliados / spawn
- **Emocao**: Defensividade pura, enfase FORCADA em "moderado", insistencia de quem ninguem acredita
- **Volume**: 8/10
- **Duracao**: 1.5s
- **Frequencia**: Cada 20s em idle / SEMPRE ao levar dano (reflexo defensivo) / spawn
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu sou MODERADO!" --rate "+5%" --pitch "-1Hz" --write-media flavio-01-moderado.mp3`
- **Efeitos de pos-producao**: Enfase FORCADA em "MODERADO" (volume +30% e pitch +2Hz so nessa palavra), tom defensivo, como se repetisse pela milesima vez
- **URL referencia**: Narrativa de Flavio como "o moderado" da familia Bolsonaro -- autodenominacao
- **Notas**: O bordao mais REPETIDO do Flavio. Diz com tanta insistencia que o efeito e o OPOSTO -- quanto mais insiste, menos acreditam. "MODERADO" soa como se estivesse escrito em caps lock. Ninguem reage. Silencio constrangedor depois.

### 2. "Meu pai e inocente! ...mas vamos falar de propostas."
- **Trigger**: idle / quando Bolsonaro e mencionado / interacao com NPCs / debate
- **Emocao**: Inicio RAPIDO querendo passar batido, pausa constrangedora, depois tom ENSAIADO de politico
- **Volume**: 6/10
- **Duracao**: 3.0s
- **Frequencia**: Cada 35s em idle / quando tema "pai" e tocado por aliados
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Meu pai e inocente! ...mas vamos falar de propostas." --rate "+5%" --pitch "-1Hz" --write-media flavio-02-inocente.mp3`
- **Efeitos de pos-producao**:
  - "Meu pai e inocente!" -- tom RAPIDO, quase atropelando as palavras (rate +15%), como quem quer tirar isso do caminho
  - PAUSA de 0.8s (silencio constrangedor)
  - "...mas vamos falar de propostas." -- tom COMPLETAMENTE DIFERENTE, ensaiado, voz de politico em entrevista, rate -10%, calmo e controlado
- **Notas**: A TRANSICAO e o humor. Vai de defesa desesperada do pai para politico ensaiado em 0.8s. A pausa e onde o constrangimento mora. O "mas" e a dobradura retorica mais desajeitada do jogo.

### 3. "Sera?"
- **Trigger**: idle / reacao a qualquer fala de aliado / pos-evento surpresa
- **Emocao**: Tom de trend TikTok, sorriso na voz, tentativa de parecer jovem e conectado
- **Volume**: 5/10
- **Duracao**: 0.5s
- **Frequencia**: Aleatorio -- cada 15s como reacao a QUALQUER coisa
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Sera?" --rate "+0%" --pitch "+1Hz" --write-media flavio-03-sera.mp3`
- **Efeitos de pos-producao**: Tom de trend TikTok, sorriso na voz (entonacao levemente ascendente, quase cantado), breve e descontraido
- **URL referencia**: Trend TikTok / meme generico -- Flavio tentando ser relevante nas redes
- **Notas**: O bordao mais CURTO do jogo (0.5s). Flavio diz "Sera?" como reacao a TUDO -- mata um zumbi ("Sera?"), encontra item ("Sera?"), leva dano ("Sera?"). Tentativa de parecer descolado e digital. Funciona como filler universal.

### 4. "O Brasil precisa de renovacao. ...com o sobrenome Bolsonaro."
- **Trigger**: idle / spawn / discurso pre-wave / interacao com NPCs
- **Emocao**: Tom politico ensaiado na primeira parte, contradicao comica na segunda
- **Volume**: 7/10
- **Duracao**: 3.0s
- **Frequencia**: Cada 40s em idle / spawn / pre-wave
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "O Brasil precisa de renovacao. ...com o sobrenome Bolsonaro." --rate "-5%" --pitch "-1Hz" --write-media flavio-04-renovacao.mp3`
- **Efeitos de pos-producao**:
  - "O Brasil precisa de renovacao." -- tom politico ensaiado, SERIO, voz de estadista (pitch -2Hz, rate -10%), como discurso de posse
  - PAUSA de 0.6s
  - "...com o sobrenome Bolsonaro." -- tom CASUAL, quase murmurado, como quem adiciona um detalhe insignificante (pitch volta ao normal, rate +5%)
- **URL referencia**: Narrativa de Flavio como candidato "proprio" mas com DNA familiar
- **Notas**: A CONTRADICAO COMICA perfeita. "Renovacao" seguido de "mesmo sobrenome". Flavio nao percebe a ironia -- e 100% sincero nas duas partes. A pausa entre elas e onde o humor vive.

### 5. "Eduardo, sai de cena, o candidato sou EU."
- **Trigger**: interact_eduardo (se Eduardo esta no mapa) / idle quando Eduardo fala / rivalidade
- **Emocao**: Rivalidade fraternal, enfase MAXIMA em "EU", tom de "chega de palhaçada, agora e minha vez"
- **Volume**: 8/10
- **Duracao**: 2.5s
- **Frequencia**: SEMPRE que Eduardo fala/aparece no mesmo mapa / cada 30s se ambos presentes
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eduardo, sai de cena, o candidato sou EU." --rate "+5%" --pitch "-1Hz" --write-media flavio-05-candidato.mp3`
- **Efeitos de pos-producao**: "Eduardo, sai de cena" -- tom de irmao mais velho mandando (firme mas nao gritando). "o candidato sou" -- pausa micro (0.2s). "EU" -- enfase MAXIMA (volume +40%, pitch +3Hz), como se a palavra estivesse em negrito sublinhado italico.
- **URL referencia**: Disputa interna Bolsonaro -- quem sera o candidato, Flavio ou Eduardo
- **Notas**: Rivalidade fraternal como mecanica. Se Eduardo E Flavio estao no mesmo mapa, este bordao toca COM FREQUENCIA. "EU" e quase gritado -- toda a fachada de "moderado" desmorona nessa unica palavra. A verdade do Flavio: ego de candidato.

---

## Variantes de Intensidade

| Bordao | Tom Normal | Tom Irritado (quando Eduardo presente) |
|--------|-----------|----------------------------------------|
| "Eu sou MODERADO!" | vol 7, defensivo | vol 9, GRITO defensivo, voz quebrando |
| "Meu pai e inocente!" | vol 6, rapido | vol 8, DESESPERADO, sem pausa |
| "Sera?" | vol 5, casual | vol 7, sarcastico, "SERA?" como acusacao |
| "Renovacao...Bolsonaro" | vol 6, ensaiado | vol 8, sem pausa (contradicao mais obvia) |
| "O candidato sou EU" | vol 7, firme | vol 10, GRITO de irmao, "EU" explode |

## Regras de Frequencia (Flavio-Especificas)

1. **"Eu sou MODERADO!"** e reflexo automatico -- toca em QUALQUER situacao de estresse
2. **"Sera?"** e filler universal -- 0.5s, pode tocar entre QUALQUER outro bordao
3. Se **Eduardo** esta no mesmo mapa: bordao 5 toca a cada 30s (rivalidade constante)
4. Se **Bolsonaro (pai)** e mencionado: bordao 2 e OBRIGATORIO (defesa reflexa)
5. Flavio oscila entre "ensaiado" e "real" -- os bordoes ensaiados (1, 2, 4) contrastam com os genuinos (3, 5)

## Efeitos Sonoros Contextuais
- **SFX de tosse politica**: "Ahem" sutil (0.3s) antes dos bordoes ensaiados (1, 2, 4) -- como quem se prepara para falar em publico
- **SFX de microfone**: Leve feedback de microfone quando "MODERADO" e gritado -- como se estivesse num palco
- **Silencio pos-"Sera?"**: 0.5s de silencio absoluto depois -- ninguem reage, ninguem responde

## Mecanica de Interacao: Flavio vs Eduardo
Quando AMBOS estao no mapa:
- Flavio diz "Eduardo, sai de cena!" -> Eduardo responde "Pai! Pai!" (chama reforço)
- Eduardo diz "Comunismo!" -> Flavio diz "Eu sou MODERADO!" (distanciamento)
- Eduardo leva dano -> Flavio diz "Sera?" (indiferença fraternal)
- Flavio leva dano -> Eduardo NAO reage (reciproco)

## Referencias de Audio Original
- Entrevistas do Flavio Bolsonaro -- tom "serio"/ensaiado
- Disputa familiar Bolsonaro -- quem sera candidato 2026
- "Sera?" como trend de TikTok/meme generico
- Auto-denominacao "moderado" -- recorrente
- Andre Guedes: Serie "Zumbis em Brasilia"
