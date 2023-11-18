import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def initialize_grocery_data():
    return pd.DataFrame(columns=['Name', 'Quantity', 'Additional Notes/Expiration Date'])

def manually_input_items(grocery_data):
    return grocery_data

def upload_receipt():
    st.header("Upload Receipt")
    uploaded_file = st.file_uploader("Choose a receipt file", type=["jpg", "jpeg", "png", "pdf"])
    if uploaded_file is not None:
        st.success("Receipt uploaded successfully!")
        # Add your code here for processing the uploaded receipt

def main():
    st.set_page_config(layout="wide")

    # Define the HTML and CSS styling for the title
    title_html = """
    <html>
    <head>
    <link href='https://fonts.googleapis.com/css?family=Cedarville Cursive' rel='stylesheet'>
    <style>
    body {
        font-family: 'Cedarville Cursive';font-size: 22px;
        font-size: 22px;
    	text-align: center;
    }
    h1 {
        font-family: 'Cedarville Cursive';
        font-size: 56px;
    	display: inline-block;
    }
    </style>
    </head>
    <body>
    <h1>Nom Nom!</h1>
    </body>
    </html>
    """

    # Use st.markdown to display the title with the specified font
    st.markdown(title_html, unsafe_allow_html=True)
    
    caption_html = """
    <div style="display: flex; justify-content: center; align-items: center; font-style: italic; font-weight: bold;">
        <p>Helping College Students Keep Track of Groceries</p>
    </div>
	"""
	
    st.markdown(caption_html, unsafe_allow_html=True)


    # Initialize or retrieve the existing dataframe to store grocery items
    grocery_data = initialize_grocery_data()

    tab1, tab2, tab3 = st.tabs(["Add Groceries", "Available Groceries", "Create recipes"])

    with tab1:
        st.subheader("Add Groceries - Manually Input Items")
        # User input for the grocery item
        grocery_data = st.data_editor(grocery_data, num_rows="dynamic", hide_index=True)
        st.write("---")
        st.subheader("Add Groceries - OCR of Receipt")


    with tab2:
        st.header("Available Groceries")
        st.table(grocery_data)  # Display the overall grocery list

    with tab3:
        st.header("Create recipes")

    st.markdown("""
    <style>
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            width: 100%;
            white-space: pre-wrap;
            background-color: #F1C0B9;
            border-radius: 4px 4px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
            color: black; /* Added this line to set the text color */
            font-weight: bold; /* Added this line to make the text bold */
        }

        .stTabs [aria-selected="true"] {
            background-color: #F1C0B9;
            color: black;
            font-weight: bold; /* Added this line to make the text bold */
        }

    </style>""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()