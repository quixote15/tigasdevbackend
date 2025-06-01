# TigasdevBackend

A monorepo containing Node.js backend services for WebRTC communication.

## Project Structure

```
tigasdevbackend/
├── services/
│   ├── peer-server/          # WebRTC peer connection server
│   │   ├── index.js         # Main application file
│   │   ├── package.json     # Service dependencies
│   │   ├── Dockerfile       # Docker configuration
│   │   ├── captain-definition # Caprover deployment config
│   │   └── .dockerignore    # Docker ignore rules
│   └── signaling-server/     # WebRTC signaling server
│       ├── index.js         # Main application file
│       ├── package.json     # Service dependencies
│       ├── Dockerfile       # Docker configuration
│       ├── captain-definition # Caprover deployment config
│       └── .dockerignore    # Docker ignore rules
├── captain-definition-peer   # Root-level Caprover config for peer server
├── captain-definition-signaling # Root-level Caprover config for signaling server
├── Makefile                 # Build and deployment automation
├── package.json            # Root workspace configuration
└── README.md               # This file
```

## Services

### Peer Server
- **Port**: 3001 (default)
- **Purpose**: Handles WebRTC peer connections
- **Health Check**: `GET /health`
- **Base URL**: `GET /`

### Signaling Server  
- **Port**: 3002 (default)
- **Purpose**: Handles WebRTC signaling
- **Health Check**: `GET /health`
- **Base URL**: `GET /`

## Prerequisites

- Node.js 18+ 
- npm 8+
- Docker (for containerization)
- Caprover (for deployment)
- Make (for build automation)

## Quick Start

### View Available Commands
```bash
make help
```

### Local Development

1. **Install dependencies:**
   ```bash
   make install
   ```

2. **Run individual services:**
   ```bash
   # Run peer server
   make start-peer
   
   # Run signaling server  
   make start-signaling
   ```

3. **Test the services:**
   ```bash
   # Peer server health check
   curl http://localhost:3001/health
   
   # Signaling server health check
   curl http://localhost:3002/health
   ```

## Available Make Commands

### 🚀 Development Commands

```bash
make install          # Install all dependencies
make start-peer       # Start peer server (port 3001)
make start-signaling  # Start signaling server (port 3002)  
make dev-peer         # Start peer server in dev mode
make dev-signaling    # Start signaling server in dev mode
```

### 🐳 Docker Commands

```bash
make build-peer       # Build peer server Docker image
make build-signaling  # Build signaling server Docker image
make build-all        # Build all Docker images
```

### ☁️ Deployment Commands

```bash
make deploy-peer      # Deploy peer server to Caprover
make deploy-signaling # Deploy signaling server to Caprover
make deploy-all       # Deploy all services to Caprover
```

### 🧹 Cleanup Commands

```bash
make clean           # Clean up temporary files
```

## Docker Deployment

### Build and Run with Docker

```bash
# Build images
make build-all

# Run containers manually
docker run -d -p 3001:3001 --name peer-server peer-server:latest
docker run -d -p 3002:3002 --name signaling-server signaling-server:latest
```

### Docker Compose (Optional)

You can create a `docker-compose.yml` file to run both services:

```yaml
version: '3.8'
services:
  peer-server:
    build: ./services/peer-server
    ports:
      - "3001:3001"
    environment:
      - PORT=3001
      
  signaling-server:
    build: ./services/signaling-server  
    ports:
      - "3002:3002"
    environment:
      - PORT=3002
```

## Caprover Deployment

### Prerequisites
- Caprover server setup and configured
- Caprover CLI installed: `npm install -g caprover`

### Deployment from Root Directory

Thanks to the Makefile and root-level captain-definition files, you can now deploy directly from the project root:

1. **Login to Caprover:**
   ```bash
   caprover login
   ```

2. **Deploy individual services:**
   ```bash
   make deploy-peer      # Deploy peer server
   make deploy-signaling # Deploy signaling server
   ```

3. **Deploy all services at once:**
   ```bash
   make deploy-all
   ```

### How Deployment Works

The Makefile uses the root-level captain-definition files:
- `captain-definition-peer` - Points to peer server Dockerfile and context
- `captain-definition-signaling` - Points to signaling server Dockerfile and context

During deployment, the Makefile temporarily copies the appropriate captain-definition file as `captain-definition` for Caprover to use, then cleans it up after deployment.

### Caprover App Configuration

For each service in Caprover dashboard:

1. **Create the app** (e.g., `peer-server`, `signaling-server`)
2. **Configure environment variables** if needed:
   - `PORT` (optional, defaults to 3001/3002)
3. **Enable HTTPS** in the HTTP Settings
4. **Configure health checks** using the `/health` endpoint

### Environment Variables

Both services support the following environment variables:

- `PORT`: Port number (defaults: 3001 for peer-server, 3002 for signaling-server)

## API Endpoints

### Peer Server (Port 3001)

- `GET /` - Service information
- `GET /health` - Health check endpoint

### Signaling Server (Port 3002)

- `GET /` - Service information  
- `GET /health` - Health check endpoint

## Health Checks

Both services include comprehensive health checks:

- **Endpoint**: `/health`
- **Method**: GET
- **Response**: JSON with service status, timestamp, and uptime
- **Docker**: Built-in health checks configured
- **Status Codes**: 200 (healthy), 500+ (unhealthy)

## Security Features

- **Helmet.js**: Security headers
- **CORS**: Cross-origin resource sharing
- **Non-root user**: Docker containers run as non-root user
- **Input validation**: JSON body parsing with limits

## Monitoring

### Health Check Responses

```json
{
  "service": "peer-server",
  "status": "healthy", 
  "timestamp": "2024-01-01T00:00:00.000Z",
  "uptime": 123.456
}
```

### Docker Health Checks

Both Dockerfiles include health check configurations that:
- Check every 30 seconds
- 3-second timeout
- 5-second startup grace period  
- 3 retries before marking unhealthy

## Troubleshooting

### Common Issues

1. **Port conflicts**: Change the PORT environment variable
2. **Docker build fails**: Check Dockerfile and .dockerignore
3. **Caprover deployment fails**: Verify captain-definition file
4. **Health check fails**: Check if service is running on correct port
5. **Make command not found**: Install `make` on your system

### Logs

```bash
# Docker logs
docker logs <container-name>

# Caprover logs
# Available in Caprover dashboard under App > Logs
```

## Development Workflow

1. **Make changes** in the appropriate service directory
2. **Test locally** using `make start-peer` or `make start-signaling`
3. **Build Docker images** using `make build-all`
4. **Deploy to staging** using `make deploy-all`

## Contributing

1. Use the Makefile for all build and deployment operations
2. Test locally before deploying
3. Update documentation when adding new features
4. Follow the existing project structure

## License

[Your License Here]

# PeerJS Signaling Server (Production-Ready)

A production-level PeerJS signaling server with comprehensive monitoring, debugging capabilities, and scalability features.

## Features

### 🚀 Production-Ready
- **Express.js** with security middleware (Helmet)
- **Compression** for improved performance
- **Rate limiting** and DDoS protection
- **CORS** configuration
- **Graceful shutdown** handling
- **SSL/TLS** support

### 📊 Monitoring & Observability
- **Prometheus metrics** integration
- **Winston logging** with daily rotation
- **Health check** endpoints
- **Connection tracking** and statistics
- **System resource monitoring**
- **Request/response monitoring**

### 🔧 Advanced Configuration
- **Environment-based** configuration
- **Custom PeerJS** settings
- **Flexible CORS** policies
- **SSL certificate** support
- **Proxy support** for cloud deployments

### 🛡️ Security Features
- **Rate limiting** (per IP)
- **Request slowdown** for abuse prevention
- **Security headers** via Helmet
- **Input validation**
- **Error handling** and logging
- **Secure key generation** with multiple methods

### 👥 Connection Management
- **Real-time connection tracking**
- **Admin endpoints** for connection management
- **Connection statistics**
- **Peer discovery** controls
- **Concurrent connection limits**

## Quick Start

### Installation

```bash
cd services/peer-server
npm install
```

### Development

```bash
npm run dev
```

### Production

```bash
npm start
```

## 🔐 Secure Key Generation

Generate cryptographically secure PEERJS_KEY values using our built-in Makefile:

```bash
# Generate recommended OpenSSL URL-Safe Base64 key
make key1

# Generate Node.js crypto key  
make key2

# Generate UUID + entropy key
make key3

# Show all methods
make all
```

**Example output:**
```bash
🎯 Method 1: OpenSSL URL-Safe Base64
PEERJS_KEY=zPbDQJrtvZWPA8ntA5oAjjLyhU1uDhgJnb8WIP7M1EU
```

Copy the generated `PEERJS_KEY=...` line to your `.env` file.

## Configuration

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

### Key Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 9000 | Server port |
| `NODE_ENV` | development | Environment mode |
| `CORS_ORIGIN` | * | Allowed CORS origins (comma-separated) |
| `PEERJS_PATH` | / | PeerJS endpoint path |
| `PEERJS_KEY` | peerjs | **MUST BE CHANGED IN PRODUCTION** |
| `CONCURRENT_LIMIT` | 5000 | Max concurrent connections |
| `MONITORING_ENABLED` | true | Enable Prometheus metrics |
| `LOG_LEVEL` | info | Logging level |

⚠️ **SECURITY WARNING**: Never use the default `PEERJS_KEY=peerjs` in production! Generate a secure key using `make key1`.

## API Endpoints

### Health & Status

- **GET `/health`** - Health check with system metrics
- **GET `/status`** - Detailed server status
- **GET `/`** - Server information and endpoints

### Monitoring

- **GET `/metrics`** - Prometheus metrics (if enabled)

### Admin (Management)

- **GET `/admin/connections`** - List all active connections
- **DELETE `/admin/connections/:peerId`** - Disconnect specific peer

### PeerJS

- **WebSocket `/`** - PeerJS signaling endpoint

## Security

This server implements comprehensive security measures for production use. For detailed security information, see:

- **[Security Documentation](docs/SECURITY.md)** - Comprehensive security guide covering container security, application security, monitoring, and best practices
- **[Deployment Security Guide](docs/DEPLOYMENT.md)** - Secure deployment practices for Caprover and production environments
- **[PeerJS Key Security](docs/PEERJS-KEY-SECURITY.md)** - Complete guide to secure key generation and why OpenSSL is the best choice

### Quick Security Overview

- **Non-root container execution** for reduced attack surface
- **Rate limiting and DDoS protection** to prevent abuse
- **Security headers** via Helmet (XSS, CSRF protection)
- **Structured logging** with security event tracking
- **Connection monitoring** with admin management endpoints
- **Environment-based configuration** for secure secrets management
- **Cryptographically secure key generation** with multiple methods

### Security Features

- 🔐 Non-root Docker user execution
- 🛡️ Rate limiting (configurable per IP)
- 🚫 Request slowdown for abuse prevention
- 📊 Real-time connection monitoring
- 🔍 Structured security logging
- ⚡ Graceful shutdown handling
- 🌐 CORS and SSL/TLS configuration
- 🔑 Secure PEERJS_KEY generation (OpenSSL, Node.js crypto, UUID)

### 🔐 PEERJS_KEY Security

The `PEERJS_KEY` is critical for server security. Use our Makefile to generate secure keys:

| Method | Command | Security Level | Recommended Use |
|--------|---------|----------------|-----------------|
| **OpenSSL** | `make key1` | ⭐⭐⭐⭐⭐ | **Production** |
| **Node.js** | `make key2` | ⭐⭐⭐⭐⭐ | Development/CI |
| **UUID+Entropy** | `make key3` | ⭐⭐⭐⭐ | Debugging |

**Why OpenSSL is best:**
- 256-bit entropy from CSPRNG
- URL-safe character set
- No external dependencies
- FIPS 140-2 compliant
- Universal availability

See [PeerJS Key Security Documentation](docs/PEERJS-KEY-SECURITY.md) for complete details.
