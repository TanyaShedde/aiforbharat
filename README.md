# SPASHT AI Backend

FastAPI backend for the SPASHT AI prototype. It accepts simulated caller text, returns a mock intent with confidence and urgency, and sends back the final decision for the frontend dashboard.

## Your backend files

```text
backend/
  main.py
  risk_engine.py
requirements.txt
```

## Setup

```powershell
cd C:\Users\Vanshika\aiforbharat
python -m pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Open API docs:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### GET /

Health check.

### GET /mock-intent

Returns the backend's hardcoded mock intent mappings.

### POST /mock-intent

Request:

```json
{
  "text": "Someone is following me and I am scared"
}
```

Response:

```json
{
  "text": "Someone is following me and I am scared",
  "intent": "harassment",
  "confidence": 0.6,
  "urgency": 0.9
}
```

### POST /analyze

Request:

```json
{
  "text": "Someone is following me and I am scared"
}
```

Response:

```json
{
  "text": "Someone is following me and I am scared",
  "intent": "harassment",
  "confidence": 0.6,
  "urgency": 0.9,
  "decision": "ESCALATE",
  "color": "red"
}
```

## Decision rules

- High urgency: `ESCALATE`
- Low confidence and medium risk: `CONFIRM`
- High confidence and low risk: `PROCEED`
- Risky cases such as violence, break-in, or harassment with medium urgency: `CONFIRM`
