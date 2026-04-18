# Q1-01 — HORA EXTRA: PLANO DE BACKEND
### Werner Vogels — Backend Architecture | Capitulo 1 | Abril 2026

---

> *"Everything fails, all the time. A boa noticia: um jogo que roda 100% no browser do usuario nao tem servidor pra falhar."*

---

## 1. DECISAO FUNDAMENTAL: QUEST 01 PRECISA DE BACKEND?

**Resposta direta: Nao. Quest 01 e frontend-only.**

E essa nao e uma decisao de preguica. E uma decisao de arquitetura.

### Por que nao precisa

Quest 01 e um side-scroller linear de 5-7 minutos. Sem multiplayer. Sem economia de itens. Sem estado compartilhado entre jogadores. O personagem Ze nao existe em nenhum servidor — ele existe no browser de quem esta jogando.

O checklist de "precisa de backend" falha em todos os criterios relevantes:

| Criterio | Quest 01 | Precisa de backend? |
|---|---|---|
| Multiplayer / co-op? | Nao | Nao |
| Estado persistido entre dispositivos? | Nao (por enquanto) | Nao |
| Validacao server-side de pontuacao? | Nao (sem leaderboard ainda) | Nao |
| Conteudo gerado por usuario? | Nao | Nao |
| Autenticacao? | Nao | Nao |
| Pagamento? | Nao | Nao |

Um servidor introduz: latencia, custo, um ponto de falha, um vetor de ataque, complexidade operacional, e pelo menos duas semanas a mais de trabalho. Para Quest 01, o trade-off e negativo em todas as dimensoes.

### A excecao que confirma a regra: telemetria

O PM/CEO pediu metricas. Taxa de conclusao, drop-off por wave, replay rate. Essas metricas sao criticas — sem elas o time voa cego e pode gastar semanas otimizando a coisa errada.

**A telemetria pode ser implementada sem servidor proprio.** GA4 (Google Analytics 4) e gratuito, tem SDK client-side, e vai capturar tudo que precisamos para o Cap 1 sem custo operacional. Nao e a solucao definitiva — mas e a solucao correta para o MVP.

**Conclusao: Quest 01 = frontend-only + GA4 para telemetria.**

---

## 2. AVALIACAO DE CAPABILITIES

### 2.1 Save / Load de Progresso

**Decisao: localStorage. Agora. Servidor: nunca para Cap 1.**

A Quest 01 tem um checkpoint (inicio da Wave 3). O estado a salvar e minimo:

```
{
  "checkpoint": "wave_3_start" | null,
  "hp": number,          // 0-100
  "weapons": ["broom"],  // items no inventario
  "score": number,
  "stealth_bonus": boolean
}
```

localStorage aguenta isso sem suar. Tamanho estimado: menos de 200 bytes por save slot.

**Quando vira servidor:** Nunca para save local de uma quest. Quando o jogo tiver conta de usuario e o jogador quiser continuar em outro dispositivo — ai sim. Isso e Cap 2 no minimo, provavelmente Cap 3.

**Schema de save para preparar o futuro:**

```typescript
interface QuestSaveState {
  version: 1;                          // versionar desde o inicio
  quest_id: "Q1-01";
  player_id: string;                   // UUID gerado no primeiro acesso, salvo em localStorage
  saved_at: number;                    // Unix timestamp
  checkpoint: string | null;
  hp_percent: number;
  inventory: string[];
  score: number;
  flags: Record<string, boolean>;      // stealth_used, carlao_defeated, etc.
}
```

Versionar o schema desde o primeiro dia. Quando vier a migracao para servidor, o `version` e `player_id` ja existem.

### 2.2 Telemetria de Gameplay

**Decisao: Implementar agora. E o item mais importante desta lista.**

O PM precisa de metricas. Sem telemetria o Cap 1 pode ser lançado, falhar silenciosamente, e ninguem sabe onde o funil quebrou.

GA4 cobre o necessario para o MVP sem custo e sem servidor proprio. Detalhamento completo na secao 4.

**Quando migrar:** Se o volume de eventos superar 10M/mes no GA4 (limite do plano gratuito), ou se precisar de queries ad-hoc mais complexas (ex: "quais jogadores fizeram stealth E completaram no top 10% de tempo?"). Nesse ponto, BigQuery ou ClickHouse.

### 2.3 Leaderboard / Ranking de Tempo

**Decisao: Nao implementar para Quest 01. Preparar schema.**

Leaderboard requer servidor, banco de dados, protecao minima contra cheat. Nada disso faz sentido para a quest de tutorial.

**O que fazer agora:** Calcular e salvar o score em localStorage com o schema correto para que a migracao futura seja trivial:

```typescript
interface ScoreRecord {
  quest_id: string;
  player_id: string;
  score: number;
  time_seconds: number;
  kills: number;
  hp_remaining: number;
  stealth_bonus: boolean;
  completed_at: number;
}
```

**Quando implementar leaderboard:** Q1-06 (boss final do Cap 1) ou inicio do Cap 2. Nesse ponto o jogador ja tem investimento emocional e vai querer comparar com outros.

### 2.4 Anti-Cheat / Validacao Server-Side

**Decisao: Nao. Nunca para Cap 1.**

Anti-cheat server-side para um jogo single-player gratuito no browser e over-engineering. O custo de implementacao e operacao nao se justifica. Se alguem hackear o localStorage pra ter um score alto num leaderboard que nao existe... tudo bem.

**Quando reconsiderar:** Se vier leaderboard com premio real (cash, NFT, item exclusivo). Ai sim, validar o score server-side no momento do submit. Para Cap 1, isso nao existe.

**Abordagem pratica quando vier leaderboard:** Calcular score server-side com replay dos inputs (nao dos resultados). Dificulta cheat sem exigir anticheat complexo.

### 2.5 Autenticacao

**Decisao: Anonimo agora. Auth real: Cap 2.**

Para Quest 01, gerar um `player_id` UUID no primeiro acesso e salvar em localStorage. Isso e suficiente para correlacionar sessoes do mesmo usuario sem pedir nada.

```typescript
// Executar uma vez, no boot do jogo
function getOrCreatePlayerId(): string {
  const key = "zb_player_id";
  let id = localStorage.getItem(key);
  if (!id) {
    id = crypto.randomUUID();
    localStorage.setItem(key, id);
  }
  return id;
}
```

**Quando implementar auth real:** Quando vier leaderboard persistido, save na nuvem, ou qualquer feature social. Nesse ponto, usar Supabase Auth (Google + email magic link). Nao construir auth proprio — nunca.

**LGPD:** `player_id` UUID anonimo sem vinculo a identidade real nao constitui dado pessoal. Quando vier auth com email/Google, ai entra na regulacao. Ver secao 7.

### 2.6 Analytics

**Decisao: GA4 para MVP. PostHog quando precisar de funnels por sessao.**

- **GA4**: gratuito, zero infra, tracking de eventos customizados, funciona com `gtag.js`. Ideal para o lancamento.
- **PostHog**: open-source, self-hosted ou cloud. Melhor que GA4 para analise de sessao, replay, funnels complexos. Custo: $0 self-hosted em Railway/Render, ou ~$20/mes no plano cloud ate 1M eventos.
- **Mixpanel / Amplitude**: over-engineered para este momento. Custo nao justificado antes de 50k MAU.

**Recomendacao:** GA4 agora + PostHog no lancamento publico (quando o volume de dados comecar a importar para decisoes de produto).

---

## 3. PLANO MINIMO VIAVEL — QUEST 01

### Arquitetura: Frontend-Only

```
Browser
  |
  +-- Phaser 3 (game loop)
  |     |
  |     +-- GameEventTracker (wrapper de eventos)
  |           |
  |           +-- GA4 (gtag.js) -----> Google Analytics 4
  |           |
  |           +-- localStorage ------> Save state local
  |
  +-- Vercel / Cloudflare Pages (hosting estatico)
```

Custo operacional: $0/mes.
Pontos de falha externos: apenas GA4 (se cair, o jogo continua funcionando normalmente — os eventos sao perdidos, nao o jogo).

### O que implementar no frontend agora

**1. GameEventTracker** — wrapper unico sobre GA4:

```typescript
// src/analytics/GameEventTracker.ts

export class GameEventTracker {
  private playerId: string;
  private sessionStart: number;

  constructor() {
    this.playerId = this.getOrCreatePlayerId();
    this.sessionStart = Date.now();
  }

  track(eventName: string, params: Record<string, unknown> = {}): void {
    if (typeof gtag === "undefined") return; // falha silenciosa

    gtag("event", eventName, {
      ...params,
      player_id: this.playerId,
      quest_id: "Q1-01",
      client_ts: Date.now(),
      session_duration_s: Math.floor((Date.now() - this.sessionStart) / 1000),
    });
  }

  private getOrCreatePlayerId(): string {
    const key = "zb_player_id";
    let id = localStorage.getItem(key);
    if (!id) {
      id = crypto.randomUUID();
      localStorage.setItem(key, id);
    }
    return id;
  }
}
```

**2. SaveManager** — abstrai localStorage com schema versionado:

```typescript
// src/save/SaveManager.ts

const SAVE_KEY = "zb_save_Q1-01";

export function saveQuestState(state: QuestSaveState): void {
  localStorage.setItem(SAVE_KEY, JSON.stringify(state));
}

export function loadQuestState(): QuestSaveState | null {
  const raw = localStorage.getItem(SAVE_KEY);
  if (!raw) return null;
  try {
    const parsed = JSON.parse(raw);
    if (parsed.version !== 1) return null; // schema mudou, ignorar save antigo
    return parsed as QuestSaveState;
  } catch {
    return null;
  }
}

export function clearQuestState(): void {
  localStorage.removeItem(SAVE_KEY);
}
```

### O que NAO implementar para Quest 01

- Qualquer servidor Node/Go/Python
- Banco de dados (RDS, Firestore, Supabase)
- Leaderboard
- Auth
- WebSockets
- CDN de assets propria (usar Vercel/Cloudflare Pages built-in)

---

## 4. TELEMETRIA RECOMENDADA

Esta secao e critica. O PM quer taxa de conclusao, drop-off e replay. Sem esses eventos instrumentados, nao ha como medir.

### Eventos a instrumentar — Quest 01

#### quest_started
Disparado: quando Ze se levanta da cadeira (controles liberados).

```typescript
tracker.track("quest_started", {
  mode: "cidadao",
  chapter: 1,
  quest: 1,
  is_replay: boolean,    // true se ja existia save desta quest
  referrer: document.referrer,
});
```

#### wave_started
Disparado: no inicio de cada wave.

```typescript
tracker.track("wave_started", {
  wave_number: 1 | 2 | 3,           // 1=corredor, 2=sala_reunioes, 3=escada
  wave_label: "corredor_andar",
  elapsed_s: number,                 // segundos desde quest_started
  hp_percent: number,
  has_broom: boolean,
});
```

#### wave_completed
Disparado: quando jogador avanca para a proxima area.

```typescript
tracker.track("wave_completed", {
  wave_number: number,
  wave_label: string,
  elapsed_s: number,
  hp_percent: number,
  stealth_used: boolean,             // wave 2 especifico
  kills_in_wave: number,
});
```

#### player_died
Disparado: Ze chega a 0 HP.

```typescript
tracker.track("player_died", {
  wave_number: number,
  wave_label: string,
  elapsed_s: number,
  death_cause: "burocrata_zumbi" | "carlao_zumbi" | string,
  respawn_from_checkpoint: boolean,
  total_deaths_this_run: number,
});
```

#### item_collected
Disparado: jogador pega vassoura, sanduiche ou tablet.

```typescript
tracker.track("item_collected", {
  item_id: "vassoura_palha" | "sanduiche_refeitorio" | "tablet_carlao",
  elapsed_s: number,
  wave_number: number,
});
```

#### carlao_defeated
Disparado: Carlao-Zumbi morre. Evento especial — ele e o inimigo narrativo mais importante desta quest.

```typescript
tracker.track("carlao_defeated", {
  elapsed_s: number,
  hp_percent: number,
  broom_durability_remaining: number, // 0 se a vassoura ja quebrou
  final_blow_weapon: "broom" | "fist",
});
```

#### quest_completed
Disparado: Ze passa pelo portao de seguranca.

```typescript
tracker.track("quest_completed", {
  elapsed_s: number,
  hp_percent: number,
  final_score: number,
  kills_total: number,
  stealth_bonus_earned: boolean,
  deaths_total: number,
  broom_survived: boolean,           // vassoura ainda tem durabilidade
});
```

#### quest_abandoned
Disparado: jogador fecha a aba ou volta ao menu sem completar.
Implementar via `beforeunload` + `visibilitychange`.

```typescript
tracker.track("quest_abandoned", {
  wave_number: number,               // onde estava quando saiu
  elapsed_s: number,
  hp_percent: number,
  total_deaths: number,
});
```

#### share_triggered
Disparado: jogador clica em share na tela de Game Over ou conclusao.

```typescript
tracker.track("share_triggered", {
  channel: "whatsapp" | "twitter" | "native" | "clipboard",
  score: number,
  quest_completed: boolean,
});
```

### Metricas derivadas (calculadas no GA4)

Com esses eventos, o PM pode medir:

| Metrica | Como calcular |
|---|---|
| Taxa de conclusao Q1-01 | `quest_completed` / `quest_started` |
| Drop-off por wave | `wave_started(N)` - `wave_started(N+1)` |
| Tempo medio de conclusao | media de `elapsed_s` nos `quest_completed` |
| Taxa de stealth | `stealth_bonus_earned: true` / `quest_completed` |
| Taxa de replay | `is_replay: true` nos `quest_started` |
| Ponto de morte mais comum | distribuicao de `wave_number` nos `player_died` |
| Retencao apos game over | jogadores com 2+ `quest_started` |

### Armazenamento local dos eventos (fallback)

Se GA4 estiver bloqueado (ad-blocker), os eventos devem ser acumulados em `sessionStorage` para nao se perderem completamente:

```typescript
// Em GameEventTracker.track():
// Se gtag nao disponivel, salvar em sessionStorage
const buffer = JSON.parse(sessionStorage.getItem("zb_event_buffer") ?? "[]");
buffer.push({ event: eventName, params, ts: Date.now() });
sessionStorage.setItem("zb_event_buffer", JSON.stringify(buffer.slice(-100)));
// Tentar reenviar na proxima oportunidade
```

---

## 5. ROADMAP DE EVOLUCAO

### Fase 0 — Quest 01 (agora)
- Frontend-only
- localStorage para save
- GA4 para telemetria
- `player_id` UUID anonimo
- Custo: $0

### Fase 1 — Final do Cap 1 (Q1-06, boss)
**Trigger:** Quando o jogo tiver pelo menos 500 jogadores completando Q1-06.

**O que adicionar:**
- Leaderboard simples para score do Cap 1 completo
- Stack: Supabase (Postgres) + Edge Functions
- Auth anonima via Supabase (sem login, mas persistindo `player_id` no servidor)
- Endpoint unico: `POST /api/scores` com validacao minima (score dentro de range plausivel, timestamp coerente)
- Custo estimado: $0 (Supabase free tier: 500MB banco, 2GB bandwidth, 500k Edge Function invocations)

**Por que Supabase e nao AWS:**
- Time pequeno, sem DevOps dedicado
- Free tier real (nao trial)
- Postgres nativo com Row Level Security
- SDK JavaScript com tipagem
- Deploy em 10 minutos

### Fase 2 — Lancamento publico / Cap 2
**Trigger:** 5k+ DAU ou necessidade de save na nuvem (jogador quer continuar em outro dispositivo).

**O que adicionar:**
- Auth real: Supabase Auth com Google + email magic link
- Save na nuvem sincronizado com localStorage (localStorage como cache, servidor como fonte de verdade)
- PostHog self-hosted em Railway ($5/mes) para funnels de sessao mais ricos
- Rate limiting nos endpoints publicos (Supabase tem built-in)
- Custo estimado: ~$10-20/mes (Railway para PostHog + Supabase pro se necessario)

### Fase 3 — Escala / Cap 3+
**Trigger:** 50k+ DAU, necessidade de anti-cheat em leaderboard com premio, ou features sociais (clans, co-op).

**O que adicionar:**
- Migrar telemetria para BigQuery (GA4 -> BigQuery export e gratuito ate 10GB/mes)
- CDN de assets dedicada se o bundle passar de 50MB
- Considerar server-side authoritative logic para leaderboard (recalcular score no servidor)
- Custo estimado: $50-200/mes dependendo de volume

### Fase 4 — Se virar produto sério
**Trigger:** Monetizacao real, escala de 500k+ MAU.

Ai revisitar arquitetura completa. Mas esse problema e bom de ter.

---

## 6. CUSTOS POR FASE

### Fase 0 (Quest 01 MVP)

| Servico | Plano | Custo/mes |
|---|---|---|
| Vercel / Cloudflare Pages | Free | $0 |
| Google Analytics 4 | Free (ate 10M eventos/mes) | $0 |
| **Total** | | **$0** |

### Fase 1 (leaderboard Cap 1, ~500 DAU)

| Servico | Plano | Custo/mes |
|---|---|---|
| Vercel | Free (ate 100GB bandwidth) | $0 |
| Supabase | Free tier | $0 |
| GA4 | Free | $0 |
| **Total** | | **$0** |

### Fase 2 (lancamento publico, ~5k DAU)

| Servico | Plano | Custo/mes |
|---|---|---|
| Vercel | Pro ($20/mes) ou Cloudflare Pages (free) | $0-20 |
| Supabase | Pro ($25/mes, 8GB banco) | $25 |
| PostHog | Railway self-hosted (~$5) | $5 |
| **Total** | | **$30-50** |

### Fase 3 (escala, ~50k DAU)

| Servico | Plano | Custo/mes |
|---|---|---|
| Cloudflare Pages | Free (CDN melhor que Vercel em escala) | $0 |
| Supabase | Pro + compute addon | $50-100 |
| PostHog Cloud | Growth plan | $50 |
| BigQuery | ~$5 por TB query | $5-20 |
| **Total estimado** | | **$100-170** |

**Perspectiva:** 50k DAU num jogo gratuito browser-based com $150/mes de infra e um numero excelente. A maioria dos jogos mobile com esse volume gasta $500-2000/mes.

---

## 7. RISCOS

### 7.1 LGPD — Personagens politicos reais

**Risco: alto. Mitigacao: necessaria antes do lancamento publico.**

O jogo retrata figuras politicas reais identificaveis (Bolsonaro, Lula, ministros, generais). A LGPD (Lei 13.709/2018) se aplica quando ha coleta de dados pessoais de usuarios brasileiros.

**O que e dado pessoal neste contexto:**
- Email (se vier auth)
- IP (coletado automaticamente pelo GA4 — configurar `anonymize_ip: true`)
- `player_id` UUID sozinho nao e dado pessoal (nao identifica individuo sem combinacao com outros dados)

**Acoes necessarias antes do lancamento publico:**

1. **Anonimizar IP no GA4:**
```javascript
gtag("config", "G-XXXXXXX", {
  anonymize_ip: true,
  cookie_flags: "SameSite=None;Secure",
});
```

2. **Aviso de cookies:** Ao primeiro acesso, informar que o jogo coleta dados anonimos de gameplay para melhoria. Nao precisa de banner GDPR-style elaborado para dados anonimos — mas precisa estar na politica de privacidade.

3. **Politica de Privacidade minima:** Pagina `/privacidade` com: quais dados sao coletados, para que sao usados, como o usuario pode solicitar exclusao. Isso e requisito legal mesmo sem auth.

4. **Retrato satirico vs. difamacao:** O jogo usa figuras publicas em contexto satirico claramente ficcional. Satira politica e constitucionalmente protegida no Brasil (art. 5o, IX). Manter o tom claramente satirico — nunca atribuir crimes reais nao comprovados. O "General de Pijama" como zumbi e satira. Atribuir ao personagem "ordenou assassinatos especificos" sem base factual seria outro territorio.

5. **Direitos de personalidade:** Figuras publicas tem protecao mais limitada em satira, mas qualquer uso de voz real (audio deepfake) ou imagem fotografica real aumenta o risco. Manter os personagens como caricaturas desenhadas, nao fotos.

### 7.2 Conteudo gerado por usuario

**Risco: baixo para Quest 01 (nao ha UGC).**

Se vier leaderboard com nomes customizados ou chat: implementar blocklist de palavras e limite de caracteres. Nada elaborado para este momento.

### 7.3 Ad-blockers bloqueando GA4

**Risco: medio. Impacto: subreporte de metricas.**

Usuarios tecnicos (que provavelmente sao parte do publico inicial) tendem a usar ad-blocker. GA4 pode ser bloqueado por uBlock, Brave, etc.

**Mitigacao:**
- `sessionStorage` buffer de eventos como fallback (descrito na secao 4)
- Considerar PostHog self-hosted (proprio dominio nao e bloqueado por default)
- Aceitar que as metricas do MVP vao subreportar 20-30% — e suficiente para decisoes direcionais

### 7.4 localStorage sendo limpo pelo browser

**Risco: baixo, mas real.**

Safari em modo privado, iOS com "Clear History and Website Data", Chrome com "Limpar dados de navegacao" — tudo apaga localStorage.

**Impacto para Quest 01:** Jogador perde checkpoint e tem que comecar do inicio. Aceitavel para uma quest de 7 minutos.

**Impacto para o jogo completo:** Progressao perdida e frustrante. Isso precisa de conta na nuvem no Cap 2.

### 7.5 Cheating no localStorage

**Risco: baixo. Impacto: baixo (sem leaderboard ainda).**

Quando vier leaderboard: nao validar apenas o score final. Validar o conjunto de eventos (morreu N vezes, demorou X segundos, numero de kills plausivel para o nivel). Scores estatisticamente imposssiveis sao rejeitados server-side. Isso e suficiente para 99% dos casos.

---

## 8. CONTRATOS DE EVENTO — REFERENCIA RAPIDA

Para o desenvolvedor frontend que vai instrumentar os eventos, a interface TypeScript completa:

```typescript
// src/analytics/events.ts

export interface BaseEvent {
  player_id: string;
  quest_id: "Q1-01";
  client_ts: number;
  session_duration_s: number;
}

export interface QuestStartedEvent extends BaseEvent {
  mode: "cidadao" | "politico";
  chapter: 1;
  quest: 1;
  is_replay: boolean;
  referrer: string;
}

export interface WaveStartedEvent extends BaseEvent {
  wave_number: 1 | 2 | 3;
  wave_label: "corredor_andar" | "sala_reunioes" | "escada_rolante";
  elapsed_s: number;
  hp_percent: number;
  has_broom: boolean;
}

export interface WaveCompletedEvent extends BaseEvent {
  wave_number: 1 | 2 | 3;
  wave_label: string;
  elapsed_s: number;
  hp_percent: number;
  stealth_used: boolean;
  kills_in_wave: number;
}

export interface PlayerDiedEvent extends BaseEvent {
  wave_number: 1 | 2 | 3;
  wave_label: string;
  elapsed_s: number;
  death_cause: string;
  respawn_from_checkpoint: boolean;
  total_deaths_this_run: number;
}

export interface ItemCollectedEvent extends BaseEvent {
  item_id: "vassoura_palha" | "sanduiche_refeitorio" | "tablet_carlao";
  elapsed_s: number;
  wave_number: 1 | 2 | 3;
}

export interface CarlaoDefeatedEvent extends BaseEvent {
  elapsed_s: number;
  hp_percent: number;
  broom_durability_remaining: number;
  final_blow_weapon: "broom" | "fist";
}

export interface QuestCompletedEvent extends BaseEvent {
  elapsed_s: number;
  hp_percent: number;
  final_score: number;
  kills_total: number;
  stealth_bonus_earned: boolean;
  deaths_total: number;
  broom_survived: boolean;
}

export interface QuestAbandonedEvent extends BaseEvent {
  wave_number: number;
  elapsed_s: number;
  hp_percent: number;
  total_deaths: number;
}

export interface ShareTriggeredEvent extends BaseEvent {
  channel: "whatsapp" | "twitter" | "native" | "clipboard";
  score: number;
  quest_completed: boolean;
}
```

---

## 9. SUMARIO EXECUTIVO

| Decisao | Escolha | Razao |
|---|---|---|
| Backend para Quest 01? | Nao | Zero necessidade funcional. Servidor e custo e falha sem beneficio. |
| Save state? | localStorage | Suficiente para quest de 7 min. Schema versionado para migracao futura. |
| Telemetria? | GA4 agora | Gratuito, zero infra, suficiente para metricas do PM. |
| Auth? | UUID anonimo | Correla sessoes sem pedir nada ao usuario. |
| Leaderboard? | Futuro (Q1-06+) | Supabase quando houver volume. |
| Anti-cheat? | Nao para Cap 1 | Sem premio real, sem necessidade. |
| Proximo passo real de backend? | Final do Cap 1 | Quando tiver 500 jogadores completando o capitulo. |
| Custo atual? | $0/mes | Vercel + GA4 free tiers. |
| Risco mais critico? | LGPD + retrato politico | Anonimizar IP no GA4, manter tom satirico claro, politica de privacidade antes do lancamento. |

**A regra que guia tudo:** construir agora apenas o que e necessario para saber se o jogo funciona. Se Q1-01 tiver drop-off de 60% na Wave 1, o problema nao e a falta de leaderboard — e o design da Wave 1. Metricas primeiro. Infraestrutura depois.

---

*Werner Vogels — "Build what you need, when you need it. Everything else is debt."*
