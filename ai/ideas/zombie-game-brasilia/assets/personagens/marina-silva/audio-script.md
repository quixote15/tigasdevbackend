# Marina Silva - Script de Audio

## VISAO GERAL

Marina e o personagem MAIS SILENCIOSO do jogo. Quase nao fala. Quando fala, e em sussurro. O contraste com Ciro (que grita o tempo todo) e proposital e fundamental. O audio de Marina deve transmitir: MELANCOLIA, RESIGNACAO, SILENCIO e AUSENCIA.

### Voz Base
- Tom: mezzo-soprano suave, quase eterea
- Sotaque: neutro, sem regionalismos fortes
- Cadencia: LENTA, pausada, como quem pensa antes de falar (e desiste no meio)
- Volume base: 60% do volume medio dos outros personagens (MUITO BAIXO)
- Emocao predominante: melancolica aceitacao, tristeza serena
- Caracteristica: voz parece vir de LONGE, como eco de outro comodo

---

## BORDOES PRINCIPAIS

### 1. "Eu volto em 4 anos..."

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `marina_volto_4anos.ogg`                                  |
| Duracao            | 2.5s (incluindo silencio final)                            |
| Volume             | 55% (sussurro)                                             |
| Contexto           | Fade Out / Death. Ultima fala antes de desaparecer.        |
| Entonacao          | Sussurro melancolico, resignado. "Eu volto..." (pausa 0.5s, como se duvidasse) "em quatro anos..." (voz desvanecendo ate sumir, trailing off). Nao e uma promessa — e uma esperanca que nem ela acredita. |
| Direcao de TTS     | Sussurrar. Volume começa em 55% e vai pra 20% ate o final. Cada palavra mais suave que a anterior. Como alguem se afastando de um microfone. |
| Efeitos            | Reverb longo (como se falasse numa catedral vazia). Low-pass leve. Volume decrescente linear. |
| Frequencia de uso  | Sempre que desaparece (Fade Out e Death). A assinatura sonora dela. |
| Prioridade         | ALTA — e rara, quando toca, toca.                          |

### 2. "Eu estava aqui o tempo todo..."

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `marina_estava_aqui.ogg`                                  |
| Duracao            | 2.2s                                                       |
| Volume             | 50% (quase inaudivel)                                      |
| Contexto           | Quando jogador finalmente interage com ela durante a janela de 3 segundos. Resposta a ser notada. |
| Entonacao          | Surpresa suave misturada com tristeza. "Eu estava aqui..." (incredulidade de ser notada) "o tempo todo..." (quase um alivio, quase um choro). |
| Direcao de TTS     | Começa com surpresa genuina (alguem a viu!), transiciona pra emocao contida. Voz levemente tremula no "tempo todo". Como se quase chorasse mas se controlasse. |
| Efeitos            | Reverb medio. Levissimo tremble/vibrato na voz.           |
| Frequencia de uso  | Rara. Apenas quando jogador interage com sucesso.          |

### 3. "Alguem viu a Marina?" (dito por OUTROS personagens)

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `outros_cadê_marina.ogg`(versoes multiplas)               |
| Duracao            | 1.5s                                                       |
| Volume             | 80% (volume normal, dito por OUTROS)                       |
| Contexto           | NPC ou personagem aleatorio pergunta. Marina pode ou nao estar presente. Se estiver presente, ninguem nota mesmo assim. |
| Entonacao          | Casual, como quem pergunta por educação mas nao se importa com a resposta. "Alguem viu a Marina?" (olhando pro celular, sem interesse real). |
| Direcao de TTS     | NAO e Marina falando. E outro personagem. Tom casual, distraido. A pergunta e retorica — ninguem espera resposta. |
| Efeitos            | Nenhum. Audio seco, direto.                                |
| Frequencia de uso  | Media. Outros NPCs dizem aleatorialmente.                  |
| Variantes          |                                                            |
| Ciro               | "Alguem viu a Marina? Nao? Enfim, como eu dizia..." (2.5s)|
| NPC generico       | "Marina? Que Marina?" (1.0s)                              |
| Zumbi              | (silencio — ate os zumbis a ignoram)                       |

### 4. "Democraticamente..."

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `marina_democraticamente.ogg`                             |
| Duracao            | 1.8s                                                       |
| Volume             | 50%                                                        |
| Contexto           | Idle raro (3% chance a cada 20s). Marina diz a palavra sozinha, como mantra, sem contexto. |
| Entonacao          | Sussurro contemplativo. "De-mo-cra-ti-ca-men-te..." Cada silaba pronunciada com cuidado, como quem saboreia a palavra. Trailing off no final. |
| Direcao de TTS     | MUITO lento. Cada silaba separada. Como meditacao. A palavra perde sentido de tao repetida. |
| Efeitos            | Reverb longo. Eco suave. Como se a palavra ecoasse num espaco vazio. |
| Frequencia de uso  | Rara. Idle contemplativo.                                  |

---

## FALAS DE CONTEXTO

### Aparicao (Fade In)

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `marina_aparicao.ogg`                                     |
| Duracao            | 0.3s                                                       |
| Volume             | 30% (QUASE inaudivel)                                      |
| Contexto           | Quando Marina faz Fade In. Jogador atento TALVEZ ouca.    |
| Conteudo           | Nao e uma palavra. E um suspiro suave. Um "hm" minusculo. |
| Entonacao          | Suspiro existencial. O som de alguem que materializa e ja sabe que ninguem vai notar. |
| Efeitos            | High-pass (voz fina, distante). Reverb maximo.            |
| Nota               | 70% dos jogadores NAO vao ouvir isso. E proposital.       |

### Interacao bem sucedida

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `marina_interacao_sucesso.ogg`                            |
| Duracao            | 1.0s                                                       |
| Volume             | 65% (o mais alto que Marina fica!)                         |
| Contexto           | Jogador interage durante janela de 3s. Momento raro.       |
| Conteudo           | Micro-riso surpreso. "Oh!" (surpresa genuina). Quase um soluço de alivio. |
| Entonacao          | O UNICO momento de genuina alegria de Marina. "Oh!" — surpresa, alivio, gratidao, tudo em uma silaba. |
| Efeitos            | Sem reverb (pra soar mais PRESENTE que o normal). O audio mais "direto" dela. |
| Nota               | Contraste com tudo mais: por um instante, Marina existe.   |

### Presenca Espectral (enquanto visivel)

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `marina_presenca_loop.ogg`                                |
| Duracao            | 3.0s (loop)                                                |
| Volume             | 15% (QUASE subliminar)                                     |
| Contexto           | Loop ambiente enquanto Marina esta presente no mapa.       |
| Conteudo           | Nao e fala. E uma respiracao suave. Inspirar... expirar... Um som VIVO mas QUASE nao la. |
| Entonacao          | N/A (respiracao)                                           |
| Efeitos            | Heavy reverb. Low-pass. Como ouvir alguem respirar num sonho. |
| Nota               | Jogador com headphones TALVEZ perceba. E sutil.            |

### Hit recebido

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `marina_hit.ogg`                                          |
| Duracao            | 0.4s                                                       |
| Volume             | 40%                                                        |
| Contexto           | Marina leva dano (fica mais transparente).                 |
| Conteudo           | "Ah..." — nao e grito de dor. E sussurro de surpresa triste. Como quem diz "ate voce me viu... pra me machucar." |
| Entonacao          | Sussurro breveissimo. Mais triste que dolorido. Resignacao. |
| Efeitos            | Volume cai de 40% pra 10% no decay. Como se o hit a empurrasse pra mais longe do microfone. |

---

## SFX (EFEITOS SONOROS)

### Aparicao / Desaparicao

| Efeito             | Arquivo                   | Duracao | Volume | Descricao                              |
|--------------------|---------------------------|---------|--------|----------------------------------------|
| Fade In            | `sfx_marina_fadein.ogg`   | 1.0s    | 25%    | Tom suave ascendente. Como sino de vento distante. Nao musical — organico. |
| Fade Out           | `sfx_marina_fadeout.ogg`  | 1.0s    | 25%    | Tom descendente. O contrario do fade in. Desvanece ate silencio total. |
| Folha caindo       | `sfx_marina_folha.ogg`    | 0.8s    | 20%    | Folha seca caindo no chao. Tss... toque suave. |
| Particulas subindo | `sfx_marina_particulas.ogg`| 0.5s   | 15%    | Shimmer sutil. Brilhos micro. Quase nada. |

### Presenca

| Efeito             | Arquivo                   | Duracao | Volume | Descricao                              |
|--------------------|---------------------------|---------|--------|----------------------------------------|
| Ambiencia          | `sfx_marina_ambiente.ogg` | (loop)  | 10%    | Drone suavissimo. Tom unico, distante. Campo indica presenca sem ser obvio. |
| Oscilacao alpha    | `sfx_marina_oscila.ogg`   | 0.3s    | 8%     | Micro-som a cada pico de oscilacao de alpha. Like static whisper. |
| Timer aviso        | `sfx_marina_timer.ogg`    | 0.5s    | 30%    | A 1s do fim da janela de interacao. Tom suave urgente. "Ela vai sumir." |

### Interacao

| Efeito             | Arquivo                   | Duracao | Volume | Descricao                              |
|--------------------|---------------------------|---------|--------|----------------------------------------|
| Bonus desbloqueado | `sfx_marina_bonus.ogg`    | 1.5s    | 50%    | Tom magico suave. Reward sound. O mais "presente" som dela. |
| Toque de confusao  | `sfx_marina_toque.ogg`    | 0.5s    | 30%    | Reverb distorcido. O inimigo ouve... algo. Nao sabe o que. |

---

## DESIGN DE SILENCIO

### O que Marina NAO tem (e os outros tem):

| Audio                    | Outros personagens | Marina                |
|--------------------------|--------------------|-----------------------|
| Grito de ataque          | Sim                | Nao                   |
| Grunhido de dor          | Sim                | Sussurro              |
| Passos audiveis          | Sim                | NAO (ela flutua)      |
| Grito de morte           | Sim                | Silencio + sussurro   |
| Falas de combate         | Sim                | Nao                   |
| Bordoes frequentes       | Sim                | Raros e baixos        |
| SFX de impacto           | Sim                | Abafados              |
| Musica tematica propria  | Sim (para bosses)  | Silencio tematico     |

### O "Som do Silencio" de Marina
Quando Marina esta presente, os sons ambientes do jogo ficam LEVEMENTE mais baixos (-5dB) num raio de 64px ao redor dela. Como se a presença dela absorvesse som. O jogador atento nota que "algo ficou mais quieto" antes de ve-la.

---

## TABELA DE PRIORIDADE DE AUDIO

| Prioridade | Audio                              | Volume  | Pode ser interrompido por |
|------------|-------------------------------------|---------|---------------------------|
| 1 (max)    | "Eu volto em 4 anos..." (death/fade)| 55%     | Nada                      |
| 2          | "Eu estava aqui o tempo todo..."    | 50%     | Apenas prioridade 1       |
| 3          | Interacao sucesso "Oh!"            | 65%     | Prioridade 1-2            |
| 4          | "Democraticamente..."              | 50%     | Prioridade 1-3            |
| 5          | Hit "Ah..."                        | 40%     | Qualquer fala             |
| 6          | SFX (fade, particulas, etc)        | 15-30%  | Qualquer fala             |
| 7 (min)    | Respiracao/ambiencia               | 10-15%  | Qualquer coisa            |

**Regra**: NUNCA mais de 1 audio de Marina simultaneo (fala OU sfx, nunca ambos). Simplicidade = invisibilidade.

---

## INTERACAO SONORA COM OUTROS PERSONAGENS

### "Alguem viu a Marina?" — Versoes por personagem

| Personagem      | Arquivo                         | Fala                                             | Tom                          |
|-----------------|---------------------------------|--------------------------------------------------|------------------------------|
| Ciro            | `ciro_cade_marina.ogg`         | "Alguem viu a Marina? Nao? Enfim, como eu dizia sobre a Cirocracia..." | Desinteressado, muda de assunto imediatamente |
| Lula (se houver)| `lula_cade_marina.ogg`         | "A companheira Marina... como e mesmo o nome dela?" | Esqueceu o nome              |
| Bolsonaro (se houver)| `bolso_cade_marina.ogg`   | (silencio total, nao menciona)                   | Nem lembra que existe        |
| NPC generico    | `npc_cade_marina.ogg`          | "Marina? Que Marina?"                            | Genuinamente nao sabe        |
| Narrador        | `narrador_marina.ogg`          | "Em algum lugar, alguem quase existiu."          | Existencial, poetico         |

---

## EASTER EGG SONORO

### Achievement "Alguem viu a Marina?"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `sfx_achievement_marina.ogg`                              |
| Duracao            | 3.0s                                                       |
| Volume             | 70% (alto pra Marina! Momento especial)                    |
| Contexto           | Jogador interage com Marina com sucesso pela primeira vez.  |
| Conteudo           | Tom de achievement suave (nao fanfarra). Piano unico nota. Depois o sussurro de Marina: "Voce... me viu?" |
| Nota               | Esse e o momento MAIS ALTO de Marina no jogo inteiro. Deve ser emocional. |

### Segredo: 5 interacoes

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `sfx_marina_5_interacoes.ogg`                             |
| Duracao            | 4.0s                                                       |
| Volume             | 60%                                                        |
| Contexto           | Jogador encontrou e interagiu com Marina 5 vezes. Desbloqueia skin Ectoplasmatica. |
| Conteudo           | Marina, pela PRIMEIRA e UNICA vez, fala em volume quase normal: "Obrigada por me procurar." Pausa. "Mas eu preciso ir agora." Som etéreo crescente. Silencio. |

---

## CONFIGURACAO DE TTS / GRAVACAO

### Para geracao TTS (ElevenLabs / similar)

```
Voice characteristics:
- Gender: Female
- Age: 60-65
- Accent: Brazilian Portuguese (neutral, no strong regional accent)
- Tone: Soft, ethereal, melancholic, resigned
- Speed: 0.7x normal (slow, contemplative)
- Pitch: Mezzo-soprano, gentle, never rises to shout
- Emotion range: melancholic (base) -> surprised (rare) -> serene -> sad
- Distinctive feature: Voice sounds like it comes from slightly far away, as if through a wall
- Volume: Always softer than expected. If other characters are at 100%, Marina is at 50-60% MAX.
```

### Instrucoes de gravacao (se usar ator/atriz)

1. Atriz deve imaginar que esta falando numa biblioteca vazia as 3 da manha
2. NUNCA levantar a voz. O volume maximo de Marina e o volume normal dos outros
3. Cada fala deve soar como se pudesse ser a ultima coisa que ela diz
4. "Eu volto em 4 anos" nao e promessa — e um desejo que ela sabe que nao vai se realizar
5. O "Oh!" de surpresa ao ser notada e o UNICO momento genuino — deve soar como alguem que recebeu um presente inesperado
6. Respiracoes entre frases devem ser audiveis mas suaves
7. Trail off: quase TODAS as frases terminam desvanecendo, como se a voz fosse embora antes da pessoa

### Pos-Processamento Obrigatorio
- Aplicar reverb longo em TUDO (cathedral preset, wet 40-60%)
- Low-pass sutil em tudo (corte acima de 8kHz, suave)
- Normalizar volume em -12dB (mais baixo que o padrao de -6dB)
- NAO comprimir dinamica — deixar as variacoes naturais de volume
