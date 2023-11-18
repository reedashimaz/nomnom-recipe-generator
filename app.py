# app.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

title_html = """
    <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
        <h1 style="text-align: center;">Nom Nom</h1>
    </div>
"""

# Display the centered title
st.markdown(title_html, unsafe_allow_html=True)

ingredient_quantities = {}

tab1, tab2, tab3 = st.tabs(["Add Groceries", "Available Groceries", "Create recipes"])

with tab1:
   st.header("Add Groceries")
   
def ingredient_html_maker(ingredient, num_ingredients):
    return_val = f"<div class=\"card\" style=\"background-color: #dedede; padding: 10px; margin: 5px; border-radius: 10px;\">\n"
    return_val += f"<h3>{ingredient}</h3>\n"  # Ingredient name
    return_val += f"<p>Quantity: <span id='quantity_{ingredient}'>{num_ingredients}</span></p>\n"
    return_val += f"<button onclick=\"updateQuantity('{ingredient}', '-')\">-</button>\n"
    return_val += f"<button onclick=\"updateQuantity('{ingredient}', '+')\">+</button>\n"
    return_val += "</div>\n"
    return return_val

with tab2:
    list_of_groceries = {
        "Ingredient 1": 2,
        "Ingredient 2": 1,
        "Ingredient 3": 3,
        "Ingredient 4": 1,
        "Ingredient 5": 2,
        "tomatoes": 5,
        "lettuce": 1,
    }

    javascript_code = """
<script>
    function updateQuantity(ingredient, operation) {
        // Get the current quantity
        var quantityElement = document.getElementById('quantity_' + ingredient);
        var currentQuantity = parseInt(quantityElement.innerText);

        // Update the quantity based on the operation
        if (operation === '+') {
            currentQuantity += 1;
        } else if (operation === '-') {
            currentQuantity = Math.max(0, currentQuantity - 1);
        }

        // Update the quantity display
        quantityElement.innerText = currentQuantity;

        // Communicate with Streamlit app
        Streamlit.setComponentValue(JSON.stringify({ ingredient: ingredient, quantity: currentQuantity }));
    }
</script>
"""

    list_html = ''
    with open('List.html') as list_file:
        list_html = list_file.read()
    
    list_html_without_end = list_html[:-6]
    end = list_html[-6:]
    final_list_html = list_html_without_end + "\n"
    
    for ingredient in list_of_groceries:
        final_list_html += ingredient_html_maker(ingredient, list_of_groceries[ingredient])
    
    final_list_html += "\n" + end
    components.html(final_list_html + javascript_code, height=500)


with tab3:
    st.header("Create recipes")

# Add styling for tabs
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 5px;
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
        color: black;
        font-weight: bold;
    }

    .stTabs [aria-selected="true"] {
        background-color: #F1C0B9;
        color: black;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)
