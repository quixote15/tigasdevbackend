# RAIOS DE LUZ NOS OLHOS -- Efeito de Fe Laser
### O Olhar que Queima o Pecado | Overlay de Efeito
### Zumbis de Brasilia | Abril 2026

---

> *"Quando Daciolo olha para voce com os olhos brilhando, voce sente. Nao importa se voce e ateu, agnostico, budista ou zumbi. Aqueles olhos VEEM sua alma. E se sua alma tiver pecado, os raios fazem o trabalho."*

---

## Specs Tecnicas

| Propriedade | Valor |
|---|---|
| Tamanho por frame | 32x16px (horizontal, mais largo que alto) |
| Total de frames | 4 |
| Sheet total | 128x16px (horizontal) |
| Formato | PNG com transparencia |
| Frame rate | 8 fps |
| Loop | Sim (durante ativacao) |
| Tipo | Overlay sprite (renderizado na frente dos olhos do Daciolo) |
| Blend mode | ADD (aditivo para brilho) |
| Posicao | Centrado nos olhos, projetando para frente |

---

## Frame-by-Frame

### Frame 1 -- Ignicao (Olhos Acendem)
```
32x16px.

Dois pontos de ORIGEM nos olhos (posicao: 8px a partir da esquerda para olho
esquerdo, 14px para olho direito, ambos a 8px da base -- ajustar conforme
sprite do personagem).

De cada ponto: FLASH circular pequeno (3x3px), cor amarelo puro (#FFFF00),
opacidade 100%. Glow circular ao redor de cada flash (5x5px, #FFFF00 @ 50%).

NENHUM raio ainda -- apenas os PONTOS DE LUZ nos olhos. Como um LED acendendo.
O poder CARREGANDO.

Particulas de "fagulha" (1x1px, branco) -- 2-3 saindo de cada olho em direcoes
aleatorias (burst curto).
```

### Frame 2 -- Raios Nascendo (Feixes Curtos)
```
32x16px.

Dos pontos de origem: FEIXES DE LUZ comecando a projetar para FRENTE e
LEVEMENTE PARA CIMA (angulo: 10-15 graus acima da horizontal).

Feixe esquerdo: linha de 8px comprimento, 2px largura, gradiente:
  - Origem: branco (#FFFFFF)
  - Meio: amarelo (#FFFF00)
  - Ponta: dourado (#FFD700)
  Opacidade: 90% na origem, 50% na ponta.

Feixe direito: espelhado do esquerdo mas NAO simetrico (1px de diferenca
em comprimento, angulo levemente diferente -- organico).

Glow ao redor de cada feixe: 1px, dourado (#FFD700 @ 30%).
Os pontos de origem nos olhos continuam BRILHANDO (#FFFF00).

Os raios estao NASCENDO. Curtos, incertos, pulsantes. Como o motor de um
carro divino dando partida.
```

### Frame 3 -- Raios Completos (Feixes Longos)
```
32x16px.

Feixes COMPLETOS projetados para fora do frame (ou ate a borda do sprite).

Feixe esquerdo: linha de 16px (ate a borda direita do sprite), 3px largura
no meio (mais grosso que Frame 2). Gradiente:
  - Origem: branco PURO (#FFFFFF)
  - 1/3: amarelo intenso (#FFFF00)
  - 2/3: dourado (#FFD700)
  - Ponta: dourado transparente (#FFD700 @ 30%)

Feixe direito: identico mas com leve ONDULACAO (nao perfeitamente reto --
o raio VIBRA com energia divina, 1px de variacao senoidal).

ENTRE os dois feixes: area de BRILHO DIFUSO (triangulo de luz entre os raios,
#FFFF00 @ 15%). Os raios convergem levemente (como faróis de carro convergindo
no horizonte).

Particulas ao longo dos feixes: 2-3 pontos brancos (1x1px) distribuidos
aleatoriamente no comprimento dos raios (brilhos internos).

Glow ao redor: 2px, dourado suave.

ESTE E O FRAME DE PICO. Os raios estao a TODA POTENCIA. Visao divina ATIVA.
```

### Frame 4 -- Raios Pulsando (Variacao de Intensidade)
```
32x16px.

Feixes com MESMA direcao e comprimento do Frame 3, MAS:
  - Largura VARIA: 2px (mais finos que Frame 3)
  - Opacidade REDUZIDA: 70% geral (vs 90% do Frame 3)
  - Cor levemente mais DOURADA (menos branco na origem)
  - Ondulacao MAIS pronunciada (2px de variacao senoidal)

Os pontos de origem nos olhos: pulsam (BRILHO -> DIM -> BRILHO em transicao
para loop de volta ao Frame 1).

Efeito visual: os raios "RESPIRAM". Expandem e contraem. Como batimento cardiaco
divino. PUMP-pump-PUMP-pump.

Particulas reduzidas: 1-2 pontos apenas.

Este frame cria o CONTRASTE que faz o loop funcionar. Sem ele, os raios
pareceriam estaticos. Com ele, parecem VIVOS.
```

---

## Ciclo de Animacao

```
Frame 1 (125ms) -> Frame 2 (125ms) -> Frame 3 (125ms) -> Frame 4 (125ms) -> [loop]
  Ignicao         Nascendo         PICO            Pulsando
  (pontos)        (curtos)         (completos)     (ondulando)

Ciclo total: 500ms (2 pulsacoes por segundo)
```

---

## Triggers de Ativacao

Os raios dos olhos NAO sao permanentes. Eles ATIVAM em momentos especificos:

### 1. Durante Skills (OBRIGATORIO)
```javascript
const RAIOS_TRIGGERS_SKILL = [
    'daciolo-special-fumaca',       // Frames 1-7 (durante toda a skill)
    'daciolo-special-gloria',       // Frames 2-5 (durante grito)
    'daciolo-special-exorcismo',    // Frames 2-4 (durante imposicao)
    'daciolo-special-roraima',      // Frames 5-7 (no topo da montanha)
    'daciolo-special-ursal',        // Frames 0-1 (ao ver a URSAL descendo)
    'daciolo-attack'                // Frame 1 (wind-up, pupilas laser)
];
```

### 2. Durante Idle (ALEATORIO)
```javascript
// 15% de chance a cada 3 segundos no idle
function checkIdleRaiosRandom() {
    if (currentState === 'idle' && Math.random() < 0.15) {
        activateRaios(800);  // ativa por 800ms (flash curto)
    }
}
```

### 3. Ao Receber Hit (REATIVO)
```javascript
// Ativa por 300ms ao levar dano (reflexo divino)
function onDacioloTakesDamage() {
    activateRaios(300);
}
```

### 4. Proximidade de Inimigos "Demoniacos" (SENSOR)
```javascript
// Ativa quando inimigo tipo "demoniaco" entra em range de 3 tiles
function onDemonicEnemyNearby(enemy) {
    if (enemy.type === 'demonic') {
        activateRaios(-1);  // fica ativo enquanto inimigo estiver perto
        // Os raios APONTAM na direcao do inimigo
    }
}
```

---

## Direcionalidade dos Raios

Os raios SEGUEM a direcao que Daciolo esta olhando:

### Down (olhando para camera)
```
Raios projetam para BAIXO-FRENTE (em direcao ao jogador).
Angulo: 80-100 graus (quase para baixo).
Visualmente: raios saem dos olhos e apontam para a parte inferior do frame.
```

### Up (olhando para cima)
```
Raios projetam para CIMA.
Angulo: 260-280 graus.
Visualmente: raios saem dos olhos para o topo do frame.
NOTA: Quando olhando para cima, os olhos sao menos visiveis -- raios sao menores.
```

### Left
```
Raios projetam para a ESQUERDA.
Angulo: 170-190 graus.
Ambos os raios apontam na mesma direcao (convergindo levemente).
```

### Right
```
Raios projetam para a DIREITA.
Angulo: 350-10 graus.
Mirror da versao left.
```

---

## Implementacao Phaser 3

### Setup

```javascript
// Sprite overlay dos raios
const raiosOlhos = this.add.sprite(0, 0, 'raios-olhos-sheet');
raiosOlhos.setVisible(false);
raiosOlhos.setBlendMode(Phaser.BlendModes.ADD);
raiosOlhos.setDepth(daciolo.depth + 2);  // acima de tudo

this.anims.create({
    key: 'raios-olhos-anim',
    frames: this.anims.generateFrameNumbers('raios-olhos-sheet', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1
});

this.dacioloRaios = raiosOlhos;
```

### Ativacao/Desativacao

```javascript
function activateRaios(duration) {
    const raios = this.dacioloRaios;
    raios.setVisible(true);
    raios.play('raios-olhos-anim');

    // Fade in rapido
    raios.setAlpha(0);
    this.tweens.add({
        targets: raios,
        alpha: 1.0,
        duration: 50
    });

    // Auto-desativar se duration > 0
    if (duration > 0) {
        this.time.delayedCall(duration, () => {
            deactivateRaios();
        });
    }
}

function deactivateRaios() {
    const raios = this.dacioloRaios;
    // Fade out
    this.tweens.add({
        targets: raios,
        alpha: 0,
        duration: 100,
        onComplete: () => {
            raios.setVisible(false);
            raios.stop();
        }
    });
}
```

### Update Loop (posicao + direcao)

```javascript
// Em update()
if (this.dacioloRaios.visible) {
    const raios = this.dacioloRaios;
    const direction = this.daciolo.getData('facingDirection');

    // Posicionar nos olhos conforme direcao
    switch (direction) {
        case 'down':
            raios.setPosition(daciolo.x, daciolo.y - 8);
            raios.setAngle(80);
            raios.setFlipX(false);
            break;
        case 'up':
            raios.setPosition(daciolo.x, daciolo.y - 20);
            raios.setAngle(260);
            raios.setFlipX(false);
            raios.setScale(0.7);  // menores quando olhando para cima
            break;
        case 'left':
            raios.setPosition(daciolo.x - 4, daciolo.y - 14);
            raios.setAngle(180);
            raios.setFlipX(false);
            break;
        case 'right':
            raios.setPosition(daciolo.x + 4, daciolo.y - 14);
            raios.setAngle(0);
            raios.setFlipX(false);
            break;
    }
}
```

---

## Variantes por Skin

### Normal (Skin 1)
- Raios padroes: dourado -> amarelo -> branco
- Ativacao em skills + aleatorio

### Candidato 2026 (Skin 2)
- Identicos ao normal

### Zombie Exorcista (Skin 3)
- Raios MISTAS: dourado + verde (batalha interior)
- Frames alternados: frame 1-2 dourado, frame 3 verde, frame 4 dourado
- O verde e a infeccao zumbi TENTANDO corromper a visao divina (mas falhando)

### Monte Roraima (Skin 4)
- Raios normais mas com tint levemente mais quente (sol do Roraima)

### Profeta Maximo (Skin 5)
- Raios PERMANENTES (sempre ativos, nao aleatorios)
- Cor: branco puro (#FFFFFF) na origem, dourado na ponta
- Mais largos (3px base vs 2px)
- Glow mais intenso

### Super Daciolo (Skin 6)
- LASER LITERAL permanente
- Raios 4px de largura, retorcidos
- Cor: neon amarelo (#FFFF00) solido
- Causam DANO REAL (1 DPS em inimigos na linha de visao)
- Trail persistente de 200ms (afterimage dos raios)
- Efeito de calor/distorcao ao redor dos feixes

---

## Paleta de Cores

| Componente | Cor | Hex | Uso |
|---|---|---|---|
| Ponto de origem | Amarelo puro | `#FFFF00` | Centro dos olhos |
| Feixe inicio | Branco | `#FFFFFF` | Proximo aos olhos |
| Feixe meio | Amarelo | `#FFFF00` | Corpo do raio |
| Feixe ponta | Dourado | `#FFD700` | Extremidade |
| Glow externo | Dourado suave | `#FFD700` @ 30% | Ao redor do feixe |
| Brilho difuso | Amarelo | `#FFFF00` @ 15% | Entre os feixes |
| Fagulhas | Branco | `#FFFFFF` | Particulas pequenas |
| Versao zombie | Verde | `#7CFC00` | Frame 3 da skin zombie |
| Versao super | Neon amarelo | `#FFFF00` | Super Daciolo laser |

---

## Notas Finais

1. Os raios devem parecer ORGANICOS, nao mecanicos -- ondulam, vibram, pulsam
2. NUNCA perfeitamente simetricos entre olho esquerdo e direito
3. Blend mode ADD e obrigatorio para o efeito de luminosidade
4. Em backgrounds claros, os raios podem ficar invisiveis -- considerar outline escuro fino
5. Performance: os raios sao 1 sprite overlay simples, custo minimo
6. Os raios sao um dos DETALHES que tornam Daciolo unico -- outros personagens nao tem olhos laser
7. Quando combinados com a aureola brilhando e a fumaca nas maos, criam o VISUAL COMPLETO do poder divino
