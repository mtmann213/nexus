import os
from openai import OpenAI

# ---------------------------------------------------------
# PROJECT NEXUS UNIVERSAL CONFIGURATION
# ---------------------------------------------------------
# How to use:
# 1. LOCAL: Ensure LM Studio is running. No changes needed.
# 2. CLOUD: Set your GROQ_API_KEY environment variable.
#    Terminal: export GROQ_API_KEY="your_key_here"
# ---------------------------------------------------------

# Detect if we should use Groq Cloud or Local LM Studio
GROQ_KEY = os.environ.get("GROQ_API_KEY")

if GROQ_KEY:
    # --- CLOUD CONFIG (Groq) ---
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = GROQ_KEY
    MODEL_NAME = "llama-3.1-8b-instant"  # High speed cloud model
    EMBED_MODEL = "nomic-embed-text-v1.5" # Note: Keep local embedding for privacy if possible
    print("☁️  PROJECT NEXUS: Using GROQ CLOUD acceleration.")
else:
    # --- LOCAL CONFIG (LM Studio) ---
    # Note: Use 'localhost' for native Linux or your Host IP for WSL
    BASE_URL = "http://172.18.176.1:1234/v1" 
    API_KEY = "lm-studio"
    MODEL_NAME = "qwen/qwen3.5-35b-a3b"
    EMBED_MODEL = "text-embedding-nomic-embed-text-v1.5"
    print("🏠 PROJECT NEXUS: Using LOCAL hardware (3080 Ti).")

# Universal OpenAI Client
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

# Tool configurations
TIMEOUT = 300.0 # Standard 5-minute timeout for heavy RF math
