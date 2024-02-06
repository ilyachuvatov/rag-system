from streamlit_app import initialize_streamlit, manage_chat

if __name__ == "__main__":
    website_url = initialize_streamlit()
    manage_chat(website_url)
