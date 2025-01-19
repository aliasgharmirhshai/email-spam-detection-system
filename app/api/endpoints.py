from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.spam_filter import predict_spam

router = APIRouter(prefix="/email", tags=["Email Detection"])


class EmailRequest(BaseModel):
    subject: str
    body: str
    sender: str


@router.post("/detect")
def detect_spam(email: EmailRequest):
    """
    Detects if the email is spam or not.
    """
    try:
        prediction = predict_spam(email.subject, email.body, email.sender)
        return {"spam": prediction, "message": "Detection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
