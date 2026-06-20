# SPASHT AI
While this repository contains the full collaborative project, my primary focus was on engineering the **Data Intelligence Layer**, which allows the AI to accurately route emergency distress calls based on urgency and risk.

##  My Contributions
I engineered the core datasets that power the system's routing logic. These JSON-based intelligence layers allow the AI to categorize incoming voice-to-voice interactions into four distinct decision paths:
* **`PROCEED.json`**: Datasets for routine civic and utility reports (e.g., potholes, streetlights, internet outages) requiring low-urgency processing.
* **`CONFIRM.json`**: Datasets for "surgical" AI verification, handling cultural understatements, vague descriptions, and sudden dialect shifts.
* **`ESCALATE.json`**: Datasets for high-urgency, life-threatening emergencies (e.g., mass transit disasters, active shootings) designed to bypass AI loops for immediate human intervention.
* **`SHADOW_SPEECH.json`**: A specialized safety protocol for domestic violence victims. This dataset trains the model to detect coded distress signals (e.g., pretending to order a pizza while signaling entrapment) and trigger a 10/10 urgency override.

##  Technical Approach
1. **Dataset Engineering**: Authored hundreds of simulated emergency scenarios featuring Kannada, Hindi, and English code-switching.
2. **Risk Mapping**: Each scenario is mapped with precise `expected_urgency` (0.0–1.0) and `expected_confidence` (0.0–1.0) scores to calibrate the model’s threat-detection logic.
3. **Dialect Awareness**: Scenarios include region-specific Bengaluru Kannada phrasing and pragmatic understatements to improve real-world model performance.
