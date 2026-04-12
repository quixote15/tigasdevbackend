# Espelho D'Agua — Tileset & Art Spec

> Divisor de mapa impassavel. Agua turva esverdeada.
> "A transparencia prometida — opaca como sempre."
> Zumbis caem e afundam dramaticamente.

---

## 1. Dimensoes

| Parametro | Valor |
|---|---|
| **Largura** | 28 tiles (448px) |
| **Altura** | 5 tiles (80px) — inclui bordas |
| **Agua pura (centro)** | 26x3 tiles |
| **Borda de concreto** | 1 tile em cada lado |
| **Posicao no mapa** | Rows 22-26, centralizado |

---

## 2. Tiles

### Agua
| ID | Tile | Animacao |
|---|---|---|
| W01 | Agua turva centro | 4 frames, 4fps (ondulacao lenta) |
| W02 | Agua com reflexo esverdeado | Overlay `#3D6B3A` alpha 30% |
| W03 | Agua com peixe morto | Sprite 3x2px branco sobre agua |

### Bordas
| ID | Tile | Descricao |
|---|---|---|
| W04 | Borda norte | Concreto acima, agua abaixo |
| W05 | Borda sul | Agua acima, concreto abaixo |
| W06 | Borda leste | Concreto direita, agua esquerda |
| W07 | Borda oeste | Concreto esquerda, agua direita |
| W08-W11 | Cantos (NE, NW, SE, SW) | Transicao curva |

---

## 3. Animacao da Agua

**Spritesheet: 4 frames, 16x16 cada = 64x16 total**

```
Frame 0: Textura base — linhas horizontais finas (1px) onduladas
Frame 1: Linhas deslocadas 1px para direita
Frame 2: Linhas deslocadas 2px (ou padrao invertido)
Frame 3: Linhas deslocadas 1px para esquerda (voltando)

Loop: 0→1→2→3→0 a 4fps = ciclo de 1 segundo
Efeito: Agua parecendo viva mas turva, ondulacao lenta e inquietante
```

---

## 4. Reflexo do Congresso

Sprite separado (64x24px) colocado sobre a agua no centro:
- Silhueta distorcida do Congresso (2 cupulas)
- Alpha: 20%
- Cor: `#3D6B3A`
- Distorcao: ondulacao vertical (2px sine wave)
- Oscila lentamente com a animacao da agua

---

## 5. Interacao: Zumbi Caindo na Agua

Quando um zumbi e empurrado ou caminha para a agua:
1. **Sprite de splash** — 16x16, 3 frames: circulo se expandindo
2. **Zumbi afunda** — Scale Y de 1.0 para 0.0 em 500ms
3. **Bolhas** — 3-4 circulos brancos (2px) subindo por 1s
4. **SFX** — "SPLASH" + gorgolejo

```
Splash sprite (3 frames):
Frame 0: ○ pequeno (4px)
Frame 1: ◯ medio (8px) 
Frame 2: O grande (12px) com gotas
Cores: #2A3D2E base + #E8E0D0 espuma branca
```

---

## 6. Propriedades Phaser

```json
{
  "walkable": false,
  "collision": true,
  "damage_zone": true,
  "damage_type": "instant_kill_zombie",
  "player_effect": "push_back",
  "description": "Espelho d'agua — zumbis caem, player e empurrado"
}
```

**Player vs Agua:**
- Player NAO morre na agua — e empurrado de volta (invisible wall)
- Justificativa narrativa: "O brasileiro sabe nadar no caos"

**Zumbi vs Agua:**
- Zumbi CAI e MORRE com animacao de afogamento
- Funciona como armadilha tatica — empurrar zumbis para a agua

---

## 7. Art Prompt

```
[STYLE PREFIX]
polluted government reflecting pool, top-down view,
murky dark green-black stagnant water surface,
concrete edges around rectangular pool,
dead fish floating (tiny white shapes), oily sheen on surface,
distorted greenish building reflection barely visible,
oppressive stagnant water, no transparency,
colors: #2A3D2E dark water, #3D6B3A green tint, 
#8A8580 concrete border, #E8E0D0 dead fish,
pixel art rectangular water feature, seamless water tiles
```
