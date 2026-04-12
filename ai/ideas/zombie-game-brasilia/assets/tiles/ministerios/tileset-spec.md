# Blocos Ministeriais (M1-M5) — Tileset & Art Spec

> 5 blocos de ministerio ao longo da Esplanada. Brutalismo de Niemeyer.
> Cada bloco: 3 tiles de largura x 4 tiles de altura (48x64px)
> Referencia: Oscar Niemeyer, concreto armado, janelas escuras como olhos vazios

---

## 1. Dimensoes e Estrutura

| Parametro | Valor |
|---|---|
| **Tamanho por bloco** | 48x64px (3x4 tiles de 16x16) |
| **Total de blocos** | 5 (M1 a M5) |
| **Variantes visuais** | 2 (fachada normal + fachada danificada) |
| **Collision** | Sim — paredes sao impassaveis |
| **Interacao** | Portas (1 tile) permitem spawn de zumbis |

---

## 2. Anatomia de um Bloco Ministerial

```
Cada bloco (3x4 tiles):

┌────────────────────────────┐
│  TELHADO/TOPO              │  Row 0: topo do predio (concreto + borda)
│  ██████████████████████████│  
├────────────────────────────┤
│  ANDAR 2 (janelas)         │  Row 1: 3-4 janelas escuras (#1A1A18)
│  ██ ▓▓ ██ ▓▓ ██ ▓▓ ██████│  ▓▓ = janela (olhos mortos)
├────────────────────────────┤
│  ANDAR 1 (janelas)         │  Row 2: 3-4 janelas + placa
│  ██ ▓▓ ██ ▓▓ ██ ▓▓ ██████│  Placa satirica no centro
├────────────────────────────┤
│  TERREO (colunas + porta)  │  Row 3: colunas (pilotis Niemeyer)
│  ┃┃  PORTA  ┃┃    ┃┃     │  Porta = spawn zone (1 tile)
└────────────────────────────┘

Cores:
█ = Concreto #8A8580
▓ = Janela #1A1A18 (preto profundo)
┃ = Coluna/pilotis #7A7A72
PORTA = tile walkable no centro do terreo
```

---

## 3. Placas Satiricas (Sprite separado, 32x8px cada)

| Ministerio | Placa | Posicao |
|---|---|---|
| **M1** | "MIN. DA ENROLACAO" | Centro do Andar 1 |
| **M2** | "MIN. DO PUXADINHO" | Centro do Andar 1 |
| **M3** | "MIN. DA PROMESSA NAO CUMPRIDA" | Centro do Andar 1 |
| **M4** | "MIN. DO JEITINHO" | Centro do Andar 1 |
| **M5** | "MIN. DA PLANILHA INFINITA" | Centro do Andar 1 |

**Estilo da placa:**
- Fundo: `#2A5A3A` (verde institucional)
- Texto: `#F0E8D0` (creme)
- Borda: `#1A1A18` (1px)
- Fonte: Condensada, irregular, estilo carimbo
- Leve inclinacao (1-2 graus) — nada e reto neste mundo

---

## 4. Tiles Individuais do Bloco

### Row 0 — Topo
| Tile | Conteudo | Cor |
|---|---|---|
| M_top_L | Canto superior esquerdo, borda + concreto | `#8A8580`, borda `#5C5C55` |
| M_top_C | Centro do topo, laje/parapeito | `#8A8580` |
| M_top_R | Canto superior direito | `#8A8580`, borda `#5C5C55` |

### Row 1 — Andar Superior
| Tile | Conteudo | Cor |
|---|---|---|
| M_floor2_L | Parede + janela esquerda | `#8A8580` parede, `#1A1A18` janela |
| M_floor2_C | Parede + janela central | `#8A8580` parede, `#1A1A18` janela |
| M_floor2_R | Parede + janela direita | `#8A8580` parede, `#1A1A18` janela |

### Row 2 — Andar Inferior (com placa)
| Tile | Conteudo | Cor |
|---|---|---|
| M_floor1_L | Parede + janela | `#8A8580`, `#1A1A18` |
| M_floor1_C | Parede + PLACA SATIRICA | `#2A5A3A` placa sobre `#8A8580` |
| M_floor1_R | Parede + janela | `#8A8580`, `#1A1A18` |

### Row 3 — Terreo (Pilotis)
| Tile | Conteudo | Collision |
|---|---|---|
| M_ground_L | Coluna esquerda + sombra | SIM (coluna bloqueia) |
| M_ground_C | PORTA (abertura entre colunas) | NAO (spawn zone) |
| M_ground_R | Coluna direita + sombra | SIM |

---

## 5. Variante Danificada

Apos wave 10+, ministerios podem ter variante danificada:
- Janelas quebradas (linhas diagonais sobre `#1A1A18`)
- Rachaduras no concreto (linhas `#3A3530`)
- Placa torta ou caida
- Manchas esverdeadas do gas (`#3D6B3A` alpha 30%)
- Santinhos grudados na fachada (`#F0E8D0` retangulos)

---

## 6. Sombras Projetadas

Cada ministerio projeta sombra no chao (direcao NE→SW, sol a noroeste, 15h):
- **Comprimento:** 4 tiles para o sul/sudoeste
- **Cor:** `#1A1A18` alpha 25%
- **Layer:** ground-shadows (Layer 1, sub-layer)
- **Formato:** Trapezio se alargando

```
Sombra de um ministerio:
      ┌───┐
      │ M │  ← Ministerio
      └───┘
       \██\
        \████\
         \██████\  ← Sombra se alargando
```

---

## 7. Art Prompt (Geracao)

```
[STYLE PREFIX]
brutalist government ministry building, top-down RPG view,
Oscar Niemeyer inspired concrete block, rectangular severe shape,
dark empty windows arranged in grid like dead eyes,
concrete columns (pilotis) at ground level,
satirical green sign on facade, weathered gray concrete,
small door opening at ground level between pillars,
colors: #8A8580 concrete walls, #1A1A18 dark windows, 
#2A5A3A green sign, #7A7A72 columns,
pixel art building sprite, 48x64 pixels total,
hand-drawn rough outlines, cross-hatching shadows
```

---

## 8. Checklist

- [ ] Desenhar template base do bloco (3x4 tiles)
- [ ] Criar 12 tiles individuais (3 cols x 4 rows)
- [ ] Criar 5 placas satiricas (32x8px cada)
- [ ] Criar variante danificada (12 tiles alternativos)
- [ ] Criar tiles de sombra projetada (8-10 tiles)
- [ ] Definir collision map no Tiled
- [ ] Definir spawn zones nas portas (Object Layer)
- [ ] Testar que zumbis podem sair pelas portas
- [ ] Testar que projeteis sao bloqueados por colunas
