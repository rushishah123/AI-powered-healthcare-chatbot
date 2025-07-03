"""Minimal Streamlit frontend for the chatbot."""
import streamlit as st
import requests
import os

CHAT_URL = os.getenv('CHAT_URL', 'http://chat-service:5003')

st.title('Healthcare Chatbot')
user_id = st.text_input('User ID', '1')
message = st.text_input('Message')

uploaded_file = st.file_uploader('Upload document')

if st.button('Send'):
    files = {'file': uploaded_file} if uploaded_file else None
    data = {'user_id': user_id, 'message': message}
    resp = requests.post(f'{CHAT_URL}/chat', data=data, files=files)
    st.write(resp.json())
