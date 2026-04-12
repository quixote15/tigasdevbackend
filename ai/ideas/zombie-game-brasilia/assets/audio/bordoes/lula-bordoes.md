# LULA (O Cachaceiro) -- Bordoes & Audio Script
### Boss Principal (Lado Esquerdo) | Zumbis de Brasilia
### Referencia: Transcricoes Andre Guedes + Memes Virais

---

## Visao Geral

Lula e o personagem mais VERBAL do jogo. Fala CONSTANTEMENTE. O jogador nunca pode esquecer que ele esta ali. Mesmo quando nao esta atacando, esta murmurando, reclamando, discursando. O audio e tao importante quanto o visual para este boss.

### Diretrizes de Voz
- **Tom**: Grave-medio, rouco de cachaca. Voz de fumante/bebedor.
- **Sotaque**: Nordestino forte (Pernambuco). "R" retroflexo no final de silabas. "E" aberto. "Voces" vira "voceis".
- **Ritmo**: Lento no inicio, acelera no meio, perde o fio da meada, recomeca.
- **Emocao base**: Entre raiva teatral e contentamento alcoolico. Nunca neutro.
- **Volume**: Tende a GRITAR no final das frases mesmo que comece sussurrando.
- **Erros gramaticais**: INTENCIONAIS. "A gente vamos", "nos vamos fazer o que", etc.
- **TTS Voice padrao**: `pt-BR-AntonioNeural` (edge-tts) -- grave, masculina. Ajustar rate -15% para fala arrastada.
- **Bark Voice**: `v2/pt_speaker_3` (grave masculino)

### Formato dos Arquivos de Audio
- Formato: OGG Vorbis (para web/Phaser 3) + WAV backup
- Sample rate: 44100 Hz
- Bit depth: 16-bit
- Channels: Mono
- Normalizacao: -3dB peak
- Duracao maxima por bordao: 4000ms (exceto Discurso Ultimate que e 8000ms)

---

## BORDOES PRINCIPAIS (In-Game)

### 1. "Eu quero dizer pra voces..."
**ID**: `lula_eu_quero_dizer`
**Arquivo**: `bordoes/lula_eu_quero_dizer.ogg`
**Duracao**: 1800ms
**Trigger**: Idle aleatorio (a cada 5-8s), Inicio de Fato Alternativo
**Volume**: 0.6
**Emocao**: Didatico, condescendente, levemente irritado. Retorica vazia -- tom de quem vai comecar um discurso e nunca chega ao ponto.
**Prioridade**: MAXIMA -- e a frase mais reconhecivel do Lula no universo Andre Guedes. Muleta verbal que abre TODA frase.

**Script fonetico (guia de pronuncia)**:
> "Eu quéru dizê pra vocêis..."

**Timing interno**:
- 0-200ms: "Eu" (pausa dramatica de 100ms depois)
- 300-700ms: "quero dizer" (rapido, como se fosse uma palavra so)
- 700-800ms: pausa
- 800-1500ms: "pra voces..." (desacelerando, tom caindo)
- 1500-1800ms: silencio com respiracao

**TTS Commands**:
```bash
# edge-tts (Microsoft) -- Melhor para portugues brasileiro
edge-tts --voice "pt-BR-AntonioNeural" --rate "-15%" --pitch "-5Hz" --text "Eu quero dizer pra vocês..." --write-media bordoes/lula_eu_quero_dizer.ogg

# bark (Suno AI) -- Melhor para emocao/personalidade
python -c "
from bark import SAMPLE_RATE, generate_audio, preload_models
preload_models()
audio = generate_audio('[sighing] Eu quero dizer pra vocês... [pause]', history_prompt='v2/pt_speaker_3')
import scipy; scipy.io.wavfile.write('bordoes/lula_eu_quero_dizer.wav', SAMPLE_RATE, audio)
"

# piper (local, rapido)
echo "Eu quero dizer pra vocês" | piper --model pt_BR-faber-medium --output_file bordoes/lula_eu_quero_dizer.wav
```

**Pos-processamento (ffmpeg)**:
```bash
ffmpeg -i lula_eu_quero_dizer.wav -af "asetrate=44100*0.9,aresample=44100,highpass=f=80,lowpass=f=6000,afftdn=nf=-30" lula_eu_quero_dizer_processed.ogg
```

**URL referencia**: Compilacoes de discursos do Lula no YouTube -- frase de abertura universal.
**Notas**: O "voces" deve soar como "voceis". Nunca chega a dizer o que quer dizer.

---

### 2. "Companheiro alcool em mim!"
**ID**: `lula_companheiro_alcool`
**Arquivo**: `bordoes/lula_companheiro_alcool.ogg`
**Duracao**: 1500ms
**Trigger**: Attack (Cachacada Companheira) com 30% chance, Spawn/inicio de wave
**Volume**: 0.7
**Emocao**: Alegria bebada, grito de guerra alcoolico, euforia. Saudacao calorosa de comicio + risada abafada.
**Prioridade**: Alta -- bordao exclusivo do Andre Guedes (trocadilho com "Alckmin")

**Script fonetico**:
> "Companhêiru álcool em mim!" (gritado, enfatico)

**Timing interno**:
- 0-500ms: "Companheiro" (rapido, como saudacao automatica)
- 500-600ms: micro-pausa
- 600-1100ms: "alcool em mim!" (GRITADO, crescendo, pico de volume)
- 1100-1500ms: eco natural + respiracao

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "+10%" --pitch "-3Hz" --volume "+20%" --text "Companheiro álcool em mim!" --write-media bordoes/lula_companheiro_alcool.ogg

# bark
python -c "
from bark import SAMPLE_RATE, generate_audio, preload_models
preload_models()
audio = generate_audio('[laughing] Companheiro álcool em mim! [laughing]', history_prompt='v2/pt_speaker_3')
import scipy; scipy.io.wavfile.write('bordoes/lula_companheiro_alcool.wav', SAMPLE_RATE, audio)
"
```

**Pos-processamento**:
```bash
ffmpeg -i lula_companheiro_alcool.wav -af "volume=1.3,highpass=f=100,lowpass=f=7000,adelay=0|30" lula_companheiro_alcool_processed.ogg
```

---

### 3. "Ta maravilhoso, companheiro!"
**ID**: `lula_ta_maravilhoso`
**Arquivo**: `bordoes/lula_ta_maravilhoso.ogg`
**Duracao**: 1600ms
**Trigger**: Idle aleatorio (cada 20s), Quarto Mandato (apos ressurreicao), attack_success
**Volume**: 0.5
**Emocao**: Satisfacao delirante, negacao da realidade, sorriso na voz. Otimismo absurdo -- dito com conviccao mesmo durante o apocalipse zumbi.
**Prioridade**: Media

**Script fonetico**:
> "Tá maravilhôso, companhêiru!" (tom alegre, quase cantando)

**Timing interno**:
- 0-200ms: "Ta" (curto, staccato)
- 200-900ms: "maravilhoooso" (esticado, saboreando a palavra)
- 900-1000ms: virgula (pausa)
- 1000-1500ms: "companheiro!" (automatico, reflexo)
- 1500-1600ms: risinho

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-5%" --pitch "-2Hz" --text "Tá maravilhoso, companheiro!" --write-media bordoes/lula_ta_maravilhoso.ogg

# bark
python -c "
from bark import SAMPLE_RATE, generate_audio, preload_models
preload_models()
audio = generate_audio('[happy] Tá maravilhoso, companheiro! [laughing]', history_prompt='v2/pt_speaker_3')
import scipy; scipy.io.wavfile.write('bordoes/lula_ta_maravilhoso.wav', SAMPLE_RATE, audio)
"
```

---

### 4. "A culpa e do Bolsonaro"
**ID**: `lula_culpa_bolsonaro`
**Arquivo**: `bordoes/lula_culpa_bolsonaro.ogg`
**Duracao**: 1400ms
**Trigger**: Death (ao morrer pela ultima vez, como fantasma), Hit (20% chance)
**Volume**: 0.6
**Emocao**: Indignacao automatica, reflexo de culpar o outro, raiva superficial. Dedo (4 dedos) apontando. Independente de quem atacou.
**Prioridade**: Alta -- referencia cruzada com o outro boss

**Script fonetico**:
> "A culpa é do Bolsonaro!" (dedo apontando, tom acusatorio)

**Timing interno**:
- 0-300ms: "A culpa" (rapido, como se ja estivesse pronto)
- 300-400ms: micro-pausa dramatica
- 400-1100ms: "e do Bolsonaro!" (enfatico, nome pronunciado com desprezo)
- 1100-1400ms: bufar de raiva

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "+5%" --pitch "-4Hz" --text "A culpa é do Bolsonaro!" --write-media bordoes/lula_culpa_bolsonaro.ogg

# bark
python -c "
from bark import SAMPLE_RATE, generate_audio, preload_models
preload_models()
audio = generate_audio('[angry] A culpa é do Bolsonaro! [scoff]', history_prompt='v2/pt_speaker_3')
import scipy; scipy.io.wavfile.write('bordoes/lula_culpa_bolsonaro.wav', SAMPLE_RATE, audio)
"
```

---

### 5. "Nunca antes na historia deste pais..."
**ID**: `lula_nunca_antes`
**Arquivo**: `bordoes/lula_nunca_antes.ogg`
**Duracao**: 2200ms
**Trigger**: Fato Alternativo (durante efeito), Ultimate intro, pre-attack forte (cada 30s)
**Volume**: 0.7
**Emocao**: Grandiosidade, narcisismo, tom presidencial pomposo. Fala LENTA e dramatica. Nunca completa a frase.
**Prioridade**: Media

**Script fonetico**:
> "Nunca antes na história deste país..." (lento, pomposo, como se anunciando algo epico que nunca chega)

**Timing interno**:
- 0-500ms: "Nunca antes" (tom subindo, dramatico)
- 500-600ms: pausa
- 600-1200ms: "na historia" (destaque, voz GRAVE)
- 1200-1300ms: pausa
- 1300-1900ms: "deste pais..." (voz baixando, trailing off)
- 1900-2200ms: silencio pensativo (como se fosse continuar mas nao continua)

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-20%" --pitch "-6Hz" --text "Nunca antes na história deste país..." --write-media bordoes/lula_nunca_antes.ogg
```

---

### 6. "A gente vamos..."
**ID**: `lula_a_gente_vamos`
**Arquivo**: `bordoes/lula_a_gente_vamos.ogg`
**Duracao**: 1000ms
**Trigger**: Walk (aleatorio, 10% chance ao iniciar walk), Idle
**Volume**: 0.4
**Emocao**: Casual, erro gramatical natural, sem percepcao do erro. Tom como se fosse perfeitamente normal.
**Prioridade**: Baixa (flavor audio)

**Script fonetico**:
> "A gente vamos..." (natural, como se fosse a forma correta)

**Timing interno**:
- 0-400ms: "A gente" (casual)
- 400-800ms: "vamos..." (trailing)
- 800-1000ms: silencio

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-10%" --pitch "-3Hz" --text "A gente vamos..." --write-media bordoes/lula_a_gente_vamos.ogg
```

---

### 7. "Fico puto da vida!"
**ID**: `lula_fico_puto`
**Arquivo**: `bordoes/lula_fico_puto.ogg`
**Duracao**: 1200ms
**Trigger**: Hit (50% chance), dano >20% HP, Quarto Mandato (ao morrer antes de reviver)
**Volume**: 0.7
**Emocao**: Raiva EXPLOSIVA, veia saltando, grito visceral. Tom completamente diferente do Lula calmo -- aqui ele ESTOURA.
**Prioridade**: Alta -- reacao principal de dano

**Script fonetico**:
> "FICO PUTO DA VIDA!" (GRITADO com toda a raiva)

**Timing interno**:
- 0-100ms: inspiracao rapida
- 100-400ms: "FICO" (explosivo)
- 400-700ms: "PUTO" (pico de volume, silabas separadas: PU-TO)
- 700-1000ms: "DA VIDA!" (mantendo volume alto)
- 1000-1200ms: bufar furioso

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "+15%" --pitch "-2Hz" --volume "+30%" --text "Fico puto da vida!" --write-media bordoes/lula_fico_puto.ogg

# bark -- grito de raiva
python -c "
from bark import SAMPLE_RATE, generate_audio, preload_models
preload_models()
audio = generate_audio('[scream] FICO PUTO DA VIDA! [angry]', history_prompt='v2/pt_speaker_3')
import scipy; scipy.io.wavfile.write('bordoes/lula_fico_puto.wav', SAMPLE_RATE, audio)
"
```

**Pos-processamento**:
```bash
ffmpeg -i lula_fico_puto.wav -af "compand=attacks=0.01:decays=0.3:points=-80/-80|-30/-15|-20/-10|0/0:soft-knee=6,bass=g=5:f=150" lula_fico_puto_processed.ogg
```

---

### 8. "Faz o L!"
**ID**: `lula_faz_o_l`
**Arquivo**: `bordoes/lula_faz_o_l.ogg`
**Duracao**: 800ms
**Trigger**: Empurra Mole / Faz o L (pico do ataque), Vitoria, special
**Volume**: 0.8
**Emocao**: Triunfo, provocacao, energia maxima. Comando curto e energico. Gesto iconico de campanha.
**Prioridade**: MAXIMA -- bordao mais iconico

**Script fonetico**:
> "FAZ O L!" (curto, explosivo, como grito de guerra)

**Timing interno**:
- 0-200ms: "FAZ" (staccato, agressivo)
- 200-300ms: "O" (ligacao rapida)
- 300-700ms: "ELLL!" (esticado, enfatico, L vibra)
- 700-800ms: eco

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "+20%" --pitch "-2Hz" --volume "+30%" --text "Faz o L!" --write-media bordoes/lula_faz_o_l.ogg
```

**Variante lenta (para ultimate)**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-30%" --pitch "-5Hz" --text "Faz o L... bem devagarinho..." --write-media bordoes/lula_faz_o_l_lento.ogg
```

---

### 9. "O povo brasileiro nunca comeu tanta picanha"
**ID**: `lula_picanha`
**Arquivo**: `bordoes/lula_picanha.ogg`
**Duracao**: 2400ms
**Trigger**: Idle longo (apos 15s sem combate), Fato Alternativo (20% chance), idle/special
**Volume**: 0.5
**Emocao**: Autoconfianca absurda, negacao da realidade, sorriso na voz. Tom de conquista pessoal. Orgulho delirante.
**Prioridade**: Media

**Script fonetico**:
> "O povu brasileiru nunca comeu tanta picanha!" (tom de orgulho, como se fosse merito dele)

**Timing interno**:
- 0-400ms: "O povo brasileiro" (rapido, conectado)
- 400-500ms: pausa para efeito
- 500-1000ms: "nunca comeu" (enfase em "nunca")
- 1000-1100ms: pausa
- 1100-2000ms: "tanta picanha!" (prazer na palavra "picanha", quase saboreando)
- 2000-2400ms: risinho satisfeito

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-10%" --pitch "-4Hz" --text "O povo brasileiro nunca comeu tanta picanha!" --write-media bordoes/lula_picanha.ogg
```

---

### 10. "Se o Tadala ta caro, empurra mole mesmo..."
**ID**: `lula_empurra_mole_full`
**Arquivo**: `bordoes/lula_empurra_mole_full.ogg`
**Duracao**: 4000ms (versao completa)
**Trigger**: Empurra Mole / Faz o L (audio principal, durante toda a animacao de 1200ms + sustain)
**Volume**: 0.7
**Emocao**: Duplo sentido, malicia, humor sexual, cadencia hipnotica. Cada segmento mais lento que o anterior.
**Prioridade**: MAXIMA -- meme viral, audio completo do Discord/TikTok/Reels

**Script fonetico**:
> "Se o Tadala tá caro... empurra mole mesmo... mas empurra pensando no Lula... faz o L... bem devagariiiinho..." (desacelerando progressivamente)

**Timing interno**:
- 0-800ms: "Se o Tadala ta caro..." (conversacional, introdutorio)
- 800-1000ms: pausa
- 1000-1800ms: "empurra mole mesmo..." (tom caindo, insinuante)
- 1800-2000ms: pausa
- 2000-2800ms: "mas empurra pensando no Lula..." (mais lento, malicioso)
- 2800-3000ms: pausa longa
- 3000-3400ms: "faz o L..." (sussurrado quase)
- 3400-3600ms: pausa
- 3600-4000ms: "bem devagariiiinho..." (ultra-lento, esticando o "inho")

**TTS Commands**:
```bash
# bark (RECOMENDADO -- edge-tts nao captura a malicia do tom)
python -c "
from bark import SAMPLE_RATE, generate_audio, preload_models
preload_models()
audio = generate_audio(
    '[whispering] Se o Tadala tá caro... empurra mole mesmo... [pause] mas empurra pensando no Lula... [pause] faz o L... [long pause] bem devagariiiiiinho... [laughing quietly]',
    history_prompt='v2/pt_speaker_3'
)
import scipy; scipy.io.wavfile.write('bordoes/lula_empurra_mole_full.wav', SAMPLE_RATE, audio)
"

# edge-tts (backup, menor qualidade para este bordao)
edge-tts --voice "pt-BR-AntonioNeural" --text "Empurra mole mesmo... mas empurra pensando no Lula... faz o L... bem devagarinho..." --rate "-30%" --pitch "-5Hz" --write-media bordoes/lula_empurra_mole_full.ogg
```

**Pos-processamento**:
```bash
# Desaceleracao progressiva + reverb leve + bass boost
ffmpeg -i lula_empurra_mole_full.wav -af "atempo=0.95,aecho=0.8:0.88:60:0.3,bass=g=4:f=120,lowpass=f=5000" lula_empurra_mole_full_processed.ogg
```

**URL referencia**: Audio viral do Discord/TikTok/Reels -- referencia ao Tadalafila (generico Viagra/Cialis). Meme "Lula 26:13" (referencia biblica fake). Edits com Homem-Aranha e anime.
**Notas**: Este e o bordao mais importante do Lula. A versao do jogo deve ser RECONHECIVEL como o meme mas com o tom do Andre Guedes (mais grotesco, exagerado). O audio deve ser ASMR-level de sussurro. Easter egg: 10% chance de tocar versao completa do audio viral.

---

### 11. "Mas eu acabei de ser reeleito, companheiro!"
**ID**: `lula_reeleito`
**Arquivo**: `bordoes/lula_reeleito.ogg`
**Duracao**: 2000ms
**Trigger**: Quarto Mandato (ressurreicao, frames 5-6)
**Volume**: 0.6
**Emocao**: Indignacao comica, incredulidade de quem nao aceita a derrota. A morte e uma afronta pessoal.
**Prioridade**: Alta -- vinculado a mecanica core de ressurreicao

**Script fonetico**:
> "Mas eu acabei de ser reeleito, companhêiru!" (indignado)

**Timing interno**:
- 0-200ms: "Mas eu" (rapido, protestando)
- 200-800ms: "acabei de ser reeleito" (enfatico, como prova juridica)
- 800-900ms: pausa de indignacao
- 900-1700ms: "companheiro!" (gritado, frustrado)
- 1700-2000ms: bufar

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "+5%" --pitch "-3Hz" --text "Mas eu acabei de ser reeleito, companheiro!" --write-media bordoes/lula_reeleito.ogg
```

---

### 12. "Essa cicatriz e do povo, companheiro"
**ID**: `lula_cicatriz_povo`
**Arquivo**: `bordoes/lula_cicatriz_povo.ogg`
**Duracao**: 2000ms
**Trigger**: Hit (headshot, quando dano e reduzido pela placa de titanio)
**Volume**: 0.5
**Emocao**: Orgulho perverso, transformando fraqueza em virtude, malandro. Sorriso na voz. Como se fosse uma medalha.
**Prioridade**: Media -- vinculado a mecanica de Cirurgia Craniana

**Script fonetico**:
> "Essa cicatriz é do povo, companhêiru..." (sorrindo)

**Timing interno**:
- 0-500ms: "Essa cicatriz" (tocando a cabeca)
- 500-600ms: pausa
- 600-1200ms: "e do povo" (tom subindo, orgulhoso)
- 1200-1300ms: pausa
- 1300-1800ms: "companheiro..." (suavizando, trailing)
- 1800-2000ms: risinho de malandro

**TTS Commands**:
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-10%" --pitch "-4Hz" --text "Essa cicatriz é do povo, companheiro..." --write-media bordoes/lula_cicatriz_povo.ogg
```

---

## BORDOES SECUNDARIOS (Flavor/Ambientacao)

### 13. "Eu nao sei explicar, mas..."
**ID**: `lula_nao_sei`
**Arquivo**: `bordoes/lula_nao_sei.ogg`
**Duracao**: 1400ms
**Trigger**: Idle longo aleatorio (cada 40s)
**Volume**: 0.3
**Emocao**: Confusao alcoolica, honestidade acidental. Tom honesto seguido de silencio. Depois continua como se nada.
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-15%" --pitch "-5Hz" --text "Eu não sei explicar, mas..." --write-media bordoes/lula_nao_sei.ogg
```

### 14. "Nos vamos fazer o que? Nos vamos fazer!"
**ID**: `lula_circularidade`
**Arquivo**: `bordoes/lula_circularidade.ogg`
**Duracao**: 2000ms
**Trigger**: Walk (aleatorio, 5% chance), Fato Alternativo
**Volume**: 0.4
**Emocao**: Circularidade logica, confianca sem substancia
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "+5%" --pitch "-3Hz" --text "Nós vamos fazer o quê? Nós vamos fazer!" --write-media bordoes/lula_circularidade.ogg
```

### 15. "Eu vou lhe dizer uma coisa..."
**ID**: `lula_vou_dizer`
**Arquivo**: `bordoes/lula_vou_dizer.ogg`
**Duracao**: 1600ms
**Trigger**: Antes de ataque (15% chance), idle (cada 20s)
**Volume**: 0.5
**Emocao**: Ameaca velada em tom paternalista. NUNCA diz a "coisa".
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-10%" --pitch "-4Hz" --text "Eu vou lhe dizer uma coisa..." --write-media bordoes/lula_vou_dizer.ogg
```

### 16. "Pelotas e polo exportador de que?"
**ID**: `lula_pelotas`
**Arquivo**: `bordoes/lula_pelotas.ogg`
**Duracao**: 1800ms
**Trigger**: Easter egg (0.5% chance no idle, referencia a gafe real)
**Volume**: 0.4
**Emocao**: Curiosidade genuina seguida de constrangimento
```bash
edge-tts --voice "pt-BR-AntonioNeural" --rate "-5%" --pitch "-3Hz" --text "Pelotas é polo exportador de quê?" --write-media bordoes/lula_pelotas.ogg
```

---

## AUDIO DO ULTIMATE: "Discurso de Hora e Meia"

### Discurso Loop Principal
**ID**: `lula_discurso_loop`
**Arquivo**: `bordoes/lula_discurso_loop.ogg`
**Duracao**: 8000ms (loop seamless)
**Trigger**: Ultimate ativo (durante os 8 segundos em que todos estao parados)
**Volume**: 0.7 (domina o soundscape)
**Emocao**: Grandiosidade crescente, paixao sem conteudo, hipnose verbal, loop infinito. Palanque total.

**Script completo (8 segundos -- NUNCA CHEGA AO PONTO)**:
> "Eu quero dizer pra voces... olha... eu quero dizer... eu quero dizer uma coisa... esse pais... voces nao sabem o que... nunca antes... olha... eu quero dizer... companheiros... olha... eu quero dizer pra voces uma coisa... uma coisa que... olha..."

**Timing interno**:
- 0-800ms: "Eu quero dizer pra voces..." (padrao, abertura)
- 800-1200ms: "olha..." (pausa com interjeicao)
- 1200-2000ms: "eu quero dizer..." (repete, NUNCA chega ao ponto)
- 2000-2800ms: "eu quero dizer uma coisa..." (adiciona "uma coisa" para parecer que vai chegar la)
- 2800-3600ms: "esse pais..." (muda de assunto no meio)
- 3600-4200ms: "voces nao sabem o que..." (frase incompleta)
- 4200-5000ms: "nunca antes..." (cita o classico mas nao termina)
- 5000-5400ms: "olha..." (outra interjeicao)
- 5400-6200ms: "eu quero dizer..." (DE NOVO, loop linguistico)
- 6200-6600ms: "companheiros..." (pausa para respirar)
- 6600-7000ms: "olha..." (MAIS UMA VEZ)
- 7000-7600ms: "eu quero dizer pra voces uma coisa..." (reinicia o ciclo)
- 7600-8000ms: "uma coisa que... olha..." (fade para loop seamless)

**Nota**: O ponto do discurso e que NUNCA CHEGA AO PONTO. E uma obra-prima de enrolacao. O jogador deve sentir que Lula poderia falar para sempre sem dizer nada. Todos param para ouvir. Score continua rodando. Lula se cura enquanto discursa.

**TTS Commands**:
```bash
# Gerar em partes e concatenar
# Parte 1
edge-tts --voice "pt-BR-AntonioNeural" --rate "-20%" --pitch "-5Hz" --text "Eu quero dizer pra vocês... olha... eu quero dizer... eu quero dizer uma coisa..." --write-media bordoes/lula_discurso_p1.ogg

# Parte 2
edge-tts --voice "pt-BR-AntonioNeural" --rate "-15%" --pitch "-5Hz" --text "esse país... vocês não sabem o quê... nunca antes... olha..." --write-media bordoes/lula_discurso_p2.ogg

# Parte 3
edge-tts --voice "pt-BR-AntonioNeural" --rate "-20%" --pitch "-5Hz" --text "eu quero dizer... companheiros... olha... eu quero dizer pra vocês uma coisa... uma coisa que... olha..." --write-media bordoes/lula_discurso_p3.ogg

# Concatenar
ffmpeg -i "concat:bordoes/lula_discurso_p1.ogg|bordoes/lula_discurso_p2.ogg|bordoes/lula_discurso_p3.ogg" -c copy bordoes/lula_discurso_loop.ogg

# BARK (recomendado para naturalidade):
python -c "
from bark import SAMPLE_RATE, generate_audio, preload_models
preload_models()
audio = generate_audio(
    '[speaking slowly] Eu quero dizer pra vocês... [pause] olha... eu quero dizer... [pause] eu quero dizer uma coisa... [pause] esse país... vocês não sabem o quê... [pause] nunca antes... olha... eu quero dizer... [pause] companheiros... olha...',
    history_prompt='v2/pt_speaker_3'
)
import scipy; scipy.io.wavfile.write('bordoes/lula_discurso_loop.wav', SAMPLE_RATE, audio)
"
```

**Pos-processamento**:
```bash
# Reverb de palanque + echo leve + loop crossfade
ffmpeg -i lula_discurso_loop.wav -af "aecho=0.8:0.9:100:0.3,areverse,aecho=0.8:0.9:100:0.3,areverse,highpass=f=60,lowpass=f=8000" -t 8 lula_discurso_loop_processed.ogg
```

---

## TABELA RESUMO DE TODOS OS BORDOES

| # | ID | Frase (resumida) | Duracao | Trigger | Volume | Prioridade |
|---|-----|-------------------|---------|---------|--------|------------|
| 1 | lula_eu_quero_dizer | "Eu quero dizer pra voces..." | 1800ms | Idle 5-8s, Fato Alt | 0.6 | MAX |
| 2 | lula_companheiro_alcool | "Companheiro alcool em mim!" | 1500ms | Attack 30%, Spawn | 0.7 | Alta |
| 3 | lula_ta_maravilhoso | "Ta maravilhoso, companheiro!" | 1600ms | Idle 20s, Resurreicao | 0.5 | Media |
| 4 | lula_culpa_bolsonaro | "A culpa e do Bolsonaro" | 1400ms | Death final, Hit 20% | 0.6 | Alta |
| 5 | lula_nunca_antes | "Nunca antes na historia..." | 2200ms | Fato Alt, Ultimate | 0.7 | Media |
| 6 | lula_a_gente_vamos | "A gente vamos..." | 1000ms | Walk 10% | 0.4 | Baixa |
| 7 | lula_fico_puto | "Fico puto da vida!" | 1200ms | Hit 50%, dano >20% HP | 0.7 | Alta |
| 8 | lula_faz_o_l | "Faz o L!" | 800ms | Faz o L pico, Vitoria | 0.8 | MAX |
| 9 | lula_picanha | "...nunca comeu tanta picanha" | 2400ms | Idle 15s+, Fato Alt 20% | 0.5 | Media |
| 10 | lula_empurra_mole_full | "Se o Tadala ta caro..." | 4000ms | Empurra Mole (full) | 0.7 | MAX |
| 11 | lula_reeleito | "Acabei de ser reeleito!" | 2000ms | Quarto Mandato | 0.6 | Alta |
| 12 | lula_cicatriz_povo | "Essa cicatriz e do povo" | 2000ms | Headshot block | 0.5 | Media |
| 13 | lula_nao_sei | "Eu nao sei explicar, mas..." | 1400ms | Idle aleatorio 40s | 0.3 | Baixa |
| 14 | lula_circularidade | "Nos vamos fazer o que?..." | 2000ms | Walk 5%, Fato Alt | 0.4 | Baixa |
| 15 | lula_vou_dizer | "Eu vou lhe dizer uma coisa..." | 1600ms | Pre-attack 15%, idle 20s | 0.5 | Baixa |
| 16 | lula_pelotas | "Pelotas e polo exportador..." | 1800ms | Easter egg 0.5% | 0.4 | Easter Egg |
| 17 | lula_discurso_loop | Discurso de 8s sem ponto | 8000ms | Ultimate | 0.7 | MAX |

**Total**: 17 arquivos de audio de bordoes

---

## VARIANTES DE INTENSIDADE

| Bordao | Sussurro (vol 0.3) | Normal (vol 0.6) | Grito (vol 0.9) |
|--------|---------------------|-------------------|-------------------|
| "Eu quero dizer pra voces..." | idle longo | idle normal | pre-attack |
| "Companheiro alcool em mim!" | -- | spawn | -- |
| "Faz o L!" | ultimate (devagarinho) | attack | special |
| "Fico puto da vida!" | -- | -- | low_hp ONLY |
| "Empurra mole..." | ASMR sussurro | normal | -- |

---

## SISTEMA DE PRIORIDADE DE AUDIO

Para evitar cacofonia, implementar fila de prioridade:
1. **MAX** (interrompe tudo): Ultimate, Faz o L, Empurra Mole, "Eu quero dizer"
2. **Alta** (interrompe Media/Baixa): Attack, Death, Hit (Fico Puto), Resurreicao
3. **Media** (interrompe Baixa): Fato Alternativo, Headshot block, Picanha, Idle longo
4. **Baixa** (so toca se nada mais tocando): Walk murmurs, Idle curto
5. **Easter Egg** (mesma prioridade de Baixa): Pelotas, etc.

### Regras de Fila
- Maximo 1 bordao tocando por vez
- Cooldown minimo entre bordoes: 2000ms (exceto Hit que e imediato)
- Se bordao de Alta tenta tocar durante MAX, e enfileirado (toca depois se ainda relevante)
- SFX (garrafa, passo, impacto) tocam em canal separado -- nao interferem com bordoes

---

## REFERENCIAS DE AUDIO ORIGINAL
- Compilacoes de discursos do Lula: YouTube "Lula melhores momentos discurso"
- Meme "empurra mole": TikTok/Discord viral -- "Lula 26:13"
- Andre Guedes: Episodios 1-10 de Zumbis em Brasilia (2018, 2022, 2026) -- YouTube
- "Faz o L": Videos de campanha 2022
- Gafes: "Pelotas e polo exportador de que?" -- YouTube compilacoes

---

## PIPELINE DE PRODUCAO RECOMENDADO

### Opcao A: TTS + Pos-Processamento (Rapido, Custo Zero)
1. Gerar com `edge-tts` (voice: `pt-BR-AntonioNeural`)
2. Processar com `ffmpeg` (pitch down, reverb, distorcao)
3. Ajustar manualmente timing no Audacity se necessario
4. Exportar como OGG Vorbis, mono, 44100Hz

### Opcao B: Bark AI (Melhor Qualidade, Mais Lento)
1. Instalar Bark: `pip install git+https://github.com/suno-ai/bark.git`
2. Usar `v2/pt_speaker_3` como voice preset (grave, masculino)
3. Adicionar tags de emocao: `[laughing]`, `[angry]`, `[whispering]`, `[pause]`
4. Gerar WAV, processar com ffmpeg, converter para OGG

### Opcao C: Gravacao Profissional (Melhor Resultado, Custo)
1. Contratar ator de voz brasileiro (imitador de politicos)
2. Script completo acima como guia
3. Gravacao em estudio, sessao de 4h
4. Pos-producao: limpar, normalizar, exportar

### Opcao D: Hibrida (RECOMENDADA)
1. TTS para prototipo rapido (opcao A) -- MVP
2. Bark para bordoes MAX priority (opcao B) -- Alpha
3. Gravacao profissional para versao final de lancamento (opcao C) -- Release
4. Cada fase substitui a anterior, assets sao drop-in replacement (mesmo ID, mesmo filename)
