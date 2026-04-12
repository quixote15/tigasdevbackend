# Eixo Monumental — Tileset & Art Spec

> Corredor central de asfalto rachado. Principal via de kiting e fuga.
> 2 tiles de largura (base), expandido para 6 tiles com calcadas laterais.
> Faixa amarela desbotada no centro.

---

## 1. Dimensoes

| Parametro | Valor |
|---|---|
| **Largura total** | 6 tiles (96px) — asfalto central + calcadas |
| **Largura asfalto** | 4 tiles (64px) |
| **Comprimento** | 60 tiles (largura total do mapa) — horizontal |
| **Orientacao** | Horizontal (leste-oeste) |
| **Faixa amarela** | 2px de largura, centro do asfalto |

---

## 2. Composicao (Corte Transversal)

```
Tile:  1      2      3      4      5      6
     ┌──────┬──────┬──────┬──────┬──────┬──────┐
     │Grama │Calca-│Asfal-│Asfal-│Calca-│Grama │
     │ seca │ da   │ to   │ to   │ da   │ seca │
     │(T03) │(T01) │(T06b)│(T06b)│(T01) │(T03) │
     │      │      │══════│══════│      │      │
     │      │      │faixa │faixa │      │      │
     └──────┴──────┴──────┴──────┴──────┴──────┘
              ↑                     ↑
         Borda grama/          Borda calcada/
         concreto              grama
```

---

## 3. Tiles Especificos

| ID | Tile | Descricao |
|---|---|---|
| EX01 | Asfalto com faixa H | `#3A3530` com faixa `#B8A030` horizontal |
| EX02 | Asfalto sem faixa | `#3A3530` liso, rachado |
| EX03 | Asfalto muito rachado | Rachaduras grandes, quase buraco |
| EX04 | Calcada lateral | Concreto T01 com meio-fio (borda escura) |
| EX05 | Transicao grama→calcada | Borda irregular |
| EX06 | Transicao calcada→asfalto | Borda com meio-fio |

---

## 4. Decoracoes do Eixo

| Sprite | Tamanho | Posicao | Collision |
|---|---|---|---|
| Poste tombado | 16x32px | Calcada, inclinado | Parcial (base bloqueia) |
| Cone de transito | 16x16px | Asfalto, aleatorio | Nao |
| Carro abandonado | 32x16px | Asfalto, lateral | Sim (cover) |
| Placa de transito torta | 16x32px | Calcada | Nao |
| Faixa "OBRA EM ANDAMENTO" | 32x8px | Atravessando asfalto | Nao |

---

## 5. Propriedades de Gameplay

| Propriedade | Valor |
|---|---|
| **Speed modifier** | 1.0 (asfalto = velocidade maxima) |
| **Cover** | Nenhum (corredor aberto) |
| **Visibilidade** | Total (sem obstaculos visuais) |
| **Spawn de zumbis** | Raro (apenas nas extremidades) |
| **Uso tatico** | Kiting — correr com zumbis atras, sem parar |

---

## 6. Art Prompt

```
[STYLE PREFIX]
cracked asphalt highway corridor, top-down view,
wide ceremonial avenue with faded yellow center line,
dark gray pavement with cracks and potholes,
toppled street lights on sidewalk, traffic cones scattered,
abandoned car on side, construction barrier,
dystopian government district main road,
colors: #3A3530 asphalt, #B8A030 faded yellow stripe,
#8A8580 concrete sidewalks, #C4A265 dead grass edges,
pixel art seamless horizontal corridor
```
