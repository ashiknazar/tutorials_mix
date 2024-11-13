import streamlit as st

def display_home():
    st.write('Welcome to the Home page!')
    st.write('Use the sidebar to navigate.')
    
    if st.button('Add Text'):
        append_text()  # Call the function to append text

    if st.button('Go to Another Page'):
        st.session_state.page = 'Another Page'  # Set the session state to navigate to another page

def append_text():
    st.write('Additional text data appended!')
