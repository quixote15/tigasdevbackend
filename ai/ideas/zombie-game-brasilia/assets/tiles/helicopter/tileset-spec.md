# Helicoptero IBAMA — Sprite & Art Spec

> Helicoptero verde-musgo tombado. Laminas torcidas. Cover parcial.
> "Manutencao Preventiva desde 1987"
> Obstaculo tatico — projeteis sao bloqueados, jogador se esconde atras.

---

## 1. Dimensoes

| Parametro | Valor |
|---|---|
| **Tamanho** | 48x32px (3x2 tiles) |
| **Posicao no mapa** | Tile (18, 32) — zona sul |
| **Tipo Phaser** | StaticSprite (Entities layer, Y-sorted) |
| **Collision** | Parcial — corpo bloqueia, laminas nao |

---

## 2. Visual

```
48x32px — Vista top-down:

    ╲╲╲              ← Laminas torcidas (1px linhas)
  ┌─────────────┐
  │  IBAMA      │    ← Fuselagem (retangulo arredondado)
  │   ████████  │    ← Janela/windshield (rachado)
  │             │
  └──┤     ├────┘
     │SKID │         ← Skid/trem de pouso
     └─────┘
      ///            ← Lamina traseira (torcida)

Tombado para o lado esquerdo (inclinacao 15-20 graus)
```

### Cores
| Parte | Cor |
|---|---|
| Fuselagem | `#4A6B3A` (verde-musgo IBAMA) |
| Ferrugem/dano | `#8B4513` (marrom ferrugem) |
| Windshield | `#5C5C55` rachado com linhas brancas |
| Laminas | `#7A7A72` (metal cinza) |
| Skid | `#3A3530` (metal escuro) |
| Texto "IBAMA" | `#F0E8D0` desbotado |

### Detalhes Obrigatorios
- Laminas TORCIDAS (nao retas) — linhas onduladas
- Windshield rachado (linhas diagonais de crack)
- Placa: "MANUTENCAO PREVENTIVA DESDE 1987" (sprite separado 32x4px)
- Mancha de oleo no chao ao redor (`#3A3530` alpha 30%)
- 1-2 parafusos no chao (sprites 2x2px)

---

## 3. Collision Map

```
Hitbox (3x2 tiles):
┌───┬───┬───┐
│ N │ Y │ Y │  N = sem collision (laminas), Y = collision (corpo)
├───┼───┼───┤
│ N │ Y │ N │  Centro bloqueia, extremidades nao
└───┴───┴───┘
```

O jogador pode se posicionar atras do corpo (tiles Y) para bloquear projeteis vindos do norte.

---

## 4. Art Prompt

```
[STYLE PREFIX]
crashed helicopter lying on its side, top-down view,
green-brown military/environmental agency helicopter wreck,
"IBAMA" text faded on fuselage, twisted rotor blades,
cracked windshield with spider-web cracks, rust patches,
oil stain on ground around wreck, scattered bolts,
small plaque reading maintenance joke,
colors: #4A6B3A green body, #8B4513 rust, #7A7A72 metal blades,
#5C5C55 cracked glass, #3A3530 oil stain,
pixel art sprite, 48x32 pixels, hand-drawn rough style
```

---

## 5. Checklist

- [ ] Desenhar sprite 48x32px
- [ ] Garantir laminas visivelmente torcidas
- [ ] Texto "IBAMA" legivel a 2x scale
- [ ] Criar placa de manutencao (32x4px)
- [ ] Definir collision parcial no Phaser
- [ ] Criar mancha de oleo no chao (tile decorativo)
- [ ] Testar cover: projeteis bloqueados pela fuselagem?
