#!/bin/bash
# ============================================================================
# ZUMBIS DE BRASILIA — Art Agent Army Launcher
# Spawns 8 Claude Code agents in parallel via tmux
# Each agent handles a specific domain: characters, weapons, tiles, audio
# ============================================================================

set -e

SESSION="zumbis-art"
PROJECT_DIR="/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia"
PROMPTS_DIR="$PROJECT_DIR/assets/prompts"

# Kill existing session if any
tmux kill-session -t "$SESSION" 2>/dev/null || true

echo "🧟 ZUMBIS DE BRASILIA — Launching Art Agent Army..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Create the tmux session with first window
tmux new-session -d -s "$SESSION" -n "bosses" -c "$PROJECT_DIR"

# ── Agent 1: BOSSES (Lula, Bolsonaro, BolsoLula) ──
echo "[1/8] Spawning Agent: BOSSES (Lula, Bolsonaro, BolsoLula)..."
tmux send-keys -t "$SESSION:bosses" \
  "claude --dangerously-skip-permissions -p \"\$(cat $PROMPTS_DIR/agent-01-bosses.md)\"" Enter

# ── Agent 2: STF (Xandao, Gilmar, Barroso, Toffoli, Flavio Dino) ──
echo "[2/8] Spawning Agent: STF..."
tmux new-window -t "$SESSION" -n "stf" -c "$PROJECT_DIR"
tmux send-keys -t "$SESSION:stf" \
  "claude --dangerously-skip-permissions -p \"\$(cat $PROMPTS_DIR/agent-02-stf.md)\"" Enter

# ── Agent 3: FAMILIA & ALIADOS (Eduardo, Flavio, Daciolo, Alckmin, Janja) ──
echo "[3/8] Spawning Agent: FAMILIA & ALIADOS..."
tmux new-window -t "$SESSION" -n "familia" -c "$PROJECT_DIR"
tmux send-keys -t "$SESSION:familia" \
  "claude --dangerously-skip-permissions -p \"\$(cat $PROMPTS_DIR/agent-03-familia-aliados.md)\"" Enter

# ── Agent 4: NPCs SPECIAL (Ciro, Taxadd, Marina, Moro, Nikolas, Zema) ──
echo "[4/8] Spawning Agent: NPCs SPECIAL..."
tmux new-window -t "$SESSION" -n "npcs" -c "$PROJECT_DIR"
tmux send-keys -t "$SESSION:npcs" \
  "claude --dangerously-skip-permissions -p \"\$(cat $PROMPTS_DIR/agent-04-npcs-special.md)\"" Enter

# ── Agent 5: INTERNACIONAL & LIMBO (Trump, Maduro, Eneas, Monark, etc.) ──
echo "[5/8] Spawning Agent: INTERNACIONAL & LIMBO..."
tmux new-window -t "$SESSION" -n "intl-limbo" -c "$PROJECT_DIR"
tmux send-keys -t "$SESSION:intl-limbo" \
  "claude --dangerously-skip-permissions -p \"\$(cat $PROMPTS_DIR/agent-05-internacional-limbo.md)\"" Enter

# ── Agent 6: ARMAS & ITEMS ──
echo "[6/8] Spawning Agent: ARMAS & ITEMS..."
tmux new-window -t "$SESSION" -n "armas" -c "$PROJECT_DIR"
tmux send-keys -t "$SESSION:armas" \
  "claude --dangerously-skip-permissions -p \"\$(cat $PROMPTS_DIR/agent-06-armas.md)\"" Enter

# ── Agent 7: TILES & ENVIRONMENT ──
echo "[7/8] Spawning Agent: TILES & ENVIRONMENT..."
tmux new-window -t "$SESSION" -n "tiles" -c "$PROJECT_DIR"
tmux send-keys -t "$SESSION:tiles" \
  "claude --dangerously-skip-permissions -p \"\$(cat $PROMPTS_DIR/agent-07-tiles.md)\"" Enter

# ── Agent 8: AUDIO & SFX ──
echo "[8/8] Spawning Agent: AUDIO & SFX..."
tmux new-window -t "$SESSION" -n "audio" -c "$PROJECT_DIR"
tmux send-keys -t "$SESSION:audio" \
  "claude --dangerously-skip-permissions -p \"\$(cat $PROMPTS_DIR/agent-08-audio.md)\"" Enter

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧟 ALL 8 AGENTS LAUNCHED IN PARALLEL!"
echo ""
echo "To monitor:"
echo "  tmux attach -t $SESSION         # Attach to session"
echo "  tmux select-window -t $SESSION:0  # Switch to bosses"
echo "  tmux select-window -t $SESSION:1  # Switch to stf"
echo "  tmux select-window -t $SESSION:2  # Switch to familia"
echo "  tmux select-window -t $SESSION:3  # Switch to npcs"
echo "  tmux select-window -t $SESSION:4  # Switch to intl-limbo"
echo "  tmux select-window -t $SESSION:5  # Switch to armas"
echo "  tmux select-window -t $SESSION:6  # Switch to tiles"
echo "  tmux select-window -t $SESSION:7  # Switch to audio"
echo ""
echo "  Ctrl+B then N = next window"
echo "  Ctrl+B then P = previous window"
echo "  Ctrl+B then W = window list"
echo "  Ctrl+B then D = detach"
echo ""
echo "Output dirs:"
echo "  $PROJECT_DIR/assets/personagens/  # Character sprites & specs"
echo "  $PROJECT_DIR/assets/armas/        # Weapon sprites & specs"
echo "  $PROJECT_DIR/assets/tiles/        # Tilesets & environment"
echo "  $PROJECT_DIR/assets/audio/        # Audio scripts & TTS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
