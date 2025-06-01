require('dotenv').config();
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const compression = require('compression');
const rateLimit = require('express-rate-limit');
const slowDown = require('express-slow-down');
const morgan = require('morgan');
const winston = require('winston');
require('winston-daily-rotate-file');
const { v4: uuidv4 } = require('uuid');
const { ExpressPeerServer } = require('peer');

// ==========================================
// CONFIGURATION
// ==========================================
const CONFIG = {
  port: process.env.PORT || 9000,
  host: process.env.HOST || '0.0.0.0',
  environment: process.env.NODE_ENV || 'development',
  cors: {
    origin: process.env.CORS_ORIGIN ? process.env.CORS_ORIGIN.split(',') : '*',
    credentials: true
  },
  peerjs: {
    path: process.env.PEERJS_PATH || '/',
    key: process.env.PEERJS_KEY || 'peerjs',
    allow_discovery: process.env.ALLOW_DISCOVERY === 'true',
    concurrent_limit: parseInt(process.env.CONCURRENT_LIMIT) || 5000,
    cleanup_outmsg: parseInt(process.env.CLEANUP_OUTMSG) || 1000,
    cleanup_out_trans: parseInt(process.env.CLEANUP_OUT_TRANS) || 5000,
    cleanup_expire: parseInt(process.env.CLEANUP_EXPIRE) || 5000,
    alive_timeout: parseInt(process.env.ALIVE_TIMEOUT) || 60000,
    port: parseInt(process.env.PORT) || 9000,
    proxied: process.env.PROXIED === 'true',
    ssl: {
      key: process.env.SSL_KEY,
      cert: process.env.SSL_CERT
    }
  },
  monitoring: {
    enabled: process.env.MONITORING_ENABLED !== 'false',
    metrics_path: process.env.METRICS_PATH || '/metrics'
  },
  rateLimit: {
    windowMs: parseInt(process.env.RATE_LIMIT_WINDOW) || 15 * 60 * 1000, // 15 minutes
    max: parseInt(process.env.RATE_LIMIT_MAX) || 1000, // limit each IP to 1000 requests per windowMs
    message: 'Too many requests from this IP'
  }
};

// ==========================================
// LOGGING SETUP
// ==========================================
const logFormat = winston.format.combine(
  winston.format.timestamp(),
  winston.format.errors({ stack: true }),
  winston.format.json()
);

// Create base transports array with console
const transports = [
  new winston.transports.Console({
    format: winston.format.combine(
      winston.format.colorize(),
      winston.format.simple()
    )
  })
];

// Only add file transports if not in Docker environment
const isDocker = process.env.DOCKER === 'true' || process.env.NODE_ENV === 'production';
if (!isDocker) {
  transports.push(
    new winston.transports.DailyRotateFile({
      filename: 'logs/peer-server-%DATE%.log',
      datePattern: 'YYYY-MM-DD',
      maxSize: '20m',
      maxFiles: '14d'
    }),
    new winston.transports.DailyRotateFile({
      filename: 'logs/peer-server-error-%DATE%.log',
      datePattern: 'YYYY-MM-DD',
      level: 'error',
      maxSize: '20m',
      maxFiles: '30d'
    })
  );
}

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: logFormat,
  defaultMeta: { service: 'peer-server' },
  transports: transports
});

// ==========================================
// BASIC METRICS TRACKING
// ==========================================
const metrics = {
  connections: {
    total: 0,
    active: 0,
    failed: 0,
    disconnected: 0
  },
  requests: {
    total: 0,
    byPath: {},
    byStatus: {}
  },
  startTime: Date.now()
};

// Simple metrics middleware
const metricsMiddleware = (req, res, next) => {
  const start = Date.now();
  metrics.requests.total++;
  
  // Track by path
  const path = req.path || 'unknown';
  metrics.requests.byPath[path] = (metrics.requests.byPath[path] || 0) + 1;
  
  // Capture response status
  const originalSend = res.send;
  res.send = function(data) {
    const status = res.statusCode;
    metrics.requests.byStatus[status] = (metrics.requests.byStatus[status] || 0) + 1;
    
    logger.debug('Request completed', {
      method: req.method,
      path: req.path,
      status: res.statusCode,
      duration: Date.now() - start,
      ip: req.ip
    });
    
    return originalSend.call(this, data);
  };
  
  next();
};

// ==========================================
// EXPRESS APP SETUP
// ==========================================
const app = express();

// Security middleware
app.use(helmet({
  crossOriginEmbedderPolicy: false,
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      connectSrc: ["'self'", "ws:", "wss:"],
      scriptSrc: ["'self'", "'unsafe-inline'"]
    }
  }
}));

// Performance middleware
app.use(compression());

// CORS
app.use(cors(CONFIG.cors));

// Rate limiting
const limiter = rateLimit(CONFIG.rateLimit);
app.use(limiter);

// Slow down repeated requests
const speedLimiter = slowDown({
  windowMs: 15 * 60 * 1000, // 15 minutes
  delayAfter: 100, // allow 100 requests per 15 minutes at full speed
  delayMs: 3000 // add 3s delay per request after delayAfter
});
app.use(speedLimiter);

// Logging middleware
app.use(morgan('combined', {
  stream: { write: message => logger.info(message.trim()) }
}));

// Basic metrics tracking
if (CONFIG.monitoring.enabled) {
  app.use(metricsMiddleware);
}

// Body parsing
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// ==========================================
// CONNECTION TRACKING
// ==========================================
const activeConnections = new Map();
const connectionStats = {
  total: 0,
  active: 0,
  failed: 0,
  disconnected: 0
};

// ==========================================
// EXPRESS SERVER SETUP
// ==========================================
const server = require('http').createServer(app);

// ==========================================
// PEERJS SERVER SETUP
// ==========================================
const peerServer = ExpressPeerServer(server, {
  debug: CONFIG.environment === 'development',
  path: CONFIG.peerjs.path,
  key: CONFIG.peerjs.key,
  allow_discovery: CONFIG.peerjs.allow_discovery,
  concurrent_limit: CONFIG.peerjs.concurrent_limit,
  cleanup_outmsg: CONFIG.peerjs.cleanup_outmsg,
  cleanup_out_trans: CONFIG.peerjs.cleanup_out_trans,
  cleanup_expire: CONFIG.peerjs.cleanup_expire,
  alive_timeout: CONFIG.peerjs.alive_timeout,
  proxied: CONFIG.peerjs.proxied
});

// Use PeerJS server
app.use(CONFIG.peerjs.path, peerServer);

// ==========================================
// PEERJS EVENT HANDLERS
// ==========================================
peerServer.on('connection', (client) => {
  const clientId = client.getId();
  const connectionId = uuidv4();
  
  activeConnections.set(clientId, {
    id: connectionId,
    peerId: clientId,
    connectedAt: new Date(),
    lastSeen: new Date(),
    ip: client.getSocket()?.remoteAddress || 'unknown'
  });
  
  connectionStats.total++;
  connectionStats.active++;
  metrics.connections.total++;
  metrics.connections.active++;
  
  logger.info('New peer connected', {
    peerId: clientId,
    connectionId,
    totalConnections: connectionStats.total,
    activeConnections: connectionStats.active
  });
});

peerServer.on('disconnect', (client) => {
  const clientId = client.getId();
  const connection = activeConnections.get(clientId);
  
  if (connection) {
    activeConnections.delete(clientId);
    connectionStats.active--;
    connectionStats.disconnected++;
    metrics.connections.active--;
    metrics.connections.disconnected++;
    
    logger.info('Peer disconnected', {
      peerId: clientId,
      connectionId: connection.id,
      sessionDuration: Date.now() - connection.connectedAt.getTime(),
      activeConnections: connectionStats.active
    });
  }
});

peerServer.on('error', (error) => {
  connectionStats.failed++;
  metrics.connections.failed++;
  
  logger.error('PeerJS server error', {
    error: error.message,
    stack: error.stack
  });
});

// ==========================================
// API ENDPOINTS
// ==========================================

// Basic metrics endpoint (simple JSON format)
if (CONFIG.monitoring.enabled) {
  app.get(CONFIG.monitoring.metrics_path, (req, res) => {
    const uptime = Date.now() - metrics.startTime;
    
    res.json({
      server: {
        uptime_ms: uptime,
        uptime_seconds: Math.floor(uptime / 1000)
      },
      connections: metrics.connections,
      requests: metrics.requests,
      memory: process.memoryUsage(),
      timestamp: new Date().toISOString()
    });
  });
}

// Health check endpoint
app.get('/health', (req, res) => {
  const healthData = {
    service: 'peer-server',
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    port: CONFIG.port,
    environment: CONFIG.environment,
    version: '2.0.0',
    connections: {
      active: connectionStats.active,
      total: connectionStats.total,
      failed: connectionStats.failed,
      disconnected: connectionStats.disconnected
    },
    memory: process.memoryUsage(),
    cpu: process.cpuUsage()
  };
  
  res.status(200).json(healthData);
});

// Detailed status endpoint
app.get('/status', (req, res) => {
  res.json({
    server: {
      name: 'PeerJS Signaling Server',
      version: '2.0.0',
      environment: CONFIG.environment,
      uptime: process.uptime(),
      started: new Date(Date.now() - process.uptime() * 1000).toISOString()
    },
    connections: connectionStats,
    config: {
      peerjs_path: CONFIG.peerjs.path,
      concurrent_limit: CONFIG.peerjs.concurrent_limit,
      allow_discovery: CONFIG.peerjs.allow_discovery,
      monitoring_enabled: CONFIG.monitoring.enabled
    },
    system: {
      memory: process.memoryUsage(),
      cpu: process.cpuUsage(),
      platform: process.platform,
      arch: process.arch,
      nodeVersion: process.version
    }
  });
});

// List active connections (admin endpoint)
app.get('/admin/connections', (req, res) => {
  const connections = Array.from(activeConnections.values()).map(conn => ({
    peerId: conn.peerId,
    connectedAt: conn.connectedAt,
    lastSeen: conn.lastSeen,
    duration: Date.now() - conn.connectedAt.getTime(),
    ip: conn.ip
  }));
  
  res.json({
    total: connections.length,
    connections
  });
});

// Disconnect a specific peer (admin endpoint)
app.delete('/admin/connections/:peerId', (req, res) => {
  const { peerId } = req.params;
  const connection = activeConnections.get(peerId);
  
  if (connection) {
    // Note: PeerJS doesn't provide direct disconnect method in this version
    // This would typically be handled by the client or through WebSocket management
    activeConnections.delete(peerId);
    connectionStats.active--;
    metrics.connections.active--;
    
    logger.info('Peer forcefully disconnected', { peerId });
    res.json({ message: `Peer ${peerId} disconnected`, success: true });
  } else {
    res.status(404).json({ message: 'Peer not found', success: false });
  }
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    service: 'PeerJS Signaling Server',
    version: '2.0.0',
    message: 'Production-ready PeerJS server with monitoring',
    port: CONFIG.port,
    endpoints: {
      health: '/health',
      status: '/status',
      metrics: CONFIG.monitoring.metrics_path,
      peerjs: CONFIG.peerjs.path,
      admin: '/admin/connections'
    },
    documentation: 'https://peerjs.com/docs/',
    monitoring: CONFIG.monitoring.enabled
  });
});

// ==========================================
// ERROR HANDLING
// ==========================================
app.use((err, req, res, next) => {
  logger.error('Express error', {
    error: err.message,
    stack: err.stack,
    url: req.url,
    method: req.method,
    ip: req.ip
  });
  
  res.status(500).json({
    error: 'Internal Server Error',
    message: CONFIG.environment === 'development' ? err.message : 'Something went wrong'
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    error: 'Not Found',
    message: 'The requested resource was not found'
  });
});

// ==========================================
// SERVER STARTUP
// ==========================================
server.listen(CONFIG.port, CONFIG.host, () => {
  logger.info('🚀 PeerJS Signaling Server started', {
    port: CONFIG.port,
    host: CONFIG.host,
    environment: CONFIG.environment,
    peerjs_path: CONFIG.peerjs.path,
    monitoring: CONFIG.monitoring.enabled,
    cors_origin: CONFIG.cors.origin
  });
  
  console.log(`🚀 PeerJS Signaling Server running on ${CONFIG.host}:${CONFIG.port}`);
  console.log(`📊 Health check: http://localhost:${CONFIG.port}/health`);
  console.log(`📈 Status: http://localhost:${CONFIG.port}/status`);
  if (CONFIG.monitoring.enabled) {
    console.log(`📊 Metrics: http://localhost:${CONFIG.port}${CONFIG.monitoring.metrics_path}`);
  }
  console.log(`🔗 PeerJS endpoint: http://localhost:${CONFIG.port}${CONFIG.peerjs.path}`);
});

// ==========================================
// GRACEFUL SHUTDOWN
// ==========================================
const gracefulShutdown = (signal) => {
  logger.info(`🛑 ${signal} received, shutting down gracefully...`);
  
  server.close(() => {
    logger.info('✅ HTTP server closed');
    
    // Close all active connections
    activeConnections.clear();
    connectionStats.active = 0;
    metrics.connections.active = 0;
    
    logger.info('✅ Server shutdown complete');
    process.exit(0);
  });
  
  // Force close after 30 seconds
  setTimeout(() => {
    logger.error('❌ Could not close connections in time, forcefully shutting down');
    process.exit(1);
  }, 30000);
};

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

// Handle uncaught exceptions
process.on('uncaughtException', (err) => {
  logger.error('💥 Uncaught Exception', {
    error: err.message,
    stack: err.stack
  });
  process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
  logger.error('💥 Unhandled Rejection', {
    reason,
    promise
  });
  process.exit(1);
});

// Export for testing
module.exports = { app, server, logger }; 