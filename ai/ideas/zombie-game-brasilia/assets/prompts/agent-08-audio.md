Voce e um agente de arte do time "Zumbis de Brasilia". Seu trabalho e criar TODOS os assets de AUDIO: bordoes, SFX, musica ambiente e scripts TTS.

## Categorias de Audio

### 1. BORDOES DOS PERSONAGENS (vozes)
Para CADA personagem, crie script de audio com:
- Texto exato do bordao
- Emocao/tom (grito, sussurro, sarcastico, desesperado, etc.)
- Volume relativo (1-10)
- Duracao estimada
- Quando toca no jogo (idle, attack, death, spawn, special)
- Comando TTS para gerar (edge-tts, bark, ou instrucoes para voice actor)

**Personagens prioritarios (MVP):**
1. LULA: "Eu quero dizer pra voces...", "Companheiro alcool em mim!", "Ta maravilhoso!", "A culpa e do Bolsonaro", "Faz o L!", "Nunca antes na historia", "Fico puto da vida!", "A gente vamos..."
2. BOLSONARO: "TALKEI?", "Bomba!", "Vagabundo! Canalha!", "E dai? Lamento.", "So uma gripezinha!", "Imbrochavel!", "Pintou um clima..."
3. DACIOLO: "GLORIA A DEUS!" (VARIAS intensidades: sussurro, normal, GRITO COSMICO), "Queima Jesus! Shabalaba!", "Sinto o cheiro de Satanas!", "A URSAL EXISTE!", "Gloria a sap— opa, Gloria a Deus!" (falha 10%)
4. XANDAO: "Monocraticamente!", "Faz silencio!", "Censurado!", "Xandaquistao!"
5. CIRO: "Acabou meu Rivotril!", "Bossaloide!", "Pacoca", "Eu tenho um plano!", "Que brisa mano"
6. TAXADD: "TAXADO!", "Nao e imposto, e contribuicao!", "Que horas e a merenda?"
7. TRUMP: "TREMENDOUS!", "FAKE NEWS!", "Very good companheiro!", "Trampi!"
8. ENEAS: "MEU NOME E ENEAS!" (EPICO com reverb), "MEU NUMERO E CINQUENTA E SEEEEIS!"
9. GILMAR: Tudo repetido 3x: "Sou fa, sou fa, sou fa", "Vagabundo! x3", "Pastel pastel pastel"
10. EDUARDO: "Pai! Pai!", "Posso pedir embaixada?"
11. MONARK: "Mano pensa comigo...", "Bem-vindo ao Limbo"
12. JANJA: "FORA ELON MUSK!" (grito mundial), "Quem manda aqui sou eu, amor"

### 2. SFX (Efeitos Sonoros)
Crie specs para gerar ou buscar:
- **Armas**: THWACK (chinelo), SWOOSH (vassoura), CLINK-BROCHA (arma falhando), CRASH (garrafa), GAVEL-SLAM (martelo), HOLY-WIND (fumaca santa)
- **Impactos**: Hit flesh, hit metal (armadura senador), hit paper (santinho), explosion (molotov cachaca)
- **UI**: Score up, combo multiplier, wave start, wave end, game over, level up
- **Zumbis genericos**: Gemidos de "fui eleito democraticamente", "merenda", "emenda", grunhidos burocraticos
- **Ambiente**: AC zumbindo, alarmes distantes, papel voando no vento
- **Especiais**: Fusao BolsoLula (body horror sound), Eneas aparicao (coro celestial + trovao), Censura Xandao (static + silencio)

### 3. MUSICA AMBIENTE
- **Gameplay normal**: Loop tenso-comico, percussao brasileira distorcida, berimbau eletronico, maracatu sinistro
- **Boss fight**: Intensificacao — adicionar jingle de campanha distorcido, bateria mais pesada
- **Game Over / Limbo**: Podcast ambient, lo-fi beats, silencio existencial
- **Tela de titulo**: Hino Nacional do Brasil tocado em orgao de igreja gotico, distorcido

## Instrucoes

### Passo 1: Pesquisa Web
- "Andre Guedes zumbis brasilia audio bordoes"
- "Andre Guedes [personagem] fala bordao" (para cada)
- "Lula companheiro audio meme"
- "Bolsonaro talkei audio original"
- "Daciolo gloria a deus audio"
- "Eneas meu nome e eneas audio original"
- "Ciro gomes rivotril audio"
- "Janja fora elon musk audio g20"
- "Gilmar mendes vagabundo audio stf"
- "edge-tts portuguese brazil voices"
- "bark text to speech portuguese"
- "free game sfx generator"

### Passo 2: Leia Documentos
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/research/personagens/top_20_personagens.md` (INTEIRO — todos os bordoes)
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/09-storytelling-art-direction.md` (secao de atmosfera sonora)
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/research/personagens/avaliacao_andre_guedes.md`
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/assets/prompts/context-base.md`

### Passo 3: Gere Assets

**Em `assets/audio/bordoes/`:**
Para CADA personagem crie `[nome]-bordoes.md`:
```
## [Nome do Personagem] — Bordoes

### 1. "[texto]"
- Trigger: [quando toca — idle/attack/spawn/death/special]
- Emocao: [tom]
- Volume: [1-10]
- Duracao: [estimada em segundos]
- Frequencia: [cada Xs / unica / aleatoria]
- TTS Command: `edge-tts --voice "pt-BR-AntonioNeural" --text "[texto]" --rate "+10%" --pitch "+5Hz" --write-media [nome]-01.mp3`
- URL referencia: [se encontrou audio original online]
- Notas: [contexto, variantes]
```

**Em `assets/audio/sfx/`:**
- `sfx-catalog.md`: Catalogo completo de efeitos sonoros com descricao, trigger, duracao
- `sfx-generation.md`: Scripts/comandos para gerar SFX (ffmpeg, sox, sfxr, etc.)

**Em `assets/audio/ambiente/`:**
- `ambient-spec.md`: Loops de ambiente, layers, mixing
- `music-spec.md`: Specs de musica (BPM, instrumentos, mood, referencia)

**Em `assets/audio/musica/`:**
- `soundtrack-spec.md`: Trilha por cena (gameplay, boss, limbo, titulo)

### PRIORIDADE: Scripts TTS Executaveis
Crie um script Python `generate_bordoes.py` em `assets/audio/` que:
1. Usa `edge-tts` (pip install edge-tts) 
2. Gera TODOS os bordoes automaticamente
3. Salva MP3 organizados por personagem
4. Inclui variantes de intensidade (sussurro, normal, grito)
5. Vozes brasileiras masculinas e femininas conforme personagem

### Tambem busque audios ORIGINAIS
Muitos bordoes existem como audio real (discursos, memes). Busque URLs de:
- Compilacoes de falas reais dos politicos
- Memes com audio editado
- Videos do Andre Guedes com os bordoes
Documente tudo para que a equipe possa baixar os originais.

Trabalhe em `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/`.
