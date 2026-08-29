\# SentryOps - Autonomous Incident Response Agent



> An autonomous site reliability agent built on the \*\*TrueForge Agent Harness\*\*, featuring MCP tool integration, sandboxed diagnostic execution, and strict human approval gates.



\---



\## What it Does

SentryOps continuously ingests production error alerts, queries metrics and traces via \*\*MCP (Model Context Protocol)\*\*, tests root-cause fixes in an isolated sandbox, and \*\*halts before any irreversible operation\*\* (like rolling back or restarting services) until approved by a human engineer.



\## Architecture \& Harness Features

\* \*\*Agent Harness:\*\* TrueForge runtime managing state, execution loops, and persistent session reconnects.

\* \*\*Tool Connectivity:\*\* MCP server integration for telemetry and repository log checks.

\* \*\*Sandbox Execution:\*\* Safe sandbox runner for automated bisect and dry-run patches.

\* \*\*Safety Gate:\*\* Pauses execution at critical boundary before taking state-altering actions.



\---



\## Qodo Code Review Evidence

\* \*\*Representative Merged PR:\*\* \[PR #1: Implement TrueForge Agent Harness and Human-in-the-Loop Safety Gate](https://github.com/dharmkoshiya74/sentryops-agent/pull/1)

\* \*\*Qodo Review Impact:\*\*

&#x20; \* \*\*Concurrency \& State Safeguards:\*\* Qodo identified potential race conditions if multiple webhooks hit the agent before resolution. Added validation to prevent multiple approvals on a single session.

&#x20; \* \*\*Input Validation:\*\* Enforced strict Pydantic payload models to prevent malformed telemetry inputs.

&#x20; \* \*\*Test Coverage:\*\* Generated unit test suite for state transitions (IDLE -> ANALYZING -> WAITING\_FOR\_APPROVAL -> RESOLVED).



\---



\## Quickstart



\### 1. Install \& Run Backend

```powershell

cd backend

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

uvicorn backend.main:app --reload --port 8000

