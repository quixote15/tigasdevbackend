# BOLSONARO (O Mito) -- Sprite Specification

## Overview
- **Character Type:** Boss Principal (Lado Direito)
- **Sprite Dimensions:** 64x64px per frame
- **Atlas Max Size:** 2048x2048px
- **Format:** PNG with alpha transparency
- **Perspective:** Top-down slightly isometric (Y-sorting)
- **Style:** Andre Guedes grotesque -- thick irregular outlines, exaggerated deformities, dirty saturated colors
- **Anchor Point:** Bottom-center (32, 60) -- feet position for Y-sorting

---

## Versao Humana vs Versao Zumbi

Todo personagem jogavel em **Zumbis de Brasilia** possui DOIS conjuntos completos de sprites: a versao **humana** e a versao **zumbi**. O jogador comeca como humano e, ao receber uma mordida zumbi (Mordida Zumbi), passa por uma transformacao irreversivel para a forma zumbi.

### Estrutura de Pastas
```
Bolsonaro/
├── sprites/
│   ├── humano/           # Sprite sets da forma humana
│   │   ├── bolsonaro-humano-idle.png
│   │   ├── bolsonaro-humano-walk.png
│   │   ├── bolsonaro-humano-attack.png
│   │   ├── bolsonaro-humano-death.png
│   │   ├── bolsonaro-humano-hit.png
│   │   └── bolsonaro-humano-transformacao.png
│   └── zumbi/            # Sprite sets da forma zumbi (versao atual/default)
│       ├── bolsonaro-idle.png
│       ├── bolsonaro-walk.png
│       ├── bolsonaro-attack.png
│       ├── bolsonaro-death.png
│       ├── bolsonaro-hit.png
│       └── [todas as special/ultimate sheets]
```

### Versao Humana -- Bolsonaro
- **Corpo:** Magricela com ponchete de cerveja (barriga de cerveja proeminente num corpo fino) -- NAO e a versao barril/barrel-chest do zumbi. Ombros estreitos, bracos finos, mas a barriga transborda da camisa. A cicatriz da facada fica mais visivel nessa versao porque a pele esta esticada sobre a barriga.
- **Arma:** AK-47 (substitui o revolver dourado). O fuzil e grande demais para o corpo magricela -- parece uma crianca segurando a arma do pai. A AK-47 tem uma taxa de **40% de brocha** (travamento/falha) ao disparar -- pior que os 30% do revolver dourado.
- **Pele:** Tons naturais de pele humana (sem esverdeamento). Pele bronzeada de quem fica no sol da Esplanada, com vermelhidao no pescoco e bracos.
- **Personalidade:** Mais covarde como humano. Idle com movimentos nervosos, olhando para os lados com medo. O queixao e o mesmo, mas a expressao e de panico, nao de bravata.
- **Velocidade:** 100% base (80 px/s) -- antes da mordida.

### Versao Zumbi -- Bolsonaro (Versao Atual/Default)
- **Corpo:** Peito de barril, ombros largos, postura de bravata. O torso e mais largo, mais grotesco, inflado pela zumbificacao.
- **Arma:** Revolver dourado de cowboy com adesivo da bandeira do Brasil. Taxa de brocha de 30%.
- **Pele:** Esverdeada (#7D8A6A base), em decomposicao. Olhos brilham com um verde doentio.
- **Personalidade:** Mais corajoso, mas cerebro de zumbi. Strut arrogante, bravata constante, o sorriso forcado agora e um rigor mortis permanente.
- **Velocidade:** 60% da base (48 px/s) -- penalidade de -40% pos-mordida.

### Animacao de Transformacao (Humano → Zumbi)
- **Duracao:** 3000ms (3 segundos)
- **Frames:** 8 frames de morphing progressivo
- **Sprite Sheet:** `bolsonaro-humano-transformacao.png` -- 512x64px (8 frames x 64px)
- **Sequencia:**
  1. Mordida recebida -- flash vermelho, personagem cai de joelhos
  2. Pele comeca a esverdeear (transicao gradual dos hex de pele humana para pele zumbi)
  3. Roupas comecam a rasgar (camisa estoura nos ombros enquanto o torso infla)
  4. AK-47 cai no chao, revolver dourado materializa na mao (particulas douradas)
  5. Queixo CRESCE ainda mais (impossivel, mas acontece -- +3px de extensao)
  6. Olhos mudam de cor para verde brilhante (#44FF44, 60% opacity glow)
  7. Sorriso forcado congela em rigor mortis permanente
  8. Postura muda de covarde/curvada para bravata/peito estufado
- **Penalidade permanente:** -40% velocidade de movimento (80 px/s → 48 px/s)
- **Habilidades ganhas:** Ataque corpo-a-corpo com garras, propagacao de infeccao por mordida

---

## Color Palette

| Element                    | Hex Code  | Usage                                      |
|----------------------------|-----------|--------------------------------------------|
| Skin Base                  | `#D4A574` | Face, arms, hands                          |
| Skin Shadow                | `#B8834A` | Under-chin shadow, arm creases             |
| Skin Highlight             | `#E8C49A` | Forehead, nose tip, chin point             |
| Chin Special               | `#C4915C` | Exaggerated chin area (4x oversized)       |
| Hair Dark                  | `#2C1810` | Slicked-back hair                          |
| Hair Highlight             | `#4A2E1C` | Hair sheen                                 |
| Sash Green                 | `#006400` | Faixa presidencial -- verde                |
| Sash Yellow                | `#FFD700` | Faixa presidencial -- amarelo              |
| Jersey Yellow              | `#FFD700` | Camisa selecao -- base                     |
| Jersey Yellow Dirty        | `#CCAA00` | Camisa selecao -- shadows/grime            |
| Jersey Green Trim          | `#006400` | Collar, sleeve trim                        |
| Prison Orange              | `#FF6600` | Uniforme presidiario -- base               |
| Prison Orange Dark         | `#CC5500` | Uniforme presidiario -- shadows            |
| Prison Orange Light        | `#FF8833` | Uniforme presidiario -- highlights         |
| Pants Dark                 | `#1A1A2E` | Terno escuro pants                         |
| Shoe Black                 | `#0D0D0D` | Sapatos                                    |
| Gun Gold                   | `#DAA520` | Revolver dourado                           |
| Gun Gold Light             | `#F0C040` | Revolver highlight                         |
| Gun Gold Dark              | `#8B6914` | Revolver shadow                            |
| Brazil Flag Sticker        | `#009B3A` | Adesivo bandeira no revolver (verde)       |
| Scar Pink                  | `#D35D6E` | Cicatriz da facada (abdomen)               |
| Scar Dark                  | `#A0323F` | Cicatriz deeper tone                       |
| Sunglasses Lens            | `#1A1A1A` | Oculos escuros                             |
| Sunglasses Frame           | `#333333` | Armacao oculos                             |
| Phone Screen               | `#4488FF` | Celular -- tela acesa (live)               |
| Outline Main               | `#0A0A0A` | Thick 2-3px irregular outlines             |
| Outline Rage               | `#1A0000` | Reddish-black for angry frames             |
| Teeth White                | `#F5F5DC` | Dentes grandes (sorriso forcado)           |
| Teeth Shadow               | `#C8C8A0` | Dentes shadow                              |
| Eyebrow Black              | `#0D0806` | Sobrancelhas grossas                       |
| Bar Gray                   | `#808080` | Grades da cela (2026 skin)                 |
| Bar Gray Dark              | `#505050` | Grades shadow                              |
| Moto Chrome                | `#C0C0C0` | Harley dourada -- metal parts              |
| Moto Gold                  | `#DAA520` | Harley dourada -- paint                    |
| Belly Flesh                | `#D4A070` | Barriga exposta com cicatriz               |
| Blood Red                  | `#8B0000` | Blood particles, scar emphasis             |
| Ghost Green                | `#44FF44` | Motos fantasma (ultimate), 60% opacity     |

### Paleta Exclusiva -- Versao Humana

| Element                    | Hex Code  | Usage                                      |
|----------------------------|-----------|--------------------------------------------|
| AK-47 Metal Dark           | `#2A2A2A` | Corpo do fuzil, cano, receptor              |
| AK-47 Metal Light          | `#4A4A4A` | Highlights metalicos, gatilho, mira         |
| AK-47 Wood Stock           | `#5C3A1E` | Coronha de madeira, punho (base)            |
| AK-47 Wood Light           | `#7A5232` | Coronha highlights, detalhe do grain        |
| AK-47 Muzzle Flash         | `#FF8800` | Flash do tiro da AK-47 (mais alaranjado que o dourado do revolver) |
| AK-47 Jam Smoke            | `#AAAAAA` | Fumaca do travamento/brocha (40% opacity)   |
| Human Skin Base            | `#D4A574` | Pele humana -- rosto, bracos, maos          |
| Human Skin Shadow          | `#B8834A` | Sombras da pele humana -- sob queixo, dobras |
| Human Skin Highlight       | `#E8C49A` | Highlights da pele humana -- testa, nariz, ponta do queixo |

---

## Character Proportions (64x64 frame)

```
    [Sunglasses on top: 4px]
    [Hair: 6px slicked back]
    [Head: 18px tall x 16px wide -- grotesquely large]
      - Forehead: 4px (small)
      - Eyes: 3px row (wide-set, squinting)
      - Eyebrows: 4px thick, bushy, angry
      - Nose: 3px (small, crushed)
      - Mouth: 4px (forced grin, big teeth visible)
      - CHIN: 8px tall (4x normal) -- THE defining feature
    [Neck: 2px (barely visible, chin covers it)]
    [Torso: 16px -- wide barrel chest, pot belly]
      - Faixa presidencial diagonal: 3px wide stripe
      - Belly: visibly protruding 4px past torso edge
      - Cicatriz: 6px vertical scar on belly, jagged line
    [Arms: 12px each side, one holds revolver]
    [Legs: 12px -- stocky, bow-legged]
    [Feet: 4px -- tiny compared to body]
```

**Key Deformity Rules:**
- Chin MUST be at minimum 4x the size of a normal chin -- it juts out absurdly
- Belly MUST protrude with a clearly visible knife scar (jagged vertical line, pink/red)
- Eyebrows MUST be absurdly thick -- 4px minimum, unibrow tendency
- Smile MUST look forced/unnatural -- too wide, too many teeth, eyes not smiling
- Gun MUST be comically oversized cowboy revolver with visible Brazil flag sticker
- Sunglasses ALWAYS perched on top of head, never covering eyes

---

## Animation: IDLE (4 frames)
**Sprite Sheet:** `bolsonaro-idle.png` -- 256x64px (4 frames x 64px)
**Frame Rate:** 8 fps
**Loop:** Yes, ping-pong (1-2-3-4-3-2)

### Frame 0: Idle Base -- "Talkei Stance"
- **Position:** 0,0 to 63,63
- **Description:** Bolsonaro standing in signature wide stance, chest puffed out, chin jutting forward aggressively. Right hand holds the golden revolver loosely at hip level, barrel pointing slightly upward. Left hand hangs at side with thumb-up gesture (signature "talkei" pose). Forced grin with large teeth visible. Eyebrows thick and slightly raised. Sunglasses perched on hair. Faixa presidencial draped diagonally across torso. Belly protrudes with visible scar. Feet planted wide apart, bow-legged.
- **Style Notes:** Outlines 2-3px thick, irregular. Colors dirty/saturated. The grin must look UNSETTLING -- too wide, muscles straining. Chin dominates lower face. Tiny sweat drop (2px) near temple.

### Frame 1: Idle Shift -- "Chin Jut"
- **Position:** 64,0 to 127,63
- **Description:** Chin pushes forward 2px more. Chest inflates (torso widens 1px each side). Revolver hand twitches upward 1px as if about to draw. The forced grin intensifies -- one more tooth visible. A subtle nostril flare (1px darker shade on nose). Left hand thumb-up gesture more emphatic. Weight shifts to right foot (left foot lifts 1px).
- **Style Notes:** Subtle breathing/bravado animation. The chin forward motion should feel like a rooster puffing up.

### Frame 2: Idle Shift -- "Belly Breath"
- **Position:** 128,0 to 191,63
- **Description:** Belly inflates outward 2px (breathing). Scar stretches slightly (scar pixels spread 1px). Chin returns to base position. Eyes narrow 1px (squinting at imagined enemies). Revolver drops back to hip level. Shoulders rise 1px (tension). Hair shows a single strand falling forward (1px line). Sunglasses slide 1px forward on head.
- **Style Notes:** The belly inflation should be grotesque -- flesh visibly distending, scar pulling apart.

### Frame 3: Idle Shift -- "Restless Gunhand"
- **Position:** 192,0 to 255,63
- **Description:** Gun hand lifts revolver 3px upward, finger twitching near trigger. Head turns 2px to the side (paranoid glance). Chin wobbles (1px jiggle line underneath). Forced grin flickers -- mouth opens 1px more (showing upper AND lower teeth). Left hand curls into partial fist. Belly deflates back to normal. One eye wider than the other (asymmetric paranoia). Small vein visible on temple (1px red line).
- **Style Notes:** This frame should convey restless aggression. The asymmetric eyes are critical -- one wide/paranoid, one squinting/angry. Gun finger twitch is key personality detail.

---

## Animation: WALK (6 frames)
**Sprite Sheet:** `bolsonaro-walk.png` -- 384x64px (6 frames x 64px)
**Frame Rate:** 10 fps
**Loop:** Yes, cyclic (1-2-3-4-5-6-1)

### Frame 0: Walk -- Right Step Forward
- **Position:** 0,0 to 63,63
- **Description:** Right leg extends forward 4px, left leg back 3px. Arms swing opposite to legs (right arm with gun swings back, left arm forward). Torso tilts forward 2px (aggressive march posture). Chin leads the way -- juts out 3px past body center. Faixa flutters 1px behind. Belly bounces slightly upward. Forced grin maintained. Dust cloud (2x2px, tan) at back foot.
- **Style Notes:** Walk must be a STRUT -- arrogant, chest-first, chin-first. Not a shamble. This is a man who thinks he owns the place.

### Frame 1: Walk -- Right Foot Down
- **Position:** 64,0 to 127,63
- **Description:** Right foot plants. Impact squash (body compresses 1px vertically). Belly jiggles downward 1px from impact. Gun arm at mid-swing. Chin wobbles on impact (1px bounce). Teeth clench slightly (grin tightens). Scar on belly shifts with skin. Dust puff at right foot (3x3px, dissipating).
- **Style Notes:** The impact should feel HEAVY -- this is a stocky, solid man.

### Frame 2: Walk -- Mid-stride (passing)
- **Position:** 128,0 to 191,63
- **Description:** Legs cross center. Body at maximum height (stretches 1px vertically). Both feet briefly close together. Arms at sides. Chin at maximum forward extension. Belly swings slightly left (momentum). Revolver catches a glint (1px white highlight). Sunglasses bounce on head (1px upward from base). Eyes scan ahead.
- **Style Notes:** Moment of peak height in the walk cycle. Brief moment of "composed" before next heavy step.

### Frame 3: Walk -- Left Step Forward
- **Position:** 192,0 to 255,63
- **Description:** Mirror of Frame 0 but left leg forward. Left arm (no gun) swings back. Right arm with gun swings forward -- gun barrel visible pointing ahead menacingly. Torso tilts forward. Faixa flutters opposite direction. Belly bounces. Small sweat drop detaches from forehead (1px, arcing trajectory).
- **Style Notes:** The gun casually pointing forward during walk is intentional -- always armed, always threatening, even casually.

### Frame 4: Walk -- Left Foot Down
- **Position:** 256,0 to 319,63
- **Description:** Mirror of Frame 1 for left foot impact. Belly jiggles right. Chin wobbles left. Gun arm reaches maximum forward position. Dust at left foot. Scar stretches. Eyes briefly wider (step impact). Faixa settles momentarily.
- **Style Notes:** Same heavy impact as Frame 1, mirrored.

### Frame 5: Walk -- Mid-stride Return
- **Position:** 320,0 to 383,63
- **Description:** Mirror of Frame 2. Legs cross center returning. Body stretches upward. Arms returning to neutral. Chin forward. A 1px motion line trails behind the chin (speed indicator for this absurdly prominent feature). Belly centered. Quick tongue lick of lips (1px pink on lower lip edge).
- **Style Notes:** The tongue lick is a subtle grotesque touch -- nervous/predatory habit.

---

## Animation: ATTACK (3 frames) -- "Arma que Brocha"
**Sprite Sheet:** `bolsonaro-attack.png` -- 192x64px (3 frames x 64px)
**Frame Rate:** 10 fps
**Loop:** No (play once per attack)

### Frame 0: Attack -- Draw / Aim
- **Position:** 0,0 to 63,63
- **Description:** Right arm whips upward, revolver raised to shoulder height. Left hand comes up to support the gun (cowboy two-handed aim). Chin thrusts forward. Eyes narrow to slits (aiming squint). Forced grin becomes a snarl -- upper lip curls, teeth bared aggressively. Body leans back slightly (recoil anticipation). Belly exposes more scar (shirt rides up 2px). Legs spread wider for stability. 2px motion blur on gun arm.
- **Style Notes:** The aim must look like a Hollywood cowboy -- except grotesque. Gun absurdly large, aim probably not straight. The snarl is key -- this is ANGRY shooting.

### Frame 1: Attack -- Fire (SUCCESS: 70% chance)
- **Position:** 64,0 to 127,63
- **Description:** MUZZLE FLASH: 8x8px starburst of yellow (#FFD700) and orange (#FF6600) from gun barrel. Recoil pushes body back 3px. Gun kicks upward 4px. Head jerks back (chin points skyward momentarily). Eyes go wide (recoil surprise). Mouth opens in a yell. Smoke wisps (3-4 small gray pixels, 50% opacity) around barrel. Faixa flies backward. Belly jiggles from recoil. Spent casing (2x2px gold pixel) ejects to the right. The whole body vibrates (1px left-right offset).
- **Style Notes:** MAXIMUM violence energy. The muzzle flash should be oversized and garish. Casing ejection is a fun detail. Body vibration conveys the "barely in control" feel.

### Frame 2: Attack -- Fire (FAIL: 30% chance) / "Brocha"
- **Position:** 128,0 to 191,63
- **Description:** Gun clicks with NO flash. A tiny "pfft" cloud (4x4px, light gray, comical) exits barrel. The revolver droops downward (barrel sags 3px as if the gun itself is embarrassed). Body posture collapses -- shoulders slump, chin drops, eyes go wide with SHOCK and EMBARRASSMENT. Mouth opens in an "O" of dismay. A small "?" appears above head (4px, yellow). Left hand releases gun support and covers face. Self-damage indicated by red flash (2px red overlay on face/body, 30% opacity). Small crack lines appear on the gun (1px dark lines). The word "TALKEI?" could float in small text near the gun (optional in-game overlay).
- **Style Notes:** This frame is COMEDY GOLD. The gun LITERALLY droops like... you get it. The embarrassment must be PALPABLE. Eyes wide, mouth agape. The contrast between Frame 1 (action hero) and Frame 2 (humiliation) is the entire joke.

---

## Animation: DEATH (4 frames)
**Sprite Sheet:** `bolsonaro-death.png` -- 256x64px (4 frames x 64px)
**Frame Rate:** 8 fps
**Loop:** No (play once, hold last frame)

### Frame 0: Death -- Impact Hit
- **Position:** 0,0 to 63,63
- **Description:** Full body recoil. Head snaps back (chin points straight up). Arms fly outward -- revolver slips from right hand (gun now 4px away from hand, tumbling). Sunglasses fly off head (2px above, spinning). Eyes bulge out (2px larger than normal). Mouth opens in a scream. Faixa unravels 3px. Belly scar glows red (1px red highlight on scar). Feet lift off ground 2px (knocked into air). Blood particles (3-4 red 2x2px dots) spray from chest. Phone falls from pocket (2x3px rectangle, screen lit).
- **Style Notes:** Maximum drama. Every accessory flying off. The chin pointing straight up should be ABSURD -- like a cartoonish jaw unhinged by the impact.

### Frame 1: Death -- Falling
- **Position:** 64,0 to 127,63
- **Description:** Body tilting backward at 30 degrees. Revolver further away (8px from hand, spinning in air). Sunglasses at frame top edge. Arms flailing (left arm up, right arm reaching for gun). Chin still pointing up. Mouth forms the word "TALKEI?" (rictus shape). One shoe comes off (4px away from foot). Belly exposed fully, scar pulsing (alternating pink/red). Faixa streaming behind like a flag. Gravity pulling hair down. Phone screen shows a paused live stream interface. Motion lines (2px white, 40% opacity) trail behind the body.
- **Style Notes:** The reaching for the gun while falling is essential character -- even dying, he wants the weapon. Shoe flying off is classic Andre Guedes absurdism.

### Frame 2: Death -- Floor Impact
- **Position:** 128,0 to 191,63
- **Description:** Body hits ground at 80 degrees from vertical. SQUASH frame (body compresses 4px vertically, widens 3px). Massive dust cloud (8x6px tan/brown cloud) at impact point. Revolver bounces off ground (now above the body, still spinning). Sunglasses shatter (3 small fragments, 1x1px each). Chin hits ground first (flattens comically -- 2px wider). Belly impacts with a visible wobble ripple (concentric 1px lines). Faixa draped over face. Blood pool starts forming (2x1px red under body). Phone cracks on ground (screen goes to static pattern). Stars orbit head (3 yellow 2x2px stars in circle, classic cartoon KO).
- **Style Notes:** The chin hitting first is THE JOKE. His most prominent feature is his undoing. The wobble ripple on the belly is grotesque perfection.

### Frame 3: Death -- Final / Defeated
- **Position:** 192,0 to 255,63
- **Description:** Body flat on ground, fully horizontal. Revolver lies 8px away, barrel drooping (brochavel even in death). Sunglasses fragments scattered. Eyes replaced by X marks (classic cartoon death). Chin rests on ground, taking up a disproportionate amount of space. Tongue hangs out 2px to the side. Faixa crumpled and dirty. Belly scar visible and faded. One shoe off, one shoe on. Blood pool at 4x4px. Phone beside body showing "LIVE ENDED" on cracked screen. Dust settling (2-3 small particles). The forced grin is GONE -- replaced by a slack-jawed grimace. Stars still orbiting but slowing down.
- **Style Notes:** Pathetic. Defeated. Deflated. Every symbol of his power (gun, faixa, sunglasses, phone) broken and scattered. The drooping gun barrel in death echoes the "brocha" theme. The "LIVE ENDED" on the phone is a dark comedy touch.

---

## Animation: HIT (2 frames)
**Sprite Sheet:** `bolsonaro-hit.png` -- 128x64px (2 frames x 64px)
**Frame Rate:** 12 fps
**Loop:** No (play once, return to idle)

### Frame 0: Hit -- Impact Flash
- **Position:** 0,0 to 63,63
- **Description:** White flash overlay (full body, 40% opacity white). Body jerks right 3px from impact. Chin compresses into neck (for once, the chin retreats). Eyes go WIDE and ROUND (shock). Mouth opens revealing ALL teeth (pain grimace, not grin). Gun hand spasms (revolver points skyward). Left arm clutches stomach instinctively (protecting scar area). Belly recoils inward 2px. Faixa whips to the side. Red damage numbers placeholder space above head. Hair disheveled (2px strands out of place). Sweat drops (2x 1px drops) fly off forehead.
- **Style Notes:** The chin retreating into the neck is an INVERSION of his normal posture -- pain literally pushes his defining feature inward. Critical visual joke.

### Frame 1: Hit -- Recovery Anger
- **Position:** 64,0 to 127,63
- **Description:** Body snaps back to center. Face contorted in RAGE -- eyebrows form a V (angry), eyes bloodshot (1px red veins), nostrils flared, teeth clenched in fury snarl. Chin THRUSTS out further than normal (+2px past idle position, overcompensating). Revolver arm pulls gun into aggressive ready position. Left hand makes fist. Belly puffs out (angry inflation). Scar glows slightly (1px pink highlight). Veins visible on forehead and neck (2-3 1px lines). Faixa still swinging from impact. Red aura (1px red outline around body, 20% opacity) indicating rage state.
- **Style Notes:** The overcompensation is key. He got hurt, so now he's ANGRIER and more puffed up than before. Chin goes EXTRA far out. This is pure fragile ego in pixel form.

---

## Animation: SPECIAL -- "Arma Brochavel" (4 frames)
**Sprite Sheet:** `bolsonaro-special-arma.png` -- 256x64px (4 frames x 64px)
**Frame Rate:** 10 fps
**Loop:** No

### Frame 0: Charge -- Dramatic Draw
- **Position:** 0,0 to 63,63
- **Description:** Full cowboy pose. Legs spread WIDE (feet at frame edges). Right hand reaches across body to holster on left hip (cross-draw). Left hand raised with finger pointing (accusatory "vagabundo!" gesture). Chin thrust forward. Body rotates 10 degrees for dramatic angle. Eyes blazing (tiny yellow highlight in pupils). Teeth bared in predatory grin. Camera zoom effect indicated by 1px inward border lines at corners.
- **Style Notes:** Pure cowboy movie parody. The cross-draw is deliberately theatrical.

### Frame 1: Draw -- Gun Out
- **Position:** 64,0 to 127,63
- **Description:** Revolver pulled out in dramatic arc. Motion trail on gun (3px yellow arc line, 50% opacity). Gun catches light (2px white starburst on barrel). Body pivots to face target. Left hand drops to brace. Chin leads the rotation. Wind effect on hair (strands blown back 2px). Faixa billows dramatically. Belly exposed as shirt rides up during motion. Scar visible and EMPHASIZED (wider than normal, glowing slightly).
- **Style Notes:** The gun draw should feel like a spaghetti western freeze-frame. Maximum cool-guy energy that is about to be undermined.

### Frame 2: Fire -- RNG Split
- **Position:** 128,0 to 191,63
- **Description:** **SUCCESS (70%):** Enormous muzzle flash (12x12px, golden-yellow with orange core). THREE bullets visible as golden trails. Recoil pushes entire body back 4px. Shell casings rain (3x 2px gold pixels). Smoke cloud (6x4px). Face shows MANIC JOY -- grin at maximum width, eyes wild. Chin vibrates from recoil. Screen shake indicator (frame border jitters 1px). **FAIL (30%):** Gun emits pathetic "poof" cloud (5x5px gray, comical shape like a sad cloud). Gun barrel droops dramatically. Face transitions from manic joy to CRUSHED DESPAIR in the same frame (left half maniac, right half devastated -- grotesque split expression). Self-damage red flash on body. Small bandaid icon appears on gun.
- **Style Notes:** The success/fail are rendered as the SAME frame with alternate versions. The fail version's split-face expression is a masterpiece of grotesque comedy -- half triumphant, half horrified, all absurd.

### Frame 3: Aftermath
- **Position:** 192,0 to 255,63
- **Description:** **SUCCESS:** Smoke clearing. Cowboy pose held -- gun raised, smoke trailing, smirk on face. Chin at MAXIMUM jut. Free hand blows smoke from barrel (lips pursed, tiny smoke wisps). Belly sucked in (trying to look cool). Faixa settles. **FAIL:** Full humiliation pose. Gun held at arm's length like a dead fish. Other hand on hip in frustration. Head hanging (chin points at ground for once). Kicked-dirt effect at feet (small dust cloud). Faixa tangled. Belly hanging out, scar exposed, no attempt to look cool. Phone buzzes in pocket (screen glow through fabric -- supporters sending "???").
- **Style Notes:** The contrast between success and fail aftermath must be STARK. Success = parody of cool. Fail = depths of patheticness.

---

## Animation: SPECIAL -- "Motociata" (6 frames)
**Sprite Sheet:** `bolsonaro-special-motociata.png` -- 384x64px (6 frames x 64px)
**Frame Rate:** 12 fps
**Loop:** No

### Frame 0: Mount Up
- **Position:** 0,0 to 63,63
- **Description:** Bolsonaro swinging leg over a Harley-Davidson silhouette (golden, 40x24px, lower half of frame). Right leg in mid-air. Arms reaching for handlebars. Chin up, triumphant expression. Faixa streaming behind. Gun holstered. The motorcycle is grotesquely oversized with chrome highlights and a Brazil flag on the fuel tank. Exhaust pipe emits green-yellow fumes (verde-amarelo particles).

### Frame 1: Rev Engine
- **Position:** 64,0 to 127,63
- **Description:** Seated on bike. Both hands on handlebars. Revving throttle -- right hand twisted forward. Bike vibrates (1px jitter on all motorcycle pixels). Exhaust cloud grows (8x6px, verde-amarelo). Face shows ECSTASY -- mouth wide open in a yell, eyes maniacally wide. Chin vibrates with engine. Belly bounces on seat. Screen shake lines at frame edges. Tire spin marks (2px dark lines under rear wheel). Sound wave indicators (2 curved lines emanating from exhaust, 1px each).

### Frame 2: Launch / Charge
- **Position:** 128,0 to 191,63
- **Description:** Bike wheels UP -- front wheel lifts 4px (wheelie). Bolsonaro leans forward, chin almost touching handlebars. Hair blown straight back. Faixa horizontal behind like a flag. Maximum speed lines (4-5 horizontal lines, 1px white, 60% opacity, full frame width). Tire burns (fire-like orange/red particles at rear wheel). Verde-amarelo exhaust trail fills bottom 8px of frame. Ghost motos begin appearing behind (2-3 translucent green motorcycle silhouettes, 30% opacity, offset 4-8px behind).

### Frame 3: Full Speed Charge
- **Position:** 192,0 to 255,63
- **Description:** Maximum velocity. Bike and rider are a blur of motion. Speed lines dominate (6+ lines across frame). Ghost motos multiply (5-6 translucent green copies filling the background, varying opacity 20-40%). Fire trail under rear wheel. Bolsonaro's face is a grotesque blur of grin and chin -- features smear horizontally from speed. Faixa becomes a solid horizontal line. Impact zone ahead indicated by target marker (2x2px red crosshair at frame right edge). Chrome and gold of the bike catch light in streaks. The whole composition screams FORWARD MOMENTUM.

### Frame 4: Impact / Crash Zone
- **Position:** 256,0 to 319,63
- **Description:** Bike hits SOMETHING (impact zone). Massive starburst (16x16px, centered on right third of frame). Bolsonaro separating from bike (body lifting upward and forward, bike sliding underneath). Arms flailing. Chin leads the trajectory (naturally). Ghost motos pile up behind in a chain-reaction crash (overlapping translucent silhouettes crumpling). Debris everywhere -- chrome pieces (2x2px silver), faixa fragments, exhaust cloud mushrooming. Bike tilting onto its side. Bolsonaro's expression: TERRIFIED SURPRISE, mouth as wide as physically possible.

### Frame 5: Aftermath / Dismount Fail
- **Position:** 320,0 to 383,63
- **Description:** Bolsonaro on the ground next to the toppled bike. Bike wheels still spinning (motion blur on wheels). Bolsonaro in a heap -- limbs askew, chin resting on the ground, faixa wrapped around one leg. Dust cloud settling around the crash site. Ghost motos have dissipated (fading green wisps). One shoe off. Hair completely messed up. Sunglasses cracked and hanging off one ear. Trying to stand but only managing to lift chin off ground (chin as leverage point). Revolver fell out during crash (visible 6px away). Small "estrelinhas" (cartoon stars) orbiting his head. Despite everything, one thumb weakly raised in a "talkei" gesture.
- **Style Notes:** The comedy climax. He did the big dramatic motociata and ended up in a heap. The weak "talkei" thumbs-up from the ground is PERFECT Andre Guedes energy -- delusional positivity in the face of complete failure.

---

## Animation: SPECIAL -- "Golpe Frustrado" (8 frames)
**Sprite Sheet:** `bolsonaro-special-golpe.png` -- 512x64px (8 frames x 64px)
**Frame Rate:** 10 fps
**Loop:** No

### Frame 0: Military Salute
- **Position:** 0,0 to 63,63
- **Description:** Bolsonaro in full military salute pose. Body rigid. Chin at 45 degrees upward. Right hand at forehead in crisp salute. Left hand at side, fist clenched. Expression: DETERMINED, jaw set. Feet together. A faint green camouflage pattern overlays his clothes (4-5 camo splotches, 20% opacity). The air behind him shimmers with anticipation (heat-wave effect, 2-3 wavy vertical lines).

### Frame 1: Summoning Call
- **Position:** 64,0 to 127,63
- **Description:** Mouth opens WIDE in a commanding shout. Both arms raised overhead in a rallying gesture. Veins pop on forehead (3 red 1px lines). Eyes blazing. Chin thrusts forward while shouting. Sound wave rings emanate from mouth (3 concentric arcs, 1px each, expanding outward). Faixa billows from the vocal force. A military trumpet icon (4x6px, golden) appears to the side. The ground cracks slightly at his feet (1-2 dark lines).

### Frame 2: Waiting...
- **Position:** 128,0 to 191,63
- **Description:** Arms still raised but starting to lower. Expression shifts from commanding to... confused. One eyebrow raises (the other stays angry -- asymmetric). The trumpet icon shatters into pixels. Sound waves dissipate. An awkward silence visual -- "..." appears above head (3 dots, 2px each, gray). Chin wobbles with uncertainty. Sweat drop appears. He glances left and right with just his eyes. Faixa droops.

### Frame 3: Eduardo Appears (Wrong)
- **Position:** 192,0 to 255,63
- **Description:** Instead of military forces, EDUARDO appears from the right edge of the frame -- a smaller, goofier version of Bolsonaro (35px tall, same chin but somehow dumber-looking). Eduardo is running in from the wrong direction (entering from behind Bolsonaro instead of toward the enemy). Eduardo wears an oversized American flag t-shirt and has his phone out taking a selfie. Bolsonaro's expression: JAW DROP. Chin literally hangs lower (2px drop from shock). Eyes popping. One hand reaches toward Eduardo in a "WHAT ARE YOU DOING" gesture.

### Frame 4: Eduardo Runs Wrong Way
- **Position:** 256,0 to 319,63
- **Description:** Eduardo running across the frame in the WRONG direction (away from enemies). Speed lines trail behind Eduardo. Eduardo is looking at his phone, not where he's going. Bolsonaro pointing frantically the other way with both hands, gun forgotten at his side. Face contorted in paternal FURY and EMBARRASSMENT. Chin vibrates with rage. Veins popping. Faixa being pulled in Eduardo's direction from the whoosh of his passing.

### Frame 5: Eduardo Falls in Hole
- **Position:** 320,0 to 383,63
- **Description:** A hole opens in the ground (8x8px dark void in the frame). Eduardo's legs sticking up out of the hole, still running motion (legs cycling in air). Phone flying upward from the hole with a cracked screen. Stars and dust cloud around the hole opening. Bolsonaro frozen mid-gesture, staring at the hole with an expression that mixes HORROR, EMBARRASSMENT, and "I knew this would happen" resignation. Mouth slightly open. One hand covers part of his face (facepalm beginning).

### Frame 6: Facepalm
- **Position:** 384,0 to 447,63
- **Description:** Full FACEPALM. Both hands covering face (but chin still visible because it's too large to cover). Body slumped. Gun dangling from one finger. Faixa limp. Eduardo's legs still weakly kicking from the hole (slowing down). A "shame cloud" effect around Bolsonaro -- dark gray aura (2px around body, 15% opacity). Small text-balloon-style "..." near his head. The ground around the hole has cracks spreading. Sunglasses slide completely off head onto ground.

### Frame 7: Angry Recovery
- **Position:** 448,0 to 511,63
- **Description:** Hands slam down from face. Expression: VOLCANIC RAGE. Eyes bloodshot, veins everywhere, chin thrust forward at maximum. Mouth forms a scream (all teeth visible, gums visible). Points accusingly at the hole where Eduardo fell. Other hand raises gun (but accidentally pointing at himself -- ironic detail). Faixa whips with the force of his anger. Body trembles (1px vibration). A small Eduardo hand sticks out of the hole waving weakly. Despite rage, a single tear of frustration (1px blue pixel) on one cheek.

---

## Animation: SPECIAL -- "Pintou um Clima" (4 frames)
**Sprite Sheet:** `bolsonaro-special-pintou.png` -- 256x64px (4 frames x 64px)
**Frame Rate:** 8 fps
**Loop:** No

### Frame 0: Setup -- Uncomfortable Lean
- **Position:** 0,0 to 63,63
- **Description:** Bolsonaro leans in toward the viewer with an uncomfortably close posture. One arm propped on an invisible wall/ledge. Other hand gestures vaguely. Face has a CREEPY inappropriate smile -- different from his normal forced grin. This one is worse: eyes half-lidded, one eyebrow raised, teeth slightly parted. Chin forward but in a "smarmy" angle rather than aggressive. Body language: too close, too casual, too confident about something no one should be confident about.
- **Style Notes:** Maximum cringe. The viewer should feel the discomfort radiating from this frame. This is the "awkward uncle at the family BBQ" energy turned up to 11.

### Frame 1: The Phrase
- **Position:** 64,0 to 127,63
- **Description:** Mouth forming the words "Pintou um clima..." Speech bubble indicator (small tail from mouth, 2px). Eyes somehow get MORE half-lidded. Free hand makes a weird wiggling gesture (fingers undulating). Entire body radiates a pink/purple "cringe aura" (2px gradient border around body, blending from pink #FF69B4 to purple #800080, 30% opacity). Other characters in range would freeze (not rendered here, handled by game engine). A visible "wave" of discomfort emanates outward (concentric semicircles of pink energy, 1px each, expanding from his position).
- **Style Notes:** The cringe aura is a literal gameplay mechanic visualization. Pink/purple conveys the skeeviness.

### Frame 2: Area Effect Active
- **Position:** 128,0 to 191,63
- **Description:** Full cringe zone active. Bolsonaro in the center of a pulsing pink/purple energy field (fills 80% of frame, concentric rings). His expression is OBLIVIOUS -- he doesn't understand why everyone is frozen/disgusted. Still doing the smarmy lean. Still smiling that HORRIBLE smile. The energy field has small "!" marks floating in it (4-5 exclamation points, 2px each, scattered). The ground beneath him has a pink tint. His own faixa recoils away from him (curves unnaturally away from his body as if even the sash is disgusted). Phone in pocket buzzes (glow through fabric -- people are already clipping this).
- **Style Notes:** The obliviousness is critical. He thinks this is normal. He thinks this is CHARMING. The disconnect between his self-perception and reality IS the joke and the attack.

### Frame 3: Effect End / Confusion
- **Position:** 192,0 to 255,63
- **Description:** Energy field dissipating (rings fading, pink color draining). Bolsonaro straightens up, brushing off his shirt as if nothing happened. Expression returns to normal forced grin. Adjusts sunglasses on head. Adjusts faixa. Completely unaware of the damage he just caused. A single sweat drop on targets in range (not rendered here). His posture returns to the "talkei stance" from idle. Small sparkle effect as cringe zone fully dissipates (3-4 white 1px pixels). Chin returns to standard jut position.
- **Style Notes:** Total reset. He has no idea what just happened. This is the punchline -- the oblivious recovery.

---

## Animation: SPECIAL -- "Live da Cela" (6 frames)
**Sprite Sheet:** `bolsonaro-special-live.png` -- 384x64px (6 frames x 64px)
**Frame Rate:** 10 fps
**Loop:** No

### Frame 0: Secret Phone Pull
- **Position:** 0,0 to 63,63
- **Description:** Bolsonaro glances left and right (eyes shifting, paranoid). One hand slowly reaches into prison uniform pocket (for 2026 skin -- or regular pants pocket for default skin). The phone's screen glow visible through the fabric before extraction (blue-white glow, 2px, through orange or yellow fabric). Other hand raised in a "shh" gesture (finger to lips). Body hunched, sneaky posture. Chin tucked in (rare!) to avoid detection. Prison bars visible in foreground (for 2026 skin, 3 vertical gray lines at 20% opacity overlaying the frame).
- **Style Notes:** The sneaky posture is COMPLETELY at odds with his normal bravado. The phone glow through fabric is a great detail.

### Frame 1: Live Start
- **Position:** 64,0 to 127,63
- **Description:** Phone out and held up at face level (3x5px phone with blue-white screen). Red "LIVE" indicator dot (1px red, pulsing). Face illuminated by phone light (blue-white highlights on chin, nose, cheeks). Expression transforms from sneaky to MANIC ENERGY -- eyes wide open, grin at maximum, eyebrows raised. Straightens up (no longer sneaky, now fully committed). Other hand makes thumb-up. Viewer count indicator on phone screen (small numbers). The transformation from sneaky to showman should be INSTANT -- like flipping a switch.

### Frame 2: Broadcasting
- **Position:** 128,0 to 191,63
- **Description:** Full live-streaming mode. Phone held steady. Free hand gesticulating wildly (blurred motion, 2px motion lines on hand). Mouth WIDE open, clearly ranting. Chin at maximum projection. Signal waves emanate from phone (3 curved lines, expanding outward to the right, alternating blue and white, 1px each). Phone screen shows a crude representation of his own face (recursive live -- he's watching himself stream). Viewer count rising (small upward arrow). Red recording dot BRIGHT. Body language: full energy, standing straight, commanding.

### Frame 3: Apoiadores Summoned (Spawn Start)
- **Position:** 192,0 to 255,63
- **Description:** Signal waves from phone reach frame edges and BEGIN MANIFESTING into ghost forms. 2-3 translucent green motorcycle silhouettes (#44FF44, 30% opacity) materialize at frame edges, riding in from the right. Each ghost moto has a rider silhouette with a small Brazil flag. Bolsonaro's expression: TRIUMPHANT. Points at the ghost motos with gun hand (gun used as pointer, not weapon). Chin at maximum. Phone still streaming. The ghost motos leave green exhaust trails. Small "notification" icons (heart shapes, thumbs up, 1px each, red/blue) float up from the phone.

### Frame 4: Ghost Horde Active
- **Position:** 256,0 to 319,63
- **Description:** Frame filled with ghost motos (5-6 translucent green motorcycles riding in various directions). Bolsonaro at center, phone held high like a conductor's baton. Expression: ECSTASY of power. Free arm spread wide, embracing the chaos. Ghost riders are crude silhouettes -- just enough detail to see they're on motorcycles waving flags. Green exhaust creates a haze across the lower half of the frame (verde mist, 20% opacity). Notification icons multiply. Sound wave indicators from multiple ghost motos. The whole scene is CHAOTIC ENERGY.

### Frame 5: Signal Fade / Return
- **Position:** 320,0 to 383,63
- **Description:** Ghost motos beginning to fade (opacity dropping from 30% to 10%). Bolsonaro hurriedly hiding phone back in pocket (arm jammed in pocket up to the elbow). Expression shifts from triumphant to paranoid again (eyes darting). Body returning to hunched posture. One ghost moto lingers, frozen mid-ride, then pixelates and dissipates. Green haze clearing. Notification icons falling like dead pixels. Signal waves collapsing inward. The "LIVE" dot blinks twice and goes dark. Bolsonaro's grin becomes a tight-lipped "I was definitely not doing anything" expression. Hands behind back, whistling pose (small music notes, 2px, near mouth).
- **Style Notes:** The transition back to "innocent" is as abrupt as the transition TO mania in Frame 1. Same switch, opposite direction. Peak comedy.

---

## Animation: SPECIAL -- "Imorrivel, Imbrochavel, Incomivel" (4 frames)
**Sprite Sheet:** `bolsonaro-special-invuln.png` -- 256x64px (4 frames x 64px)
**Frame Rate:** 8 fps
**Loop:** Frames 1-2 loop for 5 seconds duration

### Frame 0: Activation Pose
- **Position:** 0,0 to 63,63
- **Description:** Arms crossed over chest in an X (power-up pose). Head tilted back, chin pointing at the sky. Eyes closed with supreme confidence. Faixa GLOWING (verde-amarelo pulsing, 1px glow outline). Gun holstered. Feet planted. A golden aura begins forming (1px gold outline, 30% opacity, 2px away from body). Body begins to GLOW from within (skin highlights intensify, all highlight hex values brighten by 20%). Belly scar SHINES (scar becomes golden instead of pink). The word "IMORRIVEL" begins to form above head in golden letters (partial, 6px tall).

### Frame 1: Invulnerable State A
- **Position:** 64,0 to 127,63
- **Description:** Golden aura at full strength (3px golden glow around entire body, 60% opacity). Arms uncross and go to triumphant fists-at-sides pose. Chin MAXIMUM forward. Eyes BLAZING gold. Forced grin now looks genuinely confident (rare). Entire body has golden overlay (20% opacity, #DAA520). All incoming damage indicators bounce off (small white "PING" starbursts, 2-3px, at random points around the aura border). "IMORRIVEL" text complete above head, pulsing. Faixa rigid and billowing with power. Scar glowing gold. Hair swept back by energy. Even the gun in holster glows.

### Frame 2: Invulnerable State B
- **Position:** 128,0 to 191,63
- **Description:** Golden aura PULSES (expands 2px then contracts, breathing rhythm). Arms shift to different triumphant pose -- one fist raised, one pointing forward. Chin oscillates (1px forward/back with the aura pulse). Eyes flash between gold and normal (alternating frames creates strobe). Text above head cycles: "IMBROCHAVEL" then "INCOMIVEL" (3 phrases rotate). The golden overlay shifts color slightly on pulse (pure gold -> warm gold -> pure gold). Small golden particles (3-4 1px gold pixels) orbit the body in a slow circle. Faixa streams horizontally from wind energy.
- **Style Notes:** The cycling text and pulsing aura are the key tells for this invulnerability state. Should feel POWERFUL but also ridiculous -- a man making himself invincible by saying three made-up words.

### Frame 3: Deactivation
- **Position:** 192,0 to 255,63
- **Description:** Golden aura SHATTERS (fragments outward as 8-10 gold 2x2px shards flying to frame edges). Body returns to normal colors instantly. The text above head dissolves letter by letter. Bolsonaro STAGGERS (body tilts 3px to the side, one hand on knee). The energy drain is visible -- eyes half-closed, forced grin weakens, chin droops 2px. Sweat drops (3-4 1px drops) fly off. Faixa goes limp. Belly distends from exhaustion. Gun droops in holster. A brief gray "exhaustion cloud" (4x3px, 20% opacity) passes over his body. Recovery takes a beat -- vulnerability window.
- **Style Notes:** The crash from invulnerability is HARSH. All that bravado drains out instantly. The physical toll of pretending to be invincible is written all over his body.

---

## Animation: ULTIMATE -- "Motociata do Juizo Final" (8 frames)
**Sprite Sheet:** `bolsonaro-ultimate-motociata.png` -- 512x64px (8 frames x 64px)
**Frame Rate:** 12 fps
**Loop:** No (play once)

### Frame 0: Whistle / Summon
- **Position:** 0,0 to 63,63
- **Description:** Two fingers in mouth, LOUD whistle pose. Body leaning back. Chin angled up. Eyes scanning horizon. Sound waves MASSIVE (5 concentric arcs from mouth, filling half the frame). The ground vibrates (zigzag lines at floor level, 2px). Distant rumble indicated by small debris bouncing (3-4 1px pixels hopping at ground level). Faixa catches wind from an unseen approaching force. Hair blown forward.

### Frame 1: Golden Harley Arrives
- **Position:** 64,0 to 127,63
- **Description:** A MASSIVE golden Harley-Davidson crashes into frame from the left (44x28px, takes up most of the bottom half). Pure gold paint (#DAA520) with chrome accents (#C0C0C0). Brazil flag fuel tank. Oversized exhaust pipes belching verde-amarelo smoke. The bike is still SLIDING (spark trail under tires, 4-5 orange 1px pixels). Bolsonaro leaping toward it (feet off ground 4px, arms reaching for handlebars). Expression: PURE CHILDLIKE JOY -- the only time his smile looks genuine. Chin leading the leap.

### Frame 2: Mount + Rev
- **Position:** 128,0 to 191,63
- **Description:** Seated and revving. Engine indicators HUGE (vibration lines completely surround the bike, 2px offset in all directions). Exhaust cloud fills bottom 12px of frame. Head thrown back in a howl/war cry (mouth at maximum open, every tooth visible, chin at maximum angle). Both hands on handlebars, throttle CRANKED. The bike lifts on its shocks (2px bounce). Ground cracks radiate from rear tire (4-5 dark lines). Behind him, the first ghost motos begin forming -- 3 green translucent motorcycles materializing from verde smoke.

### Frame 3: Charge Launch
- **Position:** 192,0 to 255,63
- **Description:** WHEELIE at maximum angle (front wheel 8px higher than rear). Speed lines EXPLODE across the entire frame (8+ horizontal lines, varying thickness 1-2px). Body compressed forward, chin as aerodynamic point. Faixa streaming 16+ pixels behind (extends to left frame edge). Ghost motos multiply: 8-10 translucent green bikes in V-formation behind. Each ghost rider waves a small flag. Tire fire at rear wheel (8x4px flame sprite). The golden bike GLEAMS (multiple white highlights). Screen border flashes gold. Dust/debris mushroom cloud at launch point.

### Frame 4: Full Horde Charge
- **Position:** 256,0 to 319,63
- **Description:** MAXIMUM CHAOS. Frame is dominated by the golden bike in center-left with 12-15 ghost motos filling the background. Speed lines everywhere. Verde-amarelo exhaust trail creates a fog across the entire frame bottom. Bolsonaro is a blur of teeth and chin (features smeared by speed). Ghost riders are crude but MENACING -- glowing green with small red eye dots. The formation is a wedge shape aimed at the right side of the frame. Small objects caught in the wake fly backward (paper, leaves, a hat, small debris pixels). The bike's headlight is a blinding white circle (4px diameter).

### Frame 5: Impact Zone
- **Position:** 320,0 to 383,63
- **Description:** The wedge formation HITS. Massive impact starburst (20x20px, centered on right third, golden-white core fading to orange edges). Ghost motos crashing into each other (overlapping green silhouettes compressing). The golden bike begins to TILT (45 degree lean, front wheel turning). Bolsonaro's expression shifts from MANIC JOY to "oh no" (eyes suddenly wide, grin becoming grimace). Debris EVERYWHERE -- chrome pieces, flag fragments, green ghost particles, orange exhaust, white impact sparkles. The impact fills 60% of the frame with effects.

### Frame 6: The Fall
- **Position:** 384,0 to 447,63
- **Description:** Bolsonaro AIRBORNE. Separated from bike completely. Body in ragdoll tumble (limbs in random directions). Bike sliding away sideways on the ground, sparking. Ghost motos EXPLODING into green pixel clouds. Bolsonaro rotates 180 degrees (now upside down, chin pointing at ground). Faixa wrapped around his leg. Gun flying free (8px from body). Sunglasses long gone. Expression: PURE TERROR -- eyes circles, mouth a perfect O, chin somehow STILL prominent even upside down. Trajectory arc indicated by dotted line. Small golden stars circling already.

### Frame 7: Crash Landing
- **Position:** 448,0 to 511,63
- **Description:** GROUND IMPACT. Bolsonaro face-down (chin-down, specifically -- chin creates a small CRATER in the ground, 4x2px indentation). Bike toppled 12px away, rear wheel spinning, exhaust sputtering. All ghost motos gone (only fading green wisps remain). Crater has radiating crack lines. Dust cloud MASSIVE (12x8px, settling). Faixa limp across body. Arms and legs in a star pattern (sprawled). One shoe gone, one barely hanging on. Gun at maximum distance (16px away). Stars orbiting intensely (5 golden stars, 2px each, tight circle). Despite everything: one hand slowly raises... thumb up... "talkei." A weak, broken, but PERSISTENT thumb-up from the wreckage.
- **Style Notes:** THIS IS THE MONEY FRAME. The chin crater. The weak thumbs-up from the rubble. The spinning bike wheel. The fading ghost wisps. This single frame encapsulates the entire character: grandiose ambition, spectacular failure, and delusional persistence. Every pixel must serve the comedy.

---

## Sprite Sheet Summary

| Animation         | Filename                            | Frames | Sheet Size | FPS |
|-------------------|-------------------------------------|--------|------------|-----|
| Idle              | `bolsonaro-idle.png`                | 4      | 256x64     | 8   |
| Walk              | `bolsonaro-walk.png`                | 6      | 384x64     | 10  |
| Attack            | `bolsonaro-attack.png`              | 3      | 192x64     | 10  |
| Death             | `bolsonaro-death.png`               | 4      | 256x64     | 8   |
| Hit               | `bolsonaro-hit.png`                 | 2      | 128x64     | 12  |
| Special: Arma     | `bolsonaro-special-arma.png`        | 4      | 256x64     | 10  |
| Special: Motociata| `bolsonaro-special-motociata.png`   | 6      | 384x64     | 12  |
| Special: Golpe    | `bolsonaro-special-golpe.png`       | 8      | 512x64     | 10  |
| Special: Pintou   | `bolsonaro-special-pintou.png`      | 4      | 256x64     | 8   |
| Special: Live     | `bolsonaro-special-live.png`        | 6      | 384x64     | 10  |
| Special: Invuln   | `bolsonaro-special-invuln.png`      | 4      | 256x64     | 8   |
| Ultimate          | `bolsonaro-ultimate-motociata.png`  | 8      | 512x64     | 12  |

**Total frames:** 59
**Combined atlas:** All sheets pack into a single 2048x2048 atlas with room for skin variants.

## Phaser 3 Atlas Keys
```
key: 'boss_bolsonaro_idle'       frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_walk'       frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_attack'     frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_death'      frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_hit'        frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_special_arma'      frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_special_motociata' frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_special_golpe'     frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_special_pintou'    frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_special_live'      frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_special_invuln'    frameWidth: 64  frameHeight: 64
key: 'boss_bolsonaro_ultimate'          frameWidth: 64  frameHeight: 64
```

## Notes for Artist
1. The CHIN is the character. If the chin doesn't dominate, start over.
2. The forced grin should NEVER look natural -- it must always feel like muscles straining against the face.
3. The gun drooping on fail ("brochavel") must read clearly even at 64px -- exaggerate the droop.
4. Every "cool" moment (cowboy draw, motorcycle ride, invulnerability) must be immediately followed by humiliation.
5. The belly scar is ALWAYS visible -- shirt too tight, riding up, or just exposed. It glows during damage.
6. Outlines MUST be 2-3px thick and IRREGULAR. If they look clean, redraw them worse.
7. Colors should look like they were mixed in dirty water -- saturated but grimy, never bright and clean.
8. Andre Guedes reference: watch his TikTok Bolsonaro animations before drawing a single pixel.
9. Eduardo (in Golpe Frustrado) should be visibly DUMBER-looking -- same chin but with no charisma behind it.
10. The "talkei" thumbs-up from the wreckage in the ultimate's final frame is the character's thesis statement.
