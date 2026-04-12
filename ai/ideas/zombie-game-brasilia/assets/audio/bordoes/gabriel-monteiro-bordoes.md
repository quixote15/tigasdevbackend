# GABRIEL MONTEIRO (O Recorrente do Limbo) — Bordões de Áudio

**Voz**: Média, FORÇADA, tentando soar heróica mas saindo patética. Tom de YouTuber fazendo voz de "policial durão" que não convence ninguém. Alternância entre bravata (quando acha que está bem) e lamento (quando percebe que não está).
**TTS Voice**: `pt-BR-AntonioNeural` — ajustar rate normal + pitch +1Hz (ligeiramente forçado)
**Alternativa**: Voice actor fazendo voz de quem imita ator de filme de ação mas não consegue — a tentativa de parecer forte É a fraqueza.

---

### 1. "Eu era policial! Eu era vereador! Eu era YouTuber!"
- **Trigger**: spawn no Limbo / idle principal
- **Emoção**: Nostalgia desesperada de todas as identidades perdidas
- **Volume**: 7/10
- **Duração**: 3.0s
- **Frequência**: Ao aparecer + cada 20s idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu era policial! Eu era vereador! Eu era YouTuber!" --rate "+5%" --pitch "+1Hz" --write-media gabriel-01-era.mp3`
- **Processamento**: Cada "Eu era" com crescendo de desespero. "Policial" com eco médio. "Vereador" com eco menor. "YouTuber" com eco quase morto — degradação progressiva de importância.
- **URL referência**: Gabriel Monteiro foi policial militar, vereador do Rio de Janeiro, e YouTuber — perdeu tudo
- **Notas**: A degradação do eco representa a degradação da importância de cada título. Policial = alguma respeitabilidade. Vereador = menos. YouTuber = o fundo do poço. Cada repetição de "Eu era" soa mais desesperada.

### 2. "O Limbo é injusto. ...tá, talvez não."
- **Trigger**: idle reflexivo / ao reclamar e ser confrontado
- **Emoção**: Indignação que dura 2s antes de virar auto-consciência forçada
- **Volume**: 6/10
- **Duração**: 2.5s
- **Frequência**: 20% idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "O Limbo é injusto. ...tá, talvez não." --rate "-5%" --pitch "+1Hz" --write-media gabriel-02-injusto.mp3`
- **Processamento**: "É injusto" com convicção. Pausa 0.8s. "...tá, talvez não" sussurrado, quase pra si.
- **URL referência**: Personagem que tenta se vitimizar mas a realidade não permite
- **Notas**: A pausa é onde Gabriel olha ao redor, vê que ninguém compra a vitimização, e recua. O "tá, talvez não" é a confissão mais sincera que ele consegue dar.

### 3. "Quando eu saio daqui? ...nunca? Ah."
- **Trigger**: idle / ao perguntar sobre saída do Limbo
- **Emoção**: Esperança → realidade → aceitação triste
- **Volume**: 5/10
- **Duração**: 3.0s
- **Frequência**: 15% idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Quando eu saio daqui? ...nunca? ...ah." --rate "-10%" --pitch "+1Hz" --write-media gabriel-03-nunca.mp3`
- **Processamento**: "Quando eu saio daqui?" com esperança genuína (pitch +2Hz). "...nunca?" com medo (pitch neutro). "Ah." com aceitação morta (pitch -2Hz, volume -40%)
- **URL referência**: Gabriel Monteiro é residente PERMANENTE do Limbo — cancelamento sem retorno
- **Notas**: O "Ah." final é o som mais triste do jogo. Monossilábico. Toda a esperança, pergunta e aceitação em uma sílaba. Ele sabe. Sempre soube.

### 4. "Eu fazia vídeos ajudando pessoas! ...não me olhem assim."
- **Trigger**: quando outros NPCs do Limbo o encaram / jogador olha pra ele
- **Emoção**: Tentativa de redenção que todos sabem que é falsa
- **Volume**: 6/10
- **Duração**: 3.5s
- **Frequência**: Quando jogador foca nele
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu fazia vídeos ajudando pessoas! ...não me olhem assim." --rate "+5%" --pitch "+1Hz" --write-media gabriel-04-videos.mp3`
- **Processamento**: Primeira parte com convicção forçada. "Não me olhem assim" dito olhando pro chão — volume -20%, tom derrotado
- **URL referência**: Gabriel Monteiro ficou famoso com vídeos "ajudando" pessoas — depois revelados como armados/encenados
- **Notas**: A primeira parte é a persona pública — o herói de YouTube. A segunda parte é a realidade — todos sabem que era tudo armado. A transição é instantânea e brutal.

### 5. "Operação... policial... no... Limbo..." *dorme de pé*
- **Trigger**: idle longo (40s+) — Gabriel cochila no Limbo
- **Emoção**: Degradação total — nem a persona falsa ele consegue manter
- **Volume**: 3/10 (murmúrio)
- **Duração**: 3.0s
- **Frequência**: Após 40s de idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Operação... policial... no... Limbo..." --rate "-30%" --pitch "-2Hz" --write-media gabriel-05-dorme.mp3`
- **Processamento**: Fala arrastada + fade-out gradual + ronco leve no final (1s)
- **Notas**: Gabriel está tão degradado pelo Limbo que cochila no meio de tentar ser herói. A "operação policial no Limbo" é absurda e ele nem consegue terminar a frase. O ronco final é patético e cômico.

### 6. "Vocês vão ver quando eu voltar! EU VOU VOLTAR!"
- **Trigger**: raro / quando jogador sai do Limbo sem interagir com ele
- **Emoção**: Bravata vazia — a negação mais profunda
- **Volume**: 8/10
- **Duração**: 2.5s
- **Frequência**: Ao jogador sair do Limbo
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Vocês vão ver quando eu voltar! EU VOU VOLTAR!" --rate "+10%" --pitch "+2Hz" --write-media gabriel-06-voltar.mp3`
- **Processamento**: Gritado com desespero. Eco do Limbo absorve o som rapidamente — o vazio engole o grito.
- **Notas**: O grito desesperado de quem sabe que não volta. O eco sendo absorvido pelo vazio é a metáfora sonora: o Limbo não ecoa bravatas — engole. O silêncio após é ensurdecedor.

---

## Efeitos Sonoros Específicos do Gabriel Monteiro

| SFX | Descrição | Trigger | Arquivo |
|-----|-----------|---------|---------|
| gabriel-sfx-badge-rattle | Crachá "CANCELADO PERMANENTE" balançando no peito | Movimento | `gabriel-sfx-badge.wav` |
| gabriel-sfx-shadow-grow | Sombra crescendo (som grave ameaçador) | Idle — sombra maior que ele | `gabriel-sfx-shadow.wav` |
| gabriel-sfx-camera-fake | Som de câmera ligando (fake — está encenando) | Skill Vídeo Armado | `gabriel-sfx-camera.wav` |
| gabriel-sfx-shirt-fade | Tecido desbotando (fabric stretch) | Ambient — camiseta desbotada | `gabriel-sfx-fade.wav` |
| gabriel-sfx-snore | Ronco leve | Idle longo — cochila | `gabriel-sfx-snore.wav` |
