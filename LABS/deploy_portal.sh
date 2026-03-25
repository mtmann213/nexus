#!/bin/bash

# Phase 10: The Link (Local Web Portal)
# This script deploys Open WebUI via Docker, optimized for WSL -> Windows LM Studio bridge.

echo "🏁 STARTING PHASE 10: PORTAL DEPLOYMENT 🏁"
echo "----------------------------------------"

# 1. Fixed Windows Host IP
echo "📡 Using Fixed Windows Host IP..."
WINDOWS_IP="192.168.68.50"
echo "✅ Windows targeted at: $WINDOWS_IP"

# 2. Configuration
PORT=3000
IMAGE="ghcr.io/open-webui/open-webui:main"
CONTAINER_NAME="nexus-portal"
LM_STUDIO_URL="http://$WINDOWS_IP:1234/v1"

echo "🛠️  Configuring Portal..."
echo "🔗 Backend: $LM_STUDIO_URL"
echo "🌐 Frontend: http://localhost:$PORT"

# 3. Stop existing container if it exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "🛑 Stopping existing nexus-portal..."
    docker rm -f $CONTAINER_NAME > /dev/null
fi

# 4. Launch Open WebUI with GPU support
# We map port 3000 and pass the LM Studio URL as the default OpenAI API base.
echo "🚀 Launching Nexus Portal (Open WebUI)..."

docker run -d \
  -p $PORT:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=$LM_STUDIO_URL \
  -e OPENAI_API_KEY="lm-studio" \
  -v nexus-webui:/app/backend/data \
  --name $CONTAINER_NAME \
  --restart always \
  $IMAGE

echo "✅ DEPLOYMENT COMPLETE"
echo "📍 Nexus Portal (Chat/Docs): http://localhost:$PORT"
echo "📍 OpenCode Visual (Terminal Sync): http://localhost:3001"
echo "📱 Mobile Access: http://$(hostname -I | awk '{print $1}'):$PORT"
echo "----------------------------------------"
echo "💡 To start Terminal Sync, run: opencode web --hostname 0.0.0.0 --port 3001"
echo "💡 TIP: When you first log in, you can create a local admin account."
echo "💡 Your 4-agent team from Phase 9 will be visible in the model dropdown!"
