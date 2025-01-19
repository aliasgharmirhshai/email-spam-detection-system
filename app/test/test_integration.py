from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_integration_detect_spam():
    response = client.post(
        "/email/detect",
        json={
            "subject": "Act now! Limited time offer!",
            "body": "Get a 50% discount on your purchase. Click here.",
            "sender": "offers@marketing.com"
        }
    )
    assert response.status_code == 200
    assert response.json()["spam"] is True

def test_integration_detect_non_spam():
    response = client.post(
        "/email/detect",
        json={
            "subject": "Weekly Project Update",
            "body": "Please find the project updates attached.",
            "sender": "team@company.com"
        }
    )
    assert response.status_code == 200
    assert response.json()["spam"] is False
