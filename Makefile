.PHONY: help install start-peer start-signaling dev-peer dev-signaling build-peer build-signaling deploy-peer deploy-signaling deploy-all clean

# Default target
help:
	@echo "TigasdevBackend - Available Commands:"
	@echo ""
	@echo "🚀 Development:"
	@echo "  install          - Install all dependencies"
	@echo "  start-peer       - Start peer server (port 3001)"
	@echo "  start-signaling  - Start signaling server (port 3002)"
	@echo "  dev-peer         - Start peer server in dev mode"
	@echo "  dev-signaling    - Start signaling server in dev mode"
	@echo ""
	@echo "🐳 Docker:"
	@echo "  build-peer       - Build peer server Docker image"
	@echo "  build-signaling  - Build signaling server Docker image"
	@echo "  build-all        - Build all Docker images"
	@echo ""
	@echo "☁️  Deployment:"
	@echo "  deploy-peer      - Deploy peer server to Caprover"
	@echo "  deploy-signaling - Deploy signaling server to Caprover"
	@echo "  deploy-all       - Deploy all services to Caprover"
	@echo ""
	@echo "🧹 Cleanup:"
	@echo "  clean            - Clean up temporary files"

# Development targets
install:
	@echo "📦 Installing dependencies..."
	npm install

start-peer:
	@echo "🚀 Starting peer server..."
	npm run start:peer

start-signaling:
	@echo "🚀 Starting signaling server..."
	npm run start:signaling

dev-peer:
	@echo "🔧 Starting peer server in dev mode..."
	npm run dev:peer

dev-signaling:
	@echo "🔧 Starting signaling server in dev mode..."
	npm run dev:signaling

# Docker build targets
build-peer:
	@echo "🐳 Building peer server Docker image..."
	cd services/peer-server && docker build -t peer-server:latest .

build-signaling:
	@echo "🐳 Building signaling server Docker image..."
	cd services/signaling-server && docker build -t signaling-server:latest .

build-all: build-peer build-signaling
	@echo "✅ All Docker images built successfully!"

# Deployment targets
deploy-peer:
	@echo "☁️  Deploying peer server to Caprover..."
	@cp captain-definition-peer captain-definition
	@caprover deploy -a peer-server
	@rm captain-definition
	@echo "✅ Peer server deployed successfully!"

deploy-signaling:
	@echo "☁️  Deploying signaling server to Caprover..."
	@cp captain-definition-signaling captain-definition
	@caprover deploy -a signaling-server
	@rm captain-definition
	@echo "✅ Signaling server deployed successfully!"

deploy-all: deploy-peer deploy-signaling
	@echo "🎉 All services deployed successfully!"

# Cleanup
clean:
	@echo "🧹 Cleaning up..."
	@rm -f captain-definition
	@echo "✅ Cleanup completed!" 