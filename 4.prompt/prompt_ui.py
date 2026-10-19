from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b",temperature=0.5)

st.header("Research Tool - Summarization")
user_input = st.text_input("Enter your prompt here:")

if st.button("Summarize"):
    if user_input:
        try:
            response = llm.invoke(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")    