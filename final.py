import sys
import streamlit as st
from src.model import qa_chain


# Set page title and icon
st.set_page_config(page_title="Potentiam Chatbot", page_icon=":robot_face:")

# Function to display chat messages

# Streamlit app title
st.title('Potentiam Chatbot')


text = st.text_input("Please enter your Query")
if st.button('Submit'):
    if not text:
        st.warning("Please enter your Query")
    else:
        with st.spinner("Please wait, it may take some time to run..."):
            result=qa_chain.invoke(user_input)
            response=result['result']
            st.write(response)
