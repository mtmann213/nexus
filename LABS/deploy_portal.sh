#!/bin/bash
# Phase 10: Deploy Open WebUI Local Dashboard (Strict Docker Implementation)
# Architecture: Docker Container bridging to Host LM Studio API

echo "🚀 NexOS Web Portal Initialization..."

# Pre-flight check
if ! command -v docker &> /dev/null; then
    echo "❌ ERROR: Docker is not installed or the Docker Desktop Daemon is not running locally!"
    echo "Please open Docker Desktop on Windows, ensure it is running in the system tray, and try again."
    exit 1
fi

echo "📦 Pulling and Spinning up Open WebUI Docker Container [project-nexus-portal]..."

# Deploys Open WebUI natively via Docker Container
# Maps port 8080 inside the container to 3000 on your external network
# Injects OPENAI_API_BASE_URL to bridge through the host-gateway to Windows LM Studio 

docker run -d \
  --name project-nexus-portal \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  --gpus all \
  -e OPENAI_API_BASE_URL="http://host.docker.internal:1234/v1" \
  -v open-webui:/app/backend/data \
  --restart always \
  ghcr.io/open-webui/open-webui:main

# Fetch Local IP for mobile access
local_ip=$(hostname -I | awk '{print $1}')

echo ""
echo "✅ Docker Deployment Successful! The web portal is quietly running in the background."
echo "--------------------------------------------------------"
echo "📱 ACCESS YOUR COMMAND CENTER / WEB INTERFACE:"
echo "🌐 Local Desktop Browser:    http://localhost:3000   (or http://127.0.0.1:3000)"
echo "🌐 Mobile Phone Browser:     http://$local_ip:3000"
echo "--------------------------------------------------------"
echo "🛑 IMPORTANT: HOW TO SHUT DOWN THE DASHBOARD:"
echo "Because Docker runs efficiently as a background service, it will stay alive even if you close this terminal."
echo "To safely kill the portal and free up your system ports and RAM, simply run this exact command:"
echo ""
echo "    docker stop project-nexus-portal && docker rm project-nexus-portal"
echo ""
echo "💡 TIP: Open your desktop browser right now to ensure it can see the LM Studio models in the dropdown screen!"
