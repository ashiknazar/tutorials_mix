import streamlit as st


st.title("Python front end tasks")

st.header("Data science tutorial") 

st.subheader('pandas tutorial')

st.text("Pandas is a powerful and widely-used open-source data analysis and manipulation library for Python. It provides easy-to-use data structures and data analysis tools designed to make data cleaning, transformation, and analysis fast and intuitive. Here's a detailed description of pandas:")

import streamlit as st

st.markdown("""
### Key Features of Pandas:

1. **DataFrame and Series**:
   - **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types. It's similar to a spreadsheet or SQL table, and it can handle both rows and columns of data.
   - **Series**: A one-dimensional labeled array capable of holding data of any type (integer, string, float, Python objects, etc.).

2. **Data Handling**:
   - **Reading and Writing Data**: Pandas can read data from various file formats such as CSV, Excel, SQL databases, and more. It can also write data back to these formats.
   - **Indexing and Selecting Data**: Pandas provides powerful indexing and selection capabilities to subset, filter, and manipulate data efficiently.

3. **Data Operations**:
   - **Data Cleaning**: Handling missing data (`NaN` values), converting data types, and removing duplicates.
   - **Data Transformation**: Applying functions to data, reshaping data (e.g., pivoting, melting), and merging and joining datasets.

4. **Time Series Analysis**:
   - Pandas has extensive support for working with time series data. It includes features for date/time indexing, resampling, and time zone handling.

5. **Performance and Efficiency**:
   - Pandas is optimized for performance, making it suitable for handling large datasets and complex data operations efficiently.

6. **Integration with Other Libraries**:
   - Pandas integrates well with other Python libraries such as NumPy (for numerical computations) and Matplotlib/Seaborn (for data visualization).
""")

from PIL import Image
img = Image.open("5853.jpg")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

name = st.text_input("Enter Your name", "Type Here ...")

if(st.button('Submit')):
    result = name.title()
    st.success(result)

status = st.radio("Select Gender: ", ('Male', 'Female'))

if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

if st.checkbox("Know pandas?"):
 
    # display the text if the checkbox returns True value
    st.text("thats nice")


hobby = st.selectbox("favourite language: ",
                     ['java', 'python', 'c++'])
 
# print the selected hobby
st.write("Your fav is: ", hobby)


langs = st.multiselect("libraries already know: ",
                         ['pandas', 'numpy', 'scikit'])
 
# write the selected options
st.write("You selected", len(langs), 'pandas')


level = st.slider("Select the python knowledge level", 1, 5)
 
st.text('Selected: {}'.format(level))


 

if(st.button("Register")):
    st.text("Welcome To Pandas !!!")