import streamlit as st
from transformers import pipeline

fugu_translator = pipeline('translation', model='staka/fugumt-ja-en')

st.title("Japanese to English Translator")
st.write("日本語を入力してください。")

input_text = st.text_area("日本語を入力してください。", height=200)

if st.button("翻訳"):
    translated_text = fugu_translator(input_text)[0]['translation_text']
    st.write("翻訳結果")
    st.write(translated_text)