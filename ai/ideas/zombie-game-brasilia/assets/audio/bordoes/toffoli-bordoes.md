# TOFFOLI (Dias Toffoli) - Scripts de Bordoes para Audio/TTS

## Direcao Geral de Voz

- **Tipo**: Sussurro conspirador, espiao amador, neutro demais para ser inocente
- **Referencia**: Andre Guedes fazendo voz de personagem de filme de espionagem B - aquele cara que finge ser o mais sem graca da sala mas sabe de TUDO. Tipo agente secreto aposentado que gravou todas as conversas da vida
- **Pitch**: Baixo, sussurrado, quase inaudivel no modo normal. Muda para medio-grave e confiante quando revela informacoes
- **Velocidade**: Muito lenta no sussurro, rapida e assertiva quando revela
- **Sotaque**: Neutro demais - sem sotaque perceptivel, o que e suspeito por si so
- **Maneirismos**: SUSSURRA quase tudo. Duas vozes: a "publica" (sussurro apagado, sem graça) e a "real" (confiante, cruel, calculista). A transicao entre as duas e o traco definidor. Faz pausas longas olhando pros lados. Frases interrompidas como se checasse se alguem esta ouvindo
- **Respiracao**: Controlada e silenciosa - quase nao se ouve respirar

---

## Bordao 01: "Gravei! Gravei tudo!"

| Campo | Valor |
|---|---|
| **Texto exato** | "Gravei! Gravei tudo!" |
| **Emocao/Intensidade** | Revelacao triunfante, saindo das sombras - 8/10 |
| **Duracao estimada** | 1.5s |
| **Direcao TTS** | TRANSICAO DE VOZ. "Gravei!" comeca como sussurro e SOBE para voz confiante em uma unica palavra. "Gravei tudo!" agora em voz plena, satisfeita, quase euforica com poder. E o momento em que o espiao se revela. Sorriso audivel. De sussurro a grito contido em 1.5s. |
| **Trigger no jogo** | Ativacao da habilidade Escuta Secreta |
| **Prioridade** | 1 - toca sempre |
| **Efeitos sonoros** | Som de fita cassete rebobinando rapido. Click de gravador. Estatica de microfone escondido. Bipe de equipamento de espionagem. |

---

## Bordao 02: "Eu? Eu nao sei de nada..."

| Campo | Valor |
|---|---|
| **Texto exato** | "Eu? Eu nao sei de nada..." |
| **Emocao/Intensidade** | Inocencia falsa, cara-de-pau maxima - 4/10 (proposital) |
| **Duracao estimada** | 2.0s |
| **Direcao TTS** | SUSSURRADO. "Eu?" com tom genuinamente confuso (mentira). Pausa de 0.3s. "Eu nao sei de nada..." arrastado, voz sumindo no final como se a propria pessoa estivesse sumindo. Tom de quem olha pro ceu assobiando. A voz deve ser tao sem graca e monotona que o jogador quase esquece que ele esta ali. ESTE E O PONTO. Volume muito baixo - o jogador precisa prestar atencao pra ouvir. |
| **Trigger no jogo** | Idle - quando nao esta em combate |
| **Prioridade** | 2 - toca frequentemente |
| **Efeitos sonoros** | Quase nenhum. Apenas o som ambiente do cenario. Um relogio fazendo tic-tac distante. O silencio E o efeito sonoro. |

---

## Bordao 03: "Tenho um dossie sobre voce... e sobre voce... e sobre VOCE."

| Campo | Valor |
|---|---|
| **Texto exato** | "Tenho um dossie sobre voce... e sobre voce... e sobre VOCE." |
| **Emocao/Intensidade** | Ameaca crescente, poder revelado - 9/10 |
| **Duracao estimada** | 3.5s |
| **Direcao TTS** | Comeca sussurro e ESCALA. "Tenho um dossie" sussurrado com sorriso. "Sobre voce" apontando para um lugar (primeiro alvo), voz subindo. "E sobre voce" apontando para outro, voz mais alta e confiante. "E sobre VOCE" olhando direto para o jogador, voz PLENA e ameacadora, "VOCE" quase gritado. Cada repeticao de "voce" muda o pitch ascendentemente. A revelacao do poder que ele tem sobre TODOS. |
| **Trigger no jogo** | Ativacao da habilidade Dossie (debuff em multiplos alvos) |
| **Prioridade** | 1 - toca sempre |
| **Efeitos sonoros** | Som de pasta de documentos sendo aberta (THWACK). Papeis espalhando. Flash de camera fotografica a cada "voce". Na terceira vez, trovao. |

---

## Bordao 04: "Cara de paisagem? Isso e ESTRATEGIA."

| Campo | Valor |
|---|---|
| **Texto exato** | "Cara de paisagem? Isso e ESTRATEGIA." |
| **Emocao/Intensidade** | Revelacao, orgulho calculista - 7/10 |
| **Duracao estimada** | 2.2s |
| **Direcao TTS** | "Cara de paisagem?" em tom de pergunta inocente, sussurrado, como se repetisse o que alguem disse sobre ele. Pausa de 0.3s. "Isso e" tom mudando - do sussurro para voz confiante. "ESTRATEGIA" com enfase e orgulho, voz plena, quase rindo de quem subestimou ele. O "E" antes de estrategia e alongado ("eeee ESTRATEGIA"). |
| **Trigger no jogo** | Quando inimigos ignoram ele (habilidade passiva Cara de Paisagem) |
| **Prioridade** | 2 - toca frequentemente |
| **Efeitos sonoros** | Som de capa de invisibilidade desativando. Shimmer sonico. Leve nota de piano reveladora. |

---

## Bordao 05: "O microfone estava ligado? Que surpresa..."

| Campo | Valor |
|---|---|
| **Texto exato** | "O microfone estava ligado? Que surpresa..." |
| **Emocao/Intensidade** | Falsa surpresa, manipulacao pura - 6/10 |
| **Duracao estimada** | 2.5s |
| **Direcao TTS** | "O microfone estava ligado?" com falsa surpresa ABSURDAMENTE mal atuada (proposital - ele SABE que estava ligado). Voz de quem finge estar chocado mas nao consegue esconder o sorriso. "Que surpresa..." com sarcasmo tao pesado que goteja. As reticencias sao um sorriso de gato que comeu o canario. Sussurro debochado. |
| **Trigger no jogo** | Ao revelar gravacao (apos ativar Escuta Secreta e capturar informacao) |
| **Prioridade** | 2 - toca frequentemente |
| **Efeitos sonoros** | Som de "REC" aparecendo na tela (bip bip de gravacao). Estatica de audio. Playback da gravacao reverberando. Risada abafada. |

---

## Bordao 06: "Ninguem desconfia do mais sem graca da sala."

| Campo | Valor |
|---|---|
| **Texto exato** | "Ninguem desconfia do mais sem graca da sala." |
| **Emocao/Intensidade** | Auto-conhecimento sombrio, confianca oculta - 7/10 |
| **Duracao estimada** | 2.8s |
| **Direcao TTS** | Sussurro que se transforma. "Ninguem desconfia" com tom melancolico quase triste (falso). "Do mais sem graca" com pausa e auto-deprecacao que e na verdade ORGULHO. "Da sala" com voz mudando para o tom confiante e sombrio - revelando que a mediocridade e uma ARMA. O final da frase deve soar como vilao de filme revelando seu plano. A monotonia e a mascara. |
| **Trigger no jogo** | Spawn/intro do boss |
| **Prioridade** | 1 - toca sempre |
| **Efeitos sonoros** | Ambiente de sala vazia. Passos leves quase inaudiveis. Sombra se materializando. Nota de suspense cinematografica (tipo violino fino). |

---

## Bordao 07: "Essas informacoes valem muito... muito... muito dinheiro."

| Campo | Valor |
|---|---|
| **Texto exato** | "Essas informacoes valem muito... muito... muito dinheiro." |
| **Emocao/Intensidade** | Ganancia revelada, mascara caindo - 8/10 |
| **Duracao estimada** | 3.5s |
| **Direcao TTS** | "Essas informacoes valem" em sussurro conspiratorio, olhando pros lados. "Muito..." primeiro com tom neutro. "Muito..." segundo com sorriso crescendo na voz. "Muito dinheiro" com voz plena, GANANCIOSA, quase lambendo os labios. Cada "muito" com crescendo de volume e satisfacao. Na ultima frase a mascara caiu COMPLETAMENTE - nao e mais o cara sem graca, e o corrupto satisfeito. A voz deve morrer no final como se ele percebesse que falou demais e voltasse ao sussurro. |
| **Trigger no jogo** | Ao dropar dossie na morte (loot drop) |
| **Prioridade** | 1 - toca sempre |
| **Efeitos sonoros** | Som de cofre abrindo. Moedas tilintando. Papeis confidenciais caindo. Carimbo de "CONFIDENCIAL" batendo. Na morte, som de gravador parando com click. |

---

## Resumo de Prioridades

| Prioridade | Bordoes |
|---|---|
| 1 (sempre) | Gravei tudo, Tenho um dossie, Ninguem desconfia, Essas informacoes valem |
| 2 (frequente) | Eu nao sei de nada, Cara de paisagem, O microfone estava ligado |
| 3 (raro) | - |

## Nota Especial de Producao

Toffoli e o boss mais SILENCIOSO do jogo. Seu volume de voz e consistentemente mais baixo que os outros bosses. O jogador precisa prestar atencao pra ouvir as falas dele - isso e intencional e faz parte do design. A excecao sao os momentos de revelacao (Gravei!, Dossie, Essas informacoes) onde o volume SOBE dramaticamente. O contraste entre o silencio habitual e as revelacoes e o que torna ele assustador. Mixar as falas dele 30-40% mais baixo que os outros personagens no baseline, com os picos de revelacao no volume normal.

## Direcao de Mixagem

- **Volume base**: -6dB abaixo dos outros bosses
- **Volume de revelacao**: Volume normal (+0dB)
- **Efeito de sussurro**: Reverb minimo, dry, intimo (como se falasse no ouvido do jogador)
- **Efeito de revelacao**: Reverb medio, mais presenca, mais graves
