# Ciro Gomes - Script de Audio

## VISAO GERAL

Ciro e o personagem MAIS BARULHENTO do jogo. Fala o tempo todo, grita, xinga, gesticula sonoramente. O contraste com Marina (que sussurra e some) e proposital. Audio de Ciro deve transmitir: ARROGANCIA, RAIVA, DESCONTROLE e COMEDIA.

### Voz Base
- Tom: barítono grave, levemente rouco
- Sotaque: cearense/nordestino moderado (nao caricato demais)
- Cadencia: rapida, atropela palavras, engole finais de frase
- Volume base: ALTO (120% do volume medio dos outros personagens)
- Emocao predominante: irritacao contida prestes a explodir

---

## BORDOES PRINCIPAIS

### 1. "Acabou meu Rivotril!"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_rivotril_acabou.ogg`                                |
| Duracao            | 1.8s                                                       |
| Volume             | 140% (GRITO)                                               |
| Contexto           | Barra de Rivotril chega a 0%. Trigger automatico.          |
| Entonacao          | Começa grave e sobe pra agudo no "Rivotril!". Desespero puro. Voz quebra no "meu". |
| Direcao de TTS     | "a-ca-BOU" (pausa dramatica 0.3s) "MEU" (voz quebrando) "ri-vo-TRIL!!!" (grito ascendente, quase chorando) |
| Efeitos            | Leve reverb. Distorcao nos picos. Eco rapido no final.     |
| Frequencia de uso  | Sempre que Rivotril zera. Pode repetir.                    |
| Prioridade audio   | ALTA — interrompe qualquer outro audio de Ciro.            |

### 2. "Bossaloide!"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_bossaloide.ogg`                                     |
| Duracao            | 0.9s                                                       |
| Volume             | 130%                                                       |
| Contexto           | Xingamento Erudito (skill). Tambem usado como Hit reaction aleatoria (30% chance). |
| Entonacao          | Cuspe a palavra com desprezo. "BOS-sa-LOI-de!" Enfase na primeira e terceira silabas. Desdenhoso. |
| Direcao de TTS     | Voz carregada de desprezo. Pronunciar como se a palavra fosse um insulto FISICO. Boca cheia de cuspe. |
| Efeitos            | Nenhum efeito especial. Audio seco, direto, agressivo.     |
| Frequencia de uso  | Alta. E o xingamento padrao.                               |
| Variantes          | Gravar 3 variantes com entonacoes diferentes pra nao cansar.|

### 3. "Patife!"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_patife.ogg`                                         |
| Duracao            | 0.7s                                                       |
| Volume             | 125%                                                       |
| Contexto           | Xingamento alternativo. Usado em Hit reaction (20% chance) e como variante do Xingamento Erudito. |
| Entonacao          | Mais contido que "Bossaloide" mas igualmente venenoso. "pa-TI-fe!" Sibilante no "f". |
| Direcao de TTS     | Dito entre dentes cerrados. Maxilar travado. Como se estivesse se segurando pra nao agredir. |
| Efeitos            | Nenhum.                                                    |
| Frequencia de uso  | Media.                                                     |

### 4. "Eu tenho um plano!"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_tenho_plano.ogg`                                    |
| Duracao            | 1.5s                                                       |
| Volume             | 115%                                                       |
| Contexto           | Idle aleatorio (10% chance a cada 15s de idle). Ciro anuncia que tem um plano. Nunca apresenta o plano. |
| Entonacao          | Confiante, altivo, como quem vai revelar algo genial. "EU" (peito estufado) "TENHO" (enfatico) "um PLA-no!" (dedo levantado). Pausa no final esperando aplausos que nunca vem. |
| Direcao de TTS     | Tom professoral. Como se estivesse num palco. Aguarda reacao do publico. Silencio apos. |
| Efeitos            | Silencio de 0.5s apos a fala (expectativa). Nenhum efeito sonoro no silencio. |
| Frequencia de uso  | Baixa-media. Aleatorio em idle.                            |

### 5. "Ja ouviu falar na Cirocracia? O unico caminho possivel!"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_cirocracia.ogg`                                     |
| Duracao            | 3.2s                                                       |
| Volume             | 120%                                                       |
| Contexto           | Ativacao da skill Cirocracia. Dito enquanto a cupula se forma. |
| Entonacao          | "Ja ouviu falar" (rapido, desdenhoso) "na CIROCRACIA?" (enfatico, orgulhoso, pausa dramatica 0.3s) "O UNICO" (maos abertas, revelacao) "caminho possivel!" (sorriso convicto). |
| Direcao de TTS     | Tom messiânico. Ele ACREDITA. Pra ele e revelacao divina. Pro jogador e piada. |
| Efeitos            | Leve eco no "Cirocracia" (reverb curto). Efeito de energia crescente no fundo (SFX). |
| Frequencia de uso  | Sempre que ativa Cirocracia.                               |

### 6. "Que brisa, mano"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_que_brisa.ogg`                                      |
| Duracao            | 1.2s                                                       |
| Volume             | 85% (MAIS BAIXO que o normal dele)                         |
| Contexto           | Pos-Rage do Rivotril. Ciro esta tonto, confuso, como se tivesse saido de um transe. Tambem aleatorio apos stunado. |
| Entonacao          | Arrastada, lenta, como se estivesse CHAPADO. "Que... brisa... mano..." Olhar perdido. Contraste total com a energia normal dele. |
| Direcao de TTS     | Tom baixo, arrastado, quase sussurrando. Como se nao soubesse onde esta. Alcoolizado/sedado. |
| Efeitos            | Leve filtro de "underwater" (low-pass suave). Eco distante. |
| Frequencia de uso  | Baixa. Apos Rage e stun.                                   |

### 7. "Voce gosta de pacoca?"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_pacoca_pergunta.ogg`                                |
| Duracao            | 1.4s                                                       |
| Volume             | 100%                                                       |
| Contexto           | Interacao com jogador/NPC. Aleatorio quando jogador se aproxima (5% chance). Completamente fora de contexto. |
| Entonacao          | Genuinamente curiosa, como se fosse a pergunta mais importante do mundo. "Voce gosta..." (inclinando a cabeca) "de PACOCA?" (olhos arregalados, esperando resposta). |
| Direcao de TTS     | Serio. Ele esta SERIO. Nao e piada pra ele. E questao existencial. |
| Efeitos            | Nenhum.                                                    |
| Frequencia de uso  | Rara. Easter egg de interacao.                              |

### 8. "Canaleao machista!"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_canaleao.ogg`                                       |
| Duracao            | 1.1s                                                       |
| Volume             | 130%                                                       |
| Contexto           | Xingamento alternativo. Usado contra inimigos especificos ou aleatorio em combate. |
| Entonacao          | CUSPIDO com nojo. "ca-na-LE-ao" (prolongando o "ao") "ma-CHIS-ta!" (quase cuspindo). |
| Direcao de TTS     | Raiva visceral. Como se a pessoa a quem se dirige fosse a pior do mundo. |
| Efeitos            | Nenhum.                                                    |
| Frequencia de uso  | Media.                                                     |

### 9. "Eu me recuso a responder essa pergunta bossaloide e caluniosa!"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_me_recuso.ogg`                                      |
| Duracao            | 3.8s                                                       |
| Volume             | 135%                                                       |
| Contexto           | Debate Unilateral (skill). A fala mais longa. Dita durante o discurso que ninguem pediu. |
| Entonacao          | Começa indignado e vai CRESCENDO. "Eu me RECUSO" (dedo apontado) "a responder" (desprezo) "essa pergunta" (cuspe) "BOSSALOIDE" (grito) "e CALUNIOSA!" (batendo na mesa imaginaria). |
| Direcao de TTS     | Escalar de irritado pra FURIOSO progressivamente. Cada palavra mais alta que a anterior. Final quase gritando. |
| Efeitos            | Reverb no final. Eco de "caluniosa" desvanecendo.          |
| Frequencia de uso  | Baixa. Apenas durante Debate Unilateral.                   |

### 10. "Liberalzinho de merda!"

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_liberalzinho.ogg`                                   |
| Duracao            | 1.3s                                                       |
| Volume             | 130%                                                       |
| Contexto           | Xingamento variante. Usado contra inimigos tipo "economista" ou aleatorio. |
| Entonacao          | Desprezo puro. "Liberalzinho" dito com diminutivo venenoso. "de MERDA!" gritado. |
| Direcao de TTS     | O diminutivo "-zinho" e a chave. Ele MENOSPREZANDO. O "de merda" e o remate furioso. |
| Efeitos            | Nenhum.                                                    |
| Frequencia de uso  | Media.                                                     |

---

## FALAS DE CONTEXTO (NAO-BORDOES)

### Death / Pacoca Mental

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_pacoca_death.ogg`                                   |
| Duracao            | 3.0s (loop de 1s x3)                                      |
| Volume             | 60% -> 40% -> 20% (decrescente)                           |
| Contexto           | Morte. Ciro no chao repetindo "pacoca" ate desaparecer.    |
| Entonacao          | "pa-CO-ca... pa-CO-ca... pa... co... ca..." Cada repeticao mais fraca, mais lenta, mais distante. Voz quebrando. Desvanecendo. |
| Direcao de TTS     | Primeira repeticao: 80% velocidade normal. Segunda: 60%. Terceira: 40%. Como um disco desacelerando. |
| Efeitos            | Low-pass filter crescente (fica mais abafado). Reverb aumenta (distancia). |
| Loop               | 3 repeticoes exatas, nao loop infinito.                    |

### Ressurreicao (Candidatura Eterna)

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_voltei.ogg`                                         |
| Duracao            | 1.5s                                                       |
| Volume             | 90% (cada ressurreicao 10% mais baixo)                     |
| Contexto           | Apos ressuscitar via Candidatura Eterna.                   |
| Entonacao          | "Desta vez... EU VOU!" Confiante mas visivelmente mais fraco a cada vez. |
| Direcao de TTS     | Volume e confianca diminuem a cada ressurreicao. Na 5a vez, e quase um sussurro patetico. Na 10a, e inaudivel. |
| Efeitos            | Eco crescente a cada morte (como se falasse de cada vez mais longe). |

### Cirocracia Quebrando

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_cirocracia_quebra.ogg`                              |
| Duracao            | 1.0s                                                       |
| Volume             | 110%                                                       |
| Contexto           | Cupula da Cirocracia rachando e estourando (frames 6-8).   |
| Entonacao          | "NAO! O sistema... era PERFEITO!" Incredulidade. Desespero comico. |
| Direcao de TTS     | "NAO!" agudo, gritado. Depois "o sistema..." (voz quebrando) "era PERFEITO!" (entre lagrimas de raiva). |
| Efeitos            | SFX de vidro quebrando sobreposto. Reverb.                 |

### Terceira Via (Esquiva)

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_terceira_via.ogg`                                   |
| Duracao            | 0.8s                                                       |
| Volume             | 100%                                                       |
| Contexto           | Durante dash da Terceira Via.                              |
| Entonacao          | "Ha! Nao me pega!" Convicto de que foi genial. |
| Direcao de TTS     | Rapido, confiante, quase rindo. Voz de quem acha que venceu. |
| Efeitos            | Efeito de velocidade (pitch levemente pra cima por 0.3s).  |

### Interacao NPC

| Campo              | Valor                                                     |
|--------------------|------------------------------------------------------------|
| Arquivo            | `ciro_interacao_01.ogg` ate `ciro_interacao_05.ogg`       |
| Duracao            | 1.0-2.0s cada                                              |
| Volume             | 100%                                                       |
| Contexto           | Jogador se aproxima de Ciro no mapa.                      |
| Falas              |                                                            |
| 01                 | "Eu sou o unico que entende de economia aqui."            |
| 02                 | "Voces vao se arrepender de nao terem me escolhido."      |
| 03                 | "Alguem quer ouvir meu plano? ...Alguem? ...Ninguem?"    |
| 04                 | "Eu ja disse que sou o mais preparado?"                   |
| 05                 | "Quando eu for presidente... quer dizer, SE... NAO, QUANDO!" |
| Entonacao geral    | Arrogante, professoral, levemente desesperado por atencao. |

---

## SFX (EFEITOS SONOROS)

### Frasco de Rivotril

| Efeito             | Arquivo                | Duracao | Descricao                              |
|--------------------|------------------------|---------|----------------------------------------|
| Beber              | `sfx_rivotril_beber.ogg`| 0.5s   | "Glug glug" de liquido + suspiro aliviado |
| Frasco vazio       | `sfx_rivotril_vazio.ogg`| 0.3s   | Batida seca em vidro vazio             |
| Frasco quebrando   | `sfx_rivotril_quebra.ogg`| 0.6s   | Vidro estilhaçando + liquido espirrando|
| Clava (swing)      | `sfx_rivotril_swing.ogg`| 0.3s   | Whoosh pesado (frasco gigante no ar)   |
| Clava (impacto)    | `sfx_rivotril_impacto.ogg`| 0.4s  | Thud + vidro rachando + splash         |

### Cirocracia

| Efeito             | Arquivo                | Duracao | Descricao                              |
|--------------------|------------------------|---------|----------------------------------------|
| Formacao           | `sfx_cirocracia_forma.ogg`| 1.0s  | Energia crescente, hum eletrico        |
| Cupula ativa       | `sfx_cirocracia_hum.ogg`| (loop) | Zumbido constante, brilhante           |
| Rachaduras         | `sfx_cirocracia_crack.ogg`| 0.5s  | Vidro rachando lentamente              |
| Explosao           | `sfx_cirocracia_explode.ogg`| 0.8s| Estilhacar de energia + onda de choque |

### Rage

| Efeito             | Arquivo                | Duracao | Descricao                              |
|--------------------|------------------------|---------|----------------------------------------|
| Heartbeat rapido   | `sfx_rage_heartbeat.ogg`| (loop)  | Batimento cardiaco acelerado           |
| Onda de choque     | `sfx_rage_shockwave.ogg`| 0.5s   | Boom grave + vento                     |
| Estrelas (tontura) | `sfx_rage_stars.ogg`   | 1.0s    | "Tweet tweet" classico de cartoon      |

### Xingamento

| Efeito             | Arquivo                | Duracao | Descricao                              |
|--------------------|------------------------|---------|----------------------------------------|
| Onda sonora        | `sfx_xing_wave.ogg`   | 0.4s    | Blast de ar comprimido                 |
| Texto voando       | `sfx_xing_text.ogg`   | 0.3s    | Whoosh rapido (texto como projetil)    |
| Stun (impacto)     | `sfx_xing_stun.ogg`   | 0.5s    | Bonk + estrelas                        |

### Debate Unilateral

| Efeito             | Arquivo                | Duracao | Descricao                              |
|--------------------|------------------------|---------|----------------------------------------|
| Blabla loop        | `sfx_debate_blabla.ogg`| (loop)  | Murmuro de fala incompreensivel, rapido|
| Xicara             | `sfx_debate_cafe.ogg`  | 0.3s    | Ceramica batendo no pires              |
| Cafe espirrando    | `sfx_debate_splash.ogg`| 0.2s    | Splash pequeno de liquido              |

### Gerais

| Efeito             | Arquivo                | Duracao | Descricao                              |
|--------------------|------------------------|---------|----------------------------------------|
| Hit recebido       | `sfx_ciro_hit.ogg`    | 0.3s    | Thud + grunhido de raiva (nao dor)    |
| Passos (walk)      | `sfx_ciro_step.ogg`   | 0.15s   | Sapato social no asfalto. Rapido. Bravo.|
| Ressurreicao brilho| `sfx_ciro_ress.ogg`   | 1.0s    | Tom ascendente angelical (ironico)     |
| Suspiro (idle)     | `sfx_ciro_suspiro.ogg`| 0.5s    | Suspiro de frustração e desprezo       |

---

## TABELA DE PRIORIDADE DE AUDIO

Quando multiplos audios tentam tocar ao mesmo tempo:

| Prioridade | Audio                        | Pode ser interrompido por |
|------------|------------------------------|---------------------------|
| 1 (max)    | "Acabou meu Rivotril!"       | Nada                      |
| 2          | Death "pacoca..."            | Apenas prioridade 1       |
| 3          | Cirocracia (fala)            | Prioridade 1-2            |
| 4          | Xingamentos em combate       | Prioridade 1-3            |
| 5          | Debate Unilateral            | Prioridade 1-4            |
| 6          | Falas de contexto/idle       | Qualquer fala prioritaria |
| 7 (min)    | SFX ambientais               | Qualquer fala             |

**Regra**: NUNCA mais de 2 audios de Ciro simultaneos. Fala + 1 SFX maximo.

---

## CONFIGURACAO DE TTS / GRAVACAO

### Para geracao TTS (ElevenLabs / similar)

```
Voice characteristics:
- Gender: Male
- Age: 65-70
- Accent: Brazilian Portuguese (Ceara region, moderate)
- Tone: Authoritative, arrogant, perpetually angry
- Speed: 1.2x normal (fast talker)
- Pitch: Baritone, drops to bass when serious, rises to tenor when screaming
- Emotion range: irritated (base) -> furious -> panicked -> dazed
- Distinctive feature: Occasionally voice cracks when extremely angry
```

### Instrucoes de gravacao (se usar ator)

1. Ator deve imaginar que e o UNICO candidato inteligente numa sala de idiotas
2. Nunca esta calmo — minimo de irritacao e "desprezo contido"
3. Xingamentos sao ditos com CONVICÇÃO, nao com humor (o humor vem da situacao)
4. "Pacoca" deve parecer que o cerebro travou num loop
5. Cada ressurreicao deve ser MENOS convincente que a anterior
6. O "Que brisa, mano" e o UNICO momento de vulnerabilidade real
