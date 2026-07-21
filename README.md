# AI-Powered Computer Vision Event Pipeline

An open-source, event-driven pipeline that transforms computer-vision detections into AI-analyzed, image-enriched real-time notifications and auditable event records using **Frigate, MQTT, n8n, OpenAI multimodal AI, Telegram, PostgreSQL, and Docker.**

## What it does
Frigate publishes computer-vision events over MQTT. n8n filters relevant detections, retrieves event imagery, submits it to OpenAI for structured multimodal analysis, recombines the image with the resulting intelligence, delivers a rich real-time phone notification through Telegram, and persists an auditable event record to PostgreSQL.

The current implementation monitors person detections from a front-door camera, while the workflow architecture can be adapted to additional cameras, object classes, notification channels, and downstream automation.

## Demonstrates
- Event-driven MQTT automation and n8n orchestration
- Frigate API integration and binary image handling
- Multimodal AI with constrained structured output
- Explicit analysis of hands and carried objects
- Package, vehicle, animal, OCR/text, and activity extraction
- Dynamic Telegram photo notifications
- PostgreSQL + JSONB event/audit logging
- AI response IDs and token telemetry
- End-to-end API and systems integration across self-hosted and cloud services

## Architecture
```text
Frigate -> MQTT -> n8n -> filter -> snapshot -> OpenAI vision
                                      |             |
                                      +----------> Merge
                                                    |
                                      +-------------+-------------+
                                      v                           v
                                   Telegram                   PostgreSQL
                                photo + summary             event/audit log
```

## Files
- `workflows/frigate-ai-camera-analysis.json` — sanitized importable workflow
- `database/schema.sql` — PostgreSQL schema
- `docs/architecture.md` — architecture notes
- `.env.example` — example configuration
- `.gitignore` — secret/runtime exclusions

## Security
No API keys, passwords, or bot tokens are included. Configure MQTT, OpenAI, Telegram, and PostgreSQL credentials in n8n after import. The RFC1918 Frigate address `10.1.1.13` is intentionally retained as an example of the self-hosted architecture. The Telegram destination is parameterized.

## Setup
1. Create `camera_event_log` using `database/schema.sql`.
2. Import the workflow JSON into n8n.
3. Configure MQTT, OpenAI, Telegram, and PostgreSQL credentials.
4. Set `TELEGRAM_CHAT_ID` and adjust Frigate URL/camera/topic as needed.
5. Test, then activate the workflow.

## Status
Working production proof-of-concept.

Planned enhancements:

Improve image timing by selecting a frame shortly after initial detection, allowing subjects to move farther into the camera frame before analysis.
Evaluate migration of multimodal analysis from OpenAI to locally hosted Ollama models to keep image processing entirely on-premises.
Integrate Home Assistant as an additional local notification and automation channel.
