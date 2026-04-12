# Buffet de Gala — Sprite & Art Spec

> Mesa com toalha branca manchada, champagne, lagosta meio-comida.
> Score multiplier zone (x2 por 5 segundos).
> "O contribuinte paga, o politico come."

---

## 1. Dimensoes

| Parametro | Valor |
|---|---|
| **Tamanho** | 32x16px (2x1 tiles) |
| **Posicao no mapa** | Tile (40, 32) |
| **Tipo Phaser** | StaticSprite + Overlap Zone |
| **Collision** | Nao (jogador pode passar por cima para coletar bonus) |

---

## 2. Visual

```
32x16px — Vista top-down:

┌──────────────────────────────┐
│ ┌──────────────────────────┐ │
│ │ 🦞   🍾   🥂   🍾  🦞  │ │  ← Mesa coberta de toalha
│ │     manchas              │ │  ← Manchas vermelhas na toalha
│ └──────────────────────────┘ │
│   ┃┃            ┃┃          │  ← Pernas da mesa
└──────────────────────────────┘

Elementos na mesa (sprites 2-3px):
- Lagosta vermelha (meio-comida)
- Garrafas de champagne (tombadas)
- Tacas quebradas
- Manchas de vinho/sangue na toalha
```

### Cores
| Parte | Cor |
|---|---|
| Toalha | `#E8E0D0` (branco sujo) |
| Manchas | `#8B0000` (vinho/sangue — ambiguo proposital) |
| Lagosta | `#CC3030` |
| Champagne | `#C8A832` (dourado corrupto) |
| Tacas | `#E8E0D0` com brilho |
| Pernas da mesa | `#3A3530` |

---

## 3. Mecanica de Score

| Parametro | Valor |
|---|---|
| **Efeito** | Score x2 por 5 segundos |
| **Ativacao** | Player pisa na zona |
| **Cooldown** | 45 segundos |
| **Visual ativo** | Brilho dourado (`#C8A832`) ao redor do player |
| **Texto** | "SCORE x2!" flutuante em `#F0C830` |
| **SFX** | Som de champagne abrindo |

---

## 4. Art Prompt

```
[STYLE PREFIX]
fancy politician banquet table aftermath, top-down view,
long table with stained white tablecloth,
half-eaten red lobster, toppled champagne bottles,
broken wine glasses, wine/blood stains on cloth (ambiguous),
decadent feast remains, corruption party leftovers,
gold and red accents on dirty white cloth,
colors: #E8E0D0 tablecloth, #8B0000 stains, #C8A832 champagne gold,
#CC3030 lobster, #3A3530 table legs,
pixel art sprite, 32x16 pixels, grotesque detail
```
