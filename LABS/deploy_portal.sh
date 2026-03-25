#!/bin/bash

# Phase 10: The Link (Local Web Portal)
# This script deploys Open WebUI via Docker, optimized for WSL -> Windows LM Studio bridge.

echo "🏁 STARTING PHASE 10: PORTAL DEPLOYMENT 🏁"
echo "----------------------------------------"

# 1. Detect Windows Host IP (Bridge)
echo "📡 Detecting Windows Host IP..."
WINDOWS_IP=$(grep nameserver /etc/resolv.conf | awk '{print $2}')
if [ -z "$WINDOWS_IP" ]; then
    echo "❌ Error: Could not detect Windows IP. Falling back to localhost."
    WINDOWS_IP="127.0.0.1"
else
    echo "✅ Windows detected at: $WINDOWS_IP"
fi

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

echo "----------------------------------------"
echo "✅ DEPLOYMENT COMPLETE"
echo "📍 Access your Command Center at: http://localhost:$PORT"
echo "📱 To access from your phone/tablet: http://$(hostname -I | awk '{print $1}'):$PORT"
echo "----------------------------------------"
echo "💡 TIP: When you first log in, you can create a local admin account."
echo "💡 Your 4-agent team from Phase 9 will be visible in the model dropdown!"
