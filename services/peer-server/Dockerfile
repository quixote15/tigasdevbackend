# Use Node.js 22 Alpine as base image
FROM node:22-alpine

# Install dumb-init for proper signal handling
RUN apk add --no-cache dumb-init

# Create app directory
WORKDIR /usr/src/app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S peerjs -u 1001

# Change ownership of the app directory
RUN chown -R peerjs:nodejs /usr/src/app

# Switch to non-root user
USER peerjs

# Set environment variables for Docker
ENV DOCKER=true
ENV NODE_ENV=production

# Expose port
EXPOSE 9000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:' + (process.env.PORT || 9000) + '/health', (res) => { \
    if (res.statusCode === 200) { \
      console.log('Health check passed'); \
      process.exit(0); \
    } else { \
      console.log('Health check failed with status:', res.statusCode); \
      process.exit(1); \
    } \
  }).on('error', (err) => { \
    console.log('Health check error:', err.message); \
    process.exit(1); \
  });"

# Use dumb-init to handle signals properly
ENTRYPOINT ["dumb-init", "--"]

# Start the application
CMD ["node", "index.js"] 