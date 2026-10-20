from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "system-health-monitor"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] in {"healthy", "degraded"}
    assert "metrics" in body


def test_system():
    response = client.get("/system")
    assert response.status_code == 200
    body = response.json()
    assert "cpu_percent" in body
    assert "memory_percent" in body
    assert "disk_percent" in body


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "system_cpu_percent" in response.text
