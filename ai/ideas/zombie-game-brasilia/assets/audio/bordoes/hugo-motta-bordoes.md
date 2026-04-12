# HUGO MOTTA (O Presidente da Câmara dos Mortos) — Bordões de Áudio

**Voz**: Média, CALMA, controlada. Voz baixa que obriga os outros a prestarem atenção. Tom de quem nunca levanta a voz porque não precisa — o poder fala por ele. Sorriso permanente audível. Pausas calculadas entre frases.
**TTS Voice**: `pt-BR-AntonioNeural` — ajustar rate -15% para fala calculada + volume -10% (fala baixo de propósito)
**Alternativa**: Voice actor fazendo político articulador — voz de quem conversa em corredor do Congresso às 2h da manhã.

---

### 1. "Vamos conversar nos bastidores."
- **Trigger**: spawn / início de boss fight / skill Articulação Suprema
- **Emoção**: Controle absoluto, convite ameaçador disfarçado de cordialidade
- **Volume**: 5/10 (baixo de propósito — poder não precisa gritar)
- **Duração**: 2.0s
- **Frequência**: Ao aparecer + a cada Articulação
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Vamos conversar... nos bastidores." --rate "-15%" --pitch "-1Hz" --write-media hugo-01-bastidores.mp3`
- **Processamento**: Reverb de corredor do Congresso (eco leve, distante) + sussurro amplificado
- **URL referência**: Modus operandi real de articuladores políticos — tudo acontece nos bastidores
- **Notas**: Pausa de 0.5s entre "conversar..." e "nos bastidores." O "bastidores" é sussurrado como segredo. Quem ouve sabe que decisões já foram tomadas.

### 2. "Eu não decido nada. Eu só... articulo."
- **Trigger**: idle / ao ser questionado / resposta a ataque
- **Emoção**: Falsa humildade + poder real
- **Volume**: 5/10
- **Duração**: 3.0s
- **Frequência**: Cada 25s idle / ao ser atacado (40% chance)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu não decido nada. Eu só... articulo." --rate "-15%" --pitch "-1Hz" --write-media hugo-02-articulo.mp3`
- **Processamento**: Pausa de 0.8s antes de "articulo" — a palavra mais pesada da frase
- **Notas**: O "não decido nada" é mentira e todos sabem. O "articulo" é dito com um prazer sutil — é a verdade escondida na falsa humildade. O sorriso é audível.

### 3. "O Vorcaro? Conheço de vista. ...de muitas vistas, na verdade."
- **Trigger**: ao estar no mapa com Vorcaro / skill Conexão com o Master
- **Emoção**: Tentativa de distanciamento que vira confissão
- **Volume**: 5/10
- **Duração**: 3.5s
- **Frequência**: Quando Vorcaro está presente no mapa
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "O Vorcaro? Conheço de vista. ...de muitas vistas, na verdade." --rate "-10%" --pitch "-1Hz" --write-media hugo-03-vorcaro.mp3`
- **Processamento**: Primeira parte normal. Pausa 0.5s. Segunda parte mais baixa (quase pra si mesmo) — a confissão involuntária
- **URL referência**: Referência às mensagens encontradas no celular de Vorcaro
- **Notas**: Começa como negação ("conheço de vista" = mal conheço). A segunda parte ("de muitas vistas") destrói a negação. Hugo percebe o que disse e sorri nervoso.

### 4. "A Câmara funciona no diálogo. E no sigilo."
- **Trigger**: skill Pauta Secreta
- **Emoção**: Democracia subvertida com frase bonita
- **Volume**: 6/10
- **Duração**: 2.5s
- **Frequência**: A cada uso de Pauta Secreta
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A Câmara funciona no diálogo. E no sigilo." --rate "-10%" --pitch "-1Hz" --write-media hugo-04-sigilo.mp3`
- **Processamento**: "Diálogo" com tom aberto/público. "E no sigilo" com volume -30% (sussurro) — a transição é a piada
- **URL referência**: Contraste entre a retórica democrática e a prática autoritária
- **Notas**: A transição de volume entre "diálogo" (público) e "sigilo" (sussurro) é o DESIGN SONORO central do personagem. Tudo no Hugo Motta tem duas camadas: o que se diz e o que se faz.

### 5. "Quem controla a pauta, controla o país."
- **Trigger**: boss phase transition / power-up momento
- **Emoção**: Revelação de poder — a máscara cai por 1 segundo
- **Volume**: 7/10 (excepcionalmente alto para o Hugo — momento raro)
- **Duração**: 2.5s
- **Frequência**: Uma vez por encounter (momento de virada)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Quem controla a pauta... controla o país." --rate "-15%" --pitch "-2Hz" --write-media hugo-05-pauta.mp3`
- **Processamento**: Reverb de plenário vazio (eco grandioso) + pausa dramática + sub-bass no "país"
- **URL referência**: Verdade política absoluta — quem decide O QUE se vota controla tudo
- **Notas**: O ÚNICO momento em que Hugo fala com volume real. A máscara cai. O sorriso some por 1 segundo. O eco de plenário vazio sugere que ele está sozinho com seu poder. Depois volta ao sussurro normal.

### 6. "A sessão está aberta." (Boss fight trigger)
- **Trigger**: início da boss fight final / sessão de votação zumbi
- **Emoção**: Formalidade institucional — o horror está na normalidade
- **Volume**: 8/10
- **Duração**: 1.5s
- **Frequência**: Uma vez (início do boss fight)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A sessão... está aberta." --rate "-20%" --pitch "-2Hz" --write-media hugo-06-sessao.mp3`
- **Processamento**: Reverb de plenário + som de martelo batendo mesa (THUD grave) + eco no "aberta"
- **Notas**: Formalidade processual. É EXATAMENTE como uma sessão real da Câmara começa. O horror está na normalidade — é uma sessão legislativa, só que com zumbis votando. O martelo bate mesa em sync.

---

## Efeitos Sonoros Específicos do Hugo Motta

| SFX | Descrição | Trigger | Arquivo |
|-----|-----------|---------|---------|
| hugo-sfx-handshake | Aperto de mão excessivo (muitos dedos) | Articulação Suprema | `hugo-sfx-handshake.wav` |
| hugo-sfx-phone-glow | Celular brilhando + vibração de notificação | Loop ambient (tela VORCARO) | `hugo-sfx-phone.wav` |
| hugo-sfx-gavel | Martelo de presidente batendo na mesa | Início de sessão / ataque especial | `hugo-sfx-gavel.wav` |
| hugo-sfx-whisper | Sussurro indecifrável de corredor | Pauta Secreta ativando | `hugo-sfx-whisper.wav` |
| hugo-sfx-vote-sim | "SIM!" gritado por massa de zumbis | Votação zumbi — projéteis SIM | `hugo-sfx-sim.wav` |
| hugo-sfx-vote-nao | "NÃO!" gritado por massa de zumbis | Votação zumbi — projéteis NÃO | `hugo-sfx-nao.wav` |
| hugo-sfx-smile-creak | Som de sorriso plástico (creak) | Idle — sorriso permanente | `hugo-sfx-smile.wav` |
