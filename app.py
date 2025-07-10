import streamlit as st
import google.generativeai as genai

st.title("💬 Gemini Interview Assistant")

question = st.text_input("Enter Interview Question:")
answer = st.text_area("Enter Your Answer:")

if "GEMINI_API_KEY" not in st.secrets:
    st.error("Gemini API key not found in Streamlit secrets.")
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    if st.button("Analyze"):
        try:
            model = genai.GenerativeModel("models/gemini-pro")
            prompt = f"Question: {question}\nAnswer: {answer}\nGive constructive feedback."

            response = model.generate_content(prompt)
            st.write("### 🧠 AI Feedback:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
