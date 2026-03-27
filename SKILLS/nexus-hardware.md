# Skill: Nexus Hardware Management
## Description: Expert guidance for managing and monitoring the Project Nexus local hardware stack (3080 Ti / 64GB RAM).

### 1. Context
- **Primary Hardware:** NVIDIA RTX 3080 Ti (12GB VRAM).
- **Secondary Memory:** 64GB System RAM (Available for CPU offloading).
- **Environment:** Ubuntu 24.04.
- **Control Plane:** Model Context Protocol (MCP).

### 2. Available Tools
- `get_gpu_status`: Returns real-time VRAM usage and GPU utilization.

### 3. Procedural Rules (Expert Logic)
- **VRAM Guardrail:** 
    - < 11,000MB: Safe for 35B Inference.
    - > 11,500MB: Critical. Do NOT load new models. Recommend deleting KV cache or offloading layers to System RAM.
- **Inference Speed:** Target ~19 t/s. If < 5 t/s, the model has likely swapped to System RAM (CPU bottleneck).
- **Template Awareness:** All local inference via LM Studio requires strict alternating **User -> Assistant** patterns. Never send consecutive roles.

### 4. Expert Workflows
#### Hardware Recovery Strategy (OOM)
1. If an `OutOfMemory` error occurs, immediately check `get_gpu_status`.
2. Identify if the KV cache size can be reduced (e.g., from 32k to 16k).
3. If using multi-agent swarms, ensure only ONE high-parameter model is in VRAM at a time.

#### Vision Model Integration
1. When using multimodal models (Vision), reserve 2GB of VRAM headroom for image encoding.
2. Prioritize `qwen2-vl` for analyzing GNU Radio screenshots.

### 5. Code Examples
```python
# Standard Defensive JSON Parsing Pattern
start_idx = raw_output.find("{")
end_idx = raw_output.rfind("}")
clean_json = raw_output[start_idx:end_idx + 1]
```

### 6. 5G Sionna Simulation VRAM Strategy
When explicitly encountering a `ResourceExhaustedError` during a TensorFlow or Sionna 5G pipeline simulation, you MUST follow this mandatory 3-step procedural playbook:
1. **Precision Downgrade:** Inspect the traceback to determine if the pipeline is running in `tf.float64` / `tf.complex128`. You must explicitly instruct the user to downgrade Sionna precision to `tf.complex64` via dtype overriding to save 50% memory immediately.
2. **Dimension Scaling:** Locate the `batch` parameter in the tensor shape. You must instruct the user to strictly cut their batch size by exactly 50% (e.g., if 1024, suggest 512).
3. **Dataset Optimization:** Suggest utilizing `tf.data.Dataset` mapping optimizations if caching is overflowing the GPU (e.g., recommend `.prefetch(tf.data.AUTOTUNE)`).
**CRITICAL:** Do NOT hallucinate generic Python memory advice (like `gc.collect()`). You must provide exactly these 3 steps in your response.
