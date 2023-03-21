import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="concert program OCR"
)

header = st.container()
dataset = st.container()
features = st.container()
contacts = st.container()

with header:
    st.title(':orange[soundbendor lab: concert program OCR]')
    st.text('Researchers in computational musicology desire to apply modern natural language\n'
            'processing techniques to historic documents describing musical pieces and specific\n'
            'performances. This project allows users to download datasets of professional\n' 
            'symphony orchestra concert programs.')
    st.text('Link to GitHub repository:\n' 
            'https://github.com/Soundbendor/concert-program-ocr')

with dataset:
    st.header(':orange[concert program dataset]')
    st.text('This data is scrapped from the New York Philharmonic which provides publicily\n'
            'available archives of documents.\n'
            'Note that you can sort, resize, and search through the table.')
    sample = pd.read_csv('data/example_concert_data.csv')
    st.dataframe(sample, use_container_width=True)
    st.bar_chart(sample, y=['orch','first_location'])


with features:
    st.header(':orange[available composers]')
    st.markdown('* **Beethoven**')
    st.markdown('* **Mozart**')
    st.markdown('* **Tchaikovsky**')

    sel_col, disp_col = st.columns(2)

    n_composers = sel_col.selectbox('Which composer would you like to choose?',
        options=['Beethoven', 'Mozart', 'Tchaikovsky'], index = 0)

with contacts:
    st.header(':orange[contact information]')
    st.text('Author: Patrick Donnelly\n'
            'Contributors: Jonah Broyer, Samson DeVol')
