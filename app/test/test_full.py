from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_full_stack_spam_detection():
    # Simulate an end-to-end request
    response = client.post(
        "/email/detect",
        json={
            "subject": "Congratulations! You've won!",
            "body": "Click here to receive your prize.",
            "sender": "winner@spam.com"
        }
    )
    assert response.status_code == 200
    result = response.json()
    assert "spam" in result
    assert result["spam"] is True
    assert result["message"] == "Detection successful"
