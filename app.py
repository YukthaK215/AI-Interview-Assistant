import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Interview Assistant")

st.title("🧠 SmartIRAI - Gemini-Powered Interview Simulator")
st.subheader("Simulate interview answers and get instant AI feedback")

question = st.text_input("Enter the interview question")
answer = st.text_area("Enter your answer")

if "GEMINI_API_KEY" not in st.secrets:
    st.error("Gemini API Key not found in secrets.")
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    if st.button("Analyze") and question and answer:
        try:
            model = genai.GenerativeModel(model_name="models/gemini-pro")
            prompt = f"""
            You are an expert interviewer. The question is: "{question}".
            The candidate answered: "{answer}". Provide a detailed feedback highlighting strengths, weaknesses, and suggestions for improvement.
            """
            response = model.generate_content(prompt)
            st.success("AI Feedback:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
