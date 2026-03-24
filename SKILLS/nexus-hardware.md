# Skill: Nexus Hardware Management
## Description: Expert guidance for managing and monitoring the Project Nexus local hardware stack.

### 1. Context
- **Primary Hardware:** NVIDIA RTX 3080 Ti (12GB VRAM).
- **Environment:** Ubuntu 24.04 (Native or WSL).
- **Control Plane:** Model Context Protocol (MCP).

### 2. Available Tools
- `get_gpu_status`: Returns real-time VRAM usage and GPU utilization.

### 3. Procedural Rules (Expert Logic)
- **VRAM Guardrail:** If VRAM usage is above **11,500MB (93%)**, do NOT attempt to load additional models. Suggest offloading or quantization.
- **Inference Speed:** Typical performance for a 35B model should be ~19 t/s. If speed drops below 5 t/s, check for thermal throttling or background processes.
- **MCP Protocol:** Always use the standardized `mcp_client.py` pattern to connect to the hardware server.

### 4. Expert Workflows
#### Checking Hardware Health
1. Start the `nexus_hardware_server.py`.
2. Connect using `mcp_client.py`.
3. Call `get_gpu_status`.
4. Analyze results against the VRAM Guardrail.

### 5. Code Examples
```python
# Optimal connection parameters for the local hardware server
server_params = StdioServerParameters(
    command="./venv/bin/python",
    args=["nexus_hardware_server.py"],
)
```
