# ARTHUR DO VAL / MAMÃE FALEI (O Co-Apresentador do Limbo) — Bordões de Áudio

**Voz**: Média-aguda, RÁPIDA, ansiosa. Fala atropelada como quem está sempre se justificando. Volume alto mas sem autoridade — grita por desespero, não por poder. Tom de indignação permanente que ninguém leva a sério.
**TTS Voice**: `pt-BR-AntonioNeural` — ajustar rate +15% para fala rápida + pitch +2Hz (mais agudo que o normal)
**Alternativa**: Voice actor fazendo político jovem desesperado — gesticula enquanto fala (afeta a voz), interrompe a si próprio.

---

### 1. "Isso é um absurdo! Eu fui tirado de contexto!"
- **Trigger**: spawn no Limbo / qualquer interação inicial
- **Emoção**: Indignação crônica + negação automática
- **Volume**: 8/10
- **Duração**: 2.5s
- **Frequência**: A cada aparição do jogador no Limbo
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Isso é um absurdo! Eu fui tirado de contexto!" --rate "+15%" --pitch "+2Hz" --write-media arthur-01-contexto.mp3`
- **Processamento**: Reverb Limbo (mesmo do Monark) + leve eco no "contexto" (ironia — o contexto é o problema)
- **URL referência**: Defesa padrão de Arthur do Val após vazamento dos áudios sobre refugiadas ucranianas
- **Notas**: Dito ANTES de qualquer um perguntar qualquer coisa. Arthur já entra se defendendo. A velocidade mostra desespero. O "tirado de contexto" é sua armadura verbal — usa pra tudo.

### 2. "Mamãe falei, mas falei DEMAIS."
- **Trigger**: idle auto-reflexivo (raro) / após dar dica errada
- **Emoção**: Rara auto-consciência seguida de arrependimento momentâneo
- **Volume**: 5/10
- **Duração**: 2.5s
- **Frequência**: 10% idle / após erro
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Mamãe falei... mas falei DEMAIS." --rate "+5%" --pitch "+1Hz" --write-media arthur-02-demais.mp3`
- **Processamento**: Primeira parte normal. "DEMAIS" com suspiro + volume -20% (auto-consciência)
- **URL referência**: Trocadilho com nome do canal dele + auto-reconhecimento
- **Notas**: O ÚNICO momento de honestidade do Arthur. O trocadilho é a piada, mas o tom é genuinamente reflexivo. Dura 2 segundos, depois volta à indignação padrão.

### 3. "No Limbo pelo menos ninguém grava meus áudios."
- **Trigger**: idle no Limbo
- **Emoção**: Alívio perverso + trauma de vazamento
- **Volume**: 5/10
- **Duração**: 3.0s
- **Frequência**: 20% idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "No Limbo pelo menos ninguém grava meus áudios." --rate "+5%" --pitch "+1Hz" --write-media arthur-03-audios.mp3`
- **Processamento**: Reverb Limbo + suspiro de alívio no final
- **URL referência**: Referência ao escândalo dos áudios vazados sobre refugiadas ucranianas
- **Notas**: Olha ao redor paranoico enquanto fala. O "pelo menos" contém todo o trauma. O suspiro de alívio é genuíno — o Limbo é melhor que o mundo real para ele.

### 4. "Eu era deputado, sabia? DEPUTADO!"
- **Trigger**: idle indignado / ao ser ignorado pelo jogador
- **Emoção**: Nostalgia de poder perdido + indignação que ninguém respeita
- **Volume**: 8/10
- **Duração**: 2.5s
- **Frequência**: 25% idle / quando jogador ignora ele
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu era deputado, sabia? DEPUTADO!" --rate "+10%" --pitch "+2Hz" --write-media arthur-04-deputado.mp3`
- **Processamento**: "DEPUTADO!" com eco que morre rápido (no Limbo, ninguém se impressiona)
- **URL referência**: Arthur do Val foi deputado estadual de SP antes do cancelamento
- **Notas**: A repetição "DEPUTADO!" é gritada com toda força, mas o eco morre instantaneamente — o Limbo absorve pretensão. É uma metáfora sonora: o título não vale nada aqui.

### 5. "Isso aqui é censura! Onde está meu advogado?"
- **Trigger**: quando jogador tenta sair do Limbo sem interagir
- **Emoção**: Indignação legal absurda aplicada ao além
- **Volume**: 7/10
- **Duração**: 2.5s
- **Frequência**: Quando jogador se afasta
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Isso aqui é censura! Onde está meu advogado?" --rate "+15%" --pitch "+2Hz" --write-media arthur-05-censura.mp3`
- **Processamento**: Reverb Limbo + desespero crescente
- **Notas**: Tenta usar vocabulário legal no Limbo. Não funciona. Ninguém responde. A piada é que ele acha que direitos legais valem no além.

### 6. "DENÚNCIA EXCLUSIVA: O Limbo é mal administrado!"
- **Trigger**: skill Denúncia do Limbo (oferecendo dicas ao jogador)
- **Emoção**: Jornalismo amador + indignação de YouTuber
- **Volume**: 8/10
- **Duração**: 3.0s
- **Frequência**: A cada uso da skill
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "DENÚNCIA EXCLUSIVA: O Limbo é mal administrado!" --rate "+10%" --pitch "+2Hz" --write-media arthur-06-denuncia.mp3`
- **Processamento**: Estilo breaking news (jingle sutil de noticiário em background) + eco de Limbo
- **URL referência**: Estilo Mamãe Falei de denúncia — sensacionalismo de YouTuber político
- **Notas**: Tenta fazer denúncia do Limbo como se fosse matéria jornalística. Ninguém se importa. O jingle de noticiário em background é desafinado e triste — reflete a decadência do "jornalismo" dele.

---

## Efeitos Sonoros Específicos do Arthur do Val

| SFX | Descrição | Trigger | Arquivo |
|-----|-----------|---------|---------|
| arthur-sfx-phone-record | Beep de gravação de celular (trauma) | Quando alguém fala perto dele | `arthur-sfx-record.wav` |
| arthur-sfx-mouth-flap | Boca que não para (flap-flap-flap) | Loop idle — boca sempre movendo | `arthur-sfx-mouth.wav` |
| arthur-sfx-mic-small | Microfone menor que o do Monark (som mais fraco) | Quando fala ao microfone | `arthur-sfx-mic.wav` |
| arthur-sfx-gasp | Gasp de "pego no flagra" | Idle — expressão permanente | `arthur-sfx-gasp.wav` |
| arthur-sfx-wrinkle | Som de camisa amarrotada (fabric crumple) | Movimento | `arthur-sfx-wrinkle.wav` |
