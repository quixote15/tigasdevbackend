# Flavio Bolsonaro (O Herdeiro) - Skin Variants

## Base Character Reference
- **Tipo:** Mini-boss / Rival do Eduardo / Candidato 2026
- **Base Dimensions:** 64x64px per frame
- **Style:** Grotesque underground comix, Robert Crumb, thick outlines

---

## SKIN 1: NORMAL (Terno Azul "Moderado")
**Unlock:** Default skin

### Description
O Flavio padrao -- tentando ser o politico serio e moderado que ninguem acredita. E a versao mais "composta" e polida (na superficie).

### Visual Details
- **Terno:** Azul marinho escuro (#1B2A4A), corte classico, bem ajustado
- **Camisa:** Branca impecavel (#F0EDE5), colarinho engomado
- **Gravata:** Vermelha discreta (#8B1A1A), no classico
- **Cabelo:** Penteado com gel excessivo, brilho no topo (#3D2B1F com highlight #5A4030)
- **Abotoaduras:** Douradas (#D4A940), ostentacao disfarçada
- **Sapatos:** Pretos sociais, engraxados
- **Acessorios:** Relogio discreto (mas caro) no pulso esquerdo
- **Expressao:** Sorriso ensaiado permanente, olhos que piscam demais

### Color Palette
| Element          | Hex       |
|------------------|-----------|
| Terno principal  | `#1B2A4A` |
| Terno highlight  | `#2C3E6B` |
| Terno shadow     | `#0D1A2E` |
| Camisa           | `#F0EDE5` |
| Gravata          | `#8B1A1A` |
| Abotoaduras      | `#D4A940` |
| Pele             | `#D4A574` |
| Cabelo           | `#3D2B1F` |

### Alteracoes por Animacao
- **Death:** Terno rasga revelando tatuagem "BOLSONARO" no peito
- **Hit:** Terno amassa no ponto de impacto, recupera mecanicamente
- **Special:** Mancha de suor na axila apos dança

---

## SKIN 2: CAMPANHA 2026 (Terno + Faixa Presidencial Imaginaria)
**Unlock:** Completar Chapter 3 "A Sucessao" OU derrotar Flavio como mini-boss

### Description
Flavio no auge da delusao eleitoral. Veste o terno padrao MAS com uma faixa presidencial que ele mesmo costurou. A faixa e OBVIAMENTE falsa -- costurada torta, com letras feitas a mao, bordas desfiando. Ele acredita que ja venceu.

### Visual Details
- **Terno:** Mesmo azul marinho, porem com PIN de campanha no peito esquerdo (circulo verde-amarelo, 4x4px)
- **Faixa Presidencial:** Faixa verde-amarela diagonal do ombro direito ao quadril esquerdo
  - CLARAMENTE FALSA: costura irregular (linhas pontilhadas tortas), bordas desfiando
  - Texto "PRESIDENTE" escrito a mao (letras tortas, tamanho inconsistente)
  - O verde e amarelo sao levemente ERRADOS (verde lima #7FCC00 em vez de verde bandeira, amarelo neon #FFD700 em vez de ouro)
  - 1-2 manchas de cola visivel onde ele colou pedras de strass
- **Cabelo:** MAIS gel que o normal -- parece capacete brilhante
- **Gravata:** Trocou para verde-amarela (patriotica, mas de mal gosto)
- **Sapatos:** Mesmos, porem com adesivo de campanha colado na sola (visivel no walk frame 1/3)
- **Expressao:** Sorriso AINDA MAIS LARGO (se possivel) -- confiança delirante

### Color Palette Delta (vs Normal)
| Element          | Hex       | Nota                              |
|------------------|-----------|-----------------------------------|
| Faixa verde      | `#7FCC00` | Verde ERRADO (lima, nao bandeira) |
| Faixa amarelo    | `#FFD700` | Amarelo ERRADO (neon, nao ouro)   |
| Faixa texto      | `#1A1A1A` | Letras tortas a mao               |
| Faixa borda      | `#5A8F00` | Borda desfiando                   |
| PIN campanha     | `#228B22` | + `#FFD700` centro                |
| Gravata          | `#228B22` | Trocada para verde                |

### Alteracoes por Animacao
- **Idle:** A faixa escorrega 1px para baixo no Frame 2 (ele ajusta discretamente)
- **Walk:** A faixa balança levemente, ameaçando cair
- **Attack:** A faixa se desajusta completamente no grito (Frame 1), ele a reposiciona no Frame 2
- **Death:** A faixa cai ao lado do corpo. Tatuagem + faixa no chao = comedia maxima
- **Special:** Faixa destaca durante a dança, "+2026" aparece ao inves de "+10K"

### Bordoes Extras (Skin-Specific)
- "O povo ME escolheu! ...ainda nao, mas VAI escolher."
- "Esta faixa e PROVISORIA. Em breve, a oficial."

---

## SKIN 3: ZOMBIE (Terno Rasgado, Tatuagem Exposta)
**Unlock:** Completar o jogo no modo Nightmare OU encontrar segredo no Stage "Cadeia de Papuda"

### Description
Flavio pos-zombificacao. O terno caro esta em frangalhos. A tatuagem "BOLSONARO" esta permanentemente exposta e BRILHA com energia verde doentia. O sorriso ensaiado agora e literal -- os musculos do rosto TRAVARAM na posicao de sorriso por rigor mortis. Os olhos nao piscam mais (o nervosismo morreu com ele).

### Visual Details
- **Terno:** Azul marinho DESTRUIDO -- rasgos por todo lado, um ombro exposto, a outra manga pendurada por um fio
  - Cor desbotada: azul marinho agora acinzentado (#2A3040)
  - Manchas de terra/lama (#4A3520) nas costas e joelhos
  - Furos de bala/mordida (circulos irregulares revelando pele esverdeada)
- **Camisa:** Aberta, botoes arrancados, revelando tatuagem permanentemente
- **Tatuagem "BOLSONARO":** Agora BRILHA em verde toxico (#33FF33, pulsando)
  - Glow effect: 2px halo verde ao redor das letras
  - Pulsa a cada 500ms (alpha 0.6 -> 1.0 -> 0.6)
- **Pele:** Tom verde-acinzentado (#7A9070) -- zombificada
  - Veias visiveis em verde escuro (#3D5030) no pescoco e bracos
  - Manchas de decomposicao marrom-esverdeadas
- **Cabelo:** Gel DERRETEU -- cabelo em todas as direcoes, com musgo verde
- **Olhos:** Amarelo-esverdeados (#AACC33), nao piscam NUNCA, pupilas dilatadas
- **Sorriso:** TRAVADO por rigor mortis -- identico ao sorriso ensaiado, mas os dentes estao manchados e 2 estao faltando. O efeito e mais perturbador que o sorriso original.
- **Gravata:** Pendurada em um pedaco, vermelha desbotada para rosa (#CC6666)
- **Abotoaduras:** Uma perdida, a outra enferrujada (#8B7340)

### Color Palette Delta (vs Normal)
| Element            | Hex       | Nota                            |
|--------------------|-----------|----------------------------------|
| Terno (desbotado)  | `#2A3040` | Azul acinzentado                 |
| Pele zombie        | `#7A9070` | Verde-cinza                      |
| Pele shadow        | `#5A7050` | Verde mais escuro                |
| Tatuagem glow      | `#33FF33` | Verde toxico brilhante           |
| Tatuagem base      | `#CC2222` | Mesmo vermelho, mais saturado    |
| Olhos              | `#AACC33` | Amarelo-verde doentio            |
| Cabelo             | `#3D4030` | Castanho + musgo verde           |
| Veias              | `#3D5030` | Verde escuro, visiveis           |
| Dentes             | `#D0C890` | Amarelados/manchados             |
| Gravata desbotada  | `#CC6666` | Vermelho -> rosa desbotado       |

### Alteracoes por Animacao
- **Idle:** SEM piscar (olhos travados abertos). Tatuagem PULSA no ritmo do idle. O corpo faz micro-tremble (1px shake) em vez do piscar nervoso.
- **Walk:** Manca levemente (1 frame com tilt 2px). O gel derretido escorre 1px (particula). Pedacos de terno caem (1 particula a cada 3 ciclos).
- **Attack:** O grito e MAIS GRAVE (pitch down). O balao de fala tem simbolos VERDES ao inves de pretos. Ondas sonicas sao verdes.
- **Death:** A tatuagem faz EXPLOSION de luz verde. O fantasma do pai tambem aparece como zombie.
- **Special:** Dança "Sera?" mas em slow motion (FPS reduzido para 6). Ondas hipnoticas sao VERDES toxicas ao inves de pink/cyan.
- **Hit:** NAO trava o sorriso (ja esta travado). Em vez disso, pedacos de pele/terno se soltam como particulas.

### VFX Especiais da Skin
- **Tatuagem Pulse:** `this.tweens.add({ alpha: { from: 0.6, to: 1 }, duration: 500, yoyo: true, repeat: -1 })` na overlay da tatuagem
- **Particulas de Decomposicao:** Emitter constante -- 1 particula verde (#5A7050, 1x1px) a cada 2 segundos, cai com gravidade
- **Trail de Lama:** Ao caminhar, mancha marrom (#4A3520, 2x2px, alpha 0.2) no chao, fade em 3 segundos

---

## SKIN 4: TIKTOKER (Roupa Casual da Trend "Sera?")
**Unlock:** Fazer o skill "Sera?" 50 vezes no total OU completar side quest "Viral Challenge"

### Description
Flavio em modo INFLUENCER. Largou o terno, vestiu roupa "jovem" que NAO combina com ele. E um homem de 40+ anos tentando parecer de 25. Cada peça e de uma marca diferente (mostrando que nao entende moda). O celular dourado agora esta PERMANENTEMENTE na mao.

### Visual Details
- **Camiseta:** Preta oversized com logo generico de marca streetwear (circulo + X em branco)
  - Camiseta grande DEMAIS (ele comprou o tamanho dos "jovens")
  - Pende nos ombros, mostrando mais pescoco
- **Calca:** Jeans skinny (apertada DEMAIS para a idade) (#3D5580)
  - Rasgos nos joelhos (tentando trend destroyed jeans)
  - Os rasgos sao PERFEITAMENTE simetricos (ele comprou assim, nao sao naturais)
- **Tenis:** Branco chunky/platform (#F0F0E0), desproporcional (parece espacial)
  - Logo generico colorido no lado
- **Acessorios:**
  - Bone branco virado para tras (#F0F0E0) com texto "SERA?" em rosa neon
  - Corrente dourada fina no pescoco (#D4A940) -- tentando ser "drip"
  - Ring light miniatura flutuando atras (referencia a setup de TikTok)
  - Celular DOURADO permanentemente na mao esquerda
- **Cabelo:** Visivel sob o bone -- sem gel pela primeira vez, mais natural (e melhor assim, ironicamente)
- **Expressao:** Sorriso mais NATURAL nesta skin (o TikTok e o unico lugar onde ele se solta). Mas ainda pisca demais.
- **Oculos de Sol:** Aviador espelhado no topo da cabeca (nao nos olhos) -- pose de influencer

### Color Palette
| Element           | Hex       | Nota                           |
|-------------------|-----------|--------------------------------|
| Camiseta preta    | `#1A1A1A` | Oversized                      |
| Logo camiseta     | `#F0F0E0` | Circulo + X generico           |
| Jeans             | `#3D5580` | Skinny                         |
| Tenis branco      | `#F0F0E0` | Chunky platform                |
| Bone branco       | `#F0F0E0` | Virado para tras               |
| Bone texto "SERA?"| `#FF69B4` | Rosa neon                      |
| Corrente          | `#D4A940` | Dourada fina                   |
| Celular           | `#D4A940` | Dourado, sempre na mao         |
| Oculos espelhado  | `#88BBDD` | Aviador, reflexo azul          |
| Pele              | `#D4A574` | Mesma                          |

### Alteracoes por Animacao
- **Idle:** Fica olhando o celular e sorrindo (scroll TikTok). Piscar substituido por scroll do polegar.
- **Walk:** Caminhada mais SOLTA (nao tem terno restringindo). Mas ainda rigida porque e ele. Tenis grandes fazem bounce exagerado.
- **Attack:** Em vez de discurso, grava video (celular vira camera). O flash do celular e o ataque. Balao de fala substituido por notificacao push.
- **Death:** Celular cai no chao e QUEBRA (tela rachada). Ultima notificacao aparece: "0 views". O bone voa. SEM revelacao de tatuagem (esta de camiseta).
- **Special:** "Sera?" com BUFF -- ondas hipnoticas 20% maiores, stun 0.5s mais longo. Flavio mais no ritmo. Ring light atras intensifica.
- **Hit:** Celular quase cai (mao treme). Bone vira levemente. Oculos caem do topo da cabeca para o nariz.

### Bordoes Extras (Skin-Specific)
- "Curtam, sigam e compartilhem!"
- "Link na bio!"
- "Like se voce quer renovacao! ...com o sobrenome Bolsonaro."

---

## SKIN 5: HERDEIRO (Uniforme Identico ao Pai + Grade de Prisao como Sombra)
**Unlock:** Boss secreto -- derrotar o fantasma do Bolsonaro pai no Stage "Cadeia de Papuda"

### Description
A skin mais SOMBRIA e tematica. Flavio veste um uniforme IDENTICO ao que o pai usava (terno escuro, estilo mais agressivo dos anos Bolsonaro). A diferença: ao inves de sombra normal no chao, a sombra de Flavio sao GRADES DE PRISAO. Onde quer que ele va, as grades o seguem. O sobrenome e literalmente uma prisao.

### Visual Details
- **Terno:** Escuro quase preto (#0D1520), mais largo nos ombros (imitando o pai)
  - Corte mais "agressivo" que o normal -- ombros exageradamente largos (power suit)
  - Lapela larga estilo anos 2000
  - PIN de bandeira do Brasil no peito (obrigatorio -- referencia ao pai)
- **Camisa:** Branca, mas com colarinho ALTO (estilo militar-politico)
- **Gravata:** Azul royal (#1A3CCC) com listras diagonais douradas -- a gravata FAVORITA do pai
- **Cabelo:** Penteado IDENTICO ao do pai (mais para o lado, menos gel, mais volume)
  - Cor levemente mais clara pra simular o envelhecimento acelerado pelo estresse (#4A3828)
- **Expressao:** O sorriso ensaiado agora e uma COPIA do sorriso do pai (mais agressivo, menos "moderado")
  - Queixo PROEMINENTE no maximo (imitando o queixo do pai)
  - Olhos mais apertados (tentando o olhar intimidador do pai)
  - Mas o piscar nervoso permanece (ele NAO consegue copiar isso)
- **Sombra no Chao:** Em vez de ellipse escura normal, a sombra e formada por LINHAS VERTICAIS (grades de prisao)
  - 5-6 linhas verticais (#0D0D0D, alpha 0.3)
  - Se movem com o personagem
  - Leve distorcao/ondulacao (as grades sao vivas)
- **Mao Direita:** Segura um papel enrolado (carta do pai da prisao)
- **Acessorios:** Broche "27" discreto na lapela (27 anos de pena do pai, referencia sutil)

### Color Palette
| Element               | Hex       | Nota                            |
|-----------------------|-----------|----------------------------------|
| Terno quase-preto     | `#0D1520` | Mais escuro que normal           |
| Terno highlight       | `#1A2535` | Reflexo sutil                    |
| Terno shadow          | `#060A10` | Quase invisivel                  |
| Ombros (power suit)   | `#0D1520` | Exageradamente largos            |
| Gravata azul royal    | `#1A3CCC` | A do pai                         |
| Gravata listras       | `#D4A940` | Douradas diagonais               |
| PIN bandeira verde    | `#009739` | No peito                         |
| PIN bandeira amarelo  | `#FEDD00` | Centro                           |
| Camisa colarinho alto | `#F0EDE5` | Militar-politico                 |
| Cabelo (estilo pai)   | `#4A3828` | Mais claro, mais estresse        |
| Sombra grades         | `#0D0D0D` | Alpha 0.3, linhas verticais      |
| Broche "27"           | `#C0C0C0` | Prata discreto                   |
| Papel/carta           | `#F0E8D0` | Envelhecido, borda irregular     |

### Alteracoes por Animacao
- **Idle:** A sombra de grades pulsa levemente (expand/contract 1px). O papel na mao treme. O piscar nervoso e MAIS FREQUENTE (a cada 2 segundos em vez de 3-5). Ele olha para tras por 1 frame a cada 8 segundos (paranoia).
- **Walk:** As grades na sombra "caminham" junto, mas com delay de 2 frames (parecem arrastar). O stride e mais largo e agressivo (imitando o pai). Os ombros power suit balancam.
- **Attack:** O grito e mais GRAVE e AGRESSIVO (imitando o pai). O papel na mao se transforma em megafone por 1 frame. A sombra de grades se LEVANTA do chao durante o ataque (2D effect -- grades parecem ficar verticais atras dele).
- **Death:** As grades da sombra se FECHAM ao redor dele (convergem para o corpo). A carta do pai cai e se dissolve. O fantasma do pai aparece mais SOLIDO (30% opacity ao inves de 10%). Ultima expressao: olha para cima como se visse o pai. Os ombros power suit deflate (encolhem 2px).
- **Special ("Sera?"):** Desajeitado nesta skin -- ele TENTA dancar mas o terno pesado e a sombra de grades dificultam. Ondas hipnoticas sao azul-escuro (#1A3CCC) ao inves de rosa. Zema NAO aparece (este Flavio e serio demais). No lugar, a sombra do pai danca por 1 frame (easter egg).
- **Hit:** As grades da sombra TREMEM violentamente. O papel cai e ele pega rapidamente. O sorriso trava no estilo do PAI (mais agressivo) ao inves do sorriso "moderado" normal.

### VFX Especiais da Skin
- **Sombra de Grades:**
  ```javascript
  // Em vez do shadow ellipse normal, desenhar grades
  const gradesShadow = this.add.graphics();
  gradesShadow.lineStyle(1, 0x0D0D0D, 0.3);
  for (let i = -10; i <= 10; i += 4) {
      gradesShadow.lineBetween(
          sprite.x + i, sprite.y + 24,
          sprite.x + i, sprite.y + 32
      );
  }
  // Horizontal bar
  gradesShadow.lineBetween(
      sprite.x - 10, sprite.y + 28,
      sprite.x + 10, sprite.y + 28
  );
  ```

- **Grades Pulse (Idle):**
  ```javascript
  this.tweens.add({
      targets: gradesShadow,
      scaleX: { from: 1.0, to: 1.05 },
      scaleY: { from: 1.0, to: 0.95 },
      duration: 2000,
      yoyo: true,
      repeat: -1,
      ease: 'Sine.easeInOut'
  });
  ```

- **Grades Fecham (Death):**
  ```javascript
  // Linhas convergem para o centro
  this.tweens.add({
      targets: gradeLines, // array de line objects
      x: sprite.x, // todas convergem para o centro
      duration: 400,
      ease: 'Power2'
  });
  ```

### Bordoes Extras (Skin-Specific)
- "Meu pai me escolheu. De DENTRO da cadeia."
- "27 anos? ...isso nao vai ficar assim."
- "Eu sou a continuacao." (tom sombrio)
- "A heranca e mais pesada que o terno."

---

## COMPARATIVE TABLE

| Feature          | Normal        | Campanha 2026  | Zombie          | TikToker       | Herdeiro        |
|------------------|---------------|----------------|-----------------|----------------|-----------------|
| Terno            | Azul marinho  | Azul + faixa   | Destruido       | Sem terno      | Quase-preto     |
| Sorriso          | Ensaiado      | Delirante      | Rigor mortis    | Mais natural   | Copia do pai    |
| Piscar           | Nervoso       | Menos (confiante) | ZERO          | Scroll celular | Mais frequente  |
| Tatuagem         | Escondida     | Escondida      | Exposta+glow    | N/A            | Escondida       |
| Sombra           | Normal        | Normal         | Normal+trail    | Normal         | GRADES PRISAO   |
| Special VFX      | Pink/cyan     | Green/yellow   | Green toxico    | Pink+buff      | Blue escuro     |
| Tone             | Satirico      | Delusional     | Horror          | Cringe comedy  | Sombrio/tragico |
| Deformidade      | Sorriso+piscar| Sorriso+faixa  | Rigor mortis    | Cringe outfit  | Grades+paranoia |

---

## SKIN SELECTION UI

### Preview
- Cada skin mostra idle animation (4 frames) no menu de selecao
- Fundo: silhueta do Congresso Nacional (identico para todos)
- Nome da skin em fonte estilizada abaixo
- Icone de cadeado para skins nao desbloqueadas (com hint de como desbloquear)

### Unlock Notifications
```
SKIN DESBLOQUEADA!
[Preview da skin girando 360]
"[Nome da Skin]"
[Descricao em 1 linha]
```
