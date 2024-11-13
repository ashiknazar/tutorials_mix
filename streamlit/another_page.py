import streamlit as st

def display_another_page():
    st.title('Another Page with Top Navbar')
    
    nav = st.radio("Navigate", ["Section 1", "Section 2", "Section 3"], horizontal=True)
    
    if nav == "Section 1":
        st.write("Welcome to Section 1")
    elif nav == "Section 2":
        st.write("Welcome to Section 2")
    elif nav == "Section 3":
        st.write("Welcome to Section 3")
