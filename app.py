

# app.py
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

title_html = """
    <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
        <h1 style="text-align: center;">Nom Nom</h1>
    </div>
"""

# Display the centered title
st.markdown(title_html, unsafe_allow_html=True)


tab1, tab2, tab3 = st.tabs(["Add Groceries", "Available Groceries", "Create recipes"])

with tab1:
   st.header("Add Groceries")
   

with tab2:
   st.header("Available Groceries")
   

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
