import streamlit as st
from transcriber import transcribe_audio

st.set_page_config(page_title="WhisperStream", layout="centered")
st.title("🎤 WhisperStream (API Version)")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    with st.spinner("Transcribing via OpenAI Whisper API..."):
        transcript = transcribe_audio(uploaded_file)
        st.text_area("Transcript", transcript, height=300)
        st.download_button("Download Transcript", transcript, file_name="transcript.txt")
