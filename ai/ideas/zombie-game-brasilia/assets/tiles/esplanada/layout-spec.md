# Layout Spec — Mapa da Esplanada dos Ministerios

> Como os tiles se conectam. Mapa da arena principal (MVP).
> Dimensoes: 60 x 40 tiles (960 x 640 px em 16x16 tiles)
> Viewport: 480 x 320 px, camera segue player, escala 2x

---

## 1. Mapa Macro (Visao Aerea)

```
Legenda:
  C = Concreto rachado (T01)      G = Grama seca (T03)
  A = Asfalto (T06)               W = Agua turva (T05)
  . = Grama com decoracao         M = Bloco Ministerial
  H = Helicoptero IBAMA           B = Buffet de Gala
  U = Ambulancia SUS              V = Cabine de Votacao
  P = Palanque Eleitoral          S = Santinhos densos (T09c)

Norte (cima) = Direcao do Congresso
Sul (baixo) = Ponto de spawn do player

Cada celula = 2x2 tiles (para legibilidade do ASCII)
Mapa real = 60x40 tiles
```

```
Col:  0    5    10   15   20   25   30   35   40   45   50   55   60
     ┌────────────────────────────────────────────────────────────────┐
  0  │GGGG.GGGGGGGG.GGGGGGGGGGGGGGGGGGGGGGGGG.GGGGGGGGGG.GGGGGGGGGGG│ 
  2  │GG.GGGGGM1M1M1GGGGGM2M2M2GGGGGM3M3M3GGGGGM4M4M4GGGGM5M5M5GG│
  4  │GGGGGG.GM1M1M1G.GGGM2M2M2GGGGGM3M3M3GG.GGM4M4M4GGGGM5M5M5GG│
  6  │GGGGGGGCM1M1M1CCCCCM2M2M2CCCCCM3M3M3CCCCCM4M4M4CCCCM5M5M5GG│
  8  │GG.GGGGCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGGG│
 10  │GGGGGGGCCCCCCSCCCCCCCCCCCCCSCCCCCCCCCSCCCCCCCCCCSCCCCCCCCCCCGGG│
 12  │CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC│
 14  │AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA│ ← Eixo
 16  │AAAA====AAAA====AAAA====AAAA====AAAA====AAAA====AAAA====AAAA│ ← Faixa
 18  │AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA│ ← Monumental
 20  │CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC│
 22  │GGGCCCCCCCCCCCCWWWWWWWWWWWWWWWWWWWWWWWWWWWWCCCCCCCCCCCCCCCCGGGG│
 24  │GGGGCCCCCCCCCCCWWWWWWWWWWWWWWWWWWWWWWWWWWWWCCCCCCCCCCCCCCCGGGGG│ ← Espelho
 26  │GGGCCCCCCCCCCCCWWWWWWWWWWWWWWWWWWWWWWWWWWWWCCCCCCCCCCCCCCCGGGGG│     D'Agua
 28  │GGGGCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGGGG│
 30  │GG.GGGGGGGGGGCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGGGGGGGGGGGG.GGGG│
 32  │GGGGG.GGGGGGGCCCCCHHHCCCCCVCCCCCCUCCCCCCCBBBCCCGGGGGGG.GGGGGGG│
 34  │GGGGGGGGGG.GGGCCCCCHHHCCCCCCCCCCCCCCCCCCCBBBCCCCGGG.GGGGGGGGGG│
 36  │GGG.GGGGGGGGGGGCCCCCCCCCCPCCCCCCCCCCCCCCCCCCCCCGGGGGGGGGG.GGGG│
 38  │GGGGGGGG.GGGGGGGGGG.GGGGGPGGGGG.GGGGGGG.GGGGGGGG.GGGGGGGGGGG│
 40  │GGG.GGGGGGGGGGGGGG.GGGGGGGGGGGGGGG.GGGGGGGGGGGGG.GGGGGGGG.GGG│
     └────────────────────────────────────────────────────────────────┘
          ↑ SPAWN ZONE (player começa aqui, row 36-40)
```

---

## 2. Zonas do Mapa

### Zona Norte: Ministerios (Rows 0-11)
- **Terreno base:** Grama seca + concreto (calcadas entre ministerios)
- **Landmarks:** 5 Blocos Ministeriais (M1-M5), alinhados
- **Funcao:** Chokepoints — colunas dos ministerios bloqueiam projeteis e canalizam zumbis
- **Spawn de zumbis:** Sim — saem de dentro dos ministerios (portas)
- **Decoracao:** Placas satiricas, santinhos densos (T09c) entre blocos

### Zona Central: Eixo Monumental (Rows 12-20)
- **Terreno base:** Asfalto (T06) com faixa amarela
- **Largura:** 6 tiles (3 tiles de cada lado da faixa)
- **Funcao:** Corredor de kiting — sem cobertura, alta velocidade
- **Spawn de zumbis:** Raro — e corredor, nao area de spawn
- **Decoracao:** Postes tombados (D01), cones de transito (D06)

### Zona Sul-Central: Espelho D'Agua (Rows 22-28)
- **Terreno base:** Agua turva (T05) cercada por concreto
- **Dimensoes:** 28 tiles de largura x 5 tiles de altura
- **Funcao:** Divisor de mapa — impassavel, zumbis caem e afundam
- **Visual:** Reflexo esverdeado do Congresso (sprite overlay)

### Zona Sul: Area Aberta (Rows 28-40)
- **Terreno base:** Grama seca + concreto (calcadas)
- **Landmarks:** Helicoptero (H), Ambulancia (U), Cabine de Votacao (V), Buffet (B), Palanque (P)
- **Funcao:** Area principal de combate — mais aberta, mais drops
- **Spawn do player:** Row 38, coluna 30 (centro-sul)
- **Spawn de zumbis:** Bordas laterais + area norte

---

## 3. Conexoes Entre Tiles (Regras de Adjacencia)

### Regras Obrigatorias

| Tile A | Pode ser adjacente a | Tile de transicao necessario |
|---|---|---|
| Concreto (T01) | Grama (T03) | Sim — borda concreto/grama |
| Concreto (T01) | Asfalto (T06) | Sim — borda concreto/asfalto |
| Concreto (T01) | Agua (T05) | Sim — borda concreto/agua |
| Grama (T03) | Agua (T05) | Sim — borda grama/agua |
| Asfalto (T06) | Grama (T03) | Sim — borda asfalto/grama |
| Asfalto (T06) | Concreto (T01) | Sim — borda asfalto/concreto |
| Piso Interno (T07) | Concreto (T01) | Sim — borda porta/entrada |
| Carpete (T08) | Piso Interno (T07) | Sim — borda simples |

### Regras Proibidas

| Tile A | NAO pode ser adjacente a | Razao |
|---|---|---|
| Grama (T03) | Piso Interno (T07) | Nao faz sentido — grama nao entra em predio |
| Carpete (T08) | Grama (T03) | Nao faz sentido |
| Agua (T05) | Asfalto (T06) | O espelho d'agua e cercado de concreto |
| Carpete (T08) | Asfalto (T06) | Carpete e so dentro de predios |

### Autotiling (Wang Tiles)
Para o Tiled Map Editor, usar terrain sets:
- Terreno 1: Concreto
- Terreno 2: Grama
- Terreno 3: Agua
- Terreno 4: Asfalto

Cada par de terrenos tem 8 tiles de transicao (4 bordas + 4 cantos).

---

## 4. Posicoes dos Landmarks (Coordenadas em Tiles)

| Landmark | Posicao (tile X, Y) | Tamanho (tiles) | Collision |
|---|---|---|---|
| **Ministerio 1** | (8, 2) | 3x4 | Sim (paredes) |
| **Ministerio 2** | (17, 2) | 3x4 | Sim |
| **Ministerio 3** | (26, 2) | 3x4 | Sim |
| **Ministerio 4** | (35, 2) | 3x4 | Sim |
| **Ministerio 5** | (44, 2) | 3x4 | Sim |
| **Espelho D'Agua** | (14, 22) | 28x5 | Sim (kill zone) |
| **Helicoptero IBAMA** | (18, 32) | 3x2 | Parcial (cover) |
| **Cabine Votacao** | (26, 32) | 1x1 | Nao (interagivel) |
| **Ambulancia SUS** | (33, 32) | 2x1 | Parcial (interagivel) |
| **Buffet Gala** | (40, 32) | 2x1 | Nao (interagivel) |
| **Palanque** | (28, 36) | 2x2 | Parcial |

---

## 5. Spawn Points

### Player Spawn
- **Posicao:** Tile (30, 38) — centro-sul do mapa
- **Direcao:** Olhando para norte (em direcao aos ministerios)
- **Seguranca:** Nenhum zumbi spawna dentro de 8 tiles do player spawn

### Zombie Spawn Zones
```
SPAWN ZONES (bordas do mapa + portas dos ministerios):

    ↓↓↓↓↓ Spawn Norte (wave 1+)
  ←M1  M2  M3  M4  M5→  Spawn das portas (wave 3+)
  ←                    →  Spawn Laterais (wave 1+)
  ←                    →
  ←    [EIXO]          →
  ←                    →
  ←   [ESPELHO]        →
  ←                    →
  ←                    →
  ←     [PLAYER]       →
    ↑↑↑↑↑ Spawn Sul (wave 5+ — cercam o player)
```

| Zona de Spawn | Ativacao | Tiles | Max Simultaneo |
|---|---|---|---|
| **Bordas laterais** | Wave 1+ | Y:0-40, X:0 e X:59 | 5 por lado |
| **Norte** | Wave 1+ | Y:0, X:5-55 | 8 |
| **Portas ministerios** | Wave 3+ | Frente de cada M | 2 por ministerio |
| **Sul** | Wave 5+ | Y:39, X:10-50 | 6 |
| **Centro (pos-espelho)** | Wave 8+ | Y:28-30, X:20-40 | 4 |

---

## 6. Zones Funcionais (Phaser Overlap Zones)

| Zona | Posicao | Efeito | Visual |
|---|---|---|---|
| **Zona de Cura (Ambulancia)** | (33,31)-(34,33) 2x3 tiles | Cura 10 HP/s apos 3s na fila | Cadeiras plasticas + sinal "SUS" |
| **Zona de Power-up (Cabine)** | (25,31)-(26,33) 2x3 tiles | Spawn de power-up 1x por wave | Urna tombada brilhando |
| **Zona de Score (Buffet)** | (39,31)-(41,33) 3x3 tiles | Score x2 por 5s | Brilho dourado |
| **Zona de Cover (Helicoptero)** | (17,31)-(20,33) 4x3 tiles | Projeteis bloqueados | Sombra do helicoptero |
| **Zona de Boss (Palanque)** | (27,35)-(29,37) 3x3 tiles | Spawn de boss wave 5 | Microfone + bandeiras |

---

## 7. Camera e Limites

| Parametro | Valor |
|---|---|
| **Camera viewport** | 480 x 320 px |
| **Mapa total** | 960 x 640 px |
| **Camera follow** | Player, com deadzone 60x40px |
| **Camera bounds** | (0, 0) a (960, 640) |
| **Zoom** | 1.0 (sem zoom, tiles a 2x por padrao do scale) |

### Deadzone
A camera so se move quando o player sai da zona central:
```javascript
this.cameras.main.startFollow(this.player, true, 0.1, 0.1);
this.cameras.main.setDeadzone(60, 40);
this.cameras.main.setBounds(0, 0, 960, 640);
```

---

## 8. Fluxo de Navegacao do Player

```
FLUXO TIPICO DE UMA PARTIDA:

1. Player spawna no SUL (row 38)
   → Primeiros zumbis vem do NORTE e LATERAIS
   → Player naturalmente se move para NORTE (em direcao aos ministerios)

2. Wave 1-2: Combate na AREA ABERTA SUL
   → Zumbis fracos (Vereadores), espaco aberto
   → Player descobre landmarks: Ambulancia, Helicoptero, Cabine

3. Wave 3-4: Zumbis saem dos MINISTERIOS
   → Player avanca para o EIXO MONUMENTAL
   → Corredor de kiting, sem cobertura
   → Assessores com projeteis forcam movimento

4. Wave 5: BOSS no PALANQUE
   → Candidato Eterno spawna no palanque
   → Arena semi-aberta no sul

5. Wave 6+: Mapa inteiro e usado
   → Zumbis de todos os lados
   → Espelho D'Agua como barreira tatica
   → Player usa ministerios como chokepoint
   
6. High waves: CERCAMENTO
   → Spawns de todos os lados
   → Player precisa usar TODA a arena
   → Ministerios + Helicoptero como cover
   → Ambulancia como recurso estrategico
```

---

## 9. Mapa de Calor (Dificuldade por Zona)

```
DIFICULDADE POR AREA (1-5 estrelas):

  ★★★★☆  ★★★★★  ★★★★★  ★★★★★  ★★★★☆
    M1      M2      M3      M4      M5     ← Perto de ministerios: DIFICIL
  
  ★★★☆☆  ★★★☆☆  ★★★☆☆  ★★★☆☆  ★★★☆☆  ← Eixo: MEDIO (sem cover)

  ★★☆☆☆  ★★☆☆☆  WATER   ★★☆☆☆  ★★☆☆☆  ← Perto d'agua: FACIL (poucos spawns)

  ★★★☆☆  ★★★☆☆  ★★★☆☆  ★★★☆☆  ★★★☆☆  ← Area aberta: MEDIO
  
  ★☆☆☆☆  ★★☆☆☆  ★★☆☆☆  ★★☆☆☆  ★☆☆☆☆  ← Spawn area: FACIL (waves baixas)
```

---

## 10. Checklist de Producao do Mapa

- [ ] Criar mapa base no Tiled (60x40 tiles, 16x16)
- [ ] Pintar terrenos base (concreto, grama, asfalto, agua)
- [ ] Aplicar tiles de transicao (autotile)
- [ ] Colocar decoracoes de chao (layer ground-decor)
- [ ] Pintar sombras dos ministerios (layer ground-shadows)
- [ ] Posicionar landmarks como Object Layer no Tiled
- [ ] Definir spawn zones como Object Layer
- [ ] Definir functional zones como Object Layer
- [ ] Exportar JSON para Phaser 3
- [ ] Testar carregamento e collision
- [ ] Testar camera follow e bounds
- [ ] Playtest de fluxo: player consegue navegar todas as areas?
- [ ] Playtest de dificuldade: zonas difíceis sao interessantes?
