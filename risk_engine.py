"""Backward-compatible entrypoint.

Run with:
    uvicorn risk_engine:app --reload

Preferred project structure:
    uvicorn backend.main:app --reload
"""

from backend.main import app
from backend.risk_engine import Decision, Urgency, decide_action, get_decision_color

__all__ = ["app", "Decision", "Urgency", "decide_action", "get_decision_color"]
