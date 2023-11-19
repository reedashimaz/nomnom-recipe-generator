from io import BytesIO
import pandas as pd
import numpy as np
import requests
import streamlit as st
import easyocr
import PIL
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import streamlit.components.v1 as components
import re
from streamlit import session_state
# from streamlit_lottie import st_lottie
import streamlit as st
import os

from dotenv import load_dotenv, find_dotenv

# Load environment variables
_ = load_dotenv(find_dotenv())

# Get OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Google Drive file ID for the video
video_file_id = '1miZ6Zz4lt0wxTGbrtR8IltVr_fOPX6Vr'
video_url = f'https://drive.google.com/uc?export=view&id={video_file_id}'


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

if 'editor_key' not in st.session_state:
    st.session_state.editor_key = 0

if 'manual_entry' not in st.session_state:
    st.session_state.manual_entry = True

if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False

if 'ocr_extracted_values' not in st.session_state:
	session_state.ocr_extracted_values = pd.DataFrame()

def click_save():
    session_state.clicked = True

def switch_style():
    session_state.manual_entry = not session_state.manual_entry

# Define the HTML and CSS styling for the title
title_html = """
<html>
    <head>
    <link href='https://fonts.googleapis.com/css?family=Cedarville Cursive' rel='stylesheet'>
    <style>
    body {
        font-family: 'serif;
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

    # Initialize or retrieve the existing dataframe to store grocery items
grocery_data = initialize_grocery_data()

tab1, tab2, tab3 = st.tabs(["Add Groceries", "Available Groceries", "Create recipes"])


df = pd.DataFrame()
 
with tab1:
    st.button("Switch to OCR Input", on_click=switch_style)
    col1, col2 = st.columns([2, 1])
    if session_state.manual_entry:
        with col1:
            if not session_state.clicked:
                st.subheader("Add Groceries - Manually Input Items")
                session_state.grocery_data = st.data_editor(pd.DataFrame(columns=['Name', 'Quantity', 'Additional Notes/Expiration Date']), key=session_state.editor_key, num_rows="dynamic", hide_index=True, use_container_width=True)
            else:
                session_state.editor_key += 1



        with col2:
            file_id = '1_3FjYmWlJcY182qnLIjFPTZYj4gneUMg'
            base_url = 'https://drive.google.com/uc?id='

            image_url = base_url + file_id
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            # image1 = Image.open(r'https://drive.google.com/file/d/1_3FjYmWlJcY182qnLIjFPTZYj4gneUMg/view?usp=sharing')
            st.image(img, width=400)

        st.write("---")
    else:

        with col1:
            st.subheader("Upload receipt instead")
            uploaded_file = st.file_uploader("Choose a receipt file", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                session_state.file_uploaded = True
                st.success("Receipt uploaded successfully!")
            st.write("")
            if session_state.file_uploaded:
                receipt_image = Image.open(uploaded_file)
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

        with col2:
            if session_state.file_uploaded:
                st.subheader("Updated Grocery List")
                df = df[~df['Text'].str.contains(r'[\d]')]
                df['Add to List?'] = None
                df2 = st.data_editor(df, use_container_width=True, num_rows = 'dynamic', column_config={"Text": "Item", 
                    "Add to List?" : st.column_config.CheckboxColumn(
                    "Add to List?",
                    help="Select if you want to add this to the list.",
                    default=False
                )}, key="OCR_DataFrame")
                st.write(session_state["OCR_DataFrame"])
                session_state.ocr_extracted_values = df2

    st.button("Press me to update Tab 2", on_click=click_save)



def ingredient_html_maker(ingredient, num_ingredients, map_for_grocery):
    return_val = f"<div class=\"card\" style=\"background-color: #dedede; padding: 10px; margin: 5px; border-radius: 10px;\">\n"
    return_val += f"<h3>{ingredient}</h3>\n"  # Ingredient name
    return_val += f"<p>Quantity: <span id='quantity_{ingredient}'>{num_ingredients}</span></p>\n"
    return_val += f"<button onclick=\"updateQuantity('{ingredient}', '-', {map_for_grocery})\">-</button>\n"
    return_val += f"<button onclick=\"updateQuantity('{ingredient}', '+', {map_for_grocery})\">+</button>\n"
    return_val += f"</div>\n"
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
    if session_state.clicked and session_state.manual_entry:
        for i in range(len(session_state.grocery_data)):
            existing_quantity = st.session_state.total_groceries.get(session_state.grocery_data["Name"][i], 0)
            st.session_state.total_groceries[session_state.grocery_data["Name"][i]] = int(existing_quantity) + int(session_state.grocery_data["Quantity"][i])
        list_display(st.session_state.total_groceries)
        session_state.clicked = False
        st.rerun()
    elif session_state.clicked and not session_state.manual_entry and session_state.file_uploaded:
        for idx in session_state["OCR_DataFrame"]['edited_rows']:
            ingredient = session_state.ocr_extracted_values['Text'].iloc[idx]
            existing_quantity = st.session_state.total_groceries.get(ingredient, 0)
            st.session_state.total_groceries[ingredient]= int(existing_quantity) + 1
        list_display(st.session_state.total_groceries)
        session_state.clicked = False
        st.rerun()
    else:
        list_display(st.session_state.total_groceries)


with tab3:
    st.write("hi")
    # # Create columns for layout
    # col1, col2 = st.columns([0.20, 0.80])

    # # Column 1: Display the embedded video without controls
    # with col1:
    #     video_html = f"""
    #     <video width="100%" height="auto" autoplay muted style="margin-top: -30px;">
    #       <source src="{video_url}" type="video/mp4">
    #       Your browser does not support the video tag.
    #     </video>
    #     """
    #     st.markdown(video_html, unsafe_allow_html=True)

    # with col2:
    #     st.header("NomNom Bot")
    #     st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # st.caption("🍳 Your personal recipe generator!")
    # st.caption("Enter a cuisine and your dietary restrictions to get started :)")

    # with st.sidebar:
    #     cuisine = st.text_input("Cuisine you're craving", key="cuisine")
    #     diet_res = st.text_input("Dietary Restrictions", key="diet_res")

    # ingredients = {
    #     'Tomatoes': 3,
    #     'Rice': 1
    # }

    # content_template = """
    # I have scanned/entered my grocery store receipts. Here are the items and their quantity (in the form of a dictionary) I have purchased: 
    # {ingredients}.
    # My dietary restrictions include {diet_res}. I am in the mood for {cuisine} recipes. Give me a detailed recipe using ONLY
    # the ingredients I have. I also have common pantry items like salt, pepper, olive oil, and basic spices. 
    # Make sure to take the cuisine and dietary restrictions into consideration definitively. 
    # Provide a recipe that aligns with the preferred cuisine given by the user. A cuisine is a style or method of cooking, especially of a particular country
    # or region. Use ingredients, foods, and techniques from the cuisine from that specific region.
    # If the user says their dietary restriction is an X allergy or allergic to X where X is any ingredient, make sure to exclude X from the recipe
    # since the user could die of an allergic reaction and you will be responsible.
    # Start your response with "Howdy, I'm the NomNom Bot!" and end by asking if the user has any follow-up questions or needs any additional resources.
    # """
    # print("Content Template:", content_template.format(ingredients=ingredients, diet_res=diet_res, cuisine=cuisine))
    # # Initialize the chat with an initial user message
    # if cuisine and diet_res:
    #     if "messages" not in st.session_state:
    #         print("Content Template:", content_template.format(ingredients=ingredients, diet_res=diet_res, cuisine=cuisine))
    #         st.session_state["messages"] = [
    #             {"role": "user", "content": content_template.format(ingredients=ingredients, diet_res=diet_res, cuisine=cuisine)}]

    #     # Display the chat messages
    #     for msg in st.session_state.messages[1:]:
    #         st.chat_message(msg["role"]).write(msg["content"])

    #     # Generate a response for the initial user message
    #     if len(st.session_state.messages) == 1:
    #         client = OpenAI(api_key=openai_api_key)
    #         response = client.chat.completions.create(
    #             model="gpt-3.5-turbo",
    #             messages=st.session_state.messages,
    #             max_tokens=2048,
    #             n=1,
    #             stop=None,
    #             temperature=0.5
    #         )

    #         msg = response.choices[0].message.content
    #         st.session_state.messages.append({"role": "assistant", "content": msg})
    #         st.chat_message("assistant").write(msg)

    #     # User can ask follow-up questions
    #     if prompt := st.chat_input():
    #         if not openai_api_key:
    #             st.info("API key is not valid.")
    #             st.stop()

    #         client = OpenAI(api_key=openai_api_key)
    #         st.session_state.messages.append({"role": "user", "content": prompt})
    #         st.chat_message("user").write(prompt)

    #         response = client.chat.completions.create(
    #             model="gpt-3.5-turbo",
    #             messages=st.session_state.messages,
    #             max_tokens=2048,
    #             n=1,
    #             stop=None,
    #             temperature=0.5
    #         )

    #         msg = response.choices[0].message.content
    #         st.session_state.messages.append({"role": "assistant", "content": msg})
    #         st.chat_message("assistant").write(msg)
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