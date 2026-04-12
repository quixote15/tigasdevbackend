# EDUARDO BOLSONARO (O Herdeiro / O Embaixador) -- Bordoes de Audio

**Voz**: Jovem, ligeiramente anasalada, sotaque paulista. Tom geral: filho mimado tentando parecer forte. Voz fina que tenta ser grave mas falha. Oscila entre crianca pedindo pro pai e macho alfa de internet.
**TTS Voice**: `pt-BR-AntonioNeural` -- ajustar pitch +4Hz para voz mais jovem, rate +10% para tom ansioso
**Alternativa**: Voice actor jovem (20-30 anos) com sotaque paulista, voz anasalada, inseguranca na entonacao

---

### 1. "Pai! Pai!"
- **Trigger**: hit (ao levar dano) / low_hp / situacao de perigo
- **Emocao**: Desespero de crianca, voz fina, panico regressivo -- toda a fachada de macho alfa desmorona
- **Volume**: 8/10
- **Duracao**: 0.8s
- **Frequencia**: Ao levar dano >15% HP / ao ficar com HP <30%
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Pai! Pai!" --rate "+20%" --pitch "+6Hz" --write-media eduardo-01-pai.mp3`
- **Efeitos de pos-producao**: Voz fina (pitch +6Hz), tom desesperado de crianca, leve crack vocal no segundo "Pai!"
- **URL referencia**: Meme "Eduardo Bolsonaro chamando o pai" -- compilacoes de dependencia paterna
- **Notas**: O bordao MAIS ICONICO do Eduardo. Toda vez que esta em perigo, regride a crianca. Voz fina, olhos arregalados, mao estendida na direcao do pai (mesmo que nao esteja no mapa).

### 2. "Posso pedir uma embaixada?"
- **Trigger**: idle / interact_npc / ao encontrar itens diplomaticos
- **Emocao**: Esperanca inocente, tom de quem pede presente de Natal, olhos brilhando
- **Volume**: 6/10
- **Duracao**: 2.0s
- **Frequencia**: Cada 30s em idle / ao interagir com NPCs
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Posso pedir uma embaixada?" --rate "+5%" --pitch "+4Hz" --write-media eduardo-02-embaixada.mp3`
- **Efeitos de pos-producao**: Tom esperancoso/inocente, leve sorriso na voz, entonacao ascendente no final (pergunta)
- **URL referencia**: Caso real da indicacao a embaixada dos EUA (2019) -- virou meme
- **Notas**: Referencia ao episodio real em que Eduardo quase foi indicado embaixador nos EUA. Tom de crianca pedindo brinquedo caro. Cada NPC que encontra, tenta pedir uma embaixada.

### 3. "Foi brilhante, pai!"
- **Trigger**: ally_buff / quando Bolsonaro (se presente) faz algo / pos-ataque de aliado
- **Emocao**: Puxa-saco absoluto, admiracao exagerada, bajulacao extrema
- **Volume**: 7/10
- **Duracao**: 1.2s
- **Frequencia**: Ao presenciar ataque de aliado / aleatoriamente quando perto de aliados
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Foi brilhante, pai!" --rate "+10%" --pitch "+4Hz" --write-media eduardo-03-brilhante.mp3`
- **Efeitos de pos-producao**: Tom de puxa-saco genuino, enfase em "brilhante", sorriso na voz
- **Notas**: Diz "pai" para qualquer aliado, nao so o Bolsonaro. Puxa-saquismo e reflexo pavloviano. Ate quando o aliado faz algo mediocre, Eduardo acha "brilhante".

### 4. "Manda grana pra mim, pai! Preciso fazer algo importantissimo aqui na Disney!"
- **Trigger**: idle / low_resources / ao gastar muito ammo/items
- **Emocao**: Tom de pedido natural, menciona Disney com total naturalidade como se fosse missao oficial
- **Volume**: 7/10
- **Duracao**: 3.0s
- **Frequencia**: Quando recursos estao baixos / cada 45s em idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Manda grana pra mim, pai! Preciso fazer algo importantissimo aqui na Disney!" --rate "+10%" --pitch "+4Hz" --write-media eduardo-04-disney.mp3`
- **Efeitos de pos-producao**: Tom de pedido casual, "Disney" dito com naturalidade total, como se fosse lugar de trabalho
- **URL referencia**: Viagens frequentes de Eduardo a Orlando/Disney -- meme
- **Notas**: A Disney e mencionada como se fosse quartel-general de operacoes diplomaticas. Para o Eduardo, "missao na Disney" e tao serio quanto operacao militar. Total falta de nocao.

### 5. "Pai, manda um audio pra minha namorada"
- **Trigger**: idle / interact_npc / momento de calma
- **Emocao**: Adolescente pedindo favor constrangedor, casualidade inapropriada
- **Volume**: 5/10
- **Duracao**: 2.0s
- **Frequencia**: Raro -- cada 50s em idle
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Pai, manda um audio pra minha namorada" --rate "+5%" --pitch "+4Hz" --write-media eduardo-05-namorada.mp3`
- **Efeitos de pos-producao**: Tom de adolescente casual, voz baixa como quem nao quer que os outros oucam
- **Notas**: Dito em meio ao apocalipse zumbi com total casualidade. Zero senso de urgencia. Prioridades: namorada > zumbis.

### 6. "Se o senhor nao me apoiar, vou pro Twitter fazer textao!"
- **Trigger**: hit / low_hp / quando aliado nao ajuda / rejeicao de buff
- **Emocao**: Ameaca infantil, birra de quem so tem redes sociais como arma
- **Volume**: 8/10
- **Duracao**: 2.5s
- **Frequencia**: Quando levar dano sem receber ajuda / cada 35s se ninguem esta perto
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Se o senhor nao me apoiar, vou pro Twitter fazer textao!" --rate "+10%" --pitch "+4Hz" --write-media eduardo-06-twitter.mp3`
- **Efeitos de pos-producao**: Tom de ameaca infantil crescente, enfase dramatica em "textao!", entonacao de ultimato
- **Notas**: A unica arma real do Eduardo: textao no Twitter. Tom de quem acha que isso e ameaca nuclear. Birra publica como estrategia politica.

### 7. "Comunismo vai voltar com forca!"
- **Trigger**: enemy_spawn / boss_appear / ver inimigos vermelhos
- **Emocao**: Paranoia conspiratoria, olhos arregalados, alarme ideologico
- **Volume**: 8/10
- **Duracao**: 2.0s
- **Frequencia**: Quando inimigos especiais aparecem / ao entrar em area nova
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Comunismo vai voltar com forca!" --rate "+15%" --pitch "+4Hz" --write-media eduardo-07-comunismo.mp3`
- **Efeitos de pos-producao**: Tom de paranoia urgente, voz acelerada, olhos arregalados na entonacao (pitch ligeiramente instavel)
- **URL referencia**: Posts e videos de Eduardo sobre ameaca comunista -- recorrente
- **Notas**: Cada zumbi e evidencia de que o comunismo voltou. Nao importa o contexto -- Eduardo ve comunismo em TUDO. Paranoia como worldview.

### 8. "Frouxo! Covarde! Fujao!"
- **Trigger**: hit (ao levar dano) / quando forcado a recuar / knock-back
- **Emocao**: Isto NAO e o Eduardo falando -- e o que a INTERNET grita pra ele. Audio de "haters"
- **Volume**: 7/10 (voz distorcida de multidao)
- **Duracao**: 1.5s
- **Frequencia**: 30% de chance ao levar dano / ao recuar
- **TTS Command**: `edge-tts --voice "pt-BR-AntonioNeural" --text "Frouxo! Covarde! Fujao!" --rate "+20%" --pitch "+2Hz" --write-media eduardo-08-haters.mp3`
- **Efeitos de pos-producao**: Voz DISTORCIDA como multidao/internet (multiplas vozes sobrepostas, leve distorcao de megafone, eco de rede social). NAO e a voz do Eduardo -- e a voz dos haters.
- **URL referencia**: Compilacoes de criticas a Eduardo -- xingamentos que recebe online
- **Notas**: Audio especial: NAO e o Eduardo falando. Sao vozes externas (internet/publico) gritando insultos. Quando toca, Eduardo faz cara de dor emocional. Mecanica: debuff psicologico.

---

## Variantes de Intensidade

| Bordao | Normal | Desesperado (low HP) |
|--------|--------|----------------------|
| "Pai! Pai!" | vol 7, 0.8s | vol 10, 1.2s, voz QUEBRANDO |
| "Posso pedir uma embaixada?" | vol 6, casual | vol 8, "POR FAVOR uma embaixada!" |
| "Comunismo vai voltar com forca!" | vol 7, paranoia leve | vol 9, HISTERIA total |
| "Frouxo! Covarde!" | vol 6, fundo | vol 9, ensurdecedor |

## Regras de Frequencia (Eduardo-Especificas)

1. **"Pai! Pai!"** e o bordao primario -- toca em QUALQUER situacao de perigo
2. **"Frouxo!"** (bordao 8) e audio EXTERNO -- voz de multidao, nao do Eduardo
3. Se Bolsonaro estiver no mesmo mapa, frequencia de "Pai!" triplica
4. **"Disney"** e **"namorada"** so tocam em idle -- nunca durante combate (prioridades erradas)
5. Eduardo tem os bordoes mais CURTOS do elenco -- fala rapido, pensa pouco

## Referencias de Audio Original
- Compilacoes "Eduardo Bolsonaro melhores momentos" -- YouTube
- Caso embaixada EUA (2019) -- reportagens e memes
- Viagens a Disney/Orlando -- fotos e memes
- Posts de Twitter do Eduardo -- tom e linguagem
- Andre Guedes: Serie "Zumbis em Brasilia"
