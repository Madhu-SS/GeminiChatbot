import sys
import streamlit as st
from src.model import qa_chain


# Set page title and icon
st.set_page_config(page_title="Potentiam Chatbot", page_icon=":robot_face:")

# Function to display chat messages

# Streamlit app title
st.title('Potentiam Chatbot')

# Main chat loop
while True:
    # User input
    user_input = st.text_input("You:", "")

    # Send button
    if st.button("Send"):
        # Display user message
        result=qa_chain.invoke(user_input)
        response=result['result']
        st.write(response)
