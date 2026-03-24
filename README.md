# 🔐 Phishing Detection System

A Machine Learning-based web application that detects whether a given URL is Safe, Suspicious, or Phishing in real time.

🌐 **Live Demo:** https://phishing-detector-eyy0.onrender.com/

---

## 🚀 Features

- 🔍 URL-based feature extraction  
- 🤖 Machine Learning model (Random Forest)  
- 🌐 Flask web interface  
- ⚡ Real-time prediction  
- 📊 Confidence score display  
- 🔗 API endpoint for automation  

---

## 🧠 How It Works

1. User enters a URL  
2. System extracts features (length, HTTPS, keywords, etc.)  
3. Features are passed to ML model  
4. Model predicts:
   - ✅ Safe  
   - ⚠️ Suspicious  
   - ❌ Phishing  

---

## 🛠️ Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- HTML, CSS (Bootstrap)  

---

## 📸 Screenshots

![Home](images/homepage.png)
![Safe](images/safe.png)
![Phishing](images/phishing.png)

## 📁 Project Structure


---

## ⚙️ Installation

```bash
git clone https://github.com/itspranayjain/phishing-detector.git
cd phishing-detector
pip install -r requirements.txt
python app.py
