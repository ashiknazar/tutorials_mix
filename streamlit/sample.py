
import streamlit as st

def main():
    st.title('Sample Website with Form and Navbar')
    
    # Create a navigation bar
    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ('Home', 'Form'))
    
    if page == 'Home':
        st.write('Welcome to the Home page!')
        st.write('Use the sidebar to navigate.')
        
    elif page == 'Form':
        st.subheader('Form')
        with st.form(key='my_form'):
            name = st.text_input(label='Enter your name')
            age = st.number_input(label='Enter your age', min_value=0, max_value=120, step=1)
            submit_button = st.form_submit_button(label='Submit')
            
            if submit_button:
                st.write(f'Name: {name}')
                st.write(f'Age: {age}')
    
if __name__ == '__main__':
    main()
