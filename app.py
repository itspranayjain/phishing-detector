from flask import Flask, request, render_template
import joblib
from feature_extraction import extract_features

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]
    features = extract_features(url)

    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0][1]

    # Decision logic
    if prob < 0.4:
     result = "✅ Safe (Low Risk)"
    elif prob < 0.75:
     result = "⚠️ Suspicious"
    else:
     result = "❌ Phishing (High Risk)"

    return render_template("index.html",
                           prediction_text=result,
                           probability=round(prob * 100, 2))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)