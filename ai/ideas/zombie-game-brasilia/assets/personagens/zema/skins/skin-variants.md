# Zema (O Privatizador / "Sera?") - Skin Variants

## Visao Geral
Cada skin modifica a aparencia visual do Zema mantendo a silhueta base (64x64px), as deformidades (pupilas de numeros, maos de privatizacao) e as animacoes. O desafio artistico de Zema: ele e LIMPO no estilo SUJO -- cada skin deve manter essa tensao.

---

## SKIN 1: NORMAL (Default)
**Nome in-game:** "O Governador-CEO"
**Unlock:** Disponivel desde o inicio

### Descricao Visual
- Visual padrao conforme sprite-spec.md
- Terno azul escuro perfeitamente cortado, sem rugas
- Cabelo impecavel de executivo
- Calculadora no bolso do paleto, display verde
- Pupilas = numeros verdes LED
- Sorriso frio permanente
- Sapatos sociais brilhando
- Postura excessivamente ereta

### Paleta
- Paleta padrao conforme sprite-spec.md
- Tons frios e corporativos, azul escuro, verde LED, dourado nos cifroes

---

## SKIN 2: ZOMBIE
**Nome in-game:** "O CEO Morto-Vivo"
**Unlock:** Completa a fase de Belo Horizonte

### Descricao Visual
- Pele esverdeada/acinzentada MAS ele ainda TENTA manter a compostura
- Terno: sujo com manchas de sangue e terra, MAS ele continua ajustando a gravata (gesto)
- Cabelo: parcialmente caindo, mas ele PENTEIA o que sobrou (perturbador)
- Calculadora: rachada, display com glitch, mas AINDA FUNCIONA
- Pupilas-numeros: verdes MAS com static/glitch ocasional ("Err.0r")
- Sorriso frio PERSISTE mesmo com mandibula parcialmente deslocada
- Um osso exposto no braco MAS ele usa o braco normalmente
- Sapatos: sujos mas ele TENTA limpar (manchas de sangue que ele ignora)
- Postura: AINDA ereta, mas com leve tremor zombificado que ele reprime

### Paleta Delta
| Element              | Normal        | Zombie        |
|----------------------|---------------|---------------|
| Skin Base            | `#E8D0B8`     | `#8BA87A`     |
| Skin Shadow          | `#C4A882`     | `#5A7A4A`     |
| Suit Dark Blue       | `#1A2744`     | `#1A2244`     |
| Suit Stains          | N/A           | `#4A1010`     |
| Hair                 | `#3A2A1A`     | `#3A3A2A`     |
| Calculator Display   | `#00FF41`     | `#00AA30`     |
| Blood Stains         | N/A           | `#6B0000`     |
| Bone Exposed         | N/A           | `#E0D8C0`     |
| Rot Patches          | N/A           | `#4A5A30`     |

### Efeitos Especiais Unicos
- Tremor zombificado que ele SUPRIME: a cada 3s, corpo treme 1px e volta (ele se controla)
- Display da calculadora tem glitch: a cada 5s, numeros ficam estaticos por 200ms
- Pupilas-numeros ocasionalmente mostram "BRAINS" por 1 frame antes de voltar
- Ao caminhar, deixa rastro de sangue sutil (ao inves de so cifroes)
- Selo "PRIVATIZADO" agora tem manchas de sangue
- Na morte: o tremor finalmente VENCE -- corpo convulsiona antes de ficar imovel

---

## SKIN 3: SPECIAL - "PRIVATIZADOR SUPREMO"
**Nome in-game:** "O Privatizador Supremo"
**Unlock:** Privatiza 100 objetos em uma unica partida

### Descricao Visual
- Terno agora e DOURADO (gold suit -- #FFD700 base com #B8860B sombras)
- Gravata feita de notas de dinheiro
- Calculadora DOURADA com display VERMELHO (LED vermelho em vez de verde)
- Pupilas-numeros agora sao DOURADAS (#FFD700) em vez de verdes
- Tudo ao redor de Zema ja tem cifroes -- o ar ao redor dele tem particulas de dinheiro
- Coroa de cifrao ($) sutil acima da cabeca (como uma coroa de rei)
- Sapatos dourados brilhando excessivamente
- Cabelo com gel dourado (brilho exagerado)
- Sorriso frio agora e sorriso de POSSE (ele ja privatizou tudo)
- Aura dourada sutil ao redor do corpo (2px glow)

### Paleta Delta
| Element              | Normal        | Privatizador Supremo |
|----------------------|---------------|----------------------|
| Suit                 | `#1A2744`     | `#FFD700`            |
| Suit Shadow          | `#0E1A30`     | `#B8860B`            |
| Tie                  | `#8B1A1A`     | `#228B22`            |
| Calculator           | `#1A1A1A`     | `#FFD700`            |
| Calc Display         | `#00FF41`     | `#FF0000`            |
| Pupil Numbers        | `#00FF41`     | `#FFD700`            |
| Dollar Signs         | `#FFD700`     | `#FFD700` (glow +)   |
| Crown                | N/A           | `#FFD700`            |
| Aura                 | N/A           | `#FFD700` 20%        |

### Efeitos Especiais Unicos
- Particulas de dinheiro flutuam permanentemente ao redor (como neve dourada)
- Coroa de cifrao ($) paira acima da cabeca, girando lentamente
- Onda de privatizacao do special e 30% MAIOR em raio
- Selo "PRIVATIZADO" agora e dourado em vez de vermelho
- Objetos privatizados brilham dourado
- Na morte: ouro vira cinza/chumbo, coroa cai e quebra
- Footstep trail: pegadas douradas em vez de cifroes sutis

---

## SKIN 4: EASTER EGG - "REI MIDAS MINEIRO"
**Nome in-game:** "O Midas"
**Unlock:** Completa o jogo sem gastar nenhum ponto (score hoarding)

### Descricao Visual
- Visual MITOLOGICO distorcido: Zema como Rei Midas versao Minas Gerais
- Toga grega POR CIMA do terno (combinacao absurda: terno + toga)
- Pele com veios DOURADOS (como veios de ouro numa rocha -- referencia mineracao MG)
- Coroa de louros DOURADA, mas feita de cifroes entrelaçados
- Maos: COMPLETAMENTE DOURADAS (o toque de Midas e permanente, nao mais efeito visual)
- Pupilas-numeros: numeros ROMANOS em dourado ("XLVII", "MMXXVI")
- Barba dourada curta (ele normalmente nao tem, mas Midas tinha)
- Calculadora substituida por um ABACO dourado flutuante
- Sapatos: sandalia grega dourada (absurdo sobre as meias sociais)
- Tudo que toca vira LITERALMENTE dourado (nao so cifrao -- a textura muda)

### Paleta Delta
| Element              | Normal        | Midas         |
|----------------------|---------------|---------------|
| Skin Base            | `#E8D0B8`     | `#E8D0B8`     |
| Skin Veins           | N/A           | `#FFD700`     |
| Suit                 | `#1A2744`     | `#1A2744`     |
| Toga                 | N/A           | `#F5F0E0`     |
| Hands                | `#E8D0B8`     | `#FFD700`     |
| Crown                | N/A           | `#FFD700`     |
| Beard                | N/A           | `#DAA520`     |
| Pupil Numbers        | `#00FF41`     | `#FFD700`     |
| Abacus               | N/A           | `#FFD700`     |
| Sandals              | N/A           | `#DAA520`     |
| Touch Effect         | `#FFD700`     | Full gold texture |

### Efeitos Especiais Unicos
- TOQUE DE MIDAS: tudo que toca vira textura dourada completa (nao so cifrao)
- Abaco dourado flutuante substitui calculadora (contas se movem sozinhas)
- Numeros romanos nas pupilas mudam mais devagar (gravidade classica)
- Ao caminhar: chao vira dourado temporariamente nas pegadas
- Toga balanca com o movimento (physics simples de cloth)
- Na morte: "maldicao do Midas" -- ele se transforma completamente em ouro (estatua)
- A estatua dourada persiste no cenario como decoracao (nao desaparece)
- Special: em vez de onda dourada, ondas SISMICAS de ouro transformam o cenario inteiro

---

## Notas de Implementacao

### Troca de Skin
```javascript
this.load.spritesheet('zema_idle_zombie', 'assets/personagens/zema/skins/zombie/zema_idle.png', { frameWidth: 64, frameHeight: 64 });

function setSkin(zema, skinName) {
    const prefix = skinName === 'normal' ? 'zema' : `zema_${skinName}`;
    zema.play(`${prefix}_idle`);
}
```

### Prioridade de Producao
1. **Normal** -- essencial, primeiro a ser produzido
2. **Zombie** -- segundo, necessario para fases avancadas
3. **Privatizador Supremo** -- terceiro, reward de progressao
4. **Rei Midas Mineiro** -- ultimo, easter egg (menor prioridade)

### Regras Visuais para TODAS as Skins
1. PUPILAS DE NUMEROS devem ser visiveis em todas as skins (formato pode variar)
2. O efeito de cifrao/privatizacao ao tocar e SEMPRE presente
3. A postura EXCESSIVAMENTE ERETA e permanente em todas as skins
4. O SORRISO FRIO (ou variante) esta sempre presente
5. A calculadora (ou substituto) esta sempre acessivel
6. Contornos grossos 2px e estilo underground comix em todas
7. A TENSAO entre limpeza do personagem e sujeira do mundo deve persistir
8. Na skin Zombie, o humor e ele TENTANDO manter a compostura (e falhando sutilmente)
