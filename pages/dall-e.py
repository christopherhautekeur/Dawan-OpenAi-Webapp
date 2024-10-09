import streamlit as st
from tools import Processing

process = Processing()
key = st.text_input("Your Api Key")
st.subheader("Generate Image")

text = st.text_area("Enter a prompt to generate an image")

if st.button("Generate"):
    process.setApiKey(key)
    st.image(process.openai_create_image(text))
