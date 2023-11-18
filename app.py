import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from streamlit import session_state


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

st.set_page_config(layout="wide")


if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'total_groceries' not in st.session_state:
    st.session_state.total_groceries = {}

if 'grocery_data' not in st.session_state:
    st.session_state.grocery_data = pd.DataFrame(columns=['Name', 'Quantity', 'Additional Notes/Expiration Date'])

def click_save():
	session_state.clicked = True

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
ingredient_quantities = {}
# Initialize or retrieve the existing dataframe to store grocery items
#grocery_data = initialize_grocery_data()

tab1, tab2, tab3 = st.tabs(["Add Groceries", "Available Groceries", "Create recipes"])
    
with tab1:
    if not session_state.clicked:
        st.subheader("Add Groceries - Manually Input Items")
         # User input for the grocery item
        session_state.grocery_data = st.data_editor(pd.DataFrame(columns=['Name', 'Quantity', 'Additional Notes/Expiration Date']), key="manual_input", num_rows="dynamic", hide_index=True)
        st.write("---")
        st.subheader("Add Groceries - OCR of Receipt")
        print("Before")
        print(session_state.grocery_data)
        st.button("Press me to update Tab 2", on_click=click_save)
    else:
        st.subheader("Add Groceries - Manually Input Items")
         # User input for the grocery item
        st.data_editor(pd.DataFrame(columns=['Name', 'Quantity', 'Additional Notes/Expiration Date']), num_rows="dynamic", hide_index=True)
        st.write("---")
        st.subheader("Add Groceries - OCR of Receipt")
        print("Before")
        print(session_state.grocery_data)
        st.button("Press me to update Tab 2", on_click=click_save)


   







def ingredient_html_maker(ingredient, num_ingredients, map_for_grocery):
    return_val = f"<div class=\"card\" style=\"background-color: #dedede; padding: 10px; margin: 5px; border-radius: 10px;\">\n"
    return_val += f"<h3>{ingredient}</h3>\n"  # Ingredient name
    return_val += f"<p>Quantity: <span id='quantity_{ingredient}'>{num_ingredients}</span></p>\n"
    return_val += f"<button onclick=\"updateQuantity('{ingredient}', '-', {map_for_grocery})\">-</button>\n"
    return_val += f"<button onclick=\"updateQuantity('{ingredient}', '+', {map_for_grocery})\">+</button>\n"
    return_val += "</div>\n"
    return return_val

def list_display(total_groceries):
    list_html = ''
    with open('List.html') as list_file:
        list_html = list_file.read()
    
    list_html_without_end = list_html[:-6]
    end = list_html[-6:]
    final_list_html = list_html_without_end + "\n"

    for item in total_groceries:
        final_list_html += ingredient_html_maker(item, total_groceries[item], total_groceries)
    
    final_list_html += "\n" + end

    return components.html(final_list_html + javascript_code, height=500)



with tab2: 
    javascript_code = """
<script>
    function updateQuantity(ingredient, operation, grocery_data) {
        // Get the current quantity
        var quantityElement = document.getElementById('quantity_' + ingredient);
        var currentQuantity = parseInt(quantityElement.innerText);

        // Update the quantity based on the operation
        if (operation === '+') {
            currentQuantity += 1;
        } else if (operation === '-') {
            currentQuantity = Math.max(0, currentQuantity - 1);
        }
		grocery_data[ingredient] = currentQuantity;
        console.log(grocery_data);
        // Update the quantity display
        quantityElement.innerText = currentQuantity;
    }
</script>
"""
    if session_state.clicked:
        for i in range(len(session_state.grocery_data)):
            existing_quantity = st.session_state.total_groceries.get(session_state.grocery_data["Name"][i], 0)
            st.session_state.total_groceries[session_state.grocery_data["Name"][i]] = existing_quantity + int(session_state.grocery_data["Quantity"][i])
        print(st.session_state.total_groceries)
        list_display(st.session_state.total_groceries)
        session_state.clicked = False








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

