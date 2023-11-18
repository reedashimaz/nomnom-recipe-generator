from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai_api_key = os.getenv('OPENAI_API_KEY')

st.title("💬 NomNom Bot")
st.caption("🚀 Your personal recipe generator!")
st.caption("Enter a cuisine and your dietary restrictions to get started :)")

with st.sidebar:
    cuisine = st.text_input("Cuisine you're craving", key="cuisine")
    diet_res = st.text_input("Dietary Restrictions", key = "diet_res")

ingredients = {
    'Tomatoes' : 3,
    'Rice' : 1
}

content_template = """
I have scanned/entered my grocery store receipts. Here are the items and their quantity (in the form of a dictionary) I have purchased: 
{ingredients}.
My dietary restrictions include {diet_res}. I am in the mood for {cuisine} recipes. Give me a detailed recipe using ONLY
the ingredients I have. I also have common pantry items like salt, pepper, olive oil, and basic spices. Make sure to take the 
cuisine and dietary restructions into consideration definitively. Start your response with
"Howdy, I'm the NomNom Bot!" and end by asking if the user has any follow-up questions or needs any additional resources.
"""

# Initialize the chat with an initial user message
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "user", "content": content_template.format(ingredients=ingredients, diet_res=diet_res, cuisine=cuisine)}]

# Display the chat messages
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# Generate a response for the initial user message
if cuisine and diet_res:
    if len(st.session_state.messages) == 1:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=st.session_state.messages,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5
        )

        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

# User can ask follow-up questions
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("API key is not valid.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=st.session_state.messages,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )

    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
