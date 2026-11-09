from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model  = ChatGroq(model="openai/gpt-oss-20b",temperature=0.5)

template1 = PromptTemplate(
    template = 'Write a detailed repot on {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Write a summery about that text./n {text}',
    input_variables=['text']
)

prompt1  = template1.invoke({'topic':'Artificial Intelligence'})
response1 = model.invoke(prompt1)

promt2 = template2.invoke({'text':response1.text})
response2 = model.invoke(promt2)
print(response2.text)


