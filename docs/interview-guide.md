# Interview Guide

## 30-second version

> I built a containerized system health monitoring platform to practice IT infrastructure and DevOps concepts.
> The API collects CPU, memory and disk metrics, Prometheus handles metric collection, and Grafana provides visualization.
> I also added automated tests and a GitHub Actions CI pipeline.
> The project reflects the troubleshooting workflow I use in semiconductor equipment support: detect an abnormal condition, collect evidence, isolate the problem, recover the service, and verify the result.

## 90-second version

> My current role is mainly semiconductor equipment software support, so I wanted to build a project that translates that experience into a more general IT infrastructure environment.
>
> I designed a small monitoring stack with FastAPI, Prometheus and Grafana. The FastAPI service exposes health and system metrics, Prometheus periodically collects those metrics, and Grafana visualizes CPU, memory and disk utilization.
>
> I containerized the components with Docker Compose and added GitHub Actions to automatically run tests and build the Docker image after code changes.
>
> The main thing I wanted to demonstrate was not just programming. I wanted to show an operational mindset: monitoring, health checks, troubleshooting, verification, and repeatable deployment.
>
> This is similar to how I currently troubleshoot equipment-side incidents. I first identify the symptom, collect logs and system information, isolate whether the issue is software, system or network related, perform recovery, and then verify that production is stable.

## Common Questions

### Why did you build this project?

I wanted to bridge my semiconductor equipment support experience into IT infrastructure and DevOps. Monitoring and troubleshooting are already part of my daily work, so this project helped me demonstrate those skills in a general-purpose environment.

### Why Prometheus?

Prometheus is designed around time-series metrics and a pull-based scraping model. It is a good fit for demonstrating infrastructure monitoring.

### Why Grafana?

Grafana provides visualization and makes trends easier to identify. For example, a single CPU value is less useful than seeing CPU utilization continuously increase over time.

### Why Docker?

Docker makes the environment reproducible. Instead of manually installing Python, Prometheus and Grafana, the whole stack can be started with one `docker compose up`.

### What would you improve next?

I would add Alertmanager, centralized logs, network/TCP checks, persistent metric storage, and eventually deploy the stack to Kubernetes. I would also separate the application into collectors and add role-based configuration.

### What happens if the API goes down?

Prometheus stops receiving metrics and Grafana can show the missing-data condition. In a production environment, I would add an alert for target availability and use service restart policies or an orchestration platform for recovery.

### What is the difference between monitoring and logging?

Monitoring focuses on measurable system state such as CPU, memory, latency and availability. Logging provides detailed event information that helps investigate why a problem occurred. In troubleshooting, I would normally use both.

### How would you use this in a real company?

I would adapt the collectors to monitor approved server and service endpoints, define thresholds based on operational requirements, add alerts, and integrate the result with the team's incident-management workflow.

## Important honesty point

This is a portfolio lab, not a production monitoring system. In an interview, clearly distinguish what was implemented in the project from what is planned as a production enhancement.
