import streamlit as st
import form_page  # Import the form_page module
import home_page  # Import the home_page module
import another_page  # Import the another_page module
import mysql.connector
import os

def main():
    st.title('Sample Website with Form and Navbar')
    
    # Create a navigation bar
    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ('Home', 'Form', 'Another Page'))
    
    if page == 'Home':
        home_page.display_home()  # Call the function to display the home page from home_page.py
        
    elif page == 'Form':
        form_page.display_form()  # Call the function to display the form from form_page.py
        
    elif page == 'Another Page':
        another_page.display_another_page()  # Call the function to display another page from another_page.py

if __name__ == '__main__':
    main()
