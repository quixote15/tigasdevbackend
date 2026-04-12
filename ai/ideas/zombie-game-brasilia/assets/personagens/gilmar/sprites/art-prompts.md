# Gilmar Mendes — Art Prompts para Geracao de Imagem

## Boss do STF — "O Coringa do STF" | Zumbis de Brasilia

---

## Instrucoes Gerais para TODOS os Prompts

### Estilo Obrigatorio
Todos os prompts devem gerar imagens no estilo **Andre Guedes / underground comix brasileiro**:
- Robert Crumb + humor politico BR + horror B-movie
- Linhas GROSSAS e IRREGULARES (simular mao humana)
- Cores SATURADAS mas SUJAS (nunca cores puras digitais)
- Cross-hatching para sombras (nunca gradientes suaves)
- Textura de papel/offset barato como overlay
- Proporcoes GROTESCAS: cabeca enorme, corpo pequeno
- Expressoes EXAGERADAS ao extremo

### Parametros Tecnicos
- **Resolucao de trabalho**: 512x512px (depois reduzir pra 64x64px)
- **Fundo**: Transparente (alpha channel)
- **Perspectiva**: Top-down levemente isometrica
- **Paleta restrita**: Usar paleta definida em sprite-spec.md

### Palavras-Chave de Estilo (usar em TODOS os prompts)
```
underground comix style, Robert Crumb influence, grotesque caricature,
thick irregular ink outlines, cross-hatching shadows, saturated dirty colors,
paper texture overlay, hand-drawn imperfections, Brazilian political satire,
pixel art, sprite sheet frame, 64x64 pixel art, transparent background
```

---

## PROMPT 01 — Character Sheet / Referencia Visual Completa

### Prompt Principal (Stable Diffusion / DALL-E)
```
Character design sheet of a grotesque elderly Brazilian Supreme Court minister caricature.
Short old man, ENORMOUS 1970s-style glasses covering half his face, thick brown frames.
TRIPLE chin (three distinct layers of neck fat, each hanging lower than the last).
Thin hair combed to the side (5-7 visible strands, grey).
PERMANENT cynical smirk — right corner of mouth lifted, "I know something you don't" expression.
Wearing a black judge's robe (toga) stained with GREASE spots from pastéis (Brazilian fried pastries).
Pastry crumbs visible on the robe. Left pocket stuffed with money bills (green paper sticking out).
Right hand holds a half-eaten greasy pastel. Left hand holds a cellphone with green screen showing "VORCARO" contact.
Tiny legs barely visible under the long robe.

Style: underground comix, Robert Crumb influence, grotesque Brazilian political caricature,
thick irregular ink outlines 2-3px, cross-hatching shadows, saturated dirty color palette,
paper texture overlay, hand-drawn imperfections, extremely exaggerated proportions.

Views: front, side, 3/4 angle, back.
Transparent background. Character sheet layout.
```

### Prompt Alternativo (Midjourney)
```
/imagine grotesque Brazilian Supreme Court judge caricature, character sheet,
tiny old man with ENORMOUS 70s glasses, triple chin hanging, thin combover hair,
permanent cynical smirk, black robe stained with grease and pastry crumbs,
money falling from pockets, holding half-eaten pastel and cellphone,
Robert Crumb underground comix style, thick ink lines, cross-hatching,
dirty saturated colors, paper texture, political satire --ar 1:1 --v 6 --style raw
```

---

## PROMPT 02 — IDLE Animation (4 Frames)

### Frame 0: Papada Tremendo
```
Single sprite frame, 64x64 pixel art scale, top-down slight isometric view.
Grotesque short old man in black stained judge robe, standing slightly hunched forward.
ENORMOUS 1970s glasses dominating the face. Triple chin at maximum extension (gravity pulling down).
Cynical smirk. Right hand holds half-eaten greasy pastel. Left hand holds cellphone with green screen.
Money bills poking from left robe pocket. Pastry grease stains on robe (3-4 yellow spots).
Thin grey hair combed to the left side (5-7 strands visible).

Robert Crumb underground comix style, thick irregular outlines, cross-hatching shadows,
dirty saturated palette, paper texture. Transparent background. Pixel art sprite.
```

### Frame 1: Oculos Brilhando
```
Same character as previous frame with TWO differences:
1) Triple chin raised 2 pixels (involuntary jiggle, second layer compressing against first)
2) INTENSE white glint on glasses lenses — asymmetric: left lens has 4x4 circular glare,
right lens has 2x2 smaller glare. Creates "glasses glinting with malice" villain effect.

Same underground comix style. Same pose and outfit. Transparent background. Pixel art sprite 64x64.
```

### Frame 2: Mordendo Pastel
```
Same grotesque old judge character. Right hand raised 6 pixels, bringing pastel to open mouth.
JAW OPEN showing 4-5 yellowish teeth. Triple chin COMPRESSED (three layers squished together
into mass of pink flesh). Crumbs FLYING from mouth (3-4 golden pixels in random directions).
Oil dripping from pastel onto chin (1-2 translucent yellow pixels). Cynical smirk opens into
WIDE momentary grin for the bite. Money bill falling from pocket (body movement dislodged it).
Cellphone still visible in left hand.

Underground comix style, grotesque, thick outlines, cross-hatching. Transparent BG. 64x64 pixel art.
```

### Frame 3: Sorrisinho de Deboche
```
Same character, post-bite. Mouth closed, CHEWING. Triple chin returns to normal position
(3 separate layers, slight residual wobble). Eyes NARROWED behind enormous glasses —
smaller pupils, half-closed eyelids, "I know something you don't" expression. Cynical smirk
returns to right corner of mouth (default position). Single crumb stuck at mouth corner
(1 golden pixel). Glasses glint reduced but present. Posture relaxes 1 pixel backward.

Underground comix style. The expression of absolute smugness. Transparent BG. 64x64 pixel art.
```

---

## PROMPT 03 — WALK Animation (6 Frames)

### Prompt Base (adaptar por frame)
```
Grotesque short old judge walking animation frame. Top-down slight isometric.
Hunched old man shuffle-walk. Black stained robe swinging with each step.
Triple chin BOUNCING with impact (gelatinous physics). Enormous 1970s glasses sliding on nose.
Money bills FALLING from robe pocket with each step (trail of corruption behind him).
Pastel in right hand getting progressively more eaten each frame.
Cellphone in left hand occasionally flashing green (notification from "VORCARO").
Robe shows pastry grease stains. Tiny legs barely visible during walk cycle.

Each step: robe swings opposite to movement, triple chin swings opposite to body (inertia),
glasses slide down on impact then return. Money note detaches from pocket every 2 frames.

Robert Crumb underground comix, thick irregular outlines, cross-hatching, dirty palette.
Transparent background. 64x64 pixel art sprite frame.
```

### Variacao por Frame
```
Frame 0: Right foot forward, body tilting. Robe swings left. Triple chin swings back. Money loosening.
Frame 1: Right foot IMPACT. Body squashes 1px. Triple chin DROPS (slaps chest). Glasses slide down. Money note falls.
Frame 2: Recovery from right step. Triple chin BOUNCES up. Glasses return. Money note floating behind.
Frame 3: Left foot forward (mirror of 0). New grease stain visible on robe right side. Pastel MORE eaten.
Frame 4: Left foot IMPACT (mirror of 1). TWO money notes fall (harder step). Triple chin drops again.
Frame 5: Recovery from left step (mirror of 2). Cellphone screen flashes bright green (Vorcaro notification). Head turns slightly toward phone.
```

---

## PROMPT 04 — ATTACK Animation (3 Frames)

### Frame 0: Arremesso de Pastel (Wind-up)
```
Grotesque old judge in attack pose. Right arm pulled BACK holding oversized greasy pastel
like a grenade. Body rotated 20 degrees right. Cynical smirk opens to WIDE sadistic grin —
all yellowish teeth visible. Glasses FLASH with intense white glint (both lenses).
Triple chin compresses to the right (body pulled that way). Robe stretches with the windup.
Exaggerated baseball pitcher pose from a hunched old man — absurd vigor.
Pastel is DISPROPORTIONALLY LARGE (fills entire hand and more), dripping oil.

Underground comix, grotesque, thick outlines. Transparent BG. 64x64 pixel art.
```

### Frame 1: Toga Reflete (Teflon Flash)
```
Same judge character mid-throw. Right arm at 90-degree angle, pastel LEAVING hand.
Motion blur lines (2 white translucent lines) following pastel trajectory.
SIMULTANEOUSLY: the black robe FLASHES — a wave of light energy runs across the surface
(3-4 white pixels at 40% alpha forming left-to-right wave). This is the "Teflon toga" property —
nothing sticks to him. Triple chin shakes violently with throwing motion. Crumbs EXPLODE
from pastel in semicircle arc (5-6 golden pixels). Grin at MAXIMUM width.

Two visual stories: offensive (pastel projectile) and defensive (Teflon flash). BUSY frame.
Underground comix, thick outlines. Transparent BG. 64x64 pixel art.
```

### Frame 2: Gargalhada Pos-Ataque
```
Post-throw grotesque old judge LAUGHING. Right arm extended (empty hand, pastel is gone).
Body leans forward 2px from throwing momentum. CRITICAL: judge is CACKLING MADLY.
Mouth open 180 degrees (grotesque exaggeration). Triple chin trembling UNCONTROLLABLY
(each of 3 layers vibrating independently at different offsets). Glasses pushed UP nose
by force of laughter (2px above normal). Eyes CLOSED from laughing (inverted arcs).
Impact lines radiating from mouth (3 curved lines, thin, white 30% alpha).
The cynical smirk has become OPEN BELLY LAUGH — chaos-causing joy.

This is the character's ESSENCE: he ENJOYS causing havoc. Underground comix. 64x64 pixel art.
```

---

## PROMPT 05 — DEATH Animation (4 Frames)

### Frame 0: Oculos Deslocam
```
Grotesque old judge taking FATAL hit. Body tilting 10 degrees backward.
FOCUS ON GLASSES: enormous 1970s glasses fly OFF face — 4 pixels away, angled 15 degrees,
as if knocked by impact. Left lens has a crack (1px diagonal line). Triple chin STRETCHES
forward (inertia — body went back but chin continues forward). The cynical smirk REMAINS —
still smirking even when dying. Pastel falls from right hand. Cellphone falls from left hand
(screen still showing "VORCARO"). Slow-motion feel.

Underground comix, grotesque, thick outlines. Transparent BG. 64x64 pixel art.
```

### Frame 1: Papada Murcha
```
Judge falling backward at 30 degrees. Tiny thin legs visible for first time
(grotesquely disproportional to torso). TRIPLE CHIN DEFLATING: 3 layers collapsing
onto each other, losing volume (from full extension to half), like a balloon deflating.
Chin skin turning GREYER (loss of vitality). Glasses now 10px from face, spinning in air
at 45 degrees. Pastel on ground dismantling into separate components (dough, filling, oil).
Habeas corpus DOCUMENTS flying from robe pockets (3-4 yellowish rectangles in random directions).

The deflating chin is the DEATH SIGNAL — equivalent to a light going out.
Underground comix. 64x64 pixel art. Transparent BG.
```

### Frame 2: Toga Vira Pasteis
```
Judge almost on the ground, 60 degrees angle. The black robe TRANSFORMS:
dark fabric fragmenting into golden shapes — PASTÉIS. The robe is literally becoming
a PILE OF PASTÉIS. 40% of the robe already converted (black pixels becoming golden-greasy).
Judge's face visible between the pastéis — and the SMIRK IS STILL THERE.
Dying and still smirking. Glasses on the ground 15px away, cracked but with
one last glint of light (cynical even in death). Cellphone on ground, cracked screen
but still ON — "VORCARO" blinking. Money notes floating EVERYWHERE
(8-10 green pixels, cash rain as pockets disintegrate).

SURREAL metamorphosis. Underground comix. 64x64 pixel art. Transparent BG.
```

### Frame 3: Pilha de Pasteis Final
```
The judge is GONE. In his place: a PILE OF GROTESQUE PASTÉIS
(7-8 overlapping golden greasy pastries, oil pooling underneath).
ON TOP of the pile: THE GLASSES — intact now (cracks gone), with cynical glint
as if he's STILL ALIVE inside, watching, smirking. Next to pile: cellphone showing
"VORCARO — 3 Missed Calls". Money notes scattered around. ONE golden glowing
habeas corpus document floating 2px ABOVE the pile (his spirit trying to free itself —
a habeas corpus for himself). Crumbs forming a circle around everything.

ICONIC death image: pastel pile with glasses. Player sees it and KNOWS: "I killed Gilmar."
Underground comix. 64x64 pixel art. Transparent BG.
```

---

## PROMPT 06 — HIT Animation (2 Frames)

### Frame 0: Oculos Torcem
```
Grotesque old judge taking damage. Micro-recoil of 2px. NOT in pain — in AMUSED INDIGNATION.
As if someone committed a social faux pas. Enormous glasses TWIST — frame bends 10 degrees
(left lens higher than right). Triple chin VIBRATES laterally (3 layers displaced 2px left,
out of sync — gelatin wave effect). Cynical smirk remains with added SURPRISE
(left eyebrow raised 2px). White hit-flash border around character (1px, 30% alpha).
Robe ripples from impact. Pastel in hand squirts oil forward (2 yellow pixels).

NOT pain. INDIGNATION. The hit is a social insult, not a physical attack.
Underground comix. 64x64 pixel art. Transparent BG.
```

### Frame 1: Papada Chacoalha (Recuperacao)
```
Same judge recovering from hit. Body returns to normal position. Glasses returning
(still 3 degrees crooked, correcting). Triple chin PENDULUM SWING to the right
(opposite from Frame 0). Second layer arrives after first, third after second
(cascading wave of chin flesh). Smirk INCREASES — now a challenge smile: "Is that all?"
Glasses return to cynical glint. Hit-flash disappears. Robe settles.
Clear visual message: "That didn't affect me."

FAST recovery. Underground comix. 64x64 pixel art. Transparent BG.
```

---

## PROMPT 07 — SPECIAL: Habeas Corpus Triplo (4 Frames)

### Frame 0: Mao Entra na Toga
```
Grotesque judge reaching RIGHT hand INTO his robe (pulling something from secret pocket).
Arm disappears to the elbow inside the toga. Concentrated cynical expression — eyebrows together,
focused eyes, but smirk MAINTAINED. Glasses emit GOLDEN aura (lens edges glow golden #FFD700).
Triple chin trembles in anticipation. Left hand puts cellphone away in pocket
(needs both hands for the ritual). Mysterious, sinister, comedic.

Underground comix, golden mystical elements. 64x64 pixel art. Transparent BG.
```

### Frame 1: Um Documento
```
Right hand EMERGES from robe holding ONE habeas corpus document.
Document is large (fills hand), aged yellowed paper with illegible text lines
and a GOLDEN seal in corner. GOLDEN AURA: particles (#FFD700, 30% alpha)
float around document. Triple chin STOPS trembling — moment of cynical solemnity.
Glasses emit continuous golden glow. Robe inflates slightly (mystical wind).
The judge holds the document like a priest holds a relic — sacred mockery.

Underground comix, golden mystical light. 64x64 pixel art. Transparent BG.
```

### Frame 2: Tres Documentos (Triplo!)
```
NOW THERE ARE THREE. Judge holds 3 habeas corpus documents fanned like playing cards
in right hand (angles: 0, 15, -15 degrees). Each identical with golden seal.
GOLDEN AURA EXPLODES: particles EVERYWHERE (12-15 golden pixels, varying opacity 20-60%).
ENTIRE BODY glows with golden outline (1px golden border). Expression shifts:
concentration to ABSOLUTE TRIUMPH. Maximum grin. Glasses so bright pupils disappear
(lenses are pure white-gold glare). Triple chin trembles with EXCITEMENT.
Robe vibrates with energy. PEAK POWER frame.

Underground comix, divine mockery, golden explosion. 64x64 pixel art. Transparent BG.
```

### Frame 3: Aura de Invulnerabilidade
```
Three documents MERGE into golden light explosion. Where documents were: sphere of golden
energy (16x16px, center). Judge's body wrapped in INVULNERABILITY AURA: 2px golden outline,
pulsating. Expression: CYNICAL ECSTASY — eyes closed, beatific smile, relaxed triple chin
(he knows nothing can touch him). Robe glows golden instead of black.
Cellphone in pocket shows green flash (Vorcaro sent "congratulations").
This frame marks the START of invulnerable state. Serene yet mocking.

Underground comix, divine golden aura. 64x64 pixel art. Transparent BG.
```

---

## PROMPT 08 — SPECIAL: STF da Pastelaria (6 Frames)

### Frame 0: Invocacao
```
Grotesque judge CLAPPING hands together (pastel and phone put away).
A CRACK appears in the ground in front of him (dark fissure pixels).
Hot oil SMOKE rises from the crack (yellow-amber translucent cloud).
Expression of GENUINE HAPPINESS — the only time cynicism gives way to REAL JOY.
Glasses reflect oily sheen (yellow tint instead of white). Triple chin trembles
with gastronomic anticipation. He's summoning something sacred.

Underground comix, food magic ritual. 64x64 pixel art. Transparent BG.
```

### Frame 1: Balcao Aparece
```
A PASTRY STAND has sprouted from the ground. Cheap wood counter, dented aluminum surface.
Height: covers lower third of frame. On the counter: 3 pastéis in a row (golden, greasy),
a pot of hot sauce (dark red), and a makeshift fryer BUBBLING (oil pixels jumping).
The judge stands BEHIND the counter like a professional pastry chef.
His robe now looks like an apron (grease stain dominates the front).
Proud smile. Glasses steam from fryer heat.

Underground comix, grotesque food stand. 64x64 pixel art. Transparent BG.
```

### Frame 2: Pegando Pastel
```
Judge grabs first pastel from counter with right hand. The pastel is ENORMOUS in his hand
(disproportional). Oil drips from it (yellow drops falling). Fryer bubbles more intensely
(oil pixels jump 4px). Steam rises thicker. Other 2 pastéis on counter TREMBLE
(as if alive). Sauce pot overflows slightly. Judge's triple chin is SALIVATING
(1px of shine on lowest chin layer). Hungry, greedy, ecstatic.

Underground comix, grotesque food. 64x64 pixel art. Transparent BG.
```

### Frame 3: Mordida Extase
```
Judge BITES the pastel with disproportionate ferocity. Mouth open 150 degrees.
Teeth sink into pastry. Filling EXPLODES (brown pixels flying all directions).
Oil SQUIRTS from pastel (yellow pixels in arc). Crumbs form CLOUD around head
(8-10 golden pixels). Triple chin VIBRATES with bite (wave from top to bottom layer).
Glasses FOG UP from hot pastel steam (lenses become semi-opaque).
GOLDEN INVULNERABILITY BORDER pulses around character — nothing matters when eating pastel.
Pure grotesque ecstasy.

Underground comix, food ecstasy grotesque. 64x64 pixel art. Transparent BG.
```

### Frame 4: Oleo Espirra (AoE)
```
The fryer OVERFLOWS. Hot oil SPLASHES in ALL directions (8-10 amber pixels radiating
from counter center to frame edges). This is the AREA OF EFFECT visual.
Judge continues chewing (mouth closed, cheeks INFLATED), completely INDIFFERENT
to the oil chaos. Pastéis on counter fry uncontrollably. Dense steam rises.
Glasses clearing (lenses brightening). New oil stains on triple chin.
Chaos everywhere but the judge is at PEACE — eating is all that matters.

Underground comix, explosive food chaos. 64x64 pixel art. Transparent BG.
```

### Frame 5: Satisfacao Final
```
Pastry stand SINKING into ground (descending 4px, disappearing). Judge does a visual BURP:
mouth in O shape, triple chin momentarily inflating, surprised eyes from the force.
In hand: only the crumpled greasy wrapper (no more pastel). Glasses return to normal glint.
Invulnerability aura dissipating (golden border flickering). Crumbs EVERYWHERE.
Cynical smirk returns — moment of happiness is over, back to scheming.
Wipes mouth on robe (new stain). The counter vanishes. Back to business.

Underground comix, post-feast satisfaction. 64x64 pixel art. Transparent BG.
```

---

## PROMPT 09 — SPECIAL: Briga com Barroso (8 Frames)

### Frame 0-1: Deteccao e Confronto
```
Frame 0: Grotesque old judge FREEZES mid-action. Head turns 30 degrees toward an off-screen target.
Glasses flash RED (rage, not cynicism — red glint #CC3030). Triple chin STIFFENS (muscles tense).
Smirk changes to COMBAT GRIN — teeth clenched, mouth corners up. Drops everything
(pastel and phone falling). Robe inflates with anger.

Frame 1: Full body rotation, FACING target. Posture TRANSFORMS: hunched old man becomes
CONFRONTATIONAL BULL. Shoulders raise 3px. Chest inflates. Triple chin displayed as THREAT.
Both fists clenched. Thin hair strands BRISTLE (each strand 1px higher, standing up).
Veins appear on neck (2-3 red lines). The tiny old man suddenly looks DANGEROUS.

Underground comix, confrontation pose. 64x64 pixel art. Transparent BG.
```

### Frame 2-4: "VAGABUNDO!" x3 (Escalacao)
```
THREE frames showing ESCALATING SCREAM. Each frame MORE intense than the last.

Frame 2: Mouth WIDE OPEN. Triple chin INFLATES with the scream. Sound impact lines radiate
from mouth (4 curved lines). Single "!" above head in red. Saliva spray (2 pixels). Body leans forward.

Frame 3: Mouth 2px WIDER. Triple chin 1px MORE inflated. Impact lines 2px LONGER.
"!!" above head. Veins on neck 1px THICKER. Saliva spray (3 pixels). ESCALATING.

Frame 4: MAXIMUM of everything. Mouth impossibly wide (22px — anatomically impossible grotesque).
Triple chin looks about to BURST. Impact lines reach FRAME EDGE. "!!!" above head, PULSING.
Glasses nearly falling off (3px displaced). Veins PULSING (2px thick). Saliva MAXIMUM (5 pixels).
THE MOST GROTESQUE FRAME IN THE ENTIRE SHEET. Peak Andre Guedes energy.

Underground comix, screaming escalation. 64x64 pixel art. Transparent BG.
```

### Frame 5-6: Empurrao
```
Frame 5: Judge CHARGES forward (4px aggressive step). Both hands extended in shoving position.
Mouth closes but combat grin stays. Triple chin swings forward with momentum (3px bounce).
Glasses crooked but he doesn't care. Robe billows behind. Dust from feet. The old man is a BULL.

Frame 6: Hands make CONTACT (implied — squashing against surface). Body COMPRESSES 2px (squash).
Triple chin SLAPS AGAINST CHEST from sudden deceleration. Glasses jump 2px up.
Shockwave emanates from contact point (2-3 semicircular impact lines). Combat grin becomes
SATISFACTION LAUGH. Residual pastry crumbs fly from body on impact.

Underground comix, physical confrontation. 64x64 pixel art. Transparent BG.
```

### Frame 7: Pose de Vitoria
```
Judge steps back 2px post-shove. WINNER POSE: chest puffed, chin raised, triple chin displayed
like a trophy. Cynical smirk back at AMPLIFIED level — the grin of someone who WON the fight
(even if he didn't). Glasses back in place with MAXIMUM white cynical glint. Hands on hips
(power pose). Robe settles with false dignity (still stained, but worn as victory mantle).
Hair smoothed back to combed position. Picks up cellphone from ground (first priority).
Expression says: "I always win. Always win. Always win."

Underground comix, victory pose. 64x64 pixel art. Transparent BG.
```

---

## PROMPT 10 — PROJETEIS (32x32px)

### Pastel Projetil
```
Single flying pastel (Brazilian fried pastry), 32x32 pixel art. Top-down slight isometric view.
Golden-greasy oversized pastel, semi-circular shape. Oil DRIPPING from bottom (2-3 amber drops).
Brown filling visible at the bitten open end. Motion lines trailing behind (2 white translucent).
Crumbs falling. Steam rising. GROTESQUE — not appetizing, REPULSIVE yet recognizable.
Thick irregular outlines. Dirty golden color. Underground comix style. Transparent BG.
```

### Documento Habeas Corpus
```
Glowing habeas corpus document, 32x32 pixel art. Aged yellowed parchment paper,
rolled or flat. Illegible cursive text lines. Large GOLDEN seal/stamp in corner.
GOLDEN AURA radiating (4-6 golden particles around it). Slight glow effect.
Feels bureaucratic yet mystical — a cursed legal document.
Thick outlines. Underground comix style. Transparent BG.
```

### Nota de Dinheiro (Chuva do Vorcaro)
```
Brazilian money bill, 32x32 pixel art (or smaller, 16x16 for particle).
Green bill with illegible face print. Fluttering/floating appearance (slight curve).
One corner slightly folded. Feels DIRTY — not clean money, corrupt money.
Faint golden aura (corruption glow). Underground comix style. Transparent BG.
```

### Oleo Quente (AoE da Pastelaria)
```
Splash of hot frying oil, 32x32 pixel art. Amber-golden liquid in explosive splash shape.
Multiple droplets radiating outward. Steam/smoke particles rising (white translucent).
Sizzle effect (small white sparks). Feels HOT and DANGEROUS. Greasy, viscous.
Underground comix style. Transparent BG.
```

---

## PROMPT 11 — EFEITOS VISUAIS

### Aura Dourada (Habeas Corpus Invulnerabilidade)
```
Golden invulnerability aura effect, pixel art. Pulsating golden border/outline that wraps
around a character silhouette. Particles of golden light floating upward within the aura.
Two states for animation: bright (#FFD700) and dim (#C8A832) alternating.
Feels divine yet MOCKINGLY so — fake holiness, bureaucratic divinity.
Can be overlaid on any character sprite. Transparent BG. Underground comix golden glow.
```

### Flash Teflon (Toga refletindo)
```
Teflon reflection flash effect, pixel art. A wave of white light (40% alpha) sweeping
across a dark surface left to right. Suggests projectiles BOUNCING OFF.
Small spark at the point of deflection. Brief and sharp — 2-frame effect max.
Feels slippery, teflon-coated, untouchable. Transparent BG.
```

### Onomatopeia "VAGABUNDO!"
```
Comic book speech onomatopoeia "VAGABUNDO!" in pixel art style. Bold, jagged letters,
RED (#CC3030) with dark outline (#1A1A18, 2px). Slightly tilted for aggression.
Impact lines radiating behind the text. Exclamation marks. Hand-lettered look,
NOT typeset — each letter slightly different size and baseline.
Needs 3 variants: one "!", two "!!", three "!!!" for the escalation mechanic.
Transparent BG. Underground comix lettering style.
```

---

## PROMPT 12 — SKINS (Variantes de Prompt — modificar o PROMPT 01)

### Skin: Vorcaro VIP
```
Same grotesque judge character BUT:
- Robe is now GOLDEN instead of black (corrupt luxury, #C8A832 base with #FFD700 highlights)
- Cellphone GLOWING intensely (screen bright, "VORCARO VIP" visible)
- Money bills actively FALLING from ALL pockets (not just poking out)
- Glasses have DIAMOND-ENCRUSTED frames (sparkle pixels on frames)
- Golden rings on fingers (3-4 gold pixel dots on hands)
- Pastel replaced with CHAMPAGNE GLASS (golden flute, #C8A832)
- Robe has a subtle dollar-sign pattern embroidered
- Aura of corrupt wealth — everything golden and gaudy

Underground comix, corrupt luxury grotesque. 64x64 pixel art. Transparent BG.
```

### Skin: Pasteleiro
```
Same grotesque judge character BUT:
- APRON worn OVER the robe — white apron (#E8E0D0) covered in massive grease stains
- Chef hat (toque) sitting crooked on top of thin combed hair
- Both hands hold pastéis (one in each hand, no cellphone)
- Apron pocket has "STF PASTELARIA" written in crude letters
- Oil stains are MORE PROMINENT — apron is 60% stain, 40% white
- A SPATULA tucked in the apron pocket
- Flour/crumbs dust on the glasses lenses
- Expression: PROUD pastry chef — cynicism replaced with culinary pride
- Tiny legs wearing kitchen clogs instead of hidden under robe

Underground comix, grotesque chef. 64x64 pixel art. Transparent BG.
```

### Skin: Carnaval
```
Same grotesque judge character BUT:
- Robe covered in CONFETTI (multicolored pixels scattered across the black)
- SERPENTINE ribbons wrapped around the robe (curling colored strips)
- Triple chin PAINTED — each layer a different color (green, yellow, blue — Brazilian flag parody)
- Glasses frames wrapped in GLITTER (sparkle pixels on the brown frames)
- Small carnival crown/tiara sitting crooked on thin hair
- Pastel replaced with COXINHA (Brazilian carnival snack, teardrop-shaped)
- Money bills in pocket replaced with PARTY FAVORS (noisemakers, etc.)
- Expression: FESTIVE DEBOCHE — cynical smirk with added party energy
- Confetti particles floating around the character (4-5 colored pixels in air)
- Thin hair has a small feather attached (single colorful feather, 3px)

Underground comix, carnival grotesque. 64x64 pixel art. Transparent BG.
```

---

## Notas para Geracao de Imagem

1. **SEMPRE gerar em resolucao alta primeiro** (512x512 ou maior) e depois reduzir pra 64x64
2. **Pos-processamento OBRIGATORIO**: adicionar textura de papel (noise 3-5%), engrossar contornos, sujar cores
3. **Testar em fundo escuro E claro** — o alpha channel deve funcionar em ambos
4. **Consistencia entre frames e CRITICA** — o personagem deve ser reconhecivel em TODOS os frames
5. **Se a imagem gerada parecer "bonita" ou "limpa", REFAZER** — o estilo exige sujeira e grotesco
6. **A papada tripla deve ser visivel em TODOS os angulos** — e a marca registrada anatomica
7. **Os oculos enormes devem dominar o rosto em TODOS os frames** — sem oculos, nao e Gilmar
8. **O sorrisinho cinico NUNCA desaparece** — nem no hit, nem na death (morre rindo)
9. **Prompts podem ser combinados com LoRA/checkpoints de pixel art** para melhores resultados
10. **Para Midjourney, adicionar**: `--no realistic, photographic, smooth, clean, modern`
