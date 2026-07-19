# Architecture

Frigate → MQTT → n8n → FrontDoor/person filter → snapshot → OpenAI vision → structured JSON → Merge → Telegram + PostgreSQL.

The AI schema captures people, clothing, behavior, hands/held objects, packages, delivery evidence, vehicles, animals, visible text, and security-relevant observations. PostgreSQL combines relational fields with JSONB and retains model/token telemetry plus the original AI response.

## Future enhancement
Select a Frigate recording frame approximately 100 ms after initial detection so subjects are more fully in frame.
