# ALCKMIN (Alcool em Mim) - Skin Variants

## Overview
Todas as skins usam a mesma base de sprite sheet (64x64px) com as mesmas animacoes. As diferencas sao APENAS visuais: paleta de cores, acessorios e detalhes. A silhueta base (costas curvadas, bracos longos, sorriso permanente) se mantem em TODAS as skins.

---

## Skin 1: Normal (Mordomo Subserviente)
**Skin padrao -- desbloqueada desde o inicio**

### Descricao Visual
O Alckmin classico. Camisa branca de mordomo encardida, calca preta social, aventalzinho marrom curto (ridiculamente pequeno), bandeja de cafe bege com xicara fumegante. Cabelo preto impecavelmente penteado com gel. Sorriso perturbador permanente. Costas curvadas 40 graus. Bracos longos ate abaixo dos joelhos. Pescoco inclinado 30 graus para cima. Sapatos sociais pretos lustrados.

### Paleta
| Elemento          | Hex       |
|-------------------|-----------|
| Camisa            | `#E8E5DA` |
| Calca             | `#1A1A1A` |
| Avental           | `#6B4226` |
| Bandeja           | `#C8A96E` |
| Cafe              | `#3E1F0D` |
| Cabelo            | `#1E1E1E` |
| Pele              | `#E0B898` |
| Sapatos           | `#0D0D0D` |

### Sprite Sheet Key
```
npc_alckmin_idle_normal
npc_alckmin_walk_normal
npc_alckmin_attack_normal
npc_alckmin_death_normal
npc_alckmin_hit_normal
npc_alckmin_special_normal
```

### Notas
- Skin de referencia -- todas as specs de animacao se baseiam nesta
- O avental deve parecer CURTO DEMAIS -- como se ele tivesse pego o tamanho errado
- A bandeja tem leve reflexo metalico (1px de highlight)

---

## Skin 2: Presidente Interino 2026
**Desbloqueio: Completar 3 waves sem o Lula**

### Descricao Visual
EXATAMENTE o mesmo visual do Normal, MAS com uma faixa presidencial verde-amarela no peito. A piada: a faixa e tao DISCRETA e MAL COLOCADA que ninguem percebe. Ela esta torta, parcialmente coberta pelo avental, quase caindo. O proprio Alckmin parece nao ter certeza se esta usando a faixa ou nao. O sorriso e o mesmo, mas os olhos tem um BRILHO SUTIL de orgulho (que ninguem nota).

### Diferencas da Skin Normal
- **Faixa presidencial:** Verde (#2E7D32) com faixa central amarela (#F9A825), colocada TORTA no peito, parcialmente sob o avental
- **Micro-detalhe:** Crachá "PRESIDENTE (interino) (temporario) (provisorio)" em fonte minuscula (1-2px) no bolso
- **Olhos:** 1px de highlight branco extra (brilho de orgulho contido)
- **Postura:** IDENTICA -- as costas continuam curvadas. Nem a presidencia endireita esse homem
- **Bandeja:** Agora tem uma xicara EXTRA (cafe para si mesmo? nao, e pro proximo presidente)

### Paleta Adicional
| Elemento              | Hex       |
|-----------------------|-----------|
| Faixa verde           | `#2E7D32` |
| Faixa amarela         | `#F9A825` |
| Cracha texto          | `#666666` |
| Highlight orgulho     | `#FFFFFF` |

### Animacoes Modificadas
- **Idle especial:** A faixa escorrega 1px a cada ciclo de idle. No frame 3, esta quase caindo. No frame 0, volta (ele ajusta discretamente)
- **Death:** A faixa cai antes do corpo. Ninguem a pega. Um texto micro aparece: "A faixa esta disponivel"
- **Special:** Durante Mordomo Supremo, a faixa SAI completamente (prioridade e servir, nao governar)

### Sprite Sheet Key
```
npc_alckmin_idle_interino
npc_alckmin_walk_interino
npc_alckmin_attack_interino
npc_alckmin_death_interino
npc_alckmin_hit_interino
npc_alckmin_special_interino
```

### Efeito Unico
- A cada 30 segundos, texto flutuante aparece por 2s: "Alckmin esta governando" em fonte 6px, cor #888888, alpha 0.3 (quase invisivel)
- NPCs NAO mudam de comportamento durante a interinidade
- Se o jogador tentar interagir especificamente com a faixa: "Ela esta so de passagem"

---

## Skin 3: Zombie Mordomo
**Desbloqueio: Alckmin morre 10 vezes no total**

### Descricao Visual
Alckmin ZUMBIFICADO, mas CONTINUA SERVINDO CAFE. A pele esta cinza-esverdeada. Pedacos do rosto faltam (mas o SORRISO permanece intacto -- os dentes estao expostos porque o labio superior se decompoe). O cabelo continua PERFEITAMENTE PENTEADO apesar de ter fungos crescendo nele. O avental esta rasgado e ensanguentado. A camisa tem buracos com costelas visiveis. A bandeja esta enferrujada MAS o cafe esta fresco (o cafe NUNCA morre). Os bracos ficaram AINDA MAIS longos (decomposicao esticou os tendoes). As costas curvaram MAIS (gravidade + decomposicao). Os olhos sao brancos, sem pupila, mas o sorriso e IDENTICO.

### Diferencas da Skin Normal
- **Pele:** De `#E0B898` para `#7A8C6E` (cinza-esverdeado zumbi)
- **Camisa:** Rasgada, com manchas verdes e marrons de decomposicao. Buracos mostrando costelas
- **Avental:** Rasgado em 3 pontos, manchas de sangue seco marrom-escuro
- **Cabelo:** Mesmo penteado MAS com 2-3px de musgo verde crescendo
- **Dentes:** Mais expostos (labio superior parcialmente decomposto), amarelados
- **Olhos:** Brancos sem pupila (zumbi padrao)
- **Bandeja:** Enferrujada (`#8B4513` com manchas `#6B3410`), mas cafe INTACTO
- **Xicara:** Rachada mas funcional
- **Bracos:** 4px mais longos que o normal (esticaram na decomposicao)
- **Postura:** 5 graus MAIS curvada (gravidade vencendo)
- **Andar:** 20% mais lento, com leve arrasto no pe esquerdo

### Paleta
| Elemento              | Hex       |
|-----------------------|-----------|
| Pele zumbi            | `#7A8C6E` |
| Pele zumbi (shadow)   | `#5A6C4E` |
| Sangue seco           | `#4A1A0A` |
| Musgo                 | `#3D5C2A` |
| Bandeja enferrujada   | `#8B4513` |
| Ferrugem              | `#6B3410` |
| Osso exposto          | `#D4C5A9` |
| Olhos zumbi           | `#E8E8E8` |
| Dentes amarelados     | `#D4C490` |

### Animacoes Modificadas
- **Idle:** Alem do tremor da bandeja, a cabeca PENDE 2px para o lado a cada ciclo (musculatura deteriorada)
- **Walk:** Pe esquerdo arrasta (1px drag trail). Velocidade 80% da normal
- **Attack:** O cafe lancado agora e VERDE (contaminado) -- causa poison damage (2 HP/s por 3s)
- **Hit:** O sorriso NAO quebra (os musculos faciais travaram na decomposicao)
- **Death:** Cai e se LEVANTA de novo apos 5 segundos (e um zumbi, afinal). Maximo 3 resurrections
- **Special:** Identico mas com particulas verdes em vez de douradas

### Sprite Sheet Key
```
npc_alckmin_idle_zombie
npc_alckmin_walk_zombie
npc_alckmin_attack_zombie
npc_alckmin_death_zombie
npc_alckmin_hit_zombie
npc_alckmin_special_zombie
```

### Efeito Unico
- Cafe verde causa **Poison** em vez de dano direto (mais util contra bosses)
- Inimigos zumbis IGNORAM o Alckmin zumbi (acham que e um deles -- e de certa forma e)
- A cada 20 segundos, geme: "Caaaafeeeee..." (gemido de zumbi + desejo de servir)
- Resurreicao: Apos "morrer", fica caido 5s e levanta com 30% HP. Maximo 3x por wave

---

## Skin 4: Barista Premium
**Desbloqueio: Servir 100 cafes no total (Cafe Revigorante)**

### Descricao Visual
Alckmin em modo CAFE GOURMET. Aventalzinho de mordomo substituido por avental de barista de cafe especial (preto, longo, com logo "Cafe do Vice" bordado). Maquina de espresso portatil nas costas (tipo mochila). A bandeja foi substituida por um porta-copos de madeira nobre com 3 xicaras diferentes (espresso, cappuccino, latte). Usa uma boina francesa preta. O sorriso continua IDENTICO mas agora tem bigodinho fino (pretensioso). Luvas brancas de barista. O cabelo esta MAIS penteado (se possivel). As costas estao curvadas do peso da maquina de espresso.

### Diferencas da Skin Normal
- **Avental:** Preto longo (`#1A1A1A`) com logo "Cafe do Vice" em dourado (`#C8A040`) bordado no peito
- **Boina:** Boina francesa preta no topo da cabeca (4x4px)
- **Maquina de espresso:** Mochila metalica prateada (`#B0B0B0`) nas costas com tubos e manometro
- **Bandeja -> Porta-copos:** Madeira nobre (`#5C3A1E`) com 3 xicaras de tamanhos diferentes
- **Luvas:** Brancas (`#F0F0F0`) nas maos (elegancia barista)
- **Bigodinho:** Fino, pretensioso (2px preto sob o nariz)
- **Expressao:** Sorriso com LEVE ar de superioridade (nao mais 100% subserviente -- agora 90% subserviente, 10% snob)

### Paleta Adicional
| Elemento              | Hex       |
|-----------------------|-----------|
| Avental barista       | `#1A1A1A` |
| Logo dourado          | `#C8A040` |
| Maquina metal         | `#B0B0B0` |
| Maquina (shadow)      | `#808080` |
| Porta-copos madeira   | `#5C3A1E` |
| Luvas brancas         | `#F0F0F0` |
| Boina                 | `#1A1A1A` |
| Bigodinho             | `#1A1A1A` |
| Espresso crema        | `#C49040` |
| Cappuccino foam       | `#F5E6D0` |
| Latte art             | `#E8D4B8` |

### Animacoes Modificadas
- **Idle:** Em vez de tremor simples, a maquina de espresso nas costas VIBRA e solta vapor (particulas metalicas)
- **Walk:** Mais lento (peso da maquina) mas MAIS elegante -- passos medidos de sommelier
- **Attack:** Lanca 3 tipos de cafe em sequencia (espresso = dano rapido, cappuccino = dano medio + slow, latte = dano menor + cura aliados na area)
- **Special:** "Barista Supremo" -- a maquina de espresso EXPLODE em acao, tubos saem e servem cafe para TODOS os aliados simultaneamente. Cura 25 HP em vez de 15
- **Death:** Cai, a maquina de espresso explode em pecas (parafusos, tubos, manometro). Ultimo cafe perfeito voa no ar e aterrissa INTACTO

### Sprite Sheet Key
```
npc_alckmin_idle_barista
npc_alckmin_walk_barista
npc_alckmin_attack_barista
npc_alckmin_death_barista
npc_alckmin_hit_barista
npc_alckmin_special_barista
```

### Efeito Unico
- **Cafe Triplo:** Attack dispara 3 projeteis em leque (espresso, cappuccino, latte) com efeitos diferentes
- **Cafe Revigorante+:** Cura 25 HP em vez de 15 (cafe gourmet e mais eficaz)
- **Aroma:** Aura passiva de 40px que dá buff de +5% velocidade para aliados proximos (o cheiro do cafe bom anima)
- Bordao unico: "Este e um blend single-origin, notas de chocolate com cereja, presidente"
- Bordao de morte: "O espresso... nao pode... morrer..." (sussurro dramatico)

---

## Skin 5: Alcool em Mim (Versao Etilica)
**Desbloqueio: Easter Egg -- interagir com Alckmin 10 vezes seguidas sem parar**

### Descricao Visual
A versao LITERAL do apelido "Alcool em Mim". Alckmin BEBADO. A bandeja de cafe foi substituida por uma GARRAFA de cachaca/pinga. O sorriso permanente agora parece de RESSACA (mesma forma, contexto diferente -- dentes a mostra de quem esta rindo de nada). Os olhos estao SEMI-FECHADOS (pior que subserviente -- etílico). O cabelo tem UM TUFO fora do lugar pela PRIMEIRA VEZ em qualquer skin (o alcool derrotou o gel). O andar e CAMBALEANTE -- oscila 4px para cada lado. O avental esta ao contrario e amarrado na cabeca como bandana. A camisa esta aberta mostrando uma camiseta por baixo escrita "VICE DA PINGA". Nariz VERMELHO (rosácea etílica). Gravata usada como faixa na testa.

### Diferencas da Skin Normal
- **Bandeja -> Garrafa:** Garrafa de cachaca verde-marrom (`#4A6B3A`) no lugar da bandeja, meio vazia
- **Xicara -> Copo:** Copinho de cachaca (2px, transparente)
- **Olhos:** Semi-fechados, com 1px vermelho (injecao)
- **Cabelo:** 1 TUFO fora do lugar (3px rebelde) -- revolucionario para o personagem
- **Nariz:** Vermelho (`#CC4444`) -- rosácea
- **Avental:** Amarrado na cabeca como bandana
- **Camisa:** Aberta, camiseta por baixo com "VICE DA PINGA" (micro-texto)
- **Gravata:** Na testa como faixa de guerra/festa
- **Postura:** Costas MAIS curvadas + oscilacao lateral constante
- **Expressao:** Sorriso IDENTICO mas com contexto de bebado feliz (sem dignidade)

### Paleta Adicional
| Elemento              | Hex       |
|-----------------------|-----------|
| Garrafa cachaca       | `#4A6B3A` |
| Garrafa (rotulo)      | `#F5E6B8` |
| Liquido cachaca       | `#D4A040` |
| Nariz vermelho        | `#CC4444` |
| Camiseta (base)       | `#E8E8E8` |
| Camiseta (texto)      | `#1A1A1A` |
| Olhos injectados      | `#CC3333` |
| Gravata na testa      | `#2C3E6B` |
| Bandana (avental)     | `#6B4226` |

### Animacoes Modificadas
- **Idle:** Oscilacao lateral constante (4px para esquerda, 4px para direita, loop). A garrafa balanca no ritmo oposto. Solucos visuais a cada 3 ciclos (corpo pula 2px)
- **Walk:** CAMBALEANTE -- path nao e reto, oscila em zig-zag. Velocidade 70% da normal. Cada passo tem delay aleatorio de 50-100ms. Os bracos balancam sem controle. A garrafa quase cai mas nunca cai
- **Attack:** Joga CACHACA nos inimigos. Splash amarelo-dourado. Causa dano + CONFUSAO (inimigo anda em direcao aleatoria por 2s). O vento do arremesso faz Alckmin girar 180 graus (desequilibrio)
- **Hit:** NAO reage ao hit (anestesia etílica). O corpo absorve o impacto como gelatina (squash-stretch exagerado). O sorriso CONTINUA (ele nao sentiu nada)
- **Death:** Cai, RONCA (zzz aparece), depois de 3 segundos acorda assustado, olha ao redor, e morre de novo. Loop 2x
- **Special:** "Alcool em TODOS" -- joga cachaca em area, TODOS (aliados E inimigos) ficam bebados por 3s. Aliados ganham +30% dano mas -20% precisao. Inimigos andam em circulos

### Sprite Sheet Key
```
npc_alckmin_idle_etilico
npc_alckmin_walk_etilico
npc_alckmin_attack_etilico
npc_alckmin_death_etilico
npc_alckmin_hit_etilico
npc_alckmin_special_etilico
```

### Efeitos Unicos
- **Andar Cambaleante:** Path do NPC oscila em onda senoidal (amplitude 4px, frequencia 0.5Hz)

```javascript
// Oscilacao de bebado
this.tweens.add({
    targets: alckmin,
    x: alckmin.x + 4,
    duration: 500,
    ease: 'Sine.easeInOut',
    yoyo: true,
    repeat: -1
});
```

- **Soluco Visual:** A cada 3s, o sprite pula 2px e volta (squash-stretch micro)

```javascript
// Soluco
this.time.addEvent({
    delay: 3000,
    callback: () => {
        this.tweens.add({
            targets: alckmin,
            y: alckmin.y - 2,
            scaleX: 1.05,
            scaleY: 0.95,
            duration: 50,
            yoyo: true
        });
    },
    loop: true
});
```

- **Garrafa Infinita:** Assim como a bandeja de cafe, a garrafa nunca acaba. Serve cachaca para sempre
- **Imunidade ao Frio:** Dano de gelo/frio reduzido em 50% (o alcool aquece)
- **Confusao em Area:** Projetil de cachaca cria zona de confusao (40px raio) por 2s
- Bordao principal: "Eu adoro esse nome... *hic*... alcool em mim!" (com soluco)
- Bordao de ataque: "To-toma uma, presidente... *hic*... companheiro!" 
- Bordao de morte: "Eu nao tava bebado... tava apenas... interinamente... *zzz*"

---

## Tabela Comparativa de Skins

| Aspecto        | Normal      | Interino    | Zombie      | Barista     | Etílico     |
|---------------|-------------|-------------|-------------|-------------|-------------|
| **Velocidade** | 100%        | 100%        | 80%         | 90%         | 70%         |
| **Dano cafe**  | 15 HP       | 15 HP       | 2 HP/s (3s) | 15/12/10 HP | 10 HP+confuse |
| **Cura**       | 15 HP       | 15 HP       | 15 HP       | 25 HP       | 0 (cachaca) |
| **Buff**       | Nenhum      | Nenhum      | Poison      | +5% speed   | +30% dmg/-20% acc |
| **Death**      | Fade+bandeja| Faixa cai   | Ressurge 3x | Maquina explode | Ronca+morre |
| **Sorriso**    | Subserviente| Orgulhoso   | Travado     | Snob        | Bebado      |
| **Cabelo**     | Perfeito    | Perfeito    | Com musgo   | Mais perfeito| 1 tufo rebel |
| **Projetil**   | Cafe preto  | Cafe preto  | Cafe verde  | 3 cafes     | Cachaca     |

---

## Phaser 3 Skin Swap

```javascript
// Sistema de troca de skin
class AlckminSkin {
    static NORMAL = 'normal';
    static INTERINO = 'interino';
    static ZOMBIE = 'zombie';
    static BARISTA = 'barista';
    static ETILICO = 'etilico';

    static loadSkin(scene, skinKey) {
        const animations = ['idle', 'walk', 'attack', 'death', 'hit', 'special'];
        const suffix = skinKey === AlckminSkin.NORMAL ? '' : `_${skinKey}`;

        animations.forEach(anim => {
            scene.load.spritesheet(
                `npc_alckmin_${anim}${suffix}`,
                `assets/personagens/alckmin/skins/${skinKey}/alckmin_${anim}.png`,
                { frameWidth: 64, frameHeight: 64 }
            );
        });
    }

    static applySkin(alckmin, skinKey) {
        alckmin.setData('currentSkin', skinKey);
        // Re-bind animations para a nova skin
        // Aplicar modificadores de stats
        switch (skinKey) {
            case AlckminSkin.ZOMBIE:
                alckmin.speedMultiplier = 0.8;
                alckmin.maxResurrections = 3;
                break;
            case AlckminSkin.BARISTA:
                alckmin.speedMultiplier = 0.9;
                alckmin.healAmount = 25;
                break;
            case AlckminSkin.ETILICO:
                alckmin.speedMultiplier = 0.7;
                alckmin.wobbleEnabled = true;
                break;
            default:
                alckmin.speedMultiplier = 1.0;
                break;
        }
    }
}
```

---

## Condicoes de Desbloqueio

| Skin             | Condicao                                   | Notificacao                                    |
|------------------|--------------------------------------------|------------------------------------------------|
| Normal           | Padrao                                     | --                                             |
| Interino 2026    | Completar 3 waves sem Lula no time         | "A faixa esta disponivel... alguem quer?"      |
| Zombie Mordomo   | Alckmin morre 10 vezes (acumulativo)       | "Ate morto ele serve cafe..."                  |
| Barista Premium  | Usar Cafe Revigorante 100 vezes            | "Alckmin fez um curso de barista!"             |
| Alcool em Mim    | Interagir com Alckmin 10x seguidas         | "Alcool em mim ativado! *hic*"                 |

---

## Notas para o Artista (Todas as Skins)
- O SORRISO e o elemento CONSTANTE em todas as skins -- mesmo zumbi, mesmo bebado, mesmo morto
- A curvatura das costas deve ser consistente (40 graus base, variando por skin)
- Os bracos longos sao MARCA REGISTRADA -- mantenha em todas as skins
- O cabelo so sai do lugar nas skins Zombie (musgo) e Etílico (1 tufo). Nas demais, TITANIO
- Cada skin deve ser reconhecivel em 64x64 a primeira vista -- use cores distintas
- Outlines grossas e irregulares (Crumb) em TODAS as skins
- Teste cada skin a 8-12 fps -- o feel jerky do Andre Guedes e OBRIGATORIO
