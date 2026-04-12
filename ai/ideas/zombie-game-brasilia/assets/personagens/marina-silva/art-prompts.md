# Marina Silva - Prompts para Geracao de Arte

## PROMPT BASE DO PERSONAGEM

### Stable Diffusion / SDXL

```
subtle minimalist caricature of a thin Brazilian woman politician, short dark hair, melancholic expression, sad gentle eyes, olive green faded blouse, gray neutral pants, SEMI-TRANSPARENT ghostly figure, nearly invisible, fading into the background, soft gray outlines NOT black, desaturated washed-out colors, understated design, the opposite of grotesque, ethereal ghostly presence, pixel art sprite 64x64, top-down isometric perspective, transparent background, Robert Crumb inspired but MINIMAL version, existential sadness
```

### DALL-E 3

```
A 64x64 pixel game sprite of a ghostly, nearly invisible Brazilian woman politician in top-down isometric perspective. She is thin with short dark hair and deeply melancholic brown eyes — the saddest most resigned expression. She wears a faded olive green blouse and gray pants. Her entire body is SEMI-TRANSPARENT, as if she's always about to disappear. Unlike other characters who are grotesque and exaggerated, she is understated and minimal — her "deformity" is INVISIBILITY itself. Outlines are gray (not black), colors are washed out and neutral. She looks like a ghost who forgot she died. Style: the quietest character in a Robert Crumb underground comix world. Transparent PNG background.
```

### Midjourney

```
/imagine ghostly semi-transparent woman politician, thin, short dark hair, melancholic sad eyes, faded olive green top, gray pants, nearly invisible, fading into background, understated minimal caricature, gray soft outlines, desaturated washed colors, ethereal ghost, pixel art sprite 64x64, top-down isometric, existential sadness, Robert Crumb world but she's the quiet whisper, transparent background --ar 1:1 --style raw --no vibrant, saturated, grotesque, exaggerated, bold, thick outlines, bright colors
```

---

## PROMPTS POR ANIMACAO

### Idle (4 frames)

```
[BASE PROMPT] + standing still with arms at sides, distant unfocused gaze, slight hair movement from invisible breeze, barely there, alpha transparency oscillating, feet beginning to fade, pixel art sprite sheet, 4 frames horizontal strip, 256x64 pixels total, each frame slightly MORE transparent than previous then cycling back, ghostly subtle movement
```

### Walk (6 frames)

```
[BASE PROMPT] + floating walk cycle barely touching ground, 1 pixel gap between feet and shadow, gentle minimal movement, subtle afterimage ghost trail behind her, clothes barely moving (no wind no drama), body drifting more than walking, pixel art walk cycle sprite sheet, 6 frames horizontal strip, 384x64 pixels total, ethereal floating movement NOT heavy footsteps
```

### Attack (Touch of Confusion - 3 frames)

```
[BASE PROMPT] + becoming slightly MORE opaque for one moment (rare), reaching out with one hand to touch enemy, area around her becoming slightly blurred/distorted, then RAPIDLY becoming much more transparent as cost of being noticed, pixel art attack animation sprite sheet, 3 frames horizontal strip, 192x64 pixels total, subtle non-violent interaction
```

### Death / Disappearance (4 frames)

```
[BASE PROMPT] + gradually fading from feet upward, extremities disappearing first, then torso, then only face visible with sad eyes, then only eyes, then nothing, small white particles floating upward where she was, a single dried leaf falls to the ground, pixel art death animation sprite sheet, 4 frames horizontal strip, 256x64 pixels total, quiet melancholic disappearance NOT dramatic death
```

### Hit (2 frames)

```
[BASE PROMPT] + becoming MORE transparent when hit (opposite of others who flash white), body rippling like disturbed water, gentle 1 pixel shake, slightly sadder expression after, pixel art hit reaction sprite sheet, 2 frames horizontal strip, 128x64 pixels total, absorbing impact quietly
```

### Fade In / Aparicao (6 frames)

```
[BASE PROMPT] + appearing from nothing: frame 1 is just a vague shadow on the ground, frame 2 is a distorted silhouette blending with scenery, frame 3 shows gray outlines forming a human shape, frame 4 face becomes visible with melancholic expression, frame 5 body mostly visible but still translucent, frame 6 maximum opacity (still not fully opaque), pixel art apparition animation sprite sheet, 6 frames horizontal strip, 384x64 pixels total, ghostly materialization, slow gentle fade in
```

### Fade Out / Desaparicao (6 frames)

```
[BASE PROMPT] + disappearing gradually: starts at maximum opacity, extremities fade first (feet and hands), then legs and arms, then torso, then only sad face and shoulders visible, then only melancholic eyes in the void, then nothing except a small dried leaf falling and tiny white particles rising, pixel art disappearance animation sprite sheet, 6 frames horizontal strip, 384x64 pixels total, ghostly dematerialization, the saddest exit, quiet
```

### Presenca Espectral (4 frames loop)

```
[BASE PROMPT] + standing present but flickering like a candle in wind, alpha oscillating, edges of body rippling with heat-haze distortion, looking around hopefully waiting for interaction but slowly losing hope with each frame, pixel art idle-present loop sprite sheet, 4 frames horizontal strip, 256x64 pixels total, ghostly presence flickering
```

---

## PROMPTS PARA EFEITOS ESPECIAIS

### Folha Seca (Marca de Presenca)
```
pixel art tiny dried leaf, 4x4 pixels, brown #8B7355, slightly transparent, falling spiral animation 4 frames, 16x16 sprite sheet (4x4 per frame with padding), simple organic shape, transparent background, natural subtle
```

### Flocos de Desaparicao
```
pixel art small white particles floating upward, 2x2 pixels each, very faint alpha 60, 4-6 particles in different positions, rising gently, transparent background, ethereal ghost particles, subtle
```

### Distorcao de Borda (Heat Haze)
```
pixel art edge distortion effect, heat shimmer, edges of sprite area blurring and warping, scenery colors bleeding through, transparent overlay effect, 64x64 frame, very subtle almost imperceptible
```

---

## NEGATIVE PROMPTS

### Para TODOS os prompts de Marina, adicionar:

**Stable Diffusion:**
```
--negative_prompt grotesque, exaggerated, bulging, deformed body, thick black outlines, heavy shadows, saturated colors, bright colors, vibrant, bold, loud, aggressive, violent, gory, bloody, muscular, large, imposing, confident, happy, smiling wide, dramatic pose, action pose, weapon, armor, detailed accessories, busy design, cluttered, noisy, oversized head, caricature proportions, Robert Crumb grotesque
```

**Midjourney:**
```
--no grotesque, exaggerated, bulging, deformed, thick outlines, heavy shadows, saturated, vibrant, bold, loud, aggressive, violent, muscular, imposing, confident, happy, dramatic, weapon, armor, accessories, busy, cluttered, oversized head
```

**DALL-E 3:**
Incluir no prompt: "Do NOT make this character grotesque, exaggerated, bold, or visually loud. She must be the OPPOSITE: subtle, quiet, fading, minimal. No thick black outlines. No saturated colors. No dramatic poses. She is a ghost, a whisper, almost not there."

---

## STYLE TAGS

### Tags obrigatorias em TODOS os prompts:

```
ghostly, semi-transparent, fading, ethereal, minimal, understated, quiet, melancholic, sad, washed-out colors, gray outlines, pixel art, game sprite, top-down isometric, nearly invisible, existential, whisper
```

### Tags especificas de Marina:

```
ghost candidate, disappearing woman, forgotten politician, invisible presence, sad eyes, short dark hair, olive green, gray neutral, floating not walking, silent, resigned, dried leaf, four more years
```

---

## DICAS PARA GERACAO

1. **ANTI-padrao**: Marina e o OPOSTO de todos os outros personagens do jogo. Se os outros sao grotescos, ela e sutil. Se os outros sao barulhentos, ela e um sussurro. Reforcar isso em cada prompt.

2. **Alpha e TUDO**: O aspecto mais importante e a transparencia. Se a IA gerar uma Marina totalmente opaca, FALHOU. Ela deve parecer fantasmagorica SEMPRE.

3. **Olhos sao o ancora**: Os olhos de Marina sao a parte mais definida e expressiva. Mesmo quando o resto some, os olhos devem transmitir melancolica resignacao.

4. **Contornos CINZA, nao preto**: Isso e crucial para diferencia-la dos outros personagens. Linhas cinza #999999, finas (1px em vez de 2px).

5. **Cores LAVADAS**: Se a paleta ficar saturada, dessaturar 40-60%. As cores dela devem parecer que ja foram lavadas muitas vezes.

6. **Sem acessorios chamativos**: NAO adicionar armas, brilhos, itens magicos. A unica "marca" e a folha seca no cabelo. Menos e mais.

7. **Teste de invisibilidade**: Se voce colocar o sprite dela sobre um cenario e ela se DESTACAR, esta errado. Ela deve quase se confundir com o fundo.

8. **Sprite sheet alignment**: Como outros personagens, manter pes alinhados. Mas para Marina, os pes podem estar 1px ACIMA da linha base (ela flutua).

9. **Geracao em duas etapas**: Pode ser util gerar Marina em duas etapas:
   - Etapa 1: Gerar versao opaca com as caracteristicas corretas
   - Etapa 2: Aplicar alpha/transparencia em pos-processamento (mais controle)

10. **Contexto no prompt**: Mencionar que ela existe em um mundo de personagens GROTESCOS ajuda a IA entender o contraste: "In a world of grotesque exaggerated characters, she is the one nobody notices."
