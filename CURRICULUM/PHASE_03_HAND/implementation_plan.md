# Verify Phase 3 Implementation (Tool Calling Agents)

The curriculum for Phase 3 teaches the agent how to execute functions (JSON parsing and loop running). The required scripts (`LABS/agent_simple.py` and `LABS/agent_multitool.py`) are **already present** in the repository.

Our goal is not to write them from scratch, but rather to verify they meet the Phase 3 success criteria using the local `gemma-3-4b` model (or the cloud model, depending on `GROQ_API_KEY` configuration).

## Proposed Changes
No direct code modifications are planned initially unless tests reveal bugs.

### [LABS Configuration]
* We rely on the `LABS/config.py` configuration (currently set to `google/gemma-3-4b` for local).

## Verification Plan
We will execute both agent scripts to ensure they successfully generate JSON function calls and handle terminal evaluation without hallucinatory loops.

### Automated Tests
1. **Run Simple Agent**
   - Command: `wsl -e /home/dev/nexus/venv/bin/python /home/dev/nexus/LABS/agent_simple.py`
   - Expected Result: The agent outputs a JSON block causing `wavelength.py` to be created.

2. **Run Multi-Tool Agent**
   - Command: `wsl -e /home/dev/nexus/venv/bin/python /home/dev/nexus/LABS/agent_multitool.py`
   - Expected Result: The agent creates `test_calc.py`, executes it via `run_terminal_command`, reads the output `4`, and prints `FINISH: ...`.

### Manual Verification
Check that `wavelength.py` and `test_calc.py` were actually created on disk.
