# DANIEL VORCARO - Especificacao de Animacoes

## Boss Nomeado / Vilao Real de 2026 - "Zumbis de Brasilia"

---

## Parametros Globais de Animacao

| Parametro             | Valor                                               |
|-----------------------|-----------------------------------------------------|
| Framerate base        | 8fps (jerky, twitchy)                               |
| Framerate ataque      | 10fps (ligeiramente mais rapido para impacto)       |
| Framerate death       | 6fps (mais lento, dramatico)                        |
| Estilo de movimento   | Controlado, confiante, NUNCA desajeitado            |
| Interpolacao          | NENHUMA -- snappy, frame a frame, sem tweening      |
| Deformacao organica   | Minima no corpo, MAXIMA nas expressoes e particulas |
| Easing                | Nao usar. Cortes secos entre frames                 |

---

## SISTEMA DE PARTICULAS: Dinheiro Flutuante (PERMANENTE)

Este sistema roda em PARALELO a todas as animacoes. Nunca para.

### Especificacao Tecnica

| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Quantidade            | 4-6 particulas simultaneas                         |
| Tipos                 | Nota R$100 (60%), moeda dourada (30%), cifrao (10%)|
| Tamanho nota          | 8x4px                                              |
| Tamanho moeda         | 4x4px                                              |
| Tamanho cifrao        | 6x8px                                              |
| Raio de orbita        | 20-28px do centro do sprite                        |
| Velocidade orbital    | 0.5 rotacao/segundo (idle), 2 rot/s (ataque)       |
| Oscilacao vertical    | +/- 3px, sinusoidal, periodo 2 segundos            |
| Opacidade             | 80-100%, variacao aleatoria                        |
| Rotacao individual    | Notas: 15 graus/frame. Moedas: 30 graus/frame     |

### Comportamento por Estado
- **IDLE**: Orbita lenta, calma. Particulas distantes do corpo
- **WALK**: Arrasto para tras (delay de 2 frames). Concentradas no lado traseiro
- **ATTACK**: Aceleradas, orbita caotica. Algumas sao "lancadas" como projeteis
- **HIT**: Varias caem para baixo, depois voltam a orbitar em 1 segundo
- **DEATH**: Pegam fogo individualmente, caem e viram cinza. NAO voltam

---

## SISTEMA: Brilho do Celular (PERMANENTE)

### Especificacao Tecnica

| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Posicao               | Mao esquerda, ~20px da base do sprite              |
| Tamanho da tela       | 6x8px visivel                                      |
| Cor da luz             | #00CCFF (azul-ciano)                              |
| Pulso                 | Opacidade 60-100%, ciclo de 1.5 segundos           |
| Blend mode            | Additive (soma de luz)                             |
| Raio de luz na pele   | 8px ao redor da mao, sutil                         |
| "Texto" rolando       | Linhas horizontais de 1px alternando em 2 cores    |

### Comportamento por Estado
- **IDLE**: Pulso suave e regular
- **WALK**: Leve tremor (simulando passo)
- **ATTACK**: Flash intenso no momento do impacto
- **SKILL (Celular Bomba)**: Brilho MAXIMO, ocupa 1/3 do sprite de luz
- **DEATH**: Celular cai. Tela pisca 3x e apaga. Depois explode em luz

---

## SISTEMA: Flash dos Dentes (PERMANENTE)

### Especificacao Tecnica

| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Intervalo             | A cada 12-16 frames (aleatorio dentro do range)    |
| Duracao do flash      | 2 frames                                           |
| Tipo                  | Ponto de brilho branco (#FFFFFF) sobre os dentes   |
| Posicao do flash      | Alterna entre dente esquerdo e direito             |
| Intensidade           | Frame 1: 100% opaco, 3px. Frame 2: 50%, 5px, fade |
| Blend mode            | Additive ou Screen                                 |

### Notas
- O flash dos dentes e a assinatura visual mais ICONICA do personagem
- Deve ser visivel mesmo durante acoes intensas
- Na death animation, o flash PARA e os dentes escurecem gradualmente

---

## SISTEMA: Cifroes nas Pupilas (PERMANENTE)

### Especificacao Tecnica

| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Tamanho de cada cifrao| 3x4px por olho                                     |
| Cor                   | #00CC00 (verde dinheiro) com borda #004400         |
| Rotacao               | 5 graus por frame, sentido horario                 |
| Brilho                | Pulso sutil a cada 20 frames                       |

### Comportamento por Estado
- **IDLE**: Rotacao lenta, calma
- **ATTACK**: Rotacao 3x mais rapida. Cifroes crescem 1px
- **SKILL (R$52 Bilhoes)**: Cifroes OCUPAM o olho inteiro (dobram de tamanho)
- **HIT**: Cifroes piscam em VERMELHO por 2 frames
- **DEATH**: Piscam como neon quebrado (on-off-on-off) e depois apagam

---

## SISTEMA: Dedos Contando (PERMANENTE)

### Especificacao Tecnica

| Parametro             | Valor                                              |
|-----------------------|----------------------------------------------------|
| Mao afetada           | Direita (a que nao segura o celular)               |
| Ciclo                 | 4 frames, loop continuo                            |
| Frame 1               | Dedos abertos, relaxados                           |
| Frame 2               | Polegar toca indicador                             |
| Frame 3               | Polegar toca medio                                 |
| Frame 4               | Polegar toca anelar, depois volta ao frame 1       |
| Sobreposicao          | Este ciclo roda SOBRE qualquer animacao principal   |
| Excecoes              | Para durante skills que usam ambas as maos          |

---

## ANIMACAO 1: IDLE

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 4                              |
| FPS           | 8                              |
| Loop          | Sim, infinito                  |
| Direcoes      | 4 (frente, costas, esquerda, direita) |

### Descricao Frame a Frame

**Frame 1 (base)**:
- Postura ereta, ombros abertos, confiante
- Sorriso largo, dentes brilhantes
- Cifroes nas pupilas posicao 0 graus
- Celular na mao esquerda, tela acesa
- Particulas de dinheiro: posicoes 0, 60, 120, 180, 240, 300 graus

**Frame 2 (+125ms)**:
- FLASH dos dentes (ponto de brilho)
- Cifroes giram 15 graus
- Dedos mao direita: polegar-indicador
- Celular: mesmo brilho
- Particulas: avancam 15 graus na orbita, nota mais alta sobe 1px

**Frame 3 (+250ms)**:
- Dentes voltam ao brilho normal
- Cifroes giram mais 15 graus (total 30)
- Celular: PULSO de luz (opacidade 100%)
- Dedos: polegar-medio
- Sobrancelha esquerda levanta 1px (arrogancia sutil)
- Particulas: avancam mais 15 graus, moeda gira

**Frame 4 (+375ms)**:
- Cifroes giram mais 15 graus (total 45)
- Dedos: polegar-anelar (completa gesto "contar")
- Celular: opacidade volta a 60%
- Sobrancelha volta
- Particulas: completam segmento, volta ao frame 1

---

## ANIMACAO 2: WALK

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 6                              |
| FPS           | 8                              |
| Loop          | Sim, durante movimento         |
| Direcoes      | 4                              |

### Descricao Frame a Frame

**Frame 1**: Pe direito avanca. Corpo inclina 2 graus frente. Celular na mao. Particulas concentram atras
**Frame 2**: Peso transfere para pe direito. Sapato brilha (flash no pixel). Sorriso estavel
**Frame 3**: Pe esquerdo avanca. Dentes fazem FLASH. Celular oscila levemente
**Frame 4**: Peso no pe esquerdo. Dedos contam no ar. Particulas reagrupam
**Frame 5**: Pe direito levantando. Celular faz flash de notificacao. Sorriso se abre mais 1px
**Frame 6**: Transicao. Particulas completam reposicionamento. Pronto para loop

### Notas de Movimento
- Caminhada CONFIANTE. Nunca corre. Nunca tropeça. Passos firmes
- O corpo quase nao balanca verticalmente (bounce minimo de 1px). Ele DESLIZA com superioridade
- Olha para o celular a cada 2 ciclos (vira cabeca 10 graus para esquerda)
- Particulas de dinheiro ficam com "rastro" -- delay de 2 frames no reposicionamento

---

## ANIMACAO 3: ATAQUE BASICO

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 8                              |
| FPS           | 10                             |
| Loop          | Nao, single shot               |
| Direcoes      | 4                              |

### Sequencia
1. **Windup** (frames 1-2): Ergue celular, mostra tela. Particulas aceleram
2. **Flash** (frames 3-4): Tela do celular faz flash branco-azulado. Brilho cobre 1/4 do sprite
3. **Disparo** (frames 5-6): Onda de notas dispara para frente. 3-4 notas como projeteis. Knockback visual
4. **Recovery** (frames 7-8): Retorna a pose. Sorriso mais largo. Cifroes giram rapido 1 frame. Novas particulas surgem para repor as lancadas

### Projeteis Gerados
- 3x Nota R$100 em chamas (32x32px, velocidade 120px/s, dano base)
- Direcao: frente do personagem, spread de 15 graus

---

## ANIMACAO 4: SKILL "R$52 Bilhoes" (Area)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 12                             |
| FPS           | 10                             |
| Loop          | Nao, single shot               |
| Cooldown      | 8 segundos                     |
| Area de efeito| 160x160px (centro no personagem)|

### Sequencia Detalhada

**Preparacao (frames 1-3)**:
- Frame 1: Bracos abrem lateralmente. Celular flutua (solta da mao, fica ao lado). Aura dourada comeca
- Frame 2: Bracos sobem acima da cabeca. Aura dourada INTENSA. Todas as particulas aceleram para cima
- Frame 3: Expressao muda de sorriso para GARGALHADA (boca 2x maior). Veias de ouro aparecem no chao

**Climax (frames 4-5)**:
- Frame 4: Cifroes nos olhos CRESCEM (2x tamanho normal, ocupam olho inteiro). Brilho verde intenso nos olhos. Tela do celular flutuante mostra "R$ 52.000.000.000"
- Frame 5: SHAKE de tela (screen shake de 3px por 200ms). Chao racha com simbolos $. Flash BRANCO de 1 frame

**Explosao (frames 6-8)**:
- Frame 6: EXPLOSAO de notas em 360 graus. 20+ notas disparam. Moedas douradas em onda concentrica
- Frame 7: Segunda onda de notas. Particulas de ouro enchem a tela. Tudo sacudindo
- Frame 8: Terceira onda menor. Confete de dinheiro no ar

**Recovery (frames 9-12)**:
- Frame 9: Notas comecam a cair como chuva
- Frame 10: Vorcaro pega celular de volta. Mao esquerda
- Frame 11: Ajusta gravata com mao direita. Sorriso satisfeito
- Frame 12: Volta a idle. Particulas orbitais se reconstituem. Chuva de notas termina

---

## ANIMACAO 5: SKILL "Delacao Premiada" (Debuff Global)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 10                             |
| FPS           | 8                              |
| Loop          | Nao, trigger unico (ao ser derrotado) |
| Efeito        | -20% defesa em todos os bosses  |

### Sequencia

**Frames 1-2**: Cai de joelhos ESTRATEGICAMENTE (nao e derrota, e NEGOCIACAO). Sorriso permanece. Ergue celular como oferenda

**Frames 3-4**: Celular projeta holograma:
- Teia de linhas VERMELHAS conectando silhuetas de outros bosses
- Cada silhueta tem mini-icone identificavel (toga do Xandao, microfone do Nikolas, etc.)
- A teia PULSA como batimento cardiaco

**Frames 5-6**: 
- Linhas vermelhas EXPLODEM (fragmentam em particulas)
- Flash vermelho em cada silhueta conectada
- Balao de fala: "Quem eu entrego primeiro?"
- Notas flutuantes congelam no ar por 1 frame

**Frames 7-8**:
- Ondas de choque (circulos concentricos vermelhos) emanam do celular
- Selo "DELACAO PREMIADA" (texto em caixa vermelha com borda amarela) aparece acima da cabeca
- Cada boss no mapa recebe icone de "escudo rachado" sobre a cabeca

**Frames 9-10**:
- Vorcaro se levanta CALMAMENTE
- Ajusta terno
- Celular guarda no bolso (pela primeira e unica vez)
- Sorriso: o MAIS largo do jogo inteiro. Ele acabou de destruir todo mundo

---

## ANIMACAO 6: SKILL "Celular Bomba" (Paralisia 3s)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 10                             |
| FPS           | 10                             |
| Loop          | Nao, single shot               |
| Cooldown      | 12 segundos                    |
| Range         | 120px raio                     |

### Sequencia

**Frames 1-2**: Ergue celular acima da cabeca com AMBAS as maos (para de contar dinheiro). Tela brilha branco

**Frames 3-4**: 
- Ondas sonicas (circulos concentricos azul-ciano) emanam do celular, expandindo
- Onda 1: raio 20px. Onda 2: raio 40px
- Icones escapam da tela: miniatura WhatsApp, chamada telefonica, foto, PDF

**Frames 5-7**:
- Bolhas de "mensagens" explodem pelo ar (8-12 bolhas pequenas, 4x3px cada)
- Cada bolha tem linhas horizontais imitando texto
- Inimigos dentro do raio: sprite congela, expressao muda para PANICO
- Olhos dos inimigos paralisados: arregalam 2px
- Ondas sonicas atingem raio maximo (120px)

**Frames 8-9**:
- Simbolo de cadeado ABERTO (verde, 8x8px) aparece sobre cada inimigo paralisado
- Bolhas de mensagem flutuam para cima e somem (fade out)
- Vorcaro abaixa celular

**Frame 10**:
- Guarda celular na mao esquerda (posicao padrao)
- Volta a pose idle
- Sorriso presunçoso

---

## ANIMACAO 7: SKILL "Captura Financeira" (Corrupcao)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 12                             |
| FPS           | 10                             |
| Loop          | Nao, single shot               |
| Cooldown      | 15 segundos                    |
| Range         | 80px, alvo unico               |

### Sequencia

**Frames 1-3**:
- Frame 1: Mao direita para de contar. Dedos se posicionam para estalar
- Frame 2: ESTALO (particula visual: estrela amarela 4px entre dedos)
- Frame 3: Particulas de dinheiro que orbitavam Vorcaro DISPARAM em direcao ao alvo

**Frames 4-6**:
- Frame 4: Notas adicionais surgem do nada, convergem no alvo
- Frame 5: TORNADO de dinheiro envolve o inimigo alvo (rotacao de notas ao redor, 8 notas em espiral)
- Frame 6: Tornado no ponto maximo. Inimigo invisivel dentro do tornado

**Frames 7-9**:
- Frame 7: Tornado se dissipa. Inimigo revelado com mudancas: olhos agora com cifroes ($), aura dourada
- Frame 8: Barra de vida do inimigo muda de cor (vermelho/verde -> dourado)
- Frame 9: Inimigo se reposiciona, caminhando para ENTRE Vorcaro e o jogador

**Frames 10-12**:
- Frame 10: Inimigo corrompido assume posicao de guarda-costas
- Frame 11: Vorcaro cruza os bracos
- Frame 12: Novas particulas de dinheiro surgem para repor as usadas. Idle com bracos cruzados (variacao)

---

## ANIMACAO 8: HIT/DAMAGE

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 4                              |
| FPS           | 12 (rapido)                    |
| Loop          | Nao, single shot               |

### Sequencia

**Frame 1**: Flash VERMELHO sobre o sprite inteiro (overlay vermelho 30% opacidade). Sorriso se CONTORCE (nao desaparece, apenas distorce)
**Frame 2**: Recuo de 4px para tras. 2-3 particulas de dinheiro CAEM (perdem orbita). Celular tremula na mao
**Frame 3**: Cifroes nos olhos piscam em VERMELHO (#CC0000) por 1 frame. Marca de impacto visivel no terno (rasgo, 2px)
**Frame 4**: Recupera posicao. Terno "se conserta" (magicamente). Sorriso volta a FULL FORCE. Particulas caidas voltam a orbitar

### Nota Critica
- O sorriso NUNCA desaparece quando toma dano. Ele se distorce, contorce, mas permanece
- Isso comunica: "voce nao pode me machucar de verdade"

---

## ANIMACAO 9: DEATH

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 12                             |
| FPS           | 6 (lento, dramatico)           |
| Loop          | Nao, single shot + hold ultimo frame |

### Sequencia Detalhada

**Fase 1: Choque (frames 1-3)**:
- Frame 1: UNICO momento de surpresa GENUINA. Olhos arregalados. Boca FECHA (sorriso desaparece pela primeira vez). Cifroes piscam
- Frame 2: Celular escorrega da mao, cai. Trilha: celular caindo em slow motion
- Frame 3: Terno comeca a perder cor. Riscas douradas -> cinza. Particulas de dinheiro CONGELAM no ar

**Fase 2: Desintegracao (frames 4-7)**:
- Frame 4: Celular atinge o chao. EXPLODE em fragmentos de luz. Conversas vazam como fantasmas (silhuetas luminosas subindo)
- Frame 5: Notas flutuantes PEGAM FOGO individualmente (de fora para dentro da orbita)
- Frame 6: Moedas DERRETEM (deformam para baixo, viram poças douradas). Dentes perdem brilho (de branco para amarelo para cinza)
- Frame 7: Cifroes nos olhos fazem "efeito neon quebrado" -- on, off, on, off, APAGAM. Pupilas normais aparecem pela unica vez (pretas, humanas, com MEDO)

**Fase 3: Colapso (frames 8-10)**:
- Frame 8: Corpo ENCOLHE dentro do terno (como se o dinheiro fosse o que o mantinha grande). Terno fica folgado, pendurado
- Frame 9: Pele fica cinza. Gel do cabelo derrete. Cabelo desmancha. Ainda de pe, mas cambaleando
- Frame 10: COLAPSA. Cai para frente. Terno vazio pousa no chao

**Fase 4: Aftermath (frames 11-12)**:
- Frame 11: Pilha de cinzas dentro do terno vazio. Celular destruido (tela rachada, sem luz). Ultimas notas caindo do ar
- Frame 12 (HOLD): Ultima nota de R$ cai em camera lenta. Toca as cinzas. Pega fogo. Vira cinza. Texto aparece: "R$52 bilhoes em fumaca". Silencio. Hold indefinido

---

## ANIMACAO 10: TAUNT/PROVOCACAO (Pre-batalha)

| Campo         | Valor                          |
|---------------|--------------------------------|
| Frames        | 6                              |
| FPS           | 8                              |
| Loop          | Nao, single shot               |

### Sequencia

**Frame 1**: Tira celular do bolso (posicao especial -- normalmente ja esta na mao)
**Frame 2**: Mostra tela para o jogador. Tela exibe lista de nomes (barras horizontais representando nomes)
**Frame 3**: GARGALHADA. Boca abre 2x. Dentes flasham INTENSO. Cabeca tilt para tras
**Frame 4**: Notas EXPLODEM para cima como confete. 12+ notas. Moedas chovem
**Frame 5**: Aponta para o jogador com indicador da mao direita. Dedo faz gesto de "contar"
**Frame 6**: Balao de fala: "Eu conheco TODO MUNDO." Volta a idle

---

## Transicoes entre Animacoes

| De           | Para          | Transicao                                         |
|-------------|---------------|---------------------------------------------------|
| IDLE        | WALK          | Imediata (0 frames). Snap para walk frame 1       |
| WALK        | IDLE          | 1 frame de desaceleracao. Particulas se reajustam  |
| IDLE/WALK   | ATTACK        | Imediata. Particulas aceleram instantaneamente     |
| ATTACK      | IDLE          | 2 frames de recovery (ja no ataque)               |
| IDLE        | SKILL         | 1 frame preparatorio (bracos abrem)               |
| SKILL       | IDLE          | Incluido nos ultimos frames da skill              |
| ANY         | HIT           | Interrompe QUALQUER animacao imediatamente         |
| HIT         | IDLE          | Apos frame 4, volta ao estado anterior             |
| ANY         | DEATH         | Interrompe tudo. Unica animacao nao-interrompivel  |
| CUTSCENE    | TAUNT         | Disparada por trigger de inicio de batalha         |

---

## Screen Shake e Efeitos Globais

| Animacao          | Screen Shake | Flash de Tela | Slowdown     |
|-------------------|-------------|---------------|--------------|
| R$52 Bilhoes      | 3px, 200ms  | Branco, 50ms  | Nenhum       |
| Delacao Premiada   | 2px, 150ms  | Vermelho, 80ms| 0.5x por 500ms |
| Celular Bomba      | 1px, 100ms  | Azul, 60ms   | Nenhum       |
| Captura Financeira | Nenhum      | Dourado, 40ms | Nenhum       |
| Death              | 4px, 300ms  | Nenhum        | 0.3x por 1s  |

---

## Prioridade de Renderizacao (Z-Order)

1. (atras) Background / Arena
2. Particulas de dinheiro (camada traseira, 50% das particulas)
3. Sprite do personagem
4. Celular + brilho (blend additive)
5. Particulas de dinheiro (camada frontal, 50% das particulas)
6. Efeitos de skill (ondas, explosoes, hologramas)
7. Flash dos dentes (blend additive/screen)
8. UI de barra de vida / nome
9. (frente) Baloes de fala / texto de bordao
