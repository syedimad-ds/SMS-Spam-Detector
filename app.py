import streamlit as st
import joblib

model = joblib.load('spam_model.pkl')

st.title("🚨 SMS Spam Detector")
st.write("Are you unsure if a text message is a scam? Paste it below to find out!")

user_input = st.text_area("Enter the text message here:", "")

if st.button("Check Message"):
    
    if user_input.strip() == "":
        st.warning("Please type or paste a message into the box first!")
    else:
        prediction = model.predict([user_input])[0]
        if prediction == 'spam':
            st.error("🛑 ALERT: This message is SPAM!")
        else:
            st.success("✅ RELAX: This message is SAFE.")
