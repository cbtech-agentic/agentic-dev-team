"""Tests for the main FastAPI application."""

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


def test_get_time(client):
    """Test the /time endpoint returns valid time data."""
    response = client.get("/time")
    assert response.status_code == 200

    data = response.json()
    assert "current_time" in data
    assert "timezone" in data
    assert "unix_timestamp" in data
    assert data["timezone"] == "UTC"
    assert isinstance(data["unix_timestamp"], int)


def test_health_check(client):
    """Test the /health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
