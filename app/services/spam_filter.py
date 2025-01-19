import pickle
import os

# Load the model at startup
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "models/spam_classifier_model.pkl")
BLACKLIST_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Data/blacklist.txt")

with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

def load_blacklist():
    if os.path.exists(BLACKLIST_PATH):
        with open(BLACKLIST_PATH, "r") as file:
            return set(line.strip() for line in file)
    return set()

def save_to_blacklist(sender: str):
    with open(BLACKLIST_PATH, "a") as file:
        file.write(f"{sender}\n")

def predict_spam(subject: str, body: str, sender: str) -> bool:
    """
    Predicts whether the email is spam or not.
    :param subject: Email subject
    :param body: Email body
    :param sender: Email sender
    :return: True if spam, False otherwise
    """
    blacklist = load_blacklist()
    if sender in blacklist:
        return True

    # Preprocess input (subject + body)
    email_content = f"{subject} {body}"
    prediction = model.predict([email_content])  # Assumes model supports .predict()
    is_spam = bool(prediction[0])  # Convert to True/False

    if is_spam:
        save_to_blacklist(sender)

    return is_spam
