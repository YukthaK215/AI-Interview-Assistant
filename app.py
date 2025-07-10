import streamlit as st
from openai import OpenAI

# Get your OpenAI key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Interview Assistant", page_icon="🤖")
st.title("🧠 AI Interview Assistant")

st.write("Simulate a technical interview and get instant feedback using AI.")

# Input fields
question = st.text_input("Enter an interview question:")
answer = st.text_area("Your answer to the question:")

if st.button("Analyze"):
    if not question or not answer:
        st.warning("Please enter both a question and an answer.")
    else:
        with st.spinner("Analyzing your answer..."):
            try:
                prompt = f"You are a professional interview coach. Provide constructive feedback on the following answer:\n\nQuestion: {question}\nAnswer: {answer}"

                chat_response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=300
                )

                feedback = chat_response.choices[0].message.content
                st.success("✅ Feedback received:")
                st.write(feedback)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
