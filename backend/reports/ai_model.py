import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load model once
model = MobileNetV2(weights='imagenet')


def predict_issue(image_path, title="", description=""):
    text = (image_path + " " + title + " " + description).lower()

    if "pothole" in text or "road" in text or "hole" in text:
        return "pothole", 4

    elif "garbage" in text or "trash" in text or "waste" in text:
        return "garbage", 3

    elif "drainage" in text or "flood" in text or "water" in text:
        return "drainage", 4

    elif "streetlight" in text or "light" in text or "dark" in text:
        return "streetlight", 2

    else:
        return "unknown", 1
