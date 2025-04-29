import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import sys

# Load secrets or env variables
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

st.title("Bina.AI - Your Web Builder Buddy")

user_input = st.text_area("Describe your website idea:")
language = st.selectbox("Choose Language", ["English", "Bahasa Melayu"])

if st.button("Generate Website Plan") and user_input:
    try:
        with open("app/prompt_template.txt", "r") as f:
            prompt = f.read().format(user_input=user_input, language=language)

        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that builds websites."},
                {"role": "user", "content": prompt}
            ]
        )

        st.markdown("### Website Plan:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
        sys.stderr.write(str(e))
