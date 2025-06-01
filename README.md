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
