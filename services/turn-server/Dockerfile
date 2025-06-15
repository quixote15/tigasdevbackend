# Use an official Node.js runtime as a parent image
FROM node:18-alpine AS builder

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install app dependencies
# Using --omit=dev to skip development dependencies in the final image
RUN npm install --omit=dev

# Copy the rest of the application code
COPY . .

# Final stage for a lean image
FROM node:18-alpine

WORKDIR /usr/src/app

# Copy only necessary files from the builder stage
COPY --from=builder /usr/src/app/package*.json ./
COPY --from=builder /usr/src/app/node_modules ./node_modules
COPY --from=builder /usr/src/app/index.js ./
COPY --from=builder /usr/src/app/.env.example ./

# Make port 3478 available to the world outside this container (for TURN/STUN)
# Also expose the UDP relay port range
# Note: Docker EXPOSE is more for documentation; actual port mapping happens during `docker run`
EXPOSE 3478/udp
EXPOSE 3478/tcp
# The UDP port range needs to be mapped during `docker run -p`
# EXPOSE 49152-65535/udp # This syntax might not be directly supported by EXPOSE for ranges in all contexts,
                        # but it's good for documentation. The actual mapping is crucial.

# Define environment variables (defaults, can be overridden at runtime)
ENV NODE_ENV=production
# It's better to set sensitive defaults like username/password via .env file or runtime variables
# For other variables, providing a default can be okay.
ENV TURN_LISTEN_IP=0.0.0.0
ENV TURN_MIN_PORT=49152
ENV TURN_MAX_PORT=65535
ENV TURN_PORT=3478
ENV TURN_VERBOSE=false
# TURN_USERNAME, TURN_PASSWORD, TURN_REALM, TURN_RELAY_IP should be set via .env or runtime.

# Command to run the application
CMD [ "node", "index.js" ]