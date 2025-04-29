import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Bina.AI - Your Web Builder Buddy")

user_input = st.text_area("Describe your website idea:")
language = st.selectbox("Choose Language", ["English", "Bahasa Melayu"])

if st.button("Generate Website Plan") and user_input:
    with open("app/prompt_template.txt", "r") as file:
        base_prompt = file.read()
    prompt = base_prompt.format(user_input=user_input, language=language)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that builds websites."},
                {"role": "user", "content": prompt}
            ]
        )

        st.markdown("### Website Plan:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
