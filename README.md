# 🚨 SMS Spam Detector

## 📌 Project Overview
This project is an interactive Machine Learning web application designed to classify SMS text messages as either "Spam" (malicious/promotional) or "Ham" (safe/legitimate). By leveraging Natural Language Processing (NLP), this tool demonstrates how unstructured text data can be transformed into mathematical vectors to automatically filter out phishing scams and unwanted advertisements.

## ⚙️ Tech Stack
* **Machine Learning:** Scikit-Learn (Multinomial Naive Bayes)
* **Natural Language Processing:** CountVectorizer (Bag of Words)
* **Data Manipulation:** Pandas
* **Web Deployment:** Streamlit
* **Model Serialization:** Joblib

## 🚀 Live Demo
Check out the live web application here: **[https://sms-spam-detector-k2.streamlit.app/]**

## 🧠 How It Works
The core of this application is a **Multinomial Naive Bayes** classifier, a probabilistic algorithm that is an industry standard for text classification.
1. **Text Preprocessing:** The user's input text is fed into a `CountVectorizer` pipeline, which tokenizes the text and converts it into a "Bag of Words" (a numerical matrix representing word frequencies).
2. **Prediction Pipeline:** The mathematical vector is passed to the trained Naive Bayes model. The model calculates the probability of the message being Spam vs. Ham based on the historical word patterns it learned during training.
3. **User Interface:** The entire pipeline is wrapped in a clean, interactive Streamlit web interface where users can paste messages and receive real-time security alerts.

## 📂 Repository Structure
* `app.py`: The Streamlit web application script.
* `spam_model.pkl`: The serialized Machine Learning pipeline (containing both the text vectorizer and the Naive Bayes model).
* `requirements.txt`: The dependencies required to run the app.

## 💻 How to Run Locally
1. Clone this repository to your local machine.
2. Install the required packages: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`

## ⚠️ Model Limitations & Real-World Applicability
While this model is highly effective on the dataset it was trained on, it has several limitations inherent to the Naive Bayes algorithm and basic NLP techniques:

* **Lack of Context (Feature Independence):** Naive Bayes strictly assumes every word is independent of the others. It evaluates words like "Free" and "Money" separately, completely ignoring the sequential context, sarcasm, or grammatical structure of the overall phrase.
* **The "Unseen Word" Problem:** Spammers constantly invent new slang, abbreviations, and intentional misspellings (e.g., "Fr33 M0ney" or "C1ick h3re") to evade filters. Because this model relies on a static vocabulary learned during training, it can struggle to classify previously unseen character variations.
* **Evolving Phishing Tactics:** Modern spam heavily relies on malicious URLs. This model only analyzes plain text frequencies and does not actively scan, resolve, or verify the safety of embedded web links.

**Future Improvements:** To upgrade this into a production-grade enterprise spam filter, the architecture would need to transition from a Bag-of-Words approach to a Deep Learning sequence model (like an LSTM or a Transformer such as BERT) that natively understands word sequences and context.
