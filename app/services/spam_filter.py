import pickle
import os
# Load the model at startup
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "models/spam_classifier_model.pkl")

with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

def predict_spam(subject: str, body: str) -> bool:
    """
    Predicts whether the email is spam or not.
    :param subject: Email subject
    :param body: Email body
    :return: True if spam, False otherwise
    """
    # Preprocess input (subject + body)
    email_content = f"{subject} {body}"
    prediction = model.predict([email_content])  # Assumes model supports .predict()
    return bool(prediction[0])  # Convert to True/False
