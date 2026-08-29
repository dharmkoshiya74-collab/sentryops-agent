import pytest
from backend.agent import SentryOpsAgent

def test_agent_approval_gate_flow():
    agent = SentryOpsAgent()
    assert agent.status == "IDLE"

    # Trigger incident
    res = agent.analyze_incident({"service": "auth-service", "error": "500 Internal Server Error"})
    assert agent.status == "WAITING_FOR_APPROVAL"
    assert res["requires_human_approval"] is True

    # Test rejection
    agent.execute_action(approved=False)
    assert agent.status == "ABORTED_BY_OPERATOR"

def test_agent_approval_resolution():
    agent = SentryOpsAgent()
    agent.analyze_incident({"service": "billing-service", "error": "Deadlock"})
    res = agent.execute_action(approved=True)
    assert agent.status == "RESOLVED"
    assert "successfully" in res["message"] or "Executed" in res["message"]
