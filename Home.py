import streamlit as st
from tools import Processing

# Page config
st.set_page_config(
    page_title="Dawan OpenAI Webapp",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded",
)

process = Processing()

st.title("Dawan OpenAI Webapp")

openai_page = st.Page("pages/openai.py", title="OpenAI")
dalle_page = st.Page("pages/dall-e.py", title="DALL-E")
whisper_page = st.Page("pages/whisper.py", title="Whisper")
chatbot_page = st.Page("pages/chatgpt.py", title="Chatbot")

pg = st.navigation([openai_page,dalle_page,whisper_page,chatbot_page], position="sidebar")
pg.run()





