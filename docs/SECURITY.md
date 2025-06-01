# Security Documentation

This document outlines the security measures implemented in the PeerJS Production Server and provides guidance for secure deployment and operation.

## 🔐 Container Security

### Non-Root User Execution

**Why it matters:**
Running containers as root poses significant security risks. If an attacker compromises your application, they would have root privileges inside the container, which could lead to:
- System file modifications
- Installation of malicious software
- Container escape attacks
- Host system compromise

**Implementation:**
```dockerfile
# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S peerjs -u 1001

# Transfer file ownership to non-root user
RUN chown -R peerjs:nodejs /usr/src/app

# Switch to non-root user
USER peerjs
```

**Security Benefits:**
- **Principle of Least Privilege:** Application runs with minimal required permissions
- **Reduced Attack Surface:** Limited access even if compromised
- **Compliance:** Meets security standards (SOC2, PCI-DSS)
- **Kubernetes Compatible:** Works with Pod Security Policies

### Signal Handling with dumb-init

**Why it matters:**
Node.js applications running as PID 1 in containers don't handle Unix signals properly, leading to:
- Graceful shutdown handlers not executing
- Zombie process accumulation
- Unresponsive container shutdowns
- Resource leaks

**Implementation:**
```dockerfile
# Install lightweight init system
RUN apk add --no-cache dumb-init

# Use dumb-init as entrypoint
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "index.js"]
```

**Security Benefits:**
- **Proper Signal Forwarding:** Ensures graceful shutdown handlers execute
- **Zombie Process Cleanup:** Prevents resource exhaustion
- **Container Responsiveness:** Reliable container lifecycle management

### Alternative Approaches

If you prefer simpler configurations:

**Option 1: Node.js --init flag (Node.js 16+)**
```dockerfile
CMD ["node", "--init", "index.js"]
```

**Option 2: COPY --chown (cleaner ownership transfer)**
```dockerfile
COPY --chown=peerjs:nodejs . .
# Replaces: COPY . . + RUN chown -R peerjs:nodejs /usr/src/app
```

**Option 3: Root execution (less secure, simpler)**
```dockerfile
# Remove user creation and ownership transfer
# Run as root (not recommended for production)
```

## 🛡️ Application Security

### Rate Limiting & DDoS Protection

**Express Rate Limiting:**
```javascript
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 1000, // 1000 requests per window per IP
  message: 'Too many requests from this IP'
});
```

**Request Slowdown:**
```javascript
const speedLimiter = slowDown({
  windowMs: 15 * 60 * 1000,
  delayAfter: 100, // First 100 requests at full speed
  delayMs: 3000 // 3s delay for subsequent requests
});
```

**Configuration:**
- `RATE_LIMIT_WINDOW`: Time window in milliseconds
- `RATE_LIMIT_MAX`: Maximum requests per window per IP

### Security Headers (Helmet)

**Implementation:**
```javascript
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
```

**Protection Against:**
- XSS (Cross-Site Scripting)
- CSRF (Cross-Site Request Forgery)
- Clickjacking
- MIME sniffing attacks
- Information disclosure

### CORS Configuration

**Flexible CORS Setup:**
```javascript
const corsConfig = {
  origin: process.env.CORS_ORIGIN ? 
    process.env.CORS_ORIGIN.split(',') : '*',
  credentials: true
};
```

**Best Practices:**
- **Development:** Use `*` for flexibility
- **Production:** Specify exact origins
- **HTTPS Only:** Enable `credentials: true` only with specific origins

### Input Validation & Error Handling

**Request Size Limits:**
```javascript
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));
```

**Error Handling:**
```javascript
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
    message: CONFIG.environment === 'development' ? 
      err.message : 'Something went wrong'
  });
});
```

## 🔍 Monitoring & Logging Security

### Structured Logging

**Security-Focused Logging:**
```javascript
// Log security events
logger.info('New peer connected', {
  peerId: clientId,
  connectionId,
  ip: client.getSocket()?.remoteAddress
});

logger.error('PeerJS server error', {
  error: error.message,
  stack: error.stack
});
```

**Log Rotation (Development):**
- Daily log rotation prevents disk exhaustion
- Separate error logs for security incident analysis
- Configurable retention periods

**Container Logging (Production):**
- Stdout-only logging in Docker
- No file system writes for stateless containers
- Log aggregation via container orchestration

### Connection Monitoring

**Real-time Tracking:**
- Active connection counts
- Connection source IPs
- Session durations
- Failed connection attempts

**Admin Endpoints:**
```bash
# Monitor active connections
GET /admin/connections

# Force disconnect suspicious peers
DELETE /admin/connections/:peerId
```

## 🌐 Network Security

### SSL/TLS Configuration

**HTTPS Setup:**
```javascript
const CONFIG = {
  peerjs: {
    ssl: {
      key: process.env.SSL_KEY,
      cert: process.env.SSL_CERT
    }
  }
};
```

**Client Configuration:**
```javascript
const peer = new Peer({
  host: 'your-domain.com',
  port: 443,
  secure: true, // HTTPS
  path: '/'
});
```

### Proxy Support

**Cloud Deployment:**
```javascript
const CONFIG = {
  peerjs: {
    proxied: process.env.PROXIED === 'true'
  }
};
```

**Benefits:**
- Load balancer compatibility
- SSL termination support
- Header forwarding for real IP tracking

## 🚀 Deployment Security

### Environment Variables

**Sensitive Configuration:**
```bash
# Never commit these to version control
SSL_KEY=/path/to/private-key.pem
SSL_CERT=/path/to/certificate.pem
PEERJS_KEY=your-secret-key
CORS_ORIGIN=https://yourdomain.com
```

**Security Variables:**
```bash
# Rate limiting
RATE_LIMIT_WINDOW=900000
RATE_LIMIT_MAX=1000

# Connection limits
CONCURRENT_LIMIT=5000
ALIVE_TIMEOUT=60000

# Logging
LOG_LEVEL=warn  # Reduce log verbosity in production
```

### Container Image Security

**Base Image:**
```dockerfile
FROM node:22-alpine  # Minimal attack surface
```

**Security Scanning:**
```bash
# Scan for vulnerabilities
docker scan peer-server:latest

# Use multi-stage builds for smaller images
# Update dependencies regularly
npm audit fix
```

### Caprover Deployment

**Security Considerations:**
- Use HTTPS for all communications
- Configure firewall rules
- Regular security updates
- Monitor container logs
- Implement backup strategies

## 📋 Security Checklist

### Pre-Deployment

- [ ] **Environment Variables:** All sensitive data in env vars
- [ ] **CORS Origins:** Specific domains, not wildcards
- [ ] **SSL Certificates:** Valid HTTPS certificates
- [ ] **Rate Limits:** Appropriate for your use case
- [ ] **Dependency Scan:** `npm audit` clean
- [ ] **Image Scan:** Docker vulnerability scan

### Production Monitoring

- [ ] **Log Monitoring:** Set up log aggregation
- [ ] **Rate Limit Alerts:** Monitor for abuse patterns
- [ ] **Connection Monitoring:** Track unusual connection patterns
- [ ] **Resource Monitoring:** CPU, memory, disk usage
- [ ] **Health Checks:** Automated health monitoring
- [ ] **Backup Strategy:** Regular configuration backups

### Incident Response

- [ ] **Log Analysis:** Tools for security incident investigation
- [ ] **Connection Termination:** Ability to quickly disconnect malicious peers
- [ ] **Rate Limit Adjustment:** Dynamic rate limit configuration
- [ ] **Container Restart:** Quick rollback procedures
- [ ] **Notification System:** Alert mechanisms for security events

## 🔧 Security Configuration Examples

### Development Environment
```bash
# .env.development
NODE_ENV=development
CORS_ORIGIN=*
LOG_LEVEL=debug
RATE_LIMIT_MAX=10000
MONITORING_ENABLED=true
```

### Production Environment
```bash
# .env.production
NODE_ENV=production
CORS_ORIGIN=https://app.yourdomain.com,https://admin.yourdomain.com
LOG_LEVEL=warn
RATE_LIMIT_MAX=1000
RATE_LIMIT_WINDOW=900000
ALIVE_TIMEOUT=60000
CONCURRENT_LIMIT=5000
PROXIED=true
SSL_KEY=/etc/ssl/private/server.key
SSL_CERT=/etc/ssl/certs/server.crt
```

### High-Security Environment
```bash
# .env.secure
NODE_ENV=production
CORS_ORIGIN=https://secure.yourdomain.com
LOG_LEVEL=error
RATE_LIMIT_MAX=100
RATE_LIMIT_WINDOW=300000  # 5 minutes
ALIVE_TIMEOUT=30000
CONCURRENT_LIMIT=1000
ALLOW_DISCOVERY=false
MONITORING_ENABLED=true
```

## 📚 Additional Resources

- [OWASP Container Security](https://owasp.org/www-project-docker-top-10/)
- [Node.js Security Best Practices](https://nodejs.org/en/docs/guides/security/)
- [Docker Security Documentation](https://docs.docker.com/engine/security/)
- [Express.js Security](https://expressjs.com/en/advanced/best-practice-security.html)
- [WebRTC Security](https://webrtc-security.github.io/)

## 🆘 Security Contact

For security vulnerabilities or concerns:
- Review logs for suspicious activity
- Update dependencies regularly
- Monitor security advisories
- Implement defense in depth strategies 