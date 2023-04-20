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

with features:
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')
    
    st.header(':orange[datasets]')

    sel_col, disp_col = st.columns(2)

    n_composers = sel_col.selectbox('Which sample would you like to choose?',
        options=['Sample 1', 'Sample 2', 'Sample 3'], index = 0)

    if n_composers == "Sample 1":
        sample_1_df = pd.read_csv("data/sample1.csv")
        st.dataframe(sample_1_df)
        
        sample_1_csv = convert_df(sample_1_df)
        
        st.download_button(
            label="Download data as CSV",
            data=sample_1_csv,
            file_name="sample1.csv",
            mime="text/csv",
            help="Click or Tap the button to download"
        )
    if n_composers == "Sample 2":
        sample_2_df = pd.read_csv("data/sample2.csv")
        st.dataframe(sample_2_df)
        
        sample_2_csv = convert_df(sample_2_df)
        
        st.download_button(
            label="Download data as CSV",
            data=sample_2_csv,
            file_name="sample2.csv",
            mime="text/csv",
            help="Click or Tap the button to download"
        )
    if n_composers == "Sample 3":
        sample_3_df = pd.read_csv("data/sample3.csv")
        st.dataframe(sample_3_df)
        
        sample_3_csv = convert_df(sample_3_df)
        
        st.download_button(
            label="Download data as CSV",
            data=sample_3_csv,
            file_name="sample3.csv",
            mime="text/csv",
            help="Click or Tap the button to download"
        )

with contacts:
    st.header(':orange[contact information]')
    st.text('Author: Patrick Donnelly\n'
            'Contributors: Jonah Broyer, Samson DeVol')
