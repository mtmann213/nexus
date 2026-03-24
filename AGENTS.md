# Project Agents: Project Nexus Standard

## 👥 The Team
- **@senior-architect**: Strategic planner. High-level logic, design patterns, and system architecture. (Optimized for RAM tier/70B models).
- **@lead-developer**: Execution expert. Writes code, runs terminal commands, and manages Git. (Optimized for VRAM tier/14B models).
- **@researcher**: Knowledge specialist. Scans local docs and web for updated APIs.

## 🛠️ Tech Stack & Conventions
- **Language:** Python 3.12+ / NumPy / TensorFlow (Sionna).
- **Architecture:** Modular, service-oriented with robust Integration Harnesses.
- **Protocol:** Model Context Protocol (MCP) for tool integration.
- **Blackboard:** This file (`AGENTS.md`) is the single source of truth for cross-agent synchronization.

## 🛡️ Hardware Guardrails (RTX 3080 Ti / 64GB RAM)
- **Safe Inference:** Maintain VRAM < 11,000MB.
- **Critical Threshold:** > 11,500MB (Do NOT load models).
- **Performance Target:** ~19 tokens/sec (Local 35B).
- **Template Rule:** Strict alternating User -> Assistant patterns required.

## 🚦 Communication Protocol
1. **Plan First:** Always define the mathematical or architectural plan in the Architect's section below before coding.
2. **Execute:** The Developer implements only what has been architected.
3. **Verify:** Every task must conclude with a terminal-based verification or unit test.
4. **Handoff:** Update the "System State" section after every major change.

## 📍 System State
- **Status:** Phase 6 - Orchestration Complete
- **Last Run ID:** REF-1774377519
- **Sync Time:** 2026-03-24 13:41:28

## 🏛️ Architect's Section
- **Design:** Tiered memory architecture implemented via `LABS/config.py`.

## 🛠️ Developer's Section
- **Files Created:** benchmark_inference.py, store_memories.py, mcp_client.py, etc.
- **Status:** All baseline infrastructure scripts consolidated into `LABS/`.

### Architect's Section

**Run REF-1774377519 (2026-03-24 13:38:39)**
## 🏛️ Architect's Section: Multi-Agent Code Review & Refactoring System

### 1. High-Level Architecture Pattern
**Pattern:** Hierarchical Orchestrator with Specialized Workers (Orchestrator-Worker).
**Rationale:** Ensures safety in automated refactoring by separating decision-making from execution. The system operates as a pipeline where agents validate state before transitioning to the next phase.

### 2. Agent Role Mapping
| Nexus Role | Code Review Function | Responsibilities |
| :--- | :--- | :--- |
| **@senior-architect** | **Review Manager** | Defines review policies, approves high-risk refactors, validates architectural consistency, final safety gatekeeper. |
| **@lead-developer** | **Refactor Executor** | Generates specific code changes, applies patches via MCP file tools, writes unit tests for changed modules. |
| **@researcher** | **Knowledge Validator** | Verifies API usage against latest docs, checks for deprecated patterns, suggests library alternatives. |

### 3. Workflow Pipeline (State Machine)
1.  **Ingestion:** Codebase snapshot -> Hash verification.
2.  **Static Analysis:** Parse AST/IR for complexity metrics and dependency graphs.
3.  **Review Proposal:** `@researcher` identifies technical debt; `@senior-architect` prioritizes based on policy.
4.  **Refactor Plan:** `@lead-developer` drafts changes + test cases (Sandboxed).
5.  **Verification:** Run tests in isolated container/VM. Diff validation.
6.  **Commit:** Merge if pass rate = 100%; else rollback and report failure.

### 4. Safety & Concurrency Constraints
*   **Sandboxing:** All code modifications must be validated against a `virtualenv` or Docker container before production merge.
*   **MCP Restrictions:** File system access limited to read-only unless explicitly granted write permission for specific PR branches.
*   **Rollback Hooks:** Git reflog preservation required for every automated commit.
*   **Concurrency:** Only one active refactoring task per repository module to prevent race conditions on file locks.

### 5. Integration Points (MCP)
*   `mcp_git`: For branch creation, diffing, and merging.
*   `mcp_fs`: For reading/writing source files within sandbox limits.
*   `mcp_llm`: For semantic analysis queries (via local TensorFlow/Sionna inference where possible).

### 6. Data Model
*   **ReviewTicket:** UUID, Status (Open, In-Progress, Verified), Priority Level.
*   **ChangeProposal:** File Path, Diff Hash, Test Coverage Impact, AgentID.
*   **AuditLog:** Immutable record of all automated changes for compliance.

### 7. Next Steps for Developer
1.  Implement `ReviewManager` class to handle state transitions.
2.  Configure MCP toolsets for Git and Filesystem sandboxing.
3.  Initialize CI pipeline integration for test verification phase.

### Reviewer's Section

**Run REF-1774377519 (2026-03-24 13:38:39)**
## 🕵️ Reviewer's Section: Security & Reliability Audit

### 🔍 Critical Feedback on Architect's Design

While the Hierarchical Orchestrator pattern provides a solid foundation for separation of concerns, several critical risks regarding security, determinism, and concurrency control require immediate attention before Phase 6 execution.

**1. ⚠️ MCP Write Permissions Security Risk**
*   **Concern:** The design relies on "explicitly granted write permission" via `mcp_fs` for refactoring. This is a high-risk attack surface if the approval mechanism is automated or lacks cryptographic signing. An adversarial prompt injection could potentially escalate permissions to critical system files.
*   **Recommendation:** Implement a **Human-in-the-Loop (HITL) Approval Gate** for any `mcp_fs` write operations on production branches. Additionally, enforce **Signed Commits** where the refactoring agent must sign the diff hash using a private key before the merge hook executes.

**2. 🧠 Deterministic Parsing vs. LLM Inference**
*   **Concern:** The workflow suggests using `mcp_llm` for "semantic analysis queries" during the Static Analysis phase (Step 2). Relying on probabilistic models for AST parsing or structural dependency graphs introduces hallucination risks that can break code syntax irreparably.
*   **Recommendation:** Decouple structural analysis from semantic reasoning. Use deterministic Python libraries (`ast`, `tree-sitter`, `pylint`) for all file structure, complexity metrics, and dependency graph