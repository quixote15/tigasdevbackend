# Sprite Spec — MONARK (O Rei do Limbo)

> NPC do Game Over / Loja do Limbo. Apresentador do "Limbo dos Cancelados".
> Crossover META entre Zumbis em Brasilia e Limbo dos Cancelados (Andre Guedes).
> Sprites 64x64px, PNG com transparencia.
> Estilo: Andre Guedes — grotesco, underground comix, Robert Crumb + humor politico BR.

---

## 1. Tipo de Personagem

| Parametro | Valor |
|---|---|
| **Tipo** | NPC (nao-jogavel, nao-combatente) |
| **Contexto** | Tela de Game Over / Loja do Limbo |
| **Interacao** | Dialogo + Loja + Mini-desafio de revive |
| **Sprite size** | 64x64px |
| **Perspectiva** | Top-down levemente isometrica (consistente com o jogo) |
| **Formato** | PNG-8 com transparencia |
| **Proporcoes** | Cabeca 1.5x, torso 2x, pernas 1.5x (~5 cabecas total, atarracado) |
| **Contorno** | Linhas grossas 2-4px, irregulares, simulando mao humana |

---

## 2. Anatomia e Deformidade

### Proporcoes Gerais (dentro do 64x64)
```
┌────────────────────────────────────────┐
│  CHAPEU DE PESCADOR (topo)             │  ~8px altura
│  ┌──────────────────────────────┐      │
│  │  CABECA (1.5x proporcional)  │      │  ~14px altura
│  │  Olhos semicerrados          │      │
│  │  Sorriso bobo permanente     │      │
│  │  FUMACA saindo das orelhas   │      │
│  └──────────────────────────────┘      │
│         │  PESCOCO curto │             │
│  ┌──────────────────────────────┐      │
│  │  TORSO (2x, sentado)        │      │  ~18px altura
│  │  Camiseta largona            │      │
│  │  Microfone de podcast na mao │      │
│  │  Mao apoiada no braco cadeira│      │
│  └──────────────────────────────┘      │
│  ┌──────────────────────────────┐      │
│  │  PERNAS (1.5x, sentado)     │      │  ~12px altura
│  │  Bermuda/calca larga         │      │
│  │  Pes pendurados (cadeira     │      │
│  │  FLUTUA, nao toca o chao)   │      │
│  └──────────────────────────────┘      │
│  ═══ CADEIRA DE PODCAST ═══           │  ~10px (flutuante)
│       (sombra no void abaixo)          │
└────────────────────────────────────────┘
```

### Deformidade Principal: PUPILAS DILATADAS + FUMACA NAS ORELHAS
- **Olhos**: Semicerrados (palpebras pesadas, 60% fechados), mas as PUPILAS sao discos enormes pretos que ocupam quase todo o iris visivel. Aspecto de "chapado permanente".
- **Fumaca**: Das orelhas sai fumaca verde-acinzentada que se dissipa (2-3 wisps de fumaca, animados separadamente do sprite base).
- **Efeito combinado**: Da a impressao que o cerebro dele esta literalmente fumegando — "queimou os neuronios com filosofia barata".

### Elementos Faciais
| Elemento | Descricao | Pixels Aproximados |
|---|---|---|
| **Olhos** | Semicerrados, iris quase coberto pela palpebra, pupila GIGANTE preta | 4x2px cada, pupila 3x2px |
| **Sobrancelhas** | Relaxadas, levemente arqueadas (nao raiva, nao surpresa — apatia chapada) | 5x1px cada |
| **Nariz** | Grande, bulboso, vermelho na ponta (capilares estourados) | 4x3px |
| **Boca** | Sorriso bobo permanente, dentes a mostra, labios grossos | 6x3px |
| **Barba** | Barba rala, mal-feita, fios irregulares | Hachura 1px em cross |
| **Orelhas** | Ligeiramente pontudas/grandes, com FUMACA saindo | 2x3px + wisps |

---

## 3. Vestimenta e Acessorios

### Chapeu de Pescador (Marca Registrada)
- **Tipo**: Bucket hat / chapeu de pescador estilo anos 2000
- **Cor**: `#5A6B55` (verde musgo desbotado) com manchas `#3A4A38`
- **Posicao**: Levemente torto, inclinado pra um lado
- **Detalhe**: Aba mole, amassada, com 1 anzol preso na aba (1px dourado `#C8A832`)
- **Tamanho no sprite**: ~16x6px (ocupa boa parte da largura da cabeca)

### Camiseta
- **Tipo**: Camiseta largona, gola larga, mangas longas ate cotovelo
- **Cor**: `#2A2A2A` (preto desbotado para cinza escuro)
- **Estampa**: Estampa quase apagada no peito (pode ser logo do podcast, ilegivel a 64px — representado como mancha `#3A3A3A` de 4x3px)
- **Detalhe**: Amarrotada, dobras visíveis (linhas 1px mais escuras)

### Bermuda/Calca
- **Tipo**: Bermuda larga, abaixo do joelho
- **Cor**: `#4A4A44` (cinza medio sujo)
- **Detalhe**: Bolsos laterais salientes, barra desfiada

### Microfone de Podcast
- **Tipo**: Microfone condensador de mesa estilo podcast (nao handheld)
- **Cor**: `#5C5C5C` corpo, `#8A8A8A` grade do microfone, `#3A3A3A` suporte
- **Posicao**: Na frente do Monark, ligeiramente a esquerda, em braco articulado
- **Tamanho no sprite**: ~6x10px (incluindo suporte)
- **Detalhe importantissimo**: Uma luz vermelha "ON AIR" de 1px (`#CC3030`) piscando

### Cadeira de Podcast (FLUTUANTE)
- **Tipo**: Cadeira gamer/escritorio com encosto alto
- **Cor**: `#1A1A18` base, `#D47820` detalhes (glow laranja)
- **Posicao**: Monark esta SENTADO nela, e ela FLUTUA no void
- **Efeito flutuacao**: Bob vertical de 2px (sobe e desce lentamente)
- **Sombra abaixo**: Circulo difuso `#0A0A0A` alpha 30%, 1-2px abaixo

### Chinelos
- **Tipo**: Chinelos de dedo (Havaianas)
- **Cor**: `#2A5A3A` (verde escuro)
- **Detalhe**: Pes pendurados com chinelos frouxos, um quase caindo (gravidade do void)

---

## 4. Paleta de Cores

| Elemento | Hex | Notas |
|---|---|---|
| **Pele** | `#D4956A` | Tom quente, levemente avermelhado |
| **Pele sombra** | `#B07848` | Cross-hatching nas sombras faciais |
| **Nariz ponta** | `#CC5555` | Vermelho de capilares |
| **Chapeu** | `#5A6B55` | Verde musgo desbotado |
| **Chapeu sombra** | `#3A4A38` | Manchas e dobras |
| **Camiseta** | `#2A2A2A` | Preto desbotado |
| **Bermuda** | `#4A4A44` | Cinza medio sujo |
| **Chinelos** | `#2A5A3A` | Verde escuro |
| **Cabelo (sob chapeu)** | `#3A2A1A` | Castanho escuro, pouco visivel |
| **Barba rala** | `#4A3A2A` | Fios irregulares |
| **Pupila dilatada** | `#0A0A0A` | Preto quase total |
| **Iris** | `#6B5A3A` | Castanho, quase coberto |
| **Branco do olho** | `#E8D8C8` | Amarelado (olhos cansados/chapados) |
| **Fumaca orelha** | `#6A8A6A` alpha 50% | Verde-cinza, difusa |
| **Microfone** | `#5C5C5C` | Metal escuro |
| **Mic ON AIR** | `#CC3030` | LED vermelho piscante |
| **Cadeira base** | `#1A1A18` | Preto |
| **Cadeira glow** | `#D47820` | Laranja/brilho eterico |
| **Contorno geral** | `#1A1A18` | Linhas 2-4px irregulares |

---

## 5. Sprite States (NPC)

Como NPC, Monark NAO tem walk/run/attack sprites tradicionais. Em vez disso:

### S01 — IDLE (Sentado no Podcast)
- **Frames**: 4 (loop)
- **FPS**: 4 (propositalmente lento, chapado)
- **Descricao**: Sentado na cadeira flutuante, segurando microfone, sorriso bobo. Cadeira faz bob vertical de 2px. Fumaca sai das orelhas.
- **Variacao entre frames**: Palpebras oscilam (mais abertas → mais fechadas → mais abertas), fumaca muda de formato, LED pisca.
- **Arquivo**: `monark-idle.png` (spritesheet 256x64, 4 frames)

### S02 — FALANDO (Dialogo Ativo)
- **Frames**: 6 (loop durante dialogo)
- **FPS**: 8 (mais rapido, gesticulando)
- **Descricao**: Boca abre e fecha em ciclo. Mao livre gesticula (levanta e abaixa). Sobrancelhas se movem. Chapeu treme levemente.
- **Variacao entre frames**: Boca aberta/fechada, mao sobe/desce, sobrancelha sobe quando "filosofa".
- **Arquivo**: `monark-talking.png` (spritesheet 384x64, 6 frames)

### S03 — OFERECENDO DEAL (Loja do Limbo)
- **Frames**: 4 (loop)
- **FPS**: 6
- **Descricao**: Inclina-se pra frente na cadeira. Mao estendida como quem oferece algo. Sorriso mais largo. Pupilas brilham levemente (reflexo `#3D6B3A`).
- **Variacao entre frames**: Inclinacao pra frente/pra tras, mao oscila, brilho nas pupilas pisca.
- **Arquivo**: `monark-deal.png` (spritesheet 256x64, 4 frames)

### S04 — REACAO POSITIVA (Jogador aceita deal)
- **Frames**: 6 (play once)
- **FPS**: 10
- **Descricao**: Levanta os bracos, chapeu salta da cabeca por 1 frame, sorriso ENORME, olhos abrem mais (revelando pupilas dilatadas por completo). Fumaca sai em rajada.
- **Arquivo**: `monark-happy.png` (spritesheet 384x64, 6 frames)

### S05 — REACAO NEGATIVA (Jogador recusa)
- **Frames**: 4 (play once)
- **FPS**: 6
- **Descricao**: Encolhe ombros tipo "tanto faz", olhos fecham mais ainda, sorriso continua (nao se importa). Fumaca diminui.
- **Arquivo**: `monark-shrug.png` (spritesheet 256x64, 4 frames)

### S06 — PODCAST DO LIMBO (Mini-desafio intro)
- **Frames**: 8 (play once, intro do mini-desafio)
- **FPS**: 8
- **Descricao**: Ajusta microfone, limpa garganta (corpo treme), faz gesto de "comeca a gravar". LED de ON AIR acende com brilho maior. Fumaca intensifica.
- **Arquivo**: `monark-podcast-intro.png` (spritesheet 512x64, 8 frames)

---

## 6. Composicao de Layers

Para facilitar animacao modular, o sprite e montado em layers separadas:

```
Layer 5 (topo):  Fumaca das orelhas (animacao independente)
Layer 4:         Chapeu de pescador
Layer 3:         Cabeca + face (olhos, boca, barba)
Layer 2:         Torso + bracos + microfone
Layer 1:         Pernas + chinelos
Layer 0 (base):  Cadeira flutuante + sombra
```

### Vantagens
- Fumaca pode ser animada separadamente do corpo
- Chapeu pode "pular" da cabeca sem redesenhar tudo
- Boca pode ser animada via substituicao de sprite de 6x3px
- Cadeira bob pode ser offset separado sem mover o personagem

---

## 7. Integracao com Cenario do Limbo

### Posicao no Cenario
- Monark fica no CENTRO da tela de Game Over
- Cadeira flutuante a ~60% da altura da tela (levemente acima do centro)
- Abaixo da cadeira: VOID absoluto (`#0A0A0A`)
- Ao redor: particulas do Limbo (`#2A2A2A` alpha 40%)
- Luz do podcast ilumina ele por cima-esquerda (`#3D6B3A`)

### Iluminacao no Sprite
- Luz principal: cima-esquerda, tom `#3D6B3A` (podcast light)
- Highlight na testa, nariz, chapeu (lado esquerdo mais claro)
- Sombras: lado direito, cross-hatching diagonal 45deg
- Glow da cadeira: `#D47820` reflete de baixo pra cima nas pernas/bermuda
- Contraluz: borda fina `#D47820` no contorno direito (rim light da cadeira)

### Efeito de Flutuacao (Phaser 3)
```javascript
// Bob vertical da cadeira + Monark
this.tweens.add({
    targets: monarkSprite,
    y: monarkSprite.y + 2,
    duration: 2000,
    yoyo: true,
    repeat: -1,
    ease: 'Sine.easeInOut'
});
```

---

## 8. Detalhes de Pixel Art

### Tecnicas Obrigatorias
- **Contorno**: 2-3px no corpo principal, 3-4px na silhueta contra o void (contraste maximo no escuro)
- **Anti-aliasing manual**: 1px de cor intermediaria nas curvas do chapeu e ombros
- **Dithering**: Nas sombras do rosto, usar dithering checkerboard em vez de gradiente
- **Cross-hatching**: Sombras na camiseta e bermuda com linhas diagonais 1px, espacamento 2px
- **Textura de papel**: Overlay sutil no sprite final (noise 3-5%)
- **Linhas irregulares**: NUNCA linhas retas perfeitas — microvariacoes de 1px simulando traco manual

### Pontos de Atencao Especificos
1. **Olhos semicerrados**: A fenda dos olhos deve ser MUITO estreita (1-2px de abertura), mas a pupila negra visivel deve ser desproporcionalmente grande dentro dessa fenda
2. **Sorriso bobo**: Canto da boca curvado pra cima dos dois lados, dentes visíveis (2-3 retangulos brancos de 1px)
3. **Chapeu torto**: A aba esquerda mais baixa que a direita em 1px — assimetria proposital
4. **Fumaca**: Wisps de 3-4px de largura, forma organica (nao geometrica), dissipando de opaco para transparente
5. **Microfone**: O pop filter circular (grade redonda) e o elemento mais reconhecivel — priorizá-lo mesmo a 64px

---

## 9. Checklist de Producao

- [ ] Definir paleta final no editor (Aseprite/Photoshop)
- [ ] Desenhar sprite base S01 frame 0 (referencia para todos os outros)
- [ ] Validar proporcoes e deformidade (pupilas + fumaca) no frame base
- [ ] Criar layers separadas (cadeira, corpo, cabeca, chapeu, fumaca)
- [ ] Desenhar todos os frames de S01-S06
- [ ] Montar spritesheets horizontais (64px altura, N*64px largura)
- [ ] Aplicar overlay de textura de papel em todos os frames
- [ ] Testar animacoes em loop a 8-12fps
- [ ] Verificar legibilidade contra fundo `#0A0A0A` (void do Limbo)
- [ ] Verificar que fumaca das orelhas e visivel e nao se confunde com o chapeu
- [ ] Testar bob da cadeira com sprite em Phaser 3
- [ ] Exportar PNG-8 com transparencia
