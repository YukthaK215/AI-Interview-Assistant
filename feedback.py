import openai
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_answer(answer):
    prompt = f"Evaluate the following answer to a technical interview question:\n\n'{answer}'\n\nGive detailed feedback on tone, clarity, correctness, and suggestions."

    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert interview coach."},
            {"role": "user", "content": prompt}
        ]
    )

    feedback = gpt_response['choices'][0]['message']['content']
    sentiment = SentimentIntensityAnalyzer().polarity_scores(answer)

    return feedback, sentiment
