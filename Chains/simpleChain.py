from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "write a summary about {topic}",
    input_variables = ['topic']
)

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)

chain = prompt | model | parser

result = chain.invoke({"topic":'Generative AI'})

print(result)

chain.get_graph().print_ascii();