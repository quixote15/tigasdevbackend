# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Monorepo for WebRTC backend services using npm workspaces. Three independent Node.js services:

- **peer-server** (port 9000) — PeerJS signaling server with Express, rate limiting, monitoring
- **signaling-server** (port 3002) — Socket.IO server for WebRTC signaling, room management, chat
- **turn-server** (port 3478) — TURN server for NAT traversal using node-turn

## Common Commands

```bash
# Install all workspace dependencies
make install          # or: npm install

# Development (with nodemon)
make dev-peer         # or: npm run dev --workspace=peer-server
make dev-signaling    # or: npm run dev --workspace=signaling-server

# Production
make start-peer       # or: npm start --workspace=peer-server
make start-signaling  # or: npm start --workspace=signaling-server

# Docker
make build-peer       # Build peer-server image
make build-signaling  # Build signaling-server image
make build-all        # Build all images

# Deploy to Caprover
make deploy-peer
make deploy-signaling
make deploy-all

# Peer-server only
cd services/peer-server
npm test              # Jest tests
npm run lint          # ESLint
```

## Architecture

All three services are standalone Express/HTTP servers in `services/`. Each has its own `package.json`, `Dockerfile`, and Caprover `captain-definition`. There is no shared library code between services.

**peer-server** (`services/peer-server/index.js`): Express app wrapping the PeerJS library. Tracks active connections in a `Map`, exposes admin endpoints for connection management, and collects metrics. Uses Helmet, CORS, rate-limit, and express-slow-down for security. Winston handles logging with daily log rotation.

**signaling-server** (`services/signaling-server/index.js`): Express + Socket.IO server. Manages rooms and user connections in-memory. Handles WebRTC signaling events (offer/answer/ice-candidate), chat messaging with input validation, and typing indicators. All state is event-driven through Socket.IO.

**turn-server** (`services/turn-server/index.js`): Thin wrapper around `node-turn` with long-term auth. Configured entirely via environment variables. Critical: `TURN_RELAY_IP` must be set when running behind NAT.

## Environment Configuration

Each service uses `.env` files (see `.env.example` in peer-server and turn-server). Key variables:

- `PEERJS_KEY` — Must be changed from default `peerjs` in production
- `CORS_ORIGIN` — Currently `*`, restrict in production
- `TURN_RELAY_IP` — Required for NAT traversal in production

## Deployment

Docker images use `node:22-alpine` with `dumb-init`, run as non-root users, and include HTTP health checks. Deployed via Caprover using the Makefile targets.

## Tech Stack

Node.js 22+, Express 4, Socket.IO 4, PeerJS (peer), node-turn, Helmet, Winston, Jest
