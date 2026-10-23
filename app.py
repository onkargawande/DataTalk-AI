import streamlit as st
import pandas as pd
from core import ask_question,run_code

st.title(':bar_chart: Chat with your Data :chart_with_upwards_trend:')

file = st.file_uploader('upload a csv file', type = "csv")

if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    question = st.text_input('Ask question about your dataframe')

    if question and st.button('Get Answer'):
        code = ask_question(df, question)
        st.code(code, language="python")
        st.write(run_code(df,code))
        