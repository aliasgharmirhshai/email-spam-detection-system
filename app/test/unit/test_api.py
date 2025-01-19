from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_detect_spam():
    response = client.post(
        "/email/detect",
        json={
            "subject": "Win a free iPhone!",
            "body": "Click here to claim your prize now!",
            "sender": "promo@spam.com"
        }
    )
    assert response.status_code == 200
    assert "spam" in response.json()
    assert response.json()["spam"] is True
