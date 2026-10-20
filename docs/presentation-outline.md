# Interview Presentation — 5 Slides

## Slide 1 — Problem

**From Equipment Support to IT Infrastructure**

- Existing experience: system troubleshooting, logs, network, software deployment
- Goal: demonstrate infrastructure / DevOps skills with a reproducible project

## Slide 2 — Architecture

```text
FastAPI → Prometheus → Grafana
   ↑
Docker Compose
```

Explain data flow and why each component exists.

## Slide 3 — Monitoring

Show Grafana dashboard.

Talk about:
- CPU
- Memory
- Disk
- Health endpoint
- Metrics collection

## Slide 4 — DevOps

Show GitHub repository and Actions.

Explain:
- Git workflow
- Automated tests
- Docker build
- Repeatable deployment

## Slide 5 — Troubleshooting / Next Step

Incident example:

```text
Alert → Evidence → Isolation → Recovery → Verification → RCA
```

Then mention future improvements:
- Alertmanager
- Log aggregation
- Network checks
- Kubernetes
- Terraform
