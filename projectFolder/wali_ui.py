
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Configure the page
st.set_page_config(page_title="WALi AI", page_icon="🤖")

st.title("🤖 WALi AI Chatbot")
st.caption("Powered by Groq and LangChain")

# Initialize the model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask WALi anything...")

if user_input:
    # Display and store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    try:
        with st.chat_message("assistant"):
            with st.spinner("WALi is thinking..."):
                response = llm.invoke(user_input)
                answer = response.content
                st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error(f"Error: {e}")
