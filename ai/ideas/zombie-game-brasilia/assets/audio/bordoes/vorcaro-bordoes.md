# DANIEL VORCARO (O Banqueiro do Master) — Bordões de Áudio

**Voz**: Média, SUAVE, controlada. Voz de quem fala baixo porque sabe que todos precisam se inclinar para ouvir. Tom de businessman que trata crime como reunião de board. Dicção perfeita, sem sotaque forte. Sorriso audível em cada palavra.
**TTS Voice**: `pt-BR-AntonioNeural` — ajustar rate -10% para fala calculada + pitch neutro
**Alternativa**: Voice actor fazendo voz de CEO de banco — suave como veludo, ameaçadora como seda escondendo aço.

---

### 1. "Isso não é corrupção, é networking."
- **Trigger**: spawn / idle principal / ao corromper inimigo (Captura Financeira)
- **Emoção**: Amoralidade casual, sociopatia com charm
- **Volume**: 6/10
- **Duração**: 2.5s
- **Frequência**: Ao aparecer + a cada uso de Captura Financeira
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Isso não é corrupção... é networking." --rate "-10%" --pitch "0Hz" --write-media vorcaro-01-networking.mp3`
- **Processamento**: Sem reverb (intimista — como se falasse direto no ouvido) + leve boost de graves (autoridade)
- **URL referência**: Frase criada para o jogo — captura a essência do euphemism corporativo para crime
- **Notas**: Pausa de 0.5s entre "corrupção..." e "é networking". O "networking" é dito com sorriso audível — como se estivesse explicando algo óbvio para alguém lento.

### 2. "Eu conheço TODO MUNDO. E tenho TUDO gravado."
- **Trigger**: skill Celular Bomba / ameaça
- **Emoção**: Poder absoluto do informante — calma ameaçadora
- **Volume**: 7/10
- **Duração**: 3.0s
- **Frequência**: A cada uso de Celular Bomba
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu conheço TODO MUNDO. E tenho TUDO gravado." --rate "-15%" --pitch "-1Hz" --write-media vorcaro-02-gravado.mp3`
- **Processamento**: "TODO MUNDO" com ênfase (volume +20%). "TUDO gravado" com som de celular gravando em background (beep sutil)
- **URL referência**: Referência ao celular apreendido com conversas de metade da classe política
- **Notas**: A frase mais ameaçadora do jogo. Não é gritada — é sussurrada com poder. O beep de gravação em background é perturbador. Quem ouve sabe que está sendo gravado.

### 3. "R$52 bilhões? É um número relativo..."
- **Trigger**: skill R$52 Bilhões / idle
- **Emoção**: Minimalização do absurdo, gaslighting financeiro
- **Volume**: 5/10
- **Duração**: 2.5s
- **Frequência**: A cada uso da skill / 20% idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "R$52 bilhões? É um número relativo..." --rate "-10%" --pitch "0Hz" --write-media vorcaro-03-bilhoes.mp3`
- **Processamento**: Leve reverb corporativo (sala de reunião) + som de moedas caindo distante
- **Notas**: Dito com a casualidade de quem fala de troco de padaria. O "relativo" é CHAVE — sorriso audível. Moedas caindo em background reforçam que o dinheiro está literalmente flutuando ao redor dele.

### 4. "Delação? Vou pensar. ...já pensei. Quem eu entrego primeiro?"
- **Trigger**: ao ser derrotado / HP baixo / skill Delação Premiada
- **Emoção**: Oportunismo instantâneo, lealdade zero
- **Volume**: 7/10
- **Duração**: 4.0s
- **Frequência**: Ao morrer / HP < 15%
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Delação? Vou pensar. ...já pensei. Quem eu entrego primeiro?" --rate "-5%" --pitch "0Hz" --write-media vorcaro-04-delacao.mp3`
- **Processamento**: Pausa de 0.3s entre "pensar." e "...já pensei." — a decisão mais rápida da história
- **URL referência**: Referência à negociação de delação premiada com a PF
- **Notas**: A velocidade entre "Vou pensar" e "já pensei" mostra que não houve pensamento algum. Vorcaro trairia qualquer um instantaneamente. "Quem eu entrego primeiro?" é dito com entusiasmo genuíno.

### 5. "O dinheiro não some. Ele muda de endereço."
- **Trigger**: idle filosofico / ao soltar particulas de dinheiro
- **Emoção**: Sabedoria criminosa, cinismo elegante
- **Volume**: 5/10
- **Duração**: 2.5s
- **Frequência**: 15% idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "O dinheiro não some. Ele muda de endereço." --rate "-15%" --pitch "-1Hz" --write-media vorcaro-05-endereco.mp3`
- **Processamento**: Reverb de sala vazia (solidão do rico) + som de notas flutuando
- **Notas**: A frase mais filosoficamente honesta do personagem. Dita como quem ensina uma lição de vida. Som de notas flutuando ao redor adiciona literalidade à metáfora.

### 6. "Vorcaro, Daniel. Prazer. Quanto custa o seu... silêncio?"
- **Trigger**: ao encontrar novo NPC/personagem / primeiro encontro
- **Emoção**: Charm predatório + oferta implícita
- **Volume**: 6/10
- **Duração**: 3.5s
- **Frequência**: Primeiro encontro com cada personagem
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Vorcaro, Daniel. Prazer. Quanto custa o seu... silêncio?" --rate "-10%" --pitch "0Hz" --write-media vorcaro-06-prazer.mp3`
- **Processamento**: Pausa de 0.5s antes de "silêncio" — a palavra que muda tudo
- **Notas**: Começa como apresentação profissional normal. A pausa antes de "silêncio" transforma a frase em ameaça/suborno. Sorriso audível no "silêncio".

---

## Efeitos Sonoros Específicos do Vorcaro

| SFX | Descrição | Trigger | Arquivo |
|-----|-----------|---------|---------|
| vorcaro-sfx-money-float | Notas de dinheiro flutuando (paper flutter + shimmer) | Loop ambient permanente | `vorcaro-sfx-money.wav` |
| vorcaro-sfx-phone-buzz | Celular vibrando com notificação (buzz + flash) | Loop ambient / Celular Bomba | `vorcaro-sfx-phone.wav` |
| vorcaro-sfx-phone-reveal | Som de revelação (tá-dá sinistro) | Celular Bomba — mostra tela | `vorcaro-sfx-reveal.wav` |
| vorcaro-sfx-coin-count | Dedos contando moedas rapidamente (clink-clink-clink) | Idle — dedos contando | `vorcaro-sfx-count.wav` |
| vorcaro-sfx-teeth-gleam | Brilho de dentes (ping! como estrela de anime) | Sorriso em close | `vorcaro-sfx-teeth.wav` |
| vorcaro-sfx-corruption | Som de corrupção (moeda caindo + sussurro) | Captura Financeira — zumbi corrompido | `vorcaro-sfx-corrupt.wav` |
| vorcaro-sfx-money-explosion | Explosão de notas (confete + whoosh) | Skill R$52 Bilhões | `vorcaro-sfx-explosion.wav` |
