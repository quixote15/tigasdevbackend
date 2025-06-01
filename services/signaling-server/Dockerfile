# Use Node.js 18 Alpine as base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy application code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

# Change ownership of the app directory
RUN chown -R nextjs:nodejs /app

# Switch to non-root user
USER nextjs

# Expose port
EXPOSE 3002

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "const http = require('http'); \
  const options = { host: 'localhost', port: process.env.PORT || 3002, path: '/health', timeout: 2000 }; \
  const request = http.request(options, (res) => { \
    if (res.statusCode === 200) process.exit(0); \
    else process.exit(1); \
  }); \
  request.on('error', () => process.exit(1)); \
  request.end();"

# Start the application
CMD ["npm", "start"] 