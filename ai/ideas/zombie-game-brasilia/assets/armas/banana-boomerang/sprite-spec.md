# Banana Boomerang - Sprite Specification

## Overview
- **Weapon Type:** Ranged / Boomerang (Special Weapon - Eduardo Bolsonaro)
- **Sprite Dimensions:** 32x32px
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 21 (1 static + 8 rotation + 3 trail + 4 impact + 2 idle + 3 return)
- **Sprite Sheet Size:** 672x32px
- **Format:** PNG with alpha transparency
- **Anchor Point:** Center (16, 16) -- boomerang pivot point

## Color Palette

| Element                  | Hex Code  | Usage                                    |
|--------------------------|-----------|------------------------------------------|
| Banana Yellow (main)     | `#D4B84A` | Main banana body, faded/sickly yellow    |
| Banana Yellow (light)    | `#E8D06B` | Top-side highlights, bruise-free spots   |
| Banana Yellow (dark)     | `#A08830` | Underside shadows, curvature depth       |
| Bruise Brown (spots)     | `#6B4C1A` | Brown rot spots, overripe patches        |
| Bruise Brown (dark)      | `#4A3210` | Deep bruise centers, tip rot             |
| Peel Green (tip)         | `#6B7A3A` | Stem tip, unripe remnant                 |
| Sweat Sheen              | `#F5E8A0` | Greasy surface glint, sweat droplets     |
| Sticker White            | `#F0F0E8` | "MADE IN USA" sticker background         |
| Sticker Blue             | `#1A3A7A` | Sticker text color                       |
| Sticker Red              | `#B22234` | Tiny American flag stripes on sticker    |
| Trail Yellow (sick)      | `#C4A830` | Boomerang trail core, sickly yellow      |
| Trail Yellow (fade)      | `#A08820` | Trail outer edge, fading                 |
| Trail Green (toxic)      | `#8A9A40` | Trail tinge, rotten afterglow            |
| Explosion Cream          | `#F5E6B8` | Banana flesh chunks on impact            |
| Explosion Brown          | `#5A3A10` | Peel fragments on impact                 |
| Outline Black            | `#1A1A1A` | Thick 2px outlines (Crumb style)         |
| Shadow Dark              | `#0D0D0D` | Drop shadow, 50% opacity                |
| Impact White             | `#FFFFF0` | Starburst flash at hit point             |
| Slime Yellow             | `#B8A020` | Splattered banana goo residue            |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 31,31
- **Description:** Banana GROTESCA vista em top-down isometrico. Curvatura classica de banana mas EXAGERADA -- mais grossa e curvada que qualquer banana real, preenche ~85% do frame 32x32. Cor amarela DESBOTADA (#D4B84A), nao amarelo vivo -- parece uma banana esquecida no fundo da mochila por duas semanas. 3-4 manchas marrons (#6B4C1A) irregulares espalhadas pela superficie, concentradas nas pontas. Ponta do talo levemente esverdeada (#6B7A3A). ADESIVO "MADE IN USA" colado no meio da banana -- retangular pequeno (8x4px), fundo branco com texto azul minusculo e micro bandeira americana. O adesivo esta levemente descascando num canto. Superficie com BRILHO DE SUOR -- 2-3 pixels brancos (#F5E8A0) sugerindo oleosidade grotesca. Contornos grossos pretos (2px) irregulares estilo Crumb. Sombra de drop (2px offset, 50% opacity).
- **Style Notes:** A banana deve parecer DOENTIA, nao apetitosa. E grande demais, madura demais, suada demais. O adesivo "MADE IN USA" e o detalhe satirico essencial -- deve ser legivel mesmo em 32x32 (simplificado mas reconhecivel). Textura da casca com micro-riscos e imperfeicoes.

### Frame 1: Rotation - 0 degrees
- **Position in sheet:** 32,0 to 63,31
- **Description:** Banana em posicao horizontal, ponta para a direita. Inicio da animacao de voo do boomerang. Banana ligeiramente esticada (stretch 2px na direcao do voo) para sugerir velocidade. A curvatura natural da banana esta para cima (formato de sorriso). Adesivo "MADE IN USA" visivel. 1 linha de movimento (1px, #A08830, 40% opacity) atrás. Brilho de suor ainda presente, agora parecendo goticulas sendo arrancadas pelo vento.

### Frame 2: Rotation - 45 degrees
- **Position in sheet:** 64,0 to 95,31
- **Description:** Banana rotacionada 45 graus no sentido horario. A forma da banana cria um visual de "bumerangue" natural neste angulo. Stretch de 2px na diagonal. 2 linhas de movimento trilhando. A mancha marrom principal fica mais visivel conforme a banana gira. Micro-goticulas de suor (#F5E8A0, 1x1px) se desprendendo da superficie (2-3 particulas).

### Frame 3: Rotation - 90 degrees
- **Position in sheet:** 96,0 to 127,31
- **Description:** Banana vertical, ponta para cima. Curvatura agora visivel lateralmente -- enfatiza o formato de boomerang. A parte de baixo da banana (mais escura, #A08830) fica visivel, mostrando mais manchas marrons. Adesivo parcialmente oculto pelo angulo. 2 linhas de movimento mais definidas (60% opacity). Goticulas de suor em arco, seguindo a trajetoria da rotacao.

### Frame 4: Rotation - 135 degrees
- **Position in sheet:** 128,0 to 159,31
- **Description:** Banana em diagonal invertida (ponta para cima-esquerda). A curvatura natural agora parece a lâmina de uma foice -- visual ameacador. Sombras mais pesadas no lado inferior. Manchas marrons parecem mais sinistras neste angulo. 3 linhas de movimento. Particulas de suor mais dispersas. Um pixel de brilho intenso (#FFFFF0) na borda de ataque (ponta dianteira que corta o ar).

### Frame 5: Rotation - 180 degrees
- **Position in sheet:** 160,0 to 191,31
- **Description:** Banana horizontal INVERTIDA -- ponta para a esquerda, curvatura para BAIXO (formato de carranca). A face inferior da banana e mais visivel -- mais escura, mais manchas. O adesivo esta de cabeca para baixo. Efeito visual "sinistro" -- a banana de cabeca para baixo parece mais uma arma. 3 linhas de movimento grossas. Goticulas de suor voando para cima.

### Frame 6: Rotation - 225 degrees
- **Position in sheet:** 192,0 to 223,31
- **Description:** Banana em diagonal (ponta para baixo-esquerda). Espelha o Frame 4 mas com a face inferior dominante. Sombras profundas. A rotacao esta no ponto maximo de velocidade -- stretch de 3px. 3 linhas de movimento mais grossas e brilhantes. Micro-particulas de casca (#6B4C1A, 1x1px) comecam a se soltar -- a banana esta se degradando com o impacto do ar.

### Frame 7: Rotation - 270 degrees
- **Position in sheet:** 224,0 to 255,31
- **Description:** Banana vertical invertida (ponta para baixo). Espelha o Frame 3. A ponta inferior mostra mais deterioracao -- a mancha marrom na ponta se expande 1px. Gotas de polpa (#F5E6B8, 1x1px) pingam da ponta inferior. 2 linhas de movimento. A banana esta sofrendo com o voo, comecando a parecer mais mole.

### Frame 8: Rotation - 315 degrees
- **Position in sheet:** 256,0 to 287,31
- **Description:** Banana em diagonal final antes de completar o ciclo (ponta para baixo-direita). Ultimo frame antes de reiniciar a rotacao. Leve compressao (squash 1px) sugerindo que a banana esta perdendo rigidez. 2 linhas de movimento enfraquecendo. Goticulas de suor e micro-particulas de casca em padrao circular ao redor, marcando a trilha completa de 360 graus.

### Frame 9: Trail Effect - Intense
- **Position in sheet:** 288,0 to 319,31
- **Description:** Efeito de RASTRO puro (sem banana visivel neste frame -- apenas o trail). Arco de cor amarela DOENTIA (#C4A830) formando a trilha do boomerang -- uma meia-lua grossa (4px largura) com borda esverdeada (#8A9A40). O rastro parece TOXICO -- nao e um brilho bonito, e uma fumaca oleosa amarelo-esverdeada. Particulas de banana podre (2-3, 2x2px, #6B4C1A) flutuando no rastro. O centro do arco e mais brilhante, as bordas se dissipam com textura granulada.

### Frame 10: Trail Effect - Mid
- **Position in sheet:** 320,0 to 351,31
- **Description:** Rastro a 60% opacity. O arco fica mais fino (3px largura) e mais esverdeado -- a cor saudavel (#C4A830) da lugar ao verde doentio (#8A9A40). Particulas de banana quase sumindo. Textura do rastro fica irregular -- furos e falhas, como fumaca se dissipando. Um cheiro visivel (2 linhas onduladas verdes, 1px, 20% opacity) sobe do rastro.

### Frame 11: Trail Effect - Fade
- **Position in sheet:** 352,0 to 383,31
- **Description:** Rastro quase invisivel (30% opacity). Apenas fragmentos do arco original -- linhas quebradas e pontilhadas. Cor completamente esverdeada (#8A9A40). Uma unica particula de casca (#6B4C1A, 1x1px) persiste no centro. Frame de transicao de volta ao gameplay normal.

### Frame 12: Impact - Banana Explode 1 (Contact)
- **Position in sheet:** 384,0 to 415,31
- **Description:** Momento EXATO do impacto. A banana se deforma grotescamente -- SQUASH extremo (28x16px, achatada como panqueca). A casca racha em 3-4 linhas (1px, #4A3210) irradiando do ponto de contato. Starburst branco (6x6px, #FFFFF0) no centro do impacto. O adesivo "MADE IN USA" se descola e voa para o canto (2x1px branco). 2-3 gotas de polpa (#F5E6B8) esguicham para os lados. A banana inteira treme -- linhas de vibracao (2 linhas onduladas, 1px, ao redor).

### Frame 13: Impact - Banana Explode 2 (Rupture)
- **Position in sheet:** 416,0 to 447,31
- **Description:** Banana EXPLODE! Casca se parte em 4-5 pedacos distintos que voam para fora do centro. Cada pedaco e um fragmento curvado de casca amarela (#D4B84A) com borda marrom (#6B4C1A), tamanhos variados (4x3px, 3x2px, 2x2px). POLPA DE BANANA (#F5E6B8 com #E8D06B) espirra do centro em 6-8 gotas de varios tamanhos. O starburst se expande (10x10px). Uma nuvem de spray amarelento (8x8px central, 40% opacity, #C4A830) representa o "splash" da polpa. Contorno grosso de cada fragmento mantido.

### Frame 14: Impact - Banana Explode 3 (Scatter)
- **Position in sheet:** 448,0 to 479,31
- **Description:** Fragmentos de casca nos cantos do frame, quase saindo. Gotas de polpa no pico de dispersao -- as maiores ja atingiram as bordas do frame. O centro mostra uma "mancha" residual de banana esmagada (12x8px, #Slime Yellow #B8A020) no ponto de impacto. Pedacos menores de casca (1x1px, #6B4C1A) ainda girando no ar. Starburst diminuindo (6x6px, 50% opacity). Um pedaco de adesivo "MADE IN USA" rasgado paira no ar (1x1px branco com azul).

### Frame 15: Impact - Banana Explode 4 (Residue)
- **Position in sheet:** 480,0 to 511,31
- **Description:** Frame final do impacto. Fragmentos quase todos fora do frame -- apenas 1-2 pedacinhos (1x1px) ainda visiveis nos cantos extremos. A mancha de banana esmagada no centro permanece (10x6px, #B8A020, 70% opacity) como residuo. Nenhum starburst. Uma ultima goticula de polpa escorre do centro para baixo (2px, #F5E6B8). O efeito termina com esta marca nojenta de banana no chao. Transicao para gameplay.

### Frame 16: Idle - Banana Sway 1 (Left)
- **Position in sheet:** 512,0 to 543,31
- **Description:** Banana na mao do Eduardo, balancando PREGUICOSAMENTE para a esquerda (inclinacao 10 graus). A banana esta em posicao de repouso mas parece VIVA -- a curvatura pulsa levemente (1px mais larga que o Frame 0). Goticulas de suor (#F5E8A0) acumulam-se na parte inferior (gravidade). O adesivo "MADE IN USA" pende levemente com o balanco. Manchas marrons parecem ligeiramente maiores que no Frame 0 (a banana continua amadurecendo mesmo como arma). Brilho de suor no lado esquerdo (pixel highlight no lado alto da inclinacao). Atmosfera de desleixo total.

### Frame 17: Idle - Banana Sway 2 (Right)
- **Position in sheet:** 544,0 to 575,31
- **Description:** Espelha o Frame 16 mas inclinada para a direita (10 graus oposto). Goticulas de suor deslocam-se correspondentemente. Brilho de suor move para o lado direito. O adesivo "MADE IN USA" pende para o outro lado. Uma MOSCA (2x2px, preta) aparece perto da banana -- mosca de fruta atraida pelo estado de deterioracao. A mosca e o detalhe comico essencial do idle -- a banana e tao podre que atrai inseto mesmo sendo arma. Juntos Frames 16-17 criam um balanco lento e preguicoso.

### Frame 18: Return Flight - Incoming 1
- **Position in sheet:** 576,0 to 607,31
- **Description:** Banana RETORNANDO ao jogador (mecanica de boomerang). Banana vista de frente (vindo em direcao a camera/jogador), escala 80% do tamanho normal (perspectiva de distancia). Rotacao lenta (diferente da ida). Rastro atras mas agora mais fraco (#C4A830, 30% opacity). A banana esta PIOR do que quando saiu -- mais manchas marrons, casca parcialmente descascada num canto (2px de polpa exposta #F5E6B8). 1 mosca perseguindo a banana.

### Frame 19: Return Flight - Incoming 2
- **Position in sheet:** 608,0 to 639,31
- **Description:** Banana a 90% do tamanho, mais proxima. Rotacao avancou 90 graus. Mais detalhes visiveis da deterioracao pos-impacto -- amassados, casca mais solta, manchas maiores. O adesivo "MADE IN USA" esta pendurado por uma ponta, quase caindo. Rastro mais fraco. Mosca mais perto. 1 gota de polpa (#F5E6B8) pinga da banana em voo.

### Frame 20: Return Flight - Catch
- **Position in sheet:** 640,0 to 671,31
- **Description:** Banana no tamanho cheio, momento do "catch" pelo Eduardo. A banana esta visivelmente PIOR -- parece que sobreviveu a uma guerra. Casca parcialmente aberta no lado do impacto, polpa exposta (4px de #F5E6B8 com manchas #Bruise Brown). Adesivo completamente solto, flutuando ao lado (1x1px). O outline preto ao redor fica mais grosso (3px) neste frame para enfatizar o momento de captura. Flash sutil (2px, branco, 30% opacity) ao redor da banana sugere o "smack" da mao pegando. Mosca pousa na banana.

## Sprite Sheet Summary

| Frame | Name                 | Position   | Purpose                        |
|-------|----------------------|------------|--------------------------------|
| 0     | static               | 0-31       | Inventory / UI icon            |
| 1     | rotation_000         | 32-63      | Flight rotation 0 deg          |
| 2     | rotation_045         | 64-95      | Flight rotation 45 deg         |
| 3     | rotation_090         | 96-127     | Flight rotation 90 deg         |
| 4     | rotation_135         | 128-159    | Flight rotation 135 deg        |
| 5     | rotation_180         | 160-191    | Flight rotation 180 deg        |
| 6     | rotation_225         | 192-223    | Flight rotation 225 deg        |
| 7     | rotation_270         | 224-255    | Flight rotation 270 deg        |
| 8     | rotation_315         | 256-287    | Flight rotation 315 deg        |
| 9     | trail_intense        | 288-319    | Boomerang trail full           |
| 10    | trail_mid            | 320-351    | Boomerang trail fading         |
| 11    | trail_fade           | 352-383    | Boomerang trail dissipating    |
| 12    | impact_contact       | 384-415    | Hit moment - squash            |
| 13    | impact_rupture       | 416-447    | Banana explodes                |
| 14    | impact_scatter       | 448-479    | Fragments scatter              |
| 15    | impact_residue       | 480-511    | Gross residue remains          |
| 16    | idle_sway_left       | 512-543    | Idle banana sway A             |
| 17    | idle_sway_right      | 544-575    | Idle banana sway B (with fly)  |
| 18    | return_far           | 576-607    | Boomerang return distant       |
| 19    | return_mid           | 608-639    | Boomerang return approaching   |
| 20    | return_catch         | 640-671    | Boomerang caught by player     |

## Phaser 3 Atlas Key
```
key: 'weapon_banana_boomerang'
frameWidth: 32
frameHeight: 32
```

## Phaser 3 Animation Config
```javascript
// Rotation loop (flight)
this.anims.create({
    key: 'banana_spin',
    frames: this.anims.generateFrameNumbers('weapon_banana_boomerang', { start: 1, end: 8 }),
    frameRate: 12, // Fast spin
    repeat: -1
});

// Trail overlay (spawned behind projectile)
this.anims.create({
    key: 'banana_trail',
    frames: this.anims.generateFrameNumbers('weapon_banana_boomerang', { start: 9, end: 11 }),
    frameRate: 8,
    repeat: 0
});

// Impact explosion
this.anims.create({
    key: 'banana_impact',
    frames: this.anims.generateFrameNumbers('weapon_banana_boomerang', { start: 12, end: 15 }),
    frameRate: 10,
    repeat: 0
});

// Idle sway (in hand)
this.anims.create({
    key: 'banana_idle',
    frames: this.anims.generateFrameNumbers('weapon_banana_boomerang', { start: 16, end: 17 }),
    frameRate: 3, // Slow, lazy sway
    repeat: -1
});

// Return flight
this.anims.create({
    key: 'banana_return',
    frames: this.anims.generateFrameNumbers('weapon_banana_boomerang', { start: 18, end: 20 }),
    frameRate: 8,
    repeat: 0
});
```

## Particle Effects

### Sweat Droplets (during flight)
- 1-2 particulas por frame
- Cor: #F5E8A0 (amarelo oleoso)
- Tamanho: 1-2px
- Lifetime: 400ms
- Direcao: tangencial a rotacao (centrifuga)
- Opacity: 0.7 -> 0.0

### Trail Particles (behind boomerang)
- 2-3 particulas por frame
- Cores: #C4A830 (amarelo doentio), #8A9A40 (verde toxico)
- Tamanho: 2-4px
- Lifetime: 600ms
- Opacity: 0.5 -> 0.0
- Comportamento: flutuam e se dispersam lentamente

### Impact Chunks (on hit)
- 8-12 particulas no momento do impacto
- Cores mix: #D4B84A (casca), #F5E6B8 (polpa), #6B4C1A (manchas), #B8A020 (goo)
- Tamanho: 2-6px (variado)
- Lifetime: 500-900ms
- Direcao: radial 360 graus, com gravidade (arco parabolico)
- Rotacao: cada particula gira individualmente

### Fruit Flies (idle)
- 1-2 moscas orbitando
- Cor: #1A1A1A (preto)
- Tamanho: 2x2px
- Movimento: padrao circular erratico (sine wave + noise)
- Permanente enquanto arma estiver idle

---

## Audio Sincronizado

| Evento | Som | Duracao | Trigger |
|---|---|---|---|
| Arremesso | whoosh suave + "vai banana!" (Eduardo) | 400ms | Lancamento |
| Voo (spin) | whirr mecanico + squelch molhado | loop 200ms | Durante rotacao |
| Trail | sizzle abafado (banana podre cortando ar) | loop 300ms | Durante voo |
| Impacto | SPLAT molhado + CRACK de casca | 500ms | Frame 12 |
| Explosao | squelch gore + tchu-tchu de polpa | 300ms | Frame 13 |
| Return | whoosh reverso (mais fraco) | 400ms | Frames 18-20 |
| Catch | SLAP de mao + buzz de mosca | 200ms | Frame 20 |
| Idle | buzz distante de mosca de fruta | loop 500ms | Durante idle |
| Bordao | "Isso e mais eficiente que um tweet!" | 1500ms | Random 20% no arremesso |

---

## Mecanica do Boomerang (Game Design Notes)

- **Trajetoria:** Arco parabolico curvo (nao linear) -- a banana segue um path de boomerang real
- **Alcance:** 180px ida, retorna automaticamente
- **Dano ida:** 15 HP (banana fresca)
- **Dano volta:** 8 HP (banana ja amassada)
- **Cooldown:** 2000ms (Eduardo precisa limpar a polpa da mao)
- **Special:** Se pegar a banana no frame exato do return_catch (timing window 200ms), proximo arremesso tem dano 2x ("Perfect Catch Bonus")

---

## Art Generation Prompts

### Style Preamble (prepend to ALL prompts)
```
Style: grotesque underground comix, Robert Crumb inspired, thick uneven black outlines,
heavy shadows, saturated-dirty colors, pixel art 32x32, top-down isometric perspective,
Brazilian satirical political cartoon, B-movie horror aesthetic, intentionally rough and
asymmetric. The banana looks DISEASED and WEAPONIZED, not appetizing.
```

### Frame 0: Static / Inventory Icon

**Stable Diffusion / DALL-E:**
```
A single grotesquely oversized banana viewed from above in top-down isometric perspective,
pixel art 32x32 pixels. The banana is a faded sickly yellow (#D4B84A), NOT bright yellow --
it looks overripe and sweaty. 3-4 irregular brown rot spots on the surface. A small
rectangular sticker reading "MADE IN USA" with tiny American flag colors is stuck on the
middle of the banana, slightly peeling at one corner. The surface has a greasy sweat sheen
(white highlight pixels). Thick uneven black outlines (2px minimum), Robert Crumb underground
comix style. Drop shadow beneath. Transparent background. Game weapon sprite asset. The banana
is unnervingly large, filling 85% of the frame.
```

**Midjourney:**
```
/imagine pixel art 32x32, top-down view of grotesquely oversized sickly overripe banana,
faded dirty yellow with brown rot spots, "MADE IN USA" sticker, greasy sweat sheen, Robert
Crumb thick outlines underground comix, satirical Brazilian political cartoon, game weapon
sprite, transparent background, intentionally ugly and rough --ar 1:1 --s 250 --no photorealistic
```

### Frames 1-8: Rotation Cycle

**Stable Diffusion / DALL-E:**
```
Sprite sheet of a grotesque overripe banana rotating 360 degrees in 8 frames, pixel art
32x32 per frame, 256x32 total horizontal strip. Each frame shows the banana at a 45-degree
increment (0, 45, 90, 135, 180, 225, 270, 315 degrees). The banana is faded sickly yellow
with brown spots, motion blur trails behind each frame. Small sweat droplets fly off due to
centrifugal force. The banana looks like a weaponized boomerang in flight. Robert Crumb style
thick black outlines, underground comix aesthetic. Transparent background. Top-down perspective.
Each frame shows increasing deterioration -- more bruises appear as the banana spins.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 256x32, 8 frames of grotesque banana rotating 360 degrees,
boomerang flight animation, each frame 32x32, faded yellow with brown rot spots, motion blur
trails, sweat droplets flying off, Robert Crumb underground comix thick outlines, top-down
game sprite, transparent background, weaponized fruit --ar 8:1 --s 250
```

### Frames 9-11: Trail Effect

**Stable Diffusion / DALL-E:**
```
Three frames (96x32 sprite sheet) showing a sickly yellow-green boomerang trail effect
dissipating, pixel art 32x32 per frame. Frame 1: thick arc of toxic yellow-green energy trail,
oily and unhealthy looking. Frame 2: trail at 60% opacity, more green, breaking apart. Frame 3:
faint dotted remnants of trail, nearly gone. The trail looks like the sickly afterglow of a
rotten banana cutting through air. Underground comix style. No banana visible, just the trail
residue. Transparent background. Game VFX sprite.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 96x32, 3 frames of sickly yellow-green boomerang trail fading,
toxic energy arc dissipating, oily unhealthy glow, underground comix style, game VFX sprite,
transparent background --ar 3:1 --s 250
```

### Frames 12-15: Impact Explosion

**Stable Diffusion / DALL-E:**
```
Four frames (128x32 sprite sheet) showing a banana EXPLODING on impact, pixel art 32x32 per
frame. Frame 1: banana squashed flat, cracking, white starburst at impact. Frame 2: banana
ruptures into 4-5 peel fragments and sprays of cream-colored pulp, full explosion. Frame 3:
fragments scattering to edges, yellow-brown goo residue at center. Frame 4: only a gross
slimy banana stain remains at the impact point. Grotesque underground comix style, Robert
Crumb thick outlines. Each fragment has its own outline. The explosion is WET and DISGUSTING,
not fiery. Transparent background. Game impact animation.
```

**Midjourney:**
```
/imagine pixel art sprite sheet 128x32, 4 frames of grotesque banana exploding on impact,
wet splattery destruction, peel fragments flying, cream pulp spray, slimy residue, Robert
Crumb underground comix thick outlines, disgusting fruit explosion, game impact VFX,
transparent background --ar 4:1 --s 250
```

### Frames 16-17: Idle Animation

**Stable Diffusion / DALL-E:**
```
Two frames (64x32 sprite sheet) of a grotesque overripe banana in idle sway animation, pixel
art 32x32 per frame. Frame 1: banana tilted slightly left, sweat drops on underside, sickly
yellow with brown spots. Frame 2: banana tilted slightly right, a tiny black fruit fly (2x2px)
buzzes near the banana. The banana looks lazy, heavy, and disgustingly overripe. "MADE IN USA"
sticker visible, hanging loosely. Robert Crumb underground comix style, thick black outlines.
Top-down isometric view. Transparent background. Game idle weapon sprite.
```

**Midjourney:**
```
/imagine pixel art 64x32 sprite sheet, 2 frames of overripe grotesque banana idle sway
animation, sickly yellow brown spots, tiny fruit fly orbiting, "MADE IN USA" sticker, lazy
preguicoso wobble, Robert Crumb underground comix thick outlines, top-down game sprite,
transparent background --ar 2:1 --s 250
```

### Frames 18-20: Return Flight

**Stable Diffusion / DALL-E:**
```
Three frames (96x32 sprite sheet) of a battered banana returning like a boomerang, pixel art
32x32 per frame. Frame 1: small banana (80% scale, perspective distance) with faint trail,
visibly damaged from impact. Frame 2: banana at 90% scale, more damage visible -- partial peel,
sticker hanging off. Frame 3: full size banana being caught, thick outline flash, a fruit fly
landing on it. The banana is significantly MORE damaged than when it was thrown -- bruised,
partially peeled, disgusting. Robert Crumb underground comix style. Transparent background.
```

**Midjourney:**
```
/imagine pixel art 96x32 sprite sheet, 3 frames of damaged banana boomerang returning,
increasing scale perspective, battered bruised partially peeled, fruit fly following,
Robert Crumb underground comix thick outlines, top-down game sprite, transparent background
--ar 3:1 --s 250
```

---

## Post-Processing Notes
- Apos geracao, limpar manualmente para grid exato de 32x32 pixels
- Garantir contornos pretos grossos e consistentes (2px minimo)
- Verificar transparencia limpa (sem artefatos de fundo)
- Ajustar cores para os hex codes exatos da paleta
- Adicionar assimetria intencional se o output da IA ficar "perfeito" demais
- Sujar superficies limpas com 1-2 pixels de ruido na cor de sombra
- A banana NUNCA deve parecer apetitosa -- se parecer boa, esta errada
- O adesivo "MADE IN USA" deve ser legivel mesmo simplificado
- Montar frames da esquerda para a direita em sprite sheet horizontal (672x32 final)
- A mosca de fruta no idle e ESSENCIAL -- nao remover

## Notes for Artist
- A banana e a arma SATIRICA do Eduardo -- a piada e que ele arremessa uma banana podre como se fosse um boomerang australiano sofisticado
- O contraste entre a pretensao (boomerang! arma especial!) e a realidade (e so uma banana velha e nojenta) e o humor central
- O adesivo "MADE IN USA" e referencia a conexao do Eduardo com os EUA -- deve estar SEMPRE visivel exceto nos angulos que fisicamente o escondem
- A banana deve se DETERIORAR progressivamente: inventory (ruim) -> flight (pior) -> return (horrivel)
- O suor na banana e NOJENTO, nao estetico -- parece banana que ficou no bolso de alguem num dia quente
- A mosca de fruta e o detalhe comico que finaliza -- mesmo como arma letal, a banana e tao podre que atrai inseto
- NUNCA faca a banana parecer amarelo-vivo -- o amarelo deve ser DOENTIO, desbotado, quase esverdeando
- Robert Crumb style: tracos grossos, irregulares, NADA e reto, NADA e limpo, tudo tem textura e peso
- A explosao de impacto deve ser MOLHADA e NOJENTA, nao dramatica -- banana esmagada e grotesca, nao epica
