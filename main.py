import streamlit as st
import joblib
import os

model_path = "model/prompt_detector.pkl"
if not os.path.exists(model_path):
    st.error("Model not found. Please train the model using detector.py")
    st.stop()

model = joblib.load(model_path)

st.title("Prompt Injection Detector")
st.write("Enter a prompt and check if it's safe or potentially malicious.")

user_input = st.text_area("Prompt Input:")

if st.button("Check Prompt"):
    prediction = model.predict([user_input])[0]
    proba = model.predict_proba([user_input])[0].max()

    if prediction == "malicious":
        st.markdown(f"*Prediction:* MALICIOUS ({proba * 100:.2f}% confidence)")
    else:
        st.markdown(f"*Prediction:* SAFE ({(1 - proba) * 100:.2f}% confidence)")