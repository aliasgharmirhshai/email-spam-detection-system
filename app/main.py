from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(title="Email Spam Detection API")

# Include the email detection routes
app.include_router(endpoints.router)
