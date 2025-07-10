import streamlit as st
import google.generativeai as genai

# Streamlit UI
st.title("🧠 SmartIRAI - GPT-Powered Interview Simulator")

question = st.text_input("Enter an interview question")
answer = st.text_area("Your answer to the question")

# Load Gemini API Key
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Missing Gemini API key. Please add it in Streamlit secrets.")
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    if question and answer:
        if st.button("Analyze"):
            try:
                model = genai.GenerativeModel(model_name="models/gemini-pro")
                prompt = f"""You are a technical interviewer. A candidate answered this question: "{question}" 
                with: "{answer}". Please evaluate it with strengths, weaknesses, and suggested improvements."""

                response = model.generate_content(prompt)
                st.success("AI Feedback:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
