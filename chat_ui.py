import time
import requests
import streamlit as st

def get_rasa_bot_response(user_query):
    data = {
        "sender": "dhruv",
        "message": user_query
    }

    response = requests.post('http://localhost:5005/webhooks/rest/webhook', json=data)
    print(response.status_code)
    print(response.json())

    bot_resp = response.json()[0]['text']

    return bot_resp


def ai_response_writer(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.07)


st.title("RAG Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_rasa_bot_response(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write_stream(ai_response_writer(response))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})