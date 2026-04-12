# Cabine de Votacao — Sprite & Art Spec

> Urna eletronica tombada, fios expostos.
> Ponto de spawn de power-up (1 por wave).
> "A democracia estava aqui. Saiu para almocar."

---

## 1. Dimensoes

| Parametro | Valor |
|---|---|
| **Tamanho** | 16x16px (1x1 tile) |
| **Posicao no mapa** | Tile (26, 32) |
| **Tipo Phaser** | StaticSprite + spawn point |
| **Collision** | Nao — interagivel (overlap) |

---

## 2. Visual

```
16x16px — Vista top-down:

┌──────────────┐
│  ┌────────┐  │  ← Cabine de plastico (tombada)
│  │ URNA   │  │
│  │ ■■■■■  │  │  ← Teclado numerico (quadrados pequenos)
│  │ [TELA] │  │  ← Tela mostrando estatica
│  └───┤├───┘  │  ← Fios expostos (linhas cobre)
│      ││      │
│    ~~||~~    │  ← Fios espalhados
└──────────────┘

Tombada ~30 graus para a direita
```

### Cores
| Parte | Cor |
|---|---|
| Cabine | `#4A4A4A` (cinza institucional) |
| Tela | `#1A1A18` com pixels de estatica (`#5C5C55`) |
| Teclas | `#2A2A2A` |
| Fios | `#CC6600` (cobre exposto) |
| Isolamento | `#8B0000` (vermelho de fio) |

---

## 3. Mecanica de Power-up

| Parametro | Valor |
|---|---|
| **Spawn** | 1 power-up por wave, no inicio |
| **Tipo** | Aleatorio do pool de power-ups |
| **Visual** | Item brilha sobre a urna tombada |
| **Coleta** | Player pisa = coleta automatica |
| **Feedback** | Flash + onomatopeia "VOTO!" |

### Brilho do Power-up
- Sprite de glow 16x16 pulsante (`#40B840`)
- Alpha: 0.3 → 0.7 loop
- Scale: 0.9 → 1.1 loop

---

## 4. Art Prompt

```
[STYLE PREFIX]
toppled electronic voting machine booth, top-down view,
Brazilian "urna eletronica" fallen on its side at angle,
gray plastic shell cracked, small screen showing static,
exposed copper wires hanging out, numeric keypad visible,
democracy abandoned aesthetic, institutional gray device,
colors: #4A4A4A gray body, #CC6600 copper wires,
#1A1A18 screen with #5C5C55 static pixels,
pixel art sprite, 16x16 pixels
```
