# Palanque Eleitoral — Sprite & Art Spec

> Palco com microfone e bandeiras. Spawn de boss (Wave 5).
> Onde o Candidato Eterno faz sua "entrada triunfal".
> Madeira barata, bandeiras rasgadas de TODOS os partidos.

---

## 1. Dimensoes

| Parametro | Valor |
|---|---|
| **Tamanho** | 32x32px (2x2 tiles) |
| **Posicao no mapa** | Tile (28, 36) |
| **Tipo Phaser** | StaticSprite + Boss Spawn Zone |
| **Collision** | Parcial (base do palco bloqueia, area ao redor nao) |

---

## 2. Visual

```
32x32px — Vista top-down:

┌──────────────────────────────┐
│  🏴 🏴 🏴 🏴 🏴 🏴 🏴 🏴  │  ← Bandeiras rasgadas (todas as cores)
│  ════════════════════════════│  ← Borda do palco
│ ┌──────────────────────────┐│
│ │      🎤                  ││  ← Microfone no suporte
│ │   ┌──────┐               ││  ← Mesa/podium pequeno
│ │   │PODIUM│               ││
│ │   └──────┘               ││
│ │                          ││  ← Tablado de madeira
│ └──────────────────────────┘│
│   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  │  ← Sombra do palco
└──────────────────────────────┘

Palco elevado ~1 tile, madeira barata, instavel
```

### Cores
| Parte | Cor |
|---|---|
| Tablado/madeira | `#6B4423` (madeira barata) |
| Borda do palco | `#3A3530` (metal/madeira escura) |
| Podium | `#5C5C55` (metal cinza) |
| Microfone | `#7A7A72` com head `#1A1A18` |
| Bandeiras | MIX: `#CC0000`, `#009739`, `#FEDD00`, `#2A3A5A` — TODAS rasgadas |
| Sombra | `#1A1A18` alpha 20% |
| Auto-falantes | `#1A1A18` (caixas de som nos cantos) |

---

## 3. Bandeiras (APARTIDARISMO)

**REGRA CRITICA:** As bandeiras NUNCA sao de um partido so. Todas aparecem JUNTAS e RASGADAS.

Sprites de bandeira (4x8px cada, 6 bandeiras):
- Bandeira vermelha rasgada
- Bandeira verde rasgada
- Bandeira amarela rasgada
- Bandeira azul rasgada
- Bandeira laranja rasgada
- Bandeira branca suja rasgada

Dispostas em arco atras do podium. Mescladas. Nenhuma predomina.

---

## 4. Mecanica de Boss Spawn

| Parametro | Valor |
|---|---|
| **Trigger** | Wave 5 inicia |
| **Pre-spawn** | Microfone distorce audio (1s warning) |
| **Spawn** | Candidato Eterno aparece ATRAS do palanque |
| **Efeito** | Camera shake leve + flash de luz |
| **Texto** | "O CANDIDATO ETERNO ENTROU NA DISPUTA" |
| **Jingle** | Jingle de campanha distorcido |

---

## 5. Art Prompt

```
[STYLE PREFIX]
campaign rally stage/podium, top-down view,
small cheap wooden stage with microphone stand,
torn political party flags from multiple parties hanging behind,
red blue green yellow flags all mixed together and tattered,
small podium/lectern at center, speaker equipment on sides,
Brazilian election rally aesthetics, cheap construction,
colors: #6B4423 wood platform, mixed flag colors all faded/torn,
#7A7A72 microphone, #5C5C55 podium, #1A1A18 speakers,
pixel art sprite, 32x32 pixels, hand-drawn style
```
