from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


chat_prompt_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} assistant.'),
    ('human','Explain the {topic} in simple words')
])

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash", temperature=0.5, max_output_tokens=500)

prompt = chat_prompt_template.invoke({'domain':'professor', 'topic':'prompt template'})

response = llm.invoke(prompt)

print(response.text)