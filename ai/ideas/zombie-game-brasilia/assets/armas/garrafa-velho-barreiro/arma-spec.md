# Garrafa de Velho Barreiro Incendiaria — Arma Exclusiva do LULA

## Visao Geral

**Dono**: LULA (O Cachaceiro)
**Tipo**: Projetil em area (Molotov de cachaca)
**Subtipo**: Arremesso + Area of Effect + Debuff
**Dimensoes Sprite**: 32x32px (projetil em voo), 48x48px (explosao/poca no chao)
**Perspectiva**: Top-down levemente isometrica

---

## Descricao Visual

Uma garrafa de cachaca Velho Barreiro com rotulo visivel, pavio de pano aceso saindo do gargalo. A garrafa e marrom-escuro com rotulo amarelado-sujo (nao brilhante). O vidro e irregular, com bolhas e imperfeicoes — nao e uma garrafa bonita, e uma garrafa GROTESCA. O pavio e um pedaco de gravata vermelha PT que o Lula arrancou.

### Cores Hex
| Elemento | Cor | Hex |
|---|---|---|
| Vidro da garrafa | Marrom escuro sujo | #3B2610 |
| Vidro transparencia | Ambar turvo | #7A5C2E |
| Rotulo fundo | Amarelo desbotado | #C4A840 |
| Rotulo texto | Vermelho escuro | #6B0F0F |
| Liquido interno | Ambar dourado sujo | #B8860B |
| Pavio (gravata PT) | Vermelho desbotado | #8B1A1A |
| Chama do pavio | Laranja/amarelo | #FF6B00 / #FFD700 |
| Fumaca | Cinza esverdeado | #5A5A4A |
| Poca de fogo | Laranja com azul de cachaca | #CC5500 / #3355AA |
| Vidro quebrado | Marrom claro | #8B6914 |

---

## Estados da Arma

### 1. Em Mao (Idle) — 2 frames loop
- **Frame 1**: Lula segura a garrafa pela barriga com a mao esquerda (4 dedos). Garrafa inclinada 15 graus. Pavio apagado. Liquido visivel balancando.
- **Frame 2**: Mesma pose, liquido levemente deslocado (efeito balanco de bebado). Bolhas subindo no liquido.
- **Timing**: 500ms por frame (lento, preguicoso como o Lula)

### 2. Acendendo Pavio — 3 frames
- **Frame 1**: Lula aproxima um isqueiro BIC (vermelho PT) do pavio. Expressao de concentracao bebada (olhos semicerrados, lingua pra fora).
- **Frame 2**: Faisca do isqueiro. Particulas de fogo pequenas. Pavio comeca a pegar fogo.
- **Frame 3**: Pavio totalmente aceso. Chama laranja/amarela com particulas. Lula com sorriso malicioso. Fumaca subindo.
- **Timing**: 150ms, 100ms, 200ms (total 450ms)

### 3. Arremesso — 4 frames
- **Frame 1**: Lula puxa o braco para tras (windup). Garrafa atras da cabeca. Barriga empurra pra frente pelo momentum. Cicatriz craniana visivel.
- **Frame 2**: Braco no ponto mais alto. Garrafa acima da cabeca. Pavio deixando rastro de fumaca.
- **Frame 3**: Arremesso! Braco estendido para frente. Garrafa saindo da mao (4 dedos se abrem). Corpo inclinado pelo esforco — barriga balanca.
- **Frame 4**: Follow-through. Lula cambaleando pelo peso do arremesso (bebado). Quase cai. Mao vazia.
- **Timing**: 120ms, 80ms, 60ms, 200ms (total 460ms — arremesso rapido, recovery lento)

### 4. Projetil em Voo — 4 frames loop (32x32px)
- **Frame 1**: Garrafa voando com rotacao. Pavio aceso deixando trilha de fumaca e particulas de fogo. Rotacao 0 graus.
- **Frame 2**: Rotacao 90 graus. Liquido visivel sloshing dentro. Trilha de fumaca mais longa.
- **Frame 3**: Rotacao 180 graus (de cabeca pra baixo). Liquido escorrendo pro gargalo. Chama mais intensa.
- **Frame 4**: Rotacao 270 graus. Ultimo momento antes do impacto. Chama maxima.
- **Timing**: 80ms por frame (rotacao rapida, estilo cartoon)
- **Velocidade de projetil**: 280px/s
- **Alcance maximo**: 200px (curto — Lula nao tem forca, e alcolatra)

### 5. Impacto/Explosao — 6 frames (48x48px)
- **Frame 1**: Garrafa atinge o chao. Vidro comecando a rachar. Flash branco no ponto de impacto.
- **Frame 2**: EXPLOSAO! Vidro se estilhaca em 8-12 cacos. Cachaca se espalha em circulo. Fogo irrompe — chamas laranja/azul (cachaca queima azulado). Rotulo "Velho Barreiro" voando como shrapnel.
- **Frame 3**: Chamas no maximo. Circuito de fogo de 48px de diametro. Fumaca densa subindo. Cacos de vidro no ar. Poca de liquido flamejante no centro.
- **Frame 4**: Chamas diminuindo levemente. Poca de cachaca em chamas no chao (forma irregular, 40px). Fumaca escurecendo. Cheiro visivel (linhas onduladas verdes saindo da poca — representando fedor de cachaca).
- **Frame 5**: Fogo menor, poca persistente. Cacos de vidro pousando no chao. Fumaca dispersando.
- **Frame 6**: Poca residual de cachaca em chamas (24px). Chamas baixas, azuladas. Vai persistir por 4 segundos como hazard de area.
- **Timing**: 60ms, 100ms, 150ms, 200ms, 200ms, 300ms (total 1010ms)

### 6. Poca Persistente (Hazard) — 3 frames loop (48x48px)
- **Frame 1**: Poca de cachaca flamejante no chao. Chamas baixas azul/laranja. Bolhas de fermentacao. Linhas onduladas de cheiro.
- **Frame 2**: Chamas tremelicando. Bolhas estourando. Fumacinha subindo.
- **Frame 3**: Chamas quase apagando, reavivam. Poca levemente menor.
- **Timing**: 300ms por frame (loop lento)
- **Duracao total da poca**: 4000ms (4 segundos)
- **Dano**: 5 HP/s para quem pisar
- **Debuff**: Controles invertidos por 3000ms ("bebado")

---

## Efeitos de Particula

### Fogo do Pavio
- 2-4 particulas por frame
- Cores: #FF6B00 (laranja), #FFD700 (amarelo), #FF4500 (vermelho)
- Tamanho: 2-4px
- Lifetime: 300ms
- Direcao: para cima com leve wind

### Fumaca de Trilha
- 1-2 particulas por frame durante voo
- Cor: #5A5A4A (cinza esverdeado)
- Tamanho: 3-6px (cresce ao dissipar)
- Lifetime: 600ms
- Opacity: 0.6 -> 0.0

### Explosao
- 15-20 particulas no frame de impacto
- Mix de fogo (#FF6B00), vidro (#8B6914), cachaca (#B8860B)
- Tamanho: 2-8px (variado)
- Lifetime: 400-800ms
- Direcao: radial 360 graus

### Fedor (Linhas de Cheiro)
- 3 particulas sinusoidais subindo da poca
- Cor: #4A7A3A (verde doentio)
- Formato: linhas onduladas (sine wave)
- Lifetime: 1000ms
- Opacity: 0.3 -> 0.0

---

## Audio Sincronizado

| Evento | Som | Duracao | Trigger |
|---|---|---|---|
| Acender pavio | click de isqueiro + fwoosh | 400ms | Frame 2 do acendimento |
| Arremesso | whoosh com grunt do Lula | 300ms | Frame 3 do arremesso |
| Voo | whistle descendente + crackle de fogo | loop 80ms | Durante projetil |
| Impacto | CRASH de vidro + WHOOMPF de fogo | 600ms | Frame 1 da explosao |
| Poca ativa | crackle de fogo baixo + borbulhar | loop 300ms | Durante hazard |
| Debuff aplicado | "Companheiro alcool em mim!" (Lula rindo) | 1200ms | Quando inimigo pisa |
| Bordao de arremesso | "Vai uma Velho Barreiro, companheiro!" | 1500ms | Random 30% no arremesso |

---

## Interacoes Especiais

### Com Bolsonaro
- Se a garrafa acertar Bolsonaro diretamente: dano 2x + Bolsonaro grita "VAGABUNDO!" + animacao especial de Bolsonaro pegando fogo
- A poca de cachaca faz Bolsonaro tropecar (stun 1s adicional)

### Com Daciolo
- A "Fumaca Santa" de Daciolo APAGA o fogo da poca instantaneamente
- "Essa cachaca nao tem poder contra a fe, GLORIA A DEUS!"

### Com BolsoLula
- Acerta so a metade Lula: Lula absorve (cachaca = cura 10% HP)
- Acerta so a metade Bolsonaro: dano 1.5x (Bolsonaro nao bebe)
- Acerta no centro (fusao): explosao dupla — 2x area, 2x duracao

---

## Upgrade Path

| Nivel | Nome | Efeito | Visual |
|---|---|---|---|
| 1 | Velho Barreiro Original | Dano base, poca 4s | Garrafa normal |
| 2 | Velho Barreiro Gold | +25% dano, poca 5s | Rotulo dourado |
| 3 | Edicao Companheira | +50% dano, poca 6s, debuff 4s | Rotulo vermelho PT com estrela |
| 4 | Reserva Especial do Planalto | +100% dano, poca 8s, debuff 5s, area 1.5x | Garrafa com faixa presidencial |
