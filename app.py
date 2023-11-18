<<<<<<< Updated upstream
import streamlit as st
import pandas as pd
import numpy as np
=======
import pandas as pd
import numpy as np
import streamlit as st
import easyocr
import PIL
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import streamlit.components.v1 as components
import re

>>>>>>> Stashed changes

@st.cache_data
def initialize_grocery_data():
    return pd.DataFrame(columns=['Name', 'Quantity', 'Additional Notes/Expiration Date'])

def manually_input_items(grocery_data):
    return grocery_data

<<<<<<< Updated upstream
def upload_receipt():
    st.header("Upload Receipt")
    uploaded_file = st.file_uploader("Choose a receipt file", type=["jpg", "jpeg", "png", "pdf"])
    if uploaded_file is not None:
        st.success("Receipt uploaded successfully!")
        # Add your code here for processing the uploaded receipt

def main():
    st.set_page_config(layout="wide")
=======
st.set_page_config(layout="wide")
>>>>>>> Stashed changes

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
        margin_bottom: 3px;
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
        <p>Helping College Students Manage Their Groceries</p>
    </div>
	"""
	
    st.markdown(caption_html, unsafe_allow_html=True)


<<<<<<< Updated upstream
    # Initialize or retrieve the existing dataframe to store grocery items
    grocery_data = initialize_grocery_data()

    tab1, tab2, tab3 = st.tabs(["Add Groceries", "Available Groceries", "Create recipes"])
=======
ingredient_quantities = {}
# Initialize or retrieve the existing dataframe to store grocery items
grocery_data = initialize_grocery_data()
df = pd.DataFrame()

tab1, tab2, tab3 = st.tabs(["Add Groceries", "Available Groceries", "Create recipes"])
    
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Add Groceries")
        st.write("You can manually input your groceries below or scroll down to upload a grocery receipt!")
        grocery_data = st.data_editor(grocery_data, num_rows="dynamic", hide_index=True, use_container_width=True)
        
        # User input for the grocery item
        
    
    with col2:
        image1 = Image.open('picture1forwebsite.png')
        st.image(image1, width=400)
    
    st.write("---")
    
    col3, col4 = st.columns([1, 1.5])
with col3:
    st.subheader("Upload receipt instead")
    uploaded_file = st.file_uploader("Choose a receipt file", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.success("Receipt uploaded successfully!")
    st.write("")

    receipt_image = Image.open('testreceipt1.jpeg')
    st.image(receipt_image)
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(np.array(receipt_image))

    text_list = []
    confidence_list = []

    for idx in range(len(result)):
        pred_coor = result[idx][0]
        pred_text = result[idx][1]
        pred_confidence = result[idx][2]

        text_list.append(pred_text)
        confidence_list.append(pred_confidence)

    df = pd.DataFrame({'Text': text_list, 'Confidence': confidence_list})   

    with col4:
        st.subheader("Updated Grocery List")
        df = df[~df['Text'].str.contains(r'[\d]')]
        st.table(df)

        


def ingredient_html_maker(ingredient, num_ingredients):
    return_val = f"<div class=\"card\" style=\"background-color: #dedede; padding: 10px; margin: 5px; border-radius: 10px;\">\n"
    return_val += f"<h3>{ingredient}</h3>\n"  # Ingredient name
    return_val += f"<p>Quantity: <span id='quantity_{ingredient}'>{num_ingredients}</span></p>\n"
    return_val += f"<button onclick=\"updateQuantity('{ingredient}', '-')\">-</button>\n"
    return_val += f"<button onclick=\"updateQuantity('{ingredient}', '+')\">+</button>\n"
    return_val += "</div>\n"
    return return_val
>>>>>>> Stashed changes

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