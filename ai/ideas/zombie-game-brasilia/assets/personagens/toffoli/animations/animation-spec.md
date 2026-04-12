# TOFFOLI (Dias Toffoli) - Especificacao de Animacoes (Phaser 3)

## Boss Secundario STF - "O Rato do STF / O Espiao" - "Zumbis de Brasilia"

---

## Configuracao Geral do Phaser 3

```javascript
// ========================================
// TOFFOLI - Configuracao de Animacoes
// Boss Secundario STF - O Espiao
// ========================================

// Constantes do personagem
const TOFFOLI_CONFIG = {
  key: 'toffoli',
  type: 'boss_secundario_stf',
  spriteSize: { width: 64, height: 64 },
  projectileSize: { width: 32, height: 32 },
  defaultFrameRate: 10, // fps base (jerky, estilo Andre Guedes)
  hitboxScale: 0.7, // hitbox menor que sprite (espiao e dificil de acertar)
  
  // Stats base
  hp: 800,
  damage: 35,
  speed: 90, // mais lento que maioria — anda discreto
  defense: 20,
  
  // Passiva: Cara de Paisagem
  passiveStealth: true, // inimigos comuns o ignoram ate ser atacado
  stealthBreakOnAttack: true,
  stealthCooldown: 8000, // 8s pra voltar a ser ignorado
  
  // Drop ao morrer
  deathDrop: 'dossie_debuff', // enfraquece outros bosses
  debuffTargets: ['xandao', 'gilmar', 'barroso', 'lula', 'bolsonaro', 'vorcaro'],
  debuffAmount: 0.15, // 15% reducao de stats
};
```

---

## Carregamento de Assets (Preload)

```javascript
// ========================================
// PRELOAD — Carregamento de Spritesheets
// ========================================

function preloadToffoli(scene) {
  // --- Sprites principais (64x64 por frame) ---
  
  scene.load.spritesheet('toffoli_idle', 
    'assets/personagens/toffoli/sprites/toffoli_idle.png', 
    { frameWidth: 64, frameHeight: 64 }
  );
  
  scene.load.spritesheet('toffoli_walk', 
    'assets/personagens/toffoli/sprites/toffoli_walk.png', 
    { frameWidth: 64, frameHeight: 64 }
  );
  
  scene.load.spritesheet('toffoli_attack', 
    'assets/personagens/toffoli/sprites/toffoli_attack.png', 
    { frameWidth: 64, frameHeight: 64 }
  );
  
  scene.load.spritesheet('toffoli_death', 
    'assets/personagens/toffoli/sprites/toffoli_death.png', 
    { frameWidth: 64, frameHeight: 64 }
  );
  
  scene.load.spritesheet('toffoli_hit', 
    'assets/personagens/toffoli/sprites/toffoli_hit.png', 
    { frameWidth: 64, frameHeight: 64 }
  );
  
  // --- Specials (64x64 por frame) ---
  
  scene.load.spritesheet('toffoli_special_escuta', 
    'assets/personagens/toffoli/sprites/toffoli_special_escuta.png', 
    { frameWidth: 64, frameHeight: 64 }
  );
  
  scene.load.spritesheet('toffoli_special_dossie', 
    'assets/personagens/toffoli/sprites/toffoli_special_dossie.png', 
    { frameWidth: 64, frameHeight: 64 }
  );
  
  scene.load.spritesheet('toffoli_special_fantasma', 
    'assets/personagens/toffoli/sprites/toffoli_special_fantasma.png', 
    { frameWidth: 64, frameHeight: 64 }
  );
  
  // --- Projeteis e Efeitos (32x32 por frame) ---
  
  scene.load.spritesheet('toffoli_proj_onda', 
    'assets/personagens/toffoli/sprites/toffoli_proj_onda.png', 
    { frameWidth: 32, frameHeight: 32 }
  );
  
  scene.load.spritesheet('toffoli_fx_escuta', 
    'assets/personagens/toffoli/sprites/toffoli_fx_escuta.png', 
    { frameWidth: 32, frameHeight: 32 }
  );
  
  scene.load.spritesheet('toffoli_fx_dossie', 
    'assets/personagens/toffoli/sprites/toffoli_fx_dossie.png', 
    { frameWidth: 32, frameHeight: 32 }
  );
  
  scene.load.spritesheet('toffoli_fx_holograma', 
    'assets/personagens/toffoli/sprites/toffoli_fx_holograma.png', 
    { frameWidth: 32, frameHeight: 32 }
  );
  
  scene.load.spritesheet('toffoli_fx_rec', 
    'assets/personagens/toffoli/sprites/toffoli_fx_rec.png', 
    { frameWidth: 32, frameHeight: 32 }
  );
  
  // --- Portrait para UI ---
  
  scene.load.image('toffoli_portrait', 
    'assets/personagens/toffoli/sprites/toffoli_portrait.png'
  );
  
  // --- Audio ---
  
  scene.load.audio('toffoli_sfx_gravei', 'assets/audio/sfx/toffoli_gravei.ogg');
  scene.load.audio('toffoli_sfx_naosei', 'assets/audio/sfx/toffoli_naosei.ogg');
  scene.load.audio('toffoli_sfx_dossie', 'assets/audio/sfx/toffoli_dossie.ogg');
  scene.load.audio('toffoli_sfx_cara', 'assets/audio/sfx/toffoli_cara.ogg');
  scene.load.audio('toffoli_sfx_microfone', 'assets/audio/sfx/toffoli_microfone.ogg');
  scene.load.audio('toffoli_sfx_rec', 'assets/audio/sfx/toffoli_rec_beep.ogg');
  scene.load.audio('toffoli_sfx_playback', 'assets/audio/sfx/toffoli_playback.ogg');
  scene.load.audio('toffoli_sfx_tape_rewind', 'assets/audio/sfx/toffoli_tape_rewind.ogg');
}
```

---

## Definicao de Animacoes (Create)

```javascript
// ========================================
// CREATE — Registro de Animacoes
// ========================================

function createToffoliAnimations(scene) {

  // -----------------------------------------
  // IDLE — "Cara de Paisagem"
  // 4 frames, 8 fps (propositalmente lento, contemplativo)
  // Loop infinito. A animacao mais "parada" do jogo.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_idle',
    frames: scene.anims.generateFrameNumbers('toffoli_idle', { 
      start: 0, end: 3 
    }),
    frameRate: 8,
    repeat: -1, // loop infinito
    // Nota: framerate BAIXO e proposital. O Toffoli idle deve ser
    // quase uma imagem estatica com micro-movimentos. As orelhas
    // girando e o unico sinal de "vida" alem da luz REC piscando.
  });

  // -----------------------------------------
  // WALK — "Espiao Discreto"
  // 6 frames, 10 fps (andar furtivo, nao apressado)
  // Loop infinito durante movimento.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_walk',
    frames: scene.anims.generateFrameNumbers('toffoli_walk', { 
      start: 0, end: 5 
    }),
    frameRate: 10,
    repeat: -1,
    // Nota: O walk do Toffoli e mais LENTO que outros bosses.
    // Ele nao marcha, ele se esgueira. O frame 5 (agachado com
    // olhos em direcoes opostas) e o frame mais caracteristico.
  });

  // -----------------------------------------
  // ATTACK — "Gravacao Comprometedora"
  // 3 frames, 12 fps (rapido — puxa, toca, guarda)
  // Nao loopa. Dispara projetil no frame 2.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_attack',
    frames: scene.anims.generateFrameNumbers('toffoli_attack', { 
      start: 0, end: 2 
    }),
    frameRate: 12,
    repeat: 0, // toca uma vez
    // CALLBACK no frame 1 (index 1): disparar projetil onda sonora
    // CALLBACK no frame 2 (index 2): voltar a idle
    // A transicao frame 1->2 (expressao->paisagem) deve ser INSTANTANEA
  });

  // -----------------------------------------
  // DEATH — "Queda do Espiao"
  // 4 frames, 8 fps (dramatico, cada frame tem muito detalhe)
  // Nao loopa. Segura no ultimo frame.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_death',
    frames: scene.anims.generateFrameNumbers('toffoli_death', { 
      start: 0, end: 3 
    }),
    frameRate: 8,
    repeat: 0,
    hideOnComplete: false, // corpo fica visivel no chao
    // Frame 1: choque genuino (unica expressao real)
    // Frame 2: microfones cascateando (spawnar particulas)
    // Frame 3: dossies explodindo (spawnar itens de drop)
    // Frame 4: corpo no chao (estado final)
  });

  // -----------------------------------------
  // HIT — "A Mascara Cai (Por 1 Frame)"
  // 2 frames, timing ESPECIAL (ver nota)
  // Nao loopa. Frame 1 rapido, Frame 2 instantaneo.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_hit',
    frames: [
      { key: 'toffoli_hit', frame: 0, duration: 120 },  // 120ms de surpresa
      { key: 'toffoli_hit', frame: 1, duration: 80 },   // 80ms de recuperacao
    ],
    repeat: 0,
    // NOTA CRITICA: O frame 0 (surpresa) dura EXATAMENTE 120ms.
    // Rapido o suficiente pra duvidar se viu, lento o suficiente
    // pra registrar subconscientemente. Este timing e a piada central.
    // 
    // O frame 1 (recuperacao) e ainda mais rapido — 80ms e volta a idle.
    // A velocidade da recuperacao e PARTE DA COMEDIA.
    //
    // Efeito colateral: spawnar fone de ouvido caindo (particula)
    // no frame 0, e "teletransportar" de volta no frame 1.
  });

  // -----------------------------------------
  // SPECIAL: Escuta Secreta
  // 4 frames, 6 fps (lento, deliberado, poderoso)
  // Nao loopa. Ativa buff de captura.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_special_escuta',
    frames: scene.anims.generateFrameNumbers('toffoli_special_escuta', { 
      start: 0, end: 3 
    }),
    frameRate: 6,
    repeat: 0,
    // Frame 0: orelhas comecam a crescer
    // Frame 1: orelhas no maximo, ondas sonoras emanam
    // Frame 2: captacao (spawnar efeito fx_escuta ao redor)
    // Frame 3: escuta completa, buff ativo
    //
    // Apos completar: Toffoli ganha buff "Escuta Ativa" por 10s.
    // Proximo ataque inimigo e CAPTURADO (nao causa dano) e
    // armazenado para uso no Special "Gravacao Fantasma".
  });

  // -----------------------------------------
  // SPECIAL: Dossie Secreto
  // 6 frames, 8 fps (medio, dramatico)
  // Nao loopa. Dropa debuffs em area.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_special_dossie',
    frames: scene.anims.generateFrameNumbers('toffoli_special_dossie', { 
      start: 0, end: 5 
    }),
    frameRate: 8,
    repeat: 0,
    // Frame 0: mao entra na toga
    // Frame 1: puxa pasta gigante
    // Frame 2: abre pasta (expressao rara: sorriso sinistro)
    // Frame 3: documentos voam (spawnar fx_dossie multiplos)
    // Frame 4: particulas de debuff se espalham
    // Frame 5: guarda pasta vazia, ajusta toga
    //
    // Efeito: Todos os bosses no mapa perdem 15% de stats
    // permanentemente. Cada dossie droppado e um item coletavel
    // que revela fraqueza de um boss especifico.
  });

  // -----------------------------------------
  // SPECIAL: Gravacao Fantasma
  // 6 frames, 10 fps (medio-rapido, espetacular)
  // Nao loopa. Reflete ultimo ataque capturado.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_special_fantasma',
    frames: scene.anims.generateFrameNumbers('toffoli_special_fantasma', { 
      start: 0, end: 5 
    }),
    frameRate: 10,
    repeat: 0,
    // Frame 0: prepara gravador carregado
    // Frame 1: aperta play (expressao diabolica MAXIMA)
    // Frame 2: holograma aparece (spawnar fx_holograma)
    // Frame 3: holograma ataca inimigo original
    // Frame 4: impacto (screen shake, particulas)
    // Frame 5: dissipacao, volta a normalidade
    //
    // REQUER: buff "Escuta Ativa" com ataque capturado.
    // Se nao tiver gravacao, animacao nao roda (gravador nao brilha).
    // Dano = dano original do ataque capturado x 1.5
  });

  // -----------------------------------------
  // PROJETIL: Onda Sonora
  // 4 frames, 12 fps (rapido, efemero)
  // Loop ate colidir ou sair da tela.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_proj_onda',
    frames: scene.anims.generateFrameNumbers('toffoli_proj_onda', { 
      start: 0, end: 3 
    }),
    frameRate: 12,
    repeat: -1,
    // Projetil viaja em linha reta na direcao do alvo.
    // Velocidade: 200 px/s
    // Dano: 35 (base)
    // Ao colidir: particulas de texto ("GRAVEI", "FLAGRA") se dispersam.
    // Range: 300px (medio — nao e sniper, e gravacao)
  });

  // -----------------------------------------
  // FX: Ondas de Escuta Passiva
  // 4 frames, 2 fps (MUITO lento, ambiente)
  // Loop infinito enquanto idle.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_fx_escuta',
    frames: scene.anims.generateFrameNumbers('toffoli_fx_escuta', { 
      start: 0, end: 3 
    }),
    frameRate: 2,
    repeat: -1,
    // Efeito ambiente que roda constantemente sobre as orelhas
    // do Toffoli. Circulos concentricos verdes expandindo.
    // Opacity: 30% (sutil, quase subliminar).
    // Indica que ele SEMPRE esta escutando.
  });

  // -----------------------------------------
  // FX: Documentos Voando
  // 6 frames, 10 fps (medio)
  // Toca uma vez por documento spawnado.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_fx_dossie',
    frames: scene.anims.generateFrameNumbers('toffoli_fx_dossie', { 
      start: 0, end: 5 
    }),
    frameRate: 10,
    repeat: 0,
    // Spawnado multiplas vezes durante special_dossie.
    // Cada instancia tem direcao e rotacao aleatoria.
    // Ao final da animacao, documento se torna item coletavel.
  });

  // -----------------------------------------
  // FX: Holograma Fantasma
  // 6 frames, 8 fps
  // Toca uma vez durante special_fantasma.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_fx_holograma',
    frames: scene.anims.generateFrameNumbers('toffoli_fx_holograma', { 
      start: 0, end: 5 
    }),
    frameRate: 8,
    repeat: 0,
    // Silhueta verde translucida que replica o inimigo.
    // Escala: match do sprite inimigo (pode variar).
    // Tint: green (#00FF88), alpha: 0.6
    // Efeito adicional: CRT scan lines via shader ou overlay.
  });

  // -----------------------------------------
  // FX: Luz REC
  // 2 frames, 3 fps (piscada lenta de LED)
  // Loop infinito — sempre visivel sobre gravador.
  // -----------------------------------------
  scene.anims.create({
    key: 'toffoli_fx_rec',
    frames: scene.anims.generateFrameNumbers('toffoli_fx_rec', { 
      start: 0, end: 1 
    }),
    frameRate: 3,
    repeat: -1,
    // Overlay permanente posicionado sobre o gravador do Toffoli.
    // Posicao relativa ao sprite: ajustar per-animation.
    // Esse LED vermelho piscando e um lembrete constante:
    // ele esta SEMPRE gravando.
  });
}
```

---

## Maquina de Estados de Animacao

```javascript
// ========================================
// STATE MACHINE — Transicoes de Animacao
// ========================================

const TOFFOLI_STATES = {
  IDLE: 'idle',
  WALK: 'walk',
  ATTACK: 'attack',
  HIT: 'hit',
  DEATH: 'death',
  SPECIAL_ESCUTA: 'special_escuta',
  SPECIAL_DOSSIE: 'special_dossie',
  SPECIAL_FANTASMA: 'special_fantasma',
  STEALTH: 'stealth', // estado passivo "Cara de Paisagem"
};

// Transicoes permitidas (de -> [para])
const TOFFOLI_TRANSITIONS = {
  idle: ['walk', 'attack', 'hit', 'death', 'special_escuta', 'special_dossie', 'special_fantasma'],
  walk: ['idle', 'attack', 'hit', 'death', 'special_escuta'],
  attack: ['idle'], // sempre volta pra idle apos attack
  hit: ['idle', 'death'], // volta a idle ou morre
  death: [], // estado final, sem transicao
  special_escuta: ['idle'],
  special_dossie: ['idle'],
  special_fantasma: ['idle'],
  stealth: ['idle', 'walk', 'attack', 'special_escuta'], // pode agir de stealth
};

// Prioridades de animacao (maior numero = maior prioridade)
const TOFFOLI_PRIORITY = {
  idle: 0,
  walk: 1,
  stealth: 1,
  attack: 5,
  hit: 8,
  special_escuta: 6,
  special_dossie: 7,
  special_fantasma: 7,
  death: 10, // maxima prioridade, nao pode ser interrompido
};
```

---

## Logica de Animacao em Runtime

```javascript
// ========================================
// UPDATE — Logica de Animacao por Frame
// ========================================

class ToffoliAnimationController {
  constructor(scene, sprite) {
    this.scene = scene;
    this.sprite = sprite;
    this.currentState = TOFFOLI_STATES.IDLE;
    this.isStealthed = true; // comeca em stealth (Cara de Paisagem)
    this.hasRecording = false; // se tem gravacao pra Fantasma
    this.recordedAttack = null; // ataque capturado
    this.escutaBuffActive = false;
    this.stealthTimer = null;
    
    // Overlays persistentes
    this.recLight = null; // FX da luz REC (sempre visivel)
    this.escutaWaves = null; // FX ondas passivas das orelhas
    
    this.setupOverlays();
    this.setupCallbacks();
  }

  // -----------------------------------------
  // Overlays permanentes
  // -----------------------------------------
  setupOverlays() {
    // Luz REC — sempre piscando sobre o gravador
    this.recLight = this.scene.add.sprite(
      this.sprite.x + 12, // offset X pro gravador na mao direita
      this.sprite.y + 5,  // offset Y
      'toffoli_fx_rec'
    );
    this.recLight.play('toffoli_fx_rec');
    this.recLight.setAlpha(0.8);
    this.recLight.setDepth(this.sprite.depth + 1);
    
    // Ondas de escuta passiva — sobre as orelhas
    this.escutaWaves = this.scene.add.sprite(
      this.sprite.x,
      this.sprite.y - 10, // offset Y pra cima (orelhas)
      'toffoli_fx_escuta'
    );
    this.escutaWaves.play('toffoli_fx_escuta');
    this.escutaWaves.setAlpha(0.3); // BEM sutil
    this.escutaWaves.setDepth(this.sprite.depth - 1); // atras do sprite
  }

  // -----------------------------------------
  // Callbacks de eventos de animacao
  // -----------------------------------------
  setupCallbacks() {
    // ATTACK — spawnar projetil no frame 1 (meio do ataque)
    this.sprite.on('animationupdate', (anim, frame) => {
      if (anim.key === 'toffoli_attack' && frame.index === 1) {
        this.spawnOndaSonora();
        this.playSound('toffoli_sfx_gravei');
      }
    });

    // ATTACK — volta a idle quando completa
    this.sprite.on('animationcomplete-toffoli_attack', () => {
      this.transitionTo(TOFFOLI_STATES.IDLE);
    });

    // HIT — efeito de fone caindo no frame 0
    this.sprite.on('animationupdate', (anim, frame) => {
      if (anim.key === 'toffoli_hit' && frame.index === 0) {
        this.spawnFoneCaindo();
        this.breakStealth(); // ser atacado quebra stealth
      }
    });

    // HIT — volta a idle quando completa
    this.sprite.on('animationcomplete-toffoli_hit', () => {
      this.transitionTo(TOFFOLI_STATES.IDLE);
      this.startStealthCooldown(); // comeca timer pra voltar a stealth
    });

    // DEATH — spawnar microfones cascata no frame 1
    this.sprite.on('animationupdate', (anim, frame) => {
      if (anim.key === 'toffoli_death' && frame.index === 1) {
        this.spawnMicrofonesCascata(25); // 25 microfones caindo
        this.playSound('toffoli_sfx_microfone');
      }
    });

    // DEATH — spawnar dossies no frame 2
    this.sprite.on('animationupdate', (anim, frame) => {
      if (anim.key === 'toffoli_death' && frame.index === 2) {
        this.spawnDossiesExplosao();
        this.playSound('toffoli_sfx_dossie');
        this.applyGlobalDebuff(); // enfraquece todos os bosses
      }
    });

    // DEATH — estado final
    this.sprite.on('animationcomplete-toffoli_death', () => {
      this.onDeathComplete();
    });

    // SPECIAL ESCUTA — ativar buff no ultimo frame
    this.sprite.on('animationcomplete-toffoli_special_escuta', () => {
      this.escutaBuffActive = true;
      this.playSound('toffoli_sfx_gravei');
      this.showBuffIndicator('ESCUTA ATIVA', 10000); // 10s
      this.transitionTo(TOFFOLI_STATES.IDLE);
      
      // Timer pra desativar buff
      this.scene.time.delayedCall(10000, () => {
        this.escutaBuffActive = false;
      });
    });

    // SPECIAL DOSSIE — spawnar documentos no frame 3
    this.sprite.on('animationupdate', (anim, frame) => {
      if (anim.key === 'toffoli_special_dossie' && frame.index === 3) {
        this.spawnDossiesVoando(8); // 8 documentos
        this.playSound('toffoli_sfx_dossie');
      }
    });

    // SPECIAL DOSSIE — completo
    this.sprite.on('animationcomplete-toffoli_special_dossie', () => {
      this.applyGlobalDebuff();
      this.transitionTo(TOFFOLI_STATES.IDLE);
    });

    // SPECIAL FANTASMA — spawnar holograma no frame 2
    this.sprite.on('animationupdate', (anim, frame) => {
      if (anim.key === 'toffoli_special_fantasma' && frame.index === 2) {
        this.spawnHolograma();
        this.playSound('toffoli_sfx_playback');
      }
    });

    // SPECIAL FANTASMA — impacto no frame 4
    this.sprite.on('animationupdate', (anim, frame) => {
      if (anim.key === 'toffoli_special_fantasma' && frame.index === 4) {
        this.hologramaImpacto();
        this.scene.cameras.main.shake(200, 0.01); // screen shake
      }
    });

    // SPECIAL FANTASMA — completo
    this.sprite.on('animationcomplete-toffoli_special_fantasma', () => {
      this.hasRecording = false; // gravacao foi usada
      this.recordedAttack = null;
      this.transitionTo(TOFFOLI_STATES.IDLE);
    });
  }

  // -----------------------------------------
  // Transicao de estado
  // -----------------------------------------
  transitionTo(newState) {
    const allowed = TOFFOLI_TRANSITIONS[this.currentState];
    if (!allowed || !allowed.includes(newState)) {
      // Excecao: death sempre e permitido
      if (newState !== TOFFOLI_STATES.DEATH) return;
    }
    
    // Checar prioridade
    if (TOFFOLI_PRIORITY[newState] < TOFFOLI_PRIORITY[this.currentState]) {
      if (this.currentState === TOFFOLI_STATES.DEATH) return; // morte nao pode ser interrompida
    }
    
    this.currentState = newState;
    this.sprite.play(`toffoli_${newState}`);
    
    // Atualizar overlays
    this.updateOverlayPositions();
    
    // Stealth visual
    if (this.isStealthed && newState === TOFFOLI_STATES.IDLE) {
      this.sprite.setAlpha(0.7); // levemente transparente quando em stealth
    } else {
      this.sprite.setAlpha(1.0);
    }
  }

  // -----------------------------------------
  // Cara de Paisagem (Passiva: Stealth)
  // -----------------------------------------
  breakStealth() {
    this.isStealthed = false;
    this.sprite.setAlpha(1.0);
    // Inimigos comuns passam a notar o Toffoli
  }

  startStealthCooldown() {
    if (this.stealthTimer) this.stealthTimer.remove();
    this.stealthTimer = this.scene.time.delayedCall(
      TOFFOLI_CONFIG.stealthCooldown, 
      () => {
        this.isStealthed = true;
        if (this.currentState === TOFFOLI_STATES.IDLE) {
          this.sprite.setAlpha(0.7);
        }
      }
    );
  }

  // -----------------------------------------
  // Escuta Secreta — captura ataque inimigo
  // -----------------------------------------
  captureEnemyAttack(attackData) {
    if (!this.escutaBuffActive) return false;
    
    this.hasRecording = true;
    this.recordedAttack = {
      damage: attackData.damage * 1.5, // dano amplificado
      type: attackData.type,
      source: attackData.source,
      animation: attackData.animKey, // pra replicar visual
    };
    
    this.escutaBuffActive = false;
    this.playSound('toffoli_sfx_rec');
    
    // Visual: gravador brilha verde
    this.recLight.setTint(0x00FF88);
    this.scene.time.delayedCall(500, () => {
      this.recLight.clearTint();
    });
    
    return true; // ataque foi capturado (anulado)
  }

  // -----------------------------------------
  // Metodos de spawn de efeitos
  // -----------------------------------------
  
  spawnOndaSonora() {
    const proj = this.scene.physics.add.sprite(
      this.sprite.x + (this.sprite.flipX ? -20 : 20),
      this.sprite.y,
      'toffoli_proj_onda'
    );
    proj.play('toffoli_proj_onda');
    proj.setVelocityX(this.sprite.flipX ? -200 : 200);
    proj.damage = TOFFOLI_CONFIG.damage;
    proj.setAlpha(0.7);
    
    // Auto-destruir apos 300px de range
    this.scene.time.delayedCall(1500, () => {
      if (proj.active) proj.destroy();
    });
    
    return proj;
  }

  spawnFoneCaindo() {
    // Particula do fone de ouvido caindo da orelha
    const fone = this.scene.add.sprite(
      this.sprite.x + 8,
      this.sprite.y - 15,
      'toffoli_fx_rec' // reutiliza asset, tintado de preto
    );
    fone.setTint(0x333333);
    fone.setScale(0.5);
    
    this.scene.tweens.add({
      targets: fone,
      y: fone.y + 30,
      alpha: 0,
      duration: 300,
      ease: 'Bounce.easeOut',
      onComplete: () => fone.destroy(),
    });
  }

  spawnMicrofonesCascata(count) {
    for (let i = 0; i < count; i++) {
      this.scene.time.delayedCall(i * 40, () => { // cascata com delay
        const mic = this.scene.add.sprite(
          this.sprite.x + Phaser.Math.Between(-15, 15),
          this.sprite.y + Phaser.Math.Between(-20, 0),
          'toffoli_fx_rec' // placeholder — substituir por sprite de mic
        );
        mic.setTint(0x555555);
        mic.setScale(Phaser.Math.FloatBetween(0.3, 0.7));
        mic.setAngle(Phaser.Math.Between(0, 360));
        
        this.scene.tweens.add({
          targets: mic,
          y: mic.y + Phaser.Math.Between(30, 60),
          x: mic.x + Phaser.Math.Between(-30, 30),
          angle: mic.angle + Phaser.Math.Between(-180, 180),
          alpha: 0.3,
          duration: Phaser.Math.Between(600, 1200),
          ease: 'Bounce.easeOut',
          onComplete: () => mic.destroy(),
        });
      });
    }
  }

  spawnDossiesExplosao() {
    const bossNames = ['XANDAO', 'GILMAR', 'BARROSO', 'LULA', 'BOLSO', 'VORCARO'];
    
    bossNames.forEach((name, i) => {
      this.scene.time.delayedCall(i * 80, () => {
        const dossie = this.scene.add.sprite(
          this.sprite.x,
          this.sprite.y - 5,
          'toffoli_fx_dossie'
        );
        dossie.play('toffoli_fx_dossie');
        dossie.setData('bossTarget', name);
        
        // Voar em direcao aleatoria
        const angle = (i / bossNames.length) * Math.PI * 2;
        this.scene.tweens.add({
          targets: dossie,
          x: dossie.x + Math.cos(angle) * 80,
          y: dossie.y + Math.sin(angle) * 80 - 40, // arco pra cima
          duration: 1000,
          ease: 'Sine.easeOut',
          onComplete: () => {
            // Dossie se torna item coletavel
            this.convertToCollectible(dossie);
          },
        });
      });
    });
  }

  spawnDossiesVoando(count) {
    for (let i = 0; i < count; i++) {
      const dossie = this.scene.add.sprite(
        this.sprite.x + Phaser.Math.Between(-10, 10),
        this.sprite.y - 10,
        'toffoli_fx_dossie'
      );
      dossie.play('toffoli_fx_dossie');
      
      const angle = (i / count) * Math.PI * 2;
      this.scene.tweens.add({
        targets: dossie,
        x: dossie.x + Math.cos(angle) * 100,
        y: dossie.y + Math.sin(angle) * 100 - 50,
        alpha: 0,
        duration: 1500,
        ease: 'Sine.easeOut',
        onComplete: () => dossie.destroy(),
      });
    }
  }

  spawnHolograma() {
    if (!this.recordedAttack) return;
    
    // Criar holograma verde translucido do inimigo
    this.holograma = this.scene.add.sprite(
      this.sprite.x + (this.sprite.flipX ? -30 : 30),
      this.sprite.y,
      'toffoli_fx_holograma'
    );
    this.holograma.play('toffoli_fx_holograma');
    this.holograma.setTint(0x00FF88);
    this.holograma.setAlpha(0.6);
    
    // Efeito CRT scan lines (shader ou overlay)
    // TODO: Implementar shader de CRT scan lines
  }

  hologramaImpacto() {
    if (!this.holograma || !this.recordedAttack) return;
    
    // Flash de impacto
    this.scene.cameras.main.flash(100, 0, 255, 136, true); // flash verde
    
    // Particulas de impacto
    // TODO: Emitter de particulas verdes + brancas
    
    // Aplicar dano refletido
    // this.recordedAttack.source.takeDamage(this.recordedAttack.damage);
    
    // Destruir holograma com fade
    this.scene.tweens.add({
      targets: this.holograma,
      alpha: 0,
      duration: 500,
      onComplete: () => {
        if (this.holograma) {
          this.holograma.destroy();
          this.holograma = null;
        }
      },
    });
  }

  applyGlobalDebuff() {
    // Aplicar debuff de -15% stats em todos os bosses vivos
    TOFFOLI_CONFIG.debuffTargets.forEach(bossKey => {
      // TODO: Acessar referencia global de bosses
      // const boss = this.scene.bosses[bossKey];
      // if (boss && boss.active) {
      //   boss.applyDebuff('toffoli_dossie', TOFFOLI_CONFIG.debuffAmount);
      // }
    });
  }

  convertToCollectible(dossie) {
    // Converter sprite de dossie voando em item coletavel
    const bossTarget = dossie.getData('bossTarget');
    // TODO: Converter para item coletavel do sistema de drops
    dossie.destroy();
  }

  // -----------------------------------------
  // Helpers
  // -----------------------------------------
  
  playSound(key) {
    this.scene.sound.play(key, { volume: 0.6 });
  }

  showBuffIndicator(text, duration) {
    const indicator = this.scene.add.text(
      this.sprite.x,
      this.sprite.y - 30,
      text,
      { fontSize: '8px', color: '#00FF88', fontFamily: 'monospace' }
    );
    indicator.setOrigin(0.5);
    
    this.scene.tweens.add({
      targets: indicator,
      y: indicator.y - 20,
      alpha: 0,
      duration: duration,
      onComplete: () => indicator.destroy(),
    });
  }

  updateOverlayPositions() {
    if (this.recLight) {
      this.recLight.x = this.sprite.x + (this.sprite.flipX ? -12 : 12);
      this.recLight.y = this.sprite.y + 5;
    }
    if (this.escutaWaves) {
      this.escutaWaves.x = this.sprite.x;
      this.escutaWaves.y = this.sprite.y - 10;
    }
  }

  update() {
    this.updateOverlayPositions();
  }

  destroy() {
    if (this.recLight) this.recLight.destroy();
    if (this.escutaWaves) this.escutaWaves.destroy();
    if (this.holograma) this.holograma.destroy();
    if (this.stealthTimer) this.stealthTimer.remove();
  }
}
```

---

## Tabela de Timing Detalhado

| Animacao            | Frames | FPS  | Duracao Total | Loop | Notas                                           |
|--------------------|--------|------|---------------|------|-------------------------------------------------|
| Idle               | 4      | 8    | 500ms         | Sim  | Propositalmente lento e monótono                |
| Walk               | 6      | 10   | 600ms         | Sim  | Furtivo, nao apressado                          |
| Attack             | 3      | 12   | 250ms         | Nao  | Rapido: puxa-toca-guarda                        |
| Death              | 4      | 8    | 500ms         | Nao  | Dramatico, cada frame tem muito detalhe         |
| Hit                | 2      | *    | 200ms         | Nao  | *Custom: F0=120ms, F1=80ms                      |
| Sp: Escuta         | 4      | 6    | 667ms         | Nao  | Lento, deliberado, cerimonial                   |
| Sp: Dossie         | 6      | 8    | 750ms         | Nao  | Medio, com pause dramatico no F2                |
| Sp: Fantasma       | 6      | 10   | 600ms         | Nao  | Medio-rapido, espetacular                       |
| Proj: Onda         | 4      | 12   | 333ms         | Sim  | Rapido, efemero                                 |
| FX: Escuta         | 4      | 2    | 2000ms        | Sim  | Muito lento, ambiente, quase subliminar         |
| FX: Dossie         | 6      | 10   | 600ms         | Nao  | Uma vez por documento                           |
| FX: Holograma      | 6      | 8    | 750ms         | Nao  | Pulsacao CRT                                    |
| FX: Luz REC        | 2      | 3    | 667ms         | Sim  | Piscada lenta constante de LED                  |

---

## Bordoes e Audio Triggers

| Evento                  | Bordao                                             | Arquivo Audio             |
|------------------------|-----------------------------------------------------|---------------------------|
| Attack (frame 1)       | "Gravei! Gravei tudo!"                              | `toffoli_sfx_gravei.ogg`  |
| Hit (frame 0)          | (silencio — a surpresa e muda)                      | (nenhum — o silencio e a piada) |
| Death (frame 2)        | "Tenho um dossiê sobre você... e sobre VOCÊ."      | `toffoli_sfx_dossie.ogg`  |
| Special Escuta (fim)   | "O microfone estava ligado? Que surpresa..."        | `toffoli_sfx_microfone.ogg` |
| Special Dossie (frame 2)| "Tenho um dossiê sobre você... e sobre você... e sobre VOCÊ." | `toffoli_sfx_dossie.ogg` |
| Special Fantasma (frame 1)| "Cara de paisagem? Isso é ESTRATÉGIA."           | `toffoli_sfx_cara.ogg`    |
| Idle (aleatorio, 5%)   | "Eu? Eu não sei de nada..."                         | `toffoli_sfx_naosei.ogg`  |
| Stealth ativado        | (nenhum som — ele e discreto)                       | (nenhum)                  |
| Captura ataque         | *bip* de gravacao                                   | `toffoli_sfx_rec.ogg`     |
| Fantasma playback      | *som de fita rebobinando*                           | `toffoli_sfx_tape_rewind.ogg` |

---

## Interacoes com Outros Bosses

### Passiva: Cara de Paisagem
- Inimigos comuns (zumbis, minions) IGNORAM o Toffoli completamente quando em stealth
- Bosses TAMBEM o ignoram se ele nao atacou recentemente
- O jogador precisa PERCEBER que o Toffoli esta ali (ele quase nao se destaca)
- Ao atacar, stealth quebra por 8 segundos

### Drop ao Morrer: Dossie Secreto
- Ao morrer, Toffoli AUTOMATICAMENTE dropa 6 dossies
- Cada dossie enfraquece um boss especifico em 15%
- Os dossies sao itens coletaveis — o jogador decide quais pegar
- Visualmente: pasta amarelada com nome do boss e carimbo "CONFIDENCIAL"

### Sinergia com VORCARO
- Se VORCARO esta vivo quando Toffoli morre, o dossie do Vorcaro causa 25% de debuff (extra)
- Se o jogador matou Toffoli ANTES do Vorcaro, o Vorcaro fica mais fraco
- Referencia narrativa: skin "Banco Master" ativa dialogo especial com Vorcaro

### Combo com Escuta + Fantasma
- Escuta Secreta captura o proximo ataque inimigo
- Gravacao Fantasma reproduz esse ataque com 1.5x dano
- Se capturar ataque de BOSS, o fantasma replica a animacao especifica daquele boss (com tint verde)
- Cooldown combinado: Escuta 15s, Fantasma 20s

---

## Notas de Implementacao

1. **O hit de 2 frames tem timing CUSTOM** — nao usa frameRate uniforme. Frame 0 = 120ms, Frame 1 = 80ms. Usar `duration` por frame ao inves de `frameRate`.
2. **Overlays de FX (REC e ondas)** devem seguir o sprite em todo frame. Atualizar posicao no `update()`.
3. **Stealth alpha**: Quando em Cara de Paisagem, sprite fica em alpha 0.7. Ao atacar/levar hit, volta a 1.0.
4. **Screen shake** no impacto do Fantasma deve ser SUTIL (0.01 intensity, 200ms) — e um ataque cirurgico, nao uma explosao.
5. **Holograma** idealmente usa shader de CRT scan lines. Fallback: overlay semi-transparente com linhas horizontais.
6. **Audio do idle** ("Eu? Eu nao sei de nada...") deve ter 5% de chance a cada ciclo de idle. NAO deve ser frequente — a raridade e parte da comedia.
7. **O silencio no hit e INTENCIONAL** — nenhum som, nenhum bordao. A ausencia de reacao sonora reforça que a surpresa visual e tudo.
