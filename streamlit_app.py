import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from chat import ChatBot
from vector_store import VectorStore


def initialize_streamlit():
    st.set_page_config(page_title="Chat with websites", page_icon="🤖")
    st.title("Chat with websites")
    with st.sidebar:
        st.header("Settings")
        website_url = st.text_input("Website URL")
    return website_url


def manage_chat(website_url):
    if website_url is None or website_url == "":
        st.info("Please enter a website URL")
    else:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                AIMessage(content="Hello, I am a bot. How can I help you?")
            ]
        if "vector_store" not in st.session_state:
            st.session_state.vector_store = VectorStore.get_vectorstore_from_url(
                website_url
            )
        user_query = st.chat_input("Type your message here...")
        if user_query is not None and user_query != "":
            response = ChatBot.get_response(
                user_query, st.session_state.vector_store, st.session_state.chat_history
            )
            st.session_state.chat_history.append(HumanMessage(content=user_query))
            st.session_state.chat_history.append(AIMessage(content=response))
        display_conversation()


def display_conversation():
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
