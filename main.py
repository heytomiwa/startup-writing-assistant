import os

import streamlit as st
from model import GeneralModel

def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):
        return pred.model_prediction(input=input.strip(), api_key=os.getenv("OPENAI_API_KEY"))
    
    if api_key:
        # Setting up the title
        st.title("Email Generator")

        input = st.text_area(
            "Input email creation email in here. Remember to be very descriptive.",
            max_chars=150,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In Progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
