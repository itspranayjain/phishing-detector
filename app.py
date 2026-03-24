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
    if prob < 0.3:
        result = "✅ Safe (Low Risk)"
    elif prob < 0.7:
        result = "⚠️ Suspicious"
    else:
        result = "❌ Phishing (High Risk)"

    return render_template("index.html",
                           prediction_text=result,
                           probability=round(prob * 100, 2))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)