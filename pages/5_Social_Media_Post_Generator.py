import os
from decouple import config

import streamlit as st
from model import GeneralModel

st.set_page_config(page_title="Inkwell - Socail Media Post Generator", page_icon="🖋️")

prompt = """ {context} """

def app():

    # Creating an object of prediction service
    pred = GeneralModel(generator_type="Social Media Post Generator", prompt=prompt)

    # api_key = st.sidebar.text_input("APIkey", type="password")
    api_key = config("OPENAI_API_KEY")
    # Using the streamlit cache
    @st.cache_data
    def process_prompt(input):

        return pred.model_prediction(input=input.strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Social Media Post Generator")

        # st.write("---")

        input = st.text_area(
            "Input Social Media Post creation details in here. Remember to be very descriptive.",
            max_chars=750,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")

app()
