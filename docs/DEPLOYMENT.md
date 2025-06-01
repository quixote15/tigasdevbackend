# Deployment Security Guide

This guide covers secure deployment practices for the PeerJS Production Server on Caprover and other container platforms.

## 🚀 Caprover Deployment

### Pre-Deployment Security

1. **Environment Variables Setup**
```bash
# In Caprover App Settings -> Environment Variables
NODE_ENV=production
DOCKER=true
CORS_ORIGIN=https://yourdomain.com
RATE_LIMIT_MAX=1000
RATE_LIMIT_WINDOW=900000
CONCURRENT_LIMIT=5000
ALIVE_TIMEOUT=60000
LOG_LEVEL=warn
PROXIED=true
```

2. **SSL/HTTPS Configuration**
```bash
# Enable Force HTTPS in Caprover
# SSL certificates automatically managed by Let's Encrypt
```

3. **Container HTTP Port**
```bash
# Set in Caprover Dashboard
Container HTTP Port: 9000
```

### Security Hardening

1. **Firewall Rules**
```bash
# Only allow necessary ports
22 (SSH) - Restricted to admin IPs
80 (HTTP) - Redirect to HTTPS
443 (HTTPS) - Public
3000 (Caprover) - Admin only
```

2. **Domain Configuration**
```bash
# Use specific subdomains
peer-server.yourdomain.com
# Avoid wildcard certificates in production
```

3. **Resource Limits**
```json
{
  "memory": "512M",
  "cpu": "0.5",
  "restart": "unless-stopped"
}
```

## 🔒 Security Monitoring

### Log Analysis
```bash
# View container logs
docker logs peer-server-container

# Monitor specific security events
docker logs peer-server-container | grep "error\|failed\|blocked"
```

### Health Monitoring
```bash
# Automated health checks
curl https://peer-server.yourdomain.com/health

# Connection monitoring
curl https://peer-server.yourdomain.com/admin/connections
```

### Rate Limit Monitoring
```bash
# Check for abuse patterns
curl https://peer-server.yourdomain.com/metrics
```

## 🛡️ Production Security Checklist

- [ ] **HTTPS Enabled:** Force HTTPS redirect
- [ ] **Environment Variables:** All secrets in env vars
- [ ] **CORS Origins:** Specific domains only
- [ ] **Rate Limits:** Configured for expected load
- [ ] **Resource Limits:** Memory and CPU limits set
- [ ] **Log Monitoring:** Automated log analysis
- [ ] **Health Checks:** Monitoring endpoints configured
- [ ] **Backup Strategy:** Configuration backup plan
- [ ] **Update Schedule:** Regular security updates
- [ ] **Incident Response:** Security incident procedures

## 🚨 Incident Response

### Suspicious Activity Detection
```bash
# High connection rates
curl /metrics | grep connections

# Failed authentication attempts
docker logs | grep "error"

# Unusual traffic patterns
docker logs | grep "rate limit"
```

### Emergency Procedures
```bash
# Force disconnect all peers
curl -X DELETE /admin/connections/ALL

# Restart container
caprover api restart-app peer-server

# Scale down temporarily
caprover api update-app peer-server --replicas 0
```

### Log Analysis Tools
```bash
# Export logs for analysis
docker logs peer-server-container > security-audit.log

# Search for security events
grep -i "error\|failed\|blocked\|attack" security-audit.log
```

## 📊 Performance vs Security

### High Security Configuration
```bash
RATE_LIMIT_MAX=100
RATE_LIMIT_WINDOW=300000  # 5 minutes
CONCURRENT_LIMIT=1000
ALLOW_DISCOVERY=false
LOG_LEVEL=error
```

### Balanced Configuration
```bash
RATE_LIMIT_MAX=1000
RATE_LIMIT_WINDOW=900000  # 15 minutes
CONCURRENT_LIMIT=5000
ALLOW_DISCOVERY=false
LOG_LEVEL=warn
```

### High Performance Configuration
```bash
RATE_LIMIT_MAX=10000
RATE_LIMIT_WINDOW=900000  # 15 minutes
CONCURRENT_LIMIT=10000
ALLOW_DISCOVERY=true
LOG_LEVEL=error
```

## 🔧 Troubleshooting Security Issues

### CORS Errors
```bash
# Check CORS configuration
echo $CORS_ORIGIN

# Update CORS for new domains
CORS_ORIGIN=https://app1.com,https://app2.com
```

### Rate Limiting Issues
```bash
# Increase limits temporarily
RATE_LIMIT_MAX=5000

# Check current limits
curl /status | jq '.config'
```

### Container Security Issues
```bash
# Verify non-root execution
docker exec peer-server-container whoami
# Should return: peerjs

# Check file permissions
docker exec peer-server-container ls -la /usr/src/app
```

### SSL/TLS Issues
```bash
# Test SSL certificate
openssl s_client -connect peer-server.yourdomain.com:443

# Verify HTTPS redirect
curl -I http://peer-server.yourdomain.com
# Should return: 301 Moved Permanently
```

## 📈 Scaling Security

### Multi-Instance Deployment
```bash
# Load balancer configuration
upstream peer_servers {
    server peer-server-1:9000;
    server peer-server-2:9000;
    ip_hash;  # Sticky sessions
}
```

### Database Integration
```bash
# Connection state persistence
REDIS_URL=redis://redis-server:6379
```

### Advanced Monitoring
```bash
# Prometheus integration
PROMETHEUS_ENABLED=true
PROMETHEUS_ENDPOINT=/metrics

# External log aggregation
LOG_AGGREGATION_URL=https://logs.yourcompany.com
```

## 🎯 Security Best Practices Summary

1. **Never commit secrets** to version control
2. **Use HTTPS everywhere** in production
3. **Implement rate limiting** appropriate for your use case
4. **Monitor logs regularly** for security events
5. **Keep dependencies updated** with security patches
6. **Use specific CORS origins** instead of wildcards
7. **Implement resource limits** to prevent abuse
8. **Have an incident response plan** ready
9. **Backup configurations** regularly
10. **Test security measures** before deployment 