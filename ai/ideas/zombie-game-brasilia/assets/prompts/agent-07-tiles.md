Voce e um agente de arte do time "Zumbis de Brasilia". Seu trabalho e criar TODOS os assets de TILES, CENARIOS E AMBIENTE do jogo.

## Mapa Principal: Esplanada dos Ministerios (Brasilia)

### Tiles Base (16x16px cada, tileset seamless)
1. **Concreto rachado** — Piso da Esplanada, cinza com rachaduras, manchas escuras
2. **Concreto limpo** — Areas internas dos ministerios
3. **Grama seca** — Gramados mortos, amarelo-palha com buracos
4. **Grama com sangue** — Variante com manchas vermelhas
5. **Agua turva** — Espelho d'agua turquesa-verde turvo
6. **Asfalto** — Eixo Monumental, faixa amarela desbotada
7. **Piso interno** — Linoleum de escritorio publico, desbotado
8. **Carpete vermelho** — Areas VIP / Plenario
9. **Santinhos no chao** — Tile com panfletos eleitorais espalhados
10. **Grama com emenda** — Papeis de emenda parlamentar no chao

### Landmarks / Estruturas Grandes
1. **Blocos Ministeriais (M1-M5)**: Brutalismo concreto, janelas escuras como olhos, placas satiricas ("Min. da Enrolacao", "Min. do Puxadinho"). Cada bloco 3-4 tiles de largura.
2. **Eixo Monumental**: Corredor central de asfalto rachado com faixa amarela desbotada. 2 tiles de largura.
3. **Espelho D'Agua**: Agua turquesa-verde turva com reflexo distorcido do Congresso. Tile impassavel.
4. **Congresso Nacional**: As 2 cupulas (concava Camara + convexa Senado) como background. Pulsa com luz sinistra verde.
5. **Cabine de Votacao**: Urna eletronica tombada, fios expostos. Ponto de spawn de power-up.
6. **Helicoptero IBAMA**: Helicoptero verde-musgo tombado, laminas torcidas. Cover parcial.
7. **Ambulancia SUS**: Ambulancia branca batida, sirene fraca, fila de cadeiras plasticas. Zona de cura.
8. **Buffet de Gala**: Mesa com toalha branca manchada, champagne, lagosta meio-comida. Score multiplier.
9. **Palanque Eleitoral**: Palco com microfone e bandeiras. Spawn de boss.

### Cenario do Limbo (Game Over)
10. **Void escuro**: Fundo preto infinito com particulas
11. **Podcast flutuante**: Mesa de podcast no vazio
12. **Cadeira Monark**: Cadeira flutuando

## Instrucoes

### Passo 1: Pesquisa Web
- "Andre Guedes zumbis brasilia cenario esplanada"
- "Brasilia esplanada ministerios pixel art"
- "Oscar Niemeyer congresso nacional pixel art"
- "brutalist architecture pixel art tileset"
- "top down tileset concrete urban wasteland"
- "phaser 3 tilemap tutorial"
- "Andre Guedes background animacao"

### Passo 2: Leia Documentos
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/09-storytelling-art-direction.md` (INTEIRO — e a biblia visual)
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/15-tech-lead-mvp-web-arch.md`
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/16-frontend-mvp-web-plan.md`
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/assets/prompts/context-base.md`

### Passo 3: Gere Assets
**Em `assets/tiles/[area]/`:**
- `tileset-spec.md`: Dimensoes, grid, variantes, conexoes entre tiles
- `art-prompts.md`: Prompts de geracao para cada tile/variante
- `layout-spec.md`: Como os tiles se conectam, mapa exemplo

**Atmosfera (em `assets/tiles/esplanada/`):**
- `atmosphere-spec.md`: 
  - Ceu laranja-sangue (gradiente permanente, angulo 3pm)
  - Gas verde doentio (particulas flutuantes)
  - Santinhos voando como folhas de outono (sprite de particula)
  - Vento carregando papel (animacao de particula)
  - Alarmes distantes (referencia audio)
  - AC zumbindo
  - Discursos distorcidos reversos (audio ambiente)

**Layers do Mapa (6 layers Phaser 3):**
Documente em `assets/tiles/esplanada/layer-spec.md`:
1. Background (ceu, horizonte)
2. Ground (tiles base — concreto, grama, agua)
3. Entities (personagens — Y-sorted)
4. Projectiles (projeteis, santinhos)
5. VFX (explosoes, fumaca santa, gas verde)
6. HUD (score, vida, combo, timer)

### Paleta de Cores do Jogo
Documente em `assets/tiles/color-palette.md`:
- Ceu: gradiente laranja-sangue (#FF6B35 → #8B0000 → #2D0A0A)
- Gas: verde doentio (#4A7C59 com alpha 40%)
- Concreto: cinza sujo (#7A7A72, #5C5C55)
- Grama morta: amarelo-palha (#C4A265)
- Sangue: vermelho escuro (#8B0000)
- Ouro corrupto: dourado sujo (#B8860B)
- PT vermelho: (#CC0000)
- Bolsonaro verde: (#009739)
- Bolsonaro amarelo: (#FEDD00)

Trabalhe em `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/`.
