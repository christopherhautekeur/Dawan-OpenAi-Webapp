import io

import streamlit as st

from tools import Processing

st.title("Chatbot with OpenAI")

process = Processing()

key = st.text_input("Your Api Key")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        if type(message['content']) is io.BytesIO:
            st.audio(message['content'], format="audio/mp3")
        elif "https://" in message['content']:
            st.image(message['content'])
        else:
            st.markdown(message['content'])

if prompt := st.chat_input("You:"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
        process.setApiKey(key)

    with st.chat_message("assistant"):
        # Handle response
        if "tts/" in prompt:
            prompt = prompt.split("tts/")[1]
            response = io.BytesIO(process.text_to_speech(prompt).read())
            st.audio(response, format="audio/mp3")
        elif "complete/" in prompt:
            response = process.openai_generate(prompt)
            st.markdown(response)
        elif "imagine/" in prompt:
            response = process.openai_create_image(prompt)
            st.image(response)
        else:
            response = f"echo: {prompt}"
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
