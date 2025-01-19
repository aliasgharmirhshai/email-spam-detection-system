from app.services.spam_filter import predict_spam

def test_predict_spam():
    subject = "Claim your prize!"
    body = "You have won $1,000. Click here to collect it."
    result = predict_spam(subject, body, sender=None)
    assert result is True  # Assuming this input is classified as spam

def test_predict_non_spam():
    subject = "Meeting Agenda"
    body = "Let’s discuss the project updates in the meeting tomorrow."
    result = predict_spam(subject, body, sender=None)
    assert result is False  # Assuming this input is not classified as spam
