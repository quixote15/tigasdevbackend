# Toga de Teflon -- Especificacao de Sprites

**Weapon ID:** 12
**Boss:** Gilmar Mendes
**Tipo:** Defensivo / Reflexivo (Escudo + Reflect)
**Categoria:** Arma Exclusiva de Boss do STF
**Nivel de Perigo:** ALTO -- mecanica frustrante por design (nada gruda nesse cara)

---

## Descricao Geral

A Toga de Teflon e a arma/armadura exclusiva do boss Gilmar Mendes. Nao e uma arma convencional -- e uma toga de ministro do STF que funciona como escudo reflexivo: projeteis que acertam Gilmar tem 33% de chance de VOLTAR no atirador (refletidos). A toga e esvoacante, dramatica, e grotescamente luxuosa. Tem manchas amareladas de pastel (Gilmar ama um pastel, referencia a suas aparicoes publicas em feiras), um bolso secreto de onde caem notas de dinheiro constantemente, e uma superficie com brilho de teflon que sugere que NADA gruda nele -- acusacoes, processos, balas, nada.

A toga deve emanar uma aura de impunidade cosmica. E simultaneamente ridicula (manchas de pastel, dinheiro caindo) e ameacadora (projeteis voltando, brilho sobrenatural). Um artefato de corrupcao protegido pela mais alta corte.

---

## 1. Sprite da Toga (Base / Vestida no Boss)

**Dimensoes:** 64x64 px (arma de boss -- desproporcional, toga esvoacante ultrapassa o corpo)
**Anchor point:** Center (32, 32) -- centrada no boss
**Sprite sheet:** 256x64 px (4 frames: static + 3 idle/esvoacar)

### Paleta de Cores

| Elemento                   | Hex       | Uso                                           |
|----------------------------|-----------|-----------------------------------------------|
| Toga Preto Base            | `#1C1C1C` | Tecido principal da toga                       |
| Toga Preto Profundo        | `#0A0A0A` | Dobras profundas, sombras internas             |
| Toga Cinza Highlight       | `#3A3A3A` | Highlights do tecido, areas iluminadas         |
| Toga Brilho Teflon         | `#6A6A6A` | Reflexo de teflon na superficie (brilho oily)  |
| Toga Brilho Maximo         | `#A0A0A0` | Pico do shimmer de teflon                      |
| Forro Vermelho             | `#8B0000` | Forro interno da toga (visivel nas dobras)      |
| Forro Vermelho Claro       | `#B22222` | Highlight do forro                             |
| Mancha Pastel Amarelo      | `#D4A017` | Manchas de gordura de pastel                   |
| Mancha Pastel Escuro       | `#A07D14` | Sombra das manchas (gordura acumulada)         |
| Migalha Pastel             | `#E8C840` | Migalhas de pastel voando                      |
| Dinheiro Verde             | `#2E7D32` | Notas de dinheiro base                         |
| Dinheiro Verde Claro       | `#4CAF50` | Highlight das notas                            |
| Dinheiro Amarelo           | `#FFD700` | Cifras / detalhe dourado nas notas             |
| Outline Preto              | `#0D0D0D` | Contornos grossos estilo Crumb (3px)           |
| Reflexo Shield             | `#C0C0C0` | Flash de reflexao quando projetil volta        |
| Reflexo Shield Brilho      | `#FFFFFF` | Pico branco do flash de reflexao               |
| Aura Impunidade            | `#4A4A4A30` | Aura semi-transparente sinistra               |
| Poeira Dourada             | `#DAA52060` | Particulas de ostentacao flutuando            |

### Descricao por Frame

#### Frame 0 -- Static / Icone de Inventario
- A toga vista de cima (top-down isometrica) envolvendo o corpo do boss (corpo implicito, toga e o foco)
- Tecido negro DRAMATICO -- dobras profundas e volumosas, a toga e MAIOR que o personagem
- A toga flui para os lados e para tras, criando uma silhueta imponente e larga (~56px de largura visual)
- Dobras profundas no tecido: pelo menos 5-6 vincos visiveis com gradiente #0A0A0A nos vales e #3A3A3A nos picos
- Forro vermelho escuro visivel nas bordas onde o tecido vira (2-3px de vermelho nos cantos dobrados)
- **MANCHAS DE PASTEL:** 3-4 manchas amareladas (#D4A017) em posicoes aleatorias no tecido frontal
  - Cada mancha e irregular (3-5px de largura), com borda mais escura (#A07D14)
  - Uma mancha maior no peito (mais antiga, mais escura)
  - Manchas menores nos ombros e lateral
  - As manchas tem textura de gordura -- levemente brilhantes comparadas ao tecido fosco ao redor
- **BOLSO COM DINHEIRO:** Um bolso no lado direito do peito, de onde sobressaem 2-3 notas de dinheiro
  - Notas parcialmente visiveis (8-10px de comprimento saindo do bolso)
  - Verdes (#2E7D32) com detalhes dourados (#FFD700) simulando cifras
  - Uma nota esta quase caindo (inclinada, prestes a sair)
- **BRILHO DE TEFLON:** Em 3-4 pontos do tecido, reflexos longos e finos (#6A6A6A ao #A0A0A0)
  - Parecem reflexos oleosos, como se o tecido tivesse uma camada protetora sobrenatural
  - Os reflexos sao DIFERENTES de highlights de tecido normal -- sao mais "quimicos", mais artificiais
- Contornos GROSSOS e IRREGULARES (3px minimo) estilo Robert Crumb
- Sombra pesada projetada pela toga (offset 4px, forma irregular, 50% opacidade)
- Aura sutil e sinistra ao redor da toga (#4A4A4A, 15% opacidade, 2px ao redor)

#### Frame 1 -- Idle Esvoacar A
- A toga se move levemente para a ESQUERDA como se houvesse brisa ou energia sobrenatural
- A borda direita da toga levanta-se (3-4px acima da posicao estatica), revelando MAIS forro vermelho
- Dobras do tecido se redistribuem (os vincos mudam de posicao levemente)
- O brilho de teflon DESLIZA pela superficie (reflexos movem 2px para a esquerda)
- Uma migalha de pastel (#E8C840, 2x2px) se desprende da mancha maior e flutua para a direita
- Uma nota de dinheiro do bolso comeca a CAIR (deslocada 2px para baixo comparada ao Frame 0)
- 1-2 particulas de poeira dourada (#DAA520, 1px, 40% opacidade) flutuam perto da toga

#### Frame 2 -- Idle Esvoacar B
- A toga se move para a DIREITA (espelho do Frame 1)
- A borda esquerda levanta, forro vermelho visivel do outro lado
- Dobras redistribuidas novamente
- Brilho de teflon desliza 2px para a direita
- A migalha do Frame 1 esta mais longe (4px da toga) e comecando a desaparecer
- A nota de dinheiro caiu MAIS (4px abaixo do bolso), quase solta
- Nova migalha comecando a se desprender de outra mancha
- Particulas douradas em posicoes diferentes

#### Frame 3 -- Idle Esvoacar C (Reset)
- Toga retorna a posicao QUASE identica ao Frame 0 (leve variacao para evitar loop robotico)
- A migalha do Frame 1 desapareceu
- A nota que estava caindo CAIU FORA DO BOLSO e esta agora como particula independente abaixo (6px abaixo)
- Uma NOVA nota aparece no bolso (reposicao ciclica -- o bolso nunca acaba)
- Brilho de teflon em posicao ligeiramente diferente do Frame 0
- Particula dourada solitaria desaparecendo
- Loop: Frame 1 -> 2 -> 3 -> 1 cria movimento organico constante

---

## 2. Efeito de Reflexao (Projetil Rebatido)

**Dimensoes:** 48x48 px por frame (area de efeito ao redor do ponto de impacto na toga)
**Frames:** 4
**Sprite sheet:** 192x48 px
**Trigger:** Quando projetil acerta Gilmar e o RNG decide refletir (33% de chance)

#### Frame 0 -- Projetil Chega (Pre-Reflexao)
- O projetil (representado genericamente como circulo de 4px, cor do projetil original) esta a ~6px da superficie da toga
- A toga comeca a BRILHAR no ponto de impacto iminente:
  - Circulo de brilho de teflon se forma (raio 4px, #A0A0A0, 40% opacidade)
  - O reflexo oleoso no ponto de impacto se INTENSIFICA (de #6A6A6A para #A0A0A0)
- Linhas de velocidade atras do projetil (2 linhas de 1px) indicando direcao de chegada
- O tecido da toga comeca a ficar rigido naquela area (dobras alisando-se, como se o teflon endurecesse)

#### Frame 1 -- Contato e Deflexao
- O projetil TOCA a toga e o momento de reflexao acontece
- **FLASH MASSIVO de teflon:** circulo branco (#FFFFFF) no ponto de contato (raio 8px, 80% opacidade)
- A superficie da toga no ponto de contato fica PRATEADA (#C0C0C0) temporariamente
- O projetil comeca a MUDAR DE DIRECAO -- agora apontando na direcao OPOSTA
- Ondas de reflexao concentricas saindo do ponto de contato (2 aneis, prata/cinza claro, 2px e 4px de raio)
- Texto "NADA GRUDA!" aparecendo acima em letras vermelhas minusculas (estilo comico, 1px de altura, pode ser sugerido)
- Particulas de brilho (4-5 pontos de 1px brancos/prateados) irradiando do ponto de contato
- A toga ONDULA violentamente ao redor do ponto de impacto (2-3 dobras agudas radiais)

#### Frame 2 -- Projetil Retornando
- O projetil agora viaja na DIRECAO OPOSTA, se afastando da toga
- O projetil tem um glow prateado adicional (#C0C0C0, 2px ao redor) -- marcado pelo teflon
- Linhas de velocidade agora do lado da toga (projetil indo embora)
- O flash de contato encolheu (raio 4px, 40% opacidade) e esta desvanecendo
- As ondas concentricas expandiram (raio 8px e 12px, ficando transparentes)
- A toga ainda ondula mas esta se acalmando
- Uma nota de dinheiro foi sacudida pelo impacto e esta voando para o lado (detalhe comico)
- "NADA GRUDA!" no brilho maximo, tamanho ligeiramente maior

#### Frame 3 -- Dissipacao
- O projetil saiu do frame (ou esta na borda, pequeno)
- O flash desapareceu completamente
- As ondas concentricas dissiparam
- A toga esta quase normal, com residuo de brilho prateado desvanecendo no ponto de impacto
- "NADA GRUDA!" desbotando rapidamente (30% opacidade)
- A superficie da toga retorna a cor normal (#1C1C1C -> #3A3A3A)
- Ultima particula de brilho cai
- A nota de dinheiro sacudida esta ao chao (detalhe persistente por 1-2 segundos)

---

## 3. Particulas de Migalha de Pastel

**Dimensoes:** 16x16 px cada (sprites individuais de particula)
**Quantidade:** 4 variantes
**Uso:** Emitter de particulas no Phaser -- quando Gilmar se move, migalhas se desprendem

#### Particula 0 -- Migalha Grande
- Pedaco irregular de massa de pastel frito (~4x3px dentro do frame 16x16)
- Cor principal: #E8C840 (amarelo dourado de massa frita)
- Borda mais escura (#A07D14) sugerindo crosta
- 1 pixel de brilho de gordura (#FFD700) no ponto mais alto
- Formato organico, irregular -- NAO e um quadrado perfeito

#### Particula 1 -- Migalha Media
- Menor que Particula 0 (~3x2px)
- Mesma paleta, menos detalhes
- Levemente rotacionada comparada a 0
- Sem brilho de gordura (so cor base e sombra)

#### Particula 2 -- Migalha Pequena
- Apenas ~2x2px de migalha
- Cor unica (#D4A017) com 1px de sombra
- Quase desaparecendo, fim do ciclo de vida

#### Particula 3 -- Mancha de Gordura
- Nao e uma migalha solida -- e uma gota de gordura
- ~3x3px, semi-transparente (#D4A01740)
- Brilho oleoso no centro (1px #FFD700 50%)
- Persiste um pouco no chao antes de desaparecer (efeito de area suja)

---

## 4. Notas de Dinheiro Caindo (Money Drop)

**Dimensoes:** 16x16 px por frame
**Frames:** 4 (rotacao em queda, loop)
**Sprite sheet:** 64x16 px
**Comportamento:** A cada 3-5 segundos, uma nota cai do bolso de Gilmar e flutua ate o chao

#### Frame 0 -- Nota Frente (Saindo do Bolso)
- Nota de dinheiro vista de frente (~10x6px dentro de 16x16)
- Papel verde (#2E7D32) com borda mais escura
- Cifra "R$" em dourado (#FFD700) no centro-esquerda
- Numeros sugeridos na direita (scribble cinza, ilegivel)
- Retrato minusculo de rosto generico no centro (3x3px, tom de pele)
- Contorno preto fino (1px)
- A nota esta LIMPA e PLANA -- acabou de sair do bolso

#### Frame 1 -- Nota Girando (45 graus)
- A nota esta rotacionada ~45 graus, comecando a "planar"
- Perspectiva mostra a nota ficando mais fina (achatada pela rotacao)
- O verde ainda visivel, cifra parcialmente obscurecida
- Leve ondulacao na nota (borda superior curvada)
- Comeco de trail (1px verde atras, 30% opacidade)

#### Frame 2 -- Nota de Lado (90 graus)
- A nota vista quase de perfil -- apenas uma faixa fina verde (2x6px)
- Borda com highlight (#4CAF50) no topo
- Sombra (#1B5E20) embaixo
- Trail mais pronunciado (2px, opacidades decrescentes)
- A nota esta descendo (posicao 2px mais abaixo no frame que Frame 0)

#### Frame 3 -- Nota Verso (Quase completou giro)
- A nota mostra o verso -- mais liso, com linhas horizontais (pauta)
- Cor ligeiramente diferente (#388E3C) para diferenciar do frente
- Numero serial sugerido no topo (scribble fino)
- A nota ondula mais (borda ondulada mais pronunciada)
- Trail no maximo (3px, desvanecendo)
- Loop: 0 -> 1 -> 2 -> 3 -> 0 enquanto a nota flutua ate o chao

---

## 5. Brilho de Teflon (Shield Shimmer)

**Dimensoes:** 64x64 px por frame (overlay sobre a toga inteira)
**Frames:** 3 (loop sutil constante)
**Sprite sheet:** 192x64 px

### Descricao Geral
Um brilho oleoso, quase sobrenatural, que percorre a superficie da toga constantemente. Sugere que a toga tem uma propriedade magica/cientifica que repele tudo. O shimmer deve parecer "errado" -- nao e um tecido normal brilhando, e algo QUIMICO e ANTINATURAL.

#### Frame 0 -- Shimmer Posicao A
- Linhas de brilho finas (#6A6A6A -> #A0A0A0 gradiente) em posicoes diagonais (superior-esquerda para inferior-direita)
- 2-3 linhas de shimmer, cada uma com 8-12px de comprimento, 1px de largura
- As linhas seguem as DOBRAS da toga (curvam-se com o tecido)
- Um ponto de brilho maximo (#FFFFFF, 1px) no meio de cada linha
- O shimmer tem aspecto OLEOSO -- nao e metalico limpo, e gorduroso/quimico
- Semi-transparente (50% opacidade geral do layer)

#### Frame 1 -- Shimmer Posicao B
- As linhas de brilho se moveram ~8px na diagonal (descendo-para-direita)
- Novas linhas comecam a aparecer no canto superior-esquerdo onde as anteriores estavam
- Os pontos de brilho maximo estao em posicoes diferentes ao longo das linhas
- Uma das linhas esta mais LARGA (2px) temporariamente -- pulso de teflon
- Efeito geral: como reflexo se movendo em superficie oleosa

#### Frame 2 -- Shimmer Posicao C
- Linhas continuaram se movendo, agora no terco inferior da toga
- As linhas do Frame 0 que chegaram ao fim do tecido estao desvanecendo
- Novas linhas no topo estao no inicio do ciclo
- O brilho mais largo do Frame 1 voltou ao normal
- Um reflexo EXTRA aparece brevemente no ponto onde havia uma mancha de pastel (gordura + teflon = brilho duplo)
- Loop: 0 -> 1 -> 2 -> 0 cria um shimmer hipnotico e perturbador

---

## 6. Efeito de Bloqueio Nao-Reflexivo (Quando NÃO reflete -- 67%)

**Dimensoes:** 32x32 px por frame
**Frames:** 2
**Sprite sheet:** 64x32 px
**Trigger:** Quando projetil acerta Gilmar mas NAO reflete (67% das vezes -- ele ainda toma dano)

#### Frame 0 -- Impacto Absorvido
- O projetil atinge a toga e cria um pequeno impacto ABAFADO
- Flash menor que o reflexivo (raio 3px, #A0A0A0, 40% opacidade)
- A toga absorve o impacto com uma leve ondulacao local (2-3px de deformacao no tecido)
- Particulas de migalha de pastel sacudidas pelo impacto (2 migalhas voando)
- Sem ondas concentricas (diferenca visual clara do efeito reflexivo)
- Uma gota de teflon se desprende (1px prateado caindo)

#### Frame 1 -- Impacto Dissipando
- Flash desvanecido
- Toga voltando ao normal
- Migalhas continuam flutuando para longe
- Leve marca de impacto no tecido (1-2px mais escuros que o redor) que desaparece em 0.5s
- SEM texto "NADA GRUDA" -- neste caso, GRUDOU

---

## Resumo do Sprite Sheet

| Sheet                      | Frames | Tam. Frame | Tam. Total | Phaser Key                       |
|----------------------------|--------|------------|------------|----------------------------------|
| `toga_idle`                | 4      | 64x64      | 256x64     | `weapon_toga_idle`               |
| `toga_reflect`             | 4      | 48x48      | 192x48     | `fx_toga_reflect`                |
| `toga_migalha`             | 4      | 16x16      | 64x16      | `particle_migalha_pastel`        |
| `toga_dinheiro`            | 4      | 16x16      | 64x16      | `particle_nota_dinheiro`         |
| `toga_shimmer`             | 3      | 64x64      | 192x64     | `fx_toga_shimmer`                |
| `toga_block`               | 2      | 32x32      | 64x32      | `fx_toga_block`                  |

## Configuracao Phaser 3

```javascript
// Toga base + idle
this.load.spritesheet('weapon_toga_idle', 'assets/armas/toga-teflon/toga_idle.png', {
  frameWidth: 64,
  frameHeight: 64
});

// Efeito de reflexao
this.load.spritesheet('fx_toga_reflect', 'assets/armas/toga-teflon/toga_reflect.png', {
  frameWidth: 48,
  frameHeight: 48
});

// Particulas de migalha de pastel
this.load.spritesheet('particle_migalha_pastel', 'assets/armas/toga-teflon/toga_migalha.png', {
  frameWidth: 16,
  frameHeight: 16
});

// Notas de dinheiro caindo
this.load.spritesheet('particle_nota_dinheiro', 'assets/armas/toga-teflon/toga_dinheiro.png', {
  frameWidth: 16,
  frameHeight: 16
});

// Brilho de teflon (overlay)
this.load.spritesheet('fx_toga_shimmer', 'assets/armas/toga-teflon/toga_shimmer.png', {
  frameWidth: 64,
  frameHeight: 64
});

// Bloqueio nao-reflexivo
this.load.spritesheet('fx_toga_block', 'assets/armas/toga-teflon/toga_block.png', {
  frameWidth: 32,
  frameHeight: 32
});
```

## Animacoes Phaser 3

```javascript
// Idle esvoaçante (loop)
this.anims.create({
  key: 'toga_idle',
  frames: this.anims.generateFrameNumbers('weapon_toga_idle', { frames: [1, 2, 3] }),
  frameRate: 6,  // Lento, dramatico
  repeat: -1
});

// Reflexao de projetil (play once quando reflect trigger)
this.anims.create({
  key: 'toga_reflect',
  frames: this.anims.generateFrameNumbers('fx_toga_reflect', { start: 0, end: 3 }),
  frameRate: 10,  // Rapido, impactante
  repeat: 0
});

// Migalha de pastel (particula individual)
this.anims.create({
  key: 'migalha_fall',
  frames: this.anims.generateFrameNumbers('particle_migalha_pastel', { start: 0, end: 3 }),
  frameRate: 4,  // Lento, flutuando
  repeat: 0
});

// Dinheiro caindo (rotacao loop ate atingir chao)
this.anims.create({
  key: 'dinheiro_drop',
  frames: this.anims.generateFrameNumbers('particle_nota_dinheiro', { start: 0, end: 3 }),
  frameRate: 8,
  repeat: -1  // Loop ate callback de chao destruir
});

// Shimmer de teflon (overlay constante)
this.anims.create({
  key: 'toga_shimmer',
  frames: this.anims.generateFrameNumbers('fx_toga_shimmer', { start: 0, end: 2 }),
  frameRate: 3,  // Muito lento, hipnotico
  repeat: -1
});

// Bloqueio absorvido (play once)
this.anims.create({
  key: 'toga_block',
  frames: this.anims.generateFrameNumbers('fx_toga_block', { start: 0, end: 1 }),
  frameRate: 8,
  repeat: 0
});
```

## Logica de Emitters Phaser 3

```javascript
// Emitter de migalhas de pastel (constante enquanto Gilmar se move)
const migalhaEmitter = this.add.particles('particle_migalha_pastel').createEmitter({
  speed: { min: 10, max: 30 },
  angle: { min: 230, max: 310 },  // Cai para baixo e para os lados
  lifespan: 2000,
  frequency: 800,  // Uma migalha a cada 0.8s
  gravityY: 50,
  scale: { start: 1, end: 0.3 },
  alpha: { start: 0.8, end: 0 },
});
migalhaEmitter.startFollow(gilmarSprite);

// Emitter de notas de dinheiro (periodico)
const dinheiroEmitter = this.add.particles('particle_nota_dinheiro').createEmitter({
  speed: { min: 5, max: 20 },
  angle: { min: 250, max: 290 },  // Quase reto para baixo
  lifespan: 3000,
  frequency: 4000,  // Uma nota a cada 3-5 segundos
  gravityY: 30,
  rotate: { min: 0, max: 360 },  // Gira enquanto cai
  scale: { start: 1, end: 0.8 },
  alpha: { start: 1, end: 0.5 },
});
dinheiroEmitter.startFollow(gilmarSprite, 8, -4);  // Offset para o bolso
```

---

## Notas para o Artista

- A toga DEVE ser MAIOR que o Gilmar -- ela domina o sprite, esvoaca dramaticamente como capa de vilao
- As MANCHAS DE PASTEL sao essenciais -- sao o detalhe comico que humaniza (e ridiculariza) o boss
  - Devem parecer GORDUROSAS e REAIS -- nao abstratas
  - Referencia: manchas de oleo em avental de cozinheiro, mas numa toga oficial do STF
- O DINHEIRO CAINDO e constante e descarado -- o bolso e um buraco negro de corrupcao
  - As notas devem ser reconhecivelmente DINHEIRO BRASILEIRO (verde, cifras)
  - O fato de cair constantemente e o piada: ele nem se importa mais em esconder
- O BRILHO DE TEFLON e o elemento sobrenatural -- deve parecer ERRADO no tecido
  - Nao e reflexo de seda ou cetim -- e reflexo QUIMICO, INDUSTRIAL, ANTINATURAL
  - Referencia visual: superficies de teflon industrial, panelas antiaderentes
  - O brilho e a explicacao visual de por que nada gruda
- O efeito de REFLEXAO deve ser SATISFATORIAMENTE FRUSTRANTE para o jogador
  - O flash branco/prateado e o "NADA GRUDA!" devem comunicar INSTANTANEAMENTE o que aconteceu
  - O jogador precisa entender em milissegundos: "meu tiro voltou em mim"
- DIFERENCIAR CLARAMENTE reflexao (33%) de bloqueio normal (67%) visualmente
  - Reflexao: flash grande, ondas concentricas, "NADA GRUDA!", projetil visivelmente retornando
  - Bloqueio: flash pequeno, sem ondas, sem texto, projetil simplesmente some
- Contornos GROSSOS e IRREGULARES (3px minimo) estilo Robert Crumb / Andre Guedes
- A toga nao e elegante -- e GROTESCA. Rica, mas suja. Imponente, mas corrupta.
- Cada frame deve transmitir a sensacao de um homem que esta ACIMA DA LEI e sabe disso
- O humor vem do contraste: um artefato de poder SUPREMO coberto de migalha de pastel e notas caindo
- Referencia emocional: a frustracao de tentar acusar alguem intocavel no sistema juridico brasileiro
