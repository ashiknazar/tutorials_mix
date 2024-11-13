# app.py
import streamlit as st
from model import test_quality

# Create the form
st.title("Wine Quality Testing")

with st.form("wine_quality_form"):
    fixed_acidity = st.number_input('Fixed Acidity')
    volatile_acidity = st.number_input('Volatile Acidity')
    citric_acid = st.number_input('Citric Acid')
    residual_sugar = st.number_input('Residual Sugar')
    chlorides = st.number_input('Chlorides')
    free_sulfur_dioxide = st.number_input('Free Sulfur Dioxide')
    total_sulfur_dioxide = st.number_input('Total Sulfur Dioxide')
    density = st.number_input('Density')
    pH = st.number_input('pH')
    sulphates = st.number_input('Sulphates')
    alcohol = st.number_input('Alcohol')
    
    # Submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        # Call the test_quality function
        quality = test_quality(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
                               chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, 
                               pH, sulphates, alcohol)
        
        st.write(f'The predicted quality of the wine is: {quality}')
