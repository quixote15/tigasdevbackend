# Gilmar Mendes — Animation Specification

## Boss do STF — "O Coringa do STF" | Zumbis de Brasilia

---

## Configuracao Global de Animacao

### Engine: Phaser 3
### Frame Rate Global: 8-10 fps (estilo Andre Guedes — JERKY, nunca fluido)
### Easing: NENHUM. Transicoes CORTADAS. Sem interpolacao. Sem tweening suave.
### Principio: Cada frame e uma POSE CHAVE. Nao existe "entre-frames". O estilo Andre Guedes e stop-motion digital — cortes secos entre poses.

### Sprite Anchor Point
```javascript
// Todos os sprites do Gilmar
sprite.setOrigin(0.5, 0.9375); // (32/64, 60/64) = bottom-center
```

---

## 1. IDLE — "O Deboche Eterno"

### Configuracao Phaser 3
```javascript
this.anims.create({
    key: 'gilmar_idle',
    frames: this.anims.generateFrameNumbers('gilmar_idle', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1  // loop infinito
});
```

### Timing Frame-by-Frame

| Frame | Duracao | Descricao | Evento de Som |
|---|---|---|---|
| 0 | 125ms | Papada tremendo (posicao base) | — |
| 1 | 125ms | Oculos brilham (flash cinico) | SFX: brilho sutil (tink) |
| 2 | 150ms | Mordendo pastel (momento chave) | SFX: mordida crocante |
| 3 | 125ms | Sorrisinho de deboche (mastigando) | — |

**Duracao total do ciclo**: ~525ms (~1.9 ciclos por segundo)

### Efeitos de Particula (durante Idle)

#### Migalhas de Pastel
```javascript
// Emitter ativo durante Frame 2 (mordida)
const migalhas = this.add.particles('particle_migalha');
migalhas.createEmitter({
    x: sprite.x + 4,
    y: sprite.y - 20,  // altura da boca
    speed: { min: 10, max: 30 },
    angle: { min: 200, max: 340 },  // cai pra baixo e pros lados
    scale: { start: 1, end: 0 },
    lifespan: 400,
    quantity: 3,
    frequency: -1,  // emissao unica por trigger
    tint: 0xD4A855  // cor migalha
});
```

#### Brilho dos Oculos
```javascript
// Flash branco no Frame 1
// Overlay sprite de brilho posicionado sobre os oculos
const brilho = this.add.sprite(sprite.x, sprite.y - 28, 'fx_glasses_glint');
brilho.setAlpha(0.6);
brilho.setScale(0.5);
// Aparece por 1 frame (125ms) e desaparece
this.time.delayedCall(125, () => brilho.setAlpha(0));
```

### Variacao Aleatoria (Anti-Monotonia)
```javascript
// A cada 3-4 ciclos de idle, inserir variacao aleatoria:
// 50% chance: Gilmar olha pro celular (cabeca gira 5px pra esquerda)
// 30% chance: Papada faz tremor extra (frame 0 com shake de 1px)
// 20% chance: Nota de dinheiro escorrega do bolso (particula verde cai)
```

### Transicoes
- **Idle -> Walk**: CORTE SECO. Sem blend. Frame 3 do idle -> Frame 0 do walk.
- **Idle -> Attack**: CORTE SECO. Qualquer frame do idle -> Frame 0 do attack.
- **Idle -> Hit**: INTERROMPE qualquer frame do idle. Hit tem prioridade absoluta.
- **Idle -> Special**: CORTE SECO. Gilmar "acorda" do idle e comeca o special.

---

## 2. WALK — "A Marcha da Corrupcao"

### Configuracao Phaser 3
```javascript
this.anims.create({
    key: 'gilmar_walk',
    frames: this.anims.generateFrameNumbers('gilmar_walk', { start: 0, end: 5 }),
    frameRate: 10,
    repeat: -1  // loop infinito
});
```

### Timing Frame-by-Frame

| Frame | Duracao | Descricao | Evento de Som | Evento de Particula |
|---|---|---|---|---|
| 0 | 100ms | Passo direito — impulso | — | — |
| 1 | 100ms | Passo direito — contato/impacto | SFX: passo pesado (thud) | Dinheiro cai do bolso |
| 2 | 100ms | Passo direito — recuperacao | — | Dinheiro flutua pro chao |
| 3 | 100ms | Passo esquerdo — impulso | — | — |
| 4 | 100ms | Passo esquerdo — contato/impacto | SFX: passo pesado (thud) | 2x notas de dinheiro caem |
| 5 | 100ms | Passo esquerdo — recuperacao | SFX: notificacao celular (bip) | Flash verde do celular |

**Duracao total do ciclo**: 600ms (~1.67 ciclos por segundo)

### Efeitos de Particula (durante Walk)

#### Trilha de Dinheiro
```javascript
// Emitter que cria notas de dinheiro caindo no chao atras do Gilmar
const dinheiro = this.add.particles('particle_dinheiro');
const dinheiroEmitter = dinheiro.createEmitter({
    x: sprite.x,
    y: sprite.y - 10,   // altura do bolso da toga
    speedY: { min: 20, max: 40 },
    speedX: { min: -10, max: 10 },
    angle: { min: 80, max: 100 },  // cai quase vertical
    rotate: { min: -30, max: 30 },
    scale: { start: 0.8, end: 0.6 },
    lifespan: 800,
    quantity: 1,
    frequency: -1,  // trigger manual nos frames de impacto
    tint: 0x3D8B3A
});

// Trigger nos frames 1 e 4 (impacto dos passos)
sprite.on('animationupdate', (anim, frame) => {
    if (frame.index === 1) dinheiroEmitter.explode(1);
    if (frame.index === 4) dinheiroEmitter.explode(2);  // passo esquerdo = mais dinheiro
});
```

#### Notificacao do Vorcaro (Frame 5)
```javascript
// Flash verde no celular a cada ciclo completo de walk
sprite.on('animationupdate', (anim, frame) => {
    if (frame.index === 5) {
        // Flash verde overlay no celular
        const flash = this.add.rectangle(
            sprite.x - 8, sprite.y - 16,
            3, 4, 0x40B840, 0.8
        );
        this.tweens.add({
            targets: flash,
            alpha: 0,
            duration: 100,
            onComplete: () => flash.destroy()
        });
    }
});
```

### Velocidade de Movimento
```javascript
// Gilmar e LENTO — velhinho baixinho
const GILMAR_WALK_SPEED = 60; // pixels por segundo (comparar: jogador ~120)
// Gilmar nunca corre. Nunca tem pressa. O deboche nao tem pressa.
```

### Transicoes
- **Walk -> Idle**: Frame 2 ou 5 (recuperacao) -> Frame 0 do idle. CORTE SECO.
- **Walk -> Attack**: QUALQUER frame -> Frame 0 do attack. Walk interrompe.
- **Walk -> Hit**: INTERROMPE instantaneo. Hit tem prioridade.

---

## 3. ATTACK — "Pasteleada"

### Configuracao Phaser 3
```javascript
this.anims.create({
    key: 'gilmar_attack',
    frames: this.anims.generateFrameNumbers('gilmar_attack', { start: 0, end: 2 }),
    frameRate: 10,
    repeat: 0  // NAO repete — executa uma vez
});
```

### Timing Frame-by-Frame

| Frame | Duracao | Descricao | Evento de Som | Evento de Gameplay |
|---|---|---|---|---|
| 0 | 100ms | Wind-up (puxa pastel pra tras) | SFX: whoosh reverso | — |
| 1 | 80ms | Arremesso + flash Teflon | SFX: arremesso + tink metalico | Spawna projetil `pastel_projectile` |
| 2 | 150ms | Gargalhada pos-ataque | SFX: gargalhada cinica (bordao) | — |

**Duracao total**: ~330ms (ataque RAPIDO — Gilmar e traicoeiro)

### Projetil: Pastel
```javascript
// Spawna no Frame 1 do attack
const pastel = this.physics.add.sprite(sprite.x + 16, sprite.y - 20, 'projectile_pastel');
pastel.setVelocity(
    Math.cos(angleToPlayer) * 200,  // velocidade do projetil
    Math.sin(angleToPlayer) * 200
);
pastel.setSize(32, 32);

// Particulas do pastel em voo (migalhas + oleo)
const trailEmitter = this.add.particles('particle_migalha').createEmitter({
    follow: pastel,
    speed: 20,
    scale: { start: 0.5, end: 0 },
    lifespan: 300,
    quantity: 1,
    frequency: 50,
    tint: [0xD4A855, 0xC8A832]  // migalhas e oleo
});

// Ao acertar o alvo
pastel.on('hit', () => {
    // Explosao de recheio
    const recheioExplosion = this.add.particles('particle_recheio');
    recheioExplosion.createEmitter({
        x: pastel.x, y: pastel.y,
        speed: { min: 30, max: 80 },
        angle: { min: 0, max: 360 },
        scale: { start: 1, end: 0 },
        lifespan: 500,
        quantity: 8,
        frequency: -1,
        tint: [0x8B4513, 0xC8A832, 0xD4A855]
    }).explode(8);
});
```

### Mecanica: Toga de Teflon (Defesa Passiva)
```javascript
// 33% chance de projetil VOLTAR pro atirador
onProjectileHit(projectile, gilmar) {
    if (Math.random() < 0.33) {
        // REFLETE o projetil
        projectile.setVelocity(
            -projectile.body.velocity.x * 0.8,
            -projectile.body.velocity.y * 0.8
        );
        
        // Visual: Flash Teflon na toga
        playTeflonFlash(gilmar);
        
        // Som: tink metalico de deflexao
        this.sound.play('sfx_teflon_deflect');
        
        // Texto flutuante
        showFloatingText(gilmar.x, gilmar.y - 30, "TEFLON!", '#C8A832');
    }
}

function playTeflonFlash(sprite) {
    // Onda de luz branca percorrendo a toga da esquerda pra direita
    const flash = this.add.sprite(sprite.x - 16, sprite.y, 'fx_teflon_wave');
    this.tweens.add({
        targets: flash,
        x: sprite.x + 16,
        alpha: { from: 0.6, to: 0 },
        duration: 150,
        onComplete: () => flash.destroy()
    });
}
```

### Cooldown do Ataque
```javascript
const GILMAR_ATTACK_COOLDOWN = 2000; // 2 segundos entre ataques
// Gilmar ataca devagar mas cada ataque e triplo (Repeticao Compulsiva)
// Na pratica: 3 pasteis por ataque, com 100ms de delay entre cada
```

### Transicoes
- **Attack -> Idle**: Frame 2 (gargalhada) -> Frame 3 do idle. CORTE SECO.
- **Attack -> Hit**: INTERROMPE no Frame 0 ou 1 (Frame 2 nao pode ser interrompido — invulneravel de riso)

---

## 4. DEATH — "O Ultimo Pastel"

### Configuracao Phaser 3
```javascript
this.anims.create({
    key: 'gilmar_death',
    frames: this.anims.generateFrameNumbers('gilmar_death', { start: 0, end: 3 }),
    frameRate: 6,  // MAIS LENTO que normal — morte dramatica
    repeat: 0
});
```

### Timing Frame-by-Frame

| Frame | Duracao | Descricao | Evento de Som | Evento de Particula |
|---|---|---|---|---|
| 0 | 166ms | Impacto — oculos deslocam | SFX: impacto pesado + vidro rachando | Oculos voam como particula |
| 1 | 200ms | Queda — papada murcha | SFX: som de balao esvaziando (bizzz) | Documentos HC voam dos bolsos |
| 2 | 250ms | Colapso — toga vira pasteis | SFX: som de fritura (psshhhh) | Chuva de dinheiro + pasteis brotando |
| 3 | ∞ (permanece) | Pilha de pasteis + oculos | SFX: silencio... depois brilho dourado | HC dourado flutuando |

**Duracao da sequencia**: ~616ms + frame final permanente

### Efeitos de Particula Detalhados

#### Frame 0: Oculos Voando
```javascript
// Os oculos se tornam uma particula independente que voa do rosto
sprite.on('animationupdate', (anim, frame) => {
    if (frame.index === 0) {
        const oculos = this.add.sprite(sprite.x, sprite.y - 28, 'particle_oculos');
        this.tweens.add({
            targets: oculos,
            x: sprite.x + Phaser.Math.Between(-20, 20),
            y: sprite.y + 10,
            angle: Phaser.Math.Between(-45, 45),
            duration: 600,
            ease: 'Bounce.easeOut',  // UNICA excecao de easing — oculos quicam no chao
            onComplete: () => {
                // Oculos ficam no chao ate frame final
                oculosNoChao = oculos;
            }
        });
    }
});
```

#### Frame 1: Documentos de Habeas Corpus Voando
```javascript
// 3-4 documentos saem dos bolsos da toga
if (frame.index === 1) {
    for (let i = 0; i < 4; i++) {
        const doc = this.add.sprite(sprite.x, sprite.y - 10, 'particle_habeas_doc');
        this.tweens.add({
            targets: doc,
            x: sprite.x + Phaser.Math.Between(-30, 30),
            y: sprite.y + Phaser.Math.Between(-40, -10),
            angle: Phaser.Math.Between(-180, 180),
            alpha: { from: 1, to: 0.3 },
            duration: 800,
            ease: 'Power1',  // documentos flutuam levemente
        });
    }
}
```

#### Frame 2: Toga Metamorfose em Pasteis + Chuva de Dinheiro
```javascript
// Particulas de dinheiro caem por todo o frame
if (frame.index === 2) {
    const chuva = this.add.particles('particle_dinheiro');
    chuva.createEmitter({
        x: { min: sprite.x - 20, max: sprite.x + 20 },
        y: sprite.y - 30,
        speedY: { min: 40, max: 80 },
        speedX: { min: -20, max: 20 },
        rotate: { min: -180, max: 180 },
        scale: { start: 0.8, end: 0.4 },
        lifespan: 1200,
        quantity: 2,
        frequency: 80,
        maxParticles: 12,
        tint: 0x3D8B3A
    });
    
    // Pasteis brotando onde a toga estava
    for (let i = 0; i < 5; i++) {
        this.time.delayedCall(i * 50, () => {
            const pastel = this.add.sprite(
                sprite.x + Phaser.Math.Between(-15, 15),
                sprite.y + Phaser.Math.Between(-10, 5),
                'particle_pastel_small'
            );
            pastel.setScale(0);
            this.tweens.add({
                targets: pastel,
                scale: { from: 0, to: Phaser.Math.FloatBetween(0.6, 1.0) },
                duration: 200,
            });
        });
    }
}
```

#### Frame 3: Corpo Final (Permanente)
```javascript
if (frame.index === 3) {
    // Destruir sprite animada, substituir por sprite estatica do "corpo"
    const corpo = this.add.sprite(sprite.x, sprite.y, 'gilmar_death', 3);
    corpo.setDepth(sprite.depth - 1);  // abaixo de outros personagens
    
    // HC dourado flutuante (loop)
    const hcFlutuante = this.add.sprite(sprite.x, sprite.y - 20, 'particle_habeas_golden');
    this.tweens.add({
        targets: hcFlutuante,
        y: sprite.y - 24,
        alpha: { from: 1, to: 0.6 },
        duration: 1000,
        yoyo: true,
        repeat: -1  // flutua infinitamente
    });
    // O HC dourado pode ser COLETAVEL pelo jogador
    hcFlutuante.setInteractive();
    
    sprite.destroy();  // remove sprite animada
}
```

### Screen Effects na Morte
```javascript
// Ao iniciar a death animation:
// 1. Camera shake leve (velhinho caiu — impacto no chao)
this.cameras.main.shake(300, 0.005);

// 2. Slow motion de 0.5s (drama)
this.time.timeScale = 0.5;
this.time.delayedCall(500, () => this.time.timeScale = 1.0);

// 3. Texto flutuante (bordao final)
showFloatingText(
    sprite.x, sprite.y - 40,
    "Na minha jurisdicao... na minha... na...",
    '#FFD700', 2000  // dourado, 2 segundos
);
```

---

## 5. HIT — "Indignacao Cinica"

### Configuracao Phaser 3
```javascript
this.anims.create({
    key: 'gilmar_hit',
    frames: this.anims.generateFrameNumbers('gilmar_hit', { start: 0, end: 1 }),
    frameRate: 10,
    repeat: 0
});
```

### Timing Frame-by-Frame

| Frame | Duracao | Descricao | Evento de Som |
|---|---|---|---|
| 0 | 100ms | Oculos torcem + papada vibra | SFX: "tsc!" (som de desaprovacao) |
| 1 | 100ms | Papada chacoalha (recuperacao) | SFX: "hmph!" (som de desdem) |

**Duracao total**: 200ms (RAPIDO — Gilmar se recupera depressa)

### Efeitos Visuais do Hit
```javascript
// Hit Flash (borda branca pulsante)
onGilmarHit(sprite, damage) {
    // Flash branco
    sprite.setTintFill(0xFFFFFF);
    this.time.delayedCall(50, () => sprite.clearTint());
    
    // Numero de dano flutuante
    showDamageNumber(sprite.x, sprite.y - 30, damage, '#CC3030');
    
    // Chance de 33% de Teflon refletir
    if (damage.isProjectile && Math.random() < 0.33) {
        // Cancelar dano, refletir projetil
        // (ver secao Attack -> Toga de Teflon)
    }
    
    // Play hit animation
    sprite.play('gilmar_hit');
    sprite.once('animationcomplete', () => {
        sprite.play('gilmar_idle');
    });
    
    // Micro-knockback (2px na direcao oposta ao hit)
    const knockbackAngle = Phaser.Math.Angle.Between(
        damage.source.x, damage.source.y, sprite.x, sprite.y
    );
    sprite.x += Math.cos(knockbackAngle) * 2;
    sprite.y += Math.sin(knockbackAngle) * 2;
}
```

### Transicoes
- **Hit -> Idle**: AUTOMATICO apos Frame 1. Sempre volta pro idle.
- **Hit -> Death**: Se HP <= 0, Frame 1 do hit -> Frame 0 do death. SEM idle entre.
- **Hit -> Hit**: Se novo hit durante hit animation, REINICIA do Frame 0 (stagger).

---

## 6. SPECIAL: HABEAS CORPUS TRIPLO — "Imunidade Juridica"

### Configuracao Phaser 3
```javascript
this.anims.create({
    key: 'gilmar_special_habeas',
    frames: this.anims.generateFrameNumbers('gilmar_special_habeas', { start: 0, end: 3 }),
    frameRate: 6,  // mais lento — ritual solene (cinico)
    repeat: 0
});
```

### Timing Frame-by-Frame

| Frame | Duracao | Descricao | Evento de Som | Evento de Gameplay |
|---|---|---|---|---|
| 0 | 166ms | Mao entra na toga | SFX: rustle de tecido | — |
| 1 | 200ms | Puxa 1 documento | SFX: papel desdobrando + brilho | Aura dourada comeca (fraca) |
| 2 | 250ms | 3 documentos (triplo!) | SFX: coral angelico SARCASTICO | Aura dourada EXPLODE |
| 3 | ∞ (ate acabar) | Invulnerabilidade ativa | SFX: hum dourado constante | INVULNERAVEL — dano = 0 |

### Mecanica de Invulnerabilidade
```javascript
activateHabeasCorpus(gilmar) {
    // Gilmar fica invulneravel 3 VEZES (nao por tempo — por HITS)
    gilmar.habeasCharges = 3;
    gilmar.isInvulnerable = true;
    
    // Aura visual
    const aura = this.add.sprite(gilmar.x, gilmar.y, 'fx_golden_aura');
    aura.play('aura_pulse');  // animacao de 2 frames pulsando
    
    // Display de cargas restantes (3 icones de documento sobre a cabeca)
    const chargeIcons = [];
    for (let i = 0; i < 3; i++) {
        const icon = this.add.sprite(
            gilmar.x - 10 + (i * 10),
            gilmar.y - 38,
            'icon_habeas_charge'
        );
        chargeIcons.push(icon);
    }
    
    // Ao levar hit enquanto invulneravel:
    gilmar.onHitWhileInvulnerable = () => {
        gilmar.habeasCharges--;
        
        // Remove um icone de carga
        const icon = chargeIcons.pop();
        icon.destroy();
        
        // Texto flutuante
        showFloatingText(gilmar.x, gilmar.y - 30,
            `HC ${3 - gilmar.habeasCharges}/3!`, '#FFD700');
        
        // Som de papel rasgando
        this.sound.play('sfx_paper_tear');
        
        // Flash dourado no corpo
        gilmar.setTint(0xFFD700);
        this.time.delayedCall(100, () => gilmar.clearTint());
        
        if (gilmar.habeasCharges <= 0) {
            // Acabaram os habeas corpus
            gilmar.isInvulnerable = false;
            aura.destroy();
            showFloatingText(gilmar.x, gilmar.y - 30,
                "Sem HC! Sem HC! Sem HC!", '#CC3030');
        }
    };
}
```

### Cooldown
```javascript
const HABEAS_COOLDOWN = 15000; // 15 segundos entre usos
// Gilmar usa quando HP cai abaixo de 50%, 25%, e 10%
```

---

## 7. SPECIAL: STF DA PASTELARIA — "Hora do Lanche"

### Configuracao Phaser 3
```javascript
this.anims.create({
    key: 'gilmar_special_pastelaria',
    frames: this.anims.generateFrameNumbers('gilmar_special_pastelaria', { start: 0, end: 5 }),
    frameRate: 8,
    repeat: 0
});
```

### Timing Frame-by-Frame

| Frame | Duracao | Descricao | Evento de Som | Evento de Gameplay |
|---|---|---|---|---|
| 0 | 125ms | Invocacao (bate palmas) | SFX: clap + rumble subterraneo | Fissura no chao |
| 1 | 150ms | Balcao aparece | SFX: madeira brotando + oleo fervendo | Spawna objeto `balcao_pastelaria` |
| 2 | 125ms | Pega pastel | SFX: oleo borbulhando intenso | — |
| 3 | 200ms | Mordida extase | SFX: mordida CROCANTE + gemido de prazer | INVULNERAVEL comeca |
| 4 | 150ms | Oleo espirra (AoE) | SFX: PSSSHH (oleo espirrando) | Dano em area ao redor |
| 5 | 125ms | Satisfacao (arroto) | SFX: arroto discreto (prrp) | Invulnerabilidade termina |

**Duracao total**: ~875ms para animacao + 5s de invulnerabilidade durante cena

### Objeto: Balcao de Pastelaria
```javascript
spawnBalcaoPastelaria(gilmar) {
    const balcao = this.add.sprite(gilmar.x, gilmar.y + 10, 'object_balcao');
    balcao.setDepth(gilmar.depth - 1);
    
    // Balcao emerge do chao (tween de entrada)
    balcao.y += 30;  // comeca abaixo do chao
    balcao.setAlpha(0);
    this.tweens.add({
        targets: balcao,
        y: gilmar.y + 10,
        alpha: 1,
        duration: 300,
        ease: 'Back.easeOut'  // bounce de entrada
    });
    
    // Particulas de oleo borbulhando CONTINUAMENTE enquanto o balcao existe
    const oleoEmitter = this.add.particles('particle_oleo').createEmitter({
        x: balcao.x,
        y: balcao.y - 8,
        speed: { min: 10, max: 30 },
        angle: { min: 250, max: 290 },
        scale: { start: 0.5, end: 0 },
        lifespan: 400,
        quantity: 1,
        frequency: 100,
        tint: 0xC8A832
    });
    
    // Vapor subindo
    const vaporEmitter = this.add.particles('particle_vapor').createEmitter({
        x: balcao.x,
        y: balcao.y - 12,
        speedY: -20,
        alpha: { start: 0.3, end: 0 },
        lifespan: 600,
        quantity: 1,
        frequency: 150,
        tint: 0xFFFFFF
    });
    
    // Invulnerabilidade enquanto o balcao existe
    gilmar.isInvulnerable = true;
    
    // Duracao: 5 segundos
    this.time.delayedCall(5000, () => {
        // Balcao afunda de volta
        this.tweens.add({
            targets: balcao,
            y: balcao.y + 30,
            alpha: 0,
            duration: 400,
            onComplete: () => {
                balcao.destroy();
                oleoEmitter.stop();
                vaporEmitter.stop();
                gilmar.isInvulnerable = false;
            }
        });
    });
    
    // AREA DE EFEITO: inimigos proximos ganham pastel e ficam stunados
    const stunZone = this.add.zone(balcao.x, balcao.y, 80, 80);
    this.physics.add.existing(stunZone, true);
    this.physics.add.overlap(stunZone, enemies, (zone, enemy) => {
        if (!enemy.hasReceivedPastel) {
            enemy.hasReceivedPastel = true;
            // Stun de 2 segundos
            enemy.stun(2000);
            // Visual: pastel aparece na mao do inimigo
            const enemyPastel = this.add.sprite(enemy.x + 5, enemy.y - 10, 'particle_pastel_small');
            showFloatingText(enemy.x, enemy.y - 20, "Pastel?!", '#D4A040');
            this.time.delayedCall(2000, () => {
                enemy.hasReceivedPastel = false;
                enemyPastel.destroy();
            });
        }
    });
}
```

### Transicoes
- **Pastelaria -> Idle**: Frame 5 (satisfacao) -> Frame 3 do idle (mastigando). Transicao TEMATICA.
- **Pastelaria interrompida**: NAO PODE SER INTERROMPIDA. Gilmar e invulneravel durante.

---

## 8. SPECIAL: BRIGA COM BARROSO — "O Embate Historico"

### Configuracao Phaser 3
```javascript
this.anims.create({
    key: 'gilmar_special_briga',
    frames: this.anims.generateFrameNumbers('gilmar_special_briga', { start: 0, end: 7 }),
    frameRate: 8,
    repeat: 0
});
```

### Condicao de Ativacao
```javascript
// Verifica a cada 2 segundos se Barroso esta no mapa
this.time.addEvent({
    delay: 2000,
    loop: true,
    callback: () => {
        if (barroso && barroso.active && !gilmar.isFighting) {
            const distance = Phaser.Math.Distance.Between(
                gilmar.x, gilmar.y, barroso.x, barroso.y
            );
            if (distance < 200) {  // raio de deteccao
                triggerBrigaGilmarBarroso(gilmar, barroso);
            }
        }
    }
});
```

### Timing Frame-by-Frame

| Frame | Duracao | Descricao | Evento de Som | Evento de Gameplay |
|---|---|---|---|---|
| 0 | 125ms | Detecta Barroso (congela) | SFX: som de alerta/radar | PARA de atacar jogador |
| 1 | 150ms | Vira pro Barroso | SFX: toga esvoaçando | Gilmar fica IMUNE ao jogador |
| 2 | 200ms | "VAGABUNDO!" #1 | VOZ: "Vagabundo!" (grito 1) | Screen shake LEVE |
| 3 | 200ms | "VAGABUNDO!" #2 | VOZ: "Vagabundo!" (grito 2, mais alto) | Screen shake MEDIO |
| 4 | 250ms | "VAGABUNDO!" #3 | VOZ: "VAGABUNDO!" (grito 3, MAXIMO) | Screen shake FORTE |
| 5 | 125ms | Empurrao (avanca) | SFX: passo de investida | Gilmar se move em direcao a Barroso |
| 6 | 150ms | Empurrao (contato) | SFX: impacto fisico (THUMP) | Dano em Barroso (e Barroso dano em Gilmar) |
| 7 | 200ms | Pose de vitoria | SFX: risada de satisfacao | 2s de deboche, depois volta ao idle |

**Duracao total da briga**: ~1.4s de animacao + 10s de briga total (loops frames 2-6 repetem)

### Mecanica da Briga Completa
```javascript
function triggerBrigaGilmarBarroso(gilmar, barroso) {
    gilmar.isFighting = true;
    barroso.isFighting = true;
    
    // AMBOS param de atacar o jogador
    gilmar.targetPlayer = false;
    barroso.targetPlayer = false;
    
    // Caminham um em direcao ao outro
    moveTowards(gilmar, barroso, 80);  // velocidade de briga
    moveTowards(barroso, gilmar, 80);
    
    // Quando se encontram (distancia < 30px)
    onMeeting(() => {
        // LOOP de briga por 10 segundos
        let brigaTimer = 10000;
        
        const brigaLoop = this.time.addEvent({
            delay: 1400,  // cada ciclo de briga
            repeat: 7,    // ~10 segundos
            callback: () => {
                gilmar.play('gilmar_special_briga');
                barroso.play('barroso_special_briga');
                
                // Dano mutuo
                gilmar.damage(5);  // Barroso causa 5
                barroso.damage(5); // Gilmar causa 5
                
                // Textos flutuantes alternados
                showFloatingText(gilmar.x, gilmar.y - 30,
                    "VAGABUNDO!", '#CC3030');
                this.time.delayedCall(300, () => {
                    showFloatingText(barroso.x, barroso.y - 30,
                        "HORRIVEL!", '#CC3030');
                });
                
                // Screen shake progressivo
                this.cameras.main.shake(200, 0.003);
            }
        });
        
        // APOS 10 SEGUNDOS:
        this.time.delayedCall(10000, () => {
            brigaLoop.destroy();
            gilmar.isFighting = false;
            barroso.isFighting = false;
            gilmar.targetPlayer = true;
            barroso.targetPlayer = true;
            
            // Separacao dramatica
            gilmar.x -= 20;
            barroso.x += 20;
            gilmar.play('gilmar_idle');
            barroso.play('barroso_idle');
            
            // Texto final
            showFloatingText(gilmar.x, gilmar.y - 30,
                "Eu sempre ganho!", '#FFD700');
        });
    });
    
    // DURANTE A BRIGA: jogador pode passar LIVRE
    // Mostrar texto na tela: "Eles estao brigando! Aproveite!"
    showScreenMessage("Os ministros estao brigando entre si!\nAproveite para passar!", 3000);
}
```

### Particulas e Efeitos da Briga
```javascript
// Durante o loop de briga:

// 1. Onomatopeias flutuantes
const onomatopeias = [
    "VAGABUNDO!", "HORRIVEL!", "PASTELEIRO!", "DESGRACA!",
    "INCOMPETENTE!", "VENDIDO!", "CINICO!", "ARROGANTE!"
];

// 2. Estrelas de impacto nos empurroes (estilo quadrinhos)
function showImpactStar(x, y) {
    const star = this.add.sprite(x, y, 'fx_impact_star');
    star.setScale(0);
    this.tweens.add({
        targets: star,
        scale: { from: 0, to: 1.5 },
        alpha: { from: 1, to: 0 },
        duration: 300,
        onComplete: () => star.destroy()
    });
}

// 3. Nuvem de poeira da briga (estilo cartoon)
const dustCloud = this.add.particles('particle_dust');
dustCloud.createEmitter({
    x: (gilmar.x + barroso.x) / 2,
    y: (gilmar.y + barroso.y) / 2,
    speed: { min: 20, max: 60 },
    angle: { min: 0, max: 360 },
    alpha: { start: 0.4, end: 0 },
    lifespan: 500,
    quantity: 2,
    frequency: 200,
    tint: [0x8A8580, 0xC4A265]
});

// 4. Migalhas de pastel voando da toga do Gilmar durante briga
// (o pastel sobrevive a tudo)
```

---

## 9. ULTIMATE: HABEAS CORPUS UNIVERSAL — "Ninguem Morre na Minha Jurisdicao"

### Condicao de Ativacao
```javascript
// Gilmar usa quando HP cai abaixo de 15% E esta encurralado
// OU aleatoriamente 1x a cada 60 segundos de combate
const ULTIMATE_HP_THRESHOLD = 0.15;
const ULTIMATE_COOLDOWN = 60000;
```

### Sequencia de Animacao (reutiliza frames do Habeas Corpus + efeitos extras)

#### Fase 1: Proclamacao (1s)
```javascript
// Gilmar ergue as duas maos pro alto
// Usa frames customizados (ou overlay sobre frame 2 do habeas)
gilmar.play('gilmar_special_habeas');

// Texto dramatico em tela cheia
showFullScreenText(
    "HABEAS CORPUS UNIVERSAL!",
    '#FFD700', 1000,
    { fontSize: '24px', fontFamily: 'Impact', stroke: '#1A1A18', strokeThickness: 3 }
);

// Camera zoom in no Gilmar
this.cameras.main.zoomTo(1.5, 500);
this.cameras.main.pan(gilmar.x, gilmar.y, 500);
```

#### Fase 2: Invulnerabilidade Global (5s)
```javascript
// TODOS ficam invulneraveis — jogador, aliados, inimigos
function activateHabeasUniversal() {
    const allEntities = [...enemies, player, ...allies];
    
    allEntities.forEach(entity => {
        entity.isInvulnerable = true;
        
        // Aura dourada em TODOS
        const aura = this.add.sprite(entity.x, entity.y, 'fx_golden_aura');
        aura.play('aura_pulse');
        entity.habeasAura = aura;
        
        // Borda dourada
        entity.setTint(0xFFD700);
    });
    
    // O jogo PARA — ninguem pode ser atacado
    // Mostrar contador: "5... 4... 3... 2... 1..."
    for (let i = 5; i >= 1; i--) {
        this.time.delayedCall((5 - i) * 1000, () => {
            showFullScreenText(`${i}`, '#FFD700', 800, { fontSize: '48px' });
        });
    }
    
    // Gilmar ri durante os 5 segundos
    this.time.addEvent({
        delay: 1500,
        repeat: 2,  // 3 vezes (x3, claro)
        callback: () => {
            showFloatingText(gilmar.x, gilmar.y - 40,
                "Na MINHA jurisdicao!", '#FFD700');
            this.sound.play('sfx_gilmar_riso');
        }
    });
}
```

#### Fase 3: Fim da Invulnerabilidade (1s)
```javascript
this.time.delayedCall(5000, () => {
    const allEntities = [...enemies, player, ...allies];
    
    allEntities.forEach(entity => {
        entity.isInvulnerable = false;
        entity.habeasAura.destroy();
        entity.clearTint();
    });
    
    // Camera volta ao normal
    this.cameras.main.zoomTo(1, 500);
    
    // Texto final (bordao triplo)
    showFloatingText(gilmar.x, gilmar.y - 40,
        "Ninguem morre na MINHA jurisdicao,\nna MINHA jurisdicao,\nna MINHA jurisdicao!",
        '#FFD700', 3000);
    
    // Gilmar gargalha (frame 2 do attack)
    gilmar.play('gilmar_attack');
});
```

### Efeitos Globais durante Ultimate
```javascript
// 1. Filtro dourado na tela inteira
this.cameras.main.setPostPipeline('GoldenFilter');

// 2. Particulas douradas caindo como chuva em toda a tela
const goldenRain = this.add.particles('particle_golden');
goldenRain.createEmitter({
    x: { min: 0, max: this.cameras.main.width },
    y: -10,
    speedY: { min: 30, max: 60 },
    alpha: { start: 0.6, end: 0 },
    lifespan: 2000,
    quantity: 3,
    frequency: 100,
    tint: 0xFFD700
});

// 3. Background music muda para versao "epica sarcastica"
// (coro angelico proposital, exageradamente dramatico)
this.sound.play('bgm_habeas_universal', { volume: 0.8 });

// 4. Texto no topo da tela piscando:
// "NINGUEM PODE MORRER" em dourado
```

---

## 10. TABELA RESUMO DE ANIMACOES

| Animacao | Key Phaser | Frames | FPS | Loop | Duracao | Prioridade |
|---|---|---|---|---|---|---|
| Idle | `gilmar_idle` | 4 | 8 | Sim | 525ms/ciclo | 0 (menor) |
| Walk | `gilmar_walk` | 6 | 10 | Sim | 600ms/ciclo | 1 |
| Attack | `gilmar_attack` | 3 | 10 | Nao | 330ms | 2 |
| Hit | `gilmar_hit` | 2 | 10 | Nao | 200ms | 4 (alta) |
| Death | `gilmar_death` | 4 | 6 | Nao | 616ms+ | 5 (maxima) |
| Habeas Corpus | `gilmar_special_habeas` | 4 | 6 | Nao | ~800ms + efeito | 3 |
| Pastelaria | `gilmar_special_pastelaria` | 6 | 8 | Nao | ~875ms + 5s efeito | 3 |
| Briga Barroso | `gilmar_special_briga` | 8 | 8 | Sim* | ~1.4s x loops (10s) | 3 |
| Ultimate | (composto) | — | — | Nao | ~7s total | 5 (maxima) |

*Briga faz loop dos frames 2-6 durante 10 segundos

### Sistema de Prioridade de Animacao
```javascript
// Prioridade 5 (Death/Ultimate) interrompe TUDO
// Prioridade 4 (Hit) interrompe idle, walk, attack
// Prioridade 3 (Specials) interrompe idle, walk. NAO interrompe attack mid-frame
// Prioridade 2 (Attack) interrompe idle, walk
// Prioridade 1 (Walk) interrompe idle
// Prioridade 0 (Idle) NAO interrompe nada — e o fallback

const ANIM_PRIORITY = {
    'gilmar_idle': 0,
    'gilmar_walk': 1,
    'gilmar_attack': 2,
    'gilmar_special_habeas': 3,
    'gilmar_special_pastelaria': 3,
    'gilmar_special_briga': 3,
    'gilmar_hit': 4,
    'gilmar_death': 5
};

function playAnimIfHigherPriority(sprite, newAnim) {
    const currentPriority = ANIM_PRIORITY[sprite.anims.currentAnim?.key] || 0;
    const newPriority = ANIM_PRIORITY[newAnim] || 0;
    if (newPriority >= currentPriority) {
        sprite.play(newAnim);
    }
}
```

---

## 11. SONS E BORDOES — TIMING

### Tabela de Audio Cues
| Trigger | Audio File | Timing | Volume | Condicao |
|---|---|---|---|---|
| Idle Frame 1 | `sfx_glasses_tink.wav` | Instantaneo | 0.3 | Sempre |
| Idle Frame 2 | `sfx_bite_crunch.wav` | Instantaneo | 0.5 | Sempre |
| Walk Frame 1,4 | `sfx_heavy_step.wav` | Instantaneo | 0.4 | Sempre |
| Walk Frame 5 | `sfx_phone_bip.wav` | Instantaneo | 0.2 | 50% chance |
| Attack Frame 0 | `sfx_whoosh_reverse.wav` | Instantaneo | 0.5 | Sempre |
| Attack Frame 1 | `sfx_throw.wav` + `sfx_teflon.wav` | Instantaneo + 50ms delay | 0.5 | Sempre |
| Attack Frame 2 | `vox_gilmar_laugh.wav` | Instantaneo | 0.6 | 70% chance |
| Hit Frame 0 | `sfx_tsc.wav` | Instantaneo | 0.5 | Sempre |
| Death Frame 0 | `sfx_impact_heavy.wav` + `sfx_glass_crack.wav` | Simultaneo | 0.7 | Sempre |
| Death Frame 2 | `sfx_frying.wav` | Fade in 200ms | 0.5 | Sempre |
| Habeas Frame 2 | `sfx_angelic_choir_sarcastic.wav` | Instantaneo | 0.6 | Sempre |
| Briga Frame 2 | `vox_gilmar_vagabundo_1.wav` | Instantaneo | 0.8 | Sempre |
| Briga Frame 3 | `vox_gilmar_vagabundo_2.wav` | Instantaneo | 0.9 | Sempre |
| Briga Frame 4 | `vox_gilmar_vagabundo_3.wav` | Instantaneo | 1.0 | Sempre |
| Ultimate | `bgm_habeas_universal.wav` | Instantaneo | 0.8 | Sempre |
| Ultimate fim | `vox_gilmar_jurisdicao.wav` | No frame final | 0.7 | Sempre |

### Bordoes com Timing TTS
| Bordao | Emocao | Repeticao | Uso |
|---|---|---|---|
| "Sou fa, sou fa, sou fa" | Cinismo alegre | x3 (padrao) | Ao encontrar inimigo poderoso |
| "Pior que nao foi" | Deboche | x3 | Ao desviar ataque (Teflon) |
| "Faz o gosto" | Desdem | x3 | Ao atacar |
| "Vagabundo!" | Furia total | x3 (escalando) | Na briga com Barroso |
| "Era so um jantar" | Cinismo defensivo | x3 | Ao usar Contato do Vorcaro |
| "Na minha jurisdicao" | Triunfo | x3 | No ultimate |
| "Pastel?" | Alegria genuina | x1 | Ao invocar pastelaria |
| "E so isso?" | Desdem | x1 | Ao tomar hit |
