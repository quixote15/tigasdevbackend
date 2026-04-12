# HUGO MOTTA (O Presidente da Camara dos Mortos) - Animation Specification

## Principios de Animacao

### Estilo Geral
- **Frame Rate:** 8fps (JERKY mas CONTROLADO -- diferente do caos dos outros personagens)
- **Tecnica:** Micro-movimentos perturbadores em corpo aparentemente estatico
- **Easing:** Stepped easing (cortes bruscos), exceto orelhas e dedos (movement smooth SUTIL)
- **Principio Core:** Hugo parece PARADO mas detalhes se movem independentemente. O horror esta nos micro-tells: orelha girando, dedos mexendo, sorriso congelado, olhos que nao piscam.

### Hierarquia de Movimento
1. **SORRISO** -- NUNCA se move (exceto hit e death). A ausencia de movimento E o elemento perturbador.
2. **OLHOS** -- NUNCA piscam (exceto hit frame 0 e death). Pupilas se movem RARAMENTE (1-2px, calculando).
3. **ORELHAS** -- Movem-se INDEPENDENTE da cabeca. Giram como antenas parabolicas captando informacao.
4. **DEDOS (6)** -- Mexem sutilmente. O sexto dedo tem ciclo proprio de movimento.
5. **CELULAR** -- Presente em 80% dos frames. Tela pisca com "VORCARO" periodicamente.
6. **CORPO** -- MINIMO movimento. Hugo e o personagem que MENOS se move fisicamente. O poder e invisivel.

### Contraste com Outros Personagens
| Personagem | Estilo de Animacao          | Frequencia de Movimento |
|------------|-----------------------------|-----------------------|
| Maduro     | Caotico, ridiculo, tudo mexe| MAXIMO                 |
| Xandao     | Agressivo, forte, impactante| ALTO                   |
| Lula       | Carismático, expressivo     | MEDIO-ALTO             |
| **Hugo**   | **Estatico, sutil, perturbador** | **MINIMO**        |
| Bolsonaro  | Erratico, nervoso           | ALTO                   |

---

## Animacoes Detalhadas

### 1. IDLE
- **Frames:** 4
- **FPS:** 8
- **Loop:** Sim
- **Duracao Total:** 0.5s por ciclo

#### Sequencia de Frames:
```
Frame 0 (125ms): Pose base. Sorriso fixo. Olhos abertos. Celular na mao. Mao no bolso.
Frame 1 (125ms): Tela do celular pisca "VORCARO". Pupilas desviam 1px pro celular. Sorriso INTACTO.
Frame 2 (125ms): Orelha direita gira 10-15 graus (antena). Resto do corpo IMÓVEL.
Frame 3 (125ms): Dedos no bolso mexem. Sexto dedo se destaca. Micro-movimento no bolso.
```

#### Principio de Animacao:
- O idle parece QUASE ESTATICO a distancia. So de perto voce ve os micro-movimentos.
- Cada frame muda UMA coisa sutil. Nunca duas ao mesmo tempo. DISCIPLINA visual.
- O corpo principal NAO se move. Zero bounce, zero sway. Imobilidade perturbadora.
- O "VORCARO" na tela aparece a cada 2-3 ciclos (nao todo ciclo -- para surpreender)
- A orelha rotaciona e volta suavemente (unico movimento smooth do personagem)

#### Codigo Phaser 3:
```javascript
// Idle animation -- sutilmente perturbador
this.anims.create({
    key: 'hugo_idle',
    frames: this.anims.generateFrameNumbers('hugo_idle', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1
});

// SEM jitter effect (diferente de todos os outros personagens)
// Hugo NAO treme. A imobilidade E o efeito.

// Efeito "VORCARO" na tela (overlay separado)
let idleCycleCount = 0;
hugoSprite.on('animationrepeat', () => {
    idleCycleCount++;
    if (idleCycleCount % 3 === 0) { // a cada 3 ciclos
        this.showVorcaroFlash(hugoSprite.x + 8, hugoSprite.y - 5, 200); // flash de 200ms
    }
});
```

---

### 2. WALK
- **Frames:** 6
- **FPS:** 10
- **Loop:** Sim (com variacao a cada 2 ciclos)
- **Duracao Total:** 0.6s por ciclo

#### Sequencia de Frames:
```
Frame 0 (100ms): Passo direito. Postura PERFEITA. Celular pronto. 6 dedos visiveis na mao esquerda.
Frame 1 (100ms): Transicao. Bounce MINIMO (1px). Terno nao amassa.
Frame 2 (100ms): Passo esquerdo. Orelha gira levemente captando informacao.
Frame 3 (100ms): Transicao. Olhos descem 2px pro celular. "VORCARO" flash.
Frame 4 (100ms): CUMPRIMENTO AUTOMATICO (a cada 2 ciclos). Mao abre -- 6 dedos claramente visiveis.
Frame 5 (100ms): Volta ao normal. Mao fecha. Como se nada tivesse acontecido.
```

#### Logica de Variacao:
```
Ciclo 1: Frame 0 -> 1 -> 2 -> 3 -> 0 -> 1... (sem cumprimento)
Ciclo 2: Frame 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0... (com cumprimento)
```

#### Efeitos de Particula no Walk:
- **SEM poeira nos pes.** Hugo nao faz impacto no chao. Ele DESLIZA quase.
- **Celular flash:** Tela pisca no Frame 3 (cada 2 ciclos)
- **Sombra sutil:** Sombra se move ANTES do corpo (1 frame de anticipacao -- como se a sombra soubesse o caminho)

#### Principio de Animacao:
- O walk de Hugo e EFICIENTE. Sem desperdicio de energia. Sem drama.
- Passos sao CURTOS e RAPIDOS (corpo se desloca pouco por frame, alta frequencia)
- ZERO tropeco (diferente de Maduro). Hugo NUNCA erra um passo.
- O cumprimento e REFLEXO -- ele nao decide fazer, o corpo faz sozinho
- Sorriso INTACTO durante todo o walk. Olhos FIXOS na frente.
- A sombra ter anticipacao cria UNCANNY VALLEY sutil

#### Codigo Phaser 3:
```javascript
// Walk with automatic greeting
let walkCycleCount = 0;

this.anims.create({
    key: 'hugo_walk_normal',
    frames: this.anims.generateFrameNumbers('hugo_walk', { frames: [0, 1, 2, 3] }),
    frameRate: 10,
    repeat: 0
});

this.anims.create({
    key: 'hugo_walk_greet',
    frames: this.anims.generateFrameNumbers('hugo_walk', { frames: [0, 1, 2, 3, 4, 5] }),
    frameRate: 10,
    repeat: 0
});

// Shadow anticipation effect
hugoShadow.x = hugoSprite.x + velocityX * 0.1; // sombra 1 frame a frente
hugoShadow.y = hugoSprite.y + velocityY * 0.1;
```

---

### 3. ATTACK -- Articulacao Suprema
- **Frames:** 8
- **FPS:** 8
- **Loop:** Nao
- **Duracao Total:** 1.0s

#### Timeline Detalhada:
```
Frame 0 (125ms): AVALIACAO. Olhos escaneiam (pupilas movem esq->dir pela 1a vez).
  - Efeito: Nenhum visivel. Anticipacao FRIA.
  - Sorriso diminui (RARO -- concentracao)
  - Maos entrelaçam (12 dedos visiveis -- perturbador)
  
Frame 1 (125ms): O GESTO. Uma mao (6 dedos) levanta, palma para frente.
  - Efeito: Spawn distorcao de ar (heat shimmer, projetil 'influencia')
  - Efeito: Ondulacao SUTIL ao redor da mao (1-2px wave)
  - Sorriso volta ao MAXIMO
  
Frame 2 (125ms): ONDAS DE INFLUENCIA. Distorcao se expande.
  - Efeito: Projeteis de influencia se expandem radialmente
  - Efeito: Micro-icones de documentos e selos dentro das ondas
  - Hugo PARADO, mao erguida, sorriso fixo
  - SEM screen shake (diferente de Maduro -- poder SILENCIOSO)
  
Frame 3 (125ms): NPCs MUDAM. Ondas atingem inimigos.
  - Efeito: Flash dourado (#FFD700) nos olhos dos inimigos atingidos (1 frame)
  - Gameplay: Inimigos param de atacar Hugo, atacam o player
  - Hugo abaixa mao. Tira celular. Checa notificacao. CALMA TOTAL.
  - Dano: Nao causa dano direto -- muda COMPORTAMENTO
  
Frame 4 (125ms): CONTROLE. Linhas de marionete aparecem.
  - Efeito: Linhas finas cinza (#5A5A5A, 1px) de Hugo para cada NPC afetado
  - Efeito: Linhas quase invisiveis -- puppet strings
  - Hugo: maos nos bolsos, celular checando, sorriso amplo
  - Gameplay: NPCs afetados duram 5 segundos
  
Frame 5 (125ms): ENFRAQUECE. Linhas ficam mais finas.
  - Efeito: Linhas 50% mais transparentes
  - Hugo: olhos se estreitam 1px (calculando duracao restante)
  
Frame 6 (125ms): PERDA. Linhas se rompem.
  - Efeito: Cada linha rompe com micro-flash branco
  - Efeito: NPCs voltam ao normal (flash dourado inverso nos olhos)
  - Hugo: guarda celular. Micro-irritacao (sorriso diminui 1px)
  
Frame 7 (125ms): RESET. Tudo "normal".
  - Efeito: Zero evidencia visual do ataque
  - Hugo: posicao idle perfeita. Sorriso padrao. Como se nada.
  - Cooldown: 10 segundos
```

#### Hitbox da Influencia:
```
Tipo: Radial (cone direcional opcional)
Raio: 80px (MAIOR que Maduro -- alcance politico e longo)
Duracao do efeito: 5 segundos
Efeito: NPCs atingidos param de atacar Hugo e atacam targets aliados do player
Maximo de NPCs afetados: 4
```

#### Codigo Phaser 3:
```javascript
// Articulacao Suprema -- muda comportamento de inimigos
function articulacaoSuprema(hugo, enemies) {
    const range = 80;
    const maxTargets = 4;
    const duration = 5000;
    
    let affected = enemies
        .filter(e => Phaser.Math.Distance.Between(hugo.x, hugo.y, e.x, e.y) < range)
        .slice(0, maxTargets);
    
    affected.forEach(enemy => {
        // Flash dourado nos olhos
        flashEyes(enemy, '#FFD700', 125);
        
        // Linha de marionete (quase invisivel)
        const line = drawPuppetString(hugo, enemy, '#5A5A5A', 0.3);
        
        // Muda comportamento
        enemy.setTarget('player'); // para de atacar Hugo
        enemy.setAggression(1.5);  // mais agressivo contra player
        
        // Timer para reverter
        this.time.delayedCall(duration, () => {
            enemy.resetBehavior();
            line.destroy();
            flashEyes(enemy, '#FFD700', 125); // flash inverso
        });
    });
}
```

---

### 4. SKILL 1 -- Pauta Secreta
- **Frames:** 6
- **FPS:** 8
- **Loop:** Nao
- **Duracao Total:** 0.75s + efeitos silenciosos por 8s

#### Timeline Detalhada:
```
Frame 0 (125ms): DOCUMENTO. Tira papel sigiloso do terno.
  - Efeito: Gesto furtivo (quase esconde do viewer)
  - Efeito: Selo vermelho "CONFIDENCIAL" visivel
  - Sorriso DIMINUI (seriedade rara)
  - Orelhas viram para fora (checando)
  
Frame 1 (125ms): LEITURA. Desdobra parcialmente (nunca revela tudo).
  - Efeito: Olhos descem pela 1a vez (olha para baixo)
  - Efeito: 6 dedos seguram e ESCONDEM conteudo
  
Frame 2 (125ms): ATIVA. Dobra, guarda, gesto de "ok" com 6 dedos.
  - Efeito: NADA VISIVEL MUDA NO MAPA
  - Gameplay: Regras comecam a mudar SILENCIOSAMENTE
  - Sorriso volta ao maximo
  
Frame 3 (125ms): EFEITO INVISIVEL. Hugo volta a idle.
  - Efeito: Mini-icone engrenagem (8x8px, 30% opacidade, canto do frame)
  - Gameplay: Spawn rates mudando, drops alterando
  
Frame 4 (125ms): REGRAS MUDANDO. Engrenagem gira mais rapido.
  - Hugo anda normalmente (pode ativar walk)
  - Gameplay: Dificuldade oscila silenciosamente
  
Frame 5 (125ms): FIM SILENCIOSO. Engrenagem some.
  - Efeito: Celular recebe notificacao (tela pisca)
  - Gameplay: Novas regras fixadas por 8 segundos
  - Cooldown: 12 segundos
  - NINGUEM sabe quem fez
```

#### Efeitos da Pauta Secreta (8 segundos):
```javascript
const PAUTA_EFFECTS = {
    // Efeitos sao sorteados -- 2 de 5 por ativacao
    'spawn_increase': {
        desc: 'Aumenta spawn de inimigos em 50%',
        multiplier: 1.5
    },
    'drop_decrease': {
        desc: 'Diminui chance de drop em 30%',
        multiplier: 0.7
    },
    'speed_increase': {
        desc: 'Inimigos 20% mais rapidos',
        multiplier: 1.2
    },
    'boss_buff': {
        desc: 'Hugo ganha +15% ataque',
        multiplier: 1.15
    },
    'heal_reduce': {
        desc: 'Cura do player reduzida em 25%',
        multiplier: 0.75
    }
};

// Ativar 2 efeitos aleatorios
function activatePautaSecreta() {
    const effects = Phaser.Utils.Array.Shuffle(Object.keys(PAUTA_EFFECTS)).slice(0, 2);
    effects.forEach(key => {
        applyEffect(PAUTA_EFFECTS[key], 8000); // 8 segundos
    });
    // SEM feedback visual pro player (ele precisa PERCEBER)
}
```

---

### 5. SKILL 2 -- Conexao com o Master
- **Frames:** 6
- **FPS:** 8
- **Loop:** Nao
- **Duracao Total:** 0.75s + buff de 10s

#### Timeline Detalhada:
```
Frame 0 (125ms): CELULAR TOCA. Vibracao visual.
  - Efeito: Linhas de vibracao no celular (1-2px)
  - Efeito: Tela "VORCARO" vermelho piscante
  - Orelhas se eriçam (ALERTA)
  
Frame 1 (125ms): ATENDE. Celular na orelha (orelha engole metade).
  - Efeito: Hugo vira de lado (posicao secreta)
  - Sorriso menor (concentracao)
  - Mao livre faz gesto "espera"
  
Frame 2 (125ms): LINK ESTABELECIDO. Linha vermelha sai do celular.
  - Efeito: Spawn linha vermelha (#FF3333) pulsante para fora do frame
  - Efeito: Micro-cifraoes ($) fluem ao longo da linha
  - Efeito: Micro-nod de assentimento
  - Gameplay: Conexao ativa -- +30% defesa para Hugo
  
Frame 3 (125ms): DEFESA ATIVA. Halo dourado sutil.
  - Efeito: Halo (#FFD700, 15-20% opacidade) ao redor de Hugo
  - Efeito: Linha vermelha mais forte (2px)
  - Hugo desliga celular. Sorriso satisfeito.
  - Se Vorcaro estiver no mapa: ele TAMBÉM ganha +30% defesa
  
Frame 4 (125ms): REDE ATIVA. Multiplas linhas se estendem.
  - Efeito: Linhas finas para varios pontos do mapa
  - Efeito: Hugo no CENTRO da teia (aranha)
  - Efeito: Halo pulsa
  - Hugo: maos nos bolsos, sorriso MAXIMO
  
Frame 5 (125ms): REDE DESVANECE. Linhas somem.
  - Efeito: Fade das linhas (uma a uma)
  - Efeito: Halo diminui
  - Hugo tira celular (planejando proxima conexao)
  - Buff de +30% defesa persiste por 10s APOS rede visual sumir
  - Cooldown: 15 segundos
```

#### Logica da Conexao:
```javascript
function conexaoMaster(hugo, vorcaro) {
    // +30% defesa para Hugo
    hugo.defenseMultiplier = 1.3;
    
    // Se Vorcaro estiver no mapa, ele tambem ganha
    if (vorcaro && vorcaro.active) {
        vorcaro.defenseMultiplier = 1.3;
        drawConnectionLine(hugo, vorcaro, '#FF3333', 10000);
    }
    
    // Buff dura 10 segundos
    this.time.delayedCall(10000, () => {
        hugo.defenseMultiplier = 1.0;
        if (vorcaro && vorcaro.active) {
            vorcaro.defenseMultiplier = 1.0;
        }
    });
}
```

---

### 6. SKILL 3 -- Imunidade Parlamentar
- **Frames:** 4
- **FPS:** 8
- **Loop:** Nao
- **Duracao Total:** 0.5s + escudo de 6s

#### Timeline Detalhada:
```
Frame 0 (125ms): INVOCACAO. Mao erguida (6 dedos estendidos).
  - Efeito: Escudo dourado comeca a formar acima da cabeca
  - Efeito: Brasao da Camara estilizado (grotesco)
  - Sorriso vira sorriso SERIO (raro)
  
Frame 1 (125ms): ESCUDO COMPLETO. Circulo dourado ao redor.
  - Efeito: Halo dourado 40% opacidade envolvendo Hugo
  - Efeito: Projeteis RICOCHETEIAM com texto "IMUNE" (5px)
  - Gameplay: Hugo invulneravel a certos tipos de dano
  - Hugo relaxado. Checa celular DENTRO do escudo.
  
Frame 2 (125ms): ESCUDO ATIVO. Pulsando.
  - Efeito: Escudo pulsa (scale 1.0 -> 1.05 -> 1.0, 500ms ciclo)
  - Efeito: "IMUNE" aparece a cada ricochet
  - Hugo pode andar normalmente (overlay segue sprite)
  
Frame 3 (125ms): DESVANECE. Escudo racha.
  - Efeito: Linhas de fratura no dourado
  - Efeito: Ultimo "IMUNE?" com interrogacao
  - Orelhas abaixam (micro-preocupacao)
  - Sorriso diminui 1px
  - Escudo some
  - Cooldown: 20 segundos
```

#### Logica da Imunidade:
```javascript
function imunidadeParlamentar(hugo) {
    const duration = 6000;
    const shield = createParliamentaryShield(hugo);
    
    // Lista de ataques que NAO afetam Hugo com imunidade
    hugo.immuneTo = ['projectile_normal', 'melee_basic', 'area_basic'];
    
    // Ataques que AINDA afetam (ninguem e totalmente imune)
    // 'projectile_special', 'boss_attack', 'ultimate'
    
    // Ricochet visual
    hugo.on('shielded_hit', (projectile) => {
        ricochetEffect(projectile);
        showText('IMUNE', projectile.x, projectile.y, '#FFD700', 500);
    });
    
    this.time.delayedCall(duration, () => {
        shield.crack();
        this.time.delayedCall(500, () => {
            shield.destroy();
            hugo.immuneTo = [];
            showText('IMUNE?', hugo.x, hugo.y - 30, '#FFD700', 800);
        });
    });
}
```

---

### 7. HIT (Tomar Dano)
- **Frames:** 3
- **FPS:** 12
- **Loop:** Nao
- **Duracao Total:** 0.25s

#### Timeline:
```
Frame 0 (83ms): IMPACTO CONTIDO.
  - Efeito: Flash branco SUTIL (30% opacidade -- MENOS que outros)
  - Efeito: Corpo move apenas 1-2px (minimo)
  - Efeito: Sorriso CONGELA (nao some, trava -- pior que sumir)
  - Efeito: Celular CAI da mao (voa 4px)
  - Efeito: Olhos PISCAM (UNICA vez fora de death -- o susto quebra o controle)
  - Efeito: Terno amassa levemente em 1 ponto
  - Som: SFX sutil -- nao grito, mas um "hm" contido + celular caindo
  
Frame 1 (83ms): RECOMPOSICAO INSTANTANEA.
  - Efeito: Mao pega celular no ar (6 dedos agarram como aranha)
  - Efeito: Sorriso VOLTA (forcado -- 1px mais largo que normal)
  - Efeito: Terno se alinha
  - Efeito: Olhos voltam a NAO PISCAR
  - Velocidade de recomposicao e ASSUSTADORA
  
Frame 2 (83ms): "NADA ACONTECEU".
  - Efeito: Idle perfeito restaurado
  - Efeito: Unica evidencia: micro-ruga no terno (1px sombra extra)
  - Efeito: Ruga desaparece em 2 segundos (auto-repair)
  - Invencibilidade: 0.5s
```

#### Contraste com outros personagens:
```
Maduro hit: DRAMATICO -- grita, chora, medalhas voam, pede Lula
Xandao hit: FURIOSO -- fica mais bravo, contra-ataca
Hugo hit:   CONTIDO -- quase nao reage. Isso e mais ASSUSTADOR.
```

---

### 8. DEATH
- **Frames:** 8
- **FPS:** 6 (MAIS LENTO que outros -- a morte e burocratica, nao explosiva)
- **Loop:** Nao (ultimo frame permanece)
- **Duracao Total:** 1.33s

#### Timeline:
```
Frame 0 (166ms): A FACHADA RACHA.
  - Efeito: Sorriso SOME pela primeira vez EVER
  - Efeito: Boca aberta em O genuino
  - Efeito: AMBOS olhos piscam descontrolados
  - Efeito: Celular voa
  - Efeito: Terno racha como PORCELANA (linhas de fratura)
  - Efeito: Screen shake minimo (1px) -- ate o screen shake dele e contido
  - Som: Silencio. Depois: som de porcelana rachando.
  
Frame 1 (166ms): DOCUMENTOS ESCAPAM.
  - Efeito: CENTENAS de micro-documentos voam do terno rachado
  - Efeito: Cada documento tem selo vermelho "SIGILOSO"
  - Efeito: Hugo tenta recolher -- 6 dedos de cada mao agarrando
  - Efeito: Documentos demais para segurar
  - Efeito: Emitter de particulas: papeis em todas as direcoes
  - Som: Papeis voando (rustle)
  
Frame 2 (166ms): CELULAR EXPOE.
  - Efeito: Celular no chao, tela para cima, MAXIMIZADA
  - Efeito: Lista de contatos visivel com nomes de todos os personagens
  - Efeito: Hugo olha com HORROR genuino (1a expressao de medo)
  - Efeito: Tenta pisar no celular -- pernas falham
  - Som: Notificacao do celular
  
Frame 3 (166ms): TERNO ESVAZIA.
  - Efeito: Terno fica FROUXO (scale do corpo diminui, terno mantem forma)
  - Efeito: Dentro: mais papeis, contratos, notas promissorias, cifraoes
  - Efeito: Hugo ENCOLHE -- sua substancia era PAPEL
  - Som: Papel amassando
  
Frame 4 (166ms): A REDE APARECE.
  - Efeito: TODAS as linhas de conexao que eram invisiveis se MATERIALIZAM
  - Efeito: Linhas vermelhas finas em TODAS as direcoes
  - Efeito: Hugo no centro, encolhido, cercado pela propria teia
  - Efeito: A rede e REVELADA -- tudo que ele escondia agora e visivel
  - Som: Zumbido eletronico (rede ativando)
  
Frame 5 (166ms): MAOS PUXAM.
  - Efeito: Linhas da rede PUXAM Hugo em direcoes opostas
  - Efeito: Corpo deforma (stretch em multiplas direcoes)
  - Efeito: Orelhas esticam (puxadas pela informacao)
  - Efeito: Dedos extras agarram o chao (resistencia)
  - Efeito: Expressao de desespero REAL -- sem sorriso, sem fachada
  - Som: Cordas tensionando
  
Frame 6 (166ms): DISSOLUCAO BUROCRATICA.
  - Efeito: Corpo se CONVERTE em documentos
  - Efeito: Pixel por pixel vira micro-documento voando
  - Efeito: Ele nunca foi pessoa -- sempre foi PILHA DE PAPEIS em forma humana
  - Efeito: Terno = pasta, sorriso = selo, maos = assinaturas
  - Som: Papel se desfazendo + vento
  
Frame 7 (166ms): RESTA O CELULAR. Frame final permanente.
  - Efeito: Hugo SUMIU. Nenhum corpo.
  - Efeito: Pilha de documentos no chao + celular no topo
  - Efeito: Tela ainda ligada: mensagem "VORCARO" nao lida
  - Efeito: Tela pisca
  - Efeito: Ultima notificacao: "Nova conexao disponivel"
  - Efeito: As conexoes PERSISTEM sem ele -- o sistema continua
  - Efeito: Fade lento (opacity 1.0 -> 0.3 em 3 segundos)
  - Som: Notificacao final do celular. Depois: silencio total.
```

#### Particulas da Death:
```javascript
// Documentos voando do terno
const documentExplosion = this.add.particles('document_particle');
documentExplosion.createEmitter({
    speed: { min: 20, max: 80 },     // mais LENTO que medalhas do Maduro
    angle: { min: 0, max: 360 },
    lifespan: 2000,                   // duram MAIS (burocratico)
    frequency: 50,                    // frequencia alta (muitos documentos)
    quantity: 3,
    gravityY: 40,                     // caem devagar (papel e leve)
    rotate: { min: -180, max: 180 },  // giram como papeis
    scale: { start: 0.8, end: 0.3 },
    alpha: { start: 1, end: 0.4 }
});

// Rede de conexoes se materializando
function revealNetwork(hugo, connectionPoints) {
    connectionPoints.forEach((point, index) => {
        this.time.delayedCall(index * 100, () => {  // uma por uma
            const line = this.add.graphics();
            line.lineStyle(1, 0xFF3333, 0);
            line.lineBetween(hugo.x, hugo.y, point.x, point.y);
            
            this.tweens.add({
                targets: line,
                alpha: { from: 0, to: 0.6 },
                duration: 300,
                ease: 'Stepped',
                easeParams: [3]
            });
        });
    });
}

// Dissolucao pixel-por-pixel em documentos
function bureaucraticDissolve(sprite, duration) {
    const totalPixels = 64 * 64;
    const pixelsPerFrame = Math.ceil(totalPixels / (duration / 16));
    
    // Cada "pixel" vira um documento voando
    let dissolved = 0;
    const timer = this.time.addEvent({
        delay: 16,
        repeat: duration / 16,
        callback: () => {
            for (let i = 0; i < pixelsPerFrame; i++) {
                const x = Phaser.Math.Between(0, 63) + sprite.x - 32;
                const y = Phaser.Math.Between(0, 63) + sprite.y - 32;
                spawnMicroDocument(x, y);
            }
            sprite.alpha -= (1 / (duration / 16));
        }
    });
}
```

---

## Transicoes Entre Estados

### State Machine:
```
IDLE -> WALK (input de movimento)
IDLE -> ATTACK (ativar Articulacao, cooldown respeitado)
IDLE -> SKILL_PAUTA (ativar Pauta Secreta, cooldown respeitado)
IDLE -> SKILL_CONEXAO (ativar Conexao Master, cooldown respeitado)
IDLE -> SKILL_IMUNIDADE (ativar Imunidade, cooldown respeitado)
WALK -> IDLE (parar movimento)
WALK -> ATTACK (cancela walk)
WALK -> SKILL_PAUTA (pode ativar andando -- Hugo nao precisa parar pra articular)
ANY -> HIT (dano recebido -- exceto se IMUNIDADE ativa para certos tipos)
ANY -> DEATH (HP = 0)
HIT -> IDLE (apos 0.25s + invencibilidade)
ATTACK -> IDLE (apos completar frames)
SKILL -> IDLE (apos completar frames)
DEATH -> REMOVE (apos fade de 3s)
```

### Prioridade de Interrupcao:
```
DEATH > HIT > SKILL_IMUNIDADE > ATTACK/SKILL > WALK > IDLE
```

### Regras de Transicao:
1. DEATH nunca e interrompida
2. HIT interrompe tudo exceto DEATH e IMUNIDADE ativa
3. IMUNIDADE pode ser ativada DURANTE qualquer estado (exceto DEATH)
4. Hugo pode usar PAUTA SECRETA ENQUANTO ANDA (unico personagem com essa capacidade)
5. Transicoes sao INSTANTANEAS -- sem blend (corte brusco)
6. O SORRISO tem state machine PROPRIA:
   - FIXO (99% do tempo): sorriso padrao inalterado
   - CONCENTRADO (attack/skill): sorriso 1px menor
   - CONGELADO (hit): musculos travam -- PIOR que desaparecer
   - AUSENTE (death): sorriso some -- o momento mais perturbador do jogo

---

## Efeitos Sonoros (SFX) por Animacao

| Animacao           | SFX Principal                      | SFX Secundario               |
|--------------------|------------------------------------|------------------------------|
| idle               | SILENCIO (sem respiracao audivel)  | Notificacao celular (sutil)  |
| walk               | Passos leves em marmore            | Celular vibrando             |
| walk_greet         | Passos + aperto de mao fantasma    | --                           |
| attack_articulacao | Distorcao de ar (shimmer sonoro)   | Flash dourado nos inimigos   |
| skill_pauta        | Papel desdobrando + selo quebrando | Engrenagem girando (micro)   |
| skill_conexao      | Celular vibrando + ligacao         | Cifraoes digitais            |
| skill_imunidade    | Sino dourado (reverb)              | "IMUNE" em voz processada    |
| hit                | "Hm" contido + celular caindo      | Terno amassando              |
| death              | Porcelana rachando + papeis voando | Celular notificando + silencio|

### Nota sobre som do Hugo:
Hugo e o personagem MAIS SILENCIOSO do jogo. A maioria dos seus SFX sao sutis, abafados, discretos. O contraste com o Maduro (que grita no megafone) e intencional. O poder dele nao faz barulho.

---

## Bordoes com Timing de Animacao

| Bordao                                              | Trigger                | Duracao |
|-----------------------------------------------------|------------------------|---------|
| "Vamos conversar nos bastidores."                   | Ao ativar ATTACK       | 2.0s    |
| "Eu nao decido nada. Eu so... articulo."            | IDLE (random, 10%)     | 2.5s    |
| "O Vorcaro? Conheco de vista. ...de muitas vistas." | Celular flash VORCARO  | 3.0s    |
| "A Camara funciona no dialogo. E no sigilo."        | Ao ativar SKILL_PAUTA  | 2.5s    |
| "Quem controla a pauta, controla o pais."           | Ao ativar SKILL_PAUTA  | 2.5s    |
| "Nada pessoal. So articulacao."                     | Apos ATTACK sucesso    | 2.0s    |
| "Imunidade e um direito. Meu direito."              | Ao ativar IMUNIDADE    | 2.0s    |
| "...isso nao devia estar gravado."                  | Ao tomar HIT           | 2.0s    |

### Implementacao dos Bordoes:
```javascript
// Bordoes do Hugo -- estilo diferente dos outros personagens
// Texto em ITALICO e DISCRETO (fonte menor, cor cinza)
function showHugoCatchphrase(sprite, text, duration) {
    const bubble = this.add.text(sprite.x, sprite.y - 35, text, {
        fontSize: '7px',               // MENOR que outros personagens
        fontFamily: 'monospace',
        fontStyle: 'italic',            // italico -- sussurro
        backgroundColor: '#F0F0F0',     // cinza claro (nao branco)
        color: '#3A3A3A',               // cinza escuro (nao preto)
        padding: { x: 3, y: 1 },
        wordWrap: { width: 90 }
    });
    bubble.setOrigin(0.5, 1);
    bubble.setAlpha(0.85);              // levemente transparente
    
    this.tweens.add({
        targets: bubble,
        alpha: { from: 0.85, to: 0 },
        y: sprite.y - 45,
        duration: duration,
        ease: 'Stepped',
        easeParams: [4],
        onComplete: () => bubble.destroy()
    });
}
```

---

## Interacao com Outros Personagens

### Hugo + Vorcaro (Conexao Master)
```
Quando ambos estao no mapa:
  - Linha vermelha PERMANENTE (muito fina, 0.5px, 10% opacidade) entre eles
  - +10% defesa passiva para ambos (sem ativar skill)
  - Skill "Conexao Master" fica 30% mais forte (+40% defesa em vez de +30%)
  - Se um morre, o outro perde 20% defesa por 5 segundos (rede caindo)
```

### Hugo + Lula (Articulacao Politica)
```
Quando ambos estao no mapa:
  - Hugo pode usar Lula como "escudo" involuntario (similar ao Passa Pano do Maduro)
  - Articulacao Suprema afeta 2 NPCs a mais quando perto de Lula
  - Lula nao sabe que esta sendo usado (nenhum feedback visual no sprite do Lula)
```

### Hugo + Maduro (O Passa Pano do Passa Pano)
```
Se Maduro usa "Passa Pano" e Hugo esta perto:
  - Hugo pode "articular" o Passa Pano do Maduro via Lula
  - Cadeia: Maduro -> Lula -> Hugo (cada um se esconde atras do proximo)
  - Easter egg visual: os tres empilhados, so os olhos aparecendo
```
