import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Bina.AI - Your Web Builder Buddy")

user_input = st.text_area("Describe your website idea:")
language = st.selectbox("Choose Language", ["English", "Bahasa Melayu"])

if st.button("Generate Website Plan"):
    with open("app/prompt_template.txt", "r") as file:
        base_prompt = file.read()

    prompt = base_prompt.format(user_input=user_input, language=language)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    st.markdown("### Website Plan:")
    st.write(response['choices'][0]['message']['content'])
