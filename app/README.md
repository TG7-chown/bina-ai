# Bina.AI

Bina.AI is a smart AI assistant that helps users build WordPress websites by simply describing what they need. It suggests themes, plugins, and generates content in English or Bahasa Melayu.

## Features
- Understands natural language prompts
- Recommends WordPress theme + plugins
- Writes Homepage, About, and Contact page content
- Beginner-friendly Streamlit interface

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app/main.py

### ✅ Optional: assets/logo.png
You can upload any logo image here later and display it in your Streamlit UI with:
```python
st.image("assets/logo.png", width=200)
