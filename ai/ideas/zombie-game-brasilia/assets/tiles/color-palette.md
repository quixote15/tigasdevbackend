# Paleta de Cores — Zumbis de Brasilia | Tiles & Cenario

> Referencia cruzada com o Art Direction Bible (09-storytelling-art-direction.md)
> Todas as cores sao "sujas" — NUNCA use cores puras (#FF0000, #0000FF, etc.)
> Inspiracao: impressao offset barata, revista underground, Robert Crumb

---

## 1. Paleta do Ceu (Background Gradient)

O ceu e PERMANENTEMENTE em fim de tarde. Nunca muda. O apocalipse congelou Brasilia as 15h.

| Nome | Hex | Uso | Posicao no Gradiente |
|---|---|---|---|
| **Laranja Sangue** | `#FF6B35` | Topo do horizonte | 0% (base do ceu) |
| **Vermelho Queimado** | `#8B0000` | Meio do ceu | 50% |
| **Noite Morta** | `#2D0A0A` | Topo do ceu | 100% |
| **Laranja Niemeyer** | `#D47820` | Highlight de nuvens | Pontual |

**CSS Gradient de referencia:**
```css
background: linear-gradient(to top, #FF6B35 0%, #8B0000 45%, #2D0A0A 100%);
```

---

## 2. Paleta do Gas da Emenda 666

O gas esverdeado que sai do ar-condicionado do Congresso. Emendas parlamentares liquefazeitas. Onipresente.

| Nome | Hex + Alpha | Uso |
|---|---|---|
| **Gas Base** | `#4A7C59` alpha 40% | Particulas flutuantes no ar |
| **Gas Denso** | `#3D6B3A` alpha 60% | Perto do Congresso, areas mais infectadas |
| **Gas Leve** | `#5A9A6A` alpha 20% | Bordas do mapa, areas perifericas |
| **Brilho Zumbi** | `#3D6B3A` alpha 80% | Olhos dos zumbis, reflexos no espelho d'agua |

---

## 3. Paleta de Terreno (Tiles Base 16x16)

| Nome | Hex | Tile | Notas |
|---|---|---|---|
| **Concreto Niemeyer** | `#8A8580` | Concreto rachado/limpo | Base principal da Esplanada |
| **Concreto Escuro** | `#7A7A72` | Sombras de concreto, rachaduras | Variante escura |
| **Concreto Sujo** | `#5C5C55` | Manchas, areas degradadas | Variante muito escura |
| **Grama Morta** | `#C4A265` | Gramados secos | Amarelo-palha, Brasil desidratado |
| **Grama Escura** | `#7A8830` | Grama com sombra/umidade | Areas mais escuras do gramado |
| **Grama Sangue** | `#8B0000` sobre `#C4A265` | Manchas de sangue-tinta no gramado | Estilizado, NAO realista |
| **Asfalto** | `#3A3530` | Eixo Monumental | Infraestrutura abandonada |
| **Asfalto Faixa** | `#B8A030` | Faixa amarela desbotada | Sobre o asfalto |
| **Agua Turva** | `#2A3D2E` | Espelho d'agua | Transparencia morta |
| **Agua Reflexo** | `#3D6B3A` alpha 50% | Reflexo esverdeado | Sobre a agua turva |
| **Piso Interno** | `#A09888` | Linoleum de escritorio | Desbotado, institucional |
| **Carpete Vermelho** | `#8B2020` | Areas VIP / Plenario | Poder decadente |
| **Santinho Base** | `#F0E8D0` | Papeis no chao | Promessas vazias |
| **Emenda Papel** | `#E8D8B0` | Papeis de emenda no chao | Mais amarelado que santinho |

---

## 4. Paleta dos Landmarks

| Nome | Hex | Landmark | Notas |
|---|---|---|---|
| **Concreto Ministerial** | `#8A8580` | Blocos M1-M5 | Brutalismo, janelas escuras |
| **Janela Vazia** | `#1A1A18` | Janelas dos ministerios | Preto profundo como olhos mortos |
| **Placa Satirica** | `#2A5A3A` | Placas dos ministerios | Verde-institucional |
| **Letra Placa** | `#F0E8D0` | Texto das placas | Creme sobre verde |
| **Metal Enferrujado** | `#8B4513` | Helicoptero, ambulancia | Ferrugem e abandono |
| **Branco Amassado** | `#E8E0D0` | Ambulancia, mesa buffet | Branco sujo, nunca branco puro |
| **Sirene Fraca** | `#CC3030` alpha 60% | Sirene da ambulancia | Pulsa fraco |
| **Toalha Manchada** | `#E8E0D0` + `#8B0000` | Mesa do buffet | Branco com manchas |
| **Champagne** | `#C8A832` | Restos do buffet | Dourado corrupto |
| **Urna Cinza** | `#4A4A4A` | Cabine de votacao | Cinza institucional |
| **Fio Exposto** | `#CC6600` | Cabine tombada | Cobre |
| **Congresso Silhueta** | `#1A1A18` | Congresso ao fundo | Quase preto |
| **Congresso Brilho** | `#3D6B3A` | Luz sinistra do Congresso | Pulsa |
| **Palanque Madeira** | `#6B4423` | Palco eleitoral | Madeira barata |
| **Bandeira Rasgada** | `#CC0000` + `#009739` + `#FEDD00` | Bandeiras no palanque | Todas misturadas, nenhuma inteira |

---

## 5. Paleta Politica (APARTIDARISMO)

**REGRA: Estas cores NUNCA aparecem isoladas identificando um lado. Sempre aparecem JUNTAS ou MISTURADAS.**

| Nome | Hex | Uso CORRETO | Uso PROIBIDO |
|---|---|---|---|
| **PT Vermelho** | `#CC0000` | Bandeira rasgada JUNTO com verde/amarelo | Zumbi identificado como "de esquerda" |
| **Bolsonaro Verde** | `#009739` | Bandeira rasgada JUNTO com vermelho | Zumbi identificado como "de direita" |
| **Bolsonaro Amarelo** | `#FEDD00` | Misturado com outras cores | Camisa amarela em zumbi especifico |
| **Azul Generico** | `#2A3A5A` | Terno de qualquer zumbi | Cor de partido especifico |

---

## 6. Paleta de UI/HUD

| Elemento | Hex | Logica |
|---|---|---|
| **Score/Combo** | `#F0C830` | Recompensa, conquista |
| **Vida/HP** | `#C83030` | Urgencia, pulsante |
| **Power-up Ativo** | `#40B840` | Acao disponivel |
| **Alerta de Wave** | `#D47820` | Transicao, atencao |
| **Texto Principal** | `#F0E8D8` | Sobre fundo escuro |
| **Critico/Headshot** | `#FFD700` | Destaque |
| **Debuff** | `#8A4A8A` | Efeito negativo, burocracia |
| **Onomatopeia** | `#FFFFFF` com outline `#1A1A18` | HIT! SLAP! THWACK! |

---

## 7. Paleta do Limbo (Game Over)

| Nome | Hex | Uso |
|---|---|---|
| **Void** | `#0A0A0A` | Fundo infinito |
| **Particula Limbo** | `#2A2A2A` alpha 40% | Particulas no escuro |
| **Podcast Light** | `#3D6B3A` | Luz do podcast flutuante |
| **Cadeira Glow** | `#D47820` | Brilho da cadeira flutuante |

---

## 8. Regras de Aplicacao

### Textura de Papel (Overlay Global)
Todos os tiles devem ter um overlay sutil de textura de papel:
- **Noise:** Gaussian, monocromatico, 3-5% opacity
- **Grain:** Fino, uniforme, simula impressao offset barata
- Isso remove o aspecto "digital limpo" e alinha com o estilo Andre Guedes

### Hachuras (Cross-Hatching)
Sombras em tiles NAO usam gradiente. Usam:
- Linhas diagonais 45deg, espacamento 2px, cor 20% mais escura que a base
- Cross-hatching para sombras mais densas
- Referencia visual: Robert Crumb, Ralph Steadman

### Linhas de Contorno
- **Silhueta de landmark:** 3-4px, cor `#1A1A18`
- **Detalhes internos:** 1-2px, variavel
- **NUNCA** uniforme — microvariacoes simulando mao humana

### Cores Nunca Puras
- Nenhum `#FF0000`, `#00FF00`, `#0000FF`
- Toda cor e "suja" — misturada com cinza/marrom
- Se a cor parece "digital", adicione 10% de `#5C5C55` e re-teste
