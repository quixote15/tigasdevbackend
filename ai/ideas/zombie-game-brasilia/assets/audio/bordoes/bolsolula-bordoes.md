# BOLSOLULA (Fusao) — Bordoes de Audio

## Voice Design — DUAL VOICE SYSTEM

BolsoLula has TWO simultaneous voices. They overlap, contradict, and interrupt each other. This is the core audio identity of the character.

### Lula Voice (Left Channel)
- **Timbre**: Grave, rouca, arrastada. Sotaque nordestino forte (Pernambuco).
- **Pace**: Lenta com pausas dramaticas. Tom de comicio permanente.
- **TTS Voice**: `pt-BR-AntonioNeural` (grave, masculina) — rate -15% para fala arrastada
- **Stereo**: Panned 70% LEFT
- **Alternative**: Voice actor imitando sotaque nordestino + rouquidao etilica

### Bolsonaro Voice (Right Channel)
- **Timbre**: Media-aguda, nasalada, agressiva. Sotaque carioca/paulista militar.
- **Pace**: Rapida, entrecortada, interjeicoes constantes ("talkei?", "ok?"). Tom de live no Facebook.
- **TTS Voice**: `pt-BR-FranciscoNeural` (media, masculina) — rate +10% para fala rapida e picotada
- **Stereo**: Panned 70% RIGHT
- **Alternative**: Voice actor imitando nasalidade + militarismo casual

### MIXING RULES
1. Both voices are ALWAYS present — even when one is "dominant", the other murmurs in the background (10% volume)
2. On "dominance switch" (every 5s), the dominant voice fades to 100% and the subordinate to 10% over 200ms
3. During "unified" lines (rare), both voices say the SAME words but with DIFFERENT delivery — always slightly out of sync (100-200ms offset)
4. During "argument" lines, both voices speak DIFFERENT words simultaneously at 100% volume — cacophony

---

## Bordoes List

### 1. "Companheiro, talkei?"
- **Trigger**: idle (first idle after dominance switch)
- **Type**: UNIFIED — both voices say a fused catchphrase
- **Lula voice**: "Companheiro..." (slow, warm, extending the "ei" of companheiro)
- **Bolsonaro voice**: "...talkei?" (fast, appended, nasalado)
- **Timing**: Lula starts at 0ms, Bolsonaro enters at 600ms (overlapping the tail of "companheiro")
- **Volume**: Lula 7/10, Bolsonaro 6/10
- **Duration**: 1.8s total
- **Emotion**: Confused warmth — the greeting of something that doesn't know what it is
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Companheiro..." --rate "-15%" --pitch "-3Hz" --write-media bolsolula-01-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Talkei?" --rate "+10%" --pitch "+1Hz" --write-media bolsolula-01-R.mp3`
- **Mix**: Overlap at 600ms offset, pan L/R respectively
- **Output**: `bolsolula-01-idle-companheiro-talkei.ogg`
- **Frequency**: First idle after each dominance switch

---

### 2. "A gente vamos... TALKEI?... fazer o que e melhor... VAGABUNDO!... pro povo, companheiro."
- **Trigger**: idle (long idle, 10s+)
- **Type**: ARGUMENT — both voices interrupt each other mid-sentence
- **Lula voice**: "A gente vamos... [PAUSE]... fazer o que e melhor... [PAUSE]... pro povo, companheiro."
- **Bolsonaro voice**: [SILENCE]... "TALKEI?" [INTERRUPT]... [SILENCE]... "VAGABUNDO!" [INTERRUPT]
- **Timing**:
  - 0ms: Lula "A gente vamos..."
  - 800ms: Bolsonaro interrupts "TALKEI?" (cuts into Lula's pause)
  - 1200ms: Lula resumes "...fazer o que e melhor..."
  - 2200ms: Bolsonaro interrupts "VAGABUNDO!" (loud, angry)
  - 2800ms: Lula finishes "...pro povo, companheiro." (unfazed by interruptions)
- **Volume**: Lula 6/10 baseline, Bolsonaro 8/10 on interrupts (louder to interrupt)
- **Duration**: 4.5s total
- **Emotion**: Schizophrenic monologue — one brain trying to give a speech while the other heckles
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "A gente vamos fazer o que e melhor pro povo, companheiro." --rate "-15%" --pitch "-3Hz" --write-media bolsolula-02-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Talkei?" --rate "+15%" --pitch "+2Hz" --write-media bolsolula-02-R-talkei.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Vagabundo!" --rate "+20%" --pitch "+3Hz" --write-media bolsolula-02-R-vagabundo.mp3`
- **Mix**: Layer with timing offsets as described. Lula continuous with pauses. Bolsonaro burst inserts.
- **Output**: `bolsolula-02-idle-long-argument.ogg`
- **Frequency**: Every 30s during extended idle

---

### 3. "Eu sou dois. E nenhum dos dois presta."
- **Trigger**: idle (rare — 5% chance, existential moment)
- **Type**: UNIFIED — both voices in sync (unique moment of agreement)
- **Lula voice**: "Eu sou dois... e nenhum dos dois presta." (sad, reflective, slow)
- **Bolsonaro voice**: Same words, 100ms delay, slightly different cadence (echo effect)
- **Timing**: Lula at 0ms, Bolsonaro at 100ms (creates a ghostly echo/chorus effect)
- **Volume**: Both 5/10 (quiet, introspective)
- **Duration**: 3.0s
- **Emotion**: The single moment of genuine self-awareness. Deeply sad. The monster knows what it is.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu sou dois. E nenhum dos dois presta." --rate "-20%" --pitch "-4Hz" --write-media bolsolula-03-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Eu sou dois. E nenhum dos dois presta." --rate "-15%" --pitch "-2Hz" --write-media bolsolula-03-R.mp3`
- **Mix**: Both centered (break the usual L/R pan for this line), 100ms offset, slight reverb
- **Output**: `bolsolula-03-idle-existential.ogg`
- **Frequency**: Rare — 5% chance when idle exceeds 15s. Once per encounter max.

---

### 4. "A culpa e do... de mim mesmo? NAO! Do outro lado!"
- **Trigger**: hit (on taking damage)
- **Type**: CONFUSION — starts unified, splits into argument
- **Lula voice**: "A culpa e do..." (starts blaming Bolsonaro) then confused pause
- **Bolsonaro voice**: "...de mim mesmo?" (accidentally self-aware for 200ms) then "NAO! Do outro lado!" (aggressive correction)
- **Timing**:
  - 0ms: Lula "A culpa e do..."
  - 500ms: Bolsonaro "...de mim mesmo?" (confused, quiet)
  - 900ms: BOTH simultaneously: "NAO!" (unified denial)
  - 1100ms: Bolsonaro "Do outro lado!" (pointing accusingly across the seam)
- **Volume**: Starts 5/10, "NAO!" peaks at 9/10, settles to 7/10
- **Duration**: 2.0s
- **Emotion**: Blame reflex — automatic, confused, ultimately pointing at the other half of themselves
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa e do..." --rate "-10%" --pitch "-3Hz" --write-media bolsolula-04-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "De mim mesmo? Nao! Do outro lado!" --rate "+5%" --pitch "+1Hz" --write-media bolsolula-04-R.mp3`
- **Mix**: Overlapping with timing as described
- **Output**: `bolsolula-04-hit-blame.ogg`
- **Frequency**: 40% chance on hit

---

### 5. "COMPANHEIRO!" / "VAGABUNDO!" (Simultaneous Scream)
- **Trigger**: attack (on strike frame), special (Debate Eterno)
- **Type**: SIMULTANEOUS CONFLICT — both voices at maximum, different words
- **Lula voice**: "COMPANHEIRO!" (bellowed, comicio-style)
- **Bolsonaro voice**: "VAGABUNDO!" (screamed, live-rant-style)
- **Timing**: Both at 0ms simultaneously. The overlap creates a cacophonous mess where neither word is fully intelligible.
- **Volume**: Both 9/10 (MAX)
- **Duration**: 1.2s
- **Emotion**: Pure contradictory rage directed outward. The monster's war cry.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Companheiro!" --rate "+10%" --pitch "+2Hz" --write-media bolsolula-05-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Vagabundo!" --rate "+15%" --pitch "+3Hz" --write-media bolsolula-05-R.mp3`
- **Mix**: Both at full volume, panned L/R respectively. NO offset — simultaneous.
- **Output**: `bolsolula-05-attack-dual-scream.ogg`
- **Frequency**: Every attack (100%)

---

### 6. "Faz o... MITO!... L... TALKEI!... bem devagarinho... IMBROCHAVEL!"
- **Trigger**: special (Polarizacao Total charge)
- **Type**: INTERLEAVED — Lula's catchphrase interlaced with Bolsonaro's
- **Lula voice**: "Faz o... L... bem devagarinho..." (slow, malicious whisper)
- **Bolsonaro voice**: "MITO!... TALKEI!... IMBROCHAVEL!" (loud interjections between Lula's words)
- **Timing**:
  - 0ms: Lula "Faz o..." (whisper)
  - 400ms: Bolsonaro "MITO!" (shout)
  - 700ms: Lula "...L..." (whisper)
  - 900ms: Bolsonaro "TALKEI!" (shout)
  - 1200ms: Lula "...bem devagarinho..." (slow whisper, ASMR-level)
  - 1800ms: Bolsonaro "IMBROCHAVEL!" (maximum scream)
- **Volume**: Lula 4/10 (whisper), Bolsonaro 9/10 (scream) — extreme dynamic contrast
- **Duration**: 2.5s
- **Emotion**: Contrast-comedy. One side seduces, the other side screams machismo. Together it's absurd.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Faz o L, bem devagarinho..." --rate "-25%" --pitch "-5Hz" --write-media bolsolula-06-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Mito! Talkei! Imbrochavel!" --rate "+20%" --pitch "+3Hz" --write-media bolsolula-06-R.mp3`
- **Mix**: Interleave with timing offsets. Lula whisper is intimate (slight reverb). Bolsonaro shouts are dry and aggressive.
- **Output**: `bolsolula-06-special-faz-o-L-mito.ogg`
- **Frequency**: On Polarizacao Total activation

---

### 7. "Nunca antes na historia deste... CHEGA! Brasil acima de... pais, companheiro... TUDO! Talkei?"
- **Trigger**: special (Palanque Infinito speech phase)
- **Type**: OVERLAPPING SPEECHES — both giving campaign speeches simultaneously
- **Lula voice**: "Nunca antes na historia deste... pais, companheiro..." (classic Lula comicio opening)
- **Bolsonaro voice**: "CHEGA!... Brasil acima de... TUDO! Talkei?" (campaign slogans interjected)
- **Timing**:
  - 0ms: Lula "Nunca antes na historia deste..."
  - 1200ms: Bolsonaro "CHEGA!" (interrupts)
  - 1500ms: Bolsonaro "Brasil acima de..."
  - 2000ms: Lula "...pais, companheiro..."
  - 2200ms: Bolsonaro "TUDO! Talkei?"
- **Volume**: Both 7/10 — comicio volume, projecting
- **Duration**: 3.0s (then LOOPS with variations during Palanque Infinito skill)
- **Emotion**: Dueling rallies — two speeches fighting for the microphone in one body
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Nunca antes na historia deste pais, companheiro" --rate "-20%" --pitch "-3Hz" --write-media bolsolula-07-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Chega! Brasil acima de tudo! Talkei?" --rate "+10%" --pitch "+1Hz" --write-media bolsolula-07-R.mp3`
- **Mix**: Overlap with timing. Both at rally volume. Add slight echo (outdoor rally reverb).
- **Output**: `bolsolula-07-special-palanque.ogg`
- **Frequency**: Loops during Palanque Infinito skill (4 second loop)
- **Variation**: 3 recorded variants of this loop with slightly different word choices/timing to avoid repetition

---

### 8. "Fico puto da vida! / Eu nao fico puto, eu fico INDIGNADO!"
- **Trigger**: hit (heavy damage, >20% HP)
- **Type**: ARGUMENT ABOUT HOW TO REACT — they argue about the pain itself
- **Lula voice**: "Fico puto da vida!" (genuine rage)
- **Bolsonaro voice**: "Eu nao fico puto, eu fico INDIGNADO!" (correcting Lula's vocabulary)
- **Timing**:
  - 0ms: Lula "Fico puto da vida!" (fast, angry)
  - 800ms: Bolsonaro "Eu nao fico puto..." (corrective tone)
  - 1400ms: Bolsonaro "...eu fico INDIGNADO!" (emphasis on indignado)
- **Volume**: Lula 8/10 (genuine scream), Bolsonaro 7/10 (pedantic correction) then 9/10 on "INDIGNADO"
- **Duration**: 2.2s
- **Emotion**: Can't even agree on HOW to be angry. Peak absurdity.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Fico puto da vida!" --rate "+15%" --pitch "+2Hz" --write-media bolsolula-08-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Eu nao fico puto, eu fico indignado!" --rate "+5%" --pitch "+2Hz" --write-media bolsolula-08-R.mp3`
- **Output**: `bolsolula-08-hit-heavy.ogg`
- **Frequency**: On heavy hits (>20% HP damage), 50% chance

---

### 9. "Todo mundo vem pra ca! Talkei, companheiro?"
- **Trigger**: special (Centrao Gravitacional activation)
- **Type**: RARE AGREEMENT — both voices cooperate (the Centrao brings everyone together)
- **Lula voice**: "Todo mundo vem pra ca!" (welcoming, arms-open tone)
- **Bolsonaro voice**: "Talkei, companheiro?" (accidentally using Lula's word — contamination)
- **Timing**:
  - 0ms: Lula "Todo mundo vem pra ca!" (open, inviting)
  - 1200ms: Bolsonaro "Talkei, companheiro?" (realizes he used "companheiro" and is briefly confused)
- **Volume**: Lula 7/10 (warm rally voice), Bolsonaro 6/10 (confused agreement)
- **Duration**: 2.0s
- **Emotion**: The Centrao is the one thing that unites ALL politicians. Both sides genuinely agree on pulling everyone into their orbit.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Todo mundo vem pra ca!" --rate "-5%" --pitch "-2Hz" --write-media bolsolula-09-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Talkei, companheiro?" --rate "+5%" --pitch "+1Hz" --write-media bolsolula-09-R.mp3`
- **Output**: `bolsolula-09-special-centrao.ogg`
- **Frequency**: On Centrao Gravitacional activation

---

### 10. "A culpa e do outro lado! / A culpa e do outro lado!"
- **Trigger**: special (Polarizacao Total active field)
- **Type**: PERFECT MIRROR — both say EXACTLY the same phrase, pointing at each other
- **Lula voice**: "A culpa e do outro lado!" (pointing RIGHT at Bolsonaro half)
- **Bolsonaro voice**: "A culpa e do outro lado!" (pointing LEFT at Lula half)
- **Timing**: Both at 0ms simultaneously, but Lula's is 15% slower, so they drift apart in cadence
- **Volume**: Both 8/10
- **Duration**: 1.8s
- **Emotion**: The quintessence of polarization — blame the other side, EVEN WHEN THEY ARE LITERALLY THE SAME BODY. Maximum irony.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "A culpa e do outro lado!" --rate "-10%" --pitch "-3Hz" --write-media bolsolula-10-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "A culpa e do outro lado!" --rate "+5%" --pitch "+1Hz" --write-media bolsolula-10-R.mp3`
- **Output**: `bolsolula-10-special-polarizacao.ogg`
- **Frequency**: During Polarizacao Total field active phase, every 3s

---

### 11. "Com... panheiro?" / "...talkei?"
- **Trigger**: fusion_sequence (Frame 8 — first words after fusion)
- **Type**: BIRTH CRY — the monster's first words
- **Lula voice**: "Com... panheiro?" (broken, uncertain, like learning to speak again)
- **Bolsonaro voice**: "...talkei?" (equally broken, small voice)
- **Timing**:
  - 0ms: Lula "Com..." (pause, breath)
  - 400ms: Lula "...panheiro?" (questioning, rising intonation)
  - 600ms: Bolsonaro "...talkei?" (tiny, unsure, almost a whisper)
- **Volume**: Both 4/10 (whisper — the monster is scared)
- **Duration**: 1.5s
- **Emotion**: Fear. Confusion. The newborn monster doesn't understand what it is. Both voices are stripped of their usual bravado. This should make the player feel briefly SORRY for the abomination.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Com... panheiro?" --rate "-30%" --pitch "-5Hz" --write-media bolsolula-11-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Talkei?" --rate "-20%" --pitch "-4Hz" --write-media bolsolula-11-R.mp3`
- **Mix**: Both nearly centered (80%L/80%R — less extreme pan than normal). Slight reverb (empty space feeling).
- **Output**: `bolsolula-11-fusion-first-words.ogg`
- **Frequency**: Once — during fusion sequence only

---

### 12. Dual Scream (Fusion Horror)
- **Trigger**: fusion_sequence (Frames 2-4 — body horror merge)
- **Type**: RAW SCREAM — not words, just horror
- **Lula voice**: Prolonged scream, low register, gurgling as throat merges
- **Bolsonaro voice**: Prolonged scream, higher register, cutting through Lula's
- **Timing**: Both at 0ms, continuous for 2000ms, overlapping and merging
- **Volume**: Both 8/10, rising to 10/10 at the peak of fusion (frame 3)
- **Duration**: 2.0s
- **Emotion**: PURE HORROR. Neither wants this. The screams are genuine.
- **TTS Commands**: TTS cannot produce screams — must be recorded or synthesized
  - **Alternative**: Use pitch-shifted stock scream SFX, layered: low male scream (Lula, pitch -5 semitones) + medium male scream (Bolsonaro, pitch +2 semitones)
  - Add wet organic filter (low-pass at 2kHz with 10% distortion) to simulate the merging
- **Output**: `bolsolula-12-fusion-scream.ogg`
- **Frequency**: Once — during fusion sequence

---

### 13. "FUSAO REVERSA!" (Split Ultimate Call)
- **Trigger**: split_sequence (Frame 0 — strain before split)
- **Type**: UNIFIED SCREAM — both voices call the attack name together
- **Lula voice**: "FUSAO..." (strained, effort)
- **Bolsonaro voice**: "...REVERSA!" (explosive release)
- **Timing**:
  - 0ms: Both simultaneously: "FU-" (guttural, straining)
  - 200ms: Lula: "-SAO..." (extends, pulling)
  - 600ms: Bolsonaro: "RE-VER-SA!" (explosive, each syllable punctuated)
- **Volume**: Starts 7/10, peaks at 10/10 on "REVERSA!"
- **Duration**: 1.5s
- **Emotion**: The moment of splitting. Pain + liberation + power. An ultimate attack that costs everything.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Fusao!" --rate "+10%" --pitch "+3Hz" --write-media bolsolula-13-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Reversa!" --rate "+20%" --pitch "+4Hz" --write-media bolsolula-13-R.mp3`
- **Output**: `bolsolula-13-ultimate-fusao-reversa.ogg`
- **Frequency**: On Fusao Reversa activation (1-2 per fight max)

---

### 14. Separation Scream (Split — head divides)
- **Trigger**: split_sequence (Frame 3 — head divides)
- **Type**: RAW DUAL SCREAM — the moment of separation
- **Both voices**: Maximum volume scream that SPLITS in stereo — starts centered, then Lula voice pans hard LEFT and Bolsonaro voice pans hard RIGHT as the halves separate
- **Timing**: 0ms both centered -> 500ms fully panned L/R
- **Volume**: 10/10 (maximum — loudest sound in the game)
- **Duration**: 1.0s
- **Emotion**: The birth scream in reverse — the un-fusion. Pain of being torn apart.
- **TTS Commands**: Not applicable — must be produced as SFX
  - **Alternative**: Record two male screams. Apply dynamic stereo pan automation: center -> L/R spread. Add reverb tail. Layer with bone crack SFX.
- **Output**: `bolsolula-14-split-scream.ogg`
- **Frequency**: Once per Fusao Reversa

---

### 15. "Eu vou lhe dizer uma... CHEGA DE MENTIRA!... coisa, companheiro..."
- **Trigger**: pre-attack (windup phase), idle
- **Type**: INTERRUPTED MONOLOGUE
- **Lula voice**: "Eu vou lhe dizer uma... coisa, companheiro..." (classic muleta verbal, never finishes)
- **Bolsonaro voice**: "CHEGA DE MENTIRA!" (interrupts mid-sentence)
- **Timing**:
  - 0ms: Lula "Eu vou lhe dizer uma..." (slow buildup)
  - 1000ms: Bolsonaro "CHEGA DE MENTIRA!" (cuts in aggressively)
  - 1600ms: Lula (unfazed) "...coisa, companheiro..." (finishes as if nothing happened)
- **Volume**: Lula 6/10 (steady), Bolsonaro 8/10 (interruption)
- **Duration**: 2.5s
- **Emotion**: One side trying to give a speech, the other heckling. Neither succeeds. Business as usual.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu vou lhe dizer uma coisa, companheiro." --rate "-15%" --pitch "-3Hz" --write-media bolsolula-15-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Chega de mentira!" --rate "+15%" --pitch "+3Hz" --write-media bolsolula-15-R.mp3`
- **Output**: `bolsolula-15-idle-interrupted.ogg`
- **Frequency**: Every 20s in idle, 30% chance

---

### 16. "O povo brasileiro... TALKEI... nunca comeu tanta... ARMA... picanha... BIBLIA!"
- **Trigger**: idle (rare, comic relief)
- **Type**: WORD SALAD — both catchphrase sets merge into incoherent fusion
- **Lula voice**: "O povo brasileiro... nunca comeu tanta... picanha..."
- **Bolsonaro voice**: "TALKEI... ARMA... BIBLIA!"
- **Timing**: Interleaved every 400-600ms, creating a nonsensical sentence
- **Volume**: Both 6/10
- **Duration**: 3.5s
- **Emotion**: The ultimate expression of political word salad. All talking points from both sides blended into meaningless noise.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "O povo brasileiro nunca comeu tanta picanha" --rate "-10%" --pitch "-2Hz" --write-media bolsolula-16-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Talkei! Arma! Biblia!" --rate "+10%" --pitch "+2Hz" --write-media bolsolula-16-R.mp3`
- **Output**: `bolsolula-16-idle-word-salad.ogg`
- **Frequency**: Rare — every 45s, 15% chance

---

### 17. "Eu sou dois... e nenhum dos dois presta..." (Death Line)
- **Trigger**: death (Frame 2-3)
- **Type**: UNIFIED WHISPER — dying words
- **Lula voice**: "Eu sou dois..." (fading, sad)
- **Bolsonaro voice**: "...e nenhum dos dois presta..." (completing the sentence, equally sad)
- **Timing**:
  - 0ms: Lula "Eu sou dois..." (whisper, fading volume)
  - 1200ms: Bolsonaro "...e nenhum dos dois presta..." (whisper, even quieter)
- **Volume**: Lula 4/10 -> 2/10 (fading). Bolsonaro 3/10 -> 1/10 (dying whisper).
- **Duration**: 3.5s
- **Emotion**: The final truth. In death, both halves finally agree: they were always the same, and neither was any good. This should be GENUINELY moving despite the absurdity.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Eu sou dois..." --rate "-25%" --pitch "-5Hz" --write-media bolsolula-17-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "E nenhum dos dois presta." --rate "-20%" --pitch "-4Hz" --write-media bolsolula-17-R.mp3`
- **Mix**: Both centered (breaking normal pan). Heavy reverb. Slow fade to silence.
- **Output**: `bolsolula-17-death.ogg`
- **Frequency**: Once — on death (100% play rate)

---

### 18. "IMBROCHAVEL! / Empurra mole..."
- **Trigger**: low_hp (<25%)
- **Type**: CONTRAST DESPERATION — machismo meets seduction, both desperate
- **Lula voice**: "Empurra mole... empurra pensando no Lula..." (ASMR whisper, suggestive)
- **Bolsonaro voice**: "IMBROCHAVEL! IMBROCHAVEL! IM-BRO-CHA-VEL!" (screaming, denial of weakness)
- **Timing**: Both simultaneously — Lula whispers under Bolsonaro's screams
- **Volume**: Lula 3/10 (ASMR whisper), Bolsonaro 9/10 (desperation scream)
- **Duration**: 2.5s
- **Emotion**: Both halves cope with near-death differently. Lula retreats into meme seduction. Bolsonaro screams about being invincible. Neither is helpful. Both are pathetic.
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "Empurra mole, empurra pensando no Lula" --rate "-30%" --pitch "-5Hz" --write-media bolsolula-18-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "Imbrochavel! Imbrochavel! Imbrochavel!" --rate "+20%" --pitch "+4Hz" --write-media bolsolula-18-R.mp3`
- **Output**: `bolsolula-18-low-hp.ogg`
- **Frequency**: On entering <25% HP, then every 8s while below threshold

---

### 19. Walk Mumble (Background)
- **Trigger**: walk (ambient)
- **Type**: BACKGROUND MURMUR — unintelligible dual mumbling
- **Lula voice**: Incoherent mumbling, rhythm of a speech but no words, nordestino cadence
- **Bolsonaro voice**: Incoherent mumbling, rhythm of a live rant but no words, nasal cadence
- **Timing**: Continuous, overlapping, no clear words
- **Volume**: Both 2/10 (barely audible — ambient texture)
- **Duration**: 4.0s (loops)
- **Emotion**: The constant internal argument that never stops, even while walking
- **TTS Commands**:
  - `edge-tts --voice "pt-BR-AntonioNeural" --text "hm hm hm, eu quero, hm, dizer, hm hm" --rate "-20%" --pitch "-4Hz" --write-media bolsolula-19-L.mp3`
  - `edge-tts --voice "pt-BR-FranciscoNeural" --text "ok ok, talkei, ok, nao nao, talkei ok" --rate "+5%" --pitch "+1Hz" --write-media bolsolula-19-R.mp3`
- **Mix**: Both at low volume, panned L/R. Loop seamlessly.
- **Output**: `bolsolula-19-walk-mumble.ogg`
- **Frequency**: Continuous during walk (loops)

---

### 20. "Vota em mim! / Vota em mim! / NAO! EM MIM!"
- **Trigger**: spawn (boss entrance, after fusion sequence)
- **Type**: COMPETING — both sides campaign for the player's vote
- **Lula voice**: "Vota em mim!" (first)
- **Bolsonaro voice**: "Vota em mim!" (immediately after)
- **Both**: "NAO! EM MIM!" (simultaneous scream at each other)
- **Timing**:
  - 0ms: Lula "Vota em mim!" (toward player)
  - 600ms: Bolsonaro "Vota em mim!" (toward player)
  - 1200ms: Both turn to each other "NAO! EM MIM!" (simultaneous, now fighting each other)
- **Volume**: 7/10, peaking to 9/10 on "NAO! EM MIM!"
- **Duration**: 2.0s
- **Emotion**: Pathetic campaign competition that devolves into internal fight. They can't even unite against the player.
- **Output**: `bolsolula-20-spawn.ogg`
- **Frequency**: Once — on boss battle start (after fusion sequence)

---

## Variantes de Intensidade

| Bordao | Sussurro (vol 2-3) | Normal (vol 5-6) | Grito (vol 8-10) |
|---|---|---|---|
| "Companheiro, talkei?" | After combat (exhausted) | Idle (default) | Pre-attack (aggressive) |
| Dual scream ("COMPANHEIRO!"/"VAGABUNDO!") | N/A (always loud) | N/A | Attack + Debate (ALWAYS max) |
| "Eu sou dois..." | Death (whisper) | Idle rare (reflective) | N/A (never shouted) |
| "Fico puto da vida!/INDIGNADO!" | N/A | N/A | Heavy hit ONLY |
| "FUSAO REVERSA!" | N/A | N/A | Ultimate ONLY (max) |
| Walk mumble | Default (barely audible) | N/A | N/A (never loud) |
| "A culpa e do outro lado!" | N/A | Polarizacao field | On damage (heated) |

## Dominance-Dependent Voice Selection

| Dominant Side | Voice Lines Pool | Subdominant Behavior |
|---|---|---|
| **Lula** | #1, #2, #6, #7, #8(Lula part), #15, #16, #18(whisper) | Bolsonaro murmurs at 10% volume, occasional "talkei" interjections |
| **Bolsonaro** | #1, #4, #5(Bolso emphasis), #7, #8(Bolso part), #15(interrupts louder) | Lula murmurs at 10% volume, occasional "companheiro" interjections |
| **Neither** (argument) | #2, #3, #5, #10, #16, #20 | Both at 100% — cacophony |

## Audio File Summary

| # | File | Duration | Type | Priority |
|---|---|---|---|---|
| 01 | `bolsolula-01-idle-companheiro-talkei.ogg` | 1.8s | Idle greeting | MVP |
| 02 | `bolsolula-02-idle-long-argument.ogg` | 4.5s | Idle argument | MVP |
| 03 | `bolsolula-03-idle-existential.ogg` | 3.0s | Idle rare | MVP |
| 04 | `bolsolula-04-hit-blame.ogg` | 2.0s | Hit reaction | MVP |
| 05 | `bolsolula-05-attack-dual-scream.ogg` | 1.2s | Attack | MVP |
| 06 | `bolsolula-06-special-faz-o-L-mito.ogg` | 2.5s | Special | HIGH |
| 07 | `bolsolula-07-special-palanque.ogg` | 3.0s (loop) | Special | HIGH |
| 08 | `bolsolula-08-hit-heavy.ogg` | 2.2s | Hit heavy | HIGH |
| 09 | `bolsolula-09-special-centrao.ogg` | 2.0s | Special | HIGH |
| 10 | `bolsolula-10-special-polarizacao.ogg` | 1.8s | Special | HIGH |
| 11 | `bolsolula-11-fusion-first-words.ogg` | 1.5s | Fusion | MVP |
| 12 | `bolsolula-12-fusion-scream.ogg` | 2.0s | Fusion | MVP |
| 13 | `bolsolula-13-ultimate-fusao-reversa.ogg` | 1.5s | Ultimate | MVP |
| 14 | `bolsolula-14-split-scream.ogg` | 1.0s | Ultimate | MVP |
| 15 | `bolsolula-15-idle-interrupted.ogg` | 2.5s | Idle | MEDIUM |
| 16 | `bolsolula-16-idle-word-salad.ogg` | 3.5s | Idle | MEDIUM |
| 17 | `bolsolula-17-death.ogg` | 3.5s | Death | MVP |
| 18 | `bolsolula-18-low-hp.ogg` | 2.5s | Low HP | HIGH |
| 19 | `bolsolula-19-walk-mumble.ogg` | 4.0s (loop) | Walk | MEDIUM |
| 20 | `bolsolula-20-spawn.ogg` | 2.0s | Spawn | MVP |

## Audio Production Pipeline

### Step 1: TTS Generation
```bash
# Generate all TTS lines using edge-tts
# Run all TTS commands listed above
# This produces raw .mp3 files for each voice (L and R channels)
```

### Step 2: Mixing
```bash
# For each bordao:
# 1. Load L (Lula) and R (Bolsonaro) tracks
# 2. Apply stereo pan (70% L / 70% R)
# 3. Apply timing offsets as specified
# 4. Apply volume levels as specified
# 5. Export as .ogg (Vorbis, quality 6)

# Tools: Audacity (manual) or FFmpeg (automated):
# ffmpeg -i bolsolula-XX-L.mp3 -i bolsolula-XX-R.mp3 \
#   -filter_complex "[0]pan=stereo|FL=FC|FR=0[l];[1]pan=stereo|FL=0|FR=FC[r];[l][r]amix=inputs=2" \
#   -c:a libvorbis -q:a 6 bolsolula-XX-final.ogg
```

### Step 3: Post-Processing
- Add subtle reverb to "unified" lines (cathedral reverb, 15% wet)
- Add slight distortion to screams (tube saturation, 10%)
- Ensure all files normalize to -3dB peak
- Test stereo pan on headphones AND speakers
- Verify timing sync with animation frames (cross-reference animation-spec.md)

### Step 4: Implementation
```javascript
// Phaser 3 audio setup
this.load.audio('bolsolula_bordao_01', 'assets/audio/bordoes/bolsolula-01-idle-companheiro-talkei.ogg');
// ... repeat for all 20 bordoes

// Playback with dominance awareness:
function playBordao(id) {
  const sound = this.sound.add(`bolsolula_bordao_${id}`);
  // Adjust volume based on current dominant side
  const dominantMultiplier = getDominantSide() === 'lula' ? { L: 1.0, R: 0.1 } : { L: 0.1, R: 1.0 };
  // For unified lines (3, 11, 13, 17): both at 1.0
  sound.play({ volume: 0.6 });
}
```

## References
- Compilacoes de Lula: "melhores momentos discurso" no YouTube
- Compilacoes de Bolsonaro: "melhores momentos live" no YouTube
- Andre Guedes Zumbis de Brasilia episodes 1-10 (2018, 2022, 2026)
- Meme "Empurra Mole / Tadalafila": TikTok/Discord viral
- Meme "Imbrochavel": Lives do Bolsonaro
- Meme "BolsoLula": Twitter/X politico brasileiro
