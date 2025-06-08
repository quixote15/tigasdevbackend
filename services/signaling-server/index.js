const express = require('express');
const http = require('http');
const cors = require('cors');
const helmet = require('helmet');
const { Server } = require('socket.io');

const app = express();
const PORT = process.env.PORT || 3002;
const NODE_ENV = process.env.NODE_ENV || 'development';

// Create HTTP server
const server = http.createServer(app);

// Setup Socket.IO with CORS configuration
const io = new Server(server, {
    cors: {
        origin: '*',
        methods: ["GET", "POST"],
        credentials: false
    },
    transports: ['websocket', 'polling']
});

// Room and connection tracking
const rooms = new Map();
const connections = new Map();

// Statistics
const stats = {
    totalConnections: 0,
    activeConnections: 0,
    totalRooms: 0,
    activeRooms: 0,
    startTime: Date.now()
};

// Middleware
app.use(helmet({
    crossOriginEmbedderPolicy: false,
    contentSecurityPolicy: {
        directives: {
            defaultSrc: ["'self'"],
            connectSrc: ["'self'", "ws:", "wss:"]
        }
    }
}));

app.use(cors({
    origin: process.env.CORS_ORIGIN || "*",
    credentials: false
}));

app.use(express.json());

// Logging middleware
app.use((req, res, next) => {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${req.method} ${req.url} - ${req.ip}`);
    next();
});

// Root endpoint with server information
app.get('/', (req, res) => {
    res.json({
        service: 'signaling-server',
        version: '2.0.0',
        message: 'WebRTC Signaling Server with Room Management',
        port: PORT,
        environment: NODE_ENV,
        features: [
            'Socket.IO room management',
            'WebRTC signaling',
            'Group chat functionality',
            'Typing indicators',
            'Connection tracking',
            'Room statistics',
            'Health monitoring'
        ],
        endpoints: {
            health: '/health',
            rooms: '/rooms',
            connections: '/connections',
            stats: '/stats'
        }
    });
});

// Health check endpoint
app.get('/health', (req, res) => {
    const uptime = process.uptime();
    const memoryUsage = process.memoryUsage();
    
    res.status(200).json({
        service: 'signaling-server',
        status: 'healthy',
        timestamp: new Date().toISOString(),
        uptime: uptime,
        version: '2.0.0',
        environment: NODE_ENV,
        port: PORT,
        memory: {
            used: Math.round(memoryUsage.heapUsed / 1024 / 1024) + ' MB',
            total: Math.round(memoryUsage.heapTotal / 1024 / 1024) + ' MB'
        },
        connections: {
            active: stats.activeConnections,
            total: stats.totalConnections
        },
        rooms: {
            active: stats.activeRooms,
            total: stats.totalRooms
        }
    });
});

// Rooms endpoint - list all active rooms
app.get('/rooms', (req, res) => {
    const roomList = Array.from(rooms.entries()).map(([roomId, room]) => ({
        roomId,
        users: room.users.length,
        userList: room.users.map(user => ({
            userId: user.userId,
            socketId: user.socketId,
            joinedAt: user.joinedAt
        })),
        createdAt: room.createdAt,
        lastActivity: room.lastActivity
    }));

    res.json({
        totalRooms: rooms.size,
        rooms: roomList
    });
});

// Connections endpoint - list all active connections
app.get('/connections', (req, res) => {
    const connectionList = Array.from(connections.values());
    
    res.json({
        totalConnections: connections.size,
        connections: connectionList
    });
});

// Statistics endpoint
app.get('/stats', (req, res) => {
    const uptime = Date.now() - stats.startTime;
    
    res.json({
        ...stats,
        uptime: uptime,
        uptimeFormatted: formatUptime(uptime),
        averageUsersPerRoom: rooms.size > 0 ? 
            Array.from(rooms.values()).reduce((sum, room) => sum + room.users.length, 0) / rooms.size : 0
    });
});

// Socket.IO connection handling
io.on('connection', (socket) => {
    const connectionInfo = {
        socketId: socket.id,
        connectedAt: new Date().toISOString(),
        ip: socket.handshake.address,
        userAgent: socket.handshake.headers['user-agent']
    };
    
    connections.set(socket.id, connectionInfo);
    stats.totalConnections++;
    stats.activeConnections++;
    
    console.log(`📱 Client connected: ${socket.id} (Total: ${stats.activeConnections})`);

    // Handle room joining
    socket.on('join-room', (roomId, userId) => {
        if (!roomId || !userId) {
            socket.emit('error', { message: 'Room ID and User ID are required' });
            return;
        }

        console.log(`🏠 User ${userId} joining room ${roomId}`);
        
        // Leave any previous rooms
        Array.from(socket.rooms).forEach(room => {
            if (room !== socket.id) {
                socket.leave(room);
                removeUserFromRoom(room, socket.id);
            }
        });

        // Join the new room
        socket.join(roomId);
        addUserToRoom(roomId, userId, socket.id);
        
        // Update connection info
        connections.set(socket.id, {
            ...connectionInfo,
            currentRoom: roomId,
            userId: userId
        });

        // Notify other users in the room
        socket.to(roomId).emit('user-connected', {
            userId,
            socketId: socket.id,
            timestamp: new Date().toISOString()
        });

        // Send room info to the joining user
        const room = rooms.get(roomId);
        socket.emit('room-joined', {
            roomId,
            userId,
            users: room ? room.users.map(u => ({ userId: u.userId, socketId: u.socketId })) : [],
            timestamp: new Date().toISOString()
        });

        console.log(`✅ User ${userId} joined room ${roomId} (Room has ${room ? room.users.length : 0} users)`);
    });

    // Handle WebRTC signaling
    socket.on('offer', (data) => {
        socket.to(data.target).emit('offer', {
            ...data,
            from: socket.id
        });
    });

    socket.on('answer', (data) => {
        socket.to(data.target).emit('answer', {
            ...data,
            from: socket.id
        });
    });

    socket.on('ice-candidate', (data) => {
        socket.to(data.target).emit('ice-candidate', {
            ...data,
            from: socket.id
        });
    });

    // Handle disconnection
    socket.on('disconnect', (reason) => {
        const connection = connections.get(socket.id);
        const roomId = connection?.currentRoom;
        const userId = connection?.userId;

        console.log(`📱 Client disconnected: ${socket.id} (Reason: ${reason})`);
        
        if (roomId && userId) {
            // Notify other users in the room
            socket.to(roomId).emit('user-disconnected', {
                userId,
                socketId: socket.id,
                timestamp: new Date().toISOString(),
                reason
            });
            
            // Remove user from room
            removeUserFromRoom(roomId, socket.id);
            console.log(`🏠 User ${userId} left room ${roomId}`);
        }

        // Clean up connection tracking
        connections.delete(socket.id);
        stats.activeConnections--;
        
        console.log(`📊 Active connections: ${stats.activeConnections}`);
    });

    // Handle chat messages
    socket.on('send-message', (data) => {
        const connection = connections.get(socket.id);
        const roomId = connection?.currentRoom;
        const userId = connection?.userId;

        if (!roomId || !userId) {
            socket.emit('error', { message: 'Must be in a room to send messages' });
            return;
        }

        if (!data.message || typeof data.message !== 'string' || data.message.trim().length === 0) {
            socket.emit('error', { message: 'Message cannot be empty' });
            return;
        }

        const message = {
            id: generateMessageId(),
            userId: userId,
            message: data.message.trim(),
            timestamp: new Date().toISOString(),
            roomId: roomId
        };

        // Broadcast message to all users in the room (including sender)
        io.to(roomId).emit('new-message', message);

        console.log(`💬 Message from ${userId} in room ${roomId}: ${message.message.substring(0, 50)}${message.message.length > 50 ? '...' : ''}`);
    });

    // Handle typing indicators
    socket.on('typing-start', () => {
        const connection = connections.get(socket.id);
        const roomId = connection?.currentRoom;
        const userId = connection?.userId;

        if (roomId && userId) {
            socket.to(roomId).emit('user-typing', { userId, isTyping: true });
        }
    });

    socket.on('typing-stop', () => {
        const connection = connections.get(socket.id);
        const roomId = connection?.currentRoom;
        const userId = connection?.userId;

        if (roomId && userId) {
            socket.to(roomId).emit('user-typing', { userId, isTyping: false });
        }
    });



    // Handle custom events
    socket.on('ping', () => {
        socket.emit('pong', { timestamp: Date.now() });
    });
});

// Room management functions
function addUserToRoom(roomId, userId, socketId) {
    if (!rooms.has(roomId)) {
        rooms.set(roomId, {
            users: [],
            createdAt: new Date().toISOString(),
            lastActivity: new Date().toISOString()
        });
        stats.totalRooms++;
        stats.activeRooms++;
    }
    
    const room = rooms.get(roomId);
    
    // Remove user if already in room (reconnection case)
    room.users = room.users.filter(user => user.socketId !== socketId);
    
    // Add user to room
    room.users.push({
        userId,
        socketId,
        joinedAt: new Date().toISOString()
    });
    
    room.lastActivity = new Date().toISOString();
}

function removeUserFromRoom(roomId, socketId) {
    const room = rooms.get(roomId);
    if (!room) return;
    
    room.users = room.users.filter(user => user.socketId !== socketId);
    room.lastActivity = new Date().toISOString();
    
    // Remove empty rooms
    if (room.users.length === 0) {
        rooms.delete(roomId);
        stats.activeRooms--;
        console.log(`🗑️ Empty room ${roomId} removed`);
    }
}

// Message management functions
function generateMessageId() {
    return 'msg_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
}

// Utility functions
function formatUptime(milliseconds) {
    const seconds = Math.floor(milliseconds / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);
    
    if (days > 0) return `${days}d ${hours % 24}h ${minutes % 60}m`;
    if (hours > 0) return `${hours}h ${minutes % 60}m ${seconds % 60}s`;
    if (minutes > 0) return `${minutes}m ${seconds % 60}s`;
    return `${seconds}s`;
}

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('❌ Express Error:', err);
    res.status(500).json({
        error: 'Internal Server Error',
        message: NODE_ENV === 'development' ? err.message : 'Something went wrong'
    });
});

// Start server
server.listen(PORT, () => {
    console.log(`🚀 Signaling Server with Room Management started`);
    console.log(`📡 Server running on port ${PORT}`);
    console.log(`🌍 Environment: ${NODE_ENV}`);
    console.log(`📊 Health check: http://localhost:${PORT}/health`);
    console.log(`🏠 Room list: http://localhost:${PORT}/rooms`);
    console.log(`📈 Statistics: http://localhost:${PORT}/stats`);
    console.log(`🔗 WebSocket ready for connections`);
});

// Graceful shutdown handling
const shutdown = (signal) => {
    console.log(`🛑 ${signal} received, shutting down gracefully...`);
    
    // Notify all connected clients
    io.emit('server-shutdown', { 
        message: 'Server is shutting down',
        timestamp: new Date().toISOString()
    });
    
    // Close server
    server.close(() => {
        console.log('✅ HTTP server closed');
        console.log('📊 Final stats:', {
            totalConnections: stats.totalConnections,
            totalRooms: stats.totalRooms,
            uptime: formatUptime(Date.now() - stats.startTime)
        });
        process.exit(0);
    });
};

process.on('SIGTERM', () => shutdown('SIGTERM'));
process.on('SIGINT', () => shutdown('SIGINT'));

// Handle uncaught exceptions
process.on('uncaughtException', (err) => {
    console.error('💥 Uncaught Exception:', err);
    process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('💥 Unhandled Rejection at:', promise, 'reason:', reason);
    process.exit(1);
}); 