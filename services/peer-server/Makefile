.PHONY: help key1 key2 key3 all

help:
	@echo "🔐 PeerJS Server Key Generator"
	@echo "Available commands:"
	@echo "  make key1    OpenSSL URL-Safe Base64 (RECOMMENDED)"
	@echo "  make key2    Node.js crypto method"
	@echo "  make key3    UUID + entropy method"
	@echo "  make all     Show all 3 methods"

key1:
	@echo "🎯 Method 1: OpenSSL URL-Safe Base64"
	@openssl rand -base64 32 | tr "/+" "_-" | tr -d "=" | sed "s/^/PEERJS_KEY=/"

key2:
	@echo "⚙️ Method 2: Node.js Crypto"
	@node -e "console.log('PEERJS_KEY=' + require('crypto').randomBytes(32).toString('base64url'))"

key3:
	@echo "🆔 Method 3: UUID + Entropy"
	@node -e "console.log('PEERJS_KEY=' + require('uuid').v4() + '-' + require('crypto').randomBytes(16).toString('hex'))"

all:
	@make key1
	@echo ""
	@make key2
	@echo ""
	@make key3

start:
	npm start

dev:
	npm run dev
