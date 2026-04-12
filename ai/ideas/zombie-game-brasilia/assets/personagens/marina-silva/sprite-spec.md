# Marina Silva - Especificacao de Sprites

## Dados Gerais

| Propriedade         | Valor                                    |
|--------------------|------------------------------------------|
| Tipo                | Easter Egg / NPC Raro (Candidata Fantasma)|
| Sprite size         | 64x64px                                  |
| Perspectiva         | Top-down levemente isometrica            |
| Sprite atlas        | 2048x2048px (compartilhado)              |
| Formato             | PNG com transparencia VARIAVEL           |
| Orientacoes         | 4 direcoes (S, N, E, W)                 |
| Alpha maximo        | 180/255 (NUNCA totalmente opaca)         |

---

## PALETA DE CORES

### Cores Primarias (Neutras e Desbotadas)
| Elemento             | Hex       | Alpha  | Notas                                   |
|---------------------|-----------|--------|------------------------------------------|
| Pele                | #C4A882  | 180    | Tom quente mas lavado                    |
| Cabelo              | #2C2C2C  | 160    | Preto acinzentado, curto                 |
| Blusa               | #7A8B6E  | 170    | Verde oliva desbotado                    |
| Calca               | #6B6B6B  | 170    | Cinza neutro                             |
| Sapatos             | #5A5A5A  | 160    | Cinza escuro                             |
| Olhos               | #4A3728  | 200    | Castanho (parte mais opaca dela)         |
| Contorno            | #999999  | 140    | Cinza medio (NAO preto como os outros!)  |
| Sombra              | #666666  | 100    | Sombra sutil, quase inexistente          |

### IMPORTANTE: Diferenca de Estilo
Enquanto TODOS os outros personagens usam:
- Linhas de contorno PRETAS (#000000) e GROSSAS (2px)
- Cores SATURADAS e SUJAS
- Sombras PESADAS

Marina usa:
- Linhas de contorno CINZA (#999999) e FINAS (1px)
- Cores NEUTRAS e LAVADAS
- Sombras QUASE INEXISTENTES
- Alpha channel NUNCA em 255

Isso e INTENCIONAL. A "deformidade" dela e ser INVISIVEL.

---

## ANATOMIA DO SPRITE (64x64px)

### Proporcoes (Anti-Caricatura)
- Cabeca: ~16x14px (proporcional, NAO exagerada)
- Tronco: ~14x18px (magro, delicado)
- Pernas: ~10x22px (longas e finas)
- Bracos: ~6x18px (finos, gesticulacao minima)
- Pescoco: ~6x6px (fino, normal)
- Postura: levemente curvada, como quem esta prestes a sumir

### "Deformidade": INVISIBILIDADE PROGRESSIVA
- Extremidades (pes, maos) sao as PRIMEIRAS a ficar transparentes
- O rosto e a ULTIMA coisa a desaparecer
- Bordas do sprite fazem "bleed" com o cenario (pixels das bordas se misturam com as cores do tile abaixo)
- Quando alpha < 60: apenas olhos melancolicos visiveis (como Cheshire Cat reverso)

### Detalhes Faciais
- Expressao: melancolica, resignada, um sorriso triste sutil
- Olhos: grandes para o tamanho da cabeca, ligeiramente umidos
- Boca: quase fechada, comissura levemente pra baixo
- Sem exagero, sem deformacao — o oposto proposital de todos os outros

---

## ACESSORIOS

Marina NAO tem acessorios chamativos. Isso e parte do design.
- Sem armas visiveis
- Sem itens brilhantes
- Talvez uma folha seca presa no cabelo (2x2px, #8B7355) — sutil

---

## ANIMACOES

### 1. IDLE (4 frames, 8 FPS)
Sprite sheet: 256x64px (4 frames x 64px)

| Frame | Alpha | Descricao                                                                              |
|-------|-------|----------------------------------------------------------------------------------------|
| 1     | 170   | Parada, bracos ao lado do corpo. Olhar distante. Cabelo move 1px com brisa invisivel. |
| 2     | 160   | Leve suspiro: ombros sobem/descem 1px. Alpha diminui 10. Extremidades comecam a desvanecer. |
| 3     | 170   | Olha ao redor como quem espera ser notada. Mao levanta levemente. Alpha volta. |
| 4     | 155   | Desiste de chamar atencao. Mao abaixa. Alpha cai. Pes quase invisiveis. |

**Ciclo**: Alpha oscila entre 155-170. NUNCA estavel.

### 2. WALK (6 frames, 10 FPS)
Sprite sheet: 384x64px (6 frames x 64px) — 4 direcoes = 384x256px total

| Frame | Alpha | Descricao                                                                              |
|-------|-------|----------------------------------------------------------------------------------------|
| 1     | 165   | Passo esquerdo, suave. Movimento MUITO mais sutil que outros personagens. |
| 2     | 155   | Transicao. Afterimage leve (ghost de 1 frame atras, alpha 40). |
| 3     | 160   | Passo direito. Pes mal tocam o chao (1px gap entre pe e shadow). |
| 4     | 150   | Transicao. Corpo parece flutuar levemente. |
| 5     | 160   | Passo esquerdo. Roupas nao se movem muito (sem vento, sem drama). |
| 6     | 145   | Alpha mais baixo do ciclo. Quase sumindo. |

**Nota**: Walk de Marina deve parecer que ela FLUTUA, nao anda. Sem impacto no chao.

### 3. ATTACK (3 frames, 12 FPS)
Sprite sheet: 192x64px (3 frames x 64px)
Marina NAO ataca no sentido tradicional.

| Frame | Alpha | Descricao                                                                              |
|-------|-------|----------------------------------------------------------------------------------------|
| 1     | 180   | Marina fica MAIS opaca por um instante (alpha sobe!). Olhar determinado. Mao levanta. |
| 2     | 180   | Toca o inimigo. Inimigo fica CONFUSO (nao leva dano, fica desorientado). Area ao redor fica levemente desfocada. |
| 3     | 120   | Marina recua e fica MUITO transparente. Custo de se revelar. |

### 4. DEATH (4 frames, 6 FPS)
Sprite sheet: 256x64px (4 frames x 64px)
Nao e dramático — e um desaparecimento gradual, melancolico.

| Frame | Alpha | Descricao                                                                              |
|-------|-------|----------------------------------------------------------------------------------------|
| 1     | 140   | Expressao triste. Corpo comeca a desvanecer pelas extremidades. Pes ja invisiveis. |
| 2     | 100   | Maos desaparecem. Tronco transparente. Apenas cabeca e ombros claros. |
| 3     | 60    | Apenas rosto visivel. Olhos melancolicos. Boca move dizendo "Eu volto em 4 anos...". |
| 4     | 20    | Apenas olhos. Depois nada. Particulas leves sobem (4-6 flocos brancos alpha 60). |

**Nota**: ZERO drama. Sem explosao, sem queda. Ela simplesmente... SOME.

### 5. HIT (2 frames, 12 FPS)
Sprite sheet: 128x64px (2 frames x 64px)

| Frame | Alpha | Descricao                                                                              |
|-------|-------|----------------------------------------------------------------------------------------|
| 1     | 100   | Ao ser atingida, fica MAIS transparente (nao mais opaca como os outros). Corpo treme 1px. Sem flash branco (ela absorve o impacto). |
| 2     | 150   | Volta parcialmente. Mas nunca tao opaca quanto antes do hit. Olhar mais triste. |

### 6. SPECIAL: APARICAO / Fade In (6 frames, 6 FPS)
Sprite sheet: 384x64px (6 frames x 64px)
Animacao de quando Marina APARECE no mapa (Easter Egg trigger).

| Frame | Alpha | Descricao                                                                              |
|-------|-------|----------------------------------------------------------------------------------------|
| 1     | 10    | Quase nada: sombra vaga no chao. Player atento nota algo. |
| 2     | 30    | Silhueta vaga. Cores do cenario dominam, Marina e apenas distorcao. |
| 3     | 60    | Forma humana reconhecivel. Contornos cinza aparecem. |
| 4     | 100   | Rosto visivel. Expressao melancolica. Corpo ainda parcialmente transparente. |
| 5     | 140   | Quase "presente". Roupas ganham cor (desaturada). |
| 6     | 170   | Alpha maximo dela. Timer de 3 segundos comeca. Janela de interacao ABERTA. |

### 7. SPECIAL: DESAPARICAO / Fade Out (6 frames, 6 FPS)
Sprite sheet: 384x64px (6 frames x 64px)
Inverso exato do Fade In.

| Frame | Alpha | Descricao                                                                              |
|-------|-------|----------------------------------------------------------------------------------------|
| 1     | 170   | Comeca a desvanecer. Olha pro jogador com tristeza. |
| 2     | 140   | Extremidades somem primeiro. Folha do cabelo cai (particula). |
| 3     | 100   | Meio corpo invisivel. Boca move: "Eu volto em 4 anos..." |
| 4     | 60    | Apenas rosto e ombros. Cenario sangra atraves dela. |
| 5     | 30    | Apenas olhos tristes. |
| 6     | 0     | Nada. Apenas a folha seca no chao onde ela estava. Particulas leves sobem. |

### 8. SPECIAL: PRESENCA ESPECTRAL (4 frames, 4 FPS)
Sprite sheet: 256x64px (4 frames x 64px)
Loop que roda enquanto Marina esta "presente" (entre fade in e fade out).

| Frame | Alpha | Descricao                                                                              |
|-------|-------|----------------------------------------------------------------------------------------|
| 1     | 170   | Alpha maximo. Marina olha ao redor esperando interacao. |
| 2     | 160   | Alpha oscila. Bordas do sprite tremulam como calor. |
| 3     | 150   | Alpha cai mais. Impaciente: quanto mais tempo sem interacao, mais transparente. |
| 4     | 140   | Quase desistindo. Se jogador nao interagir, transiciona pra Fade Out. |

---

## EFEITOS DE TRANSPARENCIA (Implementacao Tecnica)

### Sistema de Alpha por Layer

Marina e renderizada em LAYERS com alpha independente:

| Layer        | Alpha Base | Comportamento                              |
|-------------|-----------|---------------------------------------------|
| Pes          | base - 30 | Primeiro a sumir, ultimo a voltar            |
| Pernas       | base - 20 | Segundo a sumir                              |
| Tronco       | base - 10 | Core relativamente estavel                   |
| Bracos       | base - 25 | Quase tao fragil quanto pes                 |
| Cabeca       | base      | Mais opaco, ultimo a sumir                   |
| Olhos        | base + 20 | SEMPRE mais opacos que o resto (cap 200)    |

### Bleed com Cenario
- Pixels nas bordas externas do sprite: alpha = base * 0.3
- Pixels da segunda borda: alpha = base * 0.6
- Core pixels: alpha = base
- Resultado: Marina se MISTURA com o cenario em vez de ter bordas definidas

---

## PROJETEIS

Marina NAO tem projeteis. Ela nao ataca.

Unico "projetil" e a folha seca que cai quando ela desaparece:
- Tamanho: 4x4px
- Cor: #8B7355 alpha 120
- Animacao: 4 frames de queda espiral (rotacao + descida)
- Pousa no chao e fica por 5 segundos antes de sumir

---

## EFEITOS DE PARTICULAS

| Efeito                  | Tamanho   | Cor         | Alpha | Quantidade | Contexto              |
|------------------------|-----------|-------------|-------|------------|-----------------------|
| Flocos de desaparicao  | 2x2px     | #FFFFFF     | 60    | 4-6        | Fade out, death       |
| Folha seca             | 4x4px     | #8B7355     | 120   | 1          | Marca onde ela estava  |
| Distorcao de calor     | N/A       | N/A         | N/A   | N/A        | Shader effect nas bordas|
| Brilho dos olhos       | 1x1px     | #FFFFFF     | 200   | 2          | Ultimos frames de fade |

---

## LAYOUT NO ATLAS (2048x2048px)

Posicao sugerida para sprites de Marina no atlas compartilhado:

| Animacao                | Posicao no Atlas | Tamanho Total        |
|------------------------|------------------|----------------------|
| Idle (4dir)            | (0, 1024)        | 256x256px            |
| Walk (4dir)            | (256, 1024)      | 384x256px            |
| Attack (4dir)          | (640, 1024)      | 192x256px            |
| Death                  | (832, 1024)      | 256x64px             |
| Hit (4dir)             | (0, 1280)        | 128x256px            |
| Fade In                | (128, 1280)      | 384x64px             |
| Fade Out               | (512, 1280)      | 384x64px             |
| Presenca Espectral     | (896, 1280)      | 256x64px             |
| Folha particula        | (1152, 1280)     | 16x16px              |
| Flocos de desaparicao  | (1168, 1280)     | 16x16px              |

### Nota de Renderizacao
Todos os sprites de Marina devem ser renderizados com `blendMode: Phaser.BlendModes.NORMAL` e alpha controlado via `setAlpha()` no game code. NAO fazer pre-multiply alpha nos PNGs — o alpha e DINAMICO e controlado pelo engine.
