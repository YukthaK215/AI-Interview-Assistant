import streamlit as st
import google.generativeai as genai

st.title("🧠 SmartIRAI - GPT-Powered Interview Simulator")

question = st.text_input("Enter an interview question")
answer = st.text_area("Your answer to the question")

# Configure Gemini using your API key
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Missing Gemini API key. Please add it in Streamlit secrets.")
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-pro")

    if st.button("Analyze") and question and answer:
        with st.spinner("Analyzing your response..."):
            try:
                prompt = f"""You are an expert interviewer. A candidate answered this question: "{question}"
                with: "{answer}". Please provide a short evaluation with strengths, areas of improvement, and suggestions."""

                response = model.generate_content(prompt)
                st.success("AI Feedback:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
