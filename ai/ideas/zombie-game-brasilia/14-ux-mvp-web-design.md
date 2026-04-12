# ZUMBIS DE BRASÍLIA — UX MVP Web Design
### Jenova Chen | Experiência Emocional para Browser | Abril 2026

**Versão 1.0 — Revisão Web MVP**

---

> *"No mobile você compete com o metrô. No browser você compete com 23 abas abertas, um artigo do G1, o feed do Instagram e a reunião que não fechou. O jogo precisa ser mais interessante que tudo isso — e precisa provar isso em 5 segundos."*

---

## 1. Filosofia UX Web — O Que Muda do Mobile para o Browser

### A Mudança Fundamental: Intenção vs. Impulso

No design original para mobile, o jogador estava no metrô. Ele tinha 7 minutos e um objetivo claro: passar o tempo. Havia intenção de uso.

No browser, o jogador recebeu um link no WhatsApp durante o horário de almoço. Ele está na mesa de trabalho, com o chefe circulando, com outras abas abertas, com o celular na mão e o notebook na frente. Não há intenção pré-formada. Há **impulso** — e impulso tem prazo de validade medido em segundos.

Essa diferença muda tudo.

### Os Três Inimigos do Browser Game

**Inimigo 1: A Aba Concorrente**
O usuário de browser tem, em média, 8 abas abertas. Cada notificação, cada barulho, cada segundo de loading é uma oportunidade para ele clicar em outra aba e nunca mais voltar. A fricção que no mobile seria "incômodo" no browser é "abandono permanente".

**Inimigo 2: O Contexto Incontrolável**
No mobile o jogador está no espaço dele. No browser, especialmente no desktop, ele está no trabalho, na faculdade, num lugar público com monitor visível. O jogo precisa ser o tipo de coisa que você fecha rapidamente quando o chefe passa — e reabre com um clique.

**Inimigo 3: A Barreira de Legitimidade**
Browser games carregam um estigma histórico de qualidade inferior. Os primeiros 10 segundos de gameplay precisam destruir esse preconceito. Se o jogo parecer barato ou lento no primeiro impacto, o jogador sai com a conclusão confirmada.

### O Que Muda na Emoção Central

O UX original tinha uma curva emocional longa: curiosidade, aprendizado, flow state, triunfo, "mais uma". Era projetado para sessões de 7 a 12 minutos.

Para o MVP web, a curva precisa ser comprimida sem perder os picos:

```
ORIGINAL (mobile):
Curiosidade → Aprendizado → Competência → Flow → Triunfo → "Mais uma"
    |              |              |           |       |          |
   10s            1min          2min        5min   8min       10min

MVP WEB:
Curiosidade → [Aprendizado + Competência fundidos] → Catarse → "Mais uma"
    |                         |                         |          |
   5s                        30s                       2min      3min
```

O aprendizado e a primeira competência precisam acontecer simultaneamente. O jogador aprende fazendo, e cada coisa que aprende é imediatamente recompensada. Não há fase separada de tutorial — o tutorial É o início do gameplay.

### O Princípio do "Já Entendi"

Para o browser, cada elemento de UI deve comunicar seu propósito em zero leituras. Não em uma leitura. Zero. O jogador deve olhar para a tela e entender o estado do jogo como se fosse instintivo.

Isso significa: zero texto de instrução, zero pop-ups de boas-vindas, zero onboarding explícito. O jogo fala através do design visual, do movimento, e do som — não através de palavras.

---

## 2. Fluxo Completo — Zero Fricção do Link ao Replay

### O Imperativo: Nenhuma Tela Entre o Link e o Jogo

A decisão do CEO é absoluta e está correta: o jogador clica no link e está jogando. Qualquer tela entre o clique e o gameplay é uma oportunidade de abandono.

```
FLUXO COMPLETO — CONGRESSO DOS MORTOS (WEB)

[LINK COMPARTILHADO]
        |
        | clique no WhatsApp / Twitter / mensagem
        v
[LOADING — máx 3 segundos]
        |
        | assets carregados em background
        | animação de loading satirica (não spinner genérico)
        v
[GAMEPLAY IMEDIATO]
        |
        | sem menu, sem seleção de arma, sem tutorial
        | o cidadão está na Esplanada, zumbis se aproximam
        v
[LOOP DE GAMEPLAY — 3 minutos]
        |
        | waves contínuas
        | morte é possível a qualquer momento
        v
    [MORREU?]
       / \
     NÃO  SIM
      |    |
      |   [TELA DE RESULTADO — "SEU MANDATO ACABOU"]
      |    |
      |    |--- [COMPARTILHAR] → screenshot para redes sociais
      |    |--- [MAIS UMA] → volta ao início do gameplay (não ao menu)
      |    |--- [VER RANKING] → leaderboard (opcional, não bloqueia)
      |    
      |
[TIMER DE 3 MINUTOS ESGOTA]
        |
        v
[TELA DE RESULTADO — "TEMPO ESGOTOU"]
        |
        |--- [COMPARTILHAR]
        |--- [MAIS UMA]
        |--- [VER RANKING]
```

### Detalhamento Fase a Fase

**Fase 1 — Loading (0 a 3 segundos)**

O loading não existe como tela separada — existe como transição. Enquanto os assets carregam, o jogador vê a abertura narrativa animada: texto datilografado aparecendo sobre fundo escuro ("Brasília, abril de 2026. O Congresso aprovou a Emenda 666..."). O texto leva exatamente o tempo do loading. Quando termina, o gameplay começa.

Se o loading terminar antes do texto: o gameplay começa imediatamente assim que o texto terminar.
Se o loading demorar mais que 3 segundos: o texto continua, o game não travou, o jogador ainda está engajado.

O loading não é espera — é contexto narrativo.

**Fase 2 — Gameplay (3 segundos a 3 minutos)**

O cidadão está no centro da Esplanada. Três vereadores-zumbi se aproximam lentamente de direções diferentes. No desktop, o cursor do mouse muda para uma mira. No mobile, um joystick virtual aparece suavemente onde o jogador toca.

Não há instrução. Não há seta. Não há "use WASD para mover". O design visual comunica tudo:
- Os zumbis vêm em sua direção: movimento é necessário
- A vassoura está na mão do cidadão: ataque é possível
- O botão de ataque pulsa suavemente no canto inferior direito: aqui está o gatilho

O primeiro toque/clique ataca. O primeiro movimento faz o personagem andar. Em 5 segundos, o jogador aprendeu tudo que precisa.

**Fase 3 — Morte (em qualquer momento)**

A morte é justa e cinematográfica. Tela congela por 0.5 segundos, fade a preto, e aparece a tela de resultado. Não há loading. Não há espera. A transição é parte do ritmo.

**Fase 4 — Tela de Resultado (10 a 20 segundos)**

Design projetado para screenshot. Detalhado na seção 4.

**Fase 5 — "Mais Uma" (instantâneo)**

O botão "MAIS UMA" reinicia o gameplay diretamente. Sem menu, sem seleção, sem loading. O cidadão aparece na Esplanada em 0.5 segundos. A onda começa. O jogador está de volta.

A segunda partida é mais rápida de começar que a primeira — intencionalmente. O jogador que acabou de morrer tem o impulso de revanche. Se ele precisar esperar qualquer coisa, esse impulso esfria.

---

## 3. Controles Dual — Desktop e Mobile Browser

### Filosofia: Dois Inputs, Uma Experiência

O maior erro de browser games "responsive" é tratar mobile como um desktop menor. São paradigmas de input fundamentalmente diferentes. O design precisa abraçar ambos sem comprometer nenhum.

**Regra de ouro dual-input**: qualquer ação que pode ser feita com teclado/mouse pode ser feita com touch — e vice-versa. Nunca há uma ação que exige um input específico de plataforma.

---

### Desktop — Teclado e Mouse

**Movimento: WASD ou Setas direcionais**

WASD é o padrão de games PC há 30 anos. Todo jogador de game de PC sabe WASD instintivamente. As setas direcionais são o fallback para quem não é gamer. Ambos funcionam simultaneamente — não há necessidade de configurar.

O personagem se move em 8 direções com WASD. Velocidade constante — sem aceleração gradual que deixa o jogo "escorregadio".

**Mira: Mouse**

O cursor do mouse define a direção do ataque, não a direção do movimento. Isso cria uma separação natural entre "onde estou indo" (WASD) e "onde estou atacando" (mouse). É a mecânica de twin-stick shooter adaptada para teclado+mouse — e é o controle mais preciso e satisfatório possível para esse gênero.

O cursor visual é substituído por uma mira estilizada: um alvo de papel de jornal com o crosshair feito de linhas irregulares. Comunica "eu controlo para onde ataco" sem precisar explicar.

**Ataque: Clique esquerdo ou Barra de espaço**

Dois inputs para o mesmo gesto por acessibilidade e preferência. Usuários que jogam com uma mão no mouse preferem o clique. Usuários que jogam com as duas mãos no teclado preferem o espaço.

O ataque é instantâneo ao input. Zero input lag percebível — qualquer delay acima de 50ms destrói a satisfação do combate.

**Power-up: Shift ou clique direito**

Ativação de power-up coletado. Shift porque está na borda do alcance natural da mão esquerda. Clique direito porque é o "outro botão" natural do mouse.

**Pausa: Esc ou P**

A aba perde foco automaticamente quando o usuário troca de aba — o jogo pausa automaticamente. Isso é crítico para o contexto de trabalho/faculdade: o jogo "coopera" com o usuário que precisa sair rápido.

**Responsividade do Teclado**

- Input buffering de 1 frame: se o jogador pressiona ataque enquanto o ataque anterior ainda está no cooldown, o próximo ataque dispara imediatamente ao fim do cooldown
- Nenhuma ação "perdida" por timing imperfeito — o jogo é generoso com inputs

---

### Mobile Browser — Touch

**Movimento: Joystick Virtual Dinâmico**

O joystick não existe fixo na tela. Ele aparece onde o polegar toca — especificamente na metade esquerda da tela (área natural do polegar esquerdo). O raio do joystick é 80px. O ponto central é 24px.

Por que dinâmico, não fixo:
- Tamanhos de tela variam enormemente (iPhone SE a tablet Android)
- A posição natural do polegar varia por tamanho de mão
- Joystick fixo força o jogador a adaptar a mão ao jogo; joystick dinâmico adapta o jogo à mão

**Ataque: Toque na metade direita da tela**

Qualquer toque na metade direita da tela dispara o ataque. Não há um botão específico — toda a área direita é o botão de ataque. Isso maximiza a área de toque e elimina o problema de "não acertei o botão".

A mira automática no mobile seleciona o zumbi mais próximo na direção do movimento. O jogador não precisa mirar — ele precisa se posicionar. É uma decisão deliberada: no mobile, precisão de mira é impossível com touch, então o jogo assume a mira e libera o jogador para focar no posicionamento.

**Power-up: Toque duplo na área de ataque**

Dois toques rápidos (< 300ms de intervalo) na área direita ativa o power-up coletado. É um gesto suficientemente distinto do toque simples para não disparar acidentalmente, mas intuitivo o suficiente para ser descoberto sem instrução.

**Pausa: Toque no ícone de pausa (único elemento fixo de UI)**

O único elemento de UI permanentemente visível e tocável é um ícone de pausa no canto superior direito — 44x44px (mínimo para área de toque confortável). Toque único pausa e abre overlay com opções.

**Prevenção de Scroll Acidental**

O jogo captura todos os eventos de touch e previne scroll da página. Isso é tecnicamente necessário e UX necessário: um scroll acidental durante gameplay é fatal para a imersão.

`event.preventDefault()` em todos os touchstart/touchmove na área do canvas.

**Feedback Háptico (onde disponível)**

- Hit confirmado em zumbi: vibração de 15ms
- Levar dano: vibração de 25ms (diferente, identifica como evento negativo)
- Morte: vibração de 3 pulsos de 20ms com 50ms entre eles
- Power-up coletado: vibração de 10ms (sutil, positiva)

---

### Calibração de Dificuldade por Input

O jogo detecta automaticamente se o jogador está usando touch ou teclado+mouse e ajusta sutilmente:

| Parâmetro | Desktop | Mobile |
|---|---|---|
| Mira | Manual (mouse) | Automática (nearest enemy) |
| Hitbox dos zumbis | Normal | +15% maior |
| Velocidade inicial dos zumbis | 100% | 90% |
| Alcance de ataque | Normal | +10% |

Isso não é "modo fácil" no mobile — é compensação de precisão de input. O desafio de posicionamento e sobrevivência é idêntico. A dificuldade de execução de ataque é equalizada.

---

## 4. Tela de Resultado — Design para Compartilhamento

### O Imperativo do Screenshot

A tela de resultado é a arma viral do jogo. Cada pessoa que morre e compartilha é um anúncio gratuito enviado para todos os contatos dela. O design precisa ser:

1. **Reconhecível como Zumbis de Brasília** — sem o nome do jogo visível, a identidade visual precisa ser óbvia
2. **Engraçado por si só** — o screenshot precisa fazer rir mesmo sem ter jogado
3. **Gerador de competição** — o score precisa convidar comparação ("consigo mais que isso")
4. **Compartilhável em portrait** — a maioria dos screenshots de mobile são em portrait; o design deve funcionar em 9:16

### Layout da Tela de Resultado

```
┌──────────────────────────────────┐
│                                  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ░ MANCHETE DE JORNAL RASGADO ░  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│                                  │
│  ╔════════════════════════════╗  │
│  ║                            ║  │
│  ║   ZUMBIS DE BRASÍLIA       ║  │  ← logo do jogo
│  ║   CONGRESSO DOS MORTOS     ║  │
│  ║                            ║  │
│  ╚════════════════════════════╝  │
│                                  │
│  ┌──────────────────────────┐   │
│  │  "SEU MANDATO ACABOU"    │   │  ← título satírico (grande, impacto)
│  │  (por enquanto)          │   │  ← subtítulo irônico (menor)
│  └──────────────────────────┘   │
│                                  │
│  ┌───────────┬──────────────┐   │
│  │  SCORE    │  SOBREVIVEU  │   │
│  │  14.820   │  2min 34s    │   │  ← dados da partida
│  ├───────────┼──────────────┤   │
│  │  ZUMBIS   │  WAVE        │   │
│  │  MORTOS   │  ALCANÇADA   │   │
│  │   247     │    7         │   │
│  └───────────┴──────────────┘   │
│                                  │
│  ┌──────────────────────────┐   │
│  │  TÍTULO POLÍTICO OBTIDO  │   │  ← gerado dinamicamente
│  │  "VEREADOR DOS MORTOS"   │   │
│  └──────────────────────────┘   │
│                                  │
│  [  COMPARTILHAR  ]  [MAIS UMA] │  ← CTAs
│                                  │
│  congressodosmortos.com.br       │  ← URL sempre visível
└──────────────────────────────────┘
```

### Hierarquia Visual

**Elemento 1 — Manchete Satirica (60% da largura, topo)**
Fonte Bebas Neue, corpo 48px, fundo de papel de jornal com textura. O título satirico é gerado dinamicamente baseado no score e na causa da morte. Exemplos:

- "SEU MANDATO ACABOU" — morte padrão
- "APROVADO EM COMISSÃO (de zumbis)" — morte por onda de inimigos
- "IMPUGNADO POR UNANIMIDADE" — morte rápida (< 30 segundos)
- "REELEITO... NÃO. COMIDO." — morte por boss
- "FORO PRIVILEGIADO NEGADO" — morte por Senador Blindado
- "DELAÇÃO PREMIADA INSUFICIENTE" — morte por Banqueiro-Zumbi
- "EMENDA CONSTITUCIONAL 666 APROVADA" — morte com HP cheio (acidente)
- "SOBREVIVEU MAIS QUE A CPMI" — tempo > 2 minutos

**Elemento 2 — Score em destaque**
Número enorme, amarelo-ouro, corpo 72px. É o elemento mais legível em qualquer tamanho de screenshot. A competição começa aqui.

**Elemento 3 — Stats da partida**
Grid 2x2 com os quatro números que importam: score, tempo, zumbis mortos, wave alcançada. Fonte bold, legível, sem decoração excessiva. Esses números são a razão pela qual o jogador compartilha E a razão pela qual o amigo dele vai querer superar.

**Elemento 4 — Título Político**
Sistema de geração de título baseado em thresholds de score:

| Score | Título |
|---|---|
| 0 - 1.000 | "Cabo Eleitoral Zumbi" |
| 1.001 - 5.000 | "Vereador dos Mortos" |
| 5.001 - 10.000 | "Deputado Estadual Zumbi" |
| 10.001 - 20.000 | "Deputado Federal dos Mortos" |
| 20.001 - 40.000 | "Senador Blindado (de verdade)" |
| 40.001 - 80.000 | "Ministro da Corrupção Épica" |
| 80.001+ | "Candidato Eterno — Aprovado" |

O título é engraçado por si só. Um amigo que recebe o screenshot e vê "Vereador dos Mortos" ri antes de ler qualquer outro elemento.

**Elemento 5 — URL do jogo**
`congressodosmortos.com.br` em rodapé, corpo 16px, sempre visível. Em qualquer screenshot, em qualquer crop, o link precisa estar legível. É o CTA mais importante do jogo.

### Botão de Compartilhamento

No mobile: abre o share sheet nativo do sistema operacional (Web Share API). O jogador escolhe WhatsApp, Instagram Stories, Twitter — onde já está logado, sem fricção adicional.

No desktop: copia o link para o clipboard com mensagem pré-escrita ("Meu mandato acabou. Veja quanto tempo você sobrevive: congressodosmortos.com.br") e abre opções para Twitter e WhatsApp Web.

A imagem compartilhada é um screenshot gerado em canvas (não uma captura de tela) — isso garante que a imagem tenha sempre exatamente o tamanho e proporção corretos para cada plataforma.

---

## 5. Juice para Web — O Que Sobrevive, o Que é Cortado, o Que é Adaptado

### O Princípio da Destilação

Juice é o conjunto de feedback audiovisual que faz o jogo parecer vivo — os hits que batem, os números que saltam, os sons que confirmam cada ação. Para o MVP web, a regra é: **manter apenas o juice que serve à catarse, cortar tudo que serve ao grinding**.

### O Que Sobrevive (essencial para a emoção central)

**Onomatopeias de impacto visuais**
THWACK, SLAP, BOOM — aparecem no ponto de impacto, 6 frames, desaparecem. São a assinatura visual do jogo. Sem elas, o combate perde 50% da satisfação percebida. Custo de implementação: baixo. Impacto emocional: alto. Sobrevivem intactas.

**Hit numbers flutuantes**
Números de dano saindo dos zumbis. No original mobile tinham gradações de cor (branco/amarelo/laranja). No web: simplificar para dois estados — dano normal (branco) e crítico (amarelo). O número de gradações no mobile era para sessões longas onde o jogador precisava de feedback granular. Para sessões de 3 minutos, dois estados são suficientes.

**Frases dos zumbis ao morrer**
"Fui eleito democraticamente!" / "Tenho foro privilegiado mesmo depois de morto!" / "Era tudo declarado!" — essas frases são o contrato emocional do jogo. É o momento que transforma um sprite em personagem, e um personagem em piada política. Estas são inegociáveis. Sobrevivem intactas.

**Screen flash ao levar dano**
Flash vermelho de 30% opacidade por 4 frames + personagem pisca branco. É o feedback de dano mais eficiente e universal possível. Funciona em desktop e mobile. Custa zero de UI real estate. Sobrevive.

**Score "saltando" ao ganhar pontos**
O número do score faz um bounce leve (110% → 100% de escala) a cada ganho de ponto. É microanimação de 3 frames. Custo zero. Feedback positivo constante que mantém o ritmo de satisfação entre kills. Sobrevive.

**Efeito de morte cômica do zumbi**
Ao morrer, o zumbi voa para trás com squash-and-stretch exagerado. No original havia mais frames de animação. No web: simplificar para 5 frames totais. O exagero slapstick é fundamental para o tom de catarse cômica — não pode ser cortado, apenas otimizado.

**Música adaptativa**
Loop principal + variante de intensidade alta para waves avançadas. No original havia 4 loops. No web: 2 loops. O contraste entre "wave tranquila" e "wave intensa" é necessário para a curva emocional. Mais que 2 loops é luxo para um MVP de 2 semanas.

### O Que é Cortado (serve ao longo prazo, não ao MVP)

**Sistema de upgrades entre waves**
No original, entre waves o jogador escolhia upgrades. Para o MVP web com sessões de 3 minutos, isso interrompe o ritmo e adiciona decisões num momento onde o flow state está construído. Cortado do MVP. Pode ser adicionado na v1.5 se a retenção D7 justificar.

**Missões diárias e metagame entre sessões**
Completamente fora do escopo do MVP web. A retenção do browser game vem de viralidade e score competitivo, não de loops de progressão. Adicionar metagame num MVP de 2 semanas é desperdiçar tempo de desenvolvimento em feature que não gera viralidade.

**Leaderboard global**
Pode existir como feature secundária (não bloqueia o fluxo principal), mas não é necessário para o MVP de lançamento. O compartilhamento orgânico de score é mais viral que um leaderboard sem contexto. Adicionado na v1.2 se os dados de engajamento justificarem.

**Sistema de skins e customização do personagem**
Cortado. No original havia 3 variantes de tom de pele + skins desbloqueáveis. Para o MVP: personagem único. Personagem com identidade visual forte é mais memorável que personagem genérico com opções.

**Conquistas formais**
Cortado. Conquistas servem à retenção de longo prazo. Para o MVP, o equivalente emocional são os títulos gerados na tela de resultado — que entregam a satisfação de "conquistei algo" sem o overhead de sistema de achievements.

### O Que é Adaptado

**Joystick virtual**
No original: dinâmico, aparece onde o dedo toca, raio de 60dp. Para o web mobile: mantido dinâmico, raio aumentado para 80px (telas maiores de browser), sensibilidade de detecção de movimento reduzida para 10px (evita ativação acidental por toques leves).

**HUD**
O HUD original era projetado para 720p portrait mobile. Para web: deve funcionar em landscape desktop (16:9), portrait mobile (9:16) e landscape mobile (16:9). A solução: HUD dinâmico que reposiciona seus elementos baseado na orientação e tamanho de tela. Detalhado na seção 6.

**Curva de dificuldade**
No original, a curva se estendia por 7-12 minutos. Para o web MVP com timer de 3 minutos: a dificuldade deve atingir o pico nos últimos 30 segundos, não no minuto 8. A wave progression é comprimida: o que antes chegava na wave 5 agora chega na wave 3.

**Tela de morte**
No original: tela de morte com opção de continuar (rewarded ad) ou encerrar. Para o MVP web: a opção de "continuar" via rewarded ad é mantida como feature de monetização, mas o fluxo primário é morte → resultado → mais uma. O ad é oferecido como alternativa, não como obstáculo.

---

## 6. Responsive Design — Adaptação para Diferentes Telas

### A Realidade das Resoluções

O jogador de browser game em 2026 usa:
- Desktop: 1920x1080 (16:9), 1366x768 (16:9), 2560x1440 (16:9)
- Mobile portrait: 390x844 (iPhone 14), 360x800 (Android médio)
- Mobile landscape: 844x390 (iPhone 14), 800x360 (Android médio)
- Tablet: 768x1024 (iPad portrait), 1024x768 (iPad landscape)

O canvas do jogo é sempre **16:9 fixo**. O que se adapta é como esse canvas é apresentado na tela.

### Estratégia: Canvas Fixo + Letterbox Adaptativo

```
DESKTOP (1920x1080):
┌──────────────────────────────────────────────────────────┐
│  background color (fora do canvas)                        │
│  ┌────────────────────────────────────────────────────┐  │
│  │                                                    │  │
│  │          CANVAS DO JOGO (16:9, 1280x720)           │  │
│  │                                                    │  │
│  └────────────────────────────────────────────────────┘  │
│  background color (fora do canvas)                        │
└──────────────────────────────────────────────────────────┘

MOBILE PORTRAIT (390x844):
┌──────────────┐
│ UI controles │  ← área fora do canvas com controles touch
│ ┌──────────┐ │
│ │          │ │
│ │  CANVAS  │ │  ← canvas redimensionado para 390x219 (16:9)
│ │  (16:9)  │ │
│ │          │ │
│ └──────────┘ │
│ [JS] [ATK]   │  ← joystick e área de ataque abaixo do canvas
└──────────────┘

MOBILE LANDSCAPE (844x390):
┌────────────────────────────────────┐
│ ┌──────────────────────────────┐  │
│ │                              │  │
│ │   CANVAS (16:9, ocupa ~90%   │  │
│ │   da largura)                │  │
│ │                              │  │
│ └──────────────────────────────┘  │
└────────────────────────────────────┘
```

### Decisões de Layout por Contexto

**Desktop (landscape, tela grande)**

O canvas centralizado com barras laterais escuras (letterbox) ou preenchimento com arte de fundo (os gramados da Esplanada se estendem além do canvas como paralax). Resolução nativa do canvas: 1280x720. Em telas 1920x1080, o canvas escala para 1440x810 (máximo que mantém pixel density confortável).

**Mobile Portrait**

Contexto mais comum para quem recebe o link no WhatsApp e abre no celular. Neste caso, o canvas fica no topo da tela (acima da dobra), e os controles touch ficam na área abaixo. O canvas em portrait é reduzido — mas o que importa é que o personagem e os zumbis próximos estejam sempre visíveis com clareza. A câmera tem um zoom out leve (10%) em portrait para compensar a área menor.

**Mobile Landscape**

Ideal para gameplay prolongado. O canvas ocupa quase toda a tela. Os controles ficam sobrepostos ao canvas (joystick na esquerda, área de ataque na direita), com opacidade reduzida. É o layout mais próximo do design original mobile.

**Detecção automática de orientação**

Ao detectar mudança de orientação, o jogo pausa automaticamente por 0.5 segundos (para o layout se ajustar) e retorna. Sem mensagem de "gire o dispositivo" — o jogo funciona em qualquer orientação.

### Fontes e Legibilidade por Resolução

| Resolução | Score | Wave | Texto UI |
|---|---|---|---|
| Desktop 1080p | 48px | 28px | 18px |
| Mobile landscape | 36px | 22px | 14px |
| Mobile portrait | 32px | 20px | 13px |

O mínimo absoluto de qualquer texto tocável/clicável é 44px de área de toque, independente do tamanho da fonte.

### Mapa de Jogo em Diferentes Telas

O mapa da Esplanada é renderizado como um espaço maior que a viewport, com câmera seguindo o personagem. Em telas maiores, mais do mapa fica visível — isso é uma vantagem estratégica para jogadores de desktop (mais tempo de reação). Em telas menores, a câmera fica mais próxima do personagem.

Isso cria uma diferença de experiência entre plataformas que é funcional mas não injusta: o jogador mobile tem uma área menor de visão, mas o jogo compensa com mira automática e hitboxes maiores.

---

## 7. Onboarding Web — 5 Segundos para Entender Tudo

### A Regra dos 5 Segundos

Em 5 segundos de gameplay, o jogador precisa ter respondido internamente três perguntas:
1. "O que eu controlo?" — O personagem responde ao input
2. "O que é ameaça?" — Os zumbis se aproximam
3. "O que eu faço?" — O ataque funciona e é satisfatório

Se essas três perguntas não forem respondidas em 5 segundos, o jogador está confuso. Se ele está confuso no browser, ele fecha a aba.

### A Sequência de Onboarding Silencioso

**Segundo 0-1: Orientação**
O cidadão está parado no centro. Os zumbis aparecem nas bordas da tela caminhando lentamente para o centro. O jogador vê o personagem, vê a ameaça, percebe a distância de segurança que está diminuindo.

Nenhum texto. Nenhuma instrução. Apenas a cena.

**Segundo 1-3: Prompt de Input**
O botão de ataque (ou a vassoura do personagem, no mobile) pulsa suavemente uma vez. Não é uma animação de tutorial — é mais sutil que isso. É a linguagem do jogo dizendo "olha aqui". Em 0.3 segundos de pulsação, desaparece.

No desktop: o cursor já está visível como mira, indicando que o mouse tem função.
No mobile: a metade esquerda da tela tem um gradiente muito sutil (quase imperceptível) indicando a zona de joystick.

**Segundo 3-5: Primeiro Feedback**
O jogador toca/clica. O personagem ataca. O zumbi voa para trás. O THWACK aparece. O número de score surge. O zumbi cai e grita "Fui eleito democraticamente!".

O riso acontece. O contrato está assinado.

### O Que Não Fazer (anti-padrões eliminados)

**Não fazer: Tutorial pop-up**
"Use WASD para mover, clique para atacar, colete power-ups para..." — ninguém lê isso no browser. O pop-up é fechado antes de ser lido. E pior: ele diz ao jogador que o jogo é complicado o suficiente para precisar de explicação.

**Não fazer: Slow-motion de tutorial**
"Primeiro, mova o personagem para a esquerda..." com setas animadas. Infantiliza o jogador e destrói o flow da abertura.

**Não fazer: Bloqueio de gameplay durante instrução**
Qualquer tela, overlay ou pausa antes do primeiro input é uma barreira. O onboarding acontece DURANTE o jogo, não antes dele.

**Não fazer: Wave 1 vazia demais**
Se a primeira wave for fácil demais (um único zumbi), o jogador fica sem entender se o jogo tem substância. A wave 1 precisa ter pelo menos 3 vereadores se aproximando de direções diferentes para comunicar "vai ser tenso".

### Dica Contextual Única (se o jogador ficar parado)

Se o jogador ficar parado por mais de 3 segundos sem qualquer input, o botão de ataque pisca mais intensamente por 0.5 segundos. Apenas uma vez. Sem texto, sem seta. Um lembrete gentil, não uma instrução.

Se o jogador morrer sem nunca ter atacado, a tela de morte mostra uma única linha de texto abaixo do score: "Dica: clique/toque na tela para atacar" — apenas neste caso específico.

---

## 8. Mockups Descritivos — As 4 Telas Essenciais

### Mockup 1: Gameplay Desktop (1280x720)

```
┌────────────────────────────────────────────────────────────────────────────┐
│ ❤❤❤❤❤          WAVE 3  ·  47 restantes                    SCORE: 8.340   │  ← HUD topo, 40px altura
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│    [CONGRESSO - silhueta pulsando verde ao fundo]                          │
│                                                                            │
│         🧟 Vereador-Zumbi     🧟 Vereador-Zumbi                          │
│                "Fui eleito..."                                             │
│                                                                            │
│    [ESPELHO D'ÁGUA - zona de perigo, reflejo distorcido]                  │
│                                                                            │
│                        ☩ cursor-mira                                      │
│                                                                            │
│    [MIN. ENROLAÇÃO]   🧑 CIDADÃO   [MIN. PUXADINHO]                      │
│                     (polo azul, vassoura)                                 │
│                                                                            │
│         🧟 Senador Blindado    THWACK!                                    │
│           [escudo dourado]     ← onomatopeia no ponto de impacto          │
│                                                                            │
│    [GRAMADO SECO - casca de papel de santinho voando]                     │
│                                                                            │
│    [CÉU LARANJA-SANGUE como fundo fixo]                                   │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│ (sem elementos de UI na parte inferior — área do teclado no desktop)       │
└────────────────────────────────────────────────────────────────────────────┘

ELEMENTOS PRESENTES: ❤❤❤❤❤ (vidas), indicador de wave, score, cursor-mira
ELEMENTOS AUSENTES: joystick (desktop usa teclado), botão de ataque visível
PALETA: ceu laranja-sangue, gramado amarelo-sujo, tons sombrios dos ministérios
```

**Notas de design do mockup 1:**
O HUD superior ocupa 40px fixos. O gameplay ocupa os 680px restantes. Zero UI na parte inferior em desktop — o jogador usa teclado e mouse sem elementos na tela competindo pela atenção na área de combate. O cursor-mira substitui o cursor padrão do sistema em toda a área do canvas.

---

### Mockup 2: Gameplay Mobile Portrait (390x844)

```
┌──────────────────────┐  ← 390px largura
│ ❤❤❤❤❤  W:3  8.340  │  ← HUD topo comprimido, 36px
├──────────────────────┤
│                      │
│   [CONGRESSO fundo]  │
│                      │
│  🧟    🧟    🧟      │  ← 3 vereadores se aproximando
│                      │
│     🧑 CIDADÃO       │  ← personagem com perspectiva isométrica leve
│                      │
│  [ESPELHO D'ÁGUA]    │
│                      │  ← canvas 390x219 (16:9 preservado)
│                      │
│  [GRAMADO SECO]      │
│                      │
├──────────────────────┤  ← linha divisória sutil
│    ╔════╗            │
│    ║    ║  [ÁREA DE  │  ← zona touch esquerda (joystick dinâmico)
│    ║ JS ║  ATAQUE    │     e zona touch direita (todo o lado direito)
│    ║    ║  (direita)]│
│    ╚════╝            │
│         [PAUSE] ⏸   │  ← único botão fixo, canto sup. direito
└──────────────────────┘

SEPARAÇÃO VISUAL: canvas do jogo vs. área de controle (linha sutil de 1px)
JOYSTICK: aparece onde o polegar esquerdo toca, raio 80px, semi-transparente
ATAQUE: toda a metade direita da área de controle (não há botão específico)
```

**Notas de design do mockup 2:**
A separação entre canvas e área de controle é fundamental — o jogador não toca acidentalmente no canvas quando pretende usar os controles. A linha divisória é sutil (1px, 20% opacidade) mas presente. O joystick virtual não existe fixo — aparece apenas quando o polegar esquerdo toca a tela.

---

### Mockup 3: Tela de Resultado (Share Screen)

```
┌──────────────────────────────────┐  ← 390x844 (portrait, otimizado para screenshot)
│                                  │
│  ████ TEXTURA DE PAPEL ████████  │
│  █                            █  │
│  █   ZUMBIS DE BRASÍLIA       █  │
│  █   CONGRESSO DOS MORTOS     █  │  ← logo, corpo 28px, branco sobre fundo escuro
│  █                            █  │
│  ████████████████████████████ █  │
│                                  │
│  ╔══════════════════════════╗   │
│  ║                          ║   │
│  ║   SEU MANDATO ACABOU     ║   │  ← manchete, Bebas Neue 52px, amarelo-queimado
│  ║   (por enquanto)         ║   │  ← subtítulo, 18px, branco-sujo
│  ║                          ║   │
│  ╚══════════════════════════╝   │
│                                  │
│  ┌────────────────────────────┐ │
│  │                            │ │
│  │      14.820                │ │  ← SCORE, Bebas Neue 88px, amarelo-ouro
│  │      PONTOS                │ │
│  │                            │ │
│  └────────────────────────────┘ │
│                                  │
│  ┌────────────┬───────────────┐ │
│  │ 2min 34s   │   247 zumbis  │ │  ← stats, Oswald Bold 24px
│  │ SOBREVIVEU │   ELIMINADOS  │ │
│  ├────────────┴───────────────┤ │
│  │     WAVE 7 ALCANÇADA       │ │
│  └────────────────────────────┘ │
│                                  │
│  ╔══════════════════════════╗   │
│  ║ TÍTULO OBTIDO:           ║   │
│  ║ "DEPUTADO DOS MORTOS"    ║   │  ← título gerado, fundo verde-escuro, 22px
│  ╚══════════════════════════╝   │
│                                  │
│  [  COMPARTILHAR  ][MAIS UMA]   │  ← botões CTA, 48px altura, cor e contraste altos
│                                  │
│  congressodosmortos.com.br       │  ← URL, 14px, sempre visível no screenshot
└──────────────────────────────────┘
```

**Notas de design do mockup 3:**
Proporção 9:16 (390x844) porque é o formato de screenshot mais compartilhado — stories do Instagram e WhatsApp. A URL no rodapé é obrigatória e precisa sobreviver a qualquer crop. O score em 88px é o maior elemento — é o primeiro item que o olho vê, e é o item que gera comparação e competição.

---

### Mockup 4: Loading / Abertura (máx 3 segundos)

```
┌──────────────────────────────────┐
│                                  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ░░ FUNDO PRETO, CÉU DE NOITE ░  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│                                  │
│  [silhueta do Congresso ao fundo]│
│  [luz verde pulsando nas cúpulas]│
│                                  │
│  ┌──────────────────────────┐   │
│  │ Brasília, abril de 2026. │   │  ← texto datilografado, aparece letra a letra
│  │                          │   │     Oswald Regular, 18px, branco
│  │ O Congresso aprovou a    │   │
│  │ Emenda 666 — nenhum      │   │
│  │ parlamentar perde o cargo│   │
│  │ Nunca. Nem com a morte.  │   │
│  │                          │   │
│  │ Ninguém leu o texto.     │   │
│  │ Ninguém nunca lê.        │   │  ← último parágrafo aparece com os assets carregados
│  │                          │   │
│  │ Na madrugada seguinte,   │   │
│  │ os corredores ficaram    │   │
│  │ silenciosos.             │   │
│  │                          │   │
│  │ Depois, ficaram          │   │
│  │ barulhentos demais.█     │   │  ← cursor piscando de máquina de escrever
│  └──────────────────────────┘   │
│                                  │
│  [sem barra de progresso]        │  ← o texto É o progress indicator
│  [sem spinner]                   │
│  [sem percentual]                │
│                                  │
│  → transição direta para gameplay│  ← sem botão "clique para iniciar"
│    quando o texto termina         │
└──────────────────────────────────┘
```

**Notas de design do mockup 4:**
O loading não é uma tela de espera — é a narrativa de abertura. O tempo que o texto leva para aparecer (digitação letra a letra) mascara o loading. Não há indicador de progresso porque indicadores de progresso lembram o usuário que ele está esperando. O cursor de máquina de escrever piscando dá sensação de ao vivo, de presente. Quando o último parágrafo termina, fade suave para o gameplay — sem botão, sem confirmação.

---

## Síntese: Os 7 Princípios UX do MVP Web

1. **Zero cliques entre o link e o jogo.** O link é o botão de iniciar.

2. **O loading conta uma história.** Nenhum segundo de espera é desperdiçado.

3. **O controle responde antes do jogador terminar o pensamento.** Input lag zero percebível.

4. **A morte é cômica, não punitiva.** O jogador sai rindo, não frustrado.

5. **A tela de resultado é um cartaz de campanha satirico.** Feita para ser vista por quem não jogou.

6. **O replay começa mais rápido que a primeira partida.** O impulso de revanche não pode esfriar.

7. **O jogo coopera com o contexto do jogador.** Pausa automática ao trocar de aba. Funciona em qualquer tela. Não exige orientação específica.

---

*congressodosmortos.com.br*
*Jenova Chen — UX MVP Web | Abril 2026*
