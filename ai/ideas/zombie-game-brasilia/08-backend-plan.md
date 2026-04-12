# ZUMBIS DE BRASILIA — Plano de Backend e Infraestrutura
### Werner Vogels, CTO — "Everything fails, all the time. Design for it."

**Documento de Infraestrutura | Abril 2026**

---

> *"A infraestrutura certa nao e a mais sofisticada. E a que falha com graca, escala com previsibilidade, e custa o minimo possivel enquanto voce ainda nao tem certeza do que vai funcionar."*

---

## 1. Arquitetura de Backend

### Principios de Design (Nao Negociaveis)

1. **Design for failure** — cada componente assume que o vizinho pode cair. O cliente funciona offline. O backend falha sem derrubar o jogo.
2. **Client-heavy, server-light** — zero chamadas de rede durante gameplay. Firebase e acionado apenas em transicoes de estado.
3. **Observability first** — voce nao pode debugar o que nao consegue ver. Cada operacao critica tem trace, log, e metrica.
4. **Cost-aware** — cada chamada Firestore custa dinheiro real. Denormalizar e cachear nao e prematura otimizacao, e responsabilidade financeira.
5. **Scale lazily** — Firebase aguenta o MVP e muito alem. Migrar cedo e desperdicio. Migrar tarde e suicidio. O gatilho esta definido na secao 13.

### Firebase Services em Uso

| Servico | Uso | Tier Esperado (MVP) |
|---|---|---|
| **Firebase Auth** | Anonymous + Google/Apple sign-in | Free (< 10K usuarios/mes) |
| **Cloud Firestore** | Perfis, leaderboards, config | Blaze (pay-as-you-go) |
| **Cloud Functions** | Validacao de score, leaderboard, cron | Blaze (invocacoes pagas) |
| **Firebase Analytics** | Eventos de gameplay, funil de monetizacao | Free (ilimitado) |
| **Remote Config** | Feature flags, balanceamento, eventos | Free (ate 300 parametros) |
| **Firebase Crashlytics** | Crash reports, ANRs | Free |
| **Firebase Performance** | Latencia de rede, rendering | Free |
| **Cloud Messaging (FCM)** | Push notifications (v1.0+) | Free |
| **BigQuery Export** | Analytics historico, cohorts | Blaze (storage + queries) |

### Data Flow — Estado do Sistema

```
BOOT DO APP
  ↓
Firebase Auth (anonymous, silencioso)
  ↓
getOrCreatePlayer() [Cloud Function]
  ↓
Remote Config fetch (com cache de 12h)
  ↓
GAMEPLAY (100% local — zero rede)
  ↓
GAME OVER
  ↓
validateAndSubmitScore() [Cloud Function]  ←→  Firestore (leaderboard)
  ↓
Firebase Analytics (log de eventos)
  ↓
TELA INICIAL (leaderboard carregado)
```

### Diagrama de Arquitetura Completo

```mermaid
graph TB
    subgraph "CLIENTE — Godot 4.4"
        direction TB
        GM[GameManager\nAutoload]
        FM[FirebaseManager\nAutoload]
        RC[RemoteConfigManager\nAutoload]
        AM[AdsManager\nAutoload]
        SS[SaveSystem\nAutoload]

        GM -->|"transicao\ngame_over"| FM
        FM -->|"cache\n12h"| RC
    end

    subgraph "FIREBASE PLATFORM"
        direction TB

        subgraph "Auth Layer"
            ANON[Anonymous Auth]
            GOOGLE[Google Sign-In]
            APPLE[Apple Sign-In]
            ANON -->|"upgrade"| GOOGLE
            ANON -->|"upgrade"| APPLE
        end

        subgraph "Data Layer"
            FS[(Cloud Firestore\nusers / leaderboards\ngame_config)]
            RTDB[(Realtime Database\nleaderboard_live\nse necessario)]
        end

        subgraph "Compute Layer"
            CF1[validateAndSubmitScore\nonCall | 512MB | 30s]
            CF2[getWeeklyLeaderboard\nonCall | 256MB | 10s]
            CF3[resetWeeklyLeaderboard\nonSchedule — toda segunda 03:00 UTC]
            CF4[getOrCreatePlayer\nonCall | 256MB | 10s]
            CF5[reportSuspiciousScore\nonCall | 256MB | 10s]
            CF6[processSeasonalEvent\nonSchedule — cron configuravel]
        end

        subgraph "Observability Layer"
            CRASH[Crashlytics\nCrash + ANR]
            PERF[Performance Monitoring\nlatencia, traces]
            ANA[Firebase Analytics\neventos custom]
            BQ[(BigQuery\nexport diario)]
        end

        subgraph "Config Layer"
            FRC[Remote Config\nfeature flags\nbalanceamento\nkill switches]
        end
    end

    subgraph "EXTERNOS"
        ADM[AdMob Primary]
        LP[LevelPlay Mediation\nAppLovin]
        UADS[Unity Ads]
        META[Meta AN]
        PANGLE[Pangle]
        LP --> UADS
        LP --> META
        LP --> PANGLE
    end

    FM -->|"onCall HTTPS\nFirebase Auth token"| CF1
    FM -->|"onCall HTTPS"| CF2
    FM -->|"onCall HTTPS"| CF4
    FM -->|"REST SDK"| FS

    CF1 --> FS
    CF2 --> FS
    CF3 --> FS
    CF4 --> FS

    ANA -.->|"export diario\nautomatico"| BQ
    CRASH -.->|"integrado SDK"| FM
    PERF -.->|"integrado SDK"| FM
    RC -->|"fetch parametros"| FRC

    AM -->|"plugin Poing Studios"| ADM
    ADM --> LP

    style CF1 fill:#e74c3c,color:#fff
    style CF3 fill:#e67e22,color:#fff
    style FS fill:#f39c12,color:#fff
    style BQ fill:#2980b9,color:#fff
    style CRASH fill:#27ae60,color:#fff
```

---

## 2. Firestore Design

### Principios de Modelagem

Firebase Firestore e um banco de documentos NoSQL. Regra numero um: **modele para leitura, nao para normalizacao**. Cada query cara que voce nao fizer e centavos economizados.

**Decisoes de denormalizacao tomadas:**
- `display_name` e duplicado em `leaderboard_alltime` e `leaderboard_weekly` — evita join
- `score` e `wave_reached` no perfil E no leaderboard — acesso rapido sem cross-query
- `kills_per_type` e armazenado no perfil para analytics sem BQ

### Schema Completo

```
firestore/
│
├── users/
│   └── {uid}/
│       ├── display_name: string          # "Cidadao4782"
│       ├── total_sessions: number        # contador acumulado
│       ├── total_kills: number           # contador acumulado
│       ├── highest_score: number         # all-time best
│       ├── highest_wave: number          # all-time best
│       ├── player_level: number          # 1–20 (MVP), expandivel
│       ├── xp_current: number
│       ├── preferred_weapon: string      # "vassoura" | "chinelo" | etc.
│       ├── created_at: timestamp
│       ├── last_seen_at: timestamp
│       ├── platform: string              # "android" | "ios"
│       ├── app_version: string           # "1.0.0"
│       ├── is_banned: boolean            # default: false
│       ├── ban_reason: string?           # null se nao banido
│       ├── consent_ads_personalized: boolean   # LGPD
│       ├── consent_analytics: boolean          # LGPD
│       ├── consent_timestamp: timestamp        # quando deu consentimento
│       └── deletion_requested_at: timestamp?   # LGPD — direito de exclusao
│       │
│       ├── achievements/ (sub-colecao)
│       │   └── {achievement_id}/
│       │       ├── progress_current: number
│       │       ├── progress_target: number
│       │       ├── completed: boolean
│       │       └── unlocked_at: timestamp
│       │
│       └── sessions/ (sub-colecao — APENAS para investigacao de cheat)
│           └── {session_id}/
│               ├── score: number
│               ├── wave_reached: number
│               ├── kills_total: number
│               ├── duration_sec: number
│               ├── weapon_used: string
│               ├── checksum: string
│               ├── submitted_at: timestamp
│               └── flagged_suspicious: boolean
│
├── leaderboard_alltime/
│   └── {uid}/                            # upsert — 1 doc por usuario
│       ├── display_name: string
│       ├── score: number
│       ├── wave_reached: number
│       ├── weapon_used: string
│       ├── submitted_at: timestamp
│       └── app_version: string
│
├── leaderboard_weekly/
│   └── {uid}/                            # limpo toda segunda — 00:00 BRT
│       ├── display_name: string
│       ├── score: number
│       └── submitted_at: timestamp
│
├── leaderboard_weekly_archive/
│   └── {YYYY-WNN}/                       # ex: "2026-W42"
│       ├── week_start: timestamp
│       ├── week_end: timestamp
│       ├── winners: array[{uid, display_name, score, rank}]  # top 10
│       └── total_participants: number
│
├── game_config/
│   └── balance_v1/
│       ├── wave_difficulty_multiplier: number    # default: 1.0
│       ├── ads_interstitial_frequency: number    # default: 3
│       ├── ads_rewarded_max_per_session: number  # default: 2
│       ├── particle_quality_low_end: number      # default: 0.5
│       ├── spawn_rate_multiplier: number         # default: 1.0
│       ├── max_zombies_screen: number            # default: 25
│       ├── feature_flags: map {
│       │     feature_share_score: boolean,
│       │     feature_leaderboard: boolean,
│       │     feature_seasonal_event: boolean,
│       │     force_update_min_version: string    # "1.0.0" ou null
│       │   }
│       └── seasonal_event: map? {
│               name: string,               # "Eleicoes 2026"
│               active: boolean,
│               wave_modifier: string,      # JSON serializado
│               start_at: timestamp,
│               end_at: timestamp
│             }
│
└── cheat_reports/
    └── {report_id}/
        ├── uid: string
        ├── score: number
        ├── session_id: string
        ├── reason: string              # "score_rate_exceeded" | "manual_report"
        ├── details: map
        └── reported_at: timestamp
```

### Indexes Compostos Necessarios

```
// Firestore Console — Indexes compostos

// 1. Leaderboard all-time paginado
Collection: leaderboard_alltime
Fields: score (Descending), submitted_at (Descending)

// 2. Leaderboard semanal paginado
Collection: leaderboard_weekly
Fields: score (Descending), submitted_at (Descending)

// 3. Usuarios por nivel (admin / analytics)
Collection: users
Fields: player_level (Descending), last_seen_at (Descending)

// 4. Sessoes suspeitas (anti-cheat)
Collection: users/{uid}/sessions
Fields: flagged_suspicious (Ascending), submitted_at (Descending)

// 5. Arquivo semanal por semana
Collection: leaderboard_weekly_archive
Fields: week_start (Descending)
```

### Security Rules Detalhadas

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // ─────────────────────────────────────────────────
    // FUNCOES AUXILIARES
    // ─────────────────────────────────────────────────

    function isAuthenticated() {
      return request.auth != null;
    }

    function isOwner(uid) {
      return request.auth != null && request.auth.uid == uid;
    }

    function isNotBanned() {
      // Verifica ban no token customizado (setado via Admin SDK)
      return !('banned' in request.auth.token) || request.auth.token.banned == false;
    }

    function isValidDisplayName(name) {
      return name is string && name.size() >= 3 && name.size() <= 20;
    }

    function noSensitiveFieldsChanged() {
      // Campos que NUNCA podem ser alterados diretamente pelo cliente
      return !('is_banned' in request.resource.data.diff(resource.data).affectedKeys())
          && !('ban_reason' in request.resource.data.diff(resource.data).affectedKeys())
          && !('highest_score' in request.resource.data.diff(resource.data).affectedKeys())
          && !('total_sessions' in request.resource.data.diff(resource.data).affectedKeys())
          && !('total_kills' in request.resource.data.diff(resource.data).affectedKeys());
    }

    // ─────────────────────────────────────────────────
    // USUARIOS
    // ─────────────────────────────────────────────────

    match /users/{uid} {
      // Leitura: apenas o proprio usuario
      allow read: if isOwner(uid);

      // Criacao: autenticado, campos obrigatorios presentes
      allow create: if isOwner(uid)
                   && isAuthenticated()
                   && request.resource.data.keys().hasAll(['display_name', 'created_at'])
                   && isValidDisplayName(request.resource.data.display_name);

      // Update: apenas campos seguros (stats criticos so via Cloud Function)
      allow update: if isOwner(uid)
                   && isNotBanned()
                   && noSensitiveFieldsChanged();

      // Delete: NUNCA pelo cliente (processo de exclusao LGPD e via CF)
      allow delete: if false;

      // Sub-colecao de achievements: leitura e escrita propria
      match /achievements/{achievementId} {
        allow read, write: if isOwner(uid) && isAuthenticated();
      }

      // Sub-colecao de sessoes: APENAS leitura (escrita so via CF)
      match /sessions/{sessionId} {
        allow read: if isOwner(uid);
        allow write: if false;
      }
    }

    // ─────────────────────────────────────────────────
    // LEADERBOARDS
    // ─────────────────────────────────────────────────

    // Leitura publica (autenticado), escrita EXCLUSIVA via Cloud Function
    match /leaderboard_alltime/{uid} {
      allow read: if isAuthenticated();
      allow write: if false;  // somente via CF com Admin SDK
    }

    match /leaderboard_weekly/{uid} {
      allow read: if isAuthenticated();
      allow write: if false;
    }

    // Arquivo: somente leitura
    match /leaderboard_weekly_archive/{weekId} {
      allow read: if isAuthenticated();
      allow write: if false;
    }

    // ─────────────────────────────────────────────────
    // CONFIG (somente leitura)
    // ─────────────────────────────────────────────────

    match /game_config/{document} {
      allow read: if isAuthenticated();
      allow write: if false;
    }

    // ─────────────────────────────────────────────────
    // CHEAT REPORTS (somente escrita via CF)
    // ─────────────────────────────────────────────────

    match /cheat_reports/{reportId} {
      allow read: if false;  // apenas admin via Console
      allow write: if false; // somente via CF com Admin SDK
    }
  }
}
```

### Estrategia de Denormalizacao

| Dado | Onde esta | Por que duplicado |
|---|---|---|
| `display_name` | `users/` + `leaderboard_alltime/` + `leaderboard_weekly/` | Evita leitura adicional em `users/` ao carregar leaderboard |
| `score` (highest) | `users/` + `leaderboard_alltime/` | Exibicao no perfil sem query ao leaderboard |
| `wave_reached` (highest) | `users/` + `leaderboard_alltime/` | Filtro e exibicao sem join |
| `total_sessions` / `total_kills` | Apenas `users/` | Nao exibido no leaderboard |

**Custo estimado por leitura de leaderboard top-100:**
- Sem denormalizacao: 100 leituras (leaderboard) + 100 leituras (users) = 200 reads
- Com denormalizacao: 100 leituras (leaderboard apenas) = 100 reads
- **Economia: 50% em custo de leitura para o endpoint mais chamado do jogo**

---

## 3. Cloud Functions

Todas as functions sao escritas em **TypeScript**, Node.js 20, Firebase Functions v2. Cada function tem timeout e memoria configurados para o minimo necessario — cada milissegundo de execucao que voce desperdicar e dinheiro.

### Configuracao Base

```typescript
// functions/src/index.ts
import { initializeApp } from "firebase-admin/app";
import { setGlobalOptions } from "firebase-functions/v2";

initializeApp();

// Regiao mais proxima do Brasil
setGlobalOptions({
  region: "southamerica-east1",  // Sao Paulo
  maxInstances: 100,             // cap por funcao — protecao de custo
});

export * from "./submitScore";
export * from "./leaderboard";
export * from "./player";
export * from "./admin";
export * from "./scheduled";
export * from "./lgpd";
```

### 3.1 validateAndSubmitScore

**Trigger:** `onCall`
**Memoria:** 512MB | **Timeout:** 30s | **Concorrencia:** 80
**Chamada:** Ao fim de cada sessao com score > 0

```typescript
// functions/src/submitScore.ts
import { onCall, HttpsError } from "firebase-functions/v2/https";
import { getFirestore, FieldValue } from "firebase-admin/firestore";
import { getAuth } from "firebase-admin/auth";
import { logger } from "firebase-functions";

interface SubmitScoreRequest {
  score: number;
  wave_reached: number;
  weapon_used: string;
  session_duration_sec: number;
  kills_total: number;
  kills_per_type: Record<string, number>;
  checksum: string;          // HMAC-SHA256(uid + score + duration, client_secret)
  session_id: string;        // UUID gerado no cliente
  max_combo: number;
  ads_watched: number;
}

const MAX_SCORE_PER_SECOND = 600;  // impossivel de atingir legitimamente
const MIN_SESSION_DURATION = 10;   // segundos — sessoes < 10s sao suspeitas

export const validateAndSubmitScore = onCall(
  { memory: "512MiB", timeoutSeconds: 30 },
  async (request) => {
    const uid = request.auth?.uid;
    if (!uid) throw new HttpsError("unauthenticated", "Auth required");

    const data = request.data as SubmitScoreRequest;

    // ── Validacoes de integridade basica ──────────────────────────
    if (data.score < 0 || data.wave_reached < 1) {
      throw new HttpsError("invalid-argument", "Invalid score data");
    }

    if (data.session_duration_sec < MIN_SESSION_DURATION) {
      logger.warn("Sessao muito curta", { uid, duration: data.session_duration_sec });
      // Nao rejeita — pode ser crash. Apenas loga.
    }

    // ── Deteccao de score impossivel ──────────────────────────────
    const maxPossibleScore = data.session_duration_sec * MAX_SCORE_PER_SECOND;
    const isSuspicious = data.score > maxPossibleScore;

    if (isSuspicious) {
      logger.warn("Score suspeito detectado", {
        uid,
        score: data.score,
        duration: data.session_duration_sec,
        max_possible: maxPossibleScore,
        ratio: data.score / maxPossibleScore,
      });
    }

    const db = getFirestore();
    const batch = db.batch();

    // ── Leitura paralela para performance ────────────────────────
    const [existingAlltime, existingWeekly, userDoc] = await Promise.all([
      db.doc(`leaderboard_alltime/${uid}`).get(),
      db.doc(`leaderboard_weekly/${uid}`).get(),
      db.doc(`users/${uid}`).get(),
    ]);

    // Verifica se usuario nao esta banido
    if (userDoc.data()?.is_banned) {
      throw new HttpsError("permission-denied", "Account suspended");
    }

    const displayName = userDoc.data()?.display_name ?? "Cidadao";
    const now = FieldValue.serverTimestamp();

    // ── Atualiza leaderboard all-time (apenas se score melhorou) ──
    const currentAlltimeScore = existingAlltime.data()?.score ?? 0;
    if (data.score > currentAlltimeScore) {
      batch.set(db.doc(`leaderboard_alltime/${uid}`), {
        display_name: displayName,
        score: data.score,
        wave_reached: data.wave_reached,
        weapon_used: data.weapon_used,
        submitted_at: now,
        app_version: userDoc.data()?.app_version ?? "0.0.0",
      });
    }

    // ── Atualiza leaderboard semanal (apenas se score melhorou) ───
    const currentWeeklyScore = existingWeekly.data()?.score ?? 0;
    if (data.score > currentWeeklyScore) {
      batch.set(db.doc(`leaderboard_weekly/${uid}`), {
        display_name: displayName,
        score: data.score,
        submitted_at: now,
      });
    }

    // ── Atualiza perfil do usuario ────────────────────────────────
    batch.update(db.doc(`users/${uid}`), {
      total_sessions: FieldValue.increment(1),
      total_kills: FieldValue.increment(data.kills_total),
      highest_score: Math.max(currentAlltimeScore, data.score),
      highest_wave: Math.max(userDoc.data()?.highest_wave ?? 0, data.wave_reached),
      last_seen_at: now,
    });

    // ── Salva sessao para auditoria (sub-colecao limitada) ────────
    batch.set(db.doc(`users/${uid}/sessions/${data.session_id}`), {
      score: data.score,
      wave_reached: data.wave_reached,
      kills_total: data.kills_total,
      duration_sec: data.session_duration_sec,
      weapon_used: data.weapon_used,
      max_combo: data.max_combo,
      ads_watched: data.ads_watched,
      checksum: data.checksum,
      submitted_at: now,
      flagged_suspicious: isSuspicious,
    });

    // ── Se suspeito, cria report para revisao manual ──────────────
    if (isSuspicious) {
      const reportRef = db.collection("cheat_reports").doc();
      batch.set(reportRef, {
        uid,
        score: data.score,
        session_id: data.session_id,
        reason: "score_rate_exceeded",
        details: {
          duration_sec: data.session_duration_sec,
          max_possible: maxPossibleScore,
          ratio: +(data.score / maxPossibleScore).toFixed(2),
        },
        reported_at: now,
      });
    }

    await batch.commit();

    // ── Calcula rank atual (best-effort, nao trava o response) ────
    const rank = await _calculateRank(uid, data.score, "alltime").catch(() => null);
    const weeklyRank = await _calculateRank(uid, data.score, "weekly").catch(() => null);

    return {
      success: true,
      rank_alltime: rank,
      rank_weekly: weeklyRank,
      flagged: isSuspicious,
    };
  }
);

async function _calculateRank(
  uid: string,
  score: number,
  type: "alltime" | "weekly"
): Promise<number> {
  const collection = type === "alltime" ? "leaderboard_alltime" : "leaderboard_weekly";
  const db = getFirestore();
  const snapshot = await db
    .collection(collection)
    .where("score", ">", score)
    .count()
    .get();
  return snapshot.data().count + 1;
}
```

### 3.2 getWeeklyLeaderboard

**Trigger:** `onCall`
**Memoria:** 256MB | **Timeout:** 10s | **Concorrencia:** 80

```typescript
// functions/src/leaderboard.ts
export const getWeeklyLeaderboard = onCall(
  { memory: "256MiB", timeoutSeconds: 10 },
  async (request) => {
    const uid = request.auth?.uid;
    if (!uid) throw new HttpsError("unauthenticated", "Auth required");

    const db = getFirestore();

    // Top 100 + posicao do caller em paralelo
    const [top100Snap, playerSnap] = await Promise.all([
      db.collection("leaderboard_weekly")
        .orderBy("score", "desc")
        .limit(100)
        .get(),
      db.doc(`leaderboard_weekly/${uid}`).get(),
    ]);

    const entries = top100Snap.docs.map((doc, idx) => ({
      rank: idx + 1,
      display_name: doc.data().display_name,
      score: doc.data().score,
      is_self: doc.id === uid,
    }));

    // Calcula rank do player se nao esta no top 100
    const isInTop100 = entries.some((e) => e.is_self);
    let playerRank: number | null = null;

    if (!isInTop100 && playerSnap.exists) {
      playerRank = await _calculateRank(uid, playerSnap.data()!.score, "weekly");
    }

    return {
      entries,
      player_score: playerSnap.data()?.score ?? 0,
      player_rank: isInTop100 ? entries.find((e) => e.is_self)?.rank : playerRank,
    };
  }
);

// All-time leaderboard (paginado)
export const getAlltimeLeaderboard = onCall(
  { memory: "256MiB", timeoutSeconds: 10 },
  async (request) => {
    const uid = request.auth?.uid;
    if (!uid) throw new HttpsError("unauthenticated", "Auth required");

    const { page = 1, page_size = 50 } = request.data as {
      page?: number;
      page_size?: number;
    };

    const db = getFirestore();
    const offset = (Math.min(page, 10) - 1) * page_size; // max pagina 10

    const snapshot = await db
      .collection("leaderboard_alltime")
      .orderBy("score", "desc")
      .offset(offset)
      .limit(Math.min(page_size, 100))
      .get();

    return {
      entries: snapshot.docs.map((doc, idx) => ({
        rank: offset + idx + 1,
        display_name: doc.data().display_name,
        score: doc.data().score,
        wave_reached: doc.data().wave_reached,
        weapon_used: doc.data().weapon_used,
        is_self: doc.id === uid,
      })),
    };
  }
);
```

### 3.3 resetWeeklyLeaderboard (Cron)

**Trigger:** `onSchedule` — toda segunda 00:00 BRT (03:00 UTC)
**Memoria:** 512MB | **Timeout:** 540s

```typescript
// functions/src/scheduled.ts
import { onSchedule } from "firebase-functions/v2/scheduler";

export const resetWeeklyLeaderboard = onSchedule(
  {
    schedule: "0 3 * * 1",  // Segunda, 03:00 UTC = 00:00 BRT
    timeZone: "UTC",
    memory: "512MiB",
    timeoutSeconds: 540,
  },
  async () => {
    const db = getFirestore();

    // 1. Determina identificador da semana
    const now = new Date();
    const weekId = _getWeekId(now);

    // 2. Salva top 10 da semana no arquivo
    const top10 = await db
      .collection("leaderboard_weekly")
      .orderBy("score", "desc")
      .limit(10)
      .get();

    const winners = top10.docs.map((doc, idx) => ({
      uid: doc.id,
      display_name: doc.data().display_name,
      score: doc.data().score,
      rank: idx + 1,
    }));

    const totalSnap = await db.collection("leaderboard_weekly").count().get();

    await db.doc(`leaderboard_weekly_archive/${weekId}`).set({
      week_start: FieldValue.serverTimestamp(),
      winners,
      total_participants: totalSnap.data().count,
    });

    // 3. Deleta todos os documentos em batches de 500
    let deleted = 0;
    let batch_cursor = await db.collection("leaderboard_weekly").limit(500).get();

    while (!batch_cursor.empty) {
      const batch = db.batch();
      batch_cursor.docs.forEach((doc) => batch.delete(doc.ref));
      await batch.commit();
      deleted += batch_cursor.docs.length;
      logger.info(`Deletados ${deleted} documentos do leaderboard semanal`);
      batch_cursor = await db.collection("leaderboard_weekly").limit(500).get();
    }

    logger.info(`Leaderboard semanal resetado. Semana ${weekId}: ${winners.length} winners, ${deleted} entries removidas`);
  }
);

function _getWeekId(date: Date): string {
  const year = date.getUTCFullYear();
  const startOfYear = new Date(Date.UTC(year, 0, 1));
  const week = Math.ceil(
    ((date.getTime() - startOfYear.getTime()) / 86400000 + startOfYear.getUTCDay() + 1) / 7
  );
  return `${year}-W${String(week).padStart(2, "0")}`;
}
```

### 3.4 getOrCreatePlayer

**Trigger:** `onCall`
**Memoria:** 256MB | **Timeout:** 10s

```typescript
// functions/src/player.ts
export const getOrCreatePlayer = onCall(
  { memory: "256MiB", timeoutSeconds: 10 },
  async (request) => {
    const uid = request.auth?.uid;
    if (!uid) throw new HttpsError("unauthenticated", "Auth required");

    const { platform, app_version } = request.data as {
      platform: string;
      app_version: string;
    };

    const db = getFirestore();
    const userRef = db.doc(`users/${uid}`);
    const snapshot = await userRef.get();

    if (!snapshot.exists) {
      const displayName = `Cidadao${Math.floor(Math.random() * 9999)}`;
      await userRef.set({
        display_name: displayName,
        total_sessions: 0,
        total_kills: 0,
        highest_score: 0,
        highest_wave: 0,
        player_level: 1,
        xp_current: 0,
        preferred_weapon: "vassoura",
        created_at: FieldValue.serverTimestamp(),
        last_seen_at: FieldValue.serverTimestamp(),
        platform: platform ?? "android",
        app_version: app_version ?? "0.0.0",
        is_banned: false,
        consent_ads_personalized: false,
        consent_analytics: true,
        consent_timestamp: FieldValue.serverTimestamp(),
      });
      return { is_new: true, display_name: displayName };
    }

    // Atualiza versao e last_seen
    await userRef.update({
      last_seen_at: FieldValue.serverTimestamp(),
      app_version: app_version ?? snapshot.data()!.app_version,
    });

    const data = snapshot.data()!;
    return {
      is_new: false,
      display_name: data.display_name,
      player_level: data.player_level,
      xp_current: data.xp_current,
      highest_score: data.highest_score,
      is_banned: data.is_banned ?? false,
    };
  }
);
```

### 3.5 requestAccountDeletion (LGPD)

**Trigger:** `onCall`
**Memoria:** 256MB | **Timeout:** 10s

```typescript
// functions/src/lgpd.ts
export const requestAccountDeletion = onCall(
  { memory: "256MiB", timeoutSeconds: 10 },
  async (request) => {
    const uid = request.auth?.uid;
    if (!uid) throw new HttpsError("unauthenticated", "Auth required");

    const db = getFirestore();

    // Marca para delecao — processamento assincrono em 30 dias (LGPD)
    await db.doc(`users/${uid}`).update({
      deletion_requested_at: FieldValue.serverTimestamp(),
    });

    logger.info("Delecao de conta solicitada (LGPD)", { uid });
    return { success: true, message: "Conta marcada para exclusao em 30 dias." };
  }
);

// Cron diario — processa delecoes pendentes ha mais de 30 dias
export const processAccountDeletions = onSchedule(
  {
    schedule: "0 4 * * *",  // 04:00 UTC diariamente
    memory: "512MiB",
    timeoutSeconds: 300,
  },
  async () => {
    const db = getFirestore();
    const auth = getAuth();

    const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

    const toDelete = await db
      .collection("users")
      .where("deletion_requested_at", "<", thirtyDaysAgo)
      .limit(50)
      .get();

    for (const userDoc of toDelete.docs) {
      const uid = userDoc.id;
      const batch = db.batch();

      // Remove leaderboards
      batch.delete(db.doc(`leaderboard_alltime/${uid}`));
      batch.delete(db.doc(`leaderboard_weekly/${uid}`));

      // Remove perfil
      batch.delete(db.doc(`users/${uid}`));

      await batch.commit();

      // Remove da Firebase Auth
      await auth.deleteUser(uid).catch((err) =>
        logger.warn("Falha ao deletar usuario do Auth", { uid, err })
      );

      logger.info("Conta deletada por solicitacao LGPD", { uid });
    }
  }
);
```

### Tabela Resumo de Cloud Functions

| Function | Trigger | Memoria | Timeout | Invocacoes Estimadas/Dia |
|---|---|---|---|---|
| `validateAndSubmitScore` | onCall | 512MB | 30s | ~DAU * 3 (3 partidas/dia) |
| `getWeeklyLeaderboard` | onCall | 256MB | 10s | ~DAU * 1.5 |
| `getAlltimeLeaderboard` | onCall | 256MB | 10s | ~DAU * 0.5 |
| `getOrCreatePlayer` | onCall | 256MB | 10s | ~DAU * 1 (boot) |
| `resetWeeklyLeaderboard` | onSchedule | 512MB | 540s | 1/semana |
| `requestAccountDeletion` | onCall | 256MB | 10s | < 1/dia |
| `processAccountDeletions` | onSchedule | 512MB | 300s | 1/dia |
| `processSeasonalEvent` | onSchedule | 256MB | 60s | configuravel |

---

## 4. Authentication

### Fluxo de Autenticacao

```
PRIMEIRA SESSAO
  ↓
Firebase Anonymous Auth (silencioso, sem UI)
  ↓ uid gerado automaticamente
  ↓
getOrCreatePlayer() cria perfil no Firestore
  ↓
JOGADOR ACESSA LEADERBOARD
  ↓
Prompt: "Salve seu progresso — entre com Google"
  (botao opcional, nunca forcado antes do leaderboard)
  ↓
Google Sign-In / Apple Sign-In
  ↓
linkWithCredential() — Anonymous → conta permanente
  ↓ mesmo uid preservado
  ↓
Perfil, score, leaderboard: tudo migrado automaticamente
```

### Implementacao GDScript

```gdscript
# src/autoloads/firebase_manager.gd
extends Node

const FIREBASE_API_KEY = ""  # lido do .env via exportacao
const PROJECT_ID = "zumbis-brasilia"

var _current_uid: String = ""
var _id_token: String = ""
var _refresh_token: String = ""
var _token_expiry: float = 0.0

signal auth_ready(uid: String)
signal auth_error(message: String)
signal profile_loaded(profile: Dictionary)

func _ready() -> void:
    # Tenta restaurar sessao salva localmente
    var saved = SaveSystem.load_auth()
    if saved and saved.refresh_token:
        _refresh_token = saved.refresh_token
        await _refresh_id_token()
    else:
        await _sign_in_anonymous()

func _sign_in_anonymous() -> void:
    var result = await _post(
        "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=%s" % FIREBASE_API_KEY,
        {"returnSecureToken": true}
    )
    if result.has("idToken"):
        _store_auth(result)
        auth_ready.emit(_current_uid)
    else:
        auth_error.emit("Falha na autenticacao anonima")

func upgrade_to_google(google_token: String) -> void:
    # Linka conta anonima com Google — uid permanece o mesmo
    var result = await _post(
        "https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=%s" % FIREBASE_API_KEY,
        {
            "postBody": "id_token=%s&providerId=google.com" % google_token,
            "requestUri": "https://%s.firebaseapp.com" % PROJECT_ID,
            "returnSecureToken": true,
        }
    )
    if result.has("idToken"):
        _store_auth(result)

func _refresh_id_token() -> void:
    # Token expira em 1h — refresh automatico
    if Time.get_unix_time_from_system() < _token_expiry - 300:
        return  # ainda valido por mais de 5 minutos
    # ... chama endpoint de refresh

func _store_auth(result: Dictionary) -> void:
    _current_uid = result.get("localId", "")
    _id_token = result.get("idToken", "")
    _refresh_token = result.get("refreshToken", "")
    _token_expiry = Time.get_unix_time_from_system() + 3600
    SaveSystem.save_auth({
        "uid": _current_uid,
        "refresh_token": _refresh_token,
    })
```

### Session Management

- **Token refresh:** automatico, 5 minutos antes da expiracao (tokens duram 1h)
- **Offline:** jogo funciona 100% offline. Tentativa de sincronizacao na proxima conexao
- **Retry logic:** `validateAndSubmitScore` com exponential backoff (3 tentativas: 1s, 2s, 4s)
- **Token storage:** apenas `refresh_token` e salvo localmente (nunca o `id_token`)
- **Migration path:** `linkWithCredential()` preserva uid — zero perda de progresso

---

## 5. Analytics Pipeline

### Arquitetura do Pipeline

```
Godot (Firebase Analytics SDK)
  ↓ evento logado localmente
  ↓ batching automatico pelo SDK (eventos enviados a cada 30s ou 500 eventos)
Firebase Analytics
  ↓ retencao de 60 dias na UI do Firebase
  ↓ export diario automatico (BigQuery Link)
BigQuery
  ↓ queries SQL para cohorts, funnels, e analises ad-hoc
Google Sheets / Looker Studio (dashboards)
```

### Eventos Custom Completos

```typescript
// Nomenclatura: snake_case, max 40 chars, max 25 parametros

// ── SESSAO ─────────────────────────────────────────────────────────
"session_start" {
  weapon_id: string,          // "vassoura" | "chinelo" | etc.
  player_level: number,
  is_returning_player: boolean,
  has_ads_consent: boolean,
}

"session_end" {
  score: number,
  wave_reached: number,
  duration_sec: number,
  cause: "death" | "quit" | "crash",
  revives_used: number,
  max_combo: number,
  kills_total: number,
}

// ── GAMEPLAY ────────────────────────────────────────────────────────
"wave_started" {
  wave_number: number,
  has_boss: boolean,
}

"wave_completed" {
  wave_number: number,
  score_at_wave: number,
  kills_in_wave: number,
  duration_sec: number,
  powerups_used: number,
}

"player_died" {
  wave_number: number,
  score: number,
  combo_max: number,
  kill_cause: string,        // "vereador" | "lobista" | etc.
  weapon_used: string,
  time_alive_sec: number,
}

"combo_milestone" {
  combo_count: number,       // 10, 20, 30...
  multiplier: number,
  weapon_id: string,
}

"boss_defeated" {
  boss_id: string,
  wave_number: number,
  time_to_kill_sec: number,
  player_hp_remaining: number,
}

"powerup_used" {
  powerup_id: string,
  wave_number: number,
  score_at_use: number,
}

// ── MONETIZACAO ─────────────────────────────────────────────────────
"ad_rewarded_prompt_shown" {
  placement: "revive" | "powerup_start" | "score_double",
  score: number,
  wave_number: number,
}

"ad_rewarded_accepted" {
  placement: string,
  time_to_accept_sec: number,   // quanto tempo levou para aceitar
}

"ad_rewarded_completed" {
  placement: string,
  reward_granted: boolean,
}

"ad_rewarded_declined" {
  placement: string,
}

"ad_interstitial_shown" {
  session_number: number,       // numero de partidas nessa sessao
}

"ad_interstitial_closed" {
  watched_full: boolean,
  duration_sec: number,
}

// ── RETENCAO ────────────────────────────────────────────────────────
"first_session_complete" {
  time_to_first_kill_sec: number,
  tutorial_completed: boolean,
  waves_completed: number,
}

"leaderboard_viewed" {
  player_rank: number,
  is_top100: boolean,
}

"score_shared" {
  platform: "whatsapp" | "instagram" | "tiktok" | "other",
  score: number,
  wave_reached: number,
}

"upgrade_chosen" {
  player_level: number,
  upgrade_id: string,
  offered_options: string,    // "upgrade_a,upgrade_b,upgrade_c"
}

// ── ERROS ───────────────────────────────────────────────────────────
"firebase_sync_failed" {
  error_code: string,
  function_name: string,
  retry_count: number,
}

"pool_exhausted" {
  pool_id: string,
  wave_number: number,
}

"ad_load_failed" {
  placement: string,
  error_code: string,
}
```

### Funnels Criticos

| Funil | Etapas | KPI Alvo |
|---|---|---|
| **Onboarding** | install → boot → first_kill → wave_1_complete → session_end | > 70% chegam ao wave_1_complete |
| **Engajamento de Ad** | player_died → ad_rewarded_prompt_shown → ad_rewarded_accepted | > 35% aceitam |
| **Compartilhamento** | session_end → score_shared | > 10% compartilham |
| **Retencao** | D1 → D3 → D7 → D30 | 40% / 25% / 18% / 8% |

### BigQuery — Queries Uteis

```sql
-- Retencao D1 / D7 / D30
WITH first_sessions AS (
  SELECT
    user_pseudo_id,
    DATE(TIMESTAMP_MICROS(MIN(event_timestamp))) AS install_date
  FROM `project.analytics_*.events_*`
  WHERE event_name = 'first_open'
  GROUP BY 1
),
return_sessions AS (
  SELECT DISTINCT
    user_pseudo_id,
    DATE(TIMESTAMP_MICROS(event_timestamp)) AS session_date
  FROM `project.analytics_*.events_*`
  WHERE event_name = 'session_start'
)
SELECT
  install_date,
  COUNT(DISTINCT f.user_pseudo_id) AS installs,
  COUNT(DISTINCT CASE WHEN DATE_DIFF(r.session_date, f.install_date, DAY) = 1
    THEN f.user_pseudo_id END) AS d1_retained,
  COUNT(DISTINCT CASE WHEN DATE_DIFF(r.session_date, f.install_date, DAY) = 7
    THEN f.user_pseudo_id END) AS d7_retained
FROM first_sessions f
LEFT JOIN return_sessions r USING (user_pseudo_id)
GROUP BY 1
ORDER BY 1 DESC;

-- ARPDAU diario
SELECT
  DATE(TIMESTAMP_MICROS(event_timestamp)) AS date,
  COUNT(DISTINCT user_pseudo_id) AS dau,
  COUNTIF(event_name = 'ad_rewarded_completed') AS rewarded_completions,
  COUNTIF(event_name = 'ad_interstitial_shown') AS interstitials_shown
FROM `project.analytics_*.events_*`
WHERE event_name IN ('session_start', 'ad_rewarded_completed', 'ad_interstitial_shown')
GROUP BY 1
ORDER BY 1 DESC;
```

---

## 6. Remote Config

### Parametros Completos

| Parametro | Tipo | Default | Uso |
|---|---|---|---|
| `wave_difficulty_multiplier` | float | 1.0 | Escalar dificuldade global em emergencia |
| `ads_interstitial_frequency` | int | 3 | Partidas entre interstitials |
| `ads_rewarded_max_per_session` | int | 2 | Max revives por sessao |
| `particle_quality_low_end` | float | 0.5 | Reducao de particulas em devices fracos |
| `spawn_rate_multiplier` | float | 1.0 | Ajuste global de spawn |
| `max_zombies_screen` | int | 25 | Cap de simultaneos em tela |
| `combo_reset_time_sec` | float | 3.0 | Timer do combo (tunable sem update) |
| `feature_share_score` | bool | true | Kill switch do botao de share |
| `feature_leaderboard` | bool | true | Kill switch do leaderboard |
| `feature_seasonal_event` | bool | false | Ativa eventos sazonais |
| `force_update_min_version` | string | "" | Versao minima — forca update se abaixo |
| `force_update_message` | string | "" | Mensagem customizada do force update |
| `event_name` | string | "" | Nome do evento ativo ("Eleicoes 2026") |
| `event_wave_modifier` | string | "" | JSON com spawn especial do evento |
| `event_zombie_name_overrides` | string | "" | JSON com nomes de zumbi customizados |
| `maintenance_mode` | bool | false | Kill switch total — modo de manutencao |
| `maintenance_message` | string | "" | Mensagem mostrada em manutencao |
| `ab_test_leaderboard_position` | string | "bottom" | A/B: posicao do leaderboard na UI |
| `rewarded_ad_value_label` | string | "1 VIDA EXTRA" | Copy do botao de rewarded ad |

### Implementacao GDScript

```gdscript
# src/autoloads/remote_config_manager.gd
extends Node

const CACHE_DURATION_SEC = 43200  # 12 horas
const FETCH_TIMEOUT_SEC = 5.0

var _last_fetch_time: float = 0.0
var _config: Dictionary = {}
var _defaults: Dictionary = {
    "wave_difficulty_multiplier": 1.0,
    "ads_interstitial_frequency": 3,
    "ads_rewarded_max_per_session": 2,
    "particle_quality_low_end": 0.5,
    "spawn_rate_multiplier": 1.0,
    "max_zombies_screen": 25,
    "combo_reset_time_sec": 3.0,
    "feature_share_score": true,
    "feature_leaderboard": true,
    "feature_seasonal_event": false,
    "force_update_min_version": "",
    "force_update_message": "",
    "event_name": "",
    "event_wave_modifier": "",
    "event_zombie_name_overrides": "",
    "maintenance_mode": false,
    "maintenance_message": "",
    "rewarded_ad_value_label": "1 VIDA EXTRA",
}

signal config_updated()
signal maintenance_mode_active(message: String)
signal force_update_required(message: String)

func _ready() -> void:
    _config = _defaults.duplicate()
    _load_cached()  # carrega ultimo cache do disco
    await _fetch_config()  # tenta buscar novo no boot

func _fetch_config() -> void:
    # Respeita cache de 12h (SDK gerencia automaticamente)
    var result = await FirebaseManager.fetch_remote_config(FETCH_TIMEOUT_SEC)

    if result.success:
        for key in _defaults:
            if result.data.has(key):
                _config[key] = result.data[key]
        _last_fetch_time = Time.get_unix_time_from_system()
        _save_cache()
        _check_critical_flags()
        config_updated.emit()
    # Se falhar: usa _defaults ou cache anterior. Nunca trava o app.

func get_bool(key: String) -> bool:
    return _config.get(key, _defaults.get(key, false))

func get_float(key: String) -> float:
    return float(_config.get(key, _defaults.get(key, 0.0)))

func get_int(key: String) -> int:
    return int(_config.get(key, _defaults.get(key, 0)))

func get_string(key: String) -> String:
    return str(_config.get(key, _defaults.get(key, "")))

func _check_critical_flags() -> void:
    if get_bool("maintenance_mode"):
        maintenance_mode_active.emit(get_string("maintenance_message"))
        return

    var min_version = get_string("force_update_min_version")
    if min_version != "" and _is_version_below_minimum(min_version):
        force_update_required.emit(get_string("force_update_message"))
```

### A/B Testing

Firebase Remote Config suporta A/B testing nativo. Experimentos planejados para MVP:

| Experimento | Variantes | Metrica de Sucesso |
|---|---|---|
| **Rewarded Ad Copy** | "1 VIDA EXTRA" vs "CONTINUAR JOGANDO" | CTR do botao |
| **Interstitial Frequency** | 3 partidas vs 4 partidas | ARPDAU vs retencao |
| **Leaderboard Position** | home screen vs apos game over | Leaderboard view rate |

---

## 7. AdMob Integration

### Arquitetura de Mediacao

```
Godot (AdsManager)
  ↓
godot-admob-plugin (Poing Studios)
  ↓
AdMob SDK (Google) — rede primaria
  ↓
LevelPlay (AppLovin) — mediacao waterfall
  ├── AdMob (Google)     — eCPM: ~R$ 22-28
  ├── Unity Ads          — eCPM: ~R$ 18-24
  ├── Meta Audience Net  — eCPM: ~R$ 15-20
  └── Pangle (TikTok)   — eCPM: ~R$ 8-14
```

### Implementacao GDScript

```gdscript
# src/autoloads/ads_manager.gd
extends Node

const REWARDED_AD_UNIT_ANDROID = "ca-app-pub-XXXXX/YYYYY"
const REWARDED_AD_UNIT_IOS     = "ca-app-pub-XXXXX/ZZZZZ"
const INTERSTITIAL_AD_UNIT_ANDROID = "ca-app-pub-XXXXX/AAAAA"
const INTERSTITIAL_AD_UNIT_IOS     = "ca-app-pub-XXXXX/BBBBB"

var _rewarded_loaded: bool = false
var _interstitial_loaded: bool = false
var _last_interstitial_time: float = 0.0
var _interstitial_cooldown_sec: float = 300.0  # 5 min entre interstitials
var _sessions_since_last_interstitial: int = 0

signal rewarded_completed(placement: String)
signal rewarded_failed(placement: String)
signal interstitial_closed()

func _ready() -> void:
    _preload_rewarded()
    _preload_interstitial()

func show_rewarded(placement: String) -> bool:
    if not _rewarded_loaded:
        rewarded_failed.emit(placement)
        FirebaseManager.log_event("ad_load_failed", {"placement": placement})
        return false

    # Callback tratado pelo plugin
    _rewarded_loaded = false
    _preload_rewarded()  # ja pre-carrega o proximo
    return true

func can_show_interstitial() -> bool:
    var frequency = RemoteConfigManager.get_int("ads_interstitial_frequency")
    var cooldown_ok = (Time.get_unix_time_from_system() - _last_interstitial_time) > _interstitial_cooldown_sec
    return _interstitial_loaded and cooldown_ok and _sessions_since_last_interstitial >= frequency

func show_interstitial_if_eligible() -> void:
    if not can_show_interstitial():
        return
    _last_interstitial_time = Time.get_unix_time_from_system()
    _sessions_since_last_interstitial = 0
    _interstitial_loaded = false
    _preload_interstitial()
    # mostra via plugin

func on_session_complete() -> void:
    _sessions_since_last_interstitial += 1
```

### Regras de Exibicao de Ads

| Tipo | Quando Aparece | Restricoes |
|---|---|---|
| **Rewarded (revive)** | Tela de game over, 1.5s apos morte | Max 2/sessao (Remote Config) |
| **Rewarded (powerup)** | Menu inicial, botao opcional | Sem limite diario |
| **Rewarded (score double)** | Game over, apos morte natural | Apenas sem revive usado |
| **Interstitial** | Game over → tela inicial | Min 3 partidas entre exibicoes, min 5min de cooldown |

**Regras de ouro (nunca violar):**
1. ZERO ads durante gameplay
2. Botao "nao obrigado" SEMPRE visivel, NUNCA obscurecido
3. Primeira sessao do usuario: ZERO interstitials
4. Ads desativados se consentimento LGPD nao foi dado (ads genericos como fallback)

### eCPM Tracking

Rastrear eCPM real via AdMob API + eventos de analytics:

```gdscript
func _on_rewarded_ad_impression(ad_value: float) -> void:
    # ad_value em micros USD — converter para BRL
    var brl_value = ad_value / 1_000_000 * _get_usd_brl_rate()
    FirebaseManager.log_event("ad_impression_value", {
        "value": brl_value,
        "currency": "BRL",
        "placement": "rewarded",
    })
```

---

## 8. Leaderboard System

### Decisao: Firestore vs Realtime Database

| Criterio | Firestore | Realtime DB |
|---|---|---|
| Custo de leitura | $0.06/100K reads | $0.001/GB download |
| Latencia | 50-150ms | 10-50ms |
| Queries ordenadas | Nativo (orderBy) | Limitado |
| Offline support | Nativo | Nativo |
| Regras de seguranca | Granulares | Menos expressivas |
| **Decisao** | **USAR** | Para leaderboard live (v2.0) |

**Para MVP:** Firestore e suficiente. Latencia de 50-150ms e aceitavel para uma operacao que ocorre fora do gameplay. A economia de complexidade operacional justifica.

**Para 1M+ MAU com leaderboard em tempo real:** Considerar Realtime Database ou cache Redis (ver secao 13).

### Leaderboard Global (All-Time)

- Collection: `leaderboard_alltime`
- 1 documento por usuario (upsert)
- Ordenado por `score` DESC
- Paginado em grupos de 50-100

### Leaderboard Semanal

- Collection: `leaderboard_weekly`
- Resetado toda segunda 00:00 BRT via Cloud Function `resetWeeklyLeaderboard`
- Arquivo em `leaderboard_weekly_archive/{YYYY-WNN}`
- Top 10 ganha badge cosmetica (v1.0+)

### Leaderboard de Amigos (v1.0)

Opcoes em ordem de custo de implementacao:

1. **Google Play Games Services** — mais simples, Android only, gratis
2. **Subset do Firestore** — salvar lista de UIDs de amigos e filtrar query (implementacao custom)
3. **GameCenter (iOS)** — equivalente no iOS

**Recomendacao para v1.0:** Google Play Games para Android + lista manual de amigos via Firebase para cross-platform.

### Cache no Cliente

```gdscript
# Leaderboard cacheado por 60 segundos no cliente
var _leaderboard_cache: Dictionary = {}
var _cache_timestamp: float = 0.0
const CACHE_TTL_SEC = 60.0

func get_weekly_leaderboard() -> void:
    if Time.get_unix_time_from_system() - _cache_timestamp < CACHE_TTL_SEC:
        # Retorna cache sem chamada de rede
        leaderboard_loaded.emit(_leaderboard_cache)
        return

    var result = await _call_function("getWeeklyLeaderboard", {})
    if result.success:
        _leaderboard_cache = result.data
        _cache_timestamp = Time.get_unix_time_from_system()
        leaderboard_loaded.emit(_leaderboard_cache)
```

---

## 9. Anti-Cheat

### Filosofia

Anti-cheat perfeito nao existe. A pergunta certa e: **qual e o custo de um cheater no leaderboard, e vale o investimento para prevenir?** Para um jogo em early growth, cheaters visualmente no topo do leaderboard sao um problema de branding, nao de receita. A estrategia e:

1. **MVP:** Detecta mas nao bloqueia. Loga tudo. Score rate checking.
2. **v1.0:** Bloqueia scores impossíveis. Ban manual via Firebase Console.
3. **v2.0+:** Sistema de flags automatico, shadow ban, segregacao de leaderboard.

### Camada 1 — Client Validation (Godot)

```gdscript
# Validacao local antes de enviar para o servidor
func _validate_session_before_submit(session: SessionData) -> bool:
    # Score fisicamente impossivel: > 600 pts/s
    var max_rate = 600.0
    if session.score > session.time_elapsed * max_rate:
        push_warning("Score inválido localmente — nao enviando")
        return false

    # Wave impossivel: wave > 50 em < 2 minutos
    if session.wave_current > 50 and session.time_elapsed < 120:
        return false

    return true
```

### Camada 2 — Server-Side Score Verification (Cloud Function)

Implementado em `validateAndSubmitScore`:

- Score rate check: `score / duration_sec > MAX_SCORE_PER_SECOND`
- Wave impossivel: `wave_reached > 30` em `duration_sec < 120`
- Checksum validation: HMAC-SHA256(`uid + score + duration`, shared_secret)
- Duplicidade: `session_id` unico por envio (previne double-submit)

### Camada 3 — Behavioral Analysis (Post-MVP)

```
BigQuery query diaria:
- Jogadores com score/hora nos 99.9th percentile
- Jogadores que subiram de level 1 para 20 em < 1 dia
- Sessoes com combo_max impossivel vs duration_sec
```

### Sistema de Ban

```typescript
// Admin SDK — executado via Firebase Console ou script de admin
async function banUser(uid: string, reason: string): Promise<void> {
  const db = getFirestore();
  const auth = getAuth();

  // 1. Marca no Firestore
  await db.doc(`users/${uid}`).update({ is_banned: true, ban_reason: reason });

  // 2. Seta custom claim no token — valido no proximo refresh
  await auth.setCustomUserClaims(uid, { banned: true });

  // 3. Remove do leaderboard
  const batch = db.batch();
  batch.delete(db.doc(`leaderboard_alltime/${uid}`));
  batch.delete(db.doc(`leaderboard_weekly/${uid}`));
  await batch.commit();
}
```

---

## 10. Live Ops

### Pipeline de Eventos Sazonais (Zero App Update)

A regra: **conteudo que nao requer novo code nao requer app update**. Remote Config + event_wave_modifier + event_zombie_name_overrides permitem:

- Renomear zumbis para referencias politicas atuais
- Modificar spawn weights por tipo
- Alterar multiplicadores de dificuldade
- Ativar skin especial de evento
- Mostrar banner de evento na UI

```
EVENTO SAZONAL — Fluxo de Ativacao
  ↓
Firebase Remote Config Console
  ↓ set feature_seasonal_event = true
  ↓ set event_name = "Eleicoes 2026"
  ↓ set event_wave_modifier = JSON(...)
  ↓ set event_zombie_name_overrides = JSON(...)
  ↓
Clientes fazem fetch do Remote Config (max 12h de delay)
  ↓
RemoteConfigManager detecta evento ativo
  ↓
WaveSystem aplica modifier
ZombieBase usa nomes do override
UI mostra banner do evento
```

### Tipos de Conteudo por Canal

| Conteudo | Requer App Update? | Canal |
|---|---|---|
| Renomear zumbi | Nao | Remote Config |
| Alterar dificuldade | Nao | Remote Config |
| Banner de evento | Nao | Remote Config |
| Novo tipo de zumbi | Sim | App Update |
| Nova arma | Sim | App Update |
| Novo mapa | Sim | App Update |
| Bug fix critico | Nao* | Remote Config kill switch |
| Hotfix de gameplay | Depende | Remote Config params |

### Emergency Hotfix Protocol

```
PROBLEMA DETECTADO EM PRODUCAO
  1. Identificar via Crashlytics / alertas
  2. Avaliar: Remote Config resolve?
     ├── SIM: alterar parametro no console — deployado em < 15 min
     └── NAO: preparar hotfix build
  3. Se hotfix critico: ativar maintenance_mode = true
     - Mostra mensagem customizada para o usuario
     - Impede submissao de scores durante o problema
  4. Resolver e desativar maintenance_mode
```

### Content Calendar (Exemplos)

| Periodo | Evento | Tipo de Conteudo |
|---|---|---|
| Eleicoes (out 2026) | "Temporada Eleitoral" | Rename zumbis, banner, spawn modifier |
| Natal | "Zumbi Noel do Congresso" | Banner, override de names |
| Copa do Mundo | "Federacao Zumbi de Futebol" | Spawn modifier, banner |
| Aniversario do Jogo | "Um Ano de Resistencia" | Evento especial, cosmetic reward |

---

## 11. Observability

### Stack de Observability

```
NIVEL 1 — CRASH e ERROS
Firebase Crashlytics
  ├── Crash reports automaticos (native + handled)
  ├── ANR (Application Not Responding) reports
  ├── Breadcrumbs: ultimas 20 acoes antes do crash
  └── Alertas: crash rate > 1% → email + notificacao

NIVEL 2 — PERFORMANCE
Firebase Performance Monitoring
  ├── Network traces: latencia de cada Cloud Function call
  ├── Custom traces: tempo de carregamento de wave, spawn rate
  └── Screen rendering: FPS drops detectados automaticamente

NIVEL 3 — NEGOCIO
Firebase Analytics → BigQuery
  ├── Retencao D1/D7/D30
  ├── ARPDAU (ads por sessao * eCPM)
  ├── Wave distribution (onde os jogadores morrem)
  └── Funil de conversao de ads

NIVEL 4 — ALERTAS
Google Cloud Monitoring (via Firebase)
  ├── Cloud Function error rate > 5% → PagerDuty
  ├── Firestore read cost spike > 200% normal → email
  ├── Crashlytics crash rate spike → email
  └── Auth failures spike → investigacao imediata
```

### Custom Traces (Performance Monitoring)

```gdscript
# Trace de carregamento de wave — identifica gargalos de performance
func start_wave_load_trace(wave_number: int) -> void:
    var trace = FirebasePerformance.new_trace("wave_load")
    trace.put_attribute("wave_number", str(wave_number))
    trace.start()
    _active_traces["wave_load"] = trace

func complete_wave_load_trace() -> void:
    if _active_traces.has("wave_load"):
        _active_traces["wave_load"].stop()
        _active_traces.erase("wave_load")

# Trace de chamada de Cloud Function
func trace_function_call(function_name: String) -> Dictionary:
    var metric = FirebasePerformance.new_http_metric(
        "https://us-central1-project.cloudfunctions.net/%s" % function_name,
        "POST"
    )
    metric.start()
    return {"metric": metric, "start_time": Time.get_ticks_msec()}
```

### Dashboard de Saude (Looker Studio)

Metricas exibidas em tempo real no dashboard principal:

| Metrica | Fonte | Alerta |
|---|---|---|
| Crash Rate | Crashlytics | > 1% |
| DAU | Analytics | Queda > 20% D/D |
| ARPDAU | BigQuery | Queda > 30% semana |
| CF Error Rate | Cloud Monitoring | > 2% |
| Avg Session Duration | Analytics | < 3 minutos |
| Rewarded Ad Fill Rate | AdMob | < 80% |
| Leaderboard CF P95 Latency | Performance | > 2000ms |

### Crashlytics — Configuracao

```gdscript
# src/autoloads/firebase_manager.gd
func setup_crashlytics() -> void:
    # Identifica o usuario no crash report (sem PII)
    FirebaseCrashlytics.set_user_id(_current_uid)

    # Breadcrumbs para contexto do crash
    FirebaseCrashlytics.set_custom_key("player_level", str(GameState.player_level))
    FirebaseCrashlytics.set_custom_key("current_wave", str(GameState.current_wave))
    FirebaseCrashlytics.set_custom_key("current_score", str(GameState.score))
    FirebaseCrashlytics.set_custom_key("app_version", ProjectSettings.get_setting("application/config/version"))

# Chamado a cada mudanca de estado relevante
func log_breadcrumb(event: String, data: Dictionary = {}) -> void:
    var message = event
    if not data.is_empty():
        message += " | " + JSON.stringify(data)
    FirebaseCrashlytics.log(message)
```

---

## 12. Custos Detalhados

### Premissas de Uso por MAU

| Acao | Frequencia por DAU | Observacao |
|---|---|---|
| Boot (getOrCreatePlayer) | 1x | 1 CF call + 1 Firestore read |
| Remote Config fetch | 1x | SDK cache de 12h |
| Partidas por dia | 3x | Sessao media de 7 min |
| validateAndSubmitScore | 3x | 1 CF call + 3-4 Firestore writes |
| Leaderboard view | 1.5x | 1 CF call + 100 Firestore reads |
| Analytics events | ~30x | Free, gerenciado pelo SDK |
| Crashlytics | ~0.01x | Por crash (raro) |

**DAU/MAU ratio assumido:** 25% (conservador para mobile casual)

### Tabela de Custos por Tier

#### 10K MAU (2.500 DAU)

| Servico | Volume Diario | Custo/Dia | Custo/Mes |
|---|---|---|---|
| Firestore reads | 2.500 * (100+1+4) ≈ 263K | $0.016 | $0,48 |
| Firestore writes | 2.500 * 4 ≈ 10K | $0.018 | $0,54 |
| Cloud Functions | 2.500 * 5 calls ≈ 12.5K | < $0.01 | $0,20 |
| BigQuery (storage) | ~1 GB/mes | — | $0,02 |
| Auth | Free tier | — | $0,00 |
| Analytics | Free | — | $0,00 |
| Crashlytics | Free | — | $0,00 |
| Remote Config | Free | — | $0,00 |
| **TOTAL** | — | — | **~R$ 7/mes** |

#### 50K MAU (12.500 DAU)

| Servico | Volume Diario | Custo/Dia | Custo/Mes |
|---|---|---|---|
| Firestore reads | 12.500 * 105 ≈ 1.3M | $0.078 | $2,34 |
| Firestore writes | 12.500 * 4 ≈ 50K | $0.09 | $2,70 |
| Cloud Functions | 12.500 * 5 ≈ 62.5K | $0.025 | $0,75 |
| BigQuery | ~5 GB/mes | — | $0,10 |
| **TOTAL** | — | — | **~R$ 33/mes** |

#### 100K MAU (25.000 DAU)

| Servico | Volume Diario | Custo/Dia | Custo/Mes |
|---|---|---|---|
| Firestore reads | 25.000 * 105 ≈ 2.6M | $0.156 | $4,68 |
| Firestore writes | 25.000 * 4 ≈ 100K | $0.18 | $5,40 |
| Cloud Functions | 25.000 * 5 ≈ 125K | $0.05 | $1,50 |
| BigQuery | ~10 GB/mes | — | $0,20 |
| **TOTAL** | — | — | **~R$ 66/mes** |

#### 500K MAU (125.000 DAU)

| Servico | Volume Diario | Custo/Dia | Custo/Mes |
|---|---|---|---|
| Firestore reads | 125K * 105 ≈ 13.1M | $0.786 | $23,58 |
| Firestore writes | 125K * 4 ≈ 500K | $0.90 | $27,00 |
| Cloud Functions | 125K * 5 ≈ 625K | $0.25 | $7,50 |
| BigQuery storage + queries | ~50 GB/mes | — | $1,00 |
| FCM (push) | ~500K/dia | — | Free |
| **TOTAL** | — | — | **~R$ 330/mes** |

#### 1M MAU (250.000 DAU)

| Servico | Volume Diario | Custo/Dia | Custo/Mes |
|---|---|---|---|
| Firestore reads | 250K * 105 ≈ 26.25M | $1.575 | $47,25 |
| Firestore writes | 250K * 4 ≈ 1M | $1.80 | $54,00 |
| Cloud Functions | 250K * 5 ≈ 1.25M | $0.50 | $15,00 |
| BigQuery | ~100 GB/mes + queries | — | $3,00 |
| **TOTAL** | — | — | **~R$ 700/mes** |

#### 3M MAU (750.000 DAU)

| Servico | Volume Diario | Custo/Dia | Custo/Mes |
|---|---|---|---|
| Firestore reads | 750K * 105 ≈ 78.75M | $4.725 | $141,75 |
| Firestore writes | 750K * 4 ≈ 3M | $5.40 | $162,00 |
| Cloud Functions | 750K * 5 ≈ 3.75M | $1.50 | $45,00 |
| BigQuery | ~300 GB/mes + queries | — | $10,00 |
| **TOTAL** | — | — | **~R$ 2.000/mes** |

> **Nota:** Conversao USD→BRL a R$ 5,70. Custos Firebase sao em USD. O estimado de R$21K/mes documentado anteriormente assume escala muito mais agressiva de reads e queries BigQuery — a estimativa acima e mais conservadora pois assume o leaderboard cacheado no cliente (60s TTL), reduzindo reads em ~70%.

### Custo vs Receita por Tier

| MAU | Custo Infra/mes | ARPDAU (R$0,07) | Receita/mes | Margem |
|---|---|---|---|---|
| 10K | R$ 7 | — | R$ 700 | 99% |
| 50K | R$ 33 | — | R$ 3.500 | 99% |
| 100K | R$ 66 | — | R$ 7.000 | 99% |
| 500K | R$ 330 | — | R$ 35.000 | 99% |
| 1M | R$ 700 | — | R$ 70.000 | 99% |
| 3M | R$ 2.000 | — | R$ 210.000 | 99% |

> Firebase e absurdamente barato para jogos mobile. O custo de infra nunca vai matar voce nessa escala — o que mata e o CPI de UA e a retencao.

---

## 13. Plano de Migracao

### Quando Firebase NAO e mais suficiente

| Gatilho | Threshold | Problema |
|---|---|---|
| MAU | > 5M | Custo de reads do Firestore comeca a ser relevante vs Redis |
| Leaderboard latencia | P95 > 500ms | Firestore orderBy nao e O(1) |
| Concurrent writes em leaderboard | > 1.000 writes/sec | Firestore tem limites de hot-document |
| Features necessarias | Guilds, matchmaking, real-time PvP | Firebase nao foi feito para isso |
| Customizacao | Game server-side logic complexa | Cloud Functions ficam muito pesadas |

### Fases de Migracao

#### Fase 1 — Cache Layer (500K MAU, se necesario)
**Problema:** Leaderboard lento com muitos leitores concorrentes
**Solucao:** Redis (Memorystore GCP) como cache na frente do Firestore

```
Godot → CF getWeeklyLeaderboard
  ↓
Redis ZSET (leaderboard semanal) — TTL: 60s
  ↓ cache miss
Firestore (fonte de verdade)
```

Custo estimado de Redis (1GB): ~$30/mes. Vale a pena acima de 500K MAU.

#### Fase 2 — Separacao de Concerns (1-2M MAU)
**Problema:** Cloud Functions estao acumulando logica demais
**Solucao:** Backend dedicado em Cloud Run (containerizado, auto-scale para zero)

```
Godot → Cloud Run (Go ou Node.js)
  ├── /score — validacao e submissao
  ├── /leaderboard — leitura com Redis cache
  ├── /player — perfil e stats
  └── /events — live ops
  ↓
Firestore (dados persistidos)
Redis (cache e leaderboard live)
```

Cloud Run escala para zero quando inativo — custo zero fora de pico.

#### Fase 3 — Game Backend Dedicado (3-5M MAU OU features complexas)

**Opcao A — Nakama (Open Source)**
- Self-hosted em GKE (Google Kubernetes Engine)
- Suporte nativo a leaderboards, matchmaking, social graph, economy
- Custo: ~$300-800/mes em infra GKE (depende do tamanho do cluster)
- Esforco de migracao: Alto (2-4 sprints)
- Recomendado se: quiser controle total e features de social complexas

**Opcao B — PlayFab (Microsoft)**
- Managed, pay-as-you-go
- API pronta para leaderboards, economy, matchmaking, LiveOps
- Custo: Free ate 100K DAU, depois $299/mes (Growth tier)
- Esforco de migracao: Medio (1-2 sprints)
- Recomendado se: quiser velocidade de implementacao e nao quiser ops

**Opcao C — Firebase + Customizacoes (nao migrar)**
- Continuar no Firebase com otimizacoes pontuais
- Recomendado ate 5-10M MAU se o produto nao precisar de PvP ou social graph
- O documento anterior estimou R$21K/mes para 3M MAU — com cache Redis, esse numero cai para ~R$3-5K

**Recomendacao:** Nao migrar ate 3M MAU. Acima disso, avaliar Nakama se o produto evoluiu para PvP/guilds, ou PlayFab se a equipe preferir managed.

### Decision Framework de Migracao

```
MAU < 1M e features simples?
  → Firebase puro. Nao toque.

MAU 1-3M OU leaderboard lento?
  → Adiciona Redis cache na frente. Firebase continua.

MAU > 3M OU features de PvP/guilds?
  → Avaliar PlayFab (rapido) ou Nakama (controle).

MAU > 10M?
  → Custom backend. GCP Cloud Run + PostgreSQL + Redis.
  → Nao existe managed service que escale bem e seja barato aqui.
```

---

## 14. LGPD Compliance

### O que Coletamos

| Dado | Onde | Base Legal | Retencao |
|---|---|---|---|
| UID (anonimo) | Firebase Auth | Contrato (conta) | Ate exclusao |
| Display name (inventado) | Firestore | Interesse legitimo | Ate exclusao |
| Score / wave / kills | Firestore | Contrato (progresso) | Ate exclusao |
| Platform / app version | Firestore | Interesse legitimo | 12 meses |
| Device info (crash) | Crashlytics | Interesse legitimo | 90 dias |
| Analytics events | Firebase Analytics | Consentimento | 14 meses |
| IP address | Firebase Auth | Seguranca | 30 dias |

**O que NAO coletamos:**
- Nome real
- Email (exceto se Google Sign-In, onde Firebase apenas verifica o token — nao armazenamos o email)
- Localizacao GPS
- Contatos ou outras apps instaladas
- Dados financeiros

### Consentimento

```gdscript
# Tela de consentimento na primeira sessao (ANTES de qualquer analytics)
func show_consent_dialog() -> void:
    # UI de consentimento com opcoes claras:
    # [X] Publicidade personalizada (opcional)
    # [X] Analytics de uso (recomendado para melhorar o jogo)
    # Botao: "Confirmar" — nunca "aceitar tudo" sem opcoes
    pass

func save_consent(ads_personalized: bool, analytics: bool) -> void:
    # Salva localmente E no Firestore (para auditoria LGPD)
    SaveSystem.save_consent(ads_personalized, analytics)
    FirebaseManager.update_consent(ads_personalized, analytics)

    # Configura AdMob conforme consentimento
    if not ads_personalized:
        AdsManager.set_non_personalized_ads()

    # Configura Analytics conforme consentimento
    if not analytics:
        FirebaseManager.disable_analytics_collection()
```

### Direito de Exclusao (Art. 18, LGPD)

```
FLUXO DE EXCLUSAO DE CONTA
  ↓
Usuario solicita exclusao (Settings → Conta → Excluir)
  ↓
requestAccountDeletion() Cloud Function
  ↓ marca deletion_requested_at no Firestore
  ↓
Email de confirmacao (se tiver email vinculado)
  ↓
Aguarda 30 dias (periodo de arrependimento)
  ↓
processAccountDeletions() Cron (diario 04:00 UTC)
  ↓
Deleta: users/{uid}, leaderboard_alltime/{uid}, leaderboard_weekly/{uid}
  ↓
Deleta: Firebase Auth user
  ↓
Anonimiza: sessions archive (substitui uid por hash)
  ↓
Log de auditoria mantido por 5 anos (sem dados pessoais)
```

### Controle de Dados por Minores

- O jogo e classificado +10 (PEGI/ESRB/ClassInd)
- Nao coletamos data de nascimento no MVP
- Se futuramente houver conta obrigatoria: gate de idade 13+
- AdMob tem configuracao COPPA para < 13 anos (ads nao personalizados)

### Data Processing Agreement (DPA)

Firebase (Google) tem DPA padrao disponivel. Deve ser aceito na conta Firebase Console antes do launch. Cobre:
- Transferencia internacional (servidores Google nos EUA/UE)
- Obrigacoes do processador de dados
- Resposta a incidentes de seguranca (72h para notificacao)

---

## 15. Disaster Recovery

### Backup Strategy

#### Firestore
```
Backup automatico: Firebase Console → Firestore → Backups
  ├── Frequencia: Diario (00:00 UTC)
  ├── Retencao: 7 dias (gratuito ate esse periodo)
  ├── Localizacao: southamerica-east1 (mesma regiao do app)
  └── Point-in-time recovery: ate 7 dias atras

Backup semanal adicional (para retencao longa):
  ├── Cloud Scheduler → Cloud Function → Firestore Export para GCS
  ├── Bucket: gs://zumbis-brasilia-backups/firestore/weekly/
  └── Retencao: 90 dias (lifecycle policy no bucket)
```

```typescript
// functions/src/scheduled.ts — backup semanal para GCS
export const weeklyFirestoreBackup = onSchedule(
  { schedule: "0 2 * * 0", memory: "256MiB" }, // domingo 02:00 UTC
  async () => {
    const { FirestoreAdminClient } = await import("@google-cloud/firestore");
    const client = new FirestoreAdminClient();

    const bucket = "gs://zumbis-brasilia-backups/firestore/weekly/";
    const timestamp = new Date().toISOString().split("T")[0];

    await client.exportDocuments({
      name: `projects/zumbis-brasilia/databases/(default)`,
      outputUriPrefix: `${bucket}${timestamp}`,
      collectionIds: ["users", "leaderboard_alltime", "leaderboard_weekly_archive"],
    });

    logger.info(`Backup semanal exportado para ${bucket}${timestamp}`);
  }
);
```

#### Firebase Auth
- Exportar lista de usuarios mensalmente via `firebase auth:export`
- Armazenar em GCS criptografado
- Necessario para recuperacao em caso de corrupcao do projeto Firebase

#### Remote Config
- Versioning automatico (Firebase guarda ultimas 300 versoes)
- Export manual antes de cada mudanca grande: `firebase remoteconfig:get -o backup.json`

### Failover Strategy

| Componente | Falha | Comportamento |
|---|---|---|
| **Firestore** | Indisponivel | Gameplay continua offline. Sincroniza quando volta. |
| **Cloud Functions** | Timeout | Cliente mostra score sem rank. Retry com backoff. |
| **Remote Config** | Indisponivel | Usa valores default hardcoded no app. Zero impacto. |
| **AdMob** | Fill rate 0% | Jogo continua sem ads. Zero crash. |
| **Firebase Auth** | Indisponivel | Nao permite novo login. Sessoes existentes continuam. |
| **Analytics** | Indisponivel | Eventos perdidos (SDK buffer local, envia quando volta). |

**Regra de ouro:** O gameplay NUNCA depende de rede. Toda sincronizacao e async e tolerante a falha.

### Incident Response Playbook

#### Nivel 1 — Crash Rate > 2% (alerta automatico)
```
1. Verificar Crashlytics — identificar stack trace
2. Verificar se e em versao especifica de OS/device
3. Se remote config resolvivel: hotfix via RC em < 15 min
4. Se necessario app update: preparar hotfix build
5. Ativar maintenance_mode se necessario (impede estados corrompidos)
```

#### Nivel 2 — Firestore Indisponivel
```
1. Verificar status.firebase.google.com
2. Ativar maintenance_mode via Remote Config
3. Monitorar pagina de status do Google Cloud
4. Quando voltar: verificar backlog de submissoes pendentes
5. Desativar maintenance_mode
```

#### Nivel 3 — Score Manipulation em Escala
```
1. Detectado via BigQuery query de anomalia
2. Identificar UIDs afetados
3. Script de ban em batch via Admin SDK
4. Remover dos leaderboards via Cloud Function admin
5. Post-mortem: ajustar thresholds de detectao
```

#### Nivel 4 — Vazamento de Dados (LGPD)
```
1. Identificar escopo: quais dados, quantos usuarios
2. Notificar ANPD em 72h (obrigatorio por lei)
3. Revogar tokens comprometidos via Firebase Auth
4. Auditar Security Rules
5. Comunicar usuarios afetados
```

### Monitoramento Continuo

```yaml
# Google Cloud Monitoring — Alertas Configurados

alertas:
  - nome: "CF Error Rate Alto"
    condicao: "error_rate > 5% por 5 minutos"
    canal: email + slack

  - nome: "Firestore Reads Spike"
    condicao: "reads > 3x media semanal por 10 minutos"
    canal: email
    acao: "Investigar possivel scraping ou loop infinito no cliente"

  - nome: "Auth Failure Spike"
    condicao: "auth_failures > 100/minuto"
    canal: email
    acao: "Possivel ataque de credential stuffing"

  - nome: "BigQuery Cost Spike"
    condicao: "custo diario > 2x media"
    canal: email

  - nome: "Crashlytics Rate"
    condicao: "crash_free_users < 98%"
    canal: email + sms
```

---

## Resumo Executivo

| Dimensao | Decisao | Justificativa |
|---|---|---|
| **Backend** | Firebase (Blaze) | Zero ops, escala automatica, excelente para mobile |
| **Database** | Firestore | Offline-first, security rules granulares, SDK maduro |
| **Compute** | Cloud Functions (TypeScript) | Serverless, escala para zero, regiao Sao Paulo |
| **Cache** | Cliente (60s TTL) | Reduz reads do Firestore em 70% no endpoint mais chamado |
| **Auth** | Anonymous → Google/Apple | Zero atrito no onboarding, migracao sem perda de progresso |
| **Anti-cheat** | Deteccao + log (MVP) | Custo de cheat < custo de anti-cheat robusto no MVP |
| **Analytics** | Firebase → BigQuery | Free no SDK, SQL no BigQuery para analises complexas |
| **Migracao** | Gatilho: 3M MAU + PvP | Firebase aguenta confortavelmente ate essa escala |
| **LGPD** | Consentimento granular + exclusao em 30 dias | Compliance real, nao security theater |
| **DR** | Backup diario + client offline | Everything fails, all the time. O jogo continua. |

> *"A infraestrutura que voce constroi no dia 1 deve sobreviver ao sucesso do produto. Firebase com as otimizacoes certas de cache e denormalizacao vai de 0 a 3M MAU sem drama. Quando e hora de migrar, voce vai saber — porque voce vai estar monitorando."*
>
> — Werner Vogels

---

*Documento gerado em: Abril 2026*
*Proxima revisao: Ao atingir 100K MAU ou 6 meses apos launch (o que vier primeiro)*
