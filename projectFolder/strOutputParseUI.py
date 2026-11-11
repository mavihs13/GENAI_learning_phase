
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="AI Report Generator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Report Generator")
st.write("Enter a topic to generate a detailed report and its 5-line summary.")

# Initialize model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

# Template 1: Generate detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Template 2: Generate summary
template2 = PromptTemplate(
    template="Write a 5-line summary about the following text:\n{text}",
    input_variables=["text"]
)

# Output parser
parse = StrOutputParser()

# LangChain pipeline
chain = template1 | model | parse | template2 | model | parse

# User input
topic = st.text_input(
    "Enter your topic:",
    placeholder="e.g. Artificial Intelligence"
)

# Generate button
if st.button("Generate Report", type="primary"):

    if topic.strip():

        with st.spinner("Generating report and summary..."):

            try:
                # Invoke chain with user input
                response = chain.invoke({"topic": topic})

                st.success("Report generated successfully!")

                st.subheader("📝 5-Line Summary")
                st.write(response)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

    else:
        st.warning("Please enter a topic first.")
