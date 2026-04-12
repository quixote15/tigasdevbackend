# Gramados Secos — Tileset & Art Spec

> Terreno de grama morta da Esplanada. O jardim publico que ninguem rega.
> Spawns secundarios, mais drops de power-up, terreno mais lento.
> "Brasil desidratado, negligencia."

---

## 1. Tiles de Grama (ver tileset-spec.md principal)

Os tiles base de grama (T03, T04, T10) sao definidos no tileset principal da Esplanada. Este doc cobre a ZONA de gramado como area funcional.

---

## 2. Zonas de Gramado no Mapa

| Zona | Posicao (tiles) | Funcao |
|---|---|---|
| Gramado Norte | Rows 0-6, entre ministerios | Transicao entre ministerios |
| Gramado Sul-Leste | Rows 28-40, cols 0-14 | Area aberta de combate |
| Gramado Sul-Oeste | Rows 28-40, cols 46-60 | Area aberta de combate |
| Gramado bordas | Perimetro do mapa | Borda visual |

---

## 3. Decoracoes Especificas do Gramado

| Sprite | Tamanho | Descricao |
|---|---|---|
| Placa de campanha | 8x16px | Retangulo vertical fincado na grama. "VOTE XX" |
| Irrigador quebrado | 16x16px | Metal torto, sem agua. Jato seco |
| Buraco de obra | 16x16px | Circulo escuro, terra exposta |
| Formigueiro | 8x8px | Montinho de terra |
| Toco de arvore | 16x16px | Arvore cortada, aneis visiveis |
| Banco destruido | 32x16px | Banco de praca partido ao meio |
| Lata de lixo tombada | 16x16px | Lixo espalhado |

---

## 4. Propriedades do Terreno

| Propriedade | Valor |
|---|---|
| **Speed modifier** | 0.85 (15% mais lento que concreto/asfalto) |
| **Spawn probability** | 1.5x vs concreto (mais zumbis surgem aqui) |
| **Drop rate** | 1.3x (mais power-ups dropam no gramado) |
| **Justificativa narrativa** | "Grama morta esconde coisas" |

---

## 5. Art Prompts

**Decoracoes:**
```
[STYLE PREFIX]
abandoned public park decorations on dead grass, top-down view,
broken irrigation sprinkler (no water), campaign signs stuck in ground,
unfinished construction holes, toppled park bench,
knocked over trash can with litter spilling out,
dead tree stump with visible rings,
neglected Brazilian government district green space,
colors: various on #C4A265 dead grass base,
pixel art decoration sprites, 8-32 pixels each
```
