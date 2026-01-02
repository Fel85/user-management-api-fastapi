import os
import tempfile

import pytest
from fastapi.testclient import TestClient

from app.core.config import settings


@pytest.fixture(scope="session", autouse=True)
def _test_db():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    settings.DATABASE_URL = f"sqlite:///{path}"
    yield
    try:
        os.remove(path)
    except OSError:
        pass


def test_flow():
    # Import after DB override
    from app.main import app
    from app.db.init_db import init_db

    # Ensure tables exist for the test DB
    init_db()

    with TestClient(app) as client:
        r = client.post(
            "/api/v1/users",
            json={
                "email": "felipe@example.com",
                "full_name": "Felipe Test",
                "password": "SuperSecret123",
                "is_active": True,
            },
        )
        assert r.status_code == 201, r.text

        r = client.post(
            "/api/v1/auth/login",
            data={"username": "felipe@example.com", "password": "SuperSecret123"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        assert r.status_code == 200, r.text
        token = r.json()["access_token"]

        r = client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
        assert r.status_code == 200, r.text
        me = r.json()

        r = client.put(
            f"/api/v1/users/{me['id']}",
            json={"full_name": "Felipe Updated"},
            headers={"Authorization": f"Bearer {token}"},
        )
        assert r.status_code == 200, r.text
        assert r.json()["full_name"] == "Felipe Updated"

        r = client.delete(
            f"/api/v1/users/{me['id']}",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert r.status_code == 204, r.text
