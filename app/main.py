import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Azure credentials from Streamlit secrets or .env
openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"  # Keep this version unless you’re using something newer

# Your deployment name in Azure
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# UI
st.title("Bina.AI - Your Web Builder Buddy")

user_input = st.text_area("Describe your website idea:")
language = st.selectbox("Choose Language", ["English", "Bahasa Melayu"])

if st.button("Generate Website Plan") and user_input:
    with open("app/prompt_template.txt", "r") as file:
        base_prompt = file.read()

    prompt = base_prompt.format(user_input=user_input, language=language)

    try:
        response = openai.ChatCompletion.create(
            engine=deployment_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that builds websites."},
                {"role": "user", "content": prompt}
            ]
        )

        st.markdown("### Website Plan:")
        st.write(response['choices'][0]['message']['content'])

    except Exception as e:
        st.error(f"Something went wrong: {e}")
