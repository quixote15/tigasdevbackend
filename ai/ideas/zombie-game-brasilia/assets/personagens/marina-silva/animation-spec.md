# Marina Silva - Especificacao de Animacoes

## MAQUINA DE ESTADOS (State Machine)

```
                     +-----------+
                     | INVISIBLE |  (estado padrao: NAO existe no mapa)
                     +-----+-----+
                           |
                    Easter Egg trigger
                           |
                           v
                     +-----+-----+
                     |  FADE IN  |
                     +-----+-----+
                           |
                           v
              +------------+------------+
              |      PRESENTE           |
              | (Presenca Espectral)    |
              | Timer: 3s de interacao  |
              +--+------+------+------++
                 |      |      |      |
              +--+--+ +-+--+ +-+--+   |
              | IDLE| |WALK| | HIT|   | 3s sem interacao
              +--+--+ +-+--+ +-+--+   | OU
                 |      |      |      | player interage
                 +------+------+      |
                        |             v
                        |       +-----+------+
                        |       |  FADE OUT  |
                        |       +-----+------+
                        |             |
                        |             v
                        |       +-----+------+
                        +------>| INVISIBLE  |
                                +------------+
                                     |
                                (death unico)
                                     |
                                     v
                                +----+----+
                                | DEATH   |
                                | (fade   |
                                | final)  |
                                +---------+
```

**IMPORTANTE**: Marina NAO tem estado de ataque agressivo, ressurreicao, ou skills ofensivas. Ela e um Easter Egg passivo.

---

## TABELA MESTRA DE ANIMACOES

| Animacao              | Frames | FPS | Duracao Total | Loop  | Prioridade | Interruptivel |
|----------------------|--------|-----|---------------|-------|------------|---------------|
| Idle                 | 4      | 8   | 0.500s        | Sim   | 0 (base)   | Sim           |
| Walk                 | 6      | 10  | 0.600s        | Sim   | 1          | Sim           |
| Attack (toque)       | 3      | 12  | 0.250s        | Nao   | 2          | Nao           |
| Death                | 4      | 6   | 0.667s        | Nao   | 5 (max)    | Nao           |
| Hit                  | 2      | 12  | 0.167s        | Nao   | 4          | Nao           |
| Fade In              | 6      | 6   | 1.000s        | Nao   | 5          | Nao           |
| Fade Out             | 6      | 6   | 1.000s        | Nao   | 5          | Nao           |
| Presenca Espectral   | 4      | 4   | 1.000s        | Sim   | 0          | Sim           |

---

## SISTEMA DE ALPHA (Controle Central)

Todas as animacoes de Marina sao governadas por um sistema de alpha dinamico.

### Alpha Base por Estado

| Estado           | Alpha Base | Oscilacao      | Nota                            |
|-----------------|-----------|----------------|---------------------------------|
| Invisible       | 0         | Nenhuma        | Nao renderizada                 |
| Fade In         | 10 -> 170 | Linear ascend  | 1 segundo de transicao          |
| Presente        | 140 - 170 | Senoidal lenta | Respira-se visualmente          |
| Idle            | 155 - 170 | Senoidal       | Oscilacao sutil                 |
| Walk            | 145 - 165 | Senoidal + step| Diminui levemente ao caminhar   |
| Attack          | 120 - 180 | Spike          | Sobe ao atacar, depois cai      |
| Hit             | 100 - 150 | Queda brusca   | Fica MAIS transparente ao hit   |
| Death           | 140 -> 0  | Linear descend | Desaparece pra sempre           |
| Fade Out        | 170 -> 0  | Linear descend | 1 segundo de transicao          |

### Formula de Alpha por Layer

```
alpha_layer = alpha_base * layer_multiplier

Layer multipliers:
  pes:    0.70  (primeiro a sumir)
  pernas: 0.80
  bracos: 0.75
  tronco: 0.90
  cabeca: 1.00  (mais opaco)
  olhos:  min(1.20 * alpha_base, 200)  (sempre mais visivel)
```

---

## DETALHAMENTO POR ANIMACAO

### 1. FADE IN - Aparicao (NAO loop)

**Conceito**: Marina se materializa do nada. Lento, sutil, facil de perder.

```
Frame 1 (0.000s - 0.167s) - Sombra
  Alpha: 10
  - Apenas uma sombra no chao: oval 12x6px, #000000 alpha 20
  - Se o jogador nao estiver olhando, nem percebe
  - Nenhum som, nenhum efeito
  - Cenario ao redor: completamente normal

Frame 2 (0.167s - 0.333s) - Distorcao
  Alpha: 30
  - Silhueta vaga: cores do cenario ATRAS dela se distorcem levemente
  - Como calor sobre asfalto quente
  - Forma humana: adivinhavel mas nao certa
  - Shader sugerido: distorcao UV nos pixels ao redor da posicao

Frame 3 (0.333s - 0.500s) - Forma
  Alpha: 60
  - Contornos cinza (#999999) comecam a aparecer
  - Forma humana reconhecivel: pessoa magra, de pe
  - Ainda sem detalhes faciais
  - Cores: apenas cinzas, sem as verdes/marrons da roupa ainda

Frame 4 (0.500s - 0.667s) - Rosto
  Alpha: 100
  - Rosto fica visivel: olhos melancolicos sao o primeiro detalhe claro
  - Corpo ainda parcialmente transparente
  - Pes e maos: alpha 50 (quase invisiveis)
  - Expressao: olha diretamente pro jogador (se possivel, tracking)

Frame 5 (0.667s - 0.833s) - Quase Presente
  Alpha: 140
  - Corpo ganha cor (desaturada): verde oliva, cinza
  - Cabelo visivel: curto, escuro
  - Roupas definidas mas transparentes
  - Sombra no chao fica mais definida

Frame 6 (0.833s - 1.000s) - Maxima Presenca
  Alpha: 170
  - Alpha MAXIMO (nunca 255!)
  - Marina "presente" — TIMER DE 3 SEGUNDOS INICIA
  - Icone de interacao pode aparecer (se jogador proximo)
  - Olhar: esperancoso, como quem finalmente foi notada
  - Transiciona pra Presenca Espectral (loop)
```

**Evento**: Ao completar Fade In, start timer de 3 segundos. Se jogador nao interagir, trigger Fade Out.

---

### 2. PRESENCA ESPECTRAL (Loop durante os 3 segundos)

**Conceito**: Marina presente mas instavel. Alpha oscila. Cada segundo mais transparente.

```
Frame 1 (0.000s - 0.250s)
  Alpha: 170
  - Marina olha ao redor: olhos se movem (pupilas 1px pro lado)
  - Postura: levemente inclinada pro jogador (esperanca)
  - Alpha no maximo
  - Bordas do sprite: tremulam 1px (heat shimmer)

Frame 2 (0.250s - 0.500s)
  Alpha: 160
  - Alpha cai levemente
  - Marina olha pro outro lado (procurando alguem)
  - Mao se levanta 1px (quase acenando, desiste)
  - Pes: alpha diminui mais rapido que o resto

Frame 3 (0.500s - 0.750s)
  Alpha: 150
  - Alpha cai mais
  - Expressao: preocupada, percebe que esta sumindo de novo
  - Olha pras proprias maos (vendo transparencia)
  - Corpo: bordas comecam a sangrar com cenario

Frame 4 (0.750s - 1.000s)
  Alpha: 140
  - Alpha minimo do loop
  - Expressao: resignada ("de novo nao...")
  - Se ninguem interagiu: prepara transicao pra Fade Out
  - Se jogador interagir DURANTE QUALQUER FRAME: trigger dialogo/bonus
```

**Degradacao temporal**: A cada ciclo completo (1s), o alpha maximo do Frame 1 diminui em 10:
- Ciclo 1: 170, 160, 150, 140
- Ciclo 2: 160, 150, 140, 130
- Ciclo 3: 150, 140, 130, 120 -> trigger Fade Out

---

### 3. IDLE (Loop, quando presente)

```
Frame 1 (0.000s - 0.125s)
  Alpha: alpha_base (varia com Presenca Espectral)
  - Pose parada, bracos ao lado
  - Olhar distante, desfocado
  - Cabelo: 1px de movimento (brisa que ninguem sente)
  - Sombra: sutil, quase inexistente

Frame 2 (0.125s - 0.250s)
  Alpha: alpha_base - 10
  - Suspiro: ombros sobem 1px, descem 1px
  - Extremidades desvanecendo 10% a mais
  - Expressao: melancolica

Frame 3 (0.250s - 0.375s)
  Alpha: alpha_base
  - Olha ao redor: procurando alguem que a note
  - Mao levanta 1-2px (quase chamando atencao)
  - Alpha volta ao base

Frame 4 (0.375s - 0.500s)
  Alpha: alpha_base - 15
  - Desiste de chamar atencao
  - Mao desce
  - Alpha no ponto mais baixo
  - Pes quase invisiveis neste frame
```

---

### 4. WALK (Loop)

**Conceito**: Mais FLUTUAR do que andar. Sem peso, sem impacto.

```
Frame 1 (0.000s - 0.100s)
  Alpha: 165
  - "Passo" esquerdo: pe nao toca o chao (1px gap com sombra)
  - Movimento minimo do corpo: quase desliza
  - Afterimage: ghost alpha 40 na posicao anterior

Frame 2 (0.100s - 0.200s)
  Alpha: 155
  - Transicao: corpo desliza pra frente
  - Afterimage do frame anterior: alpha 20 (sumindo)
  - Roupas: NAO se movem (sem vento, sem fisica)

Frame 3 (0.200s - 0.300s)
  Alpha: 160
  - "Passo" direito: mesmo gap de 1px
  - Flutuacao vertical: corpo sobe 0.5px (sub-pixel, implementar com offset)

Frame 4 (0.300s - 0.400s)
  Alpha: 150
  - Alpha mais baixo do ciclo
  - Afterimage mais forte neste frame (alpha 50)
  - Como se ela "se espalhasse" ao se mover

Frame 5 (0.400s - 0.500s)
  Alpha: 160
  - Recupera alpha
  - "Passo" esquerdo novamente
  - Expressao: olha pro caminho com resignacao

Frame 6 (0.500s - 0.600s)
  Alpha: 145
  - Alpha minimo absoluto do walk
  - Pes: alpha 80 (quase invisiveis)
  - Quase sumindo... mas o ciclo recomeça
```

**Nota tecnica**: Walk de Marina NAO deve ter bounce vertical (Y bob) como outros personagens. Ela DESLIZA.

---

### 5. ATTACK - Toque de Confusao

**Conceito**: Nao e ataque. E presenca. Ela toca e confunde. Custo: ficar mais transparente.

```
Frame 1 (0.000s - 0.083s) - Revelacao
  Alpha: 180 (!!! MAXIMO ABSOLUTO — unico momento)
  - Marina fica MAIS opaca que nunca por 1 frame
  - E assustador: ela estava quase invisivel e de repente ESTA LA
  - Olhar: determinado (raro nela)
  - Mao estende pra frente em direcao ao alvo

Frame 2 (0.083s - 0.167s) - Toque
  Alpha: 180
  - Mao toca o alvo (ou area proxima)
  - Area ao redor: distorcao visual (3x3 pixel area fica "blur")
  - Inimigo tocado: expressao confusa, "?" acima
  - Sem dano, sem violencia — apenas CONFUSAO existencial
  - Efeito: inimigo desorientado por 2s (direcao de movimento aleatorio)

Frame 3 (0.083s - 0.250s) - Custo
  Alpha: 120 (QUEDA BRUSCA)
  - Marina recua
  - Corpo fica MUITO mais transparente
  - Custo de se revelar: perde 50 pontos de alpha base por 5s
  - Expressao: exausta, como se "aparecer" custasse energia vital
  - Transiciona de volta pra Idle mas mais transparente
```

**Mecanica**: Attack e CUSTOSO. Cada uso reduz alpha base temporariamente. Usar muito = desaparecer mais rapido.

---

### 6. DEATH - Desaparecimento Final

**Conceito**: Nao morre. Some. Pra sempre. O desaparecimento mais triste do jogo.

```
Frame 1 (0.000s - 0.167s) - Inicio
  Alpha: 140
  - Expressao: triste mas NAO surpresa (ela sabia que ia acontecer)
  - Corpo comeca a desaparecer pelas extremidades
  - Pes: alpha 40 (quase idos)
  - Maos: alpha 60 (indo)
  - Nao ha dor, nao ha grito, nao ha dramaticidade
  - Silencio

Frame 2 (0.167s - 0.333s) - Dissolucao
  Alpha: 100
  - Pes: invisiveis (alpha 0)
  - Pernas: alpha 40
  - Maos: invisiveis (alpha 0)
  - Tronco: alpha 60
  - Rosto: alpha 100 (ainda presente)
  - Olhos: alpha 150 (segurando ate o fim)
  - Bolha de fala sutil: "Eu volto em 4 anos..." (12x6px, cinza, quase invisivel)

Frame 3 (0.333s - 0.500s) - Quase Nada
  Alpha: 60
  - Apenas rosto e ombros parcialmente visiveis
  - Olhos: alpha 120 (melancolicos, ultimos a ir)
  - Tudo mais: alpha < 20
  - Bolha de fala: fade out
  - Boca move minimamente (repetindo a frase sem som)
  - Cenario ao redor: completamente visivel atraves dela

Frame 4 (0.500s - 0.667s) - Nada
  Alpha: 20 -> 0
  - Apenas olhos por 0.1s: dois pontos castanhos na tela
  - Depois: nada
  - Particulas: 4-6 flocos brancos (#FFFFFF alpha 60) sobem lentamente
  - Folha seca cai: 4x4px (#8B7355) espirala ate o chao
  - Folha fica no chao por 5 segundos: unica evidencia de que Marina esteve ali
  - Sombra no chao: fade de 0.5s

TOTAL: Marina some em ~0.7s. Nao ha ressurreicao. Nao ha "Candidatura Eterna".
Proximo spawn: aleatorio, proximo Easter Egg trigger.
```

**CONTRASTE**: Enquanto Ciro morre com DRAMA (pacoca, ressurreicao, cada vez mais fraco), Marina simplesmente... nao esta mais la. O humor e existencial.

---

### 7. HIT

**Conceito**: Ao ser atingida, fica MAIS transparente (oposto dos outros que flasham branco).

```
Frame 1 (0.000s - 0.083s) - Impacto
  Alpha: alpha_base - 50
  - Corpo fica MAIS transparente ao hit (oposto dos outros)
  - Sem flash branco
  - Corpo ondula: 1px de distorcao tipo agua
  - Sem expressao de dor: expressao de tristeza
  - "Ah... estou aqui..."
  - Absorve o impacto silenciosamente

Frame 2 (0.083s - 0.167s) - Recuperacao Parcial
  Alpha: alpha_base - 20
  - Volta parcialmente (NAO 100%)
  - Permanentemente mais transparente que antes do hit
  - Olhar: mais triste que antes
  - Cada hit acumula: alpha_base_permanente -= 5
  - Apos muitos hits: alpha tao baixo que trigger Death
```

**Mecanica**: Hits acumulam transparencia permanente. Marina nao tem HP visivel -- ela simplesmente some quando fica transparente demais.

---

### 8. FADE OUT - Desaparicao (NAO loop)

**Conceito**: Inverso exato do Fade In. Marina vai embora porque ninguem a notou.

```
Frame 1 (0.000s - 0.167s)
  Alpha: 170
  - Marina olha pro jogador uma ultima vez
  - Expressao: tristeza, nao raiva
  - Corpo comeca a desvanecer pelas bordas

Frame 2 (0.167s - 0.333s)
  Alpha: 140
  - Extremidades perdem definicao
  - Folha do cabelo cai (particula: 4x4px, espiral descendente)
  - Mao se levanta levemente: aceno de despedida timido

Frame 3 (0.333s - 0.500s)
  Alpha: 100
  - Meio corpo invisivel
  - Boca move: "Eu volto em 4 anos..."
  - Bolha de fala: 12x6px, cinza (#999999 alpha 80)
  - Cenario sangrando atraves dela

Frame 4 (0.500s - 0.667s)
  Alpha: 60
  - Apenas rosto e ombros
  - Olhos: parte mais visivel
  - Mao de despedida: desaparecendo

Frame 5 (0.667s - 0.833s)
  Alpha: 30
  - Apenas olhos tristes
  - Dois pontos castanhos na tela
  - Tudo mais: invisivel

Frame 6 (0.833s - 1.000s)
  Alpha: 0
  - Nada
  - Folha seca no chao (se nao caiu antes)
  - Particulas brancas subindo (2-3 flocos)
  - Silencio
  - Estado: volta pra INVISIBLE

NOTA: Apos Fade Out, Marina so reaparece em outro trigger de Easter Egg.
Timer minimo entre aparicoes: 60 segundos.
```

---

## TRANSICOES ENTRE ESTADOS

| De                  | Para                | Condicao                            | Blending        |
|--------------------|---------------------|--------------------------------------|-----------------|
| Invisible          | Fade In             | Easter Egg trigger (aleatorio/area)  | N/A             |
| Fade In            | Presenca Espectral  | Frame 6 completa                     | Suave (alpha)   |
| Presenca           | Idle                | Nenhum input                         | Suave           |
| Presenca           | Walk                | Marina se move (IA ou script)        | Suave           |
| Presenca           | Fade Out            | Timer 3s expira OU player interage   | Imediato        |
| Idle               | Walk                | IA decide mover                      | 2 frame blend   |
| Walk               | Idle                | IA decide parar                      | 2 frame blend   |
| Qualquer (presente)| Hit                 | Recebe dano                          | Interrompe      |
| Hit                | Idle                | Frame 2 completa                     | 1 frame blend   |
| Qualquer (presente)| Death               | Alpha acumulado < 20                 | Suave           |
| Fade Out           | Invisible           | Frame 6 completa                     | N/A             |
| Idle (presente)    | Attack              | Player interagiu E Marina quer "ajudar"| Imediato      |
| Attack             | Idle                | Frame 3 completa                     | 2 frame blend   |

**Nota**: TODAS as transicoes de Marina devem ser SUAVES. Nao ha cortes bruscos, nao ha interrupcoes violentas. Tudo FLUI como neblina.

---

## EFEITOS DE PARTICULAS (Timing)

| Particula                | Spawn Time             | Duracao  | Fade   | Quantidade |
|-------------------------|------------------------|----------|--------|------------|
| Flocos de desaparicao   | Death frame 4, Fade Out frame 6 | 2.0s | 1.0s | 4-6       |
| Folha seca              | Fade Out frame 2 OU Death frame 4 | 5.0s (no chao) | 1.0s | 1 |
| Distorcao UV            | Fade In frame 2        | 0.167s   | Nenhum | N/A (shader)|
| Ghost afterimage (walk) | Walk todos frames      | 0.2s     | 0.1s   | 1 por frame|
| Brilho dos olhos        | Death frames 3-4       | 0.3s     | 0.2s   | 2          |

---

## EASTER EGG TRIGGER SYSTEM

### Condicoes de Aparicao

Marina aparece quando:
1. **Area especifica**: Jogador entra em zona de Easter Egg marcada no mapa
2. **Tempo de jogo**: Apos X minutos sem evento (preencher tedio)
3. **Aleatorio**: 2% de chance por minuto quando em area aberta
4. **Referencia cruzada**: Ciro menciona "candidata fantasma" -> Marina aparece por 1 frame ao fundo

### Janela de Interacao

```
[Fade In: 1.0s] -> [INTERAGIVEL: 3.0s] -> [Fade Out: 1.0s]
                          ^
                          |
                    Jogador deve
                    apertar botao
                    NESTA janela
```

Se jogador interage a tempo:
- Bonus secreto (definir com game design)
- Dialogo melancolico
- Achievement: "Alguem viu a Marina?"
- Marina sorri brevemente (unico momento de felicidade)

Se jogador NAO interage:
- Marina some sem comentario
- Nenhum feedback pro jogador (talvez ele nem percebeu)
- Proximo trigger: minimo 60 segundos

---

## CONFIGURACAO PHASER 3

```javascript
// Exemplo de configuracao de animacao para Marina
// (referencia para implementacao, nao codigo final)

const marinaAnimConfig = {
  fadeIn: {
    key: 'marina-fadein',
    frames: { start: 0, end: 5 },
    frameRate: 6,
    repeat: 0
  },
  presencaEspectral: {
    key: 'marina-presenca',
    frames: { start: 0, end: 3 },
    frameRate: 4,
    repeat: -1 // loop ate timer acabar
  },
  idle: {
    key: 'marina-idle',
    frames: { start: 0, end: 3 },
    frameRate: 8,
    repeat: -1
  },
  walk: {
    key: 'marina-walk',
    frames: { start: 0, end: 5 },
    frameRate: 10,
    repeat: -1
  },
  attack: {
    key: 'marina-attack',
    frames: { start: 0, end: 2 },
    frameRate: 12,
    repeat: 0
  },
  death: {
    key: 'marina-death',
    frames: { start: 0, end: 3 },
    frameRate: 6,
    repeat: 0
  },
  hit: {
    key: 'marina-hit',
    frames: { start: 0, end: 1 },
    frameRate: 12,
    repeat: 0
  },
  fadeOut: {
    key: 'marina-fadeout',
    frames: { start: 0, end: 5 },
    frameRate: 6,
    repeat: 0
  }
};

// Sistema de alpha dinamico
class MarinaAlphaSystem {
  constructor(sprite) {
    this.sprite = sprite;
    this.alphaBase = 0;
    this.alphaTarget = 0;
    this.permanentReduction = 0; // acumula com hits
    this.oscillationPhase = 0;
  }

  update(delta) {
    // Oscilacao senoidal
    this.oscillationPhase += delta * 0.002;
    const oscillation = Math.sin(this.oscillationPhase) * 15;

    // Alpha efetivo
    const effectiveAlpha = Math.max(0,
      this.alphaBase - this.permanentReduction + oscillation
    );

    // Aplicar por layer (simplificado: usa alpha global)
    this.sprite.setAlpha(effectiveAlpha / 255);
  }

  onHit() {
    this.permanentReduction += 5;
    this.alphaBase -= 50; // temporario
    // Restaura parcial apos 0.167s
    setTimeout(() => {
      this.alphaBase += 30; // nao restaura 100%
    }, 167);
  }
}
```
