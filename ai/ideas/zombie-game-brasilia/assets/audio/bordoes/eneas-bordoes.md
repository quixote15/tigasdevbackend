# ENÉAS CARNEIRO (O Fantasma Patriota) — Bordões de Áudio

**Voz**: Grave profunda, IMPONENTE, ressonante como caixa de som de catedral. Dicção perfeita — cada sílaba pronunciada com gravidade presidencial. Tom de discurso épico, NUNCA cômico direto. A comédia vem da reverência absurda. Eco natural de fantasma (reverb pesado).
**TTS Voice**: `pt-BR-AntonioNeural` — ajustar pitch -5Hz para gravidade extrema + reverb massivo
**Alternativa**: Voice actor fazendo voz grave de orador clássico anos 90 com eco sobrenatural. Referência: pregador evangélico SÉRIO (não gritando), político de palanque antigo.

---

### 1. "MEU NOME É ENÉAS!"
- **Trigger**: spawn / aparição inicial / skill Grito Patriota
- **Emoção**: Dignidade ABSOLUTA, apresentação sagrada, impacto sísmico
- **Volume**: 10/10 (o mais alto do jogo inteiro)
- **Duração**: 2.5s
- **Frequência**: Na aparição + a cada uso do Grito Patriota
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "MEU NOME... É ENÉAS!" --rate "-20%" --pitch "-5Hz" --write-media eneas-01-grito.mp3`
- **Processamento**: Reverb cathedral (decay 3s) + leve distorção de holograma (tremolo 2Hz) + sub-bass boost. Tela deve tremer em sync.
- **URL referência**: Bordão LENDÁRIO da campanha presidencial de 1994/1998/2002. Viral antes da internet existir.
- **Notas**: A frase mais icônica da política brasileira. Pausa dramática de 0.8s entre "MEU NOME..." e "É ENÉAS!". O "ENÉAS" deve estender ligeiramente o "É" (ENÉÉÉAS). O eco deve continuar por 2s após a frase terminar. Quando toca, TUDO para — até o tema musical do jogo diminui volume.

### 2. "MEU NÚMERO É CINQUENTA E SEEEEIS!"
- **Trigger**: skill 56! / ataque numérico
- **Emoção**: Paixão patriótica, urgência eleitoral de outro tempo
- **Volume**: 10/10
- **Duração**: 3.5s
- **Frequência**: A cada uso da skill 56!
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "MEU NÚMERO... É CINQUENTA E SEEEEIS!" --rate "-15%" --pitch "-5Hz" --write-media eneas-02-56.mp3`
- **Processamento**: Reverb cathedral + crescendo no "SEEEEIS" (volume sobe 20% na última sílaba) + harmônico grave adicionado. O "56" numérico gigante surge na tela em sync.
- **URL referência**: Segundo bordão mais famoso — usado em todo horário eleitoral gratuito
- **Notas**: O "SEEEEIS" deve ser ESTENDIDO como se o Enéas estivesse segurando uma nota musical épica. Duração do "SEEEEIS" = 1.5s mínimo. Imagine um cantor de ópera terminando uma ária. É ESSE o nível de dramaticidade.

### 3. "Se eu tivesse sido presidente..."
- **Trigger**: idle / passiva Saudade do Que Não Tivemos
- **Emoção**: Melancolia profunda, nostalgia cósmica, "e se...?"
- **Volume**: 5/10 (sussurro grave)
- **Duração**: 3.0s
- **Frequência**: Loop de idle a cada 25s
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Se eu tivesse sido presidente..." --rate "-25%" --pitch "-6Hz" --write-media eneas-03-saudade.mp3`
- **Processamento**: Reverb ghost (decay longo 4s) + filtro etéreo (high-cut a 3kHz) + leve chorus. Deve soar como vindo de outro plano de existência.
- **URL referência**: Frase criada para o jogo — captura o sentimento de "saudade do que não tivemos"
- **Notas**: Dito como reflexão sussurrada, não como discurso. É o momento mais HUMANO do Enéas. A melancolia deve ser palpável. Os outros personagens (se presentes) completam automaticamente: "...seria diferente." (em coro baixo, quase inaudível).

### 4. "...seria diferente." (CORO)
- **Trigger**: resposta automática ao bordão 3 (dito por outros NPCs/inimigos presentes)
- **Emoção**: Respeito coletivo, reconhecimento universal
- **Volume**: 3/10 (coro distante)
- **Duração**: 1.5s
- **Frequência**: Sempre após bordão 3
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "...seria diferente." --rate "-20%" --pitch "-3Hz" --write-media eneas-04-coro.mp3` (multiplicar em 3 vozes com pitch ligeiramente diferente)
- **Processamento**: 3 camadas de voz com pitch variado (-2Hz, 0, +2Hz) + reverb catedral + fade-in suave
- **Notas**: Dito por TODOS os personagens presentes na cena simultaneamente. Até inimigos. Até zumbis. É o momento mais surreal do jogo — todos param, dizem a frase em uníssono, e voltam ao normal.

### 5. "MEU NOME... É ENEEEEEEEAS!" (ULTIMATE)
- **Trigger**: ultimate / aparição holográfica gigante
- **Emoção**: ÁPICE ABSOLUTO. Grandiosidade impossível. O grito que racha a realidade.
- **Volume**: 11/10 (acima do máximo — clipar intencionalmente o áudio)
- **Duração**: 5.0s
- **Frequência**: ÚNICA por partida
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "MEU NOME... É ENEEEEEEEAS!" --rate "-30%" --pitch "-7Hz" --write-media eneas-05-ultimate.mp3`
- **Processamento**: ESPECIAL:
  1. Começa com reverb catedral
  2. No "É" — som de vidro rachando (crack)
  3. No "ENEEEEEEEAS" — crescendo MASSIVO, sub-bass extremo, reverb infinito
  4. Após a frase — 3s de eco que vai morrendo lentamente
  5. Leve distorção digital (glitch) como se o som quebrasse o jogo
  6. Trilha sonora do jogo SILENCIA durante o grito
- **URL referência**: Versão maximizada do bordão — o grito DEFINITIVO
- **Notas**: Este é O MOMENTO do jogo. A performance sonora deve ser épica ao ponto de dar arrepio. O jogador deve sentir que algo SAGRADO aconteceu. O áudio deve ser processado para parecer que vem de DENTRO do jogo quebrando a quarta parede. Após o grito, 2s de silêncio absoluto antes do jogo voltar ao normal.

### 6. Silêncio Respeitoso
- **Trigger**: skill O Verdadeiro Patriota (passiva) — momento em que todos param
- **Emoção**: Reverência coletiva
- **Volume**: 0/10 → 2/10
- **Duração**: 1.5s
- **Frequência**: A cada aparição
- **Arquivo**: `eneas-06-silencio.mp3`
- **Processamento**: Não é uma fala. É: mute total do jogo (1s) → som de vento suave → leve humming grave como harpa distante → retorno gradual dos sons do jogo
- **Notas**: O SILÊNCIO é o bordão. Quando Enéas aparece, tudo cala. Esse arquivo de áudio é literalmente silêncio com uma leve ambiência etérea. É mais impactante que qualquer grito.

---

## Efeitos Sonoros Específicos do Enéas

| SFX | Descrição | Trigger | Arquivo |
|-----|-----------|---------|---------|
| eneas-sfx-hologram-on | Materialização holográfica (zap elétrico + shimmer) | Aparição | `eneas-sfx-hologram.wav` |
| eneas-sfx-hologram-flicker | Holograma piscando/falhando (estática + tremolo) | Loop ambient | `eneas-sfx-flicker.wav` |
| eneas-sfx-mustache-detach | Som cômico de algo se desprendendo + whoosh | Arma Bigode da Justiça (lançar) | `eneas-sfx-detach.wav` |
| eneas-sfx-mustache-spin | Whoosh rotativo (como hélice) | Bigode girando | `eneas-sfx-spin.wav` |
| eneas-sfx-mustache-return | Snap magnético + click de reencaixe | Bigode voltando ao rosto | `eneas-sfx-return.wav` |
| eneas-sfx-screen-crack | Vidro rachando + estalo profundo | Ultimate — tela quebrando | `eneas-sfx-crack.wav` |
| eneas-sfx-screen-rebuild | Vidro se remontando (reverso do crack) | Tela se reconstruindo | `eneas-sfx-rebuild.wav` |
| eneas-sfx-aura-golden | Humming dourado/angélico (loop) | Aura passiva | `eneas-sfx-aura.wav` |
| eneas-sfx-flag-flutter | Tecido esvoaçante (bandeira ao vento) | Capa-bandeira do Brasil | `eneas-sfx-flag.wav` |
| eneas-sfx-56-launch | Impacto numérico + whoosh | Número 56 sendo lançado | `eneas-sfx-56.wav` |
