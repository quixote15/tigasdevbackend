# Bigode da Justica -- Sprite Specification

## Overview
Arma exclusiva do Eneas Carneiro (O Fantasma Patriota). O bigode ICONICO se DESTACA do rosto do Eneas, gira como um boomerang gigante, corta inimigos no caminho, e RETORNA ao rosto. E a arma mais reverenciada do jogo -- tratada com a mesma dignidade do personagem.

- **Weapon Type**: Ranged / Boomerang (ida e volta)
- **Sprite Dimensions**: 32x32px (projetil em voo)
- **Sprite Sheet Layout**: Horizontal strip, 1 row
- **Total Frames**: 22 (4 destaque + 8 voo + 3 impacto + 4 retorno + 2 re-acoplamento + 1 static)
- **Format**: PNG com alpha transparency
- **Anchor Point**: Center (16, 16)
- **Dano**: Alto por hit (pode atingir multiplos inimigos na trajetoria)
- **Alcance**: 192px (ida) + 192px (volta) -- trajetoria em arco
- **Cooldown**: 8s

> **REGRA SAGRADA**: O bigode da arma e IDENTICO em forma e cor ao bigode do rosto do Eneas.
> Quando o bigode sai, o rosto do Eneas fica sem bigode (coberto pela mao).
> Quando retorna, se reaclopla com um SNAP magnetico satisfatorio.

---

## Color Palette

| Elemento | Hex + Alpha | Descricao |
|---|---|---|
| Bigode base | `#3A2A1A` alpha 90% | Pelos do bigode -- castanho escuro (MAIS opaco que o fantasma!) |
| Bigode escuro | `#2A1A0A` alpha 90% | Sombras internas do bigode |
| Bigode claro | `#5A4A3A` alpha 85% | Highlights nos pelos |
| Bigode borda | `#1A1A1A` alpha 85% | Outline dos pelos individuais |
| Aura dourada interna | `#D4A017` alpha 30% | Glow imediato ao redor do bigode |
| Aura dourada externa | `#FFD700` alpha 15% | Halo externo difuso |
| Trail de voo | `#D4A017` alpha 20-40% | Rastro dourado durante o voo |
| Brilho rotacao | `#FFD700` alpha 50% | Flash nas pontas durante giro |
| Ondas de corte | `#F0F0E8` alpha 60% | Linhas de "corte" no impacto |
| Particula pelo | `#3A2A1A` alpha 40% | Pelos individuais que se soltam |
| Flash destaque | `#FFFFFF` alpha 70% | Flash no momento de destacar do rosto |
| Flash re-acoplamento | `#FFD700` alpha 80% | Flash dourado no retorno ao rosto |
| Impact starburst | `#FFD700` alpha 70% | Explosao de impacto |
| Speed lines | `#F0F0E8` alpha 40% | Linhas de velocidade |
| Outline projetil | `#1A1A1A` alpha 80% | Contorno grosso (2px) estilo Crumb |
| Debris de inimigo | `#8B0000` alpha 60% | Respingos ao cortar |

---

## Forma do Bigode (32x32px)

```
O bigode em repouso (no rosto) tem ~18x8px.
Como projetil em voo, ele GIRA e ocupa mais espaco:

Forma base (vista frontal, 0 graus):
- Largura: ~26px (pontas esticadas para os lados)
- Altura: ~10px (centro mais grosso, afina nas pontas)
- Centro: tufo denso de 8x6px (onde ficava o nariz)
- Ponta esquerda: 9px saindo para a esquerda, curvada para cima
- Ponta direita: 9px saindo para a direita, curvada para cima
- Cada "ponta" termina num ponto afiado (1px) -- LAMINA de pelos
- As pontas brilham com aura dourada (1px flash)

A forma sugere um CROISSANT ACHATADO, ou um GULL EM VOO.
Simetrico no eixo vertical. As pontas sao as "laminas".
```

---

## Frame-by-Frame Descriptions

### Frame 0: Static / Inventory Icon
- **Posicao no sheet**: 0,0 a 31,31
- **Descricao**: Bigode visto de frente, flutuando no centro do frame. Posicao "em repouso": pontas curvadas para cima, centro denso. Ocupa ~26x10px do frame. Outline grosso de 2px preto (estilo Crumb). Aura dourada sutil ao redor (2px glow). Sombra mínima (1px offset para baixo, alpha 30%). Textura de pelos: linhas finas de 1px na direcao do crescimento capilar. Cada pelo e sugerido, nao desenhado individualmente (seriam subdimensionais a 32px).
- **Style Notes**: O bigode deve parecer VIVO mesmo parado. As pontas tem um micro-tremor sugerido pela forma irregular. GROTESCAMENTE grande para uma arma -- e um bigode que CORTA GENTE.

### Destaque do Rosto (4 frames, 32x32px)

### Frame 1: `bigode_detach_01.png`
- **Posicao**: 32,0 a 63,31
- **Descricao**: O bigode comeca a TREMER no rosto. Vibração de 1px horizontal (posicao normal com blur de 1px nos dois lados). As pontas começam a brilhar (1px dourado nas extremidades). Energia se acumula: micro-particulas douradas (1x1px) surgem nas pontas. O bigode ainda esta "acoplado" ao rosto, mas QUER sair.

### Frame 2: `bigode_detach_02.png`
- **Posicao**: 64,0 a 95,31
- **Descricao**: SEPARACAO. O bigode se desloca 2px para frente (saindo do "rosto" implicito). Um gap de 2px entre onde o rosto estaria e o bigode. Flash branco (3x3px, alpha 70%) no ponto de separacao. As pontas estao AFIADAS -- os curls se endireitam levemente. Aura dourada intensifica (4px raio).

### Frame 3: `bigode_detach_03.png`
- **Posicao**: 96,0 a 127,31
- **Descricao**: O bigode agora flutua LIVREMENTE. 6px a frente do ponto de origem. Comeca a GIRAR: leve rotacao de 10 graus. Pontas totalmente endireitadas e afiadas. Speed lines comecam a se formar (2 linhas de 1px branco atras). Flash de separacao se dissipa. O bigode e agora um PROJETIL.

### Frame 4: `bigode_detach_04.png`
- **Posicao**: 128,0 a 159,31
- **Descricao**: LANCAMENTO. O bigode esta a 12px do ponto de origem, rotacao 30 graus. Speed lines fortes (3 linhas, 2px de comprimento). A aura dourada forma um TRAIL atras (arco de 8px, alpha 25%). As pontas brilham intensamente (flash dourado 1px). O bigode esta em velocidade maxima. Transicao para ciclo de voo.

### Ciclo de Voo / Rotacao (8 frames, 32x32px, LOOP)

### Frame 5: `bigode_flight_01.png`
- **Posicao**: 160,0 a 191,31
- **Descricao**: Bigode em rotacao 0 graus (horizontal, pontas para os lados). Posicao de "maximo alcance" -- totalmente esticado. Aura dourada uniforme (2px). Speed lines: 2 linhas atras (na direcao de voo). Brilho nas pontas: ponta direita (no sentido de rotacao) tem flash. Nenhuma particula se solta.

### Frame 6: `bigode_flight_02.png`
- **Posicao**: 192,0 a 223,31
- **Descricao**: Rotacao 45 graus horario. O bigode forma um "X" diagonal. A ponta superior agora e a "lider". Speed lines se curvam levemente (sugerindo a trajetoria de arco/boomerang). Blur sutil nas pontas (1px). 1 particula de pelo se solta (2x1px, castanho, alpha 40%).

### Frame 7: `bigode_flight_03.png`
- **Posicao**: 224,0 a 255,31
- **Descricao**: Rotacao 90 graus -- bigode VERTICAL. Pontas para cima e para baixo. Nesta posicao, o bigode parece uma LAMINA vertical. Aura dourada mais concentrada (centro brilha mais). Speed lines retas. Silhueta maxima de "arma cortante".

### Frame 8: `bigode_flight_04.png`
- **Posicao**: 256,0 a 287,31
- **Descricao**: Rotacao 135 graus. Diagonal oposta ao Frame 6. Blur de rotacao mais visivel (2px nas pontas). Trail dourado mais longo (12px arco atras). 1 particula de pelo se solta no lado oposto ao Frame 6.

### Frame 9: `bigode_flight_05.png`
- **Posicao**: 288,0 a 319,31
- **Descricao**: Rotacao 180 graus -- bigode horizontal INVERTIDO (pontas curvadas para BAIXO). Espelho do Frame 5 mas invertido. Aura pulsa: alpha 25% (frame brilhante). Flash nas pontas AMBAS simultaneamente.

### Frame 10: `bigode_flight_06.png`
- **Posicao**: 320,0 a 351,31
- **Descricao**: Rotacao 225 graus. Diagonal descendente. Blur de velocidade. Trail dourado se estende. Particula de pelo debris.

### Frame 11: `bigode_flight_07.png`
- **Posicao**: 352,0 a 383,31
- **Descricao**: Rotacao 270 graus -- vertical novamente, mas invertido do Frame 7. Pontas agora para baixo e para cima (invertido). Aura pulsante. Silhueta cortante maxima.

### Frame 12: `bigode_flight_08.png`
- **Posicao**: 384,0 a 415,31
- **Descricao**: Rotacao 315 graus. Diagonal final antes de completar o giro. Loop completo de 360 graus em 8 frames. Trail dourado no maximo comprimento. Transicao suave para Frame 5.

### Impacto (3 frames, 32x32px)

### Frame 13: `bigode_impact_01.png`
- **Posicao**: 416,0 a 447,31
- **Descricao**: O bigode atinge o inimigo. SQUASH: comprime 4px na direcao do impacto (de 26x10 para 18x14 -- mais achatado e largo). Starburst de impacto: 6 linhas de 1px irradiando do centro, douradas (#FFD700 alpha 70%). Flash branco 4px raio. "SHLICK!" comeca a se formar (onomatopeia de corte, NAO o THWACK do chinelo). Debris de inimigo: 3-4 particulas vermelhas (2x2px, #8B0000 alpha 60%) voam do ponto de impacto.

### Frame 14: `bigode_impact_02.png`
- **Posicao**: 448,0 a 479,31
- **Descricao**: "SHLICK!" no maximo -- texto em dourado (#FFD700) com outline preto, letras chunky hand-lettered. O bigode CORTA ATRAVES (nao para -- e boomerang, continua). Linhas de corte: 2 linhas finas diagonais (#F0F0E8 alpha 60%) no ponto do corte, como se tivesse fatiado o ar. Debris se afasta. Flash se expande e esmaece. O bigode retoma forma normal (sem squash).

### Frame 15: `bigode_impact_03.png`
- **Posicao**: 480,0 a 511,31
- **Descricao**: O bigode ja passou pelo inimigo. "SHLICK!" esmaece (alpha 40%). Linhas de corte persistem por 1 frame e desaparecem. Debris nos limites do frame. O bigode retoma rotacao normal. O inimigo fica com marca visual de "corte" (efeito aplicado no sprite do inimigo, nao no projetil). Trail dourado se reconecta.

### Retorno / Boomerang (4 frames, 32x32px)

### Frame 16: `bigode_return_01.png`
- **Posicao**: 512,0 a 543,31
- **Descricao**: O bigode atinge o alcance maximo e INVERTE direcao. Pausa de 1 frame (velocidade zero). Aura PULSA forte (alpha 35%). O bigode vibra (shake 1px). As pontas "procuram" a direcao do Eneas (curvam-se levemente para a direcao de retorno).

### Frame 17: `bigode_return_02.png`
- **Posicao**: 544,0 a 575,31
- **Descricao**: Bigode acelerando de volta. Rotacao reinicia na direcao oposta. Speed lines agora na frente (direcao de retorno). Trail dourado na direcao de retorno. O bigode parece "ansioso" para voltar ao rosto -- velocidade 1.3x da ida.

### Frame 18: `bigode_return_03.png`
- **Posicao**: 576,0 a 607,31
- **Descricao**: Velocidade maxima de retorno. Rotacao rapida (blur de 2px). Trail dourado longo. As pontas se curvam de volta para a posicao de "repouso" (preparando para re-acoplamento). Speed lines multiplas.

### Frame 19: `bigode_return_04.png`
- **Posicao**: 608,0 a 639,31
- **Descricao**: Proximidade do rosto. Rotacao DESACELERA (bigode se alinha horizontalmente). As pontas curvam para cima (posicao de encaixe). Aura intensifica -- flash dourado de "quase la". Speed lines curtas (desacelerando).

### Re-acoplamento (2 frames, 32x32px)

### Frame 20: `bigode_reattach_01.png`
- **Posicao**: 640,0 a 671,31
- **Descricao**: CONTATO. O bigode toca a area do rosto. Flash DOURADO massivo (6px raio, #FFD700 alpha 80%). Onda de choque circular minima (1px dourado, raio 8px). O bigode se ACHATA contra o rosto (squash: de 26x10 para 20x12). Snap magnetico visual: linhas de forca curvas (2 arcos de 1px) puxando o bigode para a posicao.

### Frame 21: `bigode_reattach_02.png`
- **Posicao**: 672,0 a 703,31
- **Descricao**: Acomodacao. O bigode volta ao tamanho normal. Flash se dissipa. As pontas TREMEM (vibram 1px para cima e para baixo) por 1 frame -- se acomodando. Uma onda de satisfacao: 1px anel dourado se expande e desaparece. O bigode esta de volta. Tudo esta certo no mundo.

---

## Sprite Sheet Layout

Horizontal strip: 32px height, frames left-to-right.

| Sheet | Frames | Total Width | Descricao |
|---|---|---|---|
| `bigode_static` | 1 | 32px | Icone inventario |
| `bigode_detach` | 4 | 128px | Destacando do rosto |
| `bigode_flight` | 8 | 256px | Rotacao em voo (LOOP) |
| `bigode_impact` | 3 | 96px | Impacto no inimigo |
| `bigode_return` | 4 | 128px | Retorno boomerang |
| `bigode_reattach` | 2 | 64px | Re-acoplamento ao rosto |
| **TOTAL** | **22** | **704px** | |

**Sheet completo**: `bigode_justica_spritesheet.png` -- 704x32px

---

## Particulas de Pelo (16x16px, sprites auxiliares)

### `pelo_particle_01.png` (16x16)
Fio de pelo individual, curvado. 1x4px castanho (#3A2A1A alpha 50%). Gira lentamente enquanto cai. Aparece quando o bigode atinge velocidade maxima de rotacao.

### `pelo_particle_02.png` (16x16)
Tufo de 2-3 pelos juntos. 3x3px castanho. Mais opaco (alpha 60%). Se solta no impacto. Flutua e desaparece em 0.5s.

### `pelo_particle_03.png` (16x16)
Pelo com brilho dourado. 1x3px castanho com 1px dourado na ponta. Se solta durante o destaque do rosto (Frame 2-3). Efeito magico -- o pelo tem aura propria.

---

## Trajetoria do Boomerang

```
O bigode NAO voa em linha reta. Trajetoria em ARCO:

   Eneas (origem)
     |
     |  Fase 1: Lancamento reto (32px)
     |
     +---> Inicio do arco
              \
               \  Fase 2: Arco para cima (96px de raio)
                \
                 +  Ponto mais alto do arco
                /
               /   Fase 3: Arco descendente
              /
     +---> Fim do arco / Ponto de inversao (192px de distancia)
     |
     |  Fase 4: Retorno reto (os ultimos 32px)
     |
   Eneas (destino)

O arco completo tem forma de U invertido.
Inimigos na TRAJETORIA DO ARCO levam dano (nao so no destino).
O bigode pode atingir 4-6 inimigos em uma passagem completa.
```

---

## Phaser 3 Atlas Key

```javascript
// Projetil
{ key: 'weapon_bigode_justica', frameWidth: 32, frameHeight: 32 }

// Particulas de pelo
{ key: 'bigode_pelo_particle', frameWidth: 16, frameHeight: 16 }
```

---

## Interacao com o Personagem

Quando o bigode esta FORA do rosto:

```
1. O sprite do Eneas (64x64) muda para uma variante SEM BIGODE:
   - A area do bigode (18x8px no rosto) fica VAZIA
   - Eneas COBRE a area com a mao (mao sobem 8px para tapar o labio superior)
   - OU vira levemente de lado (mostra perfil 3/4 para esconder a ausencia)
   - NUNCA mostrar o rosto completamente sem bigode -- e um misterio sagrado

2. O rosto sem bigode tem MENOS presenca:
   - Alpha do rosto na regiao do bigode ausente: reduz para 30%
   - O Eneas parece mais VULNERAVEL sem o bigode
   - A aura diminui levemente (alpha 15% -> 10%)

3. Quando o bigode RETORNA:
   - Flash de alegria/alivio visual
   - Alpha restaurado
   - Aura volta ao normal
   - O bigode treme de felicidade por 2 frames
```

---

## Efeito Sonoro Sincronizado

| Frame | Evento de Audio |
|---|---|
| Frame 2 (detach) | "SHWIP" -- som de destacar, seco e rapido |
| Frame 5-12 (flight) | "WHIRR" contínuo -- zumbido de rotacao |
| Frame 13 (impact) | "SHLICK!" -- som de corte afiado |
| Frame 16 (return start) | "WHOOSH" reverso -- som de retorno |
| Frame 20 (reattach) | "SNAP!" magnetico satisfatorio |

---

## Notas para o Artista

1. O bigode DEVE ser reconhecivel como o MESMO bigode do rosto do Eneas -- forma identica.
2. As pontas do bigode sao as "LAMINAS" -- devem parecer afiadas quando em voo.
3. A rotacao deve ser FLUIDA apesar do estilo jerky -- o bigode corta com GRACA.
4. O trail dourado e ESSENCIAL -- sem ele, o bigode parece "jogado" em vez de "magico".
5. No impacto, "SHLICK!" (NAO "THWACK") -- a onomatopeia de corte diferencia esta arma.
6. O bigode e SAGRADO. Mesmo como arma, ele e tratado com respeito. Os inimigos sao cortados com DIGNIDADE.
7. Thick irregular outlines (2px, estilo Crumb) em todos os frames.
8. Cross-hatching sutil nos pelos do bigode para dar textura.
9. A forma do bigode em rotacao deve sugerir tanto um boomerang quanto um par de asas.
10. No re-acoplamento, o SNAP magnetico deve ser o frame mais SATISFATORIO de toda a animacao.
