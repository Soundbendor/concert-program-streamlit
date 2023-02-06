import streamlit as st

st.set_page_config(
    title="concert program OCR"
)

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

    sel_col, disp_col = st.columns(2)

    n_composers = sel_col.selectbox('Which composer would you like to choose?', options=['Beethoven', 'Mozart', 'Tchaikovsky'], index = 0)
