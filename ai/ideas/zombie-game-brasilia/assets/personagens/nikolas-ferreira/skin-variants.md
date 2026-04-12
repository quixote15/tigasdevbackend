# Nikolas Ferreira (O Influencer-Politico) - Skin Variants

## Visao Geral
Cada skin modifica a aparencia visual do Nikolas mantendo a silhueta base (64x64px), as deformidades anatomicas (polegar enorme, pescoco curvado) e as animacoes. Todas as skins devem manter o estilo grotesco Andre Guedes / underground comix.

---

## SKIN 1: NORMAL (Default)
**Nome in-game:** "O Influencer"
**Unlock:** Disponivel desde o inicio

### Descricao Visual
- Visual padrao conforme sprite-spec.md
- Camiseta branca de influencer, calca escura
- Cabelo excessivamente arrumado com gel
- Celular preto com tela azul brilhante
- Ring light branco-quente como aureola
- Numeros de views verdes e vermelhos flutuando
- Polegar ENORME na mao direita
- Pescoco curvado 45 graus
- Expressao de deboche permanente

### Paleta
- Paleta padrao conforme sprite-spec.md
- Tons de pele bronzeada (ring light tan), roupa branca/preta, ring light quente

---

## SKIN 2: ZOMBIE
**Nome in-game:** "O Influencer Morto-Vivo"
**Unlock:** Completa a fase do Congresso

### Descricao Visual
- Pele esverdeada/acinzentada com manchas de decomposicao
- RING LIGHT QUEBRADO: metade do circulo faltando, fios expostos, luz piscando intermitente
- TELA RACHADA: celular com tela quebrada mas AINDA FUNCIONANDO (ele ainda filma)
- Polegar ENORME agora com unha preta e pele descascando -- MAIS GROTESCO ainda
- Cabelo parcialmente caindo, gel derretido misturado com sangue
- Um olho saindo da orbita (mas olhando a tela mesmo assim)
- Roupa rasgada, manchas de sangue seco
- Numeros de views agora sao VERMELHOS ESCURO (sangue) com texto glitchado
- Expressao de deboche PERSISTE mesmo como zumbi (o algoritmo nunca morre)

### Paleta Delta (mudancas da paleta base)
| Element              | Normal        | Zombie        |
|----------------------|---------------|---------------|
| Skin Base            | `#D4A574`     | `#7A9B6E`     |
| Skin Shadow          | `#A67B5B`     | `#4A6B3E`     |
| Hair                 | `#1A1A1A`     | `#2A1A1A`     |
| Shirt                | `#F0EDE8`     | `#C0B8A0`     |
| Ring Light           | `#FFFDE0`     | `#FF4040`     |
| Views Numbers        | `#00FF41`     | `#8B0000`     |
| Phone Screen         | `#4A90D9`     | `#3A6040`     |
| Blood Stains         | N/A           | `#8B0000`     |
| Rot Spots            | N/A           | `#4A3A20`     |

### Efeitos Especiais Unicos
- Ring light pisca irregularmente (ON 200ms, OFF 100ms, ON 50ms, OFF 300ms)
- Particulas de carne/pele caem do polegar enorme ocasionalmente
- Tela do celular tem linhas de glitch horizontal (scanlines verdes)
- Numeros de views ocasionalmente mostram "BRAINS" em vez de numeros

---

## SKIN 3: SPECIAL - "CANCELADO"
**Nome in-game:** "O Cancelado"
**Unlock:** Atinge 1 milhao de pontos em uma unica partida

### Descricao Visual
- Visual base intacto MAS coberto de marcas de "CANCELAMENTO"
- Grande X VERMELHO sobre o rosto (como selo de cancelado)
- Celular com tela mostrando "CONTA SUSPENSA" permanentemente
- Ring light VERMELHO (nao branco -- luz de alerta/perigo)
- Numeros de views sao NEGATIVOS: "-1M", "-500K", "👎 99%"
- Camiseta agora tem estampa "CANCELADO" em fonte de carimbo vermelho
- Expressao mudou de deboche para DESESPERO MASCARADO DE DEBOCHE
- Polegar enorme com band-aid (de tanto scrollar tentando recuperar a conta)
- Nuvens de thumbs-down (👎) flutuando em vez de views

### Paleta Delta
| Element              | Normal        | Cancelado     |
|----------------------|---------------|---------------|
| Ring Light           | `#FFFDE0`     | `#FF2020`     |
| Views Numbers        | `#00FF41`     | `#FF0000`     |
| Cancel X             | N/A           | `#CC0000`     |
| Shirt Detail         | N/A           | `#CC0000`     |
| Thumb Band-Aid       | N/A           | `#F5DEB3`     |

### Efeitos Especiais Unicos
- Thumbs-down (👎) flutuam no lugar dos numeros de views
- Ring light vermelho pulsa como sirene de alarme
- Ocasionalmente, um "RATIO" aparece acima da cabeca como dano recebido
- Ataque Flash agora mostra "EXPOSED!" em vez de "GRAVA!"
- Na morte, em vez de "SEM SINAL" mostra "CONTA DELETADA PERMANENTEMENTE"

---

## SKIN 4: EASTER EGG - "DEEPFAKE NIKOLAS"
**Nome in-game:** "O Deepfake"
**Unlock:** Encontra o QR code secreto na fase da Esplanada

### Descricao Visual
- O ROSTO GLITCHA constantemente -- a cada 2-3 segundos o rosto muda para outro politico por 1 frame
- Efeito de deepfake digital: pixels soltos ao redor do rosto, bordas do rosto tremendo
- Corpo intacto mas com artefatos digitais (blocos de pixels coloridos aleatorios)
- Celular mostra diferentes rostos na tela (gerando deepfakes em tempo real)
- Ring light agora e MULTICOLORIDO (RGB gamer -- vermelho, verde, azul, ciclo rapido)
- Polegar enorme PIXELADO (como se estivesse em baixa resolucao)
- Numeros de views sao ABSURDOS: "999T", "∞", "NaN", "OVERFLOW"
- Expressao muda com o glitch: deboche -> surpresa -> raiva -> deboche (ciclo)
- Linhas de scanline horizontal passam pelo corpo a cada 500ms

### Paleta Delta
| Element              | Normal        | Deepfake      |
|----------------------|---------------|---------------|
| Ring Light           | `#FFFDE0`     | RGB cycle     |
| Views Numbers        | `#00FF41`     | `#00FFFF`     |
| Glitch Artifacts     | N/A           | `#FF00FF`     |
| Pixel Blocks         | N/A           | Random        |
| Scanlines            | N/A           | `#00FF00` 20% |

### Efeitos Especiais Unicos
- Face swap glitch: a cada 2-3s, rosto muda para 1 frame de outro personagem
- RGB ring light cicla cores (R->G->B) a cada 200ms
- Particulas de pixels soltos flutuam ao redor do personagem
- Scanlines horizontais passam pelo sprite periodicamente
- Ataque Flash gera um "deepfake" do alvo por 1s (alvo fica com rosto glitchado)
- Na morte, o personagem "desrenderiza" -- desintegra em blocos de pixels
- Numeros de views mostram valores impossiveis ("∞", "NaN", "SEGFAULT")

---

## Notas de Implementacao

### Troca de Skin
```javascript
// Carregar skin alternativa
this.load.spritesheet('nikolas_idle_zombie', 'assets/personagens/nikolas-ferreira/skins/zombie/nikolas_idle.png', { frameWidth: 64, frameHeight: 64 });

// Trocar skin em runtime
function setSkin(nikolas, skinName) {
    const prefix = skinName === 'normal' ? 'nikolas' : `nikolas_${skinName}`;
    nikolas.play(`${prefix}_idle`);
}
```

### Prioridade de Producao
1. **Normal** -- essencial, primeiro a ser produzido
2. **Zombie** -- segundo, necessario para fases avancadas
3. **Cancelado** -- terceiro, reward de progressao
4. **Deepfake** -- ultimo, easter egg (menor prioridade)

### Regras Visuais para TODAS as Skins
1. O POLEGAR ENORME deve ser visivel e grotesco em TODAS as skins
2. O celular NUNCA e removido (mesmo na zombie, ele continua filmando)
3. O ring light (ou variante) esta SEMPRE presente
4. O pescoco curvado e permanente em todas as skins
5. Contornos grossos 2px e estilo underground comix em todas
6. A deformidade e a piada -- cada skin INTENSIFICA, nunca diminui
