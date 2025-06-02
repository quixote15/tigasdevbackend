# WebRTC Signaling Server with Room Management

A production-ready WebRTC signaling server built with Socket.IO, featuring comprehensive room management, connection tracking, and real-time monitoring capabilities.

## 🚀 Features

### Core Functionality
- **Socket.IO Integration** - Real-time bidirectional communication
- **Room Management** - Users can join/leave rooms with automatic cleanup
- **WebRTC Signaling** - Handle offer, answer, and ICE candidate exchange
- **Connection Tracking** - Monitor all active connections and their metadata
- **Real-time Statistics** - Live metrics and server monitoring

### Production Ready
- **Graceful Shutdown** - Proper cleanup on server termination
- **Error Handling** - Comprehensive error handling and logging
- **Security Headers** - Helmet.js integration for security
- **CORS Support** - Configurable cross-origin resource sharing
- **Health Monitoring** - Multiple endpoints for server status

### API Endpoints
- `GET /` - Server information and feature list
- `GET /health` - Detailed health check with metrics
- `GET /rooms` - List all active rooms and their users
- `GET /connections` - List all active connections
- `GET /stats` - Server statistics and uptime information

## 📋 Requirements

- Node.js 22.0.0 or higher
- npm for package management

## 🛠️ Installation

```bash
# Navigate to signaling-server directory
cd services/signaling-server

# Install dependencies
npm install

# Start the server
npm start
```

## ⚙️ Configuration

Configure the server using environment variables:

```bash
# Server port (default: 3002)
PORT=3002

# CORS origin (default: *)
CORS_ORIGIN=*

# Environment mode
NODE_ENV=development
```

### For Production:
```bash
PORT=3002
CORS_ORIGIN=https://yourdomain.com
NODE_ENV=production
```

## 🔌 Socket.IO Events

### Client → Server Events

#### `join-room`
Join a specific room
```javascript
socket.emit('join-room', roomId, userId);
```

#### `offer` (WebRTC)
Send WebRTC offer to another peer
```javascript
socket.emit('offer', {
    target: targetSocketId,
    offer: rtcOffer
});
```

#### `answer` (WebRTC)
Send WebRTC answer to another peer
```javascript
socket.emit('answer', {
    target: targetSocketId,
    answer: rtcAnswer
});
```

#### `ice-candidate` (WebRTC)
Send ICE candidate to another peer
```javascript
socket.emit('ice-candidate', {
    target: targetSocketId,
    candidate: iceCandidate
});
```

#### `ping`
Test server connectivity
```javascript
socket.emit('ping');
```

### Server → Client Events

#### `user-connected`
Notifies when a user joins the room
```javascript
socket.on('user-connected', (data) => {
    // data: { userId, socketId, timestamp }
});
```

#### `user-disconnected`
Notifies when a user leaves the room
```javascript
socket.on('user-disconnected', (data) => {
    // data: { userId, socketId, timestamp, reason }
});
```

#### `room-joined`
Confirms successful room join
```javascript
socket.on('room-joined', (data) => {
    // data: { roomId, userId, users[], timestamp }
});
```

#### WebRTC Events
```javascript
socket.on('offer', (data) => {
    // data: { target, offer, from }
});

socket.on('answer', (data) => {
    // data: { target, answer, from }
});

socket.on('ice-candidate', (data) => {
    // data: { target, candidate, from }
});
```

#### `pong`
Response to ping
```javascript
socket.on('pong', (data) => {
    // data: { timestamp }
});
```

#### `server-shutdown`
Server shutdown notification
```javascript
socket.on('server-shutdown', (data) => {
    // data: { message, timestamp }
});
```

## 📡 API Usage Examples

### Health Check
```bash
curl http://localhost:3002/health
```

Response:
```json
{
    "service": "signaling-server",
    "status": "healthy",
    "timestamp": "2025-06-01T17:30:00.000Z",
    "uptime": 300.123,
    "version": "2.0.0",
    "environment": "development",
    "port": "3002",
    "memory": {
        "used": "25 MB",
        "total": "50 MB"
    },
    "connections": {
        "active": 5,
        "total": 12
    },
    "rooms": {
        "active": 2,
        "total": 8
    }
}
```

### List All Rooms
```bash
curl http://localhost:3002/rooms
```

Response:
```json
{
    "totalRooms": 2,
    "rooms": [
        {
            "roomId": "room_abc123",
            "users": 3,
            "userList": [
                {
                    "userId": "user_1",
                    "socketId": "socket_xyz",
                    "joinedAt": "2025-06-01T17:25:00.000Z"
                }
            ],
            "createdAt": "2025-06-01T17:20:00.000Z",
            "lastActivity": "2025-06-01T17:29:00.000Z"
        }
    ]
}
```

### Server Statistics
```bash
curl http://localhost:3002/stats
```

Response:
```json
{
    "totalConnections": 15,
    "activeConnections": 8,
    "totalRooms": 12,
    "activeRooms": 3,
    "startTime": 1635789600000,
    "uptime": 3600000,
    "uptimeFormatted": "1h 0m 0s",
    "averageUsersPerRoom": 2.67
}
```

## 🧪 Testing with the Demo Client

Open the included `example-client-rooms.html` in multiple browser windows to test:

1. **Open the HTML file** in your browser
2. **Auto-generated User ID** will be created
3. **Join a room** by entering a room ID
4. **Open another browser window** and join the same room
5. **Watch real-time events** in the message log
6. **Test server endpoints** using the provided buttons

### Features to Test:
- ✅ Multiple users joining the same room
- ✅ Real-time user connection/disconnection events
- ✅ Server statistics and monitoring
- ✅ Health checks and room listings
- ✅ WebSocket connectivity and latency testing

## 🐳 Docker Deployment

The server includes Docker support for containerized deployment:

```bash
# Build the Docker image
docker build -t signaling-server .

# Run the container
docker run -d \
  -p 3002:3002 \
  -e NODE_ENV=production \
  -e CORS_ORIGIN=https://yourdomain.com \
  --name signaling-server \
  signaling-server
```

## ☁️ Caprover Deployment

Deploy to Caprover using the included captain-definition:

```bash
# From the signaling-server directory
caprover deploy
```

Set environment variables in Caprover dashboard:
- `PORT`: 3002
- `NODE_ENV`: production
- `CORS_ORIGIN`: your domain

## 🔧 Development

### Start in Development Mode
```bash
npm run dev
```

### Server Logs
The server provides detailed logging for all operations:

```
🚀 Signaling Server with Room Management started
📡 Server running on port 3002
🌍 Environment: development
📊 Health check: http://localhost:3002/health
🏠 Room list: http://localhost:3002/rooms
📈 Statistics: http://localhost:3002/stats
🔗 WebSocket ready for connections

📱 Client connected: socket_abc123 (Total: 1)
🏠 User user_456 joining room room_test
✅ User user_456 joined room room_test (Room has 1 users)
```

## 🔒 Security Considerations

### CORS Configuration
```javascript
// Restrict origins in production
CORS_ORIGIN=https://yourdomain.com,https://app.yourdomain.com
```

### Rate Limiting
Consider adding rate limiting for production deployments:
```javascript
// Example with express-rate-limit
const rateLimit = require('express-rate-limit');
app.use(rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100 // limit each IP to 100 requests per windowMs
}));
```

### Input Validation
The server validates:
- Room ID and User ID presence
- Socket connection state
- Event payload structure

## 📊 Monitoring

### Health Endpoint
- Memory usage tracking
- Connection statistics
- Uptime monitoring
- Environment information

### Statistics Tracking
- Total/active connections
- Total/active rooms
- Average users per room
- Server uptime with formatting

### Real-time Events
- Connection/disconnection logging
- Room join/leave tracking
- Error handling and reporting

## 🤝 Integration with WebRTC

This signaling server is designed to work with WebRTC applications:

```javascript
// Basic WebRTC integration example
const socket = io('http://localhost:3002');

// Join a room
socket.emit('join-room', 'my-room', 'my-user-id');

// Handle WebRTC signaling
socket.on('offer', async (data) => {
    await peerConnection.setRemoteDescription(data.offer);
    const answer = await peerConnection.createAnswer();
    await peerConnection.setLocalDescription(answer);
    socket.emit('answer', { target: data.from, answer });
});

socket.on('answer', async (data) => {
    await peerConnection.setRemoteDescription(data.answer);
});

socket.on('ice-candidate', async (data) => {
    await peerConnection.addIceCandidate(data.candidate);
});
```

## 📚 Related Documentation

- [Socket.IO Documentation](https://socket.io/docs/)
- [WebRTC API Reference](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API)
- [Express.js Documentation](https://expressjs.com/)

---

## 🆚 Comparison with Original

### Enhanced Features Added:
- ✅ **Socket.IO Integration** (was basic HTTP only)
- ✅ **Room Management** (join/leave rooms)
- ✅ **Connection Tracking** (detailed connection metadata)
- ✅ **Real-time Events** (user connect/disconnect notifications)
- ✅ **WebRTC Signaling** (offer/answer/ICE candidate handling)
- ✅ **Statistics API** (server metrics and monitoring)
- ✅ **Production Features** (logging, error handling, graceful shutdown)
- ✅ **Comprehensive Demo Client** (full testing interface)

### Maintained Features:
- ✅ **Express.js Framework**
- ✅ **CORS Support**
- ✅ **Security Headers (Helmet)**
- ✅ **Health Check Endpoint**
- ✅ **Docker Support**
- ✅ **Caprover Deployment**

This enhanced signaling server provides a solid foundation for WebRTC applications requiring room-based communication with real-time user management. 