# LULA (O Cachaceiro) -- Skin Variants
### Boss Principal (Lado Esquerdo) | Zumbis de Brasilia
### Estilo: Andre Guedes (Grotesco/Underground Comix)

---

## Visao Geral de Skins

Todas as skins compartilham a mesma base de animacao (mesmos frames, mesmos timings). As diferencas sao puramente visuais: paleta de cores, acessorios, estado das roupas, e detalhes de superficie. O hitbox e comportamento de combate sao identicos entre skins.

**Total de skins**: 7 (1 base + 6 alternativas)
**Desbloqueio**: Skin base gratuita (boss padrao). Alternativas desbloqueadas por conquistas, loot, ou loja do jogo.

---

## SKIN 1: Normal / Base (Terno Amassado)
**ID**: `lula_normal`
**Desbloqueio**: Padrao (primeira aparicao no jogo)

### Descricao Visual Completa
O Lula classico do Andre Guedes. Terno cinza sujo e amassado, gravata vermelha PT torta, camisa parcialmente aberta revelando peito peludo. Barba branca desgrenhada, nariz bulboso vermelho, olhos semicerrados de bebado. Garrafa de Velho Barreiro na mao direita. Mao esquerda com 4 dedos (sem mindinho). Barriga de chope proeminente estourando os botoes da camisa. Cicatriz craniana 2026 com pontos de sutura e curativos parciais. Placa de titanio sob a pele com brilho metalico sutil.

### Paleta
| Elemento | Hex |
|----------|-----|
| Terno | #3D3D3D / #1A1A1A (sombra) |
| Gravata | #8B1A1A |
| Camisa | #D9D0C0 |
| Pele | #D4956B |
| Nariz | #CC3333 |
| Barba | #C8C8C8 |
| Sapatos | #2E1A0A |
| Garrafa | #2A5A2A |
| Cachaca | #CC8833 |
| Cicatriz | #8B4060 |
| Placa titanio | #8090A0 |

### Detalhes Especificos
- Terno: 3 vincos de amassado (linhas de sombra internas)
- Gravata: torta 10 graus para a esquerda, no desfeito
- Camisa: 2 botoes faltando no abdomen (barriga estica o tecido)
- Curativos: 1 faixa branca no topo do cranio, 1 band-aid na testa
- Pontos de sutura: 5 pontos pretos em linha no topo da cabeca

---

## SKIN 2: 2026 Frankenstein (Cicatriz Enfatizada)
**ID**: `lula_frankenstein`
**Desbloqueio**: Derrotar Lula pela primeira vez no modo historia

### Descricao Visual Completa
Versao que enfatiza o trauma craniano de 2026. A cicatriz craniana domina o visual -- costuras grossas cruzando o cranio inteiro (nao apenas uma linha, mas um padrao em X e linhas perpendiculares). Placa de titanio EXPOSTA com parafusos visiveis (pele nao fechou completamente). Curativos removidos, revelando incisoes cruas e avermelhadas. O resto do corpo e identico a skin base mas com um hospital bracelet no pulso direito e uma bata de hospital por baixo do terno (visivel na abertura da camisa). Expressao ligeiramente mais perturbada -- olhos um pouco mais arregalados que o normal, como quem sofreu trauma recente.

### Paleta (diferencas da base)
| Elemento | Hex | Mudanca |
|----------|-----|---------|
| Cicatriz principal | #AA3355 | Mais vermelha e inflamada |
| Cicatrizes secundarias | #993366 | Linhas cruzadas adicionais |
| Placa titanio | #A0B0C0 | Mais visivel/brilhante |
| Parafusos titanio | #666666 | Novos -- 4 pontos metalicos |
| Pele ao redor cicatriz | #CC5555 | Inflamacao intensa |
| Bata hospital | #E8E8F0 | Visivel sob terno |
| Pulseira hospital | #FFFFFF com texto #333333 | Novo acessorio |
| Pontos de sutura | #000000 | Mais grossos -- 2px em vez de 1px |

### Detalhes Especificos
- Cicatriz: padrao em forma de H no topo do cranio (2 linhas paralelas + 1 perpendicular)
- Placa de titanio: 6x4px visivel com 4 pontos de parafuso
- SEM curativos (foram removidos, ferida exposta)
- Pele ao redor dos cortes: inchada, avermelhada, com textura rugosa
- Hospital bracelet: fita branca de 4x1px no pulso direito com texto ilegivel
- Bata de hospital: visivel no peito (onde normalmente seria peito peludo, agora e tecido branco hospitalar)
- Expressao base: olhos 1px mais abertos que normal (trauma)
- Efeito especial: cicatriz pulsa (#AA3355 -> #CC4466 -> #AA3355) a cada 600ms (dor cronica)

### Animacao Extra
- Durante idle: mao esquerda (4 dedos) ocasionalmente vai a cabeca e toca a cicatriz (a cada 8-10s, micro-animacao de 200ms)
- Durante hit (headshot): particulas extras de faiscas na placa (#A0B0C0, 4-6 particulas)
- Som extra no headshot: `sfx/titanio_clank_reverb.ogg` -- versao com mais reverb

---

## SKIN 3: Zombie Premium
**ID**: `lula_zombie`
**Desbloqueio**: Completar o modo historia na dificuldade "Emenda 666"

### Descricao Visual Completa
Lula completamente zombificado. Pele verde-acinzentada de decomposicao com manchas escuras de necrose. Nariz bulboso AINDA MAIS EXAGERADO, agora roxo de putrefacao com textura de couve-flor. Um olho pendurado para fora da orbita por um fio de musculo (o outro semicerrado como sempre). Terno rasgado em multiplos pontos revelando costelas e carne exposta. Barriga de chope INCHADA com gases de decomposicao -- ainda maior que a normal, com coloracao esverdeada e veias visiveis na superficie. Barba com larvas (pixels brancos minusculos se movendo). Garrafa de Velho Barreiro FUNDIDA na mao direita (carne cresceu ao redor do vidro, nao pode mais soltar). Cicatriz craniana expoe o cranio diretamente -- sem pele nessa area, osso branco-amarelado visivel com a placa de titanio oxidada. Liquido verde toxico escorrendo do cranio aberto.

### Paleta (diferencas da base)
| Elemento | Hex | Mudanca |
|----------|-----|---------|
| Pele base | #7A8B6A | Verde-cinza de decomposicao |
| Pele sombra | #556B44 | Verde escuro |
| Pele necrose | #4A5A3A | Manchas escuras irregulares |
| Nariz | #8B4488 | Roxo de putrefacao |
| Nariz veias | #6B2266 | Roxo escuro |
| Olho pendurado | #CCCC44 com pupila #331100 | Amarelado/doente |
| Costelas expostas | #D4CCAA | Osso claro |
| Carne exposta | #883333 | Vermelho escuro de carne |
| Barriga veias | #445544 | Veias esverdeadas sob pele |
| Garrafa fundida | #2A5A2A com #7A8B6A | Vidro + carne misturados |
| Cranio exposto | #D4CCAA | Osso amarelado |
| Placa oxidada | #7A6A5A | Titanio oxidado, marrom-acinzentado |
| Liquido craniano | #66AA44 | Toxico verde brilhante |
| Larvas na barba | #EEEECC | Branco-amarelado, animado |

### Detalhes Especificos
- Olho esquerdo: pendurado 3px abaixo da orbita, balanca com o movimento (physics tether)
- Olho direito: semicerrado como sempre mas com iris amarelada
- Terno: 5-6 rasgos grandes (em vez dos 3 vincos do normal), revelando corpo
- Costelas: 3 arcos de 1px branco-amarelado visiveis no lado esquerdo
- Barba: mesma forma branca mas com 2-3 pixels animados que se movem lentamente (larvas)
- Garrafa: vidro parcialmente engolido pela carne da mao. Transicao suave entre vidro (#2A5A2A) e pele (#7A8B6A). Cachaca dentro agora e verde-toxico (#66AA44)
- Cranio: area de 6x4px no topo da cabeca sem pele, osso visivel, placa oxidada no centro
- Gotejamento craniano: emitter permanente de 1 particula (#66AA44) a cada 1000ms, caindo pela lateral da cabeca

### Animacoes Extras
- Olho pendurado: oscila como pendulo durante walk (physics sim simples)
- Larvas na barba: 2-3 pixels brancos se movem 1px a cada 400ms em direcoes aleatorias
- Gotejamento verde: particula constante no cranio
- Durante death: corpo se desintegra parcialmente -- pedacos (3-4 chunks de 4x4px) se separam e caem
- Som de walk: `sfx/zombie_squelch.ogg` em vez de `passo_pesado` -- som umido/podre

---

## SKIN 4: Cachaceiro de Gala
**ID**: `lula_gala`
**Desbloqueio**: Vencer 50 partidas online

### Descricao Visual Completa
Lula em traje de gala TENTANDO parecer elegante mas falhando grotescamente. Smoking branco com manchas de cachaca (manchas marrons irregulares no peito e nas mangas). Gravata borboleta vermelha (#8B1A1A) em vez da gravata normal -- torta, e claro. Cartola (top hat) levemente amassada e inclinada sobre a cicatriz craniana (tentando esconder, mas uma costura escapa por baixo). Monoculo sobre um olho semicerrado (comicamente inutil -- ele nao consegue manter o olho aberto o suficiente para segurar o monoculo, que cai a cada poucos segundos). Abotoaduras douradas. Sapatos de verniz preto arranhados. MESMO nariz bulboso vermelho, MESMA barriga de chope (agora esticando o smoking ao ponto dos botoes voarem), MESMA garrafa de Velho Barreiro (agora com um lacinho dourado no gargalo, "fancy"). A gravata borboleta esta sobre peito peludo -- a camisa abriu.

### Paleta (diferencas da base)
| Elemento | Hex | Mudanca |
|----------|-----|---------|
| Smoking | #F0EEE8 | Branco com leve tom creme |
| Smoking sombra | #C8C4BA | Sombra quente |
| Manchas de cachaca | #AA7722 | Irregular, 3-4 areas no peito |
| Gravata borboleta | #8B1A1A | Mesmo vermelho PT |
| Cartola | #1A1A1A | Preta, amassada |
| Cartola faixa | #8B1A1A | Vermelho PT na faixa |
| Monoculo | #CCDDEE | Lente transparente, aro dourado |
| Aro monoculo | #CCAA44 | Dourado |
| Corrente monoculo | #CCAA44 | Dourado, fio fino |
| Abotoaduras | #FFCC22 | Dourado brilhante |
| Sapatos verniz | #111111 | Preto brilhante com highlight |
| Laco na garrafa | #CCAA44 | Dourado |

### Detalhes Especificos
- Smoking: branco mas SUJO -- 3-4 manchas irregulares marrons de cachaca
- Gravata borboleta: 4x2px, vermelha, levemente torta
- Cartola: 6x8px preta no topo da cabeca. Amassada (indent de 1px no topo). Inclinada 5 graus. 1 ponto de sutura da cicatriz escapa por baixo da ala
- Monoculo: aro dourado 3x3px sobre olho direito com corrente fina (1px) descendo ate o bolso
- Botoes do smoking: 2 dos 3 ja voaram (gaps visiveis), o terceiro sob tensao
- Sapatos: highlight branco 1x1px indicando verniz (reflexo)
- Garrafa: mesma de sempre mas com lacinho dourado 2x2px no gargalo

### Animacoes Extras
- Monoculo: cai a cada 4-5s (tween Y +4px em 200ms, depois Lula pega de volta em 300ms)
- Cartola: desliza para o lado durante walk (tween X +/-1px alternado)
- Botao voando: durante attack, 1 botao branco (1x1px) voa radialmente (burst particle, 1 vez, then gone)
- Som extra: `sfx/monoculo_cai.ogg` quando monoculo cai -- "tink" de vidro fino
- Idle extra: Lula tenta ajustar a gravata borboleta com os 4 dedos e falha (micro-anim a cada 12s)

---

## SKIN 5: Operario (Throwback)
**ID**: `lula_operario`
**Desbloqueio**: Encontrar todas as 5 garrafas escondidas no modo historia

### Descricao Visual Completa
Lula jovem (anos 70/80), epoca de lider sindical metalurgico. Macacao azul de operario com manchas de graxa e oleo. Capacete de seguranca amarelo (mal encaixado sobre a cabeca -- na versao 2026, esconde parcialmente a cicatriz MAS a cicatriz e um anacronismo proposital, porque e SEMPRE presente em todas as skins). Crachá de sindicato no peito (ABC metalurgico). Barba menos branca -- cinza escuro em vez de branco (mais jovem). MESMO nariz bulboso vermelho (ja bebia naquela epoca). Botas de bico de aco. Luvas de trabalho nas maos -- mas na mao esquerda, a luva e feita para 4 dedos (costurada no local do mindinho). Garrafa de Velho Barreiro substituida por cantil de aluminio (mas conteudo e o mesmo). Barriga menor que na versao base (mais jovem, menos cerveja acumulada), mas ainda proeminente.

### Paleta (diferencas da base)
| Elemento | Hex | Mudanca |
|----------|-----|---------|
| Macacao | #2244AA | Azul operario |
| Macacao sombra | #1A3388 | Azul escuro |
| Manchas graxa | #333322 | Preto-esverdeado oleoso |
| Capacete | #CCAA22 | Amarelo seguranca |
| Capacete sombra | #AA8811 | Amarelo escuro |
| Cracha sindicato | #CC3333 | Vermelho com estrela |
| Barba | #777777 | Cinza escuro (mais jovem) |
| Luvas | #AA8844 | Couro marrom |
| Botas | #554422 | Marrom industrial |
| Bico de aco | #888888 | Metal |
| Cantil | #AAAAAA | Aluminio |

### Detalhes Especificos
- Macacao: tirantes visiveis sobre os ombros, bolso no peito com cracha
- Capacete: amarelo, levemente torto, com adesivo do sindicato (1x1px vermelho)
- Cicatriz: parcialmente oculta pelo capacete mas 2-3 pontos escapam por baixo
- Barba: cinza escuro, menos volume (mais jovem -- 4x3px em vez de 6x4px)
- Nariz: MESMO tamanho e cor (ja era alcoolatra)
- Barriga: 2px menor em cada eixo (mais jovem, menos cerveja)
- Luva esquerda: visualmente tem espaco para 4 dedos (costura no lugar do mindinho)
- Cantil: 3x5px aluminio, substituindo a garrafa (mesmo comportamento de jogo)
- Botas: com bico de aco -- pixel de highlight metalico na ponta

### Animacoes Extras
- Walk: postura levemente mais ereta (mais jovem, menos bebado -- mas AINDA cambaleante)
- Idle: em vez de beber da garrafa, bebe do cantil (mesma animacao, sprite diferente)
- Attack: arremessa cantil (mesmo arco, mesma mecanica, visual diferente)
- Som: `sfx/cantil_metal.ogg` em vez de vidro para sons de impacto

---

## SKIN 6: Presidente de Cela (Alternativa 2026)
**ID**: `lula_preso`
**Desbloqueio**: Easter egg -- derrotar Lula e Bolsonaro no mesmo round sem tomar dano

### Descricao Visual Completa
Versao hipotetica/satirica onde Lula esta preso (referencia ao periodo de 2018-2019 em Curitiba). Uniforme laranja de presidiario com numero no peito ("PRES-001"). Mesmo nariz bulboso vermelho, mesma barba, mesma barriga -- mas tudo dentro do uniforme laranja largo. Chinelos (havaianas) em vez de sapatos. Algemas rompidas penduradas num pulso (escapou ou foram removidas). Cicatriz craniana totalmente exposta (sem curativos, sem cartola -- nada escondendo). Garrafa de Velho Barreiro substituida por garrafa PET de tubaína (mas com cachaca dentro, rotulo "Tubaina" colado por cima do rotulo real que e "Velho Barreiro"). Faixa presidencial SOBRE o uniforme de preso -- porque ele se recusa a tirar, mesmo na cadeia.

### Paleta (diferencas da base)
| Elemento | Hex | Mudanca |
|----------|-----|---------|
| Uniforme | #CC6622 | Laranja presidiario |
| Uniforme sombra | #AA4411 | Laranja escuro |
| Numero no peito | #333333 | Preto estampado |
| Chinelos | #2244AA | Havaianas azuis |
| Tira chinelo | #FFFFFF | Branco |
| Algemas rompidas | #888888 | Metal |
| Corrente | #666666 | Metal escuro |
| Garrafa PET | #CCDDEE (transparente) | Plastico claro |
| Liquido dentro | #CC8833 | Cachaca (mesma cor) |
| Rotulo fake | #44AACC | "Tubaina" |
| Faixa presidencial | #22AA22 com #FFCC22 | Verde-dourado |

### Detalhes Especificos
- Uniforme: largo, mal ajustado, barriga estica o tecido no centro
- Numero: "PRES-001" em 2 linhas no peito (3x6px area)
- Chinelos (havaianas): substituem sapatos, dedos dos pes visiveis (5 no pe direito, 4 no pe esquerdo -- sim, falta dedo no pe tambem, piada extra)
- Algemas: 1 algema aberta no pulso esquerdo com 3px de corrente pendurada
- Garrafa PET: transparente, formato diferente (mais larga, mais baixa, 5x8px). Rotulo "Tubaina" (#44AACC) colado torto
- Faixa presidencial: diagonal no peito sobre o uniforme, verde (#22AA22) com letras douradas
- Cicatriz: maxima visibilidade -- sem nada cobrindo, todos os pontos e placa visiveis

### Animacoes Extras
- Walk: chinelos fazem "flap flap" -- som diferente: `sfx/chinelo_flap.ogg`
- Idle: ajusta a faixa presidencial sobre o uniforme (micro-anim a cada 10s)
- Corrente da algema: balanca durante walk (physics pendulo, 3px)
- Attack: arremessa garrafa PET (mesmo arco, mas som de plastico: `sfx/pet_arremesso.ogg`)
- Impacto da PET: menos cacos (plastico nao estilhaca -- amassa e vaza), poca maior (mais liquido)

---

## SKIN 7: Discursador Cosmico (Skin Mistica)
**ID**: `lula_cosmico`
**Desbloqueio**: Usar o Ultimate "Discurso de Hora e Meia" 10 vezes em partidas diferentes

### Descricao Visual Completa
Lula transcendeu a realidade politica e se tornou uma entidade cosmica de discurso infinito. Corpo envolto em aura nebulosa vermelho-dourada. Terno feito de ESTRELAS -- textura de constelacao no tecido (pontos brilhantes no fundo escuro). Nariz bulboso brilha como uma NEBULOSA vermelha (particulas cosmicas orbitando). Olhos: em vez de semicerrados, sao duas GALAXIAS espirais minusculas. Barba e feita de cometas brancos com caudas luminosas. Garrafa de Velho Barreiro e feita de cristal cosmico (transparente com arco-iris interno). Cicatriz craniana: em vez de costura, e uma FISSURA no espaco-tempo, com estrelas visiveis DENTRO da cabeca. A gravata e a cauda de um cometa vermelho. A barriga contem um buraco negro em miniatura (circulo escuro com anel de acrecao). Microfone cosmico flutuando ao lado.

### Paleta (diferencas da base)
| Elemento | Hex | Mudanca |
|----------|-----|---------|
| Terno base | #0A0A2A | Azul escuro cosmico |
| Estrelas no terno | #FFFFFF, #FFCC88, #88CCFF | Pontos brilhantes |
| Aura | #CC6622 alpha 40% | Nebulosa dourada |
| Nariz nebulosa | #FF4444 com #FF8888 | Vermelho brilhante irradiante |
| Olhos galaxia | #8888FF com #FFFFFF espiral | Azul-branco giratório |
| Barba cometa | #FFFFFF com trail #CCCCFF | Branco luminoso |
| Garrafa cristal | #AACCFF alpha 70% | Cristal transparente |
| Arco-iris garrafa | Gradiente espectral | Dentro do cristal |
| Fissura craniana | #000000 com #FFFFFF pontos | Buraco com estrelas |
| Gravata cometa | #CC3333 com trail #FF6666 | Vermelho com cauda |
| Buraco negro barriga | #000000 com anel #FFCC44 | Centro escuro, anel brilhante |

### Detalhes Especificos
- TODAS as texturas tem animacao interna (estrelas cintilam, galaxias giram, cometas fluem)
- Skin puramente cosmetica -- nenhuma diferenca mecanica
- Trail: Lula deixa rastro de particulas cosmicas ao caminhar (#FFCC88, lifetime 500ms)
- Sons: todos os SFX ganham reverb espacial (eco longo, como se em vacuo)
- Idle: particulas cosmicas orbitam o corpo permanentemente
- A fissura craniana mostra um mini-universo dentro da cabeca de Lula (referencia: "o universo de mentiras e tao grande que cabe na cabeca dele")

### Animacoes Extras
- Nariz: particulas orbitantes (#FF4444, 2-3, orbita circular 4px raio, perpetua)
- Olhos galaxia: rotacao lenta (1 ciclo completo a cada 4s)
- Barba cometa: trail de 2-3 pixels brancos que seguem com delay
- Walk: flutuando 1px acima do chao (sem som de passo, som de "hum" cosmico)
- Ultimate (Discurso): o palanque e feito de estrelas e o discurso reverbera pelo cosmos

---

## TABELA COMPARATIVA DE SKINS

| Skin | Terno | Cabeca | Acessorio Mao | Acessorio Extra | Cor Dominante |
|------|-------|--------|---------------|-----------------|---------------|
| Normal | Cinza amassado | Cicatriz + curativos | Velho Barreiro (vidro) | Gravata torta | Cinza/Vermelho PT |
| Frankenstein | Cinza + bata hospital | Cicatriz ENFATIZADA | Velho Barreiro (vidro) | Pulseira hospital | Cinza/Rosa-cirurgico |
| Zombie | Rasgado c/ costelas | Cranio exposto | Garrafa FUNDIDA na carne | Olho pendurado | Verde decomposicao |
| Gala | Smoking branco manchado | Cartola + monoculo | Velho Barreiro c/ laco | Gravata borboleta | Branco/Dourado |
| Operario | Macacao azul | Capacete amarelo | Cantil aluminio | Cracha sindicato | Azul/Amarelo |
| Preso | Laranja presidiario | Cicatriz maxima | PET de "tubaina" | Faixa presidencial + algema | Laranja |
| Cosmico | Constelacao | Fissura espaco-tempo | Cristal cosmico | Aura nebulosa | Azul-escuro/Dourado |

---

## NOTAS DE IMPLEMENTACAO

### Atlas de Skins
Cada skin ocupa as mesmas rows do atlas que a skin base (rows 0-7 para a base, rows 8-15 para skins). Para economizar espaco no atlas 2048x2048:
- Skins com poucas diferencas (Frankenstein, Preso): usar palette swap + overlay sprites
- Skins com muitas diferencas (Zombie, Cosmico): sprite sheets completos

### Prioridade de Producao
1. **Normal** -- OBRIGATORIA para MVP
2. **Frankenstein 2026** -- Alta (atualidade, marketing)
3. **Zombie Premium** -- Alta (tema do jogo)
4. **Preso** -- Media (referencia politica forte)
5. **Operario** -- Media (nostalgia, throwback)
6. **Gala** -- Baixa (cosmetico puro)
7. **Cosmico** -- Baixa (reward de endgame)

### Desbloqueio no Jogo
| Skin | Condicao | Dificuldade |
|------|----------|-------------|
| Normal | Padrao | -- |
| Frankenstein | Derrotar Lula 1x | Facil |
| Zombie | Completar historia dificuldade max | Dificil |
| Gala | 50 vitorias online | Medio-Dificil |
| Operario | 5 garrafas escondidas | Medio |
| Preso | No-hit Lula + Bolsonaro | Muito Dificil |
| Cosmico | 10 Ultimates usados | Medio |
