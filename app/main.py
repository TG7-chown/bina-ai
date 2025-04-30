import streamlit as st 
import os 
from openai import OpenAI 
from dotenv import load_dotenv 
from io import StringIO

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Bina.AI - Web Builder Buddy", layout="centered") 
st.title("Bina.AI - Your Web Builder Buddy")

st.markdown(""" 
Describe your website idea and let Bina.AI recommend WordPress themes, plugins, and generate starter content. 
""")

#Sample input
user_input = st.text_area("Describe your website idea:", placeholder="e.g. I want a website to sell homemade sambal and share recipes") 
language = st.selectbox("Choose Language", ["English", "Bahasa Melayu"])

#Session state for download
if "last_result" not in st.session_state: 
        st.session_state.last_result = ""

if st.button("Generate Website Plan") and user_input: 
        with st.spinner("Thinking like a web designer..."): 
                try: 
                        with open("app/prompt_template.txt", "r", encoding="utf-8") as file: 
                                base_prompt = file.read()

                        prompt = base_prompt.format(user_input=user_input, language=language)

                        response = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant that builds websites."},
                                {"role": "user", "content": prompt}
                            ]
                        )

                result = response.choices[0].message.content
                st.session_state.last_result = result

                st.markdown("### Website Plan")
                st.markdown(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

if st.session_state.last_result:
        st.download_button( 
                label="Download Website Plan as .txt", 
                data=st.session_state.last_result,
                file_name="binaai_website_plan.txt",
                mime="text/plain" 
        )
