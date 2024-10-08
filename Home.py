import streamlit as st
from tools import Processing

process = Processing()



# Page config
st.set_page_config(
    page_title="Dawan OpenAI Webapp",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Dawan OpenAI Webapp")

key = st.sidebar.text_input("Your Api Key")

st.subheader("Translate")

text = st.text_area("Enter text to translate")

if st.button("Translate"):
    st.write("Translated text:")
    process.setApiKey(key)
    st.write(process.openai_translate(text))

st.subheader("Summarize")

text = st.text_area("Enter text to summarize")

if st.button("Summarize"):
    st.write("Summarized text:")
    process.setApiKey(key)
    st.write(process.openai_summarize(text))

st.subheader("Generate")

text = st.text_area("Enter a subject to generate")

if st.button("Generate"):
    st.write("Generated text:")
    process.setApiKey(key)
    st.write(process.openai_generate(text))

st.subheader("Verify")

text = st.text_area("Enter code to verify")

if st.button("Verify"):
    st.write("Ouput:")
    process.setApiKey(key)
    st.write(process.openai_codex(text))