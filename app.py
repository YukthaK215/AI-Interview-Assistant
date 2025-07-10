import streamlit as st
from feedback import analyze_answer

st.set_page_config(page_title="AI Interview Assistant", page_icon="🤖")
st.title("🤖 AI Interview Assistant")

st.markdown("Simulate technical interviews and get instant AI-powered feedback.")

question = st.text_input("💬 Enter an interview question:")
answer = st.text_area("📝 Your answer to the question:")

if st.button("Analyze"):
    if not answer:
        st.warning("Please enter your answer.")
    else:
        feedback, sentiment = analyze_answer(answer)
        st.subheader("🔍 AI Feedback")
        st.write(feedback)

        st.subheader("📊 Sentiment Analysis")
        st.json(sentiment)

st.caption("Made with 💡 using OpenAI and Python NLP")
