# LULA (O Cachaceiro) -- Art Prompts for AI Image Generation
### Boss Principal (Lado Esquerdo) | Zumbis de Brasilia
### Estilo: Andre Guedes (Grotesco/Underground Comix)

---

## Instrucoes Gerais para Todos os Prompts

### Style Prefix (usar em TODOS os prompts)
```
in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background,
```

### Negative Prompt Global (usar em TODOS os prompts)
```
realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime style, cute, chibi, vector art, flat design, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, neutral expression, generic, stock photo, watermark, text overlay, blurry, low quality, deformed hands with 5 fingers on left hand
```

### Notas Tecnicas
- Resolucao de geracao: 512x512 ou 1024x1024, depois downscale para 64x64 com nearest-neighbor (sem anti-alias)
- Formato: PNG com transparencia
- Para Stable Diffusion: usar modelo checkpoint realista + LoRA de pixel art + LoRA de caricatura se disponivel
- Para DALL-E 3: incluir "pixel art game sprite" no prompt
- CFG Scale recomendado (SD): 7-9
- Steps recomendados (SD): 30-50
- Sampler recomendado (SD): DPM++ 2M Karras

---

## IDLE ANIMATION

### Idle Frame 1 -- Posicao Neutra Bebada
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man standing idle slightly drunk leaning left, messy white beard covering chin and jaw, ENORMOUS bulbous alcoholic red nose three times normal size with visible veins, half-closed drowsy eyes with heavy eyelids, prominent beer belly protruding under wrinkled dirty gray suit with crooked dark red tie, white shirt partially open showing hairy chest, LEFT HAND HAS ONLY 4 FINGERS missing pinky finger visible stump, right hand holding dark green bottle of cachaça with golden label, Frankenstein-style cranial scar on top of head with visible stitches and titanium plate, partial bandage on skull, dark red and brown earth color palette, grimy filthy look, political humor

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, neutral expression, 5 fingers on left hand, clean suit, sober expression, young face
```

### Idle Frame 2 -- Oscilacao Direita + Gole
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man swaying right while lifting bottle to mouth, messy white beard, ENORMOUS bulbous bright red alcoholic nose with veins, eyes almost completely shut in alcoholic bliss, head tilted back slightly, green cachaça bottle raised toward mouth golden label visible, prominent beer belly expanded with deep breath, wrinkled gray suit crooked red tie, LEFT HAND 4 FINGERS ONLY no pinky, Frankenstein cranial scar stretched with head tilt showing 4 stitch points, titanium plate glint, right foot slightly raised losing balance

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, neutral expression, 5 fingers on left hand, standing straight, sober
```

### Idle Frame 3 -- Arroto
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man burping with mouth wide open, small yellow-green vapor cloud coming from mouth, messy white beard, ENORMOUS bulbous red alcoholic nose even redder than normal pulsating, eyes opening slightly surprised by own burp, green cachaça bottle lowered with small drops splashing from opening, beer belly contracting from burp force, wrinkled gray suit with tie swinging to the side from body movement, LEFT HAND 4 FINGERS no pinky, cranial Frankenstein scar visible bandage flapping, disgusting comedic expression

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, dignified expression, 5 fingers on left hand, clean, elegant
```

### Idle Frame 4 -- Sossego Momentaneo
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man standing in brief moment of drunken contentment, slight satisfied cunning smile, messy white beard, ENORMOUS bulbous red alcoholic nose glowing, eyes half-open showing visible pupils for once, head tilted to expose full cranial Frankenstein scar with 5 visible stitch points and reddened skin around titanium plate, green cachaça bottle held low and relaxed in right hand, LEFT HAND 4 FINGERS gesturing slightly at nothing, beer belly prominent, wrinkled gray suit, crooked dark red tie, almost stable footing for once, sly politician expression

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, fully sober, alert eyes, 5 fingers on left hand
```

---

## WALK ANIMATION

### Walk Frame 1 -- Passo Esquerdo Inicio
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man taking drunken step forward left foot extended, body leaning right as counterweight, messy white beard, ENORMOUS bulbous red alcoholic nose, half-closed eyes, green cachaça bottle swinging back in right hand with liquid sloshing, LEFT HAND 4 FINGERS swinging forward, beer belly displaced forward by inertia, wrinkled gray suit flapping, head lagging behind body movement like a drunk, left foot raised off ground mid-step, cranial Frankenstein scar with stitches and bandage, stumbling walking pose

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, walking straight, sober gait, athletic, 5 fingers on left hand
```

### Walk Frame 2 -- Passo Esquerdo Contato
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man left foot just hitting ground with small dust cloud, body returning to less tilted position, messy white beard bouncing, ENORMOUS bulbous red nose, half-closed eyes, green cachaça bottle with small splash from impact, tie flying left from momentum, beer belly jiggling downward from step impact, LEFT HAND 4 FINGERS no pinky, wrinkled gray suit, cranial scar bandage flapping with movement, drunk stumble walk mid-cycle

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, graceful movement
```

### Walk Frame 3 -- Transferencia de Peso
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man mid-stride both feet on ground weight transferring, body nearly vertical for a moment, messy white beard, ENORMOUS bulbous red alcoholic nose swaying slightly, flushed red cheeks visible, half-closed eyes trying to focus forward, beer belly at maximum forward extension from momentum, LEFT HAND 4 FINGERS clearly visible in silhouette passing body, right hand holding bottle at side, wrinkled suit, crooked tie, cranial Frankenstein scar, brief moment of stability in drunken walk

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, walking normally
```

### Walk Frame 4 -- Passo Direito Inicio
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man taking step with right foot extended forward, body leaning LEFT as counterweight this time, messy white beard, ENORMOUS bulbous red nose, eyes barely open, green cachaça bottle swinging forward almost slipping from grip, LEFT HAND 4 FINGERS swinging back showing missing pinky stump, beer belly displaced to opposite side, wrinkled gray suit, tie flying, cranial scar visible, right foot raised off ground, drunken asymmetric walk

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, coordinated walk
```

### Walk Frame 5 -- Passo Direito Contato
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man right foot touching ground lighter impact, body recovering from lean, head doing small forward nod as if agreeing with himself, messy white beard bouncing, ENORMOUS bulbous red nose, half-closed eyes, beer belly jiggling, green bottle at side, tie flying right, LEFT HAND 4 FINGERS, wrinkled suit, cranial Frankenstein scar, micro-stumble recovery in drunk walk

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, steady walk
```

### Walk Frame 6 -- Tropeco Leve (Assinatura)
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man almost tripping forward, body pitched forward extra 10 degrees, feet close together recovering balance, eyes suddenly wide open in surprise, messy white beard, ENORMOUS bulbous red nose, green cachaça bottle tilting dangerously with 3 drops of liquid flying out, beer belly maximum downward sag from gravity during stumble, LEFT HAND 4 FINGERS reaching out for balance, wrinkled suit extra disheveled, cranial scar, comedic drunk stumble signature animation frame, about to fall but catching himself

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, graceful, elegant, balanced
```

---

## ATTACK ANIMATION -- "Cachaçada Companheira"

### Attack Frame 1 -- Wind-Up
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man winding up to throw bottle overhead, right arm raised HIGH above and behind head holding green cachaça bottle with golden label gleaming, torso rotated back in throwing position, LEFT HAND 4 FINGERS extended forward pointing at target with spread fingers MISSING PINKY very visible, face showing drunken RAGE with wide furious eyes bloodshot veins visible, eyebrows in angry V shape, mouth open screaming showing yellowish teeth, ENORMOUS bulbous red nose even bigger from anger, messy white beard bristling, beer belly contracted with effort, cranial scar stitches under tension, feet in throwing stance

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, calm expression, gentle throw
```

### Attack Frame 2 -- Arremesso
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man mid-throw releasing bottle, RIGHT HAND EMPTY with motion blur trail, green cachaça bottle flying through air rotating with liquid drops trailing behind it golden label visible, torso snapping forward from throw, LEFT HAND pulled to body from follow-through 4 FINGERS, face screaming "COMPANHEIRO" mouth enormous wide open tongue visible, ENORMOUS bulbous red nose, messy white beard, beer belly lurching forward with momentum, wrinkled suit, cranial Frankenstein scar, molotov cocktail throw pose, chaotic energy

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, gentle, careful throw, quiet expression
```

### Attack Frame 3 -- Follow-Through + Explosao
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man off-balance after throwing, leaning forward about to fall, satisfied EVIL GRIN on face with half-closed eyes of pleasure, ENORMOUS bulbous red nose shiny with sweat, messy white beard, beer belly hanging, wrinkled suit open, RIGHT HAND relaxed hanging after throw, LEFT HAND 4 FINGERS at side, EXPLOSION in background with orange fire and brown cachaça splashes and green glass shards flying, blue alcohol flames, cranial scar visible, post-throw comedic satisfaction pose, chaos behind him

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, clean explosion, serious expression
```

---

## DEATH ANIMATION

### Death Frame 1 -- Impacto
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man hit and recoiling backward, body bending at waist, head thrown back mouth in shocked O shape, eyes wide with tiny pupils in shock, ENORMOUS bulbous red nose deforming from impact, messy white beard pointing up, green cachaça bottle flying out of hand with splashes, cranial titanium plate flashing metallic glint from impact, beer belly showing wave motion from top going back while bottom still forward, tie flying up, LEFT HAND 4 FINGERS reaching up, feet leaving ground, dramatic telenovela death beginning

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, stoic, controlled fall, dignified
```

### Death Frame 2 -- Queda
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man falling backwards at 45 degree angle, eyes closing drowsily as if falling asleep, mouth murmuring open slightly, beard pointing upward, ENORMOUS bulbous red nose, LEFT HAND 4 FINGERS reaching dramatically skyward missing pinky visible, beer belly pointing up prominent, wrinkled suit jacket open showing hairy chest and dirty shirt, green bottle in mid-air further away spinning with glass shard separating, cranial scar visible, slow dramatic fall like soap opera death scene

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, quick fall, action movie
```

### Death Frame 3 -- Impacto no Chao
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man lying on back having just hit the ground, small cartoon stars circling head, dust cloud around body, ENORMOUS bulbous red nose pointing up, eyes showing small stars of impact, messy white beard splayed, beer belly rising like a hill, wrinkled suit fully open torn showing hairy chest and brown chest hair, shattered green glass pieces and pool of brown cachaça liquid on ground near body, LEFT HAND 4 FINGERS fallen to side, cranial scar stitch coming loose, top-down view of fallen body with impact effects

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, peaceful, clean ground
```

### Death Frame 4 -- Morto / Quarto Mandato Ready
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man lying completely flat on ground DEAD, X X eyes classic cartoon death, tongue hanging out side of mouth, ENORMOUS bulbous red nose now dimmer faded red, messy white beard disheveled flat, tie draped across face, beer belly prominent hill, arms spread out, LEFT HAND 4 FINGERS curled no pinky, shattered bottle pieces and expanding pool of cachaça on ground, cranial Frankenstein scar fully exposed stitches visible titanium plate dull, wrinkled torn suit, top-down dead body sprite, comedic death pose, ghost of green cachaça vapor rising

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, peaceful death, dignified, sleeping
```

---

## HIT ANIMATION

### Hit Frame 1 -- Flash de Dano
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, pixel art 64x64, game sprite with transparent background, WHITE SILHOUETTE FLASH of old man politician body shape, glowing white outline with red border, motion blur 3 pixels backward showing recoil direction, small red damage particles flying from impact point, beer belly silhouette visible, bottle silhouette, 4 finger left hand silhouette, Frankenstein scar head shape, damage flash frame, invincibility frame sprite

Negative: realistic, detailed, colored, normal appearance, calm, full color rendering, 5 fingers
```

### Hit Frame 2 -- Reacao de Raiva
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man FURIOUS after being hit, overall red tint to entire body from rage, eyebrows in extreme V shape ANGER, mouth square shape screaming in rage, ENORMOUS bulbous red nose pulsating expanded extra, eyes of fury with red tinted pupils, beer belly inflated from rage breath, LEFT HAND 4 FINGERS clenched in fist missing pinky gap visible, right hand squeezing cachaça bottle deforming it, messy white beard bristling with anger, wrinkled suit, cranial scar, pure politician tantrum

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, calm, accepting, gentle
```

---

## SPECIAL ANIMATIONS

### Special: "Fato Alternativo" -- Frame 3 (Key Frame: Onda de Distorcao)
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man emitting wave of dark red energy from body, concentric distortion rings expanding outward in dark red and brown, LEFT HAND 4 FINGERS pointing at viewer accusingly, eyes glowing red with supernatural politician power, cunning manipulative LIAR smile, messy white beard, ENORMOUS bulbous red nose, cachaça bottle tucked under arm, beer belly, wrinkled suit, cranial scar, reality warping propaganda magic, political lie made manifest as visual distortion, UI glitch aesthetic

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, honest expression, trustworthy
```

### Special: "Dedo Perdido" -- Frame 2 (Key Frame: Dedada)
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man lunging forward in melee attack, LEFT HAND 4 FINGERS extended in eye-poke V shape like Three Stooges, index and middle finger forming V pointing forward, ONLY 4 FINGERS clearly visible NO PINKY with obvious gap where fifth finger should be, body stretched forward maximum reach, evil mischievous grin one eyebrow raised, ENORMOUS bulbous red nose, messy white beard, beer belly, wrinkled suit, cranial scar, comedic eye poke attack, grotesque close combat

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, gentle touch, kind expression
```

### Special: "Quarto Mandato" -- Frame 5 (Key Frame: Ressurreicao)
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man sitting up from death rising from the ground like zombie resurrection, torso at 30 degrees from ground one arm supporting, eyes reopening from X X death to half-closed drunk eyes again, color returning to skin from pale to ruddy, ENORMOUS bulbous red nose starting to glow red again pulsating, cachaça dripping from chin supernatural revival liquid, messy white beard, beer belly, wrinkled torn suit more damaged than before, cranial Frankenstein scar titanium plate glowing, golden supernatural particles floating around body, resurrection power up, zombie politician rising from the dead AGAIN, third mandate joke

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, staying dead, peaceful, beautiful resurrection
```

### Special: "Empurra Mole / Faz o L" -- Frame 4 (Key Frame: L Completo)
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man making L HAND GESTURE high above head with LEFT HAND which has ONLY 4 FINGERS, index finger up and thumb out forming L shape other fingers closed, missing pinky making the L look wrong and grotesque, bright red glowing outline around the L gesture, white flash behind, face exultant screaming mouth wide open, ENORMOUS bulbous red nose glowing, eyes intense, ground cracking beneath feet with dark energy lines radiating outward, shockwave forming, dark red and brown energy aura, messy white beard, beer belly, wrinkled suit, cranial scar, political gesture as weapon, slow motion power attack

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, right hand making gesture, gentle wave, peaceful
```

### Special: "Discurso de Hora e Meia" ULTIMATE -- Frame 5 (Key Frame: Pico Emocional)
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque caricature, Robert Crumb inspired, thick irregular ink lines, dirty saturated colors, extreme anatomical exaggeration, B-movie horror comedy, pixel art 64x64, top-down slightly isometric view, game sprite with transparent background, old Brazilian politician man standing on wooden PODIUM elevated above ground with dark red flags hanging, holding microphone in LEFT HAND 4 FINGERS, right hand on chest emotional fake tears, eyes closed with emotion one tear drop, mouth enormously open in passionate speech, visible sound wave arcs emanating from mouth, golden healing aura surrounding body absorbing green healing particles, ENORMOUS bulbous red nose, messy white beard, beer belly, wrinkled suit, cranial scar, wooden podium with red PT color decorations below feet, political rally speech as ultimate weapon, everyone forced to listen, narcissistic politician on stage, healing while talking, comedic megalomania

Negative: realistic, photorealistic, beautiful, pretty, clean lines, smooth shading, 3D render, anime, cute, vector, minimalist, pastel colors, bright clean colors, symmetrical, perfect proportions, 5 fingers on left hand, sincere tears, genuine emotion, humble speaker, modern podium
```

---

## SKIN VARIANT PROMPTS

### Skin: Normal (Base -- descrito acima)
Todos os prompts acima sao para a skin base/normal.

### Skin: 2026 Frankenstein (Cicatriz Enfatizada)
**Modifier to add to all prompts:**
```
, EMPHASIZED cranial surgery scars covering entire top of head, multiple Frankenstein stitching lines criss-crossing skull, large visible titanium plate with screws, partially removed bandages hanging loose, fresh surgical redness around all incision lines, more stitches more grotesque more medical horror, hospital bracelet still on wrist
```

### Skin: Zombie Premium
**Modifier to add to all prompts:**
```
, ZOMBIE VERSION with decaying green-gray skin, exposed skull bone through rotting cranial scar, nose even more bulbous and purple with rot, one eye hanging from socket, torn suit with ribs visible through holes, cachaça bottle fused into hand flesh, beer belly bloated with decomposition gases, maggots in beard, zombie politician undead horror comedy, green toxic drool
```

### Skin: Cachaceiro de Gala
**Modifier to add to all prompts:**
```
, wearing fancy WHITE TUXEDO stained with cachaça, red bow tie instead of regular tie, top hat slightly crushed and tilted, monocle over one half-closed eye, golden cufflinks, patent leather shoes scuffed, trying to look elegant but still drunk and grotesque, fancy drunk politician at gala event, beer belly stretching tuxedo buttons to breaking point
```

### Skin: Operario (Throwback)
**Modifier to add to all prompts:**
```
, wearing blue FACTORY WORKER overalls with grease stains, hard hat over cranial scar barely fitting, union badge on chest, younger but still grotesque, less white in beard more dark gray, same enormous red nose, steel-toed boots, welding gloves on but still showing 4 fingers on left hand, working class politician origin skin throwback
```

---

## WEAPON PROMPT -- Garrafa de Velho Barreiro Incendiaria

### Standalone Weapon Sprite
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque, pixel art 32x32, game sprite with transparent background, dark green glass bottle of Brazilian cachaça labeled "Velho Barreiro" with golden vintage label, cloth fuse stuffed in bottle neck with small flame burning, brown cachaça liquid inside sloshing, bottle slightly cracked with leaking drops, molotov cocktail made from cachaça bottle, weapon item sprite, thick irregular outline, dirty colors

Negative: realistic, photorealistic, clean, modern bottle, wine bottle, smooth, vector, minimalist, bright colors, no label
```

### Weapon Impact/Explosion Sprite
```
Prompt: in the style of André Guedes Brazilian political cartoon, underground comix grotesque, pixel art 32x32, game sprite with transparent background, EXPLOSION of cachaça bottle, orange and brown fire burst, blue alcohol flames, green glass shards flying outward, brown liquid splashing in all directions, puddle of burning cachaça forming below, chaotic dirty explosion, molotov cocktail impact, thick lines, grimy fire colors not clean orange

Negative: realistic, photorealistic, clean explosion, nuclear, mushroom cloud, bright clean fire, smooth, vector, minimalist
```

---

## EFFECT SPRITES

### Cachaca Puddle (Ground Hazard)
```
Prompt: pixel art 32x32, game sprite with transparent background, top-down view puddle of brown cachaça liquid on ground with blue alcohol flames flickering on surface, green glass shard pieces scattered in and around puddle, dirty brown and orange tones, fire hazard ground tile, grimy liquid pool, thick pixel outlines

Negative: realistic, water, clean, blue liquid, smooth, vector
```

### Speech Bubble Loop (Ultimate Effect)
```
Prompt: pixel art 48x16, game sprite with transparent background, comic speech bubble with text "Eu quero dizer..." trailing off with ellipsis, wobbly hand-drawn bubble outline, dirty white fill, red accent marks, politician speech bubble, repeating loop text that never reaches the point, underground comix style lettering

Negative: realistic, clean typography, modern font, vector, smooth bubble, complete sentence
```

### L Gesture Shockwave Ring
```
Prompt: pixel art 48x48, game sprite with transparent background, circular shockwave ring expanding outward, dark red and brown energy colors, irregular not perfectly round, cracking ground effect inside ring, political energy wave, dirty saturated colors, thick pixel lines, distortion ripple effect

Negative: realistic, clean circle, perfect ring, bright colors, smooth gradient, vector, energy beam
```
