import streamlit as st
import whisper

st.title(
    'Speech to text translation'
)

audio_file = st.file_uploader('Upload audio that you want to transcribe to text.', type=['wav', 'mp3', 'm4a'])

model = whisper.load_model('base')
st.success('Whisper model loaded')

# @st.cache_data
# def load_whisper_model(model_name:str = 'base'):
#     model = whisper.load_model(model_name)
#     return model

# if st.sidebar.button('Load whisper model'):
#     global model
#     model = load_whisper_model()
#     st.sidebar.success('Whisper model loaded')

if st.sidebar.button('Transcribe Audio'):
    if audio_file is not None:
        st.sidebar.info('Transcribing Audio')
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success('Transcription Complete')
        st.text(transcription['text'])
    else:
        st.sidebar.error('Please upload an audio file')

if audio_file:
    st.sidebar.header('Play original audio')
    st.sidebar.audio(audio_file)