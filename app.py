import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="AI Interview Assistant")

st.title("🧠 SmartIRAI - Gemini-Powered Interview Simulator")
st.subheader("Enter an interview question and your answer to get instant AI feedback.")

# Input
question = st.text_input("Interview Question")
answer = st.text_area("Your Answer")

# Gemini API Key from secrets
if "GEMINI_API_KEY" not in st.secrets:
    st.warning("⚠ Please add your Gemini API key in Streamlit Secrets.")
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    if st.button("Analyze") and question and answer:
        try:
            model = genai.GenerativeModel("models/gemini-pro")
            prompt = f"""You are an expert technical interviewer.
            Question: {question}
            Candidate's Answer: {answer}
            Provide feedback on correctness, communication, clarity, and how to improve."""
            
            response = model.generate_content(prompt)
            st.success("AI Feedback:")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
