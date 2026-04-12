# Congresso Nacional — Background & Art Spec

> O Congresso e background, NAO tile jogavel no MVP.
> Fica ao fundo do mapa, acima do horizonte, como presenca ameacadora.
> Pulsa com luz verde sinistra — o epicentro da infestacao.
> "As 2 cupulas como dois olhos mortos observando."

---

## 1. Sprite do Congresso (Silhueta)

| Parametro | Valor |
|---|---|
| **Tamanho** | 128x48px |
| **Tipo** | Sprite estatico (background) |
| **scrollFactor** | 0.3 (parallax lento) |
| **depth** | -999 |
| **Posicao** | Centro horizontal, linha do horizonte |

---

## 2. Anatomia Visual

```
128x48 pixels — Silhueta simplificada frontal:

                    ┌──┐┌──┐
                    │T1││T2│          T1, T2 = Torres gemeas (retangulos verticais)
         ___        │  ││  │        ___
        / C \       │  ││  │       / S \
       /AMAR\      │  ││  │      / ENA \
      / A    \     │  ││  │     / DO   \
     /________\    │  ││  │    /________\
                    │  ││  │
    ════════════════╧══╧╧══╧════════════════
                   RAMPA / BASE

C = Cupula concava da Camara (forma de prato/bowl invertido)
S = Cupula convexa do Senado (forma de domo/meia-esfera)
T1, T2 = Torres gemeas (28 andares, retangulares)

Tudo em #1A1A18 (silhueta quase preta)
Brilho verde #3D6B3A emana do espaco entre as torres
```

---

## 3. Efeito de Pulso Verde

O brilho entre as cupulas pulsa como algo RESPIRANDO dentro do Congresso.

| Parametro | Valor |
|---|---|
| **Tipo Phaser** | PointLight |
| **Cor** | `#3D6B3A` |
| **Raio** | 100px |
| **Intensidade min** | 0.2 |
| **Intensidade max** | 0.5 |
| **Duracao do ciclo** | 3 segundos (yoyo) |
| **Ease** | Sine.easeInOut |

### Progressao por Wave
O brilho se intensifica conforme o jogo avanca:

| Wave | Intensidade min/max | Raio | Efeito |
|---|---|---|---|
| 1-5 | 0.1 / 0.3 | 80px | Sutil, quase imperceptivel |
| 6-10 | 0.2 / 0.5 | 100px | Noticeable, inquietante |
| 11-15 | 0.3 / 0.7 | 120px | Obvio, ameacador |
| 16+ | 0.4 / 0.9 | 150px | Dominante, pulsa como coracao |

---

## 4. Detalhes Visuais da Silhueta

### Cupula da Camara (Concava)
- Forma de prato / bowl virado para cima
- Borda fina (1px) mais clara que o corpo (`#2A2A28`)
- Interior sugere vazio (mesmo tom do ceu)

### Cupula do Senado (Convexa)
- Forma de meia-esfera / domo
- Borda fina (1px) mais clara
- Solida, opaca

### Torres Gemeas
- 2 retangulos verticais estreitos
- 4-5px de largura cada, ~30px de altura
- Espaçamento de 3-4px entre elas
- O brilho verde sai desse espaco

### Base / Rampa
- Plataforma horizontal sob tudo
- Linha fina representando a rampa iconica
- Mesma cor da silhueta

---

## 5. Congresso Expandido (Futuro — Boss Arena)

No futuro (Wave 25+, boss final), o Congresso se torna area jogavel:

### Exterior (Rampa)
- Rampa ascendente (3 tiles de largura, 5 tiles de comprimento)
- Maos de zumbi emergindo do concreto (sprites decorativos)
- Gas mais denso aqui (emitter com density 3x)

### Interior (Plenario)
- Carpete vermelho (T08)
- Cadeiras enfileiradas (sprites, cobertura parcial)
- Cadeira gigante do Presidente da Camara (boss throne)
- Iluminacao verde vinda de cima (lampadas infectadas)

*(Nao produzir agora — apenas documentar para expansao)*

---

## 6. Art Prompt

**Silhueta:**
```
[STYLE PREFIX]
Brazilian National Congress building silhouette against orange-red sky,
front view iconic architecture, two distinctive domes:
left dome is concave (bowl shape facing up = House of Representatives),
right dome is convex (dome shape = Senate),
twin rectangular towers rising between the domes,
flat platform/ramp at base connecting everything,
dark silhouette almost black, sinister green glow between towers,
Oscar Niemeyer modernist architecture,
pixel art, 128x48 pixels,
colors: #1A1A18 dark silhouette, #3D6B3A eerie green glow,
dramatic backlit against sunset sky
```

**Brilho verde (referencia para efeito):**
```
soft green pulsating light emanating from between two dark towers,
bio-luminescent toxic glow, alien-like pulse,
breathing rhythm, slow intensity change,
color: #3D6B3A green, diffuse edges
```

---

## 7. Checklist

- [ ] Desenhar silhueta 128x48px (Aseprite)
- [ ] Garantir que as 2 cupulas sao distinguiveis a distancia
- [ ] Testar silhueta contra gradient de ceu (deve ter contraste)
- [ ] Implementar PointLight no Phaser
- [ ] Testar parallax (scrollFactor 0.3)
- [ ] Testar progressao de intensidade por wave
- [ ] Documentar assets para expansao futura (plenario)
