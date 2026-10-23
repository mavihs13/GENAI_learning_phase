from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} assistant.'),
    ('human', 'Explain the {topic} in simple words, with examples')
])

llm = ChatGroq(
    model="openai/gpt-oss-20b", temperature=0.5)

domain = input("Enter the assistant domain: ")
topic = input("Enter the topic to explain: ")
try:
    domain = domain.strip()
    topic = topic.strip()
    if not domain or not topic:
        raise ValueError("Domain and topic cannot be empty.")
except ValueError as e:
    print(f"Error: {e}")
else:
    prompt = template.invoke({'domain': domain, 'topic': topic})
    response = llm.invoke(prompt)
    print("Response by your assistant:\n", response.text)
