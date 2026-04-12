# JANJA (A Primeira-Dama / A Mandachuva) -- Bordoes de Audio

**Voz**: Feminina forte, assertiva, sotaque paranaense. Tom geral: mulher que SABE que manda. Voz que oscila entre mel/acucar (com Lula) e aco temperado (com todos os outros). Projecao vocal potente -- nunca fala baixo por acidente, so por estrategia.
**TTS Voice**: `pt-BR-FranciscaNeural` -- voz feminina assertiva, ajustar rate +5% para tom energetico
**Alternativa**: Voice actor feminina com voz forte, assertiva, sotaque paranaense, capacidade de variar entre docura calculada e autoridade pura

---

### 1a. "FORA, ELON MUSK!" (Normal)
- **Trigger**: attack / enemy_spawn / encontro com inimigos tecnologicos
- **Emocao**: Indignacao pura, GRITO ENERGETICO, voz aguda potente
- **Volume**: 9/10
- **Duracao**: 1.5s
- **Frequencia**: Ao atacar / quando inimigos aparecem / cada 20s em combate
- **TTS Command**: `edge-tts --voice "pt-BR-FranciscaNeural" --text "FORA, ELON MUSK!" --rate "+10%" --pitch "+4Hz" --write-media janja-01a-musk-normal.mp3`
- **Efeitos de pos-producao**: GRITO energetico limpo, voz aguda potente, entonacao de protesto
- **URL referencia**: Discurso real da Janja no G20 (2024) -- "Fuck you, Elon Musk" adaptado
- **Notas**: O bordao MAIS ICONICO da Janja. Baseado no momento real do G20. Deve soar como protesto de rua com microfone aberto. Energia de lider sindical.

### 1b. "FORA, ELON MUSK!" (GRITO G20)
- **Trigger**: special / ultimate / boss_appear
- **Emocao**: Indignacao MAXIMA, eco de estadio, publico reagindo ao fundo
- **Volume**: 10/10
- **Duracao**: 2.0s
- **Frequencia**: Ao ativar skill especial / boss fight
- **TTS Command**: `edge-tts --voice "pt-BR-FranciscaNeural" --text "FORAAA, ELON MUSK!" --rate "+15%" --pitch "+5Hz" --write-media janja-01b-musk-g20.mp3`
- **Efeitos de pos-producao**: Eco de estadio/auditorio (reverb 2.0s), SFX de publico reagindo ao fundo ("OHHH!"), voz no pico de potencia
- **URL referencia**: G20 momento viral -- eco do salao de conferencias
- **Notas**: Versao EPICA. Eco de salao do G20, multidao reagindo ao fundo. Deve soar como momento historico. Stun em area nos inimigos.

### 1c. "fora... elon musk..." (Sussurro Ameacador)
- **Trigger**: pre-attack / stealth / antes de emboscada
- **Emocao**: Ameaca sussurrada entre dentes, calma assassina, promessa de violencia
- **Volume**: 3/10
- **Duracao**: 1.0s
- **Frequencia**: Antes de ataque surpresa / modo stealth
- **TTS Command**: `edge-tts --voice "pt-BR-FranciscaNeural" --text "fora... elon musk..." --rate "-10%" --pitch "+0Hz" --volume "-40%" --write-media janja-01c-musk-sussurro.mp3`
- **Efeitos de pos-producao**: Sussurro entre dentes, voz baixa mas CARREGADA de ameaca, cada palavra separada por pausa (0.3s)
- **Notas**: A versao mais ASSUSTADORA. Sussurro de quem ja decidiu o destino do inimigo. Mais ameacador que o grito. Calma que precede a tempestade.

### 2. "Querido, gostou da reforma?"
- **Trigger**: idle / apos usar buff / apos alterar cenario/mapa
- **Emocao**: Mel/acucar na superficie, CONTROLE total por baixo. Voz doce mas com subtexto de "nao tinha opcao"
- **Volume**: 6/10
- **Duracao**: 2.0s
- **Frequencia**: Cada 30s em idle / apos ativar buff de area
- **TTS Command**: `edge-tts --voice "pt-BR-FranciscaNeural" --text "Querido, gostou da reforma?" --rate "-5%" --pitch "+2Hz" --write-media janja-02-reforma.mp3`
- **Efeitos de pos-producao**: Tom mel/acucar, voz doce mas CONTROLADORA. Entonacao de pergunta retorica -- nao importa se gostou, ja foi feito.
- **URL referencia**: Reformas do Palacio da Alvorada -- polemicas de decoracao
- **Notas**: "Querido" dito com doçura calculada. A pergunta e RETORICA -- a reforma ja esta feita. Tom de esposa que redecora a casa sem consultar o marido e depois pergunta como cortesia.

### 3. "Para quem eu mando a conta, amor?"
- **Trigger**: attack / gastar recursos / usar item caro / destruir cenario
- **Emocao**: Casualidade de quem gasta sem preocupacao, tom de shopping center
- **Volume**: 6/10
- **Duracao**: 2.0s
- **Frequencia**: Ao usar itens caros / destruir cenario / cada 35s em combate
- **TTS Command**: `edge-tts --voice "pt-BR-FranciscaNeural" --text "Para quem eu mando a conta, amor?" --rate "+0%" --pitch "+2Hz" --write-media janja-03-conta.mp3`
- **Efeitos de pos-producao**: Tom casual de quem pergunta por educacao mas ja sabe a resposta (conta vai pro contribuinte). "Amor" dito com docura que esconde total indiferenca ao custo.
- **Notas**: A conta sempre vai pra alguem. Janja gasta com naturalidade de quem nunca viu a fatura. Tom de socialite em shopping -- "manda pra conta" como reflexo.

### 4. "Quem manda aqui sou eu, amor. Voce so assina."
- **Trigger**: special / ultimate / momento de dominancia / interact_lula
- **Emocao**: Autoritarismo disfarçado de carinho. Tom de "verdade que todo mundo sabe" dita com sorriso
- **Volume**: 7/10
- **Duracao**: 3.0s
- **Frequencia**: Ao ativar skill especial / ao interagir com Lula (se presente) / cada 50s
- **TTS Command**: `edge-tts --voice "pt-BR-FranciscaNeural" --text "Quem manda aqui sou eu, amor. Voce so assina." --rate "-5%" --pitch "+2Hz" --write-media janja-04-manda.mp3`
- **Efeitos de pos-producao**:
  - "Quem manda aqui sou eu, amor." -- tom autoritario mas disfarçado de carinhoso, voz firme
  - PAUSA de 0.5s
  - "Voce so assina." -- tom mais baixo, factual, sorriso na voz, como verdade obvia
- **URL referencia**: Narrativa de "Janja manda no Lula" -- memes e analises politicas
- **Notas**: O bordao que CONFIRMA o que todos suspeitam. Dito com naturalidade total -- nao e acusacao, e fato. "Amor" e usado como titulo, nao como afeto. A pausa entre as frases e essencial.

### 5. "Mais uma reforminha, presidente?"
- **Trigger**: idle / apos mudar de area / apos buff de cenario
- **Emocao**: Inocencia CALCULADA, manipulacao disfarçada de sugestao doce
- **Volume**: 6/10
- **Duracao**: 2.0s
- **Frequencia**: Cada 35s em idle / ao entrar em area nova
- **TTS Command**: `edge-tts --voice "pt-BR-FranciscaNeural" --text "Mais uma reforminha, presidente?" --rate "-5%" --pitch "+3Hz" --write-media janja-05-reforminha.mp3`
- **Efeitos de pos-producao**: Tom inocente/manipulador, diminutivo "reforminha" dito com doçura extrema, entonacao ascendente de pergunta
- **Notas**: O diminutivo "reforminha" e a arma. Faz parecer pequeno, inofensivo. Mas cada "reforminha" custa milhoes. Tom de quem ja decidiu e esta apenas informando disfarçado de pergunta.

---

## Variantes de Intensidade

| "FORA, ELON MUSK!" | Volume | Pitch | Duracao | Efeito | Contexto |
|---|---|---|---|---|---|
| Sussurro Ameacador | 3/10 | +0Hz | 1.0s | Entre dentes, ameaca | Pre-ataque / stealth |
| Normal | 9/10 | +4Hz | 1.5s | Grito limpo | Combate padrao |
| GRITO G20 | 10/10 | +5Hz | 2.0s | Eco + publico ao fundo | Special / ultimate / boss |

## Regras de Frequencia (Janja-Especificas)

1. **"FORA, ELON MUSK!"** e o bordao primario -- pelo menos UMA variante por combate
2. **Bordoes com "amor"/"querido"** so tocam fora de combate ou em idle -- sao manipulacao, nao grito de guerra
3. **Sussurro ameacador** (1c) e mais RARO e mais ASSUSTADOR que o grito -- usar com parcimonia
4. Se Lula esta no mapa, bordoes 2, 4 e 5 triplicam em frequencia (ela fala COM ele)
5. Janja tem o bordao com MAIOR VARIACAO de intensidade -- 3 versoes do mesmo grito

## Efeitos Sonoros Contextuais
- **SFX de salto alto**: Clique de salto alto (0.2s) antes de QUALQUER fala da Janja -- identidade sonora
- **SFX de multidao G20**: Layer de fundo exclusivo para versao 1b
- **SFX de cartao de credito**: Som sutil de "beep" de maquininha apos bordao 3

## Referencias de Audio Original
- G20 (2024): "Fuck you, Elon Musk" -- momento viral real
- Entrevistas da Janja -- tom assertivo, sotaque paranaense
- Polemicas de reforma do Alvorada -- reportagens
- Memes "Janja manda" -- compilacoes
- Andre Guedes: Serie "Zumbis em Brasilia"
