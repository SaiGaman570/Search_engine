from agent import get_response
import streamlit as st
import random
import time
from agent import get_response

st.title("hello world")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
# Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})