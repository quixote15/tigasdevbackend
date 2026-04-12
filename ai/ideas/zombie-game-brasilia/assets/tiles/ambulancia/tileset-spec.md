# Ambulancia SUS — Sprite & Art Spec

> Ambulancia branca batida, sirene fraca, fila de cadeiras plasticas.
> Ponto de cura passiva (3s de fila para curar).
> "Satirizando filas do SUS — ate no apocalipse."

---

## 1. Dimensoes

| Parametro | Valor |
|---|---|
| **Ambulancia** | 32x16px (2x1 tiles) |
| **Zona de cura (cadeiras)** | 32x16px (2x1 tiles, ao lado) |
| **Total com zona** | 32x32px (2x2 tiles) |
| **Posicao no mapa** | Tile (33, 32) |
| **Tipo Phaser** | StaticSprite + Overlap Zone |

---

## 2. Visual da Ambulancia

```
32x16px — Vista top-down:

┌──────────────────────────────┐
│  🚨  ┌────────────────────┐  │
│ (sir)│   AMBULANCIA SUS   │  │  ← Branco sujo com cruz vermelha
│      │        +           │  │  ← Cruz no teto
│      └────────────────────┘  │
│         ████  ████           │  ← Rodas (pretas)
└──────────────────────────────┘
  Amassada no canto frontal esquerdo (deformacao)
```

### Cores
| Parte | Cor |
|---|---|
| Carroceria | `#E8E0D0` (branco sujo, NUNCA branco puro) |
| Cruz | `#CC3030` |
| Sirene | `#CC3030` alpha pulsante (60-100%) |
| Amassado | `#B0A890` (sombra do amassado) |
| Rodas | `#1A1A18` |
| Texto "SUS" | `#2A5A3A` verde institucional |

---

## 3. Fila de Cadeiras (Zona de Cura)

```
32x16px — Vista top-down:

  ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐      ← 5 cadeiras de plastico alinhadas
  │░│ │░│ │░│ │░│ │░│
  └─┘ └─┘ └─┘ └─┘ └─┘
  ═══════════════════         ← Faixa "AGUARDE SUA VEZ" (4px altura)

Cadeiras: #E8E0D0 (branco) e #4A8ACA (azul SUS)
Placa: #2A5A3A fundo, #F0E8D0 texto
```

---

## 4. Mecanica de Cura

| Parametro | Valor |
|---|---|
| **Tempo de espera** | 3 segundos (satira da fila do SUS) |
| **Cura por segundo** | 10 HP/s (apos esperar) |
| **Cura maxima** | 50 HP por visita |
| **Cooldown** | 30 segundos entre usos |
| **Visual durante espera** | Timer circular sobre o player |
| **Visual durante cura** | Particulas brancas + cruz vermelha flutuante |

### Implementacao
```javascript
// Overlap zone da ambulancia
this.physics.add.overlap(this.player, this.ambulanciaZone, () => {
    if (!this.ambulanciaOnCooldown) {
        this.startHealingQueue(); // 3s de espera, depois cura
    }
});
```

---

## 5. Sirene Piscando

Efeito visual sutil — a sirene pisca fraca:
- **Frequencia:** 1Hz (1 flash por segundo)
- **Alpha:** 0.3 → 0.8 → 0.3
- **Cor:** `#CC3030`
- **Raio:** 8px (PointLight pequeno)
- Indica que a ambulancia "funciona" (mal, mas funciona)

---

## 6. Art Prompt

```
[STYLE PREFIX]
crashed ambulance van, top-down view,
white ambulance with red cross on roof, dented front-left corner,
weak red siren light on top barely flashing,
"SUS" text in green on side, dirty white paint,
row of 5 plastic chairs next to ambulance (waiting line),
small sign "AGUARDE SUA VEZ" (wait your turn),
satirical public healthcare waiting line even in zombie apocalypse,
colors: #E8E0D0 dirty white body, #CC3030 red cross and siren,
#2A5A3A green SUS text, chairs in white and blue,
pixel art sprite, 32x32 pixels total (ambulance + chairs area)
```

---

## 7. Checklist

- [ ] Desenhar ambulancia 32x16px
- [ ] Desenhar fila de cadeiras 32x16px
- [ ] Criar animacao da sirene (PointLight pulse)
- [ ] Implementar zona de cura (overlap + timer)
- [ ] Criar particulas de cura (brancas + cruz)
- [ ] Testar tempo de espera (3s deve SENTIR como SUS)
- [ ] Placa "AGUARDE SUA VEZ" legivel a 2x
