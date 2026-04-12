# Ciro Gomes - Especificacao de Animacoes

## MAQUINA DE ESTADOS (State Machine)

```
                    +---------+
                    |  SPAWN  |
                    +----+----+
                         |
                         v
              +----------+----------+
              |        IDLE         |<-----------+
              | (estado padrao)     |            |
              +--+---+---+---+---+-+            |
                 |   |   |   |   |              |
     +-----------+   |   |   |   +----------+  |
     v               v   v   v              v  |
  +--+---+    +-----++ +-+--+ +------+ +---+--+
  | WALK |    |ATTACK| | HIT| |DEATH | |SPECIAL|
  +--+---+    +--+---+ +-+--+ +--+---+ +---+---+
     |           |        |       |         |
     +-----------+--------+       |         |
           |                      v         |
           |              +-------+------+  |
           |              | CANDIDATURA  |  |
           |              | ETERNA       |--+
           |              | (ressurreicao)|
           |              +--------------+
           |
           +----> volta pra IDLE
```

---

## TABELA MESTRA DE ANIMACOES

| Animacao             | Frames | FPS | Duracao Total | Loop  | Prioridade | Interruptivel |
|---------------------|--------|-----|---------------|-------|------------|---------------|
| Idle                | 4      | 8   | 0.500s        | Sim   | 0 (base)   | Sim           |
| Walk                | 6      | 10  | 0.600s        | Sim   | 1          | Sim           |
| Attack              | 3      | 12  | 0.250s        | Nao   | 3          | Nao           |
| Death               | 4      | 6   | 0.667s        | Nao   | 5 (max)    | Nao           |
| Hit                 | 2      | 12  | 0.167s        | Nao   | 4          | Nao           |
| Cirocracia          | 8      | 8   | 1.000s        | Nao   | 3          | Nao           |
| Rage do Rivotril    | 6      | 10  | 0.600s        | Nao   | 4          | Nao           |
| Candidatura Eterna  | 4      | 6   | 0.667s        | Nao   | 5 (max)    | Nao           |
| Debate Unilateral   | 4      | 8   | 0.500s        | Nao   | 2          | Sim           |
| Xingamento Erudito  | 4      | 10  | 0.400s        | Nao   | 3          | Nao           |
| Terceira Via        | 4      | 12  | 0.333s        | Nao   | 3          | Nao           |

---

## DETALHAMENTO POR ANIMACAO

### 1. IDLE (Loop)

**Conceito**: Ciro parado, impaciente, arrogante, tremendo levemente se Rivotril estiver baixo.

```
Frame 1 (0.000s - 0.125s)
  - Pose base: pe esquerdo levemente a frente
  - Queixo levantado (arrogancia)
  - Mao esquerda: segura Rivotril no nivel do peito
  - Braco direito: livro debaixo do braco
  - Veias: estado normal (largura 1px)
  - Rosto: cor baseada no nivel de Rivotril
  - Micro-movimento: nenhum

Frame 2 (0.125s - 0.250s)
  - Corpo inclina 1px pra frente (quer falar)
  - Boca entreaberta
  - Sobrancelha levanta 1px
  - Veias pulsam (largura 1.5px por 1 frame)
  - Mao do Rivotril: estavel

Frame 3 (0.250s - 0.375s)
  - Volta a posicao base
  - Mao do Rivotril: tremor de 1px (offset aleatorio X ou Y)
  - Olhar: impaciente, olha pro lado
  - Se Rivotril < 50%: tremor aumenta pra 2px

Frame 4 (0.375s - 0.500s)
  - Ombros sobem 1px (inspirando)
  - Ombros descem 1px (suspiro de desprezo)
  - Expressao: narinas dilatadas
  - Veias: voltam ao normal
```

**Variacao por nivel de Rivotril:**
- 100-75%: Idle normal como descrito
- 75-50%: Adicionar tremor constante de 1px em todos os frames
- 50-25%: Tremor 2px, rosto vermelho em todos os frames, veias sempre dilatadas
- 25-0%: Tremor 3px, rosto berrante, veias maximais, suor (particulas) em todos os frames

---

### 2. WALK (Loop)

**Conceito**: Caminhada apressada, irritada. Ciro anda como quem esta ATRASADO pra um debate que ninguem quer ver.

```
Frame 1 (0.000s - 0.100s)
  - Perna esquerda a frente (contato do pe)
  - Braco direito balanca pra tras (oposto)
  - Tronco levemente inclinado pra frente
  - Rivotril no bolso do terno (nao na mao)
  - Terno estica nos ombros (tensao)

Frame 2 (0.100s - 0.200s)
  - Transicao: pernas quase juntas
  - Corpo no ponto mais alto do passo (sobe 1px)
  - Bracos proximos ao corpo

Frame 3 (0.200s - 0.300s)
  - Perna direita a frente
  - Braco esquerdo balanca pra tras
  - Gravata move 1px na direcao do movimento
  - Livro escorrega levemente (offset 1px)

Frame 4 (0.300s - 0.400s)
  - Transicao: passo largo, agressive
  - Cabeca inclinada: queixo pra cima
  - Expressao impaciente

Frame 5 (0.400s - 0.500s)
  - Perna esquerda a frente de novo
  - Livro prestes a cair (offset 2px)
  - Mao direita ajustando livro

Frame 6 (0.500s - 0.600s)
  - Transicao rapida: quadro de blur
  - Pernas em movimento rapido
  - Efeito: 1px de motion blur nas pernas (pixel duplicado atras)
```

**Direcoes**: 4 sets de sprites (S, N, E, W). Espelhamento horizontal para E/W se possivel.

---

### 3. ATTACK - Frasco de Rivotril Turbo

**Conceito**: Swing de clava com o frasco gigante. Rapido, furioso, se machuca no processo.

```
Frame 1 - Windup (0.000s - 0.083s)
  - Braco direito levanta frasco acima da cabeca
  - Frasco: tamanho 16x20px (GIGANTE comparado ao sprite)
  - Corpo inclina pra tras 2px (contra-peso)
  - Rosto: #CC3333 (vermelho irritado)
  - Veias: dilatadas ao maximo
  - Boca: aberta, gritando

Frame 2 - Swing (0.083s - 0.167s)
  - Braco desce em arco
  - Frasco no ponto mais baixo
  - Motion trail: 2px de afterimage atras do frasco
  - Corpo segue o swing (inclina pra frente)
  - Veias: MAXIMAIS
  - Particulas: gota de liquido azul (#00BFFF) sai do frasco

Frame 3 - Impact (0.167s - 0.250s)
  - Frasco atinge alvo (ou chao)
  - Ondas de impacto: 3 circulos concentricos (2px, 4px, 6px raio)
  - Liquido espirra: 3-4 goticulas azuis voam em direcoes radiais
  - Rosto: satisfeito por 1 frame (meio sorriso perverso)
  - Tela treme 1px (screen shake sugerido)
```

**Evento de dano**: Frame 3 dispara hitbox. Raio: 16px do centro do frasco.
**Efeito no inimigo**: Sedacao (-50% velocidade por 3s).

---

### 4. DEATH - Pacoca Mental

**Conceito**: Morte em 4 fases + periodo de "pacoca" + trigger de Candidatura Eterna.

```
Frame 1 - Impacto (0.000s - 0.167s)
  - Corpo jogado pra tras 4px
  - Bracos abertos em X
  - Rivotril VOA da mao (spawn projetil separado: frasco girando 32x32, 4 frames rotacao)
  - Livro cai (projetil separado: livro 10x8 caindo)
  - Expressao: choque total, olhos arregalados
  - Flash branco: 50% opacity, 1 sub-frame

Frame 2 - Desabando (0.167s - 0.333s)
  - Joelhos dobram (pernas encurtam 4px)
  - Terno amassa: linhas de dobra aparecem
  - Rosto TRAVA numa expressao VAZIA (olhos arregalados, boca aberta)
  - Gravata solta: pende pro lado
  - Corpo inclina pro lado

Frame 3 - No chao (0.333s - 0.500s + EXTENDED 1.5s)
  - Corpo de lado no chao
  - Boca se move (2 sub-frames alternando boca aberta/fechada)
  - Bolha de fala aparece: "pacoca..." (sprite 16x10px acima)
  - Veias ainda pulsando fracamente (1px, ritmo lento)
  - DURACAO EXTENDIDA: este frame fica por 1.5 segundos

Frame 4 - Fade (0.500s + 1.5s, duracao 1.5s)
  - Mesma pose do Frame 3
  - Olhos fechando (2 sub-frames)
  - Bolha "pacoca..." fica alpha 50% -> 0%
  - Veias param de pulsar
  - Cores do sprite inteiro: dessaturam 20% gradualmente
  - Corpo inteiro: alpha 255 -> 100 gradualmente
  - DURACAO EXTENDIDA: 1.5 segundos

TOTAL DEATH: ~0.5s animacao + 3.0s de "pacoca" no chao = 3.5 segundos

TRIGGER: Ao completar frame 4, dispara Candidatura Eterna (ressurreicao) apos 1s de delay.
```

---

### 5. HIT

**Conceito**: Knockback com xingamento imediato. Fica MAIS irritado, nunca MENOS.

```
Frame 1 - Recuo (0.000s - 0.083s)
  - Corpo deslocado 2px na direcao oposta ao ataque
  - Flash branco: overlay 80% opacity por este frame
  - Rosto: instantaneamente #CC3333
  - Boca: aberta (gritando xingamento)
  - Rivotril quase cai: offset 2px, angulo inclinado
  - Bracos: jogados pra tras

Frame 2 - Recuperacao (0.083s - 0.167s)
  - Volta a posicao original
  - MAIS IRRITADO que antes:
    - Veias 1.5x mais grossas que pre-hit
    - Rosto #FF2222 (mais vermelho)
    - Punho cerrado
    - Sobrancelha mais franzida
  - Rivotril volta a posicao
```

**Efeito persistente**: Apos hit, o nivel de "irritacao visual" aumenta por 2 segundos.

---

### 6. CIROCRACIA (Cupula de Energia)

**Conceito**: Ciro cria campo de forca pessoal. Ninguem entra, ele nao sai. Eventualmente se autodestroi.

```
Frame 1 (0.000s - 0.125s) - Invocacao
  - Ciro levanta os bracos, palmas pra cima
  - Particulas azuis (#4169E1, alpha 150) surgem no chao
  - 6-8 particulas, 2x2px cada, spawn aleatorio dentro de 8px do pe
  - Rosto: concentrado, olhos fechados

Frame 2 (0.125s - 0.250s) - Energia Sobe
  - Particulas sobem em espiral (trajetoria helicoidal)
  - Terno tremula: 1px de distorcao nas bordas
  - Cabelo arrepia levemente: 1px pra cima
  - Linhas de energia verticais (1px wide, #4169E1 alpha 100) ao redor

Frame 3 (0.250s - 0.375s) - Cupula Forma (inicio)
  - Semi-esfera comeca a se materializar
  - Diametro: 48px (3/4 do max)
  - Cor: #4169E1 alpha 80
  - Borda: 1px mais brilhante (#6495ED)
  - Ciro dentro: pose de expectativa

Frame 4 (0.375s - 0.500s) - Cupula Completa
  - Semi-esfera completa: 56x56px
  - Cor: #4169E1 alpha 100
  - Borda pulsante: alterna entre #4169E1 e #6495ED
  - Ciro dentro: bracos cruzados, pose "eu sei de tudo"
  - Queixo levantado ao maximo
  - Hitbox ATIVA: repele tudo (aliados E inimigos)

Frame 5 (0.500s - 0.625s) - Cupula Pulsa
  - Cupula expande 2px (58x58) e contrai 2px (54x54) no mesmo frame
  - Particulas circulam na borda (4-6, orbitando)
  - Inimigos proximos: empurrados 4px pra fora
  - Aliados proximos: tambem empurrados (Ciro nao diferencia)
  - Ciro: satisfeito dentro

Frame 6 (0.625s - 0.750s) - Rachaduras
  - Cupula comeca a rachar: 3-4 linhas brancas (#FFFFFF alpha 200) na superficie
  - Rachaduras em posicoes aleatorias
  - Cor da cupula: alpha diminui pra 70
  - Ciro dentro: percebe, expressao muda pra surpresa
  - Olhos arregalados

Frame 7 (0.750s - 0.875s) - Instabilidade
  - Cupula pisca: alterna visivel (alpha 60) / invisivel (alpha 0) a cada 2 sub-frames
  - Rachaduras se alargam
  - Particulas se dispersam erraticamente
  - Ciro: PANICO dentro da cupula, bracos balancando

Frame 8 (0.875s - 1.000s) - Explosao
  - Cupula ESTOURA
  - 8-10 fragmentos voam radialmente (3x3px cada, #4169E1 alpha 150)
  - Fragmentos decaem: alpha diminui durante 0.5s apos spawn
  - Onda de choque: circulo branco expandindo (1 frame)
  - Ciro: tonto, estrelinhas (3x 4x4px, #FFD700) circulando na cabeca
  - Corpo balancando levemente
```

**Cooldown**: 15 segundos apos uso.
**Dano na explosao**: 10% do HP max em area 32px (inclui Ciro).

---

### 7. RAGE DO RIVOTRIL

**Conceito**: Panico absoluto quando o Rivotril acaba. Furia descontrolada.

**Trigger automatico**: Barra de Rivotril chega a 0%.

```
Frame 1 (0.000s - 0.100s) - Descoberta
  - Ciro olha pro frasco: mao levanta ao nivel do rosto
  - Frasco: VAZIO (sem liquido azul, apenas vidro #FF6B00)
  - Olhos: arregalados progressivamente (pupilas dilatam)
  - Suor: 2 gotas (2x3px, #87CEEB) spawn na testa
  - Mao: tremor intenso (2px)

Frame 2 (0.100s - 0.200s) - Transicao pro Panico
  - Rosto: gradiente de #D4956A -> #FF2222
  - Veias do pescoco: EXPLODEM (triplicam de tamanho)
  - Veias se estendem ate a testa (novas linhas #660066)
  - Olhos: tornam-se #FF0000 (injetados)
  - Boca: aberta em grito
  - Corpo: treme 3px em todas direcoes

Frame 3 (0.200s - 0.300s) - Furia
  - Ciro agarra frasco com DUAS maos
  - Corpo comeca a girar (fase 1 de rotacao)
  - Motion blur circular: afterimage do corpo (alpha 40) em 45 graus atras
  - Rivotril vazio vira arma contundente
  - Efeito: linhas de velocidade radiais (4 linhas, 1px, brancas)

Frame 4 (0.300s - 0.400s) - Area Damage
  - Ciro no centro: girou 180 graus
  - Onda de choque: circulo expandindo (raio 16px -> 32px)
  - Cor da onda: #FF4444 alpha 100
  - DANO: tudo no raio 32px leva dano (INIMIGOS E ALIADOS)
  - Auto-dano: Ciro perde 15% HP
  - Particulas: debris voando (6-8, 2x2px, cores variadas)

Frame 5 (0.400s - 0.500s) - Auto-Destruicao
  - Ciro para de girar: pose desequilibrada
  - Cai sobre um joelho
  - Estrelas na cabeca: 3 estrelas 4x4px (#FFD700) girando em orbita
  - Rosto: tonto, olhos em espiral (ou X classico)
  - HP diminui visivelmente

Frame 6 (0.500s - 0.600s) - Recuperacao
  - Ciro de joelhos, respirando pesado
  - Rosto: voltando de #FF2222 -> #CC3333 (ainda vermelho mas diminuindo)
  - Veias: diminuindo de tamanho (2x normal, nao 3x)
  - Respiracao: peito expandindo/contraindo (2px)
  - Estrelas somem gradualmente
  - Transiciona de volta pra Idle (mas irritado)
```

**Apos Rage**: Barra de Rivotril nao regenera por 10 segundos.

---

### 8. CANDIDATURA ETERNA (Ressurreicao)

**Conceito**: Morre mas volta. Sempre. Cada vez mais fraco e menor.

**Trigger**: 1 segundo apos completar Death (frame 4).

```
Frame 1 (0.000s - 0.167s) - Brilho
  - Corpo no chao (mesma pose de Death frame 4)
  - Brilho dourado (#FFD700 alpha 100) nas bordas do sprite
  - 8-12 particulas douradas (2x2px) surgem ao redor
  - Particulas se movem lentamente em direcao ao corpo

Frame 2 (0.167s - 0.333s) - Levitacao
  - Corpo levita: sobe 4px do chao
  - Brilho se intensifica: alpha 150
  - Terno MAGICAMENTE se ajusta: dobras somem, lapela se endireita
  - Gravata se endireita sozinha (animacao: de torta pra reta)
  - Cabelo volta ao penteado perfeito

Frame 3 (0.333s - 0.500s) - De Pe (Encolhido)
  - Ciro de pe, MAS:
    - Sprite diminui de 64x64 pra (64-2*N)x(64-2*N) onde N = numero de mortes
    - Primeira morte: 62x62 (quase imperceptivel)
    - Segunda: 60x60 (ja notavel)
    - Terceira: 58x58 (comico)
    - Decima+: 44x44 (minusculo, patetico)
  - Olhos: abertos, confusos
  - Cores: 10% mais desbotadas a cada ressurreicao (cumulativo)
  - Brilho dourado diminuindo

Frame 4 (0.500s - 0.667s) - "Eu Voltei"
  - Pose triunfante: dedo apontando pra cima
  - Expressao: convicto que desta vez vai dar certo
  - MAS: claramente menor e mais fraco
  - Brilho some completamente
  - Transiciona pra Idle

NOTA: HP volta a 1% (nao 100%). Cada ressurreicao e MAIS PATETICA.
```

---

### 9. DEBATE UNILATERAL

**Conceito**: Para e faz discurso. Ninguem pediu. Efeito em area.

```
Frame 1 (0.000s - 0.125s) - Preparacao
  - Ciro para abruptamente
  - Bracos abrem: pose de orador de palanque
  - Mao direita: xicara de cafe (6x6px, fumaca saindo)
  - Olhar: inspirado, como se tivesse plateia (nao tem)

Frame 2 (0.125s - 0.250s) - Discurso
  - Mao esquerda aponta pra frente acusatoriamente
  - Bolha de fala: 16x12px aparece acima, conteudo "!@#$%"
  - Inimigos em raio 32px: "?" aparece acima deles (confusao)
  - Inimigos: velocidade -20% (debuff aplicado)
  - Rosto: vermelho de paixao oratoria

Frame 3 (0.250s - 0.375s) - Climax
  - Bolha de fala: DOBRA de tamanho (32x24px)
  - Texto na bolha muda pra bloco de texto ilegivel
  - Ciro: mais vermelho, gesticulando freneticamente
  - Cafe espirra da xicara (2-3 goticulas marrons #6F4E37)
  - Aliados em raio 24px: "!" irritado acima (+10% dano mas e buff de raiva)

Frame 4 (0.375s - 0.500s) - Conclusao
  - Ciro sorri: satisfeito, como se tivesse convencido todos
  - Bolha de fala: encolhe e some com POP (2-3 particulas)
  - Ninguem ao redor mudou de comportamento alem dos buffs/debuffs
  - Xicara: vazia (cafe todo espirrado)
  - Transiciona pra Idle
```

**Debuffs aplicados**: Inimigos -20% velocidade por 3s. Aliados +10% dano por 3s.

---

### 10. XINGAMENTO ERUDITO

**Conceito**: Grito direcionado que STUNA o inimigo. A boca deforma grotescamente.

```
Frame 1 (0.000s - 0.100s) - Inspiracao
  - Ciro inspira: peito expande 2px
  - Corpo infla levemente (todo sprite "engorda" 1px)
  - Rosto vai ficando vermelho gradualmente
  - Veias: comecam a pulsar rapido

Frame 2 (0.100s - 0.200s) - GRITO
  - BOCA DEFORMA: abre ate ocupar 60% do rosto
  - Caricatura maxima: mandibula desce abaixo do queixo original
  - Onda sonora: 3 semicirculos concentricos (1px cada) saindo da boca
  - Cor das ondas: #FFD700 com alpha decrescente (200, 150, 100)
  - Corpo: inclinado pra frente no grito

Frame 3 (0.200s - 0.300s) - Projetil de Texto
  - Texto pixelado bold voa da boca em direcao ao inimigo
  - Texto: "BOSSALOIDE!" (32x16px, #FF0000, outline #000000)
  - Velocidade: 64px por frame
  - Trail: afterimage do texto (alpha 60, 1 frame atras)
  - Ondas sonoras continuam expandindo

Frame 4 (0.300s - 0.400s) - Impacto + Recuperacao
  - Texto atinge inimigo: STUN (3s)
  - Estrelas ao redor do inimigo stunado
  - Ciro: boca fechando (volta ao tamanho normal)
  - Endireitando a gravata (gesto classico de quem "ganhou o debate")
  - Rosto: satisfeito, queixo pra cima
```

**Variantes de texto**: Alternar entre "BOSSALOIDE!", "PATIFE!", "CANALHA!", "LIBERALZINHO!".

---

### 11. TERCEIRA VIA (Dash/Esquiva)

**Conceito**: Esquiva que funciona perfeitamente MAS nunca acerta nada. Comedia.

```
Frame 1 (0.000s - 0.083s) - Preparacao
  - Ciro agacha: corpo abaixa 4px
  - Olhar pro lado (direcao do dash)
  - Tensao nas pernas (pixels de "compressao")

Frame 2 (0.083s - 0.167s) - Dash
  - DESLOCAMENTO INSTANTANEO: 32px na direcao
  - Afterimage: 3 copias ghost do Ciro no caminho
    - Copia 1: alpha 100, posicao original
    - Copia 2: alpha 60, 16px
    - Copia 3: alpha 30, 24px
  - Ciro real: esticado na direcao do dash (sprite distorcido 1-2px horizontal)
  - Hitbox: DESLIGADA durante dash (invulneravel)

Frame 3 (0.083s - 0.250s)
  - Afterimages desvanecendo
  - Ciro passa PELOS inimigos (atravessa hitbox deles sem interacao)
  - Expressao: concentrada no dash

Frame 4 (0.250s - 0.333s) - Chegada
  - Ciro para no destino
  - Olha pra tras: confuso
  - Inimigos: completamente intactos
  - Expressao: "como nao acertei?"
  - Afterimages finais desaparecem
  - Transiciona pra Idle
```

**Nota mecanica**: Dash tem 100% dodge mas 0% hit chance. Pura esquiva, zero ofensa. A "terceira via" que nao leva a lugar nenhum.

---

## SISTEMA DE BARRA DE RIVOTRIL (Animacao Continua)

### Componentes Visuais

```
+---+--------------------+
| F |████████████████████| <- Barra cheia
+---+--------------------+
  ^          ^
  |          |
  Icone      Preenchimento
  8x8px      24x4px
```

### Transicoes Visuais da Barra

| Nivel    | Cor Barra  | Icone           | Efeito no Sprite         | Efeito na Barra        |
|----------|-----------|-----------------|--------------------------|------------------------|
| 100-76%  | #00BFFF   | Frasco cheio    | Normal                   | Estavel                |
| 75-51%   | #FFD700   | Frasco meio     | Tremor 1px              | Leve pulsacao          |
| 50-26%   | #FF8C00   | Frasco quase    | Tremor 2px, vermelho    | Pulsacao intensa       |
| 25-1%    | #FF0000   | Frasco vazio    | Tremor 3px, panico      | Pisca ON/OFF (4Hz)     |
| 0%       | (vazio)   | Frasco quebrado | RAGE ativada            | Borda vermelha pulsa   |

### Animacao da Barra Diminuindo
- Transicao de cor: gradiente suave entre niveis
- Tamanho: diminui da direita pra esquerda (1px = ~4% de Rivotril)
- Particulas: quando perde Rivotril, 1-2 gotinhas azuis (#00BFFF) "pingam" da barra

### Animacao da Barra VAZIA (Panico)
- Borda da barra: pisca vermelho (#FF0000) / preto (#000000) a 4Hz
- Icone: frasco quebrado treme 2px
- Texto "!" aparece ao lado (4x6px, vermelho)

---

## TRANSICOES ENTRE ESTADOS

| De               | Para                | Condicao                          | Blending     |
|-----------------|---------------------|-----------------------------------|-------------|
| Idle            | Walk                | Input de movimento                | Imediato     |
| Walk            | Idle                | Input para                        | 1 frame blend|
| Idle/Walk       | Attack              | Input de ataque                   | Imediato     |
| Attack          | Idle                | Frame 3 completa                  | 1 frame blend|
| Qualquer        | Hit                 | Recebe dano                       | Interrompe   |
| Hit             | Idle                | Frame 2 completa                  | Imediato     |
| Qualquer        | Death               | HP = 0                            | Interrompe   |
| Death           | Candidatura Eterna  | Apos 1s delay                     | Fade (0.3s)  |
| Candidatura     | Idle                | Frame 4 completa                  | 1 frame blend|
| Idle            | Cirocracia          | Skill ativada                     | Imediato     |
| Cirocracia      | Idle                | Frame 8 completa                  | 2 frame blend|
| Qualquer        | Rage Rivotril       | Rivotril = 0%                     | Interrompe   |
| Rage Rivotril   | Idle                | Frame 6 completa                  | 2 frame blend|
| Idle            | Debate Unilateral   | Skill ativada (ou aleatorio)      | Imediato     |
| Debate          | Idle                | Frame 4 completa                  | 1 frame blend|
| Idle/Walk       | Xingamento          | Skill ativada                     | Imediato     |
| Xingamento      | Idle                | Frame 4 completa                  | 1 frame blend|
| Idle/Walk       | Terceira Via        | Input de esquiva                  | Imediato     |
| Terceira Via    | Idle                | Frame 4 completa                  | Imediato     |

---

## EFEITOS DE PARTICULAS (Timing)

| Particula            | Spawn Time              | Duracao   | Fade   | Quantidade |
|---------------------|-------------------------|-----------|--------|------------|
| Gotas de suor       | Qualquer (Rivotril<50%) | 0.5s      | 0.2s   | 2-4/s      |
| Vapor orelha        | Rage frame 2-4          | 0.3s      | 0.15s  | 2 (constante)|
| Gotas Rivotril      | Attack frame 3          | 0.4s      | 0.2s   | 4-6        |
| Estrelas tontura    | Rage frame 5, Cirocracia frame 8 | 1.0s | 0.3s | 3          |
| Fragmentos cupula   | Cirocracia frame 8      | 0.8s      | 0.4s   | 8-10       |
| Particulas energia  | Cirocracia frames 1-5   | Constante | N/A    | 6-8        |
| Brilho ressurreicao | Candidatura frames 1-2  | 0.5s      | 0.3s   | 8-12       |
| Debris              | Rage frame 4            | 0.6s      | 0.3s   | 6-8        |
| Fumaca cafe         | Debate frames 1-3       | Constante | N/A    | 2-3        |
| Ondas sonoras       | Xingamento frames 2-3   | 0.3s      | 0.15s  | 3          |
| Gotas cafe          | Debate frame 3          | 0.3s      | 0.2s   | 2-3        |

---

## CONFIGURACAO PHASER 3

```javascript
// Exemplo de configuracao de animacao para Ciro
// (referencia para implementacao, nao codigo final)

const ciroAnimConfig = {
  idle: {
    key: 'ciro-idle',
    frames: { start: 0, end: 3 },
    frameRate: 8,
    repeat: -1 // loop infinito
  },
  walk: {
    key: 'ciro-walk',
    frames: { start: 0, end: 5 },
    frameRate: 10,
    repeat: -1
  },
  attack: {
    key: 'ciro-attack',
    frames: { start: 0, end: 2 },
    frameRate: 12,
    repeat: 0
  },
  death: {
    key: 'ciro-death',
    frames: [
      { frame: 0, duration: 167 },
      { frame: 1, duration: 167 },
      { frame: 2, duration: 1500 }, // extendido: pacoca
      { frame: 3, duration: 1500 }  // extendido: fade
    ],
    repeat: 0
  },
  hit: {
    key: 'ciro-hit',
    frames: { start: 0, end: 1 },
    frameRate: 12,
    repeat: 0
  },
  cirocracia: {
    key: 'ciro-cirocracia',
    frames: { start: 0, end: 7 },
    frameRate: 8,
    repeat: 0
  },
  rageRivotril: {
    key: 'ciro-rage',
    frames: { start: 0, end: 5 },
    frameRate: 10,
    repeat: 0
  },
  candidaturaEterna: {
    key: 'ciro-resurrect',
    frames: { start: 0, end: 3 },
    frameRate: 6,
    repeat: 0
  },
  debateUnilateral: {
    key: 'ciro-debate',
    frames: { start: 0, end: 3 },
    frameRate: 8,
    repeat: 0
  },
  xingamentoErudito: {
    key: 'ciro-xingamento',
    frames: { start: 0, end: 3 },
    frameRate: 10,
    repeat: 0
  },
  terceiraVia: {
    key: 'ciro-dash',
    frames: { start: 0, end: 3 },
    frameRate: 12,
    repeat: 0
  }
};
```
