import platform
import socket
import time

import psutil
from fastapi import FastAPI
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, generate_latest
from starlette.responses import Response

app = FastAPI(
    title="System Health Monitor",
    version="1.0.0",
    description="Infrastructure health and metrics API",
)

START_TIME = time.time()

CPU_USAGE = Gauge("system_cpu_percent", "Current CPU utilization percentage")
MEMORY_USAGE = Gauge("system_memory_percent", "Current memory utilization percentage")
DISK_USAGE = Gauge("system_disk_percent", "Current root filesystem utilization percentage")
UPTIME = Gauge("system_uptime_seconds", "Application uptime in seconds")
HEALTH_CHECKS = Counter("health_check_total", "Total health endpoint requests")


def collect_metrics() -> dict:
    cpu = psutil.cpu_percent(interval=0.2)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    CPU_USAGE.set(cpu)
    MEMORY_USAGE.set(memory.percent)
    DISK_USAGE.set(disk.percent)
    UPTIME.set(time.time() - START_TIME)

    return {
        "cpu_percent": cpu,
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "uptime_seconds": round(time.time() - START_TIME, 2),
    }


@app.get("/")
def root():
    return {
        "service": "system-health-monitor",
        "version": app.version,
        "docs": "/docs",
        "health": "/health",
        "metrics": "/metrics",
    }


@app.get("/health")
def health():
    HEALTH_CHECKS.inc()
    metrics = collect_metrics()

    status = "healthy"
    if metrics["cpu_percent"] >= 90 or metrics["memory_percent"] >= 90:
        status = "degraded"

    return {
        "status": status,
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "metrics": metrics,
    }


@app.get("/system")
def system():
    return {
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "cpu_count": psutil.cpu_count(),
        **collect_metrics(),
    }


@app.get("/metrics")
def metrics():
    collect_metrics()
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
