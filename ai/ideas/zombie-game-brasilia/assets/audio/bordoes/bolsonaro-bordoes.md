# BOLSONARO (O Mito / Jair) -- Bordoes de Audio

**Voz**: Media-grave, nasalada, cadencia militar staccato. Fala rapida em rajadas curtas seguidas de pausa. Tom de quem esta dando uma ordem mas nao tem certeza se alguem vai obedecer. Sotaque carioca-militar (influencia da caserna, nao da praia). Frequente pigarro entre frases. Em 2026 (skin Preso): voz ABAFADA como se falasse de dentro de cela com celular escondido.
**TTS Voice**: `pt-BR-AntonioNeural` (grave, masculina) -- ajustar rate +10% para fala rapida e staccato, pitch +1Hz (nasalidade)
**Alternativa**: Gravar com voice actor imitando a cadencia militar curta, nasalada, com "talkei" grudado no final de tudo
**Nota**: O "TALKEI?" e quase uma palavra so -- pronunciado rapid-fire, grudado na frase anterior, quase como um tique nervoso

---

### 1. "TALKEI?"
- **Trigger**: idle (toca quando o personagem fica parado por 3s+) / sufixo grudavel em qualquer outro bordao
- **Emocao**: Pergunta retorica que nao espera resposta. Tom de quem acabou de dar uma ordem. Afirmacao disfarçada de pergunta.
- **Volume**: 5/10
- **Duracao**: 0.4s
- **Frequencia**: Cada 8s em idle / apos qualquer outra fala (pode ser GRUDADO no final de outros bordoes)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Talkei?" --rate "+20%" --pitch "+2Hz" --write-media bolsonaro-01-talkei.mp3`
- **Bark/XTTS**: `bark --text "Talkei?" --speaker "v2/pt_speaker_3" --output bolsonaro-01-talkei.wav`
- **URL referencia**: Compilacoes "talkei bolsonaro" no YouTube -- centenas de instancias
- **Notas**: O bordao DEFINITIVO. Quase uma assinatura sonora. Deve ser pronunciado como uma unica silaba rapida: "TALKEI" (nao "ta ok"). Pode ser adicionado ao FINAL de qualquer outro bordao como sufixo. Variantes de intensidade: sussurrado (pos-derrota), normal (idle), gritado (pos-ataque).

### 2. "Bomba!"
- **Trigger**: attack_success / spawn de wave forte
- **Emocao**: Exclamacao de surpresa-entusiasmo. Como se ele mesmo ficasse surpreso que deu certo. Energia de quem ta compartilhando um furo.
- **Volume**: 8/10
- **Duracao**: 0.6s
- **Frequencia**: 40% de chance em attack_success
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "BOMBA!" --rate "+15%" --pitch "+3Hz" --write-media bolsonaro-02-bomba.mp3`
- **Bark/XTTS**: `bark --text "BOMBA!" --speaker "v2/pt_speaker_3" --output bolsonaro-02-bomba.wav`
- **URL referencia**: Lives do Bolsonaro -- "bomba" como catchphrase para revelaçoes
- **Notas**: Grito curto e explosivo. A boca faz um "B" exagerado (labios projetados). O "A" final e aberto e alto. Usar como punctuation sonora em momentos de impacto.

### 3. "Vagabundo! Canalha!"
- **Trigger**: attack / pre-attack / hit (ao levar dano)
- **Emocao**: Raiva pura, descontrolada. Xingamento military-style. Cuspindo as palavras.
- **Volume**: 9/10
- **Duracao**: 1.5s
- **Frequencia**: 30% de chance em attack ou hit
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Vagabundo! Canalha!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-03-vagabundo.mp3`
- **Bark/XTTS**: `bark --text "Vagabundo! Canalha!" --speaker "v2/pt_speaker_3" --output bolsonaro-03-vagabundo.wav`
- **URL referencia**: Entrevistas e lives onde Bolsonaro xinga adversarios
- **Notas**: Cada palavra e uma punhalada sonora. Pausa de 0.2s entre "Vagabundo!" e "Canalha!". Cuspe (literalmente) pode ser um efeito sonoro adicional (pequeno "pft" umido). Veias saltando no pescoco.

### 4. "Minha arma e brochavel!"
- **Trigger**: attack_fail (quando a arma falha -- 30% chance)
- **Emocao**: Frustacao envergonhada, tentando fazer piada pra disfarcar a humilhacao. Tom de stand-up que ri da propria desgraca.
- **Volume**: 7/10
- **Duracao**: 1.8s
- **Frequencia**: 50% de chance quando attack_fail ocorre (o outro 50% e "talkei?" triste)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Minha arma é brochável!" --rate "+5%" --pitch "+1Hz" --write-media bolsonaro-04-brochavel.mp3`
- **Bark/XTTS**: `bark --text "Minha arma é brochável!" --speaker "v2/pt_speaker_3" --output bolsonaro-04-brochavel.wav`
- **URL referencia**: Versao Andre Guedes da piada -- adaptacao do "imbrochavel" invertido
- **Notas**: Referencia direta ao Andre Guedes. O tom oscila entre frustacao e auto-depreciacão. A enfase esta em "bro-CHA-vel" -- a silaba do meio e mais longa e mais alta. Riso nervoso pode seguir (0.5s de risada forcada).

### 5. "A culpa e do Lula! / STF! / Globo! / urnas!"
- **Trigger**: hit (ao levar dano) / death (durante queda)
- **Emocao**: Deflecao automatica de culpa. Tom acusatorio, dedo apontado. Nao importa o que aconteceu, a culpa NUNCA e dele.
- **Volume**: 8/10
- **Duracao**: 1.5s
- **Frequencia**: 25% de chance ao levar dano (variante aleatoria: Lula / STF / Globo / urnas)
- **TTS Command (variante Lula)**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa é do Lula!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-05a-culpa-lula.mp3`
- **TTS Command (variante STF)**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa é do STF!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-05b-culpa-stf.mp3`
- **TTS Command (variante Globo)**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa é da Globo!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-05c-culpa-globo.mp3`
- **TTS Command (variante urnas)**: `edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa é das urnas!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-05d-culpa-urnas.mp3`
- **URL referencia**: Memes "a culpa e do..." -- acusacao universal
- **Notas**: 4 variantes que tocam ALEATORIAMENTE. Mesmo trigger, alvo diferente. O dedo aponta para o inimigo que atacou, independente de quem seja. A ironia e que o inimigo pode ser um zumbi-vereador e ele culpa o Lula. Variante "urnas" e especificamente priorizada para a skin de Preso.

### 6. "E dai? Lamento. Quer que eu faca o que?"
- **Trigger**: hit (dano pesado) / low_hp (abaixo de 30%)
- **Emocao**: Descaso absoluto. Indiferenca gelida. O tom mais frio e mais calculado de todos os bordoes. Zero empatia.
- **Volume**: 6/10 (deliberadamente MAIS BAIXO que os gritos -- o descaso e mais assustador que a raiva)
- **Duracao**: 3.0s
- **Frequencia**: Rara -- 15% de chance em hit grave, ou uma vez ao atingir 30% HP
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "E daí? Lamento. Quer que eu faça o quê?" --rate "-5%" --pitch "-1Hz" --write-media bolsonaro-06-edai.mp3`
- **Bark/XTTS**: `bark --text "E daí? Lamento. Quer que eu faça o quê?" --speaker "v2/pt_speaker_3" --output bolsonaro-06-edai.wav`
- **URL referencia**: Entrevista real, abril 2020 -- frase que definiu a resposta a pandemia
- **Notas**: Frase REAL dita sobre mortes da COVID. No jogo, e dita ao levar dano -- a mesma indiferença aplicada a propria saude. Pausas entre cada parte: "E dai?" [0.3s] "Lamento." [0.3s] "Quer que eu faca o que?" O "lamento" deve soar como o oposto de lamento -- zero sentimento.

### 7. "Nao sou coveiro!"
- **Trigger**: death (durante animacao de morte) / low_hp
- **Emocao**: Defensividade agressiva. Recusa de responsabilidade. Quase um grito de guerra inverso.
- **Volume**: 8/10
- **Duracao**: 1.2s
- **Frequencia**: 50% de chance ao morrer (alternando com "E dai?")
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Não sou coveiro!" --rate "+15%" --pitch "+3Hz" --write-media bolsonaro-07-coveiro.mp3`
- **Bark/XTTS**: `bark --text "Não sou coveiro!" --speaker "v2/pt_speaker_3" --output bolsonaro-07-coveiro.wav`
- **URL referencia**: Frase real de 2020 sobre os numeros de mortes
- **Notas**: Ironia maxima: dito ENQUANTO morre. A frase sobre nao ser responsavel pela morte dos outros, dita durante a PROPRIA morte. Humor negro puro. Tom agressivo, curto, cortante.

### 8. "E so uma gripezinha!"
- **Trigger**: hit (dano leve) / idle (raro)
- **Emocao**: Minimizacao. Negacao da realidade. Tom de quem acha que e mais forte que qualquer problema.
- **Volume**: 6/10
- **Duracao**: 1.5s
- **Frequencia**: 20% de chance em hit leve / Rara em idle (cada 30s)
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "É só uma gripezinha!" --rate "+5%" --pitch "+2Hz" --write-media bolsonaro-08-gripezinha.mp3`
- **Bark/XTTS**: `bark --text "É só uma gripezinha!" --speaker "v2/pt_speaker_3" --output bolsonaro-08-gripezinha.wav`
- **URL referencia**: Frase infame de marco 2020 sobre a COVID-19
- **Notas**: Dito ao levar dano como forma de minimizar. O diminutivo "-inha" deve ser enfatizado e alongado: "gripe-ZI-nha". Tom de descaso misturado com bravata. Pode ter uma risada curta no final (0.3s, forçada).

### 9. "Pintou um clima..."
- **Trigger**: special (skill "Pintou um Clima")
- **Emocao**: Tom inapropriadamente intimo, sussurrado, smarmy. O bordao mais DESCONFORTAVEL de todos. A voz baixa e deliberada.
- **Volume**: 5/10 (sussurro deliberado -- ASMR do cringe)
- **Duracao**: 2.0s
- **Frequencia**: Unica -- ao ativar a skill especifica
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Pintou um clima..." --rate "-20%" --pitch "-3Hz" --write-media bolsonaro-09-pintou.mp3`
- **Bark/XTTS**: `bark --text "Pintou um clima..." --speaker "v2/pt_speaker_3" --output bolsonaro-09-pintou.wav`
- **URL referencia**: Frase controversa que gerou enorme repercussao
- **Notas**: SUSSURRO. O oposto dos outros bordoes. Enquanto todos sao gritados, este e baixo, lento, deliberado. O "..." no final e um silencio que PESA. A voz deve fazer o jogador fisicamente desconfortavel. Rate reduzido (-20%) para fala lenta. Pitch reduzido para tom mais grave e intimo.

### 10. "Eu sou Messias, mas nao faco milagre"
- **Trigger**: special (Invulnerabilidade deactivation / fail)
- **Emocao**: Auto-ironia involuntaria. Ele acha que ta sendo humilde, mas esta literalmente se comparando ao Messias. Tom de falsa humildade que mal esconde o ego.
- **Volume**: 7/10
- **Duracao**: 2.5s
- **Frequencia**: 100% ao terminar invulnerabilidade / rara em idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu sou Messias, mas não faço milagre" --rate "-5%" --pitch "+1Hz" --write-media bolsonaro-10-messias.mp3`
- **Bark/XTTS**: `bark --text "Eu sou Messias, mas não faço milagre" --speaker "v2/pt_speaker_3" --output bolsonaro-10-messias.wav`
- **URL referencia**: Frase real -- referencia ao nome do meio "Messias"
- **Notas**: O nome do meio dele e literalmente "Messias". A frase funciona em dois niveis: referencia biblica e referencia ao proprio nome. O tom e de quem realmente acha que e quase divino mas "humildemente" admite limitacoes. Pausa antes de "mas" para efeito dramatico.

### 11. "Brasil acima de tudo, Deus acima de todos!"
- **Trigger**: spawn / inicio de boss fight / ultimate charge
- **Emocao**: Slogan de campanha. Tom de comicio. Maximo volume, maximo entusiasmo artificial. Como um jingle politico incarnado em frase.
- **Volume**: 10/10 (MAXIMO)
- **Duracao**: 3.0s
- **Frequencia**: Uma vez ao spawnar. Uma vez ao ativar ultimate.
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Brasil acima de tudo! Deus acima de todos!" --rate "+5%" --pitch "+3Hz" --write-media bolsonaro-11-slogan.mp3`
- **Bark/XTTS**: `bark --text "Brasil acima de tudo! Deus acima de todos!" --speaker "v2/pt_speaker_3" --output bolsonaro-11-slogan.wav`
- **URL referencia**: Slogan oficial de campanha 2018/2022
- **Notas**: A entrada do boss. O equivalente sonoro de um rugido de leao, mas de um politico. Pausa de 0.3s entre as duas frases. A segunda parte ("Deus acima de todos") sobe em pitch -- como um crescendo de comicio. Pode ter eco/reverb para efeito dramatico de arena.

### 12. "Eu sou imorrivel, imbrochavel e incomivel!"
- **Trigger**: special (skill "Imorrivel, Imbrochavel, Incomivel" -- ativacao)
- **Emocao**: Auto-glorificacao maxima. Convicao absoluta. Os tres adjetivos inventados ditos como se fossem fato cientifico comprovado.
- **Volume**: 9/10
- **Duracao**: 3.5s
- **Frequencia**: Unica -- ao ativar a skill
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu sou imorrível! Imbrochável! E incomível!" --rate "+5%" --pitch "+2Hz" --write-media bolsonaro-12-imorrivel.mp3`
- **Bark/XTTS**: `bark --text "Eu sou imorrível! Imbrochável! E incomível!" --speaker "v2/pt_speaker_3" --output bolsonaro-12-imorrivel.wav`
- **URL referencia**: Frase real dita em entrevista/live -- viralizou
- **Notas**: Cada adjetivo e separado por uma pausa dramatica de 0.5s. Cada um e mais alto que o anterior (crescendo). "IMORRIVEL!" (8/10) -> "IMBROCHAVEL!" (9/10) -> "E INCOMIVEL!" (10/10, pico). O "e" antes de "incomivel" e importante -- e o "e" de lista que culmina. As palavras sao inventadas e devem soar como se fossem a coisa mais natural do mundo.

### 13. "Pais de maricas!"
- **Trigger**: idle (raro) / ao ver inimigos fugindo
- **Emocao**: Desprezo machista. Tom de superior moral auto-proclamado. Olhar de cima pra baixo.
- **Volume**: 7/10
- **Duracao**: 1.2s
- **Frequencia**: Rara -- cada 45s em idle / 30% quando inimigos fogem
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "País de maricas!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-13-maricas.mp3`
- **Bark/XTTS**: `bark --text "País de maricas!" --speaker "v2/pt_speaker_3" --output bolsonaro-13-maricas.wav`
- **URL referencia**: Frase real de novembro 2020 sobre a pandemia
- **Notas**: Tom de desprezo absoluto. O "maricas" e cuspido, nao falado. Nariz empinado. Queixo a maxima elevacao. Pode ser precedido por um "tsc" de reprovacao (0.2s).

### 14. "CPF cancelado!"
- **Trigger**: kill (ao eliminar um inimigo)
- **Emocao**: Celebracao macabra de violencia. Tom de videogame FPS (proposital -- ele ACHA que ta num jogo). Satisfacao predatoria.
- **Volume**: 8/10
- **Duracao**: 1.0s
- **Frequencia**: 25% de chance ao eliminar inimigo
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "CPF cancelado!" --rate "+15%" --pitch "+3Hz" --write-media bolsonaro-14-cpf.mp3`
- **Bark/XTTS**: `bark --text "CPF cancelado!" --speaker "v2/pt_speaker_3" --output bolsonaro-14-cpf.wav`
- **URL referencia**: Giria de apoiadores para matar alguem / "cancelar CPF"
- **Notas**: Tom de quem esta jogando Call of Duty e marcou um headshot. Satisfacao desproporcional. O "cancelado" e dito com um sorriso audivel. Variante: "Mais um CPF cancelado!" (1.3s) para multi-kills.

### 15. "MOTOCIATA, PORRA!"
- **Trigger**: ultimate (skill "Motociata do Juizo Final" -- ativacao)
- **Emocao**: EUFORIA TOTAL. A emocao mais genuina de todas. Ele REALMENTE ama motociata. E o unico momento em que o sorriso parece verdadeiro.
- **Volume**: 10/10 (MAXIMO)
- **Duracao**: 1.5s
- **Frequencia**: Unica -- ao ativar ultimate
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "MOTOCIATA, PORRA!" --rate "+20%" --pitch "+4Hz" --write-media bolsonaro-15-motociata.mp3`
- **Bark/XTTS**: `bark --text "MOTOCIATA, PORRA!" --speaker "v2/pt_speaker_3" --output bolsonaro-15-motociata.wav`
- **URL referencia**: Compilacoes de motociata + grito de guerra
- **Notas**: O GRITO do ultimate. Deve soar como grito de guerra samurai misturado com torcida de futebol. A unica emocao 100% genuina do personagem. "PORRA" e o ponto de exclamacao sonoro definitivo do portugues brasileiro. Rate +20% para urgencia maxima. Pode ter eco/reverb de estadio.

### 16. "Ta...l...kei..."
- **Trigger**: death (frame final) / ultimate aftermath (no chao)
- **Emocao**: Patetico. Fraco. Quebrado. O "talkei" mais triste do universo. Um sussurro de quem nao desiste mas deveria.
- **Volume**: 2/10 (sussurro fraco, quase inaudivel)
- **Duracao**: 2.0s (cada silaba arrastada com pausas)
- **Frequencia**: 100% ao morrer / 100% apos crash do ultimate
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Ta... l... kei..." --rate "-40%" --pitch "-5Hz" --write-media bolsonaro-16-talkei-triste.mp3`
- **Bark/XTTS**: `bark --text "Ta l kei" --speaker "v2/pt_speaker_3" --output bolsonaro-16-talkei-triste.wav`
- **URL referencia**: Inversao do bordao -- versao derrotada
- **Notas**: A ANTITESE do bordao #1. Mesmo talkei, mas quebrado em silabas individuais com pausas longas. Rate -40% para arrastar. Pitch -5Hz para tom grave e derrotado. Deve causar uma ponta de PENA no jogador -- mesmo sendo o vilao, esse "talkei" partido e humanizante. E o momento Andre Guedes puro: grotesco E humano ao mesmo tempo.

### 17. "Estou aqui ao vivo da minha cela, talkei?"
- **Trigger**: spawn (skin 2026 Preso ONLY) / special "Live da Cela" start
- **Emocao**: Desafio teimoso, rebeldia de presidiario, "voces nao vao me calar"
- **Volume**: 5/10 (abafado pela cela -- audio filter: low-pass + slight reverb)
- **Duracao**: 3.0s
- **Frequencia**: Uma vez ao spawnar (skin Preso) / 100% no inicio da skill Live da Cela
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Estou aqui ao vivo da minha cela, talkei? Censurado pelo sistema!" --rate "+5%" --pitch "+2Hz" --volume "-20%" --write-media bolsonaro-17-cela-live.mp3`
- **Bark/XTTS**: `bark --text "Estou aqui ao vivo da minha cela, talkei? Censurado pelo sistema!" --speaker "v2/pt_speaker_3" --output bolsonaro-17-cela-live.wav`
- **URL referencia**: Contexto 2026 -- Bolsonaro preso fazendo lives escondidas do celular
- **Notas**: Voz ABAFADA como se estivesse falando de dentro de cela com celular escondido. Post-process: aplicar low-pass filter (cortar acima de 4kHz), adicionar reverb de espaco pequeno (simulando cela), reduzir volume 20%. O "talkei?" no final e automatico -- nao importa a situacao.

### 18. "XANDAO?! NAO! NAO!" (ao ver Xandao)
- **Trigger**: proximity (Xandao entra no range de 200px)
- **Emocao**: PAVOR ABSOLUTO. O unico momento de medo REAL. Voz tremendo, cracking.
- **Volume**: 9/10 (grito de puro terror)
- **Duracao**: 1.5s
- **Frequencia**: 100% quando Xandao entra no range
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "XANDÃO?! NÃO! NÃO!" --rate "+20%" --pitch "+5Hz" --write-media bolsonaro-18-xandao-medo.mp3`
- **Bark/XTTS**: `bark --text "XANDÃO?! NÃO! NÃO!" --speaker "v2/pt_speaker_3" --output bolsonaro-18-xandao-medo.wav`
- **URL referencia**: Andre Guedes TikTok "Gabinete do Xandao" -- reacao de medo animada
- **Notas**: Pitch +5Hz para fazer a voz QUEBRAR de medo. O "NAO!" repetido e escalating panic. Deve soar como crianca vendo bicho-papao. O contraste com toda a bravata anterior e o PONTO COMICO maximo. O Bolsonaro que enfrenta tudo tremendo diante de uma unica pessoa.

### 19. "EDUARDO! SEU INUTIL!" (durante Golpe Frustrado)
- **Trigger**: special (skill "Golpe Frustrado" -- quando Eduardo erra)
- **Emocao**: Frustacao paterna MAXIMA. O pai decepcionado universal, versao brasileira.
- **Volume**: 9/10
- **Duracao**: 1.5s
- **Frequencia**: 100% durante a skill Golpe Frustrado
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "EDUARDO! Seu inútil!" --rate "+15%" --pitch "+3Hz" --write-media bolsonaro-19-eduardo.mp3`
- **Bark/XTTS**: `bark --text "EDUARDO! Seu inútil!" --speaker "v2/pt_speaker_3" --output bolsonaro-19-eduardo.wav`
- **URL referencia**: Dinamica pai-filho na politica, Andre Guedes animacoes
- **Notas**: "EDUARDO" e gritado. Pausa de 0.5s. "Seu inutil" e dito mais baixo (6/10), entre dentes, com desprezo concentrado. A dinamica pai-filho decepcionante em uma unica fala.

### 20. "Acidente de percurso, talkei?"
- **Trigger**: ultimate aftermath (apos cair da moto) / death (variante rara)
- **Emocao**: Tentativa patetica de minimizar um desastre completo. O "talkei?" final e delusional.
- **Volume**: 5/10 (dito do chao, fraco mas tentando parecer tranquilo)
- **Duracao**: 2.0s
- **Frequencia**: 80% apos crash do ultimate (antes do "Ta...l...kei...")
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Acidente de percurso, talkei?" --rate "-10%" --pitch "-2Hz" --write-media bolsonaro-20-acidente.mp3`
- **Bark/XTTS**: `bark --text "Acidente de percurso, talkei?" --speaker "v2/pt_speaker_3" --output bolsonaro-20-acidente.wav`
- **URL referencia**: Linguagem politica para minimizar fracassos
- **Notas**: Dito do CHAO, apos cair da moto. Tentando soar casual enquanto claramente destruido. O "talkei?" no final com a voz quebrando. Comedia vem do contraste entre a situacao (destruicao total) e o tom (casual/normal).

---

## Variantes de Intensidade

| Bordao | Sussurro (vol 3) | Normal (vol 6) | Grito (vol 9) |
|--------|------------------|-----------------|----------------|
| "TALKEI?" | pos-derrota (#16) | idle padrao (#1) | pos-ataque sucesso |
| "Bomba!" | -- | idle surpresa | attack_success (#2) |
| "Vagabundo!" | -- | -- | attack / hit (#3, GRITO ONLY) |
| "E dai? Lamento..." | SEMPRE baixo (#6) | -- | -- |
| "Pintou um clima..." | SEMPRE sussurro (#9) | -- | -- |
| "Brasil acima de tudo!" | -- | -- | SEMPRE grito (#11, spawn/ultimate) |
| "Imorrivel..." | -- | -- | SEMPRE grito (#12, crescendo) |
| "Ta...l...kei..." | SEMPRE sussurro (#16, morte) | -- | -- |
| "XANDAO NAO!" | -- | -- | SEMPRE grito (#18, panico) |

---

## Mapa de Triggers por Situacao de Jogo

| Situacao | Bordoes Possiveis | Probabilidade |
|----------|-------------------|---------------|
| **Spawn (default skin)** | #11 "Brasil acima de tudo" | 100% |
| **Spawn (skin Preso)** | #17 "Ao vivo da minha cela" | 100% |
| **Idle (longo, 8s+)** | #1 "Talkei?", #8 "Gripezinha", #13 "Maricas" | Random pool, 1 cada 8s |
| **Walk** | #1 "Talkei?" (raro) | 10% cada 10s |
| **Attack Success** | #2 "Bomba!", #3 "Vagabundo!", #14 "CPF cancelado" | 40% / 30% / 25% |
| **Attack Fail** | #4 "Brochavel!", #1 "Talkei?" (triste) | 50% / 50% |
| **Hit (leve, <10% HP)** | #8 "Gripezinha", #5 "Culpa do..." | 20% / 25% |
| **Hit (grave, >20% HP)** | #6 "E dai?", #5 "Culpa do..." | 15% / 25% |
| **Low HP (<30%)** | #6 "E dai?", #7 "Nao sou coveiro" | 30% / 30% |
| **Death** | #7 "Nao sou coveiro" -> #16 "Ta...l...kei..." | 50% + 100% (sequencial) |
| **Kill** | #14 "CPF cancelado" | 25% |
| **Special: Motociata** | #15 "Motociata porra!" | 100% |
| **Special: Golpe Frustrado** | #19 "Eduardo inutil!" | 100% |
| **Special: Pintou um Clima** | #9 "Pintou um clima..." | 100% |
| **Special: Live da Cela** | #17 "Ao vivo da cela" + #1 "Talkei!" (loop) | 100% |
| **Special: Invuln start** | #12 "Imorrivel..." | 100% |
| **Special: Invuln end** | #10 "Sou Messias..." | 100% |
| **Ultimate start** | #11 "Brasil acima..." -> #15 "Motociata!" | 100% sequencial |
| **Ultimate crash** | #20 "Acidente de percurso" -> #16 "Ta...l...kei..." | 80% + 100% sequencial |
| **Xandao aparece (200px)** | #18 "XANDAO NAO!" | 100% (cancela tudo) |

---

## Cooldown entre Bordoes
- **Minimo entre falas**: 3s (evitar cacofonia)
- **Excecoes**: #1 "Talkei?" pode ser GRUDADO ao final de outros bordoes (delay 0.1s, sem cooldown)
- **Priority override**: #18 (Xandao medo) cancela QUALQUER bordao em andamento (interrupt imediato)
- **Death override**: #16 ("Ta...l...kei...") SEMPRE toca no final da morte, mesmo se outro bordao estava ativo
- **Skill override**: Bordoes de skill (#9, #12, #15, #17, #19) tem prioridade sobre idle/walk bordoes
- **Nao acumula**: Se um bordao esta tocando, novos triggers sao ignorados (exceto overrides acima)

---

## Notas de Producao

### Para edge-tts (Rapido, Gratuito, Qualidade Media)
- Voice: `pt-BR-AntonioNeural`
- Base rate: `+10%` (fala rapida padrao do Bolsonaro)
- Base pitch: `+1Hz` (nasalidade leve)
- Ajustar per-bordao conforme tabela individual acima
- Post-process: adicionar leve distorcao (overdrive sutil) para agressividade
- Batch command para gerar todos:
```bash
#!/bin/bash
# Gerar todos os bordoes do Bolsonaro via edge-tts
edge-tts --voice "pt-BR-AntonioNeural" --text "Talkei?" --rate "+20%" --pitch "+2Hz" --write-media bolsonaro-01-talkei.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "BOMBA!" --rate "+15%" --pitch "+3Hz" --write-media bolsonaro-02-bomba.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Vagabundo! Canalha!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-03-vagabundo.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Minha arma é brochável!" --rate "+5%" --pitch "+1Hz" --write-media bolsonaro-04-brochavel.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa é do Lula!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-05a-culpa-lula.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa é do STF!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-05b-culpa-stf.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa é da Globo!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-05c-culpa-globo.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa é das urnas!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-05d-culpa-urnas.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "E daí? Lamento. Quer que eu faça o quê?" --rate "-5%" --pitch "-1Hz" --write-media bolsonaro-06-edai.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Não sou coveiro!" --rate "+15%" --pitch "+3Hz" --write-media bolsonaro-07-coveiro.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "É só uma gripezinha!" --rate "+5%" --pitch "+2Hz" --write-media bolsonaro-08-gripezinha.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Pintou um clima..." --rate "-20%" --pitch "-3Hz" --write-media bolsonaro-09-pintou.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Eu sou Messias, mas não faço milagre" --rate "-5%" --pitch "+1Hz" --write-media bolsonaro-10-messias.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Brasil acima de tudo! Deus acima de todos!" --rate "+5%" --pitch "+3Hz" --write-media bolsonaro-11-slogan.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Eu sou imorrível! Imbrochável! E incomível!" --rate "+5%" --pitch "+2Hz" --write-media bolsonaro-12-imorrivel.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "País de maricas!" --rate "+10%" --pitch "+2Hz" --write-media bolsonaro-13-maricas.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "CPF cancelado!" --rate "+15%" --pitch "+3Hz" --write-media bolsonaro-14-cpf.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "MOTOCIATA, PORRA!" --rate "+20%" --pitch "+4Hz" --write-media bolsonaro-15-motociata.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Ta... l... kei..." --rate "-40%" --pitch "-5Hz" --write-media bolsonaro-16-talkei-triste.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Estou aqui ao vivo da minha cela, talkei? Censurado pelo sistema!" --rate "+5%" --pitch "+2Hz" --volume "-20%" --write-media bolsonaro-17-cela-live.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "XANDÃO?! NÃO! NÃO!" --rate "+20%" --pitch "+5Hz" --write-media bolsonaro-18-xandao-medo.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "EDUARDO! Seu inútil!" --rate "+15%" --pitch "+3Hz" --write-media bolsonaro-19-eduardo.mp3
edge-tts --voice "pt-BR-AntonioNeural" --text "Acidente de percurso, talkei?" --rate "-10%" --pitch "-2Hz" --write-media bolsonaro-20-acidente.mp3
```

### Para Bark (Melhor Qualidade, Mais Lento)
- Speaker: `v2/pt_speaker_3` (voz masculina brasileira)
- Post-process: pitch shift +2 semitones para nasalidade
- Adicionar room reverb leve (simular ambiente aberto/celular)
- Para skin Preso: adicionar reverb de espaco pequeno (cela)

### Para XTTS v2 (Clone de Voz -- Melhor Resultado)
- Clonar de audio original do Bolsonaro (minimo 6s de audio limpo)
- Fonte de audio: entrevistas/lives (disponivel publicamente no YouTube)
- Prompt: fornecer texto + contexto emocional
- Post-process: minimal, a voz clonada ja tera a cadencia correta
- Comando XTTS:
```bash
# Exemplo com xtts v2
python -m TTS.bin.synthesize \
  --text "TALKEI?" \
  --model_name "tts_models/multilingual/multi-dataset/xtts_v2" \
  --speaker_wav reference_bolsonaro_6s.wav \
  --language_idx "pt" \
  --out_path bolsonaro-01-talkei-clone.wav
```

### Post-Processing Pipeline (TODOS os outputs)
1. Normalizar volume (target: -14 LUFS para jogo web)
2. Aplicar EQ: boost 2-4kHz (presenca/nasalidade), cut below 100Hz (remover rumble)
3. Aplicar compressao leve (ratio 3:1, threshold -18dB)
4. Para bordoes de GRITO: adicionar saturacao sutil (1-2dB overdrive)
5. Para bordoes de SUSSURRO: adicionar room noise minimo + breath sounds
6. Para skin PRESO: low-pass filter (4kHz cutoff) + small room reverb (decay 0.3s)
7. Trim silence no inicio e final (< 50ms padding)
8. Fade-in 10ms, fade-out 20ms (evitar clicks)
9. Exportar em: OGG Vorbis q5 (web primary) + MP3 128kbps (fallback)
10. Filename convention: `bolsonaro-{NN}-{trigger}.{ext}`
11. Metadata: incluir trigger tag e volume target nos metadados do arquivo

### Tamanho de Arquivo Target
- Bordao curto (< 1s): < 20KB OGG
- Bordao medio (1-2s): < 40KB OGG
- Bordao longo (2-3.5s): < 60KB OGG
- Total estimado (20 bordoes + 4 variantes #5): ~700KB OGG

---

## Referencias de Audio Original
- Compilacoes de lives: YouTube "bolsonaro lives melhores momentos"
- Entrevistas: YouTube "bolsonaro entrevista [frase especifica]"
- Andre Guedes animacoes: TikTok @andreguedescartoon (audio das animacoes com Bolsonaro)
- "Motociata": YouTube "bolsonaro motociata" (som ambiente, motos, multidao gritando)
- "Talkei compilacao": YouTube "bolsonaro talkei compilacao" (50+ instancias da mesma palavra)
- "E dai? Lamento": YouTube "bolsonaro e dai lamento entrevista" (audio original abril 2020)
- "Gripezinha": YouTube "bolsonaro gripezinha pronunciamento" (audio original marco 2020)
- "Imbrochavel": YouTube "bolsonaro imorrivel imbrochavel" (audio original do comicio)
- Reacao Xandao: Andre Guedes TikTok "Gabinete do Xandao" (reacao de medo animada)
- Jingle de campanha: YouTube "jingle bolsonaro 2018" (para distorcer como SFX de spawn)
