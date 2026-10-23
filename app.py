# Import Streamlit to build the app's web interface.
import streamlit as st
# Import Pandas to read and work with CSV data.
import pandas as pd
# Import the functions that ask the AI for code and run it.
from core import ask_question,run_code

# Show the app title at the top of the page.
st.title(':bar_chart: Chat with your Data :chart_with_upwards_trend:')

# Let the user choose a CSV file to upload.
file = st.file_uploader('upload a csv file', type = "csv")

# Continue only after the user uploads a file.
if file:
    # Read the uploaded CSV file into a Pandas DataFrame.
    df = pd.read_csv(file)
    # Show a preview of the first few rows.
    st.dataframe(df.head())

    # Give the user a box to type a question about the data.
    question = st.text_input('Ask question about your dataframe')

    # Get and display an answer when the user enters a question and clicks the button.
    if question and st.button('Get Answer'):
        # Ask the AI to generate pandas code for the question.
        code = ask_question(df, question)

        # Display the generated code in the app.
        st.code(code, language="python")

        # Run the code on the uploaded data and show the result.
        st.write(run_code(df, code))
        
