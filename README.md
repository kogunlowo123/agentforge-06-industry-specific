# AgentForge 06 — Industry-Specific Agents

![Category](https://img.shields.io/badge/Category-06-c8420a) ![Cloud](https://img.shields.io/badge/Cloud-AWS%20%7C%20Azure%20%7C%20GCP-0078d4) ![License](https://img.shields.io/badge/License-MIT-16a34a)

## Quick Start
```bash
cp .env.example .env && pip install -r requirements.txt
python -m labs.exercise_06_1_beginner.agent
cd infrastructure/terraform/environments/dev && terraform init && terraform plan
```

## Structure
```
├── core/agent_base.py                  # ReAct loop, tool registry, cost tracker
├── labs/exercise_06_*/             # 4 exercises (beginner → stretch)
├── infrastructure/terraform/modules/   # runtime, datastore, gateway
├── infrastructure/docker/Dockerfile    # Multi-stage production image
├── tests/                              # pytest tests
├── .github/workflows/deploy.yml        # lint → test → tf validate
└── docs/                               # Architecture, practices, concepts
```

## Portal & Diagrams
- [Full Curriculum](https://kogunlowo123.github.io/agentforge-portal/)
- [Architecture Diagram](https://kogunlowo123.github.io/agentforge-portal/diagrams/06-industry-specific.html)

---
AgentForge v1.0 · MIT · [kogunlowo123](https://github.com/kogunlowo123)
