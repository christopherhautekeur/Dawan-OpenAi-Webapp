import streamlit as st
import io

from tools import Processing

process = Processing()
key = st.text_input("Your Api Key")
st.subheader("Transcription")

uploaded_file = st.file_uploader("Upload a .mp3 file", type=["mp3", "wav"])
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    file = (uploaded_file.name, bytes_data, "audio/wav")

    if st.button("Transcribe"):
        st.write("Transcribed text:")
        process.setApiKey(key)
        st.write(process.openai_transcribe(file))

    if st.button("Translate"):
        st.write("Translated Audio File:")
        process.setApiKey(key)
        st.write(process.openai_translate(file))

text = st.text_area("Enter tts")

if st.button("TTS"):
    st.write("TTS:")
    process.setApiKey(key)
    audio_buffer = io.BytesIO(process.text_to_speech(text).read())
    st.audio(audio_buffer, format="audio/mp3")


record = st.experimental_audio_input("Record audio", key="audio_input")

if record:
    st.audio(record)
    if st.button("Transcribe"):
        st.write("Transcribed text:")
        process.setApiKey(key)
        st.write(process.openai_transcribe(record))


