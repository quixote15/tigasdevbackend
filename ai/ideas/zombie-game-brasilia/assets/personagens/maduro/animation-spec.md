# MADURO (O Ditador Palhaco) - Animation Specification

## Principios de Animacao

### Estilo Geral
- **Frame Rate:** 8-10fps (JERKY, twitchy -- NUNCA suave)
- **Tecnica:** Deformacao organica, squash-stretch exagerado
- **Easing:** NENHUM easing suave. Transicoes BRUSCAS entre poses
- **Principio Core:** Tudo no Maduro e FALSO e prestes a cair. Cada animacao deve reforcar a precariedade do personagem.

### Hierarquia de Movimento
1. **BIGODE** -- Sempre em movimento independente. Reage ANTES do corpo. E uma entidade separada.
2. **BARRIGA** -- Segue o corpo com delay de 1-2 frames (inercia de gelatina). Nunca para de balançar.
3. **MEDALHAS** -- Tilintam e balancam com qualquer movimento. Soltas. Uma sempre quase caindo.
4. **BOINA** -- Sempre torta, sempre escorregando. Em movimentos bruscos, voa.
5. **CORPO** -- O ultimo a reagir. Lento, pesado, desajeitado.

---

## Animacoes Detalhadas

### 1. IDLE
- **Frames:** 4
- **FPS:** 8
- **Loop:** Sim
- **Duracao Total:** 0.5s por ciclo

#### Sequencia de Frames:
```
Frame 0 (125ms): Pose base. Bigode centralizado. Medalhas paradas.
Frame 1 (125ms): Bigode move 2px ESQUERDA. Gota de suor aparece. Olhos estreitam.
Frame 2 (125ms): Bigode volta ao centro. Uma medalha pende 2px. Olhar de panico lateral.
Frame 3 (125ms): Bigode move 2px DIREITA. Medalha volta. Suor do outro lado.
```

#### Principio de Animacao:
- O idle comunica ANSIEDADE CONSTANTE. Maduro nunca esta relaxado.
- O bigode tem ciclo proprio: esquerda-centro-centro-direita-centro-centro (2x mais lento que o body)
- Medalhas tem micro-oscilacao (1px) continua
- Suor aparece e desaparece em frames alternados
- Micro-tremor no corpo todo (0.5px jitter em posicao -- implementar via codigo, nao sprite)

#### Codigo Phaser 3:
```javascript
// Idle animation
this.anims.create({
    key: 'maduro_idle',
    frames: this.anims.generateFrameNumbers('maduro_idle', { start: 0, end: 3 }),
    frameRate: 8,
    repeat: -1
});

// Jitter effect overlay (aplicar via tween)
this.tweens.add({
    targets: maduroSprite,
    x: { value: '+=0.5', duration: 100, yoyo: true, repeat: -1, ease: 'Stepped', easeParams: [2] },
    y: { value: '+=0.3', duration: 150, yoyo: true, repeat: -1, ease: 'Stepped', easeParams: [2] }
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
Frame 0 (100ms): Passo direito. Perna levanta DEMAIS. Barriga pende esquerda.
Frame 1 (100ms): Transicao. Bounce UP (+2px). Medalhas em inercia.
Frame 2 (100ms): Passo esquerdo. Mirror do 0. Barriga pende direita.
Frame 3 (100ms): Transicao. Bounce DOWN (-1px). Suor se forma.
Frame 4 (100ms): TROPECO (a cada 2 ciclos). Corpo inclina 5-8 graus. Bigode ereto.
Frame 5 (100ms): Recuperacao. Finge que nada aconteceu. Postura exagerada.
```

#### Logica de Variacao:
```
Ciclo 1: Frame 0 -> 1 -> 2 -> 3 -> 0 -> 1... (sem tropeco)
Ciclo 2: Frame 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0... (com tropeco)
```

#### Efeitos de Particula no Walk:
- **Poeira nos pes:** 2-3 pixels marrom-claro a cada passo (spawn no frame de contato)
- **Medalhas tilintando:** Micro-flash branco (1px) nas medalhas a cada bounce
- **Suor voando:** Gota sai no frame 3, voa 4px para tras, desaparece em 3 frames

#### Principio de Animacao:
- A marcha e PATETICA. Imitacao ruim de parada militar.
- Pernas levantam demais (overcompensacao -- quer parecer disciplinado, parece ridiculo)
- Barriga tem inercia de gelatina (delay de 1 frame, overshoot de 1px)
- Tropeco QUEBRA o ritmo -- essencial para a comedia
- Recuperacao do tropeco e INSTANTANEA (corte brusco para pose ereta -- denial)

#### Codigo Phaser 3:
```javascript
// Walk with stumble variation
let walkCycleCount = 0;

this.anims.create({
    key: 'maduro_walk_normal',
    frames: this.anims.generateFrameNumbers('maduro_walk', { frames: [0, 1, 2, 3] }),
    frameRate: 10,
    repeat: 0
});

this.anims.create({
    key: 'maduro_walk_stumble',
    frames: this.anims.generateFrameNumbers('maduro_walk', { frames: [0, 1, 2, 3, 4, 5] }),
    frameRate: 10,
    repeat: 0
});

maduroSprite.on('animationcomplete', (anim) => {
    if (anim.key.startsWith('maduro_walk')) {
        walkCycleCount++;
        const key = (walkCycleCount % 2 === 0) ? 'maduro_walk_stumble' : 'maduro_walk_normal';
        maduroSprite.play(key);
    }
});
```

---

### 3. ATTACK -- Ditadura Express
- **Frames:** 8
- **FPS:** 10
- **Loop:** Nao
- **Duracao Total:** 0.8s

#### Timeline Detalhada:
```
Frame 0 (100ms): WIND-UP. Puxa megafone de tras. Corpo inclina para tras.
  - Efeito: Nenhum ainda. Anticipacao pura.
  
Frame 1 (100ms): PREPARACAO. Megafone na boca. Inhala. Corpo expande 2px.
  - Efeito: Screen shake leve (1px, 50ms)
  
Frame 2 (100ms): GRITO INICIAL. Boca abre, bigode parte ao meio. Ondas sonoras.
  - Efeito: Spawn projetil 'onda_sonora' na direcao do megafone
  - Efeito: 2-3 particulas de 'nota_bolivar' voam com as ondas
  - Som: SFX megafone distorcido + grito comico
  
Frame 3 (100ms): GRITO MAXIMO. Ondas preenchem 50% do frame.
  - Efeito: Ondas sonoras se expandem (hitbox ativo)
  - Efeito: Chuva de notas de bolivar (8-12 particulas)
  - Efeito: Screen shake medio (2px, 100ms)
  - Dano: Aplicar dano AoE na zona
  
Frame 4 (100ms): ZONA FORMA. Circulo vermelho/dourado no chao.
  - Efeito: Spawn zona 'ditadura_express' no chao
  - Efeito: Gas verde doentio nas bordas (particulas subindo)
  - Gameplay: Zona ativa -- regras da area mudam
  
Frame 5 (100ms): ZONA ATIVA. Caos visual dentro da zona.
  - Efeito: Particulas caoticas dentro da zona (setas, ??, notas)
  - Efeito: Maduro faz pose de propaganda (mao erguida)
  
Frame 6 (100ms): ZONA ENFRAQUECE. Efeitos diminuem.
  - Efeito: Zona fica 50% transparente
  - Efeito: Notas caem no chao (gravidade)
  - Efeito: Gas se dissipa
  
Frame 7 (100ms): FIM. Maduro ofegante, derrotado.
  - Efeito: Zona desaparece
  - Gameplay: Regras voltam ao normal
  - Cooldown inicia: 8 segundos
```

#### Hitbox da Zona:
```
Tipo: Circular
Raio: 48px do centro de Maduro
Duracao: Frames 4-6 (300ms ativo)
Efeito: Inimigos na zona tem movimentacao INVERTIDA por 3s
```

---

### 4. SKILL 1 -- Passa Pano
- **Frames:** 6
- **FPS:** 8
- **Loop:** Nao
- **Duracao Total:** 0.75s
- **Condicao:** Lula deve estar no mapa (raio de 200px)

#### Timeline Detalhada:
```
Frame 0 (125ms): PROCURA. Olha ao redor. Pupilas giram.
  - Efeito: Icone de "?" sobre a cabeca
  - AI: Detecta posicao do Lula no mapa
  
Frame 1 (125ms): CORRE. Corrida comica em direcao a Lula.
  - Efeito: Speed lines atras
  - Efeito: Boina voa, lagrimas comicas (3 particulas)
  - Efeito: Bigode como bandeira ao vento
  - Movimento: Maduro se reposiciona ATRAS de Lula
  
Frame 2 (125ms): ESCONDE. Apenas bigode e olhos visiveis atras de Lula.
  - Efeito: Corpo parcialmente ocultado pelo sprite do Lula
  - Efeito: Maos agarrando ombros de Lula (overlay no sprite do Lula)
  
Frame 3 (125ms): ESCUDO ATIVA. Campo de energia vermelho.
  - Efeito: Spawn escudo vermelho com estrela PT entre os dois
  - Efeito: Texto "COMPANHEIRO" micro no escudo
  - Gameplay: +50% defesa para Maduro enquanto perto de Lula
  
Frame 4 (125ms): ESCUDO MAXIMO. Projeteis ricocheteiam.
  - Efeito: Particulas de ricochet nos projeteis que acertam o escudo
  - Efeito: Maduro da joinha por tras
  
Frame 5 (125ms): ESCUDO DESVANECE. Lula se afasta.
  - Efeito: Escudo fica transparente e some
  - Efeito: Lula sprite se move para longe (cansou)
  - Efeito: Maduro fica sozinho, expressao de abandono
  - Gameplay: Defesa volta ao normal
  - Cooldown: 12 segundos
```

#### Condicoes Especiais:
```
Se Lula NAO esta no mapa:
  - Maduro faz o Frame 0 (procura) por 4x mais tempo
  - Depois Frame de PANICO: grita "LULA!" com balao
  - Skill FALHA. Cooldown de 15s.
  - Bigode cai parcialmente (tristeza)
```

---

### 5. SKILL 2 -- Plano Economico Absurdo
- **Frames:** 6
- **FPS:** 8
- **Loop:** Nao
- **Duracao Total:** 0.75s + 5s de efeito

#### Timeline Detalhada:
```
Frame 0 (125ms): IDEIA. Lampada-de-nota-de-dinheiro acende.
  - Efeito: Particula de "lampada" acende (nota de bolivar brilhando)
  - Efeito: Dedo erguido, olhos de lunático
  
Frame 1 (125ms): QUADRO. Puxa quadro branco do nada.
  - Efeito: Quadro aparece (32x32px overlay) com graficos absurdos
  - Efeito: Numeros no quadro sao IMPOSSIVEIS ("PIB = infinito")
  
Frame 2 (125ms): EXPLICA. Aponta com bastao-salame pro quadro.
  - Efeito: Graficos no quadro MUDAM em tempo real (tween nos numeros)
  - Efeito: Notas de bolivar comecam a cair como neve (particulas leves)
  
Frame 3 (125ms): IMPLEMENTA. Zona de caos economico forma.
  - Efeito: Spawn zona AoE circular (raio 64px)
  - Gameplay: REGRAS MUDAM na zona por 5 segundos:
    - Direcoes de input INVERTIDAS (50% chance)
    - Velocidade de inimigos RANDOMIZADA (0.5x a 2x)
    - Drops mudam de valor (positivo vira negativo e vice-versa)
  
Frame 4 (125ms): CAOS. Maduro danca no meio da destruicao.
  - Efeito: Particulas MAXIMAS (notas, setas, icones quebrados)
  - Efeito: Bigode gira como helice (rotacao no eixo central)
  - Efeito: Medalhas orbitam (rotacao circular ao redor do sprite)
  
Frame 5 (125ms): RESULTADO. Zona se desfaz. Destruicao visivel.
  - Efeito: Zona fade out
  - Efeito: Quadro pega fogo (particulas de fogo, 3 frames)
  - Efeito: Notas caem mortas no chao
  - Gameplay: Regras voltam ao normal
  - Cooldown: 15 segundos
```

#### Logica do Caos Economico (5 segundos):
```javascript
// Efeitos aleatorios que mudam a cada segundo dentro da zona
const CAOS_EFFECTS = [
    'invert_controls',      // Controles invertidos
    'speed_randomize',      // Velocidades aleatorias  
    'drop_value_invert',    // Valores de drop invertidos
    'gravity_flip',         // Gravidade invertida (1s)
    'size_randomize'        // Tamanho dos sprites oscila
];

// A cada segundo, sorteia 1-2 efeitos diferentes
function applyCaosEconomico(zone, deltaTime) {
    if (deltaTime % 1000 < 16) { // a cada segundo
        const effect = Phaser.Utils.Array.GetRandom(CAOS_EFFECTS);
        zone.applyEffect(effect, 1000); // dura 1s
    }
}
```

---

### 6. HIT (Tomar Dano)
- **Frames:** 3
- **FPS:** 12
- **Loop:** Nao
- **Duracao Total:** 0.25s

#### Timeline:
```
Frame 0 (83ms): IMPACTO.
  - Efeito: Flash branco (overlay 50% opacidade)
  - Efeito: Squash horizontal (corpo comprimido)
  - Efeito: Spawn particulas de medalhas voando (3-4)
  - Efeito: Bigode se solta parcialmente
  - Efeito: Boina voa (particula separada)
  - Efeito: Screen shake (1px, 50ms)
  - Som: SFX "bonk" metalico + grito agudo
  
Frame 1 (83ms): REACAO.
  - Efeito: Stretch vertical (bounce de volta)
  - Efeito: Lagrimas comicas (4-5 gotas)
  - Efeito: Balao de fala "LULA!" (micro, 1 segundo)
  - Efeito: Bracos para cima em panico
  
Frame 2 (83ms): RECUPERACAO.
  - Efeito: Recolhe medalhas (desaparecem do chao)
  - Efeito: Gruda bigode (fita visivel por 2 segundos apos)
  - Efeito: Postura exagerada (overcompensacao)
  - Invencibilidade: 0.5s apos dano
```

---

### 7. DEATH
- **Frames:** 8
- **FPS:** 8
- **Loop:** Nao (ultimo frame permanece)
- **Duracao Total:** 1.0s

#### Timeline:
```
Frame 0 (125ms): GOLPE FATAL. Arqueamento dramatico para tras.
  - Efeito: Bigode se SEPARA completamente (sprite independente voa)
  - Efeito: Boina voa para fora da tela
  - Efeito: Medalhas EXPLODEM (8-10 particulas radiais)
  - Efeito: Screen shake forte (3px, 200ms)
  - Som: SFX impacto massivo + grito comico longo
  
Frame 1 (125ms): QUEDA. Maduro caindo.
  - Efeito: Mao estendida tentando pegar o bigode
  - Efeito: Faixa presidencial se desenrola (sprite separado)
  - Efeito: Maquiagem de palhaco mais VISIVEL (cores mais saturadas)
  
Frame 2 (125ms): NO CHAO. Barriga para cima.
  - Efeito: Impacto no chao (poeira, 4px radial)
  - Efeito: Uniforme rasgado revelando camiseta "I LOVE SOCIALISMO"
  - Efeito: Medalhas pousam ao redor (bounce leve)
  
Frame 3 (125ms): BIGODE RETORNA. Voa de volta ERRADO.
  - Efeito: Bigode sprite voa de volta ao rosto
  - Efeito: Pousa ERRADO (de lado ou invertido)
  - Efeito: Tentativa de se ajeitar (rotacao lenta)
  - Comedia: O bigode tem mais personalidade que o dono
  
Frame 4 (125ms): ULTIMA TENTATIVA. Tenta levantar.
  - Efeito: Megafone aparece, Maduro se apoia nele
  - Efeito: Megafone QUEBRA (sprites de estilhacos)
  - Efeito: Barriga impede rotacao
  
Frame 5 (125ms): DISCURSO FINAL. Megafone quebrado.
  - Efeito: Tenta gritar -- sai "pfrrrt" (balao de fala comico)
  - Efeito: Confete de bolivares desvalorizados cai ao redor
  - Som: SFX trompete triste / trombone wah-wah
  
Frame 6 (125ms): DESINFLANDO.
  - Efeito: Corpo diminui gradualmente (scale tween 1.0 -> 0.7)
  - Efeito: Uniforme fica frouxo (pixels se expandem ao redor)
  - Efeito: Linhas onduladas de ar saindo (3-4 particulas onduladas)
  - Efeito: Som de balao desinflando
  
Frame 7 (125ms): PALHACO REVELADO. Frame final permanente.
  - Efeito: Fade lento (opacity 1.0 -> 0.3 em 2 segundos)
  - Efeito: Nota "SEM VALOR" pousa suavemente
  - Efeito: Bigode finalmente inerte ao lado
  - Efeito: Ultimo flash -- nariz de palhaco vermelho brilha 1x
  - Permanece visivel por 2 segundos depois faz fade total
```

#### Particulas da Death:
```javascript
// Medalhas explodindo
const medalExplosion = this.add.particles('medal_particle');
medalExplosion.createEmitter({
    speed: { min: 50, max: 150 },
    angle: { min: 0, max: 360 },
    lifespan: 800,
    quantity: 8,
    gravityY: 200,
    bounce: 0.3,
    scale: { start: 1, end: 0.5 }
});

// Confete de bolivares
const bolivarConfetti = this.add.particles('bolivar_particle');
bolivarConfetti.createEmitter({
    speed: { min: 10, max: 40 },
    angle: { min: 250, max: 290 },
    lifespan: 2000,
    frequency: 100,
    quantity: 2,
    gravityY: 30,
    rotate: { min: 0, max: 360 },
    scale: { start: 0.8, end: 0.3 },
    alpha: { start: 1, end: 0.2 }
});
```

---

## Transicoes Entre Estados

### State Machine:
```
IDLE -> WALK (ao receber input de movimento)
IDLE -> ATTACK (ao ativar skill de ataque, cooldown respeitado)
IDLE -> SKILL_PASSAPANO (ao ativar, Lula detectado no mapa)
IDLE -> SKILL_PLANO (ao ativar, cooldown respeitado)
WALK -> IDLE (ao parar movimento)
WALK -> ATTACK (pode atacar andando -- cancela walk)
ANY -> HIT (ao receber dano -- interrompe QUALQUER animacao, exceto DEATH)
ANY -> DEATH (ao HP chegar a 0)
HIT -> IDLE (apos 0.25s + invencibilidade)
ATTACK -> IDLE (apos completar todos os frames)
SKILL -> IDLE (apos completar todos os frames)
DEATH -> REMOVE (apos fade de 2s)
```

### Prioridade de Interrupcao:
```
DEATH > HIT > ATTACK/SKILL > WALK > IDLE
```

### Regras de Transicao:
1. DEATH nunca e interrompida
2. HIT interrompe tudo exceto DEATH
3. ATTACK/SKILL nao podem ser interrompidos por WALK
4. WALK pode ser interrompido por qualquer coisa
5. Entre IDLE e WALK, transicao e INSTANTANEA (sem blend)
6. O BIGODE tem sua propria state machine que roda em PARALELO:
   - Calmo (idle): oscilacao leve
   - Mentindo (ataque/skill): tremor rapido
   - Chocado (hit): ereto/solto
   - Morto (death): inerte

---

## Efeitos Sonoros (SFX) por Animacao

| Animacao        | SFX Principal                    | SFX Secundario             |
|-----------------|----------------------------------|----------------------------|
| idle            | Respiracao pesada (loop leve)    | Metal tilintando (medalhas)|
| walk            | Passos pesados + barriga         | Medalhas chacoalhando      |
| walk_stumble    | Tropeco + "opa!" comico          | Boina hit sound            |
| attack          | Megafone distorcido + grito      | Notas de papel voando      |
| skill_passapano | Corrida + choro comico           | Escudo energizando         |
| skill_plano     | "EUREKA!" + quadro aparecendo    | Caos economico (glitch)    |
| hit             | "Bonk" metalico + grito agudo    | Medalhas caindo            |
| death           | Impacto massivo + grito longo    | Trombone triste + deflate  |

---

## Bordoes com Timing de Animacao

| Bordao                                          | Trigger              | Duracao |
|-------------------------------------------------|----------------------|---------|
| "O imperialismo americano nao nos detera!"      | Ao ativar ATTACK     | 2.0s    |
| "A revolucao bolivariana e eterna! ...certo?"   | IDLE (random, 15%)   | 2.5s    |
| "Lula, me defende! LULA!"                       | Ao tomar HIT         | 1.5s    |
| "Nosso plano economico e simples: imprimir mais dinheiro!" | Ao ativar SKILL_PLANO | 3.0s |
| "Isso costumava funcionar..."                   | Fim do ATTACK (fail) | 1.5s    |
| "Eu QUIS tropecar! Era parte do plano!"         | Apos WALK_STUMBLE    | 2.0s    |

### Implementacao dos Bordoes:
```javascript
// Balao de fala temporario
function showCatchphrase(sprite, text, duration) {
    const bubble = this.add.text(sprite.x, sprite.y - 40, text, {
        fontSize: '8px',
        fontFamily: 'monospace',
        backgroundColor: '#FFFFFF',
        color: '#1A1A1A',
        padding: { x: 4, y: 2 },
        wordWrap: { width: 80 }
    });
    bubble.setOrigin(0.5, 1);
    
    this.tweens.add({
        targets: bubble,
        alpha: { from: 1, to: 0 },
        y: sprite.y - 55,
        duration: duration,
        ease: 'Stepped',
        easeParams: [4],
        onComplete: () => bubble.destroy()
    });
}
```
