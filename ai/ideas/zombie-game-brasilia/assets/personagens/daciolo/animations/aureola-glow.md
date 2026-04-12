# AUREOLA GLOW -- Efeito Pulsante
### Overlay Permanente do Daciolo | A Marca da Fe
### Zumbis de Brasilia | Abril 2026

---

> *"A aureola do Daciolo NUNCA apaga. NUNCA. Mesmo quando ele e zumbificado. Mesmo quando erra o grito. Ela pode piscar, pode diminuir, pode mudar de cor -- mas ela NUNCA desaparece completamente. Porque a fe genuina nao tem off switch."*

---

## Specs Tecnicas

| Propriedade | Valor |
|---|---|
| Tamanho por frame | 32x32px |
| Total de frames | 4 |
| Sheet total | 128x32px (horizontal) |
| Formato | PNG com transparencia |
| Frame rate | 4 fps (pulsacao lenta, hipnotica) |
| Loop | Sim (infinito enquanto Daciolo existir) |
| Tipo | Overlay sprite (renderizado ACIMA do sprite do personagem) |
| Blend mode | ADD (aditivo, para brilho) |
| Posicao | Centrado 12-16px ACIMA da cabeca do Daciolo, inclinado 15 graus |

---

## Frame-by-Frame

### Frame 1 -- Dourado Intenso (Pico de Fe)
```
32x32px. Centro do frame.

Forma: anel/aro ovalado (NAOUM circulo perfeito -- levemente achatado, inclinado
15 graus para a direita, estilo TORTO que e marca do Daciolo). Proporcao do aro:
~20px largura x 6px altura (perspectiva isometrica, visto de cima-frente).

Cor PRINCIPAL: Dourado intenso (#FFD700).
Glow EXTERNO: 3px de halo dourado-claro (#FFE44D) ao redor, opacity 60%.
Glow INTERNO: preenchimento semi-transparente dourado (#FFD700 @ 20%) dentro do aro.
Brilho maximo: 2 pontos de highlight branco (#FFFFFF) nos cantos superior-esquerdo
e inferior-direito do aro (reflexo de luz).

Linhas: contorno GROSSO (2px) no aro, estilo Andre Guedes (irregular, NAO suave).
Textura: leves riscos internos (aro metalico desgastado pelo uso divino).

Este e o frame de MAXIMO BRILHO. A fe no auge. Aureola RADIANTE.
```

### Frame 2 -- Dourado Suave (Fe Constante)
```
32x32px. Centro do frame.

Mesma forma e posicao do Frame 1. Diferenças:

Cor PRINCIPAL: Dourado suave (#DAA520) -- menos saturado.
Glow EXTERNO: 2px, dourado (#FFD700 @ 40%) -- menor e mais fraco.
Glow INTERNO: preenchimento (#DAA520 @ 15%) -- quase invisivel.
Highlights brancos: REMOVIDOS (sem reflexo neste frame).

O aro parece LEVEMENTE menor (1px a menos em cada lado -- compressao visual
da pulsacao). Contorno mantem 2px.

Fe constante mas sem pico. A respiracao da divindade. Sistole.
```

### Frame 3 -- Branco (Transcendencia Momentanea)
```
32x32px. Centro do frame.

Mesma posicao. Cor MUDA:

Cor PRINCIPAL: Branco (#FFFFFF) com LEVE tom dourado.
Glow EXTERNO: 4px de halo branco (#FFFFFF @ 50%) -- MAIOR que Frame 1.
Glow INTERNO: preenchimento branco (#FFFFFF @ 25%).
O aro inteiro fica com aparencia de LUZ PURA (nao mais metal dourado).

Este frame e o FLASH de transcendencia. Dura pouco (250ms) mas e o momento
em que a aureola parece MAIS divina. A pulsacao white-out.

Detalhes: 4 raios CURTOS (3px cada) saindo dos pontos cardeais do aro
(cima, baixo, esquerda, direita) -- cruzes de luz momentaneas.
```

### Frame 4 -- Dourado Intenso Retorno (Volta ao Pico)
```
32x32px. Centro do frame.

IDENTICO ao Frame 1 mas com 1 diferenca sutil:
- A posicao do aro deslocou 1px para a esquerda (micro-wobble).
- Os highlights brancos estao nos pontos OPOSTOS (inferior-esquerdo e superior-direito).

Isso cria um MICRO-MOVIMENTO na aureola -- ela nao fica perfeitamente estatica,
ela OSCILA levemente. Parecendo VIVA. Flutuante. Divina.

O retorno ao dourado intenso fecha o ciclo. Loop infinito.
```

---

## Ciclo de Pulsacao

```
Frame 1 (250ms) -> Frame 2 (250ms) -> Frame 3 (250ms) -> Frame 4 (250ms) -> [loop]
                   Intenso      Suave       Branco      Intenso+wobble
                   MAXIMO      MEDIO       FLASH        MAXIMO deslocado

Ciclo total: 1000ms (1 segundo por pulsacao)
```

---

## Estados Especiais da Aureola

### Estado IDLE (padrao)
```javascript
const aureolaIdle = {
    animation: 'aureola-glow',
    frameRate: 4,
    alpha: 1.0,
    scale: 1.0,
    tint: null,  // cores originais do sprite
    offsetY: -24,  // acima da cabeca
    angle: -15  // inclinacao torta
};
```

### Estado POWER-UP (durante skills)
```javascript
const aureolaPowerUp = {
    animation: 'aureola-glow',
    frameRate: 8,        // DOBRA a velocidade de pulsacao
    alpha: 1.2,          // over-bright (blend ADD faz funcionar)
    scale: 1.5,          // 50% MAIOR
    tint: null,
    offsetY: -28,        // sobe mais
    angle: -15,
    additionalEffect: 'spin'  // gira durante skills
};

// Transicao para power-up
function aureolaToPressPowerUp(aureola) {
    scene.tweens.add({
        targets: aureola,
        scale: 1.5,
        y: aureola.y - 4,
        duration: 200,
        ease: 'Back.easeOut'
    });
    aureola.anims.msPerFrame = 125;  // 8fps
    // Adicionar spin
    scene.tweens.add({
        targets: aureola,
        angle: 360 - 15,
        duration: 800,
        repeat: -1
    });
}
```

### Estado DIM (pos-Fumaca Santa / cooldown)
```javascript
const aureolaDim = {
    animation: 'aureola-glow',
    frameRate: 2,        // pulsacao LENTA (exausto)
    alpha: 0.3,          // 30% -- quase invisivel
    scale: 0.8,          // menor
    tint: 0xAAAAAA,      // acinzentado
    offsetY: -22,        // abaixa levemente
    angle: -20           // inclina mais (cansado)
};

// Transicao para dim
function aureolaToDim(aureola, duration) {
    scene.tweens.add({
        targets: aureola,
        alpha: 0.3,
        scale: 0.8,
        angle: -20,
        duration: 500,
        ease: 'Quad.easeOut'
    });
    aureola.anims.msPerFrame = 500;  // 2fps
    aureola.setTint(0xAAAAAA);

    // Recovery apos cooldown
    scene.time.delayedCall(duration, () => {
        scene.tweens.add({
            targets: aureola,
            alpha: 1.0,
            scale: 1.0,
            angle: -15,
            duration: 2000,
            ease: 'Sine.easeInOut'
        });
        aureola.anims.msPerFrame = 250;  // 4fps
        aureola.clearTint();
    });
}
```

### Estado FLICKER (hit / dano)
```javascript
function aureolaFlicker(aureola) {
    scene.tweens.add({
        targets: aureola,
        alpha: { from: 1.0, to: 0.2 },
        duration: 50,
        yoyo: true,
        repeat: 2  // 3 flickers
    });
}
```

### Estado DEATH (ascensao)
```javascript
function aureolaDeathSequence(aureola) {
    // Fase 1: Flicker frenetico
    scene.tweens.add({
        targets: aureola,
        alpha: { from: 1.0, to: 0.1 },
        duration: 30,
        yoyo: true,
        repeat: 5
    });

    // Fase 2: Estabiliza no MAXIMO
    scene.time.delayedCall(300, () => {
        scene.tweens.add({
            targets: aureola,
            alpha: 1.5,
            scale: 2.0,
            duration: 500,
            ease: 'Back.easeOut'
        });
    });

    // Fase 3: Duplica (DUAS aureolas)
    scene.time.delayedCall(800, () => {
        const aureloa2 = scene.add.sprite(aureola.x, aureola.y - 8, 'aureola-glow');
        aureloa2.play('aureola-glow-anim');
        aureloa2.setBlendMode(Phaser.BlendModes.ADD);
        aureloa2.setScale(2.5);
        aureloa2.setAlpha(0);
        scene.tweens.add({
            targets: aureloa2,
            alpha: 0.8,
            duration: 500
        });
    });

    // Fase 4: Transforma em estrela de 8 pontas
    scene.time.delayedCall(1300, () => {
        aureola.setTexture('aureola-estrela');  // sprite separado
        scene.tweens.add({
            targets: aureola,
            scale: 3,
            alpha: 0,
            angle: 180,
            duration: 1000,
            ease: 'Quad.easeIn'
        });
    });
}
```

### Estado ERRO COMICO (vergonha divina)
```javascript
function aureolaErroComico(aureola) {
    // A UNICA vez que a aureola APAGA completamente
    scene.tweens.add({
        targets: aureola,
        alpha: 0,       // APAGA!
        duration: 50,
        hold: 150,      // fica apagada 150ms
        yoyo: true
    });

    // Volta com vergonha (50% brilho, timida)
    scene.time.delayedCall(250, () => {
        scene.tweens.add({
            targets: aureola,
            alpha: 0.5,
            scale: 0.7,  // menor (encolheu de vergonha)
            duration: 300
        });
        // Recuperacao total em 3s
        scene.time.delayedCall(3000, () => {
            scene.tweens.add({
                targets: aureola,
                alpha: 1.0,
                scale: 1.0,
                duration: 2000,
                ease: 'Sine.easeInOut'
            });
        });
    });
}
```

---

## Variantes por Skin

### Aureola Normal (Skin 1: O Profeta)
- Frames: 4 (padrao descrito acima)
- Inclinacao: 15 graus
- Cor: dourado -> dourado suave -> branco -> dourado

### Aureola com Estrela (Skin 2: Candidato 2026)
- Frames: 4 (identicos + estrela no topo)
- Estrela: amarelo vivo (#FFE000), 4x4px, ponta para cima, posicionada no topo do aro
- A estrela pisca em phase OPOSTA a aureola (quando aureola dim, estrela bright, e vice-versa)

### Aureola Glitch (Skin 3: Zombie Exorcista)
- Frames: 4 base + 2 frames EXTRA de glitch
- Glitch frames: aureola fica VERDE DOENTIO (#7CFC00) por 1 frame aleatorio a cada 3-5 ciclos
- Formato do aro: levemente DISTORCIDO (bordas irregulares, como interferencia de sinal)
- Flickering mais frequente que o normal (como TV com mal contato)

### Aureola 150% (Skin 4: Monte Roraima)
- Frames: 4 (identicos mas 150% do brilho)
- Glow externo: 5px (vs 3px normal)
- Cor: dourado mais quente (#FFE000 base)
- Mais perto de Deus no alto da montanha

### Aureola Dupla (Skin 5: Profeta Maximo)
- Frames: 4 base para CADA aureola (2 aureolas sobrepostas)
- Aureola 1: padrao, horizontal
- Aureola 2: maior (1.5x), perpendicular (vertical, como saturn rings)
- As duas pulsam em FASES OPOSTAS (quando 1 esta no pico, 2 esta no vale)
- Juntas formam uma ESFERA DE LUZ abstrata

### Aureola Tripla (Skin 6: Super Daciolo)
- Frames: 4 base para cada aureola (3 aureolas)
- Aureola 1: padrao, horizontal
- Aureola 2: 1.3x, 45 graus
- Aureola 3: 1.6x, perpendicular
- Giram em DIRECOES OPOSTAS (1: horario, 2: anti-horario, 3: horario)
- Brilho PERMANENTE no maximo (sem dim phase)
- Cor: dourado / branco / dourado (cada uma com tom diferente)

---

## Implementacao Phaser 3

### Setup Base

```javascript
// Em create()
const aureola = this.add.sprite(0, 0, 'aureola-glow-sheet');

this.anims.create({
    key: 'aureola-glow-anim',
    frames: this.anims.generateFrameNumbers('aureola-glow-sheet', { start: 0, end: 3 }),
    frameRate: 4,
    repeat: -1
});

aureola.play('aureola-glow-anim');
aureola.setBlendMode(Phaser.BlendModes.ADD);
aureola.setOrigin(0.5, 0.5);
aureola.setAngle(-15);  // inclinacao torta

// Attach a Daciolo
this.dacioloAureola = aureola;
```

### Update Loop (seguir Daciolo)

```javascript
// Em update()
if (this.dacioloAureola && this.daciolo.active) {
    this.dacioloAureola.setPosition(
        this.daciolo.x,
        this.daciolo.y - 24  // offset acima da cabeca
    );
    this.dacioloAureola.setDepth(this.daciolo.depth + 1);  // sempre acima

    // Micro-float (leve bobbing vertical)
    this.dacioloAureola.y += Math.sin(this.time.now / 500) * 0.5;
}
```

---

## Paleta Completa da Aureola

| Estado | Frame 1 | Frame 2 | Frame 3 | Frame 4 |
|---|---|---|---|---|
| **Normal** | `#FFD700` 100% | `#DAA520` 80% | `#FFFFFF` 100% | `#FFD700` 100% |
| **Power-Up** | `#FFE000` 120% | `#FFD700` 100% | `#FFFFFF` 120% | `#FFE000` 120% |
| **Dim** | `#AAAAAA` 30% | `#999999` 20% | `#CCCCCC` 30% | `#AAAAAA` 30% |
| **Flicker** | ON/OFF rapid | ON/OFF rapid | ON/OFF rapid | ON/OFF rapid |
| **Death** | crescendo... | crescendo... | MAXIMO | estrela 8 pontas |
| **Erro** | APAGA (0%) | -- | -- | 50% timida |

---

## Notas de Arte

1. A aureola NUNCA e um circulo perfeito -- sempre OVALADA e TORTA
2. Os contornos sao GROSSOS e IRREGULARES (estilo Andre Guedes)
3. O brilho deve parecer QUENTE, nao frio (dourado, nao azulado)
4. A inclinacao de 15 graus e FIXA -- nunca fica reta (a imperfeicao e a piada: ate a aureola dele e meio torta, mas FUNCIONA)
5. Blend mode ADD e ESSENCIAL para o efeito de brilho funcionar sobre sprites escuros
6. Em backgrounds claros, considerar adicionar outline escuro na aureola para manter visibilidade
