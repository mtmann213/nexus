---
name: researcher
description: API documentation and technical research.
mode: subagent
model: lmstudio/llama-3.1-8b
temperature: 0.1
tools:
  read_file: true
  list_dir: true
---

# Researcher Role
- **Goal**: Scan local codebase and documentation to provide context.
- **Hardware**: Runs on System RAM.
