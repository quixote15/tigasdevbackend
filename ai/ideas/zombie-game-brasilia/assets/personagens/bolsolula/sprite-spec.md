# BOLSOLULA (Fusao) — Sprite Specification

## Overview
- **Character Type:** Boss Secreto (secret boss — fusion of Bolsonaro + Lula)
- **Sprite Dimensions:** 96x96px (oversized due to 4 arms and dual body)
- **Sprite Sheet Layout:** Horizontal strips, 1 animation per row
- **Total Frames:** 53 frames across 8 animation sets
- **Sprite Sheet Size:** 2048x2048px (atlas shared)
- **Format:** PNG with alpha transparency
- **Anchor Point:** Bottom-center (48, 90) — center of fused torso base
- **Perspective:** Top-down slightly isometric (Y-sorting)
- **Outline Weight:** 3-4px irregular black outlines (rage-drawn)

## CRITICAL DESIGN RULES
1. The body is split vertically down the center — LEFT half = Lula, RIGHT half = Bolsonaro
2. The fusion line down the middle is UGLY: exposed stitches, mismatched skin tones, visible muscle/tendons, Frankenstein bolts
3. 4 arms total: 2 on Lula side (left), 2 on Bolsonaro side (right)
4. 2 faces fused into one head: Lula's features on left, Bolsonaro's on right
5. NEVER symmetrical. Each side has its own posture, expression, and color scheme
6. Both faces are ALWAYS expressing different emotions simultaneously

---

## Color Palette

| Element | Hex Code | Usage |
|---|---|---|
| **Lula Skin** | `#B07850` | Left half skin — nordestino tan, weathered |
| **Bolsonaro Skin** | `#D4A574` | Right half skin — lighter, paler |
| **Lula Red (Terno)** | `#8B1A1A` | Left half suit / PT vermelho sujo |
| **Lula Red (Light)** | `#A82828` | Left half suit highlights |
| **Lula Red (Dark)** | `#5C1010` | Left half suit shadows |
| **Bolso Green** | `#2E5A1C` | Right half selecao green (normal skin) |
| **Bolso Yellow** | `#C8A832` | Right half selecao yellow accents |
| **Bolso Orange (2026 Preso)** | `#CC5500` | Right half prison uniform (2026 skin) |
| **Bolso Orange (Light)** | `#E07020` | Prison uniform highlights |
| **Bolso Orange (Dark)** | `#993D00` | Prison uniform shadows |
| **Fusion Seam** | `#5C2020` | Central fusion line — exposed flesh |
| **Fusion Stitches** | `#1A1A1A` | Black stitches along seam |
| **Fusion Muscle** | `#8B3030` | Exposed muscle at fusion points |
| **Fusion Bolt** | `#7A7A72` | Frankenstein bolts, metallic gray |
| **Lula Scar (Craniana)** | `#6B3535` | Frankenstein cranial scar on left skull |
| **Lula Nose** | `#C06848` | Bulbous nose — reddened, alcoholic |
| **Bolso Chin** | `#D4A574` x 130% size | Enormous protruding chin |
| **Lula Hair (sparse)** | `#3A3A3A` | Thin gray hair left side |
| **Bolso Hair (sparse)** | `#4A4A3A` | Thin dark hair right side |
| **Beard Lula** | `#5A5A5A` | Gray stubble left jaw |
| **Eye White** | `#E8E0D0` | Dirty white, never pure |
| **Lula Pupil** | `#2A1A0A` | Dark brown, bloodshot |
| **Bolso Pupil** | `#2A2A1A` | Dark, squinting, paranoid |
| **Caneta BIC Red** | `#CC2020` | Left side of weapon |
| **Caneta BIC Green** | `#2E5A1C` | Right side of weapon |
| **Caneta BIC Body** | `#E8E0D0` | Plastic BIC body |
| **Emenda Explosion** | `#F0C830` | Parliamentary amendment explosions |
| **Outline** | `#1A1A18` | All outlines — thick, irregular, angry |
| **Shadow** | `#0D0D0D` alpha 50% | Drop shadow beneath character |

---

## Animation Sets

### SET 1: IDLE (4 frames) — `bolsolula_idle`
**Loop:** Yes | **Frame Rate:** 8 fps | **Sheet Position:** Row 0

#### Frame 0 — `idle_lula_dominant`
- **Position:** 0,0 to 95,95
- **Lula Side (Left):** Stands slightly taller, chest puffed. Left upper arm on hip (power pose). Left lower arm gesticulates with 4-finger hand (missing pinky). Lula face: smug grin, half-closed eyes, bulbous red nose prominent. Frankenstein cranial scar visible across top-left of skull with crude stitches. Wearing dark red terno (2026: presidential suit with sash). Gray stubble on jaw.
- **Bolsonaro Side (Right):** Slightly slumped, subordinate. Right upper arm hangs loosely. Right lower arm holds Caneta BIC diagonally. Bolsonaro face: grimacing, jaw jutting out (enormous chin extends 6px beyond normal), furrowed brow. Wearing green-yellow camisa (2026: orange prison jumpsuit). Thin dark hair combed over.
- **Fusion Seam:** Thick irregular line down center of body. 4-5 visible stitches with cross-hatch pattern. A Frankenstein bolt protrudes from the collarbone area. Skin tones clash violently at the seam — no blending. Small exposed muscle fibers visible at neck junction.
- **4 Arms:** Upper pair slightly raised. Lower pair at waist height. All proportioned differently — Lula arms are thicker/stubbier, Bolsonaro arms are longer/bonier.
- **Weapon:** Caneta BIC Gigante held in Bolsonaro's lower-right hand. Red tip pointing left, green cap pointing right. Oversized — about 40px long.
- **Shadow:** Irregular blob shadow beneath, offset 2px down.

#### Frame 1 — `idle_bolso_dominant`
- **Position:** 96,0 to 191,95
- **Lula Side (Left):** Now subordinate. Slightly slumped. Lula face shifts to annoyed scowl, one eye twitching. Upper-left arm crosses chest defensively. Lower-left arm drops to side. Cranial scar pulses slightly (1px glow around stitches).
- **Bolsonaro Side (Right):** Now dominant. Puffs up, stands taller. Bolsonaro face: triumphant sneer, thumbs-up with upper-right hand (classic Bolsonaro pose). Lower-right hand waves Caneta BIC aggressively. Chin juts forward even more (extra 2px). Prison jumpsuit / selecao shirt wrinkles with motion.
- **Fusion Seam:** Stitches STRETCH as the dominant side puffs up — 2 stitches show visible tension, one has a tiny thread popping. The seam line warps 2px to the left as Bolsonaro side expands.
- **Overall:** Body leans 3-4 degrees to the right (Bolsonaro dominant).

#### Frame 2 — `idle_argue_1`
- **Position:** 192,0 to 287,95
- **Both Sides:** MID-ARGUMENT. Both faces turned slightly inward, facing each other across the fusion seam. Lula face: mouth open wide (yelling "Companheiro!"), veins on temple. Bolsonaro face: mouth open wide (yelling "Vagabundo!"), jaw hyper-extended. All 4 arms gesticulating wildly — upper pair point accusatory fingers at each other across the seam, lower pair wave dismissively. Comic speed lines (2-3 small 1px lines) around the flailing arms.
- **Fusion Seam:** STRAINING. 1 stitch visibly popped (small thread hanging). The bolt vibrates (1px motion blur). Skin at seam is reddened/inflamed from the internal conflict.
- **Caneta BIC:** Dropped to foot level — both sides too busy arguing to hold it.

#### Frame 3 — `idle_confused`
- **Position:** 288,0 to 383,95
- **Both Sides:** Moment of existential confusion. Both faces stare forward (at the player) with identical bewildered expressions — the ONE moment where both faces match. Eyes wide, mouths slightly open, brows raised. All 4 arms hang limply. The body slouches 4px downward. A small "?" symbol (6x6px, `#F0E8D8`) floats above the head (comic book style).
- **Fusion Seam:** Relaxed. Stitches loose. The seam almost looks... peaceful. This is the saddest frame — the monster briefly realizes what it is.
- **Caneta BIC:** Dangles from lower-right hand, tip touching the ground.

---

### SET 2: WALK (6 frames) — `bolsolula_walk`
**Loop:** Yes | **Frame Rate:** 10 fps | **Sheet Position:** Row 1

#### Frame 0 — `walk_step_left`
- **Position:** 0,96 to 95,191
- **Movement:** Left leg forward (Lula side leads). Body leans 5 degrees left. Lula side dominant in this step — face confident. Bolsonaro side dragged along reluctantly — face grimacing.
- **Upper Arms:** Lula upper-left swings forward naturally. Bolsonaro upper-right swings back (counter-motion).
- **Lower Arms:** Lula lower-left holds Caneta BIC mid-stride. Bolsonaro lower-right trails behind.
- **Fusion Seam:** Twists slightly with the walking motion — stitches on the torso stretch diagonally.
- **Feet:** Lula side wears brown dress shoe (scuffed). Bolsonaro side wears military-style boot (2026: prison sandal). Mismatched footwear.

#### Frame 1 — `walk_weight_left`
- **Position:** 96,96 to 191,191
- **Movement:** Full weight on left (Lula) leg. Body compressed 2px vertically (squash). Right (Bolsonaro) leg lifts off ground, knee bent. The 4-arm sway peaks — upper arms at maximum extension.
- **Expressions:** Lula: determined march. Bolsonaro: being dragged, annoyed.
- **Caneta BIC:** Swings forward with momentum.

#### Frame 2 — `walk_mid_transition`
- **Position:** 192,96 to 287,191
- **Movement:** Transitional frame. Both legs roughly even. Body straightens vertically. Both faces look forward. The dominant-side flicker is visible: a subtle 1px color shift at the fusion seam indicates the dominance is switching.
- **Arms:** All 4 at rest position briefly.
- **Fusion Seam:** Bolt sparks (1px yellow flash).

#### Frame 3 — `walk_step_right`
- **Position:** 288,96 to 383,191
- **Movement:** Right leg forward (Bolsonaro side leads). Body leans 5 degrees right. Bolsonaro face now confident — military march posture. Lula side reluctant — scowling.
- **Upper Arms:** Bolsonaro upper-right pumps forward (military march). Lula upper-left swings back.
- **Lower Arms:** Mirror of Frame 0 but reversed dominance.
- **Feet:** Right boot/sandal forward, left shoe trailing.

#### Frame 4 — `walk_weight_right`
- **Position:** 384,96 to 479,191
- **Movement:** Full weight on right (Bolsonaro) leg. Squash on right side. Lula leg lifts. Bolsonaro posture is more rigid/military. Lula side flops loosely.
- **Caneta BIC:** Swings backward.

#### Frame 5 — `walk_stumble`
- **Position:** 480,96 to 575,191
- **Movement:** STUMBLE frame — the internal disagreement causes a brief trip. Body pitches forward 8 degrees. Both faces show surprise. All 4 arms flail outward for balance. 1-2 motion blur lines behind the torso. The fusion seam STRETCHES visibly — one stitch pops.
- **Comedy Beat:** This frame is 1.5x normal duration (held longer) for comedic timing. The fused monster can't even walk straight because both halves disagree on direction.

---

### SET 3: ATTACK (3 frames) — `bolsolula_attack`
**Loop:** No | **Frame Rate:** 10 fps | **Sheet Position:** Row 2

#### Frame 0 — `attack_windup`
- **Position:** 0,192 to 95,287
- **Action:** Both sides rear back in unison (rare agreement). All 4 arms pull backward. Upper-right (Bolsonaro) arm grips the Caneta BIC Gigante at the top. Upper-left (Lula) arm grips it at the bottom. Lower arms brace the body. Both faces show RAGE — Lula's teeth bared, Bolsonaro's jaw clenched.
- **Caneta BIC:** Pulled back to maximum, angled 45 degrees. Red tip glows (2px aura, `#CC2020` at 40% opacity). Green cap glows (2px aura, `#2E5A1C` at 40% opacity).
- **Body:** Compressed 4px (squash), storing energy.
- **Fusion Seam:** Taut. All stitches pulled tight. Bolt glows hot (1px white highlight).

#### Frame 1 — `attack_strike`
- **Position:** 96,192 to 191,287
- **Action:** SLAM. Caneta BIC swung forward with all 4 arms driving it. The pen is now nearly horizontal, tip pointing at enemy. Motion blur trails (3 lines, 1px each, decreasing opacity 60/40/20%). Body stretches 4px forward (stretch from the squash). Both faces SCREAM — mouths fully open, Lula: "COMPANHEIRO!", Bolsonaro: "VAGABUNDO!" Speech bubble hint (tiny "!" symbols, 3px, flanking each side of the head).
- **Caneta BIC:** At point of contact. The tip WRITES mid-air — a small scribble trail (3-4px squiggle line in red/green mixed) appears behind the pen tip. This is the "emenda parlamentar explosiva" being signed.
- **Impact Zone:** Small starburst (8x8px) at pen tip in `#F0C830`.

#### Frame 2 — `attack_followthrough`
- **Position:** 192,192 to 287,287
- **Action:** Follow-through. Caneta BIC has passed the strike point. The signed "emenda" (small paper icon, 6x6px, `#E8D8B0`) flies forward from the pen tip, about to explode. All 4 arms extended forward. Body returns to normal proportions. Both faces: post-strike satisfaction — Lula smugly nods, Bolsonaro smugly sneers. 
- **Particles:** 2-3 small paper scraps (`#E8D8B0`, 2x2px) scatter from the emenda. Ink drops (1px, red and green) splatter from pen tip.
- **Fusion Seam:** Relaxes. One stitch swings loosely.

---

### SET 4: DEATH (4 frames) — `bolsolula_death`
**Loop:** No | **Frame Rate:** 6 fps (slower, dramatic) | **Sheet Position:** Row 3

#### Frame 0 — `death_shock`
- **Position:** 0,288 to 95,383
- **Action:** Moment of fatal hit. Both faces register SHOCK differently — Lula face: wide-eyed disbelief, mouth O-shaped. Bolsonaro face: enraged, refusing to accept it, jaw clenched. All 4 arms splay outward dramatically. Body jerks backward 4px. Caneta BIC flies out of hands (airborne, rotated 30 degrees). A crack appears on the Frankenstein bolt.
- **Fusion Seam:** The first stitch SNAPS. A bright red flash (2px) at the snap point.
- **HP Bar:** Would show 0 at this point.

#### Frame 1 — `death_split_start`
- **Position:** 96,288 to 191,383
- **Action:** The fusion begins to FAIL. The seam splits 4px wide at the torso — exposing a dark void inside (`#0A0A0A`). Stitches snap one by one (2 more gone). Lula half pulls left, Bolsonaro half pulls right. Both faces now show FEAR — the one emotion they share. All 4 arms reach across the widening gap, trying to hold the two halves together.
- **Particles:** Stitch thread fragments (1px black lines) fly outward. Small chunks of flesh (2x2px, `#8B3030`) fall from the seam.
- **Caneta BIC:** On the ground behind them, broken in half — red side and green side separated.

#### Frame 2 — `death_collapse`
- **Position:** 192,288 to 287,383
- **Action:** The body collapses. Both halves sag inward — unable to stand without each other. Knees buckle. The head droops. Lula face: tears streaming (2px blue lines). Bolsonaro face: single tear (won't admit it, but there's one). All 4 arms go limp, hanging at sides. The gap at the seam is now 6px wide — the void inside pulses with faint green gas (`#4A7C59` at 20% opacity) — the same gas from the Congresso.
- **Body:** Compressed 8px vertically (collapsing down). Tilted 15 degrees forward.

#### Frame 3 — `death_final`
- **Position:** 288,288 to 383,383
- **Action:** FINAL FRAME. The fused body lies on the ground as a heap. Both faces visible but pressed against the ground, eyes closed (Lula) and half-open-dead (Bolsonaro). All 4 arms splayed in different directions like a squashed spider. The fusion seam is fully split — both halves barely connected by a single remaining stitch at the waist. Small pool of mixed red+green liquid (4x4px puddle) seeps from the seam — neither blood nor ink, something worse.
- **Caneta BIC:** Two broken halves lie nearby, ink pooling — red ink from Lula half, green ink from Bolsonaro half, mixing into a brown sludge.
- **Final Detail:** A tiny paper "emenda" (3x3px) lies in the puddle, dissolving.
- **Shadow:** Flat wide shadow beneath the body, irregular edges.

---

### SET 5: HIT (2 frames) — `bolsolula_hit`
**Loop:** No | **Frame Rate:** 12 fps (fast) | **Sheet Position:** Row 4

#### Frame 0 — `hit_impact`
- **Position:** 0,384 to 95,479
- **Action:** Moment of damage. Body rocks backward 6px. Both faces contort: Lula winces (eyes squeezed shut, mouth grimace), Bolsonaro rages (eyes wide, mouth screaming). The SIDES DISAGREE on reaction — Lula wants to retreat, Bolsonaro wants to fight. This causes the body to twist 10 degrees at the waist (visible torque). Upper arms: Lula's shield face, Bolsonaro's clench fists. Lower arms: Lula's grab stomach, Bolsonaro's point accusingly at attacker.
- **Flash:** White full-body outline flash (1px, `#FFFFFF` at 60% opacity) — standard hit feedback.
- **Fusion Seam:** 1 stitch stretches from the twist. Bolt tilts.
- **Particles:** 2-3 small star impacts (3x3px, `#F0C830`) at point of hit.

#### Frame 1 — `hit_recoil`
- **Position:** 96,384 to 191,479
- **Action:** Recoil. Body bounces back to center (spring effect). Both faces transition to ANGER (unified response — they agree on revenge). All 4 arms swing forward aggressively. The white flash fades. Body stretches 2px upward (bounce). Both halves glow their respective colors briefly: Lula half tints `#8B1A1A` at 15% overlay, Bolsonaro half tints `#CC5500` at 15% overlay.
- **Fusion Seam:** Snaps back taut. The bolt sparks (1px flash).

---

### SET 6: SPECIAL SKILLS (8 frames across multiple attacks) — `bolsolula_special`
**Loop:** No | **Frame Rate:** 8 fps | **Sheet Position:** Row 5

#### Frame 0 — `special_polarizacao_charge` (Polarizacao Total)
- **Position:** 0,480 to 95,575
- **Action:** Both halves pull APART (stretching the seam 6px) while remaining attached. Lula half faces left, Bolsonaro half faces right. Upper arms extend outward to their respective sides. Lower arms hold the Caneta BIC between them (the pen bridges the gap). The ground beneath starts to split — a crack line (1px, `#1A1A18`) extends left (turning red `#8B1A1A`) and right (turning green `#2E5A1C`).
- **Energy Buildup:** Red particles (2x2px) orbit Lula half. Green/yellow particles orbit Bolsonaro half.

#### Frame 1 — `special_polarizacao_blast` (Polarizacao Total)
- **Position:** 96,480 to 191,575
- **Action:** RELEASE. A shockwave emanates from the fusion seam outward in both directions. Left shockwave is RED (`#8B1A1A` at 50% opacity, semicircle expanding left). Right shockwave is GREEN-YELLOW (`#2E5A1C` + `#C8A832` at 50% opacity, semicircle expanding right). Both faces scream outward. All 4 arms throw energy. The Caneta BIC SPINS rapidly (rotation blur) at the epicenter.
- **Effect:** The field is now divided — anything on the "wrong" side takes damage.

#### Frame 2 — `special_palanque_summon` (Palanque Infinito)
- **Position:** 192,480 to 287,575
- **Action:** Both lower arms SLAM downward. TWO palanques (wooden podiums, `#6B4423`) erupt from the ground — one on each side. Left palanque draped in red cloth (`#8B1A1A`). Right palanque draped in green-yellow cloth (`#2E5A1C` + `#C8A832`). Both faces adopt COMICIO expressions: wide-mouth oratory, one finger raised (upper arms).
- **Podiums:** Each ~20x24px, crude wooden construction with microphone (1px line + 3px circle).
- **Caneta BIC:** Used as a gavel, raised high.

#### Frame 3 — `special_palanque_speech` (Palanque Infinito)
- **Position:** 288,480 to 383,575
- **Action:** SPEAKING. Both mouths open wide, speech bubbles emerge from BOTH sides simultaneously. Left bubble: "COMPANHEIRO!" (tiny red text, 1px font). Right bubble: "VAGABUNDO!" (tiny green text, 1px font). Sound waves (concentric arcs, 1px, alternating red and green) radiate outward from both podiums. The speeches are IDENTICAL in content despite different words — same gestures, same cadence, same empty promises.
- **Audience:** 4-6 tiny figures (3x3px each) gather around each podium, mesmerized.

#### Frame 4 — `special_debate_start` (Debate Eterno)
- **Position:** 384,480 to 479,575
- **Action:** Both faces turn INWARD to face each other across the seam. Both mouths open for debate. Upper arms: index fingers pointing at each other aggressively. Lower arms: pound respective podiums. The energy between the two faces crackles (zigzag line, 1px, alternating red/green, between the faces).
- **Expression:** Lula: righteous indignation. Bolsonaro: contemptuous rage.

#### Frame 5 — `special_debate_sonic` (Debate Eterno)
- **Position:** 480,480 to 575,575
- **Action:** SONIC BLAST. Both faces scream simultaneously, creating a visible sound wave that expands in a full circle (not hemicircle). The wave is a pulsing ring (2px thick, alternating red-green-red-green segments). Both faces are MAX distortion: Lula's mouth stretches 8px wide, Bolsonaro's chin extends 8px down. All 4 arms cover their own ears (they're hurting themselves). Small cracks appear on the Frankenstein bolt from the vibration.
- **Damage Zone:** Full 360-degree AoE indicated by the expanding ring.

#### Frame 6 — `special_centrao_pull` (Centrao Gravitacional)
- **Position:** 576,480 to 671,575
- **Action:** BolsoLula raises all 4 arms upward. A gravitational pull effect: swirl lines (1px, `#1A1A18`) spiral inward toward the body from all directions. Small enemy silhouettes (4x4px dark shapes) are being pulled inward along the spiral paths. Both faces show POWER — rare unified expression of dominance. The Caneta BIC hovers above, spinning slowly, acting as the gravitational center.
- **Effect Indicator:** Circular dashed line (orbit path) around BolsoLula at ~40px radius.

#### Frame 7 — `special_centrao_orbit` (Centrao Gravitacional)
- **Position:** 672,480 to 767,575
- **Action:** Enemies now ORBIT around BolsoLula like satellites. 4-6 small enemy sprites (4x4px) circle at various distances. Both faces look smugly satisfied. All 4 arms conduct the orbiting enemies like orchestra conductors. The Caneta BIC signs emendas mid-air that float to the orbiting enemies (tiny paper bits, 2x2px, traveling outward along orbit paths).
- **Visual:** Resembles a political solar system with BolsoLula as the corrupt gravitational center.

---

### SET 7: FUSION SEQUENCE (10 frames) — `bolsolula_fusion`
**Loop:** No | **Frame Rate:** 8 fps (frames 0-5), 6 fps (frames 6-9 for drama) | **Sheet Position:** Row 6-7

> This sequence plays ONCE when the boss first appears. Lula and Bolsonaro collide and merge.
> PRE-REQUISITE: Lula (32x48px, entering from left) and Bolsonaro (32x48px, entering from right) sprites must be on screen.

#### Frame 0 — `fusion_approach`
- **Position:** 0,576 to 95,671
- **Description:** Both characters visible as SEPARATE entities within the 96x96 frame. Lula on far left (~24px from left edge), Bolsonaro on far right (~24px from right edge). Gap between them: ~48px. Both running toward center. Lula: red terno, cranial scar, 4-finger hand reaching forward. Bolsonaro: green-yellow/orange, enormous chin, both hands reaching forward. Their expressions: confused rage — they hate each other but are drawn together by unseen force.
- **Effect:** Green gas tendrils (`#4A7C59`, 1px wavy lines) connect from the Congresso (implied off-screen above) to both characters, pulling them together.

#### Frame 1 — `fusion_collision`
- **Position:** 96,576 to 191,671
- **Description:** IMPACT. The two bodies collide at center of frame. A massive starburst (16x16px, white `#FFFFFF` at 80% opacity) at the collision point. Both bodies deform on impact — Lula's right side compresses, Bolsonaro's left side compresses. Their reaching hands have OVERLAPPED — fingers interlocking involuntarily. Shockwave ring (2px, `#F0C830`) expands outward from collision point.
- **Particles:** Debris — fabric scraps (red + green, 2x2px, 6-8 particles) fly outward. A suit button (1px) pings off.
- **Screen Effect Note:** Game should apply 50ms screen shake here.

#### Frame 2 — `fusion_merge_start`
- **Position:** 192,576 to 287,671
- **Description:** The bodies BEGIN to merge. Skin at the contact point is melting/fusing — Lula's right arm sinks INTO Bolsonaro's left arm. The two faces are pressing together, cheek-to-cheek, both eyes wide with horror. The starburst fades. In its place: a pulsing organic mass (12x12px, blending their skin tones with `#8B3030` muscle exposed) at center. Both characters' legs tangle and begin to merge at the thighs.
- **Body Horror Detail:** Small tendrils of flesh (1px lines in skin tone) reach across from one body to the other, like biological magnets. The green gas is being ABSORBED into the fusion point.
- **Expressions:** PURE HORROR. Both faces screaming. This is NOT willing.

#### Frame 3 — `fusion_body_horror_1`
- **Position:** 288,576 to 383,671
- **Description:** 50% merged. The torso is now ONE mass but still visibly two different textures/colors fighting for dominance. The skin ripples (wavy edge on the forming seam line, 2px amplitude). TWO extra arms are budding from the sides — the fusion is creating additional limbs from the overlapping arm tissue. Lula's cranial scar EXTENDS across the forming shared skull. Bolsonaro's chin GROWS as it merges with Lula's jaw.
- **Horror Details:** A tooth (1px white) falls from the morphing jaw. An eye (3x3px) briefly appears on the chest (wrong place) before being reabsorbed. Spine visible through the back skin (1px bumps).
- **Color:** The fusion point churns through both color palettes rapidly — flickering between red and green undertones.

#### Frame 4 — `fusion_body_horror_2`
- **Position:** 384,576 to 479,671
- **Description:** 75% merged. The body shape is close to final BolsoLula but still UNSTABLE. The seam line is forming but not yet stitched — raw exposed flesh down the center. The 4 arms are distinct now but WRONG — arms swap sides briefly (Lula arm on Bolsonaro side), then snap to correct positions. The fused head takes shape: two profiles forced into one front-facing skull. The cranial scar now runs across both halves.
- **Stitches Begin:** The first Frankenstein stitch materializes at the collar (appears with a tiny flash, 1px, `#F0C830`). Then a second at the waist. The stitches are the body's desperate attempt to hold itself together.
- **Sound Note:** A wet, cracking sound should accompany this frame.

#### Frame 5 — `fusion_stitching`
- **Position:** 480,576 to 575,671
- **Description:** 90% merged. Stitches rapidly appear along the seam: 1 at frame start, 5 by frame end, materializing top-to-bottom with small flashes. The Frankenstein bolt PUNCHES through the collarbone from inside (pushes outward with a small ring of displaced skin). The body proportions settle into final form. Both faces have stopped screaming and now show EXHAUSTED RESIGNATION.
- **Arms:** All 4 arms test their range of motion — flex, extend, grip. The lower arms discover the Caneta BIC (which materialized from the fusion of Lula's pen and Bolsonaro's pen — merged like the bodies).

#### Frame 6 — `fusion_stabilize`
- **Position:** 576,576 to 671,671
- **Description:** The fusion is COMPLETE but unstable. The full BolsoLula body is now at final proportions (filling the 96x96 frame properly). The seam is fully stitched but still glowing (`#8B3030` at 30% opacity along the seam). Small aftershock tremors — the body vibrates 1px left-right-left. Both faces blink independently (Lula blinks first, then Bolsonaro 100ms later).
- **Residual Particles:** Last few flesh particles (1x1px) settle. Green gas wisps dissipate. The starburst is completely gone.

#### Frame 7 — `fusion_first_look`
- **Position:** 672,576 to 767,671
- **Description:** BolsoLula looks down at itself for the first time. Both faces angle downward. All 4 arms are held outward in front, fingers splayed, examining themselves. Lula face: horrified recognition. Bolsonaro face: confused anger. The body has a subtle convulsion (1px vertical jitter) as the two nervous systems conflict.
- **Detail:** A small mirror shard (3x3px, reflective highlight) on the ground shows a tiny distorted reflection of the fused face — player can see both profiles in the reflection.

#### Frame 8 — `fusion_first_words`
- **Position:** 768,576 to 863,671
- **Description:** BolsoLula speaks for the first time. TWO speech bubbles emerge simultaneously: LEFT bubble (red border): "Com...panheiro?" RIGHT bubble (green border): "...talkei?" Both are uncertain, questioning. The mouths move out of sync — Lula mouth moves first, Bolsonaro mouth follows 1 frame behind. All 4 arms drop to sides in defeated acceptance.
- **Posture:** The body straightens to full height. The shadow beneath sharpens. This is the boss becoming REAL.

#### Frame 9 — `fusion_battle_ready`
- **Position:** 864,576 to 959,671
- **Description:** FINAL FUSION FRAME. BolsoLula snaps into battle stance. Both faces shift to RAGE simultaneously. Upper arms raise fists. Lower arms grip the Caneta BIC in combat position. One foot (Lula's) steps forward. The other foot (Bolsonaro's) plants. The fusion seam PULSES once (bright flash along entire seam, `#F0C830` at 40% opacity) — the monster has accepted what it is.
- **Transition:** This frame holds for 500ms, then transitions directly to `idle` animation.
- **Boss HP Bar:** Should appear during this frame.

---

### SET 8: SPLIT SEQUENCE / FUSAO REVERSA (8 frames) — `bolsolula_split`
**Loop:** No | **Frame Rate:** 8 fps (frames 0-3), 6 fps (frames 4-7) | **Sheet Position:** Row 8

> This is the ULTIMATE ability. BolsoLula splits into two separate bosses for 15 seconds of chaos.

#### Frame 0 — `split_strain`
- **Position:** 0,768 to 95,863
- **Description:** BolsoLula grabs its own body — Lula arms pull LEFT, Bolsonaro arms pull RIGHT. Both faces grimace with effort. The fusion seam GLOWS intensely (`#F0C830` at 80% opacity). Stitches strain visibly — threads going taut, small gaps appearing between skin and thread. The Frankenstein bolt vibrates (2px motion blur). The Caneta BIC is clenched in teeth (the fused mouth bites it in half).
- **Energy:** Crackling energy (zigzag lines, 1px, alternating red/green) along the entire seam.

#### Frame 1 — `split_stitches_snap`
- **Position:** 96,768 to 191,863
- **Description:** Stitches BREAK in sequence — top-to-bottom, each one snapping with a small spark (1px, `#F0C830`). Thread fragments (1px lines) fly outward. The seam opens 8px wide — the dark void inside is now visible as a pulsing mass of red AND green energy fighting each other. Both halves are pulling apart but still connected at the hips and head.
- **Flesh Detail:** Muscle fibers stretch across the gap like rubber bands. 2-3 snap with tiny red splashes (1x1px).
- **Expressions:** Both faces show DETERMINATION mixed with PAIN.

#### Frame 2 — `split_halfway`
- **Position:** 192,768 to 287,863
- **Description:** HALF SPLIT. Connected only at head and one leg. The torso gap is now 16px. Inside the gap: a miniature political campaign in progress — tiny red and green banners (1px each) being torn apart. The Frankenstein bolt falls out (small metallic object dropping, 3x3px). Each half has pulled 2 arms free — Lula half has both left arms, Bolsonaro half has both right arms.
- **Head:** The skull is the last major connection. The cranial scar line is the fault line — it glows white-hot.

#### Frame 3 — `split_head_divide`
- **Position:** 288,768 to 383,863
- **Description:** THE HEAD SPLITS. This is the most dramatic frame. A vertical crack runs down the center of the fused skull. The two faces separate with a FLASH (full-frame white at 40% opacity for 1 game-frame). Lula's left-profile face emerges. Bolsonaro's right-profile face emerges. Both faces are briefly visible in profile as they pull apart, connected by the last strand of the cranial scar tissue.
- **Central Flash:** Large starburst (24x24px, `#FFFFFF` at 70% opacity) at the point of final separation.
- **Sound Note:** A massive CRACK sound + dual screams.

#### Frame 4 — `split_separation`
- **Position:** 384,768 to 479,863
- **Description:** TWO SEPARATE ENTITIES. Lula (left half, now ~48x96px within the frame) stumbles to the left. Bolsonaro (right half, now ~48x96px) stumbles to the right. Each has 2 arms (one upper, one lower). Each has one complete face (but the seam side is raw — exposed muscle, dangling stitches). Each holds half of the broken Caneta BIC (Lula: red half, Bolsonaro: green half).
- **Residue:** Stitching threads trail from both halves. Small particles of fused tissue fall between them.
- **Expressions:** Lula: free but confused. Bolsonaro: free but enraged.

#### Frame 5 — `split_regenerate`
- **Position:** 480,768 to 575,863
- **Description:** Each half REGENERATES. New tissue grows over the exposed seam side: Lula's right side fills in with his skin tone and a partial red terno. Bolsonaro's left side fills in with his skin tone and partial green/orange uniform. Each regrows a 2nd arm (budding outward, small at first). The regeneration is IMPERFECT — scars, miscolored patches, asymmetry.
- **Visual:** Rapid tissue growth shown as expanding pixels: 2px of new skin per visible area, rough edges.

#### Frame 6 — `split_two_bosses`
- **Position:** 576,768 to 671,863
- **Description:** FULLY SPLIT. Two distinct entities now occupy the frame. LEFT: Lula (~44x90px) — full body, both arms, wielding red Caneta half like a dagger. Presidential terno torn, cranial scar prominent, 4 fingers visible. RIGHT: Bolsonaro (~44x90px) — full body, both arms, wielding green Caneta half like a club. Prison jumpsuit/selecao shirt torn, enormous chin, military posture.
- **Between them:** 8px gap. Electrical arcs (1px, `#F0C830`) still connect them — they can't fully separate.
- **Key Detail:** They are already turning to face EACH OTHER, not the player. The rivalry kicks in immediately.

#### Frame 7 — `split_chaos_begin`
- **Position:** 672,768 to 767,863
- **Description:** CHAOS STARTS. Both bosses lunge at each other AND at the player simultaneously. Lula swings left with red Caneta half. Bolsonaro charges right with green Caneta half. But their trajectories cross — they'll hit each other as much as the player. Motion lines (2px each) trail from both. Expressions: PURE UNDILUTED RAGE at each other. 
- **Indicator:** A visible timer appears (HUD element, not sprite): "15" in `#F0C830` text, counting down to re-fusion.
- **End Note:** After 15 seconds of separate AI, play `fusion` sequence in reverse (or a shortened 4-frame re-merge) to recombine.

---

## Sprite Sheet Summary

| Set | Animation | Frames | Row | Frame Size | Total Width |
|---|---|---|---|---|---|
| 1 | Idle | 4 | 0 | 96x96 | 384px |
| 2 | Walk | 6 | 1 | 96x96 | 576px |
| 3 | Attack | 3 | 2 | 96x96 | 288px |
| 4 | Death | 4 | 3 | 96x96 | 384px |
| 5 | Hit | 2 | 4 | 96x96 | 192px |
| 6 | Special | 8 | 5 | 96x96 | 768px |
| 7 | Fusion | 10 | 6-7 | 96x96 | 960px |
| 8 | Split | 8 | 8 | 96x96 | 768px |
| **TOTAL** | | **45** | | | |

> Note: 8 additional directional variants (N, NE, E, SE, S, SW, W, NW) may be needed for Walk and Idle. If implemented, multiply Walk and Idle frames by 8 = (4+6)*8 = 80 directional frames. For MVP, use only S-facing (default) and flip horizontally for E/W.

## Phaser 3 Atlas Key
```json
{
  "key": "boss_bolsolula",
  "frameWidth": 96,
  "frameHeight": 96,
  "margin": 0,
  "spacing": 0
}
```

## Phaser 3 Animation Config
```javascript
// Idle
this.anims.create({
  key: 'bolsolula_idle',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 0, end: 3 }),
  frameRate: 8,
  repeat: -1
});

// Walk
this.anims.create({
  key: 'bolsolula_walk',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 4, end: 9 }),
  frameRate: 10,
  repeat: -1
});

// Attack
this.anims.create({
  key: 'bolsolula_attack',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 10, end: 12 }),
  frameRate: 10,
  repeat: 0
});

// Death
this.anims.create({
  key: 'bolsolula_death',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 13, end: 16 }),
  frameRate: 6,
  repeat: 0
});

// Hit
this.anims.create({
  key: 'bolsolula_hit',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 17, end: 18 }),
  frameRate: 12,
  repeat: 0
});

// Special (varies per skill)
this.anims.create({
  key: 'bolsolula_special_polarizacao',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 19, end: 20 }),
  frameRate: 8,
  repeat: 0
});

this.anims.create({
  key: 'bolsolula_special_palanque',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 21, end: 22 }),
  frameRate: 8,
  repeat: 0
});

this.anims.create({
  key: 'bolsolula_special_debate',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 23, end: 24 }),
  frameRate: 8,
  repeat: 0
});

this.anims.create({
  key: 'bolsolula_special_centrao',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 25, end: 26 }),
  frameRate: 8,
  repeat: 0
});

// Fusion Sequence
this.anims.create({
  key: 'bolsolula_fusion',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 27, end: 36 }),
  frameRate: 8,
  repeat: 0
});

// Split Sequence (Ultimate)
this.anims.create({
  key: 'bolsolula_split',
  frames: this.anims.generateFrameNumbers('boss_bolsolula', { start: 37, end: 44 }),
  frameRate: 8,
  repeat: 0
});
```

## Notes for Artist
1. BolsoLula must look like a MISTAKE OF NATURE — two politicians forced into one grotesque body by corrupt supernatural forces
2. The fusion seam is the visual centerpiece. It should be DISGUSTING: stitches, exposed muscle, mismatched skin, Frankenstein bolts. Never clean or symmetrical.
3. The 4 arms must each have PERSONALITY: Lula's arms are stubby and gesture like a comicio speaker. Bolsonaro's arms are rigid and gesture like a military officer.
4. Both faces express DIFFERENT emotions in EVERY frame (except the rare unified moments: confusion in idle_3, death horror, battle stance)
5. Color contamination: some red should bleed into Bolsonaro's side at the seam, some green should bleed into Lula's side. The corruption goes both ways.
6. The Caneta BIC Gigante is the size of a baseball bat. It's absurd. The BIC logo should be barely visible (parody, not trademark).
7. The 2026 update (prison jumpsuit on Bolsonaro side) makes the visual asymmetry even MORE extreme: presidential formal vs prison casual.
8. SCALE: BolsoLula at 96x96 should be visibly LARGER than any regular 64x64 character. This is a boss. It dominates the screen.
9. Every frame should look like it was drawn by someone who is ANGRY at both politicians equally.
10. If any frame looks "cool" or "badass" in a flattering way, it is WRONG. This character is pathetic, grotesque, and darkly funny.
