# MONTE RORAIMA SURGINDO -- Animacao de Invocacao
### A Montanha Sagrada Atende ao Chamado | Sprite de Cenario Dinamico
### Zumbis de Brasilia | Abril 2026

---

> *"Quando Daciolo invoca o Monte Roraima, a TERRA OBEDECE. A montanha que ele subiu de chinelo na vida real, surge do chao de Brasilia no jogo. Porque se a fe pode mover montanhas, a fe do Daciolo pode INVOCAR montanhas."*

---

## Specs Tecnicas

| Propriedade | Valor |
|---|---|
| Tamanho por frame | 64x64px (sprite de cenario, mesmo tamanho do personagem) |
| Total de frames | 8 |
| Sheet total | 512x64px (horizontal) |
| Formato | PNG com transparencia |
| Frame rate | 10 fps |
| Loop | Nao (single play, frames 6-7 podem loop durante chuva de fogo) |
| Tipo | Sprite de cenario dinamico (renderizado como objeto do mundo) |
| Blend mode | Normal (nao aditivo -- e um objeto solido) |
| Depth | Abaixo de Daciolo no topo, acima de inimigos na base |

---

## Referencia Visual: Monte Roraima Real

O Monte Roraima e um TEPUI -- montanha de topo PLANO, paredes VERTICAIS. 
Caracteristicas que DEVEM aparecer no sprite:

- **Topo plano**: a caracteristica mais iconica. Mesa de pedra no ceu
- **Paredes verticais**: falesias quase 90 graus
- **Nuvens na base**: coberto de neblina na base/meio
- **Vegetacao escura**: pedra escura com musgo/liquen
- **Cachoeiras**: agua caindo das bordas do topo (referencia real)
- **Formato geral**: trapezoide invertido (base menor que topo, visualmente)

No estilo Andre Guedes:
- Linhas GROSSAS, irregulares
- Cores SATURADAS e SUJAS (nao bonito-natureza -- grotesco-natureza)
- Textura CARREGADA (cross-hatching nas rochas)
- A montanha parece VIVA e IRRITADA por ter sido arrancada do chao

---

## Frame-by-Frame

### Frame 1 -- Rachaduras no Chao
```
64x64px.

A montanha AINDA NAO APARECEU. O que aparece:

CHAO (parte inferior do frame, ~16px de altura): superficie com RACHADURAS
radiais partindo de um ponto central. 5-6 linhas de rachadura, cor: preto (#1A1A1A)
nas linhas, marrom-terra (#8B6914) no chao ao redor. As rachaduras sao FINAS
(1px) mas visiveis.

PARTICULAS DE POEIRA: 3-4 pixels de terra subindo das rachaduras (marrom-terra,
1x1 ou 2x2px, dispersos).

NADA mais visivel acima do chao. Apenas a promessa de algo ENORME vindo de baixo.

O chao esta AVISANDO. A terra sabe o que vem.
```

### Frame 2 -- Chao Quebrando
```
64x64px.

Rachaduras EXPANDIRAM (2px de largura agora). Pedacos de chao comecam a LEVANTAR
(3-4 blocos de terra, 4x4px cada, flutuando 2-4px acima da superficie).

PONTA DA MONTANHA comeca a aparecer: no centro do frame, emergindo do chao,
APENAS o TOPO PLANO do Roraima e visivel (4-6px de altura acima do solo).
Cor da pedra: cinza escuro (#555555) com linhas grossas (#2A2A2A).
Textura: cross-hatching pesado (rocha antiga).

Poeira MASSIVA: 8-10 particulas de terra voando para cima e para os lados.
Cores: marrom (#8B6914), cinza (#808080), verde musgo (#556B2F).

Screen shake comeca aqui (indicado para implementacao, nao visual no sprite).
```

### Frame 3 -- Emergencia (Tepui Visivel)
```
64x64px.

A montanha emergiu ~25% da altura total. A forma de TEPUI e agora RECONHECIVEL:

TOPO PLANO: 40px de largura no topo do sprite, 6-8px de espessura.
Superficie: textura de rocha com POCINHAS D'AGUA (3-4 pixels azul claro #87CEEB).
Vegetacao: 2-3 tufos de verde escuro (#2D5A27) no topo.

PAREDES: quase verticais, 90 graus. Pedra cinza-escura (#444444) com estratos
horizontais visiveis (linhas de camada geologica, 1px cada, alternando cinza
claro e escuro). Cross-hatching PESADO.

BASE (ainda enterrada): linha do solo EXPLODIU. Blocos de terra e pedra voando
(6-8 particulas, maiores que frame 2, 4x4 a 6x6px). Poeira densa.

CACHOEIRA: uma linha de agua (#87CEEB, 1px) comecando a cair da borda esquerda.
```

### Frame 4 -- Ascensao (50% Emergido)
```
64x64px.

Montanha em 50% da emergencia. IMPOE RESPEITO.

TOPO: mesma textura, agora com MAIS detalhe. Cristais de quartzo visiveis
(2-3 pixels brancos brilhantes #E0E0FF no topo). Vegetacao definida.
Marca de CRUZ dourada (#FFD700) no centro do topo (onde Daciolo vai ficar).

PAREDES: mais expostas (24-28px de parede visivel). Estratos geologicos claros.
Uma CAVERNA pequena visivel na face frontal (abertura escura 3x2px, #1A1A1A).
Musgo/liquen nas paredes (manchas verde-escuro irregulares).

CACHOEIRAS: DUAS agora -- esquerda e direita. Linhas de agua (#87CEEB) descendo
das bordas do topo. Respingos de agua na base (particulas azul-claras).

BASE: terra e rocha continuam voando, mas menos intenso (montanha ja deslocou
o grosso do solo). Rachadura no chao EXPANDIU para 48px de diametro.

NUVENS: wisps de nevoa branca (#FFFFFF @ 30%) comecam a se formar ao redor
do terco superior da montanha (altitude -- nuvens de condensacao).
```

### Frame 5 -- Completa (Montanha Total)
```
64x64px. A MONTANHA COMPLETA.

COMPOSICAO VERTICAL:
- Topo (8px): plato plano, vegetacao, cristais, marca de cruz dourada, pocinhas
- Paredes (36px): falesias verticais, estratos, caverna, musgo, cachoeiras
- Base (12px): rocha exposta + cratera no chao + poeira residual
- Espaco para Daciolo (8px): area no topo onde o sprite do Daciolo vai ficar

TOPO DETALHADO:
- Superficie: cinza-medio (#666666) com textura de rocha plana
- Cristais de quartzo: 4-5 pontos brancos brilhantes (#E0E0FF), 2x2px
- Vegetacao: 3-4 arbustos (verde escuro #2D5A27, 3x3px cada)
- Pocinhas: 2-3 areas de agua (#87CEEB, 4x2px cada)
- Cruz dourada: centro do topo, 5x5px, brilhando (#FFD700 com glow 1px)

PAREDES DETALHADAS:
- Rocha base: cinza escuro (#444444)
- Estratos: 6-8 linhas horizontais alternando #555555 e #3C3C3C
- Caverna: abertura 4x3px, interior preto
- Musgo: manchas irregulares #2D5A27, espalhadas
- Cachoeiras: 2 linhas de agua, esquerda e direita, #87CEEB, 1px largura
- Respingos: 3-4 particulas de agua na base de cada cachoeira

BASE:
- Cratera circular (~48px diametro) no chao
- Rochas expostas nas bordas da cratera
- Poeira residual (particulas menores, dispersando)
- Brilho dourado na marca de cruz no chao (reflexo da cruz do topo)

NUVENS:
- 4-5 wisps de nevoa (#FFFFFF @ 20-40%) ao redor do terco superior
- Parcialmente cobrindo as paredes (efeito de altitude)

ESCALA: a montanha ocupa QUASE TODO o frame 64x64. E MASSIVA. Imponente.
Mesmo em pixel art minusculo, deve parecer ENORME e SAGRADA.
```

### Frame 6 -- Chuva de Fogo 1 (Fogo Nasce no Topo)
```
64x64px.

Montanha IDENTICA ao Frame 5, mas com ADICOES:

FOGO SANTO no topo: 3-4 bolas de fogo nascendo da marca de cruz dourada.
Cada bola: 3x3px, cor gradiente #FFD700 (dourado) -> #FF8C00 (laranja).
Trail de 2px dourado atras de cada bola.

As bolas estao no INICIO da trajetoria -- ainda proximas ao topo, comecando
a descender. Direcoes: dispersas radialmente (caem para fora da montanha).

GLOW no topo: a area ao redor da marca de cruz fica MAIS BRILHANTE
(overlay dourado #FFD700 @ 40% numa area de 12x12px).

Daciolo (NAO incluso neste sprite, mas a area dele no topo deve estar CLARA
para ele ser visivel): silhueta de referencia 8x8px com bracos abertos.

Os cristais de quartzo no topo brilham MAIS INTENSO (reacao a energia divina).
```

### Frame 7 -- Chuva de Fogo 2 (Intensidade Maxima)
```
64x64px.

Montanha base identica, mas:

CHUVA DE FOGO INTENSA: 8-10 bolas de fogo em VARIOS ESTAGIOS de queda:
- 2-3 nascendo no topo (3x3px, perto da cruz)
- 3-4 no meio do caminho (descendo pelas laterais da montanha)
- 2-3 proximas ao chao (prestes a impactar)

Cada bola: gradiente de cor conforme altura:
- Topo: branco-dourado (#FFFACD) -- nascimento
- Meio: dourado (#FFD700) -- descida
- Chao: laranja (#FF8C00) -- pre-impacto

IMPACTOS no chao (base do sprite): 2-3 marcas de CRUZ (+) de fogo nos pontos
onde bolas ja atingiram. Cada cruz: 4x4px, dourado (#FFD700) com glow de 1px.

O TOPO INTEIRO da montanha brilha dourado (energia divina maxima).
Nuvens ao redor ficam DOURADAS (tingidas pela luz do fogo santo).

ESTE E O FRAME DE LOOP durante a duracao da chuva de fogo (com Frame 6).
```

### Frame 8 -- Descida (Montanha Afundando)
```
64x64px.

Montanha comecando a AFUNDAR de volta no chao.

TOPO: ainda visivel, mas 10px MAIS BAIXO que no Frame 5. Brilho divino
diminuindo (glow dourado reduz). Fogo santo parando (1-2 bolas residuais).
Cruz dourada comeca a DESVANECER.

PAREDES: metade inferior ja DENTRO DO CHAO (nao visivel). Cachoeiras pararam.
Nuvens dissipando.

BASE: terra FECHANDO ao redor da montanha. Solo se reconstituindo parcialmente.
Particulas de terra CAINDO (gravidade, para baixo desta vez).

CRATERA RESIDUAL: no chao, a forma da montanha deixou uma MARCA. Formato
circular/ovalado, com uma CRUZ DOURADA no centro (marca permanente por 5s).
Brilho na cratera: #FFD700 @ 30%, diminuindo.

POEIRA FINAL: nuvem de poeira subindo do fechamento do chao (particulas
marrons, ascendentes).

A montanha RETORNA. A terra aceita de volta o que emprestou.
Mas a marca fica. A fe deixa MARCAS.
```

---

## Implementacao Phaser 3

### Criacao e Animacao

```javascript
// Preload
this.load.spritesheet('monte-roraima', 'assets/personagens/daciolo/animations/monte-roraima-sheet.png', {
    frameWidth: 64,
    frameHeight: 64
});

// Create animation
this.anims.create({
    key: 'monte-roraima-emerge',
    frames: this.anims.generateFrameNumbers('monte-roraima', { start: 0, end: 4 }),
    frameRate: 10,
    repeat: 0
});

this.anims.create({
    key: 'monte-roraima-fire',
    frames: this.anims.generateFrameNumbers('monte-roraima', { frames: [5, 6] }),
    frameRate: 8,
    repeat: -1  // loop durante chuva de fogo
});

this.anims.create({
    key: 'monte-roraima-descend',
    frames: this.anims.generateFrameNumbers('monte-roraima', { frames: [7] }),
    frameRate: 10,
    repeat: 0
});
```

### Sequencia Completa

```javascript
function spawnMonteRoraima(scene, x, y) {
    const montanha = scene.add.sprite(x, y + 16, 'monte-roraima');
    montanha.setOrigin(0.5, 1.0);  // ancora na base
    montanha.setDepth(scene.daciolo.depth - 1);

    // Fase 1: Emergencia (frames 0-4)
    montanha.play('monte-roraima-emerge');

    // Screen shake durante emergencia
    scene.cameras.main.shake(1500, 0.005);

    // Particulas de terra voando
    const terraEmitter = scene.add.particles('terra-particle').createEmitter({
        x: x,
        y: y + 20,
        speed: { min: 30, max: 100 },
        angle: { min: 200, max: 340 },  // para cima e lados
        scale: { start: 0.6, end: 0.1 },
        tint: [0x8B6914, 0x808080, 0x556B2F],
        lifespan: 1200,
        frequency: 25,
        quantity: 4,
        gravityY: 50  // caem depois de subir
    });

    // Rochas maiores (sprites separados)
    for (let i = 0; i < 5; i++) {
        scene.time.delayedCall(i * 80, () => {
            const rocha = scene.add.rectangle(
                x + Phaser.Math.Between(-24, 24),
                y + 16,
                Phaser.Math.Between(3, 7),
                Phaser.Math.Between(3, 7),
                Phaser.Utils.Array.GetRandom([0x8B6914, 0x555555, 0x666666])
            );
            scene.tweens.add({
                targets: rocha,
                x: rocha.x + Phaser.Math.Between(-40, 40),
                y: rocha.y - Phaser.Math.Between(20, 50),
                angle: Phaser.Math.Between(0, 360),
                alpha: 0,
                duration: 800,
                ease: 'Quad.easeOut',
                onComplete: () => rocha.destroy()
            });
        });
    }

    // Montanha sobe (tween de posicao)
    montanha.y = y + 48;  // comeca abaixo
    scene.tweens.add({
        targets: montanha,
        y: y - 16,  // posicao final (acima do chao)
        duration: 1500,
        ease: 'Back.easeOut'
    });

    // Fase 2: Chuva de fogo (apos emergencia completa)
    montanha.on('animationcomplete-monte-roraima-emerge', () => {
        terraEmitter.stop();

        // Transicao para loop de fogo
        montanha.play('monte-roraima-fire');

        // Bolas de fogo santo (particulas separadas)
        const fogoEmitter = scene.add.particles('fogo-santo').createEmitter({
            x: { min: x - 20, max: x + 20 },
            y: y - 40,  // topo da montanha
            speed: { min: 30, max: 70 },
            angle: { min: 60, max: 120 },  // para baixo, espalhado
            scale: { start: 0.5, end: 0.2 },
            tint: [0xFFD700, 0xFF8C00, 0xFFFFFF],
            lifespan: { min: 600, max: 1000 },
            frequency: 80,
            quantity: 2,
            gravityY: 80,  // acelerao caindo
            blendMode: Phaser.BlendModes.ADD
        });

        // Impactos de cruz no chao
        const impactTimer = scene.time.addEvent({
            delay: 200,
            callback: () => {
                const impX = x + Phaser.Math.Between(-60, 60);
                const impY = y + Phaser.Math.Between(20, 50);

                // Cruz de fogo
                const cruzH = scene.add.rectangle(impX, impY, 8, 2, 0xFFD700, 0.8);
                const cruzV = scene.add.rectangle(impX, impY, 2, 8, 0xFFD700, 0.8);
                cruzH.setBlendMode(Phaser.BlendModes.ADD);
                cruzV.setBlendMode(Phaser.BlendModes.ADD);

                scene.tweens.add({
                    targets: [cruzH, cruzV],
                    alpha: 0,
                    scale: 1.5,
                    duration: 600,
                    onComplete: () => { cruzH.destroy(); cruzV.destroy(); }
                });

                // Dano AoE no ponto
                scene.applyPointDamage(impX, impY, 16, 40);

                // Flash de impacto
                const flash = scene.add.circle(impX, impY, 6, 0xFFD700, 0.5);
                flash.setBlendMode(Phaser.BlendModes.ADD);
                scene.tweens.add({
                    targets: flash,
                    alpha: 0, scale: 2,
                    duration: 200,
                    onComplete: () => flash.destroy()
                });
            },
            repeat: 19  // 20 impactos durante duracao
        });

        // Fase 3: Descida (apos duracao da chuva)
        scene.time.delayedCall(4000, () => {
            fogoEmitter.stop();
            impactTimer.remove();

            montanha.play('monte-roraima-descend');

            // Montanha afunda
            scene.tweens.add({
                targets: montanha,
                y: y + 48,
                alpha: 0,
                duration: 1200,
                ease: 'Quad.easeIn',
                onComplete: () => {
                    montanha.destroy();

                    // Particulas de fechamento do chao
                    const fechamentoEmitter = scene.add.particles('terra-particle').createEmitter({
                        x: x,
                        y: y + 20,
                        speed: { min: 10, max: 30 },
                        angle: { min: 250, max: 290 },
                        scale: { start: 0.4, end: 0 },
                        tint: [0x8B6914, 0x808080],
                        lifespan: 600,
                        frequency: 40,
                        quantity: 3
                    });
                    scene.time.delayedCall(800, () => fechamentoEmitter.stop());

                    // Cratera residual com cruz
                    const cratera = scene.add.sprite(x, y + 16, 'cratera-cruz');
                    cratera.setAlpha(0.6);
                    scene.tweens.add({
                        targets: cratera,
                        alpha: 0,
                        duration: 5000,
                        delay: 2000,
                        onComplete: () => cratera.destroy()
                    });
                }
            });
        });
    });

    return montanha;
}
```

---

## Paleta de Cores da Montanha

| Elemento | Cor | Hex |
|---|---|---|
| Rocha base | Cinza escuro | `#444444` |
| Rocha clara | Cinza medio | `#666666` |
| Rocha sombra | Cinza muito escuro | `#2A2A2A` |
| Estratos claros | Cinza claro | `#555555` |
| Estratos escuros | Cinza | `#3C3C3C` |
| Contorno | Preto | `#1A1A1A` |
| Musgo/Vegetacao | Verde escuro | `#2D5A27` |
| Agua/Cachoeiras | Azul celeste | `#87CEEB` |
| Cristais quartzo | Branco translucido | `#E0E0FF` |
| Cruz dourada topo | Dourado | `#FFD700` |
| Terra voando | Marrom | `#8B6914` |
| Terra escura | Marrom escuro | `#5C4033` |
| Nuvens | Branco | `#FFFFFF` @ 20-40% |
| Fogo santo | Dourado -> Laranja | `#FFD700` -> `#FF8C00` |
| Fogo nascendo | Branco-dourado | `#FFFACD` |
| Impacto cruz | Dourado | `#FFD700` |
| Cratera residual | Dourado suave | `#FFD700` @ 30% |

---

## Efeitos de Camera

```javascript
// Durante toda a sequencia do Monte Roraima
const cameraEffects = {
    // Fase 1: Emergencia
    emergence: {
        shake: { duration: 1500, intensity: 0.005 },
        zoom: { target: 0.9, duration: 800 }  // leve zoom out
    },
    // Fase 2: Chuva de fogo
    fire: {
        shake: { duration: 200, intensity: 0.002, repeat: true },  // tremor continuo leve
        zoom: { target: 0.85, duration: 500 }  // mais zoom out para ver area de fogo
    },
    // Fase 3: Descida
    descent: {
        shake: { duration: 800, intensity: 0.003 },
        zoom: { target: 1.0, duration: 1000 }  // volta ao normal
    }
};
```

---

## Colisao e Interacao

```javascript
// A montanha e um obstaculo fisico enquanto existe
function setupMontanhaCollision(scene, montanha) {
    // Hitbox: retangulo na base da montanha
    const hitbox = scene.physics.add.staticBody(
        montanha.x - 20, montanha.y - 48,
        40, 48
    );

    // Inimigos nao podem passar ATRAVES da montanha
    scene.physics.add.collider(scene.enemies, hitbox);

    // Aliados tambem nao (exceto Daciolo, que esta NO TOPO)
    scene.physics.add.collider(scene.allies, hitbox, null, (ally) => {
        return ally !== scene.daciolo;  // Daciolo passa
    });

    // Destruir hitbox quando montanha desaparece
    montanha.on('destroy', () => hitbox.destroy());
}
```

---

## Notas de Arte

1. O Monte Roraima deve ser RECONHECIVEL mesmo em 64x64 -- o topo plano e a chave
2. As paredes verticais sao ESSENCIAIS para a forma de tepui
3. Cross-hatching nas rochas seguindo estilo Andre Guedes (nao textura suave)
4. As cachoeiras sao um detalhe REAL do Roraima -- mantê-las adiciona autenticidade
5. Os cristais de quartzo sao reais tambem -- o Roraima e famoso por eles
6. A cruz dourada no topo e o toque DACIOLO -- ele santificou a montanha
7. A chuva de fogo e DOURADA, nao vermelha -- e FOGO SANTO, nao fogo infernal
8. O efeito de emergencia deve parecer VIOLENTO (terra voando) mas DIVINO (brilho dourado)
9. A cratera residual com cruz e a "assinatura" que Daciolo deixa no mapa
