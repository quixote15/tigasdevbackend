# Skin Variants — MONARK (O Rei do Limbo)

> Variacoes visuais do NPC Monark. Desbloqueaveis por progresso ou condicoes especiais.
> Todas as skins mantém a mesma hitbox, proporcoes e animation rig.
> A diferenca e VISUAL: roupas, cores, acessorios, efeitos.
> Sprites 64x64px.

---

## 1. Skin PADRAO — Rei do Limbo

### Descricao
O Monark default. Apresentador do Limbo dos Cancelados. Chapado, flutuando no void, podcast eterno.

### Elementos Visuais
| Elemento | Descricao | Cor Principal |
|---|---|---|
| Chapeu | Pescador/bucket hat verde musgo, torto | `#5A6B55` |
| Camiseta | Preta desbotada, largona, estampa ilegivel | `#2A2A2A` |
| Bermuda | Cinza suja, larga, bolsos salientes | `#4A4A44` |
| Chinelos | Havaianas verde escuro | `#2A5A3A` |
| Microfone | Condensador de podcast, LED ON AIR | `#5C5C5C` |
| Cadeira | Gamer preta com glow laranja | `#1A1A18` / `#D47820` |
| Deformidade | Pupilas dilatadas + fumaca verde-cinza das orelhas | `#0A0A0A` / `#6A8A6A` |

### Condicao de Desbloqueio
Disponivel desde o inicio (default).

---

## 2. Skin PODCAST OG — Era Flow (Pre-Cancelamento)

### Descricao
Monark na era "aurea" do Flow Podcast, antes do cancelamento. Mais arrumado (relativamente), cenario mais iluminado, microfone mais caro. Mas os olhos ja estavam chapados — nada mudou por dentro.

### Diferencas Visuais vs Padrao
| Elemento | Mudanca | Cor |
|---|---|---|
| Chapeu | MESMO chapeu de pescador, mas NOVO (cor mais viva, sem manchas) | `#6B8B6B` |
| Camiseta | Camiseta com logo "FLOW" visivel (4x3px, branco) | `#1A1A1A` (preto mais puro) |
| Bermuda | Calca jeans (sim, calca — era a "fase seria") | `#3A4A6A` (jeans azul escuro) |
| Chinelos | Tenis (era o auge, podia pagar tenis) | `#4A4A4A` (cinza) |
| Microfone | Dourado (mic caro, patrocinado) | `#C8A832` |
| Cadeira | Mesma gamer mas SEM glow (ainda nao estava no Limbo) | `#1A1A18` (sem `#D47820`) |
| Background | Nao e void — e um estudio escuro com parede atras | `#2A2A2A` parede |
| Deformidade | Pupilas dilatadas iguais, mas SEM fumaca nas orelhas (fumaca so no Limbo) | `#0A0A0A` |

### Efeito Especial
- Logo "FLOW" no peito da camiseta pulsa levemente (1px de brilho a cada 3s)
- Sem fumaca nas orelhas (overlay A07 desativado)
- Sem glow na cadeira (A08 bob mantido, mas sem laranja)

### Condicao de Desbloqueio
Morrer 10 vezes no jogo (Monark comenta: "Mano, voce ja morreu tantas vezes que eu vou te mostrar como era no inicio...")

---

## 3. Skin LIMBO SUPREMO — Rei Coroado

### Descricao
Monark ascendeu. Nao e mais apenas apresentador do Limbo — ele E o Limbo. Coroa no lugar do chapeu, toga eterea, trono no lugar da cadeira de podcast. O cancelamento o tornou uma entidade cosmica da irrelevancia.

### Diferencas Visuais vs Padrao
| Elemento | Mudanca | Cor |
|---|---|---|
| Chapeu | SUBSTITUIDO por coroa torta feita de microfones quebrados | `#C8A832` (dourado sujo) + `#5C5C5C` (metal mic) |
| Camiseta | SUBSTITUIDA por toga/manto rasgado e transparente | `#2A0A2A` (roxo muito escuro) alpha 70% |
| Bermuda | Desaparece sob a toga (so contorno das pernas visivel) | `#2A0A2A` |
| Chinelos | Pes descalcos, flutuando, dedos crispados | Pele `#D4956A` |
| Microfone | 3 microfones flutuando ao redor (em orbita) | `#5C5C5C` com glow `#3D6B3A` |
| Cadeira | SUBSTITUIDA por trono de ossos feitos de cabos de audio | `#E8D8C8` (osso) + `#1A1A18` (cabos) |
| Background | Void MAIS profundo, particulas VERMELHAS em vez de cinza | `#050505` void, `#4A0A0A` particulas |
| Deformidade | Pupilas BRILHAM verde no escuro. Fumaca sai dos olhos TAMBEM. | Pupilas `#3D6B3A`, fumaca olhos + orelhas |

### Efeitos Especiais
- Microfones orbitam lentamente (rotacao continua, 1 ciclo a cada 6s)
- Toga ondula como se houvesse vento no void (2 frames alternantes)
- Pupilas emitem luz verde (pointlight pequeno no Phaser)
- Fumaca sai dos OLHOS E ORELHAS (overlay expandido)
- Trono de ossos/cabos pulsa com heartbeat lento (1 ciclo a cada 4s)

### Condicao de Desbloqueio
Completar o jogo inteiro (todos os stages) + morrer na ultima fase. Monark comenta: "Mano, voce morreu no FINAL? Ta, agora voce merece ver minha forma verdadeira."

---

## 4. Skin MONARK DE FERIAS — Pescador Literal

### Descricao
Monark levou o chapeu de pescador a serio. Esta literalmente pescando no void do Limbo. Vara de pescar em vez de microfone, balde no lugar da mesa de podcast, sentado numa caixa termica em vez de cadeira gamer.

### Diferencas Visuais vs Padrao
| Elemento | Mudanca | Cor |
|---|---|---|
| Chapeu | MESMO chapeu, mas com MAIS anzois (3-4 na aba) | `#5A6B55` + `#C8A832` anzois |
| Camiseta | Camisa havaiana aberta sobre camiseta regata | `#D47820` flores / `#E8E0D0` regata |
| Bermuda | Bermuda de praia, mais curta, estampa tropical | `#2A5A3A` com flores `#D47820` |
| Chinelos | Descalco (pes na caixa termica) | Pele `#D4956A` |
| Microfone | SUBSTITUIDO por vara de pescar artesanal | `#6B4423` (madeira) + `#8A8A8A` (linha) |
| Cadeira | SUBSTITUIDA por caixa termica de isopor | `#D0E0D0` (branco esverdeado) |
| Acessorio novo | Balde com "cancelados" (silhuetas de peixinhos) ao lado | `#5C5C5C` balde, `#2A2A2A` peixinhos |
| Deformidade | Mesma (pupilas + fumaca), mais oculos de sol na testa (nao cobrindo os olhos) | `#1A1A18` oculos |

### Efeitos Especiais
- Linha de pescar balanca levemente (tween pendular)
- Ocasionalmente "fisga algo" no void (puxao da vara, 1 vez a cada 10s)
- Caixa termica nao flutua tao suavemente — tem microtremor (ela nao e magica, e isopor)
- Quando fala, ajusta a vara pra nao perder a "pesca"

### Condicao de Desbloqueio
Morrer 5 vezes sem usar nenhuma arma (morte pacifista). Monark comenta: "Mano, voce veio pro Limbo de maos vazias? Senta aqui, vamo pescar."

---

## 5. Skin CANCELADO EM CHAMAS — Inferno Podcast

### Descricao
Monark pegou fogo. Literalmente. A cadeira esta em chamas, a camiseta esta queimando, o chapeu derrete. Mas ele continua falando no podcast como se nada tivesse acontecendo. A piada: o cancelamento e tao total que ate no Limbo ele queima, mas nao se importa.

### Diferencas Visuais vs Padrao
| Elemento | Mudanca | Cor |
|---|---|---|
| Chapeu | Derretendo, forma deformada, borda ondulada | `#4A3A28` (verde queimado para marrom) |
| Camiseta | Buracos de queimadura, bordas carbonizadas | `#1A1A18` com `#8B2020` bordas |
| Bermuda | Metade queimada, metade intacta | `#4A4A44` metade + `#2A1A1A` queimado |
| Chinelos | Derretendo (deformados, formato errado) | `#2A2020` |
| Microfone | Intacto (a unica coisa que NAO queima — a ironia) | `#5C5C5C` (normal) |
| Cadeira | Em CHAMAS — fogo animado ao redor | `#1A1A18` + `#CC5500` / `#FFAA00` chamas |
| Deformidade | Pupilas + fumaca, MAS a fumaca agora e PRETA (combustao) | Fumaca `#2A2A2A` |
| Acessorio novo | Chamas (overlay animado, 4 frames) | `#CC5500` base, `#FFAA00` ponta |

### Efeitos Especiais
- Chamas na cadeira: overlay animado de 4 frames a 10fps (rapido, flickering)
- Particulas de fagulha subindo (emitter, 2-3 particulas/s, `#FFAA00`, vida curta)
- Chapeu DERRETENDO progressivamente ao longo da conversa (a cada 30s perde 1px de forma)
- Fumaca preta em vez de verde (A07 recolorido)
- Expressao do Monark: IDENTICA ao normal (nao se importa que esta pegando fogo)

### Condicao de Desbloqueio
Morrer por fogo/explosao 3 vezes. Monark comenta: "Mano, voce veio carbonizado? Pera, eu tambem to pegando fogo. Que dia."

---

## 6. Skin ENTREVISTADOR DO VOID — Talk Show Cosmico

### Descricao
Monark transforma o Limbo num late night show. Terno (mal vestido), mesa de entrevistador, caneca de cafe no lugar do microfone de podcast, aplausos fantasmagoricos. Trata cada jogador morto como convidado de talk show.

### Diferencas Visuais vs Padrao
| Elemento | Mudanca | Cor |
|---|---|---|
| Chapeu | REMOVIDO (cabelo a mostra — bagunca total, amassado pelo chapeu) | Cabelo `#3A2A1A` |
| Camiseta | SUBSTITUIDA por terno mal vestido (gravata torta, camisa pra fora) | Terno `#2A2A3A`, gravata `#8B2020`, camisa `#E8E0D0` |
| Bermuda | Calca social (mas muito curta, mostrando meia branca) | `#2A2A3A` calca + `#E8E0D0` meia |
| Chinelos | Sapato social com meias brancas visiveis | `#1A1A18` sapato |
| Microfone | SUBSTITUIDO por caneca de cafe com vapor saindo | `#E8D8C8` caneca + `#6A8A6A` vapor |
| Cadeira | SUBSTITUIDA por poltrona de entrevistador (estilo talk show) | `#8B2020` estofado + `#6B4423` madeira |
| Acessorio novo | Mesa baixa ao lado com papeis bagunçados | `#6B4423` mesa + `#F0E8D0` papeis |
| Background | Cortina atras (mal presa, rasgada) | `#2A0A2A` cortina |
| Deformidade | Pupilas dilatadas (mantidas) + fumaca SAI DA CANECA (nao das orelhas) | `#6A8A6A` vapor/fumaca |

### Efeitos Especiais
- Aplausos fantasmagoricos: particulas de maos transparentes (`#2A2A2A` alpha 20%) aparecem e somem nos cantos
- Cortina tremula (2 frames alternantes, bem sutil)
- Caneca de cafe tem vapor que substitui a fumaca das orelhas (A07 reposicionado)
- Papeis na mesa voam ocasionalmente (1 papel a cada 15s sai flutuando)
- LED de ON AIR substituido por placa "NO AR" pixelada em vermelho

### Condicao de Desbloqueio
Assistir TODOS os dialogos do Monark sem pular (nenhum skip). Monark comenta: "Mano, voce ouviu TUDO que eu falei? Ninguem faz isso. Voce merece o show completo."

---

## 7. Tabela Comparativa de Skins

| Skin | Chapeu | Roupa | Microfone | Cadeira | Fumaca | Desbloqueio |
|---|---|---|---|---|---|---|
| **Padrao** | Pescador verde | Camiseta preta + bermuda | Podcast | Gamer flutuante | Orelhas (verde-cinza) | Default |
| **Podcast OG** | Pescador novo | Camiseta Flow + calca | Dourado | Gamer sem glow | Nenhuma | 10 mortes |
| **Limbo Supremo** | Coroa de microfones | Toga eterea | 3 orbitando | Trono de ossos | Olhos + orelhas (verde brilhante) | Completar jogo + morrer |
| **De Ferias** | Pescador com anzois | Havaiana + bermuda praia | Vara de pescar | Caixa termica | Orelhas + oculos na testa | 5 mortes pacifistas |
| **Em Chamas** | Derretendo | Tudo queimando | Intacto (ironia) | Em chamas | Preta (combustao) | 3 mortes por fogo |
| **Talk Show** | Removido (cabelo) | Terno mal vestido | Caneca de cafe | Poltrona talk show | Da caneca | Ver todos dialogos |

---

## 8. Regras Globais de Skins

### O Que NUNCA Muda
1. **Pupilas dilatadas** — TODAS as skins mantém pupilas enormes (e a identidade visual)
2. **Sorriso bobo** — TODAS as skins mantém o sorriso chapado
3. **Proporcoes** — Cabeca 1.5x, torso 2x, pernas 1.5x (hitbox identica)
4. **Posicao sentada** — SEMPRE sentado (nunca em pe)
5. **Flutuacao** — SEMPRE flutuando no void (exceto OG que tem parede atras)
6. **Contorno grosso** — 2-4px irregulares em TODAS as skins

### O Que PODE Mudar
1. Roupas e acessorios
2. Cor/forma da fumaca (mas ALGUMA fumaca sempre existe, exceto OG)
3. Objeto na mao (microfone, vara, caneca)
4. Tipo de assento (cadeira, trono, caixa, poltrona)
5. Efeitos adicionais (chamas, orbita, aplausos)
6. Cor do glow sob o assento

### Impacto no Gameplay
NENHUM. Skins sao puramente cosmeticas. O Monark funciona identicamente em qualquer skin. Os bordoes, precos da loja, e mecanicas de revive sao iguais.

---

## 9. Checklist de Producao por Skin

Para CADA skin, produzir:
- [ ] Frame base (64x64) mostrando visual completo
- [ ] Spritesheet de Idle (4 frames)
- [ ] Spritesheet de Talking (6 frames)
- [ ] Spritesheet de Offering (4 frames)
- [ ] Spritesheet de Happy (6 frames)
- [ ] Spritesheet de Shrug (4 frames)
- [ ] Spritesheet de Podcast Intro (8 frames) — adaptar pro contexto da skin
- [ ] Overlay de fumaca/efeito (6 frames)
- [ ] Overlay de LED/placa (2 frames)
- [ ] Testar todas as animacoes com a skin ativa
- [ ] Verificar legibilidade contra void escuro

### Prioridade de Producao
1. **PADRAO** (obrigatorio para MVP)
2. **PODCAST OG** (narrativamente importante, mostra backstory)
3. **LIMBO SUPREMO** (recompensa endgame, impacto visual alto)
4. **EM CHAMAS** (mais simples de produzir — mesma base + overlay de fogo)
5. **DE FERIAS** (humor)
6. **TALK SHOW** (mais complexo — muitos elementos novos)
