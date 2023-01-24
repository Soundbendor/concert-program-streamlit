import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()

with header:
    st.title('soundbendor lab: concert program OCR')
    st.text('Researchers in computational musicology desire to apply modern natural language processing techniques to historic documents describing musical pieces and specific performances. This project allows users to download datasets of professional symphony orchestras concert programs.')

with dataset:
    st.header('concert program dataset')
    st.text('This data is scrapped from the New York Philharmonic which provides publicily available archives of documents.')

with features:
    st.header('available composers')
    st.markdown('* **Beethoven**')
    st.markdown('* **Mozart**')
    st.markdown('* **Tchaikovsky**')
