import os

import streamlit as st
from tools import Processing

process = Processing()
key = st.text_input("Your Api Key")
st.subheader("Generate Image")

text = st.text_area("Enter a prompt to generate an image")

if st.button("Generate"):
    process.setApiKey(key)
    st.image(process.openai_create_image(text))

st.subheader("Generate Image Variation")

img = st.file_uploader("Upload an image to generate an image variation", type=["png", "jpg", "jpeg"])
if st.button("Generate Variation"):
    process.setApiKey(key)
    if img is not None:
        url = f"tmp.{img.name.split('.')[1]}"
        with open(url, 'wb') as f:
            f.write(img.getvalue())
        st.image(process.openai_create_image_variation(url))
