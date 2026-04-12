# Calculadora Infernal - Sprite Specification

## Overview
- **Weapon Type:** Ranged (projectile shooter) - Arma do Taxadd
- **Sprite Dimensions:** 32x32px
- **Sprite Sheet Layout:** Horizontal strip, 1 row
- **Total Frames:** 14 (1 static + 3 fire + 3 impact + 2 projectile + 2 idle + 3 display states)
- **Sprite Sheet Size:** 448x32px
- **Format:** PNG with alpha transparency
- **Anchor Point:** Center (16, 16) -- held like a shield/cannon

## Conceito
Calculadora cientifica GIGANTE que dispara cifras ($$$) como projeteis. Cada cifra que acerta o jogador drena pontos/score. O display mostra "impostos acumulados" que crescem conforme mais cifras acertam. Arma do Taxadd (Haddad) que e droppada pelo Zema ao ser derrotado.

## Color Palette

| Element                | Hex Code  | Usage                                  |
|------------------------|-----------|----------------------------------------|
| Body Black             | `#1A1A1A` | Corpo principal da calculadora         |
| Body Dark Gray         | `#2A2A2A` | Corpo highlights sutis                 |
| Body Edge              | `#0A0A0A` | Bordas/profundidade do corpo           |
| Display Green          | `#00FF41` | Display LED verde (numeros)            |
| Display Green Dark     | `#008A22` | Display LED verde (sombra/fundo)       |
| Display Background     | `#0A1A0A` | Fundo escuro do display                |
| Key White              | `#E8E4D8` | Teclas numericas (branco sujo)         |
| Key Shadow             | `#B0A898` | Sombras das teclas                     |
| Key Red Function       | `#CC2200` | Teclas de funcao (C, =, %, TAX)        |
| Key Red Shadow         | `#8A1600` | Sombra das teclas vermelhas            |
| Key Orange             | `#FF8C00` | Teclas de operacao (+, -, x, /)        |
| Cifrao Projectile Gold | `#FFD700` | Cifrao ($) projetil disparado          |
| Cifrao Shadow          | `#B8860B` | Sombra do cifrao projetil              |
| Taxado Stamp Red       | `#CC0000` | Carimbo "TAXADO" no alvo               |
| Taxado Stamp BG        | `#FF4040` | Fundo do carimbo "TAXADO"              |
| Screen Glow            | `#00FF41` | Glow verde do display (ambient)        |
| Outline Black          | `#1A1A1A` | Contorno grosso (2px, Crumb style)     |
| Shadow Dark            | `#0D0D0D` | Drop shadow (50% opacity)              |
| Spark Yellow           | `#FFFF00` | Faiscas ao disparar                    |
| Energy Lines           | `#00FF41` | Linhas de energia saindo do display    |

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Position in sheet:** 0,0 to 31,31
- **Description:** Calculadora cientifica GIGANTE vista de cima (top-down isometric). Formato retangular com cantos arredondados, tamanho de um ESCUDO. Preenche ~90% do frame 32x32. Corpo preto (#1A1A1A) com acabamento fosco. Display LED verde (#00FF41) no topo mostrando "0000.00" (em repouso). Grid de teclas visivel: teclas brancas numericas (0-9), teclas VERMELHAS de funcao (C, =, %, e uma tecla especial "TAX"), teclas LARANJAS de operacao (+, -, x, /). As teclas sao GROTESCAMENTE grandes e bulbosas (estilo underground comix). Display tem leve glow verde ao redor (2px, 20% opacity). Contornos grossos 2px, assimetricos. Drop shadow.
- **Style Notes:** A calculadora deve parecer uma ARMA PESADA, nao um gadget. O display brilha de forma AMEACADORA. As teclas parecem estar vivas (bulbosas, organicas).

### Frame 1: Fire - Charging
- **Position in sheet:** 32,0 to 63,31
- **Description:** Calculadora preparando disparo. Display verde BRILHA INTENSAMENTE (glow dobra para 4px). Numeros no display mudam FRENETICAMENTE (blur de numeros). Teclas se PRESSIONAM SOZINHAS (2-3 teclas visivelmente afundadas, animacao de auto-digitacao). Faiscas amarelas (#FFFF00) ao redor do display (2-3 sparks, 1px cada). Tecla "TAX" brilha em vermelho intenso. A calculadora treme levemente (2px) sugerindo energia acumulando.

### Frame 2: Fire - Discharge
- **Position in sheet:** 64,0 to 95,31
- **Description:** Momento do DISPARO. Do display, um cifrao ENORME ($) sai disparado (representado por 6-8px de cifrao saindo do display com trail). Flash de energia verde no display. 3-4 linhas de energia verdes (#00FF41) radiam do display na direcao do disparo. Teclas recoil: todas levemente saltam (release de pressao). O corpo da calculadora RECUA levemente (efeito de recuo como arma de fogo). Faiscas no maximo. Display mostra "+$$$" por um frame.

### Frame 3: Fire - Cooldown
- **Position in sheet:** 96,0 to 127,31
- **Description:** Pos-disparo. Calculadora voltando a posicao normal. Residuo de glow verde diminuindo. Teclas voltando a posicao. Display mostra o novo total de "impostos acumulados" (numero levemente maior que antes). Fumaca verde sutil (1-2 wisps) saindo do display. Calculadora estabiliza.

### Frame 4: Projectile - Cifrao ($) Frame 1
- **Position in sheet:** 128,0 to 159,31
- **Description:** Projetil cifrao ($) em voo. Sprite 8x8px CENTRALIZADO no frame 32x32. Cifrao dourado (#FFD700) com contorno grosso preto (2px). Brilho/glow dourado ao redor (2px, 40% opacity). Trail verde atras (residuo de display). O cifrao GIRA levemente (rotacao 0 graus neste frame). Numeros pequenos orbiting ao redor do cifrao ("R$", "%", "IPI", "ICMS" em 2-3px, quase sub-pixel).

### Frame 5: Projectile - Cifrao ($) Frame 2
- **Position in sheet:** 160,0 to 191,31
- **Description:** Cifrao ($) rotacionado 45 graus (metade da rotacao). Brilho dourado pulsa (glow 3px). Trail verde mais longo. Numeros orbitantes em posicao diferente. Leve stretch na direcao do movimento (2px).

### Frame 6: Impact - "TAXADO" Frame 1
- **Position in sheet:** 192,0 to 223,31
- **Description:** Carimbo "TAXADO" aparecendo em estilo comic-book no ponto de impacto. Texto vermelho (#CC0000) GROSSO em fundo levemente rosado (#FF4040, 30% opacity). Formato de selo/carimbo retangular com bordas irregulares (como carimbo real batido com forca). Rotacao leve (~5-10 graus, imperfect). Starburst de cifroes ($) menores radiando (3-4 cifroes de 3x3px). Flash de impacto amarelo.

### Frame 7: Impact - "TAXADO" Frame 2
- **Position in sheet:** 224,0 to 255,31
- **Description:** "TAXADO" no tamanho MAXIMO (110%). Cor intensificada. Cifroes radiando atingem distancia maxima. Tinta do carimbo "escorre" levemente (efeito de tinta fresca -- 1-2px de drip vermelho para baixo). Numeros de imposto ("13.5%", "R$ 50") flutuam ao redor brevemente.

### Frame 8: Impact - "TAXADO" Frame 3
- **Position in sheet:** 256,0 to 287,31
- **Description:** "TAXADO" fading: escala 85%, opacity 50%. Tinta secando (drips param). Cifroes menores quase desapareceram. Numeros de imposto dissipando. Residuo de vermelho. Voltando ao gameplay normal.

### Frame 9: Idle - Teclas Autonomas 1
- **Position in sheet:** 288,0 to 319,31
- **Description:** Calculadora em idle com teclas que se pressionam SOZINHAS. Neste frame: 2 teclas aleatorias estao PRESSIONADAS (afundadas 1px). Display mostra um numero estavel (o total acumulado). Leve glow verde do display. Corpo levemente inclinado para a esquerda (2px sway). Uma tecla na posicao "pressionando" e outra na posicao "soltando".

### Frame 10: Idle - Teclas Autonomas 2
- **Position in sheet:** 320,0 to 351,31
- **Description:** Espelho do idle: 2 teclas DIFERENTES pressionadas. Display mostra mesmo numero. Corpo inclinado para a direita (2px sway). As teclas que estavam pressionadas antes agora soltaram, e OUTRAS estao pressionadas. Efeito: a calculadora esta "calculando" sozinha, autonomamente.

### Frame 11: Display State - Low Tax
- **Position in sheet:** 352,0 to 383,31
- **Description:** Estado do display quando impostos acumulados sao BAIXOS (0-1000). Display mostra "R$ 0.00" a "R$ 999". Glow verde FRACO (1px). Corpo da calculadora normal. Poucas teclas ativas. Visual calmo. A calculadora esta "aquecendo".

### Frame 12: Display State - Mid Tax
- **Position in sheet:** 384,0 to 415,31
- **Description:** Estado do display quando impostos MEDIOS (1000-5000). Display mostra "R$ 1,000+" com numeros levemente maiores. Glow verde MEDIO (2px). 2-3 teclas auto-pressionando mais rapido. Leves faiscas ao redor. A calculadora esta TRABALHANDO.

### Frame 13: Display State - High Tax (OVERLOAD)
- **Position in sheet:** 416,0 to 447,31
- **Description:** Estado do display quando impostos ALTOS (5000+). Display mostra "R$ 99,999" com numeros ENORMES quase estourando o display. Glow verde INTENSO (3px). TODAS as teclas pressionando freneticamente. Faiscas constantes. Display PULSA. A calculadora esta em OVERLOAD -- brilho maximo, energia maxima, PERIGO fiscal.

## Sprite Sheet Summary

| Frame | Name                | Position    | Purpose                     |
|-------|---------------------|-------------|-----------------------------|
| 0     | static              | 0-31        | Inventory / UI icon         |
| 1     | fire_charge         | 32-63       | Charging (pre-fire)         |
| 2     | fire_discharge      | 64-95       | Firing moment               |
| 3     | fire_cooldown       | 96-127      | Post-fire recovery          |
| 4     | projectile_1        | 128-159     | Cifrao ($) in flight A      |
| 5     | projectile_2        | 160-191     | Cifrao ($) in flight B      |
| 6     | impact_taxado_1     | 192-223     | "TAXADO" appear             |
| 7     | impact_taxado_2     | 224-255     | "TAXADO" peak               |
| 8     | impact_taxado_3     | 256-287     | "TAXADO" fade               |
| 9     | idle_keys_1         | 288-319     | Idle (auto-pressing A)      |
| 10    | idle_keys_2         | 320-351     | Idle (auto-pressing B)      |
| 11    | display_low         | 352-383     | Low tax accumulated         |
| 12    | display_mid         | 384-415     | Mid tax accumulated         |
| 13    | display_high        | 416-447     | High tax (OVERLOAD)         |

## Phaser 3 Atlas Key
```javascript
key: 'weapon_calculadora'
frameWidth: 32
frameHeight: 32
```

## Notes for Artist
- A calculadora deve parecer um CANHAO FISCAL, nao um dispositivo de escritorio
- O display LED verde e AMEACADOR -- brilha como olhos de monstro
- As teclas se PRESSIONAM SOZINHAS -- a calculadora tem vida propria
- Cifroes ($) sao PROJETEIS LETAIS, nao decoracao
- "TAXADO" substitui "THWACK" -- o humor e FISCAL, nao violento
- Contornos GROSSOS (2px+), assimetricos, Robert Crumb style
- As teclas devem ser BULBOSAS e organicas (parecem vivas)
- O vermelho das teclas de funcao e AGRESSIVO, como botoes de destruicao
- A transicao low -> mid -> high no display deve ser VISUALMENTE ESCALANTE
- Tamanho de ESCUDO -- a calculadora e enorme, quase comica no tamanho
