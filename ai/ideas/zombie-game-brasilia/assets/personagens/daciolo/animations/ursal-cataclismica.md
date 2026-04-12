# URSAL CATACLISMICA -- Animacao do Ultimate
### A Conspiração que Virou Arma de Destruição em Massa | O Ataque Definitivo
### Zumbis de Brasilia | Abril 2026

---

> *"A URSAL nao existe? Entao explica como ela acabou de cair do ceu e esmagar 47 zumbis. EXPLICA. Ah, nao consegue? Entao talvez o Daciolo estivesse certo esse tempo todo. O maluco que todo mundo chamou de louco e o unico que tem uma arma nuclear no bolso."*

---

## Specs Tecnicas

| Propriedade | Valor |
|---|---|
| Tamanho por frame | 128x128px (MAIOR que sprites normais -- ultimate merece) |
| Total de frames | 8 |
| Sheet total | 1024x128px (horizontal) |
| Formato | PNG com transparencia |
| Frame rate | 8 fps (cinematico, pesado, cada frame conta) |
| Loop | Nao (single play, absolutamente nao repete) |
| Tipo | Overlay de cenario (renderizado ACIMA de quase tudo) |
| Blend mode | Normal para o mapa, ADD para explosao/efeitos |
| Depth | Maximo (acima de tudo exceto UI) |

**NOTA**: Este sprite e 128x128, NAO 64x64. O ultimate do Daciolo merece
DOBRO do espaco visual. O mapa da URSAL PRECISA de espaco para ser legivel.

---

## Design do Mapa da URSAL

Antes dos frames, a especificacao do MAPA propriamente dito:

### O Mapa (Objeto Central)

```
Forma: Contorno da AMERICA DO SUL + AMERICA CENTRAL + CARIBE + MEXICO
Estilo: PROPAGANDA SOVIETICA parodiada

Detalhes do mapa:
- Contorno GROSSO (3px preto)
- Interior: vermelho escuro (#CC0000) uniforme
- Fronteiras entre paises: linhas pontilhadas brancas (1px)
- Texto "URSAL" no centro do continente:
  - Fonte: bold, GRANDE (ocupa ~30% da largura do mapa)
  - Cor: branco (#FFFFFF) com outline preto
  - Estilo: tipografia sovietica/construtivista
- Estrelas vermelhas (★) nos cantos:
  - 4 estrelas, uma em cada quadrante
  - Cor: vermelho mais claro (#FF0000) sobre fundo vermelho escuro
  - Tamanho: 6x6px cada
- Detalhes parodicos:
  - "UNIAO DAS REPUBLICAS SOCIALISTAS DA AMERICA LATINA" em texto minusculo
    curvando ao redor da borda (ILEGIVEL no tamanho real -- easter egg)
  - Foice e martelo minuscula substituida por CHINELO E VASSOURA (humor)
  - Seta apontando para Brasilia com "SEDE" escrito
  - Bandeirinha do Brasil no ponto de Brasilia

Estetica: o mapa deve parecer um POSTER DE PROPAGANDA REAL, mas ERRADO.
Como se alguem com conhecimento limitado de design sovietico tentasse
fazer um panfleto de conspiração. DELIBERADAMENTE amador. Andre Guedes
desenhando propaganda comunista com humor.
```

---

## Frame-by-Frame

### Frame 1 -- Sombra Crescente no Chao
```
128x128px.

NADA no ceu ainda. O frame mostra APENAS o CHAO (perspectiva isometrica top-down).

No centro do frame: SOMBRA comecando a se formar. Formato: vago, amorfo,
mas insinuando uma forma CONTINENTAL. Cor: preto (#000000) com opacity 15%.
Tamanho: 30x20px (pequena ainda).

Bordas da sombra: difusas (gradiente de opacity, nao sharp).

Ao redor da sombra: textura de chao normal (piso da Esplanada dos Ministerios,
cinza-claro #CCCCCC com linhas de ladrilho #AAAAAA).

VENTO visual: 3-4 linhas curvas ascendentes (1px, branco @ 40%) indicando
movimento de ar para CIMA. Algo esta deslocando o ar ao descer.

ILUMINACAO: o frame inteiro esta levemente mais ESCURO que o normal
(overlay preto 10% -- ceu escurecendo).

O jogador olha para cima sem ver nada. Mas a sombra DIZ: algo vem.
```

### Frame 2 -- Sombra Definida + Ceu Escuro
```
128x128px.

SOMBRA: cresceu para 60x40px. Agora a forma e RECONHECIVEL como America do Sul.
O contorno da costa leste brasileira e VISIVEL na sombra. Opacity: 30%.

CEU (metade superior do frame): ficou SIGNIFICATIVAMENTE mais escuro.
Overlay preto 25%. Nuvens escuras (#333333 @ 50%) nos cantos superiores.

VENTO: intensificou. 6-8 linhas de vento. Particulas de poeira sendo PUXADAS
para cima (detritos ascendentes). Papeis voando.

CHAO: textura normal, mas com iluminacao dramatica (sombra longa do mapa
projetando na diagonal).

TENSAO crescente. O ceu esta caindo. Literalmente.
```

### Frame 3 -- Mapa Aparece no Topo
```
128x128px.

O MAPA DA URSAL aparece no TOPO DO FRAME. Posicao: parcialmente visivel
(30-40% do mapa dentro do frame, restante "acima" fora de quadro).

MAPA: seguindo design especificado acima. Vermelho escuro, URSAL em branco,
estrelas, contorno grosso. O mapa esta INCLINADO levemente (10 graus --
nao cai reto, cai com angulo, mais dramatico).

SOMBRA: 80x55px. Quase forma completa do continente. Opacity 45%.
Definicao clara da forma.

ESCALA do mapa: MASSIVO. O mapa e 80% da largura do frame. IMPOE dominancia.

EFEITO ATMOSFERICO: ao redor do mapa, RAIOS (relampagos) -- 2-3 linhas
brancas (#FFFFFF) em zigzag saindo do mapa para baixo. O mapa carrega
ENERGIA CATACLISMICA.

Texto "URSAL" ja e LEGIVEL, pulsando levemente (vermelho mais claro #FF0000
alternando com o branco base -- 1 ciclo por frame).

VENTO EXTREMO: tudo no chao esta sendo afetado. Arvores (se existirem no
cenario) vergam. Detritos voam horizontalmente. Caos atmosferico.
```

### Frame 4 -- Mapa em Descida Acelerada
```
128x128px.

MAPA: agora 70% visivel dentro do frame. DESCENDO RAPIDO. Motion blur na
borda inferior do mapa (3-4px de blur vertical, indicando velocidade).

DETALHES DO MAPA VISIVEIS:
- Fronteiras entre paises (linhas pontilhadas brancas)
- Estrelas nos cantos (★) pulsando vermelho
- "URSAL" totalmente legivel, GRANDE, IMPONENTE
- Seta para Brasilia com "SEDE" (se o zoom permitir)
- O mapa parece SOLIDO -- como se fosse feito de pedra/metal/concreto

SOMBRA: 100x70px. COMPLETA. Forma continental perfeita. Opacity 60%.
Escuridao no chao cresce. Os inimigos NAO podem ver isso porque estao
DEBAIXO da sombra. O jogador vê de fora.

TREMOR: chao comecando a RACHAR pela pressao atmosferica. 3-4 linhas
de rachadura radiando do centro da sombra.

SONS VISUAIS: linhas de choque (ring) ao redor do mapa (onda de pressao
atmosferica precedendo o impacto). 2 rings, brancos, expandindo para baixo.

Neste frame, tudo esta em PANICO VISUAL. A escala do desastre e CLARA.
```

### Frame 5 -- IMPACTO
```
128x128px. O FRAME MAIS IMPORTANTE DO JOGO.

EXPLOSAO TOTAL.

Composicao: o frame e dominado por LUZ e DESTRUICAO.

FLASH CENTRAL: circulo branco (#FFFFFF) de 40px de raio no ponto de impacto.
Opacity: 90%. O flash CEGA -- domina o frame. Dentro do flash: NADA visivel
(whiteout total).

ONDA DE CHOQUE: 3 aneis concentricos expandindo do centro:
- Anel 1 (mais proximo): branco-amarelo (#FFFFF0), 3px largura, raio 30px
- Anel 2 (medio): dourado (#FFD700), 2px largura, raio 50px
- Anel 3 (externo): vermelho (#CC0000), 1px largura, raio 70px
  (VERMELHO porque e a URSAL -- ate a onda de choque e vermelha)

FRAGMENTOS DE MAPA: o mapa se DESPEDACOU no impacto. 15-20 fragmentos
voando radialmente:
- Pedacos de continente (formas irregulares, 4x4 a 8x8px)
- Cores: vermelho (#CC0000), verde (#228B22, referencia a bandeiras)
- Rotacao: cada pedaco gira enquanto voa
- Trail de fumaca atras de cada pedaco

LETRAS "URSAL": as letras SEPARARAM -- cada letra voa independentemente:
- U -- para cima-esquerda
- R -- para cima
- S -- para cima-direita
- A -- para direita
- L -- para baixo-direita
  Cada letra: branca com outline vermelho, girando, trail de fumaca

CHAO: CRATERA formando. Centro: escuro (#1A1A1A), circular, 50px diametro.
Poeira/detritos voando para TODAS as direcoes. Terra, pedra, concreto
(do piso da Esplanada) -- particulas de 2x2 a 5x5px.

SCREEN SHAKE: maximo possivel. Este frame TREME.

ESTE FRAME DEVE SER A COISA MAIS VISUALMENTE VIOLENTA DO JOGO INTEIRO.
Mas tambem a mais ENGRAÇADA. Porque e um MAPA DE CONSPIRAÇÃO caindo do ceu.
```

### Frame 6 -- Devastacao (Pos-Impacto)
```
128x128px.

A poeira comeca a baixar. A destruicao e VISIVEL.

CRATERA: forma completa no centro. Formato de AMERICA DO SUL (!) no chao.
A cratera HERDOU a forma do mapa que impactou. Detalhes:
- Contorno da cratera: borda elevada de terra/entulho (3-4px, marrom #8B4513)
- Interior: escuro (#2A2A2A) com rachaduras vermelhas (magma? Comunismo? Ambos?)
- "URSAL" escrito em NEON VERMELHO no centro da cratera:
  - Letras: #CC0000 com glow de 3px (#FF0000 @ 60%)
  - PISCANDO: on-off-on-off (250ms ciclo)
  - As letras sao feitas de LUZ -- projetadas na cratera como laser

ONDA DE CHOQUE: 2o e 3o anel ainda expandindo (no limite do frame).
Tudo que a onda toca: DESTRUIDO ou EMPURRADO.

FRAGMENTOS: continuam voando mas desacelerando. Menores. Menos.
Fumaca densa ao redor da cratera (#333333 @ 50%, wisps grandes).

INIMIGOS: onde havia inimigos, agora ha PARTICULAS. Silhuetas de destruicao.
Pop-offs de score/XP subindo (+100, +200, etc).

O SILENCIO VISUAL pos-explosao. Tudo parou. So a poeira se move. E as letras
URSAL piscam no chao como um letreiro de neon quebrado. Macabro. Hilario.
```

### Frame 7 -- Aftermath (Poeira Baixando)
```
128x128px.

80% da poeira baixou. A cena e CLARA.

CRATERA: completamente visivel. Forma continental. Glow vermelho diminuindo
mas ainda presente. "URSAL" piscando mais lento (500ms ciclo).

CAMPO DE DESTRUICAO ao redor da cratera:
- Detritos espalhados (fragmentos de mapa, 2-3px, vermelhos/verdes)
- Rachaduras no chao radiais (partindo da cratera, 3-4 linhas de 20px cada)
- Fumaca residual (wisps finos, subindo lentamente)
- Nenhum inimigo vivo na area (total annihilation)

DETALHES COMICOS no aftermath:
- Um santinho do Daciolo intacto (2x3px, branco) flutuando no meio da destruicao
- Uma estrela vermelha do mapa cravada no chao como shuriken (★)
- "SEDE" com seta ainda visivel num fragmento (apontando para a cratera)

ATMOSFERA: ceu voltando ao normal. Overlay escuro reduzindo (15% -> 5%).
Luz voltando. A tempestade passou.

Daciolo (NAO neste sprite, mas referenciado): caminhando DE VOLTA para o
centro da cratera. Silhueta distante com aureola brilhando.
```

### Frame 8 -- Letras Desvanecem / Cratera Fecha
```
128x128px.

RESOLUCAO da cena.

CRATERA: comecando a FECHAR. Bordas se aproximando do centro. Terra preenchendo.
A forma continental se desfaz.

"URSAL": letras em FADE OUT final. Piscam 3x mais rapidas e depois APAGAM.
Ultimo flash: branco (nao vermelho) -- purificacao.

RESIDUAL:
- Marca circular no chao onde a cratera estava (cicatriz, #8B6914 @ 30%)
- Wisps finais de fumaca
- 1-2 fragmentos de mapa restantes no chao (coletaveis? easter egg?)
- Brilho dourado no centro (onde Daciolo vai ficar para pose de victoria)

ATMOSFERA: completamente normalizada. Ceu claro. Luz natural.

PARTICULAS FINAIS: 8-10 pontos de luz DOURADA (#FFD700) subindo do centro
da antiga cratera -- como se a terra AGRADECESSE a purificacao. Ou como se
a alma da URSAL estivesse subindo ao ceu. Interpretacao livre.

O frame fecha com PAZ. Apos a destruicao total, a calma. Apos a URSAL,
a fe. Apos o caos, a GLORIA.
```

---

## Implementacao Phaser 3

### Preload (Sprite maior que normal)

```javascript
// O sprite da URSAL e 128x128, nao 64x64
this.load.spritesheet('ursal-map', 'assets/personagens/daciolo/animations/ursal-sheet.png', {
    frameWidth: 128,
    frameHeight: 128
});

// Mapa independente (para descida)
this.load.image('ursal-map-static', 'assets/personagens/daciolo/animations/ursal-map.png');
```

### Sequencia Completa do Ultimate

```javascript
function executeURSALCataclismica(scene, daciolo) {
    const cx = daciolo.x;
    const cy = daciolo.y;

    // Container para toda a sequencia
    const ursalContainer = scene.add.container(cx, cy);
    ursalContainer.setDepth(1000);  // acima de TUDO

    // ============================================
    // FASE 0: Daciolo grita (pre-animacao)
    // ============================================
    scene.sound.play('daciolo-a-ursal-existe');

    // ============================================
    // FASE 1: SOMBRA CRESCENTE (Frames 1-2) ~500ms
    // ============================================

    // Sombra no chao
    const sombra = scene.add.ellipse(0, 0, 20, 14, 0x000000, 0.15);
    ursalContainer.add(sombra);

    scene.tweens.add({
        targets: sombra,
        scaleX: 12,
        scaleY: 10,
        alpha: 0.5,
        duration: 1000,
        ease: 'Quad.easeIn'
    });

    // Ceu escurece
    const darkSky = scene.add.rectangle(
        scene.cameras.main.centerX, scene.cameras.main.centerY,
        scene.cameras.main.width * 2, scene.cameras.main.height * 2,
        0x000000, 0
    ).setScrollFactor(0).setDepth(999);

    scene.tweens.add({
        targets: darkSky,
        alpha: 0.4,
        duration: 800
    });

    // Vento ascendente
    const ventoEmitter = scene.add.particles('debris').createEmitter({
        x: { min: cx - 80, max: cx + 80 },
        y: { min: cy + 40, max: cy + 60 },
        speed: { min: 20, max: 50 },
        angle: { min: 250, max: 290 },  // para cima
        scale: { start: 0.3, end: 0 },
        tint: [0xCCCCCC, 0x999999],
        lifespan: 800,
        frequency: 40,
        quantity: 2
    });

    // ============================================
    // FASE 2: MAPA DESCE (Frames 3-4) ~500ms
    // ============================================

    scene.time.delayedCall(500, () => {
        // Mapa da URSAL como sprite
        const mapa = scene.add.sprite(cx, cy - 300, 'ursal-map-static');
        mapa.setDepth(1001);
        mapa.setScale(0.3);
        mapa.setAngle(-10);  // levemente inclinado

        // Relampagos ao redor do mapa
        const relampago = scene.time.addEvent({
            delay: 150,
            callback: () => {
                const lightning = scene.add.graphics();
                lightning.lineStyle(2, 0xFFFFFF, 0.8);
                lightning.beginPath();
                const lx = mapa.x + Phaser.Math.Between(-40, 40);
                let ly = mapa.y + 20;
                lightning.moveTo(lx, ly);
                for (let i = 0; i < 4; i++) {
                    ly += Phaser.Math.Between(10, 25);
                    lightning.lineTo(lx + Phaser.Math.Between(-15, 15), ly);
                }
                lightning.strokePath();
                lightning.setDepth(1002);
                scene.tweens.add({
                    targets: lightning,
                    alpha: 0,
                    duration: 100,
                    onComplete: () => lightning.destroy()
                });
            },
            repeat: 6
        });

        // Texto URSAL pulsando no mapa
        const ursalText = scene.add.text(mapa.x, mapa.y, 'URSAL', {
            fontSize: '20px',
            color: '#FFFFFF',
            fontStyle: 'bold',
            stroke: '#CC0000',
            strokeThickness: 3
        }).setOrigin(0.5).setDepth(1002);

        // Mapa desce (tween principal)
        scene.tweens.add({
            targets: [mapa, ursalText],
            y: cy,
            duration: 600,
            ease: 'Quad.easeIn'
        });

        scene.tweens.add({
            targets: mapa,
            scale: 2.5,
            duration: 600,
            ease: 'Quad.easeIn'
        });

        // Camera zoom out
        scene.cameras.main.zoomTo(0.6, 400);

        // Tremor crescente
        scene.cameras.main.shake(600, 0.003);

        // ============================================
        // FASE 3: IMPACTO (Frame 5) -- O MOMENTO
        // ============================================

        scene.time.delayedCall(600, () => {
            relampago.remove();
            ventoEmitter.stop();

            // === FLASH NUCLEAR ===
            scene.cameras.main.flash(300, 255, 255, 255, false, 1.0);

            // === SCREEN SHAKE MAXIMO ===
            scene.cameras.main.shake(600, 0.015);

            // === ONDA DE CHOQUE ===
            const shockColors = [0xFFFFF0, 0xFFD700, 0xCC0000];
            const shockWidths = [3, 2, 1];
            for (let i = 0; i < 3; i++) {
                scene.time.delayedCall(i * 60, () => {
                    const ring = scene.add.circle(cx, cy, 10, shockColors[i], 0);
                    ring.setStrokeStyle(shockWidths[i], shockColors[i], 0.9 - i * 0.2);
                    ring.setDepth(1003);
                    scene.tweens.add({
                        targets: ring,
                        radius: 200 + i * 40,
                        alpha: 0,
                        duration: 500,
                        onComplete: () => ring.destroy()
                    });
                });
            }

            // === FRAGMENTOS DO MAPA VOANDO ===
            mapa.setVisible(false);
            ursalText.setVisible(false);

            for (let i = 0; i < 20; i++) {
                const fragW = Phaser.Math.Between(4, 10);
                const fragH = Phaser.Math.Between(4, 10);
                const fragColor = Phaser.Utils.Array.GetRandom([0xCC0000, 0x228B22, 0xFFD700, 0x0033CC]);
                const frag = scene.add.rectangle(cx, cy, fragW, fragH, fragColor, 0.9);
                frag.setDepth(1003);

                const angle = Phaser.Math.DegToRad(Phaser.Math.Between(0, 360));
                const dist = Phaser.Math.Between(60, 160);

                scene.tweens.add({
                    targets: frag,
                    x: cx + Math.cos(angle) * dist,
                    y: cy + Math.sin(angle) * dist,
                    angle: Phaser.Math.Between(0, 720),
                    alpha: 0,
                    scale: 0.3,
                    duration: Phaser.Math.Between(600, 1200),
                    ease: 'Quad.easeOut',
                    onComplete: () => frag.destroy()
                });
            }

            // === LETRAS VOANDO SEPARADAMENTE ===
            const letters = ['U', 'R', 'S', 'A', 'L'];
            const letterAngles = [-135, -90, -45, 0, 45];
            letters.forEach((letter, i) => {
                const letterSprite = scene.add.text(cx + (i - 2) * 8, cy, letter, {
                    fontSize: '14px', color: '#FFFFFF',
                    stroke: '#CC0000', strokeThickness: 2, fontStyle: 'bold'
                }).setOrigin(0.5).setDepth(1003);

                const lAngle = Phaser.Math.DegToRad(letterAngles[i]);
                scene.tweens.add({
                    targets: letterSprite,
                    x: cx + Math.cos(lAngle) * 120,
                    y: cy + Math.sin(lAngle) * 120,
                    angle: Phaser.Math.Between(-180, 180),
                    alpha: 0,
                    duration: 1000,
                    onComplete: () => letterSprite.destroy()
                });
            });

            // === DETRITOS E POEIRA ===
            const detritosEmitter = scene.add.particles('debris').createEmitter({
                x: cx, y: cy,
                speed: { min: 40, max: 120 },
                angle: { min: 0, max: 360 },
                scale: { start: 0.6, end: 0.1 },
                tint: [0x8B4513, 0x808080, 0xCCCCCC, 0x555555],
                lifespan: { min: 500, max: 1200 },
                quantity: 30,
                maxParticles: 30,
                gravityY: 50
            });

            // === ELIMINAR TODOS OS INIMIGOS ===
            scene.enemies.getChildren().forEach(enemy => {
                const dist = Phaser.Math.Distance.Between(cx, cy, enemy.x, enemy.y);
                if (dist <= 250) {
                    // Destruicao espetacular
                    const destroyBurst = scene.add.particles('debris').createEmitter({
                        x: enemy.x, y: enemy.y,
                        speed: { min: 20, max: 60 },
                        angle: { min: 0, max: 360 },
                        scale: { start: 0.4, end: 0 },
                        tint: [0xFF0000, 0x00FF00, 0x808080],
                        lifespan: 500,
                        quantity: 8,
                        maxParticles: 8
                    });
                    enemy.destroy();
                }
            });

            // === SFX ===
            scene.sound.play('sirene-alerta', { volume: 0.5, delay: 0 });
            scene.sound.play('trovao', { volume: 0.9, delay: 0.05 });
            scene.sound.play('impacto-nuclear', { volume: 1.0, delay: 0.1 });

            // ============================================
            // FASE 4: DEVASTACAO (Frames 6-7) ~1500ms
            // ============================================

            scene.time.delayedCall(400, () => {
                // Cratera em forma de continente
                const cratera = scene.add.ellipse(cx, cy, 140, 100, 0x1A1A1A, 0.7);
                cratera.setStrokeStyle(3, 0x8B4513);
                cratera.setDepth(50);

                // Letras URSAL piscando no centro da cratera
                const ursalNeon = scene.add.text(cx, cy, 'URSAL', {
                    fontSize: '16px', color: '#CC0000', fontStyle: 'bold',
                    stroke: '#000000', strokeThickness: 2
                }).setOrigin(0.5).setDepth(51);

                // Piscar neon
                scene.tweens.add({
                    targets: ursalNeon,
                    alpha: { from: 1, to: 0.2 },
                    duration: 250,
                    yoyo: true,
                    repeat: 12
                });

                // Glow vermelho na cratera
                const crateraGlow = scene.add.ellipse(cx, cy, 130, 90, 0xCC0000, 0.2);
                crateraGlow.setBlendMode(Phaser.BlendModes.ADD);
                crateraGlow.setDepth(50);
                scene.tweens.add({
                    targets: crateraGlow,
                    alpha: { from: 0.3, to: 0.1 },
                    duration: 500,
                    yoyo: true,
                    repeat: 4
                });

                // ============================================
                // FASE 5: AFTERMATH + VICTORIA (Frame 8) ~2000ms
                // ============================================

                scene.time.delayedCall(2000, () => {
                    // Camera volta ao normal
                    scene.cameras.main.zoomTo(1.0, 1000);

                    // Ceu volta ao normal
                    scene.tweens.add({
                        targets: darkSky,
                        alpha: 0,
                        duration: 1000,
                        onComplete: () => darkSky.destroy()
                    });

                    // URSAL neon fade out
                    scene.tweens.add({
                        targets: ursalNeon,
                        alpha: 0,
                        duration: 1500,
                        onComplete: () => ursalNeon.destroy()
                    });

                    // Cratera fade out
                    scene.tweens.add({
                        targets: [cratera, crateraGlow],
                        alpha: 0,
                        duration: 3000,
                        delay: 2000,
                        onComplete: () => {
                            cratera.destroy();
                            crateraGlow.destroy();
                        }
                    });

                    // Particulas de luz dourada subindo (purificacao)
                    const purificacao = scene.add.particles('light-particle').createEmitter({
                        x: { min: cx - 40, max: cx + 40 },
                        y: { min: cy - 20, max: cy + 20 },
                        speed: { min: 10, max: 30 },
                        angle: { min: 250, max: 290 },
                        scale: { start: 0.4, end: 0 },
                        tint: [0xFFD700, 0xFFFFFF],
                        lifespan: 1500,
                        frequency: 60,
                        quantity: 2,
                        blendMode: Phaser.BlendModes.ADD
                    });
                    scene.time.delayedCall(3000, () => purificacao.stop());

                    // Daciolo: quote de victoria
                    scene.time.delayedCall(500, () => {
                        scene.triggerDacioloQuote('eu-avisei-ursal');
                        // "EU AVISEI! A URSAL EXISTE!"
                    });

                    // Cleanup do container
                    scene.time.delayedCall(5000, () => {
                        ursalContainer.destroy();
                        mapa.destroy();
                        ursalText.destroy();
                    });
                });
            });
        });
    });
}
```

---

## Paleta de Cores do Ultimate

| Elemento | Cor | Hex |
|---|---|---|
| Mapa base | Vermelho escuro | `#CC0000` |
| Mapa contorno | Preto grosso | `#1A1A1A` |
| Texto URSAL | Branco | `#FFFFFF` |
| Texto URSAL stroke | Vermelho | `#CC0000` |
| Estrelas ★ | Vermelho claro | `#FF0000` |
| Fronteiras | Branco pontilhado | `#FFFFFF` |
| Sombra chao | Preto | `#000000` @ 15-50% |
| Flash impacto | Branco puro | `#FFFFFF` |
| Onda choque 1 | Branco-amarelo | `#FFFFF0` |
| Onda choque 2 | Dourado | `#FFD700` |
| Onda choque 3 | Vermelho | `#CC0000` |
| Fragmentos mapa | Multi (vermelho, verde, dourado, azul) | Variados |
| Cratera interior | Quase preto | `#1A1A1A` |
| Cratera borda | Marrom | `#8B4513` |
| URSAL neon | Vermelho | `#CC0000` com glow |
| Glow cratera | Vermelho translucido | `#CC0000` @ 20% |
| Relampagos | Branco | `#FFFFFF` |
| Purificacao final | Dourado | `#FFD700` |
| Ceu escuro | Preto | `#000000` @ 25-40% |

---

## Variante: Super Daciolo

Quando o Super Daciolo (Skin 6) usa a URSAL Cataclismica:

- O mapa e **DOURADO** ao inves de vermelho
- "URSAL" escrito em branco com stroke DOURADO (nao vermelho)
- Estrelas sao DOURADAS (★)
- A onda de choque e toda DOURADA (nao vermelha)
- O neon na cratera e DOURADO
- A explosao e 50% MAIOR
- Os fragmentos do mapa sao DOURADOS
- O efeito de purificacao final e BRANCO PURO

A URSAL dourada e a versao SANTIFICADA. O Super Daciolo nao apenas invocou
a conspiração -- ele a REDIMIU. A URSAL divina.

---

## Efeitos de Camera (Timeline Completa)

```
T=0ms     : Camera normal
T=0ms     : "A URSAL! A URSAL EXISTE!" (audio)
T=200ms   : Sombra comeca
T=500ms   : Mapa aparece no topo, camera zoom out para 0.6x
T=500ms   : Tremor comeca (leve)
T=800ms   : Relampagos ao redor do mapa
T=1100ms  : IMPACTO
T=1100ms  : Flash branco TOTAL (300ms)
T=1100ms  : Screen shake MAXIMO (600ms)
T=1100ms  : Audio: sirene + trovao + impacto nuclear
T=1500ms  : Poeira e fragmentos voando
T=1900ms  : Cratera visivel, URSAL neon piscando
T=3500ms  : Camera zoom volta para 1.0x
T=3500ms  : Ceu normaliza
T=4000ms  : "EU AVISEI!" (audio Daciolo)
T=5500ms  : URSAL neon apaga
T=8000ms  : Cratera desaparece
T=8000ms  : Sequencia completa
```

---

## Notas Finais

1. Este e o ULTIMATE. A bomba atomica comica. Deve ser ESPETACULAR e RIDICULO ao mesmo tempo
2. O mapa da URSAL deve ser LEGIVEL quando desce -- o jogador precisa VER que e um mapa
3. O texto "URSAL" e a ESTRELA do show -- deve ser grande, bold, impossivel de ignorar
4. A cratera em forma de continente e o PUNCHLINE VISUAL -- a conspiração LITERALMENTE marcou a terra
5. O neon piscando e uma referencia a letreiros de bar/motel decadente -- estetica proposital
6. Performance: este efeito e PESADO. Limitar particulas. Considerar pre-render do mapa
7. Cooldown de 60s+ e NECESSARIO -- este efeito nao pode ser spammado
8. O som "A URSAL EXISTE!" deve ser ALTO e CLARO -- e o battlecry do ultimate
9. Na versao Super Daciolo: dourar TUDO. A URSAL de ouro. Absurdo? PERFEITO
