# Frasco de Rivotril Turbo - Sprite Specification

## Overview
- **Weapon Type:** Melee (clava/mace) - Arma do Ciro
- **Sprite Dimensions:** 32x32px
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 14 (1 static + 3 swing + 3 impact + 3 state variations + 2 idle + 2 panic)
- **Sprite Sheet Size:** 448x32px
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (16, 28) -- grip point no gargalo do frasco

## Conceito
Frasco GIGANTE de Rivotril que Ciro usa como clava. Ao acertar, inimigo fica "sedado" (velocidade -50% por 3s). Se Ciro ficar 10s sem usar, ELE fica sem Rivotril e entra em panico. O jogador precisa CONTINUAR BATENDO pra manter Ciro funcional. A arma E o remedio.

## Color Palette

| Element                | Hex Code  | Usage                                  |
|------------------------|-----------|----------------------------------------|
| Glass Body Light       | `#C8D8E8` | Vidro do frasco (area clara)           |
| Glass Body Mid         | `#8BA8C8` | Vidro do frasco (tom medio)            |
| Glass Body Dark        | `#5A7A9A` | Vidro sombra/borda                     |
| Glass Highlight        | `#E8F0FF` | Reflexo brilhante no vidro             |
| Liquid Blue Full       | `#4A8BB8` | Liquido azul quando cheio              |
| Liquid Blue Mid        | `#6AAAD8` | Liquido azul quando meio               |
| Liquid Blue Low        | `#8ACAF0` | Liquido azul quando quase vazio        |
| Liquid Empty           | `#3A5A7A` | Fundo do frasco vazio (vidro opaco)    |
| Label White            | `#F0EDE8` | Fundo do rotulo farmaceutico           |
| Label Text             | `#1A1A1A` | Texto "RIVOTRIL" no rotulo             |
| Label Red              | `#CC2200` | Detalhes vermelhos no rotulo (tarja)   |
| Cap Gold               | `#D4A830` | Tampa/gargalo metalico dourado         |
| Cap Shadow             | `#A08020` | Sombra da tampa                        |
| Crack Lines            | `#4A4A4A` | Rachaduras quando vazio                |
| Impact Blue Particle   | `#4AE0FF` | Particulas azuis de impacto ("SEDADO") |
| Impact Blue Glow       | `#2AC0FF` | Glow azulado de impacto                |
| Panic Red              | `#FF2020` | Brilho de panico quando vazio          |
| Outline Black          | `#1A1A1A` | Contorno grosso (2px, Crumb style)     |
| Shadow Dark            | `#0D0D0D` | Drop shadow (50% opacity)              |
| Sedated Text Yellow    | `#F4D03F` | Onomatopeia "SEDADO" texto             |
| Sedated Text Shadow    | `#2A80B0` | Sombra do texto "SEDADO" (azul)        |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon (CHEIO)
- **Position in sheet:** 0,0 to 31,31
- **Description:** Frasco de vidro farmaceutico GIGANTE visto de cima (top-down isometric). Formato de garrafa de champagne, porem com rotulo farmaceutico. GROTESCAMENTE grande -- preenche ~85% do frame 32x32. Rotulo visivel com "RIVOTRIL" em fonte farmaceutica distorcida/grotesca (letras tremulas, como se escritas sob efeito do medicamento). Liquido azulado visivel dentro, nivel CHEIO (80% do frasco). Brilho azulado suave emanando do liquido. Tampa dourada metalica no gargalo (topo). Reflexo de luz no vidro (2-3px de highlight branco). Contornos grossos 2px, assimetricos. Drop shadow 2px. Pequena tarja vermelha no rotulo (aviso farmaceutico distorcido).
- **Style Notes:** O frasco deve parecer uma ARMA, nao um remedio. Proporcoes exageradas, vidro pesado e robusto. O rotulo e uma parodia grotesca de rotulo farmaceutico real.

### Frame 1: Swing - Wind-up
- **Position in sheet:** 32,0 to 63,31
- **Description:** Frasco puxado para tras em posicao de wind-up. Rotacionado ~40 graus. Liquido azul BALANCA dentro do frasco (nivel do liquido inclina na direcao oposta ao swing). Leve squash horizontal (2px). Uma motion line trailing (1px, 30% opacity). O rotulo "RIVOTRIL" distorce levemente com o movimento. Brilho azulado segue o liquido.

### Frame 2: Swing - Mid-swing
- **Position in sheet:** 64,0 to 95,31
- **Description:** Frasco em velocidade maxima, quase horizontal. Stretch maximo (3px na direcao do swing). Liquido azul agitado -- bolhas visiveis (2-3 pixels claros dentro do liquido). Duas motion lines trailing (60% e 30% opacity). O vidro parece PESADO e letal. Brilho azulado forma trail.

### Frame 3: Swing - Contact/Impact
- **Position in sheet:** 96,0 to 127,31
- **Description:** Frasco no momento do impacto. SQUASH na ponta (deformacao de impacto grotesca). EXPLOSAO de particulas azuis no ponto de contato (4-5 particulas de 2x2px, azul claro #4AE0FF, radiais). Uma GOTA de liquido azul espirra para fora (nível diminui visivelmente). Starburst branco no contato (6x6px). O vidro treme visualmente (linhas de vibracao). Rotulo "RIVOTRIL" tremendo.

### Frame 4: Impact - "SEDADO" Frame 1
- **Position in sheet:** 128,0 to 159,31
- **Description:** Texto "SEDADO" aparecendo em estilo comic-book. Letras GROSSAS, grotescas, mao-desenhadas. Amarelo (#F4D03F) com sombra azul (#2A80B0) em vez de vermelho (remetendo ao medicamento). Starburst atras com ondas azuladas concentricas (efeito de sedacao). Particulas azuis radiando. Fundo com leve tint azulado (30% opacity).

### Frame 5: Impact - "SEDADO" Frame 2
- **Position in sheet:** 160,0 to 191,31
- **Description:** "SEDADO" no tamanho maximo (110% do frame anterior). Letras mais BORRADAS/TREMULAS (efeito de sedacao visual). Ondas azuladas concentricas expandem. As particulas azuis se transformam em "Zzz" (dormindo). Starburst no maximo. O efeito visual INTEIRO parece "embebedado" -- levemente fora de foco.

### Frame 6: Impact - "SEDADO" Frame 3
- **Position in sheet:** 192,0 to 223,31
- **Description:** "SEDADO" DISSOLVENDO -- letras se desfazem em particulas azuis. Escala reduz para 80%, opacity 50%. As "Zzz" flutuam para cima e desaparecem. Ondas concentricas dissipando. Efeito de sedacao passando. Residuo azulado fading.

### Frame 7: State - CHEIO (nivel alto)
- **Position in sheet:** 224,0 to 255,31
- **Description:** Frasco com liquido no nivel MAXIMO (80% cheio). Brilho azulado INTENSO emanando (glow 3px ao redor do frasco). Vidro transparente, limpo. Rotulo legivel. Tampa intacta brilhando dourado. Este e o estado mais poderoso da arma.

### Frame 8: State - MEIO (nivel medio)
- **Position in sheet:** 256,0 to 287,31
- **Description:** Frasco com liquido no nivel MEDIO (40% cheio). Brilho azulado REDUZIDO (glow 1px). Vidro com leves marcas de uso (1-2 micro-rachaduras, 1px). Rotulo levemente sujo/borrado. Metade superior do frasco vazia, vidro mais opaco nessa area. Tampa com leve oxidacao.

### Frame 9: State - VAZIO (nivel critico)
- **Position in sheet:** 288,0 to 319,31
- **Description:** Frasco QUASE VAZIO (5% liquido -- ultimo gole). SEM brilho azulado -- vidro completamente OPACO e fosco. Rachaduras visiveis no vidro (2-3 linhas de crack, #4A4A4A). Rotulo quase ilegivel (desgastado, "RIVOT..." mal se le). Tampa oxidada/escura. Aspecto DESESPERADOR -- a arma/remedio esta acabando. Tonalidade geral mais escura.

### Frame 10: Idle - Borbulhar 1
- **Position in sheet:** 320,0 to 351,31
- **Description:** Frasco em posicao de descanso com idle animation sutil. Liquido borbulha levemente (1-2 bolhas de 1px subindo dentro do liquido). Frasco inclina 2px para a esquerda (sway). Brilho azulado pulsa levemente mais forte. Rotulo estatico.

### Frame 11: Idle - Borbulhar 2
- **Position in sheet:** 352,0 to 383,31
- **Description:** Espelho do Frame 10: frasco inclina 2px para a direita. Bolhas em posicao diferente (subindo). Brilho azulado no nivel base. Sutil rubber-sway.

### Frame 12: Panic - Frasco Vazio Tremendo 1
- **Position in sheet:** 384,0 to 415,31
- **Description:** Frasco VAZIO tremendo violentamente (estado de panico do Ciro). Vidro opaco, sem liquido, rachado. Borda do frasco com GLOW VERMELHO (#FF2020) pulsante (alerta de panico). Rotulo rasgado. O frasco TREME 2px para a esquerda. Onomatopeia pequena "VAZIO!" em vermelho (8px) no canto.

### Frame 13: Panic - Frasco Vazio Tremendo 2
- **Position in sheet:** 416,0 to 447,31
- **Description:** Continuacao do panic: frasco treme 2px para a direita. Glow vermelho no pico de brilho. Rachaduras se expandem (1px a mais que frame anterior). "VAZIO!" pulsa. Particulas de vidro soltas tremem ao redor (2-3 fragmentos de 1x1px).

## Sprite Sheet Summary

| Frame | Name                | Position    | Purpose                    |
|-------|---------------------|-------------|----------------------------|
| 0     | static_full         | 0-31        | Inventory icon (cheio)     |
| 1     | swing_windup        | 32-63       | Attack start               |
| 2     | swing_mid           | 64-95       | Attack peak velocity       |
| 3     | swing_contact       | 96-127      | Hit moment + splash        |
| 4     | impact_sedado_1     | 128-159     | "SEDADO" appear            |
| 5     | impact_sedado_2     | 160-191     | "SEDADO" peak              |
| 6     | impact_sedado_3     | 192-223     | "SEDADO" fade              |
| 7     | state_full          | 224-255     | Cheio (alto brilho)        |
| 8     | state_mid           | 256-287     | Meio (brilho reduzido)     |
| 9     | state_empty         | 288-319     | Vazio (sem brilho, cracks) |
| 10    | idle_bubble_1       | 320-351     | Idle borbulhar A           |
| 11    | idle_bubble_2       | 352-383     | Idle borbulhar B           |
| 12    | panic_shake_1       | 384-415     | Panico vazio A             |
| 13    | panic_shake_2       | 416-447     | Panico vazio B             |

## Phaser 3 Atlas Key
```javascript
key: 'weapon_rivotril'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- O frasco deve parecer uma CLAVA/MACE farmaceutica -- pesado, letal, GROTESCO
- O "RIVOTRIL" no rotulo e uma PARODIA -- fonte tremula, distorcida, como se sob efeito
- O liquido azul deve BRILHAR -- e a vida/poder do Ciro
- Quando VAZIO, o frasco deve parecer DESESPERADOR (rachaduras, opacidade, morte)
- As particulas de impacto sao AZUIS, nao vermelhas (sedacao, nao sangue)
- "SEDADO" substitui "THWACK" -- o humor e farmaceutico, nao violento
- O efeito de panic (frames 12-13) deve transmitir ABSTINENCIA e DESESPERO
- Contornos GROSSOS (2px+), assimetricos, Robert Crumb style
- A transicao cheio -> meio -> vazio deve ser VISUALMENTE DRAMATICA
- O nivel do liquido e a BARRA DE VIDA da arma
