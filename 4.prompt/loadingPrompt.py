from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b",temperature=0.5)

st.header("Research Tool - Summarization")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# load the prompt template from the saved JSON file
template = load_prompt("template.json")

#fill the placeholders in the template with user inputs
prompt = template.invoke({'paper_input': paper_input, 'style_input': style_input, 'length_input': length_input})

if st.button("Summarize"):
    if paper_input and style_input and length_input:
        try:
            response = llm.invoke(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")