# MONARK (O Rei do Limbo) — Bordões de Áudio

**Voz**: Média-grave, LENTA, arrastada, com pausas longas onde o pensamento parece se perder. Tom de quem está pensando alto mas não chegou a nenhuma conclusão. Levemente rouca. Dição relaxada — consoantes suaves, vogais longas. Som de "mano" permanente.
**TTS Voice**: `pt-BR-AntonioNeural` — ajustar rate -25% para fala arrastada de chapado + leve reverb de espaço vazio
**Alternativa**: Voice actor fazendo voz de podcaster chapado — referência: o próprio Monark real, mas 50% mais lento.

---

### 1. "Mano, pensa comigo..."
- **Trigger**: idle principal / início de diálogo NPC
- **Emoção**: Pseudo-filosofia, convite a reflexão que nunca chega a lugar nenhum
- **Volume**: 5/10
- **Duração**: 2.5s
- **Frequência**: Início de toda interação no Limbo
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Mano... pensa comigo..." --rate "-25%" --pitch "-2Hz" --write-media monark-01-idle.mp3`
- **Processamento**: Reverb de espaço vazio infinito (decay 5s) + filtro low-pass leve (tira brilho — som abafado do Limbo)
- **URL referência**: Frase introdutória clássica do Monark em podcasts
- **Notas**: O "Mano" tem pausa de 0.5s antes do "pensa comigo". O "comigo" some no eco do vazio. O jogador deve sentir que está no nada absoluto.

### 2. "Bem-vindo ao Limbo."
- **Trigger**: game_over / jogador morre e chega ao Limbo
- **Emoção**: Boas-vindas casual ao vazio existencial
- **Volume**: 6/10
- **Duração**: 2.0s
- **Frequência**: A cada morte do jogador
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Bem-vindo ao Limbo." --rate "-20%" --pitch "-2Hz" --write-media monark-02-welcome.mp3`
- **Processamento**: Reverb catedral + leve chorus + som ambiente de vento vazio em background
- **URL referência**: Frase de recepção da série Limbo dos Cancelados do André Guedes
- **Notas**: Dito com a normalidade mais assustadora possível. Como se morrer e chegar ao Limbo fosse rotina. Zero drama, zero emoção. É a casualidade que dá o impacto.

### 3. "E aí mano, bem-vindo ao Limbo. Quer um baseado... digo, uma segunda chance?"
- **Trigger**: diálogo de revive (quando jogador pode escolher voltar)
- **Emoção**: Hospitalidade absurda + correção cômica
- **Volume**: 6/10
- **Duração**: 4.5s
- **Frequência**: A cada oportunidade de revive
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "E aí mano, bem-vindo ao Limbo. Quer um baseado... digo, uma segunda chance?" --rate "-20%" --pitch "-2Hz" --write-media monark-03-revive.mp3`
- **Processamento**: Reverb Limbo + pausa de 0.3s no "baseado... digo"
- **URL referência**: Adaptação do bordão do Limbo dos Cancelados
- **Notas**: O "baseado" sai naturalmente e a correção para "segunda chance" é feita sem vergonha nenhuma. O Monark não esconde — ele corrige por formalidade, não por arrependimento.

### 4. "Aqui no Limbo todo mundo é igual. Todo mundo ferrou."
- **Trigger**: idle no Limbo / diálogo de loja
- **Emoção**: Democracia do fracasso, igualitarismo niilista
- **Volume**: 5/10
- **Duração**: 3.5s
- **Frequência**: Aleatória a cada 30s no Limbo
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Aqui no Limbo todo mundo é igual. Todo mundo ferrou." --rate "-20%" --pitch "-2Hz" --write-media monark-04-igualdade.mp3`
- **Processamento**: Reverb vazio + leve eco na palavra "ferrou"
- **Notas**: A frase mais filosófica do Monark. Dita com uma sabedoria que ele próprio não percebe que tem. O "ferrou" deve ter um tom quase de conforto — como "relaxa, tá todo mundo na mesma".

### 5. "Você foi cancelado por quê? Ah, morreu? Tanto faz, mano."
- **Trigger**: chegada ao Limbo (variante do welcome)
- **Emoção**: Indiferença total entre morte e cancelamento
- **Volume**: 5/10
- **Duração**: 4.0s
- **Frequência**: Variação aleatória do welcome (50% de chance vs bordão 2)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Você foi cancelado por quê? Ah, morreu? Tanto faz, mano." --rate "-20%" --pitch "-2Hz" --write-media monark-05-cancelado.mp3`
- **Processamento**: Reverb Limbo padrão
- **Notas**: Para o Monark, morrer e ser cancelado são a mesma coisa. Essa é a piada. O "Tanto faz" é dito com a sinceridade mais profunda possível.

### 6. "A liberdade de expressão deveria valer até no inferno."
- **Trigger**: idle raro / após jogador recusar oferta
- **Emoção**: Pseudo-profundidade, reflexão que parece inteligente mas não é
- **Volume**: 4/10
- **Duração**: 3.5s
- **Frequência**: Raro — 10% de chance em idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A liberdade de expressão deveria valer até no inferno." --rate "-25%" --pitch "-3Hz" --write-media monark-06-liberdade.mp3`
- **Processamento**: Reverb máximo + eco dramático no "inferno"
- **Notas**: Esta é a frase que o Monark acha que é profunda. Dita com gravidade. O eco exagerado no "inferno" adiciona uma camada de falsa importância. O jogador ri porque é EXATAMENTE o tipo de coisa que o Monark real diria.

### 7. "Podcast do Limbo — episódio..." *conta nos dedos* "...sei lá, tipo, muitos."
- **Trigger**: início do mini-desafio (Podcast do Limbo skill)
- **Emoção**: Desorganização profissional charming
- **Volume**: 6/10
- **Duração**: 4.0s
- **Frequência**: A cada mini-desafio
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Podcast do Limbo, episódio... sei lá, tipo, muitos." --rate "-15%" --pitch "-2Hz" --write-media monark-07-podcast.mp3`
- **Processamento**: Reverb Limbo + pausa de 1s entre "episódio..." e "sei lá"
- **Notas**: O Monark perdeu a conta dos episódios. A pausa longa sugere que ele tentou contar e desistiu. "Tipo, muitos" é o máximo de precisão que ele oferece.

---

## Efeitos Sonoros Específicos do Monark

| SFX | Descrição | Trigger | Arquivo |
|-----|-----------|---------|---------|
| monark-sfx-limbo-ambient | Vazio existencial (drone grave + vento distante) | Background loop do Limbo | `monark-sfx-ambient.wav` |
| monark-sfx-chair-creak | Cadeira de podcast flutuante rangendo | Idle do Monark | `monark-sfx-chair.wav` |
| monark-sfx-smoke-puff | Baforada de fumaça saindo das orelhas | Loop visual de fumaça | `monark-sfx-smoke.wav` |
| monark-sfx-mic-feedback | Feedback de microfone (high pitch squeal) | Início de diálogo | `monark-sfx-feedback.wav` |
| monark-sfx-shop-open | Som de loja abrindo (cash register etéreo) | Abertura da Loja do Limbo | `monark-sfx-shop.wav` |
| monark-sfx-revive-whoosh | Whoosh ascendente (alma voltando ao corpo) | Jogador aceita segunda chance | `monark-sfx-revive.wav` |
| monark-sfx-cancel-stamp | Carimbo de "CANCELADO" batendo (thud + paper) | Debuff de cancelamento aplicado | `monark-sfx-cancel.wav` |
