# ALCKMIN (O Vice / O Mordomo) -- Bordoes de Audio

**Voz**: Suave, educada, levemente nasal. Sotaque paulista refinado. Tom geral: mordomo britanico versao brasileira. Voz que pede desculpas por existir. Fala mansa, quase sussurrada, como quem nao quer incomodar. Entonacao de quem aceita qualquer humilhacao com um sorriso.
**TTS Voice**: `pt-BR-AntonioNeural` -- ajustar pitch -1Hz para voz mais suave, rate -5% para tom calmo/subserviente
**Alternativa**: Voice actor com voz mansa, educada, sotaque paulista, tom de mordomo resignado

---

### 1. "Eu adoro esse nome, alcool em mim!"
- **Trigger**: spawn / inicio de episodio / primeiro encontro com qualquer personagem
- **Emocao**: Alegria subserviente, auto-depreciacam aceita, risadinha no final
- **Volume**: 6/10
- **Duracao**: 2.0s
- **Frequencia**: OBRIGATORIO em TODOS os episodios/encontros. Primeira fala do Alckmin SEMPRE.
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu adoro esse nome, alcool em mim!" --rate "-5%" --pitch "-1Hz" --write-media alckmin-01-alcool.mp3`
- **Efeitos de pos-producao**: Tom alegre mas subserviente, risadinha sutil no final (0.5s, "hehehe" abafado), entonacao de quem aceita a piada com prazer
- **URL referencia**: Trocadilho classico "Alckmin = alcool em mim" -- piada recorrente
- **REGRA ESPECIAL**: Este bordao DEVE tocar em TODOS os episodios e encontros. E a assinatura sonora do Alckmin. Se o episodio comeca sem esse bordao, e um BUG.
- **Notas**: O Alckmin GOSTA do trocadilho. Nao e constrangimento -- e aceitacao total. Risadinha de quem acha genuinamente engracado ser chamado de "alcool em mim".

### 2. "Companheiro Lula, eu resolvo!"
- **Trigger**: ally_buff / quando Lula (se presente) pede algo / pre-ataque servical
- **Emocao**: Servicalismo rapido, eficiencia de mordomo, tom de "deixa comigo chefe"
- **Volume**: 6/10
- **Duracao**: 1.5s
- **Frequencia**: Quando Lula esta no mapa e faz qualquer acao / ao receber ordem de grupo
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Companheiro Lula, eu resolvo!" --rate "+5%" --pitch "-1Hz" --write-media alckmin-02-resolvo.mp3`
- **Efeitos de pos-producao**: Tom servical, rapido, eficiente. Voz de quem ja esta se mexendo antes de terminar a frase.
- **URL referencia**: Relacao Lula-Alckmin no governo -- vice que resolve bastidores
- **Notas**: Dito com VELOCIDADE -- Alckmin ja esta agindo antes de terminar de falar. Servicalismo como superpoder. Se Lula nao esta no mapa, diz para o vazio (habito).

### 3. "Quer que eu passe o cafe?"
- **Trigger**: idle / interact_npc / momento de calma entre waves
- **Emocao**: Mordomo absoluto, hospitalidade extrema, oferece cafe ate durante apocalipse
- **Volume**: 5/10
- **Duracao**: 1.2s
- **Frequencia**: Cada 25s em idle / ao encontrar qualquer personagem
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Quer que eu passe o cafe?" --rate "-5%" --pitch "-1Hz" --write-media alckmin-03-cafe.mp3`
- **Efeitos de pos-producao**: Tom de mordomo perfeito, voz suave, entonacao de pergunta gentil (ascendente no final)
- **Notas**: Em pleno apocalipse zumbi, Alckmin oferece cafe. Prioridades: hospitalidade > sobrevivencia. Tom de quem genuinamente acha que cafe resolve qualquer crise.

### 4. "Eu estava governando esse tempo todo... alguem notou?"
- **Trigger**: idle longo (10s+) / quando ignorado por aliados / entre episodios
- **Emocao**: Melancolia existencial, invisibilidade aceita, pausa dramatica antes de "alguem notou?"
- **Volume**: 5/10
- **Duracao**: 3.0s
- **Frequencia**: Cada 45s em idle longo / quando nenhum aliado interage com ele por 15s+
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu estava governando esse tempo todo... alguem notou?" --rate "-10%" --pitch "-2Hz" --write-media alckmin-04-governando.mp3`
- **Efeitos de pos-producao**: Tom melancolico, PAUSA DRAMATICA de 0.8s antes de "alguem notou?". "Alguem notou?" quase sussurrado, com leve crack vocal de tristeza contida.
- **URL referencia**: Alckmin como vice invisivel -- memes sobre ele governar sem ninguem perceber
- **Notas**: O bordao mais TRISTE do jogo. Alckmin governou durante viagens do Lula e NINGUEM notou. A pausa antes de "alguem notou?" e essencial -- e o momento de duvida existencial. Resposta do jogo: silencio total. Nenhum NPC responde.

### 5. "Mais alguma coisa, presidente? Cafe? Pastel? Minha dignidade?"
- **Trigger**: idle / interact_lula / pos-buff de aliado / situacao de humilhacao
- **Emocao**: Resignacao crescente, lista de ofertas que escala de normal a tragico. "Dignidade" quase sussurrado.
- **Volume**: 5/10
- **Duracao**: 3.5s
- **Frequencia**: Cada 40s em idle / apos interagir com Lula (se presente)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Mais alguma coisa, presidente? Cafe? Pastel? Minha dignidade?" --rate "-5%" --pitch "-1Hz" --write-media alckmin-05-dignidade.mp3`
- **Efeitos de pos-producao**:
  - "Mais alguma coisa, presidente?" -- tom normal de mordomo (vol 5/10)
  - "Cafe?" -- tom de oferta padrao (vol 5/10)
  - "Pastel?" -- tom ligeiramente mais baixo (vol 4/10)
  - "Minha dignidade?" -- QUASE SUSSURRO (vol 2/10), tom de resignacao total, leve tremor na voz
  - Crescente de resignacao ao longo da frase. A voz vai diminuindo ate quase sumir em "dignidade".
- **URL referencia**: Memes sobre Alckmin servindo cafe para Lula no Planalto
- **Notas**: O bordao mais TRAGICO-COMICO do Alckmin. A lista de ofertas escala de hospitalidade normal (cafe) para absurdo (pastel em apocalipse) para tragedia existencial (dignidade). "Minha dignidade?" deve ser quase inaudivel -- o jogador precisa prestar atencao para ouvir.

---

## Variantes de Intensidade

| Bordao | Tom Normal | Tom Melancolico (idle longo) |
|--------|-----------|------------------------------|
| "Alcool em mim!" | vol 6, alegre, risadinha | vol 4, risadinha mais fraca, sorriso triste |
| "Eu resolvo!" | vol 6, eficiente | vol 5, "eu resolvo... como sempre..." |
| "Quer cafe?" | vol 5, hospitalidade | vol 3, sussurro para si mesmo |
| "Alguem notou?" | vol 5, melancolico | vol 2, quase inaudivel, para si mesmo |
| "Minha dignidade?" | vol 5->2 (decrescente) | vol 3->1, voz quebrando |

## Regras de Frequencia (Alckmin-Especificas)

1. **"Alcool em mim!"** e OBRIGATORIO em todo episodio/encontro -- NUNCA pode faltar
2. Se Lula esta no mapa, frequencia de bordoes SERVIC AIS triplica
3. **"Alguem notou?"** so toca em idle LONGO (10s+) -- e recompensa por observar o Alckmin parado
4. **"Minha dignidade?"** tem volume DECRESCENTE -- o jogador precisa prestar atencao
5. Alckmin e o personagem mais SILENCIOSO do elenco -- poucos bordoes, baixo volume, facil de ignorar (meta-comentario sobre sua invisibilidade politica)

## Efeitos Sonoros Contextuais
- **Som de xicrinha de cafe**: SFX sutil que acompanha QUALQUER fala do Alckmin (identidade sonora)
- **Silencio**: Apos "alguem notou?", 3s de silencio absoluto antes de qualquer outro audio
- **Suspiro resignado**: SFX de 0.3s que acompanha "minha dignidade?" -- suspiro longo

## Referencias de Audio Original
- Entrevistas do Alckmin -- tom educado, voz mansa
- Memes "Alckmin mordomo" -- compilacoes
- Relacao Lula-Alckmin no governo federal
- Trocadilho "alcool em mim" -- recorrente em humor politico
- Andre Guedes: Serie "Zumbis em Brasilia"
