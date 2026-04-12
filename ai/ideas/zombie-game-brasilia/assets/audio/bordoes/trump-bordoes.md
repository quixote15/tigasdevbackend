# TRUMP (Trampi / O Imperador Americano) — Bordões de Áudio

**Voz**: Grave-média, nasalada, arrogante. Inglês macarrônico misturado com português torto. Tom de discurso de comício americano com sotaque BR absurdo. Ênfase EXAGERADA em adjetivos ("TREMENDOUS", "BEAUTIFUL", "PERFECT").
**TTS Voice**: `en-US-GuyNeural` (para partes em inglês) + `pt-BR-AntonioNeural` (para partes em português) — mixar com crossfade
**Alternativa**: Voice actor fazendo sotaque americano tentando falar português. O inglês é fluente, o português é HORRÍVEL.

---

### 1. "TREMENDOUS!"
- **Trigger**: attack_success / ao acertar inimigo com Taco de Golfe
- **Emoção**: Satisfação narcisista extrema, auto-congratulação
- **Volume**: 9/10
- **Duração**: 1.2s
- **Frequência**: A cada hit bem-sucedido / 30% de chance
- **TTS Command**: `edge-tts --voice "en-US-GuyNeural" --text "TREMENDOUS!" --rate "+10%" --pitch "+2Hz" --write-media trump-01-attack.mp3`
- **URL referência**: Palavra mais usada pelo Trump real em discursos
- **Notas**: Deve soar como se fosse a maior conquista da história da humanidade. Eco leve. O "TREMENDOUS" é quase um grunhido de prazer narcisista.

### 2. "FAKE NEWS!"
- **Trigger**: miss / ao errar ataque / ao levar dano / skill Fake News Presidential
- **Emoção**: Raiva indignada + negação total da realidade
- **Volume**: 10/10
- **Duração**: 1.0s
- **Frequência**: A cada miss / hit recebido / ativação de skill
- **TTS Command**: `edge-tts --voice "en-US-GuyNeural" --text "FAKE NEWS!" --rate "+20%" --pitch "+3Hz" --write-media trump-02-miss.mp3`
- **URL referência**: Bordão mais icônico do Trump — usado para negar qualquer coisa
- **Notas**: Gritado com RAIVA. A reação padrão para qualquer coisa negativa. Se erra — "FAKE NEWS!". Se leva dano — "FAKE NEWS!". Se morre — "FAKE NEWS!".

### 3. "Trãmpi!"
- **Trigger**: spawn / início de aparição
- **Emoção**: Auto-apresentação grandiosa com sotaque BR
- **Volume**: 8/10
- **Duração**: 1.5s
- **Frequência**: Ao aparecer no mapa
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Trãmpi!" --rate "+5%" --pitch "+1Hz" --write-media trump-03-spawn.mp3`
- **URL referência**: Pronúncia brasileira satirizada do nome Trump nos vídeos do André Guedes
- **Notas**: Deve soar como brasileiro tentando falar "Trump" e saindo "Trãmpi". Sotaque nasal. É a identidade sonora do personagem no universo André Guedes.

### 4. "This is MY country now. Obrigado."
- **Trigger**: ultimate (AMERICA FIRST) / boss phase 3
- **Emoção**: Dominação imperial + falsa cortesia
- **Volume**: 9/10
- **Duração**: 3.0s
- **Frequência**: Uma vez por ultimate
- **TTS Command**: `edge-tts --voice "en-US-GuyNeural" --text "This is MY country now." --rate "-5%" --write-media trump-04a-ultimate.mp3 && edge-tts --voice "pt-BR-AntonioNeural" --text "Obrigado." --rate "-10%" --write-media trump-04b-ultimate.mp3`
- **URL referência**: Bordão criado para o jogo — captura a essência do intervencionismo
- **Notas**: "This is MY country now" em inglês perfeito, arrogante. Pausa de 0.5s. "Obrigado" em português torto, como se fosse a única palavra que aprendeu — mas dita com condescendência total.

### 5. "Very good, companheiro! Make Brazil great again, talkei?"
- **Trigger**: idle (quando parado por 5s+)
- **Emoção**: Condescendência imperial + tentativa patética de se adaptar ao Brasil
- **Volume**: 7/10
- **Duração**: 3.5s
- **Frequência**: Cada 20s em idle
- **TTS Command**: `edge-tts --voice "en-US-GuyNeural" --text "Very good, companheiro! Make Brazil great again, talkei?" --rate "-5%" --write-media trump-05-idle.mp3`
- **URL referência**: Mix de bordão Trump + "companheiro" (Lula) + "talkei" (Bolsonaro) = hibridismo satirico perfeito
- **Notas**: O "companheiro" sai completamente errado em sotaque americano. O "talkei" é imitação horrível do Bolsonaro. Mostra que Trump absorve bordões de quem quiser usar como fantoche.

### 6. "É o México vai pagar! ...ou o Brasil, tanto faz."
- **Trigger**: skill Build the Wall
- **Emoção**: Indiferença imperial — qualquer país latino serve
- **Volume**: 8/10
- **Duração**: 3.0s
- **Frequência**: A cada ativação de Build the Wall
- **TTS Command**: `edge-tts --voice "en-US-GuyNeural" --text "É o México vai pagar!" --rate "+5%" --write-media trump-06a-wall.mp3 && edge-tts --voice "en-US-GuyNeural" --text "...ou o Brasil, tanto faz." --rate "-10%" --write-media trump-06b-wall.mp3`
- **URL referência**: Adaptação do "Mexico will pay for the wall" para o contexto BR
- **Notas**: Primeira parte gritada com convicção. Pausa de 0.8s. Segunda parte murmurada, quase como reflexão — porque para Trump, todos os países latinos são intercambiáveis.

### 7. "Make taxes great again, companheiro!"
- **Trigger**: skill Tarifa de 100%
- **Emoção**: Entusiasmo absurdo por tarifas
- **Volume**: 8/10
- **Duração**: 2.5s
- **Frequência**: A cada ativação de Tarifa
- **TTS Command**: `edge-tts --voice "en-US-GuyNeural" --text "Make taxes great again, companheiro!" --rate "+5%" --pitch "+1Hz" --write-media trump-07-tariff.mp3`
- **URL referência**: Paródia do "Make America Great Again"
- **Notas**: Dito com o mesmo entusiasmo de comício. "Companheiro" sai totalmente errado.

### 8. "Não acredite em nada que você vê. Acredite em MIM."
- **Trigger**: skill Fake News Presidential (secundário)
- **Emoção**: Autoritarismo puro disfarçado de conselho
- **Volume**: 7/10
- **Duração**: 3.0s
- **Frequência**: A cada ativação de Fake News
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Não acredite em nada que você vê. Acredite em MIM." --rate "-5%" --pitch "-1Hz" --write-media trump-08-fakenews.mp3`
- **URL referência**: Filosofia Trump de controle narrativo
- **Notas**: Todo em português péssimo. O "MIM" é gritado com ênfase narcisista. É a frase mais assustadora do personagem — por ser a mais real.

### 9. "AMERICA FIRST!"
- **Trigger**: ultimate activation (grito de guerra)
- **Emoção**: Nacionalismo extremo, euforia militar
- **Volume**: 10/10
- **Duração**: 1.5s
- **Frequência**: Uma vez por ultimate
- **TTS Command**: `edge-tts --voice "en-US-GuyNeural" --text "AMERICA FIRST!" --rate "+15%" --pitch "+3Hz" --write-media trump-09-ultimate-shout.mp3`
- **URL referência**: Slogan principal do Trump
- **Notas**: Gritado com força máxima. Eco épico. Distorção leve de áudio (reverb + overdrive). Hino americano começa distorcido em background. É o trigger sonoro do ultimate.

### 10. "You're fired!"
- **Trigger**: death de inimigo boss / eliminação de personagem importante
- **Emoção**: Satisfação sádica
- **Volume**: 8/10
- **Duração**: 1.2s
- **Frequência**: Ao matar boss/mini-boss
- **TTS Command**: `edge-tts --voice "en-US-GuyNeural" --text "You're fired!" --rate "+10%" --write-media trump-10-kill.mp3`
- **URL referência**: Bordão do The Apprentice
- **Notas**: Clássico. Dedo apontando (micro-mão apontando). Som de disparo de pistola junto.

---

## Efeitos Sonoros Específicos do Trump

| SFX | Descrição | Trigger | Arquivo |
|-----|-----------|---------|---------|
| trump-sfx-hands-fumble | Som de objeto escorregando de mãos pequenas | Tentativa de pegar item (50% chance) | `trump-sfx-fumble.wav` |
| trump-sfx-golf-swing | Som de taco de golfe cortando o ar | Ataque com Taco Nuclear | `trump-sfx-swing.wav` |
| trump-sfx-golf-explode | Explosão da bola de golfe | Impacto do projétil | `trump-sfx-explode.wav` |
| trump-sfx-wall-build | Tijolos de ouro se empilhando rapidamente | Build the Wall skill | `trump-sfx-wall.wav` |
| trump-sfx-eagle-screech | Águia americana gritando (distorcido) | Ultimate AMERICA FIRST | `trump-sfx-eagle.wav` |
| trump-sfx-anthem-distorted | Hino americano distorcido e sinistro | Background do Ultimate | `trump-sfx-anthem.wav` |
| trump-sfx-tariff-cha-ching | Som de caixa registradora + moedas | Tarifa de 100% | `trump-sfx-tariff.wav` |
| trump-sfx-orange-glow | Humming elétrico fluorescente | Ambient (loop permanente do glow) | `trump-sfx-glow-loop.wav` |
