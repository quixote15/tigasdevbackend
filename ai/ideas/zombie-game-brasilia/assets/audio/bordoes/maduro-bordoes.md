# MADURO (O Ditador Palhaço) — Bordões de Áudio

**Voz**: Média, pomposa, EXAGERADAMENTE séria para coisas ridículas. Sotaque venezuelano forte (espanhol misturado com português torto). Dicção de discurso presidencial para conteúdo absurdo. O contraste entre o tom sério e o conteúdo ridículo É a piada.
**TTS Voice**: `es-VE-SebastianNeural` (espanhol venezuelano) mixado com `pt-BR-AntonioNeural` — algumas frases em portunhol
**Alternativa**: Voice actor fazendo sotaque venezuelano tentando falar português. Tom de Fidel Castro fazendo stand-up sem querer.

---

### 1. "Nosso plano econômico: imprimir mais dinheiro!"
- **Trigger**: spawn / skill Plano Econômico Absurdo
- **Emoção**: Convicção ABSOLUTA em ideia absurda
- **Volume**: 8/10
- **Duração**: 3.0s
- **Frequência**: Ao aparecer + a cada uso da skill
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Nosso plano econômico é simples: imprimir mais dinheiro!" --rate "-5%" --pitch "-1Hz" --write-media maduro-01-plano.mp3`
- **Processamento**: Leve eco de discurso (reverb de palanque) + aplausos falsos sutis em background (3 pessoas batendo palma)
- **URL referência**: Sátira da política econômica venezuelana — hiperinflação como piada
- **Notas**: Dito com a SERIEDADE de quem acredita genuinamente que é um bom plano. Os aplausos falsos são de 3 pessoas no máximo (milícia aplaudindo). O "imprimir mais dinheiro" deve soar como revelação genial.

### 2. "O imperialismo americano não nos deterá!"
- **Trigger**: ao encontrar Trump no mapa / ao levar dano de jogador
- **Emoção**: Raiva revolucionária + covardia mal disfarçada
- **Volume**: 9/10
- **Duração**: 2.5s
- **Frequência**: Ao ver Trump / a cada hit recebido (25% chance)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "O imperialismo americano não nos deterá!" --rate "+5%" --pitch "+1Hz" --write-media maduro-02-imperialismo.mp3`
- **Processamento**: Reverb de palanque + eco dramático no "deterá"
- **URL referência**: Discurso padrão anti-EUA do Maduro real
- **Notas**: Gritado com punho erguido. Mas se Trump realmente se aproximar, Maduro recua. O contraste entre a bravata e a covardia é proposital.

### 3. "Lula, me defende! LULA!"
- **Trigger**: ao levar dano pesado / HP baixo / sem Lula por perto
- **Emoção**: Desespero + dependência patética
- **Volume**: 8/10
- **Duração**: 2.0s
- **Frequência**: HP < 30%
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Lula, me defende! LULA!" --rate "+10%" --pitch "+3Hz" --write-media maduro-03-lula.mp3`
- **Processamento**: Voz levemente trêmula + desespero crescente no segundo "LULA!"
- **URL referência**: Referência a Lula defendendo Maduro diplomaticamente
- **Notas**: O primeiro "Lula, me defende!" é pedido. O segundo "LULA!" é grito de socorro. Se Lula não está no mapa, deve ter eco vazio (ninguém responde). Patético por design.

### 4. "A revolução bolivariana é eterna! ...certo?"
- **Trigger**: idle / quando sozinho
- **Emoção**: Bravata seguida de insegurança
- **Volume**: 6/10
- **Duração**: 3.0s
- **Frequência**: Cada 20s em idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A revolução bolivariana é eterna! ...certo?" --rate "-5%" --pitch "-1Hz" --write-media maduro-04-revolucao.mp3`
- **Processamento**: "É eterna!" com eco forte. "...certo?" sussurrado, quase inaudível, sem eco.
- **URL referência**: Retórica bolivariana com insegurança
- **Notas**: A transição entre convicção ("é eterna!") e dúvida ("...certo?") é INSTANTÂNEA. Sem transição. O bigode se move detectando a mentira.

### 5. "Las elecciones fueron perfectas! Yo gané con 107%!"
- **Trigger**: raro / idle especial
- **Emoção**: Fraude eleitoral como fato casual
- **Volume**: 7/10
- **Duração**: 3.0s
- **Frequência**: 15% de chance em idle
- **TTS Command**: `edge-tts --voice "es-VE-SebastianNeural" --text "Las elecciones fueron perfectas! Yo gané con ciento siete por ciento!" --rate "-5%" --write-media maduro-05-elecciones.mp3`
- **Processamento**: Eco de palanque + riso abafado distante
- **Notas**: Em espanhol puro. O "107%" é dito com orgulho genuíno. Ninguém questiona. O riso distante é dos poucos que ainda têm sanidade.

### 6. "Maduro... Nicolás... MADURO!" (tentativa de grito patriota)
- **Trigger**: ao ver Enéas (tentativa de imitar o bordão)
- **Emoção**: Inveja + imitação fracassada
- **Volume**: 7/10
- **Duração**: 2.5s
- **Frequência**: Quando Enéas aparece
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Maduro... Nicolás... MADURO!" --rate "-10%" --pitch "-2Hz" --write-media maduro-06-imita.mp3`
- **Processamento**: Eco fraco (imitação falhada — não tem a potência do Enéas) + silêncio constrangedor após
- **Notas**: Maduro tenta fazer o "MEU NOME É ENÉAS!" mas com seu nome. Fracassa miseravelmente. Nenhum inimigo para. Ninguém se impressiona. 2s de silêncio constrangedor.

---

## Efeitos Sonoros Específicos do Maduro

| SFX | Descrição | Trigger | Arquivo |
|-----|-----------|---------|---------|
| maduro-sfx-bigode-twitch | Som de pelo se movendo (foley sutil) | Bigode detecta mentira | `maduro-sfx-bigode.wav` |
| maduro-sfx-medal-clink | Medalhas de papel alumínio tilintando | Movimento / idle | `maduro-sfx-medals.wav` |
| maduro-sfx-applause-fake | 3 pessoas batendo palma desanimadamente | Após discurso / skill | `maduro-sfx-applause.wav` |
| maduro-sfx-money-printer | Impressora de dinheiro (brrrrr) | Skill Plano Econômico | `maduro-sfx-printer.wav` |
| maduro-sfx-boina-fall | Boina caindo e sendo recolocada | Hit recebido | `maduro-sfx-boina.wav` |
