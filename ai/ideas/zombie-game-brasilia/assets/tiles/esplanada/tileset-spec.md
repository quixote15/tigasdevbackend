# Tileset Spec — Esplanada dos Ministerios

> Mapa principal (MVP). Arena de sobrevivencia top-down.
> Todos os tiles: 16x16px, PNG com transparencia, seamless.
> Tileset unico para Phaser 3: max 512x512px (32x32 tiles = 1024 tiles possiveis).

---

## 1. Dimensoes e Grid

| Parametro | Valor |
|---|---|
| **Tile size** | 16x16 pixels |
| **Tileset image** | 512x512px (max) |
| **Tiles por linha** | 32 |
| **Total de tiles possiveis** | 1024 (32x32) |
| **Tiles planejados** | ~120 tiles (10 base + variantes + landmarks + decoracoes) |
| **Formato** | PNG-8 com transparencia |
| **Ferramenta de edicao** | Tiled Map Editor (export JSON para Phaser 3) |
| **Perspectiva** | Top-down levemente isometrica (Y-sorting em entidades) |

---

## 2. Tiles Base (10 Tipos Fundamentais)

### T01 — Concreto Rachado
- **Funcao:** Piso principal da Esplanada
- **Cores:** `#8A8580` base, `#5C5C55` rachaduras, `#3A3530` manchas
- **Variantes:** 4 (rachaduras em direcoes diferentes para evitar repeticao)
- **Propriedades Phaser:** walkable, no collision
- **Detalhes:** Rachaduras finas (1px) em padrao irregular. Manchas escuras sugerindo sujeira/tempo. Textura de papel overlay.
- **IDs no tileset:** T01a, T01b, T01c, T01d

### T02 — Concreto Limpo
- **Funcao:** Areas internas dos ministerios
- **Cores:** `#8A8580` base mais uniforme, `#A09888` highlights
- **Variantes:** 2 (com e sem rodape/borda)
- **Propriedades Phaser:** walkable, no collision
- **Detalhes:** Mais uniforme que T01 mas NAO perfeito. Leve textura de desgaste.
- **IDs:** T02a, T02b

### T03 — Grama Seca
- **Funcao:** Gramados mortos da Esplanada
- **Cores:** `#C4A265` base, `#7A8830` tufos, `#5C5C55` buracos
- **Variantes:** 4 (densidade de grama diferente, com/sem buracos)
- **Propriedades Phaser:** walkable, speed_modifier: 0.85 (terreno lento)
- **Detalhes:** Grama amarelo-palha em tufos irregulares. Buracos de obra inacabada. Irrigadores quebrados (sprite decorativo).
- **IDs:** T03a, T03b, T03c, T03d

### T04 — Grama com Sangue
- **Funcao:** Variante da grama com manchas de sangue-tinta
- **Cores:** `#C4A265` base + `#8B0000` manchas
- **Variantes:** 3 (manchas em posicoes diferentes)
- **Propriedades Phaser:** walkable, speed_modifier: 0.85
- **Detalhes:** Sangue estilizado como TINTA — amorfas, gotas exageradas, NAO realista. Estilo Robert Crumb.
- **IDs:** T04a, T04b, T04c

### T05 — Agua Turva
- **Funcao:** Espelho d'agua (divisor de mapa impassavel)
- **Cores:** `#2A3D2E` base, `#3D6B3A` reflexo, `#1A1A18` profundidade
- **Variantes:** 3 (centro, borda norte, borda sul) + 1 animado (ondulacao)
- **Propriedades Phaser:** NOT walkable, collision: true, kills_on_contact: true (zumbis caem e afundam)
- **Detalhes:** Agua opaca e esverdeada. Reflexo distorcido do Congresso (sprite separado). Peixes mortos como sprite decorativo.
- **Animacao:** 4 frames, 4fps — ondulacao lenta e inquietante
- **IDs:** T05a (centro), T05b (borda-N), T05c (borda-S), T05d (borda-E), T05e (borda-W), T05f-i (cantos)

### T06 — Asfalto
- **Funcao:** Eixo Monumental, ruas
- **Cores:** `#3A3530` base, `#B8A030` faixa amarela desbotada
- **Variantes:** 4 (liso, com faixa horizontal, com faixa vertical, rachado)
- **Propriedades Phaser:** walkable, no collision, speed_modifier: 1.0 (terreno rapido)
- **Detalhes:** Faixa amarela desbotada (1-2px). Rachaduras finas. Postes de luz como sprite decorativo separado.
- **IDs:** T06a (liso), T06b (faixa-H), T06c (faixa-V), T06d (rachado)

### T07 — Piso Interno
- **Funcao:** Linoleum de escritorio publico nos ministerios
- **Cores:** `#A09888` base, `#8A8580` desgaste
- **Variantes:** 2 (desbotado, muito desbotado)
- **Propriedades Phaser:** walkable, no collision
- **Detalhes:** Textura levemente quadriculada (grid 4x4 dentro do tile). Marcas de sapato.
- **IDs:** T07a, T07b

### T08 — Carpete Vermelho
- **Funcao:** Areas VIP, plenario, corredores de poder
- **Cores:** `#8B2020` base, `#6B1515` sombra, `#A03030` highlight
- **Variantes:** 2 (limpo, com manchas)
- **Propriedades Phaser:** walkable, no collision
- **Detalhes:** Textura de tecido (hachuras diagonais finas). Manchas indeterminadas.
- **IDs:** T08a, T08b

### T09 — Santinhos no Chao
- **Funcao:** Tile decorativo com panfletos eleitorais espalhados
- **Cores:** `#F0E8D0` papeis sobre qualquer tile base
- **Variantes:** 3 (poucos papeis, muitos papeis, amontoado)
- **Propriedades Phaser:** walkable, no collision (overlay decorativo)
- **Detalhes:** Retangulos pequenos (3x4px) em angulos aleatorios representando santinhos. Cores dos papeis variadas mas sujas. Alguns com "VOTE" legivel em 1px.
- **IDs:** T09a, T09b, T09c

### T10 — Grama com Emenda
- **Funcao:** Papeis de emenda parlamentar no gramado
- **Cores:** `#E8D8B0` papeis sobre `#C4A265` grama
- **Variantes:** 2 (papeis espalhados, papeis amontoados)
- **Propriedades Phaser:** walkable, speed_modifier: 0.85
- **Detalhes:** Papeis maiores que santinhos (4x5px). Alguns com selo dourado (`#C8A832`) de 1px. Texto ilegivel em linhas finas.
- **IDs:** T10a, T10b

---

## 3. Tiles de Transicao (Bordas)

Para cada par de tiles adjacentes, criar tiles de transicao:

| Transicao | Tiles Necessarios | Prioridade |
|---|---|---|
| Concreto → Grama | 4 bordas + 4 cantos = 8 tiles | ALTA (mais comum) |
| Concreto → Asfalto | 4 bordas + 4 cantos = 8 tiles | ALTA |
| Grama → Agua | 4 bordas + 4 cantos = 8 tiles | ALTA |
| Asfalto → Grama | 4 bordas + 4 cantos = 8 tiles | MEDIA |
| Concreto → Agua | 4 bordas + 4 cantos = 8 tiles | MEDIA |
| Piso Interno → Concreto | 2 bordas (H, V) = 2 tiles | BAIXA |
| Carpete → Piso Interno | 2 bordas (H, V) = 2 tiles | BAIXA |

**Total de tiles de transicao:** ~46 tiles

### Metodo de Transicao
Usar **autotiling Wang tiles** (metodo Tiled Map Editor):
- Cada tile de transicao mistura os 2 terrenos com borda organica
- Bordas NAO sao linhas retas — sao irregulares, sujas, com detritos
- Cross-hatching na zona de transicao

---

## 4. Tiles de Decoracao (Layer Separada)

Sprites decorativos que vao SOBRE os tiles base:

| ID | Decoracao | Tamanho | Sobre Qual Tile |
|---|---|---|---|
| D01 | Poste de luz tombado | 16x32 (2 tiles alto) | Asfalto |
| D02 | Placa de campanha fincada | 16x16 | Grama |
| D03 | Irrigador quebrado | 16x16 | Grama |
| D04 | Banco de praca destruido | 32x16 (2 tiles largo) | Concreto/Grama |
| D05 | Lixeira transbordando | 16x16 | Concreto |
| D06 | Cone de transito | 16x16 | Asfalto |
| D07 | Crateras pequenas | 16x16 | Qualquer |
| D08 | Manchas de gas no chao | 16x16 (alpha) | Qualquer |
| D09 | Papeis voando (sprite sheet) | 16x16, 4 frames | Overlay |
| D10 | Pegadas verdes | 16x16 (alpha) | Qualquer |

---

## 5. Propriedades de Collision (Tiled Custom Properties)

Cada tile deve ter as seguintes propriedades no Tiled:

```json
{
  "walkable": true,
  "speed_modifier": 1.0,
  "collision": false,
  "damage_zone": false,
  "spawn_zone": false,
  "cover": false,
  "description": "Tile description for debug"
}
```

| Tile | walkable | speed_mod | collision | damage_zone | cover |
|---|---|---|---|---|---|
| Concreto | true | 1.0 | false | false | false |
| Grama | true | 0.85 | false | false | false |
| Agua | false | 0 | true | true | false |
| Asfalto | true | 1.0 | false | false | false |
| Piso Interno | true | 1.0 | false | false | false |
| Carpete | true | 1.0 | false | false | false |

---

## 6. Organizacao do Tileset PNG

Layout do tileset 512x512:

```
Row 0:  T01a T01b T01c T01d T02a T02b [vazio] ...
Row 1:  T03a T03b T03c T03d T04a T04b T04c [vazio] ...
Row 2:  T05a T05b T05c T05d T05e T05f T05g T05h T05i ...
Row 3:  T06a T06b T06c T06d T07a T07b T08a T08b ...
Row 4:  T09a T09b T09c T10a T10b [vazio] ...
Row 5-8: Tiles de transicao (Concreto→Grama, Concreto→Asfalto, etc.)
Row 9-11: Tiles de transicao continuacao
Row 12-15: Decoracoes (D01-D10)
Row 16-20: Landmarks parciais (paredes ministeriais, etc.)
Row 21-31: Reservado para expansao
```

---

## 7. Exportacao para Phaser 3

### Arquivo Tiled (.tmx → .json)
```
esplanada.json          — Mapa completo (JSON export)
esplanada-tileset.png   — Tileset image (512x512)
esplanada-tileset.json  — Tileset data (JSON, embedded no mapa)
```

### Carregamento no Phaser (BootScene.ts)
```javascript
// Preload
this.load.image('esplanada-tiles', 'assets/tiles/esplanada-tileset.png');
this.load.tilemapTiledJSON('esplanada-map', 'assets/maps/esplanada.json');

// Create
const map = this.make.tilemap({ key: 'esplanada-map' });
const tileset = map.addTilesetImage('esplanada-tileset', 'esplanada-tiles');
const groundLayer = map.createLayer('Ground', tileset, 0, 0);
groundLayer.setCollisionByProperty({ collision: true });
```

---

## 8. Checklist de Producao

- [ ] Criar paleta de cores no editor (Aseprite/Photoshop)
- [ ] Desenhar 10 tiles base (T01-T10) com variantes
- [ ] Criar tiles de transicao (46 tiles)
- [ ] Criar decoracoes (D01-D10)
- [ ] Montar tileset PNG 512x512
- [ ] Configurar no Tiled Map Editor
- [ ] Definir propriedades de collision
- [ ] Exportar JSON para Phaser 3
- [ ] Testar carregamento na BootScene
- [ ] Aplicar overlay de textura de papel em todos os tiles
- [ ] Verificar que nenhuma cor e "pura" (ver color-palette.md)
- [ ] Testar seamless em grid 8x8 minimo
