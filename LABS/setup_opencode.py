import json
import os
from pathlib import Path

# Target paths for OpenCode config
config_dir = Path.home() / ".config" / "opencode"
config_file = config_dir / "opencode.json"

# The configuration for LM Studio
# Note: Using your Host IP for WSL connectivity
opencode_config = {
    "$schema": "https://opencode.ai/config.json",
    "provider": {
        "lmstudio": {
            "npm": "@ai-sdk/openai-compatible",
            "name": "LM Studio (Local)",
            "options": {
                "baseURL": "http://172.18.176.1:1234/v1"
            },
            "models": {
                "qwen/qwen3.5-35b-a3b": { "name": "Qwen 3.5 35B" }
            }
        }
    },
    "model": "lmstudio/qwen/qwen3.5-35b-a3b"
}

def setup():
    # 1. Create directory
    config_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Write opencode.json
    with open(config_file, "w") as f:
        json.dump(opencode_config, f, indent=2)
    
    print(f"✅ OpenCode configuration written to {config_file}")
    print("\n🚀 Next Steps:")
    print("1. Restart OpenCode.")
    print("2. When prompted for an API key, enter: sk-local")
    print("3. Type '/models' in OpenCode to confirm 'Qwen 3.5 35B' is selected.")

if __name__ == "__main__":
    setup()
