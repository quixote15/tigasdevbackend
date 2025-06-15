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
| `CONCURRENT_LIMIT` | 5000 | Max concurrent connections |
| `MONITORING_ENABLED` | true | Enable Prometheus metrics |
| `LOG_LEVEL` | info | Logging level |

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

## Client Usage

### Basic Connection

```javascript
// Initialize PeerJS client
const peer = new Peer('unique-peer-id', {
  host: 'your-server.com',
  port: 9000, // or 443 for HTTPS
  path: '/',
  secure: true, // true for HTTPS
  debug: 2 // 0-3 for different debug levels
});

peer.on('open', (id) => {
  console.log('Connected with ID:', id);
});

peer.on('connection', (conn) => {
  console.log('Incoming connection:', conn);
  
  conn.on('data', (data) => {
    console.log('Received:', data);
  });
});

// Connect to another peer
const conn = peer.connect('other-peer-id');
conn.on('open', () => {
  conn.send('Hello!');
});
```

### WebRTC Data Channels

```javascript
const peer = new Peer({
  host: 'your-server.com',
  port: 9000,
  path: '/'
});

// Create data connection
const conn = peer.connect('remote-peer-id');

conn.on('open', () => {
  // Send data
  conn.send('Hello World!');
  
  // Send JSON
  conn.send({ type: 'message', data: 'Hello' });
  
  // Send binary data
  const buffer = new ArrayBuffer(8);
  conn.send(buffer);
});

conn.on('data', (data) => {
  console.log('Received:', data);
});
```

### Video/Audio Calling

```javascript
// Get user media
navigator.mediaDevices.getUserMedia({ video: true, audio: true })
  .then(stream => {
    // Call another peer
    const call = peer.call('remote-peer-id', stream);
    
    call.on('stream', (remoteStream) => {
      // Display remote video
      const video = document.getElementById('remote-video');
      video.srcObject = remoteStream;
    });
  });

// Answer incoming calls
peer.on('call', (call) => {
  navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => {
      call.answer(stream);
      
      call.on('stream', (remoteStream) => {
        // Display remote video
        const video = document.getElementById('remote-video');
        video.srcObject = remoteStream;
      });
    });
});
```

## Monitoring

### Prometheus Metrics

The server exposes Prometheus metrics at `/metrics`:

- `peerjs_connections_total` - Total connections by type and status
- `peerjs_active_connections` - Current active connections
- `http_request_duration_seconds` - HTTP request duration histogram
- Standard Node.js metrics (memory, CPU, etc.)

### Logging

**Local Development:**
- Console (formatted for development)
- `logs/peer-server-YYYY-MM-DD.log` (daily rotation)
- `logs/peer-server-error-YYYY-MM-DD.log` (errors only)

**Docker/Production:**
- Stdout only (no file logging)
- Logs collected via container orchestration
- JSON format for structured logging

### Health Check Response

```json
{
  "service": "peer-server",
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "uptime": 3600,
  "port": 9000,
  "environment": "production",
  "version": "2.0.0",
  "connections": {
    "active": 42,
    "total": 150,
    "failed": 2,
    "disconnected": 106
  },
  "memory": {
    "rss": 52428800,
    "heapTotal": 26214400,
    "heapUsed": 18874352,
    "external": 1234567
  },
  "cpu": {
    "user": 156250,
    "system": 31250
  }
}
```

## Docker Deployment

The server includes a production-ready Dockerfile:

```bash
# Build image
docker build -t peer-server .

# Run container
docker run -p 9000:9000 -e NODE_ENV=production peer-server
```

## Performance Tuning

### Connection Limits

```env
CONCURRENT_LIMIT=5000
ALIVE_TIMEOUT=60000
CLEANUP_EXPIRE=5000
```

### Rate Limiting

```env
RATE_LIMIT_WINDOW=900000  # 15 minutes
RATE_LIMIT_MAX=1000       # 1000 requests per window
```

### Memory Management

```env
CLEANUP_OUTMSG=1000
CLEANUP_OUT_TRANS=5000
```

## Troubleshooting

### Common Issues

1. **CORS Errors**
   - Set `CORS_ORIGIN` to your client domain
   - Ensure protocol (HTTP/HTTPS) matches

2. **Connection Timeouts**
   - Increase `ALIVE_TIMEOUT`
   - Check firewall settings
   - Verify WebSocket support

3. **High Memory Usage**
   - Reduce `CONCURRENT_LIMIT`
   - Decrease cleanup timeouts
   - Monitor connection stats

### Debug Mode

Enable debug mode for development:

```env
NODE_ENV=development
LOG_LEVEL=debug
```

### Admin Endpoints

Check active connections:
```bash
curl http://localhost:9000/admin/connections
```

Force disconnect a peer:
```bash
curl -X DELETE http://localhost:9000/admin/connections/peer-id-here
```

## Security

This server implements comprehensive security measures for production use. For detailed security information, see:

- **[Security Documentation](docs/SECURITY.md)** - Comprehensive security guide covering container security, application security, monitoring, and best practices
- **[Deployment Security Guide](docs/DEPLOYMENT.md)** - Secure deployment practices for Caprover and production environments

### Quick Security Overview

- **Non-root container execution** for reduced attack surface
- **Rate limiting and DDoS protection** to prevent abuse
- **Security headers** via Helmet (XSS, CSRF protection)
- **Structured logging** with security event tracking
- **Connection monitoring** with admin management endpoints
- **Environment-based configuration** for secure secrets management

### Security Features

- 🔐 Non-root Docker user execution
- 🛡️ Rate limiting (configurable per IP)
- 🚫 Request slowdown for abuse prevention
- 📊 Real-time connection monitoring
- 🔍 Structured security logging
- ⚡ Graceful shutdown handling
- 🌐 CORS and SSL/TLS configuration

## Scaling

### Horizontal Scaling

For multiple instances, consider:
- Load balancer with sticky sessions
- Redis for session storage
- Message queue for coordination

### Vertical Scaling

- Increase `CONCURRENT_LIMIT`
- Optimize cleanup timeouts
- Monitor memory and CPU usage

## License

MIT License 