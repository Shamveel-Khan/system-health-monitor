# System Health Monitor

A containerized infrastructure monitoring project built to demonstrate practical skills in **IT System Engineering, DevOps, monitoring, automation, and troubleshooting**.

The project exposes system/application health metrics through a FastAPI service, collects metrics with Prometheus, and visualizes them in Grafana.

## Architecture

```text
                    ┌──────────────────────┐
                    │      Grafana         │
                    │  Dashboard / Alerts  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Prometheus       │
                    │ Metrics Collection   │
                    └──────────┬───────────┘
                               │ scrape
                               ▼
                    ┌──────────────────────┐
                    │     FastAPI App      │
                    │ /health /metrics     │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    ▼                      ▼
              System Metrics          App Health
             CPU / RAM / Disk        Service Status
```

## Features

- CPU, memory and disk monitoring
- Application health endpoint
- Prometheus-compatible metrics
- Grafana visualization
- Docker Compose deployment
- Automated tests
- GitHub Actions CI pipeline
- Health-check endpoint suitable for container orchestration
- Structured project layout for future expansion

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- psutil
- Prometheus
- Grafana
- Docker / Docker Compose
- Pytest
- GitHub Actions

## Quick Start

### 1. Clone

```bash
git clone https://github.com/Shamveel-khan/system-health-monitor.git
cd system-health-monitor
```

### 2. Start the stack

```bash
docker compose up --build
```

### 3. Open services

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- Metrics: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

Grafana default login:

```text
username: admin
password: admin
```

## API

### Health

```http
GET /health
```

Example:

```json
{
  "status": "healthy",
  "hostname": "monitor-api",
  "platform": "Linux"
}
```

### System Information

```http
GET /system
```

Returns current CPU, memory, disk and uptime information.

### Prometheus Metrics

```http
GET /metrics
```

Exposes metrics such as:

```text
system_cpu_percent
system_memory_percent
system_disk_percent
system_uptime_seconds
```

## Local Development

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

## Testing

```bash
pytest -q
```

## DevOps Pipeline

Every push / pull request triggers:

1. Checkout source code
2. Set up Python
3. Install dependencies
4. Run unit tests
5. Build Docker image

The pipeline is intentionally simple so the workflow is easy to understand and extend.

## Troubleshooting Scenario

A representative incident scenario:

> Grafana shows increasing CPU utilization and API latency.

Troubleshooting flow:

```text
Alert
  ↓
Check dashboard
  ↓
Confirm CPU / memory / disk
  ↓
Check API health
  ↓
Inspect application logs
  ↓
Identify abnormal process / resource
  ↓
Mitigation
  ↓
Verify recovery
  ↓
Document RCA
```

This mirrors the structured troubleshooting approach used in production equipment-support environments.

## Future Improvements

- Windows Performance Counter collector
- Linux node exporter integration
- Alertmanager
- Email / Teams notification
- PostgreSQL health monitoring
- Network latency / TCP port monitoring
- Log aggregation with Loki
- Kubernetes deployment
- Infrastructure as Code with Terraform

