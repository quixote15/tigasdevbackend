# BOLSONARO (O Mito) -- Skin Variants

## Skin System Overview
- **Base Resolution:** 64x64px per frame
- **Skin Method:** Full sprite sheet replacement (each skin is a complete set of all animation sheets)
- **Palette Swap Optimization:** Skins 1-3 share the same silhouette/pose; only colors and accessories differ. Skins 4-6 have modified silhouettes.
- **Atlas Budget:** Each skin variant adds ~59 frames. Total atlas budget per skin: ~256x64 to 512x64 per animation.
- **Unlock System:** See per-skin notes for unlock conditions.

---

## SKIN 1: "Camisa da Selecao" (DEFAULT)

### Description
The default Bolsonaro skin. The classic yellow jersey of the Brazilian national team, dirty and grimy, with the presidential sash over it. This is the "rally Bolsonaro" -- the populist at a motociata, the man who appropriated the national team jersey as a political uniform.

### Color Palette
| Element              | Hex Code  | Notes                                      |
|----------------------|-----------|--------------------------------------------|
| Jersey Base          | `#FFD700` | Dirty golden-yellow, NOT clean canary      |
| Jersey Shadow        | `#CCAA00` | Darker folds, pit stains, grime            |
| Jersey Highlight     | `#FFE44D` | Stretched over belly, collar               |
| Jersey Collar/Trim   | `#006400` | Green trim, slightly faded                 |
| Number "17"          | `#006400` | Back of jersey, faded/peeling              |
| Shorts               | `#1A3A5C` | Dark blue, official CBF                    |
| Sash Green           | `#006400` | Presidential sash verde                    |
| Sash Yellow          | `#FFD700` | Presidential sash amarelo                  |
| Skin/Gun/Accessories | Standard  | See main sprite-spec.md palette            |

### Unique Visual Details
- Jersey is TOO TIGHT -- belly flesh visible underneath stretching the fabric
- Sweat stains under arms (darker yellow circles, 2x2px)
- Number "17" on back partially peeling off (when viewed from certain angles)
- The jersey is a size too small -- seams visible straining at the sides
- Knee-length dark blue shorts, white stripe on side
- Soccer cleats instead of dress shoes (white cleats with green laces, dirty)

### Unlock Condition
- Default skin, available from the start.

---

## SKIN 2: "Terno Presidencial" (Formal)

### Description
Bolsonaro in his official presidential attire. Dark suit, white shirt, conservative tie, presidential sash. This is the "institutional Bolsonaro" -- except the suit never quite fits right, the tie is always slightly crooked, and he looks fundamentally uncomfortable in formal wear. Like a military man shoved into civilian costume.

### Color Palette
| Element              | Hex Code  | Notes                                      |
|----------------------|-----------|--------------------------------------------|
| Suit Jacket          | `#1A1A2E` | Near-black dark blue, conservative         |
| Suit Shadow          | `#0D0D1A` | Deep folds, under arms                     |
| Suit Highlight       | `#2A2A3E` | Shoulder, lapel edges (subtle)             |
| Shirt White          | `#F0EDE5` | Off-white, slightly yellowed               |
| Shirt Shadow         | `#D4D0C8` | Collar folds, under jacket                 |
| Tie                  | `#8B0000` | Dark red, conservative, slightly crooked   |
| Tie Pin              | `#DAA520` | Gold pin with Brazil coat of arms          |
| Suit Pants           | `#1A1A2E` | Matching jacket                            |
| Dress Shoes          | `#0D0D0D` | Black, slightly scuffed                    |
| Sash Green           | `#006400` | Presidential sash (more prominent here)    |
| Sash Yellow          | `#FFD700` | Presidential sash                          |
| Lapel Pin            | `#009B3A` | Small Brazil flag pin on left lapel        |

### Unique Visual Details
- Suit is clearly uncomfortable on him -- shoulders slightly hunched, collar too tight
- Tie ALWAYS crooked (tilted 5-10 degrees off-center)
- Shirt buttons strain over belly -- gap visible between middle buttons showing skin/scar
- Jacket cannot close over belly -- always open, sash visible underneath
- Gold presidential cufflinks (tiny 1px gold squares at wrists)
- Military posture fighting against civilian clothing -- stiff, unnatural
- The suit jacket is slightly too short -- wrists visible past sleeve ends
- One jacket pocket has a pen (1px dark blue line sticking out)

### Unique Animation Modifications
- **Walk:** Stiffer, more rigid (military muscle memory in civilian clothes)
- **Idle:** Pulls at collar occasionally (extra idle frame variant: hand at throat, uncomfortable)
- **Attack:** Jacket flaps open during gun draw, fully exposing belly scar
- **Death:** Tie detaches and flutters down separately (extra accessory physics)

### Unlock Condition
- Complete Act 1 (waves 1-5) on any difficulty.

---

## SKIN 3: "Bolsonaro de Cela" (2026 PRESO) -- FEATURED SKIN

### Description
The 2026 UPDATE skin. Bolsonaro condenado a 27 anos. PRESO. Orange prison uniform, wrinkled and ill-fitting. Same forced grin but now with dark circles under the eyes. Prison bars overlaid on certain frames. Doing lives from a hidden phone in his pocket. This is the DEFINITIVE 2026 version -- the man who tried to overthrow democracy and is now livestreaming from a cell.

### Color Palette
| Element              | Hex Code  | Notes                                      |
|----------------------|-----------|--------------------------------------------|
| Jumpsuit Orange      | `#FF6600` | Prison orange, institutional               |
| Jumpsuit Shadow      | `#CC5500` | Folds, wrinkles, shadows                   |
| Jumpsuit Highlight   | `#FF8833` | Stretched over belly, shoulders            |
| Jumpsuit Stripe      | `#CC5500` | Darker horizontal stripes (prison pattern) |
| Number Patch         | `#1A1A1A` | "2027-0001" in white text on chest pocket  |
| Collar/Cuffs         | `#CC5500` | Darker trim on collar and sleeve cuffs     |
| Prison Shoes         | `#4A4A4A` | Gray institutional slip-ons                |
| Ankle Monitor        | `#333333` | Dark gray electronic monitor on left ankle |
| Monitor LED          | `#FF0000` | Blinking red LED on ankle monitor          |
| Prison Bars          | `#808080` | Foreground overlay, 3 vertical bars        |
| Prison Bars Shadow   | `#505050` | Bar shadows                                |
| Dark Circles         | `#8B7355` | Under-eye circles (sleepless in prison)    |
| Stubble              | `#3A3028` | 5 o'clock shadow (no barber access)        |
| Hidden Phone Glow    | `#4488FF` | Glow through pocket fabric                 |

### Unique Visual Details
- Orange jumpsuit WRINKLED and ill-fitting (too big in some places, too tight over belly)
- "COMPLEXO PENITENCIARIO DE PAPUDA" faintly visible on the back (if sprite detail allows, otherwise just implied)
- Prisoner number "2027-0001" on chest pocket in white stencil
- NO presidential sash (confiscated) -- replaced by wrinkled jumpsuit collar
- NO sunglasses on head (confiscated) -- replaced by messy uncombed hair
- Dark circles under eyes (2px darker skin patches)
- 5 o'clock shadow (stippled gray-brown dots on lower face/chin area)
- Ankle monitor on left ankle with BLINKING RED LED (1px red, 0.5Hz blink)
- The golden revolver is HIDDEN -- pulled from under the mattress during attacks (implied)
- Phone ALWAYS hidden -- glow through pocket fabric visible during idle
- Belly scar MORE prominent (prison uniform is thinner fabric, scar shows through)
- Prison bars overlay on idle and walk (foreground layer, 3 vertical gray lines, 20% opacity)

### Unique Animation Modifications
- **Idle:** Occasionally glances around nervously (eyes dart left-right). Phone pocket glow pulses. Ankle monitor LED blinks. Scratches stubble.
- **Walk:** Shuffle instead of strut (prison slippers, no more boots). Ankle monitor visible. Speed reduced 10%.
- **Attack:** Gun pulled from UNDER something (hidden contraband animation -- furtive reach, then draw). 50ms longer draw time.
- **Hit:** Prison bars rattle (bar sprites shake +/-1px for 200ms on hit). Orange fabric ripples.
- **Death:** Falls against prison bars. Ankle monitor beeps rapidly. Phone slides out of pocket, screen shows "LIVE ENDED -- CONNECTION LOST".
- **Special (Live da Cela):** THIS SKIN was designed for this special. Prison bars prominent in foreground. Phone hiding/revealing extra dramatic. Guard footstep sounds in background (tension).
- **Special (Golpe Frustrado):** Eduardo appears OUTSIDE the bars, running in the prison yard. Even more pathetic.
- **Ultimate (Motociata):** Motorcycle appears INSIDE the cell (impossible, comedic). He rides it into the bars, which break. Ghost motos are ghost prisoners on ghost motos.

### Unlock Condition
- Reach the Bolsonaro boss fight in Act 3 (2026 storyline). Automatically applied during the prison chapter boss encounter.
- Also unlockable: defeat Bolsonaro boss fight on Hard difficulty.

---

## SKIN 4: "Zombie Premium" (Undead Bolsonaro)

### Description
Bolsonaro fully infected by the Emenda 666 virus. Zombie politician. Green-tinged skin, rotting suit, one eye hanging out, jaw unhinged (chin somehow EVEN BIGGER now that it's not attached properly). The forced grin is now permanent because the face muscles are locked in rigor mortis. This is the HORROR version -- black comedy through zombification of an already grotesque character.

### Color Palette
| Element              | Hex Code  | Notes                                      |
|----------------------|-----------|--------------------------------------------|
| Zombie Skin Base     | `#6B8E5B` | Green-gray dead flesh                      |
| Zombie Skin Shadow   | `#4A6B3D` | Deeper rot, darker patches                 |
| Zombie Skin Highlight| `#8BAE7B` | Exposed bone, stretched skin               |
| Rot Patches          | `#3D5C2E` | Dark green rot spots, scattered            |
| Bone White           | `#E8E0D0` | Exposed cheekbone, finger bones            |
| Blood Dark           | `#4A0000` | Dried old blood, dark stains               |
| Blood Fresh          | `#8B0000` | Fresh wounds, still oozing                 |
| Torn Suit            | `#1A1A2E` | Remnants of terno presidencial, torn       |
| Torn Suit Exposed    | `#6B8E5B` | Where suit is torn, zombie skin visible    |
| Eye Glow             | `#CCFF00` | One eye yellow-green glow (undead)         |
| Eye Socket Empty     | `#1A0000` | Other eye socket -- empty/dangling         |
| Jersey Fragments     | `#998800` | Dirty yellow jersey fragments mixed in     |
| Sash Rotted          | `#003300` | Presidential sash, rotted and torn         |
| Teeth Yellow         | `#C8B050` | Yellowed, some missing, permanent grin     |
| Hair Patchy          | `#2C1810` | Hair falling out in patches                |
| Maggot White         | `#F0F0E0` | Tiny maggot detail in wounds (1px)         |

### Unique Visual Details
- Skin is GREEN-GRAY with visible rot patches (dark green spots, 2x2px, random placement)
- ONE EYE glowing yellow-green (undead), the other eye socket empty or dangling
- JAW UNHINGED -- chin is now 5x normal instead of 4x (even bigger because it's disconnected)
- Permanent forced grin: muscles locked in rigor mortis, teeth yellowed with gaps
- Suit in tatters: half terno presidencial, half exposed zombie flesh
- Presidential sash rotted and torn, barely recognizable
- Exposed rib cage on one side (where scar was -- now fully open wound)
- Knife scar has OPENED into a gaping wound (visible intestines? or just darkness inside)
- Hair falling out in patches (bald spots with visible scalp, green-tinged)
- Fingers: some are bone-only (1px white tips on hands)
- Gun is RUSTED (golden color faded to #8B7840, brown-orange rust spots)
- Maggots: 1-2 tiny white pixels moving slowly in wound areas
- Dragging one foot (limp animation)

### Unique Animation Modifications
- **Idle:** Jaw clacks open/shut randomly (chin drops 2px, rises 2px, 500ms interval). Eye glow pulses. Occasional maggot drops from body (1px white, gravity fall).
- **Walk:** SHAMBLE not strut. Dragging left foot (asymmetric walk cycle). Head tilts at odd angle. Speed reduced 20%. Leaves trail of dark spots (blood drips).
- **Attack:** Gun rust makes it jam MORE often (40% fail rate instead of 30%). Gun droop on fail is accompanied by rust flakes falling.
- **Hit:** Zombie flesh deforms differently -- squish instead of recoil. Green blood particles instead of red. A piece of suit might detach.
- **Death:** Body DECOMPOSES instead of just falling. Melts into a puddle of verde goo over 2000ms. Final frame is a green puddle with the rusted gun, a shoe, and the sash floating on top. Maggots scatter.
- **Special effects:** All green-yellow color scheme instead of golden.

### Unlock Condition
- Complete the game on Normal difficulty.
- Alternative: find all "Fragmento de Documento" collectibles in Acts 1-2.

---

## SKIN 5: "Camuflado Militar" (Military)

### Description
Bolsonaro in his fantasy military persona. Full camouflage fatigues, military beret, combat boots, multiple medals that he didn't earn. This is the "military man" self-image -- the captain who never saw combat but never shuts up about the army. The uniform is covered in absurdly oversized medals, stars, and pins that he clearly gave himself.

### Color Palette
| Element              | Hex Code  | Notes                                      |
|----------------------|-----------|--------------------------------------------|
| Camo Green Light     | `#5B7744` | Camouflage pattern -- light                |
| Camo Green Dark      | `#3B5224` | Camouflage pattern -- dark                 |
| Camo Brown           | `#6B5B3A` | Camouflage pattern -- earth                |
| Camo Black           | `#2A2A1A` | Camouflage pattern -- shadow               |
| Beret Green          | `#2E4420` | Military beret (replaces sunglasses slot)  |
| Beret Badge          | `#DAA520` | Gold badge on beret                        |
| Boot Black           | `#1A1A0A` | Heavy military combat boots                |
| Boot Sole            | `#3A3A2A` | Thick boot soles (add 2px height)          |
| Medal Gold           | `#DAA520` | Self-awarded medals (5+ on chest)          |
| Medal Silver         | `#C0C0C0` | Additional medals                          |
| Medal Ribbon Red     | `#8B0000` | Medal ribbons                              |
| Medal Ribbon Blue    | `#00008B` | Medal ribbons                              |
| Belt Utility         | `#4A4A2A` | Military utility belt with pouches         |
| Rank Stars           | `#FFD700` | Self-promoted star rank on collar (5 stars)|
| Holster Leather      | `#5C3A1E` | Hip holster for the golden revolver        |
| Dog Tags             | `#C0C0C0` | Military dog tags around neck              |

### Unique Visual Details
- Full camouflage pattern (4-color camo, pixel pattern across all fabric)
- Military beret (replaces sunglasses on head) with oversized gold badge
- ABSURD number of medals: 5-7 medal sprites on chest, overlapping, oversized. He clearly gave these to himself
- Self-promoted rank: 5-star general collar insignia (Brasil has no 5-star generals in peacetime -- he made it up)
- Military combat boots add 2px to height (taller sprite variant)
- Utility belt with pouches (mystery contents)
- Dog tags around neck (visible above collar)
- NO presidential sash (replaced by military decoration across chest)
- Belly scar partially covered by medals but still visible underneath
- Beret sits slightly wrong on his head (cocked to one side, not proper military angle)
- One medal is clearly a bottle cap spray-painted gold (1px detail, comedic)
- Ammo bandolier across chest (despite using a revolver -- overkill decoration)

### Unique Animation Modifications
- **Idle:** Rigid military "at ease" stance. Occasionally snaps to salute (hand to beret). Medals clink (small movement, 1px oscillation on medal sprites). More serious expression (still forced, but trying to look tough instead of grinning).
- **Walk:** MARCH instead of strut. More rigid, arms swing precisely. Combat boots make louder step sounds. Medals bounce and clink with each step.
- **Attack:** Military draw from hip holster (different angle than cowboy draw). Slightly more competent-looking aim (but same 70/30 success/fail rate). On success: military shout instead of grin. On fail: medals fall off from gun malfunction vibration.
- **Death:** Falls like a soldier (stiffer fall). Beret falls off first. Medals scatter on impact (each medal is a separate physics object, 5-7 gold pixels bouncing). Final frame: face down, one hand still reaching toward beret.
- **Special (Golpe Frustrado):** In this skin, the military salute is EXTRA elaborate (longer wind-up). Eduardo still appears and fails, but Eduardo is in a child-sized military costume (even more pathetic).
- **Ultimate (Motociata):** Military Jeep instead of Harley (re-skinned vehicle). Ghost motos become ghost military trucks. Camo colored effects instead of verde-amarelo.

### Unlock Condition
- Reach Wave 15 (late Act 2) without dying.
- Alternative: defeat 100 enemies with the "Arma que Brocha" weapon.

---

## SKIN 6: "O Mito Dourado" (Legendary / Gold)

### Description
The ULTIMATE meme skin. Bolsonaro as his supporters see him -- literally made of gold. Golden skin, golden suit, golden everything. The "Mito" deified. A walking golden idol with an absurdly oversized golden chin. Crown instead of sunglasses. Cape instead of faixa. This is the satirical apotheosis -- what happens when a cult of personality is taken to its literal visual extreme. It's tacky, it's garish, it's EXACTLY the kind of thing that would be sold as a golden statuette at a political rally.

### Color Palette
| Element              | Hex Code  | Notes                                      |
|----------------------|-----------|--------------------------------------------|
| Gold Skin Base       | `#DAA520` | Golden flesh                               |
| Gold Skin Shadow     | `#8B6914` | Golden flesh shadows                       |
| Gold Skin Highlight  | `#FFD700` | Golden flesh highlights                    |
| Gold Suit            | `#B8860B` | Darker gold for suit distinction           |
| Gold Suit Shadow     | `#856000` | Suit fold shadows                          |
| Gold Suit Highlight  | `#FFD700` | Suit highlights, lapels                    |
| Crown Gold           | `#FFD700` | Crown on head (replaces sunglasses)        |
| Crown Jewel Red      | `#FF0000` | Ruby on crown                              |
| Crown Jewel Green    | `#00FF00` | Emerald on crown (Brazil colors)           |
| Crown Jewel Blue     | `#0000FF` | Sapphire on crown                          |
| Cape Green           | `#006400` | Royal cape (replaces faixa)                |
| Cape Inner Gold      | `#FFD700` | Cape inner lining                          |
| Specular White       | `#FFFFFF` | Bright specular highlights (metallic look) |
| Gun Platinum         | `#E5E4E2` | Platinum revolver (upgrade from gold)      |
| Eye Glow White       | `#FFFFCC` | Eyes glow warm white                       |

### Unique Visual Details
- ENTIRE CHARACTER is gold-toned -- skin, clothes, hair, everything
- Crown on head with 3 gems (red, green, blue -- tacky patriotic crown)
- Royal cape instead of presidential sash (verde outer, gold inner lining)
- Platinum revolver instead of golden (because gold wasn't enough)
- Eyes have a warm white glow (divine light parody)
- Every surface has specular highlights (1-2px white dots, metallic sheen)
- Golden particles orbit the character at all times (4 gold 1px pixels, slow orbit)
- Footsteps leave golden footprints that fade (3s lifespan)
- The forced grin has GOLDEN teeth (every tooth a gold pixel)
- Chin is POLISHED GOLD -- shinier than the rest (extra highlights)
- Belly scar is also golden but still visibly a scar (golden keloid)
- The overall effect should look like a CHEAP GOLDEN STATUETTE -- not elegant gold, but GAUDY rally-merchandise gold

### Unique Animation Modifications
- **All animations:** Golden particle trail. Every movement leaves a brief golden sparkle (1px, 100ms lifespan, 3 per frame).
- **Idle:** Crown glints periodically (2px white starburst on crown, every 2s). Cape billows dramatically (more wind than other skins). Slow rotation sparkle across body (specular highlight moves).
- **Walk:** Leaves golden footprints (2x2px gold sprites, alpha 1.0->0.0 over 3000ms). Each step produces a "clink" sound (metallic, golden).
- **Attack:** Platinum gun has BIGGER muzzle flash (golden-white, 14x14px instead of 12x12px). On fail, gun tarnishes briefly (gold becomes dark for 500ms).
- **Hit:** Golden sparks fly instead of sweat drops. Ring-like metallic sound on impact. Dents appear (1px darker gold, persistent for 3s).
- **Death:** Statue CRUMBLES. Instead of falling like a person, cracks appear (dark gold lines spreading across body over 400ms), then pieces break off (8-12 gold chunks, physics objects). Final frame: pile of golden rubble with the crown sitting on top, gems still glinting. No blood -- just broken gold.
- **Special (Invulnerable):** PLATINUM aura instead of golden. Even more absurd glowing. Text "IMORRIVEL" etc. in platinum.
- **Ultimate (Motociata):** Golden Harley becomes PLATINUM Harley. Ghost motos are golden (not green). Crash scatters golden coins instead of debris.

### Unlock Condition
- Secret unlock: complete the game on Hard difficulty without using any continues.
- Alternative: collect all skins 1-5 first.
- Meta-unlock: achieve a score above 1,000,000 in endless mode.

---

## SKIN COMPARISON MATRIX

| Feature              | Selecao (1) | Terno (2) | Preso (3) | Zombie (4) | Militar (5) | Mito Gold (6) |
|----------------------|-------------|-----------|-----------|------------|-------------|----------------|
| **Primary Color**    | Yellow      | Dark blue | Orange    | Green-gray | Camo        | Gold           |
| **Headwear**         | Sunglasses  | Sunglasses| Messy hair| Patchy hair| Beret       | Crown          |
| **Torso Garment**    | Jersey      | Suit+shirt| Jumpsuit  | Torn suit  | Fatigues    | Gold suit      |
| **Sash/Chest**       | Faixa       | Faixa     | Number    | Rotted sash| Medals      | Cape           |
| **Footwear**         | Cleats      | Dress shoe| Slip-ons  | Dragging   | Boots       | Gold shoes     |
| **Gun Color**        | Gold        | Gold      | Gold(hide)| Russted    | Gold+holster| Platinum       |
| **Scar Visibility**  | High        | Medium    | High      | Open wound | Medal-cover | Golden scar    |
| **Walk Style**       | Strut       | Stiff     | Shuffle   | Shamble    | March       | Parade         |
| **Fail Rate**        | 30%         | 30%       | 30%       | 40%        | 30%         | 25%            |
| **Speed Modifier**   | 1.0x        | 0.95x     | 0.9x      | 0.8x       | 1.0x        | 1.0x           |
| **Special FX**       | Standard    | Standard  | Bars+LED  | Rot+maggot | Medal clink | Gold sparkle   |
| **Death Style**      | Ragdoll     | Stiff fall| Bars fall | Decompose  | Soldier fall| Crumble        |
| **Unlock**           | Default     | Act 1     | Act 3/Hard| Normal beat| Wave 15+    | Hard no-death  |

---

## SKIN SELECTION UI NOTES

### Preview Animation
- Each skin shows a 4-second preview loop: idle (2s) -> signature pose (2s)
- Signature poses per skin:
  1. Selecao: Thumbs up + jersey tug
  2. Terno: Adjusts crooked tie, fails
  3. Preso: Phone glow in pocket, paranoid glance
  4. Zombie: Jaw clacks, eye dangles
  5. Militar: Sharp salute, medals clink
  6. Mito Gold: Crown glint, golden particle burst

### Locked Skin Display
- Grayed out silhouette (desaturated to 20%)
- Lock icon overlay (16x16px padlock)
- Unlock requirement text on hover/tap
- Teaser: one frame visible in color (the most dramatic frame of each skin)

### Skin Swap In-Game
- Skins can be changed at checkpoint stations between waves
- Skin change triggers a 1s "costume swap" animation: character spins 360deg, dust cloud at 180deg, new skin visible at 360deg
- SFX: `costume_whoosh` + `costume_reveal`
