from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai_api_key = os.getenv('OPENAI_API_KEY')

print(openai_api_key)

st.title("💬 Recipe Bot")
st.caption("🚀 Here's a recipe ")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Here's a recipe suggestion! How else can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please enter API key again bruh")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    chatbot_prompt = """
    As an advanced chatbot, your primary goal is to assist users to the best of your ability. This involves generating recipes by 
    taking in the ingredients from a grocery store receipt, dietary restrictions and cuisine preferences and producing a response in 
    a format that includes the ingredients and cooking steps.

    <conversation_history>

    User: I have scanned/entered my grocery store receipts. Here are the items I have purchased: [Tomato sauce, pasta]
    User: My dietary restrictions include vegetarian.
    User: I am in mood for Italian recipes.
    Chatbot:
    """

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
