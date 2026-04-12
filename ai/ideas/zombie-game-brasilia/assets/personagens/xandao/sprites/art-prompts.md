# XANDAO - Art Prompts para Geracao de Assets

## Boss do STF Principal - "Zumbis de Brasilia"

---

## Instrucoes Gerais para Todos os Prompts

### Prefixo Universal (adicionar ANTES de cada prompt)
```
pixel art, 64x64 sprite, retro game character, grotesque underground comix style,
inspired by Robert Crumb and Brazilian political cartoons by Andre Guedes,
thick outlines, heavy shadows, exaggerated proportions, dirty saturated colors,
B-movie horror aesthetic, no anti-aliasing, transparent background, PNG,
```

### Sufixo Universal (adicionar DEPOIS de cada prompt)
```
--style raw --no photorealistic --no smooth --no cute --no anime
--ar 1:1 --s 250 --c 30
```

### Negative Prompts (usar SEMPRE)
```
smooth shading, anti-aliasing, cute, kawaii, anime, realistic,
photographic, 3D render, clean lines, symmetrical, pretty,
soft colors, pastel, gentle expression, friendly, nice suit,
clean clothes, pressed suit, gentle eyes, calm expression
```

---

## PROMPTS POR ESTADO DE ANIMACAO

---

### 1. IDLE - Postura Parada Ameacadora

#### Prompt Principal (Midjourney/DALL-E)
```
pixel art sprite sheet, 4 frames horizontal, 64x64 each frame,
grotesque bald Brazilian judge character "XANDAO",
extremely shiny reflective bald head like a mirror with white highlight,
permanent angry scowl, thick furrowed eyebrows,
small glowing red eyes with rage,
square prominent jaw, thick MMA fighter neck with visible bulging veins,
wearing dirty wrinkled black judge robe (toga),
absurdly oversized biceps bulging under the robe fabric stretching,
holding a COMICALLY OVERSIZED judge gavel bigger than himself on shoulder,
gavel has "CENSURADO" written in red letters,
standing power pose with legs apart,

frame 1: neutral angry stance bald gleaming,
frame 2: bald head shine shifts position veins pulse,
frame 3: robe flutters slightly biceps flex larger,
frame 4: biceps at maximum size robe stretching veins maximum,

underground comix style Robert Crumb inspired,
thick black outlines heavy crosshatch shadows,
dirty saturated color palette blood orange sky sickly green accents,
twitchy jerky animation feel deformed organic proportions,
Brazilian political cartoon grotesque humor
```

#### Prompt Stable Diffusion (mais tecnico)
```
(pixel art:1.4), (sprite sheet:1.3), 4 frames horizontal,
(64x64 pixels:1.2), (transparent background:1.3),
(grotesque:1.4) bald man, (extremely shiny bald head:1.5),
(mirror-like scalp reflection:1.3), (white highlight on head:1.2),
(angry expression:1.5), (furrowed brow:1.3), (red glowing eyes:1.3),
(thick neck:1.3), (bulging veins:1.4), (forehead veins:1.3),
(black dirty robe:1.3), (wrinkled fabric:1.2),
(absurdly large biceps:1.5), (muscles stretching robe:1.4),
(oversized gavel:1.5), (comically large hammer:1.4),
red text "CENSURADO" on gavel,
(underground comix style:1.3), (Robert Crumb inspired:1.2),
(thick outlines:1.3), (heavy shadows:1.3),
(no anti-aliasing:1.2), (retro game:1.2),
(political cartoon:1.3), (Brazilian humor:1.1)

Negative: smooth, cute, anime, realistic, 3d, soft, gentle,
clean suit, pressed clothes, thin neck, small arms, friendly
```

---

### 2. WALK - Marcha Intimidadora

#### Prompt Principal
```
pixel art sprite sheet, 6 frames horizontal walk cycle, 64x64 each frame,
grotesque bald Brazilian judge "XANDAO" walking menacingly,
shiny bald head reflecting light differently each frame,
angry stomping march like military dictator,
dragging an ENORMOUS judge gavel on the ground behind him,
gavel scraping ground creating cracks and sparks,
ground cracking under his heavy footsteps,
dirty black robe billowing behind from movement,
huge biceps visible under stretching robe fabric,
thick veiny neck, permanent scowl, red glowing eyes,
dust particles rising from heavy steps,

frame 1: right foot forward gavel dragging ground cracking,
frame 2: weight on right leg body lower gavel lifts slightly,
frame 3: legs passing neutral gavel sparking on ground,
frame 4: left foot forward new ground crack,
frame 5: weight on left leg body lower veins maximum,
frame 6: transition dust rising gavel raised slightly,

underground comix grotesque Robert Crumb style,
thick outlines dirty saturated colors twitchy animation,
Brazilian political cartoon B-movie horror aesthetic
```

#### Prompt Stable Diffusion
```
(pixel art:1.4), (sprite sheet:1.3), (walk cycle:1.3), 6 frames,
(64x64:1.2), (transparent background:1.3),
(grotesque bald judge:1.4), (shiny reflective bald head:1.5),
(intimidating march:1.3), (heavy footsteps:1.2),
(dragging oversized gavel:1.5), (ground cracking:1.3),
(sparks from gavel:1.2), (dirty black robe:1.3),
(robe billowing:1.2), (huge biceps:1.4),
(angry expression:1.4), (red eyes:1.3), (bulging veins:1.3),
(dust particles:1.2), (military march:1.2),
(underground comix:1.3), (thick outlines:1.3),
(political cartoon:1.3), (retro pixel game:1.2)

Negative: smooth walking, graceful, elegant, light steps,
clean ground, small hammer, thin arms, calm, peaceful
```

---

### 3. ATTACK - Martelada da Censura

#### Prompt Principal
```
pixel art sprite sheet, 3 frames horizontal attack animation, 64x64 each,
grotesque bald judge "XANDAO" smashing with ENORMOUS gavel,

frame 1 WINDUP: gavel raised HIGH above head reaching top of sprite,
biceps at MAXIMUM size robe tearing at shoulders,
veins popping everywhere red eyes wide mouth screaming,
bald head gleaming at maximum shine from exertion,

frame 2 IMPACT: gavel SMASHING down in front,
impact explosion white and red flash 6x6 pixels,
"CENSURADO" text appearing in red above impact point,
ground shattering in star crack pattern,
robe flying upward from violent motion dust everywhere,

frame 3 SHOCKWAVE: shockwave rings emanating from impact,
gavel on ground cracks spreading three directions,
dust cloud brown-gray particles,
cruel satisfied smirk on face bald head dimming,

underground comix grotesque Robert Crumb style,
thick outlines heavy shadows dirty saturated colors,
Brazilian political cartoon absurd violence humor,
B-movie horror impact effects screen shake feeling
```

#### Prompt Stable Diffusion
```
(pixel art:1.4), (sprite sheet:1.3), 3 frames attack animation,
(64x64:1.2), (transparent background:1.3),
(grotesque judge:1.4), (shiny bald head:1.5),
(ENORMOUS gavel attack:1.5), (oversized hammer smash:1.4),
(frame 1 windup:1.2) gavel above head (bulging biceps:1.5),
(frame 2 impact:1.3) (explosion:1.3) (CENSURADO text:1.4) (ground crack:1.3),
(frame 3 shockwave:1.2) (concentric rings:1.3) (dust cloud:1.2),
(screaming face:1.3), (red eyes wide:1.3), (veins popping:1.4),
(robe billowing:1.3), (violent motion:1.3),
(underground comix:1.3), (Robert Crumb:1.2),
(thick outlines:1.3), (heavy shadows:1.3)

Negative: gentle, soft hit, small hammer, calm, controlled,
clean impact, no debris, peaceful, elegant swing
```

---

### 4. DEATH - Toga Vira Papeis de Inquerito

#### Prompt Principal
```
pixel art sprite sheet, 4 frames horizontal death animation, 64x64 each,
grotesque bald judge "XANDAO" defeated and falling,

frame 1 SHOCK: recoiling backwards eyes WIDE with surprise NOT anger,
mouth open in O shape first time showing vulnerability,
bald head flickering between shiny and dull,
gavel slipping from hand robe starting to disintegrate at edges,

frame 2 FALLING: falling backwards knees buckling,
gavel on ground cracking into pieces,
robe 30% decomposed into flying PAPER DOCUMENTS inquiry papers,
4-6 small white paper rectangles floating away,
bald head barely shining eyes closing red fading,

frame 3 DOWN: on the ground legs up,
gavel shattered into 3 pieces beside body,
robe 70% decomposed paper documents scattered everywhere,
8-10 paper rectangles at various heights some with red text "INQUERITO",
bald head NO SHINE completely dull opaque,
eyes closed veins disappearing,

frame 4 FINAL: body silhouette nearly covered by papers,
only gavel handle visible among papers,
robe 100% gone only papers remain,
bald head like dead stone zero reflection,
body semi-transparent 70% opacity papers fully opaque,
faint red glow on scattered papers residual power,

underground comix grotesque dramatic death scene,
Robert Crumb style thick outlines heavy tragedy,
papers flying like bureaucratic explosion
```

#### Prompt Stable Diffusion
```
(pixel art:1.4), (sprite sheet:1.3), 4 frames death animation,
(64x64:1.2), (transparent background:1.3),
(grotesque judge defeated:1.4), (bald head losing shine:1.5),
(robe disintegrating into papers:1.5), (paper documents flying:1.4),
(inquiry papers scattered:1.3), (gavel breaking:1.3),
(falling backwards:1.3), (surprised expression:1.3),
(vulnerability shown:1.2), (veins fading:1.2),
(progressive decomposition:1.3), (bureaucratic explosion:1.3),
(dramatic death:1.3), (body becoming transparent:1.2),
(papers with red text INQUERITO:1.3),
(underground comix:1.3), (thick outlines:1.3),
(Robert Crumb style:1.2), (heavy dramatic shadows:1.3)

Negative: peaceful death, dignified, clean, no papers,
robe intact, standing, fighting, angry expression in final frame
```

---

### 5. HIT - Recuo Furioso

#### Prompt Principal
```
pixel art sprite sheet, 2 frames horizontal hit reaction, 64x64 each,
grotesque bald judge "XANDAO" hit and becoming ANGRIER,

frame 1 RECOIL: body displaced backwards 4 pixels,
white damage flash outline 1 pixel border,
eyes WIDE OPEN red at MAXIMUM intensity 3x3 red glow each eye,
mouth open screaming in fury bald head glowing RED not white,
veins DOUBLED in size pulsing vivid red,
biceps instantly SWELLING 3 pixels larger,
robe rippling violently gavel gripped white-knuckled,
3-4 red pixels shooting from eyes beginning of laser beams,

frame 2 RAGE AMPLIFIED: body back to position but 1px LARGER in each direction,
short red laser beams from eyes 4 pixels long,
veins at ABSOLUTE MAXIMUM visible on arms too,
bald head returning to white but MORE INTENSE than normal 4x4 highlight,
jaw clenched muscles visible robe stretching with expanded body,
faint red aura glow 1 pixel around entire body,
visual communication that boss is now MORE DANGEROUS,

underground comix grotesque Robert Crumb fury expression,
thick outlines rage incarnate power increasing,
Brazilian political cartoon angry authority figure
```

#### Prompt Stable Diffusion
```
(pixel art:1.4), (sprite sheet:1.3), 2 frames hit reaction,
(64x64:1.2), (transparent background:1.3),
(grotesque judge enraged:1.5), (hit reaction:1.3),
(bald head glowing red then white:1.4),
(eyes maximum red glow:1.5), (laser beams from eyes:1.3),
(veins doubled:1.4), (biceps swelling:1.4),
(white damage flash:1.3), (body expanding with rage:1.3),
(red aura:1.3), (white knuckle grip:1.2),
(screaming fury:1.4), (jaw clenched:1.3),
(more dangerous visual:1.3), (power increasing:1.2),
(underground comix:1.3), (Robert Crumb:1.2),
(thick outlines:1.3), (rage expression:1.4)

Negative: hurt, weakened, scared, retreating, losing power,
calm, controlled, small eyes, thin veins, relaxed muscles
```

---

### 6. SPECIAL - Censura Monocratica (Raios dos Olhos)

#### Prompt Principal
```
pixel art sprite sheet, 6 frames horizontal special attack, 64x64 each,
grotesque bald judge "XANDAO" performing CENSORSHIP ULTIMATE POWER,

frame 1 PREPARE: rigid military posture left hand raising palm forward STOP gesture,
gavel in right hand pointed down eyes narrowing red glow building,
bald head concentrating light in center like charging energy,

frame 2 HAND UP: left hand fully raised fingers spread,
red glow aura around palm 3x3 pixels,
eyes brightening text "MONOCRATICAMENTE" beginning to form,
air distortion heat wave effect around body,

frame 3 EYE BEAMS ACTIVATE: eyes FIRE horizontal red laser beams extending 8px beyond sprite,
beams 2px thick bright red with yellow border,
hand maintained aura expanded body levitating 2px,
robe billowing upward bald head MAXIMUM RED GLOW,

frame 4 CENSURADO APPEARS: laser beams converge at point ahead,
GIANT "CENSURADO" text stamp style red with black border appears above,
body floating 3px robe horizontal toga billowing,
fist clenched now shockwave circles emanating from text,

frame 5 EXPANSION: CENSURADO text expanding and pulsing larger,
silence wave propagating all directions larger arcs,
body descending eye beams diminishing,
letter fragments C E N flying as shrapnel particles,
area of effect visual 5-tile radius red border,

frame 6 CONCLUSION: CENSURADO fading text pulsing weak,
body landed arms crossed arrogant smile,
bald head returning to white glow,
ground has residual red glow in affected area,
robe settled slightly smoking smugly satisfied expression,

underground comix grotesque Robert Crumb absolute power,
thick outlines supernatural censorship power,
Brazilian political satire judge with godlike powers
```

---

### 7. SPECIAL - Xandaquistao (Zona de Controle)

#### Prompt Principal
```
pixel art sprite sheet, 8 frames horizontal zone creation, 64x64 each,
grotesque bald judge "XANDAO" creating AUTHORITARIAN CONTROL ZONE,

frame 1: imperial stance chin up gavel raised as scepter,
eyes glowing GOLD not red different power bald head golden shine,
mouth screaming "XANDAQUISTAO" robe edges turning golden,

frame 2: gavel SLAMS into ground massive impact,
golden and red particle explosion at impact point,
star crack pattern BIGGER than normal attack,
body leaning forward from effort seismic wave expanding,

frame 3: influence circle beginning to form golden border expanding,
gavel stuck in ground vibrating body straightening arms open,
golden dust rising from ground around robe transforming,

frame 4: zone 50% formed 2 red banners appear on sides,
banners have CROSSED OUT X symbol generic X with slash through it,
ground inside zone changing color darker red-brown,
golden details appearing on robe eyes intense gold,

frame 5: zone 75% formed golden border bright 4 banners waving,
ground fully transformed inside zone body floating 2px,
golden and red particles intensifying gavel glowing as anchor,

frame 6: zone 100% complete solid golden border,
dark red floor inside different texture pattern,
4 banners at cardinal positions body lands toga now MILITARY style,
eyes returning to red gold fading gavel back in hand,

frame 7: zone pulsing border expanding contracting 1px,
ripple effects on ground showing force field,
body patrolling inside guard pose cruel smile territorial satisfaction,

frame 8: sustained state zone active subtle pulse,
sentinel stance gavel on shoulder eyes scanning,
military toga stabilized reduced particles border glow only,

underground comix grotesque Robert Crumb dictatorial power,
thick outlines territorial domination zone control,
dystopian political cartoon authoritarian aesthetic
```

---

### 8. SPECIAL - Apagao Digital / Ultimate

#### Prompt Principal
```
pixel art sprite sheet, 6 frames horizontal ultimate attack, 64x64 each,
grotesque bald judge "XANDAO" SHUTTING DOWN THE INTERNET,

frame 1 POWER RAISE: imposing stance chest puffed,
right hand raised index finger pointing up like power switch,
gavel in left hand on ground eyes glowing white-BLUE electricity,
bald head reflecting BLUE like computer screen,
static electricity running through robe thin blue-white lines,
EVIL smile robe crackling with energy,

frame 2 ELECTRICITY CONCENTRATES: sphere of electricity forms at fingertip 4x4 pixels blue-white,
electric arcs zigzag from body to sphere thin lines,
bald head BRIGHT BLUE eyes completely white no pupils,
robe undulating with electromagnetic field,
electricity running through gavel handle colored static pixels appearing,

frame 3 DISCHARGE: hand SLAMS down sphere fires upward,
total power pose leaning back,
"no internet" wifi-X icon beginning to appear,
electricity EXPLODES in all directions from sphere,
environment darkening DRAMATICALLY static pixels INTENSE,
robe lifting from discharge force,

frame 4 TOTAL STATIC: entire frame covered by TV static pattern,
random black white colored pixels noise pattern,
XANDAO visible ONLY as dark silhouette in center of static,
bald head only point of blue glow in silhouette,
"CONEXAO PERDIDA" text flashing "no signal" bars at edges,
representing moment HUD disappears player goes blind,

frame 5 SUSTAINING BLACKOUT: static slightly reduced still intense,
XANDAO silhouette more visible laughing open mouth,
TWO bright red eye dots in silhouette ONLY vivid color,
text alternating between "CENSURADO" and "SEM SINAL",
horizontal CRT scanlines at screen edges,

frame 6 RECOVERY: static rapidly dissipating pixels disappearing,
XANDAO fully visible again arms crossed satisfaction smile,
bald head returning to normal white glow,
eyes back to standard red robe settling residual electric smoke,
environment brightening last static pixels vanishing,
expression says "see I can shut down everything",

underground comix grotesque Robert Crumb technological destruction,
thick outlines digital apocalypse TV static horror,
Brazilian political cartoon internet censorship satire
```

---

## PROMPTS PARA PROJETEIS (32x32px)

### Projetil: Multa do X
```
pixel art sprite sheet, 4 frames, 32x32 each, transparent background,
spinning projectile combining X/Twitter bird logo with dollar sign $,
frame 1: X logo with $ overlay rotation 0 degrees,
frame 2: rotation 90 degrees red glow,
frame 3: rotation 180 degrees money particles flying off,
frame 4: rotation 270 degrees trail of "R$" behind,
grotesque style thick outlines red and gold colors,
retro game projectile no anti-aliasing
```

### Projetil: Raio do Olho
```
pixel art sprite sheet, 2 frames, 32x32 each, transparent background,
horizontal red laser beam energy projectile,
frame 1: bright red beam with yellow border clean,
frame 2: beam pulsing slightly larger more intense color,
retro game projectile thick outlines no anti-aliasing,
energy beam censorship power red yellow colors
```

### Efeito: Texto CENSURADO
```
pixel art sprite sheet, 3 frames, 32x32 each, transparent background,
"CENSURADO" rubber stamp text effect,
frame 1: text fading in red stamp style tilted,
frame 2: text pulsing border expanding bright red black outline,
frame 3: text fragmenting letters breaking apart fading out,
grotesque style thick outlines retro game effect
```

### Efeito: Static/Apagao (Tileable)
```
pixel art sprite sheet, 4 frames, 32x32 each,
TV static noise pattern tileable seamless,
random black white and colored pixels,
CRT television interference pattern,
each frame different random pattern for animation,
retro game overlay effect horror static,
must tile seamlessly horizontally and vertically
```

---

## PROMPTS PARA UI

### Retrato do Boss (32x32)
```
pixel art portrait, 32x32 single frame, transparent background,
grotesque bald judge close-up face portrait,
extremely shiny bald head white highlight,
thick furrowed angry eyebrows small red glowing eyes,
square jaw prominent thick veiny neck,
dark red background with robe texture,
golden ornate border like coat of arms,
Robert Crumb underground comix style,
thick outlines heavy shadows game UI boss portrait
```

### Icone HP (16x16)
```
pixel art icon, 16x16 single frame, transparent background,
tiny minimalist bald head icon,
shiny white highlight on top red dot eyes,
game UI health bar indicator boss icon,
thick outline simple readable at small size
```

---

## PROMPTS PARA SKINS (ver skin-variants.md para detalhes)

### Skin: Xandaquistao (Militar)
```
Adicionar ao prompt base de cada animacao:
"military style robe dark olive green with golden epaulettes,
military beret instead of bare head (but head still shiny underneath),
medals on chest authoritarian dictator aesthetic,
red armband with crossed-out X symbol"
```

### Skin: Sancionado (USA)
```
Adicionar ao prompt base:
"robe with LARGE red white blue USA sanction stamp seal,
official looking document pinned to robe,
embarrassed-angry expression reddened face,
small American flags stuck to robe like sticky notes"
```

### Skin: Mao TSE Tung (Comunista)
```
Adicionar ao prompt base:
"communist red robe with golden star emblems,
Mao collar on robe raising little red book in hand,
propaganda poster aesthetic socialist realism mixed with grotesque,
hammer and sickle replacing gavel design"
```

### Skin: Dormindo (Pijama Meme)
```
Adicionar ao prompt base:
"wearing polka dot pajamas nightcap on bald head,
sleepy half-closed eyes drool from mouth corner,
ZZZ floating above head pillow tucked under arm instead of gavel,
bedroom slippers instead of shoes relaxed not angry for once"
```

---

## DICAS TECNICAS PARA GERACAO

### Para Midjourney
- Usar `--style raw` para evitar embelezamento
- `--s 250` para maior estilizacao
- `--c 30` para mais variacao (escolher a mais grotesca)
- Versao v6 ou superior
- Repetir geracao 4-8 vezes, escolher resultado mais grotesco

### Para DALL-E 3
- Ser MUITO especifico sobre "pixel art" e "64x64"
- Enfatizar "no anti-aliasing" e "thick outlines"
- DALL-E tende a suavizar - adicionar "rough", "dirty", "crude"
- Pode precisar de pos-processamento para atingir 64x64 exato

### Para Stable Diffusion
- Usar modelo treinado em pixel art (ex: pixel-art-xl)
- ControlNet com pose reference para consistencia entre frames
- CFG Scale: 7-9 (mais alto = mais fiel ao prompt)
- Steps: 30-50
- Usar img2img com frame anterior para manter consistencia

### Pos-Processamento Obrigatorio
1. Redimensionar para exatamente 64x64 (nearest neighbor, NAO bilinear)
2. Reduzir paleta para cores especificadas no sprite-spec.md
3. Adicionar outline preto de 1px se nao presente
4. Verificar transparencia do fundo
5. Alinhar todos os frames na sprite sheet horizontal
6. Verificar que personagem esta CENTRALIZADO em cada frame
7. Testar animacao em loop para verificar transicoes
