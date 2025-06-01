# PeerJS Client Configuration Guide

This document explains how to properly configure PeerJS clients to connect to your production signaling server.

## 🚨 Important: Client Authentication Required

**Key Point**: Your PeerJS server requires clients to provide the `PEERJS_KEY` for authentication. This key must match the one configured on your server.

### ❌ Incorrect (Missing Authentication)
```javascript
// DON'T DO THIS - Missing required key
const peer = new Peer({
    host: 'peer-server.tigasdev.com',
    port: 443,
    secure: true
    // ❌ Missing key - will cause 404/authentication errors
});
```

### ✅ Correct Configuration
```javascript
// DO THIS - Include the required key
const peer = new Peer({
    host: 'peer-server.tigasdev.com',
    port: 443,
    path: '/',
    secure: true,
    key: 'your-server-peerjs-key-here'  // ✅ Must match server's PEERJS_KEY
});
```

## 🔧 Production Client Configuration

### Basic Connection
```javascript
const PEERJS_KEY = 'your-actual-server-key'; // Replace with your server's key

const peer = new Peer({
    host: 'peer-server.tigasdev.com',  // Your domain
    port: 443,                         // HTTPS port  
    path: '/',                         // Server path
    secure: true,                      // Enable HTTPS
    debug: 0,                          // Disable debug in production
    key: PEERJS_KEY                    // Authentication key
});
```

### Development Configuration
```javascript
const PEERJS_KEY = 'peerjs'; // Default development key

const peer = new Peer({
    host: 'localhost',
    port: 9000,
    path: '/',
    secure: false,
    debug: 2,  // Enable debug logs
    key: PEERJS_KEY
});
```

### With Custom Peer ID
```javascript
const PEERJS_KEY = 'your-server-key';

const peer = new Peer('my-unique-peer-id', {
    host: 'peer-server.tigasdev.com',
    port: 443,
    path: '/',
    secure: true,
    key: PEERJS_KEY
});
```

## 🔑 Key Management

### Finding Your Server Key
1. Check your server's `.env` file for `PEERJS_KEY`
2. Or check your server environment variables
3. Generate a new one using: `make key1` in your server directory

### Security Considerations
- **Never hardcode keys** in production client code
- **Use environment variables** or configuration files
- **Different keys** for different environments (dev/staging/prod)
- **Rotate keys** regularly for security

### Environment-Based Key Management
```javascript
// Development vs Production
const PEERJS_KEY = window.location.hostname === 'localhost' 
    ? 'peerjs'  // Development key
    : 'production-key-here';  // Production key

const peer = new Peer({
    host: window.location.hostname === 'localhost' 
        ? 'localhost' 
        : 'peer-server.tigasdev.com',
    port: window.location.hostname === 'localhost' ? 9000 : 443,
    secure: window.location.hostname !== 'localhost',
    key: PEERJS_KEY
});
```

## 🌐 Environment-Specific Configurations

### Production
```javascript
const PEER_CONFIG = {
    host: 'peer-server.tigasdev.com',
    port: 443,
    path: '/',
    secure: true,
    debug: 0
};
```

### Staging
```javascript
const PEER_CONFIG = {
    host: 'peer-server-staging.tigasdev.com',
    port: 443,
    path: '/',
    secure: true,
    debug: 1
};
```

### Local Development
```javascript
const PEER_CONFIG = {
    host: 'localhost',
    port: 9000,
    path: '/',
    secure: false,
    debug: 2
};
```

## 📱 Complete Client Example

### HTML Setup
```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://unpkg.com/peerjs@1.5.4/dist/peerjs.min.js"></script>
</head>
<body>
    <div id="peerId">Connecting...</div>
    <input id="connectId" placeholder="Enter peer ID">
    <button onclick="connect()">Connect</button>
    <div id="messages"></div>
    
    <script src="client.js"></script>
</body>
</html>
```

### JavaScript Client (client.js)
```javascript
class PeerClient {
    constructor() {
        this.peer = null;
        this.conn = null;
        this.initializePeer();
    }

    initializePeer() {
        // Production configuration
        this.peer = new Peer({
            host: 'peer-server.tigasdev.com',
            port: 443,
            path: '/',
            secure: true,
            debug: 0
        });

        this.peer.on('open', (id) => {
            console.log('Connected with ID:', id);
            document.getElementById('peerId').textContent = `Your ID: ${id}`;
        });

        this.peer.on('connection', (conn) => {
            this.setupConnection(conn);
        });

        this.peer.on('error', (err) => {
            console.error('PeerJS error:', err);
            this.handleError(err);
        });

        this.peer.on('disconnected', () => {
            console.log('Disconnected from server');
            // Attempt to reconnect
            setTimeout(() => this.peer.reconnect(), 1000);
        });
    }

    connect() {
        const peerId = document.getElementById('connectId').value;
        if (!peerId) return;

        this.conn = this.peer.connect(peerId);
        this.setupConnection(this.conn);
    }

    setupConnection(conn) {
        conn.on('open', () => {
            console.log('Connection opened with:', conn.peer);
        });

        conn.on('data', (data) => {
            console.log('Received:', data);
            this.displayMessage(conn.peer, data);
        });

        conn.on('close', () => {
            console.log('Connection closed');
        });
    }

    sendMessage(message) {
        if (this.conn && this.conn.open) {
            this.conn.send(message);
            this.displayMessage('You', message);
        }
    }

    displayMessage(sender, message) {
        const div = document.createElement('div');
        div.textContent = `${sender}: ${message}`;
        document.getElementById('messages').appendChild(div);
    }

    handleError(err) {
        // Error handling based on error type
        switch(err.type) {
            case 'browser-incompatible':
                alert('Browser not supported');
                break;
            case 'network':
                console.log('Network error, attempting reconnect...');
                setTimeout(() => this.peer.reconnect(), 3000);
                break;
            case 'server-error':
                console.log('Server error:', err.message);
                break;
            default:
                console.log('Unknown error:', err);
        }
    }
}

// Initialize client
const client = new PeerClient();

// Global function for button
function connect() {
    client.connect();
}
```

## 🔒 Security Considerations

### HTTPS Required
- Always use `secure: true` in production
- Your server must have valid SSL certificates
- Port 443 for HTTPS connections

### Error Handling
```javascript
peer.on('error', (err) => {
    console.error('PeerJS error:', err);
    
    // Handle specific error types
    if (err.type === 'network') {
        // Network connectivity issues
        setTimeout(() => peer.reconnect(), 3000);
    } else if (err.type === 'server-error') {
        // Server-side issues
        console.log('Server error - check server status');
    }
});
```

## 🚨 Common Mistakes & Solutions

### 404 Error: "Could not get an ID from the server"
**Problem**: Client is passing `key` parameter
**Solution**: Remove the `key` from client configuration

```javascript
// ❌ Wrong - causes 404
const peer = new Peer({
    host: 'peer-server.tigasdev.com',
    key: 'some-key'  // Remove this line
});

// ✅ Correct
const peer = new Peer({
    host: 'peer-server.tigasdev.com',
    port: 443,
    secure: true
});
```

### Connection Timeout
**Problem**: Wrong port or secure setting
**Solution**: Use port 443 with `secure: true` for HTTPS

### CORS Errors
**Problem**: Server CORS configuration
**Solution**: Check server CORS_ORIGIN environment variable

## 📊 Testing Your Configuration

### Test Server Connectivity
```javascript
// Test server health endpoint
fetch('https://peer-server.tigasdev.com/health')
    .then(response => response.json())
    .then(data => console.log('Server health:', data))
    .catch(err => console.error('Server unreachable:', err));
```

### Test PeerJS Connection
```javascript
const peer = new Peer({
    host: 'peer-server.tigasdev.com',
    port: 443,
    secure: true,
    debug: 2  // Enable debug for testing
});

peer.on('open', (id) => {
    console.log('✅ Successfully connected with ID:', id);
});

peer.on('error', (err) => {
    console.error('❌ Connection failed:', err);
});
```

## 🔧 Debugging Tips

### Enable Debug Logging
```javascript
const peer = new Peer({
    host: 'peer-server.tigasdev.com',
    port: 443,
    secure: true,
    debug: 3  // Maximum debug level
});
```

### Check Network Tab
1. Open browser Developer Tools
2. Go to Network tab
3. Look for WebSocket connections
4. Check for 404 or other HTTP errors

### Verify Server Status
```bash
# Check if server is running
curl https://peer-server.tigasdev.com/health

# Check server configuration
curl https://peer-server.tigasdev.com/status
```

## 📚 Additional Resources

- [PeerJS Documentation](https://peerjs.com/docs/)
- [WebRTC API Reference](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API)
- [Server Security Guide](PEERJS-KEY-SECURITY.md)

---

**Remember**: Your PeerJS server uses server-side authentication via `PEERJS_KEY`. Clients connect without providing this key - the server validates connections internally. 