# Sprite Spec — ARTHUR DO VAL / MAMAE FALEI (Co-Apresentador do Limbo)

> NPC do Game Over (parceiro do Monark no Limbo dos Cancelados).
> Enquanto Monark filosofa, Arthur RECLAMA e tenta fazer "denuncias".
> Sprites 64x64px, PNG com transparencia.
> Estilo: Andre Guedes — grotesco, underground comix, Robert Crumb + humor politico BR.

---

## 1. Tipo de Personagem

| Parametro | Valor |
|---|---|
| **Tipo** | NPC (nao-jogavel, nao-combatente) |
| **Contexto** | Tela de Game Over / Co-apresentador do Limbo |
| **Interacao** | Dialogo complementar ao Monark + dicas (confusas) |
| **Sprite size** | 64x64px |
| **Perspectiva** | Top-down levemente isometrica (consistente com o jogo) |
| **Formato** | PNG-8 com transparencia |
| **Proporcoes** | Cabeca 1.5x, torso 2x, pernas 1.5x (~5 cabecas total, atarracado) |
| **Contorno** | Linhas grossas 2-4px, irregulares, simulando mao humana |
| **Posicao relativa** | A DIREITA do Monark, ligeiramente atras e abaixo (co-apresentador, nao estrela) |

---

## 2. Anatomia e Deformidade

### Proporcoes Gerais (dentro do 64x64)
```
┌────────────────────────────────────────┐
│  CABELO DESPENTEADO (topo, espalha)    │  ~6px altura (bagunca pra todos os lados)
│  ┌──────────────────────────────┐      │
│  │  CABECA (1.5x proporcional)  │      │  ~14px altura
│  │  Expressao de "OPS" eterna   │      │
│  │  BOCA QUE NAO PARA           │      │
│  │  Celular GRUDADO na orelha   │      │
│  └──────────────────────────────┘      │
│         │  PESCOCO tenso │             │
│  ┌──────────────────────────────┐      │
│  │  TORSO (2x, sentado)        │      │  ~18px altura
│  │  Camisa social amarrotada    │      │
│  │  Mangas arregacadas          │      │
│  │  Maos gesticulando SEMPRE    │      │
│  └──────────────────────────────┘      │
│  ┌──────────────────────────────┐      │
│  │  PERNAS (1.5x, sentado)     │      │  ~12px altura
│  │  Calca social amassada       │      │
│  │  Sapatos batendo no chao     │      │
│  │  (cadeira MENOR que Monark)  │      │
│  └──────────────────────────────┘      │
│  ═══ CADEIRA DE PODCAST (menor) ═══   │  ~8px (flutuante, mas instavel)
│       (balanca mais que a do Monark)   │
└────────────────────────────────────────┘
```

### Deformidade Principal: BOCA QUE NAO PARA + CELULAR GRUDADO NA ORELHA
- **Boca**: A boca do Arthur esta SEMPRE em movimento. Mesmo no idle, os labios tremem, como se ele estivesse murmurando ou prestes a falar. A boca e proporcionalmente GRANDE demais para o rosto — ocupa 40% da area facial inferior. Dentes a mostra permanentemente (boca semi-aberta default).
- **Celular**: Um smartphone esta FISICAMENTE GRUDADO na orelha direita. Nao e que ele segura — o celular E PARTE DELE agora. Fios de pele/carne conectam o celular a orelha (body horror leve). A tela do celular brilha (`#4A9ACA` azul tela). Ele esta SEMPRE gravando ou sendo gravado — nunca se sabe qual.
- **Efeito combinado**: Da a impressao de alguem que nao consegue parar de falar E nao consegue largar o celular — ambos se tornaram extensoes do corpo. Dupla maldicao do Limbo.

### Elementos Faciais
| Elemento | Descricao | Pixels Aproximados |
|---|---|---|
| **Olhos** | ARREGALADOS, abertos demais (oposto do Monark). Expressao permanente de "fui pego". Iris pequenas com muito branco visivel. | 4x3px cada, iris 2x2px |
| **Sobrancelhas** | Erguidas PERMANENTEMENTE em arcos de surpresa/indignacao | 5x2px cada, curvadas |
| **Nariz** | Afilado, levemente empinado ("nariz em pe") | 3x4px |
| **Boca** | GRANDE, semi-aberta, dentes a mostra, labios SEMPRE tremendo (1px oscilacao) | 8x4px (enorme!) |
| **Queixo** | Proeminente, projetado pra frente | 6x2px |
| **Orelhas** | Direita coberta pelo celular grudado. Esquerda normal mas vermelha (de vergonha?) | 2x3px visivel (esquerda) |
| **Cabelo** | Despenteado TOTAL — mechas pra todos os lados, como quem acabou de ser pego no flagra | 16x6px (area irregular acima da cabeca) |

---

## 3. Vestimenta e Acessorios

### Cabelo Despenteado
- **Tipo**: Cabelo castanho medio, medio comprimento, TOTALMENTE bagunçado
- **Cor**: `#5A4030` base, `#3A2A1A` mechas escuras, `#7A6050` highlights
- **Posicao**: Mechas apontando pra cima, pros lados, uma caindo na testa
- **Detalhe**: Parece que ele acabou de acordar, ou de correr, ou de ser pego fazendo algo errado. Sempre.
- **Tamanho no sprite**: ~16x6px (extrapola os limites da cabeca em 2-3px pra cada lado)

### Camisa Social Amarrotada
- **Tipo**: Camisa social manga longa, botoes, colarinho — mas COMPLETAMENTE amarrotada
- **Cor**: `#D8D0C0` (branco sujo/creme) com sombras `#B0A890`
- **Mangas**: Arregacadas ate o cotovelo (um lado mais que o outro — assimetrico)
- **Botoes**: 2-3 botoes abertos no colarinho (desalinhado)
- **Detalhe**: Manchas de suor nas axilas (`#C8C0A8`), camisa pra fora da calca do lado direito
- **Tamanho**: Ocupa todo o torso area

### Calca Social
- **Tipo**: Calca social que ja foi bonita, agora amassada e com vincos errados
- **Cor**: `#3A3A3A` (cinza escuro) com vincos `#2A2A2A`
- **Detalhe**: Um cinto `#5A3A1A` (couro marrom) com fivela `#C8A832` levemente torto
- **Barra**: Dobrada errado (um lado mais alto que outro)

### Sapatos Sociais
- **Tipo**: Sapatos sociais pretos que ja viram dias melhores
- **Cor**: `#1A1A18` (preto desgastado)
- **Detalhe**: Um com cadarco desamarrado (1px branco pendendo)

### Microfone de Podcast (MENOR que o do Monark)
- **Tipo**: Mesmo tipo de microfone condensador, mas VISIVELMENTE MENOR
- **Cor**: `#5C5C5C` corpo, `#7A7A7A` grade
- **Posicao**: A direita dele, braco articulado MAIS CURTO que o do Monark
- **Detalhe**: SEM LED de ON AIR (ele e co-apresentador, nao tem luz propria)
- **Tamanho no sprite**: ~5x8px (menor que os 6x10px do Monark)

### Celular Grudado na Orelha (DEFORMIDADE)
- **Tipo**: Smartphone moderno, mas FUSIONADO com a orelha
- **Cor**: `#1A1A18` corpo do celular, `#4A9ACA` tela brilhando
- **Posicao**: Lado direito da cabeca, angulo de "falando no telefone"
- **Detalhe**: 2-3 fios de pele/carne (`#D4956A` com `#CC6666`) conectando o celular a orelha (body horror)
- **Tela**: Brilha com luz azul que ilumina levemente o lado direito do rosto
- **Tamanho no sprite**: ~4x6px

### Cadeira de Podcast (MENOR e INSTAVEL)
- **Tipo**: Cadeira de escritorio basica (nao gamer — ele e CO-apresentador)
- **Cor**: `#3A3A3A` (cinza escuro, sem glow — sem o `#D47820` do Monark)
- **Posicao**: Ligeiramente MAIS BAIXA que a cadeira do Monark (hierarquia visual)
- **Flutuacao**: Mais instavel — balanca 1-2px lateralmente alem do bob vertical
- **Tamanho no sprite**: ~14x8px (menor que a do Monark)

---

## 4. Paleta de Cores

| Elemento | Hex | Notas |
|---|---|---|
| **Pele** | `#D4956A` | Tom quente (mesma base que Monark para consistencia) |
| **Pele sombra** | `#B07848` | Cross-hatching nas sombras |
| **Pele rubor** | `#CC7777` | Bochechas levemente coradas (vergonha/constrangimento permanente) |
| **Cabelo** | `#5A4030` | Castanho medio |
| **Cabelo sombra** | `#3A2A1A` | Mechas escuras |
| **Cabelo highlight** | `#7A6050` | Mechas claras (descoloridas?) |
| **Camisa** | `#D8D0C0` | Branco sujo/creme |
| **Camisa sombra** | `#B0A890` | Dobras e amarrotamento |
| **Camisa suor** | `#C8C0A8` | Manchas nas axilas |
| **Calca** | `#3A3A3A` | Cinza escuro |
| **Cinto** | `#5A3A1A` | Couro marrom |
| **Fivela** | `#C8A832` | Dourado |
| **Sapatos** | `#1A1A18` | Preto desgastado |
| **Celular corpo** | `#1A1A18` | Preto |
| **Celular tela** | `#4A9ACA` | Azul tela brilhante |
| **Celular-carne** | `#CC6666` | Fios de pele/body horror |
| **Boca interior** | `#4A1A1A` | Vermelho escuro quando aberta |
| **Dentes** | `#E8E0D0` | Branco sujo |
| **Olho branco** | `#F0E8E0` | Branco levemente amarelado |
| **Iris** | `#5A4030` | Castanho, pequena |
| **Sobrancelha** | `#3A2A1A` | Escuras, expressivas |
| **Microfone** | `#5C5C5C` | Metal escuro (sem brilho — subordinado) |
| **Cadeira** | `#3A3A3A` | Cinza escuro simples |
| **Contorno geral** | `#1A1A18` | Linhas 2-4px irregulares |

---

## 5. Sprite States (NPC)

Como NPC co-apresentador, Arthur tem animacoes que COMPLEMENTAM as do Monark. Ele reage ao que o Monark faz/fala.

### S01 — IDLE (Inquieto na Cadeira)
- **Frames**: 6 (loop — mais frames que Monark porque ele NAO PARA quieto)
- **FPS**: 6 (mais rapido que o idle do Monark — ele e nervoso)
- **Descricao**: Sentado na cadeira menor, mexendo-se constantemente. Boca murmurando (labios tremem). Mao alternando entre gesticular e cocar a cabeca. Celular brilha na orelha. Cadeira balanca.
- **Variacao entre frames**: Boca tremula, mao muda de posicao, corpo inclina 1px pra frente e pra tras, cabelo tem 1 mecha que muda de direcao.
- **Arquivo**: `arthur-idle.png` (spritesheet 384x64, 6 frames)

### S02 — RECLAMANDO (Dialogo Ativo)
- **Frames**: 8 (loop durante dialogo dele)
- **FPS**: 10 (RAPIDO — ele fala rapido, gesticula freneticamente)
- **Descricao**: Boca ENORME aberta, bracos voando pra todo lado, corpo inclinado pra frente agressivamente, sobrancelhas no maximo de indignacao. Cadeira balanca perigosamente.
- **Variacao entre frames**: Boca abre MAX → fecha → abre → fecha (ciclo rapido). Bracos alternam entre apontar pra cima, pro lado, e bater na coxa. Cabelo treme.
- **Arquivo**: `arthur-ranting.png` (spritesheet 512x64, 8 frames)

### S03 — "TIRADO DE CONTEXTO" (Reacao Defensiva)
- **Frames**: 6 (play once quando Monark diz algo e Arthur reage)
- **FPS**: 8
- **Descricao**: Maos pra frente em gesto de PARA (palmas abertas). Olhos MAIS arregalados que o normal. Boca forma O de protesto. Corpo joga pra tras na cadeira. Celular brilha mais forte (alguem gravou?).
- **Arquivo**: `arthur-context.png` (spritesheet 384x64, 6 frames)

### S04 — DANDO DICAS (Skill "Denuncia do Limbo")
- **Frames**: 6 (loop durante dicas)
- **FPS**: 8
- **Descricao**: Inclina-se pro lado como quem conta um segredo. Uma mao ao lado da boca (gesto de sussurro). Olhos olham pro lado (paranoia). Celular na orelha brilha VERMELHO em vez de azul (informacao "quente"?).
- **Arquivo**: `arthur-whispering.png` (spritesheet 384x64, 6 frames)

### S05 — INTERROMPENDO (Ele corta o Monark)
- **Frames**: 4 (play once, transicao rapida)
- **FPS**: 12 (MUITO rapido — interrupcao subita)
- **Descricao**: Pula na cadeira (sobe 3px). Mao estende-se na direcao do Monark. Boca ABERTA no maximo. Corpo todo inclinado pra esquerda (direcao do Monark). Cabelo explode pra cima.
- **Arquivo**: `arthur-interrupt.png` (spritesheet 256x64, 4 frames)

### S06 — DERROTADO (Aceita que foi cancelado)
- **Frames**: 4 (play once, momento raro)
- **FPS**: 4 (lento, abatido)
- **Descricao**: Ombros caem. Cabeca abaixa. Mao passa pelo cabelo (desespero). Boca fecha pela UNICA VEZ. Celular escurece (desligou?). Olhos ficam normais por um instante (nao arregalados).
- **Arquivo**: `arthur-defeated.png` (spritesheet 256x64, 4 frames)

---

## 6. Composicao de Layers

```
Layer 5 (topo):  Cabelo despenteado (mechas que se movem independentemente)
Layer 4:         Celular grudado na orelha + brilho da tela
Layer 3:         Cabeca + face (olhos, boca, sobrancelhas)
Layer 2:         Torso + bracos + camisa amarrotada
Layer 1:         Pernas + calca + sapatos
Layer 0 (base):  Cadeira de escritorio + sombra
```

### Vantagens
- Boca pode ser animada via substituicao independente (frame dentro do frame)
- Cabelo pode tremular sem redesenhar toda a cabeca
- Celular pode mudar cor da tela (azul/vermelho/escuro) via swap de 4x6px
- Bracos podem gesticular sem alterar torso

---

## 7. Posicionamento no Cenario do Limbo

### Posicao Relativa ao Monark
```
┌───────────────────────────────────────────────────────┐
│                     VOID DO LIMBO                     │
│                                                       │
│                                                       │
│          ┌─────────┐        ┌─────────┐               │
│          │ MONARK  │        │ ARTHUR  │               │
│          │ (centro │        │ (direita│               │
│          │  cima)  │        │  baixo) │               │
│          │ 64x64   │        │ 64x64   │               │
│          │  ★ mic  │        │  mic ☆  │               │
│          └────┬────┘        └────┬────┘               │
│               │                  │                    │
│          ═══CADEIRA═══     ═══CADEIRA═══              │
│          (grande,glow)     (menor,plain)              │
│                                                       │
│                   VOID INFINITO                       │
└───────────────────────────────────────────────────────┘

★ = Microfone grande com ON AIR
☆ = Microfone menor sem ON AIR
```

- Arthur esta ~48px a direita e ~16px abaixo do Monark (hierarquia visual)
- Cadeira do Arthur e MENOR e flutua MAIS BAIXO que a do Monark
- Microfone do Arthur esta entre os dois (compartilhado visualmente)
- Quando Arthur gesticula, as maos podem "invadir" o espaco do Monark em 2-3px

### Iluminacao no Sprite
- Luz principal: MESMA do Monark (podcast light `#3D6B3A` cima-esquerda)
- MAS Arthur recebe MENOS luz (esta mais pro lado — penumbra parcial)
- Celular cria luz secundaria azul `#4A9ACA` no lado direito do rosto
- Cross-hatching mais denso no lado direito do corpo (sombra)
- SEM glow laranja da cadeira (cadeira dele e simples)

---

## 8. Detalhes de Pixel Art

### Tecnicas Obrigatorias
- **Contorno**: 2-3px no corpo, 3-4px na silhueta (contra void escuro)
- **Anti-aliasing manual**: 1px intermediaria nas curvas (cabelo, ombros)
- **Dithering**: Sombras da camisa branca usam dithering checkerboard (nao gradiente)
- **Cross-hatching**: Sombras na calca e lado escuro do corpo com linhas diagonais 1px, espacamento 2px
- **Textura de papel**: Overlay sutil no sprite final (noise 3-5%)
- **Linhas irregulares**: NUNCA retas perfeitas

### Pontos de Atencao Especificos
1. **Boca ENORME**: E o feature mais importante. Proporcionalmente grande demais. Mesmo fechada, ocupa mais espaco facial que olhos+nariz juntos.
2. **Olhos arregalados**: OPOSTO do Monark. Muito branco visivel. Iris pequenas perdidas no branco. Expressao de "fui pego".
3. **Celular grudado**: Os fios de carne conectando celular a orelha sao ESSENCIAIS para o body horror comico. 2-3 linhas de 1px em tom rosado.
4. **Camisa amarrotada**: Muitas linhas de dobra (1px mais escuro). A camisa deve parecer que nunca viu um ferro de passar.
5. **Cabelo explosivo**: Mechas em todas as direcoes. NAO e estiloso — e panico congelado em cabelo.
6. **Hierarquia visual**: Arthur SEMPRE parece subordinado ao Monark — cadeira menor, mic menor, posicao secundaria. A piada e que ele nao aceita isso.

### Contraste com Monark (IMPORTANTE)
| Aspecto | Monark | Arthur |
|---|---|---|
| Olhos | Semicerrados (chapado) | Arregalados (panico) |
| Boca | Sorriso bobo (relaxado) | Aberta/falando (frenetico) |
| Postura | Largado na cadeira (zen) | Tenso, inclinado pra frente (ansioso) |
| Movimentos | Lentos, minimos (4fps) | Rapidos, excessivos (6-10fps) |
| Cadeira | Gamer grande com glow | Escritorio simples sem glow |
| Mic | Grande com ON AIR | Menor sem ON AIR |
| Fumaca/Efeito | Fumaca eterea (orelhas) | Celular grudado (body horror) |
| Energia | Low energy, sereno | High energy, nervoso |

---

## 9. Checklist de Producao

- [ ] Definir paleta final no editor (Aseprite/Photoshop)
- [ ] Desenhar sprite base S01 frame 0 (referencia base)
- [ ] Validar proporcoes e deformidades (boca grande + celular grudado) no frame base
- [ ] Criar layers separadas (cadeira, corpo, cabeca, cabelo, celular)
- [ ] Validar POSICAO RELATIVA ao Monark (ambos na mesma cena)
- [ ] Desenhar todos os frames de S01-S06
- [ ] Montar spritesheets horizontais (64px altura)
- [ ] Aplicar overlay de textura de papel
- [ ] Testar animacoes em loop (especialmente idle a 6fps — deve parecer INQUIETO)
- [ ] Verificar legibilidade contra fundo `#0A0A0A` (void)
- [ ] Verificar contraste visual com Monark lado a lado
- [ ] Testar que gesticulacao do Arthur nao "invade" demais o sprite do Monark
- [ ] Exportar PNG-8 com transparencia
