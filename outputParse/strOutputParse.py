from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model  = ChatGroq(model="openai/gpt-oss-20b",temperature=0.5)

#template1
template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables = ['topic']
)

#template2
template2 = PromptTemplate(
    template = 'Write 5 line summary about that text.\n {text}',
    input_variables=['text']
)

parse = StrOutputParser()

chain = template1 | model | parse | template2 |model | parse

response = chain.invoke({'topic':'Artificial Intelligence'})
print(response)