
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Create the prompt template
template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} assistant."),
    ("human", "Explain the {topic} in simple words, with examples.")
])

# App heading
st.title("🤖 AI Assistant")
st.write("Ask anything and get simple explanations with examples.")

st.info(
    "This app uses LangChain and Groq to generate "
    "explanations based on your chosen domain and topic."
)

# Input form
with st.form("assistant_form"):
    domain = st.text_input(
        "Assistant Domain",
        placeholder="e.g. Computer Science Professor"
    )

    topic = st.text_input(
        "Topic to Explain",
        placeholder="e.g. Prompt Templates"
    )

    submitted = st.form_submit_button(
        "✨ Get Explanation",
        use_container_width=True
    )

# Process user input
if submitted:
    domain = domain.strip()
    topic = topic.strip()

    if not domain or not topic:
        st.warning("Please enter both the domain and topic.")

    else:
        try:
            with st.spinner("Generating your explanation..."):

                # Fill the prompt template
                prompt = template.invoke({
                    "domain": domain,
                    "topic": topic
                })

                # Initialize Groq model
                llm = ChatGroq(
                    model="openai/gpt-oss-20b",
                    temperature=0.5
                )

                # Get the model response
                response = llm.invoke(prompt)

            st.success("Explanation generated successfully!")

            st.subheader("📘 Response by Your Assistant")
            st.markdown(response.content)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
