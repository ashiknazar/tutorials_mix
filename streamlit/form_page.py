import streamlit as st

def display_form():
    st.subheader('Form')
    with st.form(key='my_form'):
        name = st.text_input(label='Enter your name')
        age = st.number_input(label='Enter your age', min_value=0, max_value=120, step=1)
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            st.write(f'Name: {name}')
            st.write(f'Age: {age}')
